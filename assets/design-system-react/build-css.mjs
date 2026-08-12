// Aplatit assets/design-system/styles.css (et sa chaîne d'@import locaux)
// en un seul fichier dist/francisation.css. Aucune règle n'est réécrite :
// c'est le CSS du projet, concaténé dans l'ordre déclaré par styles.css.
// Les @import distants (Google Fonts) remontent en tête, comme l'exige CSS.
import { existsSync, mkdirSync, readFileSync, writeFileSync } from 'node:fs';
import { dirname, resolve } from 'node:path';

const CSS_ROOT = resolve('../design-system');
const ENTRY = resolve(CSS_ROOT, 'styles.css');
const remote = [];
const seen = new Set();

function flatten(file) {
  if (seen.has(file)) return '';
  seen.add(file);
  if (!existsSync(file)) throw new Error(`CSS introuvable : ${file}`);
  const css = readFileSync(file, 'utf8');
  let out = `\n/* ─── ${file.slice(CSS_ROOT.length + 1)} ─── */\n`;
  const rx = /@import\s+url\(\s*["']?([^"')]+)["']?\s*\)\s*;/g;
  let last = 0;
  for (const m of css.matchAll(rx)) {
    out += css.slice(last, m.index);
    last = m.index + m[0].length;
    const target = m[1];
    if (/^(https?:)?\/\//.test(target)) remote.push(m[0]);
    else out += flatten(resolve(dirname(file), target));
  }
  return out + css.slice(last);
}

const body = flatten(ENTRY);
mkdirSync('dist', { recursive: true });
writeFileSync('dist/francisation.css', `${[...new Set(remote)].join('\n')}\n${body}`);
console.log(`dist/francisation.css ← ${seen.size} fichiers CSS`);
