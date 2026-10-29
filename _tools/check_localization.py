"""Check bilingual routes and preserved academic content using only stdlib.

Usage: python _tools/check_localization.py BUILT_SITE [--baseurl /preview]
"""

import argparse
from html.parser import HTMLParser
from pathlib import Path
import re

from check_publications import PublicationParser, ROOT, source_entries


def require(condition, message):
    if not condition:
        raise ValueError(message)


def compact(text):
    return " ".join(text.split())


def chinese(text):
    return bool(re.search(r"[\u4e00-\u9fff]", text))


class Page(HTMLParser):
    """Read the actual navigation, selected papers and profile sections."""

    def __init__(self, path):
        super().__init__(convert_charrefs=True)
        self.lang, self.canonical, self.alternates = "", [], []
        self.nav, self.nav_current, self.switch = [], [], []
        self.nav_scope = None
        self.content_depth = 0
        self.paragraph, self.paragraphs = None, []
        self.paper, self.paper_field, self.papers = None, None, []
        self.section, self.item = None, None
        self.sections = {key: [] for key in ("-projects", "-awards", "-education")}
        self.html = path.read_text(encoding="utf-8")
        self.feed(self.html)

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        classes = attrs.get("class", "").split()
        if tag == "html":
            self.lang = attrs.get("lang", "")
        elif tag == "link":
            rel = attrs.get("rel", "").split()
            if "canonical" in rel:
                self.canonical.append(attrs.get("href"))
            elif "alternate" in rel and attrs.get("hreflang"):
                self.alternates.append((attrs["hreflang"], attrs.get("href")))
        elif tag == "nav":
            self.nav_scope = ("main" if attrs.get("id") == "site-nav"
                              else "switch" if "language-switch" in classes else None)
        elif tag == "section":
            if self.content_depth or "page__content" in classes:
                self.content_depth += 1
        if tag == "a":
            href = attrs.get("href", "")
            if self.nav_scope == "main":
                self.nav.append(href)
                if attrs.get("aria-current") == "page":
                    self.nav_current.append(href)
            elif self.nav_scope == "switch":
                self.switch.append((href, attrs.get("lang"), attrs.get("hreflang")))
            if self.paragraph is not None:
                self.paragraph["links"].append(href)
            if self.item is not None:
                self.item["links"].append(href)
        if self.content_depth:
            if tag in ("h1", "h2") and attrs.get("id") in self.sections:
                self.section = attrs["id"]
            elif tag == "li" and self.section:
                self.item = {"text": "", "links": []}
            elif tag == "p":
                self.paragraph = {"text": "", "links": [],
                                  "inside_paper": self.paper is not None}
        if tag == "article" and "selected-publication" in classes:
            self.paper = {key: "" for key in
                          ("title", "title_url", "authors", "venue", "summary", "image", "image_full", "alt")}
            self.paper["links"] = []
        if self.paper is not None:
            if tag == "h2":
                self.paper_field = "title"
            elif tag == "p":
                self.paper_field = next(
                    (key for key in ("authors", "venue", "summary", "links")
                     if "selected-publication__" + key in classes), None)
            elif tag == "img":
                self.paper["image"], self.paper["alt"] = attrs.get("src", ""), attrs.get("alt", "")
            elif tag == "a":
                if "selected-publication__figure-link" in classes:
                    self.paper["image_full"] = attrs.get("href", "")
                elif self.paper_field == "title":
                    self.paper["title_url"] = attrs.get("href", "")
                elif self.paper_field == "links":
                    self.paper["links"].append(attrs.get("href", ""))

    def handle_data(self, data):
        if self.paragraph is not None:
            self.paragraph["text"] += data
        if self.item is not None:
            self.item["text"] += data
        if self.paper is not None and self.paper_field in ("title", "authors", "venue", "summary"):
            self.paper[self.paper_field] += data

    def handle_endtag(self, tag):
        if tag == "nav":
            self.nav_scope = None
        elif tag == "section" and self.content_depth:
            self.content_depth -= 1
        elif tag == "li" and self.item is not None:
            self.item["text"] = compact(self.item["text"])
            self.sections[self.section].append(self.item)
            self.item = None
        elif tag == "p" and self.paragraph is not None:
            self.paragraph["text"] = compact(self.paragraph["text"])
            self.paragraphs.append(self.paragraph)
            self.paragraph = None
        if tag in ("p", "h2"):
            self.paper_field = None
        elif tag == "article" and self.paper is not None:
            for key in ("title", "authors", "venue", "summary"):
                self.paper[key] = compact(self.paper[key])
            self.papers.append(self.paper)
            self.paper = None


def source_lines(filename):
    text = (ROOT / "_pages/includes" / filename).read_text(encoding="utf-8")
    text = re.sub(r"<!--.*?-->", "", text, flags=re.S)
    return [line[2:] for line in text.splitlines() if line.startswith("- ")]


def date_range(text):
    match = re.search(r"(\d{4}\.\d{2})\s*[-–]\s*(\d{4}\.\d{2})", text)
    return match.groups() if match else None


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("built_site", type=Path)
    parser.add_argument("--baseurl", default="")
    args = parser.parse_args()
    prefix = "/" + args.baseurl.strip("/") if args.baseurl.strip("/") else ""
    config = (ROOT / "_config.yml").read_text(encoding="utf-8")
    site_url = re.search(r'^url\s*:\s*["\']?([^"\'\s#]+)', config, re.M)
    email = re.search(r'^\s+email\s*:\s*["\']?([^"\'\s#]+)', config, re.M)
    require(site_url and email, "Cannot read configured site URL or email.")
    origin, mailto = site_url.group(1).rstrip("/"), "mailto:" + email.group(1)
    routes = {"home": ("/", "/zh/"),
              "publications": ("/publications/", "/zh/publications/"),
              "about": ("/about/", "/zh/about/")}
    pages = {}
    for key, pair in routes.items():
        for index, route in enumerate(pair):
            language = ("en", "zh-CN")[index]
            page = Page(args.built_site / route.strip("/") / "index.html")
            pages[key, index] = page
            require(page.lang == language, f"{route}: wrong html lang.")
            expected_nav = [prefix + routes[name][index] for name in routes]
            require(page.nav == expected_nav, f"{route}: navigation crosses languages or loses a main link.")
            require(page.nav_current == [prefix + route], f"{route}: wrong current-page navigation.")
            other = ("en", "zh-CN")[1 - index]
            require(page.switch == [(prefix + pair[1 - index], other, other)],
                    f"{route}: language switch does not point to its counterpart.")
            require(page.canonical == [origin + prefix + route], f"{route}: canonical is not self-referencing.")
            expected_alternates = {"en": origin + prefix + pair[0],
                                   "zh-CN": origin + prefix + pair[1],
                                   "x-default": origin + prefix + pair[0]}
            require(len(page.alternates) == 3 and dict(page.alternates) == expected_alternates,
                    f"{route}: incorrect or duplicate hreflang counterparts.")

    expected = source_entries()
    require(len(expected) == 15, "The original bibliography must still contain 15 publications.")
    for index in (0, 1):
        publications = PublicationParser()
        publications.feed(pages["publications", index].html)
        require(publications.entries == expected,
                f"{routes['publications'][index]}: original bibliography fields or order changed.")

    homes = [pages["home", index] for index in (0, 1)]
    require(all(len(page.papers) == 5 for page in homes), "Both Home pages must contain five selected papers.")
    for before, after in zip(homes[0].papers, homes[1].papers):
        for key in ("title", "title_url", "authors", "venue", "links", "image", "image_full"):
            require(before[key] == after[key], f"Selected paper differs between languages: {key}, {before['title']}")
        require(before["image"].startswith(prefix + "/images/") and
                before["image_full"].startswith(prefix + "/images/"),
                f"Selected paper image ignores the base URL prefix: {before['title']}")
        require(after["summary"] and chinese(after["summary"]),
                f"Selected paper has no Chinese summary: {after['title']}")
        require(after["alt"] and chinese(after["alt"]),
                f"Selected paper has no Chinese alternative text: {after['title']}")
    for index, page in enumerate(homes):
        contact = [p for p in page.paragraphs if mailto in p["links"] and not p["inside_paper"]]
        require(len(contact) == 1 and contact[0]["links"] == [mailto],
                f"{routes['home'][index]}: contact email is not in its own content paragraph.")

    abouts = [pages["about", index] for index in (0, 1)]
    project_ids = [re.search(r"Grant No\.\s+([A-Za-z0-9]+)", line).group(1)
                   for line in source_lines("projects.md")]
    require(len(project_ids) == 7, "The current project source must contain seven project IDs.")
    award_urls = [re.findall(r"\[[^\]]+\]\(([^)]+)\)", line)
                  for line in source_lines("awards.md")]
    education = source_lines("others.md")
    require(len(award_urls) == 4 and len(education) == 3, "Original award or education count changed.")
    for index, page in enumerate(abouts):
        projects = page.sections["-projects"]
        require(len(projects) == 7 and
                all([code for code in project_ids if code in item["text"]] == [expected_id]
                    for item, expected_id in zip(projects, project_ids)),
                f"{routes['about'][index]}: seven project IDs are missing or out of order.")
        awards = page.sections["-awards"]
        require(len(awards) == 4 and [item["links"] for item in awards] == award_urls,
                f"{routes['about'][index]}: one of four awards or its evidence link is missing.")
        degrees = page.sections["-education"]
        require(len(degrees) == 3, f"{routes['about'][index]}: one of three degrees is missing.")
        degree_terms = ("Ph.D", "Master", "Bachelor") if index == 0 else ("博士", "硕士", "学士")
        for item, original, term in zip(degrees, education, degree_terms):
            require(date_range(item["text"]) == date_range(original) and term in item["text"] and
                    re.findall(r"\b(?:SCAU|ECJTU)\b", item["text"]) ==
                    re.findall(r"\b(?:SCAU|ECJTU)\b", original),
                    f"{routes['about'][index]}: degree type, dates or institution changed.")
    for english, translated in zip(abouts[0].sections["-awards"], abouts[1].sections["-awards"]):
        require(set(re.findall(r"\b20\d{2}\b", english["text"])) ==
                set(re.findall(r"\b20\d{2}\b", translated["text"])),
                "An award year differs between languages.")

    archive = Page(args.built_site / "profile-2026-10-29/index.html")
    require(archive.lang == "en", "The original profile must remain English.")
    require(not any(lang.startswith("zh") for lang, _ in archive.alternates),
            "The original profile declares a nonexistent Chinese alternate.")
    print("PASS: 6 bilingual routes, navigation/switches/canonical/hreflang; "
          "15+15 original publications; 5 matching selected papers; "
          "2 separate contact paragraphs; 7 projects, 4 awards and 3 degrees per About; English archive.")


if __name__ == "__main__":
    try:
        main()
    except (ValueError, OSError) as error:
        raise SystemExit("FAIL: " + str(error))
