const DIALOGUES = {
  prep: {
    label: "Dialogue — Qu'est-ce qu'on fait dans un bureau de poste ?",
    lines: [
      ["YASSINE","Denise, il y a un bureau de poste près d'ici ?"],
      ["DENISE","Oui, sur la 3e Avenue, à dix minutes à pied. Pourquoi ?"],
      ["YASSINE","Je veux envoyer une boîte à mon frère, à Calgary."],
      ["DENISE","Alors c'est là. On y envoie des lettres et des colis."],
      ["YASSINE","Et les timbres, on les achète où ?"],
      ["DENISE","Au même comptoir. En carnet, ça coûte moins cher qu'à l'unité."],
      ["YASSINE","Est-ce qu'on peut faire autre chose là-bas ?"],
      ["DENISE","Beaucoup de choses. Un envoi recommandé, un mandat-poste, un changement d'adresse."],
      ["YASSINE","Un mandat-poste, c'est quoi ?"],
      ["DENISE","Un papier qui vaut de l'argent. On l'envoie quand on ne veut pas envoyer du comptant."],
      ["YASSINE","Et la boîte rouge, dans la rue ?"],
      ["DENISE","C'est pour les lettres déjà timbrées. Jamais pour un colis."],
      ["YASSINE","Est-ce que la préposée parle vite ?"],
      ["DENISE","Un peu. Demande-lui de répéter, elle va le faire. C'est normal."],
      ["YASSINE","Ça ouvre à quelle heure, le jeudi ?"],
      ["DENISE","À neuf heures. Vas-y le matin : il y a moins de monde."],
    ]
  },

  t1: {
    label: "Dialogue — Combien ça coûte et combien de temps ça prend ?",
    lines: [
      ["YASSINE","Bonjour. Je voudrais envoyer ce colis, s'il vous plaît."],
      ["CAROLE","Bonjour. Il va où, votre colis ?"],
      ["YASSINE","À Calgary, en Alberta."],
      ["CAROLE","Parfait. Je le pèse. Deux kilos et cent grammes."],
      ["YASSINE","Combien est-ce que ça coûte ?"],
      ["CAROLE","Ça dépend de la vitesse. Vous êtes pressé ?"],
      ["YASSINE","Pas trop. C'est un cadeau pour le douze du mois."],
      ["CAROLE","Alors le colis standard suffit. C'est le moins cher."],
      ["YASSINE","Combien de temps est-ce que ça prend ?"],
      ["CAROLE","De Québec à Calgary, comptez à peu près une semaine."],
      ["YASSINE","Et si je veux plus vite ?"],
      ["CAROLE","L'Xpresspost arrive en un ou deux jours ouvrables. Mais c'est plus cher."],
      ["YASSINE","Est-ce que je pourrais suivre le colis sur Internet ?"],
      ["CAROLE","Oui. Le repérage est compris dans les deux services."],
      ["YASSINE","Est-ce que vous pouvez répéter le prix, s'il vous plaît ?"],
      ["CAROLE","Bien sûr. Standard, vingt-deux dollars. Xpresspost, trente-huit dollars."],
    ]
  },

  t2: {
    label: "Dialogue — Qu'est-ce qu'il y a dans la boîte ?",
    lines: [
      ["CAROLE","Qu'est-ce qu'il y a dans la boîte, monsieur ?"],
      ["YASSINE","Il y a des vêtements et un livre. Rien de fragile."],
      ["CAROLE","Rien de liquide, rien de dangereux ?"],
      ["YASSINE","Non, rien. Juste des vêtements et un livre."],
      ["CAROLE","Bon. Alors, standard ou Xpresspost ?"],
      ["YASSINE","Le standard. Je vais le prendre."],
      ["CAROLE","Très bien. Il me faut l'adresse complète, avec le code postal."],
      ["YASSINE","Je l'ai écrite sur la boîte. Est-ce que c'est correct ?"],
      ["CAROLE","Oui. Votre adresse en haut à gauche, la sienne au milieu. C'est parfait."],
      ["YASSINE","J'aimerais aussi des timbres pour des lettres."],
      ["CAROLE","En carnet ou à l'unité ? Le carnet coûte moins cher."],
      ["YASSINE","Donnez-moi un carnet, s'il vous plaît."],
      ["CAROLE","Voilà. Autre chose ?"],
      ["YASSINE","Ces enveloppes-là, elles coûtent combien ?"],
      ["CAROLE","Deux dollars chacune."],
      ["YASSINE","Je vais en prendre trois. Ça fait combien en tout ?"],
    ]
  },

  t3: {
    label: "Dialogue — Ce carton-là était dans ma boîte aux lettres",
    lines: [
      ["YASSINE","Bonjour. J'ai trouvé ce carton-là dans ma boîte aux lettres."],
      ["CAROLE","C'est un avis de livraison. Votre colis est ici."],
      ["YASSINE","Qu'est-ce qu'il faut apporter ?"],
      ["CAROLE","Le carton et une pièce d'identité avec photo. Les deux."],
      ["YASSINE","J'ai mon permis de conduire. Ça va ?"],
      ["CAROLE","Ça va très bien. Un instant, je vais le chercher."],
      ["YASSINE","Est-ce que vous le gardez longtemps, un colis ?"],
      ["CAROLE","Quinze jours. Après, il retourne à la personne qui l'a envoyé."],
      ["YASSINE","Quinze jours seulement ? Je ne le savais pas."],
      ["CAROLE","On envoie un deuxième carton après cinq jours, pour rappeler."],
      ["YASSINE","J'ai une autre question. Je déménage le premier juillet."],
      ["CAROLE","Vous pouvez faire suivre votre courrier à la nouvelle adresse."],
      ["YASSINE","Pendant combien de temps ?"],
      ["CAROLE","Jusqu'à douze mois. Mais attention : les colis ne suivent pas."],
      ["YASSINE","Seulement les lettres, alors ?"],
      ["CAROLE","Les lettres, le recommandé et les magazines. Demandez-le avant de déménager."],
    ]
  },

  appli: {
    label: "Dialogue — Ça s'est bien passé ?",
    lines: [
      ["DENISE","Alors, ça s'est bien passé au bureau de poste ?"],
      ["YASSINE","Très bien. J'ai posé mes questions avant de choisir."],
      ["DENISE","Et tu as pris quoi ?"],
      ["YASSINE","Le colis standard. Vingt-deux dollars, une semaine."],
      ["DENISE","C'est le bon choix pour un cadeau qui n'est pas pressé."],
      ["YASSINE","J'ai aussi acheté un carnet de timbres et trois enveloppes."],
      ["DENISE","Tu vois ? Ce n'était pas si difficile."],
      ["YASSINE","Non. Il fallait juste demander avant de dire oui."],
    ]
  },
};
