# Put Clinical Companion’s AI proxy on the Wix site

The browser app is in the `app` folder. It opens from GitHub Pages. Case notes stay in the counselor’s browser. They are not stored on GitHub or on Wix.

Right now the app is in **mock mode**. It answers with canned drafts so you can try the screens with fictional cases. Nothing is sent to an AI service, and the app does not contain an API key.

Do not turn on live answers until you have pasted the backend files below and published the site. Merging this folder does not turn on the paid AI by itself.

## What you are adding

Three backend files. Paste them into the Wix editor’s Backend section. They do not run from GitHub Pages.

| File in this repo | Where it goes in Wix |
|---|---|
| `http-functions.js` | Backend → `http-functions.js` |
| `cc-token.js` | Backend → `cc-token.js` |
| `cc-membership.web.js` | Backend → `cc-membership.web.js` |

If the site already has an `http-functions.js`, do not delete it. Copy `options_clinicalCompanion` and `post_clinicalCompanion` into the existing file.

The address, after you publish, is:

`https://www.beliefcounselor.com/_functions/clinicalCompanion`

That is the only address the browser app needs. A different server can replace Wix later. Put its address in the same one place: `proxyUrl` in `app/config.js`.

## Secrets (the key never goes in GitHub)

In the Wix editor, open **Developer** → **Secrets Manager** and create two secrets:

1. **XAI_API_KEY** — the key from the xAI console. Only the backend reads it. Do not paste it into a page, into `config.js`, or into GitHub.
2. **CC_MEMBERSHIP_SECRET** — any long random phrase you make up. It signs a short-lived “this member may call the AI” token. It is not the xAI key.

## Membership check

Each AI call checks that the person has an **active Pricing Plan** order (`status` ACTIVE). The free week counts, because that order is active too.

The app runs on GitHub Pages, which is a different website from Wix, so the member’s Wix login cookie is not sent with the AI call. The Counselors page has to hand the open tab a short-lived token. The token lasts 8 hours, lives in that browser tab only, and is not an API key.

On the Wix page where members open the app, add a button and this page code:

```javascript
import { mintClinicalCompanionToken } from 'backend/cc-membership.web';

$w('#openClinicalCompanion').onClick(async () => {
  const { token } = await mintClinicalCompanionToken();
  const app = 'https://doctorishome.github.io/belief-therapy-tool/app/';
  const tab = window.open(app, '_blank');
  setTimeout(() => {
    tab.postMessage({ type: 'cc-membership', token }, 'https://doctorishome.github.io');
  }, 1200);
});
```

## Turn live answers on

In `app/config.js`:

- Set `proxyUrl` to the `_functions/clinicalCompanion` address above.
- Set `mode` to `"live"`.

Leave `fictionalOnly` set to `true` until both of these are true: a Business Associate Agreement is signed, and zero data retention is confirmed on the xAI account. Until then the yellow banner stays up and the app is for fictional cases only.

Publish the Wix site after the backend files change. GitHub Pages updates when this folder is merged. Do not merge until you have looked at the screens.

## If you later use a different server

The browser sends one JSON POST:

```json
{
  "action": "chat",
  "model": "grok-4.7",
  "maxTokens": 4000,
  "reasoningEffort": "medium",
  "messages": [{ "role": "system", "content": "..." }, { "role": "user", "content": "..." }]
}
```

A successful reply is JSON: `{ "content": "...", "thinking": "", "model": "..." }`.

Refusals use `{ "error": "plain sentence", "code": "MEMBER_REQUIRED" }` with HTTP 403 when there is no active membership.

The server holds the key, checks membership, and does not store the message text. The browser never sees the key.

## Words to use

Do not say the app is “HIPAA approved” or “HIPAA certified.”

Today: it is **not yet for real client data**.

Later, only after a signed BAA and zero data retention: **HIPAA-compliant processing under a signed BAA**.

## Back to Counselors

The app’s Back to Counselors button opens `https://www.beliefcounselor.com/blank-11`, the Counselors’ Room. That page embeds `counselors/welcome.html`. If you rename it, change `counselorsReturnUrl` in `app/config.js` only.
