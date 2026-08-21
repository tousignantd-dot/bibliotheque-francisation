const PLUS = {
  prPhon: {
    eye:'Mini-leçon', tit:"Le « on » de livraison et le « an » de grand",
    blocs:[
      {t:'texte', h:"Deux sons qui passent par le nez",
       p:"Le français a des voyelles <b>nasales</b> : l'air sort par le nez en même temps que par la bouche. Deux d'entre elles reviennent sans arrêt dans un magasin : le <b>on</b> de « livrais<b>on</b> » et le <b>an</b> de « gr<b>an</b>d ». Beaucoup de langues n'en ont aucune, et l'oreille les mélange au début.",
       note:"Ce n'est pas un détail : « cent » et « son » ne veulent pas dire la même chose, et « comptant » contient les deux sons, l'un après l'autre."},

      {t:'ana', h:"Le son « on » — la bouche petite et ronde",
       p:"C'est le son de « livraison », « rond », « onze ».",
       mots:[['On écrit','livrais{on}'],['Les lèvres','en rond, bien avancées',true],['Aussi écrit','om devant b et p : c{om}ptant']],
       say:"La livraison arrive onze novembre.",
       note:"Truc : dis « o » comme dans « pot », puis bouche le nez avec deux doigts. Si le son change, c'est que l'air passait par le nez : c'était le bon."},

      {t:'ana', h:"Le son « an » — la bouche grande ouverte",
       p:"C'est le son de « grand », « cent », « dimanche ».",
       mots:[['On écrit','gr{an}d'],['Aussi écrit','en : c{en}t · v{en}deur',true],['Aussi écrit','am, em devant b et p : ch{am}bre']],
       say:"Cent dollars, dimanche, chez le vendeur.",
       note:"La bouche est plus ouverte que pour « on », et les lèvres ne sont pas rondes du tout."},

      {t:'ana', h:"Quatre écritures, deux sons",
       p:"Ce sont les lettres qui trompent, pas les sons.",
       mots:[['Le son on','on, om'],['Le son an','an, am, en, em',true],['Le piège','« en » se dit « an » : v{en}deur']],
       say:"Le vendeur vend cent laveuses.",
       note:"Retiens la paire de mots « vendeur / livraison » : elle contient les deux sons et les deux écritures les plus fréquentes."},

      {t:'labo', h:"Écoute les paires",
       p:"Choisis une paire et écoute la différence.",
       axes:[{id:'p', lbl:'Quelle paire ?', opts:[
         ['a','son / cent'],
         ['b','rond / rang'],
         ['c','onze / anse'],
         ['d','livraison / vendeur'],
         ['e','dans une phrase']]}],
       out:{
         a:{w:['s{on} / c{en}t'], say:"Son, cent.", n:'on puis an'},
         b:{w:['r{on}d / r{an}g'], say:"Rond, rang.", n:'les lèvres changent'},
         c:{w:['{on}ze / {an}se'], say:"Onze, anse.", n:'le son est au début'},
         d:{w:['livrais{on} / v{en}deur'], say:"La livraison, le vendeur.", n:'les deux mots du module'},
         e:{w:['« Cent dollars pour la livraison. »'], say:"Cent dollars pour la livraison.", n:'les deux sons dans la même phrase'},
       },
       note:"Écoute chaque paire deux fois : la première pour comprendre, la seconde en fermant les yeux."},

      {t:'ex', h:"À écouter et à répéter",
       p:"Six phrases du magasin.",
       rows:[
         ["La livraison coûte soixante dollars.","on trois fois"],
         ["Le vendeur est dans le grand rayon.","an quatre fois"],
         ["Onze appareils sont en spécial.","on puis an"],
         ["Ce modèle est trop grand pour ma chambre.","an trois fois"],
         ["Je paie comptant, pas par carte.","les deux sons dans un seul mot"],
         ["Mon ordinateur a quatre ans.","on puis an"],
       ]},

      {t:'piege', h:"Trois pièges à connaître",
       rows:[
         ["prononcer la lettre n","dire « li-vrai-son-ne »",
          "Dans « livraison », le n ne se prononce pas tout seul : il rend la voyelle nasale, puis il disparaît. La bouche ne se ferme pas à la fin."],
         ["croire que « en » se dit « en »","le mot « vendeur »",
          "Les lettres e et n ensemble se disent « an ». C'est l'écriture la plus fréquente du son, et la plus trompeuse."],
         ["mélanger cent et son","« cent dollars » et « son prix »",
          "Là, la confusion change le sens de la phrase. Ouvre bien la bouche pour « cent », arrondis-la pour « son »."],
       ]},

      {t:'check', h:"Est-ce que c'est clair maintenant ?",
       p:"Quatre questions rapides.",
       qs:[
         {q:"« Livraison » a le son…", opts:["on","an"], ok:0,
          fb:"Les lèvres sont rondes et avancées."},
         {q:"« Vendeur » a le son…", opts:["on","an"], ok:1,
          fb:"Les lettres e et n ensemble se disent « an »."},
         {q:"Dans ces sons, l'air passe…", opts:["par la bouche seulement","par le nez aussi"], ok:1,
          fb:"C'est pour ça qu'on les appelle des voyelles nasales."},
         {q:"Dans « comptant », il y a…", opts:["un seul son nasal","deux sons nasaux"], ok:1,
          fb:"« com » se dit « on », « tant » se dit « an »."},
       ]},

      {t:'revoir', h:"À retenir",
       p:"Deux mots repères, et rien d'autre : <b>livraison</b> pour le son « on », <b>grand</b> pour le son « an ». Quand tu hésites devant un mot nouveau, dis-le à côté de l'un des deux et écoute lequel se ressemble."},
    ]
  },

  prComposes: {
    eye:'Mini-leçon', tit:'Une laveuse, un réfrigérateur, des micro-ondes',
    blocs:[
      {t:'texte', h:"Le nom de l'appareil se retient avec son déterminant",
       p:"En français, chaque appareil est masculin ou féminin, et rien dans l'objet ne le dit. Une laveuse et un réfrigérateur sont deux grosses boîtes blanches ; l'une est féminine, l'autre masculin. Il n'y a donc rien à comprendre : il y a quelque chose à <b>ranger</b>. On apprend toujours « <b>une</b> laveuse », jamais « laveuse » tout seul.",
       note:"Écris-le ainsi dans ton carnet dès la première fois. Deux lettres de plus, et la question est réglée pour toujours."},

      {t:'ana', h:"Les appareils féminins",
       p:"Trois mots à retenir avec « une ».",
       mots:[['On dit','{une} laveuse'],['Aussi','une sécheuse · une cuisinière'],['Et','une affichette · une circulaire',true]],
       say:"Une laveuse, une sécheuse, une cuisinière.",
       note:"Ils finissent tous par un e qu'on n'entend presque pas. C'est un indice, pas une règle."},

      {t:'ana', h:"Les appareils masculins",
       p:"La famille des mots en -teur.",
       mots:[['On dit','{un} réfrigérateur'],['Aussi','un aspirateur · un ordinateur',true],['Et','un rayon · un modèle · un bon']],
       say:"Un réfrigérateur, un aspirateur, un ordinateur.",
       note:"Trois appareils, trois mots en -teur, tous masculins. C'est la petite famille la plus facile du module."},

      {t:'ana', h:"Les mots à trait d'union",
       p:"Deux mots collés qui n'en font qu'un.",
       mots:[['On dit','{un} micro-ondes'],['Aussi','un lave-vaisselle · un grille-pain'],['Au pluriel','{des} micro-ondes — rien ne change',true]],
       say:"Un micro-ondes, des micro-ondes, un lave-vaisselle.",
       note:"Le premier morceau dit ce que l'appareil fait — laver, griller — et le second sur quoi il le fait."},

      {t:'labo', h:"Un, une ou des ?",
       p:"Choisis un appareil et vois son déterminant.",
       axes:[
         {id:'v', lbl:'Quel appareil ?', opts:[['a','laveuse'],['b','réfrigérateur'],['c','micro-ondes'],['d','ordinateur portable']]},
         {id:'q', lbl:'Quelle phrase ?', opts:[['1','je cherche…'],['2','le magasin vend…']]}],
       out:{
         a1:{w:["Je cherche une laveuse."], say:"Je cherche une laveuse.", n:'féminin'},
         a2:{w:["Le magasin vend des laveuses."], say:"Le magasin vend des laveuses.", n:'pluriel : un s de plus'},
         b1:{w:["Je cherche un réfrigérateur."], say:"Je cherche un réfrigérateur.", n:'masculin, en -teur'},
         b2:{w:["Le magasin vend des réfrigérateurs."], say:"Le magasin vend des réfrigérateurs.", n:'pluriel régulier'},
         c1:{w:["Je cherche un micro-ondes."], say:"Je cherche un micro-ondes.", n:'le s est déjà là au singulier'},
         c2:{w:["Le magasin vend des micro-ondes."], say:"Le magasin vend des micro-ondes.", n:'seul le déterminant change'},
         d1:{w:["Je cherche un ordinateur portable."], say:"Je cherche un ordinateur portable.", n:"l'adjectif vient après"},
         d2:{w:["Le magasin vend des ordinateurs portables."], say:"Le magasin vend des ordinateurs portables.", n:'les deux mots prennent un s'},
       },
       note:"Huit phrases, toutes correctes, toutes utilisables telles quelles au magasin."},

      {t:'ex', h:"À écouter et à répéter",
       p:"Six phrases pour ranger les mots.",
       rows:[
         ["Une laveuse et une sécheuse.","deux féminins"],
         ["Un réfrigérateur et une cuisinière.","un de chaque"],
         ["Un aspirateur, un ordinateur.","la famille des -teur"],
         ["Des micro-ondes, un micro-ondes.","le mot ne change pas"],
         ["Un ordinateur portable pour l'école.","deux mots, un appareil"],
         ["Des laveuses blanches, en spécial.","le pluriel s'entend au déterminant"],
       ]},

      {t:'piege', h:"Trois pièges à connaître",
       rows:[
         ["mettre un s à micro-ondes","« des micro-ondeses »",
          "Le s est déjà dans le mot au singulier. Au pluriel, rien ne bouge : seul « un » devient « des »."],
         ["oublier le trait d'union","« micro ondes », « lave vaisselle »",
          "Sans trait d'union, ce sont deux mots séparés et le sens se perd. C'est court à écrire et ça compte à l'examen."],
         ["se fier au son pour le genre","laveuse et réfrigérateur",
          "Rien dans le son ne dit le genre. Le e final aide un peu, mais « un modèle » finit aussi par un e et reste masculin."],
       ]},

      {t:'check', h:"Est-ce que c'est clair maintenant ?",
       p:"Quatre questions rapides.",
       qs:[
         {q:"On dit…", opts:["un laveuse","une laveuse"], ok:1,
          fb:"Laveuse, sécheuse, cuisinière : trois féminins."},
         {q:"On dit…", opts:["un aspirateur","une aspirateur"], ok:0,
          fb:"Les mots en -teur du module sont masculins."},
         {q:"Le pluriel de « un micro-ondes » est…", opts:["des micro-ondes","des micro-ondeses"], ok:0,
          fb:"Le mot ne change pas ; seul le déterminant change."},
         {q:"Pour apprendre un appareil nouveau, on note…", opts:["le mot seul","le mot avec un ou une"], ok:1,
          fb:"Toujours avec son déterminant, dès la première fois."},
       ]},
    ]
  },

  t1prix: {
    eye:'Mini-leçon', tit:'Lire un prix de trois ou quatre chiffres',
    blocs:[
      {t:'texte', h:"Un appareil, ce n'est pas un pain",
       p:"À l'épicerie, les prix ont un ou deux chiffres. Un appareil, lui, coûte des centaines de dollars — parfois plus de mille. Les nombres deviennent longs, et le magasin les dit vite. Savoir les <b>lire</b> dans la circulaire, c'est déjà la moitié du travail : le papier ne parle pas vite, lui.",
       note:"Dans la circulaire, le prix est toujours le plus gros chiffre de l'encadré. Cherche la taille avant de chercher le sens."},

      {t:'ana', h:"Les centaines",
       p:"On dit le chiffre, puis « cent », puis le reste.",
       mots:[['On écrit','849 $'],['On dit','huit {cent} quarante-neuf dollars',true],['Attention','200 $ se dit « deux cents » avec un s']],
       say:"Huit cent quarante-neuf dollars.",
       note:"Le mot « cent » prend un s quand rien ne le suit : deux cents, trois cents. Avec un nombre après, pas de s : deux cent vingt."},

      {t:'ana', h:"Soixante-dix, quatre-vingts, quatre-vingt-dix",
       p:"Les trois nombres qui font peur, et qui reviennent tout le temps.",
       mots:[['70','soixante-dix'],['80','{quatre-vingts}',true],['90','quatre-vingt-dix']],
       say:"Soixante-dix, quatre-vingts, quatre-vingt-dix.",
       note:"En français du Québec, on ne dit pas « septante » ni « nonante ». Ce sont ces trois formes-là, et seulement elles."},

      {t:'ana', h:"Au-dessus de mille",
       p:"Un gros appareil dépasse souvent mille dollars.",
       mots:[['On écrit','1 049 $'],['On dit','{mille} quarante-neuf dollars',true],['Jamais','« un mille quarante-neuf »']],
       say:"Mille quarante-neuf dollars.",
       note:"À l'écrit, on sépare les milliers par une espace, pas par une virgule : 1 049 $, jamais 1,049 $."},

      {t:'labo', h:"Vois et entends le même prix",
       p:"Choisis un prix de la circulaire.",
       axes:[{id:'n', lbl:'Quel prix ?', opts:[
         ['a','129 $'],['b','280 $'],['c','675 $'],['d','849 $'],['e','1 049 $']]}],
       out:{
         a:{w:['129 $'], say:"Cent vingt-neuf dollars.", n:'le prix du micro-ondes'},
         b:{w:['280 $'], say:"Deux cent quatre-vingts dollars.", n:'quatre-vingts avec un s'},
         c:{w:['675 $'], say:"Six cent soixante-quinze dollars.", n:'soixante-quinze, pas septante-cinq'},
         d:{w:['849 $'], say:"Huit cent quarante-neuf dollars.", n:'le spécial de la laveuse'},
         e:{w:['1 049 $'], say:"Mille quarante-neuf dollars.", n:'le prix régulier'},
       },
       note:"Écoute, puis écris le prix en chiffres sans regarder. C'est exactement l'exercice de la caisse."},

      {t:'ex', h:"À écouter et à répéter",
       p:"Six prix de la circulaire.",
       rows:[
         ["Quatre-vingt-dix dollars.","90 $"],
         ["Cent vingt-neuf dollars.","129 $"],
         ["Deux cent quatre-vingts dollars.","280 $"],
         ["Six cent soixante-quinze dollars.","675 $"],
         ["Huit cent quarante-neuf dollars.","849 $"],
         ["Mille quarante-neuf dollars.","1 049 $"],
       ]},

      {t:'piege', h:"Trois pièges à connaître",
       rows:[
         ["confondre 849 et 840","la fin du nombre",
          "La différence est au dernier mot, et c'est là qu'on écoute le moins. Au magasin, redemande : « Huit cent quarante ou quarante-neuf ? »"],
         ["écrire 1,049 $","la virgule des milliers",
          "En français, la virgule sert aux cents : 129,99 $. Les milliers se séparent par une espace : 1 049 $."],
         ["mettre le signe à gauche","« $ 849 »",
          "Au Québec, le signe de dollar se met après le nombre, avec une espace : 849 $."],
       ]},

      {t:'check', h:"Est-ce que c'est clair maintenant ?",
       p:"Quatre questions rapides.",
       qs:[
         {q:"« Mille quarante-neuf dollars » s'écrit…", opts:["1 049 $","149 $"], ok:0,
          fb:"Mille, puis quarante-neuf."},
         {q:"80 se dit…", opts:["huitante","quatre-vingts"], ok:1,
          fb:"C'est la seule forme employée ici."},
         {q:"Le signe de dollar se met…", opts:["avant le nombre","après le nombre"], ok:1,
          fb:"849 $, avec une espace avant le signe."},
         {q:"Dans la circulaire, le prix d'aujourd'hui est…", opts:["le petit chiffre barré","le gros chiffre"], ok:1,
          fb:"Le petit chiffre barré, c'est le prix régulier."},
       ]},
    ]
  },

  t1dates: {
    eye:'Mini-leçon', tit:"Jusqu'à quel jour le prix est-il bon ?",
    blocs:[
      {t:'texte', h:"Un spécial a toujours une fin",
       p:"Le prix de la circulaire n'est pas le prix du magasin : c'est le prix <b>de cette semaine-là</b>. En bas de la page, deux dates disent quand il commence et quand il finit. Arriver le lundi suivant, c'est payer le prix régulier — deux cents dollars de plus, parfois.",
       note:"Au Québec, la plupart des circulaires commencent le jeudi ou le mardi et finissent le mercredi ou le dimanche. Regarde toujours : ce n'est pas pareil d'un magasin à l'autre."},

      {t:'ana', h:"« Du… au… »",
       p:"La forme la plus fréquente.",
       mots:[['On lit','{du mardi au dimanche}'],['Le premier jour','compris',true],['Le dernier jour','compris aussi']],
       say:"Le spécial dure du mardi au dimanche.",
       note:"Les deux jours nommés font partie du spécial. C'est le jour d'après qui ne compte plus."},

      {t:'ana', h:"« Jusqu'à… »",
       p:"La même chose, en plus court.",
       mots:[['On lit',"{jusqu'à dimanche}"],['Dimanche','oui',true],['Lundi','non']],
       say:"Le prix est bon jusqu'à dimanche.",
       note:"On entend souvent cette formule dans la bouche du vendeur : « Le spécial finit dimanche. »"},

      {t:'ana', h:"Les sept jours, dans l'ordre",
       p:"Les deux qui reviennent le plus dans ce module sont ceux de la livraison.",
       mots:[['La semaine','lundi · mardi · mercredi'],['La suite','{jeudi} · vendredi · {samedi} · dimanche',true],['La date',"le 9 novembre, jamais « novembre 9 »"]],
       say:"Jeudi ou samedi, entre huit heures et midi.",
       note:"Les noms de jours ne prennent pas de majuscule en français : on écrit « samedi », pas « Samedi »."},

      {t:'labo', h:"Le spécial finit quand ?",
       p:"Choisis une formule et vois ce qu'elle veut dire.",
       axes:[
         {id:'f', lbl:'Quelle formule ?', opts:[['a','Du 4 au 9 novembre'],['b',"Jusqu'à dimanche"],['c','Pendant 3 jours'],['d','Quantité limitée']]},
         {id:'j', lbl:'Quel jour es-tu ?', opts:[['1','samedi'],['2','lundi']]}],
       out:{
         a1:{w:["Le prix est bon."], say:"Le prix est bon.", n:'le 9 novembre est un dimanche'},
         a2:{w:["Trop tard : le prix est remonté."], say:"Trop tard, le prix est remonté.", n:'le lundi 10 ne compte plus'},
         b1:{w:["Le prix est bon."], say:"Le prix est bon.", n:'dimanche est compris'},
         b2:{w:["Trop tard."], say:"Trop tard.", n:"« jusqu'à dimanche » s'arrête le dimanche soir"},
         c1:{w:["Regarde la date de début."], say:"Regarde la date de début.", n:'trois jours à partir de quand ?'},
         c2:{w:["Probablement fini."], say:"C'est probablement fini.", n:"trois jours, c'est court"},
         d1:{w:["Vas-y tôt le matin."], say:"Vas-y tôt le matin.", n:'la date ne suffit pas'},
         d2:{w:["Téléphone avant de te déplacer."], say:"Téléphone avant de te déplacer.", n:'il peut ne rien rester'},
       },
       note:"« Quantité limitée » est la seule mention qui peut rendre la date inutile : le spécial finit quand il n'y en a plus."},

      {t:'ex', h:"À écouter et à répéter",
       p:"Six phrases pour parler des dates.",
       rows:[
         ["Le spécial dure du mardi au dimanche.","les deux jours compris"],
         ["Le prix est bon jusqu'à dimanche.","la même chose, en plus court"],
         ["Lundi, le prix remonte.","ce qui arrive après"],
         ["La circulaire arrive le mardi.","dans la boîte aux lettres"],
         ["Le camion passe jeudi ou samedi.","les deux jours de livraison"],
         ["Attention : quantité limitée.","la ligne écrite en petit"],
       ]},

      {t:'piege', h:"Trois pièges à connaître",
       rows:[
         ["croire que le dernier jour ne compte pas","« du 4 au 9 »",
          "Le 9 est compris. C'est le 10 qui est trop tard. En cas de doute, vas-y avant le dernier jour."],
         ["ne pas lire les lignes en petit","« quantité limitée »",
          "Le gros chiffre attire l'œil ; la ligne qui décide est écrite en bas, en petit. Lis-la avant de te déplacer."],
         ["mettre le mois avant le jour","« novembre 9 »",
          "C'est l'ordre de l'anglais. En français, on écrit et on dit « le 9 novembre »."],
       ]},

      {t:'check', h:"Est-ce que c'est clair maintenant ?",
       p:"Quatre questions rapides.",
       qs:[
         {q:"« Du mardi 4 au dimanche 9 » : le dimanche 9…", opts:["compte","ne compte pas"], ok:0,
          fb:"Les deux jours nommés font partie du spécial."},
         {q:"« Jusqu'à dimanche » : le lundi…", opts:["le prix est encore bon","le prix est remonté"], ok:1,
          fb:"Le lundi, on paie le prix régulier."},
         {q:"On écrit…", opts:["le 9 novembre","novembre 9"], ok:0,
          fb:"Le jour d'abord, le mois ensuite."},
         {q:"« Quantité limitée » veut dire…", opts:["il y en a beaucoup","il peut ne plus en rester"], ok:1,
          fb:"Quand c'est vendu, c'est fini, même avant la date."},
       ]},
    ]
  },

  t2ce: {
    eye:'Mini-leçon', tit:"Montrer un appareil : ce, cet, cette, ces",
    blocs:[
      {t:'texte', h:"Quand on ne connaît pas encore le nom exact",
       p:"Dans un magasin, on n'a pas toujours le mot juste. Montrer du doigt et dire « <b>cette laveuse-là</b> » règle la question en une seconde. Ces quatre petits mots — ce, cet, cette, ces — servent à désigner ce qu'on a devant les yeux, et ils sont parmi les plus utiles du niveau.",
       note:"Avec la circulaire dans la main, c'est encore plus simple : on pose le doigt sur la photo et on dit « celle-là »."},

      {t:'ana', h:"Devant un mot masculin : ce",
       p:"La forme la plus courante.",
       mots:[['On dit','{ce modèle}'],['Aussi','ce rayon · ce prix · ce bon',true],['Jamais','« ce aspirateur »']],
       say:"Ce modèle coûte huit cent quarante-neuf dollars.",
       note:"Si le mot masculin commence par une voyelle, on passe à « cet » : c'est la ligne suivante."},

      {t:'ana', h:"Devant une voyelle : cet",
       p:"Pour que ce soit plus facile à dire.",
       mots:[['On dit','{cet aspirateur}'],['Aussi','cet ordinateur · cet appareil',true],['On entend','« cè-t-aspirateur », attaché']],
       say:"Cet aspirateur est en spécial.",
       note:"« cet » et « cette » se prononcent exactement pareil. La différence ne s'entend pas : elle s'écrit."},

      {t:'ana', h:"Devant un mot féminin : cette",
       p:"Et le petit « -là » du Québec.",
       mots:[['On dit','{cette laveuse}'],['Pour montrer','{cette laveuse-là}',true],['Au pluriel','ces laveuses, ces modèles']],
       say:"Cette laveuse-là, elle coûte combien ?",
       note:"Le « -là » n'est pas obligatoire, mais il est partout dans la langue parlée d'ici, et il aide vraiment le vendeur à suivre ton doigt."},

      {t:'labo', h:"Quel mot devant quel appareil ?",
       p:"Choisis un appareil et une phrase.",
       axes:[
         {id:'a', lbl:'Quel appareil ?', opts:[['a','laveuse'],['b','modèle'],['c','aspirateur'],['d','réfrigérateurs']]},
         {id:'p', lbl:'Quelle phrase ?', opts:[['1','montrer'],['2','demander le prix']]}],
       out:{
         a1:{w:["Cette laveuse-là, s'il vous plaît."], say:"Cette laveuse-là, s'il vous plaît.", n:'féminin singulier'},
         a2:{w:["Cette laveuse coûte combien ?"], say:"Cette laveuse coûte combien ?", n:'cette, avec deux t et un e'},
         b1:{w:["Ce modèle-là, dans la circulaire."], say:"Ce modèle-là, dans la circulaire.", n:'masculin, consonne'},
         b2:{w:["Ce modèle coûte combien ?"], say:"Ce modèle coûte combien ?", n:'ce, tout court'},
         c1:{w:["Cet aspirateur-là, en haut."], say:"Cet aspirateur-là, en haut.", n:'masculin, voyelle'},
         c2:{w:["Cet aspirateur coûte combien ?"], say:"Cet aspirateur coûte combien ?", n:"cet, à cause du a"},
         d1:{w:["Ces réfrigérateurs-là sont trop grands."], say:"Ces réfrigérateurs-là sont trop grands.", n:'pluriel'},
         d2:{w:["Ces réfrigérateurs coûtent combien ?"], say:"Ces réfrigérateurs coûtent combien ?", n:'ces, pour les deux genres'},
       },
       note:"Huit phrases prêtes à dire au rayon, sans rien changer."},

      {t:'ex', h:"À écouter et à répéter",
       p:"Six phrases pour montrer.",
       rows:[
         ["Cette laveuse-là est dans la circulaire.","féminin"],
         ["Ce modèle est en spécial.","masculin"],
         ["Cet aspirateur fait moins de bruit.","voyelle"],
         ["Ces réfrigérateurs sont trop grands.","pluriel"],
         ["Cette affichette dit vingt-sept pouces.","féminin"],
         ["Je voudrais essayer cet ordinateur.","voyelle encore"],
       ]},

      {t:'piege', h:"Trois pièges à connaître",
       rows:[
         ["dire « ce aspirateur »","deux voyelles qui se cognent",
          "C'est justement pour ça que « cet » existe. Dès que le mot masculin commence par une voyelle, on met « cet »."],
         ["écrire « cet laveuse »","cet et cette se disent pareil",
          "L'oreille ne peut pas t'aider ici. Demande-toi si le mot est masculin ou féminin, puis écris."],
         ["oublier que « ces » sert aux deux genres","ces laveuses, ces modèles",
          "Au pluriel, il n'y a plus qu'une seule forme. C'est la bonne nouvelle de la leçon."],
       ]},

      {t:'check', h:"Est-ce que c'est clair maintenant ?",
       p:"Quatre questions rapides.",
       qs:[
         {q:"On dit…", opts:["ce aspirateur","cet aspirateur"], ok:1,
          fb:"Devant une voyelle, toujours « cet »."},
         {q:"On écrit…", opts:["cet laveuse","cette laveuse"], ok:1,
          fb:"Laveuse est féminin : cette."},
         {q:"Au pluriel, on dit…", opts:["ces","ce et cette"], ok:0,
          fb:"Une seule forme pour les deux genres."},
         {q:"« Cette laveuse-là » sert à…", opts:["montrer du doigt","dire qu'elle est loin"], ok:0,
          fb:"C'est la façon d'ici de désigner ce qu'on montre."},
       ]},
    ]
  },

  t2questions: {
    eye:'Mini-leçon', tit:'Quatre questions qui suffisent au magasin',
    blocs:[
      {t:'texte', h:"On n'a pas besoin de longues phrases",
       p:"Un vendeur répond à des questions courtes. Où, combien, est-ce que vous avez : avec trois débuts de phrase et un mot d'appareil, tu obtiens tout ce dont tu as besoin. Le reste — la politesse — tient en deux mots : <b>bonjour</b> et <b>merci</b>.",
       note:"Commence toujours par « Bonjour ». Ici, entrer dans un magasin et parler sans saluer surprend."},

      {t:'ana', h:"Trouver le rayon",
       p:"La première question, celle de l'entrée.",
       mots:[['On dit','{où est le rayon} des laveuses ?'],['Au pluriel','Où sont les micro-ondes ?',true],['Réponse type','Au fond, à gauche.']],
       say:"Bonjour, où est le rayon des laveuses ?",
       note:"« Où est » pour un mot singulier, « Où sont » pour un pluriel. Les deux se disent presque pareil, et personne ne te reprendra."},

      {t:'ana', h:"Demander le prix",
       p:"Deux façons, également correctes.",
       mots:[['La plus courte',"{c'est combien} ?"],['La plus complète','Elle coûte combien ?',true],['Avec le doigt',"C'est combien, celui-là ?"]],
       say:"C'est combien, celui-là ?",
       note:"La voix monte à la fin. C'est ce qui fait de la phrase une question, même sans « est-ce que »."},

      {t:'ana', h:"Demander si le magasin l'a",
       p:"La question qui évite de chercher pour rien.",
       mots:[['On dit','{est-ce que vous avez} ce modèle en gris ?'],['Plus court','Vous l\'avez en gris ?',true],['Autre usage','Est-ce que vous livrez ?']],
       say:"Est-ce que vous avez ce modèle en gris ?",
       note:"« Est-ce que » se met devant n'importe quelle phrase et la transforme en question. C'est l'outil le plus rentable du niveau."},

      {t:'ana', h:"Demander le format, et faire répéter",
       p:"Deux questions qui sauvent un achat.",
       mots:[['Le format','Elle fait {combien de large} ?'],['Au Québec','on répond en pouces',true],['Si tu perds le fil','{pouvez-vous répéter} ?']],
       say:"Elle fait combien de large ? Pouvez-vous répéter, s'il vous plaît ?",
       note:"Mesure chez toi <b>avant</b> de partir, et note le chiffre sur un papier. Un appareil trop large revient au magasin."},

      {t:'labo', h:"Construis ta question",
       p:"Choisis ce que tu veux savoir et pour quel appareil.",
       axes:[
         {id:'q', lbl:'Tu veux savoir…', opts:[['a','où c\'est'],['b','le prix'],['c','la couleur'],['d','le format']]},
         {id:'a', lbl:'Quel appareil ?', opts:[['1','la laveuse'],['2','le micro-ondes']]}],
       out:{
         a1:{w:["Où est le rayon des laveuses ?"], say:"Où est le rayon des laveuses ?", n:'singulier : où est'},
         a2:{w:["Où sont les micro-ondes ?"], say:"Où sont les micro-ondes ?", n:'pluriel : où sont'},
         b1:{w:["Cette laveuse-là coûte combien ?"], say:"Cette laveuse-là coûte combien ?", n:'avec le doigt'},
         b2:{w:["C'est combien, celui-là ?"], say:"C'est combien, celui-là ?", n:'la forme la plus courte'},
         c1:{w:["Est-ce que vous l'avez en gris ?"], say:"Est-ce que vous l'avez en gris ?", n:'est-ce que + phrase'},
         c2:{w:["Est-ce que vous l'avez en blanc ?"], say:"Est-ce que vous l'avez en blanc ?", n:'la même question, autre couleur'},
         d1:{w:["Elle fait combien de large ?"], say:"Elle fait combien de large ?", n:'féminin : elle'},
         d2:{w:["Il fait combien de large ?"], say:"Il fait combien de large ?", n:'masculin : il'},
       },
       note:"Huit questions, quatre besoins. C'est tout ce qu'il faut pour un achat."},

      {t:'ex', h:"À écouter et à répéter",
       p:"Six phrases à dire au vendeur.",
       rows:[
         ["Bonjour, où est le rayon des laveuses ?","pour entrer"],
         ["C'est combien, celui-là ?","pour le prix"],
         ["Est-ce que vous avez ce modèle en gris ?","pour la couleur"],
         ["Elle fait combien de large ?","pour le format"],
         ["Pouvez-vous répéter, s'il vous plaît ?","quand ça va trop vite"],
         ["Merci beaucoup. Je la prends.","pour finir"],
       ]},

      {t:'piege', h:"Trois pièges à connaître",
       rows:[
         ["ne pas saluer","entrer et demander tout de suite",
          "Un « bonjour » change complètement l'accueil. Ce n'est pas une règle de grammaire, c'est une règle d'ici."],
         ["dire « je comprends pas » et s'arrêter","rester bloqué",
          "« Pouvez-vous répéter, s'il vous plaît ? » relance la conversation. Tout le monde le dit, y compris entre gens d'ici."],
         ["oublier la voix qui monte","« Vous l'avez en gris. »",
          "Dite avec la voix qui descend, la phrase n'est plus une question : le vendeur croit que tu lui apprends quelque chose."],
       ]},

      {t:'check', h:"Est-ce que c'est clair maintenant ?",
       p:"Quatre questions rapides.",
       qs:[
         {q:"Pour trouver le rayon, on demande…", opts:["Où est le rayon des laveuses ?","Le rayon des laveuses."], ok:0,
          fb:"Une vraie question, avec « où »."},
         {q:"« Est-ce que » se met…", opts:["au début de la phrase","à la fin"], ok:0,
          fb:"Devant la phrase, qui ne change pas autrement."},
         {q:"Au Québec, la largeur d'un appareil se dit en…", opts:["centimètres","pouces"], ok:1,
          fb:"27 pouces, 20 pouces : c'est la mesure du magasin."},
         {q:"Quand tu n'as pas compris, tu dis…", opts:["rien","Pouvez-vous répéter ?"], ok:1,
          fb:"C'est la phrase la plus utile de tout le module."},
       ]},
    ]
  },

  t3futur: {
    eye:'Mini-leçon', tit:'Le futur proche : ce qui va arriver samedi',
    blocs:[
      {t:'texte', h:"Parler de tout à l'heure et de samedi prochain",
       p:"Pour dire ce qui va se passer bientôt, le français n'a pas besoin d'un temps compliqué : il prend le verbe <b>aller</b> au présent et lui colle un second verbe. « Je <b>vais payer</b> », « Le camion <b>va arriver</b> ». C'est le futur du magasin, de la livraison et de la vie de tous les jours.",
       note:"C'est aussi le futur qu'on entend le plus dans la rue. Le futur en -rai existe, mais il attend le niveau suivant."},

      {t:'ana', h:"La forme, en deux morceaux",
       p:"Aller au présent, puis le verbe sans rien changer.",
       mots:[['On dit','{je vais payer}'],['Jamais','« je vais je paie »',true],['Le second verbe','ne change pas : payer, arriver, prendre']],
       say:"Je vais payer à la caisse.",
       note:"Le second verbe garde sa forme de base — celle du dictionnaire. C'est ce qui rend ce futur si facile."},

      {t:'ana', h:"Les quatre formes utiles",
       p:"Celles dont tu as besoin au comptoir.",
       mots:[['Moi','je vais'],['Toi','tu vas'],['Le camion, elle','va — et eux, ils {vont}',true]],
       say:"Je vais, tu vas, il va, ils vont.",
       note:"« Nous allons » et « vous allez » existent aussi, mais à l'oral on entend surtout « on va » : « On va être là samedi. »"},

      {t:'ana', h:"Avec un jour ou une heure",
       p:"C'est ce qui rend la phrase claire.",
       mots:[['On dit','Ils vont passer {samedi matin}'],['Ou','entre huit heures et midi',true],['Ou encore','{la semaine prochaine}']],
       say:"Ils vont passer samedi matin, entre huit heures et midi.",
       note:"Le moment peut se mettre au début ou à la fin : « Samedi matin, ils vont passer. » Les deux se disent."},

      {t:'labo', h:"Qui va faire quoi ?",
       p:"Choisis une personne et une action.",
       axes:[
         {id:'p', lbl:'Qui ?', opts:[['a','je'],['b','le camion'],['c','les livreurs'],['d','tu']]},
         {id:'v', lbl:'Fait quoi ?', opts:[['1','payer'],['2','arriver samedi']]}],
       out:{
         a1:{w:["Je vais payer à la caisse."], say:"Je vais payer à la caisse.", n:'je vais'},
         a2:{w:["Je vais être là samedi."], say:"Je vais être là samedi.", n:'être marche aussi'},
         b1:{w:["Le camion va prendre l'ancienne laveuse."], say:"Le camion va prendre l'ancienne laveuse.", n:'il, elle, le camion : va'},
         b2:{w:["Le camion va arriver samedi matin."], say:"Le camion va arriver samedi matin.", n:'avec le moment'},
         c1:{w:["Les livreurs vont monter la laveuse."], say:"Les livreurs vont monter la laveuse.", n:'ils : vont'},
         c2:{w:["Les livreurs vont arriver entre huit heures et midi."], say:"Les livreurs vont arriver entre huit heures et midi.", n:"une plage d'heures"},
         d1:{w:["Tu vas payer comment ?"], say:"Tu vas payer comment ?", n:'une question au futur proche'},
         d2:{w:["Tu vas être là samedi ?"], say:"Tu vas être là samedi ?", n:'la voix monte à la fin'},
       },
       note:"Huit phrases utiles au comptoir de la livraison."},

      {t:'ex', h:"À écouter et à répéter",
       p:"Six phrases du comptoir.",
       rows:[
         ["Je vais payer à la caisse.","je vais"],
         ["Le camion va arriver samedi matin.","va"],
         ["Les livreurs vont monter la laveuse.","vont"],
         ["Tu vas garder le bon de livraison ?","une question"],
         ["Je ne vais pas être là jeudi.","à la forme négative"],
         ["On va vous appeler avant de passer.","on va, très fréquent"],
       ]},

      {t:'piege', h:"Trois pièges à connaître",
       rows:[
         ["changer le second verbe","« je vais je paie »",
          "Le second verbe reste dans sa forme de base : payer, arriver, prendre, être. Rien à conjuguer deux fois."],
         ["oublier aller","« je payer demain »",
          "Sans « vais », la phrase n'a plus de temps. Les deux morceaux vont toujours ensemble."],
         ["mal placer la négation","« je vais ne pas être là »",
          "« ne » et « pas » entourent aller, pas le second verbe : « je ne vais pas être là »."],
       ]},

      {t:'check', h:"Est-ce que c'est clair maintenant ?",
       p:"Quatre questions rapides.",
       qs:[
         {q:"On dit…", opts:["je vais payer","je vais je paie"], ok:0,
          fb:"Le second verbe garde sa forme de base."},
         {q:"Pour « les livreurs », on emploie…", opts:["va","vont"], ok:1,
          fb:"Ils vont : la forme du pluriel."},
         {q:"À la forme négative, on dit…", opts:["je ne vais pas être là","je vais ne pas être là"], ok:0,
          fb:"Ne et pas entourent le verbe aller."},
         {q:"Ce futur sert surtout pour…", opts:["dans dix ans","bientôt"], ok:1,
          fb:"Samedi, demain, la semaine prochaine."},
       ]},
    ]
  },

  t3pronoms: {
    eye:'Mini-leçon', tit:'Je le prends, je la prends, je les prends',
    blocs:[
      {t:'texte', h:"Ne pas répéter le nom de l'appareil",
       p:"Le vendeur vient de dire « la laveuse » trois fois. Répondre « je prends la laveuse » sonne lourd, et surtout, ce n'est pas ce qu'on entend ici. On remplace le nom par un petit mot placé avant le verbe : « Je <b>la</b> prends. » Trois mots, et l'affaire est conclue.",
       note:"Ces petits mots s'appellent des pronoms. Le nom n'a pas d'importance ; ce qui compte, c'est de savoir lequel choisir et où le mettre."},

      {t:'ana', h:"Masculin : le",
       p:"Pour un appareil masculin.",
       mots:[['Le micro-ondes','{je le prends}'],['Aussi','Vous pouvez le livrer ?',true],['Devant une voyelle',"le devient l' : je l'achète"]],
       say:"Oui, je le prends.",
       note:"Le même petit mot sert pour tous les masculins : le réfrigérateur, l'aspirateur, le bon de livraison."},

      {t:'ana', h:"Féminin : la",
       p:"Pour un appareil féminin.",
       mots:[['La laveuse','{je la prends}'],['Aussi','Vous pouvez la livrer ?',true],['Devant une voyelle',"la devient l' : je l'ai vue"]],
       say:"Oui, je la prends.",
       note:"Devant une voyelle, « le » et « la » deviennent tous deux « l' ». La différence disparaît alors complètement."},

      {t:'ana', h:"Pluriel : les",
       p:"Pour deux appareils ou plus.",
       mots:[['Les deux appareils','{je les prends}'],['Aussi','Ils vont les livrer samedi.',true],['Une seule forme','pour le masculin et le féminin']],
       say:"Les deux sont en spécial : je les prends.",
       note:"Comme pour « ces », le pluriel simplifie tout : une seule forme, quel que soit le genre."},

      {t:'ana', h:"La place du petit mot",
       p:"Avant le verbe, toujours.",
       mots:[['Un verbe','Je {le} prends.'],['Deux verbes','{je vais le prendre}',true],['À l\'impératif','Gardez-le. — là, il passe après']],
       say:"Je vais le prendre tout de suite.",
       note:"Avec deux verbes, le pronom se glisse entre les deux : « Je vais le prendre », « Vous pouvez la livrer ? »"},

      {t:'labo', h:"Quel petit mot ?",
       p:"Choisis un appareil et une phrase.",
       axes:[
         {id:'a', lbl:'Quel appareil ?', opts:[['a','la laveuse'],['b','le micro-ondes'],['c','les deux']]},
         {id:'p', lbl:'Quelle phrase ?', opts:[['1','je prends'],['2','vous livrez ?'],['3','je ne prends pas']]}],
       out:{
         a1:{w:["Je la prends."], say:"Je la prends.", n:'féminin'},
         a2:{w:["Vous pouvez la livrer ?"], say:"Vous pouvez la livrer ?", n:'entre les deux verbes'},
         a3:{w:["Je ne la prends pas."], say:"Je ne la prends pas.", n:'le pronom reste collé au verbe'},
         b1:{w:["Je le prends."], say:"Je le prends.", n:'masculin'},
         b2:{w:["Vous pouvez le livrer ?"], say:"Vous pouvez le livrer ?", n:'même place'},
         b3:{w:["Je ne le prends pas."], say:"Je ne le prends pas.", n:'ne … pas autour du verbe'},
         c1:{w:["Je les prends."], say:"Je les prends.", n:'pluriel'},
         c2:{w:["Vous pouvez les livrer ?"], say:"Vous pouvez les livrer ?", n:'une seule forme au pluriel'},
         c3:{w:["Je ne les prends pas."], say:"Je ne les prends pas.", n:'même place encore'},
       },
       note:"Neuf phrases : c'est tout ce que le vendeur attend comme réponse."},

      {t:'ex', h:"À écouter et à répéter",
       p:"Six réponses courtes.",
       rows:[
         ["Oui, je la prends.","la laveuse"],
         ["Oui, je le prends.","le micro-ondes"],
         ["Je les prends tous les deux.","deux appareils"],
         ["Vous pouvez la livrer samedi ?","avec deux verbes"],
         ["Non, je ne le prends pas aujourd'hui.","à la forme négative"],
         ["Gardez-le jusqu'à samedi.","à l'impératif, il passe après"],
       ]},

      {t:'piege', h:"Trois pièges à connaître",
       rows:[
         ["mettre le pronom après le verbe","« je prends le »",
          "En français, le petit mot passe avant : « je le prends ». C'est l'inverse de plusieurs langues, et c'est la faute la plus fréquente."],
         ["choisir d'après l'objet","le genre du mot, pas de l'appareil",
          "C'est le mot qui décide : « la laveuse » donne « la », « le micro-ondes » donne « le ». L'objet, lui, n'a pas de genre."],
         ["oublier l'apostrophe","« je le achète »",
          "Devant une voyelle, le et la deviennent l' : « je l'achète », « je l'ai vue »."],
       ]},

      {t:'check', h:"Est-ce que c'est clair maintenant ?",
       p:"Quatre questions rapides.",
       qs:[
         {q:"« Je prends la laveuse » devient…", opts:["je la prends","je prends la"], ok:0,
          fb:"Le pronom passe avant le verbe."},
         {q:"Pour « le micro-ondes », on dit…", opts:["je le prends","je la prends"], ok:0,
          fb:"Micro-ondes est masculin."},
         {q:"Avec deux verbes, le pronom se met…", opts:["avant le premier","entre les deux"], ok:1,
          fb:"« Je vais le prendre », « Vous pouvez la livrer ? »"},
         {q:"Devant une voyelle, « le » devient…", opts:["l'","les"], ok:0,
          fb:"Je l'achète, je l'ai vue."},
       ]},
    ]
  },
};
