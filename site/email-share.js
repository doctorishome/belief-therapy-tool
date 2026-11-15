/* Email a card or a page. The To line is left empty.
   Loaded by belief cards, belief lists, the counselors landing page, and the Counselors' Room. */
(function () {
  var SITE = "https://www.beliefcounselor.com";
  var DISCLAIMER = "This educational resource is not a diagnosis or a substitute for professional care.";
  var MAX = 1800;
  var PAGES = [
    { test: /\/belief-lists\/psychological\.html$|\/belief-cards\/psychological\//, url: SITE + "/blank-7" },
    { test: /\/belief-lists\/biological|\/belief-cards\/biological\//, url: SITE + "/biological-physical-false-beliefs" },
    { test: /\/belief-lists\/interpersonal|\/belief-cards\/interpersonal\//, url: SITE + "/blank-8" },
    { test: /\/belief-lists\/socioeconomic|\/belief-cards\/socioeconomic\//, url: SITE + "/blank-9" },
    { test: /\/belief-lists\/sociocultural|\/belief-cards\/sociocultural\//, url: SITE + "/blank-10" },
    { test: /\/belief-lists\/spiritual|\/belief-cards\/Belief-|\/belief-cards\/spiritual/, url: SITE + "/spiritual-religious-false-beliefs" },
    { test: /\/belief-lists\/core|\/belief-cards\/core\//, url: SITE + "/core-beliefs" },
    { test: /\/counselors\/landing\.html$|\/members\//, url: SITE + "/blank-11" }
  ];

  function text(el) {
    return el ? String(el.textContent || "").replace(/\s+/g, " ").trim() : "";
  }
  function clip(s, n) {
    s = String(s || "").trim();
    if (s.length <= n) return s;
    return s.slice(0, n - 1).replace(/\s+\S*$/, "") + "…";
  }
  function publicPage() {
    var path = location.pathname || "";
    for (var i = 0; i < PAGES.length; i++) {
      if (PAGES[i].test.test(path)) return PAGES[i].url;
    }
    return SITE + "/blank-7";
  }
  function cardNumber() {
    var tag = text(document.querySelector(".tag"));
    var m = tag.match(/#\s*(\d+)/);
    if (m) return m[1];
    m = (location.pathname || "").match(/(?:Psych|Socio|Cult|Bio|Core|Belief|Marriage|Inter)-(\d+)/);
    return m ? String(parseInt(m[1], 10)) : "";
  }
  function beliefText() {
    var h = text(document.querySelector("h1"));
    return h.replace(/^[“"]+|[”"]+$/g, "");
  }
  function truthText() {
    var p = document.querySelector("p.truth");
    if (p) return text(p);
    var heads = document.querySelectorAll("h2");
    for (var i = 0; i < heads.length; i++) {
      if (/truth summary/i.test(heads[i].textContent || "")) {
        var n = heads[i].nextElementSibling;
        if (n) return text(n);
      }
    }
    return "";
  }
  function pageTitle() {
    var h = text(document.querySelector("h1"));
    if (h) return h;
    return (document.title || "Belief Counseling").replace(/\s+/g, " ").trim();
  }
  var PROCESS = "https://doctorishome.github.io/belief-therapy-tool/members/process.html";
  function keyVerse() {
    var k = document.querySelector(".key");
    if (!k) return "";
    var q = text(k.querySelector("q")), r = text(k.querySelector(".ref"));
    if (!q) return "";
    return "\u201c" + q + "\u201d" + (r ? " " + r : "");
  }
  function sharedDraft() {
    var belief = clip(beliefText(), 300);
    var truth = clip(truthText(), 400);
    var verse = clip(keyVerse(), 400);
    var body = "I pray that this Belief Counseling information might be helpful:";
    body += "\n\nThe lie: \"" + belief + "\"";
    if (truth) body += "\n\nThe truth: " + truth;
    if (verse) body += "\n\nScripture: " + verse;
    body += "\n\nRead more here:\n" + cardAddress();
    body += "\n\nFor a general overview of Belief Counseling, see:\n" + PROCESS;
    body += "\n\n" + DISCLAIMER;
    return { subject: "Belief Counseling information you may find helpful", body: body };
  }
  function cardAddress() {
    return location.origin + location.pathname;
  }
  function cardDraft(direct) {
    var num = cardNumber();
    var belief = clip(beliefText(), 400);
    var truth = clip(truthText(), 500);
    var link = direct ? cardAddress() : publicPage() + (num ? "#card-" + num : "");
    var body = "I thought this Belief Counseling card might be helpful:\n\n\"" + belief + "\"";
    if (truth) body += "\n\n" + truth;
    body += "\n\nRead more here:\n" + link;
    if (num) body += "\n\nThis is card #" + num + ".";
    if (direct) body += "\n\nVisit the Belief Counseling website:\n" + SITE;
    body += "\n\n" + DISCLAIMER;
    if (body.length > MAX) {
      body = "I thought this Belief Counseling card might be helpful:\n\n\"" + clip(belief, 240) + "\"";
      body += "\n\nRead more here:\n" + link;
      if (num) body += "\n\nThis is card #" + num + ".";
      body += "\n\n" + DISCLAIMER;
    }
    return { subject: "A Belief Counseling card you may find helpful", body: body };
  }
  function pageDraft() {
    var title = clip(pageTitle(), 180);
    var link = publicPage();
    var body = "I thought this Belief Counseling page might be helpful:\n\n" + title +
      "\n\nRead more here:\n" + link + "\n\n" + DISCLAIMER;
    return { subject: "A Belief Counseling page you may find helpful", body: body };
  }
  function mailto(draft) {
    return "mailto:?subject=" + encodeURIComponent(draft.subject) +
      "&body=" + encodeURIComponent(draft.body);
  }
  function openMail(href) {
    var a = document.createElement("a");
    a.href = href;
    a.target = "_top";
    a.rel = "noopener";
    a.style.display = "none";
    document.body.appendChild(a);
    a.click();
    a.remove();
  }
  window.beliefEmailDraft = function (kind, direct) {
    var draft = kind === "page" ? pageDraft() : (direct ? sharedDraft() : cardDraft(false));
    draft.href = mailto(draft);
    return draft;
  };

  var css = document.createElement("style");
  css.textContent =
    ".emailshare{margin:10px 0 14px;font:14px/1.3 Arial,Helvetica,sans-serif}" +
    ".emailshare-btn{display:inline-flex;align-items:center;gap:6px;color:#1e3556;text-decoration:none;" +
    "border:1px solid #c4b48a;background:#fffdf8;border-radius:999px;padding:5px 12px}" +
    ".emailshare-btn:hover{border-color:#a8864f;color:#a8864f}" +
    ".emailshare-btn svg{display:block}" +
    "@media print{.emailshare{display:none !important}}";
  document.head.appendChild(css);

  document.addEventListener("click", function (e) {
    var a = e.target.closest ? e.target.closest("a[data-email]") : null;
    if (!a) return;
    e.preventDefault();
    var draft = window.beliefEmailDraft(a.getAttribute("data-email"), a.getAttribute("data-link") === "card");
    openMail(draft.href);
  });

  function tagCards() {
    var links = document.querySelectorAll("a[href]");
    for (var i = 0; i < links.length; i++) {
      var href = links[i].getAttribute("href") || "";
      var m = href.match(/(?:Psych|Socio|Cult|Bio|Core|Belief|Marriage|Inter)-(\d+)/);
      if (!m) continue;
      var li = links[i].closest ? links[i].closest("li") : null;
      var el = li || links[i];
      if (!el.id) el.id = "card-" + parseInt(m[1], 10);
    }
  }
  function reveal() {
    tagCards();
    var m = (location.hash || "").match(/^#card-(\d+)$/);
    if (!m) return;
    var el = document.getElementById("card-" + m[1]);
    if (!el) return;
    var box = el.closest ? el.closest("details") : null;
    if (box) box.open = true;
    try { el.scrollIntoView({ block: "center" }); } catch (err) { el.scrollIntoView(); }
  }
  if (document.readyState === "loading") document.addEventListener("DOMContentLoaded", reveal);
  else reveal();
  setTimeout(reveal, 400);
})();
