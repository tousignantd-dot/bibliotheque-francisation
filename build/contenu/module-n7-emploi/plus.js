const PLUS = {

  prProso: {
    eye:'Mini-leçon', tit:"La mélodie d'un exposé",
    blocs:[
      {t:'texte', h:"Ce qui manque quand tout est correct et que personne ne suit",
       p:"Vous pouvez avoir les bons mots, les bons temps de verbe et les bons chiffres, et voir la salle décrocher au bout d'une minute. Ce qui manque alors n'est presque jamais du vocabulaire : c'est la <b>mélodie</b>. Une présentation dite sur une seule note s'entend comme une liste, et une liste ne se retient pas.",
       note:"Le programme du niveau 7 appelle ça le <b>système prosodique</b> : l'intonation, l'accentuation, le rythme."},

      {t:'texte', h:"On ne parle pas mot par mot",
       p:"Le français se dit par <b>groupes rythmiques</b> de trois à sept syllabes. Entre deux groupes, il y a un arrêt très court — trop court pour être une pause, assez long pour être entendu. <i>D'abord, on mesure / pendant deux semaines / chaque camion.</i> Trois groupes, trois respirations minuscules, et la phrase devient suivable.",
       note:"À l'intérieur d'un groupe, un seul mot est accentué : le <b>dernier</b>. C'est la règle du français, et elle est différente de presque toutes les autres langues."},

      {t:'ana', h:"La voix monte : ce n'est pas fini",
       p:"À la fin d'un groupe qui n'est pas le dernier de la phrase, la voix monte légèrement. C'est un signal, pas une question.",
       mots:[['On dit','D\'abord, on mesure… / Il y a quatre étapes…'],['La voix','monte sur la dernière syllabe',true],['Ce que la salle comprend','ne partez pas, la suite arrive']],
       say:"D'abord, on mesure, pendant deux semaines, chaque camion qui se présente.",
       note:"Si vous descendez à chaque groupe, votre auditoire croit que vous avez fini quatre fois par minute."},

      {t:'ana', h:"La voix descend : c'est fini",
       p:"Au dernier groupe de la phrase, la voix descend franchement. C'est le seul signal qui autorise l'autre à parler.",
       mots:[['On dit','Voilà. Des questions ? / Rien n\'est acheté avant la mi-novembre.'],['La voix','descend nettement',true],['Ce que la salle comprend','je vous laisse la parole']],
       say:"Deux mois et demi, quatre cents dollars pour savoir, et une décision en novembre. Voilà. Des questions ?",
       note:"Une question qui commence par un mot interrogatif descend elle aussi : <i>quand est-ce qu'on décide ?</i> Seule la question sans mot interrogatif monte : <i>on décide en novembre ?</i>"},

      {t:'ana', h:"L'accent d'insistance : appuyer sans crier",
       p:"Pour qu'un mot ressorte, on n'augmente pas le volume. On appuie sa <b>première</b> syllabe, on la tient un peu plus longtemps, et on ralentit juste avant.",
       mots:[['Ordinaire','la partie la moins spectaculaire du projet'],['Avec insistance','la partie la moins <b>spec</b>taculaire du projet',true],['Ce que ça fait','le mot se détache sans que la voix monte']],
       say:"C'est la partie la moins spectaculaire du projet, et c'est la plus importante.",
       note:"Un ou deux accents d'insistance par minute. Trois de suite et plus rien ne ressort."},

      {t:'labo', h:"Écoutez les deux mélodies",
       p:"Choisissez un moment de la présentation et voyez ce que la voix y fait.",
       axes:[
         {id:'m', lbl:'Quel moment ?', opts:[['a','au milieu d\'une phrase'],['b','à la fin d\'une phrase']]},
         {id:'n', lbl:'Quel exemple ?', opts:[['1','le premier'],['2','le second']]}],
       out:{
         a1:{w:["d'abord, on mesure"], say:"D'abord, on mesure, pendant deux semaines, chaque camion qui se présente.", n:'la voix monte : la phrase continue'},
         a2:{w:['Il y a quatre étapes'], say:"Ensuite, les étapes. Il y a quatre étapes, et je vais les nommer dans l'ordre.", n:'elle monte encore : une énumération s\'annonce'},
         b1:{w:['Voilà. Des questions ?'], say:"Deux mois et demi, quatre cents dollars pour savoir, et une décision en novembre. Voilà. Des questions ?", n:'elle descend : la parole est rendue à la salle'},
         b2:{w:['la moins spectaculaire'], say:"C'est la partie la moins spectaculaire du projet, et c'est la plus importante.", n:'accent d\'insistance sur la première syllabe'},
       },
       note:"Écoutez, puis redites la phrase à voix haute en exagérant un peu. On exagère toujours trop peu."},

      {t:'piege', h:"Trois habitudes qui se corrigent en une semaine",
       rows:[
         ["monter la voix à la fin de chaque phrase","descendre quand c'est fini",
          "C'est l'habitude la plus fréquente chez les adultes qui présentent en français. Elle donne l'impression que vous demandez la permission à chaque phrase, et la salle finit par ne plus vous croire."],
         ["parler plus fort pour insister","appuyer la première syllabe",
          "Le volume fatigue et n'ajoute aucune information. L'accent d'insistance, lui, désigne un mot précis."],
         ["ne jamais s'arrêter","respirer entre les groupes",
          "Un exposé sans silence est un exposé sans structure. Les arrêts très courts sont ce qui rend une présentation compréhensible, pas ce qui la ralentit."],
       ]},

      {t:'check', h:"Est-ce que c'est clair ?",
       p:"Quatre questions rapides.",
       qs:[
         {q:"« D'abord, on mesure… » : la voix…", opts:["monte","descend"], ok:0,
          fb:"Le groupe n'est pas le dernier de la phrase : la voix monte."},
         {q:"« Voilà. Des questions ? » : la voix…", opts:["monte","descend"], ok:1,
          fb:"C'est fini, et une question avec mot interrogatif ou une clôture descend."},
         {q:"Pour insister sur un mot, on…", opts:["parle plus fort","appuie sa première syllabe"], ok:1,
          fb:"Le volume n'est pas un outil de sens en français."},
         {q:"Un groupe rythmique fait…", opts:["trois à sept syllabes","douze à quinze syllabes"], ok:0,
          fb:"Au-delà, l'auditeur perd le fil et vous manquez d'air."},
       ]},
    ]
  },

  prCinq: {
    eye:'Mini-leçon', tit:"Cinq parties, et pourquoi aucune ne se saute",
    blocs:[
      {t:'texte', h:"La différence n'est pas dans le ton",
       p:"On croit souvent qu'une plainte se distingue d'un projet par la politesse, ou par le calme de celui qui parle. C'est faux. On peut se plaindre très poliment pendant dix minutes. La différence est dans <b>ce qu'on met dans sa phrase</b> : une plainte porte le problème, un projet porte le problème et sa suite.",
       note:"Thérèse le dit à Aïcha en une phrase : « Une plainte, ça dit ce qui ne va pas et ça s'arrête là. »"},

      {t:'ana', h:"1 · Le constat — ce que vous avez vu et compté",
       p:"Pas d'adjectif, pas de jugement. Des personnes, des jours, des nombres.",
       mots:[['On dit','Trois personnes du poste 4 ont consulté pour le dos depuis mars.'],['On ne dit pas','Le poste 4, c\'est un scandale.',true],['Le test','est-ce que quelqu\'un pourrait aller le vérifier ?']],
       say:"Trois personnes du poste quatre ont consulté pour le dos depuis le mois de mars.",
       note:"Un constat vérifiable donne à toute la suite sa solidité. Un constat vague la retire à tout."},

      {t:'ana', h:"2 · La cause — pourquoi ça arrive",
       p:"Sans cause nommée, la salle en invente une, et c'est presque toujours « les gens ne font pas attention ».",
       mots:[['On dit','Les caisses sont au sol : l\'emballeur se penche quatre-vingt-deux fois par quart.'],['Ce qui use','la répétition, pas le poids',true],['Ce que ça évite','qu\'on cherche un coupable']],
       say:"Ce qui use le dos, ce n'est pas le poids d'une caisse, c'est de se pencher quatre-vingt-deux fois.",
       note:"Nommer la cause déplace la conversation de « qui est fautif » vers « qu'est-ce qu'on change »."},

      {t:'ana', h:"3 · La conséquence — ce que ça coûte",
       p:"C'est la partie qu'on saute le plus souvent, et c'est celle qui fait décider. Des jours, de l'argent, des retards.",
       mots:[['On dit','Quinze jours ouvrables d\'absence depuis mars, plus un poste allégé depuis onze semaines.'],['Ce qu\'on ajoute','chaque absence se remplace par une agence',true],['Ce qu\'on ne fait pas','inventer un chiffre qu\'on n\'a pas']],
       say:"Quinze jours ouvrables d'absence depuis mars, plus un poste en tâches allégées depuis onze semaines.",
       note:"Dire « je n'ai pas ce chiffre, telle personne l'a » vous grandit. Inventer un chiffre vous coûte tout le reste de la présentation."},

      {t:'ana', h:"4 · Le correctif — ce que vous proposez",
       p:"Proposez toujours le gratuit avant le cher, et rendez-les indépendants l'un de l'autre.",
       mots:[['Le gratuit','faire tourner les gens : quatre heures d\'emballage, quatre heures ailleurs'],['Le cher','une table élévatrice à ciseaux',true],['Pourquoi cet ordre','on ne peut pas vous refuser les deux d\'un coup']],
       say:"La rotation ne coûte rien du tout, ça se décide dans un horaire.",
       note:"Un projet qui n'a qu'une solution, et une solution chère, se refuse en une phrase."},

      {t:'ana', h:"5 · L'échéance — une date",
       p:"Pas « bientôt », pas « dès que possible ». Un jour de la semaine et un chiffre.",
       mots:[['On dit','La rotation à l\'essai à partir du lundi 22 septembre.'],['On dit aussi','Une décision sur la table le 20 octobre.',true],['Ce qui arrive sans date','le projet n\'est pas refusé : il est oublié']],
       say:"La rotation à l'essai à partir du lundi vingt-deux septembre.",
       note:"Une date force une réponse. C'est exactement pour ça qu'on hésite à en donner une, et exactement pour ça qu'il en faut une."},

      {t:'check', h:"Reconnaissez la partie qui manque",
       p:"Trois questions.",
       qs:[
         {q:"« Le poste 4 fait mal au dos, il faudrait une table. » Que manque-t-il surtout ?", opts:["les chiffres et la date","la politesse"], ok:0,
          fb:"Il y a un constat vague et un correctif vague. Ni conséquence chiffrée, ni échéance."},
         {q:"« Trois personnes blessées, quinze jours d'absence. » C'est…", opts:["un projet complet","un constat et une conséquence"], ok:1,
          fb:"Il manque la cause, le correctif et la date."},
         {q:"Dans quel ordre proposer les correctifs ?", opts:["le gratuit d'abord","le plus efficace d'abord"], ok:0,
          fb:"Le gratuit d'abord : il peut être accepté tout de suite, et il montre que vous ne demandez pas de l'argent par réflexe."},
       ]},
    ]
  },

  prOrdre: {
    eye:'Mini-leçon', tit:"Lire un ordre du jour",
    blocs:[
      {t:'texte', h:"Un document de six lignes qui décide de votre semaine",
       p:"L'ordre du jour n'est pas une formalité : c'est lui qui dit qui doit être là, ce qui va se discuter, dans quel ordre et pendant combien de temps. Une personne qui le lit vraiment arrive préparée ; les autres découvrent en séance qu'elles avaient un document à lire.",
       note:"Au Québec, il circule le plus souvent deux ou trois jours d'avance, par courriel ou au babillard."},

      {t:'ex', h:"Ce qu'on y trouve, et ce que ça vous demande",
       p:"À gauche l'élément, à droite ce que vous devez en faire.",
       rows:[
         ["La date, l'heure et le lieu","Notez la durée aussi : « de 8 h à 9 h 15 » vous dit combien de temps vous avez pour votre point."],
         ["La convocation","Le nom de la personne qui convoque est celui à qui l'on signale une absence."],
         ["Les personnes convoquées","Si vous y êtes, votre présence est attendue, pas facultative."],
         ["Les points numérotés","Le numéro sert à nommer un sujet en deux mots : « au point 3 »."],
         ["La durée d'un point","« Douze minutes » veut dire douze minutes. C'est une contrainte, pas une estimation."],
         ["Le varia","Les points de dernière minute. Ils se demandent en début de réunion, jamais au milieu."],
         ["Les documents joints","Ce qu'il faut avoir lu avant d'arriver. Personne ne le relira pour vous en séance."],
         ["Le procès-verbal déposé","Le compte rendu de la dernière fois, à approuver. C'est le moment de corriger une erreur qui vous concerne."],
       ]},

      {t:'texte', h:"Demander un point à l'ordre du jour",
       p:"C'est le geste que fait Thérèse pour Aïcha, et il tient en une phrase : <i>« Est-ce qu'il reste de la place à l'ordre du jour d'une prochaine réunion ? »</i> On demande la place avant de préparer le contenu — l'inverse coûte des soirées perdues. Une fois la place obtenue, on confirme par écrit avant la date limite indiquée.",
       note:"Demander quinze minutes et en prendre vingt-cinq est la façon la plus sûre de ne plus jamais en obtenir."},

      {t:'piege', h:"Deux malentendus fréquents",
       rows:[
         ["croire que « varia » veut dire « n'importe quand »","le demander en début de réunion",
          "Le varia est un espace prévu à la fin, pas une permission d'interrompre. Un point demandé au milieu du point 2 sera renvoyé au varia de toute façon."],
         ["arriver sans avoir lu le document joint","le lire la veille, crayon en main",
          "Le document joint est la seule partie de la réunion que vous pouvez maîtriser d'avance. C'est aussi celle qui vous permet de poser une question précise plutôt qu'une question générale."],
       ]},
    ]
  },

  t1plan: {
    eye:'Mini-leçon', tit:"Le plan que toute présentation de projet suit",
    blocs:[
      {t:'texte', h:"Pourquoi c'est toujours le même plan",
       p:"Une présentation de projet en milieu de travail suit presque toujours cinq mouvements, dans le même ordre, quel que soit le métier. Ce n'est pas une convention arbitraire : c'est l'ordre dans lequel les questions montent dans la tête de celui qui écoute. Il veut savoir <i>pour quoi faire</i>, puis <i>comment</i>, puis <i>quand</i>, puis <i>combien</i>, puis <i>qu'est-ce qui peut mal aller</i>.",
       note:"Répondre dans un autre ordre n'est pas interdit ; ça oblige simplement l'auditeur à garder ses questions en attente, et il en oublie la moitié."},

      {t:'ex', h:"Les cinq mouvements, et la phrase qui les ouvre",
       p:"À gauche la partie, à droite la façon de l'annoncer.",
       rows:[
         ["L'objectif","« L'objectif tient en une phrase : … » — une seule phrase, vraiment. Si elle en prend trois, l'objectif n'est pas clair pour vous non plus."],
         ["Les étapes","« Il y en a quatre. D'abord… ensuite… puis… enfin… » — annoncez le nombre avant de commencer."],
         ["L'échéancier","« Les relevés commencent le 8 septembre et se terminent le 19. » — des dates, pas des durées floues."],
         ["Le budget","« L'essai coûte quatre cents dollars. » — et dites d'où vient le chiffre."],
         ["Les risques","« Il y en a trois, et je préfère les nommer moi-même. »"],
         ["Le résumé","« En somme : on mesure, on trace, on essaie, on installe. » — les quatre mots que la salle emportera."],
       ]},

      {t:'texte', h:"Nommer ses risques soi-même",
       p:"C'est le mouvement que les débutants sautent, et c'est celui qui fait la différence. Un projet présenté sans risque a l'air préparé par quelqu'un qui n'a pas réfléchi ; on lui trouvera ses risques à sa place, et depuis la salle. Les nommer soi-même, en revanche, prouve qu'on a regardé le projet en face — et permet de les présenter avec ce qu'on compte faire.",
       note:"Trois risques est un bon nombre. Un seul a l'air d'une concession polie ; six ont l'air d'un projet qu'on ne croit pas."},

      {t:'texte', h:"Annoncer le nombre : le petit geste qui change tout",
       p:"« Il y en a quatre. » « Il y en a trois. » Ces cinq mots donnent à l'auditeur une carte : il sait combien de temps il en a, il peut cocher, il ne se demande pas si vous allez continuer longtemps. C'est le geste le moins coûteux et le plus efficace de toute la présentation.",
       note:"Le corollaire : annoncez quatre étapes, donnez-en quatre. Une cinquième surprise défait tout le bénéfice."},

      {t:'check', h:"Trois questions",
       p:"",
       qs:[
         {q:"Où placer les risques ?", opts:["à la fin, avant le résumé","au début, pour être honnête"], ok:0,
          fb:"Après le budget : la salle a alors tout ce qu'il faut pour juger si le risque en vaut la peine."},
         {q:"L'objectif tient en…", opts:["une phrase","un paragraphe"], ok:0,
          fb:"S'il en prend plus, c'est qu'il y a deux objectifs, et il faut choisir."},
         {q:"Pourquoi annoncer le nombre d'étapes ?", opts:["pour faire sérieux","pour que l'auditeur sache où il en est"], ok:1,
          fb:"C'est une carte donnée à celui qui écoute."},
       ]},
    ]
  },

  t1connect: {
    eye:'Mini-leçon', tit:"Les connecteurs, ou les panneaux de la route",
    blocs:[
      {t:'texte', h:"Ils ne disent rien, et ils changent tout",
       p:"Un connecteur n'ajoute aucune information : il dit <b>où l'on est rendu</b>. C'est exactement le rôle d'un panneau routier, qui ne construit pas la route mais sans lequel personne ne sait s'il faut tourner. Dans un exposé de douze minutes, les connecteurs sont la seule chose qui empêche l'auditeur de se perdre.",
       note:"C'est un savoir de <b>grammaire du texte</b> : il ne porte pas sur la phrase, mais sur ce qui relie les phrases entre elles."},

      {t:'ana', h:"Les connecteurs d'énumération",
       p:"Ils numérotent sans dire « un, deux, trois ».",
       mots:[['On dit','d\'abord · ensuite · puis · enfin'],['On annonce avant','Il y en a quatre.',true],['Attention','« enfin » annonce la dernière : jamais au milieu']],
       say:"D'abord, ensuite, puis, enfin.",
       note:"« Premièrement, deuxièmement » existe, mais s'entend administratif. Réservez-le à l'écrit."},

      {t:'ana', h:"Les connecteurs de conséquence",
       p:"Ils disent : voici ce que ça produit.",
       mots:[['Formels','par conséquent · c\'est pourquoi · ainsi'],['Courant','résultat · donc',true],['Dans une réunion','« par conséquent » passe très bien']],
       say:"Le quai n'a pas changé depuis deux mille neuf ; par conséquent, les camions attendent.",
       note:"« Donc » n'est pas incorrect, mais il s'use vite : trois « donc » par minute et il ne veut plus rien dire."},

      {t:'ana', h:"Les connecteurs d'opposition",
       p:"Ils annoncent que ce qui suit va contre ce qui précède.",
       mots:[['À l\'écrit','en revanche · cependant · toutefois · néanmoins'],['À l\'oral','par contre · mais',true],['La règle','on ne mélange pas les deux registres dans un même texte']],
       say:"L'essai coûte quatre cents dollars. En revanche, l'installation coûterait douze mille dollars.",
       note:"« Par contre » est parfaitement correct en français du Québec. C'est une question de registre, pas de correction."},

      {t:'ana', h:"Les connecteurs d'exemple et de clôture",
       p:"Ils illustrent, puis ils ferment.",
       mots:[['Exemple','par exemple · notamment · ainsi · prenons'],['Clôture','en somme · pour résumer · en définitive',true],['Le piège de « notamment »','il annonce un exemple parmi d\'autres, jamais une liste complète']],
       say:"Notamment. En somme. Pour résumer.",
       note:"« En somme » promet un résumé. Le promettre et parler encore quatre minutes est ce qui fait décrocher une salle."},

      {t:'labo', h:"Choisissez la relation, entendez le connecteur",
       p:"Deux axes : ce que vous voulez dire, et le registre.",
       axes:[
         {id:'r', lbl:'Quelle relation ?', opts:[['a','conséquence'],['b','opposition'],['c','clôture']]},
         {id:'g', lbl:'Quel registre ?', opts:[['1','écrit / formel'],['2','oral courant']]}],
       out:{
         a1:{w:['par conséquent'], say:"Le quai n'a pas changé ; par conséquent, les camions attendent.", n:'le connecteur d\'une note de service'},
         a2:{w:['par conséquent'], say:"Le quai n'a pas changé, résultat, les camions attendent.", n:'« résultat » ou « donc » à l\'oral'},
         b1:{w:['en revanche'], say:"L'essai coûte quatre cents dollars. En revanche, l'installation coûterait douze mille dollars.", n:'« en revanche » s\'écrit très bien'},
         b2:{w:['en revanche'], say:"L'essai coûte quatre cents piastres. Par contre, l'installation, c'est douze mille.", n:'« par contre » à l\'oral, correct au Québec'},
         c1:{w:['en somme'], say:"En somme : on mesure, on trace, on essaie, on installe.", n:'annonce un vrai résumé, en une phrase'},
         c2:{w:['en somme'], say:"Pour résumer : on mesure, on trace, on essaie, on installe.", n:'même geste, mot plus simple'},
       },
       note:"Écoutez la version formelle et la version courante l'une après l'autre : c'est la même phrase, et ce n'est pas la même réunion."},

      {t:'piege', h:"Deux excès et un manque",
       rows:[
         ["mettre un connecteur à chaque phrase","un toutes les deux ou trois phrases",
          "Au-delà, l'exposé sonne comme une liste d'épicerie : on n'entend plus que les panneaux et plus du tout la route."],
         ["mélanger les registres","choisir et s'y tenir",
          "« En revanche » suivi de « par contre » deux phrases plus loin s'entend comme une hésitation. Dans une lettre, tout est formel ; en réunion, tout peut être courant."],
         ["n'en mettre aucun","au moins aux quatre charnières",
          "Ouvrir, enchaîner, opposer, fermer. Quatre connecteurs dans un exposé de dix minutes est un minimum, pas un maximum."],
       ]},
    ]
  },

  t1futant: {
    eye:'Mini-leçon', tit:"Le futur antérieur, le temps des échéanciers",
    blocs:[
      {t:'texte', h:"Deux choses dans le futur, et il faut dire laquelle d'abord",
       p:"Un échéancier n'est rien d'autre qu'une suite de « ceci avant cela ». Le français a un temps fait exactement pour ça : le <b>futur antérieur</b>. Il porte l'action qui sera <b>déjà terminée</b> quand l'autre arrivera. Sans lui, on peut dire quand les choses se passent, mais pas dans quel ordre — et c'est justement ce que la salle veut savoir.",
       note:"Il s'appelle « antérieur » parce qu'il est antérieur à un autre futur, pas parce qu'il est passé."},

      {t:'ana', h:"Comment il se forme",
       p:"Auxiliaire au futur simple, puis participe passé. Rien d'autre.",
       mots:[['Avec avoir','j\'aurai terminé · nous aurons reçu · ils auront décidé'],['Avec être','elle sera partie · la table sera arrivée',true],['Aux verbes pronominaux','l\'essai se sera terminé']],
       say:"J'aurai terminé. Nous aurons reçu. La table sera arrivée.",
       note:"Le choix de l'auxiliaire est le même qu'au passé composé : si vous dites « elle est partie », vous direz « elle sera partie »."},

      {t:'ana', h:"Les six mots qui l'appellent",
       p:"Après eux, quand les deux actions sont au futur, la première passe au futur antérieur.",
       mots:[['La liste','quand · lorsque · dès que · aussitôt que · une fois que · après que'],['La forme','quand + futur antérieur, puis futur simple',true],['Exemple','Quand l\'essai sera terminé, on décidera.']],
       say:"Quand l'essai sera terminé, on décidera. Dès que nous aurons reçu le prix, je vous le ferai circuler.",
       note:"« Après que » demande l'indicatif, pas le subjonctif — c'est « avant que » qui prend le subjonctif. La confusion est extrêmement répandue, y compris chez les francophones."},

      {t:'ana', h:"L'erreur qui rend un échéancier flou",
       p:"Mettre les deux verbes au futur simple.",
       mots:[['On ne dit pas','Quand nous recevrons le prix, nous déciderons.'],['On dit','Quand nous aurons reçu le prix, nous déciderons.',true],['Ce que ça change','on sait maintenant que la réception vient en premier']],
       say:"Quand nous aurons reçu le prix, nous prendrons la décision.",
       note:"Le premier énoncé n'est pas incompréhensible ; il est simplement moins précis, et dans un échéancier la précision est tout le sujet."},

      {t:'labo', h:"La même phrase, avec et sans",
       p:"Choisissez une étape du projet.",
       axes:[
         {id:'e', lbl:'Quelle étape ?', opts:[['a','les relevés'],['b','la soumission'],['c','la table']]},
         {id:'f', lbl:'Quelle forme ?', opts:[['1','futur antérieur'],['2','futur simple partout']]}],
       out:{
         a1:{w:['nous aurons reçu'], say:"Dès que les relevés auront été compilés, ils seront affichés au babillard.", n:'juste : la compilation vient d\'abord'},
         a2:{w:['nous aurons reçu'], say:"Dès que les relevés seront compilés, ils seront affichés au babillard.", n:'plus flou : les deux semblent simultanés'},
         b1:{w:['nous aurons reçu'], say:"Une fois que nous aurons reçu la soumission, je la ferai circuler.", n:'juste'},
         b2:{w:['nous aurons reçu'], say:"Une fois que nous recevrons la soumission, je la ferai circuler.", n:'boiteux : personne ne dit ça'},
         c1:{w:['nous aurons reçu'], say:"Quand la table sera arrivée, il faudra former les cinq emballeurs.", n:'juste, et l\'accord se fait avec le sujet'},
         c2:{w:['nous aurons reçu'], say:"Quand la table arrivera, il faudra former les cinq emballeurs.", n:'acceptable ici : l\'arrivée est un point, pas une durée'},
       },
       note:"Le dernier cas montre la nuance réelle : quand l'action est instantanée, le futur simple passe. Quand elle a une durée qui doit être finie, il faut le futur antérieur."},

      {t:'check', h:"Quatre questions",
       p:"",
       qs:[
         {q:"« Quand nous ___ le prix, nous déciderons. »", opts:["recevrons","aurons reçu"], ok:1,
          fb:"La réception doit être terminée avant la décision."},
         {q:"L'auxiliaire du futur antérieur est au…", opts:["futur simple","présent"], ok:0,
          fb:"« j'aurai terminé », « je serai parti »."},
         {q:"« Après que » demande…", opts:["l'indicatif","le subjonctif"], ok:0,
          fb:"C'est « avant que » qui prend le subjonctif."},
         {q:"« Quand la table ___ (arriver)… » avec l'auxiliaire être :", opts:["sera arrivée","aura arrivé"], ok:0,
          fb:"« arriver » se conjugue avec être, et le participe s'accorde."},
       ]},
    ]
  },

  t1compte: {
    eye:'Mini-leçon', tit:"Du dit à l'écrit : le compte rendu",
    blocs:[
      {t:'texte', h:"Ce n'est pas une transcription",
       p:"Un compte rendu ne rapporte pas ce qui a été dit : il rapporte ce qui a été <b>décidé et convenu</b>. Il est deux fois plus court que la réunion, il ne garde aucune hésitation, aucun ton, aucune plaisanterie. C'est un document de travail qu'on relira dans six mois pour savoir qui devait faire quoi.",
       note:"Au Québec, on dit aussi <b>procès-verbal</b> — le mot est plus formel et suppose une adoption en début de réunion suivante."},

      {t:'ex', h:"Quatre transformations, toujours les mêmes",
       p:"À gauche ce qui a été dit, à droite ce qui s'écrit.",
       rows:[
         ["« Je vous rappelle qu'on charge dix-neuf camions. »","M. Cormier rappelle que dix-neuf camions sont chargés quotidiennement."],
         ["« On va mesurer pendant deux semaines. »","Relevé des temps d'attente : deux semaines, du 8 au 19 septembre."],
         ["« Je veux que ce soit noté. »","Mme Lapointe demande que le risque soit inscrit au présent compte rendu."],
         ["« Les résultats, je vais les afficher. »","Les résultats seront affichés au babillard. Responsable : R. Cormier."],
       ]},

      {t:'ana', h:"Le passage du « je » au nom",
       p:"Personne ne dit « je » dans un compte rendu, pas même celui qui l'écrit.",
       mots:[['En réunion','« Je vous rappelle… »'],['Au compte rendu','M. Cormier rappelle que…',true],['Pourquoi','le document sera lu par des gens qui n\'étaient pas là']],
       say:"Monsieur Cormier rappelle que le quai n'a pas été modifié depuis deux mille neuf.",
       note:"Le nom est écrit une fois en entier, puis abrégé : « M. Cormier », « M<sup>me</sup> Lapointe »."},

      {t:'ana', h:"Le présent de compte rendu",
       p:"Même trois semaines après, tout est au présent.",
       mots:[['On écrit','M. Cormier présente le projet. Trois risques sont signalés.'],['On n\'écrit pas','M. Cormier a présenté le projet.',true],['Ce que ça donne','un texte plus court et plus net']],
       say:"Monsieur Cormier présente le projet. Trois risques sont signalés.",
       note:"Le futur, lui, reste : « les résultats seront affichés ». Ce qui reste à faire se dit au futur."},

      {t:'ana', h:"La nominalisation : remplacer le verbe par un nom",
       p:"C'est ce qui rend un compte rendu sec, et c'est ce qui le rend court.",
       mots:[['On mesure pendant deux semaines','Relevé des temps d\'attente : deux semaines'],['On va installer','Installation définitive',true],['On décide en novembre','Décision : novembre']],
       say:"Relevé des temps d'attente : deux semaines. Installation définitive : novembre.",
       note:"Trop de noms rend le texte illisible. La bonne mesure : les titres et les listes sont nominalisés, les phrases restent des phrases."},

      {t:'piege', h:"Ce qu'un compte rendu ne fait jamais",
       rows:[
         ["rapporter le ton","rapporter le contenu",
          "« M. Cormier semblait agacé » n'a rien à faire dans un compte rendu. Ce qui compte, c'est ce qu'il a dit et ce qui a été décidé."],
         ["trancher un désaccord","écrire qu'il y a eu désaccord",
          "S'il y a eu deux positions, on écrit les deux. Le compte rendu ne donne raison à personne."],
         ["mélanger décisions et contexte","mettre les décisions à part",
          "Une décision porte un responsable et une date, et se lit seule. Noyée dans un paragraphe, elle est perdue dans trois mois."],
       ]},
    ]
  },

  t1repr: {
    eye:'Mini-leçon', tit:"Reprendre sans répéter",
    blocs:[
      {t:'texte', h:"Le problème que ça règle",
       p:"Écrivez « le projet » cinq fois dans un paragraphe et votre lecteur croira, à la troisième, que vous parlez d'un autre projet. La répétition ne fatigue pas seulement l'oreille : elle <b>désoriente</b>. Reprendre, c'est dire la même chose autrement pour que le lecteur sache qu'il s'agit toujours de la même chose.",
       note:"C'est le deuxième grand savoir de grammaire du texte, après les connecteurs — et le plus discret des deux."},

      {t:'ana', h:"Reprendre par un pronom",
       p:"Le plus court, et le plus risqué.",
       mots:[['Complément direct','le · la · l\' · les — Elle a relu la soumission. Elle la trouve claire.'],['Complément indirect','lui · leur — J\'ai écrit au fournisseur. Je lui ai demandé un délai.',true],['Après une préposition','en (de) · y (à, lieu)']],
       say:"Elle a relu la soumission. Elle la trouve claire.",
       note:"Un pronom ne peut reprendre qu'un nom déjà nommé, et récemment. Trois phrases plus loin, il ne reprend plus rien."},

      {t:'ana', h:"« en » et « y », les deux qu'on oublie",
       p:"Ils reprennent ce qui vient après « de » et après « à ».",
       mots:[['en','Il a parlé du budget. Il en a parlé longtemps.'],['y','Il pense à l\'échéancier. Il y pense depuis lundi.',true],['y de lieu','Le programme est dans le classeur. Personne n\'y a jamais regardé.']],
       say:"Il en a parlé longtemps. Il y pense depuis lundi.",
       note:"Le test : si le verbe se construit avec <i>de</i>, c'est « en ». Avec <i>à</i>, c'est « y »."},

      {t:'ana', h:"Reprendre par un nom qui résume — le plus utile",
       p:"On reprend une phrase entière, ou tout un raisonnement, par deux mots.",
       mots:[['Ce constat','Trois personnes se sont blessées. Ce constat a été présenté en réunion.'],['Cette démarche','On mesure, on trace, on essaie. Cette démarche prendra deux mois.',true],['Cette décision · ce problème · cette situation','les quatre passe-partout de l\'écrit de travail']],
       say:"Ce constat a été présenté en réunion. Cette démarche prendra deux mois et demi.",
       note:"C'est la reprise qui distingue vraiment un texte de niveau 7 : elle demande de <b>résumer</b> ce qui précède, pas seulement de le désigner."},

      {t:'ana', h:"Reprendre par un mot voisin",
       p:"Un synonyme, un terme plus général, un terme plus précis.",
       mots:[['la table élévatrice','l\'appareil · l\'équipement'],['Meubles Rive-du-Nord','l\'entreprise · l\'usine',true],['monsieur Cormier','le chef de production · son supérieur']],
       say:"L'appareil serait installé au poste quatre. L'entreprise compte soixante-deux personnes.",
       note:"C'est ce qui donne à un texte l'air d'avoir été écrit par quelqu'un plutôt que produit par une machine."},

      {t:'piege', h:"L'erreur qui coûte le plus cher",
       rows:[
         ["une reprise ambiguë","répéter le nom",
          "« Il a montré le plan au chef d'équipe. Il l'a trouvé compliqué. » Qui a trouvé quoi compliqué ? Quand deux lectures sont possibles, répétez le nom : ce n'est pas élégant, mais c'est compris."],
         ["reprendre trop loin","reprendre dans la phrase suivante",
          "Un pronom porte sur une ou deux phrases, pas sur un paragraphe. Au-delà, reprenez par un nom qui résume."],
         ["ne jamais reprendre","varier dès la deuxième mention",
          "Le texte qui répète le même groupe du nom huit fois se lit comme une liste de mots-clés. C'est le défaut le plus visible d'un écrit de travail mal relu."],
       ]},
    ]
  },

  t2eval: {
    eye:'Mini-leçon', tit:"Faire une évaluation sommaire",
    blocs:[
      {t:'texte', h:"« Sommaire » ne veut pas dire « approximatif »",
       p:"Une évaluation sommaire est un <b>premier</b> examen, pas un examen bâclé. Elle donne des ordres de grandeur, elle dit d'où viennent ses chiffres, et elle nomme ce qu'elle ne sait pas. Ce qui la distingue d'une évaluation complète, ce n'est pas le sérieux : c'est le nombre de décimales.",
       note:"Le programme du niveau 7 la nomme trois fois : la comprendre, la présenter, la mettre par écrit."},

      {t:'ex', h:"Ce qu'elle contient, ligne par ligne",
       p:"À gauche l'élément, à droite ce qu'il exige.",
       rows:[
         ["Le constat","Ce que vous avez observé, avec la période : « depuis le mois de mars »."],
         ["Les données","D'où elles viennent : le registre, le relevé, le compte. Jamais « il paraît que »."],
         ["La cause probable","Dites « probable » si elle l'est. On ne vous reprochera jamais une prudence annoncée."],
         ["Les conséquences","En jours, en argent, en retards. Ce que le problème coûte si on ne fait rien."],
         ["Les options","Deux au minimum, dont une gratuite. Une option unique n'est pas une évaluation, c'est une demande."],
         ["Ce qui n'est pas connu","La partie que tout le monde saute, et celle qui vous rend crédible."],
         ["La suite proposée","Une action, une personne, une date."],
       ]},

      {t:'texte', h:"Dire ce qu'on ne sait pas",
       p:"Aïcha n'a pas le coût des remplacements par l'agence. Elle aurait pu inventer un chiffre : personne ne l'aurait vérifié sur-le-champ. Elle dit à la place : <i>« Je n'ai pas le chiffre exact, madame Ouellet l'a et je ne voulais pas l'inventer ici. »</i> Cette phrase-là fait plus pour sa crédibilité que tous les chiffres qu'elle a donnés avant.",
       note:"La règle : un chiffre inventé qu'on découvre faux jette le doute sur tous les autres, y compris les vrais."},

      {t:'ana', h:"Le vocabulaire de l'évaluation",
       p:"Six mots qui reviennent dans toutes les évaluations sommaires.",
       mots:[['un constat','ce que j\'ai observé et compté'],['une cause','pourquoi ça arrive',true],['une conséquence','ce que ça produit et ce que ça coûte'],['un correctif','le changement proposé'],['une échéance','la date'],['un responsable','la personne nommée']],
       say:"Un constat, une cause, une conséquence, un correctif, une échéance, un responsable.",
       note:"Employer ces mots-là, tels quels, fait gagner du temps : tout le monde en milieu de travail les connaît."},

      {t:'check', h:"Trois questions",
       p:"",
       qs:[
         {q:"Une évaluation sommaire doit contenir…", opts:["une seule solution, la meilleure","au moins deux options"], ok:1,
          fb:"Une option unique n'est pas une évaluation, c'est une demande."},
         {q:"Vous n'avez pas un chiffre. Que faites-vous ?", opts:["vous l'estimez sans le dire","vous dites que vous ne l'avez pas et qui l'a"], ok:1,
          fb:"C'est ce qui rend crédibles tous vos autres chiffres."},
         {q:"« Sommaire » veut dire…", opts:["premier examen, en ordres de grandeur","fait rapidement, sans vérifier"], ok:0,
          fb:"Le sérieux est le même ; c'est la précision qui diffère."},
       ]},
    ]
  },

  t2emph: {
    eye:'Mini-leçon', tit:"La mise en relief : faire ressortir un mot",
    blocs:[
      {t:'texte', h:"Le problème d'une phrase ordinaire",
       p:"Dans une phrase ordinaire, tous les mots ont à peu près le même poids. Or vous voulez souvent qu'on retienne <b>un</b> mot sur douze. Parler plus fort ne sert à rien : le volume ne désigne rien. Le français a des constructions faites exprès pour ça, et elles sont plus efficaces qu'un ton de voix.",
       note:"On les appelle des <b>phrases emphatiques</b> — cinq points de savoir au niveau 7, ce qui dit assez leur importance."},

      {t:'ana', h:"« ce qui… c'est » — mettre en avant un sujet",
       p:"On isole le sujet de l'action et on le rejette après « c'est ».",
       mots:[['Phrase ordinaire','Se pencher quatre-vingt-deux fois use le dos.'],['Mise en relief','Ce qui use le dos, c\'est de se pencher quatre-vingt-deux fois.',true],['Ce que ça fait','le vrai coupable arrive en fin de phrase, là où on l\'entend']],
       say:"Ce qui use le dos, ce n'est pas le poids d'une caisse, c'est de se pencher quatre-vingt-deux fois.",
       note:"La forme négative est encore plus forte : « ce n'est pas X, c'est Y »."},

      {t:'ana', h:"« ce que… c'est » et « ce dont… c'est »",
       p:"Pour un complément direct, puis pour un complément en « de ».",
       mots:[['Complément direct','Ce que je demande, c\'est l\'autorisation d\'écrire.'],['Complément en « de »','Ce dont j\'ai besoin, c\'est d\'une soumission écrite.',true],['Le repère','« avoir besoin DE » → ce DONT']],
       say:"Ce que je demande, c'est l'autorisation d'écrire. Ce dont j'ai besoin, c'est d'une soumission écrite.",
       note:"« Ce dont » est la forme que les apprenants évitent le plus, et celle qui impressionne le plus quand elle est juste."},

      {t:'ana', h:"« c'est… qui » et « c'est… que »",
       p:"Le mot mis en avant passe tout de suite après « c'est ».",
       mots:[['Il fait l\'action → qui','C\'est la répétition qui blesse, pas le poids.'],['Il subit l\'action → que','C\'est le prix que j\'attends avant de décider.',true],['Une personne','C\'est monsieur Cormier qui a demandé la mise en copie.']],
       say:"C'est la répétition qui blesse. C'est le prix que j'attends.",
       note:"L'erreur classique est « c'est la répétition que blesse ». Le test : remplacez par « elle blesse » — le sujet fait l'action, donc « qui »."},

      {t:'ana', h:"Le détachement à gauche — la forme parlée",
       p:"On sort le mot, on met une virgule, et on le reprend par un pronom.",
       mots:[['On dit','Le poste 4, il nous coûte quinze jours par année.'],['Ou à droite','Il nous coûte cher, le poste 4.',true],['Registre','très courant à l\'oral, correct, plus rare à l\'écrit formel']],
       say:"Le poste quatre, il nous coûte quinze jours par année.",
       note:"À l'écrit d'affaires, préférez « ce qui… c'est ». À l'oral d'une réunion, le détachement passe très bien."},

      {t:'labo', h:"La même idée, quatre façons",
       p:"Choisissez ce que vous voulez mettre en avant.",
       axes:[
         {id:'q', lbl:'Quoi mettre en avant ?', opts:[['a','la cause'],['b','ce que je demande'],['c','la personne']]},
         {id:'f', lbl:'Quelle construction ?', opts:[['1','ce qui / ce que… c\'est'],['2','c\'est… qui / que']]}],
       out:{
         a1:{w:['la moins spectaculaire'], say:"Ce qui use le dos, c'est de se pencher quatre-vingt-deux fois.", n:'la construction la plus neutre'},
         a2:{w:['la moins spectaculaire'], say:"C'est la répétition qui use le dos, pas le poids.", n:'plus tranchant, parce qu\'il y a un contraste'},
         b1:{w:['la moins spectaculaire'], say:"Ce que je demande, c'est l'autorisation d'écrire.", n:'la demande arrive en fin de phrase'},
         b2:{w:['la moins spectaculaire'], say:"C'est l'autorisation d'écrire que je demande, rien de plus.", n:'utile pour corriger un malentendu'},
         c1:{w:['la moins spectaculaire'], say:"Ce que monsieur Cormier a demandé, c'est d'être mis en copie.", n:'on met en avant la demande'},
         c2:{w:['la moins spectaculaire'], say:"C'est monsieur Cormier qui a demandé la mise en copie.", n:'on met en avant la personne'},
       },
       note:"Écoutez les deux versions de chaque paire : ce n'est pas la même information qui reste."},

      {t:'piege', h:"Le dosage, et une faute d'accord",
       rows:[
         ["deux mises en relief de suite","une par minute",
          "Deux insistances collées s'annulent : la salle entend une insistance générale, donc plus aucune insistance."],
         ["« c'est… que » pour un sujet","« c'est… qui »",
          "« C'est la répétition qui blesse », jamais « que blesse ». Remplacez le mot par « elle » : si « elle blesse » se dit, c'est « qui »."],
         ["« ce que j'ai besoin »","« ce dont j'ai besoin »",
          "Le verbe est « avoir besoin DE ». La reprise prend donc « dont », qui contient le « de »."],
       ]},
    ]
  },

  t2passif: {
    eye:'Mini-leçon', tit:"La phrase passive, et ce qu'elle cache",
    blocs:[
      {t:'texte', h:"Pourquoi les écrits de travail en sont pleins",
       p:"Ouvrez n'importe quelle note de service, n'importe quel compte rendu, n'importe quelle politique : vous y trouverez « les résultats seront affichés », « trois risques ont été signalés », « le programme est mis à jour annuellement ». Ce n'est pas un tic de style. Ces textes parlent de <b>ce qui se fait</b>, pas de qui le fait — et la phrase passive est la seule construction qui permet de dire l'un sans l'autre.",
       note:"Le programme demande de la <b>reconnaître</b> et de la comprendre. Produire des passives à tout bout de champ n'est pas le but."},

      {t:'ana', h:"Comment elle se forme",
       p:"Trois mouvements, toujours les mêmes.",
       mots:[['1 · Le complément direct devient sujet','Thérèse a signalé le risque → Le risque…'],['2 · Le verbe passe à être + participe','…a été signalé…',true],['3 · L\'ancien sujet part derrière « par »','…par Thérèse. — ou disparaît.']],
       say:"Thérèse a signalé le risque. Le risque a été signalé par Thérèse. Le risque a été signalé.",
       note:"Le temps du verbe ne change pas : c'est l'auxiliaire <i>être</i> qui le porte. « signale » → « est signalé » ; « signalera » → « sera signalé »."},

      {t:'ana', h:"Le repère pour la reconnaître",
       p:"Deux marques, et il les faut toutes les deux.",
       mots:[['être conjugué','est · sont · a été · sera · avait été'],['+ un participe passé','signalé · affichés · élue · corrigé',true],['+ le sujet ne fait pas l\'action','« la table sera livrée » : la table ne livre rien']],
       say:"La table sera livrée. Les caisses ont été empilées. La demande avait été refusée.",
       note:"Attention : « elle est partie » n'est pas une passive. « Partir » se conjugue avec être — le sujet fait bien l'action."},

      {t:'ana', h:"L'accord du participe",
       p:"Avec être, il suit toujours le sujet.",
       mots:[['masculin singulier','le risque a été signalé'],['féminin singulier','la table sera livrée',true],['féminin pluriel','les caisses ont été empilées'],['masculin pluriel','les résultats seront affichés']],
       say:"Le risque a été signalé. La table sera livrée. Les caisses ont été empilées.",
       note:"C'est l'accord le plus simple du français, et c'est aussi l'oubli le plus visible à l'écrit."},

      {t:'texte', h:"Quand elle devient malhonnête",
       p:"La passive permet de ne pas nommer. C'est utile quand le nom n'a pas d'importance — personne n'a besoin de savoir qui tiendra le rouleau de papier collant au babillard. Elle devient malhonnête quand elle sert à effacer un responsable qu'on devrait nommer : <i>« Des erreurs ont été commises. »</i> Par qui ? La phrase est faite pour éviter la question.",
       note:"Le test, à faire sur vos propres écrits : ajoutez « par qui ? » après chaque passive. Si la réponse compte et n'y est pas, remettez-la."},

      {t:'check', h:"Quatre questions",
       p:"",
       qs:[
         {q:"« La demande a été refusée. » C'est…", opts:["une passive","un passé composé ordinaire"], ok:0,
          fb:"être conjugué + participe, et la demande ne refuse rien."},
         {q:"« Elle est partie à midi. » C'est…", opts:["une passive","un passé composé avec être"], ok:1,
          fb:"Le sujet fait l'action : ce n'est pas une passive."},
         {q:"« Les caisses ont été empil___ »", opts:["empilé","empilées"], ok:1,
          fb:"Avec être, le participe s'accorde avec le sujet."},
         {q:"Pourquoi les comptes rendus emploient-ils la passive ?", opts:["par politesse","parce qu'ils parlent de ce qui se fait, pas de qui le fait"], ok:1,
          fb:"C'est une question de point de vue, pas de politesse."},
       ]},
    ]
  },

  t2cnesst: {
    eye:'Mini-leçon', tit:"Santé et sécurité : ce qui est vrai au Québec",
    blocs:[
      {t:'texte', h:"Deux sortes de règles, et il ne faut pas les confondre",
       p:"Dans une usine, deux sortes de textes vous concernent. Les <b>politiques de l'employeur</b>, qu'il écrit lui-même et qui changent d'une entreprise à l'autre. Et la <b>loi</b>, qui est la même partout au Québec et qu'aucun employeur ne peut réduire. Le programme de prévention de Meubles Rive-du-Nord est du premier type ; le droit de refus est du second.",
       note:"Tout ce qui suit se vérifie sur <b>cnesst.gouv.qc.ca</b>. Les personnes et l'usine de ce module sont inventées ; ces règles-là, non."},

      {t:'ana', h:"Vingt travailleurs : la ligne qui décide de tout",
       p:"Depuis le 1<sup>er</sup> octobre 2025, le Règlement sur les mécanismes de prévention et de participation en établissement s'applique.",
       mots:[['20 travailleurs ou plus','programme de prévention · comité de santé et de sécurité · représentant en santé et en sécurité'],['19 travailleurs ou moins','plan d\'action · agent de liaison en santé et en sécurité',true],['Meubles Rive-du-Nord','soixante-deux personnes : le premier régime']],
       say:"Vingt travailleurs ou plus : un programme de prévention, un comité, un représentant.",
       note:"Le seuil se compte par <b>établissement</b>, pas par entreprise : une compagnie de deux cents personnes réparties en trois petits ateliers relève du second régime pour chacun."},

      {t:'ana', h:"Le programme de prévention",
       p:"Ce n'est pas un document qu'on écrit une fois.",
       mots:[['L\'employeur doit','l\'élaborer, l\'appliquer et le mettre à jour chaque année'],['Tous les trois ans','transmettre à la CNESST les priorités d\'action et le suivi des mesures',true],['Ce qu\'il contient','les risques de l\'établissement et ce qu\'on fait pour les enlever']],
       say:"Le programme de prévention se met à jour annuellement.",
       note:"C'est le document qu'Aïcha ne connaissait pas et qui parlait déjà de son problème : la manutention manuelle répétitive."},

      {t:'ana', h:"Le représentant en santé et en sécurité",
       p:"Ce qui distingue Thérèse d'une gestionnaire.",
       mots:[['Il est élu','par les travailleurs, pas nommé par la direction'],['Au comité','au moins la moitié des membres, dont lui, représentent les travailleurs',true],['Ce que ça change','on peut lui parler sans passer par son supérieur']],
       say:"La représentante en santé et en sécurité est élue par les travailleurs.",
       note:"Le comité de santé et de sécurité réunit les deux côtés. Le représentant, lui, est du côté des travailleurs, et c'est écrit dans la loi."},

      {t:'ana', h:"Le droit de refus",
       p:"Articles 12 et 13 de la Loi sur la santé et la sécurité du travail.",
       mots:[['Article 12','un travailleur peut refuser s\'il a des motifs raisonnables de croire que le travail l\'expose à un danger — ou expose une autre personne à un danger semblable'],['Article 13 — il ne peut pas refuser','si le refus met en péril immédiat une autre personne, ou si les conditions sont normales pour ce genre de travail',true],['En cas de désaccord','l\'inspecteur de la CNESST décide s\'il existe un danger']],
       say:"Un travailleur a le droit de refuser d'exécuter un travail s'il a des motifs raisonnables de croire qu'il l'expose à un danger.",
       note:"« Motifs raisonnables de croire » n'exige pas d'avoir raison : il exige d'avoir des raisons. C'est une nuance juridique importante, et elle protège la personne de bonne foi."},

      {t:'piege', h:"Trois confusions courantes",
       rows:[
         ["croire qu'une politique d'employeur est une loi","demander où c'est écrit",
          "Une politique interne s'applique parce que l'employeur s'y engage. Elle peut être meilleure que la loi, jamais moins bonne."],
         ["croire que le droit de refus sert à tout","le réserver au danger",
          "Il ne sert pas à contester un horaire ou une tâche déplaisante. Il porte sur un danger pour la santé, la sécurité ou l'intégrité."],
         ["croire que refuser règle le problème","refuser fait venir un inspecteur",
          "Le refus déclenche une procédure : on en informe l'employeur, et s'il y a désaccord, l'inspecteur de la CNESST tranche."],
       ]},
    ]
  },

  t3note: {
    eye:'Mini-leçon', tit:"Écrire une note de service",
    blocs:[
      {t:'texte', h:"Le plus court des écrits de travail, et le plus lu",
       p:"Une note de service tient sur une page, souvent sur une demi-page. Elle circule <b>à l'intérieur</b> de l'entreprise, entre des gens qui se connaissent. Elle ne fait pas de phrases : elle informe, elle demande, elle date. Et parce qu'elle est courte, chacun de ses six morceaux se voit — un morceau manquant se remarque tout de suite.",
       note:"C'est l'une des deux intentions de production écrite du programme, à cette situation : « écrire une note de service »."},

      {t:'ex', h:"Les six parties",
       p:"À gauche la partie, à droite ce qu'elle contient.",
       rows:[
         ["L'en-tête","Le nom de l'entreprise, puis DESTINATAIRE, EXPÉDITEUR, DATE, OBJET. Toujours cet ordre, toujours alignés."],
         ["L'objet","Six à dix mots, sans verbe conjugué : « rotation des tâches au poste 4, à l'essai ». C'est souvent la seule ligne lue."],
         ["Le contexte","Une ou deux phrases : pourquoi cette note existe. Aucun reproche, aucune histoire."],
         ["Le message","Ce qui change, avec les dates, les personnes visées, les heures. La partie qui compte."],
         ["La demande","Ce que le lecteur doit faire, avant quand, auprès de qui. Une note qui ne demande rien n'a pas besoin d'exister."],
         ["La signature","Prénom, nom, fonction. Puis « c. c. » s'il y a des copies conformes."],
       ]},

      {t:'texte', h:"Ce qu'une note de service n'a pas",
       p:"Pas de vedette avec l'adresse : les gens sont dans le même bâtiment. Pas d'appel — on n'écrit pas « Monsieur, ». Pas de salutation finale — on ne finit pas par « veuillez agréer ». Ces trois absences sont ce qui distingue une note d'une lettre, et les ajouter ne rend pas la note plus polie : ça la rend étrange.",
       note:"En revanche, elle dit « vous » et elle peut être chaleureuse. « Toute question peut m'être adressée directement » n'est pas une formule creuse."},

      {t:'ana', h:"Les tournures qui font une note",
       p:"Elles sont peu nombreuses et elles reviennent toutes.",
       mots:[['Annoncer','À compter du lundi 22 septembre… · Veuillez prendre note que…'],['Demander','Il vous est demandé de… · Nous vous prions de…',true],['Rassurer','Aucune modification n\'est apportée à…'],['Ouvrir','Toute question peut m\'être adressée directement.']],
       say:"À compter du lundi vingt-deux septembre. Il vous est demandé de noter l'heure de chaque changement.",
       note:"« Il vous est demandé de » est une passive : la note demande, pas la personne. C'est ce qui la rend impersonnelle sans la rendre froide."},

      {t:'piege', h:"Trois erreurs qui se voient de loin",
       rows:[
         ["un objet avec un verbe conjugué","un groupe du nom",
          "« Objet : nous changeons l'horaire du poste 4 » se corrige en « Objet : modification de l'horaire du poste 4 »."],
         ["une note sans date de fin","une échéance écrite",
          "« Pendant quelque temps » n'engage personne. « Pour une période d'essai de quatre semaines » se vérifie."],
         ["terminer par une formule de lettre","terminer par sa fonction",
          "« Veuillez agréer » dans une note de service fait sourire l'équipe. Prénom, nom, fonction, et c'est tout."],
       ]},
    ]
  },

  t3genres: {
    eye:'Mini-leçon', tit:"La lettre d'affaires courantes",
    blocs:[
      {t:'texte', h:"Elle sort de l'entreprise, et elle l'engage",
       p:"C'est la différence de fond avec la note de service. Une note circule entre gens qui se connaissent et n'engage personne au-delà de l'équipe. Une lettre d'affaires part chez un tiers — un fournisseur, un client, un organisme — et ce qui y est écrit peut être invoqué plus tard. D'où sa longueur, ses formules, et le soin qu'on met à ne pas écrire « nous voulons acheter » quand on veut dire « nous demandons un prix ».",
       note:"C'est la seconde intention de production écrite du programme : « rédiger une lettre d'affaires courantes »."},

      {t:'ex', h:"Les sept parties, de haut en bas",
       p:"À gauche la partie, à droite ce qu'elle contient.",
       rows:[
         ["Le lieu et la date","En haut à droite. « Terrebonne, le 17 septembre 2026 ». Le mois ne s'abrège pas."],
         ["La vedette","À gauche : nom, fonction, entreprise, adresse du destinataire. C'est ce qui manque le plus souvent."],
         ["L'objet","« Objet : demande de soumission — table élévatrice à ciseaux ». Sans verbe conjugué."],
         ["L'appel","« Monsieur, » ou « Madame, » seul sur sa ligne, suivi d'une virgule."],
         ["Le corps","Trois paragraphes : pourquoi j'écris, ce que je demande, ce que j'attends comme suite."],
         ["La salutation","Elle reprend l'appel mot pour mot : « Veuillez agréer, Monsieur, mes salutations distinguées. »"],
         ["La signature","Signature manuscrite, nom dactylographié, fonction. Puis « p. j. » et « c. c. » s'il y a lieu."],
       ]},

      {t:'ana', h:"Trois paragraphes, trois travaux",
       p:"Le corps d'une lettre courante ne devrait presque jamais en compter davantage.",
       mots:[['Paragraphe 1','Pourquoi j\'écris. Nous vous écrivons afin d\'obtenir une soumission pour…'],['Paragraphe 2','Ce que je demande, en détail : les données, les options, les questions.',true],['Paragraphe 3','La suite : la date de réponse souhaitée, et ce qui se passera ensuite.']],
       say:"Nous vous écrivons afin d'obtenir une soumission pour une table élévatrice à ciseaux.",
       note:"Un paragraphe, une idée. Un bloc de douze lignes ne se lit pas, quelle que soit sa qualité."},

      {t:'ana', h:"Ne pas engager l'entreprise sans le vouloir",
       p:"La leçon que monsieur Cormier donne à Aïcha en une phrase.",
       mots:[['On écrit','Nous demandons une soumission. · Le projet est à l\'étude.'],['On n\'écrit pas','Nous voulons acheter. · Nous commandons.',true],['La formule qui protège','Sous réserve de l\'approbation du budget…']],
       say:"Nous demandons une soumission. Sous réserve de l'approbation du budget.",
       note:"Dire où l'on en est — « la décision se prend en octobre » — est plus utile au fournisseur qu'un enthousiasme qui n'engage rien."},

      {t:'check', h:"Quatre questions",
       p:"",
       qs:[
         {q:"La salutation finale doit…", opts:["reprendre l'appel du début","varier pour éviter la répétition"], ok:0,
          fb:"Si l'appel dit « Madame », la salutation dit « Madame »."},
         {q:"« p. j. » signifie…", opts:["pièce jointe","pour information"], ok:0,
          fb:"« c. c. » est la copie conforme."},
         {q:"Une note de service a-t-elle un appel ?", opts:["oui","non"], ok:1,
          fb:"Ni appel, ni salutation : c'est ce qui la distingue de la lettre."},
         {q:"Combien de paragraphes dans le corps d'une lettre courante ?", opts:["trois","sept"], ok:0,
          fb:"Pourquoi j'écris, ce que je demande, ce que j'attends."},
       ]},
    ]
  },

  t3formules: {
    eye:'Mini-leçon', tit:"Les formules : à quoi chacune sert",
    blocs:[
      {t:'texte', h:"Ce ne sont pas des politesses vides",
       p:"On croit souvent que les formules d'une lettre d'affaires sont de la décoration. Elles ne le sont pas : chacune fait un <b>travail précis</b> que le lecteur reconnaît immédiatement. « Sous réserve de » ne dit pas la même chose que « nous confirmons ». Employer la mauvaise formule, ce n'est pas manquer de politesse : c'est écrire autre chose que ce qu'on voulait dire.",
       note:"C'est pour ça qu'elles s'apprennent par leur fonction, jamais par cœur en liste."},

      {t:'ex', h:"Huit formules et leur travail",
       p:"À gauche la formule, à droite ce qu'elle fait.",
       rows:[
         ["Nous vous écrivons afin de…","Ouvrir en disant tout de suite pourquoi. Évite les trois lignes d'introduction."],
         ["Je vous saurais gré de bien vouloir…","Demander sans ordonner. La plus utile des huit."],
         ["Sous réserve de…","Prévenir que rien n'est décidé. Protège l'entreprise et informe le fournisseur."],
         ["Vous trouverez ci-joint…","Annoncer un document. Se double d'un « p. j. » en bas de page."],
         ["Nous souhaiterions recevoir votre réponse pour le…","Demander une date sans en faire une exigence."],
         ["Dans l'attente de votre réponse,","Fermer le corps, juste avant la salutation."],
         ["Veuillez agréer, Monsieur, mes salutations distinguées.","Saluer, en reprenant l'appel."],
         ["Nous accusons réception de…","Confirmer qu'un document est arrivé. Se fait dans les jours qui suivent."],
       ]},

      {t:'ana', h:"Les trois degrés de la demande",
       p:"Du plus direct au plus prudent.",
       mots:[['Direct','Envoyez-nous votre prix. — un ordre, réservé à un fournisseur habituel'],['Neutre','Nous vous demandons de nous faire parvenir votre prix.',true],['Prudent','Je vous saurais gré de bien vouloir nous faire parvenir votre prix.']],
       say:"Je vous saurais gré de bien vouloir nous faire parvenir votre prix.",
       note:"« Je vous saurais gré » est du verbe <i>savoir</i> au conditionnel : « je vous saurais gré », jamais « je vous serais gré »."},

      {t:'ana', h:"La salutation, et l'erreur qui se voit",
       p:"Elle reprend l'appel, exactement.",
       mots:[['Appel « Monsieur, »','Veuillez agréer, Monsieur, mes salutations distinguées.'],['Appel « Madame, »','Veuillez agréer, Madame, mes salutations distinguées.',true],['Ce qu\'on n\'écrit pas','Cordialement, dans une lettre d\'affaires formelle']],
       say:"Veuillez agréer, Monsieur, mes salutations distinguées.",
       note:"« Cordialement » et « Bien à vous » appartiennent au courriel, pas à la lettre. Dans un courriel professionnel, ils sont très bien."},

      {t:'piege', h:"Trois formules mal employées",
       rows:[
         ["« Je vous serais gré »","« Je vous saurais gré »",
          "C'est le verbe savoir, pas être. L'erreur est fréquente y compris chez les francophones, et elle se voit."],
         ["« Nous accusons réception » avant d'avoir reçu","seulement après réception",
          "La formule confirme une arrivée. L'employer d'avance n'a aucun sens et engage sur un document qu'on n'a pas vu."],
         ["« Veuillez agréer » sans reprendre l'appel","reprendre l'appel mot pour mot",
          "« Monsieur, » au début et « Veuillez agréer, Madame » à la fin : c'est le signe d'une lettre recopiée sans être relue."],
       ]},
    ]
  },

  t3subj: {
    eye:'Mini-leçon', tit:"Le subjonctif après le verbe qui introduit",
    blocs:[
      {t:'texte', h:"Le mode de ce qui n'est pas encore vrai",
       p:"L'indicatif dit ce qui est. Le subjonctif dit ce qu'on veut, ce qu'on craint, ce qu'on doute, ce qu'on souhaite — bref, ce qui n'est <b>pas encore</b> vrai au moment où on parle. Dans une lettre d'affaires, on souhaite beaucoup et on affirme peu : c'est pourquoi le subjonctif y est partout.",
       note:"Le programme du niveau 7 lui consacre cinq points de savoir."},

      {t:'ana', h:"Comment il se forme",
       p:"Une seule opération, et elle marche pour presque tous les verbes.",
       mots:[['On part de','la 3e personne du pluriel du présent : ils envoient, ils reçoivent'],['On enlève -ent','envoi- · reçoiv-',true],['On ajoute','-e, -es, -e, -ions, -iez, -ent'],['Résultat','que j\'envoie · que nous recevions · qu\'ils reçoivent']],
       say:"Que j'envoie. Que nous recevions. Qu'ils reçoivent.",
       note:"Aux deux premières personnes du pluriel, la forme est celle de l'imparfait : que nous <b>recevions</b>, que vous <b>receviez</b>."},

      {t:'ana', h:"Les six irréguliers qu'il faut savoir",
       p:"Ce sont ceux qui reviennent tout le temps.",
       mots:[['être · avoir','que je sois · que j\'aie · que nous soyons · que nous ayons'],['faire · aller','que je fasse · que j\'aille · que nous fassions · que nous allions',true],['pouvoir · savoir','que je puisse · que je sache · que nous puissions · que nous sachions']],
       say:"Que je sois, que j'aie, que je fasse, que j'aille, que je puisse, que je sache.",
       note:"Six verbes appris une fois couvrent la grande majorité des subjonctifs d'une lettre."},

      {t:'ana', h:"Les verbes qui l'appellent",
       p:"Volonté, souhait, nécessité, sentiment.",
       mots:[['Volonté et souhait','vouloir que · souhaiter que · demander que · exiger que · préférer que · proposer que'],['Nécessité','il faut que · il est nécessaire que · il importe que · il convient que',true],['Sentiment','je regrette que · je crains que · je suis heureux que']],
       say:"Je souhaite que vous nous fassiez parvenir votre soumission. Il faut que la soumission soit valide.",
       note:"« Espérer que » est l'exception qui surprend tout le monde : à la forme affirmative, il prend l'<b>indicatif</b>. « J'espère que vous recevrez ma lettre. »"},

      {t:'ana', h:"Les verbes qui ne l'appellent pas — et qui basculent",
       p:"Déclaration et opinion prennent l'indicatif… tant qu'ils sont affirmatifs.",
       mots:[['Affirmatif → indicatif','Je pense que la table est nécessaire.'],['Négatif → subjonctif','Je ne pense pas que la table soit nécessaire.',true],['Interrogatif → souvent subjonctif','Pensez-vous que ce délai soit réaliste ?']],
       say:"Je pense que la table est nécessaire. Je ne pense pas que la table soit nécessaire.",
       note:"La logique est constante : dès que la certitude tombe, le subjonctif arrive."},

      {t:'labo', h:"Le même verbe, deux modes",
       p:"Choisissez le verbe introducteur et la forme.",
       axes:[
         {id:'v', lbl:'Quel verbe ?', opts:[['a','je souhaite que'],['b','je pense que'],['c','il faut que']]},
         {id:'f', lbl:'Quelle forme ?', opts:[['1','affirmative'],['2','négative']]}],
       out:{
         a1:{w:['une soumission'], say:"Je souhaite que vous nous fassiez parvenir votre soumission.", n:'subjonctif : c\'est un souhait'},
         a2:{w:['une soumission'], say:"Je ne souhaite pas que cela vous fasse perdre du temps.", n:'subjonctif encore : la négation ne change rien ici'},
         b1:{w:['une soumission'], say:"Je pense que ce délai est réaliste.", n:'indicatif : opinion affirmée'},
         b2:{w:['une soumission'], say:"Je ne pense pas que ce délai soit réaliste.", n:'subjonctif : la certitude est tombée'},
         c1:{w:['une soumission'], say:"Il faut que la soumission soit valide jusqu'en novembre.", n:'subjonctif : nécessité'},
         c2:{w:['une soumission'], say:"Il ne faut pas que la soumission expire avant la décision.", n:'subjonctif : nécessité, encore'},
       },
       note:"Écoutez les deux formes de « je pense que » l'une après l'autre : c'est le seul couple du laboratoire où le mode change."},

      {t:'piege', h:"Trois pièges",
       rows:[
         ["« après que » au subjonctif","à l'indicatif",
          "« Après que la direction a approuvé » est la forme correcte. C'est « avant que » qui prend le subjonctif. L'erreur est si répandue qu'elle passe presque inaperçue — presque."],
         ["« espérer que » au subjonctif","à l'indicatif",
          "« J'espère que vous recevrez » et non « que vous receviez ». Verbe d'espoir, mais construction de déclaration."],
         ["éviter le subjonctif par prudence","l'employer là où il s'impose",
          "« Je veux que vous envoyez » n'est pas plus simple : c'est faux, et ça s'entend tout de suite. Six verbes irréguliers appris une fois règlent le problème."],
       ]},
    ]
  },

  t3cond: {
    eye:'Mini-leçon', tit:"Le conditionnel : demander, proposer, nuancer",
    blocs:[
      {t:'texte', h:"Un temps qui sert surtout à ne pas heurter",
       p:"Le conditionnel présent a la réputation de servir aux hypothèses. C'est vrai, mais en milieu de travail son usage principal est ailleurs : il sert à <b>demander sans exiger</b>, à <b>proposer sans imposer</b> et à <b>dire un chiffre dont on n'est pas sûr</b>. Trois emplois, et vous les rencontrerez dans chaque lettre que vous écrirez.",
       note:"Cinq points de savoir au niveau 7, dont l'exemple du programme : « Me passeriez-vous une autre voiture en attendant ? »"},

      {t:'ana', h:"Comment il se forme",
       p:"Le radical du futur, les terminaisons de l'imparfait.",
       mots:[['Réguliers','je demanderais · nous souhaiterions · vous pourriez'],['Radicaux irréguliers du futur','je ferais · j\'irais · je verrais · il faudrait · je voudrais',true],['La marque','-ais, -ais, -ait, -ions, -iez, -aient']],
       say:"Je demanderais. Nous souhaiterions. Vous pourriez. Il faudrait.",
       note:"Si vous savez le futur, vous savez le conditionnel : c'est le même radical."},

      {t:'ana', h:"1 · Demander sans exiger",
       p:"L'emploi le plus fréquent dans une lettre d'affaires.",
       mots:[['On n\'écrit pas','Je veux connaître votre prix.'],['On écrit','Je voudrais connaître votre prix.',true],['Encore plus prudent','Pourriez-vous nous indiquer votre délai de livraison ?']],
       say:"Nous voudrions connaître le prix d'une table élévatrice. Pourriez-vous nous indiquer votre délai ?",
       note:"Il ne s'agit pas d'être gentil : il s'agit de ne pas engager l'autre avant qu'il ait répondu."},

      {t:'ana', h:"2 · Proposer sans imposer",
       p:"En réunion, c'est ce qui ouvre la discussion au lieu de la fermer.",
       mots:[['Fermé','Nous commencerons la rotation le 22 septembre.'],['Ouvert','Nous pourrions commencer la rotation le 22 septembre.',true],['Ce que la salle entend','on me demande mon avis']],
       say:"Nous pourrions commencer la rotation le vingt-deux septembre.",
       note:"Le futur annonce une décision prise ; le conditionnel annonce une décision à prendre. Choisissez selon ce qui est vrai."},

      {t:'ana', h:"3 · Dire ce qui n'est pas certain",
       p:"Un chiffre entendu au téléphone n'est pas une soumission.",
       mots:[['On écrit','L\'installation coûterait entre onze et treize mille dollars.'],['Et on ajoute','selon un premier appel · d\'après une estimation verbale',true],['Ce que ça évite','qu\'on vous cite ce chiffre en octobre comme une promesse']],
       say:"Selon un premier appel, l'appareil coûterait entre quatre et sept mille dollars.",
       note:"C'est le même conditionnel que celui des journalistes : « le local serait loué pour cinq ans »."},

      {t:'ana', h:"4 · L'hypothèse en « si »",
       p:"Imparfait après <i>si</i>, conditionnel dans l'autre partie.",
       mots:[['La forme','Si l\'essai était concluant, nous installerions en novembre.'],['Jamais','Si l\'essai serait concluant…',true],['L\'autre forme, réelle','Si l\'essai est concluant, nous installerons en novembre.']],
       say:"Si l'essai était concluant, nous installerions la table en novembre.",
       note:"La règle absolue : <b>jamais de conditionnel juste après « si »</b>. C'est l'une des rares règles du français qui ne souffre aucune exception."},

      {t:'piege', h:"Le piège de l'écrit",
       rows:[
         ["« je demanderai » pour « je demanderais »","relire tous les verbes en -rai / -rais",
          "À l'oral, la différence s'entend à peine. À l'écrit, le -s change tout : l'un annonce ce que vous ferez, l'autre demande poliment. C'est la faute la plus fréquente dans les lettres d'affaires."],
         ["« si je serais »","« si j'étais »",
          "Aucune exception. Après « si », jamais de conditionnel."],
         ["tout mettre au conditionnel","garder l'indicatif pour les faits",
          "Une lettre entièrement au conditionnel n'a plus l'air prudente : elle a l'air de ne rien savoir. Les faits se disent à l'indicatif ; seules les demandes, les propositions et les estimations passent au conditionnel."],
       ]},
    ]
  },

  t3ponct: {
    eye:'Mini-leçon', tit:"La mise en page fait partie du message",
    blocs:[
      {t:'texte', h:"Ce n'est pas de la coquetterie",
       p:"Le programme du niveau 7 range la <b>présentation matérielle</b> parmi les savoirs de grammaire du texte, au même titre que les connecteurs. La raison est simple : dans un écrit de travail, la mise en page porte de l'information. Un objet en gras dit « lisez ceci d'abord ». Trois paragraphes disent « il y a trois idées ». Un bloc de douze lignes dit « je n'ai pas trié ».",
       note:"Un texte impeccable et mal présenté est lu de travers. Un texte moyen et bien présenté est lu."},

      {t:'ex', h:"Les règles qui reviennent",
       p:"À gauche la règle, à droite l'exemple.",
       rows:[
         ["La date ne s'abrège pas","« Terrebonne, le 17 septembre 2026 » — jamais « 17/09/26 »."],
         ["L'objet n'a pas de verbe conjugué","« Objet : demande de soumission — table élévatrice »."],
         ["L'appel prend une virgule","« Monsieur, » — ni point, ni deux-points, ni point d'exclamation."],
         ["Une seule paire de deux-points","« Trois données sont requises : la charge, les dimensions et la hauteur. »"],
         ["Espace avant les signes doubles","Une espace avant ? ! ; : et avant le guillemet fermant."],
         ["Les abréviations d'usage","M. · Mme · p. j. · c. c. · 2e — « Mr » est anglais."],
         ["Un paragraphe, une idée","Trois paragraphes de quatre lignes valent mieux qu'un bloc de douze."],
       ]},

      {t:'ana', h:"Les abréviations que vous emploierez",
       p:"Peu nombreuses, et toujours les mêmes.",
       mots:[['Les personnes','M. · Mme · Mmes · MM.'],['Les documents','p. j. (pièce jointe) · c. c. (copie conforme) · N/Réf. (notre référence)',true],['Les nombres','1er · 2e · 3e — jamais « 1ère » ni « 2ème »']],
       say:"Monsieur. Madame. Pièce jointe. Copie conforme. Premier. Deuxième.",
       note:"« Mr » est l'abréviation anglaise. En français, c'est « M. » — un M majuscule et un point."},

      {t:'texte', h:"Ce que la mise en page dit avant qu'on lise",
       p:"Une personne pressée regarde d'abord la forme : y a-t-il un objet ? des paragraphes ? une date ? une signature ? Si oui, elle lit. Sinon, elle remet à plus tard, et « plus tard » veut souvent dire jamais. Soigner la forme n'est pas un raffinement : c'est ce qui décide si votre texte est lu le jour où il compte.",
       note:"Le test que vous pouvez faire seul : regardez votre lettre à un mètre de distance, sans la lire. Si vous ne voyez pas où sont l'objet, les paragraphes et la signature, personne ne les verra."},

      {t:'check', h:"Quatre questions",
       p:"",
       qs:[
         {q:"« Terrebonne, 17/09/26 » dans une lettre :", opts:["correct","à corriger"], ok:1,
          fb:"Le mois s'écrit en toutes lettres : « le 17 septembre 2026 »."},
         {q:"Après l'appel « Monsieur », on met…", opts:["une virgule","deux-points"], ok:0,
          fb:"« Monsieur, » seul sur sa ligne."},
         {q:"L'abréviation française de « Monsieur » est…", opts:["M.","Mr"], ok:0,
          fb:"« Mr » est anglais."},
         {q:"« 2ème » s'écrit…", opts:["2e","2ème"], ok:0,
          fb:"Deuxième s'abrège « 2e », avec le e en exposant."},
       ]},
    ]
  },

};
