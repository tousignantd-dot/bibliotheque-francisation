const DIALOGUES = {
  prep: {
    label: "Dialogue — La tache au plafond",
    lines: [
      ["MARIAMA","Kim ! Attends une minute avant de descendre. Est-ce que tu as eu de l'eau chez toi cette nuit ?"],
      ["KIM","De l'eau ? Non… Pourquoi ? Qu'est-ce qui se passe ?"],
      ["MARIAMA","Viens voir. Regarde le plafond de ma chambre, dans le coin, au-dessus du lit."],
      ["KIM","Oh là là. C'est une grosse tache brune. Et le tour est plus foncé, on dirait un cerne."],
      ["MARIAMA","Ça coulait encore à six heures ce matin. J'ai mis une chaudière par terre, et elle est déjà à moitié pleine."],
      ["KIM","Le coin de ta chambre, c'est juste en dessous de ma salle de bain. Attends… mon chauffe-eau est dans le garde-robe, là."],
      ["MARIAMA","Est-ce que tu peux aller voir tout de suite ? Moi, je commence à sept heures et demie."],
      ["KIM","J'y monte. Si c'est le chauffe-eau qui a lâché, ça expliquerait tout : il a quinze ans, ce réservoir-là."],
      ["MARIAMA","Et le plancher de ma chambre a commencé à gondoler. Les lattes se soulèvent près du mur."],
      ["KIM","Prends des photos. Tout de suite, avant que ça sèche, et avec la date."],
      ["MARIAMA","Bonne idée. Il y a aussi ma boîte de papiers qui était par terre, en dessous. Elle est trempée."],
      ["KIM","Prends-la en photo aussi, et ne jette rien. Rien du tout, même ce qui est fini. C'est ta preuve."],
      ["MARIAMA","Je vais appeler monsieur Cloutier sur l'heure du dîner."],
      ["KIM","Appelle-le avant. Un dégât d'eau, ça ne s'améliore pas tout seul en attendant midi."],
    ]
  },

  t1: {
    label: "Dialogue — L'appel au propriétaire",
    lines: [
      ["MARIAMA","Monsieur Cloutier ? Mariama Baldé, du logement 4, au 118 Sainte-Hélène."],
      ["RÉJEAN","Bonjour, madame Baldé. Qu'est-ce que je peux faire pour vous ?"],
      ["MARIAMA","J'ai un dégât d'eau dans ma chambre. Le plafond a coulé pendant la nuit."],
      ["RÉJEAN","Coulé comment ? Une goutte de temps en temps, ou de l'eau qui tombe ?"],
      ["MARIAMA","De l'eau qui tombait vraiment. Quand je me suis levée à six heures, il y en avait déjà partout sur le plancher."],
      ["RÉJEAN","Et là, présentement, est-ce que ça coule encore ?"],
      ["MARIAMA","Ça a arrêté vers sept heures. Mais en revenant du travail, j'ai vu que la tache avait doublé."],
      ["RÉJEAN","Bon. Décrivez-moi les dommages, pièce par pièce."],
      ["MARIAMA","Une tache brune d'à peu près un mètre au plafond, le plancher qui gondole sur trois lattes, et la peinture du mur qui cloque."],
      ["RÉJEAN","D'accord. Et vos affaires ?"],
      ["MARIAMA","Une boîte de documents complètement trempée, et le matelas est humide sur un coin. J'ai dormi sur le divan hier soir."],
      ["RÉJEAN","Je m'excuse. Madame Nguyên m'a appelé aussi : c'est son chauffe-eau qui a lâché. Le plombier est passé cet après-midi."],
      ["MARIAMA","Donc la fuite est réparée. Mais chez moi, le dégât reste."],
      ["RÉJEAN","Il reste, oui. J'envoie une compagnie d'assèchement demain matin. Ils vont installer des appareils dans votre chambre pour trois ou quatre jours."],
      ["MARIAMA","Trois ou quatre jours pendant lesquels je ne peux pas coucher dans ma chambre."],
      ["RÉJEAN","Je le sais. On va en reparler. Envoyez-moi vos photos par courriel aujourd'hui, avec la date."],
    ]
  },

  t2: {
    label: "Dialogue — L'avis dans l'entrée",
    lines: [
      ["KIM","Mariama, viens voir. Il y a un avis affiché dans l'entrée, à côté des boîtes aux lettres."],
      ["MARIAMA","Il était là ce matin ?"],
      ["KIM","Non, il vient d'être posé. C'est écrit « Avis aux locataires » en gros, en haut."],
      ["MARIAMA","« Des travaux d'assèchement seront effectués dans les logements 3 et 4… » Ça, c'est chez toi et chez moi."],
      ["KIM","« … du mercredi 12 au vendredi 14 novembre, entre 8 h et 17 h. »"],
      ["MARIAMA","Trois jours. Et en dessous : « Il est nécessaire que les occupants libèrent l'accès au mur touché. »"],
      ["KIM","Ça veut dire tasser les meubles. Ton lit, ta commode, tout ce qui est le long de ce mur-là."],
      ["MARIAMA","« Veuillez prévoir un accès au logement. À défaut, l'entrepreneur communiquera avec le propriétaire. »"],
      ["KIM","Autrement dit : si tu n'es pas là et que personne n'ouvre, ils appellent monsieur Cloutier et il ouvre lui-même."],
      ["MARIAMA","Est-ce qu'il a le droit d'entrer chez moi comme ça ?"],
      ["KIM","Pour des travaux, oui, mais il doit t'avertir vingt-quatre heures d'avance, et venir entre sept heures du matin et sept heures du soir. L'avis, c'est justement ça."],
      ["MARIAMA","Il y a une dernière ligne, en petit : « Le bruit des appareils est important et continu. »"],
      ["KIM","Ça, c'est vrai. Un asséchateur, ça souffle jour et nuit. On ne dort pas à côté."],
      ["MARIAMA","Alors je note tout : les dates, les heures, ce que je dois faire, et ce que ça m'enlève. Trois nuits sur le divan, ce n'est pas rien."],
      ["KIM","Écris-le au propriétaire aujourd'hui même. Un avis qu'on lit sans répondre, c'est un avis qu'on accepte."],
    ]
  },

  t3: {
    label: "Dialogue — La réclamation",
    lines: [
      ["SYLVIE","Assurances Bellerive, Sylvie Painchaud à l'appareil."],
      ["MARIAMA","Bonjour. Je voudrais ouvrir une réclamation. J'ai eu un dégât d'eau chez moi le 10 novembre."],
      ["SYLVIE","Je vous écoute. Racontez-moi ce qui est arrivé, dans l'ordre."],
      ["MARIAMA","Le chauffe-eau du logement du dessus a lâché pendant la nuit. Quand je me suis levée, l'eau coulait du plafond de ma chambre."],
      ["SYLVIE","Est-ce que la cause a été confirmée par quelqu'un ?"],
      ["MARIAMA","Oui. Un plombier est venu le jour même et il a remplacé le réservoir. J'ai le nom de la compagnie."],
      ["SYLVIE","Parfait. Maintenant, ce qui est endommagé chez vous : qu'est-ce qui vous appartient ?"],
      ["MARIAMA","Ce qui m'appartient, c'est le matelas, une commode et une boîte de documents. Le plafond et le plancher, eux, appartiennent à l'immeuble."],
      ["SYLVIE","Exactement. Le bâtiment, c'est l'assurance du propriétaire ; vos biens, c'est la vôtre. Vous avez des photos ?"],
      ["MARIAMA","J'en ai vingt-deux, prises le matin même, avec la date. Et j'ai gardé le matelas : je ne l'ai pas jeté."],
      ["SYLVIE","Vous avez très bien fait. Ce qui bloque la plupart des réclamations, c'est justement qu'on jette avant de faire constater."],
      ["MARIAMA","Il y a une franchise, je pense ?"],
      ["SYLVIE","Cinq cents dollars à votre contrat. En dessous de ce montant-là, ça ne vaut pas la peine de réclamer."],
      ["MARIAMA","Le matelas à lui seul en valait huit cents. Donc je réclame."],
      ["SYLVIE","Alors je vous ouvre un dossier. Étant donné que la cause vient du logement du dessus, il se peut qu'on se retourne ensuite vers l'assureur du propriétaire — mais ça, c'est entre nous, pas votre problème."],
      ["MARIAMA","Et pour les trois nuits où je n'ai pas pu dormir dans ma chambre ?"],
      ["SYLVIE","Ça, c'est une autre démarche : c'est au propriétaire que vous demandez une réduction de loyer, par écrit. Nous, on couvre vos biens."],
    ]
  },
};
