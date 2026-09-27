# Runner implementation boundary

Start with a fake provider and exact transcript logging. Follow docs/architecture.md:
preflight, deterministic input rendering, oracle isolation, durable attempt journal,
bounded dialogue, no silent truncation, no answer-quality retries, explicit metadata.
Do not add paid calls, tools or telemetry by default. No runner is present yet.
