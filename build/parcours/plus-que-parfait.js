// ═══════════════════════════════════════════════════════════════════════════
// Point express — Le plus-que-parfait : ce qui s'était passé avant
//
// Savoir n6-s26. Dix minutes, dix écrans.
//
// ── L'écart avec les mini-leçons, qui sont sept ───────────────────────────
// Sept modules portent déjà une mini-leçon sur ce temps (n5-urgence,
// n6-classe, n6-actualite, n6-emploi, n6-logement, n6-oeuvres, n6-relations)
// et elles procèdent toutes de la même façon : la formation d'abord
// (« l'auxiliaire à l'imparfait »), puis la liste des mots qui l'annoncent,
// puis les pièges d'auxiliaire. Trois d'entre elles emploient la même image —
// « reculer d'un cran », « l'étage du dessous », « le passé du passé ». Un
// élève envoyé ici l'a lue au moins une fois, et il continue de raconter tout
// au passé composé.
//
// Ce point express prend le problème par l'autre bout :
//
//   1. IL PART DE CELUI QUI ÉCOUTE, pas de celui qui parle. La panne n'est
//      pas une forme ratée, c'est un récit devenu illisible : l'interlocuteur
//      ne sait plus quoi est arrivé en premier. Chaque écran a une
//      conséquence, jamais une forme à produire pour elle-même.
//   2. AUCUNE MÉTAPHORE D'ÉTAGE NI DE CRAN. « Plus passé » est justement ce
//      qui trompe, et le point le dit explicitement (écran 4) : le
//      plus-que-parfait n'est pas plus loin dans le passé, il est AVANT UNE
//      AUTRE CHOSE PASSÉE. Sans cette autre chose, il n'existe pas.
//   3. LE TEST N'EST PAS UNE LISTE DE MOTS, C'EST UNE QUESTION : « où est
//      l'autre passé ? » Elle se pose sur une phrase qu'on n'a jamais vue,
//      et elle marche là où « déjà » et « la veille » sont absents.
//   4. INDUCTIF, ET SUR L'ORDRE DES MOTS. Le tri de l'écran 3 ne demande pas
//      de reconnaître un temps : il demande de dire ce qui est arrivé en
//      premier — et fait découvrir que l'ordre des mots n'est pas l'ordre des
//      faits. Aucune mini-leçon ne pose la question ainsi.
//   5. LA FORMATION EST DITE EN DERNIER (écran 8), en trois lignes, comme
//      « ce qu'il n'y a pas à apprendre ». Les mini-leçons ouvrent dessus.
//   6. « QUAND » EST TRAITÉ À PART (écran 7), avec les trois scènes qu'il
//      peut décrire selon le temps qui suit. Aucune mini-leçon ne le liste :
//      elles donnent déjà, la veille, avant, parce que — jamais « quand »,
//      qui est pourtant l'endroit exact où l'élève de niveau 6 trébuche.
//
// Extraits : `module-n6-sante` — le récit de Leyla, qui attend depuis sept
// mois. C'est le module du corpus où les deux passés s'enchaînent le plus
// naturellement, parce qu'on y raconte sans arrêt ce qui a précédé la
// consultation. Aucun média neuf.
// ═══════════════════════════════════════════════════════════════════════════

const PARCOURS = {
  slug:     'plus-que-parfait',
  module:   'module-n6-sante',
  titre:    "Ce qui s'était passé avant",
  surtitre: "Point express · 10 minutes",
  niveau:   6,
  savoir:   'n6-s26',
};

const ECRANS = [

  // ── 1. Une décision, avant toute règle. ─────────────────────────────────
  {
    id:   'depart',
    type: 'verif',
    eye:  'Une question, pour commencer',
    menu: 'Deux fois la même porte',
    titre: "Vous racontez votre journée. Dans quelle phrase avez-vous fait le voyage pour rien ?",
    consigne: "Répondez avec ce que vous savez déjà — on expliquera après, c'est fait exprès.",
    options: [
      { txt: "« Quand je suis arrivé, ils avaient déjà fermé. »", juste: true },
      { txt: "« Quand je suis arrivé, ils ont fermé. »",
        rat_t: "Ici, vous êtes entré.",
        rat: "Cette phrase raconte deux choses qui se suivent&nbsp;: vous arrivez, et le bureau "
           + "ferme après. Vous étiez là au bon moment&nbsp;— peut-être de justesse, mais vous "
           + "étiez là. Ce n'est pas le voyage pour rien." },
      { txt: "Les deux racontent la même chose.",
        rat_t: "Les deux mêmes faits, dans deux ordres différents.",
        rat: "Fermer et arriver, dans les deux cas. Mais dans l'une la porte est fermée avant "
           + "vous, dans l'autre après. Un seul mot les sépare — et c'est ce mot qui décide si "
           + "vous êtes rentré chez vous les mains vides." },
    ],
    pourquoi: "«&nbsp;Ils <b>avaient</b> fermé&nbsp;»&nbsp;: c'était fait avant que vous arriviez. "
            + "Gardez les deux phrases en tête&nbsp;; on y revient à la fin.",
    attente: "Choisissez une réponse pour continuer.",
  },

  // ── 2. On écoute, sans règle : une observation sur l'ordre. ─────────────
  {
    id:   'sept-mois',
    type: 'notion',
    eye:  'Écoutez un dossier se raconter',
    menu: "L'ordre des faits",
    titre: "Deux répliques au comptoir d'une clinique. Trois faits, et pas dans l'ordre.",
    paras: [
      "Leyla attend depuis sept mois un rendez-vous en médecine interne. La réceptionniste "
      + "reconstitue son dossier. Écoutez les deux répliques et essayez seulement de mettre "
      + "les faits dans l'ordre du calendrier&nbsp;: la demande du médecin, le conseil d'attendre, "
      + "l'arrivée de Leyla ce matin.",

      "Rien à retenir pour l'instant. Remarquez juste que ni Mariette ni Leyla ne disent "
      + "«&nbsp;a envoyé&nbsp;» ou «&nbsp;m'a dit&nbsp;». Elles emploient une autre forme, "
      + "et c'est elle qui range les faits.",
    ],
    sons: [
      { fichier: 'prep/line_06_mariette.mp3', qui: 'Mariette, à la réception',
        texte: "Sept mois, ce n'est pas rare. Votre médecin de famille avait envoyé une demande "
             + "de consultation, c'est ça&nbsp;?" },
      { fichier: 'prep/line_07_leyla.mp3', qui: 'Leyla répond',
        texte: "Oui. En avril. Elle m'avait dit d'attendre l'appel et de ne pas rappeler avant "
             + "l'automne." },
    ],
    retenir: "Les deux répliques se disent au comptoir, ce matin. Les deux faits qu'elles "
           + "racontent sont d'avril. <b>C'est la forme du verbe qui le dit</b>, pas la date.",
    attente: "Écoutez les deux extraits, puis continuez.",
  },

  // ── 3. Le cœur : trancher l'ordre, sans qu'aucun temps n'ait été nommé. ─
  {
    id:   'tri-ordre',
    type: 'tri',
    eye:  'À vous de trancher',
    menu: 'Six phrases',
    titre: "Six phrases, deux faits passés dans chacune. Lequel est arrivé en premier ?",
    consigne: "Ne cherchez pas de règle&nbsp;: dites seulement si le fait le plus ancien est "
            + "raconté <b>au début</b> ou <b>à la fin</b> de la phrase.",
    colonnes: [
      { id: 'debut', t: 'Le plus ancien est au début', b: 'Au début' },
      { id: 'fin',   t: 'Le plus ancien est à la fin',  b: 'À la fin' },
    ],
    items: [
      { txt: "Quand je suis arrivé, ils avaient déjà fermé.", ok: 'fin',
        rat: "La fermeture est racontée en second et elle s'est produite en premier&nbsp;: "
           + "la porte était close avant que vous tourniez le coin.",
        pourquoi: "La fermeture, racontée en dernier, est arrivée d'abord." },
      { txt: "Elle avait pris rendez-vous en avril, et elle a vu la médecin en novembre.", ok: 'debut',
        rat: "Ici l'ordre des mots suit le calendrier&nbsp;: avril, puis novembre. Ça arrive "
           + "aussi — c'est justement pour ça qu'on ne peut pas se fier à la place des mots.",
        pourquoi: "Avril d'abord, novembre ensuite. L'ordre suit." },
      { txt: "J'ai raté l'autobus : j'avais oublié de mettre mon réveil.", ok: 'fin',
        rat: "L'oubli est la cause, et une cause vient toujours avant. On la raconte en second "
           + "parce qu'on explique après coup.",
        pourquoi: "L'oubli du réveil précède l'autobus raté." },
      { txt: "Il avait perdu sa carte, alors il est allé au comptoir.", ok: 'debut',
        rat: "La perte, puis le déplacement. Les mots et les faits vont dans le même sens.",
        pourquoi: "La perte d'abord, le comptoir ensuite." },
      { txt: "Quand le camion est passé, j'avais déjà sorti le bac.", ok: 'fin',
        rat: "Le bac était dehors avant le camion — c'est pour ça qu'il a été ramassé. "
           + "Le fait le plus ancien est raconté en dernier.",
        pourquoi: "Le bac était sorti avant le passage du camion." },
      { txt: "Nous avions rempli le formulaire, puis nous nous sommes présentés au guichet.", ok: 'debut',
        rat: "Le formulaire, puis le guichet. Rien ne se retourne ici.",
        pourquoi: "Le formulaire d'abord, le guichet ensuite." },
    ],
    attente: "Tranchez les six phrases pour continuer.",
  },

  // ── 4. La règle, écrite comme un constat de ce qu'il vient de faire. ────
  {
    id:   'lautre-passe',
    type: 'notion',
    eye:  'Ce que vous venez de faire',
    menu: "Cherchez l'autre passé",
    titre: "Vous n'avez pas suivi l'ordre des mots. Vous avez suivi « avait ».",
    paras: [
      "Trois fois sur six, le fait le plus ancien était raconté en dernier. Vous ne vous êtes "
      + "pas trompé pour autant, parce que vous avez repéré autre chose&nbsp;: le petit mot "
      + "<b>avait</b> ou <b>était</b> devant le verbe. Il ne dit pas «&nbsp;c'est vieux&nbsp;». "
      + "Il dit&nbsp;: <b>c'était déjà fait quand l'autre chose est arrivée.</b>",

      "Cette forme s'appelle le <b>plus-que-parfait</b>, et son nom trompe. «&nbsp;Plus&nbsp;» "
      + "fait croire à un passé plus lointain, comme s'il y avait des degrés. Il n'y en a pas. "
      + "Une chose d'il y a dix ans se raconte très bien au passé composé&nbsp;: "
      + "<i>je suis arrivée au Québec en 2016.</i> Ce n'est pas la distance qui décide.",

      "<b>Le test, à poser sur n'importe quelle phrase&nbsp;: où est l'autre passé&nbsp;?</b> "
      + "Le plus-que-parfait ne vit jamais seul. Il y a toujours, dans la phrase ou dans celle "
      + "d'à côté, un deuxième fait passé — et c'est par rapport à celui-là, et à rien d'autre, "
      + "qu'il se situe. Si vous ne trouvez pas ce deuxième fait, c'est que vous n'aviez pas "
      + "besoin du plus-que-parfait.",
    ],
    retenir: "Pas «&nbsp;plus passé&nbsp;»&nbsp;: <b>avant un autre passé</b>. "
           + "Cherchez toujours l'autre fait — sans lui, cette forme ne veut rien dire.",
    attente: "Lisez, puis continuez.",
  },

  // ── 5. Le test appliqué à un vrai récit entendu. ─────────────────────────
  {
    id:   'le-printemps',
    type: 'verif',
    eye:  'Vérification',
    menu: 'Un récit dans une salle d’attente',
    titre: "Leyla raconte sa dernière année à un inconnu. Qu'est-ce qui est arrivé en premier ?",
    consigne: "Écoutez, puis appliquez le test&nbsp;: où est l'autre passé, et lequel des deux "
            + "porte «&nbsp;avait&nbsp;»&nbsp;?",
    sons: [
      { fichier: 't1/line_14_leyla.mp3', qui: 'Leyla, dans la salle d’attente',
        texte: "C'est exactement ça. Mon médecin m'avait fait passer des prises de sang au "
             + "printemps. Il y avait quelque chose, une anémie légère, elle a dit. Elle a envoyé "
             + "une demande de consultation et j'ai attendu." },
    ],
    options: [
      { txt: "Les prises de sang.", juste: true },
      { txt: "La demande de consultation.",
        rat_t: "Elle est racontée en second, et elle est arrivée en second.",
        rat: "«&nbsp;Elle <b>a envoyé</b> une demande&nbsp;»&nbsp;: passé composé, sans "
           + "«&nbsp;avait&nbsp;». C'est un fait de la suite du récit. Ce sont les prises de "
           + "sang qui portent la marque de l'antériorité — et c'est logique&nbsp;: on ne demande "
           + "une consultation qu'<i>après</i> avoir vu un résultat." },
      { txt: "On ne peut pas savoir, elle ne donne pas les dates.",
        rat_t: "Elle en donne une seule, et elle n'en a pas besoin de plus.",
        rat: "«&nbsp;Au printemps&nbsp;» est la seule date de tout l'extrait, et pourtant l'ordre "
           + "est parfaitement clair. C'est exactement ce que ce temps sert à faire&nbsp;: "
           + "<b>ranger les faits sans avoir à dater chacun d'eux.</b>" },
    ],
    pourquoi: "«&nbsp;M'<b>avait</b> fait passer&nbsp;» d'un côté, «&nbsp;a envoyé&nbsp;» et "
            + "«&nbsp;j'ai attendu&nbsp;» de l'autre. Un seul verbe recule&nbsp;; les autres "
            + "avancent. <b>C'est ça, un récit qui se tient</b>&nbsp;: la médecin qui l'écoute "
            + "sait dans quel ordre lire son dossier.",
    attente: "Choisissez une réponse pour continuer.",
  },

  // ── 6. « déjà », et ce qu'il ajoute vraiment. ────────────────────────────
  {
    id:   'deja',
    type: 'notion',
    eye:  'Le mot qui trahit',
    menu: '« Déjà »',
    titre: "« Déjà » ne dit pas seulement l'ordre. Il dit qu'il était trop tard.",
    paras: [
      "Comparez ces deux messages, écrits le même soir à deux personnes différentes. "
      + "«&nbsp;<i>Quand j'ai rappelé, ils avaient donné la place à quelqu'un d'autre.</i>&nbsp;» "
      + "«&nbsp;<i>Quand j'ai rappelé, ils avaient <b>déjà</b> donné la place à quelqu'un "
      + "d'autre.</i>&nbsp;» Les deux disent le même ordre. Le second ajoute un reproche, "
      + "ou un regret&nbsp;: c'était fait, et il n'y avait plus rien à négocier.",

      "C'est pour ça que «&nbsp;déjà&nbsp;» revient si souvent dans les récits d'ennuis — "
      + "un guichet fermé, un formulaire perdu, une place partie. Et c'est pour ça qu'il vous "
      + "sert de signal&nbsp;: <b>dès que vous écrivez «&nbsp;déjà&nbsp;» dans un récit au passé, "
      + "le verbe qui le suit prend «&nbsp;avait&nbsp;» ou «&nbsp;était&nbsp;».</b> "
      + "Il se glisse entre les deux&nbsp;: <i>ils avaient déjà donné</i>, "
      + "<i>elle était déjà partie</i>.",

      "Le contraire existe aussi, et il est utile&nbsp;: "
      + "«&nbsp;<i>Quand je suis passée à la pharmacie, mon ordonnance était déjà prête.</i>&nbsp;» "
      + "Ici, ce qui était fait d'avance vous arrange. «&nbsp;Déjà&nbsp;» ne se plaint pas "
      + "toujours&nbsp;: il constate que la chose n'était plus à faire.",
    ],
    retenir: "«&nbsp;Déjà&nbsp;» + un récit au passé → «&nbsp;avait&nbsp;» ou "
           + "«&nbsp;était&nbsp;», et le mot se met entre les deux.",
    attente: "Lisez, puis continuez.",
  },

  // ── 7. « quand » : trois scènes, selon le temps qui suit. ───────────────
  {
    id:   'quand',
    type: 'verif',
    eye:  'Le cas qui trompe',
    menu: '« Quand » et trois scènes',
    titre: "« Quand je suis arrivé… » : trois suites possibles, trois scènes différentes.",
    consigne: "Vous poussez la porte du bureau à seize heures moins deux. "
            + "Dans quelle phrase le bureau était-il fermé <b>avant</b> vous&nbsp;?",
    options: [
      { txt: "« Quand je suis arrivé, ils avaient fermé. »", juste: true },
      { txt: "« Quand je suis arrivé, ils fermaient. »",
        rat_t: "Là, c'est en train de se faire — devant vous.",
        rat: "L'imparfait montre une action en cours&nbsp;: on baisse le rideau pendant que vous "
           + "montez les marches. Rien n'est terminé, et vous avez encore une chance de vous "
           + "faire servir. C'est une scène, pas un mur." },
      { txt: "« Quand je suis arrivé, ils ont fermé. »",
        rat_t: "Là, ils ont fermé après votre arrivée.",
        rat: "Deux passés composés côte à côte se lisent l'un après l'autre&nbsp;: vous arrivez, "
           + "puis ils ferment. La phrase est un peu brutale mais elle est claire — et elle dit "
           + "l'inverse de ce qu'on cherchait." },
    ],
    pourquoi: "«&nbsp;Quand&nbsp;» tout seul ne range rien&nbsp;: il pose deux faits l'un à côté "
            + "de l'autre et laisse le temps du verbe décider. "
            + "<b>Avaient fermé</b>&nbsp;: c'était fini avant. <b>Fermaient</b>&nbsp;: c'était en "
            + "train. <b>Ont fermé</b>&nbsp;: c'est venu après. "
            + "Trois formes, trois soirées différentes.",
    attente: "Choisissez une réponse pour continuer.",
  },

  // ── 8. La formation, gardée pour la fin : il n'y a rien à apprendre. ────
  {
    id:   'rien-a-apprendre',
    type: 'notion',
    eye:  'La partie facile',
    menu: 'Comment on l’écrit',
    titre: "On a gardé la fabrication pour la fin, parce qu'elle ne demande rien.",
    paras: [
      "Vous savez déjà écrire «&nbsp;elle a demandé&nbsp;», «&nbsp;je suis partie&nbsp;». "
      + "Alors vous savez déjà tout&nbsp;: <b>on garde la phrase telle quelle et on met le petit "
      + "verbe à l'imparfait.</b> Elle a demandé → elle <b>avait</b> demandé. Je suis partie → "
      + "j'<b>étais</b> partie. Aucune forme nouvelle à mémoriser.",

      "Une seule chose ne bouge pas&nbsp;: le verbe garde le même petit verbe qu'au passé "
      + "composé. Si vous dites «&nbsp;je suis partie&nbsp;», vous direz "
      + "«&nbsp;j'étais partie&nbsp;» — jamais «&nbsp;j'avais partie&nbsp;». Et l'accord suit la "
      + "même règle qu'avant&nbsp;: <i>elle était arrivée</i>, <i>les résultats étaient "
      + "revenus</i>.",

      "Écoutez la médecin de Leyla. «&nbsp;Votre médecin <b>avait</b> demandé des prélèvements "
      + "en mars&nbsp;»&nbsp;— et juste après, «&nbsp;est-ce qu'on vous <b>a</b> expliqué&nbsp;?&nbsp;» "
      + "Le même verbe conjugué, deux petits verbes différents, et deux places différentes dans "
      + "le temps. C'est toute la mécanique.",
    ],
    sons: [
      { fichier: 't2/line_11_sylvine.mp3', qui: 'La docteure Charest, interniste',
        texte: "Vous arrêtez de parler dans l'escalier. Merci, c'est précis. Votre médecin avait "
             + "demandé des prélèvements en mars — je les ai, il y avait une anémie légère. "
             + "Est-ce qu'on vous a expliqué ce que ça veut dire&nbsp;?" },
    ],
    retenir: "La même phrase qu'au passé composé, avec <b>avait</b> ou <b>était</b> à la place "
           + "de <b>a</b> ou <b>est</b>. Rien d'autre ne change.",
    attente: "Écoutez, puis continuez.",
  },

  // ── 9. Écrire un récit, pas reconnaître une forme. ──────────────────────
  {
    id:   'raconter',
    type: 'verif',
    eye:  'Vérification',
    menu: 'Un récit à écrire',
    titre: "Vous racontez votre matinée par écrit. Une seule version se lit sans hésiter.",
    consigne: "Les faits&nbsp;: vous perdez votre carte lundi, vous en demandez une nouvelle "
            + "mardi, et mercredi au comptoir on vous dit que la nouvelle est arrivée. "
            + "Trois façons de l'écrire.",
    options: [
      { txt: "« Mercredi, je suis allée au comptoir. J'avais perdu ma carte lundi et j'en avais "
           + "demandé une autre le lendemain. Elle était déjà arrivée. »",
        juste: true },
      { txt: "« Mercredi, je suis allée au comptoir. J'ai perdu ma carte lundi et j'ai demandé "
           + "une autre le lendemain. Elle est déjà arrivée. »",
        rat_t: "Tout au passé composé&nbsp;: les trois jours s'aplatissent.",
        rat: "Aucune faute de forme, et pourtant le récit se défait. Trois faits alignés sans "
           + "relief&nbsp;: celui qui lit doit refaire le calendrier tout seul, à partir de "
           + "«&nbsp;lundi&nbsp;» et de «&nbsp;mercredi&nbsp;». <b>C'est exactement le récit "
           + "d'un élève de niveau 6</b>&nbsp;: correct, et fatigant à suivre." },
      { txt: "« Mercredi, j'étais allée au comptoir. J'avais perdu ma carte lundi et j'avais "
           + "demandé une autre le lendemain. Elle avait déjà arrivé. »",
        rat_t: "Deux problèmes, dont un de sens.",
        rat: "D'abord le sens&nbsp;: si <i>tout</i> recule, plus rien ne sert de repère — "
           + "il faut un fait principal au passé composé, et c'est la visite de mercredi. "
           + "Ensuite la forme&nbsp;: <i>arriver</i> se dit «&nbsp;elle <b>est</b> arrivée&nbsp;», "
           + "donc «&nbsp;elle <b>était</b> arrivée&nbsp;», jamais «&nbsp;avait&nbsp;»." },
    ],
    pourquoi: "Un seul fait au premier plan — la visite de mercredi — et deux faits qui reculent "
            + "derrière lui. <b>Le plus-que-parfait ne s'emploie jamais partout&nbsp;: il "
            + "s'emploie par rapport à quelque chose.</b> Sans ce point d'appui, il n'y a plus "
            + "de récit du tout.",
    attente: "Choisissez une réponse pour continuer.",
  },

  // ── 10. La fermeture : la porte de l'écran 1. ───────────────────────────
  {
    id:   'fermeture',
    type: 'verif',
    eye:  'La dernière',
    menu: 'Pour finir',
    titre: "Retour à la porte du début. Vous écrivez à votre enseignante pour expliquer.",
    consigne: "Vous êtes passé au secrétariat mardi à seize heures moins deux et le comptoir "
            + "était fermé. Quelle phrase le dit sans qu'elle ait à vous relire deux fois&nbsp;?",
    options: [
      { txt: "« Je suis passé mardi vers seize heures, mais le comptoir avait déjà fermé. »",
        juste: true },
      { txt: "« Je suis passé mardi vers seize heures, mais le comptoir a déjà fermé. »",
        rat_t: "«&nbsp;Déjà&nbsp;» annonçait le recul, et le verbe ne l'a pas fait.",
        rat: "C'est la faute la plus fréquente une fois qu'on a compris le sens&nbsp;: on place "
           + "bien le «&nbsp;déjà&nbsp;», et on laisse le verbe au passé composé. "
           + "Rappelez-vous l'écran&nbsp;6&nbsp;: <b>«&nbsp;déjà&nbsp;» dans un récit au passé "
           + "appelle «&nbsp;avait&nbsp;»</b>. Ici&nbsp;: «&nbsp;avait déjà fermé&nbsp;»." },
      { txt: "« J'étais passé mardi vers seize heures, mais le comptoir avait déjà fermé. »",
        rat_t: "Les deux faits ont reculé, et il n'en reste aucun au premier plan.",
        rat: "La deuxième moitié est juste. Mais votre passage est le fait principal du "
           + "message&nbsp;: c'est lui qui doit rester au passé composé, sinon on se demande "
           + "avant quoi il a eu lieu. <b>Un seul des deux recule</b>, et c'est celui qui "
           + "explique l'autre." },
    ],
    pourquoi: "«&nbsp;Je suis passé… le comptoir <b>avait déjà fermé</b>.&nbsp;» Un fait au "
            + "premier plan, un fait qui recule derrière lui, et votre enseignante sait "
            + "immédiatement que vous n'y êtes pour rien. "
            + "<b>C'était toute la question de l'écran&nbsp;1.</b>",
    attente: "Choisissez une réponse pour finir.",
  },

];
