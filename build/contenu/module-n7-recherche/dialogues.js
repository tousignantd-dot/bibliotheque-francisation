const DIALOGUES = {
  // Niveau 7 : la compétence vise des discours étendus. Les quatre extraits
  // ci-dessous font de dix-huit à vingt et une répliques, dont plusieurs de
  // quatre ou cinq phrases. Le reportage du Défi 1 est fait pour trois
  // écoutes : une pour le sujet, une pour les chiffres, une pour le détail.
  //
  // Aucune balise HTML dans les répliques : le texte part tel quel à la
  // synthèse vocale, et un « <b> » s'y entendrait.
  prep: {
    label: "Dialogue — Il y a du travail, mais pas là où vous regardez",
    lines: [
      ["SYLVAIN","Bonjour. Vous cherchez un poste libre à l'ordinateur, ou vous avez une question ?"],
      ["HAFIDA","Les deux, je pense. C'est la première fois que je viens ici. On m'a dit que la salle était gratuite."],
      ["SYLVAIN","Elle l'est, et pour tout le monde. Vous avez les ordinateurs, l'imprimante, le téléphone, et moi. Je suis Sylvain Desbiens, agent d'aide à l'emploi. Installez-vous."],
      ["HAFIDA","Hafida Zerouali. Je travaille dans un centre de la petite enfance, à Longueuil. Je suis préposée à l'entretien depuis quatre ans."],
      ["SYLVAIN","Et vous voulez changer."],
      ["HAFIDA","Je veux revenir à mon métier. Chez moi, en Algérie, j'étais technicienne de laboratoire. Analyses de matériaux, contrôle de la qualité. J'ai fait ça neuf ans."],
      ["SYLVAIN","Neuf ans, ce n'est pas rien. Vous avez fait évaluer votre diplôme ?"],
      ["HAFIDA","J'ai demandé l'évaluation comparative il y a deux ans. Ils me l'ont envoyée. Mais j'ai compris que ça ne valait pas grand-chose."],
      ["SYLVAIN","Ça vaut quelque chose, mais pas ce que les gens croient. L'évaluation comparative, c'est un avis d'expert du gouvernement du Québec. Elle dit à quel niveau d'études québécois votre diplôme se compare. Ce n'est pas une équivalence, et ça ne remplace jamais un permis d'exercice."],
      ["HAFIDA","Alors elle sert à quoi ?"],
      ["SYLVAIN","À l'employeur. Il ne connaît pas votre établissement, il ne sait pas lire votre relevé de notes. L'avis lui traduit tout ça en une page qu'il comprend. Ce n'est pas un laissez-passer, c'est un traducteur."],
      ["HAFIDA","D'accord. Mais le problème n'est pas là. J'ai envoyé trente-quatre candidatures depuis janvier. Trois réponses. Toutes négatives."],
      ["SYLVAIN","Trente-quatre où ?"],
      ["HAFIDA","Ici. Longueuil, Montréal, la Rive-Sud."],
      ["SYLVAIN","Voilà. Vous cherchez là où tout le monde cherche. Venez voir quelque chose à l'écran. Ceci s'appelle IMT en ligne. C'est le site d'information sur le marché du travail. Plus de cinq cents métiers, avec les salaires, les tâches et les perspectives d'emploi, région par région."],
      ["HAFIDA","Région par région ?"],
      ["SYLVAIN","C'est tout l'intérêt. Le Québec, ce n'est pas un seul marché du travail : c'en est dix-sept, et ils ne se ressemblent pas. Il y a des régions où votre métier ne se pratique presque pas, et d'autres où on ne trouve personne pour le faire."],
      ["HAFIDA","Je n'ai jamais pensé à partir. Ma fille est à l'école ici."],
      ["SYLVAIN","Je ne vous dis pas de partir. Je vous dis de regarder avant de décider. Ce n'est pas la même chose. Prenez trois régions, lisez leur portrait économique, comparez, et ensuite vous choisirez en connaissance de cause."],
      ["HAFIDA","Par où je commence ?"],
      ["SYLVAIN","Par vos oreilles. Il y a une série d'émissions sur les économies régionales, à la radio. Demain matin, ils font le Saguenay–Lac-Saint-Jean. Écoutez-la. Vous verrez que ça parle beaucoup de transformation, et un peu de laboratoires."],
    ]
  },

  t1: {
    label: "Reportage — Le Québec au travail : Saguenay–Lac-Saint-Jean",
    lines: [
      ["ODILE","Bonjour. Odile Pominville, et bienvenue à la troisième émission de notre série sur les économies régionales. Aujourd'hui, le Saguenay–Lac-Saint-Jean. D'abord les chiffres, ensuite les gens qui embauchent, et pour finir la question qui revient toujours : est-ce qu'on peut y refaire sa vie professionnelle ?"],
      ["ODILE","Rappelons que la région compte un peu plus de deux cent quatre-vingt-six mille habitants, ce qui la place onzième sur les dix-sept régions du Québec. Son produit intérieur brut a atteint quinze virgule cinq milliards de dollars en 2023, et l'emploi total tournait autour de cent trente-sept mille postes en 2025."],
      ["ODILE","Pour comprendre ce que ces chiffres veulent dire, j'ai demandé à Ghislain Néron, économiste régional, de nous les traduire. Monsieur Néron, bonjour."],
      ["GHISLAIN","Bonjour. Le premier chiffre à retenir n'est pas le plus gros, c'est le plus révélateur. Le secteur primaire occupe quatre virgule deux pour cent de l'emploi régional. Ailleurs au Québec, c'est deux pour cent. Autrement dit, la région tire deux fois plus de son sol et de sa forêt que la moyenne."],
      ["ODILE","Et la fabrication ?"],
      ["GHISLAIN","Onze virgule deux pour cent des emplois, et surtout une fabrication d'un type très précis : la transformation des ressources naturelles. L'aluminium d'abord, les produits du bois ensuite, la machinerie après. Les ventes manufacturières ont dépassé onze milliards de dollars. Ce n'est pas une région de bureaux, c'est une région d'usines."],
      ["ODILE","En ce qui concerne la construction, on m'a dit qu'elle était forte aussi."],
      ["GHISLAIN","Huit virgule neuf pour cent de l'emploi, contre sept pour cent pour l'ensemble du Québec. Là encore, plus que la moyenne. Quant aux services, ils représentent tout de même plus des trois quarts de l'emploi, comme partout ailleurs : il ne faut pas imaginer une région où tout le monde serait en usine."],
      ["ODILE","Vous employez souvent le mot transformation. Qu'est-ce que ça change, pour quelqu'un qui cherche du travail ?"],
      ["GHISLAIN","Ça change tout. Une usine de transformation ne fait pas que produire : elle vérifie, elle mesure, elle certifie. Chaque lot est analysé. Or ces postes-là, les postes de contrôle de la qualité, on ne les remplit plus. La relève ne suit pas. Il y a des laboratoires industriels qui fonctionnent avec une personne de moins depuis deux ans."],
      ["ODILE","À propos de la relève, justement, la région n'est pas la seule à en manquer."],
      ["GHISLAIN","Non, mais elle en manque autrement. À Montréal, il y a moins de postes ouverts et plus de candidats. Ici, c'est l'inverse : moins de candidats, et des postes qui restent affichés six mois. Un employeur de Montréal choisit ; un employeur d'ici convainc."],
      ["ODILE","Merci, monsieur Néron. J'ai voulu vérifier ça sur le terrain. Frédérick Gauthier-Simard dirige le laboratoire de contrôle d'Alumico, une entreprise de transformation de l'aluminium installée à Jonquière. Monsieur Gauthier-Simard, combien de personnes travaillent dans votre laboratoire ?"],
      ["FRÉDÉRICK","Sept. Nous devrions être neuf. J'ai deux postes affichés depuis le mois de février, et je n'ai reçu que onze candidatures. Onze, en six mois."],
      ["ODILE","C'est peu."],
      ["FRÉDÉRICK","C'est très peu. Et le plus frustrant, c'est que le métier n'est pas si rare. Il y a des centaines de techniciennes et de techniciens de laboratoire au Québec. Ils sont simplement tous ailleurs, et ils n'imaginent pas qu'on cherche ici."],
      ["ODILE","Qu'est-ce que vous demandez, exactement ?"],
      ["FRÉDÉRICK","Un diplôme technique, ou une expérience équivalente qu'on peut vérifier. Le reste s'apprend chez nous : nos appareils, nos méthodes, nos normes. Ce que je ne peux pas enseigner, c'est la rigueur. Quelqu'un qui a tenu un cahier de laboratoire pendant neuf ans, même à l'étranger, m'intéresse davantage qu'un diplômé de l'an dernier."],
      ["ODILE","Et si la personne vient d'une autre région ?"],
      ["FRÉDÉRICK","Nous en engageons déjà. Ce que je conseille, c'est de nous appeler avant d'envoyer un curriculum vitæ. Une conversation de dix minutes en dit plus long qu'une lettre, et ça permet à la personne de tailler sa candidature pour ce que nous faisons vraiment."],
      ["ODILE","En somme : une région d'usines, une main-d'œuvre qui manque, et des employeurs qui répondent au téléphone. Odile Pominville, pour Le Québec au travail. La semaine prochaine, Chaudière-Appalaches."],
    ]
  },

  t2: {
    label: "Dialogue — Deux régions, deux portraits, une décision",
    lines: [
      ["MARIE-ÈVE","Vous avez imprimé les deux portraits ? Parfait. Posez-les côte à côte sur la table."],
      ["HAFIDA","Le Saguenay et Chaudière-Appalaches. Je les ai lus trois fois. Je comprends chaque phrase, mais je n'arrive pas à décider."],
      ["MARIE-ÈVE","C'est normal : ce n'est pas un problème de vocabulaire, c'est un problème de méthode. On ne décide pas en lisant, on décide en comparant. Prenez une feuille et tracez deux colonnes."],
      ["HAFIDA","D'accord. Qu'est-ce que je compare ?"],
      ["MARIE-ÈVE","Trois choses seulement, sinon vous vous noyez. Un : est-ce que mon métier existe là-bas ? Deux : est-ce qu'il y manque du monde ? Trois : est-ce que ma famille pourrait y vivre ? Le reste vient après."],
      ["HAFIDA","Pour le premier point, le Saguenay gagne. La fabrication y occupe onze virgule deux pour cent de l'emploi, et c'est de la transformation. Chaudière-Appalaches transforme aussi, mais surtout des aliments et du métal ouvré."],
      ["MARIE-ÈVE","Bien. Et notez comment le texte le dit : « la transformation des ressources naturelles ». Il ne dit pas « on transforme les ressources naturelles ». Vous avez remarqué ?"],
      ["HAFIDA","Oui, il y a beaucoup de mots comme ça. Transformation, fabrication, embauche, croissance. Ce sont des verbes déguisés en noms."],
      ["MARIE-ÈVE","Exactement, et c'est la marque de ce genre de texte. Un portrait économique ne raconte pas ce que les gens font, il nomme des activités. Ça le rend court et froid. Quand une phrase vous résiste, cherchez le verbe qui se cache sous le nom et remettez-le debout : la transformation, ça veut dire qu'on transforme."],
      ["HAFIDA","Il y a autre chose qui me gêne. Le texte dit souvent « ils ». « Ils ont investi », « ils ont annoncé ». Mais on ne sait jamais qui."],
      ["MARIE-ÈVE","Et c'est fait exprès. Dans ces textes-là, « ils » désigne les décideurs sans les nommer : l'entreprise, la municipalité, le gouvernement. On appelle ça un référent implicite. Vous n'avez pas manqué une information : elle n'a jamais été donnée."],
      ["HAFIDA","Alors comment je sais de qui on parle ?"],
      ["MARIE-ÈVE","Par le contexte, et par le paragraphe d'avant. Si le paragraphe parle d'une usine, « ils » c'est l'usine. Si le paragraphe parle d'un budget régional, « ils » c'est le gouvernement. Et quand vraiment on ne peut pas trancher, c'est que la phrase ne veut pas qu'on tranche."],
      ["HAFIDA","Il y a aussi toutes ces phrases où personne n'agit. « L'usine a été agrandie en 2021. » Par qui ?"],
      ["MARIE-ÈVE","Même logique. La phrase passive permet de dire ce qui est arrivé sans dire qui l'a fait. Parfois l'auteur l'ajoute : « a été agrandie par le propriétaire ». Souvent il ne l'ajoute pas, parce que ça n'intéresse personne. Ce qui compte, c'est que l'usine est plus grande."],
      ["HAFIDA","Deuxième point, alors : est-ce qu'il manque du monde ? Le portrait ne le dit pas."],
      ["MARIE-ÈVE","Un portrait économique ne le dit jamais. Il décrit une structure, pas un manque. Pour le manque, vous retournez à IMT en ligne et vous regardez les perspectives d'emploi de votre profession, région par région. Et vous avez déjà une réponse : l'employeur de Jonquière a dit à la radio qu'il n'avait reçu que onze candidatures en six mois."],
      ["HAFIDA","Onze. À Montréal, ils en reçoivent deux cents."],
      ["MARIE-ÈVE","Voilà votre deuxième colonne remplie. Reste la troisième, et celle-là, aucun document ne la remplira à votre place. Elle se règle à la maison, en famille, un soir de semaine."],
      ["HAFIDA","Ma fille a treize ans. C'est elle qui va décider, au fond."],
      ["MARIE-ÈVE","Peut-être. Mais présentez-lui deux colonnes, pas deux angoisses. Elle décidera mieux."],
    ]
  },

  t3: {
    label: "Dialogue — Ce que votre curriculum vitæ ne dit pas encore",
    lines: [
      ["MARIE-ÈVE","Vous avez l'offre sous les yeux ? Lisez-moi le titre exact."],
      ["HAFIDA","« Technicienne ou technicien de laboratoire — contrôle de la qualité. Alumico, Jonquière. Quart de jour. Poste permanent. »"],
      ["MARIE-ÈVE","Et votre curriculum vitæ, en haut, sous votre nom, qu'est-ce qu'il annonce ?"],
      ["HAFIDA","« Recherche d'emploi dans le domaine scientifique. »"],
      ["MARIE-ÈVE","Voilà le problème, et il est en trois mots. Cette ligne pourrait être celle de n'importe qui. Ce que l'employeur veut lire à cet endroit-là, c'est le titre du poste qu'il a affiché, pas une catégorie."],
      ["HAFIDA","Je mets « Technicienne de laboratoire — contrôle de la qualité » ?"],
      ["MARIE-ÈVE","Oui. Le même titre, mot pour mot. Un curriculum vitæ ne se rédige pas une fois pour toutes : il se retaille pour chaque offre. Ce n'est pas de la flatterie, c'est de la lisibilité. Une personne qui reçoit quarante dossiers ne lit d'abord que les premières lignes."],
      ["HAFIDA","Ensuite, j'ai mis mes emplois dans l'ordre. Le centre de la petite enfance en premier, parce que c'est le plus récent."],
      ["MARIE-ÈVE","C'est la règle habituelle, et ici elle vous dessert. Votre expérience la plus récente n'est pas votre expérience la plus pertinente. Créez deux blocs : « Expérience en laboratoire » d'abord, « Autre expérience professionnelle » ensuite. Vous n'inventez rien, vous rangez autrement."],
      ["HAFIDA","On a le droit de faire ça ?"],
      ["MARIE-ÈVE","On a le droit d'organiser. On n'a pas le droit de mentir. Tant que les dates y sont et qu'elles sont exactes, vous choisissez l'ordre. Le programme de votre cours l'appelle « mettre en valeur des informations en fonction d'un poste spécifique ». C'est précisément ce que vous faites."],
      ["HAFIDA","Et mes neuf années là-bas, je les décris comment ? J'ai écrit « responsable des analyses »."],
      ["MARIE-ÈVE","Trop vague. Donnez trois tâches et un chiffre. « Analyses de conformité sur quarante lots par semaine. » « Tenue du cahier de laboratoire. » « Formation de deux nouvelles techniciennes. » Un chiffre vaut trois adjectifs."],
      ["HAFIDA","Bon. Et la lettre ?"],
      ["MARIE-ÈVE","La lettre d'accompagnement ne répète pas le curriculum vitæ. Elle répond à une seule question : pourquoi vous, et pourquoi ici. Trois paragraphes. Le premier dit ce que vous demandez et où vous avez vu l'offre. Le deuxième relie votre expérience à ce que l'entreprise fait. Le troisième demande la rencontre."],
      ["HAFIDA","J'ai écrit « Je veux ce poste ». Ça se dit ?"],
      ["MARIE-ÈVE","Ça se dit entre nous. Dans une lettre, on prend le conditionnel : « Je souhaiterais poser ma candidature ». « J'aimerais vous rencontrer. » Ce n'est pas de l'hésitation, c'est de la politesse écrite. Et gardez le même ton du début à la fin : on ne commence pas en vouvoyant poliment pour finir avec « à bientôt ! »."],
      ["HAFIDA","Le deuxième paragraphe, je le commence comment ?"],
      ["MARIE-ÈVE","Par ce qui est fort. Mettez-le en avant : « C'est la rigueur du cahier de laboratoire qui a fait l'essentiel de mon métier pendant neuf ans. » Ou : « Ce que j'apporte, c'est neuf ans de contrôle de conformité. » Le français a des tournures faites exprès pour ça."],
      ["HAFIDA","Et je dis que je suis prête à déménager ?"],
      ["MARIE-ÈVE","Vous le dites, clairement, et en une phrase. C'est la première question qu'il se posera. « Je suis disponible pour m'installer dans la région avant que le quart de jour ne reprenne en janvier. » Il saura tout de suite qu'il ne perd pas son temps."],
      ["HAFIDA","Et si je téléphonais avant, comme il l'a conseillé à la radio ?"],
      ["MARIE-ÈVE","Faites-le. Mais préparez trois questions avant de composer le numéro, pour que l'appel ait un but. Un appel sans question, c'est une candidature de plus. Un appel avec trois questions, c'est un nom qu'il retiendra."],
    ]
  },
};
