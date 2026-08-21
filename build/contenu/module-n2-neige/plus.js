const PLUS = {
  prSon: {
    eye:'Mini-leçon', tit:"« An » et « on » : deux sons du nez",
    blocs:[
      {t:'texte', h:"Deux sons qui décident du mot",
       p:"Le français du Québec a des sons qui passent par le nez. Deux d'entre eux reviennent tout l'hiver : celui de <b>vent</b> et celui de <b>bonjour</b>. Ils se ressemblent, mais ils ne veulent pas dire la même chose. <b>Le temps</b> et <b>ils sont</b> ne se disent pas pareil, et <b>janvier</b> ne se dit pas comme <b>jonquière</b>.",
       note:"Commencer par faire écouter les deux sons en série, sans explication. L'oreille se règle avant que la règle n'ait un sens."},

      {t:'ana', h:"Le son de « vent » : la bouche grande ouverte",
       p:"C'est le son de la météo et des mois de l'année.",
       mots:[["On dit","le v{en}t — la bouche s'ouvre"],["Aussi","le t{em}ps · print{em}ps"],["Aussi","j{an}vier · nov{em}bre · déc{em}bre"],["On ne dit pas","« le vont » ni « le tomps »",true]],
       say:"Le vent. Le temps. Janvier. Novembre. Décembre.",
       note:"Faire poser la main sous le menton : la mâchoire descend. C'est le repère le plus sûr pour ce son."},

      {t:'ana', h:"Le son de « bonjour » : les lèvres en rond",
       p:"C'est le son des salutations et des verbes en « nous ».",
       mots:[["On dit","b{on}jour — les lèvres font un rond"],["Aussi","l{on}g · ils s{on}t · le n{om}bre"],["Aussi","n{ou}s mont{on}s · n{ou}s sort{on}s"],["On ne dit pas","« banjour » ni « ils sant »",true]],
       say:"Bonjour. Long. Ils sont. Nous montons.",
       note:"Faire avancer les lèvres comme pour siffler. Le son sort plus petit, plus fermé que celui de « vent »."},

      {t:'ana', h:"Les quatre écritures du son de « vent »",
       p:"Un seul son, quatre façons de l'écrire.",
       mots:[["an","j{an}vier · un {an}"],["am","une l{am}pe · une ch{am}bre"],["en","le v{en}t · l'arg{en}t"],["em","le t{em}ps · nov{em}bre · print{em}ps"],["La règle du m","devant b et p, on écrit m, jamais n",true]],
       say:"Janvier. Une lampe. Le vent. Novembre.",
       note:"La règle « m devant b et p » explique novembre, décembre, printemps, chambre, lampe. Elle vaut aussi pour le son « on » : nombre, tomber."},

      {t:'labo', h:"Écoute les deux sons",
       p:"Choisis un son et une façon de l'entendre.",
       axes:[
         {id:'p', lbl:'Quel son ?', opts:[
           ['a','le son de « vent »'],
           ['b','le son de « bonjour »'],
           ['c','les deux, à la suite']]},
         {id:'q', lbl:'Dans quoi ?', opts:[['1','un mot seul'],['2','un mot de la météo'],['3','une phrase']]}],
       out:{
         a1:{w:["le vent"], say:"Le vent.", n:'la bouche est grande ouverte'},
         a2:{w:["le temps, janvier"], say:"Le temps. Janvier.", n:'deux mots de la météo, même son'},
         a3:{w:["Le vent est froid en janvier."], say:"Le vent est froid en janvier.", n:'trois fois le même son dans une phrase'},
         b1:{w:["bonjour"], say:"Bonjour.", n:'les lèvres font un rond'},
         b2:{w:["long, ils sont"], say:"Long. Ils sont.", n:'même son, deux mots courants'},
         b3:{w:["Bonjour, ils sont dehors."], say:"Bonjour, ils sont dehors.", n:'le son « on » trois fois'},
         c1:{w:["vent, bonjour"], say:"Vent. Bonjour.", n:'la paire à entendre en premier'},
         c2:{w:["le temps, ils sont"], say:"Le temps. Ils sont.", n:'la paire la plus difficile du module'},
         c3:{w:["Bonjour ! Il vente beaucoup ce matin."], say:"Bonjour ! Il vente beaucoup ce matin.", n:'les deux sons dans la même phrase'},
       },
       note:"Neuf extraits. Les faire écouter les yeux fermés, puis lever une main pour « an », deux pour « on »."},

      {t:'ex', h:"À écouter et à répéter",
       p:"Six mots de l'hiver, trois par son.",
       rows:[
         ["le vent","son de « an »"],
         ["le temps","son de « an »"],
         ["janvier","son de « an »"],
         ["bonjour","son de « on »"],
         ["ils sont","son de « on »"],
         ["nous montons","son de « on »"],
       ]},

      {t:'piege', h:"Trois pièges à connaître",
       rows:[
         ["dire « le vont » pour « le vent »","la bouche ne s'ouvre pas assez",
          "Beaucoup d'élèves ferment les lèvres par habitude. Ouvre grand la bouche, comme chez le dentiste, et le son sort juste."],
         ["prononcer le n ou le m à la fin","le son passe par le nez, pas par la langue",
          "Dans « vent », on n'entend pas de « n » à la fin. La langue ne touche rien. Si tu entends « vé-neu », c'est trop."],
         ["écrire « tenps » au lieu de « temps »","devant b et p, on écrit m",
          "C'est pourquoi on écrit novembre, décembre, printemps, chambre. Une seule règle, et six mots de l'hiver deviennent faciles."],
       ]},

      {t:'check', h:"Est-ce que c'est clair maintenant ?",
       p:"Quatre questions rapides.",
       qs:[
         {q:"« Janvier » a le son de…", opts:["vent","bonjour"], ok:0,
          fb:"Le son de « vent » : la bouche s'ouvre grand."},
         {q:"« Nous montons » a le son de…", opts:["bonjour","vent"], ok:0,
          fb:"Les lèvres font un rond, comme dans bonjour."},
         {q:"On écrit « nove___bre » avec…", opts:["m","n"], ok:0,
          fb:"Devant b et p, on écrit toujours m."},
         {q:"Dans « le temps », on entend le « s » de la fin ?", opts:["non","oui"], ok:0,
          fb:"Ni le « p » ni le « s ». On dit « le tan »."},
       ]},
    ]
  },

  prIl: {
    eye:'Mini-leçon', tit:"Le « il » de la météo",
    blocs:[
      {t:'texte', h:"Un « il » qui n'est personne",
       p:"En français, la météo se dit toujours avec <b>il</b> : il neige, il pleut, il vente, il fait froid. Ce « il » ne remplace personne. Ce n'est ni un homme, ni le ciel, ni le temps — c'est un mot obligatoire, et il ne change jamais. On ne dit pas « la neige neige » ni « ça fait froid ».",
       note:"C'est un savoir du programme : la phrase impersonnelle. Insister sur le mot « obligatoire » plutôt que sur l'explication grammaticale."},

      {t:'ana', h:"Un seul verbe suffit",
       p:"Trois verbes disent le temps à eux seuls.",
       mots:[["On dit","Il {neige}."],["Aussi","Il {pleut}."],["Aussi","Il {vente}."],["On ne dit pas","« la neige tombe du ciel neige »",true]],
       say:"Il neige. Il pleut. Il vente.",
       note:"Trois verbes, trois phrases de deux mots. C'est la phrase française la plus courte qui existe."},

      {t:'ana', h:"« Il fait » + un mot",
       p:"Avec « il fait », on ajoute un mot qui dit comment c'est.",
       mots:[["On dit","Il {fait} froid."],["Aussi","Il {fait} chaud · Il {fait} beau"],["Aussi","Il {fait} mauvais · Il {fait} soleil"],["Aussi","Il {fait} moins huit degrés"],["On ne dit pas","« il est froid » pour la météo",true]],
       say:"Il fait froid. Il fait chaud. Il fait beau. Il fait moins huit degrés.",
       note:"« Il est froid » existe, mais parle d'un objet : le café est froid. La météo prend toujours « il fait »."},

      {t:'ana', h:"« Il y a » + une chose",
       p:"Avec « il y a », on nomme ce qu'il y a dans le ciel ou dans la rue.",
       mots:[["On dit","Il {y a} du soleil."],["Aussi","Il {y a} des nuages · Il {y a} du vent"],["Aussi","Il {y a} de la neige · Il {y a} de la glace"],["Aussi","Il {y a} une tempête"],["On ne dit pas","« il a du soleil » : le y ne se saute pas",true]],
       say:"Il y a du soleil. Il y a des nuages. Il y a de la neige.",
       note:"Faire remarquer les petits mots : du soleil, des nuages, de la neige. Ils changent, le « il y a » ne change pas."},

      {t:'labo', h:"Dis le temps qu'il fait",
       p:"Choisis un temps et une façon de le dire.",
       axes:[
         {id:'p', lbl:'Quel temps ?', opts:[
           ['a','la neige'],
           ['b','la pluie'],
           ['c','le vent'],
           ['d','le soleil']]},
         {id:'q', lbl:'Comment ?', opts:[['1','avec un verbe seul'],['2','avec « il y a »'],['3','la question']]}],
       out:{
         a1:{w:["Il neige."], say:"Il neige.", n:'deux mots, et tout est dit'},
         a2:{w:["Il y a de la neige."], say:"Il y a de la neige.", n:'la neige est déjà par terre'},
         a3:{w:["Est-ce qu'il neige ?"], say:"Est-ce qu'il neige ?", n:'la question du matin'},
         b1:{w:["Il pleut."], say:"Il pleut.", n:'le verbe pleuvoir, seul'},
         b2:{w:["Il y a de la pluie."], say:"Il y a de la pluie.", n:'la même chose, avec un nom'},
         b3:{w:["Est-ce qu'il pleut ?"], say:"Est-ce qu'il pleut ?", n:'à poser avant de sortir'},
         c1:{w:["Il vente."], say:"Il vente.", n:'très employé au Québec'},
         c2:{w:["Il y a du vent."], say:"Il y a du vent.", n:'la forme la plus courante à la radio'},
         c3:{w:["Est-ce qu'il vente ?"], say:"Est-ce qu'il vente ?", n:'la question qui décide de la tuque'},
         d1:{w:["Il fait soleil."], say:"Il fait soleil.", n:'ici, on emploie « il fait »'},
         d2:{w:["Il y a du soleil."], say:"Il y a du soleil.", n:'les deux se disent'},
         d3:{w:["Est-ce qu'il fait soleil ?"], say:"Est-ce qu'il fait soleil ?", n:'la bonne nouvelle du bulletin'},
       },
       note:"Douze extraits. Faire dire les quatre temps debout, en montrant la fenêtre."},

      {t:'ex', h:"À écouter et à répéter",
       p:"Les six phrases de la météo.",
       rows:[
         ["Il neige.","un verbe seul"],
         ["Il pleut.","un verbe seul"],
         ["Il vente.","un verbe seul"],
         ["Il fait froid.","il fait + un mot"],
         ["Il fait beau.","il fait + un mot"],
         ["Il y a des nuages.","il y a + une chose"],
       ]},

      {t:'piege', h:"Trois pièges à connaître",
       rows:[
         ["oublier le « il »","il est obligatoire",
          "« Neige aujourd'hui » ne se dit pas. Même si le sens se devine, la phrase n'existe pas. Toujours : <b>il</b> neige."],
         ["dire « il est froid » pour la météo","c'est « il fait froid »",
          "« Il est froid » parle d'une chose : le café est froid, la chambre est froide. Le temps, lui, prend toujours <b>il fait</b>."],
         ["dire « il a du soleil »","le petit « y » ne se saute pas",
          "On dit <b>il y a</b> du soleil. Le « y » est court, presque muet, mais il est là. Sans lui, la phrase parle de quelqu'un qui possède du soleil."],
       ]},

      {t:'check', h:"Est-ce que c'est clair maintenant ?",
       p:"Quatre questions rapides.",
       qs:[
         {q:"Pour dire qu'il tombe de la neige, je dis…", opts:["Il neige.","La neige tombe neige."], ok:0,
          fb:"Un verbe et le mot « il ». Rien d'autre."},
         {q:"Pour la température, je dis…", opts:["Il fait froid.","Il est froid."], ok:0,
          fb:"La météo prend « il fait », toujours."},
         {q:"Pour parler des nuages, je dis…", opts:["Il y a des nuages.","Il a des nuages."], ok:0,
          fb:"« Il y a » : le petit « y » ne se saute jamais."},
         {q:"Ce « il » de la météo remplace…", opts:["personne","le ciel"], ok:0,
          fb:"Il ne remplace personne. C'est un mot obligatoire, et c'est tout."},
       ]},
    ]
  },

  t1degre: {
    eye:'Mini-leçon', tit:"Lire une température au Québec",
    blocs:[
      {t:'texte', h:"Un nombre, et un signe devant",
       p:"Au Québec, la température se dit en degrés Celsius, et le nombre vient presque toujours avec un signe. <b>Moins huit</b> et <b>plus huit</b>, ce n'est pas la même journée : entre les deux, il y a seize degrés et deux manteaux différents. Le signe est plus important que le nombre.",
       note:"Beaucoup d'élèves arrivent de pays où la température ne descend jamais sous zéro. Le mot « moins » est une nouveauté réelle, pas une révision."},

      {t:'ana', h:"Zéro : la ligne du gel",
       p:"À zéro degré, l'eau devient de la glace.",
       mots:[["On dit","{zéro} degré — au singulier"],["Au-dessus","la pluie reste de la pluie"],["Au-dessous","la pluie devient de la neige"],["Sur le trottoir","à zéro, l'eau gèle et ça devient glissant"],["On ne dit pas","« zéro degrés » avec un s",true]],
       say:"Zéro degré. La pluie devient de la neige.",
       note:"Le passage de la pluie à la neige autour de zéro est le meilleur exemple concret. Le montrer avec le bulletin de mercredi."},

      {t:'ana', h:"Sous zéro : moins",
       p:"On dit « moins » devant le nombre.",
       mots:[["On dit","Il fait {moins} huit."],["Aussi","{moins} deux · {moins} seize · {moins} trente"],["Plus grand, plus froid","{moins} trente est plus froid que {moins} dix"],["À l'écrit","−8 · −16 · −30"],["On ne dit pas","« huit moins » ni « il fait huit sous zéro »",true]],
       say:"Il fait moins huit. Moins seize. Moins trente.",
       note:"Le renversement est difficile : un grand nombre veut dire un grand froid. Le faire ordonner à voix haute, du plus doux au plus froid."},

      {t:'ana', h:"Au-dessus de zéro : plus, ou rien",
       p:"On peut dire « plus », ou seulement le nombre.",
       mots:[["On dit","Il fait {plus} quatre."],["Ou simplement","Il fait {quatre} degrés."],["En été","{plus} vingt-cinq · {plus} trente"],["À l'écrit","+4 · +25 · 30"],["On ne dit pas","« plus » quand il est déjà clair qu'il fait chaud",true]],
       say:"Il fait plus quatre. Il fait quatre degrés. Il fait trente degrés.",
       note:"En été, personne ne dit « plus trente » : on dit « trente ». Le « plus » sert surtout quand la température tourne autour de zéro."},

      {t:'labo', h:"Lis la température",
       p:"Choisis une température et une façon de la dire.",
       axes:[
         {id:'p', lbl:'Quelle température ?', opts:[
           ['a','−8 degrés'],
           ['b','0 degré'],
           ['c','+4 degrés'],
           ['d','+30 degrés']]},
         {id:'q', lbl:'Comment ?', opts:[['1','le nombre seul'],['2','la phrase complète'],['3','ce que ça veut dire']]}],
       out:{
         a1:{w:["moins huit"], say:"Moins huit.", n:'le signe se dit avant le nombre'},
         a2:{w:["Il fait moins huit degrés."], say:"Il fait moins huit degrés.", n:'la phrase du bulletin de lundi'},
         a3:{w:["Il neige. Je mets ma tuque."], say:"Il neige. Je mets ma tuque.", n:'sous zéro, la neige reste'},
         b1:{w:["zéro degré"], say:"Zéro degré.", n:'degré au singulier'},
         b2:{w:["Il fait zéro degré."], say:"Il fait zéro degré.", n:'la ligne du gel'},
         b3:{w:["L'eau gèle. Le trottoir est glissant."], say:"L'eau gèle. Le trottoir est glissant.", n:'la journée la plus dangereuse à pied'},
         c1:{w:["plus quatre"], say:"Plus quatre.", n:'au-dessus de zéro'},
         c2:{w:["Il fait quatre degrés."], say:"Il fait quatre degrés.", n:'on peut laisser tomber le « plus »'},
         c3:{w:["Il pleut. La neige fond."], say:"Il pleut. La neige fond.", n:'le temps du mois d’avril'},
         d1:{w:["trente degrés"], say:"Trente degrés.", n:'personne ne dit « plus trente »'},
         d2:{w:["Il fait trente degrés."], say:"Il fait trente degrés.", n:'une journée de juillet'},
         d3:{w:["Il fait chaud. Je sors sans manteau."], say:"Il fait chaud. Je sors sans manteau.", n:'l’été du Québec, court mais chaud'},
       },
       note:"Douze extraits. Faire ranger les quatre températures dans l'ordre, du plus froid au plus chaud, avant d'écouter."},

      {t:'ex', h:"À écouter et à répéter",
       p:"Six températures d'une année au Québec.",
       rows:[
         ["Il fait moins trente.","janvier, une journée très froide"],
         ["Il fait moins huit.","une journée d'hiver ordinaire"],
         ["Il fait zéro degré.","la neige devient de l'eau"],
         ["Il fait plus quatre.","le mois d'avril"],
         ["Il fait vingt degrés.","une belle journée de juin"],
         ["Il fait trente degrés.","juillet, il fait chaud"],
       ]},

      {t:'piege', h:"Trois pièges à connaître",
       rows:[
         ["croire que moins trente est moins froid que moins dix","c'est le contraire",
          "Plus le nombre est grand après « moins », plus il fait froid. Moins trente est une journée où on ne sort pas longtemps."],
         ["oublier de dire « moins »","le sens se renverse",
          "« Il fait huit » veut dire huit degrés au-dessus de zéro : on sort en veste. « Il fait moins huit », c'est manteau, tuque et mitaines."],
         ["dire « zéro degrés »","au singulier",
          "Zéro prend le singulier : <b>zéro degré</b>. À partir de deux, on met le s : deux degrés, huit degrés."],
       ]},

      {t:'check', h:"Est-ce que c'est clair maintenant ?",
       p:"Quatre questions rapides.",
       qs:[
         {q:"Quelle journée est la plus froide ?", opts:["moins vingt","moins cinq"], ok:0,
          fb:"Après « moins », le grand nombre veut dire le grand froid."},
         {q:"−16 se dit…", opts:["moins seize","seize moins"], ok:0,
          fb:"Le signe se dit avant le nombre, toujours."},
         {q:"À zéro degré, la pluie…", opts:["devient de la neige","reste de la pluie"], ok:0,
          fb:"Zéro, c'est la ligne du gel."},
         {q:"En juillet, on dit…", opts:["il fait trente degrés","il fait plus trente degrés"], ok:0,
          fb:"Quand il fait clairement chaud, le « plus » ne se dit pas."},
       ]},
    ]
  },

  t1saison: {
    eye:'Mini-leçon', tit:"En hiver, au printemps",
    blocs:[
      {t:'texte', h:"Quatre saisons, un seul mot qui change",
       p:"Trois saisons prennent <b>en</b> : en hiver, en été, en automne. Une seule prend <b>au</b> : au printemps. Il n'y a pas de raison à apprendre — il y a une exception à retenir. Au Québec, ces quatre mots servent tous les jours, parce que la température change beaucoup d'une saison à l'autre.",
       note:"Ne pas chercher à expliquer l'exception. La faire répéter en série : en hiver, au printemps, en été, en automne."},

      {t:'ana', h:"Les trois saisons en « en »",
       p:"Hiver, été, automne prennent « en ».",
       mots:[["On dit","{en} hiver — décembre, janvier, février"],["Aussi","{en} été — juin, juillet, août"],["Aussi","{en} automne — septembre, octobre, novembre"],["On ne dit pas","« au hiver » ni « dans l'été »",true]],
       say:"En hiver. En été. En automne.",
       note:"Faire nommer les mois de chaque saison. Le calendrier fixe le mot mieux que la règle."},

      {t:'ana', h:"La seule exception : au printemps",
       p:"Le printemps prend « au », et lui seul.",
       mots:[["On dit","{au} printemps — mars, avril, mai"],["C'est la seule","les trois autres prennent {en}"],["Au Québec","{au} printemps, la neige fond et la rue est pleine d'eau"],["On ne dit pas","« en printemps »",true]],
       say:"Au printemps. Au printemps, la neige fond.",
       note:"Une seule exception dans tout le système : la nommer comme telle rassure plus qu'elle n'inquiète."},

      {t:'ana', h:"Devant un mois, toujours « en »",
       p:"Les douze mois prennent « en », sans exception.",
       mots:[["On dit","{en} janvier · {en} février · {en} mars"],["Aussi","{en} juillet, il fait trente degrés"],["Aussi","{en} novembre, la première neige tombe"],["On peut aussi dire","{au} mois de janvier"],["On ne dit pas","« à janvier »",true]],
       say:"En janvier. En juillet. En novembre. Au mois de janvier.",
       note:"« Au mois de » est une porte de sortie utile quand on hésite : elle marche avec les douze mois."},

      {t:'labo', h:"Une saison, un temps",
       p:"Choisis une saison et ce que tu veux en dire.",
       axes:[
         {id:'p', lbl:'Quelle saison ?', opts:[
           ["a","l'hiver"],
           ['b','le printemps'],
           ["c","l'été"],
           ["d","l'automne"]]},
         {id:'q', lbl:'Quoi ?', opts:[['1','le petit mot'],['2','le temps qu\'il fait'],['3','les mois']]}],
       out:{
         a1:{w:["en hiver"], say:"En hiver.", n:'trois saisons sur quatre : en'},
         a2:{w:["En hiver, il neige et il fait moins vingt."], say:"En hiver, il neige et il fait moins vingt.", n:'la saison la plus longue au Québec'},
         a3:{w:["décembre, janvier, février"], say:"Décembre, janvier, février.", n:'trois mois de neige'},
         b1:{w:["au printemps"], say:"Au printemps.", n:'la seule saison en « au »'},
         b2:{w:["Au printemps, la neige fond."], say:"Au printemps, la neige fond.", n:'la rue est pleine d’eau'},
         b3:{w:["mars, avril, mai"], say:"Mars, avril, mai.", n:'la température remonte'},
         c1:{w:["en été"], say:"En été.", n:'« en » devant une voyelle aussi'},
         c2:{w:["En été, il fait chaud. Il fait trente degrés."], say:"En été, il fait chaud. Il fait trente degrés.", n:'court, mais vraiment chaud'},
         c3:{w:["juin, juillet, août"], say:"Juin, juillet, août.", n:'les trois mois sans manteau'},
         d1:{w:["en automne"], say:"En automne.", n:'« en », comme hiver et été'},
         d2:{w:["En automne, il pleut souvent et il vente."], say:"En automne, il pleut souvent et il vente.", n:'la saison du parapluie'},
         d3:{w:["septembre, octobre, novembre"], say:"Septembre, octobre, novembre.", n:'la première neige arrive à la fin'},
       },
       note:"Douze extraits. Faire dire à chacun sa saison préférée avec le bon petit mot, et pourquoi, en une phrase."},

      {t:'ex', h:"À écouter et à répéter",
       p:"Les quatre saisons et deux mois.",
       rows:[
         ["En hiver, il neige.","en"],
         ["Au printemps, la neige fond.","au — la seule"],
         ["En été, il fait chaud.","en"],
         ["En automne, il pleut.","en"],
         ["En janvier, il fait très froid.","en, devant un mois"],
         ["Au mois de juillet, il fait trente degrés.","au mois de + un mois"],
       ]},

      {t:'piege', h:"Trois pièges à connaître",
       rows:[
         ["dire « en printemps »","c'est « au printemps »",
          "C'est la seule saison qui prend <b>au</b>. Les trois autres prennent <b>en</b>. Il n'y a rien à comprendre : il faut le retenir."],
         ["dire « à janvier »","les mois prennent en",
          "On dit <b>en</b> janvier, ou <b>au mois de</b> janvier. Jamais « à janvier »."],
         ["croire que l'automne est doux","au Québec, il vente et il pleut",
          "En novembre, il fait déjà autour de zéro et la première neige tombe. Le manteau d'hiver sort souvent avant l'hiver."],
       ]},

      {t:'check', h:"Est-ce que c'est clair maintenant ?",
       p:"Quatre questions rapides.",
       qs:[
         {q:"___ hiver, il neige.", opts:["En","Au"], ok:0,
          fb:"Hiver, été, automne prennent « en »."},
         {q:"___ printemps, la neige fond.", opts:["Au","En"], ok:0,
          fb:"Le printemps est la seule saison en « au »."},
         {q:"___ juillet, il fait chaud.", opts:["En","À"], ok:0,
          fb:"Les douze mois prennent « en »."},
         {q:"La première neige tombe souvent…", opts:["en novembre","en janvier"], ok:0,
          fb:"Au Québec, novembre est déjà un mois de neige."},
       ]},
    ]
  },

  t1notes: {
    eye:'Mini-leçon', tit:"Prendre un bulletin météo en note",
    blocs:[
      {t:'texte', h:"Trois choses, et rien d'autre",
       p:"Un bulletin météo à la radio dure vingt secondes et passe vite. On n'écrit pas les phrases : on écrit <b>la ville</b>, <b>le temps</b> et <b>la température</b>. Trois mots suffisent à retenir toute la journée, et ils tiennent sur un coin de papier.",
       note:"Faire écouter le bulletin du dialogue une deuxième fois, crayon en main. La prise de note est un geste : elle s'apprend en le faisant."},

      {t:'ana', h:"D'abord la ville",
       p:"Le bulletin ne dit pas la même chose partout au Québec.",
       mots:[["On entend","À {Montréal}, neige."],["Aussi","À {Québec}, moins seize."],["Aussi","En {Gaspésie}, du vent."],["Ce qu'on écrit","Montréal — un seul mot"],["On n'écrit pas","toute la phrase du bulletin",true]],
       say:"À Montréal, neige. À Québec, moins seize.",
       note:"Nommer trois ou quatre villes proches du centre. Un élève doit reconnaître la sienne au milieu d'une liste."},

      {t:'ana', h:"Ensuite le temps, en un mot",
       p:"Le mot du temps est court : c'est celui qu'il faut attraper.",
       mots:[["On entend","{neige} · {pluie} · {soleil}"],["Aussi","{nuages} · {vent}"],["Ce qu'on écrit","neige — pas « il neige aujourd'hui »"],["Un dessin marche aussi","un flocon, une goutte, un rond"],["On n'écrit pas","des phrases complètes : le bulletin va trop vite",true]],
       say:"Neige. Pluie. Soleil. Nuages. Vent.",
       note:"Autoriser le dessin. Au niveau 2, un flocon dessiné est une note valable et beaucoup plus rapide qu'un mot."},

      {t:'ana', h:"Enfin la température, avec son signe",
       p:"Le nombre ne vaut rien sans le signe qui est devant.",
       mots:[["On entend","{moins huit} degrés"],["Ce qu'on écrit","−8"],["Aussi","+4 pour {plus quatre}"],["Après aujourd'hui","le bulletin donne toujours demain"],["On n'écrit pas","8 tout seul : le signe se perd",true]],
       say:"Moins huit degrés. Plus quatre degrés.",
       note:"Le signe oublié est l'erreur la plus fréquente et la plus coûteuse : elle change le manteau du lendemain."},

      {t:'labo', h:"Écoute et note",
       p:"Choisis un jour et ce que tu veux noter.",
       axes:[
         {id:'p', lbl:'Quel jour ?', opts:[
           ["a","aujourd'hui"],
           ['b','demain'],
           ['c','une autre ville']]},
         {id:'q', lbl:'Quoi ?', opts:[['1','le temps'],['2','la température'],['3','le bulletin en entier']]}],
       out:{
         a1:{w:["neige"], say:"Neige.", n:'un mot, pas une phrase'},
         a2:{w:["moins huit"], say:"Moins huit.", n:'le signe d’abord'},
         a3:{w:["À Montréal, neige, moins huit degrés."], say:"À Montréal, neige, moins huit degrés.", n:'ville, temps, température'},
         b1:{w:["soleil"], say:"Soleil.", n:'la bonne nouvelle de demain'},
         b2:{w:["moins deux"], say:"Moins deux.", n:'six degrés de plus qu’aujourd’hui'},
         b3:{w:["Demain, soleil, moins deux degrés."], say:"Demain, soleil, moins deux degrés.", n:'le bulletin donne toujours le lendemain'},
         c1:{w:["vent"], say:"Vent.", n:'le mot qu’on entend pour la Gaspésie'},
         c2:{w:["moins seize"], say:"Moins seize.", n:'la température de Québec ce matin'},
         c3:{w:["À Québec, vent, moins seize degrés."], say:"À Québec, vent, moins seize degrés.", n:'même forme, autre ville'},
       },
       note:"Neuf extraits. Les faire écouter deux fois : la première pour entendre, la seconde pour écrire."},

      {t:'ex', h:"À écouter et à répéter",
       p:"Six bulletins de vingt secondes.",
       rows:[
         ["À Montréal, neige, moins huit.","ville, temps, température"],
         ["Demain, soleil, moins deux.","le lendemain"],
         ["À Québec, moins seize.","une autre ville"],
         ["Mercredi, nuages, zéro degré.","la ligne du gel"],
         ["Jeudi, pluie, plus quatre.","au-dessus de zéro"],
         ["Vendredi, vent et neige, moins quatorze.","deux mots de temps"],
       ]},

      {t:'piege', h:"Trois pièges à connaître",
       rows:[
         ["écrire des phrases","trois mots suffisent",
          "Pendant que tu écris « il neige aujourd'hui », le bulletin est déjà rendu à demain. Écris <b>neige</b>, et écoute la suite."],
         ["oublier le signe de la température","8 et −8 ne sont pas la même journée",
          "Un nombre sans signe ne veut rien dire au Québec. Écris toujours le − ou le +, même vite, même mal."],
         ["arrêter d'écouter après aujourd'hui","demain vient tout de suite après",
          "Le bulletin donne presque toujours le lendemain dans la même minute. C'est ce qui décide de ce que tu prépares le soir."],
       ]},

      {t:'check', h:"Est-ce que c'est clair maintenant ?",
       p:"Quatre questions rapides.",
       qs:[
         {q:"Dans un bulletin, on note…", opts:["la ville, le temps, la température","toutes les phrases"], ok:0,
          fb:"Trois choses, et rien d'autre."},
         {q:"Pour « moins huit degrés », j'écris…", opts:["−8","8"], ok:0,
          fb:"Le signe fait partie du nombre."},
         {q:"Pour le temps, j'écris…", opts:["neige","il neige aujourd'hui à Montréal"], ok:0,
          fb:"Un mot. Le bulletin ne t'attend pas."},
         {q:"Après aujourd'hui, le bulletin donne…", opts:["demain","rien"], ok:0,
          fb:"Il faut écouter jusqu'au bout : demain arrive tout de suite après."},
       ]},
    ]
  },

  t2faut: {
    eye:'Mini-leçon', tit:"Il faut, je mets, mets",
    blocs:[
      {t:'texte', h:"Trois façons de dire quoi mettre",
       p:"Devant la porte, le matin, on dit trois choses différentes : ce qui vaut pour tout le monde (<b>il faut</b> une tuque), ce que je fais moi (<b>je mets</b> mes bottes), et ce que je demande à quelqu'un (<b>mets</b> tes mitaines). Trois formes courtes, et l'hiver devient dicible.",
       note:"Les trois formes sont des savoirs du programme : l'auxiliaire de modalité, l'indicatif présent, l'impératif. Les présenter ensemble parce qu'elles se disent ensemble."},

      {t:'ana', h:"Une règle pour tout le monde : il faut",
       p:"Après « il faut », le verbe ne change jamais.",
       mots:[["On dit","{Il faut} mettre une tuque."],["Aussi","{Il faut} porter des bottes."],["Aussi","{Il faut} rester à la maison."],["Le verbe reste entier","mettre · porter · rester · sortir"],["On ne dit pas","« il faut je mets »",true]],
       say:"Il faut mettre une tuque. Il faut rester à la maison.",
       note:"« Il faut » est un autre « il » impersonnel, comme celui de la météo. Le rapprochement aide : même mot, même absence de personne."},

      {t:'ana', h:"Ce que je fais, moi : je mets",
       p:"Le verbe « mettre » au présent, pour parler de soi.",
       mots:[["On dit","{Je mets} mon manteau."],["Aussi","{Tu mets} ta tuque."],["Aussi","{Il met} ses bottes."],["Au pluriel","{Nous mettons} · {Vous mettez} · {Ils mettent}"],["On ne dit pas","« je met » sans s",true]],
       say:"Je mets mon manteau. Tu mets ta tuque. Il met ses bottes.",
       note:"Écrire les six formes au tableau. « Je mets » et « il met » se disent pareil, mais ne s'écrivent pas pareil."},

      {t:'ana', h:"Un ordre court : mets, mettez",
       p:"Pour dire à quelqu'un de le faire, on enlève le « tu » ou le « vous ».",
       mots:[["À quelqu'un qu'on tutoie","{Mets} tes mitaines !"],["À quelqu'un qu'on vouvoie","{Mettez} un foulard."],["Aussi","{Prends} ton parapluie. · {Restez} à la maison."],["Ce n'est pas impoli","c'est court, et on ajoute « s'il vous plaît »"],["On ne dit pas","« tu mets tes mitaines ! » pour donner un ordre",true]],
       say:"Mets tes mitaines ! Mettez un foulard. Restez à la maison.",
       note:"Au Québec, l'impératif est très employé entre proches et reste poli avec « s'il vous plaît ». Le dire évite un malaise."},

      {t:'labo', h:"Habille-toi pour dehors",
       p:"Choisis un vêtement et une façon d'en parler.",
       axes:[
         {id:'p', lbl:'Quel vêtement ?', opts:[
           ['a','la tuque'],
           ['b','les mitaines'],
           ['c','les bottes'],
           ["d","le manteau d'hiver"]]},
         {id:'q', lbl:'Comment ?', opts:[['1','la règle'],['2','moi'],['3','un ordre']]}],
       out:{
         a1:{w:["Il faut mettre une tuque."], say:"Il faut mettre une tuque.", n:'le verbe reste entier'},
         a2:{w:["Je mets ma tuque."], say:"Je mets ma tuque.", n:'je mets, avec un s'},
         a3:{w:["Mets ta tuque !"], say:"Mets ta tuque !", n:'sans « tu » devant'},
         b1:{w:["Il faut porter des mitaines."], say:"Il faut porter des mitaines.", n:'vrai pour tout le monde'},
         b2:{w:["Je mets mes mitaines."], say:"Je mets mes mitaines.", n:'mes, parce qu’il y en a deux'},
         b3:{w:["Mets tes mitaines !"], say:"Mets tes mitaines !", n:'ce que Zina dit à Youssef'},
         c1:{w:["Il faut mettre des bottes."], say:"Il faut mettre des bottes.", n:'avec de la neige, c’est une règle'},
         c2:{w:["Je mets mes bottes."], say:"Je mets mes bottes.", n:'tous les matins de l’hiver'},
         c3:{w:["Mettez vos bottes."], say:"Mettez vos bottes.", n:'la forme polie, à quelqu’un qu’on vouvoie'},
         d1:{w:["Il faut mettre un manteau d'hiver."], say:"Il faut mettre un manteau d'hiver.", n:'sous zéro, le manteau d’automne ne suffit plus'},
         d2:{w:["Je mets mon manteau d'hiver."], say:"Je mets mon manteau d'hiver.", n:'mon, parce que manteau est masculin'},
         d3:{w:["Mettez votre manteau, il fait moins huit."], say:"Mettez votre manteau, il fait moins huit.", n:'un ordre avec sa raison'},
       },
       note:"Douze extraits. Faire jouer la scène de la porte à deux : l'un donne les ordres, l'autre s'habille."},

      {t:'ex', h:"À écouter et à répéter",
       p:"Six phrases du matin.",
       rows:[
         ["Il faut mettre une tuque.","une règle"],
         ["Il faut rester à la maison.","un jour de tempête"],
         ["Je mets mes bottes.","moi"],
         ["Je mets mon manteau d'hiver.","moi"],
         ["Mets tes mitaines !","un ordre, à quelqu'un qu'on tutoie"],
         ["Mettez un foulard, s'il vous plaît.","un ordre poli"],
       ]},

      {t:'piege', h:"Trois pièges à connaître",
       rows:[
         ["dire « il faut je mets »","après il faut, le verbe reste entier",
          "On dit <b>il faut mettre</b>, <b>il faut rester</b>, <b>il faut sortir</b>. Le verbe ne se conjugue pas après « il faut »."],
         ["écrire « je met »","il manque le s",
          "<b>Je mets</b> et <b>tu mets</b> prennent un s. <b>Il met</b> n'en prend pas. À l'oreille, c'est pareil ; à l'écrit, non."],
         ["croire que l'impératif est impoli","il est court, pas sec",
          "« Mettez votre tuque » est une phrase normale et gentille au Québec, surtout suivie de « s'il vous plaît » ou d'un sourire."],
       ]},

      {t:'check', h:"Est-ce que c'est clair maintenant ?",
       p:"Quatre questions rapides.",
       qs:[
         {q:"« Il faut ___ une tuque. »", opts:["mettre","je mets"], ok:0,
          fb:"Après « il faut », le verbe reste entier."},
         {q:"« ___ mes bottes tous les matins. »", opts:["Je mets","Je met"], ok:0,
          fb:"Je mets, avec un s."},
         {q:"Pour dire à ton fils de mettre ses mitaines…", opts:["Mets tes mitaines !","Tu mets tes mitaines !"], ok:0,
          fb:"À l'impératif, le « tu » disparaît."},
         {q:"À une personne qu'on vouvoie, on dit…", opts:["Mettez votre tuque.","Mets votre tuque."], ok:0,
          fb:"Vous → mettez. Tu → mets."},
       ]},
    ]
  },

  t2quest: {
    eye:'Mini-leçon', tit:"Poser une question sur le temps",
    blocs:[
      {t:'texte', h:"Quatre questions, et la journée est claire",
       p:"On n'a pas besoin de comprendre tout le bulletin si on sait poser quatre questions : <b>quel temps fait-il ?</b>, <b>est-ce qu'il neige ?</b>, <b>il fait combien de degrés ?</b> et <b>pouvez-vous répéter ?</b> Elles marchent avec un voisin, un collègue, la personne à côté de soi dans l'autobus.",
       note:"Insister sur la quatrième : demander de répéter est une stratégie du programme, pas un aveu d'échec."},

      {t:'ana', h:"La question complète : quel temps fait-il ?",
       p:"C'est la question la plus large, et elle ouvre la conversation.",
       mots:[["On dit","{Quel temps fait-il} aujourd'hui ?"],["Aussi","{Quel temps fait-il} demain ?"],["Réponse possible","Il neige. · Il fait beau."],["Plus court","{Il fait quel temps} ?"],["On ne dit pas","« quelle temps » : temps est masculin",true]],
       say:"Quel temps fait-il aujourd'hui ? Quel temps fait-il demain ?",
       note:"Le « t » de « fait-il » se prononce : « fè-til ». Le faire répéter comme un seul mot."},

      {t:'ana', h:"La question fermée : est-ce qu'il neige ?",
       p:"On l'emploie quand on veut vérifier une seule chose.",
       mots:[["On dit","{Est-ce qu'}il neige ?"],["Aussi","{Est-ce qu'}il pleut ? · {Est-ce qu'}il vente ?"],["Réponse possible","Oui. · Non, il fait beau."],["Encore plus court","{Il neige} ? — la voix monte à la fin"],["On ne dit pas","« est-ce que il neige » : il faut l'apostrophe",true]],
       say:"Est-ce qu'il neige ? Est-ce qu'il pleut ? Il neige ?",
       note:"La version à une seule intonation montante est celle qu'on entend vraiment. La faire pratiquer autant que la forme complète."},

      {t:'ana', h:"La question du nombre : il fait combien de degrés ?",
       p:"C'est la question qui décide du manteau.",
       mots:[["On dit","{Il fait combien de degrés} ?"],["Plus court","{Il fait combien} ?"],["Réponse possible","Moins huit. · Moins huit degrés."],["Pour vérifier","{Moins huit} ? — on répète le nombre"],["On ne dit pas","« combien il fait de degré » sans s",true]],
       say:"Il fait combien de degrés ? Il fait combien ? Moins huit ?",
       note:"Répéter le nombre entendu est la stratégie la plus utile du module. La faire faire systématiquement."},

      {t:'labo', h:"Pose ta question",
       p:"Choisis ce que tu veux savoir et une façon de le demander.",
       axes:[
         {id:'p', lbl:'Tu veux savoir…', opts:[
           ['a','le temps'],
           ['b',"s'il neige"],
           ['c','la température'],
           ['d','le temps de demain']]},
         {id:'q', lbl:'Comment ?', opts:[['1','la question complète'],['2','la version courte'],['3','la réponse']]}],
       out:{
         a1:{w:["Quel temps fait-il aujourd'hui ?"], say:"Quel temps fait-il aujourd'hui ?", n:'la question la plus large'},
         a2:{w:["Il fait quel temps ?"], say:"Il fait quel temps ?", n:'la forme parlée, très courante'},
         a3:{w:["Il neige, et il vente."], say:"Il neige, et il vente.", n:'deux mots de temps dans la réponse'},
         b1:{w:["Est-ce qu'il neige ?"], say:"Est-ce qu'il neige ?", n:'on vérifie une seule chose'},
         b2:{w:["Il neige ?"], say:"Il neige ?", n:'la voix monte à la fin'},
         b3:{w:["Oui, depuis la nuit."], say:"Oui, depuis la nuit.", n:'la réponse de monsieur Pelchat'},
         c1:{w:["Il fait combien de degrés ?"], say:"Il fait combien de degrés ?", n:'la question qui décide du manteau'},
         c2:{w:["Il fait combien ?"], say:"Il fait combien ?", n:'trois mots suffisent'},
         c3:{w:["Moins douze. Et il vente."], say:"Moins douze. Et il vente.", n:'le signe, puis le nombre'},
         d1:{w:["Quel temps fait-il demain ?"], say:"Quel temps fait-il demain ?", n:'la même question, un autre jour'},
         d2:{w:["Et demain ?"], say:"Et demain ?", n:'deux mots, et la conversation continue'},
         d3:{w:["Demain, soleil. Moins deux."], say:"Demain, soleil. Moins deux.", n:'la forme du bulletin'},
       },
       note:"Douze extraits. Faire circuler dans la classe : chacun pose deux questions à trois personnes différentes."},

      {t:'ex', h:"À écouter et à répéter",
       p:"Six questions de tous les matins.",
       rows:[
         ["Quel temps fait-il aujourd'hui ?","la question complète"],
         ["Est-ce qu'il neige ?","une seule chose à vérifier"],
         ["Il fait combien de degrés ?","le nombre"],
         ["Et demain ?","deux mots"],
         ["Pouvez-vous répéter, s'il vous plaît ?","quand ça va trop vite"],
         ["Moins douze ? Merci !","répéter pour vérifier"],
       ]},

      {t:'piege', h:"Trois pièges à connaître",
       rows:[
         ["dire « quelle temps »","temps est masculin",
          "On dit <b>quel</b> temps. « Quelle » sert devant un mot féminin : quelle saison, quelle ville, quelle température."],
         ["dire « est-ce que il neige »","l'apostrophe est obligatoire",
          "Devant « il », « que » perd son e : <b>est-ce qu'il</b> neige. C'est aussi vrai pour est-ce qu'il pleut, est-ce qu'il vente."],
         ["ne pas oser demander de répéter","c'est une phrase du programme",
          "« Pouvez-vous répéter, s'il vous plaît ? » fait partie de ce qu'on apprend à dire au niveau 2. Personne ne la trouve étrange."],
       ]},

      {t:'check', h:"Est-ce que c'est clair maintenant ?",
       p:"Quatre questions rapides.",
       qs:[
         {q:"« ___ temps fait-il ? »", opts:["Quel","Quelle"], ok:0,
          fb:"Temps est un mot masculin."},
         {q:"« Est-ce ___ il neige ? »", opts:["qu'","que"], ok:0,
          fb:"Devant « il », que devient qu'."},
         {q:"Pour connaître la température, je demande…", opts:["Il fait combien de degrés ?","Quel temps fait-il ?"], ok:0,
          fb:"La deuxième question donne le temps, pas le nombre."},
         {q:"Quand la personne parle trop vite, je dis…", opts:["Pouvez-vous répéter, s'il vous plaît ?","rien"], ok:0,
          fb:"Demander de répéter fait partie de la conversation."},
       ]},
    ]
  },
};
