# Codex task list

Use these as small, safe tasks for Codex.

## Task 1: Sponsorship classifier

Build `packages/sponsorship_detector/classifier.py`.

Input:

```json
{
  "title": "Software Developer",
  "company": "Example Ltd",
  "description": "We can provide Skilled Worker sponsorship for eligible candidates."
}
```

Output:

```json
{
  "status": "clear",
  "evidence": ["Skilled Worker sponsorship"],
  "reason": "The job description explicitly says sponsorship is available."
}
```

Statuses:
- `clear`
- `likely`
- `unknown`
- `not_available`

Must include tests.

## Task 2: Match scorer

Build `packages/match_scorer/scorer.py`.

Score jobs from 0 to 10 using:
- sponsorship status
- salary threshold
- skills match
- location match
- seniority match
- deadline urgency

Must expose a simple pure function and tests.

## Task 3: GPT JSON schema

Create a document generation schema for:
- tailored CV summary
- cover letter
- application question answers
- risky questions requiring human review

Must not generate final submit behaviour.

## Task 4: Playwright safe form filler

Build a module that:
- opens a URL
- fills only safe fields from an approved profile
- uploads only approved files
- stops at sensitive fields
- never clicks Submit
- writes an audit log

Must include mocked tests where possible.

## Task 5: API endpoints

Create FastAPI endpoints:
- `POST /jobs/score`
- `POST /jobs/classify-sponsorship`
- `POST /documents/draft`
- `POST /applications/audit-log`

Keep endpoints simple and typed.
