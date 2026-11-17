// Page code for the Wix "For Counselors" page (page file: public/pages/ceafa.js).
// Shows the public landing page (counselors/landing.html) to visitors and the
// members-only Welcome page (counselors/welcome.html) to signed-in members, in the
// same embed box (#html1). The landing page's buttons send messages here:
//   cc-start-free-week -> Wix checkout for the Clinical Companion plan (sign up + free week)
//   cc-login           -> Wix log-in window
//   navigate {path}    -> move to another page of this site (for example "/" = public home page)
//   cc-member-status?  -> answers {type:'cc-member-status', member:true/false} (Weekly Tips lock)
// A link like /blank-11?tip=tip-demonic-possession opens counselors/<tip>.html in the box
// (used by the weekly tip emails; only simple names made of letters, numbers and dashes).
// Members-only tips: /blank-11?tip=members-tip&t=<name>. counselors/members-tip.html sends
//   cc-tip? {slug} and gets {type:'cc-tip', ok, html} back from the private ProTips collection.
import { currentMember, authentication } from 'wix-members-frontend';
import { checkout, orders } from 'wix-pricing-plans-frontend';
import wixLocationFrontend from 'wix-location-frontend';
import { getMembersTip } from 'backend/cc-membership.web';

const GH = 'https://doctorishome.github.io/belief-therapy-tool/counselors/';
const PLAN_ID = 'e3d1c25e-0e6e-4ced-a2c3-32af360e23df';   // "Clinical Companion": 7 days free, then $29.95/month
const REQUIRE_PAID = true;    // keep in step with masterPage.js
const ADMIN_ROLE_ID = '00000000-0000-0000-0000-000000000001'; // Wix's built-in "Admin" role

async function isMember() {
  const member = await currentMember.getMember();
  if (!member) return false;
  if (!REQUIRE_PAID) return true;
  try {
    const roles = await currentMember.getRoles();
    if ((roles || []).some((r) => r._id === ADMIN_ROLE_ID || r.title === 'Admin')) return true;
  } catch (e) {}
  try {
    const list = await orders.listCurrentMemberOrders({ orderStatuses: ['ACTIVE'] });
    return (list || []).some((o) => o.planId === PLAN_ID && o.status === 'ACTIVE');
  } catch (e) {
    return false;
  }
}

async function showRightPage() {
  const member = await isMember();
  const tip = String(wixLocationFrontend.query.tip || '');
  const t = String(wixLocationFrontend.query.t || '');   // members-only tip name, for counselors/members-tip.html
  $w('#html1').src = /^[a-z0-9-]+$/.test(tip) ? GH + tip + '.html' + (/^[a-z0-9-]+$/.test(t) ? '?t=' + t : '') : GH + (member ? 'welcome.html' : 'landing.html');
  return member;
}

$w.onReady(async function () {
  await showRightPage();
  try { $w('#section5').collapse(); } catch (e) {}   // old sign-up section; the landing page replaces it

  // Moving to the same page doesn't reload it, so re-check membership in place after login.
  authentication.onLogin(async () => { await showRightPage(); });

  $w('#html1').onMessage(async (event) => {
    const d = event.data || {};
    if (d.type === 'cc-start-free-week') {
      try {
        await checkout.startOnlinePurchase(PLAN_ID);
        await showRightPage();
      } catch (e) {
        console.error('Checkout could not start', e);
        wixLocationFrontend.to('/blank-11');   // sign-up page ("For Counselors"); /plans-pricing does not exist
      }
    } else if (d.type === 'cc-tip?' && typeof d.slug === 'string') {
      let r = { ok: false, reason: 'members-only' };
      try { r = await getMembersTip(d.slug); } catch (e) {}
      $w('#html1').postMessage({ type: 'cc-tip', slug: d.slug, ok: !!r.ok, html: r.ok ? r.html : '', reason: r.reason || '' });
    } else if (d.type === 'cc-member-status?') {
      $w('#html1').postMessage({ type: 'cc-member-status', member: await isMember() });
    } else if (d.type === 'cc-login') {
      try { await authentication.promptLogin(); } catch (e) {}
    } else if (d.type === 'navigate' && typeof d.path === 'string' && d.path.startsWith('/')) {
      wixLocationFrontend.to(d.path);
    }
  });
});
