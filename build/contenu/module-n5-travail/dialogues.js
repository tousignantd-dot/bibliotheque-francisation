const DIALOGUES = {

  // ── Je découvre — le bureau de l'accueil, un lundi matin ────────────────
  // Deux voix : DORINE (féminine) et GHISLAIN (masculine), son chef d'équipe.
  // Le vouvoiement est tenu partout dans le module : ils travaillent ensemble
  // depuis dix-huit mois, mais l'un dirige et l'autre exécute.
  prep: {
    label: "Dialogue — Ce qui change avec le poste",
    lines: [
      ["GHISLAIN","Bonjour Dorine. Assoyez-vous, c'est votre bureau maintenant."],
      ["DORINE","Merci. J'ai un peu peur, je vous le dis franchement."],
      ["GHISLAIN","Peur de quoi ? Vous connaissez la coopérative mieux que moi."],
      ["DORINE","Je connais les logements, les horaires, les gens. Je ne connais pas le bureau."],
      ["GHISLAIN","C'est vrai que ça change. Avant, on vous disait quoi faire le matin. Maintenant, c'est écrit."],
      ["DORINE","Écrit où ?"],
      ["GHISLAIN","Partout. Vos tâches sont dans un tableau. Les directives des appareils sont sur le mur. Vos heures sont au registre. Et les demandes passent par des formulaires."],
      ["DORINE","Et le téléphone ?"],
      ["GHISLAIN","Le téléphone est à vous. Poste vingt-deux. Quand vous n'êtes pas là, c'est votre boîte vocale qui répond, avec votre voix."],
      ["DORINE","Il faut que j'enregistre quelque chose, alors."],
      ["GHISLAIN","Un message d'accueil, oui. Trente secondes, pas plus. On le refera ensemble cette semaine."],
      ["DORINE","Et les messages que les gens laissent ?"],
      ["GHISLAIN","Vous les écoutez, et vous en faites une note. Une vraie note, que quelqu'un d'autre peut lire sans vous appeler pour comprendre."],
      ["DORINE","Je peux écrire en abrégé ?"],
      ["GHISLAIN","Pour vous, oui. Pour les autres, non. Une note qui ne se comprend que par celle qui l'a écrite ne sert à rien."],
      ["DORINE","D'accord. Autre chose ?"],
      ["GHISLAIN","Une dernière. Au téléphone et par écrit, vous vouvoyez tout le monde, même les gens que vous connaissez. Ici, on se tutoie ; là, non."],
      ["DORINE","Même madame Thériault ? Je lui parle depuis un an."],
      ["GHISLAIN","Même madame Thériault. Ce n'est pas Dorine qui répond au poste vingt-deux : c'est la coopérative."],
    ]
  },

  // ── Défi 1 — la boîte vocale, mardi matin ───────────────────────────────
  // GHISLAIN écoute avec Dorine ; THERIAULT est la voix enregistrée dans la
  // boîte vocale. Les deux ne se répondent jamais : elles peuvent partager
  // une voix du générateur si nécessaire.
  t1: {
    label: "Dialogue — Quatre messages et une note",
    lines: [
      ["DORINE","J'ai enregistré mon message hier soir. Vous voulez l'entendre ?"],
      ["GHISLAIN","Allez-y."],
      ["DORINE","« Bonjour, vous êtes bien à la Coopérative d'aide à domicile de Rosemont. Ici Dorine Kabeya, à l'accueil. Je ne suis pas disponible en ce moment. Laissez-moi votre nom, votre numéro de téléphone et la raison de votre appel : je vous rappellerai dans la journée. Pour une urgence, faites le poste onze. Merci et bonne journée. »"],
      ["GHISLAIN","C'est bon. Vous vous nommez, vous nommez la coopérative, vous demandez les trois choses, vous dites quand vous rappelez, et vous donnez une porte de sortie. Une seule remarque."],
      ["DORINE","Laquelle ?"],
      ["GHISLAIN","« Dans la journée. » Si vous êtes en congé jeudi, ce n'est plus vrai, et le message continue de le dire. Mettez « dans les meilleurs délais » et changez le message quand vous partez plus d'une journée."],
      ["DORINE","Je note. Maintenant, j'ai quatre messages dans la boîte."],
      ["GHISLAIN","Écoutons le premier ensemble. Vous écrivez, je me tais."],
      ["THERIAULT","Oui bonjour, c'est madame Thériault, du 5680 rue Beaubien, appartement 3. Je vous appelle parce que la dame qui vient le mercredi matin, Nadège je pense, m'a dit qu'elle ne pourrait pas venir cette semaine. Alors moi je voulais savoir si quelqu'un d'autre peut passer, parce que j'ai mon rendez-vous à la clinique jeudi et il faut que quelqu'un m'aide avant. Mon numéro c'est le cinq un quatre, deux deux cinq, quatorze quarante. Rappelez-moi avant midi si possible, après je ne réponds pas. Merci beaucoup."],
      ["DORINE","Elle parle vite."],
      ["GHISLAIN","Elle parle normalement. Vous, vous cherchez les six mêmes choses à chaque fois. Qui appelle, quand, pourquoi, ce qu'elle demande, comment la joindre, et ce qui presse."],
      ["DORINE","Alors : madame Thériault, ce matin, 5680 Beaubien, appartement 3. Elle dit que son aide du mercredi ne viendra pas. Elle demande un remplacement avant son rendez-vous de jeudi."],
      ["GHISLAIN","Continuez."],
      ["DORINE","Numéro : 514 225-1440. Elle demande qu'on la rappelle avant midi ; après, elle ne répond pas."],
      ["GHISLAIN","Voilà une note. Six lignes, et je peux agir sans vous poser une seule question. Ajoutez la date et votre nom en bas."],
      ["DORINE","Pourquoi mon nom ? C'est elle qui a appelé."],
      ["GHISLAIN","Parce que dans trois jours, quelqu'un voudra savoir qui a pris le message. Une note sans nom, c'est une note sans personne derrière."],
    ]
  },

  // ── Défi 2 — le corridor, devant le photocopieur neuf ───────────────────
  t2: {
    label: "Dialogue — L'appareil neuf du corridor",
    lines: [
      ["KEVIN","Tu as vu ? Ils ont changé le photocopieur pendant la fin de semaine."],
      ["DORINE","J'ai vu. Et j'ai vu aussi que personne ne sait s'en servir."],
      ["KEVIN","Il y a le livret, là, sur la tablette."],
      ["DORINE","Quatre-vingts pages. En deux langues. Je cherche seulement à numériser une feuille et à me l'envoyer par courriel."],
      ["KEVIN","Regarde la table des matières. Tu ne lis jamais un mode d'emploi du début à la fin : tu cherches ta page."],
      ["DORINE","« Numérisation vers un courriel », page trente-quatre. Bon. « Placer le document face vers le haut dans le chargeur. »"],
      ["KEVIN","Le chargeur, c'est le bac du dessus. Le bac à papier, lui, c'est le tiroir d'en bas."],
      ["DORINE","« Appuyer sur Numériser. Entrer l'adresse courriel. Confirmer. » C'est tout ?"],
      ["KEVIN","C'est tout. Trois gestes."],
      ["DORINE","Trois gestes et une page trente-quatre. Kevin, tu as combien de temps devant toi ?"],
      ["KEVIN","Dix minutes. Pourquoi ?"],
      ["DORINE","On écrit une demi-page. Les quatre choses que le monde fait ici : copier, numériser, changer le papier, débloquer une feuille coincée. Et on la colle sur le mur."],
      ["KEVIN","Ghislain va aimer ça."],
      ["DORINE","Ghislain va surtout arrêter d'être dérangé quatre fois par jour. Commence : pour faire une copie, on fait quoi d'abord ?"],
      ["KEVIN","D'abord, tu lèves le couvercle et tu poses ta feuille face vers le bas, dans le coin en haut à gauche."],
      ["DORINE","Ensuite ?"],
      ["KEVIN","Ensuite tu choisis le nombre de copies avec le clavier. Puis tu appuies sur le gros bouton vert. Et enfin tu reprends ton original sous le couvercle — c'est ça que tout le monde oublie."],
      ["DORINE","« Reprendre son original » va en gras. Et le bourrage ?"],
      ["KEVIN","Tu ouvres la porte de côté, tu tires la feuille lentement, sans forcer, et tu refermes bien. Si l'écran reste rouge, tu ne recommences pas dix fois : tu appelles le service technique au poste dix-neuf."],
    ]
  },

  // ── Défi 3 — la demande de congé, jeudi après-midi ──────────────────────
  // GHISLAIN d'abord, SYLVIE (la paie) ensuite. Elles ne se répondent pas.
  t3: {
    label: "Dialogue — Six étapes et un formulaire",
    lines: [
      ["DORINE","Ghislain, est-ce que je peux vous parler deux minutes de mes vacances ?"],
      ["GHISLAIN","Entrez. Quelles dates ?"],
      ["DORINE","Du lundi 12 août au vendredi 16 août. Cinq jours. Ma sœur arrive de Kinshasa le 12."],
      ["GHISLAIN","La semaine du 12 est déjà prise par Amel. Celle du 19 est libre."],
      ["DORINE","Alors ce sera du 19 au 23 août. Retour le lundi 26."],
      ["GHISLAIN","Bien. Qui répond au téléphone de l'accueil pendant ce temps-là ?"],
      ["DORINE","J'ai demandé à Kevin. Il est d'accord pour les avant-midis, et Amel prend les après-midis."],
      ["GHISLAIN","Ça, c'est une demande bien préparée. Vous savez comment ça marche ensuite ?"],
      ["DORINE","Pas exactement. Dites-moi les étapes, je les écris."],
      ["GHISLAIN","Six. D'abord vous vérifiez au registre combien de jours il vous reste. Ensuite vous prenez le formulaire au babillard. Puis vous le remplissez : les deux dates, le nom de la personne qui vous remplace. Après, vous me le faites signer. Ensuite vous l'envoyez à Sylvie, à la paie. Et enfin vous attendez sa confirmation par courriel."],
      ["DORINE","Et si je ne reçois rien ?"],
      ["GHISLAIN","Vous relancez. Tant que la confirmation n'est pas écrite, votre congé n'existe pas. Une entente de corridor ne vaut rien au mois d'août."],
      ["DORINE","Combien de temps d'avance ?"],
      ["GHISLAIN","Ici, trois semaines : c'est notre politique. La loi, elle, oblige l'employeur à annoncer les dates de vacances au moins quatre semaines à l'avance. Ce n'est pas la même chose, mais ça va dans le même sens : personne n'aime les surprises."],
      ["SYLVIE","Dorine ? J'ai votre formulaire. Tout est bon, sauf une case."],
      ["DORINE","Laquelle ?"],
      ["SYLVIE","« Personne à joindre en cas d'urgence pendant l'absence. » Vous avez mis votre propre numéro."],
      ["DORINE","C'est bien moi qu'on doit joindre, non ?"],
      ["SYLVIE","Non. Cette case dit qui répond à votre place. Vous serez en congé : ce sera Kevin le matin et Amel l'après-midi. Corrigez, et je vous envoie la confirmation aujourd'hui."],
      ["DORINE","Je corrige tout de suite. Et pour mon courriel ?"],
      ["SYLVIE","Vous réglez votre réponse automatique le vendredi avant de partir, pas le lundi matin de votre départ. La date du retour, un autre nom, un autre numéro. Trois lignes suffisent."],
    ]
  },

};
