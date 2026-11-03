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
import { signMembershipToken } from "backend/cc-token";

const elevatedGetSecretValue = elevate(secrets.getSecretValue);

function secretString(value) {
  if (typeof value === "string") return value.trim();
  if (value && typeof value.value === "string") return value.value.trim();
  return "";
}

export const mintClinicalCompanionToken = webMethod(Permissions.SiteMember, async () => {
  const current = await members.getCurrentMember();
  const member = current && current.member ? current.member : current;
  if (!member || !member._id) throw new Error("Sign in on the website first.");
  const list = await orders.memberListOrders();
  const active = ((list && list.orders) || []).find((order) => order && (order.status === "ACTIVE" || order.statusNew === "ACTIVE"));
  if (!active) throw new Error("An active membership is required.");
  const secret = secretString(await elevatedGetSecretValue("CC_MEMBERSHIP_SECRET"));
  if (!secret) throw new Error("Membership token is not configured.");
  return { token: await signMembershipToken(member._id, secret), expiresInHours: 8 };
});
