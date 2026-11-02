# Belief Counseling AI Knowledge Package

One master copy of everything an AI needs to teach and reason like Dr. Brian Campbell,
so the same materials can be loaded into Claude, Grok, or any other AI.

Never put real client names or details in any file here.

**Important: this GitHub repository is public.** Anyone can see what is uploaded here. Do not upload
your book text (*Pearls*, *Godly Counsel*, *Christlike*), the Project instructions, or any
unpublished material you want to keep private. Keep those in a private place instead (a private
GitHub repository, Google Drive, or a folder on your computer) and load them into the AI from there.

---

## Part 1: What to bring over from the Claude Project ("Belief Therapy" on claude.ai)

These live only in the Claude Project today. Gather them into one private folder.

- [ ] **The Project instructions.** Open the Belief Therapy project on claude.ai, open its
      instructions, select all of the text, copy it, and paste it into a new
      file named `instructions.md`, kept in your private folder (not this public repository).
      This is the most important item: it holds the voice, the Identify, Challenge, Replace
      steps, and how to coach a counselor.
- [ ] **The knowledge files (about 38).** The project's file list shows each document.
      Gather the originals (from your computer, Google Drive, or the project itself) into your
      private folder. Only material already meant to be public belongs in this repository.
- [ ] **A list of the files** (file name and one line on what each covers), so nothing is
      missed and duplicates can be spotted.
- [ ] **Remove anything with real client information** before uploading.

Known items in the project's knowledge (from earlier work): the Belief Therapy model and
workflow, the "I Am Worthless" counseling companion, intake worksheets (Discover the Lies,
Deeper Issues), the 32-case training curriculum and Training Mode instructions, and
material from *Pearls* and *Godly Counsel*.

## Part 2: Already on GitHub (no action needed)

| What | Where |
|---|---|
| False belief cards (120 Spiritual/Religious, plus Core, Biological, Interpersonal, Psychological, Sociocultural, Socioeconomic) | `belief-cards/` (web pages and PDFs) |
| Card source data | `tools/cards/` and the other `tools/<set>/` folders (JSON) |
| Master list of 447 false beliefs, with origins and client words | `lie-finder/master-list.json` |
| False Belief Finder search instructions | `lie-finder/search-instructions.md` |
| Belief lists shown on the website | `belief-lists/` |
| DSM-5-TR teaching reviews (29) | `counselors/reviews/` (PDFs; sources in `tools/reviews/`) |
| Clinical forms: Cognitive Errors Checklist, Questioning False Beliefs, Parental Messages Checklist | `counselors/forms/` |
| Counselors' Room pages (Process, Theory, Core False Beliefs, Library, Videos) | `counselors/` |
| Public pages (Beliefs?, Belief Counseling?, Behavioral Experiments, Help for You) | `pages/` |
| Counseling companion (I Am Worthless), Core Beliefs, Life Events screening | top folder |
| Videos | listed on `counselors/videos.html` (stored on YouTube) |

## Part 3: Loading the package into an AI

- **Claude (Project):** upload the files to Project knowledge and paste `instructions.md`
  into the Project instructions.
- **Grok (app):** use a Grok Project (or similar workspace) with the same files and
  instructions.
- **Grok or Claude on the website:** the site code reads files from GitHub (as the False
  Belief Finder already does). For a large document set, xAI "Collections" or a similar
  document store can hold the files for searching.
- **Test before switching:** run the same practice cases through each AI and compare.
