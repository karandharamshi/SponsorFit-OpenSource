# SponsorFit

Open-source job application assistant for international candidates who need visa sponsorship.

SponsorFit helps users find sponsored jobs, rank matches, generate tailored application drafts, and safely prefill repetitive job application forms. It is designed for a human-in-the-loop workflow, not blind auto-applying.

## Core workflow

1. Search jobs from configured sources.
2. Filter for visa sponsorship, salary threshold, role fit and location.
3. User reviews and approves jobs.
4. GPT generates tailored CV, cover letter and application answers.
5. User reviews and approves the generated documents.
6. Playwright opens the application page and prefills safe fields.
7. User reviews the final application and clicks Submit manually.

## Safety position

SponsorFit must never:
- Click final Submit automatically.
- Guess visa, right-to-work, criminal record, health, disability or equality answers.
- Store job-board passwords.
- Misrepresent a user's experience.
- Bypass paywalls, CAPTCHAs, robots.txt restrictions or job-board terms.

## GPT and Codex support

This repo is structured so GPT/Codex-style coding agents can work on it safely:
- `AGENTS.md` gives project-wide coding and safety instructions.
- `prompts/` contains stable prompts for CVs, scoring and application answers.
- `.env.example` documents runtime configuration.
- Tests and lint commands are defined in `Makefile`.
- Codex tasks are listed in `docs/codex_tasks.md`.

## MVP modules

- `packages/job_sources`: fetch or import job listings.
- `packages/sponsorship_detector`: classify sponsorship evidence.
- `packages/match_scorer`: score jobs against a user profile.
- `packages/document_generator`: generate CV and application draft data.
- `packages/form_filler`: safe Playwright form prefill helper.
- `apps/api`: FastAPI backend.
- `apps/web`: future dashboard placeholder.

## Quick start

```bash
cp .env.example .env
python -m venv .venv
source .venv/bin/activate
pip install -r requirements-dev.txt
make test
```

To run the API:

```bash
uvicorn apps.api.app.main:app --reload
```

## Project status

Early public scaffold. Users set up their own API keys, job sources and browser sessions later.
