/* Visitor preview of the Counselors' Room. Does nothing unless ?view=visitor is in the URL,
   so the live member pages stay exactly as they are. */
(function () {
  if (!/[?&]view=visitor(?:&|$)/.test(location.search || "")) return;

  var OPEN = { "process.html": 1, "assessment.html": 1 };
  var SIGNUP = "https://www.beliefcounselor.com/blank-11";

  var css = document.createElement("style");
  css.textContent =
    ".vlock{font-size:.85em}" +
    ".vmemb{display:block;font:11px/1.2 Arial,Helvetica,sans-serif;font-weight:normal;letter-spacing:0;text-transform:none;color:#c9a227}" +
    ".nav a .vmemb{color:#e7d7a2}" +
    ".vpanel{background:#fff;border:1px solid #e3dcc6;border-left:4px solid #c9a227;border-radius:0 8px 8px 0;padding:22px 20px;margin:12px 0;max-width:640px}" +
    ".vpanel h2{margin:0 0 8px;color:#12284c;font-size:1.45rem;border:0}" +
    ".vpanel p{margin:0 0 12px;color:#1f2a3a}" +
    ".vbtn{display:inline-block;background:#12284c;color:#fff;font:bold 16px Arial,Helvetica,sans-serif;text-decoration:none;border-radius:24px;padding:10px 18px}" +
    ".vbtn:hover{background:#1d3a6b}" +
    ".vlogin{font-size:.95rem;color:#5b6678}" +
    ".vlogin a{color:#12284c;font-weight:bold}" +
    "a.card .vmemb, .start a .vmemb{color:#c9a227}";
  document.head.appendChild(css);

  function fileOf(href) {
    href = (href || "").split("?")[0].split("#")[0];
    var parts = href.split("/");
    return parts[parts.length - 1] || "";
  }
  function here() {
    return fileOf(location.pathname) || "index.html";
  }
  function isOpen(href) {
    var f = fileOf(href);
    return OPEN[f] === 1;
  }
  function keepLink(a) {
    if (a.classList.contains("lf") || a.classList.contains("pub")) return true;
    var href = a.getAttribute("href") || "";
    if (href.indexOf("false-belief-finder") !== -1) return true;
    if (href.indexOf("membership") !== -1) return true;
    if (href.indexOf("http") === 0 && href.indexOf("beliefcounselor.com/blank-11") !== -1) return true;
    return false;
  }
  function stamp(a) {
    if (a.querySelector(".vlock")) return;
    a.insertAdjacentHTML("beforeend", ' <span class="vlock" aria-hidden="true">\uD83D\uDD12</span><span class="vmemb">Members only</span>');
  }
  function panelHtml() {
    return '<div class="vpanel"><h2>Members only</h2>' +
      '<p>Members only — sign up for the Counselors\u2019 Room ($14.95/month) to open this.</p>' +
      '<p><a class="vbtn" target="_top" href="' + SIGNUP + '">Sign up — $14.95/month</a></p>' +
      '<p class="vlogin">Already a member? <a target="_top" href="' + SIGNUP + '">Log in</a></p></div>';
  }
  function showPanel() {
    var wrap = document.querySelector(".wrap");
    if (!wrap) return;
    wrap.innerHTML = panelHtml();
  }
  function carry(a) {
    var href = a.getAttribute("href") || "";
    if (!href || href.charAt(0) === "#" || href.indexOf("mailto:") === 0) return;
    if (href.indexOf("view=visitor") !== -1) return;
    if (href.indexOf("http") === 0) return;
    a.setAttribute("href", href + (href.indexOf("?") >= 0 ? "&" : "?") + "view=visitor");
  }

  document.querySelectorAll(".nav a, .start a, a.card").forEach(function (a) {
    if (keepLink(a)) return;
    var href = a.getAttribute("href") || "";
    if (href.indexOf(".html") === -1) return;
    carry(a);
    if (isOpen(href)) return;
    stamp(a);
    a.addEventListener("click", function (e) {
      e.preventDefault();
      showPanel();
    });
  });

  var page = here();
  if (page === "assessment.html") {
    var wrap = document.querySelector(".wrap");
    if (wrap) {
      var keep = false;
      Array.prototype.forEach.call(wrap.children, function (el) {
        if (el.tagName === "H2" && /Live Interactive Diagnosis Practice/.test(el.textContent || "")) keep = true;
        else if (el.tagName === "H2") keep = false;
        if (!keep) el.style.display = "none";
      });
    }
  } else if (page !== "process.html" && page !== "index.html") {
    showPanel();
  }
})();
