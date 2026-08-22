const PLUS = {
  prPhon: {
    eye:'Mini-leçon', tit:"Le « é » de métier et le « è » de salaire",
    blocs:[
      {t:'texte', h:"Deux e qui ne se disent pas pareil",
       p:"En français, la lettre <b>e</b> se prononce de plusieurs façons. Deux d'entre elles reviennent sans arrêt dans les mots du travail : le <b>é fermé</b> de « m<b>é</b>tier », et le <b>è ouvert</b> de « sal<b>ai</b>re ». Pour le premier, la bouche est presque fermée et les lèvres s'étirent ; pour le second, la mâchoire descend et la bouche s'ouvre.",
       note:"Ce n'est pas un détail : « j'ai travaillé » et « je travaillais » ne se distinguent qu'à ce son-là. Quand le patron demande depuis quand tu travailles, c'est ce qu'il écoute."},

      {t:'ana', h:"Le son « é » — la bouche presque fermée",
       p:"C'est le son de « métier », « embaucher », « congé », « employé ».",
       mots:[['On écrit','m{é}tier'],['Aussi écrit','er à la fin d\'un verbe : embauch{er}',true],['Aussi écrit','ez : vous engag{ez} · z final muet']],
       say:"Un métier, un employé, un congé.",
       note:"Les lèvres s'étirent, comme au début d'un sourire. La mâchoire ne bouge presque pas."},

      {t:'ana', h:"Le son « è » — la bouche ouverte",
       p:"C'est le son de « salaire », « horaire », « formulaire », « semaine ».",
       mots:[['On écrit','sal{ai}re'],['Aussi écrit','è : mon p{è}re · ils ach{è}tent',true],['Aussi écrit','ê, ei : la f{ê}te · s{ei}ze']],
       say:"Le salaire, l'horaire, le formulaire.",
       note:"La mâchoire descend d'un cran. Si tu peux glisser un doigt entre tes dents, tu es dans le bon son."},

      {t:'ana', h:"Le mot qui contient les deux",
       p:"« Un employé salarié » traverse les deux sons.",
       mots:[['On dit','em-plo-y{é} sa-la-ri{é}'],['Et à côté','le sal{ai}re, lui, s\'ouvre',true],['Retiens la paire','« un employ{é} » / « un sal{ai}re »']],
       say:"Un employé reçoit un salaire.",
       note:"Garde cette phrase comme repère : elle te redonne les deux sons chaque fois que tu la dis."},

      {t:'labo', h:"Écoute les paires",
       p:"Choisis une paire et écoute la différence.",
       axes:[{id:'p', lbl:'Quelle paire ?', opts:[
         ['a','métier / salaire'],
         ['b','embaucher / horaire'],
         ['c','employé / formulaire'],
         ['d','congé / semaine'],
         ['e','dans une phrase']]}],
       out:{
         a:{w:['m{é}tier / sal{ai}re'], say:"Un métier, un salaire.", n:'la bouche se ferme, puis s\'ouvre'},
         b:{w:['embauch{er} / hor{ai}re'], say:"Embaucher, un horaire.", n:'le er du verbe se dit « é »'},
         c:{w:['employ{é} / formul{ai}re'], say:"Un employé, un formulaire.", n:'les deux mots du défi 3'},
         d:{w:['cong{é} / sem{ai}ne'], say:"Un congé, une semaine.", n:'deux mots de l\'horaire'},
         e:{w:['« L\'employé regarde son horaire et son salaire. »'], say:"L'employé regarde son horaire et son salaire.", n:'les deux sons dans la même phrase'},
       },
       note:"Écoute chaque paire deux fois : la première pour comprendre, la seconde en fermant les yeux."},

      {t:'ex', h:"À écouter et à répéter",
       p:"Six phrases du module.",
       rows:[
         ["C'est un métier que j'aimerais apprendre.","é deux fois"],
         ["Le salaire est de seize dollars de l'heure.","è trois fois"],
         ["La boulangerie va embaucher quelqu'un.","é à la fin du verbe"],
         ["Mon horaire va de neuf heures à une heure.","è au début"],
         ["Vous engagez encore ? J'ai vu votre affiche.","é, puis é"],
         ["Je remplis le formulaire cette semaine.","è deux fois"],
       ]},

      {t:'piege', h:"Trois pièges à connaître",
       rows:[
         ["dire « er » comme en anglais","le verbe « embaucher »",
          "À la fin d'un verbe, les lettres <b>er</b> se disent « é » et rien d'autre : embauch<b>é</b>, travaill<b>é</b>, cherch<b>é</b>. Le r ne s'entend jamais."],
         ["ouvrir le é de « employé »","dire « employè »",
          "Un accent aigu ferme toujours le son. Si la bouche s'ouvre, l'oreille entend un autre mot — et ce mot n'existe pas."],
         ["fermer le è de « salaire »","dire « salére »",
          "Les lettres <b>ai</b> ouvrent le son. Même chose pour « horaire », « formulaire », « aide » : ce sont les mots les plus fréquents de l'annonce."],
       ]},

      {t:'check', h:"Est-ce que c'est clair maintenant ?",
       p:"Quatre questions rapides.",
       qs:[
         {q:"« Métier » a le son…", opts:["é fermé","è ouvert"], ok:0,
          fb:"L'accent aigu ferme le son : les lèvres s'étirent."},
         {q:"« Salaire » a le son…", opts:["é fermé","è ouvert"], ok:1,
          fb:"Les lettres ai ouvrent le son : la mâchoire descend."},
         {q:"À la fin de « embaucher », on entend…", opts:["é","er comme en anglais"], ok:0,
          fb:"Le r final d'un verbe en -er ne se prononce jamais."},
         {q:"« Horaire » se dit avec…", opts:["la bouche ouverte","la bouche fermée"], ok:0,
          fb:"Comme « salaire » et « formulaire » : le son s'ouvre."},
       ]},

      {t:'revoir', h:"À retenir",
       p:"Deux mots repères, et rien d'autre : <b>métier</b> pour le é fermé, <b>salaire</b> pour le è ouvert. Devant un mot nouveau, dis-le à côté de l'un des deux et écoute lequel se ressemble."},
    ]
  },

  prQuatre: {
    eye:'Mini-leçon', tit:"Les quatre choses qu'on dit en poussant la porte",
    blocs:[
      {t:'texte', h:"Une porte, trente secondes",
       p:"Quand on entre dans un commerce pour offrir ses services, la personne à qui on parle est en train de travailler. Elle n'a pas trois minutes. Tout tient donc dans quatre renseignements, toujours les mêmes, toujours dans le même ordre : <b>pourquoi je viens</b>, <b>ce que je sais faire</b>, <b>quand je suis libre</b>, <b>où on me joint</b>.",
       note:"Ce n'est pas une entrevue. Personne ne va te demander tes qualités ni tes défauts. On veut savoir si tu peux venir travailler, et quand."},

      {t:'ana', h:"1. Saluer et dire pourquoi on vient",
       p:"Une seule phrase, et elle nomme l'affiche.",
       mots:[['La phrase','Bonjour. {J\'ai vu votre affiche} dans la vitrine.'],['S\'il n\'y a pas d\'affiche','Bonjour. Est-ce que vous cherchez quelqu\'un ?',true],['Ce qu\'on ajoute','Excusez-moi de vous déranger.']],
       say:"Bonjour, j'ai vu votre affiche dans la vitrine.",
       note:"Nommer l'affiche est le meilleur début : la personne comprend en trois mots pourquoi tu es là, et elle sait déjà de quel poste tu parles."},

      {t:'ana', h:"2. Dire ce qu'on sait faire",
       p:"Un verbe, un domaine. Rien de plus au premier contact.",
       mots:[['Ce que je sais faire','{Je sais faire} le ménage.'],['Ce que j\'ai déjà fait','J\'ai de l\'expérience {en} garde d\'enfants.',true],['Ce que je ne sais pas encore','Je peux apprendre vite.']],
       say:"Je sais faire le ménage. J'ai de l'expérience en garde d'enfants.",
       note:"Deux phrases suffisent. Une liste de dix choses fait perdre le fil ; deux choses précises restent en tête."},

      {t:'ana', h:"3. Dire quand on est libre",
       p:"Des jours et des heures, jamais « n'importe quand ».",
       mots:[['Les jours','{Du} lundi {au} vendredi.'],['Les heures','{De} huit heures {à} une heure.',true],['Le moment','Le matin. · Le soir. · La fin de semaine.']],
       say:"Je suis libre du lundi au vendredi, le matin.",
       note:"« Je suis disponible n'importe quand » sonne bien, mais ne sert à rien : le patron doit écrire un horaire, et il a besoin de cases."},

      {t:'ana', h:"4. Laisser où on peut nous joindre",
       p:"Le nom, épelé s'il le faut, et le numéro — écrit.",
       mots:[['Le nom','Fanta Traor{é}. T-R-A-O-R-É.'],['Le numéro','{Vous pouvez me joindre au} 438 555-0192.',true],['Le geste qui compte','Je peux vous l\'écrire ?']],
       say:"Vous pouvez me joindre au 438 555-0192. Je peux vous l'écrire ?",
       note:"Un numéro dit à l'oral se perd. Demande toujours à l'écrire toi-même : c'est le geste qui fait la différence entre un rappel et un oubli."},

      {t:'labo', h:"Compose ton entrée",
       p:"Choisis le lieu et ce que tu sais faire.",
       axes:[
         {id:'l', lbl:'Tu entres où ?', opts:[['a','à la boulangerie'],['b','au centre communautaire'],['c','à l\'épicerie']]},
         {id:'s', lbl:'Tu sais faire quoi ?', opts:[['1','le ménage'],['2','la cuisine']]}],
       out:{
         a1:{w:["Bonjour. J'ai vu votre affiche dans la vitrine. Je sais faire le ménage et je suis libre le matin."], say:"Bonjour. J'ai vu votre affiche dans la vitrine. Je sais faire le ménage et je suis libre le matin.", n:'l\'affiche, puis ce que je sais faire'},
         a2:{w:["Bonjour. J'ai vu votre affiche. J'ai de l'expérience en cuisine et je suis libre le matin."], say:"Bonjour. J'ai vu votre affiche. J'ai de l'expérience en cuisine et je suis libre le matin.", n:'« de l\'expérience en » quand on a déjà fait le travail'},
         b1:{w:["Bonjour. Est-ce que vous cherchez quelqu'un pour l'entretien ? Je sais faire le ménage."], say:"Bonjour. Est-ce que vous cherchez quelqu'un pour l'entretien ? Je sais faire le ménage.", n:'sans affiche, on pose la question directement'},
         b2:{w:["Bonjour. Est-ce que vous engagez à la cuisine ? J'ai six ans d'expérience."], say:"Bonjour. Est-ce que vous engagez à la cuisine ? J'ai six ans d'expérience.", n:'le nombre d\'années arrive tout de suite'},
         c1:{w:["Bonjour. J'ai vu l'annonce sur le babillard. Je fais le ménage depuis longtemps."], say:"Bonjour. J'ai vu l'annonce sur le babillard. Je fais le ménage depuis longtemps.", n:'au babillard, on nomme l\'annonce'},
         c2:{w:["Bonjour. J'ai vu l'annonce sur le babillard. Je sais cuisiner et je suis libre le jour."], say:"Bonjour. J'ai vu l'annonce sur le babillard. Je sais cuisiner et je suis libre le jour.", n:'les disponibilités closent la phrase'},
       },
       note:"Six entrées différentes, toutes courtes, toutes utilisables telles quelles demain matin."},

      {t:'ex', h:"À écouter et à répéter",
       p:"Six phrases d'entrée.",
       rows:[
         ["Bonjour, excusez-moi de vous déranger.","le début poli"],
         ["J'ai vu votre affiche dans la vitrine.","pourquoi je viens"],
         ["Est-ce que vous engagez encore ?","la question qui compte"],
         ["Je sais faire le ménage et la vaisselle.","ce que je sais faire"],
         ["Je suis libre du lundi au vendredi, le matin.","quand je suis libre"],
         ["Vous pouvez me joindre au 438 555-0192.","où on me joint"],
       ]},

      {t:'piege', h:"Trois pièges à connaître",
       rows:[
         ["arriver à l'heure du dîner","entrer à midi et demi",
          "Entre onze heures et deux heures, tous les commerces de nourriture sont débordés. Va-y avant dix heures ou après deux heures : la même phrase sera écoutée au lieu d'être expédiée."],
         ["dire « n'importe quand »","« Je suis disponible n'importe quand. »",
          "Le patron fait un horaire avec des cases. « N'importe quand » ne remplit aucune case. Donne des jours et des heures, même si tu es libre partout."],
         ["repartir sans laisser son numéro","« Je repasserai demain. »",
          "Si tu ne laisses rien, il ne reste rien de ton passage. Laisse ton nom et ton numéro par écrit, même si on te dit que le poste est comblé."],
       ]},

      {t:'check', h:"Est-ce que c'est clair maintenant ?",
       p:"Quatre questions rapides.",
       qs:[
         {q:"Combien de renseignements il faut donner en entrant ?", opts:["Quatre","Dix"], ok:0,
          fb:"Pourquoi je viens, ce que je sais faire, quand je suis libre, où on me joint."},
         {q:"Quand vaut-il mieux ne pas entrer ?", opts:["Tôt le matin","À l'heure du dîner"], ok:1,
          fb:"Entre onze heures et deux heures, personne n'a le temps de t'écouter."},
         {q:"« Je suis libre n'importe quand » est…", opts:["une bonne réponse","une réponse inutile"], ok:1,
          fb:"Le patron a besoin de jours et d'heures pour faire son horaire."},
         {q:"Le numéro de téléphone, il faut…", opts:["le dire seulement","l'écrire soi-même"], ok:1,
          fb:"Un numéro dit à l'oral se perd. Demande à l'écrire."},
       ]},

      {t:'revoir', h:"À retenir",
       p:"Quatre phrases, dans cet ordre : <b>« J'ai vu votre affiche. »</b> — <b>« Je sais faire… »</b> — <b>« Je suis libre… »</b> — <b>« Vous pouvez me joindre au… »</b>. Apprends-les par cœur : elles marchent dans tous les commerces du quartier."},
    ]
  },

  t1quest: {
    eye:'Mini-leçon', tit:"Est-ce que vous engagez ? — poser la question",
    blocs:[
      {t:'texte', h:"Une question, trois formes",
       p:"En français, une question se pose de trois façons. La plus simple monte la voix à la fin : « Vous engagez ? » La deuxième ajoute <b>est-ce que</b> devant : « Est-ce que vous engagez ? » La troisième retourne le verbe et le sujet : « Engagez-vous ? » Au comptoir d'un commerce, c'est la <b>deuxième</b> qu'on emploie : polie sans être guindée, et comprise partout.",
       note:"Les trois sont correctes. Mais la première peut sonner sèche avec un inconnu, et la troisième sonne comme un formulaire. « Est-ce que » est le juste milieu, et c'est celle du module."},

      {t:'ana', h:"« Est-ce que » se pose devant, sans rien changer d'autre",
       p:"La phrase qui suit reste dans l'ordre normal.",
       mots:[['La phrase','Vous engagez.'],['La question','{Est-ce que} vous engagez ?',true],['Jamais','Est-ce que engagez-vous ?']],
       say:"Est-ce que vous engagez ?",
       note:"On ne retourne pas le verbe après « est-ce que ». C'est l'erreur la plus fréquente, et elle s'entend tout de suite."},

      {t:'ana', h:"Demander autrement quand il n'y a pas d'affiche",
       p:"Trois questions qui ouvrent la même porte.",
       mots:[['Le plus large','Est-ce que vous {cherchez quelqu\'un} ?'],['Quand l\'affiche traîne','Est-ce que le poste est {encore libre} ?',true],['Pour du temps partiel','Est-ce que vous engagez pour le matin ?']],
       say:"Est-ce que vous cherchez quelqu'un pour le matin ?",
       note:"Une affiche peut rester collée une semaine après l'embauche. « Encore libre » évite le malaise des deux côtés."},

      {t:'ana', h:"Demander à qui parler",
       p:"Le patron n'est pas toujours là — et c'est la moitié des visites.",
       mots:[['La question','{À qui est-ce que je peux parler} ?'],['Plus court','Je parle à qui, s\'il vous plaît ?',true],['Ce qu\'on note','Le nom de la personne et l\'heure où elle est là.']],
       say:"À qui est-ce que je peux parler, s'il vous plaît ?",
       note:"Repartir avec un nom et une heure vaut mieux qu'une visite ratée : tu reviens le lendemain en demandant la personne par son nom."},

      {t:'labo', h:"Pose ta question",
       p:"Choisis la situation et le ton.",
       axes:[
         {id:'s', lbl:'La situation', opts:[['a','il y a une affiche'],['b','il n\'y a pas d\'affiche'],['c','le patron n\'est pas là']]},
         {id:'t', lbl:'Le ton', opts:[['1','direct'],['2','plus poli']]}],
       out:{
         a1:{w:["Est-ce que vous engagez encore ?"], say:"Est-ce que vous engagez encore ?", n:'court, correct, très fréquent'},
         a2:{w:["Bonjour. J'ai vu votre affiche. Est-ce que le poste est encore libre ?"], say:"Bonjour. J'ai vu votre affiche. Est-ce que le poste est encore libre ?", n:'on nomme l\'affiche avant de demander'},
         b1:{w:["Est-ce que vous cherchez quelqu'un ?"], say:"Est-ce que vous cherchez quelqu'un ?", n:'la question la plus large'},
         b2:{w:["Excusez-moi. Est-ce que vous cherchez quelqu'un pour le matin ?"], say:"Excusez-moi. Est-ce que vous cherchez quelqu'un pour le matin ?", n:'on précise tout de suite ses heures'},
         c1:{w:["Je parle à qui, s'il vous plaît ?"], say:"Je parle à qui, s'il vous plaît ?", n:'la forme parlée, courante au comptoir'},
         c2:{w:["À qui est-ce que je peux parler, et à quelle heure il est là ?"], say:"À qui est-ce que je peux parler, et à quelle heure il est là ?", n:'un nom et une heure : de quoi revenir'},
       },
       note:"Six questions, toutes utilisables telles quelles. Choisis-en deux et apprends-les par cœur."},

      {t:'ex', h:"À écouter et à répéter",
       p:"Six questions du défi.",
       rows:[
         ["Est-ce que vous engagez ?","la question du module"],
         ["Est-ce que vous engagez encore ?","quand l'affiche est là depuis un moment"],
         ["Est-ce que vous cherchez quelqu'un ?","sans affiche"],
         ["Est-ce que le poste est encore libre ?","poli, et prudent"],
         ["À qui est-ce que je peux parler ?","quand le patron n'est pas là"],
         ["Est-ce que je peux laisser mon numéro ?","avant de repartir"],
       ]},

      {t:'piege', h:"Trois pièges à connaître",
       rows:[
         ["retourner le verbe après « est-ce que »","« Est-ce que engagez-vous ? »",
          "Après « est-ce que », la phrase reste dans l'ordre normal : est-ce que <b>vous engagez</b>. Retourner le verbe fait une question double."],
         ["dire « j'ai besoin d'un travail »","au lieu de demander si ça engage",
          "C'est vrai, mais ce n'est pas une question : la personne ne sait pas quoi répondre. Demande si ça engage, et laisse tes besoins de côté."],
         ["dire « je veux du travail »","à la place d'« offrir ses services »",
          "« Je veux » sonne exigeant en français. On dit « je cherche du travail », ou mieux : « je viens offrir mes services »."],
       ]},

      {t:'check', h:"Est-ce que c'est clair maintenant ?",
       p:"Quatre questions rapides.",
       qs:[
         {q:"Après « est-ce que », le verbe et le sujet…", opts:["restent dans l'ordre normal","se retournent"], ok:0,
          fb:"Est-ce que vous engagez — jamais « est-ce que engagez-vous »."},
         {q:"L'affiche est là depuis dix jours. Tu demandes…", opts:["Vous engagez ?","Est-ce que le poste est encore libre ?"], ok:1,
          fb:"L'affiche peut traîner après l'embauche : « encore libre » évite le malaise."},
         {q:"Le patron est absent. Tu demandes…", opts:["à qui parler et à quelle heure","tu repars sans rien dire"], ok:0,
          fb:"Un nom et une heure valent une visite de plus."},
         {q:"« Je veux du travail » est…", opts:["correct et poli","trop exigeant"], ok:1,
          fb:"On dit « je cherche du travail » ou « je viens offrir mes services »."},
       ]},

      {t:'revoir', h:"À retenir",
       p:"Une phrase à savoir par cœur : <b>« Est-ce que vous engagez ? »</b> Et une deuxième pour le jour où le patron n'est pas là : <b>« À qui est-ce que je peux parler ? »</b>"},
    ]
  },

  t1sais: {
    eye:'Mini-leçon', tit:"Je sais faire, j'ai de l'expérience en…",
    blocs:[
      {t:'texte', h:"Deux façons de parler de ce qu'on peut faire",
       p:"Il y a ce qu'on <b>sait faire</b> — une capacité, aujourd'hui — et ce qu'on <b>a déjà fait</b> — une expérience, avant. Les deux se disent avec deux constructions différentes, et le patron écoute les deux : la première lui dit si tu peux commencer, la seconde lui dit si tu vas apprendre vite.",
       note:"Personne n'attend une liste de dix compétences. Deux choses nettes, dites avec assurance, valent mieux qu'une énumération dont on ne retient rien."},

      {t:'ana', h:"Savoir + un autre verbe",
       p:"Le deuxième verbe ne change jamais de forme.",
       mots:[['La construction','{Je sais} faire le ménage.'],['Autres exemples','Je sais servir. · Je sais cuisiner. · Je sais conduire.',true],['Jamais','Je sais je fais le ménage.']],
       say:"Je sais faire le ménage. Je sais servir les clients.",
       note:"Le verbe qui suit « je sais » reste à l'infinitif — la forme du dictionnaire. C'est vrai aussi après « je peux » et « je veux »."},

      {t:'ana', h:"Avoir de l'expérience en…",
       p:"Après « en », on nomme le domaine, pas le lieu.",
       mots:[['La construction','{J\'ai de l\'expérience en} cuisine.'],['Autres domaines','en ménage · en garde d\'enfants · en entretien',true],['Avec un nombre','J\'ai {six ans} d\'expérience en cuisine.']],
       say:"J'ai de l'expérience en garde d'enfants.",
       note:"On dit « en cuisine », pas « en restaurant » : le mot après « en » nomme le travail, pas le bâtiment."},

      {t:'ana', h:"Dire combien de temps",
       p:"Deux petits mots, et ils ne disent pas la même chose.",
       mots:[['Une durée finie','J\'ai gardé des enfants {pendant} six ans.'],['Une durée qui continue','Je fais le ménage {depuis} longtemps.',true],['La forme courte','Six ans d\'expérience.']],
       say:"J'ai gardé des enfants pendant six ans.",
       note:"<b>Pendant</b> pour ce qui est terminé, <b>depuis</b> pour ce qui continue aujourd'hui. Le patron entend la différence."},

      {t:'ana', h:"Quand on n'a pas encore travaillé ici",
       p:"On le dit — et on enchaîne aussitôt.",
       mots:[['La phrase','{Je n\'ai jamais travaillé} au Québec.'],['Ce qu\'on ajoute tout de suite','mais j\'apprends vite. · mais je sais faire le ménage.',true],['Jamais tout seul','Je ne sais pas.']],
       say:"Je n'ai jamais travaillé au Québec, mais j'apprends vite.",
       note:"« Je ne sais pas » tout seul ferme la porte. Il y a toujours un « mais » à dire après : ce que tu sais, ou ce que tu peux apprendre."},

      {t:'labo', h:"Compose ta phrase",
       p:"Choisis le domaine et la façon de le dire.",
       axes:[
         {id:'d', lbl:'Ton domaine', opts:[['a','le ménage'],['b','la cuisine'],['c','la garde d\'enfants'],['d','rien encore']]},
         {id:'f', lbl:'Comment le dire', opts:[['1','ce que je sais faire'],['2','ce que j\'ai déjà fait']]}],
       out:{
         a1:{w:["Je sais faire le ménage et la vaisselle."], say:"Je sais faire le ménage et la vaisselle.", n:'savoir + infinitif'},
         a2:{w:["J'ai de l'expérience en ménage, depuis longtemps."], say:"J'ai de l'expérience en ménage, depuis longtemps.", n:'« depuis » : ça continue'},
         b1:{w:["Je sais cuisiner pour beaucoup de personnes."], say:"Je sais cuisiner pour beaucoup de personnes.", n:'une capacité d\'aujourd\'hui'},
         b2:{w:["J'ai travaillé en cuisine pendant quatre ans."], say:"J'ai travaillé en cuisine pendant quatre ans.", n:'« pendant » : c\'est terminé'},
         c1:{w:["Je sais m'occuper des enfants."], say:"Je sais m'occuper des enfants.", n:'savoir + infinitif, forme réfléchie'},
         c2:{w:["J'ai six ans d'expérience en garde d'enfants."], say:"J'ai six ans d'expérience en garde d'enfants.", n:'le nombre d\'années d\'abord'},
         d1:{w:["Je n'ai jamais fait ce travail, mais je peux apprendre vite."], say:"Je n'ai jamais fait ce travail, mais je peux apprendre vite.", n:'jamais « je ne sais pas » tout seul'},
         d2:{w:["Je n'ai jamais travaillé au Québec, mais j'ai travaillé chez moi."], say:"Je n'ai jamais travaillé au Québec, mais j'ai travaillé chez moi.", n:'l\'expérience d\'ailleurs compte aussi'},
       },
       note:"Huit phrases. Choisis celle qui te ressemble, et dis-la à voix haute cinq fois."},

      {t:'ex', h:"À écouter et à répéter",
       p:"Six phrases du défi.",
       rows:[
         ["Je sais faire le ménage.","savoir + infinitif"],
         ["Je sais servir les clients au comptoir.","une capacité"],
         ["J'ai de l'expérience en garde d'enfants.","en + le domaine"],
         ["J'ai gardé des enfants pendant six ans.","une durée finie"],
         ["Je fais le ménage depuis longtemps.","une durée qui continue"],
         ["Je n'ai jamais travaillé ici, mais j'apprends vite.","le « mais » qui rouvre la porte"],
       ]},

      {t:'piege', h:"Trois pièges à connaître",
       rows:[
         ["conjuguer le deuxième verbe","« Je sais je fais le ménage. »",
          "Après « je sais », le verbe reste à l'infinitif : je sais <b>faire</b>, je sais <b>servir</b>, je sais <b>cuisiner</b>."],
         ["confondre pendant et depuis","« Je fais le ménage pendant longtemps. »",
          "<b>Pendant</b> ferme la durée : c'est fini. <b>Depuis</b> l'ouvre : ça continue aujourd'hui. Devant le patron, ce n'est pas la même chose."],
         ["s'arrêter à « je ne sais pas »","« Vous savez servir ? — Non. »",
          "Ajoute toujours la suite : « Non, mais je peux apprendre vite. » C'est cette moitié de phrase qui décide de la suite."],
       ]},

      {t:'check', h:"Est-ce que c'est clair maintenant ?",
       p:"Quatre questions rapides.",
       qs:[
         {q:"Après « je sais », le verbe est…", opts:["à l'infinitif","conjugué"], ok:0,
          fb:"Je sais faire, je sais servir, je sais cuisiner."},
         {q:"« J'ai travaillé en cuisine ___ quatre ans » — c'est terminé.", opts:["pendant","depuis"], ok:0,
          fb:"« Pendant » ferme la durée ; « depuis » veut dire que ça continue."},
         {q:"Après « de l'expérience en », on nomme…", opts:["le lieu","le domaine"], ok:1,
          fb:"En cuisine, en ménage, en garde d'enfants — le travail, pas le bâtiment."},
         {q:"Tu n'as jamais fait ce travail. Tu réponds…", opts:["« Non. »","« Non, mais je peux apprendre vite. »"], ok:1,
          fb:"Le « mais » rouvre la porte que le « non » vient de fermer."},
       ]},

      {t:'revoir', h:"À retenir",
       p:"Deux phrases à emporter : <b>« Je sais faire… »</b> pour aujourd'hui, <b>« J'ai de l'expérience en… »</b> pour avant. Et jamais de « non » tout seul : il y a toujours un « mais » à dire après."},
    ]
  },

  t1dispo: {
    eye:'Mini-leçon', tit:"Du lundi au vendredi, de 9 h à 13 h",
    blocs:[
      {t:'texte', h:"Les petits mots qui font un horaire",
       p:"Dire ses disponibilités, c'est donner deux choses : des <b>jours</b> et des <b>heures</b>. Le français les encadre avec des paires de petits mots qui ne se séparent jamais : <b>du… au…</b> pour les jours, <b>de… à…</b> pour les heures. Une fois la paire connue, tout horaire se dit en une phrase.",
       note:"Le patron n'écoute pas ta phrase : il remplit un tableau. Chaque mot que tu dis doit pouvoir aller dans une case."},

      {t:'ana', h:"Du… au… pour les jours",
       p:"Les deux mots vont ensemble, toujours.",
       mots:[['La paire','{Du} lundi {au} vendredi.'],['Autres exemples','Du mardi au samedi. · Du jeudi au dimanche.',true],['Jamais','De lundi à vendredi.']],
       say:"Je travaille du lundi au vendredi.",
       note:"Les jours de la semaine ne prennent pas de majuscule en français : on écrit « lundi », pas « Lundi »."},

      {t:'ana', h:"De… à… pour les heures",
       p:"La même mécanique, avec deux autres mots.",
       mots:[['La paire','{De} neuf heures {à} une heure.'],['À l\'écrit','de 9 h à 13 h',true],['Le midi et minuit','de midi à cinq heures']],
       say:"Je suis libre de neuf heures à une heure.",
       note:"À l'écrit, on met un espace avant le h et rien après : <b>9 h</b>, <b>13 h 30</b>. Et l'heure officielle va jusqu'à 24 : 13 h, c'est une heure de l'après-midi."},

      {t:'ana', h:"Le moment de la journée",
       p:"Un petit mot devant, et le moment revient chaque jour.",
       mots:[['Ce qui revient','{Le} matin. · {Le} soir. · {L\'}après-midi.'],['La fin de semaine','{La} fin de semaine — samedi et dimanche.',true],['Une seule fois','Ce matin. · Demain soir.']],
       say:"Je suis libre le matin, et la fin de semaine.",
       note:"Au Québec, on dit <b>la fin de semaine</b> pour samedi et dimanche. « Week-end » se comprend, mais ce n'est pas le mot d'ici."},

      {t:'ana', h:"Enlever un jour de la liste",
       p:"Un seul mot, et le jour sort de l'horaire.",
       mots:[['Le mot','Du mardi au samedi, {sauf} le mercredi.'],['Autre façon','Tous les jours {excepté} le dimanche.',true],['À l\'inverse','Seulement le samedi et le dimanche.']],
       say:"Je travaille du mardi au samedi, sauf le mercredi.",
       note:"« Sauf » est le mot le plus utile de l'horaire : il évite de réciter cinq jours pour en exclure un."},

      {t:'labo', h:"Dis tes disponibilités",
       p:"Choisis tes jours et tes heures.",
       axes:[
         {id:'j', lbl:'Quels jours ?', opts:[['a','du lundi au vendredi'],['b','du mardi au samedi'],['c','la fin de semaine']]},
         {id:'h', lbl:'Quelles heures ?', opts:[['1','le matin'],['2','l\'après-midi'],['3','le soir']]}],
       out:{
         a1:{w:["Je suis libre du lundi au vendredi, le matin, de 8 h à 13 h."], say:"Je suis libre du lundi au vendredi, le matin, de huit heures à treize heures.", n:'jours, moment, heures : les trois'},
         a2:{w:["Je suis libre du lundi au vendredi, l'après-midi, de 13 h à 17 h."], say:"Je suis libre du lundi au vendredi, l'après-midi, de treize heures à dix-sept heures.", n:'l\'après-midi prend l\'apostrophe'},
         a3:{w:["Je suis libre du lundi au vendredi, le soir, après 17 h."], say:"Je suis libre du lundi au vendredi, le soir, après dix-sept heures.", n:'« après » remplace la paire quand la fin est ouverte'},
         b1:{w:["Je suis libre du mardi au samedi, le matin, de 9 h à 13 h."], say:"Je suis libre du mardi au samedi, le matin, de neuf heures à treize heures.", n:'l\'horaire du centre Léo-Bourdon'},
         b2:{w:["Je suis libre du mardi au samedi, l'après-midi."], say:"Je suis libre du mardi au samedi, l'après-midi.", n:'sans heures précises, mais avec un moment'},
         b3:{w:["Je suis libre du mardi au samedi, le soir, sauf le jeudi."], say:"Je suis libre du mardi au samedi, le soir, sauf le jeudi.", n:'« sauf » enlève un jour de la liste'},
         c1:{w:["Je suis libre la fin de semaine, le matin."], say:"Je suis libre la fin de semaine, le matin.", n:'samedi et dimanche'},
         c2:{w:["Je suis libre la fin de semaine, l'après-midi, de 13 h à 18 h."], say:"Je suis libre la fin de semaine, l'après-midi, de treize heures à dix-huit heures.", n:'très demandé dans les commerces'},
         c3:{w:["Je suis libre la fin de semaine, le soir, jusqu'à 22 h."], say:"Je suis libre la fin de semaine, le soir, jusqu'à vingt-deux heures.", n:'« jusqu\'à » ferme la tranche par la fin'},
       },
       note:"Neuf horaires. Trouve le tien, écris-le sur un papier, et garde-le dans ta poche."},

      {t:'ex', h:"À écouter et à répéter",
       p:"Six façons de dire quand on est libre.",
       rows:[
         ["Je suis libre du lundi au vendredi.","la paire du… au…"],
         ["Je peux travailler de neuf heures à une heure.","la paire de… à…"],
         ["Je suis libre le matin seulement.","un moment qui revient"],
         ["Je travaille du mardi au samedi, sauf le jeudi.","enlever un jour"],
         ["Je suis à l'école l'après-midi.","dire aussi ce qui n'est pas libre"],
         ["La fin de semaine, je garde mes enfants.","le mot du Québec"],
       ]},

      {t:'piege', h:"Trois pièges à connaître",
       rows:[
         ["séparer la paire","« De lundi à vendredi. »",
          "Pour les jours, c'est <b>du… au…</b> ; pour les heures, <b>de… à…</b>. Mélanger les deux paires est l'erreur la plus fréquente du défi."],
         ["oublier de dire ce qui n'est pas libre","« Je suis libre. »",
          "Dis aussi ce qui bloque : « Je suis à l'école l'après-midi. » Le patron préfère le savoir tout de suite qu'après avoir fait l'horaire."],
         ["dire « week-end »","au lieu de « la fin de semaine »",
          "Ça se comprend partout, mais ce n'est pas le mot du Québec. Dans un commerce de quartier, dis <b>la fin de semaine</b>."],
       ]},

      {t:'check', h:"Est-ce que c'est clair maintenant ?",
       p:"Quatre questions rapides.",
       qs:[
         {q:"Pour les jours, on dit…", opts:["du… au…","de… à…"], ok:0,
          fb:"Du lundi au vendredi. « De… à… » est réservé aux heures."},
         {q:"13 h, c'est…", opts:["une heure de l'après-midi","une heure du matin"], ok:0,
          fb:"L'heure officielle va jusqu'à 24 : 13 h = une heure de l'après-midi."},
         {q:"Pour enlever un jour, on dit…", opts:["sauf","sans"], ok:0,
          fb:"Du mardi au samedi, sauf le mercredi."},
         {q:"Samedi et dimanche, au Québec, c'est…", opts:["le week-end","la fin de semaine"], ok:1,
          fb:"« Fin de semaine » est le mot d'ici. L'autre se comprend, mais s'entend moins."},
       ]},

      {t:'revoir', h:"À retenir",
       p:"Deux paires, et tout tient : <b>du… au…</b> pour les jours, <b>de… à…</b> pour les heures. Plus un mot de secours : <b>sauf</b>."},
    ]
  },

  t2chiffres: {
    eye:'Mini-leçon', tit:"De l'heure, par semaine, aux deux semaines",
    blocs:[
      {t:'texte', h:"Trois petits mots qui changent tout le calcul",
       p:"Une offre d'emploi tient en chiffres, et chaque chiffre est accompagné d'un petit mot qui dit ce qu'il compte. <b>De l'heure</b> compte l'argent d'une heure. <b>Par semaine</b> compte le total d'une semaine. <b>Aux deux semaines</b> dit quand la paie arrive. Lire l'annonce, c'est lire ces mots-là autant que les nombres.",
       note:"Une erreur de lecture ici coûte un matin : on se présente pour un poste de 40 heures qui en fait 20, ou on croit gagner 330 $ par jour."},

      {t:'ana', h:"De l'heure — l'argent d'une seule heure",
       p:"C'est le salaire tel qu'il s'affiche partout au Québec.",
       mots:[['On lit','16,50 $ {de l\'heure}'],['On dit','seize dollars cinquante de l\'heure',true],['Le calcul','16,50 $ × 20 heures = 330 $']],
       say:"Le salaire est de seize dollars cinquante de l'heure.",
       note:"En français du Québec, la virgule sépare les cents : 16,50 $. Le signe de dollar se met après le nombre, avec une espace."},

      {t:'ana', h:"Par semaine — le total d'une semaine",
       p:"Le mot « par » découpe le temps.",
       mots:[['On lit','20 heures {par} semaine'],['Autres découpes','par jour · par mois · par année',true],['Ce que ça dit','20 h par semaine = temps partiel']],
       say:"C'est un poste de vingt heures par semaine.",
       note:"Moins de trente heures par semaine, c'est du <b>temps partiel</b> ; à partir de trente-cinq environ, c'est du <b>temps plein</b>."},

      {t:'ana', h:"Aux deux semaines — quand la paie arrive",
       p:"Le rythme de la paie, et non celui du travail.",
       mots:[['On lit','payé {aux deux semaines}'],['Autres rythmes','payé chaque semaine · payé deux fois par mois',true],['Le premier chèque','souvent trois semaines après le début']],
       say:"Le salaire est payé aux deux semaines.",
       note:"Au Québec, la paie aux deux semaines est la plus courante. Le premier chèque arrive rarement le premier vendredi : prévois-le."},

      {t:'ana', h:"Sur — comparer deux nombres",
       p:"Le mot qui dit combien sur combien.",
       mots:[['On lit','ouvert six jours {sur} sept'],['Autres exemples','deux fins de semaine sur trois',true],['Ce que ça dit','il reste un jour de fermeture']],
       say:"La boulangerie est ouverte six jours sur sept.",
       note:"« Sur » compare toujours au tout : six sur sept, c'est presque tous les jours ; deux sur trois, c'est la majorité."},

      {t:'labo', h:"Fais le calcul",
       p:"Choisis le salaire et le nombre d'heures.",
       axes:[
         {id:'s', lbl:'Le salaire', opts:[['a','16,00 $ de l\'heure'],['b','16,50 $ de l\'heure'],['c','20,00 $ de l\'heure']]},
         {id:'h', lbl:'Les heures', opts:[['1','20 h par semaine'],['2','35 h par semaine']]}],
       out:{
         a1:{w:["16,00 $ × 20 h = 320 $ par semaine · 640 $ aux deux semaines"], say:"Seize dollars de l'heure, vingt heures par semaine : trois cent vingt dollars.", n:'temps partiel'},
         a2:{w:["16,00 $ × 35 h = 560 $ par semaine · 1 120 $ aux deux semaines"], say:"Seize dollars de l'heure, trente-cinq heures par semaine : cinq cent soixante dollars.", n:'temps plein'},
         b1:{w:["16,50 $ × 20 h = 330 $ par semaine · 660 $ aux deux semaines"], say:"Seize dollars cinquante de l'heure, vingt heures par semaine : trois cent trente dollars.", n:'l\'offre du babillard'},
         b2:{w:["16,50 $ × 35 h = 577,50 $ par semaine · 1 155 $ aux deux semaines"], say:"Seize dollars cinquante de l'heure, trente-cinq heures par semaine : cinq cent soixante-dix-sept dollars cinquante.", n:'la même offre, à temps plein'},
         c1:{w:["20,00 $ × 20 h = 400 $ par semaine · 800 $ aux deux semaines"], say:"Vingt dollars de l'heure, vingt heures par semaine : quatre cents dollars.", n:'le prix que Fanta demande dans son annonce'},
         c2:{w:["20,00 $ × 35 h = 700 $ par semaine · 1 400 $ aux deux semaines"], say:"Vingt dollars de l'heure, trente-cinq heures par semaine : sept cents dollars.", n:'temps plein'},
       },
       note:"Les montants sont bruts : les retenues sont prises avant que le chèque arrive. Le net est toujours plus bas."},

      {t:'ex', h:"À écouter et à répéter",
       p:"Six phrases de l'annonce.",
       rows:[
         ["Le salaire est de 16,50 $ de l'heure.","l'argent d'une heure"],
         ["C'est un poste de vingt heures par semaine.","le total de la semaine"],
         ["Le salaire est payé aux deux semaines.","le rythme de la paie"],
         ["Vingt heures par semaine, c'est du temps partiel.","moins de trente heures"],
         ["On travaille de neuf heures à une heure.","la tranche du jour"],
         ["Le commerce est ouvert six jours sur sept.","comparer deux nombres"],
       ]},

      {t:'piege', h:"Trois pièges à connaître",
       rows:[
         ["lire le salaire comme un total","« 16,50 $ » pour la journée",
          "C'est le prix d'<b>une heure</b>. Multiplie par le nombre d'heures pour savoir ce que fait la semaine."],
         ["croire que 20 h, c'est un temps plein","« 20 heures par semaine »",
          "Vingt heures, c'est du <b>temps partiel</b> : environ quatre heures par jour, cinq jours. Un temps plein tourne autour de trente-cinq."],
         ["attendre la paie le premier vendredi","« payé aux deux semaines »",
          "Le premier chèque arrive souvent deux ou trois semaines après le premier jour. Prévois-le avant de compter dessus."],
       ]},

      {t:'check', h:"Est-ce que c'est clair maintenant ?",
       p:"Quatre questions rapides.",
       qs:[
         {q:"16,50 $ de l'heure, 20 h par semaine, ça fait…", opts:["330 $ par semaine","16,50 $ par semaine"], ok:0,
          fb:"16,50 × 20 = 330. « De l'heure » compte une seule heure."},
         {q:"Vingt heures par semaine, c'est…", opts:["du temps plein","du temps partiel"], ok:1,
          fb:"Moins de trente heures : temps partiel."},
         {q:"« Payé aux deux semaines » veut dire…", opts:["une paie tous les quinze jours","deux paies par semaine"], ok:0,
          fb:"C'est le rythme le plus courant au Québec."},
         {q:"« Ouvert six jours sur sept » veut dire…", opts:["fermé un jour","ouvert six semaines"], ok:0,
          fb:"« Sur » compare au tout : six jours d'ouverture, un de fermeture."},
       ]},

      {t:'revoir', h:"À retenir",
       p:"Trois mots à repérer dans toute annonce : <b>de l'heure</b> (l'argent d'une heure), <b>par semaine</b> (le total), <b>aux deux semaines</b> (quand la paie arrive). Le reste, c'est du calcul."},
    ]
  },

  t2faut: {
    eye:'Mini-leçon', tit:"Exigé, aucune expérience, un atout",
    blocs:[
      {t:'texte', h:"Ce que l'annonce demande vraiment",
       p:"Le bas d'une offre d'emploi dit ce qu'il faut pour se présenter. Trois mots y décident de tout : ce qui est <b>exigé</b> (obligatoire), ce qui n'est demandé <b>aucunement</b> (« aucune expérience exigée ») et ce qui est un <b>atout</b> (utile, mais pas obligatoire). Beaucoup de gens renoncent à un poste qu'ils pouvaient avoir, faute d'avoir lu ces trois mots.",
       note:"S'il est écrit « atout », vas-y quand même. C'est écrit exprès pour dire que l'absence de cette chose ne bloque pas."},

      {t:'ana', h:"Ce qui est obligatoire",
       p:"Deux façons de le dire, et elles pèsent pareil.",
       mots:[['La forme courante','{Il faut} parler français.'],['La forme de l\'annonce','Français parlé {exigé}.',true],['Autre forme','Le permis de conduire est {obligatoire}.']],
       say:"Il faut parler français pour ce poste.",
       note:"« Exigé » s'accorde avec ce qu'il suit : expérience exigé<b>e</b>, diplôme exigé, deux ans exigé<b>s</b>."},

      {t:'ana', h:"Ce qui n'est pas obligatoire",
       p:"La ligne la plus importante pour qui commence.",
       mots:[['La formule','{Aucune expérience exigée.}'],['Autres formes','Débutants acceptés. · Ouvert aux débutants.',true],['Ce qui l\'accompagne souvent','Formation donnée sur place.']],
       say:"Aucune expérience exigée : je peux me présenter.",
       note:"« Aucune expérience exigée » et « formation donnée sur place » vont souvent ensemble : c'est un poste où l'on t'apprendra le travail."},

      {t:'ana', h:"Ce qui aide sans être obligatoire",
       p:"Le mot le plus mal lu de toute l'annonce.",
       mots:[['La formule','Anglais {un atout}.'],['Autres formes','Expérience {un atout}. · Permis de conduire, {un atout}.',true],['Ce que ça veut dire','ce n\'est pas obligatoire : présente-toi.']],
       say:"Parler anglais est un atout, mais ce n'est pas exigé.",
       note:"Un atout te donne une longueur d'avance ; il ne t'interdit rien. Beaucoup de postes sont donnés à quelqu'un qui n'avait pas l'atout."},

      {t:'ana', h:"Ce qu'on te demande d'apporter ou de faire",
       p:"La dernière ligne dit toujours comment s'y prendre.",
       mots:[['Le plus simple','{Se présenter en personne}, entre 9 h et 11 h.'],['Avec un papier','{Apporter} son curriculum vitæ.',true],['Par téléphone','Demander Hugo Pelletier au 514 555-0148.']],
       say:"Il faut se présenter en personne, entre neuf et onze heures.",
       note:"Respecte l'heure indiquée : c'est le moment où la personne qui embauche est disponible. Arriver à un autre moment, c'est arriver pour rien."},

      {t:'labo', h:"Est-ce que je peux me présenter ?",
       p:"Choisis ce que dit l'annonce et ce que tu as.",
       axes:[
         {id:'a', lbl:'L\'annonce dit', opts:[['a','aucune expérience exigée'],['b','expérience exigée'],['c','anglais un atout']]},
         {id:'t', lbl:'Toi, tu as', opts:[['1','aucune expérience'],['2','de l\'expérience']]}],
       out:{
         a1:{w:["Oui. « Aucune expérience exigée » : présente-toi sans hésiter."], say:"Aucune expérience exigée : présente-toi sans hésiter.", n:'la formation sera donnée sur place'},
         a2:{w:["Oui, et dis-le : « J'ai de l'expérience en cuisine. » C'est un avantage."], say:"J'ai de l'expérience en cuisine.", n:'l\'expérience aide même quand elle n\'est pas exigée'},
         b1:{w:["Présente-toi quand même, en disant ce que tu sais faire d'autre."], say:"Je n'ai pas travaillé en cuisine, mais je sais faire le ménage et j'apprends vite.", n:'« exigé » ferme la porte, mais elle se rouvre parfois'},
         b2:{w:["Oui. Dis tout de suite combien d'années : « J'ai six ans d'expérience. »"], say:"J'ai six ans d'expérience en garde d'enfants.", n:'le nombre d\'années répond directement à l\'exigence'},
         c1:{w:["Oui. Un atout n'est pas une exigence : le français suffit."], say:"Je parle français et soussou. L'anglais, je l'apprends.", n:'ne renonce jamais devant le mot « atout »'},
         c2:{w:["Oui, et si tu parles anglais, dis-le : c'est ta longueur d'avance."], say:"Je parle français, et un peu d'anglais aussi.", n:'l\'atout se mentionne, sans insister'},
       },
       note:"Dans cinq cas sur six, la réponse est : présente-toi. C'est la leçon de cette mini-leçon."},

      {t:'ex', h:"À écouter et à répéter",
       p:"Six lignes du bas des annonces.",
       rows:[
         ["Il faut parler français.","ce qui est obligatoire"],
         ["Deux ans d'expérience exigée.","la forme sèche de l'annonce"],
         ["Aucune expérience exigée.","la ligne qui ouvre la porte"],
         ["Formation donnée sur place.","ils vont t'apprendre"],
         ["Anglais un atout.","utile, pas obligatoire"],
         ["Se présenter en personne, entre 9 h et 11 h.","comment s'y prendre"],
       ]},

      {t:'piege', h:"Trois pièges à connaître",
       rows:[
         ["renoncer devant « un atout »","« Anglais un atout » et je n'y vais pas",
          "Un atout n'est jamais une exigence. Cette ligne est écrite pour dire que l'absence de cette chose ne bloque pas la candidature."],
         ["ne pas lire la dernière ligne","celle qui dit comment se présenter",
          "Elle donne l'heure, l'adresse et le nom de la personne à demander. Se présenter au mauvais moment, c'est perdre le déplacement."],
         ["croire que « exigé » ne se discute pas","« Expérience exigée »",
          "Souvent, oui. Mais si tu sais faire un travail proche, présente-toi en le disant : « Je n'ai pas travaillé en cuisine, mais je sais faire le ménage. »"],
       ]},

      {t:'check', h:"Est-ce que c'est clair maintenant ?",
       p:"Quatre questions rapides.",
       qs:[
         {q:"« Anglais un atout » veut dire…", opts:["il faut parler anglais","c'est utile, pas obligatoire"], ok:1,
          fb:"Un atout donne une longueur d'avance, il n'interdit rien."},
         {q:"« Aucune expérience exigée » veut dire…", opts:["je peux me présenter","il faut de l'expérience"], ok:0,
          fb:"C'est la ligne qui ouvre la porte aux débutants."},
         {q:"« Formation donnée sur place » veut dire…", opts:["il faut suivre un cours avant","ils vont t'apprendre le travail"], ok:1,
          fb:"Elle accompagne presque toujours « aucune expérience exigée »."},
         {q:"La dernière ligne de l'annonce donne…", opts:["le salaire","comment et quand se présenter"], ok:1,
          fb:"L'heure, l'adresse, et le nom de la personne à demander."},
       ]},

      {t:'revoir', h:"À retenir",
       p:"Trois mots, trois portes : <b>exigé</b> = obligatoire ; <b>aucune… exigée</b> = va-y ; <b>un atout</b> = va-y aussi. Et lis toujours la dernière ligne."},
    ]
  },

  t3imper: {
    eye:'Mini-leçon', tit:"Écrivez, cochez, signez, datez",
    blocs:[
      {t:'texte', h:"La forme des consignes",
       p:"Sur un formulaire, les verbes ne sont pas conjugués comme dans une phrase ordinaire : ils sont à l'<b>impératif</b>, la forme qui donne une consigne. « Écrivez », « cochez », « signez ». Il n'y a pas de « vous » devant, et ce n'est pas impoli : c'est la langue des papiers officiels, et elle est la même pour tout le monde.",
       note:"Reconnaître ces six verbes, c'est pouvoir remplir n'importe quel formulaire du Québec — d'emploi, de clinique, d'école, de bibliothèque."},

      {t:'ana', h:"Écrivez, remplissez — mettre des mots",
       p:"Les deux verbes les plus fréquents du formulaire.",
       mots:[['La consigne','{Écrivez} votre nom en lettres moulées.'],['Le tout d\'un coup','{Remplissez} le formulaire au complet.',true],['Ce qu\'on ajoute souvent','en lettres moulées · en majuscules · lisiblement']],
       say:"Écrivez votre nom en lettres moulées.",
       note:"Les <b>lettres moulées</b> sont les majuscules bien détachées, une par case. C'est demandé partout : la machine et l'œil les lisent sans se tromper."},

      {t:'ana', h:"Cochez — faire un crochet",
       p:"Un petit carré, un crochet, et la réponse est donnée.",
       mots:[['La consigne','{Cochez} la bonne case.'],['Ce qu\'on lit à côté','oui / non · homme / femme · temps plein / temps partiel',true],['La règle d\'or','Ne laissez jamais une case vide.']],
       say:"Cochez la bonne case : oui ou non.",
       note:"Une case vide n'est pas un « non » : c'est une réponse manquante, et celui qui lit le formulaire ne sait pas quoi en faire."},

      {t:'ana', h:"Signez, datez — au bas de la page",
       p:"Les deux derniers gestes, et ils vont toujours ensemble.",
       mots:[['La consigne','{Signez} et {datez} au bas de la page.'],['La date au Québec','2026-08-22, ou 22 août 2026',true],['Ce que dit la signature','ce que j\'ai écrit est vrai.']],
       say:"Signez ici, puis datez le formulaire.",
       note:"Une signature, c'est ton nom écrit à la main, toujours de la même façon. Elle n'a pas besoin d'être lisible : elle doit être <b>la tienne</b>."},

      {t:'ana', h:"Joignez — ajouter un papier",
       p:"Le verbe qui demande un document en plus.",
       mots:[['La consigne','{Joignez} une copie de votre carte.'],['Autres formes','Veuillez joindre… · Prière de joindre…',true],['Ce qu\'on demande souvent','une pièce d\'identité · un numéro d\'assurance sociale']],
       say:"Joignez une copie de votre carte d'assurance maladie.",
       note:"On joint une <b>copie</b>, jamais l'original. Un original remis ne revient pas toujours, et il est difficile à remplacer."},

      {t:'labo', h:"Que faut-il faire ?",
       p:"Choisis la case et vois la consigne.",
       axes:[{id:'c', lbl:'Quelle case ?', opts:[
         ['a','Nom de famille'],
         ['b','Avez-vous un permis de conduire ?'],
         ['c','Disponibilités'],
         ['d','Signature'],
         ['e','Documents']]}],
       out:{
         a:{w:["Écrivez TRAORÉ en lettres moulées, une lettre par case."], say:"Écrivez votre nom de famille en lettres moulées.", n:'le nom de famille, sans le prénom'},
         b:{w:["Cochez « oui » ou « non ». Ne laissez pas le carré vide."], say:"Cochez oui ou non. Ne laissez pas le carré vide.", n:'une case vide n\'est pas une réponse'},
         c:{w:["Écrivez les jours et les heures : du mardi au samedi, de 9 h à 13 h."], say:"Du mardi au samedi, de neuf heures à treize heures.", n:'précis, comme au comptoir'},
         d:{w:["Signez à la main, puis datez : 2026-08-22."], say:"Signez à la main, puis datez le formulaire.", n:'les deux gestes vont ensemble'},
         e:{w:["Joignez une copie de votre carte — jamais l'original."], say:"Joignez une copie de votre carte, jamais l'original.", n:'l\'original reste chez toi'},
       },
       note:"Cinq cases, cinq gestes. C'est tout ce que demande un formulaire de demande d'emploi."},

      {t:'ex', h:"À écouter et à répéter",
       p:"Six consignes de formulaire.",
       rows:[
         ["Écrivez en lettres moulées.","la consigne la plus fréquente"],
         ["Remplissez toutes les cases.","ne rien laisser vide"],
         ["Cochez la bonne case.","oui ou non"],
         ["Signez au bas de la page.","ton nom à la main"],
         ["Datez le formulaire.","le jour, le mois, l'année"],
         ["Joignez une copie de votre carte.","une copie, pas l'original"],
       ]},

      {t:'piege', h:"Trois pièges à connaître",
       rows:[
         ["laisser une case vide","la case « permis de conduire »",
          "Une case vide ne veut pas dire « non » : elle veut dire que la question n'a pas été lue. Coche « non », ou écris « aucun »."],
         ["écrire en lettres attachées","quand il est demandé des lettres moulées",
          "Les lettres moulées sont des majuscules détachées, une par case. C'est demandé pour que personne ne se trompe en lisant ton nom."],
         ["remettre un original","« Joignez une copie »",
          "Ta carte d'assurance maladie, ton permis, ton passeport ne se remettent jamais. Fais une photocopie et garde l'original sur toi."],
       ]},

      {t:'check', h:"Est-ce que c'est clair maintenant ?",
       p:"Quatre questions rapides.",
       qs:[
         {q:"« Lettres moulées » veut dire…", opts:["majuscules détachées","lettres attachées"], ok:0,
          fb:"Une lettre par case, bien séparée, comme sur une carte d'assurance maladie."},
         {q:"La réponse est non. Tu…", opts:["laisses la case vide","coches « non »"], ok:1,
          fb:"Une case vide est une réponse manquante, pas un non."},
         {q:"« Joignez une copie » veut dire…", opts:["remettez l'original","ajoutez une photocopie"], ok:1,
          fb:"L'original reste toujours chez toi."},
         {q:"Signer, ça veut dire…", opts:["écrire son nom à la main","écrire son nom en lettres moulées"], ok:0,
          fb:"La signature est ton nom écrit à la main, toujours de la même façon."},
       ]},

      {t:'revoir', h:"À retenir",
       p:"Six verbes, et tous les formulaires du Québec s'ouvrent : <b>écrivez</b>, <b>remplissez</b>, <b>cochez</b>, <b>signez</b>, <b>datez</b>, <b>joignez</b>. Plus une règle : aucune case vide."},
    ]
  },

  t3annparts: {
    eye:'Mini-leçon', tit:"Écrire sa petite annonce en six lignes",
    blocs:[
      {t:'texte', h:"Un carton, six lignes, un numéro en gros",
       p:"Une petite annonce se lit debout, en dix secondes, par quelqu'un qui passait pour acheter du lait. Elle n'a donc pas de phrases longues et pas de politesses : un <b>titre</b> lisible de loin, quatre lignes de renseignements, et un <b>numéro</b> en gros tout en bas. Six lignes, jamais plus.",
       note:"C'est de la production écrite, et c'est ce que le module te demande à la fin. Écris-la une fois pour de vrai : elle servira au babillard de ton quartier."},

      {t:'ana', h:"1. Le titre — ce qui arrête le passant",
       p:"Deux ou trois mots, en majuscules, en haut.",
       mots:[['Le titre','{MÉNAGE ET GARDE D\'ENFANTS}'],['Autres titres','ENTRETIEN MÉNAGER · AIDE À LA CUISINE · DÉNEIGEMENT',true],['Jamais','Bonjour à tous, je me présente…']],
       say:"Ménage et garde d'enfants.",
       note:"Le titre nomme le <b>service</b>, pas la personne. Celui qui cherche quelqu'un pour son ménage cherche le mot « ménage », pas ton prénom."},

      {t:'ana', h:"2 et 3. Qui je suis, ce que je sais faire",
       p:"Le prénom suffit, le quartier rassure, l'expérience convainc.",
       mots:[['Qui je suis','{Je m\'appelle} Fanta et {j\'habite dans} Saint-Michel.'],['Ce que je sais faire','{J\'ai six ans d\'expérience} en garde d\'enfants.',true],['On peut ajouter','Je parle français et soussou.']],
       say:"Je m'appelle Fanta et j'habite dans Saint-Michel.",
       note:"Ne donne jamais ton adresse complète sur un babillard public. Le quartier suffit : il dit que tu es proche, sans dire où tu habites."},

      {t:'ana', h:"4. Quand je suis libre",
       p:"Les mêmes paires qu'au comptoir : du… au…, de… à…",
       mots:[['La ligne','{Du lundi au vendredi}, {de 8 h à 13 h}.'],['Plus court','Le matin, en semaine.',true],['Jamais','Disponible n\'importe quand.']],
       say:"Du lundi au vendredi, de huit heures à treize heures.",
       note:"Celui qui lit ton annonce a un besoin à une heure précise. S'il ne voit pas son heure, il ne t'appelle pas."},

      {t:'ana', h:"5 et 6. Le prix, et le numéro en gros",
       p:"Les deux dernières lignes, et les plus lues.",
       mots:[['Le prix','{Je demande 20 $ de l\'heure.}'],['Le numéro','{Appelez-moi au} 438 555-0192.',true],['Le mot de la fin','Merci !']],
       say:"Je demande vingt dollars de l'heure. Appelez-moi au 438 555-0192.",
       note:"Écris le numéro plus gros que le reste, et vérifie-le deux fois. Un chiffre de travers, et l'annonce ne sert à rien."},

      {t:'labo', h:"Compose ton annonce",
       p:"Choisis ton service et ton moment.",
       axes:[
         {id:'s', lbl:'Ton service', opts:[['a','ménage'],['b','garde d\'enfants'],['c','déneigement']]},
         {id:'m', lbl:'Ton moment', opts:[['1','le matin, en semaine'],['2','la fin de semaine']]}],
       out:{
         a1:{w:["ENTRETIEN MÉNAGER — Je m'appelle… J'habite dans le quartier. Libre du lundi au vendredi, le matin. 22 $ de l'heure. Appelez-moi au …"], say:"Entretien ménager. Libre du lundi au vendredi, le matin. Vingt-deux dollars de l'heure.", n:'titre, disponibilités, prix, numéro'},
         a2:{w:["ENTRETIEN MÉNAGER — Libre la fin de semaine, samedi et dimanche. 22 $ de l'heure. Appelez-moi au …"], say:"Entretien ménager. Libre la fin de semaine, samedi et dimanche.", n:'très demandé pour les logements'},
         b1:{w:["GARDE D'ENFANTS — Six ans d'expérience. Libre du lundi au vendredi, de 8 h à 13 h. 20 $ de l'heure."], say:"Garde d'enfants. Six ans d'expérience. Libre du lundi au vendredi, de huit heures à treize heures.", n:'l\'expérience passe avant le prix'},
         b2:{w:["GARDE D'ENFANTS — Six ans d'expérience. Libre la fin de semaine, soirs compris. 20 $ de l'heure."], say:"Garde d'enfants. Six ans d'expérience. Libre la fin de semaine, soirs compris.", n:'les soirs de fin de semaine sont recherchés'},
         c1:{w:["DÉNEIGEMENT — Escaliers et entrées, le matin avant 8 h. 25 $ par entrée."], say:"Déneigement. Escaliers et entrées, le matin avant huit heures. Vingt-cinq dollars par entrée.", n:'ici, on facture par entrée, pas de l\'heure'},
         c2:{w:["DÉNEIGEMENT — Escaliers et entrées, la fin de semaine. 25 $ par entrée. Appelez-moi au …"], say:"Déneigement. Escaliers et entrées, la fin de semaine. Vingt-cinq dollars par entrée.", n:'même annonce, autre moment'},
       },
       note:"Six annonces. Prends celle qui te ressemble, remplace le prénom et le numéro, et va la punaiser."},

      {t:'ex', h:"À écouter et à répéter",
       p:"Les six lignes, dans l'ordre.",
       rows:[
         ["Ménage et garde d'enfants.","le titre, en gros"],
         ["Je m'appelle Fanta et j'habite dans Saint-Michel.","qui je suis"],
         ["J'ai six ans d'expérience en garde d'enfants.","ce que je sais faire"],
         ["Je suis libre du lundi au vendredi, de 8 h à 13 h.","quand je suis libre"],
         ["Je demande 20 $ de l'heure.","mon prix"],
         ["Appelez-moi au 438 555-0192. Merci !","mon numéro, en gros"],
       ]},

      {t:'piege', h:"Trois pièges à connaître",
       rows:[
         ["écrire son adresse complète","« J'habite au 3410, rue Jarry, app. 5 »",
          "Un babillard est public : tout le monde lit. Donne le <b>quartier</b>, jamais le numéro de porte."],
         ["commencer par une longue politesse","« Bonjour à tous, je me permets de… »",
          "Personne ne lit la deuxième ligne d'une annonce qui commence ainsi. Le titre en premier, toujours."],
         ["oublier le prix","une annonce sans montant",
          "Sans prix, on t'appelle pour demander le prix — ou on ne t'appelle pas. Écris un montant, quitte à ajouter « à discuter »."],
       ]},

      {t:'check', h:"Est-ce que c'est clair maintenant ?",
       p:"Quatre questions rapides.",
       qs:[
         {q:"La première ligne de l'annonce, c'est…", opts:["le titre du service","ton nom complet"], ok:0,
          fb:"Le passant cherche le service, pas la personne."},
         {q:"Sur un babillard public, tu écris…", opts:["ton adresse complète","ton quartier"], ok:1,
          fb:"Le quartier dit que tu es proche, sans dire où tu habites."},
         {q:"Le numéro de téléphone se met…", opts:["au milieu","en bas, en gros"], ok:1,
          fb:"C'est la ligne la plus lue : elle doit se voir de loin."},
         {q:"Une annonce sans prix…", opts:["attire plus d'appels","fait hésiter"], ok:1,
          fb:"Écris un montant, quitte à ajouter « à discuter »."},
       ]},

      {t:'revoir', h:"À retenir",
       p:"Six lignes, dans cet ordre : <b>le titre</b>, <b>qui je suis</b>, <b>ce que je sais faire</b>, <b>quand je suis libre</b>, <b>mon prix</b>, <b>mon numéro</b>. Rien d'autre, et le numéro en gros."},
    ]
  },
};
