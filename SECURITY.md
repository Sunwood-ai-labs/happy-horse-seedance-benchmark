# Security Policy

## Reporting

Do not open a public issue for secrets, account data, API keys, unpublished
media, or provider-specific access details.

Report security or privacy concerns privately to the repository owner.

## Sensitive Data

Never commit:

- API keys or `.env` files
- personal account information
- raw provider exports that include private identifiers
- generated source videos unless they have been explicitly approved for release
- full rendered MP4 files unless they are intentionally published as release assets

The repository is configured to keep benchmark media local by default through
`.gitignore`.
