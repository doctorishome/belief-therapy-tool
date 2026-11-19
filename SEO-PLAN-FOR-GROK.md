# Instructions for Grok: Make beliefcounselor.com visible to Google (SEO)

Hello Grok. You are helping Dr. Brian Campbell with his website, **beliefcounselor.com** ("Belief Counseling").
Please read this whole page before doing anything.

## Who you are working with
- Dr. Campbell is a retired psychologist, **not a technical person**. Explain everything in plain language, one step at a time, with no jargon.
- When he must click something himself, tell him exactly where it is on the screen. If you are not sure where a button is, say so. Do not guess.
- **Ask him before you publish anything, delete anything, or change a page's web address.** Show him the change first.
- Work through the jobs below **in order**, one at a time. After each job, tell him in two or three sentences what you did and what he will see.

## How the website is built (important)
- The website is a **Wix Studio** site. In his Wix account the site is called **"Pearls Working 5 "** (site ID `f5ebb4be-1a1e-48f8-8fa9-70737c1c6393`). There are also copies called "Pearls Working 5 D1", "R" and "R2". **Do not touch the copies.** Only the main site is live at beliefcounselor.com.
- Much of the content is **not stored in Wix**. It is stored as files in the GitHub repository **github.com/doctorishome/belief-therapy-tool**, shown live at **doctorishome.github.io/belief-therapy-tool/**, and displayed on the Wix pages inside embed boxes (iframes).
- In that repository, read **`AGENTS.md`** and **`PROGRESS.md`** first. PROGRESS.md is the running record of how everything was built. Add a short dated note at the bottom of PROGRESS.md for anything you change.
- The **Counselors' Room** is the members' area (Wix page `/blank-11`, the files in `members/` and `counselors/`, and Wix pages `/false-belief-finder` and `/counselor-scriptures`). Members-only material must **not** be shown in Google. The public pages should be shown.
- **Do NOT rename these Wix page addresses:** `/blank-11`, `/false-belief-finder`, `/counselor-scriptures`, `/scriptures`, `/find-help`, `/help`. Many GitHub files link straight to them (for example `/blank-11?tip=...`), and renaming them would break those links.
- Do not change any Wix **page code** (the code panel at the bottom of the Wix editor). The Lie Finder, the Scripture lookup limits, and the membership checks depend on it.

## Job 1: Change the site's name from "Pearls Working 5" to "Belief Counseling"
Right now every browser tab and every Google result says "… | Pearls Working 5". That is an old working name.
1. In the Wix dashboard for the site, find the site name and the default title format for search results (Wix keeps these in the site's **Settings** and its **SEO** settings). Check the current Wix Help Center for the exact place, because Wix moves things around.
2. Change the name shown to visitors and to Google to **Belief Counseling**.
3. Check two or three pages afterward. The browser tab should read, for example, "Home | Belief Counseling".
4. Do **not** rename the site in a way that changes its web address (beliefcounselor.com must stay the same).

## Job 2: Connect the site to Google Search Console
1. In the Wix dashboard, open **Marketing & SEO → SEO** (or search the dashboard for "SEO Setup Checklist"), and follow Wix's **SEO Setup Checklist**. It connects the site to **Google Search Console** and sends Google the site's map of pages (the sitemap, at beliefcounselor.com/sitemap.xml).
2. Dr. Campbell will need to sign in to his Google account when Wix asks. Tell him when that moment comes and what he will see.
3. When it is done, confirm that Search Console shows the site as verified and that the sitemap was accepted. (Google can take days or weeks to show the site in results. That is normal.)

## Job 3: Hide the members-only pages and test pages from Google
In the Wix editor, each page has **Settings → SEO basics** with a switch for whether search engines may show the page. Turn that switch **off** (do not let search engines index) for:
- The Counselors' Room pages: `/blank-11` (For Counselors), `/false-belief-finder`, `/counselor-scriptures`, and any page whose name says Counselor, Member, Clinical, Membership, Plans, Paywall, or Program.
- Any test, copy, or unused page (names like "Copy of…", "New page", "blank-…" that are not in the public menu). **List them for Dr. Campbell first and ask before changing them.**
Leave the switch **on** for the public pages: Home, Beliefs?, Belief Counseling?, the Belief Mining pages, Identify / Challenge / Replace False Beliefs pages, Core False Beliefs, Spiritual/Religious False Beliefs, Pearls Scripture Search (`/scriptures`), Find Help, Search False Beliefs, and Help.

## Job 4: Give public pages clear web addresses
Some public pages have addresses like `/blank-5` or `/blank-7`. For each **public** page with a "blank" address (except the ones listed above under "Do NOT rename"):
1. First make a list: page name, current address, suggested new address (short, lowercase, words joined by hyphens, for example `/behavioral-experiments`). **Show Dr. Campbell the list and wait for his OK.**
2. Then, in the Wix editor, page **Settings → SEO basics → URL slug**, change the address. When Wix offers to **create a 301 redirect** from the old address, say **yes**, so old links keep working.
3. Search the GitHub repository for the old address (for example search for `blank-5`). If any file links to it, update the link and note it in PROGRESS.md.

## Job 5: Write a title and description for each public page
For each public page, in **Settings → SEO basics**:
- **Title tag:** about 50–60 characters, saying what the page is, ending with "| Belief Counseling". Example: "Core False Beliefs: 22 Lies That Hurt Us | Belief Counseling".
- **Meta description:** one or two plain sentences (about 150 characters) that would make a hurting person or a counselor want to click. Example: "Find the false beliefs behind anxiety, depression, and shame, and replace them with the truth of Scripture."
- Use warm, plain, non-clinical language on public pages. **Show Dr. Campbell the wording for all pages in one list and get his OK before entering it.**

## Job 6: Picture descriptions (alt text)
Google cannot see pictures; it reads a short description of each one. On each public page, give every picture a short plain description (for example "Counselor listening to a client in a bright office"). Skip pictures that are only decoration.

## Job 7 (the big one): Words that Google cannot credit to beliefcounselor.com
Many public pages show their content inside embed boxes that load files from **doctorishome.github.io**. Google counts those words as belonging to GitHub, so to Google the Wix pages look almost empty.
**Do not change anything for this job yet.** Instead:
1. Make a list of the public Wix pages whose main content is inside an embed box, and say for each one about how much visible text the Wix page itself has outside the box.
2. Suggest options in plain language, with the work each one would take, for example:
   - adding a short written introduction (2–4 paragraphs) directly on each Wix page, above the embed box, in Wix's own text boxes;
   - for the most important public pages, moving the main text into Wix itself.
3. Do not add "noindex" tags to the GitHub files without asking: that would remove them from Google entirely.
Bring the list and the options to Dr. Campbell and let him decide.

## Job 8: Final check
1. Open each public page on a phone-size screen and a computer screen and confirm nothing looks broken.
2. Confirm that the members-only pages still work for a signed-in member.
3. Give Dr. Campbell a short summary: what was done, what Google will now see, and anything still left to decide.

## Things to avoid
- Do not change the Lie Finder, Scripture lookup, membership, or pricing.
- Do not touch the duplicate Wix sites.
- Do not remove or rename files in the GitHub repository unless a job above says so.
- Do not pay for any Wix or Google upgrade. Everything above can be done for free.
