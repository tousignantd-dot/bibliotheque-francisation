const PLUS = {
  prPhon: {
    eye:'Mini-leçon', tit:"Le « ou » de jour et le « u » de minute",
    blocs:[
      {t:'texte', h:"Deux sons que l'horaire fait se croiser à chaque phrase",
       p:"Une journée de travail se dit avec des <b>jour</b>s, des <b>heure</b>s et des <b>minute</b>s. Or « jour » a le son <b>ou</b>, et « minute » a le son <b>u</b>. Les deux se ressemblent à l'oreille, et beaucoup de langues n'en ont qu'un seul. Résultat : « douze » devient « duze », ou « une » devient « oune » — et le chef d'équipe entend une autre heure que celle qu'on a dite.",
       note:"Ce n'est pas un détail de politesse : c'est une heure d'arrivée. Un son mal placé, et on se présente au mauvais moment."},

      {t:'ana', h:"Le son « ou » — la langue au fond de la bouche",
       p:"C'est le son de « jour », « douze », « four », « tout de suite ».",
       mots:[['On écrit','j{ou}r'],['Les lèvres','en rond, poussées en avant',true],['La langue','tirée vers le fond']],
       say:"Le four est ouvert tout le jour.",
       note:"C'est le son que presque toutes les langues possèdent. Ce n'est donc pas celui-là qu'il faut travailler."},

      {t:'ana', h:"Le son « u » — la langue en avant, contre les dents",
       p:"C'est le son de « minute », « une », « uniforme », « cuisine ».",
       mots:[['On écrit','min{u}te'],['Les lèvres','en rond, très petites',true],['La langue','poussée contre les dents du haut']],
       say:"Une minute dans la cuisine.",
       note:"Le truc qui marche : dis « i » longtemps, puis arrondis les lèvres sans bouger la langue. Le son qui sort est le « u »."},

      {t:'ana', h:"Ce qui les sépare, c'est la langue, pas les lèvres",
       p:"Les lèvres font presque la même chose dans les deux sons.",
       mots:[['ou','langue en ARRIÈRE'],['u','langue en AVANT'],['Le test','dis « jour », puis « jure » : ça bouge',true]],
       say:"Jour, jure. Jour, jure.",
       note:"Si tu ne sens rien bouger entre les deux mots, c'est que la langue reste immobile. C'est elle qu'il faut déplacer."},

      {t:'labo', h:"Écoute les paires de l'horaire",
       p:"Choisis une paire et écoute la différence.",
       axes:[{id:'p', lbl:'Quelle paire ?', opts:[
         ['a','jour / jure'],
         ['b','douze / du'],
         ['c','tout / tu'],
         ['d','four / fut'],
         ['e','dans une phrase']]}],
       out:{
         a:{w:['j{ou}r / j{u}re'], say:"Un jour, une jure.", n:'ou derrière, u devant'},
         b:{w:['d{ou}ze / d{u}'], say:"Le casier douze, du matin.", n:'deux mots de l’horaire'},
         c:{w:['t{ou}t / t{u}'], say:"Tout de suite, tu commences.", n:'les deux dans la même phrase'},
         d:{w:['f{ou}r / f{u}t'], say:"Le four fut chaud.", n:'le mot du défi 3'},
         e:{w:['« Une minute, je poinçonne. »'], say:"Une minute, je poinçonne.", n:'u, puis ou'},
       },
       note:"Écoute chaque paire deux fois : la première pour comprendre, la seconde en fermant les yeux."},

      {t:'ex', h:"À écouter et à répéter",
       p:"Six phrases de la cafétéria.",
       rows:[
         ["Mon quart commence à douze heures.","ou deux fois"],
         ["Une minute, s'il vous plaît.","u deux fois"],
         ["Le four est dans la cuisine.","ou puis u"],
         ["Je poinçonne tous les jours.","ou trois fois"],
         ["Mon uniforme est dans le casier.","u au début"],
         ["Tout de suite après ma pause.","ou deux fois"],
       ]},

      {t:'piege', h:"Trois pièges à connaître",
       rows:[
         ["remplacer u par ou","« oune minute » au lieu de « une minute »",
          "Le piège le plus courant. Reviens au truc : dire « i », puis arrondir les lèvres sans bouger la langue."],
         ["croire que la lettre u fait toujours « u »","le u de « jour » ne se dit pas « u »",
          "Quand o et u sont côte à côte, ils font un seul son : « ou ». On lit la paire de lettres, jamais chaque lettre."],
         ["oublier le son dans les nombres","« douze » et « du » ne sonnent pas pareil",
          "Les nombres de l'horaire sont pleins de « ou » : douze, tout, jour. Une erreur là change une heure."],
       ]},

      {t:'check', h:"Est-ce que c'est clair maintenant ?",
       p:"Quatre questions rapides.",
       qs:[
         {q:"« Minute » a le son…", opts:["ou","u"], ok:1,
          fb:"La langue est en avant, contre les dents."},
         {q:"« Douze » a le son…", opts:["ou","u"], ok:0,
          fb:"Les lettres o et u ensemble font « ou »."},
         {q:"Ce qui distingue les deux sons, c'est…", opts:["les lèvres","la langue"], ok:1,
          fb:"Les lèvres sont presque pareilles dans les deux."},
         {q:"Pour trouver le « u », on part du son…", opts:["i","a"], ok:0,
          fb:"On dit « i », puis on arrondit les lèvres sans bouger la langue."},
       ]},
    ]
  },

  prMoments: {
    eye:'Mini-leçon', tit:'Le matin, le midi, le soir',
    blocs:[
      {t:'texte', h:"Quatre mots découpent toute la journée",
       p:"Avant même de lire une heure, on situe la journée en quatre morceaux : <b>le matin</b>, <b>le midi</b>, <b>l'après-midi</b>, <b>le soir</b>. Un horaire de travail se raconte presque toujours ainsi : « je travaille le matin », « lui, c'est le soir ». Les chiffres viennent après, pour préciser.",
       note:"Quand tu ne comprends pas une heure écrite, commence par demander le moment : « C'est le matin ou l'après-midi ? » On te répondra sans hésiter."},

      {t:'ana', h:"Le matin et le midi",
       p:"Du lever du jour jusqu'au repas.",
       mots:[['De 6 h à 11 h','{le matin}'],['Autour de 12 h','{le midi}'],['Sur l’horaire','6 h - 14 h, c’est un quart du matin',true]],
       say:"Je travaille le matin, de six heures à quatorze heures.",
       note:"« Midi » est une heure et un moment à la fois : « à midi » veut dire à douze heures pile."},

      {t:'ana', h:"L'après-midi et le soir",
       p:"Après le repas, jusqu'à la fermeture.",
       mots:[['De 13 h à 17 h',"{l’après-midi}"],['Après 18 h','{le soir}'],['Sur l’horaire','14 h - 22 h, c’est un quart du soir',true]],
       say:"Miguel travaille l'après-midi et le soir.",
       note:"« La nuit » existe aussi, pour les quarts qui commencent après vingt-trois heures. La cafétéria n'en a pas."},

      {t:'ana', h:"« Le » lundi ou « lundi » : deux sens",
       p:"Une seule petite lettre change l'habitude en date.",
       mots:[['Une seule fois','Je travaille {lundi}.'],['Chaque semaine','Je travaille {le} lundi.'],['Au pluriel','Je travaille {les} lundis et {les} mardis.',true]],
       say:"Je travaille lundi. Je travaille le lundi.",
       note:"Devant un jour, « le » veut dire : toutes les semaines. C'est exactement la même règle pour « le matin »."},

      {t:'labo', h:"Quel moment, quelle phrase ?",
       p:"Choisis un moment et vois comment on en parle.",
       axes:[
         {id:'m', lbl:'Quel moment ?', opts:[['a','le matin'],['b','le midi'],['c',"l'après-midi"],['d','le soir']]},
         {id:'q', lbl:'Quelle phrase ?', opts:[['1','mon habitude'],['2','aujourd’hui']]}],
       out:{
         a1:{w:["Je travaille le matin."], say:"Je travaille le matin.", n:'toutes les semaines'},
         a2:{w:["Ce matin, je commence à six heures."], say:"Ce matin, je commence à six heures.", n:'aujourd’hui seulement'},
         b1:{w:["Je prends ma pause le midi."], say:"Je prends ma pause le midi.", n:'chaque jour'},
         b2:{w:["Ce midi, je mange avant les résidents."], say:"Ce midi, je mange avant les résidents.", n:'aujourd’hui seulement'},
         c1:{w:["Je ne travaille pas l'après-midi."], say:"Je ne travaille pas l'après-midi.", n:'jamais, en général'},
         c2:{w:["Cet après-midi, je finis à quatorze heures."], say:"Cet après-midi, je finis à quatorze heures.", n:'aujourd’hui seulement'},
         d1:{w:["Miguel travaille le soir."], say:"Miguel travaille le soir.", n:'son quart habituel'},
         d2:{w:["Ce soir, il ferme la cuisine."], say:"Ce soir, il ferme la cuisine.", n:'aujourd’hui seulement'},
       },
       note:"Huit phrases utilisables telles quelles pour parler de ton propre horaire."},

      {t:'ex', h:"À écouter et à répéter",
       p:"Six phrases de la salle du personnel.",
       rows:[
         ["Je travaille le matin, du lundi au vendredi.","habitude"],
         ["Ce matin, il y a une livraison.","aujourd'hui"],
         ["Ma pause est le midi, trente minutes.","habitude"],
         ["L'après-midi, c'est le quart de Miguel.","habitude"],
         ["Ce soir, la cafétéria ferme à vingt-deux heures.","aujourd'hui"],
         ["Samedi et dimanche, je suis en congé.","habitude"],
       ]},

      {t:'piege', h:"Trois pièges à connaître",
       rows:[
         ["dire « en le matin »","on dit « le matin », sans autre mot",
          "Le moment de la journée n'a pas besoin de préposition : « le matin », « le soir ». Seulement « à midi » et « à minuit » prennent « à »."],
         ["confondre « le lundi » et « lundi »","l'un est chaque semaine, l'autre est une date",
          "Devant un jour, « le » veut dire : toujours. C'est la source d'un vrai malentendu avec un chef d'équipe."],
         ["croire qu'une case vide est une erreur","une case vide veut dire congé",
          "Rien n'est écrit parce qu'il n'y a rien à faire. On ne se présente pas ce jour-là."],
       ]},

      {t:'check', h:"Est-ce que c'est clair maintenant ?",
       p:"Quatre questions rapides.",
       qs:[
         {q:"« Je travaille le lundi » veut dire…", opts:["ce lundi-ci","tous les lundis"], ok:1,
          fb:"« Le » devant un jour veut dire : chaque semaine."},
         {q:"Un quart de 14 h à 22 h, c'est…", opts:["le matin","l'après-midi et le soir"], ok:1,
          fb:"Il commence après midi et se termine tard."},
         {q:"Une case vide sur l'horaire veut dire…", opts:["congé","tâche à choisir"], ok:0,
          fb:"Le congé ne s'écrit jamais : il se lit dans le vide."},
         {q:"On dit…", opts:["en le matin","le matin"], ok:1,
          fb:"Pas de préposition devant le moment de la journée."},
       ]},
    ]
  },

  t1prep: {
    eye:'Mini-leçon', tit:"De… à, jusqu'à, à partir de",
    blocs:[
      {t:'texte', h:"Quatre façons de placer une heure",
       p:"Sur l'horaire, une heure est un chiffre. À l'oral, elle a besoin d'un petit mot devant elle, et ce petit mot dit ce dont on parle : le <b>début</b>, la <b>fin</b>, les <b>deux</b>, ou la <b>durée</b>. Quatre formes, et une journée de travail se raconte au complet.",
       note:"Ces mots ne se traduisent pas un pour un depuis les autres langues. Le plus sûr est de les apprendre dans une phrase entière."},

      {t:'ana', h:"Les deux bouts : de… à…",
       p:"Un début et une fin, dans la même phrase.",
       mots:[['La forme','{de} 6 h {à} 14 h'],['On dit','Je travaille de six heures à quatorze heures.'],["C'est la forme de l’horaire",'6 h - 14 h se lit ainsi',true]],
       say:"Je travaille de six heures à quatorze heures.",
       note:"Le tiret de l'horaire, « 6 h - 14 h », se lit toujours « de… à… ». C'est la lecture la plus utile du module."},

      {t:'ana', h:"Seulement la fin : jusqu'à",
       p:"On dit quand ça s'arrête, sans dire quand ça a commencé.",
       mots:[['La forme',"{jusqu’à} 14 h"],['On dit','Je reste jusqu’à quatorze heures.'],['Avec midi',"{jusqu’à} midi",true]],
       say:"Je reste jusqu'à quatorze heures.",
       note:"« Jusqu'à » répond à la question « et après ? ». Il ferme le temps, il ne l'ouvre pas."},

      {t:'ana', h:"Seulement le début : à partir de",
       p:"On dit quand ça commence, sans dire quand ça finit.",
       mots:[['La forme','{à partir de} 5 h'],['On dit','La cuisine est ouverte à partir de cinq heures.'],['Plus court','{dès} cinq heures',true]],
       say:"La cuisine est ouverte à partir de cinq heures.",
       note:"« Dès » veut dire la même chose en un seul mot, mais « à partir de » s'entend beaucoup plus souvent au travail."},

      {t:'ana', h:"La durée : pendant",
       p:"Combien de temps, sans placer l'heure sur l'horloge.",
       mots:[['La forme','{pendant} huit heures'],['On dit','Je travaille pendant huit heures.'],['La question','{Combien de temps} ?',true]],
       say:"Je travaille pendant huit heures.",
       note:"Attention : « pendant huit heures » est une longueur ; « à huit heures » est un moment. Un seul mot de différence, deux sens."},

      {t:'labo', h:"La même journée, quatre façons de la dire",
       p:"Choisis le petit mot et vois la phrase.",
       axes:[
         {id:'p', lbl:'Quel petit mot ?', opts:[['a','de… à…'],['b',"jusqu'à"],['c','à partir de'],['d','pendant']]},
         {id:'q', lbl:'De quoi on parle ?', opts:[['1','mon quart'],['2','ma pause']]}],
       out:{
         a1:{w:["Je travaille de six heures à quatorze heures."], say:"Je travaille de six heures à quatorze heures.", n:'les deux bouts'},
         a2:{w:["Ma pause est de onze heures et demie à midi."], say:"Ma pause est de onze heures et demie à midi.", n:'les deux bouts'},
         b1:{w:["Je reste jusqu'à quatorze heures."], say:"Je reste jusqu'à quatorze heures.", n:'la fin seulement'},
         b2:{w:["Je mange jusqu'à midi."], say:"Je mange jusqu'à midi.", n:'la fin seulement'},
         c1:{w:["Je suis là à partir de six heures."], say:"Je suis là à partir de six heures.", n:'le début seulement'},
         c2:{w:["Je suis libre à partir de onze heures et demie."], say:"Je suis libre à partir de onze heures et demie.", n:'le début seulement'},
         d1:{w:["Je travaille pendant huit heures."], say:"Je travaille pendant huit heures.", n:'la durée'},
         d2:{w:["Je me repose pendant trente minutes."], say:"Je me repose pendant trente minutes.", n:'la durée'},
       },
       note:"Huit phrases, la même journée. Choisis celle qui répond à la question qu'on te pose."},

      {t:'ex', h:"À écouter et à répéter",
       p:"Six phrases du défi.",
       rows:[
         ["Je travaille de six heures à quatorze heures.","de… à…"],
         ["Miguel reste jusqu'à vingt-deux heures.","la fin"],
         ["La cuisine ouvre à partir de cinq heures.","le début"],
         ["La pause dure trente minutes.","la durée"],
         ["Je poinçonne avant six heures.","avant"],
         ["Le four chauffe pendant deux heures.","la durée"],
       ]},

      {t:'piege', h:"Trois pièges à connaître",
       rows:[
         ["dire « de 6 h jusqu'à 14 h »","on dit « de 6 h à 14 h »",
          "« De » va avec « à ». « Jusqu'à » se suffit à lui seul, sans « de » devant."],
         ["confondre « à » et « pendant »","« à huit heures » n'est pas « pendant huit heures »",
          "Le premier est un moment sur l'horloge, le second une longueur de temps. C'est l'erreur qui fait arriver au mauvais moment."],
         ["oublier le « de » du début","« je travaille six heures à quatorze heures »",
          "Sans « de », la phrase est bancale et l'on comprend une durée. Les deux petits mots vont ensemble."],
       ]},

      {t:'check', h:"Est-ce que c'est clair maintenant ?",
       p:"Quatre questions rapides.",
       qs:[
         {q:"« 6 h - 14 h » se lit…", opts:["de six heures à quatorze heures","pendant six heures"], ok:0,
          fb:"Le tiret de l'horaire se lit « de… à… »."},
         {q:"Pour dire seulement quand ça finit, on emploie…", opts:["à partir de","jusqu'à"], ok:1,
          fb:"« Jusqu'à » ferme le temps."},
         {q:"« Je travaille pendant huit heures » dit…", opts:["une durée","une heure d'arrivée"], ok:0,
          fb:"« Pendant » compte le temps, il ne le place pas."},
         {q:"« La cuisine ouvre ___ cinq heures. »", opts:["à partir de","jusqu'à"], ok:0,
          fb:"On donne ici le début, pas la fin."},
       ]},
    ]
  },

  t1quest: {
    eye:'Mini-leçon', tit:'Poser la question qui manque',
    blocs:[
      {t:'texte', h:"Cinq mots règlent presque toutes les questions du travail",
       p:"<b>À quelle heure</b>, <b>quand</b>, <b>combien de temps</b>, <b>qui</b>, <b>où</b>. Chacun appelle une réponse d'un type précis : une heure, un jour, une durée, une personne, un lieu. Choisir le bon mot, c'est déjà obtenir la bonne réponse.",
       note:"Une question mal posée reçoit une réponse qui ne sert à rien. Ce n'est pas de la grammaire de luxe : c'est du temps gagné."},

      {t:'ana', h:"Trois façons de poser la même question",
       p:"De la plus familière à la plus soignée.",
       mots:[['Familier','Tu commences {quand} ?'],['Courant','{Quand} est-ce que tu commences ?'],['Soigné','{Quand} commencez-vous ?',true]],
       say:"Quand est-ce que je commence ?",
       note:"La forme du milieu, avec « est-ce que », est la plus sûre au travail : polie, et facile à construire."},

      {t:'ana', h:"L'heure et le jour",
       p:"Deux questions qu'on pose chaque semaine.",
       mots:[['Une heure de l’horloge','{À quelle heure} est-ce que je commence ?'],['Un jour','{Quand} est-ce que je travaille ?'],['La réponse','à six heures · lundi',true]],
       say:"À quelle heure est-ce que je commence ?",
       note:"« Quand » accepte aussi une heure, mais « à quelle heure » est plus précis. Devant un chef d'équipe pressé, la précision paie."},

      {t:'ana', h:"La durée, la personne, le lieu",
       p:"Trois questions courtes et très utiles.",
       mots:[['Une longueur','{Combien de temps} est-ce que ça dure ?'],['Une personne','{Qui} est-ce qui me remplace ?'],['Un endroit','{Où} est-ce que je poinçonne ?',true]],
       say:"Combien de temps est-ce que ça dure ?",
       note:"« Qui est-ce qui » paraît long, mais c'est la forme la plus claire. « Qui me remplace ? » marche aussi très bien."},

      {t:'labo', h:"La question et sa réponse",
       p:"Choisis un mot interrogatif et vois ce qu'on te répondra.",
       axes:[{id:'m', lbl:'Quel mot ?', opts:[
         ['a','à quelle heure'],['b','quand'],['c','combien de temps'],['d','qui'],['e','où']]}],
       out:{
         a:{w:["À quelle heure est-ce que je commence ?","— À six heures."], say:"À quelle heure est-ce que je commence ? À six heures.", n:'une heure de l’horloge'},
         b:{w:["Quand est-ce que je travaille ?","— Du lundi au vendredi."], say:"Quand est-ce que je travaille ? Du lundi au vendredi.", n:'un jour, une période'},
         c:{w:["Combien de temps est-ce que la pause dure ?","— Trente minutes."], say:"Combien de temps est-ce que la pause dure ? Trente minutes.", n:'une durée'},
         d:{w:["Qui est-ce qui me remplace jeudi ?","— Miguel."], say:"Qui est-ce qui me remplace jeudi ? Miguel.", n:'une personne'},
         e:{w:["Où est-ce que je poinçonne ?","— À côté de la porte grise."], say:"Où est-ce que je poinçonne ? À côté de la porte grise.", n:'un lieu'},
       },
       note:"Cinq questions, cinq types de réponse. Apprends-les par paires : la question et ce qu'elle appelle."},

      {t:'ex', h:"À écouter et à répéter",
       p:"Six questions du premier mois de travail.",
       rows:[
         ["À quelle heure est-ce que je commence lundi ?","une heure"],
         ["Quand est-ce que j'ai congé ?","un jour"],
         ["Combien de temps dure ma pause ?","une durée"],
         ["Qui est-ce qui me montre le lave-vaisselle ?","une personne"],
         ["Où est le vestiaire, s'il vous plaît ?","un lieu"],
         ["Est-ce que je peux poser une question ?","la question avant la question"],
       ]},

      {t:'piege', h:"Trois pièges à connaître",
       rows:[
         ["utiliser « quand » pour une durée","« Quand ça dure ? » ne veut rien dire",
          "La durée se demande avec « combien de temps ». « Quand » demande un moment, pas une longueur."],
         ["oublier « est-ce que »","« Je finis quand ? » est très familier",
          "Avec un chef d'équipe, garde « est-ce que » : ça reste simple à construire et ça sonne poli."],
         ["poser deux questions à la fois","« Quand et à quelle heure et qui ? »",
          "Une question, une réponse. On note, puis on pose la suivante. C'est ainsi qu'on retient."],
       ]},

      {t:'check', h:"Est-ce que c'est clair maintenant ?",
       p:"Quatre questions rapides.",
       qs:[
         {q:"Pour connaître la durée d'une pause, on demande…", opts:["quand","combien de temps"], ok:1,
          fb:"« Combien de temps » appelle une longueur."},
         {q:"« À six heures » répond à…", opts:["à quelle heure","où"], ok:0,
          fb:"C'est une heure de l'horloge."},
         {q:"La forme la plus sûre au travail est…", opts:["Tu finis quand ?","Quand est-ce que je finis ?"], ok:1,
          fb:"« Est-ce que » est poli et facile à construire."},
         {q:"« Miguel » répond à…", opts:["qui","quand"], ok:0,
          fb:"C'est une personne."},
       ]},
    ]
  },

  t2modal: {
    eye:'Mini-leçon', tit:'Pouvoir, devoir, falloir',
    blocs:[
      {t:'texte', h:"Trois verbes, trois messages très différents",
       p:"Ces trois verbes se placent devant un autre verbe et changent complètement le sens de la phrase. <b>Pouvoir</b> demande ou accorde ; <b>devoir</b> explique une obligation personnelle ; <b>falloir</b> énonce la règle de la place. Se tromper de verbe, c'est demander une permission là où on annonce une décision — ou l'inverse.",
       note:"Au travail, la différence entre « je peux partir à midi » et « je dois partir à midi » est énorme. La première demande ; la seconde informe."},

      {t:'ana', h:"Pouvoir — la permission et la capacité",
       p:"Le verbe de la demande polie.",
       mots:[['Demander','Est-ce que {je peux} partir à midi ?'],['Demander de l’aide','Est-ce que {vous pouvez} m’aider ?'],['Être capable','Miguel {peut} me remplacer.',true]],
       say:"Est-ce que je peux partir à midi ?",
       note:"« Est-ce que je pourrais… ? » est la version encore plus polie. Elle s'emploie pour une demande qui dérange un peu."},

      {t:'ana', h:"Devoir — l'obligation qui vient d'ailleurs",
       p:"Ce n'est pas un choix : quelque chose m'y oblige.",
       mots:[['Une obligation','{Je dois} aller à la clinique.'],['Une règle pour moi','{Je dois} poinçonner en arrivant.'],['Pour une autre personne','Miguel {doit} fermer la cuisine.',true]],
       say:"Je dois aller à la clinique avec mon garçon.",
       note:"« Je dois » explique pourquoi on demande. C'est la phrase qui accompagne presque toujours la demande de permission."},

      {t:'ana', h:"Falloir — la règle de la place",
       p:"Personne n'est nommé : c'est vrai pour tout le monde.",
       mots:[['La règle','{Il faut} aviser trois jours avant.'],['Une seule forme','{il faut}, jamais « je faut »'],['Au négatif','{Il ne faut pas} oublier le four.',true]],
       say:"Il faut aviser le chef d'équipe trois jours avant.",
       note:"Ce verbe n'existe qu'avec « il ». C'est le seul de la langue à fonctionner ainsi, et c'est celui des consignes affichées."},

      {t:'labo', h:"La même journée, trois verbes",
       p:"Choisis le verbe et la situation.",
       axes:[
         {id:'v', lbl:'Quel verbe ?', opts:[['a','pouvoir'],['b','devoir'],['c','falloir']]},
         {id:'s', lbl:'Quelle situation ?', opts:[['1','partir à midi'],['2','échanger un quart']]}],
       out:{
         a1:{w:["Est-ce que je peux partir à midi ?"], say:"Est-ce que je peux partir à midi ?", n:'je demande la permission'},
         a2:{w:["Est-ce que je peux échanger mon jeudi ?"], say:"Est-ce que je peux échanger mon jeudi ?", n:'je demande la permission'},
         b1:{w:["Je dois partir à midi, j'ai un rendez-vous."], say:"Je dois partir à midi, j'ai un rendez-vous.", n:'j’explique pourquoi'},
         b2:{w:["Je dois échanger mon jeudi, mon garçon est malade."], say:"Je dois échanger mon jeudi, mon garçon est malade.", n:'j’explique pourquoi'},
         c1:{w:["Il faut avertir avant de partir."], say:"Il faut avertir avant de partir.", n:'la règle de la place'},
         c2:{w:["Il faut aviser trois jours avant."], say:"Il faut aviser trois jours avant.", n:'la règle de la place'},
       },
       note:"La bonne conversation les emploie tous les trois : je dois (j'explique), est-ce que je peux (je demande), il faut (on me répond)."},

      {t:'ex', h:"À écouter et à répéter",
       p:"Six phrases du défi.",
       rows:[
         ["Est-ce que je peux vous parler deux minutes ?","permission"],
         ["Est-ce que vous pouvez m'aider ?","aide"],
         ["Je dois aller à la clinique jeudi.","obligation"],
         ["Il faut aviser trois jours avant.","règle"],
         ["Miguel peut me remplacer.","capacité"],
         ["Il ne faut pas oublier de poinçonner.","règle au négatif"],
       ]},

      {t:'piege', h:"Trois pièges à connaître",
       rows:[
         ["conjuguer le deuxième verbe","« je peux je pars » au lieu de « je peux partir »",
          "Après pouvoir, devoir et falloir, le verbe suivant ne change jamais : il reste à l'infinitif."],
         ["dire « je faut »","falloir n'existe qu'avec « il »",
          "Pour parler de soi, on dit « je dois ». « Il faut » ne nomme personne, exprès."],
         ["tutoyer son chef d'équipe","« est-ce que tu peux » à une personne responsable",
          "Au travail, on dit « vous » à son supérieur, et souvent « tu » aux collègues du même rang."],
       ]},

      {t:'check', h:"Est-ce que c'est clair maintenant ?",
       p:"Quatre questions rapides.",
       qs:[
         {q:"Pour demander une permission, on emploie…", opts:["pouvoir","falloir"], ok:0,
          fb:"« Est-ce que je peux… ? » demande la permission."},
         {q:"« Il faut poinçonner » veut dire…", opts:["c'est la règle pour tout le monde","c'est mon choix"], ok:0,
          fb:"Falloir énonce la règle de la place."},
         {q:"Après « je dois », le verbe est…", opts:["conjugué","à l'infinitif"], ok:1,
          fb:"Je dois finir, je dois partir, je dois aviser."},
         {q:"À son chef d'équipe, on dit…", opts:["est-ce que tu peux","est-ce que vous pouvez"], ok:1,
          fb:"On vouvoie la personne responsable."},
       ]},
    ]
  },

  t2repondre: {
    eye:'Mini-leçon', tit:'Répondre à une demande de service',
    blocs:[
      {t:'texte', h:"Répondre, c'est aussi une compétence de travail",
       p:"Un collègue demande de l'aide, et il faut répondre tout de suite — même quand la réponse est non. Trois réponses possibles : <b>oui</b>, <b>pas maintenant</b>, ou <b>non, et voici pourquoi</b>. Ce qui compte, c'est de répondre : un silence est plus impoli qu'un refus.",
       note:"Le programme demande explicitement de répondre à une demande de service, pas seulement d'en faire. C'est ce que ce défi travaille."},

      {t:'ana', h:"Dire oui, en trois mots",
       p:"Les réponses courtes sont les plus naturelles.",
       mots:[['La plus courante','{Oui, bien sûr.}'],['Encore plus simple','{Pas de problème.}'],['Si tu viens tout de suite','{Tout de suite.}',true]],
       say:"Oui, bien sûr. Pas de problème.",
       note:"Inutile de faire une longue phrase : « Oui, bien sûr » suffit et sonne juste dans toutes les cuisines du Québec."},

      {t:'ana', h:"Faire attendre, sans refuser",
       p:"Une réponse honnête quand on a les mains pleines.",
       mots:[['Le plus court','{Une minute}, j’arrive.'],['Entre collègues','{Attends deux secondes.}'],['Avec une raison','{Après le four}, je viens t’aider.',true]],
       say:"Une minute, j'arrive.",
       note:"Cette réponse dit deux choses à la fois : j'ai entendu, et je ne t'oublie pas. C'est la plus utile des trois."},

      {t:'ana', h:"Dire non, avec une raison",
       p:"Un « non » tout seul est dur ; un « non » expliqué ne l'est pas.",
       mots:[['On adoucit','{Je regrette}, je suis occupée.'],['Autre forme','{Désolée}, je dois éteindre le four.'],['On propose autre chose','Demande à Miguel, il {est libre}.',true]],
       say:"Je regrette, je dois éteindre le four.",
       note:"Proposer une autre solution transforme un refus en aide. C'est ce que fait une bonne équipe."},

      {t:'labo', h:"La même demande, trois réponses",
       p:"Choisis la demande et ta réponse.",
       axes:[
         {id:'d', lbl:'Quelle demande ?', opts:[['a','« Tu peux m’aider ? »'],['b','« Passe-moi ton crayon. »']]},
         {id:'r', lbl:'Ta réponse ?', opts:[['1','oui'],['2','attends'],['3','non']]}],
       out:{
         a1:{w:["Oui, bien sûr. J'arrive."], say:"Oui, bien sûr. J'arrive.", n:'la plus simple'},
         a2:{w:["Une minute, je finis les plateaux."], say:"Une minute, je finis les plateaux.", n:'j’ai entendu, j’arrive après'},
         a3:{w:["Je regrette, je dois éteindre le four."], say:"Je regrette, je dois éteindre le four.", n:'non, avec la raison'},
         b1:{w:["Tiens, le voilà."], say:"Tiens, le voilà.", n:'un service rendu tout de suite'},
         b2:{w:["Attends deux secondes, je note l'heure."], say:"Attends deux secondes, je note l'heure.", n:'court, entre collègues'},
         b3:{w:["Désolée, je n'en ai pas. Demande à Miguel."], say:"Désolée, je n'en ai pas. Demande à Miguel.", n:'non, et une solution'},
       },
       note:"Six réponses, toutes polies. Aucune n'est un silence, et c'est ce qui compte."},

      {t:'ex', h:"À écouter et à répéter",
       p:"Six réponses de la cafétéria.",
       rows:[
         ["Oui, bien sûr.","oui"],
         ["Pas de problème, j'arrive.","oui"],
         ["Une minute, je finis les boîtes.","attendre"],
         ["Je regrette, je suis occupée.","non"],
         ["Désolée, je finis à quatorze heures.","non avec raison"],
         ["Merci beaucoup, monsieur Roy.","remercier"],
       ]},

      {t:'piege', h:"Trois pièges à connaître",
       rows:[
         ["répondre « non » tout seul","sans raison, ça sonne dur",
          "Un mot de raison suffit : « non, je dois éteindre le four ». L'autre comprend et ne le prend pas mal."],
         ["ne rien répondre","le silence passe pour un refus",
          "Même occupé, dis quelque chose : « une minute ». C'est ce que le collègue attend."],
         ["oublier de remercier","une demande acceptée se remercie",
          "« Merci beaucoup » clôt la conversation. Sans lui, l'échange reste bizarrement ouvert."],
       ]},

      {t:'check', h:"Est-ce que c'est clair maintenant ?",
       p:"Quatre questions rapides.",
       qs:[
         {q:"La pire réponse à une demande d'aide est…", opts:["« Je regrette, je suis occupée. »","ne rien dire"], ok:1,
          fb:"Le silence est plus impoli qu'un refus expliqué."},
         {q:"« Une minute, j'arrive » veut dire…", opts:["non","oui, mais pas tout de suite"], ok:1,
          fb:"C'est une acceptation, avec un délai."},
         {q:"Un refus se dit toujours avec…", opts:["une raison","un long discours"], ok:0,
          fb:"Une raison courte suffit."},
         {q:"Après une demande acceptée, on dit…", opts:["merci beaucoup","rien"], ok:0,
          fb:"On remercie, toujours."},
       ]},
    ]
  },

  t3imp: {
    eye:'Mini-leçon', tit:"L'impératif : la forme qui commande",
    blocs:[
      {t:'texte', h:"Le verbe passe en premier, et le sujet disparaît",
       p:"Quand un chef d'équipe donne une consigne, il ne dit pas « vous sortez les plateaux », il dit « <b>Sortez</b> les plateaux ». C'est la même forme du verbe, mais sans le mot « vous » devant. Le verbe se retrouve au début de la phrase : c'est le signal qu'on te demande de faire quelque chose maintenant.",
       note:"Reconnaître cette forme, c'est reconnaître qu'on te parle à toi. C'est l'intention « comprendre une consigne » du programme."},

      {t:'ana', h:"Trois formes, et une seule sert vraiment",
       p:"Selon à qui on parle.",
       mots:[['À un collègue','{Range} les boîtes.'],['À vous, ou poliment','{Rangez} les boîtes.'],['Ensemble','{Rangeons} les boîtes.',true]],
       say:"Range les boîtes. Rangez les boîtes.",
       note:"Au travail, la forme en -ez domine : elle sert pour « vous » et comme forme polie. C'est celle du module."},

      {t:'ana', h:"La négation entoure le verbe",
       p:"Comme dans toutes les phrases négatives.",
       mots:[['La forme',"{N’oubliez pas} le four."],['Autre exemple','{Ne partez pas} avant midi.'],['À l’oral','on entend surtout le « pas »',true]],
       say:"N'oubliez pas le four à onze heures.",
       note:"« N'oubliez pas » est la consigne la plus fréquente de toutes les cuisines. Apprends-la en bloc."},

      {t:'ana', h:"Trois verbes irréguliers à connaître",
       p:"Ceux-là ne suivent pas la règle.",
       mots:[['venir','{Venez} me voir.'],['faire','{Faites} les plateaux d’abord.'],['être','{Soyez} là à six heures.',true]],
       say:"Venez me voir. Faites les plateaux. Soyez là à six heures.",
       note:"Trois formes à apprendre par cœur : elles reviennent chaque semaine dans une cuisine."},

      {t:'labo', h:"La consigne et ce qu'elle demande",
       p:"Choisis un verbe et vois la consigne complète.",
       axes:[
         {id:'v', lbl:'Quel verbe ?', opts:[['a','sortir'],['b','ranger'],['c','éteindre'],['d','venir']]},
         {id:'f', lbl:'Quelle forme ?', opts:[['1','on demande'],['2','on interdit']]}],
       out:{
         a1:{w:["Sortez les plateaux du chariot."], say:"Sortez les plateaux du chariot.", n:'la consigne'},
         a2:{w:["Ne sortez pas les plateaux tout de suite."], say:"Ne sortez pas les plateaux tout de suite.", n:'la consigne au négatif'},
         b1:{w:["Rangez les boîtes dans la chambre froide."], say:"Rangez les boîtes dans la chambre froide.", n:'la consigne'},
         b2:{w:["Ne rangez pas les boîtes dans le corridor."], say:"Ne rangez pas les boîtes dans le corridor.", n:'la consigne au négatif'},
         c1:{w:["Éteignez le four à onze heures."], say:"Éteignez le four à onze heures.", n:'la consigne'},
         c2:{w:["N'éteignez pas le lave-vaisselle."], say:"N'éteignez pas le lave-vaisselle.", n:'la consigne au négatif'},
         d1:{w:["Venez me voir avant votre pause."], say:"Venez me voir avant votre pause.", n:'verbe irrégulier'},
         d2:{w:["Ne venez pas avant six heures."], say:"Ne venez pas avant six heures.", n:'verbe irrégulier au négatif'},
       },
       note:"Huit consignes réelles. Écoute-les, puis redis-les : c'est exactement ce que fait Fabiola dans le dialogue."},

      {t:'ex', h:"À écouter et à répéter",
       p:"Six consignes de la cuisine.",
       rows:[
         ["Sortez les plateaux du chariot.","-ez"],
         ["Rangez les boîtes dans la chambre froide.","-ez"],
         ["Éteignez le four à onze heures.","-ez"],
         ["N'oubliez pas de poinçonner.","au négatif"],
         ["Venez me voir avant midi.","irrégulier"],
         ["Soyez là à six heures, s'il vous plaît.","irrégulier"],
       ]},

      {t:'piege', h:"Trois pièges à connaître",
       rows:[
         ["croire que c'est impoli","une consigne n'est pas une colère",
          "« Éteignez le four » est la façon normale de donner une tâche. Le « s'il vous plaît » qui suit dit tout."],
         ["garder le mot « vous »","« Vous rangez les boîtes » n'est pas une consigne",
          "Sans le sujet, c'est un ordre ; avec le sujet, c'est une description. Le chef d'équipe emploie la première forme."],
         ["oublier le « ne » à l'écrit","« oubliez pas » s'entend, mais s'écrit avec « n’ »",
          "À l'oral québécois, le « ne » disparaît souvent. Dans le petit mot qu'on laisse, il s'écrit."],
       ]},

      {t:'check', h:"Est-ce que c'est clair maintenant ?",
       p:"Quatre questions rapides.",
       qs:[
         {q:"« Sortez les plateaux » est…", opts:["une consigne","une question"], ok:0,
          fb:"Le verbe est en premier : c'est une consigne."},
         {q:"La forme la plus employée au travail est…", opts:["-e","-ez"], ok:1,
          fb:"Elle sert pour « vous » et comme forme polie."},
         {q:"Le négatif se construit avec…", opts:["ne… pas autour du verbe","pas devant le verbe"], ok:0,
          fb:"« N'oubliez pas », « ne partez pas »."},
         {q:"L'impératif de « être » à la forme polie est…", opts:["soyez","êtes"], ok:0,
          fb:"« Soyez là à six heures. »"},
       ]},
    ]
  },

  t3aspect: {
    eye:'Mini-leçon', tit:'Fini, en cours, ou pas commencé',
    blocs:[
      {t:'texte', h:"Trois tournures qui disent où en est une tâche",
       p:"Quand le chef d'équipe demande « et les boîtes ? », il attend une réponse précise. Trois tournures suffisent : <b>je viens de</b> (fini à l'instant), <b>je suis en train de</b> (en cours), <b>je vais</b> (pas commencé, mais prévu). Elles se placent devant le verbe, qui ne change pas.",
       note:"Ces trois réponses rassurent, chacune à sa manière. La pire réponse est « oui » tout seul : personne ne sait ce qu'elle veut dire."},

      {t:'ana', h:"Juste avant : venir de",
       p:"L'action est terminée depuis une ou deux minutes.",
       mots:[['La forme','{Je viens de} finir.'],['Avec la tâche','{Je viens de} sortir les plateaux.'],['Encore plus court','{C’est fait.}',true]],
       say:"Je viens de finir les plateaux.",
       note:"« Je viens de » ne parle jamais d'hier : c'est tout juste avant, à la minute près."},

      {t:'ana', h:"Pendant : être en train de",
       p:"J'ai commencé, je n'ai pas fini, je le fais maintenant.",
       mots:[['La forme','{Je suis en train de} ranger.'],['Avec le détail','Il me reste {trois boîtes}.'],['Pour un appareil','Le lave-vaisselle {est en train de} laver.',true]],
       say:"Je suis en train de ranger les boîtes.",
       note:"Ajoute toujours ce qui reste : « il me reste trois boîtes ». Le chef d'équipe sait alors s'il doit envoyer quelqu'un."},

      {t:'ana', h:"Après : aller + infinitif",
       p:"Ce n'est pas commencé, mais c'est prévu, et je dis quand.",
       mots:[['La forme','{Je vais} éteindre le four.'],['Avec l’heure','{Je vais} le faire à onze heures.'],['Tout de suite après','{Je vais} commencer après ma pause.',true]],
       say:"Je vais éteindre le four à onze heures.",
       note:"Dis toujours quand. « Je vais le faire » sans heure ressemble à une façon de gagner du temps."},

      {t:'labo', h:"La même tâche, trois moments",
       p:"Choisis la tâche et son état.",
       axes:[
         {id:'t', lbl:'Quelle tâche ?', opts:[['a','les plateaux'],['b','les boîtes'],['c','le four']]},
         {id:'e', lbl:'Où en es-tu ?', opts:[['1','fini'],['2','en cours'],['3','à venir']]}],
       out:{
         a1:{w:["Je viens de finir les plateaux."], say:"Je viens de finir les plateaux.", n:'fini à l’instant'},
         a2:{w:["Je suis en train de sortir les plateaux."], say:"Je suis en train de sortir les plateaux.", n:'en cours'},
         a3:{w:["Je vais sortir les plateaux après ma pause."], say:"Je vais sortir les plateaux après ma pause.", n:'prévu, avec le moment'},
         b1:{w:["Les boîtes, c'est fait."], say:"Les boîtes, c'est fait.", n:'la réponse la plus courte'},
         b2:{w:["Je suis en train de les ranger, il en reste trois."], say:"Je suis en train de les ranger, il en reste trois.", n:'en cours, avec le reste'},
         b3:{w:["Je vais les ranger avant midi."], say:"Je vais les ranger avant midi.", n:'prévu, avec l’heure'},
         c1:{w:["Le four est éteint depuis onze heures."], say:"Le four est éteint depuis onze heures.", n:'fini, avec l’heure'},
         c2:{w:["Le four est en train de refroidir."], say:"Le four est en train de refroidir.", n:'en cours'},
         c3:{w:["Je vais éteindre le four à onze heures."], say:"Je vais éteindre le four à onze heures.", n:'prévu, avec l’heure'},
       },
       note:"Neuf réponses possibles à une seule question. Choisis celle qui est vraie : c'est tout ce qu'on te demande."},

      {t:'ex', h:"À écouter et à répéter",
       p:"Six réponses au chef d'équipe.",
       rows:[
         ["Je viens de finir les plateaux.","fini"],
         ["Les boîtes, c'est fait.","fini"],
         ["Je suis en train de les ranger.","en cours"],
         ["Il me reste trois boîtes.","en cours"],
         ["Je vais éteindre le four à onze heures.","à venir"],
         ["J'ai mis mon minuteur.","à venir"],
       ]},

      {t:'piege', h:"Trois pièges à connaître",
       rows:[
         ["conjuguer le verbe qui suit","« je viens de je finis »",
          "Après ces trois tournures, le verbe reste à l'infinitif : finir, ranger, éteindre."],
         ["répondre seulement « oui »","personne ne sait si c'est fait",
          "« Oui » ne dit pas si la tâche est finie ou commencée. Une des trois tournures règle la question."],
         ["employer « je viens de » pour hier","c'est seulement pour l'instant d'avant",
          "Pour hier, on dit « j'ai fini hier ». « Je viens de » veut dire : il y a une ou deux minutes."],
       ]},

      {t:'check', h:"Est-ce que c'est clair maintenant ?",
       p:"Quatre questions rapides.",
       qs:[
         {q:"« Je viens de finir » veut dire…", opts:["c'est fini à l'instant","je vais finir"], ok:0,
          fb:"L'action est terminée depuis une ou deux minutes."},
         {q:"« Je suis en train de ranger » veut dire…", opts:["c'est commencé, pas fini","c'est fini"], ok:0,
          fb:"L'action est en cours maintenant."},
         {q:"Après « je vais », le verbe est…", opts:["à l'infinitif","conjugué"], ok:0,
          fb:"Je vais éteindre, je vais ranger."},
         {q:"La réponse la plus courte pour une tâche terminée est…", opts:["c'est fait","oui"], ok:0,
          fb:"Trois mots, et la tâche est réglée."},
       ]},
    ]
  },
};
