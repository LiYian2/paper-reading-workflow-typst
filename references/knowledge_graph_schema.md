# Knowledge Graph Schema

Use this schema to produce reviewable graph patches. Adapt field names to the user's existing graph store if one is present.

## Node Types

- `Paper`
- `Author`
- `Institution`
- `Venue`
- `Method`
- `Task`
- `Dataset`
- `Metric`
- `Baseline`
- `Claim`
- `Limitation`
- `CodeRepository`
- `ProjectPage`
- `RelatedPaper`
- `Concept`

## Required Paper Node

```json
{
  "id": "paper:<normalized-title-year>",
  "type": "Paper",
  "title": "",
  "venue": "",
  "year": "",
  "urls": {
    "paper": "",
    "arxiv": "",
    "openreview": "",
    "code": "",
    "project": ""
  },
  "scope": "",
  "subfield": "",
  "summary": "",
  "evidence": []
}
```

## Edge Types

- `AUTHORED_BY`
- `AFFILIATED_WITH`
- `PUBLISHED_IN`
- `PROPOSES`
- `ADDRESSES_TASK`
- `EVALUATED_ON`
- `USES_METRIC`
- `COMPARES_TO`
- `CLAIMS`
- `HAS_LIMITATION`
- `HAS_CODE`
- `HAS_PROJECT_PAGE`
- `BUILDS_ON`
- `CONTRADICTS`
- `SUPPORTS`
- `RELATED_TO`

## Edge Fields

```json
{
  "source": "paper:<id>",
  "target": "method:<id>",
  "type": "PROPOSES",
  "confidence": "high",
  "evidence": "Section 3, Algorithm 1"
}
```

Use `confidence: low` when the relation is inferred or ambiguous. Avoid inserting low-confidence graph facts silently; surface them in the source log.

## ID Normalization

- Lowercase.
- Replace spaces and punctuation with hyphens.
- Preserve meaningful acronyms when readable.
- Include year for papers.
- Include dataset or method version if needed.

Examples:

- `paper:attention-is-all-you-need-neurips-2017`
- `method:direct-preference-optimization`
- `dataset:imagenet-1k`
- `metric:pass-at-k`
