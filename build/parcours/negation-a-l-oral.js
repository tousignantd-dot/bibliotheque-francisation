// ═══════════════════════════════════════════════════════════════════════════
// Point express — Dire non : ce qui s'entend, ce qui s'écrit
//
// Savoir n1-s05 (phrases négatives). Dix minutes, dix écrans. Une ORDONNANCE :
// l'enseignant l'envoie à l'élève qui répond « oui » à une phrase négative, ou
// qui écrit « je viens pas » dans un message à l'école.
//
// Le point tient sur DEUX SENS DE CIRCULATION, et c'est sa raison d'être :
//   · on ENTEND une négation qui n'a pas de « ne » — « je travaille pas » ;
//   · on ÉCRIT une négation qui en a un — « je ne travaille pas ».
// Un élève qui n'a appris que le second sens rate la moitié de ce qu'on lui
// dit au comptoir ; un élève qui n'a appris que le premier écrit comme on parle.
//
// ── Ce qui le sépare de la mini-leçon existante ────────────────────────────
// `module-n2-secretaire`, « Dire non : "ne … pas" » — la seule mini-leçon du
// dépôt qui enseigne la négation de front. Elle donne la règle du sandwich
// (« ne » devant, « pas » derrière), puis l'élision « n' », puis « un/du → de »,
// puis un labo à douze phrases dont une colonne « à l'oral rapide ». L'élève
// envoyé ici l'a probablement lue. Les cinq écarts tenus :
//
//   1. INDUCTIF. Aucune règle avant l'écran 3. L'élève tranche six phrases
//      entendues — sens : oui ou non ? — sans qu'on lui ait rien dit. La règle
//      de l'écran 3 est écrite comme un constat de ce qu'il vient de faire.
//   2. PARTIEL, ET UN AUTRE TEST. La mini-leçon apprend le sandwich complet.
//      Ici : UN SEUL MOT à surveiller — « pas ». C'est le seul des deux qui ne
//      tombe jamais, ni à l'oral ni à l'écrit ; le « ne », lui, disparaît dans
//      la moitié de ce que l'élève entend. Un test qui marche sur une phrase
//      jamais vue vaut mieux qu'une règle qui suppose un mot souvent absent.
//   3. LE « NE » EST DIT EN DERNIER (écrans 5 et 6). La mini-leçon ouvre
//      dessus. Or c'est la moitié qui ne sert qu'à l'écrit : la nommer trop tôt
//      fait chercher à l'oreille un mot qui n'y est pas.
//   4. LE MÉTALANGAGE APRÈS. « Phrase négative » n'est écrit qu'à l'écran 3,
//      une fois six phrases triées. Aucun autre mot savant du début à la fin.
//   5. EXEMPLES VARIÉS, JAMAIS CEUX D'UN MODULE. Un mot à l'école, un message
//      à un employeur, un texto, une phrase au comptoir. Aucune phrase n'est
//      reprise de la mini-leçon, et le point ne dépend d'aucun scénario.
//
// Aucun média. La faute se juge sur des chaînes écrites : ce point doit tourner
// dans un centre en mode sans assistance. Les phrases « entendues » sont donc
// écrites telles qu'on les dit — c'est exactement ce que l'élève doit
// apprendre à reconnaître.
// ═══════════════════════════════════════════════════════════════════════════

const PARCOURS = {
  slug:     'negation-a-l-oral',
  titre:    "Dire non : ce qui s'entend, ce qui s'écrit",
  surtitre: "Point express · 10 minutes",
  niveau:   1,
  savoir:   'n1-s05',
};

const ECRANS = [

  // ── 1. Une décision, sans aucune règle donnée. ───────────────────────────
  {
    id:   'depart',
    type: 'verif',
    eye:  'Une question, pour commencer',
    menu: 'Samedi',
    titre: "Une collègue vous dit : « Moi, je travaille pas samedi. »",
    consigne: "Est-ce qu'elle travaille samedi&nbsp;? Répondez avec ce que vous savez "
            + "déjà — c'est fait exprès.",
    options: [
      { txt: "Non. Elle ne travaille pas samedi.", juste: true },
      { txt: "Oui. Elle travaille samedi.",
        rat_t: "Il manque un petit mot, et vous l'avez cherché.",
        rat: "Vous cherchez le mot «&nbsp;ne&nbsp;». Il n'est pas là. C'est normal&nbsp;: "
           + "ici, personne ne le dit. Mais la phrase dit bien <b>non</b>. Regardez le "
           + "mot juste après le verbe." },
      { txt: "On ne peut pas savoir.",
        rat_t: "On peut savoir. Un seul mot suffit.",
        rat: "Il y a un mot dans cette phrase qui dit non, et il est très court. "
           + "Il est après «&nbsp;travaille&nbsp;». Relisez la phrase." },
    ],
    pourquoi: "Elle ne travaille <b>pas</b> samedi. Le mot qui dit non, c'est "
            + "«&nbsp;pas&nbsp;». Gardez-le en tête&nbsp;: tout le point est là.",
    attente: "Choisissez une réponse pour continuer.",
  },

  // ── 2. On trie AVANT de savoir. ──────────────────────────────────────────
  {
    id:   'tri-oui-non',
    type: 'tri',
    eye:  'À vous de trancher',
    menu: 'Six phrases',
    titre: "Six phrases comme on les dit ici. Oui ou non ?",
    consigne: "Aucune règle ne vous a été donnée — normal. Lisez chaque phrase "
            + "à voix basse et demandez-vous seulement&nbsp;: la personne dit oui, "
            + "ou elle dit non&nbsp;?",
    colonnes: [
      { id: 'oui', t: 'Elle dit oui', b: 'Oui' },
      { id: 'non', t: 'Elle dit non', b: 'Non' },
    ],
    items: [
      { txt: "J'ai pas de crayon.", sous: "en classe", ok: 'non',
        rat: "Le mot «&nbsp;pas&nbsp;» est là, juste après «&nbsp;ai&nbsp;». "
           + "La personne n'a rien pour écrire.",
        pourquoi: "« pas » après le verbe : elle dit non." },
      { txt: "Je comprends.", sous: "au comptoir", ok: 'oui',
        rat: "Il n'y a pas de «&nbsp;pas&nbsp;» dans cette phrase. Elle dit oui.",
        pourquoi: "Aucun « pas » : elle dit oui." },
      { txt: "Elle vient pas aujourd'hui.", sous: "un message à l'école", ok: 'non',
        rat: "«&nbsp;pas&nbsp;» est après «&nbsp;vient&nbsp;». La personne ne vient "
           + "pas. Le mot «&nbsp;ne&nbsp;» n'est pas écrit, mais la phrase dit non.",
        pourquoi: "« pas » après le verbe : elle dit non." },
      { txt: "Je ne comprends pas.", sous: "au comptoir", ok: 'non',
        rat: "Ici, il y a deux mots&nbsp;: «&nbsp;ne&nbsp;» et «&nbsp;pas&nbsp;». "
           + "C'est la même chose que la phrase du haut, écrite en entier.",
        pourquoi: "« ne » et « pas » : elle dit non." },
      { txt: "Y a pas de cours lundi.", sous: "au téléphone", ok: 'non',
        rat: "Le début est mangé — on dit «&nbsp;y a&nbsp;» pour «&nbsp;il y a&nbsp;». "
           + "Mais «&nbsp;pas&nbsp;» est là, et c'est lui qui compte.",
        pourquoi: "« pas » est là : il n'y a pas de cours." },
      { txt: "Le bureau est ouvert.", sous: "sur la porte", ok: 'oui',
        rat: "Aucun «&nbsp;pas&nbsp;» dans cette phrase. Le bureau est ouvert.",
        pourquoi: "Aucun « pas » : la phrase dit oui." },
    ],
    attente: "Tranchez les six phrases pour continuer.",
  },

  // ── 3. La règle, écrite comme un constat. Le métalangage arrive ici. ─────
  {
    id:   'le-mot-pas',
    type: 'notion',
    eye:  'Ce que vous venez de faire',
    menu: 'Le mot « pas »',
    titre: "Vous avez cherché un seul mot : « pas ».",
    paras: [
      "Regardez votre colonne «&nbsp;elle dit non&nbsp;». Dans les quatre phrases, "
      + "il y a le mot <b>pas</b>, et il est toujours <b>après le verbe</b>. "
      + "Dans les deux autres, il n'y est pas. Vous n'avez pas eu besoin d'autre chose.",

      "Une phrase qui dit non s'appelle une <b>phrase négative</b>. Vous n'avez pas "
      + "besoin du nom pour vous en servir, mais votre enseignant l'emploiera.",

      "<b>Le test, à vous poser sur toutes les phrases que vous entendez&nbsp;:</b> "
      + "est-ce qu'il y a le mot <i>pas</i> après le verbe&nbsp;? Si oui, la personne "
      + "dit non.",
    ],
    retenir: "<b>« pas » ne tombe jamais.</b> C'est le seul mot sur lequel vous "
           + "pouvez compter&nbsp;: écoutez-le, et vous savez si c'est oui ou non.",
    attente: "Lisez, puis continuez.",
  },

  // ── 4. L'autre sens de circulation. On écrit, maintenant. ────────────────
  {
    id:   'vous-ecrivez',
    type: 'verif',
    eye:  "Maintenant, vous écrivez",
    menu: 'Un mot à l’école',
    titre: "Vous écrivez à l'école. Votre fille est malade.",
    consigne: "Vous voulez dire qu'elle ne vient pas demain. Quelle ligne écrivez-vous&nbsp;?",
    options: [
      { txt: "Ma fille ne vient pas demain.", juste: true },
      { txt: "Ma fille vient pas demain.",
        rat_t: "C'est ce qu'on dit. Ce n'est pas ce qu'on écrit.",
        rat: "Cette phrase est juste à l'oral, et tout le monde la dit. Mais quand on "
           + "<b>écrit</b> à l'école, on remet le petit mot devant le verbe&nbsp;: "
           + "«&nbsp;ne vient pas&nbsp;». C'est la moitié qu'on n'entend jamais." },
      { txt: "Ma fille ne vient demain.",
        rat_t: "Vous avez gardé le mot qui tombe et perdu celui qui reste.",
        rat: "«&nbsp;ne&nbsp;» tout seul ne dit rien. C'est «&nbsp;pas&nbsp;» qui dit "
           + "non — c'est le mot que vous avez cherché dans les six phrases. "
           + "Il ne se retire jamais." },
    ],
    pourquoi: "«&nbsp;Ma fille <b>ne</b> vient <b>pas</b> demain.&nbsp;» Deux mots à "
            + "l'écrit&nbsp;: un devant le verbe, un derrière.",
    attente: "Choisissez une réponse pour continuer.",
  },

  // ── 5. Le « ne », dit en dernier : c'est la moitié réservée à l'écrit. ───
  {
    id:   'le-ne-decrit',
    type: 'notion',
    eye:  'Ce qui reste',
    menu: 'Le mot « ne »',
    titre: "« ne » est un mot d'écriture. On ne l'entend presque jamais.",
    paras: [
      "On a gardé celui-ci pour la fin, et c'est voulu. Le mot <b>ne</b> se place "
      + "<b>devant le verbe</b>&nbsp;: je <b>ne</b> travaille <b>pas</b>. À l'écrit, "
      + "on l'écrit toujours. À l'oral, ici, presque personne ne le dit.",

      "Devant <i>a, e, i, o, u</i> et devant <i>h</i>, «&nbsp;ne&nbsp;» devient "
      + "<b>n'</b>&nbsp;: je <b>n'</b>ai pas de crayon, ce <b>n'</b>est pas grave, "
      + "il <b>n'</b>y a pas de cours.",

      "Alors vous avez <b>deux choses</b> à faire, et elles vont dans deux sens. "
      + "Quand vous <b>écoutez</b>&nbsp;: cherchez «&nbsp;pas&nbsp;». Quand vous "
      + "<b>écrivez</b>&nbsp;: ajoutez «&nbsp;ne&nbsp;» devant le verbe.",
    ],
    retenir: "J'écoute → je cherche <b>pas</b>. J'écris → j'ajoute <b>ne</b>.",
    attente: "Lisez, puis continuez.",
  },

  // ── 6. Trois colonnes : le cœur des deux sens de circulation. ────────────
  {
    id:   'tri-dit-ecrit',
    type: 'tri',
    eye:  'À vous de trancher',
    menu: 'Six façons',
    titre: "Six phrases. Laquelle s'écrit, laquelle se dit seulement ?",
    consigne: "Trois colonnes. «&nbsp;Ça s'écrit&nbsp;» pour un message à l'école ou "
            + "au patron. «&nbsp;Ça se dit&nbsp;» pour une phrase correcte à l'oral, "
            + "mais qu'on n'écrit pas. «&nbsp;Ça ne se dit pas&nbsp;» pour une phrase "
            + "qu'on ne dira nulle part.",
    colonnes: [
      { id: 'ecrit', t: "Ça s'écrit",       b: "Ça s'écrit" },
      { id: 'dit',   t: 'Ça se dit',        b: 'Ça se dit' },
      { id: 'non',   t: 'Ça ne se dit pas', b: 'Jamais' },
    ],
    items: [
      { txt: "Je ne peux pas venir lundi.", sous: "message au patron", ok: 'ecrit',
        rat: "Les deux mots sont là, chacun à sa place&nbsp;: «&nbsp;ne&nbsp;» devant "
           + "«&nbsp;peux&nbsp;», «&nbsp;pas&nbsp;» derrière. C'est la phrase à écrire.",
        pourquoi: "« ne » devant, « pas » derrière : c'est la forme écrite." },
      { txt: "Je peux pas venir lundi.", sous: "à un ami, au téléphone", ok: 'dit',
        rat: "Cette phrase est bonne, et vous l'entendrez tous les jours. Mais il lui "
           + "manque le «&nbsp;ne&nbsp;»&nbsp;: on ne l'écrit pas dans un message au patron.",
        pourquoi: "Correcte à l'oral. Il manque « ne » pour l'écrire." },
      { txt: "Je ne peux venir lundi.", sous: "—", ok: 'non',
        rat: "Le mot qui dit non a disparu. Sans «&nbsp;pas&nbsp;», la personne qui vous "
           + "lit ne sait plus si vous venez ou non.",
        pourquoi: "Sans « pas », la phrase ne dit plus non." },
      { txt: "Je n'ai pas compris.", sous: "en classe", ok: 'ecrit',
        rat: "«&nbsp;ne&nbsp;» est devenu «&nbsp;n'&nbsp;» parce que «&nbsp;ai&nbsp;» "
           + "commence par une voyelle. C'est bien la forme écrite.",
        pourquoi: "n' + ai : la forme écrite, avec l'apostrophe." },
      { txt: "J'ai pas compris.", sous: "en classe, à voix basse", ok: 'dit',
        rat: "C'est la même phrase, sans le «&nbsp;n'&nbsp;». Tout le monde la dit. "
           + "Dans un devoir, on écrit «&nbsp;je n'ai pas compris&nbsp;».",
        pourquoi: "Ce qu'on dit. À l'écrit : « je n'ai pas compris »." },
      { txt: "Je pas travaille demain.", sous: "—", ok: 'non',
        rat: "«&nbsp;pas&nbsp;» est passé devant le verbe. Il va toujours <b>après</b>&nbsp;: "
           + "«&nbsp;je travaille pas&nbsp;» à l'oral, «&nbsp;je ne travaille pas&nbsp;» "
           + "à l'écrit. C'est une faute très fréquente&nbsp;: beaucoup de langues placent "
           + "le mot de la négation devant le verbe.",
        pourquoi: "« pas » se place après le verbe, jamais devant." },
    ],
    attente: "Tranchez les six phrases pour continuer.",
  },

  // ── 7. Le cas fréquent : l'élision, dans un vrai message. ────────────────
  {
    id:   'napostrophe',
    type: 'verif',
    eye:  'Vérification',
    menu: 'Le message au patron',
    titre: "Vous écrivez à votre patron. Vous n'avez pas encore votre horaire.",
    consigne: "Une seule de ces trois lignes s'écrit.",
    options: [
      { txt: "Je n'ai pas mon horaire.", juste: true },
      { txt: "Je ne ai pas mon horaire.",
        rat_t: "Les deux mots sont bons. C'est la rencontre qui ne va pas.",
        rat: "«&nbsp;ne&nbsp;» et «&nbsp;ai&nbsp;» ne se touchent jamais&nbsp;: le "
           + "«&nbsp;e&nbsp;» tombe et on met une apostrophe. On écrit "
           + "«&nbsp;je <b>n'ai</b> pas&nbsp;». Toujours, devant a, e, i, o, u et h." },
      { txt: "J'ai pas mon horaire.",
        rat_t: "C'est ce que vous direz. Pas ce que vous écrirez à votre patron.",
        rat: "La phrase est correcte à l'oral. Dans un message au travail, on remet "
           + "le petit mot&nbsp;: «&nbsp;je <b>n'</b>ai pas&nbsp;». C'est la même "
           + "phrase, écrite en entier." },
    ],
    pourquoi: "«&nbsp;Je <b>n'</b>ai pas mon horaire.&nbsp;» Devant une voyelle, "
            + "«&nbsp;ne&nbsp;» perd son <i>e</i> et prend une apostrophe.",
    attente: "Choisissez une réponse pour continuer.",
  },

  // ── 8. Ce qu'on entend vraiment. Le test tient quand même. ───────────────
  {
    id:   'ce-quon-entend',
    type: 'notion',
    eye:  'Au comptoir, dans la rue',
    menu: 'Ce qu’on entend',
    titre: "Le début des phrases est souvent mangé. « pas » reste toujours.",
    paras: [
      "Ici, on parle vite et on coupe le début&nbsp;: «&nbsp;<b>y a pas</b> de "
      + "place&nbsp;» pour «&nbsp;il n'y a pas de place&nbsp;». "
      + "«&nbsp;<b>c'est pas</b> grave&nbsp;» pour «&nbsp;ce n'est pas grave&nbsp;». "
      + "«&nbsp;<b>j'peux pas</b>&nbsp;» pour «&nbsp;je ne peux pas&nbsp;».",

      "Ce sont les trois phrases négatives que vous entendrez le plus souvent. "
      + "Regardez ce qui a disparu, et ce qui est resté&nbsp;: le début change, "
      + "«&nbsp;pas&nbsp;» ne bouge pas.",

      "C'est pour ça que votre test tient. Vous n'avez pas besoin de comprendre "
      + "tous les mots d'une phrase rapide&nbsp;: vous avez besoin d'entendre "
      + "<b>un seul</b>.",
    ],
    retenir: "Le début se mange, la fin reste. <b>Écoutez après le verbe.</b>",
    attente: "Lisez, puis continuez.",
  },

  // ── 9. Écrire une phrase entière, pas reconnaître un mot. ────────────────
  {
    id:   'le-texto',
    type: 'verif',
    eye: 'Vérification',
    menu: 'Trois messages',
    titre: "Trois messages écrits à l'école. Un seul est correct d'un bout à l'autre.",
    consigne: "Chaque message dit deux choses&nbsp;: mon fils est malade, et je ne "
            + "peux pas venir le chercher.",
    options: [
      { txt: "« Mon fils est malade. Je ne peux pas venir le chercher. »", juste: true },
      { txt: "« Mon fils est malade. Je peux pas venir le chercher. »",
        rat_t: "La phrase est bonne. Il manque le mot d'écriture.",
        rat: "«&nbsp;pas&nbsp;» est là, et c'est l'essentiel&nbsp;: on comprend que "
           + "vous ne venez pas. Mais à l'école on écrit «&nbsp;je <b>ne</b> peux "
           + "pas&nbsp;». C'est le seul mot qui manque." },
      { txt: "« Mon fils est malade. Je ne peux venir le chercher. »",
        rat_t: "Le mot qui dit non est parti.",
        rat: "Vous avez mis «&nbsp;ne&nbsp;» et retiré «&nbsp;pas&nbsp;». C'est "
           + "l'inverse de ce qu'il faut&nbsp;: «&nbsp;pas&nbsp;» est celui qui reste "
           + "toujours. Sans lui, l'école lit que vous venez." },
    ],
    pourquoi: "«&nbsp;Je <b>ne</b> peux <b>pas</b> venir.&nbsp;» Les deux mots, "
            + "chacun de son côté du verbe. <b>C'est tout le point en une phrase.</b>",
    attente: "Choisissez une réponse pour continuer.",
  },

  // ── 10. La fermeture : la phrase de l'écran 1, dans l'autre sens. ────────
  {
    id:   'fermeture',
    type: 'verif',
    eye:  'La dernière',
    menu: 'Pour finir',
    titre: "On revient à samedi. Cette fois, c'est vous qui écrivez.",
    consigne: "Vous écrivez à votre patron pour dire que vous ne travaillez pas "
            + "samedi. Quelle ligne écrivez-vous&nbsp;?",
    options: [
      { txt: "« Je ne travaille pas samedi. »", juste: true },
      { txt: "« Je travaille pas samedi. »",
        rat_t: "C'est la phrase de l'écran 1 — celle qu'on entend.",
        rat: "Votre collègue vous l'a dite comme ça, et c'était correct&nbsp;: à l'oral, "
           + "le «&nbsp;ne&nbsp;» tombe. Mais vous <b>écrivez</b> maintenant, et à votre "
           + "patron. Remettez-le devant le verbe." },
      { txt: "« Je ne travaille samedi. »",
        rat_t: "Vous avez retiré le seul mot qui ne se retire jamais.",
        rat: "Sans «&nbsp;pas&nbsp;», votre patron lit que vous travaillez samedi — et "
           + "il vous attend. C'est le mot que vous avez cherché dans les six phrases "
           + "du début&nbsp;: il ne part jamais." },
    ],
    pourquoi: "«&nbsp;Je <b>ne</b> travaille <b>pas</b> samedi.&nbsp;» Vous savez "
            + "maintenant faire les deux sens&nbsp;: entendre le non sans "
            + "«&nbsp;ne&nbsp;», et l'écrire avec.",
    attente: "Choisissez une réponse pour finir.",
  },

];
