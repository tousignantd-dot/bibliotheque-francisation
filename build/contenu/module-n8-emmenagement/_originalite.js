// Le relevé de coïncidence du module 120 avec les autres contenus.
//
//     node build/contenu/module-n8-emmenagement/_originalite.js
//
// LE FILTRE EST LE POINT DÉLICAT, et deux journaux l'ont déjà payé. Ne relever
// que les chaînes à **guillemets doubles** — les fichiers de contenu écrivent
// le texte visible ainsi, précisément parce qu'il est plein d'apostrophes ; une
// regex qui accepte aussi les guillemets simples ouvre une fausse chaîne à la
// première apostrophe française et se remplit de fragments de code. Et exclure
// les chaînes qui contiennent un saut de ligne, un chevron ouvrant ou une
// interpolation : ce sont du balisage et du code, que tous les modules
// partagent forcément puisque le gabarit est commun. Sans ces trois filtres,
// la mesure surestime d'environ quatre points.
const fs = require('fs');
const path = require('path');

const SLUG = 'module-n8-emmenagement';
const DIR = path.join('build', 'contenu');
const FICHIERS = ['dialogues.js', 'fccards.js', 'sections.js', 'exos.js',
                  'plus.js', 'carrier.js', 'custom.js'];

function enonces(slug) {
  const vus = new Set();
  for (const f of FICHIERS) {
    const p = path.join(DIR, slug, f);
    if (!fs.existsSync(p)) continue;
    const src = fs.readFileSync(p, 'utf8');
    for (const m of src.matchAll(/"([^"\\\n]{12,})"/g)) {
      const s = m[1].trim();
      if (!s) continue;
      if (s.includes('<') || s.includes('${') || s.includes('/assets/')) continue;
      if (!/[a-zà-ÿ]{3}/i.test(s)) continue;   // au moins un vrai mot
      // Quatrième filtre, ajouté le 23 août 2026 : `custom.js` est du HTML
      // écrit à la main, et ses attributs (`aria-hidden=`, `autocomplete=`)
      // comme ses valeurs de style (`background:#7E3F98`, `btn btn-ghost`)
      // sont évidemment identiques d'un module à l'autre. Sans lui, la mesure
      // compte du balisage et gagne près de deux points.
      if (/[=;{}]/.test(s)) continue;
      if (/^[a-z-]+(\s+[a-z-]+)*$/.test(s) && !/\s(le|la|les|un|une|de|des|et|ou)\s/.test(s)) continue;
      if (/^[a-z-]+:/.test(s)) continue;
      if (!/\s/.test(s)) continue;             // un mot seul n'est pas un énoncé
      vus.add(s);
    }
  }
  return vus;
}

const miens = enonces(SLUG);
const autres = new Set();
let nModules = 0;
for (const slug of fs.readdirSync(DIR)) {
  if (slug === SLUG) continue;
  if (!fs.statSync(path.join(DIR, slug)).isDirectory()) continue;
  nModules++;
  for (const s of enonces(slug)) autres.add(s);
}

const communs = [...miens].filter(s => autres.has(s));
const pct = (communs.length / miens.size * 100);
console.log('%d énoncés visibles dans %s', miens.size, SLUG);
console.log('%d énoncés dans les %d autres modules', autres.size, nModules);
console.log('%d identiques, soit %s %%', communs.length, pct.toFixed(1));
console.log(pct < 5 ? '✓ sous le seuil de 5 %' : '✗ au-dessus du seuil de 5 %');
console.log('\nLes coïncidences :');
communs.sort().forEach(s => console.log('  · ' + s.slice(0, 90)));
