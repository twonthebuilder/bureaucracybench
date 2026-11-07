# BureaucracyBench

**What happens when we take the UK government's emerging AI practices seriously enough to test them across models?**

BureaucracyBench is a research-first foundation for evaluating public-sector prompts, professional personas, prompting frameworks and documented AI workflows. The intended harness supports local inference and bring-your-own-key (BYOK) hosted models. Its question is memorable — “Which local model is best at His Majesty's bureaucracy?” — but its measurements must be reproducible, inspectable and appropriately limited.

## Repository status

**Design and corpus foundation; no model runner or leaderboard yet.** This repository contains a source inventory, archived extracted source content, benchmark design, draft schemas, four worked case specifications, three synthetic scenarios, one controlled experiment specification, provider contracts and offline integrity tests. It does not contain measured model results. Example `run` commands below describe the planned interface, not working commands.

Research observed **47 prompts, including 17 explicitly Verified prompts**, plus 47 tool/use-case pages, 12 how-to pages and seven headline capability pages on 27 September 2026. The requested `https://ai.gov.uk/knowledge-hub/` returned HTTP 403 in this research environment. The publicly accessible `https://knowledgehub.dev.ai.gov.uk/` was inspected instead. **Production-host equivalence is not established.** The 119-page archive is therefore named `UK-AIKH-2026-09-27-dev-observed` and marked a research candidate, not a production-verified benchmark release.

Start with [the research answers](docs/research.md), [all 47 prompt assessments](docs/prompt-inventory.md), and [the implementation roadmap](docs/roadmap.md). Coding agents must read [AGENTS.md](AGENTS.md).

For a reproducible checkout, offline checks and an issue-to-review workflow, see [repository onboarding](docs/repository-onboarding.md).

## Source corpus and status

The [AI Knowledge Hub](https://knowledgehub.dev.ai.gov.uk/about) shares public-sector tools, practices, prompts and practical guidance. It is not a comprehensive policy authority. The library describes itself as user-submitted; submissions are curated. Its prompt index defines Verified as subject professionals having reviewed and approved a prompt. The 17 observed labeled pages identify Government Project Delivery Professionals as verifying the **approach**. They still require output checks. No reproducible verification protocol, model matrix or error threshold was found.

Keep these axes separate:

- published prompt with explicit verification evidence;
- curated prompt without an explicit verification label;
- contribution origin, which is often unspecified at individual-page level;
- general guidance, including draft guidance;
- documented use cases, including prototypes, live tools and retired services.

A community contribution can also be verified. “Not labelled” does not mean rejected. An adapted benchmark case is not government-verified merely because its source prompt is. Internal HTML profession attributes are not a substitute for a badge and verifying statement.

## What will be measured

Quality is a profile, not one arbitrary score: instruction following, completion, evidence grounding, framework conformity, completeness, unsupported claims, handling of missing information and useful persona behavior. Report latency, tokens and costs separately. A heading saying “Green Book” is not framework compliance; a link is not proof of grounded content.

Evaluation is layered: deterministic assertions where defensible; reference-grounded fact checks; explicit qualitative rubrics; optional, recorded LLM judgments. Human rubric review is a first-class path. Missing judgments remain unassessed. Inspectable outputs and per-criterion evidence are mandatory. See [scoring](docs/scoring.md).

## Proposed suites

| Suite | Selection |
|---|---|
| `full` | Every released case; incompatible cases reported with reasons |
| `verified` | Faithful instantiations of sources explicitly labeled Verified in the pinned snapshot |
| `prompt-library` | Cases derived from individual prompt pages, with adaptation status visible |
| `personas` | Paired role-present and role-removed conditions; no automatic Verified inheritance |
| `frameworks` | Information-matched plain, CRIT and PICSE conditions; RACE/GCSE expansion later |
| `use-cases` | Explicit reconstructions inspired by documented tools; never claims to replicate their systems |
| Capability/family suites | Source capability categories and project tags such as `procurement`, `risk`, `writing` |

The site has seven headline capabilities, but prompt metadata also uses **Learning and development**. We preserve both taxonomies instead of forcing an inaccurate mapping. See [benchmark design](docs/benchmark-design.md).

## Proposed v0.1

Twelve base tasks: ten library tasks (six Verified sources) and two use-case reconstructions; three synthetic scenarios; at least two persona pairs and one plain/CRIT/PICSE experiment. Start execution with a generic OpenAI-compatible chat adapter for local endpoints and compatible hosted models, then a native Anthropic adapter. A fake provider enables free offline tests. Add native OpenAI Responses and Google adapters only where compatibility endpoints fail the required contract.

Every source-dependent case needs frozen reference material, complete fixture bindings, a documented interaction script where necessary, acceptance rubrics and evaluator tests before promotion from draft. The four included specifications are development examples, not a released suite. The [roadmap](docs/roadmap.md) defines the exact twelve-task scope and gates.

## Local and hosted models

LM Studio, llama.cpp, vLLM and Ollama expose OpenAI-compatible surfaces, with differing capabilities. Compatibility is tested per endpoint/model configuration, not assumed from the protocol name. No model weights or runtime server are bundled.

Use environment variables for API keys; [.env.example](.env.example) contains names and blank values only. A model profile records endpoint identity, actual model/version, requested and applied settings, unsupported settings, reasoning configuration and local metadata such as quantization, weight digest, chat template, runtime and hardware. Unsupported settings fail preflight by default; an explicit waiver must record what was omitted. Never silently retry with different settings. See [providers](docs/providers.md).

## Planned CLI (not implemented)

```bash
bureaucracybench models --config models.local.json
bureaucracybench suites --corpus UK-AIKH-2026-09-27-dev-observed
bureaucracybench run --model local/qwen-example --suite verified --repetitions 3
bureaucracybench run --model hosted/example --suite personas
bureaucracybench run --model anthropic/example --case BB-PROCUREMENT-001
bureaucracybench compare results/run_a results/run_b
bureaucracybench corpus discover --output corpus/candidates/new-observation
```

Discovery stages reviewable candidates; it never changes a release. No recurring network job is enabled by this repository.

## Reproducibility and results

Pin corpus, case, fixture, evaluator, prompt variant, reference packet and code versions independently. Store exact rendered messages, output, stop reason, errors, every attempt, settings, model identity, usage and optional judgments. Seeds and temperature zero do not guarantee identical answers. Repeat runs, preserve failed attempts and report comparison coverage and uncertainty. Explicitly record alias drift, quantization and missing metadata.

JSON manifests and JSONL sample records are the canonical outputs; terminal, CSV and Markdown reports are derived views. Compare only compatible cases/configurations and show per-dimension results. No universal leaderboard score is planned. Live-source experiments are a separate track with archived retrieval traces. Details: [architecture](docs/architecture.md), [corpus](docs/corpus.md), [experimental protocol](docs/benchmark-design.md).

## Check the foundation locally

Requires Python 3.11 or newer. The foundation has no runtime dependencies.

```bash
python -m unittest discover -s tests -v
python scripts/validate_foundation.py
```

These checks cover corpus hashes/counts, prompt provenance, fixture bindings, draft contracts, experimental information parity and the scheduling oracle. They do not run models or establish validity of qualitative rubrics. JSON Schemas are draft contracts. Optional standards-based checks validate the schema definitions and case/profile examples; runtime loading and result-record conformance remain implementation gates.

Optional schema checks (install in a virtual environment):

```bash
python -m pip install -e ".[validation]"
python scripts/validate_schemas.py
```

## Repository map

| Path | Purpose |
|---|---|
| `corpus/` | Candidate archive and release catalog; immutable after publication |
| `benchmarks/` | Readable case and experiment definitions, planned suite catalog |
| `fixtures/` | Fictional model-visible packets and separate evaluator-only facts |
| `schemas/` | Draft JSON Schema contracts for case, profile and result records |
| `src/bureaucracybench/` | Typed provider boundary and subsystem responsibilities |
| `docs/` | Research, provenance, architecture, scoring and implementation plan |
| `tests/` | Offline foundation checks; no paid inference in CI |
| `results/` | Ignored run outputs; no fabricated examples presented as measurements |

## Licence and independence

Original code, project documentation and synthetic fixtures are [MIT licensed](LICENSE). Imported government material remains under its stated terms, generally Open Government Licence v3.0 with exceptions. See [NOTICE](NOTICE) and [licensing notes](docs/licensing.md). BureaucracyBench is independent and not endorsed by the UK Government. The GitHub repository's existing visibility is not changed by this initialization.
