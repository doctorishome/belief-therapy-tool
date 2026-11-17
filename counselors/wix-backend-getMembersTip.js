// Added to the Wix backend file backend/cc-membership.web.js (Nov 17, 2026), plus at the top:
//   import wixData from "wix-data";
// (isAdmin, members, orders, currentMember, webMethod and Permissions are already in that file.)

// Members-only Professional Tips.
// The tip pages are kept in the private CMS collection "ProTips" (read: Admin only), not on GitHub.
// Returns a tip only to a site owner/admin or a member with an active Clinical Companion plan.
const TIPS_PLAN_ID = "e3d1c25e-0e6e-4ced-a2c3-32af360e23df";
export const getMembersTip = webMethod(Permissions.Anyone, async (slug) => {
  slug = String(slug || "");
  if (!/^[a-z0-9-]+$/.test(slug)) return { ok: false, reason: "not-found" };
  let staff = false;
  try { staff = isAdmin(await currentMember.getRoles()); } catch (e) { staff = false; }
  if (!staff) {
    let memberId = "";
    try {
      const current = await members.getCurrentMember();
      const member = current && current.member ? current.member : current;
      memberId = member && member._id ? String(member._id) : "";
    } catch (e) { memberId = ""; }
    if (!memberId) return { ok: false, reason: "members-only" };
    let active = false;
    try {
      const list = await orders.memberListOrders();
      active = ((list && list.orders) || []).some((o) => o && o.planId === TIPS_PLAN_ID && (o.status === "ACTIVE" || o.statusNew === "ACTIVE"));
    } catch (e) { active = false; }
    if (!active) return { ok: false, reason: "members-only" };
  }
  try {
    const item = await wixData.get("ProTips", slug, { suppressAuth: true });
    if (!item || !item.html) return { ok: false, reason: "not-found" };
    return { ok: true, html: item.html };
  } catch (e) {
    return { ok: false, reason: "not-found" };
  }
});
