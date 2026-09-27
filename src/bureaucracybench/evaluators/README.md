# Evaluator implementation boundary

Implement independent, versioned measurements defined in docs/scoring.md.
First slice: schedule feasibility and critical-path checking against the Northbridge DAG.
Structural checks cannot certify semantic framework compliance. Add valid alternatives,
empty outputs, contradictions and format-gaming cases to evaluator tests.
Human rubric records are first-class; LLM judging is optional and separately recorded.
No evaluator implementation is present yet.
