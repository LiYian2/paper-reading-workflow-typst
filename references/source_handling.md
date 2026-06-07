# Source Handling

## Source Priority

1. Official conference, journal, OpenReview, arXiv, or publisher page.
2. Author project page and official repository.
3. Paper TeX source from arXiv when available.
4. Paper PDF.
5. Indexing pages such as Semantic Scholar, Papers With Code, DBLP, or Google Scholar snippets.

Use lower-priority pages for discovery, then verify important facts against higher-priority sources.

## arXiv

For an arXiv URL:

- Normalize the ID and version.
- Check abstract metadata for title, authors, categories, and date.
- Try TeX source via arXiv e-print before relying on PDF text extraction.
- Compare source version and PDF version if there are multiple versions.
- Treat arXiv category as a hint, not a venue.

## OpenReview

For OpenReview:

- Capture forum URL.
- Check accepted/rejected status, venue name, decision, and revision history when visible.
- If reviews are public, summarize field objections separately from your own objections.
- Do not quote long review passages; paraphrase with links.

## PDF Extraction

Use `markitdown` when available:

```bash
markitdown paper.pdf > paper.md
```

Then manually inspect:

- Abstract and introduction.
- Method equations.
- Algorithm blocks.
- Main result tables.
- Figures central to the argument.
- Appendix details for datasets and hyperparameters.

PDF-to-Markdown often damages equations, table layout, and captions. Treat extracted Markdown as a reading aid, not the source of record.

## Code and Artifacts

When a code URL exists:

- Verify it is official or clearly linked by authors.
- Record license and maintenance status if relevant.
- Inspect README for supported checkpoints, datasets, and reproduction commands.
- Do not assume code implements the final paper method unless linked or tagged.

## Source Log

Maintain a source log with:

- URL or file path.
- Source type.
- Access date.
- What facts were taken from it.
- Missing or ambiguous facts.
