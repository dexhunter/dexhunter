# /// script
# requires-python = ">=3.11"
# dependencies = []
# ///
"""Rebuild the open source pull request tables in README.md.

Fails loudly and leaves README.md untouched whenever the GitHub API does not
return data we can fully trust: a stale table beats a wrong one.
"""

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

TOP = 20
API = "https://api.github.com/"
START, END = "<!-- OSS-PRS:START -->", "<!-- OSS-PRS:END -->"
# Fails immediately, before any request, if unset.
TOKEN = os.environ.get("GITHUB_TOKEN") or die("GITHUB_TOKEN is not set.")
ROOT = pathlib.Path(__file__).resolve().parent.parent
README = ROOT / "README.md"
# Shields.io endpoint badge, same shape as images/google-scholar-citations.json.
BADGE = ROOT / "images" / "oss-prs.json"
MONTHS = ("Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec")
HEADER = ["| Project | Stars | Merged PRs | Latest |", "| --- | ---: | ---: | --- |"]


def get(path: str, **params: object) -> dict:
    url = API + path + (f"?{urllib.parse.urlencode(params)}" if params else "")
    request = urllib.request.Request(
        url,
        headers={
            "Accept": "application/vnd.github+json",
            "X-GitHub-Api-Version": "2022-11-28",
            "Authorization": f"Bearer {TOKEN}",
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


def row(count: int, prs: int, repo: str, url: str, latest: str) -> str:
    when = f"{MONTHS[int(latest[5:7]) - 1]} {latest[:4]}"
    search = f"{url}/pulls?q=is%3Apr+author%3A{USER}+is%3Amerged"
    return f"| [{repo}]({url}) | {stars(count)} | [{prs}]({search}) | {when} |"


def table(projects: list[tuple]) -> list[str]:
    return HEADER + [row(*project) for project in projects]


def fold(lines: list[str], summary: str) -> list[str]:
    # The blank line after </summary> is required, or the table renders as
    # literal pipes instead of a table.
    return ["", "<details>", f"<summary>{summary}</summary>", "", *lines, "", "</details>"]


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
                   max(merges.values()))
        topics = {topic.lower() for topic in meta.get("topics") or ()}
        is_ai = bool(topics & AI_TOPICS) or meta["full_name"].lower() in AI_PROJECTS
        (ai if is_ai else other).append(project)
    if not ai and not other:
        die("Every project was filtered out; the filters must be wrong.")

    for projects in (ai, other):
        projects.sort(key=lambda project: (-project[0], -project[1], project[2]))

    count = sum(project[1] for project in ai + other)
    block = [
        f"**{count} merged pull requests across {len(ai) + len(other)} open source "
        f"projects — {len(ai)} of them AI or agent infrastructure.**",
        "",
        "### AI and agent infrastructure",
        "",
        *table(ai[:TOP]),
    ]
    if ai[TOP:]:
        block += fold(table(ai[TOP:]), f"{len(ai) - TOP} more AI projects")
    if other:
        block += fold(table(other), f"{len(other)} projects outside AI")

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
            {"schemaVersion": 1, "label": "Merged PRs", "message": str(count), "color": "blue"},
            indent=2,
        ) + "\n",
        encoding="utf-8", newline="\n",
    )
    print(f"{count} merged PRs: {len(ai)} AI projects, {len(other)} others")


main()
