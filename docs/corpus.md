# Corpus provenance and living releases

## Initial observation

`UK-AIKH-2026-09-27-dev-observed` contains 119 extracted public pages and 47 structured prompt records. It is a **research candidate**. The supplied production root failed with HTTP 403; no equivalence claim is made. Every source record keeps its actual URL. Do not rewrite it to an unobserved production URL. A future canonical URL can be added as separately evidenced metadata without changing the original record.

`pages.jsonl` archives main-element text, extracted `pre` blocks, outgoing links, retrieval timestamps, available ETag/Last-Modified headers and hashes. `prompts.jsonl` adds observed labels, verifier evidence, categories, preparation, warning text and exact prompt bytes. `manifest.json` hashes both archive files. `corpus/catalog.json` intentionally lists no released corpus.

Extraction procedure v0: fetch publicly linked pages, parse `//main` with lxml; remove script/style; strip each text node and join with LF; preserve `pre.text_content()` separately without typo correction, Markdown unescaping or whitespace trimming. Hash bytes as SHA-256 UTF-8. Manifest hashes are over file bytes; prompt hashes are over the exact `original_prompt` string, including indentation. Raw HTML hashes describe retrieved responses, but raw HTML is not redistributed. Dates shown on pages are preserved as text; absent dates remain null. Initial cached index/header metadata has explicitly missing HTTP headers.

## Metadata model

Source records preserve original title, retrieved URL/host/time, created/updated values if present, kind, contribution evidence, curation, verification status/body/evidence, category/subcategory/profession, task, prerequisites, warnings, expected behavior, original prompt and hash. Benchmark annotations are visibly separate. The current parser is a research extraction, not a production importer: before release, review section segmentation and compare fields against archived text.

Evidence levels: `verified` (explicit badge and matching page statement), `not_labelled`, `conflicting` (index/detail disagreement), `unknown` (unavailable). Verified suite eligibility also depends on case fidelity and release status. Tool records use their actual lifecycle (`Alpha`, `Beta`, `Live`, `Retired`) and “Publicly sourced” status independently of prompt verification.

## Future discovery workflow

1. Read the documented public index/site map and applicable access policy; identify all pagination/filter states. Prefer an official feed if one becomes available. No API was established in this investigation.
2. Fetch with a descriptive user agent, low concurrency, timeouts, conditional requests where headers support them and bounded retries. Record redirects and final URLs. Refuse login-only sources. Stop on persistent access denial.
3. Preserve bytes or licensed extracted representations and retrieval metadata. A response hash is not proof the source is authoritative; source identity remains explicit.
4. Produce a candidate manifest and review report: added/removed paths; prompt text edits; badge/body changes; author/verifier changes; categories; warnings; guidance; reference-link target changes. Use normalized-content hashes to suppress navigation churn but retain original bytes/hashes.
5. Fetch linked authoritative reference documents only from a reviewed allowlist. Compare document bytes/edition, not just URL. Record inaccessible, withdrawn or third-party references for manual review.
6. Treat 403/404/timeout as availability observations, not automatic deletions. Confirm removals over a later successful enumeration; use tombstones and preserve old snapshots.
7. A maintainer reviews licensing, extraction, verification conflicts and semantic changes; updates case variants/fixtures/rubrics separately; runs integrity tests and calibration.
8. Publish an immutable snapshot and benchmark manifest with a changelog and explicit included cases. Discovery never promotes itself.

These steps are a design, not an implemented sync command. No scheduler has been created. A future weekly/manual discovery option is reasonable; publication remains separately reviewed.

## Version identities

| Identity | Example | Changes when |
|---|---|---|
| Source observation | `UK-AIKH-2026-09-27-dev-observed` | New observation bundle/host |
| Benchmark release | `0.1.0` | Included cases/scoring protocol changes |
| Case revision | `BB-GANTT-001@0.1.0-draft` | Bindings, variant, references, behavior or rubric changes |
| Prompt variant | `faithful`, `persona_removed`, `modernized_2026` | Any instruction edit |
| Fixture/reference digest | SHA-256 | Any input/oracle/reference byte changes |
| Evaluator version | `schedule-feasibility@1` | Interpretation, parser or scoring changes |
| Run identity | UUID plus manifest digest | New execution plan |

A published bundle is never edited in place, even to fix a typo. Corrections create a new version and supersession record. Running an old snapshot remains possible. Comparing across prompt versions is a named experiment with aligned tasks, not an ordinary same-test leaderboard comparison.

## Historical and live tracks

Historical: frozen prompts plus the actual linked reference edition where retrievable and licensed. Current-standard adaptation: reviewed new reference packet and explicit edits. Live: tools may retrieve current information, but every retrieval URL/time/content digest and tool transcript is archived; results belong to that run's derived corpus, not the stable suite. Never silently reinterpret a 2022-linked prompt using 2026 rules.

The reference packet must distinguish official source excerpts from synthetic organizational policies. Source locator validity and semantic grounding can then be inspected. If a source cannot be redistributed, include rights-aware retrieval instructions and a digest where lawful, and mark the task unavailable until the user supplies the exact licensed material. Do not invent text or page numbers to fill gaps.
