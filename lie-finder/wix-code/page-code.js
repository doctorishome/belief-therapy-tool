// Lie Finder - page code (Wix Studio site "Pearls Working 5", page "Lie Finder")
// Paste this into the page's code panel. It assumes the embedded page element is named #html1.
// It passes the counselor's notes from the embedded Lie Finder page to the backend and the
// results back again.

import { findLies } from 'backend/lieFinder.web';

$w.onReady(function () {
  const box = $w('#html1');
  const reply = (msg) => box.postMessage(Object.assign({ source: 'lie-finder-site' }, msg));

  box.onMessage(async (event) => {
    const m = event.data;
    if (!m || m.source !== 'lie-finder') return;
    if (m.type === 'ready') reply({ type: 'hello' });
    if (m.type === 'search') {
      try {
        const answer = await findLies(m.input);
        if (answer && answer.result) reply({ type: 'result', result: answer.result });
        else reply({ type: 'error', message: (answer && answer.error) || 'The search did not work. Please try again.' });
      } catch (e) {
        reply({ type: 'error', message: 'Please log in to the website to use the Lie Finder.' });
      }
    }
  });

  reply({ type: 'hello' });
});
