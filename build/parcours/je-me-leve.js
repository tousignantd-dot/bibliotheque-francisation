// ═══════════════════════════════════════════════════════════════════════════
// Point express — Je me lève, je me lave, je m'appelle
//
// Savoir n2-s24 (Indicatif présent : reconnaître et utiliser quelques verbes
// usuels), avec n2-s19 en arrière-plan. Une ORDONNANCE : l'enseignant l'envoie
// à un élève qui écrit « je lève à six heures » ou « je appelle Oksana ». Dix
// minutes, dix écrans, niveau 2.
//
// ── Ce qui le sépare de ce qui existe déjà ─────────────────────────────────
// Aucune mini-leçon du dépôt ne traite les verbes en « me, te, se » pour
// eux-mêmes, et c'est justement le problème : l'élève rencontre « je
// m'appelle » dès son premier cours, dans une formule à mémoriser, puis « je
// me lève » dans une routine, sans que le petit mot soit jamais expliqué. Il
// en conclut que « m' » fait partie du mot « appelle », et il écrit « je
// appelle » dès qu'il compose lui-même. Les cinq écarts tenus :
//
//   1. INDUCTIF. L'élève range huit phrases AVANT qu'on lui dise à quoi sert
//      le petit mot. La règle de l'écran 3 est le constat de son tri.
//   2. PARTIEL, JAMAIS LA LISTE. Aucun tableau de conjugaison. Un TEST —
//      l'action retombe-t-elle sur la personne qui la fait ? — qui marche sur
//      un verbe jamais vu, plus six verbes du quotidien.
//   3. LE MOT QUI CHANGE AVEC LA PERSONNE (me / te / se) EST DIT AVANT la
//      liste des verbes : c'est là qu'est la faute, pas dans le vocabulaire.
//   4. LE MÉTALANGAGE ARRIVE APRÈS. Aucun mot savant avant l'écran 3, et un
//      seul en tout.
//   5. EXEMPLES VARIÉS, JAMAIS CEUX D'UN MODULE. Une entrevue, un texto, une
//      note à l'école, un formulaire, un appel au comptoir.
//
// Aucun média : le petit mot s'entend très bien. Ce que l'élève ne fait pas,
// c'est l'écrire — et le choisir quand la personne change.
// ═══════════════════════════════════════════════════════════════════════════

const PARCOURS = {
  slug:     'je-me-leve',
  titre:    "Je me lève, je me lave, je m'appelle",
  surtitre: "Point express · 10 minutes",
  niveau:   2,
  savoir:   'n2-s24',
};

const ECRANS = [

  // ── 1. Une décision, sans aucune règle donnée. ───────────────────────────
  {
    id:   'depart',
    type: 'verif',
    eye:  'Une question, pour commencer',
    menu: 'Le matin',
    titre: "Vous racontez votre matinée. Quelle phrase écrivez-vous ?",
    consigne: "Répondez avec ce que vous savez déjà — ou au feeling. On expliquera après&nbsp;: "
            + "c'est fait exprès.",
    options: [
      { txt: "Je me lève à six heures.", juste: true },
      { txt: "Je lève à six heures.",
        rat_t: "C'est la phrase la plus courante chez les élèves de votre niveau.",
        rat: "Elle est logique&nbsp;: un sujet, un verbe, une heure. Mais «&nbsp;lever&nbsp;» "
           + "tout seul veut dire <b>soulever quelque chose</b>&nbsp;: je lève la main, je lève "
           + "une boîte. Pour dire que vous sortez du lit, il faut le petit mot <b>me</b>." },
      { txt: "Je me lever à six heures.",
        rat_t: "Le petit mot est bon. C'est la fin du verbe qui n'est pas la bonne.",
        rat: "«&nbsp;Lever&nbsp;» est la forme du dictionnaire. Avec «&nbsp;je&nbsp;», le verbe "
           + "change de fin&nbsp;: je <b>lève</b>. Vous le faites déjà sans y penser&nbsp;: je "
           + "parle, je travaille, je mange." },
    ],
    pourquoi: "«&nbsp;Je me lève à six heures.&nbsp;» Gardez cette phrase&nbsp;: on y revient au "
            + "dernier écran.",
    attente: "Choisissez une réponse pour continuer.",
  },

  // ── 2. On trie AVANT de savoir. ──────────────────────────────────────────
  {
    id:   'tri-sur-qui',
    type: 'tri',
    eye:  'À vous de trancher',
    menu: 'Huit phrases',
    titre: "Huit phrases correctes. Sur qui, ou sur quoi, tombe l'action ?",
    consigne: "Toutes ces phrases sont justes. Demandez-vous seulement&nbsp;: la personne fait "
            + "l'action <b>sur elle-même</b>, ou <b>sur autre chose</b>&nbsp;? Aucune règle ne "
            + "vous a été donnée — c'est normal.",
    colonnes: [
      { id: 'soi',   t: "Sur elle-même",  b: "Sur elle-même" },
      { id: 'autre', t: "Sur autre chose", b: "Sur autre chose" },
    ],
    items: [
      { txt: "Je lave la vaisselle après le souper.", sous: "un texto à une amie", ok: 'autre',
        rat: "Ce qui est lavé, c'est la vaisselle. L'action ne revient pas sur la personne qui "
           + "la fait.",
        pourquoi: "C'est la vaisselle qui est lavée." },
      { txt: "Je me lave les mains avant de manger.", sous: "à la garderie", ok: 'soi',
        rat: "Les mains sont les vôtres&nbsp;: l'action revient sur vous. C'est ce que dit le "
           + "petit mot <b>me</b>.",
        pourquoi: "Ce sont vos mains : l'action revient sur vous." },
      { txt: "Elle réveille son fils à sept heures.", sous: "une note à l'école", ok: 'autre',
        rat: "C'est le fils qui est réveillé, pas la mère. L'action va sur quelqu'un d'autre.",
        pourquoi: "C'est le fils qui est réveillé." },
      { txt: "Elle se réveille très tôt.", sous: "en entrevue", ok: 'soi',
        rat: "Personne ne la réveille&nbsp;: elle se réveille toute seule. Le petit mot "
           + "<b>se</b> le dit.",
        pourquoi: "Elle se réveille elle-même." },
      { txt: "J'appelle la clinique ce matin.", sous: "un message à son mari", ok: 'autre',
        rat: "Vous téléphonez à la clinique&nbsp;: l'action va vers l'extérieur.",
        pourquoi: "Vous appelez la clinique." },
      { txt: "Je m'appelle Oksana.", sous: "au comptoir d'un centre", ok: 'soi',
        rat: "Vous ne téléphonez à personne&nbsp;: vous dites le nom que vous portez. L'action "
           + "revient sur vous.",
        pourquoi: "C'est votre propre nom." },
      { txt: "Nous couchons les enfants à huit heures.", sous: "chez la voisine", ok: 'autre',
        rat: "Ce sont les enfants qu'on met au lit. L'action va sur eux.",
        pourquoi: "Ce sont les enfants qu'on couche." },
      { txt: "Le samedi, je me couche tard.", sous: "un texto", ok: 'soi',
        rat: "Personne ne vous couche&nbsp;: vous allez au lit vous-même. Encore le petit mot "
           + "<b>me</b>.",
        pourquoi: "Vous allez au lit vous-même." },
    ],
    attente: "Tranchez les huit phrases pour continuer.",
  },

  // ── 3. La règle, écrite comme un constat. ────────────────────────────────
  {
    id:   'le-constat',
    type: 'notion',
    eye:  'Ce que vous venez de faire',
    menu: 'Le test',
    titre: "Toutes vos phrases « sur elle-même » ont un petit mot devant le verbe.",
    paras: [
      "Relisez votre colonne de gauche&nbsp;: <b>me</b>, <b>me</b>, <b>se</b>, <b>m'</b>, "
      + "<b>me</b>. Ce petit mot ne veut rien dire tout seul. Il dit une seule chose&nbsp;: "
      + "<b>l'action revient sur la personne qui la fait</b>.",

      "Dans l'autre colonne, il n'y en a aucun, parce que l'action va ailleurs&nbsp;: sur la "
      + "vaisselle, sur le fils, sur la clinique.",

      "<b>Le test, à appliquer sur n'importe quel verbe&nbsp;:</b> demandez-vous qui reçoit "
      + "l'action. Si c'est la personne elle-même, mettez le petit mot devant le verbe. Sinon, "
      + "n'en mettez pas.",
    ],
    retenir: "L'action revient sur la personne&nbsp;: <b>un petit mot devant le verbe</b>. Sinon, "
           + "rien.",
    attente: "Lisez, puis continuez.",
  },

  // ── 4. Le mot change avec la personne. C'est là qu'est la faute. ─────────
  {
    id:   'le-mot-change',
    type: 'verif',
    eye:  'Le piège',
    menu: 'Le mot change',
    titre: "Vous parlez de votre fille. Quelle phrase écrivez-vous ?",
    consigne: "Vous voulez dire qu'elle sort du lit à sept heures. Une seule phrase "
            + "s'écrit.",
    options: [
      { txt: "Elle se lève à sept heures.", juste: true },
      { txt: "Elle me lève à sept heures.",
        rat_t: "Vous avez gardé le mot de «&nbsp;je me lève&nbsp;».",
        rat: "C'est très logique&nbsp;: vous aviez appris le verbe avec «&nbsp;me&nbsp;». Mais "
           + "ce petit mot suit la <b>personne</b>&nbsp;: <b>me</b> pour je, <b>te</b> pour tu, "
           + "<b>se</b> pour il et elle. Votre phrase dit en fait qu'elle vous soulève, vous." },
      { txt: "Elle lève à sept heures.",
        rat_t: "Sans petit mot, on attend de savoir ce qu'elle soulève.",
        rat: "«&nbsp;Lever&nbsp;» tout seul demande une suite&nbsp;: elle lève la main, elle "
           + "lève une boîte. Ici l'action revient sur elle&nbsp;: il faut le petit mot." },
    ],
    pourquoi: "<b>Je me · tu te · il se · elle se · nous nous · vous vous.</b> Le petit mot suit "
            + "la personne, jamais le verbe.",
    attente: "Choisissez une réponse pour continuer.",
  },

  // ── 5. Les verbes qui ne se disent jamais autrement. ─────────────────────
  {
    id:   'six-verbes',
    type: 'notion',
    eye:  'Le petit groupe',
    menu: 'Six verbes',
    titre: "Six verbes du quotidien, que vous emploierez chaque jour.",
    paras: [
      "<b>se lever</b> · <b>se laver</b> · <b>se coucher</b> · <b>se réveiller</b> · "
      + "<b>se dépêcher</b> · <b>s'appeler</b>. Je me lève, je me lave, je me couche, je me "
      + "réveille, je me dépêche, je m'appelle.",

      "Deux d'entre eux ne se disent <b>jamais</b> sans le petit mot&nbsp;: <b>se dépêcher</b> "
      + "et <b>s'appeler</b> au sens du nom. On ne dit pas «&nbsp;je dépêche&nbsp;», et "
      + "«&nbsp;j'appelle Oksana&nbsp;» veut dire que vous téléphonez à Oksana.",

      "Devant une voyelle, le petit mot perd sa lettre et prend une apostrophe&nbsp;: je "
      + "<b>m'</b>appelle, elle <b>s'</b>appelle, je <b>m'</b>habille. Comme «&nbsp;je&nbsp;» "
      + "devient «&nbsp;j'ai&nbsp;».",
    ],
    retenir: "Six verbes à reconnaître. Et devant une voyelle&nbsp;: <b>m'</b>, <b>t'</b>, "
           + "<b>s'</b>.",
    attente: "Lisez, puis continuez.",
  },

  // ── 6. Trier des phrases écrites. ────────────────────────────────────────
  {
    id:   'tri-ecrites',
    type: 'tri',
    eye:  'À vous de trancher',
    menu: 'Six phrases',
    titre: "Six phrases écrites. Lesquelles sont correctes ?",
    consigne: "Deux choses à regarder&nbsp;: le petit mot est-il là quand il faut, et est-il le "
            + "bon pour la personne&nbsp;?",
    colonnes: [
      { id: 'ok',   t: 'Correct',   b: 'Correct' },
      { id: 'faux', t: 'Une faute', b: 'Une faute' },
    ],
    items: [
      { txt: "Je m'appelle Ibrahim.", ok: 'ok',
        rat: "Le petit mot est là, et il perd sa lettre devant la voyelle. Rien à corriger.",
        pourquoi: "« m' » devant une voyelle. Juste." },
      { txt: "Mon fils se couche à huit heures.", ok: 'ok',
        rat: "L'action revient sur le fils, et <b>se</b> est le bon mot pour «&nbsp;il&nbsp;».",
        pourquoi: "« il » va avec « se ». Juste." },
      { txt: "Je lave les mains avant de manger.", ok: 'faux',
        rat: "Ce sont vos mains&nbsp;: l'action revient sur vous. Il faut «&nbsp;je <b>me</b> "
           + "lave les mains&nbsp;». Sans le petit mot, on comprend que vous lavez les mains de "
           + "quelqu'un d'autre.",
        pourquoi: "Il faut « je me lave les mains »." },
      { txt: "Elle me réveille toujours à six heures.", ok: 'ok',
        rat: "Attention, celle-ci est un piège&nbsp;: elle est correcte, mais elle veut dire que "
           + "c'est <b>elle</b> qui vous réveille, vous. Le petit mot dit sur qui tombe l'action, "
           + "et ici c'est bien vous.",
        pourquoi: "Correcte : c'est elle qui vous réveille." },
      { txt: "Nous se dépêchons le matin.", ok: 'faux',
        rat: "Le verbe est bon, le petit mot ne l'est pas&nbsp;: avec «&nbsp;nous&nbsp;», on "
           + "écrit «&nbsp;nous <b>nous</b> dépêchons&nbsp;». Le mot répété paraît étrange, et "
           + "c'est pourtant la bonne forme.",
        pourquoi: "Il faut « nous nous dépêchons »." },
      { txt: "Tu te lèves à quelle heure ?", ok: 'ok',
        rat: "Avec «&nbsp;tu&nbsp;», le petit mot est <b>te</b>. La question est correcte telle "
           + "quelle.",
        pourquoi: "« tu » va avec « te ». Juste." },
    ],
    attente: "Tranchez les six phrases pour continuer.",
  },

  // ── 7. Dire non : où se glisse le petit mot. ─────────────────────────────
  {
    id:   'dire-non',
    type: 'verif',
    eye:  'Vérification',
    menu: 'Dire non',
    titre: "Le dimanche, vous ne sortez pas du lit tôt. Comment l'écrivez-vous ?",
    consigne: "Vous écrivez à une amie qui propose de déjeuner à sept heures le dimanche.",
    options: [
      { txt: "Le dimanche, je ne me lève pas tôt.", juste: true },
      { txt: "Le dimanche, je me ne lève pas tôt.",
        rat_t: "Vous avez gardé le petit mot collé à «&nbsp;je&nbsp;».",
        rat: "Ces deux petits mots ont un ordre fixe et il ne bouge jamais&nbsp;: <b>ne</b> "
           + "d'abord, puis <b>me</b>, puis le verbe. «&nbsp;Je <b>ne me</b> lève pas.&nbsp;»" },
      { txt: "Le dimanche, je ne lève pas tôt.",
        rat_t: "En ajoutant la négation, vous avez perdu le petit mot.",
        rat: "C'est ce qui arrive presque toujours&nbsp;: la phrase s'allonge, et le mot le plus "
           + "court disparaît. L'action revient toujours sur vous&nbsp;: «&nbsp;je ne <b>me</b> "
           + "lève pas&nbsp;»." },
    ],
    pourquoi: "<b>ne · me · le verbe.</b> Le petit mot reste collé au verbe, quoi qu'on mette "
            + "devant.",
    attente: "Choisissez une réponse pour continuer.",
  },

  // ── 8. Après « je dois » et « je peux » : dit en dernier, rien de neuf. ──
  {
    id:   'apres-devoir',
    type: 'notion',
    eye:  'Ce qui reste',
    menu: 'Je dois me…',
    titre: "Après « je dois » et « je peux », le petit mot ne change pas de règle.",
    paras: [
      "«&nbsp;Je dois <b>me</b> lever tôt demain.&nbsp;» «&nbsp;Est-ce que je peux <b>me</b> "
      + "laver les mains&nbsp;?&nbsp;» Le verbe reprend sa forme du dictionnaire — lever, laver "
      + "— mais le petit mot, lui, <b>suit toujours la personne</b>&nbsp;: c'est «&nbsp;je&nbsp;», "
      + "donc c'est <b>me</b>.",

      "«&nbsp;Elle doit <b>se</b> dépêcher.&nbsp;» «&nbsp;Vous pouvez <b>vous</b> "
      + "asseoir.&nbsp;» Même chose&nbsp;: le mot regarde qui parle, jamais le verbe qui suit.",

      "Ces verbes-là s'appellent des <b>verbes pronominaux</b>. Votre enseignant emploiera ce "
      + "mot. Vous n'en avez pas besoin&nbsp;: vous avez le test, et il vaut pour tous.",
    ],
    retenir: "Le petit mot suit <b>la personne qui parle</b>, où qu'il se trouve dans la phrase.",
    attente: "Lisez, puis continuez.",
  },

  // ── 9. Écrire, pas reconnaître. ──────────────────────────────────────────
  {
    id:   'votre-message',
    type: 'verif',
    eye:  'Vérification',
    menu: 'Votre message',
    titre: "Marta écrit à son enseignante. Quelle version tient d'un bout à l'autre ?",
    consigne: "Elle explique pourquoi elle arrive parfois en retard le lundi.",
    options: [
      { txt: "Le lundi, je me lève à cinq heures et je réveille mes enfants. Après, nous nous "
           + "dépêchons.", juste: true },
      { txt: "Le lundi, je lève à cinq heures et je me réveille mes enfants. Après, nous nous "
           + "dépêchons.",
        rat_t: "La fin est parfaite. Les deux premiers verbes sont inversés.",
        rat: "C'est vous qui sortez du lit&nbsp;: «&nbsp;je <b>me</b> lève&nbsp;». Et ce sont "
           + "<b>les enfants</b> qui sont réveillés, pas vous&nbsp;: «&nbsp;je réveille mes "
           + "enfants&nbsp;», sans petit mot. Le test tranche les deux d'un coup." },
      { txt: "Le lundi, je me lève à cinq heures et je réveille mes enfants. Après, nous se "
           + "dépêchons.",
        rat_t: "Les deux premiers verbes sont justes. C'est la dernière phrase qui a lâché.",
        rat: "Avec «&nbsp;nous&nbsp;», le petit mot est <b>nous</b>, lui aussi&nbsp;: "
           + "«&nbsp;nous <b>nous</b> dépêchons&nbsp;». C'est la forme qui paraît la plus "
           + "bizarre, et c'est pourtant la bonne." },
    ],
    pourquoi: "Un petit mot quand l'action revient sur la personne, aucun quand elle va sur "
            + "quelqu'un d'autre. <b>C'est tout le point en deux phrases.</b>",
    attente: "Choisissez une réponse pour continuer.",
  },

  // ── 10. La fermeture : le cas de l'écran 1. ──────────────────────────────
  {
    id:   'fermeture',
    type: 'verif',
    eye:  'La dernière',
    menu: 'Pour finir',
    titre: "On revient au début : « Je me lève à six heures. »",
    consigne: "Cette fois, vous parlez de votre mari, et vous ajoutez une chose&nbsp;: il doit "
            + "partir tôt. Quelle version&nbsp;?",
    options: [
      { txt: "Il se lève à six heures. Il doit se dépêcher.", juste: true },
      { txt: "Il me lève à six heures. Il doit me dépêcher.",
        rat_t: "Vous avez gardé le petit mot de la phrase du début.",
        rat: "«&nbsp;Me&nbsp;» va avec «&nbsp;je&nbsp;». Ici, c'est <b>il</b>&nbsp;: le petit mot "
           + "devient <b>se</b>, dans les deux phrases. Votre version dit qu'il vous soulève et "
           + "qu'il vous presse, vous." },
      { txt: "Il se lève à six heures. Il doit dépêcher.",
        rat_t: "La première phrase est parfaite. Le petit mot a disparu de la seconde.",
        rat: "«&nbsp;Dépêcher&nbsp;» ne se dit jamais seul&nbsp;: c'est un des deux verbes de "
           + "l'écran des six. Après «&nbsp;il doit&nbsp;», le petit mot reste et suit la "
           + "personne&nbsp;: «&nbsp;il doit <b>se</b> dépêcher&nbsp;»." },
    ],
    pourquoi: "Vous avez fait les deux choses&nbsp;: reconnaître que l'action revient sur la "
            + "personne, et changer le petit mot quand la personne change.",
    attente: "Choisissez une réponse pour finir.",
  },

];
