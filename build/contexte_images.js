// Ce que chaque image est censée montrer, relevé dans le contenu du module.
//
//     node build/contexte_images.js            # tous les modules
//     node build/contexte_images.js module-n6-sante
//
// Une planche de contact sans contexte ne sert qu'à juger la photo. Or le vrai
// défaut d'une image de module n'est pas qu'elle soit laide : c'est qu'elle ne
// corresponde pas à la phrase que l'élève doit lui associer. « Un fauteuil à
// large accoudoir et un chariot à tiroirs » devant une photo de salle
// d'attente, l'exercice devient infaisable — et rien dans le HTML ne le dit.
//
// Le relevé remonte donc, pour chaque fichier image, l'énoncé qui la désigne :
//   - `imgmatch` : la rangée dont le `ok` porte l'id de l'image (son `txt`) ;
//   - partout ailleurs : le champ `img`/`src` d'un objet, et ce que cet objet
//     dit de plus lisible (`txt`, `q`, `tit`, `mot`, `fr`).
// Le parcours est **générique** : il descend n'importe quelle structure et
// garde le dernier titre d'exercice traversé. Un type d'exercice ajouté demain
// entre donc au relevé sans qu'on y touche.
//
// Les neuf modules d'avant la chaîne de production n'ont pas de dossier dans
// `build/contenu/` : leurs constantes sont lues dans le HTML livré, par
// équilibrage d'accolades — pas de regex sur du JavaScript, elle casserait au
// premier crochet dans une chaîne.
const fs = require('fs');
const path = require('path');

const CONTENU = 'build/contenu';
const INTERACTIF = 'assets/interactive';
// `custom.js` est écarté : il ne déclare pas de constante, il porte des
// fragments de balisage et de code, et l'évaluer casse le chargement entier.
// `fccards.js` passe en premier — `exos.js` appelle `FC_CARDS.map()` dès
// l'évaluation, et l'ordre inverse s'arrête sur « Cannot access before
// initialization ». Même piège que le relevé des sons.
const FICHIERS = ['fccards.js', 'exos.js', 'carrier.js', 'plus.js',
                  'sections.js', 'dialogues.js'];
const NOMS = ['FC_CARDS', 'EXOS', 'PLUS', 'SECTIONS', 'DIALOGUES'];

// Les champs où se lit « ce que l'image doit montrer », par ordre de finesse.
// Une carte de vocabulaire porte `word` et `def` ; une rangée d'exercice
// porte `txt` ou `q`. L'ordre va du plus précis au plus vague : c'est le
// premier trouvé qui est gardé.
const CHAMPS_TEXTE = ['txt', 'q', 'legende', 'alt', 'word', 'mot', 'fr',
                      'def', 'tit', 'nom'];

function charger(slug) {
  const dir = path.join(CONTENU, slug);
  if (fs.existsSync(dir)) {
    const src = FICHIERS
      .filter(f => fs.existsSync(path.join(dir, f)))
      .map(f => fs.readFileSync(path.join(dir, f), 'utf8'))
      .join('\n');
    const dispo = NOMS.filter(n => new RegExp('const\\s+' + n + '\\s*=').test(src));
    if (!dispo.length) return {};
    return new Function(src + '\n; return {' + dispo.join(',') + '};')();
  }
  return depuisHtml(slug);
}

/** Les modules d'avant la chaîne : leurs constantes vivent dans le HTML. */
function depuisHtml(slug) {
  const dossier = path.join(INTERACTIF, slug);
  if (!fs.existsSync(dossier)) return {};
  const html = fs.readdirSync(dossier)
    .filter(f => f.endsWith('.html'))
    .map(f => fs.readFileSync(path.join(dossier, f), 'utf8'))
    .join('\n');
  const morceaux = [];
  for (const nom of NOMS) {
    const bloc = extraire(html, nom);
    if (bloc) morceaux.push('const ' + nom + ' = ' + bloc + ';');
  }
  if (!morceaux.length) return {};
  const dispo = NOMS.filter(n => morceaux.some(m => m.startsWith('const ' + n + ' ')));
  try {
    return new Function(morceaux.join('\n') + '\n; return {' + dispo.join(',') + '};')();
  } catch (e) {
    process.stderr.write('  ' + slug + ' : ' + e.message + '\n');
    return {};
  }
}

/** Rend le littéral qui suit `const <nom> =`, par équilibrage. */
function extraire(html, nom) {
  const m = html.match(new RegExp('(?:const|let|var)\\s+' + nom + '\\s*='));
  if (!m) return null;
  let i = m.index + m[0].length;
  while (i < html.length && /\s/.test(html[i])) i++;
  const ouvre = html[i];
  const ferme = {'[': ']', '{': '}'}[ouvre];
  if (!ferme) return null;
  let prof = 0, chaine = null, echap = false;
  for (let j = i; j < html.length; j++) {
    const c = html[j];
    if (chaine) {
      if (echap) echap = false;
      else if (c === '\\') echap = true;
      else if (c === chaine) chaine = null;
      continue;
    }
    if (c === '"' || c === "'" || c === '`') { chaine = c; continue; }
    if (c === ouvre) prof++;
    else if (c === ferme && --prof === 0) return html.slice(i, j + 1);
  }
  return null;
}

/** Le premier champ de texte lisible d'un objet. */
function texteDe(obj) {
  if (!obj || typeof obj !== 'object') return '';
  for (const c of CHAMPS_TEXTE) {
    if (typeof obj[c] === 'string' && obj[c].trim()) return obj[c].trim();
  }
  return '';
}

function nomFichier(src) {
  return String(src).split('/').pop();
}

/**
 * Descend n'importe quelle structure et note, pour chaque image trouvée,
 * l'exercice traversé et l'énoncé qui la désigne.
 */
function parcourir(noeud, ctx, sortie) {
  if (Array.isArray(noeud)) {
    for (const n of noeud) parcourir(n, ctx, sortie);
    return;
  }
  if (!noeud || typeof noeud !== 'object') return;

  // Un objet qui porte `num`/`tit` est un exercice : il devient le contexte.
  if (noeud.tit || noeud.num) {
    ctx = Object.assign({}, ctx, {
      exercice: [noeud.num, noeud.tit].filter(Boolean).join(' · '),
      consigne: noeud.sub || ctx.consigne || '',
    });
  }

  // Le cas nommé : un imgmatch relie ses images à ses rangées par `ok`.
  if (Array.isArray(noeud.images) && Array.isArray(noeud.rows)) {
    for (const im of noeud.images) {
      if (!im || !im.src) continue;
      const rangee = noeud.rows.find(r => r && r.ok === im.id);
      noter(sortie, im.src, ctx, rangee ? texteDe(rangee) : '',
            rangee ? 'associer' : 'image sans rangée');
    }
  }

  // Le cas général : un objet qui porte lui-même une image.
  for (const cle of ['img', 'image', 'src', 'photo', 'vignette']) {
    const v = noeud[cle];
    if (typeof v === 'string' && /\.(jpe?g|png|webp)$/i.test(v)) {
      const detail = noeud.word && noeud.def ? noeud.word + ' — ' + noeud.def
                                              : texteDe(noeud);
      noter(sortie, v, ctx, detail, noeud.word ? 'vocabulaire' : cle);
    }
  }

  for (const k of Object.keys(noeud)) parcourir(noeud[k], ctx, sortie);
}

function noter(sortie, src, ctx, enonce, role) {
  const nom = nomFichier(src);
  const deja = sortie[nom];
  // Une image citée deux fois garde l'énoncé le plus précis, pas le dernier.
  if (deja && deja.enonce && deja.enonce.length >= (enonce || '').length) return;
  sortie[nom] = {
    module: ctx.module,
    exercice: ctx.exercice || '',
    consigne: ctx.consigne || '',
    enonce: enonce || '',
    role: role,
  };
}

function modules() {
  return fs.readdirSync(INTERACTIF)
    .filter(s => fs.existsSync(path.join(INTERACTIF, s, 'images')))
    .sort();
}

const demande = process.argv[2];
const tout = {};
for (const slug of demande ? [demande] : modules()) {
  let data;
  try {
    data = charger(slug);
  } catch (e) {
    process.stderr.write('  ' + slug + ' : ' + e.message + '\n');
    continue;
  }
  const sortie = {};
  parcourir(Object.values(data), {module: slug}, sortie);
  for (const nom of Object.keys(sortie)) tout[slug + '/' + nom] = sortie[nom];
}
process.stdout.write(JSON.stringify(tout, null, 1) + '\n');
