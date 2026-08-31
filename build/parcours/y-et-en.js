// ═══════════════════════════════════════════════════════════════════════════
// Point express — « J'y vais », « j'en prends » : les deux mots qu'on oublie
//
// Savoir n3-s22 (Pronoms personnels conjoints CD et CI — « Remplacer un GN
// introduit par un déterminant quantifiant par en »), prolongé par le « y » de
// lieu que le niveau 4 reprend (n4-s22). Une ORDONNANCE : l'enseignant
// l'envoie à un élève qui répond « J'ai deux » ou « Je vais » — la phrase
// amputée du petit mot.
//
// ── Ce qui le sépare de ce qui existe déjà ─────────────────────────────────
// L'étagère porte déjà « Je le vois ou je lui parle ? », qui fait CHOISIR
// entre deux pronoms de personne. Les mini-leçons des modules ajoutent « Le,
// en, y : reprendre sans répéter », « y et là », « Ne pas tout répéter : le,
// lui, y, en » — toutes bâties sur la même idée : quatre pronoms alignés dans
// un tableau, et l'élève doit désigner le bon.
//
// Ce point-ci ne fait pas choisir : il fait REMARQUER UNE ABSENCE. La faute de
// l'élève de niveau 3 n'est presque jamais « j'y ai deux » ; c'est « j'ai
// deux », la phrase où le petit mot n'est simplement pas là. Un tableau à
// quatre entrées ne peut pas corriger ça — il répond à une question que
// l'élève ne se pose pas. Les cinq écarts tenus :
//
//   1. INDUCTIF. L'élève trie huit réponses entendues au comptoir AVANT
//      qu'aucune règle ne soit dite. La règle de l'écran 3 est écrite comme
//      un constat : « vous avez suivi le petit mot de la question ».
//   2. PARTIEL. Deux emplois seulement — la quantité et le lieu — et rien sur
//      le reste. Un test unique : REGARDER LE MOT DE LA QUESTION. « de » ou
//      un nombre appelle « en » ; « à », « au », « chez » appellent « y ».
//   3. L'OUBLI EST LE SUJET, pas le choix. Trois écrans sur dix portent sur
//      la phrase amputée, jamais sur la confusion entre les deux mots.
//   4. LE MÉTALANGAGE EST DIT UNE FOIS, à l'écran 3, après huit tris.
//   5. EXEMPLES VARIÉS : un comptoir de pharmacie, un formulaire d'école, un
//      texto, une entrevue d'embauche, un appel au propriétaire.
//
// Aucun média : les deux mots sont d'une syllabe et ne posent aucun problème
// d'écoute. Ce qui manque, c'est de les dire — pas de les entendre.
// ═══════════════════════════════════════════════════════════════════════════

const PARCOURS = {
  slug:     'y-et-en',
  titre:    "« J'y vais », « j'en prends » : les deux mots qu'on oublie",
  surtitre: "Point express · 10 minutes",
  niveau:   3,
  savoir:   'n3-s22',
};

const ECRANS = [

  // ── 1. Une décision, sans aucune règle donnée. ───────────────────────────
  {
    id:   'depart',
    type: 'verif',
    eye:  'Une question, pour commencer',
    menu: 'Deux enfants',
    titre: "À l'école, on vous demande : « Vous avez des enfants ? »",
    consigne: "Vous en avez deux. Répondez avec ce que vous savez déjà — ou au feeling. "
            + "On expliquera après&nbsp;: c'est fait exprès.",
    options: [
      { txt: "«&nbsp;Oui, j'en ai deux.&nbsp;»", juste: true },
      { txt: "«&nbsp;Oui, j'ai deux.&nbsp;»",
        rat_t: "C'est la phrase la plus fréquente, et il lui manque un mot.",
        rat: "Elle se comprend, et personne ne vous reprendra. Mais elle est incomplète&nbsp;: "
           + "en français, un nombre tout seul après le verbe ne tient pas debout. Il faut "
           + "rappeler <b>de quoi</b> on compte deux — c'est le travail du petit mot manquant." },
      { txt: "«&nbsp;Oui, je les ai deux.&nbsp;»",
        rat_t: "Vous avez senti qu'un mot manquait — c'est déjà l'essentiel.",
        rat: "Vous avez pris «&nbsp;les&nbsp;», qui sert quand on parle d'enfants précis "
           + "(«&nbsp;mes enfants, je <b>les</b> emmène&nbsp;»). Ici on compte&nbsp;: la question "
           + "dit «&nbsp;<b>des</b> enfants&nbsp;», pas «&nbsp;les vôtres&nbsp;». Un autre mot "
           + "sert à ça." },
    ],
    pourquoi: "«&nbsp;J'en ai deux.&nbsp;» Gardez la phrase&nbsp;: on y revient au dernier écran.",
    attente: "Choisissez une réponse pour continuer.",
  },

  // ── 2. On trie AVANT de savoir. ──────────────────────────────────────────
  {
    id:   'tri-huit',
    type: 'tri',
    eye:  'À vous de trancher',
    menu: 'Huit réponses',
    titre: "Huit réponses entendues cette semaine. Quel petit mot manque ?",
    consigne: "Aucune règle ne vous a été donnée — normal. Lisez la question écrite sous chaque "
            + "réponse&nbsp;: elle vous dit presque tout.",
    colonnes: [
      { id: 'en', t: "Il manque « en »", b: "« en »" },
      { id: 'y',  t: "Il manque « y »",  b: "« y »" },
    ],
    items: [
      { txt: "Oui, j'___ ai trois.", sous: "« Avez-vous des reçus ? »", ok: 'en',
        rat: "La question dit «&nbsp;<b>des</b> reçus&nbsp;» et vous répondez par un nombre. On "
           + "compte&nbsp;: c'est le mot qui rappelle une quantité.",
        pourquoi: "J'en ai trois. On compte des reçus." },
      { txt: "J'___ vais demain matin.", sous: "« Quand allez-vous à la clinique ? »", ok: 'y',
        rat: "La question dit «&nbsp;<b>à</b> la clinique&nbsp;»&nbsp;: un endroit. Le mot qui "
           + "remplace un endroit n'est pas celui qui compte.",
        pourquoi: "J'y vais. « y » remplace « à la clinique »." },
      { txt: "Non, je n'___ ai plus.", sous: "« Il vous reste du lait ? »", ok: 'en',
        rat: "«&nbsp;<b>Du</b> lait&nbsp;» est une quantité, pas un endroit. Et à la forme "
           + "négative, le petit mot ne disparaît pas&nbsp;: il se glisse entre «&nbsp;n'&nbsp;» "
           + "et le verbe.",
        pourquoi: "Je n'en ai plus. « du lait » = une quantité." },
      { txt: "Mon fils ___ est déjà allé.", sous: "« Il connaît le parc Maisonneuve ? »", ok: 'y',
        rat: "Un parc est un endroit. Rien ne se compte dans cette phrase.",
        pourquoi: "Il y est allé. Un endroit." },
      { txt: "Oui, j'___ ai besoin aujourd'hui.", sous: "« Vous avez besoin de la voiture ? »", ok: 'en',
        rat: "Celui-là trompe&nbsp;: la voiture n'est pas une quantité. Mais regardez le verbe — "
           + "«&nbsp;avoir besoin <b>de</b>&nbsp;». C'est le mot «&nbsp;de&nbsp;» qui décide, "
           + "pas ce dont on parle.",
        pourquoi: "Besoin DE quelque chose : « en »." },
      { txt: "Elle ___ travaille depuis six ans.", sous: "« Elle travaille à l'usine ? »", ok: 'y',
        rat: "«&nbsp;À l'usine&nbsp;» est un lieu de travail — donc un endroit, comme la "
           + "clinique et le parc.",
        pourquoi: "Elle y travaille. Un endroit." },
      { txt: "Je ___ prends deux, s'il vous plaît.", sous: "« Combien de billets voulez-vous ? »", ok: 'en',
        rat: "«&nbsp;Combien <b>de</b> billets&nbsp;»&nbsp;: on compte. Et remarquez que le "
           + "nombre reste à sa place, après le verbe.",
        pourquoi: "J'en prends deux. Le nombre reste après." },
      { txt: "N'___ pensez plus.", sous: "« Je pense encore à cette erreur. »", ok: 'y',
        rat: "Celui-là n'est pas un endroit, et pourtant c'est le même mot&nbsp;: on dit "
           + "«&nbsp;penser <b>à</b>&nbsp;». Le mot de la phrase de départ décide encore.",
        pourquoi: "Penser À quelque chose : « y »." },
    ],
    attente: "Tranchez les huit cas pour continuer.",
  },

  // ── 3. La règle, écrite comme un constat de ce qu'il vient de faire. ─────
  {
    id:   'le-test',
    type: 'notion',
    eye:  'Ce que vous venez de faire',
    menu: 'Le test',
    titre: "Vous n'avez pas deviné : vous avez suivi le mot de la question.",
    paras: [
      "Relisez votre colonne «&nbsp;en&nbsp;»&nbsp;: chaque question portait un "
      + "<b>de</b>, un <b>du</b>, un <b>des</b> ou un nombre. Votre colonne "
      + "«&nbsp;y&nbsp;»&nbsp;: chaque question portait un <b>à</b>, un <b>au</b>, un "
      + "<b>chez</b>. Vous n'avez pas eu besoin de savoir ce que remplaçait le mot.",

      "<b>Le test, sur n'importe quelle phrase&nbsp;:</b> cherchez la petite préposition "
      + "juste devant le groupe à remplacer. «&nbsp;de&nbsp;», «&nbsp;du&nbsp;», "
      + "«&nbsp;des&nbsp;» ou un nombre&nbsp;→ <b>en</b>. «&nbsp;à&nbsp;», "
      + "«&nbsp;au&nbsp;», «&nbsp;chez&nbsp;», «&nbsp;dans&nbsp;»&nbsp;→ <b>y</b>.",

      "Ces deux mots s'appellent des <b>pronoms</b>&nbsp;: ils tiennent la place d'un groupe "
      + "entier pour qu'on n'ait pas à le redire. Votre enseignant emploiera le mot&nbsp;; "
      + "vous n'en avez pas besoin pour vous en servir.",
    ],
    retenir: "Regardez la préposition de la question. <b>de, du, des, un nombre</b> → «&nbsp;en&nbsp;». "
           + "<b>à, au, chez, dans</b> → «&nbsp;y&nbsp;».",
    attente: "Lisez, puis continuez.",
  },

  // ── 4. Le vrai défaut : le mot n'est pas choisi, il est absent. ──────────
  {
    id:   'labsence',
    type: 'verif',
    eye:  'Le défaut à corriger',
    menu: 'Le mot absent',
    titre: "Le pharmacien demande : « Il vous reste des comprimés ? »",
    consigne: "Il vous en reste quatre. Trois réponses sont possibles à l'oreille&nbsp;: "
            + "une seule est une phrase complète.",
    options: [
      { txt: "«&nbsp;Il m'en reste quatre.&nbsp;»", juste: true },
      { txt: "«&nbsp;Il me reste quatre.&nbsp;»",
        rat_t: "C'est la faute que ce point vient corriger.",
        rat: "Rien n'est mal placé, rien n'est mal accordé&nbsp;: il manque simplement le mot. "
           + "Un nombre seul après le verbe laisse la phrase en suspens — quatre <b>quoi</b>&nbsp;? "
           + "En français, le nombre ne se suffit jamais à lui-même." },
      { txt: "«&nbsp;Il me reste quatre comprimés.&nbsp;»",
        rat_t: "Correcte, mais vous répétez ce que le pharmacien vient de dire.",
        rat: "Cette phrase est juste et personne ne vous reprendra. Seulement, tout l'intérêt "
           + "du petit mot est là&nbsp;: il évite de redire «&nbsp;comprimés&nbsp;» une seconde "
           + "fois dans le même échange. C'est ce que fait un locuteur d'ici." },
    ],
    pourquoi: "Le nombre reste après le verbe, et le petit mot passe <b>devant</b>&nbsp;: "
            + "«&nbsp;il m'<b>en</b> reste quatre&nbsp;».",
    attente: "Choisissez une réponse pour continuer.",
  },

  // ── 5. Où le mot se pose. ────────────────────────────────────────────────
  {
    id:   'la-place',
    type: 'notion',
    eye:  'La place',
    menu: 'Où le poser',
    titre: "Ces deux mots se placent avant le verbe, et jamais à la fin.",
    paras: [
      "C'est la grande différence avec beaucoup de langues&nbsp;: le mot ne vient pas après. "
      + "«&nbsp;J'<b>y</b> vais.&nbsp;» «&nbsp;J'<b>en</b> veux.&nbsp;» "
      + "«&nbsp;Je n'<b>y</b> suis jamais allé.&nbsp;»",

      "Quand il y a <b>deux verbes</b>, il se colle au second&nbsp;: «&nbsp;Je vais "
      + "<b>y</b> passer demain.&nbsp;» «&nbsp;Tu peux <b>en</b> prendre un autre.&nbsp;» "
      + "Jamais «&nbsp;j'y vais passer&nbsp;».",

      "Une seule exception, et c'est celle qu'on entend tous les jours&nbsp;: quand on donne "
      + "une consigne, le mot passe <b>derrière</b>, attaché par un trait "
      + "d'union — «&nbsp;<i>Vas-<b>y</b>.</i>&nbsp;» «&nbsp;<i>Prenez-<b>en</b> deux.</i>&nbsp;» "
      + "«&nbsp;<i>Allez-<b>y</b> avant midi.</i>&nbsp;»",
    ],
    retenir: "Avant le verbe. Deux verbes&nbsp;: avant le second. Une consigne&nbsp;: derrière, "
           + "avec un trait d'union.",
    attente: "Lisez, puis continuez.",
  },

  // ── 6. Trier des phrases écrites. ────────────────────────────────────────
  {
    id:   'tri-ecrites',
    type: 'tri',
    eye:  'À vous de trancher',
    menu: 'Six phrases',
    titre: "Six phrases écrites. Lesquelles tiennent ?",
    consigne: "Regardez deux choses seulement&nbsp;: le mot est-il là, et est-il à la bonne place&nbsp;?",
    colonnes: [
      { id: 'ok',   t: 'Correcte',  b: 'Correcte' },
      { id: 'faux', t: 'Une faute', b: 'Une faute' },
    ],
    items: [
      { txt: "Je vais y aller vendredi.", ok: 'ok',
        rat: "Deux verbes, et le mot est collé au second. C'est exactement la règle de l'écran "
           + "précédent.",
        pourquoi: "Deux verbes : le mot va devant le second." },
      { txt: "J'ai besoin, pouvez-vous m'aider ?", ok: 'faux',
        rat: "«&nbsp;Avoir besoin&nbsp;» ne se termine jamais en l'air&nbsp;: besoin de "
           + "<b>quoi</b>&nbsp;? Il faut «&nbsp;j'<b>en</b> ai besoin&nbsp;», ou nommer la chose.",
        pourquoi: "Il manque « en » : j'en ai besoin." },
      { txt: "Prenez-en une le matin et une le soir.", ok: 'ok',
        rat: "Une consigne&nbsp;: le mot passe derrière, avec le trait d'union. Et les deux "
           + "nombres restent à leur place.",
        pourquoi: "Une consigne : le mot passe derrière." },
      { txt: "Je vais en parler à mon propriétaire.", ok: 'ok',
        rat: "«&nbsp;Parler <b>de</b> quelque chose&nbsp;»&nbsp;: le mot est le bon, et il est "
           + "collé au second verbe.",
        pourquoi: "Parler DE : « en », devant l'infinitif." },
      { txt: "Ma fille va à l'école, elle aime beaucoup.", ok: 'faux',
        rat: "On aime beaucoup <b>quoi</b>&nbsp;? La phrase s'arrête avant sa fin. Il faut "
           + "«&nbsp;elle <b>y</b> va&nbsp;» plus loin, ou «&nbsp;elle aime beaucoup "
           + "l'école&nbsp;» — mais pas un verbe laissé seul.",
        pourquoi: "Le verbe reste sans complément." },
      { txt: "Je en veux deux, s'il vous plaît.", ok: 'faux',
        rat: "La place est bonne et le mot aussi&nbsp;: c'est l'écriture qui accroche. Devant "
           + "«&nbsp;en&nbsp;», le «&nbsp;je&nbsp;» perd son «&nbsp;e&nbsp;» — "
           + "«&nbsp;<b>j'en</b> veux deux&nbsp;».",
        pourquoi: "Il faut « j'en » : je + en se soudent." },
    ],
    attente: "Tranchez les six phrases pour continuer.",
  },

  // ── 7. Le cas qui trompe : ni quantité, ni lieu. ─────────────────────────
  {
    id:   'ni-lun-ni-lautre',
    type: 'verif',
    eye:  'Le cas qui trompe',
    menu: 'Ni compter, ni aller',
    titre: "« Je pense souvent à mon examen. » Comment le dire plus court ?",
    consigne: "Ici on ne compte rien et on ne va nulle part. Le test de l'écran 3 marche "
            + "quand même — regardez seulement la préposition.",
    options: [
      { txt: "«&nbsp;J'y pense souvent.&nbsp;»", juste: true },
      { txt: "«&nbsp;J'en pense souvent.&nbsp;»",
        rat_t: "Vous avez cherché une quantité — il n'y en a pas.",
        rat: "C'est logique&nbsp;: un examen n'est ni un lieu ni une quantité, alors on hésite. "
           + "Mais le test ne demande pas ce qu'est la chose&nbsp;: il demande quelle "
           + "<b>préposition</b> le verbe appelle. On dit «&nbsp;penser <b>à</b>&nbsp;», donc "
           + "«&nbsp;y&nbsp;»." },
      { txt: "«&nbsp;Je le pense souvent.&nbsp;»",
        rat_t: "Cette phrase existe, mais elle dit autre chose.",
        rat: "«&nbsp;Je le pense&nbsp;» veut dire «&nbsp;c'est mon avis&nbsp;». Vous vouliez "
           + "dire que l'examen vous revient en tête&nbsp;: ce n'est pas la même chose, et "
           + "votre interlocuteur ne comprendrait pas." },
    ],
    pourquoi: "Le verbe commande la préposition, et la préposition commande le mot. "
            + "<b>Penser à&nbsp;→ y. Parler de&nbsp;→ en.</b>",
    attente: "Choisissez une réponse pour continuer.",
  },

  // ── 8. Les tours tout faits, dits en dernier. ────────────────────────────
  {
    id:   'les-tours-faits',
    type: 'notion',
    eye:  'Ce qui reste',
    menu: 'Les tours tout faits',
    titre: "Vous employez déjà ces deux mots, sans le savoir.",
    paras: [
      "On a gardé ceci pour la fin parce que ce n'est pas une règle de plus&nbsp;: c'est une "
      + "liste de tours que vous dites peut-être déjà tous les jours. «&nbsp;<b>Il y a</b> "
      + "quelqu'un&nbsp;?&nbsp;» «&nbsp;<b>Vas-y</b>.&nbsp;» «&nbsp;<b>Ça y est</b>.&nbsp;» "
      + "«&nbsp;J'<b>en</b> ai assez.&nbsp;» «&nbsp;Je m'<b>en</b> vais.&nbsp;»",

      "Dans ces tours, personne ne se demande ce que le mot remplace — il fait partie de "
      + "l'expression. Les reconnaître vous donne une chose utile&nbsp;: la preuve que ces deux "
      + "mots ne sont pas une difficulté d'examen, mais deux syllabes de la conversation "
      + "ordinaire.",

      "Il reste donc <b>une seule chose</b> à surveiller quand vous parlez&nbsp;: quand vous "
      + "répondez par un nombre ou par un endroit, le petit mot est-il là&nbsp;?",
    ],
    retenir: "Vous les dites déjà dans «&nbsp;il y a&nbsp;» et «&nbsp;je m'en vais&nbsp;». "
           + "Ce qui manque, ce n'est pas le mot&nbsp;: c'est l'habitude de le poser.",
    attente: "Lisez, puis continuez.",
  },

  // ── 9. Écrire, pas reconnaître. ──────────────────────────────────────────
  {
    id:   'votre-message',
    type: 'verif',
    eye:  'Vérification',
    menu: 'Votre message',
    titre: "Vous écrivez à votre propriétaire. Quelle version tient d'un bout à l'autre ?",
    consigne: "Vous lui avez déjà parlé du robinet. Vous êtes passé au bureau deux fois. "
            + "Trois versions du même message&nbsp;: une seule est correcte partout.",
    options: [
      { txt: "«&nbsp;Je vous ai parlé du robinet. J'y suis passé deux fois et je n'en ai pas "
           + "eu de nouvelles.&nbsp;»", juste: true },
      { txt: "«&nbsp;Je vous ai parlé du robinet. Je suis passé deux fois et je n'ai pas eu "
           + "de nouvelles.&nbsp;»",
        rat_t: "Rien n'est faux — et pourtant deux mots manquent.",
        rat: "Passé <b>où</b>&nbsp;? de nouvelles <b>de quoi</b>&nbsp;? Votre propriétaire "
           + "devinera, parce que le sujet est écrit juste avant. Mais dans une plainte écrite, "
           + "les liens qu'on ne pose pas sont ceux qu'on vous reprochera de ne pas avoir faits." },
      { txt: "«&nbsp;Je vous ai parlé du robinet. J'en suis passé deux fois et je n'y ai pas "
           + "eu de nouvelles.&nbsp;»",
        rat_t: "Les deux mots sont là — ils ont été échangés.",
        rat: "Vous êtes passé <b>au</b> bureau&nbsp;: un endroit, donc «&nbsp;y&nbsp;». Vous "
           + "n'avez pas eu de nouvelles <b>du</b> robinet&nbsp;: un «&nbsp;de&nbsp;», donc "
           + "«&nbsp;en&nbsp;». Reprenez le test sur chaque phrase séparément." },
    ],
    pourquoi: "Un endroit&nbsp;→ y. Un «&nbsp;de&nbsp;»&nbsp;→ en. Deux phrases, deux tests, "
            + "et le message tient.",
    attente: "Choisissez une réponse pour continuer.",
  },

  // ── 10. La fermeture : le cas de l'écran 1. ──────────────────────────────
  {
    id:   'fermeture',
    type: 'verif',
    eye:  'La dernière',
    menu: 'Pour finir',
    titre: "On revient au début : « Vous avez des enfants ? »",
    consigne: "Cette fois, on vous demande aussi s'ils fréquentent l'école du quartier. Vous en "
            + "avez deux, et ils y vont tous les deux. Une seule réponse est complète.",
    options: [
      { txt: "«&nbsp;J'en ai deux, et ils y vont tous les deux.&nbsp;»", juste: true },
      { txt: "«&nbsp;J'ai deux, et ils vont tous les deux.&nbsp;»",
        rat_t: "C'est la phrase de l'écran 1, doublée.",
        rat: "Les deux petits mots manquent au même endroit&nbsp;: après un nombre "
           + "(«&nbsp;j'<b>en</b> ai deux&nbsp;») et devant un verbe de déplacement "
           + "(«&nbsp;ils <b>y</b> vont&nbsp;»). C'est exactement ce que vous veniez de "
           + "corriger&nbsp;: la phrase amputée, pas le mauvais mot." },
      { txt: "«&nbsp;J'en ai deux, et ils en vont tous les deux.&nbsp;»",
        rat_t: "Le premier est juste. Le second suit par habitude.",
        rat: "Une fois qu'on a posé un petit mot, on a envie de reprendre le même. Mais la "
           + "seconde phrase parle d'un endroit — l'école — et l'endroit appelle "
           + "«&nbsp;y&nbsp;». Chaque phrase se teste pour elle-même." },
    ],
    pourquoi: "Vous avez fait les trois choses&nbsp;: remarquer que le mot manquait, le choisir "
            + "sur la préposition, et le poser devant le verbe.",
    attente: "Choisissez une réponse pour finir.",
  },

];
