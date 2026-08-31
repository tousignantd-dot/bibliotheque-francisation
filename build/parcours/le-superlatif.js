// ═══════════════════════════════════════════════════════════════════════════
// Point express — Un contre tous : dire lequel est en tête
//
// Savoir n4-s38 (Adverbes et GAdv) : « comprendre le superlatif — C'est la
// plus économique. » Une ORDONNANCE : l'enseignant l'envoie à un élève qui
// écrit « c'est plus économique du magasin » ou « c'est le plus économique que
// les autres ».
//
// ── Ce qui le sépare du point express « Comparer », et des mini-leçons ─────
// L'étagère porte déjà « Comparer : plus, moins, aussi… que » (n4-s38), et il
// ne faut surtout pas le refaire. Ce point-là tient sur DEUX objets et sur une
// flèche : le mot « que », et ce qui vient après lui. Il ne dit pas un mot de
// l'article, et c'est volontaire — un comparatif n'en a pas.
//
// Celui-ci porte sur le geste inverse : UN objet contre TOUT UN GROUPE. Et la
// faute n'est pas la même. En comparatif, l'élève se trompe de préposition
// (« plus cher de »). En superlatif, il OUBLIE UN MOT — l'article « le »,
// « la », « les » — et sa phrase devient une comparaison sans second terme :
// « c'est plus économique », qui laisse l'interlocuteur attendre la suite.
//
// Trois mini-leçons l'effleurent : « Le plus, le moins » (module-n5-quebec),
// « Comparer avec des chiffres : comparatifs et superlatifs » et « Comparer
// deux prix ». Toutes le donnent comme une case de plus dans le tableau du
// comparatif — donc comme une variante, alors que c'est un autre geste. Les
// cinq écarts tenus :
//
//   1. INDUCTIF, ET SUR LE DÉCODAGE. Écran 1 et écran 2 : combien de choses le
//      vendeur a-t-il comparées ? L'élève tranche huit cas avant qu'aucune
//      règle ne soit dite.
//   2. UN SEUL TEST, RÉUTILISABLE : « que » ou « de ». « que » ouvre sur un
//      second objet ; « de » ouvre sur un groupe entier — et un groupe entier
//      exige l'article. Rien à mémoriser d'autre.
//   3. L'ARTICLE OUBLIÉ EST LE SUJET. Quatre écrans sur dix portent sur ce
//      petit mot, jamais sur le choix entre « plus » et « moins ».
//   4. LES IRRÉGULIERS SONT DITS EN DERNIER (écran 8), et seulement sous leur
//      forme de superlatif — « le meilleur », « le mieux ». Le comparatif
//      « meilleur que » appartient à l'autre point express.
//   5. EXEMPLES VARIÉS : un circulaire d'épicerie, un choix de logement, un
//      trajet d'autobus, une lettre de motivation, un forfait de cellulaire.
//
// Aucun média : « c'est plus économique » et « c'est la plus économique » se
// distinguent parfaitement à l'oreille. Ce que l'élève rate, c'est de
// l'écrire — et de comprendre ce que la phrase entendue voulait dire.
// ═══════════════════════════════════════════════════════════════════════════

const PARCOURS = {
  slug:     'le-superlatif',
  titre:    "Un contre tous : dire lequel est en tête",
  surtitre: "Point express · 10 minutes",
  niveau:   4,
  savoir:   'n4-s38',
};

const ECRANS = [

  // ── 1. Une décision, sans aucune règle donnée. ───────────────────────────
  {
    id:   'depart',
    type: 'verif',
    eye:  'Une question, pour commencer',
    menu: 'Deux phrases',
    titre: "Un commis vous dit : « Celle-là, c'est la moins chère du magasin. »",
    consigne: "Répondez tout de suite, sans relire trois fois — c'est le temps que vous aurez "
            + "devant lui. On expliquera après&nbsp;: c'est fait exprès.",
    options: [
      { txt: "Il l'a comparée à <b>toutes</b> celles du magasin.", juste: true },
      { txt: "Il l'a comparée à une autre, celle qu'il vous a montrée avant.",
        rat_t: "C'est ce que voudrait dire «&nbsp;elle est moins chère <b>que</b> l'autre&nbsp;».",
        rat: "Le commis n'a pas dit «&nbsp;que&nbsp;»&nbsp;: il a dit «&nbsp;<b>du</b> "
           + "magasin&nbsp;». Ce petit mot-là ouvre sur un groupe entier, pas sur un second "
           + "objet. Et il a mis un article devant — «&nbsp;<b>la</b> moins chère&nbsp;» — ce "
           + "qu'une comparaison entre deux choses n'a jamais." },
      { txt: "Il dit seulement qu'elle n'est pas chère.",
        rat_t: "C'est une phrase de publicité, et celle-ci dit beaucoup plus.",
        rat: "«&nbsp;Elle n'est pas chère&nbsp;» ne s'engage à rien. «&nbsp;La moins chère du "
           + "magasin&nbsp;» est une affirmation vérifiable&nbsp;: s'il y en a une autre à "
           + "moindre prix, le commis a tort. C'est exactement pour ça que la formule est "
           + "utile — et qu'il faut savoir la reconnaître." },
    ],
    pourquoi: "Toutes celles du magasin. Gardez la phrase&nbsp;: on y revient au dernier écran.",
    attente: "Choisissez une réponse pour continuer.",
  },

  // ── 2. On trie AVANT de savoir. ──────────────────────────────────────────
  {
    id:   'tri-huit',
    type: 'tri',
    eye:  'À vous de trancher',
    menu: 'Huit phrases',
    titre: "Huit phrases entendues ou lues. Combien de choses sont comparées ?",
    consigne: "Aucune règle ne vous a été donnée — normal. Demandez-vous seulement&nbsp;: la "
            + "phrase parle-t-elle d'un <b>deuxième</b> objet, ou d'un <b>groupe</b>&nbsp;?",
    colonnes: [
      { id: 'deux',   t: "Deux choses",     b: "Deux choses" },
      { id: 'groupe', t: "Un groupe entier", b: "Un groupe" },
    ],
    items: [
      { txt: "Le 55 est plus rapide que le 24.", sous: "deux lignes d'autobus", ok: 'deux',
        rat: "Le mot «&nbsp;que&nbsp;» est là, et il est suivi d'un seul autre autobus. On ne "
           + "sait rien des autres lignes de la ville.",
        pourquoi: "« que » + un seul autre objet : deux choses." },
      { txt: "Le 55 est la ligne la plus rapide du secteur.", sous: "un plan affiché à l'arrêt", ok: 'groupe',
        rat: "«&nbsp;Du secteur&nbsp;» englobe toutes les lignes du coin. Et remarquez le "
           + "petit mot devant «&nbsp;plus&nbsp;»&nbsp;: il n'était pas dans la phrase "
           + "précédente.",
        pourquoi: "« du secteur » : toutes les lignes du coin." },
      { txt: "C'est le logement le moins cher que j'ai visité.", sous: "un message à sa sœur", ok: 'groupe',
        rat: "Celui-là trompe, parce qu'il porte un «&nbsp;que&nbsp;». Mais ce "
           + "«&nbsp;que&nbsp;»-là n'introduit pas un second logement&nbsp;: il ouvre "
           + "«&nbsp;<i>que j'ai visité</i>&nbsp;», c'est-à-dire le groupe de toutes les "
           + "visites. Et l'article est là&nbsp;: «&nbsp;<b>le</b> moins cher&nbsp;».",
        pourquoi: "Le groupe est « tout ce que j'ai visité »." },
      { txt: "Ce manteau est aussi chaud que l'autre.", sous: "dans un magasin", ok: 'deux',
        rat: "Deux manteaux, et une égalité entre les deux. Aucun article devant "
           + "«&nbsp;aussi&nbsp;», et aucun groupe nommé.",
        pourquoi: "Deux manteaux, rien d'autre." },
      { txt: "De tous les modèles, c'est le plus léger.", sous: "un dépliant de quincaillerie", ok: 'groupe',
        rat: "Le groupe est même écrit en premier&nbsp;: «&nbsp;de tous les modèles&nbsp;». "
           + "La phrase désigne ensuite un seul gagnant.",
        pourquoi: "« de tous les modèles » : un groupe entier." },
      { txt: "Ma fille est plus grande que moi.", sous: "une conversation entre voisines", ok: 'deux',
        rat: "Deux personnes, et une flèche entre les deux. On ne dit rien de la famille "
           + "entière.",
        pourquoi: "Deux personnes comparées." },
      { txt: "Ma fille est la plus grande de la classe.", sous: "la même conversation, dix secondes plus tard", ok: 'groupe',
        rat: "Même personne, même adjectif — et pourtant la phrase a changé de métier. "
           + "«&nbsp;De la classe&nbsp;» ouvre sur trente élèves, et l'article "
           + "«&nbsp;<b>la</b>&nbsp;» est apparu.",
        pourquoi: "« de la classe » : trente élèves derrière." },
      { txt: "Le forfait à 30 $ offre moins de données.", sous: "un site de téléphonie", ok: 'deux',
        rat: "Il manque le second terme, mais il est sous-entendu&nbsp;: moins que l'autre "
           + "forfait dont on vient de parler. Aucun article, aucun groupe&nbsp;: ce n'est pas "
           + "un classement.",
        pourquoi: "Comparaison avec l'autre forfait, sous-entendu." },
    ],
    attente: "Tranchez les huit phrases pour continuer.",
  },

  // ── 3. La règle, écrite comme un constat. ────────────────────────────────
  {
    id:   'le-test',
    type: 'notion',
    eye:  'Ce que vous venez de faire',
    menu: 'Le test',
    titre: "Vous avez rangé les phrases sur un seul mot, et ce n'était pas « plus ».",
    paras: [
      "Regardez votre colonne «&nbsp;un groupe&nbsp;»&nbsp;: chaque phrase porte un petit "
      + "article devant «&nbsp;plus&nbsp;» ou «&nbsp;moins&nbsp;» — <b>le</b>, <b>la</b>, "
      + "<b>les</b> — et un groupe introduit par <b>de</b>, <b>du</b>, <b>des</b>. Votre autre "
      + "colonne n'a ni l'un ni l'autre&nbsp;: elle a un «&nbsp;que&nbsp;» et un second objet.",

      "<b>Le test, sur n'importe quelle phrase&nbsp;:</b> essayez d'ajouter «&nbsp;de "
      + "tous&nbsp;» ou «&nbsp;du magasin&nbsp;». Si ça tient, vous désignez le premier d'un "
      + "groupe&nbsp;: il faut <b>l'article</b>, et le groupe s'introduit par "
      + "<b>de</b>. Si ça ne tient pas, vous comparez deux choses&nbsp;: pas d'article, et "
      + "<b>que</b>.",

      "Cette forme s'appelle le <b>superlatif</b>. Vous n'avez pas besoin du mot pour vous en "
      + "servir&nbsp;; votre enseignant l'emploiera.",
    ],
    retenir: "Un groupe derrière&nbsp;? Alors <b>le / la / les</b> devant, et <b>de</b> pour "
           + "nommer le groupe. Jamais «&nbsp;que&nbsp;».",
    attente: "Lisez, puis continuez.",
  },

  // ── 4. Le mot oublié. C'est le cœur du point. ────────────────────────────
  {
    id:   'larticle-oublie',
    type: 'verif',
    eye:  'Le défaut à corriger',
    menu: "L'article",
    titre: "Vous écrivez à un collègue pour lui indiquer le chemin le plus court.",
    consigne: "Vous connaissez trois trajets. Vous voulez lui donner celui qui gagne sur les "
            + "trois.",
    options: [
      { txt: "«&nbsp;Passe par la rue Saint-Zotique&nbsp;: c'est le trajet le plus court.&nbsp;»",
        juste: true },
      { txt: "«&nbsp;Passe par la rue Saint-Zotique&nbsp;: c'est un trajet plus court.&nbsp;»",
        rat_t: "C'est la faute que ce point vient corriger.",
        rat: "Sans l'article devant «&nbsp;plus&nbsp;», votre collègue attend la suite&nbsp;: "
           + "plus court <b>que quoi</b>&nbsp;? Il va se demander s'il existe encore mieux. "
           + "Le petit mot «&nbsp;le&nbsp;» est ce qui ferme la question&nbsp;: c'est celui-là, "
           + "et il n'y a rien au-dessus." },
      { txt: "«&nbsp;Passe par la rue Saint-Zotique&nbsp;: c'est le trajet plus court que les "
           + "autres.&nbsp;»",
        rat_t: "Vous avez mis l'article — et gardé le «&nbsp;que&nbsp;» de la comparaison.",
        rat: "Les deux constructions sont là en même temps, et elles se contredisent. Choisissez "
           + "l'une&nbsp;: «&nbsp;<b>le</b> trajet <b>le</b> plus court&nbsp;» (un contre tous) "
           + "ou «&nbsp;un trajet plus court <b>que</b> les autres&nbsp;» (deux à deux)." },
    ],
    pourquoi: "L'article n'est pas une décoration&nbsp;: c'est lui qui dit qu'il n'y a rien "
            + "au-dessus. Sans lui, la phrase reste ouverte.",
    attente: "Choisissez une réponse pour continuer.",
  },

  // ── 5. La place, quand le nom est écrit. ─────────────────────────────────
  {
    id:   'la-place',
    type: 'notion',
    eye:  'La place',
    menu: 'Deux fois le petit mot',
    titre: "Quand le nom est écrit, le petit mot revient deux fois.",
    paras: [
      "«&nbsp;<b>Le</b> trajet <b>le</b> plus court.&nbsp;» «&nbsp;<b>La</b> ligne <b>la</b> "
      + "plus rapide.&nbsp;» «&nbsp;<b>Les</b> loyers <b>les</b> moins chers.&nbsp;» Ça semble "
      + "lourd, et c'est pourtant ce qu'on écrit et ce qu'on entend. Le premier appartient au "
      + "nom, le second au classement.",

      "Quand le nom vient d'être dit, on le laisse tomber et il n'en reste qu'un&nbsp;: "
      + "«&nbsp;<i>J'ai visité trois logements. <b>Le</b> moins cher est sur Bélanger.</i>&nbsp;» "
      + "C'est le cas le plus fréquent à l'oral.",

      "Et le petit mot <b>s'accorde avec la chose</b>, pas avec l'adjectif&nbsp;: une ligne "
      + "→ <b>la</b> plus rapide&nbsp;; des loyers → <b>les</b> moins chers. C'est là que se "
      + "glissent la moitié des fautes d'écrit.",
    ],
    retenir: "Nom écrit&nbsp;: deux petits mots («&nbsp;le trajet le plus court&nbsp;»). Nom "
           + "sous-entendu&nbsp;: un seul («&nbsp;le moins cher&nbsp;»).",
    attente: "Lisez, puis continuez.",
  },

  // ── 6. Trier des phrases écrites. ────────────────────────────────────────
  {
    id:   'tri-ecrites',
    type: 'tri',
    eye:  'À vous de trancher',
    menu: 'Six phrases',
    titre: "Six phrases écrites. Lesquelles tiennent ?",
    consigne: "Deux choses à regarder&nbsp;: l'article est-il là, et le groupe est-il introduit "
            + "par «&nbsp;de&nbsp;»&nbsp;?",
    colonnes: [
      { id: 'ok',   t: 'Correcte',  b: 'Correcte' },
      { id: 'faux', t: 'Une faute', b: 'Une faute' },
    ],
    items: [
      { txt: "C'est la pharmacie la plus proche de chez moi.", ok: 'ok',
        rat: "Nom écrit, donc deux petits mots, tous deux au féminin comme «&nbsp;pharmacie&nbsp;». "
           + "Et le groupe est introduit par «&nbsp;de&nbsp;».",
        pourquoi: "Deux articles au féminin : correct." },
      { txt: "C'est plus économique du magasin.", ok: 'faux',
        rat: "Le groupe est bien annoncé par «&nbsp;du magasin&nbsp;», mais l'article manque "
           + "devant «&nbsp;plus&nbsp;». La phrase promet un classement et n'en donne "
           + "pas&nbsp;: «&nbsp;c'est <b>le</b> plus économique du magasin&nbsp;».",
        pourquoi: "Il manque l'article : le plus économique." },
      { txt: "Mon fils est le plus jeune de sa classe.", ok: 'ok',
        rat: "Le nom est sous-entendu («&nbsp;le plus jeune <i>élève</i>&nbsp;»), donc un seul "
           + "petit mot. Groupe en «&nbsp;de&nbsp;». Rien à corriger.",
        pourquoi: "Nom sous-entendu : un seul article." },
      { txt: "C'est le solution la plus simple.", ok: 'faux',
        rat: "Les deux articles sont là et le groupe est sous-entendu&nbsp;: la construction "
           + "est bonne. C'est l'accord qui manque — «&nbsp;<b>la</b> solution&nbsp;», donc "
           + "«&nbsp;<b>la</b> solution <b>la</b> plus simple&nbsp;». Le petit mot suit la "
           + "chose, jamais l'adjectif.",
        pourquoi: "« Solution » est féminin : la solution la plus…" },
      { txt: "Ce sont les loyers les moins chers du quartier.", ok: 'ok',
        rat: "Pluriel d'un bout à l'autre&nbsp;: deux articles au pluriel, adjectif au pluriel, "
           + "groupe en «&nbsp;du quartier&nbsp;».",
        pourquoi: "Pluriel partout : correct." },
      { txt: "C'est le plus rapide que tous les autres.", ok: 'faux',
        rat: "L'article est bon, mais le groupe est amené par «&nbsp;que&nbsp;», qui appartient "
           + "à la comparaison entre deux. Un groupe se nomme avec «&nbsp;de&nbsp;»&nbsp;: "
           + "«&nbsp;c'est le plus rapide <b>de tous</b>&nbsp;».",
        pourquoi: "Un groupe s'introduit par « de », pas par « que »." },
    ],
    attente: "Tranchez les six phrases pour continuer.",
  },

  // ── 7. L'accord, là où il coûte cher. ────────────────────────────────────
  {
    id:   'laccord',
    type: 'verif',
    eye:  'Vérification',
    menu: 'Une candidature',
    titre: "Vous écrivez une lettre pour un poste. Une phrase à choisir.",
    consigne: "Vous voulez dire que la formation que vous avez suivie est reconnue partout au "
            + "Québec, et qu'elle est en tête.",
    options: [
      { txt: "«&nbsp;J'ai suivi la formation la plus reconnue de la province.&nbsp;»", juste: true },
      { txt: "«&nbsp;J'ai suivi le formation le plus reconnu de la province.&nbsp;»",
        rat_t: "La construction est parfaite. Ce sont les accords qui tombent.",
        rat: "Vous avez posé les deux petits mots au bon endroit, et c'est le plus difficile. "
           + "Reste qu'ils suivent la chose&nbsp;: «&nbsp;formation&nbsp;» est féminin, donc "
           + "«&nbsp;<b>la</b> formation <b>la</b> plus reconnu<b>e</b>&nbsp;». Dans une "
           + "lettre de candidature, cette faute-là se voit du premier coup d'œil." },
      { txt: "«&nbsp;J'ai suivi une formation plus reconnue de la province.&nbsp;»",
        rat_t: "Sans l'article, la phrase ne dit plus ce que vous vouliez dire.",
        rat: "Elle laisse entendre qu'il y en a d'autres au-dessus — c'est même le contraire "
           + "de votre intention. Et «&nbsp;plus reconnue de la province&nbsp;» ne se dit "
           + "pas&nbsp;: le groupe en «&nbsp;de&nbsp;» réclame l'article devant." },
    ],
    pourquoi: "Le petit mot s'accorde avec la <b>chose</b>&nbsp;: la formation → la plus "
            + "reconnue&nbsp;; le dossier → le plus complet&nbsp;; les résultats → les plus "
            + "solides.",
    attente: "Choisissez une réponse pour continuer.",
  },

  // ── 8. Les deux irréguliers, dits en dernier. ────────────────────────────
  {
    id:   'les-irreguliers',
    type: 'notion',
    eye:  'Ce qui reste',
    menu: 'Le meilleur, le mieux',
    titre: "Deux mots refusent « le plus », et ce sont les deux qu'on emploie le plus souvent.",
    paras: [
      "On a gardé ceci pour la fin&nbsp;: ce n'est pas une règle de plus, c'est une exception à "
      + "celle que vous venez d'apprendre. On ne dit jamais «&nbsp;le plus bon&nbsp;» ni "
      + "«&nbsp;le plus bien&nbsp;». On dit <b>le meilleur</b> et <b>le mieux</b>.",

      "La différence tient en une question&nbsp;: parle-t-on d'une <b>chose</b> ou d'une "
      + "<b>façon de faire</b>&nbsp;? Une chose&nbsp;: «&nbsp;<i>C'est <b>le meilleur</b> prix "
      + "du quartier.</i>&nbsp;» «&nbsp;<i><b>La meilleure</b> école est sur Papineau.</i>&nbsp;» "
      + "Une façon de faire&nbsp;: «&nbsp;<i>C'est ce qui marche <b>le mieux</b>.</i>&nbsp;» "
      + "«&nbsp;<i><b>Le mieux</b>, c'est de rappeler demain matin.</i>&nbsp;»",

      "«&nbsp;Le meilleur&nbsp;» s'accorde comme tout le reste — <b>la meilleure</b>, "
      + "<b>les meilleurs</b>. «&nbsp;Le mieux&nbsp;» ne bouge jamais. Vous n'avez donc "
      + "<b>qu'une chose</b> à surveiller de plus&nbsp;: est-ce que je qualifie un objet, ou "
      + "une manière&nbsp;?",
    ],
    retenir: "Un objet&nbsp;: <b>le meilleur</b>, et il s'accorde. Une manière&nbsp;: "
           + "<b>le mieux</b>, qui ne bouge pas.",
    attente: "Lisez, puis continuez.",
  },

  // ── 9. Écrire, pas reconnaître. ──────────────────────────────────────────
  {
    id:   'votre-message',
    type: 'verif',
    eye:  'Vérification',
    menu: 'Trois forfaits',
    titre: "Vous comparez trois forfaits pour votre sœur. Quelle version tient d'un bout à l'autre ?",
    consigne: "Le forfait à 25 $ gagne sur les trois pour le prix, et c'est aussi celui qui "
            + "donne les meilleures conditions.",
    options: [
      { txt: "«&nbsp;Le forfait à 25 $ est le moins cher des trois, et c'est le meilleur pour "
           + "toi.&nbsp;»", juste: true },
      { txt: "«&nbsp;Le forfait à 25 $ est le moins cher que les trois, et c'est le plus bon "
           + "pour toi.&nbsp;»",
        rat_t: "Deux fautes, et ce sont les deux dernières que vous avez vues.",
        rat: "Un groupe se nomme avec «&nbsp;de&nbsp;»&nbsp;: «&nbsp;le moins cher <b>des</b> "
           + "trois&nbsp;». Et «&nbsp;bon&nbsp;» refuse «&nbsp;plus&nbsp;»&nbsp;: on dit "
           + "«&nbsp;<b>le meilleur</b>&nbsp;». Le reste de la phrase était juste." },
      { txt: "«&nbsp;Le forfait à 25 $ est moins cher des trois, et c'est le mieux pour "
           + "toi.&nbsp;»",
        rat_t: "L'article manque au premier, et le second désigne un objet.",
        rat: "«&nbsp;Moins cher des trois&nbsp;» reste ouvert&nbsp;: il faut «&nbsp;<b>le</b> "
           + "moins cher&nbsp;». Et «&nbsp;le mieux&nbsp;» qualifie une manière de faire, pas "
           + "un forfait&nbsp;: pour un objet, c'est «&nbsp;<b>le meilleur</b>&nbsp;»." },
    ],
    pourquoi: "L'article, le groupe en «&nbsp;de&nbsp;», et l'irrégulier au bon endroit. "
            + "<b>C'est tout le point en une phrase.</b>",
    attente: "Choisissez une réponse pour continuer.",
  },

  // ── 10. La fermeture : le cas de l'écran 1. ──────────────────────────────
  {
    id:   'fermeture',
    type: 'verif',
    eye:  'La dernière',
    menu: 'Pour finir',
    titre: "On revient au magasin. Cette fois, c'est vous qui parlez.",
    consigne: "Vous avez regardé toutes les bouilloires du rayon. Vous voulez dire au commis "
            + "que celle-ci gagne sur toutes, et lui demander s'il en existe une moins chère "
            + "ailleurs.",
    options: [
      { txt: "«&nbsp;C'est la moins chère du rayon, non&nbsp;? En avez-vous une moins chère "
           + "en réserve&nbsp;?&nbsp;»", juste: true },
      { txt: "«&nbsp;C'est moins chère que le rayon, non&nbsp;? En avez-vous la moins chère en "
           + "réserve&nbsp;?&nbsp;»",
        rat_t: "Les deux constructions ont été échangées.",
        rat: "La première phrase désigne un gagnant dans un groupe&nbsp;: article, et "
           + "«&nbsp;<b>du</b> rayon&nbsp;». La seconde compare deux objets&nbsp;: pas "
           + "d'article, juste «&nbsp;une moins chère&nbsp;». Chaque phrase se teste pour "
           + "elle-même — c'est ce qui a fait le tri de l'écran 2." },
      { txt: "«&nbsp;C'est la plus bonne du rayon, non&nbsp;? En avez-vous une plus bon "
           + "marché&nbsp;?&nbsp;»",
        rat_t: "La construction est juste. C'est l'irrégulier de l'écran 8 qui manque.",
        rat: "«&nbsp;Bon&nbsp;» ne prend jamais «&nbsp;plus&nbsp;»&nbsp;: on dit «&nbsp;<b>la "
           + "meilleure</b> du rayon&nbsp;». Et vous parliez de prix, pas de qualité&nbsp;: "
           + "«&nbsp;la moins chère&nbsp;» dit exactement ce que vous vouliez dire." },
    ],
    pourquoi: "Vous avez fait les trois choses&nbsp;: reconnaître qu'un groupe était derrière, "
            + "poser l'article, et nommer le groupe avec «&nbsp;de&nbsp;».",
    attente: "Choisissez une réponse pour finir.",
  },

];
