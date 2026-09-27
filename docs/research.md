# Research findings and answers

Research date: 27 September 2026. This document distinguishes observed source statements, project interpretations and unresolved questions. Source content is evidence of what the Hub said, not independent proof of the effectiveness of its advice or tools.

## Access and coverage

The supplied [production entrypoint](https://ai.gov.uk/knowledge-hub/) returned HTTP 403. Search located the public government-hosted [Knowledge Hub](https://knowledgehub.dev.ai.gov.uk/). Its [site map](https://knowledgehub.dev.ai.gov.uk/site-map), prompt index and individual pages were fetched directly over HTTPS. All 47 prompt pages, 47 tool pages, 12 how-tos, seven capability pages and six navigation/about/index pages were archived: **119 pages**. The two dot-containing routes for GOV.UK Chat and the GOV.UK style prompt initially failed without trailing slashes; their linked trailing-slash URLs succeeded. No sign-in, private pages or access-control workaround was used. Search extracts omitted an important verification banner that was present in the actual index HTML; the direct page record controls.

This is a complete enumeration of that observed public index, not proof that the inaccessible production host has the same current content. `UK-AIKH-2026-09-27-dev-observed` is a research snapshot, not an official government release. Raw-response hashes, extracted text, links, prompt bytes and per-page observation times are preserved. No official API, feed or guaranteed update schedule was established. Robots retrieval failed; future unattended crawling needs access-policy review.

## 1. What is the Hub?

The [About page](https://knowledgehub.dev.ai.gov.uk/about) describes practical cross-public-sector knowledge sharing: tools/templates, examples of adoption, experimentation and how-to guides. It explicitly says it is **not a comprehensive source of AI policy**. Therefore benchmark-source status must not be mistaken for policy authority or approval to deploy a model.

## 2. Who maintains it?

The Hub team uses `ai-knowledge-hub@dsit.gov.uk`. An official [GDS roadmap article, 20 January 2026](https://gds.blog.gov.uk/2026/01/20/our-roadmap-for-modern-digital-government/) says GDS will continue building the Hub; [MOD's official resource index](https://digital.mod.uk/policy-rules-standards-and-guidance/aiph/resource-library/cross-government-resources-and-guidance) places it under DSIT. The supported institutional attribution is **GDS/DSIT, operated by the AI Knowledge Hub team**, drawing on public-sector contributions. The examined About page does not give a precise named editorial owner, CMS operator or formal verification governance chart. Do not substitute the owner of an individual i.AI tool for the owner of the whole Hub.

## 3. How are prompts contributed?

The [About page](https://knowledgehub.dev.ai.gov.uk/about) invites public/third-sector contributions by email. It requests purpose, preparation, customization, workflow, after-use checks, level of verification and full prompt sections. Submissions are reviewed and may be tested or edited. The principles page still mentions a form, so the recorded pages are not perfectly consistent about the route. Individual submitter identity is generally unavailable; preserve it as unknown.

## 4. What does Verified mean?

The [prompt index](https://knowledgehub.dev.ai.gov.uk/prompts) banner defines it as reviewed and approved by professionals in the subject. All 17 observed explicitly labeled prompt pages state that Government Project Delivery Professionals verified the **approach**, while requiring users to check results because AI makes mistakes. See, for example, [Gantt scheduling](https://knowledgehub.dev.ai.gov.uk/prompts/create-a-gantt-style-project-schedule) and [business-case summary](https://knowledgehub.dev.ai.gov.uk/prompts/develop-a-business-case-summary).

No sample size, tested model/version/settings, success threshold, controlled evaluation, independent certification or universal reliability claim was found. Most unlabeled pages explicitly warn that the library has not been formally evaluated. The broad library warning and narrow approach-review claim can coexist. “Verified” is source metadata, never a gold correctness label.

There are 24 cards with a `data-verified-by-profession="Project delivery"` attribute but only 17 visible Verified badges. Several unlabeled prompts have that attribute. Record both; badges and individual-page verification statements determine explicit status. Verified and community origin overlap: do not invent five mutually exclusive quality tiers from the user's research categories.

## 5. How many prompts exist?

**47 in the observed index; all 47 individually inspected. 17 explicitly Verified, 30 without an explicit label.** Counts apply to the specified host and retrieval date. Full titles, URLs, dates, roles, modes and suitability notes appear in [the inventory](prompt-inventory.md); exact originals are in `corpus/snapshots/UK-AIKH-2026-09-27-dev-observed/prompts.jsonl`.

## 6. Which personas occur?

Actual model-role assignments include: expert teacher/communicator; expert in a parameterized profession; expert business-case adviser; Business Case Manager; public-sector Business Case Assessor; senior procurement and finance officer; senior/quantitatively minded Risk Manager; Benefits Manager; Business Change Manager; Change Manager; Project Planner; PMO Manager; experienced Project Manager; veteran business analyst; Portfolio Manager; stakeholder engagement lead; Stakeholder Manager; Stakeholder and Communication Manager; communications specialist; senior content designer; lead GOV.UK content designer/trusted colleague; presentation designer/communicator; parameterized senior writer; productivity/time-management coach; meeting-preparation coach; prompt engineer; prompt-optimization specialist; facilitator; intellectual sparring partner; daily-routine assistant; Lead Change Management Consultant.

The general CRIT example adds a sustainability procurement adviser; PICSE adds a senior DfT policy adviser specializing in stakeholder engagement and infrastructure policy. Those are **guidance-example personas**, not evidence of standalone library entries. Several prompts specify the user's role rather than the model's, and some descriptions claim an editor/survey designer role absent from the prompt text. Preserve exact role clauses before normalizing families. Persona adherence should mean useful expertise/behavior, not saying “as a senior adviser.”

## 7. Which prompting frameworks are recommended?

[Experimenting with prompts](https://knowledgehub.dev.ai.gov.uk/how-to/experiment-with-prompts) recommends clear simple instructions for everyday tasks and four detailed structures:

| Framework | Actual expansion | Suggested use on page |
|---|---|---|
| RACE | Role, Action, Context, Expected output | Focused task with one output |
| GCSE | Goal, Context, Source material, Expected output | Existing documents/data |
| CRIT | Context, Role, Intent, Type of output | Strategic/creative work, structure and tone |
| PICSE | Persona, Intention, Criteria, Sources, Examples | Complex or iterative workflows |

The page also recommends asking clarification questions, requesting sources/uncertainty, revising outputs and chaining stages with human review. A library entry uses **4-D: Deconstruct, Diagnose, Develop, Deliver** and platform-specific suggestions for GPT-4, Claude and Gemini. Other task methods include Five Case Model, OASIS, GCS Evaluation Cycle, cause-event-consequence risks, RACI, force-field analysis, Eisenhower/MoSCoW, SMART actions, ADKAR and Kotter. Distinguish prompting structure from a professional task framework. PICSE syntax alone does not make an interaction iterative. The site's claims that these approaches improve results are hypotheses for evaluation, not findings BureaucracyBench may assume.

## 8. Which capabilities does the site recognize?

The [home page](https://knowledgehub.dev.ai.gov.uk/) lists: Find information; Analyse data and text; Collect and clean data; Create and review documents; Triage and route information; Run meetings and appointments; Digitise documents. Prompt-card data additionally uses **Learning and development**. Observed prompt counts by source category: 25 Create and review documents, 15 Learning and development, five Analyse data and text, two Run meetings and appointments.

Prompt subcategories: General tasks (12), Reports and business documents (5), Check compliance and standards (4), Strategy and planning documents (14), Identify themes and trends (1), Personal productivity (7), Prompt development (3), Personal development (1). Project management is an explicit profession attribute on 24 cards, blank on 23. Keep these original fields separate from benchmark tags such as procurement or extraction.

## 9. Which documented use cases suit benchmarking?

The [tool library](https://knowledgehub.dev.ai.gov.uk/tools) has 47 entries with lifecycle distinctions. [Use-case assessment](use-cases.md) discusses suitable reconstructions. Strong text-only candidates include Consult theme coding; HMT correspondence flags/routing; Consular Digital Triage template selection; Minute transcript summarization; Redbox/AskOps/Caddy evidence-grounded answers; Scout assurance review; GCS Assist drafting; Data Disambiguation country matching.

These are synthetic reconstructions of task components, **not evaluations of the government systems**. Their production retrieval, prompts, training data, integration and review processes are not reproduced. HMT's [ATRS record](https://www.gov.uk/algorithmic-transparency-records/hmt-correspondence-triage-automation-tool) makes this especially clear: it combines SVM team classification, GPT-4-family prompting and retrieval-based standard-line matching. A lone LLM is not that stack. Reported Hub productivity/satisfaction metrics are not transferable benchmark baselines.

## 10–14. Which prompts are feasible, fixture-dependent, interactive or unsuitable?

Every test needs a stable task instantiation. The [47-row inventory](prompt-inventory.md) gives a decision for each source.

- **Easiest:** event-feedback survey structure; presentation slide/notes counts; consequence-scan coverage; Gantt schedule given a complete task DAG; daily-action extraction given a fixed message packet.
- **Synthetic packets essential:** business cases, risks, stakeholder maps, readiness, portfolios, procurement, benefits and briefings. Numeric claims need known supporting facts and missing-data traps.
- **Explicit multi-turn:** business-case writing, procurement, RACI threshold/word-count inquiry, project brief with section approvals, meeting coaching, prompt-improvement game, teaching prompts that first ask the topic, simplification that first asks for text, writing feedback that first asks for a style sample. The business-case summary asks questions if details are missing.
- **Reference documents:** Green/Magenta/Orange/Aqua/Rose/Teal books, business-case guidance, Project Data Standard, GovS 002/011, GCS/OASIS, departmental policies and GOV.UK style sources. Freeze actual editions/sections. Linked-only prompts are not automatically grounded.
- **Connected workflows:** leadership analysis, mid-year review, 1:1 preparation, weekly planning, mail prioritization, mentions and daily actions assume inbox/calendar/chat access. Replace with synthetic documents and label the adaptation; no real accounts.
- **Unsuitable for fully automated quality certification:** leadership traits, political judgement, rhetorical quality, teaching usefulness, stakeholder reactions, innovative mitigations and open-ended coaching. Structural subtests remain possible; utility needs human review.
- **Not faithful in baseline v0.1:** live-GOV.UK style checking, browsing, Word export, slide-file production, real connectors, audio transcription, OCR and clinical decisions. Text-only adaptations must declare capability loss. Do not count a Markdown project brief as successful Word export.

## 15–17. What to measure, and how?

Measure instruction following, artifact completion, grounding, framework conformity, completeness, unsupported assertions, missing-information handling and useful role behavior. Cost/latency/tokens are separate. See [scoring](scoring.md) for metric definitions, evidence records and denominators.

Deterministic: schema validity, literal format constraints, field coverage, exact extraction, date/unit consistency, schedule feasibility and critical path, risk-score arithmetic when inputs are fixed, closed-set classification, known citation IDs and verbatim quote matches. Heuristics for headings or questions are labeled proxies. They do not establish semantic compliance.

Qualitative: whether a risk is material, an analogy faithful, a recommendation justified, a source entails a claim, an OASIS plan coherent, a Five Case appraisal adequate or language accessible. Use anchored human rubrics and optional calibrated judges; retain disagreement and evidence. Never equate reference overlap or fluent prose with correctness.

## 18–19. Providers and local models

[Provider design](providers.md) separates endpoint protocol from model identity and records requested, sent and observed settings. Local profile identity includes exact weights/revision, quantization, runtime/version, tokenizer/chat-template digest, context settings, hardware and offload details where available. Unknown metadata stays unknown. The same “Llama” alias on two runtimes is not a controlled comparison.

Official documentation confirms compatible surfaces for [LM Studio](https://lmstudio.ai/docs/developer/openai-compat), [llama.cpp](https://github.com/ggml-org/llama.cpp/blob/master/tools/server/README.md), [vLLM](https://docs.vllm.ai/en/latest/serving/online_serving/) and [Ollama](https://docs.ollama.com/api/openai-compatibility). Surface support is not parameter parity. Native Anthropic/Google adapters remain separate extensions. [Google's compatibility documentation](https://ai.google.dev/gemini-api/docs/openai) and [OpenRouter parameters](https://openrouter.ai/docs/api/reference/parameters) inform later profiles. No integration was executed in this research.

## 20. How do upstream changes become releases?

Discovery writes dated candidates and diffs; review produces immutable releases. Preserve original observations even if upstream corrects them. Diff text, verification evidence, taxonomy, warnings, guidance, referenced document bytes and availability independently. Count failures separately from removals. Runs pin complete manifests and content hashes. The [corpus design](corpus.md) specifies the promotion protocol. No automatic background task or overwrite is enabled.

## 21. Existing projects to learn from

| Primary source | Useful design influence | Boundary |
|---|---|---|
| [Inspect](https://inspect.aisi.org.uk/), [logs](https://inspect.aisi.org.uk/eval-logs.html), [scoring](https://inspect.aisi.org.uk/scoring.html) | Dataset/solver/scorer separation, rich transcripts, deferred rescoring, provider abstractions | Prefer interoperability; do not couple corpus identity to an execution framework |
| [EleutherAI lm-evaluation-harness](https://github.com/EleutherAI/lm-evaluation-harness), [task/config guidance](https://github.com/EleutherAI/lm-evaluation-harness/blob/main/docs/config_files.md) | Declarative tasks, model abstraction, sample logging, model/runtime metadata | Many log-likelihood benchmarks differ from interactive artifact production |
| [HELM](https://crfm.stanford.edu/2022/11/17/helm.html), [HELM Instruct](https://crfm.stanford.edu/2024/02/18/helm-instruct.html) | Multidimensional evaluation, scenario coverage and explicit missingness | No universal metric copied without validation |
| [Promptfoo assertions](https://www.promptfoo.dev/docs/configuration/expected-outputs/) | Readable prompt variants and heterogeneous assertions | Avoid adopting an aggregate pass rate as evidence of factuality |

Python wins on typed validation, scientific/statistical tooling, local model metadata and Inspect/lm-eval interoperability. TypeScript with Promptfoo is credible, especially for web-focused development, but a web UI is not this project's center. A thin HTTP-based harness avoids loading inference engines into the benchmark process. See architecture for the dependency decision and an Inspect backend checkpoint.

## 22. Licensing and provenance

Hub footers state OGL v3.0 except where otherwise stated. The [National Archives licence](https://www.nationalarchives.gov.uk/doc/open-government-licence/version/3/) permits reuse/adaptation with attribution and conditions; [exceptions](https://www.nationalarchives.gov.uk/information-management/re-using-public-sector-information/uk-government-licensing-framework/open-government-licence/exceptions-to-ogl/) matter for third-party rights and excluded material. Full licence-page fetching was blocked here; official indexed text and the site's express licence notice support the archive's attribution. Do not treat that as clearance for every linked publication. ISO, Prosci, Kotter, proprietary templates and third-party style guides need separate review. Details in [licensing](licensing.md). Source text is not relicensed MIT and government logos are not included.

## 23. What makes this scientifically useful?

Preregister contrasts; match information and resources; distinguish model effects from prompt/fixture/provider effects; repeat runs; use family-held-out scenarios; blind and calibrate qualitative ratings; report coverage, errors, uncertainty and effect sizes; publish raw permitted artifacts and exact version identities. Compare verified/unlabeled groups descriptively unless task difficulty and family are controlled. Public prompts may already be in training data. Novel synthetic fixtures reduce answer memorization risk but do not establish contamination freedom. No claim of population-level government productivity follows from this small suite.

## 24. Smallest compelling v0.1

Twelve base tasks, three scenarios, six Verified-source tasks, two persona pairs, one three-framework matched experiment, deterministic plus human rubric evaluation, one generic compatible adapter plus native Anthropic, fake-provider testing, bounded multi-turn execution, raw JSON/JSONL and terminal/CSV/Markdown reports, paired comparison and no judge dependency. The [roadmap](roadmap.md) lists tasks and implementation gates. The current foundation includes four draft cases; the remaining tasks are specified for incremental implementation.

## Additional findings that change the design

1. **Efficiency advice is conditional and marked draft.** [Ethics guidance](https://knowledgehub.dev.ai.gov.uk/how-to/ethics) suggests the smallest adequate model, giving Gemini Flash/Pro and GPT Instant/Thinking examples, plus fewer/shorter prompts. It does not establish a single preferred government model or a universal instruction to disable thinking. Token counts/latency are not measured energy or emissions.
2. **Specific vendors appear in different contexts.** Prompt pages often say Copilot or Gemini as examples; [AI-at-work guidance](https://knowledgehub.dev.ai.gov.uk/how-to/how-to-use-ai-at-work) also mentions Claude. Tool descriptions cite GPT-4/4o/4.1, Claude Sonnet 3.5, Gemini, Amazon Translate, Azure search and other infrastructure. These are dated source claims, not current universal recommendations.
3. **Stale standards are real.** Several Verified prompts link Green Book 2022; [Treasury's 2026 edition](https://www.gov.uk/government/publications/the-green-book-appraisal-and-evaluation-in-central-government/the-green-book-2026) is now available. Preserve historical and current-standard tracks separately. The procurement prompt invokes MEAT; [official Procurement Act training](https://www.gov.uk/government/publications/the-official-procurement-act-2023-e-learning/module-7-assessment-and-award-of-contracts) distinguishes the newer MAT term. Applicability depends on jurisdiction, start date and transitional regime, so do not use a universal string penalty.
4. **Source prompt defects must remain visible.** Risk-register columns repeat Risk Response; Prompt Improv duplicates Purposefulness; meeting coaching says five stages then gives six; presentation preparation omits the Y bullet-count placeholder present in the prompt; Force Field Analysis uses different summary-placeholder wording between preparation and template. Do not normalize them silently.
5. **Truth versus instruction conflicts deserve a dedicated flag.** The Verified risk-analysis prompt asks for reassurance that mitigations work. Weekly planning treats replying as task completion. The GOV.UK style prompt supplies its own long checklist while prioritizing live guidance and contains tensions between table-only output and conversational examples. Score conflicting obligations separately and predeclare interpretation.
6. **Human review is integral.** [Using AI at work](https://knowledgehub.dev.ai.gov.uk/how-to/how-to-use-ai-at-work) warns about invented sources and misquotes, advises cross-checking figures and expert review, and distinguishes augmentation from automation. [Principles](https://knowledgehub.dev.ai.gov.uk/how-to/principles) require meaningful human control. [Security](https://knowledgehub.dev.ai.gov.uk/how-to/security) discusses prompt injection and limits of mitigations. A generic disclaimer alone is not evidence that a model detected a concrete uncertainty or risk.

## Unresolved before a public benchmark release

Production-host parity; documented upstream verification procedure and editorial ownership detail; exact rights on incorporated third-party materials; frozen authoritative reference packets; domain-expert rubric review and human inter-rater reliability; provider conformance and tested dependency lock; representative model pilot and sample-size assessment. These block strong empirical claims, not building the next development slice.
