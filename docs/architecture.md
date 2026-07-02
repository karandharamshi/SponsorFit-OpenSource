# Architecture

## Components

### Job sources
Fetch or import jobs. Initial MVP should support CSV import and manually pasted job descriptions before adding scrapers.

### Sponsorship detector
Classifies visa sponsorship status from job text and employer clues.

### Match scorer
Scores the job against the user's profile.

### Document generator
Uses GPT to draft CV summaries, cover letters and answers. All outputs are drafts.

### Form filler
Uses Playwright to prefill approved fields and pauses before final submission.

### API
FastAPI backend for scoring and generation.

### Web dashboard
Future user interface for reviewing jobs, documents and audit logs.

## Data flow

```text
Job source -> sponsorship detector -> match scorer -> user approval
-> document generator -> user approval -> form filler -> user submits
```
