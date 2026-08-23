const DIALOGUES = {
  // Quatre dialogues longs — le niveau 7 vise « des discours détaillés et
  // structurés », et les deux intentions orales de la situation sont des
  // échanges tenus : une entrevue, un appel de suivi. Ils se travaillent en
  // écoutes successives : une fois pour le fil, une fois pour les chiffres et
  // les dates, une fois pour ce qui n'est pas dit.
  //
  // Cinq personnages, quatre voix, et les locuteurs ont été comptés **par
  // extrait avant l'écriture** : aucun extrait ne réunit trois personnes du
  // même genre. RANIA parle dans les quatre ; GHYSLAINE et NADINE ne se
  // rencontrent jamais et partagent donc un timbre ; YVAN n'apparaît que dans
  // l'entrevue, où il répond à ÉMILIEN — deux voix masculines distinctes.
  //
  // Un seul dialogue est au tutoiement, celui des deux collègues.

  prep: {
    label: "Dialogue — Le dîner de midi et quart",
    lines: [
      ["RANIA","Ghyslaine, tu as deux minutes ? Je voudrais te demander quelque chose, et je ne sais pas à qui d'autre le demander."],
      ["GHYSLAINE","Assis-toi. J'ai jusqu'à moins vingt. Qu'est-ce qui se passe ?"],
      ["RANIA","Rien de grave. C'est pour le diplôme. Le programme de santé, assistance et soins infirmiers, au centre de formation. Je veux le faire."],
      ["GHYSLAINE","Ah oui ? Bon. Ça fait combien de temps que tu es préposée, toi, cinq ans ?"],
      ["RANIA","Cinq ans en novembre. Et deux ans d'école en Syrie avant, en soins infirmiers. Je n'ai pas fini : l'école a fermé."],
      ["GHYSLAINE","Tu ne me l'avais jamais dit, ça."],
      ["RANIA","On ne me l'a jamais demandé. Et puis mon relevé de notes est en arabe, avec une traduction. Personne ne sait quoi en faire ici."],
      ["GHYSLAINE","Tu vas t'inscrire quand ?"],
      ["RANIA","C'est là que ça se complique. Je pensais que je remplissais un formulaire et que j'attendais une lettre. Mais j'ai appelé, et la dame m'a dit qu'il y avait une entrevue."],
      ["GHYSLAINE","Une entrevue de sélection. Oui. Le programme est contingenté."],
      ["RANIA","Contingenté, ça veut dire quoi exactement ?"],
      ["GHYSLAINE","Ça veut dire qu'il y a plus de monde qui demande que de places. Ma nièce l'a fait il y a trois ans : ils recevaient à peu près soixante-dix demandes pour vingt-quatre places."],
      ["RANIA","Soixante-dix pour vingt-quatre. Donc ils en refusent deux sur trois."],
      ["GHYSLAINE","À peu près. Et ce n'est pas juste les notes qui décident. Il y a le dossier, la lettre, puis la rencontre."],
      ["RANIA","La lettre ? Quelle lettre ?"],
      ["GHYSLAINE","La lettre de motivation. Tu écris pourquoi tu veux entrer, ce que tu as fait avant, où tu t'en vas après. Une page."],
      ["RANIA","Une page pour dire que je veux le diplôme ? Je peux l'écrire ce soir."],
      ["GHYSLAINE","C'est ce que tout le monde pense, puis c'est là que ça accroche. Ils en lisent soixante-dix, des lettres. Elles disent toutes la même affaire : j'aime aider les gens, j'ai toujours voulu travailler en santé."],
      ["RANIA","Et ce n'est pas vrai ?"],
      ["GHYSLAINE","C'est vrai pour les soixante-dix. C'est justement le problème. Ce qu'il faut qu'ils lisent, c'est pourquoi toi — pas pourquoi le métier."],
      ["RANIA","Cinq ans à l'étage, deux ans d'école, quinze mots d'arabe qui servent avec madame Khoury quand elle panique. Ça, c'est à moi."],
      ["GHYSLAINE","Ça, ça se lit. Écris ça, puis fais-la relire par quelqu'un du centre avant de l'envoyer."],
      ["RANIA","Ils font ça, relire une lettre avant de la recevoir ?"],
      ["GHYSLAINE","Le conseiller pédagogique le fait. Il ne te corrigera pas tes fautes, mais il va te dire ce qui manque. Appelle-le. Le pire qu'il peut te dire, c'est non."],
    ]
  },

  t1: {
    label: "Dialogue — Ce que la lettre ne dit pas",
    lines: [
      ["ÉMILIEN","Centre de formation professionnelle du Ruisseau-Vert, Émilien Fiset, bonjour."],
      ["RANIA","Bonjour, monsieur Fiset. Rania Nassar. Je vous ai envoyé un courriel jeudi au sujet du programme de santé, assistance et soins infirmiers."],
      ["ÉMILIEN","Oui, madame Nassar, j'ai votre lettre devant moi. Merci de me l'avoir envoyée avant le dépôt : c'est rare, et c'est une bonne idée."],
      ["RANIA","Est-ce qu'elle est correcte ?"],
      ["ÉMILIEN","Elle est bien écrite. Ce n'est pas la question que je me poserais à votre place."],
      ["RANIA","Quelle question, alors ?"],
      ["ÉMILIEN","Celle que le comité se pose en la lisant : qu'est-ce qui, dans cette lettre-là, n'aurait pas pu être écrit par quelqu'un d'autre ? Là, tout aurait pu l'être."],
      ["RANIA","Pourtant, tout ce que j'ai écrit est vrai."],
      ["ÉMILIEN","Je n'en doute pas une seconde. Regardez votre deuxième paragraphe : « je suis une personne responsable, patiente et à l'écoute ». Trois adjectifs. Un comité en lit deux cents par année."],
      ["RANIA","Qu'est-ce que je devrais écrire à la place ?"],
      ["ÉMILIEN","Ce qui les a produits. Vous êtes préposée depuis cinq ans, si je lis bien ?"],
      ["RANIA","Cinq ans en novembre. Aux Quatre-Vents, à l'unité prothétique."],
      ["ÉMILIEN","Alors écrivez l'unité prothétique. Écrivez cinq ans. Un fait daté vaut trois adjectifs, et il ne se conteste pas."],
      ["RANIA","Et pour mes deux années d'études en Syrie ? Je ne sais pas comment le dire. Je n'ai pas de diplôme."],
      ["ÉMILIEN","Vous le dites exactement comme vous venez de me le dire : deux années faites, pas de diplôme, l'école a fermé. On ne cache pas un trou dans un dossier, on l'explique en une phrase et on passe à la suite. Ce qui inquiète un comité, ce n'est pas le trou, c'est de le découvrir tout seul."],
      ["RANIA","Est-ce que ces deux années-là comptent pour quelque chose ?"],
      ["ÉMILIEN","Pour l'admission, non : ce sont les préalables du secondaire d'ici qui décident, et ça se règle avec le service d'accueil. Pour le comité, oui — ça dit que vous savez ce qu'est un cours de soins et que vous n'idéalisez pas le métier."],
      ["RANIA","Bon. Et le reste de la lettre ? Le début, la fin ?"],
      ["ÉMILIEN","Votre objet est trop long, il fait deux lignes. Un objet, c'est six ou sept mots. Et vous finissez par « merci beaucoup pour votre temps » : ce n'est pas une formule de courtoisie, c'est une formule de reconnaissance."],
      ["RANIA","Quelle est la différence ?"],
      ["ÉMILIEN","Une formule de courtoisie vous laisse debout. « Veuillez agréer, Madame, Monsieur, mes salutations distinguées. » Vous remerciez d'avance de quelque chose qui ne vous a pas encore été accordé, et ça se sent."],
      ["RANIA","Est-ce que je peux vous demander une dernière chose ? Combien de paragraphes ?"],
      ["ÉMILIEN","Trois, et un par idée. Le premier dit ce que vous demandez et pourquoi ce programme-ci. Le deuxième dit ce que vous apportez, avec des faits. Le troisième dit où vous allez après le diplôme, et ce que vous faites déjà pour y arriver."],
      ["RANIA","Où je vais après. Je n'y avais pas pensé, à celui-là."],
      ["ÉMILIEN","C'est pourtant celui qui vous distingue. Une formation contingentée cherche des gens qui finissent, pas des gens qui commencent. Réécrivez-la, et déposez-la avant le premier mars."],
    ]
  },

  t2: {
    label: "Dialogue — Vingt-cinq minutes, mardi neuf heures quinze",
    lines: [
      ["ÉMILIEN","Madame Nassar, bonjour. Émilien Fiset, on s'est parlé au téléphone. Je vous présente Yvan Lemay, infirmier auxiliaire et enseignant du programme."],
      ["YVAN","Bonjour. C'est moi qui vous aurai devant moi en classe, si ça marche."],
      ["RANIA","Bonjour, monsieur Lemay. Merci de me recevoir."],
      ["ÉMILIEN","On a vingt-cinq minutes. Il n'y a pas de piège dans nos questions : on veut comprendre votre parcours et savoir si le programme vous convient. Commençons simplement. Pourquoi ce diplôme-là, et pourquoi maintenant ?"],
      ["RANIA","Je suis préposée aux bénéficiaires depuis cinq ans. Ce que je fais aujourd'hui, je le fais bien, mais je m'arrête toujours au même endroit : quand il faut donner un médicament, faire un pansement ou noter un signe, je vais chercher quelqu'un d'autre. Je veux être celle qu'on va chercher."],
      ["YVAN","Vous savez ce que ça change, comme responsabilité ?"],
      ["RANIA","Une partie, oui. Je vous vois travailler tous les jours. Ce que je ne connais pas, c'est ce qui se passe quand une décision est mauvaise et qu'elle est la mienne."],
      ["YVAN","C'est la bonne réponse, et c'est la seule qui compte pour moi. Continuez."],
      ["ÉMILIEN","Vous avez fait deux ans en soins infirmiers à Alep. Racontez-nous."],
      ["RANIA","Deux années terminées sur quatre. L'école a fermé au milieu de la troisième. Je n'ai pas de diplôme, seulement un relevé de notes traduit. Je ne demande pas qu'on me les reconnaisse : je dis que je sais ce qu'est un cours d'anatomie et ce qu'est un examen pratique."],
      ["ÉMILIEN","Vous seriez prête à recommencer une matière que vous avez déjà faite ?"],
      ["RANIA","Bien que je l'aie déjà faite, je la referais sans discuter. En cinq ans, la moitié a changé, et l'autre moitié, je l'ai apprise en arabe."],
      ["YVAN","Parlons de l'horaire. La formation est à temps plein, il y a des stages, et vous travaillez. Comment vous organisez-vous ?"],
      ["RANIA","J'ai parlé à ma coordonnatrice avant de déposer mon dossier. Je passe de cinq quarts à deux, les fins de semaine, à partir de septembre. Ma fille a quinze ans, mon garçon en a onze, et ma sœur habite à trois rues."],
      ["ÉMILIEN","Donc c'est déjà réglé ?"],
      ["RANIA","C'est écrit. Même si ça reste serré, je préfère un horaire serré et prévu à un horaire large qu'on n'a pas préparé."],
      ["YVAN","Une dernière chose de mon côté. Le stage se fait dans un établissement de la région, et on vous y verra en début de formation. Qu'est-ce qui va être le plus dur pour vous ?"],
      ["RANIA","Écrire. Parler avec un patient, ça va ; noter au dossier, c'est autre chose. J'écris lentement et je vérifie tout deux fois."],
      ["YVAN","Vous vérifiez deux fois. Ce n'est pas un défaut dans notre métier."],
      ["RANIA","Ce n'est pas un défaut, mais ça prend du temps, et le temps, il n'y en a pas. C'est pour ça que je suis un cours de français le mercredi soir depuis janvier."],
      ["ÉMILIEN","Vous avez des questions pour nous ?"],
      ["RANIA","Trois. Est-ce que les cours du premier bloc sont donnés le jour, toute la semaine ?"],
      ["ÉMILIEN","Le jour, du lundi au vendredi, de huit heures à quinze heures trente."],
      ["RANIA","Deuxièmement, pourriez-vous me dire à quel moment le stage commence dans l'année ?"],
      ["YVAN","Le premier stage est court et il arrive tôt, avant Noël. C'est voulu : ceux à qui le métier ne convient pas le savent avant d'avoir investi un an."],
      ["RANIA","Et si je ne suis pas retenue cette fois-ci, qu'est-ce que je peux faire d'ici l'an prochain pour que mon dossier soit plus fort ?"],
      ["ÉMILIEN","Ça, c'est une question qu'on ne nous pose jamais. Je vous répondrai, mais pas aujourd'hui : rappelez-moi après la décision."],
    ]
  },

  t3: {
    label: "Dialogue — Personne ne s'occupe de ça",
    lines: [
      ["NADINE","Centre de formation professionnelle du Ruisseau-Vert, bonjour."],
      ["RANIA","Bonjour. Rania Nassar, dossier 41-2887. J'appelle au sujet de la lettre que j'ai reçue lundi pour le programme de santé, assistance et soins infirmiers."],
      ["NADINE","Oui, madame. Qu'est-ce que je peux faire pour vous ?"],
      ["RANIA","La lettre dit que ma candidature est retenue et que je suis inscrite sur la liste d'attente. Elle ne dit rien d'autre. Je voudrais savoir à quel rang je suis."],
      ["NADINE","Le rang ne se communique pas, madame. Ce n'est pas moi qui décide de ça : c'est la même réponse pour tout le monde."],
      ["RANIA","Je comprends. Est-ce que quelqu'un s'occupe des personnes qui sont sur la liste ?"],
      ["NADINE","Personne ne s'en occupe comme telle. La liste bouge toute seule : quand une personne admise se désiste, on appelle la suivante."],
      ["RANIA","Donc si je ne fais rien, il ne se passe rien, et si je fais quelque chose, il ne se passe rien non plus ?"],
      ["NADINE","Dit comme ça, ce n'est pas très encourageant. Mais oui, c'est à peu près ça."],
      ["RANIA","Est-ce que je peux vous demander une chose alors ? Monsieur Fiset m'avait dit, à la fin de mon entrevue, de le rappeler après la décision. Est-ce qu'il est là ?"],
      ["NADINE","Il est en rencontre jusqu'à onze heures. Je peux lui laisser un message. Vous voulez que je lui dise quoi exactement ?"],
      ["RANIA","Que Rania Nassar a rappelé comme il l'avait demandé, au sujet du dossier 41-2887, et qu'elle veut savoir ce qu'elle peut faire d'ici l'an prochain. Mon numéro est le quatre cent cinquante, cinq cent cinquante-cinq, zéro un quatre-vingt-douze."],
      ["NADINE","Quatre cent cinquante, cinq cent cinquante-cinq, zéro un quatre-vingt-douze. C'est noté, madame Nassar. Il rappelle toujours."],
      ["ÉMILIEN","Madame Nassar ? Émilien Fiset, du Ruisseau-Vert. On m'a remis votre message."],
      ["RANIA","Merci de me rappeler, monsieur Fiset. Je serai brève : je vous appelle au sujet de la décision du dix avril. Vous m'aviez dit, à la fin de l'entrevue, que vous me diriez ce que je peux faire d'ici l'an prochain."],
      ["ÉMILIEN","Je m'en souviens très bien. Vous nous aviez demandé si le stage arrivait tôt, et monsieur Lemay vous avait répondu qu'il arriverait avant Noël. Votre entrevue s'est très bien passée, je vous le dis franchement."],
      ["RANIA","Alors qu'est-ce qui a manqué ?"],
      ["ÉMILIEN","Rien n'a manqué. Il y avait vingt-quatre places et quarante et une candidatures retenues. Ceux qui sont passés devant vous avaient tous leur préalable de mathématiques, et vous ne l'avez pas encore."],
      ["RANIA","Donc ce n'est ni l'entrevue ni la lettre. C'est une seule case."],
      ["ÉMILIEN","Une seule case, oui. Et c'est une bonne nouvelle, parce qu'une case, ça se remplit."],
      ["RANIA","Si je faisais la mise à niveau en mathématiques d'ici décembre, est-ce que ça changerait mon rang ?"],
      ["ÉMILIEN","Ça ne changerait pas votre rang sur la liste de cette année-là — la liste de cette année est fermée. Ça changerait votre dossier pour l'entrée de janvier, et pour celle de l'automne prochain, où vous ne seriez plus dans la même catégorie."],
      ["RANIA","Il y a une entrée en janvier ?"],
      ["ÉMILIEN","Il y en a une, plus petite, et elle se remplit surtout avec la liste d'attente. Je ne vous promets rien du tout : je vous dis qu'une personne qui a son préalable au mois de décembre n'est pas la même candidate qu'aujourd'hui."],
      ["RANIA","Quant à mes cinq ans comme préposée, est-ce qu'il y a moyen de les faire compter ?"],
      ["ÉMILIEN","Il y a une démarche pour ça, la reconnaissance des acquis. Elle ne fait pas entrer dans un programme contingenté, mais elle peut faire reconnaître des compétences une fois qu'on y est. Je vous envoie le nom de la personne responsable par courriel aujourd'hui."],
      ["RANIA","Autrement dit : je m'inscris à la mise à niveau cette semaine, je vous rappelle en décembre avec le résultat, et je regarde la reconnaissance des acquis en parallèle."],
      ["ÉMILIEN","C'est exactement ça. Et rappelez-moi en décembre, pas en février : les dossiers de l'entrée de janvier se regardent à la mi-décembre."],
    ]
  },
};
