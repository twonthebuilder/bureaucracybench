# Provider and model configuration

## Protocol support is not semantic equivalence

The v0.1 generic adapter targets `/v1/chat/completions` with text messages. This supports a useful common surface for local servers and compatible hosted services without loading model weights into the harness. Profiles choose provider, API surface, model and endpoint independently. Native Anthropic Messages is the second adapter; native OpenAI Responses and Google Gemini can follow. An OpenRouter profile must also record routing preferences and actual backend/provider metadata where available.

| Runtime/provider | Investigated official surface | Initial decision |
|---|---|---|
| [LM Studio](https://lmstudio.ai/docs/developer/openai-compat) | OpenAI-compatible endpoints | Generic adapter; confirm loaded model and server settings |
| [llama.cpp](https://github.com/ggml-org/llama.cpp/blob/master/tools/server/README.md) | Compatible chat routes, local inference/server controls | Generic adapter; record GGUF hash, quantization, build and chat template |
| [vLLM](https://docs.vllm.ai/en/latest/serving/online_serving/) | Compatible serving | Generic adapter; distinguish serving defaults and batching |
| [Ollama](https://docs.ollama.com/api/openai-compatibility) | Partial compatibility; some context configuration outside API | Generic baseline plus explicit runtime profile; no invented context-setting support |
| [OpenAI](https://platform.openai.com/docs/api-reference/chat/create) | Chat and newer Responses surface | Explicit compatible Chat profile first; native Responses later if required |
| [Anthropic](https://docs.anthropic.com/en/api/messages) | Native Messages contract | Dedicated adapter; verify SDK/model-specific settings during implementation |
| [Google](https://ai.google.dev/gemini-api/docs/openai) | Gemini API with compatible surface | Compatible experiment first; native adapter extension |
| [OpenRouter](https://openrouter.ai/docs/api/reference/parameters) | Compatible routing and provider-dependent parameters | Explicit routing metadata; unsupported parameters cannot silently vanish |

Documents were inspected as design evidence on 27 September 2026. The Anthropic full reference exceeded retrieval size; implementation must check its current official API/SDK documentation. None of these integrations has been exercised here. Do not hard-code current model aliases or advertise universal parameter support.

## Normalized request

Model profile fields: `profile_id`, `provider`, `api_surface`, `base_url`, `api_key_env` (name only), `model`, `model_revision`, `deployment`, `settings`, `capabilities`, `local_metadata`.

Settings normalize only clear common intent: temperature, top_p, output-token limit, seed, stop sequences, timeout and reasoning configuration. Reasoning uses a tagged provider-native object, not a universal boolean. Preserve distinct meanings of visible output budget, total completion budget and internal reasoning budget. Server context length is not necessarily a per-request setting. `provider_options` is namespaced, validated and cannot override canonical values without an explicit conflict error.

Capabilities are profile assertions that need conformance evidence: text/chat roles, supported settings, reasoning controls, structured outputs, context metadata, token usage, streaming, tools and attachments. Unknown is different from unsupported. Preflight rejects unsupported required fields; users may explicitly omit optional controls, generating a different recorded configuration. Never say a requested seed was applied merely because the request succeeded.

## Returned measurement

Always retain sanitized raw response, visible assistant text, provider request ID, returned model identity, finish reason and error envelope. Usage separates input, visible output, reasoning and cached-input tokens if reported. Null means not available. Record requested settings, transmitted settings, effective/confirmed settings and warnings separately. Provider fingerprint/API version is nullable.

Store request start/end and monotonic latency. Streaming may give time-to-first-token and generation duration. `output_tokens / total_request_seconds` is end-to-end throughput, not local decode speed. Only runtime-provided decode counts/timing support “local generation tokens/s.” Record model warmup, queue time, concurrency, hardware and cache state for latency comparisons.

Cost includes currency, pricing date/source, charge mode (`actual`, `estimated`, `unknown`), cached/reasoning-token treatment and per-attempt cost. Local marginal API cost can be zero while electricity/hardware cost is unknown; do not report “free compute.” No historical price is silently used as today's price.

## Local identity

Require an explicit `deployment=local` profile, but allow metadata to be unknown for exploratory runs. Release-quality local comparisons should include weight source/revision/digest, architecture/model size if verified, quantization format/bits, tokenizer revision, chat template and digest, runtime/version/build, context length, CPU/GPU model/count/memory, RAM, OS, accelerator libraries, offload/layer placement, batching and sampling configuration. Missing fields lower reproducibility completeness; they do not trigger fabricated guesses.

## Safety and conformance

`.env.example` never contains secrets. The runner reads only named key variables, not the full environment. Reject literal secrets in profiles, URL userinfo and sensitive query parameters. Do not log request headers. Provider errors may echo credentials: sanitize before journaling. No cross-host redirect with authorization and no auto-fallback to another host. Endpoint profiles represent user-authorized connections; source pages cannot supply endpoints.

Mock transport tests must cover success, unknown usage, malformed response, rate limiting, timeout, authentication error, unsupported setting, ignored-setting warning, redaction and model identity drift. Live smoke runs are opt-in. Unsupported configuration should return a useful preflight error, not a crash or a result falsely labeled with the requested settings.
