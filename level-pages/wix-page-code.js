// Page code for each Belief Mining level page (Wix Studio site "Pearls Working 5").
// Lets the GitHub box at the bottom (level-pages/tools.html) move visitors to another page
// of this site in the same window when they click "Back to Belief Mining" or the gold
// "Forward to Level #N Mining Results" button.
// Works with every embed box on the page, whatever its ID.

import wixLocationFrontend from 'wix-location-frontend';

$w.onReady(function () {
  $w('HtmlComponent').forEach((box) => {
    box.onMessage((event) => {
      const data = event.data;
      if (data && data.openPdf) {
        wixLocationFrontend.to(data.openPdf);
        return;
      }
      if (data && data.type === 'navigate' && typeof data.path === 'string' && data.path.startsWith('/')) {
        try { box.postMessage({ type: 'navigate-ok' }); } catch (e) {}
        wixLocationFrontend.to(data.path);
      }
    });
  });
});
