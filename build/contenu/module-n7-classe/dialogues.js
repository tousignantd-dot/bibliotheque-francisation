const DIALOGUES = {
  // Niveau 7 : la compétence vise des discours étendus et structurés. Les
  // quatre extraits font de dix-huit à vingt et une répliques, dont plusieurs
  // de quatre ou cinq phrases.
  //
  // Aucune balise HTML dans les répliques : le texte part tel quel à la
  // synthèse vocale, et un « <b> » s'y entendrait. Les nombres s'écrivent en
  // lettres quand ils doivent s'entendre en lettres.
  //
  // LE CASTING A ÉTÉ COMPTÉ AVANT D'ÉCRIRE, et c'est ce qui a décidé du genre
  // de Miguel Ospina. Le dépôt a quatre voix — deux féminines, deux
  // masculines — et deux personnages ne peuvent en partager une que s'ils ne
  // se répondent jamais dans un même extrait. Une salle de classe réunit
  // naturellement trois ou quatre personnes ; les quatre dialogues sont donc
  // répartis pour ne jamais mettre trois voix du même genre dans une scène :
  //   prep : GHISLAINE (F) · NEUSA (F) · YOUSSOUF (M)
  //   t1   : PERRINE   (F) · NEUSA (F) · MIGUEL   (M)
  //   t2   : GHISLAINE (F) · NEUSA (F) · MIGUEL   (M)
  //   t3   : NEUSA     (F) · YOUSSOUF (M) · MIGUEL (M)
  //
  // Rivière-Noire, Vert-Rivière et le Centre de la Pointe-aux-Ormes sont
  // inventés ; les faits sur la chaleur, l'ombre et l'évapotranspiration sont
  // généraux et relevés dans le docstring de manifest.py.

  prep: {
    label: "Dialogue — Ce n'est pas le rôle que je voulais",
    lines: [
      ["GHISLAINE","Bon. Vous avez maintenant vos équipes et vos sujets. Il reste une chose, et c'est celle dont personne ne parle jamais : les rôles. Dans chaque équipe, quelqu'un anime, quelqu'un tient les notes, quelqu'un surveille le temps."],
      ["YOUSSOUF","Madame, on ne peut pas juste travailler ensemble, tout le monde pareil ?"],
      ["GHISLAINE","Vous pouvez essayer. Ça donne trois personnes qui parlent en même temps pendant vingt minutes, et une feuille blanche à la fin. J'ai vu ça souvent. Quelqu'un doit conduire, sinon la rencontre conduit toute seule, et elle conduit mal."],
      ["NEUSA","Et le rôle, c'est nous qui le choisissons ?"],
      ["GHISLAINE","Cette fois-ci, non. Je les ai attribués. Équipe trois : Youssouf aux notes, Miguel au temps et aux sources, Neusa à l'animation."],
      ["NEUSA","À l'animation. Madame, je pense qu'il y a une erreur. Moi, je cherche bien. Je lis vite, je trouve les documents. Mais faire parler les autres, ce n'est pas moi."],
      ["GHISLAINE","Je sais. C'est exactement pour ça."],
      ["NEUSA","Je ne comprends pas."],
      ["GHISLAINE","Neusa, depuis janvier, vous me remettez des textes très propres et vous ne dites presque rien en classe. Vous n'êtes pas silencieuse parce que vous n'avez pas d'idées. Vous êtes silencieuse parce que vous attendez d'être sûre. Animer, ça oblige à parler avant d'être sûre."],
      ["YOUSSOUF","Ça, c'est vrai. Moi, je parle avant même d'avoir une idée."],
      ["GHISLAINE","Et c'est pour ça que vous prenez les notes, Youssouf. Chacun travaille un peu ce qu'il ne fait pas naturellement."],
      ["NEUSA","Mais concrètement, qu'est-ce qu'une animatrice doit faire ? Décider ?"],
      ["GHISLAINE","Presque jamais. Elle ouvre la rencontre en rappelant ce qu'on cherche. Elle donne la parole, et surtout elle la reprend quand quelqu'un la garde trop longtemps. Elle fait préciser : quand quelqu'un dit qu'il y a beaucoup d'arbres, elle demande combien, et où, et comment il le sait."],
      ["NEUSA","Et si les deux autres ne sont pas d'accord entre eux ?"],
      ["GHISLAINE","Alors c'est là que votre rôle commence vraiment. Vous ne tranchez pas tout de suite. Vous reformulez la position de chacun, à voix haute, jusqu'à ce que chacun se reconnaisse dans ce que vous dites. Neuf fois sur dix, le désaccord se dégonfle là."],
      ["YOUSSOUF","Et la dixième fois ?"],
      ["GHISLAINE","La dixième fois, vous mettez les deux positions dans le compte rendu et vous demandez l'avis de la personne-ressource. Ça, c'est une réponse professionnelle. Ce n'est pas une défaite."],
      ["NEUSA","Le compte rendu, c'est aussi l'animatrice ?"],
      ["GHISLAINE","C'est l'animatrice, avec les notes de Youssouf. Après chaque rencontre, une page : qui a proposé quoi, ce qui a été décidé, ce qu'il reste à faire, et pour quand. Et vous l'envoyez aux absents le soir même."],
      ["NEUSA","Madame, je vais être honnête. Ça me fait plus peur que l'exposé."],
      ["GHISLAINE","Je le sais, et je vous le dis franchement : c'est la partie du cours qui vous servira le plus. Un exposé, vous en ferez deux ou trois dans votre vie. Une rencontre où il faut faire parler du monde, vous en aurez une par semaine, dans n'importe quel emploi."],
    ]
  },

  t1: {
    label: "Dialogue — La personne-ressource, un mardi soir",
    lines: [
      ["PERRINE","Bonsoir tout le monde. Je m'appelle Perrine Auclair, je suis agente de projet à Vert-Rivière. Avant de commencer, je vous dis où je m'en vais : je vais parler d'abord de ce qu'est un îlot de chaleur, ensuite de ce que fait un arbre exactement, et enfin de ce qui se passe chez vous, à Rivière-Noire. Vous m'arrêtez quand vous voulez."],
      ["NEUSA","Merci d'être venue. Est-ce qu'on peut vous arrêter vraiment, ou c'est une formule ?"],
      ["PERRINE","Vraiment. Une question au bon moment vaut mieux qu'une main levée pendant vingt minutes. Donc, premier point. Un îlot de chaleur, ce n'est pas une journée chaude. C'est un secteur où la température de surface dépasse celle des secteurs voisins, le même jour, à la même heure."],
      ["MIGUEL","Ça dépasse de combien ?"],
      ["PERRINE","Bonne question, et je vais y répondre en deux temps. Ce qui est mesuré et certain : l'asphalte noir en plein soleil monte bien plus haut qu'une pelouse à côté. Ce qui est estimé : chez vous, l'écart serait d'une dizaine de degrés entre le stationnement du centre commercial et la rue des Ormes. Je dis serait, parce que la mesure a été prise une seule journée, en juillet."],
      ["NEUSA","Vous venez de faire quelque chose que je voudrais bien comprendre. Vous avez dit serait au lieu de est. C'est volontaire ?"],
      ["PERRINE","Complètement. Quand je dis une chose que je n'ai pas vérifiée moi-même, ou qui vient d'une seule mesure, je la mets au conditionnel. Ce serait, il y aurait, on estimerait. Ça vous dit : notez le chiffre, mais ne le mettez pas dans votre exposé comme une certitude."],
      ["MIGUEL","Dans les travaux, on nous demande justement de citer nos sources. Là, ça devient utile."],
      ["PERRINE","C'est la même chose. Deuxième point : qu'est-ce qu'un arbre fait, exactement ? Deux choses, et deux seulement. La première, tout le monde la connaît : il porte de l'ombre, donc le sol sous lui ne chauffe pas."],
      ["NEUSA","Et la deuxième ?"],
      ["PERRINE","La deuxième, on l'oublie toujours. L'arbre pompe de l'eau par ses racines et il la rejette par ses feuilles, sous forme de vapeur. Ça s'appelle l'évapotranspiration. Et rejeter de la vapeur, ça consomme de la chaleur. Autrement dit, un arbre ne fait pas seulement de l'ombre : il refroidit l'air autour de lui, même si vous n'êtes pas dessous."],
      ["MIGUEL","Donc un grand arbre vaut plus que dix petits ?"],
      ["PERRINE","Pour rafraîchir, aujourd'hui, oui, et de beaucoup. Un arbre mature a une cime large et des milliers de feuilles ; un jeune arbre planté l'an dernier n'a presque rien. C'est pour ça qu'abattre un vieil érable et planter trois jeunes arbres à la place, ce n'est pas neutre, même si le compte est bon."],
      ["NEUSA","Je vous arrête, parce que je veux être sûre de bien noter. Si je comprends bien, ce qui compte, ce n'est pas le nombre d'arbres, c'est la surface couverte par les cimes. C'est ça ?"],
      ["PERRINE","C'est exactement ça, et vous venez de nommer le mot que je gardais pour la fin. Cette surface-là, vue d'en haut, on l'appelle la canopée. On la mesure en pourcentage du territoire."],
      ["MIGUEL","Et à Rivière-Noire, il y en a combien ?"],
      ["PERRINE","La ville publie un chiffre autour de dix-sept pour cent pour l'ensemble du territoire. Prenez ce chiffre avec précaution : la méthode de calcul change d'une ville à l'autre, et le chiffre de deux villes voisines ne se compare pas toujours. Quant au secteur de votre centre, ce serait plutôt sous les dix pour cent."],
      ["NEUSA","Encore le conditionnel."],
      ["PERRINE","Encore. Vous apprenez vite. Dernier point, et c'est celui qui vous concerne le plus pour votre travail. La ville a un plan de plantation, et il y a une chose qu'on ne dit presque jamais : le difficile, ce n'est pas de planter. C'est d'arroser pendant trois ans."],
      ["MIGUEL","Trois ans ? Un arbre, ça ne se débrouille pas tout seul ?"],
      ["PERRINE","Pas les premières années, et pas dans une fosse de trottoir large comme une table de cuisine. Un jeune arbre de rue mal arrosé meurt en silence, et personne ne le remarque avant le troisième été. Si vous cherchez un angle pour votre exposé, il est là, et il n'est presque jamais traité."],
    ]
  },

  t2: {
    label: "Dialogue — Vous m'avez remis un copier-coller poli",
    lines: [
      ["GHISLAINE","Neusa, Miguel, vous avez deux minutes avant la pause ? J'ai lu votre premier résumé."],
      ["NEUSA","On l'a fait à deux. Il est trop long ?"],
      ["GHISLAINE","Il fait la bonne longueur. Le problème n'est pas là. Regardez la troisième phrase et dites-moi d'où elle vient."],
      ["MIGUEL","De la fiche de la ville. On l'a prise telle quelle parce qu'elle était claire."],
      ["GHISLAINE","Elle est claire parce que quelqu'un a été payé pour l'écrire. Et c'est justement pour ça qu'on ne la recopie pas. Un résumé qui reprend les phrases du texte ne prouve rien : je ne sais pas si vous avez compris ou si vous avez copié."],
      ["NEUSA","Mais si la phrase dit exactement ce qu'on veut dire, pourquoi la changer ?"],
      ["GHISLAINE","Parce que ce n'est pas votre travail de dire ce que le texte dit. Votre travail, c'est de dire ce que le texte apporte à votre question. Ce n'est pas la même chose. Quelle est votre question de départ, déjà ?"],
      ["MIGUEL","Pourquoi certaines rues de Rivière-Noire sont plus chaudes que d'autres."],
      ["GHISLAINE","Bon. Alors relisez votre troisième phrase avec cette question dans la tête."],
      ["NEUSA","Elle parle du budget du programme de plantation. Ça ne répond pas à la question."],
      ["GHISLAINE","Voilà. Et pourtant vous l'avez gardée. Pourquoi ?"],
      ["NEUSA","Parce qu'elle était intéressante."],
      ["GHISLAINE","C'est le piège de tous les résumés. On garde ce qui est intéressant au lieu de garder ce qui répond. Première règle : chaque phrase de votre résumé doit pouvoir se rattacher à votre question. Si vous n'y arrivez pas, la phrase sort."],
      ["MIGUEL","Et pour ne pas recopier, on fait comment, concrètement ? Si on change juste deux mots, c'est pareil."],
      ["GHISLAINE","Trois outils, et vous les avez déjà tous vus. Le premier : remplacez un morceau de phrase par un nom. La fiche dit que la ville a planté quatre cents arbres. Vous écrivez : la plantation de quatre cents arbres. Vous venez de gagner sept mots."],
      ["NEUSA","Ça, c'est ce que vous appelez la nominalisation ?"],
      ["GHISLAINE","C'est ça, et c'est l'outil numéro un du résumé. Deuxième outil : quand une chose revient, ne la renommez pas pareil. Les arbres plantés le long des rues, puis ces jeunes arbres, puis les plantations. Vous reprenez la même chose avec un mot différent, et le texte tient debout sans se répéter."],
      ["MIGUEL","Et le troisième ?"],
      ["GHISLAINE","Les connecteurs. Un résumé sans connecteurs est une liste. Avec autrement dit, en somme, quant à, en ce qui concerne, vos phrases se tiennent par la main. Et le lecteur voit où vous l'emmenez."],
      ["NEUSA","Madame, une dernière chose. Est-ce qu'on a le droit de citer une phrase du texte, quand même ?"],
      ["GHISLAINE","Oui, une, entre guillemets, avec la source. Une citation dans un résumé de dix lignes, c'est un choix ; trois, c'est un copier-coller poli."],
    ]
  },

  t3: {
    label: "Dialogue — Ça ne prouve rien, ton comptage",
    lines: [
      ["NEUSA","Bon. Il est sept heures cinq, on a quarante minutes. Je rappelle où on en est : on cherche pourquoi certaines rues sont plus chaudes que d'autres, et il nous manque encore les données de notre secteur. Youssouf, tu voulais commencer."],
      ["YOUSSOUF","Oui. Ma proposition est simple : samedi matin, on descend la rue des Ormes et la rue Bellechasse, et on compte les arbres. Un côté chacun. En deux heures, c'est fait, et on a un chiffre à nous."],
      ["MIGUEL","Franchement, ça ne prouve rien, ton comptage."],
      ["NEUSA","Attends, Miguel. Youssouf, avant qu'on discute : tu comptes quoi exactement ? Tous les arbres, ou seulement ceux du bord de la rue ?"],
      ["YOUSSOUF","Ceux du bord de la rue. Ceux des cours privées, on ne les voit pas bien."],
      ["NEUSA","D'accord. Alors Miguel, vas-y. Qu'est-ce qui ne va pas, selon toi ?"],
      ["MIGUEL","Perrine l'a dit clairement : ce qui compte, ce n'est pas le nombre d'arbres, c'est la surface des cimes. Deux rues peuvent avoir le même nombre d'arbres et pas du tout la même canopée. On va marcher deux heures pour un chiffre qu'on ne pourra même pas utiliser."],
      ["YOUSSOUF","Alors on ne fait rien, c'est ça ? On recopie les chiffres de la ville et on rentre chez nous ?"],
      ["NEUSA","On se calme, tous les deux. Je reformule, et vous me dites si je me trompe. Youssouf, tu dis qu'une donnée que nous avons prise nous-mêmes vaut mieux qu'un chiffre repris ailleurs, même si elle est imparfaite. C'est bien ça ?"],
      ["YOUSSOUF","C'est ça. Et on est les seuls à être allés voir."],
      ["NEUSA","Miguel, tu dis que compter des troncs ne mesure pas ce qu'on cherche, et qu'un chiffre qui ne répond pas à la question est un chiffre perdu. C'est bien ça aussi ?"],
      ["MIGUEL","C'est exactement ça. Je ne suis pas contre aller marcher. Je suis contre compter la mauvaise chose."],
      ["NEUSA","Bon. Alors écoutez ce que je viens d'entendre : vous n'êtes pas en désaccord sur le fait d'y aller. Vous êtes en désaccord sur ce qu'on note en y allant."],
      ["YOUSSOUF","Dit comme ça, oui."],
      ["MIGUEL","Bien que ce soit plus long, on pourrait noter autre chose que le nombre. Par exemple, à chaque coin de rue, est-ce que le trottoir est à l'ombre ou au soleil à dix heures."],
      ["NEUSA","Répète ça, Miguel, je le note. L'ombre au sol, à une heure fixe, à des endroits fixes."],
      ["MIGUEL","Voilà. Et ça, ça se compare d'une rue à l'autre. Un arbre mature fait une grande tache d'ombre ; trois petits n'en font presque pas."],
      ["YOUSSOUF","Même si je trouve qu'on complique, je suis d'accord. On note les deux : le nombre et l'ombre. Le nombre me prend trente secondes de plus par coin de rue."],
      ["NEUSA","Parfait. Alors je résume les décisions, et Youssouf, tu vérifies tes notes pendant que je parle. Un : on y va samedi à dix heures, pas à neuf, parce que l'ombre à neuf heures ne veut rien dire. Deux : à chaque coin, on note le nombre d'arbres de rue et si le trottoir est à l'ombre ou au soleil. Trois : Miguel écrit à Perrine pour lui demander si notre méthode tient debout. Quatre : moi, j'envoie le compte rendu à Alfonso ce soir, parce qu'il travaillait et qu'il n'était pas là."],
      ["YOUSSOUF","Tout y est. Et il est sept heures trente-cinq."],
      ["NEUSA","Alors on a fini cinq minutes en avance. C'est la première fois depuis trois semaines."],
    ]
  },
};
