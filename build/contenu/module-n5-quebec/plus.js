const PLUS = {

  // ════════════════════════════════════════════════════════════════════════
  prPhon: {
    eye:'Mini-leçon', tit:"Le son de « ou » et le son de « u »",
    blocs:[
      {t:'texte', h:"Une seule chose bouge : la langue",
       p:"Ces deux voyelles sont la difficulté la plus répandue du français, et pour une raison simple : beaucoup de langues ont le son de « ou » et n'ont pas celui de « u ». L'oreille qui n'a jamais eu à les distinguer entend deux fois le même son, et la bouche fait deux fois le même geste. Or la différence est minuscule et parfaitement mécanique : les lèvres sont exactement pareilles dans les deux cas, arrondies et poussées en avant. Ce qui change, c'est la position de la langue — reculée pour « ou », avancée pour « u ». Rien d'autre.",
       note:"C'est une bonne nouvelle : un son qui dépend d'un seul muscle s'apprend en une semaine, à condition de travailler ce muscle-là et pas l'oreille."},

      {t:'ana', h:"Le son de « ou » : la langue recule",
       p:"Les lèvres avancent comme pour souffler une bougie, et la langue se retire vers le fond de la bouche. C'est le son le plus grave des deux, et c'est celui qui vient tout seul.",
       mots:[["Dans le voyage","la route · un tour · un groupe · la soute"],["Dans les noms de lieux","Rimouski · Chicoutimi · Tadoussac · Bouctouche",true],["Dans les mots de tous les jours","nous · vous · tout · le jour · beaucoup"]],
       say:"La route. Un tour de bateau. Rimouski. La soute.",
       note:"Si votre langue maternelle a déjà ce son, ne le travaillez pas : il est correct. Toute votre énergie doit aller sur l'autre."},

      {t:'ana', h:"Le son de « u » : la langue avance",
       p:"Gardez exactement les mêmes lèvres arrondies que pour « ou », et poussez seulement la langue vers les dents du haut, comme pour dire « i ». Le son qui sort est « u ».",
       mots:[["Dans le voyage","la nature · une chute · la durée · le sud"],["Dans les mots de tous les jours","tu · une rue · une minute · une voiture",true],["Dans les verbes","j'ai lu · j'ai vu · j'ai su · il a plu"]],
       say:"La nature. Une chute. La durée. Le sud.",
       note:"Le mot « nature » contient les deux difficultés à la file : le « a » ouvert, puis le « u ». Dites-le en trois temps — na-tu-re — jusqu'à ce que le milieu soit net."},

      {t:'ana', h:"Le geste qui règle le cas en dix secondes",
       p:"Dites « i » : la langue est bien en avant, contre les dents du haut. Gardez la langue exactement là, sans la bouger d'un millimètre, et arrondissez les lèvres. Le son qui sort est « u ». Refaites-le cinq fois de suite.",
       mots:[["L'exercice, dans l'ordre","i · u · i · u · i"],["Puis avec une consonne","di · du · ti · tu · li · lu",true],["Puis les paires complètes","tout / tu · nous / nu · la roue / la rue"]],
       say:"I. U. I. U. Tout, tu. Nous, nu. La roue, la rue.",
       note:"Faites-le devant un miroir. Les lèvres ne doivent pas bouger entre le « ou » et le « u » : si elles bougent, c'est que la langue ne travaille pas."},

      {t:'labo', h:"Écoutez la paire, puis le mot dans sa phrase",
       p:"Choisissez une paire et écoutez la différence, puis le mot replacé dans une phrase du module.",
       axes:[{id:'p', lbl:'Quelle paire ?', opts:[
         ['a','tout / tu'],
         ['b','nous / nu'],
         ['c','la roue / la rue'],
         ['d','la soute / la suite'],
         ['e','les quatre à la suite']]}],
       out:{
         a:{w:['la soute'], say:"Tout. Tu. Tu mets tout dans la soute.", n:"la langue recule, puis elle avance"},
         b:{w:['le fleuve'], say:"Nous. Nu. Nous avons vu le fleuve tout nu, sans un bateau dessus.", n:"la même consonne au départ, deux voyelles"},
         c:{w:['un sentier'], say:"La roue. La rue. La rue du sentier monte vers le village.", n:"la paire la plus connue, et la plus utile"},
         d:{w:['la soute','un horaire'], say:"La soute. La suite. La valise va dans la soute ; la suite de l'horaire est en bas.", n:"la paire du module, celle qui fait sourire les préposés"},
         e:{w:['la soute','le fleuve'], say:"Tout, tu. Nous, nu. La roue, la rue. La soute, la suite.", n:"quatre paires sans reprendre son souffle"},
       },
       note:"Écoutez chaque paire deux fois : la première pour entendre les deux mots, la seconde en surveillant votre propre langue."},

      {t:'ex', h:"À écouter et à répéter",
       p:"Six phrases prises dans le module.",
       rows:[
         ["Nous sommes partis de Rimouski vers midi.","« ou » trois fois"],
         ["La durée du trajet est de huit heures.","« u » deux fois, « ou » une fois"],
         ["La valise va dans la soute, le sac reste avec vous.","les deux sons dans la même phrase"],
         ["Le sentier de la nature fait cinq kilomètres.","« u » au milieu du mot"],
         ["Il a plu tout le jour, mais nous avons tout vu.","« u » et « ou » en alternance"],
         ["Un tour de bateau dure une heure et demie.","commence par « ou », finit par « u »"],
       ]},

      {t:'piege', h:"Trois pièges de « ou » et de « u »",
       rows:[
         ["arrondir les lèvres seulement pour « ou »","« la rrue » dit avec des lèvres larges, qui sonne comme « la ri »",
          "Les lèvres sont arrondies dans les deux cas, exactement pareil. Si elles s'écartent sur le « u », le son devient un « i » et « la rue » devient « la rie ». Le miroir règle ça en une minute."],
         ["croire que « ou » est plus long","« touuut » au lieu de « tout »",
          "Les deux voyelles ont la même longueur. Allonger le « ou » pour bien le distinguer donne un accent très marqué sans rendre le mot plus clair — et ça ne règle pas le « u », qui reste le vrai problème."],
         ["lire « u » dans « qu » et « gu »","« question » lu « qu-u-estion »",
          "Après q et g, le u ne se prononce pas : question, quatre, quai, guide, la guerre. Il est là pour l'orthographe. Le mot « quai », qu'on entend cinq fois dans une gare, se dit tout simplement « ké »."],
       ]},

      {t:'check', h:"Est-ce que c'est clair maintenant ?",
       p:"Quatre questions rapides.",
       qs:[
         {q:"Entre « ou » et « u », qu'est-ce qui bouge ?", opts:["les lèvres","la langue"], ok:1,
          fb:"La langue. Les lèvres restent arrondies dans les deux cas."},
         {q:"Pour trouver le son « u », on part…", opts:["du son « i »","du son « o »"], ok:0,
          fb:"Du son « i » : on garde la langue en avant et on arrondit les lèvres."},
         {q:"Dans « la soute », on entend…", opts:["le son de « ou »","le son de « u »"], ok:0,
          fb:"Le son de « ou ». « La suite », c'est autre chose — et ce n'est pas là qu'on met les valises."},
         {q:"Dans « le quai », le u…", opts:["se prononce","ne se prononce pas"], ok:1,
          fb:"Il ne se prononce pas. Après q et g, le u est muet."},
       ]},
    ]
  },

  // ════════════════════════════════════════════════════════════════════════
  prPrep: {
    eye:'Mini-leçon', tit:"À Rimouski, en Gaspésie, au Saguenay",
    blocs:[
      {t:'texte', h:"Ce n'est pas la distance qui décide, c'est le genre du nom",
       p:"« Je vais à Rimouski », mais « je vais en Gaspésie » et « je vais au Saguenay ». Trois prépositions différentes pour trois endroits du même Québec, situés à quelques heures les uns des autres. La règle n'a rien à voir avec la taille du lieu ni avec la distance : elle dépend du genre du nom et de sa forme. Une ville prend « à ». Une région féminine prend « en ». Une région masculine prend « au ». Un nom pluriel prend « dans les ». C'est mécanique, et une fois posé, ça ne bouge plus.",
       note:"C'est la faute qui identifie le plus vite quelqu'un qui n'est pas d'ici — plus qu'un accent, parce qu'elle s'entend à l'écrit aussi."},

      {t:'ana', h:"Devant une ville : à, toujours",
       p:"Aucune exception utile. Toutes les villes et tous les villages du Québec prennent « à », qu'ils soient grands, petits, connus ou non.",
       mots:[["Les grandes","à Montréal · à Québec · à Laval · à Gatineau"],["Celles du module","à Rimouski · à Trois-Rivières · à Rivière-du-Loup · à La Pocatière",true],["Ailleurs au Québec","à Chicoutimi · à Gaspé · à Val-d'Or · à Sept-Îles"]],
       say:"Je vais à Rimouski. Il s'arrête à Trois-Rivières et à Québec.",
       note:"Attention aux noms de villes qui contiennent un article — La Pocatière, Les Éboulements. On dit tout de même « à La Pocatière », l'article restant collé au nom."},

      {t:'ana', h:"Devant une région féminine : en, sans article",
       p:"Les noms de régions qui se terminent par -ie ou par -e sont féminins et prennent « en ». On ne met jamais d'article : « en la Gaspésie » ne se dit pas.",
       mots:[["Les régions en -ie","en Gaspésie · en Estrie · en Mauricie · en Montérégie"],["Les autres féminines","en Abitibi · en Beauce · en Matawinie",true],["Le piège du masculin","en Outaouais, malgré la finale en -ais"]],
       say:"Ma sœur habite en Gaspésie. Ils passent l'été en Mauricie.",
       note:"L'Outaouais est le cas qu'on retient comme une exception, parce qu'on l'entend beaucoup à la radio."},

      {t:'ana', h:"Devant une région masculine : au",
       p:"« Au », c'est « à » collé à « le ». On l'emploie devant les noms de régions masculins, et devant les noms de pays masculins pour la même raison.",
       mots:[["Les régions du module","au Bas-Saint-Laurent · au Saguenay · au Centre-du-Québec"],["Les autres","au Nunavik · au Lac-Saint-Jean · au Témiscamingue",true],["Et les pays, pour la même raison","au Québec · au Canada · au Viêt Nam · au Mexique"]],
       say:"Le parc du Bic se trouve au Bas-Saint-Laurent. Elle est arrivée au Québec il y a trois ans.",
       note:"On entend souvent « dans le Bas-Saint-Laurent » : c'est également correct, et un peu plus courant à l'oral. « Au » est la forme des dépliants."},

      {t:'ana', h:"Devant un pluriel : dans les",
       p:"Quand le nom de la région est au pluriel, on emploie « dans les ». On entend aussi la forme courte « aux », surtout pour les Îles.",
       mots:[["Les régions au pluriel","dans les Laurentides · dans les Cantons-de-l'Est"],["Les Îles","dans les Îles-de-la-Madeleine · aux Îles",true],["Et les lieux précis","dans le parc du Bic · sur le sentier · au bord du fleuve"]],
       say:"En hiver, on va skier dans les Laurentides. L'été, ils sont aux Îles.",
       note:"« Aux Îles » sans préciser lesquelles se comprend partout au Québec : ce sont les Îles-de-la-Madeleine, et rien d'autre."},

      {t:'labo', h:"Choisissez une destination, entendez la phrase",
       p:"Sélectionnez un endroit et écoutez la phrase complète, avec sa préposition.",
       axes:[{id:'d', lbl:'Vous allez où ?', opts:[
         ['a','Rimouski — une ville'],
         ['b','la Gaspésie — une région féminine'],
         ['c','le Saguenay — une région masculine'],
         ['d','les Laurentides — un pluriel'],
         ['e','le parc, le sentier, le bord du fleuve']]}],
       out:{
         a:{w:['un horaire'], say:"Je vais à Rimouski lundi prochain. L'horaire donne trois départs par jour.", n:"une ville : à, sans exception"},
         b:{w:['un attrait'], say:"Ma sœur habite en Gaspésie, dans un village au bord de la mer. Le principal attrait, c'est la mer elle-même.", n:"région féminine : en, sans article"},
         c:{w:['un vacancier'], say:"Ils passent leurs vacances au Saguenay tous les étés. Il y a plus de vacanciers que d'habitants au mois de juillet.", n:"région masculine : au"},
         d:{w:['un sentier'], say:"En hiver, tout le monde va skier dans les Laurentides. En été, on y marche sur les sentiers.", n:"nom pluriel : dans les"},
         e:{w:['un sentier','le fleuve'], say:"On entre dans le parc, on marche sur le sentier, et on s'assoit au bord du fleuve.", n:"dans un parc, sur un sentier, au bord du fleuve"},
       },
       note:"Écoutez les cinq à la file une fois par jour pendant une semaine. Ces prépositions s'installent par l'oreille bien plus vite que par la règle."},

      {t:'ex', h:"À écouter et à répéter",
       p:"Six phrases du module.",
       rows:[
         ["Je voudrais aller à Rimouski, dans le Bas-Saint-Laurent.","une ville, puis une région"],
         ["Sa sœur habite en Gaspésie depuis quinze ans.","région féminine"],
         ["Ils passent toujours leurs vacances au Saguenay.","région masculine"],
         ["En hiver, beaucoup de monde va skier dans les Laurentides.","nom pluriel"],
         ["Le gîte est au bord du fleuve, à dix minutes du village.","au bord du, puis à"],
         ["Elle est arrivée au Québec il y a trois ans.","un pays masculin, même règle"],
       ]},

      {t:'piege', h:"Trois pièges des prépositions de lieu",
       rows:[
         ["mettre un article après « en »","« en la Gaspésie », « en l'Estrie »",
          "« En » ne prend jamais d'article. On dit « en Gaspésie », comme on dit « en France ». L'article vient avec « au » et « dans les », jamais avec « en »."],
         ["choisir selon la taille du lieu","« au Rimouski » parce que c'est une grande ville",
          "La taille n'entre pas en jeu. Toutes les villes prennent « à », de Montréal au plus petit village. C'est le genre du nom qui décide, et une ville n'a pas de genre pour cette règle."],
         ["dire « dans » un sentier ou une rue","« dans le sentier », « dans la rue Berri »",
          "On est <b>sur</b> un sentier, <b>sur</b> une rue, <b>sur</b> une route ; on est <b>dans</b> un parc, <b>dans</b> un village, <b>dans</b> une région. « Dans la rue » existe, mais veut dire autre chose : sans domicile."],
       ]},

      {t:'check', h:"Est-ce que c'est clair maintenant ?",
       p:"Quatre questions rapides.",
       qs:[
         {q:"« Je vais ___ Gaspésie. »", opts:["en","dans la"], ok:0,
          fb:"En Gaspésie. Une région féminine prend « en », sans article."},
         {q:"« Je vais ___ Rimouski. »", opts:["à","au"], ok:0,
          fb:"À Rimouski. Toutes les villes prennent « à »."},
         {q:"« On skie ___ Laurentides. »", opts:["en","dans les"], ok:1,
          fb:"Dans les Laurentides. Le nom est au pluriel."},
         {q:"Le gîte est ___ bord du fleuve.", opts:["au","sur le"], ok:0,
          fb:"Au bord du fleuve. C'est une expression figée : on ne la construit pas mot à mot."},
       ]},
    ]
  },

  // ════════════════════════════════════════════════════════════════════════
  t1dem: {
    eye:'Mini-leçon', tit:"Demander poliment : la question indirecte",
    blocs:[
      {t:'texte', h:"La même question, et une tout autre impression",
       p:"« Ça prend combien de temps ? » et « Pourriez-vous me dire combien de temps ça prend ? » demandent exactement la même chose. La première est correcte, personne ne vous reprendra, et pourtant elle sonne sèche à un comptoir. La seconde prend une seconde de plus et change complètement le ton de l'échange. Ce n'est pas de la décoration : au Québec, la politesse passe beaucoup par ces formules d'ouverture, et pas du tout par le vocabulaire savant. Quelqu'un qui dit « pourriez-vous » avec un vocabulaire de trois cents mots sera toujours mieux reçu que quelqu'un qui exige avec un vocabulaire de trois mille.",
       note:"Ces formules s'apprennent comme des blocs, une fois pour toutes. Elles vous serviront au comptoir, au téléphone, à la banque, au CLSC, à l'école de vos enfants."},

      {t:'ana', h:"Les quatre débuts à savoir par cœur",
       p:"Ce sont eux qui font tout le travail. Le reste de la phrase ne change presque pas.",
       mots:[["Pour demander un renseignement","Pourriez-vous me dire… · Savez-vous… · Est-ce que vous savez…"],["Pour dire ce qu'on veut","Je voudrais savoir… · J'aimerais savoir… · Je me demandais…",true],["Pour demander une permission","Est-ce que je pourrais… · Est-ce qu'il serait possible de…"]],
       say:"Pourriez-vous me dire combien de temps ça prend ? Je voudrais savoir s'il y a une correspondance.",
       note:"« Je me demandais si… » est la plus douce des quatre. Elle s'emploie quand on demande une faveur plutôt qu'un renseignement."},

      {t:'ana', h:"Le mot de question ne bouge pas",
       p:"Combien, quand, où, comment, pourquoi, à quelle heure : il reste exactement où il était dans la question directe. On ajoute seulement le début.",
       mots:[["Directe puis polie","Ça prend combien de temps ? → Pourriez-vous me dire combien de temps ça prend ?"],["Avec « à quelle heure »","Il part à quelle heure ? → Je voudrais savoir à quelle heure il part.",true],["Avec « où »","Le quai est où ? → Pourriez-vous me dire où est le quai ?"]],
       say:"Je voudrais savoir à quelle heure il part. Pourriez-vous me dire où est le quai ?",
       note:"L'ordre des mots se remet à l'endroit : « où est le quai » plutôt que « où le quai est-il ». La question polie n'est plus une question, c'est une phrase ordinaire."},

      {t:'ana', h:"« Est-ce que » devient « si »",
       p:"C'est le seul vrai changement, et c'est l'erreur la plus fréquente. Une question qui commence par « est-ce que » se transforme avec « si ».",
       mots:[["La transformation","Est-ce qu'il faut changer ? → Je voudrais savoir s'il faut changer."],["Devant « il », « si » devient « s' »","s'il faut · s'il y a · s'il est ouvert",true],["Devant les autres, il reste entier","si vous avez · si c'est possible · si le déjeuner est compris"]],
       say:"Je voudrais savoir s'il faut changer d'autocar. Savez-vous si le déjeuner est compris ?",
       note:"« Je voudrais savoir est-ce qu'il faut changer » est la phrase à ne jamais dire. Le « est-ce que » et le « si » ne cohabitent pas."},

      {t:'labo', h:"La question directe, puis la question polie",
       p:"Choisissez une question et écoutez les deux versions à la file.",
       axes:[{id:'q', lbl:'Quelle question ?', opts:[
         ['a','La durée du trajet'],
         ['b','La correspondance'],
         ['c','Les bagages'],
         ['d','Le prix en basse saison'],
         ['e','Les quatre à la suite']]}],
       out:{
         a:{w:['un horaire'], say:"Ça prend combien de temps ? Pourriez-vous me dire combien de temps ça prend, selon l'horaire ?", n:"le mot de question reste en place"},
         b:{w:['une correspondance'], say:"Est-ce qu'il y a une correspondance ? Je voudrais savoir s'il y a une correspondance.", n:"est-ce que devient si"},
         c:{w:['la soute'], say:"Je peux apporter deux valises ? Est-ce que je pourrais apporter deux valises dans la soute ?", n:"une permission : est-ce que je pourrais"},
         d:{w:['la basse saison'], say:"C'est combien après le quinze septembre ? Savez-vous si le tarif de basse saison s'applique après le quinze septembre ?", n:"savez-vous si, pour un renseignement"},
         e:{w:['un horaire','une correspondance'], say:"Pourriez-vous me dire combien de temps ça prend ? Je voudrais savoir s'il y a une correspondance. Est-ce que je pourrais apporter deux valises ? Savez-vous si le gîte est ouvert ?", n:"les quatre formules, à la file"},
       },
       note:"Écoutez la version directe puis la version polie : c'est le contraste qui fait entendre ce que la formule ajoute."},

      {t:'ex', h:"À écouter et à répéter",
       p:"Six questions polies du module.",
       rows:[
         ["Pourriez-vous me dire combien de temps ça prend ?","le mot de question ne bouge pas"],
         ["Je voudrais savoir s'il faut changer d'autocar.","est-ce que devient si"],
         ["Est-ce que je pourrais changer la date du retour ?","une permission"],
         ["Savez-vous si le phare est encore ouvert à la fin septembre ?","si, devant une phrase complète"],
         ["J'aimerais savoir à quelle heure le premier autocar part.","à quelle heure, sans inversion"],
         ["Je me demandais s'il resterait de la place mercredi.","la formule la plus douce"],
       ]},

      {t:'piege', h:"Trois pièges de la question polie",
       rows:[
         ["garder « est-ce que » après « je voudrais savoir »","« Je voudrais savoir est-ce qu'il faut changer »",
          "« Est-ce que » devient <b>si</b>, sans exception. C'est la faute la plus fréquente et la plus facile à corriger : dès que la phrase commence par « je voudrais savoir » ou « savez-vous », cherchez le « si »."],
         ["mettre un point d'interrogation partout","« Je voudrais savoir à quelle heure il part ? »",
          "Si la phrase commence par « je », c'est une affirmation : point final. Le point d'interrogation ne revient que si la phrase commence par un verbe — « Pourriez-vous me dire… ? »"],
         ["inverser le sujet après le mot de question","« Pourriez-vous me dire où est-il, le quai ? »",
          "Après la formule polie, l'ordre redevient normal : sujet, puis verbe. « Pourriez-vous me dire où est le quai ? » ou « où le quai se trouve ». Pas d'inversion."],
       ]},

      {t:'check', h:"Est-ce que c'est clair maintenant ?",
       p:"Quatre questions rapides.",
       qs:[
         {q:"« Est-ce qu'il faut réserver ? » devient : « Je voudrais savoir… »", opts:["s'il faut réserver","est-ce qu'il faut réserver"], ok:0,
          fb:"« S'il faut réserver ». Le « est-ce que » devient « si »."},
         {q:"« Je voudrais savoir à quelle heure il part » se termine par…", opts:["un point","un point d'interrogation"], ok:0,
          fb:"Un point. La phrase commence par « je » : c'est une affirmation."},
         {q:"Pour demander une permission, on dit plutôt…", opts:["Est-ce que je pourrais…","Savez-vous si…"], ok:0,
          fb:"« Est-ce que je pourrais… ». « Savez-vous si » sert à demander un renseignement."},
         {q:"Le conditionnel « je voudrais » remplace…", opts:["« je veux »","« je peux »"], ok:0,
          fb:"« Je veux ». C'est ce seul changement de temps qui adoucit toute la demande."},
       ]},
    ]
  },

  // ════════════════════════════════════════════════════════════════════════
  t1dur: {
    eye:'Mini-leçon', tit:"En huit heures, pour une semaine",
    blocs:[
      {t:'texte', h:"Six mots, et chacun répond à une question différente",
       p:"En, pour, dans, à, vers, pendant : ce sont six petits mots, tous suivis d'un nombre, et l'on est tenté de les prendre l'un pour l'autre. Ils ne disent pourtant pas du tout la même chose. « Je pars en une semaine » et « je pars pour une semaine » sont deux phrases très différentes, et la première ne veut à peu près rien dire. Dans une conversation de voyage — un comptoir, un téléphone, un gîte — ces six mots reviennent toutes les trois phrases. Les mélanger fait perdre des places, des correspondances et des nuits d'hôtel.",
       note:"La bonne façon de les apprendre n'est pas de les réciter, c'est de retenir la question à laquelle chacun répond."},

      {t:'ana', h:"En + durée : combien de temps ça prend",
       p:"C'est le temps que la chose occupe, du début à la fin. Il répond à « combien de temps faut-il pour faire ça ? ».",
       mots:[["Le trajet","On fait Montréal-Rimouski en huit heures. · Il monte au belvédère en vingt minutes."],["Les petites choses","Elle a lu le dépliant en dix minutes. · On réserve en ligne en trois clics.",true],["La question à se poser","Combien de temps faut-il ?"]],
       say:"On fait Montréal-Rimouski en huit heures, avec les arrêts.",
       note:"« En » sert aussi à dire le moyen de transport — « en autocar », « en train », « en auto » — et c'est un autre emploi, à ne pas confondre avec celui-ci."},

      {t:'ana', h:"Pour + durée : combien de temps on va rester",
       p:"C'est le temps prévu du séjour, de l'absence, de l'engagement. Il regarde vers l'avant.",
       mots:[["Le séjour","Je pars pour une semaine. · Le gîte est réservé pour six nuits."],["L'absence du travail","Elle s'absente pour trois jours. · Il part pour le mois d'août.",true],["La question à se poser","Combien de temps ça va durer ?"]],
       say:"Je pars pour une semaine et je reviens le dimanche suivant.",
       note:"À l'oral, on l'omet souvent : « je pars une semaine » se dit très bien. Mais on ne le remplace jamais par « en »."},

      {t:'ana', h:"À et vers : l'heure exacte, l'heure approximative",
       p:"« À » donne l'heure écrite dans l'horaire. « Vers » donne l'heure approximative, celle qu'on annonce à quelqu'un qui vient nous attendre.",
       mots:[["L'horaire, précis","Le départ est à sept heures. · Le déjeuner est servi à huit heures."],["L'annonce, approximative","On arrive vers trois heures. · Je serai là vers midi.",true],["Ensemble","Le départ est à sept heures et on arrive vers quinze heures."]],
       say:"Le départ est à sept heures. On arrive vers trois heures de l'après-midi.",
       note:"Employer « à » pour une heure qu'on ne connaît pas exactement est une petite promesse qu'on ne tiendra pas. « Vers » n'engage à rien, et personne ne s'en formalise."},

      {t:'ana', h:"Dans et pendant : le délai et la durée",
       p:"« Dans » compte à partir de maintenant, vers l'avant. « Pendant » couvre une durée d'un bout à l'autre.",
       mots:[["Dans, le délai","L'autocar part dans vingt minutes. · Je pars dans trois semaines."],["Pendant, la durée complète","Elle a regardé dehors pendant tout le trajet. · Il a plu pendant deux jours.",true],["Ne pas confondre","Je pars dans une semaine — c'est le départ. · Je pars pour une semaine — c'est le séjour."]],
       say:"L'autocar part dans vingt minutes. Elle a regardé le fleuve pendant tout le trajet.",
       note:"« Je pars dans une semaine pour une semaine » est une phrase parfaitement correcte, et c'est le meilleur test : si les deux « une semaine » ne veulent pas dire la même chose, vous avez compris."},

      {t:'labo', h:"La même semaine, six façons d'en parler",
       p:"Choisissez un mot et écoutez la phrase qui va avec.",
       axes:[{id:'m', lbl:'Quel mot ?', opts:[
         ['a','en — le temps que ça prend'],
         ['b','pour — le temps qu\'on reste'],
         ['c','à — l\'heure exacte'],
         ['d','vers — l\'heure approximative'],
         ['e','dans et pendant']]}],
       out:{
         a:{w:['un horaire'], say:"On fait le trajet en huit heures. C'est ce que dit l'horaire.", n:"combien de temps faut-il ?"},
         b:{w:['un gîte'], say:"Je pars pour une semaine : le gîte est réservé pour six nuits.", n:"combien de temps ça va durer ?"},
         c:{w:['un aller-retour'], say:"Le départ est à sept heures et le retour est à six heures quarante-cinq.", n:"l'heure écrite dans l'horaire"},
         d:{w:['un vacancier'], say:"On arrive vers trois heures. Les autres vacanciers arrivent vers cinq heures.", n:"l'heure qu'on annonce"},
         e:{w:['le fleuve','un dépliant'], say:"L'autocar part dans vingt minutes. Elle a regardé le fleuve pendant tout le trajet, le dépliant sur les genoux.", n:"le délai, puis la durée complète"},
       },
       note:"Écoutez les cinq à la file, puis refaites chaque phrase avec vos propres chiffres : votre trajet, votre séjour, votre heure de départ."},

      {t:'ex', h:"À écouter et à répéter",
       p:"Six phrases du module.",
       rows:[
         ["On fait Montréal-Rimouski en huit heures.","le temps que ça prend"],
         ["Je pars pour une semaine.","le temps qu'on reste"],
         ["Le départ est à sept heures précises.","l'heure de l'horaire"],
         ["On arrive vers trois heures de l'après-midi.","l'heure approximative"],
         ["Nous partons dans vingt minutes.","le délai à partir de maintenant"],
         ["Il a plu pendant deux jours.","la durée complète"],
       ]},

      {t:'piege', h:"Trois pièges des mots du temps",
       rows:[
         ["confondre « en » et « pour »","« Je pars en une semaine » au lieu de « pour une semaine »",
          "« En une semaine » voudrait dire que le départ lui-même dure une semaine. Retenez la question : <b>en</b> répond à « combien de temps faut-il ? », <b>pour</b> répond à « combien de temps ça va durer ? »."],
         ["employer « à » pour une heure incertaine","« J'arrive à trois heures » quand on n'en sait rien",
          "« À » est l'heure de l'horaire, celle qu'on peut vérifier. Pour une heure qu'on estime, dites <b>vers</b>. Personne ne vous en voudra ; on vous en voudra d'être en retard sur une heure précise."],
         ["confondre « dans » et « pendant »","« J'ai lu pendant vingt minutes » pour dire « je pars dans vingt minutes »",
          "<b>Dans</b> regarde vers l'avant à partir de maintenant ; <b>pendant</b> couvre une durée qui est déjà en cours ou déjà passée. Les deux se disent avec le même chiffre, et c'est ce qui les rend traîtres."],
       ]},

      {t:'check', h:"Est-ce que c'est clair maintenant ?",
       p:"Quatre questions rapides.",
       qs:[
         {q:"« Le trajet se fait ___ huit heures. »", opts:["en","pour"], ok:0,
          fb:"En huit heures : c'est le temps que le trajet prend."},
         {q:"« Je pars ___ une semaine, je reviens dimanche. »", opts:["en","pour"], ok:1,
          fb:"Pour une semaine : c'est la durée du séjour."},
         {q:"Pour une heure que vous estimez, vous dites…", opts:["à trois heures","vers trois heures"], ok:1,
          fb:"Vers trois heures. « À » est réservé à l'heure exacte."},
         {q:"« L'autocar part ___ vingt minutes. »", opts:["dans","pendant"], ok:0,
          fb:"Dans vingt minutes : on compte à partir de maintenant."},
       ]},
    ]
  },

  // ════════════════════════════════════════════════════════════════════════
  t1bag: {
    eye:'Mini-leçon', tit:"Ce qu'on emporte dans un autocar",
    blocs:[
      {t:'texte', h:"Deux endroits, deux règles, et huit heures entre les deux",
       p:"Un autocar interurbain, ce n'est ni un autobus de ville ni un avion. Il y a deux endroits où mettre ses affaires : la soute, sous le plancher, et le siège, avec soi. Ce qui va dans la soute disparaît pour toute la durée du trajet — huit heures, dans le cas de Montréal-Rimouski, avec des arrêts où l'on descend sans pouvoir y accéder. Ce qui reste avec soi doit tenir dans un seul sac léger. Toute la difficulté du départ tient dans cette phrase : ce dont vous aurez besoin en route ne doit pas être sous le plancher.",
       note:"Cette règle vaut aussi pour le train et pour l'avion, avec d'autres chiffres. Ce qui s'apprend ici s'applique au prochain voyage, quel qu'il soit."},

      {t:'ana', h:"Ce que le transporteur accepte",
       p:"Chez le principal transporteur interurbain du Québec, chaque personne a droit à deux bagages en soute et à un bagage à main.",
       mots:[["En soute","deux bagages par personne · remis au chauffeur avant de monter"],["Avec soi","un seul bagage à main · cinq kilos au maximum · cent quinze centimètres au total",true],["Ce qui dépasse","le service de messagerie du transporteur, payé au poids"]],
       say:"Deux valises par personne sont acceptées dans la soute, plus un bagage à main.",
       note:"Les cent quinze centimètres sont la longueur, la largeur et la hauteur additionnées — c'est la mesure qu'emploient tous les transporteurs, et elle surprend toujours la première fois."},

      {t:'ana', h:"Ce qui ne descend jamais dans la soute",
       p:"Ce n'est pas une question de vol : c'est une question de huit heures sans accès.",
       mots:[["Les indispensables","les médicaments · les papiers d'identité · l'argent · le téléphone et son chargeur"],["Les fragiles et les chers","les lunettes · un ordinateur · un appareil photo",true],["Le confort du trajet","de l'eau · un lunch · un chandail · un livre ou le dépliant du parc"]],
       say:"Les médicaments, les papiers et le téléphone restent avec vous, à votre siège.",
       note:"Le chandail est le plus oublié des huit : la climatisation d'un autocar est réglée pour le chauffeur, pas pour vous, et le trajet se fait en septembre."},

      {t:'ana', h:"Comment ça se passe, au quai",
       p:"Vingt minutes avant le départ, avec ses valises, à côté de l'autocar. Le chauffeur ouvre la soute et charge lui-même.",
       mots:[["Avant de monter","on présente son billet · on remet ses valises au chauffeur"],["À l'arrivée","on attend à côté de l'autocar · le chauffeur ressort les valises une à une",true],["Aux arrêts en route","la soute reste fermée · on descend avec son seul bagage à main"]],
       say:"Présentez-vous vingt minutes avant : les valises se chargent avant le départ, pas après.",
       note:"Aux arrêts de vingt ou quarante minutes, on peut descendre manger. Le bagage à main descend avec vous : rien n'est surveillé à bord."},

      {t:'labo', h:"Chaque objet à sa place",
       p:"Choisissez un objet et écoutez où il va, et pourquoi.",
       axes:[{id:'o', lbl:'Quel objet ?', opts:[
         ['a','Une grosse valise'],
         ['b','Vos médicaments'],
         ['c','Une bicyclette'],
         ['d','Un sac à dos léger'],
         ['e','Les quatre à la suite']]}],
       out:{
         a:{w:['la soute'], say:"Une grosse valise va dans la soute. Vous la remettez au chauffeur avant de monter.", n:"deux par personne, sans supplément"},
         b:{w:['la soute','une correspondance'], say:"Vos médicaments restent avec vous. Huit heures de trajet et une correspondance, ce n'est pas le moment de les avoir sous le plancher.", n:"jamais en soute, jamais"},
         c:{w:['un aller-retour'], say:"Une bicyclette passe par le service de messagerie et se paie au poids. Elle n'entre pas dans le prix de l'aller-retour.", n:"il faut arriver plus tôt au comptoir"},
         d:{w:['un dépliant'], say:"Un sac à dos de trois kilos reste avec vous : un livre, un lunch, un chandail, le dépliant du parc.", n:"cinq kilos au maximum"},
         e:{w:['la soute','un dépliant'], say:"La valise dans la soute. Les médicaments avec vous. La bicyclette par messagerie. Le sac à dos et le dépliant, à votre siège.", n:"les quatre cas, à la file"},
       },
       note:"Faites la liste de ce que vous emporteriez, puis rangez chaque objet dans l'une des deux colonnes. C'est plus rapide que d'y penser au quai."},

      {t:'ex', h:"À écouter et à répéter",
       p:"Six phrases du comptoir.",
       rows:[
         ["Deux bagages en soute par personne, plus un bagage à main.","la règle, en une phrase"],
         ["Le bagage à main, c'est cinq kilos maximum.","la limite qu'on oublie"],
         ["Est-ce que je pourrais apporter une grosse valise ?","la question polie"],
         ["Ce qui dépasse passe par le service de messagerie.","ce qu'on répond au comptoir"],
         ["Présentez-vous vingt minutes avant le départ.","le conseil qui compte"],
         ["Les valises se chargent avant le départ, pas après.","et la raison du conseil"],
       ]},

      {t:'piege', h:"Trois pièges du départ",
       rows:[
         ["mettre ses médicaments dans la valise","huit heures sans y avoir accès, et une correspondance",
          "La soute ne s'ouvre pas en route, même aux arrêts. Médicaments, papiers, argent, téléphone, lunettes : dans le sac qui reste avec vous, toujours, quel que soit le moyen de transport."],
         ["arriver à la dernière minute avec deux valises","le chauffeur a fermé la soute, vous prenez le suivant",
          "Le chargement se fait avant le départ. Vingt minutes, c'est la marge que les préposés recommandent d'eux-mêmes, et elle suffit — sauf si vous avez un colis à faire peser au comptoir."],
         ["croire qu'un troisième sac passera","« c'est tout petit, ils ne diront rien »",
          "Parfois ils ne disent rien, souvent ils le disent. Un troisième bagage se règle au comptoir, au poids, et ça prend dix minutes qu'on n'a pas quand on arrive vingt minutes avant."],
       ]},

      {t:'check', h:"Est-ce que c'est clair maintenant ?",
       p:"Quatre questions rapides.",
       qs:[
         {q:"Combien de bagages en soute par personne ?", opts:["un","deux"], ok:1,
          fb:"Deux en soute, plus un bagage à main gardé avec soi."},
         {q:"Le bagage à main ne doit pas dépasser…", opts:["cinq kilos","quinze kilos"], ok:0,
          fb:"Cinq kilos, et cent quinze centimètres en dimensions additionnées."},
         {q:"Vos médicaments vont…", opts:["dans la soute","avec vous, à votre siège"], ok:1,
          fb:"Avec vous. La soute ne s'ouvre pas pendant le trajet."},
         {q:"On se présente au quai…", opts:["cinq minutes avant","vingt minutes avant"], ok:1,
          fb:"Vingt minutes avant : les valises se chargent avant le départ."},
       ]},
    ]
  },

  // ════════════════════════════════════════════════════════════════════════
  t2rel: {
    eye:'Mini-leçon', tit:"Qui, que, où, dont",
    blocs:[
      {t:'texte', h:"Ce qui sépare deux phrases d'un discours",
       p:"« Le sentier fait cinq kilomètres. Il longe le fleuve. » Deux phrases correctes, et pourtant ce n'est pas ainsi qu'on parle ni qu'on écrit. On dit : « Le sentier qui longe le fleuve fait cinq kilomètres. » Une seule phrase, et l'on sait au passage duquel des trois sentiers il s'agit. C'est précisément ce que le niveau 5 appelle un discours simple mais organisé : les idées ne sont plus posées l'une après l'autre, elles sont reliées. Les pronoms relatifs sont l'outil qui fait cette soudure, et il n'y en a que quatre à connaître.",
       note:"Vous les comprenez déjà tous les quatre en lisant. Ce qui se travaille ici, c'est de les employer soi-même — et surtout de choisir le bon sans hésiter trois secondes."},

      {t:'ana', h:"Qui : le sujet du verbe qui suit",
       p:"Après « qui », il y a tout de suite un verbe. C'est la chose nommée avant qui fait l'action.",
       mots:[["Dans le module","le sentier qui longe le fleuve · l'autocar qui part à sept heures"],["Au gîte","le gîte qui sert le déjeuner · la chambre qui donne sur la cour",true],["Le test","remplacez par « il » ou « elle » : il longe le fleuve, il part à sept heures"]],
       say:"L'autocar qui part à sept heures est le seul qui soit direct.",
       note:"« Qui » ne s'élide jamais : on écrit « qui il », jamais « qu'il », quand c'est le relatif sujet. Ce détail sépare les deux mots à l'écrit."},

      {t:'ana', h:"Que : le complément direct",
       p:"Après « que », il y a un sujet, puis le verbe. La chose nommée avant subit l'action.",
       mots:[["Dans le module","le sentier que nous avons fait hier · la chambre que j'ai réservée"],["Au comptoir","le billet que vous m'avez vendu · l'horaire que j'ai lu",true],["Le test","peut-on mettre « je », « nous », « vous » juste après ? Alors c'est que."]],
       say:"Le sentier que nous avons fait hier était plus long que prévu.",
       note:"Devant une voyelle, « que » devient « qu' » : le sentier qu'on a fait, la chambre qu'elle a réservée. « Qui » ne bouge pas."},

      {t:'ana', h:"Où : le lieu, et aussi le moment",
       p:"« Où » remplace un endroit, mais également un moment. C'est son deuxième emploi que l'on oublie.",
       mots:[["Le lieu","le village où l'autocar s'arrête · l'anse où les phoques se couchent"],["Le moment","le matin où il a plu · l'année où elle est arrivée · le jour où on est partis",true],["Ce qu'on ne dit pas","le jour que · le matin que · la fois que"]],
       say:"C'est l'anse où les phoques se couchent à marée basse.",
       note:"« Le jour que » s'entend beaucoup à l'oral, au Québec comme ailleurs. Ce n'est pas la forme écrite : dans un courriel, écrivez « le jour où »."},

      {t:'ana', h:"Dont : quand la suite commencerait par « de »",
       p:"On parle <b>de</b> quelque chose, on a besoin <b>de</b> quelque chose, on voit les îles <b>du</b> belvédère. Ce « de » devient « dont ».",
       mots:[["Dans le module","le gîte dont Camille m'a parlé · le parc dont je vous parlais"],["Ailleurs","les papiers dont j'ai besoin · la région dont elle vient",true],["Le test","refaites la phrase séparée : Camille m'a parlé de ce gîte."]],
       say:"Le gîte dont Camille m'a parlé n'a que quatre chambres.",
       note:"C'est le seul des quatre qu'on peut éviter en refaisant sa phrase autrement. Mais l'employer une fois dans un courriel change tout de suite le niveau de ce qu'on écrit."},

      {t:'labo', h:"Deux phrases, puis une seule",
       p:"Choisissez un relatif et écoutez les deux phrases séparées, puis la phrase soudée.",
       axes:[{id:'r', lbl:'Quel relatif ?', opts:[
         ['a','qui'],
         ['b','que'],
         ['c','où'],
         ['d','dont'],
         ['e','les quatre à la suite']]}],
       out:{
         a:{w:['un sentier'], say:"Le sentier fait cinq kilomètres. Il longe le fleuve. Le sentier qui longe le fleuve fait cinq kilomètres.", n:"après qui, un verbe tout de suite"},
         b:{w:['un gîte'], say:"La chambre donne sur la cour. Je l'ai réservée. La chambre que j'ai réservée donne sur la cour.", n:"après que, un sujet puis un verbe"},
         c:{w:['la marée'], say:"C'est une anse. Les phoques s'y couchent à marée basse. C'est l'anse où les phoques se couchent à marée basse.", n:"un lieu — ou un moment"},
         d:{w:['un belvédère'], say:"Le belvédère est à vingt minutes. On voit les îles de là-haut. Le belvédère dont on voit les îles est à vingt minutes.", n:"la suite commençait par de"},
         e:{w:['un sentier','un gîte'], say:"Le sentier qui longe le fleuve. La chambre que j'ai réservée. L'anse où les phoques se couchent. Le gîte dont on m'a parlé.", n:"les quatre, à la file"},
       },
       note:"Le contraste entre les deux phrases séparées et la phrase soudée est ce qui fait entendre à quoi sert le relatif. Écoutez-le deux fois."},

      {t:'ex', h:"À écouter et à répéter",
       p:"Six phrases du module.",
       rows:[
         ["Le sentier qui longe le fleuve fait cinq kilomètres.","qui, sujet"],
         ["La chambre que j'ai réservée donne sur la cour.","que, complément direct"],
         ["C'est l'anse où les phoques se couchent à marée basse.","où, un lieu"],
         ["Le matin où il a plu, elle a visité le phare.","où, un moment"],
         ["Le gîte dont Camille m'a parlé n'a que quatre chambres.","dont, parler de"],
         ["L'autocar qui part à sept heures est direct.","qui, encore"],
       ]},

      {t:'piege', h:"Trois pièges des relatifs",
       rows:[
         ["mettre « que » à la place de « qui »","« le sentier que longe le fleuve »",
          "Après le relatif, regardez ce qui suit : un verbe tout seul → <b>qui</b> ; un sujet puis un verbe → <b>que</b>. « Longe » est un verbe seul, donc « qui ». Le test tient en une seconde."],
         ["dire « le jour que »","« le jour que nous sommes partis »",
          "Pour un moment comme pour un lieu, c'est <b>où</b> : le jour où, le matin où, l'année où. Cette forme s'entend beaucoup à l'oral, mais elle ne s'écrit pas."],
         ["éviter « dont » en répétant « de »","« le gîte que Camille m'a parlé de »",
          "Le « de » ne se laisse pas en fin de phrase en français, comme il le ferait en anglais. Il remonte au début, sous la forme <b>dont</b> : « le gîte dont Camille m'a parlé »."],
       ]},

      {t:'check', h:"Est-ce que c'est clair maintenant ?",
       p:"Quatre questions rapides.",
       qs:[
         {q:"« Le sentier ___ longe le fleuve. »", opts:["qui","que"], ok:0,
          fb:"Qui : après lui vient un verbe seul, « longe »."},
         {q:"« La chambre ___ j'ai réservée. »", opts:["qui","que"], ok:1,
          fb:"Que : après lui vient un sujet, « je », puis le verbe."},
         {q:"« Le matin ___ il a plu. »", opts:["que","où"], ok:1,
          fb:"Où. Il remplace un moment comme il remplace un lieu."},
         {q:"« Le gîte ___ on m'a parlé. »", opts:["dont","que"], ok:0,
          fb:"Dont : on parle « de » quelque chose, et ce « de » devient « dont »."},
       ]},
    ]
  },

  // ════════════════════════════════════════════════════════════════════════
  t2comp: {
    eye:'Mini-leçon', tit:"Comparer, puis choisir",
    blocs:[
      {t:'texte', h:"Une comparaison sert à décider, sinon elle ne sert à rien",
       p:"Préparer un voyage, c'est comparer sans arrêt : l'autocar ou le train, le gîte ou le camping, le départ du matin ou celui de midi, la haute ou la basse saison. Le français a pour cela une mécanique très simple — trois mots devant l'adjectif, « que » derrière — et deux ou trois formes irrégulières qu'on entend tous les jours. Mais la mécanique n'est que la moitié du travail. Une comparaison qui n'aboutit à aucune décision laisse l'interlocuteur en plan : au niveau 5, on compare, puis on conclut, dans la même réplique.",
       note:"C'est cette conclusion qui fait la différence entre quelqu'un qui récite des phrases et quelqu'un qui tient une conversation."},

      {t:'ana', h:"Les trois degrés, devant un adjectif",
       p:"Plus, moins, aussi devant l'adjectif ; « que » derrière. C'est toute la construction.",
       mots:[["Plus … que","L'autocar est plus pratique que le train."],["Moins … que","Le camping est moins cher que le gîte.",true],["Aussi … que","Le sentier de la montagne est aussi beau que celui du bord de l'eau."]],
       say:"L'autocar est plus pratique que le train. Le camping est moins cher que le gîte.",
       note:"Le « que » ne se supprime jamais. « C'est plus cher » tout seul se dit, mais alors on ne compare plus rien : on constate."},

      {t:'ana', h:"Devant un nom, on ajoute « de »",
       p:"C'est le seul changement à retenir. Devant un adjectif : plus, moins, aussi. Devant un nom : plus de, moins de, autant de.",
       mots:[["Avec un nom","Il y a plus de vacanciers en juillet qu'en septembre."],["Autant de … que","Le gîte a autant de chambres que l'auberge.",true],["Ne pas mélanger","aussi + adjectif · autant de + nom"]],
       say:"Il y a plus de vacanciers en juillet qu'en septembre.",
       note:"« Aussi de » n'existe pas, et « autant beau » non plus. C'est la seule vraie difficulté de la leçon : la forme dépend de ce qui suit."},

      {t:'ana', h:"Meilleur et mieux : les deux irréguliers",
       p:"« Bon » devient « meilleur ». « Bien » devient « mieux ». On ne dit jamais « plus bon » ni « plus bien ».",
       mots:[["Meilleur, avec un nom derrière","Le déjeuner du gîte est meilleur que celui de l'hôtel."],["Mieux, avec un verbe devant","On dort mieux au gîte qu'en tente.",true],["Le test","bon décrit une chose ; bien décrit une action"]],
       say:"Le déjeuner du gîte est meilleur que celui de l'hôtel, et on y dort mieux.",
       note:"« Pire » existe aussi, pour « plus mauvais ». Mais « plus mauvais » se dit très bien, alors que « plus bon » ne se dit pas du tout."},

      {t:'ana', h:"Le superlatif : le plus, la plus, les plus",
       p:"On ajoute l'article devant. C'est ce qui distingue « plus beau » de « le plus beau ».",
       mots:[["Avec un adjectif","C'est le plus beau moment de l'année. · La plus longue étape est celle du matin."],["Avec un nom","C'est la région qui a le plus de parcs nationaux.",true],["L'irrégulier","le meilleur, jamais le plus bon"]],
       say:"Fin septembre, c'est le plus beau moment de l'année dans la région.",
       note:"Quand l'adjectif se place après le nom, l'article se répète : « le sentier le plus long », et non « le plus long sentier », qui se dit aussi mais sonne moins naturel ici."},

      {t:'labo', h:"Deux possibilités, une décision",
       p:"Choisissez une comparaison du module et écoutez-la en entier, conclusion comprise.",
       axes:[{id:'c', lbl:'Comparer quoi ?', opts:[
         ['a','L\'autocar ou le train'],
         ['b','Le gîte ou le camping'],
         ['c','La haute ou la basse saison'],
         ['d','Le départ du matin ou celui de midi'],
         ['e','Les quatre à la suite']]}],
       out:{
         a:{w:['un horaire'], say:"Le train est plus confortable que l'autocar, mais il passe trois fois par semaine et il arrive en pleine nuit. L'horaire décide : je prends l'autocar.", n:"deux différences, une conclusion"},
         b:{w:['un gîte','le prêt-à-camper'], say:"Le prêt-à-camper est moins cher que le gîte, mais il n'est pas chauffé et il fait cinq degrés la nuit. Je prends le gîte.", n:"le prix n'est pas le seul argument"},
         c:{w:['la basse saison','un vacancier'], say:"En basse saison, il y a moins de vacanciers et le gîte coûte vingt dollars de moins par nuit. Je pars après le quinze septembre.", n:"moins de + nom"},
         d:{w:['une correspondance'], say:"Le départ de midi trente est moins matinal, mais il a une correspondance et il arrive une heure plus tard. Je prends celui du matin.", n:"plus tard, moins matinal"},
         e:{w:['un gîte','la basse saison'], say:"Le train est plus confortable. Le camping est moins cher. La basse saison a moins de monde. Le départ du matin est plus direct.", n:"les quatre comparaisons, sans les conclusions"},
       },
       note:"Écoutez surtout la dernière phrase de chaque cas : c'est la décision, et c'est ce qui manque le plus souvent dans les productions d'élèves."},

      {t:'ex', h:"À écouter et à répéter",
       p:"Six phrases du module.",
       rows:[
         ["L'autocar est plus pratique que le train.","plus + adjectif"],
         ["Le camping est moins cher que le gîte.","moins + adjectif"],
         ["Le sentier de la montagne est aussi beau que l'autre.","aussi + adjectif"],
         ["Il y a plus de vacanciers en juillet qu'en septembre.","plus de + nom"],
         ["Le déjeuner du gîte est meilleur que celui de l'hôtel.","l'irrégulier de bon"],
         ["C'est le plus beau moment de l'année.","le superlatif"],
       ]},

      {t:'piege', h:"Trois pièges de la comparaison",
       rows:[
         ["dire « plus bon »","« le déjeuner est plus bon qu'à l'hôtel »",
          "« Bon » n'a pas de comparatif régulier : il devient <b>meilleur</b>. Et « bien » devient <b>mieux</b>. Ce sont les deux seuls irréguliers à retenir, et ce sont ceux qu'on emploie le plus souvent."],
         ["oublier le « de » devant un nom","« il y a plus vacanciers en juillet »",
          "Devant un nom, il faut <b>plus de</b>, <b>moins de</b>, <b>autant de</b>. Devant un adjectif, pas de « de ». Regardez ce qui suit avant de choisir la forme."],
         ["comparer sans conclure","« Le train est plus confortable, l'autocar est moins cher. » Et alors ?",
          "Une comparaison sans décision oblige l'autre à demander « donc tu prends quoi ? ». Ajoutez la conclusion dans la même réplique : « … donc je prends l'autocar ». C'est ce que le niveau 5 attend."],
       ]},

      {t:'check', h:"Est-ce que c'est clair maintenant ?",
       p:"Quatre questions rapides.",
       qs:[
         {q:"« Il y a ___ vacanciers en juillet. »", opts:["plus de","plus"], ok:0,
          fb:"Plus de : « vacanciers » est un nom."},
         {q:"Le comparatif de « bon » est…", opts:["plus bon","meilleur"], ok:1,
          fb:"Meilleur. Et celui de « bien » est « mieux »."},
         {q:"« Le sentier est ___ beau que l'autre. » (égalité)", opts:["aussi","autant"], ok:0,
          fb:"Aussi : devant un adjectif. « Autant de » se met devant un nom."},
         {q:"Une comparaison, au niveau 5, se termine par…", opts:["une décision","une autre comparaison"], ok:0,
          fb:"Une décision. Sinon l'autre doit vous demander ce que vous choisissez."},
       ]},
    ]
  },

  // ════════════════════════════════════════════════════════════════════════
  t3reg: {
    eye:'Mini-leçon', tit:"Tu, vous et les salutations d'usage",
    blocs:[
      {t:'texte', h:"Ce qui se joue dans les dix premières secondes",
       p:"Vous arrivez dans un village où personne ne vous connaît. L'hôtesse du gîte vous parle de la pluie comme à une amie, l'homme sur le sentier vous dit bonjour sans vous avoir jamais vu, et le préposé du parc vous appelle par votre prénom. Le Québec est chaleureux et il est direct, et cela crée un malentendu très courant : la chaleur n'est pas une invitation à tutoyer. On reste au « vous » avec les inconnus, les gens de service et les personnes plus âgées, aussi longtemps qu'on ne vous a pas proposé autre chose — et c'est la personne d'ici, ou la plus âgée, qui le propose.",
       note:"Se tromper de ce côté-là ne se corrige jamais à voix haute : personne ne vous dira « vous m'avez tutoyé ». On le sent seulement à la conversation qui raccourcit."},

      {t:'ana', h:"Qui l'on vouvoie, et jusqu'à quand",
       p:"La règle est simple à énoncer, et elle ne connaît que peu d'exceptions en voyage.",
       mots:[["On vouvoie","un inconnu · une personne de service · quelqu'un de plus âgé · quelqu'un qui vous vouvoie"],["On tutoie","un collègue de son âge · un ami · un enfant · quelqu'un qui vous a proposé le tu",true],["On attend","« On peut se tutoyer, si vous voulez. » — c'est l'autre qui l'offre"]],
       say:"Bonjour madame. Oui, très bon voyage, merci.",
       note:"Une exception qui surprend : dans beaucoup de commerces et de restaurants, le personnel jeune tutoie spontanément les clients. Cela ne vous oblige à rien — vous pouvez rester au « vous » sans que ce soit froid."},

      {t:'ana', h:"Les formules d'arrivée, à retenir en bloc",
       p:"Elles ne se construisent pas mot à mot. On les apprend telles quelles et on les emploie telles quelles.",
       mots:[["À l'arrivée","Bienvenue ! · Vous avez fait bon voyage ? · Vous venez de loin ?"],["Pour ouvrir une conversation","Belle journée, hein ? · Il fait beau aujourd'hui ! · C'est votre première fois par ici ?",true],["Pour répondre et relancer","Oui, très bon, merci. Et vous, vous êtes de la région ?"]],
       say:"Belle journée, hein ? C'est votre première fois par ici ?",
       note:"Le « hein ? » à la fin d'une phrase n'est pas une faute : c'est la façon la plus courante d'inviter l'autre à répondre. « Belle journée, hein ? » attend un « oui, magnifique », pas un silence."},

      {t:'ana', h:"Les formules de départ, tout aussi obligatoires",
       p:"Ne pas les rendre laisse une impression de froideur que l'on ne voulait pas donner. Elles coûtent trois secondes.",
       mots:[["Quand on part en voyage","Bon voyage ! · Bonne route ! · Faites attention à vous !"],["Quand on quitte quelqu'un sur place","Bon séjour ! · Bonne fin de journée ! · Bonne continuation !",true],["Quand on reçoit","Bienvenue chez nous ! · Revenez nous voir !"]],
       say:"Bon séjour, madame. Et bienvenue chez nous.",
       note:"« Bienvenue » a deux sens au Québec : c'est l'accueil, mais c'est aussi la réponse à « merci ». « Merci beaucoup. — Bienvenue ! » veut dire « de rien »."},

      {t:'ana', h:"Jaser : le mot qui dit ce qu'on fait vraiment",
       p:"Au Québec, on ne bavarde pas et on ne discute pas : on jase. Jaser, c'est parler pour le plaisir, sans but, avec quelqu'un qu'on ne reverra peut-être jamais.",
       mots:[["Comment ça s'emploie","On a jasé une demi-heure. · Viens jaser deux minutes. · On jasait de la pluie."],["Ce que ça n'est pas","ce n'est pas commérer · ce n'est pas se plaindre · ce n'est pas discuter d'affaires",true],["Ce que ça ouvre","un conseil sur un sentier · une histoire du village · une invitation à revenir"]],
       say:"Ils ont jasé une demi-heure sur le quai, sans se connaître.",
       note:"Employez-le. C'est un mot parfaitement correct, chaleureux, et il vous fera passer tout de suite pour quelqu'un qui écoute la langue d'ici plutôt que celle des manuels."},

      {t:'labo', h:"La même rencontre, du début à la fin",
       p:"Choisissez un moment de la rencontre et écoutez ce qui se dit.",
       axes:[{id:'m', lbl:'Quel moment ?', opts:[
         ['a','L\'arrivée au gîte'],
         ['b','La rencontre sur le sentier'],
         ['c','La question qu\'on vous pose'],
         ['d','Le conseil qu\'on vous donne'],
         ['e','Le départ']]}],
       out:{
         a:{w:['un gîte'], say:"Bienvenue ! Vous avez fait bon voyage ? — Bonjour madame. Oui, très bon : huit heures, mais je n'ai pas vu le temps passer. Le gîte est encore plus joli que sur les photos.", n:"on répond, puis on ajoute quelque chose"},
         b:{w:['jaser'], say:"Bonjour ! Belle journée, hein ? — Oui, magnifique. Je n'avais jamais vu le fleuve comme ça. On a jasé dix minutes.", n:"une phrase sur le temps ouvre tout"},
         c:{w:['un vacancier'], say:"Vous n'êtes pas du coin, vous non plus ? — J'arrive de Montréal, c'est ma première fois dans la région. Et vous ? — Nous, on est des vacanciers de Sherbrooke.", n:"on répond et on retourne la question"},
         d:{w:['un belvédère','un attrait'], say:"Montez au belvédère avant de repartir. C'est ce qu'on vient chercher ici. — J'y vais cet après-midi. Merci du conseil !", n:"un conseil se prend au sérieux et se remercie"},
         e:{w:['un phare'], say:"Bon séjour, madame ! Et bienvenue chez nous. — Merci beaucoup. J'irai voir le phare demain, comme vous avez dit.", n:"la formule d'usage se rend toujours"},
       },
       note:"Écoutez la rencontre entière une fois, puis reprenez chaque réplique de l'élève à voix haute. Ce sont cinq phrases, et elles ouvrent une région."},

      {t:'ex', h:"À écouter et à répéter",
       p:"Six phrases de la rencontre.",
       rows:[
         ["Bonjour madame. Oui, très bon voyage, merci.","on répond vraiment à la question"],
         ["Belle journée, hein ? On a été chanceux avec le temps.","la phrase qui ouvre"],
         ["C'est ma première fois dans la région. Et vous ?","on retourne la question"],
         ["Merci du conseil ! J'y vais cet après-midi.","on prend le conseil au sérieux"],
         ["Bon séjour, madame. Bienvenue chez nous.","les deux formules de départ"],
         ["Merci beaucoup. — Bienvenue !","bienvenue veut aussi dire de rien"],
       ]},

      {t:'piege', h:"Trois pièges de la conversation en région",
       rows:[
         ["tutoyer parce que l'autre est chaleureux","« Salut ! Tu me donnes ma clé ? » à l'hôtesse du gîte",
          "La chaleur n'est pas une permission. On reste au « vous » avec les gens de service et les inconnus jusqu'à ce qu'on vous propose autre chose. Accepter est alors très simple : « Avec plaisir. »"],
         ["comparer en défaveur de l'endroit","« C'est bien petit, votre village, comparé à Montréal. »",
          "C'est ressenti comme un jugement, même dit gentiment. Retournez la phrase : « C'est tellement tranquille ici, ça change de Montréal. » Même observation, tout autre effet."],
         ["répondre « oui » à une question ouverte","« Vous avez fait bon voyage ? — Oui. »",
          "Ces questions-là attendent trois ou quatre mots de plus : la durée, le moyen de transport, une chose remarquée. Un « oui » sec ferme la conversation, et c'est presque toujours involontaire."],
       ]},

      {t:'check', h:"Est-ce que c'est clair maintenant ?",
       p:"Quatre questions rapides.",
       qs:[
         {q:"L'hôtesse du gîte vous parle très chaleureusement. Vous…", opts:["passez au tu","restez au vous"], ok:1,
          fb:"Vous restez au « vous ». C'est elle qui proposera le tutoiement, si elle le veut."},
         {q:"« Merci beaucoup. — Bienvenue ! » veut dire…", opts:["de rien","entrez"], ok:0,
          fb:"De rien. « Bienvenue » a les deux sens au Québec."},
         {q:"« Jaser » veut dire…", opts:["se plaindre","parler pour le plaisir"], ok:1,
          fb:"Parler pour le plaisir, sans but précis. C'est un mot chaleureux."},
         {q:"À « Vous avez fait bon voyage ? », on répond…", opts:["oui","oui, plus deux ou trois mots"], ok:1,
          fb:"Oui, plus quelque chose : la durée, le moyen, une chose remarquée."},
       ]},
    ]
  },

  // ════════════════════════════════════════════════════════════════════════
  t3ger: {
    eye:'Mini-leçon', tit:"Le gérondif : en marchant, en passant",
    blocs:[
      {t:'texte', h:"Trois mots qui remplacent une phrase entière",
       p:"« Si vous passez par le petit chemin derrière l'église, vous couperez dix minutes. » Neuf mots avant d'arriver à l'information. La même chose avec un gérondif : « En passant par le petit chemin, vous coupez dix minutes. » C'est plus court, c'est plus clair, et surtout c'est ainsi qu'on vous parlera en région : les indications de chemin, les conseils, les explications de raccourci passent presque toutes par cette tournure. La comprendre est indispensable ; l'employer soi-même fait passer d'un français d'élève à un français de tous les jours.",
       note:"Le gérondif est aussi la marque du niveau 5 dans le programme : le savoir dit « employer des participes présents avec en pour marquer la simultanéité ou la manière »."},

      {t:'ana', h:"Comment il se forme : une seule recette",
       p:"On prend le verbe à « nous » au présent, on enlève -ons, on ajoute -ant, et on met « en » devant.",
       mots:[["La recette","nous marchons → en marchant · nous prenons → en prenant · nous partons → en partant"],["Sur des verbes du module","nous réservons → en réservant · nous montons → en montant · nous attendons → en attendant",true],["Les trois exceptions","être → en étant · avoir → en ayant · savoir → en sachant"]],
       say:"En marchant, comptez quarante minutes. En passant par le petit chemin, vous coupez dix minutes.",
       note:"La recette marche même sur les verbes irréguliers : nous faisons → en faisant, nous allons → en allant, nous venons → en venant. Il n'y a vraiment que trois exceptions."},

      {t:'ana', h:"Le chemin qu'on prend pour y arriver",
       p:"C'est l'emploi le plus utile du module. Le gérondif répond à « comment ? ».",
       mots:[["Un chemin","En passant par le chemin de l'église, vous coupez dix minutes."],["Une économie","En réservant en basse saison, on paie vingt dollars de moins par nuit.",true],["Un conseil","En partant tôt le matin, vous éviterez le monde sur le sentier."]],
       say:"En réservant après le quinze septembre, je paie le tarif de basse saison.",
       note:"Ce gérondif-là se place presque toujours en tête de phrase, suivi d'une virgule. C'est la position qui met le moyen en avant."},

      {t:'ana', h:"La simultanéité : deux choses en même temps",
       p:"Les deux actions se passent au même moment, et c'est la même personne qui fait les deux.",
       mots:[["Pendant le trajet","Elle a regardé le fleuve en voyageant. · Il a lu le dépliant en attendant l'autocar."],["Sur place","On jase en marchant. · Il a pris des photos en montant au belvédère.",true],["La règle qui ne se contourne pas","le sujet du gérondif est celui de la phrase"]],
       say:"Il a lu le dépliant en attendant l'autocar.",
       note:"Ce gérondif-là se place plutôt après le verbe. « En attendant l'autocar, il a lu le dépliant » se dit aussi, et met l'attente en avant."},

      {t:'ana', h:"Le sujet est toujours celui de la phrase",
       p:"C'est la seule erreur qui rend une phrase impossible à comprendre, et elle est fréquente.",
       mots:[["Ce qui ne se dit pas","En montant au belvédère, les îles sont apparues."],["Ce qui se dit","En montant au belvédère, nous avons vu les îles.",true],["Le test","qui monte ? Ce doit être le sujet de la phrase principale."]],
       say:"En montant au belvédère, nous avons vu les îles et l'autre rive.",
       note:"Le test tient en une question : qui fait l'action du gérondif ? Si ce n'est pas le sujet de la phrase, il faut refaire la phrase autrement."},

      {t:'labo', h:"La phrase longue, puis la phrase courte",
       p:"Choisissez un cas et écoutez la version longue, puis la version au gérondif.",
       axes:[{id:'g', lbl:'Quel cas ?', opts:[
         ['a','Le raccourci'],
         ['b','L\'économie'],
         ['c','Pendant le trajet'],
         ['d','Sur le sentier'],
         ['e','Deux gérondifs à la file']]}],
       out:{
         a:{w:['un sentier'], say:"Si vous passez par le chemin de l'église, vous couperez dix minutes. En passant par le chemin de l'église, vous coupez dix minutes et le sentier est plus joli.", n:"le moyen, en tête de phrase"},
         b:{w:['la basse saison','un gîte'], say:"Si vous réservez après le quinze septembre, le gîte coûte moins cher. En réservant en basse saison, on paie vingt dollars de moins par nuit.", n:"le gérondif remplace un si"},
         c:{w:['le fleuve','un dépliant'], say:"Elle regardait le fleuve et elle voyageait. Elle a regardé le fleuve en voyageant, le dépliant sur les genoux.", n:"deux actions au même moment"},
         d:{w:['un belvédère'], say:"Nous sommes montés au belvédère et nous avons vu les îles. En montant au belvédère, nous avons vu les îles.", n:"la même personne pour les deux verbes"},
         e:{w:['un gîte','un sentier'], say:"En sortant du gîte et en tournant à droite après l'église, vous êtes au sentier en dix minutes.", n:"deux gérondifs, un chemin complet"},
       },
       note:"Le dernier cas est le modèle à réutiliser : deux gérondifs suffisent à expliquer n'importe quel chemin, et c'est ainsi qu'on vous les donnera."},

      {t:'ex', h:"À écouter et à répéter",
       p:"Six phrases du module.",
       rows:[
         ["En marchant, comptez quarante minutes.","le moyen, tout court"],
         ["En passant par le petit chemin, vous coupez dix minutes.","le raccourci"],
         ["En réservant en basse saison, on paie moins cher.","le gérondif à la place d'un si"],
         ["Elle a regardé le fleuve en voyageant.","deux actions en même temps"],
         ["Il a lu le dépliant en attendant l'autocar.","l'attente, occupée"],
         ["En sortant du gîte et en tournant à droite, vous y êtes.","deux gérondifs, un chemin"],
       ]},

      {t:'piege', h:"Trois pièges du gérondif",
       rows:[
         ["changer de sujet en cours de route","« En montant au belvédère, les îles sont apparues »",
          "Le sujet du gérondif doit être celui de la phrase. Ce ne sont pas les îles qui montent : dites « en montant au belvédère, nous avons vu les îles ». C'est la seule erreur qui rend la phrase incompréhensible."],
         ["oublier le « en »","« Marchant, comptez quarante minutes »",
          "Le participe présent sans « en » existe, mais il ne dit ni le moyen ni la simultanéité, et il appartient à l'écrit soigné. Dans une conversation, le <b>en</b> est obligatoire."],
         ["former le gérondif sur l'infinitif","« en prendant » au lieu de « en prenant »",
          "La recette part du verbe à <b>nous</b>, jamais de l'infinitif : nous prenons → en prenant, nous venons → en venant, nous faisons → en faisant. Un instant pour dire le « nous » dans sa tête, et la forme sort juste."],
       ]},

      {t:'check', h:"Est-ce que c'est clair maintenant ?",
       p:"Quatre questions rapides.",
       qs:[
         {q:"Le gérondif se forme à partir du verbe à…", opts:["l'infinitif","nous, au présent"], ok:1,
          fb:"À partir de « nous » au présent : nous prenons → en prenant."},
         {q:"« En montant au belvédère, ___ »", opts:["les îles sont apparues","nous avons vu les îles"], ok:1,
          fb:"« Nous avons vu les îles » : c'est nous qui montons."},
         {q:"Combien d'exceptions à la recette ?", opts:["trois","une dizaine"], ok:0,
          fb:"Trois : être, avoir, savoir."},
         {q:"« En réservant en basse saison, on paie moins cher » dit…", opts:["le moyen","le moment"], ok:0,
          fb:"Le moyen : c'est la réponse à « comment paie-t-on moins cher ? »."},
       ]},
    ]
  },

  // ════════════════════════════════════════════════════════════════════════
  t3pc: {
    eye:'Mini-leçon', tit:"Raconter : le passé composé et l'imparfait",
    blocs:[
      {t:'texte', h:"L'un fait avancer le récit, l'autre plante le décor",
       p:"On rentre au gîte, on vous demande comment s'est passée la journée, et il faut raconter. C'est là que les deux temps du passé se séparent, et la règle n'est pas une affaire de durée : elle est une affaire de rôle. Le passé composé raconte ce qui s'est passé — les actions, l'une après l'autre, qui font avancer l'histoire. L'imparfait décrit ce qu'il y avait autour — le temps qu'il faisait, le paysage, l'ambiance, ce que l'on ressentait. Un récit fait uniquement de passé composé est une liste. Un récit fait uniquement d'imparfait est une carte postale. Il en faut les deux.",
       note:"Le test qui marche presque toujours : si l'on peut demander « et après ? », c'est du passé composé. Si l'on peut demander « c'était comment ? », c'est de l'imparfait."},

      {t:'ana', h:"Le passé composé : ce qui s'est passé",
       p:"Une action, un moment, et le récit avance d'un pas. C'est le temps des verbes d'action.",
       mots:[["Le départ","J'ai pris l'autocar de sept heures. · Nous sommes partis vers neuf heures."],["Sur place","Elle a visité le phare. · Nous sommes montés au belvédère. · J'ai vu trois phoques.",true],["Le test","peut-on demander « et après ? » ? Alors c'est le passé composé."]],
       say:"Lundi matin, j'ai pris l'autocar de sept heures.",
       note:"Une action qui a duré longtemps reste au passé composé si elle est terminée et située : « j'ai marché pendant trois heures » est un événement, pas un décor."},

      {t:'ana', h:"L'imparfait : ce qu'il y avait autour",
       p:"Le temps qu'il faisait, le paysage, les gens, l'ambiance. Rien n'avance : c'est le décor.",
       mots:[["Le temps qu'il faisait","Il pleuvait. · Il faisait frais. · Le fleuve était gris."],["Le décor","Il n'y avait personne sur le sentier. · La marée descendait. · Les phoques dormaient.",true],["Ce qu'on ressentait","J'étais fatiguée mais contente. · J'avais froid aux mains."]],
       say:"Il faisait frais et il n'y avait personne sur le sentier.",
       note:"« Il y avait », « c'était », « il faisait », « j'étais » : quatre formes qui ouvrent presque tous les décors. Apprenez-les comme des blocs, elles reviennent sans arrêt."},

      {t:'ana', h:"Les deux ensemble, dans la même phrase",
       p:"C'est la construction la plus utile de toutes : l'imparfait pose la situation, le passé composé y fait tomber l'événement.",
       mots:[["Avec « pendant que »","J'ai visité le phare pendant qu'il pleuvait."],["Avec « quand »","Quand nous sommes arrivés, la marée descendait.",true],["Sans mot de liaison","Il faisait déjà noir ; nous sommes rentrés à pied."]],
       say:"J'ai visité le phare pendant qu'il pleuvait. Quand nous sommes arrivés, la marée descendait.",
       note:"Regardez lequel des deux verbes est interrompu par l'autre : celui qui était déjà en cours va à l'imparfait, celui qui survient va au passé composé."},

      {t:'ana', h:"L'habitude va à l'imparfait",
       p:"Ce qui se répétait pendant le séjour se raconte à l'imparfait, même si le séjour est bel et bien fini.",
       mots:[["L'habitude du séjour","Tous les matins, je déjeunais à sept heures et je partais marcher."],["Les marqueurs qui l'annoncent","tous les jours · chaque matin · d'habitude · le soir",true],["Le contraste","Tous les matins je marchais, mais le jeudi j'ai pris l'autobus."]],
       say:"Tous les matins, je déjeunais à sept heures et je partais marcher.",
       note:"C'est le point qui surprend le plus : « le séjour est fini, donc tout devrait être au passé composé » — non. Une habitude est un décor, quel que soit son âge."},

      {t:'ana', h:"Être ou avoir : le piège de l'auxiliaire",
       p:"Une petite famille de verbes se conjugue avec « être », et alors le participe s'accorde avec le sujet. Tous les autres prennent « avoir ».",
       mots:[["Les verbes avec être","aller · venir · partir · arriver · monter · descendre · rester · entrer · sortir · tomber"],["L'accord qui suit","je suis allée · nous sommes montés · elle est restée · ils sont partis",true],["Tous les autres","j'ai pris · j'ai vu · j'ai marché · j'ai visité — le participe ne bouge pas"]],
       say:"Je suis allée au parc. Nous sommes montés au belvédère. J'ai visité le phare.",
       note:"Attention : monter, descendre et sortir prennent « avoir » quand ils ont un complément direct — « j'ai monté ma valise », « j'ai sorti le dépliant ». C'est le seul cas qui bascule."},

      {t:'labo', h:"Le décor, l'action, et les deux ensemble",
       p:"Choisissez un moment de la journée et écoutez comment il se raconte.",
       axes:[{id:'r', lbl:'Quel moment ?', opts:[
         ['a','Le décor du matin'],
         ['b','Les actions de la journée'],
         ['c','Les deux dans la même phrase'],
         ['d','L\'habitude du séjour'],
         ['e','Le récit complet']]}],
       out:{
         a:{w:['un sentier'], say:"Ce matin, il faisait frais, le fleuve était gris et il n'y avait personne sur le sentier.", n:"imparfait : rien n'avance, tout est autour"},
         b:{w:['un phare','un belvédère'], say:"Je suis partie vers neuf heures, j'ai marché jusqu'à l'anse, j'ai visité le phare et je suis montée au belvédère.", n:"passé composé : quatre pas dans le récit"},
         c:{w:['la marée'], say:"Quand je suis arrivée à l'anse, la marée descendait et trois phoques dormaient sur les roches.", n:"l'action tombe dans le décor"},
         d:{w:['un gîte'], say:"Tous les matins, je déjeunais à sept heures au gîte et je partais marcher avant huit heures.", n:"une habitude, donc l'imparfait"},
         e:{w:['un vacancier','un belvédère'], say:"Ce matin il faisait frais. Je suis partie vers neuf heures. Il n'y avait aucun vacancier sur le sentier. J'ai vu trois phoques. Du belvédère, on voyait les îles. C'était la plus belle journée depuis mon arrivée.", n:"le décor et les actions, en alternance"},
       },
       note:"Écoutez le récit complet en dernier : c'est le modèle de ce que vous aurez à produire, et l'alternance des deux temps s'y entend très nettement."},

      {t:'ex', h:"À écouter et à répéter",
       p:"Six phrases du récit.",
       rows:[
         ["Lundi matin, j'ai pris l'autocar de sept heures.","une action, le récit avance"],
         ["Pendant tout le trajet, il faisait soleil.","un décor, rien n'avance"],
         ["Quand nous sommes arrivés, la marée descendait.","l'action tombe dans le décor"],
         ["J'ai visité le phare pendant qu'il pleuvait.","les deux dans la même phrase"],
         ["Tous les matins, je déjeunais à sept heures.","une habitude du séjour"],
         ["Le dernier jour, nous sommes montés au belvédère.","être, avec accord"],
       ]},

      {t:'piege', h:"Trois pièges du récit au passé",
       rows:[
         ["choisir selon la durée","« j'ai marché trois heures » mis à l'imparfait parce que c'est long",
          "La durée n'entre pas en jeu. Ce qui compte, c'est le rôle : une marche terminée et située est un événement, donc du passé composé, même si elle a duré toute la journée."],
         ["oublier l'accord avec « être »","« je suis allé » écrit par une femme, « nous sommes monté »",
          "Avec l'auxiliaire <b>être</b>, le participe s'accorde avec le sujet : je suis allée, nous sommes montés, elles sont restées. C'est visible à l'écrit, et parfois audible : « allée » et « allé » se disent pareil, mais « monté » et « montés » aussi — c'est donc surtout une question d'écrit."],
         ["tout mettre au passé composé","« Il a fait frais, il n'y a pas eu personne, la marée est descendue »",
          "C'est correct grammaticalement et c'est illisible comme récit : rien ne distingue plus le décor des événements. Posez d'abord une phrase d'imparfait, puis enchaînez vos actions."],
       ]},

      {t:'check', h:"Est-ce que c'est clair maintenant ?",
       p:"Quatre questions rapides.",
       qs:[
         {q:"« Quand nous sommes arrivés, la marée ___ »", opts:["descendait","est descendue"], ok:0,
          fb:"Descendait : c'est le décor, déjà en cours quand nous arrivons."},
         {q:"« Tous les matins, je ___ à sept heures. »", opts:["ai déjeuné","déjeunais"], ok:1,
          fb:"Déjeunais : une habitude va à l'imparfait, même terminée."},
         {q:"« Nous ___ au belvédère. »", opts:["avons monté","sommes montés"], ok:1,
          fb:"Sommes montés : « monter » sans complément direct prend « être », et le participe s'accorde."},
         {q:"Le test du passé composé, c'est de pouvoir demander…", opts:["« et après ? »","« c'était comment ? »"], ok:0,
          fb:"« Et après ? ». « C'était comment ? » appelle l'imparfait."},
       ]},
    ]
  },

};
