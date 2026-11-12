# Telephone Intake Form: hand-off to the Clinical Companion

Written November 12, 2026, for whoever builds the secure connection for client information
(Dr. Campbell's Grok helper or another developer).

## What Dr. Campbell wants

The intake person takes the first call on one computer and fills in the on-screen Telephone Intake Form
(`counselors/forms/telephone-intake.html`). The counselor works on a different computer. When the call is
finished, the intake person presses one button, and the intake appears in the counselor's Clinical Companion
as a new client file. Nothing is retyped.

## Where things stand

- The form works today. It can hold a call in the browser on the intake person's computer, print, and save a PDF.
- It does not send anything anywhere. There is no server yet.
- The Clinical Companion (`app/`) keeps cases in an encrypted store in the counselor's own browser
  (`app/js/vault.js`: AES-GCM, key derived from the counselor's password, ciphertext in IndexedDB).
- Because the two computers are different, the browser cannot pass the form across by itself. It has to go
  through the secure connection. Until that exists, the intake person prints or saves the PDF for the counselor.

## What the form would send

One record per call. The names on the left are the field names already used in the form.

| Field | What it holds |
|---|---|
| `callDate`, `callTime`, `takenBy` | When the call came in and who took it |
| `last`, `first` | Client's last name; first and middle name |
| `who`, `whoOther` | `client` or `other`; if other, the caller's name and relationship |
| `adult` | `yes` or `no` (the practice serves adults only) |
| `dob`, `referredBy` | Date of birth; who referred the caller |
| `phone`, `phone2`, `phoneType`, `message` | Best phone, alternate phone, `cell`/`home`/`work`, OK to leave a message `yes`/`no` |
| `email`, `address` | Email (the link to the intake forms goes here) and mailing address |
| `insured`, `insurer` | `yes`/`no`/`private`; insurance company |
| `holder`, `holderDob`, `holderRel` | Policy holder, if not the client |
| `problem` | Nature of the problem, in the caller's words |
| `physician`, `lastExam`, `conditions`, `medications` | Medical background |
| `onList`, `referredTo` | Whether the problem is on the counselor's referral list; who the caller was referred to |
| `explained`, `faith` | Faith-integrated approach explained (`true`/`false`); caller wants faith included `yes`/`no`/`unsure` |
| `apptDate`, `apptTime` | First appointment |
| `forms`, `formsDate` | `online` or `paper`; date the link was sent or the paper forms were given |
| `notes` | Anything else |

Dates are `YYYY-MM-DD`. Times are 24-hour `HH:MM`. The counselor's referral list (14 lines) is a practice
setting, not part of the client record, and stays on the intake computer.

In the form's code, `read()` already returns exactly this record as one object.

## What the connection has to do

1. **Sign-in.** Only a signed-in intake person of that practice can send. Only that practice's counselor can receive.
2. **Encrypted in transit and at rest.** HTTPS for the trip. On the server, the record stays encrypted and is
   held only until the counselor's Companion collects it, then it is deleted from the server.
3. **Covered by the Business Associate Agreement.** This record is client information. It must not pass
   through or rest on any service the agreement does not cover. GitHub Pages and the browser's own storage are not covered.
4. **Delivery into the vault.** When the counselor unlocks the Companion, it collects waiting intakes, creates a
   new case from each (name, contact, insurance, reason for calling, appointment), saves it through
   `vault.js`, and confirms to the server so the waiting copy is erased.
5. **Clear the intake computer.** After a successful send, the form erases its held copy (the same thing
   "Clear for a new caller" does now).
6. **No send if not a fit.** If `adult` is `no` or `onList` is `yes`, the caller was referred elsewhere. The
   practice should decide whether those calls are sent at all or only printed for its own records.

## On the form itself

Add a "Send to Clinical Companion" button beside "Hold this form" once the connection exists. It should say
plainly whether the send worked, and keep the form on screen if it did not.
