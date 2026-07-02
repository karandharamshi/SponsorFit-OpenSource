# Safety policy

SponsorFit is a user-controlled application assistant, not a spam bot.

## Allowed

- Import jobs from user-provided CSV files.
- Search configured job sources where allowed.
- Rank jobs using transparent scoring.
- Draft CVs and answers for user review.
- Prefill repetitive non-sensitive application fields.
- Pause for the user before submission.

## Not allowed

- Automatic final submission.
- Applying without user approval.
- Creating fake experience.
- Guessing protected-category or legal answers.
- Circumventing CAPTCHAs or access controls.
- Mass application spam.
- Storing credentials in the repo.

## Sensitive fields

These must always require human review:
- Visa and right-to-work
- Sponsorship declarations
- Criminal record
- Medical or disability
- Equal opportunities
- Salary expectations when tied to legal declarations
- Any final declaration that information is true

## Auditability

The system should keep a local audit log showing:
- Job applied to
- Fields filled
- Files uploaded
- Fields skipped
- Timestamp
- Whether final submission was left to the user
