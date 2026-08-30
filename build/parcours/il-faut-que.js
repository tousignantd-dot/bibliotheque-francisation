// ═══════════════════════════════════════════════════════════════════════════
// Point express — « Il faut que… » : un seul emploi, six verbes
//
// Savoir n5-s34. Dix minutes, dix écrans.
//
// ── L'écart avec les mini-leçons, qui sont nombreuses ─────────────────────
// Cinq modules de niveau 5 portent déjà une mini-leçon sur « il faut que »
// (n5-rendezvous, n5-services, n5-degat, n5-ecole, n5-logement), et toutes
// enseignent la MÊME chose de la MÊME façon : la fabrication du subjonctif à
// partir du « ils » du présent, puis une liste de formes à savoir par cœur.
// Un élève envoyé ici l'a lue au moins une fois. Le point express ne la
// reprend donc pas :
//
//   1. AUCUNE RÈGLE DE FABRICATION. La règle du « ils » ne sert à rien sur
//      les verbes qui posent problème — vienne, soit, ait, fasse, aille,
//      puisse sont précisément ceux qu'elle n'explique pas. Et sur tous les
//      autres, la forme est celle qu'on écrivait déjà. Le point express
//      retourne le constat : il n'y a que six formes à connaître, le reste
//      s'écrit tout seul.
//   2. INDUCTIF. L'élève trie six phrases avant qu'on ait prononcé le mot
//      « subjonctif ». La règle de l'écran 4 est écrite comme un constat de
//      ce qu'il vient de faire.
//   3. LE TEST N'EST PAS GRAMMATICAL, IL EST SÉMANTIQUE : « est-ce que la
//      phrase dit à qui ? » Une liste s'oublie ; cette question se pose sur
//      n'importe quelle phrase.
//   4. L'ÉCHAPPATOIRE EST ENSEIGNÉE (écran 6). Les mini-leçons présentent
//      « il faut » + infinitif comme un cas voisin ; ici c'est une compétence
//      à part entière — savoir se sortir d'une phrase qu'on ne sait pas finir
//      vaut mieux que de la rater.
//   5. LE MÉTALANGAGE ARRIVE À L'ÉCRAN 4, et le point dit à l'élève qu'il
//      peut s'en passer.
//
// Le découpage est volontairement plus étroit que le programme : un seul
// déclencheur, « il faut que », et rien sur « je veux que », « avant que »,
// « pour que » ni sur le doute. C'est ce qu'un élève de niveau 5 entend
// vraiment à un comptoir, dans une clinique ou à l'école.
//
// Extraits : `module-n5-services` — les quatre « il faut que » du module,
// rejoués par chemin. Aucun média neuf. Aucun des six points express déjà
// écrits ne tire de ce module : les cinq autres viennent tous de
// `module-n5-rendezvous`.
// ═══════════════════════════════════════════════════════════════════════════

const PARCOURS = {
  slug:     'il-faut-que',
  module:   'module-n5-services',
  titre:    "« Il faut que… » : un seul emploi, six verbes",
  surtitre: "Point express · 10 minutes",
  niveau:   5,
  savoir:   'n5-s34',
};

const ECRANS = [

  // ── 1. Une décision, sans qu'aucune règle ait été donnée. ────────────────
  {
    id:   'depart',
    type: 'verif',
    eye:  'Une question, pour commencer',
    menu: 'Deux phrases',
    titre: "Le comptoir vous répond. Une seule de ces deux phrases se dit. Laquelle ?",
    consigne: "Répondez avec ce que vous savez déjà — ou à l'oreille. On expliquera après&nbsp;: "
            + "c'est fait exprès.",
    options: [
      { txt: "« Il faut que vous venez avec votre bail. »",
        rat_t: "C'est la forme du présent ordinaire, et elle ne passe pas ici.",
        rat: "«&nbsp;Vous venez&nbsp;» est juste partout ailleurs&nbsp;: <i>vous venez demain</i>, "
           + "<i>vous venez souvent</i>. Mais après «&nbsp;il faut que&nbsp;», le verbe change de "
           + "forme. C'est le seul endroit où ça arrive, et c'est tout le sujet de ces dix minutes." },
      { txt: "« Il faut que vous veniez avec votre bail. »", juste: true },
      { txt: "Les deux se disent.",
        rat_t: "Une seule, et l'écart s'entend.",
        rat: "«&nbsp;Venez&nbsp;» et «&nbsp;veniez&nbsp;» ne se prononcent pas pareil&nbsp;: "
           + "il y a une syllabe de plus. À un comptoir, la personne devant vous entend la "
           + "différence même si elle ne vous corrige pas." },
    ],
    pourquoi: "«&nbsp;Il faut que vous <b>veniez</b>&nbsp;». Gardez la phrase entière pour "
            + "l'instant&nbsp;; on va voir tout de suite d'où vient ce changement.",
    attente: "Choisissez une réponse pour continuer.",
  },

  // ── 2. On écoute. Aucune règle encore : une observation. ─────────────────
  {
    id:   'deux-obligations',
    type: 'notion',
    eye:  'Écoutez deux fois la même chose',
    menu: 'Deux obligations',
    titre: "Deux personnes, deux comptoirs, la même construction.",
    paras: [
      "Écoutez les deux extraits. Chaque fois, quelqu'un annonce une obligation. Ne cherchez pas "
      + "encore de règle&nbsp;: repérez seulement <b>à qui</b> l'obligation s'adresse.",

      "Dans le premier, c'est <b>toi</b>. Dans le second, c'est <b>vous</b>. Dans les deux, le mot "
      + "<b>que</b> arrive juste après «&nbsp;il faut&nbsp;» — et le verbe qui suit n'est pas tout "
      + "à fait celui qu'on attendait.",
    ],
    sons: [
      { fichier: 'prep/line_12_pierre-luc.mp3', qui: 'Pierre-Luc, un voisin',
        texte: "Pas pour les résidents, dans la plupart des cas. Mais il faut que tu apportes une "
             + "preuve que tu habites la ville." },
      { fichier: 't3/line_10_gaetan.mp3', qui: 'Gaétan, préposé au comptoir',
        texte: "Tout à fait. Il faut que vous me montriez deux pièces&nbsp;: une avec votre photo, "
             + "et une avec votre adresse." },
    ],
    retenir: "Écoutez le second une deuxième fois&nbsp;: «&nbsp;montr<b>iez</b>&nbsp;», "
           + "pas «&nbsp;montrez&nbsp;». Une syllabe de plus.",
    attente: "Écoutez les deux extraits, puis continuez.",
  },

  // ── 3. Le cœur : on trie, avant qu'aucune règle n'ait été dite. ──────────
  {
    id:   'tri-vise',
    type: 'tri',
    eye:  'À vous de trancher',
    menu: 'Six phrases',
    titre: "Six phrases affichées à un comptoir. Lesquelles visent quelqu'un ?",
    consigne: "Une seule question à vous poser sur chacune&nbsp;: est-ce que la phrase dit "
            + "<b>à qui</b>&nbsp;? Ne regardez pas la forme du verbe pour l'instant.",
    colonnes: [
      { id: 'qui',  t: 'La phrase dit à qui',   b: 'Elle dit à qui' },
      { id: 'tous', t: 'Elle ne dit à personne', b: 'Elle ne dit à personne' },
    ],
    items: [
      { txt: "Il faut apporter une preuve d'adresse.", ok: 'tous',
        rat: "Personne n'est nommé&nbsp;: ni vous, ni moi, ni elle. C'est l'affiche au mur, "
           + "elle vaut pour tout le monde qui entre.",
        pourquoi: "Personne n'est nommé. C'est la règle générale." },
      { txt: "Il faut que vous apportiez votre bail.", ok: 'qui',
        rat: "«&nbsp;Vous&nbsp;» est là, juste après «&nbsp;que&nbsp;». La phrase ne vaut plus "
           + "pour tout le monde&nbsp;: elle vous vise, vous.",
        pourquoi: "« Vous » est nommé." },
      { txt: "Il faut être là avant seize heures.", ok: 'tous',
        rat: "Le comptoir ferme à seize heures pour tout le monde. Aucun nom, aucun pronom.",
        pourquoi: "Aucun nom. L'horaire vaut pour tous." },
      { txt: "Il faut que je sois là avant seize heures.", ok: 'qui',
        rat: "Même horaire, mais la phrase parle de <b>moi</b>&nbsp;: c'est mon problème à moi, "
           + "pas une règle affichée.",
        pourquoi: "« Je » est nommé." },
      { txt: "Il faut faire la demande en personne.", ok: 'tous',
        rat: "C'est la procédure du service, écrite sur la page Web. Elle ne s'adresse à "
           + "personne en particulier.",
        pourquoi: "La procédure, sans destinataire." },
      { txt: "Il faut qu'elle fasse la demande elle-même.", ok: 'qui',
        rat: "«&nbsp;Elle&nbsp;»&nbsp;: une personne précise, dont on parle. La phrase la vise "
           + "aussi sûrement qu'un «&nbsp;vous&nbsp;».",
        pourquoi: "« Elle » est nommée." },
    ],
    attente: "Tranchez les six phrases pour continuer.",
  },

  // ── 4. La règle, écrite comme un constat de ce qu'il vient de faire. ─────
  {
    id:   'le-mot-que',
    type: 'notion',
    eye:  'Ce que vous venez de faire',
    menu: 'Le mot « que »',
    titre: "Vous avez trié sur un seul mot, et vous ne l'avez peut-être pas remarqué.",
    paras: [
      "Regardez votre colonne «&nbsp;la phrase dit à qui&nbsp;». Les trois phrases contiennent "
      + "<b>que</b>. Les trois autres ne le contiennent pas. C'est aussi net que ça&nbsp;: "
      + "<b>quand on nomme la personne, on met «&nbsp;que&nbsp;» ; quand on ne nomme personne, "
      + "le verbe reste à l'infinitif.</b>",

      "Et c'est le mot «&nbsp;que&nbsp;» qui déclenche le changement de forme que vous avez "
      + "entendu à l'écran&nbsp;2&nbsp;: <i>vous montrez</i> devient <i>que vous montriez</i>, "
      + "<i>elle fait</i> devient <i>qu'elle fasse</i>. Le verbe ne change jamais tout seul&nbsp;; "
      + "il change parce que «&nbsp;que&nbsp;» est passé devant.",

      "Cette forme porte un nom&nbsp;: le <b>subjonctif</b>. Votre enseignant l'emploiera, alors "
      + "autant le savoir. Mais vous n'en avez pas besoin pour vous en servir&nbsp;: la question "
      + "à vous poser reste «&nbsp;est-ce que je dis à qui&nbsp;?&nbsp;»",
    ],
    retenir: "Je nomme quelqu'un → <b>que</b> + la forme qui change. "
           + "Je ne nomme personne → l'infinitif, et rien à faire.",
    attente: "Lisez, puis continuez.",
  },

  // ── 5. Le renversement : presque rien ne change, en réalité. ─────────────
  {
    id:   'six-verbes',
    type: 'notion',
    eye:  'La bonne nouvelle',
    menu: 'Six verbes, pas plus',
    titre: "Sur la plupart des verbes, vous écrivez déjà la bonne forme sans le savoir.",
    paras: [
      "Écoutez Gaétan. Il dit «&nbsp;il faut qu'elle <b>date</b> de moins de trois mois&nbsp;». "
      + "Et si la facture était vieille, il aurait dit «&nbsp;elle date de l'an dernier&nbsp;». "
      + "<b>Exactement le même mot.</b> C'est le cas de la grande majorité des verbes&nbsp;: "
      + "qu'elle arrive, que je paie, que vous signiez, qu'il travaille.",

      "Ce qui vous fait trébucher, ce sont <b>six verbes</b>, toujours les mêmes, et vous les "
      + "connaissez déjà par ailleurs&nbsp;: "
      + "<b>venir → que je vienne · être → que je sois · avoir → que j'aie · "
      + "faire → que je fasse · aller → que j'aille · pouvoir → que je puisse.</b>",

      "Six formes. Pas une conjugaison complète, pas un tableau&nbsp;: six mots, à reconnaître "
      + "quand on vous les dit et à sortir quand vous en avez besoin. Le reste s'écrit tout seul.",
    ],
    sons: [
      { fichier: 't3/line_14_gaetan.mp3', qui: 'Gaétan, sur les pièces acceptées',
        texte: "Alors il fait la job. Ce qui manque parfois, c'est une facture trop vieille — "
             + "il faut qu'elle date de moins de trois mois." },
    ],
    retenir: "Six verbes à savoir&nbsp;: <b>venir, être, avoir, faire, aller, pouvoir</b>. "
           + "Partout ailleurs, écrivez ce que vous auriez écrit.",
    attente: "Écoutez, puis continuez.",
  },

  // ── 6. L'échappatoire, enseignée comme une compétence. ───────────────────
  {
    id:   'la-sortie',
    type: 'verif',
    eye:  'Quand vous bloquez',
    menu: 'La sortie de secours',
    titre: "Vous êtes au comptoir. La forme ne vient pas. Que dites-vous ?",
    consigne: "Vous voulez dire que vous allez revenir avec une facture récente, et vous ne "
            + "retrouvez pas la forme après «&nbsp;que&nbsp;». Trois sorties possibles.",
    options: [
      { txt: "« Il faut revenir avec une facture récente. »", juste: true },
      { txt: "« Il faut que je reviens avec une facture récente. »",
        rat_t: "C'est la faute la plus visible du niveau 5.",
        rat: "Vous avez posé «&nbsp;que&nbsp;», donc vous avez annoncé un changement de forme — "
           + "et vous ne l'avez pas fait. La personne qui vous écoute attend "
           + "«&nbsp;revienne&nbsp;» et entend «&nbsp;reviens&nbsp;». "
           + "Si vous n'êtes pas sûr de la forme, <b>ne posez pas «&nbsp;que&nbsp;»</b>." },
      { txt: "« Il faut que revenir avec une facture récente. »",
        rat_t: "Les deux constructions sont mélangées.",
        rat: "«&nbsp;Que&nbsp;» annonce une personne, et l'infinitif dit qu'il n'y en a pas. "
           + "On ne peut pas avoir les deux. Choisissez&nbsp;: ou bien "
           + "«&nbsp;il faut revenir&nbsp;», ou bien «&nbsp;il faut que je revienne&nbsp;»." },
    ],
    pourquoi: "«&nbsp;Il faut revenir&nbsp;» ne dit pas <i>qui</i> revient — et dans une "
            + "conversation où il n'y a que vous deux, personne ne se demande de qui vous parlez. "
            + "<b>C'est une phrase entièrement correcte, pas une phrase de dépannage.</b> "
            + "Savoir l'employer vaut mieux que de rater l'autre.",
    attente: "Choisissez une réponse pour continuer.",
  },

  // ── 7. La première personne, à l'écoute. ─────────────────────────────────
  {
    id:   'je-sorte',
    type: 'verif',
    eye:  'Vérification',
    menu: 'Une question au téléphone',
    titre: "Leïla appelle la Ville. Écoutez sa question, puis dites ce qui est juste.",
    consigne: "Elle parle d'elle-même. Quelle est la bonne forme après «&nbsp;il faut que "
            + "je&nbsp;»&nbsp;?",
    sons: [
      { fichier: 't1/line_10_leila.mp3', qui: 'Leïla, au service à la clientèle',
        texte: "Le mardi. Est-ce que vous pouvez me dire à quelle heure il faut que je sorte "
             + "le bac&nbsp;?" },
    ],
    options: [
      { txt: "« Il faut que je sorte le bac. »", juste: true },
      { txt: "« Il faut que je sors le bac. »",
        rat_t: "C'est la forme du présent, et «&nbsp;que&nbsp;» vient de l'écarter.",
        rat: "«&nbsp;Je sors&nbsp;» est juste dans <i>je sors le bac le mardi</i>. Après "
           + "«&nbsp;il faut que&nbsp;», il faut la forme en <b>-e</b>&nbsp;: que je sort<b>e</b>. "
           + "C'est la même chose que <i>qu'elle date</i> tout à l'heure&nbsp;: un verbe ordinaire, "
           + "une petite fin en -e." },
      { txt: "« Il faut que je sortir le bac. »",
        rat_t: "L'infinitif ne se met jamais après «&nbsp;que&nbsp;».",
        rat: "Vous avez nommé quelqu'un — «&nbsp;je&nbsp;» — donc le verbe doit se conjuguer. "
           + "L'infinitif s'emploie quand il n'y a personne&nbsp;: «&nbsp;il faut sortir le bac "
           + "avant sept heures&nbsp;», sur l'affiche de la Ville." },
    ],
    pourquoi: "«&nbsp;Que je sort<b>e</b>&nbsp;». Remarquez ce que Leïla obtient en posant cette "
            + "question&nbsp;: une heure précise. C'est la phrase qui sert vraiment — "
            + "«&nbsp;à quelle heure il faut que je…&nbsp;» ouvre presque toutes les démarches.",
    attente: "Choisissez une réponse pour continuer.",
  },

  // ── 8. Le tri des six verbes, correct ou fautif. ─────────────────────────
  {
    id:   'tri-formes',
    type: 'tri',
    eye:  'À vous de trancher',
    menu: 'Six phrases écrites',
    titre: "Six phrases prises à six endroits. Lesquelles sont correctes ?",
    consigne: "Elles emploient les six verbes de l'écran&nbsp;5. Une seule chose à "
            + "regarder&nbsp;: la forme après «&nbsp;que&nbsp;».",
    colonnes: [
      { id: 'ok',   t: 'Correct',   b: 'Correct' },
      { id: 'faux', t: 'Une faute', b: 'Une faute' },
    ],
    items: [
      { txt: "Il faut que je vienne chercher mon fils avant dix-sept heures.",
        sous: "un message à la garderie", ok: 'ok',
        rat: "<i>Venir</i> donne «&nbsp;que je vienne&nbsp;». C'est la forme de l'écran&nbsp;1, "
           + "et c'est la plus fréquente des six.",
        pourquoi: "Venir → que je vienne. Juste." },
      { txt: "Il faut que vous êtes à jeun depuis minuit.",
        sous: "une consigne de laboratoire", ok: 'faux',
        rat: "<i>Être</i> est le verbe le plus fréquent de la langue, et c'est celui qu'on rate "
           + "le plus. Après «&nbsp;que&nbsp;»&nbsp;: «&nbsp;que vous <b>soyez</b>&nbsp;». "
           + "«&nbsp;Vous êtes&nbsp;» reste dans les phrases sans «&nbsp;que&nbsp;».",
        pourquoi: "Il faut « que vous soyez »." },
      { txt: "Il faut qu'elle fasse la demande elle-même.",
        sous: "au guichet d'un service", ok: 'ok',
        rat: "<i>Faire</i> donne «&nbsp;qu'elle fasse&nbsp;». Rien à voir avec "
           + "«&nbsp;elle fait&nbsp;»&nbsp;: c'est justement pour ça qu'il est dans les six.",
        pourquoi: "Faire → qu'elle fasse. Juste." },
      { txt: "Il faut que j'ai ma carte d'assurance maladie avec moi.",
        sous: "une note pour soi-même", ok: 'faux',
        rat: "À l'oreille, «&nbsp;j'ai&nbsp;» et «&nbsp;j'aie&nbsp;» se ressemblent beaucoup — "
           + "et à l'écrit la faute se voit tout de suite. Après «&nbsp;que&nbsp;»&nbsp;: "
           + "«&nbsp;que j'<b>aie</b>&nbsp;».",
        pourquoi: "Il faut « que j'aie »." },
      { txt: "Il faut que vous alliez au comptoir trois.",
        sous: "à l'accueil d'un bureau", ok: 'ok',
        rat: "<i>Aller</i> donne «&nbsp;que vous alliez&nbsp;». On l'entend tous les jours dans "
           + "un couloir&nbsp;; c'est le sixième des six.",
        pourquoi: "Aller → que vous alliez. Juste." },
      { txt: "Il faut que je peux revenir demain matin.",
        sous: "au téléphone avec un employeur", ok: 'faux',
        rat: "<i>Pouvoir</i> donne «&nbsp;que je <b>puisse</b>&nbsp;». Celui-là s'entend rarement "
           + "chez les élèves — non pas qu'il soit rare, mais parce qu'on l'évite. "
           + "Il vaut la peine d'être appris&nbsp;: il sert à négocier.",
        pourquoi: "Il faut « que je puisse »." },
    ],
    attente: "Tranchez les six phrases pour continuer.",
  },

  // ── 9. Écrire, pas reconnaître. ──────────────────────────────────────────
  {
    id:   'un-message',
    type: 'verif',
    eye:  'Vérification',
    menu: 'Un message à écrire',
    titre: "Un message à l'école. Une seule version tient d'un bout à l'autre.",
    consigne: "Vous prévenez le secrétariat que votre fille sera absente vendredi et que vous "
            + "passerez chercher ses devoirs.",
    options: [
      { txt: "« Bonjour. Ma fille sera absente vendredi. Il faut qu'elle aille chez le dentiste "
           + "à dix heures. Est-ce qu'il faut passer au secrétariat pour ses devoirs ? »",
        juste: true },
      { txt: "« Bonjour. Ma fille sera absente vendredi. Il faut qu'elle va chez le dentiste "
           + "à dix heures. Est-ce qu'il faut passer au secrétariat pour ses devoirs ? »",
        rat_t: "La deuxième phrase seulement.",
        rat: "La fin est bonne — «&nbsp;il faut passer&nbsp;», sans «&nbsp;que&nbsp;», parce que "
           + "vous ne nommez personne. Mais «&nbsp;qu'elle <b>va</b>&nbsp;» ne peut pas rester&nbsp;: "
           + "<i>aller</i> est l'un des six, et donne «&nbsp;qu'elle <b>aille</b>&nbsp;»." },
      { txt: "« Bonjour. Ma fille sera absente vendredi. Il faut qu'elle aille chez le dentiste "
           + "à dix heures. Est-ce qu'il faut que passer au secrétariat pour ses devoirs ? »",
        rat_t: "Le début est juste. C'est la question qui casse.",
        rat: "«&nbsp;Qu'elle aille&nbsp;» est parfait. Mais dans la question, vous n'avez nommé "
           + "personne&nbsp;: alors il n'y a pas de «&nbsp;que&nbsp;» à mettre. "
           + "«&nbsp;Est-ce qu'il faut passer au secrétariat&nbsp;?&nbsp;» — l'infinitif seul." },
    ],
    pourquoi: "Une phrase avec «&nbsp;que&nbsp;» parce qu'elle nomme la fille, une phrase sans "
            + "«&nbsp;que&nbsp;» parce qu'elle ne nomme personne. <b>C'est tout le point express "
            + "dans un message de trois lignes.</b>",
    attente: "Choisissez une réponse pour continuer.",
  },

  // ── 10. La fermeture : le cas de l'écran 1, en plus difficile. ───────────
  {
    id:   'fermeture',
    type: 'verif',
    eye:  'La dernière',
    menu: 'Pour finir',
    titre: "On revient au bail du début. Vous répondez au préposé.",
    consigne: "Il vous a dit&nbsp;: «&nbsp;Il faut que vous veniez avec votre bail.&nbsp;» "
            + "Vous voulez savoir si votre fils peut venir à votre place. Que dites-vous&nbsp;?",
    options: [
      { txt: "« Est-ce qu'il faut que je vienne moi-même, ou est-ce que mon fils peut venir ? »",
        juste: true },
      { txt: "« Est-ce qu'il faut que je viens moi-même, ou est-ce que mon fils peut venir ? »",
        rat_t: "C'est la faute de l'écran 1, retournée.",
        rat: "Vous avez posé «&nbsp;que&nbsp;» et vous avez laissé la forme du présent. "
           + "<i>Venir</i> est le premier des six&nbsp;: «&nbsp;que je <b>vienne</b>&nbsp;». "
           + "Notez que la fin de votre phrase, elle, est impeccable&nbsp;: "
           + "«&nbsp;mon fils peut venir&nbsp;» n'a pas de «&nbsp;que&nbsp;», donc rien à changer." },
      { txt: "« Est-ce qu'il faut venir moi-même, ou est-ce que mon fils peut venir ? »",
        rat_t: "La forme est correcte. C'est le sens qui se perd.",
        rat: "Aucune faute&nbsp;: «&nbsp;il faut venir&nbsp;» est une phrase juste, et c'est la "
           + "sortie de secours de l'écran&nbsp;6. Mais ici elle vous dessert&nbsp;: votre question "
           + "porte justement sur <b>qui</b> doit se présenter. Quand la personne est le sujet de "
           + "la question, il faut la nommer — donc «&nbsp;que&nbsp;»." },
    ],
    pourquoi: "«&nbsp;Il faut que je <b>vienne</b> moi-même&nbsp;». Vous avez fait les deux "
            + "moitiés&nbsp;: vous nommez la personne parce que c'est elle qui est en jeu, "
            + "et vous mettez la forme des six verbes. "
            + "<b>Le reste du temps, l'infinitif suffit — et il est correct.</b>",
    attente: "Choisissez une réponse pour finir.",
  },

];
