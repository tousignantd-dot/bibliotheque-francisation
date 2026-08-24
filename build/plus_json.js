#!/usr/bin/env node
/*
 * Les mini-leçons d'un module, en JSON, d'où qu'elles viennent.
 *
 *     node build/plus_json.js module-restaurant
 *
 * Deux origines, une seule sortie. Les modules **générés** portent leurs
 * mini-leçons dans `build/contenu/<slug>/plus.js` ; les neuf modules du
 * niveau 4 écrits **avant le gabarit** les portent dans le `const PLUS = {…}`
 * de leur propre HTML. Plutôt que d'évaluer le script entier du module — qui
 * touche au DOM dès son chargement —, on découpe la constante par comptage
 * d'accolades, en sautant les accolades qui vivent dans une chaîne ou un
 * commentaire, puis on évalue ce seul littéral.
 *
 * Sert à `build/manuel_eleve.py`, qui imprime les mini-leçons dans le manuel :
 * les fiches de séance n'en portent que 54 sur 289.
 */
const fs = require('fs');
const path = require('path');

const RACINE = path.resolve(__dirname, '..');

function litteralApres(src, marque) {
  const debut = src.indexOf(marque);
  if (debut === -1) return null;
  const ouvre = src.indexOf('{', debut);
  if (ouvre === -1) return null;
  let profondeur = 0, i = ouvre;
  let chaine = null, echappe = false, commentaire = null;
  for (; i < src.length; i++) {
    const c = src[i], suivant = src[i + 1];
    if (commentaire === 'ligne') { if (c === '\n') commentaire = null; continue; }
    if (commentaire === 'bloc') { if (c === '*' && suivant === '/') { commentaire = null; i++; } continue; }
    if (chaine) {
      if (echappe) { echappe = false; continue; }
      if (c === '\\') { echappe = true; continue; }
      if (c === chaine) chaine = null;
      continue;
    }
    if (c === '/' && suivant === '/') { commentaire = 'ligne'; i++; continue; }
    if (c === '/' && suivant === '*') { commentaire = 'bloc'; i++; continue; }
    if (c === '"' || c === "'" || c === '`') { chaine = c; continue; }
    if (c === '{') profondeur++;
    else if (c === '}') { profondeur--; if (profondeur === 0) return src.slice(ouvre, i + 1); }
  }
  return null;
}

function plusDuModule(slug) {
  const genere = path.join(RACINE, 'build/contenu', slug, 'plus.js');
  if (fs.existsSync(genere)) {
    const src = fs.readFileSync(genere, 'utf8');
    return eval(src + '; PLUS');                                  // eslint-disable-line
  }
  const html = path.join(RACINE, 'assets/interactive', slug, slug + '-activite-interactive.html');
  if (!fs.existsSync(html)) throw new Error('module introuvable : ' + slug);
  const litteral = litteralApres(fs.readFileSync(html, 'utf8'), 'const PLUS');
  if (!litteral) throw new Error('aucun const PLUS dans ' + path.basename(html));
  return eval('(' + litteral + ')');                              // eslint-disable-line
}

const slug = process.argv[2];
if (!slug) { console.error('usage : node build/plus_json.js <slug>'); process.exit(2); }
process.stdout.write(JSON.stringify(plusDuModule(slug), null, 1));
