/* Level meter + Back/Forward bar for the six Belief Mining levels.
   Use on a page:  <div id="level-nav" data-level="bio" data-stage="results"></div>
                   <script src="https://doctorishome.github.io/belief-therapy-tool/level-pages/level-nav.js"></script>
   data-level: bio | psych | inter | socioeconomic | sociocultural | spiritual
   data-stage: explore (the level page)  or  results (the level's False Beliefs page)
   data-bar="no" shows only the meter (used on level pages, which have their own bar). */
(function () {
  var SITE = "https://doctorishome.wixstudio.com/website-6";
  var LEVELS = [
    { key: "bio",           name: "Biological/Physical",     explore: "/biological-physical",     results: "/biological-physical-false-beliefs" },
    { key: "psych",         name: "Psychological/Cognitive", explore: "/psychological-cognitive", results: "/blank-7" },
    { key: "inter",         name: "Interpersonal",           explore: "/interpersonal",           results: "/blank-8" },
    { key: "socioeconomic", name: "Socioeconomic",           explore: "/socioeconomic",           results: "/blank-9" },
    { key: "sociocultural", name: "Sociocultural",           explore: "/blank",                   results: "/blank-10" },
    { key: "spiritual",     name: "Spiritual/Religious",     explore: "/blank-4",                 results: "/spiritual-religious-false-beliefs" }
  ];
  var AFTER_LAST = { label: "Forward to Core False Beliefs", path: "/core-beliefs" };

  var box = document.getElementById("level-nav");
  if (!box) return;
  var key = box.getAttribute("data-level") || "bio";
  var stage = box.getAttribute("data-stage") || "results";
  var idx = 0; LEVELS.forEach(function (l, i) { if (l.key === key) idx = i; });
  var L = LEVELS[idx];

  var css = document.createElement("style");
  css.textContent =
    ".lvn{max-width:1040px;margin:40px auto 0;font-family:'Helvetica Neue',Helvetica,Arial,sans-serif;color:#1b2a41}" +
    ".lvn-title{font-size:13px;letter-spacing:.08em;text-transform:uppercase;color:#8C6D3F;font-weight:700;margin:0 0 10px}" +
    ".lvn-track{display:grid;grid-template-columns:repeat(6,1fr);gap:6px}" +
    ".lvn-step{display:block;text-decoration:none;color:#5E554A;border-top:6px solid #E6DCC8;padding:8px 4px 0;font-size:13px;line-height:1.3}" +
    ".lvn-step b{display:block;font-size:12px;color:#8C6D3F}" +
    ".lvn-step.done{border-top-color:#d9b45a;color:#1b2a41}" +
    ".lvn-step.now{border-top-color:#1b2a41;color:#1b2a41;font-weight:700}" +
    ".lvn-step.now b{color:#1b2a41}" +
    ".lvn-step:hover{color:#1b2a41;text-decoration:underline}" +
    ".lvn-where{margin:10px 0 0;font-size:15px;color:#5E554A}" +
    ".lvn-bar{margin:22px 0 0;background:#1b2a41;border-radius:12px;padding:18px 24px;display:flex;align-items:center;justify-content:space-between;gap:18px}" +
    ".lvn-back{color:#fff;font-size:17px;font-weight:700;text-decoration:none}" +
    ".lvn-back:hover{text-decoration:underline}" +
    ".lvn-go{flex:none;background:#d9b45a;color:#1b2a41;font-weight:700;font-size:15px;border-radius:999px;padding:12px 22px;text-decoration:none}" +
    ".lvn-go:hover{background:#e8c873}" +
    "@media(max-width:640px){.lvn-track{grid-template-columns:repeat(3,1fr);row-gap:12px}.lvn-bar{flex-direction:column;align-items:flex-start;padding:16px}}";
  document.head.appendChild(css);

  function esc(s) { return String(s).replace(/&/g, "&amp;").replace(/</g, "&lt;").replace(/"/g, "&quot;"); }

  var steps = LEVELS.map(function (l, i) {
    var cls = i < idx ? "done" : (i === idx ? "now" : "");
    return '<a class="lvn-step ' + cls + '" href="' + SITE + l.explore + '" data-path="' + l.explore + '"' + (i === idx ? ' aria-current="step"' : "") +
           "><b>Level " + (i + 1) + "</b>" + esc(l.name) + "</a>";
  }).join("");
  var where = "You are on Level " + (idx + 1) + " of 6: " + esc(L.name) + (stage === "results" ? " — False Beliefs" : " — Explore");
  var h = '<div class="lvn"><p class="lvn-title">Belief Mining progress</p><div class="lvn-track">' + steps + '</div><p class="lvn-where">' + where + "</p>";

  if (box.getAttribute("data-bar") !== "no") {
    var next = LEVELS[idx + 1];
    var fwd = next ? { label: "Forward to Level #" + (idx + 2) + ": " + next.name, path: next.explore } : AFTER_LAST;
    var back = stage === "results" ? { label: "← Back to Level #" + (idx + 1) + ": " + L.name, path: L.explore }
                                   : { label: "← Back to Belief Mining", path: "/belief-mining" };
    h += '<div class="lvn-bar"><a class="lvn-back" href="' + SITE + back.path + '" data-path="' + back.path + '">' + esc(back.label) + "</a>" +
         '<a class="lvn-go" href="' + SITE + fwd.path + '" data-path="' + fwd.path + '">' + esc(fwd.label) + " →</a></div>";
  }
  box.innerHTML = h + "</div>";

  // Inside a Wix page, ask the page code to move in the same window; otherwise open a new tab.
  box.querySelectorAll("a[data-path]").forEach(function (a) {
    a.addEventListener("click", function (e) {
      e.preventDefault();
      var p = a.getAttribute("data-path"), done = false;
      function onAck(ev) { if (ev.data && ev.data.type === "navigate-ok") done = true; }
      window.addEventListener("message", onAck);
      try { window.parent.postMessage({ type: "navigate", path: p }, "*"); } catch (x) {}
      setTimeout(function () { window.removeEventListener("message", onAck); if (!done) window.open(SITE + p, "_blank"); }, 700);
    });
  });
})();
