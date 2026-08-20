const DIALOGUES = {
  prep: {
    label: "Dialogue — Je ne trouve pas",
    lines: [
      ["MARISOL","Excusez-moi, monsieur. Je cherche quelque chose."],
      ["ÉRIC","Oui ? Qu'est-ce que vous cherchez ?"],
      ["MARISOL","De la farine de maïs. Pour faire des tortillas."],
      ["ÉRIC","De la farine de maïs… Attendez. Vous avez regardé où ?"],
      ["MARISOL","Là-bas. Avec les autres farines. Il n'y en a pas."],
      ["ÉRIC","Ah, non. Elle n'est pas avec les farines. Elle est dans les produits du monde."],
      ["MARISOL","Les produits du monde ? Qu'est-ce que c'est ?"],
      ["ÉRIC","C'est une allée pour les produits d'autres pays. Allée douze, tout au fond."],
      ["MARISOL","Allée douze. Merci beaucoup."],
      ["ÉRIC","Si vous ne trouvez pas, revenez me voir. Je suis ici toute la journée."]
    ]
  },

  t1: {
    label: "Dialogue — Dans quelle allée ?",
    lines: [
      ["MARISOL","Excusez-moi. Je cherche l'huile."],
      ["ÉRIC","L'huile, c'est allée cinq."],
      ["MARISOL","Pardon ? Allée cinq ou allée quinze ?"],
      ["ÉRIC","Cinq. Un, deux, trois, quatre, cinq."],
      ["MARISOL","Ah, cinq. Et c'est où, l'allée cinq ?"],
      ["ÉRIC","Vous voyez le grand panneau blanc ? C'est juste en dessous."],
      ["MARISOL","D'accord. Et l'huile est en haut ou en bas ?"],
      ["ÉRIC","Au milieu. À côté du vinaigre."],
      ["MARISOL","Merci. Vous êtes gentil."],
      ["ÉRIC","Ça me fait plaisir."]
    ]
  },

  t2: {
    label: "Dialogue — La circulaire de la semaine",
    lines: [
      ["GINETTE","Marisol ! Vous magasinez ici aussi ?"],
      ["MARISOL","Bonjour, madame Ginette. Oui, mais c'est cher."],
      ["GINETTE","Vous regardez la circulaire avant de venir ?"],
      ["MARISOL","La circulaire ? Le papier dans la boîte aux lettres ?"],
      ["GINETTE","Oui. Elle arrive le mercredi. Elle montre les spéciaux de la semaine."],
      ["MARISOL","Je la jette. Je pensais que c'était de la publicité."],
      ["GINETTE","C'est de la publicité, mais elle est utile. Regardez : le poulet est à trois dollars la livre cette semaine."],
      ["MARISOL","Et la semaine prochaine ?"],
      ["GINETTE","La semaine prochaine, ce sera autre chose. Les spéciaux changent le jeudi."],
      ["MARISOL","Alors je dois acheter aujourd'hui."],
      ["GINETTE","Ou demain. Le spécial finit mercredi soir. C'est écrit en petit, en bas."]
    ]
  },

  t2b: {
    label: "Dialogue — Attention, c'est dangereux",
    lines: [
      ["MARISOL","Madame Ginette, je cherche un produit pour le plancher."],
      ["GINETTE","C'est dans l'allée des produits d'entretien. Mais faites attention."],
      ["MARISOL","Attention à quoi ?"],
      ["GINETTE","Regardez les petits dessins sur la bouteille. Celui-là veut dire « poison »."],
      ["MARISOL","Le dessin avec la tête de mort ?"],
      ["GINETTE","Oui. Et celui-là, la main avec le trou, ça veut dire que ça brûle la peau."],
      ["MARISOL","Alors je mets des gants ?"],
      ["GINETTE","Des gants, et vous ouvrez la fenêtre. Et surtout : vous ne mélangez jamais deux produits."],
      ["MARISOL","Pourquoi ?"],
      ["GINETTE","Parce que ça peut faire un gaz dangereux. C'est écrit sur la bouteille, mais personne ne le lit."]
    ]
  },

  t3: {
    label: "Dialogue — À la caisse",
    lines: [
      ["STÉPHANE","Bonjour ! Vous avez la carte de points ?"],
      ["MARISOL","La carte de points ? Non. C'est quoi ?"],
      ["STÉPHANE","C'est gratuit. Vous ramassez des points, et après vous avez des rabais."],
      ["MARISOL","Ah. Je peux avoir une carte ?"],
      ["STÉPHANE","Oui, je vous donne le formulaire. Vous avez des sacs ?"],
      ["MARISOL","Non. Je dois acheter des sacs ?"],
      ["STÉPHANE","Les sacs de plastique, on n'en donne plus. Les sacs réutilisables sont à deux dollars."],
      ["MARISOL","D'accord, un sac, s'il vous plaît."],
      ["STÉPHANE","Ça fait quarante-deux dollars et quinze. Débit ou crédit ?"],
      ["MARISOL","Débit. Pardon, vous pouvez répéter le montant ?"],
      ["STÉPHANE","Quarante-deux quinze. Quarante-deux dollars et quinze cents."]
    ]
  },

  t3b: {
    label: "Dialogue — Ce n'est pas le bon prix",
    lines: [
      ["MARISOL","Excusez-moi. Je regarde ma facture. Le poulet, c'est cinq dollars."],
      ["STÉPHANE","Oui, cinq dollars la livre."],
      ["MARISOL","Mais dans la circulaire, c'est trois dollars."],
      ["STÉPHANE","Vous avez la circulaire ?"],
      ["MARISOL","J'ai la photo sur mon téléphone."],
      ["STÉPHANE","Attendez, je regarde… Vous avez raison. Le spécial n'est pas passé."],
      ["MARISOL","Qu'est-ce qu'on fait ?"],
      ["STÉPHANE","Je vous rembourse la différence. Deux dollars la livre, trois livres : six dollars."],
      ["MARISOL","Merci. Je pensais que je me trompais."],
      ["STÉPHANE","Non, non. Vérifiez toujours votre facture. Ça arrive plus souvent qu'on pense."]
    ]
  },

  appli: {
    label: "Dialogue — Toute seule",
    lines: [
      ["MARISOL","Excusez-moi. Est-ce que vous travaillez ici ?"],
      ["ÉRIC","Oui. Je peux vous aider ?"],
      ["MARISOL","Je cherche le riz. Le grand sac, pas le petit."],
      ["ÉRIC","Allée huit, avec les pâtes. Les grands sacs sont en bas."],
      ["MARISOL","Merci. Et une dernière question : le sucre est en spécial cette semaine ?"],
      ["ÉRIC","Je pense que oui. Vous avez regardé la circulaire ?"],
      ["MARISOL","Oui, mais je veux être sûre. C'est deux pour cinq dollars ?"],
      ["ÉRIC","C'est ça. Deux sacs pour cinq dollars. Un seul sac, c'est trois dollars."],
      ["MARISOL","Alors je prends deux sacs. Merci beaucoup, monsieur."],
      ["ÉRIC","Bonne journée !"]
    ]
  },
};
