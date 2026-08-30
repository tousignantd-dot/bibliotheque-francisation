// Relevé des identifiants d'audio d'un module, hors navigateur.
//
//     node build/releve_sons.js module-n2-classe > manifestes/sons_module_n2_classe.json
//
// Il remplace `build/collecte_sons.py`, dont le port peut être occupé par une
// session voisine : le relevé part alors écrire dans le `manifestes/sons_<slug>.json`
// d'un autre module sans que rien ne le dise, et le script échoue en silence
// dans un `nohup`. Ici, rien n'écoute et rien ne s'écrase.
//
// Il reproduit les trois endroits du gabarit qui appellent `playWord` :
//   - le bloc `savoir` d'un exercice   → <exid>_savoir_<ri>_<wi>
//   - les exercices `vf` à cartes      → <exid>_<rowid>
//   - les mini-leçons de plus.js       → plus_<cle>_ana<i> / _lab<i>_<k> / _ex<i>_<n>
//
// Le suffixe des clés de `plus.js` est **l'indice du bloc** dans `blocs`, pas
// un compteur : `ana1` est le bloc 1, `lab4` le bloc 4. Écrit et vérifié le
// 21 août 2026 en produisant module-n2-classe, en le rejouant sur
// module-n2-bonjour : il rend ses 164 clés à l'octet près, valeurs comprises.
const fs = require('fs');
const slug = process.argv[2];
const dir = 'build/contenu/' + slug + '/';
const src = ['fccards.js','exos.js','carrier.js','plus.js'].map(f=>fs.readFileSync(dir+f,'utf8')).join('\n');
const {EXOS, PLUS, CARRIER_PHRASES, FC_CARDS} =
  new Function(src + '\n; return {EXOS, PLUS, CARRIER_PHRASES, FC_CARDS};')();
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
  // `cards && listen` était trop étroit : le gabarit pose un haut-parleur sur
  // les lignes d'un `vf` dès que `listen` est là, cartes ou pas. Un exercice
  // en liste avec `listen:true` sortait donc du relevé — boutons dans la page,
  // aucun MP3 produit, et le repli en voix de navigateur pour seule lecture.
  // Le texte est nettoyé de ses balises comme le fait le gabarit avant de lire.
  if (ex.type === 'vf' && (ex.cards || ex.listen) && ex.rows) {
    ex.rows.forEach(r => { sons[ex.id + '_' + r.id] = r.txt.replace(/<[^>]+>/g, ''); });
  }
}
for (const cle of Object.keys(PLUS)) {
  (PLUS[cle].blocs || []).forEach((b, i) => {
    if (b.t === 'ana' && b.say) sons['plus_' + cle + '_ana' + i] = b.say;
    if (b.t === 'labo' && b.out) for (const k of Object.keys(b.out)) {
      if (b.out[k].say) sons['plus_' + cle + '_lab' + i + '_' + k] = b.out[k].say;
    }
    if (b.t === 'ex' && b.rows) b.rows.forEach((r, n) => { sons['plus_' + cle + '_ex' + i + '_' + n] = r[0]; });
  });
}
process.stdout.write(JSON.stringify(sons, null, 1) + '\n');
