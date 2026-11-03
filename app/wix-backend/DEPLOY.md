# Turn on live answers (do this before merging the pull request)

The app on GitHub Pages is set to call `https://www.beliefcounselor.com/_functions/clinicalCompanion`. That address does nothing until you paste the files below into Wix and publish. Do that first, then merge the pull request. Merging first would make the app ask a server that is not there yet.

Case notes still stay in the counselor’s browser. The yellow banner stays up. This is still not for real client data. The xAI key is never put in GitHub and is never sent back to the browser. The backend does not save the message text.

## Secrets

In the Wix editor: **Developer** → **Secrets Manager**. Create these two names:

1. **XAI_API_KEY** — the key from the xAI console.
2. **CC_MEMBERSHIP_SECRET** — a long random phrase you make up. It only signs the short-lived membership token. It is not the xAI key.

## Files to paste

| File in this folder | Where it goes in Wix |
|---|---|
| `http-functions.js` | Backend → `http-functions.js`. If that file already exists, copy `options_clinicalCompanion` and `post_clinicalCompanion` into it. Do not delete the rest of the file. |
| `ai-budget.js` | Backend → new file `ai-budget.js` |
| `cc-token.js` | Backend → new file `cc-token.js` |
| `cc-membership.web.js` | Backend → new file `cc-membership.web.js` |
| `clinical-companion-page-code.js` | The code panel of the Wix page whose address is `/clinical-companion` |

The page code expects the HTML embed on that page to be named **html1** (the element id `#html1`). That embed is the one that shows `counselors/clinical-companion.html`. If the embed has another name, rename it to html1, or change `#html1` in the page code to match.

## What the button does

Start Clinical Companion is still a normal link, so it works if the page is opened outside Wix. Inside the Wix embed it asks the parent page for a membership token. The page code mints that token (active plan, or the site owner/admin) and opens the app in the **same tab**. The token is only in the `#cct=` part of the address. The app saves it for that tab and removes it from the address bar. It is not the API key, and it lasts 8 hours.

## Order

1. Paste the four backend files and the page code. `ai-budget.js` holds the prices, the $10 cap, and the off-topic wording. If the token, membership, and page files are already published, paste only the updated `http-functions.js` and the new `ai-budget.js`.
2. Add the two secrets.
3. Publish the Wix site.
4. Merge the pull request so GitHub Pages starts calling the proxy.

The model name sent to xAI is **grok-4.7**. A short clinical check uses **grok-4.20-0309-non-reasoning** only when the question is not already clearly clinical or clearly off-topic.

## Monthly allowance

Each member can use **$10** of AI in a calendar month (Eastern Time). That is `MEMBER_MONTHLY_AI_BUDGET_USD` in `ai-budget.js`. Site-owner tokens are not capped. Add a Wix member id to `ADMIN_UNLIMITED_MEMBER_IDS` in that same file if you want another uncapped person.

Create a Wix collection named **ClinicalCompanionUsage** before relying on the cap. Fields: memberId (text), month (text), inputTokens (number), outputTokens (number), cachedTokens (number), costUsd (number). Set the collection so only you can see it in the dashboard. The backend writes to it and does not store question or answer text. If the collection is missing, the proxy will not send an answer, so the allowance cannot be skipped.
