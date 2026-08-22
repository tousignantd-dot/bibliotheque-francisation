const DIALOGUES = {
  // Quatre dialogues, un par section. Au niveau 6, ils font dix-huit à vingt
  // répliques : le cours vise « des discours détaillés et structurés », et
  // une explication technique ne se découpe pas en saynètes de trois lignes.
  //
  // Cinq personnages, quatre voix, aucun croisement possible :
  //   prep  DOÏNA + LÉANDRE            t1  DOÏNA + FERNAND
  //   t2    DOÏNA + KETTLY             t3  DOÏNA + FERNAND + KETTLY + RÉJEAN
  // LÉANDRE et RÉJEAN partagent le timbre « narrateur » et ne se rencontrent
  // jamais ; KETTLY prend la voix « enseignante », ralentie à 0,85, parce que
  // c'est elle qui énonce ce que l'élève doit pouvoir redire.

  prep: {
    label: "Dialogue — Par où ça commence, un chantier",
    lines: [
      ["DOÏNA", "Léandre ! Tu as deux minutes ? Je voudrais te demander quelque chose."],
      ["LÉANDRE", "Prends-en cinq, je ne fais rien de mon avant-midi. C'est pour ton sous-sol ?"],
      ["DOÏNA", "Oui. Ma mère arrive de Roumanie au mois de mai. On voudrait lui aménager le sous-sol : une chambre, une petite salle de bain, une cuisinette."],
      ["LÉANDRE", "C'est exactement ce qu'on a fait l'an passé, de l'autre bord de la rue. Je peux te dire une chose : ce n'est pas les travaux qui sont difficiles, c'est ce qui vient avant."],
      ["DOÏNA", "Comment ça, ce qui vient avant ? On appelle quelqu'un, il vient, il donne un prix, non ?"],
      ["LÉANDRE", "Si tu fais ça, tu vas payer deux fois. Nous autres, on a commencé par une inspection. Une inspectrice en bâtiment est venue, elle a passé trois heures dans la maison, et elle nous a remis un rapport."],
      ["DOÏNA", "Un rapport pour quoi faire ? On voit bien qu'il n'y a rien de cassé."],
      ["LÉANDRE", "On voit ce qui est visible. Elle, elle regarde la fondation, l'humidité, la pente du terrain, le drain. Chez nous, elle a trouvé une fissure derrière une étagère qu'on n'avait jamais tassée."],
      ["DOÏNA", "Ah bon. Et ensuite ?"],
      ["LÉANDRE", "Ensuite, tu appelles un entrepreneur général. Lui, il coordonne les corps de métier : le maçon, le plombier, l'électricien, le poseur de gypse. Tu n'as pas à les appeler un par un."],
      ["DOÏNA", "Et il donne son prix comme ça, en regardant ?"],
      ["LÉANDRE", "Non. Il te fait une soumission écrite. Une vraie, détaillée, ligne par ligne, avec ce qui est inclus et ce qui ne l'est pas. Une soumission écrite au dos d'une facture, ça ne vaut rien le jour où vous n'êtes plus d'accord."],
      ["DOÏNA", "Marius va me dire qu'on peut faire une partie nous-mêmes."],
      ["LÉANDRE", "Peut-être. Mais tout ce qui touche à la plomberie et à l'électricité, laisse faire ça à des gens de métier. Et vérifie la licence de ton entrepreneur : au Québec, celui qui exécute des travaux de construction pour quelqu'un d'autre doit avoir une licence de la Régie du bâtiment."],
      ["DOÏNA", "Ça se vérifie où, une licence ?"],
      ["LÉANDRE", "Dans le registre de la Régie. C'est public, ça se consulte en ligne, et ça prend deux minutes. Deux minutes, Doïna, avant de signer pour trente mille piastres."],
      ["DOÏNA", "Trente mille. Tu me fais peur."],
      ["LÉANDRE", "Je te dis les vrais chiffres, c'est tout. Et il y a le permis : chez nous, la ville en demandait un. Ça dépend de la municipalité et du genre de travaux — tu appelles la tienne, tu ne te fies pas à ce que le voisin a eu."],
      ["DOÏNA", "Donc : une inspection, une soumission écrite, une licence à vérifier, un permis à demander."],
      ["LÉANDRE", "Et une question à te poser chaque fois que tu ne comprends pas un mot. C'est celle-là qui sauve le plus d'argent."],
    ]
  },

  t1: {
    label: "Dialogue — Ce que l'entrepreneur a trouvé au sous-sol",
    lines: [
      ["FERNAND", "Bon. Madame Petrescu, je viens de passer une heure en bas et j'ai fait le tour du terrain. Je vais vous expliquer ce que j'ai trouvé, et après vous poserez vos questions."],
      ["DOÏNA", "Allez-y. Je vous préviens, je vais vous arrêter souvent."],
      ["FERNAND", "Arrêtez-moi tant que vous voulez. Premièrement, la fissure. Elle est dans le mur de fondation, du côté nord, et elle monte en biais sur à peu près un mètre."],
      ["DOÏNA", "Elle est apparue quand ? On a acheté la maison il y a deux ans."],
      ["FERNAND", "Elle s'était ouverte bien avant que vous achetiez. Une fissure comme celle-là, ça travaille pendant des années. Votre inspectrice l'avait notée dans son rapport, d'ailleurs."],
      ["DOÏNA", "Elle l'avait notée, oui. Je l'ai relu hier soir. Mais je n'ai pas compris la cause."],
      ["FERNAND", "La cause est dehors. Venez à la fenêtre. Vous voyez la descente de gouttière, là, au coin ? Elle se vide à trente centimètres du mur."],
      ["DOÏNA", "Et c'est un problème ?"],
      ["FERNAND", "C'en est un, oui. Chaque grosse pluie, vous envoyez des centaines de litres d'eau directement contre votre fondation. Le sol se gorge, il pousse sur le mur, et le mur finit par fendre."],
      ["DOÏNA", "Alors ce n'est pas la fissure, le vrai problème."],
      ["FERNAND", "Vous venez de dire la chose la plus importante de la matinée. La fissure, c'est le résultat. Si je la répare sans toucher au reste, elle revient dans trois ans, et vous me rappelez."],
      ["DOÏNA", "Donc on fait quoi, dans l'ordre ?"],
      ["FERNAND", "Dans l'ordre : on rallonge les descentes de gouttière pour éloigner l'eau, on refait la pente du terrain sur deux mètres autour de la maison, et seulement après, on fait injecter la fissure."],
      ["DOÏNA", "Vous dites « on fait injecter ». Ce n'est pas vous qui le faites ?"],
      ["FERNAND", "Non. L'injection, je la fais faire par un spécialiste : ça se fait sous pression, avec un produit qui prend en quelques minutes. Moi, je coordonne, je ne fais pas tout de mes mains."],
      ["DOÏNA", "Et après l'injection, on peut commencer le sous-sol ?"],
      ["FERNAND", "Pas tout de suite. On laisse sécher. Comptez trois ou quatre semaines avec un déshumidificateur avant de refermer les murs. Si vous isolez sur de l'humidité, vous faites pousser de la moisissure derrière votre gypse neuf."],
      ["DOÏNA", "Quatre semaines de plus. Ma mère arrive le 12 mai."],
      ["FERNAND", "Je le sais, vous me l'avez dit deux fois. Ça rentre, mais il faut commencer maintenant, pas en février. Et j'ai besoin d'une réponse sur la soumission avant le 15."],
      ["DOÏNA", "Vous me la remettez quand, cette soumission ?"],
      ["FERNAND", "Jeudi, par courriel, détaillée ligne par ligne. Vous la lirez, vous m'appellerez, et là vous aurez le droit de me poser trente questions."],
    ]
  },

  t2: {
    label: "Dialogue — Deux papiers qui ne disent pas la même chose",
    lines: [
      ["DOÏNA", "Madame Alcindor, merci de me rappeler. J'ai votre rapport devant moi et j'ai la soumission de monsieur Trudelle à côté. Je n'arrive pas à les faire concorder."],
      ["KETTLY", "C'est normal, et c'est même sain. Ces deux papiers ne servent pas à la même chose. Le mien décrit ce qui est ; le sien décrit ce qui sera fait."],
      ["DOÏNA", "D'accord. Mais commençons par le vôtre. Il y a une section que je ne comprends pas du tout, à la page deux. Elle s'appelle « Historique du bâtiment »."],
      ["KETTLY", "Celle-là, je la rédige au passé, dans la langue des vieux documents, parce que je recopie ce que disent les archives de la ville. La maison fut construite en 1961. Les propriétaires précédents refirent la toiture en 1998 et remplacèrent la fournaise en 2011."],
      ["DOÏNA", "« Fut construite », « refirent »… On ne parle pas comme ça."],
      ["KETTLY", "On ne parle pas comme ça, non. On l'écrit. C'est le passé des récits écrits. Quand vous le rencontrez, traduisez-le dans votre tête : « fut construite », c'est « a été construite » ; « refirent », c'est « ont refait ». Rien de plus."],
      ["DOÏNA", "Bon. Deuxième chose. Vous écrivez : « Le mur nord, où la fissure a été relevée, présente un taux d'humidité de dix-neuf pour cent. » Dix-neuf, c'est beaucoup ?"],
      ["KETTLY", "C'est trop pour refermer un mur par-dessus. En bas de quinze, je vous dirais d'y aller. À dix-neuf, il faut que vous laissiez sécher, et il faut que le déshumidificateur tourne pendant tout ce temps-là."],
      ["DOÏNA", "Monsieur Trudelle m'a dit la même chose. Trois ou quatre semaines."],
      ["KETTLY", "Alors vous avez deux avis qui concordent. Notez-le : c'est rare, et ça vaut la peine d'être noté."],
      ["DOÏNA", "Maintenant sa soumission. Il y a une colonne « inclus » et une colonne « exclusions ». Pourquoi une entreprise écrirait-elle ce qu'elle ne fait pas ?"],
      ["KETTLY", "Parce que c'est là que se trouvent les mauvaises surprises. Lisez-moi les exclusions."],
      ["DOÏNA", "« Ne sont pas compris : le permis municipal, la peinture, les luminaires, la disposition des matériaux excavés, et tout travail découlant d'une condition non visible au moment de la visite. »"],
      ["KETTLY", "Arrêtez-vous sur la dernière. Elle veut dire : si on ouvre le plancher et qu'on trouve quelque chose que personne ne pouvait voir, ce n'est pas dans le prix."],
      ["DOÏNA", "Et ça arrive souvent, dans une maison de 1961 ?"],
      ["KETTLY", "Assez souvent pour que je vous demande de garder une réserve. Dix pour cent du montant, mis de côté, auxquels vous ne touchez pas."],
      ["DOÏNA", "Trois mille quatre cents dollars que je n'ai pas."],
      ["KETTLY", "Alors demandez-lui d'écrire ce qu'il ferait dans ce cas-là. Pas de vive voix : par écrit, dans la soumission. Une phrase suffit — « toute condition imprévue fera l'objet d'un avis écrit et d'une approbation avant exécution »."],
      ["DOÏNA", "Je peux exiger ça ?"],
      ["KETTLY", "Vous pouvez le demander, et un bon entrepreneur va l'écrire sans discuter. Il souhaite autant que vous que personne ne se retrouve devant une facture qu'il n'attendait pas."],
    ]
  },

  t3: {
    label: "Dialogue — La rencontre du 8 avril, au sous-sol",
    lines: [
      ["FERNAND", "Bon, tout le monde est là. Madame Petrescu, madame Alcindor, et monsieur Toupin est au téléphone, en haut-parleur. On a ouvert le plancher hier matin."],
      ["DOÏNA", "Et vous avez trouvé quelque chose."],
      ["FERNAND", "On a trouvé deux choses. Un : il n'y a aucune membrane sous la dalle de béton. En 1961, ça ne se faisait pas. Deux : il y a un vieux puisard, là, sous le coin, qui avait été condamné par quelqu'un avant vous."],
      ["DOÏNA", "Condamné comment ?"],
      ["KETTLY", "Rempli de pierre et coulé par-dessus. Ça se voyait nulle part : c'est exactement la « condition non visible » dont on parlait au téléphone la semaine passée."],
      ["DOÏNA", "Donc ce n'est pas dans le prix."],
      ["FERNAND", "Ce n'est pas dans le prix, non. Et j'ai deux solutions à vous proposer, avec deux prix et deux délais."],
      ["DOÏNA", "Allez-y. Une à la fois, s'il vous plaît."],
      ["FERNAND", "Première solution : on casse la dalle, on pose une membrane et un drain neuf, on recoule. Six mille huit cents dollars, neuf jours ouvrables de plus."],
      ["DOÏNA", "Et la deuxième ?"],
      ["FERNAND", "On laisse la dalle en place, on pose une membrane par-dessus, puis un plancher flottant sur fourrures. Mille neuf cents dollars, deux jours."],
      ["DOÏNA", "Quelle est la différence, dans dix ans ?"],
      ["KETTLY", "Bonne question, et c'est la vraie. La deuxième solution tolère l'humidité, elle ne l'arrête pas. Si le sol reste sec, elle tient très bien. Si l'eau revient, vous refaites tout, et vous payez le premier prix en plus du deuxième."],
      ["DOÏNA", "Et le sol va rester sec, si on rallonge les gouttières et qu'on refait la pente ?"],
      ["FERNAND", "Il devrait. Je ne peux pas vous le garantir, et je ne vous le garantirai pas par écrit."],
      ["DOÏNA", "Monsieur Toupin, vous êtes toujours là ? Est-ce que ça change quelque chose au permis ?"],
      ["RÉJEAN", "Je suis là. Ça peut, oui. Si vous refaites la dalle, vous touchez à la structure du plancher, et je veux voir le plan modifié avant que les travaux continuent. Si vous posez un plancher flottant par-dessus, c'est du revêtement, et je n'ai rien à voir là-dedans."],
      ["DOÏNA", "Et si je vous envoie le plan modifié, ça prend combien de temps ?"],
      ["RÉJEAN", "Comptez dix jours ouvrables. Et ne vous fiez pas à ce que votre voisin a vécu : chaque municipalité a ses propres exigences, et les miennes ne sont pas celles de la ville d'à côté."],
      ["DOÏNA", "Dix jours de permis, plus neuf jours de travaux. Ma mère arrive le 12 mai. Monsieur Trudelle, si je choisis la première solution aujourd'hui, est-ce que le sous-sol est prêt le 12 ?"],
      ["FERNAND", "Si le permis sort dans dix jours et qu'il ne pleut pas trois semaines de suite, oui. Sinon, il vous manque une semaine."],
      ["DOÏNA", "Alors voici ce que je fais. Je prends la première solution, parce que je ne veux pas payer deux fois. Vous m'écrivez les deux prix et les deux délais aujourd'hui, par courriel, et je signe demain matin. Monsieur Toupin, je vous envoie le plan cet après-midi."],
    ]
  },
};
