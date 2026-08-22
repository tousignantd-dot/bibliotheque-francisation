const DIALOGUES = {
  // Trois dialogues, un par section. Au niveau 6, ils font dix-huit à vingt
  // répliques : la compétence vise « des discours détaillés et structurés »,
  // et une conversation de trois répliques n'en est pas un.
  //
  // Le même dossier revient dans les trois — le travail de recherche de
  // l'équipe de Marisol — sous trois angles : l'annonce en classe, la
  // consigne lue ligne à ligne, puis les sources qui ne concordent pas.
  //
  // Quatre personnages, trois timbres. Voir l'en-tête de
  // generer_audio_module_n6_classe.py : MIREILLE et DANIÈLE partagent une
  // voix et ne se répondent jamais, parce qu'elles ne paraissent pas dans le
  // même dialogue.

  prep: {
    label: "Dialogue — L'annonce, un lundi matin",
    lines: [
      ["MIREILLE","Bon. Avant qu'on ouvre le cahier, j'ai quelque chose à vous annoncer, et j'aime autant vous le dire tout de suite : ça va durer trois semaines."],
      ["MARISOL","Trois semaines de quoi, madame ?"],
      ["MIREILLE","D'un travail de recherche. En équipe de trois. Chaque équipe choisit un sujet dans une liste, cherche de l'information, écrit un court texte et vient présenter ce qu'elle a trouvé devant la classe."],
      ["YOUSSEF","Un exposé ? Devant tout le monde ?"],
      ["MIREILLE","Un compte rendu, plutôt. Cinq minutes par équipe. Ce n'est pas un concours : personne ne va vous demander d'être drôle. On veut savoir ce que vous avez trouvé et d'où ça vient."],
      ["MARISOL","Et le sujet, on le choisit vraiment ? Ou bien il est déjà choisi et vous nous laissez croire qu'on choisit ?"],
      ["MIREILLE","Vous choisissez vraiment. Il y a huit sujets sur la feuille et ils touchent tous la ville : la collecte des matières organiques, le transport en commun, les bibliothèques de quartier, l'eau potable… Prenez celui qui vous fâche ou celui qui vous intrigue, ça revient au même."],
      ["YOUSSEF","Celui qui nous fâche ?"],
      ["MIREILLE","Un sujet qui ne vous fait rien du tout, vous allez l'abandonner à la deuxième journée. Je préfère vous le dire avant que vous choisissiez au hasard."],
      ["MARISOL","Moi, je prendrais le bac brun. Ça fait deux ans que j'en ai un sur mon balcon et je ne sais toujours pas ce qui a le droit d'aller dedans."],
      ["MIREILLE","Voilà exactement le genre de départ que je cherche. Une question à laquelle vous n'avez pas la réponse, pas un sujet dont vous savez déjà tout."],
      ["YOUSSEF","Je veux bien me mettre avec Marisol. Mais on cherche où, l'information ? Sur Internet, il y a tout et le contraire de tout."],
      ["MIREILLE","C'est justement une partie du travail. Vous aurez trois sources au minimum, et pas trois fois la même. Madame Ouimet, à la bibliothèque du centre, vous montrera comment on juge une source. Elle vous attend jeudi après-midi."],
      ["MARISOL","Trois sources différentes… Une page de la ville, un article de journal, ça compte ?"],
      ["MIREILLE","Ça compte, et ce sont deux genres très différents : la ville explique ce qu'elle a décidé, le journal raconte ce qui s'est passé. Une lettre de lecteur compte aussi, mais elle ne dit pas la même chose : elle dit ce que quelqu'un en pense."],
      ["YOUSSEF","Et si les trois ne disent pas la même chose ?"],
      ["MIREILLE","Alors vous aurez enfin quelque chose à écrire. Un travail où tout le monde est d'accord n'apprend rien à personne. Ce que je veux lire, c'est : voici ce que dit l'un, voici ce que dit l'autre, et voici pourquoi ils ne s'entendent pas."],
      ["MARISOL","Ça me semble beaucoup pour trois semaines."],
      ["MIREILLE","Ce sera beaucoup si vous commencez la dernière fin de semaine. La consigne est écrite au complet : la feuille fait une page et demie, elle donne les étapes, l'échéance et la grille d'évaluation. Lisez-la ce soir, au complet, avant de choisir votre sujet."],
      ["YOUSSEF","La grille aussi ? On sait d'avance comment vous allez nous noter ?"],
      ["MIREILLE","Toujours. Je n'ai jamais compris qu'on cache ça aux gens. Vous verrez : ce n'est pas la longueur qui compte, c'est l'organisation. Prenez la feuille en sortant."],
    ]
  },

  t1: {
    label: "Dialogue — La consigne, ligne par ligne",
    lines: [
      ["MARISOL","Madame, on a lu la feuille tous les deux et on n'est pas d'accord sur ce qu'il faut remettre."],
      ["MIREILLE","Assoyez-vous. Ça arrive à toutes les équipes, et c'est pour ça que je reste une demi-heure après le cours cette semaine. Sur quoi vous n'êtes pas d'accord ?"],
      ["YOUSSEF","Sur le nombre de textes. Moi je comprends qu'on remet un seul document. Marisol pense qu'il y en a deux."],
      ["MIREILLE","Relisez-moi la deuxième ligne du paragraphe deux, celle qui commence par « chaque équipe remettra »."],
      ["MARISOL","« Chaque équipe remettra un texte de deux pages et le plan qui a servi à l'écrire. »"],
      ["MIREILLE","Deux documents, donc. Le texte et le plan. Youssef, tu as lu trop vite, et je ne t'en blâme pas : cette phrase-là est une phrase de consigne, et une consigne ne se lit pas comme un roman."],
      ["YOUSSEF","Elle se lit comment ?"],
      ["MIREILLE","Une ligne à la fois, avec un crayon. Chaque fois qu'un verbe vous dit de faire quelque chose, vous le soulignez. Il y en a sept dans ma feuille, et je les ai comptés."],
      ["MARISOL","Il y a aussi une chose que je ne comprends pas. C'est écrit « vous choisirez votre sujet avant le 3 novembre ». Ce n'est pas une question de ce qui va arriver, ça. C'est un ordre."],
      ["MIREILLE","C'en est un. Dans un document écrit, le futur donne souvent un ordre poli. « Vous choisirez » veut dire « choisissez ». C'est la même chose partout : sur un avis, sur une convocation, sur un formulaire d'hôpital."],
      ["YOUSSEF","Et l'ordre des étapes ? Il n'y a pas de « premièrement », pas de « ensuite ». On dirait que tout arrive en même temps."],
      ["MIREILLE","Regardez mieux. La consigne dit « une fois le sujet approuvé, l'équipe cherchera trois sources ». Le mot « une fois » vous dit ce qui vient avant quoi. Il y en a d'autres : « avant de », « dès que », « sans avoir ». Ce ne sont pas des connecteurs de temps ordinaires, mais ils font le même travail."],
      ["MARISOL","Donc on ne peut pas chercher les sources tout de suite."],
      ["MIREILLE","Vous pouvez, mais vous risquez de chercher pour un sujet que je vais vous refuser. Ce serait dommage."],
      ["YOUSSEF","Parlez-nous de la grille. Il y a quatre lignes et je ne comprends pas la dernière : « organisation du texte, quatre points ». Qu'est-ce que vous regardez, exactement ?"],
      ["MIREILLE","Trois choses. Un paragraphe par idée principale. Un blanc entre les paragraphes. Et des mots qui relient une idée à la suivante — « par exemple », « c'est-à-dire », « notamment ». Un texte juste mais mal découpé perd les quatre points, et ça se produit toutes les sessions."],
      ["MARISOL","Quatre points sur combien ?"],
      ["MIREILLE","Sur vingt. Le contenu en vaut huit, les sources quatre, la langue quatre, l'organisation quatre. Ce n'est pas moi qui l'ai décidé, c'est écrit dans la feuille, et c'est écrit d'avance justement pour que vous puissiez viser."],
      ["YOUSSEF","Dernière question. Si on ne trouve que deux sources ?"],
      ["MIREILLE","Venez me voir avant l'échéance, pas après. Un texte à deux sources remis à temps avec un mot d'explication, ça se discute. Un texte remis en retard, non : la feuille dit « aucun travail ne sera reçu après le 24 novembre », et cette phrase-là, je la respecte pour tout le monde."],
    ]
  },

  t2: {
    label: "Dialogue — Trois sources qui ne disent pas la même chose",
    lines: [
      ["DANIÈLE","Alors, l'équipe du bac brun. Vous avez apporté ce que vous avez trouvé ?"],
      ["MARISOL","Trois documents. Mais plus on les lit, moins on comprend."],
      ["DANIÈLE","C'est bon signe. Étalez-les. On va les regarder un par un, et je vais vous poser à chaque fois les deux mêmes questions : qui parle, et qu'est-ce que cette personne veut ?"],
      ["YOUSSEF","Le premier vient du site de la ville. C'est une page qui explique la collecte : ce qu'on met dans le bac, ce qu'on n'y met pas, et pourquoi."],
      ["DANIÈLE","Qui parle, donc ?"],
      ["YOUSSEF","La ville."],
      ["DANIÈLE","Et qu'est-ce qu'elle veut ? Elle veut que la collecte fonctionne. Ce n'est pas un défaut, c'est un fait à savoir : cette page vous donnera très bien la liste des matières acceptées, et elle ne vous dira jamais ce qui a mal marché la première année."],
      ["MARISOL","Le deuxième, c'est un article du bulletin municipal du printemps passé. Il raconte l'histoire de la collecte depuis le début. C'est écrit d'une drôle de façon : « le conseil adopta le règlement », « les premiers bacs arrivèrent en avril »."],
      ["DANIÈLE","Le passé simple. On ne le parle jamais et on l'écrit encore souvent, dans les historiques surtout. Traduisez-le en passé composé dans votre tête et continuez : « le conseil a adopté », « les bacs sont arrivés »."],
      ["MARISOL","J'ai buté sur une phrase. « La ville avait distribué les bacs en avril, mais la collecte ne commença qu'en juin. »"],
      ["DANIÈLE","Deux moments passés, et l'un est avant l'autre. « Avait distribué » se place avant « commença ». Les gens ont donc eu un bac vide sur leur balcon pendant deux mois, et c'est exactement le genre de détail qui fait un bon travail de recherche."],
      ["YOUSSEF","Le troisième, c'est une lettre. Une dame écrit au bulletin pour dire que le compostage ne sert à rien parce que tout le monde met n'importe quoi dans le bac."],
      ["DANIÈLE","Qui parle ?"],
      ["YOUSSEF","Une lectrice."],
      ["DANIÈLE","Et qu'est-ce qu'elle veut ? Elle veut convaincre. Ce n'est pas une source de faits, c'est une source d'opinions — et vous en avez besoin, à condition de la présenter pour ce qu'elle est. « Selon une lectrice du bulletin », et non « la collecte ne sert à rien »."],
      ["MARISOL","Mais alors, laquelle des trois a raison ?"],
      ["DANIÈLE","Aucune ne ment. La ville décrit une règle, le bulletin raconte ce qui est arrivé, la lectrice donne son avis. Vous les mettez côte à côte, vous notez à quel endroit elles se contredisent, et vous l'écrivez. C'est ça, votre travail — pas de choisir un gagnant."],
      ["YOUSSEF","Il nous faut aussi noter d'où viennent les phrases qu'on recopie."],
      ["DANIÈLE","Toujours. Le titre du document, qui l'a publié, la date. Faites-le pendant que vous lisez : retrouver la page où vous avez pris une phrase, trois jours plus tard, prend plus de temps que de l'avoir notée."],
      ["MARISOL","Une dernière chose. Est-ce qu'on peut recopier une phrase telle quelle ?"],
      ["DANIÈLE","Entre guillemets, avec la source, oui, une ou deux. Le reste, vous le dites dans vos mots. Un travail fait de phrases recopiées se voit à trois mètres, et il ne vous apprend rien."],
    ]
  },
};
