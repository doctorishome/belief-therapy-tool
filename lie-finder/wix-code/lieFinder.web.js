// Lie Finder - website backend (Wix Studio site "Pearls Working 5")
// File name in Wix:  backend/lieFinder.web.js
//
// What it does: takes the counselor's notes from the Lie Finder page, adds the search
// instructions and the master list of lies (both read from GitHub), asks Claude for the
// best-fitting lies, and sends the answer back to the page.
//
// WHICH AI: change PROVIDER below to 'claude' or 'grok'. Nothing else needs to change.
// Needs one secret in the Secrets Manager, named to match the AI you chose:
//   Claude -> ANTHROPIC_API_KEY      Grok -> XAI_API_KEY
//
// CACHING (saves about three-quarters of the cost when searches come close together):
// the instructions and the full master list are sent first and always in the same order,
// so the AI company can reuse them instead of charging full price each time.
//   Claude: marked for caching on purpose (kept 5 minutes, renewed by each search).
//   Grok: caches repeated openings automatically; a fixed conversation ID helps it match.
// The levels the counselor checks are sent with the notes (not used to shorten the list),
// so the cached part never changes.
// Who can use it: right now only the site owner (Permissions.Admin), for testing.
// When the Counselor's Room has members, change Permissions.Admin to Permissions.SiteMember.

import { Permissions, webMethod } from 'wix-web-module';
import { fetch } from 'wix-fetch';
import { secrets } from 'wix-secrets-backend.v2';
import { elevate } from 'wix-auth';

const GITHUB = 'https://doctorishome.github.io/belief-therapy-tool/lie-finder/';
const PROVIDER = 'claude';               // 'claude' or 'grok'
const MODELS = { claude: 'claude-sonnet-5-5', grok: 'grok-4.6' };
const KEY_NAMES = { claude: 'ANTHROPIC_API_KEY', grok: 'XAI_API_KEY' };
const ALL_LEVELS = ['Biological/Physical', 'Psychological/Cognitive', 'Interpersonal',
  'Socioeconomic', 'Sociocultural', 'Spiritual/Religious'];

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
  if (!res.ok) { console.error('False Belief Finder (Claude) error', res.status, JSON.stringify(data)); return null; }
  if (data.usage) console.log('Claude usage', JSON.stringify(data.usage));
  return (data.content || []).filter((c) => c.type === 'text').map((c) => c.text).join('');
}

async function askGrok(apiKey, system, user) {
  const res = await fetch('https://api.x.ai/v1/chat/completions', {
    method: 'post',
    headers: {
      'content-type': 'application/json',
      authorization: 'Bearer ' + apiKey,
      'x-grok-conv-id': 'belief-counseling-false-belief-finder',
    },
    body: JSON.stringify({
      model: MODELS.grok,
      max_tokens: 3000,
      messages: [{ role: 'system', content: system }, { role: 'user', content: user }],
    }),
  });
  const data = await res.json();
  if (!res.ok) { console.error('False Belief Finder (Grok) error', res.status, JSON.stringify(data)); return null; }
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
    try {
      const raw = await elevate(secrets.getSecretValue)(KEY_NAMES[PROVIDER]);
      apiKey = typeof raw === 'string' ? raw : raw && raw.value;
    } catch (e) {
      apiKey = '';
    }
    if (!apiKey) return { error: 'The search is not set up yet (the AI key is missing).' };

    // Fixed part (cached): instructions + the whole master list, same every time.
    const system = instructions +
      '\n\n## Master list of false beliefs (choose only from these; use the exact ID and wording)\n' +
      '(Core False Beliefs are always considered. Prefer the levels the counselor checked; if none are checked, consider all levels.)\n' +
      listForPrompt(beliefs);

    // Changing part: this search's notes.
    const user =
      'Levels the counselor checked: ' + (levels.length ? levels.join(', ') : 'none checked (search all levels)') +
      '\n\nHunch: ' + (notes.hunch || '(not given)') +
      '\n\nWhat the client has experienced: ' + (notes.experiences || '(not given)') +
      '\n\nThe client’s exact words: ' + (notes.words || '(not given)') +
      '\n\nWhat the Mining Tools showed: ' + (notes.mining || '(not given)') +
      '\n\nReply with the JSON only.';

    const text = PROVIDER === 'grok'
      ? await askGrok(apiKey, system, user)
      : await askClaude(apiKey, system, user);
    if (text === null) {
      return { error: 'The search service is busy or unavailable. Please try again in a minute.' };
    }
    const result = readJson(text);
    const known = new Set(beliefs.map((b) => b.id));
    result.beliefs = (result.beliefs || []).filter((b) => known.has(b.id));
    return { result };
  } catch (e) {
    console.error('Lie Finder failed', e);
    return { error: 'Something went wrong with the search. Please try again.' };
  }
});
