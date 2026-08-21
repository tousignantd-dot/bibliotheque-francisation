const DIALOGUES = {
  prep: {
    label: "Dialogue — Le tableau au-dessus de la caisse",
    lines: [
      ["YOLETTE","Fatou, on mange où ce midi ? J'ai seulement une heure."],
      ["FATOU","Chez Marcel, le casse-croûte au coin. On commande au comptoir, c'est vite."],
      ["YOLETTE","Il n'y a pas de serveur ?"],
      ["FATOU","Non. Tu fais la file, tu commandes, tu paies, et on t'appelle quand c'est prêt."],
      ["YOLETTE","Et le menu ? Je ne vois pas de papier sur les tables."],
      ["FATOU","Regarde en haut, au-dessus de la caisse. Le grand tableau, c'est le menu."],
      ["YOLETTE","Ah oui. Il y a des photos et des colonnes de chiffres."],
      ["FATOU","À gauche, ce que tu manges. À droite, le prix. En bas, les breuvages."],
      ["YOLETTE","Et les trois chiffres à côté de la soupe ?"],
      ["FATOU","Ce sont les trois formats : petit, moyen, grand."],
      ["YOLETTE","Trois prix pour la même soupe. D'accord."],
      ["FATOU","Prends ton plateau au bout du comptoir. Les serviettes sont là aussi."],
    ]
  },

  t1: {
    label: "Dialogue — Lire le tableau avant de commander",
    lines: [
      ["YOLETTE","Il y a beaucoup de choses écrites. Par où je commence ?"],
      ["FATOU","Par le titre des colonnes. « Sandwichs », « Soupes », « Breuvages », « Extras »."],
      ["YOLETTE","Sandwich au poulet, sandwich aux œufs, sandwich au jambon."],
      ["FATOU","« Au poulet », ça veut dire qu'il y a du poulet dedans. C'est ça qui change."],
      ["YOLETTE","Et « servi avec salade ou frites » ?"],
      ["FATOU","C'est l'accompagnement. Il vient avec le sandwich, tu ne paies pas plus."],
      ["YOLETTE","Alors le trio, c'est quoi ?"],
      ["FATOU","Le trio, c'est le sandwich, l'accompagnement et le breuvage ensemble. Un seul prix."],
      ["YOLETTE","C'est moins cher que trois choses séparées ?"],
      ["FATOU","Oui, un peu. Regarde la colonne de droite et compare."],
      ["YOLETTE","Et cette ligne en bas, avec le petit dessin de feuille ?"],
      ["FATOU","Ça veut dire sans viande. La soupe aux légumes est là."],
      ["YOLETTE","Bon. Un trio sandwich au poulet, soupe petite, jus. Je suis prête."],
    ]
  },

  t2: {
    label: "Dialogue — Au comptoir, chez Marcel",
    lines: [
      ["STEVE","Bonjour ! Prochaine personne, s'il vous plaît."],
      ["YOLETTE","Bonjour. Je voudrais un trio sandwich au poulet, s'il vous plaît."],
      ["STEVE","Avec salade ou avec frites ?"],
      ["YOLETTE","Avec salade, s'il vous plaît."],
      ["STEVE","Et comme breuvage ?"],
      ["YOLETTE","Un jus de pomme. Est-ce que je peux avoir une soupe aussi ?"],
      ["STEVE","Oui. Quel format ? Petit, moyen ou grand ?"],
      ["YOLETTE","Petit, s'il vous plaît. La soupe aux légumes."],
      ["STEVE","Parfait. Pour ici ou pour emporter ?"],
      ["YOLETTE","Pour ici."],
      ["STEVE","Ça fait onze dollars et quarante. Débit ou comptant ?"],
      ["YOLETTE","Débit, s'il vous plaît."],
      ["STEVE","Merci. Voici votre reçu. Votre numéro est le 42."],
      ["YOLETTE","Le 42. Merci beaucoup."],
    ]
  },

  t3: {
    label: "Dialogue — Numéro 42 !",
    lines: [
      ["MARCEL","Numéro 42 ! Le trio poulet, numéro 42 !"],
      ["YOLETTE","C'est moi. Bonjour."],
      ["MARCEL","Voilà. Le sandwich, la salade, le jus. Et votre petite soupe."],
      ["YOLETTE","Merci. Excusez-moi, je n'ai pas de cuillère pour la soupe."],
      ["MARCEL","Les ustensiles sont là, à votre gauche, dans les bacs."],
      ["YOLETTE","D'accord. Est-ce qu'il y a des serviettes de table aussi ?"],
      ["MARCEL","Oui, juste à côté. Prenez-en deux, la soupe est pleine."],
      ["YOLETTE","Merci. Et est-ce que je peux avoir du sel et du poivre ?"],
      ["MARCEL","Servez-vous. Il y a aussi de la moutarde et du ketchup au bout."],
      ["YOLETTE","Une dernière chose. Il manque le jus dans mon plateau."],
      ["MARCEL","Ah, excusez-moi. Vous avez pris quoi ? Un jus de pomme ?"],
      ["YOLETTE","Oui, un jus de pomme."],
      ["MARCEL","Il n'en reste plus. Je vous donne un jus d'orange, ça va ?"],
      ["YOLETTE","Ça va, merci. Bonne journée !"],
    ]
  },

  appli: {
    label: "Dialogue — Toute seule au comptoir",
    lines: [
      ["YOLETTE","Bonjour. Je voudrais une soupe et un sandwich aux œufs, s'il vous plaît."],
      ["STEVE","Quel format pour la soupe ?"],
      ["YOLETTE","Moyen, s'il vous plaît. Qu'est-ce qu'il y a comme soupe aujourd'hui ?"],
      ["STEVE","Soupe aux légumes ou soupe au poulet et nouilles."],
      ["YOLETTE","Aux légumes, alors. Et un café, s'il vous plaît."],
      ["STEVE","Pour ici ou pour emporter ?"],
      ["YOLETTE","Pour emporter. Est-ce que vous mettez un couvercle sur la soupe ?"],
      ["STEVE","Oui, un couvercle et une cuillère dans le sac. Numéro 17."],
    ]
  },
};
