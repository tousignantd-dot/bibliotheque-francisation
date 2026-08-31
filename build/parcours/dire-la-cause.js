// ═══════════════════════════════════════════════════════════════════════════
// Point express — Cinq façons de dire pourquoi, et celle qui accuse
//
// Savoir n6-s02 (Connecteurs et relations logiques). Une ORDONNANCE :
// l'enseignant l'envoie à un élève qui écrit « à cause de » partout, ou qui
// colle une phrase entière derrière « à cause de ». Dix minutes, dix écrans.
//
// ── Ce qui le sépare des mini-leçons existantes ────────────────────────────
// Cinq mini-leçons du dépôt traitent la cause, et toutes procèdent en listant :
//   · `module-n5-saisons` — « Dire pourquoi : six connecteurs de cause ».
//   · `module-n5-voisinage` — « Dire pourquoi : parce que, comme, puisque, donc ».
//   · `module-n4-etablissement` — « Parce que, à cause de, grâce à ».
//   · `module-relations` — « grâce à ou à cause de ».
//   · `module-n5-degat` — « Cause et conséquence : les mots qui font tenir une
//     demande », qui les aborde par la lettre de réclamation.
// Un élève qui les a lues connaît les mots et continue d'écrire « à cause de
// que le bureau était fermé » — parce qu'aucune ne sépare ce qui suit un NOM de
// ce qui suit une PHRASE, et parce qu'aucune ne dit que « à cause de » blâme.
// Les cinq écarts tenus :
//
//   1. INDUCTIF. L'élève trie six phrases selon le sentiment qu'elles laissent
//      AVANT qu'on lui ait dit qu'un des mots reproche. La règle de l'écran 3
//      est écrite comme un constat de ce qu'il vient de faire.
//   2. PARTIEL, JAMAIS LA LISTE. Pas de tableau des six connecteurs. DEUX
//      questions réutilisables — « ce qui suit est-il un nom ou une phrase ? »
//      et « est-ce que je veux juger ? » — qui suffisent à choisir devant un
//      connecteur jamais vu.
//   3. LE NEUTRE EST DIT EN DERNIER (écran 8), alors que « en raison de » est
//      la forme des avis officiels. Le nommer d'entrée ferait un troisième
//      mot à retenir avant d'avoir compris pourquoi les deux premiers gênent.
//   4. LE MÉTALANGAGE ARRIVE APRÈS. « Connecteur », « groupe du nom » et
//      « subordonnée » ne sont écrits qu'à l'écran 5, la chose manipulée.
//   5. EXEMPLES VARIÉS, JAMAIS CEUX D'UN MODULE. Un texto, un avis d'immeuble,
//      un courriel à un employeur, une demande à un bureau, un message à une
//      enseignante. L'élève doit reconnaître la faute partout.
//
// Aucun média : la faute est un choix de mot et une construction, toutes deux
// visibles à l'écrit seulement. Rien à écouter.
// ═══════════════════════════════════════════════════════════════════════════

const PARCOURS = {
  slug:     'dire-la-cause',
  titre:    "Cinq façons de dire pourquoi, et celle qui accuse",
  surtitre: "Point express · 10 minutes",
  niveau:   6,
  savoir:   'n6-s02',
};

const ECRANS = [

  // ── 1. Une décision, sans aucune règle donnée. ───────────────────────────
  {
    id:   'depart',
    type: 'verif',
    eye:  'Une question, pour commencer',
    menu: 'Un retard',
    titre: "« Je suis arrivée en retard ___ l'autobus. » Que met-on dans le trou ?",
    consigne: "Répondez avec ce que vous savez déjà — ou au feeling. On expliquera après&nbsp;: "
            + "c'est fait exprès.",
    options: [
      { txt: "à cause de", juste: true },
      { txt: "parce que",
        rat_t: "Le sens est bon&nbsp;; c'est la suite qui ne peut pas venir.",
        rat: "«&nbsp;Parce que&nbsp;» réclame une <b>phrase</b> derrière lui&nbsp;: quelqu'un qui "
           + "fait quelque chose. «&nbsp;<i>Parce que l'autobus était en retard</i>&nbsp;» serait "
           + "juste. Tout seul, «&nbsp;l'autobus&nbsp;» n'est pas une phrase — il manque le verbe." },
      { txt: "grâce à",
        rat_t: "La construction est bonne, le sentiment est à l'envers.",
        rat: "«&nbsp;Grâce à&nbsp;» se met bien devant un nom, vous avez raison là-dessus. Mais "
           + "il annonce toujours quelque chose d'heureux&nbsp;: on ne remercie pas l'autobus de "
           + "nous avoir mis en retard. Le mot lui-même porte un jugement, et c'est le sujet des "
           + "deux prochains écrans." },
    ],
    pourquoi: "«&nbsp;À cause de&nbsp;» — un nom derrière, et un ennui devant. Gardez la phrase "
            + "en tête&nbsp;: on y revient au dernier écran, dans un courriel où elle ne s'écrira "
            + "plus tout à fait pareil.",
    attente: "Choisissez une réponse pour continuer.",
  },

  // ── 2. On trie AVANT de savoir. C'est ici que le point se sépare. ────────
  {
    id:   'tri-jugement',
    type: 'tri',
    eye:  'À vous de trancher',
    menu: 'Six phrases',
    titre: "Six phrases lues cette semaine. Celui qui écrit remercie-t-il, ou reproche-t-il ?",
    consigne: "Aucune règle ne vous a été donnée — normal. Ne regardez pas la grammaire&nbsp;: "
            + "demandez-vous ce que la personne <b>ressent</b> en écrivant sa phrase.",
    colonnes: [
      { id: 'merci',    t: "Elle remercie",  b: "Elle remercie" },
      { id: 'reproche', t: "Elle reproche",  b: "Elle reproche" },
    ],
    items: [
      { txt: "J'ai eu la place grâce à votre lettre de recommandation.",
        sous: "un courriel à une ancienne patronne", ok: 'merci',
        rat: "La lettre a servi, et celui qui écrit le dit exprès. C'est le mot qu'on emploie "
           + "quand on veut que le lecteur se sente utile.",
        pourquoi: "La lettre a servi, et il le lui dit." },
      { txt: "La réunion a été reportée à cause de votre absence.",
        sous: "un message à un collègue", ok: 'reproche',
        rat: "Rien n'est insultant dans la phrase, et pourtant le collègue la recevra mal&nbsp;: "
           + "le mot désigne un responsable. C'est exactement la nuance que les dictionnaires "
           + "bilingues n'affichent pas.",
        pourquoi: "Le collègue est désigné comme responsable." },
      { txt: "J'ai pu payer mon loyer grâce à ce dépannage.",
        sous: "un message à un organisme", ok: 'merci',
        rat: "Le résultat est heureux et l'aide est nommée. C'est la formule des lettres de "
           + "remerciement, et elle est ici parfaitement à sa place.",
        pourquoi: "Le résultat est heureux : on remercie." },
      { txt: "Mon dossier a pris six mois à cause d'un papier manquant.",
        sous: "une plainte à un bureau", ok: 'reproche',
        rat: "Le papier ne se vexera pas, mais le lecteur comprend qu'on lui reproche de ne pas "
           + "l'avoir réclamé plus tôt. Le mot cherche un fautif, même quand le fautif est une "
           + "chose.",
        pourquoi: "Un fautif est désigné : le papier manquant." },
      { txt: "J'ai trouvé l'adresse grâce à la carte que vous m'aviez envoyée.",
        sous: "un texto", ok: 'merci',
        rat: "Même mécanique que la lettre de recommandation&nbsp;: une aide, un bon résultat, et "
           + "celui qui écrit choisit de le souligner.",
        pourquoi: "L'aide a marché, et il le dit." },
      { txt: "Le cours a été annulé à cause de la tempête.",
        sous: "un avis affiché au centre", ok: 'reproche',
        rat: "Celui-là trompe souvent&nbsp;: personne n'en veut à la météo. Mais le mot reste "
           + "celui de l'ennui — il annonce un désagrément, et c'est pour cette raison qu'un avis "
           + "officiel lui préférera un troisième mot, qu'on verra à la fin.",
        pourquoi: "L'ennui est annoncé : le mot du désagrément." },
    ],
    attente: "Tranchez les six phrases pour continuer.",
  },

  // ── 3. La règle, écrite comme un constat de ce qu'il vient de faire. ─────
  {
    id:   'deux-questions',
    type: 'notion',
    eye:  'Ce que vous venez de faire',
    menu: 'Le tri',
    titre: "Vous n'avez pas hésité une seule fois. Le mot faisait le travail à votre place.",
    paras: [
      "Vous n'avez jamais eu à lire la fin de la phrase pour savoir si on remerciait ou si on "
      + "reprochait&nbsp;: le mot le disait dès son apparition. C'est ce que la plupart des "
      + "listes ne disent pas — <b>ces deux-là ne sont pas interchangeables</b>, même quand la "
      + "cause est la même.",

      "<b>Grâce à</b> annonce que la suite est heureuse, et il désigne quelqu'un ou quelque chose "
      + "à qui l'on doit ce bonheur. <b>À cause de</b> annonce que la suite est fâcheuse, et il "
      + "désigne un responsable. Devant votre lecteur, ce n'est pas une nuance de style&nbsp;: "
      + "c'est la différence entre le remercier et lui envoyer la facture.",

      "Et ils partagent une contrainte&nbsp;: tous deux se mettent devant un <b>nom</b> — la "
      + "tempête, votre lettre, un papier manquant. Jamais devant une phrase. C'est l'écran "
      + "suivant.",
    ],
    retenir: "<b>Grâce à</b>&nbsp;: heureux, et je remercie. <b>À cause de</b>&nbsp;: fâcheux, et "
           + "je désigne un responsable. Le mot juge avant que la phrase soit finie.",
    attente: "Lisez, puis continuez.",
  },

  // ── 4. Le piège de construction. ─────────────────────────────────────────
  {
    id:   'nom-ou-phrase',
    type: 'verif',
    eye:  'Le piège de la suite',
    menu: 'Nom ou phrase',
    titre: "Wei écrit au bureau du programme. Quelle phrase envoie-t-il ?",
    consigne: "Il veut expliquer que son dossier n'a pas avancé, et la raison est que le bureau "
            + "était fermé.",
    options: [
      { txt: "Mon dossier n'a pas avancé parce que le bureau était fermé.", juste: true },
      { txt: "Mon dossier n'a pas avancé à cause que le bureau était fermé.",
        rat_t: "On l'entend tous les jours, et il ne s'écrit pas.",
        rat: "«&nbsp;À cause que&nbsp;» circule beaucoup à l'oral, ici comme ailleurs. Mais "
           + "«&nbsp;à cause de&nbsp;» est fait pour un <b>nom</b>&nbsp;; dès qu'une phrase "
           + "complète suit — un sujet, un verbe — il faut «&nbsp;parce que&nbsp;». Écrire "
           + "«&nbsp;à cause que&nbsp;» dans un courriel officiel est la faute qu'on remarque." },
      { txt: "Mon dossier n'a pas avancé à cause de le bureau était fermé.",
        rat_t: "Vous avez senti qu'il manquait quelque chose — c'est juste.",
        rat: "La phrase mélange les deux constructions&nbsp;: «&nbsp;à cause de&nbsp;» attend le "
           + "nom seul («&nbsp;<i>à cause de la fermeture</i>&nbsp;»), et «&nbsp;le bureau était "
           + "fermé&nbsp;» est déjà une phrase entière, qui réclame «&nbsp;parce que&nbsp;». Il "
           + "faut choisir l'une ou l'autre, jamais coudre les deux." },
    ],
    pourquoi: "Deux constructions&nbsp;: «&nbsp;<b>à cause de la fermeture</b>&nbsp;» ou "
            + "«&nbsp;<b>parce que le bureau était fermé</b>&nbsp;». Le sens est le même, la "
            + "suite ne l'est pas.",
    attente: "Choisissez une réponse pour continuer.",
  },

  // ── 5. Les trois qui prennent une phrase, et où ils se posent. ───────────
  {
    id:   'les-trois-phrases',
    type: 'notion',
    eye:  'La deuxième moitié',
    menu: 'Les trois autres',
    titre: "Trois mots prennent une phrase entière. Ils ne se posent pas au même endroit.",
    paras: [
      "<b>Parce que</b> répond à la question «&nbsp;pourquoi&nbsp;?&nbsp;» et apporte une "
      + "information que le lecteur n'a pas. C'est le seul des trois qui peut être la réponse à "
      + "lui tout seul&nbsp;: «&nbsp;— Pourquoi&nbsp;? — Parce que la clinique ferme à "
      + "midi.&nbsp;»",

      "<b>Puisque</b> s'appuie sur une raison que <b>les deux connaissent déjà</b>. "
      + "«&nbsp;<i>Puisque vous partez à trois heures, je vous laisse les clés maintenant.</i>&nbsp;» "
      + "Il ne renseigne pas, il rappelle — et il se place le plus souvent en tête de phrase.",

      "<b>Car</b> ne commence jamais une phrase&nbsp;: il vient toujours après une virgule, au "
      + "milieu, et il appartient à l'écrit soigné. «&nbsp;<i>Nous fermerons plus tôt, car "
      + "l'inventaire est prévu ce soir.</i>&nbsp;» À l'oral, personne ne le dit&nbsp;; dans un "
      + "avis, il fait très bien.",

      "En vocabulaire de grammaire&nbsp;: ces trois-là ouvrent une <b>subordonnée</b> — une phrase "
      + "dans la phrase, avec son sujet et son verbe. «&nbsp;Grâce à&nbsp;» et «&nbsp;à cause "
      + "de&nbsp;» ouvrent un <b>groupe du nom</b>. Votre enseignant emploiera ces mots&nbsp;; le "
      + "test, lui, tient sans eux.",
    ],
    retenir: "Une phrase derrière&nbsp;: <b>parce que</b> (j'informe), <b>puisque</b> (on le sait "
           + "déjà), <b>car</b> (à l'écrit, jamais en tête). Un nom derrière&nbsp;: grâce à, à "
           + "cause de.",
    attente: "Lisez, puis continuez.",
  },

  // ── 6. Trier des phrases écrites. ────────────────────────────────────────
  {
    id:   'tri-ecrites',
    type: 'tri',
    eye:  'À vous de trancher',
    menu: 'Six phrases',
    titre: "Six phrases écrites. Lesquelles tiennent ?",
    consigne: "Deux choses à vérifier, dans cet ordre&nbsp;: ce qui suit le mot est-il un nom ou "
            + "une phrase&nbsp;? Et le jugement est-il celui que la personne veut porter&nbsp;?",
    colonnes: [
      { id: 'ok',   t: 'Correct',   b: 'Correct' },
      { id: 'faux', t: 'Une faute', b: 'Une faute' },
    ],
    items: [
      { txt: "J'ai réussi mon examen à cause de vos explications.", ok: 'faux',
        rat: "La construction est bonne — un nom suit. Mais le résultat est heureux et la "
           + "personne veut remercier&nbsp;: «&nbsp;<b>grâce à</b> vos explications&nbsp;». Écrite "
           + "ainsi, la phrase se lit comme un reproche adressé à quelqu'un qui a aidé.",
        pourquoi: "Le résultat est heureux : « grâce à vos explications »." },
      { txt: "Le rendez-vous est annulé, car la neige bloque la route.", ok: 'ok',
        rat: "Une phrase entière suit, et «&nbsp;car&nbsp;» est bien au milieu, après la virgule. "
           + "C'est le ton d'un avis, et il est juste.",
        pourquoi: "Une phrase suit, et « car » est au milieu. Juste." },
      { txt: "Puisque vous connaissez déjà l'immeuble, je ne vous refais pas la visite.",
        ok: 'ok',
        rat: "La raison est connue des deux — c'est exactement l'emploi de "
           + "«&nbsp;puisque&nbsp;», et il est bien placé en tête de phrase.",
        pourquoi: "La raison est déjà connue des deux. Juste." },
      { txt: "Je n'ai pas pu venir à cause que ma fille était malade.", ok: 'faux',
        rat: "Une phrase entière suit («&nbsp;ma fille était malade&nbsp;»), donc il faut "
           + "«&nbsp;<b>parce que</b>&nbsp;». La version au nom existe aussi&nbsp;: «&nbsp;à cause "
           + "de la maladie de ma fille&nbsp;». Les deux se disent, «&nbsp;à cause que&nbsp;» ne "
           + "s'écrit pas.",
        pourquoi: "Une phrase suit : « parce que ma fille était malade »." },
      { txt: "Car je n'avais plus de billets, j'ai pris un taxi.", ok: 'faux',
        rat: "Le mot est bon, la place ne l'est pas&nbsp;: «&nbsp;car&nbsp;» ne commence jamais "
           + "une phrase. Deux corrections possibles — «&nbsp;<i>J'ai pris un taxi, car je "
           + "n'avais plus de billets</i>&nbsp;» ou «&nbsp;<i>Comme je n'avais plus de "
           + "billets…</i>&nbsp;».",
        pourquoi: "« Car » ne se met jamais en tête de phrase." },
      { txt: "Grâce à un voisin, j'ai retrouvé mon trousseau de clés.", ok: 'ok',
        rat: "Un nom suit, le résultat est heureux, et le voisin est nommé comme celui à qui on "
           + "le doit. Les deux vérifications passent.",
        pourquoi: "Un nom suit, le résultat est heureux. Juste." },
    ],
    attente: "Tranchez les six phrases pour continuer.",
  },

  // ── 7. Ce qu'on écrit, et à qui. ─────────────────────────────────────────
  {
    id:   'ce-quon-ecrit',
    type: 'verif',
    eye:  'Vérification',
    menu: "À l'écrit",
    titre: "Vous écrivez à votre employeur pour expliquer une livraison en retard.",
    consigne: "Le retard vient d'une erreur du fournisseur. Vous voulez que ce soit clair, sans "
            + "faire un procès à personne dans un courriel qui sera relu.",
    options: [
      { txt: "«&nbsp;La livraison a été retardée en raison d'une erreur de commande.&nbsp;»",
        juste: true },
      { txt: "«&nbsp;La livraison a été retardée à cause du fournisseur.&nbsp;»",
        rat_t: "Rien de faux, et c'est justement le problème.",
        rat: "La construction est correcte et le sens aussi. Mais vous venez de nommer un "
           + "responsable par écrit, dans un message qui peut être transféré. «&nbsp;À cause "
           + "de&nbsp;» pointe quelqu'un&nbsp;; quand ce n'est pas votre intention, il existe une "
           + "forme qui n'accuse pas — c'est celle de la bonne réponse, et l'écran suivant y "
           + "revient." },
      { txt: "«&nbsp;La livraison a été retardée grâce à une erreur de commande.&nbsp;»",
        rat_t: "Le mot neutralise, mais dans le mauvais sens.",
        rat: "Vous avez bien senti qu'il fallait retirer le reproche. Seulement "
           + "«&nbsp;grâce à&nbsp;» ne neutralise pas&nbsp;: il remercie. La phrase se lit comme "
           + "de l'ironie, ce qui est pire qu'un reproche franc dans un courriel de travail." },
    ],
    pourquoi: "<b>«&nbsp;En raison de&nbsp;» ne juge ni dans un sens ni dans l'autre.</b> C'est la "
            + "forme des avis, des lettres officielles et des messages qu'on préfère ne pas voir "
            + "transférés.",
    attente: "Choisissez une réponse pour continuer.",
  },

  // ── 8. Le neutre, dit en dernier : c'est le plus utile à l'écrit. ────────
  {
    id:   'le-neutre-en-dernier',
    type: 'notion',
    eye:  'Ce qui reste',
    menu: 'Le mot neutre',
    titre: "Le cinquième mot ne juge rien, et c'est celui qu'on lit partout.",
    paras: [
      "On l'a gardé pour la fin exprès&nbsp;: tant qu'on n'a pas senti que les deux autres "
      + "jugent, il n'a l'air d'être qu'un synonyme compliqué. <b>En raison de</b> se met devant "
      + "un nom, comme «&nbsp;grâce à&nbsp;» et «&nbsp;à cause de&nbsp;», et il n'annonce ni bonne "
      + "ni mauvaise nouvelle&nbsp;: «&nbsp;<i>Fermeture en raison des travaux</i>&nbsp;», "
      + "«&nbsp;<i>En raison de la demande, les délais sont de six semaines</i>&nbsp;».",

      "Regardez les avis autour de vous — arrêt d'autobus, guichet, porte de clinique&nbsp;: "
      + "c'est presque toujours celui-là. Une organisation évite de reprocher quoi que ce soit à "
      + "sa clientèle, et évite aussi de se faire remercier.",

      "Autrement dit, vous n'avez <b>qu'une seule question</b> à vous poser au moment d'écrire "
      + "la cause&nbsp;: est-ce que je veux juger&nbsp;? Si oui, choisissez le sens du jugement. "
      + "Si non, il y a un mot pour ça, et il n'est pas plus difficile que les autres.",
    ],
    retenir: "Trois mots devant un nom&nbsp;: <b>grâce à</b> (je remercie), <b>à cause de</b> (je "
           + "reproche), <b>en raison de</b> (je ne juge pas).",
    attente: "Lisez, puis continuez.",
  },

  // ── 9. Écrire, pas reconnaître. ──────────────────────────────────────────
  {
    id:   'a-vous-decrire',
    type: 'verif',
    eye:  'Vérification',
    menu: 'Votre message',
    titre: "Un message à votre enseignante. Quelle version tient d'un bout à l'autre ?",
    consigne: "Amal a manqué le cours de mardi&nbsp;: sa fille était malade. Elle a pu reprendre "
            + "les exercices avec l'aide d'une camarade. Trois versions du même message&nbsp;: "
            + "une seule est correcte partout.",
    options: [
      { txt: "Je n'étais pas là mardi parce que ma fille était malade, mais j'ai pu reprendre les "
           + "exercices grâce à Sofia.",
        juste: true },
      { txt: "Je n'étais pas là mardi à cause que ma fille était malade, mais j'ai pu reprendre "
           + "les exercices grâce à Sofia.",
        rat_t: "La fin est parfaite. C'est le début qui ne s'écrit pas.",
        rat: "«&nbsp;Grâce à Sofia&nbsp;» est exactement juste&nbsp;: un nom, un résultat heureux, "
           + "une personne remerciée. Mais «&nbsp;ma fille était malade&nbsp;» est une phrase "
           + "entière, et une phrase entière veut «&nbsp;parce que&nbsp;»." },
      { txt: "Je n'étais pas là mardi parce que ma fille était malade, mais j'ai pu reprendre les "
           + "exercices à cause de Sofia.",
        rat_t: "Le début est réglé. C'est la fin qui accuse quelqu'un qui a rendu service.",
        rat: "Vous avez le plus technique&nbsp;: la phrase entière derrière "
           + "«&nbsp;parce que&nbsp;». Reste le sentiment&nbsp;: Sofia a aidé, et le message la "
           + "désigne comme la responsable d'un ennui. C'est le genre de phrase qui refroidit une "
           + "camarade sans qu'on comprenne pourquoi." },
    ],
    pourquoi: "Une phrase entière derrière «&nbsp;parce que&nbsp;», un nom derrière "
            + "«&nbsp;grâce à&nbsp;», et le jugement du bon côté. <b>C'est tout le point en un "
            + "message.</b>",
    attente: "Choisissez une réponse pour continuer.",
  },

  // ── 10. La fermeture : le même cas qu'à l'écran 1. ───────────────────────
  {
    id:   'fermeture',
    type: 'verif',
    eye:  'La dernière',
    menu: 'Pour finir',
    titre: "On revient au début : le retard, et l'autobus.",
    consigne: "Cette fois, ce n'est plus un texto à une amie&nbsp;: vous écrivez à la personne "
            + "qui vous accueille en stage, le matin même. Que choisissez-vous&nbsp;?",
    options: [
      { txt: "«&nbsp;J'aurai quinze minutes de retard en raison d'une interruption de "
           + "service.&nbsp;»",
        juste: true },
      { txt: "«&nbsp;J'aurai quinze minutes de retard à cause de l'autobus.&nbsp;»",
        rat_t: "C'est la phrase de l'écran 1 — et elle était juste là-bas.",
        rat: "Rien n'est faux dedans, et à une amie elle passerait très bien. Mais elle a changé "
           + "de destinataire&nbsp;: dans un message professionnel, le mot qui désigne un "
           + "responsable donne l'impression qu'on se défend d'avance. La forme neutre dit la "
           + "même chose sans se justifier." },
      { txt: "«&nbsp;J'aurai quinze minutes de retard parce que l'autobus.&nbsp;»",
        rat_t: "Le ton est meilleur, la phrase est coupée en deux.",
        rat: "«&nbsp;Parce que&nbsp;» attend un sujet et un verbe&nbsp;: «&nbsp;<i>parce que "
           + "l'autobus ne passait pas</i>&nbsp;». Écrite ainsi, la phrase s'arrête au milieu — "
           + "et c'est la faute qu'on remarque le plus dans un message écrit vite, le matin, sur "
           + "un téléphone." },
    ],
    pourquoi: "Vous avez fait les trois choses&nbsp;: regarder ce qui suit le mot, choisir si "
            + "vous vouliez juger, et adapter le mot à la personne qui va lire.",
    attente: "Choisissez une réponse pour finir.",
  },

];
