# Repository onboarding and agent workflow

This guide explains how to bring BureaucracyBench into an AI-assisted development workflow. GitHub remains the source of truth for code, issues and review; a Slack thread can provide intake and progress. No Slack service is required to develop the project locally.

## What “import this repository” means

Treat onboarding as four independently verified steps:

| Step | What it enables | Evidence of success |
|---|---|---|
| Repository access | Read code; separately authorize issue, branch and PR writes | Read the default branch, then perform an authorized test write |
| Local checkout | Run checks and edit a working tree | Record the base SHA, Python version and passing checks |
| Cloud execution environment (optional) | Run a separate hosted coding task | A task actually starts in an eligible environment and returns results |
| Slack integration (optional) | Receive notifications or dispatch through an enabled agent app | A real event or task result returns to the intended channel/thread |

A connected GitHub account is not proof of a working cloud environment. Posting a slash command as ordinary message text does not execute it. A PR link posted by an assistant is not proof that GitHub notifications are subscribed.

## 1. Inspect before executing

Confirm the exact repository, visibility, default branch and intended scope. Read [AGENTS.md](../AGENTS.md), [README.md](../README.md), and the architecture, benchmark-design, scoring, corpus and roadmap documents that AGENTS.md requires. Inspect commands and installation scripts before running them.

This repository is a **design and corpus foundation**, not a model runner. Preserve archived source wording, provenance and the research-candidate status. The CLI shown in the README is planned, not implemented. No model credentials are needed for the foundation checks.

For another repository, discover its own instructions, runtime, build commands, secrets requirements and deployment hooks. Do not copy BureaucracyBench's commands blindly.

## 2. Clone and establish a baseline

In a new development directory, with Git and Python 3.11 or newer installed:

```bash
git clone https://github.com/twonthebuilder/bureaucracybench.git
cd bureaucracybench
git status --short
git rev-parse HEAD
python --version
python -m unittest discover -s tests -v
python scripts/validate_foundation.py
```

Run from the repository root. If your system calls Python 3 `python3`, substitute that executable. These two checks use the standard library; no package installation or inference endpoint is needed. Stop and investigate a failed baseline before assigning a feature task. Record pre-existing failures separately from changes introduced by the task.

Optional JSON Schema validation requires the README's validation extra. It is not part of the dependency-free onboarding path and was not run in the initial demonstration. Install optional packages only in an isolated environment after reviewing them.

## 3. Create one task and one isolated work area

Search open issues and PRs before creating another task for the same work. Use the GitHub issue URL as the durable task identity. A local queue can add its own ID, but should link to the existing issue instead of duplicating its specification.

The onboarding example is [issue #1](https://github.com/twonthebuilder/bureaucracybench/issues/1). For a new task, replace the example branch name with its issue number and purpose:

```bash
git switch -c docs/repository-onboarding-1
```

For parallel work, use separate worktrees and branches. Starting from the main checkout, this creates a new sibling checkout for a different task:

```bash
git worktree add ../bureaucracybench-task-2 -b task/2-short-description main
```

Do not run two writers in the same worktree or silently reset somebody else's edits. If a branch or directory already exists, inspect it and resume deliberately rather than overwriting it.

A useful task brief contains:

```text
Repository: twonthebuilder/bureaucracybench
Issue: <issue URL>
Base: <commit SHA>
Outcome: <one reviewable result>
Acceptance: <observable checks>
Allowed scope: <files/subsystems and permitted tools>
Constraints: read AGENTS.md; preserve corpus; no paid inference or secrets
Executor: <one accountable actor>
Review: draft PR, diff summary, exact tested SHA and check results
Stop before: merge, deployment, destructive action or new credential access
```

## 4. Implement, validate and request review

Keep a documentation task limited to documentation. For implementation, start with the roadmap's first milestone: strict loaders, fixture isolation and a fake-provider path. Do not introduce a general orchestration framework or pretend a benchmark runner already exists.

After the change:

```bash
git diff --check
git diff --stat
git diff
python -m unittest discover -s tests -v
python scripts/validate_foundation.py
```

Review all changed files, including new untracked files, before committing. Publish only the task branch using your already-authorized Git client or connected repository tools, then open a **draft** PR targeting `main`. Link the issue with `Closes #<number>`. Record the final commit SHA and check results in the PR. If publishing modifies the commit, verify the published tree and rerun the required checks there.

Describe self-review as self-review. A second agent's opinion is useful evidence, not human merge approval. After reviewing the exact head and test evidence, the human operator can request revisions or mark the PR ready and merge in GitHub. Any later change invalidates approval of the earlier head. No automatic merge is enabled by this guide.

## 5. Optional Slack notifications

This procedure is documented, **not installed or verified by the onboarding test**. In the intended Slack workspace, inspect existing apps and channel subscriptions first. Reuse the official GitHub app if present; otherwise the operator must install it and review its requested permissions. Prefer access to selected repositories.

In the chosen private channel, run these commands interactively, one at a time:

```text
/invite @github
/github signin
/github subscribe list features
```

For a new subscription:

```text
/github subscribe twonthebuilder/bureaucracybench
/github unsubscribe twonthebuilder/bureaucracybench commits releases deployments
/github subscribe list features
```

This starts with issues and PRs and removes the other default event types. Preserve an existing subscription's deliberate settings; inspect and adjust any additional enabled features individually. Verify delivery with a harmless issue or PR event and distinguish the app-generated notification from a manually posted link. Do not enable all workflow or comment events by default. There were no checked-in GitHub Actions workflows in the inspected baseline; local checks must not be described as CI results.

Use one thread per task for assignment, blocker, review and outcome updates. Keep routine command output in the PR/check logs. If notifications become noisy, remove the specific feature; to remove this repository subscription entirely:

```text
/github unsubscribe twonthebuilder/bureaucracybench
```

See the [official GitHub Slack integration](https://github.com/integrations/slack) for current installation, permissions and notification options (checked 2026-10-14).

## 6. Optional hosted agent dispatch

The initial test used an assistant's connected GitHub/Slack tools and a local checkout. It did **not** start a native Slack-to-Codex Cloud task or create a cloud environment.

For OpenAI's current Slack route, an admin must enable the ChatGPT app and Cloud delegation. The repository needs an accessible, published environment shared with the workspace; a personal environment alone does not qualify. Verify environment and repository access, then make a small request mentioning `@ChatGPT` in an enabled channel. Review connection and approval prompts, and confirm that a separate task starts and returns a result in the thread. These requirements come from the [official Slack guide](https://learn.chatgpt.com/docs/third-party/slack), checked 2026-10-14; actual availability depends on the workspace.

Suggested environment specification for this repository: Python 3.11+, repository root working directory, the two offline validation commands above, no secrets and no dependency installation for the foundation task. Review any prepared files and environment-owned values before sharing. Environment creation, publication and dispatch remain separate verification steps.

If the app or environment is unavailable, hand the same issue brief to a configured coding environment or a local agent and post the resulting PR back to the original thread. Do not repeatedly dispatch a task merely because the Slack reply is delayed.

## 7. Status, recovery and approval

Use `Ready → Running → Review → Awaiting approval → Done`; use `Blocked` when human action or unavailable infrastructure prevents progress. The GitHub issue is the durable record; a Slack list is an operational view. Mark code work Done only after merge or an explicit decision to close without merging.

- Assign one executor. Before retrying, inspect the issue, branch, PR and any active session; reuse them if appropriate.
- Publish updates on state changes and material blockers. For long work, agree a heartbeat interval. An overdue heartbeat means inspect, not automatically launch a duplicate writer.
- Record task ID, attempt, base/head SHA, executor/session reference, check results and next action. Keep credentials, private workspace links and sensitive logs out of public issues and PRs.
- If Slack is unavailable, continue locally within the approved scope and record progress in GitHub; reconcile the thread later.
- A pause request stops new dispatches. Cancel active sessions through their runtime, inspect existing writes, and resume only after a deliberate decision. This guide does not implement a global kill switch or background queue.
- Merges, deployments and expanded credential access require a separate human decision. Approval applies to a specific action and revision, not everything mentioned in a thread.

## Initial onboarding evidence

On 2026-10-14, the public repository was read through connected GitHub tools and cloned successfully. At base `8ac2ad2584869ce65b03b4baad853646a831b3fc`, Python 3.12.14 ran all **12 unit tests successfully**. The foundation validator passed with **119 pages, 47 prompts, 17 explicitly verified prompts, 4 draft cases and 6 experiment variants**. These are integrity counts, not benchmark scores.

The test created issue #1, used branch `docs/repository-onboarding-1`, and reported progress into an existing Slack task thread. The linked PR records final publication and validation evidence. No benchmark contents, runtime dependencies, model settings or deployment configuration were changed. Native app subscriptions, cloud environment setup, independent agent review and merge remain outside this demonstration.
