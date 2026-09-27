# Prompt inventory

Observed UK-AIKH-2026-09-27-dev-observed: 47 prompts; 17 explicitly Verified; 30 not labelled. All 47 individual pages inspected. IDs are slug-based and must never be reassigned. These annotations describe benchmark work, not upstream endorsements.

Modes: single_turn = fixture substitution; document = supplied packet; multi_turn = scripted interaction; connected = synthetic replacement for mail/calendar access; live_reference = cannot faithfully run offline without a labeled adaptation. All runnable tests still need fixtures.

| Prompt | Verified | Source category | Family | Mode | Benchmark requirements |
|---|---|---|---|---|---|
| [Analyse your leadership style](https://knowledgehub.dev.ai.gov.uk/prompts/analyse-your-leadership-style) | No label | Learning and development | leadership | connected | Synthetic year of communications; subjective personality inferences; exclude real employees. |
| [Build a procurement strategy](https://knowledgehub.dev.ai.gov.uk/prompts/build-a-procurement-strategy) | No label | Create and review documents | procurement | multi_turn | Ask scope/value/timeline first; pin jurisdiction and procurement regime; MEAT wording needs context. |
| [Build a project communications strategy](https://knowledgehub.dev.ai.gov.uk/prompts/build-a-project-communications-strategy) | No label | Create and review documents | communications | multi_turn | Clarify audience/goals/risks; OASIS and GovS 011 reference packet. |
| [Build a risk mitigation plan](https://knowledgehub.dev.ai.gov.uk/prompts/build-a-risk-mitigation-plan) | No label | Analyse data and text | risk | multi_turn | Ask event/causes/impacts; Orange Book; do not redistribute ISO text without rights. |
| [Build a stakeholder engagement plan](https://knowledgehub.dev.ai.gov.uk/prompts/build-a-stakeholder-engagement-plan) | No label | Create and review documents | stakeholders | multi_turn | Ask groups and interests; synthetic roles; engagement quality needs review. |
| [Build an event feedback survey](https://knowledgehub.dev.ai.gov.uk/prompts/build-an-event-feedback-survey) | No label | Create and review documents | writing | single_turn | Easy fixture: event, aims, audience; categories and question types measurable. |
| [Challenge your ideas and approach](https://knowledgehub.dev.ai.gov.uk/prompts/challenge-your-ideas-and-approach) | No label | Learning and development | critical_thinking | multi_turn | Paired sound/flawed proposals; reward warranted challenge and avoid reflexive opposition. |
| [Check if your business case is deliverable](https://knowledgehub.dev.ai.gov.uk/prompts/check-if-your-business-case-is-deliverable) | Yes | Create and review documents | assurance | document | Business case plus exact reference editions/pages; placeholder sample citations are not authority. |
| [Create a benefits realisation plan](https://knowledgehub.dev.ai.gov.uk/prompts/create-a-benefits-realisation-plan) | Yes | Create and review documents | business_cases | document | Synthetic project plus Teal Book workbook; benefits register/map/assumptions. |
| [Create a business readiness plan](https://knowledgehub.dev.ai.gov.uk/prompts/create-a-business-readiness-plan) | Yes | Create and review documents | project_delivery | document | Evidence/sign-off fixtures; never mark incomplete readiness as complete. |
| [Create a communication plan](https://knowledgehub.dev.ai.gov.uk/prompts/create-a-communication-plan) | Yes | Create and review documents | communications | document | Current/proposed state; Teal Book, OASIS, GCS Evaluation Cycle packet. |
| [Create a Gantt-style project schedule](https://knowledgehub.dev.ai.gov.uk/prompts/create-a-gantt-style-project-schedule) | Yes | Create and review documents | planning | document | Best deterministic pilot: fixed task durations, owners, DAG, critical path. |
| [Create a governance structure and RACI matrix](https://knowledgehub.dev.ai.gov.uk/prompts/create-a-governance-structure-and-raci-matrix) | Yes | Create and review documents | governance | multi_turn | Ask approval thresholds and word count; Teal Book; explicit fixture RACI convention. |
| [Create a project brief](https://knowledgehub.dev.ai.gov.uk/prompts/create-a-project-brief) | Yes | Create and review documents | project_delivery | multi_turn | Section-at-a-time approvals and explicit advance signal; Word export separate capability. |
| [Create a risk analysis document](https://knowledgehub.dev.ai.gov.uk/prompts/create-a-risk-analysis-document) | Yes | Create and review documents | risk | document | Preserve unsupported reassurance instruction; PDS fields and dated Green/Orange/Teal references. |
| [Develop a business case summary](https://knowledgehub.dev.ai.gov.uk/prompts/develop-a-business-case-summary) | Yes | Create and review documents | business_cases | multi_turn | Ask if details missing; complete-data variant may finish once; links 2022 Green Book. |
| [Develop a change plan](https://knowledgehub.dev.ai.gov.uk/prompts/develop-a-change-plan) | Yes | Create and review documents | change | document | Four sections; stakeholder table/training timeline; third-party ADKAR/Kotter rights review. |
| [Develop a risk register](https://knowledgehub.dev.ai.gov.uk/prompts/develop-a-risk-register) | Yes | Analyse data and text | risk | document | 5–10 risks; likelihood×impact; duplicate Risk Response field and typo preserved. |
| [Develop a stakeholder map](https://knowledgehub.dev.ai.gov.uk/prompts/develop-a-stakeholder-map) | Yes | Create and review documents | stakeholders | document | Synthetic current/proposed states and Teal Book; placements not unique gold truth. |
| [Explain a complex topic for a beginner ](https://knowledgehub.dev.ai.gov.uk/prompts/explain-a-complex-topic-for-a-beginner) | No label | Learning and development | explanation | multi_turn | Ask topic first; closed reference facts; human clarity assessment. |
| [Explain a topic using comparisons (analogies)](https://knowledgehub.dev.ai.gov.uk/prompts/explain-a-topic-using-comparisons-(analogies)) | No label | Learning and development | explanation | multi_turn | Ask topic; score analogy limitations, not preferred metaphor. |
| [Explain like I'm Six](https://knowledgehub.dev.ai.gov.uk/prompts/explain-like-i'm-six) | No label | Learning and development | explanation | multi_turn | Ask topic; distinguish simple from misleading; audience review required. |
| [Generate a portfolio health overview](https://knowledgehub.dev.ai.gov.uk/prompts/generate-a-portfolio-health-overview) | Yes | Create and review documents | portfolio | document | Synthetic cases/status/budgets/benefits and pinned RAG rules; recommendations reviewed. |
| [Get feedback on your writing approach](https://knowledgehub.dev.ai.gov.uk/prompts/get-feedback-on-your-writing-approach) | No label | Create and review documents | writing | multi_turn | Writing sample before draft; do not critique the style sample; line-specific edits. |
| [Improve a prompt step-by-step](https://knowledgehub.dev.ai.gov.uk/prompts/improve-a-prompt-step-by-step) | No label | Learning and development | prompt_development | multi_turn | 4-D method; request platform; evaluate optimized prompt on held-out task, not self-score. |
| [Improve a simple prompt](https://knowledgehub.dev.ai.gov.uk/prompts/improve-a-simple-prompt) | No label | Learning and development | prompt_development | multi_turn | Revised prompt and questions until user stop; malformed ending preserved. |
| [Improve your prompt-writing skills](https://knowledgehub.dev.ai.gov.uk/prompts/improve-your-prompt-writing-skills) | Yes | Learning and development | prompt_development | multi_turn | Verified 3-round game; duplicate Purposefulness label; self-scores not benchmark truth. |
| [Learn a topic from somebody in your profession ](https://knowledgehub.dev.ai.gov.uk/prompts/learn-a-topic-from-somebody-in-your-profession) | No label | Learning and development | explanation | multi_turn | Parameterised profession; ask topic; matched expertise ablations. |
| [Map a project lifecycle](https://knowledgehub.dev.ai.gov.uk/prompts/map-a-project-lifecycle) | Yes | Create and review documents | project_delivery | document | Milestones/governance and Teal Book; avoid treating agile phase names as universal. |
| [Plan your week](https://knowledgehub.dev.ai.gov.uk/prompts/plan-your-week) | No label | Learning and development | productivity | connected | Synthetic calendar/messages, fixed clock; reply=completed instruction can conflict with actual completion. |
| [Prepare for a 1:1 meeting with your line report](https://knowledgehub.dev.ai.gov.uk/prompts/prepare-for-a-1:1-meeting-with-your-line-report) | No label | Run meetings and appointments | meetings | connected | Synthetic work evidence and manager policy only; personal issues deferred. |
| [Prepare for a briefing](https://knowledgehub.dev.ai.gov.uk/prompts/prepare-for-a-briefing) | Yes | Create and review documents | briefing | document | Synthetic pilot evidence; no invented ROI; table and assumptions; strong pilot. |
| [Prepare for a meeting](https://knowledgehub.dev.ai.gov.uk/prompts/prepare-for-a-meeting) | No label | Run meetings and appointments | meetings | multi_turn | One question at a time; says five stages but lists six; explicit review resolution. |
| [Prepare for your mid-year review](https://knowledgehub.dev.ai.gov.uk/prompts/prepare-for-your-mid-year-review) | No label | Learning and development | productivity | connected | Synthetic objectives and six-month achievements; evidence sufficiency and attribution. |
| [Prioritise emails after a break](https://knowledgehub.dev.ai.gov.uk/prompts/prioritise-emails-after-a-break) | No label | Learning and development | productivity | connected | Synthetic mail/Teams; priority rules and dated absence window. |
| [Prioritise portfolio projects and programmes](https://knowledgehub.dev.ai.gov.uk/prompts/prioritise-portfolio-projects-and-programmes) | Yes | Analyse data and text | portfolio | document | Fixed portfolio; explain weights; one ranking not uniquely right without fixed objective. |
| [Prioritise your workload](https://knowledgehub.dev.ai.gov.uk/prompts/prioritise-your-workload) | No label | Learning and development | productivity | multi_turn | Ask tasks/hours/constraints; fixed calendar; overlap/deadline checks. |
| [Review project documents for assurance](https://knowledgehub.dev.ai.gov.uk/prompts/review-project-documents-for-assurance) | No label | Analyse data and text | assurance | multi_turn | Ask document type; pinned relevant standards; avoid indiscriminate book name-dropping. |
| [Review your content against GOV.UK style and standards](https://knowledgehub.dev.ai.gov.uk/prompts/review-your-content-against-gov.uk-style-and-standards/) | No label | Create and review documents | writing | live_reference | Requires live guidance; frozen-reference adaptation separate; six columns, exact citations; long inconsistent checklist. |
| [Run Force Field Analysis](https://knowledgehub.dev.ai.gov.uk/prompts/run-force-field-analysis) | No label | Create and review documents | change | single_turn | Project/service/sector fixture; subjective weights and intervention trade-offs. |
| [Scan for project consequences](https://knowledgehub.dev.ai.gov.uk/prompts/scan-for-project-consequences) | No label | Analyse data and text | risk | single_turn | Five categories and horizons; fixture evidence separates actual from potential impacts. |
| [Simplify complex writing](https://knowledgehub.dev.ai.gov.uk/prompts/simplify-complex-writing) | No label | Create and review documents | writing | multi_turn | Ask for text, preserve material facts/conditions, human accessibility review. |
| [Summarise daily actions](https://knowledgehub.dev.ai.gov.uk/prompts/summarise-daily-actions) | No label | Learning and development | extraction | connected | Synthetic messages; fixed last-workday; five columns and bold mentions. |
| [Track mentions in emails](https://knowledgehub.dev.ai.gov.uk/prompts/track-mentions-in-emails) | No label | Learning and development | extraction | connected | Synthetic mail, identity and time window; distinguish mentions from recipients. |
| [Turn a document into a presentation](https://knowledgehub.dev.ai.gov.uk/prompts/turn-a-document-into-a-presentation) | No label | Create and review documents | writing | document | Synthetic document; exact slides/bullets/notes; Y placeholder missing from prep instructions. |
| [Write a business case](https://knowledgehub.dev.ai.gov.uk/prompts/write-a-business-case) | No label | Create and review documents | business_cases | multi_turn | Ask type/stage and five-case information; reference packet; not Verified. |
| [Write high-quality content](https://knowledgehub.dev.ai.gov.uk/prompts/write-high-quality-content) | No label | Create and review documents | writing | single_turn | Parameterized role, audience, format; fixture facts and footnoted sources. |

## Persona evidence

Exact role-bearing lines are retained in each corpus record. Some explanatory page prose describes an editor or survey designer although the actual prompt contains no model-role assignment. A user saying “I am a line manager” is not a model persona. Do not conflate these.

- **Build a procurement strategy**: You are a senior procurement and finance officer guiding a project’s commercial approach.
- **Build a project communications strategy**: You are a communications specialist responsible for the project communications plan for [PROJECT NAME].
- **Build a risk mitigation plan**: You are a highly experienced Risk Manager working on the [INSERT YOUR PROJECT OR PROGRAMME NAME].
- **Build a stakeholder engagement plan**: You are a stakeholder engagement lead for [PROJECT NAME].
- **Challenge your ideas and approach**: Your role is to serve as an intellectual sparring partner—not a passive assistant.
- **Check if your business case is deliverable**: You are a public sector Business Case Assessor trained in HM Treasury’s Green Book methodology. Your task is to assess the deliverability of a business case [DELIVERABILITY IN THIS CONTEXT].
- **Create a benefits realisation plan**: You are an experienced Benefits Manager supporting a programme \[INITIATIVE].
- **Create a business readiness plan**: You are an experienced and accredited Business Change Manager working in an agile digital delivery team in government.
- **Create a communication plan**: You are a high performing Stakeholder and Communication Manager.
- **Create a Gantt-style project schedule**: You are a high-performing Project Planner. Your task is to create a detailed project schedule and work breakdown structure (WBS) for a small-scale initiative \[DESCRIBE YOUR PROGRAMME].
- **Create a governance structure and RACI matrix**: You are a Project Management Office Manager overseeing governance for a high-profile digital transformation programme \[PROGRAMME DESCRIPTION] involving suppliers, cross-functional teams, and multiple organisations
- **Create a project brief**: Act as my Project Manager with 20 years of experience in communicating and explaining projects to senior stakeholders.
- **Create a risk analysis document**: You are a high-performing quantitatively minded Risk Manager supporting the programme. You understand the importance of risk insight for decision-making and are tasked with producing a clear, actionable risk analysis.
- **Develop a business case summary**: You are an experienced Business Case Manager working on a programme. Create a summary business case using the Five Case Model for the following programme [DESCRIBE THE PROJECT].
- **Develop a change plan**: You are a Change Manager working on a programme \[PROGRAMME DETAILS].  The plan will be used to inform readiness activities and communications at the next governance meeting.  Use a professional tone in plain UK English, with clear, actionable guidance.
- **Develop a risk register**: You are a senior Risk Manager supporting a UK government programme (for example, ERP programme) involving legacy systems and third-party suppliers.
- **Develop a stakeholder map**: You are a high performing Stakeholder Manager.
- **Explain a complex topic for a beginner **: You are an expert teacher and communicator. Use clear, simple and accessible language.
- **Explain a topic using comparisons (analogies)**: You are an expert teacher and communicator. Use clear, simple and accessible language.
- **Explain like I'm Six**: You are an expert teacher and communicator. Use clear, simple and accessible language.
- **Generate a portfolio health overview**: You are a high performing Portfolio Manager. Analyse the current portfolio and produce a high-level, data-driven overview of project health for strategic decision-making.
- **Improve a prompt step-by-step**: You are a master-level AI prompt optimisation specialist.
- **Improve a simple prompt**: I want you to become my Prompt engineer.
- **Improve your prompt-writing skills**: You’ll act as the Facilitator, and I’ll be the Participant.
- **Learn a topic from somebody in your profession **: You are an expert in [PROFESSION].
- **Map a project lifecycle**: You are a veteran business analyst.
- **Plan your week**: You are my AI assistant, optimised for my daily routine.
- **Prepare for a briefing**: You are a Stakeholder Manager briefing a senior leader.
- **Prepare for a meeting**: You are an expert meeting prep coach assisting someone preparing for an important upcoming meeting.
- **Prioritise portfolio projects and programmes**: You are a high-performing Portfolio Manager tasked with assessing a diverse set of projects.
- **Prioritise your workload**: You are an AI productivity coach and time management expert.
- **Review project documents for assurance**: You are a senior-level programme assurance expert with extensive experience reviewing major UK public sector infrastructure programmes.
- **Review your content against GOV.UK style and standards**: You are a lead GOV.UK content designer and my experienced and trusted colleague. You bring deep expertise in GOV.UK standards, content approaches and best practice - but you respect that I know the subject matter, context and strategic goals. Your responses and discussion always use clear, simple language, patiently explaining nuance and reasoning.
- **Run Force Field Analysis**: Act like a Lead Change Management Consultant for an international firm.
- **Simplify complex writing**: You are a senior content designer.
- **Turn a document into a presentation**: You are a professional presentation designer and communicator.
- **Write a business case**: You are an expert business case advisor with deep knowledge of HM Treasury’s Green Book and the Five Case Model.
- **Write high-quality content**: You are a senior-level [INSERT ROLE] with proven expertise in crafting high-impact, audience-specific content.
