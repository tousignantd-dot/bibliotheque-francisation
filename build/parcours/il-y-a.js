// ═══════════════════════════════════════════════════════════════════════════
// Point express — « Il y a » : ne le traduisez pas, apprenez-le
//
// Savoir n1-s07 (Phrases à construction particulière). Une ORDONNANCE :
// l'enseignant l'envoie à l'élève qui dit « il a trois étages » pour parler du
// bâtiment, ou qui cherche mot à mot ce que veut dire « il » dans « il y a ».
// Dix minutes, dix écrans, niveau 1.
//
// ── Ce qui le sépare des mini-leçons existantes ────────────────────────────
// Deux mini-leçons du dépôt enseignent « il y a », et toutes les deux
// l'opposent à « c'est » :
//   · `module-n2-couloirs`, « Il y a… et c'est… » — la visite du centre : il y a
//     un ascenseur / c'est la cafétéria.
//   · `module-n3-poste`, « Dire ce qu'il y a dans la boîte » — le contenu d'un
//     colis.
// Cette opposition est utile, et elle laisse entière la faute que ce point
// vient corriger : « il a » contre « il y a ». Un seul petit mot les sépare,
// aucune mini-leçon ne les met face à face, et l'élève qui les confond dit
// « la classe a douze chaises » quand il veut dire qu'il y en a douze — ou
// comprend qu'un homme possède trois étages. Les cinq écarts tenus :
//
//   1. INDUCTIF. L'élève range huit situations AVANT qu'on lui dise quoi que ce
//      soit : est-ce que ça existe quelque part, ou est-ce que quelqu'un le
//      possède ? La règle de l'écran 3 est le constat de ce tri.
//   2. PARTIEL, JAMAIS LA LISTE. Aucun tableau des présentatifs, aucune
//      opposition avec « c'est » — elle est déjà faite ailleurs. Un TEST
//      unique : peut-on ajouter « ici », « dans la classe », « près d'ici » ?
//      Alors c'est « il y a ».
//   3. LE « Y A » DE L'ORAL EST DIT EN DERNIER (écran 8). C'est ce que l'élève
//      entend vraiment dans la rue, mais le nommer d'entrée l'empêcherait
//      d'écrire les trois mots.
//   4. LE MÉTALANGAGE APRÈS, et presque pas : « il » qui ne désigne personne,
//      à l'écran 3, une fois huit cas triés.
//   5. EXEMPLES VARIÉS, JAMAIS CEUX D'UN MODULE. Une classe, un autobus, une
//      épicerie, un texto, un message à l'école. Ni visite de centre, ni colis.
//
// Aucun média. Ce point se joue sur trois mots écrits qui se corrigent par
// comparaison de chaînes : il tourne dans un centre sans assistance.
// ═══════════════════════════════════════════════════════════════════════════

const PARCOURS = {
  slug:     'il-y-a',
  titre:    "« Il y a » : ne le traduisez pas, apprenez-le",
  surtitre: "Point express · 10 minutes",
  niveau:   1,
  savoir:   'n1-s07',
};

const ECRANS = [

  // ── 1. Une décision, sans aucune règle donnée. ───────────────────────────
  {
    id:   'depart',
    type: 'verif',
    eye:  'Une question, pour commencer',
    menu: 'Douze chaises',
    titre: "Vous voulez dire : dans la classe, douze chaises. Vous dites quoi ?",
    consigne: "Répondez avec ce que vous savez déjà — ou au feeling. On expliquera après&nbsp;: "
            + "c'est fait exprès.",
    options: [
      { txt: "«&nbsp;Dans la classe, <b>il y a</b> douze chaises.&nbsp;»", juste: true },
      { txt: "«&nbsp;Dans la classe, <b>il a</b> douze chaises.&nbsp;»",
        rat_t: "Un seul petit mot de différence — et la phrase change de sens.",
        rat: "«&nbsp;Il a&nbsp;» veut dire que <b>quelqu'un possède</b>&nbsp;: Marc a douze "
           + "chaises, elles sont à lui. Vous, vous voulez dire qu'elles <b>sont là</b>. Ce n'est "
           + "pas la même chose, et le petit mot au milieu fait toute la différence." },
      { txt: "«&nbsp;Dans la classe, <b>c'est</b> douze chaises.&nbsp;»",
        rat_t: "«&nbsp;C'est&nbsp;» sert à autre chose.",
        rat: "«&nbsp;C'est&nbsp;» sert à <b>nommer</b>&nbsp;: c'est la classe, c'est mon frère. "
           + "Pour dire qu'une chose se trouve quelque part, le français a une autre phrase, et "
           + "c'est celle qu'on travaille ici." },
    ],
    pourquoi: "<b>Il y a</b> douze chaises. Gardez cette phrase en tête&nbsp;: on y revient à "
            + "la fin.",
    attente: "Choisissez une réponse pour continuer.",
  },

  // ── 2. On trie AVANT de savoir. C'est ici que le point se sépare. ────────
  {
    id:   'tri-existe-possede',
    type: 'tri',
    eye:  'À vous de trancher',
    menu: 'Huit situations',
    titre: "Huit choses à dire. Est-ce que ça existe, ou est-ce que quelqu'un l'a ?",
    consigne: "Aucune règle ne vous a été donnée — normal. Demandez-vous seulement une "
            + "chose&nbsp;: est-ce qu'on peut ajouter «&nbsp;ici&nbsp;» ou «&nbsp;dans…&nbsp;»&nbsp;?",
    colonnes: [
      { id: 'ilya', t: "Il y a", b: "Il y a" },
      { id: 'ila',  t: "Il a",  b: "Il a" },
    ],
    items: [
      { txt: "Dans la salle, une horloge.", sous: "vous décrivez la salle", ok: 'ilya',
        rat: "L'horloge n'appartient à personne dans votre phrase&nbsp;: elle est "
           + "<b>là</b>. Et vous pouvez dire «&nbsp;dans la salle&nbsp;»&nbsp;: c'est le signe.",
        pourquoi: "Il y a une horloge dans la salle." },
      { txt: "Paul, une voiture bleue.", sous: "vous parlez de Paul", ok: 'ila',
        rat: "La voiture est <b>à Paul</b>. Ici, «&nbsp;il&nbsp;» veut dire Paul&nbsp;: "
           + "«&nbsp;il a une voiture bleue&nbsp;».",
        pourquoi: "Il a une voiture bleue." },
      { txt: "Près de l'école, une pharmacie.", sous: "vous indiquez le quartier", ok: 'ilya',
        rat: "La pharmacie <b>existe</b> près de l'école. Personne ne la possède dans votre "
           + "phrase, et «&nbsp;près de l'école&nbsp;» dit bien l'endroit.",
        pourquoi: "Il y a une pharmacie près de l'école." },
      { txt: "Mon frère, deux enfants.", sous: "vous parlez de votre frère", ok: 'ila',
        rat: "Ce sont <b>ses</b> enfants&nbsp;: «&nbsp;il a deux enfants&nbsp;». On parle d'une "
           + "personne, pas d'un endroit.",
        pourquoi: "Il a deux enfants." },
      { txt: "Dans mon sac, trois cahiers.", sous: "vous ouvrez votre sac", ok: 'ilya',
        rat: "Les cahiers sont peut-être à vous, mais la phrase dit où ils <b>sont</b>. "
           + "«&nbsp;Dans mon sac&nbsp;»&nbsp;: c'est un endroit.",
        pourquoi: "Il y a trois cahiers dans mon sac." },
      { txt: "Le professeur, une question pour vous.", sous: "il lève la main", ok: 'ila',
        rat: "La question est <b>à lui</b>&nbsp;: c'est lui qui la pose. «&nbsp;Il a une "
           + "question&nbsp;».",
        pourquoi: "Il a une question." },
      { txt: "Aujourd'hui, un examen.", sous: "vous regardez l'horaire", ok: 'ilya',
        rat: "L'examen n'est à personne&nbsp;: il <b>arrive</b>, il est là aujourd'hui. "
           + "«&nbsp;Aujourd'hui&nbsp;» est un moment, et ça marche comme un endroit.",
        pourquoi: "Aujourd'hui, il y a un examen." },
      { txt: "Dans l'autobus, beaucoup de monde.", sous: "vous téléphonez à un ami", ok: 'ilya',
        rat: "Les gens sont <b>dans</b> l'autobus. L'autobus ne les possède pas&nbsp;: "
           + "«&nbsp;il y a beaucoup de monde&nbsp;».",
        pourquoi: "Il y a beaucoup de monde dans l'autobus." },
    ],
    attente: "Tranchez les huit situations pour continuer.",
  },

  // ── 3. La règle, écrite comme un constat de ce qu'il vient de faire. ─────
  {
    id:   'le-test',
    type: 'notion',
    eye:  'Ce que vous venez de faire',
    menu: 'Le test',
    titre: "Vous avez séparé les endroits des personnes.",
    paras: [
      "Regardez votre colonne «&nbsp;il y a&nbsp;»&nbsp;: à chaque fois, il y avait un "
      + "<b>endroit</b> ou un <b>moment</b> — dans la salle, près de l'école, dans mon sac, "
      + "aujourd'hui. Dans l'autre colonne, il y avait toujours une <b>personne</b> qui possède.",

      "<b>Le test, à faire sur n'importe quelle phrase&nbsp;:</b> est-ce que je peux ajouter "
      + "«&nbsp;ici&nbsp;», «&nbsp;dans…&nbsp;», «&nbsp;près d'ici&nbsp;»&nbsp;? Si oui, c'est "
      + "<b>il y a</b>.",

      "Et voici la chose importante&nbsp;: dans «&nbsp;il y a&nbsp;», le mot «&nbsp;il&nbsp;» ne "
      + "désigne <b>personne</b>. Ce n'est ni un homme, ni la classe, ni l'autobus. Les trois mots "
      + "vont ensemble et se retiennent comme <b>un seul mot</b>. N'essayez pas de les traduire un "
      + "par un dans votre langue&nbsp;: ça ne marchera pas.",
    ],
    retenir: "Un endroit ou un moment → <b>il y a</b>. Une personne qui possède → <b>il a</b>. "
           + "Et «&nbsp;il y a&nbsp;» se retient comme un seul mot.",
    attente: "Lisez, puis continuez.",
  },

  // ── 4. Le premier piège : les trois mots ne bougent jamais. ──────────────
  {
    id:   'ca-ne-bouge-pas',
    type: 'verif',
    eye:  'Le piège',
    menu: 'Trois problèmes',
    titre: "Vous parlez de trois problèmes, pas d'un seul. Est-ce que la phrase change ?",
    consigne: "Vous écrivez au propriétaire de votre logement.",
    options: [
      { txt: "«&nbsp;<b>Il y a</b> trois problèmes dans l'appartement.&nbsp;»", juste: true },
      { txt: "«&nbsp;<b>Il y ont</b> trois problèmes dans l'appartement.&nbsp;»",
        rat_t: "C'est la faute de ceux qui ont bien compris qu'il y en a plusieurs.",
        rat: "Vous avez mis le verbe au pluriel, comme on le fait partout ailleurs. Ici, non&nbsp;: "
           + "les trois mots ne bougent <b>jamais</b>. Il y a un problème, il y a trois problèmes, "
           + "il y a cent personnes." },
      { txt: "«&nbsp;<b>Ils y a</b> trois problèmes dans l'appartement.&nbsp;»",
        rat_t: "Même idée, sur l'autre mot.",
        rat: "Vous avez mis le «&nbsp;s&nbsp;» du pluriel sur «&nbsp;il&nbsp;». Mais ce "
           + "«&nbsp;il&nbsp;» ne désigne personne&nbsp;: il n'y a rien à mettre au pluriel. "
           + "Les trois mots restent tels quels." },
    ],
    pourquoi: "<b>Il y a</b>, toujours. C'est la bonne nouvelle de ce parcours&nbsp;: trois mots "
            + "à retenir, et plus jamais rien à changer.",
    attente: "Choisissez une réponse pour continuer.",
  },

  // ── 5. Les trois emplois quotidiens. ─────────────────────────────────────
  {
    id:   'trois-emplois',
    type: 'notion',
    eye:  'Ce que ça vous rapporte',
    menu: 'Dix fois par jour',
    titre: "Trois mots, et vous pouvez décrire n'importe quel endroit.",
    paras: [
      "<b>Pour dire ce qu'il y a&nbsp;:</b> «&nbsp;<i>Il y a une pharmacie au coin de la "
      + "rue.</i>&nbsp;» «&nbsp;<i>Il y a du café dans la cuisine.</i>&nbsp;» Vous n'avez besoin "
      + "d'aucun autre verbe.",

      "<b>Pour demander&nbsp;:</b> mettez «&nbsp;est-ce que&nbsp;» devant. "
      + "«&nbsp;<i>Est-ce qu'il y a un autobus à huit heures&nbsp;?</i>&nbsp;» C'est la question "
      + "qui ouvre le plus de portes quand on arrive dans un endroit qu'on ne connaît pas.",

      "<b>Pour dire non&nbsp;:</b> «&nbsp;<i>Il n'y a pas de café.</i>&nbsp;» Attention à ce petit "
      + "changement&nbsp;: après «&nbsp;pas&nbsp;», «&nbsp;du café&nbsp;» devient «&nbsp;<b>de</b> "
      + "café&nbsp;», et «&nbsp;un autobus&nbsp;» devient «&nbsp;<b>d'</b>autobus&nbsp;».",
    ],
    retenir: "Il y a… · Est-ce qu'il y a…&nbsp;? · Il n'y a pas de… "
           + "Les trois mots du milieu ne changent jamais.",
    attente: "Lisez, puis continuez.",
  },

  // ── 6. Trier des phrases écrites. ────────────────────────────────────────
  {
    id:   'tri-phrases',
    type: 'tri',
    eye:  'À vous de trancher',
    menu: 'Six phrases',
    titre: "Six phrases. Lesquelles sont correctes ?",
    consigne: "Regardez deux choses seulement&nbsp;: les trois petits mots, et ce qui vient juste "
            + "après.",
    colonnes: [
      { id: 'ok',   t: 'Correct',   b: 'Correct' },
      { id: 'faux', t: 'Une faute', b: 'Une faute' },
    ],
    items: [
      { txt: "Il y a deux autobus le matin.", ok: 'ok',
        rat: "Deux autobus, et les trois mots ne bougent pas. C'est exactement la phrase à "
           + "garder en modèle.",
        pourquoi: "Il y a deux autobus. Juste." },
      { txt: "Dans ma rue, il ont une épicerie.", ok: 'faux',
        rat: "«&nbsp;Dans ma rue&nbsp;» annonce un endroit&nbsp;: il faut «&nbsp;<b>il y a</b> une "
           + "épicerie&nbsp;». La rue ne possède rien.",
        pourquoi: "Il faut « il y a une épicerie »." },
      { txt: "Est-ce qu'il y a un examen aujourd'hui ?", ok: 'ok',
        rat: "«&nbsp;Est-ce que&nbsp;» devant, et le reste ne bouge pas. C'est la question à "
           + "connaître par cœur.",
        pourquoi: "Est-ce qu'il y a… ? Juste." },
      { txt: "Il n'y a pas du lait dans le frigo.", ok: 'faux',
        rat: "Les trois mots sont bons. C'est après «&nbsp;pas&nbsp;» que ça coince&nbsp;: "
           + "«&nbsp;du lait&nbsp;» devient «&nbsp;<b>de</b> lait&nbsp;».",
        pourquoi: "Il faut « pas de lait »." },
      { txt: "Mon voisin a une grande famille.", ok: 'ok',
        rat: "Ici, une <b>personne</b> possède&nbsp;: «&nbsp;il a&nbsp;», sans le petit mot du "
           + "milieu. La phrase est juste, et c'est l'autre phrase du parcours.",
        pourquoi: "Une personne possède : il a." },
      { txt: "Il y ont beaucoup de monde à la clinique.", ok: 'faux',
        rat: "«&nbsp;Beaucoup de monde&nbsp;» fait penser au pluriel, et le verbe a suivi. Les "
           + "trois mots ne bougent jamais&nbsp;: «&nbsp;<b>il y a</b> beaucoup de monde&nbsp;».",
        pourquoi: "Il faut « il y a beaucoup de monde »." },
    ],
    attente: "Tranchez les six phrases pour continuer.",
  },

  // ── 7. La question du comptoir. ──────────────────────────────────────────
  {
    id:   'au-comptoir',
    type: 'verif',
    eye:  'Vérification',
    menu: 'Au comptoir',
    titre: "Vous cherchez une place dans un cours du soir. Vous demandez quoi ?",
    consigne: "Vous êtes au secrétariat. Vous voulez savoir si des places restent.",
    options: [
      { txt: "«&nbsp;Est-ce qu'il y a des places pour le cours du soir&nbsp;?&nbsp;»",
        juste: true },
      { txt: "«&nbsp;Est-ce qu'il a des places pour le cours du soir&nbsp;?&nbsp;»",
        rat_t: "La personne va se demander de qui vous parlez.",
        rat: "Sans le petit mot du milieu, vous demandez si <b>quelqu'un</b> possède des places — "
           + "mais vous ne dites pas qui. On vous répondra peut-être «&nbsp;qui ça&nbsp;?&nbsp;». "
           + "Vous, vous voulez savoir si des places <b>existent</b>." },
      { txt: "«&nbsp;Est-ce que c'est des places pour le cours du soir&nbsp;?&nbsp;»",
        rat_t: "Cette phrase existe, mais elle demande autre chose.",
        rat: "«&nbsp;C'est&nbsp;» sert à <b>nommer</b>&nbsp;: vous montreriez des chaises et vous "
           + "demanderiez si ce sont les places du cours. Ce n'est pas votre question." },
    ],
    pourquoi: "<b>Est-ce qu'il y a…&nbsp;?</b> C'est la question qui sert au secrétariat, à "
            + "l'épicerie, à la clinique et au téléphone.",
    attente: "Choisissez une réponse pour continuer.",
  },

  // ── 8. Ce qu'on entend vraiment, gardé pour la fin. ──────────────────────
  {
    id:   'ce-quon-entend',
    type: 'notion',
    eye:  'Ce qui reste',
    menu: "À l'oreille",
    titre: "Vous entendrez rarement les trois mots en entier.",
    paras: [
      "On a gardé ceci pour la fin, et c'est voulu&nbsp;: si on vous l'avait dit d'abord, vous "
      + "n'écririez plus jamais les trois mots. Or à l'écrit, il en faut trois.",

      "Mais quand les gens parlent vite, «&nbsp;il&nbsp;» disparaît presque toujours. Vous "
      + "entendrez «&nbsp;<i>y a personne au comptoir</i>&nbsp;», «&nbsp;<i>y a pas de "
      + "problème</i>&nbsp;», «&nbsp;<i>y a un autobus dans dix minutes</i>&nbsp;». Ce n'est pas "
      + "une autre phrase&nbsp;: c'est la même, dite vite.",

      "Alors faites deux choses différentes selon le moment. <b>Quand vous écoutez&nbsp;:</b> "
      + "cherchez le petit «&nbsp;ya&nbsp;», et vous saurez qu'on vous parle de ce qui existe "
      + "quelque part. <b>Quand vous écrivez&nbsp;:</b> les trois mots, en entier.",
    ],
    retenir: "À l'oreille&nbsp;: «&nbsp;ya&nbsp;». Sous votre crayon&nbsp;: "
           + "<b>il y a</b>, trois mots.",
    attente: "Lisez, puis continuez.",
  },

  // ── 9. Écrire, pas reconnaître. ──────────────────────────────────────────
  {
    id:   'votre-message',
    type: 'verif',
    eye:  'Vérification',
    menu: 'Votre message',
    titre: "Vous écrivez à l'école. Quelle version tient d'un bout à l'autre ?",
    consigne: "Vous prévenez que vous arriverez en retard. Trois versions du même message&nbsp;: "
            + "une seule est correcte partout.",
    options: [
      { txt: "«&nbsp;Bonjour. Il y a un problème avec l'autobus ce matin. Il n'y a pas de bus "
           + "avant 9 h. J'arrive en retard.&nbsp;»", juste: true },
      { txt: "«&nbsp;Bonjour. Il a un problème avec l'autobus ce matin. Il n'y a pas de bus "
           + "avant 9 h. J'arrive en retard.&nbsp;»",
        rat_t: "La deuxième phrase est parfaite. C'est la première qui a lâché.",
        rat: "Vous avez écrit «&nbsp;il n'y a pas&nbsp;» ensuite&nbsp;: vous connaissez donc les "
           + "trois mots. Au début, «&nbsp;il a un problème&nbsp;» fait croire qu'une personne a un "
           + "problème — l'école se demandera qui." },
      { txt: "«&nbsp;Bonjour. Il y a un problème avec l'autobus ce matin. Il n'y a pas du bus "
           + "avant 9 h. J'arrive en retard.&nbsp;»",
        rat_t: "Le début est juste. C'est le mot après «&nbsp;pas&nbsp;» qui reste.",
        rat: "Après «&nbsp;pas&nbsp;», «&nbsp;du&nbsp;» devient «&nbsp;<b>de</b>&nbsp;»&nbsp;: "
           + "«&nbsp;il n'y a pas <b>de</b> bus&nbsp;». C'est le seul mot qui bouge dans cette "
           + "phrase — les trois autres, jamais." },
    ],
    pourquoi: "Il y a un problème… il n'y a pas de bus. <b>C'est tout le parcours en deux "
            + "phrases.</b>",
    attente: "Choisissez une réponse pour continuer.",
  },

  // ── 10. La fermeture : le même cas qu'à l'écran 1. ───────────────────────
  {
    id:   'fermeture',
    type: 'verif',
    eye:  'La dernière',
    menu: 'Pour finir',
    titre: "On revient aux douze chaises de la classe.",
    consigne: "Cette fois, vous êtes vingt élèves et vous voulez le signaler à votre "
            + "enseignante. Vous dites quoi&nbsp;?",
    options: [
      { txt: "«&nbsp;Il y a douze chaises, et nous sommes vingt.&nbsp;»", juste: true },
      { txt: "«&nbsp;Il y ont douze chaises, et nous sommes vingt.&nbsp;»",
        rat_t: "Douze chaises, alors le verbe a suivi.",
        rat: "C'est le piège de l'écran 4, et il revient toujours au moment où l'on compte. Les "
           + "trois mots ne bougent pas, même devant cent chaises&nbsp;: <b>il y a</b> douze "
           + "chaises." },
      { txt: "«&nbsp;La classe a douze chaises, et nous sommes vingt.&nbsp;»",
        rat_t: "Cette phrase se dit — et elle ne dit pas ce que vous voulez dire.",
        rat: "Vous faites de la classe une personne qui possède des chaises. On vous comprendra, "
           + "mais ce que vous voulez signaler, c'est ce qu'il y a <b>dans la salle</b>, devant "
           + "vous. C'est «&nbsp;il y a&nbsp;»." },
    ],
    pourquoi: "Vous avez fait les trois choses&nbsp;: reconnaître qu'un endroit demande "
            + "«&nbsp;il y a&nbsp;», ne jamais faire bouger les trois mots, et reconnaître le "
            + "«&nbsp;ya&nbsp;» que vous entendrez dehors.",
    attente: "Choisissez une réponse pour finir.",
  },

];
