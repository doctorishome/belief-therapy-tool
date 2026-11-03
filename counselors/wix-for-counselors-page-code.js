// Page code for the Wix "For Counselors" page (page file: public/pages/ceafa.js).
// Shows the public landing page (counselors/landing.html) to visitors and the
// members-only Welcome page (counselors/welcome.html) to signed-in members, in the
// same embed box (#html1). The landing page's buttons send messages here:
//   cc-start-free-week -> Wix checkout for the Clinical Companion plan (sign up + free week)
//   cc-login           -> Wix log-in window
//   navigate {path}    -> move to another page of this site (for example "/" = public home page)
import { currentMember, authentication } from 'wix-members-frontend';
import { checkout, orders } from 'wix-pricing-plans-frontend';
import wixLocationFrontend from 'wix-location-frontend';

const GH = 'https://doctorishome.github.io/belief-therapy-tool/counselors/';
const PLAN_ID = 'e3d1c25e-0e6e-4ced-a2c3-32af360e23df';   // "Clinical Companion": 7 days free, then $29.95/month
const REQUIRE_PAID = false;   // keep in step with masterPage.js; set to true when membership launches

async function isMember() {
  const member = await currentMember.getMember();
  if (!member) return false;
  if (!REQUIRE_PAID) return true;
  const list = await orders.listCurrentMemberOrders();
  return list.some((o) => o.status === 'ACTIVE');
}

$w.onReady(async function () {
  const member = await isMember();
  $w('#html1').src = GH + (member ? 'welcome.html' : 'landing.html');
  try { $w('#section5').collapse(); } catch (e) {}   // old sign-up section; the landing page replaces it

  authentication.onLogin(() => wixLocationFrontend.to('/blank-11'));

  $w('#html1').onMessage(async (event) => {
    const d = event.data || {};
    if (d.type === 'cc-start-free-week') {
      try {
        await checkout.startOnlinePurchase(PLAN_ID);
        wixLocationFrontend.to('/blank-11');
      } catch (e) {
        console.error('Checkout could not start', e);
        wixLocationFrontend.to('/blank-11');
      }
    } else if (d.type === 'cc-login') {
      try { await authentication.promptLogin(); } catch (e) {}
    } else if (d.type === 'navigate' && typeof d.path === 'string' && d.path.startsWith('/')) {
      wixLocationFrontend.to(d.path);
    }
  });
});
