// ═══════════════════════════════════════════════════════════════════════════
// Point express — Est-ce qu'on me pose une question ?
//
// Savoirs n1-s03 (phrases interrogatives) et n1-s21 (système prosodique).
// Dix minutes, dix écrans. Une ORDONNANCE : l'enseignant l'envoie à un élève
// qui reste muet quand on lui demande quelque chose — parce qu'il n'a pas
// entendu qu'on lui demandait quelque chose.
//
// ── Ce qui le sépare des mini-leçons ───────────────────────────────────────
// Deux existent sur ce terrain, et l'élève les a probablement lues :
//   · `module-n1-orientation`, « C'est · Ce n'est pas · C'est ici ? » — trois
//     phrases devant une porte, dont une question. La montée de la voix y est
//     une ligne d'un tableau, entre deux autres formes à produire.
//   · `module-n5-voisinage`, « L'intonation : ce que la voix dit avant les
//     mots » — complète, mais au niveau 5, et elle ENSEIGNE la prosodie :
//     quatre courbes nommées, montée au milieu, exclamation. Un élève de
//     niveau 1 n'a pas de place pour ça.
// Existe aussi le point express `poser-une-question` (niveau 5) : il traite le
// CHOIX de la forme quand on parle. Celui-ci traite l'inverse — ce qu'on
// entend, et la seconde où il faut décider de répondre ou de se taire.
//
// Les cinq écarts tenus :
//   1. INDUCTIF. Aucune règle avant l'écran 4. Les trois premiers écrans font
//      ÉCOUTER et trancher. La règle est écrite comme un constat de ce que
//      l'élève vient de faire.
//   2. AUCUN MOT SAVANT. Ni « intonation », ni « interrogative », ni
//      « déclarative », ni courbe dessinée. La voix monte, ou elle descend :
//      c'est tout le vocabulaire du point. Le programme lui-même demande de
//      « reconnaître », pas de nommer.
//   3. PARTIEL. Jamais la liste des formes de question (est-ce que,
//      inversion, particule -tu). Un seul test, réutilisable : écouter la fin,
//      puis chercher un mot au début ou à la fin.
//   4. LE PIÈGE EST DANS LE TRI, pas après. « D'où viens-tu ? » est une
//      question dont la voix NE monte PAS. L'élève se trompe, et son
//      rattrapage lui apprend la moitié qui manque.
//   5. L'ENJEU, PAS LA FORME. Ne pas entendre une question, ce n'est pas une
//      faute de grammaire : c'est un silence qu'on prend pour de l'impolitesse
//      au comptoir. Chaque écran a une conséquence.
//
// Extraits : `module-n1-presenter`, rejoués par chemin. Aucun média neuf. Le
// texte des extraits est CACHÉ par défaut (le gabarit offre « Voir le texte »)
// partout où l'élève doit trancher à l'oreille, montré partout où il lit.
// ═══════════════════════════════════════════════════════════════════════════

const PARCOURS = {
  slug:     'question-ou-affirmation',
  module:   'module-n1-presenter',
  titre:    "Est-ce qu'on me pose une question ?",
  surtitre: "Point express · 10 minutes",
  niveau:   1,
  savoir:   'n1-s03 · n1-s21',
};

const ECRANS = [

  // ── 1. On tranche AVANT de savoir. ───────────────────────────────────────
  {
    id:   'depart',
    type: 'verif',
    eye:  'Une question, pour commencer',
    menu: 'Le premier jour',
    titre: "Vous arrivez au centre. Un homme vous parle. Écoutez.",
    consigne: "Écoutez une fois, deux fois. Puis choisissez. "
            + "Répondez avec ce que vous savez déjà — c'est fait exprès.",
    sons: [
      { fichier: 'appli/line_01_monsieur_tremblay.mp3',
        qui: "Monsieur Tremblay, à l'entrée" },
    ],
    options: [
      { txt: "Il me demande quelque chose. Je dois répondre.", juste: true },
      { txt: "Il me dit quelque chose. J'écoute, c'est tout.",
        rat_t: "Il attend une réponse.",
        rat: "Écoutez encore la fin&nbsp;: «&nbsp;une nouvelle élève&nbsp;». La voix "
           + "<b>monte</b>. Il vous demande quelque chose. Si vous ne dites rien, il attend, "
           + "et vous avez l'air impoli." },
      { txt: "Il n'y a pas de mot pour dire que c'est une question.",
        rat_t: "C'est vrai. Et c'est le problème.",
        rat: "Il n'y a ni «&nbsp;est-ce que&nbsp;», ni mot spécial. Alors il reste une chose, "
           + "une seule&nbsp;: la voix. C'est ce point express." },
    ],
    pourquoi: "«&nbsp;Vous êtes une nouvelle élève&nbsp;?&nbsp;» Il demande. "
            + "Les mots ne le disent pas. <b>La voix le dit.</b>",
    attente: "Choisissez une réponse pour continuer.",
  },

  // ── 2. On écoute. Toujours pas de règle. ─────────────────────────────────
  {
    id:   'deux-fins',
    type: 'notion',
    eye:  'Écoutez seulement la fin',
    menu: 'Deux fins',
    titre: "Amina demande, puis Amina répond. Écoutez la fin des deux phrases.",
    paras: [
      "N'essayez pas de comprendre tous les mots. Écoutez seulement la <b>dernière syllabe</b>. "
      + "Écoutez la première phrase. Écoutez la deuxième. Puis les deux, l'une après l'autre.",

      "Les deux fins ne sont pas pareilles. Vous l'entendez. On ne vous dit pas encore pourquoi.",
    ],
    sons: [
      { fichier: 't1b/line_04_amina.mp3', qui: 'Amina, première phrase',
        texte: "Tu as des enfants ?", montrer: true },
      { fichier: 't1b/line_06_amina.mp3', qui: 'Amina, deuxième phrase',
        texte: "J'ai un fils. Il a six ans.", montrer: true },
    ],
    retenir: "Réécoutez trois fois. <b>La fin, seulement la fin.</b>",
    attente: "Écoutez les deux extraits, puis continuez.",
  },

  // ── 3. Le cœur : six extraits, et le piège dedans. ───────────────────────
  {
    id:   'tri-six',
    type: 'tri',
    eye:  'À vous de trancher',
    menu: 'Six extraits',
    titre: "Six extraits. Est-ce qu'on me demande, ou est-ce qu'on me dit ?",
    consigne: "Le texte est caché. C'est voulu&nbsp;: écoutez, puis choisissez. "
            + "Vous pouvez ouvrir «&nbsp;Voir le texte&nbsp;» après.",
    sons: [
      { fichier: 'prep/line_03_madame_roy.mp3', qui: 'Extrait 1',
        texte: "Amina. Vous pouvez épeler, s'il vous plaît ?" },
      { fichier: 't1/line_05_lin.mp3', qui: 'Extrait 2',
        texte: "Je viens du Vietnam. J'habite à Montréal." },
      { fichier: 't2/line_04_paul.mp3', qui: 'Extrait 3',
        texte: "De rien. Vous comprenez maintenant ?" },
      { fichier: 't2/line_02_paul.mp3', qui: 'Extrait 4',
        texte: "Pas de problème. Je répète plus lentement." },
      { fichier: 't1/line_03_lin.mp3', qui: 'Extrait 5',
        texte: "D'où viens-tu ?" },
      { fichier: 'appli/line_08_amina.mp3', qui: 'Extrait 6',
        texte: "Ah ! J'habite au 4520, rue Bélanger." },
    ],
    colonnes: [
      { id: 'q', t: 'On me demande', b: 'On me demande' },
      { id: 'a', t: 'On me dit',     b: 'On me dit' },
    ],
    items: [
      { txt: "Extrait 1", ok: 'q',
        rat: "La voix monte à la fin&nbsp;: «&nbsp;s'il vous plaît&nbsp;?&nbsp;». "
           + "On vous demande d'épeler votre nom. On attend que vous parliez.",
        pourquoi: "La voix monte. On demande." },
      { txt: "Extrait 2", ok: 'a',
        rat: "La voix descend et s'arrête. Lin donne deux informations sur lui&nbsp;: "
           + "son pays, sa ville. Il n'attend rien de vous.",
        pourquoi: "La voix descend. On donne une information." },
      { txt: "Extrait 3", ok: 'q',
        rat: "La voix monte sur «&nbsp;maintenant&nbsp;». Monsieur Paul veut savoir si vous "
           + "avez compris. Un «&nbsp;oui&nbsp;» suffit — mais il faut le dire.",
        pourquoi: "La voix monte. On demande." },
      { txt: "Extrait 4", ok: 'a',
        rat: "La voix descend. C'est une promesse, pas une question&nbsp;: il va répéter.",
        pourquoi: "La voix descend. On vous dit ce qu'on va faire." },
      { txt: "Extrait 5", ok: 'q', sous: "attention : celui-ci ne fait pas comme les autres",
        rat: "C'est une <b>question</b>, et pourtant la voix ne monte pas. Vous avez eu raison "
           + "d'écouter la fin — c'est ici que ça ne suffit pas. Il y a un mot au début, "
           + "et c'est lui qui pose la question. On y revient dans deux écrans.",
        pourquoi: "Une question, mais la voix descend. Le mot du début fait tout." },
      { txt: "Extrait 6", ok: 'a',
        rat: "La voix descend. Amina donne son adresse. C'est une réponse, pas une question.",
        pourquoi: "La voix descend. On donne une information." },
    ],
    attente: "Tranchez les six extraits pour continuer.",
  },

  // ── 4. La règle, écrite comme un constat. ────────────────────────────────
  {
    id:   'la-regle',
    type: 'notion',
    eye:  'Ce que vous venez de faire',
    menu: 'La voix monte',
    titre: "Vous n'avez pas écouté les mots. Vous avez écouté la fin.",
    paras: [
      "<b>La voix monte à la fin&nbsp;: on vous demande.</b> "
      + "<b>La voix descend&nbsp;: on vous dit.</b> "
      + "C'est vrai partout — au comptoir, en classe, au téléphone, dans la rue.",

      "Regardez ces deux phrases&nbsp;: «&nbsp;Vous habitez ici.&nbsp;» et "
      + "«&nbsp;Vous habitez ici&nbsp;?&nbsp;» Les mots sont les mêmes. L'ordre est le même. "
      + "À l'écrit, un petit signe change à la fin. À l'oral, il n'y a pas de signe&nbsp;: "
      + "il n'y a que la voix.",

      "Mais l'extrait 5 ne montait pas, et c'était une question. Il y avait un <b>mot</b> "
      + "devant. C'est la deuxième moitié, et elle arrive tout de suite.",
    ],
    retenir: "Écoutez <b>la fin</b>. Elle monte&nbsp;? On vous demande quelque chose. "
           + "Répondez.",
    attente: "Lisez, puis continuez.",
  },

  // ── 5. Le piège, isolé. ──────────────────────────────────────────────────
  {
    id:   'le-mot-devant',
    type: 'verif',
    eye:  'Le cas qui trompe',
    menu: 'La voix descend',
    titre: "Madame Roy vous parle. Sa voix descend à la fin. Alors ?",
    consigne: "Écoutez, puis choisissez.",
    sons: [
      { fichier: 'prep/line_01_madame_roy.mp3', qui: 'Madame Roy, au comptoir' },
    ],
    options: [
      { txt: "C'est une question. Je dis mon nom.", juste: true },
      { txt: "Elle me dit quelque chose. J'écoute.",
        rat_t: "Elle attend votre nom.",
        rat: "La voix descend, c'est vrai. Mais écoutez le <b>premier mot</b>&nbsp;: "
           + "«&nbsp;Comment…&nbsp;». Ce mot pose la question tout seul. La voix n'a plus "
           + "besoin de monter." },
      { txt: "Je ne sais pas. La voix ne monte pas.",
        rat_t: "Vous avez bien écouté. Il manque une chose.",
        rat: "La voix est votre premier outil, et il est bon. Le second, c'est un "
           + "<b>petit mot</b> au début&nbsp;: comment, où, quand, qui. Quand il est là, "
           + "c'est une question, même si la voix descend." },
    ],
    pourquoi: "«&nbsp;Comment vous appelez-vous&nbsp;?&nbsp;» Le mot <b>comment</b> fait la "
            + "question. La voix descend, et c'est normal.",
    attente: "Choisissez une réponse pour continuer.",
  },

  // ── 6. Les mots, et où ils se cachent. ───────────────────────────────────
  {
    id:   'les-mots',
    type: 'notion',
    eye: 'La deuxième moitié',
    menu: 'Les petits mots',
    titre: "Six mots. Quand vous en entendez un, c'est une question.",
    paras: [
      "<b>Qui · Quand · Où · Comment · Combien · Quel</b> (quelle, quels, quelles). "
      + "Six mots, pas plus. Apprenez-les comme six mots, pas comme une leçon.",

      "Attention&nbsp;: le mot n'est pas toujours au début. Au Québec, on le met souvent "
      + "à la <b>fin</b>. Écoutez les deux extraits&nbsp;: c'est la même question, deux fois.",
    ],
    sons: [
      { fichier: 'appli/line_05_monsieur_tremblay.mp3', qui: 'Le mot est à la fin',
        texte: "Merci. Vous habitez à quelle adresse ?", montrer: true },
      { fichier: 'appli/line_07_monsieur_tremblay.mp3', qui: 'Le mot est au début',
        texte: "Votre adresse. Où habitez-vous ?", montrer: true },
    ],
    retenir: "Un de ces six mots, au début <b>ou</b> à la fin&nbsp;: c'est une question. "
           + "Vous n'avez pas besoin d'écouter la voix.",
    attente: "Écoutez les deux extraits, puis continuez.",
  },

  // ── 7. La conséquence : je n'ai pas compris. ─────────────────────────────
  {
    id:   'pas-compris',
    type: 'verif',
    eye:  'Vérification',
    menu: "Je n'ai pas compris",
    titre: "Vous avez entendu que c'est une question. Mais vous n'avez pas compris les mots.",
    consigne: "Vous faites quoi&nbsp;? Écoutez ce qu'Amina dit, elle.",
    sons: [
      { fichier: 'appli/line_06_amina.mp3', qui: 'Amina, devant monsieur Tremblay',
        texte: "Pardon ? Plus lentement, s'il vous plaît.", montrer: true },
    ],
    options: [
      { txt: "Je dis : « Pardon ? Plus lentement, s'il vous plaît. »", juste: true },
      { txt: "Je dis « oui » pour être poli.",
        rat_t: "«&nbsp;Oui&nbsp;» est dangereux.",
        rat: "Vous ne savez pas à quoi vous dites oui. On vous demande peut-être votre "
           + "adresse, ou de revenir demain. Un «&nbsp;oui&nbsp;» au hasard coûte souvent "
           + "un deuxième rendez-vous." },
      { txt: "Je ne dis rien et j'attends.",
        rat_t: "Le silence ne dit pas «&nbsp;je n'ai pas compris&nbsp;».",
        rat: "La personne devant vous croit que vous ne voulez pas répondre. Elle ne peut pas "
           + "deviner. Quatre mots règlent tout&nbsp;: «&nbsp;Pardon&nbsp;? Plus lentement, "
           + "s'il vous plaît.&nbsp;»" },
    ],
    pourquoi: "<b>Entendre la question et ne pas comprendre les mots, ce n'est pas grave.</b> "
            + "Le grave, c'est de se taire. Amina fait répéter, et l'homme répète.",
    attente: "Choisissez une réponse pour continuer.",
  },

  // ── 8. Le cas fréquent : on répond ET on demande. ────────────────────────
  {
    id:   'et-toi',
    type: 'verif',
    eye:  'Le cas qui revient tous les jours',
    menu: '« Et toi ? »',
    titre: "Lin répond à Amina. Puis, dans la même phrase, il fait autre chose.",
    consigne: "Écoutez jusqu'au bout. Lin fait deux choses&nbsp;: lesquelles&nbsp;?",
    sons: [
      { fichier: 't1b/line_05_lin.mp3', qui: 'Lin' },
    ],
    options: [
      { txt: "Il répond, puis il me pose la même question.", juste: true },
      { txt: "Il répond deux fois.",
        rat_t: "La fin est différente du début.",
        rat: "Réécoutez. Le début descend&nbsp;: «&nbsp;j'ai deux enfants&nbsp;». La fin monte&nbsp;: "
           + "«&nbsp;Et toi&nbsp;?&nbsp;» Deux mots seulement, mais la voix monte&nbsp;: "
           + "c'est une question." },
      { txt: "Il répond, puis il dit au revoir.",
        rat_t: "«&nbsp;Et toi&nbsp;?&nbsp;» n'est pas au revoir.",
        rat: "C'est la façon la plus courte de renvoyer la question. On l'entend cent fois "
           + "par jour&nbsp;: «&nbsp;Et vous&nbsp;?&nbsp;», «&nbsp;Et toi&nbsp;?&nbsp;» "
           + "À vous de parler." },
    ],
    pourquoi: "«&nbsp;Oui, j'ai deux enfants. Et toi&nbsp;?&nbsp;» Une phrase, deux voix&nbsp;: "
            + "elle descend, puis elle monte. <b>Écoutez toujours jusqu'au dernier mot.</b>",
    attente: "Choisissez une réponse pour continuer.",
  },

  // ── 9. Produire, pas reconnaître. ────────────────────────────────────────
  {
    id:   'a-vous',
    type: 'verif',
    eye: 'À vous de demander',
    menu: 'Votre question',
    titre: "Vous voulez savoir si le cours commence à huit heures. Vous dites quoi ?",
    consigne: "Vous connaissez la phrase «&nbsp;Le cours commence à huit heures.&nbsp;» "
            + "Comment en faire une question&nbsp;?",
    options: [
      { txt: "« Le cours commence à huit heures ? » — en faisant monter la voix à la fin.",
        juste: true },
      { txt: "« Le cours commence à huit heures. » — la même phrase, dite pareil.",
        rat_t: "On croira que vous donnez l'information.",
        rat: "Vous dites alors à la secrétaire une chose qu'elle sait déjà. Elle répondra "
           + "«&nbsp;oui&nbsp;» ou rien du tout, et vous n'aurez rien appris. "
           + "<b>Faites monter la voix sur «&nbsp;heures&nbsp;».</b>" },
      { txt: "« Commence le cours à huit heures ? » — en changeant l'ordre des mots.",
        rat_t: "Ne changez pas l'ordre.",
        rat: "En français, on peut changer l'ordre pour poser une question, mais c'est "
           + "difficile et ce n'est pas nécessaire. <b>Gardez vos mots, montez la voix.</b> "
           + "C'est ce que tout le monde fait ici." },
    ],
    pourquoi: "Gardez la phrase. Montez la voix sur le dernier mot. "
            + "<b>C'est la question la plus facile du français, et elle marche partout.</b>",
    attente: "Choisissez une réponse pour continuer.",
  },

  // ── 10. La fermeture : le même extrait qu'à l'écran 1. ───────────────────
  {
    id:   'fermeture',
    type: 'verif',
    eye:  'La dernière',
    menu: 'Pour finir',
    titre: "On revient au premier jour. Écoutez encore monsieur Tremblay.",
    consigne: "Cette fois, vous savez. Vous dites quoi&nbsp;?",
    sons: [
      { fichier: 'appli/line_01_monsieur_tremblay.mp3',
        qui: "Monsieur Tremblay, à l'entrée",
        texte: "Bonjour. Vous êtes une nouvelle élève ?", montrer: true },
    ],
    options: [
      { txt: "« Oui. Je m'appelle Amina Benali. »", juste: true },
      { txt: "Rien. J'attends la suite.",
        rat_t: "Il attend, lui aussi.",
        rat: "Sa voix est montée sur «&nbsp;élève&nbsp;». Il a posé une question et il "
           + "s'est arrêté. Tant que vous ne dites rien, il ne dit rien&nbsp;: c'est votre tour." },
      { txt: "« Pardon ? Plus lentement, s'il vous plaît. »",
        rat_t: "Bonne phrase, mauvais moment.",
        rat: "Gardez-la pour quand vous n'avez <b>pas compris</b>. Ici, vous avez compris&nbsp;: "
           + "il demande si vous êtes nouvelle. Faire répéter une question facile fait perdre "
           + "du temps aux deux." },
    ],
    pourquoi: "La voix monte&nbsp;: on vous demande. Un des six mots&nbsp;: on vous demande. "
            + "<b>Dans les deux cas, c'est votre tour de parler.</b>",
    attente: "Choisissez une réponse pour finir.",
  },

];
