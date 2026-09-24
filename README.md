<div align="center">
<h1 align="center">Hi👋 Dex here. Welcome to my page!</h1>
</div>

> [!NOTE]
> **AI-generated optimization PRs:** This account is used to submit optimization pull requests written by autonomous AI agents as part of our research at [Weco AI](https://github.com/wecoai). We're testing how well agents can identify performance improvements, implement and evaluate changes, and prepare PRs for real open-source projects.

<p align="center">
  <a href="https://github.com/dexhunter"><img src="https://img.shields.io/github/followers/dexhunter.svg?label=GitHub&style=flat-square" alt="GitHub"></a>
  <a href="https://scholar.google.co.jp/citations?user=8Ez_u30AAAAJ&hl=en"><img src="https://img.shields.io/endpoint?url=https%3A%2F%2Fraw.githubusercontent.com%2Fdexhunter%2Fdexhunter%2Fmaster%2Fimages%2Fgoogle-scholar-citations.json&style=flat-square" alt="Google Scholar citations"></a>
  <a href="#-open-source"><img src="https://img.shields.io/endpoint?url=https%3A%2F%2Fraw.githubusercontent.com%2Fdexhunter%2Fdexhunter%2Fmaster%2Fimages%2Foss-prs.json&style=flat-square" alt="Open source projects"></a>
  <a href="https://stackoverflow.com/users/3253000/dexhunter"><img src="https://img.shields.io/stackexchange/stackoverflow/r/3253000?style=flat-square&label=Stack%20Overflow&logo=stackoverflow&logoColor=white&color=orange" alt="Stack Overflow reputation"></a>
  <a href="https://dex.moe"><img src="https://img.shields.io/badge/Website-dex.moe-red?style=flat-square" alt="Website"></a>
  <a href="mailto:i@dex.moe"><img src="https://img.shields.io/badge/-Email-red?style=flat-square&logo=gmail&logoColor=white" alt="Email"></a>
</p>

## 👨‍💻 About

I'm a Member of Technical Staff at [Weco AI](https://github.com/wecoai), where I build autonomous agents for research.

I've [contributed to AIDE](https://github.com/WecoAI/aideml/pulls?q=is%3Apr+author%3Adexhunter+is%3Amerged) since 2024 and co-authored its [2025 paper](https://arxiv.org/abs/2502.13138). AIDE uses tree search to write and improve machine learning code. OpenAI used it for [MLE-bench evaluations](https://cdn.openai.com/gpt-4-5-system-card-2272025.pdf), and Meta FAIR [reimplemented it as a baseline](https://arxiv.org/abs/2507.02554) for its own research agents.

Previously, I built trading systems at [Hex Trust](https://hextrust.com). I also served as a [maintainer of the Hyperledger Fabric Python SDK](https://github.com/hyperledger/fabric-sdk-py/blob/main/MAINTAINERS.md), a Linux Foundation project.

I studied Information and Computing Sciences at the University of Liverpool and Xi'an Jiaotong-Liverpool University. I also did research at Nanyang Technological University, Zhejiang University, and Hong Kong Baptist University.

## 🌱 Open source

### Featured

- **[UK AI Security Institute — Inspect](https://github.com/UKGovernmentBEIS/inspect_ai)** — performance work on the UK government's LLM evaluation framework: cut clustered-stderr scoring time and memory ([#4714](https://github.com/UKGovernmentBEIS/inspect_ai/pull/4714)), and made tool-result media extraction linear in conversation length ([#4628](https://github.com/UKGovernmentBEIS/inspect_ai/pull/4628)).
- **[OpenAI Parameter Golf](https://github.com/openai/parameter-golf)** — I built an autonomous research agent that set seven leaderboard records in 2026, with entries in the official [record-track directory](https://github.com/openai/parameter-golf/tree/main/records/track_10min_16mb). Its best result achieved a 5-seed mean validation BPB of [1.0645](https://github.com/openai/parameter-golf/pull/1769). OpenAI also highlighted [one of the agent's model-compression PRs](https://github.com/openai/parameter-golf/pull/1060) in its [write-up about the competition](https://openai.com/index/what-parameter-golf-taught-us/).
- **Agent runtimes** — merged performance work into [openclaw](https://github.com/openclaw/openclaw/pull/99714), [AutoGPT](https://github.com/Significant-Gravitas/AutoGPT/pull/13478), [goose](https://github.com/aaif-goose/goose/pull/10409), [qwen-code](https://github.com/QwenLM/qwen-code/pull/8253), [pydantic-ai](https://github.com/pydantic/pydantic-ai/pull/6485), [agno](https://github.com/agno-agi/agno/pull/8907) and [BAML](https://github.com/BoundaryML/baml/pull/3975).
- **AI research infrastructure** — cut redundant AST parsing in Sakana AI's [ShinkaEvolve](https://github.com/SakanaAI/ShinkaEvolve/pull/175) and bounded process-pool shutdown latency in [OpenEvolve](https://github.com/algorithmicsuperintelligence/openevolve/pull/469); smaller docs fixes in Meta's [aira-dojo](https://github.com/facebookresearch/aira-dojo/pull/2), Microsoft's [RD-Agent](https://github.com/microsoft/RD-Agent/pull/1249) and OpenAI's [MLE-bench](https://github.com/openai/mle-bench/pull/101).
- **[AIDE](https://github.com/WecoAI/aideml)** — contributions to the open-source tree-search agent behind my 2025 paper; it writes, evaluates, and improves machine learning code. I also contribute to [weco-cli](https://github.com/WecoAI/weco-cli), the command line tool that drives it.

Each project links to its merged pull requests on GitHub. Ranked by stars, refreshed weekly. Projects with fewer than 1,000 stars are listed in the expandable sections.

<!-- OSS-PRS:START -->

Contributions to 57 open source projects — 30 of them AI or agent infrastructure.

### AI and agent infrastructure

<table>
<thead><tr><th width="460">Project</th><th width="80">Stars</th><th width="130">Contributions</th><th width="100">Latest</th></tr></thead>
<tbody>
<tr><td><img src="https://avatars.githubusercontent.com/u/252820863?v=4&amp;s=40" width="16" height="16" alt=""> <a href="https://github.com/openclaw/openclaw">openclaw/openclaw</a></td><td align="right">390k</td><td><a href="https://github.com/openclaw/openclaw/pulls?q=is%3Apr+author%3Adexhunter+is%3Amerged">View PRs</a></td><td>Jul&nbsp;2026</td></tr>
<tr><td><img src="https://avatars.githubusercontent.com/u/130738209?v=4&amp;s=40" width="16" height="16" alt=""> <a href="https://github.com/Significant-Gravitas/AutoGPT">Significant-Gravitas/AutoGPT</a></td><td align="right">188k</td><td><a href="https://github.com/Significant-Gravitas/AutoGPT/pulls?q=is%3Apr+author%3Adexhunter+is%3Amerged">View PRs</a></td><td>Sep&nbsp;2026</td></tr>
<tr><td><img src="https://avatars.githubusercontent.com/u/126733545?v=4&amp;s=40" width="16" height="16" alt=""> <a href="https://github.com/langchain-ai/langchain">langchain-ai/langchain</a></td><td align="right">147k</td><td><a href="https://github.com/langchain-ai/langchain/pulls?q=is%3Apr+author%3Adexhunter+is%3Amerged">View PRs</a></td><td>Mar&nbsp;2024</td></tr>
<tr><td><img src="https://avatars.githubusercontent.com/u/80064875?v=4&amp;s=40" width="16" height="16" alt=""> <a href="https://github.com/OpenBB-finance/OpenBB">OpenBB-finance/OpenBB</a></td><td align="right">73k</td><td><a href="https://github.com/OpenBB-finance/OpenBB/pulls?q=is%3Apr+author%3Adexhunter+is%3Amerged">View PRs</a></td><td>Jul&nbsp;2026</td></tr>
<tr><td><img src="https://avatars.githubusercontent.com/u/271095942?v=4&amp;s=40" width="16" height="16" alt=""> <a href="https://github.com/aaif-goose/goose">aaif-goose/goose</a></td><td align="right">55k</td><td><a href="https://github.com/aaif-goose/goose/pulls?q=is%3Apr+author%3Adexhunter+is%3Amerged">View PRs</a></td><td>Jul&nbsp;2026</td></tr>
<tr><td><img src="https://avatars.githubusercontent.com/u/104874993?v=4&amp;s=40" width="16" height="16" alt=""> <a href="https://github.com/agno-agi/agno">agno-agi/agno</a></td><td align="right">42k</td><td><a href="https://github.com/agno-agi/agno/pulls?q=is%3Apr+author%3Adexhunter+is%3Amerged">View PRs</a></td><td>Jul&nbsp;2026</td></tr>
<tr><td><img src="https://avatars.githubusercontent.com/u/113954515?v=4&amp;s=40" width="16" height="16" alt=""> <a href="https://github.com/invoke-ai/InvokeAI">invoke-ai/InvokeAI</a></td><td align="right">28k</td><td><a href="https://github.com/invoke-ai/InvokeAI/pulls?q=is%3Apr+author%3Adexhunter+is%3Amerged">View PRs</a></td><td>Aug&nbsp;2026</td></tr>
<tr><td><img src="https://avatars.githubusercontent.com/u/141221163?v=4&amp;s=40" width="16" height="16" alt=""> <a href="https://github.com/QwenLM/qwen-code">QwenLM/qwen-code</a></td><td align="right">28k</td><td><a href="https://github.com/QwenLM/qwen-code/pulls?q=is%3Apr+author%3Adexhunter+is%3Amerged">View PRs</a></td><td>Aug&nbsp;2026</td></tr>
<tr><td><img src="https://avatars.githubusercontent.com/u/110818415?v=4&amp;s=40" width="16" height="16" alt=""> <a href="https://github.com/pydantic/pydantic-ai">pydantic/pydantic-ai</a></td><td align="right">20k</td><td><a href="https://github.com/pydantic/pydantic-ai/pulls?q=is%3Apr+author%3Adexhunter+is%3Amerged">View PRs</a></td><td>Jul&nbsp;2026</td></tr>
<tr><td><img src="https://avatars.githubusercontent.com/u/19834515?v=4&amp;s=40" width="16" height="16" alt=""> <a href="https://github.com/lllyasviel/style2paints">lllyasviel/style2paints</a></td><td align="right">18k</td><td><a href="https://github.com/lllyasviel/style2paints/pulls?q=is%3Apr+author%3Adexhunter+is%3Amerged">View PRs</a></td><td>Aug&nbsp;2017</td></tr>
<tr><td><img src="https://avatars.githubusercontent.com/u/169612734?v=4&amp;s=40" width="16" height="16" alt=""> <a href="https://github.com/pipecat-ai/pipecat">pipecat-ai/pipecat</a></td><td align="right">16k</td><td><a href="https://github.com/pipecat-ai/pipecat/pulls?q=is%3Apr+author%3Adexhunter+is%3Amerged">View PRs</a></td><td>Jul&nbsp;2026</td></tr>
<tr><td><img src="https://avatars.githubusercontent.com/u/6154722?v=4&amp;s=40" width="16" height="16" alt=""> <a href="https://github.com/microsoft/RD-Agent">microsoft/RD-Agent</a></td><td align="right">15k</td><td><a href="https://github.com/microsoft/RD-Agent/pulls?q=is%3Apr+author%3Adexhunter+is%3Amerged">View PRs</a></td><td>Sep&nbsp;2025</td></tr>
<tr><td><img src="https://avatars.githubusercontent.com/u/177023663?v=4&amp;s=40" width="16" height="16" alt=""> <a href="https://github.com/tadata-org/fastapi_mcp">tadata-org/fastapi_mcp</a></td><td align="right">12k</td><td><a href="https://github.com/tadata-org/fastapi_mcp/pulls?q=is%3Apr+author%3Adexhunter+is%3Amerged">View PRs</a></td><td>Mar&nbsp;2025</td></tr>
<tr><td><img src="https://avatars.githubusercontent.com/u/56968752?v=4&amp;s=40" width="16" height="16" alt=""> <a href="https://github.com/kornia/kornia">kornia/kornia</a></td><td align="right">11k</td><td><a href="https://github.com/kornia/kornia/pulls?q=is%3Apr+author%3Adexhunter+is%3Amerged">View PRs</a></td><td>Sep&nbsp;2026</td></tr>
<tr><td><img src="https://avatars.githubusercontent.com/u/813142?v=4&amp;s=40" width="16" height="16" alt=""> <a href="https://github.com/phillipi/pix2pix">phillipi/pix2pix</a></td><td align="right">11k</td><td><a href="https://github.com/phillipi/pix2pix/pulls?q=is%3Apr+author%3Adexhunter+is%3Amerged">View PRs</a></td><td>Jun&nbsp;2017</td></tr>
<tr><td><img src="https://avatars.githubusercontent.com/u/124114301?v=4&amp;s=40" width="16" height="16" alt=""> <a href="https://github.com/BoundaryML/baml">BoundaryML/baml</a></td><td align="right">9.3k</td><td><a href="https://github.com/BoundaryML/baml/pulls?q=is%3Apr+author%3Adexhunter+is%3Amerged">View PRs</a></td><td>Aug&nbsp;2026</td></tr>
<tr><td><img src="https://avatars.githubusercontent.com/u/238764598?v=4&amp;s=40" width="16" height="16" alt=""> <a href="https://github.com/algorithmicsuperintelligence/openevolve">algorithmicsuperintelligence/openevolve</a></td><td align="right">7.4k</td><td><a href="https://github.com/algorithmicsuperintelligence/openevolve/pulls?q=is%3Apr+author%3Adexhunter+is%3Amerged">View PRs</a></td><td>Jul&nbsp;2026</td></tr>
<tr><td><img src="https://avatars.githubusercontent.com/u/14957082?v=4&amp;s=40" width="16" height="16" alt=""> <a href="https://github.com/openai/parameter-golf">openai/parameter-golf</a></td><td align="right">5.2k</td><td><a href="https://github.com/openai/parameter-golf/pulls?q=is%3Apr+author%3Adexhunter+is%3Amerged">View PRs</a></td><td>Apr&nbsp;2026</td></tr>
<tr><td><img src="https://avatars.githubusercontent.com/u/72518640?v=4&amp;s=40" width="16" height="16" alt=""> <a href="https://github.com/TanStack/ai">TanStack/ai</a></td><td align="right">3.1k</td><td><a href="https://github.com/TanStack/ai/pulls?q=is%3Apr+author%3Adexhunter+is%3Amerged">View PRs</a></td><td>Aug&nbsp;2026</td></tr>
<tr><td><img src="https://avatars.githubusercontent.com/u/19221939?v=4&amp;s=40" width="16" height="16" alt=""> <a href="https://github.com/UKGovernmentBEIS/inspect_ai">UKGovernmentBEIS/inspect_ai</a></td><td align="right">2.9k</td><td><a href="https://github.com/UKGovernmentBEIS/inspect_ai/pulls?q=is%3Apr+author%3Adexhunter+is%3Amerged">View PRs</a></td><td>Aug&nbsp;2026</td></tr>
<tr><td><img src="https://avatars.githubusercontent.com/u/15139574?v=4&amp;s=40" width="16" height="16" alt=""> <a href="https://github.com/ZhengyaoJiang/PGPortfolio">ZhengyaoJiang/PGPortfolio</a></td><td align="right">1.9k</td><td><a href="https://github.com/ZhengyaoJiang/PGPortfolio/pulls?q=is%3Apr+author%3Adexhunter+is%3Amerged">View PRs</a></td><td>Dec&nbsp;2017</td></tr>
<tr><td><img src="https://avatars.githubusercontent.com/u/14957082?v=4&amp;s=40" width="16" height="16" alt=""> <a href="https://github.com/openai/mle-bench">openai/mle-bench</a></td><td align="right">1.8k</td><td><a href="https://github.com/openai/mle-bench/pulls?q=is%3Apr+author%3Adexhunter+is%3Amerged">View PRs</a></td><td>Nov&nbsp;2025</td></tr>
<tr><td><img src="https://avatars.githubusercontent.com/u/62961550?v=4&amp;s=40" width="16" height="16" alt=""> <a href="https://github.com/Farama-Foundation/ChatArena">Farama-Foundation/ChatArena</a></td><td align="right">1.6k</td><td><a href="https://github.com/Farama-Foundation/ChatArena/pulls?q=is%3Apr+author%3Adexhunter+is%3Amerged">View PRs</a></td><td>Jun&nbsp;2023</td></tr>
<tr><td><img src="https://avatars.githubusercontent.com/u/132215366?v=4&amp;s=40" width="16" height="16" alt=""> <a href="https://github.com/WecoAI/aideml">WecoAI/aideml</a></td><td align="right">1.5k</td><td><a href="https://github.com/WecoAI/aideml/pulls?q=is%3Apr+author%3Adexhunter+is%3Amerged">View PRs</a></td><td>Jul&nbsp;2026</td></tr>
<tr><td><img src="https://avatars.githubusercontent.com/u/140988036?v=4&amp;s=40" width="16" height="16" alt=""> <a href="https://github.com/SakanaAI/ShinkaEvolve">SakanaAI/ShinkaEvolve</a></td><td align="right">1.4k</td><td><a href="https://github.com/SakanaAI/ShinkaEvolve/pulls?q=is%3Apr+author%3Adexhunter+is%3Amerged">View PRs</a></td><td>Aug&nbsp;2026</td></tr>
</tbody>
</table>

<details>
<summary>5 more AI and agent infrastructure projects (under 1,000 stars)</summary>

<table>
<thead><tr><th width="460">Project</th><th width="80">Stars</th><th width="130">Contributions</th><th width="100">Latest</th></tr></thead>
<tbody>
<tr><td><img src="https://avatars.githubusercontent.com/u/66310692?v=4&amp;s=40" width="16" height="16" alt=""> <a href="https://github.com/tongjingqi/AI-Can-Learn-Scientific-Taste">tongjingqi/AI-Can-Learn-Scientific-Taste</a></td><td align="right">432</td><td><a href="https://github.com/tongjingqi/AI-Can-Learn-Scientific-Taste/pulls?q=is%3Apr+author%3Adexhunter+is%3Amerged">View PRs</a></td><td>Mar&nbsp;2026</td></tr>
<tr><td><img src="https://avatars.githubusercontent.com/u/16943930?v=4&amp;s=40" width="16" height="16" alt=""> <a href="https://github.com/facebookresearch/aira-dojo">facebookresearch/aira-dojo</a></td><td align="right">172</td><td><a href="https://github.com/facebookresearch/aira-dojo/pulls?q=is%3Apr+author%3Adexhunter+is%3Amerged">View PRs</a></td><td>Jul&nbsp;2025</td></tr>
<tr><td><img src="https://avatars.githubusercontent.com/u/132215366?v=4&amp;s=40" width="16" height="16" alt=""> <a href="https://github.com/WecoAI/weco-cli">WecoAI/weco-cli</a></td><td align="right">106</td><td><a href="https://github.com/WecoAI/weco-cli/pulls?q=is%3Apr+author%3Adexhunter+is%3Amerged">View PRs</a></td><td>Sep&nbsp;2025</td></tr>
<tr><td><img src="https://avatars.githubusercontent.com/u/11850255?v=4&amp;s=40" width="16" height="16" alt=""> <a href="https://github.com/JeanKaddour/sokoban_speedrun">JeanKaddour/sokoban_speedrun</a></td><td align="right">31</td><td><a href="https://github.com/JeanKaddour/sokoban_speedrun/pulls?q=is%3Apr+author%3Adexhunter+is%3Amerged">View PRs</a></td><td>Jul&nbsp;2026</td></tr>
<tr><td><img src="https://avatars.githubusercontent.com/u/263072830?v=4&amp;s=40" width="16" height="16" alt=""> <a href="https://github.com/openbydesign/lush">openbydesign/lush</a></td><td align="right">3</td><td><a href="https://github.com/openbydesign/lush/pulls?q=is%3Apr+author%3Adexhunter+is%3Amerged">View PRs</a></td><td>Aug&nbsp;2026</td></tr>
</tbody>
</table>

</details>

### Projects outside AI

<table>
<thead><tr><th width="460">Project</th><th width="80">Stars</th><th width="130">Contributions</th><th width="100">Latest</th></tr></thead>
<tbody>
<tr><td><img src="https://avatars.githubusercontent.com/u/85344006?v=4&amp;s=40" width="16" height="16" alt=""> <a href="https://github.com/remotion-dev/remotion">remotion-dev/remotion</a></td><td align="right">60k</td><td><a href="https://github.com/remotion-dev/remotion/pulls?q=is%3Apr+author%3Adexhunter+is%3Amerged">View PRs</a></td><td>Aug&nbsp;2026</td></tr>
<tr><td><img src="https://avatars.githubusercontent.com/u/65579849?v=4&amp;s=40" width="16" height="16" alt=""> <a href="https://github.com/ManimCommunity/manim">ManimCommunity/manim</a></td><td align="right">41k</td><td><a href="https://github.com/ManimCommunity/manim/pulls?q=is%3Apr+author%3Adexhunter+is%3Amerged">View PRs</a></td><td>Aug&nbsp;2026</td></tr>
<tr><td><img src="https://avatars.githubusercontent.com/u/21320719?v=4&amp;s=40" width="16" height="16" alt=""> <a href="https://github.com/pnpm/pnpm">pnpm/pnpm</a></td><td align="right">37k</td><td><a href="https://github.com/pnpm/pnpm/pulls?q=is%3Apr+author%3Adexhunter+is%3Amerged">View PRs</a></td><td>Sep&nbsp;2026</td></tr>
<tr><td><img src="https://avatars.githubusercontent.com/u/48722593?v=4&amp;s=40" width="16" height="16" alt=""> <a href="https://github.com/python-poetry/poetry">python-poetry/poetry</a></td><td align="right">34k</td><td><a href="https://github.com/python-poetry/poetry/pulls?q=is%3Apr+author%3Adexhunter+is%3Amerged">View PRs</a></td><td>Aug&nbsp;2026</td></tr>
<tr><td><img src="https://avatars.githubusercontent.com/u/129804596?v=4&amp;s=40" width="16" height="16" alt=""> <a href="https://github.com/mozilla-ai/llamafile">mozilla-ai/llamafile</a></td><td align="right">26k</td><td><a href="https://github.com/mozilla-ai/llamafile/pulls?q=is%3Apr+author%3Adexhunter+is%3Amerged">View PRs</a></td><td>Sep&nbsp;2026</td></tr>
<tr><td><img src="https://avatars.githubusercontent.com/u/5713511?v=4&amp;s=40" width="16" height="16" alt=""> <a href="https://github.com/mementum/backtrader">mementum/backtrader</a></td><td align="right">23k</td><td><a href="https://github.com/mementum/backtrader/pulls?q=is%3Apr+author%3Adexhunter+is%3Amerged">View PRs</a></td><td>Aug&nbsp;2017</td></tr>
<tr><td><img src="https://avatars.githubusercontent.com/u/149946238?v=4&amp;s=40" width="16" height="16" alt=""> <a href="https://github.com/oxc-project/oxc">oxc-project/oxc</a></td><td align="right">23k</td><td><a href="https://github.com/oxc-project/oxc/pulls?q=is%3Apr+author%3Adexhunter+is%3Amerged">View PRs</a></td><td>Sep&nbsp;2026</td></tr>
<tr><td><img src="https://avatars.githubusercontent.com/u/41247880?v=4&amp;s=40" width="16" height="16" alt=""> <a href="https://github.com/MSWorkers/support.996.ICU">MSWorkers/support.996.ICU</a></td><td align="right">10k</td><td><a href="https://github.com/MSWorkers/support.996.ICU/pulls?q=is%3Apr+author%3Adexhunter+is%3Amerged">View PRs</a></td><td>Apr&nbsp;2019</td></tr>
<tr><td><img src="https://avatars.githubusercontent.com/u/1920564?v=4&amp;s=40" width="16" height="16" alt=""> <a href="https://github.com/yeasy/blockchain_guide">yeasy/blockchain_guide</a></td><td align="right">7.1k</td><td><a href="https://github.com/yeasy/blockchain_guide/pulls?q=is%3Apr+author%3Adexhunter+is%3Amerged">View PRs</a></td><td>Mar&nbsp;2019</td></tr>
<tr><td><img src="https://avatars.githubusercontent.com/u/13629408?v=4&amp;s=40" width="16" height="16" alt=""> <a href="https://github.com/kubernetes/website">kubernetes/website</a></td><td align="right">5.4k</td><td><a href="https://github.com/kubernetes/website/pulls?q=is%3Apr+author%3Adexhunter+is%3Amerged">View PRs</a></td><td>Apr&nbsp;2020</td></tr>
<tr><td><img src="https://avatars.githubusercontent.com/u/6407041?v=4&amp;s=40" width="16" height="16" alt=""> <a href="https://github.com/ReactiveX/RxPY">ReactiveX/RxPY</a></td><td align="right">5.0k</td><td><a href="https://github.com/ReactiveX/RxPY/pulls?q=is%3Apr+author%3Adexhunter+is%3Amerged">View PRs</a></td><td>Sep&nbsp;2018</td></tr>
<tr><td><img src="https://avatars.githubusercontent.com/u/1403074?v=4&amp;s=40" width="16" height="16" alt=""> <a href="https://github.com/mikedh/trimesh">mikedh/trimesh</a></td><td align="right">3.7k</td><td><a href="https://github.com/mikedh/trimesh/pulls?q=is%3Apr+author%3Adexhunter+is%3Amerged">View PRs</a></td><td>Aug&nbsp;2026</td></tr>
<tr><td><img src="https://avatars.githubusercontent.com/u/15976103?v=4&amp;s=40" width="16" height="16" alt=""> <a href="https://github.com/yihong0618/GitHubPoster">yihong0618/GitHubPoster</a></td><td align="right">1.9k</td><td><a href="https://github.com/yihong0618/GitHubPoster/pulls?q=is%3Apr+author%3Adexhunter+is%3Amerged">View PRs</a></td><td>Jun&nbsp;2021</td></tr>
<tr><td><img src="https://avatars.githubusercontent.com/u/21127168?v=4&amp;s=40" width="16" height="16" alt=""> <a href="https://github.com/TA-Lib/ta-lib">TA-Lib/ta-lib</a></td><td align="right">1.7k</td><td><a href="https://github.com/TA-Lib/ta-lib/pulls?q=is%3Apr+author%3Adexhunter+is%3Amerged">View PRs</a></td><td>Aug&nbsp;2026</td></tr>
<tr><td><img src="https://avatars.githubusercontent.com/u/97177645?v=4&amp;s=40" width="16" height="16" alt=""> <a href="https://github.com/console-rs/console">console-rs/console</a></td><td align="right">1.2k</td><td><a href="https://github.com/console-rs/console/pulls?q=is%3Apr+author%3Adexhunter+is%3Amerged">View PRs</a></td><td>Sep&nbsp;2026</td></tr>
</tbody>
</table>

<details>
<summary>12 more non-AI projects (under 1,000 stars)</summary>

<table>
<thead><tr><th width="460">Project</th><th width="80">Stars</th><th width="130">Contributions</th><th width="100">Latest</th></tr></thead>
<tbody>
<tr><td><img src="https://avatars.githubusercontent.com/u/9341563?v=4&amp;s=40" width="16" height="16" alt=""> <a href="https://github.com/tuna/blogroll">tuna/blogroll</a></td><td align="right">952</td><td><a href="https://github.com/tuna/blogroll/pulls?q=is%3Apr+author%3Adexhunter+is%3Amerged">View PRs</a></td><td>Feb&nbsp;2020</td></tr>
<tr><td><img src="https://avatars.githubusercontent.com/u/185365251?v=4&amp;s=40" width="16" height="16" alt=""> <a href="https://github.com/hyperledger-cello/cello">hyperledger-cello/cello</a></td><td align="right">920</td><td><a href="https://github.com/hyperledger-cello/cello/pulls?q=is%3Apr+author%3Adexhunter+is%3Amerged">View PRs</a></td><td>Jun&nbsp;2021</td></tr>
<tr><td><img src="https://avatars.githubusercontent.com/u/1550888?v=4&amp;s=40" width="16" height="16" alt=""> <a href="https://github.com/Marigold/universal-portfolios">Marigold/universal-portfolios</a></td><td align="right">863</td><td><a href="https://github.com/Marigold/universal-portfolios/pulls?q=is%3Apr+author%3Adexhunter+is%3Amerged">View PRs</a></td><td>Nov&nbsp;2019</td></tr>
<tr><td><img src="https://avatars.githubusercontent.com/u/27145?v=4&amp;s=40" width="16" height="16" alt=""> <a href="https://github.com/joelparkerhenderson/demo-rust-axum">joelparkerhenderson/demo-rust-axum</a></td><td align="right">447</td><td><a href="https://github.com/joelparkerhenderson/demo-rust-axum/pulls?q=is%3Apr+author%3Adexhunter+is%3Amerged">View PRs</a></td><td>May&nbsp;2022</td></tr>
<tr><td><img src="https://avatars.githubusercontent.com/u/7657900?v=4&amp;s=40" width="16" height="16" alt=""> <a href="https://github.com/hyperledger/fabric-sdk-py">hyperledger/fabric-sdk-py</a></td><td align="right">416</td><td><a href="https://github.com/hyperledger/fabric-sdk-py/pulls?q=is%3Apr+author%3Adexhunter+is%3Amerged">View PRs</a></td><td>May&nbsp;2021</td></tr>
<tr><td><img src="https://avatars.githubusercontent.com/u/5173244?v=4&amp;s=40" width="16" height="16" alt=""> <a href="https://github.com/dimpurr/awesome-acg-machine-learning">dimpurr/awesome-acg-machine-learning</a></td><td align="right">120</td><td><a href="https://github.com/dimpurr/awesome-acg-machine-learning/pulls?q=is%3Apr+author%3Adexhunter+is%3Amerged">View PRs</a></td><td>Oct&nbsp;2018</td></tr>
<tr><td><img src="https://avatars.githubusercontent.com/u/4198311?v=4&amp;s=40" width="16" height="16" alt=""> <a href="https://github.com/skyzh/skyzh-site">skyzh/skyzh-site</a></td><td align="right">24</td><td><a href="https://github.com/skyzh/skyzh-site/pulls?q=is%3Apr+author%3Adexhunter+is%3Amerged">View PRs</a></td><td>Jul&nbsp;2021</td></tr>
<tr><td><img src="https://avatars.githubusercontent.com/u/82892425?v=4&amp;s=40" width="16" height="16" alt=""> <a href="https://github.com/awesome-xjtlu/wiki">awesome-xjtlu/wiki</a></td><td align="right">16</td><td><a href="https://github.com/awesome-xjtlu/wiki/pulls?q=is%3Apr+author%3Adexhunter+is%3Amerged">View PRs</a></td><td>Jun&nbsp;2021</td></tr>
<tr><td><img src="https://avatars.githubusercontent.com/u/167147327?v=4&amp;s=40" width="16" height="16" alt=""> <a href="https://github.com/IntensiveCoLearning/Ethereum-Protocol-Fellowship-3">IntensiveCoLearning/Ethereum-Protocol-Fellowship-3</a></td><td align="right">10</td><td><a href="https://github.com/IntensiveCoLearning/Ethereum-Protocol-Fellowship-3/pulls?q=is%3Apr+author%3Adexhunter+is%3Amerged">View PRs</a></td><td>Mar&nbsp;2025</td></tr>
<tr><td><img src="https://avatars.githubusercontent.com/u/167147327?v=4&amp;s=40" width="16" height="16" alt=""> <a href="https://github.com/IntensiveCoLearning/ai-agent">IntensiveCoLearning/ai-agent</a></td><td align="right">8</td><td><a href="https://github.com/IntensiveCoLearning/ai-agent/pulls?q=is%3Apr+author%3Adexhunter+is%3Amerged">View PRs</a></td><td>May&nbsp;2025</td></tr>
<tr><td><img src="https://avatars.githubusercontent.com/u/4354888?v=4&amp;s=40" width="16" height="16" alt=""> <a href="https://github.com/xieyuheng/awesome-why">xieyuheng/awesome-why</a></td><td align="right">1</td><td><a href="https://github.com/xieyuheng/awesome-why/pulls?q=is%3Apr+author%3Adexhunter+is%3Amerged">View PRs</a></td><td>Jul&nbsp;2019</td></tr>
<tr><td><img src="https://avatars.githubusercontent.com/u/167147327?v=4&amp;s=40" width="16" height="16" alt=""> <a href="https://github.com/IntensiveCoLearning/running">IntensiveCoLearning/running</a></td><td align="right">0</td><td><a href="https://github.com/IntensiveCoLearning/running/pulls?q=is%3Apr+author%3Adexhunter+is%3Amerged">View PRs</a></td><td>May&nbsp;2025</td></tr>
</tbody>
</table>

</details>

<!-- OSS-PRS:END -->

## 📚 Publications

- *AIDE: AI-Driven Exploration in the Space of Code* ([arXiv](https://arxiv.org/abs/2502.13138)), arXiv preprint, 2025
- *Lightweight and Unobtrusive Data Obfuscation at IoT Edge for Remote Inference* ([DOI](https://doi.org/10.1109/JIOT.2020.2983278)), IEEE Internet of Things Journal, 2020
- *Challenges of Privacy-Preserving Machine Learning in IoT* ([DOI](https://doi.org/10.1145/3363347.3363357)), ACM AIChallengeIoT, 2019
- *A Deep Reinforcement Learning Framework for the Financial Portfolio Management Problem* ([arXiv](https://arxiv.org/abs/1706.10059)), arXiv preprint, 2017

## 🎤 Talks

- **Hands-on AutoResearch: Cracking OpenAI's Parameter Golf** — workshop with the Weco AI team, [AI Engineer World's Fair 2026](https://www.ai.engineer/worldsfair/2026/schedule)
- **[Algorithmic Trading Workshop](https://slides.dex.moe)** — Network School, first cohort (2024)
- **[Deep Learning for Power System Security Assessment](https://slides.dex.moe)** (2019)
- **[Introduction to Hyperledger Fabric](https://slides.dex.moe)** (2019)

## 🏅 Awards

- 🏆 Special Prize (US$10,000), Wanxiang Blockchain Hackathon by QTUM (2018)
- 🥇 1st Prize, EOS Hackathon Hangzhou (team, 2018)
- 🥇 1st Prize, Hack x FDU 2017 Hackathon (out of more than 70 teams)
- 🥈 2nd Prize, XJTLU Blockchain Technology Application Innovation & Entrepreneurship Challenge (2020)
- 🥈 2nd Prize, XJTLU & PNP AI Innovation Hackathon (2018)
- 🥉 3rd Prize, EOS Hackathon Hangzhou (individual, 2018)
- 🥉 3rd Prize, DoraHacks x BCH Faith Hack (2018)
- 🏆 IBM Student Innovation Lab Program Award (2017)
- 🎓 Hyperledger Diversity Scholarship, Hyperledger Global Forum (2020)
- 🎓 CNCF Diversity Scholarship, KubeCon + CloudNativeCon China (2018)

## ⏱ [Vibe Clock](https://github.com/dexhunter/vibe-clock)

An open-source tool I built: WakaTime-style usage tracking for Claude Code, Codex, and OpenCode. The charts below show my own usage, with repeating animations and daily updates.

<p align="center">
  <img src="https://raw.githubusercontent.com/dexhunter/dexhunter/refs/heads/master/images/vibe-clock-card.svg" alt="Vibe Clock Stats" />
</p>
<p align="center">
  <img src="https://raw.githubusercontent.com/dexhunter/dexhunter/refs/heads/master/images/vibe-clock-donut.svg" alt="Model Usage" />
  <img src="https://raw.githubusercontent.com/dexhunter/dexhunter/refs/heads/master/images/vibe-clock-token-bars.svg" alt="Token Usage by Model" />
</p>
<p align="center">
  <img src="https://raw.githubusercontent.com/dexhunter/dexhunter/refs/heads/master/images/vibe-clock-hourly.svg" alt="Activity by Hour" />
  <img src="https://raw.githubusercontent.com/dexhunter/dexhunter/refs/heads/master/images/vibe-clock-weekly.svg" alt="Activity by Day of Week" />
</p>
