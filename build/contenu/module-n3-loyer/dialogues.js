const DIALOGUES = {
  prep: {
    label: "Dialogue — Il nous faut une chambre de plus",
    lines: [
      ["DILNOZA","Rachid, tu as déjà déménagé au Québec, toi ?"],
      ["RACHID","Deux fois. Pourquoi ? Tu cherches un logement ?"],
      ["DILNOZA","Oui. Nous sommes trois dans un deux et demie. C'est trop petit."],
      ["RACHID","Trois personnes dans un deux et demie ? Il te faut un quatre et demie."],
      ["DILNOZA","Un quatre et demie, c'est combien de pièces ?"],
      ["RACHID","Deux chambres fermées, un salon, une cuisine et une salle de bain."],
      ["DILNOZA","Et le demi, c'est quelle pièce ?"],
      ["RACHID","C'est la salle de bain. On l'appelle le demi. C'est comme ça ici."],
      ["DILNOZA","Alors mon deux et demie, c'est une seule chambre ?"],
      ["RACHID","Une seule pièce, oui, avec un coin cuisine. Ton garçon dort dans le salon."],
      ["DILNOZA","Il a six ans. Il veut sa chambre à lui."],
      ["RACHID","Regarde les petites annonces. Il y en a sur le babillard, en bas."],
      ["DILNOZA","Je les ai regardées. Je ne comprends pas la moitié des mots."],
      ["RACHID","C'est normal. Elles sont écrites en abrégé. Viens, on va en lire une ensemble."],
    ]
  },

  t1: {
    label: "Dialogue — Chauffé, éclairé, non meublé",
    lines: [
      ["RACHID","Voilà. « Quatre et demie à louer, rue Chabot, Villeray. »"],
      ["DILNOZA","Villeray, c'est loin d'ici ?"],
      ["RACHID","Vingt minutes en autobus. Continue : « deuxième étage, deux chambres fermées »."],
      ["DILNOZA","Deux chambres. C'est ce que je cherche. Et après ?"],
      ["RACHID","« Cuisine avec balcon arrière. Chauffé, éclairé. Non meublé. »"],
      ["DILNOZA","Chauffé, ça veut dire quoi ?"],
      ["RACHID","Que le chauffage est payé par la propriétaire. Tu ne paies pas l'hiver."],
      ["DILNOZA","Et éclairé ?"],
      ["RACHID","L'électricité est comprise aussi. C'est rare. C'est une bonne annonce."],
      ["DILNOZA","Non meublé, ça, je comprends : il n'y a pas de meubles."],
      ["RACHID","Exact. Tu apportes tout : le lit, la table, le réfrigérateur."],
      ["DILNOZA","Et ici, en bas ? « Libre le 1er juillet. Onze cent cinquante dollars. »"],
      ["RACHID","Le loyer, c'est mille cent cinquante dollars par mois. Chauffage compris."],
      ["DILNOZA","Le premier juillet… C'est dans deux mois."],
      ["RACHID","C'est la date de déménagement au Québec. Presque tout le monde bouge ce jour-là."],
      ["DILNOZA","Il y a un numéro de téléphone. Je devrais appeler ?"],
      ["RACHID","Appelle aujourd'hui. Une bonne annonce part vite."],
    ]
  },

  t2: {
    label: "Dialogue — Bonjour, je vous appelle pour l'annonce",
    lines: [
      ["CLAUDINE","Oui, allô ?"],
      ["DILNOZA","Bonjour, madame. Je vous appelle pour l'annonce du quatre et demie."],
      ["CLAUDINE","Bonjour. Oui, il est encore libre. Vous êtes combien de personnes ?"],
      ["DILNOZA","Nous sommes trois : mon mari, mon garçon de six ans et moi."],
      ["CLAUDINE","Très bien. Il y a deux chambres fermées, alors ça va."],
      ["DILNOZA","J'aimerais poser trois questions, si vous avez une minute."],
      ["CLAUDINE","Allez-y, je vous écoute."],
      ["DILNOZA","Est-ce que le chauffage est vraiment compris dans le loyer ?"],
      ["CLAUDINE","Oui. Onze cent cinquante dollars, chauffage et électricité compris. Il n'y a rien à ajouter."],
      ["DILNOZA","Est-ce qu'il y a une buanderie dans l'immeuble ?"],
      ["CLAUDINE","Au sous-sol. Deux laveuses, deux sécheuses. Deux dollars la brassée."],
      ["DILNOZA","Et le logement est libre à quelle date, exactement ?"],
      ["CLAUDINE","Le premier juillet. Le bail est de douze mois."],
      ["DILNOZA","Merci. Est-ce que je pourrais le visiter cette semaine ?"],
      ["CLAUDINE","Bien sûr. Samedi matin, dix heures, ça vous irait ?"],
      ["DILNOZA","Samedi, dix heures. Je vais venir avec mon mari. C'est quelle adresse ?"],
      ["CLAUDINE","Sept mille quatre cent douze, rue Chabot. Deuxième étage, la porte de droite."],
      ["DILNOZA","Sept mille quatre cent douze, rue Chabot, samedi dix heures. Merci beaucoup, madame."],
    ]
  },

  t3: {
    label: "Dialogue — Entrez, je vais vous montrer",
    lines: [
      ["CLAUDINE","Entrez, entrez. Vous avez trouvé facilement ?"],
      ["DILNOZA","Oui, merci. L'autobus arrête juste au coin."],
      ["CLAUDINE","Alors voici la cuisine. Le balcon est derrière, par cette porte-là."],
      ["DILNOZA","Il est grand. Est-ce que les fenêtres sont neuves ?"],
      ["CLAUDINE","Elles ont été changées l'an dernier. Le logement est chaud l'hiver."],
      ["DILNOZA","Et les deux chambres, elles sont où ?"],
      ["CLAUDINE","Au fond du couloir, à côté de la salle de bain."],
      ["DILNOZA","La deuxième est plus petite. C'est parfait pour mon garçon."],
      ["CLAUDINE","L'école primaire est à cinq minutes à pied, sur la même rue."],
      ["DILNOZA","Est-ce qu'il y a un stationnement pour l'auto ?"],
      ["CLAUDINE","Non. Il n'y a pas de stationnement. On se gare dans la rue, avec une vignette."],
      ["DILNOZA","Ce n'est pas grave, nous n'avons pas d'auto. Et la buanderie ?"],
      ["THÉO","Je vais vous montrer. Je suis Théo, le concierge. C'est en bas."],
      ["DILNOZA","Merci. Est-ce qu'elle est ouverte le soir ?"],
      ["THÉO","De sept heures du matin à dix heures du soir, tous les jours."],
      ["DILNOZA","Madame, est-ce que je dois donner de l'argent aujourd'hui ?"],
      ["CLAUDINE","Non. Jamais de dépôt : c'est interdit au Québec. Le premier loyer se paie le premier juillet."],
      ["DILNOZA","Merci beaucoup. Le logement me plaît. Je vous rappelle demain."],
    ]
  },

  appli: {
    label: "Dialogue — Un deux et demie meublé",
    lines: [
      ["RACHID","Bonjour, je vous appelle pour le deux et demie de la rue Saint-Hubert."],
      ["CLAUDINE","Bonjour. Il est encore libre, oui."],
      ["RACHID","L'annonce dit « meublé ». Qu'est-ce qu'il y a dedans ?"],
      ["CLAUDINE","Un lit, une table, deux chaises et une commode. Pas de vaisselle."],
      ["RACHID","Et le loyer, c'est bien sept cent quatre-vingts dollars ?"],
      ["CLAUDINE","Sept cent quatre-vingts, chauffage et électricité compris. Internet n'est pas compris."],
      ["RACHID","Il est libre à quelle date ?"],
      ["CLAUDINE","Tout de suite. Vous pourriez entrer la semaine prochaine."],
      ["RACHID","Est-ce que je pourrais le voir demain après-midi ?"],
      ["CLAUDINE","Demain, deux heures. Je vous attends."],
    ]
  },
};
