// ═══════════════════════════════════════════════════════════════════════════
// Point express — ce, cet, cette — trois mots, un seul son
//
// Savoirs n3-s15 (déterminants démonstratifs : accorder ce, cet, cette, ces)
// et n3-s16, qui donne lui-même la clé phonétique du point : « Connais-tu ce
// [stə] gars-là ? Connais-tu c(et)te [stə] fille-là ? J'aime c(e)t [st]
// appartement-là. » Dix minutes, dix écrans. Une ORDONNANCE : l'enseignant
// l'envoie à l'élève qui écrit « cet école », « cette manteau », « ce
// appartement ».
//
// Le point tient sur un constat que les mini-leçons n'osent pas dire en
// entier : au Québec, ce, cet et cette se prononcent PAREIL — [stə] devant
// une consonne, [st] devant une voyelle. L'oreille ne peut donc rien pour
// l'élève. Ce qui décide est le nom, et rien d'autre.
//
// ── Ce qui le sépare des mini-leçons existantes ────────────────────────────
// Deux existent, et l'élève en a probablement lu une :
//   · `module-n3-metro`, « Ce, cet, cette, ces — montrer une chose du doigt » :
//     les quatre formes une par une, puis le « -là » du Québec. Elle dit que
//     « cet se prononce comme cette », et s'arrête là.
//   · `module-n3-electro`, « Montrer un appareil : ce, cet, cette, ces » :
//     même plan, au rayon des électroménagers.
// Aucune des deux ne dit que « ce » sonne comme les deux autres — c'est
// pourtant la seule raison pour laquelle la faute survit. Les cinq écarts :
//
//   1. INDUCTIF. Aucune règle avant l'écran 3. L'élève range six noms dans
//      trois colonnes, et la règle de l'écran 3 est le constat de la méthode
//      qu'il vient d'employer sans le savoir.
//   2. PARTIEL, JAMAIS LES QUATRE FORMES EN TABLEAU. Ici, un TEST emprunté à
//      ce que l'élève sait déjà : « est-ce que je dis un ou une devant ce
//      mot ? » Il marche sur un nom rencontré pour la première fois, ce qu'un
//      tableau de formes ne permet pas.
//   3. « CES » EST DIT EN DERNIER (écran 8). Les mini-leçons l'annoncent en
//      quatrième ligne, à égalité avec les autres. Or c'est le cas où il n'y a
//      RIEN à décider : le nommer tôt fait croire à quatre choix quand il n'y
//      en a que trois, et seulement au singulier.
//   4. LE MÉTALANGAGE APRÈS. « Déterminant démonstratif » n'est écrit qu'à
//      l'écran 3, une fois six noms triés.
//   5. EXEMPLES VARIÉS, JAMAIS UN MAGASIN. Les deux mini-leçons se passent au
//      guichet et au rayon ; ici, un formulaire, une note à l'école, un message
//      à un propriétaire, un horaire de travail.
//
// Aucun média, et c'est le sujet même du point : la différence ne s'entend
// pas. Un extrait sonore ferait croire qu'il y a quelque chose à écouter. Les
// prononciations sont donc écrites en toutes lettres — « stə », « st » — et
// jamais en alphabet phonétique, qu'un élève de niveau 3 ne lit pas.
// ═══════════════════════════════════════════════════════════════════════════

const PARCOURS = {
  slug:     'ce-cet-cette',
  titre:    "ce, cet, cette — trois mots, un seul son",
  surtitre: "Point express · 10 minutes",
  niveau:   3,
  savoir:   'n3-s15 · n3-s16',
};

const ECRANS = [

  // ── 1. Une décision, sans aucune règle donnée. ───────────────────────────
  {
    id:   'depart',
    type: 'verif',
    eye:  'Une question, pour commencer',
    menu: 'Le manteau',
    titre: "Vous entendez : « Je vais prendre ste manteau-là. »",
    consigne: "Vous devez l'écrire dans une note. Comment s'écrit le petit mot qu'on "
            + "entend «&nbsp;ste&nbsp;»&nbsp;? Répondez avec ce que vous savez déjà — "
            + "c'est fait exprès.",
    options: [
      { txt: "ce manteau-là", juste: true },
      { txt: "cette manteau-là",
        rat_t: "L'oreille vous a dit «&nbsp;ste&nbsp;». Elle dit la même chose pour les deux.",
        rat: "Ici, «&nbsp;ce&nbsp;» et «&nbsp;cette&nbsp;» se prononcent exactement "
           + "pareil&nbsp;: «&nbsp;ste&nbsp;». Vous ne pouviez pas choisir avec l'oreille. "
           + "Il faut regarder le nom&nbsp;: on dit «&nbsp;<b>un</b> manteau&nbsp;»." },
      { txt: "cet manteau-là",
        rat_t: "«&nbsp;cet&nbsp;» existe, mais pas devant ce mot-là.",
        rat: "«&nbsp;cet&nbsp;» ne s'écrit que devant un mot qui commence par une "
           + "voyelle — cet horaire, cet appartement. «&nbsp;Manteau&nbsp;» commence "
           + "par un <i>m</i>." },
    ],
    pourquoi: "«&nbsp;<b>ce</b> manteau-là&nbsp;». Vous n'avez pas choisi avec "
            + "l'oreille&nbsp;: c'est impossible. Vous allez voir avec quoi.",
    attente: "Choisissez une réponse pour continuer.",
  },

  // ── 2. On trie AVANT de savoir. ──────────────────────────────────────────
  {
    id:   'tri-noms',
    type: 'tri',
    eye:  'À vous de trancher',
    menu: 'Six noms',
    titre: "Six noms. Quel petit mot se met devant ?",
    consigne: "Aucune règle ne vous a été donnée — normal. Chaque nom est écrit avec "
            + "«&nbsp;un&nbsp;» ou «&nbsp;une&nbsp;», que vous connaissez déjà. "
            + "Servez-vous-en.",
    colonnes: [
      { id: 'ce',    t: 'ce',    b: 'ce' },
      { id: 'cet',   t: 'cet',   b: 'cet' },
      { id: 'cette', t: 'cette', b: 'cette' },
    ],
    items: [
      { txt: "formulaire", sous: "un formulaire", ok: 'ce',
        rat: "On dit «&nbsp;un formulaire&nbsp;», et le mot commence par une consonne&nbsp;: "
           + "c'est «&nbsp;<b>ce</b> formulaire&nbsp;».",
        pourquoi: "un formulaire → ce formulaire." },
      { txt: "adresse", sous: "une adresse", ok: 'cette',
        rat: "Le mot commence par une voyelle, et c'est ce qui vous a fait hésiter. "
           + "Mais on dit «&nbsp;<b>une</b> adresse&nbsp;»&nbsp;: c'est "
           + "«&nbsp;<b>cette</b> adresse&nbsp;». La voyelle ne change rien ici.",
        pourquoi: "une adresse → cette adresse." },
      { txt: "horaire", sous: "un horaire", ok: 'cet',
        rat: "On dit «&nbsp;un horaire&nbsp;», et le <i>h</i> ne s'entend pas&nbsp;: "
           + "le mot commence donc par un son de voyelle. C'est «&nbsp;<b>cet</b> "
           + "horaire&nbsp;».",
        pourquoi: "un horaire, h muet → cet horaire." },
      { txt: "semaine", sous: "une semaine", ok: 'cette',
        rat: "On dit «&nbsp;une semaine&nbsp;»&nbsp;: c'est «&nbsp;<b>cette</b> "
           + "semaine&nbsp;».",
        pourquoi: "une semaine → cette semaine." },
      { txt: "appartement", sous: "un appartement", ok: 'cet',
        rat: "On dit «&nbsp;un appartement&nbsp;», et le mot commence par une "
           + "voyelle&nbsp;: c'est «&nbsp;<b>cet</b> appartement&nbsp;». "
           + "«&nbsp;Ce appartement&nbsp;» ne se dit pas.",
        pourquoi: "un appartement, voyelle → cet appartement." },
      { txt: "école", sous: "une école", ok: 'cette',
        rat: "Le mot commence par une voyelle, alors «&nbsp;cet&nbsp;» est très "
           + "tentant. Mais on dit «&nbsp;<b>une</b> école&nbsp;»&nbsp;: c'est "
           + "«&nbsp;<b>cette</b> école&nbsp;». La voyelle ne décide qu'après le "
           + "masculin et le féminin.",
        pourquoi: "une école → cette école." },
    ],
    attente: "Tranchez les six noms pour continuer.",
  },

  // ── 3. La règle, écrite comme un constat. Le métalangage arrive ici. ─────
  {
    id:   'le-test',
    type: 'notion',
    eye:  'Ce que vous venez de faire',
    menu: 'Le test',
    titre: "Vous n'avez pas deviné : vous avez lu « un » ou « une ».",
    paras: [
      "Regardez ce que vous avez fait six fois de suite. Vous avez lu le petit mot "
      + "déjà là — <i>un</i> ou <i>une</i> — et il vous a donné la réponse. C'est tout "
      + "le point, et vous n'avez rien de neuf à apprendre&nbsp;: vous savez déjà dire "
      + "«&nbsp;un formulaire&nbsp;» et «&nbsp;une adresse&nbsp;».",

      "Ces petits mots — ce, cet, cette, ces — servent à montrer une chose qu'on a "
      + "sous les yeux&nbsp;; on les appelle des <b>déterminants démonstratifs</b>. "
      + "Vous n'avez pas besoin du nom pour vous en servir, mais votre enseignant "
      + "l'emploiera.",

      "<b>Le test, à vous poser sur n'importe quel nom&nbsp;:</b> est-ce que je dis "
      + "<i>un</i> ou <i>une</i> devant ce mot&nbsp;? <b>une</b> → <b>cette</b>, "
      + "toujours. <b>un</b> → <b>ce</b>, sauf si le mot commence par une voyelle "
      + "ou un <i>h</i> muet&nbsp;: alors <b>cet</b>.",
    ],
    retenir: "D'abord <i>un</i> ou <i>une</i>. <b>Ensuite seulement</b> la première "
           + "lettre du nom. Dans cet ordre&nbsp;: c'est l'ordre qui évite "
           + "«&nbsp;cet école&nbsp;».",
    attente: "Lisez, puis continuez.",
  },

  // ── 4. Le piège, dans un vrai écrit. ─────────────────────────────────────
  {
    id:   'le-piege-voyelle',
    type: 'verif',
    eye:  'Le cas qui trompe',
    menu: 'Une note à l’école',
    titre: "Vous écrivez à la secrétaire. Le mot commence par une voyelle.",
    consigne: "Vous voulez dire que l'école ferme trop tôt pour vous. Quelle ligne "
            + "écrivez-vous&nbsp;?",
    options: [
      { txt: "Cette école ferme à seize heures.", juste: true },
      { txt: "Cet école ferme à seize heures.",
        rat_t: "Vous avez regardé la première lettre avant le genre.",
        rat: "C'est la faute la plus fréquente du point, et elle est logique&nbsp;: "
           + "le mot commence par une voyelle, donc on tend la main vers "
           + "«&nbsp;cet&nbsp;». Mais «&nbsp;cet&nbsp;» n'est qu'une autre façon "
           + "d'écrire «&nbsp;ce&nbsp;», et «&nbsp;ce&nbsp;» est masculin. On dit "
           + "«&nbsp;<b>une</b> école&nbsp;»&nbsp;: le mot est féminin, et "
           + "«&nbsp;cette&nbsp;» se dit très bien devant une voyelle." },
      { txt: "Ce école ferme à seize heures.",
        rat_t: "Deux choses ne vont pas dans le même mot.",
        rat: "«&nbsp;Ce&nbsp;» est masculin, et le mot est féminin — «&nbsp;une "
           + "école&nbsp;». Et même pour un mot masculin, «&nbsp;ce&nbsp;» ne se met "
           + "jamais devant une voyelle&nbsp;: on écrirait «&nbsp;cet&nbsp;»." },
    ],
    pourquoi: "«&nbsp;<b>Cette</b> école&nbsp;». Le genre d'abord, la première lettre "
            + "ensuite. Une voyelle ne rend pas un mot masculin.",
    attente: "Choisissez une réponse pour continuer.",
  },

  // ── 5. Pourquoi l'oreille ne peut pas aider. Le cœur du point. ───────────
  {
    id:   'un-seul-son',
    type: 'notion',
    eye:  'Ce que vous entendez ici',
    menu: 'Un seul son',
    titre: "Au Québec, les trois se disent de la même façon.",
    paras: [
      "Beaucoup de gens croient que «&nbsp;cette&nbsp;» s'entend plus long que "
      + "«&nbsp;ce&nbsp;». Ici, non. Devant une consonne, les deux se disent "
      + "<b>ste</b>&nbsp;: «&nbsp;Tu as vu <i>ste</i> camion-là&nbsp;?&nbsp;» et "
      + "«&nbsp;Tu as vu <i>ste</i> annonce-là&nbsp;?&nbsp;» sonnent pareil, alors "
      + "que l'un s'écrit <b>ce</b> et l'autre <b>cette</b>.",

      "Devant une voyelle, on entend <b>st</b>, attaché au mot qui suit&nbsp;: "
      + "«&nbsp;J'aime <i>st</i>appartement-là&nbsp;». Et au pluriel, "
      + "<b>sté</b>&nbsp;: «&nbsp;Connais-tu <i>sté</i> gens-là&nbsp;?&nbsp;»",

      "Alors ne cherchez pas à mieux écouter&nbsp;: il n'y a rien de plus à entendre. "
      + "Quand vous parlez, cela vous arrange — les trois se disent presque pareil, "
      + "personne ne verra votre hésitation. Quand vous <b>écrivez</b>, l'oreille ne "
      + "vous sert plus à rien, et c'est le nom qui décide.",
    ],
    retenir: "L'oreille ne tranche pas. <b>Le nom tranche.</b> Repassez par "
           + "<i>un</i> ou <i>une</i>.",
    attente: "Lisez, puis continuez.",
  },

  // ── 6. Trier des phrases écrites, cette fois. ────────────────────────────
  {
    id:   'tri-phrases',
    type: 'tri',
    eye:  'À vous de trancher',
    menu: 'Six phrases',
    titre: "Six phrases écrites. Lesquelles sont correctes ?",
    consigne: "Pour chacune, faites le test dans l'ordre&nbsp;: <i>un</i> ou "
            + "<i>une</i>&nbsp;? puis la première lettre du nom.",
    colonnes: [
      { id: 'ok',   t: 'Correct',   b: 'Correct' },
      { id: 'faux', t: 'Une faute', b: 'Une faute' },
    ],
    items: [
      { txt: "Cette semaine, je commence à huit heures.", sous: "un message au patron", ok: 'ok',
        rat: "«&nbsp;Une semaine&nbsp;» → «&nbsp;cette semaine&nbsp;». Rien à corriger.",
        pourquoi: "une semaine → cette semaine. Juste." },
      { txt: "Ce appartement est trop petit pour nous.", sous: "à un propriétaire", ok: 'faux',
        rat: "Le genre est bon — «&nbsp;un appartement&nbsp;». Mais le mot commence "
           + "par une voyelle&nbsp;: le masculin s'écrit alors "
           + "«&nbsp;<b>cet</b>&nbsp;». Il faut «&nbsp;cet appartement&nbsp;».",
        pourquoi: "Il faut « cet appartement »." },
      { txt: "Cet horaire me convient.", sous: "au travail", ok: 'ok',
        rat: "«&nbsp;Un horaire&nbsp;», et le <i>h</i> ne s'entend pas&nbsp;: c'est bien "
           + "«&nbsp;cet horaire&nbsp;».",
        pourquoi: "un horaire, h muet → cet horaire. Juste." },
      { txt: "Cet hôtel est complet jusqu'à lundi.", sous: "au téléphone", ok: 'ok',
        rat: "«&nbsp;Un hôtel&nbsp;», <i>h</i> muet&nbsp;: c'est «&nbsp;cet "
           + "hôtel&nbsp;». Même cas que «&nbsp;cet horaire&nbsp;».",
        pourquoi: "un hôtel, h muet → cet hôtel. Juste." },
      { txt: "Cet annonce n'est plus bonne.", sous: "en cherchant un logement", ok: 'faux',
        rat: "La voyelle vous a fait choisir «&nbsp;cet&nbsp;», comme pour "
           + "«&nbsp;école&nbsp;» tout à l'heure. Mais on dit «&nbsp;<b>une</b> "
           + "annonce&nbsp;»&nbsp;: il faut «&nbsp;<b>cette</b> annonce&nbsp;».",
        pourquoi: "Il faut « cette annonce »." },
      { txt: "Ces documents-là sont à vous ?", sous: "au comptoir", ok: 'ok',
        rat: "Au pluriel, il n'y a plus de choix à faire&nbsp;: c'est "
           + "«&nbsp;ces&nbsp;» pour tout. Et le trait d'union de "
           + "«&nbsp;-là&nbsp;» est bien écrit.",
        pourquoi: "Au pluriel : ces, pour tout. Juste." },
    ],
    attente: "Tranchez les six phrases pour continuer.",
  },

  // ── 7. Deux mots qui se ressemblent et ne font pas le même travail. ──────
  {
    id:   'cette-ou-cet',
    type: 'verif',
    eye:  'Vérification',
    menu: 'Le formulaire',
    titre: "Un formulaire vous demande de recopier une phrase. Deux mots à choisir.",
    consigne: "«&nbsp;Je confirme que ___ adresse et ___ numéro sont exacts.&nbsp;» "
            + "Quelle version recopiez-vous&nbsp;?",
    options: [
      { txt: "« … que cette adresse et ce numéro sont exacts. »", juste: true },
      { txt: "« … que cet adresse et ce numéro sont exacts. »",
        rat_t: "La deuxième moitié est juste. C'est la première qui a suivi la voyelle.",
        rat: "«&nbsp;Ce numéro&nbsp;» est parfait&nbsp;: masculin, consonne. Mais "
           + "«&nbsp;adresse&nbsp;» est féminin — «&nbsp;une adresse&nbsp;» — et le "
           + "féminin s'écrit «&nbsp;cette&nbsp;» même devant une voyelle." },
      { txt: "« … que cette adresse et cet numéro sont exacts. »",
        rat_t: "Les deux moitiés ont échangé leurs formes.",
        rat: "«&nbsp;Cette adresse&nbsp;» est juste. Mais «&nbsp;cet&nbsp;» ne "
           + "s'emploie que devant une voyelle&nbsp;: devant «&nbsp;numéro&nbsp;», "
           + "qui commence par un <i>n</i>, on écrit «&nbsp;<b>ce</b> numéro&nbsp;»." },
    ],
    pourquoi: "«&nbsp;<b>Cette</b> adresse et <b>ce</b> numéro.&nbsp;» Deux noms, "
            + "deux tests&nbsp;: une adresse, un numéro.",
    attente: "Choisissez une réponse pour continuer.",
  },

  // ── 8. « ces », dit en dernier : c'est le cas sans décision. ─────────────
  {
    id:   'ces-en-dernier',
    type: 'notion',
    eye:  'Ce qui reste',
    menu: 'Le pluriel',
    titre: "Au pluriel, la question disparaît : c'est « ces », et rien d'autre.",
    paras: [
      "On a gardé celui-ci pour la fin, et c'est voulu&nbsp;: il n'y a <b>rien à "
      + "décider</b>. Masculin, féminin, consonne, voyelle — dès qu'il y a plusieurs "
      + "choses, on écrit <b>ces</b>&nbsp;: ces formulaires, ces adresses, ces "
      + "horaires, ces écoles.",

      "Autrement dit, vous n'avez de choix à faire qu'<b>au singulier</b>, et il ne "
      + "porte que sur deux questions&nbsp;: <i>un</i> ou <i>une</i>, puis la "
      + "première lettre.",

      "Un dernier mot sur le «&nbsp;-là&nbsp;» qu'on entend partout ici — "
      + "«&nbsp;cette adresse-là&nbsp;», «&nbsp;ces documents-là&nbsp;». Il veut dire "
      + "«&nbsp;celui que je montre&nbsp;». Il n'est pas obligatoire, mais si vous "
      + "l'écrivez, le trait d'union l'est.",
    ],
    retenir: "Un seul choix, et seulement au singulier. <b>Au pluriel&nbsp;: ces.</b>",
    attente: "Lisez, puis continuez.",
  },

  // ── 9. Écrire une suite entière, pas reconnaître un mot. ─────────────────
  {
    id:   'le-message',
    type: 'verif',
    eye:  'Vérification',
    menu: 'Le message',
    titre: "Trois messages à un propriétaire. Un seul tient d'un bout à l'autre.",
    consigne: "La personne signale deux choses&nbsp;: la fenêtre de la chambre ferme "
            + "mal, et l'entrée n'est pas déneigée.",
    options: [
      { txt: "« Cette fenêtre ferme mal, et cette entrée est glacée depuis trois jours. »",
        juste: true },
      { txt: "« Cette fenêtre ferme mal, et cet entrée est glacée depuis trois jours. »",
        rat_t: "La première moitié est juste. La voyelle vous a repris.",
        rat: "«&nbsp;Cette fenêtre&nbsp;»&nbsp;: parfait. «&nbsp;Entrée&nbsp;» est "
           + "féminin lui aussi — «&nbsp;une entrée&nbsp;» — et le féminin garde "
           + "«&nbsp;cette&nbsp;» devant une voyelle. C'est exactement le cas de "
           + "«&nbsp;cette école&nbsp;» et de «&nbsp;cette annonce&nbsp;»." },
      { txt: "« Ce fenêtre ferme mal, et cette entrée est glacée depuis trois jours. »",
        rat_t: "La seconde moitié est juste. C'est le genre du premier nom qui a manqué.",
        rat: "«&nbsp;Cette entrée&nbsp;» est bon. Mais on dit «&nbsp;<b>une</b> "
           + "fenêtre&nbsp;»&nbsp;: il faut «&nbsp;cette fenêtre&nbsp;». Ici, la "
           + "première lettre n'avait rien à voir — le test commence toujours par "
           + "<i>un</i> ou <i>une</i>." },
    ],
    pourquoi: "Deux noms féminins, deux fois «&nbsp;cette&nbsp;», dont un devant une "
            + "voyelle. <b>C'est tout le point en une phrase.</b>",
    attente: "Choisissez une réponse pour continuer.",
  },

  // ── 10. La fermeture : le cas de l'écran 1. ──────────────────────────────
  {
    id:   'fermeture',
    type: 'verif',
    eye:  'La dernière',
    menu: 'Pour finir',
    titre: "On revient au manteau. Cette fois, c'est un autre mot que vous entendez.",
    consigne: "Quelqu'un dit&nbsp;: «&nbsp;Je vais essayer <i>ste</i> veste-là.&nbsp;» "
            + "Vous l'écrivez. Quelle ligne écrivez-vous&nbsp;?",
    options: [
      { txt: "« Je vais essayer cette veste-là. »", juste: true },
      { txt: "« Je vais essayer ce veste-là. »",
        rat_t: "C'est ce que vous avez entendu — et c'est la phrase de l'écran 1.",
        rat: "Le son est le même que pour «&nbsp;ce manteau-là&nbsp;», et c'est "
           + "justement le piège du point&nbsp;: l'oreille ne fait pas la différence. "
           + "On dit «&nbsp;<b>une</b> veste&nbsp;»&nbsp;: c'est «&nbsp;cette&nbsp;»." },
      { txt: "« Je vais essayer cet veste-là. »",
        rat_t: "«&nbsp;cet&nbsp;» ne va que devant une voyelle.",
        rat: "«&nbsp;Veste&nbsp;» commence par un <i>v</i>. Et même devant une "
           + "voyelle, «&nbsp;cet&nbsp;» ne servirait qu'à un nom masculin — celui-ci "
           + "est féminin." },
    ],
    pourquoi: "«&nbsp;<b>Cette</b> veste-là.&nbsp;» Même son qu'à l'écran 1, autre "
            + "orthographe. Vous ne choisissez plus avec l'oreille&nbsp;: vous "
            + "choisissez avec <i>un</i> ou <i>une</i>.",
    attente: "Choisissez une réponse pour finir.",
  },

];
