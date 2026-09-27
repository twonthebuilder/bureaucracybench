# Benchmark design and experimental protocol

## Unit of analysis and task taxonomy

A model is evaluated on a task/scenario/variant/repetition combination. A public prompt is not automatically a complete task or a gold answer. Preserve source category, profession, verification, contribution origin and date separately. Project tags refine discovery without rewriting upstream taxonomy.

Task families derived from the observed library: explanation/learning; writing/rewriting/style; prompt development; critical thinking; meeting preparation; personal productivity; extraction; planning/scheduling; project delivery/readiness; business cases/benefits; risk; portfolio; governance/RACI; change; stakeholder engagement; communications; procurement; assurance; briefing. Use-case reconstructions add closed classification/triage, theme analysis and reference-grounded question answering. OCR/audio/clinical inference are outside v0.1.

`benchmarks/suites.json` defines selection semantics. `full` means all released compatible cases, with incompatible planned cases listed and explained; it never silently means “whichever cases returned a good answer.” Research drafts are excluded from released runs unless an explicit development flag is recorded.

## Three fictional scenarios

1. **Northbridge Council digital permits**: task DAG, project options, costs, budgets, approval authority, go-live constraints and deliberately missing evidence. Supports Gantt, Five Case, risks, RACI, procurement, benefits and change tasks.
2. **Merefield NHS administrative logistics**: supply-delivery pilot evidence, improvement claims, readiness and a technical public notice. No patients, clinical guidance or personal data. Supports briefing, simplification and missing-evidence tests.
3. **Eastborough transport service consultation**: fictional public responses, routing rules and closed response templates. Supports Consult-inspired coding, HMT-style triage and procurement sustainability criteria.

Inputs and oracles are separate keys with a hard model-visibility boundary. Public repository access means fixtures are not secret; “oracle-only” means excluded from model requests. Add train/development and independently authored evaluation scenario families before making generalizable comparisons. Hold out complete scenario families, not paraphrases from the same story.

Difficulty is controlled through input properties: complete vs missing vs conflicting evidence; 6 vs 20 tasks/documents; explicit vs ambiguous responsibilities; direct vs distributed facts; simple vs interacting constraints. Do not define difficulty as “how badly a favored model performs.” Each level has its own ID/digest and required capability budget.

## Track A: published prompt fidelity

Replace declared placeholders and provide prerequisites. Retain source wording, including defects. Attach documents uniformly using a declared transport wrapper. Separate literal instruction compliance from professional correctness. Source-required browsing or tools cannot be falsely marked completed by an offline language-only model. Faithful cases can join `verified`; changes beyond instantiation/transport become labeled adaptations.

## Track B: persona ablation

Use at least two different task families. For each matched task compare the exact professional-role clause with the same prompt with only that role clause removed. Keep evidence, format, tools, output budget and workflow unchanged. Split mixed role/task sentences carefully: removing “You are a Project Planner” must not also remove “create a schedule.” Record exact edit spans and hashes.

Primary outcomes: task quality and groundedness. Secondary: professional tone, useful questions and unwarranted authority claims. A persona that sounds convincing but invents more facts can be a regression. A parameterized job title is not an independent task if everything else is unchanged. Wrong-role/neutral-role controls are optional later extensions, not compulsory filler.

## Track C: framework experiment

Initial controlled contrast: plain vs CRIT vs PICSE on the same transport-procurement scoring task. Two role conditions produce six cells. The experiment file contains exact prompts and common fact blocks. Each format receives the **same persona, goals, criteria, sources and example**; only packaging/order changes. Otherwise PICSE's extra example/source would confound a supposed framework effect.

Primary estimand: paired change in quality conditional on this information budget and task. A separate later ecological experiment may compare short natural prompts with naturally richer PICSE prompts, but must report the bundled information/length difference. Do not compare the Hub's original CRIT procurement example with its different PICSE stakeholder-workshop example and call that causal evidence about frameworks.

CRIT/PICSE in v0.1 is single-turn structure. Iteration is a separate factor (same number of turns, same feedback and budget) for a later experiment. RACE and GCSE are documented and reserved for expansion. Token length may still differ; report it and optionally add token-matched controls, without pretending tokenizer equivalence.

## Track D: documented workflow reconstructions

Use public tool descriptions/ATRS records to specify analogous tasks. Label as `reconstruction`; no government verification inheritance. Publish what is reproduced (e.g. eight correspondence fields) and what is omitted (SVM, retrieval system, human operations, production data). Evaluate a general-purpose model's ability on that component, not the performance of the named deployed tool.

## Preregistered pilot protocol

- v0.1 descriptive pilot: at least 3 independent repetitions per case/condition/model; 5 preferred for unstable generation. This is a practical starting point, not a power calculation.
- Freeze prompts, rubrics, test cases and model profiles before measurement. Record experiment plan digest. Calibration uses a separate development split.
- Randomize/interleave model-condition order with a recorded scheduler seed to reduce load/time confounds. Use a balanced order when API constraints allow.
- Use a documented low-variance baseline setting supported by each model. Record provider defaults where controls are unavailable; do not claim equal temperature or reasoning effort is equal behavior.
- Analyze paired differences within task/scenario. Report estimates, spread, sample counts and bootstrap intervals clustered by scenario/task, not by treating repeated outputs as independent task diversity. With only three scenario families, intervals are unstable; label exploratory and avoid broad significance claims.
- Report failure rates separately and completion rate over all planned compatible attempts. Show quality conditional on valid output AND completion coverage. Never delete operational failures or refusals from the headline context.
- Verified/unlabeled comparison is observational and confounded by task mix and complexity. Match comparable tasks or report strata; do not claim verification causes quality gains.
- For qualitative ratings, blind model identity, randomize order and use two reviewers on a calibration subset. Record adjudication and ordinal agreement (weighted kappa or agreement table); small samples may make reliability estimates imprecise.
- Multiple judges and pairwise A/B with swapped order are optional. Publish win/tie/loss and disagreements; do not convert uncalibrated preferences into an absolute accuracy score.

## Contamination and model drift

Prompts are public and may be in pretraining or tuning. New fictional facts reduce memorized-answer usefulness but do not prove uncontaminated evaluation. Reserve unseen scenario families, rotate facts only through new immutable fixture versions, compare public vs held-out development performance and disclose all training exposure known to the project. Do not submit evaluation answers to fine-tuning services by default.

Record stable provider model IDs where offered, returned aliases, date, request IDs/fingerprints, serving platform, API surface and SDK version. Pin local weight revisions/digests and quantization/runtime/chat templates. Same seed is best effort; numerical kernels, batching, routing and hosted updates can change results. Re-run baselines when upstream aliases change; do not stitch them into one model history without annotations.

## Limits of the initial science

This small, heavily project-delivery corpus is not representative of all civil-service work. A public prompt benchmark cannot establish legality, safety, deployment readiness, actual time saved or government endorsement. Quality/latency trade-offs can inform further research, but energy claims require actual instrumentation, hardware boundaries and attribution assumptions. The benchmark should publish its missing capabilities as prominently as its scores.
