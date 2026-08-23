const DIALOGUES = {
  // Niveau 7 : la compétence vise des discours étendus et structurés. Les
  // quatre extraits ci-dessous font de dix-huit à vingt et une répliques,
  // dont plusieurs de quatre ou cinq phrases — la présentation de Renaud au
  // Défi 1 et celle d'Aïcha au Défi 2 sont des monologues coupés de
  // questions, pas des saynètes. Ils se travaillent en écoutes successives.
  //
  // Quatre personnages, quatre voix, aucun croisement problématique :
  //   prep  AÏCHA, THÉRÈSE          t1  RENAUD, AÏCHA, THÉRÈSE
  //   t2    AÏCHA, RENAUD, THÉRÈSE  t3  AÏCHA, VINCENT
  prep: {
    label: "Dialogue — Se plaindre, ce n'est pas présenter un projet",
    lines: [
      ["AÏCHA","Thérèse, tu as deux minutes ? Je voudrais te montrer quelque chose avant que tu partes."],
      ["THÉRÈSE","Vas-y, mon dîner attendra. Qu'est-ce que tu as là ?"],
      ["AÏCHA","Une feuille que j'ai remplie toute seule, hier soir, à la maison. J'ai compté ce qui se passe au poste 4 depuis le mois de mars."],
      ["THÉRÈSE","Le poste d'emballage. Celui où les caisses se ramassent à terre."],
      ["AÏCHA","Exactement. Trois personnes se sont fait mal au dos depuis le printemps. Jean-Marc a manqué onze jours. Et personne n'en parle, parce que tout le monde trouve que c'est normal."],
      ["THÉRÈSE","Ce n'est pas normal, et tu le sais aussi bien que moi. Qu'est-ce que tu comptes en faire, de ta feuille ?"],
      ["AÏCHA","C'est là que je bloque. Si je vais voir monsieur Cormier et que je lui dis que le poste 4 est mal fait, il va m'écouter deux minutes et passer à autre chose."],
      ["THÉRÈSE","Il va t'écouter deux minutes, oui. Parce que ce que tu viens de me décrire, ce n'est pas encore un projet. C'est une plainte."],
      ["AÏCHA","Une plainte. Le mot est dur."],
      ["THÉRÈSE","Il n'est pas dur, il est exact, et ce n'est pas une critique. Une plainte, ça dit ce qui ne va pas et ça s'arrête là. Un projet, ça dit ce qui ne va pas, ce que ça coûte, ce qu'on fait à la place, combien ça coûte et quand. Cinq choses, pas une."],
      ["AÏCHA","Cinq choses. Redis-les-moi lentement, je les écris."],
      ["THÉRÈSE","Le constat. La cause. La conséquence, en chiffres si tu en as. Le correctif que tu proposes. Et l'échéance. Si une des cinq manque, ton monde va la chercher pendant que tu parles, et ils n'écouteront plus le reste."],
      ["AÏCHA","J'ai le constat et j'ai les chiffres. La cause aussi, je pense : les caisses arrivent à terre sur une palette et il faut se pencher quatre-vingts fois par quart."],
      ["THÉRÈSE","Ça, c'est de la manutention manuelle, et c'est justement ce qu'un programme de prévention est censé regarder. On en a un, ici. Il est obligatoire depuis qu'on a passé vingt travailleurs, et il se met à jour tous les ans."],
      ["AÏCHA","Je ne savais même pas qu'il existait."],
      ["THÉRÈSE","Il existe, il est dans le classeur du bureau de monsieur Cormier, et moi je suis représentante en santé et en sécurité — c'est les travailleurs qui m'ont élue, ce n'est pas la direction qui m'a nommée. Alors ta feuille, elle m'intéresse beaucoup."],
      ["AÏCHA","Donc je ne suis pas toute seule avec mon papier."],
      ["THÉRÈSE","Tu n'es pas toute seule, mais il va falloir que tu parles, et que tu parles bien. Lundi matin, il y a la réunion de production. Monsieur Cormier présente son projet de quai. Écoute-le comme si tu prenais des notes pour l'école."],
      ["AÏCHA","Pourquoi ? Son quai ne me concerne pas."],
      ["THÉRÈSE","Son quai, non. Sa façon de le présenter, oui. Tu vas voir dans quel ordre il met les choses, quels mots il emploie pour passer d'une partie à l'autre, et à quel moment il donne ses chiffres. Tu feras pareil pour le tien, deux semaines plus tard."],
      ["AÏCHA","Donc j'apprends en écoutant quelqu'un d'autre."],
      ["THÉRÈSE","C'est comme ça que tout le monde apprend, Aïcha. Personne n'est né en sachant présenter un projet. Apporte ta feuille lundi, et assieds-toi en avant."]
    ]
  },

  t1: {
    label: "Dialogue — La réunion de production du lundi",
    lines: [
      ["RENAUD","Bon. Il est huit heures cinq, tout le monde est là, on commence. Vous avez l'ordre du jour devant vous. Premier point : le réaménagement du quai d'expédition. J'en ai pour une douzaine de minutes, et je répondrai aux questions après."],
      ["RENAUD","Je vous rappelle d'abord pourquoi on en parle. Depuis janvier, on charge en moyenne dix-neuf camions par jour, contre quatorze l'an dernier. Le quai, lui, n'a pas changé depuis 2009. Résultat : les camions attendent, et quand un camion attend, le transporteur nous facture."],
      ["RENAUD","L'objectif du projet tient en une phrase : ramener le temps d'attente moyen sous les vingt minutes, sans agrandir le bâtiment. Je le répète parce que c'est ce qui va décider de tout le reste — on ne construit rien, on réorganise."],
      ["THÉRÈSE","Vingt minutes, c'est la moyenne ou c'est le maximum ?"],
      ["RENAUD","La moyenne. Bonne question, je l'écris. Le maximum, on ne peut pas le garantir, il y a des jours où trois camions arrivent en même temps."],
      ["RENAUD","Ensuite, les étapes. Il y en a quatre. D'abord, on mesure : deux semaines de relevés, chaque camion chronométré, du moment où il se présente à la barrière jusqu'à son départ. Ensuite, on trace : un plan à l'échelle avec les nouvelles zones d'attente. Puis on essaie : un mois à l'essai, sans rien acheter, juste avec du ruban jaune au sol. Enfin, on installe pour de bon si l'essai est concluant."],
      ["AÏCHA","Pourquoi mesurer d'abord ? On sait déjà que ça bloque."],
      ["RENAUD","On sait que ça bloque, mais on ne sait pas où. Tout le monde a son idée là-dessus et personne n'a les mêmes chiffres. Une fois qu'on aura deux semaines de relevés, on ne discutera plus d'impressions. C'est la partie la moins spectaculaire du projet et c'est la plus importante."],
      ["RENAUD","Pour l'échéancier, maintenant. Les relevés commencent le 8 septembre et se terminent le 19. Le plan sera prêt pour la réunion du 6 octobre. L'essai courra du 13 octobre au 14 novembre. Et quand l'essai sera terminé, on décidera — pas avant."],
      ["THÉRÈSE","Donc rien n'est acheté avant la mi-novembre."],
      ["RENAUD","Rien du tout. C'est voulu. Le jour où j'irai demander de l'argent à la direction, je veux pouvoir dire que la solution a déjà fonctionné pendant un mois dans notre cour."],
      ["RENAUD","Le budget, justement. L'essai coûte quatre cents dollars : du ruban, des cônes, deux panneaux. L'installation définitive, si on y va, est estimée entre onze et treize mille dollars, surtout du marquage au sol et une deuxième porte de quai. Je précise « estimée » : je n'ai pas encore de soumission, seulement un prix approximatif donné au téléphone."],
      ["AÏCHA","Et si l'essai ne marche pas ?"],
      ["RENAUD","Alors on aura dépensé quatre cents dollars et on saura pourquoi ça ne marche pas. Ce n'est pas un échec, c'est un résultat. Ce qui serait un échec, c'est de dépenser treize mille dollars et de découvrir ça après."],
      ["RENAUD","Les risques, pour finir. Il y en a trois, et je préfère les nommer moi-même. Le premier : pendant l'essai, la circulation dans la cour change, et un piéton distrait peut se retrouver dans une zone de manœuvre. Le deuxième : les deux semaines de relevés tombent en pleine rentrée, notre période la plus chargée. Le troisième : si un des deux transporteurs refuse la nouvelle zone d'attente, tout le plan est à refaire."],
      ["THÉRÈSE","Le premier risque, je veux qu'il soit noté au procès-verbal. Une zone de manœuvre modifiée, ça se signale à tout le monde, pas juste aux caristes."],
      ["RENAUD","Noté, et vous avez raison de le demander. Je vous propose qu'on regarde ça ensemble avant le 13 octobre."],
      ["RENAUD","En somme : on mesure, on trace, on essaie, on installe. Deux mois et demi, quatre cents dollars pour savoir, et une décision en novembre avec des chiffres à l'appui. Voilà. Des questions ?"],
      ["AÏCHA","Une question, monsieur Cormier. Quand vous aurez fini vos relevés, est-ce que les résultats seront affichés ?"],
      ["RENAUD","Ils seront affichés au babillard de la cafétéria, oui, et je les présenterai ici le 6 octobre. Je n'ai aucune envie de garder ça dans mon bureau : ce sont vos temps d'attente autant que les miens."],
      ["THÉRÈSE","Monsieur Cormier, avant qu'on passe au point deux : est-ce qu'il reste de la place à l'ordre du jour d'une prochaine réunion ? Aïcha a un dossier à présenter."],
      ["RENAUD","Il en reste. Madame Traoré, vous avez quinze minutes le 15 septembre si vous les voulez. Dites-moi d'ici vendredi."]
    ]
  },

  t2: {
    label: "Dialogue — Ce qui se passe au poste 4",
    lines: [
      ["AÏCHA","Merci. Comme monsieur Cormier l'a annoncé, j'ai quinze minutes pour vous parler du poste 4, celui de l'emballage. Je vais faire comme lui : le constat, la cause, ce que ça coûte, ce que je propose, et une date."],
      ["AÏCHA","Le constat, d'abord. Depuis le mois de mars, trois personnes du poste 4 ont consulté pour le dos. Jean-Marc a été absent onze jours ouvrables, Suzanne quatre, et Kadiatou travaille en tâches allégées depuis le 2 juin. Ce sont des jours que j'ai comptés dans le registre, pas des impressions."],
      ["RENAUD","Trois personnes sur combien, au poste 4 ?"],
      ["AÏCHA","Sur cinq. C'est ce qui m'a fait commencer à compter, justement."],
      ["AÏCHA","La cause, maintenant. Les caisses vides arrivent sur une palette, posées à terre. L'emballeur se penche, prend la caisse, se relève, la remplit à hauteur de poitrine, puis la repose sur une deuxième palette, à terre encore. J'ai compté quatre-vingt-deux caisses par quart en moyenne, sur six quarts différents. Ce qui use le dos, ce n'est pas le poids d'une caisse, c'est de se pencher quatre-vingt-deux fois."],
      ["THÉRÈSE","C'est exactement ce que la manutention manuelle répétitive veut dire. C'est nommé dans notre programme de prévention, section 3."],
      ["AÏCHA","Merci, Thérèse, j'y arrive. Les conséquences, en chiffres. Quinze jours ouvrables d'absence depuis mars, plus un poste en tâches allégées depuis onze semaines. Chaque jour d'absence se remplace par une agence, à un taux plus élevé que le nôtre. Je n'ai pas le chiffre exact, madame Ouellet l'a et je ne voulais pas l'inventer ici."],
      ["RENAUD","Vous avez bien fait. Je le demanderai. Continuez."],
      ["AÏCHA","Ce que je propose tient en deux choses. La première : une table élévatrice à ciseaux, celle qui monte et descend toute seule selon le poids qu'on y met. La palette est dessus, et la caisse reste toujours à la même hauteur, quelle que soit la hauteur de la pile. L'emballeur ne se penche plus."],
      ["AÏCHA","La deuxième : faire tourner les gens. Quatre heures d'emballage, quatre heures ailleurs. Ça ne coûte rien du tout, ça se décide dans un horaire, et on pourrait l'essayer lundi prochain."],
      ["THÉRÈSE","Ce qui est intéressant dans ce que tu proposes, c'est que la deuxième partie ne dépend pas de la première."],
      ["AÏCHA","C'est voulu. Si la table est refusée, la rotation reste possible. Si la rotation ne suffit pas, on aura au moins essayé quelque chose en attendant."],
      ["RENAUD","Combien coûte la table ?"],
      ["AÏCHA","Je ne le sais pas encore, et je ne vais pas vous donner un chiffre approximatif. J'ai le nom d'un fournisseur, Équipements Sorel, et je voudrais leur demander une soumission écrite. C'est justement ce que je viens vous demander : l'autorisation d'écrire, et le nom de la personne qui doit signer."],
      ["RENAUD","L'autorisation, vous l'avez. Écrivez-leur, mais mettez-moi en copie et écrivez « demande de soumission », pas « commande ». Ce n'est pas la même chose du tout, et une lettre mal formulée nous engage."],
      ["AÏCHA","C'est noté. Et l'échéance que je propose : la rotation à l'essai à partir du lundi 22 septembre, la soumission demandée cette semaine, et une décision sur la table quand nous aurons reçu le prix — disons à la réunion du 20 octobre."],
      ["THÉRÈSE","Une chose que je veux ajouter, et qui n'est pas dans la présentation d'Aïcha. Tant que le poste n'est pas corrigé, un travailleur qui a des motifs raisonnables de croire que ce travail l'expose à un danger a le droit de le refuser. C'est dans la loi, ce n'est pas une opinion. Je préfère qu'on l'entende ici plutôt qu'un matin de rush."],
      ["RENAUD","Vous avez raison de le dire, et personne ici n'a l'intention d'en arriver là. C'est bien pour ça qu'on est assis dans cette salle."],
      ["RENAUD","Madame Traoré, une dernière chose. Ce que vous venez de faire en douze minutes, quatre-vingts pour cent des gens ne savent pas le faire. Vous avez donné vos chiffres, vous avez dit ce que vous ne saviez pas, et vous avez proposé quelque chose de gratuit avant quelque chose de cher. Mettez-moi tout ça dans une note de service pour l'équipe, et la lettre part chez le fournisseur cette semaine."],
      ["AÏCHA","Une note de service pour l'équipe et une lettre pour le fournisseur. Ce ne sont pas les mêmes mots, j'imagine ?"],
      ["THÉRÈSE","Pas du tout les mêmes. Passe me voir cet après-midi, je te sortirai un exemple de chaque."]
    ]
  },

  t3: {
    label: "Dialogue — L'appel chez Équipements Sorel",
    lines: [
      ["VINCENT","Équipements Sorel, bonjour, Vincent Béliveau à l'appareil."],
      ["AÏCHA","Bonjour monsieur Béliveau. Aïcha Traoré, de Meubles Rive-du-Nord, à Terrebonne. Je vous appelle au sujet d'une table élévatrice pour un poste d'emballage."],
      ["VINCENT","Bonjour madame Traoré. Vous êtes au bon endroit. Vous cherchez de l'information, ou vous êtes rendue au prix ?"],
      ["AÏCHA","Les deux, je pense. On voudrait une soumission écrite, mais avant je voudrais être sûre de vous demander la bonne chose."],
      ["VINCENT","C'est la bonne façon de faire. Décrivez-moi le poste, et je vous dirai ce qu'il me faut."],
      ["AÏCHA","Un poste d'emballage. Les caisses arrivent sur une palette posée au sol. L'emballeur se penche pour les prendre, environ quatre-vingts fois par quart de travail. On voudrait que la palette reste toujours à la bonne hauteur."],
      ["VINCENT","Une table à niveau constant, donc. C'est notre modèle le plus demandé pour ce genre de poste. Il me faut trois choses pour vous faire un prix juste : la charge maximale sur la palette, les dimensions de la palette, et la hauteur de travail que vous visez."],
      ["AÏCHA","La palette standard, quarante-huit par quarante pouces. Pour la charge, je dirais douze cents livres pleine. La hauteur de travail, je ne sais pas."],
      ["VINCENT","Prenez la hauteur du coude de la personne qui travaille là, debout, bras le long du corps. C'est la hauteur qu'on vise. Mesurez-la sur deux ou trois personnes différentes et donnez-moi la moyenne."],
      ["AÏCHA","Je peux faire ça cet après-midi. Est-ce que vous pouvez me donner un prix approximatif tout de suite, juste pour que je sache si je fais perdre son temps à tout le monde ?"],
      ["VINCENT","Je peux vous donner un ordre de grandeur, en vous disant bien que ce n'est pas une soumission. Pour cette charge-là, comptez entre quatre et sept mille dollars, selon la finition et selon que vous prenez le plateau tournant ou non."],
      ["AÏCHA","D'accord. Et le plateau tournant, ça sert à quoi ?"],
      ["VINCENT","À ne pas contourner la palette. La personne tourne la palette au lieu de marcher autour. Sur un poste où on fait quatre-vingts caisses, ça change beaucoup de choses. Ça ajoute à peu près huit cents dollars."],
      ["AÏCHA","Je le mettrai en option dans ma demande, alors. Qu'est-ce que vous voulez recevoir, exactement, et de quelle façon ?"],
      ["VINCENT","Une lettre ou un courriel, peu importe, mais que ce soit écrit et signé. Mettez l'objet en haut : demande de soumission, avec le type d'équipement. Ensuite vos trois données, la question de l'option, et la date à laquelle vous voulez la réponse."],
      ["AÏCHA","Est-ce que j'écris que nous voulons acheter ?"],
      ["VINCENT","Surtout pas. Vous écrivez que vous demandez une soumission. Une lettre qui dit « nous voulons acheter » n'est pas une commande non plus, rassurez-vous, mais elle nous fait travailler dans le vide si le budget n'est pas approuvé. Dites simplement où vous en êtes : le projet est à l'étude, la décision se prend en octobre."],
      ["AÏCHA","Et pour le délai, je peux vous demander une date ?"],
      ["VINCENT","Demandez-la, c'est normal et c'est même utile. Nous rendons nos soumissions en cinq jours ouvrables d'habitude. Si vous écrivez que vous la souhaitez pour le 3 octobre, elle sera là le 3 octobre."],
      ["AÏCHA","Parfait. Je vous envoie ça demain, avec ma signature et celle de mon chef de production en copie."],
      ["VINCENT","Très bien. Et madame Traoré : quand vous recevrez notre soumission, regardez la date de validité en bas de page. Un prix d'équipement ne tient pas six mois. Si votre décision se prend en octobre, dites-le, et je la ferai valide jusqu'à la fin novembre."],
      ["AÏCHA","Je ne l'aurais pas remarqué. Merci beaucoup, monsieur Béliveau."],
      ["VINCENT","Ça me fait plaisir. Bonne fin de journée, et n'oubliez pas la hauteur de coude."]
    ]
  },
};
