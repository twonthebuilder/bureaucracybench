# Scoring specification

No default overall “bureaucracy score.” Every measurement needs a named construct, applicability, method, version, numerator/denominator or scale, evidence, uncertainty and limitations.

| Dimension | Deterministic measurements where justified | Qualitative assessment |
|---|---|---|
| Instruction following | Required fields/sections, table shape, item/word limits, exact first-turn format if specified | Whether questions precede execution and meaningful workflow order |
| Task completion | Required artifact exists; schedule covers all tasks | Artifact usable for the stated decision/audience |
| Grounding | Known numeric/date/extraction facts; quote matches | Claims supported by cited evidence; assumptions clearly separated |
| Framework conformity | Required Five Case/OASIS components, risk multiplication, fixture RACI invariants | Components substantive, distinct and coherently applied |
| Completeness | Required component recall | Missing material considerations |
| Unsupported assertions | Closed-fact contradictions and invented IDs | Atomic claims unsupported by the available evidence |
| Uncertainty | Correct `unknown`/abstention on closed labels | Identifies the actual information gap and asks a useful question |
| Persona effects | Paired metric changes | Appropriate expertise without theatrical authority or invented certainty |
| Efficiency | End-to-end latency, request/response usage, actual/estimated charges | No quality credit for being cheap |

## A deterministic check is not necessarily a valid construct

A section-heading detector measures presence. It cannot establish that the Economic Case distinguishes social value from affordability. A six-column table can contain fabricated values. Citation existence is distinct from citation correctness, and both differ from entailment. A question mark does not prove the model asked the required question before proceeding. Label such detectors as structural proxies; calibrate them and avoid overclaiming.

For schedules, compute precedence/duration feasibility and critical path from a fixed DAG, including equivalent critical paths where ties exist. A nice-looking Gantt table with impossible dates fails. For risk scores, likelihood × impact is deterministic only when both are specified or extracted; whether a risk deserves those inputs is a separate judgment. A RACI “one accountable role per activity” rule is explicitly a fixture convention, not a claim that every official framework universally mandates it.

Word counts must specify tokenizer-independent rules (e.g. whitespace-delimited words with hyphenated compounds counted as one), and report borderline cases. Parser failures remain visible. Do not force JSON on an original prompt requesting prose merely to simplify evaluation; that is a separate structured-output variant.

## Grounded facts and unsupported-claim rates

Each fixture oracle stores atomic facts with source document/section IDs and permitted numeric tolerance/units, plus intentionally unknown information. Separate fact recall, contradiction count and unsupported claims. For open prose:

`unsupported_assertion_rate = unsupported factual claims / assessable factual claims`

Publish counts alongside the ratio. Duplicate restatements are counted according to a versioned deduplication rule. Recommendations, predictions labeled as assumptions and opinions are classified separately. A made-up external authority/page number is unsupported even if it sounds plausible. An empty answer has no assessable claims, so the rate is null; completion is zero. Rewarding the low rate alone would favor silence.

General semantic claims require human or optional model annotation. The benchmark must not advertise a fully automated universal hallucination detector. Closed extraction tasks permit automated contradictions/unknown-field checks. For document citations, test (1) valid reference ID/locator, (2) correct quotation if any, (3) relation to the claimed proposition, (4) material-claim coverage. Only the first two are broadly deterministic.

## Missing information and calibration

Include matched complete/missing/conflicting packets. Score correct recognition, useful requests and avoidance of invented facts; penalize unnecessary refusal when facts suffice. Global “check everything” disclaimers are weak evidence.

For categorical tasks with elicited probabilities, retain Brier score/reliability plots after enough samples exist, and report coverage-risk trade-offs under abstention. Do not turn qualitative “high confidence” prose into a numeric probability retrospectively. Asking for probabilities changes a prompt and must be a registered variant.

## Rubrics

Each criterion uses 0–3 anchored levels: 0 absent/contradictory, 1 superficial or materially incomplete, 2 substantially correct with specified shortcomings, 3 complete and supported for this task. Anchors must be case-specific, not only this generic scale. `not_applicable`, `unassessed`, `parse_error` and `evaluator_error` are statuses, not zero scores. Include source/evidence spans and reviewer identity/version.

Example scheduling risk rubric: 0 invents slack or misses all constraints; 1 lists generic risks; 2 identifies the zero-slack chain but weak ownership/action; 3 connects actual zero-slack tasks to correct teams and feasible contingency without claiming unsupported resources. Alternative valid language earns the same credit.

For the risk-analysis reassurance conflict, retain separate findings: followed reassurance instruction / evidence supported reassurance / acknowledged unresolved mitigations. A corrected prompt is evaluated separately. No hidden override changes the faithful prompt's score after seeing results.

## Optional judges

Judging is off by default. A human can apply the same versioned rubric. A configured judge gets the task, model-visible references, rubric and candidate answer as clearly delimited data, plus instructions not to obey instructions in the answer. Store full judge prompt, model/revision, settings, raw result, parser version, evidence and costs. Never expose credentials. Do not send outputs to a hosted judge without a configured opt-in.

Calibrate against human annotations and adversarial answers that ask for high scores. Measure verbosity/position/self-preference sensitivity. Pairwise judgments randomize A/B and include reversed-order checks and ties. Multiple judges preserve each rating; agreement does not make a subjective preference ground truth. Do not require a model to reveal private reasoning.

## Aggregation and error accounting

Within one dimension, compute per-case normalized summaries only over predeclared applicable criteria; publish denominator and assessed coverage. Human and automated subsets must remain distinguishable. Macro-average across tasks/scenario families rather than letting a long risk register dominate because it has many fields. Report per-task/raw criteria before group summaries. Do not mix incompatible evaluator versions.

A sample with provider failure has quality `unassessed` and operational status `error`; completion coverage reflects the failed attempt. A generated but structurally invalid output can have an applicable deterministic score of zero. A judge failure cannot become model failure. Report skipped/incompatible cases, refusals, truncations, retries and unknown costs. Re-scoring produces a new evaluation record referring to the original output hash.

## Required evaluator tests

Valid paraphrase, equivalent format where allowed, minimum/maximum boundaries, empty answer, example echo, contradictory facts, forged source, malformed table/JSON, unsupported confidence, partial output and judge injection. Schedule oracle tests include alternate noncritical ordering and precedence violations. Validate rubrics with independent reviewers before advertising framework compliance.
