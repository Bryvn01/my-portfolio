# Portfolio

Professional portfolio website for Brian (Bryvn01), focused on secure engineering delivery, fintech integration, and product execution.

## Live Site

- Production URL: set by your hosting provider (GitHub Pages or Vercel)
- GitHub owner profile: https://github.com/Bryvn01

## Tech Stack

- Single-page static HTML/CSS/JavaScript
- Formspree for contact form handling
- Security-focused meta policies (CSP, referrer policy, permissions policy)
- Theme strategy: system-driven only (`prefers-color-scheme`) with no persisted manual light/dark override

## Local Development

1. Open `index.html` in a browser for quick preview.
2. For better local parity, run a static server:

```bash
npx serve .
```

3. Run the contact email regression check:

```bash
python scripts/check_contact_email.py
```

## Deployment

### GitHub Pages

1. Repository Settings -> Pages
2. Source: Deploy from a branch
3. Branch: `main`, Folder: `/(root)`

### Vercel

1. Import repository
2. Framework preset: Other
3. Build command: (empty)
4. Output directory: (empty)

## Ownership and Copyright

Copyright (c) 2026 Bryvn01.

All rights reserved. No part of this project may be copied, modified, distributed, or reused without explicit written permission from the copyright owner.

GitHub is a trademark of GitHub, Inc. This project is independently owned and operated by Brian.

## Legal Documents

- Terms of use (site): `TERMS.html`
- License: `LICENSE`
- Repository notice: `NOTICE`
