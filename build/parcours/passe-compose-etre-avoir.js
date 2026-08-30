// ═══════════════════════════════════════════════════════════════════════════
// Parcours de remédiation — Passé composé : être ou avoir ?
//
// Savoir n5-s31. Une ORDONNANCE : l'enseignant l'envoie à un élève dont la
// production écrite montre la faute. Dix minutes, dix écrans.
//
// ── Ce qui le sépare des mini-leçons, et pourquoi c'est vital ici ──────────
// Huit modules portent déjà une mini-leçon sur le passé composé — dont
// `module-n4-etablissement`, qui donne la règle en une phrase puis la liste des
// quinze verbes en tableau. Un élève envoyé ici l'a probablement déjà lue :
// la redire autrement ne servirait à rien. Les cinq écarts tenus :
//
//   1. INDUCTIF. L'élève range huit verbes AVANT qu'on lui dise pourquoi. La
//      règle de l'écran 3 est écrite comme un constat de ce qu'il vient de
//      faire, pas comme une leçon.
//   2. PARTIEL, JAMAIS LA LISTE. La mini-leçon donne les quinze verbes en bloc.
//      Ici : un TEST qu'on s'applique à soi-même — « est-ce que quelqu'un
//      change d'endroit ou d'état ? » — et six verbes, pas quinze. Une liste
//      s'oublie ; un test se réemploie sur un verbe qu'on n'a jamais vu.
//   3. AVOIR EST DIT EN DERNIER (écran 8). Les mini-leçons commencent par lui.
//      Or c'est le cas par défaut : le nommer trop tôt fait croire qu'il y a
//      deux règles à retenir, alors qu'il n'y en a qu'une, et une exception.
//   4. LE MÉTALANGAGE ARRIVE APRÈS. « Auxiliaire » n'est écrit qu'à l'écran 3,
//      une fois la chose manipulée. La mini-leçon ouvre dessus.
//   5. EXEMPLES VARIÉS, JAMAIS CEUX D'UN MODULE. Un parcours de remédiation ne
//      dépend d'aucune situation : les phrases viennent d'une note à l'école,
//      d'un message à un employeur, d'un texto. C'est voulu — l'élève doit
//      reconnaître la faute partout, pas dans un scénario.
//
// Aucun média : cette faute est invisible à l'oral, elle ne vit qu'à l'écrit.
// C'est le sujet même du parcours, et c'est pourquoi il n'a pas de son.
// ═══════════════════════════════════════════════════════════════════════════

const PARCOURS = {
  slug:     'passe-compose-etre-avoir',
  titre:    "Passé composé : être ou avoir ?",
  surtitre: "Parcours · 10 minutes",
  niveau:   5,
  savoir:   'n5-s31',
};

const ECRANS = [

  // ── 1. Une décision, sans aucune règle donnée. ───────────────────────────
  {
    id:   'depart',
    type: 'verif',
    eye:  'Une question, pour commencer',
    menu: 'Deux phrases',
    titre: "Une seule de ces deux phrases est juste. Laquelle ?",
    consigne: "Répondez avec ce que vous savez déjà — ou au feeling. On expliquera après&nbsp;: "
            + "c'est fait exprès.",
    options: [
      { txt: "Hier, j'ai resté à la maison.",
        rat_t: "«&nbsp;Rester&nbsp;» ne va pas avec «&nbsp;avoir&nbsp;».",
        rat: "C'est la faute la plus fréquente de toutes, et elle a une bonne raison&nbsp;: dans "
           + "beaucoup de langues, ce verbe se construit comme «&nbsp;avoir&nbsp;». En français, non. "
           + "Regardez l'autre phrase&nbsp;: elle vous dit avec quoi il se construit." },
      { txt: "Hier, je suis resté à la maison.", juste: true },
      { txt: "Les deux se disent.",
        rat_t: "Une seule est juste, et l'écart se voit.",
        rat: "À l'oral, on vous comprendra dans les deux cas — c'est bien le problème&nbsp;: "
           + "personne ne vous corrige. À l'écrit, la faute saute aux yeux de qui vous lit." },
    ],
    pourquoi: "«&nbsp;Je suis resté&nbsp;». Retenez la phrase entière pour l'instant&nbsp;; "
            + "on va voir pourquoi juste après.",
    attente: "Choisissez une réponse pour continuer.",
  },

  // ── 2. On trie AVANT de savoir. C'est ici que le parcours se sépare. ─────
  {
    id:   'tri-verbes',
    type: 'tri',
    eye:  'À vous de trancher',
    menu: 'Huit verbes',
    titre: "Huit verbes au passé. Lesquels se disent avec « je suis » ?",
    consigne: "Aucune règle ne vous a été donnée — normal. Essayez avec l'oreille&nbsp;: "
            + "dites la phrase dans votre tête, les deux fois, et gardez celle qui sonne juste.",
    colonnes: [
      { id: 'etre',  t: 'Je suis…',  b: 'Je suis…' },
      { id: 'avoir', t: "J'ai…",     b: "J'ai…" },
    ],
    items: [
      { txt: "partir", sous: "… à sept heures", ok: 'etre',
        rat: "«&nbsp;J'ai parti&nbsp;» ne se dit pas. Quelqu'un s'est déplacé — retenez ça, "
           + "on y revient dans deux écrans.",
        pourquoi: "Je suis parti. Quelqu'un s'est déplacé." },
      { txt: "téléphoner", sous: "… à la clinique", ok: 'avoir',
        rat: "«&nbsp;Je suis téléphoné&nbsp;» ne se dit pas&nbsp;: personne ne s'est déplacé, "
           + "on a fait quelque chose.",
        pourquoi: "J'ai téléphoné. On a fait quelque chose." },
      { txt: "arriver", sous: "… en retard", ok: 'etre',
        rat: "«&nbsp;J'ai arrivé&nbsp;» ne se dit pas. Encore un déplacement&nbsp;: on arrive "
           + "quelque part.",
        pourquoi: "Je suis arrivé. Un déplacement." },
      { txt: "oublier", sous: "… ma carte", ok: 'avoir',
        rat: "«&nbsp;Je suis oublié&nbsp;» voudrait dire que quelqu'un vous a oublié, vous. "
           + "Ici, c'est vous qui oubliez quelque chose.",
        pourquoi: "J'ai oublié. Un objet, pas un déplacement." },
      { txt: "tomber", sous: "… dans l'escalier", ok: 'etre',
        rat: "«&nbsp;J'ai tombé&nbsp;» s'entend souvent, et c'est une faute. Le corps a changé "
           + "de place&nbsp;: c'est un déplacement, même s'il n'était pas voulu.",
        pourquoi: "Je suis tombé. Le corps change de place." },
      { txt: "attendre", sous: "… une heure", ok: 'avoir',
        rat: "Attendre, c'est justement <i>ne pas</i> bouger. Rien ne se déplace, rien ne change.",
        pourquoi: "J'ai attendu. Personne ne bouge." },
      { txt: "devenir", sous: "… malade", ok: 'etre',
        rat: "Celui-là est plus difficile&nbsp;: rien ne se déplace. Mais quelque chose "
           + "<b>change</b> — on n'est plus dans le même état qu'avant.",
        pourquoi: "Je suis devenu. Un changement d'état." },
      { txt: "payer", sous: "… le loyer", ok: 'avoir',
        rat: "On fait quelque chose, on ne va nulle part et on ne devient rien.",
        pourquoi: "J'ai payé. Une action ordinaire." },
    ],
    attente: "Tranchez les huit verbes pour continuer.",
  },

  // ── 3. La règle, écrite comme un constat de ce qu'il vient de faire. ─────
  {
    id:   'le-test',
    type: 'notion',
    eye:  'Ce que vous venez de faire',
    menu: 'Le test',
    titre: "Vous avez séparé les déplacements du reste.",
    paras: [
      "Regardez votre colonne «&nbsp;je suis&nbsp;»&nbsp;: <b>partir, arriver, tomber, devenir</b>. "
      + "Dans les trois premiers, quelqu'un <b>change d'endroit</b>. Dans le dernier, quelqu'un "
      + "<b>change d'état</b>. Voilà toute la règle, et vous venez de la trouver sans qu'on vous "
      + "la dise.",

      "Le petit mot devant le participe — <i>suis</i>, <i>ai</i> — s'appelle <b>l'auxiliaire</b>. "
      + "Vous n'avez pas besoin du nom pour vous en servir, mais votre enseignant l'emploiera.",

      "<b>Le test, à vous poser sur n'importe quel verbe&nbsp;:</b> est-ce que quelqu'un change "
      + "d'endroit, ou change d'état&nbsp;? Si oui, <i>être</i>. Sinon, l'autre.",
    ],
    retenir: "Changer d'endroit ou changer d'état → <b>être</b>. "
           + "Un test vaut mieux qu'une liste&nbsp;: il marche sur un verbe que vous n'avez jamais vu.",
    attente: "Lisez, puis continuez.",
  },

  // ── 4. Le piège que le test ne couvre pas. ───────────────────────────────
  {
    id:   'les-deux',
    type: 'verif',
    eye:  'Le cas qui trompe',
    menu: 'Sortir, deux fois',
    titre: "« Sortir » avec être ou avec avoir ? Les deux — et le sens change.",
    consigne: "Amadou écrit à son propriétaire. Quelle phrase dit qu'il a <b>mis les poubelles "
            + "sur le trottoir</b>&nbsp;?",
    options: [
      { txt: "J'ai sorti les poubelles mardi soir.", juste: true },
      { txt: "Je suis sorti les poubelles mardi soir.",
        rat_t: "Cette phrase-là ne veut rien dire.",
        rat: "«&nbsp;Je suis sorti&nbsp;» est juste tout seul — c'est <i>lui</i> qui sort. Mais on "
           + "ne peut pas lui accrocher «&nbsp;les poubelles&nbsp;» derrière&nbsp;: il faudrait "
           + "comprendre qu'il est sorti <i>en étant</i> les poubelles." },
      { txt: "Je suis sorti mardi soir.",
        rat_t: "Juste, mais ce n'est pas ce qu'on demande.",
        rat: "Cette phrase dit qu'<b>Amadou</b> est sorti — lui, dehors, le soir. Elle ne dit rien "
           + "des poubelles. La question portait sur ce qu'il a déplacé." },
    ],
    pourquoi: "Quand le verbe est suivi de <b>ce qu'on déplace</b>, c'est <i>avoir</i>&nbsp;: "
            + "j'ai sorti les poubelles, j'ai monté la valise, j'ai descendu la boîte. "
            + "Sans complément, c'est <i>être</i>&nbsp;: je suis sorti, je suis monté. "
            + "Trois verbes seulement font ça — sortir, monter, descendre.",
    attente: "Choisissez une réponse pour continuer.",
  },

  // ── 5. L'accord, par le contraste, et sans tableau de formes. ────────────
  {
    id:   'la-lettre-muette',
    type: 'notion',
    eye:  'La deuxième moitié',
    menu: "La lettre qu'on n'entend pas",
    titre: "« Je suis allé » et « je suis allée » se prononcent exactement pareil.",
    paras: [
      "C'est pour ça que cette faute traverse des années sans jamais être corrigée&nbsp;: "
      + "à l'oral, il n'y a rien à entendre. Elle n'apparaît qu'au moment où vous écrivez.",

      "Avec <i>être</i>, la fin du participe suit la personne qui parle, <b>comme un adjectif</b>&nbsp;: "
      + "on écrit «&nbsp;elle est <b>grande</b>&nbsp;», on écrit «&nbsp;elle est <b>partie</b>&nbsp;». "
      + "Même mécanique, même lettre ajoutée.",

      "Teodora écrit&nbsp;: «&nbsp;<i>Je suis arrivée à huit heures et je suis restée jusqu'à midi.</i>&nbsp;» "
      + "Amadou écrit la même journée&nbsp;: «&nbsp;<i>Je suis arrivé à huit heures et je suis resté "
      + "jusqu'à midi.</i>&nbsp;» Une lettre, invisible à l'oreille, et pourtant on sait qui écrit.",
    ],
    retenir: "Avec <b>être</b>, la fin du participe dit <b>qui</b>. Avec l'autre, elle ne bouge pas.",
    attente: "Lisez, puis continuez.",
  },

  // ── 6. Trier des phrases écrites. ────────────────────────────────────────
  {
    id:   'tri-accord',
    type: 'tri',
    eye:  'À vous de trancher',
    menu: 'Six phrases',
    titre: "Six phrases écrites. Lesquelles sont correctes ?",
    consigne: "Regardez deux choses seulement&nbsp;: l'auxiliaire, puis la fin du participe.",
    colonnes: [
      { id: 'ok',   t: 'Correct',  b: 'Correct' },
      { id: 'faux', t: 'Une faute', b: 'Une faute' },
    ],
    items: [
      { txt: "Miriam est venue me voir hier.", ok: 'ok',
        rat: "<i>Venir</i> est un déplacement, donc <i>être</i>&nbsp;; et Miriam est une femme, "
           + "donc «&nbsp;venue&nbsp;». Les deux moitiés sont justes.",
        pourquoi: "Être + accord au féminin. Juste." },
      { txt: "Elle a partie à midi.", ok: 'faux',
        rat: "Deux fautes d'un coup&nbsp;: <i>partir</i> demande <i>être</i>, et avec l'autre "
           + "auxiliaire le participe ne prendrait pas de «&nbsp;e&nbsp;» de toute façon. "
           + "Il faut «&nbsp;elle est partie&nbsp;».",
        pourquoi: "Il faut « elle est partie »." },
      { txt: "J'ai oublié mon rendez-vous.", ok: 'ok',
        rat: "Rien ne se déplace, rien ne change d'état&nbsp;: c'est l'autre auxiliaire, et le "
           + "participe ne bouge pas. C'est correct, homme ou femme.",
        pourquoi: "Avoir, et rien ne bouge. Juste." },
      { txt: "Nous sommes arrivé en retard.", ok: 'faux',
        rat: "<i>Arriver</i> et <i>être</i>&nbsp;: bon. Mais «&nbsp;nous&nbsp;», c'est plusieurs "
           + "personnes — il manque le «&nbsp;s&nbsp;». «&nbsp;Nous sommes arrivés.&nbsp;»",
        pourquoi: "Il manque le « s » de « nous »." },
      { txt: "Teodora s'est levée à cinq heures.", ok: 'ok',
        rat: "Les verbes qui portent «&nbsp;se&nbsp;» — se lever, se présenter, s'absenter — "
           + "prennent <i>être</i> eux aussi, et s'accordent de la même façon.",
        pourquoi: "Un verbe en « se » : être, et l'accord suit." },
      { txt: "Elle est tombé dans l'escalier.", ok: 'faux',
        rat: "L'auxiliaire est bon — <i>tomber</i>, c'est un déplacement. C'est la fin qui manque&nbsp;: "
           + "«&nbsp;elle est tomb<b>ée</b>&nbsp;». C'est exactement la lettre qu'on n'entend pas.",
        pourquoi: "Il manque le « e » : elle est tombée." },
    ],
    attente: "Tranchez les six phrases pour continuer.",
  },

  // ── 7. Le cas le plus fréquent dans une vraie production. ────────────────
  {
    id:   'la-note',
    type: 'verif',
    eye:  'Vérification',
    menu: 'Une note à corriger',
    titre: "Miriam écrit à l'école. Une seule ligne est fautive.",
    consigne: "«&nbsp;<i>Bonjour, ma fille n'est pas venue hier. Elle est tombé dans l'escalier "
            + "et nous avons attendu deux heures à l'urgence. Elle est revenue à la maison "
            + "le soir.</i>&nbsp;»",
    options: [
      { txt: "« Elle est tombé dans l'escalier. »", juste: true },
      { txt: "« Nous avons attendu deux heures. »",
        rat_t: "Celle-là est juste.",
        rat: "<i>Attendre</i>&nbsp;: personne ne se déplace, personne ne change d'état. "
           + "L'autre auxiliaire, et le participe ne bouge pas — même si «&nbsp;nous&nbsp;» est "
           + "au pluriel. Rien à corriger." },
      { txt: "« Elle est revenue à la maison. »",
        rat_t: "Celle-là est juste aussi.",
        rat: "<i>Revenir</i> est un déplacement, donc <i>être</i>&nbsp;; «&nbsp;elle&nbsp;», donc "
           + "«&nbsp;revenue&nbsp;». Les deux moitiés sont bonnes." },
    ],
    pourquoi: "«&nbsp;Elle est <b>tombée</b>&nbsp;». L'auxiliaire était bon, c'est la lettre finale "
            + "qui manquait — et c'est presque toujours celle-là qui manque, parce qu'on ne "
            + "l'entend pas en se relisant à voix haute.",
    attente: "Choisissez une réponse pour continuer.",
  },

  // ── 8. « avoir », dit en dernier : c'est le cas par défaut. ──────────────
  {
    id:   'avoir-en-dernier',
    type: 'notion',
    eye:  'Ce qui reste',
    menu: 'Tout le reste',
    titre: "Tout le reste prend « avoir », et il ne se passe rien.",
    paras: [
      "On a gardé celui-ci pour la fin, et c'est volontaire&nbsp;: il n'y a <b>rien à retenir</b>. "
      + "Tous les autres verbes — la grande majorité — prennent <i>avoir</i>, et le participe "
      + "<b>ne bouge jamais</b>&nbsp;: j'ai téléphoné, elle a téléphoné, nous avons téléphoné, "
      + "elles ont téléphoné.",

      "Autrement dit, vous n'avez <b>qu'une seule chose</b> à surveiller quand vous écrivez&nbsp;: "
      + "les déplacements et les changements d'état. Partout ailleurs, écrivez sans y penser.",
    ],
    retenir: "Une règle, une exception. <b>L'exception, c'est le déplacement.</b> "
           + "Le reste s'écrit tout seul.",
    attente: "Lisez, puis continuez.",
  },

  // ── 9. Écrire, pas reconnaître. ──────────────────────────────────────────
  {
    id:   'a-vous-decrire',
    type: 'verif',
    eye:  'Vérification',
    menu: 'Votre phrase',
    titre: "Teodora raconte sa journée. Quelle suite est entièrement correcte ?",
    consigne: "Trois versions de la même journée. Une seule tient d'un bout à l'autre.",
    options: [
      { txt: "Je suis partie à sept heures, j'ai attendu l'autobus, et je suis arrivée en retard.",
        juste: true },
      { txt: "Je suis parti à sept heures, j'ai attendu l'autobus, et je suis arrivé en retard.",
        rat_t: "Les auxiliaires sont bons. C'est Teodora qui a disparu.",
        rat: "Trois auxiliaires justes — c'est déjà l'essentiel. Mais Teodora est une femme&nbsp;: "
           + "«&nbsp;parti<b>e</b>&nbsp;» et «&nbsp;arrivé<b>e</b>&nbsp;». «&nbsp;J'ai attendu&nbsp;» "
           + "reste tel quel, lui." },
      { txt: "J'ai partie à sept heures, j'ai attendu l'autobus, et j'ai arrivée en retard.",
        rat_t: "Les deux déplacements sont passés du mauvais côté.",
        rat: "<i>Partir</i> et <i>arriver</i> sont exactement les deux verbes de la phrase où "
           + "quelqu'un change d'endroit&nbsp;: ce sont les deux qui demandaient <i>être</i>. "
           + "Seul «&nbsp;attendre&nbsp;» était au bon endroit." },
    ],
    pourquoi: "Deux déplacements avec <i>être</i> et l'accord au féminin, une action ordinaire avec "
            + "l'autre et rien qui bouge. <b>C'est tout le parcours en une phrase.</b>",
    attente: "Choisissez une réponse pour continuer.",
  },

  // ── 10. La fermeture : le même cas qu'à l'écran 1. ───────────────────────
  {
    id:   'fermeture',
    type: 'verif',
    eye:  'La dernière',
    menu: 'Pour finir',
    titre: "On revient à la phrase du début. Miriam écrit à son employeur.",
    consigne: "Elle est restée chez elle mardi. Quelle phrase écrit-elle&nbsp;?",
    options: [
      { txt: "« Je suis restée à la maison mardi. »", juste: true },
      { txt: "« J'ai resté à la maison mardi. »",
        rat_t: "C'est la phrase de l'écran 1.",
        rat: "<i>Rester</i>, c'est ne pas se déplacer — et pourtant il prend <i>être</i>. "
           + "C'est le seul verbe de la famille qui résiste au test&nbsp;: retenez-le à part, "
           + "il revient sans arrêt." },
      { txt: "« Je suis resté à la maison mardi. »",
        rat_t: "L'auxiliaire est bon. Il manque la lettre qu'on n'entend pas.",
        rat: "Vous avez le plus difficile&nbsp;: <i>rester</i> avec <i>être</i>. Mais Miriam est "
           + "une femme&nbsp;: «&nbsp;rest<b>ée</b>&nbsp;». C'est la faute qui reste quand toutes "
           + "les autres sont réglées." },
    ],
    pourquoi: "«&nbsp;Je suis restée&nbsp;». Vous avez fait les deux moitiés&nbsp;: le bon "
            + "auxiliaire, et la fin qui dit qui écrit.",
    attente: "Choisissez une réponse pour finir.",
  },

];
