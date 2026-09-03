<div align="center">
<h1 align="center">Hi👋 Dex here. Welcome to my page!</h1>
</div>

<p align="center">
  <a href="https://github.com/dexhunter"><img src="https://img.shields.io/github/followers/dexhunter.svg?label=GitHub&style=flat-square" alt="GitHub"></a>
  <a href="https://scholar.google.co.jp/citations?user=8Ez_u30AAAAJ&hl=en"><img src="https://img.shields.io/endpoint?url=https%3A%2F%2Fraw.githubusercontent.com%2Fdexhunter%2Fdexhunter%2Fmaster%2Fimages%2Fgoogle-scholar-citations.json&style=flat-square" alt="Google Scholar citations"></a>
  <a href="#-open-source"><img src="https://img.shields.io/endpoint?url=https%3A%2F%2Fraw.githubusercontent.com%2Fdexhunter%2Fdexhunter%2Fmaster%2Fimages%2Foss-prs.json&style=flat-square" alt="Open source projects"></a>
  <a href="https://stackoverflow.com/users/3253000/dexhunter"><img src="https://img.shields.io/stackexchange/stackoverflow/r/3253000?style=flat-square&label=Stack%20Overflow&logo=stackoverflow&logoColor=white&color=orange" alt="Stack Overflow reputation"></a>
  <a href="https://dex.moe"><img src="https://img.shields.io/badge/Website-dex.moe-red?style=flat-square" alt="Website"></a>
  <a href="mailto:i@dex.moe"><img src="https://img.shields.io/badge/-Email-red?style=flat-square&logo=gmail&logoColor=white" alt="Email"></a>
</p>

## 👨‍💻 About

I'm a Member of Technical Staff at [Weco AI](https://github.com/wecoai), where I build autonomous agents for long-horizon research work — agents that write code, run it against a metric, and keep improving it without supervision. I entered one in [OpenAI's Parameter Golf](https://github.com/openai/parameter-golf) (18 March – 30 April 2026), which drew 2,000+ submissions from 1,000+ participants. Seven of the 46 entries in the official [record-track directory](https://github.com/openai/parameter-golf/tree/main/records/track_10min_16mb) are mine, more than any other participant — the next-best holds two. OpenAI's [retrospective](https://openai.com/index/what-parameter-golf-taught-us/) picked [one of them](https://github.com/openai/parameter-golf/pull/1060) as one of nine record-track submissions it chose to highlight, which OpenAI said "extended earlier quantization work into a stronger compression path".

I co-authored [AIDE](https://arxiv.org/abs/2502.13138), a tree-search agent that writes and improves machine learning code, and I've [contributed](https://github.com/WecoAI/aideml/pulls?q=is%3Apr+author%3Adexhunter+is%3Amerged) to its codebase since 2024. OpenAI's [GPT-4.5 system card](https://cdn.openai.com/gpt-4-5-system-card-2272025.pdf) ran its MLE-bench evaluations of GPT-4.5, o1 and o3-mini "using the AIDE agent", and Meta FAIR's [AI Research Agents](https://arxiv.org/abs/2507.02554) calls AIDE "the state-of-the-art approach" and rebuilds it as the baseline agent it measures against. Separately, I've [contributed](https://github.com/UKGovernmentBEIS/inspect_ai/pulls?q=is%3Apr+author%3Adexhunter+is%3Amerged) to Inspect, the UK AI Security Institute's open-source LLM evaluation framework — including performance work on clustered-stderr scoring and tool-result media extraction.

Before Weco I built trading backends in Rust, Go, and Node.js at [Hex Trust](https://hextrust.com). I'm one of the two current [maintainers](https://github.com/hyperledger/fabric-sdk-py/blob/main/MAINTAINERS.md) of the Hyperledger Fabric Python SDK, a Linux Foundation project. I studied Information and Computing Sciences at the University of Liverpool and Xi'an Jiaotong-Liverpool University, with earlier research at Nanyang Technological University, Zhejiang University, and Hong Kong Baptist University.

## 🌱 Open source

**Featured**

- **[UK AI Security Institute — Inspect](https://github.com/UKGovernmentBEIS/inspect_ai)** — performance work on the UK government's LLM evaluation framework: cut clustered-stderr scoring time and memory ([#4714](https://github.com/UKGovernmentBEIS/inspect_ai/pull/4714)), and made tool-result media extraction linear in conversation length ([#4628](https://github.com/UKGovernmentBEIS/inspect_ai/pull/4628)).
- **[OpenAI Parameter Golf](https://github.com/openai/parameter-golf)** — Aiden, the autonomous research agent I built at Weco, finished as the [#1 contributor](https://www.weco.ai/blog/parameter-golf-aiden): 7 leaderboard records, against a next-best individual human of 3. The best took validation BPB to a 5-seed mean of [1.0645](https://github.com/openai/parameter-golf/pull/1769). Aiden files under my account, so those pull requests appear in the table below.
- **Agent runtimes** — merged performance work into [openclaw](https://github.com/openclaw/openclaw/pull/99714), [AutoGPT](https://github.com/Significant-Gravitas/AutoGPT/pull/13478), [goose](https://github.com/aaif-goose/goose/pull/10409), [qwen-code](https://github.com/QwenLM/qwen-code/pull/8253), [pydantic-ai](https://github.com/pydantic/pydantic-ai/pull/6485), [agno](https://github.com/agno-agi/agno/pull/8907) and [BAML](https://github.com/BoundaryML/baml/pull/3975).
- **AI research infrastructure** — cut redundant AST parsing in Sakana AI's [ShinkaEvolve](https://github.com/SakanaAI/ShinkaEvolve/pull/175) and bounded process-pool shutdown latency in [OpenEvolve](https://github.com/algorithmicsuperintelligence/openevolve/pull/469); smaller docs fixes in Meta's [aira-dojo](https://github.com/facebookresearch/aira-dojo/pull/2), Microsoft's [RD-Agent](https://github.com/microsoft/RD-Agent/pull/1249) and OpenAI's [MLE-bench](https://github.com/openai/mle-bench/pull/101).
- **[AIDE](https://github.com/WecoAI/aideml)** — contributions to the open-source tree-search agent behind my 2025 paper; it writes, evaluates, and improves machine learning code. I also contribute to [weco-cli](https://github.com/WecoAI/weco-cli), the command line tool that drives it.

Every project below links to its merged pull requests on GitHub, so anything here can be checked directly. Ranked by stars, refreshed weekly.

<!-- OSS-PRS:START -->

**Contributions to 52 open source projects — 29 of them AI or agent infrastructure.**

### AI and agent infrastructure

| Project | Stars | Contributions | Latest |
| --- | ---: | --- | --- |
| <img src="https://avatars.githubusercontent.com/u/252820863?v=4&s=40" width="16" height="16" alt=""> [openclaw/openclaw](https://github.com/openclaw/openclaw) | 389k | [View PRs](https://github.com/openclaw/openclaw/pulls?q=is%3Apr+author%3Adexhunter+is%3Amerged) | Jul 2026 |
| <img src="https://avatars.githubusercontent.com/u/130738209?v=4&s=40" width="16" height="16" alt=""> [Significant-Gravitas/AutoGPT](https://github.com/Significant-Gravitas/AutoGPT) | 187k | [View PRs](https://github.com/Significant-Gravitas/AutoGPT/pulls?q=is%3Apr+author%3Adexhunter+is%3Amerged) | Jul 2026 |
| <img src="https://avatars.githubusercontent.com/u/126733545?v=4&s=40" width="16" height="16" alt=""> [langchain-ai/langchain](https://github.com/langchain-ai/langchain) | 146k | [View PRs](https://github.com/langchain-ai/langchain/pulls?q=is%3Apr+author%3Adexhunter+is%3Amerged) | Mar 2024 |
| <img src="https://avatars.githubusercontent.com/u/80064875?v=4&s=40" width="16" height="16" alt=""> [OpenBB-finance/OpenBB](https://github.com/OpenBB-finance/OpenBB) | 73k | [View PRs](https://github.com/OpenBB-finance/OpenBB/pulls?q=is%3Apr+author%3Adexhunter+is%3Amerged) | Jul 2026 |
| <img src="https://avatars.githubusercontent.com/u/271095942?v=4&s=40" width="16" height="16" alt=""> [aaif-goose/goose](https://github.com/aaif-goose/goose) | 54k | [View PRs](https://github.com/aaif-goose/goose/pulls?q=is%3Apr+author%3Adexhunter+is%3Amerged) | Jul 2026 |
| <img src="https://avatars.githubusercontent.com/u/104874993?v=4&s=40" width="16" height="16" alt=""> [agno-agi/agno](https://github.com/agno-agi/agno) | 42k | [View PRs](https://github.com/agno-agi/agno/pulls?q=is%3Apr+author%3Adexhunter+is%3Amerged) | Jul 2026 |
| <img src="https://avatars.githubusercontent.com/u/113954515?v=4&s=40" width="16" height="16" alt=""> [invoke-ai/InvokeAI](https://github.com/invoke-ai/InvokeAI) | 28k | [View PRs](https://github.com/invoke-ai/InvokeAI/pulls?q=is%3Apr+author%3Adexhunter+is%3Amerged) | Aug 2026 |
| <img src="https://avatars.githubusercontent.com/u/141221163?v=4&s=40" width="16" height="16" alt=""> [QwenLM/qwen-code](https://github.com/QwenLM/qwen-code) | 28k | [View PRs](https://github.com/QwenLM/qwen-code/pulls?q=is%3Apr+author%3Adexhunter+is%3Amerged) | Aug 2026 |
| <img src="https://avatars.githubusercontent.com/u/110818415?v=4&s=40" width="16" height="16" alt=""> [pydantic/pydantic-ai](https://github.com/pydantic/pydantic-ai) | 20k | [View PRs](https://github.com/pydantic/pydantic-ai/pulls?q=is%3Apr+author%3Adexhunter+is%3Amerged) | Jul 2026 |
| <img src="https://avatars.githubusercontent.com/u/19834515?v=4&s=40" width="16" height="16" alt=""> [lllyasviel/style2paints](https://github.com/lllyasviel/style2paints) | 18k | [View PRs](https://github.com/lllyasviel/style2paints/pulls?q=is%3Apr+author%3Adexhunter+is%3Amerged) | Aug 2017 |
| <img src="https://avatars.githubusercontent.com/u/169612734?v=4&s=40" width="16" height="16" alt=""> [pipecat-ai/pipecat](https://github.com/pipecat-ai/pipecat) | 15k | [View PRs](https://github.com/pipecat-ai/pipecat/pulls?q=is%3Apr+author%3Adexhunter+is%3Amerged) | Jul 2026 |
| <img src="https://avatars.githubusercontent.com/u/6154722?v=4&s=40" width="16" height="16" alt=""> [microsoft/RD-Agent](https://github.com/microsoft/RD-Agent) | 14k | [View PRs](https://github.com/microsoft/RD-Agent/pulls?q=is%3Apr+author%3Adexhunter+is%3Amerged) | Sep 2025 |
| <img src="https://avatars.githubusercontent.com/u/177023663?v=4&s=40" width="16" height="16" alt=""> [tadata-org/fastapi_mcp](https://github.com/tadata-org/fastapi_mcp) | 12k | [View PRs](https://github.com/tadata-org/fastapi_mcp/pulls?q=is%3Apr+author%3Adexhunter+is%3Amerged) | Mar 2025 |
| <img src="https://avatars.githubusercontent.com/u/813142?v=4&s=40" width="16" height="16" alt=""> [phillipi/pix2pix](https://github.com/phillipi/pix2pix) | 11k | [View PRs](https://github.com/phillipi/pix2pix/pulls?q=is%3Apr+author%3Adexhunter+is%3Amerged) | Jun 2017 |
| <img src="https://avatars.githubusercontent.com/u/124114301?v=4&s=40" width="16" height="16" alt=""> [BoundaryML/baml](https://github.com/BoundaryML/baml) | 9.1k | [View PRs](https://github.com/BoundaryML/baml/pulls?q=is%3Apr+author%3Adexhunter+is%3Amerged) | Aug 2026 |
| <img src="https://avatars.githubusercontent.com/u/238764598?v=4&s=40" width="16" height="16" alt=""> [algorithmicsuperintelligence/openevolve](https://github.com/algorithmicsuperintelligence/openevolve) | 7.3k | [View PRs](https://github.com/algorithmicsuperintelligence/openevolve/pulls?q=is%3Apr+author%3Adexhunter+is%3Amerged) | Jul 2026 |
| <img src="https://avatars.githubusercontent.com/u/14957082?v=4&s=40" width="16" height="16" alt=""> [openai/parameter-golf](https://github.com/openai/parameter-golf) | 5.2k | [View PRs](https://github.com/openai/parameter-golf/pulls?q=is%3Apr+author%3Adexhunter+is%3Amerged) | Apr 2026 |
| <img src="https://avatars.githubusercontent.com/u/72518640?v=4&s=40" width="16" height="16" alt=""> [TanStack/ai](https://github.com/TanStack/ai) | 3.1k | [View PRs](https://github.com/TanStack/ai/pulls?q=is%3Apr+author%3Adexhunter+is%3Amerged) | Aug 2026 |
| <img src="https://avatars.githubusercontent.com/u/19221939?v=4&s=40" width="16" height="16" alt=""> [UKGovernmentBEIS/inspect_ai](https://github.com/UKGovernmentBEIS/inspect_ai) | 2.7k | [View PRs](https://github.com/UKGovernmentBEIS/inspect_ai/pulls?q=is%3Apr+author%3Adexhunter+is%3Amerged) | Aug 2026 |
| <img src="https://avatars.githubusercontent.com/u/15139574?v=4&s=40" width="16" height="16" alt=""> [ZhengyaoJiang/PGPortfolio](https://github.com/ZhengyaoJiang/PGPortfolio) | 1.9k | [View PRs](https://github.com/ZhengyaoJiang/PGPortfolio/pulls?q=is%3Apr+author%3Adexhunter+is%3Amerged) | Dec 2017 |

<details>
<summary>9 more AI projects</summary>

| Project | Stars | Contributions | Latest |
| --- | ---: | --- | --- |
| <img src="https://avatars.githubusercontent.com/u/14957082?v=4&s=40" width="16" height="16" alt=""> [openai/mle-bench](https://github.com/openai/mle-bench) | 1.7k | [View PRs](https://github.com/openai/mle-bench/pulls?q=is%3Apr+author%3Adexhunter+is%3Amerged) | Nov 2025 |
| <img src="https://avatars.githubusercontent.com/u/62961550?v=4&s=40" width="16" height="16" alt=""> [Farama-Foundation/ChatArena](https://github.com/Farama-Foundation/ChatArena) | 1.6k | [View PRs](https://github.com/Farama-Foundation/ChatArena/pulls?q=is%3Apr+author%3Adexhunter+is%3Amerged) | Jun 2023 |
| <img src="https://avatars.githubusercontent.com/u/132215366?v=4&s=40" width="16" height="16" alt=""> [WecoAI/aideml](https://github.com/WecoAI/aideml) | 1.5k | [View PRs](https://github.com/WecoAI/aideml/pulls?q=is%3Apr+author%3Adexhunter+is%3Amerged) | Jul 2026 |
| <img src="https://avatars.githubusercontent.com/u/140988036?v=4&s=40" width="16" height="16" alt=""> [SakanaAI/ShinkaEvolve](https://github.com/SakanaAI/ShinkaEvolve) | 1.4k | [View PRs](https://github.com/SakanaAI/ShinkaEvolve/pulls?q=is%3Apr+author%3Adexhunter+is%3Amerged) | Aug 2026 |
| <img src="https://avatars.githubusercontent.com/u/66310692?v=4&s=40" width="16" height="16" alt=""> [tongjingqi/AI-Can-Learn-Scientific-Taste](https://github.com/tongjingqi/AI-Can-Learn-Scientific-Taste) | 432 | [View PRs](https://github.com/tongjingqi/AI-Can-Learn-Scientific-Taste/pulls?q=is%3Apr+author%3Adexhunter+is%3Amerged) | Mar 2026 |
| <img src="https://avatars.githubusercontent.com/u/16943930?v=4&s=40" width="16" height="16" alt=""> [facebookresearch/aira-dojo](https://github.com/facebookresearch/aira-dojo) | 165 | [View PRs](https://github.com/facebookresearch/aira-dojo/pulls?q=is%3Apr+author%3Adexhunter+is%3Amerged) | Jul 2025 |
| <img src="https://avatars.githubusercontent.com/u/132215366?v=4&s=40" width="16" height="16" alt=""> [WecoAI/weco-cli](https://github.com/WecoAI/weco-cli) | 94 | [View PRs](https://github.com/WecoAI/weco-cli/pulls?q=is%3Apr+author%3Adexhunter+is%3Amerged) | Sep 2025 |
| <img src="https://avatars.githubusercontent.com/u/11850255?v=4&s=40" width="16" height="16" alt=""> [JeanKaddour/sokoban_speedrun](https://github.com/JeanKaddour/sokoban_speedrun) | 31 | [View PRs](https://github.com/JeanKaddour/sokoban_speedrun/pulls?q=is%3Apr+author%3Adexhunter+is%3Amerged) | Jul 2026 |
| <img src="https://avatars.githubusercontent.com/u/263072830?v=4&s=40" width="16" height="16" alt=""> [openbydesign/lush](https://github.com/openbydesign/lush) | 3 | [View PRs](https://github.com/openbydesign/lush/pulls?q=is%3Apr+author%3Adexhunter+is%3Amerged) | Aug 2026 |

</details>

<details>
<summary>23 projects outside AI</summary>

| Project | Stars | Contributions | Latest |
| --- | ---: | --- | --- |
| <img src="https://avatars.githubusercontent.com/u/85344006?v=4&s=40" width="16" height="16" alt=""> [remotion-dev/remotion](https://github.com/remotion-dev/remotion) | 58k | [View PRs](https://github.com/remotion-dev/remotion/pulls?q=is%3Apr+author%3Adexhunter+is%3Amerged) | Aug 2026 |
| <img src="https://avatars.githubusercontent.com/u/65579849?v=4&s=40" width="16" height="16" alt=""> [ManimCommunity/manim](https://github.com/ManimCommunity/manim) | 41k | [View PRs](https://github.com/ManimCommunity/manim/pulls?q=is%3Apr+author%3Adexhunter+is%3Amerged) | Aug 2026 |
| <img src="https://avatars.githubusercontent.com/u/48722593?v=4&s=40" width="16" height="16" alt=""> [python-poetry/poetry](https://github.com/python-poetry/poetry) | 34k | [View PRs](https://github.com/python-poetry/poetry/pulls?q=is%3Apr+author%3Adexhunter+is%3Amerged) | Aug 2026 |
| <img src="https://avatars.githubusercontent.com/u/5713511?v=4&s=40" width="16" height="16" alt=""> [mementum/backtrader](https://github.com/mementum/backtrader) | 23k | [View PRs](https://github.com/mementum/backtrader/pulls?q=is%3Apr+author%3Adexhunter+is%3Amerged) | Aug 2017 |
| <img src="https://avatars.githubusercontent.com/u/41247880?v=4&s=40" width="16" height="16" alt=""> [MSWorkers/support.996.ICU](https://github.com/MSWorkers/support.996.ICU) | 10k | [View PRs](https://github.com/MSWorkers/support.996.ICU/pulls?q=is%3Apr+author%3Adexhunter+is%3Amerged) | Apr 2019 |
| <img src="https://avatars.githubusercontent.com/u/1920564?v=4&s=40" width="16" height="16" alt=""> [yeasy/blockchain_guide](https://github.com/yeasy/blockchain_guide) | 7.1k | [View PRs](https://github.com/yeasy/blockchain_guide/pulls?q=is%3Apr+author%3Adexhunter+is%3Amerged) | Mar 2019 |
| <img src="https://avatars.githubusercontent.com/u/13629408?v=4&s=40" width="16" height="16" alt=""> [kubernetes/website](https://github.com/kubernetes/website) | 5.4k | [View PRs](https://github.com/kubernetes/website/pulls?q=is%3Apr+author%3Adexhunter+is%3Amerged) | Apr 2020 |
| <img src="https://avatars.githubusercontent.com/u/6407041?v=4&s=40" width="16" height="16" alt=""> [ReactiveX/RxPY](https://github.com/ReactiveX/RxPY) | 5.0k | [View PRs](https://github.com/ReactiveX/RxPY/pulls?q=is%3Apr+author%3Adexhunter+is%3Amerged) | Sep 2018 |
| <img src="https://avatars.githubusercontent.com/u/1403074?v=4&s=40" width="16" height="16" alt=""> [mikedh/trimesh](https://github.com/mikedh/trimesh) | 3.7k | [View PRs](https://github.com/mikedh/trimesh/pulls?q=is%3Apr+author%3Adexhunter+is%3Amerged) | Aug 2026 |
| <img src="https://avatars.githubusercontent.com/u/15976103?v=4&s=40" width="16" height="16" alt=""> [yihong0618/GitHubPoster](https://github.com/yihong0618/GitHubPoster) | 1.9k | [View PRs](https://github.com/yihong0618/GitHubPoster/pulls?q=is%3Apr+author%3Adexhunter+is%3Amerged) | Jun 2021 |
| <img src="https://avatars.githubusercontent.com/u/21127168?v=4&s=40" width="16" height="16" alt=""> [TA-Lib/ta-lib](https://github.com/TA-Lib/ta-lib) | 1.7k | [View PRs](https://github.com/TA-Lib/ta-lib/pulls?q=is%3Apr+author%3Adexhunter+is%3Amerged) | Aug 2026 |
| <img src="https://avatars.githubusercontent.com/u/9341563?v=4&s=40" width="16" height="16" alt=""> [tuna/blogroll](https://github.com/tuna/blogroll) | 952 | [View PRs](https://github.com/tuna/blogroll/pulls?q=is%3Apr+author%3Adexhunter+is%3Amerged) | Feb 2020 |
| <img src="https://avatars.githubusercontent.com/u/185365251?v=4&s=40" width="16" height="16" alt=""> [hyperledger-cello/cello](https://github.com/hyperledger-cello/cello) | 918 | [View PRs](https://github.com/hyperledger-cello/cello/pulls?q=is%3Apr+author%3Adexhunter+is%3Amerged) | Jun 2021 |
| <img src="https://avatars.githubusercontent.com/u/1550888?v=4&s=40" width="16" height="16" alt=""> [Marigold/universal-portfolios](https://github.com/Marigold/universal-portfolios) | 858 | [View PRs](https://github.com/Marigold/universal-portfolios/pulls?q=is%3Apr+author%3Adexhunter+is%3Amerged) | Nov 2019 |
| <img src="https://avatars.githubusercontent.com/u/27145?v=4&s=40" width="16" height="16" alt=""> [joelparkerhenderson/demo-rust-axum](https://github.com/joelparkerhenderson/demo-rust-axum) | 442 | [View PRs](https://github.com/joelparkerhenderson/demo-rust-axum/pulls?q=is%3Apr+author%3Adexhunter+is%3Amerged) | May 2022 |
| <img src="https://avatars.githubusercontent.com/u/7657900?v=4&s=40" width="16" height="16" alt=""> [hyperledger/fabric-sdk-py](https://github.com/hyperledger/fabric-sdk-py) | 416 | [View PRs](https://github.com/hyperledger/fabric-sdk-py/pulls?q=is%3Apr+author%3Adexhunter+is%3Amerged) | May 2021 |
| <img src="https://avatars.githubusercontent.com/u/5173244?v=4&s=40" width="16" height="16" alt=""> [dimpurr/awesome-acg-machine-learning](https://github.com/dimpurr/awesome-acg-machine-learning) | 120 | [View PRs](https://github.com/dimpurr/awesome-acg-machine-learning/pulls?q=is%3Apr+author%3Adexhunter+is%3Amerged) | Oct 2018 |
| <img src="https://avatars.githubusercontent.com/u/4198311?v=4&s=40" width="16" height="16" alt=""> [skyzh/skyzh-site](https://github.com/skyzh/skyzh-site) | 24 | [View PRs](https://github.com/skyzh/skyzh-site/pulls?q=is%3Apr+author%3Adexhunter+is%3Amerged) | Jul 2021 |
| <img src="https://avatars.githubusercontent.com/u/82892425?v=4&s=40" width="16" height="16" alt=""> [awesome-xjtlu/wiki](https://github.com/awesome-xjtlu/wiki) | 16 | [View PRs](https://github.com/awesome-xjtlu/wiki/pulls?q=is%3Apr+author%3Adexhunter+is%3Amerged) | Jun 2021 |
| <img src="https://avatars.githubusercontent.com/u/167147327?v=4&s=40" width="16" height="16" alt=""> [IntensiveCoLearning/Ethereum-Protocol-Fellowship-3](https://github.com/IntensiveCoLearning/Ethereum-Protocol-Fellowship-3) | 10 | [View PRs](https://github.com/IntensiveCoLearning/Ethereum-Protocol-Fellowship-3/pulls?q=is%3Apr+author%3Adexhunter+is%3Amerged) | Mar 2025 |
| <img src="https://avatars.githubusercontent.com/u/167147327?v=4&s=40" width="16" height="16" alt=""> [IntensiveCoLearning/ai-agent](https://github.com/IntensiveCoLearning/ai-agent) | 8 | [View PRs](https://github.com/IntensiveCoLearning/ai-agent/pulls?q=is%3Apr+author%3Adexhunter+is%3Amerged) | May 2025 |
| <img src="https://avatars.githubusercontent.com/u/4354888?v=4&s=40" width="16" height="16" alt=""> [xieyuheng/awesome-why](https://github.com/xieyuheng/awesome-why) | 1 | [View PRs](https://github.com/xieyuheng/awesome-why/pulls?q=is%3Apr+author%3Adexhunter+is%3Amerged) | Jul 2019 |
| <img src="https://avatars.githubusercontent.com/u/167147327?v=4&s=40" width="16" height="16" alt=""> [IntensiveCoLearning/running](https://github.com/IntensiveCoLearning/running) | 0 | [View PRs](https://github.com/IntensiveCoLearning/running/pulls?q=is%3Apr+author%3Adexhunter+is%3Amerged) | May 2025 |

</details>

<!-- OSS-PRS:END -->

## 📚 Publications

- *AIDE: AI-Driven Exploration in the Space of Code* ([arXiv](https://arxiv.org/abs/2502.13138)), arXiv preprint, 2025
- *Lightweight and Unobtrusive Data Obfuscation at IoT Edge for Remote Inference* ([DOI](https://doi.org/10.1109/JIOT.2020.2983278)), IEEE Internet of Things Journal, 2020
- *Challenges of Privacy-Preserving Machine Learning in IoT* ([DOI](https://doi.org/10.1145/3363347.3363357)), ACM AIChallengeIoT, 2019
- *A Deep Reinforcement Learning Framework for the Financial Portfolio Management Problem* ([arXiv](https://arxiv.org/abs/1706.10059)), arXiv preprint, 2017

Citation counts are on [Google Scholar](https://scholar.google.co.jp/citations?user=8Ez_u30AAAAJ&hl=en).

## 🎤 Talks

- **Hands-on AutoResearch: Cracking OpenAI's Parameter Golf** — workshop with the Weco AI team, [AI Engineer World's Fair 2026](https://www.ai.engineer/worldsfair/2026/schedule)
- **[Algorithmic Trading Workshop](https://slides.dex.moe)** (2024)
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

An open-source tool I built: WakaTime-style usage tracking for Claude Code, Codex, and OpenCode. The charts below are my own usage, refreshed daily.

<p align="center">
  <img src="images/vibe-clock-card.svg" alt="Vibe Clock Stats" />
</p>
<p align="center">
  <img src="images/vibe-clock-donut.svg" alt="Model Usage" />
  <img src="images/vibe-clock-token-bars.svg" alt="Token Usage by Model" />
</p>
<p align="center">
  <img src="images/vibe-clock-hourly.svg" alt="Activity by Hour" />
  <img src="images/vibe-clock-weekly.svg" alt="Activity by Day of Week" />
</p>
