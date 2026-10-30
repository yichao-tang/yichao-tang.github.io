"""Compare the rendered bibliography with its original Markdown source.

Usage: python _tools/check_publications.py /path/to/built/site
No third-party Python packages are required.
"""

import html
import json
from datetime import date
from html.parser import HTMLParser
from pathlib import Path
import re
import sys


ROOT = Path(__file__).resolve().parents[1]
APPROVED_ORDER = (
    "qs-qim-rrw", "jpeg-joca", "stylesign", "dnlmark", "slmark", "genptw",
    "frpcet-rrw", "stdm-rrw", "pht-rrw", "pzms-rrw", "dmspso-gd-ijcini",
    "dms-pio-ijcsm", "dmspso-el-ssci", "dms-gpso-computing",
    "dmspso-el-access", "dms-gpso-cec", "fapso-jocs",
)
HOME_ORDER = ("qs-qim-rrw", "dnlmark", "genptw", "frpcet-rrw", "stdm-rrw")
YEAR_GROUPS = ("2026", "2025", "2024", "2023", "2022", "2021", "2020", "2019", "2018")


def plain_markdown(value):
    """Remove only formatting/escapes used by the original citations."""
    value = value.replace("**", "")
    value = re.sub(r"\\([*#&])", r"\1", value)
    return " ".join(html.unescape(value).split())


def source_entries(language="en", filename="_pages/includes/pub_short.md"):
    source = (ROOT / filename).read_text(encoding="utf-8")
    translations = json.loads((ROOT / "_data/publication_translations.json").read_text(encoding="utf-8"))
    result = []
    for line in source.splitlines():
        if not line.startswith("- "):
            continue
        fields = line[2:].split('"')
        if len(fields) != 3:
            raise ValueError("Unexpected publication format: " + line)
        authors, title, details = fields
        paper = re.search(r"\[\*\*\[Link\]\*\*\]\(([^)]+)\)", details)
        code = re.search(r"\[\*\*\[Code\]\*\*\]\(([^)]+)\)", details)
        if not paper:
            raise ValueError("Missing original Paper link: " + line)
        venue = details[:paper.start()].strip()
        if not re.search(r", \d{4}\.$", venue):
            raise ValueError("Missing original venue/year: " + line)
        result.append({
            "title": title.strip(),
            "authors": plain_markdown(authors),
            # The display uses metadata separators rather than a citation's
            # terminal full stop; retain every venue word and the exact year.
            "venue": plain_markdown(venue)[:-1],
            "paper": paper.group(1),
            "code": code.group(1) if code else None,
        })
        translation = translations.get(paper.group(1), {}).get(language)
        if translation:
            for field in ("title", "authors", "venue"):
                result[-1][field] = plain_markdown(translation[field])
    return result


def publication_chronology():
    """Validate the approved ordering separately from the citation text."""
    records = json.loads((ROOT / "_data/publication_chronology.json").read_text(encoding="utf-8"))
    if tuple(row["id"] for row in records) != APPROVED_ORDER:
        raise ValueError("Publication chronology differs from the approved 17-paper order.")
    urls = [row["paper_url"] for row in records]
    originals = source_entries()
    by_url = {entry["paper"]: entry for entry in originals}
    if len(by_url) != len(originals) or len(set(urls)) != len(urls) or set(urls) != set(by_url):
        raise ValueError("Chronology must reference each original citation URL exactly once.")
    known_dates, unknown_ids, groups = [], [], []
    for row in records:
        publication_date = row["sort_date"]
        group = str(row["group_year"])
        if bool(row.get("earlier", False)) != (row["id"] == "fapso-jocs"):
            raise ValueError("Only the undated JoCS paper should use the 'or earlier' label.")
        if publication_date is None:
            unknown_ids.append(row["id"])
            if group != "2018":
                raise ValueError("The undated JoCS paper must remain in the 2018-or-earlier group.")
        else:
            parsed = date.fromisoformat(publication_date)
            if parsed.isoformat() != publication_date or str(parsed.year) != group:
                raise ValueError("Invalid chronology date or year group: " + row["id"])
            known_dates.append(parsed)
        if not groups or groups[-1] != group:
            groups.append(group)
        citation_year = re.search(r", (\d{4})$", by_url[row["paper_url"]]["venue"])
        if not citation_year or int(citation_year.group(1)) != int(row["citation_year"]):
            raise ValueError("Chronology changed a citation's documented year: " + row["id"])
    if known_dates != sorted(known_dates, reverse=True):
        raise ValueError("Known publication/platform dates are not in descending order.")
    if unknown_ids != ["fapso-jocs"]:
        raise ValueError("Keep the unresolved JoCS date null; all other dates must be documented.")
    if tuple(groups) != YEAR_GROUPS:
        raise ValueError("Publication year groups are missing, repeated or out of order.")
    return records


def chronologically_ordered_entries(language="en"):
    by_url = {entry["paper"]: entry for entry in source_entries(language)}
    return [by_url[row["paper_url"]] for row in publication_chronology()]


class PublicationParser(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.entries = []
        self.current = None
        self.field = None

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        classes = attrs.get("class", "").split()
        if tag == "article" and "publication-list__entry" in classes:
            self.current = {"title": "", "authors": "", "venue": "",
                            "paper": None, "code": None}
        if self.current is None:
            return
        if tag == "h3":
            self.field = "title"
        elif tag == "p":
            if "publication-list__authors" in classes:
                self.field = "authors"
            elif "publication-list__venue" in classes:
                self.field = "venue"
            else:
                self.field = None
        elif tag == "a":
            url = attrs.get("href", "")
            if self.field == "title":
                self.current["paper"] = url
            elif url.startswith("https://github.com/"):
                self.current["code"] = url
        elif tag == "span" and "publication-metric" in classes:
            self.field = None

    def handle_data(self, data):
        if self.current is not None and self.field:
            self.current[self.field] += data

    def handle_endtag(self, tag):
        if tag in ("h3", "p"):
            self.field = None
        elif tag == "article" and self.current is not None:
            for key in ("title", "authors", "venue"):
                self.current[key] = " ".join(self.current[key].split())
            self.entries.append(self.current)
            self.current = None


def main():
    if len(sys.argv) != 2:
        raise SystemExit(__doc__)
    output = Path(sys.argv[1]) / "publications/index.html"
    rendered = output.read_text(encoding="utf-8")
    parser = PublicationParser()
    parser.feed(rendered)
    expected = chronologically_ordered_entries()
    if parser.entries != expected:
        for index, (before, after) in enumerate(zip(expected, parser.entries), 1):
            if before != after:
                print(f"Mismatch in publication {index}:")
                print("SOURCE:", before)
                print("BUILT: ", after)
        raise SystemExit(
            f"Bibliography mismatch: {len(expected)} source entries, "
            f"{len(parser.entries)} rendered entries."
        )
    if "# Equal contribution. * Corresponding author." not in rendered:
        raise SystemExit("Contribution/corresponding-author legend is missing.")
    if r"\&amp;" in rendered or r"\& Security" in rendered:
        raise SystemExit("The CRESS escaped ampersand is still visible.")
    if "JCI percentile:" in rendered or "JIF percentile:" not in rendered:
        raise SystemExit("The approved JIF percentile display was replaced or removed.")
    code_count = sum(entry["code"] is not None for entry in expected)
    print(
        f"PASS: {len(expected)} publications match source titles, authors, "
        f"venues/years and Paper links in approved chronological order; "
        f"{code_count} Code links preserved; JIF percentile labels retained."
    )


if __name__ == "__main__":
    main()
