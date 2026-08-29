// Le septième contrôle : la cohérence interne d'un module, hors navigateur.
//
//     node build/coherence.js module-n3-metro
//     node build/coherence.js --tous
//
// Les six contrôles de `CLAUDE.md` regardent le module **de l'extérieur** :
// les relevés, les couleurs, les pieds de page, le sommaire. Aucun ne lit ce
// qu'il y a dedans. Or c'est là que vivent les fautes les plus coûteuses,
// parce qu'elles ne se voient qu'à l'usage — un exercice sans bonne réponse
// enregistrée, une pastille qui lit un slug au lieu d'un mot, un bloc `ana`
// muet dont on ne s'aperçoit qu'une fois les MP3 payés.
//
// Ce script a été réécrit de zéro par trois agents en trois nuits, aux
// activités 69, 80 et 81, et il a tout attrapé du premier coup les trois
// fois. Le versionner, c'est cesser de le réinventer.
//
// Il sort en code 1 dès qu'il trouve un écart, comme les six autres, de quoi
// l'enchaîner dans un `&&`.

const fs = require('fs');
const path = require('path');

const FICHIERS = ['fccards.js', 'exos.js', 'carrier.js', 'plus.js', 'sections.js'];

function charger(slug) {
  const dir = path.join('build', 'contenu', slug);
  const src = FICHIERS.map(f => {
    const p = path.join(dir, f);
    return fs.existsSync(p) ? fs.readFileSync(p, 'utf8') : '';
  }).join('\n');
  return new Function(src + `
    ; return {
        EXOS:   typeof EXOS   !== 'undefined' ? EXOS   : [],
        PLUS:   typeof PLUS   !== 'undefined' ? PLUS   : {},
        CARRIER_PHRASES: typeof CARRIER_PHRASES !== 'undefined' ? CARRIER_PHRASES : {},
        FC_CARDS: typeof FC_CARDS !== 'undefined' ? FC_CARDS : [],
        SECTIONS: typeof SECTIONS !== 'undefined' ? SECTIONS : []
      };`)();
}

function verifier(slug) {
  const ecarts = [];
  const dire = m => ecarts.push(m);
  let m;
  try {
    m = charger(slug);
  } catch (e) {
    return ['les fichiers de contenu ne s’évaluent pas : ' + e.message];
  }
  const { EXOS, PLUS, CARRIER_PHRASES, FC_CARDS, SECTIONS } = m;

  // 1. Les identifiants d'exercice sont uniques — deux exercices de même id
  //    et le second écrase le premier dans le DOM, en silence.
  const vus = new Set();
  for (const ex of EXOS) {
    if (!ex.id) dire(`un exercice sans id (« ${ex.tit || '?'} »)`);
    else if (vus.has(ex.id)) dire(`id d’exercice en double : ${ex.id}`);
    vus.add(ex.id);
  }

  // 2. Chaque exercice appartient à une section qui existe.
  const sections = new Set((SECTIONS || []).map(s => s.sec || s.id));
  if (sections.size) {
    for (const ex of EXOS) {
      if (ex.sec && !sections.has(ex.sec))
        dire(`${ex.id} : section « ${ex.sec} » absente de sections.js`);
    }
  }

  // 3. Une bonne réponse enregistrée partout où l'élève en attend une, et
  //    qui pointe vers quelque chose qui existe. C'est la faute la plus
  //    grave : l'exercice s'affiche, se joue, et ne valide jamais.
  //
  //    Chaque type a sa forme, et elles ne se ressemblent pas :
  //      vf       → {id, txt, ok}          ok est la réponse elle-même
  //      imgmatch → {id, txt, ok}          ok est l'id d'une image
  //      match    → {id, q, aid, a}        aid désigne la ligne appariée
  for (const ex of EXOS) {
    const idsLignes = new Set((ex.rows || []).map(r => r && r.id));
    const idsImages = new Set((ex.images || []).map(im => im && im.id));
    const idsSegments = new Set();
    for (const p of (ex.paras || [])) {
      for (const m of String(p).matchAll(/\[\[([A-Za-z0-9_-]+)\|/g))
        idsSegments.add(m[1]);
    }
    for (const [i, r] of (ex.rows || []).entries()) {
      const etiquette = `${ex.id} ligne ${i + 1}`;
      if (ex.type === 'vf') {
        if (r.ok === undefined || r.ok === null || r.ok === '')
          dire(`${etiquette} : réponse « ok » absente (type vf)`);
      } else if (ex.type === 'imgmatch') {
        // Le moteur lit `cv:(r.ok!==undefined ? r.ok : r.aid)` : `aid` reste
        // toléré pour module-consultation et module-probleme, d'où sort le
        // gabarit. On lit donc comme lui, sinon on accuse deux modules sains.
        const bonne = r.ok !== undefined ? r.ok : r.aid;
        if (!bonne) dire(`${etiquette} : aucune bonne réponse (imgmatch)`);
        else if (idsImages.size && !idsImages.has(bonne))
          dire(`${etiquette} : « ${bonne} » ne désigne aucune image de l’exercice`);
      } else if (ex.type === 'texte') {
        // Le type `texte` (niveaux 6 à 8) : la réponse d'une question est
        // l'identifiant d'un segment marqué `[[id|les mots]]` dans `paras`.
        // Une réponse qui ne désigne aucun segment donne une question que
        // rien ne peut valider — l'élève cherche dans le texte un passage
        // qui n'y est pas.
        if (!r.q) dire(`${etiquette} : question vide (texte)`);
        if (!r.ok) dire(`${etiquette} : aucune bonne réponse (texte)`);
        else if (!idsSegments.has(r.ok))
          dire(`${etiquette} : « ${r.ok} » ne désigne aucun passage marqué du texte`);
      } else if (ex.type === 'match') {
        if (!r.aid) dire(`${etiquette} : aucun « aid » (match)`);
        else if (!idsLignes.has(r.aid))
          dire(`${etiquette} : « aid: ${r.aid} » ne désigne aucune ligne de l’exercice`);
        if (!r.q || !r.a)
          dire(`${etiquette} : appariement incomplet (q ou a manquant)`);
      }
    }
    if (ex.type === 'texte') {
      if (!(ex.paras || []).length)
        dire(`${ex.id} : exercice « texte » sans paragraphe`);
      if (!idsSegments.size)
        dire(`${ex.id} : aucun passage marqué [[id|…]] dans le texte`);
      // Un segment que rien n'interroge est cliquable pour rien : l'élève le
      // prend pour une réponse possible et se demande à quoi il sert.
      const vises = new Set((ex.rows || []).map(r => r && r.ok));
      for (const seg of idsSegments) {
        if (!vises.has(seg))
          dire(`${ex.id} : le passage « ${seg} » est cliquable mais aucune question ne l'attend`);
      }
    }
    // Un imgmatch dont une image manque laisse une zone vide à l'écran.
    for (const img of (ex.images || [])) {
      if (!img.src) { dire(`${ex.id} : une image sans src`); continue; }
      const chemin = img.src.replace(/^\//, '');
      if (!fs.existsSync(chemin))
        dire(`${ex.id} : image absente du disque — ${chemin}`);
    }
  }

  // 3 bis. Un exercice écrit qui n'accepte rien. `accept: []` est un piège
  //    silencieux : le tableau vide est *vrai* en JavaScript, le module prend
  //    donc la branche autocorrection et compare la réponse de l'élève à une
  //    liste sans aucune entrée. Rien ne peut jamais être accepté, et la
  //    « bonne réponse » affichée est vide. Un item ouvert se laisse sans
  //    `accept` du tout (correction par l'assistant) ou reçoit des `cles`.
  //    Neuf items de module-n8-emploi étaient dans ce cas, et aucun des sept
  //    contrôles ne le voyait — relevé le 28 août 2026.
  for (const ex of EXOS) {
    if (ex.type !== 'write') continue;
    for (const [i, it] of (ex.items || []).entries()) {
      if (Array.isArray(it.accept) && it.accept.length === 0)
        dire(`${ex.id} item ${i + 1} : accept vide — rien ne pourra être accepté`);
      // Une entrée vide n'est pas toujours une faute : « Je souhaite ___
      // travailler » attend justement RIEN, et module-n6-recherche écrit
      // accept:["","rien","—"]. C'est la liste entièrement vide de texte qui
      // est fautive, pas la présence d'une entrée vide à côté des autres.
      if (Array.isArray(it.accept) && it.accept.length
          && !it.accept.some(a => typeof a === 'string' && a.trim()))
        dire(`${ex.id} item ${i + 1} : aucune réponse acceptée n’a de texte`);
      if (it.cles && !Array.isArray(it.cles))
        dire(`${ex.id} item ${i + 1} : « cles » doit être un tableau de groupes`);
      for (const [g, grp] of (Array.isArray(it.cles) ? it.cles : []).entries()) {
        const mots = Array.isArray(grp) ? grp : (grp && grp.mots);
        if (!Array.isArray(mots) || !mots.length)
          dire(`${ex.id} item ${i + 1} : groupe de cles ${g + 1} sans aucun terme`);
      }
    }
  }

  // 4. Les pastilles d'écoute : chaque mot du bloc `savoir` doit avoir sa
  //    phrase porteuse, et la clé de CARRIER_PHRASES est le **mot accentué**,
  //    jamais un slug. Douze mots de module-n3-epicerie ont lu le mot seul
  //    pendant des semaines pour cette seule raison.
  //    Le gabarit teste `ex.savoir.speak && r[2]` : un bloc sans le champ
  //    dont les rangées portent quand même une troisième colonne produit des
  //    pastilles qui n'existent pas — rien ne s'affiche, rien ne s'entend,
  //    aucune erreur. Un bloc sans troisième colonne, lui, n'a rien à dire :
  //    l'absence de `speak` y est normale et ne se signale pas.
  //
  //    Une clé de CARRIER_PHRASES **inutilisée** est normale elle aussi
  //    (CLAUDE.md le dit) : on ne la compte pas comme un écart. Le défaut
  //    grave est l'inverse — un mot à pastille sans phrase porteuse.
  for (const ex of EXOS) {
    if (!(ex.savoir && ex.savoir.rows)) continue;
    const aDesMots = ex.savoir.rows.some(r => Array.isArray(r[2]) && r[2].length);
    if (aDesMots && ex.savoir.speak !== true)
      dire(`${ex.id} : rangées à pastilles mais bloc savoir sans « speak: true » — elles ne seront jamais rendues`);
    for (const r of ex.savoir.rows) {
      for (const mot of (Array.isArray(r[2]) ? r[2] : [])) {
        if (!CARRIER_PHRASES[mot])
          dire(`pastille sans phrase porteuse : « ${mot} » (${ex.id})`);
      }
    }
  }

  // 5. Les mini-leçons : un bloc `ana` sans `say` fait lire les balises HTML
  //    à voix haute, et on ne le découvre qu'une fois les MP3 payés.
  for (const cle of Object.keys(PLUS)) {
    for (const [i, b] of (PLUS[cle].blocs || []).entries()) {
      if (b.t === 'ana' && !b.say)
        dire(`plus.${cle} bloc ${i} : « ana » sans champ « say »`);
      if (b.t === 'labo' && b.out) {
        for (const k of Object.keys(b.out))
          if (!b.out[k].say)
            dire(`plus.${cle} bloc ${i} : sortie « ${k} » sans « say »`);
      }
    }
  }

  // 6. Les mini-leçons appelées par un exercice existent bien.
  for (const ex of EXOS) {
    const cle = ex.plus || (ex.savoir && ex.savoir.plus);
    if (cle && !PLUS[cle])
      dire(`${ex.id} : renvoie à la mini-leçon « ${cle} », absente de plus.js`);
  }

  // 7. Le banc de vocabulaire : une carte qui annonce une image sans fichier
  //    laisse un trou dans « Je retiens des mots ».
  for (const c of FC_CARDS) {
    if (!c.img) continue;
    const chemin = String(c.img).replace(/^\//, '');
    if (!fs.existsSync(chemin))
      dire(`banc de vocabulaire : image absente — ${chemin}`);
  }

  return ecarts;
}

const arg = process.argv[2];
if (!arg) {
  console.error('usage : node build/coherence.js <slug> | --tous');
  process.exit(2);
}
const slugs = arg === '--tous'
  ? fs.readdirSync(path.join('build', 'contenu'))
      .filter(d => fs.existsSync(path.join('build', 'contenu', d, 'exos.js')))
      .sort()
  : [arg];

let total = 0;
for (const slug of slugs) {
  const ecarts = verifier(slug);
  total += ecarts.length;
  if (ecarts.length) {
    console.log(`✗ ${slug} — ${ecarts.length} écart(s)`);
    for (const e of ecarts) console.log('    ' + e);
  } else {
    console.log(`✓ ${slug}`);
  }
}
if (total) {
  console.log(`\n${total} écart(s) au total.`);
  process.exit(1);
}
