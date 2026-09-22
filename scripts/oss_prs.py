# /// script
# requires-python = ">=3.11"
# dependencies = []
# ///
"""Rebuild the open source pull request tables in README.md.

Fails loudly and leaves README.md untouched whenever the GitHub API does not
return data we can fully trust: a stale table beats a wrong one.
"""

import html
import json
import os
import pathlib
import sys
import urllib.error
import urllib.parse
import urllib.request
from typing import NoReturn


def die(message: str) -> NoReturn:
    print(f"::error::{message}", file=sys.stderr)
    print("README.md keeps its last committed tables, which are now stale.", file=sys.stderr)
    raise SystemExit(1)


USER = "dexhunter"
# Owners kept out of the search itself: my own repos, and a past employer's.
EXCLUDE = ("dexhunter", "wenshu-tech")
QUERY = f"author:{USER} type:pr is:merged " + " ".join(f"-user:{owner}" for owner in EXCLUDE)
# My employer's repos are day-job work rather than contributions, except these
# two, which are public products in their own right.
EMPLOYER = "wecoai"
EMPLOYER_KEEP = frozenset({"wecoai/aideml", "wecoai/weco-cli"})

# A project counts as AI when GitHub lists one of these topics for it...
AI_TOPICS = frozenset({
    "agent", "agent-framework", "agent-harness", "agentic", "agentic-ai", "agents",
    "ai", "ai-agent", "ai-agents", "ai-art", "ai-coding", "anthropic",
    "artificial-intelligence", "autonomous-agents", "automated-machine-learning",
    "autoresearch", "chatgpt", "coding-agent", "computer-vision", "deep-learning",
    "gan", "generative-ai", "generative-art", "genai", "gpt", "gpt-4",
    "image-generation", "large-language-models", "llm", "llm-engineering",
    "llm-inference", "llms", "machine-learning", "mcp", "multi-agent",
    "natural-language-processing", "nlp", "openai", "prompt-optimization", "rag",
    "reinforcement-learning", "rl", "self-improving-ai", "stable-diffusion",
})
# ...or when it is named here. GitHub topics are optional, and several of the
# most relevant projects (inspect_ai, parameter-golf, mle-bench) set none at all,
# so topics alone would file them under "other".
AI_PROJECTS = frozenset({
    "facebookresearch/aira-dojo",
    "jeankaddour/sokoban_speedrun",
    "lllyasviel/style2paints",
    "openai/mle-bench",
    "openai/parameter-golf",
    "sakanaai/shinkaevolve",
    "ukgovernmentbeis/inspect_ai",
    "zhengyaojiang/pgportfolio",
})

API = "https://api.github.com/"
START, END = "<!-- OSS-PRS:START -->", "<!-- OSS-PRS:END -->"
ROOT = pathlib.Path(__file__).resolve().parent.parent
README = ROOT / "README.md"
# Shields.io endpoint badge, same shape as images/google-scholar-citations.json.
BADGE = ROOT / "images" / "oss-prs.json"
MONTHS = ("Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec")
VISIBLE_STARS = 1000
# Keep all category tables aligned, including the expandable ones.
HEADER = [
    '<table>',
    '<thead><tr><th width="460">Project</th><th width="80">Stars</th>'
    '<th width="130">Contributions</th><th width="100">Latest</th></tr></thead>',
    '<tbody>',
]


def get(path: str, **params: object) -> dict:
    token = os.environ.get("GITHUB_TOKEN") or die("GITHUB_TOKEN is not set.")
    url = API + path + (f"?{urllib.parse.urlencode(params)}" if params else "")
    request = urllib.request.Request(
        url,
        headers={
            "Accept": "application/vnd.github+json",
            "X-GitHub-Api-Version": "2022-11-28",
            "Authorization": f"Bearer {token}",
        },
    )
    try:
        with urllib.request.urlopen(request, timeout=30) as response:
            return json.load(response)
    except (urllib.error.URLError, TimeoutError, json.JSONDecodeError) as error:
        die(f"GET {path} failed: {error}")


def wanted(repo: str) -> bool:
    """Employer repos are day-job work; only the two public products count."""
    owner, _, _ = repo.partition("/")
    return owner.lower() != EMPLOYER or repo.lower() in EMPLOYER_KEEP


def merged_prs() -> dict[str, dict[str, str]]:
    """Repo full name -> {pull request url: merged_at}. The inner dict dedupes
    a pull request that straddles a page boundary when the index shifts."""
    merges: dict[str, dict[str, str]] = {}
    seen: set[str] = set()  # distinct pull requests, so a repeat cannot pass as progress
    total = 0
    page = 1
    while True:
        # Oldest first: a stable ordering, so pages cannot reshuffle under us.
        result = get("search/issues", q=QUERY, sort="created", order="asc", per_page=100, page=page)
        total = result["total_count"]
        if result["incomplete_results"]:
            die("GitHub search timed out and returned partial results.")
        if total == 0:
            die(f"GitHub search found no merged pull requests for {QUERY!r}.")
        if total > 1000:
            die(f"{total} results exceed the 1000-result search cap; split the query.")
        for item in result["items"]:
            seen.add(item["html_url"])
            repo = item["repository_url"].removeprefix(f"{API}repos/")
            if wanted(repo):
                merges.setdefault(repo, {})[item["html_url"]] = item["pull_request"]["merged_at"]
        if page * 100 >= total:
            break
        page += 1
    if len(seen) < total:
        die(f"GitHub search returned {len(seen)} of {total} pull requests; results were truncated.")
    if not merges:
        die("Every merged pull request was filtered out; the filters must be wrong.")
    return merges


def stars(count: int) -> str:
    """387289 -> 387k, 9999 -> 10k, 1490 -> 1.5k, 1000 -> 1.0k, 439 -> 439."""
    if count < 1000:
        return str(count)
    tenths = (count + 50) // 100  # tenths of a thousand, rounded half up
    if tenths >= 100:  # 10.0k and above: no decimal
        return f"{(count + 500) // 1000}k"
    return f"{tenths // 10}.{tenths % 10}k"


def row(count: int, _prs: int, repo: str, url: str, latest: str, avatar: str) -> str:
    when = f"{MONTHS[int(latest[5:7]) - 1]} {latest[:4]}"
    search = f"{url}/pulls?q=is%3Apr+author%3A{USER}+is%3Amerged"
    # The owner avatar doubles as the project's logo. It comes from metadata we
    # already fetched, so it costs no extra request, and a 40px source keeps it
    # crisp on retina while rendering at 16px.
    icon = f'<img src="{html.escape(avatar)}&amp;s=40" width="16" height="16" alt=""> '
    name = html.escape(repo)
    return (
        f'<tr><td>{icon}<a href="{html.escape(url)}">{name}</a></td>'
        f'<td align="right">{stars(count)}</td>'
        f'<td><a href="{html.escape(search)}">View PRs</a></td>'
        f'<td>{when.replace(" ", "&nbsp;")}</td></tr>'
    )


def table(projects: list[tuple]) -> list[str]:
    return HEADER + [row(*project) for project in projects] + ["</tbody>", "</table>"]


def category(projects: list[tuple], label: str) -> list[str]:
    visible = [project for project in projects if project[0] >= VISIBLE_STARS]
    more = [project for project in projects if project[0] < VISIBLE_STARS]
    block = table(visible) if visible else []
    if more:
        block += [
            "", "<details>",
            f"<summary>{len(more)} more {label} projects (under 1,000 stars)</summary>",
            "", *table(more), "", "</details>",
        ]
    return block


def main() -> None:
    # Keyed by current full name, because search can hand back both the old and
    # the new name of a renamed repo and urllib follows GitHub's rename
    # redirect: without this the same project would render as two rows.
    projects_by_name: dict[str, tuple[dict, dict[str, str]]] = {}
    for repo, merges in merged_prs().items():
        meta = get(f"repos/{repo}")
        # Private repos are invisible to every reader of this README, and to
        # the repo-scoped token CI runs with, so their rows would only 404.
        if meta["private"]:
            continue
        name = meta["full_name"].lower()
        if name in projects_by_name:
            merges = {**projects_by_name[name][1], **merges}
        projects_by_name[name] = (meta, merges)

    ai: list[tuple] = []
    other: list[tuple] = []
    for meta, merges in projects_by_name.values():
        project = (meta["stargazers_count"], len(merges), meta["full_name"], meta["html_url"],
                   max(merges.values()), meta["owner"]["avatar_url"])
        topics = {topic.lower() for topic in meta.get("topics") or ()}
        is_ai = bool(topics & AI_TOPICS) or meta["full_name"].lower() in AI_PROJECTS
        (ai if is_ai else other).append(project)
    if not ai and not other:
        die("Every project was filtered out; the filters must be wrong.")

    for projects in (ai, other):
        projects.sort(key=lambda project: (-project[0], -project[1], project[2]))

    count = sum(project[1] for project in ai + other)
    block = [
        f"Contributions to {len(ai) + len(other)} open source "
        f"projects — {len(ai)} of them AI or agent infrastructure.",
        "",
        "### AI and agent infrastructure",
        "",
        *category(ai, "AI and agent infrastructure"),
    ]
    if other:
        block += ["", "### Projects outside AI", "", *category(other, "non-AI")]

    before, _, rest = README.read_text(encoding="utf-8").partition(START)
    _, marker, after = rest.partition(END)
    if not marker:
        die(f"README.md is missing its {START} / {END} markers.")
    if START in after or END in after:
        die(f"README.md has more than one {START} / {END} pair; only the first would update.")
    README.write_text(
        before + START + "\n\n" + "\n".join(block) + "\n\n" + END + after,
        encoding="utf-8", newline="\n",
    )
    BADGE.write_text(
        json.dumps(
            {"schemaVersion": 1, "label": "Open source projects", "message": str(len(ai) + len(other)), "color": "blue"},
            indent=2,
        ) + "\n",
        encoding="utf-8", newline="\n",
    )
    print(f"{count} merged PRs: {len(ai)} AI projects, {len(other)} others")


if __name__ == "__main__":
    main()
