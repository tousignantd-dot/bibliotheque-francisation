const DIALOGUES = {
  prep: {
    label: "Dialogue — Je cherche un manteau",
    lines: [
      ["FARIDA","Bonjour, madame. Je cherche un manteau."],
      ["JOCELYNE","Bonjour ! Un manteau pour l'automne ou pour l'hiver ?"],
      ["FARIDA","Pour l'hiver. C'est mon premier hiver ici."],
      ["JOCELYNE","Ah, bienvenue ! Alors il vous faut un manteau chaud. Vous voulez quelle couleur ?"],
      ["FARIDA","Je ne sais pas. Bleu, peut-être. Ou noir."],
      ["JOCELYNE","Bleu pâle ou bleu foncé ?"],
      ["FARIDA","Pardon ? Pâle, foncé… Qu'est-ce que ça veut dire ?"],
      ["JOCELYNE","Pâle, c'est clair, comme le ciel. Foncé, c'est presque noir."],
      ["FARIDA","Alors foncé. Le pâle, ça salit vite."],
      ["JOCELYNE","Vous avez raison. Regardez : celui-ci est bleu foncé, en nylon. Et celui-là est noir, avec des rayures."],
      ["FARIDA","Rayé ? Non, merci. Je préfère uni."],
      ["JOCELYNE","Uni et foncé. Très bien. Je vais vous montrer trois modèles."]
    ]
  },

  t1: {
    label: "Dialogue — Quelle taille ?",
    lines: [
      ["JOCELYNE","Vous portez quelle taille ?"],
      ["FARIDA","Je ne sais pas. Dans mon pays, c'est un autre système."],
      ["JOCELYNE","Ici, c'est petit, moyen ou grand. Sur l'étiquette : P, M ou G."],
      ["FARIDA","Je pense que je suis moyenne."],
      ["JOCELYNE","Voici un moyen bleu foncé. Vous voulez l'essayer ?"],
      ["FARIDA","Oui, s'il vous plaît. Où est la cabine ?"],
      ["JOCELYNE","Au fond, à droite, derrière les chandails."],
      ["FARIDA","Merci… Madame ? Le moyen est trop serré aux épaules."],
      ["JOCELYNE","Trop serré ? Alors essayez le grand. Attendez, je le décroche du cintre."],
      ["FARIDA","Le grand est parfait. Mais les manches sont un peu longues."],
      ["JOCELYNE","Un peu longues, ce n'est pas grave l'hiver. Vous garderez vos mains au chaud."],
      ["FARIDA","C'est vrai. Je prends le grand."]
    ]
  },

  t2: {
    label: "Dialogue — Lequel est le moins cher ?",
    lines: [
      ["FARIDA","Excusez-moi, monsieur. Je regarde les bottes."],
      ["SAMIR","Oui ? Pour l'hiver aussi ?"],
      ["FARIDA","Oui. Celles-ci sont à quatre-vingt-dix-neuf dollars. Et celles-là ?"],
      ["SAMIR","Celles-là sont à cent trente dollars, mais elles sont en liquidation. Regardez l'étiquette."],
      ["FARIDA","Il y a deux prix. Je ne comprends pas."],
      ["SAMIR","Le premier prix, c'est le prix régulier : cent trente. Le deuxième, c'est le prix d'aujourd'hui : soixante-cinq."],
      ["FARIDA","Soixante-cinq ? Alors elles sont moins chères que les autres !"],
      ["SAMIR","Beaucoup moins chères. C'est cinquante pour cent de rabais."],
      ["FARIDA","Et elles sont aussi chaudes ?"],
      ["SAMIR","Elles sont même plus chaudes. Elles sont doublées en laine."],
      ["FARIDA","Alors pourquoi elles sont en liquidation ?"],
      ["SAMIR","Il reste seulement deux pointures. Vous avez de la chance : le sept est là."]
    ]
  },

  t2b: {
    label: "Dialogue — Trente pour cent de rabais",
    lines: [
      ["FARIDA","Madame Jocelyne, il y a une grande affiche : trente pour cent de rabais."],
      ["JOCELYNE","Oui, sur les chandails seulement. Pas sur les manteaux."],
      ["FARIDA","Comment je fais pour savoir ?"],
      ["JOCELYNE","Regardez la petite étiquette. Si elle est rouge, l'article est en rabais."],
      ["FARIDA","Celle-ci est rouge. Trente-neuf dollars quatre-vingt-dix-neuf."],
      ["JOCELYNE","Trente-neuf quatre-vingt-dix-neuf, c'est le prix régulier. Avec le rabais, ça fait environ vingt-huit dollars."],
      ["FARIDA","Vous calculez dans votre tête ?"],
      ["JOCELYNE","Un peu. Mais le vrai prix apparaît à la caisse. C'est là qu'il faut vérifier."],
      ["FARIDA","Et si ce n'est pas le bon prix ?"],
      ["JOCELYNE","Vous le dites tout de suite. On corrige, ça arrive souvent."]
    ]
  },

  t3: {
    label: "Dialogue — Qu'est-ce que ça veut dire ?",
    lines: [
      ["FARIDA","Madame, il y a une petite étiquette dans le col. Avec des dessins."],
      ["JOCELYNE","C'est l'étiquette d'entretien. Elle dit comment laver le vêtement."],
      ["FARIDA","Le premier dessin, c'est un petit bassin avec de l'eau."],
      ["JOCELYNE","Ça veut dire : laver à la machine. Le chiffre dedans, c'est la température."],
      ["FARIDA","Il y a écrit trente."],
      ["JOCELYNE","Trente degrés. De l'eau froide, donc. À l'eau chaude, la laine rapetisse."],
      ["FARIDA","Et le carré avec un rond dedans, barré ?"],
      ["JOCELYNE","Ne pas mettre à la sécheuse. Ce vêtement sèche à l'air."],
      ["FARIDA","Et le triangle barré ?"],
      ["JOCELYNE","Ne pas javelliser. Le javellisant ferait des taches jaunes."],
      ["FARIDA","C'est compliqué…"],
      ["JOCELYNE","Non : un dessin barré, c'est toujours « ne pas faire ». Gardez ça et vous comprendrez tout."]
    ]
  },

  t3b: {
    label: "Dialogue — À la caisse",
    lines: [
      ["KEVIN","Bonjour ! Vous avez trouvé tout ce que vous cherchiez ?"],
      ["FARIDA","Oui, merci. Un manteau et des bottes."],
      ["KEVIN","Le manteau grand, et les bottes en liquidation. Ça fait cent soixante-quatre dollars et quatre-vingt-quinze."],
      ["FARIDA","Pardon, vous pouvez répéter le montant ?"],
      ["KEVIN","Cent soixante-quatre quatre-vingt-quinze. Cent soixante-quatre dollars et quatre-vingt-quinze cents."],
      ["FARIDA","D'accord. Attendez… les bottes, c'est bien soixante-cinq ?"],
      ["KEVIN","Je regarde… oui, soixante-cinq. La liquidation est passée."],
      ["FARIDA","Parfait. Je paie avec ma carte de débit."],
      ["KEVIN","Insérez votre carte, s'il vous plaît. Vous voulez la facture dans le sac ?"],
      ["FARIDA","Non, je la garde dans ma poche."],
      ["KEVIN","Bonne idée. Gardez-la : c'est elle qui prouve le prix que vous avez payé."],
      ["FARIDA","Merci. Bonne journée !"]
    ]
  },

  appli: {
    label: "Dialogue — Toute seule",
    lines: [
      ["FARIDA","Bonjour. Je cherche une tuque et des mitaines."],
      ["SAMIR","Les tuques sont ici, à droite. De quelle couleur ?"],
      ["FARIDA","Gris foncé, si vous avez. Uni, pas rayé."],
      ["SAMIR","Gris foncé… voici. Elle est en laine."],
      ["FARIDA","Elle est à combien ?"],
      ["SAMIR","Vingt-deux dollars. Mais celle-là, en acrylique, est à quatorze."],
      ["FARIDA","Alors celle-ci est plus chère que celle-là. La différence, c'est quoi ?"],
      ["SAMIR","La laine est plus chaude, mais elle pique un peu. L'acrylique est plus douce."],
      ["FARIDA","Je prends la laine. J'ai plus besoin de chaleur que de douceur."],
      ["SAMIR","Bon choix pour janvier. Les mitaines sont juste à côté."]
    ]
  },
};
