const DIALOGUES = {
  // Quatre dialogues, un par section. Au niveau 6 ils font dix-huit à vingt et
  // une répliques, et non dix à seize : la compétence vise « des discours
  // détaillés et structurés », et une conversation de trois répliques n'en est
  // pas un. Le même dossier — celui de Leyla — revient dans les quatre, sous
  // quatre formes : le guichet, la banquette, le bureau, l'enveloppe.
  //
  // Cinq personnages, quatre timbres. Voir l'en-tête de
  // generer_audio_module_n6_sante.py : deux personnages ne partagent une voix
  // que s'ils ne se répondent jamais.
  //
  // Aucun conseil de santé qui pourrait être suivi. La spécialiste n'y pose
  // aucun diagnostic, ne nomme aucun médicament et ne donne aucune dose : elle
  // explique une démarche et elle dit que le reste dépend de ce qu'on
  // trouvera.

  prep: {
    label: "Dialogue — À l'accueil de la clinique externe, jeudi, 9 h 25",
    lines: [
      ["LEYLA","Bonjour. J'ai un rendez-vous à neuf heures quarante. Demirci, Leyla."],
      ["MARIETTE","Bonjour. Votre carte d'assurance maladie, s'il vous plaît. Vous venez pour la médecine interne ?"],
      ["LEYLA","Je pense. C'est écrit sur le papier qu'on m'a envoyé, mais je ne suis pas certaine de comprendre lequel des deux mots est le nom du docteur."],
      ["MARIETTE","Montrez-moi. Ah oui : Charest, Sylvine, médecine interne. Sylvine, c'est son prénom ; Charest, c'est son nom de famille. Vous êtes à la bonne place."],
      ["LEYLA","Bon. J'ai attendu sept mois pour ce rendez-vous-là, ça aurait été bête de me tromper d'étage."],
      ["MARIETTE","Sept mois, ce n'est pas rare. Votre médecin de famille avait envoyé une demande de consultation, c'est ça ?"],
      ["LEYLA","Oui. En avril. Elle m'avait dit d'attendre l'appel et de ne pas rappeler avant l'automne."],
      ["MARIETTE","Elle vous avait bien conseillée. Bon. Je vous inscris. Vous avez apporté la liste de vos médicaments ?"],
      ["LEYLA","Je n'en prends pas. À part des vitamines, l'hiver."],
      ["MARIETTE","Notez-les quand même. Tout ce qui se prend compte, même ce qui s'achète sans papier. La docteure va vous poser la question."],
      ["LEYLA","D'accord. Et les prises de sang que j'ai faites au mois de mars, est-ce qu'elle les a ?"],
      ["MARIETTE","Si elles ont été faites ici, elle les a dans le dossier. Si c'est un laboratoire privé, apportez le papier. C'est la chose qu'on oublie le plus souvent."],
      ["LEYLA","C'était ici. Bon. Et j'attends où ?"],
      ["MARIETTE","Salle d'attente C, à votre droite, après la porte vitrée. On va vous appeler par votre nom de famille."],
      ["LEYLA","Ça va durer combien de temps, à peu près ?"],
      ["MARIETTE","Je ne vous mentirai pas : votre rendez-vous est à neuf heures quarante, et la docteure en a onze ce matin. Prévoyez la matinée."],
      ["LEYLA","La matinée. J'ai pris congé jusqu'à midi."],
      ["MARIETTE","Rappelez votre employeur, si vous pouvez. Et une dernière affaire : quand vous sortirez de son bureau, elle va vous remettre une enveloppe. Ouvrez-la ici, pas chez vous."],
      ["LEYLA","Pourquoi ici ?"],
      ["MARIETTE","Parce que s'il y a une question, l'infirmier de liaison est au bout du corridor et il répond aujourd'hui. Chez vous, à sept heures du soir, il n'y a personne au bout du corridor."],
      ["LEYLA","C'est noté. Merci, madame."],
    ]
  },

  t1: {
    label: "Dialogue — Deux heures sur la même banquette",
    lines: [
      ["GILLES","Vous êtes après attendre depuis longtemps ?"],
      ["LEYLA","Depuis neuf heures et demie. Il est onze heures moins quart."],
      ["GILLES","Bienvenue. Moi, ça fait deux heures et je ne suis même pas malade. C'est ma femme qui est là-dedans."],
      ["LEYLA","Ah. Vous l'attendez tout ce temps-là ?"],
      ["GILLES","Je l'attends. Elle ne conduit plus depuis son opération, alors c'est moi le chauffeur, le secrétaire et le porte-manteau. On appelle ça un proche aidant, paraît-il. Moi, j'appelle ça être marié."],
      ["LEYLA","Ma mère était comme ça pour mon père, chez nous. En Turquie. Ça fait cinq ans que je suis ici, trois à Rimouski."],
      ["GILLES","Trois hivers. Vous êtes correcte, d'abord : c'est le troisième qui décide si le monde reste. Vous travaillez ?"],
      ["LEYLA","Aide à domicile. Je vais chez les gens le matin, sept jours sur quatorze."],
      ["GILLES","Ah ben. C'est vous autres qui venez chez nous le mercredi. Vous faites une job que personne ne veut faire."],
      ["LEYLA","C'est une job que j'aime. C'est juste que depuis huit mois, je la fais fatiguée."],
      ["GILLES","Fatiguée comment ? Fatiguée de fin de semaine, ou fatiguée qui ne part pas ?"],
      ["LEYLA","Qui ne part pas. Je dors neuf heures et je me lève comme si j'avais travaillé la nuit. Au mois de mars, j'avais laissé faire, je pensais que c'était l'hiver."],
      ["GILLES","Et là, l'hiver est revenu et vous êtes encore fatiguée."],
      ["LEYLA","C'est exactement ça. Mon médecin m'avait fait passer des prises de sang au printemps. Il y avait quelque chose, une anémie légère, elle a dit. Elle a envoyé une demande de consultation et j'ai attendu."],
      ["GILLES","Ma femme, ç'a été pareil. On avait passé proche d'annuler, au mois d'août, parce qu'elle trouvait que ça ne valait plus la peine. Je l'ai gardée dans l'auto de force."],
      ["LEYLA","Et ça valait la peine ?"],
      ["GILLES","Ça valait la peine. Pas parce qu'ils ont trouvé un remède miracle, là. Parce qu'à partir de ce jour-là, quelqu'un s'occupait de son affaire. Elle avait arrêté de porter ça toute seule."],
      ["LEYLA","Je suis sur le bord de pleurer, monsieur, et je ne vous connais même pas."],
      ["GILLES","C'est la salle d'attente qui fait ça. On est tous après attendre la même affaire. Tenez, prenez un mouchoir : j'en ai toujours quatre paquets, c'est ma femme qui les met dans mes poches. Une chose, par exemple, et après je vous laisse tranquille. Quand elle va vous demander comment vous allez, ne répondez pas « ça va ». Répondez ce que vous venez de me dire à moi. C'est la faute que ma femme a faite pendant deux ans."],
      ["LEYLA","Je pense qu'ils viennent de m'appeler."],
      ["GILLES","Ils vous ont appelée, oui. Allez-y. Bonne chance, madame."],
    ]
  },

  t2: {
    label: "Dialogue — Vingt minutes, et c'est vous qui parlez",
    lines: [
      ["SYLVINE","Madame Demirci, bonjour. Sylvine Charest, je suis interniste. Assoyez-vous. J'ai votre dossier devant moi, mais je préfère l'entendre de vous. Qu'est-ce qui vous amène ?"],
      ["LEYLA","Je suis fatiguée. Ça fait huit mois."],
      ["SYLVINE","Continuez. Huit mois, ça commence quand exactement ?"],
      ["LEYLA","Au mois de février. Je m'en souviens parce que c'est le mois où mon fils a déménagé à Québec. Au début, je pensais que c'était ça."],
      ["SYLVINE","Le mois où votre fils est parti. Et depuis février, est-ce que c'est pareil tous les jours, ou est-ce qu'il y a des journées meilleures ?"],
      ["LEYLA","Il y a des journées meilleures. Le samedi, souvent. Mais je ne sais pas quoi vous répondre pour la moyenne."],
      ["SYLVINE","Ne cherchez pas de moyenne, décrivez-moi une journée ordinaire. Vous vous levez à quelle heure ?"],
      ["LEYLA","Cinq heures et demie. Je commence chez mon premier client à sept heures. Vers dix heures, il faut que je m'assoie. Avant, je ne m'assoyais pas."],
      ["SYLVINE","Bon. Ça, c'est un renseignement utile : ce n'est pas une impression, c'est un changement. Autre chose que vous avez remarqué ? Le souffle, les jambes, l'appétit ?"],
      ["LEYLA","Je monte les escaliers plus lentement. Chez madame Turcotte, par exemple, il y a douze marches, et avant je les montais en parlant. Là, j'arrête de parler."],
      ["SYLVINE","Vous arrêtez de parler dans l'escalier. Merci, c'est précis. Votre médecin avait demandé des prélèvements en mars — je les ai, il y avait une anémie légère. Est-ce qu'on vous a expliqué ce que ça veut dire ?"],
      ["LEYLA","On m'a dit le mot. Personne ne m'a expliqué."],
      ["SYLVINE","Alors je vous l'explique, et arrêtez-moi si un mot vous échappe. Ça veut dire que le sang transporte l'oxygène moins bien qu'il le devrait. Ça, c'est le résultat. Ce n'est pas la cause, et c'est la cause qui m'intéresse, parce qu'il y en a beaucoup de possibles."],
      ["LEYLA","Beaucoup, ça veut dire combien ? Et est-ce que c'est grave ?"],
      ["SYLVINE","Assez pour qu'on ne devine pas. C'est pour ça que je vais demander d'autres examens plutôt que de vous donner une réponse aujourd'hui. Un diagnostic, ce n'est pas un mot qu'on choisit : c'est un mot qu'on mérite, à force de vérifier."],
      ["SYLVINE","Je ne peux pas vous répondre par oui ou par non, et je ne vais pas inventer. Ce que je peux vous dire, c'est que ce que je vois aujourd'hui ne me fait pas peur, et que huit mois de fatigue méritent qu'on cherche pour vrai. Voici donc ce qui arrive maintenant : trois choses. D'abord, il faut que vous passiez d'autres prélèvements ; le laboratoire est au rez-de-chaussée, où vous êtes entrée ce matin. Ensuite, j'aimerais que vous notiez vos journées pendant six semaines — l'heure du lever, les moments où vous devez vous asseoir, notamment. Une ligne par jour, pas plus. Enfin, on se revoit : le jour où j'aurai les résultats, mon bureau vous appelle. Comptez six semaines, peut-être huit."],
      ["LEYLA","Est-ce que je peux vous demander quelque chose ? Mon employeur va me demander un papier."],
      ["SYLVINE","Vous avez bien fait de le demander avant de sortir. Je vous fais une attestation de présence aujourd'hui. Pour le reste — un arrêt, un allègement —, c'est votre médecin de famille qui décide, avec ce que je vais lui écrire : elle a envoyé la demande, elle reçoit le compte rendu. Vous en aurez une copie dans l'enveloppe. Prenez le temps de la lire, c'est votre dossier et pas le mien."],
      ["LEYLA","Merci, docteure. Je pensais que j'allais ressortir avec une réponse."],
      ["SYLVINE","Vous ressortez avec un plan. C'est moins satisfaisant et c'est plus utile."],
    ]
  },

  t3: {
    label: "Dialogue — Ce qu'il y a dans l'enveloppe",
    lines: [
      ["PIERRE-LUC","Madame Demirci ? Pierre-Luc Nadeau, infirmier de liaison. Mariette m'a dit que vous aviez des questions sur ce qu'on vous a remis."],
      ["LEYLA","J'ai trois feuilles et je n'en comprends qu'une."],
      ["PIERRE-LUC","C'est déjà une de plus que la moyenne. Étalez-les sur la table. Bon : le feuillet bleu, le compte rendu, et la demande de prélèvements. Trois papiers, trois usages."],
      ["LEYLA","Le bleu, c'est celui que je comprends. Ça dit quoi apporter et qui appeler."],
      ["PIERRE-LUC","Exactement. Celui-là, gardez-le sur le frigidaire. Il ne parle pas de vous : il explique comment ça marche ici. Le numéro dans l'encadré, c'est celui qu'on appelle avant de se décourager."],
      ["LEYLA","Et le compte rendu ? Il y a des mots que je n'ai jamais vus."],
      ["PIERRE-LUC","C'est normal, il n'est pas écrit pour vous. La docteure Charest écrit à votre médecin de famille : deux médecins qui se parlent par lettre. Vous, vous en avez une copie parce que c'est votre dossier."],
      ["LEYLA","Ici, elle écrit « fatigue persistante d'apparition progressive ». Moi, je lui ai dit que j'étais fatiguée depuis février."],
      ["PIERRE-LUC","C'est la même chose, dite dans l'autre langue. Persistante, ça reprend votre « ça ne part pas ». D'apparition progressive, ça reprend votre « au début, je pensais que c'était l'hiver ». Elle n'a rien ajouté : elle a traduit."],
      ["LEYLA","Et « anémie légère, étiologie à préciser » ?"],
      ["PIERRE-LUC","L'étiologie, c'est la cause. À préciser, ça veut dire qu'on ne la connaît pas encore et qu'on la cherche. C'est exactement ce qu'elle vous a dit de vive voix."],
      ["LEYLA","Pourquoi ne pas l'écrire comme elle l'a dit, alors ?"],
      ["PIERRE-LUC","Bonne question, et la réponse n'est pas très glorieuse : parce que ces mots-là sont plus courts et qu'ils veulent dire la même chose pour tous les médecins du pays. Ça ne vous empêche pas de demander la traduction. C'est ma job."],
      ["LEYLA","Il y a un paragraphe avec des tirets, en bas."],
      ["PIERRE-LUC","C'est le plan. Chaque tiret est une étape : les prélèvements, le journal de vos journées, le rappel dans six à huit semaines. Si vous ne lisez qu'une partie de la lettre, lisez celle-là."],
      ["LEYLA","Et la ligne qui dit « la patiente sera revue à la clinique externe » ?"],
      ["PIERRE-LUC","Ça, c'est du futur d'écriture. Ça ne veut pas dire peut-être : ça veut dire que c'est décidé et que quelqu'un doit le faire."],
      ["LEYLA","Qui, quelqu'un ?"],
      ["PIERRE-LUC","Nous, pour l'appel. Vous, pour répondre au téléphone et pour aller au laboratoire. Écrivez votre nom au crayon à côté des tirets qui sont à vous, tout de suite, pendant que c'est frais."],
      ["LEYLA","Je peux écrire sur un papier officiel ?"],
      ["PIERRE-LUC","Sur votre copie, oui, et c'est même la meilleure chose à en faire. Un papier qu'on n'annote jamais, c'est un papier qu'on ne relit jamais."],
      ["LEYLA","Merci. Je vais téléphoner à ma sœur ce soir. Elle va me demander de tout raconter, et pour une fois je vais savoir quoi dire."],
      ["PIERRE-LUC","Racontez-lui avec vos mots à vous. Les mots de la lettre, gardez-les pour le laboratoire."],
    ]
  },
};
