// ═══════════════════════════════════════════════════════════════════════════
// Point express — Une maison blanche, une grande maison
//
// Savoir n2-s12 (Noms et GN : noyau et expansions). Une ORDONNANCE : l'enseignant
// l'envoie à un élève qui écrit « une blanche maison » ou « une maison grande ».
// Dix minutes, dix écrans, niveau 2.
//
// ── Ce qui le sépare des mini-leçons existantes ────────────────────────────
// Quatre mini-leçons du dépôt touchent l'adjectif, et toutes commencent par la
// règle :
//   · `module-achat` — « Où mettre l'adjectif » : la règle, puis la liste.
//   · `module-n3-vetements` — « La couleur après le vêtement » : un seul cas,
//     celui du module (les couleurs), donc rien de réutilisable ailleurs.
//   · `module-n3-voisins` et `module-n6-relations` — la place ET l'accord dans
//     la même leçon ; l'élève retient l'accord et oublie la place.
// Un élève qui a lu ces quatre-là connaît la phrase « l'adjectif se place après
// le nom » et se trompe quand même, parce qu'il ne sait pas quoi faire des six
// mots qui passent devant. Les cinq écarts tenus :
//
//   1. INDUCTIF. L'élève range huit phrases entendues AVANT qu'aucune règle ne
//      soit écrite. La règle de l'écran 3 est le constat de son tri.
//   2. PARTIEL, JAMAIS LA LISTE. Pas de tableau des adjectifs antéposés. Un
//      TEST — le mot est-il court et très courant ? — plus SIX mots à
//      reconnaître, et rien d'autre.
//   3. LE CAS PAR DÉFAUT (l'adjectif derrière) EST DIT EN PREMIER dans le
//      constat, mais les six mots de devant sont manipulés AVANT d'être nommés.
//   4. L'ACCORD N'EST PAS TRAITÉ. C'est une autre difficulté ; la mêler ici
//      referait la mini-leçon. Les exemples sont tous au singulier masculin ou
//      portent l'accord tout fait.
//   5. EXEMPLES VARIÉS, JAMAIS CEUX D'UN MODULE. Une annonce de logement, un
//      texto, une note à l'école, une affiche d'épicerie, une petite annonce.
//
// Aucun média : la place d'un mot ne s'entend pas mieux qu'elle ne se lit, et
// tout le point tient dans l'ordre des mots écrits.
// ═══════════════════════════════════════════════════════════════════════════

const PARCOURS = {
  slug:     'place-de-l-adjectif',
  titre:    "Une maison blanche, une grande maison",
  surtitre: "Point express · 10 minutes",
  niveau:   2,
  savoir:   'n2-s12',
};

const ECRANS = [

  // ── 1. Une décision, sans aucune règle donnée. ───────────────────────────
  {
    id:   'depart',
    type: 'verif',
    eye:  'Une question, pour commencer',
    menu: 'Deux phrases',
    titre: "Vous cherchez un logement. Quelle phrase écrivez-vous ?",
    consigne: "Répondez avec ce que vous savez déjà — ou au feeling. On expliquera après&nbsp;: "
            + "c'est fait exprès.",
    options: [
      { txt: "Je cherche un grand appartement.", juste: true },
      { txt: "Je cherche un appartement grand.",
        rat_t: "Le mot est au bon endroit… pour presque tous les autres mots.",
        rat: "Vous avez appliqué la règle que vous connaissez&nbsp;: le mot qui décrit vient "
           + "après. Elle est bonne pour <b>bleu</b>, <b>propre</b>, <b>tranquille</b>. Mais "
           + "<b>grand</b> fait partie d'un tout petit groupe qui passe devant. On va voir "
           + "lequel." },
      { txt: "Je cherche un appartement de grand.",
        rat_t: "Ce «&nbsp;de&nbsp;» ne sert à rien ici.",
        rat: "On met «&nbsp;de&nbsp;» entre deux <b>noms</b>&nbsp;: une salle <b>de</b> classe, "
           + "un billet <b>d'</b>autobus. Le mot <b>grand</b> n'est pas un nom&nbsp;: il décrit "
           + "l'appartement. Il se colle au nom, sans rien entre les deux." },
    ],
    pourquoi: "La première. Gardez-la en tête&nbsp;: on y revient au dernier écran.",
    attente: "Choisissez une réponse pour continuer.",
  },

  // ── 2. On trie AVANT de savoir. ──────────────────────────────────────────
  {
    id:   'tri-place',
    type: 'tri',
    eye:  'À vous de trancher',
    menu: 'Huit phrases',
    titre: "Huit phrases correctes. Où est le mot qui décrit ?",
    consigne: "Toutes ces phrases sont justes. Regardez seulement le mot en gras&nbsp;: est-il "
            + "<b>avant</b> le nom, ou <b>après</b>&nbsp;? Aucune règle ne vous a été "
            + "donnée — c'est normal.",
    colonnes: [
      { id: 'av', t: "Avant le nom",  b: "Avant" },
      { id: 'ap', t: "Après le nom",  b: "Après" },
    ],
    items: [
      { txt: "J'habite dans une maison <b>blanche</b>.", sous: "un texto à une amie", ok: 'ap',
        rat: "Le mot <b>blanche</b> vient après «&nbsp;maison&nbsp;». C'est une couleur, et "
           + "les couleurs se placent toujours après le nom.",
        pourquoi: "Une maison blanche. Le mot vient après." },
      { txt: "C'est une <b>petite</b> chambre.", sous: "une annonce de logement", ok: 'av',
        rat: "Le mot <b>petite</b> vient avant «&nbsp;chambre&nbsp;». Regardez sa longueur&nbsp;: "
           + "c'est un mot court, et vous l'employez tous les jours.",
        pourquoi: "Une petite chambre. Le mot vient avant." },
      { txt: "Le cours commence à la <b>première</b> heure.", sous: "une note de l'école", ok: 'av',
        rat: "<b>Première</b> vient avant «&nbsp;heure&nbsp;». Les mots qui comptent — premier, "
           + "deuxième, dernier — passent tous devant.",
        pourquoi: "La première heure. Le mot vient avant." },
      { txt: "J'ai acheté une table <b>ronde</b>.", sous: "un message à sa sœur", ok: 'ap',
        rat: "<b>Ronde</b> vient après «&nbsp;table&nbsp;». C'est une forme, comme une couleur "
           + "ou une matière&nbsp;: ça se place après.",
        pourquoi: "Une table ronde. Le mot vient après." },
      { txt: "Nous avons un <b>beau</b> jardin.", sous: "une petite annonce", ok: 'av',
        rat: "<b>Beau</b> vient avant «&nbsp;jardin&nbsp;». Encore un mot court et très courant.",
        pourquoi: "Un beau jardin. Le mot vient avant." },
      { txt: "C'est un quartier <b>tranquille</b>.", sous: "une annonce de logement", ok: 'ap',
        rat: "<b>Tranquille</b> vient après «&nbsp;quartier&nbsp;». Comptez ses syllabes&nbsp;: "
           + "c'est un mot long. Les mots longs restent derrière.",
        pourquoi: "Un quartier tranquille. Le mot vient après." },
      { txt: "Voici mon <b>nouveau</b> numéro.", sous: "un courriel à l'école", ok: 'av',
        rat: "<b>Nouveau</b> vient avant «&nbsp;numéro&nbsp;». Il est dans le même petit groupe "
           + "que <i>petit</i>, <i>grand</i> et <i>beau</i>.",
        pourquoi: "Mon nouveau numéro. Le mot vient avant." },
      { txt: "Je prends l'autobus <b>vert</b>.", sous: "au comptoir d'un centre", ok: 'ap',
        rat: "<b>Vert</b> vient après «&nbsp;autobus&nbsp;». Une couleur, donc derrière — même "
           + "quand le mot est court.",
        pourquoi: "L'autobus vert. Le mot vient après." },
    ],
    attente: "Tranchez les huit phrases pour continuer.",
  },

  // ── 3. La règle, écrite comme un constat. ────────────────────────────────
  {
    id:   'le-constat',
    type: 'notion',
    eye:  'Ce que vous venez de faire',
    menu: 'La règle',
    titre: "Votre colonne « après » est la grosse. Celle d'avant est toute petite.",
    paras: [
      "C'est exactement ça, la règle&nbsp;: <b>le mot qui décrit se met après le nom</b>. Une "
      + "maison blanche, une table ronde, un quartier tranquille, un autobus vert. C'est le cas "
      + "de presque tous les mots.",

      "Regardez maintenant votre petite colonne&nbsp;: <b>petite</b>, <b>première</b>, "
      + "<b>beau</b>, <b>nouveau</b>. Ce sont des mots <b>courts</b>, que vous employez tous les "
      + "jours. Il y en a environ six, et vous les connaissez déjà.",

      "Le mot qui décrit s'appelle un <b>adjectif</b>. Votre enseignant emploiera ce mot-là. "
      + "Vous n'en avez pas besoin pour écrire juste.",
    ],
    retenir: "Après le nom, presque toujours. <b>Six petits mots</b> passent devant.",
    attente: "Lisez, puis continuez.",
  },

  // ── 4. Les six mots, nommés une fois. ────────────────────────────────────
  {
    id:   'les-six',
    type: 'notion',
    eye:  'Le petit groupe',
    menu: 'Six mots',
    titre: "Six mots passent devant. Les voici, et il n'y en a pas d'autres à retenir.",
    paras: [
      "<b>grand</b> · <b>petit</b> · <b>beau</b> · <b>bon</b> · <b>jeune</b> · "
      + "<b>nouveau</b>&nbsp;— plus les mots qui comptent&nbsp;: <b>premier</b>, "
      + "<b>deuxième</b>, <b>dernier</b>.",

      "Un grand appartement. Une petite chambre. Un beau jardin. Un bon prix. Un jeune homme. "
      + "Mon nouveau numéro. Le dernier autobus.",

      "Si le mot n'est pas dans cette liste, mettez-le <b>après</b> le nom. Ça marche même sur "
      + "un mot que vous n'avez jamais vu&nbsp;: vous n'avez pas besoin de le connaître pour "
      + "savoir où le poser.",
    ],
    retenir: "Six mots devant. <b>Tout le reste derrière</b>, même les mots inconnus.",
    attente: "Lisez, puis continuez.",
  },

  // ── 5. Le piège du mot long. ─────────────────────────────────────────────
  {
    id:   'le-mot-long',
    type: 'verif',
    eye:  'Le piège',
    menu: 'Un mot inconnu',
    titre: "Vous ne connaissez pas le mot « chauffé ». Où le mettez-vous ?",
    consigne: "Vous écrivez une annonce pour sous-louer votre logement. Vous voulez dire que le "
            + "chauffage est compris.",
    options: [
      { txt: "Je loue un appartement chauffé.", juste: true },
      { txt: "Je loue un chauffé appartement.",
        rat_t: "Vous avez mis le mot devant, comme «&nbsp;grand&nbsp;».",
        rat: "<b>Chauffé</b> n'est pas dans les six mots. Vous ne le connaissez peut-être pas, "
           + "et c'est justement pour ça que le test marche&nbsp;: pas dans la liste, donc "
           + "<b>derrière</b>." },
      { txt: "Je loue un appartement de chauffé.",
        rat_t: "Encore ce «&nbsp;de&nbsp;» qui ne sert à rien.",
        rat: "Rien ne se met entre le nom et le mot qui le décrit. On écrit «&nbsp;un "
           + "appartement chauffé&nbsp;», comme «&nbsp;une maison blanche&nbsp;»." },
    ],
    pourquoi: "Vous n'avez pas eu besoin de savoir ce que le mot veut dire. <b>Pas dans les six, "
            + "donc derrière.</b>",
    attente: "Choisissez une réponse pour continuer.",
  },

  // ── 6. Trier des phrases écrites. ────────────────────────────────────────
  {
    id:   'tri-ecrites',
    type: 'tri',
    eye:  'À vous de trancher',
    menu: 'Six phrases',
    titre: "Six phrases écrites. Lesquelles sont correctes ?",
    consigne: "Une seule question à vous poser&nbsp;: le mot est-il dans les six&nbsp;? Si oui, "
            + "il va devant. Sinon, derrière.",
    colonnes: [
      { id: 'ok',   t: 'Correct',   b: 'Correct' },
      { id: 'faux', t: 'Une faute', b: 'Une faute' },
    ],
    items: [
      { txt: "J'ai trouvé un travail intéressant.", ok: 'ok',
        rat: "<b>Intéressant</b> n'est pas dans les six, et il est derrière. C'est juste.",
        pourquoi: "Pas dans les six, donc derrière. Juste." },
      { txt: "Elle habite dans une rue calme.", ok: 'ok',
        rat: "<b>Calme</b> n'est pas dans les six. Il est derrière «&nbsp;rue&nbsp;». C'est juste.",
        pourquoi: "Pas dans les six, donc derrière. Juste." },
      { txt: "C'est un appartement petit.", ok: 'faux',
        rat: "<b>Petit</b> est dans les six&nbsp;: il passe devant. On écrit «&nbsp;un petit "
           + "appartement&nbsp;».",
        pourquoi: "Il faut « un petit appartement »." },
      { txt: "Mon fils va à la nouvelle école.", ok: 'ok',
        rat: "<b>Nouvelle</b> est dans les six, et elle est devant. C'est juste.",
        pourquoi: "« Nouveau » est dans les six. Juste." },
      { txt: "Je prends le rouge autobus.", ok: 'faux',
        rat: "Une couleur ne passe jamais devant, même quand le mot est court. On écrit "
           + "«&nbsp;l'autobus rouge&nbsp;».",
        pourquoi: "Il faut « l'autobus rouge »." },
      { txt: "Il cherche un bon prix.", ok: 'ok',
        rat: "<b>Bon</b> est dans les six. Devant, donc correct.",
        pourquoi: "« Bon » est dans les six. Juste." },
    ],
    attente: "Tranchez les six phrases pour continuer.",
  },

  // ── 7. Deux mots à la fois. ──────────────────────────────────────────────
  {
    id:   'deux-mots',
    type: 'verif',
    eye:  'Vérification',
    menu: 'Deux mots',
    titre: "Vous voulez dire deux choses sur le même logement.",
    consigne: "L'appartement est <b>grand</b>, et il est <b>propre</b>. Vous écrivez une annonce. "
            + "Quelle phrase&nbsp;?",
    options: [
      { txt: "C'est un grand appartement propre.", juste: true },
      { txt: "C'est un grand propre appartement.",
        rat_t: "Vous avez mis les deux mots du même côté.",
        rat: "Chaque mot garde sa place à lui. <b>Grand</b> est dans les six, il passe devant. "
           + "<b>Propre</b> n'y est pas, il reste derrière. Un mot de chaque côté du nom." },
      { txt: "C'est un appartement grand et propre.",
        rat_t: "Cette phrase se comprend, mais elle n'est pas ce qui s'écrit.",
        rat: "«&nbsp;Et&nbsp;» réunit deux mots de la <b>même</b> place. Or ces deux-là n'ont "
           + "pas la même place. On écrit «&nbsp;un grand appartement propre&nbsp;» — ou, si "
           + "vous préférez «&nbsp;et&nbsp;»&nbsp;: «&nbsp;l'appartement est grand et "
           + "propre&nbsp;»." },
    ],
    pourquoi: "Chaque mot suit sa propre règle. <b>Grand devant, propre derrière.</b>",
    attente: "Choisissez une réponse pour continuer.",
  },

  // ── 8. Ce qui reste, et qu'on ne demande pas de retenir. ─────────────────
  {
    id:   'ce-qui-reste',
    type: 'notion',
    eye:  'Ce qui reste',
    menu: 'Pour plus tard',
    titre: "Quelques mots changent de sens selon leur place. Ce n'est pas pour aujourd'hui.",
    paras: [
      "«&nbsp;Un <b>grand</b> homme&nbsp;» n'est pas «&nbsp;un homme <b>grand</b>&nbsp;». Le "
      + "premier est important, le second mesure deux mètres. Vous rencontrerez ça, et vous n'avez "
      + "rien à en faire maintenant.",

      "Pourquoi le dire, alors&nbsp;? Pour que vous ne pensiez pas avoir mal compris le jour où "
      + "vous verrez un de ces mots des deux côtés. <b>Ce n'est pas une faute&nbsp;: c'est une "
      + "autre phrase.</b>",

      "Aujourd'hui, une seule chose compte&nbsp;: les six mots devant, tout le reste derrière.",
    ],
    retenir: "Vous écrirez juste dans presque tous les cas avec <b>une seule règle et six mots</b>.",
    attente: "Lisez, puis continuez.",
  },

  // ── 9. Écrire, pas reconnaître. ──────────────────────────────────────────
  {
    id:   'votre-message',
    type: 'verif',
    eye:  'Vérification',
    menu: 'Votre message',
    titre: "Oksana écrit à son enseignante. Quelle version tient d'un bout à l'autre ?",
    consigne: "Elle a déménagé. Elle décrit son nouveau logement en deux phrases.",
    options: [
      { txt: "J'ai un nouveau logement. C'est un petit appartement tranquille.", juste: true },
      { txt: "J'ai un logement nouveau. C'est un petit appartement tranquille.",
        rat_t: "La deuxième phrase est parfaite. C'est la première qui a lâché.",
        rat: "<b>Nouveau</b> est dans les six&nbsp;: il passe devant. On écrit «&nbsp;un nouveau "
           + "logement&nbsp;». Vous aviez la règle&nbsp;; elle s'est perdue sur le premier mot." },
      { txt: "J'ai un nouveau logement. C'est un tranquille appartement petit.",
        rat_t: "Vous avez inversé les deux mots de la seconde phrase.",
        rat: "<b>Tranquille</b> n'est pas dans les six&nbsp;: derrière. <b>Petit</b> y est&nbsp;: "
           + "devant. Vous avez fait exactement l'inverse&nbsp;: «&nbsp;un petit appartement "
           + "tranquille&nbsp;»." },
    ],
    pourquoi: "Un nouveau logement, un petit appartement tranquille. <b>Les trois mots sont à "
            + "leur place.</b>",
    attente: "Choisissez une réponse pour continuer.",
  },

  // ── 10. La fermeture : le cas de l'écran 1. ──────────────────────────────
  {
    id:   'fermeture',
    type: 'verif',
    eye:  'La dernière',
    menu: 'Pour finir',
    titre: "On revient au début : « Je cherche un grand appartement. »",
    consigne: "Cette fois, vous ajoutez une chose&nbsp;: vous le voulez <b>meublé</b>. "
            + "Qu'écrivez-vous&nbsp;?",
    options: [
      { txt: "Je cherche un grand appartement meublé.", juste: true },
      { txt: "Je cherche un grand meublé appartement.",
        rat_t: "Vous avez rangé le nouveau mot avec l'ancien.",
        rat: "<b>Meublé</b> n'est pas dans les six. Il ne rejoint donc pas «&nbsp;grand&nbsp;» "
           + "devant le nom&nbsp;: il se met derrière. Un mot de chaque côté, comme à l'écran "
           + "des deux mots." },
      { txt: "Je cherche un appartement grand meublé.",
        rat_t: "Vous avez tout mis derrière, ce qui est le bon réflexe… sauf pour six mots.",
        rat: "<b>Meublé</b> est bien placé. <b>Grand</b>, lui, est dans les six&nbsp;: il passe "
           + "devant. «&nbsp;Un grand appartement meublé&nbsp;»." },
    ],
    pourquoi: "Vous avez fait les deux choses&nbsp;: reconnaître les six mots qui passent devant, "
            + "et mettre tout le reste derrière — même un mot que vous ne connaissiez pas.",
    attente: "Choisissez une réponse pour finir.",
  },

];
