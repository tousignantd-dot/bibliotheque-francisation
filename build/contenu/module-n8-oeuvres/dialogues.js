const DIALOGUES = {

  // Quatre personnages, quatre voix distinctes — aucun partage, donc aucune
  // contrainte de croisement, et aucun extrait ne réunit plus de trois
  // locuteurs. Le casting a été compté PAR EXTRAIT ET PAR GENRE avant
  // d'écrire une seule réplique, comme CLAUDE.md le demande depuis
  // `module-n7-habitation` : le dépôt n'a que deux voix féminines.
  //
  //   FATOUMATA (enseignante, ralentie à 0,85) — présente partout ;
  //   JOSYANE   (féminine 2) — la chroniqueuse, présente en prep, t2, t3 ;
  //   LÉANDRE   (masculin 1) — présent en t1 et t3 ;
  //   GASPARD   (narrateur, NON ralentie) — seulement en t2.
  //
  // Le défi 3 réunit trois personnages dont deux femmes : c'est la limite
  // exacte du dépôt, et elle tient parce que Fatoumata prend `enseignante` et
  // Josyane `feminin_2`. Une troisième femme aurait été impossible.
  //
  // GASPARD porte le quasi-monologue du défi 2 — quatorze répliques d'affilée
  // coupées par deux questions — et il prend `narrateur` pour la raison que
  // l'activité 119 a écrite : cette voix-là n'est pas ralentie par
  // `voix_lente.py`, et quatorze répliques ralenties d'affilée seraient
  // interminables.

  prep: {
    label: "Dialogue — Tout le monde résume, personne ne lit",
    lines: [
      ["FATOUMATA","Madame Deschatelets ? Vos deux livres sont rentrés hier, je les ai mis de côté."],
      ["JOSYANE","Merci. Et appelez-moi Josyane, on se croise ici toutes les semaines depuis trois ans."],
      ["FATOUMATA","Josyane, alors. J'aurais une demande à vous faire, et vous avez le droit de dire non."],
      ["JOSYANE","Dites toujours."],
      ["FATOUMATA","J'anime le cercle du mardi soir, ici, au sous-sol. Dix-huit personnes, une œuvre par mois. Ça marche très bien, et pourtant quelque chose ne va pas."],
      ["JOSYANE","Qu'est-ce qui ne va pas ?"],
      ["FATOUMATA","Chacun raconte ce qu'il a vu. Puis chacun dit s'il a aimé. Et à neuf heures moins quart, on se lève. On n'a rien fait d'autre en une heure et demie."],
      ["JOSYANE","Autrement dit, vous résumez et vous notez."],
      ["FATOUMATA","C'est exactement ça. Résumer et noter. Personne ne dit jamais ce que l'œuvre veut dire."],
      ["JOSYANE","Attention. « Ce que l'œuvre veut dire », c'est une formule dangereuse : elle laisse croire qu'il y a une réponse cachée quelque part et qu'un professeur la connaît."],
      ["FATOUMATA","Il n'y en a pas ?"],
      ["JOSYANE","Il y a mieux. Il y a des lectures — plusieurs, et elles ne se valent pas toutes. Une lecture se juge à ce qu'elle permet d'expliquer dans l'œuvre. Celle qui explique le plus de détails est la plus solide, ce jour-là."],
      ["FATOUMATA","Ça veut dire qu'on peut avoir raison tous les deux ?"],
      ["JOSYANE","Ça veut dire qu'on peut être défendable tous les deux. Ce n'est pas la même chose, et c'est beaucoup plus intéressant."],
      ["FATOUMATA","Comment est-ce qu'on apprend ça à dix-huit personnes qui ont fini l'école il y a quarante ans ?"],
      ["JOSYANE","Par une seule discipline, et elle est difficile : séparer trois choses qu'on dit d'un même souffle. Le fait. L'interprétation. Le jugement."],
      ["FATOUMATA","Donnez-moi un exemple, sinon je vais retenir les trois mots et rien d'autre."],
      ["JOSYANE","« À la fin, elle s'assoit dans la chaloupe et elle ne démarre pas le moteur. » Qu'est-ce que c'est ?"],
      ["FATOUMATA","Un fait. On l'a tous vu."],
      ["JOSYANE","« Elle renonce à partir. » Et ça ?"],
      ["FATOUMATA","Une interprétation. Ce n'est écrit nulle part, c'est moi qui l'ajoute."],
      ["JOSYANE","Voilà. Et « cette fin est ratée » ?"],
      ["FATOUMATA","Un jugement."],
      ["JOSYANE","Le problème de votre cercle, ce n'est pas qu'on y juge trop. C'est qu'on saute du premier au troisième sans passer par le deuxième. On raconte, on note, et l'interprétation manque au milieu."],
      ["FATOUMATA","Est-ce que vous viendriez le dire vous-même, un mardi ?"],
      ["JOSYANE","Je viendrai. À une condition : que ce ne soit pas moi qui parle en premier. Vous ouvrez, vous proposez une lecture, et je n'interviens qu'après."],
      ["FATOUMATA","Ça, c'est plus effrayant que de vous inviter."],
      ["JOSYANE","Je sais. C'est pour ça que je le demande."],
    ]
  },

  t1: {
    label: "Dialogue — La dernière scène des « Eaux basses »",
    lines: [
      ["LÉANDRE","Fatoumata, avez-vous regardé la finale hier soir ? Le dernier épisode des « Eaux basses » ?"],
      ["FATOUMATA","Je l'ai regardé deux fois, monsieur Pinsonneault. Une fois hier, et une fois ce matin avant d'ouvrir."],
      ["LÉANDRE","Deux fois ! Moi, une seule m'a suffi. Six épisodes pour arriver à ça. Ils ont manqué de temps, c'est tout."],
      ["FATOUMATA","Racontez-moi la dernière scène. Juste ce qui s'y passe, sans dire ce que vous en pensez."],
      ["LÉANDRE","Bon. Estelle sort du chalet. Il fait presque nuit. Elle descend au quai, elle retourne la chaloupe, elle la remet à l'eau. Elle s'assoit dedans. Le téléphone sonne sur le quai, elle ne le prend pas. La lumière du quai s'allume toute seule. Écran noir."],
      ["FATOUMATA","Vous avez oublié deux choses."],
      ["LÉANDRE","J'ai oublié quoi ?"],
      ["FATOUMATA","Avant de descendre, elle enlève ses bottes de ville et elle met les bottes de caoutchouc de sa mère, celles qui traînent depuis le premier épisode. Et la corde de la chaloupe reste attachée au taquet du quai."],
      ["LÉANDRE","La corde… c'est vrai. Elle ne la détache pas."],
      ["FATOUMATA","Elle ne la détache pas. Elle est assise dans une chaloupe qui ne peut pas partir."],
      ["LÉANDRE","Et vous appelez ça une fin ? Moi j'appelle ça un épisode qu'on n'a pas fini de tourner."],
      ["FATOUMATA","C'est une fin ouverte. Ce n'est pas la même chose qu'une fin manquante."],
      ["LÉANDRE","Expliquez-moi la différence, parce que de mon fauteuil, ça se ressemble beaucoup."],
      ["FATOUMATA","Une fin manquante, c'est quand il manque un renseignement : on ne sait pas qui a fait le coup, et personne ne peut le deviner. Une fin ouverte, c'est quand on a tout ce qu'il faut, et que ce qu'on en fait dépend de nous."],
      ["LÉANDRE","Alors qu'est-ce que vous en faites, vous ?"],
      ["FATOUMATA","Je pense qu'elle choisit de rester, et que pour la première fois de la série, c'est elle qui choisit. Ce qui compte, ce n'est pas la chaloupe : c'est le téléphone qu'elle laisse sonner."],
      ["LÉANDRE","Moi je vois exactement le contraire. Elle est prise. Elle a passé six épisodes à dire qu'elle partirait au printemps, et à la fin elle est assise dans une chaloupe attachée. C'est une prison, votre affaire."],
      ["FATOUMATA","Bien que ce soit une chaloupe attachée, c'est elle qui l'a remise à l'eau. Personne ne l'y a forcée."],
      ["LÉANDRE","Elle aurait pu la détacher. Ça prend quatre secondes, un taquet."],
      ["FATOUMATA","Elle aurait pu, oui. Et si elle l'avait détachée, on n'en parlerait pas, vous et moi, un mardi matin, devant un chariot de retours."],
      ["LÉANDRE","Ha ! Ça, c'est un argument de bibliothécaire."],
      ["FATOUMATA","C'en est un mauvais, je vous l'accorde. En voici un meilleur : les bottes. Pourquoi la réalisatrice nous montre-t-elle quatorze secondes de bottes de caoutchouc si la fin ne veut rien dire ?"],
      ["LÉANDRE","Quatorze secondes ?"],
      ["FATOUMATA","Je les ai comptées ce matin. C'est le plan le plus long de l'épisode."],
      ["LÉANDRE","Bon. Ça, je ne peux pas le nier. Mais ça ne prouve pas qu'elle choisit. Ça prouve qu'elle prend la place de sa mère, ce qui est encore pire."],
      ["FATOUMATA","Ça, c'est une troisième lecture, et elle est bonne. Vous voyez, vous venez d'en faire une."],
      ["LÉANDRE","Je n'ai rien fait du tout, j'ai dit ce que je pensais."],
      ["FATOUMATA","Vous avez appuyé ce que vous pensiez sur un détail de l'image. C'est exactement ce que Josyane appelle une lecture. Venez mardi, vous allez être insupportable et ça va être parfait."],
    ]
  },

  t2: {
    label: "Dialogue — La chronique du samedi : une nouvelle et un poème",
    lines: [
      ["JOSYANE","Vous écoutez « À livre ouvert », la chronique du samedi matin. Gaspard Thivierge, bonjour. Vous nous apportez deux textes courts aujourd'hui."],
      ["GASPARD","Bonjour Josyane. Deux textes courts, oui, et je les ai choisis ensemble parce qu'ils font le même geste par deux moyens différents. Une nouvelle et un poème."],
      ["GASPARD","La nouvelle d'abord. Elle s'appelle « La chaise du fond », elle est d'Odile Brassard-Vézina, et elle ouvre son recueil « Les jours de semaine », paru l'automne dernier."],
      ["GASPARD","Six pages. L'histoire tient en une phrase : une femme arrive à son propre pot de départ à la retraite, dans la cafétéria de l'usine de portes et fenêtres où elle a travaillé trente et un ans."],
      ["GASPARD","Elle s'appelle Gisèle. À son arrivée, la salle est déjà pleine. Il reste deux places : une au centre, devant le gâteau, et une au fond, contre le mur, à la table où l'on installe les stagiaires l'été."],
      ["GASPARD","Elle prend la chaise du fond. Personne ne relève. Le contremaître fait un discours de quatre minutes où il l'appelle deux fois par le prénom de quelqu'un d'autre."],
      ["GASPARD","On lui tend la carte signée par l'atelier. Elle demande à sa voisine de la lire à voix haute à sa place. Elle dit qu'elle a oublié ses lunettes, et le texte précise, entre parenthèses, qu'elle ne les avait pas oubliées."],
      ["GASPARD","Et à la toute fin, quand la salle se vide, elle plie la nappe de papier de sa table, celle du fond, et elle la met dans son sac. La nouvelle s'arrête là. Six pages, pas un mot de plus."],
      ["JOSYANE","Qu'est-ce qu'on est censé comprendre de cette nappe ?"],
      ["GASPARD","Rien n'est censé, et c'est tout l'art de cette auteure-là. Deux lectures se défendent, et l'une n'est pas plus fine que l'autre."],
      ["GASPARD","La première : Gisèle est une femme effacée, qui se met au fond parce qu'elle s'est toujours mise au fond, et qui emporte la nappe comme on emporte un souvenir. C'est la lecture tendre, et le texte la nourrit : il y a partout de petits gestes de retrait."],
      ["GASPARD","La seconde : Gisèle est en colère, elle a choisi le fond pour que ça se voie, elle a refusé de lire la carte pour que quelqu'un d'autre entende à voix haute ce que trente et un ans valent, et la nappe qu'elle emporte est la preuve de l'endroit où on l'a assise."],
      ["GASPARD","La phrase entre parenthèses tranche en faveur de la seconde. Une seule parenthèse dans six pages : quand une auteure prend la peine de nous dire que le mensonge est un mensonge, elle ne le fait pas par distraction."],
      ["GASPARD","Ce qui ne veut pas dire que la première lecture est fausse. Elle explique moins de choses, voilà tout. C'est le seul critère que je connaisse."],
      ["JOSYANE","Et le poème ?"],
      ["GASPARD","« Déneigement », de Régine Amyot. Vingt-deux vers, trois strophes. Une personne dégage son auto tous les matins de janvier, dans un stationnement de Sherbrooke, avant six heures."],
      ["GASPARD","Les deux premières strophes ne parlent que de neige, de gratte et de doigts froids. Rien d'autre. On croit lire un poème sur l'hiver, et c'est très bien fait."],
      ["GASPARD","La troisième strophe change un seul mot, et ce mot fait basculer les vingt et un autres : « je déneige quelqu'un qui n'est plus là ». À partir de là, tout ce qu'on vient de lire devient autre chose."],
      ["GASPARD","La gratte n'est plus une gratte, le pare-brise n'est plus un pare-brise, et le lecteur a l'impression d'avoir été distrait pendant deux strophes. C'est faux : il n'a rien manqué. L'information n'était pas là."],
      ["GASPARD","Voilà pourquoi je les ai mis ensemble. Chez Brassard-Vézina, ce qui compte est dit une seule fois, entre parenthèses. Chez Amyot, ce qui compte est dit à la fin, en un mot. Dans les deux cas, un lecteur pressé passe à côté et n'en saura jamais rien."],
      ["JOSYANE","Gaspard Thivierge, merci. On se retrouve samedi prochain."],
      ["GASPARD","Merci à vous."],
    ]
  },

  t3: {
    label: "Dialogue — Le cercle du mardi, huit heures moins dix",
    lines: [
      ["FATOUMATA","Bonsoir à tous. Ce soir, on essaie autre chose. Personne ne raconte la finale : on l'a tous vue. On propose des lectures, et on les appuie."],
      ["FATOUMATA","Je commence, puisque c'est moi qui ai eu l'idée. Ma lecture : Estelle choisit de rester, et c'est le premier choix qu'elle fait dans toute la série."],
      ["FATOUMATA","Ce qui me le fait dire, c'est le téléphone. Elle l'apporte jusqu'au quai, elle le pose, et elle le laisse sonner. Ce n'est pas un oubli : c'est un objet qu'elle transporte pour pouvoir le laisser."],
      ["LÉANDRE","Et la corde, madame Sidibé ? Vous passez la corde sous silence, ce soir."],
      ["FATOUMATA","Je ne la passe pas sous silence, monsieur Pinsonneault. Je vous laisse la sortir : c'est votre meilleur argument, et il est à vous."],
      ["LÉANDRE","Alors je le sors. La chaloupe reste attachée. Une femme assise dans une embarcation attachée, ça ne s'appelle pas un choix, ça s'appelle un piège. Ma lecture : elle est prise, et elle le sait."],
      ["JOSYANE","Est-ce que je peux poser une question aux deux ?"],
      ["FATOUMATA","C'est pour ça qu'on vous a invitée."],
      ["JOSYANE","Chacun de vous a un indice. Le téléphone contre la corde. Est-ce que l'un des deux explique aussi l'autre ?"],
      ["LÉANDRE","Comment ça, expliquer l'autre ?"],
      ["JOSYANE","Votre lecture doit rendre compte du téléphone, et la sienne doit rendre compte de la corde. Sinon, chacun de vous a raison sur un tiers de la scène et se tait sur le reste."],
      ["LÉANDRE","Bon. Le téléphone… si elle est prise, elle le laisse sonner parce qu'elle n'a plus rien à dire à personne. Ça se tient."],
      ["JOSYANE","Ça se tient. Et la corde, madame Sidibé ?"],
      ["FATOUMATA","La corde… Si elle avait voulu partir, elle l'aurait détachée. Elle ne l'a pas détachée. Donc soit elle est prise, comme le dit monsieur Pinsonneault, soit elle a décidé de ne pas partir — et alors la corde n'est pas ce qui la retient, c'est ce qu'elle laisse en place."],
      ["JOSYANE","Vous venez de faire quelque chose d'important. Vous n'avez pas nié l'indice de l'autre : vous l'avez repris dans votre lecture."],
      ["LÉANDRE","Elle l'a surtout retourné, oui."],
      ["JOSYANE","Retourner un indice, c'est permis. Le passer sous silence, non. Vous avez maintenant deux lectures qui expliquent les trois indices, et c'est là que la discussion devient utile — pas avant."],
      ["FATOUMATA","Josyane, vous avez apporté quelque chose."],
      ["JOSYANE","J'ai apporté « L'Écho des Deux-Rives » de jeudi. Gaspard Thivierge y signe une critique de la pièce « Le troisième rang », qui se joue au Vieux-Presbytère jusqu'au 14. Aucun de vous ne l'a vue."],
      ["LÉANDRE","Alors qu'est-ce qu'on en dirait ?"],
      ["JOSYANE","Justement. On ne va pas parler de la pièce : on va parler du texte. Où est-ce que le critique décrit, où est-ce qu'il juge, et où est-ce qu'il devine ?"],
      ["FATOUMATA","On peut discuter une critique sans avoir vu ce dont elle parle ?"],
      ["JOSYANE","On ne peut pas dire si elle a raison. On peut dire si elle est appuyée, et ce n'est pas rien : c'est même ce que vous ferez toute votre vie avec les critiques que vous lisez."],
      ["LÉANDRE","Et si on n'est pas d'accord avec lui ?"],
      ["JOSYANE","Le journal a un courrier des lecteurs. Deux cents mots, on y publie tout ce qui est signé et argumenté."],
      ["FATOUMATA","Alors voilà notre devoir pour le mardi de la semaine prochaine, tout le monde. Deux cents mots à monsieur Thivierge."],
      ["LÉANDRE","Deux cents mots ! Je n'ai pas écrit deux cents mots depuis ma retraite."],
      ["FATOUMATA","Vous en avez dit trois cents ce soir sans y penser, monsieur Pinsonneault. On va simplement les mettre dans l'ordre."],
    ]
  },

};
