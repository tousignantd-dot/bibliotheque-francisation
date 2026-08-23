const PLUS = {

  prInto: {
    eye:'Mini-leçon', tit:"Ce que la voix ajoute aux mots",
    blocs:[
      {t:'texte', h:"Le seul savoir de phonétique du niveau 8",
       p:"Le programme du niveau 8 ne demande plus qu'une chose à l'oreille et à la voix : produire l'<b>intonation expressive</b>. Pas un son nouveau, pas une liaison de plus — une mélodie. À ce stade, vous prononcez assez bien pour être compris ; ce qui vous reste à gagner, c'est ce que la voix pose par-dessus les mots. Une même phrase de six mots peut dire l'admiration, la déception ou l'incompréhension, et c'est souvent la seule chose que votre interlocuteur retiendra.",
       note:"C'est aussi ce qui s'entend le plus vite chez quelqu'un qui apprend une langue : une intonation plate se lit comme de l'indifférence, alors qu'elle n'est le plus souvent que de la prudence."},

      {t:'texte', h:"Pourquoi ça compte dans une discussion sur une œuvre",
       p:"Un cercle de lecture est un endroit où l'on dit des choses fragiles à voix haute. Dire « c'est la plus belle dernière page que j'aie lue cette année » d'une voix égale annule la phrase : elle promet un enthousiasme que la voix dément, et personne n'y répond. À l'inverse, dire « je n'ai pas suivi » avec la bonne mélodie ne vous diminue jamais — cela signale une chose précise à reprendre, et la conversation continue.",
       note:"L'intonation ne sert pas à faire joli. Elle dit à l'autre où vous en êtes, et donc quoi vous répondre."},

      {t:'ana', h:"L'admiration — la voix s'élargit, puis appuie",
       p:"La phrase s'ouvre, le débit ralentit un peu, et la voix s'appuie longuement sur le mot qui porte l'éloge. Ce n'est pas une montée brusque : c'est une tenue.",
       mots:[['On dit',"C'est la plus belle dernière page que j'aie lue cette année."],['La mélodie','soutenue, appuyée sur « belle »',true],['Le repère','on ralentit au lieu de monter']],
       say:"C'est la plus belle dernière page que j'aie lue cette année.",
       note:"Une admiration dite vite passe pour de la politesse. C'est la lenteur qui la rend crédible."},

      {t:'ana', h:"La déception — la voix tombe dès la première syllabe",
       p:"La mélodie descend tout de suite et ne remonte jamais. Le débit est régulier, presque lent, souvent précédé d'un « ah » ou d'un « bon » qui tombe tout seul.",
       mots:[['On dit',"Ah bon. Moi qui attendais cette finale depuis six semaines."],['La mélodie','descendante du premier mot au dernier',true],['Le repère',"un « ah » ou un « bon » en tête"]],
       say:"Ah bon. Moi qui attendais cette finale depuis six semaines.",
       note:"Chez votre interlocuteur, c'est le signal qu'une réponse ne lui a pas plu. Il ne le dira pas ; la mélodie l'a déjà dit."},

      {t:'ana', h:"L'incompréhension — la voix freine et laisse un trou",
       p:"On ne monte pas : on ralentit. Le débit se casse à l'endroit précis où le fil s'est rompu, souvent avec un petit silence juste avant le mot en cause.",
       mots:[['On dit',"Le mot « défendable », vous l'entendez comment, exactement ?"],['La mélodie','un creux et un silence avant le mot',true],['Le repère',"on isole le mot avec la voix"]],
       say:"Le mot défendable, vous l'entendez comment, exactement ?",
       note:"C'est la mélodie qui dit « une seule chose m'échappe ». Sans elle, la même phrase s'entend comme « je n'ai rien suivi »."},

      {t:'ana', h:"La surprise — la voix monte d'un coup, à la fin",
       p:"La quatrième mélodie, la plus facile à produire et la plus facile à rater. La phrase part normalement puis grimpe brusquement sur les deux ou trois dernières syllabes.",
       mots:[['On dit',"Quatorze secondes sur des bottes de caoutchouc ?"],['La mélodie','plate, puis très haute à la fin',true],['Le repère','on répète le mot qui étonne']],
       say:"Quatorze secondes sur des bottes de caoutchouc ?",
       note:"Attention : si la voix monte trop tôt, la surprise devient un reproche — « vous vous moquez de moi »."},

      {t:'labo', h:"Écoutez les quatre intentions",
       p:"Choisissez une intention et un exemple.",
       axes:[
         {id:'i', lbl:'Quelle intention ?', opts:[['a','admiration'],['b','déception'],['c','incompréhension'],['d','surprise']]},
         {id:'n', lbl:'Quel exemple ?', opts:[['1','le premier'],['2','le second']]}],
       out:{
         a1:{w:["C'est magnifique."], say:"C'est magnifique.", n:'la voix tient sur la deuxième syllabe'},
         a2:{w:["Elle réussit tout ça sans une seule réplique."], say:"Elle réussit tout ça sans une seule réplique.", n:'le débit ralentit à mesure que la phrase avance'},
         b1:{w:["Ah bon."], say:"Ah bon.", n:'deux syllabes qui tombent : la déception se passe de phrase'},
         b2:{w:["Six épisodes pour arriver à ça."], say:"Six épisodes pour arriver à ça.", n:'descendante du début à la fin, sans colère'},
         c1:{w:["J'ai perdu le fil."], say:"J'ai perdu le fil.", n:'débit qui freine, mélodie creusée'},
         c2:{w:["Vous avez bien dit quatorze secondes ?"], say:"Vous avez bien dit quatorze secondes ?", n:"on isole le chiffre dont on n'est pas sûr"},
         d1:{w:["Quatorze secondes ?"], say:"Quatorze secondes ?", n:"la voix monte d'un coup sur le chiffre"},
         d2:{w:["Comment ça, elle ne détache pas la corde ?"], say:"Comment ça, elle ne détache pas la corde ?", n:'« comment ça » annonce la surprise'},
       },
       note:"Écoutez, puis répétez à voix haute en exagérant : l'exagération est ce qui fait entrer une mélodie dans l'oreille."},

      {t:'ex', h:"La même phrase, quatre intentions",
       p:"À gauche, ce qui est dit. À droite, ce que la voix ajoute.",
       rows:[
         ["Elle ne détache pas la corde ?","surprise — la voix monte sur « corde »"],
         ["Elle ne détache pas la corde.","constat — la voix reste plate"],
         ["Elle ne détache pas la corde…","incompréhension — la voix freine et laisse ouvert"],
         ["Elle ne détache pas la corde !","admiration — la voix s'élargit et appuie"],
         ["Bon. Elle ne détache pas la corde.","déception — le « bon » tombe avant le reste"],
         ["Ce qu'elle fait là, c'est immense.","admiration — la lenteur porte tout"],
       ]},

      {t:'piege', h:"Trois pièges de l'intonation, dans une discussion",
       rows:[
         ["monter la voix à chaque phrase","descendre quand on affirme",
          "Une mélodie qui monte partout transforme chaque affirmation en question, et chaque lecture en demande d'autorisation. C'est le défaut le plus fréquent, et il vient de la prudence : on n'ose pas conclure."],
         ["parler d'une voix parfaitement égale","varier sur les trois phrases qui comptent",
          "Une voix plate se lit comme de l'indifférence, jamais comme du calme. Vous n'avez pas besoin de jouer la comédie : trois phrases sur une heure suffisent."],
         ["baisser la voix pour dire son avis","garder la même mélodie qu'aux autres phrases",
          "Beaucoup de gens baissent la voix au moment de proposer une lecture. La proposition devient inaudible, et le groupe passe au suivant sans l'avoir entendue."],
       ]},

      {t:'check', h:"Est-ce que c'est clair maintenant ?",
       p:"Quatre questions rapides.",
       qs:[
         {q:"Pour exprimer l'admiration, la voix…", opts:["monte brusquement à la fin","ralentit et appuie"], ok:1,
          fb:"Elle tient et elle appuie. Une admiration dite vite passe pour de la politesse."},
         {q:"« Ah bon. Moi qui attendais ça depuis six semaines » exprime…", opts:["la déception","la surprise"], ok:0,
          fb:"La mélodie tombe dès la première syllabe : c'est la déception."},
         {q:"Freiner et laisser un silence avant un mot exprime…", opts:["l'incompréhension","l'admiration"], ok:0,
          fb:"Le silence isole le mot qui a manqué : une seule chose vous échappe, et vous le dites."},
         {q:"Une voix parfaitement égale pendant toute la soirée se lit comme…", opts:["du calme","de l'indifférence"], ok:1,
          fb:"Comme de l'indifférence, même quand elle n'est que de la prudence."},
       ]},

      {t:'revoir', h:"À retenir",
       p:"Quatre mélodies : l'<b>admiration</b> s'élargit et appuie ; la <b>déception</b> tombe dès la première syllabe ; l'<b>incompréhension</b> freine et laisse un trou avant le mot en cause ; la <b>surprise</b> monte d'un coup à la fin. Choisissez-en deux pour votre prochaine prise de parole et travaillez-les à voix haute."},
    ]
  },

  prFait: {
    eye:'Mini-leçon', tit:"Le fait, l'interprétation, le jugement",
    blocs:[
      {t:'texte', h:"Trois opérations qu'on dit d'un seul souffle",
       p:"« Elle s'assoit dans la chaloupe, elle renonce à partir, et franchement c'est raté. » Une phrase, trois opérations complètement différentes — et personne ne les entend passer. C'est ce mélange qui fait tourner un cercle de lecture à vide : deux personnes s'affrontent sur un jugement alors qu'elles ne se sont même pas entendues sur les faits.",
       note:"Séparer les trois ne rend pas la discussion plus froide. Cela la rend possible : on sait enfin sur quoi on n'est pas d'accord."},

      {t:'ana', h:"Le fait — je peux le vérifier en revoyant",
       p:"Un fait est ce que n'importe qui peut constater en revenant en arrière. Il ne vous appartient pas ; c'est le terrain commun.",
       mots:[['Un fait','Elle met les bottes de caoutchouc de sa mère.'],['Un fait','La corde reste attachée au taquet.',true],['Le test','je reviens en arrière et je vois la même chose']],
       say:"Elle met les bottes de caoutchouc de sa mère. La corde reste attachée au taquet.",
       note:"Un fait peut porter sur une durée, un objet, un mot prononcé, un mouvement de caméra. Il n'a pas besoin d'être important pour être un fait."},

      {t:'ana', h:"L'interprétation — j'ajoute ce que l'œuvre ne montre pas",
       p:"L'interprétation est le travail du lecteur. Elle n'est ni interdite ni douteuse : c'est elle qu'on est venu chercher. Le seul devoir est de savoir qu'on est en train d'en faire une.",
       mots:[["Une interprétation",'Elle renonce à partir.'],["Une interprétation",'Elle prend la place de sa mère.',true],['Le test',"ce n'est écrit nulle part : c'est moi qui l'apporte"]],
       say:"Elle renonce à partir. Elle prend la place de sa mère.",
       note:"Le verbe trahit toujours l'opération : « s'asseoir » se voit, « renoncer » se déduit."},

      {t:'ana', h:"Le jugement — je dis si c'est bon",
       p:"Le jugement classe l'œuvre. Il arrive en dernier, et il coûte une raison : sans elle, il ne nous apprend rien sur l'œuvre, seulement sur celui qui parle.",
       mots:[['Un jugement','Cette fin est ratée.'],['Un jugement','Les deux cadets jouent trop fort.',true],['Le test','je dis bon ou mauvais, pas ce qui se passe']],
       say:"Cette fin est ratée. Les deux cadets jouent trop fort.",
       note:"Un jugement accroché à un fait est un argument. Un jugement seul est une humeur."},

      {t:'labo', h:"Classez trois phrases sur la même scène",
       p:"Choisissez une scène et une opération.",
       axes:[
         {id:'s', lbl:'Quelle scène ?', opts:[['a','la chaloupe'],['b','le pot de départ'],['c','le stationnement']]},
         {id:'o', lbl:'Quelle opération ?', opts:[['1','un fait'],['2','une interprétation'],['3','un jugement']]}],
       out:{
         a1:{w:["Elle s'assoit dans la chaloupe et ne démarre pas le moteur."], say:"Elle s'assoit dans la chaloupe et ne démarre pas le moteur.", n:'vérifiable en revoyant la scène'},
         a2:{w:["Pour la première fois, c'est elle qui choisit."], say:"Pour la première fois, c'est elle qui choisit.", n:"le mot « choisit » n'est montré nulle part"},
         a3:{w:["Cette fin ne tient pas debout."], say:"Cette fin ne tient pas debout.", n:'aucun détail : pour l\'instant, c\'est une humeur'},
         b1:{w:["Elle prend la chaise du fond, contre le mur."], say:"Elle prend la chaise du fond, contre le mur.", n:'le texte le dit mot pour mot'},
         b2:{w:["Elle a choisi le fond pour que ça se voie."], say:"Elle a choisi le fond pour que ça se voie.", n:'l\'intention est ajoutée par le lecteur'},
         b3:{w:["Ce discours de quatre minutes est une honte."], say:"Ce discours de quatre minutes est une honte.", n:'un jugement, appuyé sur un fait daté : quatre minutes'},
         c1:{w:["Le moteur tourne depuis onze minutes."], say:"Le moteur tourne depuis onze minutes.", n:'un chiffre donné par le poème'},
         c2:{w:["La personne fait durer le geste pour ne pas partir."], say:"La personne fait durer le geste pour ne pas partir.", n:'le poème ne dit jamais pourquoi'},
         c3:{w:["C'est le plus beau poème du recueil."], say:"C'est le plus beau poème du recueil.", n:'un classement : jugement pur'},
       },
       note:"Refaites l'exercice sur une œuvre que vous connaissez : trois phrases, une par colonne. C'est plus difficile qu'il n'y paraît."},

      {t:'ex', h:"Le même détail, dans les trois colonnes",
       p:"À gauche, la phrase. À droite, l'opération.",
       rows:[
         ["Le plan des bottes dure quatorze secondes.","fait — on peut compter"],
         ["La réalisatrice insiste sur les bottes.","interprétation — « insister » est ajouté"],
         ["Ce plan est trop long.","jugement — bon ou mauvais"],
         ["Il l'appelle deux fois Ginette.","fait — c'est écrit"],
         ["Personne n'a retenu son nom en trente et un ans.","interprétation — on tire une conclusion"],
         ["Ce passage est le plus cruel du recueil.","jugement — un classement"],
       ]},

      {t:'piege', h:"Deux pièges, et ils sont partout",
       rows:[
         ["« Elle est triste »","« Elle ne lève pas les yeux »",
          "Une émotion n'est jamais un fait : on voit un visage, on déduit un sentiment. Presque toutes les phrases d'un cercle de lecture sont des interprétations déguisées en descriptions."],
         ["« Évidemment, elle renonce »","« Elle laisse sonner le téléphone : je comprends qu'elle renonce »",
          "« Évidemment », « clairement », « manifestement » font passer une interprétation pour un fait sans rien prouver. Quand vous entendez un de ces mots, cherchez le détail : s'il n'y en a pas, il n'y a rien."],
       ]},

      {t:'check', h:"Est-ce que c'est clair maintenant ?",
       p:"Quatre questions rapides.",
       qs:[
         {q:"« La corde reste attachée au taquet » est…", opts:["un fait","une interprétation"], ok:0,
          fb:"On peut revoir la scène et le constater : c'est un fait."},
         {q:"« Elle est prisonnière de ce chalet » est…", opts:["un fait","une interprétation"], ok:1,
          fb:"Rien ne le montre : le mot « prisonnière » est apporté par le spectateur."},
         {q:"Un jugement sans fait à côté nous apprend quelque chose sur…", opts:["l'œuvre","celui qui parle"], ok:1,
          fb:"Sur celui qui parle, uniquement. C'est pour cela qu'un jugement coûte une raison."},
         {q:"« Elle a l'air triste » est…", opts:["un fait","une interprétation"], ok:1,
          fb:"« Avoir l'air » signale justement la déduction : on voit un visage, on conclut."},
       ]},

      {t:'revoir', h:"À retenir",
       p:"Trois questions, dans cet ordre. <b>Est-ce que je peux le vérifier en revoyant ?</b> — c'est un fait. <b>Est-ce que j'ajoute quelque chose que l'œuvre ne montre pas ?</b> — c'est une interprétation. <b>Est-ce que je dis si c'est bon ou mauvais ?</b> — c'est un jugement. Les trois sont permis ; les mélanger ne l'est pas."},
    ]
  },

  prImpl: {
    eye:'Mini-leçon', tit:"L'implicite : ce qu'un texte laisse entendre",
    blocs:[
      {t:'texte', h:"Une phrase dit toujours plus que ses mots",
       p:"« On avait commencé sans elle » ne parle que d'une heure de début. Et pourtant tout le monde comprend autre chose : sa présence n'était pas nécessaire. Rien de cela n'est écrit, et personne n'a besoin qu'on le lui explique. C'est l'<b>implicite</b> : ce qu'un texte fait comprendre sans le dire, en comptant sur vous pour faire le dernier pas.",
       note:"L'implicite n'est pas une devinette. C'est un raccourci que l'auteur et le lecteur prennent ensemble — et il fonctionne d'autant mieux qu'il est court."},

      {t:'texte', h:"Pourquoi une langue étrangère rend l'implicite plus dur",
       p:"L'implicite s'appuie sur ce que tout le monde sait dans une société donnée : qu'un pot de départ commence par un discours, qu'une table du fond est celle des nouveaux, qu'on gratte le pare-brise du côté du conducteur en premier. Quand une de ces évidences vous manque, la phrase reste littérale et le sens tombe. Ce n'est pas un défaut de lecture : c'est un manque de contexte, et il se comble en demandant.",
       note:"Au cercle du mardi, la question « pourquoi est-ce que ça veut dire ça ? » n'est jamais une mauvaise question. Elle oblige les autres à expliciter ce qu'ils croyaient évident."},

      {t:'ana', h:"L'implicite par ce qui est omis",
       p:"L'auteur ne dit pas la chose : il décrit l'endroit vide qu'elle laisse.",
       mots:[['Le texte dit',"On ne le corrigea pas."],['On comprend',"Personne dans la salle ne connaissait son nom.",true],['Le levier',"une réaction qui n'a pas eu lieu"]],
       say:"On ne le corrigea pas. Personne dans la salle ne connaissait son nom.",
       note:"L'absence est le levier le plus fort de la littérature courte : ce qui n'arrive pas se remarque autant que ce qui arrive."},

      {t:'ana', h:"L'implicite par le détail concret",
       p:"Un objet, un chiffre, un geste — et le lecteur fait le reste tout seul.",
       mots:[['Le texte dit',"La banquette de droite est chaude pour rien."],['On comprend',"Quelqu'un s'asseyait là et ne s'y assoit plus.",true],['Le levier','un objet dont on nomme l\'usage perdu']],
       say:"La banquette de droite est chaude pour rien.",
       note:"Ce vers ne se comprend qu'après le dernier. C'est fait exprès : le poème vous demande une deuxième lecture."},

      {t:'ana', h:"L'implicite par la précision inutile",
       p:"Quand un texte court prend la peine de préciser quelque chose, c'est que ce quelque chose compte.",
       mots:[['Le texte dit',"Il l'appela deux fois Ginette."],['On comprend',"Ce n'est pas une distraction : c'est une habitude.",true],['Le levier','un nombre là où on ne l\'attendait pas']],
       say:"Il l'appela deux fois Ginette.",
       note:"« Deux fois » est le mot qui travaille. Une fois serait une erreur ; deux fois est un portrait."},

      {t:'labo', h:"Ce qui est dit, ce qu'on comprend",
       p:"Choisissez un texte et un passage.",
       axes:[
         {id:'t', lbl:'Quel texte ?', opts:[['a','la télésérie'],['b','la nouvelle'],['c','le poème']]},
         {id:'p', lbl:'Quel passage ?', opts:[['1','le premier'],['2','le second']]}],
       out:{
         a1:{w:["Elle laisse le téléphone sonner sur le quai."], say:"Elle laisse le téléphone sonner sur le quai.", n:"elle l'a porté jusque-là pour pouvoir le laisser"},
         a2:{w:["Elle met les bottes de caoutchouc de sa mère."], say:"Elle met les bottes de caoutchouc de sa mère.", n:"elle s'installe, ou elle prend une place qui était à quelqu'un"},
         b1:{w:["Une chaise restait libre au centre."], say:"Une chaise restait libre au centre.", n:"on lui avait bel et bien gardé la place d'honneur"},
         b2:{w:["Elle plia la nappe de papier et la mit dans son sac."], say:"Elle plia la nappe de papier et la mit dans son sac.", n:'un souvenir, ou la preuve de l\'endroit où on l\'a assise'},
         c1:{w:["Personne n'a jamais écrit ces règles."], say:"Personne n'a jamais écrit ces règles.", n:"elles viennent de quelqu'un, et ce quelqu'un manque"},
         c2:{w:["Je gratte encore, plus longtemps qu'il ne faut."], say:"Je gratte encore, plus longtemps qu'il ne faut.", n:'le geste sert à autre chose qu\'à dégager une vitre'},
       },
       note:"Remarquez que plusieurs sorties donnent deux lectures. C'est normal : un bon implicite en soutient souvent plus d'une."},

      {t:'ex', h:"Ce qui est dit · ce qui est entendu",
       p:"À gauche, la phrase du texte. À droite, ce qu'elle laisse entendre.",
       rows:[
         ["« On avait commencé sans elle. »","sa présence n'était pas nécessaire"],
         ["« Il l'appela deux fois Ginette. »","trente et un ans n'ont pas suffi"],
         ["« Elle dit qu'elle avait oublié ses lunettes. »","elle refuse de lire, et donne une autre raison"],
         ["« Vous passez la corde sous silence. »","vous évitez l'indice qui vous gêne"],
         ["« Je n'ai pas pu vérifier avant l'heure de tombée. »","le texte a été écrit trop vite"],
         ["« Il faut se garer le nez vers l'est. »","quelqu'un a enseigné ces règles, autrefois"],
       ]},

      {t:'piege', h:"Deux façons de se tromper sur l'implicite",
       rows:[
         ["tout lire au premier degré","chercher ce que la phrase fait, pas seulement ce qu'elle dit",
          "Un texte littéraire qui dit « il pleuvait » parle rarement de météo. Le premier degré n'est pas faux ; il est simplement incomplet."],
         ["voir de l'implicite partout","exiger un appui dans le texte",
          "Le défaut inverse existe, et il est plus difficile à corriger : on prête à l'auteur des intentions que rien ne soutient. Le contrôle est le même que pour une lecture — montrez le passage."],
       ]},

      {t:'check', h:"Est-ce que c'est clair maintenant ?",
       p:"Trois questions rapides.",
       qs:[
         {q:"L'implicite, c'est…", opts:["ce qui est écrit en petits caractères","ce que le texte fait comprendre sans le dire"], ok:1,
          fb:"Sans le dire — et en comptant sur vous pour faire le dernier pas."},
         {q:"« On ne le corrigea pas » fonctionne par…", opts:["une réaction qui n'a pas lieu","une comparaison"], ok:0,
          fb:"Par l'absence : ce qui n'arrive pas se remarque autant que ce qui arrive."},
         {q:"Quand une évidence culturelle vous manque…", opts:["c'est une faute de lecture","c'est un manque de contexte, et il se demande"], ok:1,
          fb:"Cela se demande, et la question oblige les autres à expliciter ce qu'ils croyaient évident."},
       ]},

      {t:'revoir', h:"À retenir",
       p:"Trois leviers d'implicite : <b>ce qui est omis</b> (une réaction qui n'a pas lieu), <b>le détail concret</b> (un objet dont l'usage a disparu), <b>la précision inutile</b> (un nombre là où on ne l'attendait pas). Devant chacun, une seule question : qu'est-ce que ce texte me demande de conclure tout seul ?"},
    ]
  },

  prRefor: {
    eye:'Mini-leçon', tit:"Redire avec d'autres mots",
    blocs:[
      {t:'texte', h:"Reformuler prouve qu'on a compris ; répéter prouve qu'on a entendu",
       p:"Reprendre les mots de l'autre est facile et ne coûte rien. Les remplacer par les vôtres est difficile, et c'est exactement pour cela que ça vaut quelque chose : on ne peut pas reformuler une phrase qu'on n'a pas comprise. Les attentes de fin de cours du niveau 8 le demandent en toutes lettres — l'adulte « résume les propos de son interlocuteur et emploie des paraphrases pour vérifier ou confirmer l'information reçue ».",
       note:"Dans une discussion, la reformulation fait deux choses à la fois : elle vous vérifie, et elle rend la parole à l'autre."},

      {t:'ana', h:"Autrement dit · en d'autres termes",
       p:"Ils redisent la même chose avec d'autres mots, sans rien ajouter ni retrancher. « En d'autres termes » est plus soutenu et se voit surtout à l'écrit.",
       mots:[['On entend',"On saute du fait au jugement."],['On reformule',"Autrement dit, l'interprétation manque au milieu.",true],['La règle',"rien de neuf ne doit entrer"]],
       say:"On saute du fait au jugement. Autrement dit, l'interprétation manque au milieu.",
       note:"Le test : la personne citée doit pouvoir approuver votre phrase d'un signe de tête, sans rien corriger."},

      {t:'ana', h:"C'est-à-dire — pour préciser, pas pour résumer",
       p:"Il introduit le détail qui manquait, et rétrécit au lieu d'élargir.",
       mots:[['On dit',"Elle a choisi le fond."],['On précise',"c'est-à-dire la table des stagiaires.",true],['La règle','la seconde moitié est plus étroite que la première']],
       say:"Elle a choisi le fond, c'est-à-dire la table des stagiaires.",
       note:"S'écrit avec deux traits d'union. On le confond souvent avec « autrement dit », qui ne précise rien."},

      {t:'ana', h:"En somme · bref — pour rassembler",
       p:"Ils ramassent plusieurs éléments en un seul. « Bref » est familier, « en somme » convient à l'écrit et à une discussion tenue.",
       mots:[['On énumère',"Deux lectures, trois indices, une heure et demie."],['On rassemble',"En somme, une bonne soirée.",true],['La règle','ce qui suit est plus court que ce qui précède']],
       say:"Deux lectures, trois indices, une heure et demie. En somme, une bonne soirée.",
       note:"« En somme » annonce une conclusion : ne l'employez pas au milieu d'un développement, l'auditoire croira que vous finissez."},

      {t:'ana', h:"Si je vous suis bien — la plus utile de toutes",
       p:"Elle rend la parole à l'autre et l'oblige à confirmer ou à corriger. C'est la reformulation de conversation, et elle transforme un désaccord en travail commun.",
       mots:[['On demande',"Si je vous suis bien, vous dites qu'elle choisit de rester ?"],['L\'autre répond','oui, ou : pas tout à fait, je dis que…',true],['La règle','on finit sur une question, jamais sur un point']],
       say:"Si je vous suis bien, vous dites qu'elle choisit de rester ?",
       note:"Employée deux fois dans une heure, elle change une discussion. Employée à chaque tour de parole, elle exaspère."},

      {t:'labo', h:"Choisir le bon connecteur",
       p:"Choisissez ce que vous voulez faire et l'exemple.",
       axes:[
         {id:'b', lbl:'Vous voulez…', opts:[['a','redire pareil'],['b','préciser'],['c','rassembler'],['d','faire confirmer']]},
         {id:'n', lbl:'Quel exemple ?', opts:[['1','le premier'],['2','le second']]}],
       out:{
         a1:{w:["Autrement dit, l'interprétation manque au milieu."], say:"Autrement dit, l'interprétation manque au milieu.", n:'même contenu, autres mots'},
         a2:{w:["En d'autres termes, il l'a écrit sans le savoir."], say:"En d'autres termes, il l'a écrit sans le savoir.", n:'la version soutenue, pour l\'écrit'},
         b1:{w:["Elle a choisi le fond, c'est-à-dire la table des stagiaires."], say:"Elle a choisi le fond, c'est-à-dire la table des stagiaires.", n:'on rétrécit : un détail de plus'},
         b2:{w:["Il a refusé, c'est-à-dire qu'il a demandé à quelqu'un d'autre."], say:"Il a refusé, c'est-à-dire qu'il a demandé à quelqu'un d'autre.", n:'la précision explique le mot d\'avant'},
         c1:{w:["En somme, un poème de deuil."], say:"En somme, un poème de deuil.", n:'vingt-deux vers ramassés en quatre mots'},
         c2:{w:["Bref, on n'a pas parlé du texte."], say:"Bref, on n'a pas parlé du texte.", n:'la version familière, pour l\'oral'},
         d1:{w:["Si je vous suis bien, la corde ne vous gêne pas ?"], say:"Si je vous suis bien, la corde ne vous gêne pas ?", n:'on finit sur une question'},
         d2:{w:["Si je comprends bien, vous lisez la scène à l'envers de moi ?"], say:"Si je comprends bien, vous lisez la scène à l'envers de moi ?", n:'le désaccord devient une vérification'},
       },
       note:"Quatre outils, quatre usages. Se tromper d'outil s'entend tout de suite : « en somme » devant une précision sonne faux."},

      {t:'ex', h:"Ce qu'on a entendu · ce qu'on en fait",
       p:"À gauche, la phrase de départ. À droite, la reformulation.",
       rows:[
         ["« Chacun raconte, puis chacun note. »","Autrement dit, on ne lit jamais."],
         ["« Elle a pris la chaise du fond. »","C'est-à-dire celle des stagiaires."],
         ["« Six pages, quatre gestes, aucune explication. »","En somme, tout est laissé au lecteur."],
         ["« La corde reste attachée. »","Si je vous suis bien, vous y voyez un piège ?"],
         ["« Je n'ai pas pu vérifier. »","En d'autres termes, il l'écrit sans le savoir."],
         ["« Trois strophes, un seul mot qui bascule. »","Bref, tout tient à la dernière ligne."],
       ]},

      {t:'piege', h:"Le piège de la reformulation",
       rows:[
         ["ajouter en reformulant","s'en tenir à ce qui a été dit",
          "« Autrement dit, vous trouvez la série mauvaise » alors que l'autre a seulement dit que la fin était rapide : ce n'est plus une reformulation, c'est une déformation, et l'autre a le droit de la refuser."],
         ["reformuler à chaque phrase","deux fois par heure, aux moments qui comptent",
          "Reformulée sans arrêt, la personne en face a l'impression de passer un examen. Gardez l'outil pour les endroits où le désaccord commence."],
       ]},

      {t:'check', h:"Est-ce que c'est clair maintenant ?",
       p:"Trois questions rapides.",
       qs:[
         {q:"« C'est-à-dire » sert à…", opts:["préciser","résumer"], ok:0,
          fb:"À préciser : ce qui suit est plus étroit que ce qui précède."},
         {q:"Le test d'une bonne reformulation, c'est que la personne citée…", opts:["ne réagisse pas","puisse l'approuver d'un signe de tête"], ok:1,
          fb:"Si elle doit corriger, vous avez ajouté quelque chose."},
         {q:"« Si je vous suis bien… » se termine par…", opts:["une question","un point"], ok:0,
          fb:"Par une question : c'est ce qui rend la parole à l'autre."},
       ]},

      {t:'revoir', h:"À retenir",
       p:"<b>Autrement dit</b> et <b>en d'autres termes</b> redisent pareil. <b>C'est-à-dire</b> précise. <b>En somme</b> et <b>bref</b> rassemblent. <b>Si je vous suis bien</b> fait confirmer, et c'est celui qui change une discussion. Dans tous les cas, une seule règle : rien de neuf ne doit entrer."},
    ]
  },

  t1cond: {
    eye:'Mini-leçon', tit:"Le conditionnel passé",
    blocs:[
      {t:'texte', h:"Le temps de ce qui n'a pas eu lieu",
       p:"Le conditionnel passé sert à nommer un geste que personne n'a fait. « Elle aurait pu détacher la corde » : elle ne l'a pas fait, et pourtant la phrase place le geste sous nos yeux. C'est pour cela qu'il est le premier outil de l'interprétation — une œuvre se comprend autant par ce qu'elle écarte que par ce qu'elle montre, et il faut un temps de verbe pour dire ce qu'elle a écarté.",
       note:"Sans ce temps, vous ne pouvez parler que de ce qui arrive. Avec lui, vous pouvez parler de tout ce qui aurait pu arriver — c'est-à-dire du travail de l'auteur."},

      {t:'ana', h:"Comment il se fabrique",
       p:"Deux morceaux que vous connaissez déjà : <b>avoir</b> ou <b>être</b> au conditionnel présent, puis le participe passé.",
       mots:[['Avec avoir',"j'aurais compris · elle aurait pu · nous aurions aimé"],['Avec être',"elle serait partie · ils seraient restés",true],['Aucune forme neuve',"vous savez déjà les deux moitiés"]],
       say:"J'aurais compris. Elle aurait pu. Elle serait partie.",
       note:"Le choix entre avoir et être est exactement le même qu'au passé composé : si vous dites « elle est partie », vous direz « elle serait partie »."},

      {t:'ana', h:"Le regret et le reproche — trois verbes suffisent",
       p:"Devoir, pouvoir, aimer au conditionnel passé portent le regret sans qu'on ait besoin de l'expliquer.",
       mots:[['Le reproche',"Tu aurais dû me le dire."],['Le regret',"J'aurais aimé un troisième acte.",true],['La possibilité manquée',"Elle aurait pu la détacher."]],
       say:"Tu aurais dû me le dire. J'aurais aimé un troisième acte. Elle aurait pu la détacher.",
       note:"Dans une critique, « on aurait aimé » est la formule polie du reproche. Le critique de « L'Écho » s'en sert, puis se dédit dans la même phrase."},

      {t:'ana', h:"L'information qu'on rapporte sans la garantir",
       p:"Le même temps sert au journalisme : il dit « je le rapporte, je ne le certifie pas ».",
       mots:[['On lit',"Le tournage aurait duré onze jours de plus."],['Ça veut dire',"quelqu'un le dit, le journal ne le confirme pas",true],['Le repère','aucun « si » nulle part dans la phrase']],
       say:"Le tournage aurait duré onze jours de plus que prévu.",
       note:"C'est le seul emploi du conditionnel qui ne parle pas d'hypothèse. Le reconnaître évite de croire un journal sur parole."},

      {t:'labo', h:"Trois emplois, deux exemples chacun",
       p:"Choisissez un emploi et un exemple.",
       axes:[
         {id:'e', lbl:'Quel emploi ?', opts:[['a','le geste non fait'],['b','le regret'],['c','l\'information non confirmée']]},
         {id:'n', lbl:'Quel exemple ?', opts:[['1','le premier'],['2','le second']]}],
       out:{
         a1:{w:["Elle aurait pu détacher la corde."], say:"Elle aurait pu détacher la corde.", n:'le geste existe dans la phrase, pas dans la scène'},
         a2:{w:["Elle serait partie au printemps."], say:"Elle serait partie au printemps.", n:'avec être : le participe s\'accorde'},
         b1:{w:["On aurait aimé un troisième acte."], say:"On aurait aimé un troisième acte.", n:'le reproche poli d\'une critique'},
         b2:{w:["Tu aurais dû venir mardi."], say:"Tu aurais dû venir mardi.", n:'le reproche direct, entre deux personnes'},
         c1:{w:["Le tournage aurait duré onze jours de plus."], say:"Le tournage aurait duré onze jours de plus.", n:'rapporté, non garanti'},
         c2:{w:["La pièce aurait coûté quarante mille dollars."], say:"La pièce aurait coûté quarante mille dollars.", n:'le journal se protège avec un temps de verbe'},
       },
       note:"Le troisième emploi se reconnaît à ce qu'il n'y a jamais de « si » dans la phrase."},

      {t:'ex', h:"Six phrases, six emplois",
       p:"À gauche, la phrase. À droite, ce qu'elle fait.",
       rows:[
         ["Elle aurait pu détacher la corde.","le geste qu'elle n'a pas fait"],
         ["Nous aurions aimé un dernier plan.","le regret d'un spectateur"],
         ["Tu aurais dû le dire tout de suite.","le reproche"],
         ["Le tournage aurait duré onze jours.","l'information non confirmée"],
         ["Sans les bottes, la scène serait restée fermée.","la conséquence d'une hypothèse"],
         ["Elle aurait compris, si on lui avait expliqué.","la moitié d'une hypothèse irréelle"],
       ]},

      {t:'piege', h:"Le piège de l'accord du participe",
       rows:[
         ["« elle aurait comprise »","« elle aurait compris »",
          "Avec <b>avoir</b>, le participe ne s'accorde jamais avec le sujet. C'est la faute la plus fréquente à ce temps-là, parce que l'oreille entend un sujet féminin et veut un e."],
         ["« elle serait resté »","« elle serait restée »",
          "Avec <b>être</b>, au contraire, il s'accorde toujours avec le sujet. Deux auxiliaires, deux règles opposées : c'est ce qui rend le temps difficile."],
       ]},

      {t:'check', h:"Est-ce que c'est clair maintenant ?",
       p:"Quatre questions rapides.",
       qs:[
         {q:"Le conditionnel passé se fabrique avec…", opts:["avoir ou être au conditionnel présent + participe passé","l'imparfait + un infinitif"], ok:0,
          fb:"Deux morceaux que vous connaissez déjà."},
         {q:"« Elle aurait ___ » — le participe de comprendre s'écrit…", opts:["compris","comprise"], ok:0,
          fb:"Avec avoir, pas d'accord avec le sujet."},
         {q:"« Le tournage aurait duré onze jours » veut dire…", opts:["c'est confirmé","c'est rapporté sans garantie"], ok:1,
          fb:"Aucun « si » dans la phrase : c'est l'emploi journalistique."},
         {q:"Pour dire un regret, les trois verbes les plus utiles sont…", opts:["devoir, pouvoir, aimer","aller, venir, faire"], ok:0,
          fb:"Devoir, pouvoir, aimer : ils portent le regret sans qu'on l'explique."},
       ]},

      {t:'revoir', h:"À retenir",
       p:"<b>avoir</b> ou <b>être</b> au conditionnel présent + participe passé. Trois emplois : le <b>geste non fait</b> (elle aurait pu), le <b>regret ou le reproche</b> (tu aurais dû), l'<b>information non confirmée</b> (le tournage aurait duré). Et une règle d'accord opposée selon l'auxiliaire."},
    ]
  },

  t1irreel: {
    eye:'Mini-leçon', tit:"Si les choses s'étaient passées autrement",
    blocs:[
      {t:'texte', h:"Trois hypothèses, et une seule change tout",
       p:"Le français range les hypothèses sur trois marches. « Si elle part, je le dirai » : c'est possible, ça peut encore arriver. « Si elle partait, je le dirais » : c'est imaginé, ça n'arrivera probablement pas. « Si elle était partie, je l'aurais dit » : c'est fini, ça ne peut plus arriver. La troisième marche s'appelle l'<b>irréel du passé</b>, et c'est celle dont vous avez besoin devant une œuvre : une œuvre est finie.",
       note:"Chaque marche recule d'un cran des deux côtés à la fois. Si vous savez faire la deuxième, vous savez faire la troisième."},

      {t:'ana', h:"La forme, et elle ne varie jamais",
       p:"<b>Si</b> + plus-que-parfait d'un côté, conditionnel passé de l'autre. L'ordre des deux moitiés est libre ; les temps, non.",
       mots:[['La condition',"Si elle avait voulu partir,"],['La conséquence',"elle aurait détaché la corde.",true],['Dans l\'autre sens',"Elle aurait détaché la corde si elle avait voulu partir."]],
       say:"Si elle avait voulu partir, elle aurait détaché la corde.",
       note:"Quand la condition vient en premier, une virgule sépare les deux moitiés. Quand elle vient en second, pas de virgule."},

      {t:'ana', h:"Jamais de conditionnel après « si »",
       p:"C'est la faute la plus surveillée du français écrit, et un correcteur la voit avant tout le reste.",
       mots:[['On écrit',"si elle avait su"],['On n\'écrit pas',"si elle aurait su",true],['Le repère','après « si », jamais de -rais, -rait, -rions']],
       say:"Si elle avait su, elle serait venue.",
       note:"Une règle simple pour l'oreille : le « r » du conditionnel ne se met pas dans la même moitié de phrase que le « si »."},

      {t:'ana', h:"Ce que ça permet de dire sur une œuvre",
       p:"L'irréel du passé sert à montrer qu'un détail compte : sans lui, il n'y aurait rien à discuter.",
       mots:[['Le détail',"la corde restée attachée"],['La phrase',"Si elle l'avait détachée, on n'en parlerait pas.",true],['L\'effet','le détail devient l\'objet de la discussion']],
       say:"Si elle l'avait détachée, on n'en parlerait pas un mardi matin.",
       note:"C'est une manière élégante d'argumenter : au lieu de dire « ce détail est important », on montre le vide qu'il laisserait."},

      {t:'labo', h:"Monter les trois marches",
       p:"Choisissez une marche et un exemple.",
       axes:[
         {id:'m', lbl:'Quelle hypothèse ?', opts:[['a','réelle'],['b','irréelle du présent'],['c','irréelle du passé']]},
         {id:'n', lbl:'Quel exemple ?', opts:[['1','la chaloupe'],['2','la lecture']]}],
       out:{
         a1:{w:["Si elle part, la série finit autrement."], say:"Si elle part, la série finit autrement.", n:'présent + présent ou futur : c\'est encore possible'},
         a2:{w:["Si vous venez mardi, vous entendrez trois lectures."], say:"Si vous venez mardi, vous entendrez trois lectures.", n:'présent + futur'},
         b1:{w:["Si elle partait, la série finirait autrement."], say:"Si elle partait, la série finirait autrement.", n:'imparfait + conditionnel présent : imaginé'},
         b2:{w:["Si vous veniez mardi, vous entendriez trois lectures."], say:"Si vous veniez mardi, vous entendriez trois lectures.", n:'la même chose, mais on n\'y croit pas trop'},
         c1:{w:["Si elle était partie, la série aurait fini autrement."], say:"Si elle était partie, la série aurait fini autrement.", n:'plus-que-parfait + conditionnel passé : c\'est fini'},
         c2:{w:["Si vous étiez venu mardi, vous auriez entendu trois lectures."], say:"Si vous étiez venu mardi, vous auriez entendu trois lectures.", n:'le reproche affectueux se dit à cette marche-là'},
       },
       note:"Lisez les six à voix haute dans l'ordre des colonnes : on entend la langue reculer d'un cran à chaque ligne."},

      {t:'ex', h:"Les trois marches, côte à côte",
       p:"À gauche, la phrase. À droite, ce qu'elle dit du réel.",
       rows:[
         ["Si elle part, je le dirai.","c'est encore possible"],
         ["Si elle partait, je le dirais.","c'est imaginé, peu probable"],
         ["Si elle était partie, je l'aurais dit.","c'est fini, ça ne peut plus arriver"],
         ["Si le plan avait duré deux secondes, personne ne l'aurait vu.","le détail justifie la discussion"],
         ["Si j'avais su, j'aurais regardé deux fois.","le regret, à la troisième marche"],
         ["Si vous étiez venu, vous auriez entendu.","le reproche affectueux"],
       ]},

      {t:'piege', h:"Deux pièges de l'irréel",
       rows:[
         ["« si elle aurait su »","« si elle avait su »",
          "Aucun conditionnel après « si ». Cette faute a un statut particulier en français : elle est repérée immédiatement, y compris par des gens qui n'expliqueraient pas la règle."],
         ["mélanger les marches","garder la même marche des deux côtés",
          "« Si elle était partie, je le dirais » boite : la première moitié est au passé, la seconde au présent. Elles doivent être du même cran, sauf effet voulu."],
       ]},

      {t:'check', h:"Est-ce que c'est clair maintenant ?",
       p:"Quatre questions rapides.",
       qs:[
         {q:"Après « si », dans l'irréel du passé, on met…", opts:["le plus-que-parfait","le conditionnel passé"], ok:0,
          fb:"Le plus-que-parfait. Le conditionnel passé va dans l'autre moitié."},
         {q:"« Si elle avait voulu partir, elle ___ la corde. »", opts:["aurait détaché","avait détaché"], ok:0,
          fb:"Conditionnel passé dans la conséquence."},
         {q:"L'irréel du passé dit que…", opts:["ça peut encore arriver","c'est fini et ça ne peut plus arriver"], ok:1,
          fb:"C'est la marche du « c'est trop tard » — celle qu'il faut devant une œuvre finie."},
         {q:"Quand la condition vient en premier…", opts:["une virgule sépare les deux moitiés","on ne met jamais de virgule"], ok:0,
          fb:"Virgule si la condition ouvre la phrase ; pas de virgule si elle la ferme."},
       ]},

      {t:'revoir', h:"À retenir",
       p:"<b>Si</b> + plus-que-parfait, puis <b>conditionnel passé</b>. Jamais de conditionnel après « si ». Trois marches : réelle (présent + futur), irréelle du présent (imparfait + conditionnel présent), irréelle du passé (plus-que-parfait + conditionnel passé). Une œuvre est finie : c'est la troisième qui sert."},
    ]
  },

  t1deux: {
    eye:'Mini-leçon', tit:"Ce qui fait qu'une lecture tient",
    blocs:[
      {t:'texte', h:"Deux personnes, la même scène, deux histoires",
       p:"Fatoumata et Léandre ont vu exactement la même chose. Ils s'entendent sur tous les faits : la chaloupe remise à l'eau, la corde attachée, le téléphone qui sonne, les bottes. Et ils n'en tirent pas la même histoire. Ce n'est pas que l'un a mal regardé : c'est qu'une œuvre ouverte accepte plusieurs lectures. La question n'est donc pas « qui a raison ? » mais « laquelle explique le plus ? ».",
       note:"C'est ce qui distingue une discussion sur une œuvre d'une dispute : on ne cherche pas à gagner, on cherche à couvrir la scène."},

      {t:'ana', h:"Une lecture se mesure : combien d'indices ?",
       p:"Mettez les indices en colonne et cochez ceux dont votre lecture rend compte. Le résultat est un nombre, et il tranche mieux qu'une conviction.",
       mots:[['La lecture A',"le téléphone, les bottes de ville enlevées, la chaloupe remise à l'eau"],['La lecture B',"la corde, les six épisodes de promesses, l'embarcation immobile",true],['Le partage',"les bottes et la lumière du quai appuient les deux"]],
       say:"Une lecture se mesure au nombre d'indices dont elle rend compte.",
       note:"Aucune des deux ne couvre tout, et c'est normal. Celle qui couvre le plus est la plus solide ce jour-là — pas pour toujours."},

      {t:'ana', h:"Retourner un indice, plutôt que le taire",
       p:"L'indice gênant se voit toujours. Le sortir soi-même le retourne au lieu de le subir.",
       mots:[['L\'objection',"la corde reste attachée"],['La lecture retournée',"la corde n'est pas ce qui la retient : c'est ce qu'elle laisse en place",true],['Le geste','on garde le fait et on change ce qu\'il signifie']],
       say:"La corde n'est pas ce qui la retient : c'est ce qu'elle laisse en place.",
       note:"Retourner n'est pas nier. On accepte le fait intégralement ; on discute seulement de ce qu'il veut dire."},

      {t:'ana', h:"Accepter qu'un indice appuie les deux lectures",
       p:"Certains détails sont franchement ambigus, et vouloir les trancher revient à effacer la moitié de la scène.",
       mots:[['L\'indice',"elle met les bottes de sa mère"],['Lecture A',"elle s'installe : c'est un choix",true],['Lecture B',"elle prend une place qui n'est pas la sienne"]],
       say:"Elle met les bottes de sa mère : elle s'installe, ou elle prend une place qui n'est pas la sienne.",
       note:"Un détail ambigu n'est pas un défaut de l'œuvre. C'est souvent l'endroit exact où la réalisatrice a travaillé le plus."},

      {t:'labo', h:"Un indice, deux lectures",
       p:"Choisissez un indice et une lecture.",
       axes:[
         {id:'i', lbl:'Quel indice ?', opts:[['a','le téléphone'],['b','la corde'],['c','les bottes']]},
         {id:'l', lbl:'Quelle lecture ?', opts:[['1','elle choisit'],['2','elle est prise']]}],
       out:{
         a1:{w:["Elle le porte jusqu'au quai pour pouvoir le laisser."], say:"Elle le porte jusqu'au quai pour pouvoir le laisser.", n:'le geste devient volontaire'},
         a2:{w:["Elle le laisse sonner parce qu'elle n'a plus rien à dire à personne."], say:"Elle le laisse sonner parce qu'elle n'a plus rien à dire à personne.", n:'le même geste devient un abandon'},
         b1:{w:["Elle laisse la corde en place : elle a décidé de ne pas partir."], say:"Elle laisse la corde en place : elle a décidé de ne pas partir.", n:'l\'indice gênant, retourné'},
         b2:{w:["Une chaloupe attachée n'emmène personne nulle part."], say:"Une chaloupe attachée n'emmène personne nulle part.", n:'l\'indice pris au premier degré'},
         c1:{w:["Elle enlève ses bottes de ville : elle s'installe ici."], say:"Elle enlève ses bottes de ville : elle s'installe ici.", n:'le changement de chaussures comme décision'},
         c2:{w:["Elle finit dans les bottes de sa mère, comme sa mère."], say:"Elle finit dans les bottes de sa mère, comme sa mère.", n:'la répétition d\'une vie, subie'},
       },
       note:"Six sorties, trois indices : chacun se lit dans les deux sens. C'est ce qui rend cette fin discutable — au bon sens du mot."},

      {t:'ex', h:"Ce qu'une bonne lecture fait, et ne fait pas",
       p:"À gauche, le geste. À droite, ce qu'il vaut.",
       rows:[
         ["Elle explique huit indices sur dix.","solide"],
         ["Elle explique quatre indices sur dix, dite très fort.","faible"],
         ["Elle passe l'indice gênant sous silence.","se voit toujours"],
         ["Elle reprend l'indice de l'autre et le retourne.","le geste le plus fort"],
         ["Elle accepte qu'un détail soit ambigu.","honnête, et souvent juste"],
         ["Elle cède devant une lecture qui explique plus.","on ne perd rien : on gagne une scène"],
       ]},

      {t:'piege', h:"Deux façons de perdre une discussion qu'on aurait pu tenir",
       rows:[
         ["répéter sa lecture plus fort","montrer un indice de plus",
          "Personne n'a jamais été convaincu par le volume. Une lecture avance d'un cran chaque fois qu'elle produit un détail que l'autre n'avait pas remarqué."],
         ["traiter l'autre lecture d'erreur","dire ce qu'elle explique mieux que la vôtre",
          "Reconnaître ce que l'autre couvre mieux ne vous affaiblit pas : cela vous rend crédible sur le reste, et c'est ce que le groupe entend."],
       ]},

      {t:'check', h:"Est-ce que c'est clair maintenant ?",
       p:"Trois questions rapides.",
       qs:[
         {q:"On départage deux lectures en demandant…", opts:["qui a raison","laquelle explique le plus d'indices"], ok:1,
          fb:"C'est le seul critère mesurable, et il tranche mieux qu'une conviction."},
         {q:"Devant l'indice qui gêne votre lecture, le mieux est de…", opts:["le sortir soi-même et le retourner","l'éviter"], ok:0,
          fb:"L'éviter se voit toujours. Le sortir vous donne l'initiative."},
         {q:"Un indice qui appuie les deux lectures est…", opts:["un défaut de l'œuvre","souvent l'endroit le plus travaillé"], ok:1,
          fb:"Vouloir le trancher revient à effacer la moitié de la scène."},
       ]},

      {t:'revoir', h:"À retenir",
       p:"Une lecture se juge à ce qu'elle explique, jamais à la force avec laquelle on l'affirme. Trois gestes : <b>compter les indices</b> qu'elle couvre, <b>retourner</b> celui qui gêne au lieu de le taire, et <b>accepter</b> qu'un détail soit ambigu. Et une conclusion : si quelqu'un propose mieux, on prend le sien."},
    ]
  },

  t1emph: {
    eye:'Mini-leçon', tit:"Mettre en avant ce qui porte votre lecture",
    blocs:[
      {t:'texte', h:"Une lecture repose presque toujours sur un seul détail",
       p:"Fatoumata a trois arguments, mais un seul la convainc vraiment : le téléphone. Si elle les énumère à la file, personne ne saura lequel compte, et la discussion se dispersera. L'emphase sert à cela : elle désigne le morceau de la phrase qui porte tout, et elle dit à l'autre exactement quoi contester.",
       note:"C'est un outil de clarté avant d'être un outil d'insistance. Il fait gagner du temps à tout le monde."},

      {t:'ana', h:"Le clivage — c'est… qui · c'est… que",
       p:"On extrait un morceau de la phrase et on le place en vedette, entre « c'est » et un relatif.",
       mots:[['La phrase plate',"Elle a remis la chaloupe à l'eau."],['Le sujet en vedette',"C'est elle qui a remis la chaloupe à l'eau.",true],['Le complément en vedette',"C'est la corde que vous passez sous silence."]],
       say:"C'est elle qui a remis la chaloupe à l'eau. C'est la corde que vous passez sous silence.",
       note:"<b>qui</b> quand le morceau extrait est sujet, <b>que</b> dans tous les autres cas. C'est la seule décision à prendre."},

      {t:'ana', h:"Le pseudoclivage — ce qui… c'est",
       p:"On annonce d'abord de quoi on va parler, puis on le nomme. La phrase se lit en deux temps, et l'attente fait le travail.",
       mots:[['La phrase plate',"Le téléphone compte le plus."],['Avec pseudoclivage',"Ce qui compte le plus, c'est le téléphone.",true],['Les autres formes',"ce que… c'est · ce dont… c'est · ce à quoi… c'est"]],
       say:"Ce qui compte le plus, c'est le téléphone.",
       note:"La forme se choisit sur la préposition du verbe : je pense <b>à</b> → ce <b>à quoi</b> je pense ; je parle <b>de</b> → ce <b>dont</b> je parle."},

      {t:'ana', h:"Mettre en avant un moment ou un lieu",
       p:"Deux formes de plus, utiles dans un récit ou une critique.",
       mots:[['Le moment',"Le jour où on discute, c'est le mardi."],["L'endroit","C'est au sous-sol que le cercle se réunit.",true],['La raison',"Si elle reste, c'est parce qu'elle a choisi."]],
       say:"C'est au sous-sol que le cercle se réunit. Si elle reste, c'est parce qu'elle a choisi.",
       note:"« Si… c'est parce que » est l'emphase de l'explication. Elle est très employée à l'écrit dans les textes d'opinion."},

      {t:'labo', h:"La même phrase, trois mises en relief",
       p:"Choisissez une phrase et le morceau à mettre en vedette.",
       axes:[
         {id:'p', lbl:'Quelle phrase ?', opts:[['a',"Estelle laisse le téléphone sonner"],['b',"Gisèle emporte la nappe"]]},
         {id:'m', lbl:'Quoi mettre en avant ?', opts:[['1','celle qui fait'],['2','ce qu\'elle fait'],['3','pourquoi']]}],
       out:{
         a1:{w:["C'est elle qui laisse le téléphone sonner."], say:"C'est elle qui laisse le téléphone sonner.", n:'clivage du sujet : personne ne l\'y oblige'},
         a2:{w:["Ce qu'elle laisse sonner, c'est le téléphone."], say:"Ce qu'elle laisse sonner, c'est le téléphone.", n:'pseudoclivage : l\'objet devient l\'indice'},
         a3:{w:["Si elle le laisse sonner, c'est parce qu'elle a choisi."], say:"Si elle le laisse sonner, c'est parce qu'elle a choisi.", n:'emphase de l\'explication'},
         b1:{w:["C'est Gisèle qui emporte la nappe."], say:"C'est Gisèle qui emporte la nappe.", n:'clivage du sujet'},
         b2:{w:["Ce qu'elle emporte, c'est la nappe."], say:"Ce qu'elle emporte, c'est la nappe.", n:'l\'objet en vedette, et il est dérisoire — c\'est l\'effet'},
         b3:{w:["Si elle l'emporte, c'est pour garder une preuve."], say:"Si elle l'emporte, c'est pour garder une preuve.", n:'l\'explication assumée comme telle'},
       },
       note:"Trois mises en relief de la même phrase, trois lectures différentes. L'emphase n'est pas décorative : elle oriente."},

      {t:'ex', h:"Avant · après",
       p:"À gauche, la phrase plate. À droite, la phrase mise en relief.",
       rows:[
         ["Le téléphone compte le plus.","Ce qui compte le plus, c'est le téléphone."],
         ["Elle a remis la chaloupe à l'eau.","C'est elle qui a remis la chaloupe à l'eau."],
         ["Vous passez la corde sous silence.","C'est la corde que vous passez sous silence."],
         ["Je pense à la parenthèse.","Ce à quoi je pense, c'est la parenthèse."],
         ["Il parle du dernier vers.","Ce dont il parle, c'est du dernier vers."],
         ["Le cercle se réunit au sous-sol.","C'est au sous-sol que le cercle se réunit."],
       ]},

      {t:'piege', h:"Trois pièges de l'emphase",
       rows:[
         ["« Ce qui comptent, ce sont les bottes »","« Ce qui compte, ce sont les bottes »",
          "Après « ce qui », le verbe reste au singulier, même devant un pluriel. Seul le « c'est / ce sont » de la seconde moitié peut se mettre au pluriel."],
         ["mettre trois emphases par paragraphe","deux par texte",
          "L'effet s'use très vite. Un texte qui insiste partout n'insiste plus nulle part, et le lecteur cesse de chercher ce qui compte."],
         ["« C'est la corde qui vous passez sous silence »","« C'est la corde que vous passez sous silence »",
          "« qui » seulement si le morceau extrait est le sujet du verbe. Ici, c'est vous qui passez : « la corde » est complément, donc « que »."],
       ]},

      {t:'check', h:"Est-ce que c'est clair maintenant ?",
       p:"Quatre questions rapides.",
       qs:[
         {q:"« C'est la corde ___ vous passez sous silence. »", opts:["que","qui"], ok:0,
          fb:"« La corde » est complément du verbe passer : donc « que »."},
         {q:"« Je pense à la parenthèse » se met en relief avec…", opts:["ce dont","ce à quoi"], ok:1,
          fb:"Penser à… donne « ce à quoi ». La préposition du verbe décide."},
         {q:"Après « ce qui », le verbe se met…", opts:["au singulier","au pluriel s'il y a plusieurs choses"], ok:0,
          fb:"Toujours au singulier. « Ce qui compte, ce sont les bottes. »"},
         {q:"Combien d'emphases par texte écrit ?", opts:["deux","le plus possible"], ok:0,
          fb:"Deux. Au-delà, l'effet s'use et le lecteur ne cherche plus."},
       ]},

      {t:'revoir', h:"À retenir",
       p:"<b>Clivage</b> : c'est… qui (sujet) · c'est… que (le reste). <b>Pseudoclivage</b> : ce qui / ce que / ce dont / ce à quoi… c'est. <b>Explication</b> : si…, c'est parce que. Un texte, deux emphases — et elles désignent l'indice sur lequel votre lecture repose."},
    ]
  },

  t2nouv: {
    eye:'Mini-leçon', tit:"Lire une nouvelle littéraire",
    blocs:[
      {t:'texte', h:"Ce n'est pas un roman raccourci",
       p:"Une nouvelle fait quelques pages, elle installe une situation, elle la resserre, et elle s'arrête — souvent sur un geste plutôt que sur une explication. Ce qui reste après la dernière ligne fait partie du texte : l'auteure a compté dessus. Lire une nouvelle en cherchant « la suite » revient à lire un poème en cherchant la morale.",
       note:"Six pages, quatre gestes, aucune explication : c'est un format, pas un manque. Il demande un lecteur qui accepte de finir le travail."},

      {t:'ana', h:"Le passé simple — le temps du récit écrit",
       p:"Il ne se parle plus depuis longtemps, mais il tient tout le récit littéraire. À reconnaître, jamais à produire dans une conversation.",
       mots:[['Verbes en -er',"elle poussa · ils poussèrent"],['La plupart des autres',"elle prit · il fit · on tendit · elle dit",true],['Les quatre à connaître',"elle fut · elle eut · elle fit · elle vint"]],
       say:"Elle poussa la porte. Elle prit la chaise du fond. Le contremaître fit un discours.",
       note:"Vous ne l'emploierez jamais à l'oral. Vous le lirez dans tous les romans, toutes les nouvelles et tous les contes que vous ouvrirez ici."},

      {t:'ana', h:"Le plus-que-parfait — ce qui s'était déjà passé",
       p:"Un cran plus tôt que le récit lui-même. Dans cette nouvelle, il porte tout ce qui s'est décidé sans Gisèle.",
       mots:[['Le récit',"Gisèle poussa la porte."],['Ce qui précède',"On avait commencé sans elle.",true],['Les autres',"la carte que l'atelier avait signée · personne ne s'y était assis"]],
       say:"Gisèle poussa la porte. On avait commencé sans elle.",
       note:"La grammaire dit ici la même chose que l'histoire : tout ce qui la concerne s'est réglé avant qu'elle entre."},

      {t:'ana', h:"La parenthèse du narrateur",
       p:"Une seule dans six pages. Le narrateur y sort de la scène pour nous dire ce que le personnage cache.",
       mots:[['Ce qu\'elle dit',"Elle dit qu'elle avait oublié ses lunettes."],['Ce que le narrateur ajoute',"(elle ne les avait pas oubliées)",true],['La conséquence','tout le reste se relit autrement']],
       say:"Elle dit qu'elle avait oublié ses lunettes ; elle ne les avait pas oubliées.",
       note:"Quand un texte court s'autorise cela une fois, la phrase concernée est le centre du texte. Cherchez toujours la seule fois."},

      {t:'labo', h:"Quatre gestes, deux lectures",
       p:"Choisissez un geste et une lecture.",
       axes:[
         {id:'g', lbl:'Quel geste ?', opts:[['a','la chaise du fond'],['b','le refus de lire'],['c','la nappe emportée']]},
         {id:'l', lbl:'Quelle lecture ?', opts:[['1','la femme effacée'],['2','la colère']]}],
       out:{
         a1:{w:["Elle se met au fond parce qu'elle s'est toujours mise au fond."], say:"Elle se met au fond parce qu'elle s'est toujours mise au fond.", n:'la lecture tendre : une habitude de retrait'},
         a2:{w:["Elle choisit le fond pour que ça se voie."], say:"Elle choisit le fond pour que ça se voie.", n:'la lecture de la colère : un geste public'},
         b1:{w:["Elle n'ose pas lire devant tout le monde."], say:"Elle n'ose pas lire devant tout le monde.", n:'la timidité — mais la parenthèse gêne cette lecture'},
         b2:{w:["Elle fait entendre par une autre voix ce que trente et un ans valent."], say:"Elle fait entendre par une autre voix ce que trente et un ans valent.", n:'le refus devient une mise en scène'},
         c1:{w:["Elle emporte un souvenir de sa dernière journée."], say:"Elle emporte un souvenir de sa dernière journée.", n:'la nappe comme relique'},
         c2:{w:["Elle emporte la preuve de l'endroit où on l'a assise."], say:"Elle emporte la preuve de l'endroit où on l'a assise.", n:'la nappe comme pièce à conviction'},
       },
       note:"Comptez : la lecture de la colère rend compte des trois gestes et de la parenthèse. La lecture tendre rend compte de deux gestes et bute sur la parenthèse."},

      {t:'ex', h:"Ce que le texte dit · ce qu'il montre",
       p:"À gauche, la phrase. À droite, ce qu'elle fait dans le récit.",
       rows:[
         ["« On avait commencé sans elle. »","plus-que-parfait : décidé avant elle"],
         ["« Elle traversa la salle. »","passé simple : l'action du récit"],
         ["« Personne ne dit rien. »","une réaction qui n'a pas lieu"],
         ["« Il l'appela deux fois Ginette. »","une précision qui fait tout le portrait"],
         ["« (elle ne les avait pas oubliées) »","le narrateur sort de la scène, une seule fois"],
         ["« Elle plia la nappe et la mit dans son sac. »","un geste à la place d'une conclusion"],
       ]},

      {t:'piege', h:"Deux erreurs devant une nouvelle",
       rows:[
         ["chercher ce qui manque","chercher ce qui a été mis",
          "Une nouvelle n'a pas de trous : elle a des choix. Chaque détail conservé sur six pages a coûté quelque chose à l'auteure — c'est là qu'il faut regarder."],
         ["confondre le narrateur et l'auteure","les tenir séparés",
          "Celui qui raconte est une voix construite : il peut se taire, se tromper, ou juger. Odile Brassard-Vézina n'est pas plus « la voix » de cette nouvelle que Gisèle n'est elle-même."],
       ]},

      {t:'check', h:"Est-ce que c'est clair maintenant ?",
       p:"Quatre questions rapides.",
       qs:[
         {q:"« Elle prit la chaise du fond » est au…", opts:["passé simple","plus-que-parfait"], ok:0,
          fb:"Passé simple : l'action du récit lui-même."},
         {q:"« On avait commencé sans elle » place l'action…", opts:["avant le récit","après le récit"], ok:0,
          fb:"Le plus-que-parfait recule d'un cran : c'était déjà fait."},
         {q:"La parenthèse du narrateur, dans cette nouvelle, apparaît…", opts:["une seule fois","à chaque page"], ok:0,
          fb:"Une seule fois — et c'est ce qui en fait le centre du texte."},
         {q:"La lecture qui explique le plus est celle qui rend compte…", opts:["des trois gestes et de la parenthèse","du geste le plus émouvant"], ok:0,
          fb:"Le nombre de détails couverts, toujours."},
       ]},

      {t:'revoir', h:"À retenir",
       p:"Une nouvelle finit sur un geste, pas sur une explication. <b>Passé simple</b> = l'action du récit ; <b>plus-que-parfait</b> = ce qui s'était passé avant ; <b>imparfait</b> = le décor. Et une règle de lecture : cherchez l'endroit où le narrateur sort de la scène — il n'y en a qu'un."},
    ]
  },

  t2poeme: {
    eye:'Mini-leçon', tit:"Lire un poème quand rien n'est expliqué",
    blocs:[
      {t:'texte', h:"Le décor n'est pas le sujet",
       p:"Vingt et un vers de « Déneigement » parlent de neige, de gratte et de doigts froids. Un lecteur pressé referme le poème en se disant que c'est joli et que ça parle de l'hiver. Le sujet est ailleurs, et il arrive au dernier vers. Prendre le décor pour le sujet est l'erreur la plus fréquente en lecture de poésie, et elle n'a rien à voir avec le niveau de langue.",
       note:"La parade est mécanique : lisez le dernier vers, puis relisez tout. Un poème court est écrit pour cette deuxième lecture."},

      {t:'ana', h:"La strophe est une unité, pas une mise en page",
       p:"Une ligne blanche entre deux groupes de vers sépare deux moments, comme un paragraphe sépare deux idées.",
       mots:[['Strophe 1',"le geste, ce matin-là"],['Strophe 2',"les règles, apprises de quelqu'un",true],['Strophe 3',"le retournement, en un mot"]],
       say:"Trois strophes : le geste, les règles, le retournement.",
       note:"Comptez les strophes avant de lire. Trois annoncent presque toujours une mise en place, un développement et un basculement."},

      {t:'ana', h:"Le dernier vers relit tous les autres",
       p:"Rien n'était caché : l'information n'était pas encore donnée. Après « je déneige quelqu'un qui n'est plus là », chaque vers d'avant change d'objet.",
       mots:[['Avant',"La banquette de droite est chaude pour rien."],['Après',"quelqu'un s'asseyait là et ne s'y assoit plus",true],['Le mécanisme','le sens arrive en dernier et remonte']],
       say:"La banquette de droite est chaude pour rien. Je déneige quelqu'un qui n'est plus là.",
       note:"Ce n'est pas un tour de passe-passe. C'est la façon dont un deuil se dit : par les objets, longtemps avant par les mots."},

      {t:'ana', h:"Comparaison et métaphore",
       p:"La comparaison dit qu'elle compare ; la métaphore ne le dit pas et remplace directement.",
       mots:[['Comparaison',"le bruit d'une allumette qui rate"],['Métaphore',"je déneige quelqu'un",true],['La différence',"« comme », « pareil à », « le bruit de » — ou rien"]],
       say:"La gratte fait le bruit d'une allumette qui rate. Je déneige quelqu'un.",
       note:"« Déneiger quelqu'un » n'a aucun sens littéral, et c'est exactement ce qui le rend juste : le geste continue sans son objet."},

      {t:'ana', h:"La répétition protège quelque chose",
       p:"Ce qui revient dans un poème court n'y revient jamais par hasard.",
       mots:[['Strophe 1',"en commençant par la droite, toujours par la droite"],['Strophe 3',"le côté droit, toujours le côté droit",true],['Ce que ça protège','une habitude prise à deux, tenue seule']],
       say:"En commençant par la droite, toujours par la droite. Le côté droit, toujours le côté droit.",
       note:"Cherchez d'abord ce qui se répète ; demandez ensuite ce que la répétition tient debout."},

      {t:'labo', h:"Trois strophes, deux lectures",
       p:"Choisissez une strophe et un moment de lecture.",
       axes:[
         {id:'s', lbl:'Quelle strophe ?', opts:[['a','la première'],['b','la deuxième'],['c','la troisième']]},
         {id:'m', lbl:'Quand ?', opts:[['1','à la première lecture'],['2','après le dernier vers']]}],
       out:{
         a1:{w:["Un matin d'hiver ordinaire, avant le jour."], say:"Un matin d'hiver ordinaire, avant le jour.", n:'on lit un poème sur le froid'},
         a2:{w:["Un geste appris de quelqu'un qu'on ne nomme pas encore."], say:"Un geste appris de quelqu'un qu'on ne nomme pas encore.", n:'« comme on m\'a montré » devient une présence'},
         b1:{w:["Des conseils pratiques pour déneiger une auto."], say:"Des conseils pratiques pour déneiger une auto.", n:'utile, et un peu drôle'},
         b2:{w:["Des règles léguées par quelqu'un, récitées comme une prière."], say:"Des règles léguées par quelqu'un, récitées comme une prière.", n:'« personne n\'a jamais écrit ces règles » se retourne'},
         c1:{w:["Le moteur tourne, la personne prend son temps."], say:"Le moteur tourne, la personne prend son temps.", n:'une lenteur inexpliquée'},
         c2:{w:["Elle fait durer le seul moment de la journée qui leur appartenait."], say:"Elle fait durer le seul moment de la journée qui leur appartenait.", n:'la lenteur devient le sujet du poème'},
       },
       note:"Comparez les deux colonnes : rien n'a changé dans le texte. C'est votre lecture qui a bougé, et c'est ce que le poème demandait."},

      {t:'ex', h:"Le vers · ce qu'il devient",
       p:"À gauche, le vers. À droite, ce qu'il veut dire à la relecture.",
       rows:[
         ["« comme on m'a montré »","quelqu'un a montré, et n'est plus là"],
         ["« personne n'a jamais écrit ces règles »","elles viennent d'une personne, pas d'un livre"],
         ["« à voix basse, dans le froid »","une récitation, presque une prière"],
         ["« la banquette de droite est chaude pour rien »","la place vide du passager"],
         ["« plus longtemps qu'il ne faut »","on fait durer, exprès"],
         ["« je déneige quelqu'un qui n'est plus là »","le vers qui relit tout le poème"],
       ]},

      {t:'piege', h:"Deux pièges de la lecture de poésie",
       rows:[
         ["chercher un message caché","chercher ce qui se répète et ce qui bascule",
          "Un poème n'est pas une énigme à décoder. Il organise des mots pour produire un effet ; le travail du lecteur est de repérer l'organisation, pas de trouver une réponse."],
         ["s'arrêter après une lecture","relire à partir du dernier vers",
          "Dans le poème court, le sens arrive souvent en dernier et remonte. Une seule lecture ne peut donc pas suffire : ce n'est pas un défaut d'attention."],
       ]},

      {t:'check', h:"Est-ce que c'est clair maintenant ?",
       p:"Quatre questions rapides.",
       qs:[
         {q:"Une ligne blanche entre deux groupes de vers est…", opts:["de la mise en page","une articulation de sens"], ok:1,
          fb:"Comme un paragraphe : elle sépare deux moments."},
         {q:"« Le bruit d'une allumette qui rate » est…", opts:["une comparaison","une métaphore"], ok:0,
          fb:"Elle dit qu'elle compare : « le bruit de ». La métaphore, elle, remplace sans le dire."},
         {q:"Dans « Déneigement », le sujet du poème apparaît…", opts:["dès le premier vers","au dernier vers"], ok:1,
          fb:"Au dernier — et il relit les vingt et un autres."},
         {q:"Ce qui se répète dans un poème court…", opts:["est un remplissage","protège quelque chose"], ok:1,
          fb:"Rien ne revient par hasard dans vingt-deux vers."},
       ]},

      {t:'revoir', h:"À retenir",
       p:"Comptez les <b>strophes</b>. Repérez ce qui <b>se répète</b>. Lisez le <b>dernier vers</b>, puis relisez tout. Distinguez la <b>comparaison</b> (elle se dit) de la <b>métaphore</b> (elle remplace). Et rappelez-vous que le décor — la neige, la gratte, le froid — n'est presque jamais le sujet."},
    ]
  },

  t2temps: {
    eye:'Mini-leçon', tit:"Passé simple et plus-que-parfait",
    blocs:[
      {t:'texte', h:"Deux temps qu'on lit tous les jours et qu'on ne parle jamais",
       p:"Vous n'emploierez jamais le passé simple dans une conversation, et personne ne vous le demandera. Vous le rencontrerez dans chaque roman, chaque nouvelle, chaque conte et beaucoup d'articles de fond. Il faut donc le <b>reconnaître</b>, pas le produire — et cette différence change complètement la façon de l'apprendre : quelques terminaisons et six verbes irréguliers suffisent.",
       note:"Le plus-que-parfait, lui, se parle très bien : « j'avais déjà mangé quand tu es arrivé ». C'est le seul des deux dont vous aurez besoin à l'oral."},

      {t:'ana', h:"Le passé simple des verbes en -er",
       p:"La famille la plus nombreuse, et la plus régulière.",
       mots:[['Singulier',"elle poussa · il regarda · on parla"],['Pluriel',"elles poussèrent · ils regardèrent",true],['Le repère',"un -a bien net, sans -it nulle part"]],
       say:"Elle poussa la porte. Ils regardèrent la chaise. On parla du sérieux et de la ponctualité.",
       note:"Ne confondez pas avec l'imparfait : « elle poussait » décrit, « elle poussa » raconte un geste unique et fini."},

      {t:'ana', h:"Le passé simple des autres verbes",
       p:"La plupart font -it au singulier et -irent au pluriel ; quelques-uns font -ut et -urent.",
       mots:[['En -it',"elle prit · il fit · on tendit · elle dit · elle vit"],['En -ut',"elle fut · elle eut · il put · il voulut",true],['Le sixième à savoir',"venir → elle vint · ils vinrent"]],
       say:"Elle prit la chaise du fond. Il fit un discours. Elle vint sans prévenir.",
       note:"Six verbes couvrent presque toutes les pages : être, avoir, faire, dire, voir, venir. Apprenez-les et le reste se devine."},

      {t:'ana', h:"Le plus-que-parfait — un cran avant",
       p:"<b>avoir</b> ou <b>être</b> à l'imparfait, puis le participe passé.",
       mots:[['Avec avoir',"on avait commencé · l'atelier avait signé"],['Avec être',"elle était partie · personne ne s'y était assis",true],['Ce qu\'il fait',"il place un fait plus tôt que le récit"]],
       say:"On avait commencé sans elle. Personne ne s'y était assis.",
       note:"C'est le temps de tout ce qui s'est décidé avant que le personnage entre — et dans cette nouvelle, c'est beaucoup."},

      {t:'labo', h:"Trois plans du récit",
       p:"Choisissez un plan et un exemple.",
       axes:[
         {id:'p', lbl:'Quel plan ?', opts:[['a','le décor (imparfait)'],['b','l\'action (passé simple)'],['c','l\'avant (plus-que-parfait)']]},
         {id:'n', lbl:'Quel exemple ?', opts:[['1','le premier'],['2','le second']]}],
       out:{
         a1:{w:["La salle était pleine."], say:"La salle était pleine.", n:'imparfait : un état, une toile de fond'},
         a2:{w:["Une chaise restait libre au centre."], say:"Une chaise restait libre au centre.", n:'imparfait : ça durait pendant la scène'},
         b1:{w:["Elle traversa la salle."], say:"Elle traversa la salle.", n:'passé simple : un geste unique, fini'},
         b2:{w:["Le contremaître fit un discours de quatre minutes."], say:"Le contremaître fit un discours de quatre minutes.", n:'passé simple irrégulier : faire → fit'},
         c1:{w:["On avait commencé sans elle."], say:"On avait commencé sans elle.", n:'plus-que-parfait : avant son arrivée'},
         c2:{w:["L'atelier avait signé la carte le matin même."], say:"L'atelier avait signé la carte le matin même.", n:'plus-que-parfait : réglé sans elle'},
       },
       note:"Trois plans, trois temps. Quand vous lisez, rangez chaque phrase dans l'une des trois colonnes : le texte s'organise tout seul."},

      {t:'ex', h:"Reconnaître au premier coup d'œil",
       p:"À gauche, la forme. À droite, le temps et l'infinitif.",
       rows:[
         ["elle poussa","passé simple · pousser"],
         ["ils prirent","passé simple · prendre"],
         ["il fit","passé simple · faire"],
         ["elle vint","passé simple · venir"],
         ["on avait commencé","plus-que-parfait · commencer"],
         ["elle s'était assise","plus-que-parfait · s'asseoir"],
       ]},

      {t:'piege', h:"Deux confusions fréquentes",
       rows:[
         ["« elle poussait » et « elle poussa »","l'un décrit, l'autre raconte",
          "L'imparfait installe un décor ou une habitude ; le passé simple avance l'histoire d'un geste. Dans un même paragraphe, ils alternent constamment."],
         ["croire qu'il faut savoir l'écrire","savoir le reconnaître",
          "Aucun examen de ce cours ne vous demandera de produire un passé simple dans une conversation. Ce qui compte est de ne pas buter dessus en lisant."],
       ]},

      {t:'check', h:"Est-ce que c'est clair maintenant ?",
       p:"Quatre questions rapides.",
       qs:[
         {q:"« Ils prirent » est le passé simple de…", opts:["prendre","prier"], ok:0,
          fb:"Prendre : elle prit, ils prirent."},
         {q:"« Elle était partie » est…", opts:["un plus-que-parfait","un passé simple"], ok:0,
          fb:"Être à l'imparfait + participe passé : plus-que-parfait."},
         {q:"Le passé simple sert surtout à…", opts:["décrire un décor","raconter un geste unique"], ok:1,
          fb:"C'est l'imparfait qui décrit ; le passé simple avance l'histoire."},
         {q:"Les six verbes à connaître au passé simple sont…", opts:["être, avoir, faire, dire, voir, venir","aller, partir, sortir, entrer, monter, descendre"], ok:0,
          fb:"Ces six-là couvrent presque toutes les pages que vous lirez."},
       ]},

      {t:'revoir', h:"À retenir",
       p:"<b>Passé simple</b> : -a / -èrent pour les verbes en -er, -it / -irent pour la plupart des autres, plus six irréguliers (fut, eut, fit, dit, vit, vint). À reconnaître, pas à parler. <b>Plus-que-parfait</b> : avoir ou être à l'imparfait + participe passé, pour ce qui s'était déjà passé."},
    ]
  },

  t2subj: {
    eye:'Mini-leçon', tit:"Dire son doute sans le déguiser",
    blocs:[
      {t:'texte', h:"Une interprétation qui se donne pour une certitude cesse d'être discutable",
       p:"« Elle est en colère » ferme la porte : ou bien on vous croit, ou bien on vous contredit. « Il se peut qu'elle soit en colère » laisse la porte ouverte et invite l'autre à répondre. Le subjonctif n'est pas une politesse : c'est ce qui permet d'avancer une lecture forte sans prétendre qu'elle est la seule. C'est exactement ce que le cercle du mardi cherchait sans le savoir.",
       note:"Le mode du verbe fait ici un travail que le contenu ne peut pas faire : il dit à quel titre vous parlez."},

      {t:'ana', h:"Ce qui déclenche le subjonctif",
       p:"Le doute, la possibilité, la concession, le refus de croire.",
       mots:[['La possibilité',"il se peut que · il est possible que"],['La concession',"bien que · quoique",true],['Le doute nié',"je ne crois pas que · je ne pense pas que"]],
       say:"Il se peut qu'elle soit en colère. Bien qu'il ait raison, sa lecture explique moins.",
       note:"« Il semble que » demande le subjonctif ; « il me semble que » ne le demande pas. Un pronom, et tout change."},

      {t:'ana', h:"Ce qui ne le déclenche pas",
       p:"La certitude, même faible, demande l'indicatif. C'est là que se produit presque toute la casse.",
       mots:[['Opinion assumée',"je crois que · je trouve que · il me semble que"],['Certitude',"il est certain que · il est clair que",true],['Rapport',"il paraît que · on dit que"]],
       say:"Il me semble qu'elle est en colère. Il paraît que la pièce se joue jusqu'au 14.",
       note:"Le repère est logique : si la tournure veut dire « je pense », vous assumez — donc l'indicatif."},

      {t:'ana', h:"Les formes qu'il faut savoir écrire",
       p:"Six verbes irréguliers, et une règle pour tous les autres.",
       mots:[['Les six',"qu'elle soit · qu'elle ait · qu'elle fasse · qu'elle puisse · qu'elle aille · qu'elle sache"],['La règle générale',"on part de la 3e personne du pluriel du présent",true],['Exemple',"ils prennent → qu'elle prenne · ils rendent → qu'elle rende"]],
       say:"Qu'elle soit, qu'elle ait, qu'elle fasse, qu'elle puisse, qu'elle aille, qu'elle sache.",
       note:"Pour la plupart des verbes, le subjonctif présent s'écrit exactement comme l'indicatif présent. Ce sont les six irréguliers qui font tout le travail."},

      {t:'labo', h:"Le même contenu, deux modes",
       p:"Choisissez une idée et le degré d'engagement.",
       axes:[
         {id:'i', lbl:'Quelle idée ?', opts:[['a','elle est en colère'],['b','l\'auteure l\'a fait exprès'],['c','cette lecture explique tout']]},
         {id:'d', lbl:'Vous…', opts:[['1','doutez'],['2','assumez']]}],
       out:{
         a1:{w:["Il se peut qu'elle soit en colère."], say:"Il se peut qu'elle soit en colère.", n:'subjonctif : la porte reste ouverte'},
         a2:{w:["Il me semble qu'elle est en colère."], say:"Il me semble qu'elle est en colère.", n:'indicatif : vous prenez la phrase à votre compte'},
         b1:{w:["Il est possible que l'auteure l'ait fait exprès."], say:"Il est possible que l'auteure l'ait fait exprès.", n:'subjonctif passé : le doute porte sur un fait passé'},
         b2:{w:["Je crois que l'auteure l'a fait exprès."], say:"Je crois que l'auteure l'a fait exprès.", n:'indicatif : une opinion assumée'},
         c1:{w:["Je ne crois pas que cette lecture explique tout."], say:"Je ne crois pas que cette lecture explique tout.", n:'la négation appelle le subjonctif'},
         c2:{w:["Je trouve que cette lecture explique tout."], say:"Je trouve que cette lecture explique tout.", n:'indicatif, et c\'est plus risqué'},
       },
       note:"Lisez les six à voix haute : la même idée change de statut social selon le mode. C'est tout l'intérêt."},

      {t:'ex', h:"Subjonctif · indicatif",
       p:"À gauche, le déclencheur. À droite, le mode.",
       rows:[
         ["il se peut que","subjonctif"],
         ["il est possible que","subjonctif"],
         ["bien que · quoique","subjonctif"],
         ["il semble que","subjonctif"],
         ["il me semble que","indicatif"],
         ["je crois que · il paraît que","indicatif"],
       ]},

      {t:'piege', h:"Le couple qui piège tout le monde",
       rows:[
         ["« il me semble qu'elle soit »","« il me semble qu'elle est »",
          "Avec le pronom, la tournure veut dire « je pense » : c'est une opinion assumée, donc l'indicatif. Sans le pronom, « il semble que » exprime une apparence sans sujet, donc le subjonctif."],
         ["« après que » au subjonctif","« après que » à l'indicatif",
          "« Avant que » demande le subjonctif ; « après que » demande l'indicatif, parce que la chose a eu lieu. La faute est si répandue qu'on l'entend partout, mais elle reste une faute à l'écrit."],
       ]},

      {t:'check', h:"Est-ce que c'est clair maintenant ?",
       p:"Quatre questions rapides.",
       qs:[
         {q:"« Il se peut qu'elle ___ en colère. »", opts:["soit","est"], ok:0,
          fb:"« Il se peut que » demande le subjonctif."},
         {q:"« Il me semble qu'elle ___ en colère. »", opts:["soit","est"], ok:1,
          fb:"Avec le pronom, c'est une opinion assumée : indicatif."},
         {q:"« Bien qu'il ___ raison, sa lecture explique moins. »", opts:["ait","a"], ok:0,
          fb:"« Bien que » demande toujours le subjonctif."},
         {q:"Le subjonctif de la plupart des verbes se fabrique sur…", opts:["l'infinitif","la 3e personne du pluriel du présent"], ok:1,
          fb:"ils prennent → qu'elle prenne. Six irréguliers font exception."},
       ]},

      {t:'revoir', h:"À retenir",
       p:"<b>Subjonctif</b> : il se peut que, il est possible que, il semble que, bien que, quoique, je ne crois pas que. <b>Indicatif</b> : il me semble que, je crois que, il paraît que, il est certain que. Six formes à savoir : soit, ait, fasse, puisse, aille, sache."},
    ]
  },

  t3crit: {
    eye:'Mini-leçon', tit:"Lire une critique, et lui répondre",
    blocs:[
      {t:'texte', h:"On peut discuter un texte sans avoir vu l'œuvre",
       p:"Personne au cercle n'a vu « Le troisième rang ». Personne ne peut donc dire si Gaspard Thivierge a raison. Mais tout le monde peut dire si son texte <b>tient</b> : où décrit-il, où juge-t-il, où devine-t-il, et chaque jugement est-il accroché à quelque chose ? C'est un travail complètement différent, et c'est celui qu'on fait toute sa vie avec les critiques qu'on lit.",
       note:"Ne jamais contester le fait — vous n'y étiez pas. Contester l'accrochage : ce jugement-là repose-t-il sur ce fait-là ?"},

      {t:'ana', h:"Ce qu'une critique décrit",
       p:"Les faits vérifiables : les dates, la durée, le nombre de comédiens, le lieu de l'action, ce qui arrive sur scène. Souvent les phrases les moins nombreuses.",
       mots:[['Un fait',"Quatre comédiens, un décor unique, une heure quarante."],['Un fait',"La comédienne ne quitte pas la scène.",true],['Leur usage','ce sont les seuls appuis disponibles']],
       say:"Quatre comédiens, un décor unique, une heure quarante sans entracte.",
       note:"Comptez-les en lisant. Une critique de trente lignes qui porte quatre faits vous en dit très peu sur la pièce."},

      {t:'ana', h:"Ce qu'elle juge",
       p:"Un jugement vaut ce que vaut le fait auquel il est accroché.",
       mots:[['Accroché',"Elle ne quitte pas la scène et porte le spectacle."],['Non accroché',"Le spectacle le plus juste de la saison.",true],['La question',"sur quoi cette phrase repose-t-elle ?"]],
       say:"Elle ne quitte pas la scène, et elle porte le spectacle d'un bout à l'autre.",
       note:"Un jugement seul ne vous apprend rien sur l'œuvre, seulement sur le critique. Ce n'est pas inutile — c'est autre chose."},

      {t:'ana', h:"Ce qu'elle devine, et qui doit se voir",
       p:"Le critique a le droit de supposer, à condition de le marquer.",
       mots:[['Les verbes à surveiller',"on devine · on sent · il semble · visiblement · sans doute"],['Dans ce texte',"On devine que l'auteur a grandi dans une famille de terriens.",true],['L\'aveu qui vaut de l\'or',"Je n'ai pas pu le vérifier avant l'heure de tombée."]],
       say:"On devine que l'auteur a grandi dans une famille de terriens.",
       note:"Un critique qui écrit « je n'ai pas pu vérifier » vous dit exactement où sa parole s'arrête. Cela rend le reste plus fiable, pas moins."},

      {t:'labo', h:"Trois phrases, trois statuts",
       p:"Choisissez une phrase et ce que vous voulez en faire.",
       axes:[
         {id:'p', lbl:'Quelle phrase ?', opts:[['a','le spectacle le plus juste'],['b','les cadets jouent trop fort'],['c','on devine que l\'auteur…']]},
         {id:'q', lbl:'Vous voulez…', opts:[['1','la classer'],['2','y répondre']]}],
       out:{
         a1:{w:["Un jugement d'ensemble, posé avant tout argument."], say:"Un jugement d'ensemble, posé avant tout argument.", n:'aucun fait ne le soutient encore'},
         a2:{w:["Sur quoi appuyez-vous ce classement ?"], say:"Sur quoi appuyez-vous ce classement ?", n:'on demande le fait manquant, sans nier le jugement'},
         b1:{w:["Un jugement, appuyé sur une observation de jeu."], say:"Un jugement, appuyé sur une observation de jeu.", n:'accroché à quelque chose, mais invérifiable pour nous'},
         b2:{w:["Vous leur reprochez le volume ; est-ce le jeu ou la salle ?"], say:"Vous leur reprochez le volume ; est-ce le jeu ou la salle ?", n:'on discute l\'accrochage, pas le fait'},
         c1:{w:["Une supposition, et elle est marquée comme telle."], say:"Une supposition, et elle est marquée comme telle.", n:'« on devine » fait le travail'},
         c2:{w:["Vous le devinez, et vous écrivez ne pas l'avoir vérifié."], say:"Vous le devinez, et vous écrivez ne pas l'avoir vérifié.", n:'on lui rend son propre aveu, sans agressivité'},
       },
       note:"Remarquez qu'on ne conteste jamais un fait dans la colonne de droite. On n'y était pas."},

      {t:'ex', h:"La phrase · ce qu'elle est",
       p:"À gauche, un extrait. À droite, son statut.",
       rows:[
         ["« Quatre comédiens, une heure quarante. »","fait vérifiable"],
         ["« Le spectacle le plus juste de la saison. »","jugement non accroché"],
         ["« Elle ne quitte pas la scène. »","fait vérifiable"],
         ["« Elle porte le spectacle d'un bout à l'autre. »","jugement accroché au fait précédent"],
         ["« On devine que l'auteur a grandi là. »","supposition marquée"],
         ["« Je n'ai pas pu le vérifier. »","aveu — et il rend le reste plus fiable"],
       ]},

      {t:'piege', h:"Deux façons de mal répondre à une critique",
       rows:[
         ["« Vous n'y connaissez rien »","« Ce jugement-là repose sur quel moment ? »",
          "Attaquer la personne ferme la discussion et ne se publie pas. Attaquer l'accrochage se publie, et le critique doit répondre."],
         ["contredire un fait qu'on n'a pas vu","travailler sur le texte qu'on a sous les yeux",
          "Vous n'étiez pas dans la salle. Le seul terrain où vous êtes son égal est le texte : sa construction, ses appuis, ses trous."],
       ]},

      {t:'check', h:"Est-ce que c'est clair maintenant ?",
       p:"Quatre questions rapides.",
       qs:[
         {q:"Sans avoir vu la pièce, on peut dire…", opts:["si la critique a raison","si la critique est appuyée"], ok:1,
          fb:"On peut examiner sa construction, pas vérifier son contenu."},
         {q:"« On devine que… » signale…", opts:["une supposition","un fait"], ok:0,
          fb:"Et c'est correct : le critique a le droit de supposer, s'il le marque."},
         {q:"Un jugement vaut ce que vaut…", opts:["le talent du critique","le fait auquel il est accroché"], ok:1,
          fb:"Sans fait à côté, il ne renseigne que sur celui qui parle."},
         {q:"Pour répondre à une critique, on conteste…", opts:["l'accrochage","le fait"], ok:0,
          fb:"L'accrochage. Vous n'étiez pas dans la salle : le fait vous échappe."},
       ]},

      {t:'revoir', h:"À retenir",
       p:"Trois opérations dans une critique : elle <b>décrit</b> (les faits), elle <b>juge</b> (avec ou sans appui), elle <b>devine</b> (et cela doit se voir). Pour répondre : comptez les faits, cherchez les jugements sans appui, et posez la question de l'accrochage. Jamais la personne."},
    ]
  },

  t3rel: {
    eye:'Mini-leçon', tit:"Citer un passage sans le répéter en entier",
    blocs:[
      {t:'texte', h:"Le problème que ces pronoms résolvent",
       p:"Dans une discussion sur une œuvre, on renvoie sans arrêt à des passages : celui dont il parle, celui auquel vous faites allusion, celui sur lequel votre jugement repose. Sans les relatifs à préposition, il faudrait tout répéter à chaque fois, ou dire « le passage que vous parlez de », qui ne se dit pas. Ce sont les outils du renvoi — et ils sont ce qui rend une phrase longue lisible.",
       note:"Ils sont aussi ce qui rend une phrase longue illisible quand on se trompe. D'où la méthode ci-dessous, qui ne varie jamais."},

      {t:'ana', h:"La méthode : chercher la préposition du verbe",
       p:"Ce n'est jamais le nom qui décide, c'est le verbe de la relative. Trouvez sa préposition, et le pronom suit.",
       mots:[['parler DE',"le détail dont il parle"],['penser À',"le passage auquel je pense",true],["s'appuyer SUR","le fait sur lequel vous vous appuyez"]],
       say:"Le détail dont il parle. Le passage auquel je pense. Le fait sur lequel vous vous appuyez.",
       note:"Faites la phrase à l'endroit pour trouver la préposition : « il parle de ce détail » → de → dont."},

      {t:'ana', h:"Dont — pour tout ce qui appelle « de »",
       p:"Le plus courant, et celui qui remplace le plus de choses.",
       mots:[['Complément du verbe',"la scène dont je me souviens"],['Complément du nom',"un poème dont la fin bascule",true],["Complément de l'adjectif","un texte dont il est fier"]],
       say:"La scène dont je me souviens. Un poème dont la fin bascule.",
       note:"Ne jamais doubler le « de » : on n'écrit pas « le détail dont il parle de ». Le « de » est déjà dans « dont »."},

      {t:'ana', h:"Ce dont, ce à quoi — quand rien n'est nommé devant",
       p:"S'emploient quand la chose n'a pas encore de nom dans la phrase.",
       mots:[['Avec un nom',"le passage dont il parle"],['Sans nom',"ce dont il parle",true],['Avec « à »',"ce à quoi je pense, c'est la parenthèse"]],
       say:"Ce dont il parle est à la troisième strophe. Ce à quoi je pense, c'est la parenthèse.",
       note:"Ces formes se combinent très bien avec l'emphase : « ce dont il ne parle jamais, c'est du jeu des cadets »."},

      {t:'ana', h:"Auquel, à laquelle, sur lequel — la chose est nommée",
       p:"Après une préposition, une chose prend lequel et ses composés ; une personne préfère « qui ».",
       mots:[['Une chose',"la question à laquelle personne ne répond"],['Une chose',"le fait sur lequel il s'appuie",true],['Une personne',"la voisine à qui elle tend la carte"]],
       say:"La question à laquelle personne ne répond. La voisine à qui elle tend la carte.",
       note:"à + lequel donne <b>auquel</b> ; à + lesquels donne <b>auxquels</b>. « à laquelle » ne se contracte pas."},

      {t:'labo', h:"Le verbe décide",
       p:"Choisissez un verbe et le mot repris.",
       axes:[
         {id:'v', lbl:'Quel verbe ?', opts:[['a','parler de'],['b','penser à'],['c','s\'appuyer sur']]},
         {id:'m', lbl:'On reprend…', opts:[['1','une chose nommée'],['2','rien de nommé']]}],
       out:{
         a1:{w:["le détail dont il parle"], say:"Le détail dont il parle est à la troisième strophe.", n:'de → dont'},
         a2:{w:["ce dont il parle"], say:"Ce dont il parle est à la troisième strophe.", n:'rien devant : ce dont'},
         b1:{w:["le passage auquel je pense"], say:"Le passage auquel je pense tient en une parenthèse.", n:'à + lequel → auquel'},
         b2:{w:["ce à quoi je pense"], say:"Ce à quoi je pense, c'est la parenthèse.", n:'rien devant : ce à quoi'},
         c1:{w:["le fait sur lequel il s'appuie"], say:"Le fait sur lequel il s'appuie n'est pas dans la critique.", n:'sur + lequel, sans contraction'},
         c2:{w:["ce sur quoi il s'appuie"], say:"Ce sur quoi il s'appuie n'est pas dans la critique.", n:'rien devant : ce sur quoi'},
       },
       note:"Six cases, un seul raisonnement : la préposition du verbe, puis la présence ou l'absence d'un nom devant."},

      {t:'ex', h:"Le verbe · le pronom",
       p:"À gauche, le verbe et sa préposition. À droite, le pronom.",
       rows:[
         ["parler de, se souvenir de, avoir besoin de","dont"],
         ["penser à, faire allusion à (une chose)","auquel, à laquelle"],
         ["répondre à (une question)","à laquelle"],
         ["s'appuyer sur, compter sur","sur lequel, sur laquelle"],
         ["tendre à, parler à (une personne)","à qui"],
         ["rien de nommé devant","ce dont, ce à quoi, ce sur quoi"],
       ]},

      {t:'piege', h:"Trois pièges des relatifs",
       rows:[
         ["« le passage que vous parlez »","« le passage dont vous parlez »",
          "« Que » ne remplace jamais un complément introduit par une préposition. C'est la faute la plus répandue, et elle vient de l'oral rapide."],
         ["« le détail dont il parle de »","« le détail dont il parle »",
          "Le « de » est déjà contenu dans « dont ». Le répéter double la préposition."],
         ["« le fait que vous vous appuyez dessus »","« le fait sur lequel vous vous appuyez »",
          "À l'écrit soutenu, la préposition ne se rejette jamais à la fin de la phrase. La forme avec « dessus » est parlée et ne se publie pas."],
       ]},

      {t:'check', h:"Est-ce que c'est clair maintenant ?",
       p:"Quatre questions rapides.",
       qs:[
         {q:"« Le détail ___ il parle. »", opts:["dont","auquel"], ok:0,
          fb:"Parler de… → dont."},
         {q:"« La question ___ personne n'a répondu. »", opts:["dont","à laquelle"], ok:1,
          fb:"Répondre à… → à laquelle."},
         {q:"Ce qui décide du pronom, c'est…", opts:["le nom repris","la préposition du verbe"], ok:1,
          fb:"Toujours le verbe. Faites la phrase à l'endroit pour la trouver."},
         {q:"Devant une personne, après « à », on préfère…", opts:["à qui","à laquelle"], ok:0,
          fb:"« La voisine à qui elle tend la carte » — plus naturel et plus court."},
       ]},

      {t:'revoir', h:"À retenir",
       p:"Le <b>verbe</b> donne la préposition, la préposition donne le pronom. <b>de</b> → dont (ce dont) · <b>à</b> → auquel, à laquelle (ce à quoi), à qui pour une personne · <b>sur</b> → sur lequel (ce sur quoi). Jamais de préposition rejetée à la fin, jamais de « de » doublé."},
    ]
  },

  t3conc: {
    eye:'Mini-leçon', tit:"Accorder quelque chose avant de répondre",
    blocs:[
      {t:'texte', h:"Concéder n'est pas céder",
       p:"Quelqu'un qui n'accorde jamais rien n'est plus écouté au bout de deux minutes : le groupe entend qu'il défend une position, pas qu'il examine une œuvre. Concéder, c'est reconnaître ce que l'autre a de juste, puis avancer son propre point. Vous ne perdez rien — vous gagnez le droit d'être entendu sur le reste, et c'est exactement ce que fait Fatoumata avec la corde.",
       note:"C'est aussi ce qui distingue un texte d'opinion publiable d'un texte de colère. Le courrier des lecteurs publie le premier."},

      {t:'ana', h:"Bien que · quoique + subjonctif",
       p:"Les deux concessives les plus employées, et elles demandent toujours le subjonctif.",
       mots:[['On dit',"Bien que la corde soit attachée, c'est elle qui l'a remise à l'eau."],['On dit',"Quoiqu'il ait raison sur ce point, sa lecture explique moins.",true],['La règle','subjonctif, sans exception']],
       say:"Bien que la corde soit attachée, c'est elle qui l'a remise à l'eau.",
       note:"« Quoique » en un mot signifie « bien que ». « Quoi que » en deux mots signifie « peu importe ce que ». Deux mots différents."},

      {t:'ana', h:"Même si + indicatif",
       p:"Le piège du couple : deux tournures voisines, deux modes opposés.",
       mots:[['Subjonctif',"Bien que vous ayez raison…"],['Indicatif',"Même si vous avez raison…",true],['Le repère','« même si » contient un « si », et « si » ne prend jamais le subjonctif']],
       say:"Même si vous avez raison sur la corde, il reste le téléphone.",
       note:"Le repère du « si » est fiable et vaut la peine d'être retenu : aucun « si » du français n'est suivi du subjonctif."},

      {t:'ana', h:"Opposer sans rien accorder",
       p:"En revanche, alors que, tandis que : ils mettent deux choses côte à côte sans concéder quoi que ce soit.",
       mots:[['En revanche',"La notaire porte la pièce ; en revanche, les cadets jouent trop fort."],['Alors que',"Le premier acte se passe en 1961, alors que le second se passe dix-neuf ans plus tard.",true],['La nuance','opposer n\'est pas concéder : rien n\'est accordé à personne']],
       say:"La notaire porte la pièce ; en revanche, les cadets jouent trop fort.",
       note:"« Par contre » est correct et courant au Québec ; « en revanche » est plus soutenu et convient mieux à une lettre publiée."},

      {t:'ana', h:"Certes… mais — la concession de l'écrit",
       p:"La forme la plus utile dans une lettre au courrier des lecteurs : deux mots, et votre texte cesse d'être un règlement de comptes.",
       mots:[['On écrit',"Certes, la salle n'était pas pleine, mais…"],['Variante',"Il est vrai que je n'ai pas vu la pièce ; cependant…",true],['L\'effet','le lecteur vous accorde la suite']],
       say:"Certes, la salle n'était pas pleine, mais ce n'est pas ce que vous reprochez à la pièce.",
       note:"Placez la concession en premier et votre point en second : c'est la seconde moitié que le lecteur retient."},

      {t:'labo', h:"Concéder ou opposer ?",
       p:"Choisissez ce que vous faites et le registre.",
       axes:[
         {id:'g', lbl:'Vous voulez…', opts:[['a','concéder puis avancer'],['b','opposer deux choses'],['c','concéder par écrit']]},
         {id:'r', lbl:'Quel exemple ?', opts:[['1','sur la télésérie'],['2','sur la critique']]}],
       out:{
         a1:{w:["Bien que la corde soit attachée, c'est elle qui l'a remise à l'eau."], say:"Bien que la corde soit attachée, c'est elle qui l'a remise à l'eau.", n:'bien que + subjonctif'},
         a2:{w:["Même si vous n'avez pas vu la pièce, vous pouvez lire le texte."], say:"Même si vous n'avez pas vu la pièce, vous pouvez lire le texte.", n:'même si + indicatif'},
         b1:{w:["Elle remet la chaloupe à l'eau ; en revanche, elle ne détache rien."], say:"Elle remet la chaloupe à l'eau ; en revanche, elle ne détache rien.", n:'deux faits côte à côte, rien d\'accordé'},
         b2:{w:["Il donne quatre faits, alors qu'il porte onze jugements."], say:"Il donne quatre faits, alors qu'il porte onze jugements.", n:'l\'opposition chiffrée, très efficace par écrit'},
         c1:{w:["Certes, la fin est abrupte, mais elle n'est pas manquante."], say:"Certes, la fin est abrupte, mais elle n'est pas manquante.", n:'la concession d\'ouverture'},
         c2:{w:["Il est vrai que je n'y étais pas ; cependant, votre texte se lit."], say:"Il est vrai que je n'y étais pas ; cependant, votre texte se lit.", n:'concession + connecteur soutenu'},
       },
       note:"Trois usages, six formules. Deux d'entre elles suffisent pour une lettre de deux cents mots."},

      {t:'ex', h:"Le connecteur · le mode",
       p:"À gauche, le connecteur. À droite, ce qui suit.",
       rows:[
         ["bien que","subjonctif"],
         ["quoique (en un mot)","subjonctif"],
         ["même si","indicatif"],
         ["alors que · tandis que","indicatif"],
         ["en revanche · par contre","une phrase entière"],
         ["malgré","un nom, jamais une phrase"],
       ]},

      {t:'piege', h:"Trois pièges de la concession",
       rows:[
         ["« malgré que la corde soit attachée »","« malgré la corde » ou « bien que la corde soit attachée »",
          "« Malgré » se met devant un nom. « Malgré que » est refusé à l'écrit soigné, même s'il s'entend souvent."],
         ["« bien que vous avez raison »","« bien que vous ayez raison »",
          "Bien que appelle le subjonctif, toujours. L'oreille propose l'indicatif parce que la phrase semble affirmer quelque chose."],
         ["concéder à la fin","concéder d'abord",
          "Une concession placée après votre argument l'annule. Placée avant, elle le prépare. L'ordre change tout, et il ne coûte rien."],
       ]},

      {t:'check', h:"Est-ce que c'est clair maintenant ?",
       p:"Quatre questions rapides.",
       qs:[
         {q:"« Bien que la corde ___ attachée… »", opts:["soit","est"], ok:0,
          fb:"Bien que + subjonctif, sans exception."},
         {q:"« Même si vous ___ raison… »", opts:["ayez","avez"], ok:1,
          fb:"Il y a un « si » : jamais de subjonctif après un « si »."},
         {q:"« Malgré » se met devant…", opts:["un nom","une phrase"], ok:0,
          fb:"Devant un nom. « Malgré que » ne se publie pas."},
         {q:"Dans une lettre, la concession se place…", opts:["avant votre argument","après votre argument"], ok:0,
          fb:"Avant : c'est la seconde moitié que le lecteur retient."},
       ]},

      {t:'revoir', h:"À retenir",
       p:"<b>Bien que · quoique</b> + subjonctif. <b>Même si</b> + indicatif — il y a un « si ». <b>En revanche · alors que</b> opposent sans concéder. <b>Certes… mais</b> ouvre un texte d'opinion. Et une règle d'ordre : la concession vient en premier, votre point en second."},
    ]
  },

  t3cit: {
    eye:'Mini-leçon', tit:"Citer, résumer, déformer",
    blocs:[
      {t:'texte', h:"Trois façons de rapporter, et une frontière",
       p:"Rapporter ce que quelqu'un a dit est une opération honnête ou malhonnête selon très peu de chose : un mot ajouté, une condition supprimée, un verbe changé. La frontière n'est pas morale, elle est technique — et le test tient en une phrase : <b>la personne citée pourrait-elle approuver votre version d'un signe de tête ?</b>",
       note:"Ce test vaut aussi pour vous-même. On déforme le plus souvent sans intention, en résumant trop vite."},

      {t:'ana', h:"Citer — les mots exacts, entre guillemets",
       p:"Deux-points, guillemets ouvrants, majuscule, guillemets fermants. On ne change pas un mot, pas même pour corriger une faute.",
       mots:[['La ponctuation',"Josyane a dit : « Une lecture se juge à ce qu'elle permet d'expliquer. »"],['Le point',"le point final se met à l'intérieur des guillemets",true],['La coupure',"trois points entre crochets pour ce qu'on retire"]],
       say:"Josyane a dit : une lecture se juge à ce qu'elle permet d'expliquer.",
       note:"En français, on emploie les guillemets français « » avec une espace à l'intérieur. Les guillemets droits sont tolérés, les italiques ne remplacent rien."},

      {t:'ana', h:"Résumer — d'autres mots, la même chose",
       p:"Aucun guillemet, et une seule règle : la personne doit pouvoir approuver votre phrase.",
       mots:[['Elle a dit',"Une lecture se juge à ce qu'elle permet d'expliquer."],['On résume',"Selon Josyane, une lecture vaut par le nombre de détails dont elle rend compte.",true],['Le test','elle approuve d\'un signe de tête']],
       say:"Selon Josyane, une lecture vaut par le nombre de détails dont elle rend compte.",
       note:"Le résumé est plus difficile que la citation, et beaucoup plus utile : il montre que vous avez compris."},

      {t:'ana', h:"Déformer — trois marques à connaître",
       p:"Généraliser un cas particulier, supprimer une condition, changer un verbe d'opinion en verbe de certitude.",
       mots:[['Généraliser',"« aucune lecture n'est meilleure » — elle a dit le contraire"],['Supprimer une condition',"on retire le « quand » ou le « si » qui limitait",true],['Durcir le verbe',"« il se peut que » devenu « il affirme que »"]],
       say:"Josyane prétend qu'aucune lecture n'est meilleure qu'une autre.",
       note:"L'ajout le plus courant est l'absolu : toujours, jamais, aucun, tout le monde. Ces mots-là entrent tout seuls dans un résumé pressé."},

      {t:'ana', h:"Le verbe introducteur pèse lourd",
       p:"Le verbe que vous choisissez juge celui que vous rapportez, avant même que le lecteur ait lu la citation.",
       mots:[['Neutres',"dit · écrit · explique · précise"],['Chargés',"prétend · avoue · admet · laisse entendre",true],['La règle','neutre quand vous voulez être cru']],
       say:"Il dit. Il explique. Il prétend. Il avoue.",
       note:"« Prétend » signale que vous ne le croyez pas ; « avoue » suppose qu'il y avait quelque chose à cacher. Employés sans le savoir, ils décrédibilisent votre propre texte."},

      {t:'labo', h:"La même parole, trois traitements",
       p:"Choisissez une personne et un traitement.",
       axes:[
         {id:'p', lbl:'Qui ?', opts:[['a','Josyane'],['b','Léandre'],['c','le critique']]},
         {id:'t', lbl:'On…', opts:[['1','cite'],['2','résume'],['3','déforme']]}],
       out:{
         a1:{w:["Josyane a dit : « Une lecture se juge à ce qu'elle permet d'expliquer. »"], say:"Josyane a dit : une lecture se juge à ce qu'elle permet d'expliquer.", n:'mots exacts, guillemets'},
         a2:{w:["Selon Josyane, une lecture vaut par ce qu'elle explique."], say:"Selon Josyane, une lecture vaut par ce qu'elle explique.", n:'autres mots, même contenu'},
         a3:{w:["Josyane prétend qu'aucune lecture n'est meilleure."], say:"Josyane prétend qu'aucune lecture n'est meilleure.", n:'généralisation + verbe chargé'},
         b1:{w:["Léandre a dit : « Six épisodes pour arriver à ça. »"], say:"Léandre a dit : six épisodes pour arriver à ça.", n:'la citation garde le ton'},
         b2:{w:["Léandre trouve la finale bâclée faute de temps."], say:"Léandre trouve la finale bâclée faute de temps.", n:'résumé fidèle, plus court'},
         b3:{w:["Léandre soutient que toute la série est ratée."], say:"Léandre soutient que toute la série est ratée.", n:'on étend la finale à la série entière'},
         c1:{w:["Il écrit : « Je n'ai pas pu le vérifier avant l'heure de tombée. »"], say:"Il écrit : je n'ai pas pu le vérifier avant l'heure de tombée.", n:'son aveu, mot pour mot'},
         c2:{w:["Le critique reconnaît ne pas avoir vérifié ce point."], say:"Le critique reconnaît ne pas avoir vérifié ce point.", n:'résumé fidèle'},
         c3:{w:["Le critique affirme que l'auteur a grandi dans une famille de terriens."], say:"Le critique affirme que l'auteur a grandi dans une famille de terriens.", n:'« on devine » devenu « affirme » : le doute a disparu'},
       },
       note:"Comparez les trois colonnes : rien n'est inventé dans la troisième. On a seulement retiré une nuance, et cela suffit."},

      {t:'ex', h:"Le verbe · ce qu'il ajoute",
       p:"À gauche, le verbe. À droite, ce qu'il fait entendre.",
       rows:[
         ["il dit · il écrit","rien : le verbe neutre"],
         ["il explique · il précise","il rend quelque chose plus clair"],
         ["il soutient","il maintient contre des objections"],
         ["il admet","la chose lui coûte"],
         ["il prétend","vous ne le croyez pas"],
         ["il avoue","il y avait quelque chose à cacher"],
       ]},

      {t:'piege', h:"Deux déformations qu'on commet sans le vouloir",
       rows:[
         ["« il n'aime pas la pièce »","« il reproche aux deux cadets de jouer trop fort »",
          "Étendre un reproche précis à l'ensemble de l'œuvre est la déformation la plus fréquente, et la plus difficile à voir en se relisant."],
         ["« il affirme que »","« il devine que »",
          "Changer un verbe de supposition en verbe de certitude supprime la seule précaution que l'autre avait prise. C'est ce qui rend un résumé injuste sans qu'un seul fait soit faux."],
       ]},

      {t:'check', h:"Est-ce que c'est clair maintenant ?",
       p:"Quatre questions rapides.",
       qs:[
         {q:"Le test d'un bon résumé, c'est que la personne citée…", opts:["ne réponde pas","puisse l'approuver d'un signe de tête"], ok:1,
          fb:"C'est la frontière entre résumer et déformer."},
         {q:"« Il prétend que » ajoute…", opts:["rien","que vous ne le croyez pas"], ok:1,
          fb:"Et cela se voit. Choisissez un verbe neutre quand vous voulez être cru."},
         {q:"La marque la plus fréquente d'une déformation est…", opts:["un mot absolu ajouté","une citation trop longue"], ok:0,
          fb:"Toujours, jamais, aucun, tout le monde : ils entrent tout seuls dans un résumé pressé."},
         {q:"Dans une citation, on peut corriger une faute de la personne ?", opts:["oui","non"], ok:1,
          fb:"Non. On cite exactement, ou on résume."},
       ]},

      {t:'revoir', h:"À retenir",
       p:"<b>Citer</b> : deux-points, guillemets, mots exacts. <b>Résumer</b> : d'autres mots, aucun guillemet, et la personne pourrait approuver. <b>Déformer</b> : un absolu ajouté, une condition supprimée, un verbe durci. Et surveillez le verbe introducteur : « prétend » et « avoue » jugent avant même la phrase."},
    ]
  },

};
