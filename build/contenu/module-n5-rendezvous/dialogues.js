const DIALOGUES = {

  // ── Je découvre — la cuisine, un mardi soir ─────────────────────────────
  prep: {
    label: "Dialogue — Ça fait trois mois",
    lines: [
      ["NADIA","Papa, tu t'es tenu au comptoir en te levant, tantôt. Je t'ai vu."],
      ["RACHID","C'est rien. Je me lève trop vite, c'est tout."],
      ["NADIA","Ça fait combien de temps que ça t'arrive ?"],
      ["RACHID","Je ne sais pas. Depuis le mois de mars, peut-être. Ça passe en dix secondes."],
      ["NADIA","Mars, on est en juin. Ça fait trois mois, papa."],
      ["RACHID","Trois mois, et je travaille tous les jours. Ce n'est pas une maladie, ça."],
      ["NADIA","Ce n'est pas à toi de décider. Tu as un médecin de famille, sers-t'en."],
      ["RACHID","La docteure Fongang, oui. Mais prendre un rendez-vous, c'est deux heures au téléphone."],
      ["NADIA","Ce n'est plus comme ça. C'est un GMF maintenant, ils ont une agente à l'accueil."],
      ["RACHID","Un GMF ?"],
      ["NADIA","Un groupe de médecine de famille. Plusieurs médecins et des infirmières dans la même clinique. Ils gardent des places pour les patients inscrits."],
      ["RACHID","Et si je ne veux pas attendre trois semaines ?"],
      ["NADIA","Il y a le sans-rendez-vous, mais tu n'auras pas ta médecin. Pour quelque chose qui dure depuis trois mois, tu veux la tienne."],
      ["RACHID","Bon. Et qu'est-ce que je leur dis ?"],
      ["NADIA","Que tu as des étourdissements le matin depuis trois mois, et que tu es fatigué. Deux phrases, pas plus. Garde ta carte d'assurance maladie à côté de toi."],
      ["RACHID","Pourquoi la carte ?"],
      ["NADIA","Ils demandent toujours le numéro. Et vérifie la date : si elle est expirée, tu vas payer."],
      ["RACHID","Elle est bonne jusqu'en février. J'appelle demain matin, alors."],
      ["NADIA","Demain matin. Pas la semaine prochaine."],
    ]
  },

  // ── Défi 1 — l'appel à la clinique ──────────────────────────────────────
  t1: {
    label: "Dialogue — L'appel à la clinique",
    lines: [
      ["VOIX","Vous avez joint la Clinique de la Rive. Pour prendre ou annuler un rendez-vous, faites le deux."],
      ["VOIX","Si vous croyez vivre une urgence, raccrochez et composez le neuf un un. Un instant, on vous répond."],
      ["MANON","Clinique de la Rive, Manon à l'appareil."],
      ["RACHID","Bonjour. J'aimerais prendre un rendez-vous avec la docteure Fongang, s'il vous plaît."],
      ["MANON","Certainement. Vous êtes inscrit chez elle ?"],
      ["RACHID","Oui. Rachid Benali, B, E, N, A, L, I."],
      ["MANON","Merci. Votre numéro de carte d'assurance maladie ?"],
      ["RACHID","BENR quatre-vingt-dix-huit zéro trois douze quinze."],
      ["MANON","C'est noté. Et qu'est-ce qui vous amène ? Je ne demande pas de détails, seulement de quoi choisir la bonne durée."],
      ["RACHID","J'ai des étourdissements le matin en me levant. Ça dure depuis trois mois, et je suis fatigué tout le temps."],
      ["MANON","D'accord. Trois mois, ce n'est pas rien. Je vous mets une plage de trente minutes plutôt que quinze."],
      ["RACHID","Vous avez quelque chose bientôt ?"],
      ["MANON","J'ai le mardi 17 juin à quatorze heures dix, ou le jeudi 19 en fin de journée, à dix-sept heures."],
      ["RACHID","Je finis à seize heures. Le jeudi 19, ce serait plus simple."],
      ["MANON","Jeudi 19 juin, dix-sept heures, avec la docteure Fongang. Présentez-vous quinze minutes avant, à l'accueil."],
      ["RACHID","Quinze minutes avant. Est-ce que je dois apporter quelque chose ?"],
      ["MANON","Votre carte d'assurance maladie, et la liste de tout ce que vous prenez — médicaments, vitamines, produits naturels."],
      ["RACHID","Je voudrais savoir aussi si je dois être à jeun."],
      ["MANON","Non, pas pour une consultation. Si la docteure demande une prise de sang, ce sera un autre rendez-vous."],
      ["RACHID","Parfait. Et si je ne peux plus venir ?"],
      ["MANON","Vous nous appelez au moins vingt-quatre heures à l'avance. Après ce délai, la clinique facture des frais d'absence."],
      ["RACHID","Vingt-quatre heures. Alors jeudi 19 juin, dix-sept heures, arriver à seize heures quarante-cinq. C'est bien ça ?"],
      ["MANON","C'est exact, monsieur Benali. Vous recevrez un rappel automatisé la veille. Bonne journée."],
    ]
  },

  // ── Défi 2 — dans le bureau ─────────────────────────────────────────────
  t2: {
    label: "Dialogue — Dans le bureau de la docteure Fongang",
    lines: [
      ["DRE FONGANG","Bonjour, monsieur Benali. Assoyez-vous. Racontez-moi ce qui se passe."],
      ["RACHID","Ça a commencé au mois de mars. Je me levais le matin et tout tournait pendant quelques secondes."],
      ["DRE FONGANG","Quelques secondes. Et ça arrive à quel moment, exactement ?"],
      ["RACHID","En me levant du lit, surtout. Et parfois en montant l'escalier de l'école, quand je porte mes seaux."],
      ["DRE FONGANG","Donc en passant de la position couchée à debout, et à l'effort. C'est une précision importante."],
      ["RACHID","Au début, c'était une fois par semaine. Maintenant, c'est presque tous les matins."],
      ["DRE FONGANG","Est-ce que vous avez perdu connaissance ? Est-ce que vous êtes tombé ?"],
      ["RACHID","Non, jamais. Je me tiens au mur, ça passe. Mais la semaine dernière, j'ai dû m'asseoir par terre."],
      ["DRE FONGANG","Et la fatigue ? Vous en avez parlé à Manon au téléphone."],
      ["RACHID","Je dors huit heures et je me réveille fatigué. Avant, je jouais au soccer le dimanche. J'ai arrêté au mois d'avril."],
      ["DRE FONGANG","Bon. Je vous prends la tension couché, puis debout, tout de suite après. On va voir si elle descend."],
      ["RACHID","Elle est bonne ?"],
      ["DRE FONGANG","Couché, cent vingt sur quatre-vingts. Debout… elle descend de vingt points. C'est ce que je cherchais."],
      ["RACHID","Ça veut dire quoi ?"],
      ["DRE FONGANG","Que votre pression baisse quand vous vous levez, et que votre cerveau manque de sang une ou deux secondes. Ça explique les étourdissements."],
      ["RACHID","Et la fatigue, ça vient de là aussi ?"],
      ["DRE FONGANG","Pas forcément. C'est pour ça que je demande une prise de sang : je veux vérifier votre fer et votre glande thyroïde."],
      ["RACHID","Je vous suis, mais je veux être sûr. Vous dites que ce n'est pas le cœur ?"],
      ["DRE FONGANG","Votre cœur est régulier et je n'entends rien d'anormal. Si le bilan est normal et que les malaises continuent, on ira plus loin."],
      ["RACHID","J'ai deux questions. Est-ce que je dois arrêter de travailler ? Et est-ce que je peux recommencer le soccer ?"],
      ["DRE FONGANG","Vous continuez de travailler. Pour le soccer, attendez le résultat. En attendant, levez-vous en deux temps : assis au bord du lit, vous comptez jusqu'à dix, puis debout."],
      ["RACHID","Assis, je compte jusqu'à dix, puis debout. Et buvez plus d'eau, c'est ça que vous alliez dire ?"],
      ["DRE FONGANG","Exactement. Je vous fais l'ordonnance pour le prélèvement. Il faut que vous soyez à jeun : rien à manger douze heures avant, de l'eau seulement."],
      ["RACHID","Douze heures. Alors je le prends le matin."],
    ]
  },

  // ── Défi 3 — déplacer, puis annuler ─────────────────────────────────────
  t3: {
    label: "Dialogue — Déplacer, puis annuler",
    lines: [
      ["VOIX","Vous avez joint la Clinique de la Rive. Pour annuler ou modifier un rendez-vous, faites le deux."],
      ["MANON","Clinique de la Rive, Manon à l'appareil."],
      ["RACHID","Bonjour madame. Rachid Benali. Je vous appelle pour déplacer mon rendez-vous de suivi."],
      ["MANON","Un instant, je vous trouve. Le mardi 8 juillet à onze heures, avec la docteure Fongang ?"],
      ["RACHID","C'est ça. Mon horaire de travail a changé : je commence à sept heures maintenant, et je ne finis qu'à quinze heures."],
      ["MANON","Je comprends. Vous préférez donc en fin de journée."],
      ["RACHID","Oui, ou très tôt le matin, avant sept heures, si ça existe."],
      ["MANON","Ça existe : la docteure ouvre à sept heures quinze le mercredi. J'ai mercredi le 9, à sept heures quinze."],
      ["RACHID","Il faut que je sois au travail à sept heures ce jour-là. C'est trop juste."],
      ["MANON","Alors je regarde en fin de journée… J'ai le jeudi 10 juillet à seize heures trente."],
      ["RACHID","Jeudi 10, seize heures trente, je le prends. Vous annulez celui du mardi ?"],
      ["MANON","Je viens de le faire. Vous n'avez rien d'autre à faire, et il n'y a pas de frais : vous m'appelez plus de vingt-quatre heures à l'avance."],
      ["RACHID","Une dernière chose. Ma prise de sang est prévue le lundi 7. Est-ce que le résultat sera arrivé pour le jeudi ?"],
      ["MANON","Trois jours ouvrables, en général. Ce sera juste, mais ça devrait entrer."],
      ["RACHID","Merci beaucoup. Bonne journée."],
      ["MANON","Bonne journée, monsieur Benali."],
      ["VOIX","Vous avez joint la boîte vocale des annulations de la Clinique de la Rive. Après le signal, laissez votre nom, votre date de naissance, la date et l'heure du rendez-vous que vous annulez."],
      ["RACHID","Bonjour, ici Rachid Benali, né le 4 novembre 1974. J'annule mon rendez-vous du jeudi 10 juillet, à seize heures trente, avec la docteure Fongang. Mon garçon est malade et je dois rester avec lui. Je rappellerai demain matin pour en reprendre un autre. Vous pouvez me joindre au 450 555-0173. Je répète : 450 555-0173. Merci."],
    ]
  },

};
