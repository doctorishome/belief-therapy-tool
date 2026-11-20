import wixData from 'wix-data';
import wixLocationFrontend from 'wix-location-frontend';
import wixWindowFrontend from 'wix-window-frontend';
import { authentication } from 'wix-members-frontend';
import { useScriptureLookup } from 'backend/lieFinder.web';

// Free trial (Nov 18, 2026): logged-in non-members may open 5 different topics; members and the
// site owner look up without limit. The rules and the count are in backend/lieFinder.web.js.
let lockReason = null;   // 'login' or 'limit' while a topic is locked, otherwise null

let allTopics = [];
let selectedTopic = null;
let printItem = null; // the topic currently shown in the print view (null when not in print view)
const NEW_PRINT_TOPICS = ['anger'];

$w.onReady(async function () {
    const printHandled = await handleEmbeddedPrintRequest();

    // 'Back to topic' button inside the print view
    $w('#html1').onMessage(async (event) => {
        if (event.data && event.data.type === 'pearlsBack' && printItem) {
            // Tell the print view we got the message (so it doesn't use its fallback)
            try { $w('#html1').postMessage({ type: 'pearlsBackAck' }); } catch (e) {}
            await returnFromPrintView(printItem);
        }
    });

    // Print links and the browser Back button change the address without reloading the page,
    // so switch between the print view and the topic view whenever the address changes
    wixLocationFrontend.onChange(async () => {
        const q = wixLocationFrontend.query || {};
        if (q.print && q.id) {
            if (!printItem) await handleEmbeddedPrintRequest();
        } else if (printItem) {
            await returnFromPrintView(printItem);
        }
    });
    // Hide the old 'Return to where you were' button (the print view has its own Back button)
    try { $w('#html2').collapse(); } catch (e) {}
        $w('#html1').onMessage((event) => {
        if (event.data?.type === 'pearlsPrint' && event.data?.url) {
            wixLocationFrontend.to(event.data.url);
        }
    });
    if (!printHandled) $w('#html1').collapse();
    $w('#detailBox').collapse();
    $w('#learnMoreButton').collapse();
    try {
        $w('#emailEmbed').collapse();
        $w('#emailEmbed').onMessage((event) => {
            if (event.data && event.data.type === 'emailReady' && emailHref) {
                $w('#emailEmbed').postMessage({ type: 'emailData', href: emailHref });
            }
        });
    } catch (e) {}


$w('#detailTopicName').collapse();
    $w('#closeDetailButton').collapse();
    // Search box: light cream with a thin gold border to match the page
    try {
        $w('#searchInput').style.backgroundColor = '#FFFDF8';
        $w('#searchInput').style.borderColor = '#B08A4B';
        $w('#searchInput').style.borderWidth = '1px';
        $w('#searchInput').style.borderRadius = '8px';
        $w('#searchInput').customClassList.add('pearls-search');
    } catch (e) {}

    $w('#resultsRepeater').onItemReady(($item, itemData) => {
        // Soft cream behind each topic row
        try { $item('#topicNameText').parent.style.backgroundColor = '#FAF4E6'; } catch (e) {}
        if (itemData._isRelatedHeading) {
            $item('#topicNameText').html =
                '<div style="text-align:center; color:#596653; font-family:Georgia, serif; font-size:20px; font-weight:700; padding:18px 0 8px 0;">See also:</div>';
            return;
        }

        $item('#topicNameText').html =
            `<div style="text-align:center; background-color:#F3E9D2 !important; color:#2D2A26; border:1px solid #D8CDBB; border-radius:8px; padding:16px 14px; font-family:Georgia, serif; font-size:17px; letter-spacing:0.2px;">${escapeHtml(itemData.topicName || '')}</div>`;

        $item('#topicNameText').onClick(async () => {
            await openTopic(itemData);
        });
    });

    $w('#searchInput').onInput(async () => {
        const query = ($w('#searchInput').value || '').trim().toLowerCase();

        selectedTopic = null;
        lockReason = null;
        await $w('#detailBox').collapse();
        await $w('#resultsRepeater').expand();

        if (!query) {
            $w('#resultsRepeater').data = allTopics;
            return;
                  }
        $w('#detailTopicName').collapse();

        
const exactTopic = allTopics.find((item) =>
            normalizeText(item.topicName) === normalizeText(query)
        );

        if (exactTopic) {
            const relatedItems = getRelatedTopicItems(exactTopic.relatedTopics);
            $w('#resultsRepeater').data = relatedItems.length
                ? [exactTopic, createRelatedHeading(exactTopic), ...relatedItems]
                : [exactTopic];
            return;
        }


        $w('#resultsRepeater').data = allTopics.filter((item) =>
            matchesSearch(item, query)
        );
    });

    $w('#learnMoreButton').onClick(async () => {
        if (lockReason === 'login') {
            try { await authentication.promptLogin({ mode: 'signup' }); } catch (e) {}
            if (selectedTopic) await openTopic(selectedTopic);
            return;
        }
        if (lockReason === 'limit') {
            wixLocationFrontend.to('/blank-11');
            return;
        }
        await returnToTopics();
    });

    authentication.onLogin(async () => {
        if (lockReason && selectedTopic) await openTopic(selectedTopic);
    });

    try {
        const results = await wixData.query('PearlsTopics')
            .include('godlyCounselChapter')
            .ascending('topicName')
            .limit(200)
            .find();

        allTopics = results.items;
        $w('#resultsRepeater').data = allTopics;
        // Run after the page has finished appearing (not during Wix's server step)
        setTimeout(() => {
            openTopicFromAddress();
        }, 0);
    } catch (error) {
        console.error('Unable to load Pearls topics:', error);
    }
});

async function openTopic(item, keepAtTop) {
    selectedTopic = item;
    // Keep the topic in the page address so the browser Back button (and print pages) return here
    try { wixLocationFrontend.queryParams.add({ topic: item.urlSlug || item.topicName || '' }); } catch (e) {}
    const relatedItems = getRelatedTopicItems(item.relatedTopics);
    showEmailButton(null);

    // Free trial check (members and the site owner are never limited)
    let access = { ok: true, full: true };
    try { access = await useScriptureLookup(item._id); } catch (e) { access = { ok: true, full: true }; }
    if (!access.ok) {
        lockReason = access.reason;
        await $w('#resultsRepeater').collapse();
        $w('#detailScripture').html = createLockedHtml(item.topicName || '', access);
        $w('#learnMoreButton').label = access.reason === 'login' ? 'Log in or sign up free' : 'About membership';
        $w('#learnMoreButton').show();
        $w('#learnMoreButton').expand();
        $w('#detailBox').show();
        await $w('#detailBox').expand();
        if (!keepAtTop) await $w('#detailBox').scrollTo();
        return;
    }
    lockReason = null;

    await $w('#resultsRepeater').collapse();
    await renderSelectedTopic();
    showEmailButton(item);
    if (!access.full && access.freeTotal) {
        $w('#detailScripture').html =
            `<p style="text-align:center; color:#596653; font-family:Georgia, serif; font-size:15px; margin:4px 0 10px 0;">Free trial: you have ${access.freeLeft} of ${access.freeTotal} free topic lookups left. Members get unlimited lookups.</p>` +
            $w('#detailScripture').html;
    }

    $w('#detailBox').show();
    await $w('#detailBox').expand();

    if (relatedItems.length) {
        $w('#resultsRepeater').data = [createRelatedHeading(item), ...relatedItems];
        await $w('#resultsRepeater').expand();
    }

    // When opened from a link (another page), keep the page at the top.
    if (!keepAtTop) await $w('#detailBox').scrollTo();
}

// "Email to Client" button (Counselors' Room page only). A small embed (#emailEmbed) holds the button,
// because Wix text links cannot carry an email body. Clicking opens the counselor's own email program
// with this topic's Scriptures filled in; the counselor adds the client's address and sends.
// Trial (Nov 19, 2026): shown only for the topics listed here. To show it on every topic, set EMAIL_ALL = true.
const EMAIL_TOPICS = ['abortion'];
const EMAIL_ALL = false;
const EMAIL_PAGE = 'https://doctorishome.github.io/belief-therapy-tool/counselors/email-client-button.html';
let emailHref = '';

function emailHrefFor(topic) {
    const name = String(topic.topicName || '');
    const niceName = name.toLowerCase().replace(/(^|[\s,/(-])([a-z])/g, (m, a, b) => a + b.toUpperCase());
    const scriptures = String(topic.scriptureContent || '').replace(/\r\n?/g, '\n').trim();
    const body =
        'Hello,\n\n' +
        'Here are the Scriptures on "' + niceName + '" that we talked about in our session.\n\n' +
        scriptures + '\n\n' +
        '(From Pearls: Scriptures to Live By, by Dr. Brian Campbell)\n';
    return 'mailto:?subject=' + encodeURIComponent('Scriptures from our session') +
        '&body=' + encodeURIComponent(body.replace(/\n/g, '\r\n'));
}

function showEmailButton(topic) {
    try {
        const box = $w('#emailEmbed');
        const ok = topic && (EMAIL_ALL || EMAIL_TOPICS.includes(normalizeText(topic.topicName)));
        if (!ok) { emailHref = ''; box.collapse(); return; }
        emailHref = emailHrefFor(topic);
        if (box.src !== EMAIL_PAGE) box.src = EMAIL_PAGE;
        box.expand();
        box.postMessage({ type: 'emailData', href: emailHref });
        setTimeout(() => { try { box.postMessage({ type: 'emailData', href: emailHref }); } catch (e) {} }, 1500);
    } catch (e) {
        // The email embed is not on this page
    }
}

async function renderSelectedTopic() {
    if (!selectedTopic) return;

    const topicName = selectedTopic.topicName || '';
    const scripture = selectedTopic.scriptureContent || '';
    const synopsis = getSynopsis(selectedTopic);
    const synopsisText = normalizeSynopsisParagraphs(synopsis);
    const counsel = await resolveGodlyCounselChapter(selectedTopic.godlyCounselChapter);

    $w('#detailScripture').html = createDetailHtml(
        selectedTopic._id,
        topicName,
        scripture,
        synopsisText,
        counsel
    );

    $w('#learnMoreButton').label = 'Back to Topics';
    $w('#learnMoreButton').show();
    $w('#learnMoreButton').expand();
}

async function resolveGodlyCounselChapter(reference) {
    if (!reference) return null;

    let chapter = reference;
    if (typeof chapter === 'string') {
        try {
            chapter = await wixData.get('GodlyCounselChapters', chapter);
        } catch (error) {
            console.error('Unable to load Godly Counsel chapter:', error);
            return null;
        }
    }

    if (!chapter) return null;

    const pdfUrl = getDocumentUrl(chapter.pdfFile);
    if (!pdfUrl) return null;

    return {
        chapterNumber: chapter.chapterNumber || '',
        chapterTitle: chapter.chapterTitle || '',
        pageRange: chapter.pageRange || '',
        pdfUrl
    };
}

function getDocumentUrl(documentValue) {
    if (!documentValue) return '';
    if (typeof documentValue === 'string') return documentValue;
    return documentValue.url || documentValue.fileUrl || '';
}

async function returnToTopics() {
    selectedTopic = null;
    try { wixLocationFrontend.queryParams.remove(['topic']); } catch (e) {}
    await $w('#detailBox').collapse();
    $w('#searchInput').value = '';
    $w('#resultsRepeater').data = allTopics;
    await $w('#resultsRepeater').expand();
    await $w('#searchInput').scrollTo();
}

function createDetailHtml(topicId, topicName, scripture, synopsis, counsel) {
    const scriptureHtml = formatText(scripture);
    const synopsisParts = separateCounselReference(synopsis);
    const synopsisHtml = formatSynopsisText(synopsisParts.text);

    const sections = [
        `<div style="text-align:center; color:#2D2A26; font-family:Georgia, serif; font-size:26px; font-weight:700; letter-spacing:0.4px; margin:24px 0 20px 0; padding-bottom:12px; border-bottom:2px solid #B08A4B;">${escapeHtml(topicName)}</div>`,
        `<div style="text-align:left; color:#2D2A26; background-color:#F3E9D2 !important; border-left:4px solid #71806A; padding:20px 10px 20px 24px; font-size:17px; line-height:1.65;">${scriptureHtml}</div>`
    ];

    if (synopsisParts.reference || synopsisHtml) {
        sections.push(
            '<div style="text-align:center; color:#596653; font-family:Georgia, serif; font-size:23px; font-weight:700; margin-top:28px; margin-bottom:7px;">Synopsis</div>'
        );

        if (synopsisParts.reference) {
            sections.push(
                `<p style="text-align:center; color:#796E5E; font-size:13px; margin:0 0 15px 0;">(${formatCounselReferenceHtml(synopsisParts.reference)})</p>`
            );
        }

        if (synopsisHtml) {
            sections.push(`<div style="text-align:left; color:#2D2A26; background-color:#F3E9D2 !important; border-left:4px solid #A99B84; padding:20px 10px 20px 24px; font-size:17px; line-height:1.65;">${synopsisHtml}</div>`);
        }
    }

    if (topicId) {
        const hasSynopsis = Boolean(synopsisParts.reference || synopsisParts.text);
        sections.push(createPrintLinksHtml(topicId, hasSynopsis, counsel));
    }

    return `<div style="background-color:#FAF4E6 !important; border:3px solid #665A49; border-radius:10px; box-shadow:0 5px 18px rgba(45,42,38,0.22); padding:10px 18px 16px 18px;">${sections.join('')}</div>`;
}

function createLockedHtml(topicName, access) {
    const total = access.freeTotal || 5;
    const title = `<div style="text-align:center; color:#2D2A26; font-family:Georgia, serif; font-size:26px; font-weight:700; margin:24px 0 16px 0; padding-bottom:12px; border-bottom:2px solid #B08A4B;">${escapeHtml(topicName)}</div>`;
    const text = access.reason === 'login'
        ? `Please log in or sign up (free) to read the Scriptures for this topic. You get ${total} free topic lookups. Members get unlimited lookup of 2,500 counseling Scriptures, indexed in 170 topics.`
        : `You have used your ${total} free topic lookups. Become a member for unlimited lookup of 2,500 counseling Scriptures, indexed in 170 topics.`;
    return `<div style="background-color:#FAF4E6 !important; border:3px solid #665A49; border-radius:10px; padding:10px 18px 18px 18px;">${title}<p style="text-align:center; color:#2D2A26; font-family:Georgia, serif; font-size:18px; line-height:1.6; margin:0 8px;">${escapeHtml(text)}</p></div>`;
}

function matchesSearch(item, query) {
    const normalizedQuery = normalizeText(query);
    const topicName = normalizeText(item.topicName);
    const keywords = Array.isArray(item.searchKeywords) ? item.searchKeywords : [];

    return topicName.startsWith(normalizedQuery) ||
        keywords.some((keyword) => normalizeText(keyword) === normalizedQuery);
}

function normalizeText(value) {
    return String(value || '')
        .trim()
        .toLowerCase()
        .replace(/[^a-z0-9]+/g, ' ')
        .replace(/\s+/g, ' ')
        .trim();
}

function createRelatedHeading(topic) {
    return {
        _id: `related-heading-${topic._id}`,
        _isRelatedHeading: true,
        topicName: 'See also:'
    };
}

function getRelatedTopicItems(relatedTopics) {
    const names = Array.isArray(relatedTopics)
        ? relatedTopics
        : String(relatedTopics || '')
            .split(/[;\n]+/)
            .map((topic) => topic.trim())
            .filter(Boolean);

    return names
        .map((name) => allTopics.find((item) =>
                    normalizeText(item.topicName) === normalizeText(name)

        ))
        .filter(Boolean);
}

function createPrintLinksHtml(topicId, hasSynopsis, counsel) {
    const separator = '<span style="margin:0 10px; color:#8D8D8D;">|</span>';
    const linkStyle = 'color:#2D2A26; font-size:20px; line-height:1.6; font-weight:700; text-decoration:underline; cursor:pointer;';
    // Topics that use the new built-in print page (instead of the old PDF files)
    // All topics now use the new built-in print pages (the old PDF files are no longer linked)
    const useNewPrint = true;
    const printBase = `${wixLocationFrontend.baseUrl}/${(wixLocationFrontend.path || []).join('/')}`;
    const scripturePdfUrl = useNewPrint
        ? `${printBase}?print=scriptures&id=${encodeURIComponent(topicId)}`
        : (selectedTopic?.scripturePdfUrl || '');
    const synopsisPdfUrl = useNewPrint
        ? `${printBase}?print=synopsis&id=${encodeURIComponent(topicId)}`
        : (selectedTopic?.synopsisPdfUrl || '');

    // New print pages open in the same tab (with a 'Back to topic' button); old PDFs open in a new tab
    const printTarget = useNewPrint ? '_self' : '_blank';

    const scriptureLink = scripturePdfUrl
        ? `<a href="${escapeHtml(scripturePdfUrl)}" target="${printTarget}" style="${linkStyle}">Print Scriptures</a>`
        : '';

    const synopsisLink = hasSynopsis && synopsisPdfUrl
        ? `${separator}<a href="${escapeHtml(synopsisPdfUrl)}" target="${printTarget}" style="${linkStyle}">Print Synopsis</a>`
        : '';

    const counselLink = counsel
        ? `${separator}<a href="${escapeHtml(counsel.pdfUrl)}" target="_blank" style="${linkStyle}">${createGodlyCounselLabel(counsel)}</a>`
        : '';

    return `<p style="text-align:center; margin:24px 0 10px 0;">${scriptureLink}${synopsisLink}${counselLink}</p>`;
}

async function handleEmbeddedPrintRequest() {
    const query = wixLocationFrontend.query || {};
    const part = query.print;
    const topicId = query.id;

    if (!topicId || !['scriptures', 'synopsis'].includes(part)) {
        return false;
    }

    // Print view: hide the intro and the search area right away so only the print page shows
    try { $w('#section6').collapse(); } catch (e) {}
    try { $w('#section4').collapse(); } catch (e) {}

    try {
        const item = await wixData.get('PearlsTopics', topicId);

        printItem = item;
        const synopsisParts = separateCounselReference(getSynopsis(item));

        const message = part === 'scriptures'
            ? {
                type: 'printPearls',
                topicName: item.topicName || 'Pearls Topic',
                heading: 'Scriptures',
                reference: '',
                content: item.scriptureContent || ''
            }
            : {
                type: 'printPearls',
                topicName: item.topicName || 'Pearls Topic',
                heading: 'Synopsis',
                reference: synopsisParts.reference || '',
                // Same paragraph clean-up as the on-screen synopsis
                content: normalizeSynopsisParagraphs(synopsisParts.text || '')
            };

        try { await $w('#html1').expand(); } catch (e) {}
        await new Promise((resolve) => setTimeout(resolve, 1000));
        $w('#html1').postMessage(message);
        try { await $w('#html1').scrollTo(); } catch (e) {}

        return true;
    } catch (error) {
        console.error('Unable to prepare embedded print view:', error);
        try { $w('#section6').expand(); $w('#section4').expand(); } catch (e) {}
        return false;
    }
}

// Leaves the print view and shows the full topic (Scriptures + Synopsis) on the same page
async function returnFromPrintView(item) {
    printItem = null;
    try { wixLocationFrontend.queryParams.remove(['print', 'id']); } catch (e) {}
    $w('#html1').collapse();
    await $w('#section6').expand();
    await $w('#section4').expand();
    try { $w('#html2').collapse(); } catch (e) {}
    const fullItem = allTopics.find((topic) => topic._id === item._id) || item;
    await openTopic(fullItem);
}

function createGodlyCounselLabel(counsel) {
    const chapter = counsel.chapterNumber ? `Chapter ${escapeHtml(counsel.chapterNumber)}: ` : '';
    const title = escapeHtml(counsel.chapterTitle || '');
    const pages = counsel.pageRange ? `, ${escapeHtml(counsel.pageRange)}` : '';
    return `Print Godly Counsel: ${chapter}${title}${pages}`;
}

function separateCounselReference(synopsis) {
    const value = String(synopsis || '').trim();
    const match = value.match(/^(Godly Counsel:\s*pp\.\s*[^.]+\.)\s*/i);

    if (!match) return { reference: '', text: value };

    return {
        reference: match[1],
        text: value.slice(match[0].length).trim()
    };
}

function formatCounselReferenceHtml(reference) {
    return escapeHtml(reference).replace(/^Godly Counsel/i, '<em>Godly Counsel</em>');
}

function formatText(value) {
    return escapeHtml(value || '').replace(/\r?\n/g, '<br>');
}

function formatSynopsisText(value) {
    return formatText(value)
        .replace(/(?:<br>\s*)*•\s*/g, '<br><br>• ')
        .replace(/(^|<br><br>)((?:(?!<br>).){2,60}:)/g, '$1<strong>$2</strong>')
        .replace(
            /God(?:’|')s Guidance\s*(?:<br>\s*)*/gi,
            '<div style="text-align:center; color:#596653; font-family:Georgia, serif; font-size:23px; font-weight:700; margin:28px 0 14px 0; padding-top:4px;">God’s Guidance</div>'
        );
}

function getSynopsis(item) {
    if (!item || !item.godlyCounselSynopsis) return '';

    const synopsis = String(item.godlyCounselSynopsis).trim();
    if (/^Godly Counsel:/i.test(synopsis)) return synopsis;

    return synopsis.replace(
        /^pp\.\s*([^:\n]+):\s*/i,
        (_match, pages) => `Godly Counsel: pp. ${pages.trim()}. `
    );
}

function normalizeSynopsisParagraphs(value) {
    const blocks = String(value || '')
        .replace(/\r\n?/g, '\n')
        .split(/\n{2,}/)
        .map((block) => block.replace(/\n+/g, ' ').replace(/\s+/g, ' ').trim())
        .filter(Boolean);

    const paragraphs = [];

    blocks.forEach((block) => {
        const previous = paragraphs[paragraphs.length - 1];
        const startsStructuredBlock = /^•/.test(block) || /^God’s Guidance$/i.test(block);
        const previousIsStructuredBlock = previous && (
            previous.includes('•') || /^God’s Guidance$/i.test(previous)
        );

        if (
            previous &&
            !startsStructuredBlock &&
            !previousIsStructuredBlock &&
            !/[.!?][\"')\]”’]*$/.test(previous)
        ) {
            paragraphs[paragraphs.length - 1] = `${previous} ${block}`;
        } else {
            paragraphs.push(block);
        }
    });

    return paragraphs.flatMap(splitLongParagraph).join('\n\n');
}

// Some synopses were saved as one long block with no paragraph breaks.
// Break very long blocks into readable paragraphs at sentence boundaries,
// preferring sentences that start with a transition word (e.g. "In addition", "Finally").
const TRANSITION_START = /^(In addition|Additionally|Also|Furthermore|Moreover|However|Finally|Instead|In the final analysis|In summary|In conclusion|Therefore|Fortunately|Unfortunately|On the other hand|For example|Similarly|Likewise|As Christians|God|Jesus|The Bible|Scripture)/;

function splitLongParagraph(paragraph) {
    const text = String(paragraph || '');
    if (text.length < 700 || /^•/.test(text) || /^God’s Guidance$/i.test(text)) return [text];

    const sentences = text.match(/[^.!?]+[.!?]+[”"’)\]]*\s*/g);
    if (!sentences || sentences.join('').length < text.length - 5) return [text];

    const result = [];
    let current = '';
    sentences.forEach((sentence) => {
        const s = sentence.trim();
        const goodBreak = current.length >= 350 && TRANSITION_START.test(s);
        const mustBreak = current.length >= 650;
        if (current && (goodBreak || mustBreak)) {
            result.push(current.trim());
            current = '';
        }
        current += (current ? ' ' : '') + s;
    });
    if (current.trim()) {
        // Avoid a tiny last paragraph: join it to the previous one
        if (result.length && current.trim().length < 150) {
            result[result.length - 1] += ' ' + current.trim();
        } else {
            result.push(current.trim());
        }
    }
    return result;
}

function escapeHtml(value) {
    return String(value)
        .replace(/&/g, '&amp;')
        .replace(/</g, '&lt;')
        .replace(/>/g, '&gt;')
        .replace(/"/g, '&quot;')
        .replace(/'/g, '&#039;');
}

// Opens a topic automatically when the page address includes ?topic=...
// Examples: /scriptures?topic=anxiety-worry   or   /scriptures?topic=grief
async function openTopicFromAddress() {
    if (wixWindowFrontend.rendering.env !== 'browser') return;
    const requested = (wixLocationFrontend.query || {}).topic;
    if (!requested) return;

    const wanted = normalizeText(requested);
    if (!wanted) return;

    const match =
        allTopics.find((item) => normalizeText(item.urlSlug) === wanted) ||
        allTopics.find((item) => normalizeText(item.topicName) === wanted) ||
        allTopics.find((item) => normalizeText(item.topicName).startsWith(wanted)) ||
        allTopics.find((item) => (item.searchKeywords || []).some((keyword) => normalizeText(keyword) === wanted));

    if (match) {
        try {
            await openTopic(match, true);
        } catch (error) {
            console.error('Unable to open topic from address:', error);
        }
    }
}
