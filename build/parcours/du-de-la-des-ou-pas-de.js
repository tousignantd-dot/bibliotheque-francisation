// ═══════════════════════════════════════════════════════════════════════════
// Point express — « J'ai du lait » → « Je n'ai pas de lait »
//
// Savoirs n2-s16 (déterminants quantifiants indéfinis : un, une, des) et
// n2-s17 (déterminant quantifiant négatif : de). Dix minutes, dix écrans.
// Une ORDONNANCE : l'enseignant l'envoie à l'élève dont la production écrite
// porte « je n'ai pas du temps », « il n'y a pas des places ».
//
// La faute est parmi les plus fréquentes du niveau 2, et elle a une bonne
// raison : dans la plupart des langues, le mot devant le nom ne bouge pas
// quand on dit non. En français, il bouge — et c'est le seul endroit où la
// négation change un mot qui n'est pas le verbe.
//
// ── Ce qui le sépare des mini-leçons existantes ────────────────────────────
// Deux existent sur ce terrain, et l'élève en a probablement lu une :
//   · `module-n2-panier`, « un, une, des — et "pas de" » : les trois formes
//     une par une, puis un bloc final sur la négative, puis un labo de quinze
//     phrases d'épicerie.
//   · `module-alimentation`, « Du, de la, des » : les quatre formes en
//     tableau, la négative, la quantité précise, et un « test en une seconde ».
// Les deux enseignent LES FORMES d'abord et la négation en dernier bloc. Les
// cinq écarts tenus :
//
//   1. INDUCTIF. Aucune règle avant l'écran 3. L'élève juge six phrases
//      écrites — correcte ou fautive — sans qu'on lui ait donné la règle. La
//      règle de l'écran 3 est le constat de ce qu'il vient de faire.
//   2. PARTIEL, JAMAIS LE TABLEAU DES FORMES. Les mini-leçons donnent du,
//      de la, de l', des, un, une. Ici, on ne les apprend pas : on apprend
//      qu'ils DISPARAISSENT tous dans un seul mot. Le test se pose sur la
//      phrase, pas sur le nom — « est-ce qu'il y a un mot de négation ? » —
//      et il marche sur un nom dont on ignore le genre, ce qu'aucune liste
//      de formes ne permet.
//   3. LE CAS PAR DÉFAUT EST DIT EN DERNIER (écran 6). Nommer « du, de la,
//      des » d'entrée ferait croire à deux règles à retenir ; il n'y en a
//      qu'une, et elle ne concerne que la phrase négative.
//   4. LE MÉTALANGAGE APRÈS. « Déterminant » n'est écrit qu'à l'écran 3.
//   5. EXEMPLES VARIÉS, JAMAIS L'ÉPICERIE. Les deux mini-leçons se passent
//      au marché ; ici, une note à l'école, un message à un employeur, un
//      texto, un formulaire. L'élève doit reconnaître la faute partout.
//
// L'écran 7 traite le seul contre-exemple que l'élève rencontrera — « ce n'est
// pas un problème » — en le donnant À RECONNAÎTRE, jamais à produire. Le
// taire ferait corriger comme fautive une phrase entendue tous les jours.
//
// Aucun média : cette faute se voit à l'écrit et se corrige par comparaison de
// chaînes. Le point tourne dans un centre en mode sans assistance.
// ═══════════════════════════════════════════════════════════════════════════

const PARCOURS = {
  slug:     'du-de-la-des-ou-pas-de',
  titre:    "« J'ai du lait » → « Je n'ai pas de lait »",
  surtitre: "Point express · 10 minutes",
  niveau:   2,
  savoir:   'n2-s16 · n2-s17',
};

const ECRANS = [

  // ── 1. Une décision, sans aucune règle donnée. ───────────────────────────
  {
    id:   'depart',
    type: 'verif',
    eye:  'Une question, pour commencer',
    menu: 'Le lait',
    titre: "« J'ai du lait. » Comment dit-on le contraire ?",
    consigne: "Répondez avec ce que vous savez déjà — ou au feeling. On expliquera "
            + "après&nbsp;: c'est fait exprès.",
    options: [
      { txt: "Je n'ai pas de lait.", juste: true },
      { txt: "Je n'ai pas du lait.",
        rat_t: "Vous avez gardé le mot de la phrase de départ.",
        rat: "C'est la faute la plus fréquente du niveau, et elle a une bonne "
           + "raison&nbsp;: dans presque toutes les langues, le mot devant le nom ne "
           + "change pas quand on dit non. En français, il change. Regardez l'autre "
           + "réponse&nbsp;: un seul mot y est différent." },
      { txt: "Je n'ai pas le lait.",
        rat_t: "Cette phrase existe, mais elle dit autre chose.",
        rat: "«&nbsp;Le lait&nbsp;» désigne un lait précis — celui que je devais "
           + "acheter, celui qui était sur la table. Ici, on parle du lait en général&nbsp;: "
           + "il n'y en a pas dans la maison." },
    ],
    pourquoi: "«&nbsp;Je n'ai pas <b>de</b> lait.&nbsp;» Retenez la phrase entière "
            + "pour l'instant&nbsp;; on va voir pourquoi juste après.",
    attente: "Choisissez une réponse pour continuer.",
  },

  // ── 2. On trie AVANT de savoir. ──────────────────────────────────────────
  {
    id:   'tri-phrases',
    type: 'tri',
    eye:  'À vous de trancher',
    menu: 'Six phrases',
    titre: "Six phrases écrites. Lesquelles sont correctes ?",
    consigne: "Aucune règle ne vous a été donnée — normal. Lisez chaque phrase à voix "
            + "basse&nbsp;: gardez celle qui sonne juste, écartez celle qui accroche.",
    colonnes: [
      { id: 'ok',   t: 'Correct',   b: 'Correct' },
      { id: 'faux', t: 'Une faute', b: 'Une faute' },
    ],
    items: [
      { txt: "Je n'ai pas de voiture.", sous: "sur un formulaire", ok: 'ok',
        rat: "Après «&nbsp;pas&nbsp;», le mot devant le nom est «&nbsp;de&nbsp;». "
           + "Rien à corriger.",
        pourquoi: "Après « pas » : de. Juste." },
      { txt: "Il n'y a pas des places.", sous: "au téléphone", ok: 'faux',
        rat: "«&nbsp;des&nbsp;» est le mot de la phrase positive — «&nbsp;il y a des "
           + "places&nbsp;». Après «&nbsp;pas&nbsp;», il devient «&nbsp;de&nbsp;»&nbsp;: "
           + "«&nbsp;il n'y a pas <b>de</b> places&nbsp;».",
        pourquoi: "Il faut « il n'y a pas de places »." },
      { txt: "Je ne bois pas de café.", sous: "à la pause", ok: 'ok',
        rat: "La phrase positive serait «&nbsp;je bois du café&nbsp;». Ici, "
           + "«&nbsp;du&nbsp;» est bien devenu «&nbsp;de&nbsp;».",
        pourquoi: "« du » devient « de ». Juste." },
      { txt: "Nous n'avons pas du temps.", sous: "au travail", ok: 'faux',
        rat: "«&nbsp;Nous avons du temps&nbsp;» est correct&nbsp;; dès qu'on ajoute "
           + "«&nbsp;pas&nbsp;», il faut «&nbsp;de&nbsp;»&nbsp;: «&nbsp;nous n'avons "
           + "pas <b>de</b> temps&nbsp;». Le mot change même si le nom ne change pas.",
        pourquoi: "Il faut « pas de temps »." },
      { txt: "Il n'y a pas d'eau chaude.", sous: "un message au propriétaire", ok: 'ok',
        rat: "Devant une voyelle, «&nbsp;de&nbsp;» perd son <i>e</i> et prend une "
           + "apostrophe&nbsp;: «&nbsp;pas <b>d'</b>eau&nbsp;». C'est le même mot.",
        pourquoi: "Devant une voyelle : d'. Juste." },
      { txt: "Elle ne prend pas des cours le soir.", sous: "en parlant d'une amie", ok: 'faux',
        rat: "«&nbsp;Elle prend des cours&nbsp;» devient «&nbsp;elle ne prend pas "
           + "<b>de</b> cours&nbsp;». C'est exactement la même correction que "
           + "«&nbsp;il n'y a pas de places&nbsp;»&nbsp;: le pluriel n'y change rien.",
        pourquoi: "Il faut « pas de cours », même au pluriel." },
    ],
    attente: "Tranchez les six phrases pour continuer.",
  },

  // ── 3. La règle, écrite comme un constat. Le métalangage arrive ici. ─────
  {
    id:   'le-test',
    type: 'notion',
    eye:  'Ce que vous venez de faire',
    menu: 'Le test',
    titre: "Vous avez regardé un seul mot, et il était toujours au même endroit.",
    paras: [
      "Regardez votre colonne «&nbsp;correct&nbsp;»&nbsp;: <b>pas de voiture</b>, "
      + "<b>pas de café</b>, <b>pas d'eau</b>. Et votre colonne «&nbsp;faute&nbsp;»&nbsp;: "
      + "pas <i>des</i> places, pas <i>du</i> temps, pas <i>des</i> cours. Dans les six "
      + "phrases, le mot qui décide est celui qui suit <b>pas</b>.",

      "Le petit mot devant le nom s'appelle un <b>déterminant</b>. Vous n'avez pas "
      + "besoin du nom pour vous en servir, mais votre enseignant l'emploiera.",

      "<b>Le test, à vous poser sur n'importe quelle phrase que vous écrivez&nbsp;:</b> "
      + "est-ce qu'il y a <i>pas</i> devant le nom&nbsp;? Si oui, le déterminant est "
      + "<b>de</b> — ou <b>d'</b> devant une voyelle.",
    ],
    retenir: "Après <b>pas</b>&nbsp;: toujours <b>de</b>. Un test vaut mieux qu'une "
           + "liste de formes&nbsp;: il marche même sur un nom dont vous ignorez "
           + "le genre.",
    attente: "Lisez, puis continuez.",
  },

  // ── 4. Le cas fréquent : l'apostrophe, dans un vrai message. ─────────────
  {
    id:   'apostrophe',
    type: 'verif',
    eye:  'Vérification',
    menu: 'Un texto',
    titre: "Vous écrivez à un ami. Vous ne pouvez pas payer le stationnement.",
    consigne: "Une seule de ces trois lignes s'écrit.",
    options: [
      { txt: "Je n'ai pas d'argent sur moi.", juste: true },
      { txt: "Je n'ai pas de argent sur moi.",
        rat_t: "Le mot est bon. C'est la rencontre qui ne va pas.",
        rat: "«&nbsp;de&nbsp;» et «&nbsp;argent&nbsp;» ne se touchent jamais&nbsp;: le "
           + "<i>e</i> tombe et on met une apostrophe. On écrit «&nbsp;pas "
           + "<b>d'</b>argent&nbsp;», comme «&nbsp;pas d'eau&nbsp;», «&nbsp;pas "
           + "d'enfants&nbsp;», «&nbsp;pas d'horaire&nbsp;»." },
      { txt: "Je n'ai pas de l'argent sur moi.",
        rat_t: "Vous avez gardé la phrase positive en entier.",
        rat: "«&nbsp;J'ai <b>de l'</b>argent&nbsp;» est correct. Mais dès qu'il y a "
           + "«&nbsp;pas&nbsp;», tout cela se réduit à un seul mot&nbsp;: "
           + "«&nbsp;d'&nbsp;». C'est le gain de la règle — trois formes deviennent une." },
    ],
    pourquoi: "«&nbsp;Je n'ai pas <b>d'</b>argent.&nbsp;» Devant a, e, i, o, u et h, "
            + "«&nbsp;de&nbsp;» prend l'apostrophe.",
    attente: "Choisissez une réponse pour continuer.",
  },

  // ── 5. Pourquoi la faute est tentante, et ce que « de » dit vraiment. ────
  {
    id:   'le-mot-des-quantites',
    type: 'notion',
    eye:  'Pourquoi cette faute revient',
    menu: 'Le mot « de »',
    titre: "« de » est le mot des quantités qu'on ne compte pas.",
    paras: [
      "Cette faute revient parce qu'elle est logique&nbsp;: dans presque toutes les "
      + "langues, on ajoute un mot pour dire non et le reste de la phrase ne bouge "
      + "pas. En français, la négation touche <b>deux</b> endroits&nbsp;: le verbe, "
      + "et le petit mot devant le nom.",

      "Une manière de s'en souvenir&nbsp;: <b>de</b> apparaît chaque fois que la "
      + "quantité n'est pas un nombre. Zéro — «&nbsp;pas <b>de</b> lait&nbsp;». "
      + "Une mesure — «&nbsp;un litre <b>de</b> lait&nbsp;», «&nbsp;beaucoup "
      + "<b>de</b> monde&nbsp;». C'est le même mot, et il fait le même travail.",

      "Attention à une chose&nbsp;: le «&nbsp;ne&nbsp;» tombe souvent à l'oral, "
      + "«&nbsp;de&nbsp;» jamais. On entend «&nbsp;j'ai pas <b>de</b> lait&nbsp;» "
      + "tous les jours. Ce n'est pas le mot qu'on oublie en parlant, c'est celui "
      + "qu'on oublie en écrivant.",
    ],
    retenir: "Zéro ou une mesure → <b>de</b>. Le «&nbsp;ne&nbsp;» disparaît à "
           + "l'oral&nbsp;; le «&nbsp;de&nbsp;» reste.",
    attente: "Lisez, puis continuez.",
  },

  // ── 6. Le cas par défaut, dit en dernier : trier les deux côtés. ─────────
  {
    id:   'tri-plein-ou-de',
    type: 'tri',
    eye:  'À vous de trancher',
    menu: 'Six trous',
    titre: "Six phrases à trous. De quel côté tombe chacune ?",
    consigne: "Deux colonnes seulement. À gauche, les phrases où le mot devant le nom "
            + "est <b>du</b>, <b>de la</b> ou <b>des</b>. À droite, celles où c'est "
            + "<b>de</b> ou <b>d'</b>.",
    colonnes: [
      { id: 'plein', t: 'du · de la · des', b: 'du · de la · des' },
      { id: 'de',    t: "de · d'",          b: "de · d'" },
    ],
    items: [
      { txt: "Le matin, je bois ___ café.", sous: "une habitude", ok: 'plein',
        rat: "Il n'y a aucun mot de négation dans cette phrase, et aucune mesure&nbsp;: "
           + "c'est le cas ordinaire. On écrit «&nbsp;je bois <b>du</b> café&nbsp;».",
        pourquoi: "Rien à signaler : du café." },
      { txt: "Le soir, je ne bois pas ___ café.", sous: "la même personne", ok: 'de',
        rat: "«&nbsp;pas&nbsp;» est devant le nom&nbsp;: le déterminant devient "
           + "«&nbsp;de&nbsp;». C'est exactement la même phrase que la précédente, "
           + "mise au négatif.",
        pourquoi: "Après « pas » : pas de café." },
      { txt: "Il y a ___ neige sur le trottoir.", sous: "en janvier", ok: 'plein',
        rat: "Aucune négation. Le nom est féminin, donc «&nbsp;<b>de la</b> "
           + "neige&nbsp;» — mais ce que vous aviez à décider, c'est le côté.",
        pourquoi: "Rien à signaler : de la neige." },
      { txt: "Je voudrais un litre ___ lait.", sous: "au comptoir", ok: 'de',
        rat: "Il n'y a pas de négation, et pourtant c'est «&nbsp;de&nbsp;». La raison "
           + "est la même&nbsp;: la quantité est déjà donnée par «&nbsp;un litre&nbsp;». "
           + "Zéro ou une mesure, c'est le même mot.",
        pourquoi: "Une mesure est donnée : un litre de lait." },
      { txt: "Elle achète ___ pommes chaque semaine.", sous: "en parlant d'une voisine", ok: 'plein',
        rat: "Aucune négation, aucune mesure&nbsp;: «&nbsp;<b>des</b> pommes&nbsp;». "
           + "C'est le cas ordinaire, au pluriel.",
        pourquoi: "Rien à signaler : des pommes." },
      { txt: "Cette semaine, elle n'achète pas ___ pommes.", sous: "la même voisine", ok: 'de',
        rat: "Le pluriel ne protège pas&nbsp;: «&nbsp;des&nbsp;» devient "
           + "«&nbsp;de&nbsp;» comme les autres. «&nbsp;Elle n'achète pas <b>de</b> "
           + "pommes.&nbsp;»",
        pourquoi: "Après « pas » : pas de pommes." },
    ],
    attente: "Tranchez les six phrases pour continuer.",
  },

  // ── 7. Le cas qui trompe : à reconnaître, pas à produire. ────────────────
  {
    id:   'ce-nest-pas-un',
    type: 'verif',
    eye:  'Le cas qui trompe',
    menu: 'Une phrase à part',
    titre: "Une phrase où le petit mot ne change pas.",
    consigne: "Vous lisez la réponse d'une secrétaire à une question sur un papier "
            + "reçu par la poste. Laquelle a-t-elle écrite&nbsp;?",
    options: [
      { txt: "« Ce n'est pas un compte. C'est un rappel de rendez-vous. »", juste: true },
      { txt: "« Ce n'est pas de compte. C'est un rappel de rendez-vous. »",
        rat_t: "Vous avez appliqué la règle. Ici, elle ne s'applique pas.",
        rat: "La règle vaut quand on dit qu'il n'y a <b>rien</b>&nbsp;: pas de compte "
           + "dans la boîte aux lettres. Ici, la secrétaire dit autre chose&nbsp;: le "
           + "papier existe, mais ce <b>n'est pas ça</b>. On garde alors "
           + "«&nbsp;un&nbsp;»." },
      { txt: "« Ce n'est pas du compte. C'est un rappel de rendez-vous. »",
        rat_t: "Cette forme n'existe dans aucun des deux cas.",
        rat: "«&nbsp;du&nbsp;» ne survit jamais à un «&nbsp;pas&nbsp;» — c'était la "
           + "règle des six premières phrases. Et ici, ce n'est même pas la règle qui "
           + "s'applique&nbsp;: il fallait garder «&nbsp;un&nbsp;»." },
    ],
    pourquoi: "Retenez seulement ceci&nbsp;: après <b>ce n'est pas</b> et <b>ce ne "
            + "sont pas</b>, le petit mot ne bouge pas. C'est le seul endroit. "
            + "À reconnaître quand vous le lisez&nbsp;; partout ailleurs, votre test tient.",
    attente: "Choisissez une réponse pour continuer.",
  },

  // ── 8. Le test s'étend : « plus », « jamais », « aucun » marchent pareil. ─
  {
    id:   'plus-jamais',
    type: 'notion',
    eye:  'Ce que le test couvre aussi',
    menu: 'Plus · jamais',
    titre: "Ce n'est pas seulement « pas ». Trois autres mots font la même chose.",
    paras: [
      "«&nbsp;Je n'ai <b>plus</b> <b>de</b> lait&nbsp;» — il y en avait, il n'y en a "
      + "plus. «&nbsp;Il n'y a <b>jamais</b> <b>de</b> place le lundi&nbsp;» — aucune "
      + "fois. «&nbsp;Je ne bois <b>pas encore</b> <b>de</b> café le matin&nbsp;».",

      "Vous n'avez donc pas trois règles de plus à apprendre. Le test change d'un "
      + "seul mot&nbsp;: au lieu de chercher <i>pas</i>, cherchez <b>n'importe quel "
      + "mot qui dit non</b> devant le nom. Le déterminant qui suit est toujours "
      + "<i>de</i>.",
    ],
    retenir: "pas · plus · jamais → <b>de</b>. Une seule règle, quatre portes d'entrée.",
    attente: "Lisez, puis continuez.",
  },

  // ── 9. Écrire une suite entière, pas reconnaître un mot. ─────────────────
  {
    id:   'le-message',
    type: 'verif',
    eye:  'Vérification',
    menu: 'Le message',
    titre: "Trois messages à un employeur. Un seul tient d'un bout à l'autre.",
    consigne: "La personne explique qu'elle ne peut pas venir&nbsp;: son garage n'a pas "
            + "fini la réparation, et l'autobus ne passe pas assez tôt.",
    options: [
      { txt: "« Je n'ai pas de voiture cette semaine et il n'y a pas d'autobus avant sept heures. »",
        juste: true },
      { txt: "« Je n'ai pas de voiture cette semaine et il n'y a pas des autobus avant sept heures. »",
        rat_t: "La première moitié est juste. Le pluriel vous a arrêté.",
        rat: "«&nbsp;Voiture&nbsp;» au singulier, vous l'avez traité correctement. "
           + "«&nbsp;Autobus&nbsp;» au pluriel demande exactement la même chose&nbsp;: "
           + "«&nbsp;pas <b>d'</b>autobus&nbsp;». Le nombre ne change rien à la règle." },
      { txt: "« Je n'ai pas du voiture cette semaine et il n'y a pas d'autobus avant sept heures. »",
        rat_t: "Les deux moitiés ont échangé leurs fautes.",
        rat: "La seconde est juste — «&nbsp;pas d'autobus&nbsp;». La première garde "
           + "«&nbsp;du&nbsp;», qui ne survit jamais à un «&nbsp;pas&nbsp;» — et qui "
           + "en plus ne va pas devant un nom féminin. Il faut «&nbsp;pas "
           + "<b>de</b> voiture&nbsp;»." },
    ],
    pourquoi: "Deux négations, deux fois le même mot&nbsp;: <b>de</b> devant une "
            + "consonne, <b>d'</b> devant une voyelle. <b>C'est tout le point en une "
            + "phrase.</b>",
    attente: "Choisissez une réponse pour continuer.",
  },

  // ── 10. La fermeture : le cas de l'écran 1. ──────────────────────────────
  {
    id:   'fermeture',
    type: 'verif',
    eye:  'La dernière',
    menu: 'Pour finir',
    titre: "On revient au lait. Vous écrivez un mot sur la table de la cuisine.",
    consigne: "Vous voulez dire qu'il n'y en a plus, et qu'il faut en acheter.",
    options: [
      { txt: "« Il n'y a plus de lait. Peux-tu en acheter ? »", juste: true },
      { txt: "« Il n'y a plus du lait. Peux-tu en acheter ? »",
        rat_t: "C'est la phrase de l'écran 1, avec un autre mot de négation.",
        rat: "«&nbsp;plus&nbsp;» fait le même travail que «&nbsp;pas&nbsp;»&nbsp;: le "
           + "déterminant qui suit devient <b>de</b>. C'est ce que vous avez vu à "
           + "l'écran 8 — quatre portes d'entrée, une seule règle." },
      { txt: "« Il n'y a plus le lait. Peux-tu en acheter ? »",
        rat_t: "Cette phrase dit autre chose que ce que vous vouliez dire.",
        rat: "«&nbsp;Le lait&nbsp;» désignerait un lait précis — celui qui était là "
           + "hier, celui que quelqu'un avait mis de côté. Vous voulez dire qu'il n'y "
           + "en a plus du tout&nbsp;: c'est <b>de</b>." },
    ],
    pourquoi: "«&nbsp;Il n'y a plus <b>de</b> lait.&nbsp;» Vous avez fait les deux "
            + "moitiés&nbsp;: reconnaître le mot qui dit non, et changer le petit mot "
            + "qui suit.",
    attente: "Choisissez une réponse pour finir.",
  },

];
