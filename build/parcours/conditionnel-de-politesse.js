// ═══════════════════════════════════════════════════════════════════════════
// Point express — Le conditionnel de politesse : je voudrais, pourriez-vous
//
// Savoir n7-s25. Une ORDONNANCE : l'enseignant l'envoie à un élève qu'il a
// entendu demander au présent, et qui ne sait pas l'effet qu'il produit.
// Dix minutes, dix écrans.
//
// ── Ce dont il s'écarte, et comment ────────────────────────────────────────
// Onze modules portent déjà une mini-leçon sur le conditionnel — n7-banque
// (« demander, supposer, ne pas s'engager »), n7-achat, n7-habitation,
// n7-logement, n7-emploi, n7-etablissement, n7-classe, n7-publicite,
// n7-actualite, n7-recherche, n8-recherche. Un élève envoyé ici en a
// très probablement lu deux. Toutes disent la même chose dans le même ordre :
// la forme d'abord (radical du futur, terminaisons de l'imparfait), puis les
// trois emplois (demander, supposer, annoncer), puis un tableau « sans / avec ».
// Les cinq écarts tenus :
//
//   1. INDUCTIF. L'élève tranche six situations AVANT qu'aucune règle ne soit
//      dite. La règle de l'écran 4 est écrite comme un constat de ce qu'il
//      vient de faire : « vous n'avez pas classé des verbes, vous avez classé
//      des rapports ».
//   2. UN SEUL EMPLOI SUR TROIS. Les mini-leçons traitent la demande, la
//      supposition et le chiffre annoncé. Ici, la demande seule — et
//      « si + imparfait » n'est pas mentionné une fois. Dix minutes ne
//      couvrent pas un temps, elles couvrent une situation.
//   3. LE DOSAGE, QUE PERSONNE NE TRAITE. Aucune des onze mini-leçons ne dit
//      qu'on peut en mettre trop. C'est pourtant la moitié du sujet à ce
//      niveau : l'élève qui a compris passe au tout-conditionnel et se met en
//      position basse — écrans 3, 8 et 10. Le présent y est la bonne réponse
//      trois fois.
//   4. LE MÉTALANGAGE ARRIVE APRÈS. « Conditionnel » n'est écrit qu'à
//      l'écran 4, une fois la chose manipulée ; la forme n'arrive qu'à
//      l'écran 5, et sur un seul piège (la lettre finale) plutôt qu'en
//      tableau de six personnes.
//   5. EXEMPLES PRIS À PLUSIEURS SITUATIONS — comptoir, urgence, courriel,
//      texto, entrevue. Un point express ne dépend d'aucun module.
//
// Extraits : ceux du module `module-n7-etablissement`, rejoués par chemin.
// Aucun média neuf. Le module a été choisi pour une raison précise : Rania y
// dit « je voudrais » et « je veux » à deux répliques d'intervalle, et les
// deux sont justes. C'est tout le point express en deux extraits.
// Les rangs sont ceux de `dialogues.js`, clés `prep`, `t2` et `t3`.
// ═══════════════════════════════════════════════════════════════════════════

const PARCOURS = {
  slug:     'conditionnel-de-politesse',
  module:   'module-n7-etablissement',   // d'où viennent les extraits, rien de plus
  titre:    "Demander sans brusquer",
  surtitre: "Point express · 10 minutes",
  niveau:   7,
  savoir:   'n7-s25',
};

const ECRANS = [

  // ── 1. On tranche AVANT de savoir. ───────────────────────────────────────
  {
    id:   'depart',
    type: 'verif',
    eye:  'Une question, pour commencer',
    menu: 'Au comptoir',
    titre: "Vous arrivez au comptoir d'un centre de formation. Vous ne connaissez personne. Vous dites quoi ?",
    consigne: "Répondez avec ce que vous savez déjà — ou au son. On expliquera après&nbsp;: "
            + "c'est fait exprès.",
    options: [
      { txt: "« Je veux un rendez-vous avec le conseiller. »",
        rat_t: "La phrase est correcte. C'est l'effet qui ne l'est pas.",
        rat: "Rien n'est faux là-dedans&nbsp;: la grammaire tient, on vous comprend, et vous "
           + "obtiendrez peut-être votre rendez-vous. Mais vous venez d'annoncer une décision à "
           + "quelqu'un qui n'a rien décidé. Personne ne vous le dira, et c'est bien le problème "
           + "— on note simplement que vous êtes brusque." },
      { txt: "« Je voudrais un rendez-vous avec le conseiller. »", juste: true },
      { txt: "« Les deux se disent, ça revient au même. »",
        rat_t: "Les deux se disent. Elles n'obtiennent pas la même chose.",
        rat: "Une lettre les sépare et personne ne les entend pareil. Écoutez-vous les employés "
           + "d'un comptoir&nbsp;: entre eux, ils disent «&nbsp;tu pourrais&nbsp;», jamais "
           + "«&nbsp;tu peux&nbsp;». Ce n'est pas de la décoration, c'est ce qui décide de la "
           + "suite de la conversation." },
    ],
    pourquoi: "«&nbsp;Je voudrais&nbsp;». Gardez la phrase entière pour l'instant&nbsp;; "
            + "on va voir juste après pourquoi elle passe et l'autre non.",
    attente: "Choisissez une réponse pour continuer.",
  },

  // ── 2. On écoute la même personne dire les deux, à deux répliques d'écart. ─
  {
    id:   'deux-repliques',
    type: 'notion',
    eye:  'Écoutez la même personne',
    menu: 'Deux répliques',
    titre: "Rania demande, puis Rania décide. Deux phrases, deux minutes d'écart.",
    paras: [
      "Rania veut retourner aux études. Elle en parle d'abord à une collègue. Écoutez sa "
      + "première phrase&nbsp;: elle <b>demande</b> quelque chose à quelqu'un.",

      "Écoutez maintenant la seconde, deux répliques plus loin, dans la même conversation. "
      + "Elle ne demande plus rien&nbsp;: elle <b>annonce sa décision</b>. Et là, elle ne prend "
      + "aucune précaution.",

      "Ce n'est pas qu'elle soit devenue impolie entre les deux. C'est qu'on ne parle pas de "
      + "la même chose. Retenez les deux phrases telles quelles pour l'instant&nbsp;; "
      + "on nommera la différence dans deux écrans.",
    ],
    sons: [
      { fichier: 'prep/line_01_rania.mp3', qui: 'Rania ouvre la conversation',
        texte: "Ghyslaine, tu as deux minutes ? Je voudrais te demander quelque chose, "
             + "et je ne sais pas à qui d'autre le demander." },
      { fichier: 'prep/line_03_rania.mp3', qui: 'Rania, deux répliques plus loin',
        texte: "Rien de grave. C'est pour le diplôme. Le programme de santé, assistance et "
             + "soins infirmiers, au centre de formation. Je veux le faire." },
    ],
    retenir: "«&nbsp;Je voudrais te demander&nbsp;» ouvre une porte chez l'autre. "
           + "«&nbsp;Je veux le faire&nbsp;» ne demande la permission de personne.",
    attente: "Écoutez les deux extraits, puis continuez.",
  },

  // ── 3. Le tri : six situations, et le présent gagne trois fois. ───────────
  {
    id:   'tri-situations',
    type: 'tri',
    eye:  'À vous de trancher',
    menu: 'Six situations',
    titre: "Six situations. Laquelle demande la forme prudente ?",
    consigne: "Aucune règle ne vous a été donnée — normal. Demandez-vous seulement une chose&nbsp;: "
            + "est-ce que l'autre personne peut dire non&nbsp;?",
    colonnes: [
      { id: 'prud', t: 'La forme prudente', b: 'La forme prudente' },
      { id: 'droit', t: 'Je le dis tout droit', b: 'Je le dis tout droit' },
    ],
    items: [
      { txt: "Au comptoir d'une clinique, vous demandez un rendez-vous", ok: 'prud',
        sous: "vous ne connaissez pas la personne",
        rat: "L'agente peut refuser, décaler, vous mettre sur une liste. Tout ce qu'elle peut "
           + "refuser se demande prudemment — et c'est justement pour ça qu'elle accepte.",
        pourquoi: "Elle peut dire non. Donc on demande." },
      { txt: "En entrevue, on vous demande pourquoi vous voulez ce poste", ok: 'droit',
        sous: "vous parlez de votre décision, pas d'une faveur",
        rat: "Ici, vous ne demandez rien&nbsp;: on vous demande ce que vous voulez. Répondre "
           + "prudemment donnerait l'impression que vous n'êtes pas sûr d'y tenir — et c'est "
           + "exactement ce qu'on cherche à savoir.",
        pourquoi: "Vous n'êtes pas en train de demander. Vous répondez." },
      { txt: "Un courriel à un employeur : deux questions sur l'horaire", ok: 'prud',
        sous: "vous écrivez à quelqu'un que vous n'avez jamais vu",
        rat: "À l'écrit, il n'y a ni sourire ni ton de voix pour rattraper. La forme prudente "
           + "est la seule chose qui reste pour dire que vous demandez au lieu d'exiger.",
        pourquoi: "À l'écrit, il n'y a que les mots. Donc on demande." },
      { txt: "À l'urgence, vous avez très mal et on vous demande ce qui vous amène", ok: 'droit',
        sous: "on vous demande ce qui se passe",
        rat: "Une douleur ne se raconte pas prudemment&nbsp;: «&nbsp;j'aurais un peu mal au "
           + "ventre&nbsp;» sera classé comme un petit problème, et vous attendrez. Dites ce "
           + "qui est. La politesse n'a rien à voir avec ça.",
        pourquoi: "Un fait n'est pas une demande. Dites-le tel quel." },
      { txt: "Vous n'avez pas saisi un chiffre : vous demandez qu'on répète", ok: 'prud',
        sous: "au téléphone, avec un fonctionnaire",
        rat: "Faire répéter, c'est demander à quelqu'un de refaire quelque chose qu'il vient "
           + "de faire. C'est petit, et c'est précisément là que la forme prudente coûte le "
           + "moins cher et rapporte le plus.",
        pourquoi: "Vous demandez un geste de plus. Donc on demande." },
      { txt: "Un texto à votre sœur : vous passez chercher les enfants", ok: 'droit',
        sous: "c'est convenu depuis lundi",
        rat: "Entre proches, et pour une chose déjà entendue, la forme prudente sonne froide "
           + "— comme si vous remettiez en question un arrangement qui tient. La politesse "
           + "excessive éloigne.",
        pourquoi: "Rien à négocier. Le présent, et c'est tout." },
    ],
    attente: "Tranchez les six situations pour continuer.",
  },

  // ── 4. La règle, écrite comme un constat, et la forme en deux lignes. ─────
  {
    id:   'le-constat',
    type: 'notion',
    eye:  'Ce que vous venez de faire',
    menu: 'Le constat',
    titre: "Vous n'avez pas classé des verbes. Vous avez classé des demandes.",
    paras: [
      "Regardez votre colonne prudente&nbsp;: le rendez-vous, le courriel, le chiffre à faire "
      + "répéter. <b>Dans les trois, l'autre personne peut dire non.</b> Dans les trois autres, "
      + "il n'y avait rien à refuser — un fait, une décision, un arrangement déjà pris.",

      "La forme prudente s'appelle le <b>conditionnel</b>, et vous n'avez pas besoin du nom "
      + "pour vous en servir. Votre enseignant l'emploiera&nbsp;; retenez plutôt la question, "
      + "qui marche sur n'importe quelle phrase&nbsp;: <b>est-ce que l'autre peut refuser&nbsp;?</b> "
      + "Si oui, conditionnel. Sinon, présent.",

      "Sa fabrication tient en une ligne, et c'est la seule ligne de grammaire de ce point "
      + "express&nbsp;: on prend le <b>radical du futur</b> et on y met les <b>terminaisons de "
      + "l'imparfait</b>. Je voudra<b>i</b> devient je voudra<b>is</b>&nbsp;; vous pourre<b>z</b> "
      + "devient vous pourri<b>ez</b>. Si vous savez dire une chose au futur, vous savez déjà "
      + "la dire au conditionnel.",
    ],
    retenir: "Une question, pas une liste&nbsp;: <b>l'autre peut-il dire non&nbsp;?</b> "
           + "Elle marche sur un verbe que vous n'avez jamais employé.",
    attente: "Lisez, puis continuez.",
  },

  // ── 5. La forme, sur son seul vrai piège : la lettre finale. ──────────────
  {
    id:   'la-lettre-finale',
    type: 'verif',
    eye:  'Le piège de la forme',
    menu: 'Une lettre',
    titre: "« Je voudrai » et « je voudrais » se prononcent presque pareil. Une seule demande quelque chose.",
    consigne: "Vous écrivez à la secrétaire d'un centre pour obtenir un formulaire. "
            + "Quelle ligne écrivez-vous&nbsp;?",
    options: [
      { txt: "« Je voudrais recevoir le formulaire d'inscription. »", juste: true },
      { txt: "« Je voudrai recevoir le formulaire d'inscription. »",
        rat_t: "Sans le «&nbsp;s&nbsp;», c'est du futur.",
        rat: "«&nbsp;Je voudrai&nbsp;» annonce ce que vous voudrez plus tard — la semaine "
           + "prochaine, peut-être. Vous n'avez rien demandé du tout, et la personne qui vous "
           + "lit ne saura pas quoi en faire. À l'oral, on ne vous reprendra pas&nbsp;; "
           + "à l'écrit, il manque une lettre et la demande disparaît." },
      { txt: "« Je voudrais recevoir le formulaire d'inscription, si ce n'est pas trop demander. »",
        rat_t: "La demande était déjà polie. Vous venez de vous excuser d'exister.",
        rat: "Un formulaire d'inscription est un droit, pas une faveur&nbsp;: le demander en "
           + "s'excusant fait douter qu'on y ait droit. On y revient à l'écran 8 — c'est la "
           + "seconde moitié de ce point express." },
    ],
    pourquoi: "Le «&nbsp;s&nbsp;» final est toute la différence entre <i>demander maintenant</i> "
            + "et <i>annoncer plus tard</i>. C'est la même lettre pour les six personnes&nbsp;: "
            + "-ais, -ais, -ait, -ions, -iez, -aient.",
    attente: "Choisissez une réponse pour continuer.",
  },

  // ── 6. Trois formules, et elles ne servent pas à la même chose. ───────────
  {
    id:   'trois-formules',
    type: 'notion',
    eye:  'Trois formules',
    menu: 'Les trois',
    titre: "Trois formules couvrent presque toutes vos demandes. Elles ne sont pas interchangeables.",
    paras: [
      "<b>Je voudrais</b> — ce que je viens chercher. Un rendez-vous, un papier, un "
      + "renseignement. C'est la formule du comptoir et du téléphone&nbsp;: elle nomme l'objet "
      + "de la visite, tout de suite, sans détour.",

      "<b>Pourriez-vous</b> — un geste que je demande à l'autre de faire. Répéter, vérifier, "
      + "m'envoyer, me mettre par écrit. La différence est là&nbsp;: «&nbsp;je voudrais&nbsp;» "
      + "porte sur une chose, «&nbsp;pourriez-vous&nbsp;» porte sur un travail.",

      "<b>J'aimerais</b> — ce vers quoi je vais, et qui ne se règlera pas aujourd'hui. "
      + "«&nbsp;J'aimerais reprendre mes études&nbsp;», «&nbsp;j'aimerais travailler de "
      + "jour&nbsp;». C'est la formule du projet, pas celle du guichet&nbsp;: demander un "
      + "formulaire avec «&nbsp;j'aimerais&nbsp;» fait flotter une demande qui était précise.",

      "Écoutez celle du milieu. Rania est en entrevue de sélection&nbsp;; elle demande une "
      + "information que ses interlocuteurs devront aller chercher.",
    ],
    sons: [
      { fichier: 't2/line_24_rania.mp3', qui: 'Rania, en entrevue',
        texte: "Deuxièmement, pourriez-vous me dire à quel moment le stage commence dans "
             + "l'année ?" },
    ],
    retenir: "Une chose → <b>je voudrais</b>. Un geste → <b>pourriez-vous</b>. "
           + "Un projet → <b>j'aimerais</b>.",
    attente: "Écoutez l'extrait, puis continuez.",
  },

  // ── 7. Choisir la bonne des trois, quand on insiste. ─────────────────────
  {
    id:   'insister',
    type: 'verif',
    eye:  'Vérification',
    menu: 'Insister',
    titre: "Vous rappelez pour la deuxième fois. Vous voulez une réponse, et vous ne voulez pas vous fâcher.",
    consigne: "Vous avez reçu une lettre qui ne dit presque rien. Écoutez Rania faire "
            + "exactement ça, puis choisissez votre phrase.",
    sons: [
      { fichier: 't3/line_04_rania.mp3', qui: 'Rania, au téléphone',
        texte: "La lettre dit que ma candidature est retenue et que je suis inscrite sur la "
             + "liste d'attente. Elle ne dit rien d'autre. Je voudrais savoir à quel rang je suis." },
    ],
    options: [
      { txt: "« Je voudrais savoir où en est mon dossier. »", juste: true },
      { txt: "« J'aimerais bien savoir où en est mon dossier, un jour. »",
        rat_t: "«&nbsp;J'aimerais&nbsp;» transforme votre demande en souhait.",
        rat: "Vous ne dites plus ce que vous venez chercher&nbsp;: vous dites ce qui vous "
           + "ferait plaisir. La personne au bout du fil peut vous répondre «&nbsp;je comprends "
           + "madame&nbsp;» et ne rien faire — vous ne lui avez rien demandé. Gardez "
           + "«&nbsp;j'aimerais&nbsp;» pour les projets." },
      { txt: "« Je veux savoir où en est mon dossier. »",
        rat_t: "Vous obtiendrez peut-être une réponse. Vous n'obtiendrez rien de plus.",
        rat: "Au deuxième appel, «&nbsp;je veux&nbsp;» s'entend comme un reproche à quelqu'un "
           + "qui n'a rien décidé — l'agente n'a pas fait la liste d'attente. Or c'est elle qui "
           + "peut vous dire ce que la lettre ne dit pas, et prendre le message pour la "
           + "personne qui, elle, décide. Rania obtient un rappel&nbsp;; elle ne l'aurait pas eu "
           + "autrement." },
    ],
    pourquoi: "Insister et demander prudemment ne s'opposent pas&nbsp;: Rania <b>redit deux fois</b> "
            + "ce que la lettre ne dit pas, et elle demande au conditionnel. C'est la répétition "
            + "qui insiste, pas le ton.",
    attente: "Choisissez une réponse pour continuer.",
  },

  // ── 8. Le dosage : la moitié du sujet, et personne ne la traite. ─────────
  {
    id:   'trop',
    type: 'verif',
    eye:  'Le cas qui trompe',
    menu: 'Trop poli',
    titre: "En entrevue, on vous demande pourquoi vous voulez cette formation.",
    consigne: "Trois réponses. Une seule vous laisse debout. Écoutez d'abord celle de Rania&nbsp;: "
            + "aucun conditionnel dans sa phrase, et c'est voulu.",
    sons: [
      { fichier: 't2/line_05_rania.mp3', qui: 'Rania, devant le comité',
        texte: "Je suis préposée aux bénéficiaires depuis cinq ans. Ce que je fais aujourd'hui, "
             + "je le fais bien, mais je m'arrête toujours au même endroit : quand il faut "
             + "donner un médicament, faire un pansement ou noter un signe, je vais chercher "
             + "quelqu'un d'autre. Je veux être celle qu'on va chercher." },
    ],
    options: [
      { txt: "« Je veux faire ce métier au complet, pas la moitié. »", juste: true },
      { txt: "« Je voudrais peut-être faire ce métier, si c'était possible. »",
        rat_t: "Trois précautions dans une phrase de dix mots.",
        rat: "«&nbsp;Voudrais&nbsp;», «&nbsp;peut-être&nbsp;», «&nbsp;si c'était "
           + "possible&nbsp;»&nbsp;: chacune prise seule est correcte, les trois ensemble "
           + "annulent la phrase. On vous demandait ce que vous voulez et vous avez répondu que "
           + "vous n'êtes pas sûr. Un comité qui choisit vingt-quatre personnes sur soixante-dix "
           + "retient celles qui finissent." },
      { txt: "« J'aimerais bien, oui. »",
        rat_t: "«&nbsp;J'aimerais bien&nbsp;» est la formule du souhait vague.",
        rat: "Elle convient pour un projet lointain — «&nbsp;j'aimerais un jour travailler de "
           + "jour&nbsp;». Devant un comité de sélection, elle dit que vous n'avez pas encore "
           + "décidé. Et vous, vous avez décidé&nbsp;: vous êtes assis dans la salle." },
    ],
    pourquoi: "<b>Trop de conditionnel vous met en position basse.</b> Il sert à demander à "
            + "quelqu'un qui peut refuser — pas à parler de ce que vous voulez. Quand on vous "
            + "demande votre décision, répondez au présent&nbsp;: c'est la seule fois où "
            + "«&nbsp;je veux&nbsp;» est la bonne réponse, et c'est une fois importante.",
    attente: "Choisissez une réponse pour continuer.",
  },

  // ── 9. Écrire, pas reconnaître : un courriel entier. ─────────────────────
  {
    id:   'le-courriel',
    type: 'verif',
    eye:  'Vérification',
    menu: 'Un courriel',
    titre: "Un courriel de quatre lignes à un employeur. Une seule ligne est à changer.",
    consigne: "«&nbsp;<i>Bonjour, j'ai vu votre affiche pour le poste de soir. Je travaille en "
            + "entretien depuis quatre ans. Je veux que vous m'envoyiez le formulaire de "
            + "candidature. J'aimerais commencer dès que possible.</i>&nbsp;»",
    options: [
      { txt: "La troisième : « Je veux que vous m'envoyiez le formulaire. »", juste: true },
      { txt: "La deuxième : « Je travaille en entretien depuis quatre ans. »",
        rat_t: "Celle-là est juste.",
        rat: "C'est un fait, daté, vérifiable — exactement ce qu'un employeur cherche. "
           + "Un fait ne se met pas au conditionnel&nbsp;: «&nbsp;je travaillerais en entretien "
           + "depuis quatre ans&nbsp;» laisserait croire que vous n'en êtes pas sûr, ou pire, "
           + "que quelqu'un l'a dit sans que ce soit vérifié." },
      { txt: "La quatrième : « J'aimerais commencer dès que possible. »",
        rat_t: "Celle-là est juste aussi.",
        rat: "C'est un projet, pas une demande de guichet — «&nbsp;j'aimerais&nbsp;» est à sa "
           + "place. Elle dit votre disponibilité sans exiger une date de quelqu'un qui n'a pas "
           + "encore lu votre candidature." },
    ],
    pourquoi: "«&nbsp;<b>Pourriez-vous m'envoyer le formulaire de candidature&nbsp;?</b>&nbsp;» "
            + "— c'est un geste que vous demandez à l'autre de faire, donc «&nbsp;pourriez-vous&nbsp;». "
            + "Les trois autres lignes ne demandaient rien&nbsp;: un fait, un projet, une "
            + "présentation. <b>On ne met pas tout au conditionnel, on met la demande.</b>",
    attente: "Choisissez une réponse pour continuer.",
  },

  // ── 10. La fermeture : le comptoir de l'écran 1, une marche plus haut. ────
  {
    id:   'fermeture',
    type: 'verif',
    eye:  'La dernière',
    menu: 'Pour finir',
    titre: "On revient au comptoir. Vous avez demandé votre rendez-vous, et on vous répond qu'il n'y a plus rien avant mars.",
    consigne: "Vous êtes disponible tous les soirs et personne ne vous l'a demandé. Vous dites quoi&nbsp;?",
    options: [
      { txt: "« Je suis libre tous les soirs. Pourriez-vous regarder s'il y a quelque chose en soirée ? »",
        juste: true },
      { txt: "« Je voudrais peut-être savoir s'il n'y aurait pas éventuellement autre chose. »",
        rat_t: "Quatre précautions, et aucune information.",
        rat: "Vous n'avez pas dit la seule chose qui pouvait changer la réponse&nbsp;: que vos "
           + "soirées sont libres. L'agente ne peut rien chercher avec ça. C'est le défaut de "
           + "l'écran 8, cette fois au comptoir&nbsp;: à force de précautions, la demande "
           + "disparaît." },
      { txt: "« Ce n'est pas possible, j'en ai besoin avant. »",
        rat_t: "Vous fermez une porte qui était ouverte.",
        rat: "L'agente vient de vous dire ce qu'elle voit à l'écran&nbsp;; elle n'a pas fait "
           + "l'horaire. Lui dire que ce n'est pas possible ne lui donne rien à faire, et elle "
           + "n'ira pas chercher les créneaux du soir. Dites ce que vous pouvez, et demandez-lui "
           + "le geste." },
    ],
    pourquoi: "Un fait au présent — <i>je suis libre tous les soirs</i> — puis la demande au "
            + "conditionnel — <i>pourriez-vous regarder</i>. <b>C'est tout le point express en une "
            + "phrase&nbsp;: le conditionnel sur ce que l'autre peut refuser, le présent sur "
            + "tout le reste.</b>",
    attente: "Choisissez une réponse pour finir.",
  },

];
