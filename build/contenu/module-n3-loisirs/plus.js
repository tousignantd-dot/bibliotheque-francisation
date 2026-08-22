const PLUS = {
  prPhon: {
    eye:'Mini-leçon', tit:'Le « ch » de chaudron et le « j » de gymnase',
    blocs:[
      {t:'texte', h:"Deux sons voisins, une seule différence",
       p:"Le français a deux sons qui se font exactement au même endroit de la bouche : le <b>ch</b> de « <b>ch</b>audron » et le <b>j</b> de « <b>g</b>ymnase ». La langue est au même endroit, les lèvres sont un peu avancées dans les deux cas. Une seule chose change : pour <b>ch</b>, la gorge ne vibre pas ; pour <b>j</b>, elle vibre.",
       note:"Pose deux doigts sur ta gorge et dis « chhh », puis « jjj ». Au deuxième, tu sens quelque chose bouger sous tes doigts. C'est toute la différence."},

      {t:'ana', h:"Le son « ch » — la gorge est tranquille",
       p:"C'est le son de « chaudron », « chercher », « séance ».",
       mots:[['On écrit','{ch}audron'],['La gorge','ne vibre pas',true],['Les lèvres','un peu avancées, comme pour siffler doucement']],
       say:"Le chaudron, chercher, une séance.",
       note:"Attention : dans « séance », le son s'écrit <b>c</b> devant <b>e</b>… mais il se dit « s ». Le vrai « ch » de ce mot-là est ailleurs — écoute bien : « sé-an-ce ». On l'a mis ici pour l'oreille, pas pour l'écriture."},

      {t:'ana', h:"Le son « j » — la gorge vibre",
       p:"C'est le son de « gymnase », « jeudi », « je voudrais ».",
       mots:[['On écrit','{gy}mnase'],['On écrit aussi','{j}eudi',true],['La gorge','vibre : on le sent avec les doigts']],
       say:"Le gymnase, jeudi, je voudrais.",
       note:"Le même son s'écrit de deux façons : <b>j</b> (jeudi, jouer) et <b>g</b> devant e, i, y (gymnase, gens, gigot). Devant a, o, u, le <b>g</b> se dit « gu » : gâteau, gomme."},

      {t:'ana', h:"Les paires qui changent le sens",
       p:"Trois paires courantes, à écouter deux fois chacune.",
       mots:[['chou / joue','le {ch}ou du souper · la {j}oue de Camila'],['cher / cher (j)','c\'est {ch}er · le {g}este',true],['chaud / Joe','il fait {ch}aud · bonjour {J}oe']],
       say:"Le chou, la joue. C'est cher, le geste. Il fait chaud.",
       note:"Si tu confonds les deux, on te comprend quand même la plupart du temps — le contexte aide. Mais l'oreille des autres travaille plus fort, et c'est fatigant pour tout le monde."},

      {t:'labo', h:"Écoute les paires",
       p:"Choisis une paire et écoute la différence.",
       axes:[{id:'p', lbl:'Quelle paire ?', opts:[
         ['a','chaudron / gymnase'],
         ['b','chercher / jeudi'],
         ['c','chou / joue'],
         ['d','la cuisine / je voudrais'],
         ['e','dans une phrase']]}],
       out:{
         a:{w:['{ch}audron / {gy}mnase'], say:"Chaudron. Gymnase.", n:'les deux mots repères du module'},
         b:{w:['{ch}ercher / {j}eudi'], say:"Chercher. Jeudi.", n:'la gorge se met à vibrer au deuxième'},
         c:{w:['{ch}ou / {j}oue'], say:"Le chou. La joue.", n:'deux mots très différents'},
         d:{w:['la cui{s}ine / {j}e voudrais'], say:"La cuisine. Je voudrais.", n:'le s de cuisine se dit « z », pas « j »'},
         e:{w:['« Jeudi, je cherche un chaudron dans la cuisine du gymnase. »'], say:"Jeudi, je cherche un chaudron dans la cuisine du gymnase.", n:'les deux sons quatre fois'},
       },
       note:"Écoute chaque paire deux fois : la première pour comprendre, la seconde en fermant les yeux."},

      {t:'ex', h:"À écouter et à répéter",
       p:"Six phrases du centre de quartier.",
       rows:[
         ["Le chaudron est dans la cuisine collective.","ch deux fois"],
         ["Jeudi, il y a de la danse au gymnase.","j deux fois"],
         ["Je cherche le babillard de l'entrée.","j puis ch"],
         ["Chaque séance coûte trois dollars.","ch au début"],
         ["J'aimerais changer de journée.","j, ch, j"],
         ["Le congé du dimanche change tout.","j puis ch"],
       ]},

      {t:'piege', h:"Trois pièges à connaître",
       rows:[
         ["dire « ch » à la place de « j »","« chymnase » au lieu de « gymnase »",
          "C'est le piège le plus fréquent. Mets tes doigts sur ta gorge : si elle ne vibre pas, tu dis « ch »."],
         ["lire le g comme « gu » devant e ou i","« guymnase », « gueste »",
          "Devant <b>e</b>, <b>i</b> et <b>y</b>, le g se dit « j ». Devant <b>a</b>, <b>o</b>, <b>u</b>, il se dit « gu »."],
         ["ajouter un « t » devant le ch","« tchaudron » au lieu de « chaudron »",
          "Beaucoup de langues n'ont que le son « tch ». En français, le « ch » commence tout de suite, sans petit coup de langue avant."],
       ]},

      {t:'check', h:"Est-ce que c'est clair maintenant ?",
       p:"Quatre questions rapides.",
       qs:[
         {q:"Dans « gymnase », la gorge…", opts:["vibre","ne vibre pas"], ok:0,
          fb:"C'est le son « j ». Deux doigts sur la gorge le confirment."},
         {q:"« Chaudron » commence par le son…", opts:["ch","j"], ok:0,
          fb:"La gorge reste tranquille."},
         {q:"Devant e, i et y, la lettre g se dit…", opts:["« gu »","« j »"], ok:1,
          fb:"gymnase, gens, gigot : tous avec le son « j »."},
         {q:"Ce qui change entre les deux sons, c'est…", opts:["la place de la langue","la vibration de la gorge"], ok:1,
          fb:"La langue et les lèvres ne bougent presque pas."},
       ]},

      {t:'revoir', h:"À retenir",
       p:"Deux mots repères, et rien d'autre : <b>chaudron</b> pour le son « ch », <b>gymnase</b> pour le son « j ». Devant un mot nouveau, pose deux doigts sur ta gorge : si elle vibre, c'est « j »."},
    ]
  },

  prSemaine: {
    eye:'Mini-leçon', tit:'Mardi, ou le mardi ?',
    blocs:[
      {t:'texte', h:"Un tout petit mot qui change tout",
       p:"« Mardi, je vais au badminton » et « Le mardi, je vais au badminton » ne veulent pas dire la même chose. Le premier parle d'<b>une fois</b>, mardi prochain. Le second parle de <b>toutes les semaines</b>, pendant toute la session. Un seul mot de deux lettres fait la différence, et c'est celui qu'on oublie.",
       note:"C'est le point qui rend un horaire lisible. Un feuillet de loisirs est écrit presque entièrement avec la forme « le mardi » : il décrit des habitudes, pas des dates."},

      {t:'ana', h:"Sans « le » — une seule fois",
       p:"On parle d'un jour précis, et il est proche.",
       mots:[['On dit','{Mardi}, j\'essaie le badminton.'],['Aussi','{Samedi}, on va au ciné-club.',true],['Sens','le mardi qui vient, une fois']],
       say:"Mardi, j'essaie le badminton. Samedi, on va au ciné-club.",
       note:"On peut ajouter « prochain » pour être tout à fait clair : « mardi prochain », « samedi prochain »."},

      {t:'ana', h:"Avec « le » — toutes les semaines",
       p:"On décrit une habitude ou un horaire.",
       mots:[['On dit','{Le mardi}, il y a du badminton.'],['Aussi','C\'est {le jeudi soir}, de sept heures à huit heures et demie.',true],['Sens','tous les mardis, toute la session']],
       say:"Le mardi, il y a du badminton. C'est le jeudi soir.",
       note:"C'est la forme de la préposée au téléphone, et celle du feuillet. Quand tu répètes pour vérifier, garde le <b>le</b> : « Alors c'est le mardi soir. »"},

      {t:'ana', h:"Le moment de la journée se colle après",
       p:"Trois moments, toujours dans le même ordre.",
       mots:[['Le matin','{le samedi matin}, de dix heures à onze heures'],['L\'après-midi','{le mercredi après-midi}, la cuisine collective',true],['Le soir','{le vendredi soir}, le ciné-club']],
       say:"Le samedi matin. Le mercredi après-midi. Le vendredi soir.",
       note:"On ne met rien entre les deux mots : ni « au », ni « du ». « Au jeudi soir » n'existe pas."},

      {t:'labo', h:"Une fois, ou toutes les semaines ?",
       p:"Choisis un jour et le sens que tu veux donner.",
       axes:[
         {id:'j', lbl:'Quel jour ?', opts:[['a','mardi'],['b','jeudi'],['c','samedi']]},
         {id:'s', lbl:'Quel sens ?', opts:[['1','une seule fois'],['2','toutes les semaines']]}],
       out:{
         a1:{w:['{Mardi}, je vais au badminton.'], say:"Mardi, je vais au badminton.", n:'mardi prochain, une fois'},
         a2:{w:['{Le mardi}, je vais au badminton.'], say:"Le mardi, je vais au badminton.", n:'tous les mardis de la session'},
         b1:{w:['{Jeudi}, j\'essaie la danse en ligne.'], say:"Jeudi, j'essaie la danse en ligne.", n:"un essai, une fois"},
         b2:{w:['{Le jeudi}, il y a de la danse en ligne.'], say:"Le jeudi, il y a de la danse en ligne.", n:"c'est l'horaire du feuillet"},
         c1:{w:['{Samedi}, on va voir un film.'], say:"Samedi, on va voir un film.", n:'un projet pour cette semaine'},
         c2:{w:['{Le samedi}, le centre ouvre à neuf heures.'], say:"Le samedi, le centre ouvre à neuf heures.", n:"une règle, tous les samedis"},
       },
       note:"Six phrases, deux sens. Lis-les à voix haute en te demandant chaque fois : une fois, ou toutes les semaines ?"},

      {t:'ex', h:"À écouter et à répéter",
       p:"Six phrases de l'horaire.",
       rows:[
         ["Le mardi soir, de sept heures à neuf heures.","une habitude"],
         ["Mardi, j'y vais pour la première fois.","une seule fois"],
         ["Le samedi matin, c'est l'heure des familles.","une habitude"],
         ["Le centre est fermé le dimanche.","toute l'année"],
         ["Vendredi, il y a un documentaire sur les rivières.","une date précise"],
         ["Le mercredi après-midi, la cuisine collective se réunit.","toutes les semaines"],
       ]},

      {t:'piege', h:"Trois pièges à connaître",
       rows:[
         ["mettre une majuscule aux jours","« Mardi » au milieu d'une phrase",
          "En français, les jours de la semaine et les mois s'écrivent en petites lettres, sauf au début d'une phrase."],
         ["dire « au jeudi soir »","« Le cours est au jeudi soir »",
          "On ne met rien devant : « le jeudi soir », tout simplement."],
         ["mettre un s à « le mardi »","« les mardis » quand on décrit l'horaire",
          "« Le mardi » au singulier veut déjà dire tous les mardis. « Les mardis » n'est pas faux, mais personne ne le dit au comptoir."],
       ]},

      {t:'check', h:"Est-ce que c'est clair maintenant ?",
       p:"Quatre questions rapides.",
       qs:[
         {q:"« Le vendredi, il y a un film » veut dire…", opts:["une fois","toutes les semaines"], ok:1,
          fb:"Le petit mot « le » transforme la date en habitude."},
         {q:"« Samedi, on y va » veut dire…", opts:["samedi prochain","tous les samedis"], ok:0,
          fb:"Sans « le », c'est une seule fois."},
         {q:"On écrit les jours…", opts:["avec une majuscule","avec une petite lettre"], ok:1,
          fb:"lundi, mardi, mercredi : jamais de majuscule au milieu d'une phrase."},
         {q:"La bonne forme est…", opts:["au jeudi soir","le jeudi soir"], ok:1,
          fb:"Rien devant « le »."},
       ]},

      {t:'revoir', h:"À retenir",
       p:"<b>Mardi</b> = une fois. <b>Le mardi</b> = toutes les semaines. Un horaire de loisirs est écrit avec la deuxième forme, du début à la fin."},
    ]
  },

  t1quest: {
    eye:'Mini-leçon', tit:'Poser une question : trois façons, la même réponse',
    blocs:[
      {t:'texte', h:"Personne n'attend une phrase parfaite",
       p:"Beaucoup de gens n'osent pas téléphoner parce qu'ils cherchent la « bonne » façon de poser leur question. Il n'y en a pas une : il y en a trois, et les trois marchent. La plus courte est même la plus fréquente au téléphone. Ce qui compte, ce n'est pas la forme — c'est de poser les <b>quatre questions</b> qui permettent de choisir une activité.",
       note:"Quand, combien, où, quoi apporter. Avec ces quatre-là, aucune activité de quartier ne reste mystérieuse."},

      {t:'ana', h:"Façon 1 — le mot de question tout seul",
       p:"On dit « c'est » et on met le mot de question à la fin.",
       mots:[['Le jour','{C\'est quand} ?'],['Le prix','{C\'est combien} ?',true],['Le lieu','{C\'est où} ?']],
       say:"C'est quand ? C'est combien ? C'est où ?",
       note:"Trois mots. C'est court, c'est clair, et personne ne trouve ça impoli au bout du fil. Ajoute « s'il vous plaît » si tu veux adoucir."},

      {t:'ana', h:"Façon 2 — avec « est-ce que »",
       p:"On pose « est-ce que » devant une phrase normale, sans rien changer d'autre.",
       mots:[['Phrase normale','Il faut apporter quelque chose.'],['Question','{Est-ce qu\'}il faut apporter quelque chose ?',true],['Avec un mot de question','{Quand est-ce que} ça commence ?']],
       say:"Est-ce qu'il faut apporter quelque chose ? Quand est-ce que ça commence ?",
       note:"C'est la façon la plus sûre : l'ordre des mots ne bouge pas. Devant une voyelle, « est-ce que » perd son e : <b>est-ce qu'</b>il."},

      {t:'ana', h:"Façon 3 — le sujet passe après le verbe",
       p:"On la lit dans les feuillets et on l'entend dans les services.",
       mots:[['On dit','{À quelle heure commence} le cours ?'],['Aussi','{Combien coûte} la session ?',true],['Sens','exactement la même question qu\'avant']],
       say:"À quelle heure commence le cours ? Combien coûte la session ?",
       note:"À reconnaître d'abord ; à employer quand tu te sentiras prêt. Rien ne t'oblige à l'utiliser pour être compris."},

      {t:'ana', h:"Ce que tu entendras au Québec : la particule -tu",
       p:"Une petite syllabe collée au verbe, qui transforme la phrase en question.",
       mots:[['On entend','Ça commence-{tu} cette semaine ?'],['Aussi','C\'est-{tu} loin d\'ici ?',true],['Attention','ce « tu » ne veut pas dire « toi »']],
       say:"Ça commence-tu cette semaine ? C'est-tu loin d'ici ?",
       note:"À <b>comprendre</b>, pas à écrire. C'est du français parlé d'ici, très courant et parfaitement normal — mais on ne l'écrit pas dans un courriel."},

      {t:'labo', h:"La même question, trois façons",
       p:"Choisis le renseignement que tu cherches et la façon de le demander.",
       axes:[
         {id:'r', lbl:'Tu cherches quoi ?', opts:[['a','le jour'],['b','le prix'],['c','le matériel']]},
         {id:'f', lbl:'Quelle façon ?', opts:[['1','la plus courte'],['2','avec est-ce que']]}],
       out:{
         a1:{w:["{C'est quand} ?"], say:"C'est quand ?", n:'deux mots, et on comprend'},
         a2:{w:["{Quand est-ce que} ça commence ?"], say:"Quand est-ce que ça commence ?", n:"plus long, tout aussi juste"},
         b1:{w:["{C'est combien} ?"], say:"C'est combien ?", n:'la question du tarif'},
         b2:{w:["{Combien est-ce que} ça coûte ?"], say:"Combien est-ce que ça coûte ?", n:'la même chose, en entier'},
         c1:{w:["{Il faut apporter quoi} ?"], say:"Il faut apporter quoi ?", n:'le mot de question à la fin'},
         c2:{w:["{Est-ce qu'}il faut apporter quelque chose ?"], say:"Est-ce qu'il faut apporter quelque chose ?", n:"la forme la plus polie des deux"},
       },
       note:"Six phrases, trois renseignements. Choisis celle qui sort le plus facilement de ta bouche : c'est la bonne."},

      {t:'ex', h:"À écouter et à répéter",
       p:"Six questions à poser au téléphone.",
       rows:[
         ["Bonjour, je voudrais des renseignements sur le badminton.","la phrase d'ouverture"],
         ["C'est quel jour, et à quelle heure ?","deux questions d'un coup"],
         ["C'est combien par séance ?","le tarif"],
         ["Est-ce qu'il faut apporter quelque chose ?","le matériel"],
         ["C'est où, exactement ?","le lieu"],
         ["Alors mardi, sept heures, trois dollars, des espadrilles.","répéter pour vérifier"],
       ]},

      {t:'piege', h:"Trois pièges à connaître",
       rows:[
         ["oublier de répéter à la fin","raccrocher sans vérifier",
          "Répéter les quatre renseignements prend dix secondes et évite de se tromper de soir. C'est ce que fait Marisol, et la préposée le confirme."],
         ["poser les quatre questions en une seule phrase","« C'est quand combien où quoi apporter ? »",
          "Une question à la fois. Laisse la personne répondre avant la suivante : c'est plus facile pour elle, et pour toi."],
         ["croire que « est-ce que » est plus poli","hésiter entre les formes",
          "Aucune des trois n'est impolie. Ce qui rend une demande polie, c'est « bonjour », « s'il vous plaît » et « merci » — pas la forme de la question."],
       ]},

      {t:'check', h:"Est-ce que c'est clair maintenant ?",
       p:"Quatre questions rapides.",
       qs:[
         {q:"Devant une voyelle, « est-ce que » devient…", opts:["est-ce qu'","est-ce que"], ok:0,
          fb:"Est-ce qu'il faut, est-ce qu'on peut."},
         {q:"« Ça commence-tu ? » est…", opts:["une faute","du français parlé du Québec"], ok:1,
          fb:"À comprendre à l'oral ; on ne l'écrit pas."},
         {q:"Les quatre questions à poser sont…", opts:["quand, combien, où, quoi apporter","qui, quoi, comment, pourquoi"], ok:0,
          fb:"Ce sont celles qui permettent de choisir une activité."},
         {q:"Après avoir tout demandé, la bonne réflexe est…", opts:["remercier et raccrocher","répéter ce qu'on a compris"], ok:1,
          fb:"Répéter, puis remercier."},
       ]},

      {t:'revoir', h:"À retenir",
       p:"Trois façons, aucune n'est meilleure : <b>C'est quand ?</b> · <b>Est-ce que ça commence bientôt ?</b> · <b>Quand commence la session ?</b> Et à la fin, toujours : répète ce que tu as compris."},
    ]
  },

  t1poli: {
    eye:'Mini-leçon', tit:'Je voudrais, j\'aimerais, vous pourriez',
    blocs:[
      {t:'texte', h:"La forme en -rais adoucit tout",
       p:"« Je veux des renseignements » est juste, mais sec — au téléphone, ça surprend. Le français a une forme spéciale pour demander sans donner d'ordre : le verbe se termine en <b>-rais</b>. « Je <b>voudrais</b> », « j'<b>aimerais</b> », « vous <b>pourriez</b> ». C'est la forme du comptoir, du téléphone et de tous les services.",
       note:"On l'appelle le conditionnel de politesse. Le nom n'a pas d'importance ; la terminaison, oui : elle s'entend « rè » dans tous les cas."},

      {t:'ana', h:"Pour dire ce que tu veux",
       p:"Deux verbes, le même sens.",
       mots:[['Le plus courant','{Je voudrais} des renseignements.'],['Un peu plus doux','{J\'aimerais} essayer le badminton.',true],['Avec s\'il vous plaît','{Je voudrais} m\'inscrire, s\'il vous plaît.']],
       say:"Je voudrais des renseignements. J'aimerais essayer le badminton.",
       note:"« Je voudrais » est la phrase la plus utile de tout le module. Apprends-la par cœur : elle ouvre n'importe quelle conversation de service."},

      {t:'ana', h:"Pour demander la permission",
       p:"Le verbe <i>pouvoir</i>, à la même forme.",
       mots:[['Pour toi','Est-ce que {je pourrais} venir voir une fois ?'],['Pour l\'autre','{Vous pourriez} répéter, s\'il vous plaît ?',true],['Sans est-ce que','{Je pourrais} avoir un feuillet ?']],
       say:"Est-ce que je pourrais venir voir une fois ? Vous pourriez répéter, s'il vous plaît ?",
       note:"« Vous pourriez répéter, s'il vous plaît ? » est la deuxième phrase à apprendre par cœur. Elle sauve toutes les conversations où ça va trop vite."},

      {t:'ana', h:"Pour dire ce qui est nécessaire",
       p:"Le verbe <i>falloir</i> existe aux deux formes.",
       mots:[['Une règle ferme','{Il faut} des espadrilles propres.'],['Un conseil','{Il faudrait} apporter une preuve d\'adresse.',true],['Une question','Est-ce qu\'{il faut} payer à l\'avance ?']],
       say:"Il faut des espadrilles propres. Il faudrait apporter une preuve d'adresse.",
       note:"« Il faut » est une obligation ; « il faudrait » ressemble à un conseil. La préposée emploie souvent le second pour ne pas avoir l'air de commander."},

      {t:'labo', h:"Sec, ou poli ?",
       p:"Choisis ce que tu demandes et la façon de le dire.",
       axes:[
         {id:'d', lbl:'Tu demandes quoi ?', opts:[['a','des renseignements'],['b','venir essayer'],['c','qu\'on répète']]},
         {id:'f', lbl:'Comment ?', opts:[['1','sec'],['2','poli']]}],
       out:{
         a1:{w:["Je {veux} des renseignements."], say:"Je veux des renseignements.", n:'juste, mais sec au téléphone'},
         a2:{w:["Je {voudrais} des renseignements, s'il vous plaît."], say:"Je voudrais des renseignements, s'il vous plaît.", n:'la forme du service'},
         b1:{w:["Je {viens} essayer jeudi."], say:"Je viens essayer jeudi.", n:"tu annonces, tu ne demandes pas"},
         b2:{w:["Est-ce que {je pourrais} venir essayer jeudi ?"], say:"Est-ce que je pourrais venir essayer jeudi ?", n:'tu laisses le choix à l\'autre'},
         c1:{w:["{Répétez}."], say:"Répétez.", n:"c'est un ordre"},
         c2:{w:["{Vous pourriez} répéter, s'il vous plaît ?"], say:"Vous pourriez répéter, s'il vous plaît ?", n:'la phrase à apprendre par cœur'},
       },
       note:"Écoute les deux colonnes l'une après l'autre. La différence tient à trois lettres, et elle s'entend tout de suite."},

      {t:'ex', h:"À écouter et à répéter",
       p:"Six phrases du téléphone et du comptoir.",
       rows:[
         ["Bonjour, je voudrais des renseignements, s'il vous plaît.","l'ouverture"],
         ["J'aimerais essayer la danse en ligne.","un souhait"],
         ["Est-ce que je pourrais venir voir une fois ?","une permission"],
         ["Vous pourriez répéter le prix, s'il vous plaît ?","un service"],
         ["Il faudrait apporter une preuve d'adresse.","un conseil"],
         ["Merci beaucoup, vous avez été bien gentille.","la sortie"],
       ]},

      {t:'piege', h:"Trois pièges à connaître",
       rows:[
         ["écrire « je voudrai » sans s","une seule lettre oubliée",
          "« Je voudrai » (sans s) veut dire plus tard, dans le futur. « Je voudrais » (avec s) est la demande polie. À l'oral, on entend « rè » pour le second."],
         ["dire « je peux » à la place de « je pourrais »","« Je peux venir jeudi ? »",
          "Ce n'est pas faux, mais c'est plus direct. « Je pourrais » laisse à l'autre la possibilité de dire non, et c'est ce qui le rend poli."],
         ["oublier « s'il vous plaît »","une demande toute nue",
          "La forme en -rais adoucit ; « s'il vous plaît » finit le travail. Les deux ensemble, et la demande est parfaite."],
       ]},

      {t:'check', h:"Est-ce que c'est clair maintenant ?",
       p:"Quatre questions rapides.",
       qs:[
         {q:"La forme polie de « je veux » est…", opts:["je voudrai","je voudrais"], ok:1,
          fb:"Avec un s : je voudrais."},
         {q:"Pour demander qu'on répète, on dit…", opts:["Répétez.","Vous pourriez répéter ?"], ok:1,
          fb:"La deuxième est une demande, la première un ordre."},
         {q:"« Il faudrait » est…", opts:["plus doux que « il faut »","plus ferme que « il faut »"], ok:0,
          fb:"Ça ressemble à un conseil."},
         {q:"La terminaison de la forme polie s'entend…", opts:["« ré »","« rè »"], ok:1,
          fb:"voudrais, aimerais, pourriez : toujours « rè »."},
       ]},

      {t:'revoir', h:"À retenir",
       p:"Deux phrases à savoir par cœur : <b>« Je voudrais des renseignements, s'il vous plaît. »</b> pour ouvrir, et <b>« Vous pourriez répéter, s'il vous plaît ? »</b> pour ne rien perdre."},
    ]
  },

  t2heure: {
    eye:'Mini-leçon', tit:"Dix-neuf heures trente, ou sept heures et demie ?",
    blocs:[
      {t:'texte', h:"Deux systèmes, et il faut les deux",
       p:"Un feuillet de loisirs écrit <b>19 h 30</b>. La préposée, au téléphone, dit « <b>sept heures et demie</b> ». Ce n'est pas une contradiction : le premier est l'heure officielle, celle des papiers et des horaires ; le second est l'heure de tous les jours, celle qu'on parle. Il faut savoir passer de l'une à l'autre, dans les deux sens.",
       note:"Au Québec, on écrit « 19 h 30 » avec un h minuscule et des espaces autour. Pas de « h » majuscule, pas de deux-points comme en anglais."},

      {t:'ana', h:"L'heure officielle — de 0 h à 24 h",
       p:"Celle du feuillet, du billet et de l'horaire affiché.",
       mots:[['On écrit','19 h 30'],['On dit','{dix-neuf heures trente}',true],['Avantage','aucun doute : c\'est le soir']],
       say:"Dix-neuf heures trente.",
       note:"Après midi, les heures continuent : 13, 14, 15… jusqu'à 23. Minuit, c'est 0 h ou 24 h selon les papiers."},

      {t:'ana', h:"L'heure de tous les jours — de 1 à 12",
       p:"Celle qu'on entend dans un dialogue.",
       mots:[['On dit','{sept heures et demie} {du soir}'],['Calcul','19 − 12 = 7',true],['Avant midi','9 h se dit {neuf heures}, sans calcul']],
       say:"Sept heures et demie du soir. Neuf heures du matin.",
       note:"Ajoute <b>du matin</b> ou <b>du soir</b> quand ce n'est pas évident. « On se voit à sept heures » sans précision peut mener à un malentendu de douze heures."},

      {t:'ana', h:"Les demies et les quarts",
       p:"Trois expressions, et presque tout est couvert.",
       mots:[['30 minutes','sept heures {et demie}'],['15 minutes','une heure {et quart}',true],['45 minutes','neuf heures {moins quart}']],
       say:"Sept heures et demie. Une heure et quart. Neuf heures moins quart.",
       note:"« Moins quart » se calcule sur l'heure <b>suivante</b> : 20 h 45, c'est neuf heures moins quart, pas huit heures moins quart."},

      {t:'ana', h:"Le début et la fin : de… à…",
       p:"Une activité a toujours deux heures, pas une.",
       mots:[['Sur le feuillet','19 h à 21 h'],['On dit','{de sept heures à neuf heures}',true],['Ou encore','ça dure deux heures']],
       say:"De sept heures à neuf heures.",
       note:"Sans les deux petits mots <b>de</b> et <b>à</b>, la phrase ne tient pas. C'est ce qui distingue un horaire d'un rendez-vous."},

      {t:'labo', h:"Passer d'une heure à l'autre",
       p:"Choisis une heure officielle et vois comment elle se dit.",
       axes:[{id:'h', lbl:'Quelle heure ?', opts:[
         ['a','10 h'],
         ['b','13 h 15'],
         ['c','19 h'],
         ['d','19 h 30'],
         ['e','20 h 45']]}],
       out:{
         a:{w:['10 h → {dix heures du matin}'], say:"Dix heures du matin.", n:'avant midi, rien à calculer'},
         b:{w:['13 h 15 → {une heure et quart}'], say:"Une heure et quart.", n:'13 − 12 = 1'},
         c:{w:['19 h → {sept heures du soir}'], say:"Sept heures du soir.", n:'19 − 12 = 7'},
         d:{w:['19 h 30 → {sept heures et demie}'], say:"Sept heures et demie.", n:'la séance du ciné-club'},
         e:{w:['20 h 45 → {neuf heures moins quart}'], say:"Neuf heures moins quart.", n:"on compte sur l'heure suivante"},
       },
       note:"Cinq heures du feuillet, cinq façons de les dire. Ce sont exactement celles du centre communautaire."},

      {t:'ex', h:"À écouter et à répéter",
       p:"Six phrases d'horaire.",
       rows:[
         ["Le badminton, c'est de sept heures à neuf heures.","de… à…"],
         ["La séance commence à sept heures et demie.","la demie"],
         ["L'heure des familles est à dix heures du matin.","avant midi"],
         ["La cuisine collective commence à une heure et quart.","le quart"],
         ["Le centre ferme à neuf heures moins quart.","moins quart"],
         ["Le film du 24 octobre est à deux heures de l'après-midi.","14 h"],
       ]},

      {t:'piege', h:"Trois pièges à connaître",
       rows:[
         ["oublier « du matin » ou « du soir »","« On se voit à sept heures »",
          "Douze heures d'écart. Précise dès qu'il y a le moindre doute."],
         ["calculer « moins quart » sur la mauvaise heure","dire « huit heures moins quart » pour 20 h 45",
          "« Moins quart » veut dire : il manque quinze minutes avant l'heure suivante. 20 h 45 → neuf heures moins quart."],
         ["écrire 7:30 PM","la forme anglaise",
          "En français, on écrit <b>19 h 30</b> ou <b>7 h 30 du soir</b>. Le « PM » ne se lit pas ici."],
       ]},

      {t:'check', h:"Est-ce que c'est clair maintenant ?",
       p:"Quatre questions rapides.",
       qs:[
         {q:"19 h se dit, en parlant…", opts:["sept heures du soir","neuf heures du soir"], ok:0,
          fb:"19 − 12 = 7."},
         {q:"20 h 45 se dit…", opts:["huit heures moins quart","neuf heures moins quart"], ok:1,
          fb:"On compte sur l'heure suivante."},
         {q:"13 h 15 se dit…", opts:["une heure et quart","trois heures et quart"], ok:0,
          fb:"13 − 12 = 1."},
         {q:"Pour dire le début et la fin, on emploie…", opts:["de… à…","entre… et…"], ok:0,
          fb:"De sept heures à neuf heures."},
       ]},

      {t:'revoir', h:"À retenir",
       p:"Sur le papier, <b>19 h 30</b>. En parlant, <b>sept heures et demie du soir</b>. Après midi, on enlève 12 — et on précise toujours <b>du matin</b> ou <b>du soir</b>."},
    ]
  },

  t2adj: {
    eye:'Mini-leçon', tit:"L'adjectif qui décrit le film",
    blocs:[
      {t:'texte', h:"Le mot qui dit comment c'est",
       p:"Dans une description de film, presque tout tient en deux ou trois adjectifs : <i>court</i>, <i>drôle</i>, <i>triste</i>, <i>vrai</i>. Ce sont eux qui aident à choisir. En français, l'adjectif <b>s'accorde</b> : il change de forme selon le mot qu'il décrit. Ça ne s'entend pas toujours, mais ça s'écrit toujours.",
       note:"Trois questions à se poser, dans cet ordre : le mot décrit est-il masculin ou féminin ? Est-il singulier ou pluriel ? L'adjectif finit-il déjà par un e ?"},

      {t:'ana', h:"Au féminin — on ajoute un e",
       p:"Le mot décrit est féminin, l'adjectif suit.",
       mots:[['Masculin','un film court'],['Féminin','{une séance courte}',true],['Autre exemple','{une histoire vraie}']],
       say:"Un film court. Une séance courte. Une histoire vraie.",
       note:"Le e final se prononce parfois — courte, grande — parce qu'il fait sonner la consonne d'avant. C'est un bon indice à l'oreille."},

      {t:'ana', h:"Au pluriel — on ajoute un s",
       p:"Le s ne s'entend jamais : il faut y penser en écrivant.",
       mots:[['Singulier','un film court'],['Pluriel','{des films courts}',true],['Féminin pluriel','des séances courtes']],
       say:"Des films courts. Des séances courtes.",
       note:"Au féminin pluriel, on met les deux : le <b>e</b> du féminin, puis le <b>s</b> du pluriel. Dans cet ordre, toujours."},

      {t:'ana', h:"Ceux qui ne changent pas au féminin",
       p:"Ils finissent déjà par un e.",
       mots:[['Drôle','{un film drôle} · une comédie drôle'],['Triste','{une histoire triste} · un film triste',true],['Libre, propre','une salle libre · des espadrilles propres']],
       say:"Un film drôle. Une histoire triste. Une salle libre.",
       note:"On n'ajoute jamais un deuxième e. « Drôlee » n'existe pas. Au pluriel, par contre, le s revient : des films drôles."},

      {t:'ana', h:"Ceux qui doublent ou changent",
       p:"À apprendre un par un — il n'y en a pas beaucoup.",
       mots:[['gratuit','{une entrée gratuite}'],['gros','{un gros chaudron} · une grosse portion',true],['beau','{une belle soirée} · un beau film']],
       say:"Une entrée gratuite. Un gros chaudron. Une belle soirée.",
       note:"« Beau » devient « bel » devant une voyelle : un <b>bel</b> automne. Trois formes pour un seul mot, et c'est le pire du français."},

      {t:'labo', h:"Accorde l'adjectif",
       p:"Choisis un mot et un adjectif.",
       axes:[
         {id:'n', lbl:'Quel mot ?', opts:[['a','un film'],['b','une séance'],['c','des histoires']]},
         {id:'a', lbl:'Quel adjectif ?', opts:[['1','court'],['2','drôle'],['3','gratuit']]}],
       out:{
         a1:{w:['un film {court}'], say:"Un film court.", n:'masculin singulier : rien à ajouter'},
         a2:{w:['un film {drôle}'], say:"Un film drôle.", n:'finit déjà par e'},
         a3:{w:['un film {gratuit}'], say:"Un film gratuit.", n:'masculin singulier'},
         b1:{w:['une séance {courte}'], say:"Une séance courte.", n:'féminin : on ajoute un e'},
         b2:{w:['une séance {drôle}'], say:"Une séance drôle.", n:'pas de e de plus'},
         b3:{w:['une séance {gratuite}'], say:"Une séance gratuite.", n:'le t se met à sonner'},
         c1:{w:['des histoires {courtes}'], say:"Des histoires courtes.", n:'féminin pluriel : e puis s'},
         c2:{w:['des histoires {drôles}'], say:"Des histoires drôles.", n:'le s seulement'},
         c3:{w:['des histoires {gratuites}'], say:"Des histoires gratuites.", n:'e puis s, dans cet ordre'},
       },
       note:"Neuf phrases, une seule règle. Regarde à chaque fois le mot de gauche : c'est lui qui commande."},

      {t:'ex', h:"À écouter et à répéter",
       p:"Six phrases du feuillet.",
       rows:[
         ["Le documentaire est un film court.","masculin singulier"],
         ["La séance du samedi est gratuite pour les enfants.","féminin"],
         ["C'est une histoire vraie, tournée au Québec.","féminin"],
         ["Les deux comédies sont très drôles.","le s seulement"],
         ["Le drame raconte une histoire triste.","pas de changement"],
         ["Il reste des places libres dans la salle 2.","féminin pluriel"],
       ]},

      {t:'piege', h:"Trois pièges à connaître",
       rows:[
         ["oublier le s du pluriel","« des films court »",
          "Il ne s'entend pas, donc on l'oublie. Relis toujours en cherchant les mots au pluriel."],
         ["ajouter un e à un adjectif qui en a déjà un","« une histoire drôlee »",
          "Drôle, triste, libre, propre : ils sont déjà prêts pour le féminin."],
         ["placer l'adjectif avant le nom","« un court film »",
          "Ce n'est pas faux, mais ce n'est pas la place normale. En français, l'adjectif se met presque toujours <b>après</b> : un film court."],
       ]},

      {t:'check', h:"Est-ce que c'est clair maintenant ?",
       p:"Quatre questions rapides.",
       qs:[
         {q:"« une séance ___ » (court) s'écrit…", opts:["court","courte"], ok:1,
          fb:"Séance est féminin : on ajoute un e."},
         {q:"« des histoires ___ » (drôle) s'écrit…", opts:["drôles","drôlees"], ok:0,
          fb:"L'adjectif a déjà son e ; on n'ajoute que le s."},
         {q:"La place normale de l'adjectif est…", opts:["avant le nom","après le nom"], ok:1,
          fb:"un film policier, une salle libre."},
         {q:"« une entrée ___ » (gratuit) s'écrit…", opts:["gratuit","gratuite"], ok:1,
          fb:"Le t se met à sonner au féminin."},
       ]},

      {t:'revoir', h:"À retenir",
       p:"Regarde le nom, pas l'adjectif. <b>Féminin</b> → un e. <b>Pluriel</b> → un s. <b>Les deux</b> → e puis s. Et si l'adjectif finit déjà par e, on ne touche à rien au féminin."},
    ]
  },

  t3imper: {
    eye:'Mini-leçon', tit:"L'impératif : la forme qui donne une consigne",
    blocs:[
      {t:'texte', h:"Une recette ne raconte rien, elle demande",
       p:"Regarde une recette : il n'y a aucun « je », aucun « vous » écrit devant les verbes. « <b>Pelez</b> six pommes de terre. » « <b>Faites</b> bouillir vingt minutes. » C'est une forme de verbe faite pour donner une consigne, et elle sert partout : les recettes, les modes d'emploi, les affiches du centre, les consignes du moniteur.",
       note:"Le programme de niveau 3 nomme cette forme explicitement, et c'est la seule situation où on la rencontre à l'écrit tous les jours : la recette."},

      {t:'ana', h:"La forme en -ez — celle des recettes",
       p:"On prend le verbe avec <i>vous</i>, et on enlève le mot <i>vous</i>.",
       mots:[['vous pelez →','{Pelez} six pommes de terre.'],['vous coupez →','{Coupez}-les en gros morceaux.',true],['vous ajoutez →','{Ajoutez} 60 ml de lait.']],
       say:"Pelez six pommes de terre. Coupez-les en gros morceaux. Ajoutez soixante millilitres de lait.",
       note:"C'est la forme écrite, celle de tous les livres de recettes. Elle s'adresse à tout le monde en même temps, ce qui tombe bien dans une cuisine collective."},

      {t:'ana', h:"La forme en -e — entre amis",
       p:"Avec <i>tu</i>, et sans s pour les verbes en -er.",
       mots:[['tu coupes →','{Coupe les oignons}, s\'il te plaît.'],['tu mélanges →','Mélange doucement.',true],['Attention','pas de s : « coupe », jamais « coupes »']],
       say:"Coupe les oignons, s'il te plaît. Mélange doucement.",
       note:"C'est celle que Denis emploie dans la cuisine quand il s'adresse à une seule personne qu'il connaît. À l'écrit, on garde le -ez."},

      {t:'ana', h:"Trois verbes irréguliers, très utiles",
       p:"Ils ne suivent pas la règle, et ils reviennent tout le temps.",
       mots:[['faire →','{Faites bouillir} vingt minutes.'],['mettre →','{Mettez} le chaudron sur le rond.',true],['être →','Soyez prudents avec l\'eau chaude.']],
       say:"Faites bouillir vingt minutes. Mettez le chaudron sur le rond.",
       note:"« Faites », pas « faisez ». C'est le seul vraiment traître des trois."},

      {t:'ana', h:"Les verbes d'une recette, dans l'ordre",
       p:"Sept gestes, et presque toutes les recettes sont couvertes.",
       mots:[['Préparer','pelez · lavez · {coupez}'],['Cuire','faites bouillir · {égouttez}',true],['Finir','{écrasez} · ajoutez · mélangez']],
       say:"Pelez, lavez, coupez. Faites bouillir, égouttez. Écrasez, ajoutez, mélangez.",
       note:"Une recette se lit dans l'ordre, une ligne à la fois. Ne saute pas de ligne : chaque geste prépare le suivant."},

      {t:'labo', h:"Donne la consigne",
       p:"Choisis un geste et à qui tu parles.",
       axes:[
         {id:'g', lbl:'Quel geste ?', opts:[['a','peler'],['b','couper'],['c','mélanger']]},
         {id:'p', lbl:'Tu parles à qui ?', opts:[['1','au groupe (vous)'],['2','à une amie (tu)']]}],
       out:{
         a1:{w:['{Pelez} les pommes de terre.'], say:"Pelez les pommes de terre.", n:'la forme écrite de la recette'},
         a2:{w:['{Pèle} les pommes de terre.'], say:"Pèle les pommes de terre.", n:"l'accent apparaît : pèle"},
         b1:{w:['{Coupez} les oignons.'], say:"Coupez les oignons.", n:'-ez'},
         b2:{w:['{Coupe} les oignons.'], say:"Coupe les oignons.", n:'pas de s'},
         c1:{w:['{Mélangez} jusqu\'à ce que ce soit lisse.'], say:"Mélangez jusqu'à ce que ce soit lisse.", n:'la dernière ligne de la recette'},
         c2:{w:['{Mélange} doucement.'], say:"Mélange doucement.", n:'pas de s non plus'},
       },
       note:"Six consignes. À l'écrit, prends toujours la colonne de gauche : c'est celle des recettes."},

      {t:'ex', h:"À écouter et à répéter",
       p:"Six consignes de la recette du pâté chinois.",
       rows:[
         ["Pelez six pommes de terre.","le premier geste"],
         ["Coupez-les en gros morceaux.","le pronom se colle au verbe"],
         ["Faites bouillir vingt minutes.","verbe irrégulier"],
         ["Égouttez, puis écrasez.","deux gestes de suite"],
         ["Ajoutez 60 ml de lait et une cuillère à soupe de beurre.","les quantités"],
         ["Mélangez jusqu'à ce que ce soit lisse.","la fin"],
       ]},

      {t:'piege', h:"Trois pièges à connaître",
       rows:[
         ["écrire « vous » devant le verbe","« Vous pelez six pommes de terre »",
          "Ce n'est plus une consigne, c'est une description. Dans une recette, on enlève le mot « vous »."],
         ["mettre un s à la forme en -e","« Coupes les oignons »",
          "Avec <i>tu</i>, les verbes en -er perdent leur s à l'impératif : coupe, mélange, ajoute."],
         ["dire « faisez »","au lieu de « faites »",
          "Le verbe <i>faire</i> est irrégulier partout. « Faites bouillir » s'apprend tel quel."],
       ]},

      {t:'check', h:"Est-ce que c'est clair maintenant ?",
       p:"Quatre questions rapides.",
       qs:[
         {q:"Dans une recette écrite, on emploie…", opts:["la forme en -ez","la forme en -e"], ok:0,
          fb:"Pelez, coupez, ajoutez, mélangez."},
         {q:"Avec « tu », « couper » donne…", opts:["coupes","coupe"], ok:1,
          fb:"Pas de s aux verbes en -er."},
         {q:"L'impératif de « faire » est…", opts:["faisez","faites"], ok:1,
          fb:"Faites bouillir vingt minutes."},
         {q:"Dans une consigne, le mot « vous »…", opts:["s'écrit devant le verbe","ne s'écrit pas"], ok:1,
          fb:"C'est ce qui distingue la consigne de la description."},
       ]},

      {t:'revoir', h:"À retenir",
       p:"Une recette parle en <b>-ez</b> : pelez, coupez, égouttez, écrasez, ajoutez, mélangez — et <b>faites</b> bouillir. Aucun sujet devant le verbe, jamais."},
    ]
  },

  t3quant: {
    eye:'Mini-leçon', tit:'Du lait, de la crème, des pommes de terre',
    blocs:[
      {t:'texte', h:"Ce qui se compte, et ce qui ne se compte pas",
       p:"Une recette parle de deux sortes de choses. Celles qu'on peut compter — <b>six</b> pommes de terre, <b>deux</b> oignons — et celles qu'on ne compte pas : le lait, la crème, l'eau, le sel. Pour les premières, on dit <b>des</b>. Pour les secondes, on prend une partie : <b>du</b> lait, <b>de la</b> crème, <b>de l'</b>eau.",
       note:"C'est un des points les plus difficiles du français, et une recette est le meilleur endroit pour l'apprendre : tout y est, en cinq lignes."},

      {t:'ana', h:"Une partie de quelque chose",
       p:"Trois formes, selon le mot qui suit.",
       mots:[['Masculin','{du lait} · du beurre · du sel'],['Féminin','{de la crème} · de la farine',true],['Devant une voyelle','{de l\'eau} · de l\'huile']],
       say:"Du lait, du beurre. De la crème, de la farine. De l'eau, de l'huile.",
       note:"Ce n'est pas une quantité précise : c'est « une certaine quantité de ». La recette dira ensuite combien, en millilitres ou en cuillères."},

      {t:'ana', h:"Ce qui se compte prend « des »",
       p:"On pourrait les compter un par un.",
       mots:[['On dit','{des pommes de terre}'],['Aussi','{des oignons} · des carottes',true],['Avec un nombre','six pommes de terre · deux oignons']],
       say:"Des pommes de terre, des oignons, des carottes.",
       note:"Dès qu'un nombre apparaît, « des » disparaît : on dit « six pommes de terre », jamais « six des pommes de terre »."},

      {t:'ana', h:"Après une quantité, toujours « de »",
       p:"C'est la règle qui sauve le plus de fautes.",
       mots:[['Une mesure','60 ml {de lait} · une tasse de farine'],['Un peu','{un peu de sel} · {un peu d\'huile}',true],['Beaucoup','{beaucoup d\'eau} · beaucoup de monde']],
       say:"Soixante millilitres de lait. Un peu de sel. Beaucoup d'eau.",
       note:"On ne dit jamais « un peu du sel » ni « beaucoup de l'eau ». Après une quantité, il ne reste que <b>de</b> — ou <b>d'</b> devant une voyelle."},

      {t:'ana', h:"À la forme négative, tout devient « de »",
       p:"Du, de la, des : les trois se transforment.",
       mots:[['Positif','Je prends du maïs.'],['Négatif','Je ne prends {pas de maïs}.',true],['Avec une voyelle','Il n\'y a pas d\'oignon.']],
       say:"Je prends du maïs. Je ne prends pas de maïs. Il n'y a pas d'oignon.",
       note:"Une seule exception : avec le verbe <i>être</i>, rien ne change. « Ce n'est pas du lait » garde son du."},

      {t:'ana', h:"Le mot « tout »",
       p:"Il s'accorde comme un adjectif, avec quatre formes.",
       mots:[['Masculin','{tout le lait}'],['Féminin','toute la crème',true],['Pluriel','tous les oignons · {toutes les portions}']],
       say:"Tout le lait. Toute la crème. Tous les oignons. Toutes les portions.",
       note:"Au masculin pluriel, « tous » se prononce « tou » devant un nom : tou(s) les oignons. Le s ne s'entend pas."},

      {t:'labo', h:"Quel petit mot ?",
       p:"Choisis un aliment et une façon d'en parler.",
       axes:[
         {id:'a', lbl:'Quel aliment ?', opts:[['a','lait'],['b','crème'],['c','eau'],['d','oignons']]},
         {id:'f', lbl:'Comment ?', opts:[['1','une partie'],['2','un peu']]}],
       out:{
         a1:{w:['{du} lait'], say:"Du lait.", n:'masculin'},
         a2:{w:['un peu {de} lait'], say:"Un peu de lait.", n:'après une quantité : de'},
         b1:{w:['{de la} crème'], say:"De la crème.", n:'féminin'},
         b2:{w:['un peu {de} crème'], say:"Un peu de crème.", n:'de, même au féminin'},
         c1:{w:['{de l\'}eau'], say:"De l'eau.", n:'devant une voyelle'},
         c2:{w:['un peu {d\'}eau'], say:"Un peu d'eau.", n:"de devient d'"},
         d1:{w:['{des} oignons'], say:"Des oignons.", n:'ça se compte'},
         d2:{w:['un peu {d\'}oignon'], say:"Un peu d'oignon.", n:'au singulier, cette fois'},
       },
       note:"Huit phrases. Regarde la deuxième colonne : dès qu'il y a une quantité, il ne reste que « de »."},

      {t:'ex', h:"À écouter et à répéter",
       p:"Six phrases de la recette.",
       rows:[
         ["Ajoutez du lait et une cuillère à soupe de beurre.","du, puis de"],
         ["Pelez des pommes de terre et deux oignons.","des, puis un nombre"],
         ["Mettez un peu de sel, pas plus.","après une quantité"],
         ["Faites bouillir beaucoup d'eau.","devant une voyelle"],
         ["Camila ne veut pas de maïs.","à la forme négative"],
         ["Comptez toutes les portions avant de partir.","tout au féminin pluriel"],
       ]},

      {t:'piege', h:"Trois pièges à connaître",
       rows:[
         ["garder « du » après une quantité","« un peu du sel »",
          "Après un peu, beaucoup, 60 ml, une tasse : seulement <b>de</b>. C'est la faute la plus fréquente, et la plus facile à corriger."],
         ["oublier de transformer au négatif","« Je ne veux pas du maïs »",
          "À la forme négative, du, de la et des deviennent tous <b>de</b> : « pas de maïs »."],
         ["mettre « des » devant un nombre","« six des pommes de terre »",
          "Le nombre remplace le petit mot : « six pommes de terre »."],
       ]},

      {t:'check', h:"Est-ce que c'est clair maintenant ?",
       p:"Quatre questions rapides.",
       qs:[
         {q:"« Ajoutez ___ crème » se complète avec…", opts:["du","de la"], ok:1,
          fb:"Crème est féminin."},
         {q:"« Un peu ___ sel » se complète avec…", opts:["de","du"], ok:0,
          fb:"Après une quantité, seulement « de »."},
         {q:"« Je ne veux pas ___ maïs » se complète avec…", opts:["du","de"], ok:1,
          fb:"À la forme négative, du devient de."},
         {q:"Devant « eau », on écrit…", opts:["de la eau","de l'eau"], ok:1,
          fb:"Devant une voyelle, on colle : de l'eau."},
       ]},

      {t:'revoir', h:"À retenir",
       p:"Ce qui se compte : <b>des</b>. Ce qui ne se compte pas : <b>du</b>, <b>de la</b>, <b>de l'</b>. Après une quantité ou une négation, il ne reste que <b>de</b>."},
    ]
  },

  t3abrev: {
    eye:'Mini-leçon', tit:'Les abréviations et les mesures de la recette',
    blocs:[
      {t:'texte', h:"Une recette est écrite en abrégé",
       p:"Une feuille de recette tient sur une page parce que presque tout y est raccourci : <b>ml</b>, <b>c. à soupe</b>, <b>g</b>, <b>min</b>, <b>°C</b>. Ce ne sont pas des mots difficiles : ce sont des mots courants dont on n'écrit que le début. Une fois qu'on les connaît, la page entière devient lisible.",
       note:"Le programme de niveau 3 demande justement de reconnaître « les abréviations et les symboles utiles ». C'est le point le plus vite rentable de tout le défi."},

      {t:'ana', h:"Les liquides — en millilitres",
       p:"Le Québec mesure en millilitres, et en tasses.",
       mots:[['On écrit','60 ml'],['On dit','soixante millilitres',true],['Repère','250 ml = 1 tasse · 60 ml = le quart d\'une tasse']],
       say:"Soixante millilitres. Deux cent cinquante millilitres, une tasse.",
       note:"La tasse à mesurer porte les deux échelles : les millilitres d'un côté, les tasses de l'autre. Regarde à hauteur des yeux, pas de haut."},

      {t:'ana', h:"Les cuillères — deux tailles, jamais plus",
       p:"Toute la différence tient à un mot.",
       mots:[['La grande','c. à soupe = 15 ml'],['La petite','c. à thé = 5 ml',true],['À retenir','une c. à soupe = trois c. à thé']],
       say:"Une cuillère à soupe, quinze millilitres. Une cuillère à thé, cinq millilitres.",
       note:"Trois fois plus grande : c'est l'erreur la plus coûteuse d'une recette. Une cuillère à soupe de sel au lieu d'une cuillère à thé, et le plat est perdu."},

      {t:'ana', h:"Le poids, le temps et la chaleur",
       p:"Trois abréviations qu'on retrouve partout.",
       mots:[['Le poids','500 g · 1 kg'],['Le temps','20 min · 1 h 30',true],['La chaleur','180 °C · 350 °F']],
       say:"Cinq cents grammes. Vingt minutes. Cent quatre-vingts degrés Celsius.",
       note:"Les fours du Québec sont souvent gradués en °F. 180 °C correspond à peu près à 350 °F — c'est la température la plus courante des recettes."},

      {t:'labo', h:"Que veut dire cette abréviation ?",
       p:"Choisis une abréviation de la recette.",
       axes:[{id:'a', lbl:'Quelle abréviation ?', opts:[
         ['a','60 ml'],
         ['b','1 c. à soupe'],
         ['c','1 c. à thé'],
         ['d','20 min'],
         ['e','4 pers.']]}],
       out:{
         a:{w:['60 ml → {soixante millilitres}'], say:"Soixante millilitres, le quart d'une tasse.", n:'le quart d\'une tasse'},
         b:{w:['1 c. à soupe → {une cuillère à soupe}'], say:"Une cuillère à soupe, quinze millilitres.", n:'la grande, 15 ml'},
         c:{w:['1 c. à thé → {une cuillère à thé}'], say:"Une cuillère à thé, cinq millilitres.", n:'la petite, 5 ml'},
         d:{w:['20 min → {vingt minutes}'], say:"Vingt minutes de cuisson.", n:'le temps de cuisson'},
         e:{w:['4 pers. → {pour quatre personnes}'], say:"Pour quatre personnes.", n:'toujours écrit en haut de la recette'},
       },
       note:"Cinq abréviations, et la recette du pâté chinois se lit sans hésiter."},

      {t:'ex', h:"À écouter et à répéter",
       p:"Six lignes de recette.",
       rows:[
         ["Pâté chinois, 4 pers.","le nombre de portions"],
         ["6 pommes de terre moyennes","un nombre, un adjectif"],
         ["60 ml de lait","les liquides"],
         ["1 c. à soupe de beurre","la grande cuillère"],
         ["1 c. à thé de sel","la petite cuillère"],
         ["Cuisson : 30 min à 180 °C","le temps et la chaleur"],
       ]},

      {t:'piege', h:"Trois pièges à connaître",
       rows:[
         ["confondre c. à soupe et c. à thé","mettre trois fois trop de sel",
          "Un seul mot change, et la quantité est triplée. Lis la ligne deux fois avant de verser."],
         ["confondre °C et °F","mettre le four à 350 °C",
          "180 °C = 350 °F. Regarde toujours quelle échelle porte le bouton de ton four."],
         ["lire « 1 t. » comme « 1 tonne »","au lieu de « une tasse »",
          "Dans une recette, <b>t.</b> veut dire tasse : 250 ml. Le contexte décide toujours."],
       ]},

      {t:'check', h:"Est-ce que c'est clair maintenant ?",
       p:"Quatre questions rapides.",
       qs:[
         {q:"« c. à soupe » veut dire…", opts:["cuillère à soupe, 15 ml","cuillère à thé, 5 ml"], ok:0,
          fb:"C'est la grande cuillère."},
         {q:"250 ml, c'est…", opts:["une demi-tasse","une tasse"], ok:1,
          fb:"Et 60 ml, c'est le quart d'une tasse."},
         {q:"180 °C correspond à peu près à…", opts:["350 °F","180 °F"], ok:0,
          fb:"C'est la température la plus courante des recettes."},
         {q:"« 4 pers. » veut dire…", opts:["quatre personnes","quatre portions par personne"], ok:0,
          fb:"C'est le nombre de personnes servies."},
       ]},

      {t:'revoir', h:"À retenir",
       p:"<b>ml</b> = millilitre · <b>c. à soupe</b> = 15 ml · <b>c. à thé</b> = 5 ml · <b>t.</b> = tasse, 250 ml · <b>min</b> = minute · <b>°C</b> = degré Celsius. Six abréviations, et la recette se lit d'un trait."},
    ]
  },
};
