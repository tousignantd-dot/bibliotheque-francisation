const DIALOGUES = {
  prep: {
    label: "Dialogue — Tu paies trop cher, Rosario",
    lines: [
      ["MAXIME","Rosario, tu achètes encore un dix passages ce matin ?"],
      ["ROSARIO","Oui. Trente-cinq dollars. Je fais ça chaque semaine depuis septembre."],
      ["MAXIME","Chaque semaine ? Tu paies beaucoup trop cher."],
      ["ROSARIO","Pourquoi ? Dix passages, c'est dix voyages. C'est simple."],
      ["MAXIME","Oui, mais tu viens à l'école cinq matins et tu retournes cinq soirs."],
      ["ROSARIO","Ça fait dix. C'est correct, non ?"],
      ["MAXIME","Et le samedi ? Et l'épicerie ? Tu achètes un deuxième dix passages."],
      ["ROSARIO","C'est vrai. Des fois, j'en achète deux dans la même semaine."],
      ["MAXIME","Alors regarde ta carte. C'est une carte OPUS ?"],
      ["ROSARIO","Je pense que oui. C'est la carte bleue et blanche."],
      ["MAXIME","Sur une carte OPUS, tu peux mettre un titre mensuel. Un seul prix pour tout le mois."],
      ["ROSARIO","Un mois complet ? Et je peux prendre le métro et l'autobus ?"],
      ["MAXIME","Tous les jours, autant de fois que tu veux, dans la zone A."],
      ["ROSARIO","Et ça coûte combien, ce titre-là ?"],
      ["MAXIME","Va au point de service de la station. Demande-leur. Moi, je te dis juste que tu paies trop."],
    ]
  },

  t1: {
    label: "Dialogue — Quatre titres, quatre prix",
    lines: [
      ["ROSARIO","Bonjour. Mon ami dit que je paie trop cher. Je voudrais me renseigner."],
      ["LORRAINE","Bonjour. Vous vous déplacez combien de fois par semaine ?"],
      ["ROSARIO","Cinq jours. Le matin et le soir. Des fois le samedi aussi."],
      ["LORRAINE","Et vous restez dans l'île de Montréal ? C'est la zone A."],
      ["ROSARIO","Oui. La maison, l'école, l'épicerie. Tout est à Montréal."],
      ["LORRAINE","Bon. Un passage tout seul coûte trois dollars soixante-quinze."],
      ["ROSARIO","Et le dix passages ? C'est celui-là que j'achète."],
      ["LORRAINE","Trente-cinq dollars. Ça revient à trois cinquante le passage."],
      ["ROSARIO","D'accord. Et pour une semaine complète ?"],
      ["LORRAINE","L'hebdo est à trente-trois vingt-cinq. Il est bon du lundi au dimanche."],
      ["ROSARIO","Trente-trois ? C'est moins cher que le dix passages !"],
      ["LORRAINE","Oui, et c'est illimité. Mais le mensuel est encore mieux pour vous."],
      ["ROSARIO","Combien coûte le mensuel ?"],
      ["LORRAINE","Cent dix dollars pour le mois. Vous, vous payez à peu près cent quarante."],
      ["ROSARIO","Cent dix… Je vais y penser. Merci beaucoup, madame."],
    ]
  },

  t2: {
    label: "Dialogue — Je voudrais un mensuel, s'il vous plaît",
    lines: [
      ["ROSARIO","Bonjour. Je voudrais un titre mensuel, s'il vous plaît."],
      ["LORRAINE","Bien sûr. Vous avez votre carte OPUS avec vous ?"],
      ["ROSARIO","La voici. Est-ce que je dois acheter une nouvelle carte ?"],
      ["LORRAINE","Non. Je recharge celle-là. Le titre s'ajoute dessus."],
      ["ROSARIO","Est-ce que ma fille peut avoir le tarif réduit ? Elle a quinze ans."],
      ["LORRAINE","Oui, de six à dix-sept ans. Mais il lui faut une carte avec photo."],
      ["ROSARIO","Où est-ce qu'on fait la photo ?"],
      ["LORRAINE","Ici même. Apportez une preuve de son âge et venez avec elle."],
      ["ROSARIO","Et ma mère ? Elle a soixante-huit ans."],
      ["LORRAINE","Soixante-cinq ans et plus, c'est aussi le tarif réduit. Même chose : une carte avec photo."],
      ["ROSARIO","Merci. Alors juste le mensuel pour moi aujourd'hui."],
      ["LORRAINE","Cent dix dollars. Vous payez comptant ou par carte ?"],
      ["ROSARIO","Par carte. Est-ce que je peux répéter pour être sûre ?"],
      ["LORRAINE","Allez-y."],
      ["ROSARIO","Un mensuel, zone A, cent dix dollars, bon jusqu'à la fin du mois. C'est ça ?"],
      ["LORRAINE","C'est exactement ça. N'oubliez pas de valider votre carte au tourniquet."],
    ]
  },

  t3: {
    label: "Dialogue — Ce qui est écrit sur la grille",
    lines: [
      ["ROSARIO","Monsieur, la grille est affichée au mur, mais je ne comprends pas tout."],
      ["NORMAND","Montrez-moi la ligne qui vous embête."],
      ["ROSARIO","Ici : « Soirée illimitée, six dollars soixante-quinze, valide de 18 h à 5 h »."],
      ["NORMAND","Ça veut dire à partir de six heures du soir, jusqu'à cinq heures le lendemain matin."],
      ["ROSARIO","Et « Week-end illimité, du vendredi 16 h au lundi 5 h » ?"],
      ["NORMAND","Trois jours complets pour dix-sept dollars. C'est bon si vous sortez la fin de semaine."],
      ["ROSARIO","Et cette colonne-là ? « Réduit 6-17 ans »."],
      ["NORMAND","C'est le prix pour les jeunes de six à dix-sept ans. Avec une carte avec photo."],
      ["ROSARIO","Mon garçon a neuf ans. Est-ce que je paie pour lui ?"],
      ["NORMAND","Onze ans et moins, c'est gratuit, s'il est avec vous. Vous devez avoir votre titre validé."],
      ["ROSARIO","Gratuit ? Je ne savais pas ça."],
      ["NORMAND","Une personne peut accompagner cinq enfants au maximum."],
      ["ROSARIO","Et en bas, le petit dessin de la chaise ?"],
      ["NORMAND","Les places réservées, en avant de l'autobus. Pour les personnes à mobilité réduite, les femmes enceintes et les aînés."],
      ["ROSARIO","Merci. Maintenant je peux lire le tableau toute seule."],
    ]
  },

  appli: {
    label: "Dialogue — Un titre pour la fin de semaine",
    lines: [
      ["MAXIME","Bonjour. Ma sœur arrive samedi et elle reste trois jours."],
      ["LORRAINE","Elle va se déplacer beaucoup ?"],
      ["MAXIME","Oui, elle veut visiter la ville. Le métro, l'autobus, partout."],
      ["LORRAINE","Alors le Week-end illimité. Dix-sept dollars, du vendredi seize heures au lundi cinq heures."],
      ["MAXIME","Elle n'a pas de carte OPUS. Est-ce que c'est un problème ?"],
      ["LORRAINE","Non. Je peux le mettre sur une carte à puce occasionnelle."],
      ["MAXIME","Parfait. Est-ce qu'elle peut aller à Laval avec ça ?"],
      ["LORRAINE","Non, seulement la zone A. Pour Laval, il faut un titre Tous modes AB."],
    ]
  },
};
