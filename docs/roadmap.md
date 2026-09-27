# Incremental roadmap and v0.1 boundary

## Foundation delivered

- Complete observed 47-prompt inventory and 119-page extracted research archive, including 17 explicit verification statements.
- Research answers, source caveats, task taxonomy, experimental/scoring protocol and provider/corpus design.
- Three fictional scenarios and four worked **draft** cases; no empirical results.
- Six-cell plain/CRIT/PICSE × persona experiment; information parity checked offline.
- Draft schemas and typed provider contract; standard-library integrity tests.

## Twelve base tasks for the first runnable release

| ID | Source task | Source Verified? | Scenario / key check | Release work still needed |
|---|---|---|---|---|
| BB-GANTT-001 | Create a Gantt-style project schedule | Yes | Northbridge; DAG/critical path | Renderer and schedule evaluator, human rubric calibration |
| BB-RACI-001 | Create a governance structure and RACI matrix | Yes | Northbridge; threshold inquiry and fixture roles | Freeze Teal Book; dialogue; RACI evaluator |
| BB-RISK-001 | Develop a risk register | Yes | Northbridge; score arithmetic and unsupported estimates | Reference editions/PDS; risk facts and semantic rubric |
| BB-BUSINESS-001 | Develop a business case summary | Yes | Northbridge; complete/missing fact conditions | Historical Green Book/business-case packet; Five Case rubric |
| BB-COMMS-001 | Create a communication plan | Yes | Eastborough; OASIS coherence | Teal/OASIS/GCS references and expert rubric |
| BB-BRIEFING-001 | Prepare for a briefing | Yes | Merefield; ROI cannot be inferred from incomplete costs | Briefing evaluator and rubric calibration |
| BB-PROCUREMENT-001 | Build a procurement strategy | No label | Northbridge; inquiry first, jurisdiction/regime awareness | Current commercial sources and grounded strategy rubric |
| BB-SIMPLIFY-001 | Simplify complex writing | No label | Merefield; preserve deadlines and exception | Multi-turn renderer, fact-preservation rubric |
| BB-ACTIONS-001 | Summarise daily actions | No label | Merefield synthetic mail packet | Create messages; explicit connected-tool adaptation |
| BB-PRESENTATION-001 | Turn a document into a presentation | No label | Eastborough; slides/bullets/notes and fact retention | Create document and count/grounding evaluators |
| BB-CONSULT-001 | Consult-inspired theme coding | Not a library prompt | Eastborough; multi-label reference labels | Fixed codebook, ambiguous-label policy, balanced examples |
| BB-TRIAGE-001 | HMT-inspired correspondence triage | Not a library prompt | Eastborough; eight fields/escalation | Routing/standard-line fixtures and class-wise evaluators |

Twelve base tasks do not mean only twelve model calls. Variants, evidence conditions and repetitions are explicit expansions. Include persona ablations for at least Gantt and briefing. The three-framework procurement experiment is an additional derived experimental task, not a government prompt and not counted among the twelve library/use-case base tasks. The four included draft definitions cover Gantt, briefing, simplification and procurement. None is release-ready solely because a JSON file exists.

## Milestone 1: offline vertical slice

Implement strict loaders from draft schemas, duplicate-key rejection, safe path resolution, literal rendering and fixture isolation. Promote one Gantt case after calibration; implement fake provider, append-only attempts/sample records and deterministic schedule checks. Add standard JSON Schema validation using a mature validator and negative fixtures. Generate terminal/JSON/JSONL from fake runs marked synthetic test output. Do not commit fake data as measured performance.

Acceptance: exact-message golden tests; oracle never in request; malformed references fail; valid alternate schedules pass; bad dependencies fail; no API keys/network needed. Freeze schema 0.1 only after this slice resolves ambiguities. Check whether Inspect saves executor work without losing result fidelity.

## Milestone 2: local and first hosted execution

Implement OpenAI-compatible chat with explicit endpoint/model profiles, environment keys, request/returned metadata, usage, stop reason, capability/setting errors, bounded retries and redaction. Test with a fake HTTP server; opt-in one local runtime and one hosted compatible profile. Record exact tested versions. Implement corpus/case/fixture/evaluator identities and per-run manifest.

Acceptance: no secret logging, unsupported setting is explicit, timeout preserved, aliases distinguishable, no quality-based retries, local unknown usage valid, known budgets respected. No default paid call.

## Milestone 3: interactions and quality

Implement bounded scripted dialogue; add the four draft cases, then remaining library tasks after reference packets and expert review. Implement human-rubric import/export, metric applicability and coverage. Add both persona pairs and information-matched framework experiment. Add native Anthropic adapter with conformance tests. Native Google/OpenAI Responses remain optional follow-on work.

Acceptance: clarification/approval behavior visible per turn; meaningful qualitative anchors; empty/refused/truncated outputs cannot earn high quality by omissions; independent reviewers calibrate a subset; dataset instructions cannot change runner behavior.

## Milestone 4: comparisons and release

Add the two use-case reconstructions; JSONL source of truth, long-form CSV, Markdown/terminal reports and paired comparisons. Implement multiple repetitions, order randomization, version compatibility checks and failure/uncertainty reporting. Pin tested dependency lock, obtain production-host equivalence or explicitly release only the dev-observed corpus, complete rights/reference review and publish a release manifest plus changelog.

Acceptance: twelve base tasks complete; all exact inputs/outputs inspectable; judges optional; released suite membership has no drafts; no missing-reference case silently skipped; model pilot documents limits. No claim of scientifically representative rankings from a handful of runs.

## Later, only after v0.1 works

Reviewable upstream discovery/diff command; native Google/Responses adapters; additional runtime telemetry; pairwise/multiple judges; richer finite-state dialogues; retrieval/live-source track; RACE/GCSE expansion; CLI exports to Inspect; holdout sets and power analysis; optional dashboard. No autonomous government actions, clinical decisions, real inbox connections or private-document collection.
