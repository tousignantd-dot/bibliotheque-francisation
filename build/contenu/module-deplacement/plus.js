const PLUS = {
  prPhon: {
    eye:'Mini-leçon', tit:"Les consonnes qui tombent",
    blocs:[
      {t:'texte', h:"Pourquoi vous n'entendez pas tout",
       p:"Vous connaissez le mot <b>quelque</b>, mais dans une phrase rapide vous entendez « quek ». Vous connaissez <b>plus</b>, mais vous entendez « pu ». Ce n'est pas votre oreille : en français parlé, la dernière consonne d'un groupe tombe très souvent — surtout le <b>[l]</b> et le <b>[ʁ]</b>.",
       note:"C'est la première cause de panique dans une annonce de métro. Savoir que ça existe suffit à décoder la moitié de ce qui vous échappait."},

      {t:'ana', h:"Devant une consonne, ça tombe",
       p:"Quand le mot suivant commence par une consonne, la dernière lettre du groupe disparaît.",
       mots:[['On écrit','quelque chose'],['On entend','quek {chose}',true],['Aussi','plus tard › pu tard']],
       say:"Il y a quelque chose devant la porte.",
       note:"Autres exemples : <em>quatre minutes</em> › « quat minutes » · <em>autre chose</em> › « aut chose » · <em>notre voisin</em> › « not voisin »."},

      {t:'ana', h:"Devant une voyelle, on l'entend",
       p:"Quand le mot suivant commence par une voyelle, la consonne réapparaît et se lie.",
       mots:[['On écrit','notre arrêt'],['On entend','not{re arrêt}',true],['Aussi','une autre heure']],
       say:"Notre arrêt est le prochain.",
       note:"C'est ce qui rend le même mot méconnaissable d'une phrase à l'autre : <em>notre voisin</em> et <em>notre arrêt</em> ne sonnent pas pareil."},

      {t:'texte', h:"Ce que ça change pour vous",
       p:"Vous n'avez pas à parler comme ça. Mais quand un mot vous semble incomplet, <b>essayez de lui rendre sa dernière consonne</b> : « quek » devient quelque, « pu » devient plus, « quat » devient quatre. Le mot réapparaît presque toujours.",
       note:"Le programme du cours demande de reconnaître les mots malgré cette chute. C'est un objectif de compréhension, pas de prononciation."},

      {t:'labo', h:"Le même mot, deux fois",
       p:"Choisissez une paire et écoutez la différence.",
       axes:[{id:'p', lbl:'Quelle paire ?', opts:[
         ['a','quelque / quel'],
         ['b','plus tard / plus'],
         ['c','quatre minutes / quatre'],
         ['d','autre chose / une autre'],
         ['e','notre voisin / notre arrêt']]}],
       out:{
         a:{w:['quel{que} chose'], say:"Il y a quelque chose devant la porte.", n:'devant une consonne : le -que tombe'},
         b:{w:['p{lus} tard'], say:"On se voit plus tard.", n:'devant une consonne : le [l] tombe'},
         c:{w:['quat{re} minutes'], say:"Ça prend quatre minutes.", n:'devant une consonne : le [ʁ] tombe'},
         d:{w:['aut{re} chose'], say:"C'est autre chose.", n:'devant une consonne : le [ʁ] tombe'},
         e:{w:['not{re} arrêt'], say:"Notre arrêt est le prochain.", n:'devant une voyelle : on entend tout'},
       },
       note:"La dernière paire est la plus instructive : c'est le mot suivant qui décide, pas le mot lui-même."},

      {t:'ex', h:"À écouter deux fois",
       p:"Écoutez, puis rendez au mot sa dernière consonne.",
       rows:[
         ["Il y a quelque chose devant la porte.","« quek chose » — quelque"],
         ["On se voit plus tard.","« pu tard » — plus"],
         ["Ça prend quatre minutes.","« quat minutes » — quatre"],
         ["C'est autre chose.","« aut chose » — autre"],
         ["Notre arrêt est le prochain.","tout s'entend — voyelle après"],
         ["Notre voisin descend ici.","« not voisin » — notre"],
       ]},

      {t:'piege', h:"Deux malentendus fréquents",
       rows:[
         ["croire qu'on a mal entendu","« quek chose » est bien « quelque chose »",
          "Ne cherchez pas un mot inconnu. Cherchez d'abord un mot connu auquel il manque la fin — c'est presque toujours ça."],
         ["écrire ce qu'on entend","on écrit « quatre minutes », jamais « quat minutes »",
          "Cette chute n'existe qu'à l'oral. Rien ne change à l'écrit, jamais."],
       ]},

      {t:'check', h:"Est-ce que c'est clair maintenant ?",
       p:"Trois questions rapides.",
       qs:[
         {q:"La dernière consonne tombe surtout…", opts:["devant une voyelle","devant une consonne"], ok:1,
          fb:"« quatre minutes » perd son [ʁ] ; « notre arrêt » le garde."},
         {q:"« Pu tard », c'est…", opts:["plus tard","peu tard"], ok:0,
          fb:"Le [l] de <b>plus</b> est tombé devant le [t] de tard."},
         {q:"À l'écrit, cette chute…", opts:["se note","ne se note jamais"], ok:1,
          fb:"Elle n'existe qu'à l'oral."},
       ]},
    ]
  },

  t1imper: {
    eye:'Mini-leçon', tit:"L'impératif : dire quoi faire",
    blocs:[
      {t:'texte', h:"Le temps des itinéraires",
       p:"« Continuez tout droit. » « Tournez à gauche. » « Ne traversez pas le parc. » Un itinéraire est une suite d'ordres — et le français a un temps pour ça. L'impératif n'a que <b>trois personnes</b> et ne s'écrit <b>jamais avec un sujet</b>.",
       note:"C'est aussi le temps des recettes, des consignes de sécurité et des modes d'emploi. Une fois appris ici, il resservira partout."},

      {t:'ana', h:"La forme « vous » — avec un inconnu",
       p:"C'est celle qu'on emploie dans la rue, avec quelqu'un qu'on ne connaît pas. Elle est identique au présent, sans le mot « vous ».",
       mots:[['Au présent','vous continuez'],['À l\'impératif','{continuez}',true],['Dans la rue','Continuez tout droit.']],
       say:"Continuez tout droit jusqu'au feu.",
       note:"Autres exemples : <b>tournez</b>, <b>marchez</b>, <b>prenez</b>, <b>descendez</b>, <b>sortez</b>, <b>passez</b>."},

      {t:'ana', h:"La forme « tu » — avec un proche",
       p:"Avec un collègue, un ami, quelqu'un de son âge. Attention : aux verbes en <b>-er</b>, le <b>s</b> disparaît.",
       mots:[['Au présent','tu continues'],['À l\'impératif','continu{e}',true],['Sans -er','prends, sors, descends']],
       say:"Traverse le parc, il y a un sentier au milieu.",
       note:"Le <b>s</b> ne tombe qu'aux verbes en <b>-er</b> : « tourne », « marche », « traverse ». Les autres le gardent : « prends », « sors », « descends »."},

      {t:'ana', h:"La forme négative",
       p:"<b>ne</b> et <b>pas</b> entourent le verbe, comme partout ailleurs.",
       mots:[['On écrit','{ne} traversez {pas}'],['Avec un pronom','ne la manquez pas',true],['À l\'oral','« traversez pas »']],
       say:"Ne traversez pas le parc s'il pleut.",
       note:"À l'oral, le <b>ne</b> tombe presque toujours : on entend « traversez pas ». À l'écrit, il est obligatoire."},

      {t:'texte', h:"Trois verbes irréguliers à connaître",
       p:"<b>être</b> › soyez · <b>avoir</b> › ayez · <b>savoir</b> › sachez. On les rencontre surtout sur les affiches : « soyez prudent », « ayez votre titre en main », « sachez que le service se termine à minuit ».",
       note:"Trois formes à reconnaître, pas forcément à produire. Elles ne servent presque jamais dans un itinéraire parlé."},

      {t:'labo', h:"Vous ou tu ?",
       p:"Choisissez une situation et voyez quelle forme employer.",
       axes:[{id:'p', lbl:'À qui parlez-vous ?', opts:[
         ['a','à une passante inconnue'],
         ['b','à un collègue de classe'],
         ['c','à un enfant'],
         ['d','à un client au travail'],
         ['e','à un groupe de touristes']]}],
       out:{
         a:{w:['{Continuez} tout droit.'], say:"Continuez tout droit jusqu'au feu.", n:'inconnue › vous'},
         b:{w:['{Traverse} le parc.'], say:"Traverse le parc, il y a un sentier au milieu.", n:'collègue › tu, et le -s tombe'},
         c:{w:['{Tourne} à droite.'], say:"Tourne à droite après la pharmacie.", n:'enfant › tu, et le -s tombe'},
         d:{w:['{Prenez} l\'ascenseur.'], say:"Prenez l'ascenseur jusqu'au troisième.", n:'client › vous, toujours'},
         e:{w:['{Suivez}-moi, s\'il vous plaît.'], say:"Suivez-moi, s'il vous plaît.", n:'groupe › vous'},
       },
       note:"Dans le doute, employez <b>vous</b>. Personne n'a jamais été vexé d'être vouvoyé."},

      {t:'ex', h:"Les ordres du module",
       p:"Écoutez chacun et répétez-le à voix haute.",
       rows:[
         ["Continuez tout droit jusqu'au feu.","forme vous, verbe en -er"],
         ["Tournez à gauche sur Chambly.","forme vous, verbe en -er"],
         ["Prenez la ligne jaune jusqu'au terminus.","forme vous, verbe irrégulier"],
         ["Descendez au troisième arrêt.","forme vous"],
         ["Traverse le parc, il y a un sentier au milieu.","forme tu, le -s est tombé"],
         ["Ne traversez pas le parc s'il pleut.","forme négative"],
       ]},

      {t:'piege', h:"Trois pièges à connaître",
       rows:[
         ["garder le -s à la forme tu","« tourne à droite », jamais « tournes »",
          "Aux verbes en <b>-er</b> seulement, le <b>s</b> du présent disparaît à l'impératif. C'est la faute la plus fréquente à l'écrit."],
         ["écrire le sujet","« continuez », jamais « vous continuez »",
          "L'impératif n'a pas de sujet écrit. Le mettre transforme l'ordre en simple constat."],
         ["oublier le ne à l'écrit","« ne traversez pas », même si on dit « traversez pas »",
          "Le <b>ne</b> tombe à l'oral, jamais à l'écrit. Un itinéraire écrit sans <b>ne</b> se remarque tout de suite."],
       ]},

      {t:'check', h:"Est-ce que c'est clair maintenant ?",
       p:"Quatre questions rapides.",
       qs:[
         {q:"À une passante inconnue, on dit…", opts:["Tourne à gauche","Tournez à gauche"], ok:1,
          fb:"Avec un inconnu, on vouvoie."},
         {q:"À un ami, la forme correcte est…", opts:["traverse le parc","traverses le parc"], ok:0,
          fb:"Aux verbes en -er, le <b>s</b> disparaît à l'impératif."},
         {q:"L'impératif s'écrit…", opts:["avec son sujet","sans sujet"], ok:1,
          fb:"« Continuez », pas « vous continuez »."},
         {q:"À l'écrit, la négation demande…", opts:["ne et pas","pas seulement"], ok:0,
          fb:"« Ne traversez pas ». Le <b>ne</b> ne tombe qu'à l'oral."},
       ]},
    ]
  },

  t1prep: {
    eye:'Mini-leçon', tit:"jusqu'à, vers, par",
    blocs:[
      {t:'texte', h:"Trois prépositions, trois questions",
       p:"Un itinéraire répond à trois questions : <b>où j'arrête</b>, <b>de quel côté je vais</b>, et <b>par où je passe</b>. Chacune a sa préposition : <b>jusqu'à</b>, <b>vers</b>, <b>par</b>.",
       note:"Se tromper ne rend pas la phrase incompréhensible, mais envoie souvent la personne au mauvais endroit."},

      {t:'ana', h:"jusqu'à — où j'arrête",
       p:"Elle marque la limite du déplacement. Elle fusionne avec le déterminant : jusqu'<b>au</b>, jusqu'<b>aux</b>.",
       mots:[['La question','où j\'arrête ?'],['La forme','jusqu\'{au} feu',true],['Aussi','jusqu\'à Longueuil']],
       say:"Continuez tout droit jusqu'au feu de circulation.",
       note:"Devant un nom de lieu sans déterminant, pas de fusion : <em>jusqu'à Longueuil</em>, <em>jusqu'à Montréal</em>."},

      {t:'ana', h:"vers — de quel côté",
       p:"Elle donne la direction, sans dire où l'on s'arrête. C'est le mot des panneaux et des autobus.",
       mots:[['La question','de quel côté ?'],['La forme','{vers} Gaétan-Boucher',true],['Aussi','vers le nord']],
       say:"Prenez l'autobus qui va vers Gaétan-Boucher.",
       note:"« Vers » n'annonce pas une arrivée : un autobus qui va <em>vers</em> le centre-ville peut très bien tourner avant."},

      {t:'ana', h:"par — par où je passe",
       p:"Elle nomme le chemin emprunté, pas la destination.",
       mots:[['La question','par où ?'],['La forme','{par} le corridor',true],['Aussi','par la porte principale']],
       say:"Passez par le corridor vitré, à votre gauche.",
       note:"« À travers » est un cousin de <b>par</b>, mais insiste sur le fait de traverser quelque chose : <em>à travers le parc</em>, <em>à travers le boisé</em>."},

      {t:'texte', h:"Le test en une seconde",
       p:"Posez-vous la question à laquelle la phrase répond. <b>Où j'arrête ?</b> › jusqu'à. <b>De quel côté ?</b> › vers. <b>Par où je passe ?</b> › par. Si vous hésitez encore, c'est probablement <b>jusqu'à</b> : c'est la plus fréquente dans un itinéraire.",
       note:"Ce test suffit pour tout le niveau. Ne cherchez pas plus compliqué."},

      {t:'labo', h:"Quelle question pose la phrase ?",
       p:"Choisissez une phrase et voyez à quoi elle répond.",
       axes:[{id:'p', lbl:'Quelle phrase ?', opts:[
         ['a','Continuez ___ le feu.'],
         ['b',"L'autobus va ___ Gaétan-Boucher."],
         ['c','Passez ___ le corridor vitré.'],
         ['d','Prenez la ligne jaune ___ Longueuil.'],
         ['e','Le sentier passe ___ le parc.']]}],
       out:{
         a:{w:["Continuez {jusqu'au} feu."], say:"Continuez jusqu'au feu de circulation.", n:'où j\'arrête ? › jusqu\'à, fusionné en au'},
         b:{w:["L'autobus va {vers} Gaétan-Boucher."], say:"Prenez l'autobus qui va vers Gaétan-Boucher.", n:'de quel côté ? › vers'},
         c:{w:['Passez {par} le corridor vitré.'], say:"Passez par le corridor vitré, à votre gauche.", n:'par où ? › par'},
         d:{w:["Prenez la ligne jaune {jusqu'à} Longueuil."], say:"Prenez la ligne jaune jusqu'à Longueuil.", n:"nom de lieu sans déterminant : pas de fusion"},
         e:{w:['Le sentier passe {à travers} le parc.'], say:"Le sentier passe à travers le parc.", n:'on traverse quelque chose › à travers'},
       },
       note:"Comparez a et d : la même préposition, avec et sans fusion. C'est le déterminant qui décide."},

      {t:'ex', h:"Les phrases du module",
       p:"Écoutez chacune et repérez la préposition.",
       rows:[
         ["Continuez tout droit jusqu'au feu de circulation.","jusqu'à — la limite"],
         ["Prenez la ligne jaune jusqu'à Longueuil.","jusqu'à — sans fusion"],
         ["Prenez l'autobus qui va vers Gaétan-Boucher.","vers — la direction"],
         ["Passez par le corridor vitré, à votre gauche.","par — le chemin"],
         ["Sortez par la porte principale.","par — le chemin"],
         ["Le sentier passe à travers le parc.","à travers — on traverse"],
       ]},

      {t:'piege', h:"Trois pièges à connaître",
       rows:[
         ["oublier la fusion","« jusqu'au feu », jamais « jusqu'à le feu »",
          "à + le donne <b>au</b>, à + les donne <b>aux</b>. La fusion est obligatoire, comme partout en français."],
         ["confondre vers et jusqu'à","« vers » ne dit pas où on arrête",
          "Dire « allez vers le feu » laisse la personne dans le doute : faut-il s'arrêter au feu ou continuer ? « Jusqu'au feu » tranche."],
         ["employer par pour la destination","« par » nomme le chemin, pas l'arrivée",
          "« Je vais par Longueuil » veut dire que vous passez par là. Pour dire que vous y allez, c'est « à Longueuil »."],
       ]},

      {t:'check', h:"Est-ce que c'est clair maintenant ?",
       p:"Quatre questions rapides.",
       qs:[
         {q:"« Continuez ___ le feu » demande…", opts:["jusqu'au","vers le"], ok:0,
          fb:"On dit où la personne arrête : <b>jusqu'au</b>."},
         {q:"« Passez ___ le corridor » demande…", opts:["par","vers"], ok:0,
          fb:"C'est le chemin emprunté : <b>par</b>."},
         {q:"à + le donne…", opts:["au","à le"], ok:0,
          fb:"La fusion est obligatoire : jusqu'<b>au</b> feu."},
         {q:"« L'autobus va vers le centre-ville » veut dire…", opts:["il s'arrête au centre-ville","il va de ce côté-là"], ok:1,
          fb:"<b>vers</b> donne la direction, pas l'arrivée."},
       ]},
    ]
  },

  t2lieu: {
    eye:'Mini-leçon', tit:"Situer sans montrer du doigt",
    blocs:[
      {t:'texte', h:"Au téléphone, la main ne sert à rien",
       p:"Expliquer un chemin en personne, c'est facile : on montre. Au téléphone ou par écrit, il faut des mots. Le français en a une dizaine, et ils suffisent à tout : <b>tout droit</b>, <b>à gauche</b>, <b>à droite</b>, <b>en face de</b>, <b>devant</b>, <b>derrière</b>, <b>au coin de</b>, <b>au bout de</b>, <b>au milieu de</b>, <b>au-dessus de</b>.",
       note:"Dix mots pour toute une ville. Il vaut la peine de les savoir par cœur."},

      {t:'ana', h:"Les quatre qui dirigent",
       p:"Ceux-là disent où aller. Ce sont les seuls dont on ne peut pas se passer.",
       mots:[['Ne pas tourner','{tout droit}'],['Tourner','à gauche · à droite',true],['De l\'autre côté','en face de']],
       say:"Continuez tout droit, puis tournez à gauche.",
       note:"« En face de » se fusionne : en face <b>du</b> parc, en face <b>des</b> escaliers."},

      {t:'ana', h:"Les trois qui décrivent",
       p:"Ceux-là ne disent pas où aller : ils aident à reconnaître un endroit.",
       mots:[['Avant','{devant} la pharmacie'],['Après','derrière l\'édifice',true],['Tout près','à côté de la caisse']],
       say:"Vous allez passer devant une pharmacie et une caisse.",
       note:"Un bon itinéraire alterne les deux familles : une direction, un repère, une direction, un repère."},

      {t:'ana', h:"Les trois qui situent dans un espace",
       p:"Ils servent à préciser un endroit à l'intérieur d'un autre.",
       mots:[['Au croisement','{au coin de} deux rues'],['Tout au fond','au bout du corridor',true],['Au centre','au milieu du parc']],
       say:"L'escalier est au bout du corridor.",
       note:"Tous les trois se fusionnent : au coin <b>du</b> parc, au bout <b>des</b> escaliers, au milieu <b>de la</b> place."},

      {t:'texte', h:"Le piège du côté",
       p:"« À votre droite » veut dire à la droite de <b>la personne qui marche</b>, pas de celle qui parle. Quand vous expliquez un chemin, mettez-vous mentalement à la place de l'autre — ou dites plutôt un repère fixe : « du côté de la pharmacie », « du côté des numéros pairs ».",
       note:"Cette confusion est la cause la plus fréquente des itinéraires ratés, dans toutes les langues."},

      {t:'labo', h:"Diriger ou décrire ?",
       p:"Choisissez une indication et voyez ce qu'elle fait.",
       axes:[{id:'p', lbl:'Quelle indication ?', opts:[
         ['a','Continuez tout droit.'],
         ['b','En face de la pharmacie.'],
         ['c','Devant une caisse.'],
         ['d','Au bout du corridor.'],
         ['e','Au milieu du parc.']]}],
       out:{
         a:{w:['Continuez {tout droit}.'], say:"Continuez tout droit jusqu'au feu.", n:'dirige — ne tournez nulle part'},
         b:{w:['{En face de} la pharmacie.'], say:"L'hôpital est en face de l'arrêt d'autobus.", n:'dirige — de l\'autre côté de la rue'},
         c:{w:['{Devant} une caisse.'], say:"Vous allez passer devant une pharmacie et une caisse.", n:'décrit — un repère en chemin'},
         d:{w:['{Au bout du} corridor.'], say:"Descendez l'escalier au bout du corridor.", n:'situe — tout au fond'},
         e:{w:['{Au milieu du} parc.'], say:"Il y a un sentier au milieu du parc.", n:'situe — au centre'},
       },
       note:"Un itinéraire clair contient les trois familles. Un itinéraire qui ne fait que décrire laisse la personne sur place."},

      {t:'ex', h:"Les repères du module",
       p:"Écoutez chacun et répétez-le.",
       rows:[
         ["Continuez tout droit jusqu'au feu.","dirige"],
         ["Tournez à gauche sur Chambly.","dirige"],
         ["L'hôpital est juste en face.","dirige"],
         ["Vous allez passer devant une pharmacie.","décrit"],
         ["L'escalier est au bout du corridor.","situe"],
         ["Il y a un sentier au milieu du parc.","situe"],
       ]},

      {t:'piege', h:"Trois pièges à connaître",
       rows:[
         ["dire « à droite » sans dire de qui","dites plutôt « du côté de la pharmacie »",
          "Votre droite et celle de votre interlocuteur ne sont pas la même. Un repère fixe ne se trompe jamais."],
         ["oublier la fusion","« au bout du corridor », jamais « au bout de le corridor »",
          "de + le donne <b>du</b>, de + les donne <b>des</b>. C'est mécanique."],
         ["ne donner que des repères","« devant la pharmacie » ne dit pas où aller",
          "Les repères confirment qu'on est sur le bon chemin ; ils ne le tracent pas. Il faut aussi des directions."],
       ]},

      {t:'check', h:"Est-ce que c'est clair maintenant ?",
       p:"Quatre questions rapides.",
       qs:[
         {q:"« En face de » veut dire…", opts:["juste avant","de l'autre côté"], ok:1,
          fb:"En face, c'est vis-à-vis, de l'autre côté de la rue."},
         {q:"de + le donne…", opts:["du","de le"], ok:0,
          fb:"« Au bout <b>du</b> corridor »."},
         {q:"« À votre droite » désigne la droite…", opts:["de celui qui parle","de celui qui marche"], ok:1,
          fb:"Toujours celle de la personne qui se déplace."},
         {q:"Un itinéraire clair contient…", opts:["seulement des repères","des directions et des repères"], ok:1,
          fb:"Les repères confirment ; les directions tracent le chemin."},
       ]},
    ]
  },

  t2demo: {
    eye:'Mini-leçon', tit:"Celui, celle, ceux",
    blocs:[
      {t:'texte', h:"Choisir parmi plusieurs",
       p:"Il y a douze autobus au terminus. Vous voulez désigner <b>un seul</b> sans répéter le mot « autobus » à chaque phrase. C'est le travail des pronoms démonstratifs : <b>celui</b>, <b>celle</b>, <b>ceux</b>, <b>celles</b>.",
       note:"« Prenez celui qui va vers Gaétan-Boucher » est plus court, plus clair et plus naturel que de répéter « l'autobus »."},

      {t:'ana', h:"Quatre formes, selon le nom remplacé",
       p:"La forme ne dépend pas de qui parle, mais du nom qu'on remplace.",
       mots:[['Un masculin','{celui} — l\'autobus, l\'édifice'],['Un féminin','celle — la ligne, la sortie',true],['Des masculins','ceux — les cercles, les quais']],
       say:"Prenez celui qui va vers Gaétan-Boucher.",
       note:"La quatrième forme, <b>celles</b>, s'emploie pour des féminins pluriels : « celles qui vont vers la Rive-Sud »."},

      {t:'ana', h:"Jamais tout seul",
       p:"Un pronom démonstratif est toujours suivi de quelque chose : <b>-là</b>, <b>qui</b>, <b>que</b>, ou <b>de</b>.",
       mots:[['Avec -là','{celui-là}'],['Avec qui','celle qui a une porte vitrée',true],['Avec de','celui de 7 h 51']],
       say:"Ne prends pas celui de 7 h 42, prends celui de 7 h 51.",
       note:"« Celui » tout seul n'existe pas. Si vous ne savez pas quoi mettre après, employez <b>-là</b>."},

      {t:'texte', h:"Le lien avec qui, que, où",
       p:"Vous avez vu <b>qui</b> et <b>que</b> ailleurs : ils relient deux phrases. Ici, ils suivent un pronom démonstratif et font exactement le même travail. « Celui <b>qui</b> va vers Gaétan-Boucher » : après <b>qui</b>, un verbe. « Celui <b>que</b> je prends » : après <b>que</b>, un sujet.",
       note:"Rien de nouveau à apprendre, donc : c'est la même règle, appliquée après un autre mot."},

      {t:'labo', h:"Quelle forme ?",
       p:"Choisissez une phrase et voyez quel nom est remplacé.",
       axes:[{id:'p', lbl:'Quelle phrase ?', opts:[
         ['a',"l'autobus qui va vers Gaétan-Boucher"],
         ['b',"l'édifice qui a une porte vitrée"],
         ['c','la colonne de gauche'],
         ['d','les cercles des correspondances'],
         ['e','les lignes qui vont vers la Rive-Sud']]}],
       out:{
         a:{w:['{celui} qui va vers Gaétan-Boucher'], say:"Prenez celui qui va vers Gaétan-Boucher.", n:'un autobus : masculin singulier › celui'},
         b:{w:['{celui} qui a une porte vitrée'], say:"C'est celui qui a une porte vitrée.", n:'un édifice : masculin singulier › celui'},
         c:{w:['{celle} de gauche'], say:"Celle de gauche est celle de la semaine.", n:'une colonne : féminin singulier › celle'},
         d:{w:['{ceux} des correspondances'], say:"Les cercles noirs sont ceux des correspondances.", n:'des cercles : masculin pluriel › ceux'},
         e:{w:['{celles} qui vont vers la Rive-Sud'], say:"Celles qui vont vers la Rive-Sud sont les plus rapides.", n:'des lignes : féminin pluriel › celles'},
       },
       note:"Dans les cinq cas, c'est le nom remplacé — et lui seul — qui décide de la forme."},

      {t:'ex', h:"Les phrases du module",
       p:"Écoutez chacune et repérez le pronom.",
       rows:[
         ["Prenez celui qui va vers Gaétan-Boucher.","celui — un autobus"],
         ["C'est celui qui a une porte vitrée.","celui — un édifice"],
         ["Le parc avec les jeux ? Celui-là, oui.","celui-là — un parc"],
         ["Celle de gauche est celle de la semaine.","celle — une colonne"],
         ["Les cercles noirs sont ceux des correspondances.","ceux — des cercles"],
         ["Prends celui de 7 h 51.","celui — un autobus"],
       ]},

      {t:'piege', h:"Trois pièges à connaître",
       rows:[
         ["employer celui tout seul","« celui-là », « celui qui », « celui de »",
          "Un pronom démonstratif appelle toujours une suite. Seul, il ne veut rien dire."],
         ["accorder avec la personne qui parle","c'est le nom remplacé qui décide",
          "Une femme qui parle d'un autobus dit « celui », pas « celle ». Le pronom suit le nom, pas le locuteur."],
         ["confondre avec ce, cette","« cet autobus » et « celui-là » ne se remplacent pas",
          "<b>ce</b> et <b>cette</b> accompagnent un nom ; <b>celui</b> et <b>celle</b> le remplacent. On ne dit jamais « celui autobus »."],
       ]},

      {t:'check', h:"Est-ce que c'est clair maintenant ?",
       p:"Quatre questions rapides.",
       qs:[
         {q:"Pour remplacer « l'édifice », on dit…", opts:["celui","celle"], ok:0,
          fb:"Édifice est masculin singulier."},
         {q:"« Celui » peut-il rester seul dans la phrase ?", opts:["oui","non, jamais"], ok:1,
          fb:"Il est toujours suivi de -là, qui, que ou de."},
         {q:"Pour remplacer « les lignes », on dit…", opts:["ceux","celles"], ok:1,
          fb:"Une ligne est féminine, au pluriel : <b>celles</b>."},
         {q:"« Celui autobus » est…", opts:["correct","impossible"], ok:1,
          fb:"<b>celui</b> remplace le nom ; il ne l'accompagne jamais."},
       ]},
    ]
  },

  t3horaire: {
    eye:'Mini-leçon', tit:"Lire un horaire et un plan",
    blocs:[
      {t:'texte', h:"Tout est écrit, mais rien n'est expliqué",
       p:"Un horaire d'autobus et un plan de réseau contiennent tout ce qu'il faut — et n'expliquent rien. Deux colonnes de chiffres, des petites lettres, des cercles blancs et noirs. Quatre conventions suffisent à tout lire.",
       note:"Personne n'apprend cela à l'école. Les gens d'ici les ont apprises en se trompant."},

      {t:'ana', h:"Les deux colonnes",
       p:"La première est celle de la <b>semaine</b>, la deuxième celle de la <b>fin de semaine</b>. La deuxième est toujours plus courte : le service est plus rare.",
       mots:[['Colonne 1','{semaine} — lundi au vendredi'],['Colonne 2','fin de semaine',true],['À retenir','moins de départs la fin de semaine']],
       say:"La première colonne, c'est la semaine. La deuxième, c'est la fin de semaine.",
       note:"Si vous vous trompez de colonne un samedi, vous attendrez un autobus qui ne viendra pas."},

      {t:'ana', h:"Les petites lettres",
       p:"Une lettre à côté d'une heure annonce une <b>exception</b>. La légende, en bas de la page, dit laquelle.",
       mots:[['Ce qu\'on voit','7 h 42 {a}'],['Ce que ça veut dire','ne va pas au terminus',true],['Où chercher','la légende, en bas']],
       say:"Un petit « a », ça veut dire que l'autobus ne va pas jusqu'au terminus.",
       note:"C'est le détail le plus coûteux d'un horaire : il fait descendre les gens à mi-chemin, sans prévenir."},

      {t:'ana', h:"Les cercles du plan",
       p:"Un <b>cercle blanc</b> est un arrêt ordinaire. Un <b>cercle noir</b> est une correspondance : c'est là, et seulement là, qu'on change de ligne.",
       mots:[['Cercle blanc','{arrêt} ordinaire'],['Cercle noir','correspondance',true],['Couleur','une ligne complète']],
       say:"Les cercles blancs sont les arrêts, les cercles noirs les correspondances.",
       note:"Chercher à changer de ligne à un cercle blanc, c'est sortir de la station pour rien."},

      {t:'texte', h:"La règle d'or",
       p:"Sur un quai, sur un autobus, sur un panneau : <b>le nom du terminus donne la direction</b>. Lisez-le en premier, avant le numéro de la ligne, avant tout le reste. C'est la seule information qui ne trompe jamais.",
       note:"C'est ce que Gilles dit à Nour, et c'est la phrase à retenir de tout le module."},

      {t:'labo', h:"Que veut dire ce détail ?",
       p:"Choisissez un élément et voyez ce qu'il indique.",
       axes:[{id:'p', lbl:'Quel élément ?', opts:[
         ['a','la première colonne'],
         ['b',"un petit « a » à côté de l'heure"],
         ['c','un cercle blanc'],
         ['d','un cercle noir'],
         ['e','un nom en gras au bout de la ligne']]}],
       out:{
         a:{w:['la colonne de la {semaine}'], say:"La première colonne, c'est la semaine.", n:'du lundi au vendredi'},
         b:{w:["une {exception} — voir la légende"], say:"Un petit « a » veut dire que l'autobus ne va pas jusqu'au terminus.", n:'l\'autobus s\'arrête avant'},
         c:{w:['un {arrêt} ordinaire'], say:"Les cercles blancs sont les arrêts.", n:'on descend, mais on ne change pas de ligne'},
         d:{w:['une {correspondance}'], say:"Les cercles noirs sont les correspondances.", n:'c\'est ici qu\'on change de ligne'},
         e:{w:['le {terminus} — la direction'], say:"C'est le nom du terminus qui donne la direction.", n:'à lire en premier, toujours'},
       },
       note:"La dernière est la plus importante des cinq. Si vous n'en retenez qu'une, retenez celle-là."},

      {t:'ex', h:"Les phrases du module",
       p:"Écoutez et retenez.",
       rows:[
         ["La première colonne, c'est la semaine.","les deux colonnes"],
         ["Un petit « a » veut dire que l'autobus ne va pas jusqu'au terminus.","les petites lettres"],
         ["Prends celui de 7 h 51, il fait tout le trajet.","choisir le bon départ"],
         ["Chaque couleur est une ligne.","le plan"],
         ["Les cercles noirs sont les correspondances.","le plan"],
         ["C'est le nom du terminus qui donne la direction.","la règle d'or"],
       ]},

      {t:'piege', h:"Trois pièges à connaître",
       rows:[
         ["lire la colonne de la semaine un samedi","la deuxième colonne est celle de la fin de semaine",
          "L'erreur ne se voit pas : on attend simplement un autobus qui ne viendra pas."],
         ["ignorer la petite lettre","elle change souvent le trajet complet",
          "Une lettre non lue fait descendre à mi-chemin. La légende est en bas de la page, en tout petit."],
         ["se fier au numéro de la ligne seul","le même numéro va dans les deux sens",
          "L'autobus 45 existe dans les deux directions, avec le même numéro. Seul le nom du terminus les distingue."],
       ]},

      {t:'check', h:"Est-ce que c'est clair maintenant ?",
       p:"Quatre questions rapides.",
       qs:[
         {q:"Un samedi, il faut lire…", opts:["la première colonne","la deuxième colonne"], ok:1,
          fb:"La deuxième colonne est celle de la fin de semaine."},
         {q:"Un cercle noir sur le plan indique…", opts:["un arrêt ordinaire","une correspondance"], ok:1,
          fb:"On ne change de ligne qu'aux cercles noirs."},
         {q:"Ce qui donne la direction, c'est…", opts:["le numéro de la ligne","le nom du terminus"], ok:1,
          fb:"Le même numéro circule dans les deux sens."},
         {q:"Une petite lettre à côté d'une heure signale…", opts:["une exception","un retard"], ok:0,
          fb:"La légende, en bas de la page, dit laquelle."},
       ]},
    ]
  },
};
