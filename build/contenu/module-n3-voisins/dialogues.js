const DIALOGUES = {
  prep: {
    label: "Dialogue — C'est vous, le nouveau du troisième ?",
    lines: [
      ["MANON","Bonjour ! C'est vous, le nouveau du troisième ?"],
      ["RACHID","Oui, c'est moi. Rachid Belkacem. Bonjour, madame."],
      ["MANON","Manon Lachapelle, du deuxième. Bienvenue dans l'immeuble."],
      ["RACHID","Merci beaucoup. Nous sommes arrivés il y a trois semaines."],
      ["MANON","Nous ? Vous êtes plusieurs, chez vous ?"],
      ["RACHID","Ma femme, mon petit garçon et moi. Il a quatre ans."],
      ["MANON","Quatre ans ! C'est le bel âge. Et vous travaillez dans le coin ?"],
      ["RACHID","Je suis électricien. Je pars tôt le matin, vers six heures."],
      ["MANON","Moi, je suis à la retraite. Je suis ici depuis onze ans."],
      ["LEILA","Rachid, tu viens ? La porte est restée ouverte en haut."],
      ["RACHID","Une minute. Madame Lachapelle, je vous présente ma sœur, Leïla."],
      ["LEILA","Bonjour ! Enchantée."],
      ["MANON","Enchantée. Vous habitez ici aussi ?"],
      ["LEILA","Non, j'habite à Longueuil. Je viens donner un coup de main."],
      ["MANON","C'est gentil. Si vous avez besoin de quelque chose, je suis au 2B."],
      ["RACHID","Merci, c'est noté. Bonne journée, madame Lachapelle."],
    ]
  },

  t1: {
    label: "Dialogue — Est-ce que je peux mettre mon vélo dans la remise ?",
    lines: [
      ["RACHID","Madame Lachapelle ? Excusez-moi de vous déranger."],
      ["MANON","Pas du tout. Entrez une minute, il fait froid dans l'escalier."],
      ["RACHID","Merci. Mon vélo dort dans le corridor et il gêne tout le monde."],
      ["MANON","Ah, je l'ai vu. Il prend pas mal de place devant la porte."],
      ["RACHID","Est-ce que je peux le mettre dans la remise, en arrière ?"],
      ["MANON","Bien sûr, allez-y. Il y a de la place au fond."],
      ["RACHID","Est-ce qu'il faut demander à quelqu'un d'autre ?"],
      ["MANON","Le concierge a la clé. Monsieur Nadeau, au rez-de-chaussée."],
      ["RACHID","Est-ce que je pourrais l'accrocher au mur ?"],
      ["MANON","Oui, accrochez-le au mur du fond. La tondeuse doit passer."],
      ["RACHID","D'accord. Et l'hiver, est-ce qu'on le laisse là ?"],
      ["MANON","Vous pouvez le laisser toute l'année. Personne n'y touche."],
      ["RACHID","Une dernière chose : la rampe de l'escalier, en bas ?"],
      ["MANON","Je préfère que non. C'est la sortie de secours, il faut la garder libre."],
      ["RACHID","Je comprends. Je vais voir monsieur Nadeau ce soir."],
      ["MANON","Faites ça. Et dites-lui que je vous ai donné la permission."],
    ]
  },

  t2: {
    label: "Dialogue — Venez prendre un café samedi",
    lines: [
      ["RACHID","Madame Lachapelle, vous avez deux minutes ?"],
      ["MANON","Oui, oui. Qu'est-ce qui se passe ?"],
      ["RACHID","Vous m'avez aidé avec mes boîtes. Je voudrais vous remercier."],
      ["MANON","Ce n'était rien, voyons."],
      ["RACHID","On fait un petit café chez nous. Est-ce que vous voulez venir ?"],
      ["MANON","Avec plaisir. C'est quand ?"],
      ["RACHID","Samedi, à deux heures. Chez nous, au 3A."],
      ["MANON","Samedi, deux heures. Je vais l'écrire sur mon calendrier."],
      ["RACHID","Ma sœur va faire des gâteaux. Elle cuisine très bien."],
      ["MANON","Est-ce que j'apporte quelque chose ?"],
      ["RACHID","Apportez seulement votre bonne humeur."],
      ["MANON","Ah non, je vais apporter mes biscuits. J'insiste."],
      ["LEILA","Bonjour madame ! Alors, vous venez samedi ?"],
      ["MANON","Je viens, oui. Dites donc, elle est belle, votre porte repeinte !"],
      ["LEILA","Merci ! C'est mon frère qui l'a faite dimanche."],
      ["MANON","Il a du talent. Bon, à samedi, et merci d'avoir pensé à moi."],
    ]
  },

  t3: {
    label: "Dialogue — Il est comment, votre chat ?",
    lines: [
      ["MANON","Monsieur Belkacem ! Vous avez vu mon affiche dans l'entrée ?"],
      ["RACHID","L'affiche pour le chat ? Oui, ce matin. Il est parti quand ?"],
      ["MANON","Avant-hier soir. Il n'est jamais parti aussi longtemps."],
      ["RACHID","Il est comment ? J'ai vu un chat dans la ruelle hier."],
      ["MANON","Il est roux, assez gros, avec une tache blanche sous le menton."],
      ["RACHID","Le chat d'hier était roux, oui. Il avait un collier."],
      ["MANON","Un collier bleu ? Caramel porte un collier bleu, sans médaille."],
      ["RACHID","Bleu, je pense. Il était un peu peureux, il s'est sauvé."],
      ["MANON","C'est lui ! Il est très peureux avec les gens qu'il ne connaît pas."],
      ["RACHID","Il était derrière le garage vert, au bout de la ruelle."],
      ["MANON","Merci ! Je vais y aller tout de suite avec sa nourriture."],
      ["RACHID","Attendez, j'ai trouvé autre chose. Ces clés-là, dans l'escalier."],
      ["MANON","Montrez-moi. Un trousseau avec trois clés et un petit ourson ?"],
      ["RACHID","Oui, un ourson en tissu, un peu usé. Elles sont à qui ?"],
      ["MANON","À la dame du premier. Grande, cheveux gris courts, lunettes rouges."],
      ["RACHID","Je vais les lui remettre ce soir. Bonne chance pour Caramel !"],
    ]
  },

  appli: {
    label: "Dialogue — Ça s'est bien passé, votre samedi ?",
    lines: [
      ["MANON","Alors, il était bon, ce café de samedi ?"],
      ["RACHID","Très bon. Six voisins sont venus. Même monsieur Nadeau."],
      ["MANON","Et vos gâteaux ! Je me suis resservie deux fois."],
      ["RACHID","Leïla était contente. Personne n'avait rien laissé dans l'assiette."],
      ["MANON","Vous voyez ? Il fallait juste inviter."],
      ["RACHID","Oui. Avant, je disais bonjour et je montais tout de suite."],
      ["MANON","Et Caramel dort sur mon fauteuil depuis mercredi soir."],
      ["RACHID","Tant mieux. Merci encore pour la remise, madame Lachapelle."],
    ]
  },
};
