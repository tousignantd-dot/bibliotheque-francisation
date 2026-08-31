// ═══════════════════════════════════════════════════════════════════════════
// Point express — Ça dure encore, ou c'est fini ? Trois mots qui tranchent
//
// Savoir n4-s37 (Prépositions et GPrép) : « employer des prépositions de temps
// qui introduisent un CI ou un CP — pendant, en + mois, il y a, voilà ».
// Complété par n4-s02, qui demande de comprendre la continuité (« depuis que,
// ça fait X que »). Une ORDONNANCE : l'enseignant l'envoie à un élève qui
// répond « Je travaille ici il y a six mois » ou « J'ai mal depuis trois
// jours » quand il veut dire le contraire.
//
// ── Ce qui le sépare des mini-leçons existantes ────────────────────────────
// Quatre mini-leçons du dépôt couvrent le terrain : « Depuis quand, et pour
// combien de temps » (module-n4-emploi), « Depuis quand ça dure — la question
// qu'on vous posera toujours » (module-sante), « De, à, du, au, jusqu'à,
// pendant — lire une durée » et « En huit heures, pour une semaine ». Toutes
// procèdent de la même façon : un TABLEAU des marqueurs de temps, une ligne
// par mot, un exemple par ligne — cinq, six, parfois huit entrées. L'élève
// sort de là en sachant que « depuis » existe, et il continue de dire « je
// travaille ici il y a six mois ».
//
// Ce point-ci ne donne aucun tableau et ne traite que TROIS mots. Il fait
// commencer par UNE SEULE QUESTION — est-ce que ça dure encore aujourd'hui ? —
// et cette question suffit à écarter les deux tiers des cas. Les cinq écarts :
//
//   1. INDUCTIF. Écran 2 : huit phrases à ranger en « ça dure encore » / « c'est
//      fini ». Aucune règle avant l'écran 3, où elle est écrite comme un
//      constat de ce que l'élève vient de trier.
//   2. UNE QUESTION, PUIS UNE SECONDE. Ça dure encore ? → depuis. Sinon :
//      est-ce que je dis QUAND, ou COMBIEN DE TEMPS ? Deux questions couvrent
//      les trois mots, sur une phrase jamais vue.
//   3. LE TEMPS DU VERBE EST UN INDICE, PAS UNE RÈGLE DE PLUS (écran 5). Avec
//      « depuis », le verbe reste au présent — et c'est précisément ce qui
//      surprend celui dont la langue met un passé.
//   4. UN PIÈGE QU'AUCUNE MINI-LEÇON NE TRAITE (écran 7) : « il y a » sert
//      aussi à dire ce qui existe. Les mêmes trois mots, deux métiers.
//   5. EXEMPLES VARIÉS : une entrevue d'embauche, un comptoir de clinique, un
//      formulaire d'inscription, un message à un propriétaire, une conversation
//      de voisinage.
//
// Aucun média : les trois marqueurs s'entendent parfaitement. Ce qui manque à
// l'élève, c'est de savoir lequel des trois la situation appelle.
// ═══════════════════════════════════════════════════════════════════════════

const PARCOURS = {
  slug:     'depuis-pendant-il-y-a',
  titre:    "Ça dure encore, ou c'est fini ? Trois mots qui tranchent",
  surtitre: "Point express · 10 minutes",
  niveau:   4,
  savoir:   'n4-s37',
};

const ECRANS = [

  // ── 1. Une décision, sans aucune règle donnée. ───────────────────────────
  {
    id:   'depart',
    type: 'verif',
    eye:  'Une question, pour commencer',
    menu: 'Une entrevue',
    titre: "En entrevue, on vous demande : « Vous êtes au Québec depuis quand ? »",
    consigne: "Vous êtes arrivé en mars 2024 et vous y êtes toujours. Répondez avec ce que vous "
            + "savez déjà — ou au feeling. On expliquera après&nbsp;: c'est fait exprès.",
    options: [
      { txt: "«&nbsp;Je suis ici depuis deux ans.&nbsp;»", juste: true },
      { txt: "«&nbsp;Je suis ici il y a deux ans.&nbsp;»",
        rat_t: "C'est la phrase la plus fréquente en entrevue, et elle dit autre chose.",
        rat: "«&nbsp;Il y a deux ans&nbsp;» pose un point dans le passé et l'y laisse&nbsp;: "
           + "l'employeur comprend que vous étiez ici en 2024, et il ne sait pas si vous y êtes "
           + "encore. Or c'est exactement ce qu'il voulait savoir." },
      { txt: "«&nbsp;Je suis ici pendant deux ans.&nbsp;»",
        rat_t: "Celle-ci annonce une date de départ.",
        rat: "«&nbsp;Pendant deux ans&nbsp;» enferme la durée entre un début et une fin. "
           + "L'employeur peut comprendre que votre séjour est limité et que vous repartez — "
           + "c'est la pire des trois réponses dans une entrevue." },
    ],
    pourquoi: "«&nbsp;Depuis deux ans.&nbsp;» Gardez la question&nbsp;: on y revient au dernier "
            + "écran.",
    attente: "Choisissez une réponse pour continuer.",
  },

  // ── 2. On trie AVANT de savoir. ──────────────────────────────────────────
  {
    id:   'tri-huit',
    type: 'tri',
    eye:  'À vous de trancher',
    menu: 'Huit phrases',
    titre: "Huit phrases entendues. Est-ce que ça dure encore aujourd'hui ?",
    consigne: "Aucune règle ne vous a été donnée — normal. Ne cherchez pas quel mot est employé&nbsp;: "
            + "demandez-vous seulement si, ce matin, la chose continue.",
    colonnes: [
      { id: 'dure', t: "Ça dure encore", b: "Ça dure encore" },
      { id: 'fini', t: "C'est terminé",  b: "C'est terminé" },
    ],
    items: [
      { txt: "J'habite à Laval depuis trois mois.", sous: "une voisine, dans l'ascenseur", ok: 'dure',
        rat: "Elle y habite ce matin&nbsp;: le déménagement est passé, pas l'habitation. Le "
           + "compte part d'il y a trois mois et court jusqu'à aujourd'hui.",
        pourquoi: "Elle y habite encore ce matin." },
      { txt: "J'ai habité à Laval pendant trois mois.", sous: "la même voisine, en parlant d'avant", ok: 'fini',
        rat: "Même ville, même durée — et pourtant elle n'y est plus. La durée est fermée aux "
           + "deux bouts&nbsp;: un début, une fin, et le tout est derrière.",
        pourquoi: "La durée est fermée : elle n'y est plus." },
      { txt: "Je suis arrivée au pays il y a six ans.", sous: "un formulaire d'inscription", ok: 'fini',
        rat: "Attention&nbsp;: la personne est encore ici, bien sûr. Mais la phrase ne parle "
           + "pas de son séjour&nbsp;: elle parle de son <b>arrivée</b>, qui a eu lieu une "
           + "fois, il y a six ans, et qui est terminée.",
        pourquoi: "C'est l'arrivée qui est datée, pas le séjour." },
      { txt: "J'attends une réponse depuis lundi.", sous: "un appel à un propriétaire", ok: 'dure',
        rat: "L'attente a commencé lundi et elle n'a pas cessé — c'est même le sens de "
           + "l'appel. Remarquez que le verbe est au présent&nbsp;: on y revient.",
        pourquoi: "L'attente a commencé lundi et continue." },
      { txt: "J'ai attendu deux heures à l'urgence.", sous: "un récit à un collègue, le lendemain", ok: 'fini',
        rat: "Deux heures pleines, entre l'arrivée et le passage&nbsp;: la durée est close. "
           + "Le lendemain, on la raconte.",
        pourquoi: "Deux heures closes, racontées après coup." },
      { txt: "Je prends ce médicament depuis mars.", sous: "au comptoir d'une pharmacie", ok: 'dure',
        rat: "Le mois de mars est un point de départ, pas une durée&nbsp;: le traitement court "
           + "toujours. C'est ce que la pharmacienne a besoin de savoir.",
        pourquoi: "Mars est le départ ; le traitement continue." },
      { txt: "Il a plu pendant toute la fin de semaine.", sous: "un lundi matin, au travail", ok: 'fini',
        rat: "La fin de semaine est finie, donc la pluie aussi. La durée est bornée par "
           + "l'évènement lui-même.",
        pourquoi: "La fin de semaine est passée." },
      { txt: "Ça fait deux semaines que le chauffage ne marche pas.", sous: "une plainte écrite", ok: 'dure',
        rat: "Celui-là ne porte aucun des trois mots — et pourtant il dit la même chose que "
           + "«&nbsp;depuis deux semaines&nbsp;». On y revient à l'écran 8&nbsp;: c'est le tour "
           + "le plus employé au Québec.",
        pourquoi: "Le chauffage est encore en panne ce matin." },
    ],
    attente: "Tranchez les huit phrases pour continuer.",
  },

  // ── 3. La règle, écrite comme un constat. ────────────────────────────────
  {
    id:   'les-deux-questions',
    type: 'notion',
    eye:  'Ce que vous venez de faire',
    menu: 'Deux questions',
    titre: "Vous n'avez pas choisi entre trois mots. Vous avez répondu à une question.",
    paras: [
      "Toutes les phrases de votre colonne «&nbsp;ça dure encore&nbsp;» portent "
      + "<b>depuis</b> — ou son équivalent. Toutes les autres portent <b>pendant</b> ou "
      + "<b>il y a</b>. La première question a donc déjà réglé la moitié du travail.",

      "<b>Question 1&nbsp;: est-ce que ça dure encore aujourd'hui&nbsp;?</b> Si oui, c'est "
      + "<b>depuis</b>, et il n'y a rien d'autre à se demander. «&nbsp;<i>Je travaille là "
      + "depuis six mois.</i>&nbsp;» «&nbsp;<i>J'ai mal depuis mardi.</i>&nbsp;»",

      "<b>Question 2, seulement si c'est fini&nbsp;: est-ce que je dis QUAND, ou COMBIEN DE "
      + "TEMPS&nbsp;?</b> Quand&nbsp;→ <b>il y a</b> («&nbsp;<i>je suis arrivé il y a six "
      + "mois</i>&nbsp;»). Combien de temps&nbsp;→ <b>pendant</b> («&nbsp;<i>j'ai travaillé là "
      + "pendant six mois</i>&nbsp;»). Ces trois mots sont des <b>prépositions de "
      + "temps</b>&nbsp;; le nom ne sert qu'à en parler avec votre enseignant.",
    ],
    retenir: "Ça dure encore&nbsp;? → <b>depuis</b>. Sinon&nbsp;: je dis quand&nbsp;? → "
           + "<b>il y a</b>. Je dis combien de temps&nbsp;? → <b>pendant</b>.",
    attente: "Lisez, puis continuez.",
  },

  // ── 4. Les deux mots du passé, qu'on confond entre eux. ──────────────────
  {
    id:   'quand-ou-combien',
    type: 'verif',
    eye:  'La deuxième question',
    menu: 'Quand ou combien',
    titre: "En entrevue : « Parlez-moi de votre expérience en cuisine. »",
    consigne: "Vous avez travaillé dans un restaurant de 2019 à 2022, et vous avez quitté cet "
            + "emploi. Vous voulez dire les <b>trois ans</b>, pas la date.",
    options: [
      { txt: "«&nbsp;J'ai travaillé en cuisine pendant trois ans.&nbsp;»", juste: true },
      { txt: "«&nbsp;J'ai travaillé en cuisine il y a trois ans.&nbsp;»",
        rat_t: "L'employeur entendra une date, pas une expérience.",
        rat: "«&nbsp;Il y a trois ans&nbsp;» répond à «&nbsp;quand&nbsp;?&nbsp;»&nbsp;: il "
           + "comprendra que vous y étiez en 2023, peut-être une semaine. Vous vouliez dire la "
           + "<b>longueur</b> de l'expérience, et c'est ce qui compte dans une entrevue." },
      { txt: "«&nbsp;Je travaille en cuisine depuis trois ans.&nbsp;»",
        rat_t: "Elle serait parfaite — si vous y étiez encore.",
        rat: "«&nbsp;Depuis&nbsp;» dit que ça continue aujourd'hui. Ici l'emploi est terminé "
           + "depuis 2022&nbsp;: la phrase serait fausse, et un employeur qui appelle vos "
           + "références s'en apercevra." },
    ],
    pourquoi: "Fini + une longueur&nbsp;→ <b>pendant</b>. Fini + un moment&nbsp;→ "
            + "<b>il y a</b>. Les deux racontent le passé, mais ils ne répondent pas à la même "
            + "question.",
    attente: "Choisissez une réponse pour continuer.",
  },

  // ── 5. L'indice gratuit : le temps du verbe. ─────────────────────────────
  {
    id:   'le-verbe',
    type: 'notion',
    eye:  'Un indice gratuit',
    menu: 'Le verbe',
    titre: "Avec « depuis », le verbe reste au présent. C'est ce qui surprend.",
    paras: [
      "Dans beaucoup de langues, une chose commencée dans le passé se dit au passé, même si "
      + "elle continue. En français, non&nbsp;: «&nbsp;<i>Je <b>travaille</b> ici depuis six "
      + "mois.</i>&nbsp;» «&nbsp;<i>J'<b>attends</b> depuis lundi.</i>&nbsp;» "
      + "«&nbsp;<i>Elle <b>habite</b> à Laval depuis trois ans.</i>&nbsp;»",

      "Les deux autres, eux, vont avec le passé&nbsp;: «&nbsp;<i>J'<b>ai travaillé</b> là "
      + "pendant six mois.</i>&nbsp;» «&nbsp;<i>Je <b>suis arrivé</b> il y a six mois.</i>&nbsp;» "
      + "Cela vous donne un contrôle gratuit&nbsp;: si vous avez écrit un passé composé juste "
      + "à côté de «&nbsp;depuis&nbsp;», relisez la phrase — l'un des deux est de trop.",

      "Une seule exception, et elle est fréquente&nbsp;: à la forme négative, «&nbsp;depuis&nbsp;» "
      + "accepte le passé. «&nbsp;<i>Je n'ai pas vu le médecin depuis mars.</i>&nbsp;» Ce qui "
      + "dure, dans cette phrase, c'est l'absence de rendez-vous.",
    ],
    retenir: "<b>Depuis</b> + présent. <b>Pendant</b> et <b>il y a</b> + passé composé. Un "
           + "passé collé à «&nbsp;depuis&nbsp;»&nbsp;: relisez.",
    attente: "Lisez, puis continuez.",
  },

  // ── 6. Trier des phrases écrites. ────────────────────────────────────────
  {
    id:   'tri-ecrites',
    type: 'tri',
    eye:  'À vous de trancher',
    menu: 'Six phrases',
    titre: "Six phrases écrites. Lesquelles tiennent ?",
    consigne: "Posez les deux questions dans l'ordre, puis regardez le temps du verbe.",
    colonnes: [
      { id: 'ok',   t: 'Correcte',  b: 'Correcte' },
      { id: 'faux', t: 'Une faute', b: 'Une faute' },
    ],
    items: [
      { txt: "J'attends votre appel depuis mardi.", ok: 'ok',
        rat: "L'attente continue, le marqueur est le bon, et le verbe est au présent. Les trois "
           + "s'accordent.",
        pourquoi: "Ça dure : depuis + présent." },
      { txt: "Je travaille dans cette usine il y a deux ans.", ok: 'faux',
        rat: "Le verbe est au présent, donc l'emploi dure — mais le marqueur, lui, dit que "
           + "c'est fini. Les deux moitiés de la phrase se contredisent&nbsp;: "
           + "«&nbsp;<b>depuis</b> deux ans&nbsp;».",
        pourquoi: "Ça dure encore : il faut « depuis »." },
      { txt: "Nous sommes déménagés il y a un mois.", ok: 'ok',
        rat: "Le déménagement a eu lieu une fois, à un moment précis du passé, et il est "
           + "terminé. C'est exactement l'emploi de «&nbsp;il y a&nbsp;».",
        pourquoi: "Un évènement daté, terminé." },
      { txt: "J'ai gardé le silence pendant la réunion.", ok: 'ok',
        rat: "Une durée fermée aux deux bouts — la réunion — et un verbe au passé. Rien à "
           + "corriger.",
        pourquoi: "Durée fermée + passé composé." },
      { txt: "Le chauffage est en panne pendant deux semaines.", ok: 'faux',
        rat: "Si la panne dure toujours, la durée n'est pas fermée&nbsp;: on ne peut pas la "
           + "mesurer d'un bout à l'autre. Il faut «&nbsp;<b>depuis</b> deux semaines&nbsp;» — "
           + "et c'est cette phrase-là qui obligera le propriétaire à agir.",
        pourquoi: "La panne continue : depuis deux semaines." },
      { txt: "J'ai suivi des cours de français depuis six mois, en 2022.", ok: 'faux',
        rat: "Le passé composé et la date disent tous deux que c'est fini&nbsp;; seul le "
           + "marqueur prétend le contraire. Une durée close se dit avec "
           + "«&nbsp;<b>pendant</b> six mois&nbsp;».",
        pourquoi: "C'est fini et c'est une longueur : pendant." },
    ],
    attente: "Tranchez les six phrases pour continuer.",
  },

  // ── 7. Le piège que personne ne traite : les mêmes trois mots, deux métiers.
  {
    id:   'lautre-il-y-a',
    type: 'verif',
    eye:  'Le piège',
    menu: "L'autre « il y a »",
    titre: "« Il y a une lettre pour vous à la réception depuis hier. »",
    consigne: "Cette phrase porte les mêmes trois mots que «&nbsp;je suis arrivé il y a un "
            + "an&nbsp;». Que dit-elle&nbsp;?",
    options: [
      { txt: "Une lettre <b>existe</b> à la réception, et elle y est depuis hier.", juste: true },
      { txt: "Une lettre est arrivée <b>hier</b>, et on est venu la porter.",
        rat_t: "Vous avez lu «&nbsp;il y a&nbsp;» comme un marqueur de temps — c'est le piège.",
        rat: "Ici, «&nbsp;il y a&nbsp;» n'est suivi d'aucune durée&nbsp;: il est suivi de "
           + "«&nbsp;une lettre&nbsp;». C'est le «&nbsp;il y a&nbsp;» qui dit ce qui "
           + "<b>existe</b>, comme dans «&nbsp;il y a du monde&nbsp;». Le marqueur de temps de "
           + "la phrase, c'est «&nbsp;depuis hier&nbsp;»." },
      { txt: "La lettre a été gardée pendant une journée, puis renvoyée.",
        rat_t: "Rien dans la phrase ne dit qu'elle est repartie.",
        rat: "«&nbsp;Depuis hier&nbsp;» dit que la situation dure&nbsp;: la lettre est encore "
           + "là ce matin, et c'est pour ça qu'on vous prévient. Aucune fin n'est annoncée." },
    ],
    pourquoi: "Regardez ce qui suit&nbsp;: «&nbsp;il y a&nbsp;» + une <b>durée</b> est un "
            + "marqueur de temps&nbsp;; «&nbsp;il y a&nbsp;» + une <b>chose</b> dit seulement "
            + "qu'elle existe.",
    attente: "Choisissez une réponse pour continuer.",
  },

  // ── 8. Le tour d'ici, dit en dernier. ────────────────────────────────────
  {
    id:   'ca-fait-que',
    type: 'notion',
    eye:  'Ce qui reste',
    menu: '« Ça fait… que »',
    titre: "Au Québec, on dit surtout « ça fait deux semaines que ».",
    paras: [
      "On a gardé ce tour pour la fin, et c'est volontaire&nbsp;: c'est celui que vous "
      + "entendrez le plus, et il ne s'apprend bien qu'une fois «&nbsp;depuis&nbsp;» en "
      + "place. «&nbsp;<i><b>Ça fait</b> deux semaines <b>que</b> j'attends.</i>&nbsp;» "
      + "«&nbsp;<i><b>Ça fait</b> six mois <b>que</b> je travaille là.</i>&nbsp;» C'est le "
      + "même sens que «&nbsp;depuis&nbsp;», dit autrement.",

      "Trois choses à remarquer, et elles suffisent&nbsp;: la durée se glisse au milieu, un "
      + "«&nbsp;que&nbsp;» ferme le tour, et le verbe reste <b>au présent</b>, exactement comme "
      + "avec «&nbsp;depuis&nbsp;». Vous n'avez donc rien de neuf à apprendre — vous avez un "
      + "second habit pour la même idée.",

      "Il vous sert surtout à <b>comprendre</b>&nbsp;: quand un voisin dit «&nbsp;ça fait un "
      + "mois qu'ils réparent l'ascenseur&nbsp;», il ne raconte pas le passé, il se plaint "
      + "d'aujourd'hui. À l'écrit — une plainte, une lettre au propriétaire — préférez "
      + "«&nbsp;depuis&nbsp;», plus court et plus net.",
    ],
    retenir: "«&nbsp;Ça fait X que&nbsp;» = «&nbsp;depuis X&nbsp;». Verbe au présent dans les "
           + "deux. À l'écrit officiel&nbsp;: <b>depuis</b>.",
    attente: "Lisez, puis continuez.",
  },

  // ── 9. Écrire, pas reconnaître. ──────────────────────────────────────────
  {
    id:   'votre-message',
    type: 'verif',
    eye:  'Vérification',
    menu: 'Votre plainte',
    titre: "Vous écrivez à votre propriétaire. Quelle version tient d'un bout à l'autre ?",
    consigne: "Le chauffage est tombé en panne le 3 novembre et il ne marche toujours pas. Vous "
            + "avez appelé deux fois la semaine dernière.",
    options: [
      { txt: "«&nbsp;Le chauffage ne fonctionne plus depuis le 3 novembre. Je vous ai appelé "
           + "deux fois il y a une semaine.&nbsp;»", juste: true },
      { txt: "«&nbsp;Le chauffage ne fonctionne plus il y a le 3 novembre. Je vous ai appelé "
           + "deux fois depuis une semaine.&nbsp;»",
        rat_t: "Les deux marqueurs ont été échangés.",
        rat: "La panne dure&nbsp;: elle veut «&nbsp;<b>depuis</b> le 3 novembre&nbsp;». Les "
           + "appels sont faits et datés&nbsp;: ils veulent «&nbsp;<b>il y a</b> une "
           + "semaine&nbsp;». Et «&nbsp;il y a le 3 novembre&nbsp;» ne se dit pas&nbsp;: après "
           + "«&nbsp;il y a&nbsp;», on met une durée, jamais une date." },
      { txt: "«&nbsp;Le chauffage ne fonctionne plus pendant trois semaines. Je vous ai appelé "
           + "deux fois la semaine passée.&nbsp;»",
        rat_t: "La seconde phrase est bonne. La première annonce une fin qui n'existe pas.",
        rat: "«&nbsp;Pendant trois semaines&nbsp;» ferme la durée&nbsp;: votre propriétaire "
           + "peut lire que la panne est réglée. Dans une plainte, c'est la phrase qui vous "
           + "coûte la réparation — il faut «&nbsp;<b>depuis</b> trois semaines&nbsp;»." },
    ],
    pourquoi: "Une panne qui dure&nbsp;→ depuis. Un appel fait et daté&nbsp;→ il y a. "
            + "<b>Deux phrases, deux fois la première question.</b>",
    attente: "Choisissez une réponse pour continuer.",
  },

  // ── 10. La fermeture : le cas de l'écran 1. ──────────────────────────────
  {
    id:   'fermeture',
    type: 'verif',
    eye:  'La dernière',
    menu: 'Pour finir',
    titre: "On revient à l'entrevue : « Vous êtes au Québec depuis quand ? »",
    consigne: "Cette fois, vous voulez dire trois choses&nbsp;: vous êtes arrivé en 2024, vous y "
            + "êtes toujours, et vous avez suivi un cours de français de janvier à juin.",
    options: [
      { txt: "«&nbsp;Je suis arrivé il y a deux ans et je vis ici depuis. J'ai suivi un cours "
           + "de français pendant six mois.&nbsp;»", juste: true },
      { txt: "«&nbsp;Je suis arrivé depuis deux ans et je vis ici pendant. J'ai suivi un cours "
           + "de français il y a six mois.&nbsp;»",
        rat_t: "Les trois marqueurs sont là, chacun à la mauvaise place.",
        rat: "L'arrivée est un évènement daté&nbsp;: <b>il y a</b>. Le séjour dure&nbsp;: "
           + "<b>depuis</b>. Le cours est fini et vous en donnez la longueur&nbsp;: "
           + "<b>pendant</b>. Reprenez les deux questions sur chaque phrase, une à la fois." },
      { txt: "«&nbsp;Je suis ici il y a deux ans. J'ai suivi un cours de français depuis six "
           + "mois.&nbsp;»",
        rat_t: "C'est la phrase de l'écran 1, avec une seconde du même modèle.",
        rat: "Les deux phrases posent un marqueur de passé fini sur une chose qui dure, et "
           + "l'inverse. En entrevue, la première laisse croire que vous êtes reparti, et la "
           + "seconde qu'un cours terminé est encore en cours&nbsp;: l'employeur ne saura pas "
           + "si vous êtes disponible." },
    ],
    pourquoi: "Vous avez fait les deux choses&nbsp;: demander si ça dure encore, puis, quand "
            + "c'était fini, choisir entre le moment et la longueur.",
    attente: "Choisissez une réponse pour finir.",
  },

];
