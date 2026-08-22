const PLUS = {

  // ════════════════════════════════════════════════════════════════════════
  prPhon: {
    eye:'Mini-leçon', tit:"Le son de « é » et le son de « è »",
    blocs:[
      {t:'texte', h:"Deux voyelles voisines, et la moitié du bulletin",
       p:"Comptez-les dans une seule météo : météo, prévisions, éclaircie, été, degré, gelée, reporter, annuler d'un côté ; tempête, averse, neige, grêle, veille, avertissement, verglas de l'autre. Les deux sons se font au même endroit de la bouche, à quelques millimètres près : c'est l'ouverture de la mâchoire qui les sépare, et rien d'autre. C'est pour ça qu'ils s'apprennent ensemble et jamais séparément.",
       note:"Beaucoup de langues n'ont qu'un seul son entre les deux. Si c'est votre cas, votre oreille entend d'abord « la même voyelle deux fois » — c'est normal, et ça se corrige en quelques semaines par le geste, pas par l'écoute."},

      {t:'ana', h:"Le son de « é » : la bouche presque fermée",
       p:"Les lèvres s'étirent sur les côtés comme pour un petit sourire, la mâchoire reste haute, le son est tendu et clair. Quatre orthographes, un seul son : é, er à la fin d'un verbe, ez, et parfois es.",
       mots:[["Dans le bulletin","la météo · les prévisions · une éclaircie · un degré"],["Dans les verbes du module","reporter · annuler · apportez · prévoyez",true],["Dans les saisons","l'été · une gelée · janvier · février"]],
       say:"La météo. Les prévisions. Une éclaircie. L'été.",
       note:"Le « er » final d'un infinitif se dit toujours « é » : reporter, annuler, apporter. Le r ne s'entend pas du tout, et c'est déroutant quand on vient d'une langue où toutes les lettres se prononcent."},

      {t:'ana', h:"Le son de « è » : la mâchoire descend",
       p:"La bouche s'ouvre franchement, la langue est plus basse, le son est plus grave et plus long. On l'écrit è, ê, ai, ei, ou simplement e devant deux consonnes.",
       mots:[["Le mauvais temps","la tempête · une averse · la neige · la grêle"],["Les mots de l'avis","une veille · un avertissement · le verglas",true],["Les petits mots qui reviennent","après · très · mais · jamais"]],
       say:"La tempête. Une averse. La neige. Une veille.",
       note:"« Avertissement » est le mot le plus important du module et il commence par un « è » : a-VER-tis-se-ment. Dites-le en ouvrant bien la deuxième syllabe, sinon il sonne comme « avéritissement »."},

      {t:'ana', h:"La paire qui change une décision",
       p:"Le futur et le conditionnel des verbes en -er ne se distinguent qu'à la voyelle finale : « é » pour le futur, « è » pour le conditionnel.",
       mots:[["Ce qui est décidé","je reporterai · j'annulerai · je confirmerai"],["Ce qui ne l'est pas encore","je reporterais · j'annulerais · je confirmerais",true],["La paire à dire dix fois","je reporterai / je reporterais"]],
       say:"Je reporterai. Je reporterais. Je confirmerai. Je confirmerais.",
       note:"Devant trente personnes qui attendent, ce n'est pas une nuance de prononciation : c'est la différence entre une décision prise et une décision envisagée. Beaucoup de francophones eux-mêmes ne la font plus ; faites-la, elle vous rendra service."},

      {t:'labo', h:"Écoutez la paire, puis le mot dans sa phrase",
       p:"Choisissez une paire et écoutez la différence, puis le mot replacé dans une phrase du module.",
       axes:[{id:'p', lbl:'Quelle paire ?', opts:[
         ['a','l\'été / la tempête'],
         ['b','une gelée / la grêle'],
         ['c','les prévisions / la veille'],
         ['d','je reporterai / je reporterais'],
         ['e','les quatre à la suite']]}],
       out:{
         a:{w:['une éclaircie'], say:"L'été. La tempête. En été, une tempête ne dure jamais longtemps.", n:"bouche fermée, puis bouche ouverte"},
         b:{w:['une éclaircie'], say:"Une gelée. La grêle. Une gelée au sol, de la grêle dans l'air.", n:"le même début, deux voyelles différentes"},
         c:{w:['les prévisions','une veille'], say:"Les prévisions. La veille. Les prévisions de la veille avaient changé.", n:"« é » tendu, puis « è » ouvert"},
         d:{w:['reporter'], say:"Je reporterai. Je reporterais. Je reporterai la sortie au vingt-deux.", n:"la paire qui dit si c'est décidé ou non"},
         e:{w:['une veille','les prévisions'], say:"L'été, la tempête. Une gelée, la grêle. Les prévisions, la veille. Je reporterai, je reporterais.", n:"quatre paires sans reprendre son souffle"},
       },
       note:"Écoutez chaque paire deux fois : la première pour entendre les deux mots, la seconde en ne surveillant que la position de votre propre mâchoire."},

      {t:'ex', h:"À écouter et à répéter",
       p:"Six phrases prises dans les bulletins du module.",
       rows:[
         ["Les prévisions annoncent une éclaircie en fin d'après-midi.","« é » quatre fois de suite"],
         ["La tempête laissera trente centimètres de neige.","« è » au début, « è » à la fin"],
         ["Un avertissement de pluie verglaçante est en vigueur.","le mot le plus important du module"],
         ["Je vous confirmerai vendredi à midi.","futur : la dernière voyelle est fermée"],
         ["Je reporterais volontiers, mais ce n'est pas décidé.","conditionnel : la dernière voyelle est ouverte"],
         ["En été, un indice UV de neuf brûle une peau en une heure.","« é » deux fois, puis « è » dans « neuf »"],
       ]},

      {t:'piege', h:"Trois pièges des deux « e »",
       rows:[
         ["dire « è » à la fin d'un infinitif","« reportèr », « annulèr », avec le r qui s'entend",
          "Le « er » final d'un verbe se dit « é » et le r ne s'entend jamais : reporter se dit « report-é ». C'est vrai de tous les infinitifs du premier groupe, sans exception."],
         ["fermer le « è » de « avertissement »","« avéritissement », « avértissement »",
          "La deuxième syllabe est ouverte : a-VER-tis-se-ment, comme dans « hiver ». Ce mot revient trente fois dans le module ; le dire juste une fois pour toutes vaut la peine."],
         ["croire que l'accent écrit décide tout","« neige », « veille », « après » lus avec un « é »",
          "Beaucoup de « è » ne portent aucun accent : neige, veille, verglas, avertissement, après. C'est l'oreille qui commande, pas l'orthographe. Fiez-vous à la règle du e devant deux consonnes."],
       ]},

      {t:'check', h:"Est-ce que c'est clair maintenant ?",
       p:"Quatre questions rapides.",
       qs:[
         {q:"Dans « une éclaircie », la bouche est…", opts:["presque fermée","grande ouverte"], ok:0,
          fb:"Presque fermée, les lèvres étirées : c'est le geste du son de « é »."},
         {q:"« Reporter » à l'infinitif finit par…", opts:["le son de « é »","le son de « è » avec un r"], ok:0,
          fb:"Le son de « é ». Le r final d'un infinitif ne s'entend jamais."},
         {q:"« Je reporterais » est…", opts:["un futur, c'est décidé","un conditionnel, ce n'est pas décidé"], ok:1,
          fb:"Un conditionnel. La voyelle finale est ouverte : ce n'est pas encore décidé."},
         {q:"« Avertissement » contient…", opts:["seulement des « é »","un « è » dans la deuxième syllabe"], ok:1,
          fb:"Un « è » : a-VER-tis-se-ment, comme dans « hiver »."},
       ]},
    ]
  },

  // ════════════════════════════════════════════════════════════════════════
  prAvis: {
    eye:'Mini-leçon', tit:"Veille, avertissement, bulletin spécial",
    blocs:[
      {t:'texte', h:"Trois mots, trois degrés de certitude",
       p:"Environnement Canada n'emploie pas ces trois mots au hasard : ils forment une échelle. Le bulletin météorologique spécial dit qu'un temps inhabituel s'en vient sans qu'on sache encore lequel. La veille dit que les conditions sont favorables et que le phénomène est possible. L'avertissement dit qu'il est imminent, ou qu'il a déjà commencé. On ne décide pas de la même façon devant les trois, et c'est exactement ce que ce module travaille.",
       note:"Ces trois mots sont les vrais, ceux du service. Ce ne sont pas des synonymes de journalistes : la télévision les mélange souvent, le service, jamais."},

      {t:'ana', h:"Le bulletin météorologique spécial — « attention, ça s'en vient »",
       p:"Le plus faible des trois. Il attire l'attention sur un temps qui sort de l'ordinaire, sans donner encore de quantité ni de certitude. Il précède souvent une veille de vingt-quatre heures.",
       mots:[["Ce qu'il dit","un temps inhabituel est possible dans les prochains jours"],["Ce qu'on fait","on lit, on note la date, on attend la suite",true],["Ce qu'on ne fait pas","on n'annule rien, on ne prévient personne"]],
       say:"Un bulletin météorologique spécial a été émis pour le Bas-Saint-Laurent.",
       note:"Beaucoup de gens réagissent trop fort à celui-là parce qu'il porte le mot « spécial ». C'est le plus faible des trois avis, pas le plus fort."},

      {t:'ana', h:"La veille — « c'est possible »",
       p:"Les conditions sont favorables : le phénomène peut se produire. Une veille est émise d'avance, parfois deux jours avant, et elle peut être levée sans que rien ne se produise.",
       mots:[["Ce qu'elle dit","les conditions sont favorables · le phénomène est possible"],["Ce qu'on fait","on surveille, on prépare un plan B, on annonce quand on décidera",true],["Le mot qui va avec","une veille de tempête hivernale · une veille d'orages violents"]],
       say:"Une veille de tempête hivernale a été émise pour le Bas-Saint-Laurent.",
       note:"C'est devant une veille qu'on dit la phrase la plus utile du module : « Je vous confirme vendredi à midi. » Elle ne décide rien et elle règle tout."},

      {t:'ana', h:"L'avertissement — « c'est imminent, ou c'est commencé »",
       p:"Le phénomène est sur le point de se produire ou il est déjà en cours. C'est le mot qui fait décider. Une veille devient souvent un avertissement quelques heures avant.",
       mots:[["Ce qu'il dit","le phénomène est imminent ou en cours · en vigueur jusqu'à…"],["Ce qu'on fait","on décide, on écrit au groupe, on téléphone aux personnes seules",true],["Les intitulés réels","avertissement de pluie verglaçante · de tempête hivernale · de chaleur extrême · de froid extrême"]],
       say:"Un avertissement de pluie verglaçante est en vigueur pour le Bas-Saint-Laurent.",
       note:"Guettez le changement de mot sur votre téléphone : quand « veille » devient « avertissement », ce n'est pas une répétition de l'alerte, c'est une information neuve."},

      {t:'labo', h:"Le même phénomène, trois avis",
       p:"Choisissez un avis et écoutez comment le service l'annonce, puis ce que ça change pour vous.",
       axes:[{id:'a', lbl:'Quel avis ?', opts:[
         ['a','Bulletin météorologique spécial'],
         ['b','Veille'],
         ['c','Avertissement'],
         ['d','Avertissement levé'],
         ['e','Les quatre à la suite']]}],
       out:{
         a:{w:['les prévisions'], say:"Bulletin météorologique spécial : un temps inhabituel est possible en fin de semaine.", n:"on lit, on note la date, on attend"},
         b:{w:['une veille'], say:"Veille de tempête hivernale pour le Bas-Saint-Laurent, en vigueur pour samedi.", n:"on surveille et on annonce quand on décidera"},
         c:{w:['un avertissement'], say:"Avertissement de pluie verglaçante pour le Bas-Saint-Laurent, en vigueur jusqu'à samedi matin.", n:"on décide, et on prévient le groupe"},
         d:{w:['un avertissement','une éclaircie'], say:"L'avertissement de pluie verglaçante a été levé. Quelques éclaircies sont prévues en après-midi.", n:"c'est fini : on peut maintenir"},
         e:{w:['une veille','un avertissement'], say:"Bulletin spécial. Veille de tempête hivernale. Avertissement de pluie verglaçante. Avertissement levé.", n:"l'échelle entière, du plus faible au plus fort"},
       },
       note:"Le quatrième, « levé », est celui qu'on oublie d'attendre. Beaucoup de gens annulent une activité pour un avertissement qui a été retiré la veille au soir."},

      {t:'ex', h:"À écouter et à répéter",
       p:"Six phrases de la langue des avis.",
       rows:[
         ["Un avertissement de pluie verglaçante a été émis cet après-midi.","« émis » : le verbe des avis"],
         ["L'avis est en vigueur jusqu'à samedi matin.","« en vigueur » : c'est encore vrai maintenant"],
         ["La veille a été levée en fin de soirée.","« levée » : c'est fini"],
         ["Les prévisions ont changé trois fois dans la même journée.","et ce n'est pas une erreur du service"],
         ["Je vous confirme vendredi à midi.","la phrase à dire devant une veille"],
         ["Quelques éclaircies sont prévues en fin d'après-midi.","la bonne nouvelle du bulletin"],
       ]},

      {t:'piege', h:"Trois pièges des avis météo",
       rows:[
         ["confondre veille et avertissement","annuler une sortie pour une veille émise deux jours avant",
          "Une veille dit « possible », pas « certain ». Elle est parfois levée sans que rien ne se produise. Devant une veille, on prépare et on annonce quand on décidera — on ne décide pas."],
         ["oublier de regarder la région","annuler à Rimouski pour une tempête annoncée en Gaspésie",
          "Le Québec est découpé en régions de prévision et le bulletin les nomme. Apprenez le nom de la vôtre — ici, le Bas-Saint-Laurent — et guettez-le. C'est la moitié des annulations inutiles."],
         ["croire que l'effet finit avec le phénomène","« la pluie verglaçante s'arrête à huit heures, donc à midi c'est correct »",
          "La glace reste au sol des heures après la dernière goutte. Posez-vous la question au moment exact de votre activité, pas au moment du phénomène. C'est la faute de raisonnement la plus coûteuse du module."],
       ]},

      {t:'check', h:"Est-ce que c'est clair maintenant ?",
       p:"Quatre questions rapides.",
       qs:[
         {q:"Le plus fort des trois avis, c'est…", opts:["le bulletin météorologique spécial","l'avertissement"], ok:1,
          fb:"L'avertissement : le phénomène est imminent ou déjà commencé."},
         {q:"Une veille veut dire que le phénomène est…", opts:["possible","certain"], ok:0,
          fb:"Possible. Les conditions sont favorables, rien de plus."},
         {q:"« En vigueur » veut dire…", opts:["que l'avis compte encore maintenant","que l'avis a été retiré"], ok:0,
          fb:"Que l'avis compte encore. Quand il est retiré, on dit qu'il est levé."},
         {q:"Devant une veille émise deux jours avant, on…", opts:["annule tout de suite","annonce quand on décidera"], ok:1,
          fb:"On annonce quand on décidera. Les prévisions changeront d'ici là."},
       ]},
    ]
  },

  // ════════════════════════════════════════════════════════════════════════
  t1fut: {
    eye:'Mini-leçon', tit:"Le futur simple, la langue de la prévision",
    blocs:[
      {t:'texte', h:"Un bulletin ne parle jamais du présent",
       p:"Écoutez n'importe quelle météo : tous les verbes sont au futur. La pluie débutera, les trottoirs deviendront glissants, le mercure remontera, une amélioration sera possible. C'est la marque du genre — on annonce ce qui n'est pas encore arrivé. Et comme ce module vous demande de redire le bulletin à quelqu'un d'autre, puis d'annoncer votre propre décision, le futur simple est le temps que vous emploierez le plus.",
       note:"Le futur simple est aussi le temps de la promesse : « je vous confirmerai vendredi » n'annonce pas la météo, il engage celui qui parle. Devant un groupe qui attend, c'est ce qui rassure."},

      {t:'ana', h:"La formation : l'infinitif, puis six terminaisons",
       p:"On garde l'infinitif entier et on ajoute -ai, -as, -a, -ons, -ez, -ont. Pour les verbes en -re, on enlève seulement le e final.",
       mots:[["Verbes en -er","tomber → il tombera · neiger → il neigera · durer → ça durera"],["Verbes en -ir","finir → ça finira · partir → nous partirons",true],["Verbes en -re","descendre → le mercure descendra · rendre → ça rendra"]],
       say:"Il tombera. Il neigera. Nous partirons. Le mercure descendra.",
       note:"Toutes les personnes gardent le même radical : c'est le temps le plus régulier du français. Ce qui se travaille, ce n'est pas la règle, ce sont les six ou sept verbes irréguliers du bloc suivant."},

      {t:'ana', h:"Les sept irréguliers dont vous aurez besoin",
       p:"Ils ne s'apprennent pas par règle mais par cœur, et ce sont exactement ceux du bulletin météo.",
       mots:[["Les quatre premiers","être → il sera · avoir → il y aura · faire → il fera · aller → ça ira"],["Les trois autres","pouvoir → on pourra · falloir → il faudra · venir → il viendra",true],["Dans une phrase du module","Il fera moins douze et il y aura de la poudrerie."]],
       say:"Il sera. Il y aura. Il fera. Il faudra. On pourra.",
       note:"Cinq de ces sept verbes sont impersonnels dans le bulletin : il sera, il y aura, il fera, il faudra, il viendra. Vous n'aurez presque jamais à les conjuguer à une autre personne."},

      {t:'ana', h:"Le si de condition ne prend jamais le futur",
       p:"Après « si », on met le présent, et le futur va dans l'autre moitié de la phrase. C'est la faute la plus fréquente à ce niveau, et elle s'entend tout de suite.",
       mots:[["Juste","Si l'avertissement est levé, nous maintiendrons la sortie."],["Juste aussi","Nous maintiendrons la sortie si l'avertissement est levé.",true],["Faux","Si l'avertissement sera levé, nous maintiendrons la sortie."]],
       say:"Si l'avertissement est levé, nous maintiendrons la sortie.",
       note:"L'ordre des deux moitiés est libre : ce qui compte, c'est que le verbe collé à « si » soit au présent. Retenez la phrase entière plutôt que la règle."},

      {t:'labo', h:"La même prévision, quatre verbes",
       p:"Choisissez un verbe et écoutez la phrase du bulletin qui l'emploie.",
       axes:[{id:'v', lbl:'Quel verbe ?', opts:[
         ['a','débuter'],
         ['b','devenir'],
         ['c','faire'],
         ['d','y avoir'],
         ['e','les quatre à la suite']]}],
       out:{
         a:{w:['la pluie verglaçante'], say:"La pluie verglaçante débutera vendredi en soirée.", n:"verbe en -er : l'infinitif entier, plus -a"},
         b:{w:['la pluie verglaçante'], say:"Les trottoirs deviendront très glissants pendant la nuit.", n:"irrégulier : deviendront, pas devenirent"},
         c:{w:['le refroidissement éolien'], say:"Il fera moins douze demain matin, avec un fort refroidissement éolien.", n:"faire → il fera, à apprendre par cœur"},
         d:{w:['la poudrerie'], say:"Il y aura de la poudrerie sur la route en soirée.", n:"avoir → il y aura, le plus fréquent de tous"},
         e:{w:['la pluie verglaçante','la poudrerie'], say:"La pluie débutera. Les trottoirs deviendront glissants. Il fera moins douze. Il y aura de la poudrerie.", n:"un bulletin entier en quatre verbes"},
       },
       note:"Dites-les à voix haute en gardant la même intonation descendante que l'annonceur : le bulletin est lu, pas raconté, et cette platitude-là s'imite très bien."},

      {t:'ex', h:"À écouter et à répéter",
       p:"Six phrases au futur, du bulletin au message au groupe.",
       rows:[
         ["La pluie verglaçante débutera vendredi en soirée.","le futur de l'annonce"],
         ["Elle se poursuivra jusqu'à samedi matin.","verbe pronominal, même terminaison"],
         ["Il tombera de trois à cinq millimètres de glace.","impersonnel et futur ensemble"],
         ["Je vous confirmerai vendredi à midi.","le futur de la promesse"],
         ["La sortie aura lieu le samedi vingt-deux, à treize heures.","le futur de l'avis affiché"],
         ["Si l'avertissement est levé, nous maintiendrons la sortie.","présent après « si », futur après la virgule"],
       ]},

      {t:'piege', h:"Trois pièges du futur simple",
       rows:[
         ["mettre le futur après « si »","« si il fera froid », « si l'avis sera levé »",
          "Après « si » de condition, présent obligatoire : « s'il fait froid », « si l'avis est levé ». Le futur va dans l'autre moitié de la phrase."],
         ["oublier le e des verbes en -ier et -yer","« il pluvra », « nous prévoirons » mal formés",
          "Certains verbes gardent une lettre qu'on n'entend presque pas : « il pleuvra », « vous prévoirez ». Écrivez-les une fois correctement et relisez-les : c'est une faute d'écrit, pas d'oral."],
         ["employer le futur pour une décision prise","« la sortie sera reportée » quand c'est déjà décidé",
          "Pour une décision arrêtée, le présent est plus ferme : « la sortie est reportée ». Le futur laisse entendre qu'on pourrait encore changer d'idée, et trente personnes le sentiront."],
       ]},

      {t:'check', h:"Est-ce que c'est clair maintenant ?",
       p:"Quatre questions rapides.",
       qs:[
         {q:"Le futur de « faire », c'est…", opts:["il fera","il faisera"], ok:0,
          fb:"Il fera. C'est l'un des sept irréguliers à savoir par cœur."},
         {q:"Après « si » de condition, on met…", opts:["le futur","le présent"], ok:1,
          fb:"Le présent : « si l'avertissement est levé »."},
         {q:"Pour une décision déjà prise, on préfère…", opts:["le présent","le futur"], ok:0,
          fb:"Le présent : « la sortie est reportée » est plus ferme."},
         {q:"« Il y aura » est le futur de…", opts:["il y a","il est"], ok:0,
          fb:"De « il y a ». C'est la tournure la plus fréquente du bulletin."},
       ]},
    ]
  },

  // ════════════════════════════════════════════════════════════════════════
  t1imp: {
    eye:'Mini-leçon', tit:"Le « il » qui ne désigne personne",
    blocs:[
      {t:'texte', h:"Une phrase qui n'a pas de vrai sujet",
       p:"« Il pleut. » Qui, il ? Personne. Ce « il » ne remplace aucun nom : il est là parce qu'un verbe conjugué, en français, a besoin d'un sujet devant lui. C'est la forme normale pour parler du temps qu'il fait, et beaucoup de langues s'en passent — on dit simplement « pleut », ou « est en train de pleuvoir ». D'où la faute très fréquente, et très visible, qui consiste à laisser tomber le « il ».",
       note:"On appelle ça une phrase impersonnelle. Le mot fait peur ; la chose est simple : un sujet obligatoire qui ne désigne rien du tout."},

      {t:'ana', h:"La famille météo",
       p:"Une poignée de verbes ne s'emploient qu'à cette forme. Ce sont ceux du bulletin, et il n'y en a pas beaucoup.",
       mots:[["Les verbes purs","il pleut · il neige · il vente · il grêle · il gèle"],["Avec « faire » et un adjectif","il fait froid · il fait moins douze · il fait beau",true],["Avec le vrai sujet rejeté derrière","il tombera trente centimètres de neige"]],
       say:"Il pleut. Il neige. Il vente. Il fait moins douze.",
       note:"La dernière forme est la plus utile et la moins connue : « il tombera trente centimètres de neige ». On pourrait dire « trente centimètres de neige tomberont », mais personne ne parle comme ça."},

      {t:'ana', h:"Il y a — l'existence toute nue",
       p:"La tournure la plus fréquente du français parlé, et elle est impersonnelle elle aussi. Elle sert à dire qu'une chose existe, sans dire à qui elle appartient ni d'où elle vient.",
       mots:[["Au présent","il y a un avertissement en vigueur · il y a de la glace au sol"],["Au futur","il y aura de la poudrerie · il y aura du vent toute la nuit",true],["Au passé","il y a eu une bordée de neige cette nuit"]],
       say:"Il y a un avertissement en vigueur. Il y aura de la poudrerie en soirée.",
       note:"« Il y a » ne s'accorde jamais : il y a une personne, il y a trente personnes. C'est un des rares endroits du français où l'on ne se pose aucune question d'accord."},

      {t:'ana', h:"Il faut, et il est possible que",
       p:"Deux formules impersonnelles qui ne parlent plus du temps mais de ce qu'on doit faire, et de ce qui pourrait arriver.",
       mots:[["L'obligation sans personne nommée","il faut apporter des crampons · il faudra partir plus tôt"],["La possibilité, avec le subjonctif","il est possible que la sortie soit reportée",true],["Les voisines","il est important que · il vaut mieux · il se peut que"]],
       say:"Il faut apporter des crampons. Il est possible que la sortie soit reportée.",
       note:"« Il faut » est plus doux qu'un ordre parce qu'il ne dit pas à qui l'obligation s'adresse. Devant un groupe, « il faut apporter » passe beaucoup mieux que « vous devez apporter »."},

      {t:'labo', h:"La même journée, cinq phrases impersonnelles",
       p:"Choisissez une tournure et écoutez-la dans une phrase du module.",
       axes:[{id:'i', lbl:'Quelle tournure ?', opts:[
         ['a','il + verbe de météo'],
         ['b','il fait + température'],
         ['c','il y a / il y aura'],
         ['d','il faut / il faudra'],
         ['e','il est possible que']]}],
       out:{
         a:{w:['une bordée de neige'], say:"Il neige depuis minuit : il est tombé vingt centimètres.", n:"le verbe pur, sans autre sujet possible"},
         b:{w:['le refroidissement éolien'], say:"Il fera moins douze demain, avec un refroidissement éolien de moins vingt-deux.", n:"faire + la température"},
         c:{w:['la poudrerie'], say:"Il y aura de la poudrerie sur la route en soirée.", n:"l'existence pure, au futur"},
         d:{w:['des crampons'], say:"Il faudra apporter des crampons : les trottoirs seront glacés.", n:"l'obligation sans personne nommée"},
         e:{w:['une veille','reporter'], say:"Il est possible que la sortie soit reportée ; je vous confirme vendredi.", n:"la phrase de la veille météo, avec le subjonctif"},
       },
       note:"Les cinq couvrent tout ce que ce module vous demandera de dire sur le temps. Apprenez-les comme cinq formules, pas comme cinq règles."},

      {t:'ex', h:"À écouter et à répéter",
       p:"Six phrases impersonnelles du module.",
       rows:[
         ["Il fera moins douze demain matin.","température : faire + le chiffre"],
         ["Il tombera de trois à cinq millimètres de glace.","le vrai sujet passe derrière"],
         ["Il y aura de la poudrerie sur la route 132.","existence, au futur"],
         ["Il ventera fort toute la nuit.","verbe pur, comme neiger"],
         ["Il faut apporter des crampons.","obligation sans personne nommée"],
         ["Il est possible que la sortie soit reportée.","possibilité, verbe au subjonctif"],
       ]},

      {t:'piege', h:"Trois pièges de la phrase impersonnelle",
       rows:[
         ["laisser tomber le « il »","« fait froid dehors », « pleut depuis ce matin »",
          "Le sujet est obligatoire même quand il ne désigne rien. « Il fait froid », « il pleut ». C'est la faute la plus visible du niveau, et la plus vite corrigée."],
         ["accorder « il y a »","« il y ont trente personnes », « ils y a du vent »",
          "« Il y a » ne bouge jamais, quel que soit le nombre : il y a une personne, il y a trente personnes. Un seul bloc, trois petits mots, aucune variation."],
         ["mettre l'indicatif après « il est possible que »","« il est possible que la sortie est reportée »",
          "Après « il est possible que », le subjonctif : « soit reportée ». Apprenez la formule entière — il est possible que… soit — plutôt que la règle du subjonctif."],
       ]},

      {t:'check', h:"Est-ce que c'est clair maintenant ?",
       p:"Quatre questions rapides.",
       qs:[
         {q:"Dans « il neige », le mot « il » désigne…", opts:["le ciel","personne du tout"], ok:1,
          fb:"Personne. Il est là uniquement parce qu'un verbe conjugué a besoin d'un sujet."},
         {q:"Au futur, « il y a » devient…", opts:["il y aura","ils y auront"], ok:0,
          fb:"Il y aura. La tournure ne s'accorde jamais."},
         {q:"Après « il est possible que », le verbe se met…", opts:["à l'indicatif","au subjonctif"], ok:1,
          fb:"Au subjonctif : « il est possible que la sortie soit reportée »."},
         {q:"Devant un groupe, « il faut apporter » est…", opts:["plus doux que « vous devez apporter »","plus sec que « vous devez apporter »"], ok:0,
          fb:"Plus doux : l'obligation n'est adressée à personne en particulier."},
       ]},
    ]
  },

  // ════════════════════════════════════════════════════════════════════════
  t2dec: {
    eye:'Mini-leçon', tit:"Maintenir, reporter, annuler",
    blocs:[
      {t:'texte', h:"Trois verbes, trois messages complètement différents",
       p:"C'est le cœur du module, et ce n'est pas de la grammaire : c'est du vocabulaire qui engage. Maintenir, c'est dire que l'activité a lieu comme prévu. Reporter, c'est la déplacer à une autre date. Annuler, c'est dire qu'elle n'aura pas lieu du tout. Employer l'un pour l'autre déclenche vingt téléphones, et fait manquer une sortie à des gens qui l'attendaient depuis un mois.",
       note:"Les trois se disent aussi de soi : « je maintiens ma décision », « je reporte mon rendez-vous », « j'annule ma commande ». Ce que vous apprenez ici sert bien au-delà des sorties de groupe."},

      {t:'ana', h:"Maintenir — l'activité a lieu comme prévu",
       p:"On maintient quand l'avis ne touche pas le créneau, quand l'effet est faible, ou quand l'activité se passe à l'intérieur. Maintenir n'est pas ne rien faire : il faut le dire, sinon la moitié du groupe reste chez elle.",
       mots:[["Comment ça se dit","la sortie est maintenue · l'activité a lieu comme prévu"],["Avec un changement","elle est maintenue, mais nous partirons à neuf heures",true],["Ce qu'on ajoute","habillez-vous chaudement · apportez vos crampons"]],
       say:"La sortie est maintenue : nous partirons à neuf heures comme prévu.",
       note:"Un maintien s'annonce aussi clairement qu'une annulation. Le silence n'est pas un maintien : dans le doute, les gens restent chez eux."},

      {t:'ana', h:"Reporter — même activité, autre date",
       p:"On reporte quand une date de rechange existe. C'est la décision la plus fréquente et la mieux acceptée : personne ne perd rien, on attend deux semaines.",
       mots:[["Comment ça se dit","la sortie est reportée au samedi vingt-deux"],["Ce qu'il faut toujours ajouter","même heure, même endroit · le rendez-vous ne change pas",true],["La formule complète","reportée au 22 février, à treize heures, devant le Centre"]],
       say:"La sortie est reportée au samedi vingt-deux février, à treize heures, devant le Centre.",
       note:"« Reportée » sans nouvelle date ne règle rien. Une décision incomplète crée plus d'appels qu'un silence : donnez la date dans la même phrase."},

      {t:'ana', h:"Annuler — l'activité n'aura pas lieu",
       p:"On annule quand il n'existe pas de date de rechange : un spectacle qui passe une seule fois, un autobus déjà payé, un guide qui ne revient pas, une saison qui se termine.",
       mots:[["Comment ça se dit","l'activité est annulée · elle n'aura pas lieu"],["Ce qu'on ajoute toujours","la raison, et ce qui arrive à l'argent s'il y en a",true],["Ce qu'on ne dit pas","« on verra plus tard » — c'est un report qui n'ose pas dire son nom"]],
       say:"Le spectacle de samedi est annulé : la chorale ne repasse pas cette saison.",
       note:"Annuler coûte plus cher en déception que reporter. Dites-le plus tôt, dites la raison, et dites-la en une seule phrase claire."},

      {t:'labo', h:"La même semaine, quatre décisions",
       p:"Choisissez une situation et écoutez la décision, avec sa raison.",
       axes:[{id:'d', lbl:'Quelle situation ?', opts:[
         ['a','Verglas, marche reportable'],
         ['b','Ciel gris, atelier à l\'intérieur'],
         ['c','Tempête, spectacle unique'],
         ['d','Chaleur extrême, on change l\'heure'],
         ['e','Les quatre à la suite']]}],
       out:{
         a:{w:['reporter','la pluie verglaçante'], say:"Comme un avertissement de pluie verglaçante est en vigueur, la marche est reportée au samedi vingt-deux.", n:"une date de rechange existe : on reporte"},
         b:{w:['un avertissement'], say:"L'atelier de cuisine est maintenu : il a lieu à l'intérieur, au Centre.", n:"l'avis ne touche pas l'activité : on maintient"},
         c:{w:['annuler'], say:"Le spectacle de la chorale est annulé : il passait seulement samedi soir.", n:"aucune date de rechange : on annule"},
         d:{w:['la chaleur extrême'], say:"La pétanque est maintenue, mais elle est déplacée à neuf heures du matin.", n:"on change l'heure plutôt que la date"},
         e:{w:['reporter','annuler'], say:"La marche est reportée. L'atelier est maintenu. Le spectacle est annulé. La pétanque est déplacée à neuf heures.", n:"les quatre décisions du module"},
       },
       note:"La quatrième est celle qu'on oublie : déplacer l'heure ou le lieu au lieu de toucher à la date. C'est souvent la meilleure décision de la liste."},

      {t:'ex', h:"À écouter et à répéter",
       p:"Six annonces de décision, entières.",
       rows:[
         ["La sortie est maintenue : nous partons à treize heures comme prévu.","maintien, avec l'heure rappelée"],
         ["La sortie est reportée au samedi vingt-deux, même heure, même endroit.","report, avec la date complète"],
         ["Le spectacle est annulé : la chorale ne repasse pas cette saison.","annulation, avec la raison"],
         ["La marche est maintenue, mais nous irons au centre commercial.","maintien avec changement de lieu"],
         ["Si la nouvelle date ne vous convient pas, appelez-moi avant jeudi.","la ligne qui évite vingt appels"],
         ["Je vous confirme vendredi à midi.","la phrase à dire quand on n'a pas encore tranché"],
       ]},

      {t:'piege', h:"Trois pièges de la décision",
       rows:[
         ["dire « annulé » pour « reporté »","« la sortie est annulée » alors qu'elle est déplacée au 22",
          "Annulée veut dire qu'elle n'aura pas lieu, point. Vingt personnes ne se réinscriront pas, et trois seront fâchées quand elles apprendront qu'elle a eu lieu sans elles."],
         ["reporter sans donner de date","« on reporte, je vous reviens là-dessus »",
          "Une date, même provisoire, vaut mieux que rien : « reportée au 22, je confirme lundi ». Sans date, chacun invente la sienne et personne ne réserve son samedi."],
         ["décider trop tôt","annuler le mercredi pour une veille émise pour le samedi",
          "Les prévisions changeront d'ici là, et souvent dans le bon sens. Annoncez le moment de la décision, écoutez jusque-là, et tranchez à l'heure dite."],
       ]},

      {t:'check', h:"Est-ce que c'est clair maintenant ?",
       p:"Quatre questions rapides.",
       qs:[
         {q:"On reporte plutôt qu'on annule quand…", opts:["une date de rechange existe","la météo est très mauvaise"], ok:0,
          fb:"Quand une date de rechange existe. La météo dit qu'il ne faut pas y aller samedi ; le calendrier dit s'il y a un autre samedi."},
         {q:"Un maintien…", opts:["se dit, comme les autres décisions","n'a pas besoin d'être annoncé"], ok:0,
          fb:"Se dit. Sans message, la moitié du groupe reste chez elle au cas où."},
         {q:"« Reportée » sans nouvelle date…", opts:["suffit","crée plus d'appels qu'un silence"], ok:1,
          fb:"Crée plus d'appels. Donnez la date dans la même phrase."},
         {q:"Déplacer l'heure d'une activité, c'est…", opts:["une forme de maintien","une annulation"], ok:0,
          fb:"Une forme de maintien : l'activité a lieu, à un autre moment de la journée."},
       ]},
    ]
  },

  // ════════════════════════════════════════════════════════════════════════
  t2cause: {
    eye:'Mini-leçon', tit:"Dire pourquoi : six connecteurs de cause",
    blocs:[
      {t:'texte', h:"Une décision sans raison se fait discuter toute la semaine",
       p:"C'est la phrase de Réjean, et c'est vrai bien au-delà des sorties de groupe : les gens acceptent presque tout quand ils comprennent pourquoi. Le français a une demi-douzaine de façons de dire la cause, et elles ne se placent pas au même endroit dans la phrase. Choisir la bonne, c'est décider ce que le lecteur entendra en premier — la raison, ou la décision.",
       note:"Deux de ces six mots ne disent pas la cause mais la conséquence : « donc » et « c'est pourquoi ». On les range avec les autres parce qu'ils font le même travail, à l'envers."},

      {t:'ana', h:"Parce que — après la décision, toujours",
       p:"Le plus neutre et le plus courant. Il répond à la question « pourquoi ? » et il se place après ce qu'il explique. Devant une voyelle, il devient « parce qu' ».",
       mots:[["La forme normale","La sortie est reportée parce qu'un avertissement est en vigueur."],["En réponse à une question","— Pourquoi ? — Parce que les trottoirs seront glacés.",true],["Ce qu'il ne fait pas","il ne commence jamais une phrase, sauf en réponse"]],
       say:"La sortie est reportée parce qu'un avertissement de pluie verglaçante est en vigueur.",
       note:"Quand vous hésitez entre les six, prenez celui-là. Il n'est jamais faux, il n'est jamais bizarre, et il ne dit rien de plus que la cause."},

      {t:'ana', h:"Comme — en tête de phrase, jamais ailleurs",
       p:"Il met la raison avant la décision. On l'emploie quand on veut que l'autre comprenne la situation avant d'entendre ce qu'on a décidé — souvent une bonne idée devant un groupe.",
       mots:[["La forme","Comme les trottoirs seront glacés, la sortie est reportée."],["Ce qui est interdit","« La sortie est reportée comme les trottoirs seront glacés. »",true],["Son voisin plus lourd","Étant donné que les trottoirs seront glacés, …"]],
       say:"Comme les trottoirs seront glacés toute la journée, la sortie est reportée au vingt-deux.",
       note:"« Comme » en tête de phrase veut dire « parce que ». Ailleurs, il veut dire « de la même façon que » — deux mots identiques, deux emplois qui n'ont rien à voir."},

      {t:'ana', h:"Puisque et étant donné que — deux registres particuliers",
       p:"Puisque s'appuie sur une raison que l'autre connaît déjà. Étant donné que est la formule officielle de l'avis affiché et du courriel de service.",
       mots:[["Puisque — une raison partagée","Puisque vous avez tous reçu l'alerte, vous savez pourquoi j'écris."],["Étant donné que — l'écrit officiel","Étant donné qu'un avertissement est en vigueur, l'activité est reportée.",true],["Le piège de puisque","employé avec une raison inconnue, il sonne prétentieux"]],
       say:"Puisque vous avez tous reçu l'alerte, vous savez pourquoi je vous écris.",
       note:"« Étant donné que » est un peu lourd à l'oral entre deux personnes, et parfait sur une feuille affichée à la porte du Centre. Le registre fait partie du choix."},

      {t:'ana', h:"Donc et c'est pourquoi — la conséquence",
       p:"Ceux-là ne disent pas la cause mais l'effet, et ils viennent après elle. La moitié de phrase qu'ils introduisent est la décision, pas la raison.",
       mots:[["Donc — l'oral","Il y a un avertissement, donc on reporte."],["C'est pourquoi — l'écrit","Les trottoirs seront glacés ; c'est pourquoi la sortie est reportée.",true],["Leur cousin","par conséquent — encore plus écrit, presque administratif"]],
       say:"Les trottoirs seront glacés toute la journée ; c'est pourquoi la sortie est reportée.",
       note:"On ne met jamais deux connecteurs pour la même relation : « comme il y a un avertissement, donc on reporte » en dit un de trop. Un seul suffit, toujours."},

      {t:'labo', h:"La même décision, cinq façons de la dire",
       p:"Choisissez un connecteur et écoutez la phrase entière.",
       axes:[{id:'c', lbl:'Quel connecteur ?', opts:[
         ['a','parce que'],
         ['b','comme'],
         ['c','puisque'],
         ['d','étant donné que'],
         ['e','c\'est pourquoi']]}],
       out:{
         a:{w:['reporter','un avertissement'], say:"La sortie est reportée parce qu'un avertissement de pluie verglaçante est en vigueur.", n:"la décision d'abord, la raison ensuite"},
         b:{w:['reporter'], say:"Comme les trottoirs seront glacés toute la journée, la sortie est reportée au vingt-deux.", n:"la raison d'abord : en tête de phrase seulement"},
         c:{w:['un avertissement'], say:"Puisque vous avez tous reçu l'alerte, vous savez déjà de quoi je parle.", n:"une raison que l'autre connaît déjà"},
         d:{w:['un avertissement','reporter'], say:"Étant donné qu'un avertissement est en vigueur, l'activité du huit est reportée au vingt-deux.", n:"le registre de l'avis affiché"},
         e:{w:['reporter'], say:"Le parc est fermé jusqu'au vingt ; c'est pourquoi nous avons choisi le samedi vingt-deux.", n:"la conséquence, après la cause"},
       },
       note:"Écoutez les cinq à la suite : c'est exactement la même décision, et elle ne fait pas du tout le même effet. C'est ça, choisir un connecteur."},

      {t:'ex', h:"À écouter et à répéter",
       p:"Six phrases complètes, décision et raison.",
       rows:[
         ["La sortie est reportée parce qu'un avertissement est en vigueur.","le plus neutre des six"],
         ["Comme les trottoirs seront glacés, nous préférons attendre.","la raison en premier"],
         ["Puisque vous avez reçu l'alerte, vous savez de quoi je parle.","une raison partagée"],
         ["Étant donné qu'un avis est en vigueur, l'activité est reportée au 22.","le registre de l'écrit officiel"],
         ["Le parc est fermé ; c'est pourquoi nous avons choisi le 22.","la conséquence, à l'écrit"],
         ["Il y a de la glace partout, donc on ne sort pas.","la conséquence, à l'oral"],
       ]},

      {t:'piege', h:"Trois pièges des connecteurs de cause",
       rows:[
         ["mettre « comme » au milieu de la phrase","« la sortie est reportée comme il y a du verglas »",
          "« Comme » de cause ne se place qu'en tête de phrase. Au milieu, employez « parce que ». C'est une règle sans exception, et elle règle la moitié des fautes de ce point."],
         ["doubler le connecteur","« comme il y a un avertissement, donc on reporte »",
          "Une seule relation, un seul mot. Soit « comme… , on reporte », soit « il y a un avertissement, donc on reporte ». Les deux ensemble sonnent comme une phrase qui recommence."],
         ["employer « puisque » avec une raison inconnue","« puisqu'il y aura cinq millimètres de glace » à quelqu'un qui l'ignore",
          "« Puisque » s'appuie sur ce que l'autre sait déjà. Devant une information neuve, il donne l'impression de reprocher à l'autre de ne pas être au courant. Prenez « parce que »."],
       ]},

      {t:'check', h:"Est-ce que c'est clair maintenant ?",
       p:"Quatre questions rapides.",
       qs:[
         {q:"« Comme » de cause se place…", opts:["en tête de phrase","après la décision"], ok:0,
          fb:"En tête de phrase, toujours. Ailleurs, employez « parce que »."},
         {q:"Le connecteur le plus neutre des six, c'est…", opts:["puisque","parce que"], ok:1,
          fb:"« Parce que ». Dans le doute, prenez celui-là."},
         {q:"« C'est pourquoi » introduit…", opts:["la cause","la conséquence"], ok:1,
          fb:"La conséquence : la décision, pas la raison."},
         {q:"Sur un avis affiché à la porte, on écrirait plutôt…", opts:["étant donné que","donc"], ok:0,
          fb:"« Étant donné que » : c'est le registre de l'écrit officiel."},
       ]},
    ]
  },

  // ════════════════════════════════════════════════════════════════════════
  t2fut: {
    eye:'Mini-leçon', tit:"Futur proche ou futur simple ?",
    blocs:[
      {t:'texte', h:"Deux futurs, et personne ne vous a dit lequel choisir",
       p:"« Je vais vous rappeler » et « je vous rappellerai » veulent dire la même chose et ne sonnent pas pareil. Le premier est le futur de la conversation : tout près, déjà en train de partir. Le second est le futur de l'écrit et de l'annonce : plus loin, plus officiel, plus engageant. Aucun des deux n'est plus correct que l'autre — mais employer le mauvais dans un avis affiché s'entend, et employer le mauvais au téléphone aussi.",
       note:"Les grammaires disent souvent que le futur proche est « du français parlé ». C'est vrai, mais incomplet : les gens parlent au futur simple dès qu'ils annoncent une date."},

      {t:'ana', h:"Le futur proche — aller au présent, plus l'infinitif",
       p:"C'est le futur de neuf conversations sur dix. Il dit ce qui est tout près, ou ce qu'on est déjà en train de mettre en route.",
       mots:[["La forme","je vais rappeler · tu vas partir · on va décider"],["Quand on l'emploie","au téléphone · pour la demi-heure qui vient · pour rassurer",true],["Dans le module","Je vais téléphoner aux huit personnes tout de suite."]],
       say:"Je vais vous rappeler ce soir. Ça va commencer dans une heure.",
       note:"Il donne l'impression que la chose est déjà lancée, et c'est précisément pour ça qu'il rassure quelqu'un qui attend."},

      {t:'ana', h:"Le futur simple — la date, l'avis, la promesse",
       p:"Un seul mot, formé sur l'infinitif. Il dit ce qui est fixé, ce qui est officiel, ce qui engage celui qui parle.",
       mots:[["La forme","je rappellerai · nous partirons · la sortie aura lieu"],["Quand on l'emploie","dans un avis · dans un courriel · pour une date au calendrier",true],["Dans le module","La sortie aura lieu le samedi vingt-deux, à treize heures."]],
       say:"La sortie aura lieu le samedi vingt-deux février, à treize heures.",
       note:"Devant un groupe, le futur simple fait sérieux. C'est le temps de « je vous confirmerai vendredi à midi » — une promesse qu'on tiendra."},

      {t:'ana', h:"Les deux dans le même message, sans faute",
       p:"On mélange les deux tout le temps, et personne ne trouve ça bizarre : le proche pour ce qu'on fait maintenant, le simple pour ce qui est au calendrier.",
       mots:[["Ensemble","Je vais téléphoner à tout le monde ; la sortie aura lieu le 22."],["Encore","On va décider vendredi, et je vous confirmerai à midi.",true],["Le repère","tout près → proche · au calendrier → simple"]],
       say:"Je vais téléphoner à tout le monde cet après-midi ; la sortie aura lieu le vingt-deux.",
       note:"Si vous n'êtes pas sûr, posez-vous une seule question : est-ce que cette chose a une date ? Si oui, futur simple. Sinon, futur proche."},

      {t:'labo', h:"La même annonce, deux futurs",
       p:"Choisissez une situation et écoutez la forme qui convient.",
       axes:[{id:'f', lbl:'Quelle situation ?', opts:[
         ['a','Au téléphone, tout de suite'],
         ['b','Un avis affiché à la porte'],
         ['c','Une promesse au groupe'],
         ['d','Une condition avec « si »'],
         ['e','Les deux futurs dans la même phrase']]}],
       out:{
         a:{w:['reporter'], say:"Je vais vous rappeler dans une demi-heure, dès que j'aurai parlé au coordonnateur.", n:"futur proche : tout près, à l'oral"},
         b:{w:['reporter'], say:"La sortie du huit février est reportée au samedi vingt-deux, à treize heures.", n:"le présent pour la décision, le futur pour la suite"},
         c:{w:['les prévisions'], say:"Je vous confirmerai vendredi à midi, quoi qu'annoncent les prévisions.", n:"futur simple : la promesse qui engage"},
         d:{w:['un avertissement'], say:"Si l'avertissement est levé jeudi, nous maintiendrons la sortie.", n:"présent après « si », futur simple après"},
         e:{w:['annuler','reporter'], say:"Je vais appeler les huit personnes cet après-midi ; la nouvelle sortie aura lieu le vingt-deux.", n:"le proche pour maintenant, le simple pour la date"},
       },
       note:"La quatrième est la seule où l'on n'a pas le choix : après « si » de condition, jamais de futur, ni proche ni simple."},

      {t:'ex', h:"À écouter et à répéter",
       p:"Six phrases, trois de chaque.",
       rows:[
         ["Je vais vous rappeler dès que j'aurai la confirmation.","proche : c'est pour tout de suite"],
         ["La sortie aura lieu le samedi vingt-deux, à treize heures.","simple : c'est au calendrier"],
         ["Ça va commencer dans une heure environ.","proche : c'est tout près"],
         ["Je vous confirmerai vendredi à midi au plus tard.","simple : c'est une promesse"],
         ["Si l'avertissement est levé, nous maintiendrons la sortie.","présent après « si »"],
         ["Nous partirons du Centre à treize heures précises.","simple : l'horaire annoncé"],
       ]},

      {t:'piege', h:"Trois pièges des deux futurs",
       rows:[
         ["mettre un futur après « si »","« si l'avertissement sera levé », « si ça va commencer »",
          "Après « si » de condition, présent obligatoire. Le futur va dans l'autre moitié : « si l'avertissement est levé, nous maintiendrons »."],
         ["employer le futur proche dans un avis écrit","« La sortie va avoir lieu le 22 » sur une feuille affichée",
          "À l'écrit, dans un avis, on écrit « aura lieu ». Le futur proche y sonne comme une conversation notée à la hâte."],
         ["hésiter entre futur et présent pour une décision prise","« la sortie sera reportée » quand c'est déjà décidé",
          "Une décision arrêtée se dit au présent : « la sortie est reportée ». Le futur laisse penser qu'on pourrait encore changer d'idée."],
       ]},

      {t:'check', h:"Est-ce que c'est clair maintenant ?",
       p:"Quatre questions rapides.",
       qs:[
         {q:"Au téléphone, pour ce qui est tout près, on emploie…", opts:["le futur proche","le futur simple"], ok:0,
          fb:"Le futur proche : « je vais vous rappeler »."},
         {q:"Sur un avis affiché, on écrit…", opts:["la sortie va avoir lieu le 22","la sortie aura lieu le 22"], ok:1,
          fb:"« Aura lieu ». Le futur simple est le temps de l'écrit officiel."},
         {q:"Après « si » de condition, on met…", opts:["le présent","un des deux futurs"], ok:0,
          fb:"Le présent, toujours."},
         {q:"Pour une décision déjà prise, le plus ferme est…", opts:["le présent","le futur simple"], ok:0,
          fb:"Le présent : « la sortie est reportée »."},
       ]},
    ]
  },

  // ════════════════════════════════════════════════════════════════════════
  t3imper: {
    eye:'Mini-leçon', tit:"L'impératif : dire quoi faire sans commander",
    blocs:[
      {t:'texte', h:"Un temps à trois personnes seulement",
       p:"L'impératif n'a ni « je », ni « il », ni « ils » : il ne s'adresse qu'à quelqu'un. Trois formes en tout — tu, nous, vous — et devant un groupe c'est presque toujours « vous ». Sa forme est celle du présent, sans le pronom sujet : vous apportez donne apportez. C'est le temps des consignes, des recettes, des modes d'emploi et des avis affichés à la porte d'un centre communautaire.",
       note:"Une seule bizarrerie d'écriture : à la deuxième personne du singulier, les verbes en -er perdent leur s. « Tu apportes » donne « apporte ». Devant un groupe, la question ne se pose pas."},

      {t:'ana', h:"La forme, et la négation",
       p:"On prend le présent et on enlève le pronom. À la forme négative, le ne et le pas entourent le verbe comme d'habitude.",
       mots:[["Affirmatif","apportez · prévoyez · buvez · attachez · marchez"],["Négatif","n'oubliez pas · ne partez pas sans eau · ne restez pas immobiles",true],["Dans un avis","N'oubliez pas vos crampons : les trottoirs seront glacés."]],
       say:"Apportez vos crampons. N'oubliez pas votre gourde.",
       note:"À l'oral, on entend souvent « oubliez pas » sans le « ne ». C'est du français parlé normal ; sur une feuille affichée, gardez le « ne »."},

      {t:'ana', h:"Les verbes pronominaux : le pronom passe derrière",
       p:"S'habiller, se couvrir, se rendre : à l'impératif affirmatif, le pronom vient après le verbe, avec un trait d'union. À la forme négative, il revient devant.",
       mots:[["Affirmatif","habillez-vous en trois couches · couvrez-vous le visage"],["Négatif","ne vous découvrez pas la tête · ne vous éloignez pas du groupe",true],["Avec « nous »","rendons-nous devant le Centre à midi quarante-cinq"]],
       say:"Habillez-vous en trois couches. Couvrez-vous le visage.",
       note:"C'est le point qui se voit le plus à l'écrit : « vous habillez-vous » ou « habillez vous » sans trait d'union sont deux fautes fréquentes, et faciles à éviter."},

      {t:'ana', h:"Trois irréguliers, et la façon d'adoucir",
       p:"Être, avoir et savoir ont un impératif à part, et les trois servent dans un avis. À côté, quelques formules rendent la consigne moins sèche sans rien lui enlever.",
       mots:[["Les trois irréguliers","soyez au Centre à midi · ayez vos crampons dans votre sac · sachez que la marche dure une heure"],["Adoucir","pensez à apporter… · n'oubliez pas de… · prévoyez…",true],["Adoucir encore","il faut prévoir deux litres d'eau par personne"]],
       say:"Soyez au Centre à midi quarante-cinq. Ayez vos crampons dans votre sac.",
       note:"« Pensez à apporter » et « apportez » disent exactement la même chose ; le premier laisse à l'autre l'impression d'avoir décidé lui-même. Devant des adultes, ça compte."},

      {t:'labo', h:"La même consigne, quatre façons de la donner",
       p:"Choisissez une forme et écoutez comment elle sonne.",
       axes:[{id:'m', lbl:'Quelle forme ?', opts:[
         ['a','Impératif direct'],
         ['b','Impératif adouci'],
         ['c','Impératif négatif'],
         ['d','Verbe pronominal'],
         ['e','Tournure impersonnelle']]}],
       out:{
         a:{w:['des crampons'], say:"Apportez des crampons et des bottes à bonne semelle.", n:"clair, court, un peu sec"},
         b:{w:['des crampons'], say:"Pensez à apporter vos crampons : les trottoirs seront glacés.", n:"la même consigne, en plus doux"},
         c:{w:['un coup de chaleur'], say:"Ne partez pas sans votre gourde : deux litres par personne.", n:"le ne et le pas entourent le verbe"},
         d:{w:['le refroidissement éolien'], say:"Habillez-vous en trois couches et couvrez-vous le visage.", n:"le pronom passe derrière, avec un trait d'union"},
         e:{w:['la chaleur extrême'], say:"Il faut prévoir deux litres d'eau par personne.", n:"l'obligation sans dire à qui elle s'adresse"},
       },
       note:"Les cinq disent la même chose. Dans un avis de trois lignes, alternez : cinq impératifs de suite donnent l'impression d'un règlement militaire."},

      {t:'ex', h:"À écouter et à répéter",
       p:"Six consignes du Centre communautaire.",
       rows:[
         ["Apportez des bottes à bonne semelle et vos crampons.","impératif direct"],
         ["Habillez-vous en trois couches plutôt qu'avec un gros manteau.","pronominal, trait d'union"],
         ["N'oubliez pas votre gourde : deux litres par personne.","négatif, avec la quantité"],
         ["Soyez devant le Centre à midi quarante-cinq.","être : soyez"],
         ["Buvez toutes les vingt minutes, même sans avoir soif.","la consigne qui sauve l'été"],
         ["Couvrez-vous le visage : le vent est plus froid que le thermomètre.","pronominal, avec la raison"],
       ]},

      {t:'piege', h:"Trois pièges de l'impératif",
       rows:[
         ["garder le pronom sujet","« vous apportez vos crampons » comme consigne",
          "Sans le « vous » devant, c'est une consigne ; avec, c'est une observation. « Vous apportez vos crampons » décrit ce que les gens font, il ne leur demande rien."],
         ["oublier le trait d'union des pronominaux","« habillez vous », « couvrez vous »",
          "À l'impératif affirmatif, le pronom se rattache au verbe par un trait d'union : habillez-vous, couvrez-vous. À la forme négative, il repasse devant, sans trait d'union : ne vous découvrez pas."],
         ["enchaîner cinq impératifs","« Apportez… Prenez… Mettez… Buvez… Soyez… »",
          "Une liste d'ordres met les gens sur la défensive, même quand elle est juste. Donnez la raison après chaque consigne, ou passez de temps en temps par « il faut » et « pensez à »."],
       ]},

      {t:'check', h:"Est-ce que c'est clair maintenant ?",
       p:"Quatre questions rapides.",
       qs:[
         {q:"L'impératif existe à…", opts:["trois personnes","six personnes"], ok:0,
          fb:"Trois : tu, nous, vous. Devant un groupe, c'est « vous »."},
         {q:"« S'habiller » à l'impératif, avec vous, donne…", opts:["vous habillez-vous","habillez-vous"], ok:1,
          fb:"« Habillez-vous » : pas de pronom sujet, et un trait d'union avant « vous »."},
         {q:"L'impératif d'« être », avec vous, c'est…", opts:["soyez","êtes"], ok:0,
          fb:"« Soyez ». C'est l'un des trois irréguliers utiles ici."},
         {q:"Pour adoucir une consigne, on peut dire…", opts:["pensez à apporter…","vous apportez…"], ok:0,
          fb:"« Pensez à apporter » : même consigne, moins sec."},
       ]},
    ]
  },

  // ════════════════════════════════════════════════════════════════════════
  t3ger: {
    eye:'Mini-leçon', tit:"Le gérondif : « en » plus le verbe en -ant",
    blocs:[
      {t:'texte', h:"La moitié de la consigne que tout le monde oublie",
       p:"« Buvez deux litres d'eau » dit quoi faire. « En buvant un peu toutes les vingt minutes » dit comment s'y prendre — et c'est cette moitié-là qui change quelque chose. Le gérondif est la forme qui porte la manière : une seule syllabe ajoutée devant un verbe en -ant, et la consigne devient exécutable. Le programme du niveau 5 le demande explicitement, pour marquer la manière ou la simultanéité ; le module vous fait l'employer dans les deux sens.",
       note:"Ne le confondez pas avec « être en train de », qui décrit ce qui se passe maintenant. « Il est en train de neiger » et « en neigeant toute la nuit » n'ont rien à voir."},

      {t:'ana', h:"La formation : le « nous » du présent, moins -ons, plus -ant",
       p:"Une seule règle, trois exceptions. On part du présent à la première personne du pluriel, on enlève la terminaison, on ajoute -ant, et on met « en » devant.",
       mots:[["La règle","nous marchons → en marchant · nous buvons → en buvant · nous partons → en partant"],["Les trois exceptions","être → en étant · avoir → en ayant · savoir → en sachant",true],["Les pronominaux","nous nous habillons → en vous habillant"]],
       say:"En marchant. En buvant. En partant. En vous habillant.",
       note:"Prendre le « nous » du présent règle presque tous les cas irréguliers d'un coup : nous prenons → en prenant, nous faisons → en faisant, nous voyons → en voyant."},

      {t:'ana', h:"Il dit la manière — comment on s'y prend",
       p:"C'est l'emploi le plus utile du module. La consigne vient d'abord, la manière ensuite, et le gérondif les colle ensemble.",
       mots:[["Dans les consignes du Centre","On évite un coup de chaleur en buvant avant d'avoir soif."],["Encore","On reste au chaud en s'habillant en trois couches.",true],["Et encore","On évite la foule en partant à neuf heures."]],
       say:"On évite un coup de chaleur en buvant avant d'avoir soif.",
       note:"Posez-vous la question « comment ? » après chaque consigne que vous donnez. Si vous n'avez pas de réponse, la consigne n'est pas finie."},

      {t:'ana', h:"Il dit aussi la simultanéité — en même temps",
       p:"Deux actions qui se déroulent ensemble, faites par la même personne. C'est le second emploi que le programme demande à ce niveau.",
       mots:[["Deux actions ensemble","En marchant, regardez où vous mettez les pieds."],["Encore","Elle écoutait le bulletin en préparant le café du groupe.",true],["Avec un repère de lieu","En sortant du Centre, vous verrez la promenade à votre droite."]],
       say:"En marchant, regardez toujours où vous mettez les pieds.",
       note:"La règle qui compte : les deux verbes ont le même sujet. « En sortant du Centre, vous verrez la promenade » — c'est vous qui sortez et vous qui voyez."},

      {t:'labo', h:"La même consigne, avec et sans la manière",
       p:"Choisissez une consigne et écoutez-la deux fois : nue, puis avec son gérondif.",
       axes:[{id:'g', lbl:'Quelle consigne ?', opts:[
         ['a','L\'eau, l\'été'],
         ['b','Les trois couches'],
         ['c','La marche sur la glace'],
         ['d','L\'heure de départ'],
         ['e','Les quatre à la suite']]}],
       out:{
         a:{w:['un coup de chaleur'], say:"Buvez deux litres d'eau. Buvez deux litres d'eau en prenant une gorgée toutes les vingt minutes.", n:"la manière dit quand, pas seulement combien"},
         b:{w:['le refroidissement éolien'], say:"Habillez-vous chaudement. Restez confortable en enlevant une couche à l'intérieur.", n:"la manière explique pourquoi trois couches"},
         c:{w:['des crampons'], say:"Attachez vos crampons. Vous éviterez les chutes en attachant vos crampons avant de sortir.", n:"la manière dit à quel moment"},
         d:{w:['la chaleur extrême'], say:"Partez tôt. Nous éviterons la chaleur en partant à neuf heures du matin.", n:"la manière donne le chiffre"},
         e:{w:['un coup de chaleur','des crampons'], say:"En buvant toutes les vingt minutes. En enlevant une couche à l'intérieur. En attachant vos crampons avant de sortir. En partant à neuf heures.", n:"quatre manières, quatre consignes complètes"},
       },
       note:"Écoutez la première version puis la seconde : la première se discute, la seconde s'exécute. C'est toute la différence que fait un gérondif."},

      {t:'ex', h:"À écouter et à répéter",
       p:"Six phrases avec gérondif, tirées du module.",
       rows:[
         ["On évite un coup de chaleur en buvant avant d'avoir soif.","manière"],
         ["Vous resterez au chaud en vous habillant en trois couches.","manière, verbe pronominal"],
         ["En marchant, regardez où vous mettez les pieds.","simultanéité"],
         ["Nous éviterons la chaleur en partant à neuf heures.","manière, avec l'heure"],
         ["En sortant du Centre, vous verrez la promenade à droite.","simultanéité et repère de lieu"],
         ["Elle a suivi le bulletin en préparant le café.","deux actions, un seul sujet"],
       ]},

      {t:'piege', h:"Trois pièges du gérondif",
       rows:[
         ["changer de sujet en cours de route","« en sortant du Centre, la promenade est visible »",
          "Les deux verbes doivent avoir le même sujet. La promenade ne sort pas du Centre : écrivez « en sortant du Centre, vous verrez la promenade »."],
         ["oublier le « en »","« buvant toutes les vingt minutes » tout seul",
          "Sans « en », ce n'est plus un gérondif mais un participe présent, et la phrase devient un français d'écrit ancien. Devant un groupe, gardez le « en » : c'est lui qui dit la manière."],
         ["le confondre avec « être en train de »","« il est en neigeant » au lieu de « il est en train de neiger »",
          "« En train de » décrit ce qui se passe maintenant. Le gérondif dit la manière ou la simultanéité. Les deux commencent par « en » et ne font pas le même travail."],
       ]},

      {t:'check', h:"Est-ce que c'est clair maintenant ?",
       p:"Quatre questions rapides.",
       qs:[
         {q:"Le gérondif se forme sur…", opts:["le « nous » du présent","l'infinitif"], ok:0,
          fb:"Sur le « nous » du présent : nous buvons → en buvant."},
         {q:"« En marchant, regardez où vous mettez les pieds » exprime…", opts:["la simultanéité","une condition"], ok:0,
          fb:"La simultanéité : les deux actions se font en même temps."},
         {q:"Les deux verbes d'un gérondif doivent avoir…", opts:["le même sujet","deux sujets différents"], ok:0,
          fb:"Le même sujet. C'est la règle qui attrape le plus de fautes à l'écrit."},
         {q:"Le gérondif de « savoir », c'est…", opts:["en savant","en sachant"], ok:1,
          fb:"« En sachant » : l'une des trois exceptions, avec en étant et en ayant."},
       ]},
    ]
  },

};
