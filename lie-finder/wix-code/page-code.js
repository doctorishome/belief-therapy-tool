// Lie Finder - page code (Wix Studio site "Pearls Working 5", page "Lie Finder" at /false-belief-finder)
// Paste this into the page's code panel. It assumes the embedded page element is named #html1.
// It passes the counselor's notes from the embedded Lie Finder page to the backend and the
// results back again. Nov 18, 2026: free trial — visitors log in free and get 3 searches;
// members with an active plan get unlimited searches (rules are in backend/lieFinder.web.js).

import { findLies, lieFinderAccess } from 'backend/lieFinder.web';
import { authentication } from 'wix-members-frontend';
import wixLocationFrontend from 'wix-location-frontend';

$w.onReady(function () {
  const box = $w('#html1');
  const reply = (msg) => box.postMessage(Object.assign({ source: 'lie-finder-site' }, msg));

  async function sendAccess() {
    try { reply({ type: 'access', access: await lieFinderAccess() }); } catch (e) {}
  }

  authentication.onLogin(() => { sendAccess(); });

  box.onMessage(async (event) => {
    const m = event.data;
    if (!m || m.source !== 'lie-finder') return;
    if (m.type === 'ready') { reply({ type: 'hello' }); sendAccess(); }
    if (m.type === 'login') {
      try { await authentication.promptLogin({ mode: 'signup' }); } catch (e) {}
      sendAccess();
    }
    if (m.type === 'join') wixLocationFrontend.to('/blank-11');
    if (m.type === 'search') {
      try {
        const answer = await findLies(m.input);
        if (answer && answer.result) reply({ type: 'result', result: answer.result, freeLeft: answer.freeLeft, freeTotal: answer.freeTotal });
        else reply({ type: 'error', reason: answer && answer.reason, message: (answer && answer.error) || 'The search did not work. Please try again.' });
      } catch (e) {
        reply({ type: 'error', message: 'The search did not work. Please try again.' });
      }
      sendAccess();
    }
  });

  reply({ type: 'hello' });
  sendAccess();
});
