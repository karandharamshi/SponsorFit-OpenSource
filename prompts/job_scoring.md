Score the job for the candidate.

Return JSON:

```json
{
  "score": 0,
  "salary_ok": true,
  "sponsorship_status": "clear | likely | unknown | not_available",
  "skills_match": ["..."],
  "skills_gap": ["..."],
  "location_match": "good | acceptable | poor | unknown",
  "reason": "...",
  "evidence": ["..."]
}
```

Reject jobs that clearly say sponsorship is unavailable.
