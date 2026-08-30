// Relevé des identifiants d'audio d'un module **écrit à la main**, depuis le
// HTML livré.
//
//     node build/releve_sons_livre.js module-logement > manifestes/sons_module_logement.json
//     node build/releve_sons_livre.js --tous          # dit ce qui manque, n'écrit rien
//
// `build/releve_sons.js` lit `build/contenu/<slug>/`. Dix modules — ceux du
// niveau 4, écrits avant le gabarit — n'en ont pas : ils n'avaient donc aucun
// `sons_<slug>.json`, et `build/audio_manquant.py` les déclarait « sans relevé
// — on ne sait pas ce qui y est attendu ». Autrement dit : personne ne pouvait
// savoir si leur audio était complet. Relevé le 28 août 2026 pendant l'audit.
//
// Il reproduit exactement les mêmes trois endroits que `releve_sons.js`, et
// tire EXOS / PLUS / CARRIER_PHRASES / FC_CARDS du HTML par découpe à crochet
// équilibré — les évaluer dans le désordre échouerait, EXOS se servant de
// FC_CARDS.
const fs = require('fs');

function bloc(h, nom) {
  const m = new RegExp('const\\s+' + nom + '\\s*=\\s*[\\[{]').exec(h);
  if (!m) return null;
  const cands = [h.indexOf('[', m.index), h.indexOf('{', m.index)].filter(x => x >= 0);
  const a = Math.min(...cands);
  const ouv = h[a], fer = ouv === '[' ? ']' : '}';
  let d = 0, b = a;
  for (; b < h.length; b++) {
    const c = h[b];
    if (c === ouv) d++; else if (c === fer) { d--; if (!d) { b++; break; } }
  }
  return h.slice(a, b);
}

function charger(slug) {
  const f = `assets/interactive/${slug}/${slug}-activite-interactive.html`;
  const h = fs.readFileSync(f, 'utf8');
  let src = '';
  for (const nom of ['FC_CARDS', 'CARRIER_PHRASES', 'EXOS', 'PLUS']) {
    const b = bloc(h, nom);
    src += `const ${nom} = ${b === null ? (nom === 'PLUS' ? '{}' : '[]') : b};\n`;
  }
  return new Function(src + '; return {EXOS, PLUS, CARRIER_PHRASES, FC_CARDS};')();
}

function relever(slug) {
  const { EXOS, PLUS, CARRIER_PHRASES } = charger(slug);
  const sons = {};
  for (const ex of EXOS) {
    if (ex.savoir && ex.savoir.speak && ex.savoir.rows) {
      ex.savoir.rows.forEach((r, ri) => {
        const mots = r[2];
        if (Array.isArray(mots)) mots.forEach((w, wi) => {
          sons[ex.id + '_savoir_' + ri + '_' + wi] = CARRIER_PHRASES[w] || w;
        });
      });
    }
    if (ex.type === 'vf' && (ex.cards || ex.listen) && ex.rows) {
      ex.rows.forEach(r => { sons[ex.id + '_' + r.id] = r.txt.replace(/<[^>]+>/g, ''); });
    }
  }
  for (const cle of Object.keys(PLUS || {})) {
    (PLUS[cle].blocs || []).forEach((b, i) => {
      if (b.t === 'ana' && b.say) sons['plus_' + cle + '_ana' + i] = b.say;
      if (b.t === 'labo' && b.out) for (const k of Object.keys(b.out)) {
        if (b.out[k].say) sons['plus_' + cle + '_lab' + i + '_' + k] = b.out[k].say;
      }
      if (b.t === 'ex' && b.rows) b.rows.forEach((r, n) => { sons['plus_' + cle + '_ex' + i + '_' + n] = r[0]; });
    });
  }
  return sons;
}

const arg = process.argv[2];
if (arg === '--tous') {
  const avecSource = new Set(fs.readdirSync('build/contenu'));
  for (const slug of fs.readdirSync('assets/interactive').filter(d => d.startsWith('module-')).sort()) {
    if (avecSource.has(slug)) continue;
    let sons; try { sons = relever(slug); } catch (e) { console.log(`  ${slug.padEnd(24)}illisible : ${e.message.slice(0, 50)}`); continue; }
    const cles = Object.keys(sons);
    const abs = cles.filter(k => !fs.existsSync(`assets/interactive/${slug}/sons/${k}.mp3`));
    console.log(`  ${slug.padEnd(24)}${String(cles.length).padStart(4)} attendus · ${String(abs.length).padStart(3)} manquants`);
    if (abs.length) abs.slice(0, 5).forEach(k => console.log('        ' + k));
  }
} else if (arg) {
  process.stdout.write(JSON.stringify(relever(arg), null, 1) + '\n');
} else {
  console.error('usage : node build/releve_sons_livre.js <slug> | --tous');
  process.exit(2);
}
