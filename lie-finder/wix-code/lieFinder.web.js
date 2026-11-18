// Lie Finder - website backend (Wix Studio site "Pearls Working 5")
// File name in Wix:  backend/lieFinder.web.js
//
// What it does: takes the counselor's notes from the Lie Finder page, adds the search
// instructions and the master list of lies (both read from GitHub), asks Claude for the
// best-fitting lies, and sends the answer back to the page.
//
// WHICH AI: change PROVIDER below. Nothing else needs to change.
//   'wix'    -> Claude Haiku through Wix's built-in AI (no key needed; Wix handles billing)
//   'claude' -> Claude Haiku through your own Anthropic account (secret ANTHROPIC_API_KEY)
//   'grok'   -> Grok through your own xAI account (secret XAI_API_KEY)
//
// LEVELS FIRST: only the beliefs from the levels the counselor checked (plus the Core
// False Beliefs) are sent. If no level is checked, a small first request asks the AI to
// pick the 1-3 levels that fit best. This keeps each search small and inexpensive.
//
// Who can use it (Nov 18, 2026, Brian's choice):
//   - Site owner/admin and members with an ACTIVE "Clinical Companion" plan: unlimited searches.
//   - Anyone else must first make a free website login; then they get FREE_SEARCHES searches.
//     Their count is kept in the private CMS collection "LieFinderTrials" (_id = member ID, count).
//   - Not logged in: no search; the page asks them to log in or sign up (free).

import { Permissions, webMethod } from 'wix-web-module';
import { fetch } from 'wix-fetch';
import { secrets } from 'wix-secrets-backend.v2';
import { elevate } from 'wix-auth';
import { httpClient, auth } from '@wix/essentials';
import wixData from 'wix-data';
import { currentMember } from 'wix-members-backend';
import { members } from 'wix-members.v2';
import { orders } from 'wix-pricing-plans.v2';

const PLAN_ID = 'e3d1c25e-0e6e-4ced-a2c3-32af360e23df';   // "Clinical Companion", $14.95/month
const ADMIN_ROLE_ID = '00000000-0000-0000-0000-000000000001';
const REVIEWER_PLAN_ID = '5bc05d5f-005d-49ad-88b3-91cd1de583e7';   // free hidden 2-week "Reviewer" plan (Nov 18, 2026)
const FREE_SEARCHES = 3;
const TRIALS = 'LieFinderTrials';

// Who is asking, and how many free searches they have left.
async function whoIsAsking() {
  let memberId = '';
  try {
    const cur = await members.getCurrentMember();
    const m = cur && cur.member ? cur.member : cur;
    memberId = m && m._id ? String(m._id) : '';
  } catch (e) { memberId = ''; }
  if (!memberId) return { loggedIn: false, full: false, used: 0, freeLeft: 0 };
  let full = false;
  try {
    const roles = await currentMember.getRoles();
    full = (roles || []).some((r) => r._id === ADMIN_ROLE_ID || r.title === 'Admin');
  } catch (e) { full = false; }
  if (!full) {
    try {
      const list = await orders.memberListOrders();
      full = ((list && list.orders) || []).some((o) => o && (o.planId === PLAN_ID || o.planId === REVIEWER_PLAN_ID) && (o.status === 'ACTIVE' || o.statusNew === 'ACTIVE'));
    } catch (e) { full = false; }
  }
  let used = 0;
  if (!full) {
    try {
      const item = await wixData.get(TRIALS, memberId, { suppressAuth: true });
      used = (item && Number(item.count)) || 0;
    } catch (e) { used = 0; }
  }
  return { loggedIn: true, full, memberId, used, freeLeft: full ? null : Math.max(0, FREE_SEARCHES - used) };
}

// The page asks this when it opens, to show "You have 3 free searches" (or nothing for members).
export const lieFinderAccess = webMethod(Permissions.Anyone, async () => {
  const w = await whoIsAsking();
  return { loggedIn: w.loggedIn, full: w.full, freeLeft: w.freeLeft, freeTotal: FREE_SEARCHES };
});

const GITHUB = 'https://doctorishome.github.io/belief-therapy-tool/lie-finder/';
const PROVIDER = 'wix';                  // 'wix', 'claude' or 'grok'
const MODELS = { wix: 'claude-haiku-5-5', claude: 'claude-haiku-5-5', grok: 'grok-4.6' };
const KEY_NAMES = { claude: 'ANTHROPIC_API_KEY', grok: 'XAI_API_KEY' };
const ALL_LEVELS = ['Biological/Physical', 'Psychological/Cognitive', 'Interpersonal',
  'Socioeconomic', 'Sociocultural', 'Spiritual/Religious'];
const CORE = 'Core False Beliefs';
const LEVEL_HINTS = {
  'Biological/Physical': 'illness, injury, pain, the body, aging, disability, brain chemistry, medication',
  'Psychological/Cognitive': 'thinking patterns, mood, depression, anxiety, trauma, abuse, addiction, personality patterns, self-talk',
  'Interpersonal': 'parents, family, marriage, dating, friendships, church relationships, grief and loss, work relationships',
  'Socioeconomic': 'money, debt, job loss, work and calling, class, provision, life-stage pressures',
  'Sociocultural': 'culture, family heritage, community, media, race, gender roles, politics, status, mental-health stigma',
  'Spiritual/Religious': 'God, sin, guilt, forgiveness, prayer, the church, heaven and hell, spiritual warfare, suffering',
};

let cache = { at: 0, instructions: '', beliefs: [] };

async function loadFromGitHub() {
  if (Date.now() - cache.at < 10 * 60 * 1000 && cache.beliefs.length) return cache;
  const [ins, list] = await Promise.all([
    fetch(GITHUB + 'search-instructions.md').then((r) => r.text()),
    fetch(GITHUB + 'master-list.json').then((r) => r.json()),
  ]);
  const start = ins.indexOf('## Instructions to the AI');
  cache = { at: Date.now(), instructions: start >= 0 ? ins.slice(start) : ins, beliefs: list.beliefs };
  return cache;
}

function clip(text, max) {
  return String(text || '').slice(0, max).trim();
}

function listForPrompt(beliefs) {
  return beliefs
    .map((b) => [
      b.id, b.level, b.topic, '"' + b.belief + '"',
      b.origins ? 'comes from: ' + b.origins : '',
      b.client_words && b.client_words.length ? 'clients say: ' + b.client_words.join(' / ') : '',
      b.card ? '' : 'no card yet',
    ].filter(Boolean).join(' | '))
    .join('\n');
}

function readJson(text) {
  const t = String(text || '').replace(/^```(?:json)?\s*/i, '').replace(/```\s*$/, '').trim();
  const a = t.indexOf('{');
  const z = t.lastIndexOf('}');
  return JSON.parse(a >= 0 ? t.slice(a, z + 1) : t);
}

async function askClaude(apiKey, system, user) {
  const res = await fetch('https://api.anthropic.com/v1/messages', {
    method: 'post',
    headers: { 'content-type': 'application/json', 'x-api-key': apiKey, 'anthropic-version': '2023-06-01' },
    body: JSON.stringify({
      model: MODELS.claude,
      max_tokens: 3000,
      system: [{ type: 'text', text: system, cache_control: { type: 'ephemeral' } }],
      messages: [{ role: 'user', content: user }],
    }),
  });
  const data = await res.json();
  if (!res.ok) { console.error('Lie Finder (Claude) error', res.status, JSON.stringify(data)); return null; }
  if (data.usage) console.log('Claude usage', JSON.stringify(data.usage));
  return (data.content || []).filter((c) => c.type === 'text').map((c) => c.text).join('');
}

// Claude through Wix's built-in AI. Wix signs the request; no key is needed.
async function askWix(system, user, maxTokens) {
  const request = {
    method: 'POST',
    headers: { 'content-type': 'application/json', 'anthropic-version': '2023-06-01' },
    body: JSON.stringify({
      model: MODELS.wix,
      max_tokens: maxTokens || 3000,
      system,
      messages: [{ role: 'user', content: user }],
    }),
  };
  const url = 'https://www.wixapis.com/anthropic/v1/messages';
  let res;
  try {
    res = await auth.elevate(httpClient.fetchWithAuth)(url, request);
  } catch (e) {
    console.error('Lie Finder: elevated Wix AI call failed, trying without elevation', e);
    res = await httpClient.fetchWithAuth(url, request);
  }
  const raw = await res.text();
  if (!raw) throw new Error('Wix AI sent back an empty answer (status ' + res.status + ')');
  const data = /** @type {any} */ (JSON.parse(raw));
  if (!res.ok) {
    console.error('Lie Finder (Wix AI) error', res.status, JSON.stringify(data));
    throw new Error('Wix AI answered ' + res.status + ': ' + JSON.stringify(data).slice(0, 200));
  }
  if (data.usage) console.log('Wix AI usage', JSON.stringify(data.usage));
  if (data.stop_reason === 'max_tokens') throw new Error('The AI answer was cut off before it finished');
  return (data.content || []).filter((c) => c.type === 'text').map((c) => c.text).join('');
}

async function ask(apiKey, system, user, maxTokens) {
  if (PROVIDER === 'wix') return askWix(system, user, maxTokens);
  if (PROVIDER === 'grok') return askGrok(apiKey, system, user);
  return askClaude(apiKey, system, user);
}

// First, small request: which levels fit best (used only when the counselor checked none).
async function pickLevels(apiKey, notesText) {
  const system = 'You help a Christian counselor decide where a client\'s false beliefs most likely began. ' +
    'The six levels are:\n' + ALL_LEVELS.map((l) => '- ' + l + ': ' + LEVEL_HINTS[l]).join('\n') +
    '\nReply with the names of the 1 to 3 levels that fit best, separated by commas, and nothing else.';
  const text = await ask(apiKey, system, notesText, 300);
  const picked = ALL_LEVELS.filter((l) => String(text || '').toLowerCase().includes(l.toLowerCase()));
  return picked.length ? picked.slice(0, 3) : ALL_LEVELS.slice();
}

async function askGrok(apiKey, system, user) {
  const res = await fetch('https://api.x.ai/v1/chat/completions', {
    method: 'post',
    headers: {
      'content-type': 'application/json',
      authorization: 'Bearer ' + apiKey,
      'x-grok-conv-id': 'belief-counseling-lie-finder',
    },
    body: JSON.stringify({
      model: MODELS.grok,
      max_tokens: 3000,
      messages: [{ role: 'system', content: system }, { role: 'user', content: user }],
    }),
  });
  const data = await res.json();
  if (!res.ok) { console.error('Lie Finder (Grok) error', res.status, JSON.stringify(data)); return null; }
  if (data.usage) console.log('Grok usage', JSON.stringify(data.usage));
  return (((data.choices || [])[0] || {}).message || {}).content || '';
}

export const findLies = webMethod(Permissions.Anyone, async (input) => {
  const who = await whoIsAsking();
  if (!who.loggedIn) {
    return { reason: 'login', error: 'Please log in (or sign up free) to try the Lie Finder. You get ' + FREE_SEARCHES + ' free searches.' };
  }
  if (!who.full && who.freeLeft <= 0) {
    return { reason: 'limit', error: 'You have used your ' + FREE_SEARCHES + ' free searches. Become a member for unlimited searches.' };
  }
  try {
    const levels = (Array.isArray(input && input.levels) ? input.levels : [])
      .filter((l) => ALL_LEVELS.includes(l));
    const notes = {
      hunch: clip(input && input.hunch, 1500),
      experiences: clip(input && input.experiences, 2000),
      words: clip(input && input.words, 2000),
      mining: clip(input && input.mining, 2000),
    };
    if (!notes.hunch && !notes.experiences && !notes.words) {
      return { error: 'Please fill in your hunch, the client’s experiences, or the client’s words.' };
    }

    const { instructions, beliefs } = await loadFromGitHub();
    let apiKey = '';
    if (PROVIDER !== 'wix') {
      try {
        const raw = await elevate(secrets.getSecretValue)(KEY_NAMES[PROVIDER]);
        apiKey = typeof raw === 'string' ? raw : raw && raw.value;
      } catch (e) {
        apiKey = '';
      }
      if (!apiKey) return { error: 'The search is not set up yet (the AI key is missing).' };
    }

    const notesText =
      'Hunch: ' + (notes.hunch || '(not given)') +
      '\n\nWhat the client has experienced: ' + (notes.experiences || '(not given)') +
      '\n\nThe client’s exact words: ' + (notes.words || '(not given)') +
      '\n\nWhat the Mining Tools showed: ' + (notes.mining || '(not given)');

    // Levels first: the counselor's checked levels, or the AI's pick when none are checked.
    const chosenByAI = !levels.length;
    const searchLevels = chosenByAI ? await pickLevels(apiKey, notesText) : levels;
    const shortList = beliefs.filter((b) => b.level === CORE || searchLevels.includes(b.level));

    const system = instructions +
      '\n\n## Master list of false beliefs (choose only from these; use the exact ID and wording)\n' +
      '(This list holds the Core False Beliefs plus the levels being searched: ' + searchLevels.join(', ') + '.)\n' +
      listForPrompt(shortList);

    const user =
      'Levels being searched: ' + searchLevels.join(', ') + (chosenByAI ? ' (chosen by the AI; the counselor checked none)' : ' (checked by the counselor)') +
      '\n\nHunch: ' + (notes.hunch || '(not given)') +
      '\n\nWhat the client has experienced: ' + (notes.experiences || '(not given)') +
      '\n\nThe client’s exact words: ' + (notes.words || '(not given)') +
      '\n\nWhat the Mining Tools showed: ' + (notes.mining || '(not given)') +
      '\n\nReply with the JSON only.';

    const text = await ask(apiKey, system, user, 8000);
    if (text === null) {
      return { error: 'The search service is busy or unavailable. Please try again in a minute.' };
    }
    let result;
    try {
      result = readJson(text);
    } catch (e) {
      console.error('Lie Finder: answer was not readable', String(text).slice(0, 500));
      throw new Error('The AI answer could not be read (' + String(text || '').length + ' characters)');
    }
    const known = new Set(beliefs.map((b) => b.id));
    result.beliefs = (result.beliefs || []).filter((b) => known.has(b.id));
    result.levels_searched = searchLevels;
    result.levels_chosen_by_ai = chosenByAI;
    let freeLeft = null;
    if (!who.full) {
      // Count this free search (only searches that returned results are counted).
      try {
        await wixData.save(TRIALS, { _id: who.memberId, count: who.used + 1 }, { suppressAuth: true });
      } catch (e) { console.error('Lie Finder: could not save the free-search count', e); }
      freeLeft = Math.max(0, FREE_SEARCHES - who.used - 1);
    }
    return { result, freeLeft, freeTotal: FREE_SEARCHES };
  } catch (e) {
    console.error('Lie Finder failed', e);
    return { error: 'Something went wrong with the search. Please try again. (Detail: ' + String((e && e.message) || e).slice(0, 300) + ')' };
  }
});

// ===== Scripture Lookup free trial (Nov 18, 2026, Brian's choice) =====
// Logged-in non-members may open SCRIPTURE_FREE different topics on the Pearls Scripture Search page
// (/scriptures). Opening the same topic again does not count. Members with an active plan and the
// site owner/admins look up without limit. Topics opened are kept in the private CMS collection
// "ScriptureTrials" (_id = member ID, topics = list of topic IDs, count).
// (On the live site this section comes after the Find Help section appended to this file.)
const SCRIPTURE_FREE = 5;
const SCRIPTURE_TRIALS = 'ScriptureTrials';

async function scriptureState() {
  const w = await whoIsAsking();
  let topics = [];
  if (w.loggedIn && !w.full) {
    try {
      const it = await wixData.get(SCRIPTURE_TRIALS, w.memberId, { suppressAuth: true });
      topics = Array.isArray(it && it.topics) ? it.topics : [];
    } catch (e) { topics = []; }
  }
  return { w, topics };
}

export const scriptureAccess = webMethod(Permissions.Anyone, async () => {
  const { w, topics } = await scriptureState();
  return { loggedIn: w.loggedIn, full: w.full, freeLeft: w.full ? null : Math.max(0, SCRIPTURE_FREE - topics.length), freeTotal: SCRIPTURE_FREE };
});

export const useScriptureLookup = webMethod(Permissions.Anyone, async (topicId) => {
  topicId = String(topicId || '').slice(0, 100);
  const { w, topics } = await scriptureState();
  if (!w.loggedIn) return { ok: false, reason: 'login', freeTotal: SCRIPTURE_FREE };
  if (w.full) return { ok: true, full: true };
  if (topics.includes(topicId)) return { ok: true, freeLeft: Math.max(0, SCRIPTURE_FREE - topics.length), freeTotal: SCRIPTURE_FREE };
  if (topics.length >= SCRIPTURE_FREE) return { ok: false, reason: 'limit', freeLeft: 0, freeTotal: SCRIPTURE_FREE };
  topics.push(topicId);
  try {
    await wixData.save(SCRIPTURE_TRIALS, { _id: w.memberId, topics, count: topics.length }, { suppressAuth: true });
  } catch (e) { console.error('Scripture Lookup: could not save the free-lookup count', e); }
  return { ok: true, freeLeft: Math.max(0, SCRIPTURE_FREE - topics.length), freeTotal: SCRIPTURE_FREE };
});
