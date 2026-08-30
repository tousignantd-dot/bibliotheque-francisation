// ═══════════════════════════════════════════════════════════════════════════
// Point express — Comparer : plus, moins, aussi… que
//
// Savoir n4-s38. Une ORDONNANCE : l'enseignant l'envoie à un élève qui a écrit
// « plus cher de », dit « plus bon », ou qui n'a pas su répondre devant deux
// logements. Dix minutes, dix écrans, une seule difficulté.
//
// ── Ce dont il s'écarte, et comment ────────────────────────────────────────
// Six mini-leçons du dépôt comparent déjà :
//   · `module-n3-vetements` — « Plus cher, moins cher, aussi cher » : les trois
//     moules, puis les deux irréguliers, puis trois pièges. C'est la leçon la
//     plus proche, et c'est celle dont il faut le plus s'écarter.
//   · `module-n5-quebec` — « Comparer, puis choisir » : ajoute « plus de » +
//     nom et le superlatif.
//   · `module-n3-metro`, `module-n7-banque`, `module-n7-publicite`,
//     `module-n7-recherche` — comparer des prix, des forfaits, des chiffres.
//
// Les cinq écarts tenus :
//   1. INDUCTIF, ET SUR LE DÉCODAGE. Les mini-leçons apprennent à PRODUIRE une
//      comparaison. Ce point express commence par la COMPRENDRE : l'écran 3
//      fait dire, six fois, lequel des deux est le moins cher. C'est ce que
//      l'élève rate devant un comptoir, pas la construction de la phrase.
//   2. PARTIEL. Ni superlatif, ni « autant de », ni « pire ». Trois degrés, un
//      « que », deux irréguliers. Rien d'autre.
//   3. LE « QUE » EST TRAITÉ COMME UNE FLÈCHE, pas comme une obligation
//      grammaticale : ce qui vient après lui est le point de comparaison. C'est
//      ce qui permet de répondre vite, et aucune mini-leçon ne le dit ainsi.
//   4. AUCUNE PHRASE REPRISE, et des exemples pris à plusieurs endroits : deux
//      logements, deux forfaits de téléphone, deux manteaux, un dépanneur.
//   5. UN PIÈGE D'ÉCOUTE QUE PERSONNE NE TRAITE (écran 8) : « moins trente »
//      n'est pas une comparaison. « Moins » suivi d'un nombre est une
//      température, et l'élève de niveau 4 l'entend tous les hivers.
//
// Extraits : ceux de `module-vetements` (niveau 4), rejoués par chemin. Aucun
// média neuf. Les rangs sont ceux de `dialogues.js` et les textes en sont
// recopiés. Attention : le module s'appelle `module-vetements`, pas
// `module-n3-vetements`, qui est un autre module et un autre niveau.
// ═══════════════════════════════════════════════════════════════════════════

const PARCOURS = {
  slug:     'comparer',
  module:   'module-vetements',   // d'où viennent les extraits, rien de plus
  titre:    "Comparer : plus, moins, aussi… que",
  surtitre: "Point express · 10 minutes",
  niveau:   4,
  savoir:   'n4-s38',
};

const ECRANS = [

  // ── 1. On décide vite, sans qu'aucune règle ait été dite. ────────────────
  {
    id:   'depart',
    type: 'verif',
    eye:  'Une question, pour commencer',
    menu: 'Deux logements',
    titre: "« Le quatre et demi de la rue Fabre est moins cher que celui de la rue Marquette. »",
    consigne: "Répondez tout de suite, sans relire trois fois — c'est exactement le temps que vous "
            + "aurez au téléphone. On expliquera après&nbsp;: c'est fait exprès.",
    options: [
      { txt: "Celui de la rue Fabre coûte moins cher.", juste: true },
      { txt: "Celui de la rue Marquette coûte moins cher.",
        rat_t: "Vous avez retenu le dernier nom entendu.",
        rat: "C'est l'erreur normale quand on écoute vite&nbsp;: le dernier nom reste en tête. Mais "
           + "il n'est pas là pour être choisi — il est là pour servir de <b>point de "
           + "comparaison</b>. Le mot «&nbsp;que&nbsp;» l'annonce." },
      { txt: "On ne peut pas savoir, il n'y a pas de prix.",
        rat_t: "La phrase suffit, même sans un seul chiffre.",
        rat: "C'est justement la force d'une comparaison&nbsp;: elle classe deux choses sans donner "
           + "aucun montant. «&nbsp;Moins cher&nbsp;» dit déjà lequel des deux vous coûtera moins." },
    ],
    pourquoi: "<b>Rue Fabre.</b> Retenez la phrase entière pour l'instant&nbsp;; on va voir "
            + "comment on l'a lue si vite.",
    attente: "Choisissez une réponse pour continuer.",
  },

  // ── 2. On écoute deux extraits. Toujours aucune règle. ───────────────────
  {
    id:   'avec-ou-sans',
    type: 'notion',
    eye:  "Deux phrases, une différence",
    menu: 'Écoutez les deux',
    titre: "Kofi essaie deux manteaux. Écoutez-le, puis écoutez la vendeuse.",
    paras: [
      "Deux phrases du même magasin. Toutes les deux commencent par «&nbsp;plus&nbsp;». "
      + "Une seule vous permet de faire quelque chose.",

      "La première dit qu'un manteau est plus chaud — mais plus chaud <b>que quoi</b>&nbsp;? "
      + "Personne ne le sait, Kofi non plus. La seconde va jusqu'au bout&nbsp;: elle nomme la "
      + "chose à laquelle on compare. C'est ce petit mot de liaison qui transforme une impression "
      + "en information.",
    ],
    sons: [
      { fichier: 't2/line_06_kofi.mp3', qui: "Kofi, entre le noir et le bleu",
        texte: "Tu trouves&nbsp;? Moi, je le trouvais plus chaud." },
      { fichier: 't1/line_11_valerie.mp3', qui: 'Valérie, sur le manteau en duvet',
        texte: "C'est du duvet, il est plus léger qu'il n'en a l'air. Essayez de bouger un peu." },
    ],
    retenir: "Écoutez ce qui vient <b>après</b> le mot de liaison. C'est là qu'est la moitié de "
           + "l'information.",
    attente: "Écoutez les deux extraits, puis continuez.",
  },

  // ── 3. Le cœur : six phrases à décoder, sans règle donnée. ───────────────
  {
    id:   'tri-lequel',
    type: 'tri',
    eye:  'À vous de trancher',
    menu: 'Six phrases',
    titre: "Six phrases. Dans chacune, lequel des deux coûte le moins cher ?",
    consigne: "Aucune règle ne vous a été donnée — normal. Une seule chose à repérer&nbsp;: "
            + "le mot devant, et ce qui vient après «&nbsp;que&nbsp;».",
    colonnes: [
      { id: 'avant', t: 'Celui nommé en premier',   b: 'Le premier' },
      { id: 'apres', t: 'Celui qui suit « que »',   b: 'Après « que »' },
    ],
    items: [
      { txt: "« Le forfait A est moins cher que le forfait B. »", ok: 'avant',
        rat: "«&nbsp;Moins&nbsp;» abaisse celui qui est nommé <b>avant</b>. Le forfait A descend, "
           + "donc c'est lui qui coûte le moins.",
        pourquoi: "Le forfait A. « Moins » abaisse le premier." },
      { txt: "« L'appartement de la rue Fabre est plus cher que celui de la rue Marquette. »",
        ok: 'apres',
        rat: "«&nbsp;Plus&nbsp;» monte celui qui est nommé avant. Si Fabre monte, c'est l'autre "
           + "qui reste en bas&nbsp;: Marquette.",
        pourquoi: "Rue Marquette. « Plus » monte le premier, donc l'autre descend." },
      { txt: "« Ce manteau-ci coûte moins cher que celui que tu as essayé hier. »", ok: 'avant',
        rat: "Même mécanique, avec des mots plus longs&nbsp;: «&nbsp;moins&nbsp;» abaisse "
           + "«&nbsp;ce manteau-ci&nbsp;», qui est nommé avant.",
        pourquoi: "Celui-ci. « Moins » abaisse le premier." },
      { txt: "« Le chauffage revient plus cher ici qu'au dernier étage. »", ok: 'apres',
        rat: "«&nbsp;Qu'&nbsp;» est le même mot que «&nbsp;que&nbsp;», raccourci devant une "
           + "voyelle. Ce qui le suit — le dernier étage — est le moins cher.",
        pourquoi: "Le dernier étage. « Qu' » est le même mot que « que »." },
      { txt: "« Deux petits formats coûtent plus cher qu'un grand. »", ok: 'apres',
        rat: "«&nbsp;Plus&nbsp;» monte les deux petits&nbsp;; le grand format reste donc en "
           + "dessous. C'est le calcul du dépanneur, et il surprend souvent.",
        pourquoi: "Un grand. Les deux petits montent." },
      { txt: "« Le forfait à quarante dollars est aussi cher que celui à quarante-cinq, "
           + "avec les frais. »", ok: 'avant',
        rat: "«&nbsp;Aussi&nbsp;» ne monte ni ne descend&nbsp;: les deux se valent. Alors relisez "
           + "les chiffres — celui qui est nommé avant est affiché à quarante, l'autre à "
           + "quarante-cinq. À prix final égal, c'est le premier qui vous coûte le moins d'avance.",
        pourquoi: "Le premier. « Aussi » dit que les deux se valent à la fin." },
    ],
    attente: "Tranchez les six phrases pour continuer.",
  },

  // ── 4. La règle, écrite comme un constat. ────────────────────────────────
  {
    id:   'la-fleche',
    type: 'notion',
    eye:  'Ce que vous venez de faire',
    menu: 'Le mot « que »',
    titre: "Vous n'avez pas traduit. Vous avez regardé deux endroits.",
    paras: [
      "Le premier endroit, c'est le petit mot devant l'adjectif. Il n'y en a que <b>trois</b>, et "
      + "ils font trois choses différentes&nbsp;: <b>plus</b> monte, <b>moins</b> descend, "
      + "<b>aussi</b> met à égalité. Le deuxième endroit, c'est ce qui vient après "
      + "<b>que</b>&nbsp;: la chose à laquelle on compare.",

      "«&nbsp;Que&nbsp;» n'est pas de la décoration grammaticale. C'est une <b>flèche</b>&nbsp;: "
      + "elle pointe vers l'autre chose. Sans elle, la phrase s'arrête en l'air — c'était le cas de "
      + "Kofi à l'écran 2, et son amie ne pouvait rien en faire.",

      "Le nom savant est le <b>comparatif</b>. Vous n'en avez pas besoin pour vous en servir, mais "
      + "votre enseignant l'emploiera.",
    ],
    retenir: "<b>plus · moins · aussi</b> devant, <b>que</b> derrière. "
           + "La flèche « que » pointe vers l'autre.",
    attente: "Lisez, puis continuez.",
  },

  // ── 5. La faute écrite : « plus cher de ». ───────────────────────────────
  {
    id:   'jamais-de',
    type: 'verif',
    eye:  'Le mot qui remplace « que »',
    menu: 'Ni « de », ni « comme »',
    titre: "Solange écrit à son propriétaire. Une seule version est correcte.",
    consigne: "Elle veut dire que le nouveau loyer dépasse celui de l'an dernier.",
    options: [
      { txt: "« Ce loyer est plus élevé que celui de l'an dernier. »", juste: true },
      { txt: "« Ce loyer est plus élevé de celui de l'an dernier. »",
        rat_t: "«&nbsp;De&nbsp;» sert ailleurs, jamais ici.",
        rat: "«&nbsp;De&nbsp;» existe bien dans une comparaison, mais pour dire l'<b>écart</b>&nbsp;: "
           + "«&nbsp;plus élevé <b>de</b> vingt dollars&nbsp;». Devant la chose à laquelle on "
           + "compare, c'est toujours <b>que</b>. Les deux peuvent d'ailleurs se suivre&nbsp;: plus "
           + "élevé de vingt dollars que l'an dernier." },
      { txt: "« Ce loyer est plus élevé comme celui de l'an dernier. »",
        rat_t: "«&nbsp;Comme&nbsp;» dit la ressemblance, pas la différence.",
        rat: "«&nbsp;Comme&nbsp;» sert à dire que deux choses se ressemblent&nbsp;: «&nbsp;un loyer "
           + "comme le mien&nbsp;». Dès qu'on classe l'une au-dessus ou au-dessous de l'autre, "
           + "c'est <b>que</b> — et lui seul." },
    ],
    pourquoi: "<b>Plus élevé que.</b> «&nbsp;De&nbsp;» ne vient qu'avec un chiffre d'écart&nbsp;; "
            + "«&nbsp;comme&nbsp;» ne compare pas, il rapproche.",
    attente: "Choisissez une réponse pour continuer.",
  },

  // ── 6. Les deux irréguliers, entendus avant d'être nommés. ───────────────
  {
    id:   'meilleur-mieux',
    type: 'notion',
    eye:  'Les deux qui refusent le moule',
    menu: 'Meilleur, mieux',
    titre: "Trois fois « mieux » en dix minutes de magasin. Zéro fois « plus bien ».",
    paras: [
      "Écoutez les trois extraits. Personne ne dit «&nbsp;plus bien&nbsp;» ni «&nbsp;plus "
      + "bon&nbsp;»&nbsp;: ces deux-là n'existent pas en français. Ils ont chacun un mot à eux, "
      + "et ce sont les deux mots qu'on entend le plus souvent.",

      "<b>Meilleur</b> remplace «&nbsp;plus bon&nbsp;». Il décrit une <b>chose</b>, et il s'accorde "
      + "avec elle&nbsp;: un meilleur manteau, une meilleure offre. <b>Mieux</b> remplace "
      + "«&nbsp;plus bien&nbsp;». Il décrit une <b>action</b>, et il ne change jamais&nbsp;: "
      + "il tombe mieux, on dort mieux, ça se lave mieux.",

      "<b>Le test&nbsp;:</b> si le mot répond à «&nbsp;comment&nbsp;?&nbsp;» après un verbe, c'est "
      + "<i>mieux</i>. S'il décrit un objet, c'est <i>meilleur</i>.",
    ],
    sons: [
      { fichier: 't1/line_06_kofi.mp3', qui: "Kofi, après avoir essayé le grand",
        texte: "Celui-là est mieux. Les manches sont un peu longues, par exemple." },
      { fichier: 't2/line_05_diane.mp3', qui: 'Diane donne son avis',
        texte: "Franchement, il est trop grand aux épaules. Le noir tombe mieux." },
      { fichier: 'prep/line_11_valerie.mp3', qui: 'Valérie, sur les tailles',
        texte: "Ça change d'une marque à l'autre. Le mieux, c'est d'essayer. "
             + "Les cabines sont au fond." },
    ],
    retenir: "Une chose&nbsp;: <b>meilleur</b>, et il s'accorde. Une action&nbsp;: <b>mieux</b>, "
           + "et il ne bouge pas. «&nbsp;Plus bon&nbsp;» et «&nbsp;plus bien&nbsp;» n'existent pas.",
    attente: "Écoutez les trois extraits, puis continuez.",
  },

  // ── 7. Trier six phrases entre les deux irréguliers. ─────────────────────
  {
    id:   'tri-irreguliers',
    type: 'tri',
    eye:  'À vous de trancher',
    menu: 'Six trous',
    titre: "Six phrases à trou. Meilleur ou mieux ?",
    consigne: "Une seule question&nbsp;: est-ce que le mot décrit une chose, ou la façon "
            + "dont ça se passe&nbsp;?",
    colonnes: [
      { id: 'meil', t: 'meilleur (ou meilleure)', b: 'meilleur' },
      { id: 'mieu', t: 'mieux',                   b: 'mieux' },
    ],
    items: [
      { txt: "« Ce manteau est ___ que l'autre. »", ok: 'meil',
        rat: "Le mot décrit le <b>manteau</b>, une chose&nbsp;: c'est «&nbsp;meilleur&nbsp;». "
           + "«&nbsp;Plus bon&nbsp;» ne se dit pas.",
        pourquoi: "Meilleur. Il décrit le manteau." },
      { txt: "« Depuis qu'on a changé de logement, je dors ___. »", ok: 'mieu',
        rat: "Le mot dit <b>comment</b> vous dormez&nbsp;: il décrit une action, donc "
           + "«&nbsp;mieux&nbsp;». «&nbsp;Plus bien&nbsp;» ne se dit pas.",
        pourquoi: "Mieux. Il dit comment on dort." },
      { txt: "« Le café du dépanneur est ___ que celui de la machine. »", ok: 'meil',
        rat: "Le mot décrit le <b>café</b>, une chose qu'on goûte&nbsp;: «&nbsp;meilleur&nbsp;».",
        pourquoi: "Meilleur. Il décrit le café." },
      { txt: "« Cette veste me va ___ que la grise. »", ok: 'mieu',
        rat: "Le mot dit <b>comment</b> la veste vous va — c'est la manière, pas la veste. "
           + "«&nbsp;Elle me va mieux&nbsp;», comme «&nbsp;elle tombe mieux&nbsp;».",
        pourquoi: "Mieux. Il dit comment elle va." },
      { txt: "« C'est la ___ offre des trois. »", ok: 'meil',
        rat: "Le mot décrit l'<b>offre</b>, une chose. Et comme «&nbsp;offre&nbsp;» est féminin, "
           + "il s'accorde&nbsp;: la meilleure offre.",
        pourquoi: "La meilleure offre. Il s'accorde avec « offre »." },
      { txt: "« Ce tissu se lave ___ que la laine. »", ok: 'mieu',
        rat: "C'est le piège de la série&nbsp;: le mot vient juste après un verbe et dit comment "
           + "ça se lave. Il décrit le <b>lavage</b>, pas le tissu. Donc «&nbsp;mieux&nbsp;».",
        pourquoi: "Mieux. Il dit comment ça se lave." },
    ],
    attente: "Tranchez les six phrases pour continuer.",
  },

  // ── 8. Le piège d'écoute : « moins » qui ne compare rien. ────────────────
  {
    id:   'moins-trente',
    type: 'verif',
    eye:  'Le piège de l\'oreille',
    menu: '« Moins trente »',
    titre: "Vous entendez « moins » au magasin. Ce n'est pas toujours une comparaison.",
    consigne: "Écoutez Valérie, puis dites ce qu'elle annonce.",
    sons: [
      { fichier: 'prep/line_05_valerie.mp3', qui: 'Valérie, sur le choix du manteau',
        texte: "Alors il vous faut un manteau coté moins trente. C'est écrit sur l'étiquette, "
             + "en petit." },
    ],
    options: [
      { txt: "Le manteau protège jusqu'à une température de trente degrés sous zéro.",
        juste: true },
      { txt: "Ce manteau est moins chaud qu'un autre manteau.",
        rat_t: "Il n'y a pas de «&nbsp;que&nbsp;», donc pas de comparaison.",
        rat: "Sans la flèche «&nbsp;que&nbsp;», rien n'est comparé à rien. Et regardez ce qui suit "
           + "«&nbsp;moins&nbsp;»&nbsp;: un <b>nombre</b>, pas un adjectif. Un comparatif demande "
           + "un adjectif — moins <i>chaud</i>, moins <i>cher</i>." },
      { txt: "Le manteau coûte trente dollars de moins.",
        rat_t: "Le prix ne se dit pas ainsi.",
        rat: "Un rabais s'annonce «&nbsp;trente dollars <b>de moins</b>&nbsp;», avec l'unité et "
           + "«&nbsp;de&nbsp;» derrière. Ici, «&nbsp;moins&nbsp;» est <b>devant</b> le nombre&nbsp;: "
           + "c'est le signe des températures d'hiver." },
    ],
    pourquoi: "<b>« Moins » devant un nombre est une température, pas une comparaison.</b> "
            + "Le test tient en deux secondes&nbsp;: y a-t-il un adjectif après, et un "
            + "«&nbsp;que&nbsp;» plus loin&nbsp;? Sinon, on ne compare rien.",
    attente: "Choisissez une réponse pour continuer.",
  },

  // ── 9. Écrire une comparaison entière. ───────────────────────────────────
  {
    id:   'deux-forfaits',
    type: 'verif',
    eye:  'Vérification',
    menu: 'Deux forfaits',
    titre: "Ana compare deux forfaits de téléphone pour sa sœur. Quelle version tient d'un bout à l'autre ?",
    consigne: "Le forfait de la boutique coûte 35 $ et donne moins de données&nbsp;; celui du "
            + "site coûte 40 $ et en donne davantage.",
    options: [
      { txt: "« Celui de la boutique est moins cher que celui du site, mais l'autre est meilleur "
           + "pour toi : tu utilises beaucoup de données. »", juste: true },
      { txt: "« Celui de la boutique est moins cher de celui du site, mais l'autre est plus bon "
           + "pour toi : tu utilises beaucoup de données. »",
        rat_t: "Deux fautes, et ce sont les deux du point express.",
        rat: "«&nbsp;Moins cher <b>de</b>&nbsp;»&nbsp;: devant la chose à laquelle on compare, c'est "
           + "<i>que</i>. «&nbsp;Plus bon&nbsp;»&nbsp;: ce mot n'existe pas, c'est <i>meilleur</i>, "
           + "et il s'accorde avec le forfait — masculin, donc «&nbsp;meilleur&nbsp;»." },
      { txt: "« Celui de la boutique est moins cher que celui du site, mais l'autre est mieux "
           + "pour toi : tu utilises beaucoup de données. »",
        rat_t: "La première moitié est parfaite. Le dernier mot glisse.",
        rat: "«&nbsp;Mieux&nbsp;» décrit une action&nbsp;: on dort mieux, ça se lave mieux. Ici, le "
           + "mot décrit le <b>forfait</b>, une chose — donc <b>meilleur</b>. La phrase se "
           + "comprendrait, mais c'est exactement la confusion que ce point express vient régler." },
    ],
    pourquoi: "<b>Moins cher que</b> pour classer, <b>meilleur</b> pour la chose. Et remarquez la "
            + "fin&nbsp;: Ana ne se contente pas de comparer, elle conclut. Une comparaison qui ne "
            + "sert à rien décider n'aide personne.",
    attente: "Choisissez une réponse pour continuer.",
  },

  // ── 10. La fermeture : les deux logements de l'écran 1. ──────────────────
  {
    id:   'fermeture',
    type: 'verif',
    eye:  'La dernière',
    menu: 'Pour finir',
    titre: "On revient aux deux logements. Cette fois, c'est vous qui parlez.",
    consigne: "Rue Fabre&nbsp;: 950&nbsp;$, chauffage non compris. Rue Marquette&nbsp;: "
            + "1 050&nbsp;$, chauffage compris. Vous expliquez votre choix à un ami&nbsp;: "
            + "vous prenez Marquette.",
    options: [
      { txt: "« Marquette est plus cher que Fabre, mais le chauffage est compris. "
           + "Au total, c'est meilleur pour moi. »", juste: true },
      { txt: "« Marquette est plus cher, mais le chauffage est compris. »",
        rat_t: "Plus cher que quoi&nbsp;? C'est la phrase de Kofi, à l'écran 2.",
        rat: "Votre ami ne connaît pas les deux adresses. Sans la flèche «&nbsp;que&nbsp;», il ne "
           + "sait pas à quoi vous comparez, et il ne peut rien vous répondre. Nommez l'autre "
           + "logement&nbsp;: « plus cher <b>que Fabre</b> »." },
      { txt: "« Marquette est moins cher que Fabre, mais le chauffage est compris. »",
        rat_t: "Vous avez le «&nbsp;que&nbsp;». C'est le mot devant qui est à l'envers.",
        rat: "1 050&nbsp;$ contre 950&nbsp;$&nbsp;: Marquette est <b>au-dessus</b>, donc "
           + "«&nbsp;plus cher&nbsp;». Et le «&nbsp;mais&nbsp;» qui suit le montre bien — on ne "
           + "corrige pas un avantage avec un «&nbsp;mais&nbsp;»." },
    ],
    pourquoi: "«&nbsp;<b>Plus cher que</b> Fabre… c'est <b>meilleur</b> pour moi.&nbsp;» "
            + "Vous avez fait les trois choses&nbsp;: le mot qui classe, la flèche qui nomme "
            + "l'autre, et l'irrégulier au lieu de «&nbsp;plus bon&nbsp;».",
    attente: "Choisissez une réponse pour finir.",
  },

];
