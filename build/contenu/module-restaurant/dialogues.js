const DIALOGUES = {
  prep: {
    label: "Dialogue — À l'entrée du restaurant",
    lines: [
      ["SOPHIE","Bonsoir ! Vous êtes combien ?"],
      ["ANDRÉS","Bonsoir. Deux, s'il vous plaît."],
      ["SOPHIE","Vous avez une réservation ?"],
      ["ANDRÉS","Non, je n'en ai pas. Est-ce qu'il y a de la place ?"],
      ["SOPHIE","Oui, ça va. Vous préférez près de la fenêtre ou au fond ?"],
      ["ANDRÉS","Près de la fenêtre, si c'est possible."],
      ["SOPHIE","Suivez-moi. Voici la carte. Le menu du jour est sur l'ardoise, là-bas."],
      ["MANON","Merci. On peut prendre deux minutes avant de commander ?"],
      ["SOPHIE","Bien sûr, prenez votre temps. Je vous envoie quelqu'un dans cinq minutes."],
      ["ANDRÉS","Manon, c'est quoi la différence entre la carte et le menu du jour ?"],
      ["MANON","La carte, c'est tout ce qu'ils font. Le menu du jour change chaque jour et coûte moins cher."],
      ["ANDRÉS","Et la table d'hôte ?"],
      ["MANON","C'est un prix fixe pour trois services : entrée, plat, dessert. Souvent le meilleur choix."],
    ]
  },

  t1: {
    label: "Dialogue — La commande",
    lines: [
      ["VINCENT","Bonsoir. Vous avez fait votre choix ?"],
      ["ANDRÉS","Presque. Qu'est-ce qu'il y a dans la table d'hôte ce soir ?"],
      ["VINCENT","Soupe ou salade en entrée, ensuite le poisson du jour ou le poulet, et dessert au choix."],
      ["ANDRÉS","Le poisson du jour, c'est quoi aujourd'hui ?"],
      ["VINCENT","De la truite, servie avec des légumes et du riz."],
      ["ANDRÉS","Je prendrais la table d'hôte, avec la soupe et la truite."],
      ["VINCENT","Très bien. Et pour vous, madame ?"],
      ["MANON","Je vais prendre le poulet, mais à la carte. Sans entrée."],
      ["VINCENT","Parfait. Quelque chose à boire ?"],
      ["ANDRÉS","De l'eau, s'il vous plaît. Est-ce que l'eau du robinet est gratuite ?"],
      ["VINCENT","Oui, bien sûr. Une carafe pour deux ?"],
      ["ANDRÉS","Oui, merci. Ah — est-ce qu'il y a des arachides dans le dessert ?"],
      ["VINCENT","Je vérifie en cuisine et je vous le dis avant de le servir."],
    ]
  },

  t2: {
    label: "Dialogue — Pendant le repas",
    lines: [
      ["VINCENT","Est-ce que tout va bien ?"],
      ["MANON","Très bien, merci."],
      ["ANDRÉS","Excusez-moi, est-ce que je pourrais avoir un peu de sel, s'il vous plaît ?"],
      ["VINCENT","Tout de suite. Autre chose ?"],
      ["ANDRÉS","Non, ça va. Merci."],
      ["MANON","Andrés, ton poisson est comment ?"],
      ["ANDRÉS","Très bon. Un peu froid, par exemple."],
      ["MANON","Dis-le. Ils vont le réchauffer, ça arrive tout le temps."],
      ["ANDRÉS","Je n'ose pas trop."],
      ["MANON","Ce n'est pas se plaindre, c'est normal. Regarde, je l'appelle."],
      ["VINCENT","Oui ?"],
      ["ANDRÉS","Excusez-moi, mon poisson est un peu froid. Est-ce que ce serait possible de le réchauffer ?"],
      ["VINCENT","Bien sûr, je suis désolé. Je vous le rapporte dans deux minutes."],
    ]
  },

  t2b: {
    label: "Dialogue — Un plat qui ne convient pas",
    lines: [
      ["MANON","J'avais demandé le poulet sans sauce. Il y en a beaucoup."],
      ["VINCENT","Ah, je suis désolé. Je vous en rapporte un autre ?"],
      ["MANON","Ce n'est pas nécessaire, je vais l'enlever. Mais je préfère vous le dire."],
      ["VINCENT","Vous faites bien. Je le note pour la cuisine."],
      ["ANDRÉS","Tu ne veux pas qu'ils le refassent ?"],
      ["MANON","Non, ça prendrait vingt minutes et tu aurais fini de manger."],
      ["ANDRÉS","Chez moi, on ne dirait rien du tout."],
      ["MANON","Ici non plus, beaucoup de gens ne disent rien. Mais ils préfèrent qu'on le dise."],
      ["ANDRÉS","Pourquoi ?"],
      ["MANON","Parce que sinon, ils ne savent pas que quelque chose n'a pas marché."],
    ]
  },

  t3: {
    label: "Dialogue — L'addition",
    lines: [
      ["ANDRÉS","L'addition, s'il vous plaît."],
      ["VINCENT","Tout de suite. Ensemble ou séparé ?"],
      ["ANDRÉS","Ensemble, c'est moi qui invite."],
      ["MANON","Andrés, non, on partage."],
      ["ANDRÉS","Non, tu m'as aidé toute la semaine. Ensemble, s'il vous plaît."],
      ["VINCENT","Voilà. Cinquante-huit dollars et quarante, taxes comprises."],
      ["ANDRÉS","Manon, le pourboire, c'est combien ici ?"],
      ["MANON","Quinze pour cent du montant avant taxes, en général. Ici, ça fait environ sept dollars et demi."],
      ["ANDRÉS","Ce n'est pas sur l'addition ?"],
      ["MANON","Non, tu l'ajoutes toi-même. Le terminal te propose des pourcentages, mais tu peux entrer le montant que tu veux."],
      ["ANDRÉS","Et si le service n'était pas bon ?"],
      ["MANON","Tu peux donner moins. Mais ici, le pourboire fait partie du salaire du serveur, ce n'est pas juste un remerciement."],
    ]
  },

  t3b: {
    label: "Dialogue — Au terminal",
    lines: [
      ["VINCENT","Vous payez comment ? Débit ou crédit ?"],
      ["ANDRÉS","Débit, s'il vous plaît."],
      ["VINCENT","Voilà. Il va vous demander le pourboire en premier."],
      ["ANDRÉS","Je choisis un pourcentage, ou j'entre un montant ?"],
      ["VINCENT","Comme vous voulez. « Autre montant », en bas, si vous préférez décider vous-même."],
      ["ANDRÉS","Est-ce que le pourcentage proposé est calculé avant ou après les taxes ?"],
      ["VINCENT","Après, sur beaucoup de terminaux. C'est pour ça que certains préfèrent entrer le montant."],
      ["ANDRÉS","Je vais entrer sept dollars cinquante, alors."],
      ["VINCENT","Parfait. Ensuite, votre code."],
      ["ANDRÉS","Voilà. Merci beaucoup, c'était très bon."],
      ["VINCENT","Merci à vous. Bonne fin de soirée !"],
    ]
  },

  appli: {
    label: "Dialogue — Le midi, en semaine",
    lines: [
      ["SOPHIE","Bonjour ! Une personne ?"],
      ["ANDRÉS","Bonjour. Oui, une seule. Est-ce que le menu du midi est encore servi ?"],
      ["SOPHIE","Jusqu'à deux heures. Il vous reste vingt minutes."],
      ["ANDRÉS","Parfait. Qu'est-ce qu'il y a aujourd'hui ?"],
      ["SOPHIE","Trois choix : la lasagne, le sandwich au poulet, ou la soupe-repas."],
      ["ANDRÉS","La soupe-repas, c'est quoi exactement ?"],
      ["SOPHIE","Une grosse soupe avec des légumes, des pâtes et du poulet. Servie avec du pain."],
      ["ANDRÉS","Je prendrais ça. Et un café après, s'il vous plaît."],
      ["SOPHIE","Le café est inclus dans le menu du midi."],
      ["ANDRÉS","Ah, parfait. Est-ce que je peux avoir l'addition en même temps ? Je suis un peu pressé."],
      ["SOPHIE","Bien sûr, je vous l'apporte avec le repas."],
    ]
  },
};
