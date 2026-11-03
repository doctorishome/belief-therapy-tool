// Page code for the Wix page https://www.beliefcounselor.com/clinical-companion
// Paste this into that page's code panel.
// The HTML embed that shows counselors/clinical-companion.html must be named html1
// (in the editor that is the element id #html1).
//
// The Start button inside the embed posts { type: "cc-open-app" }.
// This page mints a short-lived membership token and opens the app in the same tab.
// The token rides in the address fragment (#cct=...), which the browser does not send to GitHub.
import wixLocationFrontend from 'wix-location-frontend';
import { mintClinicalCompanionToken } from 'backend/cc-membership.web';

const APP = 'https://doctorishome.github.io/belief-therapy-tool/app/';

$w.onReady(function () {
  $w('#html1').onMessage(async (event) => {
    const data = event.data || {};
    if (!data || data.type !== 'cc-open-app') return;
    let address = APP;
    try {
      const minted = await mintClinicalCompanionToken();
      if (minted && minted.token) address = APP + '#cct=' + encodeURIComponent(minted.token);
    } catch (e) {
      address = APP;
    }
    wixLocationFrontend.to(address);
  });
});
