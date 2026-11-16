

// ===== Find Help (public AI search). Same as lie-finder/wix-code/findHelp.web.js on GitHub. =====
const FH_GITHUB = 'https://doctorishome.github.io/belief-therapy-tool/lie-finder/';
const FH_MODEL = 'claude-haiku-5-5';
const FH_CORE = 'Core False Beliefs';
const FH_LEVELS = ['Biological/Physical', 'Psychological/Cognitive', 'Interpersonal',
  'Socioeconomic', 'Sociocultural', 'Spiritual/Religious'];
const FH_HINTS = {
  'Biological/Physical': 'illness, injury, pain, the body, aging, disability, weight, sleep, medication',
  'Psychological/Cognitive': 'thinking patterns, mood, depression, anxiety, worry, trauma, abuse, addiction, grief, self-talk',
  'Interpersonal': 'parents, family, marriage, dating, friendships, church relationships, loss of a loved one, rejection',
  'Socioeconomic': 'money, debt, job loss, work, provision, retirement, feeling like a burden',
  'Sociocultural': 'culture, family heritage, community, media, race, gender roles, status, stigma',
  'Spiritual/Religious': 'God, sin, guilt, forgiveness, prayer, the church, heaven and hell, faith, suffering',
};

let fhCache = { at: 0, instructions: '', beliefs: [] };

async function fhLoad() {
  if (Date.now() - fhCache.at < 10 * 60 * 1000 && fhCache.beliefs.length) return fhCache;
  const [ins, list] = await Promise.all([
    fetch(FH_GITHUB + 'find-help-instructions.md').then((r) => r.text()),
    fetch(FH_GITHUB + 'master-list.json').then((r) => r.json()),
  ]);
  const start = ins.indexOf('## Instructions to the AI');
  // Only beliefs that already have a card are offered to the public.
  fhCache = { at: Date.now(), instructions: start >= 0 ? ins.slice(start) : ins, beliefs: list.beliefs.filter((b) => b.card) };
  return fhCache;
}

async function fhAsk(system, user, maxTokens) {
  const request = {
    method: 'POST',
    headers: { 'content-type': 'application/json', 'anthropic-version': '2023-06-01' },
    body: JSON.stringify({ model: FH_MODEL, max_tokens: maxTokens, system, messages: [{ role: 'user', content: user }] }),
  };
  const url = 'https://www.wixapis.com/anthropic/v1/messages';
  let res;
  try {
    res = await auth.elevate(httpClient.fetchWithAuth)(url, request);
  } catch (e) {
    res = await httpClient.fetchWithAuth(url, request);
  }
  const raw = await res.text();
  const data = /** @type {any} */ (JSON.parse(raw || '{}'));
  if (!res.ok) {
    console.error('Find Help (Wix AI) error', res.status, raw.slice(0, 300));
    throw new Error('AI ' + res.status);
  }
  return (data.content || []).filter((c) => c.type === 'text').map((c) => c.text).join('');
}

function fhReadJson(text) {
  const t = String(text || '');
  const a = t.indexOf('{');
  const z = t.lastIndexOf('}');
  return JSON.parse(a >= 0 ? t.slice(a, z + 1) : t);
}

async function fhPickLevels(story) {
  const system = 'A visitor to a Christian counseling website describes what they are going through. ' +
    'Pick where their struggle mostly lies. The six areas are:\n' +
    FH_LEVELS.map((l) => '- ' + l + ': ' + FH_HINTS[l]).join('\n') +
    '\nReply with the names of the 1 to 3 areas that fit best, separated by commas, and nothing else.';
  const text = await fhAsk(system, story, 100);
  const picked = FH_LEVELS.filter((l) => String(text || '').toLowerCase().includes(l.toLowerCase()));
  return picked.length ? picked.slice(0, 3) : FH_LEVELS.slice();
}

export const findHelp = webMethod(Permissions.Anyone, async (input) => {
  try {
    const story = String((input && input.story) || '').slice(0, 1500).trim();
    if (story.length < 3) return { error: 'Please write a few words about what you are going through.' };

    const { instructions, beliefs } = await fhLoad();
    const levels = await fhPickLevels(story);
    const shortList = beliefs.filter((b) => b.level === FH_CORE || levels.includes(b.level));
    const list = shortList.map((b) => [b.id, b.topic, '"' + b.belief + '"',
      b.client_words && b.client_words.length ? 'people say: ' + b.client_words.join(' / ') : ''].filter(Boolean).join(' | ')).join('\n');

    const system = instructions + '\n\n## Beliefs to choose from (use the exact ID)\n' + list;
    const text = await fhAsk(system, 'What the visitor wrote:\n' + story + '\n\nReply with the JSON only.', 1500);

    let result;
    try { result = fhReadJson(text); } catch (e) { throw new Error('unreadable answer'); }
    const byId = new Map(beliefs.map((b) => [b.id, b]));
    const cards = (result.beliefs || []).filter((b) => byId.has(b.id)).slice(0, 5).map((b) => {
      const full = byId.get(b.id);
      return { id: b.id, belief: full.belief, topic: full.topic, level: full.level, card: full.card, why: String(b.why || '').slice(0, 400) };
    });
    return { result: { crisis: !!result.crisis, real_need: String(result.real_need || ''), ask_more: String(result.ask_more || ''), cards } };
  } catch (e) {
    console.error('Find Help failed', e);
    return { error: 'The search is not available right now. Please try again in a minute, or use the word search below.' };
  }
});
