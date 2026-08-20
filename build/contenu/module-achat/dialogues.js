const DIALOGUES = {
  prep: {
    label: "Dialogue — Devant les trois laveuses",
    lines: [
      ["MARTIN","Bonjour ! Je peux vous aider ? Vous regardez les laveuses depuis un moment."],
      ["YIN","Bonjour. Oui, je cherche une laveuse, mais je ne sais pas laquelle choisir."],
      ["MARTIN","Vous avez quel espace chez vous ? C'est souvent ça qui décide en premier."],
      ["YIN","Un petit local, dans le sous-sol. Un mètre de large, à peu près."],
      ["MARTIN","Alors celle-là est trop large : elle fait soixante-seize centimètres avec la porte ouverte."],
      ["YIN","Et celle-ci ?"],
      ["MARTIN","Soixante-huit centimètres. Elle entre partout. C'est le modèle le plus vendu, justement pour ça."],
      ["YIN","Elle est bruyante ?"],
      ["MARTIN","Non, c'est une des plus silencieuses. Cinquante-deux décibels à l'essorage."],
      ["YIN","Cinquante-deux, c'est beaucoup ou peu ?"],
      ["MARTIN","C'est peu. Une conversation normale, c'est soixante. Vous ne l'entendrez pas de l'étage."],
      ["YIN","Et la troisième, là-bas ?"],
      ["MARTIN","Plus grande, plus chère, et beaucoup plus économe en eau. Elle vaut la peine si vous faites six brassées par semaine."],
      ["YIN","Nous en faisons trois. Je vais regarder les deux premières de plus près."],
    ]
  },

  t1: {
    label: "Dialogue — Ce modèle-ci ou celui-là ?",
    lines: [
      ["YIN","Quelle est la différence entre ce modèle-ci et celui-là ? Ils se ressemblent beaucoup."],
      ["MARTIN","Presque tout est pareil. Deux choses changent : la capacité et la consommation d'eau."],
      ["YIN","La capacité, ça veut dire quoi exactement ?"],
      ["MARTIN","Combien de linge entre dedans. Celui-ci prend quatre kilos et demi, celui-là cinq kilos et demi."],
      ["YIN","Un kilo de plus, ça change quoi pour nous ?"],
      ["MARTIN","Environ une brassée de moins par semaine, pour une famille de quatre."],
      ["YIN","Et l'eau ?"],
      ["MARTIN","Le modèle plus cher consomme trente litres de moins par brassée. Sur cinq ans, ça compense la différence de prix."],
      ["YIN","Ils sont garantis pareil ?"],
      ["MARTIN","Un an tous les deux, pièces et main-d'œuvre. La garantie prolongée est offerte sur les deux."],
      ["YIN","Celui-ci est en spécial jusqu'à quand ?"],
      ["MARTIN","Jusqu'à dimanche. Après, il remonte de cent dollars."],
    ]
  },

  t2: {
    label: "Dialogue — La garantie et la livraison",
    lines: [
      ["YIN","Qu'est-ce que la garantie couvre, au juste ?"],
      ["MARTIN","Un an, pièces et main-d'œuvre. Si l'appareil brise, on répare sans frais."],
      ["YIN","Et si c'est moi qui l'abîme ?"],
      ["MARTIN","Ça, ce n'est pas couvert. La garantie couvre les défauts de fabrication, pas les accidents."],
      ["YIN","Vous parliez d'une garantie prolongée."],
      ["MARTIN","Cent vingt dollars pour trois ans de plus. Elle couvre aussi le déplacement du technicien."],
      ["YIN","Je vais y penser. Pour le paiement, vous prenez quoi ?"],
      ["MARTIN","Comptant, débit, crédit. Ou en douze versements sans intérêt, si vous préférez."],
      ["YIN","Et la livraison ?"],
      ["MARTIN","Soixante dollars, ou gratuite au-dessus de mille dollars. On livre le mardi et le jeudi dans votre secteur."],
      ["YIN","Vous l'installez aussi ?"],
      ["MARTIN","L'installation est un service à part, quarante dollars. Les livreurs la montent, mais ils ne la branchent pas."],
      ["YIN","Alors je prendrai l'installation. Ce sera livré quand ?"],
      ["MARTIN","Jeudi prochain, entre huit heures et midi. On vous appellera la veille."],
    ]
  },

  t2b: {
    label: "Dialogue — La veille de la livraison",
    lines: [
      ["PATRICK","Bonjour, c'est pour la livraison de demain. Je vous confirme entre huit heures et midi."],
      ["YIN","Parfait. Est-ce que quelqu'un doit être là ?"],
      ["PATRICK","Oui, une personne majeure. On ne laisse pas l'appareil sans signature."],
      ["YIN","Il faut préparer quelque chose ?"],
      ["PATRICK","Dégagez le passage et mesurez la porte du sous-sol. Si elle fait moins de soixante-dix centimètres, appelez-nous avant."],
      ["YIN","Elle fait soixante-quinze. Ça va."],
      ["PATRICK","Bien. On monte l'appareil et on repart avec l'emballage. L'installation, c'est un autre technicien."],
      ["YIN","Il vient quand, lui ?"],
      ["PATRICK","L'après-midi, normalement. Il vous appellera en partant du magasin."],
      ["YIN","Et l'ancienne laveuse, vous la reprenez ?"],
      ["PATRICK","Si c'est noté sur le bon de livraison, oui. Sinon, il faut appeler le magasin aujourd'hui."],
    ]
  },

  t3: {
    label: "Dialogue — Avant le premier lavage",
    lines: [
      ["THÉRÈSE","Tu as reçu ta laveuse ? Tu as lu le mode d'emploi ?"],
      ["YIN","Je l'ai ouvert. Il fait quarante pages, en trois langues."],
      ["THÉRÈSE","Il n'y a que quatre pages à lire, en réalité. Le reste, ce sont les mêmes pages en anglais et en espagnol."],
      ["YIN","Lesquelles ?"],
      ["THÉRÈSE","L'installation, la première utilisation, les avertissements, et le tableau des problèmes."],
      ["YIN","Le tableau des problèmes ?"],
      ["THÉRÈSE","À la fin. Deux colonnes : le problème à gauche, quoi vérifier à droite. Ça évite bien des appels de service."],
      ["YIN","Et la première utilisation ?"],
      ["THÉRÈSE","On fait un cycle à vide, sans linge, avant tout. Ça enlève ce qui reste de l'usine."],
      ["YIN","Personne ne me l'avait dit."],
      ["THÉRÈSE","C'est écrit à la page trois. Personne ne la lit."],
      ["YIN","Et les boulons de transport, c'est quoi ?"],
      ["THÉRÈSE","Quatre boulons à l'arrière, qui bloquent le tambour pendant le transport. Si tu ne les enlèves pas, la machine saute."],
    ]
  },

  t3b: {
    label: "Dialogue — Le tableau des problèmes",
    lines: [
      ["YIN","Elle vibre beaucoup à l'essorage. J'ai regardé le tableau."],
      ["THÉRÈSE","Qu'est-ce qu'il dit ?"],
      ["YIN","Trois choses : vérifier les boulons de transport, vérifier que l'appareil est de niveau, répartir le linge."],
      ["THÉRÈSE","Tu as enlevé les boulons ?"],
      ["YIN","Oui, le technicien les a enlevés. Et le plancher est droit."],
      ["THÉRÈSE","Alors c'est le linge. Tu as mis quoi dedans ?"],
      ["YIN","Deux serviettes de bain, rien d'autre."],
      ["THÉRÈSE","C'est ça. Deux serviettes se collent d'un côté et le tambour tourne de travers. Ajoute des petites pièces."],
      ["YIN","Il fallait chercher dans le tableau, pas appeler le service."],
      ["THÉRÈSE","Neuf appels sur dix se règlent avec ce tableau. Et le déplacement du technicien coûte quatre-vingt-dix dollars."],
    ]
  },

  appli: {
    label: "Dialogue — Le réfrigérateur du sous-sol",
    lines: [
      ["YIN","Bonjour. Je cherche un petit réfrigérateur pour le sous-sol."],
      ["MARTIN","Bonjour. Vous avez quelles dimensions ? Hauteur et largeur."],
      ["YIN","Un mètre cinquante de haut, soixante centimètres de large, pas plus."],
      ["MARTIN","Celui-ci fait cent quarante-cinq sur cinquante-cinq. Il entre."],
      ["YIN","Il consomme beaucoup ?"],
      ["MARTIN","C'est un des plus économes de sa catégorie. Trois cents kilowattheures par année."],
      ["YIN","Et la garantie ?"],
      ["MARTIN","Un an complet, cinq ans sur le compresseur. C'est la pièce qui coûte cher."],
      ["YIN","La livraison est incluse ?"],
      ["MARTIN","À ce prix-là, non. Soixante dollars, ou vous le prenez avec vous : il entre dans une auto."],
      ["YIN","Je vais le prendre avec moi. Vous pouvez le sortir de la boîte ?"],
      ["MARTIN","On ne le déballe pas ici, mais on vous aide à le charger. Avancez votre auto à la porte trois."],
    ]
  },
};
