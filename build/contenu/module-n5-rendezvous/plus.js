const PLUS = {

  // ════════════════════════════════════════════════════════════════════════
  prPhon: {
    eye:'Mini-leçon', tit:"« Une » et « vous » : deux sons que personne ne voit au téléphone",
    blocs:[
      {t:'texte', h:"Le seul mouvement à apprendre",
       p:"Le son de <b>une</b> et le son de <b>vous</b> se font tous les deux avec les lèvres arrondies. Ce n'est donc pas la bouche qui les sépare : c'est la <b>langue</b>. Dans « une », elle est poussée vers l'avant, contre les dents du bas. Dans « vous », elle recule au fond. Une seule chose bouge, et elle est invisible.",
       note:"C'est pour ça que ces deux sons résistent si longtemps : en face de vous, personne ne peut vous montrer ce qu'il fait. Au téléphone, personne ne voit même vos lèvres."},

      {t:'ana', h:"[y] — le son de « une », « minute », « sur »",
       p:"Il s'écrit toujours <b>u</b>, sans autre lettre après.",
       mots:[['La recette','dites « i », puis arrondissez les lèvres sans bouger la langue'],['On écrit','u',true],['Dans ce module','une minute · la durée · sur la carte · l\'urgence']],
       say:"Une minute, monsieur, je vérifie la durée du rendez-vous.",
       note:"Si vous partez de « ou » et que vous essayez d'avancer la langue, ça ne marche presque jamais. Partez de « i » : c'est le chemin court."},

      {t:'ana', h:"[u] — le son de « vous », « jour », « douze »",
       p:"Il s'écrit <b>ou</b>, deux lettres qui font un seul son.",
       mots:[['La recette','lèvres arrondies, langue reculée au fond'],['On écrit','ou',true],['Dans ce module','vous · un jour · douze heures · toujours']],
       say:"Vous serez à jeun douze heures avant, un jour de semaine.",
       note:"C'est souvent le son que les élèves produisent bien du premier coup. Le travail porte donc sur l'autre : tant que « u » sonne comme « ou », c'est [y] qu'il faut répéter."},

      {t:'ana', h:"Le mot du module qui contient les deux",
       p:"« Un rendez-vous » finit par [u]. « Une minute » commence par [y]. Ils se suivent dans presque tous les appels.",
       mots:[['D\'abord','un rendez-v-ous'],['Ensuite','u-ne minute',true],['À dire d\'un trait','une minute pour un rendez-vous']],
       say:"Une minute pour un rendez-vous, s'il vous plaît.",
       note:"Dites la phrase dix fois de suite, lentement, en surveillant la langue. C'est le meilleur exercice de tout le défi."},

      {t:'labo', h:"Écoutez les paires, une à la fois",
       p:"Chaque paire ne diffère que par un son. Choisissez-en une et écoutez-la dans sa phrase.",
       axes:[{id:'p', lbl:'Quelle paire ?', opts:[
         ['a','sûr / sourd'],
         ['b','la rue / la roue'],
         ['c','vu / vous'],
         ['d','dessus / dessous'],
         ['e','les deux sons dans la même phrase']]}],
       out:{
         a:{w:['sûr / sourd'], say:"Je suis sûr qu'il n'est pas sourd.", n:"langue en avant, puis langue en arrière"},
         b:{w:['la rue / la roue'], say:"La roue de l'auto est restée dans la rue.", n:"deux mots, deux objets : rien à voir l'un avec l'autre"},
         c:{w:['vu / vous'], say:"Je vous ai vu à la clinique hier.", n:"le premier est court, le second est rond"},
         d:{w:['dessus / dessous'], say:"La carte est dessus, pas dessous.", n:"c'est l'exemple qu'on entend le plus souvent au comptoir"},
         e:{w:['une minute / un rendez-vous'], say:"Une minute, je vous trouve un rendez-vous.", n:"la phrase de l'agente, avec les deux sons"},
       },
       note:"Écoutez chaque phrase deux fois : la première pour comprendre, la seconde en ne guettant que la voyelle."},

      {t:'ex', h:"À écouter et à répéter",
       p:"Six phrases prises dans les appels de ce module.",
       rows:[
         ["Une minute, je vérifie vos disponibilités.","trois fois [y]"],
         ["Vous serez à jeun douze heures avant.","trois fois [u]"],
         ["La durée du rendez-vous est de trente minutes.","[y] partout"],
         ["Le jour du rendez-vous, arrivez toujours quinze minutes avant.","[u] puis [y]"],
         ["Je suis sûr que c'est le jeudi, pas le mardi.","[y] au milieu de la phrase"],
         ["Vous pouvez me joindre au numéro sur la carte.","les deux, en alternance"],
       ]},

      {t:'piege', h:"Trois pièges de ces deux sons",
       rows:[
         ["dire « ou » pour « u »","« je suis sourd » pour « je suis sûr »",
          "C'est le piège principal : ce ne sont pas deux nuances d'un même mot, ce sont deux mots. Partez du son « i » et arrondissez, plutôt que de partir de « ou »."],
         ["prononcer le u de « qu »","« quinze » dit « ku-inze »",
          "Dans qu-, le u ne se prononce pas : quinze, quatre, quelque, question. Il est là pour la lettre q, rien de plus."],
         ["allonger le son","« uuune minute »",
          "Le français ne rallonge pas ses voyelles pour insister ; il déplace l'accent sur la dernière syllabe du groupe. « une miNUTE », et non « UUUne minute »."],
       ]},

      {t:'check', h:"Est-ce que c'est clair maintenant ?",
       p:"Quatre questions rapides.",
       qs:[
         {q:"Pour faire le son de « une », la langue est…", opts:["en avant","au fond"], ok:0,
          fb:"En avant, contre les dents du bas — comme pour « i »."},
         {q:"« vous », « jour », « douze » ont…", opts:["le son [y]","le son [u]"], ok:1,
          fb:"Ils s'écrivent tous avec ou : c'est le son de « vous »."},
         {q:"Dans « quinze », le u…", opts:["se prononce","ne se prononce pas"], ok:1,
          fb:"Il ne se prononce pas : qu- fait le son [k]."},
         {q:"La meilleure façon d'apprendre [y], c'est de partir de…", opts:["« ou »","« i »"], ok:1,
          fb:"On dit « i », puis on arrondit les lèvres sans bouger la langue."},
       ]},
    ]
  },

  // ════════════════════════════════════════════════════════════════════════
  prDuree: {
    eye:'Mini-leçon', tit:"Depuis quand ça dure — la question qu'on vous posera toujours",
    blocs:[
      {t:'texte', h:"Une seule réponse à préparer",
       p:"Que ce soit l'agente au téléphone, l'infirmière du 8-1-1 ou le médecin dans son bureau, tout le monde vous posera la même question dans les trente premières secondes : <b>depuis quand ?</b> C'est ce qui sépare un rhume d'un problème à examiner, et c'est ce qui décide de la durée du rendez-vous qu'on vous donnera.",
       note:"Préparez la réponse avant de composer : un chiffre et une unité. « Trois mois. » « Deux semaines. » « Depuis le mois de mars. » Rien d'autre n'est nécessaire à ce moment-là."},

      {t:'ana', h:"depuis — le plus utile des trois",
       p:"Le problème a commencé et il est encore là aujourd'hui.",
       mots:[['On l\'emploie avec','une date : depuis le mois de mars'],['ou avec','une durée : depuis trois mois',true],['Le verbe reste au','présent : j\'ai mal, je suis fatigué']],
       say:"J'ai des étourdissements depuis le mois de mars.",
       note:"Le présent est capital : « j'ai mal depuis trois mois » veut dire que ça continue. « J'ai eu mal » voudrait dire que c'est fini."},

      {t:'ana', h:"ça fait… que — la même chose, à l'oral",
       p:"On met la durée en tête pour la faire entendre. C'est la forme la plus fréquente au Québec.",
       mots:[['La structure','ça fait + durée + que + phrase'],['Un exemple','ça fait trois mois que ça dure',true],['À l\'écrit, préférez','depuis trois mois']],
       say:"Ça fait trois mois que ça dure, docteure.",
       note:"On entend aussi « voilà trois mois que… » et « il y a trois mois que… », plus rares. Retenez-en une seule et employez-la bien."},

      {t:'ana', h:"il y a — attention, ce n'est pas pareil",
       p:"Il situe un moment terminé dans le passé. Le verbe va alors au passé composé.",
       mots:[['Fini','ça a commencé il y a trois mois'],['Encore là','j\'ai mal depuis trois mois',true],['Jamais','j\'ai mal il y a trois mois']],
       say:"Ça a commencé il y a trois mois, un lundi matin.",
       note:"Le test : si vous pouvez ajouter « et c'est encore le cas aujourd'hui », c'est <b>depuis</b>. Sinon, c'est <b>il y a</b>."},

      {t:'labo', h:"La même situation, dite de quatre façons",
       p:"Choisissez une formulation et écoutez comment elle sonne.",
       axes:[{id:'f', lbl:'Quelle formulation ?', opts:[
         ['a','avec depuis + une date'],
         ['b','avec depuis + une durée'],
         ['c','avec ça fait… que'],
         ['d','avec il y a (le début)'],
         ['e','avec depuis que + une phrase']]}],
       out:{
         a:{w:['depuis le mois de mars'], say:"J'ai des étourdissements depuis le mois de mars.", n:"on donne le point de départ"},
         b:{w:['depuis trois mois'], say:"J'ai des étourdissements depuis trois mois.", n:"on donne la durée écoulée"},
         c:{w:['ça fait trois mois que'], say:"Ça fait trois mois que j'ai des étourdissements.", n:"la durée passe en tête, plus insistant"},
         d:{w:['il y a trois mois'], say:"Ça a commencé il y a trois mois.", n:"le verbe passe au passé composé"},
         e:{w:['depuis que'], say:"Depuis que j'ai changé d'horaire, je dors moins.", n:"le point de départ est un évènement, pas une date"},
       },
       note:"Les cinq disent la même chose. Choisissez-en deux et rendez-les automatiques : c'est plus utile que d'en connaître cinq à moitié."},

      {t:'ex', h:"À écouter et à répéter",
       p:"Six phrases pour la première minute d'un appel.",
       rows:[
         ["J'ai des étourdissements depuis le mois de mars.","depuis + une date"],
         ["Ça fait trois mois que ça dure.","ça fait… que"],
         ["Ça a commencé il y a trois mois.","il y a + passé composé"],
         ["Je suis fatigué depuis des semaines.","depuis + une durée vague"],
         ["Depuis que j'ai arrêté le sport, c'est pire.","depuis que + une phrase"],
         ["Au début, c'était une fois par semaine ; maintenant, c'est tous les matins.","ce qui a changé"],
       ]},

      {t:'piege', h:"Trois pièges de la durée",
       rows:[
         ["mettre le verbe au passé avec depuis","« j'ai eu mal depuis trois mois »",
          "Avec depuis, le verbe reste au présent tant que ça continue : « j'ai mal depuis trois mois ». Le passé composé ferait croire que c'est terminé."],
         ["employer il y a pour une chose qui dure","« j'ai mal il y a trois mois »",
          "il y a ne va qu'avec un fait terminé et daté : « ça a commencé il y a trois mois »."],
         ["répondre « longtemps »","« ça fait longtemps, docteure »",
          "Ça ne renseigne personne. Donnez un chiffre, même approximatif : « environ trois mois », « depuis le printemps »."],
       ]},

      {t:'check', h:"Est-ce que c'est clair maintenant ?",
       p:"Trois questions rapides.",
       qs:[
         {q:"« J'ai mal ___ trois mois » (ça continue) :", opts:["depuis","il y a"], ok:0,
          fb:"depuis + présent, parce que ça dure encore."},
         {q:"« Ça a commencé ___ trois mois » :", opts:["depuis","il y a"], ok:1,
          fb:"Un moment terminé et daté : il y a."},
         {q:"« Ça fait trois mois ___ ça dure » :", opts:["que","de"], ok:0,
          fb:"ça fait + durée + que."},
       ]},
    ]
  },

  // ════════════════════════════════════════════════════════════════════════
  t1temps: {
    eye:'Mini-leçon', tit:"Les sept mots qui placent un rendez-vous dans le temps",
    blocs:[
      {t:'texte', h:"Sept mots, et pas un de plus",
       p:"Un appel pour un rendez-vous se joue presque entièrement sur sept petits mots de temps. Les confondre ne rend pas la phrase fausse : ça vous fait manquer le rendez-vous, ou arriver le mauvais jour. C'est la différence entre « le résultat arrive <b>en</b> trois jours » et « le résultat arrive <b>dans</b> trois jours ».",
       note:"Apprenez-les par paires opposées, pas en liste : dans / d'ici, avant / à partir de, en / dans. C'est l'opposition qui se retient."},

      {t:'ana', h:"dans — un moment futur, compté depuis aujourd'hui",
       p:"Il annonce une date à venir.",
       mots:[['Structure','dans + une durée'],['Sens','à ce moment-là, pas avant',true],['Exemple','le rendez-vous est dans trois semaines']],
       say:"Le prochain rendez-vous libre est dans trois semaines.",
       note:"« dans trois semaines » ne veut pas dire « pendant les trois prochaines semaines ». C'est un point, pas une période."},

      {t:'ana', h:"d'ici — avant la fin du délai",
       p:"Il ouvre une fenêtre, alors que <b>dans</b> pose un point.",
       mots:[['Structure','d\'ici + un moment'],['Sens','à ce moment-là ou avant',true],['Exemple','vous aurez le résultat d\'ici vendredi']],
       say:"Vous aurez le résultat d'ici vendredi.",
       note:"Si on vous dit « d'ici vendredi » et que le résultat arrive le mercredi, tout est normal. « Dans trois jours » aurait promis jeudi."},

      {t:'ana', h:"avant et à partir de — les deux bornes",
       p:"L'un ferme, l'autre ouvre.",
       mots:[['avant','la limite : appelez avant quinze heures'],['à partir de','le début : ouvert à partir de sept heures quinze',true],['Ensemble','ouvert à partir de sept heures, fermé avant midi']],
       say:"La clinique ouvre à partir de sept heures quinze, et il faut annuler avant vingt-quatre heures.",
       note:"« avant vingt-quatre heures » veut dire « plus de vingt-quatre heures à l'avance », et non « avant minuit ». C'est un délai, pas une heure."},

      {t:'ana', h:"vers, pour, en — les trois autres",
       p:"Le premier approxime, le deuxième réserve, le troisième mesure.",
       mots:[['vers','approximatif : j\'arriverai vers dix-sept heures'],['pour + durée','ce qui est réservé : une plage pour trente minutes',true],['en + durée','le temps qu\'il faut : ça passe en dix secondes']],
       say:"J'arriverai vers seize heures quarante, pour une plage de trente minutes.",
       note:"Un rendez-vous n'est jamais « vers » : il est <b>à</b> dix-sept heures. Employez « vers » pour votre propre arrivée, jamais pour l'heure qu'on vous donne."},

      {t:'labo', h:"La même phrase, avec chaque mot",
       p:"Choisissez un mot et écoutez ce qu'il change au sens.",
       axes:[{id:'m', lbl:'Quel mot de temps ?', opts:[
         ['a','dans'],
         ['b','d\'ici'],
         ['c','avant'],
         ['d','à partir de'],
         ['e','en']]}],
       out:{
         a:{w:['dans trois jours'], say:"Vous aurez le résultat dans trois jours.", n:"jeudi, si on est lundi — un point précis"},
         b:{w:['d\'ici trois jours'], say:"Vous aurez le résultat d'ici trois jours.", n:"mardi, mercredi ou jeudi — une fenêtre"},
         c:{w:['avant trois jours'], say:"Vous aurez le résultat avant trois jours.", n:"la limite à ne pas dépasser"},
         d:{w:['à partir de jeudi'], say:"Vous aurez le résultat à partir de jeudi.", n:"pas avant jeudi — le début"},
         e:{w:['en trois jours'], say:"Le laboratoire donne le résultat en trois jours.", n:"c'est le temps que ça prend au laboratoire"},
       },
       note:"Cinq phrases presque identiques, cinq réalités différentes. C'est exactement le genre de nuance qui fait revenir quelqu'un pour rien."},

      {t:'ex', h:"À écouter et à répéter",
       p:"Six phrases de l'appel.",
       rows:[
         ["Le prochain rendez-vous libre est dans trois semaines.","dans"],
         ["Vous aurez le résultat d'ici vendredi.","d'ici"],
         ["Il faut annuler avant vingt-quatre heures.","avant"],
         ["La docteure reçoit à partir de sept heures quinze.","à partir de"],
         ["Je serai là vers seize heures quarante.","vers"],
         ["Je vous réserve une plage pour trente minutes.","pour + durée"],
       ]},

      {t:'piege', h:"Trois pièges de temps",
       rows:[
         ["confondre en et dans","« le résultat arrive en trois jours » / « dans trois jours »",
          "en trois jours = ça prend trois jours de travail. dans trois jours = ce sera jeudi. On peut vous dire les deux dans le même appel."],
         ["dire vers pour un rendez-vous","« mon rendez-vous est vers dix-sept heures »",
          "Un rendez-vous a une heure exacte. « vers » ne s'emploie que pour votre propre arrivée, ou pour une estimation qu'on vous donne."],
         ["lire avant vingt-quatre heures comme une heure","« avant minuit, alors ? »",
          "Non : plus de vingt-quatre heures avant le rendez-vous. Si le rendez-vous est jeudi à seize heures trente, la limite est mercredi à seize heures trente."],
       ]},

      {t:'check', h:"Est-ce que c'est clair maintenant ?",
       p:"Quatre questions rapides.",
       qs:[
         {q:"« Le résultat arrive dans trois jours » veut dire :", opts:["ce sera jeudi","ça prend trois jours de travail"], ok:0,
          fb:"dans pose un point futur : jeudi."},
         {q:"« d'ici vendredi » veut dire :", opts:["vendredi exactement","vendredi au plus tard"], ok:1,
          fb:"C'est une fenêtre : jeudi compte aussi."},
         {q:"« ouvert à partir de sept heures » veut dire :", opts:["fermé après sept heures","pas avant sept heures"], ok:1,
          fb:"à partir de ouvre la période."},
         {q:"Une plage réservée « pour trente minutes » :", opts:["dure trente minutes","commence dans trente minutes"], ok:0,
          fb:"pour + durée dit combien de temps est réservé."},
       ]},
    ]
  },

  // ════════════════════════════════════════════════════════════════════════
  t1futur: {
    eye:'Mini-leçon', tit:"Le futur simple, ou comment prendre un engagement",
    blocs:[
      {t:'texte', h:"Deux futurs, deux poids",
       p:"« Je vais venir jeudi » et « je viendrai jeudi » disent la même date. Mais le premier raconte une intention, et le second prend un engagement. Dans un appel avec une clinique — de part et d'autre — on prend des engagements : <b>je serai</b> là, <b>vous recevrez</b> un rappel, il <b>faudra</b> être à jeun.",
       note:"Le futur proche (aller + infinitif) reste correct et très courant au Québec. Ce que le niveau 5 ajoute, c'est de savoir aussi employer le futur simple, et de le reconnaître quand on vous l'adresse."},

      {t:'ana', h:"La formation : l'infinitif, puis six terminaisons",
       p:"Les mêmes six terminaisons pour tous les verbes, sans exception.",
       mots:[['Les terminaisons','-ai, -as, -a, -ons, -ez, -ont'],['Verbes en -er et -ir','arriver → j\'arriverai · finir → je finirai',true],['Verbes en -re','attendre → j\'attendrai (le e tombe)']],
       say:"J'arriverai quinze minutes avant, et j'attendrai à l'accueil.",
       note:"Le radical du futur finit toujours par un r. C'est le son qui signale le futur à l'oreille : arrive-R-ai, atten-d-R-ai."},

      {t:'ana', h:"Les irréguliers de l'appel",
       p:"Il y en a une dizaine, et ce sont justement ceux qu'on emploie ici.",
       mots:[['Les plus fréquents','être → je serai · avoir → j\'aurai · aller → j\'irai'],['Ceux du rendez-vous','falloir → il faudra · pouvoir → je pourrai · devoir → je devrai',true],['Deux autres','venir → je viendrai · recevoir → vous recevrez']],
       say:"Il faudra être à jeun, et vous recevrez un rappel la veille.",
       note:"Ils sont irréguliers au radical seulement : les terminaisons ne changent jamais. Apprenez « je serai, j'aurai, j'irai, il faudra » et vous couvrez la moitié des appels."},

      {t:'ana', h:"Qui l'emploie, et pour dire quoi",
       p:"Écoutez qui parle : c'est presque toujours la clinique.",
       mots:[['L\'agente annonce','vous recevrez un rappel automatisé'],['Elle prévient','ce sera un autre rendez-vous',true],['Elle impose','il faudra être à jeun douze heures avant']],
       say:"Vous recevrez un rappel automatisé la veille de votre rendez-vous.",
       note:"Chaque futur simple qu'on vous adresse est une consigne déguisée. Notez-les : ce sont eux qui disent ce qu'on attendra de vous."},

      {t:'labo', h:"Le même verbe, à six personnes",
       p:"Choisissez un verbe et écoutez-le dans une phrase de l'appel.",
       axes:[{id:'v', lbl:'Quel verbe ?', opts:[
         ['a','être'],
         ['b','avoir'],
         ['c','falloir'],
         ['d','recevoir'],
         ['e','aller']]}],
       out:{
         a:{w:['je serai · vous serez'], say:"Je serai là à seize heures quarante-cinq ; vous serez à jeun.", n:"le plus employé des deux côtés"},
         b:{w:['j\'aurai · elle aura'], say:"J'aurai ma carte avec moi ; elle aura les résultats jeudi.", n:"radical aur-"},
         c:{w:['il faudra'], say:"Il faudra arriver quinze minutes avant.", n:"une seule personne : il"},
         d:{w:['vous recevrez'], say:"Vous recevrez un rappel automatisé la veille.", n:"la phrase que dit toute clinique"},
         e:{w:['j\'irai · nous irons'], say:"J'irai au laboratoire lundi ; nous irons plus loin si ça continue.", n:"radical ir-"},
       },
       note:"Répétez chaque phrase en pensant à qui la dit : vous ou la clinique. Ça aide à retenir laquelle sert à quoi."},

      {t:'ex', h:"À écouter et à répéter",
       p:"Six phrases de la fin de l'appel.",
       rows:[
         ["Je serai à la clinique quinze minutes avant l'heure.","je serai"],
         ["Vous recevrez un rappel automatisé la veille.","vous recevrez"],
         ["Il faudra être à jeun douze heures avant.","il faudra"],
         ["J'apporterai ma carte et la liste de mes médicaments.","verbe régulier"],
         ["Je vous rappellerai dès que j'aurai mon nouvel horaire.","deux futurs dans la même phrase"],
         ["Si ça continue, nous irons plus loin.","irons"],
       ]},

      {t:'piege', h:"Trois pièges du futur",
       rows:[
         ["confondre -ai et -ais","« je serai » / « je serais »",
          "Les deux se prononcent pareil. -ai = ce qui est prévu. -ais = ce qui dépendrait d'une condition, ou une demande polie (« je voudrais »). Dans un courriel à une clinique, écrivez -ai."],
         ["oublier le r du radical","« je finirai » dit « je finerai »",
          "Le r est le signal du futur. Sans lui, on entend un présent ou un conditionnel mal formé."],
         ["employer le futur après si","« si je serai libre, je viendrai »",
          "Après si de condition, on met le présent : « si je suis libre, je viendrai ». Le futur va dans l'autre moitié de la phrase."],
       ]},

      {t:'check', h:"Est-ce que c'est clair maintenant ?",
       p:"Quatre questions rapides.",
       qs:[
         {q:"Le futur simple de « il faut » est :", opts:["il faudra","il faudrait"], ok:0,
          fb:"il faudra. « il faudrait » est un conditionnel."},
         {q:"« Vous recevrez un rappel » est dit par :", opts:["le patient","la clinique"], ok:1,
          fb:"C'est la clinique qui annonce ce qui va se passer."},
         {q:"« Si je ___ libre, je viendrai » :", opts:["serai","suis"], ok:1,
          fb:"Après si de condition : le présent."},
         {q:"Dans un courriel, « je ___ là à seize heures » s'écrit :", opts:["serai","serais"], ok:0,
          fb:"C'est un engagement : -ai."},
       ]},
    ]
  },

  // ════════════════════════════════════════════════════════════════════════
  t1fiche: {
    eye:'Mini-leçon', tit:"La fiche du rendez-vous : sept lignes, et un crayon",
    blocs:[
      {t:'texte', h:"Pourquoi on note, même quand on croit retenir",
       p:"Un appel de trois minutes contient sept renseignements. À la fin, on en retient trois — et on est persuadé de les avoir tous. Ce n'est pas un problème de mémoire, c'est un problème d'attention : pendant qu'on écoute la date, on prépare déjà la phrase suivante.",
       note:"La seule solution connue : un papier et un crayon posés à côté du téléphone <b>avant</b> de composer. Chercher un crayon pendant l'appel, c'est manquer la moitié de ce qui se dit."},

      {t:'ana', h:"Les sept lignes",
       p:"Écrivez-les d'avance, en colonne, et remplissez-les pendant l'appel.",
       mots:[['Le quand','la date, l\'heure du rendez-vous, l\'heure d\'arrivée'],['Le qui et le où','le nom du professionnel, l\'adresse ou l\'étage',true],['Le comment','ce qu\'il faut apporter, le délai d\'annulation']],
       say:"Jeudi 19 juin, dix-sept heures, arriver à seize heures quarante-cinq.",
       note:"Sept lignes, sept réponses. Si l'une reste vide à la fin de l'appel, c'est qu'il manque une question à poser."},

      {t:'ana', h:"La ligne qu'on oublie toujours : l'heure d'arrivée",
       p:"Elle n'est presque jamais celle du rendez-vous.",
       mots:[['Consultation ordinaire','quinze minutes avant'],['Premier rendez-vous','souvent trente minutes avant',true],['La conséquence','arriver à l\'heure exacte, c\'est arriver en retard']],
       say:"Présentez-vous quinze minutes avant, à l'accueil.",
       note:"Ces minutes servent à l'inscription : la carte, le dossier, la salle d'attente. Sans elles, votre rendez-vous commence en retard et finit trop tôt."},

      {t:'ana', h:"La ligne qui coûte de l'argent : le délai d'annulation",
       p:"Vingt-quatre heures dans la plupart des cliniques, quarante-huit dans certaines.",
       mots:[['On le demande','le jour où l\'on prend le rendez-vous'],['Pas','le jour où l\'on doit annuler',true],['La question','et si je ne peux plus venir ?']],
       say:"Et si je ne peux plus venir ? Quel est le délai d'annulation ?",
       note:"Personne ne vous donnera cette information de lui-même. C'est vous qui posez la question, au moment où tout va bien."},

      {t:'labo', h:"Les trois questions qu'on oublie",
       p:"Choisissez-en une et écoutez comment elle se pose.",
       axes:[{id:'q', lbl:'Quelle question ?', opts:[
         ['a','à quelle heure arriver'],
         ['b','quoi apporter'],
         ['c','faut-il être à jeun'],
         ['d','le délai d\'annulation'],
         ['e','tout confirmer à la fin']]}],
       out:{
         a:{w:['à quelle heure faut-il arriver ?'], say:"À quelle heure est-ce qu'il faut que j'arrive ?", n:"presque jamais la même heure que le rendez-vous"},
         b:{w:['qu\'est-ce que je dois apporter ?'], say:"Est-ce que je dois apporter quelque chose ?", n:"la carte, la liste des médicaments, parfois un papier"},
         c:{w:['est-ce que je dois être à jeun ?'], say:"Je voudrais savoir aussi si je dois être à jeun.", n:"non pour une consultation, oui pour bien des prélèvements"},
         d:{w:['et si je ne peux plus venir ?'], say:"Et si je ne peux plus venir, quel est le délai ?", n:"la question qui évite les frais d'absence"},
         e:{w:['c\'est bien ça ?'], say:"Jeudi 19 juin, dix-sept heures, arriver à seize heures quarante-cinq. C'est bien ça ?", n:"trente secondes qui évitent un déplacement pour rien"},
       },
       note:"Ces cinq phrases suffisent. Apprenez-les telles quelles : elles se réemploient à chaque appel, dans n'importe quelle clinique."},

      {t:'ex', h:"À écouter et à répéter",
       p:"Six phrases pour finir un appel proprement.",
       rows:[
         ["Un instant, je prends une feuille et un crayon.","à dire sans gêne"],
         ["À quelle heure est-ce qu'il faut que j'arrive ?","l'heure d'arrivée"],
         ["Est-ce que je dois apporter quelque chose ?","ce qu'il faut apporter"],
         ["Je voudrais savoir aussi si je dois être à jeun.","la préparation"],
         ["Et si je ne peux plus venir ?","le délai d'annulation"],
         ["Jeudi 19 juin, dix-sept heures. C'est bien ça ?","la confirmation"],
       ]},

      {t:'piege', h:"Trois pièges de fin d'appel",
       rows:[
         ["remercier avant d'avoir tout noté","« merci beaucoup, bonne journée ! »",
          "Le remerciement ferme l'appel. Tant qu'une ligne de la fiche est vide, on ne remercie pas : on pose la question qui manque."],
         ["confondre l'heure du rendez-vous et l'heure d'arrivée","noter « 17 h » et arriver à 17 h",
          "Notez les deux, sur deux lignes différentes. C'est la cause la plus fréquente de rendez-vous perdus."],
         ["ne pas répéter les chiffres","« oui, oui, c'est noté »",
          "Un chiffre mal entendu ne se rattrape jamais tout seul. Relisez la date, l'heure et le numéro à voix haute, et finissez par « c'est bien ça ? »."],
       ]},

      {t:'check', h:"Est-ce que c'est clair maintenant ?",
       p:"Trois questions rapides.",
       qs:[
         {q:"L'heure d'arrivée est en général :", opts:["la même que le rendez-vous","quinze minutes avant"], ok:1,
          fb:"Quinze minutes avant, souvent trente pour un premier rendez-vous."},
         {q:"Le délai d'annulation se demande :", opts:["quand on prend le rendez-vous","quand on doit annuler"], ok:0,
          fb:"Le jour où tout va bien — après, c'est trop tard."},
         {q:"La bonne dernière phrase d'un appel est :", opts:["« Merci, bonne journée. »","« … C'est bien ça ? »"], ok:1,
          fb:"On confirme, puis on remercie."},
       ]},
    ]
  },

  // ════════════════════════════════════════════════════════════════════════
  t2recit: {
    eye:'Mini-leçon', tit:"L'imparfait et le passé composé : le décor et l'évènement",
    blocs:[
      {t:'texte', h:"Ce que le niveau 5 vous demande vraiment",
       p:"Aux niveaux précédents, on décrivait : « j'ai mal à la tête ». Ici, on <b>raconte</b> : ce qui se passait avant, ce qui est arrivé, ce que ça donne aujourd'hui. Un récit tient sur deux temps du passé, et sur rien d'autre. L'imparfait plante le décor ; le passé composé fait avancer l'histoire.",
       note:"Un médecin écoute exactement ça. Une liste de symptômes le renseigne moins qu'un récit de trois phrases bien ordonné."},

      {t:'ana', h:"L'imparfait — ce qui durait, ce qui se répétait",
       p:"Pas de début ni de fin visibles : c'était comme ça.",
       mots:[['Formation','le nous du présent, sans -ons, + -ais, -ais, -ait, -ions, -iez, -aient'],['Un exemple','nous dorm-ons → je dormais',true],['Dans le récit','je me levais et tout tournait']],
       say:"Je me levais le matin et tout tournait pendant quelques secondes.",
       note:"Un seul verbe est irrégulier à l'imparfait : être → j'étais. Tous les autres suivent la règle du nous, y compris faire (nous fais-ons → je faisais)."},

      {t:'ana', h:"Le passé composé — ce qui est arrivé",
       p:"Un fait, une fois, souvent daté. C'est lui qui fait bouger le récit.",
       mots:[['Formation','avoir ou être au présent + participe passé'],['Avec avoir','j\'ai eu, j\'ai dû, j\'ai arrêté',true],['Avec être','je suis tombé, je me suis assis']],
       say:"La semaine dernière, j'ai dû m'asseoir par terre.",
       note:"Avec être, le participe s'accorde avec le sujet : elle est tombée, ils sont allés. Avec avoir, on n'y touche pas dans un récit oral."},

      {t:'ana', h:"Les verbes qui prennent être",
       p:"Le déplacement, le changement d'état, et tous les verbes pronominaux.",
       mots:[['Déplacement','aller, venir, entrer, sortir, monter, descendre, partir, arriver, tomber'],['Changement d\'état','naître, mourir, devenir, rester',true],['Pronominaux','se lever → je me suis levé · s\'asseoir → je me suis assis']],
       say:"Je suis tombé une fois, et je me suis assis par terre.",
       note:"En santé, ce sont justement les verbes utiles : tomber, se lever, s'asseoir, partir à l'urgence. Apprenez-les avec être dès le départ."},

      {t:'labo', h:"Une seule situation, quatre phrases",
       p:"Choisissez un moment du récit et écoutez le temps qu'il demande.",
       axes:[{id:'r', lbl:'Quel moment du récit ?', opts:[
         ['a','le début — quand ça a commencé'],
         ['b','le décor — ce qui se passait'],
         ['c','l\'évènement — ce qui est arrivé'],
         ['d','le changement — avant / maintenant'],
         ['e','les deux temps dans une phrase']]}],
       out:{
         a:{w:['ça a commencé'], say:"Ça a commencé au mois de mars.", n:"passé composé : un fait daté"},
         b:{w:['je me levais, tout tournait'], say:"Je me levais le matin et tout tournait.", n:"imparfait : ça se répétait"},
         c:{w:['j\'ai dû m\'asseoir'], say:"La semaine dernière, j'ai dû m'asseoir par terre.", n:"passé composé : une fois, datée"},
         d:{w:['c\'était / c\'est'], say:"Au début, c'était une fois par semaine ; maintenant, c'est tous les matins.", n:"imparfait pour avant, présent pour aujourd'hui"},
         e:{w:['je montais quand ça a tourné'], say:"Je montais l'escalier quand la tête m'a tourné.", n:"le décor est interrompu par l'évènement"},
       },
       note:"La cinquième est la structure du récit à elle seule : imparfait + quand + passé composé. Elle s'apprend par cœur."},

      {t:'ex', h:"À écouter et à répéter",
       p:"Six phrases du récit de Rachid.",
       rows:[
         ["Ça a commencé au mois de mars.","le début"],
         ["Je me levais et tout tournait pendant quelques secondes.","le décor"],
         ["Au début, c'était une fois par semaine.","la fréquence d'avant"],
         ["Maintenant, c'est presque tous les matins.","aujourd'hui"],
         ["La semaine dernière, j'ai dû m'asseoir par terre.","l'évènement"],
         ["Avant, je jouais au soccer ; j'ai arrêté en avril.","les deux temps"],
       ]},

      {t:'piege', h:"Trois pièges du récit",
       rows:[
         ["tout mettre au passé composé","« j'ai eu des étourdissements, j'ai été fatigué, j'ai arrêté »",
          "On perd le décor : plus rien ne dit ce qui durait. Le médecin entend trois évènements sans savoir lequel se répète."],
         ["oublier être avec les pronominaux","« je m'ai levé »",
          "Tous les verbes pronominaux prennent être : je me suis levé, je me suis assis, je me suis tenu."],
         ["employer l'imparfait pour une fois précise","« la semaine dernière, je devais m'asseoir »",
          "Une fois, datée : passé composé. « J'ai dû m'asseoir. » L'imparfait dirait que ça se répétait."],
       ]},

      {t:'check', h:"Est-ce que c'est clair maintenant ?",
       p:"Quatre questions rapides.",
       qs:[
         {q:"« Avant, je ___ au soccer tous les dimanches » :", opts:["jouais","ai joué"], ok:0,
          fb:"Une habitude passée : imparfait."},
         {q:"« La semaine dernière, j'___ m'asseoir » :", opts:["devais","ai dû"], ok:1,
          fb:"Une fois, datée : passé composé."},
         {q:"« Je ___ l'escalier quand la tête m'a tourné » :", opts:["montais","suis monté"], ok:0,
          fb:"Le décor interrompu : imparfait."},
         {q:"« Je ___ levé trop vite » :", opts:["me suis","m'ai"], ok:0,
          fb:"Les pronominaux prennent être."},
       ]},
    ]
  },

  // ════════════════════════════════════════════════════════════════════════
  t2ger: {
    eye:'Mini-leçon', tit:"Le gérondif : « en me levant », la réponse à « à quel moment ? »",
    blocs:[
      {t:'texte', h:"La question que tout médecin pose",
       p:"« Vous avez des étourdissements. » — « À quel moment ? » Ce n'est pas une question d'heure : c'est une question de <b>circonstance</b>. En vous levant ? En marchant ? En vous penchant ? La réponse à cette question fait souvent le diagnostic à elle seule, et elle se dit avec une seule forme : <b>en</b> + le verbe en <b>-ant</b>.",
       note:"Dans le dialogue, c'est exactement ce qui se passe : dès que Rachid dit « en me levant du lit » et « en montant l'escalier », la docteure sait quoi chercher."},

      {t:'ana', h:"La formation, en trois gestes",
       p:"Elle ne rate jamais : on part du <b>nous</b> du présent.",
       mots:[['1. On prend le nous','nous levons, nous montons, nous marchons'],['2. On enlève -ons, on met -ant','levant, montant, marchant',true],['3. On met en devant','en levant, en montant, en marchant']],
       say:"En montant l'escalier, j'ai eu un étourdissement.",
       note:"Trois verbes seulement échappent à la règle : être → en étant, avoir → en ayant, savoir → en sachant. Tous les autres, sans exception, suivent le nous."},

      {t:'ana', h:"Avec un verbe pronominal, le pronom reste",
       p:"C'est l'erreur la plus fréquente, et elle change le sens.",
       mots:[['je me lève','en me levant'],['vous vous levez','en vous levant',true],['il s\'assoit','en s\'assoyant']],
       say:"J'ai des étourdissements en me levant du lit.",
       note:"« En levant » voudrait dire que je lève quelque chose. « En me levant » veut dire que je me mets debout. Le petit mot change tout."},

      {t:'ana', h:"Deux emplois : le moment, et la manière",
       p:"Même forme, deux usages, et les deux servent ici.",
       mots:[['Le moment','en me levant = quand je me lève, au même instant'],['La manière','en comptant jusqu\'à dix = voilà comment faire',true],['Le conseil de la docteure','levez-vous en deux temps, en comptant jusqu\'à dix']],
       say:"Levez-vous en deux temps, en comptant jusqu'à dix.",
       note:"Quand un professionnel vous explique quoi faire, écoutez les gérondifs : ce sont eux qui portent la marche à suivre."},

      {t:'labo', h:"Quand est-ce que ça arrive ?",
       p:"Choisissez une circonstance et écoutez la phrase complète.",
       axes:[{id:'g', lbl:'Quelle circonstance ?', opts:[
         ['a','en me levant'],
         ['b','en montant l\'escalier'],
         ['c','en me penchant'],
         ['d','en travaillant'],
         ['e','la manière, pas le moment']]}],
       out:{
         a:{w:['en me levant'], say:"J'ai des étourdissements en me levant du lit.", n:"couché puis debout : la circonstance la plus utile à dire"},
         b:{w:['en montant l\'escalier'], say:"Ça m'arrive aussi en montant l'escalier avec mes seaux.", n:"à l'effort"},
         c:{w:['en me penchant'], say:"La tête me tourne en me penchant pour ramasser quelque chose.", n:"un autre mouvement, une autre piste"},
         d:{w:['en travaillant'], say:"Je suis fatigué même en travaillant assis.", n:"pendant une activité qui dure"},
         e:{w:['en comptant jusqu\'à dix'], say:"Levez-vous en deux temps, en comptant jusqu'à dix.", n:"ici, le gérondif dit comment faire"},
       },
       note:"Les quatre premières se disent au médecin ; la dernière, c'est lui qui vous la dit. Reconnaître les deux, c'est comprendre la moitié de la consultation."},

      {t:'ex', h:"À écouter et à répéter",
       p:"Six phrases du bureau.",
       rows:[
         ["J'ai des étourdissements en me levant du lit.","le moment"],
         ["Ça m'arrive aussi en montant l'escalier.","à l'effort"],
         ["Levez-vous en deux temps, en comptant jusqu'à dix.","la manière"],
         ["En appelant vingt-quatre heures à l'avance, on évite les frais.","la manière, encore"],
         ["En étant à jeun, le résultat est plus fiable.","un des trois irréguliers"],
         ["J'ai noté la date en écoutant l'agente.","deux choses en même temps"],
       ]},

      {t:'piege', h:"Trois pièges du gérondif",
       rows:[
         ["oublier le pronom","« en levant » pour « en me levant »",
          "Sans le pronom, ce n'est plus vous qui vous levez : vous levez quelque chose. Gardez me, te, se, nous, vous."],
         ["changer de sujet en cours de route","« en montant l'escalier, ma femme m'a appelé »",
          "Le gérondif et le verbe principal ont le même sujet. Si ce n'est pas le cas, il faut une vraie subordonnée : « pendant que je montais l'escalier, ma femme m'a appelé »."],
         ["confondre avec le participe présent seul","« montant l'escalier, j'ai eu… »",
          "Sans en, la forme existe mais appartient à l'écrit soutenu. À l'oral, on met toujours en."],
       ]},

      {t:'check', h:"Est-ce que c'est clair maintenant ?",
       p:"Quatre questions rapides.",
       qs:[
         {q:"Le gérondif se forme à partir du :", opts:["nous du présent","infinitif"], ok:0,
          fb:"nous levons → en levant."},
         {q:"« J'ai mal ___ du lit » :", opts:["en levant","en me levant"], ok:1,
          fb:"Le verbe est pronominal : le pronom reste."},
         {q:"« En comptant jusqu'à dix » dit :", opts:["le moment","la manière"], ok:1,
          fb:"Ici, c'est la façon de s'y prendre."},
         {q:"Le gérondif de « être » est :", opts:["en étant","en êtant"], ok:0,
          fb:"C'est l'un des trois irréguliers : en étant."},
       ]},
    ]
  },

  // ════════════════════════════════════════════════════════════════════════
  t2quest: {
    eye:'Mini-leçon', tit:"Poser ses questions : la moitié du rendez-vous qu'on oublie",
    blocs:[
      {t:'texte', h:"Sortir avec la moitié de ce qu'on est venu chercher",
       p:"Beaucoup de gens ressortent d'un rendez-vous sans savoir quand ils auront leurs résultats, ni ce qu'ils doivent faire si ça empire. Ce n'est presque jamais parce que le médecin a refusé de répondre : c'est parce que la question n'a pas été posée. Un rendez-vous se termine quand <b>vous</b> avez fini, pas quand le médecin a fini.",
       note:"Le niveau 5 attend un échange suivi. Écouter et répondre, c'est la moitié ; relancer et demander, c'est l'autre."},

      {t:'ana', h:"Les quatre questions à poser toujours",
       p:"Quel que soit le problème, ces quatre-là s'appliquent.",
       mots:[['1','qu\'est-ce que j\'ai, en mots simples ?'],['2','qu\'est-ce que je peux continuer de faire ?',true],['3','quand et comment j\'aurai les résultats ?'],['4','qu\'est-ce que je fais si ça empire ?']],
       say:"Quand est-ce que j'aurai les résultats, et comment ?",
       note:"Écrivez-les sur le même papier que la fiche du rendez-vous. Dans le bureau, on oublie tout : le papier, lui, n'oublie rien."},

      {t:'ana', h:"Faire répéter sans se sentir gêné",
       p:"Trois phrases qui n'offensent personne, et qui sauvent un rendez-vous.",
       mots:[['La plus simple','je m\'excuse, je n\'ai pas compris ce mot-là'],['La plus efficace','vous pouvez me le redire autrement ?',true],['Pour vérifier','donc, si je comprends bien, …']],
       say:"Je m'excuse, je n'ai pas compris ce mot-là. Vous pouvez me le redire autrement ?",
       note:"« Redire autrement » vaut mieux que « répéter » : répéter donne les mêmes mots, plus lentement. Vous voulez d'autres mots."},

      {t:'ana', h:"Reformuler : la technique qui vérifie tout d'un coup",
       p:"On redit avec ses propres mots ce qu'on a compris, et on laisse l'autre corriger.",
       mots:[['La formule','donc, si je comprends bien, …'],['Un exemple','assis au bord du lit, je compte jusqu\'à dix, puis debout',true],['La réponse attendue','exactement · pas tout à fait, en fait…']],
       say:"Donc, si je comprends bien : assis au bord du lit, je compte jusqu'à dix, puis debout.",
       note:"C'est ce que fait Rachid à la fin de la consultation. En vingt secondes, il vérifie une consigne qu'il aurait pu appliquer de travers pendant des semaines."},

      {t:'labo', h:"La question, et ce qu'elle rapporte",
       p:"Choisissez une question et écoutez comment elle se dit.",
       axes:[{id:'q', lbl:'Quelle question ?', opts:[
         ['a','comprendre le mot'],
         ['b','continuer sa vie'],
         ['c','les résultats'],
         ['d','si ça empire'],
         ['e','le suivi']]}],
       out:{
         a:{w:['ce que ça veut dire'], say:"Est-ce que vous pouvez m'expliquer ce que ça veut dire ?", n:"on demande d'autres mots, pas les mêmes"},
         b:{w:['travailler, bouger'], say:"Est-ce que je dois arrêter de travailler ?", n:"la vraie question de beaucoup de gens"},
         c:{w:['quand et comment'], say:"Quand est-ce que j'aurai les résultats, et comment ?", n:"un appel ? un courriel ? un rendez-vous ?"},
         d:{w:['si ça empire'], say:"Qu'est-ce que je fais si ça empire d'ici là ?", n:"la question qui évite une visite inutile à l'urgence — ou qui en provoque une nécessaire"},
         e:{w:['le rendez-vous d\'après'], say:"Est-ce que je dois reprendre un rendez-vous de suivi ?", n:"et qui doit le fixer : vous ou la clinique ?"},
       },
       note:"Cinq questions, à poser dans cet ordre. Elles tiennent en une minute et changent complètement ce qu'on emporte en sortant."},

      {t:'ex', h:"À écouter et à répéter",
       p:"Six phrases pour la fin d'une consultation.",
       rows:[
         ["Est-ce que vous pouvez m'expliquer ce que ça veut dire ?","faire expliquer"],
         ["Je m'excuse, je n'ai pas compris ce mot-là.","faire redire"],
         ["Donc, si je comprends bien, je me lève en deux temps.","reformuler"],
         ["Quand est-ce que j'aurai les résultats, et comment ?","les résultats"],
         ["Qu'est-ce que je fais si ça empire d'ici là ?","la consigne de sécurité"],
         ["J'ai deux questions avant de partir.","annoncer ses questions"],
       ]},

      {t:'piege', h:"Trois pièges du patient poli",
       rows:[
         ["dire oui sans avoir compris","« oui, oui, d'accord »",
          "C'est ce qui arrive le plus souvent, et personne ne s'en aperçoit dans le bureau. Le prix se paie ensuite : une consigne mal appliquée pendant des semaines."],
         ["garder ses questions pour la fin de la phrase du médecin","« … mais il était déjà debout »",
          "Annoncez-les d'avance : « j'ai deux questions avant de partir ». Le médecin garde alors le temps qu'il faut."],
         ["poser une question fermée quand on veut une explication","« c'est grave ? »",
          "On obtient « non » et rien d'autre. Demandez plutôt : « qu'est-ce que ça veut dire pour moi, concrètement ? »."],
       ]},

      {t:'check', h:"Est-ce que c'est clair maintenant ?",
       p:"Trois questions rapides.",
       qs:[
         {q:"Pour comprendre un mot, la meilleure phrase est :", opts:["« Vous pouvez répéter ? »","« Vous pouvez me le redire autrement ? »"], ok:1,
          fb:"Répéter donne les mêmes mots ; redire autrement en donne d'autres."},
         {q:"Reformuler, c'est :", opts:["redire avec ses propres mots pour vérifier","répéter exactement ce qui a été dit"], ok:0,
          fb:"Et on laisse l'autre corriger."},
         {q:"Les questions se posent :", opts:["quand le médecin a fini","annoncées d'avance, avant la fin"], ok:1,
          fb:"« J'ai deux questions avant de partir » réserve le temps."},
       ]},
    ]
  },

  // ════════════════════════════════════════════════════════════════════════
  t2mots: {
    eye:'Mini-leçon', tit:"Huit mots à reconnaître dans un bureau de médecin",
    blocs:[
      {t:'texte', h:"Reconnaître, pas réciter",
       p:"Personne ne vous demandera d'employer un vocabulaire médical. Ce qu'on vous demande, c'est de <b>reconnaître</b> huit ou dix mots quand ils passent dans une phrase — parce qu'ils portent une consigne. Manquer « à jeun », c'est refaire un déplacement pour rien.",
       note:"Le reste du vocabulaire, vous pouvez le décrire avec vos mots : « la tête qui tourne », « une piqûre dans le bras ». Ça suffit parfaitement."},

      {t:'ana', h:"Ce qu'on vous demande de décrire",
       p:"Trois mots qui ne veulent pas dire la même chose.",
       mots:[['un symptôme','ce que le corps montre'],['un étourdissement','la tête qui tourne, sans tomber',true],['une perte de connaissance','on tombe et on ne sait plus rien pendant un moment']],
       say:"Un étourdissement, ce n'est pas une perte de connaissance.",
       note:"La différence entre les deux derniers décide de tout : un étourdissement s'examine en clinique, une perte de connaissance envoie souvent à l'urgence."},

      {t:'ana', h:"Ce qu'on mesure",
       p:"Deux chiffres et un brassard.",
       mots:[['la tension artérielle','deux nombres : cent vingt sur quatre-vingts'],['le pouls','les battements par minute',true],['couché puis debout','on la prend deux fois pour comparer']],
       say:"Votre tension est de cent vingt sur quatre-vingts, couché.",
       note:"Quand un médecin prend la tension deux fois, dans deux positions, c'est qu'il cherche une baisse au lever. Vous pouvez le lui demander."},

      {t:'ana', h:"Ce qu'on vous prescrit, ce qu'on vous demande",
       p:"Quatre mots à ne pas manquer.",
       mots:[['une ordonnance','le papier signé qui autorise'],['une prise de sang','le prélèvement au bras',true],['à jeun','rien à manger, de l\'eau seulement'],['un rendez-vous de suivi','le rendez-vous d\'après, pour les résultats']],
       say:"Je vous fais l'ordonnance ; il faut que vous soyez à jeun.",
       note:"« À jeun » est le mot le plus coûteux de la liste : un prélèvement fait après un café se refait au complet, un autre matin."},

      {t:'labo', h:"Chaque mot dans sa phrase",
       p:"Choisissez un mot et écoutez la phrase où on l'entend vraiment.",
       axes:[{id:'m', lbl:'Quel mot ?', opts:[
         ['a','un symptôme'],
         ['b','la tension artérielle'],
         ['c','une ordonnance'],
         ['d','à jeun'],
         ['e','un bilan sanguin']]}],
       out:{
         a:{w:['un symptôme'], say:"Depuis combien de temps avez-vous ce symptôme ?", n:"ce que le corps montre"},
         b:{w:['la tension artérielle'], say:"Je vous prends la tension couché, puis debout.", n:"deux fois, pour comparer"},
         c:{w:['une ordonnance'], say:"Je vous fais l'ordonnance pour le prélèvement.", n:"le papier qui autorise l'examen"},
         d:{w:['à jeun'], say:"Il faut être à jeun : rien à manger douze heures avant.", n:"de l'eau seulement"},
         e:{w:['un bilan sanguin'], say:"Le bilan sanguin va vérifier votre fer et votre thyroïde.", n:"plusieurs analyses en une seule prise"},
       },
       note:"Écoutez chaque phrase deux fois, puis redites-la en remplaçant le mot par votre propre explication. C'est ainsi qu'il entre."},

      {t:'ex', h:"À écouter et à répéter",
       p:"Six phrases du bureau.",
       rows:[
         ["Depuis combien de temps avez-vous ce symptôme ?","le médecin demande"],
         ["Je vous prends la tension couché, puis debout.","ce qu'il fait"],
         ["Je vous fais une ordonnance pour la prise de sang.","ce qu'il prescrit"],
         ["Il faut être à jeun douze heures avant.","la consigne à ne pas manquer"],
         ["On se revoit dans trois semaines pour un suivi.","le rendez-vous d'après"],
         ["Je m'excuse, je n'ai pas compris ce mot-là.","votre phrase à vous"],
       ]},

      {t:'piege', h:"Trois pièges de vocabulaire",
       rows:[
         ["croire que « à jeun » permet le café","« juste un café, ça compte pas »",
          "Ça compte. À jeun veut dire de l'eau seulement — pas de café, pas de jus, pas de gomme. Un prélèvement raté se refait un autre matin."],
         ["confondre étourdissement et perte de connaissance","« je tombe dans les pommes »",
          "Les deux n'envoient pas au même endroit. Si vous n'êtes pas certain, décrivez : « je me tiens au mur, mais je sais toujours où je suis »."],
         ["employer un mot médical mal compris","« j'ai de l'hypotension »",
          "Si vous n'êtes pas sûr du mot, décrivez ce que vous ressentez. Un mot mal employé envoie le médecin sur une fausse piste."],
       ]},

      {t:'check', h:"Est-ce que c'est clair maintenant ?",
       p:"Trois questions rapides.",
       qs:[
         {q:"« À jeun » permet :", opts:["un café noir","de l'eau seulement"], ok:1,
          fb:"De l'eau seulement, pendant le nombre d'heures indiqué."},
         {q:"Le papier qui autorise un examen est :", opts:["une ordonnance","un bilan"], ok:0,
          fb:"L'ordonnance autorise ; le bilan est l'ensemble des analyses."},
         {q:"Prendre la tension couché puis debout sert à :", opts:["gagner du temps","comparer les deux positions"], ok:1,
          fb:"C'est la baisse au lever que le médecin cherche."},
       ]},
    ]
  },

  // ════════════════════════════════════════════════════════════════════════
  t3faut: {
    eye:'Mini-leçon', tit:"« Il faut que » et le subjonctif — et « faut que » à l'oral d'ici",
    blocs:[
      {t:'texte', h:"La forme de ce qui n'est pas négociable",
       p:"Une clinique fonctionne avec des obligations : être à jeun, arriver quinze minutes avant, annuler vingt-quatre heures d'avance. En français, quand cette obligation vise <b>quelqu'un en particulier</b>, elle se dit avec <b>il faut que</b> et un subjonctif : « il faut que <b>vous soyez</b> à jeun ».",
       note:"Le subjonctif fait peur pour rien. Au niveau 5, on n'en demande qu'une poignée de formes, toujours les mêmes, et toujours après il faut que."},

      {t:'ana', h:"La formation : le « ils » du présent",
       p:"On part du <b>ils</b>, on enlève <b>-ent</b>, on ajoute les terminaisons.",
       mots:[['Les terminaisons','-e, -es, -e, -ions, -iez, -ent'],['Un régulier','ils parl-ent → que je parle',true],['Un autre','ils prenn-ent → que je prenne, que nous prenions']],
       say:"Il faut que je prenne un rendez-vous de suivi.",
       note:"Pour nous et vous, on prend le radical de l'imparfait : que nous prenions, que vous preniez. C'est la seule irrégularité de la règle."},

      {t:'ana', h:"Les sept formes qu'on entend vraiment",
       p:"Apprenez celles-là et vous couvrez presque tout ce qui se dit en clinique.",
       mots:[['être et avoir','que je sois, que vous soyez · que j\'aie, que vous ayez'],['aller et faire','que j\'aille · que je fasse',true],['pouvoir, venir, savoir','que je puisse · que je vienne, que vous veniez · que je sache']],
       say:"Il faut que vous soyez à jeun, et que vous veniez quinze minutes avant.",
       note:"Sept verbes, et le reste suit la règle du ils. C'est un effort d'une soirée, pas d'un trimestre."},

      {t:'ana', h:"La chute du sujet, à l'oral du Québec",
       p:"Le <b>il</b> disparaît presque toujours en parlant.",
       mots:[['On écrit','il faut que je parte'],['On entend','faut que j\'parte',true],['On entend aussi','faudrait que vous appeliez avant']],
       say:"Faut que je parte, mon garçon est malade.",
       note:"Ce n'est ni une faute ni du relâchement : c'est la langue parlée d'ici. Reconnaissez-la à l'oreille, et remettez le <b>il</b> quand vous écrivez."},

      {t:'labo', h:"L'obligation, dite de cinq façons",
       p:"Choisissez une formulation et écoutez-la.",
       axes:[{id:'o', lbl:'Quelle formulation ?', opts:[
         ['a','il faut + infinitif (la règle générale)'],
         ['b','il faut que + subjonctif (quelqu\'un de précis)'],
         ['c','il faudrait que (plus doux)'],
         ['d','faut que (l\'oral d\'ici)'],
         ['e','devoir (plus neutre)']]}],
       out:{
         a:{w:['il faut arriver quinze minutes avant'], say:"Il faut arriver quinze minutes avant.", n:"la règle, pour tout le monde"},
         b:{w:['il faut que vous soyez à jeun'], say:"Il faut que vous soyez à jeun.", n:"c'est vous que ça vise"},
         c:{w:['il faudrait que je vienne plus tôt'], say:"Il faudrait que je vienne plus tôt.", n:"une obligation qu'on négocie encore"},
         d:{w:['faut que j\'y aille'], say:"Faut que j'y aille, je commence à sept heures.", n:"le il tombe : la langue parlée d'ici"},
         e:{w:['je dois arriver plus tôt'], say:"Je dois arriver plus tôt, ce jour-là.", n:"même sens, sans subjonctif"},
       },
       note:"Les cinq sont justes. Si le subjonctif vous bloque en pleine phrase, prenez « je dois » : personne ne vous en tiendra rigueur."},

      {t:'ex', h:"À écouter et à répéter",
       p:"Six phrases de clinique.",
       rows:[
         ["Il faut que vous soyez à jeun douze heures avant.","que vous soyez"],
         ["Il faut que je sois au travail à sept heures.","que je sois"],
         ["Il faudrait que nous prenions un rendez-vous de suivi.","que nous prenions"],
         ["Il faut que vous ayez votre carte avec vous.","que vous ayez"],
         ["Faut que j'aille chercher mon garçon.","l'oral d'ici"],
         ["Il faut arriver quinze minutes avant.","sans que : la règle générale"],
       ]},

      {t:'piege', h:"Trois pièges du subjonctif",
       rows:[
         ["mettre un indicatif après il faut que","« il faut que vous êtes à jeun »",
          "Après il faut que, toujours le subjonctif : que vous soyez. C'est la faute la plus visible."],
         ["employer que quand le sujet ne change pas","« il faut que j'arrive quinze minutes avant »",
          "Ce n'est pas faux, mais l'infinitif est plus simple et plus naturel : « il faut arriver quinze minutes avant »."],
         ["écrire faut que sans le il","« Faut que je déplace mon rendez-vous. »",
          "Parfait à l'oral, à éviter dans un courriel à une clinique. À l'écrit, on remet le il."],
       ]},

      {t:'check', h:"Est-ce que c'est clair maintenant ?",
       p:"Quatre questions rapides.",
       qs:[
         {q:"« Il faut que vous ___ à jeun » :", opts:["êtes","soyez"], ok:1,
          fb:"Après il faut que : le subjonctif."},
         {q:"« Faut que j'y aille » est :", opts:["une faute","de l'oral courant au Québec"], ok:1,
          fb:"Le il tombe à l'oral ; on le remet à l'écrit."},
         {q:"Le subjonctif se forme à partir du :", opts:["ils du présent","nous du présent"], ok:0,
          fb:"ils prenn-ent → que je prenne."},
         {q:"Quand le sujet ne change pas, on peut dire :", opts:["il faut + infinitif","il faut que + indicatif"], ok:0,
          fb:"« Il faut arriver quinze minutes avant. »"},
       ]},
    ]
  },

  // ════════════════════════════════════════════════════════════════════════
  t3pron: {
    eye:'Mini-leçon', tit:"Le, la, les, y, en — ne pas tout répéter",
    blocs:[
      {t:'texte', h:"Ce qui distingue un échange d'une suite de phrases",
       p:"« Je veux déplacer mon rendez-vous. Mon rendez-vous est le mardi 8. Je ne peux pas venir à mon rendez-vous. » Chacune de ces phrases est correcte, et l'ensemble ne ressemble à aucune conversation réelle. Ce qui manque, ce sont les <b>pronoms</b> : les petits mots qui reprennent ce qui vient d'être dit.",
       note:"Le programme du niveau 5 appelle ça la « reprise de l'information ». C'est ce qui transforme des phrases isolées en discours suivi."},

      {t:'ana', h:"le, la, les — une chose déjà nommée, sans préposition",
       p:"Ils remplacent un complément direct : on peut poser la question « quoi ? » après le verbe.",
       mots:[['le / l\'','j\'annule le rendez-vous → je l\'annule'],['la','je note la date → je la note',true],['les','j\'apporte mes médicaments → je les apporte']],
       say:"J'annule le rendez-vous. Je l'annule ce matin.",
       note:"Devant une voyelle, le et la deviennent l' : je l'annule, je l'ai noté. C'est automatique."},

      {t:'ana', h:"y — un lieu, ou « à + quelque chose »",
       p:"Un seul petit mot pour tout ce qui répond à « où ? » et à « à quoi ? ».",
       mots:[['Un lieu','je vais à la clinique → j\'y vais'],['À + chose','je pense à mon rendez-vous → j\'y pense',true],['Au passé','je suis allé à la clinique → j\'y suis allé']],
       say:"Je vais à la clinique jeudi. J'y vais en autobus.",
       note:"« y » ne remplace jamais une personne : « je pense à ma fille » → « je pense à elle », et non « j'y pense »."},

      {t:'ana', h:"en — « de + quelque chose », et les quantités",
       p:"Il reprend ce qui est introduit par <b>de</b>, ou ce qui est compté.",
       mots:[['De + chose','je parle de mes symptômes → j\'en parle'],['Une quantité','j\'ai trois médicaments → j\'en ai trois',true],['Un article indéfini','je veux un rendez-vous → j\'en veux un']],
       say:"J'ai deux questions à vous poser. J'en ai deux.",
       note:"Avec une quantité, le nombre reste à la fin : « j'en ai trois », « j'en veux un ». C'est la partie qu'on oublie le plus."},

      {t:'labo', h:"La même idée, avec et sans pronom",
       p:"Choisissez une phrase et écoutez les deux versions.",
       axes:[{id:'p', lbl:'Quelle phrase ?', opts:[
         ['a','le rendez-vous'],
         ['b','la clinique'],
         ['c','les symptômes'],
         ['d','les médicaments'],
         ['e','deux pronoms ensemble']]}],
       out:{
         a:{w:['je le déplace'], say:"Mon rendez-vous du mardi ? Je voudrais le déplacer.", n:"le remplace un complément direct"},
         b:{w:['j\'y vais'], say:"La clinique, j'y vais en autobus, ça prend vingt minutes.", n:"y remplace le lieu"},
         c:{w:['j\'en ai parlé'], say:"De mes étourdissements, j'en ai parlé à la docteure.", n:"en reprend « de + quelque chose »"},
         d:{w:['je les ai apportés'], say:"Mes médicaments ? Je les ai apportés, ils sont dans le sac.", n:"au passé composé, le pronom passe avant l'auxiliaire"},
         e:{w:['vous me le confirmez'], say:"La nouvelle heure, vous me la confirmez par courriel ?", n:"me d'abord, puis la"},
       },
       note:"Écoutez la première partie de chaque phrase : elle nomme la chose, et la seconde la reprend par un pronom. C'est exactement le mouvement à imiter."},

      {t:'ex', h:"À écouter et à répéter",
       p:"Six phrases d'un appel d'annulation.",
       rows:[
         ["Mon rendez-vous du mardi ? Je voudrais le déplacer.","le"],
         ["La clinique, j'y vais en autobus.","y"],
         ["De mes étourdissements, j'en ai parlé à la docteure.","en"],
         ["Mes médicaments, je les ai apportés.","les"],
         ["J'ai deux questions ; j'en ai deux, pas plus.","en + quantité"],
         ["La nouvelle heure, vous me la confirmez ?","deux pronoms"],
       ]},

      {t:'piege', h:"Trois pièges des pronoms",
       rows:[
         ["mettre le pronom après le verbe","« je annule le » pour « je l'annule »",
          "En français, le pronom passe devant le verbe. Ce n'est qu'à l'impératif affirmatif qu'il passe derrière : « annulez-le »."],
         ["mal placer le pronom au passé composé","« j'ai le noté »",
          "Le pronom passe avant l'auxiliaire : « je l'ai noté », « j'y suis allé », « j'en ai parlé »."],
         ["employer y pour une personne","« ma fille, j'y pense »",
          "y ne remplace jamais une personne : « je pense à elle »."],
       ]},

      {t:'check', h:"Est-ce que c'est clair maintenant ?",
       p:"Quatre questions rapides.",
       qs:[
         {q:"« Je vais à la clinique » → :", opts:["j'y vais","j'en vais"], ok:0,
          fb:"y remplace le lieu."},
         {q:"« J'ai parlé de mes symptômes » → :", opts:["je les ai parlé","j'en ai parlé"], ok:1,
          fb:"en reprend « de + quelque chose »."},
         {q:"Au passé composé, le pronom se place :", opts:["avant l'auxiliaire","entre l'auxiliaire et le participe"], ok:0,
          fb:"« je l'ai noté », « j'y suis allé »."},
         {q:"« J'ai trois médicaments » → :", opts:["j'en ai trois","je les ai trois"], ok:0,
          fb:"Avec une quantité : en, et le nombre reste."},
       ]},
    ]
  },

  // ════════════════════════════════════════════════════════════════════════
  t3etapes: {
    eye:'Mini-leçon', tit:"Déplacer, annuler, ne pas venir — et le message qu'on laisse",
    blocs:[
      {t:'texte', h:"Trois mots, trois conséquences",
       p:"<b>Déplacer</b>, c'est garder la démarche et changer le moment. <b>Annuler</b>, c'est rendre la place et rester libre d'en reprendre une. <b>Ne pas venir</b>, c'est laisser un créneau vide que personne n'a pu utiliser — et c'est la seule des trois qui se paie.",
       note:"Le mot que vous employez au téléphone décide de ce qui sera inscrit à votre dossier. Dites « déplacer » si vous voulez un autre rendez-vous : l'agente s'occupe alors de l'annulation elle-même."},

      {t:'ana', h:"Déplacer : trois choses à dire",
       p:"Dans cet ordre, et l'appel dure deux minutes au lieu de six.",
       mots:[['1. Quel rendez-vous','mon rendez-vous du mardi 8 juillet, à onze heures'],['2. Pourquoi','mon horaire de travail a changé',true],['3. Quand vous êtes libre','en fin de journée, ou très tôt le matin']],
       say:"Je vous appelle pour déplacer mon rendez-vous du mardi 8 juillet.",
       note:"La troisième est celle qu'on oublie. Sans elle, l'agente propose au hasard, vous refusez, elle repropose : c'est là que l'appel s'éternise."},

      {t:'ana', h:"Annuler à temps : le délai et le rappel",
       p:"Le rappel automatisé de la veille n'est pas un simple avis.",
       mots:[['Le délai courant','vingt-quatre heures avant le rendez-vous'],['Le rappel de la veille','le dernier moment utile pour appeler',true],['Après le délai','des frais d\'absence, dans bien des cliniques']],
       say:"J'annule plus de vingt-quatre heures à l'avance, il n'y a donc pas de frais.",
       note:"Quand vous recevez le rappel, posez-vous immédiatement la question : est-ce que je serai là ? C'est la dernière fenêtre gratuite."},

      {t:'ana', h:"Le message sur la boîte vocale : six éléments",
       p:"Personne ne peut vous rappeler pour vous faire répéter. Un message se réussit du premier coup ou pas du tout.",
       mots:[['Qui','votre nom et votre date de naissance'],['Quoi','la date et l\'heure du rendez-vous annulé, et avec qui',true],['Ensuite','ce que vous voulez, et un numéro répété deux fois']],
       say:"Bonjour, ici Rachid Benali, né le 4 novembre 1974. J'annule mon rendez-vous du jeudi 10 juillet à seize heures trente.",
       note:"Parlez plus lentement que d'habitude et détachez les chiffres. Une date de naissance mal comprise, et le message ne sert à rien."},

      {t:'labo', h:"Les six morceaux du message",
       p:"Choisissez un morceau et écoutez comment il se dit.",
       axes:[{id:'m', lbl:'Quel morceau ?', opts:[
         ['a','se nommer'],
         ['b','dire ce qu\'on annule'],
         ['c','dire pourquoi'],
         ['d','dire ce qu\'on veut ensuite'],
         ['e','laisser son numéro']]}],
       out:{
         a:{w:['nom et date de naissance'], say:"Bonjour, ici Rachid Benali, né le 4 novembre 1974.", n:"la date de naissance retrouve le bon dossier"},
         b:{w:['quel rendez-vous'], say:"J'annule mon rendez-vous du jeudi 10 juillet, à seize heures trente, avec la docteure Fongang.", n:"date, heure, professionnel"},
         c:{w:['la raison, brève'], say:"Mon garçon est malade et je dois rester avec lui.", n:"une phrase suffit — et elle évite d'être noté comme absent"},
         d:{w:['la suite'], say:"Je rappellerai demain matin pour en reprendre un autre.", n:"la démarche continue"},
         e:{w:['le numéro, deux fois'], say:"Vous pouvez me joindre au 450 555-0173. Je répète : 450 555-0173.", n:"répété, toujours"},
       },
       note:"Six morceaux, quarante secondes. Écrivez-les avant d'appeler : sur une boîte vocale, on n'a pas le droit à l'erreur."},

      {t:'ex', h:"À écouter et à répéter",
       p:"Six phrases pour déplacer ou annuler.",
       rows:[
         ["Je vous appelle pour déplacer mon rendez-vous du mardi 8 juillet.","déplacer"],
         ["Mon horaire de travail a changé : je finis à quinze heures.","la raison"],
         ["Je suis libre en fin de journée, ou très tôt le matin.","vos disponibilités"],
         ["J'annule mon rendez-vous du jeudi 10 juillet, à seize heures trente.","annuler"],
         ["Je rappellerai demain matin pour en reprendre un autre.","la suite"],
         ["Vous pouvez me joindre au 450 555-0173. Je répète : 450 555-0173.","le numéro"],
       ]},

      {t:'piege', h:"Trois pièges de l'annulation",
       rows:[
         ["dire « annuler » quand on veut « déplacer »","« j'annule mon rendez-vous » … puis silence",
          "Si vous voulez un autre rendez-vous, dites « déplacer » : la clinique annule l'ancien elle-même et vous en donne un nouveau dans le même appel."],
         ["attendre le jour même","« je vais appeler demain matin »",
          "Le délai court sur vingt-quatre heures. Un rendez-vous à seize heures trente jeudi s'annule au plus tard mercredi à seize heures trente."],
         ["laisser un message incomplet","« bonjour, je peux pas venir demain, merci »",
          "Ni nom, ni date de naissance, ni heure, ni numéro. Ce message ne permet d'annuler aucun rendez-vous, et l'absence sera notée."],
       ]},

      {t:'check', h:"Est-ce que c'est clair maintenant ?",
       p:"Quatre questions rapides.",
       qs:[
         {q:"Pour garder la démarche et changer la date, on dit :", opts:["annuler","déplacer"], ok:1,
          fb:"Déplacer : la clinique annule l'ancien elle-même."},
         {q:"Le rappel automatisé de la veille est :", opts:["un simple avis","la dernière fenêtre pour annuler sans frais"], ok:1,
          fb:"C'est le moment de se demander : est-ce que je serai là ?"},
         {q:"Dans un message d'annulation, il faut donner :", opts:["son nom seulement","nom, date de naissance, date et heure, numéro"], ok:1,
          fb:"Et le numéro répété deux fois."},
         {q:"Quand on déplace, il faut aussi dire :", opts:["quand on est libre","le nom de son employeur"], ok:0,
          fb:"Sans vos disponibilités, l'appel triple de longueur."},
       ]},
    ]
  },

};
