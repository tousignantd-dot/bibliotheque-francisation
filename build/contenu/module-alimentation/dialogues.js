const DIALOGUES = {
  prep: {
    label: "Dialogue — Dans l'allée des conserves",
    lines: [
      ["FARIDA","Excusez-moi, je cherche de la pâte de tomate. J'ai fait deux fois le tour."],
      ["SIMON","De la pâte de tomate… C'est dans l'allée cinq, avec les sauces. Pas avec les légumes en conserve."],
      ["FARIDA","Ah, je cherchais du mauvais côté. Il y a plusieurs marques ?"],
      ["SIMON","Trois ou quatre. Celle du bas est la moins chère, mais elle est plus salée."],
      ["FARIDA","Comment vous savez ça ?"],
      ["SIMON","C'est écrit sur l'étiquette. Regardez la ligne du sodium : deux cent quarante milligrammes contre quatre-vingts."],
      ["FARIDA","Je ne sais jamais où regarder sur ces étiquettes."],
      ["SIMON","Le tableau de la valeur nutritive est toujours au dos, en noir et blanc. Toujours au même endroit."],
      ["FARIDA","Et ça, ça vient d'où ?"],
      ["SIMON","La provenance est écrite en petit, sous le code-barres. Celle-là vient de l'Ontario."],
      ["FARIDA","Merci beaucoup. Vous m'avez sauvé dix minutes."],
      ["SIMON","Ça fait plaisir. Si vous ne trouvez pas quelque chose, demandez : on connaît nos allées par cœur."],
    ]
  },

  t1: {
    label: "Dialogue — Ça se garde combien de temps ?",
    lines: [
      ["FARIDA","J'aimerais acheter du poisson frais, mais je ne le cuisine pas ce soir."],
      ["JOHANNE","Ça se garde deux jours au réfrigérateur, pas plus. Après, il faut le congeler."],
      ["FARIDA","Et si je le congèle tout de suite ?"],
      ["JOHANNE","Trois mois, facilement. Emballez-le bien, sinon il sèche."],
      ["FARIDA","Est-ce qu'il y a de la truite aujourd'hui ?"],
      ["JOHANNE","Oui, de la truite d'élevage, du Québec. Il y a aussi du saumon, mais lui vient de l'Atlantique."],
      ["FARIDA","Je prends de la truite. Elle est comment, à la cuisson ?"],
      ["JOHANNE","Plus délicate que le saumon. Ne la faites pas trop cuire : dix minutes suffisent."],
      ["FARIDA","Et pour la conserver, je fais quoi exactement ?"],
      ["JOHANNE","Vous la sortez du papier, vous la mettez dans un contenant fermé, et vous la placez dans le bas du frigo."],
      ["FARIDA","Dans le bas, d'accord. Pourquoi le bas ?"],
      ["JOHANNE","C'est l'endroit le plus froid. Et ça évite que le jus coule sur le reste."],
    ]
  },

  t2: {
    label: "Dialogue — Au comptoir de la boucherie",
    lines: [
      ["JOHANNE","Bonjour ! Qu'est-ce que je vous sers ?"],
      ["FARIDA","Bonjour. Je voudrais du poulet, s'il vous plaît. Des poitrines."],
      ["JOHANNE","Combien vous en voulez ?"],
      ["FARIDA","Quatre. Ça fait combien de poids, à peu près ?"],
      ["JOHANNE","Quatre poitrines, ça fait environ une livre et demie. Autour de huit dollars."],
      ["FARIDA","C'est parfait. Est-ce que je peux en avoir deux emballées séparément ?"],
      ["JOHANNE","Bien sûr. Deux et deux. Autre chose ?"],
      ["FARIDA","Oui, du bœuf haché. Il vous en reste du maigre ?"],
      ["JOHANNE","Il m'en reste, oui. Une livre, ça va ?"],
      ["FARIDA","Une livre, parfait. Et ça se garde combien de temps ?"],
      ["JOHANNE","Le haché, deux jours au frigo. C'est ce qui se garde le moins longtemps."],
      ["FARIDA","Alors je vais le cuisiner demain. Merci !"],
    ]
  },

  t2b: {
    label: "Dialogue — Je n'en prends pas aujourd'hui",
    lines: [
      ["SIMON","Vous avez trouvé tout ce que vous cherchiez ?"],
      ["FARIDA","Presque. Je voulais du riz basmati, mais il n'y en a plus."],
      ["SIMON","Il en reste peut-être en arrière. Quel format vous voulez ?"],
      ["FARIDA","Le grand sac, celui de huit kilos."],
      ["SIMON","Ah, celui-là, on n'en a plus jusqu'à jeudi. Il en reste des petits, par exemple."],
      ["FARIDA","Je vais attendre jeudi. Je n'en prends pas de petits, ça revient plus cher."],
      ["SIMON","Vous avez raison. Le grand format coûte presque moitié moins au kilo."],
      ["FARIDA","Et le savon à vaisselle, il est dans quelle allée ?"],
      ["SIMON","Allée huit, avec les produits d'entretien. Il y en a un en spécial cette semaine."],
      ["FARIDA","Parfait, j'en prends deux. Merci."],
    ]
  },

  t3: {
    label: "Dialogue — Ce qui est écrit sur l'étiquette",
    lines: [
      ["CLAUDE","Tu regardes toujours les étiquettes ? Moi, je n'y comprends rien."],
      ["FARIDA","J'ai appris à regarder trois lignes seulement. Le reste, je le saute."],
      ["CLAUDE","Lesquelles ?"],
      ["FARIDA","La portion, en haut. Tout le tableau parle de cette portion-là, pas du contenant."],
      ["CLAUDE","Ah, c'est pour ça que les chiffres sont si petits."],
      ["FARIDA","Exactement. Ensuite le sodium, et le sucre. Ce sont les deux qui varient le plus d'une marque à l'autre."],
      ["CLAUDE","Et la date, tu la regardes où ?"],
      ["FARIDA","« Meilleur avant », en avant ou sur le dessus. Ce n'est pas une date de danger, c'est une date de qualité."],
      ["CLAUDE","Ce n'est pas pareil ?"],
      ["FARIDA","Non. « Meilleur avant » veut dire que le goût change après. « Date limite d'utilisation », ça, c'est sérieux."],
      ["CLAUDE","Je ne savais pas. Et le mode d'emploi du savon, tu le lis ?"],
      ["FARIDA","Celui-là, oui, toujours. La dose est écrite dessus, et j'en mettais deux fois trop."],
    ]
  },

  t3b: {
    label: "Dialogue — Le mode d'emploi du nettoyant",
    lines: [
      ["CLAUDE","« Diluer trente millilitres dans quatre litres d'eau tiède. » Trente millilitres, c'est combien ?"],
      ["FARIDA","Deux cuillères à soupe, à peu près. Il y a un bouchon doseur sur la bouteille."],
      ["CLAUDE","Et après ? Il faut rincer ?"],
      ["FARIDA","C'est écrit juste en dessous : « Rincer à l'eau claire. Ne pas mélanger avec un produit chloré. »"],
      ["CLAUDE","Ne pas mélanger, ça, je le savais."],
      ["FARIDA","Beaucoup de gens ne le savent pas. C'est écrit en gras, avec un triangle, en bas de l'étiquette."],
      ["CLAUDE","Et « tenir hors de la portée des enfants », c'est partout, non ?"],
      ["FARIDA","Sur tous les produits d'entretien, oui. Les avertissements sont toujours en bas, séparés du reste."],
      ["CLAUDE","Donc : la dose en haut, les étapes au milieu, les avertissements en bas."],
      ["FARIDA","C'est ça. Trois blocs, toujours dans le même ordre."],
    ]
  },

  appli: {
    label: "Dialogue — Au comptoir de la charcuterie",
    lines: [
      ["FARIDA","Bonjour. Je voudrais du jambon, s'il vous plaît."],
      ["SIMON","Bonjour. Tranché mince ou épais ?"],
      ["FARIDA","Mince, s'il vous plaît. Deux cents grammes."],
      ["SIMON","Deux cents grammes… ça vous en fait une douzaine de tranches. Ça va ?"],
      ["FARIDA","C'est parfait. Il vient d'où, celui-là ?"],
      ["SIMON","Du Québec. Il y en a un autre moins cher, mais il est plus salé."],
      ["FARIDA","Je prends celui du Québec. Et il se garde combien de temps une fois ouvert ?"],
      ["SIMON","Trois jours, dans un contenant fermé. Pas plus."],
      ["FARIDA","Trois jours. Merci beaucoup."],
      ["SIMON","Ça fait cinq dollars quarante. Bonne journée !"],
    ]
  },
};
