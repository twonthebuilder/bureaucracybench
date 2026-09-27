# Government use cases: reconstruction suitability

The [47-entry tool library](https://knowledgehub.dev.ai.gov.uk/tools) and all individual pages were inspected. Every page is archived in the research snapshot. Labels below are observations of dated Hub pages, not assertions of deployment state today. “Publicly sourced” means the Hub's description status, not prompt verification. Benefits are reported by the source and are not benchmark baselines.

| Documented example | Observed phase / character | Reproducible component | What would not be replicated |
|---|---|---|---|
| [Consult](https://knowledgehub.dev.ai.gov.uk/tools/consult) | Beta, i.AI/DSIT | Fixed-codebook multi-label coding of synthetic consultation responses; later open theme discovery | ThemeFinder production pipeline, policy decisions and real consultation distribution |
| [HMT correspondence triage](https://knowledgehub.dev.ai.gov.uk/tools/correspondence-triage-automation-tool) | Live; publicly sourced | Eight-field classification/summary/template selection with fictional routing directory | SVM + GPT + retrieval production stack, real ministers/citizen correspondence |
| [Consular Digital Triage](https://knowledgehub.dev.ai.gov.uk/tools/consular-digital-triage) | Beta | Choose a vetted fictional response template or escalate; measure out-of-scope abstention | FCDO data, live consular advice or claimed operational savings |
| [Minute](https://knowledgehub.dev.ai.gov.uk/tools/minute) | Beta | Minutes/action extraction from a fixed synthetic transcript | Speech recognition, recording consent workflow and audio quality |
| [Redbox](https://knowledgehub.dev.ai.gov.uk/tools/redbox) | Beta | Briefing and Q&A over frozen public/synthetic documents with citations | Security authorization or suitability for OFFICIAL-SENSITIVE data |
| [AskOps](https://knowledgehub.dev.ai.gov.uk/tools/askops-chatbot) | Alpha; publicly sourced | HR-policy Q&A using a fictional policy packet, missing-rule traps | DSIT internal policies; original Claude Sonnet 3.5 integration |
| [Caddy](https://knowledgehub.dev.ai.gov.uk/tools/caddy) | Beta | Evidence-grounded adviser draft and escalation from supplied references | Supervisor workflow, client outcomes and reported trial effects |
| [Scout](https://knowledgehub.dev.ai.gov.uk/tools/scout) | Beta/testing; publicly sourced | Find planted assurance gaps with precise source locators | Real NISTA review judgements, private handbooks and production retrieval |
| [GCS Assist](https://knowledgehub.dev.ai.gov.uk/tools/gcs-assist) | Live | Communications draft against pinned public framework/reference packet | Internal prompt set, adoption/training program or user survey results |
| [Data Disambiguation Assistant](https://knowledgehub.dev.ai.gov.uk/tools/data-disambiguation-assistant) | Live | Synthetic place-name normalization with ambiguous cases | Actual TB screening data and operational access |
| [Business Intelligence Subject Tagger](https://knowledgehub.dev.ai.gov.uk/tools/business-intelligence-subject-tagger) | Live; publicly sourced | Closed taxonomy tagging; compare LLMs to simple baselines | CNN/ensemble training and live business feedback |
| [GOV.UK Chat](https://knowledgehub.dev.ai.gov.uk/tools/gov.uk-chat/) | Beta on archived page | Grounded service navigation with frozen public excerpts | Current deployment, live retrieval and complete web safety stack |
| [Simply Readable](https://knowledgehub.dev.ai.gov.uk/tools/simply-readable) | Live | Text simplification and factual preservation | Easy Read accessibility validation with users, images and layout |
| [Document Translate](https://knowledgehub.dev.ai.gov.uk/tools/document-translate) | Live | Translation of fictional text with bilingual review | Amazon Translate system, document fidelity, privacy controls |
| [Extract](https://knowledgehub.dev.ai.gov.uk/tools/extract) | Alpha; publicly sourced | Later multimodal extraction of synthetic planning documents | Gemini plus Segment Anything geospatial/digitisation stack |
| [Fraud Risk Assessment Accelerator](https://knowledgehub.dev.ai.gov.uk/tools/fraud-risk-assessment-accelerator) | Beta; publicly sourced | Draft risk taxonomy from synthetic project evidence | GPT-4.1 app, Excel export and expert fraud assurance |

For v0.1, choose Consult and HMT-style triage because fixed labels, known facts and synthetic inputs give useful objective measures. [HMT's ATRS record](https://www.gov.uk/algorithmic-transparency-records/hmt-correspondence-triage-automation-tool) confirms eight outputs and mixed technology: SVM for team selection; GPT-4-family components for summaries/flags; retrieval for standard lines. [Consult's ATRS record](https://www.gov.uk/algorithmic-transparency-records/dsit-consult) is the next reference for release authoring. Neither reconstruction may inherit the original tool's measured F1 or deployment status as its own.

## Exclusions and later tracks

Clinical imaging (Mia, Stroke AI), health-deterioration prediction and Limbic clinical pathways need specialist datasets and safety validation. FloodAI, AI4Peat, roofing drones, energy-cost prediction and exporter propensity modeling are valuable AI uses but not general-purpose text prompt benchmarks. Logo detection, Report It images, translation/audio routing, Speech AI, Magic Notes and real-time interpretation need separate multimodal/operational tracks. Content Education Store/Hawkeye are infrastructure/data workflows; a prose imitation would not benchmark their core function. Digital Sensitivity Review and recruitment matching can be studied with synthetic records later, but high-stakes production claims are out of scope. Asylum summaries/search require specialist factual and harm evaluation; defer rather than produce a toy “decision accuracy” claim.

The Review Automoderation Tool is marked Retired; preserve that history instead of listing it as currently deployed. Parlex's prediction of parliamentary reaction would need temporal holdouts and political-context labels, not judge preference. Some library pages describe planned rollouts whose dates have passed; their dated statements are not independently verified current status.

## Synthetic triage output contract

Eight fields: follow_up, high_risk, meeting_request, responding_minister_role, standard_line_id, summary, subject, team. Fixture rules define labels and unknown/escalate behavior; use fictional role IDs rather than real officeholders. Evaluate class-wise precision/recall, macro-F1, confusion matrices, abstention coverage and summary factuality separately. Do not average rare high-risk false negatives away in a general accuracy number. A human still makes the hypothetical final decision.
