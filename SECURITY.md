# Security

Do not report security issues publicly if they expose secrets or unsafe automation paths.

## Never commit

- API keys
- Job-board passwords
- Browser session cookies
- CVs with private personal data
- Generated applications containing private data

## Browser automation

The form filler must never click final Submit. Any PR that adds automatic final submission should be rejected.
