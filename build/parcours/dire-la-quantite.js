// ═══════════════════════════════════════════════════════════════════════════
// Point express — Dire la quantité : beaucoup de, un peu de, assez de
//
// Savoir n3-s20. Une ORDONNANCE : l'enseignant l'envoie à un élève chez qui il
// a entendu « beaucoup des pommes », ou qui n'a pas compris « assez de
// places ». Dix minutes, dix écrans, une seule difficulté.
//
// ── Ce dont il s'écarte, et comment ────────────────────────────────────────
// Trois mini-leçons du dépôt touchent déjà le sujet :
//   · `module-n3-voisins` — « Très, assez, un peu, trop » : quatre degrés
//     DEVANT UN ADJECTIF. Elle range « trop de place » dans une note de bas de
//     bloc, en une ligne. Ici, c'est l'inverse : le nom est le sujet entier, et
//     l'adjectif n'apparaît qu'à l'écran 8, comme piège.
//   · `module-alimentation` — « La liaison des quantités » : la prononciation
//     de deux, trois, six devant une voyelle. Elle ne dit rien de « de ».
//   · `module-n3-pharmacie` — « De plus de, de moins de, pas plus de » : les
//     bornes chiffrées d'une posologie, pas les déterminants.
//
// Les cinq écarts tenus :
//   1. INDUCTIF. Aucune règle avant l'écran 4. L'élève range huit cas d'abord ;
//      la règle est ensuite écrite comme un constat de ce qu'il vient de faire.
//   2. PARTIEL. Jamais la liste des déterminants. Un seul TEST — « est-ce
//      qu'un mot de quantité vient juste avant ? » — qui marche sur un mot
//      qu'on n'a jamais vu.
//   3. LE CAS PAR DÉFAUT EN DERNIER. « des · du · de la » n'est nommé qu'à
//      l'écran 4, une fois « de » isolé. Le nommer d'entrée ferait croire à
//      deux règles concurrentes.
//   4. AUCUNE PHRASE REPRISE d'une mini-leçon, et des exemples pris à plusieurs
//      endroits : un comptoir, une épicerie, une salle de classe, un texto.
//   5. LE MÉTALANGAGE APRÈS. « Déterminant » n'est jamais écrit ; « mot de
//      quantité » suffit et se réemploie.
//
// Extraits : ceux de `module-n3-restaurant`, rejoués par chemin. Aucun média
// neuf. Les rangs sont ceux de `dialogues.js` et les textes en sont recopiés.
// ═══════════════════════════════════════════════════════════════════════════

const PARCOURS = {
  slug:     'dire-la-quantite',
  module:   'module-n3-restaurant',   // d'où viennent les extraits, rien de plus
  titre:    "Dire la quantité : beaucoup de, un peu de, assez de",
  surtitre: "Point express · 10 minutes",
  niveau:   3,
  savoir:   'n3-s20',
};

const ECRANS = [

  // ── 1. On tranche AVANT de savoir. ───────────────────────────────────────
  {
    id:   'depart',
    type: 'verif',
    eye:  'Une question, pour commencer',
    menu: 'Deux phrases',
    titre: "Une seule de ces deux phrases se dit. Laquelle ?",
    consigne: "Répondez avec ce que vous savez déjà — ou à l'oreille. "
            + "On expliquera après&nbsp;: c'est fait exprès.",
    options: [
      { txt: "J'ai acheté beaucoup des pommes.",
        rat_t: "C'est la faute la plus fréquente, et elle a une bonne raison.",
        rat: "Vous avez appris «&nbsp;des pommes&nbsp;», et vous avez raison&nbsp;: on dit très bien "
           + "«&nbsp;j'ai acheté des pommes&nbsp;». Le problème vient du mot qu'on met devant. "
           + "Regardez l'autre phrase&nbsp;: quelque chose a disparu." },
      { txt: "J'ai acheté beaucoup de pommes.", juste: true },
      { txt: "Les deux se disent.",
        rat_t: "Une seule se dit, et l'écart s'entend.",
        rat: "On vous comprendra dans les deux cas — c'est bien le problème&nbsp;: personne ne vous "
           + "reprend. Mais «&nbsp;beaucoup des pommes&nbsp;» signale tout de suite quelqu'un qui "
           + "apprend le français." },
    ],
    pourquoi: "«&nbsp;Beaucoup <b>de</b> pommes&nbsp;». Retenez la phrase entière pour l'instant&nbsp;; "
            + "on va voir pourquoi juste après.",
    attente: "Choisissez une réponse pour continuer.",
  },

  // ── 2. On écoute. Toujours aucune règle. ─────────────────────────────────
  {
    id:   'ce-quon-entend',
    type: 'notion',
    eye:  "Ce qu'on entend vraiment",
    menu: 'Un mot minuscule',
    titre: "Le mot qui change tout dure un dixième de seconde.",
    paras: [
      "Yolette arrive devant le tableau d'un casse-croûte. Écoutez sa première phrase et "
      + "comptez ce qu'il y a <b>entre</b> «&nbsp;beaucoup&nbsp;» et «&nbsp;choses&nbsp;».",

      "Un seul son, très court. C'est pour ça que la faute traverse des années&nbsp;: à l'oral, "
      + "il n'y a presque rien à entendre, et personne ne vous corrige. Elle apparaît au moment "
      + "où vous parlez à votre tour.",
    ],
    sons: [
      { fichier: 't1/line_01_yolette.mp3', qui: 'Yolette, devant le menu du comptoir',
        texte: "Il y a beaucoup de choses écrites. Par où je commence&nbsp;?" },
    ],
    retenir: "Écoutez ce petit son après «&nbsp;beaucoup&nbsp;». Il est toujours là, et il est "
           + "toujours le même.",
    attente: "Écoutez l'extrait, puis continuez.",
  },

  // ── 3. Le cœur : huit cas, sans qu'aucune règle ait été dite. ────────────
  {
    id:   'tri-de-ou-des',
    type: 'tri',
    eye:  'À vous de trancher',
    menu: 'Huit trous',
    titre: "Huit phrases à trou. Qu'est-ce qui manque ?",
    consigne: "Aucune règle ne vous a été donnée — normal. Dites chaque phrase dans votre tête, "
            + "les deux fois, et gardez celle qui sonne juste.",
    colonnes: [
      { id: 'de',   t: 'de',                b: 'de' },
      { id: 'part', t: 'des · du · de la',  b: 'des · du · de la' },
    ],
    items: [
      { txt: "Il y a beaucoup ___ légumes au marché.", ok: 'de',
        rat: "«&nbsp;Beaucoup des légumes&nbsp;» ne se dit pas. Écoutez la place du mot&nbsp;: "
           + "il arrive juste après «&nbsp;beaucoup&nbsp;».",
        pourquoi: "Beaucoup de légumes. Après « beaucoup »." },
      { txt: "J'ai acheté ___ légumes au marché.", ok: 'part',
        rat: "Ici, rien ne vient devant&nbsp;: «&nbsp;j'ai acheté de légumes&nbsp;» ne se dit pas. "
           + "C'est la même phrase que la précédente, à un mot près — et ce mot change tout.",
        pourquoi: "J'ai acheté des légumes. Rien devant." },
      { txt: "Je mets un peu ___ lait dans mon café.", ok: 'de',
        rat: "«&nbsp;Un peu du lait&nbsp;» ne se dit pas. Regardez encore ce qui précède le trou.",
        pourquoi: "Un peu de lait. Après « un peu »." },
      { txt: "Je bois ___ lait tous les matins.", ok: 'part',
        rat: "«&nbsp;Je bois de lait&nbsp;» ne se dit pas. Le trou suit un verbe, pas un mot de "
           + "quantité.",
        pourquoi: "Je bois du lait. Rien devant." },
      { txt: "Il n'y a pas assez ___ chaises pour huit personnes.", ok: 'de',
        rat: "«&nbsp;Assez des chaises&nbsp;» ne se dit pas. C'est encore le même voisin de gauche "
           + "qui commande.",
        pourquoi: "Assez de chaises. Après « assez »." },
      { txt: "Il y a trop ___ sel dans la soupe.", ok: 'de',
        rat: "«&nbsp;Trop du sel&nbsp;» ne se dit pas. Vous en avez maintenant quatre pareils&nbsp;: "
           + "regardez ce qu'ils ont en commun.",
        pourquoi: "Trop de sel. Après « trop »." },
      { txt: "Il reste ___ soupe dans le chaudron.", ok: 'part',
        rat: "«&nbsp;Il reste de soupe&nbsp;» ne se dit pas. Rien ne vient annoncer une quantité "
           + "avant le trou.",
        pourquoi: "Il reste de la soupe. Rien devant." },
      { txt: "Combien ___ personnes viennent samedi ?", ok: 'de',
        rat: "«&nbsp;Combien des personnes&nbsp;» ne se dit pas — et pourtant «&nbsp;combien&nbsp;» "
           + "n'est pas dans la même famille que «&nbsp;beaucoup&nbsp;». C'est justement ce qui rend "
           + "la règle utile&nbsp;: elle marche sur des mots que vous n'avez pas appris ensemble.",
        pourquoi: "Combien de personnes. « Combien » demande une quantité." },
    ],
    attente: "Tranchez les huit cas pour continuer.",
  },

  // ── 4. La règle, écrite comme un constat de ce qu'il vient de faire. ─────
  {
    id:   'le-test',
    type: 'notion',
    eye:  'Ce que vous venez de faire',
    menu: 'Le test',
    titre: "Vous n'avez pas regardé le nom. Vous avez regardé le mot d'avant.",
    paras: [
      "Regardez votre colonne «&nbsp;de&nbsp;»&nbsp;: <b>beaucoup</b>, <b>un peu</b>, <b>assez</b>, "
      + "<b>trop</b>, <b>combien</b>. Cinq mots qui disent une quantité. Après chacun d'eux, il n'y "
      + "a qu'une seule chose possible, et elle ne change jamais&nbsp;: <b>de</b>.",

      "«&nbsp;De&nbsp;» ne bouge pas. Pas de «&nbsp;des&nbsp;» au pluriel, pas de «&nbsp;du&nbsp;» "
      + "au masculin, pas de «&nbsp;de la&nbsp;» au féminin. Beaucoup <b>de</b> pommes, beaucoup "
      + "<b>de</b> lait, beaucoup <b>de</b> monde, beaucoup <b>d'</b>argent — le seul changement, "
      + "c'est l'apostrophe devant une voyelle.",

      "L'autre colonne, c'est <b>tout le reste</b>, et il n'y a rien à y retenir&nbsp;: quand aucun "
      + "mot de quantité ne vient devant, on retrouve <i>des</i>, <i>du</i>, <i>de la</i>, comme "
      + "d'habitude.",

      "<b>Le test, à vous poser sur n'importe quelle phrase&nbsp;:</b> est-ce qu'un mot de quantité "
      + "vient juste avant&nbsp;? Si oui, <b>de</b> et rien d'autre.",
    ],
    retenir: "Un mot de quantité devant → <b>de</b>, toujours pareil. "
           + "Un test vaut mieux qu'une liste&nbsp;: il marche sur un mot que vous n'avez jamais vu.",
    attente: "Lisez, puis continuez.",
  },

  // ── 5. Ce qui change vraiment : le nom, pas le « de ». ───────────────────
  {
    id:   'compter-ou-pas',
    type: 'notion',
    eye: "Ce qui change, et ce qui ne change pas",
    menu: 'Ce qui se compte',
    titre: "« De » ne bouge pas. C'est le nom qui prend un s, ou pas.",
    paras: [
      "Des pommes, ça se compte&nbsp;: une, deux, dix. Du lait, non&nbsp;: on ne dit pas «&nbsp;deux "
      + "laits&nbsp;» à l'épicerie, on dit «&nbsp;deux litres de lait&nbsp;». Écoutez Yolette et "
      + "Marcel&nbsp;: le sel, le poivre, la moutarde, le ketchup ne se comptent pas non plus.",

      "Cette différence ne touche <b>pas</b> le mot «&nbsp;de&nbsp;». Beaucoup <b>de</b> pomme<b>s</b>, "
      + "beaucoup <b>de</b> lait&nbsp;: le même «&nbsp;de&nbsp;» des deux côtés. Elle touche "
      + "seulement la fin du nom — un <b>s</b> quand ça se compte, rien quand ça ne se compte pas.",
    ],
    sons: [
      { fichier: 't3/line_08_yolette.mp3', qui: 'Yolette, au bout du comptoir',
        texte: "Merci. Et est-ce que je peux avoir du sel et du poivre&nbsp;?" },
      { fichier: 't3/line_09_marcel.mp3', qui: 'Marcel, derrière le comptoir',
        texte: "Servez-vous. Il y a aussi de la moutarde et du ketchup au bout." },
    ],
    retenir: "Beaucoup <b>de</b> pommes, beaucoup <b>de</b> lait. Le «&nbsp;de&nbsp;» est le "
           + "même&nbsp;; c'est le <b>s</b> du nom qui dit si ça se compte.",
    attente: "Écoutez les deux extraits, puis continuez.",
  },

  // ── 6. Trier des noms, pas des règles. ───────────────────────────────────
  {
    id:   'tri-le-s',
    type: 'tri',
    eye: 'À vous de trancher',
    menu: 'Six noms',
    titre: "« Beaucoup de… » — lesquels prennent un s ?",
    consigne: "Une seule question à vous poser&nbsp;: est-ce que je peux en compter deux&nbsp;?",
    colonnes: [
      { id: 'esse', t: 'beaucoup de + s',      b: 'un s' },
      { id: 'sans', t: 'beaucoup de + rien',   b: 'pas de s' },
    ],
    items: [
      { txt: "beaucoup de voisin___", sous: "dans mon immeuble", ok: 'esse',
        rat: "Un voisin, deux voisins, douze voisins&nbsp;: ça se compte, donc le nom prend un s.",
        pourquoi: "Beaucoup de voisins. Ça se compte." },
      { txt: "beaucoup de sucre___", sous: "dans ce jus", ok: 'sans',
        rat: "«&nbsp;Deux sucres&nbsp;» se dit d'un morceau posé sur une soucoupe, pas de la "
           + "matière. Le sucre d'un jus ne se compte pas&nbsp;: il se pèse.",
        pourquoi: "Beaucoup de sucre. Ça se pèse, ça ne se compte pas." },
      { txt: "beaucoup de question___", sous: "à la fin du cours", ok: 'esse',
        rat: "Une question, trois questions&nbsp;: on les compte sans effort. Le nom prend un s.",
        pourquoi: "Beaucoup de questions. Ça se compte." },
      { txt: "beaucoup de travail___", sous: "cette semaine", ok: 'sans',
        rat: "«&nbsp;Des travaux&nbsp;» existe, mais c'est autre chose&nbsp;: un chantier. Le "
           + "travail qu'on a cette semaine ne se compte pas.",
        pourquoi: "Beaucoup de travail. Ça ne se compte pas." },
      { txt: "beaucoup de monde___", sous: "au comptoir ce midi", ok: 'sans',
        rat: "C'est le piège du groupe&nbsp;: «&nbsp;monde&nbsp;» désigne des personnes, mais le mot "
           + "reste au singulier. On ne dit jamais «&nbsp;beaucoup de mondes&nbsp;».",
        pourquoi: "Beaucoup de monde. Toujours au singulier." },
      { txt: "beaucoup d'erreur___", sous: "dans ma dictée", ok: 'esse',
        rat: "Une erreur, quatre erreurs&nbsp;: ça se compte. Et devant la voyelle, "
           + "«&nbsp;de&nbsp;» devient «&nbsp;d'&nbsp;» — c'est son seul changement.",
        pourquoi: "Beaucoup d'erreurs. Ça se compte." },
    ],
    attente: "Tranchez les six cas pour continuer.",
  },

  // ── 7. « Un peu », et ce qu'il refuse. ───────────────────────────────────
  {
    id:   'un-peu',
    type: 'verif',
    eye:  'Le cas qui trompe',
    menu: '« Un peu »',
    titre: "« Un peu de » ne va pas avec tout.",
    consigne: "Amina écrit à sa voisine. Quelle phrase se dit&nbsp;? "
            + "Écoutez d'abord Fatou&nbsp;: elle emploie «&nbsp;un peu&nbsp;» tout seul, sans nom "
            + "derrière — c'est possible aussi.",
    sons: [
      { fichier: 't1/line_10_fatou.mp3', qui: 'Fatou, sur le prix du trio',
        texte: "Oui, un peu. Regarde la colonne de droite et compare." },
    ],
    options: [
      { txt: "« Il me reste un peu de sucre, je peux t'en donner. »", juste: true },
      { txt: "« Il me reste un peu de œufs, je peux t'en donner. »",
        rat_t: "Des œufs, ça se compte&nbsp;: «&nbsp;un peu&nbsp;» ne marche pas.",
        rat: "«&nbsp;Un peu de&nbsp;» dit une petite <b>partie</b> d'une chose qu'on ne compte "
           + "pas&nbsp;: un peu de sucre, un peu de lait, un peu de temps. Pour ce qui se compte, "
           + "on dit <b>quelques</b>&nbsp;: quelques œufs, quelques minutes. Et devant la voyelle, "
           + "ce serait de toute façon «&nbsp;d'œufs&nbsp;»." },
      { txt: "« Il me reste un peu des sucre, je peux t'en donner. »",
        rat_t: "Deux mots là où il n'en faut qu'un.",
        rat: "Après «&nbsp;un peu&nbsp;», il n'y a jamais que <b>de</b>. Ajouter «&nbsp;des&nbsp;» "
           + "revient à écrire deux fois la même chose — et «&nbsp;des sucre&nbsp;» ne se dit pas "
           + "non plus, ni au singulier ni au pluriel." },
    ],
    pourquoi: "«&nbsp;Un peu <b>de</b> sucre&nbsp;». Pour ce qui se compte, changez de mot&nbsp;: "
            + "<b>quelques</b> œufs, <b>quelques</b> pommes. «&nbsp;Un peu&nbsp;» garde ce qui se "
            + "pèse et ce qui se verse.",
    attente: "Choisissez une réponse pour continuer.",
  },

  // ── 8. « Assez » et « trop » : ce sont eux qui décident. ─────────────────
  {
    id:   'assez-trop',
    type: 'notion',
    eye:  'Les deux qui décident',
    menu: 'Assez, trop',
    titre: "Au comptoir, « assez de » et « trop de » ne décrivent pas : ils tranchent.",
    paras: [
      "«&nbsp;Il y a assez de soupe pour deux&nbsp;» veut dire&nbsp;: n'en commande pas d'autre. "
      + "«&nbsp;Il y a trop de sel&nbsp;» veut dire&nbsp;: je ne prends pas ce format. Ce sont les "
      + "deux mots qui font changer une commande, et c'est pour ça qu'il faut les entendre du "
      + "premier coup. Écoutez&nbsp;: on vous propose trois quantités, il faut répondre tout de suite.",

      "<b>Un piège, et c'est le seul de la leçon.</b> Devant un <b>nom</b>, il faut «&nbsp;de&nbsp;»&nbsp;: "
      + "assez <b>de</b> soupe, trop <b>de</b> sel. Devant un <b>adjectif</b>, il n'y a rien du "
      + "tout&nbsp;: la soupe est assez chaude, elle est trop salée. Regardez ce qui suit avant de "
      + "choisir.",
    ],
    sons: [
      { fichier: 'prep/line_10_fatou.mp3', qui: 'Fatou explique les formats',
        texte: "Ce sont les trois formats&nbsp;: petit, moyen, grand." },
      { fichier: 't2/line_07_steve.mp3', qui: 'Steve, au comptoir',
        texte: "Oui. Quel format&nbsp;? Petit, moyen ou grand&nbsp;?" },
    ],
    retenir: "Assez <b>de</b> soupe, mais assez chaude. <b>Le «&nbsp;de&nbsp;» est là pour le nom, "
           + "jamais pour l'adjectif.</b>",
    attente: "Écoutez, puis continuez.",
  },

  // ── 9. Écrire une phrase entière, pas reconnaître un mot. ────────────────
  {
    id:   'le-message',
    type: 'verif',
    eye:  'Vérification',
    menu: 'Un message à écrire',
    titre: "Ibrahim écrit à son enseignante. Quelle version tient d'un bout à l'autre ?",
    consigne: "Trois versions du même message. Une seule est correcte partout.",
    options: [
      { txt: "« Bonjour. Il y a trop de bruit dans la classe et je n'entends pas assez bien. "
           + "Est-ce que je peux avoir quelques exemples de plus ? »", juste: true },
      { txt: "« Bonjour. Il y a trop du bruit dans la classe et je n'entends pas assez de bien. "
           + "Est-ce que je peux avoir un peu d'exemples de plus ? »",
        rat_t: "Trois fautes, et ce sont les trois du parcours.",
        rat: "«&nbsp;Trop du bruit&nbsp;»&nbsp;: après un mot de quantité, seulement <i>de</i>. "
           + "«&nbsp;Assez de bien&nbsp;»&nbsp;: «&nbsp;bien&nbsp;» n'est pas un nom, il ne prend "
           + "rien. «&nbsp;Un peu d'exemples&nbsp;»&nbsp;: des exemples, ça se compte — c'est "
           + "«&nbsp;quelques&nbsp;»." },
      { txt: "« Bonjour. Il y a beaucoup des bruits dans la classe et je n'entends pas assez. "
           + "Est-ce que je peux avoir quelques exemples de plus ? »",
        rat_t: "La fin est bonne. C'est le début qui tombe.",
        rat: "«&nbsp;Assez&nbsp;» tout seul se dit très bien&nbsp;: rien ne suit, donc rien à "
           + "ajouter. Mais «&nbsp;beaucoup des bruits&nbsp;» est exactement la phrase de l'écran 1, "
           + "avec un autre nom&nbsp;: il faut «&nbsp;beaucoup <b>de</b> bruit&nbsp;»." },
    ],
    pourquoi: "Trop <b>de</b> bruit devant un nom, assez <b>bien</b> devant un adverbe, "
            + "<b>quelques</b> exemples pour ce qui se compte. <b>C'est tout le point express en "
            + "trois lignes.</b>",
    attente: "Choisissez une réponse pour continuer.",
  },

  // ── 10. La fermeture : le cas de l'écran 1. ──────────────────────────────
  {
    id:   'fermeture',
    type: 'verif',
    eye:  'La dernière',
    menu: 'Pour finir',
    titre: "On revient au marché. Vous racontez vos achats à une amie.",
    consigne: "Vous avez pris six pommes et un litre de lait. Vous dites quoi&nbsp;?",
    options: [
      { txt: "« J'ai acheté beaucoup de pommes et un peu de lait. »", juste: true },
      { txt: "« J'ai acheté beaucoup des pommes et un peu du lait. »",
        rat_t: "Ce sont les deux phrases de l'écran 1 et de l'écran 7.",
        rat: "Après «&nbsp;beaucoup&nbsp;» comme après «&nbsp;un peu&nbsp;», il n'y a que "
           + "<b>de</b>&nbsp;: ni «&nbsp;des&nbsp;», ni «&nbsp;du&nbsp;». Le nom, lui, garde son "
           + "s quand ça se compte — pommes, oui&nbsp;; lait, non." },
      { txt: "« J'ai acheté beaucoup de pomme et un peu de laits. »",
        rat_t: "Les deux «&nbsp;de&nbsp;» sont bons. Les deux noms sont à l'envers.",
        rat: "Vous avez le plus difficile&nbsp;: le mot de quantité et son «&nbsp;de&nbsp;». Mais "
           + "six pommes se comptent — «&nbsp;pomme<b>s</b>&nbsp;» — et le lait se verse, il ne "
           + "prend pas de s." },
    ],
    pourquoi: "«&nbsp;Beaucoup <b>de</b> pommes et un peu <b>de</b> lait.&nbsp;» Vous avez fait les "
            + "deux moitiés&nbsp;: le mot invariable après la quantité, et le nom qui dit si ça "
            + "se compte.",
    attente: "Choisissez une réponse pour finir.",
  },

];
