// Jouer chaque exercice, hors navigateur — « est-il gagnable ? »
//
//     node build/jouer.js            # les 87 modules
//     node build/jouer.js n5         # ceux dont le slug contient ça
//
// Les sept contrôles existants regardent si une réponse est ENREGISTRÉE.
// Celui-ci demande autre chose : cette réponse, soumise telle quelle, est-elle
// ACCEPTÉE par le moteur ? Ce n'est pas la même question, et c'est celle qui
// a manqué. Trois défauts trouvés le 28 août 2026 y répondaient « non » :
// `accept: []` (rien ne pouvait passer), la comparaison au caractère près
// d'une phrase de quinze mots, et le mode sans assistant qui refusait toute
// réponse ouverte. Aucun ne levait d'erreur, aucun n'apparaissait au build.
//
// Le moteur n'est pas réécrit ici : ses fonctions de décision sont EXTRAITES
// du gabarit et exécutées telles quelles. Un contrôle qui réimplémenterait la
// règle finirait par juger autre chose que ce que l'élève rencontre.
const fs = require('fs');

// ── le moteur, tel qu'il est livré ────────────────────────────────────
const gab = fs.readFileSync('build/gabarit/module.html', 'utf8');
const moteur = gab.slice(gab.indexOf('const WSTOP'), gab.indexOf('function wBoutonReponse'));
const { normCle, motsUtiles, couvre, verifCles, reponseAttendue, COUV_MIN, LONG_MIN } =
  new Function(moteur + '; return {normCle, motsUtiles, couvre, verifCles, reponseAttendue, COUV_MIN, LONG_MIN};')();
const normWrite = s => (s || '').toLowerCase().trim().normalize('NFD').replace(/[̀-ͯ]/g, '')
  .replace(/\s+/g, ' ').replace(/[.!?;:]+$/, '').replace(/^["«»']+|["«»']+$/g, '').trim();

function bloc(h, nom) {
  const m = new RegExp('const\\s+' + nom + '\\s*=\\s*[\\[{]').exec(h);
  if (!m) return null;
  const a = Math.min(...[h.indexOf('[', m.index), h.indexOf('{', m.index)].filter(x => x >= 0));
  const ouv = h[a], fer = ouv === '[' ? ']' : '}';
  let d = 0, b = a;
  for (; b < h.length; b++) { const c = h[b]; if (c === ouv) d++; else if (c === fer) { d--; if (!d) { b++; break; } } }
  return h.slice(a, b);
}
function charger(slug) {
  const h = fs.readFileSync(`assets/interactive/${slug}/${slug}-activite-interactive.html`, 'utf8');
  let src = '';
  for (const n of ['FC_CARDS', 'CARRIER_PHRASES', 'EXOS', 'SECTIONS'])
    src += `const ${n} = ${bloc(h, n) || '[]'};\n`;
  src += `const DIALOGUES = ${bloc(h, 'DIALOGUES') || '{}'};\n`;
  // `reste` sert au contrôle des noms de personnages : le nom peut vivre dans
  // le vocabulaire, une mise en situation ou un bloc custom, hors des EXOS.
  const reste = h.replace(/<script[\s\S]*?<\/script>/g, m => m.length > 60000 ? '' : m);
  return Object.assign(
    new Function(src + '; return {EXOS, SECTIONS, DIALOGUES};')(),
    { reste: reste + JSON.stringify(bloc(h, 'FC_CARDS') || '') });
}

// ── la décision du moteur pour un item écrit, reproduite par appel ────
function ecritGagnable(it) {
  if (it.cles) {
    const modele = reponseAttendue(it) || (it.accept && it.accept[0]) || '';
    if (!modele) return 'cles sans réponse modèle : impossible à éprouver';
    return verifCles(it, modele).ok ? null : 'la réponse modèle ne satisfait pas ses propres cles';
  }
  if (it.accept) {
    if (!it.accept.length) return 'accept vide : rien ne pourra être accepté';
    const m = String(it.accept[0]);
    const long = motsUtiles(m).length >= LONG_MIN;
    const ok = it.accept.map(normWrite).includes(normWrite(m))
      || (long && it.accept.some(a => couvre(String(a), m) >= COUV_MIN));
    return ok ? null : 'la réponse modèle est refusée par le moteur';
  }
  const att = reponseAttendue(it);
  if (!att) return null;                       // production libre : rien à gagner
  return couvre(att, att) >= COUV_MIN ? null : 'la réponse attendue ne se valide pas elle-même';
}

const filtre = process.argv[2];
const slugs = fs.readdirSync('assets/interactive').filter(d => d.startsWith('module-'))
  .filter(s => !filtre || s.includes(filtre)).sort();
let nMod = 0, nItems = 0, nEcarts = 0;
for (const slug of slugs) {
  let EXOS;
  try { ({ EXOS } = charger(slug)); } catch (e) { console.log(`✗ ${slug} — illisible : ${e.message.slice(0, 60)}`); nEcarts++; continue; }
  const ecarts = [];
  for (const ex of EXOS) {
    if (ex.type === 'write') for (const [i, it] of (ex.items || []).entries()) {
      nItems++;
      const m = ecritGagnable(it);
      if (m) ecarts.push(`${ex.id} item ${i + 1} : ${m}`);
    }
    if (ex.type === 'vf' && ex.tiles) for (const r of (ex.rows || [])) {
      nItems++;
      if (!ex.tiles.includes(r.ok))
        ecarts.push(`${ex.id} ligne ${r.id} : la bonne réponse « ${r.ok} » n'est pas une des tuiles`);
    }
  }

  // ── Trois motifs relevés par l'audit de contenu du 28 août 2026, ramenés
  //    ici pour qu'ils ne se reperdent pas. Chacun est mécanique : il ne
  //    demande aucun jugement, seulement de comparer le module à lui-même.

  // 1. Deux trous, une seule case. `blankify` affiche tous les `___`, mais le
  //    moteur ne crée qu'un `<input>` par item (wi_<exo>_<i>). L'élève voit
  //    deux blancs et n'a qu'un champ : l'item est injouable. 66 items dans
  //    11 modules le jour du relevé, dont 44 dans des modules que les agents
  //    n'avaient pas lus — c'est le défaut le plus répandu du cours, et ni le
  //    build ni la console ne le voyaient.
  for (const ex of EXOS) {
    if (ex.type !== 'write') continue;
    for (const [i, it] of (ex.items || []).entries()) {
      const trous = String(it.q || '').match(/_{3,}/g);
      if (trous && trous.length > 1)
        ecarts.push(`${ex.id} item ${i + 1} : ${trous.length} trous, une seule case de saisie`);
    }
  }

  // 2. L'exercice qui n'en est pas un. Quand toutes les lignes d'un `vf`
  //    portent la même bonne réponse, la tuile opposée est inatteignable :
  //    l'élève clique huit fois le même bouton et « réussit ». Trouvé dans
  //    module-activite, et le même patron copié dans deux autres modules.
  for (const ex of EXOS) {
    if (ex.type !== 'vf' || !ex.rows || ex.rows.length < 3) continue;
    const rep = new Set(ex.rows.map(r => r.ok));
    if (rep.size === 1)
      ecarts.push(`${ex.id} : les ${ex.rows.length} lignes ont la même bonne réponse « ${[...rep][0]} » — l'autre tuile est inatteignable`);
  }

  // 3. « Deux noms pour un personnage » (CLAUDETTE aux dialogues, madame Leduc
  //    partout ailleurs) N'EST PAS ici, et c'est délibéré. Deux tentatives le
  //    28 août 2026 : chercher le nom dans le HTML brut ne déclenche jamais,
  //    le HTML contenant les dialogues eux-mêmes ; le chercher dans EXOS et
  //    SECTIONS ne déclenche pas davantage sur le cas connu. Un contrôle qui
  //    ne trouve pas le défaut qu'on lui a montré donne une fausse assurance —
  //    il vaut mieux pas de contrôle. À reprendre en cherchant d'où vient la
  //    correspondance, plutôt qu'en élargissant le témoin au hasard.

  nMod++;
  if (ecarts.length) { nEcarts += ecarts.length; console.log(`✗ ${slug} — ${ecarts.length} écart(s)`); ecarts.forEach(e => console.log('    ' + e)); }
}
console.log(`\n${nMod} module(s) · ${nItems} item(s) joué(s) · ${nEcarts} écart(s)`);
process.exit(nEcarts ? 1 : 0);
