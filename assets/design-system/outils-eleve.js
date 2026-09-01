/* ============================================================
   FRANCISATION · BARRE D'OUTILS ÉLÈVE
   Sept outils permanents, disponibles partout dans un module :
   traduire · lire · simplifier · prononcer · demander · carnet · réviser.

   Usage dans un module :
     Outils.init({ code: studentCode, module: 'module-probleme',
                   section: 'Défi 1 — …' });
   Les blocs traduisibles se marquent avec l'attribut data-oe dans
   le HTML ; la barre y greffe un marqueur de traduction en marge.

   Le fichier ne connaît aucun module en particulier : tout ce qui
   change d'un module à l'autre passe par init().
   ============================================================ */
(function (global) {
  'use strict';

  // Même clé et même liste que la section vocabulaire : l'élève qui a
  // déjà choisi sa langue là-bas ne la rechoisit pas ici.
  var LS_LANGUE = 'francisation-langue';
  var LANGUES = [
    { c: 'ar', n: 'arabe', loc: 'العربية', rtl: true },
    { c: 'es', n: 'espagnol', loc: 'Español' },
    { c: 'uk', n: 'ukrainien', loc: 'Українська' },
    { c: 'fa', n: 'persan', loc: 'فارسی', rtl: true },
    { c: 'zh', n: 'chinois (mandarin)', loc: '中文' },
    { c: 'pt', n: 'portugais', loc: 'Português' },
    { c: 'en', n: 'anglais', loc: 'English' },
    { c: 'ro', n: 'roumain', loc: 'Română' },
    { c: 'ur', n: 'ourdou', loc: 'اردو', rtl: true },
    { c: 'ru', n: 'russe', loc: 'Русский' },
    { c: 'ti', n: 'tigrigna', loc: 'ትግርኛ' }
  ];

  // Les tracés du système de design (grille 24, trait 2,2, bouts ronds).
  // Aucun émoji, aucun jeu d'icônes tierce partie : le poids de trait et les
  // proportions diffèrent, et le mélange se voit immédiatement.
  var TRACES = {
    trad: ['M3.5 6.5h8', 'M7.5 6.5c0 5-1.8 8-4.5 10', 'M5 11.5c1.6 3 3.9 5 6.5 6',
      'M12.5 20.5 16.5 11l4 9.5', 'M14 17.2h5'],
    lire: ['M11 5 6 9H2v6h4l5 4V5Z', 'M15.5 8.5a5 5 0 0 1 0 7', 'M18.5 5.5a9 9 0 0 1 0 13'],
    simp: ['M4 5.5h16', 'M4 10.3h12', 'M4 15.1h8', 'M4 19.9h4'],
    pron: ['M12 3.5a2.8 2.8 0 0 0-2.8 2.8v4.9a2.8 2.8 0 0 0 5.6 0V6.3A2.8 2.8 0 0 0 12 3.5Z',
      'M5.8 11.2a6.2 6.2 0 0 0 12.4 0', 'M12 17.4v3.1'],
    chat: ['M4.5 5h15v10.5h-8.6L6.5 19.5v-4H4.5Z', 'M9 10.2h.01', 'M12 10.2h.01', 'M15 10.2h.01'],
    carn: ['M8 3.5h11.5v17H8Z', 'M4.5 7.2h3.5', 'M4.5 12h3.5', 'M4.5 16.8h3.5', 'M12 8.5h4'],
    // Deux cartes empilées : celle du dessus porte sa ligne de texte.
    revi: ['M9 3.5h11.5V15H9Z', 'M15 20.5H3.5V9', 'M12.2 9.5h5.1']
  };

  // Les attributs de peinture sont portés par le <svg> lui-même : passés par
  // <defs>/<use>, ils ne survivent pas à une capture ou à un export, qui
  // repeignent des silhouettes noires pleines.
  function icone(id, taille) {
    var t = TRACES[id];
    if (!t) return '';
    return '<svg viewBox="0 0 24 24" width="' + (taille || 26) + '" height="' + (taille || 26)
      + '" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round"'
      + ' stroke-linejoin="round" aria-hidden="true" focusable="false">'
      + t.map(function (d) { return '<path d="' + d + '"/>'; }).join('') + '</svg>';
  }

  // Chevron du bouton masquer / afficher : pas un outil, donc hors de TRACES.
  function chevron(sens) {
    var d = sens === 'gauche' ? 'M15 5l-7 7 7 7' : 'M9 5l7 7-7 7';
    return '<svg viewBox="0 0 24 24" width="18" height="18" fill="none"'
      + ' stroke="currentColor" stroke-width="2.4" stroke-linecap="round"'
      + ' stroke-linejoin="round" aria-hidden="true" focusable="false">'
      + '<path d="' + d + '"/></svg>';
  }

  var OUTILS = [
    { id: 'trad', lb: 'Traduire', t: 'Traduire', s: 'Le français reste toujours visible' },
    { id: 'lire', lb: 'Lire', t: 'Lire à voix haute', s: 'Écouter le texte du module', audio: true },
    { id: 'simp', lb: 'Simplifier', t: 'Simplifier', s: 'Plus court, toujours en français' },
    { sep: true },
    { id: 'pron', lb: 'Prononcer', t: 'Prononcer', s: 'Écouter, s’enregistrer, comparer' },
    { id: 'chat', lb: 'Demander', t: 'Demander à l’assistant', s: '' },
    { id: 'carn', lb: 'Mon carnet', t: 'Mon carnet', s: 'Les mots que je garde' },
    // « Mon carnet » garde les mots que l'élève choisit ; « Réviser » travaille
    // les listes que le cours lui donne. Deux choses différentes, d'où deux
    // outils — l'un se nomme par son objet, l'autre par son action.
    { id: 'revi', lb: 'Réviser', t: 'Réviser mes mots', s: 'Les listes de mes modules' }
  ];

  var cfg = null;      // configuration passée à init()
  var el = {};         // références DOM
  var courant = null;  // outil ouvert, ou null
  var selection = '';  // dernier passage surligné, au caractère près
  var selectionBloc = '';  // le bloc entier qui le contient (voir blocDe)
  var chat = [];       // historique de l'assistant
  var audioEnCours = null;
  // Le centre de l'élève a-t-il refusé l'IA ? Posé après coup par sansIA(),
  // quand la réponse du serveur arrive — donc après bati() : tout ce qui est
  // déjà dans la page se retire, et tout ce qui repousse doit consulter ce
  // drapeau. C'est le cas de marqueBlocs(), rappelé à chaque render().
  var SANS_IA = false;
  // Séance sans compte : le « code » est un jeton de participant. Deux outils
  // s'en vont — voir SANS_CARNET et estJetonDeSeance().
  var SEANCE = false;
  // Les outils qui supposent un lendemain. Le carnet garde des mots pour
  // plus tard, la révision espace des rappels sur des jours : ni l'un ni
  // l'autre n'a de sens pour un participant qui n'existe que le temps d'une
  // séance, et le serveur refuse d'ailleurs `/api/vocab/*` à son jeton
  // (liste blanche ROUTES_SEANCE, server.py). Sans ce retrait, les deux
  // boutons s'ouvraient sur un message d'erreur.
  var SANS_CARNET = ['carn', 'revi'];

  // Un code d'élève fait six caractères ; un jeton de séance en fait
  // dix-sept et commence par S. La règle est celle de
  // `validate_student_code` (server.py) — si elle change là-bas, elle change
  // ici. Se tromper ne rouvre rien : le serveur refuse toujours, seuls les
  // deux boutons réapparaîtraient.
  function estJetonDeSeance(code) {
    return /^S[A-Za-z0-9]{16}$/.test(String(code || ''));
  }

  // ══ Petits utilitaires ════════════════════════════════════════
  function esc(s) {
    return String(s == null ? '' : s).replace(/[&<>"']/g, function (c) {
      return { '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;', "'": '&#39;' }[c];
    });
  }
  // Le gras **ainsi** est la seule mise en forme que l'assistant produit.
  function gras(s) {
    return esc(s).replace(/\*\*([^*]+)\*\*/g, '<b>$1</b>').replace(/\n/g, '<br>');
  }
  function lire(cle, defaut) {
    try { var v = localStorage.getItem(cle); return v === null ? defaut : JSON.parse(v); }
    catch (e) { return defaut; }   // Safari privé fait lever localStorage
  }
  function ecrire(cle, valeur) {
    try { localStorage.setItem(cle, JSON.stringify(valeur)); } catch (e) { }
  }
  function langue() {
    var c = lire(LS_LANGUE, '');
    for (var i = 0; i < LANGUES.length; i++) if (LANGUES[i].c === c) return LANGUES[i];
    return null;
  }
  function propre(t) { return String(t || '').replace(/\s+/g, ' ').trim(); }

  function poste(url, corps) {
    return fetch(url, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify(Object.assign({ code: cfg.code }, corps))
    }).then(function (r) {
      return r.json().catch(function () { return {}; }).then(function (d) {
        if (!r.ok) throw new Error(d.error || 'Le service est indisponible (' + r.status + ')');
        return d;
      });
    });
  }

  function attente(zone, texte) {
    zone.innerHTML = '<div class="oe-wait"><i></i>' + esc(texte) + '</div>';
  }
  function erreur(zone, e) {
    zone.innerHTML = '<div class="oe-err">' + esc(e && e.message ? e.message : String(e)) + '</div>';
  }

  // ══ Construction de l'interface ═══════════════════════════════
  function bati() {
    var racine = document.createElement('div');
    racine.className = 'oe-root';

    var dock = '<nav class="oe-dock" aria-label="Mes outils"><div class="oe-dock-t">Mes<br>outils</div>';
    OUTILS.forEach(function (o) {
      if (o.sep) { dock += '<div class="oe-dock-sep"></div>'; return; }
      if (SEANCE && SANS_CARNET.indexOf(o.id) >= 0) return;
      dock += '<button type="button" class="oe-tool' + (o.audio ? ' oe-audio' : '')
        + '" data-oe-outil="' + o.id + '" aria-pressed="false">'
        + '<span class="oe-ic">' + icone(o.id) + '</span>'
        + '<span class="oe-lb">' + esc(o.lb) + '</span></button>';
    });
    // Masquer le rail libère toute la largeur pour le module. L'état ne se
    // retient pas : à chaque ouverture du module, les outils sont là.
    dock += '<button type="button" class="oe-dock-cacher" id="oe-cacher"'
      + ' aria-label="Masquer les outils">' + chevron('droite')
      + '<span class="oe-dock-cacher-t">Masquer</span></button>';
    dock += '</nav>';

    var montrer = '<button type="button" class="oe-montrer" id="oe-montrer"'
      + ' aria-label="Afficher mes outils">' + chevron('gauche')
      + '<span class="oe-montrer-t">Mes outils</span></button>';

    var panneau = '<aside class="oe-panel" role="dialog" aria-label="Panneau d\'outil" aria-modal="false">'
      + '<div class="oe-h"><div class="oe-ttl"><h3 id="oe-ttl">Outils</h3>'
      + '<div class="oe-sub" id="oe-sub"></div></div>'
      + '<button type="button" class="oe-x" id="oe-x" aria-label="Fermer">✕</button></div>'
      + '<div class="oe-b">'
      + '<section class="oe-pane" id="oe-pane-trad"></section>'
      + '<section class="oe-pane" id="oe-pane-lire"></section>'
      + '<section class="oe-pane" id="oe-pane-simp"></section>'
      + '<section class="oe-pane" id="oe-pane-pron"></section>'
      + '<section class="oe-pane" id="oe-pane-chat"></section>'
      + '<section class="oe-pane" id="oe-pane-carn"></section>'
      + '<section class="oe-pane" id="oe-pane-revi"></section>'
      + '</div></aside>';

    var actions = [['trad', 'Traduire'], ['lire', 'Écouter'], ['simp', 'Simplifier'],
      ['pron', 'Prononcer'], ['carn', 'Garder']].filter(function (a) {
        return !(SEANCE && SANS_CARNET.indexOf(a[0]) >= 0);
      });
    var sel = '<div class="oe-sel" id="oe-sel">' + actions.map(function (a, i) {
      return (i ? '<span class="oe-sep"></span>' : '')
        + '<button type="button" data-oe-sel="' + a[0] + '">'
        + icone(a[0], 18) + esc(a[1]) + '</button>';
    }).join('') + '</div>';

    racine.innerHTML = dock + montrer + panneau + sel;
    document.body.appendChild(racine);
    document.body.classList.add('oe-host');

    // Le choix de la langue est la première chose que l'élève doit voir :
    // il vit en tête de page, dans son propre conteneur, et non dans la
    // racine des outils qui est ajoutée en fin de body.
    var tete = document.createElement('div');
    tete.className = 'oe-root oe-tete';
    tete.innerHTML = bandeauLangue();
    document.body.insertBefore(tete, document.body.firstChild);

    // La hauteur réelle de la bande d'outils est publiée en jeton CSS : sur
    // téléphone, un bloc collé en bas de la page hôte — le banc de réponses
    // des modules — s'arrête dessus. La valeur écrite dans la feuille de
    // style ne vaut que si aucun libellé ne passe sur deux lignes ; on mesure
    // donc plutôt que de s'y fier. Nulle au bureau, où le rail est en colonne.
    var dockEl = racine.querySelector('.oe-dock');
    function mesurerDock() {
      var enBande = matchMedia('(max-width:900px)').matches;
      var h = (enBande && !document.body.classList.contains('oe-cache'))
        ? dockEl.getBoundingClientRect().height : 0;
      document.documentElement.style.setProperty('--oe-dock-h', Math.round(h) + 'px');
    }
    mesurerDock();
    addEventListener('resize', mesurerDock);
    addEventListener('orientationchange', mesurerDock);
    if (window.ResizeObserver) {
      el.dockRO = new ResizeObserver(mesurerDock);
      el.dockRO.observe(dockEl);
    }
    el.mesurerDock = mesurerDock;

    el.tete = tete;
    el.racine = racine;
    el.panel = racine.querySelector('.oe-panel');
    el.ttl = racine.querySelector('#oe-ttl');
    el.sub = racine.querySelector('#oe-sub');
    el.sel = racine.querySelector('#oe-sel');
    OUTILS.forEach(function (o) {
      if (!o.sep) el[o.id] = racine.querySelector('#oe-pane-' + o.id);
    });

    racine.querySelector('#oe-x').onclick = fermer;
    racine.querySelector('#oe-cacher').onclick = function () { montreRail(false); };
    racine.querySelector('#oe-montrer').onclick = function () { montreRail(true); };
    racine.querySelectorAll('[data-oe-outil]').forEach(function (b) {
      b.onclick = function () { ouvrir(b.getAttribute('data-oe-outil')); };
    });
    racine.querySelectorAll('[data-oe-sel]').forEach(function (b) {
      b.onclick = function () {
        retientSelection(window.getSelection());
        cacheSel();
        ouvrir(b.getAttribute('data-oe-sel'), true);
      };
    });
  }

  function bandeauLangue() {
    var L = langue();
    if (L) {
      return '<div class="oe-langbar"><div class="oe-langbar-in">'
        + '<span class="oe-langbar-t">' + icone('trad', 18) + 'Ma langue : '
          + esc(L.loc) + ' · ' + esc(L.n) + '</span>'
        + '<button type="button" id="oe-chg">changer</button></div></div>';
    }
    return '<div class="oe-lang"><div class="oe-lang-in">'
      + '<div style="flex:1;min-width:260px"><h2>Avant de commencer : ma langue maternelle</h2>'
      + '<p>Elle sert aux outils de traduction. Vous pourrez la changer plus tard.</p></div>'
      + '<select id="oe-lsel" aria-label="Ma langue maternelle">'
      + '<option value="">— Choisissez votre langue —</option>'
      + LANGUES.map(function (l) {
        return '<option value="' + l.c + '">' + esc(l.loc) + ' · ' + esc(l.n) + '</option>';
      }).join('')
      + '</select><button type="button" class="oe-ok" id="oe-lok">C\'est noté</button>'
      + '</div></div>';
  }

  function brancheLangue() {
    var chg = el.tete.querySelector('#oe-chg');
    if (chg) { chg.onclick = function () { ecrire(LS_LANGUE, ''); refaitLangue(); }; return; }
    var sel = el.tete.querySelector('#oe-lsel');
    var ok = el.tete.querySelector('#oe-lok');
    if (!sel || !ok) return;
    ok.onclick = function () {
      if (!sel.value) { sel.focus(); return; }
      ecrire(LS_LANGUE, sel.value);
      refaitLangue();
      // Les panneaux déjà remplis montrent l'ancienne langue.
      if (courant) ouvrir(courant, true);
    };
  }

  function refaitLangue() {
    el.tete.innerHTML = bandeauLangue();
    brancheLangue();
  }

  // ══ Marqueurs de traduction en marge des blocs ══════════════
  // Un module généré ne peut pas porter d'attributs data-oe écrits à la main :
  // son HTML est reconstruit, et l'essentiel de son contenu est produit par
  // render() à chaque changement de section. Le module donne donc un sélecteur
  // et un observateur remarque les blocs à mesure qu'ils apparaissent.
  function selecteurBlocs() {
    return cfg.blocs ? '[data-oe],' + cfg.blocs : '[data-oe]';
  }

  function marqueBlocs() {
    if (SANS_IA) return;
    document.querySelectorAll(selecteurBlocs()).forEach(function (bloc) {
      if (el.racine && (el.racine.contains(bloc) || el.tete.contains(bloc))) return;
      if (bloc.querySelector(':scope > .oe-tag')) return;
      bloc.classList.add('oe-zone');
      var b = document.createElement('button');
      b.type = 'button';
      b.className = 'oe-tag';
      b.innerHTML = icone('trad', 16);
      b.title = 'Voir dans ma langue';
      b.setAttribute('aria-label', 'Traduire ce bloc dans ma langue');
      b.onclick = function (ev) {
        ev.stopPropagation();
        traduitBloc(bloc, b);
      };
      bloc.insertBefore(b, bloc.firstChild);
    });
  }

  function texteBloc(bloc, separe) {
    var copie = bloc.cloneNode(true);
    // [aria-live] écarte les compteurs de score des exercices (« 0 / 8
    // répondu ») : c'est de l'état d'interface, pas du texte à traduire, et
    // il polluait aussi bien la traduction que le contexte de l'assistant.
    copie.querySelectorAll('.oe-tag, .oe-trad, [aria-live], script, style')
      .forEach(function (n) { n.remove(); });
    // textContent recolle les éléments voisins sans espace : un titre suivi
    // d'un paragraphe donne « au QuébecLe chiffre ». Illisible à voix haute.
    // Seule la lecture demande la séparation : la traduction garde l'ancien
    // texte, sinon toutes les traductions déjà payées changeraient de clé.
    if (separe) {
      copie.querySelectorAll(COUPURES).forEach(function (n) {
        n.appendChild(document.createTextNode(' '));
      });
    }
    return propre(copie.textContent);
  }

  // Le paragraphe entier qui contient la sélection, ou '' si elle tombe hors
  // du contenu du module. C'est ce texte-là qu'on fait lire, et non la
  // sélection au caractère près : le cache de voix du serveur est indexé sur
  // le texte exact, donc trente élèves qui surlignent le même paragraphe à un
  // mot près font trente lectures facturées. Le même paragraphe n'en fait
  // qu'une. La traduction, le carnet et la prononciation gardent la sélection
  // exacte : on y surligne un mot pour avoir ce mot-là, pas ce qui l'entoure.
  //
  // On vise le paragraphe et non le bloc marqué : les blocs des modules sont
  // des cartes entières, de trois cents à mille sept cents caractères, et
  // faire écouter la carte pour une phrase surlignée noierait l'élève sous les
  // consignes d'exercice qui l'accompagnent. Le bloc ne sert que de garde-fou
  // — hors d'un bloc, on ne touche à rien — et de repli.
  var PARAGRAPHES = 'p,li,dt,dd,td,th,h1,h2,h3,h4,h5,h6,blockquote,figcaption,summary';
  var COUPURES = 'p,div,li,dt,dd,td,tr,section,article,header,footer,br,'
    + 'h1,h2,h3,h4,h5,h6,blockquote,figcaption,summary';
  var PARA_MIN = 40;   // en deçà, on tient l'élément pour un fragment

  // Les modules générés n'ont ni <p> ni <li> : leur contenu est en <div class=
  // "stxt">, <div class="vf-row">. Une liste de balises n'y mord sur rien et
  // tout retomberait sur la carte. À défaut de balise parlante, on remonte
  // donc jusqu'au premier ancêtre qui porte un texte d'un seul tenant — la
  // taille plancher écarte les étiquettes (« VRAI », un mot de vocabulaire)
  // sans jamais dépasser le bloc.
  function paragrapheDe(e, bloc) {
    var para = e.closest(PARAGRAPHES);
    if (para && bloc.contains(para) && texteBloc(para, true).length >= PARA_MIN) return para;
    var n = e;
    while (n && n !== bloc) {
      if (texteBloc(n, true).length >= PARA_MIN) return n;
      n = n.parentElement;
    }
    return bloc;
  }

  function blocDe(noeud) {
    var e = noeud && (noeud.nodeType === 1 ? noeud : noeud.parentElement);
    if (!e || !e.closest) return '';
    var bloc;
    try { bloc = e.closest(selecteurBlocs()); }
    catch (err) { return ''; }   // sélecteur de module mal formé : on s'efface
    if (!bloc || el.racine.contains(bloc) || el.tete.contains(bloc)) return '';
    return texteBloc(paragrapheDe(e, bloc), true).slice(0, 400);
  }

  // Retient une sélection du document sous ses deux formes. Rend false quand il
  // n'y a rien à retenir — l'ancienne sélection reste alors en place, ce qui
  // laisse rouvrir un outil après avoir cliqué ailleurs.
  function retientSelection(s) {
    var t = propre(String(s || ''));
    if (!t) return false;
    selection = t;
    selectionBloc = blocDe(s && s.anchorNode);
    return true;
  }

  function traduitBloc(bloc, bouton) {
    var deja = bloc.querySelector(':scope > .oe-trad');
    if (deja) { deja.remove(); bouton.classList.remove('oe-actif'); return; }

    var L = langue();
    if (!L) { refaitLangue(); alerteLangue(); return; }

    var boite = document.createElement('div');
    boite.className = 'oe-trad';
    boite.innerHTML = '<div class="oe-wait"><i></i>Je traduis…</div>';
    bloc.appendChild(boite);
    bouton.classList.add('oe-actif');

    poste('/api/outils/traduire', { langue: L.n, texte: texteBloc(bloc), contexte: cfg.section })
      .then(function (d) {
        boite.innerHTML = '<div class="oe-lbl">' + esc(L.loc) + '</div><p'
          + (L.rtl ? ' dir="rtl"' : '') + '>' + esc(d.traduction).replace(/\n/g, '<br>') + '</p>';
      })
      .catch(function (e) {
        boite.innerHTML = '<div class="oe-err">' + esc(e.message) + '</div>';
      });
  }

  function alerteLangue() {
    // Le bandeau noir est déjà revenu en haut de la page : on y amène l'élève.
    var b = el.tete.querySelector('.oe-lang');
    if (b) { b.scrollIntoView({ behavior: 'smooth', block: 'center' }); }
  }

  // ══ Rail visible ou masqué ════════════════════════════════════
  // Volontairement sans mémoire : le rail revient à chaque ouverture du
  // module. Un élève qui l'a masqué hier ne doit pas se retrouver sans
  // outils aujourd'hui sans savoir pourquoi.
  function montreRail(oui) {
    if (!oui) fermer();
    document.body.classList.toggle('oe-cache', !oui);
    if (el.mesurerDock) el.mesurerDock();
    var b = el.racine.querySelector(oui ? '#oe-cacher' : '#oe-montrer');
    if (b) b.focus();
  }

  // ══ Ouverture / fermeture ═════════════════════════════════════
  function ouvrir(id, force) {
    if (courant === id && !force) return fermer();
    courant = id;
    document.body.classList.add('oe-open');
    var meta = OUTILS.filter(function (o) { return o.id === id; })[0] || {};
    el.ttl.textContent = meta.t || '';
    el.sub.textContent = (id === 'chat' || id === 'lire') ? (cfg.section || '') : (meta.s || '');
    el.racine.querySelectorAll('.oe-pane').forEach(function (p) {
      p.classList.toggle('oe-on', p.id === 'oe-pane-' + id);
    });
    el.racine.querySelectorAll('[data-oe-outil]').forEach(function (b) {
      b.setAttribute('aria-pressed', String(b.getAttribute('data-oe-outil') === id));
    });
    ({ trad: paneTrad, lire: paneLire, simp: paneSimp, pron: panePron, chat: paneChat,
      carn: paneCarn, revi: paneRevi }[id])();
  }

  function fermer() {
    courant = null;
    document.body.classList.remove('oe-open');
    if (!el.racine) return;          // barre retirée : plus rien à refermer
    el.racine.querySelectorAll('[data-oe-outil]').forEach(function (b) {
      b.setAttribute('aria-pressed', 'false');
    });
    stopAudio();
  }

  // ══ Audio (ElevenLabs, repli sur la voix du navigateur) ═══════
  // « Arrêter » ne peut pas arrêter ce qui n'a pas encore commencé. Entre le
  // moment où l'élève touche « Écouter » et le premier son, il se passe deux
  // attentes : l'appel au serveur, puis les 120 ms que réclame Chrome avant
  // de parler. Touché pendant l'une ou l'autre, le bouton mettait en pause un
  // lecteur inexistant, annulait un énoncé pas encore soumis — et le son
  // partait juste après. De l'extérieur : « le bouton Arrêter ne marche pas ».
  //
  // Le numéro de lecture règle les deux : chaque « Écouter » prend le sien,
  // « Arrêter » l'incrémente, et tout rappel qui revient avec un numéro périmé
  // se tait. Même parade que pour la voix du jeu de rôle et le micro.
  var lectureNo = 0;
  var enVol = null;              // l'appel au serveur, pour le couper aussi

  function stopAudio() {
    lectureNo++;
    if (enVol) { try { enVol.abort(); } catch (e) {} enVol = null; }
    if (audioEnCours) { audioEnCours.pause(); audioEnCours = null; }
    if (global.speechSynthesis) global.speechSynthesis.cancel();
  }

  // Un même passage est réécouté plusieurs fois, et à deux vitesses : on
  // garde le MP3 en mémoire pour ne pas refacturer les mêmes caractères.
  var cacheSons = {};

  function dis(texte, vitesse, etat) {
    stopAudio();
    var no = lectureNo;           // pris APRÈS stopAudio, qui vient d'incrémenter
    // `etat` reçoit un mot sur ce qui a lu — ou sur ce qui n'a pas lu. Sans
    // lui, un refus du serveur suivi d'un navigateur sans voix française ne
    // laissait aucune trace : l'élève touchait « Écouter » et il ne se
    // passait rien du tout, sans un mot d'explication.
    var dire = etat || function () {};
    var t = propre(texte).slice(0, 400);
    if (!t) return Promise.resolve();

    // Le ralenti garde la voix d'ElevenLabs et joue sur playbackRate plutôt
    // que de basculer sur la voix du navigateur : même timbre à l'écoute
    // normale et à l'écoute lente, et surtout ça marche — speechSynthesis
    // avale l'énoncé quand cancel() vient de passer (stopAudio ci-dessus).
    // preservesPitch évite la voix de dessin animé au ralentissement.
    var joue = function (blob) {
      if (no !== lectureNo) return;      // l'élève a coupé pendant l'attente
      var a = new Audio(URL.createObjectURL(blob));
      a.playbackRate = vitesse || 1;
      a.preservesPitch = true;
      a.mozPreservesPitch = true;
      a.webkitPreservesPitch = true;
      audioEnCours = a;
      return a.play();
    };

    if (cacheSons[t]) { dire(''); return joue(cacheSons[t]); }

    // AbortController n'est là que pour cesser d'attendre : le numéro de
    // lecture suffirait à faire taire le son, mais laisser courir un appel
    // qu'on ne veut plus, c'est payer des caractères pour rien.
    var ctrl = global.AbortController ? new AbortController() : null;
    enVol = ctrl;
    return fetch('/api/voix', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      // Le module part avec la demande : c'est de LUI que le serveur tire le
      // niveau, donc le débit de lecture. Sans ce champ, l'outil lisait à
      // +15 % partout — au niveau 3, plus vite que le dialogue que l'élève
      // venait justement de ne pas comprendre.
      body: JSON.stringify({ code: cfg.code, texte: t, voix: 'lecture',
                             module: cfg.module }),
      signal: ctrl ? ctrl.signal : undefined
    }).then(function (r) {
      // Le 401 n'est pas une panne : c'est une page ouverte sans code d'élève,
      // et le remède n'est pas le même. On distingue donc les deux ici.
      if (!r.ok) throw new Error(r.status === 401 ? 'code' : 'voix');
      return r.blob();
    }).then(function (blob) {
      cacheSons[t] = blob;
      dire('');
      return joue(blob);
    }).catch(function (e) {
      // Une coupure voulue n'est pas une panne : sans ce filtre, « Arrêter »
      // affichait « La voix du cours n'a pas répondu » et basculait sur la
      // voix de l'appareil — exactement ce qu'on venait d'interrompre.
      if (no !== lectureNo || (e && e.name === 'AbortError')) return;
      var cause = (e && e.message === 'code')
        ? 'La voix du cours a besoin de votre code : ouvrez le module depuis votre portail.'
        : 'La voix du cours n\'a pas répondu.';
      // Dit tout de suite ce qui se passe : `navigateurDit` ne se résout qu'à
      // la fin de l'énoncé, et attendre trois secondes pour l'annoncer, c'est
      // trois secondes pendant lesquelles l'élève croit que rien ne marche.
      dire(cause + ' J\'emploie la voix de l\'appareil.');
      return navigateurDit(t, vitesse || 1).then(function (parle) {
        if (!parle) dire(cause + ' Et cet appareil n\'a pas de voix française : la lecture est impossible ici.');
      });
    });
  }

  // Repli quand ElevenLabs ne répond pas. Le délai n'est pas décoratif :
  // enchaîner cancel() et speak() dans le même tour de boucle laisse Chrome
  // ignorer l'énoncé.
  function navigateurDit(t, vitesse) {
    return new Promise(function (res) {
      if (!global.speechSynthesis || !global.SpeechSynthesisUtterance) return res(false);
      global.speechSynthesis.cancel();
      var mien = lectureNo;
      setTimeout(function () {
        if (mien !== lectureNo) return res(false);   // coupé pendant les 120 ms
        var parti = false;
        var u = new SpeechSynthesisUtterance(t);
        u.lang = 'fr-CA';
        u.rate = vitesse || 1;
        u.onstart = function () { parti = true; };
        u.onend = function () { res(true); };
        u.onerror = function () { res(parti); };
        try { global.speechSynthesis.speak(u); } catch (e) { return res(false); }
        // Un navigateur sans voix française avale l'énoncé sans lever
        // d'erreur : rien ne commence, et onend ne vient jamais. Une seconde
        // et demie suffit à séparer « ça parle » de « ça ne parlera pas ».
        setTimeout(function () {
          if (!parti && !global.speechSynthesis.speaking) res(false);
        }, 1500);
      }, 120);
    });
  }

  // ══ Panneau : TRADUIRE ════════════════════════════════════════
  function paneTrad() {
    var L = langue();
    var z = el.trad;
    if (!L) {
      z.innerHTML = '<div class="oe-tip">Choisissez d\'abord votre langue maternelle, '
        + 'dans le bandeau noir en haut de la page.</div>';
      return;
    }
    if (!selection) {
      z.innerHTML = '<div class="oe-tip"><b>Comment faire :</b> surlignez une phrase avec la souris '
        + '(ou avec le doigt), puis touchez « Traduire ». Vous pouvez aussi toucher le marqueur '
        + 'en marge d\'un bloc pour traduire le bloc entier.</div>';
      return;
    }
    z.innerHTML = '<div class="oe-quote">' + esc(selection) + '</div>'
      + '<div class="oe-lbl">' + esc(L.loc) + '</div><div id="oe-trad-r"></div>'
      + '<div class="oe-row" style="margin-top:20px">'
      + '<button type="button" class="oe-btn oe-ghost" id="oe-trad-son">' + icone('lire', 18) + 'Écouter</button>'
      + (SEANCE ? ''
        : '<button type="button" class="oe-btn oe-ghost" id="oe-trad-gard">' + icone('carn', 18) + 'Garder</button>')
      + '</div>';

    var r = z.querySelector('#oe-trad-r');
    var passage = selection;
    attente(r, 'Je traduis…');
    poste('/api/outils/traduire', { langue: L.n, texte: passage, contexte: cfg.section })
      .then(function (d) {
        r.innerHTML = '<div class="oe-res"' + (L.rtl ? ' dir="rtl"' : '') + '>'
          + esc(d.traduction).replace(/\n/g, '<br>') + '</div>';
        var g = z.querySelector('#oe-trad-gard');
        if (g) g.onclick = function () { ajouteCarnet(passage, d.traduction); };
      })
      .catch(function (e) { erreur(r, e); });

    z.querySelector('#oe-trad-son').onclick = function () { dis(passage); };
  }

  // ══ Panneau : LIRE ════════════════════════════════════════════
  function paneLire() {
    var t = selectionBloc || selection || texteParDefaut();
    el.lire.innerHTML = (t
      ? '<div class="oe-lbl">Texte à lire</div><div class="oe-quote">' + esc(t.slice(0, 400))
        + (t.length > 400 ? ' …' : '') + '</div>'
        + '<button type="button" class="oe-btn oe-dark oe-full" id="oe-l1">' + icone('lire', 18) + 'Écouter</button>'
        + '<button type="button" class="oe-btn oe-ghost oe-full" id="oe-l2">' + icone('lire', 18) + 'Écouter lentement</button>'
        + '<button type="button" class="oe-btn oe-ghost oe-full" id="oe-l3">Arrêter</button>'
        + '<div class="oe-tip" id="oe-l-etat" aria-live="polite" hidden></div>'
      : '')
      + '<div class="oe-tip">Surlignez un passage pour le faire lire. La lecture '
      + 'prend le paragraphe au complet. Sans sélection, elle prend le premier '
      + 'bloc de la page.</div>';
    if (!t) return;
    var etat = el.lire.querySelector('#oe-l-etat');
    var dire = function (m) { etat.textContent = m || ''; etat.hidden = !m; };
    el.lire.querySelector('#oe-l1').onclick = function () { dire(''); dis(t, 1, dire); };
    el.lire.querySelector('#oe-l2').onclick = function () { dire(''); dis(t, 0.7, dire); };
    el.lire.querySelector('#oe-l3').onclick = stopAudio;
  }

  function texteParDefaut() {
    // selecteurBlocs() et non [data-oe] seul : un module généré n'a que le
    // sélecteur passé à init(), donc la lecture sans sélection n'y trouvait
    // jamais rien et le panneau restait vide.
    var b;
    try { b = document.querySelector(selecteurBlocs()); } catch (e) { return ''; }
    return b ? texteBloc(b, true).slice(0, 400) : '';
  }

  // ══ Panneau : SIMPLIFIER ══════════════════════════════════════
  function paneSimp() {
    var z = el.simp;
    if (!selection) {
      z.innerHTML = '<div class="oe-tip"><b>Une phrase trop longue ?</b> Surlignez-la, puis touchez '
        + '« Simplifier ». Je la réécris en phrases plus courtes — <b>en français</b>. '
        + 'Souvent, ça suffit : pas besoin de traduire.</div>';
      return;
    }
    z.innerHTML = '<div class="oe-lbl">Phrase du module</div>'
      + '<div class="oe-quote">' + esc(selection) + '</div>'
      + '<div class="oe-lbl">Plus simplement</div><div id="oe-simp-r"></div>';

    var r = z.querySelector('#oe-simp-r');
    var passage = selection;
    attente(r, 'Je reformule…');
    poste('/api/outils/simplifier', { texte: passage })
      .then(function (d) {
        var h = '<div class="oe-res oe-vert">' + esc(d.simple).replace(/\n/g, '<br>') + '</div>';
        if (d.mot) {
          h += '<div class="oe-lbl" style="margin-top:20px">Le mot difficile</div>'
            + '<div class="oe-quote"><b>' + esc(d.mot) + '</b> — ' + esc(d.explication) + '</div>'
            + (SEANCE ? ''
              : '<button type="button" class="oe-btn oe-soft oe-full" id="oe-simp-g">'
                + icone('carn', 18) + 'Garder « ' + esc(d.mot) + ' »</button>');
        }
        h += '<div class="oe-row" style="margin-top:12px">'
          + '<button type="button" class="oe-btn oe-ghost" id="oe-simp-s">' + icone('lire', 18) + 'Écouter</button>'
          + '<button type="button" class="oe-btn oe-ghost" id="oe-simp-t">' + icone('trad', 18) + 'Traduire</button></div>';
        r.innerHTML = h;
        r.querySelector('#oe-simp-s').onclick = function () { dis(d.simple); };
        r.querySelector('#oe-simp-t').onclick = function () {
          // Le bloc d'origine ne vaut plus pour ce passage-ci : on le lâche,
          // sans quoi « Lire » ferait entendre le paragraphe d'avant.
          selection = passage; selectionBloc = '';
          ouvrir('trad', true);
        };
        var g = r.querySelector('#oe-simp-g');
        if (g) g.onclick = function () { ajouteCarnet(d.mot, d.explication); };
      })
      .catch(function (e) { erreur(r, e); });
  }

  // ══ Panneau : PRONONCER ═══════════════════════════════════════
  var SR = global.SpeechRecognition || global.webkitSpeechRecognition;

  function panePron() {
    var z = el.pron;
    if (!selection) {
      z.innerHTML = '<div class="oe-tip"><b>Comment faire :</b> surlignez un mot ou une phrase, '
        + 'puis touchez « Prononcer ». Vous écoutez le modèle, vous vous enregistrez, '
        + 'et vous comparez. Aucune note, aucun compte : recommencez autant de fois '
        + 'que vous voulez.</div>';
      return;
    }
    var cible = selection.slice(0, 200);
    z.innerHTML = '<div class="oe-lbl">À prononcer</div>'
      + '<div class="oe-quote">' + esc(cible) + '</div>'
      + '<button type="button" class="oe-btn oe-dark oe-full" id="oe-p1">' + icone('lire', 18) + 'Écouter le modèle</button>'
      + '<button type="button" class="oe-btn oe-ghost oe-full" id="oe-p2">' + icone('lire', 18) + 'Écouter lentement</button>'
      + (SR
        ? '<button type="button" class="oe-btn oe-red oe-full" id="oe-p3">' + icone('pron', 18) + 'Enregistrer ma voix</button>'
        : '<div class="oe-tip" style="margin-top:12px">Votre navigateur ne sait pas comparer '
          + 'automatiquement. <b>Ouvrez le module dans Chrome</b> pour cet outil-là. '
          + 'En attendant, écoutez le modèle et répétez à voix haute.</div>')
      + '<div id="oe-pron-r" style="margin-top:20px"></div>';

    z.querySelector('#oe-p1').onclick = function () { dis(cible); };
    z.querySelector('#oe-p2').onclick = function () { dis(cible, 0.65); };
    if (SR) z.querySelector('#oe-p3').onclick = function () { ecoute(cible, this); };
  }

  function normalise(m) {
    return m.toLowerCase()
      .normalize('NFD').replace(/[\u0300-\u036f]/g, '')   // accents
      .replace(/[^a-z0-9']/g, '');                        // ponctuation
  }

  function ecoute(cible, bouton) {
    var r = el.pron.querySelector('#oe-pron-r');
    stopAudio();
    var reco = new SR();
    reco.lang = 'fr-CA';
    reco.interimResults = false;
    reco.maxAlternatives = 1;

    bouton.innerHTML = icone('pron', 18) + 'J\'écoute… parlez';
    bouton.disabled = true;
    r.innerHTML = '';

    reco.onresult = function (ev) { compare(cible, ev.results[0][0].transcript, r); };
    reco.onerror = function (ev) {
      r.innerHTML = '<div class="oe-err">' + (ev.error === 'not-allowed'
        ? 'Le micro est bloqué. Autorisez le micro dans la barre d\'adresse, puis réessayez.'
        : 'Je n\'ai rien entendu. Réessayez en parlant plus fort.') + '</div>';
    };
    reco.onend = function () {
      bouton.innerHTML = icone('pron', 18) + 'Enregistrer ma voix';
      bouton.disabled = false;
    };
    try { reco.start(); } catch (e) { reco.onend(); }
  }

  function compare(cible, entendu, zone) {
    var attendus = cible.split(/\s+/).filter(Boolean);
    var dits = entendu.split(/\s+/).map(normalise).filter(Boolean);
    var reste = dits.slice();
    var bons = 0;

    var html = '<div class="oe-lbl">Résultat</div>';
    var mots = attendus.map(function (m) {
      var n = normalise(m);
      if (!n) return '<span class="oe-mot oe-o">' + esc(m) + '</span>';
      var i = reste.indexOf(n);
      if (i >= 0) { reste.splice(i, 1); bons++; return '<span class="oe-mot oe-o">' + esc(m) + '</span>'; }
      return '<span class="oe-mot oe-n">' + esc(m) + '</span>';
    }).join('');

    var pct = attendus.length ? Math.round(bons / attendus.length * 100) : 0;
    html += '<div class="oe-jauge"><i style="width:' + pct + '%"></i></div>'
      + '<div class="oe-mots">' + mots + '</div>'
      + '<div class="oe-entendu">J\'ai entendu : « ' + esc(entendu) + ' »</div>'
      + '<div class="oe-res' + (pct >= 80 ? ' oe-vert' : '') + '">'
      + (pct === 100 ? 'Parfait — tous les mots y sont.'
        : pct >= 80 ? 'C\'est très bien. Reprenez seulement les mots en rouge.'
          : pct >= 50 ? 'Bon début. Réécoutez le modèle lentement, puis recommencez.'
            : 'Réécoutez le modèle deux fois avant de reprendre. Parlez lentement.')
      + '</div>'
      + '<button type="button" class="oe-btn oe-soft oe-full" style="margin-top:16px" id="oe-pr">Recommencer</button>';
    zone.innerHTML = html;
    zone.querySelector('#oe-pr').onclick = function () { panePron(); };
  }

  // ══ Panneau : ASSISTANT ═══════════════════════════════════════
  var SUGGESTIONS = [
    'Je ne comprends pas la consigne.',
    'Qu\'est-ce que ça veut dire ?',
    'Donnez-moi un exemple.'
  ];

  function paneChat() {
    if (el.chat.dataset.pret) { fondChat(); return; }
    el.chat.dataset.pret = '1';
    el.chat.innerHTML = '<div class="oe-chat" id="oe-chat-l"></div>'
      + '<div class="oe-sugg" id="oe-chat-s">'
      + SUGGESTIONS.map(function (s) {
        return '<button type="button">' + esc(s) + '</button>';
      }).join('') + '</div>'
      + '<div class="oe-saisie">'
      + '<input id="oe-chat-i" placeholder="Écrivez votre question…" aria-label="Votre question">'
      + (SR ? '<button type="button" class="oe-mic" id="oe-chat-m" aria-label="Dicter">' + icone('pron', 20) + '</button>' : '')
      + '<button type="button" class="oe-go" id="oe-chat-g" aria-label="Envoyer">➤</button></div>';

    bulle('ia', 'Bonjour ! Je suis là pendant que vous travaillez. Posez-moi une question '
      + 'sur un mot, une phrase ou une consigne.\n\nJe ne donne pas les réponses des '
      + 'exercices — mais je donne des indices.');

    el.chat.querySelectorAll('#oe-chat-s button').forEach(function (b) {
      b.onclick = function () { envoie(b.textContent); };
    });
    el.chat.querySelector('#oe-chat-g').onclick = function () {
      var i = el.chat.querySelector('#oe-chat-i');
      envoie(i.value); i.value = '';
    };
    el.chat.querySelector('#oe-chat-i').onkeydown = function (e) {
      if (e.key === 'Enter') { envoie(this.value); this.value = ''; }
    };
    var mic = el.chat.querySelector('#oe-chat-m');
    if (mic) mic.onclick = function () { dicte(mic); };
  }

  function bulle(qui, texte) {
    var l = el.chat.querySelector('#oe-chat-l');
    var d = document.createElement('div');
    d.className = 'oe-bul oe-' + (qui === 'moi' ? 'moi' : 'ia');
    d.innerHTML = gras(texte);
    l.appendChild(d);
    fondChat();
    return d;
  }
  function fondChat() {
    var b = el.panel.querySelector('.oe-b');
    if (b) b.scrollTop = b.scrollHeight;
  }

  function envoie(texte) {
    var q = propre(texte);
    if (!q) return;
    bulle('moi', q);
    chat.push({ role: 'user', content: q });

    var att = bulle('ia', '…');
    att.innerHTML = '<div class="oe-wait"><i></i>Je réfléchis…</div>';
    var L = langue();

    poste('/api/outils/assistant', {
      langue: L ? L.n : '',
      module: cfg.module,
      section: cfg.section,
      contexte: contexte(),
      historique: chat
    }).then(function (d) {
      att.innerHTML = gras(d.reponse);
      chat.push({ role: 'assistant', content: d.reponse });
      fondChat();
    }).catch(function (e) {
      att.outerHTML = '<div class="oe-err">' + esc(e.message) + '</div>';
      chat.pop();   // la question n'a pas eu de réponse : on la retire de l'historique
      fondChat();
    });
  }

  function dicte(bouton) {
    if (!SR) return;
    var reco = new SR();
    reco.lang = 'fr-CA';
    reco.interimResults = false;
    bouton.classList.add('oe-actif');
    reco.onresult = function (ev) {
      el.chat.querySelector('#oe-chat-i').value = ev.results[0][0].transcript;
    };
    reco.onend = function () { bouton.classList.remove('oe-actif'); };
    reco.onerror = reco.onend;
    try { reco.start(); } catch (e) { reco.onend(); }
  }

  // Le texte que l'élève a sous les yeux : c'est la seule source de
  // l'assistant sur le contenu du module. Borné, sinon chaque question
  // renverrait la page entière — mais assez large pour qu'une section
  // complète y tienne, exercices compris. À 2000, le dialogue du Défi 1
  // mangeait tout le budget et l'assistant ne voyait pas les questions.
  var MAX_CONTEXTE = 6000;
  function contexte() {
    if (typeof cfg.contexte === 'function') return String(cfg.contexte()).slice(0, MAX_CONTEXTE);
    var morceaux = [];
    document.querySelectorAll(selecteurBlocs()).forEach(function (b) {
      // Un bloc caché appartient à une autre section : l'assistant doit voir
      // ce que l'élève a sous les yeux, pas tout le module.
      if (b.offsetParent === null) return;
      morceaux.push(texteBloc(b));
    });
    return morceaux.join('\n\n').slice(0, MAX_CONTEXTE);
  }

  // ══ Panneau : CARNET ══════════════════════════════════════════
  function cleCarnet() { return 'francisation-carnet-' + (cfg.module || 'module'); }

  function ajouteCarnet(mot, trad) {
    if (SEANCE) return;
    var m = propre(mot).slice(0, 120);
    if (!m) return;
    var liste = lire(cleCarnet(), []);
    if (!liste.some(function (x) { return x.mot.toLowerCase() === m.toLowerCase(); })) {
      liste.push({ mot: m, trad: propre(trad).slice(0, 200) });
      ecrire(cleCarnet(), liste);
    }
    ouvrir('carn', true);
  }

  function paneCarn() {
    var liste = lire(cleCarnet(), []);
    if (!liste.length) {
      el.carn.innerHTML = '<div class="oe-tip"><b>Votre carnet est vide.</b> Surlignez un mot '
        + 'n\'importe où dans le module, puis touchez « Garder ». Le mot revient ici avec '
        + 'sa traduction.</div>';
      return;
    }
    el.carn.innerHTML = '<div class="oe-lbl">Mots gardés — ' + liste.length + '</div>'
      + liste.map(function (x, i) {
        return '<div class="oe-mot-l"><b>' + esc(x.mot) + '</b><span>' + esc(x.trad || '—')
          + '</span><button type="button" class="oe-del" data-i="' + i
          + '" aria-label="Retirer">✕</button></div>';
      }).join('')
      + '<button type="button" class="oe-btn oe-soft oe-full" style="margin-top:20px" id="oe-carn-l">'
      + icone('lire', 18) + 'Écouter tous les mots</button>';

    el.carn.querySelectorAll('.oe-del').forEach(function (b) {
      b.onclick = function () {
        var l = lire(cleCarnet(), []);
        l.splice(parseInt(b.dataset.i, 10), 1);
        ecrire(cleCarnet(), l);
        paneCarn();
      };
    });
    el.carn.querySelector('#oe-carn-l').onclick = function () {
      dis(liste.map(function (x) { return x.mot; }).join(', '));
    };
  }

  // ══ Réviser mes mots ══════════════════════════════════════════
  // Le panneau ne révise pas : il montre où en est l'élève et ouvre
  // l'application de cartes mémoire, qui porte la répétition espacée. Deux
  // moteurs de mémorisation, ce serait deux progressions qui divergent.
  var APP_MOTS = '/assets/interactive/vocabulaire-flash/vocabulaire-flash-activite-interactive.html';

  function ouvreAppMots(activityId) {
    var u = APP_MOTS + '?code=' + encodeURIComponent(cfg.code)
      + (activityId ? '&liste=' + encodeURIComponent(activityId) : '');
    // Le module tourne dans le cadre du portail : une nouvelle fenêtre évite
    // de faire perdre à l'élève la section où il en était.
    global.open(u, '_blank', 'noopener');
  }

  function ligneListe(l, vedette) {
    var pct = l.total ? Math.round((l.mastered / l.total) * 100) : 0;
    var fini = l.total > 0 && l.mastered === l.total;
    var etat = fini ? '<b class="oe-liste-ok">✓ Liste maîtrisée</b>'
      : '<b>' + l.mastered + ' / ' + l.total + '</b> mots maîtrisés'
        + (l.due ? ' · <b class="oe-liste-du">' + l.due + ' à revoir</b>' : '');
    return '<div class="oe-liste' + (vedette ? ' oe-liste-v' : '') + '">'
      + (vedette ? '<div class="oe-lbl">Les mots de ce module</div>' : '')
      + '<div class="oe-liste-t">' + esc(l.titre) + '</div>'
      + '<div class="oe-liste-b"><span style="width:' + pct + '%"></span></div>'
      + '<div class="oe-liste-s">' + etat + '</div>'
      + '<button type="button" class="oe-btn ' + (vedette ? 'oe-dark' : 'oe-ghost')
      + ' oe-full" style="margin-top:12px" data-oe-liste="' + l.activityId + '">'
      + icone('revi', 18) + (fini ? 'Revoir ces mots' : 'Réviser ces mots') + '</button>'
      + '</div>';
  }

  function paneRevi() {
    var zone = el.revi;
    if (!cfg.code) {
      zone.innerHTML = '<div class="oe-tip"><b>Ouvrez le module depuis votre portail</b> '
        + 'pour retrouver vos listes de mots.</div>';
      return;
    }
    attente(zone, 'Je regarde vos listes…');
    fetch('/api/vocab/listes?code=' + encodeURIComponent(cfg.code)
      + '&module=' + encodeURIComponent(cfg.module))
      .then(function (r) {
        return r.json().catch(function () { return {}; }).then(function (d) {
          if (!r.ok) throw new Error(d.error || 'Les listes sont indisponibles.');
          return d;
        });
      })
      .then(function (d) {
        var listes = d.listes || [];
        if (!listes.length) {
          zone.innerHTML = '<div class="oe-tip"><b>Aucune liste pour le moment.</b> '
            + 'Les mots arrivent avec les modules de votre cours.</div>';
          return;
        }
        var courante = listes.filter(function (l) { return l.courante; })[0];
        var autres = listes.filter(function (l) { return !l.courante; });

        var h = courante ? ligneListe(courante, true) : '';
        h += '<button type="button" class="oe-btn oe-soft oe-full" id="oe-liste-du">'
          + icone('revi', 18) + (d.dueTotal
            ? 'Réviser mes ' + d.dueTotal + ' mots du jour'
            : 'Découvrir de nouveaux mots') + '</button>';
        if (autres.length) {
          h += '<div class="oe-lbl" style="margin-top:22px">Mes autres listes</div>'
            + autres.map(function (l) { return ligneListe(l, false); }).join('');
        }
        zone.innerHTML = h;
        zone.querySelectorAll('[data-oe-liste]').forEach(function (b) {
          b.onclick = function () { ouvreAppMots(b.getAttribute('data-oe-liste')); };
        });
        zone.querySelector('#oe-liste-du').onclick = function () { ouvreAppMots(''); };
      })
      .catch(function (e) { erreur(zone, e); });
  }

  // ══ Barre flottante de sélection ══════════════════════════════
  function cacheSel() { if (el.sel) el.sel.classList.remove('oe-on'); }

  function montreSel() {
    // En mode sans assistant il n'y a plus ni bulle ni racine : la sélection
    // redevient une sélection ordinaire.
    if (SANS_IA) return;
    var s = global.getSelection();
    if (!s || s.isCollapsed) return cacheSel();
    var t = propre(String(s));
    if (!t || t.length > 600) return cacheSel();
    // Une sélection faite DANS le panneau ne doit pas rouvrir la barre.
    var noeud = s.anchorNode;
    var hote = noeud && (noeud.nodeType === 1 ? noeud : noeud.parentElement);
    if (!hote || el.racine.contains(hote) || el.tete.contains(hote)) return cacheSel();

    selection = t;
    selectionBloc = blocDe(noeud);
    var r = s.getRangeAt(0).getBoundingClientRect();
    el.sel.classList.add('oe-on');
    var l = r.left + global.scrollX + r.width / 2 - el.sel.offsetWidth / 2;
    l = Math.max(8, Math.min(l, global.innerWidth - el.sel.offsetWidth - 8));
    el.sel.style.left = l + 'px';
    el.sel.style.top = Math.max(8, r.top + global.scrollY - el.sel.offsetHeight - 10) + 'px';
  }

  // ══ Entrée publique ═══════════════════════════════════════════
  function init(options) {
    if (cfg) return;                       // une seule barre par page
    cfg = Object.assign({ code: '', module: 'module', section: '', contexte: null, blocs: '' },
      options || {});
    SEANCE = estJetonDeSeance(cfg.code);
    bati();
    brancheLangue();
    marqueBlocs();

    // Le module réécrit ses sections : on remarque les blocs neufs. Le délai
    // regroupe la rafale de mutations d'un render() en un seul passage.
    if (cfg.blocs && global.MutationObserver) {
      var minuteur = null;
      new MutationObserver(function () {
        clearTimeout(minuteur);
        minuteur = setTimeout(marqueBlocs, 80);
      }).observe(document.body, { childList: true, subtree: true });
    }

    document.addEventListener('mouseup', function () { setTimeout(montreSel, 10); });
    document.addEventListener('touchend', function () { setTimeout(montreSel, 40); });
    document.addEventListener('mousedown', function (e) {
      if (el.sel && !el.sel.contains(e.target)) cacheSel();
    });
    document.addEventListener('keydown', function (e) {
      if (e.key === 'Escape') { cacheSel(); fermer(); }
    });
  }

  global.Outils = {
    init: init,
    // Le module appelle ceci quand l'élève change de section : l'assistant
    // et le sous-titre du panneau suivent.
    setSection: function (titre) {
      if (cfg) { cfg.section = titre; if (courant) el.sub.textContent = titre; }
    },
    ouvrir: function (id) {
      if (!cfg || SANS_IA) return;
      if (SEANCE && SANS_CARNET.indexOf(id) >= 0) return;
      ouvrir(id, true);
    },

    // ── Le mode sans assistant ────────────────────────────────────────
    // La barre disparaît **en entier**. Une première version n'en retirait
    // que les trois outils qui parlent à une IA — traduire, simplifier,
    // demander — et gardait « Lire » et « Prononcer » au motif que `dis()`
    // retombe sur la voix du navigateur. C'était vrai techniquement et faux
    // pédagogiquement : ces deux outils servent à donner un *modèle* de
    // prononciation, et une voix de synthèse du système en donne un mauvais,
    // que l'élève n'a aucun moyen de reconnaître comme tel. Sur bien des
    // postes il n'y a même pas de voix française.
    //
    // Le carnet et la révision, eux, n'ont jamais rien demandé à personne :
    // ils partent parce qu'un rail de deux outils, sur une page qui en
    // annonçait sept, se lit comme une panne. Une décision de centre doit se
    // voir comme une décision, pas comme un reste.
    sansIA: function () {
      if (SANS_IA) return;
      SANS_IA = true;
      fermer();
      // Ce que la barre avait posé dans la page hôte : les pastilles de
      // traduction des blocs et le bandeau de langue maternelle.
      document.querySelectorAll('.oe-tag, .oe-trad, .oe-lang, .oe-langbar')
        .forEach(function (n) { n.remove(); });
      // La mesure du rail publiait un jeton CSS dont les modules se servent
      // pour ne pas glisser leur banc de réponses sous la bande. Sans rail,
      // la réserve doit retomber à zéro, sinon il reste un vide en bas de
      // page sur téléphone.
      removeEventListener('resize', el.mesurerDock);
      removeEventListener('orientationchange', el.mesurerDock);
      if (el.dockRO) el.dockRO.disconnect();
      document.documentElement.style.setProperty('--oe-dock-h', '0px');
      document.body.classList.remove('oe-host', 'oe-cache');
      if (el.racine) el.racine.remove();
      if (el.tete) el.tete.remove();
      el = {};
    },
    rafraichirBlocs: marqueBlocs,

    // Un module qui a sa propre surcouche — les cartes mémoire du vocabulaire —
    // traduit par ici plutôt que de refaire la lecture de la langue choisie et
    // l'appel réseau. `langue()` rend null tant que l'élève n'a rien choisi :
    // c'est à l'appelant d'inviter au bandeau noir, en français.
    langue: langue,
    traduire: function (texte, contexte) {
      var L = langue();
      if (!cfg) return Promise.reject(new Error('Les outils ne sont pas encore prêts.'));
      if (!L) return Promise.reject(new Error('Choisissez d’abord votre langue maternelle, dans le bandeau noir en haut de la page.'));
      return poste('/api/outils/traduire', {
        langue: L.n, texte: propre(texte), contexte: contexte || cfg.section
      }).then(function (d) { return { texte: d.traduction, langue: L }; });
    }
  };
})(window);
