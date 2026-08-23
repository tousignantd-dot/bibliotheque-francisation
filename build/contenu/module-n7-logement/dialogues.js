const DIALOGUES = {
  // Quatre dialogues, volontairement longs : au niveau 7 la compétence porte
  // sur des discours étendus, et les deux intentions de la situation sont
  // toutes deux orales. Ils se travaillent en écoutes successives — une fois
  // pour le sujet, une fois pour les chiffres, une fois pour le détail.
  //
  // Quatre personnages, quatre timbres. SOKHNA parle dans les quatre ;
  // GÉRALD, JOSIANE et FARAH ne se rencontrent jamais.
  prep: {
    label: "Dialogue — L'enveloppe dans la porte",
    lines: [
      ["SOKHNA","Monsieur Lheureux ! Attendez, s'il vous plaît. J'ai trouvé une enveloppe coincée dans ma porte ce matin."],
      ["GÉRALD","C'est moi qui l'ai mise. Je fais le tour des six logements cette semaine."],
      ["SOKHNA","C'est un avis de renouvellement, si j'ai bien lu. Avec une augmentation de quatre-vingt-quatre dollars."],
      ["GÉRALD","Quatre-vingt-quatre. Le loyer passerait de neuf cent quarante à mille vingt-quatre à partir du premier juillet."],
      ["SOKHNA","Mille vingt-quatre. Ça fait sept ans que je suis ici, monsieur Lheureux, et je n'ai jamais payé une journée en retard."],
      ["GÉRALD","Je le sais, madame Diagne. Vous êtes ma meilleure locataire. Mais la taxe municipale a monté, l'assurance a monté, et le toit est à refaire l'an prochain."],
      ["SOKHNA","Je comprends que vos frais montent. Ce que je ne comprends pas, c'est le papier. Il y a une case « refuser » et une case « accepter », et une histoire de délai."],
      ["GÉRALD","Un mois. Vous avez un mois pour me répondre à partir du jour où vous avez reçu l'avis."],
      ["SOKHNA","Et si je ne réponds rien du tout ?"],
      ["GÉRALD","Si vous ne répondez rien, c'est accepté. Le bail se renouvelle au nouveau montant, et il n'y a plus rien à discuter."],
      ["SOKHNA","Ah bon. Donc le silence, ici, ce n'est pas neutre."],
      ["GÉRALD","Non. C'est un oui."],
      ["SOKHNA","Et si je refuse, vous me mettez dehors ?"],
      ["GÉRALD","Non plus. Ça ne marche pas comme ça. Si vous refusez, c'est à moi d'aller devant le Tribunal administratif du logement pour faire fixer le loyer, et j'ai un mois pour le faire. Si je ne le fais pas, vous restez à neuf cent quarante."],
      ["SOKHNA","Vous m'expliquez ça très calmement, pour quelqu'un qui demande quatre-vingt-quatre dollars de plus."],
      ["GÉRALD","Parce que je préfère m'entendre avec vous que d'aller m'asseoir dans une salle d'audience. Faites-moi une proposition, madame Diagne. Je vous écoute."],
      ["SOKHNA","Laissez-moi une semaine. Je veux lire le papier au complet, et je veux aussi vérifier quelque chose d'autre."],
      ["GÉRALD","Quelque chose d'autre ?"],
      ["SOKHNA","Ma sœur me répète depuis deux ans que je paie pour un logement qui ne sera jamais à moi. Peut-être qu'elle a raison. Peut-être que non. Je vais aller le savoir."],
      ["GÉRALD","Acheter ? À Saint-Hyacinthe, aujourd'hui ? Bonne chance. Revenez me voir avant le quinze, de toute façon."]
    ]
  },

  t1: {
    label: "Dialogue — La contre-proposition",
    lines: [
      ["SOKHNA","Merci de me recevoir dans la cuisine, monsieur Lheureux. C'est plus simple que dans l'escalier."],
      ["GÉRALD","Vous avez lu le papier ?"],
      ["SOKHNA","Trois fois. Et j'ai appelé le service de renseignements du Tribunal, aussi. J'aimerais vous faire une proposition, si vous permettez."],
      ["GÉRALD","Allez-y."],
      ["SOKHNA","Ce qui me dérange, ce n'est pas que le loyer monte. C'est qu'il monte de quatre-vingt-quatre dollars d'un coup, la même année où la fenêtre de la chambre ne ferme plus."],
      ["GÉRALD","La fenêtre de la chambre. C'est la première fois que j'en entends parler."],
      ["SOKHNA","Je vous l'ai dit en février, au téléphone. Mais je ne vous l'ai jamais écrit, et c'est mon erreur."],
      ["GÉRALD","Bon. Admettons. Qu'est-ce que vous proposez ?"],
      ["SOKHNA","Je proposerais quarante-cinq dollars au lieu de quatre-vingt-quatre, et la fenêtre changée avant l'hiver. Si la fenêtre est changée avant le premier novembre, j'accepte les quarante-cinq sans discuter."],
      ["GÉRALD","Quarante-cinq, ça ne couvre même pas la taxe."],
      ["SOKHNA","Peut-être. Mais une fenêtre neuve, c'est votre immeuble qui la garde, pas moi. Moi, je pars un jour ; elle reste."],
      ["GÉRALD","Ça, c'est vrai."],
      ["SOKHNA","Et il y a autre chose que j'aimerais vous demander. Est-ce que vous accepteriez de me le mettre par écrit ? Deux lignes, avec la date, et vos initiales."],
      ["GÉRALD","Vous ne me faites pas confiance ?"],
      ["SOKHNA","Je vous fais confiance. C'est à ma mémoire que je ne fais pas confiance, et à la vôtre non plus, avec six logements sur les bras. Un papier ne fâche personne."],
      ["GÉRALD","Vous avez appris ça où, ces façons de parler ?"],
      ["SOKHNA","À mon travail. Quand une famille demande quelque chose pour un résident, on l'écrit. Sinon, dans trois mois, personne ne se souvient de rien."],
      ["GÉRALD","Soixante. Soixante dollars, et je regarde la fenêtre au mois de septembre. Je ne promets pas de la changer, je promets de la regarder."],
      ["SOKHNA","Cinquante-cinq, et vous la regardez avec un vitrier, pas tout seul depuis la ruelle."],
      ["GÉRALD","Vous êtes dure en affaires, madame Diagne."],
      ["SOKHNA","Je suis polie et je suis précise. Ce n'est pas la même chose que dure."],
      ["GÉRALD","Cinquante-cinq. Je vous écris les deux lignes ce soir. Et si le vitrier dit que la fenêtre est correcte ?"],
      ["SOKHNA","Alors elle est correcte, et je n'en reparle plus. Je ne demande pas d'avoir raison, monsieur Lheureux. Je demande qu'on regarde."]
    ]
  },

  t2: {
    label: "Dialogue — La visite du condo de la rue Sainte-Anne",
    lines: [
      ["JOSIANE","Madame Diagne ? Josiane Bourbonnais. On s'est parlé au téléphone hier."],
      ["SOKHNA","Bonjour. Merci de m'avoir gardé une visite un samedi matin."],
      ["JOSIANE","Ça me fait plaisir. Avant qu'on monte, il y a une chose que je dois vous dire, et je la dis à tout le monde : je suis la courtière du vendeur. J'ai un contrat de courtage avec lui."],
      ["SOKHNA","C'est-à-dire ?"],
      ["JOSIANE","C'est-à-dire que je travaille pour lui. Je ne vous représente pas. Je dois vous traiter équitablement et vous donner l'information de façon objective, mais si vous voulez quelqu'un qui défend vos intérêts à vous, il vous faut votre propre courtier."],
      ["SOKHNA","Et ça me coûterait combien, mon propre courtier ?"],
      ["JOSIANE","Dans la plupart des transactions résidentielles, la rétribution est payée par le vendeur. Ce que je ne peux pas faire, moi, c'est vous réclamer quoi que ce soit : ma rétribution est fixée dans le contrat que j'ai signé avec le vendeur."],
      ["SOKHNA","D'accord. Ça au moins, c'est clair. Montons."],
      ["JOSIANE","Alors voilà. Quatre pièces et demie, deuxième étage, construit en mil neuf cent quatre-vingt-douze. Deux cent soixante-quinze mille, et les frais de copropriété sont de cent quatre-vingt-dix dollars par mois."],
      ["SOKHNA","Cent quatre-vingt-dix par mois. Ça comprend quoi, exactement ?"],
      ["JOSIANE","L'assurance de l'immeuble, l'entretien des parties communes, le déneigement, et une part qui va au fonds de prévoyance."],
      ["SOKHNA","Le fonds de prévoyance, c'est l'argent qu'on met de côté pour les gros travaux ?"],
      ["JOSIANE","Exactement. Et c'est la question la plus importante que vous pouvez poser dans un condo. Demandez toujours combien il y a dans le fonds, et depuis quand."],
      ["SOKHNA","Alors je la pose : combien il y a dans le fonds, et depuis quand ?"],
      ["JOSIANE","Je vais vous chercher le procès-verbal de la dernière assemblée. De mémoire, il y a autour de quarante mille, et le toit a été refait en deux mille vingt-deux."],
      ["SOKHNA","Une autre question. Le voisin du dessus, celui qu'on entend marcher, il est là depuis longtemps ?"],
      ["JOSIANE","Ça, je ne le sais pas, et je ne vais pas l'inventer. Je vais me renseigner et je vous rappelle."],
      ["SOKHNA","J'apprécie que vous disiez « je ne sais pas ». Duquel des deux stationnements est-ce qu'on parle, sur la fiche ?"],
      ["JOSIANE","Du numéro huit, celui de gauche. Il est inclus. Le cabanon, lui, ne l'est pas : il appartient au voisin du rez-de-chaussée."],
      ["SOKHNA","Et pour la suite, si jamais je me décide, ça se passe comment ?"],
      ["JOSIANE","Vous déposez une promesse d'achat. C'est un document sérieux : une fois qu'elle est acceptée par les deux parties, vous êtes engagée. On y écrit le prix, la date d'occupation, ce qui est inclus, et surtout les conditions."],
      ["SOKHNA","Quelles conditions ?"],
      ["JOSIANE","Les deux habituelles : le financement, et l'inspection du bâtiment. Elles vous protègent. Et avant de faire quoi que ce soit, allez chercher une préautorisation à votre institution financière — vous saurez de quel montant on parle au lieu de rêver."],
      ["SOKHNA","Une préautorisation. Bon. Je vais commencer par là, d'abord."]
    ]
  },

  t3: {
    label: "Dialogue — À la caisse, avec la conseillère",
    lines: [
      ["FARAH","Madame Diagne, entrez. Farah Zaoui, conseillère hypothécaire. Vous m'avez apporté vos papiers ?"],
      ["SOKHNA","Tout ce que vous m'aviez demandé : mes deux derniers relevés, mes talons de paie, et le relevé de mon compte d'épargne."],
      ["FARAH","Parfait. Commençons par la question que tout le monde pose en dernier : combien avez-vous de côté ?"],
      ["SOKHNA","Dix-neuf mille huit cents."],
      ["FARAH","Bon. Pour une propriété de deux cent soixante-quinze mille, la mise de fonds minimale est de cinq pour cent, parce qu'on est sous cinq cent mille. Cinq pour cent de deux cent soixante-quinze mille, ça fait treize mille sept cent cinquante."],
      ["SOKHNA","Donc j'ai assez ?"],
      ["FARAH","Vous avez assez pour la mise de fonds minimale, oui. Mais attention : sous vingt pour cent de mise de fonds, votre prêt doit être assuré. C'est la loi au Canada, et la prime d'assurance s'ajoute à votre prêt."],
      ["SOKHNA","Donc je paierais plus cher chaque mois à cause de ça."],
      ["FARAH","Un peu plus cher, oui. Et il faut aussi garder de l'argent pour les frais : le notaire, l'inspection, les droits de mutation."],
      ["SOKHNA","Les droits de mutation, c'est la taxe de bienvenue ?"],
      ["FARAH","C'est le même impôt, oui. C'est la municipalité qui le perçoit, et c'est le nouveau propriétaire qui le paie, quelques mois après l'achat. Bien du monde l'oublie et reçoit un compte qui fait mal."],
      ["SOKHNA","Et le notaire, il est obligatoire ?"],
      ["FARAH","Pour l'acte hypothécaire, oui, obligatoire. C'est lui aussi qui fait l'examen des titres, c'est-à-dire qu'il remonte les anciens actes pour vérifier que la personne qui vous vend a bien le droit de vous vendre."],
      ["SOKHNA","Bon. Et vous, qu'est-ce que vous me donnez aujourd'hui ?"],
      ["FARAH","Une préautorisation. Ce n'est pas un prêt : c'est une évaluation de ce que vous pouvez emprunter, valable un temps limité, à un taux qu'on vous garde. Ça vous dit dans quel prix chercher."],
      ["SOKHNA","Et si je fais une promesse d'achat avant d'avoir la réponse définitive ?"],
      ["FARAH","C'est justement à ça que sert la condition de financement. Vous écrivez dans votre promesse que l'achat est conditionnel à l'obtention de votre prêt, avec un nombre de jours pour l'obtenir. Prévoyez large — vingt et un jours, ce n'est pas trop."],
      ["SOKHNA","Et l'inspection ?"],
      ["FARAH","Elle n'est pas obligatoire par la loi. Mais renoncer à une inspection pour économiser six cents dollars sur un achat de deux cent soixante-quinze mille, ce serait une drôle d'économie. Faites-la, et faites-la faire par un professionnel."],
      ["SOKHNA","Madame Zaoui, je vais vous poser la question autrement. À ma place, vous achèteriez ?"],
      ["FARAH","Je ne peux pas répondre à ça, et personne ne devrait répondre à ça à votre place. Ce que je peux faire, c'est vous donner les deux chiffres et vous laisser les comparer."],
      ["SOKHNA","Allez-y."],
      ["FARAH","Locataire, à mille vingt-quatre dollars par mois — ou neuf cent quatre-vingt-quinze si votre entente tient —, vous n'avez rien d'autre à payer et rien qui vous appartienne. Propriétaire, en comptant le prêt, les frais de copropriété, les taxes et l'assurance, vous seriez autour de mille six cents par mois, et une partie de cet argent-là revient dans votre poche chaque mois."],
      ["SOKHNA","Six cents dollars de plus par mois."],
      ["FARAH","Six cents de plus, et une décision qui ne se défait pas en trente jours. Prenez le temps. Écrivez les deux colonnes sur une feuille et revenez me voir avec vos questions."]
    ]
  },
};
