// ═══════════════════════════════════════════════════════════════════════════
// Point express — « Sa voiture », même quand c'est un homme
//
// Savoir n1-s09 (Déterminants non quantifiants possessifs). Une ORDONNANCE :
// l'enseignant l'envoie à l'élève qui dit « son carte » parce qu'il parle d'une
// femme, ou « ma nom ». Dix minutes, dix écrans, niveau 1.
//
// ── Ce qui le sépare des mini-leçons existantes ────────────────────────────
// Quatre mini-leçons du dépôt touchent les possessifs, et les quatre font la
// même chose : elles opposent DEUX PERSONNES au comptoir.
//   · `module-n2-inscription`, « Mon, ma, mes — votre, vos » : la secrétaire
//     dit « votre », l'élève dit « mon ».
//   · `module-n3-pharmacie`, même titre : le pharmacien dit « votre », l'élève
//     dit « mon ».
//   · `module-n2-colis`, « Mon nom, votre nom ».
//   · `module-n3-secretariat`, « Mon billet, votre dossier ».
// Résultat : un élève qui les a lues croit que le petit mot dépend de QUI PARLE.
// Il dit alors « son voiture » pour un homme et « sa dossier » pour une femme —
// exactement la faute que ce point vient corriger. Aucune des quatre ne traite
// « son / sa », qui est pourtant au programme du niveau 1. Les cinq écarts :
//
//   1. INDUCTIF. L'élève range huit objets d'un sac AVANT qu'on lui dise
//      pourquoi. La règle de l'écran 3 est écrite comme un constat : il a
//      regardé le mot d'après, pas la personne.
//   2. PARTIEL, JAMAIS LA LISTE. Pas de tableau des huit possessifs. Un TEST
//      unique — remplacer le petit mot par « un / une / des » — qui marche sur
//      un nom jamais vu, et qui réemploie ce que l'élève sait déjà du genre.
//   3. « VOTRE » EST DIT EN DERNIER (écran 8), alors que c'est le mot que les
//      quatre mini-leçons donnent en premier. C'est le cas facile : une seule
//      forme. Le nommer d'entrée fait croire à deux règles.
//   4. LE MÉTALANGAGE APRÈS. « Masculin, féminin, pluriel » n'arrivent qu'à
//      l'écran 3, une fois huit cas triés.
//   5. EXEMPLES VARIÉS, JAMAIS CEUX D'UN MODULE. Un sac, une voisine, un texto
//      à un frère, un formulaire. Ni pharmacie, ni secrétariat, ni colis.
//
// Aucun média. La faute ne s'entend pas dans le nom, elle se voit dans le petit
// mot devant : tout se corrige par comparaison de chaînes, et le parcours
// tourne dans un centre sans assistance.
// ═══════════════════════════════════════════════════════════════════════════

const PARCOURS = {
  slug:     'mon-ma-mes',
  titre:    "« Sa voiture », même quand c'est un homme",
  surtitre: "Point express · 10 minutes",
  niveau:   1,
  savoir:   'n1-s09',
};

const ECRANS = [

  // ── 1. Une décision, sans aucune règle donnée. ───────────────────────────
  {
    id:   'depart',
    type: 'verif',
    eye:  'Une question, pour commencer',
    menu: 'La voiture de Marc',
    titre: "Marc est un homme. Il parle de sa voiture. Il dit quoi ?",
    consigne: "Répondez avec ce que vous savez déjà — ou au feeling. On expliquera après&nbsp;: "
            + "c'est fait exprès.",
    options: [
      { txt: "«&nbsp;<b>Sa</b> voiture est bleue.&nbsp;»", juste: true },
      { txt: "«&nbsp;<b>Son</b> voiture est bleue.&nbsp;»",
        rat_t: "Marc est un homme — c'est exactement pour ça que c'est tentant.",
        rat: "Vous avez regardé <b>Marc</b>. Mais le petit mot ne parle pas de Marc&nbsp;: il parle "
           + "de la <b>voiture</b>. Et on dit «&nbsp;<b>une</b> voiture&nbsp;». C'est tout le point "
           + "de ce parcours." },
      { txt: "Les deux se disent, ça dépend de la personne.",
        rat_t: "C'est ce que beaucoup d'élèves croient, et c'est faux.",
        rat: "En français, la personne qui possède ne change <b>jamais</b> la fin du petit mot. "
           + "Un homme et une femme disent tous les deux «&nbsp;sa voiture&nbsp;»." },
    ],
    pourquoi: "<b>Sa</b> voiture. Gardez cette phrase en tête&nbsp;: on y revient à la fin.",
    attente: "Choisissez une réponse pour continuer.",
  },

  // ── 2. On trie AVANT de savoir. C'est ici que le point se sépare. ────────
  {
    id:   'tri-mon-sac',
    type: 'tri',
    eye:  'À vous de trancher',
    menu: 'Dans mon sac',
    titre: "Huit choses dans votre sac. Vous dites mon, ma, ou mes ?",
    consigne: "Aucune règle ne vous a été donnée — normal. Dites chaque phrase à voix basse&nbsp;: "
            + "celle qui sonne bien est presque toujours la bonne.",
    colonnes: [
      { id: 'mon', t: "mon", b: "mon" },
      { id: 'ma',  t: "ma",  b: "ma" },
      { id: 'mes', t: "mes", b: "mes" },
    ],
    items: [
      { txt: "… cahier", sous: "un cahier", ok: 'mon',
        rat: "On dit «&nbsp;<b>un</b> cahier&nbsp;». Alors on dit «&nbsp;<b>mon</b> cahier&nbsp;». "
           + "Le petit mot suit le mot d'après.",
        pourquoi: "un cahier → mon cahier" },
      { txt: "… carte", sous: "une carte", ok: 'ma',
        rat: "On dit «&nbsp;<b>une</b> carte&nbsp;». Alors c'est «&nbsp;<b>ma</b> carte&nbsp;», que "
           + "vous soyez un homme ou une femme.",
        pourquoi: "une carte → ma carte" },
      { txt: "… clés", sous: "plusieurs clés", ok: 'mes',
        rat: "Il y en a plusieurs. Dès qu'il y en a plusieurs, c'est "
           + "«&nbsp;<b>mes</b>&nbsp;» — et on n'a plus à se demander si le mot est masculin ou "
           + "féminin.",
        pourquoi: "plusieurs → mes clés" },
      { txt: "… téléphone", sous: "un téléphone", ok: 'mon',
        rat: "Le mot finit par «&nbsp;e&nbsp;», et pourtant on dit «&nbsp;<b>un</b> "
           + "téléphone&nbsp;». Donc «&nbsp;<b>mon</b> téléphone&nbsp;».",
        pourquoi: "un téléphone → mon téléphone" },
      { txt: "… bouteille d'eau", sous: "une bouteille", ok: 'ma',
        rat: "«&nbsp;<b>Une</b> bouteille&nbsp;»&nbsp;: le petit mot suit, et donne "
           + "«&nbsp;<b>ma</b> bouteille&nbsp;».",
        pourquoi: "une bouteille → ma bouteille" },
      { txt: "… papiers", sous: "plusieurs papiers", ok: 'mes',
        rat: "Plusieurs papiers&nbsp;: «&nbsp;<b>mes</b> papiers&nbsp;». C'est le mot qu'on vous "
           + "demandera souvent au comptoir.",
        pourquoi: "plusieurs → mes papiers" },
      { txt: "… crayon", sous: "un crayon", ok: 'mon',
        rat: "«&nbsp;<b>Un</b> crayon&nbsp;» → «&nbsp;<b>mon</b> crayon&nbsp;». Toujours le même "
           + "chemin&nbsp;: on regarde le mot d'après.",
        pourquoi: "un crayon → mon crayon" },
      { txt: "… photo", sous: "une photo", ok: 'ma',
        rat: "On dit «&nbsp;<b>une</b> photo&nbsp;», même si le mot est court et finit par "
           + "«&nbsp;o&nbsp;». Donc «&nbsp;<b>ma</b> photo&nbsp;».",
        pourquoi: "une photo → ma photo" },
    ],
    attente: "Tranchez les huit choses pour continuer.",
  },

  // ── 3. La règle, écrite comme un constat de ce qu'il vient de faire. ─────
  {
    id:   'le-test',
    type: 'notion',
    eye:  'Ce que vous venez de faire',
    menu: 'Le test',
    titre: "Vous n'avez pas regardé qui possède. Vous avez regardé le mot d'après.",
    paras: [
      "Personne ne vous a demandé si vous êtes un homme ou une femme. Ça n'aurait rien changé. "
      + "Ce qui a décidé, à chaque fois, c'est le mot placé <b>après</b> le petit mot&nbsp;: un "
      + "cahier, une carte, des clés.",

      "<b>Le test, à faire sur n'importe quel mot&nbsp;:</b> remplacez le petit mot par "
      + "«&nbsp;un&nbsp;», «&nbsp;une&nbsp;» ou «&nbsp;des&nbsp;». Si vous dites <b>un</b> sac, "
      + "c'est <b>mon</b> sac. Si vous dites <b>une</b> carte, c'est <b>ma</b> carte. Si vous dites "
      + "<b>des</b> clés, c'est <b>mes</b> clés.",

      "C'est pour ça qu'il faut apprendre chaque mot avec son «&nbsp;un&nbsp;» ou son "
      + "«&nbsp;une&nbsp;»&nbsp;: ce travail-là, vous le faites une fois, et il vous sert ici "
      + "aussi. On dit qu'un mot est <b>masculin</b> (un), <b>féminin</b> (une) ou <b>pluriel</b> "
      + "(des).",
    ],
    retenir: "Un sac → <b>mon</b> sac. Une carte → <b>ma</b> carte. Des clés → <b>mes</b> clés. "
           + "La personne qui possède ne change rien.",
    attente: "Lisez, puis continuez.",
  },

  // ── 4. Le piège : une femme qui parle d'un homme. ────────────────────────
  {
    id:   'le-frere-de-julie',
    type: 'verif',
    eye:  'Le piège',
    menu: 'Le frère de Julie',
    titre: "Julie est une femme. Elle parle de son frère. Elle dit quoi ?",
    consigne: "Attention&nbsp;: il y a deux personnes dans cette phrase, et une seule décide.",
    options: [
      { txt: "«&nbsp;<b>Mon</b> frère travaille le samedi.&nbsp;»", juste: true },
      { txt: "«&nbsp;<b>Ma</b> frère travaille le samedi.&nbsp;»",
        rat_t: "Julie est une femme — c'est le même piège qu'au début, à l'envers.",
        rat: "Vous avez regardé Julie. Mais le mot d'après est «&nbsp;frère&nbsp;», et on dit "
           + "«&nbsp;<b>un</b> frère&nbsp;». Donc «&nbsp;<b>mon</b> frère&nbsp;». Une femme dit "
           + "«&nbsp;mon frère&nbsp;» et un homme dit «&nbsp;ma sœur&nbsp;»." },
      { txt: "«&nbsp;<b>Mes</b> frère travaille le samedi.&nbsp;»",
        rat_t: "«&nbsp;Mes&nbsp;» existe, mais pas ici.",
        rat: "«&nbsp;Mes&nbsp;» sert quand il y en a <b>plusieurs</b>&nbsp;: mes frères, mes "
           + "sœurs, mes papiers. Ici, Julie parle d'un seul frère — et le verbe le dit aussi&nbsp;: "
           + "«&nbsp;travaille&nbsp;»." },
    ],
    pourquoi: "<b>Mon</b> frère. Un homme dit «&nbsp;ma sœur&nbsp;»&nbsp;; une femme dit "
            + "«&nbsp;mon frère&nbsp;». Le mot d'après décide, toujours.",
    attente: "Choisissez une réponse pour continuer.",
  },

  // ── 5. Les autres personnes : le début change, la fin obéit au même mot. ─
  {
    id:   'debut-et-fin',
    type: 'notion',
    eye: "L'autre moitié du mot",
    menu: 'Le début du mot',
    titre: "La personne change le début. Le mot d'après change la fin.",
    paras: [
      "Jusqu'ici vous parliez de vous&nbsp;: <b>m</b>on, <b>m</b>a, <b>m</b>es. Pour parler de "
      + "quelqu'un d'autre, vous changez seulement la <b>première lettre</b>&nbsp;: "
      + "<b>s</b>on, <b>s</b>a, <b>s</b>es. Et pour tutoyer une personne&nbsp;: <b>t</b>on, "
      + "<b>t</b>a, <b>t</b>es.",

      "La fin, elle, ne bouge pas pour les mêmes raisons qu'avant. Un sac&nbsp;: mon sac, ton sac, "
      + "son sac. Une carte&nbsp;: ma carte, ta carte, sa carte. Des clés&nbsp;: mes clés, tes "
      + "clés, ses clés.",

      "Autrement dit, il n'y a <b>qu'une seule chose</b> à décider&nbsp;: le début, c'est de qui on "
      + "parle&nbsp;; la fin, c'est le mot qui suit. Les deux ne se mélangent jamais.",
    ],
    retenir: "<b>m</b>- c'est à moi · <b>t</b>- c'est à toi · <b>s</b>- c'est à lui ou à elle. "
           + "Et -on / -a / -es se décident sur le mot d'après.",
    attente: "Lisez, puis continuez.",
  },

  // ── 6. Le seul cas qui semble contredire la règle. ───────────────────────
  {
    id:   'mon-adresse',
    type: 'verif',
    eye: "Un cas à part",
    menu: 'Mon adresse',
    titre: "Ana remplit un formulaire. Elle écrit son adresse. Elle écrit quoi ?",
    consigne: "On dit «&nbsp;<b>une</b> adresse&nbsp;». Alors, le petit mot devrait être "
            + "«&nbsp;ma&nbsp;»… et pourtant.",
    options: [
      { txt: "«&nbsp;<b>Mon</b> adresse, c'est 12, rue Papineau.&nbsp;»", juste: true },
      { txt: "«&nbsp;<b>Ma</b> adresse, c'est 12, rue Papineau.&nbsp;»",
        rat_t: "Vous avez appliqué la règle. Elle est bonne — et ce mot fait exception.",
        rat: "Le mot commence par une <b>voyelle</b> (a, e, i, o, u). Deux voyelles collées, "
           + "«&nbsp;ma-adresse&nbsp;», sont trop difficiles à dire&nbsp;: on met "
           + "«&nbsp;<b>mon</b>&nbsp;» à la place. Pareil pour «&nbsp;mon école&nbsp;», "
           + "«&nbsp;mon amie&nbsp;»." },
      { txt: "«&nbsp;<b>Mes</b> adresse, c'est 12, rue Papineau.&nbsp;»",
        rat_t: "Une seule adresse, un seul petit mot.",
        rat: "«&nbsp;Mes&nbsp;» veut dire plusieurs. Ana n'a qu'une adresse. Le vrai piège de "
           + "cette phrase est ailleurs&nbsp;: le mot commence par une voyelle." },
    ],
    pourquoi: "<b>Mon</b> adresse — et le mot reste féminin&nbsp;: on écrit «&nbsp;mon "
            + "<b>nouvelle</b> adresse&nbsp;» au féminin. Devant a, e, i, o, u&nbsp;: mon, ton, "
            + "son.",
    attente: "Choisissez une réponse pour continuer.",
  },

  // ── 7. Trier des phrases écrites. ────────────────────────────────────────
  {
    id:   'tri-phrases',
    type: 'tri',
    eye:  'À vous de trancher',
    menu: 'Six phrases',
    titre: "Six phrases. Lesquelles sont correctes ?",
    consigne: "Ne regardez pas la personne qui parle. Regardez seulement le mot juste "
            + "après le petit mot.",
    colonnes: [
      { id: 'ok',   t: 'Correct',   b: 'Correct' },
      { id: 'faux', t: 'Une faute', b: 'Une faute' },
    ],
    items: [
      { txt: "Paul cherche sa carte d'autobus.", ok: 'ok',
        rat: "Paul est un homme, et il dit «&nbsp;<b>sa</b> carte&nbsp;»&nbsp;: on dit "
           + "«&nbsp;une carte&nbsp;». La phrase est juste.",
        pourquoi: "une carte → sa carte" },
      { txt: "Ma nom est Ibrahim.", ok: 'faux',
        rat: "On dit «&nbsp;<b>un</b> nom&nbsp;». Donc «&nbsp;<b>mon</b> nom&nbsp;». C'est la "
           + "faute qu'on entend le plus souvent au comptoir.",
        pourquoi: "Il faut « mon nom »." },
      { txt: "Ma voisine a perdu ses clés.", ok: 'ok',
        rat: "«&nbsp;Une voisine&nbsp;» → «&nbsp;ma voisine&nbsp;». Et plusieurs clés → "
           + "«&nbsp;ses clés&nbsp;». Les deux petits mots sont justes.",
        pourquoi: "ma voisine · ses clés" },
      { txt: "Son sœur travaille à l'hôpital.", ok: 'faux',
        rat: "On dit «&nbsp;<b>une</b> sœur&nbsp;»&nbsp;: donc «&nbsp;<b>sa</b> sœur&nbsp;», même "
           + "si la personne qui possède est un homme.",
        pourquoi: "Il faut « sa sœur »." },
      { txt: "Mon école est fermée aujourd'hui.", ok: 'ok',
        rat: "«&nbsp;École&nbsp;» est féminin, mais le mot commence par une voyelle&nbsp;: c'est "
           + "«&nbsp;<b>mon</b> école&nbsp;». Et le mot reste féminin&nbsp;: «&nbsp;ferm<b>ée</b>&nbsp;».",
        pourquoi: "mon école — devant une voyelle" },
      { txt: "Mes cahier est dans mon sac.", ok: 'faux',
        rat: "Un seul cahier&nbsp;: «&nbsp;<b>mon</b> cahier&nbsp;». Le verbe le disait "
           + "déjà — «&nbsp;est&nbsp;», pas «&nbsp;sont&nbsp;».",
        pourquoi: "Il faut « mon cahier »." },
    ],
    attente: "Tranchez les six phrases pour continuer.",
  },

  // ── 8. « Votre », le cas facile, gardé pour la fin. ──────────────────────
  {
    id:   'votre-en-dernier',
    type: 'notion',
    eye:  'Ce qui reste',
    menu: 'Votre, vos',
    titre: "Le mot qu'on vous dira au comptoir n'a que deux formes.",
    paras: [
      "On a gardé celui-ci pour la fin parce qu'il est <b>facile</b>, et qu'en le disant d'abord on "
      + "vous ferait croire qu'il y a beaucoup de choses à retenir. Quand une personne vous parle "
      + "poliment, elle dit <b>votre</b> et <b>vos</b>.",

      "Et là, le genre ne change rien du tout&nbsp;: <b>votre</b> nom, <b>votre</b> carte, "
      + "<b>votre</b> adresse. Une seule forme. Ce n'est qu'au pluriel que le mot change&nbsp;: "
      + "<b>vos</b> papiers, <b>vos</b> clés.",

      "Vous l'entendrez tous les jours&nbsp;: «&nbsp;<i>Votre nom, s'il vous plaît.</i>&nbsp;» Et "
      + "vous répondrez avec l'autre série&nbsp;: «&nbsp;<i>Mon nom, c'est…</i>&nbsp;»",
    ],
    retenir: "<b>Votre</b> pour une chose, <b>vos</b> pour plusieurs. C'est la personne "
           + "en face qui l'emploie&nbsp;; vous, vous répondez avec mon, ma, mes.",
    attente: "Lisez, puis continuez.",
  },

  // ── 9. Écrire, pas reconnaître. ──────────────────────────────────────────
  {
    id:   'votre-message',
    type: 'verif',
    eye:  'Vérification',
    menu: 'Votre message',
    titre: "Vous écrivez à l'école pour votre fille. Quelle version tient d'un bout à l'autre ?",
    consigne: "Elle est malade et vous envoyez un message. Trois versions du même "
            + "message&nbsp;: une seule est correcte partout.",
    options: [
      { txt: "«&nbsp;Bonjour. Ma fille est malade. Son cours commence à 9 h&nbsp;: elle ne sera "
           + "pas là.&nbsp;»", juste: true },
      { txt: "«&nbsp;Bonjour. Mon fille est malade. Son cours commence à 9 h&nbsp;: elle ne sera "
           + "pas là.&nbsp;»",
        rat_t: "La deuxième moitié est juste. C'est le premier mot qui a lâché.",
        rat: "On dit «&nbsp;<b>une</b> fille&nbsp;», donc «&nbsp;<b>ma</b> fille&nbsp;». Attention "
           + "au piège de la voyelle&nbsp;: il ne joue que si le mot <b>commence</b> par a, e, i, o "
           + "ou u. «&nbsp;Fille&nbsp;» commence par un f." },
      { txt: "«&nbsp;Bonjour. Ma fille est malade. Sa cours commence à 9 h&nbsp;: elle ne sera "
           + "pas là.&nbsp;»",
        rat_t: "Vous avez suivi la fille. C'est justement ce qu'il ne faut pas faire.",
        rat: "Le mot d'après est «&nbsp;cours&nbsp;», et on dit «&nbsp;<b>un</b> cours&nbsp;». "
           + "Donc «&nbsp;<b>son</b> cours&nbsp;», même si le cours est celui d'une fille." },
    ],
    pourquoi: "Ma fille, son cours. <b>Deux petits mots, deux mots d'après — et jamais la "
            + "personne.</b>",
    attente: "Choisissez une réponse pour continuer.",
  },

  // ── 10. La fermeture : le même cas qu'à l'écran 1. ───────────────────────
  {
    id:   'fermeture',
    type: 'verif',
    eye:  'La dernière',
    menu: 'Pour finir',
    titre: "On revient à Marc et à sa voiture.",
    consigne: "Cette fois, Marc parle aussi de son sac et de ses papiers, dans la même phrase. "
            + "Laquelle est correcte&nbsp;?",
    options: [
      { txt: "«&nbsp;Sa voiture est bleue. Son sac et ses papiers sont dedans.&nbsp;»",
        juste: true },
      { txt: "«&nbsp;Son voiture est bleue. Son sac et ses papiers sont dedans.&nbsp;»",
        rat_t: "C'est la phrase de l'écran 1, et la fin est maintenant parfaite.",
        rat: "«&nbsp;Son sac&nbsp;» et «&nbsp;ses papiers&nbsp;» sont justes&nbsp;: vous avez "
           + "regardé le mot d'après. Il ne restait que le premier&nbsp;: une voiture → "
           + "<b>sa</b> voiture." },
      { txt: "«&nbsp;Sa voiture est bleue. Sa sac et ses papiers sont dedans.&nbsp;»",
        rat_t: "Le début est juste, et vous avez continué avec le même petit mot.",
        rat: "Chaque nom décide pour lui-même&nbsp;: une voiture → <b>sa</b> voiture, mais un "
           + "sac → <b>son</b> sac. Le petit mot se choisit à chaque fois, pas une fois pour "
           + "toute la phrase." },
    ],
    pourquoi: "Vous avez fait les trois choses&nbsp;: ignorer la personne qui possède, choisir sur "
            + "le mot d'après, et recommencer à chaque nom.",
    attente: "Choisissez une réponse pour finir.",
  },

];
