---
name: ai-paper-reading-workflow
description: Create rigorous AI research paper readings from arXiv/OpenReview/online paper URLs or local PDFs, producing detailed Typst notes and knowledge-graph updates. Use when Codex needs to fetch or read paper sources, prefer TeX when available, convert PDFs with MarkItDown when useful, extract metadata, analyze methods/experiments/limitations with evidence discipline, or connect a paper into a research knowledge graph.
---

# AI Paper Reading Workflow

Use this skill to turn an AI research paper into a citation-grounded Typst interpretation and a structured knowledge-graph patch. Treat the output as a research artifact, not a blog summary.

## Core Workflow

1. Resolve sources.
   - Accept arXiv, OpenReview, publisher, project page, GitHub, Hugging Face, Semantic Scholar, or local PDF inputs.
   - Prefer original paper source over mirrors.
   - For arXiv, try to obtain TeX source when available; use PDF only when source is unavailable or incomplete.
   - For PDF-only inputs, use `markitdown` or another reliable extractor, then inspect important equations, tables, and figures from the PDF directly.
   - Search for linked OpenReview discussions, official code, project pages, datasets, and later versions.

2. Establish metadata before analysis.
   - Extract: title, venue or publication venue, year, authors, affiliations, paper URL, OpenReview URL if present, code URL if present, project URL if present, datasets, scope/subfield, task, model family, and artifact availability.
   - Do not infer affiliations, code links, or venue if not stated by a reliable source.
   - If venue/year are uncertain, write `Unknown` and explain the evidence gap.

3. Read with evidence discipline.
   - Separate claims made by authors, claims supported by experiments, and your own reviewer judgment.
   - Cite paper sections, equation numbers, figure/table IDs, appendix locations, or exact source documents whenever possible.
   - For external literature context, use real papers only. If browsing or retrieval is available and current context matters, verify with primary sources or stable scholarly pages.
   - Never fabricate links, baselines, dataset details, or limitations.

4. Build the claim-centered analysis before writing.
   - State the research question as a precise technical question, not a vague topic.
   - Identify what previous methods fail to do and why the paper believes they fail.
   - Explain how the proposed method attacks that failure mode.
   - Reconstruct the model architecture concretely: input/output shapes, modules, information flow, objectives, training/inference procedure, and design rationale.
   - Extract the paper's explicit claims and map every major experiment to the claim it is meant to support.
   - Mark claims as `supported`, `partially supported`, `weakly supported`, or `unsupported` with evidence.
   - Surface core assumptions separately from limitations: data, model, evaluation, and deployment assumptions.
   - Write both the strongest fair reviewer rejection case and the strongest fair reviewer acceptance case.
   - Conclude whether the direction is worth following, what future work should do, and how the paper compares to prior/later work.
   - Separate engineering/dataset facts from conceptual novelty and empirical proof.

5. Produce a Typst note.
   - Use `assets/paper_reading_template.typ` as the structure.
   - Title format: `<Paper Title> - <Venue or Journal> - <Year>`.
   - First section must be `Metadata`.
   - Follow the analysis modules in `references/analysis_framework.md`.
   - Use concise technical Chinese by default if the user writes in Chinese; preserve English terms where they are standard.

6. Produce a knowledge-graph patch.
   - Use `references/knowledge_graph_schema.md` for nodes and edges.
   - Prefer JSON or YAML patches that can be reviewed before insertion.
   - Link the paper to methods, tasks, datasets, metrics, baselines, claims, experiments, limitations, code repositories, and related papers.
   - Mark uncertain edges with `confidence` and `evidence`.

7. Validate before delivering.
   - Check that every strong claim has evidence.
   - Check that every central experiment has a purpose, setup, supported claim, and proof gap.
   - Check that the Typst file has all required sections.
   - Check that graph entities have stable IDs.
   - Run `scripts/validate_paper_note.py <note.typ>` when possible.

## Resource Guide

- Read `references/analysis_framework.md` for the required paper-reading rubric and red-team stance.
- Read `references/source_handling.md` when choosing between arXiv TeX, PDF extraction, OpenReview, or code repositories.
- Read `references/knowledge_graph_schema.md` before producing graph updates.
- Use `assets/paper_reading_template.typ` as the Typst skeleton.
- Run `scripts/create_note_scaffold.py` to generate an initial Typst note from metadata JSON.
- Run `scripts/validate_paper_note.py` for lightweight structural validation.

## Output Contract

Return or save:

1. A `.typ` file containing the detailed reading note.
2. A graph patch, preferably `<paper-id>.kg.json`.
3. A short source log listing paper PDF/TeX/OpenReview/code URLs checked, and any missing information.

When information is missing, write that it is missing. Do not smooth over gaps.
