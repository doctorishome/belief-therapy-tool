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
| `cc-token.js` | Backend → new file `cc-token.js` |
| `cc-membership.web.js` | Backend → new file `cc-membership.web.js` |
| `clinical-companion-page-code.js` | The code panel of the Wix page whose address is `/clinical-companion` |

The page code expects the HTML embed on that page to be named **html1** (the element id `#html1`). That embed is the one that shows `counselors/clinical-companion.html`. If the embed has another name, rename it to html1, or change `#html1` in the page code to match.

## What the button does

Start Clinical Companion is still a normal link, so it works if the page is opened outside Wix. Inside the Wix embed it asks the parent page for a membership token. The page code mints that token (active plan, or the site owner/admin) and opens the app in the **same tab**. The token is only in the `#cct=` part of the address. The app saves it for that tab and removes it from the address bar. It is not the API key, and it lasts 8 hours.

## Order

1. Paste the three backend files and the page code.
2. Add the two secrets.
3. Publish the Wix site.
4. Merge the pull request so GitHub Pages starts calling the proxy.

The model name sent to xAI is **grok-4.7**, which is a current text model on the public xAI model list (https://docs.x.ai/developers/models).
