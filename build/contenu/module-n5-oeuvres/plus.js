const PLUS = {

  // ════════════════════════════════════════════════════════════════════════
  prPhon: {
    eye:'Mini-leçon', tit:"Le son de « j » et le son de « ch »",
    blocs:[
      {t:'texte', h:"Deux sons faits au même endroit, et un seul détail entre eux",
       p:"Ouvrez n'importe quelle présentation du club et comptez : j'ai lu, une image, un personnage, un passage, l'intrigue, déjà, jamais d'un côté ; un chapitre, une chanson, une planche, chercher, toucher, touchant de l'autre. La bouche fait exactement la même chose pour les deux : les lèvres avancent un peu, la langue monte vers l'avant du palais, et l'air passe par une fente étroite. Une seule chose change, et elle ne se voit pas : la gorge vibre, ou elle ne vibre pas.",
       note:"C'est pour ça que ces deux sons sont difficiles à séparer à l'oreille quand on apprend : rien ne se voit sur le visage de la personne qui parle. Il faut passer par la main sur la gorge, une fois, et l'affaire est réglée pour de bon."},

      {t:'ana', h:"Le son de « j » : la gorge vibre",
       p:"Posez deux doigts sur votre gorge, à la hauteur de la pomme d'Adam, et dites « jjjjj » en tenant le son. Ça bourdonne sous vos doigts. On l'écrit j, ou g devant e et i, ou ge devant a et o.",
       mots:[["Écrit avec j","j'ai lu · déjà · toujours · jamais"],["Écrit avec g","une image · l'intrigue · un personnage · un passage",true],["Dans les mots du club","un personnage · un passage · une page"]],
       say:"J'ai lu. Une image. Un personnage.",
       note:"« Personnage » contient les deux difficultés du mot : le « son » du milieu et le « ge » de la fin. Dites-le en quatre temps — per-son-na-ge — puis vite."},

      {t:'ana', h:"Le son de « ch » : rien ne vibre",
       p:"Les mêmes doigts sur la gorge, dites « chhhh ». Rien ne bouge : seul l'air passe. C'est le son qu'on fait pour demander le silence. On l'écrit toujours ch, sans exception utile.",
       mots:[["Les mots du livre","un chapitre · une planche · une couche"],["Les verbes","chercher · toucher · marcher · afficher",true],["Les mots de tous les jours","une chanson · chaque · chez · une chaise"]],
       say:"Un chapitre. Une planche. Une chanson.",
       note:"« Une planche » est le mot le plus utile du Défi 2, et c'est aussi celui où l'erreur s'entend le plus : « une plange » ne veut rien dire, et l'autre personne s'arrête pour comprendre."},

      {t:'ana', h:"Le seul exercice qui sert : couper la voix",
       p:"Ne changez rien à vos lèvres ni à votre langue. Gardez la position, et coupez seulement la voix. « j » sans voix devient « ch » ; « ch » avec la voix devient « j ». Faites l'aller-retour dix fois, la main sur la gorge.",
       mots:[["Les paires de base","les gens / les champs · j'ai / chez"],["Les paires du module","bouger / boucher · la cage / la cache",true],["La phrase à deux sons","ce personnage-là m'a touchée"]],
       say:"Les gens, les champs. J'ai, chez. Bouger, boucher.",
       note:"Si vous n'entendez pas encore la différence, ne l'écoutez pas : sentez-la. La main sur la gorge est plus fiable que l'oreille pendant les premières semaines."},

      {t:'labo', h:"Écoutez la paire, puis le mot dans sa phrase",
       p:"Choisissez une paire et écoutez la différence, puis le mot replacé dans une phrase du club.",
       axes:[{id:'p', lbl:'Quelle paire ?', opts:[
         ['a','les gens / les champs'],
         ['b',"j'ai / chez"],
         ['c','bouger / boucher'],
         ['d','un personnage / une planche'],
         ['e','les quatre à la suite']]}],
       out:{
         a:{w:['un personnage'], say:"Les gens. Les champs. Les gens du club parlent des champs de ce roman.", n:"la gorge vibre, puis elle ne vibre plus"},
         b:{w:['une planche'], say:"J'ai. Chez. J'ai lu cet album chez ma sœur.", n:"deux mots très courts, deux sons voisins"},
         c:{w:['une case'], say:"Bouger. Boucher. Rien ne bouge dans cette case.", n:"la même consonne au milieu, deux fois"},
         d:{w:['un personnage','une planche'], say:"Un personnage. Une planche. Ce personnage traverse toute la planche.", n:"la paire qui revient dans tout le module"},
         e:{w:['un personnage','une planche'], say:"Les gens, les champs. J'ai, chez. Bouger, boucher. Personnage, planche.", n:"quatre paires à la suite, sans reprendre son souffle"},
       },
       note:"Écoutez chaque paire deux fois : la première pour entendre les deux mots, la seconde en gardant la main sur votre propre gorge pendant que vous répétez."},

      {t:'ex', h:"À écouter et à répéter",
       p:"Six phrases prises dans les dialogues du module.",
       rows:[
         ["J'ai lu ce roman en deux soirées.","« j » au tout début, la gorge vibre"],
         ["Chaque chapitre commence par une chanson.","trois fois « ch », rien ne vibre"],
         ["Ce personnage-là m'a touchée.","« j » puis « ch » dans la même phrase"],
         ["La planche du milieu ne contient aucune image.","« ch » d'abord, « j » à la fin"],
         ["Je cherche l'album que j'ai déjà lu.","les deux sons alternent quatre fois"],
         ["Quelle belle façon de le dire !","le « ç » n'est pas un « ch » : c'est le son de « s »"],
       ]},

      {t:'piege', h:"Trois pièges de « j » et « ch »",
       rows:[
         ["dire « ch » à la place de « j » en fin de mot","« un personnache » au lieu de « un personnage »",
          "En fin de mot, la voix a tendance à s'éteindre avant le son. Tenez la voix jusqu'au bout : la dernière syllabe de « personnage » bourdonne encore quand elle s'arrête. Exercez-vous sur image, page, passage, village."],
         ["prononcer le g de « intrigue » comme un « j »","« l'intrijue » au lieu de « l'intrigue »",
          "Le g ne se dit « j » que devant e et i. Devant u, a, o, il reste un g dur : intrigue, guide, longue. Le u de « intrigue » est là justement pour garder le g dur — il ne se prononce pas."],
         ["croire que « ch » se dit toujours pareil","« un chœur » lu comme « une chaise »",
          "Quelques mots venus du grec écrivent ch et disent « k » : un chœur, une chorale, la technologie. Ils sont rares, mais « chœur » revient souvent quand on parle de musique. Retenez-le comme une exception, pas comme une règle."],
       ]},

      {t:'check', h:"Est-ce que c'est clair maintenant ?",
       p:"Quatre questions rapides.",
       qs:[
         {q:"Dans « une planche », la gorge…", opts:["vibre","ne vibre pas"], ok:1,
          fb:"Elle ne vibre pas. « ch » est le son sans voix des deux."},
         {q:"« Un passage » contient le son…", opts:["de « j »","de « ch »"], ok:0,
          fb:"Celui de « j ». Le g devant e se dit comme un j."},
         {q:"Pour passer de « j » à « ch », il faut…", opts:["bouger la langue","couper la voix"], ok:1,
          fb:"Couper la voix. La langue et les lèvres ne bougent pas."},
         {q:"Dans « l'intrigue », le g se dit…", opts:["comme un j","comme un g dur"], ok:1,
          fb:"Comme un g dur : le u qui suit sert justement à ça."},
       ]},
    ]
  },

  // ════════════════════════════════════════════════════════════════════════
  prMot: {
    eye:'Mini-leçon', tit:"Une œuvre, un roman, une série, un album",
    blocs:[
      {t:'texte', h:"Un mot large, et quatre mots précis",
       p:"Quand quelqu'un vous demande de quoi vous voulez parler, il attend deux informations dans la même phrase : le support et le genre. Le support, c'est la forme — un livre, un film, une série, une bande dessinée, une chanson. Le genre, c'est le type d'histoire — une histoire de famille, un polar, une histoire vraie. Une seule phrase suffit pour les deux, et cette phrase-là est la première de toute présentation.",
       note:"Ne dites jamais « j'ai lu quelque chose de bien » pour commencer. C'est la seule phrase du club qui fait perdre du temps à tout le monde, y compris à celui qui la dit."},

      {t:'ana', h:"« Une œuvre » — le mot qui couvre tout",
       p:"Une œuvre, c'est ce que quelqu'un a créé pour être lu, vu ou écouté. Le mot ne dit ni la forme ni la longueur : il sert quand on parle en général, et quand on veut éviter de répéter le mot précis pour la troisième fois.",
       mots:[["Ce que le mot couvre","un livre · un film · une chanson · une bande dessinée"],["Où on l'entend","apportez une œuvre que vous avez aimée",true],["Comme mot de reprise","cette œuvre m'a suivie pendant une semaine"]],
       say:"Une œuvre. Apportez une œuvre que vous avez aimée.",
       note:"« Œuvre » est féminin : une œuvre, cette œuvre, la même œuvre. La ligature œ se prononce comme le « eu » de « peur »."},

      {t:'ana', h:"Ce qui se lit : le roman et l'album",
       p:"Un roman raconte une histoire inventée en un seul livre. Un album de bande dessinée est grand, cartonné, une cinquantaine de planches, et il porte souvent un numéro de tome. Un recueil rassemble des textes courts : des nouvelles, des poèmes.",
       mots:[["Le roman","trois cents pages · une histoire de famille · un polar"],["L'album","le premier tome · une série de quatre · cinquante planches",true],["Ce qu'on dit au comptoir","je cherche le tome deux de cette série"]],
       say:"Un roman de trois cents pages. Le premier tome d'une série.",
       note:"Au Québec, on dit couramment « une BD » à l'oral. Au club et au comptoir, « un album » et « une bande dessinée » sont les mots qu'emploient les bibliothécaires."},

      {t:'ana', h:"Ce qui se regarde et ce qui s'écoute",
       p:"Un film tient en une fois ; une série est coupée en épisodes qu'on regarde l'un après l'autre, souvent groupés en saisons. Une chanson, un album de musique et une pièce de théâtre sont aussi des œuvres, et ils sont bienvenus au club.",
       mots:[["La série","huit épisodes · quarante minutes · deux saisons"],["Le film","deux heures · en salle · en version originale",true],["La musique","une chanson · un album · les paroles"]],
       say:"Une série de huit épisodes. Un film de deux heures.",
       note:"Quand vous présentez une série, donnez tout de suite le nombre d'épisodes et leur durée. C'est la première question que les gens posent, et vous la faites disparaître."},

      {t:'labo', h:"Choisissez un support, écoutez la phrase de présentation",
       p:"Chaque support a sa première phrase. Écoutez-la, puis remplacez le contenu par le vôtre.",
       axes:[{id:'s', lbl:'Vous présentez quoi ?', opts:[
         ['a','un roman'],
         ['b','une bande dessinée'],
         ['c','une série'],
         ['d','un film'],
         ['e','une chanson']]}],
       out:{
         a:{w:['un roman','une œuvre'], say:"C'est un roman de trois cents pages, une histoire de famille qui se passe au bord de la mer.", n:"support, longueur, genre, lieu — en une phrase"},
         b:{w:['un album','une planche'], say:"C'est une bande dessinée, le premier tome d'une série de quatre albums.", n:"le support, puis la place dans la série"},
         c:{w:['une série'], say:"C'est une série de huit épisodes de quarante minutes, une seule saison.", n:"le nombre d'épisodes tout de suite"},
         d:{w:['une œuvre'], say:"C'est un film de deux heures, une histoire vraie, et il joue encore au cinéma du quartier.", n:"la durée, le genre, et où le voir"},
         e:{w:['un coup de cœur'], say:"C'est une chanson de quatre minutes, et c'est mon coup de cœur du mois.", n:"la plus courte des présentations possibles"},
       },
       note:"Ces cinq phrases sont des moules. Gardez la structure, changez les chiffres et le genre : votre première phrase est écrite pour toute l'année."},

      {t:'ex', h:"À écouter et à répéter",
       p:"Six premières phrases de présentation.",
       rows:[
         ["Chaque membre du club présente une œuvre qu'il a aimée.","le mot le plus large, au singulier"],
         ["C'est un roman de trois cents pages, une histoire de famille.","support, longueur, genre"],
         ["L'album que vous tenez est le premier tome de la série.","album, tome, série dans la même phrase"],
         ["La série compte huit épisodes de quarante minutes.","les deux chiffres qu'on demande toujours"],
         ["Elle lit un extrait de deux pages pour donner le ton.","comment finir une présentation"],
         ["Le comptoir affiche les coups de cœur du mois.","le mot de la bibliothèque"],
       ]},

      {t:'piege', h:"Trois confusions fréquentes",
       rows:[
         ["confondre la série et l'album","« j'ai lu la série » quand on a lu un seul tome",
          "La série est l'ensemble ; l'album ou le tome est le livre que vous avez entre les mains. Dites « j'ai lu le premier tome » tant que vous n'avez pas tout lu : au comptoir, la différence décide de ce qu'on vous donne."],
         ["dire « une histoire » pour « un livre »","« j'ai acheté une histoire »",
          "L'histoire est ce qu'il y a dedans ; le livre est l'objet. On achète un livre, on raconte une histoire. Les deux mots servent de reprise l'un pour l'autre dans une présentation, mais pas quand on parle d'acheter ou d'emprunter."],
         ["employer « œuvre » dès la première phrase","« je vais vous parler d'une œuvre »",
          "Trop large pour commencer : personne ne sait encore s'il s'agit d'un livre ou d'un film. Gardez « œuvre » pour les deuxième et troisième mentions, quand il évite une répétition."],
       ]},

      {t:'check', h:"Est-ce que c'est clair maintenant ?",
       p:"Quatre questions rapides.",
       qs:[
         {q:"Le premier tome d'une suite de quatre livres de bande dessinée, c'est…", opts:["une série","un album"], ok:1,
          fb:"Un album. La série est l'ensemble des quatre."},
         {q:"« Une œuvre » sert surtout…", opts:["à commencer une présentation","à éviter une répétition"], ok:1,
          fb:"À éviter une répétition. Trop large pour commencer."},
         {q:"Quand on présente une série, on donne d'abord…", opts:["le nombre d'épisodes et la durée","le nom des personnages"], ok:0,
          fb:"Le nombre d'épisodes et leur durée : c'est ce qu'on demande toujours."},
         {q:"Un extrait, c'est…", opts:["le résumé de l'œuvre","un petit morceau de l'œuvre"], ok:1,
          fb:"Un petit morceau : deux pages, deux minutes, quelques lignes."},
       ]},
    ]
  },

  // ════════════════════════════════════════════════════════════════════════
  t1pres: {
    eye:'Mini-leçon', tit:"Le présent qui raconte une histoire",
    blocs:[
      {t:'texte', h:"Pourquoi on raconte au présent une histoire déjà écrite",
       p:"Regardez le dos de n'importe quel livre, dans n'importe quelle bibliothèque du Québec : le résumé est au présent. « Une femme revient au village. Elle veut vendre la maison de sa mère. Elle trouve une boîte de lettres. » Le livre est écrit au passé, l'autrice l'a fini il y a trois ans, et pourtant tout le monde le raconte au présent. Ce n'est pas une règle de grammaire : c'est un choix qui met la personne qui écoute à l'intérieur de la scène, au moment où ça arrive.",
       note:"Au passé composé, la même chose devient un rapport : « une femme est revenue au village, elle a voulu vendre la maison ». C'est correct, mais on dirait un procès-verbal. Essayez les deux à voix haute, vous entendrez la différence tout de suite."},

      {t:'ana', h:"L'action qui se déroule maintenant, dans l'histoire",
       p:"Chaque verbe est un moment, et les moments se suivent dans l'ordre où vous les racontez. Pas de « et après », pas de « ensuite » à toutes les phrases : le présent suffit à faire avancer.",
       mots:[["Le début de l'histoire","elle arrive · elle ouvre la maison · elle trouve une boîte"],["Ce qui bouge","la porte s'ouvre · personne ne répond · il hésite",true],["Ce que le personnage veut","elle veut repartir · il cherche sa sœur · elle refuse"]],
       say:"Elle arrive au village. Elle ouvre la maison. Elle trouve une boîte.",
       note:"Trois verbes au présent, trois moments : c'est exactement la longueur d'une bonne mise en marche d'histoire. Au quatrième, on est déjà en train d'en dire trop."},

      {t:'ana', h:"L'action habituelle, au même temps",
       p:"Le présent dit aussi ce qui se répète dans l'histoire. Le verbe ne change pas ; ce qui change, c'est le petit mot devant. Sans ce mot, la personne qui écoute croira que ça n'arrive qu'une fois.",
       mots:[["Les mots qui disent l'habitude","tous les soirs · chaque matin · d'habitude"],["Dans le roman","tous les soirs, elle marche jusqu'au quai",true],["Ce qui change le sens","elle marche jusqu'au quai / tous les soirs, elle marche jusqu'au quai"]],
       say:"Tous les soirs, elle marche jusqu'au quai.",
       note:"C'est un savoir du programme de niveau 5 : distinguer l'action en cours de l'action habituelle. Le français les met au même temps, et laisse le repère de temps faire tout le travail."},

      {t:'ana', h:"Deux choses en même temps",
       p:"Quand deux actions se passent au même moment de l'histoire, les deux verbes restent au présent. Rien n'est décalé, rien ne recule.",
       mots:[["Avec pendant que","pendant qu'elle range la maison, elle relit les lettres"],["Avec quand","quand elle ouvre la boîte, elle reconnaît l'écriture",true],["Avec le gérondif","elle relit les lettres en rangeant la maison"]],
       say:"Pendant qu'elle range la maison, elle relit les lettres.",
       note:"Le gérondif — « en rangeant » — dit la même chose en moins de mots, et il fait très bon effet dans une présentation de deux minutes. Un seul par présentation suffit."},

      {t:'labo', h:"La même histoire, racontée de quatre façons",
       p:"Écoutez le même passage au présent, au passé, à l'habitude et en simultané. Choisissez, comparez.",
       axes:[{id:'f', lbl:'Comment on le raconte ?', opts:[
         ['a','au présent, comme au club'],
         ['b','au passé composé, pour comparer'],
         ['c',"une habitude du personnage"],
         ['d','deux actions en même temps'],
         ['e','les quatre à la suite']]}],
       out:{
         a:{w:["l'intrigue"], say:"Elle arrive au village. Elle ouvre la maison de sa mère. Elle trouve une boîte de lettres dans le grenier.", n:"le présent : on est dans la scène"},
         b:{w:['un personnage'], say:"Elle est arrivée au village. Elle a ouvert la maison de sa mère. Elle a trouvé une boîte de lettres.", n:"le passé composé : on est devant un rapport"},
         c:{w:['un personnage'], say:"Tous les soirs, elle marche jusqu'au quai. Elle regarde la mer et elle rentre.", n:"l'habitude : le repère de temps fait tout"},
         d:{w:["l'intrigue"], say:"Pendant qu'elle range la maison, elle relit les lettres une par une.", n:"deux actions, un seul moment"},
         e:{w:["l'intrigue",'un personnage'], say:"Elle arrive au village. Elle est arrivée au village. Tous les soirs, elle marche jusqu'au quai. Pendant qu'elle range, elle relit les lettres.", n:"les quatre à la suite, pour entendre l'écart"},
       },
       note:"La deuxième option est là exprès : elle n'est pas fautive, elle est seulement moins vivante. Entendre les deux vous fera choisir le présent sans y penser."},

      {t:'ex', h:"À écouter et à répéter",
       p:"Six phrases de résumé, toutes au présent.",
       rows:[
         ["Une femme revient au village après vingt ans.","le verbe qui met l'histoire en marche"],
         ["Elle veut repartir le jour même.","ce que le personnage veut : toujours utile"],
         ["Elle ouvre la maison et elle découvre une boîte de lettres.","deux moments dans la même phrase"],
         ["Tous les soirs, elle marche jusqu'au quai.","l'habitude, marquée par le repère de temps"],
         ["Pendant qu'elle range la maison, elle relit les lettres.","deux actions au même moment"],
         ["Le personnage principal ne parle presque jamais.","une description, au présent elle aussi"],
       ]},

      {t:'piege', h:"Trois pièges du présent de récit",
       rows:[
         ["changer de temps au milieu du résumé","« elle arrive au village et elle a trouvé une boîte »",
          "Une fois que vous êtes au présent, restez-y jusqu'à la fin. Le mélange est la faute la plus fréquente, et c'est celle qui s'entend le plus : l'auditeur ne sait plus s'il est dans l'histoire ou dans votre souvenir de l'histoire."],
         ["oublier le repère de l'habitude","« elle marche jusqu'au quai » pour dire qu'elle le fait chaque soir",
          "Sans « tous les soirs », la phrase décrit une seule promenade. Le français ne change pas le verbe : c'est vous qui devez ajouter le repère, sinon l'information se perd sans que personne s'en aperçoive."],
         ["reculer le deuxième verbe","« pendant qu'elle rangeait, elle relit les lettres »",
          "Quand les deux actions sont au même moment de l'histoire, les deux verbes restent au présent. Le décalage n'existe que si vous racontez quelque chose qui s'est passé avant le moment raconté."],
       ]},

      {t:'check', h:"Est-ce que c'est clair maintenant ?",
       p:"Quatre questions rapides.",
       qs:[
         {q:"On raconte une histoire au présent parce que…", opts:["c'est plus facile à conjuguer","ça place l'autre dans la scène"], ok:1,
          fb:"Ça place l'autre dans la scène, au moment où ça arrive."},
         {q:"Pour dire une habitude du personnage, on change…", opts:["le temps du verbe","le repère de temps devant"], ok:1,
          fb:"Le repère de temps : tous les soirs, chaque matin, d'habitude."},
         {q:"« Pendant qu'elle range, elle ___ les lettres. »", opts:["relit","relisait"], ok:0,
          fb:"Relit : deux actions au même moment, deux présents."},
         {q:"Au milieu d'un résumé au présent, on peut…", opts:["passer au passé composé","rester au présent jusqu'au bout"], ok:1,
          fb:"Rester au présent. Le mélange est ce qui s'entend le plus."},
       ]},
    ]
  },

  // ════════════════════════════════════════════════════════════════════════
  t1rel: {
    eye:'Mini-leçon', tit:"Qui, que, où — recoller les phrases",
    blocs:[
      {t:'texte', h:"Le problème que ces trois mots règlent",
       p:"Sans eux, vous dites : « C'est une femme. Elle revient au village. Elle a quitté ce village il y a vingt ans. » Trois phrases courtes, correctes, et l'auditeur perd le fil parce que rien ne les relie. Avec eux : « C'est une femme qui revient dans le village qu'elle a quitté il y a vingt ans. » Une seule phrase, la même information, et l'on entend un discours au lieu d'une liste. C'est exactement ce que le niveau 5 appelle un discours organisé.",
       note:"Ne cherchez pas à en mettre partout. Deux relatives dans une présentation de deux minutes suffisent à changer l'impression générale ; six la rendent illisible."},

      {t:'ana', h:"qui — celui qui fait l'action",
       p:"Après qui, il n'y a pas de sujet, parce que qui est le sujet. Le verbe suit tout de suite. Et qui ne perd jamais son i, même devant une voyelle.",
       mots:[["Sur un personnage","une femme qui revient · un personnage qui ne parle jamais"],["Sur une œuvre","une histoire qui se passe en hiver · un album qui fait rire",true],["Devant une voyelle","quelqu'un qui a quitté un pays"]],
       say:"Une femme qui revient au village. Un personnage qui ne parle presque jamais.",
       note:"« Qu'il » et « qui il » n'existent pas comme relatives : si vous hésitez, remplacez mentalement par « elle » — si la phrase marche, c'était un sujet, donc « qui »."},

      {t:'ana', h:"que — celui qui subit l'action",
       p:"Après que, il y a toujours un sujet : quelqu'un fait quelque chose à la personne ou à la chose dont on parle. Devant une voyelle, que devient qu'.",
       mots:[["Sur un livre","le roman que j'ai lu · l'album que vous tenez"],["Sur un personnage","le personnage qu'elle rencontre au quai",true],["Sur une chose","la boîte qu'elle trouve dans le grenier"]],
       say:"Le roman que j'ai lu la semaine passée. La boîte qu'elle trouve dans le grenier.",
       note:"C'est la forme qui sert le plus au club : « l'album que j'ai emprunté », « la série que Nadia recommande », « le film que je vous conseille »."},

      {t:'ana', h:"où — le lieu, et aussi le moment",
       p:"Où sert au lieu, comme tout le monde le sait, mais il sert aussi au temps — et c'est là que presque tout le monde se trompe.",
       mots:[["Le lieu","le village où elle est née · la page où tout bascule"],["Le moment","le jour où elle ouvre la boîte · l'année où il part",true],["Ce qu'on entend souvent, à corriger","le jour que · la fois que"]],
       say:"Le village où elle est née. Le jour où elle ouvre la boîte.",
       note:"« Le jour que » s'entend beaucoup à l'oral, au Québec comme ailleurs. Ce n'est pas ce qui s'écrit : dans une production écrite corrigée, c'est « le jour où »."},

      {t:'labo', h:"Le test, appliqué à quatre phrases",
       p:"Regardez ce qui vient juste après le trou. Choisissez une phrase et écoutez la règle appliquée.",
       axes:[{id:'r', lbl:'Quelle phrase ?', opts:[
         ['a',"une femme ___ revient au village"],
         ['b',"le roman ___ j'ai lu"],
         ['c',"le village ___ elle est née"],
         ['d',"le jour ___ elle ouvre la boîte"],
         ['e','les quatre à la suite']]}],
       out:{
         a:{w:['un personnage'], say:"C'est une femme qui revient au village. Après le trou, un verbe tout seul : qui.", n:"un verbe suit → qui"},
         b:{w:['un roman'], say:"Le roman que j'ai lu la semaine passée. Après le trou, un sujet : que.", n:"un sujet suit → que"},
         c:{w:["l'intrigue"], say:"Le village où elle est née. Devant le trou, un lieu : où.", n:"un lieu devant → où"},
         d:{w:['le dénouement'], say:"Le jour où elle ouvre la boîte. Devant le trou, un moment : où aussi.", n:"un moment devant → où"},
         e:{w:['un roman','un personnage'], say:"Une femme qui revient. Le roman que j'ai lu. Le village où elle est née. Le jour où elle ouvre la boîte.", n:"les quatre cas, dans l'ordre du test"},
       },
       note:"Trois secondes de test valent mieux qu'une règle apprise par cœur : ce qui suit le trou décide, et rien d'autre."},

      {t:'ex', h:"À écouter et à répéter",
       p:"Six phrases du module, toutes avec une relative.",
       rows:[
         ["C'est une femme qui revient au village après vingt ans.","qui + verbe, sans sujet"],
         ["Le roman que j'ai lu la semaine passée fait trois cents pages.","que + sujet"],
         ["Le village où elle est née se trouve au bord de la mer.","où de lieu"],
         ["Le jour où elle ouvre la boîte, tout change pour elle.","où de temps"],
         ["Je le recommande à quelqu'un qui a quitté un pays.","qui devant une voyelle, sans élision"],
         ["L'album que vous tenez est le premier tome de la série.","que + vous, sur un objet montré"],
       ]},

      {t:'piege', h:"Trois pièges des relatives",
       rows:[
         ["élider qui devant une voyelle","« qu'a quitté un pays » pour « qui a quitté un pays »",
          "Que s'élide, qui ne s'élide jamais. « Quelqu'un qui a quitté un pays » garde le i, toujours, dans tous les cas. C'est la faute d'écriture la plus fréquente du niveau 5."],
         ["employer que pour un moment","« le jour que je l'ai fini »",
          "Après un nom qui dit le temps — le jour, l'année, la fois, le moment — c'est où qu'il faut. « Le jour où je l'ai fini. » L'oreille dit le contraire ; l'écrit demande où."],
         ["oublier le sujet après que","« le roman que ai lu »",
          "Après que, il faut un sujet : que j'ai lu, que vous tenez, qu'elle trouve. S'il n'y a pas de sujet à mettre, c'est que la bonne réponse était qui."],
       ]},

      {t:'check', h:"Est-ce que c'est clair maintenant ?",
       p:"Quatre questions rapides.",
       qs:[
         {q:"« Un personnage ___ ne parle jamais. »", opts:["qui","que"], ok:0,
          fb:"Qui : le verbe suit tout de suite, sans sujet."},
         {q:"« La boîte ___ elle trouve dans le grenier. »", opts:["qui","qu'"], ok:1,
          fb:"Qu' : un sujet suit — elle —, et que s'élide devant la voyelle."},
         {q:"« Le jour ___ elle ouvre la boîte. »", opts:["que","où"], ok:1,
          fb:"Où : après un nom de temps, c'est où et non que."},
         {q:"Devant une voyelle, « qui »…", opts:["devient qu'","ne change jamais"], ok:1,
          fb:"Ne change jamais. Seul « que » s'élide."},
       ]},
    ]
  },

  // ════════════════════════════════════════════════════════════════════════
  t1tri: {
    eye:'Mini-leçon', tit:"Où s'arrête ce qu'on raconte",
    blocs:[
      {t:'texte', h:"Une règle sociale, pas une règle de grammaire",
       p:"Personne ne vous mettra à l'amende si vous racontez la fin. Mais vous enlèverez à l'autre la seule chose qu'il ne pourra jamais récupérer : la découverte. C'est pour ça que le club en a fait sa règle numéro un, et c'est pour ça que Gilberte arrête quelqu'un au milieu d'une phrase — la seule chose qu'elle interrompt en onze ans d'animation. Savoir où s'arrêter est une compétence de conversation, et elle s'apprend comme le reste.",
       note:"Cette règle vaut bien au-delà du club : au travail, à la garderie, dans l'autobus. Quelqu'un qui sait donner envie sans tout dire est quelqu'un avec qui on aime parler de films."},

      {t:'ana', h:"Ce qui se raconte : la mise en marche",
       p:"Tout ce qui met l'histoire en route se dit, et se dit largement. Le lieu, l'époque, qui est le personnage, ce qu'il veut, et ce qui l'empêche de l'avoir.",
       mots:[["Le cadre","ça se passe dans un village · aujourd'hui · en hiver"],["Le personnage et son désir","elle veut vendre la maison · elle veut repartir",true],["L'obstacle","elle trouve une boîte de lettres · la maison n'est pas vide"]],
       say:"Elle revient pour vendre la maison, mais elle trouve une boîte de lettres.",
       note:"Une envie naît toujours d'un obstacle, jamais d'une solution. Si votre résumé ne contient aucun « mais », il ne donnera envie à personne."},

      {t:'ana', h:"Ce qui ne se raconte pas",
       p:"Le dénouement, évidemment. Mais aussi tout ce qui le laisse deviner : qui meurt, qui se marie, qui est le coupable, si les deux se retrouvent, ce que contenaient les lettres.",
       mots:[["Les fins nommées","elle brûle les lettres · il ne revient jamais"],["Les révélations du milieu","on apprend que sa sœur est morte",true],["Les phrases qui trahissent","vous allez pleurer à la fin · attendez la dernière page"]],
       say:"Je m'arrête ici. Je ne vous dis pas ce qu'elle choisit.",
       note:"La troisième famille est la plus sournoise : « vous allez pleurer à la fin » ne raconte rien et annonce tout. Un auditeur averti sait déjà comment ça se termine."},

      {t:'ana', h:"Les trois phrases qui suffisent pour toute une vie",
       p:"Il n'y a pas besoin d'un vocabulaire compliqué pour poser la limite. Trois phrases courtes font le travail, et elles se disent avec le sourire.",
       mots:[["Pour annoncer la limite","je ne vous dis pas la fin"],["Pour s'arrêter net","je m'arrête ici",true],["Pour renvoyer à l'œuvre","lisez-le, vous verrez · allez le voir"]],
       say:"Je ne vous dis pas la fin. Je m'arrête ici. Lisez-le, vous verrez.",
       note:"Au club, « Lisez-le » est considéré comme la plus belle réponse possible à la question « comment ça finit ? ». Elle est polie, elle est ferme, et elle donne encore plus envie."},

      {t:'labo', h:"La même phrase, permise ou interdite",
       p:"Choisissez un cas et écoutez la version qu'on peut dire, puis celle qui en dit trop.",
       axes:[{id:'c', lbl:'Quel cas ?', opts:[
         ['a',"le personnage principal"],
         ['b','ce qui arrive au début'],
         ['c','ce qui arrive à la fin'],
         ['d','la phrase qui trahit sans raconter'],
         ['e','comment refuser de dire la fin']]}],
       out:{
         a:{w:['un personnage'], say:"On peut le dire : le personnage principal ne parle presque jamais. On ne peut pas : le personnage principal meurt à la fin.", n:"décrire, oui ; annoncer son sort, non"},
         b:{w:["l'intrigue"], say:"On peut le dire : elle ouvre la maison et elle trouve une boîte de lettres.", n:"la mise en marche se raconte au complet"},
         c:{w:['le dénouement'], say:"On ne peut pas le dire : à la dernière page, elle brûle toutes les lettres.", n:"le dénouement, jamais"},
         d:{w:['le dénouement'], say:"On ne peut pas le dire : vous allez pleurer aux vingt dernières pages.", n:"ça ne raconte rien et ça annonce tout"},
         e:{w:['le dénouement'], say:"Je m'arrête ici. Je ne vous dis pas ce qu'elle choisit. Lisez-le, vous verrez.", n:"trois façons de refuser, toutes polies"},
       },
       note:"Écoutez les deux versions du premier cas l'une après l'autre : c'est la différence entre donner envie et fermer la porte."},

      {t:'ex', h:"À écouter et à répéter",
       p:"Six phrases : quatre qu'on peut dire, deux qu'on garde pour soi.",
       rows:[
         ["C'est un roman de trois cents pages, une histoire de famille.","permis : le cadre"],
         ["Une femme revient au village pour vendre la maison de sa mère.","permis : le désir du personnage"],
         ["Elle trouve une boîte de lettres dans le grenier.","permis : l'obstacle"],
         ["Le personnage principal ne parle presque jamais.","permis : une description"],
         ["Finalement, elle décide de rester au village pour de bon.","interdit : c'est le dénouement"],
         ["Je m'arrête ici : je ne vous dis pas ce qu'elle choisit.","la phrase de sortie"],
       ]},

      {t:'piege', h:"Trois façons d'en dire trop sans s'en rendre compte",
       rows:[
         ["annoncer l'émotion de la fin","« vous allez pleurer aux vingt dernières pages »",
          "Vous venez de dire que ça finit mal. La personne lira le livre en attendant le malheur au lieu de le découvrir. Dites plutôt : « la fin m'a beaucoup touchée » — l'émotion est la vôtre, pas un programme."],
         ["raconter une révélation du milieu","« on apprend au chapitre douze que sa sœur est morte »",
          "Ce qui se découvre en cours de route compte autant que la dernière page. La limite n'est pas « la fin du livre » : c'est « le moment où le personnage doit choisir »."],
         ["répondre à la question « comment ça finit ? »","par gentillesse, parce que la personne insiste",
          "Elle insiste, mais elle ne veut pas vraiment savoir : elle veut savoir si ça vaut la peine. Répondez à cette question-là — « ça finit d'une façon que je n'avais pas vue venir » — et tout le monde est content."],
       ]},

      {t:'check', h:"Est-ce que c'est clair maintenant ?",
       p:"Quatre questions rapides.",
       qs:[
         {q:"On s'arrête de raconter…", opts:["au milieu du livre","au moment où le personnage doit choisir"], ok:1,
          fb:"Au moment du choix : c'est la frontière du club."},
         {q:"« Vous allez pleurer à la fin », c'est…", opts:["permis, ça ne raconte rien","interdit, ça annonce la fin"], ok:1,
          fb:"Interdit : ça ne raconte rien et ça dit tout."},
         {q:"Décrire un personnage qui ne parle jamais, c'est…", opts:["permis","interdit"], ok:0,
          fb:"Permis : c'est une description, pas un dénouement."},
         {q:"Quand on vous demande la fin, la réponse du club est…", opts:["« Lisez-le. »","« Je vous le dis, mais ne le répétez pas. »"], ok:0,
          fb:"« Lisez-le. » Polie, ferme, et elle donne encore plus envie."},
       ]},
    ]
  },

  // ════════════════════════════════════════════════════════════════════════
  t2mots: {
    eye:'Mini-leçon', tit:"La case, la bulle, la planche, l'album",
    blocs:[
      {t:'texte', h:"Quatre mots qu'on peut montrer du doigt",
       p:"La bande dessinée est le seul art dont le vocabulaire s'apprend en une minute, parce que chaque mot désigne quelque chose qu'on voit sur la page. Une bulle tient dans une case, une case tient dans une planche, une planche tient dans un album. Retenez l'ordre du plus petit au plus grand et vous ne vous tromperez plus : bulle, case, planche, album. Le reste — le tome, la série, l'onomatopée — se greffe là-dessus sans effort.",
       note:"Ce vocabulaire n'est pas décoratif : au comptoir, dire « je cherche le tome deux » ou « je cherche le deuxième livre » ne donne pas la même réponse, parce que le tome est un numéro et le livre est un objet."},

      {t:'ana', h:"La case et la planche",
       p:"La case est le petit cadre avec un dessin dedans. La planche est la page complète, avec toutes ses cases — parfois trois, parfois douze. Un album ordinaire compte une cinquantaine de planches.",
       mots:[["Ce qu'on dit d'une case","la première case · la dernière case du tome"],["Ce qu'on dit d'une planche","la planche 14 · une planche sans un seul mot",true],["Les cases sans texte","un visage · une main · une porte fermée"]],
       say:"Dans la première case, on voit seulement une porte fermée.",
       note:"Les cases sans texte sont souvent les plus fortes, et ce sont exactement celles qu'on décrit à voix haute quand on présente l'album au club."},

      {t:'ana', h:"La bulle, et ce que sa pointe raconte",
       p:"La bulle contient les mots d'un personnage. Sa pointe montre qui parle : suivez-la des yeux, elle mène toujours à une bouche. Et sa forme dit comment on parle.",
       mots:[["La pointe ordinaire","le personnage parle · les autres l'entendent"],["La pointe en petits ronds","le personnage pense · personne ne l'entend",true],["Le contour en dents de scie","le personnage crie, ou une voix sort d'un appareil"]],
       say:"La pointe de la bulle montre qui est en train de parler.",
       note:"La bulle de pensée est la plus utile à connaître : sans elle, on croit que le personnage a dit tout haut ce qu'il gardait pour lui, et l'histoire ne se tient plus."},

      {t:'ana', h:"L'onomatopée, le bruit qui n'appartient à personne",
       p:"Une onomatopée est un bruit écrit en grosses lettres, en dehors des bulles, parce qu'il n'est dit par personne : c'est le son de la scène. Sa taille dit son volume.",
       mots:[["Les bruits secs","BANG · VLAN · TOC TOC · CLAC"],["Les bruits qui durent","VROUM · DRING · SPLASH",true],["Ce que la taille indique","un petit toc dans un coin · un BANG sur la moitié de la case"]],
       say:"L'onomatopée occupe le tiers de la case, en grosses lettres.",
       note:"Chaque langue a ses onomatopées, et elles ne se ressemblent pas : c'est une des comparaisons les plus amusantes à faire en classe, et une des rares où tout le monde a quelque chose à apporter."},

      {t:'labo', h:"Montrez du doigt, dites le mot",
       p:"Choisissez ce que vous voulez nommer, et écoutez la phrase qui le désigne au club.",
       axes:[{id:'m', lbl:'Vous montrez quoi ?', opts:[
         ['a','le petit cadre'],
         ['b','la forme blanche avec une pointe'],
         ['c','la page complète'],
         ['d','le bruit en grosses lettres'],
         ['e','le livre au complet']]}],
       out:{
         a:{w:['une case'], say:"Une case. Dans la première case, on voit seulement une porte fermée.", n:"le plus petit des quatre"},
         b:{w:['une bulle'], say:"Une bulle. La pointe de la bulle montre qui est en train de parler.", n:"elle tient dans une case"},
         c:{w:['une planche'], say:"Une planche. Cette planche compte neuf cases et une seule bulle.", n:"la page entière"},
         d:{w:['une onomatopée'], say:"Une onomatopée. L'onomatopée occupe le tiers de la case, en grosses lettres.", n:"en dehors des bulles, toujours"},
         e:{w:['un album','une série'], say:"Un album. L'album que vous tenez est le premier tome de la série.", n:"l'objet, avec son numéro de tome"},
       },
       note:"Dites chacun des cinq mots en pointant réellement quelque chose sur une page, même imaginaire. Le geste fixe le mot bien mieux que la répétition."},

      {t:'ex', h:"À écouter et à répéter",
       p:"Six phrases qu'on entend au comptoir ou au club.",
       rows:[
         ["Dans la première case, on voit seulement une porte fermée.","la case et ce qu'elle montre"],
         ["La pointe de la bulle montre qui est en train de parler.","la bulle et sa pointe"],
         ["Cette planche compte neuf cases et une seule bulle.","les trois mots dans la même phrase"],
         ["L'onomatopée occupe le tiers de la case, en grosses lettres.","le bruit écrit"],
         ["L'album que vous tenez est le premier tome de la série.","album, tome, série"],
         ["On lit de gauche à droite, puis la rangée en dessous.","la seule règle d'ordre"],
       ]},

      {t:'piege', h:"Trois pièges de la bande dessinée",
       rows:[
         ["appeler « bulle » la case","« la bulle du haut » pour parler du dessin",
          "La bulle contient des mots ; la case contient un dessin. Une case peut n'avoir aucune bulle, et une bulle ne peut pas exister hors d'une case. Si ce que vous montrez est carré et dessiné, c'est une case."],
         ["lire les bulles avant de regarder","sauter d'une bulle à l'autre sans voir les images",
          "La moitié de l'histoire est dans le dessin. Un lecteur qui ne lit que les bulles ne comprend pas pourquoi les personnages réagissent, et il trouve la bande dessinée décevante — pour une raison qui ne vient pas d'elle."],
         ["confondre le tome et la planche","« le tome 14 » pour parler de la page 14",
          "Le tome est le numéro du livre dans la série ; la planche est la page dans le livre. « Tome 2, planche 14 » : deux échelles, deux mots, jamais interchangeables."],
       ]},

      {t:'check', h:"Est-ce que c'est clair maintenant ?",
       p:"Quatre questions rapides.",
       qs:[
         {q:"Du plus petit au plus grand, c'est…", opts:["case, bulle, planche, album","bulle, case, planche, album"], ok:1,
          fb:"Bulle, case, planche, album. La bulle tient dans la case."},
         {q:"Une pointe en petits ronds veut dire que le personnage…", opts:["pense","crie"], ok:0,
          fb:"Qu'il pense. Les autres personnages ne l'entendent pas."},
         {q:"L'onomatopée se place…", opts:["dans une bulle","en dehors des bulles"], ok:1,
          fb:"En dehors : le bruit n'est dit par personne."},
         {q:"« Planche 14 » désigne…", opts:["la page 14","le quatorzième livre"], ok:0,
          fb:"La page. Le livre, c'est le tome."},
       ]},
    ]
  },

  // ════════════════════════════════════════════════════════════════════════
  t2demo: {
    eye:'Mini-leçon', tit:"Celui, celle, ceux, celles",
    blocs:[
      {t:'texte', h:"Le mot qui évite de répéter le nom",
       p:"Écoutez deux minutes de conversation au comptoir d'une bibliothèque et vous entendrez ces quatre mots vingt fois. « Prenez celui qui a la couverture bleue. » « Celle que vous avez rapportée hier a une suite. » « Ceux du deuxième rayon sont plus faciles. » Ils remplacent un nom déjà dit, et ils gardent son genre et son nombre. Sans eux, on répète « le livre », « l'album », « la bande dessinée » à chaque phrase, et la conversation devient lourde à porter.",
       note:"Ce sont les pronoms démonstratifs complexes du programme de niveau 5. « Complexes » veut simplement dire qu'ils ne vivent jamais seuls : il y a toujours quelque chose derrière eux."},

      {t:'ana', h:"Quatre formes, accordées avec le nom remplacé",
       p:"L'accord se fait avec le nom qu'on remplace, jamais avec ce qui suit. Cherchez le nom, prenez son genre et son nombre, et choisissez.",
       mots:[["Masculin singulier","l'album → celui que j'ai lu"],["Féminin singulier","la planche → celle qui m'a marquée",true],["Pluriel","les personnages → ceux du début · les bulles → celles-là"]],
       say:"Celui que j'ai lu. Celle qui m'a marquée. Ceux du début.",
       note:"Les quatre formes se prononcent toutes différemment — celui, celle, ceux, celles —, ce qui est une chance : contrairement à « quel », l'accord s'entend."},

      {t:'ana', h:"Il ne vit jamais seul",
       p:"Il faut toujours quelque chose derrière : qui, que, de, ou -ci et -là collés au mot. Un « celui » tout seul au bout d'une phrase ne se dit pas.",
       mots:[["Avec qui ou que","celui qui parle · celle que je préfère"],["Avec de","ceux de la première planche · celle de ma sœur",true],["Avec -ci ou -là","celui-ci · celle-là · ceux-là"]],
       say:"Celui qui parle. Celle que je préfère. Ceux de la première planche.",
       note:"C'est la différence avec l'anglais, où « this one » se suffit à lui-même. En français, il faut dire lequel, et c'est ce qui vient après qui le dit."},

      {t:'ana', h:"Montrer du doigt, ou désigner par ce qu'on en dit",
       p:"« Celui-ci » et « celui-là » servent quand on montre quelque chose. « Celui qui » et « celui que » servent quand on désigne par une caractéristique. Le programme appelle le second cas « non déictique » : on ne pointe rien.",
       mots:[["On montre","celui-ci, sur la tablette · prenez celui-là"],["On désigne","celui que je préfère · celle qui a gagné un prix",true],["La faute courante","celui-ci pour parler d'un livre absent"]],
       say:"J'ai lu deux albums ; celui que je préfère est le deuxième.",
       note:"Si la chose n'est pas devant vous, « celui-ci » sonne faux. Employez « celui que », « celui qui », « celui de » — et la phrase redevient naturelle."},

      {t:'labo', h:"Quatre phrases du comptoir",
       p:"Choisissez un cas et écoutez la forme accordée dans sa phrase.",
       axes:[{id:'d', lbl:'On parle de quoi ?', opts:[
         ['a',"d'un album"],
         ['b',"d'une planche"],
         ['c','de plusieurs personnages'],
         ['d','de plusieurs bulles'],
         ['e','les quatre à la suite']]}],
       out:{
         a:{w:['un album'], say:"J'ai lu deux albums ; celui que je préfère est le deuxième.", n:"masculin singulier → celui"},
         b:{w:['une planche'], say:"Cette planche-ci est belle, mais celle de la fin est encore mieux.", n:"féminin singulier → celle"},
         c:{w:['un personnage'], say:"Les personnages qu'on voit au début, ceux-là reviennent au dernier tome.", n:"masculin pluriel → ceux"},
         d:{w:['une bulle'], say:"Les bulles qui ont une pointe en petits ronds, celles-là sont des pensées.", n:"féminin pluriel → celles"},
         e:{w:['un album','une planche'], say:"Celui que je préfère. Celle de la fin. Ceux du début. Celles-là.", n:"les quatre formes, à la suite"},
       },
       note:"Répétez les quatre à la suite en pensant chaque fois au nom remplacé. C'est le nom qui commande, jamais ce qui vient après."},

      {t:'ex', h:"À écouter et à répéter",
       p:"Six phrases du comptoir et du club.",
       rows:[
         ["Prenez celui qui a la couverture bleue.","masculin singulier, avec qui"],
         ["Celle que vous avez rapportée hier a une suite.","féminin singulier, avec que"],
         ["Les personnages qu'on voit au début, ceux-là reviennent.","masculin pluriel, avec -là"],
         ["Celles qui ont une pointe en petits ronds sont des pensées.","féminin pluriel, avec qui"],
         ["J'ai lu deux albums ; celui que je préfère est le deuxième.","on désigne, on ne montre pas"],
         ["Ceux de la première planche ne reparaissent jamais.","avec de, sans relative"],
       ]},

      {t:'piege', h:"Trois pièges des pronoms démonstratifs",
       rows:[
         ["laisser « celui » tout seul","« j'aime mieux celui »",
          "Il faut quelque chose derrière : celui-là, celui que j'ai lu, celui de ma sœur. Sans complément, la phrase reste en suspens et l'autre attend la suite qui ne vient pas."],
         ["accorder avec ce qui suit","« celle que j'ai lu » pour un album",
          "L'accord se fait avec le nom remplacé, pas avec le verbe ni avec le sujet de la relative. Album est masculin : celui que j'ai lu. Cherchez toujours le nom d'abord."],
         ["employer -ci pour une chose absente","« celui-ci » en parlant d'un livre resté à la maison",
          "-ci et -là servent à montrer. Si vous ne pouvez pas pointer du doigt, désignez par ce que vous en dites : celui que j'ai lu hier, celui dont je vous parle."],
       ]},

      {t:'check', h:"Est-ce que c'est clair maintenant ?",
       p:"Quatre questions rapides.",
       qs:[
         {q:"« La planche → ___ qui m'a marquée. »", opts:["celui","celle"], ok:1,
          fb:"Celle : planche est féminin singulier."},
         {q:"Un « celui » peut-il finir une phrase tout seul ?", opts:["oui","non"], ok:1,
          fb:"Non : il lui faut qui, que, de, -ci ou -là."},
         {q:"L'accord se fait avec…", opts:["le nom remplacé","le verbe qui suit"], ok:0,
          fb:"Le nom remplacé. Cherchez-le avant de choisir."},
         {q:"Pour un livre qui n'est pas devant vous, on dit…", opts:["celui-ci","celui que j'ai lu"], ok:1,
          fb:"Celui que j'ai lu : on désigne au lieu de montrer."},
       ]},
    ]
  },

  // ════════════════════════════════════════════════════════════════════════
  t2repr: {
    eye:'Mini-leçon', tit:"Reprendre l'œuvre sans se répéter",
    blocs:[
      {t:'texte', h:"Deux minutes sur un seul sujet : le problème est réel",
       p:"Une présentation de club, c'est deux minutes sur une seule chose. Si vous dites « le livre » quinze fois, la personne en face décroche avant la fin, sans savoir pourquoi. Le français règle ça en changeant de mot sans changer de sujet : le roman devient l'histoire, puis cette œuvre, puis ce récit. Personne ne se demande de quoi vous parlez, parce que c'est toujours le dernier nom cité qui commande. Le programme appelle ça la substitution lexicale, et c'est un savoir du niveau 5.",
       note:"Ce n'est pas de la coquetterie de style : c'est ce qui distingue un discours organisé d'une suite de phrases. Un correcteur le voit en trois lignes."},

      {t:'ana', h:"Remonter vers le mot plus général",
       p:"Du précis vers le large : album → livre → œuvre. On appelle ça un hyperonyme, mais le nom importe peu ; ce qui compte, c'est que le mot large soit toujours vrai pour le mot précis.",
       mots:[["Pour un album","cet album → ce livre → cette œuvre"],["Pour un film","ce film → cette œuvre → ce que j'ai vu",true],["Pour une chanson","cette chanson → ce morceau → cette œuvre"]],
       say:"C'est un album de bande dessinée. Cette œuvre m'a pris deux soirées.",
       note:"« Œuvre » est le mot le plus général du module : il est toujours vrai, il ne se trompe jamais, et c'est pour ça qu'on le garde pour la deuxième ou la troisième mention."},

      {t:'ana', h:"Passer au mot voisin",
       p:"Le synonyme n'est jamais tout à fait identique : chaque mot éclaire un côté différent. « Le roman » désigne l'objet, « l'histoire » désigne ce qu'il y a dedans, « le récit » désigne la façon de le raconter.",
       mots:[["Autour du livre","le roman · l'histoire · le récit"],["Autour de la série","la série · les épisodes · la saison",true],["Autour du personnage","le personnage · la femme · elle"]],
       say:"Le roman se passe au bord de la mer. Cette histoire ressemble à la mienne.",
       note:"La reprise par pronom — elle, il, ça — compte aussi, et c'est la plus économique. Attention seulement à ne pas en enchaîner quatre : au bout d'un moment, on ne sait plus qui est « elle »."},

      {t:'ana', h:"Le déterminant démonstratif fait la moitié du travail",
       p:"Le mot de reprise se présente presque toujours avec ce, cet, cette ou ces. Le démonstratif dit « celle dont je viens de parler » — c'est lui qui recolle, autant que le nom.",
       mots:[["Au masculin","ce livre · cet album · ce récit"],["Au féminin","cette histoire · cette œuvre · cette série",true],["Au pluriel","ces deux œuvres · ces épisodes"]],
       say:"Cette histoire m'a suivie pendant une semaine.",
       note:"C'est un savoir du niveau 5 : le déterminant démonstratif non déictique — on ne montre rien du doigt, on renvoie à ce qui vient d'être dit."},

      {t:'labo', h:"La même œuvre, reprise de cinq façons",
       p:"Choisissez une chaîne de reprise et écoutez-la en entier.",
       axes:[{id:'r', lbl:'Vous présentez quoi ?', opts:[
         ['a','un album de bande dessinée'],
         ['b','un roman'],
         ['c','une série'],
         ['d','un film'],
         ['e','deux œuvres comparées']]}],
       out:{
         a:{w:['un album','une œuvre'], say:"C'est un album de bande dessinée. Ce livre compte cinquante planches. Cette œuvre m'a pris deux soirées.", n:"album → livre → œuvre"},
         b:{w:['un roman'], say:"C'est un roman de trois cents pages. L'histoire se passe au bord de la mer. Ce récit ressemble à celui de ma mère.", n:"roman → histoire → récit"},
         c:{w:['une série'], say:"C'est une série de huit épisodes. Les derniers épisodes sont les plus forts. Cette œuvre mérite une deuxième saison.", n:"série → épisodes → œuvre"},
         d:{w:['une œuvre'], say:"C'est un film de deux heures. Cette histoire est vraie. Ce que j'ai vu là m'a suivi une semaine.", n:"film → histoire → ce que j'ai vu"},
         e:{w:['une œuvre','un roman'], say:"Ce film et ce roman racontent la même chose. Les deux œuvres sont fortes, mais la première est plus dure.", n:"un mot général pour deux œuvres à la fois"},
       },
       note:"Notez que chaque chaîne va du précis vers le général. L'inverse ne marche pas : commencer par « cette œuvre » ne dit à personne ce que vous tenez dans les mains."},

      {t:'ex', h:"À écouter et à répéter",
       p:"Six phrases où la reprise fait le lien.",
       rows:[
         ["C'est un album de bande dessinée. Cette œuvre m'a pris deux soirées.","album → œuvre"],
         ["Le roman se passe au bord de la mer. Cette histoire ressemble à la mienne.","roman → histoire"],
         ["Il y a quatre tomes en tout. La série complète est au rayon du fond.","tome → série"],
         ["Elle a emprunté une bande dessinée. Ce livre se garde trois semaines.","bande dessinée → livre"],
         ["Ce film et ce roman racontent la même chose. Les deux œuvres sont fortes.","deux œuvres, un seul mot"],
         ["Le personnage principal se tait. Cette femme n'explique jamais rien.","personnage → femme"],
       ]},

      {t:'piege', h:"Trois pièges de la reprise",
       rows:[
         ["changer pour un mot faux","dire « album » en parlant d'une série",
          "La reprise doit rester vraie. Une série n'est pas un album, un tome n'est pas une planche. Quand vous hésitez, « l'œuvre » et « l'histoire » conviennent presque toujours et ne trahissent rien."],
         ["enchaîner trop de pronoms","« elle… elle… elle… » sur cinq phrases",
          "Après deux « elle », remettez un nom : la femme, le personnage, la sœur aînée. Sinon l'auditeur reconstruit la mauvaise personne et ne s'en rend compte que trois phrases plus tard."],
         ["commencer par le mot général","« je vais vous parler de cette œuvre »",
          "La chaîne va du précis vers le général, jamais l'inverse. La première phrase doit dire ce que c'est ; les reprises viennent après, et elles vivent de ce que la première a posé."],
       ]},

      {t:'check', h:"Est-ce que c'est clair maintenant ?",
       p:"Quatre questions rapides.",
       qs:[
         {q:"Après « c'est un album », on peut reprendre par…", opts:["cette série","cette œuvre"], ok:1,
          fb:"Cette œuvre : le mot large est toujours vrai."},
         {q:"La reprise va…", opts:["du précis vers le général","du général vers le précis"], ok:0,
          fb:"Du précis vers le général : album, livre, œuvre."},
         {q:"« Le roman » et « l'histoire » désignent…", opts:["exactement la même chose","l'objet et ce qu'il contient"], ok:1,
          fb:"L'objet et ce qu'il contient : ce n'est pas tout à fait pareil."},
         {q:"Le déterminant qui recolle la reprise, c'est…", opts:["un, une, des","ce, cet, cette, ces"], ok:1,
          fb:"Le démonstratif : il dit « celle dont je viens de parler »."},
       ]},
    ]
  },

  // ════════════════════════════════════════════════════════════════════════
  t3fait: {
    eye:'Mini-leçon', tit:"Un fait, un avis, et pourquoi on les sépare",
    blocs:[
      {t:'texte', h:"Deux choses qui n'ont pas la même valeur",
       p:"Quand vous présentez une œuvre, les gens qui vous écoutent décident s'ils vont la lire ou la voir. Pour ça, ils ont besoin de deux choses très différentes : des faits, pour savoir dans quoi ils s'embarquent — trois cents pages, huit épisodes, une histoire vraie —, et de votre avis, pour savoir si ça leur ressemble. Mélangés dans la même phrase, les deux ne servent ni à l'un ni à l'autre. Séparés, ils font une présentation qu'on écoute jusqu'au bout.",
       note:"C'est le premier module du programme où l'on vous demande de donner une appréciation et de la justifier. Savoir qu'un avis est un avis est la première moitié du travail ; le dire clairement est la seconde."},

      {t:'ana', h:"Le test de la vérification",
       p:"Un fait se vérifie : deux personnes qui comptent trouvent le même chiffre. Un avis ne se vérifie pas : deux personnes trouvent deux réponses, et les deux ont raison.",
       mots:[["Ce qui se vérifie","trois cents pages · huit épisodes · quatre tomes"],["Ce qui ne se vérifie pas","c'est trop long · c'est lent · c'est magnifique",true],["Le cas limite","c'est une histoire vraie — un fait, qui se vérifie"]],
       say:"Le roman compte trois cents pages. Je le trouve trop long.",
       note:"Le nombre de pages est un fait ; « trop long » est un avis, même si les deux parlent de la même chose. « Trop » est presque toujours le mot d'un avis."},

      {t:'ana', h:"Les mots qui annoncent un avis",
       p:"Placez-en un devant votre jugement, et personne ne le prendra pour une information. C'est une politesse, et c'est aussi une précision.",
       mots:[["Les plus courants","je trouve que · selon moi · à mon avis"],["Plus prudents","j'ai l'impression que · il me semble que",true],["Ceux du club","ce que j'ai aimé, c'est · moi, ce qui m'a touché, c'est"]],
       say:"Je trouve que le dessin est plus fort que le texte.",
       note:"« Selon moi » et « à mon avis » se placent au début ou à la fin de la phrase, jamais au milieu. « Je trouve que » demande toujours une phrase complète derrière."},

      {t:'ana', h:"Les adjectifs sont presque tous des avis",
       p:"Émouvant, lent, prévisible, drôle, dur, magnifique : ce sont des jugements, même quand ils sonnent comme des constats. Le savoir change la façon dont on les dit.",
       mots:[["Ce qui touche","émouvant · touchant · dur · fort"],["Ce qui ennuie","lent · prévisible · long · répétitif",true],["Ce qui amuse","drôle · léger · rafraîchissant"]],
       say:"La fin est un peu prévisible, mais le reste tient debout.",
       note:"« La fin est prévisible » veut dire « moi, j'ai deviné la fin ». Quelqu'un d'autre ne l'avait peut-être pas devinée — d'où l'intérêt de mettre « je trouve » devant, au club comme ailleurs."},

      {t:'labo', h:"La même œuvre, en faits puis en avis",
       p:"Choisissez un aspect et écoutez d'abord le fait, ensuite l'avis qui va avec.",
       axes:[{id:'a', lbl:'On parle de quoi ?', opts:[
         ['a','la longueur'],
         ['b','le rythme'],
         ['c','la fin'],
         ['d','le dessin'],
         ['e','les deux dans la même phrase']]}],
       out:{
         a:{w:['un roman'], say:"Le fait : le roman compte trois cents pages. L'avis : je le trouve trop long de cent pages.", n:"le chiffre, puis le jugement"},
         b:{w:['une série'], say:"Le fait : la série a huit épisodes de quarante minutes. L'avis : je trouve que ça traîne au milieu.", n:"la durée, puis l'impression"},
         c:{w:['prévisible','le dénouement'], say:"Le fait : l'histoire se termine à la dernière page, sans épilogue. L'avis : la fin est un peu prévisible.", n:"attention : le second est un avis"},
         d:{w:['une planche','émouvant'], say:"Le fait : l'album compte cinquante planches en couleurs. L'avis : je trouve le dessin plus émouvant que le texte.", n:"un fait mesurable, un jugement"},
         e:{w:['une série','un avis'], say:"C'est une série de huit épisodes, et je la trouve trop longue de trois épisodes.", n:"le fait d'abord, l'avis ensuite"},
       },
       note:"La dernière option est la structure la plus solide du défi : le fait, puis « et je trouve que ». Apprenez-la telle quelle."},

      {t:'ex', h:"À écouter et à répéter",
       p:"Six phrases : trois faits, trois avis annoncés.",
       rows:[
         ["Le roman compte trois cents pages.","un fait : ça se compte"],
         ["La série a huit épisodes de quarante minutes.","un fait : deux chiffres"],
         ["L'album est le premier tome d'une série de quatre.","un fait : ça se vérifie au comptoir"],
         ["Je trouve que le dessin est plus fort que le texte.","un avis, annoncé"],
         ["La fin est un peu prévisible, mais le reste tient debout.","un avis, avec une nuance"],
         ["C'est une série de huit épisodes, et je la trouve trop longue.","le fait, puis l'avis"],
       ]},

      {t:'piege', h:"Trois façons de faire passer un avis pour un fait",
       rows:[
         ["dire un jugement sans l'annoncer","« c'est ennuyant » au lieu de « je trouve ça ennuyant »",
          "Sans l'annonce, votre jugement ressemble à une information sur l'œuvre. Trois mots de plus, et vous rendez à l'autre la liberté de ne pas être d'accord — ce qui est exactement l'esprit du club."],
         ["employer « tout le monde » ou « on »","« tout le monde trouve ça lent »",
          "Ce n'est pas un fait, c'est un avis déguisé en majorité. Dites « je » : personne au club ne vous reprochera d'avoir un avis, mais on vous reprendra si vous parlez au nom des autres."],
         ["confondre « trop » et « très »","« c'est trop long » comme si c'était une mesure",
          "« Très long » décrit ; « trop long » juge, parce que « trop » suppose une limite que vous avez fixée. Le mot est parfait pour un avis, à condition de savoir qu'on en donne un."],
       ]},

      {t:'check', h:"Est-ce que c'est clair maintenant ?",
       p:"Quatre questions rapides.",
       qs:[
         {q:"« La série a huit épisodes », c'est…", opts:["un fait","un avis"], ok:0,
          fb:"Un fait : ça se compte, et tout le monde trouve pareil."},
         {q:"« La fin est prévisible », c'est…", opts:["un fait","un avis"], ok:1,
          fb:"Un avis : quelqu'un d'autre ne l'avait peut-être pas devinée."},
         {q:"Le mot qui trahit presque toujours un avis, c'est…", opts:["trop","huit"], ok:0,
          fb:"« Trop » : il suppose une limite que vous avez fixée."},
         {q:"« Tout le monde trouve ça lent » est…", opts:["un fait vérifié","un avis déguisé"], ok:1,
          fb:"Un avis déguisé en majorité. Dites « je »."},
       ]},
    ]
  },

  // ════════════════════════════════════════════════════════════════════════
  t3disl: {
    eye:'Mini-leçon', tit:"Moi, ce qui m'a touché, c'est…",
    blocs:[
      {t:'texte', h:"La tournure qui met en avant ce qui compte",
       p:"Comparez deux phrases. « Le silence entre les deux sœurs m'a touchée. » Correcte, complète, et déjà oubliée. « Moi, ce qui m'a touchée, c'est le silence entre les deux sœurs. » La même information, mais le mot important arrive à la fin, après une petite attente, et l'auditeur a eu le temps de se préparer à le recevoir. Le français appelle ça une phrase emphatique par dislocation. Au club, c'est simplement la façon dont les gens parlent de ce qu'ils ont aimé.",
       note:"Elle a un deuxième mérite, moins avouable et très utile : elle vous donne deux secondes pour trouver la suite. Devant un groupe, en français, ces deux secondes-là valent cher."},

      {t:'ana', h:"ce qui — quand la chose fait l'action",
       p:"Employez ce qui quand ce que vous mettez en avant est le sujet du verbe. Le verbe suit tout de suite, sans sujet entre les deux.",
       mots:[["Ce qui plaît","ce qui m'a plu, c'est le dessin"],["Ce qui surprend","ce qui m'a surprise, c'est la lenteur",true],["Ce qui dérange","ce qui me dérange, c'est la fin trop rapide"]],
       say:"Moi, ce qui m'a touchée, c'est le silence entre les deux sœurs.",
       note:"Le test est le même qu'au Défi 1 : après « qui », un verbe tout seul. « Ce qui m'a plu » — « m' » est un complément, pas un sujet ; le sujet, c'est ce dont on parle."},

      {t:'ana', h:"ce que — quand c'est moi qui agis",
       p:"Employez ce que quand c'est vous, ou quelqu'un d'autre, qui faites l'action. Après que, il y a toujours un sujet.",
       mots:[["Ce que j'ai aimé","ce que j'ai aimé, c'est la fin ouverte"],["Ce que j'ai moins aimé","ce que j'ai le moins aimé, c'est la longueur",true],["Ce que les autres remarquent","ce que les gens remarquent, c'est le dessin"]],
       say:"Ce que j'ai le moins aimé, c'est la longueur des trois derniers chapitres.",
       note:"« Ce que j'ai le moins aimé » est la formule la plus utile du club : elle permet de dire une réserve sans démolir l'œuvre, et Gilberte la demande à tout le monde."},

      {t:'ana', h:"c'est, et le que qu'on oublie",
       p:"Quand ce qui suit « c'est » est un groupe de mots, on s'arrête là. Quand c'est une phrase complète avec un verbe, il faut ajouter que.",
       mots:[["Un groupe de mots","c'est le silence · c'est la lenteur du début"],["Une phrase complète","c'est que la fin arrive trop vite",true],["La faute à éviter","ce qui me dérange, c'est la fin arrive trop vite"]],
       say:"Ce qui me dérange, c'est que la fin arrive trop vite.",
       note:"Le petit « que » ne s'entend presque pas à l'oral rapide, et c'est justement pour ça qu'il disparaît à l'écrit. Relisez-vous : s'il y a un verbe conjugué après « c'est », il faut un « que »."},

      {t:'labo', h:"Cinq façons d'annoncer un avis",
       p:"Choisissez ce que vous voulez mettre en avant, et écoutez la phrase complète.",
       axes:[{id:'e', lbl:'Vous mettez en avant quoi ?', opts:[
         ['a',"ce qui vous a touché"],
         ['b',"ce que vous avez aimé"],
         ['c',"ce que vous avez moins aimé"],
         ['d','ce qui vous dérange, avec une phrase derrière'],
         ['e','les quatre à la suite']]}],
       out:{
         a:{w:['émouvant'], say:"Moi, ce qui m'a touchée, c'est le silence entre les deux sœurs.", n:"ce qui + verbe, puis c'est + groupe"},
         b:{w:['un avis'], say:"Ce que j'ai aimé, c'est la fin ouverte : elle laisse de la place au lecteur.", n:"ce que + sujet, puis la raison"},
         c:{w:['un avis'], say:"Ce que j'ai le moins aimé, c'est la longueur des trois derniers chapitres.", n:"la réserve, dite sans démolir"},
         d:{w:['le dénouement'], say:"Ce qui me dérange, c'est que la fin arrive trop vite.", n:"une phrase complète : il faut le que"},
         e:{w:['émouvant','un avis'], say:"Ce qui m'a touchée, c'est le silence. Ce que j'ai aimé, c'est la fin ouverte. Ce que j'ai le moins aimé, c'est la longueur. Ce qui me dérange, c'est que la fin arrive trop vite.", n:"les quatre moules de la présentation"},
       },
       note:"Ces quatre phrases couvrent presque tout ce qu'on dit d'une œuvre. Apprenez-les comme des moules et changez seulement la fin."},

      {t:'ex', h:"À écouter et à répéter",
       p:"Six phrases du Défi 3.",
       rows:[
         ["Moi, ce qui m'a touchée, c'est le silence entre les deux sœurs.","ce qui + c'est + groupe"],
         ["Ce que j'ai le moins aimé, c'est la longueur des derniers chapitres.","ce que + c'est + groupe"],
         ["Ce qui m'a surprise, c'est la lenteur du début.","le sujet mis en avant"],
         ["Ce qui me dérange, c'est que la fin arrive trop vite.","une phrase complète, donc que"],
         ["Ce que les gens remarquent d'abord, c'est le dessin.","le sujet n'est pas moi"],
         ["Ce qui fait la force de cet album, c'est le silence des cases.","sur une œuvre, pas sur soi"],
       ]},

      {t:'piege', h:"Trois pièges de la dislocation",
       rows:[
         ["choisir « ce que » à la place de « ce qui »","« ce que m'a touché » au lieu de « ce qui m'a touché »",
          "Après « que », il faut un sujet. Dans « ce qui m'a touché », le « m' » est un complément : personne ne fait l'action après lui, donc c'est « qui ». Faites le test du Défi 1, il vaut ici aussi."],
         ["oublier le « que » après « c'est »","« ce qui me dérange, c'est la fin arrive trop vite »",
          "Il y a un verbe conjugué derrière — arrive —, donc c'est une phrase complète, donc il faut « c'est que ». Sans lui, deux phrases sont collées l'une à l'autre sans rien pour les tenir."],
         ["accumuler les dislocations","quatre « ce qui, c'est » dans deux minutes",
          "La tournure attire l'attention ; répétée, elle la perd. Deux par présentation, pas plus : une pour ce que vous avez aimé, une pour votre réserve."],
       ]},

      {t:'check', h:"Est-ce que c'est clair maintenant ?",
       p:"Quatre questions rapides.",
       qs:[
         {q:"« ___ m'a touchée, c'est le silence. »", opts:["Ce qui","Ce que"], ok:0,
          fb:"Ce qui : après « qui », le verbe suit sans sujet."},
         {q:"« ___ j'ai aimé, c'est la fin ouverte. »", opts:["Ce qui","Ce que"], ok:1,
          fb:"Ce que : après « que », il y a un sujet — j'."},
         {q:"« Ce qui me dérange, c'est ___ la fin arrive trop vite. »", opts:["que","rien"], ok:0,
          fb:"Que : il y a un verbe conjugué derrière."},
         {q:"Combien de dislocations dans une présentation de deux minutes ?", opts:["deux","autant qu'on veut"], ok:0,
          fb:"Deux : une pour ce qu'on a aimé, une pour la réserve."},
       ]},
    ]
  },

  // ════════════════════════════════════════════════════════════════════════
  t3quel: {
    eye:'Mini-leçon', tit:"Quel, quelle, quels, quelles",
    blocs:[
      {t:'texte', h:"Ce que l'exclamation ajoute à un avis",
       p:"Un adjectif dit ce que vous pensez ; une exclamation dit à quel point. « C'est une belle façon de le dire » informe. « Quelle belle façon de le dire ! » emporte. Dans une présentation de deux minutes, une seule exclamation bien placée fait plus qu'un paragraphe d'adjectifs — et elle fait aussi quelque chose que rien d'autre ne fait : elle montre que vous avez été touché, pas seulement que vous avez jugé.",
       note:"Le déterminant exclamatif est un savoir du niveau 5, et l'accord en genre et en nombre est explicitement au programme. C'est une des rares règles où l'écrit demande plus que l'oral."},

      {t:'ana', h:"Quatre formes, un seul son",
       p:"Quel s'accorde avec le nom qui suit, et les quatre formes se prononcent exactement pareil. L'accord ne s'entend pas : il s'écrit.",
       mots:[["Masculin singulier","quel personnage ! · quel dénouement !"],["Féminin singulier","quelle histoire ! · quelle planche !",true],["Pluriel","quels dessins ! · quelles couleurs !"]],
       say:"Quel personnage ! Quelle histoire ! Quels dessins ! Quelles couleurs !",
       note:"Quatre orthographes, une prononciation. C'est exactement pour ce genre de cas que le module fait écrire l'exercice au lieu de le faire seulement écouter."},

      {t:'ana', h:"Avec un adjectif au milieu",
       p:"L'adjectif se glisse entre le déterminant et le nom, et l'accord ne change pas de règle : c'est toujours le nom, à la fin, qui commande tout le groupe.",
       mots:[["Au masculin","quel beau personnage ! · quel bon album !"],["Au féminin","quelle belle planche ! · quelle bonne façon de le dire !",true],["Au pluriel","quelles belles couleurs ! · quels beaux dessins !"]],
       say:"Quelle belle planche ! Quel beau personnage !",
       note:"L'adjectif s'accorde aussi, évidemment, et pour la même raison : beau, belle, beaux, belles suivent le nom qui vient derrière eux."},

      {t:'ana', h:"Exclamative ou interrogative ?",
       p:"Les mêmes mots servent aux deux. Ce qui les distingue, c'est la ponctuation à l'écrit, et la voix à l'oral : elle monte à la question, elle tombe à l'exclamation.",
       mots:[["Une question","quelle est votre œuvre préférée ?"],["Une exclamation","quelle œuvre !",true],["La différence à l'oral","la voix monte · la voix tombe"]],
       say:"Quelle est votre œuvre préférée ? Quelle œuvre !",
       note:"Dites les deux à la suite en exagérant la voix. C'est le seul moyen de sentir la différence, et elle se transporte ensuite dans toutes les exclamations du français."},

      {t:'labo', h:"Quatre exclamations du club",
       p:"Choisissez ce qui vous a frappé, et écoutez l'exclamation accordée.",
       axes:[{id:'q', lbl:'Vous vous exclamez sur quoi ?', opts:[
         ['a','un personnage'],
         ['b','une histoire'],
         ['c','des dessins'],
         ['d','des couleurs'],
         ['e','les quatre à la suite']]}],
       out:{
         a:{w:['un personnage'], say:"Quel personnage ! Je ne l'oublierai pas de sitôt.", n:"masculin singulier → quel"},
         b:{w:["l'intrigue"], say:"Quelle histoire ! Je l'ai lue en deux soirées.", n:"féminin singulier → quelle"},
         c:{w:['un album'], say:"Quels beaux dessins il y a dans cet album !", n:"masculin pluriel → quels"},
         d:{w:['une série'], say:"Quelles couleurs dans le dernier tome de la série !", n:"féminin pluriel → quelles"},
         e:{w:['un personnage','un album'], say:"Quel personnage ! Quelle histoire ! Quels beaux dessins ! Quelles couleurs !", n:"les quatre formes, un seul son"},
       },
       note:"Écoutez bien : les quatre se disent exactement pareil. Fermez les yeux, vous ne saurez jamais laquelle est écrite — c'est le nom qui suit qui vous le dira."},

      {t:'ex', h:"À écouter et à répéter",
       p:"Six exclamations, avec le nom qui commande.",
       rows:[
         ["Quelle belle façon de le dire !","façon, féminin singulier"],
         ["Quel personnage ! Je ne l'oublierai pas de sitôt.","personnage, masculin singulier"],
         ["Quelles couleurs dans le dernier tome !","couleurs, féminin pluriel"],
         ["Quels beaux dessins il y a dans cet album !","dessins, masculin pluriel"],
         ["Quelle histoire ! Je l'ai lue en deux soirées.","histoire, féminin singulier"],
         ["Quel dénouement ! Je ne vous en dis pas un mot.","dénouement, masculin singulier"],
       ]},

      {t:'piege', h:"Trois pièges du déterminant exclamatif",
       rows:[
         ["accorder avec l'adjectif","« quelles beaux dessins »",
          "L'adjectif ne commande rien : c'est le nom, à la fin du groupe, qui décide de tout. Dessins est masculin pluriel, donc quels beaux dessins. Cherchez le nom d'abord, toujours."],
         ["écrire « quel » pour un nom féminin","« quel histoire ! »",
          "Comme les quatre formes se prononcent pareil, rien ne prévient à l'oral. Le seul remède est de se demander le genre du nom avant d'écrire : une histoire, donc quelle histoire."],
         ["mettre un point d'interrogation","« Quelle histoire ? » quand on veut s'exclamer",
          "Le point change complètement le sens : avec un point d'interrogation, vous demandez laquelle. Avec un point d'exclamation, vous dites qu'elle vous a saisi. Un seul signe, deux phrases différentes."],
       ]},

      {t:'check', h:"Est-ce que c'est clair maintenant ?",
       p:"Quatre questions rapides.",
       qs:[
         {q:"« ___ couleurs ! » (couleurs, féminin pluriel)", opts:["Quels","Quelles"], ok:1,
          fb:"Quelles : le nom est féminin pluriel."},
         {q:"Les quatre formes se prononcent…", opts:["différemment","exactement pareil"], ok:1,
          fb:"Exactement pareil. L'accord s'écrit, il ne s'entend pas."},
         {q:"Dans « quel beau personnage ! », l'accord suit…", opts:["l'adjectif beau","le nom personnage"], ok:1,
          fb:"Le nom, toujours : c'est lui qui commande le groupe."},
         {q:"« Quelle est votre œuvre préférée ? » est…", opts:["une exclamation","une question"], ok:1,
          fb:"Une question : le point le dit, et la voix monte."},
       ]},
    ]
  },

};
