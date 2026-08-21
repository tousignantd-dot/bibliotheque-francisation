const PLUS = {

  // ════════════════════════════════════════════════════════════════════════
  prPhon: {
    eye:'Mini-leçon', tit:"Le son de « an » et le son de « on »",
    blocs:[
      {t:'texte', h:"Deux sons du nez, et la moitié du bulletin",
       p:"Comptez-les dans une seule chronique de circulation : ralentissement, accident, sens, quarante, lentement, entrave d'un côté ; pont, bouchon, camion, circulation, direction, contournement de l'autre. Ces deux voyelles portent presque tous les mots du métier. Elles se ressemblent parce que l'air passe par le nez dans les deux cas — mais la bouche ne fait pas du tout la même chose, et c'est là-dessus qu'on s'appuie.",
       note:"Confondre les deux ne fait pas seulement une faute de prononciation : ça fait entendre « le pont » quand on dit « le pan », et refaire son trajet pour rien un matin de semaine."},

      {t:'ana', h:"Le son de « an » : la bouche grande ouverte",
       p:"La bouche s'ouvre largement, la langue reste basse, l'air sort par le nez. On l'écrit an, am, en ou em — quatre orthographes, un seul son.",
       mots:[["Dans l'état de la route","un ralentissement · lentement · un embouteillage"],["Dans l'incident","un accident · dans les deux sens · une entrave",true],["Dans les durées","trente minutes · quarante minutes · pendant la fin de semaine"]],
       say:"Un ralentissement. Un accident. Quarante minutes.",
       note:"Le mot le plus utile de la liste est « ralentissement » : quatre syllabes, deux voyelles nasales de la même famille. Dites-le lentement, syllabe par syllabe, avant de le dire vite."},

      {t:'ana', h:"Le son de « on » : les lèvres en petit rond",
       p:"Les lèvres se ferment en rond, la langue recule, l'air sort encore par le nez. On l'écrit on ou om.",
       mots:[["Les ouvrages de la route","un pont · un tronçon · un contournement"],["Les véhicules et le trafic","un camion · un bouchon · la circulation",true],["Les mots du bulletin","en direction de · on annonce · une intersection"]],
       say:"Un pont. Un bouchon. En direction de Montréal.",
       note:"« En direction de » contient les deux sons dans le même souffle : « an » d'abord, « on » ensuite. C'est le meilleur exercice du module, et il revient dix fois par bulletin."},

      {t:'ana', h:"Le geste qui règle tout",
       p:"Mettez la main devant la bouche, à deux centimètres. Sur « an », la main sent une ouverture large et de l'air chaud. Sur « on », elle sent un petit rond serré. La différence est visible, pas seulement audible.",
       mots:[["Les paires à sentir","lent / long · sans / son · banc / bon"],["Les paires du métier","le pan / le pont · le rang / le rond",true],["Le mot qui contient les deux","un contournement · en direction de"]],
       say:"Lent, long. Sans, son. Banc, bon.",
       note:"Regardez les lèvres de la personne qui parle quand vous le pouvez. Une bonne moitié de l'écoute passe par les yeux, et personne ne vous le dit jamais."},

      {t:'labo', h:"Écoutez la paire, puis le mot dans sa phrase",
       p:"Choisissez une paire de mots et écoutez la différence, puis le mot replacé dans une phrase du bulletin.",
       axes:[{id:'p', lbl:'Quelle paire ?', opts:[
         ['a','lent / long'],
         ['b','sans / son'],
         ['c','banc / bon'],
         ['d','le pan / le pont'],
         ['e','les cinq à la suite']]}],
       out:{
         a:{w:['un ralentissement'], say:"Lent. Long. Ça roule lentement sur un long tronçon.", n:"« an » bouche ouverte, « on » lèvres en rond"},
         b:{w:['un bouchon'], say:"Sans. Son. Le bouchon se défait sans son klaxon.", n:"la même consonne au départ, deux voyelles différentes"},
         c:{w:['une entrave'], say:"Banc. Bon. Aucune entrave : c'est une bonne nouvelle.", n:"écoutez la fin du mot, pas le début"},
         d:{w:['un ralentissement','un bouchon'], say:"Le pan. Le pont. Le pont est fermé jusqu'à neuf heures.", n:"la paire qui coûte le plus cher dans un bulletin"},
         e:{w:['un ralentissement','un bouchon'], say:"Lent, long. Sans, son. Banc, bon. Le pan, le pont.", n:"quatre paires à la suite, sans reprendre son souffle"},
       },
       note:"Écoutez chaque paire deux fois : la première pour entendre les deux mots, la seconde en ne guettant que la position de vos propres lèvres."},

      {t:'ex', h:"À écouter et à répéter",
       p:"Six phrases prises dans les bulletins du module.",
       rows:[
         ["On annonce un ralentissement de vingt minutes.","les deux sons dans la même phrase"],
         ["Le pont est fermé dans les deux sens.","« on » au début, « an » à la fin"],
         ["Un camion est immobilisé sur l'accotement.","« on » deux fois de suite"],
         ["L'accident bloque la circulation en direction ouest.","« an », puis « on » deux fois"],
         ["Quarante minutes entre les deux sorties.","« an » trois fois"],
         ["En direction de Montréal, la circulation est dense.","le mot à deux sons, puis « an »"],
       ]},

      {t:'piege', h:"Trois pièges des voyelles nasales",
       rows:[
         ["prononcer le « n » ou le « m » qui suit","« ral-en-ti-sse-menne », avec un n final",
          "Dans une voyelle nasale, la lettre n ne se prononce pas : elle indique seulement que l'air passe par le nez. « Ralentissement » finit sur la voyelle, la langue ne touche rien. Le n s'entend seulement quand une voyelle suit : « un accident » — « un-n-accident »."],
         ["ouvrir les lèvres sur « on »","« un boucheann » au lieu de « un bouchon »",
          "Les lèvres doivent se fermer en rond, comme pour siffler. Si elles restent larges, « bouchon » devient « bouchan » et le mot n'existe plus. Exercez-vous devant une vitre : le rond doit être visible."],
         ["croire que l'orthographe décide","« em » et « en » lus comme deux sons différents",
          "an, am, en, em donnent tous le même son : embouteillage, temps, entrave, ralentissement. Ne cherchez pas quatre prononciations là où il n'y en a qu'une — c'est l'oreille qui commande, pas l'écriture."],
       ]},

      {t:'check', h:"Est-ce que c'est clair maintenant ?",
       p:"Quatre questions rapides.",
       qs:[
         {q:"Dans « un bouchon », les lèvres…", opts:["s'ouvrent largement","se ferment en petit rond"], ok:1,
          fb:"Elles se ferment en rond. C'est le geste du son de « on »."},
         {q:"« Embouteillage » contient le son…", opts:["de « an »","de « on »"], ok:0,
          fb:"Celui de « an ». Le « em » du début se dit comme « an »."},
         {q:"Dans « ralentissement », le n final…", opts:["se prononce","ne se prononce pas"], ok:1,
          fb:"Il ne se prononce pas : il indique seulement que l'air passe par le nez."},
         {q:"« En direction de » contient…", opts:["les deux sons","seulement celui de « on »"], ok:0,
          fb:"Les deux : « an » dans « en », « on » dans « direction »."},
       ]},
    ]
  },

  // ════════════════════════════════════════════════════════════════════════
  prEtat: {
    eye:'Mini-leçon', tit:"Quatre états de la route, quatre décisions",
    blocs:[
      {t:'texte', h:"Le mot dit ce qu'il faut faire",
       p:"Un bulletin de circulation n'a que quelques mots pour décrire l'état d'une route, et chacun commande une décision différente. Un ralentissement, on part quand même. Un bouchon, on cherche autre chose. Une route fermée, on suit la directive. Une entrave, on écoute la suite pour savoir laquelle. Ce n'est pas du vocabulaire de luxe : c'est de l'information qui vaut vingt minutes de votre matinée.",
       note:"Beaucoup de gens qui parlent très bien français ne font pas la différence entre « ralentissement » et « bouchon » parce qu'ils n'ont jamais eu besoin de la faire. Vous, vous en avez besoin dès demain matin."},

      {t:'ana', h:"Ralentissement : ça avance, mais lentement",
       p:"Les autos roulent à trente ou quarante à l'heure au lieu de cent. Le bulletin le mesure en minutes de plus qu'à l'habitude.",
       mots:[["Comment ça se dit","un ralentissement · la circulation est ralentie · ça roule au ralenti"],["La mesure","vingt minutes de plus qu'à l'habitude · quinze minutes entre les deux sorties",true],["La décision","on y va, on part dix minutes plus tôt"]],
       say:"On annonce un ralentissement de vingt minutes entre la quinze et la sortie Marcel-Laurin.",
       note:"« La circulation est dense mais fluide » est la formule voisine : dense veut dire qu'il y a beaucoup d'autos, fluide veut dire que ça avance quand même. Les deux mots ensemble sont rassurants."},

      {t:'ana', h:"Bouchon : ça ne bouge presque plus",
       p:"Les autos sont pare-chocs contre pare-chocs. On gagne dix mètres à la minute, et personne ne sait pour combien de temps.",
       mots:[["Comment ça se dit","un bouchon · un embouteillage · la circulation est très dense"],["Ce qu'on entend aussi","c'est bloqué · c'est arrêté · le bouchon remonte jusqu'au pont",true],["La décision","on change de chemin si on en a un, sinon on prévient"]],
       say:"À sept heures, le bouchon commençait avant même le pont.",
       note:"« Le bouchon remonte » est une image utile : le bouchon grandit vers l'arrière, donc vers vous. Entendre « ça remonte jusqu'à » vous dit jusqu'où il est rendu."},

      {t:'ana', h:"Fermé : on ne passe pas du tout",
       p:"Une route, un pont, une voie ou une bretelle fermés ne sont pas une question de patience : il n'y a pas de passage. Le bulletin donne alors une directive.",
       mots:[["Comment ça se dit","fermé · fermé dans les deux sens · fermé jusqu'à neuf heures"],["La directive qui suit","Empruntez le pont Victoria. · Suivez le détour indiqué.",true],["La décision","on prend ce que le bulletin propose, sans discuter"]],
       say:"Le pont Jacques-Cartier est fermé en direction de Montréal jusqu'à neuf heures. Empruntez le pont Victoria.",
       note:"Une fermeture s'accompagne presque toujours d'une heure de réouverture, parce qu'elle est prévue. Notez cette heure : c'est la seule information dont vous aurez besoin."},

      {t:'ana', h:"Entrave : le mot qui les couvre tous",
       p:"Une entrave, c'est tout ce qui empêche de circuler normalement. Le bulletin l'emploie sans arrêt parce qu'il n'a pas encore dit de quoi il s'agit.",
       mots:[["Ce que ça peut être","des travaux · un accident · une voie fermée · un camion en panne"],["La bonne nouvelle","aucune entrave à signaler · rien à signaler dans le tunnel",true],["La décision","on écoute la suite : le mot précis vient toujours après"]],
       say:"Aucune entrave à signaler dans le pont-tunnel ce matin.",
       note:"« Aucune entrave à signaler » est la meilleure phrase de la journée, et elle s'apprend d'un bloc : c'est une formule figée, on ne la construit pas mot à mot."},

      {t:'labo', h:"La même route, quatre états",
       p:"Choisissez un état et écoutez comment le bulletin l'annonce.",
       axes:[{id:'e', lbl:'Quel état ?', opts:[
         ['a','Ça avance lentement'],
         ['b','Ça ne bouge plus'],
         ['c','C\'est fermé'],
         ['d','Un véhicule sur l\'accotement'],
         ['e','Rien à signaler']]}],
       out:{
         a:{w:['un ralentissement'], say:"Ralentissement sur l'autoroute quarante en direction ouest : vingt minutes de plus qu'à l'habitude.", n:"on part quand même, un peu plus tôt"},
         b:{w:['un bouchon'], say:"La circulation est très dense sur l'autoroute quarante : le bouchon remonte jusqu'à la quinze.", n:"on cherche un autre chemin"},
         c:{w:['une entrave'], say:"L'autoroute quarante est fermée en direction ouest jusqu'à neuf heures. Empruntez le boulevard.", n:"on suit la directive du bulletin"},
         d:{w:["l'accotement",'une remorqueuse'], say:"Un véhicule lourd est immobilisé sur l'accotement : une remorqueuse est en route.", n:"la circulation n'est pas touchée, pour le moment"},
         e:{w:['une entrave'], say:"Aucune entrave à signaler sur l'autoroute quarante ce matin.", n:"la meilleure phrase de la journée"},
       },
       note:"Écoutez les cinq à la suite un matin, puis essayez de reconnaître lequel passe à la radio le lendemain."},

      {t:'ex', h:"À écouter et à répéter",
       p:"Six phrases du bulletin, une par état.",
       rows:[
         ["On annonce un ralentissement de vingt minutes.","ça avance : on y va"],
         ["Le bouchon remonte jusqu'au pont.","ça ne bouge plus : on change de chemin"],
         ["La voie de gauche est fermée jusqu'à cinq heures.","une voie sur trois, pas toute la route"],
         ["Un camion est immobilisé sur l'accotement.","en dehors des voies : ça inquiète, ça ne bloque pas"],
         ["Aucune entrave à signaler dans le tunnel.","rien du tout : la meilleure phrase"],
         ["La circulation est dense mais fluide.","beaucoup d'autos, mais ça avance"],
       ]},

      {t:'piege', h:"Trois pièges de l'état des routes",
       rows:[
         ["prendre « dense » pour « bloqué »","« C'est dense » compris comme « c'est arrêté »",
          "Dense veut dire : beaucoup d'autos. Le bulletin ajoute presque toujours « mais fluide », qui veut dire que ça avance. Dense et fluide ensemble, c'est une bonne nouvelle, pas une mauvaise."],
         ["croire qu'une voie fermée ferme la route","« la voie de gauche est fermée » compris comme une fermeture complète",
          "Une voie n'est pas la route. « Deux voies sur trois sont bloquées » veut dire qu'il en reste une, donc que ça passe, lentement. « La route est fermée » est une autre phrase, et le bulletin la dit autrement."],
         ["ignorer « pour le moment »","« la circulation n'est pas touchée pour le moment »",
          "Cette petite formule annonce que la personne au micro s'attend au pire. Quand vous l'entendez, écoutez le bulletin suivant : il y a de bonnes chances que ce soit touché."],
       ]},

      {t:'check', h:"Est-ce que c'est clair maintenant ?",
       p:"Quatre questions rapides.",
       qs:[
         {q:"« Un ralentissement de vingt minutes » veut dire…", opts:["que ça avance lentement","que c'est arrêté"], ok:0,
          fb:"Que ça avance, mais lentement : vingt minutes de plus qu'à l'habitude."},
         {q:"« Deux voies sur trois sont bloquées » veut dire…", opts:["que la route est fermée","qu'il en reste une d'ouverte"], ok:1,
          fb:"Qu'il en reste une. Ça passe, lentement — ce n'est pas une fermeture."},
         {q:"« Aucune entrave à signaler » veut dire…", opts:["rien ne bloque","on ne sait pas encore"], ok:0,
          fb:"Rien ne bloque : ni travaux, ni accident, ni voie fermée."},
         {q:"Un véhicule sur l'accotement…", opts:["bloque une voie","est en dehors des voies"], ok:1,
          fb:"Il est en dehors des voies. Ça n'empêche pas de passer, mais ça se signale."},
       ]},
    ]
  },

  // ════════════════════════════════════════════════════════════════════════
  t1ou: {
    eye:'Mini-leçon', tit:"Dire où, exactement",
    blocs:[
      {t:'texte', h:"Un repère ne suffit jamais",
       p:"« Il y a un accident sur la 40 » ne dit presque rien : l'autoroute 40 traverse toute l'île, et l'accident est peut-être à quarante kilomètres de vous, dans l'autre sens. Un bulletin donne toujours deux repères, jamais un seul : la route, puis la précision. C'est cette deuxième partie que les gens manquent, parce qu'elle arrive vite et qu'elle est faite de petites prépositions.",
       note:"Quand vous expliquez une entrave à quelqu'un, la règle est la même : si votre phrase ne contient qu'un nom de route, elle ne fait décider personne."},

      {t:'ana', h:"Sur — la route elle-même",
       p:"On dit sur une route, une autoroute, un pont, un boulevard, une rue. C'est la préposition de base, et elle s'emploie même quand on est dessous ou dedans, au sens propre.",
       mots:[["Les autoroutes","sur l'autoroute 40 · sur la 15 · sur la 25"],["Les autres routes","sur le boulevard Henri-Bourassa · sur le pont Victoria",true],["L'exception qui s'entend tous les jours","dans le tunnel · dans le pont-tunnel"]],
       say:"Un accident sur l'autoroute quarante. Une entrave sur le boulevard Henri-Bourassa.",
       note:"Un tunnel prend « dans » parce qu'il est fermé de tous les côtés ; un pont prend « sur » parce qu'on roule dessus. C'est la seule irrégularité de la série."},

      {t:'ana', h:"À la hauteur de — le point précis",
       p:"C'est la locution la plus employée du bulletin. Elle veut dire : à ce point-là de la route, en face de ce repère. On l'emploie quand il n'y a ni adresse ni intersection à donner.",
       mots:[["Avec une sortie","à la hauteur de la sortie Côte-de-Liesse · à la hauteur de la sortie 65"],["Avec un ouvrage","à la hauteur du pont · à la hauteur de l'échangeur",true],["Avec un quartier","à la hauteur de Pie-IX · à la hauteur de Saint-Laurent"]],
       say:"L'accident se trouve à la hauteur de la sortie Côte-de-Liesse.",
       note:"Attention à la contraction : à la hauteur <b>de la</b> sortie, mais à la hauteur <b>du</b> pont. C'est la règle ordinaire de « de » devant un nom masculin."},

      {t:'ana', h:"Entre… et… — la portion de route",
       p:"On l'emploie quand l'entrave n'est pas un point mais un bout de route. Les deux repères se donnent toujours dans le sens où l'on roule.",
       mots:[["Deux sorties","entre la sortie 65 et la sortie 70"],["Deux routes","entre la quinze et la quarante · entre la vingt et la trente",true],["Deux rues","entre Lajeunesse et Saint-Denis"]],
       say:"Vingt minutes de plus qu'à l'habitude entre la quinze et la sortie Marcel-Laurin.",
       note:"Si vous entendez « entre » et que vous ne saisissez que le premier repère, notez-le quand même : savoir où ça commence suffit souvent à décider."},

      {t:'ana', h:"En direction de — le sens, et la moitié de la décision",
       p:"Une entrave dans l'autre sens ne vous concerne pas du tout. C'est l'information qu'on oublie le plus souvent, et c'est celle qui fait faire des détours pour rien.",
       mots:[["Les points cardinaux","en direction ouest · en direction nord · en direction sud"],["Les destinations","en direction de Montréal · en direction du centre-ville",true],["Les deux à la fois","dans les deux sens · dans les deux directions"]],
       say:"La circulation est dense en direction de Montréal. Le pont est fermé dans les deux sens.",
       note:"Le matin, les gens de la Rive-Sud vont en direction de Montréal ; le soir, dans l'autre sens. Sachez laquelle des deux est la vôtre à quelle heure, et vous éliminerez la moitié du bulletin sans effort."},

      {t:'labo', h:"La même entrave, dite en entier",
       p:"Choisissez une entrave et écoutez comment le bulletin la situe, avec ses deux repères et son sens.",
       axes:[{id:'l', lbl:'Quelle entrave ?', opts:[
         ['a','Un accident sur la 40'],
         ['b','Une fermeture de pont'],
         ['c','Un camion en panne'],
         ['d','Un nid-de-poule'],
         ['e','Une bretelle en travaux']]}],
       out:{
         a:{w:['une voie'], say:"Un accident sur l'autoroute quarante, à la hauteur de la sortie Côte-de-Liesse, en direction ouest : deux voies sur trois sont bloquées.", n:"route, repère, sens, nombre de voies"},
         b:{w:['une entrave'], say:"Le pont Jacques-Cartier est fermé en direction de Montréal jusqu'à neuf heures.", n:"l'ouvrage, le sens, l'heure de réouverture"},
         c:{w:["l'accotement",'une remorqueuse'], say:"Un véhicule lourd est immobilisé sur l'accotement, à la hauteur de la sortie Pie-IX, en direction ouest.", n:"sur l'accotement : en dehors des voies"},
         d:{w:['un nid-de-poule'], say:"Un nid-de-poule important sur le boulevard Henri-Bourassa, en direction est, entre Lajeunesse et Saint-Denis.", n:"une portion de rue, entre deux repères"},
         e:{w:['une bretelle'], say:"La bretelle qui mène de la quinze nord à la quarante ouest sera fermée toute la fin de semaine.", n:"deux routes et deux directions dans la même phrase"},
       },
       note:"Écoutez chacune deux fois : la première pour la route, la seconde pour le sens. Ce sont les deux moitiés de la décision."},

      {t:'ex', h:"À écouter et à répéter",
       p:"Six annonces complètes, avec leurs deux repères.",
       rows:[
         ["Un accident sur la quarante, à la hauteur de Côte-de-Liesse.","route + point précis"],
         ["Le pont est fermé en direction de Montréal.","ouvrage + sens"],
         ["Vingt minutes de plus entre la quinze et Marcel-Laurin.","portion de route"],
         ["Un camion sur l'accotement, à la hauteur de Pie-IX.","en dehors des voies + point précis"],
         ["Tout est ouvert dans le tunnel, dans les deux sens.","« dans » le tunnel, et les deux sens"],
         ["Prudence dans la voie de droite, en direction est.","une voie + un sens"],
       ]},

      {t:'piege', h:"Trois pièges des prépositions de lieu",
       rows:[
         ["dire « dans l'autoroute »","« Il y a un accident dans la quarante »",
          "On roule <b>sur</b> une autoroute, un boulevard, un pont, une rue. « Dans » est réservé au tunnel, et à rien d'autre dans ce vocabulaire. C'est une des rares règles du module qui n'a aucune exception."],
         ["oublier le sens","« Il y a un carambolage sur la quarante » et rien de plus",
          "L'autre personne va peut-être changer de chemin pour une entrave qui est dans l'autre sens. Le sens fait la moitié de l'information : ajoutez-le toujours, même quand vous croyez que c'est évident."],
         ["confondre « à la hauteur de » et « à »","« à la sortie Côte-de-Liesse » pour dire « en face de »",
          "« À la sortie » veut dire que ça se passe dans la sortie elle-même ; « à la hauteur de la sortie » veut dire que ça se passe sur l'autoroute, en face de cette sortie. Le bulletin distingue les deux, et ce n'est pas un détail quand on décide de sortir ou non."],
       ]},

      {t:'check', h:"Est-ce que c'est clair maintenant ?",
       p:"Quatre questions rapides.",
       qs:[
         {q:"On dit…", opts:["sur l'autoroute 40","dans l'autoroute 40"], ok:0,
          fb:"Sur l'autoroute. « Dans » ne s'emploie que pour le tunnel."},
         {q:"« À la hauteur de la sortie » veut dire…", opts:["dans la sortie","en face de la sortie"], ok:1,
          fb:"En face de la sortie, sur la route principale."},
         {q:"Une entrave « en direction est » concerne…", opts:["tout le monde","ceux qui roulent vers l'est"], ok:1,
          fb:"Seulement ceux qui roulent vers l'est. Le sens fait la moitié de la décision."},
         {q:"« Entre la 15 et Marcel-Laurin » désigne…", opts:["un point précis","une portion de route"], ok:1,
          fb:"Une portion : tout le bout de route compris entre les deux repères."},
       ]},
    ]
  },

  // ════════════════════════════════════════════════════════════════════════
  t1qd: {
    eye:'Mini-leçon', tit:"Depuis quand, et pour combien de temps",
    blocs:[
      {t:'texte', h:"Deux questions, pas une",
       p:"Devant une entrave, tout le monde pose la mauvaise question : « Combien de temps ? » Il y en a deux, et elles ne se répondent pas de la même façon. <b>Depuis quand</b> ça dure vous dit si c'est en train de finir ou si ça commence. <b>Pour combien de temps encore</b> vous dit s'il faut attendre ou partir. Le français a une expression différente pour chacune, et les mélanger fait dire le contraire de ce qu'on veut.",
       note:"Quand Tereza dit « ça fait presque une heure », elle donne les deux informations d'un coup : ça a commencé il y a une heure, et ce n'est pas fini. C'est la tournure la plus efficace du module."},

      {t:'ana', h:"Depuis + le moment où ça a commencé",
       p:"On donne l'heure du début, et ça dure encore maintenant. C'est la réponse directe à « depuis quand ? ».",
       mots:[["Avec une heure","depuis six heures et demie · depuis sept heures"],["Avec un moment","depuis ce matin · depuis la nuit dernière · depuis hier",true],["Avec une durée, aussi","depuis une heure · depuis vingt minutes"]],
       say:"La voie est bloquée depuis six heures et demie.",
       note:"« Depuis » accepte les deux : un moment de départ (depuis sept heures) ou une durée (depuis une heure). C'est la seule expression de la série qui fait les deux."},

      {t:'ana', h:"Il y a + une durée écoulée",
       p:"On compte à reculons à partir de maintenant. Attention : « il y a » ne dit pas si c'est fini ou non — il dit seulement quand ça s'est passé.",
       mots:[["Le moment de l'accident","l'accident s'est produit il y a quarante minutes"],["Le moment de l'annonce","on l'a annoncé il y a dix minutes · il y a deux bulletins",true],["Ce qu'on ne dit pas","il y a depuis une heure"]],
       say:"L'accident s'est produit il y a quarante minutes.",
       note:"Ne dites jamais « il y a depuis » : ce sont deux constructions différentes, et les mettre ensemble est l'erreur la plus courante à ce niveau."},

      {t:'ana', h:"Ça fait… que — la tournure du français parlé",
       p:"Elle met la durée en avant, et elle dit du même coup que ça continue. C'est celle qu'on emploie au téléphone, quand on veut être compris tout de suite.",
       mots:[["La forme complète","ça fait presque une heure que c'est bloqué"],["Avec une négation","ça fait vingt minutes qu'on n'a pas avancé",true],["À l'imparfait, pour raconter","ça faisait une heure qu'on attendait"]],
       say:"Ça fait presque une heure que c'est arrêté.",
       note:"« Ça fait une heure que… » et « c'est bloqué depuis une heure » disent exactement la même chose. Apprenez les deux : la première s'entend, la seconde s'écrit."},

      {t:'ana', h:"Pendant, dans, jusqu'à — ce qui reste à venir",
       p:"Ces trois-là regardent vers l'avant. <b>Pendant</b> donne la durée complète, <b>dans</b> un délai à partir de maintenant, <b>jusqu'à</b> l'heure où ça finit.",
       mots:[["Pendant + une durée","fermée pendant toute la fin de semaine · pendant deux jours"],["Dans + un délai","prochain bulletin dans dix minutes · dans une heure",true],["Jusqu'à + une heure de fin","fermé jusqu'à neuf heures · jusqu'à cinq heures du matin"]],
       say:"Le pont est fermé jusqu'à neuf heures. Prochain bulletin dans dix minutes.",
       note:"« Jusqu'à » est le mot le plus précieux du bulletin : c'est le seul qui vous donne une heure à laquelle vous pourrez repartir. Notez-la, toujours."},

      {t:'labo', h:"La même entrave, quatre façons de dire le temps",
       p:"Choisissez une façon de dire le temps et écoutez-la dans une phrase du module.",
       axes:[{id:'t', lbl:'Quelle expression ?', opts:[
         ['a','depuis'],
         ['b','il y a'],
         ['c','ça fait… que'],
         ['d','pendant'],
         ['e','jusqu\'à']]}],
       out:{
         a:{w:['une entrave'], say:"La voie de gauche est bloquée depuis six heures et demie.", n:"le moment du début, et ça dure encore"},
         b:{w:['un carambolage'], say:"Le carambolage s'est produit il y a quarante minutes.", n:"on compte à reculons depuis maintenant"},
         c:{w:['un bouchon'], say:"Ça fait presque une heure que le bouchon ne bouge plus.", n:"la durée en avant, à l'oral"},
         d:{w:['une bretelle'], say:"La bretelle sera fermée pendant toute la fin de semaine.", n:"la durée complète, du début à la fin"},
         e:{w:['un imprévu'], say:"Le pont est fermé jusqu'à neuf heures ce matin.", n:"l'heure à laquelle ça finit"},
       },
       note:"Écoutez les cinq à la suite, puis redites la même entrave avec deux expressions différentes. C'est l'exercice qui les fixe."},

      {t:'ex', h:"À écouter et à répéter",
       p:"Six phrases prises dans les bulletins et dans l'appel à l'atelier.",
       rows:[
         ["C'est bloqué depuis six heures et demie.","le début, et ça continue"],
         ["L'accident s'est produit il y a quarante minutes.","à reculons depuis maintenant"],
         ["Ça fait presque une heure que ça ne bouge plus.","la tournure du téléphone"],
         ["La bretelle sera fermée pendant toute la fin de semaine.","la durée complète"],
         ["Le pont est fermé jusqu'à neuf heures.","l'heure de réouverture"],
         ["Prochain bulletin dans dix minutes.","un délai à partir de maintenant"],
       ]},

      {t:'piege', h:"Trois pièges des expressions de temps",
       rows:[
         ["mélanger « il y a » et « depuis »","« Il y a depuis une heure que c'est bloqué »",
          "Choisissez : « C'est bloqué depuis une heure » ou « Ça a commencé il y a une heure ». Les deux ensemble ne forment pas une phrase française, et c'est l'erreur la plus fréquente à ce niveau."],
         ["employer « pendant » pour un accident","« L'accident bloque la route pendant vingt minutes »",
          "« Pendant » s'emploie pour ce qui est prévu, dont on connaît la fin : des travaux, une fermeture annoncée. Un accident ne se planifie pas — on dit « pour au moins vingt minutes » ou « on ne sait pas encore »."],
         ["dire « dans » pour une heure de fin","« Le pont est fermé dans neuf heures »",
          "« Dans » compte à partir de maintenant : dans neuf heures, ce serait cet après-midi. Pour dire l'heure où ça finit, c'est <b>jusqu'à</b> : le pont est fermé jusqu'à neuf heures."],
       ]},

      {t:'check', h:"Est-ce que c'est clair maintenant ?",
       p:"Quatre questions rapides.",
       qs:[
         {q:"« C'est bloqué depuis sept heures » veut dire…", opts:["que ça a commencé à sept heures","que ça finira à sept heures"], ok:0,
          fb:"Que ça a commencé à sept heures, et que ça dure encore."},
         {q:"« Fermé jusqu'à neuf heures » veut dire…", opts:["fermé à partir de neuf heures","rouvert à neuf heures"], ok:1,
          fb:"Rouvert à neuf heures. « Jusqu'à » donne l'heure de la fin."},
         {q:"« Ça fait une heure que c'est arrêté » veut dire la même chose que…", opts:["c'est arrêté depuis une heure","ça sera arrêté pendant une heure"], ok:0,
          fb:"C'est arrêté depuis une heure. Les deux tournures sont équivalentes."},
         {q:"« Prochain bulletin dans dix minutes » : le bulletin passe…", opts:["dans dix minutes","depuis dix minutes"], ok:0,
          fb:"Dans dix minutes : « dans » compte vers l'avant."},
       ]},
    ]
  },

  // ════════════════════════════════════════════════════════════════════════
  t1inc: {
    eye:'Mini-leçon', tit:"Prévu ou imprévu : deux familles d'entraves",
    blocs:[
      {t:'texte', h:"La question qui change tout",
       p:"Devant une entrave, une seule question compte vraiment : est-ce que quelqu'un le savait d'avance ? Si oui, il y a une heure de fin, elle est publiée, et vous pouvez organiser votre trajet la veille. Si non, personne ne peut vous dire quand ce sera fini — pas même la personne au micro. Toute la différence entre les deux familles tient là, et elle décide de ce que vous faites de votre matinée.",
       note:"Au Québec, ce qui est prévu se trouve sur Québec 511 : la ligne téléphonique 511 et le site du ministère des Transports, qui publient les travaux et les fermetures planifiées. Ce qui n'est pas prévu passe d'abord à la radio, parce qu'elle parle pendant que ça se passe."},

      {t:'ana', h:"Ce qui est prévu : les travaux et les fermetures planifiées",
       p:"On les annonce des jours à l'avance, avec une heure de début et une heure de fin. Ils reviennent souvent aux mêmes heures, toutes les nuits ou toutes les fins de semaine.",
       mots:[["Les mots qui l'annoncent","des travaux · un chantier · une réfection · une fermeture planifiée"],["Les durées typiques","toutes les nuits de vingt-trois heures à cinq heures · toute la fin de semaine",true],["Ce qu'on peut faire","le savoir la veille · refaire son trajet tranquillement"]],
       say:"La bretelle sera fermée toute la fin de semaine pour des travaux de réfection de la chaussée.",
       note:"Une fermeture planifiée finit à l'heure dite, sauf quand les travaux de nuit « se prolongent » — la formule exacte du bulletin quand le chantier a pris du retard."},

      {t:'ana', h:"Ce qui arrive : l'accident, la panne, le nid-de-poule",
       p:"Personne ne le savait il y a dix minutes. Le bulletin est alors plus rapide que n'importe quel site, mais il ne peut pas vous dire quand ce sera fini.",
       mots:[["Les mots qui l'annoncent","un accident · un carambolage · une panne · un nid-de-poule"],["Les formules du bulletin","vient de se produire · on nous signale · en cours de dégagement",true],["Ce qu'on peut faire","décider en trente secondes, avec ce qu'on a entendu"]],
       say:"Un carambolage de quatre véhicules vient de se produire sur l'autoroute quarante.",
       note:"« On nous signale » veut dire que l'information vient d'arriver et n'est pas encore complète. Le bulletin suivant, dix minutes plus tard, en dira davantage."},

      {t:'ana', h:"Les véhicules qui disent combien de temps",
       p:"Le bulletin nomme les véhicules présents, et chacun est une indication de durée sans qu'on ait besoin de la dire.",
       mots:[["Une remorqueuse en route","ça va durer : elle n'est pas encore arrivée"],["Une remorqueuse sur place","ça commence : il faut charger le véhicule",true],["Des véhicules d'urgence","ce sera long : on ne rouvre pas tant qu'ils y sont"]],
       say:"Deux remorqueuses sont sur place ; les policiers dirigent la circulation sur la voie de droite.",
       note:"Amine décide de passer par le boulevard non pas parce que c'est plus court, mais parce que les remorqueuses viennent d'arriver — donc que personne ne sait quand ce sera fini. C'est du raisonnement, pas du vocabulaire."},

      {t:'ana', h:"Se ranger pour les véhicules d'urgence",
       p:"Quand une ambulance, un camion de pompiers ou une auto de police arrive derrière vous avec ses gyrophares, la loi vous demande de vous ranger à droite et d'arrêter.",
       mots:[["Ce qu'on fait","se ranger à droite · immobiliser son véhicule · attendre qu'il soit passé"],["Ce qu'on ne fait pas","accélérer pour dégager · rouler sur l'accotement pour le laisser passer",true],["Ce que le bulletin dit","on demande de laisser passer les véhicules d'urgence"]],
       say:"On demande aux automobilistes de laisser passer les véhicules d'urgence.",
       note:"Il existe aussi une règle du corridor de sécurité : en passant près d'un véhicule d'urgence arrêté sur le bord de la route, on ralentit et on se déplace dans la voie voisine quand c'est possible."},

      {t:'labo', h:"Prévu ou imprévu ?",
       p:"Choisissez une annonce et écoutez-la, puis regardez ce qu'elle vous dit de faire.",
       axes:[{id:'a', lbl:'Quelle annonce ?', opts:[
         ['a','Des travaux de fin de semaine'],
         ['b','Un carambolage'],
         ['c','Des travaux de nuit prolongés'],
         ['d','Un camion en panne'],
         ['e','Un nid-de-poule']]}],
       out:{
         a:{w:['une bretelle'], say:"La bretelle sera fermée samedi et dimanche pour des travaux de réfection.", n:"prévu : on refait son trajet la veille"},
         b:{w:['un carambolage','une remorqueuse'], say:"Un carambolage de quatre véhicules vient de se produire ; les remorqueuses sont sur place.", n:"imprévu : on décide tout de suite"},
         c:{w:['une entrave'], say:"Le pont est fermé jusqu'à neuf heures : les travaux de nuit se prolongent.", n:"prévu, mais en retard : l'heure de fin a bougé"},
         d:{w:["l'accotement",'une remorqueuse'], say:"Un véhicule lourd est immobilisé sur l'accotement ; une remorqueuse est en route.", n:"imprévu, mais la circulation n'est pas touchée"},
         e:{w:['un nid-de-poule'], say:"On nous signale un nid-de-poule important dans la voie de droite.", n:"imprévu : le dégel les creuse en une nuit"},
       },
       note:"À Montréal, un nid-de-poule se signale au 311. Il en apparaît des milliers au printemps, quand le gel et le dégel se succèdent."},

      {t:'ex', h:"À écouter et à répéter",
       p:"Six annonces, trois de chaque famille.",
       rows:[
         ["La bretelle sera fermée toute la fin de semaine.","prévu : une heure de fin existe"],
         ["Un carambolage vient de se produire.","imprévu : personne ne sait pour combien de temps"],
         ["La voie de gauche est fermée toutes les nuits.","prévu : ça revient tous les jours"],
         ["Une remorqueuse est en route.","imprévu : ça ne fait que commencer"],
         ["Les travaux de nuit se prolongent.","prévu, mais en retard"],
         ["On nous signale un nid-de-poule important.","imprévu : l'information vient d'arriver"],
       ]},

      {t:'piege', h:"Trois pièges devant une entrave",
       rows:[
         ["croire qu'un accident finit à l'heure annoncée","« vingt minutes » compris comme une promesse",
          "Les vingt minutes annoncées sont une estimation faite pendant que ça se passe. Si les remorqueuses viennent d'arriver, ce sera plus long. Le chiffre est une indication, pas un horaire."],
         ["partir quand même parce qu'on est déjà en retard","« de toute façon, je suis en retard »",
          "C'est le raisonnement qui coûte le plus cher : on entre dans le bouchon, et là on ne peut plus rien décider. Tant qu'on n'est pas engagé, on a le choix ; après, on ne l'a plus."],
         ["oublier de prévenir avant d'entrer dans le bouchon","téléphoner une fois arrêté depuis vingt minutes",
          "Le meilleur moment pour appeler est celui où l'on comprend qu'on sera en retard, pas celui où l'on est certain de combien. Un appel de trente secondes à sept heures vingt vaut mieux qu'une explication parfaite à huit heures et quart."],
       ]},

      {t:'check', h:"Est-ce que c'est clair maintenant ?",
       p:"Quatre questions rapides.",
       qs:[
         {q:"« Des travaux de réfection toute la fin de semaine », c'est…", opts:["prévu","imprévu"], ok:0,
          fb:"Prévu : c'est annoncé d'avance, avec un début et une fin."},
         {q:"Une remorqueuse « en route » veut dire…", opts:["que c'est presque fini","qu'elle n'est pas encore arrivée"], ok:1,
          fb:"Qu'elle n'est pas encore arrivée : le dégagement n'a même pas commencé."},
         {q:"« Les travaux de nuit se prolongent » veut dire…", opts:["qu'ils ont pris du retard","qu'ils commencent plus tard"], ok:0,
          fb:"Qu'ils ont pris du retard : la fermeture dure plus longtemps que prévu."},
         {q:"Quand un véhicule d'urgence arrive derrière vous…", opts:["on accélère pour dégager","on se range à droite et on arrête"], ok:1,
          fb:"On se range à droite et on immobilise son véhicule. C'est la loi."},
       ]},
    ]
  },

  // ════════════════════════════════════════════════════════════════════════
  t2rel: {
    eye:'Mini-leçon', tit:"Qui, que, où, dont : coller deux phrases en une",
    blocs:[
      {t:'texte', h:"Pourquoi le bulletin en est plein",
       p:"Un bulletin ne dit pas : « La bretelle est fermée. Elle mène à la quarante ouest. » Il dit : « La bretelle <b>qui</b> mène à la quarante ouest est fermée. » Une phrase au lieu de deux, et l'information de <i>laquelle</i> bretelle il s'agit est donnée au passage, sans ralentir. C'est exactement ce que le niveau 5 appelle un discours organisé : les idées ne se suivent pas, elles s'emboîtent.",
       note:"Ces quatre petits mots sont ce qui sépare un français scolaire d'un français adulte. Ils ne s'apprennent pas par cœur : ils s'attrapent en écoutant, puis en essayant."},

      {t:'ana', h:"Qui — le sujet du verbe qui suit",
       p:"Après « qui », il y a tout de suite un verbe, et c'est la chose nommée avant qui fait l'action.",
       mots:[["Sur la route","la voie qui reste ouverte · le camion qui bloque la sortie"],["Dans le bulletin","la bretelle qui mène à la quarante · la remorqueuse qui vient d'arriver",true],["Pour les personnes","le collègue qui conduit · la responsable qui décroche"]],
       say:"La voie de droite est la seule qui reste ouverte.",
       note:"« Qui » ne se raccourcit jamais devant une voyelle : on dit « le camion qui est arrêté », jamais « qu'est arrêté ». C'est « que » qui devient « qu' », pas « qui »."},

      {t:'ana', h:"Que — le complément direct",
       p:"Après « que », il y a un sujet, puis un verbe. Le truc qui ne trompe pas : si vous pouvez mettre « il », « nous » ou « vous » juste après, c'est « que ».",
       mots:[["Le chemin","le chemin que nous prenons · la sortie que vous cherchez"],["L'information","l'entrave qu'ils annoncent · l'heure qu'elle a donnée",true],["La forme raccourcie","qu'il · qu'elle · qu'on · qu'ils"]],
       say:"Le chemin que nous prenons ce matin passe par le boulevard.",
       note:"Devant une voyelle, « que » devient « qu' » et se colle au mot suivant : l'entrave qu'on annonce, la sortie qu'il a manquée."},

      {t:'ana', h:"Où — le lieu, et aussi le moment",
       p:"« Où » remplace un lieu, mais aussi un moment. C'est une des rares fois où le français emploie le même mot pour l'espace et pour le temps.",
       mots:[["Un lieu","l'endroit où l'accident s'est produit · la sortie où il faut tourner"],["Un moment","le matin où le pont était fermé · le jour où j'ai commencé",true],["Ce qu'on évite","le jour que je suis arrivée"]],
       say:"C'est l'endroit où l'accident s'est produit.",
       note:"« Le jour que » s'entend beaucoup dans la langue parlée. Ce n'est pas ce qui s'écrit : on dit et on écrit « le jour où »."},

      {t:'ana', h:"Dont — quand la suite commence par « de »",
       p:"On dit parler <b>de</b> quelque chose, annoncer la fin <b>de</b> quelque chose, avoir besoin <b>de</b> quelque chose. Ce « de » devient « dont ».",
       mots:[["Avec parler","la sortie dont je vous parlais · les travaux dont on a parlé"],["Avec un nom","les travaux dont on annonce la fin · la route dont la chaussée est refaite",true],["Avec avoir besoin","le détour dont nous avons besoin"]],
       say:"La sortie dont je vous parlais est juste après le pont.",
       note:"Le test est simple : si la deuxième phrase, dite seule, contient « de », c'est « dont ». « Je vous parlais de cette sortie » → la sortie <b>dont</b> je vous parlais."},

      {t:'labo', h:"Deux phrases, puis une seule",
       p:"Choisissez un couple de phrases et écoutez comment elles n'en font plus qu'une.",
       axes:[{id:'r', lbl:'Quel couple ?', opts:[
         ['a','La bretelle · elle mène à la 40'],
         ['b','Le chemin · nous le prenons'],
         ['c','L\'endroit · l\'accident s\'y est produit'],
         ['d','La sortie · je vous en parlais'],
         ['e','La voie · elle reste ouverte']]}],
       out:{
         a:{w:['une bretelle'], say:"La bretelle qui mène de la quinze nord à la quarante ouest est fermée.", n:"qui : la bretelle fait l'action de mener"},
         b:{w:['un détour'], say:"Le chemin que nous prenons ce matin passe par le boulevard.", n:"que : « nous » suit tout de suite"},
         c:{w:['la chaussée'], say:"C'est l'endroit où l'accident s'est produit.", n:"où : un lieu"},
         d:{w:['un détour'], say:"La sortie dont je vous parlais est juste après le pont.", n:"dont : on parle « de » la sortie"},
         e:{w:['une voie'], say:"La voie de droite est la seule qui reste ouverte.", n:"qui : la voie fait l'action de rester"},
       },
       note:"Faites l'exercice à l'envers aussi : prenez une phrase du bulletin avec un relatif et coupez-la en deux. C'est ce qui montre d'où vient le pronom."},

      {t:'ex', h:"À écouter et à répéter",
       p:"Six phrases du module, une par emploi.",
       rows:[
         ["La bretelle qui mène à la quarante ouest est fermée.","qui : sujet"],
         ["La voie de droite est la seule qui reste ouverte.","qui : sujet"],
         ["Le chemin que nous prenons passe par le boulevard.","que : complément direct"],
         ["C'est l'endroit où l'accident s'est produit.","où : lieu"],
         ["Le matin où le pont était fermé, nous sommes arrivés à neuf heures.","où : moment"],
         ["La sortie dont je vous parlais est après le pont.","dont : avec « de »"],
       ]},

      {t:'piege', h:"Trois pièges des pronoms relatifs",
       rows:[
         ["mettre « qui » là où il faut « que »","« le chemin qui nous prenons »",
          "Après « qui », il y a un verbe tout de suite. Ici, « nous » suit — donc c'est « que » : le chemin <b>que</b> nous prenons. Le test tient en une seconde : regardez le mot juste après."],
         ["raccourcir « qui » devant une voyelle","« le camion qu'est arrêté »",
          "« Qui » ne s'élide jamais : le camion <b>qui</b> est arrêté. Seul « que » devient « qu' ». C'est une des rares règles du français qui n'a aucune exception."],
         ["dire « le jour que »","« le jour que je suis arrivée au Québec »",
          "Pour un moment comme pour un lieu, c'est <b>où</b> : le jour où je suis arrivée. Très courant à l'oral, mais ce n'est pas ce qui s'écrit — et le module travaille aussi l'écrit."],
       ]},

      {t:'check', h:"Est-ce que c'est clair maintenant ?",
       p:"Quatre questions rapides.",
       qs:[
         {q:"« La bretelle ___ mène à la 40 » demande…", opts:["qui","que"], ok:0,
          fb:"« Qui » : un verbe suit tout de suite, et c'est la bretelle qui mène."},
         {q:"« Le chemin ___ nous prenons » demande…", opts:["qui","que"], ok:1,
          fb:"« Que » : « nous » suit, donc ce n'est pas un sujet."},
         {q:"Pour « le jour ___ je suis arrivée », on écrit…", opts:["que","où"], ok:1,
          fb:"« Où ». Il sert pour le moment comme pour le lieu."},
         {q:"« La sortie ___ je vous parlais » demande…", opts:["dont","que"], ok:0,
          fb:"« Dont » : on parle <b>de</b> quelque chose."},
       ]},
    ]
  },

  // ════════════════════════════════════════════════════════════════════════
  t2dir: {
    eye:'Mini-leçon', tit:"Les consignes du bulletin",
    blocs:[
      {t:'texte', h:"Le seul moment où l'on vous parle",
       p:"Pendant cinquante secondes, le bulletin décrit. Et puis, deux ou trois fois, il s'adresse à vous : « Empruntez le pont Victoria. » « Il est recommandé d'éviter le secteur. » « On demande aux automobilistes de réduire leur vitesse. » Ces phrases-là sont les seules qui vous demandent de faire quelque chose. Les reconnaître au passage, c'est savoir quand il faut agir.",
       note:"Les trois tournures disent la même chose avec plus ou moins de force : l'impératif commande, « il est recommandé » conseille, « on demande aux automobilistes » rapporte une demande des autorités."},

      {t:'ana', h:"L'impératif : la forme courte",
       p:"Deuxième personne du pluriel, sans « vous » devant. C'est la forme la plus fréquente à la radio parce que c'est la plus rapide.",
       mots:[["Changer de route","Empruntez le pont Victoria. · Suivez le détour indiqué."],["Faire attention","Évitez le secteur. · Prudence dans la voie de droite.",true],["Prévoir","Prévoyez vingt minutes de plus. · Partez plus tôt."]],
       say:"Empruntez le pont Victoria. Évitez le secteur.",
       note:"Le verbe « emprunter » veut dire ici « prendre une route ». Il ne veut pas dire emprunter de l'argent — c'est un des mots du métier, et il surprend la première fois."},

      {t:'ana', h:"La phrase impersonnelle : personne ne commande",
       p:"Le « il » ne remplace personne : c'est un « il » de forme, comme dans « il pleut ». La consigne existe, mais elle ne vient de personne en particulier.",
       mots:[["Il est recommandé de","Il est recommandé d'éviter le secteur."],["Il faut","Il faut prévoir vingt minutes de plus. · Il faut ralentir.",true],["Il y a, il reste","Il y a un ralentissement de vingt minutes. · Il reste une voie ouverte."]],
       say:"Il est recommandé d'éviter le secteur. Il faut prévoir vingt minutes de plus.",
       note:"C'est ce « il » sans personne derrière qui rend la consigne polie : on ne vous donne pas d'ordre, on vous informe qu'il y a une chose recommandée."},

      {t:'ana', h:"On demande aux automobilistes de…",
       p:"Le « on » désigne les autorités sans les nommer : la police, le ministère, les pompiers. Après cette formule vient toujours un verbe à l'infinitif.",
       mots:[["La forme complète","On demande aux automobilistes de réduire leur vitesse."],["Les verbes qui suivent","de ralentir · d'éviter · de laisser passer · de suivre",true],["Les variantes","On invite les automobilistes à… · On recommande de…"]],
       say:"On demande aux automobilistes de laisser passer les véhicules d'urgence.",
       note:"Après « de », le verbe ne se conjugue jamais : on demande de <b>ralentir</b>, pas « on demande de vous ralentissez ». C'est l'erreur la plus fréquente avec cette tournure."},

      {t:'ana', h:"Les trois, l'une après l'autre",
       p:"La même consigne peut se dire des trois façons. C'est utile pour comprendre, et utile pour dire : quand vous rapportez une directive, vous pouvez choisir la forme.",
       mots:[["La forte","Évitez le secteur."],["La moyenne","Il est recommandé d'éviter le secteur.",true],["La rapportée","On demande aux automobilistes d'éviter le secteur."]],
       say:"Évitez le secteur. Il est recommandé d'éviter le secteur. On demande aux automobilistes d'éviter le secteur.",
       note:"Quand vous répétez une directive à quelqu'un, la forme rapportée est la plus naturelle : « Ils disent d'emprunter le pont Victoria. » Elle dit clairement que la consigne n'est pas de vous."},

      {t:'labo', h:"La même consigne, trois formes",
       p:"Choisissez une consigne et écoutez-la dans ses trois formes.",
       axes:[{id:'c', lbl:'Quelle consigne ?', opts:[
         ['a','Éviter le secteur'],
         ['b','Emprunter un autre pont'],
         ['c','Réduire sa vitesse'],
         ['d','Laisser passer les urgences'],
         ['e','Prévoir plus de temps']]}],
       out:{
         a:{w:['un détour'], say:"Évitez le secteur. Il est recommandé d'éviter le secteur. On demande aux automobilistes d'éviter le secteur.", n:"forte, moyenne, rapportée"},
         b:{w:['un détour'], say:"Empruntez le pont Victoria. Il est recommandé d'emprunter le pont Victoria.", n:"« emprunter » veut dire prendre une route"},
         c:{w:['la chaussée'], say:"Réduisez votre vitesse. On demande aux automobilistes de réduire leur vitesse.", n:"« votre » à l'impératif, « leur » dans la rapportée"},
         d:{w:["un véhicule d'urgence"], say:"Laissez passer les véhicules d'urgence. Il faut laisser passer les véhicules d'urgence.", n:"après « il faut », l'infinitif"},
         e:{w:['un imprévu'], say:"Prévoyez vingt minutes de plus. Il est recommandé de prévoir vingt minutes de plus.", n:"prévoyez, puis de prévoir"},
       },
       note:"Remarquez le changement de possessif dans la forme rapportée : « réduisez <b>votre</b> vitesse » devient « de réduire <b>leur</b> vitesse », parce qu'on ne parle plus à la même personne."},

      {t:'ex', h:"À écouter et à répéter",
       p:"Six directives entendues dans les bulletins du module.",
       rows:[
         ["Empruntez le pont Victoria.","impératif : la forme courte"],
         ["Prudence dans la voie de droite.","un nom seul, sans verbe : très fréquent"],
         ["Il est recommandé d'éviter le secteur.","impersonnel : personne ne commande"],
         ["Il faut prévoir vingt minutes de plus.","impersonnel + infinitif"],
         ["On demande aux automobilistes de ralentir.","rapportée : les autorités, sans les nommer"],
         ["Ils disent d'emprunter le boulevard.","ce que vous direz à votre collègue"],
       ]},

      {t:'piege', h:"Trois pièges des consignes",
       rows:[
         ["conjuguer le verbe après « de »","« on demande de vous ralentissez »",
          "Après « de », le verbe reste à l'infinitif : on demande de <b>ralentir</b>, il est recommandé d'<b>éviter</b>, il faut <b>prévoir</b>. Aucune exception."],
         ["mettre « vous » devant l'impératif","« Vous empruntez le pont Victoria »",
          "Ce n'est plus une consigne, c'est une affirmation — et l'auditeur ne sait plus s'il doit faire quelque chose. L'impératif se dit sans pronom : Empruntez. Évitez. Prévoyez."],
         ["comprendre « emprunter » au sens de l'argent","« emprunter le pont » entendu comme « payer »",
          "Dans le vocabulaire de la route, emprunter une route veut dire la prendre. C'est un mot du métier, comme « entrave » : il ne s'utilise presque jamais ainsi ailleurs."],
       ]},

      {t:'check', h:"Est-ce que c'est clair maintenant ?",
       p:"Quatre questions rapides.",
       qs:[
         {q:"« Empruntez le pont Victoria » veut dire…", opts:["prenez ce pont","payez pour ce pont"], ok:0,
          fb:"Prenez ce pont. « Emprunter » est le mot du métier."},
         {q:"Après « on demande aux automobilistes de », le verbe est…", opts:["conjugué","à l'infinitif"], ok:1,
          fb:"À l'infinitif : de ralentir, d'éviter, de laisser passer."},
         {q:"Dans « il est recommandé de… », le « il »…", opts:["remplace quelqu'un","ne remplace personne"], ok:1,
          fb:"Il ne remplace personne : c'est un « il » de forme, comme dans « il pleut »."},
         {q:"L'impératif se dit…", opts:["sans pronom devant","avec « vous » devant"], ok:0,
          fb:"Sans pronom : Empruntez, Évitez, Prévoyez."},
       ]},
    ]
  },

  // ════════════════════════════════════════════════════════════════════════
  t3ger: {
    eye:'Mini-leçon', tit:"Le gérondif : dire par où et comment",
    blocs:[
      {t:'texte', h:"Trois mots pour expliquer un détour",
       p:"« En sortant à Marcel-Laurin et en prenant le boulevard, on arrive à huit heures quinze. » Une phrase, deux gérondifs, un chemin complet et une heure d'arrivée. Sans le gérondif, il faudrait dire : « Nous sortons à Marcel-Laurin. Ensuite, nous prenons le boulevard. Et comme ça, nous arrivons à huit heures quinze. » Trois phrases pour la même chose, et l'autre a déjà décroché.",
       note:"Le programme du niveau 5 le nomme explicitement : l'adulte emploie le gérondif pour marquer la simultanéité ou la manière. C'est une des marques du passage au stade intermédiaire."},

      {t:'ana', h:"Comment il se forme",
       p:"On prend le verbe à « nous » au présent, on enlève -ons, on ajoute -ant, et on met « en » devant. Trois verbes seulement font autrement.",
       mots:[["La règle","nous passons → en passant · nous prenons → en prenant"],["D'autres verbes du module","nous sortons → en sortant · nous suivons → en suivant · nous écoutons → en écoutant",true],["Les trois exceptions","être → en étant · avoir → en ayant · savoir → en sachant"]],
       say:"En passant. En prenant. En sortant. En écoutant.",
       note:"La forme en -ant est la même pour tous les sujets : en passant, que ce soit je, tu, nous ou elles. Rien ne s'accorde, rien ne change."},

      {t:'ana', h:"La manière : par quel moyen on y arrive",
       p:"C'est l'emploi central du module. Le gérondif dit comment on règle le problème, et il tient en deux ou trois mots.",
       mots:[["Éviter une entrave","En passant par le boulevard, on évite l'autoroute."],["Gagner du temps","En partant à six heures, vous éviterez le bouchon.",true],["Un chemin complet","En sortant à Marcel-Laurin et en prenant le boulevard, on arrive à huit heures quinze."]],
       say:"En passant par le boulevard, on évite tout le secteur.",
       note:"Le gérondif de manière répond à la question « comment ? » ou « par où ? ». C'est exactement la question que votre collègue vous posera."},

      {t:'ana', h:"La simultanéité : deux choses en même temps",
       p:"Les deux actions se passent au même moment, et c'est la même personne qui fait les deux.",
       mots:[["Dans l'auto","Il écoute la radio en conduisant."],["Le matin","Elle a entendu le bulletin en déjeunant.",true],["Au travail","On prend une note en écoutant le message."]],
       say:"Elle a entendu le bulletin en déjeunant.",
       note:"Le gérondif ne change pas avec le temps de la phrase : « elle a entendu… en déjeunant » au passé, « elle entendra… en déjeunant » au futur. Un seul verbe porte le temps, l'autre reste en -ant."},

      {t:'ana', h:"La règle qui ne se contourne pas",
       p:"Le sujet du gérondif est toujours celui de la phrase. Une seule personne fait les deux actions.",
       mots:[["Correct","En écoutant la radio, nous avons appris l'accident."],["Faux","En écoutant la radio, l'accident a été annoncé.",true],["La réparation","Pendant que nous écoutions la radio, l'accident a été annoncé."]],
       say:"En écoutant la radio, nous avons appris l'accident.",
       note:"Ce n'est pas l'accident qui écoute la radio. Quand les deux actions n'ont pas le même sujet, on abandonne le gérondif et on emploie « pendant que »."},

      {t:'labo', h:"Deux phrases, puis une seule",
       p:"Choisissez un couple d'actions et écoutez-le devenir une seule phrase.",
       axes:[{id:'g', lbl:'Quel couple ?', opts:[
         ['a','Prendre le boulevard · éviter le bouchon'],
         ['b','Partir à six heures · éviter l\'heure de pointe'],
         ['c','Écouter la radio · conduire'],
         ['d','Sortir à Marcel-Laurin · gagner dix minutes'],
         ['e','Suivre le détour · arriver à huit heures']]}],
       out:{
         a:{w:['un détour','un bouchon'], say:"En prenant le boulevard, nous évitons le bouchon.", n:"la manière : par quel moyen"},
         b:{w:['un imprévu'], say:"En partant à six heures, vous éviterez l'heure de pointe.", n:"la manière, avec un futur dans l'autre verbe"},
         c:{w:['le covoiturage'], say:"Il écoute la radio en conduisant.", n:"la simultanéité : les deux en même temps"},
         d:{w:['un détour'], say:"En sortant à Marcel-Laurin, il gagne dix minutes.", n:"la manière, avec un lieu"},
         e:{w:['un détour'], say:"En suivant le détour, nous arrivons à huit heures quinze.", n:"la manière, avec une heure d'arrivée"},
       },
       note:"Essayez ensuite de dire votre propre trajet du matin avec deux gérondifs. C'est l'exercice qui rend la tournure automatique."},

      {t:'ex', h:"À écouter et à répéter",
       p:"Six phrases du module.",
       rows:[
         ["En prenant le boulevard, nous évitons le bouchon.","manière"],
         ["En partant à six heures, vous éviterez le bouchon.","manière + futur"],
         ["En sortant à Marcel-Laurin, il gagne dix minutes.","manière + lieu"],
         ["En suivant le détour, nous arrivons à huit heures quinze.","manière + heure"],
         ["Elle a entendu le bulletin en déjeunant.","simultanéité"],
         ["Il écoute la radio en conduisant.","simultanéité"],
       ]},

      {t:'piege', h:"Trois pièges du gérondif",
       rows:[
         ["oublier le « en »","« Passant par le boulevard, on évite le bouchon »",
          "Sans « en », la forme existe encore mais elle change de sens et de registre : c'est du français écrit, littéraire. Pour dire la manière à l'oral, le « en » est obligatoire."],
         ["changer de sujet en cours de route","« En écoutant la radio, l'accident a été annoncé »",
          "Le sujet du gérondif est celui de la phrase : ici, ce serait l'accident qui écoute. Dites plutôt « pendant que nous écoutions la radio, l'accident a été annoncé »."],
         ["former le gérondif sur l'infinitif","« en prendant » au lieu de « en prenant »",
          "La forme part du verbe à <b>nous</b> : nous prenons → en prenant. Nous venons → en venant. Nous faisons → en faisant. Passer par « nous » évite toutes les erreurs."],
       ]},

      {t:'check', h:"Est-ce que c'est clair maintenant ?",
       p:"Quatre questions rapides.",
       qs:[
         {q:"Le gérondif se forme à partir du verbe…", opts:["à l'infinitif","à « nous » au présent"], ok:1,
          fb:"À « nous » au présent : nous prenons → en prenant."},
         {q:"« En sortant à Marcel-Laurin, il gagne dix minutes » exprime…", opts:["la manière","la cause"], ok:0,
          fb:"La manière : par quel moyen il gagne dix minutes."},
         {q:"Le sujet du gérondif est…", opts:["libre","celui de la phrase"], ok:1,
          fb:"Celui de la phrase. Une seule personne fait les deux actions."},
         {q:"Le gérondif de « avoir » est…", opts:["en ayant","en avant"], ok:0,
          fb:"En ayant. C'est une des trois exceptions, avec « en étant » et « en sachant »."},
       ]},
    ]
  },

  // ════════════════════════════════════════════════════════════════════════
  t3fut: {
    eye:'Mini-leçon', tit:"Annoncer une heure d'arrivée",
    blocs:[
      {t:'texte', h:"Une heure, même approximative",
       p:"« Je vais essayer d'arriver le plus vite possible » n'annonce rien. Personne ne peut s'organiser avec cette phrase : ni la responsable qui doit ouvrir l'atelier, ni le collègue qui vous attend, ni le camion de livraison. Une heure, même approximative, permet de décider. C'est pour cela que ce module finit sur les futurs : ils servent à donner un chiffre à quelqu'un qui en a besoin.",
       note:"« Vers huit heures quinze, huit heures vingt au plus tard » est la formule parfaite : une heure probable, et une limite. La personne au bout du fil sait tout ce qu'elle doit savoir."},

      {t:'ana', h:"Le futur proche : tout de suite, et c'est décidé",
       p:"Le verbe « aller » au présent, puis l'infinitif. C'est le futur du téléphone : ce qui arrive dans les minutes qui viennent.",
       mots:[["Annoncer le retard","Je vais être en retard. · On va manquer l'ouverture."],["Annoncer la manœuvre","On va sortir à la prochaine. · Je vais prendre le boulevard.",true],["Avec une durée","Ça va prendre une vingtaine de minutes."]],
       say:"Je vais être en retard d'une quinzaine de minutes.",
       note:"Le futur proche n'est pas « moins bon » que le futur simple : il est simplement plus près. Au téléphone, dans une auto, c'est celui qu'on emploie neuf fois sur dix."},

      {t:'ana', h:"Le futur simple : plus loin, ou plus officiel",
       p:"Les terminaisons se posent sur l'infinitif : -ai, -as, -a, -ons, -ez, -ont. C'est le futur du bulletin et de l'écrit.",
       mots:[["Annoncer une arrivée","J'arriverai vers huit heures quinze."],["Dans le bulletin","La bretelle sera fermée toute la fin de semaine.",true],["Dans un courriel","Nous partirons plus tôt lundi matin. · Les travaux se poursuivront jusqu'à neuf heures."]],
       say:"J'arriverai vers huit heures quinze. La bretelle sera fermée toute la fin de semaine.",
       note:"Dans un courriel, le futur simple est presque obligatoire : le futur proche y fait parlé, et l'écrit du travail reste un cran au-dessus."},

      {t:'ana', h:"Les cinq irréguliers dont vous aurez besoin",
       p:"Ce sont exactement ceux qui servent à annoncer un retard. Les autres verbes suivent la règle.",
       mots:[["Les trois premiers","être → je serai · avoir → j'aurai · aller → j'irai"],["Les deux autres","faire → je ferai · pouvoir → je pourrai",true],["Dans une phrase","Je serai là vers huit heures et quart. · Farida pourra ouvrir."]],
       say:"Je serai là vers huit heures et quart. Farida pourra ouvrir l'atelier.",
       note:"Tous les futurs simples, réguliers comme irréguliers, ont un « r » avant la terminaison : arriverai, serai, aurai, irai, ferai, pourrai. C'est le son qui les reconnaît à l'oreille."},

      {t:'ana', h:"Le présent, quand l'heure est dite",
       p:"Le français parlé emploie le présent pour un futur très proche et très sûr — c'est ce que Tereza fait au téléphone. C'est correct, à une condition.",
       mots:[["Avec l'heure","J'arrive vers huit heures quinze."],["Sans l'heure, c'est ambigu","J'arrive. · On arrive.",true],["Ce qu'on ajoute","huit heures vingt au plus tard"]],
       say:"J'arrive vers huit heures quinze, huit heures vingt au plus tard.",
       note:"« J'arrive » tout court veut dire « je suis presque là » — et si vous êtes à trente minutes, la personne se sentira trompée. Avec l'heure, la phrase est parfaite ; sans elle, elle est fausse."},

      {t:'labo', h:"La même annonce, trois façons",
       p:"Choisissez une annonce et écoutez-la au futur proche, au futur simple et au présent.",
       axes:[{id:'f', lbl:'Quelle annonce ?', opts:[
         ['a','Le retard'],
         ['b','L\'heure d\'arrivée'],
         ['c','La manœuvre'],
         ['d','Ce que fera quelqu\'un d\'autre'],
         ['e','Ce qui est annoncé au bulletin']]}],
       out:{
         a:{w:['un imprévu'], say:"Je vais être en retard. Je serai en retard d'un quart d'heure.", n:"proche à l'oral, simple à l'écrit"},
         b:{w:['un imprévu'], say:"J'arriverai vers huit heures quinze. J'arrive vers huit heures quinze.", n:"le présent passe, parce que l'heure est dite"},
         c:{w:['un détour'], say:"On va sortir à la prochaine. Nous sortirons à la prochaine sortie.", n:"proche dans l'auto, simple dans un courriel"},
         d:{w:['le covoiturage'], say:"Farida va ouvrir l'atelier. Farida pourra ouvrir l'atelier à sept heures et demie.", n:"« pouvoir » au futur simple : pourra"},
         e:{w:['une bretelle'], say:"La bretelle sera fermée toute la fin de semaine. Les travaux se poursuivront lundi matin.", n:"le futur du bulletin est toujours le simple"},
       },
       note:"Écoutez le « r » dans chaque futur simple : arriverai, sortirons, pourra, sera. C'est lui qu'on entend, bien plus que la terminaison."},

      {t:'ex', h:"À écouter et à répéter",
       p:"Six annonces, trois au téléphone et trois par écrit.",
       rows:[
         ["Je vais être en retard d'une quinzaine de minutes.","futur proche, au téléphone"],
         ["On va sortir à la prochaine.","futur proche, dans l'auto"],
         ["J'arrive vers huit heures quinze.","présent, avec l'heure"],
         ["J'arriverai vers huit heures quinze.","futur simple"],
         ["La bretelle sera fermée toute la fin de semaine.","futur simple, au bulletin"],
         ["Nous partirons plus tôt lundi matin.","futur simple, dans un courriel"],
       ]},

      {t:'piege', h:"Trois pièges de l'annonce",
       rows:[
         ["annoncer sans chiffre","« Je vais essayer d'arriver le plus vite possible »",
          "Ce n'est pas une annonce, c'est une intention. Donnez une heure, même large : « entre huit heures et huit heures et demie » vaut mieux que « le plus vite possible »."],
         ["dire « j'arrive » sans l'heure","« J'arrive ! » à trente minutes de distance",
          "« J'arrive » veut dire « je suis presque là ». Sans l'heure, la personne vous attend dans deux minutes, et le retard devient un malentendu en plus d'un retard."],
         ["oublier le « r » du futur simple","« j'arrivai » au lieu de « j'arriverai »",
          "« J'arrivai » est un passé (le passé simple) ; « j'arriverai » est le futur. À l'oral, c'est le « r » qui distingue les deux, et il s'entend nettement : arrive-<b>r</b>-ai."],
       ]},

      {t:'check', h:"Est-ce que c'est clair maintenant ?",
       p:"Quatre questions rapides.",
       qs:[
         {q:"Au téléphone, pour un retard de quinze minutes, on dit plutôt…", opts:["je vais être en retard","je fus en retard"], ok:0,
          fb:"« Je vais être en retard » : le futur proche est celui du téléphone."},
         {q:"Dans un courriel, on écrit plutôt…", opts:["on va partir plus tôt","nous partirons plus tôt"], ok:1,
          fb:"« Nous partirons » : le futur simple convient mieux à l'écrit du travail."},
         {q:"« J'arrive » est correct…", opts:["toujours","si on dit l'heure"], ok:1,
          fb:"Si on dit l'heure. Sans elle, « j'arrive » veut dire « je suis presque là »."},
         {q:"Le futur simple de « pouvoir » à la troisième personne est…", opts:["pourra","pouvera"], ok:0,
          fb:"« Pourra ». C'est un des cinq irréguliers utiles ici."},
       ]},
    ]
  },

  // ════════════════════════════════════════════════════════════════════════
  t3poli: {
    eye:'Mini-leçon', tit:"Annoncer son retard sans se justifier",
    blocs:[
      {t:'texte', h:"Trois informations, et rien d'autre",
       p:"Un appel de retard réussi dure trente secondes et contient trois choses : ce qui se passe, l'heure d'arrivée, ce qu'on fait en attendant. Tout le reste — le nombre de véhicules accidentés, l'heure à laquelle vous êtes partie, la preuve que ce n'est pas de votre faute — allonge l'appel et affaiblit ce que vous dites. Ghislaine le résume à sa façon : un retard annoncé n'est pas un problème ; un retard non annoncé en est un.",
       note:"C'est aussi une question de culture de travail. Au Québec, dans la plupart des milieux, on attend de vous que vous préveniez tôt et que vous proposiez une solution — pas que vous vous excusiez longuement."},

      {t:'ana', h:"On se nomme, toujours",
       p:"La personne qui décroche ne reconnaît pas les voix au téléphone, surtout dans une auto. On se nomme, on dit d'où on appelle, et seulement ensuite on explique.",
       mots:[["La formule complète","Bonjour madame Lachance, c'est Tereza Nogueira."],["Sur une boîte vocale","c'est Tereza Nogueira, de l'atelier d'assemblage",true],["Ce qu'on évite","Salut, c'est moi. · Allo ? C'est pour vous dire que…"]],
       say:"Bonjour madame Lachance, c'est Tereza Nogueira, de l'atelier d'assemblage.",
       note:"Sur un répondeur, cette ligne est la plus importante des cinq : un message sans nom oblige à rappeler pour savoir qui a appelé, ce qui annule tout le bénéfice du message."},

      {t:'ana', h:"On explique, on ne se défend pas",
       p:"Une explication donne un fait. Une défense répond à une accusation que personne n'a portée — et se défendre avant qu'on vous accuse donne l'impression qu'il y a de quoi.",
       mots:[["Une explication","Il y a eu un carambolage sur la quarante, en direction ouest."],["Une défense","Ce n'est vraiment pas de ma faute, je suis partie à l'heure, je vous jure.",true],["La bonne longueur","deux phrases, pas davantage"]],
       say:"Il y a eu un carambolage sur la quarante, en direction ouest. C'est bloqué depuis sept heures.",
       note:"Remarquez que Ghislaine ne demande jamais de preuve. Elle demande ce qui se passe, l'heure, et qui ouvre. Répondre à ces trois questions suffit à clore l'affaire."},

      {t:'ana', h:"On propose la solution avant qu'on la demande",
       p:"C'est la partie que les gens oublient, et c'est celle qui transforme un retard en simple information.",
       mots:[["L'ouverture","Est-ce que Farida peut prendre les clés ? Elle entre à sept heures et demie."],["Une livraison attendue","Le camion arrive à huit heures : il faudrait le faire attendre dans la cour.",true],["Ce qui peut se déplacer","Je reprendrai le temps ce midi, si ça vous convient."]],
       say:"Est-ce que Farida peut prendre les clés ? Elle entre à sept heures et demie.",
       note:"Proposer suppose d'avoir réfléchi avant d'appeler. Trente secondes de préparation dans l'auto valent mieux qu'un appel de trois minutes qui tourne en rond."},

      {t:'ana', h:"On vouvoie, et on ne promet pas de rouler vite",
       p:"Le vouvoiement tient des deux côtés du téléphone, même quand le ton est chaleureux et qu'on s'appelle par son prénom.",
       mots:[["Ce qui se dit","Merci de votre compréhension. · À tout à l'heure."],["Ce qui ne se dit pas","Je vais rouler plus vite pour rattraper le temps.",true],["Ce que la responsable répond","On ne va pas se casser le cou pour quinze minutes."]],
       say:"Merci madame Lachance. À tout à l'heure.",
       note:"Aucune responsable, au Québec, ne vous demandera d'accélérer — et le proposer met tout le monde mal à l'aise. Le retard est déjà pris ; la sécurité, elle, ne se rattrape pas."},

      {t:'labo', h:"La même chose, bien dite et mal dite",
       p:"Choisissez un moment de l'appel et écoutez les deux versions.",
       axes:[{id:'p', lbl:'Quel moment ?', opts:[
         ['a','Se nommer'],
         ['b','Expliquer'],
         ['c','Donner l\'heure'],
         ['d','Proposer une solution'],
         ['e','Terminer']]}],
       out:{
         a:{w:['prévenir'], say:"Bonjour madame Lachance, c'est Tereza Nogueira.", n:"la version courte : Salut, c'est moi"},
         b:{w:['un carambolage'], say:"Il y a eu un carambolage sur la quarante, en direction ouest.", n:"la version défensive : ce n'est pas de ma faute, je vous jure"},
         c:{w:['un imprévu'], say:"J'arriverai vers huit heures quinze, huit heures vingt au plus tard.", n:"la version vague : dès que je peux"},
         d:{w:['le covoiturage'], say:"Est-ce que Farida peut prendre les clés en attendant ?", n:"la version passive : je ne sais pas quoi faire pour l'ouverture"},
         e:{w:['prévenir'], say:"Merci madame Lachance. À tout à l'heure.", n:"la version qui inquiète : je vais me dépêcher"},
       },
       note:"Écoutez les cinq bonnes versions à la suite : vous avez l'appel complet, et il dure une trentaine de secondes."},

      {t:'ex', h:"À écouter et à répéter",
       p:"Six phrases de l'appel à l'atelier.",
       rows:[
         ["Bonjour madame Lachance, c'est Tereza Nogueira.","se nommer, dès la première phrase"],
         ["Je vous appelle de l'auto : je vais être en retard.","dire pourquoi on appelle"],
         ["Il y a eu un carambolage sur la quarante.","expliquer, sans se défendre"],
         ["C'est bloqué depuis sept heures.","depuis quand"],
         ["J'arriverai vers huit heures quinze.","une heure, en chiffres"],
         ["Est-ce que Farida peut prendre les clés ?","proposer la solution"],
       ]},

      {t:'piege', h:"Trois pièges de l'appel de retard",
       rows:[
         ["attendre d'être certain de l'heure pour appeler","appeler à huit heures pour dire qu'on est en retard depuis sept heures et demie",
          "Le bon moment est celui où vous comprenez que vous serez en retard, pas celui où vous savez de combien. Vous pouvez très bien dire « je ne sais pas encore, je vous rappelle dans vingt minutes »."],
         ["raconter tout le bulletin","le nombre de véhicules, la sortie exacte, ce qu'a dit l'animateur",
          "La responsable n'a pas besoin de la scène : elle a besoin de savoir que c'est sérieux, quand vous arrivez et ce qu'on fait en attendant. Deux phrases pour l'explication, pas cinq."],
         ["laisser la solution à l'autre","« Je ne sais pas comment vous allez faire pour ouvrir »",
          "Vous connaissez l'atelier mieux que personne à cette heure-là. Proposez : Farida a les clés, le camion peut attendre dans la cour. C'est cela qu'on appelle un discours organisé."],
       ]},

      {t:'check', h:"Est-ce que c'est clair maintenant ?",
       p:"Quatre questions rapides.",
       qs:[
         {q:"La première phrase d'un appel de retard sert à…", opts:["expliquer ce qui bloque","se nommer"], ok:1,
          fb:"À se nommer. Sans cela, tout le reste est inutilisable."},
         {q:"« Ce n'est vraiment pas de ma faute, je vous jure » est…", opts:["une explication","une défense"], ok:1,
          fb:"Une défense — et personne ne vous a accusé."},
         {q:"On appelle…", opts:["dès qu'on sait qu'on sera en retard","quand on connaît l'heure exacte"], ok:0,
          fb:"Dès qu'on le sait. Une heure approximative suffit."},
         {q:"Promettre de rouler plus vite…", opts:["rassure la responsable","met tout le monde mal à l'aise"], ok:1,
          fb:"Ça met tout le monde mal à l'aise. Le retard se rattrape ; la sécurité, non."},
       ]},
    ]
  },

};
