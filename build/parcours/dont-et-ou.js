// ═══════════════════════════════════════════════════════════════════════════
// Point express — « dont » et « où »
//
// Savoir n5-s25 (« Pronoms relatifs » — employer qui, que, où). Une
// ORDONNANCE : l'enseignant l'envoie à un élève qui évite « dont », ou qui
// écrit « le jour que ». Dix minutes, dix écrans.
//
// ── Ce dont il s'écarte, et comment ────────────────────────────────────────
// Une douzaine de modules portent une mini-leçon « qui, que, dont, où » ; la
// plus complète est `module-n5-services` (bloc t2rel). Elle traite les quatre
// relatifs à la file, chacun avec sa définition grammaticale — « il fait
// l'action », « il subit l'action » —, donne pour « dont » la consigne
// « cherchez le de » et pour « où » le rappel lieu + moment, puis trois
// pièges et un questionnaire. Un élève envoyé ici l'a lue. Les cinq écarts :
//
//   1. DEUX RELATIFS, PAS QUATRE. « qui » et « que » sont laissés dehors :
//      ils se règlent à l'oreille et un élève de niveau 5 les place déjà. Ce
//      point ne traite que les deux qui résistent, et il le dit.
//   2. INDUCTIF, ET LE TRI NE PARLE QUE DE PETITS MOTS. L'écran 2 fait ranger
//      six phrases ordinaires selon le mot qui accompagne la chose dont on
//      parle — « de », un lieu, un moment. Aucun relatif n'apparaît avant
//      l'écran 3 : la règle y est le constat du tri.
//   3. LE TEST PASSE PAR CE QUE LE MOT REMPLACE, JAMAIS PAR LA NOMENCLATURE.
//      Décoller la phrase en deux, remettre la chose dans la seconde, et
//      regarder le mot qui vient avec elle. Ni « antécédent », ni
//      « complément du nom », ni « subordonnée » : le mot « relatif » est le
//      seul terme employé, et il arrive à l'écran 3, après la manipulation.
//   4. L'ERREUR EST L'ENSEIGNEMENT, ET CE SONT LES DEUX VRAIES. Le « de »
//      écrit deux fois (« dont j'ai besoin de ») à l'écran 4 : c'est la faute
//      de celui qui a compris la règle, et aucune mini-leçon ne la traite.
//      « Le jour que » à l'écran 5 : la faute de celui qui parle bien, parce
//      qu'elle s'entend partout à l'oral.
//   5. EXEMPLES PRIS À PLUSIEURS SITUATIONS. Une annonce en ligne, un texto,
//      un message à un propriétaire, une note à l'école, un courriel de
//      candidature. Aucune phrase, aucun scénario d'un module.
//
// Aucun média : ces deux mots s'entendent parfaitement et se placent mal
// quand même. Le travail est de décider, pas d'écouter.
// ═══════════════════════════════════════════════════════════════════════════

const PARCOURS = {
  slug:     'dont-et-ou',
  titre:    "« dont » et « où »",
  surtitre: "Point express · 10 minutes",
  niveau:   5,
  savoir:   'n5-s25',
};

const ECRANS = [

  // ── 1. Une décision, sans aucune règle donnée. ───────────────────────────
  {
    id:   'depart',
    type: 'verif',
    eye:  'Une question, pour commencer',
    menu: 'Deux phrases',
    titre: "Une seule de ces deux phrases s'écrit. Laquelle ?",
    consigne: "Répondez avec ce que vous savez déjà — ou au feeling. On expliquera après&nbsp;: "
            + "c'est fait exprès.",
    options: [
      { txt: "«&nbsp;C'est le logement que je t'ai parlé hier.&nbsp;»",
        rat_t: "Le mot est le bon dans neuf phrases sur dix, mais pas ici.",
        rat: "«&nbsp;Que&nbsp;» est le mot qu'on met par défaut quand on hésite, et il passe "
           + "presque toujours. Le verbe de cette phrase-là refuse&nbsp;: on ne parle pas "
           + "<i>quelque chose</i>, on parle <b>de</b> quelque chose. Regardez l'autre "
           + "version&nbsp;: elle contient encore ce «&nbsp;de&nbsp;», caché." },
      { txt: "«&nbsp;C'est le logement dont je t'ai parlé hier.&nbsp;»", juste: true },
      { txt: "Les deux se disent&nbsp;; la deuxième est plus soutenue.",
        rat_t: "Ce n'est pas une question de niveau de langue.",
        rat: "«&nbsp;Dont&nbsp;» n'est pas la version chic de «&nbsp;que&nbsp;». Les deux mots "
           + "ne remplacent pas la même chose, et c'est ce que vous allez voir à l'écran "
           + "suivant — sans grammaire." },
    ],
    pourquoi: "«&nbsp;Le logement <b>dont</b> je t'ai parlé&nbsp;». Gardez la phrase telle "
            + "quelle&nbsp;; on va la démonter dans un instant.",
    attente: "Choisissez une réponse pour continuer.",
  },

  // ── 2. On trie AVANT de savoir. Aucun relatif dans le tri. ───────────────
  {
    id:   'le-petit-mot',
    type: 'tri',
    eye:  'À vous de trancher',
    menu: 'Six phrases ordinaires',
    titre: "Six phrases ordinaires. Le mot en gras dit quoi ?",
    consigne: "Aucune grammaire ici, et aucun mot compliqué&nbsp;: dites seulement si le mot "
            + "en gras introduit un <b>lieu</b>, un <b>moment</b>, ou rien de tout ça.",
    colonnes: [
      { id: 'de',  t: 'Ni lieu ni moment', b: 'Ni l’un ni l’autre' },
      { id: 'lieu', t: 'Un endroit',       b: 'Un endroit' },
      { id: 'mom',  t: 'Un moment',        b: 'Un moment' },
    ],
    items: [
      { txt: "J'ai besoin <b>de</b> ce papier.", sous: "de", ok: 'de',
        rat: "Ce papier n'est ni un endroit où l'on va, ni une date. C'est simplement ce dont "
           + "on a besoin&nbsp;: le mot «&nbsp;de&nbsp;» ne situe rien.",
        pourquoi: "« de » : ni lieu ni moment." },
      { txt: "Je travaille <b>dans</b> cet immeuble.", sous: "dans", ok: 'lieu',
        rat: "Un immeuble est un endroit, et «&nbsp;dans&nbsp;» dit qu'on s'y trouve. C'est "
           + "un lieu, même si le mot n'est pas «&nbsp;à&nbsp;».",
        pourquoi: "Un endroit où l'on se trouve." },
      { txt: "Je suis arrivée au Québec <b>cette année-là</b>.", sous: "cette année-là",
        ok: 'mom',
        rat: "«&nbsp;Cette année-là&nbsp;» ne se visite pas&nbsp;: c'est une date, une case du "
           + "calendrier.",
        pourquoi: "Une date : un moment." },
      { txt: "Tu m'as parlé <b>de</b> cette école.", sous: "de", ok: 'de',
        rat: "L'école est bien un endroit, mais ce n'est pas le rôle du mot en gras&nbsp;: "
           + "ici on ne dit pas qu'on <i>y va</i>, on dit qu'on en <b>parle</b>. Regardez le "
           + "petit mot, pas la chose.",
        pourquoi: "On parle DE l'école : ni lieu ni moment." },
      { txt: "On se rencontre <b>à</b> cet endroit.", sous: "à", ok: 'lieu',
        rat: "«&nbsp;À cet endroit&nbsp;» situe la rencontre quelque part. C'est un lieu, au "
           + "sens le plus simple.",
        pourquoi: "Un endroit où l'on se rend." },
      { txt: "Il neigeait <b>ce jour-là</b>.", sous: "ce jour-là", ok: 'mom',
        rat: "Un jour, ça ne se visite pas non plus. Le mot en gras place la phrase sur le "
           + "calendrier.",
        pourquoi: "Un jour : un moment." },
    ],
    attente: "Tranchez les six phrases pour continuer.",
  },

  // ── 3. La règle, comme constat, et le test. ──────────────────────────────
  {
    id:   'recoller',
    type: 'notion',
    eye:  'Ce que vous venez de faire',
    menu: 'Le test',
    titre: "Vos trois piles sont exactement les deux mots de ce point express.",
    paras: [
      "Recollons. «&nbsp;C'est le logement.&nbsp;» + «&nbsp;Je t'ai parlé <b>de</b> ce "
      + "logement.&nbsp;» → «&nbsp;le logement <b>dont</b> je t'ai parlé&nbsp;». "
      + "«&nbsp;C'est l'immeuble.&nbsp;» + «&nbsp;Je travaille <b>dans</b> cet "
      + "immeuble.&nbsp;» → «&nbsp;l'immeuble <b>où</b> je travaille&nbsp;».",

      "Votre pile «&nbsp;ni lieu ni moment&nbsp;» — celle du «&nbsp;de&nbsp;» — donne "
      + "<b>dont</b>. Vos deux autres piles, l'endroit et le moment, donnent toutes les deux "
      + "<b>où</b>. Ces mots s'appellent des <b>pronoms relatifs</b>&nbsp;: ils servent à "
      + "coller deux phrases sans répéter la chose.",

      "<b>Le test, à faire sur n'importe quelle phrase&nbsp;:</b> décollez-la en deux, remettez "
      + "la chose dans la deuxième phrase, et regardez le petit mot qui vient avec elle. "
      + "<i>de</i> → <b>dont</b>. Un endroit ou un moment → <b>où</b>. Rien de tout ça → ce "
      + "sera <i>qui</i> ou <i>que</i>, et ceux-là, vous les placez déjà.",
    ],
    retenir: "Le mot à écrire dépend du <b>petit mot</b> qui accompagnait la chose dans la "
           + "deuxième phrase&nbsp;: <i>de</i> → <b>dont</b>&nbsp;; un lieu ou un moment → "
           + "<b>où</b>.",
    attente: "Lisez, puis continuez.",
  },

  // ── 4. Le piège de celui qui a compris : le « de » écrit deux fois. ──────
  {
    id:   'de-en-double',
    type: 'verif',
    eye:  'Le cas qui trompe',
    menu: 'Le « de » en trop',
    titre: "La faute de celui qui a compris la règle",
    consigne: "Kevin remplit une demande en ligne. Trois versions de la même ligne — une "
            + "seule s'écrit.",
    options: [
      { txt: "«&nbsp;Voici le document dont j'ai besoin pour mon dossier.&nbsp;»", juste: true },
      { txt: "«&nbsp;Voici le document dont j'ai besoin de pour mon dossier.&nbsp;»",
        rat_t: "Le « de » est déjà dans « dont ».",
        rat: "Vous avez fait exactement le bon raisonnement — <i>avoir besoin de</i>, donc "
           + "«&nbsp;dont&nbsp;» — puis vous avez laissé le «&nbsp;de&nbsp;» en place. C'est "
           + "logique et c'est faux&nbsp;: <b>«&nbsp;dont&nbsp;» contient déjà le "
           + "«&nbsp;de&nbsp;»</b>. Il remplace les deux mots à lui seul." },
      { txt: "«&nbsp;Voici le document que j'ai besoin pour mon dossier.&nbsp;»",
        rat_t: "Le « de » a disparu sans être remplacé.",
        rat: "«&nbsp;Que&nbsp;» ne porte aucun «&nbsp;de&nbsp;». La phrase reviendrait à "
           + "«&nbsp;j'ai besoin ce document&nbsp;», qui ne se dit pas. C'est la faute "
           + "inverse de la précédente&nbsp;: on n'écrit pas le «&nbsp;de&nbsp;» deux fois, "
           + "mais il faut l'écrire une fois." },
    ],
    pourquoi: "<b>Une seule fois, et c'est dans le mot.</b> «&nbsp;Dont&nbsp;» = "
            + "«&nbsp;de&nbsp;» + la chose. Si vous voyez «&nbsp;de&nbsp;» écrit ailleurs "
            + "dans la même phrase, l'un des deux est en trop.",
    attente: "Choisissez une réponse pour continuer.",
  },

  // ── 5. « où » sur le calendrier : la faute de celui qui parle bien. ──────
  {
    id:   'le-jour-ou',
    type: 'notion',
    eye:  "L'autre moitié de « où »",
    menu: 'Un jour, une année',
    titre: "« Où » ne parle pas que des endroits, et c'est là qu'on l'oublie.",
    paras: [
      "Tout le monde écrit «&nbsp;la ville <b>où</b> j'habite&nbsp;». Presque personne "
      + "n'écrit «&nbsp;le jour <b>où</b> j'ai commencé&nbsp;» — on écrit «&nbsp;le jour "
      + "<i>que</i> j'ai commencé&nbsp;», parce que c'est ce qu'on entend toute la journée "
      + "autour de soi.",

      "À l'oral, personne ne vous reprendra. Dans un courriel à un employeur ou dans une "
      + "demande écrite, c'est une des rares fautes qui se remarquent d'emblée. Et elle est "
      + "gratuite&nbsp;: le mot juste est plus court à écrire.",

      "<b>Le test tient dans deux mots&nbsp;:</b> si la deuxième phrase dirait «&nbsp;ce "
      + "jour-là&nbsp;», «&nbsp;cette année-là&nbsp;», «&nbsp;ce matin-là&nbsp;», alors "
      + "écrivez <b>où</b>. «&nbsp;Il neigeait <i>ce jour-là</i>&nbsp;» → «&nbsp;le jour "
      + "<b>où</b> il neigeait&nbsp;».",
    ],
    retenir: "<b>où</b> vaut pour la carte <b>et</b> pour le calendrier&nbsp;: le quartier "
           + "où je vis, l'année où je suis arrivée, le moment où ça s'est passé.",
    attente: "Lisez, puis continuez.",
  },

  // ── 6. Trier des phrases écrites, avec le test en main. ──────────────────
  {
    id:   'tri-correct',
    type: 'tri',
    eye:  'À vous de trancher',
    menu: 'Six phrases',
    titre: "Six phrases prises dans de vrais messages. Lesquelles sont correctes ?",
    consigne: "Décollez chacune en deux dans votre tête, puis regardez le petit mot qui "
            + "revient avec la chose.",
    colonnes: [
      { id: 'ok',   t: 'Correct',   b: 'Correct' },
      { id: 'faux', t: 'Une faute', b: 'Une faute' },
    ],
    items: [
      { txt: "«&nbsp;Le poste dont vous m'avez parlé m'intéresse beaucoup.&nbsp;»",
        sous: "courriel de candidature", ok: 'ok',
        rat: "«&nbsp;Vous m'avez parlé <b>de</b> ce poste&nbsp;»&nbsp;: le "
           + "«&nbsp;de&nbsp;» est là, il devient «&nbsp;dont&nbsp;», et il n'est pas répété.",
        pourquoi: "parler DE : dont. Juste." },
      { txt: "«&nbsp;Voici la semaine que je serai absente.&nbsp;»", sous: "note à l'école",
        ok: 'faux',
        rat: "Une semaine, c'est une case du calendrier&nbsp;: «&nbsp;je serai absente "
           + "<i>cette semaine-là</i>&nbsp;». Il faut donc «&nbsp;la semaine <b>où</b> je "
           + "serai absente&nbsp;». C'est la faute qu'on entend partout à l'oral.",
        pourquoi: "Un moment : la semaine où je serai absente." },
      { txt: "«&nbsp;L'appartement où j'habite depuis deux ans est au troisième.&nbsp;»",
        sous: "message au propriétaire", ok: 'ok',
        rat: "«&nbsp;J'habite <b>dans</b> cet appartement&nbsp;»&nbsp;: un endroit, donc "
           + "«&nbsp;où&nbsp;». Le cas le plus facile des deux, et il est bien traité ici.",
        pourquoi: "Un endroit : où. Juste." },
      { txt: "«&nbsp;C'est un outil dont je me sers de tous les jours.&nbsp;»",
        sous: "annonce de revente", ok: 'faux',
        rat: "Le raisonnement était juste — <i>se servir de</i> — mais le "
           + "«&nbsp;de&nbsp;» a été écrit deux fois. «&nbsp;Dont&nbsp;» le porte déjà&nbsp;: "
           + "«&nbsp;dont je me sers tous les jours&nbsp;».",
        pourquoi: "Un « de » en trop : dont je me sers." },
      { txt: "«&nbsp;Le matin où je suis passée, la porte était barrée.&nbsp;»",
        sous: "texto à une amie", ok: 'ok',
        rat: "«&nbsp;Je suis passée <i>ce matin-là</i>&nbsp;»&nbsp;: un moment, donc "
           + "«&nbsp;où&nbsp;». Exactement l'emploi que presque tout le monde évite.",
        pourquoi: "Un moment : le matin où. Juste." },
      { txt: "«&nbsp;Le voisin où le chien aboie la nuit a déménagé.&nbsp;»",
        sous: "message au concierge", ok: 'faux',
        rat: "Un voisin n'est ni un endroit ni un moment&nbsp;: on ne va pas «&nbsp;dans le "
           + "voisin&nbsp;». Le chien est celui <b>du</b> voisin&nbsp;: un «&nbsp;de&nbsp;» "
           + "caché, donc «&nbsp;le voisin <b>dont</b> le chien aboie&nbsp;».",
        pourquoi: "Le chien DU voisin : dont." },
    ],
    attente: "Tranchez les six phrases pour continuer.",
  },

  // ── 7. Le « de » qui ne se voit pas : le complément du nom. ──────────────
  {
    id:   'de-cache',
    type: 'notion',
    eye:  'Le cas fréquent',
    menu: 'Le « de » caché',
    titre: "Parfois le « de » n'est pas devant un verbe, il est devant un nom.",
    paras: [
      "Jusqu'ici, le «&nbsp;de&nbsp;» venait d'un verbe&nbsp;: parler <i>de</i>, avoir "
      + "besoin <i>de</i>, se servir <i>de</i>, être content <i>de</i>. Il existe un second "
      + "endroit où il se cache, et c'est celui qu'on manque&nbsp;: entre deux noms.",

      "«&nbsp;Le chien <b>de</b> la voisine&nbsp;», «&nbsp;le prix <b>de</b> l'appareil&nbsp;», "
      + "«&nbsp;le nom <b>du</b> propriétaire&nbsp;». Le test ne change pas — on cherche le "
      + "«&nbsp;de&nbsp;», il est là — et le résultat non plus&nbsp;: la voisine "
      + "<b>dont</b> le chien aboie, l'appareil <b>dont</b> le prix a monté, le propriétaire "
      + "<b>dont</b> le nom est sur le bail.",

      "Notez l'ordre&nbsp;: après <i>dont</i>, on met la chose possédée avec <b>son</b> "
      + "article, jamais «&nbsp;son&nbsp;» ou «&nbsp;sa&nbsp;». On écrit «&nbsp;la voisine "
      + "dont <b>le</b> chien aboie&nbsp;», pas «&nbsp;dont son chien&nbsp;».",
    ],
    retenir: "Le «&nbsp;de&nbsp;» peut venir d'un verbe <b>ou</b> relier deux noms. Dans les "
           + "deux cas, même mot&nbsp;: <b>dont</b>.",
    attente: "Lisez, puis continuez.",
  },

  // ── 8. Une vraie production, une seule ligne fautive. ────────────────────
  {
    id:   'annonce',
    type: 'verif',
    eye:  'Vérification',
    menu: 'Une annonce à corriger',
    titre: "Sandra met un meuble en vente en ligne. Une seule ligne est fautive.",
    consigne: "«&nbsp;<i>Je vends la table dont je vous ai parlé la semaine passée. C'est le "
            + "modèle que j'ai acheté en 2022. Je serai à la maison le samedi que vous "
            + "voudrez venir la voir.</i>&nbsp;»",
    options: [
      { txt: "«&nbsp;Le samedi que vous voudrez venir la voir.&nbsp;»", juste: true },
      { txt: "«&nbsp;La table dont je vous ai parlé la semaine passée.&nbsp;»",
        rat_t: "Celle-là est juste.",
        rat: "«&nbsp;Je vous ai parlé <b>de</b> cette table&nbsp;»&nbsp;: le "
           + "«&nbsp;de&nbsp;» donne «&nbsp;dont&nbsp;», et il n'est pas répété derrière. "
           + "Rien à corriger." },
      { txt: "«&nbsp;Le modèle que j'ai acheté en 2022.&nbsp;»",
        rat_t: "Celle-là est juste aussi.",
        rat: "«&nbsp;J'ai acheté <i>ce modèle</i>&nbsp;»&nbsp;: pas de «&nbsp;de&nbsp;», pas "
           + "de lieu, pas de moment — c'est bien «&nbsp;que&nbsp;». Le test sert aussi à "
           + "confirmer qu'on ne doit <b>rien</b> changer." },
    ],
    pourquoi: "«&nbsp;Le samedi <b>où</b> vous voudrez venir&nbsp;». Un samedi est une case du "
            + "calendrier. Deux lignes sur trois étaient bonnes&nbsp;: c'est toujours celle "
            + "du calendrier qui tombe, parce qu'elle sonne juste à l'oreille.",
    attente: "Choisissez une réponse pour continuer.",
  },

  // ── 9. Une phrase à composer entièrement. ───────────────────────────────
  {
    id:   'a-composer',
    type: 'verif',
    eye:  'Vérification',
    menu: 'Deux relatifs de suite',
    titre: "Deux phrases à coller en une. Laquelle tient d'un bout à l'autre ?",
    consigne: "«&nbsp;Je cherche un logement.&nbsp;» + «&nbsp;Le prix <b>du</b> logement est "
            + "sous 1&nbsp;200&nbsp;$.&nbsp;» + «&nbsp;Je pourrais emménager <b>en "
            + "juillet</b>.&nbsp;»",
    options: [
      { txt: "«&nbsp;Je cherche un logement dont le prix est sous 1&nbsp;200&nbsp;$ et où je "
           + "pourrais emménager en juillet.&nbsp;»", juste: true },
      { txt: "«&nbsp;Je cherche un logement dont le prix est sous 1&nbsp;200&nbsp;$ et que je "
           + "pourrais emménager en juillet.&nbsp;»",
        rat_t: "Le premier est bon. Le second a été mis par défaut.",
        rat: "«&nbsp;Dont le prix&nbsp;» est parfaitement construit&nbsp;: le "
           + "«&nbsp;de&nbsp;» entre deux noms a été vu. Mais «&nbsp;emménager dans ce "
           + "logement&nbsp;», c'est un endroit — donc «&nbsp;<b>où</b> je pourrais "
           + "emménager&nbsp;». «&nbsp;Que&nbsp;» est le mot qu'on écrit quand on cesse de "
           + "faire le test." },
      { txt: "«&nbsp;Je cherche un logement où le prix est sous 1&nbsp;200&nbsp;$ et dont je "
           + "pourrais emménager en juillet.&nbsp;»",
        rat_t: "Les deux mots sont bons, mais intervertis.",
        rat: "Vous avez trouvé les deux relatifs de la phrase&nbsp;: c'est déjà le plus "
           + "difficile. Reprenez le test dans l'ordre&nbsp;: le prix <b>du</b> logement → "
           + "<i>dont</i>&nbsp;; emménager <b>dans</b> le logement → <i>où</i>. Le petit mot "
           + "décide, pas la place dans la phrase." },
    ],
    pourquoi: "Un «&nbsp;de&nbsp;» caché entre deux noms, puis un endroit&nbsp;: "
            + "<b>dont</b>, puis <b>où</b>. Une phrase de cette longueur, tenue sans "
            + "répéter «&nbsp;le logement&nbsp;», c'est exactement ce que le niveau 5 attend "
            + "de vous à l'écrit.",
    attente: "Choisissez une réponse pour continuer.",
  },

  // ── 10. La fermeture : le cas de l'écran 1. ──────────────────────────────
  {
    id:   'fermeture',
    type: 'verif',
    eye:  'La dernière',
    menu: 'Pour finir',
    titre: "On revient à la phrase du début, avec un mot de plus.",
    consigne: "Vous écrivez à un ami au sujet du logement de l'écran 1, et vous ajoutez la "
            + "date de la visite. Quelle version&nbsp;?",
    options: [
      { txt: "«&nbsp;C'est le logement dont je t'ai parlé, et samedi est le jour où je le "
           + "visite.&nbsp;»", juste: true },
      { txt: "«&nbsp;C'est le logement que je t'ai parlé, et samedi est le jour où je le "
           + "visite.&nbsp;»",
        rat_t: "C'est la phrase de l'écran 1, restée telle quelle.",
        rat: "Le calendrier est réglé — «&nbsp;le jour <b>où</b>&nbsp;», bien vu. Mais "
           + "«&nbsp;parler <b>de</b> quelque chose&nbsp;» n'a pas bougé&nbsp;: il faut "
           + "«&nbsp;<b>dont</b> je t'ai parlé&nbsp;». C'est le mot que ce point express "
           + "vous demandait d'aller chercher." },
      { txt: "«&nbsp;C'est le logement dont je t'ai parlé, et samedi est le jour que je le "
           + "visite.&nbsp;»",
        rat_t: "Vous avez le plus difficile. C'est le calendrier qui a lâché.",
        rat: "«&nbsp;Dont je t'ai parlé&nbsp;»&nbsp;: exact, et c'est celui des deux que la "
           + "plupart des gens évitent toute leur vie. Reste le samedi&nbsp;: "
           + "«&nbsp;je le visite <i>ce jour-là</i>&nbsp;» → «&nbsp;le jour <b>où</b>&nbsp;». "
           + "Elle revient toujours en dernier, parce qu'elle sonne juste." },
    ],
    pourquoi: "«&nbsp;Le logement <b>dont</b> je t'ai parlé&nbsp;», «&nbsp;le jour "
            + "<b>où</b> je le visite&nbsp;». Deux mots, un seul geste&nbsp;: décoller la "
            + "phrase en deux et regarder le petit mot. <b>Emportez le geste, pas la "
            + "liste.</b>",
    attente: "Choisissez une réponse pour finir.",
  },

];
