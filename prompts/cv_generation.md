Generate tailored application documents.

Return JSON:

```json
{
  "cv_summary": "...",
  "skills_section": ["..."],
  "experience_bullets": ["..."],
  "cover_letter": "...",
  "application_answers": [
    {
      "question": "...",
      "answer": "...",
      "requires_human_review": false
    }
  ],
  "sensitive_questions": [
    {
      "question": "...",
      "reason": "..."
    }
  ]
}
```

Do not answer sensitive legal, visa, medical, disability, criminal record or equality questions unless the user has provided exact values.
