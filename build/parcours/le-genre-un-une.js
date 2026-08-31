// ═══════════════════════════════════════════════════════════════════════════
// Point express — Apprendre un mot, c'est apprendre deux mots
//
// Savoir n1-s08 (Noms et GN). Une ORDONNANCE : l'enseignant l'envoie à l'élève
// qui dit « une stylo », « un chaise », ou qui demande « pourquoi une table ? »
// Dix minutes, dix écrans, niveau 1.
//
// ── Ce qui le sépare des mini-leçons existantes ────────────────────────────
// Une seule mini-leçon du dépôt traite le genre de front : `module-n3-loyer`,
// « Un ou une : le genre des pièces ». Elle est bonne, et elle est captive de
// son module — elle enseigne le genre SUR LES PIÈCES D'UN LOGEMENT (salon,
// cuisine, balcon), puis donne des terminaisons qui « aident sans décider »
// (-on, -oir, -ier / -ine, -elle). Un élève de niveau 1 n'a pas encore de
// logement à décrire, et une liste de terminaisons est exactement ce qu'il ne
// peut pas retenir. Les cinq écarts tenus :
//
//   1. INDUCTIF. L'élève range huit mots de la salle de classe AVANT qu'on lui
//      dise quoi que ce soit. La règle de l'écran 3 est écrite comme un constat
//      de ce qu'il vient de faire : il ne les a pas devinés, il s'en est
//      souvenu.
//   2. PARTIEL, JAMAIS LA LISTE. Aucune terminaison, aucun tableau. Un seul
//      GESTE réutilisable : noter le mot avec son article, les deux ensemble,
//      toujours. Il marche sur un mot jamais vu.
//   3. LE CAS QUI CONSOLE EST DIT EN DERNIER (écran 8) : la question à poser
//      quand on ne sait pas — « on dit un ou une ? ». La nommer d'entrée ferait
//      croire qu'on peut se passer de mémoire.
//   4. LE MÉTALANGAGE APRÈS. « Masculin » et « féminin » n'arrivent qu'à
//      l'écran 3, une fois huit mots triés. Ce sont les seuls mots savants du
//      parcours, et le programme les demande (n1-s30).
//   5. EXEMPLES VARIÉS, JAMAIS CEUX D'UN MODULE. La classe, un sac, un
//      autobus, une carte, un message à l'école. Aucune phrase du module du
//      loyer, aucune pièce de logement.
//
// Aucun média. Le genre ne s'entend pas dans le nom — il s'entend dans le petit
// mot devant, et c'est le sujet même du point. Tout est écrit, tout se corrige
// par comparaison de chaînes : le parcours tourne dans un centre sans
// assistance.
// ═══════════════════════════════════════════════════════════════════════════

const PARCOURS = {
  slug:     'le-genre-un-une',
  titre:    "Apprendre un mot, c'est apprendre deux mots",
  surtitre: "Point express · 10 minutes",
  niveau:   1,
  savoir:   'n1-s08',
};

const ECRANS = [

  // ── 1. Une décision, sans aucune règle donnée. ───────────────────────────
  {
    id:   'depart',
    type: 'verif',
    eye:  'Une question, pour commencer',
    menu: 'Un mot neuf',
    titre: "Vous apprenez un mot neuf : « table ». On dit un table ou une table ?",
    consigne: "Répondez avec ce que vous savez déjà. On expliquera après&nbsp;: c'est fait exprès.",
    options: [
      { txt: "On ne peut pas le deviner. Il faut apprendre le mot avec «&nbsp;un&nbsp;» ou «&nbsp;une&nbsp;».",
        juste: true },
      { txt: "C'est «&nbsp;une&nbsp;», parce que le mot finit par «&nbsp;e&nbsp;».",
        rat_t: "Souvent vrai. Assez souvent faux pour vous tromper.",
        rat: "«&nbsp;Une table&nbsp;» est juste, oui. Mais on dit aussi «&nbsp;<b>un</b> livre&nbsp;», "
           + "«&nbsp;<b>un</b> verre&nbsp;», «&nbsp;<b>un</b> groupe&nbsp;». Le «&nbsp;e&nbsp;» de la fin "
           + "aide un peu, il ne décide pas." },
      { txt: "C'est «&nbsp;un&nbsp;», parce qu'une table est un objet.",
        rat_t: "L'objet ne dit rien du mot.",
        rat: "Une table et un bureau sont deux objets de la même salle. L'un prend "
           + "«&nbsp;une&nbsp;», l'autre prend «&nbsp;un&nbsp;». Regarder la chose ne vous aidera "
           + "jamais&nbsp;: le genre est dans le <b>mot</b>." },
    ],
    pourquoi: "On dit <b>une</b> table. Et la seule façon de le savoir, c'est de l'avoir appris. "
            + "Gardez ce mot en tête&nbsp;: on y revient à la fin.",
    attente: "Choisissez une réponse pour continuer.",
  },

  // ── 2. On trie AVANT de savoir. C'est ici que le point se sépare. ────────
  {
    id:   'tri-classe',
    type: 'tri',
    eye:  'À vous de trancher',
    menu: 'Huit mots',
    titre: "Huit mots de votre classe. Un, ou une ?",
    consigne: "Vous avez entendu ces mots des dizaines de fois. Ne réfléchissez pas trop&nbsp;: "
            + "prenez celui qui vient tout seul.",
    colonnes: [
      { id: 'un',  t: "On dit UN",  b: "un" },
      { id: 'une', t: "On dit UNE", b: "une" },
    ],
    items: [
      { txt: "stylo", sous: "pour écrire", ok: 'un',
        rat: "Votre enseignante dit «&nbsp;prenez <b>un</b> stylo&nbsp;» depuis le premier jour. "
           + "Vous l'avez entendu, même sans y penser.",
        pourquoi: "un stylo" },
      { txt: "chaise", sous: "pour s'asseoir", ok: 'une',
        rat: "«&nbsp;Prenez <b>une</b> chaise&nbsp;»&nbsp;: c'est la phrase de tous les matins. "
           + "Le mot arrive toujours avec «&nbsp;une&nbsp;».",
        pourquoi: "une chaise" },
      { txt: "cahier", sous: "pour écrire", ok: 'un',
        rat: "«&nbsp;<b>Un</b> cahier et <b>un</b> crayon&nbsp;»&nbsp;: les deux vont ensemble, et "
           + "les deux prennent «&nbsp;un&nbsp;».",
        pourquoi: "un cahier" },
      { txt: "porte", sous: "pour entrer", ok: 'une',
        rat: "«&nbsp;Fermez la porte&nbsp;», «&nbsp;il y a <b>une</b> porte au fond&nbsp;». "
           + "Le mot ne se dit jamais avec «&nbsp;un&nbsp;».",
        pourquoi: "une porte" },
      { txt: "sac", sous: "pour transporter", ok: 'un',
        rat: "«&nbsp;J'ai <b>un</b> sac&nbsp;». Ce mot-là, tout le monde l'a dit au moins une fois "
           + "en classe.",
        pourquoi: "un sac" },
      { txt: "carte", sous: "d'autobus, d'assurance", ok: 'une',
        rat: "«&nbsp;Votre carte, s'il vous plaît&nbsp;»&nbsp;; «&nbsp;j'ai perdu <b>une</b> "
           + "carte&nbsp;». C'est le mot du comptoir, et il prend «&nbsp;une&nbsp;».",
        pourquoi: "une carte" },
      { txt: "livre", sous: "pour lire", ok: 'un',
        rat: "Le mot finit par «&nbsp;e&nbsp;», et pourtant on dit «&nbsp;<b>un</b> livre&nbsp;». "
           + "Voilà pourquoi la fin du mot ne décide de rien.",
        pourquoi: "un livre — même avec un « e » à la fin" },
      { txt: "fenêtre", sous: "pour voir dehors", ok: 'une',
        rat: "«&nbsp;Ouvrez <b>une</b> fenêtre&nbsp;». Celui-là finit aussi par «&nbsp;e&nbsp;», "
           + "et il prend «&nbsp;une&nbsp;»&nbsp;: la fin du mot ne dit rien.",
        pourquoi: "une fenêtre" },
    ],
    attente: "Tranchez les huit mots pour continuer.",
  },

  // ── 3. La règle, écrite comme un constat de ce qu'il vient de faire. ─────
  {
    id:   'le-geste',
    type: 'notion',
    eye:  'Ce que vous venez de faire',
    menu: 'Le geste',
    titre: "Vous n'avez rien deviné. Vous vous êtes souvenu.",
    paras: [
      "Regardez comment vous avez répondu&nbsp;: vous n'avez pas regardé la chaise, vous n'avez pas "
      + "compté les lettres. Vous avez entendu la phrase dans votre tête&nbsp;: «&nbsp;prenez une "
      + "chaise&nbsp;». Le petit mot était <b>collé</b> au mot.",

      "En français, chaque nom est <b>masculin</b> (un) ou <b>féminin</b> (une). Rien dans l'objet "
      + "ne le dit. Un livre et une carte sont deux papiers. Un sac et une chaise sont deux objets. "
      + "Ce n'est pas une question d'intelligence&nbsp;: c'est une question de mémoire.",

      "<b>Le geste, pour tous les mots neufs&nbsp;:</b> quand vous notez un mot, notez-le avec son "
      + "petit mot. Jamais «&nbsp;table&nbsp;». Toujours «&nbsp;<b>une</b> table&nbsp;». Les deux "
      + "mots ensemble, comme un seul.",
    ],
    retenir: "Le genre ne se devine pas. Il s'apprend <b>avec</b> le mot&nbsp;: "
           + "«&nbsp;une table&nbsp;», jamais «&nbsp;table&nbsp;».",
    attente: "Lisez, puis continuez.",
  },

  // ── 4. Le piège : la fin du mot. ─────────────────────────────────────────
  {
    id:   'le-e-final',
    type: 'verif',
    eye:  'Le piège',
    menu: 'La fin du mot',
    titre: "Ana écrit à son fils. Elle parle du téléphone.",
    consigne: "Le mot «&nbsp;téléphone&nbsp;» finit par «&nbsp;e&nbsp;». Alors, elle écrit "
            + "quoi&nbsp;?",
    options: [
      { txt: "«&nbsp;J'ai <b>un</b> téléphone à la maison.&nbsp;»", juste: true },
      { txt: "«&nbsp;J'ai <b>une</b> téléphone à la maison.&nbsp;»",
        rat_t: "C'est la faute la plus fréquente, et elle est logique.",
        rat: "Beaucoup de mots féminins finissent par «&nbsp;e&nbsp;»&nbsp;: une carte, une porte, "
           + "une chaise. Alors on prend l'habitude. Mais «&nbsp;téléphone&nbsp;», "
           + "«&nbsp;livre&nbsp;», «&nbsp;groupe&nbsp;» finissent aussi par «&nbsp;e&nbsp;» et "
           + "prennent «&nbsp;<b>un</b>&nbsp;»." },
      { txt: "Les deux se disent. Personne ne fait attention à ça.",
        rat_t: "On vous comprendra — et on vous reprendra.",
        rat: "C'est vrai qu'on comprend quand même. Mais ce petit mot revient dans <b>chaque</b> "
           + "phrase que vous direz en français&nbsp;: c'est la faute qu'on remarque le plus, et "
           + "c'est aussi la plus facile à corriger." },
    ],
    pourquoi: "<b>Un</b> téléphone. La fin du mot ne décide de rien&nbsp;: seul le mot appris "
            + "décide.",
    attente: "Choisissez une réponse pour continuer.",
  },

  // ── 5. Ce que le genre appris une fois vous rapporte trois fois. ─────────
  {
    id:   'trois-fois',
    type: 'notion',
    eye:  'Ce que ça vous rapporte',
    menu: 'Trois petits mots',
    titre: "Vous apprenez « une » une fois. Il vous sert trois fois.",
    paras: [
      "Le genre d'un mot ne sert pas seulement à dire «&nbsp;un&nbsp;» ou «&nbsp;une&nbsp;». Il "
      + "commande aussi <b>les autres petits mots</b> qui viennent devant le même nom.",

      "Regardez «&nbsp;carte&nbsp;», qui est féminin&nbsp;: <b>une</b> carte · <b>la</b> carte · "
      + "<b>ma</b> carte. Et «&nbsp;sac&nbsp;», qui est masculin&nbsp;: <b>un</b> sac · "
      + "<b>le</b> sac · <b>mon</b> sac.",

      "Autrement dit&nbsp;: le jour où vous avez retenu «&nbsp;une carte&nbsp;», vous savez déjà "
      + "dire «&nbsp;la carte&nbsp;» et «&nbsp;ma carte&nbsp;». Un mot appris comme il faut, c'est "
      + "trois phrases justes.",
    ],
    retenir: "Masculin&nbsp;: un · le · mon. Féminin&nbsp;: une · la · ma. "
           + "Le nom ne change pas&nbsp;; ce sont les petits mots devant lui qui changent.",
    attente: "Lisez, puis continuez.",
  },

  // ── 6. Trier des phrases écrites. ────────────────────────────────────────
  {
    id:   'tri-phrases',
    type: 'tri',
    eye:  'À vous de trancher',
    menu: 'Six phrases',
    titre: "Six phrases. Lesquelles sont correctes ?",
    consigne: "Regardez les <b>deux</b> petits mots de chaque phrase. Ils doivent aller ensemble.",
    colonnes: [
      { id: 'ok',   t: 'Correct',   b: 'Correct' },
      { id: 'faux', t: 'Une faute', b: 'Une faute' },
    ],
    items: [
      { txt: "J'ai un sac. Le sac est noir.", ok: 'ok',
        rat: "«&nbsp;Un&nbsp;» puis «&nbsp;le&nbsp;»&nbsp;: les deux petits mots du masculin. "
           + "La phrase tient.",
        pourquoi: "un sac · le sac" },
      { txt: "J'ai une chaise. Le chaise est cassée.", ok: 'faux',
        rat: "Le premier petit mot est bon&nbsp;: «&nbsp;une chaise&nbsp;». Mais le deuxième est "
           + "reparti au masculin. Il faut «&nbsp;<b>la</b> chaise&nbsp;».",
        pourquoi: "Il faut « la chaise »." },
      { txt: "Voici une carte. C'est ma carte d'autobus.", ok: 'ok',
        rat: "«&nbsp;Une&nbsp;» puis «&nbsp;ma&nbsp;»&nbsp;: les deux petits mots du féminin. Rien "
           + "à corriger.",
        pourquoi: "une carte · ma carte" },
      { txt: "Il y a un fenêtre dans la classe.", ok: 'faux',
        rat: "«&nbsp;Fenêtre&nbsp;» est féminin&nbsp;: on dit «&nbsp;<b>une</b> fenêtre&nbsp;». "
           + "Le mot est long, mais ça ne change rien.",
        pourquoi: "Il faut « une fenêtre »." },
      { txt: "Je cherche un livre. Le livre est vert.", ok: 'ok',
        rat: "Le mot finit par «&nbsp;e&nbsp;» et reste masculin. Les deux petits mots sont "
           + "d'accord&nbsp;: c'est ce qui compte.",
        pourquoi: "un livre · le livre" },
      { txt: "Il y a un porte au fond du couloir.", ok: 'faux',
        rat: "On dit «&nbsp;<b>une</b> porte&nbsp;». Le mot revient tous les jours en classe, et "
           + "il ne prend jamais «&nbsp;un&nbsp;».",
        pourquoi: "Il faut « une porte »." },
    ],
    attente: "Tranchez les six phrases pour continuer.",
  },

  // ── 7. Le geste, appliqué pour de vrai. ──────────────────────────────────
  {
    id:   'dans-le-carnet',
    type: 'verif',
    eye:  'Vérification',
    menu: 'Votre carnet',
    titre: "Vous entendez un mot neuf : « autobus ». Comment le notez-vous ?",
    consigne: "Vous avez trois secondes pour l'écrire dans votre cahier. Quelle note vous servira "
            + "encore dans un mois&nbsp;?",
    options: [
      { txt: "un autobus", juste: true },
      { txt: "autobus",
        rat_t: "C'est le mot. Ce n'est pas assez.",
        rat: "Dans un mois, vous saurez ce que le mot veut dire, et vous ne saurez toujours pas "
           + "s'il faut dire «&nbsp;un&nbsp;» ou «&nbsp;une&nbsp;». Vous devrez redemander. "
           + "Le petit mot ne coûte rien à écrire aujourd'hui." },
      { txt: "autobus (masculin)",
        rat_t: "C'est juste, et ce n'est pas ce que vous direz.",
        rat: "Vous ne direz jamais «&nbsp;masculin autobus&nbsp;» au comptoir. Vous direz "
           + "«&nbsp;<b>un</b> autobus&nbsp;». Notez la phrase que vous allez dire, pas le mot qui "
           + "l'explique." },
    ],
    pourquoi: "<b>un autobus.</b> Deux mots collés, dans le cahier comme dans la bouche.",
    attente: "Choisissez une réponse pour continuer.",
  },

  // ── 8. Ce qu'on fait quand on ne sait pas — gardé pour la fin. ───────────
  {
    id:   'quand-on-ne-sait-pas',
    type: 'notion',
    eye:  'Ce qui reste',
    menu: "Si vous ne savez pas",
    titre: "Vous ne saurez pas toujours. Voici quoi faire.",
    paras: [
      "On a gardé ceci pour la fin, et c'est voulu&nbsp;: si on le disait au début, vous "
      + "n'apprendriez plus aucun mot par cœur. Mais il arrivera que vous ayez besoin d'un mot que "
      + "vous n'avez pas encore appris.",

      "<b>Alors, demandez.</b> La phrase est courte et tout le monde la comprend&nbsp;: "
      + "«&nbsp;<i>On dit un ou une&nbsp;?</i>&nbsp;» Vous pouvez la dire à votre enseignante, à un "
      + "collègue, à la personne au comptoir. Personne ne trouvera la question bizarre.",

      "Et quand quelqu'un vous répond, écoutez le <b>petit mot</b> qu'il emploie, pas seulement le "
      + "grand. C'est la façon la plus rapide d'apprendre&nbsp;: la personne devant vous dit "
      + "«&nbsp;une carte&nbsp;», vous répétez «&nbsp;une carte&nbsp;».",
    ],
    retenir: "Quand vous ne savez pas&nbsp;: «&nbsp;On dit un ou une&nbsp;?&nbsp;» "
           + "Quand on vous répond&nbsp;: répétez les <b>deux</b> mots.",
    attente: "Lisez, puis continuez.",
  },

  // ── 9. Écrire, pas reconnaître. ──────────────────────────────────────────
  {
    id:   'votre-message',
    type: 'verif',
    eye:  'Vérification',
    menu: 'Votre message',
    titre: "Vous écrivez à l'école. Quelle version tient d'un bout à l'autre ?",
    consigne: "Vous avez perdu votre carte d'autobus dans la classe. Trois messages "
            + "disent la même chose&nbsp;: un seul est correct partout.",
    options: [
      { txt: "«&nbsp;Bonjour. J'ai perdu une carte d'autobus dans la classe. La carte est "
           + "bleue.&nbsp;»", juste: true },
      { txt: "«&nbsp;Bonjour. J'ai perdu un carte d'autobus dans la classe. La carte est "
           + "bleue.&nbsp;»",
        rat_t: "La deuxième moitié est juste. C'est la première qui a lâché.",
        rat: "Vous avez écrit «&nbsp;<b>la</b> carte&nbsp;» à la fin&nbsp;: vous saviez donc que le "
           + "mot est féminin. Il fallait le même genre au début&nbsp;: «&nbsp;<b>une</b> "
           + "carte&nbsp;». Les deux petits mots d'une même phrase vont toujours ensemble." },
      { txt: "«&nbsp;Bonjour. J'ai perdu une carte d'autobus dans le classe. La carte est "
           + "bleue.&nbsp;»",
        rat_t: "La carte est bonne. C'est la classe qui a changé de genre.",
        rat: "«&nbsp;Classe&nbsp;» est féminin&nbsp;: <b>une</b> classe, <b>la</b> classe. C'est un "
           + "mot que vous dites tous les jours — raison de plus pour le noter avec son petit mot." },
    ],
    pourquoi: "Une carte, la carte, la classe. <b>Le même mot garde le même genre du début à la "
            + "fin du message.</b>",
    attente: "Choisissez une réponse pour continuer.",
  },

  // ── 10. La fermeture : le même cas qu'à l'écran 1. ───────────────────────
  {
    id:   'fermeture',
    type: 'verif',
    eye:  'La dernière',
    menu: 'Pour finir',
    titre: "On revient au mot du début : « table ».",
    consigne: "Vous savez maintenant qu'on dit «&nbsp;une table&nbsp;». Vous notez le mot dans "
            + "votre cahier ce soir. Vous écrivez quoi&nbsp;?",
    options: [
      { txt: "une table — la table est dans la classe", juste: true },
      { txt: "table (une)",
        rat_t: "Presque. Le petit mot est là, mais il n'est pas à sa place.",
        rat: "Vous avez retenu l'information. Mais quand vous parlerez, le petit mot vient "
           + "<b>avant</b>, et c'est cet ordre-là qu'il faut mettre dans l'oreille. Écrivez-le "
           + "comme vous allez le dire." },
      { txt: "table = un meuble avec quatre pieds",
        rat_t: "Une bonne définition ne remplace pas le petit mot.",
        rat: "Vous saurez ce qu'est une table — vous le saviez déjà. Ce qui vous manquait, c'était "
           + "«&nbsp;une&nbsp;». Une note qui n'a pas le petit mot vous fera refaire la même faute "
           + "dans un mois." },
    ],
    pourquoi: "Vous avez fait les trois choses&nbsp;: reconnaître que le genre ne se devine pas, "
            + "garder le même genre dans toute la phrase, et noter chaque mot neuf <b>avec</b> son "
            + "petit mot.",
    attente: "Choisissez une réponse pour finir.",
  },

];
