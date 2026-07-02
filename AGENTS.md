# AGENTS.md

These instructions apply to the whole repository.

## Product goal

Build SponsorFit as a human-in-the-loop, open-source job application assistant for candidates who need visa sponsorship.

The product should help users:
- Find jobs with clear or likely visa sponsorship.
- Filter by salary, location, role and skills.
- Generate truthful CVs, cover letters and application answers.
- Prefill repetitive application forms.
- Review everything before final submission.

## Non-negotiable safety rules

Never implement code that:
- Clicks final Submit or equivalent buttons automatically.
- Applies to jobs without explicit user approval.
- Generates or stores false claims.
- Answers right-to-work, visa, criminal record, medical, disability or equality questions without explicit user-provided values.
- Stores passwords or session cookies in the repo.
- Bypasses CAPTCHAs, rate limits, login protections or paywalls.
- Ignores job-board terms of service.
- Scrapes personal data unrelated to job applications.

If a feature conflicts with these rules, stop and propose a safer design.

## Coding standards

- Prefer simple Python first.
- Use type hints in all new Python code.
- Keep modules small and easy to test.
- Add or update tests for every meaningful behaviour change.
- Do not add heavy frameworks unless the task requires them.
- Keep public interfaces documented.
- Avoid hidden network calls in tests.
- Use fixtures and sample files from `examples/`.

## Commands

Run these before finishing a coding task:

```bash
make test
make lint
```

If a command cannot run because dependencies are missing or the environment is limited, say exactly what failed and why.

## Architecture rules

- Keep job discovery separate from sponsorship classification.
- Keep GPT prompts separate from application logic.
- Keep browser automation separate from scoring and document generation.
- The form filler must pause before sensitive fields and final submission.
- Add audit logs for anything the assistant fills.

## OpenAI/GPT integration rules

- All LLM outputs must be treated as drafts.
- Prefer structured JSON outputs for scoring, sponsorship classification and generated application answers.
- The app must show users the raw evidence behind sponsorship and salary decisions.
- Never hide uncertainty. Use statuses such as `clear`, `likely`, `unknown`, and `not_available`.

## PR expectations

Every PR should include:
- What changed.
- Why it changed.
- Safety implications.
- Tests run.
- Known limitations.
