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
// Who can use it: right now only the site owner (Permissions.Admin), for testing.
// When the Counselor's Room has members, change Permissions.Admin to Permissions.SiteMember.

import { Permissions, webMethod } from 'wix-web-module';
import { fetch } from 'wix-fetch';
import { secrets } from 'wix-secrets-backend.v2';
import { elevate } from 'wix-auth';
import { httpClient, auth } from '@wix/essentials';

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
  const send = auth.elevate(httpClient.fetchWithAuth);
  const res = await send('https://www.wixapis.com/anthropic/v1/messages', {
    method: 'POST',
    headers: { 'content-type': 'application/json', 'anthropic-version': '2023-06-01' },
    body: JSON.stringify({
      model: MODELS.wix,
      max_tokens: maxTokens || 3000,
      system,
      messages: [{ role: 'user', content: user }],
    }),
  });
  const data = /** @type {any} */ (await res.json());
  if (!res.ok) { console.error('Lie Finder (Wix AI) error', res.status, JSON.stringify(data)); return null; }
  if (data.usage) console.log('Wix AI usage', JSON.stringify(data.usage));
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

export const findLies = webMethod(Permissions.Admin, async (input) => {
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

    const text = await ask(apiKey, system, user, 3000);
    if (text === null) {
      return { error: 'The search service is busy or unavailable. Please try again in a minute.' };
    }
    const result = readJson(text);
    const known = new Set(beliefs.map((b) => b.id));
    result.beliefs = (result.beliefs || []).filter((b) => known.has(b.id));
    result.levels_searched = searchLevels;
    result.levels_chosen_by_ai = chosenByAI;
    return { result };
  } catch (e) {
    console.error('Lie Finder failed', e);
    return { error: 'Something went wrong with the search. Please try again.' };
  }
});
