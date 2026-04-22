# Contributing to PraisonAI-examples

This repository is primarily a **mirror** of [`PraisonAI/examples`](https://github.com/MervinPraison/PraisonAI/tree/main/examples). How you contribute depends on what you are changing.

## Where structural and new examples belong

- **New folders, renames, or large layout changes** belong in the **PraisonAI** monorepo under `examples/`, not only in this mirror. After they merge upstream, the sync workflow will propose a PR here.
- **Documentation** that describes the mirror itself (this repo’s README, this file) lives here and does not need an upstream PR unless you also want the same text in PraisonAI.

## Bugfixes and small edits

- You may open a PR or push to **`main`** here for urgent fixes to mirrored files.
- If you do **not** apply the same fix upstream, the next merged **sync PR** from PraisonAI can **revert** your change on paths that still differ upstream. For durable fixes, open a matching PR on [PraisonAI](https://github.com/MervinPraison/PraisonAI).

## Sync PRs versus manual commits

| Mechanism | Purpose |
|-----------|---------|
| **Sync PR** (from Actions) | Brings this repo in line with `MervinPraison/PraisonAI` `main` `examples/`. Review diffs like any other dependency bump. |
| **Manual commit on `main`** | For mirror-only docs, workflow tweaks, or temporary fixes—be aware of overwrite risk above. |

Resolve conflicts on sync PRs by choosing upstream intent, keeping local-only workflow or README changes, and re-applying any fix that must also land upstream.

## Repo-only overlay directories (optional)

We do **not** use overlay paths today: everything under the repo root except `.git/` and `.github/` is overwritten by the mirror rules when upstream changes.

If you add a folder that must **never** be deleted or replaced by sync (for example `playground/`), you must:

1. Add **`rsync`** protect (or exclude) rules in [`.github/workflows/sync-from-praisonai.yml`](.github/workflows/sync-from-praisonai.yml), same idea as `.github/`.
2. Document the folder in **README.md** under mirror contract.

Until then, do not rely on undocumented paths surviving sync.
