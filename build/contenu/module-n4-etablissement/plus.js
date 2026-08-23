const PLUS = {

  // ════════════════════════════════════════════════════════════════════════
  prPhon: {
    eye:'Mini-leçon', tit:"Les trois sons du nez : on, an, in",
    blocs:[
      {t:'texte', h:"Trois sons qui sortent par le nez, et qu'on entend partout",
       p:"Le français a des voyelles qui passent par le nez : l'air ne sort pas seulement par la bouche, il monte aussi derrière. On en compte trois qui servent tous les jours : celui de bonjour, celui d'absence et celui de matin. Beaucoup de langues n'en ont aucune, et beaucoup d'élèves les rendent toutes les trois par un seul son, ou ajoutent un petit « n » à la fin. Ni l'un ni l'autre ne s'entend en français : la consonne « n » ne se prononce pas, elle change seulement la voyelle qui la précède.",
       note:"Au téléphone, ces trois sons portent les nombres : un, cinq, vingt, cent, onze, cinquante. Un numéro mal nasalisé est un numéro qu'on ne rappellera pas."},

      {t:'ana', h:"Le son de « bonjour » : les lèvres en rond",
       p:"Avancez les lèvres et fermez-les presque, comme pour souffler sur une cuillère. La langue reste en arrière. C'est le son le plus fermé des trois.",
       mots:[["Écrit « on »","bonjour · un répondeur · composer · le nom · onze"],["Écrit « om »","le nombre · un compte · comprendre",true],["Dans le module","un abandon · nous répondons · le son"]],
       say:"Bonjour. Un répondeur. Un abandon.",
       note:"Le « n » ne se dit pas : « bonjour » n'a pas de consonne au milieu, seulement une voyelle qui passe par le nez. Si vous entendez un « n », c'est qu'il y en a trop."},

      {t:'ana', h:"Le son de « absence » : la bouche grande ouverte",
       p:"Laissez tomber la mâchoire, ouvrez large, et laissez l'air monter par le nez. C'est le son le plus ouvert des trois, et le plus fréquent en français.",
       mots:[["Écrit « an » ou « am »","avant · un an · la chambre · septembre"],["Écrit « en » ou « em »","une absence · un empêchement · un enfant · ensemble",true],["Dans le module","cent · en retard · comment · pendant"]],
       say:"Une absence. Un empêchement. Avant.",
       note:"« an » et « en » donnent exactement le même son : rien à l'oreille ne les sépare. C'est l'orthographe seule qui les distingue, et elle s'apprend mot par mot."},

      {t:'ana', h:"Le son de « matin » : les lèvres étirées",
       p:"Écartez les lèvres sur les côtés, comme au début d'un sourire, et laissez l'air monter. La bouche est ouverte, mais large plutôt que ronde.",
       mots:[["Écrit « in » ou « im »","le matin · impossible · un timbre · cinq"],["Écrit « ain » ou « ein »","la main · demain · plein · un train",true],["Écrit « en » après i","un examen · le bien · combien · rien"]],
       say:"Le matin. La main. Cinq.",
       note:"« demain » et « le matin » se terminent par le même son, écrit de deux façons. Ce sont les deux mots que vous direz le plus souvent dans un message : « je serai absente ce matin, je serai là demain »."},

      {t:'labo', h:"Écoutez les trois sons l'un après l'autre",
       p:"Choisissez une série et écoutez la différence, puis le mot replacé dans une phrase du module.",
       axes:[{id:'s', lbl:'Quelle série ?', opts:[
         ['a','bon · banc · bain'],
         ['b','son · sans · saint'],
         ['c','les mots du téléphone'],
         ['d','les nombres du numéro'],
         ['e','les trois motifs']]}],
       out:{
         a:{w:['un répondeur'], say:"Bon. Banc. Bain. Le répondeur du centre donne les heures d'ouverture.", n:"rond, ouvert, étiré — trois lèvres différentes"},
         b:{w:['une absence'], say:"Son. Sans. Saint. Une absence sans motif reste non justifiée.", n:"une seule consonne, trois nez"},
         c:{w:['la boîte vocale','le clavier'], say:"La boîte vocale. Le clavier. Composer le poste. Avant huit heures, c'est la boîte vocale qui répond.", n:"le son de bonjour deux fois, dans composer et dans poste"},
         d:{w:['les coordonnées'], say:"Un. Cinq. Onze. Vingt. Cent. Quatre cent cinquante, cinq cent cinquante-cinq.", n:"les nasales des nombres, celles qu'on doit dire lentement"},
         e:{w:['un retard','une absence','un abandon'], say:"Un retard. Une absence. Un abandon. Trois mots, trois cases dans le dossier.", n:"le seul mot sans nasale est retard — écoutez la différence"},
       },
       note:"Écoutez chaque série deux fois : la première pour entendre, la seconde en regardant vos lèvres dans une vitre ou dans l'écran du téléphone."},

      {t:'ex', h:"À écouter et à répéter",
       p:"Six phrases prises dans les dialogues du module.",
       rows:[
         ["Bonjour, ici Nourhane Ouazzani, groupe 6.","le son de bonjour, deux fois"],
         ["Je vous appelle pour signaler mon absence.","le son d'absence, deux fois"],
         ["Je serai en classe demain matin.","le son de matin, deux fois"],
         ["Composez le poste deux cent vingt-quatre.","les trois sons dans un seul nombre"],
         ["J'ai un empêchement ce matin, mais je viendrai demain.","ouvert, étiré, étiré"],
         ["Un abandon annoncé n'est pas un échec.","rond au début, ouvert à la fin"],
       ]},

      {t:'piege', h:"Trois pièges des voyelles du nez",
       rows:[
         ["ajouter un « n » qu'on entend","dire « bonn-jour » au lieu de « bonjour »",
          "La lettre « n » ne se prononce pas : elle indique seulement que la voyelle passe par le nez. Un « n » entendu au milieu du mot fait sonner le français comme une autre langue, et c'est le défaut le plus tenace."],
         ["rendre les trois sons pareils","dire « bon », « banc » et « bain » de la même façon",
          "Personne ne vous corrigera, mais on vous fera répéter votre numéro trois fois. Travaillez avec les lèvres avant de travailler avec l'oreille : rond, ouvert, étiré. Le geste vient avant le son."],
         ["croire que le son se lit dans les lettres","« en » se dit comme « an » dans absence, mais comme « in » dans examen",
          "L'orthographe française note trois sons avec plus de dix graphies. Il n'y a pas de règle courte : il faut écouter le mot une fois et le retenir avec son son, pas avec ses lettres."],
       ]},

      {t:'check', h:"Est-ce que c'est clair maintenant ?",
       p:"Quatre questions rapides.",
       qs:[
         {q:"Dans « bonjour », la lettre « n » se prononce…", opts:["oui, on l'entend","non, elle nasalise la voyelle"], ok:1,
          fb:"Non. Le « n » ne se dit pas : il fait passer la voyelle par le nez, rien de plus."},
         {q:"« Un empêchement » contient surtout…", opts:["le son d'absence","le son de matin"], ok:0,
          fb:"Le son d'absence, deux fois : em- et -ment. La bouche s'ouvre grand."},
         {q:"« Demain » et « le matin » se terminent…", opts:["par deux sons différents","par le même son"], ok:1,
          fb:"Par le même son, écrit « ain » d'un côté et « in » de l'autre."},
         {q:"Sur le son de bonjour, les lèvres sont…", opts:["étirées sur les côtés","avancées et arrondies"], ok:1,
          fb:"Avancées et arrondies, presque fermées. C'est le plus fermé des trois."},
       ]},
    ]
  },

  // ════════════════════════════════════════════════════════════════════════
  prMot: {
    eye:'Mini-leçon', tit:"Retard, absence, abandon : trois mots, trois cases",
    blocs:[
      {t:'texte', h:"Le centre ne choisit pas à votre place",
       p:"Quand vous téléphonez, la personne du secrétariat ouvre votre dossier et doit cocher quelque chose. Le système ne connaît que trois situations : vous venez plus tard, vous ne venez pas, vous ne revenez plus. Chacune porte un nom précis, et chacune déclenche des suites différentes — un rattrapage, une note à fournir, un formulaire de retrait. Dire « je ne peux pas venir » ne dit rien de tout cela, et oblige la personne à vous rappeler pour vous poser la question.",
       note:"Ces trois mots sont exactement ceux que le programme d'études nomme : justifier un retard, une absence ou un abandon. Ce ne sont pas trois synonymes, ce sont trois démarches."},

      {t:'ana', h:"Le retard : vous venez, mais après l'heure",
       p:"On parle de retard quand on finit par assister au cours. Dix minutes ou une heure et demie, c'est la même case ; ce qui change, c'est ce que vous aurez manqué.",
       mots:[["Ce qu'on dit au téléphone","Je serai en retard d'environ une demi-heure."],["Ce qu'on dit en entrant","Excusez-moi pour le retard, l'autobus n'est pas passé.",true],["Ce qu'on ne dit pas","Je vais peut-être être un peu en retard, on verra."]],
       say:"Un retard de dix minutes se signale aussi.",
       note:"Un retard annoncé d'avance ne se traite pas comme un retard découvert à la porte : dans le premier cas, l'enseignant garde vos feuilles ; dans le second, il a déjà fait la liste."},

      {t:'ana', h:"L'absence : vous ne venez pas du tout",
       p:"L'absence porte sur une journée entière ou sur plusieurs. Le centre veut la date — pas « aujourd'hui », mais « lundi le 14 » — et un motif en une phrase.",
       mots:[["Une journée","Je serai absente aujourd'hui, lundi le 14."],["Plusieurs jours","Je serai absente du 14 au 16 inclusivement.",true],["Une absence déjà passée","Je vous remets le papier qui justifie mon absence d'hier."]],
       say:"Son absence de lundi est inscrite au dossier.",
       note:"Dites la date même si vous appelez le matin même : le message est écouté deux heures plus tard, et « aujourd'hui » n'a plus de sens pour la personne qui l'entend."},

      {t:'ana', h:"L'abandon : vous arrêtez le cours",
       p:"C'est le seul des trois qui doive toujours passer par écrit, et le seul qui change quelque chose à votre relevé. Un abandon annoncé n'est pas un échec ; un cours qu'on cesse simplement de fréquenter, si.",
       mots:[["La phrase à écrire","Je vous écris pour abandonner le cours d'informatique du soir."],["La date d'effet","À partir du 1er octobre.",true],["Ce qui garde la porte ouverte","Je souhaiterais me réinscrire à la prochaine session."]],
       say:"Un abandon annoncé par écrit n'est pas un échec.",
       note:"Le mot fait peur et beaucoup d'élèves l'évitent. C'est pourtant lui qu'il faut employer : c'est le nom de la case, et le personnel l'entend dix fois par semaine sans y mettre aucun jugement."},

      {t:'ana', h:"L'empêchement : le mot poli pour tout le reste",
       p:"Quand la raison est privée, longue à expliquer, ou simplement qu'elle ne regarde personne, un seul mot suffit et personne ne demande la suite.",
       mots:[["Seul","J'ai un empêchement ce matin."],["Précisé sans être expliqué","J'ai un empêchement familial.",true],["Ce qu'il permet","de rester exact sans rien raconter"]],
       say:"Elle a téléphoné dès qu'elle a su qu'elle avait un empêchement.",
       note:"« Empêchement » n'est pas un mot vague : il dit qu'une chose extérieure vous empêche de venir. C'est reçu partout, au centre comme au travail."},

      {t:'labo', h:"Une situation, le mot juste, la phrase",
       p:"Choisissez une situation et écoutez comment elle se dit en une phrase.",
       axes:[{id:'c', lbl:'Quelle situation ?', opts:[
         ['a','l\'autobus n\'est pas passé'],
         ['b','votre enfant est malade'],
         ['c','vous arrêtez le cours du soir'],
         ['d','la raison est privée'],
         ['e','vous partez avant la fin']]}],
       out:{
         a:{w:['un retard'], say:"J'aurai environ une heure de retard à cause de l'autobus.", n:"un retard : vous venez quand même"},
         b:{w:['une absence','un motif'], say:"Je serai absente aujourd'hui parce que mon fils est malade.", n:"une absence : la date, puis le motif"},
         c:{w:['un abandon'], say:"Je vous écris pour abandonner le cours d'informatique du soir.", n:"un abandon : toujours par écrit"},
         d:{w:['un empêchement'], say:"J'ai un empêchement familial ce matin.", n:"un empêchement : exact, et rien de plus"},
         e:{w:['un retard'], say:"Je devrai quitter à onze heures pour un rendez-vous.", n:"un départ avant la fin, annoncé d'avance"},
       },
       note:"Écoutez chaque phrase deux fois, puis redites-la sans regarder. Ce sont cinq phrases toutes faites : elles vous serviront telles quelles."},

      {t:'ex', h:"À écouter et à répéter",
       p:"Six phrases à dire au téléphone sans hésiter.",
       rows:[
         ["Je serai absente aujourd'hui, lundi le 14.","la date après le mot"],
         ["J'aurai une heure de retard à cause de la tempête.","un nom après « à cause de »"],
         ["J'ai un empêchement familial ce matin.","court, et personne ne demande la suite"],
         ["Je vous écris pour abandonner le cours du soir.","le mot exact, à l'écrit"],
         ["Je devrai quitter le cours à onze heures.","un départ annoncé d'avance"],
         ["Je vous remets le papier qui justifie mon absence.","le papier arrive après l'absence"],
       ]},

      {t:'piege', h:"Trois pièges des motifs",
       rows:[
         ["dire « je ne peux pas venir »","le secrétariat ne sait pas quoi cocher",
          "Ni la durée, ni la nature. La personne devra vous rappeler, et vous n'aurez rien gagné. Nommez la case : retard, absence, abandon."],
         ["raconter le détail","trois minutes de message pour une otite",
          "La boîte vocale coupe, la personne qui écoute a quarante messages, et l'essentiel se perd dans le milieu. Une phrase, une seule, et on passe à la suite."],
         ["éviter le mot « abandon »","« je pense que je ne continuerai pas »",
          "Ce n'est pas une annonce, c'est une hésitation, et rien ne sera inscrit. Tant que le mot n'est pas écrit, le cours continue de vous compter absente chaque soir."],
       ]},

      {t:'check', h:"Est-ce que c'est clair maintenant ?",
       p:"Quatre questions rapides.",
       qs:[
         {q:"Vous arriverez à neuf heures au lieu de huit. C'est…", opts:["un retard","une absence"], ok:0,
          fb:"Un retard : vous assistez au cours, mais après l'heure."},
         {q:"Lequel des trois doit toujours passer par écrit ?", opts:["le retard","l'abandon"], ok:1,
          fb:"L'abandon. Sans écrit, il s'inscrit comme un échec."},
         {q:"« J'ai un empêchement » veut dire…", opts:["je ne veux pas venir","quelque chose m'empêche de venir"], ok:1,
          fb:"Quelque chose vous en empêche. C'est exact et poli, et personne ne demande quoi."},
         {q:"Dans un message laissé le matin, il faut dire…", opts:["« aujourd'hui » suffit","la date exacte"], ok:1,
          fb:"La date exacte : le message est écouté deux heures plus tard."},
       ]},
    ]
  },

  // ════════════════════════════════════════════════════════════════════════
  pr1: {
    eye:'Mini-leçon', tit:"Pourquoi le centre est fermé quand vous appelez",
    blocs:[
      {t:'texte', h:"Une heure de décalage, et tout le module en découle",
       p:"Dans un centre d'éducation des adultes, le cours de jour commence à huit heures et le secrétariat ouvre à huit heures aussi. Or une absence se décide plus tôt : quand l'enfant est malade, quand l'autobus ne passe pas, quand le réveil n'a pas sonné. À sept heures, il n'y a personne. Ce n'est pas une mauvaise organisation, c'est la situation normale de tous les centres — et c'est exactement pour cela que la boîte vocale existe et qu'elle est relevée dès l'ouverture.",
       note:"Le module entier tient dans ce décalage : on parle à une machine parce qu'il n'y a personne, et on écrit une note parce que la machine ne garde rien de signé."},

      {t:'ana', h:"Ce qu'un message enregistré vaut, et ce qu'il ne vaut pas",
       p:"Il vaut une parole : il est écouté, il est inscrit au dossier, il compte comme un avertissement donné à temps. Il ne vaut pas une signature : rien de ce qui doit être prouvé ne se règle par téléphone.",
       mots:[["Ce que le message règle","le fait d'avoir prévenu · l'heure à laquelle vous avez prévenu"],["Ce qu'il ne règle pas","la justification · l'abandon · toute demande officielle",true],["Ce qui suit toujours","une note écrite, signée, remise au comptoir"]],
       say:"Avant huit heures, c'est la boîte vocale qui répond.",
       note:"Beaucoup d'élèves croient l'affaire close après l'appel, et découvrent trois semaines plus tard une absence non motivée à leur dossier. L'appel est la première moitié, jamais la seconde."},

      {t:'ana', h:"À qui parle-t-on, dans un centre",
       p:"Trois personnes, trois rôles, et on ne les interchange pas.",
       mots:[["L'enseignant","le cours, le rattrapage, les feuilles gardées"],["Le secrétariat","le dossier, les absences, les papiers officiels",true],["La conseillère","le parcours, le groupe, l'inscription"]],
       say:"Le secrétariat, c'est le poste 224 du centre.",
       note:"Prévenir seulement l'enseignant n'est pas une faute, mais rien n'entre au dossier : c'est le secrétariat qui écrit. Prévenir les deux est ce que font les élèves d'expérience."},

      {t:'labo', h:"Qui appelez-vous, selon ce que vous voulez",
       p:"Choisissez ce que vous avez à régler et écoutez à qui il faut s'adresser.",
       axes:[{id:'q', lbl:'Vous voulez…', opts:[
         ['a','signaler une absence'],
         ['b','savoir ce qui a été fait en classe'],
         ['c','faire justifier l\'absence au dossier'],
         ['d','abandonner un cours'],
         ['e','savoir si vous êtes inscrite quelque part']]}],
       out:{
         a:{w:['la boîte vocale'], say:"Le secrétariat, par la boîte vocale si c'est avant huit heures.", n:"le dossier, c'est le secrétariat"},
         b:{w:['un message'], say:"L'enseignant, par un message ou en classe le lendemain.", n:"le cours, c'est l'enseignant"},
         c:{w:['une note'], say:"Le secrétariat, avec une note écrite et signée.", n:"la preuve se remet en personne"},
         d:{w:['un abandon'], say:"Le secrétariat, par écrit, avant la fin du mois.", n:"un abandon ne se dit jamais seulement de vive voix"},
         e:{w:['un poste'], say:"Le secrétariat, au poste 224, pendant les heures d'ouverture.", n:"tout ce qui touche au dossier passe par là"},
       },
       note:"Quatre fois sur cinq, la réponse est le secrétariat. Ce n'est pas un hasard : c'est le seul endroit du centre où l'on écrit dans votre dossier."},

      {t:'ex', h:"À écouter et à répéter",
       p:"Cinq phrases entendues dans le corridor.",
       rows:[
         ["Le bureau ouvre à huit heures, comme le cours.","le décalage, en une phrase"],
         ["Tu laisses ton message et ça compte pareil.","ce que dit Wilner"],
         ["Elle écoute tout à huit heures et elle écrit dans le dossier.","ce que fait le secrétariat"],
         ["Ton nom, ton groupe, la date. Lentement, au début.","les trois choses à ne pas rater"],
         ["Ce qui fait long, c'est de raconter l'otite.","ce qu'il faut couper"],
       ]},

      {t:'piege', h:"Trois pièges du premier appel",
       rows:[
         ["attendre l'ouverture pour appeler","téléphoner à huit heures cinq, quand le cours est commencé",
          "Le message laissé à sept heures dix arrive avant tout le monde et prouve que vous avez prévenu avant l'heure du cours. Appeler après, c'est prévenir en retard."],
         ["croire que l'appel suffit","ne jamais remettre de note",
          "L'appel dit que vous avez prévenu ; la note dit pourquoi. Sans la seconde, l'absence reste au dossier comme non motivée, et personne ne vous préviendra."],
         ["parler trop vite au début","donner son nom en deux secondes",
          "C'est la partie que la personne doit écrire, et c'est celle qu'on dit le plus vite parce qu'on la connaît par cœur. Ralentissez sur le nom et le groupe ; accélérez sur le reste si vous voulez."],
       ]},

      {t:'check', h:"Est-ce que c'est clair maintenant ?",
       p:"Quatre questions rapides.",
       qs:[
         {q:"À sept heures dix, qui répond au centre ?", opts:["la boîte vocale","le secrétariat"], ok:0,
          fb:"La boîte vocale. Le bureau n'ouvre qu'à huit heures."},
         {q:"Un message laissé sur la boîte vocale…", opts:["ne compte pas","est écouté et inscrit au dossier"], ok:1,
          fb:"Il est écouté dès l'ouverture et inscrit au dossier."},
         {q:"Pour faire justifier une absence, il faut…", opts:["une note écrite et signée","un deuxième appel"], ok:0,
          fb:"Une note écrite et signée, remise au comptoir."},
         {q:"Qui garde vos feuilles pendant votre absence ?", opts:["le secrétariat","l'enseignant"], ok:1,
          fb:"L'enseignant : le cours, c'est lui. Le dossier, c'est le secrétariat."},
       ]},
    ]
  },

  // ════════════════════════════════════════════════════════════════════════
  t1a: {
    eye:'Mini-leçon', tit:"Les cinq morceaux d'un message d'une minute",
    blocs:[
      {t:'texte', h:"Un message n'est pas une conversation coupée en deux",
       p:"Dans une conversation, on peut commencer n'importe où : l'autre pose des questions et remet les choses en ordre. Dans un message, personne ne pose de question. Tout doit sortir dans le bon ordre, du premier coup, et cet ordre n'est pas celui de la pensée. On pense d'abord à l'otite, à l'inquiétude, au rendez-vous ; on doit dire d'abord son nom, son groupe et la date. Apprendre l'ordre, c'est tout ce qu'il y a à apprendre — le reste, vous le savez déjà.",
       note:"Cinquante secondes suffisent largement pour les cinq morceaux. Ce qui fait déborder un message, ce n'est jamais l'information : c'est l'explication."},

      {t:'ana', h:"Les trois premiers morceaux : qui, quoi, pourquoi",
       p:"Ils tiennent en trois phrases, et ce sont les trois que la personne écrit sur son papier pendant qu'elle écoute.",
       mots:[["1. Qui vous êtes","Bonjour, ici Nourhane Ouazzani, groupe 6, francisation de jour."],["2. Pourquoi vous appelez, avec la date","Je vous appelle pour signaler mon absence aujourd'hui, lundi le 14.",true],["3. Le motif, une phrase","Mon fils a une otite et j'ai un rendez-vous à la clinique."]],
       say:"Bonjour, ici Nourhane Ouazzani, groupe 6, francisation de jour.",
       note:"Le nom vient avant tout, et il se dit lentement. Si votre nom est long ou peu courant ici, épelez-le : « O, U, A, deux Z, A, N, I »."},

      {t:'ana', h:"Les deux derniers : ce que vous ferez, et comment vous joindre",
       p:"Ce sont les deux morceaux qu'on oublie le plus, et ce sont ceux qui évitent le rappel.",
       mots:[["4. Ce que vous ferez ensuite","Je serai en classe demain matin et je remettrai le papier jeudi."],["5. Vos coordonnées, deux fois","Vous pouvez me rappeler au 450 555-0147. Je répète : 450 555-0147.",true],["La formule de fin","Merci beaucoup. Bonne journée."]],
       say:"Elle a laissé ses coordonnées deux fois, lentement.",
       note:"Un numéro se dit par groupes de trois ou quatre chiffres, avec une pause : « quatre cent cinquante… cinq cent cinquante-cinq… zéro un quarante-sept »."},

      {t:'labo', h:"Le même message, morceau par morceau",
       p:"Choisissez un morceau et écoutez-le seul, à la vitesse où il doit être dit.",
       axes:[{id:'m', lbl:'Quel morceau ?', opts:[
         ['a','1 · qui vous êtes'],
         ['b','2 · pourquoi, avec la date'],
         ['c','3 · le motif'],
         ['d','4 · ce que vous ferez'],
         ['e','5 · le numéro, deux fois']]}],
       out:{
         a:{w:['un message'], say:"Bonjour, ici Nourhane Ouazzani, groupe 6, francisation de jour.", n:"lentement : c'est ce qu'on écrit"},
         b:{w:['une absence'], say:"Je vous appelle pour signaler mon absence aujourd'hui, lundi le 14.", n:"le mot du motif, puis la date"},
         c:{w:['un motif'], say:"Mon fils a une otite et j'ai un rendez-vous à la clinique.", n:"une phrase, et on passe"},
         d:{w:['une note'], say:"Je serai en classe demain matin et je remettrai le papier jeudi.", n:"le futur : vous revenez, le dossier se referme"},
         e:{w:['les coordonnées'], say:"Vous pouvez me rappeler au 450 555-0147. Je répète : 450 555-0147.", n:"par groupes, avec une pause"},
       },
       note:"Écoutez les cinq à la suite une fois, puis essayez de les redire de mémoire dans l'ordre. C'est l'ordre qu'il faut retenir, pas les mots."},

      {t:'ex', h:"À écouter et à répéter",
       p:"Six débuts de message, tous corrects.",
       rows:[
         ["Bonjour, ici Wilner Céleste, groupe 6.","le nom, puis le groupe"],
         ["Je vous appelle pour signaler un retard ce matin.","le mot du motif, tout de suite"],
         ["Je serai absente les 14 et 15 septembre.","deux dates, dites clairement"],
         ["Je vous rappelle au sujet de mon absence de lundi.","quand vous répondez à un message"],
         ["Je serai en classe demain matin, sans faute.","la promesse, au futur"],
         ["Vous pouvez me joindre au 450 555-0147.","le numéro, avant de raccrocher"],
       ]},

      {t:'piege', h:"Trois pièges du message enregistré",
       rows:[
         ["commencer par la raison","« Mon fils est malade… » avant même de se nommer",
          "La personne écoute trente secondes sans savoir de qui il s'agit, puis doit tout réécouter. Le nom d'abord, toujours."],
         ["dire « aujourd'hui » sans la date","« Je serai absente aujourd'hui »",
          "Le message est écouté deux heures plus tard, parfois le lendemain si vous avez appelé le soir. La date exacte lève tout doute."],
         ["oublier le numéro","terminer par « merci, bonne journée »",
          "S'il manque quelque chose à votre message, personne ne peut vous le demander. Le numéro est ce qui rend le message réparable."],
       ]},

      {t:'check', h:"Est-ce que c'est clair maintenant ?",
       p:"Quatre questions rapides.",
       qs:[
         {q:"Par quoi commence un message au secrétariat ?", opts:["par la raison de l'absence","par votre nom et votre groupe"], ok:1,
          fb:"Par votre nom et votre groupe. C'est ce que la personne écrit en premier."},
         {q:"Combien de phrases pour le motif ?", opts:["une","autant qu'il en faut"], ok:0,
          fb:"Une seule. Le détail ne sert à personne et fait déborder le message."},
         {q:"Le numéro de téléphone se dit…", opts:["une fois, à la fin","deux fois, lentement"], ok:1,
          fb:"Deux fois, par groupes de chiffres. C'est ce qui rend le rappel possible."},
         {q:"Quel morceau dit que le dossier va se refermer ?", opts:["le motif","ce que vous ferez ensuite"], ok:1,
          fb:"Ce que vous ferez ensuite : le retour, le papier, le rattrapage."},
       ]},
    ]
  },

  // ════════════════════════════════════════════════════════════════════════
  t1imper: {
    eye:'Mini-leçon', tit:"L'impératif : la langue des répondeurs",
    blocs:[
      {t:'texte', h:"Un verbe sans sujet, et tout le monde comprend",
       p:"L'impératif sert à dire à quelqu'un de faire quelque chose sans le nommer. C'est la forme la plus courte du français : un verbe, et c'est tout. Tous les menus téléphoniques du Québec sont écrits ainsi — appuyez, composez, faites, laissez, restez, raccrochez —, et toutes les consignes de classe aussi. Le reconnaître, c'est comprendre les cinq phrases qui donnent accès à n'importe quel service. L'employer, c'est pouvoir demander quelque chose poliment quand on ajoute « s'il vous plaît ».",
       note:"Trois formes existent — tu, nous, vous — mais dans ce module une seule sert : celle de « vous ». C'est celle du répondeur, celle du secrétariat, et celle qu'on emploie avec quelqu'un qu'on vouvoie."},

      {t:'ana', h:"La forme : on enlève le pronom, rien de plus",
       p:"On part du présent avec « vous » et on retire le mot « vous ». Aucune autre modification, aucune exception dans les verbes du module.",
       mots:[["Le présent","vous appuyez · vous composez · vous laissez · vous raccrochez"],["L'impératif","appuyez · composez · laissez · raccrochez",true],["Avec « s'il vous plaît »","rappelez-moi, s'il vous plaît · signez ici, s'il vous plaît"]],
       say:"Parlez après le signal sonore, jamais avant.",
       note:"À la forme « tu », les verbes en -er perdent leur « s » : « tu appuies » donne « appuie ». C'est la seule irrégularité de l'impératif, et elle ne sert pas ici, où l'on vouvoie."},

      {t:'ana', h:"La forme négative : le verbe reste entre ne et pas",
       p:"Rien ne bouge autour du verbe : « ne » devant, « pas » derrière, exactement comme dans une phrase ordinaire.",
       mots:[["Les phrases du répondeur","Ne raccrochez pas. · Ne quittez pas."],["Dans la classe","N'écrivez pas encore. · Ne fermez pas votre livre.",true],["À l'oral, le « ne » tombe","Raccrochez pas tout de suite. — s'entend, mais ne s'écrit pas"]],
       say:"La ligne était occupée : elle a rappelé plus tard.",
       note:"« Ne quittez pas » est la formule fixe du téléphone au Québec et en France : elle veut dire « restez en ligne », et elle n'a rien à voir avec quitter un lieu."},

      {t:'ana', h:"Avec un pronom : derrière au positif, devant au négatif",
       p:"C'est la seule particularité qui demande de l'attention, et elle se règle en deux exemples.",
       mots:[["Positif : derrière, avec un trait d'union","Rappelez-moi. · Parlez-lui. · Lisez-la. · Apportez-la-moi."],["Négatif : devant, sans trait d'union","Ne me rappelez pas. · Ne lui parlez pas. · Ne la remettez pas.",true],["Le pronom « me » devient « moi »","vous me rappelez ▸ rappelez-moi, jamais « rappelez-me »"]],
       say:"Sans signature, la note reste une simple feuille.",
       note:"Le trait d'union n'est pas décoratif : c'est lui qui montre que le pronom fait partie du verbe. Une note où l'on écrit « rappelez moi » se lit encore, mais elle se voit."},

      {t:'labo', h:"La même consigne, aux trois formes",
       p:"Choisissez un verbe et écoutez-le au positif, au négatif, puis avec un pronom.",
       axes:[{id:'v', lbl:'Quel verbe ?', opts:[
         ['a','appuyer'],
         ['b','raccrocher'],
         ['c','rappeler'],
         ['d','lire'],
         ['e','apporter']]}],
       out:{
         a:{w:['le clavier'], say:"Appuyez sur le 1. N'appuyez pas tout de suite. Appuyez-y quand la voix le dira.", n:"positif, négatif, avec pronom"},
         b:{w:['la ligne'], say:"Raccrochez après le message. Ne raccrochez pas maintenant. Ne quittez pas.", n:"la formule fixe du téléphone"},
         c:{w:['les coordonnées'], say:"Rappelez le secrétariat. Ne rappelez pas avant huit heures. Rappelez-moi cet après-midi.", n:"le pronom passe derrière au positif"},
         d:{w:['une note'], say:"Lisez votre note. Ne la lisez pas trop vite. Lisez-la-moi à voix haute.", n:"deux pronoms, deux traits d'union"},
         e:{w:['une copie'], say:"Apportez une copie. N'apportez pas l'original. Apportez-la-moi avant vendredi.", n:"la phrase exacte de madame Sansregret"},
       },
       note:"Répétez chaque série en marquant bien le trait d'union à l'oreille : « rappelez… moi », d'un seul souffle, sans coupure."},

      {t:'ex', h:"À écouter et à répéter",
       p:"Six consignes de répondeur, toutes réelles.",
       rows:[
         ["Appuyez sur le 1 pour signaler une absence.","le choix du menu"],
         ["Composez le poste de la personne demandée.","quand on connaît le numéro"],
         ["Laissez votre message après le signal sonore.","la phrase la plus fréquente"],
         ["Pour réentendre ce menu, ne faites rien.","une consigne qui demande de ne rien faire"],
         ["Ne quittez pas, un agent va vous répondre.","restez en ligne"],
         ["Pour terminer, raccrochez.","la fin, en deux mots"],
       ]},

      {t:'piege', h:"Trois pièges de l'impératif",
       rows:[
         ["garder le pronom « vous »","dire « vous appuyez sur le 1 » pour donner une consigne",
          "Ce n'est pas faux, mais ce n'est plus une consigne : c'est une description. Le répondeur, lui, enlève toujours le pronom."],
         ["oublier le trait d'union","écrire « rappelez moi » ou « lisez la »",
          "À l'oral, personne n'entend la différence. À l'écrit, dans une note, elle se voit tout de suite — et une note se lit."],
         ["laisser le pronom derrière au négatif","dire « ne rappelez-moi pas »",
          "Au négatif, le pronom revient devant : « ne me rappelez pas ». C'est la seule chose à retenir en plus, et elle vaut pour tous les verbes."],
       ]},

      {t:'check', h:"Est-ce que c'est clair maintenant ?",
       p:"Quatre questions rapides.",
       qs:[
         {q:"Pour former l'impératif avec « vous », on…", opts:["enlève le pronom","ajoute une terminaison"], ok:0,
          fb:"On enlève le pronom, et rien d'autre : vous appuyez ▸ appuyez."},
         {q:"« Ne quittez pas » veut dire…", opts:["ne partez pas de la salle","restez en ligne"], ok:1,
          fb:"Restez en ligne. C'est la formule fixe du téléphone."},
         {q:"Au positif, le pronom se place…", opts:["derrière, avec un trait d'union","devant le verbe"], ok:0,
          fb:"Derrière, avec un trait d'union : rappelez-moi."},
         {q:"À la forme négative, on dit…", opts:["ne rappelez-moi pas","ne me rappelez pas"], ok:1,
          fb:"Ne me rappelez pas : au négatif, le pronom revient devant."},
       ]},
    ]
  },

  // ════════════════════════════════════════════════════════════════════════
  t1devoir: {
    eye:'Mini-leçon', tit:"Devoir, il faut, il faudrait",
    blocs:[
      {t:'texte', h:"Trois façons de dire qu'une chose doit se faire",
       p:"Le français dit l'obligation de trois manières, et elles ne sont pas interchangeables. « Je dois » nomme la personne obligée. « Il faut » ne nomme personne et énonce une règle générale. « Il faudrait » adoucit et transforme la règle en suggestion. Dans un centre, vous entendrez surtout les deux dernières : le personnel évite de vous désigner, parce que la règle ne vient pas de lui. Et vous, vous emploierez la première pour dire ce que vous vous engagez à faire.",
       note:"Après ces trois formes, le second verbe reste toujours à l'infinitif. C'est la faute la plus fréquente à ce niveau, et la plus facile à corriger."},

      {t:'ana', h:"Devoir : il se conjugue et il nomme",
       p:"Six formes, et deux pièges d'orthographe : un seul « s » à je dois, un « t » à il doit.",
       mots:[["Le singulier","je dois · tu dois · il ou elle doit"],["Le pluriel","nous devons · vous devez · ils ou elles doivent",true],["Dans le module","Je dois signaler mon absence. · Vous devez nous remettre une note."]],
       say:"Un élève à temps plein doit justifier toutes ses absences.",
       note:"« Vous devez » est ferme. Le personnel l'emploie quand la chose n'est pas négociable : vous devez remettre une note écrite, vous devez signer."},

      {t:'ana', h:"Il faut : la règle, sans personne",
       p:"« Il » ne désigne rien ni personne : c'est un sujet vide, comme dans « il pleut ». La forme ne change jamais.",
       mots:[["La règle générale","Il faut téléphoner avant huit heures."],["Suivi d'un nom","Il faut une note écrite et signée.",true],["À la forme négative","Il ne faut pas attendre la fin de la semaine."]],
       say:"La note tient en cinq lignes, datées et signées.",
       note:"« Il faut » ne se conjugue à aucune personne : on ne dit jamais « je faut » ni « nous fallons ». Le verbe s'appelle « falloir » et il n'existe qu'à cette forme."},

      {t:'ana', h:"Il faudrait : le conditionnel de politesse",
       p:"Même sens, mais posé sur la table plutôt que jeté. C'est la forme la plus employée par le personnel d'un centre, et celle qui vous rendra le plus service.",
       mots:[["Ce que dit le secrétariat","Il faudrait nous apporter le papier avant vendredi."],["Ce que vous pouvez dire","Il faudrait que je parle à monsieur Corriveau.",true],["Le voisin utile","Est-ce que je pourrais vous rappeler cet après-midi ?"]],
       say:"Le motif se dit en une seule phrase.",
       note:"« Il faudrait que » demande un subjonctif : « il faudrait que je parle ». Ne vous en inquiétez pas à ce niveau — la forme courte, « il faudrait parler à… », suffit et se dit très bien."},

      {t:'labo', h:"La même chose, du plus ferme au plus doux",
       p:"Choisissez une obligation et écoutez-la aux trois degrés.",
       axes:[{id:'o', lbl:'Quelle obligation ?', opts:[
         ['a','remettre une note'],
         ['b','téléphoner avant huit heures'],
         ['c','signer le papier'],
         ['d','annoncer un abandon'],
         ['e','apporter une copie']]}],
       out:{
         a:{w:['une note'], say:"Vous devez remettre une note. Il faut remettre une note. Il faudrait remettre une note avant vendredi.", n:"ferme, général, adouci"},
         b:{w:['la boîte vocale'], say:"Je dois téléphoner avant huit heures. Il faut téléphoner avant huit heures. Il faudrait téléphoner un peu plus tôt.", n:"le même conseil, trois fois"},
         c:{w:['une signature'], say:"Vous devez signer le papier. Il faut le signer à la main. Il faudrait le signer avant de le remettre.", n:"la signature, sans détour"},
         d:{w:['un abandon'], say:"Vous devez annoncer l'abandon par écrit. Il faut le faire avant la fin du mois. Il faudrait le faire cette semaine.", n:"une échéance qui approche"},
         e:{w:['une copie'], say:"Je dois faire une copie. Il faut toujours garder une copie. Il faudrait en faire une avant de descendre.", n:"le conseil de monsieur Corriveau"},
       },
       note:"Écoutez les trois degrés à la suite : le ton change plus que les mots. C'est ce ton-là qu'il faut reconnaître au téléphone."},

      {t:'ex', h:"À écouter et à répéter",
       p:"Six phrases entendues au comptoir.",
       rows:[
         ["Je dois signaler mon absence avant le cours.","ce que vous dites de vous"],
         ["Vous devez nous remettre une note signée.","ce que le centre exige"],
         ["Il faut téléphoner avant huit heures.","la règle, sans personne"],
         ["Il faudrait nous apporter le papier avant vendredi.","la même chose, en plus doux"],
         ["Est-ce que je peux vous rappeler cet après-midi ?","la permission, pas l'obligation"],
         ["Il ne faut pas attendre la fin du mois.","la règle, à la forme négative"],
       ]},

      {t:'piege', h:"Trois pièges de l'obligation",
       rows:[
         ["conjuguer le second verbe","« je dois je téléphone »",
          "Après devoir et après falloir, le verbe qui suit reste à l'infinitif : « je dois téléphoner ». C'est la faute numéro un à ce niveau."],
         ["conjuguer falloir","« je faut », « nous fallons »",
          "Falloir n'existe qu'à une seule forme : il faut. Pour parler de soi, on emploie devoir : « je dois »."],
         ["confondre « je dois » et « je doit »","oublier ou ajouter un « t »",
          "Je dois, tu dois, il doit. Le « t » appartient à la troisième personne, jamais aux deux premières."],
       ]},

      {t:'check', h:"Est-ce que c'est clair maintenant ?",
       p:"Quatre questions rapides.",
       qs:[
         {q:"Après « il faut », le verbe suivant est…", opts:["conjugué","à l'infinitif"], ok:1,
          fb:"À l'infinitif : il faut téléphoner, il faut remettre."},
         {q:"Quelle forme est la plus douce ?", opts:["vous devez","il faudrait"], ok:1,
          fb:"Il faudrait : le conditionnel transforme l'ordre en suggestion."},
         {q:"« Falloir » se conjugue…", opts:["à toutes les personnes","seulement à « il »"], ok:1,
          fb:"Seulement à « il » : il faut, il faudrait. Jamais « je faut »."},
         {q:"On écrit…", opts:["je dois","je doit"], ok:0,
          fb:"Je dois. Le « t » est pour la troisième personne : il doit."},
       ]},
    ]
  },

  // ════════════════════════════════════════════════════════════════════════
  t1ordre: {
    eye:'Mini-leçon', tit:"Ranger un message dans le temps",
    blocs:[
      {t:'texte', h:"Sans marqueurs, une minute devient une seule phrase",
       p:"Quand on parle à une machine, on ne voit pas de visage et on perd le fil du temps. Les marqueurs sont là pour cela : ils disent à celui qui écoute où vous en êtes. « D'abord » annonce le début, « ensuite » fait avancer, « enfin » prévient qu'on termine. Ce sont trois mots, ils ne coûtent rien à dire, et ils transforment un message confus en message clair — sans qu'un seul renseignement soit ajouté.",
       note:"On les emploie aussi à l'écrit, dans une note, quand il y a deux ou trois choses à dire. Trois marqueurs suffisent : au-delà, la note est trop longue."},

      {t:'ana', h:"D'abord, ensuite, enfin",
       p:"Trois marqueurs, trois places, et on ne les mélange pas. Ils se mettent en tête de phrase, suivis d'une virgule à l'écrit.",
       mots:[["Le début","D'abord, je me nomme et je donne mon groupe."],["La suite","Ensuite, je dis quel jour je serai absente.",true],["La fin","Enfin, je laisse mon numéro de téléphone."]],
       say:"Son message durait cinquante secondes en tout.",
       note:"« Premièrement, deuxièmement, troisièmement » existent aussi, mais ils appartiennent à l'écrit administratif. Dans un message, ils sonnent raides."},

      {t:'ana', h:"Avant de + infinitif : ce qui vient en premier",
       p:"La construction est courte et elle ne se conjugue pas. Une seule condition : la même personne fait les deux actions.",
       mots:[["Dans le module","Avant de parler, attendez le signal sonore."],["Avant de raccrocher","Avant de raccrocher, redites votre numéro.",true],["Dans la note","Avant de remettre la note, faites-en une copie."]],
       say:"Parlez après le signal sonore, jamais avant.",
       note:"Ne dites pas « avant parler » ni « avant de je parle » : c'est toujours « avant de » suivi d'un verbe à l'infinitif, sans sujet."},

      {t:'ana', h:"Après avoir + participe passé : ce qui vient ensuite",
       p:"Même règle, même condition. Avec les verbes qui prennent l'auxiliaire être, on dit « après être » et le participe s'accorde.",
       mots:[["Avec avoir","Après avoir écouté le menu, j'ai appuyé sur le 1."],["Avec avoir, encore","Après avoir laissé mon message, j'ai raccroché.",true],["Avec être","Après être allée à la clinique, je suis rentrée à la maison."]],
       say:"Elle a fait une copie avant de descendre au comptoir.",
       note:"C'est une construction d'écrit, surtout. À l'oral, on dit plus simplement « j'ai écouté le menu, puis j'ai appuyé sur le 1 » — et c'est très bien."},

      {t:'labo', h:"Deux actions, deux façons de les relier",
       p:"Choisissez une paire d'actions et écoutez-la reliée dans les deux sens.",
       axes:[{id:'p', lbl:'Quelles actions ?', opts:[
         ['a','écouter le menu · appuyer sur le 1'],
         ['b','attendre le signal · parler'],
         ['c','écrire la note · faire une copie'],
         ['d','aller à la clinique · téléphoner'],
         ['e','laisser le message · raccrocher']]}],
       out:{
         a:{w:['un répondeur'], say:"Avant d'appuyer sur le 1, écoutez le menu au complet. Après avoir écouté le menu, appuyez sur le 1.", n:"la même chose, dans les deux sens"},
         b:{w:['le signal sonore'], say:"Avant de parler, attendez le signal sonore. Après avoir entendu le signal, commencez à parler.", n:"le début d'un message"},
         c:{w:['une copie'], say:"Avant de remettre la note, faites-en une copie. Après avoir fait une copie, descendez au comptoir.", n:"le conseil de l'enseignant"},
         d:{w:['un empêchement'], say:"Avant d'aller à la clinique, elle a téléphoné au centre. Après avoir téléphoné, elle est partie avec son fils.", n:"l'ordre réel de la matinée"},
         e:{w:['un message'], say:"Avant de raccrocher, redites votre numéro. Après avoir laissé son message, elle a raccroché.", n:"la fin d'un appel"},
       },
       note:"Faites l'exercice à voix haute : dites la paire dans un sens, puis dans l'autre. C'est ainsi qu'on cesse d'hésiter entre « avant de » et « après avoir »."},

      {t:'ex', h:"À écouter et à répéter",
       p:"Six phrases qui rangent les choses.",
       rows:[
         ["D'abord, je me nomme et je donne mon groupe.","le premier morceau"],
         ["Ensuite, je dis quel jour et pourquoi.","le deuxième"],
         ["Enfin, je laisse mon numéro deux fois.","le dernier"],
         ["Avant de parler, attendez le signal sonore.","une action avant l'autre"],
         ["Après avoir écouté les trois messages, elle a rappelé.","une action après l'autre"],
         ["Avant de descendre au comptoir, faites une copie.","le conseil, en une phrase"],
       ]},

      {t:'piege', h:"Trois pièges des marqueurs de temps",
       rows:[
         ["dire « avant parler »","oublier le « de »",
          "C'est toujours « avant de » devant un verbe : avant de parler, avant de raccrocher, avant de partir. Devant un nom, en revanche, on dit « avant le cours », sans « de »."],
         ["conjuguer après « avant de »","« avant de je parle »",
          "Le verbe reste à l'infinitif, sans sujet. Si les deux actions ont deux sujets différents, il faut une autre construction : « avant que vous partiez »."],
         ["employer « après » tout seul devant un verbe","« après téléphoner »",
          "On dit « après avoir téléphoné » : le participe passé est obligatoire. « Après » seul ne se met que devant un nom : après le cours, après le signal sonore."],
       ]},

      {t:'check', h:"Est-ce que c'est clair maintenant ?",
       p:"Quatre questions rapides.",
       qs:[
         {q:"Le mot qui annonce la fin d'un message est…", opts:["ensuite","enfin"], ok:1,
          fb:"« Enfin ». « Ensuite » fait avancer, « enfin » termine."},
         {q:"Devant un verbe, on écrit…", opts:["avant de parler","avant parler"], ok:0,
          fb:"« Avant de parler ». Le « de » est obligatoire devant un verbe."},
         {q:"« Après avoir écouté » est suivi de…", opts:["un participe passé, déjà présent","un infinitif"], ok:0,
          fb:"Le participe passé est déjà là : « écouté ». La construction est complète."},
         {q:"Combien de marqueurs dans un message d'une minute ?", opts:["trois suffisent","le plus possible"], ok:0,
          fb:"Trois suffisent : d'abord, ensuite, enfin."},
       ]},
    ]
  },

  // ════════════════════════════════════════════════════════════════════════
  t2a: {
    eye:'Mini-leçon', tit:"Écouter un message : trois choses, jamais plus",
    blocs:[
      {t:'texte', h:"Comprendre un message n'est pas comprendre tous les mots",
       p:"C'est le point le plus difficile à admettre, et le plus libérateur. Un message de trente secondes contient une centaine de mots, dont peut-être quinze que vous ne connaissez pas. Vous n'avez pas besoin des cent : vous avez besoin de trois choses — qui appelle, pourquoi, et ce qu'on attend de vous. Ces trois choses sont toujours aux mêmes endroits : au début, juste après, et à la fin. Écouter un message, c'est écouter trois moments, pas une durée.",
       note:"Prenez un crayon avant d'appuyer sur écouter, jamais après. Chercher un crayon pendant le message, c'est perdre le nom."},

      {t:'ana', h:"1. Qui appelle : dans les cinq premières secondes",
       p:"La personne se nomme une seule fois, tout de suite, et souvent vite parce qu'elle connaît son propre nom par cœur. C'est le moment d'être le plus attentif.",
       mots:[["La formule habituelle","Bonjour madame Ouazzani, ici Murielle Sansregret, du secrétariat."],["Ce qu'il faut noter","le prénom, le nom de famille, et d'où la personne appelle",true],["Si vous l'avez manqué","réécoutez seulement les cinq premières secondes"]],
       say:"Son message durait cinquante secondes en tout.",
       note:"Notez aussi d'où la personne appelle : « du secrétariat », « votre enseignant ». C'est ce qui vous dira à quel poste rappeler."},

      {t:'ana', h:"2. Pourquoi : presque toujours la deuxième phrase",
       p:"Une seule phrase, et tout le reste du message la développe. Si vous l'attrapez, vous comprendrez la suite même en manquant des mots.",
       mots:[["Message 1","J'ai bien reçu votre message et j'ai inscrit votre absence."],["Message 2","On a fait les nombres et l'heure ce matin ; je vous ai gardé les feuilles.",true],["Message 3","Vous êtes aussi inscrite au cours d'informatique du soir."]],
       say:"Son absence de lundi est inscrite au dossier.",
       note:"Cette phrase-là commence souvent par « je vous appelle pour… », « j'ai bien reçu… » ou « c'est au sujet de… ». Ce sont trois signaux à reconnaître."},

      {t:'ana', h:"3. Ce qu'on attend de vous : à la fin",
       p:"C'est la seule partie qui vous oblige à agir, et c'est celle qu'on oublie parce qu'on se détend en fin de message. Écrivez-la mot pour mot.",
       mots:[["Une action et une date","Apportez-la-moi avant vendredi, au comptoir."],["Un lieu et une heure","Le rattrapage a lieu demain midi, au local 214.",true],["Une échéance","Il faut nous le dire par écrit avant la fin du mois."]],
       say:"La note tient en cinq lignes, datées et signées.",
       note:"S'il n'y a rien à faire, le message le dit aussi : « ne vous inquiétez pas », « c'est juste pour vous informer ». C'est un renseignement, notez-le."},

      {t:'labo', h:"Les trois moments d'un même message",
       p:"Choisissez un message du module et écoutez-en le moment qui vous intéresse.",
       axes:[{id:'m', lbl:'Quel moment ?', opts:[
         ['a','message 1 · qui appelle'],
         ['b','message 1 · ce qu\'il faut faire'],
         ['c','message 2 · pourquoi'],
         ['d','message 2 · ce qu\'il faut faire'],
         ['e','message 3 · l\'avertissement']]}],
       out:{
         a:{w:['un message'], say:"Bonjour madame Ouazzani, ici Murielle Sansregret, du secrétariat de la Pointe-aux-Ormes.", n:"le nom et le service, en cinq secondes"},
         b:{w:['une note'], say:"Apportez-la-moi avant vendredi, au comptoir, avec le papier de la clinique.", n:"une action, une date, un lieu"},
         c:{w:['un poste'], say:"On a fait les nombres et l'heure ce matin ; je vous ai gardé les feuilles.", n:"la raison de l'appel, en une phrase"},
         d:{w:['un retard'], say:"Le rattrapage a lieu demain sur l'heure du dîner, au local 214.", n:"un lieu et un moment, à noter"},
         e:{w:['un abandon'], say:"Si vous l'abandonnez, il faut nous le dire par écrit avant la fin du mois.", n:"la condition, puis l'échéance"},
       },
       note:"Écoutez chaque extrait deux fois : la première pour saisir, la seconde en écrivant. Écrire pendant la première écoute fait manquer la moitié."},

      {t:'ex', h:"À écouter et à répéter",
       p:"Six formules qui reviennent dans tous les messages.",
       rows:[
         ["Bonjour madame, ici Murielle Sansregret, du secrétariat.","qui appelle"],
         ["Je vous appelle au sujet de votre absence de lundi.","pourquoi"],
         ["J'ai bien reçu votre message de ce matin.","une confirmation"],
         ["Il faudrait nous apporter la note avant vendredi.","ce qu'on attend de vous"],
         ["Ne vous inquiétez pas, ça arrive à tout le monde.","rien à faire"],
         ["Vous pouvez me rappeler au poste 224.","comment répondre"],
       ]},

      {t:'piege', h:"Trois pièges de l'écoute",
       rows:[
         ["vouloir tout comprendre","réécouter dix fois la même phrase difficile",
          "Le mot que vous n'avez pas compris n'est presque jamais l'un des trois renseignements utiles. Passez, et vérifiez à la fin s'il vous manque quelque chose."],
         ["ne rien écrire","se dire qu'on s'en souviendra",
          "On se souvient du sentiment, pas de la date ni du numéro de local. Trois mots sur un papier valent trois réécoutes."],
         ["rappeler pour dire qu'on a compris","« bonjour, c'est pour vous dire que j'ai eu votre message »",
          "Le secrétariat en reçoit quarante par jour. Rappelez s'il manque une des trois choses, ou si on vous le demande — sinon, faites simplement ce qu'on vous demande."],
       ]},

      {t:'check', h:"Est-ce que c'est clair maintenant ?",
       p:"Quatre questions rapides.",
       qs:[
         {q:"Où se trouve le nom de la personne qui appelle ?", opts:["dans les cinq premières secondes","à la fin"], ok:0,
          fb:"Au tout début, et souvent dit une seule fois."},
         {q:"Où se trouve ce qu'on attend de vous ?", opts:["au début","à la fin"], ok:1,
          fb:"À la fin — au moment où l'attention baisse. Écrivez-le."},
         {q:"Quand faut-il prendre un crayon ?", opts:["avant d'écouter","pendant le message"], ok:0,
          fb:"Avant. Chercher un crayon pendant le message fait manquer le nom."},
         {q:"Faut-il rappeler pour confirmer qu'on a écouté ?", opts:["oui, par politesse","non, sauf si on le demande"], ok:1,
          fb:"Non, sauf s'il manque un renseignement ou qu'on vous le demande."},
       ]},
    ]
  },

  // ════════════════════════════════════════════════════════════════════════
  t2cause: {
    eye:'Mini-leçon', tit:"Parce que, à cause de, grâce à",
    blocs:[
      {t:'texte', h:"Trois façons de dire pourquoi, et elles ne se remplacent pas",
       p:"Donner une raison est le cœur de ce module : justifier, c'est exactement cela. Le français offre trois outils, et ils ne se choisissent pas au hasard. « Parce que » introduit une phrase entière et convient partout. « À cause de » introduit un nom et sous-entend que la chose a causé un ennui. « Grâce à » introduit un nom aussi, mais sous-entend le contraire : la chose a aidé. Employer l'un pour l'autre ne fait pas seulement une faute de grammaire — cela change ce que la phrase dit de la personne dont on parle.",
       note:"Au téléphone, « parce que » est le plus sûr des trois : il accepte n'importe quelle suite, et personne ne l'entendra comme un reproche."},

      {t:'ana', h:"Parce que : une phrase complète derrière",
       p:"Après « parce que », il faut un sujet et un verbe conjugué. Devant une voyelle, le « e » tombe et on écrit « parce qu' ».",
       mots:[["La forme complète","Je serai absente parce que mon fils est malade."],["Devant une voyelle","Je vous rappelle parce qu'il manque un papier.",true],["Ce qui ne se dit pas","« parce que la tempête » — il manque le verbe"]],
       say:"Le motif se dit en une seule phrase.",
       note:"« Parce que » ne commence jamais une phrase à l'écrit, sauf pour répondre à une question. Dans une note, il vient toujours au milieu."},

      {t:'ana', h:"À cause de : un nom derrière, et un ennui",
       p:"Pas de verbe : un nom, tout de suite. Et un sens négatif — ce qui suit a causé un problème.",
       mots:[["Devant un nom féminin ou une voyelle","à cause de la neige · à cause de l'autobus"],["Contraction avec « le »","à cause du bruit · à cause du verglas",true],["Contraction avec « les »","à cause des travaux · à cause des enfants"]],
       say:"Un retard de dix minutes se signale aussi.",
       note:"La contraction est obligatoire : « à cause de le bruit » ne se dit pas, ni ne s'écrit. C'est le même mécanisme que « je parle du cours »."},

      {t:'ana', h:"Grâce à : un nom derrière, et une aide",
       p:"Même construction qu'« à cause de », sens inverse. Les mêmes contractions s'appliquent : grâce au, grâce aux.",
       mots:[["Le sens positif","Grâce à son message, elle a appris l'affaire à temps."],["Avec « le » et « les »","grâce au rattrapage · grâce aux feuilles gardées",true],["Une personne","Grâce à Wilner, elle avait le bon numéro."]],
       say:"Elle a téléphoné dès qu'elle a su qu'elle avait un empêchement.",
       note:"« Grâce à » se sent immédiatement comme un remerciement. C'est une phrase que le personnel d'un centre entend rarement, et qui fait toujours plaisir."},

      {t:'labo', h:"La même situation, avec chacun des trois",
       p:"Choisissez une situation et écoutez comment la raison se dit.",
       axes:[{id:'r', lbl:'Quelle raison ?', opts:[
         ['a','un enfant malade'],
         ['b','une tempête de neige'],
         ['c','le bruit des travaux'],
         ['d','un message reçu à temps'],
         ['e','le rattrapage du midi']]}],
       out:{
         a:{w:['une absence','un motif'], say:"Je serai absente parce que mon fils est malade.", n:"une phrase complète après parce que"},
         b:{w:['un retard'], say:"J'aurai du retard à cause de la tempête de neige.", n:"un nom, et un ennui"},
         c:{w:['la ligne'], say:"Le cours a été déplacé à cause du bruit des travaux.", n:"la contraction : de + le donne du"},
         d:{w:['un message'], say:"Grâce à son message, elle a appris l'affaire avant la fin du mois.", n:"un nom, et une aide"},
         e:{w:['un poste'], say:"Grâce au rattrapage du midi, elle n'a rien manqué.", n:"la contraction : à + le donne au"},
       },
       note:"Écoutez les deux dernières l'une après l'autre : même construction, sens opposé. C'est tout ce qui sépare « à cause de » de « grâce à »."},

      {t:'ex', h:"À écouter et à répéter",
       p:"Six phrases à dire au téléphone.",
       rows:[
         ["Je serai absente parce que mon fils a une otite.","phrase complète"],
         ["Je vous rappelle parce qu'il manque un papier.","le « e » tombe"],
         ["J'aurai du retard à cause de l'autobus.","un nom, un ennui"],
         ["Le cours est déplacé à cause du bruit.","de + le donne du"],
         ["Grâce à votre message, j'ai compris à temps.","un nom, une aide"],
         ["Grâce au rattrapage, je n'ai rien manqué.","à + le donne au"],
       ]},

      {t:'piege', h:"Trois pièges de la cause",
       rows:[
         ["mettre une phrase après « à cause de »","« à cause de mon fils est malade »",
          "Après « à cause de », il faut un nom seul : « à cause de mon fils ». Si vous voulez la phrase entière, employez « parce que »."],
         ["oublier la contraction","« à cause de le bruit »",
          "De + le donne du, de + les donne des. La règle est la même que partout ailleurs en français, et l'oreille l'attrape vite."],
         ["dire « à cause de » pour une bonne chose","« à cause de vous, j'ai réussi »",
          "Cela se comprend, mais cela sonne comme un reproche. Pour une aide, c'est « grâce à » : « grâce à vous, j'ai réussi »."],
       ]},

      {t:'check', h:"Est-ce que c'est clair maintenant ?",
       p:"Quatre questions rapides.",
       qs:[
         {q:"Après « parce que », il faut…", opts:["un nom","un sujet et un verbe"], ok:1,
          fb:"Un sujet et un verbe conjugué : parce que mon fils est malade."},
         {q:"« À cause de » + « le bruit » donne…", opts:["à cause de le bruit","à cause du bruit"], ok:1,
          fb:"À cause du bruit. La contraction est obligatoire."},
         {q:"Pour remercier, on emploie…", opts:["grâce à","à cause de"], ok:0,
          fb:"« Grâce à » : même construction, sens positif."},
         {q:"Devant une voyelle, « parce que » devient…", opts:["parce qu'","parce que"], ok:0,
          fb:"« Parce qu' » : parce qu'il manque un papier."},
       ]},
    ]
  },

  // ════════════════════════════════════════════════════════════════════════
  t2lui: {
    eye:'Mini-leçon', tit:"Lui et leur : remplacer la personne",
    blocs:[
      {t:'texte', h:"Un petit mot pour ne pas répéter le nom",
       p:"Quand on parle de la même personne trois fois de suite, le français remplace son nom par un pronom. « Lui » et « leur » servent quand la personne reçoit l'action : on parle à quelqu'un, on téléphone à quelqu'un, on écrit à quelqu'un, on remet quelque chose à quelqu'un. C'est la construction avec « à » qui commande, et pas autre chose. Dans un message, ces deux mots évitent de répéter « madame Sansregret » quatre fois — et ils font tout de suite plus naturel.",
       note:"« Lui » et « leur » sont des pronoms compléments indirects. Le nom du terme n'a aucune importance ; ce qui compte, c'est de reconnaître le « à » dans la phrase de départ."},

      {t:'ana', h:"Lui : une seule personne, homme ou femme",
       p:"C'est ce qui surprend le plus : « lui » ne veut pas dire « un homme ». Il vaut pour une personne, quelle qu'elle soit.",
       mots:[["Un homme","Je parle à Fabien ▸ Je lui parle."],["Une femme","Je parle à Murielle ▸ Je lui parle.",true],["Dans le module","Elle lui a laissé un message ce matin."]],
       say:"Le secrétariat, c'est le poste 224 du centre.",
       note:"Il existe un autre « lui », celui de « avec lui », « chez lui », qui désigne un homme. Ce n'est pas le même mot, et il vient toujours après une préposition."},

      {t:'ana', h:"Leur : deux personnes ou plus, et jamais de « s »",
       p:"Le pronom « leur » ne prend jamais de « s ». Ne le confondez pas avec le déterminant « leurs », qui accompagne un nom.",
       mots:[["Le pronom","Elle écrit aux enseignants ▸ Elle leur écrit."],["Le déterminant","Les élèves ont apporté leurs papiers.",true],["Le test","devant un verbe, jamais de « s » ; devant un nom, il s'accorde"]],
       say:"La ligne était occupée : elle a rappelé plus tard.",
       note:"Un seul repère suffit : si le mot qui suit est un verbe, c'est « leur » sans « s ». Si c'est un nom, c'est « leur » ou « leurs » selon le nombre."},

      {t:'ana', h:"La place : devant le verbe, sauf à l'impératif positif",
       p:"Le pronom se colle au verbe et passe devant lui, y compris au passé composé et avec un infinitif.",
       mots:[["Au présent","Je lui téléphone chaque semaine."],["Au passé composé","Je lui ai téléphoné hier matin.",true],["Avec deux verbes","Je vais lui téléphoner après le cours."],["À l'impératif positif","Téléphonez-lui avant midi."]],
       say:"Sans signature, la note reste une simple feuille.",
       note:"Au passé composé, le pronom passe devant l'auxiliaire, jamais entre l'auxiliaire et le participe : « je lui ai parlé », et non « j'ai lui parlé »."},

      {t:'labo', h:"La phrase longue, puis la phrase avec le pronom",
       p:"Choisissez une phrase et écoutez-la avant et après le remplacement.",
       axes:[{id:'p', lbl:'Quelle phrase ?', opts:[
         ['a','téléphoner à la secrétaire'],
         ['b','remettre la note à l\'enseignant'],
         ['c','répondre aux élèves'],
         ['d','écrire aux parents'],
         ['e','demander le numéro à Wilner']]}],
       out:{
         a:{w:['un poste'], say:"Elle téléphone à madame Sansregret. Elle lui téléphone au poste 224.", n:"une femme, et c'est bien lui"},
         b:{w:['une note'], say:"Elle remet la note à monsieur Corriveau. Elle lui remet la note jeudi.", n:"un homme, et c'est le même mot"},
         c:{w:['un message'], say:"L'enseignant répond aux élèves. Il leur répond après le cours.", n:"plusieurs personnes : leur, sans s"},
         d:{w:['une absence'], say:"Le secrétariat écrit aux parents. Il leur envoie un avis chaque session.", n:"leur, encore, et toujours sans s"},
         e:{w:['la ligne'], say:"Je demande le numéro à Wilner. Je vais lui demander à la pause.", n:"avec deux verbes, le pronom colle à l'infinitif"},
       },
       note:"Écoutez la phrase longue, puis la courte. C'est la courte qui sonne français : la longue est correcte, mais on ne parle pas ainsi."},

      {t:'ex', h:"À écouter et à répéter",
       p:"Six phrases du module.",
       rows:[
         ["Elle lui a laissé un message ce matin.","une personne"],
         ["Je lui remets ma note jeudi, en classe.","une personne, un objet remis"],
         ["L'enseignant leur répond après le cours.","plusieurs personnes"],
         ["Le secrétariat leur envoie un avis chaque session.","plusieurs, sans s"],
         ["Je vais lui demander le numéro à la pause.","le pronom colle à l'infinitif"],
         ["Rappelez-lui avant midi, s'il vous plaît.","à l'impératif, il passe derrière"],
       ]},

      {t:'piege', h:"Trois pièges de lui et leur",
       rows:[
         ["croire que « lui » désigne un homme","dire « elle » à la place, pour une femme",
          "« Lui » vaut pour une personne, homme ou femme : je lui parle, qu'il s'agisse de Fabien ou de Murielle. C'est la surprise la plus courante à ce niveau."],
         ["écrire « leurs » devant un verbe","« il leurs répond »",
          "Le pronom ne s'accorde jamais : « il leur répond ». Le « s » n'existe que sur le déterminant, devant un nom : « leurs papiers »."],
         ["placer le pronom après le verbe","« j'ai lui parlé »",
          "Le pronom passe devant l'auxiliaire : « je lui ai parlé ». La seule exception est l'impératif positif : « parlez-lui »."],
       ]},

      {t:'check', h:"Est-ce que c'est clair maintenant ?",
       p:"Quatre questions rapides.",
       qs:[
         {q:"« Je parle à Murielle » devient…", opts:["je lui parle","je leur parle"], ok:0,
          fb:"Je lui parle : une seule personne, et « lui » vaut pour une femme aussi."},
         {q:"Le pronom « leur » prend un « s »…", opts:["jamais","au pluriel"], ok:0,
          fb:"Jamais. Seul le déterminant « leurs » s'accorde, devant un nom."},
         {q:"Au passé composé, on dit…", opts:["j'ai lui parlé","je lui ai parlé"], ok:1,
          fb:"Je lui ai parlé : le pronom passe devant l'auxiliaire."},
         {q:"À l'impératif positif, le pronom…", opts:["passe derrière","reste devant"], ok:0,
          fb:"Il passe derrière, avec un trait d'union : parlez-lui."},
       ]},
    ]
  },

  // ════════════════════════════════════════════════════════════════════════
  t3pc: {
    eye:'Mini-leçon', tit:"Le passé composé avec être, et son accord",
    blocs:[
      {t:'texte', h:"Une lettre qu'on n'entend pas, et qui se voit",
       p:"« Je suis allé » et « je suis allée » se prononcent exactement pareil. C'est pourquoi cette faute traverse des années d'apprentissage sans jamais être corrigée à l'oral : personne ne l'entend. Mais une note d'absence est un écrit, et là elle saute aux yeux. La règle tient en une phrase : quand le passé composé se forme avec l'auxiliaire être, le participe passé s'accorde avec le sujet, comme un adjectif. Avec avoir, il ne bouge pas.",
       note:"Dans ce module, c'est une femme qui écrit. Tous les participes des verbes avec être prennent donc un « e » : allée, restée, revenue, arrivée, levée."},

      {t:'ana', h:"Quels verbes prennent être",
       p:"Une quinzaine, presque tous des verbes de déplacement ou de changement d'état. Ils s'apprennent en bloc, et la liste ne s'allonge pas.",
       mots:[["Aller et venir","aller · venir · revenir · retourner · arriver · partir"],["Entrer et sortir","entrer · sortir · monter · descendre · rester · tomber",true],["Naître et mourir","naître · mourir · devenir · rentrer"]],
       say:"Son absence de lundi est inscrite au dossier.",
       note:"Tous les autres verbes prennent avoir : j'ai téléphoné, j'ai écouté, j'ai remis, j'ai signé. Et avec avoir, le participe ne s'accorde pas avec le sujet."},

      {t:'ana', h:"L'accord : comme un adjectif",
       p:"Quatre formes, exactement comme pour « grand, grande, grands, grandes ».",
       mots:[["Un homme","il est allé · il est resté · il est tombé"],["Une femme","elle est allée · elle est restée · elle est tombée",true],["Plusieurs","ils sont allés · elles sont allées · nous sommes arrivés"]],
       say:"La note tient en cinq lignes, datées et signées.",
       note:"« Nous sommes arrivés » prend un « s » ; si le groupe n'est composé que de femmes, on écrit « nous sommes arrivées ». Un seul homme dans le groupe suffit pour le masculin."},

      {t:'ana', h:"Les verbes pronominaux prennent être aussi",
       p:"Tous les verbes qui portent « se » à l'infinitif : se lever, se rendre, s'absenter, se présenter. Le participe s'accorde le plus souvent avec le sujet.",
       mots:[["Se lever","Je me suis levée à cinq heures."],["S'absenter","Elle s'est absentée deux jours.",true],["Se présenter","Nous nous sommes présentés au comptoir."]],
       say:"Sans signature, la note reste une simple feuille.",
       note:"Il existe des cas où le participe d'un pronominal ne s'accorde pas, mais ils sont rares et n'apparaissent pas dans une note d'absence. À ce niveau, accordez."},

      {t:'labo', h:"La même phrase, au masculin puis au féminin",
       p:"Choisissez une phrase et écoutez les deux versions. Elles se disent pareil.",
       axes:[{id:'v', lbl:'Quelle phrase ?', opts:[
         ['a','aller à la clinique'],
         ['b','rester à la maison'],
         ['c','revenir trop tard'],
         ['d','se lever à cinq heures'],
         ['e','téléphoner au centre']]}],
       out:{
         a:{w:['une absence'], say:"Il est allé à la clinique. Elle est allée à la clinique.", n:"un e de plus, aucune différence à l'oreille"},
         b:{w:['un empêchement'], say:"Il est resté à la maison. Elle est restée à la maison.", n:"même règle, même silence"},
         c:{w:['un retard'], say:"Il est revenu trop tard. Elle est revenue trop tard.", n:"ici, le e s'entend un peu : revenu, revenue"},
         d:{w:['une note'], say:"Il s'est levé à cinq heures. Elle s'est levée à cinq heures.", n:"les pronominaux prennent être aussi"},
         e:{w:['un message'], say:"Il a téléphoné au centre. Elle a téléphoné au centre.", n:"avec avoir, rien ne change"},
       },
       note:"La dernière est celle qu'il faut retenir : avec avoir, aucun accord avec le sujet. C'est la moitié de la règle, et on l'oublie souvent."},

      {t:'ex', h:"À écouter et à répéter",
       p:"Six phrases d'une note d'absence.",
       rows:[
         ["Je suis allée à la clinique avec mon fils.","être : accord au féminin"],
         ["Mon fils est tombé malade dimanche soir.","être : masculin, pas de e"],
         ["Je suis restée à la maison toute la journée.","être : accord au féminin"],
         ["J'ai téléphoné au centre à sept heures dix.","avoir : pas d'accord"],
         ["Je me suis levée très tôt ce matin-là.","pronominal : être, et accord"],
         ["Madame Sansregret a inscrit mon absence.","avoir : pas d'accord"],
       ]},

      {t:'piege', h:"Trois pièges de l'accord",
       rows:[
         ["accorder avec avoir","« elle a téléphonée »",
          "Avec avoir, le participe ne s'accorde jamais avec le sujet. « Elle a téléphoné », « elle a remis », « elle a signé »."],
         ["oublier le e au féminin","« je suis allé » écrit par une femme",
          "Ça ne s'entend pas, mais ça se lit. Relisez en remplaçant le sujet par « une femme » : une femme est allée."],
         ["oublier que les pronominaux prennent être","« je me suis levé » sans accord",
          "Tout verbe avec « se » prend être, et le participe s'accorde presque toujours : je me suis levée, elle s'est absentée."],
       ]},

      {t:'check', h:"Est-ce que c'est clair maintenant ?",
       p:"Quatre questions rapides.",
       qs:[
         {q:"Avec l'auxiliaire avoir, le participe…", opts:["s'accorde avec le sujet","ne s'accorde pas avec le sujet"], ok:1,
          fb:"Il ne s'accorde pas : elle a téléphoné, elle a signé."},
         {q:"Une femme écrit…", opts:["je suis allé","je suis allée"], ok:1,
          fb:"Je suis allée. Le participe s'accorde comme un adjectif."},
         {q:"« Se lever » prend l'auxiliaire…", opts:["avoir","être"], ok:1,
          fb:"Être, comme tous les verbes pronominaux : je me suis levée."},
         {q:"« Allé » et « allée » se prononcent…", opts:["pareil","différemment"], ok:0,
          fb:"Pareil. C'est pour cela que la faute survit à l'oral et se voit à l'écrit."},
       ]},
    ]
  },

  // ════════════════════════════════════════════════════════════════════════
  t3futur: {
    eye:'Mini-leçon', tit:"Le futur simple : ce qu'on promet par écrit",
    blocs:[
      {t:'texte', h:"Le temps qui referme un dossier",
       p:"Une note qui ne parle que du passé demande à être excusée. Une note qui se termine au futur dit ce qui va se passer, et le dossier peut se refermer : la personne du secrétariat sait quand vous revenez, quand le papier arrivera, quand le rattrapage sera fait. C'est pour cela que le futur simple appartient à l'écrit officiel — et c'est pour cela qu'il faut savoir le reconnaître dans un avis, même si à l'oral vous continuez de dire « je vais remettre le papier ».",
       note:"Reconnaître le futur suffit largement à ce niveau. Le produire vient ensuite, et six verbes irréguliers couvrent presque tous les besoins."},

      {t:'ana', h:"La marque : un « r » avant la terminaison",
       p:"C'est le repère le plus sûr, et il ne rate jamais. Les terminaisons, elles, sont les mêmes pour tous les verbes.",
       mots:[["Les terminaisons","-ai · -as · -a · -ons · -ez · -ont"],["Verbes réguliers","je remettrai · je rattraperai · j'appellerai · je signerai",true],["Toujours le r","tu viendras · il devra · nous serons · vous pourrez"]],
       say:"La note tient en cinq lignes, datées et signées.",
       note:"Pour les verbes en -er, le futur se construit sur l'infinitif entier : téléphoner ▸ je téléphonerai. On voit encore l'infinitif dans le mot."},

      {t:'ana', h:"Six irréguliers qui reviennent tout le temps",
       p:"Ils ne se déduisent pas de l'infinitif : ils s'apprennent, et ce sont les six qu'on rencontre dans tous les avis.",
       mots:[["Être et avoir","je serai · j'aurai"],["Aller et venir","j'irai · je viendrai",true],["Pouvoir et devoir","je pourrai · je devrai"]],
       say:"Le motif se dit en une seule phrase.",
       note:"« Je serai » est le plus utile de tous : « je serai en classe demain », « je serai absente jeudi ». Ne le confondez pas avec « je saurai », qui vient de savoir."},

      {t:'ana', h:"Le futur proche, à l'oral",
       p:"« Aller » suivi d'un infinitif dit la même chose, et c'est ce qu'on emploie en parlant. Les deux sont corrects ; seul le registre change.",
       mots:[["À l'oral","Je vais remettre le papier jeudi."],["À l'écrit","Je vous remettrai le papier jeudi.",true],["Dans un avis du centre","Vous recevrez une confirmation par courriel."]],
       say:"Elle a fait une copie avant de descendre au comptoir.",
       note:"Dans un message téléphonique, le futur proche est parfaitement à sa place. Gardez le futur simple pour la note écrite : c'est ce que le lecteur attend."},

      {t:'labo', h:"La même promesse, à l'oral puis à l'écrit",
       p:"Choisissez une promesse et écoutez ses deux formes.",
       axes:[{id:'f', lbl:'Quelle promesse ?', opts:[
         ['a','revenir en classe'],
         ['b','remettre le papier'],
         ['c','rattraper la matière'],
         ['d','rappeler le secrétariat'],
         ['e','passer au comptoir']]}],
       out:{
         a:{w:['une absence'], say:"Je vais être en classe demain. Je serai en classe demain matin.", n:"le plus utile des six irréguliers"},
         b:{w:['une note'], say:"Je vais remettre le papier jeudi. Je vous remettrai le papier jeudi.", n:"l'infinitif se voit encore dans le futur"},
         c:{w:['un retard'], say:"Je vais rattraper la matière. Je rattraperai la matière au local 214.", n:"un verbe en -er, tout régulier"},
         d:{w:['un poste'], say:"Je vais vous rappeler cet après-midi. Je vous rappellerai avant seize heures.", n:"deux l au futur : rappellerai"},
         e:{w:['une copie'], say:"Je vais passer au comptoir avant midi. J'irai au comptoir avant midi.", n:"aller devient j'irai, sans prévenir"},
       },
       note:"Dites la version orale au téléphone et écrivez la version écrite dans la note. Les deux disent la même chose et personne ne vous reprendra."},

      {t:'ex', h:"À écouter et à répéter",
       p:"Six phrases de fin de note.",
       rows:[
         ["Je serai en classe demain matin.","être, au futur"],
         ["Je vous remettrai le papier de la clinique jeudi.","une preuve, à une date"],
         ["Je rattraperai la matière au local 214.","comment reprendre"],
         ["Je vous rappellerai avant la fin de la journée.","un second appel promis"],
         ["Je devrai quitter le cours à onze heures.","un départ annoncé"],
         ["J'irai au secrétariat avant midi.","aller, au futur"],
       ]},

      {t:'piege', h:"Trois pièges du futur",
       rows:[
         ["confondre -ai et -ais","« je remettrais » au lieu de « je remettrai »",
          "Avec un « s », c'est un conditionnel : « je remettrais » veut dire « si les choses le permettaient ». Dans une note, on écrit le futur, sans « s »."],
         ["oublier le r","« je remettai »",
          "Le « r » est la marque du futur : sans lui, le mot n'existe pas. Cherchez-le à chaque fois que vous écrivez un futur."],
         ["employer le futur à l'oral quand ce n'est pas nécessaire","« je vous remettrai le papier », au téléphone",
          "Ce n'est pas une faute, mais cela sonne écrit. « Je vais vous remettre le papier » est ce que tout le monde dit."],
       ]},

      {t:'check', h:"Est-ce que c'est clair maintenant ?",
       p:"Quatre questions rapides.",
       qs:[
         {q:"La marque du futur simple est…", opts:["un r avant la terminaison","un accent"], ok:0,
          fb:"Un « r » : je remettrai, je serai, je viendrai."},
         {q:"« Je serai » vient du verbe…", opts:["savoir","être"], ok:1,
          fb:"Être. « Je saurai » vient de savoir, et ce n'est pas la même chose."},
         {q:"Dans une note écrite, on emploie…", opts:["le futur simple","le futur proche"], ok:0,
          fb:"Le futur simple : c'est ce que le lecteur d'un écrit officiel attend."},
         {q:"« Je remettrais » est…", opts:["un futur","un conditionnel"], ok:1,
          fb:"Un conditionnel : le « s » change tout. Le futur s'écrit « je remettrai »."},
       ]},
    ]
  },

  // ════════════════════════════════════════════════════════════════════════
  t3note: {
    eye:'Mini-leçon', tit:"Les six lignes d'une note d'absence",
    blocs:[
      {t:'texte', h:"Cinq lignes suffisent, mais il faut les cinq",
       p:"Une note d'absence est le plus court des écrits officiels : cinq ou six lignes, pas davantage. Ce qui la rend difficile n'est donc pas la longueur, c'est la présentation — savoir ce qui va en haut, ce qui va au milieu, ce qui va en bas, et ne rien oublier. Une note à laquelle il manque une ligne n'est pas une note incomplète : c'est une note qui ne fait pas ce qu'elle devrait faire. Sans date, elle ne prouve rien. Sans signature, elle ne vaut rien. Sans groupe, elle n'arrive nulle part.",
       note:"C'est le savoir du programme appelé « tenir compte de la présentation matérielle et de la mise en page ». Il ne s'agit pas de style : il s'agit de ce que le papier peut faire."},

      {t:'ana', h:"Le haut : la date, puis le destinataire",
       p:"Deux lignes, séparées par une ligne blanche. La date à droite ou à gauche, peu importe, mais toujours avec la ville.",
       mots:[["La ligne de date","Laval, le 16 septembre 2026"],["Le destinataire","Madame, Monsieur — ou : Au secrétariat du Centre",true],["Si un enseignant a vu la note","avec mention de son nom, en dessous"]],
       say:"La note tient en cinq lignes, datées et signées.",
       note:"On écrit « le 16 septembre », jamais « le 16 de septembre » ni « septembre 16 ». Et le mois ne prend pas de majuscule en français."},

      {t:'ana', h:"Le milieu : qui, ce qui est arrivé, ce qui suivra",
       p:"Trois phrases, dans cet ordre, et pas une de plus. C'est le corps de la note.",
       mots:[["Qui vous êtes","Je suis Nourhane Ouazzani, du groupe 6, francisation de jour."],["Ce qui est arrivé, au passé composé","J'ai été absente le lundi 14 septembre parce que mon fils est tombé malade.",true],["Ce que vous ferez, au futur","Je rattraperai la matière et je vous remettrai le papier de la clinique."]],
       say:"Le motif se dit en une seule phrase.",
       note:"Le groupe est aussi important que le nom. Dans un centre de mille élèves, un prénom seul ne mène à aucun dossier."},

      {t:'ana', h:"Le bas : la formule, la signature, la copie",
       p:"La formule de politesse tient en une ligne. La signature est manuscrite, sous le nom écrit en toutes lettres.",
       mots:[["La formule","Veuillez agréer mes salutations. — ou : Merci de votre compréhension."],["Le nom et la signature","Nourhane Ouazzani, groupe 6 — puis la signature à la main",true],["Avant de remettre","une photo ou une photocopie, pour vous"]],
       say:"Sans signature, la note reste une simple feuille.",
       note:"Une note tapée à l'ordinateur se signe quand même : on l'imprime et on signe à la main. Sans ce geste, ce n'est qu'un brouillon."},

      {t:'labo', h:"Ce qui arrive quand une ligne manque",
       p:"Choisissez la ligne manquante et écoutez ce que la note ne peut plus faire.",
       axes:[{id:'l', lbl:'Quelle ligne manque ?', opts:[
         ['a','la date'],
         ['b','le groupe'],
         ['c','le destinataire'],
         ['d','la signature'],
         ['e','la copie']]}],
       out:{
         a:{w:['une note'], say:"Sans date, personne ne sait quand la note a été écrite ni si elle est arrivée à temps.", n:"le secrétariat classe par date"},
         b:{w:['un poste'], say:"Sans le groupe, il faut chercher votre nom dans douze listes.", n:"un prénom ne mène à aucun dossier"},
         c:{w:['un message'], say:"Sans destinataire, la note ressemble à un brouillon et personne ne sait à qui la transmettre.", n:"Madame, Monsieur suffit"},
         d:{w:['une signature'], say:"Sans signature, la note n'est pas officielle : c'est une feuille et rien de plus.", n:"la signature se fait à la main"},
         e:{w:['une copie'], say:"Sans copie, vous n'avez plus rien le jour où le dossier dit le contraire.", n:"une photo prend cinq secondes"},
       },
       note:"Cinq lignes, cinq conséquences. Relisez votre note en vous posant ces cinq questions dans l'ordre : c'est plus rapide que de la recommencer."},

      {t:'ex', h:"À écouter et à répéter",
       p:"Les six lignes de la note de Nourhane.",
       rows:[
         ["Laval, le 16 septembre 2026.","la ville et la date"],
         ["Madame, Monsieur,","le destinataire"],
         ["Je suis Nourhane Ouazzani, du groupe 6.","qui vous êtes"],
         ["J'ai été absente le lundi 14 septembre parce que mon fils est tombé malade.","ce qui est arrivé"],
         ["Je rattraperai la matière et je vous remettrai le papier de la clinique.","ce qui suivra"],
         ["Veuillez agréer mes salutations.","la formule de fin"],
       ]},

      {t:'piege', h:"Trois pièges de la note",
       rows:[
         ["écrire le motif au présent","« je suis absente parce que mon fils est malade », pour une absence d'hier",
          "Une note remise après coup parle du passé : « j'ai été absente », « mon fils est tombé malade ». Le présent laisse croire que vous êtes absente aujourd'hui aussi."],
         ["signer d'un prénom","« Nourhane » seul, sans nom ni groupe",
          "Il y a plusieurs Nourhane dans un centre de mille élèves. Nom complet, groupe, et la signature en dessous."],
         ["remettre l'original sans copie","descendre au comptoir avec une seule feuille",
          "Le jour où le dossier dit « absence non motivée », c'est votre copie datée qui tranche. Une photo avec le téléphone, avant de sortir de la classe."],
       ]},

      {t:'check', h:"Est-ce que c'est clair maintenant ?",
       p:"Quatre questions rapides.",
       qs:[
         {q:"Que met-on sur la toute première ligne ?", opts:["son nom","la ville et la date"], ok:1,
          fb:"La ville et la date : Laval, le 16 septembre 2026."},
         {q:"Le motif d'une absence passée s'écrit…", opts:["au passé composé","au présent"], ok:0,
          fb:"Au passé composé : j'ai été absente, mon fils est tombé malade."},
         {q:"Une note tapée à l'ordinateur…", opts:["n'a pas besoin de signature","se signe à la main après impression"], ok:1,
          fb:"Elle se signe à la main. Sans signature, c'est un brouillon."},
         {q:"Que fait-on avant de remettre la note ?", opts:["une copie pour soi","rien de particulier"], ok:0,
          fb:"Une copie. C'est elle qui tranchera si le dossier dit le contraire."},
       ]},
    ]
  },

  // ════════════════════════════════════════════════════════════════════════
  t3ecrit: {
    eye:'Mini-leçon', tit:"Annoncer un abandon en trois phrases",
    blocs:[
      {t:'texte', h:"Le mot fait peur, et c'est pourtant lui qu'il faut écrire",
       p:"Beaucoup d'élèves cessent simplement de venir. Ils ne veulent pas écrire « j'abandonne », parce que le mot sonne comme un échec — et c'est justement ce qui arrive quand on ne l'écrit pas : le cours continue de compter des absences, et le relevé finira par porter un échec au lieu d'un abandon. Le mot est celui de la case dans le système, rien de plus. Le personnel l'entend dix fois par semaine et n'y met aucun jugement. Trois phrases suffisent, et elles vous laissent en bons termes avec un établissement où vous reviendrez peut-être.",
       note:"Un abandon annoncé avant la date limite ne laisse aucune trace négative. Après la date limite, il en laisse une. C'est la seule raison pour laquelle il faut se dépêcher."},

      {t:'ana', h:"Phrase 1 : le mot, et le nom du cours",
       p:"On nomme le cours exactement, parce qu'un élève peut être inscrit à deux choses en même temps — c'est le cas de Nourhane.",
       mots:[["La formule","Je vous écris pour abandonner le cours d'informatique du soir."],["Une variante","Je vous informe que j'abandonne le cours d'informatique du soir.",true],["Ce qui ne suffit pas","« Je ne pourrai plus venir le soir. »"]],
       say:"Un abandon annoncé par écrit n'est pas un échec.",
       note:"Si vous abandonnez un cours et que vous en gardez un autre, dites-le dans la même phrase : « je garde le cours de francisation de jour »."},

      {t:'ana', h:"Phrase 2 : la date d'effet",
       p:"Sans elle, le centre ne sait pas s'il doit vous compter présente la semaine prochaine, et votre place reste bloquée pour quelqu'un d'autre.",
       mots:[["Une date précise","À partir du 1er octobre."],["Une date déjà passée","Ma dernière présence était le 26 septembre.",true],["Le mot à éviter","« bientôt », « à la fin », « prochainement »"]],
       say:"La note tient en cinq lignes, datées et signées.",
       note:"On écrit « le 1er octobre », avec « er » en petit ou en toutes lettres. Les autres jours du mois s'écrivent sans rien : le 2 octobre, le 15 octobre."},

      {t:'ana', h:"Phrase 3 : le motif, court et général",
       p:"Personne ne vérifie, personne ne juge. Ce qu'on veut, c'est une ligne dans le dossier, pas une confession.",
       mots:[["Le travail","parce que mes horaires de travail ont changé"],["La famille","pour des raisons familiales",true],["La santé","pour des raisons de santé"],["La charge","parce que deux cours en même temps, c'est trop pour moi"]],
       say:"Le motif se dit en une seule phrase.",
       note:"La dernière est celle que le personnel entend le plus souvent, et celle qu'il respecte le plus : elle montre que vous avez évalué votre situation au lieu de disparaître."},

      {t:'labo', h:"Les trois phrases, et la quatrième facultative",
       p:"Choisissez une phrase et écoutez-la telle qu'elle s'écrit.",
       axes:[{id:'a', lbl:'Quelle phrase ?', opts:[
         ['a','phrase 1 · le mot et le cours'],
         ['b','phrase 2 · la date d\'effet'],
         ['c','phrase 3 · le motif'],
         ['d','la phrase qui garde la porte ouverte'],
         ['e','les quatre à la suite']]}],
       out:{
         a:{w:['un abandon'], say:"Je vous écris pour abandonner le cours d'informatique du soir.", n:"le mot exact, et le nom du cours"},
         b:{w:['une note'], say:"Cet abandon prend effet à partir du 1er octobre.", n:"une date, jamais « bientôt »"},
         c:{w:['un motif'], say:"J'abandonne ce cours parce que mes horaires de travail ont changé.", n:"une phrase, générale, et c'est assez"},
         d:{w:['une signature'], say:"Je souhaiterais me réinscrire à la prochaine session.", n:"elle transforme un départ en pause"},
         e:{w:['une copie'], say:"Je vous écris pour abandonner le cours d'informatique du soir. Cet abandon prend effet à partir du 1er octobre. J'abandonne ce cours parce que mes horaires de travail ont changé. Je souhaiterais me réinscrire à la prochaine session.", n:"quatre phrases, vingt secondes"},
       },
       note:"Quatre phrases, et la note est complète. Ajoutez la date en haut, le destinataire, votre nom et votre signature : la démarche est faite."},

      {t:'ex', h:"À écouter et à répéter",
       p:"Six phrases d'une note d'abandon.",
       rows:[
         ["Je vous écris pour abandonner le cours du soir.","le mot exact"],
         ["Cet abandon prend effet à partir du 1er octobre.","la date d'effet"],
         ["Ma dernière présence était le 26 septembre.","quand la date est déjà passée"],
         ["J'abandonne ce cours pour des raisons familiales.","un motif général"],
         ["Je garde le cours de francisation de jour.","ce que vous continuez"],
         ["Je souhaiterais me réinscrire à la prochaine session.","la porte laissée ouverte"],
       ]},

      {t:'piege', h:"Trois pièges de l'abandon",
       rows:[
         ["ne rien écrire du tout","cesser simplement de venir",
          "C'est le seul vrai piège, et il coûte cher : après quelques semaines, le cours s'inscrit comme un échec au relevé. Trois phrases l'évitent."],
         ["écrire une longue lettre d'explication","dix lignes de justifications",
          "Une note longue inquiète et demande une réponse. Trois phrases claires se traitent en une minute, et l'affaire est réglée le jour même."],
         ["oublier de dire ce qu'on garde","abandonner un cours et laisser croire qu'on part",
          "Si vous restez inscrite à autre chose, dites-le. Sans cela, le secrétariat peut fermer votre dossier au complet, et il faudra tout rouvrir."],
       ]},

      {t:'check', h:"Est-ce que c'est clair maintenant ?",
       p:"Quatre questions rapides.",
       qs:[
         {q:"Un abandon s'annonce…", opts:["par écrit","de vive voix"], ok:0,
          fb:"Par écrit, toujours. C'est le seul des trois motifs qui l'exige."},
         {q:"Que se passe-t-il si l'on cesse de venir sans rien dire ?", opts:["rien de particulier","le cours s'inscrit comme un échec"], ok:1,
          fb:"Il finit par s'inscrire comme un échec. C'est ce que l'écrit évite."},
         {q:"Combien de phrases suffisent ?", opts:["trois","une page"], ok:0,
          fb:"Trois : le mot et le cours, la date d'effet, le motif."},
         {q:"Le motif d'un abandon doit être…", opts:["détaillé et prouvé","court et général"], ok:1,
          fb:"Court et général. Personne ne vérifie et personne ne juge."},
       ]},
    ]
  },

};
