// Find Help - page code (Wix Studio site "Pearls Working 5", page "Find Help")
// Paste into the page's code panel. The embedded page (pages/find-help.html) must be #html1.

import { findHelp } from 'backend/findHelp.web';

$w.onReady(function () {
  const box = $w('#html1');
  const reply = (msg) => box.postMessage(Object.assign({ source: 'find-help-site' }, msg));

  box.onMessage(async (event) => {
    const m = event.data;
    if (!m || m.source !== 'find-help') return;
    if (m.type === 'ready') reply({ type: 'hello' });
    if (m.type === 'search') {
      try {
        const answer = await findHelp({ story: m.story });
        if (answer && answer.result) reply({ type: 'result', result: answer.result });
        else reply({ type: 'error', message: (answer && answer.error) || 'The search did not work. Please try again.' });
      } catch (e) {
        reply({ type: 'error', message: 'The search is not available right now. Please try again in a minute.' });
      }
    }
  });

  reply({ type: 'hello' });
});
