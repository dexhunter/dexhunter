"""Keep scheduled table refreshes complete and the disclosure threshold exact."""

import unittest
from html.parser import HTMLParser

from scripts.oss_prs import category


class TableStructure(HTMLParser):
    def __init__(self):
        super().__init__()
        self.depth = self.max_depth = 0
        self.links = []
        self.widths = []

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if tag == "details":
            self.depth += 1
            self.max_depth = max(self.max_depth, self.depth)
        elif tag == "a":
            self.links.append((attrs["href"], self.depth))
        elif tag == "th":
            self.widths.append(attrs["width"])

    def handle_endtag(self, tag):
        if tag == "details":
            self.depth -= 1


def project(stars, name):
    return (stars, 1, name, f"https://github.com/{name}", "2026-09-01", "https://example.com/avatar?v=4")


class CategoryTests(unittest.TestCase):
    def test_threshold_preserves_each_project_once_without_nested_details(self):
        projects = [project(1000, "owner/visible"), project(999, "owner/small"), project(0, "owner/new")]
        rendered = "\n".join(category(projects, "AI"))
        parsed = TableStructure()
        parsed.feed(rendered)
        for item, depth in zip(projects, (0, 1, 1)):
            self.assertEqual(parsed.links.count((item[3], depth)), 1)
            self.assertEqual(sum(url == item[3] for url, _ in parsed.links), 1)
        self.assertEqual(parsed.max_depth, 1)
        self.assertEqual(parsed.depth, 0)
        self.assertEqual(parsed.widths, ["460", "80", "130", "100"] * 2)
        self.assertIn("2 more AI projects", rendered)

    def test_empty_groups_do_not_create_empty_tables_or_expanders(self):
        self.assertEqual(category([], "AI"), [])
        visible = "\n".join(category([project(1000, "owner/visible")], "AI"))
        self.assertNotIn("<details>", visible)
        small = "\n".join(category([project(999, "owner/small")], "AI"))
        self.assertEqual(small.count("<table>"), 1)
        self.assertLess(small.index("<details>"), small.index("<table>"))

    def test_html_output_escapes_metadata(self):
        rendered = "\n".join(category([project(1000, 'owner/<unsafe>&"')], "AI"))
        self.assertNotIn("<unsafe>", rendered)
        self.assertIn("&lt;unsafe&gt;&amp;&quot;", rendered)
        self.assertIn("Sep&nbsp;2026", rendered)


if __name__ == "__main__":
    unittest.main()
