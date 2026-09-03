/* La langue d'appui du portail élève.
   ═════════════════════════════════════════════════════════════════════════
   Trois couches, à ne jamais confondre :
     1. le CONTENU à apprendre — ne bascule jamais, le traduire supprime le
        produit ;
     2. la LANGUE D'APPUI — consignes, boutons, états : c'est ce fichier ;
     3. la traduction d'un mot isolé — vit déjà dans vocab.js.

   Deux propriétés font toute la sûreté de ce module :

   · **L'appui se pose SOUS le français, jamais à sa place.** Une traduction
     fausse est donc un mauvais indice, pas une consigne perdue. C'est ce qui
     permet de livrer des fichiers non encore relus sans mettre un élève en
     difficulté.

   · **Le dictionnaire est la liste blanche.** On ne traduit que les chaînes
     qui y figurent, comparées au texte français exact. Un titre d'activité,
     un mot de vocabulaire, une phrase de dialogue n'y sont pas — il est donc
     *impossible* que la couche 1 soit touchée par accident. Ajouter une clé
     est un geste délibéré.

   La langue se lit dans `francisation-langue`, LA MÊME clé que le
   vocabulaire : un élève qui a choisi l'espagnol pour ses mots le retrouve
   ici sans le redemander.
   ═════════════════════════════════════════════════════════════════════════ */
(function (global) {
  'use strict';

  var CLE = 'francisation-langue';

  // Les langues pour lesquelles un fichier existe dans langues/portail/.
  // En ajouter une, c'est un fichier et une relecture — rien d'autre.
  var LANGUES = [
    { c: 'es', n: 'Español' },
    { c: 'en', n: 'English' },
    { c: 'uk', n: 'Українська' },
    { c: 'ar', n: 'العربية', rtl: true }
  ];

  var TABLE = null;    // {français: appui}
  var LANGUE = '';

  function lue() {
    try { return localStorage.getItem(CLE) || ''; } catch (e) { return ''; }
  }
  function ecrire(c) {
    try { localStorage.setItem(CLE, c); } catch (e) {}
  }

  function norme(s) {
    return String(s == null ? '' : s).replace(/\s+/g, ' ').trim();
  }

  function charger(code) {
    if (!code) { TABLE = null; LANGUE = ''; return Promise.resolve(); }
    return fetch('langues/portail/' + encodeURIComponent(code) + '.json')
      .then(function (r) { if (!r.ok) throw new Error('absent'); return r.json(); })
      .then(function (j) { TABLE = j.mots || {}; LANGUE = code; })
      // Fichier manquant ou illisible : on reste en français. Un portail en
      // français est un portail qui marche ; un portail à moitié traduit, non.
      .catch(function () { TABLE = null; LANGUE = ''; });
  }

  /* Le texte que l'élément porte LUI-MÊME, sans celui de ses enfants.
     La première version prenait `textContent` des seuls éléments sans enfant
     élément — et laissait donc de côté les états, écrits
     `<div><span>✓</span> Terminé</div>` : la puce est un enfant, le mot est au
     parent. En lisant les nœuds de texte directs, « Terminé » se retrouve, et
     un conteneur qui ne fait qu'emballer d'autres éléments reste ignoré : rien
     n'est posé deux fois. */
  function texteDirect(el) {
    var s = '';
    for (var n = el.firstChild; n; n = n.nextSibling) {
      if (n.nodeType === 3) s += n.nodeValue;
    }
    return norme(s);
  }

  /* Pose l'appui sous chaque texte reconnu. */
  function poser(racine) {
    var hote = racine || document;
    // Nettoyage d'abord : un rendu neuf, ou un changement de langue, ne doit
    // pas empiler deux appuis.
    var vieux = hote.querySelectorAll('.ap');
    for (var v = 0; v < vieux.length; v++) vieux[v].remove();
    if (!TABLE) return;

    var rtl = false;
    for (var i = 0; i < LANGUES.length; i++) {
      if (LANGUES[i].c === LANGUE) rtl = !!LANGUES[i].rtl;
    }

    var tous = hote.querySelectorAll('h1,h2,h3,p,span,div,button,a,label,li');
    for (var k = 0; k < tous.length; k++) {
      var el = tous[k];
      if (el.closest('[data-sans-appui]')) continue;
      var t = texteDirect(el);
      if (!t) continue;
      var trad = Object.prototype.hasOwnProperty.call(TABLE, t) ? TABLE[t] : null;
      if (!trad) continue;
      var s = document.createElement('span');
      s.className = 'ap';
      s.lang = LANGUE;
      if (rtl) s.dir = 'rtl';
      s.textContent = trad;
      el.appendChild(s);
    }

    // Ce qui n'est pas du texte visible : on double l'attribut plutôt que d'y
    // toucher, pour ne jamais faire disparaître le français.
    var champs = hote.querySelectorAll('[placeholder]');
    for (var p = 0; p < champs.length; p++) {
      var ph = norme(champs[p].getAttribute('placeholder'));
      if (TABLE[ph]) champs[p].setAttribute('title', TABLE[ph]);
    }
  }

  /* Le sélecteur. Posé dans l'élément qu'on lui donne ; « Français » en tête,
     parce que revenir au français doit être aussi facile que le quitter. */
  function selecteur(hote, apresChangement) {
    if (!hote) return null;
    var sel = document.createElement('select');
    sel.className = 'appui-sel';
    sel.id = 'appuiSel';
    sel.setAttribute('aria-label', "Langue d'appui");
    var o = document.createElement('option');
    o.value = ''; o.textContent = 'Français';
    sel.appendChild(o);
    LANGUES.forEach(function (L) {
      var x = document.createElement('option');
      x.value = L.c; x.textContent = L.n;
      sel.appendChild(x);
    });
    sel.value = lue();
    sel.addEventListener('change', function () {
      var v = sel.value;
      ecrire(v);
      // Les deux barres — connexion et accueil — portent chacune un
      // sélecteur. Changer l'un doit bouger l'autre, sinon l'élève lit deux
      // réponses différentes à la même question.
      var tous = document.querySelectorAll('.appui-sel');
      for (var i = 0; i < tous.length; i++) tous[i].value = v;
      charger(v).then(function () {
        poser(document.body);
        if (apresChangement) apresChangement();
      });
    });
    hote.appendChild(sel);
    return sel;
  }

  global.Appui = {
    demarrer: function () { return charger(lue()); },
    poser: poser,
    selecteur: selecteur,
    langue: function () { return LANGUE; }
  };
})(window);
