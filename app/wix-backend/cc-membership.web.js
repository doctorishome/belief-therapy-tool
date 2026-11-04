/**
 * Called from the Wix Counselors page while the member is logged in.
 * Returns a short-lived token the browser app sends to the HTTP function.
 * Does not return the xAI key.
 *
 * Paste this file into the site Backend folder as cc-membership.web.js.
 */
import { Permissions, webMethod } from "wix-web-module";
import { secrets } from "wix-secrets-backend.v2";
import { elevate } from "wix-auth";
import { orders } from "wix-pricing-plans.v2";
import { members } from "wix-members.v2";
import { currentMember } from "wix-members-backend";
import { signMembershipToken } from "backend/cc-token";

const elevatedGetSecretValue = elevate(secrets.getSecretValue);

function secretString(value) {
  if (typeof value === "string") return value.trim();
  if (value && typeof value.value === "string") return value.value.trim();
  return "";
}

function isAdmin(roles) {
  const list = Array.isArray(roles) ? roles : (roles && roles.roles) || [];
  return list.some((role) => String((role && (role.title || role.name)) || "").toLowerCase() === "admin");
}

// Anyone can call this, but the function itself allows only an active plan or a site owner/admin.
// Permissions.SiteMember would turn the owner away after a cancelled test plan.
export const mintClinicalCompanionToken = webMethod(Permissions.Anyone, async () => {
  let staff = false;
  try { staff = isAdmin(await currentMember.getRoles()); } catch (e) { staff = false; }
  let memberId = "";
  try {
    const current = await members.getCurrentMember();
    /** @type {any} */
    const member = current && current.member ? current.member : current;
    memberId = member && member._id ? String(member._id) : "";
  } catch (e) { memberId = ""; }
  if (!memberId && !staff) throw new Error("Sign in on the website first.");
  if (!staff) {
    const list = await orders.memberListOrders();
    const active = ((list && list.orders) || []).find((/** @type {any} */ order) => order && (order.status === "ACTIVE" || order.statusNew === "ACTIVE"));
    if (!active) throw new Error("An active membership is required.");
  }
  const secret = secretString(await elevatedGetSecretValue("CC_MEMBERSHIP_SECRET"));
  if (!secret) throw new Error("Membership token is not configured.");
  const token = await signMembershipToken(memberId || "site-admin", secret, { staff });
  return { token, expiresInHours: 8 };
});
