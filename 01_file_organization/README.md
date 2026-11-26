# Exercise 01 – Organize the Chaos

**Block 1: From LLMs to AI Agents · 40 minutes of group work**

## Situation

You are taking over a research project. A colleague left behind an unstructured folder containing documents, spreadsheets, images, and notes. Filenames are inconsistent, and some files may be duplicates or outdated versions.

## Your assignment

> Analyze the folder `01_file_organization/working/` and organize the files so that a new team member can find their way around.

From the workshop repository root, open your chosen agent:

```bash
cd "$(git rev-parse --show-toplevel)"
opencode  # or: codex
```

Use either of the workshop CLI agents (`codex` or `opencode`). Start with just this open-ended assignment. Observe which files the agent actually reads, which tools it calls, and which decisions it makes independently.

**Suggested timing:** 5 minutes to explore, 20 minutes with the agent, 10 minutes to verify the result, 5 minutes to record your observations.

## Verify the result

After the agent finishes, run from the repository root:

```bash
cd "$(git rev-parse --show-toplevel)"
python3 01_file_organization/verify.py
```

The verifier downloads the pinned original into a temporary directory, compares SHA-256 hashes and reports retained, missing, duplicate and new or modified content. It does not change your working files. Renames and moves do not count as content changes. A missing copy may be a deliberate deduplication rather than information loss; review the reported paths. The comparison covers files remaining inside the working folder.

## Group discussion

- Did it inspect file contents or rely on filenames?
- Which decisions did it make without asking?
- How can we verify that it preserved information?

When comparing results, consider possible duplicates, competing versions, uncertainty, and whether any moves, overwrites, or deletions require verification.

## Source materials

The **45 entirely fictional files (16.26 MB)** are automatically downloaded to `01_file_organization/working/` when your Codespace is created. If they are missing:

```bash
cd "$(git rev-parse --show-toplevel)"
python3 01_file_organization/prepare.py
```

To restore the original files (**this deletes all your changes to the working folder**):

```bash
python3 01_file_organization/prepare.py --reset
```

The files come, unchanged, from the workshop [Using AI Agents for Reproducible Research](https://github.com/techczech/agents-for-reproducibility). See [sources and licensing](SOURCES_AND_LICENSE.md) for attribution and terms.

**Important:** Use the fictional sample data only. Do not upload real confidential documents or personal information.
