// ═══════════════════════════════════════════════════════════════════════════
// Point express — Transmettre un message sans en changer le sens
//
// Savoir n4-s13 (Phrases subordonnées à verbe conjugué) : « reconnaître des
// subordonnées à verbe conjugué CD », « employer des subordonnées à verbe
// conjugué ». Une ORDONNANCE : l'enseignant l'envoie à un élève qui écrit
// « Le propriétaire dit : je vais réparer » dans un courriel, ou qui rapporte
// un message en gardant le « je » de celui qui a parlé.
//
// ── Ce qui le sépare des mini-leçons existantes ────────────────────────────
// Le dépôt en porte sept : « Rapporter ce qu'on vous a dit », « Rapporter ce
// que la personne a dit », « Rapporter ce qui a été dit, par écrit »,
// « Rapporter une question sans point d'interrogation », « Rapporter au passé :
// tout recule d'un cran », « Rapporter des paroles quand le récit est au
// passé », « que, si, ce que — les trois portes du discours rapporté ».
// Cinq d'entre elles enseignent d'abord LA CONCORDANCE DES TEMPS — le tableau
// où le présent devient imparfait, le passé composé plus-que-parfait — et
// c'est justement ce qu'un élève de niveau 4 n'a pas à savoir : au moment où
// il rapporte, il rapporte le jour même, avec « il dit que », et RIEN NE
// RECULE. La leçon lui donne un tableau à six lignes pour un cas qu'il ne
// rencontrera pas avant deux niveaux.
//
// Ce point-ci reste au PRÉSENT d'un bout à l'autre et ne traite que DEUX
// gestes. Les cinq écarts tenus :
//
//   1. INDUCTIF, ET SUR LE DÉCODAGE. Écran 2 : huit messages rapportés, à
//      ranger selon QUI fait l'action. C'est ce que l'élève rate quand une
//      secrétaire lui transmet un message, et aucune leçon ne le fait faire.
//   2. DEUX GESTES, PAS UN TABLEAU : coller « que », changer les personnes.
//      Rien d'autre. Le temps du verbe ne bouge pas, et c'est dit explicitement
//      pour éviter la sur-correction.
//   3. LA CONCORDANCE DES TEMPS EST ÉCARTÉE, et l'écran 5 dit pourquoi : elle
//      n'arrive que si le verbe qui rapporte est au passé. Un point express
//      est partiel, et c'est la partie qui sert aujourd'hui.
//   4. LE MÉTALANGAGE ARRIVE APRÈS, à l'écran 3, une fois huit messages triés.
//   5. EXEMPLES VARIÉS : un message du secrétariat de l'école, un propriétaire
//      dans un couloir, une pharmacienne, un contremaître, un texto de voisin.
//
// Aucun média : ce qui manque à l'élève, c'est de refaire la phrase — pas de
// l'entendre.
// ═══════════════════════════════════════════════════════════════════════════

const PARCOURS = {
  slug:     'il-dit-qu-il',
  titre:    "Transmettre un message sans en changer le sens",
  surtitre: "Point express · 10 minutes",
  niveau:   4,
  savoir:   'n4-s13',
};

const ECRANS = [

  // ── 1. Une décision, sans aucune règle donnée. ───────────────────────────
  {
    id:   'depart',
    type: 'verif',
    eye:  'Une question, pour commencer',
    menu: 'Le voisin',
    titre: "Votre voisin vous arrête dans l'escalier : « Je passe à cinq heures. »",
    consigne: "Vous rentrez et vous répétez le message à la personne avec qui vous vivez. "
            + "Répondez avec ce que vous savez déjà — ou au feeling. On expliquera "
            + "après&nbsp;: c'est fait exprès.",
    options: [
      { txt: "«&nbsp;Il dit qu'il passe à cinq heures.&nbsp;»", juste: true },
      { txt: "«&nbsp;Il dit que je passe à cinq heures.&nbsp;»",
        rat_t: "C'est la faute que ce point vient corriger, et elle change tout.",
        rat: "Vous avez gardé le «&nbsp;je&nbsp;» de votre voisin. Mais dans votre bouche, "
           + "«&nbsp;je&nbsp;» veut dire <b>vous</b>&nbsp;: la personne comprend que c'est vous "
           + "qui sortez à cinq heures. Le message ne s'est pas seulement abîmé, il s'est "
           + "retourné." },
      { txt: "«&nbsp;Il dit&nbsp;: je passe à cinq heures.&nbsp;»",
        rat_t: "À l'oral, on vous comprendra. À l'écrit, c'est autre chose.",
        rat: "Répéter les mots exacts derrière deux points, c'est ce que fait un journal quand "
           + "il cite quelqu'un. Dans un message ordinaire, personne ne marque la pause qu'il "
           + "faudrait, et l'auditeur entend le «&nbsp;je&nbsp;» comme le vôtre. C'est la même "
           + "confusion que ci-dessus, en moins visible." },
    ],
    pourquoi: "«&nbsp;Il dit <b>qu'il</b> passe.&nbsp;» Gardez la scène&nbsp;: on y revient au "
            + "dernier écran.",
    attente: "Choisissez une réponse pour continuer.",
  },

  // ── 2. On trie AVANT de savoir. ──────────────────────────────────────────
  {
    id:   'tri-huit',
    type: 'tri',
    eye:  'À vous de trancher',
    menu: 'Huit messages',
    titre: "Huit messages qu'on vous transmet. Qui doit faire quelque chose ?",
    consigne: "Aucune règle ne vous a été donnée — normal. Lisez chaque message comme s'il vous "
            + "était dit ce matin, et demandez-vous&nbsp;: est-ce que je dois bouger, ou "
            + "est-ce que quelqu'un d'autre s'en occupe&nbsp;?",
    colonnes: [
      { id: 'lui', t: "C'est la personne qui a parlé", b: "C'est elle" },
      { id: 'moi', t: "C'est moi",                     b: "C'est moi" },
    ],
    items: [
      { txt: "Le médecin dit qu'il vous rappelle demain.", sous: "au comptoir d'une clinique", ok: 'lui',
        rat: "«&nbsp;Il&nbsp;» désigne le médecin, qui vient d'être nommé. C'est lui qui "
           + "compose le numéro&nbsp;: vous n'avez rien à faire qu'attendre.",
        pourquoi: "« il » renvoie au médecin : c'est lui qui appelle." },
      { txt: "Le médecin dit que vous le rappelez demain.", sous: "le même comptoir, autre patient", ok: 'moi',
        rat: "Deux mots ont changé, et la journée aussi&nbsp;: c'est vous qui devez téléphoner. "
           + "Un message mal transmis, ici, c'est un rendez-vous perdu.",
        pourquoi: "« vous » : le téléphone, c'est vous." },
      { txt: "Le propriétaire dit qu'il envoie un plombier jeudi.", sous: "un mot d'un voisin", ok: 'lui',
        rat: "Le propriétaire s'engage lui-même. Vous n'avez ni à appeler ni à payer&nbsp;: "
           + "vous avez à être là jeudi.",
        pourquoi: "Le propriétaire s'engage lui-même." },
      { txt: "Le propriétaire dit que vous devez appeler un plombier.", sous: "le même immeuble, autre logement", ok: 'moi',
        rat: "Le même homme, la même semaine, et la charge a changé de côté. C'est le genre de "
           + "message qu'il faut savoir lire du premier coup.",
        pourquoi: "La charge est sur vous." },
      { txt: "La secrétaire dit qu'elle a envoyé le bulletin par la poste.", sous: "un appel de l'école", ok: 'lui',
        rat: "«&nbsp;Elle&nbsp;» renvoie à la secrétaire, qui raconte ce qu'elle a fait. Rien "
           + "ne vous est demandé.",
        pourquoi: "Elle raconte ce qu'elle a fait." },
      { txt: "La secrétaire dit que vous devez signer le bulletin.", sous: "le même appel, une minute plus tard", ok: 'moi',
        rat: "Le verbe «&nbsp;devoir&nbsp;» et le mot «&nbsp;vous&nbsp;» disent ensemble que "
           + "c'est votre geste. C'est ce qu'on cherche quand on écoute un message&nbsp;: "
           + "est-ce qu'il y a quelque chose à faire pour moi&nbsp;?",
        pourquoi: "« vous devez » : c'est votre geste." },
      { txt: "Mon contremaître dit qu'il commence à sept heures.", sous: "un collègue, au vestiaire", ok: 'lui',
        rat: "Celui-là trompe souvent&nbsp;: on entend une heure et on croit que c'est la "
           + "sienne. Mais le mot employé est «&nbsp;il&nbsp;», et il renvoie au contremaître.",
        pourquoi: "« il » renvoie au contremaître." },
      { txt: "Mon contremaître dit que nous commençons à sept heures.", sous: "le même collègue, le lendemain", ok: 'moi',
        rat: "«&nbsp;Nous&nbsp;» vous inclut&nbsp;: vous êtes dans l'équipe. Un seul mot "
           + "sépare cette phrase de la précédente, et il décide de votre heure de réveil.",
        pourquoi: "« nous » vous inclut." },
    ],
    attente: "Tranchez les huit messages pour continuer.",
  },

  // ── 3. La règle, écrite comme un constat. ────────────────────────────────
  {
    id:   'les-deux-gestes',
    type: 'notion',
    eye:  'Ce que vous venez de faire',
    menu: 'Deux gestes',
    titre: "Vous n'avez pas lu le message. Vous avez cherché une seule chose : le petit mot.",
    paras: [
      "Chaque fois, ce qui décidait était le mot juste après «&nbsp;que&nbsp;» — <b>il</b>, "
      + "<b>elle</b>, <b>vous</b>, <b>nous</b>. Le reste de la phrase était presque identique. "
      + "Ce petit mot est donc ce qu'il faut choisir avec le plus de soin quand c'est vous qui "
      + "transmettez.",

      "<b>Rapporter un message tient en deux gestes.</b> Premier geste&nbsp;: coller "
      + "<b>que</b> après le verbe qui rapporte — «&nbsp;il dit <b>que</b>…&nbsp;», "
      + "«&nbsp;elle explique <b>que</b>…&nbsp;». Second geste&nbsp;: <b>changer les "
      + "personnes</b>, parce que ce n'est plus la même bouche qui parle. Le "
      + "«&nbsp;je&nbsp;» de l'autre devient «&nbsp;il&nbsp;» ou «&nbsp;elle&nbsp;»&nbsp;; son "
      + "«&nbsp;tu&nbsp;» devient «&nbsp;je&nbsp;» ou «&nbsp;vous&nbsp;»&nbsp;; son "
      + "«&nbsp;mon&nbsp;» devient «&nbsp;son&nbsp;».",

      "Ce que vous fabriquez ainsi s'appelle une <b>subordonnée</b>&nbsp;: une petite phrase "
      + "glissée dans une plus grande. Votre enseignant emploiera le mot&nbsp;; vous n'en avez "
      + "pas besoin pour transmettre un message juste.",
    ],
    retenir: "Deux gestes&nbsp;: coller <b>que</b>, puis <b>changer les personnes</b>. "
           + "«&nbsp;<i>Je passe</i>&nbsp;» → «&nbsp;il dit <b>qu'il</b> passe&nbsp;».",
    attente: "Lisez, puis continuez.",
  },

  // ── 4. Le « que » qu'on n'a pas dans toutes les langues. ─────────────────
  {
    id:   'le-que',
    type: 'verif',
    eye:  'Le premier geste',
    menu: 'Le « que »',
    titre: "La pharmacienne vous dit : « Le médicament arrive vendredi. »",
    consigne: "Vous rapportez la phrase à la personne qui vous accompagne.",
    options: [
      { txt: "«&nbsp;Elle dit que le médicament arrive vendredi.&nbsp;»", juste: true },
      { txt: "«&nbsp;Elle dit le médicament arrive vendredi.&nbsp;»",
        rat_t: "Beaucoup de langues laissent tomber ce mot&nbsp;; le français, jamais.",
        rat: "Sans lui, deux verbes se suivent sans rien qui les relie — «&nbsp;dit&nbsp;» et "
           + "«&nbsp;arrive&nbsp;» — et la phrase reste en suspens à l'oreille d'un "
           + "francophone. Le mot «&nbsp;que&nbsp;» est l'attache, et il ne se supprime pas, "
           + "même à l'oral le plus familier." },
      { txt: "«&nbsp;Elle dit&nbsp;: que le médicament arrive vendredi.&nbsp;»",
        rat_t: "Vous avez posé les deux constructions l'une sur l'autre.",
        rat: "Les deux points servent à citer les mots exacts — et alors il n'y a pas de "
           + "«&nbsp;que&nbsp;». Le «&nbsp;que&nbsp;» sert à rapporter — et alors il n'y a pas "
           + "de deux points. Il faut choisir&nbsp;: dans un message ordinaire, c'est toujours "
           + "le second." },
    ],
    pourquoi: "Le «&nbsp;que&nbsp;» ne s'omet jamais en français. C'est le seul mot du point "
            + "qui ne demande aucune réflexion&nbsp;: on le pose, toujours.",
    attente: "Choisissez une réponse pour continuer.",
  },

  // ── 5. Ce qui ne bouge pas — et pourquoi on le dit. ──────────────────────
  {
    id:   'ce-qui-ne-bouge-pas',
    type: 'notion',
    eye:  'Ce qui ne bouge pas',
    menu: 'Le verbe reste',
    titre: "Le temps du verbe ne change pas. Ni « demain », ni « ici ».",
    paras: [
      "C'est la bonne nouvelle de ce point, et elle mérite d'être dite parce que beaucoup "
      + "d'élèves corrigent trop&nbsp;: quand vous rapportez avec «&nbsp;<b>il dit "
      + "que</b>&nbsp;», au présent, <b>rien ne recule</b>. «&nbsp;<i>Je viens</i>&nbsp;» → "
      + "«&nbsp;il dit qu'il <b>vient</b>&nbsp;». «&nbsp;<i>J'ai payé</i>&nbsp;» → "
      + "«&nbsp;il dit qu'il <b>a payé</b>&nbsp;».",

      "Les mots de temps et de lieu ne bougent pas non plus, tant que vous rapportez le jour "
      + "même et au même endroit&nbsp;: «&nbsp;<i>Je passe <b>demain</b></i>&nbsp;» → "
      + "«&nbsp;il dit qu'il passe <b>demain</b>&nbsp;». Vous n'avez donc que les personnes à "
      + "surveiller.",

      "Il existe bien un cas où tout recule d'un cran — «&nbsp;il a dit qu'il "
      + "<i>venait</i>&nbsp;» — mais il n'arrive que si le verbe qui rapporte est lui-même au "
      + "passé. Ce n'est pas ce que vous faites en transmettant un message reçu il y a dix "
      + "minutes&nbsp;: c'est un autre sujet, pour un autre jour.",
    ],
    retenir: "Verbe qui rapporte au <b>présent</b>&nbsp;: rien ne recule. Seules les "
           + "<b>personnes</b> changent.",
    attente: "Lisez, puis continuez.",
  },

  // ── 6. Trier des phrases écrites. ────────────────────────────────────────
  {
    id:   'tri-ecrites',
    type: 'tri',
    eye:  'À vous de trancher',
    menu: 'Six phrases',
    titre: "Six messages rapportés par écrit. Lesquels tiennent ?",
    consigne: "Deux choses&nbsp;: le «&nbsp;que&nbsp;» est-il là, et les personnes ont-elles "
            + "changé de bouche&nbsp;?",
    colonnes: [
      { id: 'ok',   t: 'Correct',   b: 'Correct' },
      { id: 'faux', t: 'Une faute', b: 'Une faute' },
    ],
    items: [
      { txt: "Ma sœur dit qu'elle arrive vendredi avec ses enfants.", ok: 'ok',
        rat: "«&nbsp;Que&nbsp;» est là, «&nbsp;je&nbsp;» est devenu «&nbsp;elle&nbsp;», et "
           + "«&nbsp;mes enfants&nbsp;» est devenu «&nbsp;ses enfants&nbsp;». Les deux gestes "
           + "sont faits.",
        pourquoi: "Les deux gestes sont faits, possessif compris." },
      { txt: "Le contremaître dit je dois rester jusqu'à six heures.", ok: 'faux',
        rat: "Le «&nbsp;que&nbsp;» manque, et sans lui les deux verbes se cognent. Il faut "
           + "«&nbsp;dit <b>que</b> je dois rester&nbsp;» — la personne, elle, est juste&nbsp;: "
           + "c'est bien vous qui restez.",
        pourquoi: "Il manque « que » : dit que je dois rester." },
      { txt: "L'école dit que vous devez apporter une preuve d'adresse.", ok: 'ok',
        rat: "Le message est transmis à la bonne personne&nbsp;: c'est le parent qui apporte le "
           + "papier, et le «&nbsp;vous&nbsp;» le dit.",
        pourquoi: "« vous » désigne bien celui qui doit agir." },
      { txt: "Mon voisin dit que je répare la porte moi-même.", ok: 'faux',
        rat: "Cette phrase peut être correcte — mais seulement si votre voisin vous a vraiment "
           + "renvoyé la charge. Si c'est <b>lui</b> qui a dit «&nbsp;je répare la "
           + "porte&nbsp;», le «&nbsp;je&nbsp;» devait devenir «&nbsp;il&nbsp;»&nbsp;: "
           + "«&nbsp;dit <b>qu'il</b> répare&nbsp;». C'est exactement le retournement de "
           + "l'écran 1.",
        pourquoi: "Le « je » du voisin devient « il »." },
      { txt: "La pharmacienne dit qu'elle a commandé le médicament hier.", ok: 'ok',
        rat: "Le passé composé est resté tel quel, et c'est juste&nbsp;: le verbe qui rapporte "
           + "est au présent, donc rien ne recule.",
        pourquoi: "Le passé composé reste : rien ne recule." },
      { txt: "Le médecin dit qu'il vient et que je dois attendre dans le corridor.", ok: 'ok',
        rat: "Deux messages dans la même phrase, chacun avec son «&nbsp;que&nbsp;» et sa "
           + "personne. Le second «&nbsp;que&nbsp;» n'est pas facultatif&nbsp;: on le répète à "
           + "chaque morceau rapporté.",
        pourquoi: "Deux morceaux, deux « que » : correct." },
    ],
    attente: "Tranchez les six phrases pour continuer.",
  },

  // ── 7. Le piège : une consigne ne se rapporte pas avec « que ». ──────────
  {
    id:   'que-ou-de',
    type: 'verif',
    eye:  'Le piège',
    menu: '« que » ou « de »',
    titre: "Le contremaître vous dit : « Apportez vos bottes demain. »",
    consigne: "Ce n'est plus une information&nbsp;: c'est une consigne. Vous la transmettez à un "
            + "collègue absent.",
    options: [
      { txt: "«&nbsp;Il dit d'apporter nos bottes demain.&nbsp;»", juste: true },
      { txt: "«&nbsp;Il dit que apportez vos bottes demain.&nbsp;»",
        rat_t: "Vous avez posé le «&nbsp;que&nbsp;» — et laissé la consigne telle quelle.",
        rat: "Après «&nbsp;que&nbsp;», il faut une phrase avec un sujet&nbsp;: "
           + "«&nbsp;qu'<b>on</b> apporte&nbsp;», «&nbsp;que <b>nous devons</b> "
           + "apporter&nbsp;». Une consigne n'a pas de sujet écrit, donc elle ne peut pas se "
           + "glisser derrière «&nbsp;que&nbsp;» sans être refaite. Il existe un chemin plus "
           + "court&nbsp;: <b>de</b> + le verbe à l'infinitif." },
      { txt: "«&nbsp;Il dit qu'il apporte ses bottes demain.&nbsp;»",
        rat_t: "Les deux gestes sont bien faits — sur le mauvais message.",
        rat: "Vous avez transformé une consigne en information, et vous avez mis les bottes "
           + "sur le dos du contremaître. Votre collègue arrivera en espadrilles. Quand le "
           + "message demande une <b>action</b>, il se rapporte avec «&nbsp;de&nbsp;» + "
           + "l'infinitif." },
    ],
    pourquoi: "Une information&nbsp;→ «&nbsp;il dit <b>que</b>…&nbsp;». Une "
            + "consigne&nbsp;→ «&nbsp;il dit <b>de</b> + verbe&nbsp;»&nbsp;: "
            + "«&nbsp;il dit d'apporter&nbsp;», «&nbsp;elle dit de rappeler&nbsp;».",
    attente: "Choisissez une réponse pour continuer.",
  },

  // ── 8. Le verbe qui rapporte, dit en dernier. ────────────────────────────
  {
    id:   'le-verbe-qui-rapporte',
    type: 'notion',
    eye:  'Ce qui reste',
    menu: 'Autre chose que « dire »',
    titre: "« Dire » convient partout — et c'est justement pour ça qu'il ne dit rien.",
    paras: [
      "On a gardé ceci pour la fin&nbsp;: ce n'est pas une règle, c'est ce qui sépare un "
      + "message transmis d'un message <b>utile</b>. Le verbe qui rapporte peut porter, en un "
      + "mot, ce que la personne faisait en parlant.",

      "«&nbsp;Il <b>explique</b> qu'il n'a pas reçu la lettre.&nbsp;» (il se justifie) — "
      + "«&nbsp;Il <b>promet</b> qu'il envoie un plombier jeudi.&nbsp;» (il s'engage) — "
      + "«&nbsp;Elle <b>prévient</b> que le bureau ferme à midi.&nbsp;» (elle avertit d'avance) "
      + "— «&nbsp;Il <b>répond</b> qu'il ne peut rien faire.&nbsp;» (on lui avait demandé "
      + "quelque chose). La construction ne change pas d'un iota&nbsp;: le "
      + "«&nbsp;que&nbsp;» reste, les personnes changent comme avant.",

      "Cela compte surtout par écrit. Dans une plainte ou un courriel au travail, "
      + "«&nbsp;le propriétaire <b>a promis</b> qu'il ferait la réparation&nbsp;» pèse autrement "
      + "que «&nbsp;il a dit&nbsp;» — et c'est vrai, ce qui est la seule raison de "
      + "l'écrire. Vous n'avez donc <b>qu'une chose</b> à vous demander de plus&nbsp;: "
      + "qu'est-ce que la personne faisait en parlant&nbsp;?",
    ],
    retenir: "Même construction, verbe plus précis&nbsp;: <b>expliquer</b>, <b>promettre</b>, "
           + "<b>prévenir</b>, <b>répondre</b>. C'est ce qui rend un rapport écrit crédible.",
    attente: "Lisez, puis continuez.",
  },

  // ── 9. Écrire, pas reconnaître. ──────────────────────────────────────────
  {
    id:   'votre-message',
    type: 'verif',
    eye:  'Vérification',
    menu: 'Votre courriel',
    titre: "Vous écrivez au secrétariat de l'école. Quelle version tient d'un bout à l'autre ?",
    consigne: "Le médecin vous a dit&nbsp;: «&nbsp;<i>Votre fille peut retourner en classe lundi. "
            + "Je prépare un billet.</i>&nbsp;»",
    options: [
      { txt: "«&nbsp;Le médecin dit que ma fille peut retourner en classe lundi et qu'il "
           + "prépare un billet.&nbsp;»", juste: true },
      { txt: "«&nbsp;Le médecin dit que votre fille peut retourner en classe lundi et que je "
           + "prépare un billet.&nbsp;»",
        rat_t: "Les deux personnes sont restées dans la bouche du médecin.",
        rat: "«&nbsp;Votre fille&nbsp;» désignait la vôtre quand le médecin parlait&nbsp;; "
           + "écrit par vous à l'école, il désigne la fille de la secrétaire. Et "
           + "«&nbsp;je prépare un billet&nbsp;» fait de vous celui qui rédige le document "
           + "médical. Les deux gestes du point sont là&nbsp;: c'est le second qui manque." },
      { txt: "«&nbsp;Le médecin dit&nbsp;: ma fille peut retourner en classe lundi, je prépare "
           + "un billet.&nbsp;»",
        rat_t: "Vous avez changé les personnes — et vous les avez mises entre les mots du "
           + "médecin.",
        rat: "Derrière deux points, on écrit les mots <b>exacts</b> de la personne. Or le "
           + "médecin n'a jamais dit «&nbsp;ma fille&nbsp;». La phrase se présente comme une "
           + "citation et n'en est pas une&nbsp;: dans un échange avec une école, c'est le "
           + "genre de flou qu'on évite. Reprenez «&nbsp;que&nbsp;»." },
    ],
    pourquoi: "Un «&nbsp;que&nbsp;» par morceau, et toutes les personnes ramenées dans "
            + "<b>votre</b> bouche. <b>C'est tout le point en une phrase.</b>",
    attente: "Choisissez une réponse pour continuer.",
  },

  // ── 10. La fermeture : le cas de l'écran 1. ──────────────────────────────
  {
    id:   'fermeture',
    type: 'verif',
    eye:  'La dernière',
    menu: 'Pour finir',
    titre: "On revient au voisin de l'escalier.",
    consigne: "Cette fois, il a dit deux choses&nbsp;: «&nbsp;<i>Je passe à cinq heures. "
            + "Laissez-moi la clé chez le concierge.</i>&nbsp;» Vous transmettez les deux.",
    options: [
      { txt: "«&nbsp;Il dit qu'il passe à cinq heures et de laisser la clé chez le "
           + "concierge.&nbsp;»", juste: true },
      { txt: "«&nbsp;Il dit qu'il passe à cinq heures et qu'il laisse la clé chez le "
           + "concierge.&nbsp;»",
        rat_t: "Le premier morceau est juste. Le second a changé de mains.",
        rat: "La seconde phrase du voisin était une <b>consigne</b> adressée à vous&nbsp;: "
           + "c'est vous qui déposez la clé. En la rapportant avec «&nbsp;qu'il&nbsp;», vous "
           + "confiez le geste au voisin — et personne ne descend la clé. Une consigne se "
           + "rapporte avec «&nbsp;<b>de</b>&nbsp;» + le verbe." },
      { txt: "«&nbsp;Il dit&nbsp;: je passe à cinq heures et laissez-moi la clé.&nbsp;»",
        rat_t: "C'est la phrase de l'écran 1, avec une consigne de plus.",
        rat: "Les mots exacts sont là, et c'est justement le problème&nbsp;: le "
           + "«&nbsp;je&nbsp;» s'entend comme le vôtre, et le «&nbsp;moi&nbsp;» aussi. La "
           + "personne à qui vous parlez peut comprendre qu'elle doit <b>vous</b> laisser la "
           + "clé, à vous." },
    ],
    pourquoi: "Vous avez fait les trois choses&nbsp;: poser le «&nbsp;que&nbsp;», ramener les "
            + "personnes dans votre bouche, et reconnaître qu'une consigne se rapporte "
            + "autrement.",
    attente: "Choisissez une réponse pour finir.",
  },

];
