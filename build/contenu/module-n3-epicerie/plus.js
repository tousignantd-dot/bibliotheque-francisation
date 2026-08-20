const PLUS = {
  prNombres: {
    eye:'Mini-leçon', tit:"Treize ou trente ?",
    blocs:[
      {t:'texte', h:"Deux nombres qui se ressemblent",
       p:"« Treize » et « trente » commencent pareil. Toute la différence est à la <b>fin</b> du mot : treize finit par le son <b>ze</b>, trente finit par le son <b>te</b>. Six paires de nombres se ressemblent ainsi, et ce sont justement celles qu'on entend le plus souvent à l'épicerie : un numéro d'allée, un prix, une quantité.",
       note:"Se tromper coûte cher ici : chercher dans l'allée trente quand on vous a dit treize, ou payer trente dollars en croyant en payer treize."},

      {t:'ana', h:"La fin en « ze » : de 13 à 16",
       p:"Le mot se termine par un son qui vibre.",
       mots:[['On écrit','trei{ze}'],['On entend','trè-ZE',true],['Aussi','quator{ze} · quin{ze} · sei{ze}']],
       say:"Allée treize, tout au fond.",
       note:"Ce sont les nombres de 13 à 16. Ils finissent tous par le même son, celui du <b>z</b> de « zéro »."},

      {t:'ana', h:"La fin en « te » : de 30 à 60",
       p:"Le mot se termine par un son sec, sans vibration.",
       mots:[['On écrit','tren{te}'],['On entend','tran-TE',true],['Aussi','quaran{te} · cinquan{te} · soixan{te}']],
       say:"Trente dollars, s'il vous plaît.",
       note:"Ce sont les dizaines. Elles finissent toutes par le son du <b>t</b>, comme dans « table »."},

      {t:'ana', h:"Et le début, alors ?",
       p:"Le début change aussi, mais moins fort.",
       mots:[['13','TREI-ze — comme « treillis »'],['30','TRAN-te — le son du « an »'],['Ce qui trompe','les deux commencent par « tr »',true]],
       say:"Treize, trente. Treize, trente.",
       note:"Beaucoup de gens écoutent le début et devinent. C'est la fin qu'il faut écouter : elle est plus courte, mais elle décide."},

      {t:'labo', h:"Écoutez les paires",
       p:"Choisissez une paire et écoutez la fin des deux mots.",
       axes:[{id:'p', lbl:'Quelle paire ?', opts:[
         ['a','13 / 30'],
         ['b','14 / 40'],
         ['c','15 / 50'],
         ['d','16 / 60'],
         ['e','dans une phrase']]}],
       out:{
         a:{w:['trei{ze} / tren{te}'], say:"Treize dollars, trente dollars.", n:'ze qui vibre, te qui claque'},
         b:{w:['quator{ze} / quaran{te}'], say:"Quatorze pommes, quarante pommes.", n:'la fin décide'},
         c:{w:['quin{ze} / cinquan{te}'], say:"Allée quinze, allée cinquante.", n:'le début change aussi ici'},
         d:{w:['sei{ze} / soixan{te}'], say:"Seize dollars, soixante dollars.", n:'la paire la plus coûteuse'},
         e:{w:['« Ça fait treize quinze. »'], say:"Ça fait treize dollars et quinze cents.", n:'un montant contient souvent deux de ces nombres'},
       },
       note:"Écoutez chaque paire deux fois : la première pour comprendre, la seconde en fermant les yeux."},

      {t:'ex', h:"À écouter et à répéter",
       p:"Six phrases de l'épicerie.",
       rows:[
         ["Allée treize, à côté des conserves.","13 — la fin vibre"],
         ["Trente dollars pour la semaine.","30 — la fin claque"],
         ["Quatorze pommes dans le sac.","14"],
         ["Quarante-deux dollars et quinze cents.","42 et 15"],
         ["Le spécial finit le quinze.","15 — une date"],
         ["Soixante millilitres, c'est très peu.","60"],
       ]},

      {t:'piege', h:"Trois pièges à connaître",
       rows:[
         ["deviner d'après le début","« tr… », donc treize ou trente ?",
          "Le début est identique. Si vous n'avez pas entendu la fin, vous n'avez pas entendu le nombre : demandez à faire répéter."],
         ["ne pas oser faire répéter","« Pardon, treize ou trente ? »",
          "Donner les deux possibilités est la façon la plus rapide : la personne répond en un mot, et personne n'est gêné."],
         ["confondre 60 et 70","soixante, soixante-dix",
          "Ici, 70 se dit « soixante-dix » : il commence comme 60. Écoutez s'il y a un deuxième mot après."],
       ]},

      {t:'check', h:"Est-ce que c'est clair maintenant ?",
       p:"Quatre questions rapides.",
       qs:[
         {q:"« Treize » finit par le son…", opts:["ze","te"], ok:0,
          fb:"Comme le z de « zéro »."},
         {q:"« Quarante » finit par le son…", opts:["ze","te"], ok:1,
          fb:"Comme le t de « table »."},
         {q:"Pour distinguer, il faut écouter…", opts:["le début","la fin"], ok:1,
          fb:"Le début est le même dans les deux."},
         {q:"Vous n'avez pas compris. Vous dites…", opts:["rien, vous devinez","« Pardon, treize ou trente ? »"], ok:1,
          fb:"Donner les deux possibilités règle la question en une seconde."},
       ]},
    ]
  },

  t1ou: {
    eye:'Mini-leçon', tit:"Dire où c'est",
    blocs:[
      {t:'texte', h:"Trois sortes de repères",
       p:"Quand on vous indique où se trouve un produit, la réponse contient presque toujours trois choses : un <b>numéro d'allée</b>, une <b>position dans le magasin</b> (au fond, près de l'entrée), et une <b>hauteur de tablette</b> (en haut, au milieu, en bas). Connaître les mots des trois, c'est comprendre n'importe quelle réponse.",
       note:"Les commis répondent vite, parce qu'ils répondent cent fois par jour. Ce n'est pas contre vous."},

      {t:'ana', h:"Le numéro d'allée",
       p:"C'est le repère le plus précis.",
       mots:[['On dit','{dans} l\'allée cinq'],['On voit','un grand chiffre suspendu',true],['Aussi','allée douze · allée quinze']],
       say:"L'huile est dans l'allée cinq.",
       note:"Le chiffre est écrit en grand au bout de la rangée, des deux côtés. On le voit de loin."},

      {t:'ana', h:"La position dans le magasin",
       p:"Pour se diriger quand on ne voit pas encore les numéros.",
       mots:[['Le plus loin','{au fond} du magasin'],['Le plus proche','{près de} l\'entrée'],['De l\'autre côté','{en face des} caisses',true]],
       say:"Les produits du monde sont tout au fond.",
       note:"« Au bout de l'allée » veut dire là où l'allée se termine — pas au fond du magasin."},

      {t:'ana', h:"La hauteur de la tablette",
       p:"Une fois dans la bonne allée, il reste à lever ou baisser les yeux.",
       mots:[['Il faut lever le bras','{en haut}'],['À hauteur des yeux','{au milieu}'],['Il faut se pencher','{en bas}',true]],
       say:"Les grands sacs sont sur la tablette du bas.",
       note:"Ce n'est pas un hasard : le format le plus vendu est au milieu, le plus lourd en bas, et le moins demandé en haut."},

      {t:'labo', h:"Construisez une réponse",
       p:"Choisissez un produit et une précision.",
       axes:[
         {id:'p', lbl:'Quel produit ?', opts:[['a','le riz'],['b','le lait'],['c','le savon'],['d','les pommes']]},
         {id:'q', lbl:'Quelle précision ?', opts:[['1','le numéro'],['2','la position'],['3','la hauteur']]}],
       out:{
         a1:{w:["Le riz est dans l'allée huit."], say:"Le riz est dans l'allée huit.", n:'le repère le plus précis'},
         a2:{w:["Le riz est au milieu du magasin, avec les pâtes."], say:"Le riz est au milieu du magasin, avec les pâtes.", n:'utile quand on ne voit pas les numéros'},
         a3:{w:["Les grands sacs de riz sont en bas."], say:"Les grands sacs de riz sont en bas.", n:'le lourd est toujours en bas'},
         b1:{w:["Le lait est dans l'allée un."], say:"Le lait est dans l'allée un.", n:'souvent la première ou la dernière'},
         b2:{w:["Le lait est au fond, contre le mur."], say:"Le lait est au fond, contre le mur.", n:'le frais est sur les murs'},
         b3:{w:["Le lait est en bas, dans le réfrigérateur."], say:"Le lait est en bas, dans le réfrigérateur.", n:'le froid descend : le lait est en bas'},
         c1:{w:["Le savon est dans l'allée dix."], say:"Le savon est dans l'allée dix.", n:'avec les produits d\'entretien'},
         c2:{w:["Le savon est près de la pharmacie."], say:"Le savon est près de la pharmacie.", n:'un repère qu\'on voit de loin'},
         c3:{w:["Le savon est au milieu, à hauteur des yeux."], say:"Le savon est au milieu, à hauteur des yeux.", n:'le format courant est au milieu'},
         d1:{w:["Les pommes sont à l'entrée, avant les allées."], say:"Les pommes sont à l'entrée, avant les allées.", n:'les fruits n\'ont pas de numéro'},
         d2:{w:["Les pommes sont près de l'entrée, à droite."], say:"Les pommes sont près de l'entrée, à droite.", n:'les fruits accueillent le client'},
         d3:{w:["Les pommes sont dans les grands bacs."], say:"Les pommes sont dans les grands bacs.", n:'ni tablette ni hauteur : un bac'},
       },
       note:"Douze réponses possibles, toutes correctes. C'est exactement ce qu'un commis vous dira."},

      {t:'ex', h:"À écouter et à répéter",
       p:"Six phrases entendues à l'épicerie.",
       rows:[
         ["C'est dans l'allée cinq.","le numéro"],
         ["Tout au fond, à gauche.","la position"],
         ["Sur la tablette du bas.","la hauteur"],
         ["À côté du vinaigre.","un produit voisin"],
         ["En face des caisses.","de l'autre côté"],
         ["Au bout de l'allée, à droite.","là où l'allée finit"],
       ]},

      {t:'piege', h:"Trois pièges à connaître",
       rows:[
         ["confondre « au fond » et « au bout »","le magasin, ou l'allée",
          "« Au fond » parle du magasin : le mur le plus loin de la porte. « Au bout de l'allée » parle d'une seule rangée."],
         ["partir sans le numéro","« C'est par là », et on cherche dix minutes",
          "Si on vous montre une direction sans donner de numéro, demandez : « C'est quelle allée ? » Le numéro est ce qui fait gagner du temps."],
         ["chercher à hauteur des yeux seulement","le grand format est en bas",
          "Si vous ne voyez pas ce que vous cherchez, baissez les yeux avant de conclure qu'il n'y en a plus."],
       ]},

      {t:'check', h:"Est-ce que c'est clair maintenant ?",
       p:"Quatre questions rapides.",
       qs:[
         {q:"« Au fond du magasin », c'est…", opts:["le mur le plus loin de la porte","la fin de l'allée"], ok:0,
          fb:"« Au bout de l'allée » parle de l'allée."},
         {q:"Les grands formats sont…", opts:["en haut","en bas"], ok:1,
          fb:"Ils sont lourds."},
         {q:"Le repère le plus précis est…", opts:["le numéro d'allée","« par là »"], ok:0,
          fb:"Le chiffre est écrit en grand au bout de la rangée."},
         {q:"Le lait, le pain et la viande sont…", opts:["au milieu du magasin","sur les murs"], ok:1,
          fb:"Le frais a besoin de réfrigérateurs, qui sont contre les murs."},
       ]},
    ]
  },

  t1aide: {
    eye:'Mini-leçon', tit:"Demander de l'aide",
    blocs:[
      {t:'texte', h:"Quatre secondes, trois phrases",
       p:"Demander de l'aide dans un magasin tient en trois phrases : une pour <b>attirer l'attention</b>, une pour <b>demander</b>, une pour <b>remercier</b>. Entre les deux premières, il y a souvent une quatrième : celle qui fait <b>répéter</b>. C'est la plus utile de toutes, et c'est celle qu'on ose le moins dire.",
       note:"Personne ne trouve étrange qu'on demande où est un produit. Les commis passent leur journée à répondre à cette question."},

      {t:'ana', h:"Attirer l'attention",
       p:"On ne commence jamais par la question.",
       mots:[['On dit','{Excusez-moi}'],['On attend','que la personne se tourne',true],['Puis','on pose la question']],
       say:"Excusez-moi, monsieur.",
       note:"Ajouter « monsieur » ou « madame » est fréquent et poli, mais pas obligatoire."},

      {t:'ana', h:"Demander : trois niveaux",
       p:"Du plus court au plus poli. Les trois sont acceptables.",
       mots:[['Court','{Où est} le riz ?'],['Simple','{Je cherche} le riz.'],['Poli','{Pourriez-vous m\'indiquer} le riz ?',true]],
       say:"Excusez-moi, je cherche le riz.",
       note:"« Je cherche » est le plus facile à dire et le plus employé. Commencez par celui-là."},

      {t:'ana', h:"Faire répéter",
       p:"Trois phrases à savoir par cœur.",
       mots:[['Le plus court','{Pardon ?}'],['Le plus clair','{Vous pouvez répéter ?}'],['Le plus utile','{Plus lentement}, s\'il vous plaît.',true]],
       say:"Pardon, vous pouvez répéter ?",
       note:"Une quatrième, encore meilleure : répéter en donnant les deux possibilités — « Allée cinq ou allée quinze ? »"},

      {t:'labo', h:"Une demande complète",
       p:"Choisissez un produit et un niveau de politesse.",
       axes:[
         {id:'p', lbl:'Quoi ?', opts:[['a','le riz'],['b','la farine de maïs'],['c','le savon à vaisselle']]},
         {id:'q', lbl:'Comment ?', opts:[['1','court'],['2','simple'],['3','poli']]}],
       out:{
         a1:{w:["Excusez-moi. Où est le riz ?"], say:"Excusez-moi. Où est le riz ?", n:'direct, et parfaitement acceptable'},
         a2:{w:["Excusez-moi, je cherche le riz."], say:"Excusez-moi, je cherche le riz.", n:'le plus employé'},
         a3:{w:["Excusez-moi, pourriez-vous m'indiquer le riz ?"], say:"Excusez-moi, pourriez-vous m'indiquer le riz ?", n:'plus long, plus poli'},
         b1:{w:["Excusez-moi. Où est la farine de maïs ?"], say:"Excusez-moi. Où est la farine de maïs ?", n:'nommez le produit précisément'},
         b2:{w:["Excusez-moi, je cherche de la farine de maïs."], say:"Excusez-moi, je cherche de la farine de maïs.", n:'« de la » : une quantité indéfinie'},
         b3:{w:["Excusez-moi, auriez-vous de la farine de maïs ?"], say:"Excusez-moi, auriez-vous de la farine de maïs ?", n:'demande si le magasin en vend'},
         c1:{w:["Excusez-moi. Où est le savon à vaisselle ?"], say:"Excusez-moi. Où est le savon à vaisselle ?", n:'précisez : il y a plusieurs savons'},
         c2:{w:["Excusez-moi, je cherche du savon à vaisselle."], say:"Excusez-moi, je cherche du savon à vaisselle.", n:'« du » devant un produit qu\'on ne compte pas'},
         c3:{w:["Excusez-moi, pourriez-vous m'indiquer les produits d'entretien ?"], say:"Excusez-moi, pourriez-vous m'indiquer les produits d'entretien ?", n:'demander la famille plutôt que l\'objet'},
       },
       note:"Les neuf phrases sont bonnes. Choisissez celle que vous direz sans hésiter — c'est la meilleure pour vous."},

      {t:'ex', h:"À écouter et à répéter",
       p:"Six phrases à savoir par cœur.",
       rows:[
         ["Excusez-moi, madame.","attirer l'attention"],
         ["Je cherche la farine de maïs.","demander"],
         ["Pardon ? Vous pouvez répéter ?","faire répéter"],
         ["Plus lentement, s'il vous plaît.","ralentir"],
         ["Allée cinq ou allée quinze ?","vérifier le chiffre"],
         ["Merci beaucoup. Bonne journée !","remercier"],
       ]},

      {t:'piege', h:"Trois pièges à connaître",
       rows:[
         ["dire « oui » sans avoir compris","et chercher vingt minutes",
          "Un « oui » poli quand on n'a pas compris coûte plus cher qu'un « pardon ? ». Personne ne juge la deuxième phrase."],
         ["commencer par la question","« Où est le riz ? » à quelqu'un de dos",
          "La personne n'a pas entendu le début. « Excusez-moi » sert à ce qu'elle se tourne avant que vous parliez."],
         ["s'excuser trop","« Je suis désolé de vous déranger, excusez-moi, pardon… »",
          "Un seul « excusez-moi » suffit. Répondre à une question fait partie du travail du commis."],
       ]},

      {t:'check', h:"Est-ce que c'est clair maintenant ?",
       p:"Quatre questions rapides.",
       qs:[
         {q:"On commence par…", opts:["la question","« Excusez-moi »"], ok:1,
          fb:"Pour que la personne se tourne."},
         {q:"« Je cherche le riz » est…", opts:["impoli","parfaitement correct"], ok:1,
          fb:"C'est même la formule la plus employée."},
         {q:"Vous n'avez pas compris. Le mieux est de…", opts:["dire oui","dire « pardon ? »"], ok:1,
          fb:"Tout le monde le dit, même les gens d'ici."},
         {q:"« Bienvenue », après un merci, veut dire…", opts:["de rien","entrez"], ok:0,
          fb:"C'est la réponse habituelle à « merci » au Québec."},
       ]},
    ]
  },

  t2quantite: {
    eye:'Mini-leçon', tit:"Les mots qui mesurent",
    blocs:[
      {t:'texte', h:"On n'achète pas « du riz »",
       p:"On achète <b>un sac</b> de riz, <b>un kilo</b> de pommes, <b>une bouteille</b> d'huile. En français, la quantité passe presque toujours par un mot qui dit <b>ce qui contient</b> ou <b>ce qui pèse</b>, suivi de « de ». C'est ce petit mot qui permet de commander sans montrer du doigt.",
       note:"Au Québec, deux systèmes cohabitent : la viande s'annonce souvent à la livre, et les fruits au kilo. Les deux sont normaux."},

      {t:'ana', h:"Ce qui contient",
       p:"Le contenant donne la quantité.",
       mots:[['On dit','un {paquet de} pâtes'],['Aussi','une {boîte de} conserve · un {sac de} riz'],['Et encore','une {bouteille d\'}huile · un {pot de} confiture',true]],
       say:"Un paquet de pâtes et une boîte de tomates.",
       note:"« Une douzaine d'œufs » est un cas à part : ce n'est pas le contenant, c'est le nombre — douze."},

      {t:'ana', h:"Ce qui pèse",
       p:"Deux unités, deux habitudes.",
       mots:[['Le plus courant ici','une {livre} — environ 450 grammes'],['Le système officiel','un {kilo} — 1000 grammes'],['Sur l\'affiche','3,99 $ / lb ou 8,80 $ / kg',true]],
       say:"Le poulet est à trois dollars la livre.",
       note:"Une livre vaut un peu moins d'un demi-kilo. Un prix au kilo semble donc deux fois plus élevé, pour la même viande."},

      {t:'ana', h:"Toujours « de »",
       p:"Le mot de quantité est suivi de « de », jamais d'un article.",
       mots:[['On dit','un kilo {de} pommes'],['Devant une voyelle','une bouteille {d\'}huile'],['On ne dit pas','un kilo des pommes',true]],
       say:"Un kilo de pommes et une bouteille d'huile.",
       note:"C'est une règle sans exception avec les mots de quantité : de, d', et rien d'autre."},

      {t:'labo', h:"Composez une commande",
       p:"Choisissez un produit et une quantité.",
       axes:[
         {id:'p', lbl:'Quel produit ?', opts:[['a','des pâtes'],['b','du poulet'],['c','des pommes'],['d','de l\'huile']]},
         {id:'q', lbl:'Quelle quantité ?', opts:[['1','un contenant'],['2','un poids'],['3','un nombre']]}],
       out:{
         a1:{w:["un paquet de pâtes"], say:"Un paquet de pâtes, s'il vous plaît.", n:'le contenant habituel'},
         a2:{w:["500 grammes de pâtes"], say:"Cinq cents grammes de pâtes.", n:'rare pour des pâtes, mais correct'},
         a3:{w:["deux paquets de pâtes"], say:"Deux paquets de pâtes, s'il vous plaît.", n:'le nombre se met devant'},
         b1:{w:["un paquet de poulet"], say:"Un paquet de poulet.", n:'la barquette du comptoir'},
         b2:{w:["une livre de poulet"], say:"Une livre de poulet, s'il vous plaît.", n:'la façon la plus courante ici'},
         b3:{w:["quatre morceaux de poulet"], say:"Quatre morceaux de poulet.", n:'au comptoir, on compte les morceaux'},
         c1:{w:["un sac de pommes"], say:"Un sac de pommes.", n:'le sac est déjà rempli et pesé'},
         c2:{w:["un kilo de pommes"], say:"Un kilo de pommes, s'il vous plaît.", n:'les fruits se vendent au kilo'},
         c3:{w:["six pommes"], say:"Six pommes, s'il vous plaît.", n:'sans mot de quantité : on compte'},
         d1:{w:["une bouteille d'huile"], say:"Une bouteille d'huile.", n:'« d\' » devant la voyelle'},
         d2:{w:["un litre d'huile"], say:"Un litre d'huile.", n:'ce qui se verse se mesure en litres'},
         d3:{w:["deux bouteilles d'huile"], say:"Deux bouteilles d'huile.", n:'le nombre devant le contenant'},
       },
       note:"Douze commandes, toutes correctes. Remarquez que « de » ne change jamais, sauf devant une voyelle."},

      {t:'ex', h:"À écouter et à répéter",
       p:"Six commandes.",
       rows:[
         ["Un paquet de pâtes, s'il vous plaît.","le contenant"],
         ["Deux boîtes de conserve de tomates.","le nombre devant"],
         ["Une livre de poulet.","le poids d'ici"],
         ["Un kilo de pommes.","le poids officiel"],
         ["Une bouteille d'huile.","d' devant la voyelle"],
         ["Une douzaine d'œufs.","douze"],
       ]},

      {t:'piege', h:"Trois pièges à connaître",
       rows:[
         ["oublier « de »","« un kilo pommes »",
          "Le mot de quantité appelle toujours « de » : un kilo <b>de</b> pommes, un paquet <b>de</b> pâtes."],
         ["mettre un article après « de »","« un kilo des pommes »",
          "« De » remplace l'article, il ne s'y ajoute pas. On dit un kilo de pommes, jamais un kilo des pommes."],
         ["comparer un prix à la livre et un prix au kilo","3,99 $/lb n'est pas moins cher que 6,50 $/kg",
          "Une livre pèse moins de la moitié d'un kilo. Pour comparer, il faut ramener les deux à la même unité."],
       ]},

      {t:'check', h:"Est-ce que c'est clair maintenant ?",
       p:"Quatre questions rapides.",
       qs:[
         {q:"Après un mot de quantité, on met…", opts:["de","du"], ok:0,
          fb:"Un kilo de pommes."},
         {q:"Devant une voyelle, « de » devient…", opts:["d'","de la"], ok:0,
          fb:"Une bouteille d'huile."},
         {q:"Une livre pèse…", opts:["un peu moins qu'un demi-kilo","plus qu'un kilo"], ok:0,
          fb:"Environ 450 grammes."},
         {q:"« Une douzaine d'œufs », c'est…", opts:["douze œufs","une boîte"], ok:0,
          fb:"C'est un nombre, pas un contenant."},
       ]},
    ]
  },

  t2danger: {
    eye:'Mini-leçon', tit:"Les dessins qui avertissent",
    blocs:[
      {t:'texte', h:"Quatre dessins, une seule règle",
       p:"Sur les produits d'entretien, un petit dessin dans un losange avertit du danger. Il y en a quatre à connaître, et ils veulent dire des choses très différentes : ça <b>tue</b> si on l'avale, ça <b>brûle</b> la peau, ça <b>prend feu</b>, ça <b>éclate</b>. Ces dessins sont les mêmes dans tout le Canada, quelle que soit la marque.",
       note:"Ils sont obligatoires. Un produit d'entretien sans aucun dessin est un produit qui ne présente aucun de ces quatre dangers."},

      {t:'ana', h:"Poison et corrosif",
       p:"Les deux qu'on rencontre le plus souvent sous l'évier.",
       mots:[['Tête de mort','{poison} — tue si on l\'avale'],['Main percée','{corrosif} — brûle la peau et les yeux'],['Ce qu\'il faut','des gants, et ranger en haut',true]],
       say:"Attention, ce produit est corrosif.",
       note:"« Corrosif » est le mot écrit sur la bouteille. Dans la vie, on dit plutôt « ça brûle »."},

      {t:'ana', h:"Inflammable et explosif",
       p:"Les deux qui craignent la chaleur.",
       mots:[['Flamme','{inflammable} — prend feu'],['Bombe qui éclate','{explosif} — le contenant peut éclater'],['Ce qu\'il faut','loin de la cuisinière, jamais dans l\'auto l\'été',true]],
       say:"Ce produit est inflammable : gardez-le loin du feu.",
       note:"Une bonbonne laissée dans une auto en juillet peut atteindre soixante degrés."},

      {t:'ana', h:"La règle qu'on oublie",
       p:"Elle ne tient à aucun dessin, et c'est la plus importante.",
       mots:[['On ne mélange','{jamais} deux produits'],['Le pire mélange','eau de Javel + ammoniac'],['Ce que ça fait','un gaz qui envoie à l\'hôpital',true]],
       say:"Ne mélangez jamais deux produits d'entretien.",
       note:"C'est écrit en toutes lettres sur la bouteille. C'est aussi ce que personne ne lit."},

      {t:'labo', h:"Que faire avec ce produit ?",
       p:"Choisissez un dessin et une situation.",
       axes:[
         {id:'p', lbl:'Quel dessin ?', opts:[['a','tête de mort'],['b','main percée'],['c','flamme'],['d','bombe']]},
         {id:'q', lbl:'Quelle question ?', opts:[['1','ça veut dire quoi ?'],['2','je fais quoi ?'],['3','je range où ?']]}],
       out:{
         a1:{w:["Poison : le produit tue si on l'avale."], say:"Poison : le produit tue si on l'avale.", n:'le plus grave des quatre'},
         a2:{w:["Je ne le transvide jamais dans une bouteille d'eau."], say:"Je ne le transvide jamais dans une bouteille d'eau.", n:'chaque année, des enfants en boivent'},
         a3:{w:["En haut, hors de portée des enfants."], say:"En haut, hors de portée des enfants.", n:'jamais sous l\'évier'},
         b1:{w:["Corrosif : ça brûle la peau et les yeux."], say:"Corrosif : ça brûle la peau et les yeux.", n:'four, drain, cuvette'},
         b2:{w:["Je mets des gants et j'ouvre la fenêtre."], say:"Je mets des gants et j'ouvre la fenêtre.", n:'et on ne se frotte pas le visage'},
         b3:{w:["Debout, bien fermé, dans une armoire."], say:"Debout, bien fermé, dans une armoire.", n:'couché, il peut couler'},
         c1:{w:["Inflammable : le produit prend feu."], say:"Inflammable : le produit prend feu.", n:'alcool, décapant, aérosol'},
         c2:{w:["Je l'utilise loin de la cuisinière."], say:"Je l'utilise loin de la cuisinière.", n:'et loin d\'une cigarette'},
         c3:{w:["Au frais, jamais près d'une source de chaleur."], say:"Au frais, jamais près d'une source de chaleur.", n:'ni près du chauffe-eau'},
         d1:{w:["Explosif : le contenant peut éclater."], say:"Explosif : le contenant peut éclater.", n:'les bonbonnes sous pression'},
         d2:{w:["Je ne le perce pas et je ne le jette pas au feu."], say:"Je ne le perce pas et je ne le jette pas au feu.", n:'même vide'},
         d3:{w:["Jamais dans une auto l'été."], say:"Jamais dans une auto l'été.", n:'il y fait plus de soixante degrés'},
       },
       note:"Douze réponses. Les trois questions — quoi, comment, où — sont celles qu'il faut se poser devant n'importe quelle bouteille."},

      {t:'ex', h:"À écouter et à répéter",
       p:"Six phrases de sécurité.",
       rows:[
         ["Ce produit est un poison.","tête de mort"],
         ["Ce produit brûle la peau.","main percée"],
         ["Mettez des gants.","la précaution de base"],
         ["Ouvrez la fenêtre.","aérer la pièce"],
         ["Ne mélangez jamais deux produits.","la règle qu'on oublie"],
         ["Rangez-le hors de portée des enfants.","en haut, pas sous l'évier"],
       ]},

      {t:'piege', h:"Trois pièges à connaître",
       rows:[
         ["transvider dans une bouteille d'eau","pour économiser de la place",
          "C'est la cause d'empoisonnements chaque année. Un produit d'entretien reste dans son contenant d'origine, avec son étiquette."],
         ["mélanger deux nettoyants","« pour que ce soit plus fort »",
          "Ce n'est pas plus fort : c'est dangereux. L'eau de Javel et l'ammoniac produisent ensemble un gaz qui attaque les poumons."],
         ["croire que « naturel » veut dire « sans danger »","le vinaigre aussi peut brûler les yeux",
          "Un produit naturel peut être corrosif. Regardez le dessin, pas le mot sur l'étiquette."],
       ]},

      {t:'check', h:"Est-ce que c'est clair maintenant ?",
       p:"Quatre questions rapides.",
       qs:[
         {q:"Une tête de mort veut dire…", opts:["poison","inflammable"], ok:0,
          fb:"Le produit tue si on l'avale."},
         {q:"Une main percée veut dire…", opts:["ça brûle la peau","ça explose"], ok:0,
          fb:"Corrosif : gants obligatoires."},
         {q:"Mélanger deux produits, c'est…", opts:["plus efficace","dangereux"], ok:1,
          fb:"Le mélange peut produire un gaz toxique."},
         {q:"Un produit d'entretien se range…", opts:["sous l'évier","hors de portée des enfants"], ok:1,
          fb:"En haut, dans une armoire fermée si possible."},
       ]},
    ]
  },

  t3facture: {
    eye:'Mini-leçon', tit:"Lire une facture",
    blocs:[
      {t:'texte', h:"Un papier qui se lit en dix secondes",
       p:"La facture d'épicerie a toujours la même forme : une <b>ligne par produit</b>, puis un <b>sous-total</b>, les <b>taxes</b>, et le <b>total</b>. Ce qui compte n'est pas de tout lire : c'est de vérifier deux choses — que les spéciaux sont bien passés, et qu'aucun produit n'a été compté deux fois.",
       note:"Une erreur de caisse n'est presque jamais volontaire : c'est un prix qui n'a pas été changé dans le système."},

      {t:'ana', h:"Une ligne par produit",
       p:"Le nom est écrit court, parfois coupé.",
       mots:[['Sur l\'affiche','BANANES BIOLOGIQUES'],['Sur la facture','BAN BIO',true],['À droite','le prix payé pour cette ligne']],
       say:"Vérifiez chaque ligne de votre facture.",
       note:"Si un produit apparaît deux fois et que vous n'en avez acheté qu'un, c'est une double lecture du code-barres."},

      {t:'ana', h:"Sous-total, taxes, total",
       p:"Trois chiffres en bas, dans cet ordre.",
       mots:[['Sous-total','avant les taxes'],['TPS et TVQ','les deux taxes'],['Total','ce qu\'on paie vraiment',true]],
       say:"Le total, c'est quarante-deux dollars et quinze.",
       note:"Sur les aliments de base — pain, lait, légumes, viande, œufs — il n'y a pas de taxes. Elles s'ajoutent sur les produits d'entretien, les boissons et les plats préparés."},

      {t:'ana', h:"La ligne des économies",
       p:"Souvent en bas, souvent ignorée.",
       mots:[['Elle dit','« Vous avez économisé 8,40 $ »'],['Elle sert à','vérifier que les spéciaux sont passés',true],['Si elle est à zéro','aucun spécial n\'a été appliqué']],
       say:"Vous avez économisé huit dollars et quarante.",
       note:"C'est la façon la plus rapide de contrôler : un coup d'œil à ce chiffre avant de quitter le magasin."},

      {t:'labo', h:"Que dit cette ligne ?",
       p:"Choisissez une ligne de facture.",
       axes:[{id:'p', lbl:'Quelle ligne ?', opts:[
         ['a','POULET 3 LB · 15,00'],
         ['b','SOUS-TOTAL · 38,40'],
         ['c','TPS · 0,45'],
         ['d','TOTAL · 42,15'],
         ['e','ÉCONOMIES · 8,40']]}],
       out:{
         a:{w:['trois livres de poulet, quinze dollars'], say:"Trois livres de poulet, quinze dollars.", n:'cinq dollars la livre — à comparer avec la circulaire'},
         b:{w:['le total avant les taxes'], say:"Sous-total : trente-huit dollars et quarante.", n:'c\'est ce qui correspond aux prix des allées'},
         c:{w:['la taxe fédérale'], say:"TPS : quarante-cinq cents.", n:'faible : la plupart des aliments ne sont pas taxés'},
         d:{w:['ce qu\'on paie vraiment'], say:"Total : quarante-deux dollars et quinze.", n:'le seul chiffre que la machine demande d\'approuver'},
         e:{w:['la somme des spéciaux'], say:"Économies : huit dollars et quarante.", n:'à zéro, aucun spécial n\'est passé'},
       },
       note:"Cinq lignes, et vous avez lu toute la facture. Le reste, ce sont les produits."},

      {t:'ex', h:"À écouter et à répéter",
       p:"Six phrases de la caisse.",
       rows:[
         ["Ça fait quarante-deux quinze.","le montant"],
         ["Vous voulez la facture ?","à garder"],
         ["Il y a une erreur sur ma facture.","signaler"],
         ["Le prix ne correspond pas au spécial.","la phrase juste"],
         ["J'ai la photo de la circulaire.","la preuve"],
         ["Je vous rembourse la différence.","la solution"],
       ]},

      {t:'piege', h:"Trois pièges à connaître",
       rows:[
         ["partir sans regarder","l'erreur se découvre à la maison",
          "Une fois dehors, il faut revenir. Dix secondes à la caisse valent un deuxième déplacement."],
         ["croire qu'on s'est trompé soi-même","« j'ai dû mal lire la circulaire »",
          "Les erreurs de prix existent et les magasins le savent : un spécial qui n'est pas entré dans le système le vendredi matin arrive souvent."],
         ["jeter la facture tout de suite","surtout pour les produits d'entretien",
          "Un produit qui ne fonctionne pas, un contenant percé : sans facture, aucun échange. Elle sert au-delà du prix."],
       ]},

      {t:'check', h:"Est-ce que c'est clair maintenant ?",
       p:"Quatre questions rapides.",
       qs:[
         {q:"Le sous-total, c'est…", opts:["avant les taxes","après les taxes"], ok:0,
          fb:"Le total vient après."},
         {q:"Sur le pain et le lait, il y a…", opts:["des taxes","pas de taxes"], ok:1,
          fb:"Les aliments de base ne sont pas taxés."},
         {q:"La ligne « économies » sert à…", opts:["vérifier les spéciaux","calculer les taxes"], ok:0,
          fb:"Si elle est à zéro, aucun spécial n'est passé."},
         {q:"Il y a une erreur. Vous dites…", opts:["« Vous vous êtes trompée ! »","« Le prix ne correspond pas au spécial. »"], ok:1,
          fb:"On décrit le fait, on n'accuse pas la personne."},
       ]},
    ]
  },
};
