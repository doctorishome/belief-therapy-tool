/**
 * Brian's standing instructions. Counselors do not see or edit this text.
 * The words live in app/standing-instructions.txt so a new version can replace that one file.
 * The loaded text is cached so every live request starts with the same system message.
 */
let cached = null;

export async function loadStanding() {
  if (cached != null) return cached;
  const url = new URL("../standing-instructions.txt", import.meta.url);
  try {
    const { readFile } = await import("node:fs/promises");
    cached = await readFile(url, "utf8");
    return cached;
  } catch {
    const res = await fetch(url.href);
    if (!res.ok) throw new Error("Standing instructions could not be loaded.");
    cached = await res.text();
    return cached;
  }
}

export function standingWords(text) {
  return (String(text || "").match(/\S+/g) || []).length;
}
