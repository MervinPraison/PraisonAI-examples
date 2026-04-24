# PraisonAI examples

This repository mirrors the [`examples`](https://github.com/MervinPraison/PraisonAI/tree/main/examples) directory from [PraisonAI](https://github.com/MervinPraison/PraisonAI). The GitHub remote is [MervinPraison/PraisonAI-examples](https://github.com/MervinPraison/PraisonAI-examples).

## Mirror contract

- **Source of truth for layout and new examples** is upstream [`PraisonAI` → `examples/`](https://github.com/MervinPraison/PraisonAI/tree/main/examples). This repo tracks that tree.
- **Automation** clones `examples/` from `main` and applies it to the repo root with `rsync --delete`, while **`.git/`** and **`.github/`** are protected so Git metadata and workflows are never removed by sync.
- Anything else at the repository root (Python trees, YAML, assets, and so on) is **mirrored from upstream** unless you later add **repo-only overlay** paths documented in [CONTRIBUTING.md](CONTRIBUTING.md) and matching `rsync` rules in the workflow. **There are no overlay directories today**—the whole mirrored tree comes from PraisonAI.

## Layout of this mirror

This mirror places the upstream `examples/` tree at the repository root. Top-level folders are language-first:

| Area | What you will find |
|------|---------------------|
| **`python/`** | Python examples (agents, workflows, tools, providers, managed agents, CLI helpers, and similar). Run scripts from the repo root, for example `python python/agents/single-agent.py`. |
| **`yaml/`** | YAML workflow definitions and related layout; see upstream [examples README](https://github.com/MervinPraison/PraisonAI/blob/main/examples/README.md) for YAML links. |
| **`typescript/`** | TypeScript/Node examples (merged from the former `js/` tree where applicable). |
| **Rust** | There is **no** `rust/` examples tree in this mirror yet. Rust SDK work lives in the main monorepo under [`src/praisonai-rust`](https://github.com/MervinPraison/PraisonAI/tree/main/src/praisonai-rust). |

For tables, quick links, and how to run samples, prefer the upstream [examples README](https://github.com/MervinPraison/PraisonAI/blob/main/examples/README.md) so you always see the latest copy.

## Sync with PraisonAI

The workflow [`.github/workflows/sync-from-praisonai.yml`](.github/workflows/sync-from-praisonai.yml) keeps this repository aligned with upstream.

| Behaviour | Detail |
|-----------|--------|
| **What is copied** | The full `examples/` directory from `MervinPraison/PraisonAI` branch `main`. |
| **Deletes** | `rsync --delete` removes files and directories in this mirror that no longer exist upstream (except protected `.git/` and `.github/`). |
| **Schedule** | Cron runs daily at **03:00 UTC**; a **three-day gate** (UTC, unix-day mod 3) skips most scheduled days so a full sync attempt runs roughly **once every three days**. |
| **Manual run** | **Actions → Sync examples from PraisonAI → Run workflow** runs immediately with no three-day gate. |
| **Pull requests** | When the mirrored tree differs from `main`, the workflow creates a branch, commits, pushes, and opens a **PR** into `main`. Nothing is pushed straight to `main` from that job. |

You can still commit **directly to `main`** in this repo (for example hotfixes). If the same paths differ upstream, a later merged sync PR will **overwrite** those paths with upstream content—prefer porting structural fixes into [PraisonAI](https://github.com/MervinPraison/PraisonAI) so they persist. See [CONTRIBUTING.md](CONTRIBUTING.md).

## Documentation

See the [PraisonAI documentation](https://docs.praison.ai) for installation and guides.
