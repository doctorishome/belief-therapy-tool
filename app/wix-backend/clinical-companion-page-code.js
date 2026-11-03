// Page code for https://www.beliefcounselor.com/clinical-companion
// The HTML embed #html1 shows counselors/clinical-companion.html.
// "cc-start-free-week" scrolls to the sign-up section (existing behavior).
// "cc-open-app" (the Start button) mints a short-lived membership token and opens the app.
import wixLocationFrontend from 'wix-location-frontend';
import { mintClinicalCompanionToken } from 'backend/cc-membership.web';

const APP = 'https://doctorishome.github.io/belief-therapy-tool/app/';

$w.onReady(function () {
  $w('#html1').onMessage(async (event) => {
    const data = event.data || {};
    if (data.type === 'cc-start-free-week') {
      $w('#section5').scrollTo();
      return;
    }
    if (data.type !== 'cc-open-app') return;
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
