const DIALOGUES = {
  // Quatre dialogues, un par section. Au niveau 6, ils font dix-huit à vingt
  // répliques et non dix à seize : la compétence vise « des discours détaillés
  // et structurés », et une conversation de trois répliques n'en est pas un.
  // Le même dossier — celui de Bintou — revient dans les quatre, sous quatre
  // formes différentes : le comptoir, l'entretien à deux, la lecture à deux
  // voix, la rencontre à quatre.
  //
  // Six personnages, quatre timbres. Voir l'en-tête de
  // generer_audio_module_n6_etablissement.py : deux personnages ne partagent
  // une voix que s'ils ne se répondent jamais.

  prep: {
    label: "Dialogue — Au comptoir de l'accueil, un mardi midi",
    lines: [
      ["BINTOU","Bonjour. Je m'excuse, je ne sais pas si c'est ici qu'il faut demander ça."],
      ["RÉAL","Bonjour. Demandez toujours, on verra bien. Vous êtes en francisation ?"],
      ["BINTOU","Oui, au local 214, le soir. Bintou Sangaré. Je finis mon dernier cours en février et je voudrais savoir ce que je fais après."],
      ["RÉAL","Ah. Ça, c'est une belle question, et ce n'est pas à moi qu'il faut la poser."],
      ["BINTOU","Ce n'est pas vous qui vous occupez des inscriptions ?"],
      ["RÉAL","Des inscriptions, oui. Des dossiers, des relevés de notes, des changements d'horaire, des attestations : tout ce qui est papier passe par le comptoir. Mais choisir un programme, c'est autre chose. Ça, c'est l'orientation."],
      ["BINTOU","L'orientation, c'est une personne ?"],
      ["RÉAL","C'est une personne, oui. Pascal Lachapelle, conseiller d'orientation. Il est ici le lundi et le jeudi. Son métier, c'est justement de s'asseoir avec quelqu'un et de regarder avec lui ce qui est possible."],
      ["BINTOU","Et il décide si je peux entrer dans un programme ?"],
      ["RÉAL","Non. Personne ne décide en parlant. Lui, il vous explique, il calcule vos préalables, il vous dit où ça bloque. La décision, elle arrive après, par écrit, du centre de formation professionnelle."],
      ["BINTOU","Par écrit."],
      ["RÉAL","Toujours par écrit. Ici, une chose qui compte finit toujours en papier : un avis, une lettre, une ligne dans votre dossier. Ce qui se dit au comptoir ne compte pas."],
      ["BINTOU","Et mon enseignant, monsieur Béliveau, il sert à quoi là-dedans ?"],
      ["RÉAL","À dire où vous en êtes en français, et ça pèse lourd. Il vous voit trois soirs par semaine ; le conseiller, lui, vous verra une heure. Amenez-le à la rencontre si vous en avez une."],
      ["BINTOU","Il y a une rencontre ?"],
      ["RÉAL","Il y en a une quand le dossier est assez avancé pour ça. Plusieurs personnes autour de la même table, une heure, et on repart avec un plan écrit. Mais commencez par l'orientation, sinon vous arriverez à la rencontre les mains vides."],
      ["BINTOU","D'accord. Qu'est-ce que je dois faire, alors ?"],
      ["RÉAL","Remplissez ceci — demande de rencontre, une page — et rapportez-le-moi. Écrivez en bas ce que vous cherchez : deux lignes suffisent, mais qu'elles soient précises. « Je veux de l'information » ne veut rien dire ; « je veux savoir quels préalables il me manque pour un DEP » veut dire quelque chose."],
      ["BINTOU","Et j'apporte quoi, à la rencontre ?"],
      ["RÉAL","Vos papiers. Tous vos papiers, même ceux que vous croyez inutiles. C'est le conseiller qui trie, pas vous."],
    ]
  },

  t1: {
    label: "Dialogue — Une heure avec le conseiller d'orientation",
    lines: [
      ["PASCAL","Entrez, madame Sangaré. Assoyez-vous. J'ai lu votre demande : vous cherchez à savoir quels préalables il vous manque. C'est déjà plus clair que la moitié de ce que je reçois."],
      ["BINTOU","Merci. Je me demande surtout par où commencer. J'ai travaillé six ans dans une pharmacie à Bamako, et ici je suis commis de soir depuis deux ans."],
      ["PASCAL","Commis dans une pharmacie ?"],
      ["BINTOU","Oui. Je range, je place les commandes, je réponds au téléphone. Ce que je faisais là-bas, je ne le fais plus ici."],
      ["PASCAL","Et vous aimeriez le refaire."],
      ["BINTOU","J'y pense tous les soirs. Mais je ne sais pas quoi faire de mes années là-bas. Personne ne me dit si ça compte ou si ça ne compte pas."],
      ["PASCAL","Alors commençons par là, parce que c'est là que les gens se découragent. Le programme qui mène à ce métier ici, c'est un diplôme d'études professionnelles : assistance technique en pharmacie. Un DEP."],
      ["BINTOU","Et pour y entrer ?"],
      ["PASCAL","Trois chemins. Le premier : un diplôme d'études secondaires, ou son équivalent reconnu. Le deuxième : avoir seize ans au trente septembre et les unités de quatrième secondaire en langue d'enseignement, en langue seconde et en mathématiques. Le troisième, celui qui vous concerne : avoir dix-huit ans et réussir le test de développement général, plus les préalables particuliers du programme."],
      ["BINTOU","Ça fait beaucoup de mots. Le test, il remplace le diplôme ?"],
      ["PASCAL","Non, et c'est la confusion la plus fréquente. Le test de développement général ouvre la porte d'un DEP, rien d'autre. Celui qui donne une équivalence de cinquième secondaire, c'est l'autre : le test d'équivalence de niveau de scolarité, sept épreuves, dont deux en français."],
      ["BINTOU","Et mes six ans de pharmacie, dans tout ça ?"],
      ["PASCAL","Ils ne remplacent aucun préalable. Ils servent ailleurs, et ils servent beaucoup : en stage, en entrevue, et devant un jury de reconnaissance des acquis. Ce n'est pas la même porte, mais ce n'est pas rien."],
      ["BINTOU","J'ai aussi un papier du ministère de l'Immigration. Une évaluation comparative."],
      ["PASCAL","Vous l'avez avec vous ?"],
      ["BINTOU","Oui. On m'a dit que c'était une équivalence."],
      ["PASCAL","On vous l'a mal dit, et ça arrive chaque semaine. Ce document est un avis d'expert : il dit à quel niveau d'ici vos études de là-bas se comparent. Ce n'est pas une équivalence de diplôme, ça ne remplace pas un permis, et ça ne garantit l'admission à aucun programme. Gardez-le : il explique votre parcours. Mais ne bâtissez pas votre année dessus."],
      ["BINTOU","Bon. Alors qu'est-ce que je fais, concrètement ?"],
      ["PASCAL","Trois choses, dans cet ordre. Vous finissez votre francisation en février — le français est le préalable dont dépendent tous les autres. Vous vous inscrivez au test de développement général : la prochaine séance est le vingt-huit novembre, l'inscription se fait au comptoir. Et vous demandez la description officielle du programme au centre de formation professionnelle, celle où les préalables particuliers sont écrits noir sur blanc."],
      ["BINTOU","Et si je rate le test ?"],
      ["PASCAL","Vous le reprenez. Personne ne le réussit deux fois par plaisir, mais personne n'est fermé après un échec non plus. On se revoit en janvier, et cette fois on aura des papiers à regarder au lieu de suppositions."],
    ]
  },

  t2: {
    label: "Dialogue — Deux papiers sur la table de la cafétéria",
    lines: [
      ["ROSA","Tu as reçu quoi, finalement ? Tu avais l'air blanche en sortant du comptoir."],
      ["BINTOU","Deux papiers. La description du programme, quatre pages, et un avis officiel du centre de formation professionnelle. Une page, celui-là. C'est la page qui me fait peur."],
      ["ROSA","Montre. Ah, ça commence par « Avis d'admission conditionnelle ». Conditionnelle, ça veut dire quoi ?"],
      ["BINTOU","Que je suis acceptée, mais pas vraiment."],
      ["ROSA","Non, attends, ce n'est pas ce qui est écrit. Regarde la ligne encadrée : la place est réservée jusqu'au six février, et elle est libérée si la condition n'est pas remplie à cette date."],
      ["BINTOU","Et la condition, c'est le test."],
      ["ROSA","C'est le test. « La candidate fournira la preuve de réussite du test de développement général. » Fournira. Au futur."],
      ["BINTOU","Pourquoi au futur ? Ce n'est pas une prédiction, c'est une obligation."],
      ["ROSA","C'est comme ça qu'ils écrivent. Chez nous aussi, à l'hôpital, tout était au futur. « Le patient se présentera à jeun. » Ça veut dire : présentez-vous à jeun, et ne discutez pas."],
      ["BINTOU","Et cette phrase-là : « Les documents se déposent au secrétariat avant le premier février » ? Qui les dépose ?"],
      ["ROSA","Toi. Ils ne le disent pas, mais c'est toi. Ils écrivent comme si les papiers marchaient tout seuls."],
      ["BINTOU","Ça me mêle. Quand personne n'est nommé, je ne sais jamais qui doit bouger."],
      ["ROSA","C'est le piège de ces textes-là. Prends l'habitude : quand tu lis « se dépose », « se remplit », « s'obtient », demande-toi tout de suite par qui. Neuf fois sur dix, c'est toi."],
      ["BINTOU","Regarde la description du programme, maintenant. La première page ne parle même pas du programme."],
      ["ROSA","Elle raconte l'histoire du centre. « Le centre ouvrit ses portes en mille neuf cent soixante-huit. » Ouvrit."],
      ["BINTOU","Personne ne parle comme ça."],
      ["ROSA","Personne ne le parle, mais tout le monde l'écrit. Dans ma classe du soir, mon enseignant appelle ça le temps des livres. Tu n'as pas à l'écrire : tu as juste à comprendre que « ouvrit », c'est « a ouvert »."],
      ["BINTOU","Et les préalables particuliers, ils sont où ?"],
      ["ROSA","Page trois, dans l'encadré gris, sous le titre en gras. C'est toujours dans l'encadré, ce qui compte. Le reste, c'est de la présentation."],
    ]
  },

  t3: {
    label: "Dialogue — La rencontre du 14 novembre, local 118",
    lines: [
      ["PASCAL","Merci d'être là. On a une heure. Madame Sangaré, je résume pour tout le monde en trois phrases, puis vous corrigerez si je me trompe."],
      ["BINTOU","D'accord."],
      ["PASCAL","Bintou Sangaré termine sa francisation en février. Elle vise le DEP en assistance technique en pharmacie. Elle a un avis d'admission conditionnelle, et la condition est la réussite du test de développement général."],
      ["BINTOU","C'est exact. J'ajoute une chose : le test est le vingt-huit novembre, et je suis inscrite."],
      ["AMÉLIE","C'est noté. De mon côté, je veux qu'une chose soit claire dès maintenant : le centre de formation professionnelle n'accorde aucun délai après le six février. Ce n'est pas de la sévérité, c'est le calendrier des groupes."],
      ["MARC-OLIVIER","Si je peux me permettre — sur le français, je n'ai aucune inquiétude. Bintou lit des textes officiels depuis septembre et elle les lit mieux que la moitié du groupe. Ce qui l'arrête, ce n'est pas la langue, c'est le vocabulaire administratif."],
      ["AMÉLIE","Ce n'est pas rien non plus. Nos consignes de laboratoire sont écrites comme cet avis-là."],
      ["MARC-OLIVIER","Justement. On travaille ça en classe depuis un mois."],
      ["BINTOU","Est-ce que je peux poser une question ?"],
      ["PASCAL","Allez-y."],
      ["BINTOU","Si je réussis le test le vingt-huit et que la preuve arrive en janvier, est-ce que ça suffit ?"],
      ["AMÉLIE","Si la preuve est au dossier avant le six février, oui, ça suffit. Ce que je demande, c'est que vous ne l'apportiez pas le cinq au soir."],
      ["BINTOU","Je le déposerai la semaine où je le reçois."],
      ["PASCAL","Écrivons-le. Amélie, il faudrait que le plan de formation mentionne cette date, sinon on la retrouvera nulle part en janvier."],
      ["AMÉLIE","Je l'écris. Autre chose : j'aimerais que madame Sangaré vienne visiter le laboratoire avant de décider. Beaucoup de gens s'inscrivent sans avoir vu la place où ils passeront neuf mois."],
      ["BINTOU","Pour ma part, je préférerais y aller après le test. Si j'y vais avant, je vais penser à ça pendant l'épreuve."],
      ["AMÉLIE","C'est raisonnable. Le trois décembre, alors."],
      ["MARC-OLIVIER","Une dernière chose, et j'y tiens : que quelqu'un lui envoie le compte rendu de cette rencontre par écrit. On a dit quatre dates en une heure."],
      ["PASCAL","Ça part demain. Madame Sangaré, à mon avis, votre dossier est en bien meilleur état que vous ne le croyez : ce qui vous manque, c'est un papier, et il a une date."],
      ["BINTOU","Merci. C'est la première fois que je sors d'ici avec quelque chose d'écrit."],
    ]
  },
};
