/* Relève les exercices d'écoute des 87 modules et écrit la page d'arbitrage
 * assets/presentations/exercices-ecoute.html.
 *
 *     node build/releve_ecoute.js
 *
 * La question posée par la page : dans un exercice où l'on demande « qu'est-ce
 * que tu entends ? », est-ce qu'un élève qui n'appuie jamais sur « écouter »
 * peut répondre juste en lisant l'énoncé affiché ? Quand c'est oui, l'énoncé
 * est masqué jusqu'à la correction (build/greffe_masque_ecoute.py). Quand
 * c'est non — la réponse est un son, elle n'est pas écrite — il reste.
 *
 * La page est un relevé, pas un jugement figé : chaque ligne porte son verdict
 * et de quoi le contredire.
 */
const fs = require('fs'), path = require('path'), vm = require('vm');
const RACINE = path.resolve(__dirname, '..');
const INTERACTIF = path.join(RACINE, 'assets', 'interactive');

function bloc(lignes, nom) {
  const i = lignes.findIndex(l => l.startsWith('const ' + nom + ' = ['));
  if (i < 0) return null;
  for (let j = i + 1; j < lignes.length; j++) if (lignes[j] === '];') return lignes.slice(i, j + 1).join('\n');
  return null;
}

function releve() {
  const out = [];
  for (const d of fs.readdirSync(INTERACTIF).sort()) {
    if (!d.startsWith('module-')) continue;
    const dir = path.join(INTERACTIF, d);
    const fichiers = fs.readdirSync(dir).filter(x => x.endsWith('.html'));
    const f = fichiers.find(x => x.includes('activite-interactive')) || fichiers[0];
    if (!f) continue;
    const lignes = fs.readFileSync(path.join(dir, f), 'utf8').split('\n');
    const bE = bloc(lignes, 'EXOS');
    if (!bE) continue;
    const bFC = bloc(lignes, 'FC_CARDS');
    let exos;
    try {
      const ctx = {}; vm.createContext(ctx);
      vm.runInContext((bFC ? bFC.replace(/^const /, 'var ') : 'var FC_CARDS=[];') + '\n'
        + bE.replace(/^const /, 'var ') + '\nEXOS;', ctx);
      exos = ctx.EXOS;
    } catch (e) { console.error('  !! ' + d + ' — ' + e.message); continue; }
    for (const ex of exos) {
      if (!ex || !ex.listen) continue;
      out.push({ slug: d, id: ex.id, sec: ex.sec, num: ex.num, tit: ex.tit,
        tiles: ex.tiles || [], sub: ex.sub || '',
        rows: (ex.rows || []).map(r => ({ txt: String(r.txt), ok: r.ok })) });
    }
  }
  return out;
}

// Les exercices masqués : la même table que la greffe, lue chez elle pour
// qu'un ajout là-bas ne laisse pas cette page en arrière.
function cibles() {
  const py = fs.readFileSync(path.join(RACINE, 'build', 'greffe_masque_ecoute.py'), 'utf8');
  const dedans = py.slice(py.indexOf('CIBLES = {'), py.indexOf('\n}\n', py.indexOf('CIBLES = {')));
  const par = {};
  let slug = null;
  for (const l of dedans.split('\n')) {
    const m = /'(module-[a-z0-9-]+)':/.exec(l);
    if (m) { slug = m[1]; par[slug] = par[slug] || []; }
    if (slug) for (const q of l.matchAll(/'([a-zA-Z][a-zA-Z0-9]*)'/g)) if (!q[1].startsWith('module')) par[slug].push(q[1]);
  }
  return par;
}

// Les sept exercices d'intention : la voix porte la réponse, mais la réplique
// écrite la porte peut-être aussi. À trancher par une oreille, pas par un
// script — d'où leur section à part.
const A_TRANCHER = [
  ['module-n7-achat', 'prProso'], ['module-n7-logement', 'prTon'],
  ['module-n8-actualite', 'prInto'], ['module-n8-emmenagement', 'prInto'],
  ['module-n8-habitation', 'prInto'], ['module-n8-oeuvres', 'prInto'],
  ['module-n8-recherche', 'prInto'],
];

const esc = s => String(s).replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;');
const net = s => String(s).replace(/<[^>]+>/g, '');
const niveau = slug => { const m = /^module-n(\d)-/.exec(slug); return m ? 'Niveau ' + m[1] : 'Niveau 4'; };

function carte(e, verdict) {
  const ex = e.rows.slice(0, 3).map(r =>
    '<li><span class="dit">' + esc(net(r.txt)) + '</span> <span class="fl">→</span> <b>' + esc(r.ok) + '</b></li>').join('');
  return '<article class="ex ' + verdict + '">'
    + '<div class="ex-tete"><span class="niv">' + niveau(e.slug) + '</span>'
    + '<code>' + esc(e.slug.replace('module-', '')) + '</code>'
    + '<span class="num">' + esc(e.num) + '</span></div>'
    + '<h3>' + esc(e.tit) + '</h3>'
    + '<p class="tuiles">' + e.tiles.map(t => '<span>' + esc(t) + '</span>').join('') + '</p>'
    + '<ul class="lignes">' + ex + '</ul>'
    + '</article>';
}

function page(tous, masques, atrancher, gardes) {
  const styleSource = fs.readFileSync(path.join(RACINE, 'assets', 'presentations', 'audio-manquant.html'), 'utf8');
  const style = styleSource.slice(styleSource.indexOf('<style>'), styleSource.indexOf('</style>') + 8);
  const familles = {};
  gardes.forEach(e => {
    const f = /lettres|COMME K/i.test(e.tit + e.tiles.join('')) ? 'Les lettres et le son qu’elles font'
      : /« e »|e se dit|e qu|e tient|e que tu/i.test(e.tit) ? 'Le « e » qui tombe'
      : /liaison|\[t\]/i.test(e.tit) ? 'La liaison'
      : /registre|façons de le dire|se dit/i.test(e.tit) ? 'Le registre'
      : 'Deux sons qui se ressemblent';
    (familles[f] = familles[f] || []).push(e);
  });
  return `<!DOCTYPE html>
<html lang="fr">
<head>
<meta charset="utf-8" />
<meta name="viewport" content="width=device-width, initial-scale=1.0" />
<title>Les exercices d'écoute et leur énoncé</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Newsreader:ital,opsz,wght@0,6..72,400;0,6..72,500;0,6..72,600&family=Nunito:ital,wght@0,400;0,600;0,700;0,800&display=swap">
${style}
<style>
.grille{display:grid;gap:14px;margin:22px 0 0}
@media(min-width:720px){.grille{grid-template-columns:1fr 1fr}}
.ex{background:var(--card);border:1px solid var(--line);border-left:4px solid var(--line-fort);
  border-radius:12px;padding:16px 18px}
.ex.masque{border-left-color:var(--trou)} .ex.garde{border-left-color:var(--ok)}
.ex.trancher{border-left-color:var(--part)}
.ex-tete{display:flex;gap:10px;align-items:center;flex-wrap:wrap;font-size:12px;margin-bottom:6px}
.ex-tete code{font-family:var(--mono);font-size:12px;color:var(--muted)}
.niv{font-weight:800;letter-spacing:.06em;text-transform:uppercase;font-size:11px;color:var(--acier)}
.num{color:var(--muted)}
.ex h3{font-family:Newsreader,Georgia,serif;font-size:19px;font-weight:600;color:var(--ink);margin:0 0 8px}
.tuiles{display:flex;gap:6px;flex-wrap:wrap;margin:0 0 10px}
.tuiles span{font-size:11px;font-weight:800;letter-spacing:.04em;background:var(--sunken);
  border:1px solid var(--line);border-radius:99px;padding:3px 9px;color:var(--body)}
.lignes{list-style:none;margin:0;padding:0;font-size:14px}
.lignes li{padding:3px 0;border-top:1px solid var(--line)}
.lignes li:first-child{border-top:0}
.dit{color:var(--body)} .fl{color:var(--muted);padding:0 4px}
.masque .dit{text-decoration:line-through;text-decoration-color:var(--trou);color:var(--muted)}
.chiffres{display:flex;gap:26px;flex-wrap:wrap;margin:26px 0 0;padding:18px 20px;
  background:var(--card);border:1px solid var(--line);border-radius:12px}
.chiffre b{display:block;font-family:Newsreader,Georgia,serif;font-size:34px;font-weight:500;
  color:var(--ink);line-height:1}
.chiffre span{font-size:13px;color:var(--muted)}
.bloc{margin:56px 0 0}
.bloc>p{margin:8px 0 0}
h4{font-size:13px;font-weight:800;letter-spacing:.08em;text-transform:uppercase;
  color:var(--muted);margin:30px 0 0}
</style>
</head>
<body>
<div class="doc">
  <p class="eyebrow">Relevé · 30 août 2026</p>
  <h1>Les exercices d'écoute et leur énoncé</h1>
  <p class="chapeau">Dans « Sur, dans ou à ? » — module 1 du niveau 5 — on fait écouter
  <i>« Les clés sont sur le comptoir »</i> et on demande quelle préposition on a entendue.
  La phrase était écrite sous le bouton, préposition comprise. <strong>L'élève lisait et
  répondait sans jamais écouter.</strong> Voici les cent exercices d'écoute des
  quatre-vingt-sept modules, passés au même test.</p>

  <div class="chiffres">
    <div class="chiffre"><b>${tous.length}</b><span>exercices d'écoute</span></div>
    <div class="chiffre"><b>${masques.length}</b><span>énoncé masqué</span></div>
    <div class="chiffre"><b>${atrancher.length}</b><span>à trancher</span></div>
    <div class="chiffre"><b>${gardes.length}</b><span>énoncé gardé</span></div>
  </div>

  <div class="bloc">
    <h2>Le test</h2>
    <p><strong>Un élève qui n'appuie jamais sur « écouter » peut-il répondre juste en
    lisant ?</strong> Si oui, l'énoncé est masqué — remplacé par « Phrase 3 », « Mot 5 » —
    et il <strong>revient dès la correction</strong> : il faut voir ce qu'on vient
    d'entendre pour apprendre quelque chose de son erreur. Le bouton d'écoute, lui, ne
    change pas. Si non — la réponse est un son, elle n'est écrite nulle part — l'énoncé
    reste : le mot écrit est alors le point de départ de l'exercice, pas son indice.</p>
  </div>

  <div class="bloc">
    <h2>Masqués</h2>
    <p>La réponse se lisait dans l'énoncé : une préposition, un nombre, un point
    d'interrogation, le mot « dollars », un <i>e</i> final de féminin, ou simplement qui
    parle. <b>${masques.length} exercices, ${new Set(masques.map(e => e.slug)).size} modules.</b></p>
    <div class="grille">${masques.map(e => carte(e, 'masque')).join('')}</div>
  </div>

  <div class="bloc">
    <h2>À trancher</h2>
    <p>Ceux-là demandent <i>ce que la voix ajoute aux mots</i> : surprise, déception,
    volonté. La consigne dit que les mots seuls ne suffisent pas — mais les répliques
    proposées sont si différentes qu'on les classe sans doute à la lecture.
    <strong>Masquer suppose que les MP3 portent vraiment l'intention</strong> ; si ce
    n'est pas le cas, l'exercice devient impossible. Cela se juge à l'oreille, pas au
    script. <b>${atrancher.length} exercices.</b></p>
    <div class="grille">${atrancher.map(e => carte(e, 'trancher')).join('')}</div>
  </div>

  <div class="bloc">
    <h2>Gardés</h2>
    <p>Ici le mot écrit est le sujet de la leçon : on regarde une orthographe et on
    dit quel son elle fait. La réponse — un son, une famille de lettres, une liaison —
    n'est pas dans le texte. Le cacher ne retirerait pas un indice : il retirerait
    l'exercice. <b>${gardes.length} exercices.</b></p>
    ${Object.keys(familles).sort().map(f =>
      '<h4>' + esc(f) + ' · ' + familles[f].length + '</h4><div class="grille">'
      + familles[f].map(e => carte(e, 'garde')).join('') + '</div>').join('')}
  </div>

  <div class="bloc">
    <h2>Où c'est écrit</h2>
    <p><b>build/greffe_masque_ecoute.py</b> porte la liste des exercices masqués et la
    pose sur les fichiers déjà produits. Le gabarit reconnaît <code>masque:true</code> sur
    un exercice, et les <code>build/contenu/&lt;slug&gt;/exos.js</code> visés le portent :
    un module reconstruit masque donc tout seul. Cette page se régénère par
    <b>node build/releve_ecoute.js</b>.</p>
  </div>
</div>
</body>
</html>
`;
}

const tous = releve();
const CIB = cibles();
const estMasque = e => (CIB[e.slug] || []).includes(e.id);
const estATrancher = e => A_TRANCHER.some(([s, i]) => s === e.slug && i === e.id);
const masques = tous.filter(estMasque);
const atrancher = tous.filter(e => !estMasque(e) && estATrancher(e));
const gardes = tous.filter(e => !estMasque(e) && !estATrancher(e));
const sortie = path.join(RACINE, 'assets', 'presentations', 'exercices-ecoute.html');
fs.writeFileSync(sortie, page(tous, masques, atrancher, gardes));
console.log(tous.length + ' exercices d\'écoute — ' + masques.length + ' masqués, '
  + atrancher.length + ' à trancher, ' + gardes.length + ' gardés');
console.log('→ ' + path.relative(RACINE, sortie));
