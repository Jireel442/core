const LIGATURES: Record<string, string> = { œ: 'oe', Œ: 'OE', æ: 'ae', Æ: 'AE' };

/**
 * Normalise un texte pour la comparaison : minuscules, sans accents,
 * chaque suite de caractères non-alphanumériques devient un seul espace.
 *
 * normalize('Pointe-Noire') === 'pointe noire'
 */
export function normalize(input: string): string {
  if (typeof input !== 'string') throw new TypeError('text.normalize expects a string');
  return input
    .replace(/[œŒæÆ]/g, (c) => LIGATURES[c] ?? c)
    .normalize('NFD')
    .replace(/\p{M}/gu, '')
    .toLowerCase()
    .replace(/[^a-z0-9]+/g, ' ')
    .trim();
}
export function slugify(input: string): string {
  return normalize(input).replace(/ /g, '-');
}