"""Compare the rendered bibliography with its original Markdown source.

Usage: python _tools/check_publications.py /path/to/built/site
No third-party Python packages are required.
"""

import html
import json
from html.parser import HTMLParser
from pathlib import Path
import re
import sys


ROOT = Path(__file__).resolve().parents[1]


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
    expected = source_entries()
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
    code_count = sum(entry["code"] is not None for entry in expected)
    print(
        f"PASS: {len(expected)} publications match source titles, authors, "
        f"venues/years and Paper links; {code_count} Code links preserved."
    )


if __name__ == "__main__":
    main()
