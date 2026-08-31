// ═══════════════════════════════════════════════════════════════════════════
// Point express — Dire où l'on va : à, au, en, chez
//
// Savoir n5-s40 (« Prépositions et GPrép »). Une ORDONNANCE : l'enseignant
// l'envoie à un élève qui écrit « je vais au médecin », « je vais à Québec »
// pour la province, « je vais en Montréal ». Dix minutes, dix écrans.
//
// ── Ce dont il s'écarte, et comment ────────────────────────────────────────
// Deux mini-leçons couvrent le terrain. `module-n2-autobus` (bloc prLieu),
// « Où on va : à la, au, à l' », prend les trois formes une à une, chacune
// avec sa règle de genre, puis un labo de quinze phrases : c'est complet et
// c'est du niveau 2. `module-n5-services` (bloc t2prep), « Les prépositions
// des démarches », traite les prépositions qui suivent un verbe (s'adresser
// à, se renseigner sur) et ouvre en disant qu'« aucune logique » ne les
// explique. Un élève envoyé ici a lu l'une ou l'autre. Les cinq écarts :
//
//   1. UN CLASSEMENT, PAS UNE LISTE, ET SURTOUT PAS « ÇA NE S'EXPLIQUE PAS ».
//      C'est la décision centrale de ce point. Pour dire où l'on va, il n'y a
//      pas dix cas à mémoriser : il y en a TROIS, et on les distingue par ce
//      qu'est le lieu — une personne, un endroit ordinaire, un territoire.
//      Le tri de l'écran 2 ne demande aucune grammaire : il demande de
//      reconnaître ces trois natures, ce qu'un adulte fait sans effort.
//   2. INDUCTIF, ET AUCUNE PRÉPOSITION AVANT L'ÉCRAN 3. L'élève range huit
//      lieux avant qu'un seul « à », « au » ou « en » ait été écrit. La règle
//      est le constat de son tri : « vos trois piles sont trois prépositions ».
//   3. LE TEST TIENT DANS UNE QUESTION QU'ON SE POSE SUR LE LIEU SEUL :
//      comment est-ce que je le nomme quand il est tout seul ? « la
//      pharmacie » → à la ; « le Québec » → au ; « l'Ontario » → en (voyelle) ;
//      « Montréal », rien devant → à. Le mot qu'on met devant le lieu décide
//      du mot qu'on met devant la phrase. Un test se réemploie sur un pays
//      jamais vu ; une liste de pays, non.
//   4. LE CAS PAR DÉFAUT EST DIT EN DERNIER (écran 8). « à la, au, à l' » est
//      le cas le plus fréquent, donc celui qu'on écrit sans y penser : le
//      nommer d'entrée ferait croire à trois règles concurrentes.
//   5. EXEMPLES PRIS À PLUSIEURS SITUATIONS, ET L'ERREUR EST L'ENSEIGNEMENT.
//      Un texto, une note à l'école, un formulaire, un message à un
//      employeur. Deux fautes sont travaillées pour elles-mêmes : « je vais
//      au médecin » (écran 4) et « à Québec » / « au Québec » (écran 7), qui
//      est la confusion locale par excellence et qu'aucune mini-leçon ne
//      traite. Aucun personnage ni scénario d'un module.
//
// Aucun média : ces formes s'entendent, et l'élève les entend correctement
// tous les jours. Ce qui manque n'est pas l'oreille, c'est la décision.
// ═══════════════════════════════════════════════════════════════════════════

const PARCOURS = {
  slug:     'a-au-en-chez',
  titre:    "Dire où l'on va : à, au, en, chez",
  surtitre: "Point express · 10 minutes",
  niveau:   5,
  savoir:   'n5-s40',
};

const ECRANS = [

  // ── 1. Une décision, sans aucune règle donnée. ───────────────────────────
  {
    id:   'depart',
    type: 'verif',
    eye:  'Une question, pour commencer',
    menu: 'Trois versions',
    titre: "Une seule de ces phrases s'écrit. Laquelle ?",
    consigne: "Répondez avec ce que vous savez déjà — ou au feeling. On expliquera après&nbsp;: "
            + "c'est fait exprès.",
    options: [
      { txt: "«&nbsp;Je ne serai pas au travail jeudi&nbsp;: je vais chez le médecin.&nbsp;»",
        juste: true },
      { txt: "«&nbsp;Je ne serai pas au travail jeudi&nbsp;: je vais au médecin.&nbsp;»",
        rat_t: "C'est la version la plus fréquente, et elle ne s'écrit pas.",
        rat: "Elle est fréquente pour une bonne raison&nbsp;: on dit «&nbsp;je vais "
           + "<b>au</b> travail&nbsp;», «&nbsp;<b>au</b> dépanneur&nbsp;», "
           + "«&nbsp;<b>au</b> bureau&nbsp;» — alors on continue. Mais un médecin n'est pas "
           + "un endroit&nbsp;: c'est quelqu'un. Et pour aller vers quelqu'un, le français a "
           + "un mot à lui." },
      { txt: "«&nbsp;Je ne serai pas au travail jeudi&nbsp;: je vais à le médecin.&nbsp;»",
        rat_t: "« À le » n'existe pas en français.",
        rat: "Ces deux mots ne se rencontrent jamais&nbsp;: ils se collent toujours et "
           + "donnent «&nbsp;au&nbsp;». Vous venez donc d'écrire la phrase précédente, en "
           + "plus long — et elle ne convient pas non plus." },
    ],
    pourquoi: "«&nbsp;<b>Chez</b> le médecin&nbsp;». Retenez la phrase telle quelle pour "
            + "l'instant. On va voir qu'il n'y a que <b>trois</b> cas à distinguer, et qu'ils "
            + "se reconnaissent sans grammaire.",
    attente: "Choisissez une réponse pour continuer.",
  },

  // ── 2. On trie AVANT de savoir. Aucune préposition dans le tri. ──────────
  {
    id:   'trois-natures',
    type: 'tri',
    eye:  'À vous de trancher',
    menu: 'Huit destinations',
    titre: "Huit destinations. De quelle sorte est chacune ?",
    consigne: "Aucune grammaire ici, et aucune préposition&nbsp;: dites seulement <b>ce que "
            + "c'est</b>. Vous verrez à l'écran suivant pourquoi on vous le demande.",
    colonnes: [
      { id: 'pers', t: 'Quelqu’un',                b: 'Quelqu’un' },
      { id: 'lieu', t: 'Un endroit, un commerce',  b: 'Un endroit' },
      { id: 'terr', t: 'Une ville, une province, un pays', b: 'Un territoire' },
    ],
    items: [
      { txt: "le dentiste", ok: 'pers',
        rat: "On dit «&nbsp;le dentiste&nbsp;» comme on dit «&nbsp;la pharmacie&nbsp;», avec "
           + "un article&nbsp;: c'est ce qui trompe. Mais un dentiste est une personne, pas "
           + "un bâtiment — et c'est la personne qu'on va voir.",
        pourquoi: "Une personne, malgré l'article." },
      { txt: "la pharmacie", ok: 'lieu',
        rat: "Une pharmacie est un commerce&nbsp;: un endroit avec une porte et des heures "
           + "d'ouverture. On peut y entrer sans y voir personne en particulier.",
        pourquoi: "Un commerce : un endroit." },
      { txt: "Montréal", ok: 'terr',
        rat: "C'est un nom de ville, écrit avec une majuscule et sans rien devant. Ce n'est "
           + "pas un commerce où l'on entre&nbsp;: c'est un territoire.",
        pourquoi: "Une ville : un territoire." },
      { txt: "ma sœur", ok: 'pers',
        rat: "Une personne, sans ambiguïté possible. Gardez-la en tête&nbsp;: c'est le cas le "
           + "plus clair des trois, et il donne la règle des autres.",
        pourquoi: "Une personne." },
      { txt: "le Québec", ok: 'terr',
        rat: "Une province porte un article — «&nbsp;le&nbsp;» Québec — et c'est justement "
           + "cet article qui va compter tout à l'heure. Mais on n'y entre pas comme dans un "
           + "commerce&nbsp;: c'est un territoire.",
        pourquoi: "Une province : un territoire." },
      { txt: "l'épicerie", ok: 'lieu',
        rat: "Un commerce, comme la pharmacie. L'apostrophe change la façon de l'écrire, pas "
           + "sa nature.",
        pourquoi: "Un commerce : un endroit." },
      { txt: "l'Ontario", ok: 'terr',
        rat: "Une province voisine. Elle commence par une voyelle, ce qui aura son "
           + "importance&nbsp;; pour l'instant, rangez-la avec les territoires.",
        pourquoi: "Une province : un territoire." },
      { txt: "le dépanneur", ok: 'lieu',
        rat: "Attention à celui-là&nbsp;: «&nbsp;dépanneur&nbsp;» peut désigner une personne "
           + "qui répare, mais au Québec c'est d'abord <b>le commerce du coin</b>. C'est un "
           + "endroit, et c'est bien ainsi que tout le monde l'entend.",
        pourquoi: "Le commerce du coin : un endroit." },
    ],
    attente: "Tranchez les huit destinations pour continuer.",
  },

  // ── 3. La règle, écrite comme un constat, et le test. ────────────────────
  {
    id:   'trois-piles',
    type: 'notion',
    eye:  'Ce que vous venez de faire',
    menu: 'Le classement',
    titre: "Vos trois piles sont exactement trois façons de dire « je vais ».",
    paras: [
      "<b>Quelqu'un</b> → «&nbsp;je vais <b>chez</b> le dentiste&nbsp;», «&nbsp;chez ma "
      + "sœur&nbsp;». <b>Un endroit</b> → «&nbsp;je vais <b>à la</b> pharmacie&nbsp;», "
      + "«&nbsp;<b>au</b> dépanneur&nbsp;», «&nbsp;<b>à l'</b>épicerie&nbsp;». "
      + "<b>Un territoire</b> → «&nbsp;je vais <b>à</b> Montréal&nbsp;», «&nbsp;<b>au</b> "
      + "Québec&nbsp;», «&nbsp;<b>en</b> Ontario&nbsp;».",

      "Ces petits mots s'appellent des <b>prépositions</b>. Vous n'avez pas eu besoin du nom "
      + "pour faire le tri, mais votre enseignant l'emploiera.",

      "<b>Le test, en deux temps&nbsp;:</b> d'abord, est-ce que je vais vers <b>une "
      + "personne</b>&nbsp;? Si oui, <i>chez</i>, et c'est réglé. Sinon, je regarde comment "
      + "je nomme le lieu <b>quand il est tout seul</b>&nbsp;: «&nbsp;la pharmacie&nbsp;» → "
      + "à la&nbsp;; «&nbsp;le dépanneur&nbsp;» → au&nbsp;; «&nbsp;Montréal&nbsp;», rien "
      + "devant → à.",

      "Ce n'est donc pas une liste à apprendre&nbsp;: c'est <b>une question à se poser</b>, "
      + "et elle marche sur un lieu que vous n'avez jamais nommé.",
    ],
    retenir: "Une personne → <b>chez</b>. Sinon, le mot qui accompagne le lieu quand il est "
           + "seul décide de ce qu'on écrit devant.",
    attente: "Lisez, puis continuez.",
  },

  // ── 4. Le piège de « chez » : la personne, même derrière un commerce. ────
  {
    id:   'chez-qui',
    type: 'verif',
    eye:  'Le cas qui trompe',
    menu: 'Le métier',
    titre: "« Chez » ne se met que devant quelqu'un — et un métier, c'est quelqu'un.",
    consigne: "Ana écrit une note à l'école pour l'absence de son fils. Quelle version&nbsp;?",
    options: [
      { txt: "«&nbsp;Il avait un rendez-vous chez l'orthophoniste.&nbsp;»", juste: true },
      { txt: "«&nbsp;Il avait un rendez-vous à l'orthophoniste.&nbsp;»",
        rat_t: "Le mot ressemble à un lieu, et n'en est pas un.",
        rat: "«&nbsp;À l'&nbsp;» est juste devant un endroit — «&nbsp;à l'école&nbsp;», "
           + "«&nbsp;à l'épicerie&nbsp;» — et un nom de métier a l'air pareil à l'écrit. Mais "
           + "on n'a pas rendez-vous avec un bâtiment&nbsp;: on a rendez-vous avec une "
           + "<b>personne</b>, donc <i>chez</i>." },
      { txt: "«&nbsp;Il avait un rendez-vous à la clinique d'orthophonie.&nbsp;»",
        rat_t: "Correcte, mais ce n'est pas la même chose.",
        rat: "Cette phrase s'écrit très bien — une clinique est un endroit, donc "
           + "«&nbsp;à la&nbsp;». Elle ne dit simplement pas ce qu'Ana veut dire&nbsp;: "
           + "<b>la nature du lieu décide du mot</b>, et changer le mot revient à changer le "
           + "lieu." },
    ],
    pourquoi: "Tous les métiers fonctionnent ainsi&nbsp;: <b>chez</b> le dentiste, chez le "
            + "notaire, chez le coiffeur, chez la vétérinaire. Et par extension, <i>chez</i> "
            + "s'emploie aussi devant le nom d'un commerce qui porte un nom de "
            + "personne&nbsp;: «&nbsp;je travaille chez Desjardins&nbsp;». Le mot va toujours "
            + "vers quelqu'un.",
    attente: "Choisissez une réponse pour continuer.",
  },

  // ── 5. Les territoires : l'article du lieu décide. ───────────────────────
  {
    id:   'territoires',
    type: 'notion',
    eye:  'La pile des territoires',
    menu: 'Villes et pays',
    titre: "Pour un territoire, regardez le mot qui vient devant son nom.",
    paras: [
      "Une <b>ville</b> n'a rien devant elle&nbsp;: on dit «&nbsp;Montréal&nbsp;», "
      + "«&nbsp;Laval&nbsp;», «&nbsp;Sherbrooke&nbsp;». Alors on n'écrit rien de plus "
      + "non plus&nbsp;: <b>à</b> Montréal, <b>à</b> Laval, <b>à</b> Sherbrooke.",

      "Une <b>province</b> ou un <b>pays</b> porte un article, et c'est lui qui décide. On "
      + "dit «&nbsp;<i>le</i> Québec&nbsp;» → <b>au</b> Québec, «&nbsp;<i>le</i> "
      + "Manitoba&nbsp;» → <b>au</b> Manitoba, «&nbsp;<i>le</i> Maroc&nbsp;» → <b>au</b> "
      + "Maroc. On dit «&nbsp;<i>la</i> Colombie-Britannique&nbsp;» → <b>en</b> "
      + "Colombie-Britannique, «&nbsp;<i>la</i> France&nbsp;» → <b>en</b> France.",

      "Deux ajouts, et il n'y en a pas d'autres. Devant une <b>voyelle</b>, c'est toujours "
      + "<i>en</i>, quel que soit l'article&nbsp;: «&nbsp;<i>l'</i>Ontario&nbsp;» → <b>en</b> "
      + "Ontario, «&nbsp;<i>l'</i>Alberta&nbsp;» → <b>en</b> Alberta, «&nbsp;<i>l'</i>"
      + "Ukraine&nbsp;» → <b>en</b> Ukraine. Et devant un nom au pluriel, "
      + "<i>aux</i>&nbsp;: «&nbsp;<i>les</i> États-Unis&nbsp;» → <b>aux</b> États-Unis.",

      "Vous n'avez donc <b>aucune liste de pays à apprendre</b>. Vous avez une question à "
      + "poser au nom du territoire&nbsp;: qu'est-ce qu'on met devant lui quand il est "
      + "seul&nbsp;?",
    ],
    retenir: "Rien devant le nom → <b>à</b>. «&nbsp;le&nbsp;» → <b>au</b>. "
           + "«&nbsp;la&nbsp;» ou une voyelle → <b>en</b>. «&nbsp;les&nbsp;» → <b>aux</b>.",
    attente: "Lisez, puis continuez.",
  },

  // ── 6. Trier des phrases écrites, avec le test en main. ──────────────────
  {
    id:   'tri-correct',
    type: 'tri',
    eye:  'À vous de trancher',
    menu: 'Six phrases',
    titre: "Six phrases prises dans de vrais messages. Lesquelles sont correctes ?",
    consigne: "Reprenez le test&nbsp;: une personne&nbsp;? Sinon, qu'est-ce qu'on met devant "
            + "le lieu quand il est seul&nbsp;?",
    colonnes: [
      { id: 'ok',   t: 'Correct',   b: 'Correct' },
      { id: 'faux', t: 'Une faute', b: 'Une faute' },
    ],
    items: [
      { txt: "«&nbsp;Je passe à la pharmacie en revenant.&nbsp;»", sous: "texto",
        ok: 'ok',
        rat: "On dit «&nbsp;<i>la</i> pharmacie&nbsp;»&nbsp;: donc «&nbsp;à la&nbsp;». Le cas "
           + "le plus fréquent de tous, et il ne demande aucune réflexion.",
        pourquoi: "« la pharmacie » : à la. Juste." },
      { txt: "«&nbsp;Mon rendez-vous au notaire est reporté.&nbsp;»", sous: "courriel",
        ok: 'faux',
        rat: "Un notaire a un bureau, une adresse, des heures&nbsp;— on le prend donc pour un "
           + "endroit. C'est pourtant une personne&nbsp;: «&nbsp;<b>chez</b> le "
           + "notaire&nbsp;».",
        pourquoi: "Une personne : chez le notaire." },
      { txt: "«&nbsp;Ma famille habite en Alberta depuis 2019.&nbsp;»", sous: "formulaire",
        ok: 'ok',
        rat: "«&nbsp;<i>L'</i>Alberta&nbsp;» commence par une voyelle&nbsp;: c'est "
           + "<i>en</i>, sans avoir à chercher si le nom est masculin ou féminin.",
        pourquoi: "Une voyelle : en Alberta. Juste." },
      { txt: "«&nbsp;J'ai déménagé en Montréal l'été passé.&nbsp;»", sous: "message à un ami",
        ok: 'faux',
        rat: "La faute vient d'une bonne habitude&nbsp;: on a retenu «&nbsp;en France&nbsp;», "
           + "«&nbsp;en Ontario&nbsp;», et on l'étend. Mais Montréal est une <b>ville</b>, et "
           + "une ville n'a rien devant son nom&nbsp;: «&nbsp;<b>à</b> Montréal&nbsp;».",
        pourquoi: "Une ville : à Montréal." },
      { txt: "«&nbsp;Les enfants sont chez leur grand-mère cette semaine.&nbsp;»",
        sous: "note à l'école", ok: 'ok',
        rat: "Une personne&nbsp;: <i>chez</i>, et rien à décider de plus. C'est le cas où le "
           + "test s'arrête à la première question.",
        pourquoi: "Une personne : chez. Juste." },
      { txt: "«&nbsp;Je vais à le bureau de poste avant midi.&nbsp;»", sous: "texto",
        ok: 'faux',
        rat: "Le raisonnement est juste — un endroit, donc «&nbsp;à&nbsp;» plus son article — "
           + "mais ces deux mots ne se rencontrent jamais&nbsp;: ils se collent en "
           + "«&nbsp;<b>au</b> bureau de poste&nbsp;».",
        pourquoi: "« à le » n'existe pas : au bureau de poste." },
    ],
    attente: "Tranchez les six phrases pour continuer.",
  },

  // ── 7. La confusion locale : à Québec / au Québec. ───────────────────────
  {
    id:   'quebec',
    type: 'verif',
    eye:  'Le cas qui trompe',
    menu: 'Québec, deux fois',
    titre: "« À Québec » et « au Québec » ne veulent pas dire la même chose.",
    consigne: "Bilal remplit un formulaire d'inscription. Il habite à Longueuil et n'a jamais "
            + "quitté la province. Que doit-il écrire&nbsp;?",
    options: [
      { txt: "«&nbsp;J'habite au Québec depuis trois ans.&nbsp;»", juste: true },
      { txt: "«&nbsp;J'habite à Québec depuis trois ans.&nbsp;»",
        rat_t: "Cette phrase est correcte, et elle dit autre chose.",
        rat: "«&nbsp;<b>À</b> Québec&nbsp;» désigne la <b>ville</b> de Québec — celle du "
           + "Château Frontenac, à deux heures et demie de Longueuil. Le même nom sert aux "
           + "deux, et c'est le petit mot qui les distingue&nbsp;: la ville n'a pas "
           + "d'article, la province a «&nbsp;<i>le</i>&nbsp;»." },
      { txt: "«&nbsp;J'habite en Québec depuis trois ans.&nbsp;»",
        rat_t: "Bon réflexe de territoire, mauvais article.",
        rat: "Vous avez reconnu un territoire, ce qui est l'essentiel. Mais <i>en</i> "
           + "correspond à «&nbsp;<i>la</i>&nbsp;» ou à une voyelle&nbsp;: on dit "
           + "«&nbsp;<i>le</i> Québec&nbsp;», donc <b>au</b>. Comparez&nbsp;: «&nbsp;en "
           + "Ontario&nbsp;», «&nbsp;au Québec&nbsp;»." },
    ],
    pourquoi: "«&nbsp;<b>Au</b> Québec&nbsp;» pour la province, «&nbsp;<b>à</b> "
            + "Québec&nbsp;» pour la ville. C'est la seule paire de ce genre que vous "
            + "rencontrerez tous les jours&nbsp;; elle vaut la peine d'être vérifiée sur un "
            + "formulaire, où la différence est lue.",
    attente: "Choisissez une réponse pour continuer.",
  },

  // ── 8. Le cas par défaut, dit en dernier. ────────────────────────────────
  {
    id:   'le-cas-ordinaire',
    type: 'notion',
    eye:  'Ce qui reste',
    menu: 'Le cas ordinaire',
    titre: "Tout le reste — la grande majorité — n'a rien de particulier.",
    paras: [
      "On a gardé celui-ci pour la fin, et c'est volontaire&nbsp;: c'est le plus fréquent, et "
      + "c'est le seul où il n'y a <b>rien à décider</b>. Devant un endroit ordinaire, on "
      + "écrit <i>à</i> suivi de l'article du lieu&nbsp;: à la bibliothèque, à la banque, à "
      + "l'école, à l'aéroport, au parc, au bureau, au centre commercial.",

      "Une seule chose à savoir&nbsp;: <b>«&nbsp;à le&nbsp;» n'existe pas</b>. Ces deux mots "
      + "se collent toujours et donnent <b>au</b>&nbsp;; au pluriel, ils donnent <b>aux</b> "
      + "(aux toilettes, aux bureaux de la commission). Ce n'est pas une règle de plus, c'est "
      + "une soudure obligatoire.",

      "Autrement dit, vous n'avez que <b>deux moments d'attention</b> quand vous écrivez "
      + "où vous allez&nbsp;: est-ce quelqu'un&nbsp;? est-ce un territoire&nbsp;? Partout "
      + "ailleurs, écrivez sans y penser.",
    ],
    retenir: "Endroit ordinaire → <b>à</b> + son article, et «&nbsp;à le&nbsp;» se soude en "
           + "<b>au</b>. C'est le cas par défaut, et il ne demande rien.",
    attente: "Lisez, puis continuez.",
  },

  // ── 9. Trois cas dans la même production. ────────────────────────────────
  {
    id:   'trois-dans-une',
    type: 'verif',
    eye:  'Vérification',
    menu: 'Un message entier',
    titre: "Trois versions du même message. Une seule tient d'un bout à l'autre.",
    consigne: "Nadia prévient son employeur de trois absences. Regardez chaque destination, "
            + "l'une après l'autre.",
    options: [
      { txt: "«&nbsp;Lundi je vais chez le dentiste, mardi à la clinique, et en juillet je "
           + "pars deux semaines au Portugal.&nbsp;»", juste: true },
      { txt: "«&nbsp;Lundi je vais au dentiste, mardi à la clinique, et en juillet je pars "
           + "deux semaines au Portugal.&nbsp;»",
        rat_t: "Le territoire est bon. C'est la personne qui a été traitée comme un lieu.",
        rat: "«&nbsp;<i>Le</i> Portugal&nbsp;» → «&nbsp;au Portugal&nbsp;»&nbsp;: parfait, et "
           + "c'est le cas le plus technique des trois. Mais un dentiste est quelqu'un&nbsp;: "
           + "«&nbsp;<b>chez</b> le dentiste&nbsp;». La première question du test est celle "
           + "qu'on saute quand on est pressé." },
      { txt: "«&nbsp;Lundi je vais chez le dentiste, mardi à la clinique, et en juillet je "
           + "pars deux semaines en Portugal.&nbsp;»",
        rat_t: "Les deux premières sont justes. Le pays a pris le mauvais article.",
        rat: "«&nbsp;Chez le dentiste&nbsp;» et «&nbsp;à la clinique&nbsp;»&nbsp;: la "
           + "personne et l'endroit sont bien séparés, c'est l'essentiel du point. Reste le "
           + "pays&nbsp;: on dit «&nbsp;<i>le</i> Portugal&nbsp;», pas «&nbsp;la&nbsp;», et "
           + "il ne commence pas par une voyelle — donc <b>au</b> Portugal." },
    ],
    pourquoi: "Une personne, un endroit, un territoire&nbsp;: les trois piles de l'écran 2, "
            + "dans une seule phrase. <b>C'est tout le point express en une ligne.</b>",
    attente: "Choisissez une réponse pour continuer.",
  },

  // ── 10. La fermeture : le cas de l'écran 1. ──────────────────────────────
  {
    id:   'fermeture',
    type: 'verif',
    eye:  'La dernière',
    menu: 'Pour finir',
    titre: "On revient au message du début, avec une destination de plus.",
    consigne: "Le rendez-vous de jeudi a été déplacé dans un hôpital de la ville de Québec. "
            + "Quelle version écrivez-vous à votre employeur&nbsp;?",
    options: [
      { txt: "«&nbsp;Jeudi, je vais chez le médecin&nbsp;; le rendez-vous est à l'hôpital, à "
           + "Québec.&nbsp;»", juste: true },
      { txt: "«&nbsp;Jeudi, je vais au médecin&nbsp;; le rendez-vous est à l'hôpital, à "
           + "Québec.&nbsp;»",
        rat_t: "C'est la phrase de l'écran 1, restée telle quelle.",
        rat: "La ville et l'hôpital sont impeccables&nbsp;: «&nbsp;à l'hôpital&nbsp;» pour "
           + "l'endroit, «&nbsp;à Québec&nbsp;» pour la ville. Mais le médecin est une "
           + "personne, et c'est justement la phrase par laquelle ce point express a "
           + "commencé&nbsp;: «&nbsp;<b>chez</b> le médecin&nbsp;»." },
      { txt: "«&nbsp;Jeudi, je vais chez le médecin&nbsp;; le rendez-vous est à l'hôpital, au "
           + "Québec.&nbsp;»",
        rat_t: "Vous avez le plus difficile. C'est la ville qui est devenue une province.",
        rat: "«&nbsp;Chez le médecin&nbsp;»&nbsp;: exact, et c'était le but. Mais "
           + "«&nbsp;<b>au</b> Québec&nbsp;» annonce la province — votre employeur, qui y est "
           + "déjà, ne comprendra pas ce que vous précisez. Pour la ville&nbsp;: "
           + "«&nbsp;<b>à</b> Québec&nbsp;»." },
    ],
    pourquoi: "«&nbsp;Chez le médecin&nbsp;», «&nbsp;à l'hôpital&nbsp;», «&nbsp;à "
            + "Québec&nbsp;». Vous n'avez rien mémorisé&nbsp;: vous avez posé deux fois la "
            + "même question — <b>est-ce quelqu'un&nbsp;? sinon, qu'est-ce qu'on met devant "
            + "ce lieu quand il est seul&nbsp;?</b> Elle marchera sur une destination que "
            + "vous n'avez jamais écrite.",
    attente: "Choisissez une réponse pour finir.",
  },

];
