# Analysis Framework

Use this framework for AI research papers. Keep the analysis technical, skeptical, and traceable to evidence.

## Required Typst Sections

1. Metadata
2. One-Sentence Thesis
3. Research Question
4. Previous Gaps and Root Cause
5. Proposed Solution Overview
6. Model Architecture Design
7. Mathematical and Algorithmic Core
8. Claims and Evidence Map
9. Data, Tasks, and Evaluation Protocol
10. Experimental Validation by Claim
11. Unsupported or Weakly Supported Claims
12. Relationship to the Field
13. Core Assumptions
14. Limitations and Failure Modes
15. Reviewer Case for Rejection
16. Reviewer Case for Acceptance
17. Overall Evaluation and Research Taste
18. Red-Team Review
19. Knowledge-Graph Hooks
20. Reading Notes and Open Questions
21. References Checked

## Metadata Fields

- Authors
- Affiliations
- Venue / Journal / Conference
- Year
- Paper URL
- arXiv URL
- OpenReview URL
- Code URL
- Project URL
- Scope / Subfield
- Task
- Model / Method family
- Data sources
- Artifact status

## Analysis Stance

### Research question

Write the research question as a testable technical question:

- What is the target task?
- What setting, data regime, deployment constraint, or user need makes the task hard?
- What exact capability is missing from previous work?
- What would count as solving the problem?

Avoid generic formulations like "the paper improves performance". Prefer concrete forms such as "Can a model produce calibrated, spatially coherent 90-minute radar nowcasts for heavy rain without the blur induced by pixelwise losses?"

### Previous gaps and root cause

Identify the prior baseline or SOTA the paper argues against. Classify the claimed pain point:

- Compute efficiency
- Sample efficiency
- Generalization
- Robustness
- Training stability
- Long-context or memory bottleneck
- Reasoning or planning failure
- Alignment or safety failure
- Evaluation contamination
- Deployment cost or latency

Then explain the proposed root cause from the paper's own logic: architecture, objective mismatch, optimization geometry, data distribution, scaling law, inductive bias, approximation error, retrieval quality, or systems constraint. Distinguish author-provided explanation from your own interpretation.

For each previous method family, capture:

- What it does well.
- What it fails to do.
- Why it fails according to the paper.
- Whether that root-cause diagnosis is proven, plausible, or merely asserted.

### Proposed solution overview

Extract the core intervention:

- New architecture or module
- Loss/objective
- Training curriculum or data mixture
- Inference-time algorithm
- Retrieval, tool use, memory, or agent loop
- Alignment or preference optimization method
- Evaluation benchmark or protocol
- Systems optimization

Explain how the intervention targets the root cause. If the connection is weak, say so.

### Model architecture design

This section must be concrete enough that an engineer can sketch the model without rereading the paper. Extract:

- Inputs, outputs, time horizon, modalities, and tensor/spatial sizes if given.
- Major modules and their order.
- Information flow through the architecture.
- Conditioning, latent variables, memory, recurrence, attention, retrieval, tools, or external modules.
- Losses/objectives and what behavior each term is supposed to induce.
- Training procedure, sampling/inference procedure, and deployment-time differences from training.
- Design rationale: why this module should solve the stated root cause.
- Engineering details: compute, batch size, optimizer, preprocessing, postprocessing, data balancing, implementation constraints, and runtime.

Separate "paper explicitly states" from "architecture inference". Do not fill missing dimensions or hyperparameters from intuition.

### Mathematical and algorithmic core

Reconstruct only what is in the paper:

- State variables, inputs, outputs, and objective.
- Key equations and what each term controls.
- Optimization or inference procedure.
- Complexity claims.
- Assumptions required for proofs or derivations.

Do not invent missing derivations. If an equation is underspecified, mark it.

### Claims and evidence map

Extract the paper's central claims before writing the experiment section. Use a compact table or bullet matrix:

- Claim ID.
- Claim text in your words.
- Claim type: novelty, accuracy, efficiency, robustness, generalization, interpretability, safety, theoretical, deployment value, or engineering practicality.
- Evidence offered: figure/table/section/appendix.
- Evidence status: supported, partially supported, weakly supported, unsupported.
- Notes on missing evidence or confounders.

Claims include explicit author claims and major implied claims needed for the paper's story. Do not add claims the authors never make.

### Data and evaluation

Extract:

- Dataset names, sources, licenses if stated.
- Modalities.
- Preprocessing and filtering.
- Train/validation/test split.
- Metrics and why they are appropriate.
- Baselines and whether they are current, tuned, and comparable.
- Compute budget and implementation details.

Flag leakage risks, benchmark saturation, cherry-picked tasks, weak baselines, missing ablations, and metric mismatch.

### Experimental validation by claim

For each central experiment, state:

- Purpose of the experiment.
- Dataset and metric.
- Compared baselines.
- Relevant Figure/Table number.
- Which claim ID it is meant to support.
- Why this experiment is necessary for the paper's argument.
- What the result supports.
- What it does not support.
- What alternative explanation remains possible.

Separate main-table evidence, ablation evidence, diagnostic evidence, robustness evidence, and qualitative examples.

Do not write experiments as a chronological list only. The reader should see the proof structure: claim -> experiment -> evidence -> residual weakness.

### Unsupported or weakly supported claims

Create a dedicated section for claims that are not fully proven. Include:

- Overbroad claims relative to the tested setting.
- Claims supported only by qualitative examples.
- Claims that depend on weak or outdated baselines.
- Claims lacking ablation, sensitivity analysis, statistical testing, or external validation.
- Claims whose metrics do not match the real-world objective.

Be fair: a claim can be important and still only partially supported.

### Relationship to the field

Connect the paper to:

- Earlier methods it builds on.
- Contemporary alternatives.
- Field consensus.
- Known objections or negative results.
- Follow-up papers if relevant and verified.

Use real paper titles and venues or links. Do not cite vague "some work".

### Core assumptions

Make the paper's assumptions explicit before discussing limitations. Include:

- Problem assumptions: what setting must be true for the research question to matter?
- Data assumptions: what distribution, labels, annotations, simulators, sensors, or user feedback must be reliable?
- Model assumptions: what inductive bias, architecture choice, objective, scaling behavior, or optimization behavior must hold?
- Evaluation assumptions: why do these metrics, baselines, splits, and human studies actually measure the target capability?
- Deployment assumptions: what latency, cost, privacy, safety, robustness, or integration assumptions are required for real use?

For each assumption, state whether it is verified, plausible but unverified, fragile, or contradicted by evidence.

### Limitations and failure modes

Include both explicit limitations and reviewer-inferred limitations/failure modes:

- Hyperparameter sensitivity.
- Hidden compute or data dependence.
- Edge cases.
- Distribution shift.
- Theoretical assumptions.
- Scaling behavior.
- Reproducibility gaps.
- Human evaluation weaknesses.
- Deployment constraints.

Label inferred limitations as inference.

### Reviewer case for rejection

Write the strongest fair rejection argument, as if you were a strict reviewer. Include:

- The single most serious reason to reject.
- The second-order concerns that compound it.
- Which claims are overreaching relative to evidence.
- Which missing baseline, ablation, proof, dataset, or evaluation would be required.
- Whether the flaw is fatal or fixable.

Do not exaggerate. A good rejection case should be hard for the authors to dismiss.

### Reviewer case for acceptance

Write the strongest fair acceptance argument. Include:

- What is genuinely new or valuable.
- Why the problem matters.
- Why the evidence is strong enough despite limitations.
- What the paper changes about the field's way of thinking or engineering practice.
- Why the work deserves publication even if some claims are imperfect.

This section should help identify the real contribution, not just repeat positive results.

### Overall evaluation and research taste

Give a final technical judgment:

- What is genuinely valuable?
- What is the core scientific taste of the work?
- What is mainly engineering execution?
- What is likely to survive as a field contribution?
- How does it compare to prior and later work?
- What should future work fix first?
- Is the direction worth following, and for whom?
- What would a high-taste next paper in this line do differently?

This should not repeat the TL;DR. It should synthesize the claim/evidence balance.

### Red-team review

Write as a strict top-conference reviewer:

- What core assumption could be false?
- Which derivation step is fragile?
- Which experiment could be confounded?
- Which baseline is missing?
- Which ablation would most threaten the paper's story?
- What stress test would reveal failure?
- Where might the paper over-explain a lucky empirical result?

Do not be performatively harsh. Be precise.

## Evidence Tags

Use these tags in notes when helpful:

- `[Paper]` direct claim from the paper.
- `[Experiment]` result supported by a figure/table.
- `[External]` verified external literature.
- `[Inference]` your reasoned interpretation.
- `[Missing]` information not found.
- `[Risk]` reproducibility, validity, or deployment concern.
