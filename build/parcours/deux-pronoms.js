// ═══════════════════════════════════════════════════════════════════════════
// Point express — « Je vous le confirme » : deux pronoms d'affilée
//
// Savoir n5-s24. Dix minutes, dix écrans.
//
// ── L'écart avec les mini-leçons ───────────────────────────────────────────
//   1. Les mini-leçons de pronoms enseignent à PRODUIRE. Ce point express
//      part de la COMPRÉHENSION : un élève de niveau 5 se fait comprendre
//      sans placer ses pronoms, mais il n'entend pas ce qu'on lui dit quand
//      l'agente en enfile deux. La panne est à l'écoute, et c'est par là
//      qu'on entre.
//   2. Aucune table « me te se nous vous / le la les / lui leur » : c'est ce
//      que font les manuels, et c'est ce qu'on récite sans savoir s'en servir.
//      Ici, une seule question — « ce mot remplace une CHOSE ou une
//      PERSONNE ? » — et l'ordre se déduit.
//   3. Le métalangage (« complément direct », « indirect ») n'apparaît qu'à
//      l'écran 6, une fois la distinction faite à l'oreille.
//
// Extraits : module-n5-rendezvous. Les phrases de Manon en sont pleines —
// c'est le parler d'un comptoir. Aucun média neuf.
// ═══════════════════════════════════════════════════════════════════════════

const PARCOURS = {
  slug:     'deux-pronoms',
  module:   'module-n5-rendezvous',
  titre:    "« Je vous le confirme » : deux pronoms d'affilée",
  surtitre: "Point express · 10 minutes",
  niveau:   5,
  savoir:   'n5-s24',
};

const ECRANS = [

  // ── 1. Comprendre avant de produire. ─────────────────────────────────────
  {
    id:   'depart',
    type: 'verif',
    eye:  'Une question, pour commencer',
    menu: 'Qui reçoit quoi',
    titre: "« Je vous l'envoie demain. » Qu'est-ce que l'agente envoie, et à qui ?",
    consigne: "La phrase ne contient ni le nom de la chose, ni le nom de la personne. Et "
            + "pourtant tout est dit.",
    options: [
      { txt: "Elle envoie une chose à vous.", juste: true },
      { txt: "Elle vous envoie chez quelqu'un.",
        rat_t: "Il y a deux mots, et chacun a son rôle.",
        rat: "<b>Vous</b> est la personne qui reçoit&nbsp;; <b>l'</b> est la chose envoyée — un "
           + "reçu, un formulaire, un rappel. Personne ne va nulle part." },
      { txt: "On ne peut pas savoir sans le contexte.",
        rat_t: "Le contexte dit <i>quoi</i>, la phrase dit déjà <i>qui</i>.",
        rat: "C'est vrai qu'on ignore ce qu'est «&nbsp;l'&nbsp;»&nbsp;: il faut avoir suivi la "
           + "conversation. Mais la <b>structure</b>, elle, est claire — une chose part vers "
           + "vous. C'est déjà l'essentiel, et c'est ce qui manque quand on décroche." },
    ],
    pourquoi: "Deux petits mots, deux rôles&nbsp;: <b>vous</b> = la personne, <b>l'</b> = la "
            + "chose. Le français les colle l'un à l'autre, et c'est là que l'oreille lâche.",
    attente: "Choisissez une réponse pour continuer.",
  },

  // ── 2. Écouter : c'est le parler d'un comptoir. ──────────────────────────
  {
    id:   'au-comptoir',
    type: 'notion',
    eye:  'Écoutez',
    menu: 'Le parler du comptoir',
    titre: "Ce n'est pas de la grammaire de manuel. C'est la façon dont on vous parle.",
    paras: [
      "Une agente qui prend trente appels par jour ne répète pas les noms&nbsp;: elle les "
      + "remplace, et elle enchaîne. «&nbsp;Je <b>vous</b> <b>la</b> réserve&nbsp;», "
      + "«&nbsp;je <b>vous</b> <b>le</b> confirme&nbsp;», «&nbsp;on <b>vous</b> <b>l'</b>envoie"
      + "&nbsp;». C'est rapide, c'est normal, et ça ne s'apprend nulle part.",
      "Écoutez Manon. Elle dit <i>vous</i> deux fois dans la même réplique, et pas pour la "
      + "même raison.",
    ],
    sons: [
      { fichier: 't1/line_11_manon.mp3', qui: 'Manon',
        texte: "D'accord. Trois mois, ce n'est pas rien. Je vous mets une plage de trente "
             + "minutes plutôt que quinze." },
    ],
    retenir: "Quand on vous parle vite, <b>les noms disparaissent</b>. Reconnaître les petits "
           + "mots qui les remplacent, c'est comprendre l'appel.",
    attente: "Écoutez, puis continuez.",
  },

  // ── 3. Trier : une chose ou une personne. ────────────────────────────────
  {
    id:   'tri-chose-personne',
    type: 'tri',
    eye:  'À vous de trancher',
    menu: 'Chose ou personne',
    titre: "Dans chaque phrase, le mot en gras remplace quoi ?",
    consigne: "Une seule question à se poser, et aucune règle n'est nécessaire&nbsp;: "
            + "est-ce que ce mot désigne <b>quelque chose</b> ou <b>quelqu'un</b>&nbsp;?",
    colonnes: [
      { id: 'chose',    t: 'Une chose',   b: 'Une chose' },
      { id: 'personne', t: 'Une personne', b: 'Une personne' },
    ],
    items: [
      { txt: "Je <b>la</b> réserve pour jeudi.", sous: "la plage horaire", ok: 'chose',
        rat: "Une plage horaire n'est pas quelqu'un. <i>La</i> remplace la chose dont on vient "
           + "de parler.",
        pourquoi: "La plage horaire. Une chose." },
      { txt: "Je <b>lui</b> ai parlé ce matin.", sous: "à la docteure Fongang", ok: 'personne',
        rat: "On parle <i>à</i> quelqu'un&nbsp;: <b>lui</b> ne remplace jamais une chose. C'est "
           + "l'un des rares mots dont le rôle est absolument fixe.",
        pourquoi: "À la médecin. Une personne." },
      { txt: "Vous <b>le</b> recevrez la veille.", sous: "le rappel automatisé", ok: 'chose',
        rat: "Le rappel est un message, donc une chose. Attention&nbsp;: <i>le</i> peut aussi "
           + "désigner un homme — «&nbsp;je <b>le</b> vois demain&nbsp;» — et c'est la seule "
           + "ambiguïté de tout le système.",
        pourquoi: "Le rappel. Une chose (mais « le » peut aussi être un homme)." },
      { txt: "Je <b>vous</b> rappelle demain.", sous: "à vous", ok: 'personne',
        rat: "<i>Vous</i> désigne toujours des personnes. Ce mot-là ne pose jamais de problème "
           + "de rôle&nbsp;: seulement de <b>place</b>, et on y vient.",
        pourquoi: "Vous. Toujours une personne." },
      { txt: "Il faut <b>les</b> apporter.", sous: "vos médicaments", ok: 'chose',
        rat: "Des médicaments. <i>Les</i>, comme <i>le</i> et <i>la</i>, remplace le plus "
           + "souvent une chose — mais peut aussi désigner des personnes.",
        pourquoi: "Les médicaments. Une chose." },
      { txt: "On <b>leur</b> a envoyé le formulaire.", sous: "aux parents", ok: 'personne',
        rat: "<i>Leur</i> est le pluriel de <i>lui</i>&nbsp;: des personnes à qui l'on envoie "
           + "quelque chose. Comme <i>lui</i>, son rôle est fixe.",
        pourquoi: "Aux parents. Des personnes." },
    ],
    attente: "Tranchez les six phrases pour continuer.",
  },

  // ── 4. La règle d'ordre, tirée du tri. ───────────────────────────────────
  {
    id:   'l-ordre',
    type: 'notion',
    eye:  'Ce que vous venez de faire',
    menu: "L'ordre",
    titre: "Vous avez séparé les personnes des choses. L'ordre en découle.",
    paras: [
      "Regardez vos deux colonnes. Dans la colonne «&nbsp;personne&nbsp;», vous avez trouvé "
      + "<i>vous</i>, <i>lui</i>, <i>leur</i>. Dans l'autre, <i>le</i>, <i>la</i>, <i>les</i>. "
      + "Ce sont les deux familles, et vous venez de les former sans qu'on vous les donne.",
      "<b>La règle&nbsp;: quand les deux se suivent, «&nbsp;me, te, nous, vous&nbsp;» passent "
      + "devant.</b> «&nbsp;Je <b>vous</b> <b>le</b> confirme&nbsp;», «&nbsp;on <b>me</b> "
      + "<b>l'</b>a dit&nbsp;», «&nbsp;il <b>nous</b> <b>les</b> envoie&nbsp;». La personne à "
      + "qui l'on parle vient toujours en premier.",
      "Il n'y a qu'une exception, et elle est facile à repérer&nbsp;: avec <b>lui</b> et "
      + "<b>leur</b>, c'est l'inverse — «&nbsp;je <b>le</b> <b>lui</b> confirme&nbsp;», "
      + "«&nbsp;on <b>les</b> <b>leur</b> a envoyés&nbsp;». Ces deux mots-là passent derrière.",
    ],
    retenir: "<b>Vous</b> devant, <b>lui</b> derrière. Deux mots à retenir, pas une table.",
    attente: "Lisez, puis continuez.",
  },

  // ── 5. Vérification sur l'ordre. ─────────────────────────────────────────
  {
    id:   'verif-ordre',
    type: 'verif',
    eye:  'Vérification',
    menu: 'Dans quel ordre',
    titre: "Vous confirmez le rendez-vous à la personne à qui vous parlez. Vous dites quoi ?",
    consigne: "La chose confirmée est <i>le rendez-vous</i>&nbsp;; la personne est celle au "
            + "bout du fil.",
    options: [
      { txt: "« Je vous le confirme. »", juste: true },
      { txt: "« Je le vous confirme. »",
        rat_t: "L'ordre est inversé.",
        rat: "«&nbsp;Vous&nbsp;» fait partie des quatre qui passent devant — me, te, nous, vous. "
           + "Cette phrase-là ne se dit pas, et c'est un des rares endroits où l'oreille d'un "
           + "francophone tique tout de suite." },
      { txt: "« Je vous confirme le. »",
        rat_t: "Un pronom ne se met jamais après le verbe ici.",
        rat: "Les deux petits mots viennent <b>avant</b> le verbe, collés à lui&nbsp;: c'est ce "
           + "qui les rend difficiles à entendre. Après le verbe, on remettrait le nom entier — "
           + "«&nbsp;je vous confirme <i>le rendez-vous</i>&nbsp;», qui est correct aussi." },
    ],
    pourquoi: "<b>Vous</b> devant, <b>le</b> derrière, et les deux avant le verbe. "
            + "«&nbsp;Je vous le confirme.&nbsp;»",
    attente: "Choisissez une réponse pour continuer.",
  },

  // ── 6. Le métalangage arrive ici, et seulement ici. ──────────────────────
  {
    id:   'les-noms',
    type: 'notion',
    eye:  'Les mots de l\'enseignant',
    menu: 'Les deux noms',
    titre: "Votre enseignant appellera ça « direct » et « indirect ».",
    paras: [
      "Vous n'en avez pas eu besoin jusqu'ici, et c'est voulu. Mais vous entendrez ces mots en "
      + "classe, alors autant les poser maintenant que la chose est claire.",
      "Ce qui subit l'action directement — la chose — est le <b>complément direct</b>&nbsp;: "
      + "<i>le, la, les</i>. Ce qui reçoit, à qui l'on donne, se dit avec «&nbsp;à&nbsp;» et "
      + "s'appelle <b>complément indirect</b>&nbsp;: <i>lui, leur</i>.",
      "Le repère qui marche&nbsp;: si vous pouvez remettre «&nbsp;<b>à</b>&nbsp;» devant le nom, "
      + "c'est indirect. <i>Je parle <b>à</b> la médecin</i> → je <b>lui</b> parle. "
      + "<i>Je confirme le rendez-vous</i> → je <b>le</b> confirme.",
    ],
    retenir: "Le mot «&nbsp;<b>à</b>&nbsp;» est le test. S'il peut revenir, c'est "
           + "<i>lui</i>&nbsp;/&nbsp;<i>leur</i>.",
    attente: "Lisez, puis continuez.",
  },

  // ── 7. Trier avec le test du « à ». ──────────────────────────────────────
  {
    id:   'tri-a',
    type: 'tri',
    eye:  'À vous de trancher',
    menu: 'Le test du « à »',
    titre: "Remettez le nom. Est-ce qu'il faut « à » devant ?",
    consigne: "C'est le seul test à retenir, et il tranche à chaque fois.",
    colonnes: [
      { id: 'avec', t: 'Avec « à »',  b: 'Avec « à »' },
      { id: 'sans', t: 'Sans « à »',  b: 'Sans « à »' },
    ],
    items: [
      { txt: "Je téléphone … la clinique.", ok: 'avec',
        rat: "On téléphone <b>à</b> quelqu'un. D'où «&nbsp;je <b>lui</b> téléphone&nbsp;» — et "
           + "jamais «&nbsp;je la téléphone&nbsp;», qui est la faute la plus fréquente de ce "
           + "verbe.",
        pourquoi: "Téléphoner À. Donc : je lui téléphone." },
      { txt: "J'annule … mon rendez-vous.", ok: 'sans',
        rat: "On annule quelque chose, directement. «&nbsp;Je <b>l'</b>annule&nbsp;».",
        pourquoi: "Annuler quelque chose. Donc : je l'annule." },
      { txt: "Je demande … l'agente.", ok: 'avec',
        rat: "On demande quelque chose <b>à</b> quelqu'un&nbsp;: «&nbsp;je <b>lui</b> demande&nbsp;». "
           + "Attention — «&nbsp;je <b>la</b> demande&nbsp;» existe aussi, mais veut dire "
           + "«&nbsp;je demande à lui parler&nbsp;». Deux phrases, deux sens.",
        pourquoi: "Demander À quelqu'un. Donc : je lui demande." },
      { txt: "J'apporte … la liste.", ok: 'sans',
        rat: "On apporte une chose&nbsp;: «&nbsp;je <b>l'</b>apporte&nbsp;». Si on ajoute la "
           + "personne, elle prend le «&nbsp;à&nbsp;»&nbsp;: je <b>la lui</b> apporte.",
        pourquoi: "Apporter quelque chose. Donc : je l'apporte." },
      { txt: "Je réponds … la secrétaire.", ok: 'avec',
        rat: "On répond <b>à</b> quelqu'un — un des verbes qui piègent le plus, parce que dans "
           + "plusieurs langues il est direct. «&nbsp;Je <b>lui</b> réponds&nbsp;».",
        pourquoi: "Répondre À. Donc : je lui réponds." },
    ],
    attente: "Tranchez les cinq verbes pour continuer.",
  },

  // ── 8. Le vrai enjeu : à l'écoute. ───────────────────────────────────────
  {
    id:   'a-l-ecoute',
    type: 'verif',
    eye:  'Vérification',
    menu: 'Ce qu\'on vous dit',
    titre: "L'agente dit : « Je le lui transmets ce matin. » Qui fait quoi ?",
    consigne: "Rien n'est nommé. Deux petits mots, et il faut suivre.",
    options: [
      { txt: "Elle transmet une chose à une autre personne — pas à vous.", juste: true },
      { txt: "Elle vous transmet quelque chose.",
        rat_t: "Elle aurait dit «&nbsp;je <b>vous</b> le transmets&nbsp;».",
        rat: "C'est exactement l'information qui se perd quand on n'entend pas ces mots-là. "
           + "<b>Lui</b>, ce n'est pas vous&nbsp;: c'est une troisième personne — la médecin, "
           + "un collègue. Vous, dans cette phrase, vous n'y êtes pas." },
      { txt: "Elle transmet deux choses.",
        rat_t: "Les deux mots n'ont pas le même rôle.",
        rat: "<b>Le</b> est la chose transmise&nbsp;; <b>lui</b> est la personne qui la reçoit. "
           + "Le test du «&nbsp;à&nbsp;»&nbsp;: on transmet quelque chose <i>à</i> quelqu'un." },
    ],
    pourquoi: "<b>Le</b> = la chose, <b>lui</b> = la personne, et ce n'est pas vous. "
            + "Comprendre ça, c'est savoir s'il faut rappeler demain ou attendre.",
    attente: "Choisissez une réponse pour continuer.",
  },

  // ── 9. Produire, à l'écrit. ──────────────────────────────────────────────
  {
    id:   'ecrire',
    type: 'verif',
    eye:  'Vérification',
    menu: 'Écrire à la clinique',
    titre: "Vous écrivez : vous avez envoyé les documents à la secrétaire. Quelle phrase ?",
    consigne: "Deux pronoms, et il faut choisir l'ordre.",
    options: [
      { txt: "« Je les lui ai envoyés hier. »", juste: true },
      { txt: "« Je lui les ai envoyés hier. »",
        rat_t: "L'ordre est inversé.",
        rat: "<i>Lui</i> et <i>leur</i> sont les deux seuls qui passent <b>derrière</b> la "
           + "chose. C'est l'exception de l'écran 4, et c'est la seule qu'il y ait à retenir." },
      { txt: "« Je les ai envoyés à elle hier. »",
        rat_t: "Compréhensible, mais ce n'est pas du français courant.",
        rat: "«&nbsp;À elle&nbsp;» ne s'emploie que pour insister — «&nbsp;c'est à <b>elle</b> "
           + "que je les ai envoyés&nbsp;». Dans une phrase ordinaire, on emploie <i>lui</i>, "
           + "qui vaut pour un homme comme pour une femme." },
    ],
    pourquoi: "<b>Les</b> (la chose) puis <b>lui</b> (la personne)&nbsp;: l'exception. "
            + "Et le participe s'accorde — <i>envoyé<b>s</b></i> — parce que la chose est devant.",
    attente: "Choisissez une réponse pour continuer.",
  },

  // ── 10. Fermeture. ───────────────────────────────────────────────────────
  {
    id:   'fermeture',
    type: 'verif',
    eye:  'La dernière',
    menu: 'Pour finir',
    titre: "On revient au début. L'agente veut vous envoyer le reçu, à vous.",
    consigne: "Quelle phrase entendrez-vous&nbsp;?",
    options: [
      { txt: "« Je vous l'envoie tout de suite. »", juste: true },
      { txt: "« Je le vous envoie tout de suite. »",
        rat_t: "L'ordre, encore.",
        rat: "<i>Vous</i> passe devant — c'est la règle générale, celle des quatre "
           + "(me, te, nous, vous). L'exception ne concerne que <i>lui</i> et <i>leur</i>." },
      { txt: "« Je le lui envoie tout de suite. »",
        rat_t: "Juste, mais ce n'est plus vous qui recevez.",
        rat: "La phrase est parfaitement correcte&nbsp;— elle dit simplement que le reçu part "
           + "vers <b>quelqu'un d'autre</b>. C'est exactement le genre de détail qui fait "
           + "attendre un document qui n'arrivera jamais." },
    ],
    pourquoi: "<b>Vous</b> devant, la chose derrière. Vous savez maintenant faire les deux "
            + "choses&nbsp;: entendre à qui va quoi, et le dire dans le bon ordre.",
    attente: "Choisissez une réponse pour finir.",
  },

];
