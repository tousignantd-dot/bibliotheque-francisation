const PLUS = {
  prSons: {
    eye:'Mini-leçon', tit:"Treize ou trente ?",
    blocs:[
      {t:'texte', h:"Deux nombres, une seule syllabe de différence",
       p:"« J'ai <b>treize</b> ans » et « j'ai <b>trente</b> ans » ne veulent pas dire la même chose. Sur une fiche d'inscription, un nombre mal entendu change une date de naissance, un numéro de local, un numéro de téléphone. C'est la confusion la plus fréquente du français, et elle se règle en écoutant la <b>fin</b> du mot.",
       note:"Personne ne devine à l'oreille du premier coup. C'est un exercice, pas un talent."},

      {t:'ana', h:"La fin en « ze » — les petits nombres",
       p:"De 13 à 16, tous finissent par le même son.",
       mots:[['13','trei{ze}'],['14','quator{ze}'],['15','quin{ze}'],['16','sei{ze}',true]],
       say:"Treize, quatorze, quinze, seize.",
       note:"Le son « ze » vibre : posez la main sur votre gorge, vous le sentez."},

      {t:'ana', h:"La fin en « te » — les dizaines",
       p:"De 30 à 60, tous finissent par le même son.",
       mots:[['30','tren{te}'],['40','quaran{te}'],['50','cinquan{te}'],['60','soixan{te}',true]],
       say:"Trente, quarante, cinquante, soixante.",
       note:"Le son « te » ne vibre pas. C'est un petit coup sec, et le mot s'arrête."},

      {t:'ana', h:"Deux paires qui trompent tout le monde",
       p:"Le début se ressemble, la fin décide.",
       mots:[['13 / 30','trei{ze} · tren{te}'],['14 / 40','quator{ze} · quaran{te}'],['Ce qui change','la dernière syllabe, jamais la première',true]],
       say:"Treize, trente. Quatorze, quarante.",
       note:"15 et 50 sont plus faciles : « quinze » et « cinquante » ne commencent même pas pareil."},

      {t:'labo', h:"Écoutez et comparez",
       p:"Choisissez une paire.",
       axes:[{id:'p', lbl:'Quelle paire ?', opts:[
         ['a','13 et 30'],
         ['b','14 et 40'],
         ['c','15 et 50'],
         ['d','16 et 60'],
         ['e','2 et 12']]}],
       out:{
         a:{w:['treize · trente'], say:"Treize. Trente. Treize. Trente.", n:'la fin en ze, la fin en te'},
         b:{w:['quatorze · quarante'], say:"Quatorze. Quarante. Quatorze. Quarante.", n:'même début, fin différente'},
         c:{w:['quinze · cinquante'], say:"Quinze. Cinquante. Quinze. Cinquante.", n:'ici, même le début change'},
         d:{w:['seize · soixante'], say:"Seize. Soixante. Seize. Soixante.", n:'la paire la plus facile des quatre'},
         e:{w:['deux · douze'], say:"Deux. Douze. Deux. Douze.", n:'une paire de plus, très fréquente au téléphone'},
       },
       note:"Écoutez trois fois, puis répétez à voix haute. Ce sont les oreilles qui apprennent, pas les yeux."},

      {t:'ex', h:"À écouter et à répéter",
       p:"Six nombres de la fiche.",
       rows:[
         ["J'ai trente ans.","une dizaine"],
         ["Je suis née le treize.","un petit nombre"],
         ["Le local quatorze.","attention à la fin"],
         ["Il y a quarante élèves.","une dizaine"],
         ["Le cours dure quinze minutes.","un petit nombre"],
         ["Cinquante dollars.","une dizaine"],
       ]},

      {t:'piege', h:"Trois pièges à connaître",
       rows:[
         ["écouter le début","« quat… » ne dit rien",
          "Quatorze et quarante commencent pareil. Attendez la fin du mot avant de décider."],
         ["répondre sans vérifier","une date de naissance fausse suit longtemps",
          "Quand un chiffre compte — une date, un local, un numéro — répétez-le à voix haute : « quatorze, un-quatre ? »"],
         ["croire que c'est une question de vitesse","ce n'est pas la vitesse, c'est la syllabe",
          "Même très lentement, treize et trente restent différents seulement par leur fin."],
       ]},

      {t:'check', h:"Est-ce que c'est clair maintenant ?",
       p:"Quatre questions rapides.",
       qs:[
         {q:"« Treize » finit par…", opts:["le son ze","le son te"], ok:0,
          fb:"Trei-ze. Comme quatorze, quinze, seize."},
         {q:"« Quarante » s'écrit…", opts:["14","40"], ok:1,
          fb:"Quarante est une dizaine : 40."},
         {q:"Ce qui distingue 13 de 30, c'est…", opts:["le début","la fin"], ok:1,
          fb:"La dernière syllabe, toujours."},
         {q:"Pour vérifier un chiffre important, on…", opts:["le répète à voix haute","attend"], ok:0,
          fb:"« Quatorze, un-quatre ? » — deux secondes, et plus d'erreur."},
       ]},
    ]
  },

  t1quel: {
    eye:'Mini-leçon', tit:"Quel ou quelle ?",
    blocs:[
      {t:'texte', h:"La question qu'on vous posera toute la vie",
       p:"« <b>Quel</b> est votre nom ? » « <b>Quelle</b> est votre adresse ? » C'est la forme des questions d'une fiche, d'un guichet, d'un formulaire. Les deux se disent exactement de la même façon : à l'oral, vous n'avez rien à choisir. À l'écrit, une seule chose décide — le mot qui vient après.",
       note:"Ce n'est pas vous qui êtes masculin ou féminin dans cette phrase : c'est le mot de la case."},

      {t:'ana', h:"Quel — devant un mot masculin",
       p:"Un nom, un prénom, un numéro, un code.",
       mots:[['Le nom','{Quel} est votre nom de famille ?'],['Le prénom','{Quel} est votre prénom ?'],['Le numéro','{Quel} est votre numéro de téléphone ?',true]],
       say:"Quel est votre nom de famille ? Quel est votre prénom ?",
       note:"Le nom, le prénom, le numéro, le code postal, le courriel : tous masculins."},

      {t:'ana', h:"Quelle — devant un mot féminin",
       p:"Une adresse, une date, une année, une langue.",
       mots:[['L\'adresse','{Quelle} est votre adresse ?'],['La date','{Quelle} est votre date de naissance ?'],['L\'année','{Quelle} est votre année de naissance ?',true]],
       say:"Quelle est votre adresse ? Quelle est votre date de naissance ?",
       note:"L'adresse, la date, l'année, la ville, la rue : toutes féminines."},

      {t:'ana', h:"À l'oreille, aucune différence",
       p:"Un seul son pour deux orthographes.",
       mots:[['On entend','« kel »'],['On écrit','quel ou quelle'],['Ce qui décide','le mot juste après',true]],
       say:"Quel. Quelle. Quel. Quelle.",
       note:"C'est une bonne nouvelle : à l'oral, vous ne pouvez pas vous tromper."},

      {t:'labo', h:"Posez la question",
       p:"Choisissez une case de la fiche.",
       axes:[{id:'p', lbl:'Quelle case ?', opts:[
         ['a','le nom de famille'],
         ['b','le prénom'],
         ['c','l\'adresse'],
         ['d','la date de naissance'],
         ['e','le téléphone'],
         ['f','le code postal']]}],
       out:{
         a:{w:['Quel est votre nom de famille ?'], say:"Quel est votre nom de famille ?", n:'le nom — masculin'},
         b:{w:['Quel est votre prénom ?'], say:"Quel est votre prénom ?", n:'le prénom — masculin'},
         c:{w:['Quelle est votre adresse ?'], say:"Quelle est votre adresse ?", n:"l'adresse — féminin"},
         d:{w:['Quelle est votre date de naissance ?'], say:"Quelle est votre date de naissance ?", n:'la date — féminin'},
         e:{w:['Quel est votre numéro de téléphone ?'], say:"Quel est votre numéro de téléphone ?", n:'le numéro — masculin'},
         f:{w:['Quel est votre code postal ?'], say:"Quel est votre code postal ?", n:'le code — masculin'},
       },
       note:"Six questions. Ce sont celles qu'on vous posera à l'inscription, mot pour mot."},

      {t:'ex', h:"À écouter et à répéter",
       p:"Les six questions de la fiche.",
       rows:[
         ["Quel est votre nom de famille ?","masculin"],
         ["Quel est votre prénom ?","masculin"],
         ["Quelle est votre date de naissance ?","féminin"],
         ["Quelle est votre adresse ?","féminin"],
         ["Quel est votre numéro de téléphone ?","masculin"],
         ["Quel est votre courriel ?","masculin"],
       ]},

      {t:'piege', h:"Trois pièges à connaître",
       rows:[
         ["accorder avec soi-même","« quelle est mon nom ? »",
          "Une femme dit « <b>quel</b> est mon nom ? » et un homme dit « <b>quelle</b> est mon adresse ? ». C'est le mot de la case qui décide, jamais la personne."],
         ["chercher la différence à l'oral","il n'y en a pas",
          "Quel et quelle se prononcent pareil. Inutile de forcer une différence que personne n'entend."],
         ["écrire « qu'elle »","« qu'elle est votre adresse ? »",
          "« Qu'elle » avec une apostrophe veut dire « que elle ». Dans une question de fiche, c'est toujours <b>quelle</b>, en un seul mot."],
       ]},

      {t:'check', h:"Est-ce que c'est clair maintenant ?",
       p:"Quatre questions rapides.",
       qs:[
         {q:"___ est votre adresse ?", opts:["Quel","Quelle"], ok:1,
          fb:"L'adresse est un mot féminin."},
         {q:"___ est votre prénom ?", opts:["Quel","Quelle"], ok:0,
          fb:"Le prénom est un mot masculin."},
         {q:"À l'oral, quel et quelle…", opts:["se disent pareil","se disent autrement"], ok:0,
          fb:"Un seul son : « kel »."},
         {q:"Ce qui décide, c'est…", opts:["la personne qui parle","le mot qui suit"], ok:1,
          fb:"Le mot de la case, toujours."},
       ]},
    ]
  },

  t1date: {
    eye:'Mini-leçon', tit:"Le jour, le mois, l'année",
    blocs:[
      {t:'texte', h:"Trois nombres, un seul ordre",
       p:"Ici, une date s'écrit dans cet ordre : le <b>jour</b>, puis le <b>mois</b>, puis l'<b>année</b>. Le 12 mars 1992 devient <b>12 / 03 / 1992</b>. Dans plusieurs pays, le mois passe devant — et la même date y devient 03 / 12 / 1992, c'est-à-dire le 3 décembre. Une case remplie dans le mauvais ordre vous change de date de naissance.",
       note:"Quand vous doutez, écrivez le mois en lettres : 12 mars 1992. Personne ne peut se tromper."},

      {t:'ana', h:"Le jour — deux chiffres",
       p:"Du 01 au 31.",
       mots:[['Le 5 janvier','{05} / 01'],['Le 12 mars','{12} / 03'],['La règle','un zéro devant les nombres d\'un seul chiffre',true]],
       say:"Le cinq janvier. Le douze mars.",
       note:"05 et non 5 : la case attend deux chiffres, comme toutes les cases de date."},

      {t:'ana', h:"Le mois — un numéro, pas un mot",
       p:"Janvier est 01, décembre est 12.",
       mots:[['Mars','{03}'],['Juillet','{07}'],['Novembre','{11}',true]],
       say:"Mars, zéro trois. Juillet, zéro sept. Novembre, onze.",
       note:"Comptez sur vos doigts : janvier 1, février 2, mars 3… C'est le seul moyen, et il marche."},

      {t:'ana', h:"L'année — quatre chiffres",
       p:"Jamais deux.",
       mots:[['On écrit','{1992}'],['On n\'écrit pas','92'],['Aujourd\'hui','{2026}',true]],
       say:"Mille neuf cent quatre-vingt-douze. Deux mille vingt-six.",
       note:"Une année à deux chiffres est ambiguë : 26 peut vouloir dire 1926 ou 2026."},

      {t:'labo', h:"Écrivez la date",
       p:"Choisissez une date.",
       axes:[{id:'p', lbl:'Quelle date ?', opts:[
         ['a','le 12 mars 1992'],
         ['b','le 5 janvier 1988'],
         ['c','le 30 juillet 2001'],
         ['d','le 1er novembre 1975'],
         ['e','le 9 septembre 2010']]}],
       out:{
         a:{w:['12 / 03 / 1992'], say:"Le douze mars mille neuf cent quatre-vingt-douze.", n:'mars, le mois numéro trois'},
         b:{w:['05 / 01 / 1988'], say:"Le cinq janvier mille neuf cent quatre-vingt-huit.", n:'un zéro devant le cinq'},
         c:{w:['30 / 07 / 2001'], say:"Le trente juillet deux mille un.", n:'juillet, le mois numéro sept'},
         d:{w:['01 / 11 / 1975'], say:"Le premier novembre mille neuf cent soixante-quinze.", n:'le premier du mois se dit « premier »'},
         e:{w:['09 / 09 / 2010'], say:"Le neuf septembre deux mille dix.", n:'même chiffre deux fois, par hasard'},
       },
       note:"Faites la vôtre à la fin : écrivez votre date de naissance dans les trois cases."},

      {t:'ex', h:"À écouter et à répéter",
       p:"Six dates.",
       rows:[
         ["Le douze mars mille neuf cent quatre-vingt-douze.","la date de Yusuf"],
         ["Le cinq janvier.","un zéro devant"],
         ["Le premier novembre.","« premier », pas « un »"],
         ["Le trente juillet.","une dizaine"],
         ["Deux mille vingt-six.","l'année d'aujourd'hui"],
         ["Je suis né le quinze août.","la phrase complète"],
       ]},

      {t:'piege', h:"Trois pièges à connaître",
       rows:[
         ["le mois avant le jour","03 / 12 au lieu de 12 / 03",
          "Ici, le jour vient toujours en premier. Dans le doute, écrivez le mois en lettres."],
         ["écrire l'année à deux chiffres","« 92 »",
          "Quatre chiffres, toujours : 1992. Une fiche refuse souvent les deux chiffres."],
         ["dire « un novembre »","le premier novembre",
          "Le premier jour du mois se dit et s'écrit <b>1er</b> : le 1er novembre. Les autres jours sont des nombres ordinaires : le 2, le 3, le 15."],
       ]},

      {t:'check', h:"Est-ce que c'est clair maintenant ?",
       p:"Quatre questions rapides.",
       qs:[
         {q:"Le 12 mars 1992 s'écrit…", opts:["12 / 03 / 1992","03 / 12 / 1992"], ok:0,
          fb:"Le jour, puis le mois, puis l'année."},
         {q:"Le mois de juillet s'écrit…", opts:["06","07"], ok:1,
          fb:"Janvier 01, février 02… juillet 07."},
         {q:"L'année s'écrit avec…", opts:["deux chiffres","quatre chiffres"], ok:1,
          fb:"1992, et non 92."},
         {q:"Le 5 janvier s'écrit…", opts:["5 / 01","05 / 01"], ok:1,
          fb:"Un zéro devant les nombres d'un seul chiffre."},
       ]},
    ]
  },

  t2abrev: {
    eye:'Mini-leçon', tit:"Les petits mots coupés de la fiche",
    blocs:[
      {t:'texte', h:"Une fiche est pleine de mots coupés",
       p:"<b>app.</b>, <b>av.</b>, <b>boul.</b>, <b>QC</b>, <b>Tél.</b>, <b>C.P.</b>, <b>n°</b>. Ce ne sont pas des mots nouveaux : ce sont des mots que vous connaissez, écrits en plus court parce que la case est petite. Le point à la fin veut dire « le mot n'est pas fini ».",
       note:"Une dizaine d'abréviations suffisent pour lire n'importe quelle fiche au Québec."},

      {t:'ana', h:"Les mots de l'adresse",
       p:"Ils portent tous un point.",
       mots:[['app.','un {appartement}'],['av.','une {avenue}'],['boul.','un {boulevard}',true]],
       say:"Appartement. Avenue. Boulevard.",
       note:"« rue » ne s'abrège pas : c'est déjà court, on l'écrit en entier."},

      {t:'ana', h:"Les deux lettres de la province",
       p:"Sans point, en majuscules.",
       mots:[['QC','{Québec}'],['On écrit','Montréal, {QC}'],['Après','le code postal',true]],
       say:"Montréal, Québec. Montréal, QC.",
       note:"Chaque province a ses deux lettres : ON pour l'Ontario, NB pour le Nouveau-Brunswick."},

      {t:'ana', h:"Les cases du bas",
       p:"Trois abréviations à connaître.",
       mots:[['Tél.','le {téléphone}'],['C.P.','une {case postale}'],['n°','un {numéro}',true]],
       say:"Téléphone. Case postale. Numéro.",
       note:"Une case postale est une petite boîte au bureau de poste. On en prend une quand on n'a pas encore d'adresse à soi."},

      {t:'labo', h:"Que veut dire cette abréviation ?",
       p:"Choisissez-en une.",
       axes:[{id:'p', lbl:"Quelle abréviation ?", opts:[
         ['a','app.'],
         ['b','av.'],
         ['c','boul.'],
         ['d','QC'],
         ['e','Tél.'],
         ['f','C.P.']]}],
       out:{
         a:{w:['un appartement'], say:"App. veut dire appartement.", n:'app. 4 · le numéro suit'},
         b:{w:['une avenue'], say:"Av. veut dire avenue.", n:'3120, av. Papineau'},
         c:{w:['un boulevard'], say:"Boul. veut dire boulevard.", n:'940, boul. Saint-Laurent'},
         d:{w:['Québec, la province'], say:"QC veut dire Québec.", n:'Montréal, QC · sans point'},
         e:{w:['le téléphone'], say:"Tél. veut dire téléphone.", n:'dix chiffres après'},
         f:{w:['une case postale'], say:"C.P. veut dire case postale.", n:'une boîte au bureau de poste'},
       },
       note:"Prenez une vraie enveloppe chez vous et retrouvez-y trois de ces abréviations."},

      {t:'ex', h:"À écouter et à répéter",
       p:"Six lignes d'adresse.",
       rows:[
         ["3120, avenue Papineau.","av."],
         ["Appartement 4.","app."],
         ["940, boulevard Saint-Laurent.","boul."],
         ["Montréal, Québec.","QC"],
         ["Mon numéro de téléphone.","Tél."],
         ["Case postale 118.","C.P."],
       ]},

      {t:'piege', h:"Trois pièges à connaître",
       rows:[
         ["oublier le point","« av » au lieu de « av. »",
          "Le point fait partie de l'abréviation. Sans lui, ce n'est plus un mot coupé."],
         ["mettre un point à QC","« Q.C. »",
          "Les deux lettres de la province s'écrivent sans point et en majuscules : QC."],
         ["confondre C.P. et code postal","ce ne sont pas les mêmes cases",
          "<b>C.P.</b> est une boîte au bureau de poste. Le <b>code postal</b> est la suite de six caractères — H2K 1N4 — qui vient après la ville."],
       ]},

      {t:'check', h:"Est-ce que c'est clair maintenant ?",
       p:"Quatre questions rapides.",
       qs:[
         {q:"« app. » veut dire…", opts:["appartement","appeler"], ok:0,
          fb:"App. 4, par exemple."},
         {q:"« QC » s'écrit…", opts:["avec des points","sans point"], ok:1,
          fb:"QC, en deux majuscules."},
         {q:"« Tél. » demande…", opts:["dix chiffres","six lettres"], ok:0,
          fb:"Un numéro de téléphone a dix chiffres."},
         {q:"Le point à la fin dit que…", opts:["le mot est coupé","la phrase est finie"], ok:0,
          fb:"C'est la marque de l'abréviation."},
       ]},
    ]
  },

  t2tel: {
    eye:'Mini-leçon', tit:"Dire un numéro, un code, un courriel",
    blocs:[
      {t:'texte', h:"Trois suites de caractères à dire tout haut",
       p:"Le <b>téléphone</b>, le <b>code postal</b> et le <b>courriel</b> ne se disent pas comme des mots : ils se disent caractère par caractère, lentement, avec des pauses. C'est la partie de l'inscription où on se fait le plus souvent répéter — et c'est normal.",
       note:"Un chiffre mal entendu, et le centre ne peut plus vous joindre. Ça vaut la peine de ralentir."},

      {t:'ana', h:"Le téléphone — dix chiffres, trois groupes",
       p:"Un chiffre à la fois.",
       mots:[['On écrit','514 555 0198'],['On dit','cinq · un · quatre — cinq · cinq · cinq — zéro · un · neuf · huit'],['On ne dit pas','cinq cent quatorze',true]],
       say:"Cinq, un, quatre. Cinq, cinq, cinq. Zéro, un, neuf, huit.",
       note:"Les trois premiers chiffres sont l'indicatif de la région : 514 et 438 à Montréal, 418 à Québec, 450 autour de Montréal."},

      {t:'ana', h:"Le code postal — six caractères",
       p:"Lettre, chiffre, lettre — chiffre, lettre, chiffre.",
       mots:[['On écrit','H2K 1N4'],['On dit','H · deux · K — un · N · quatre'],['Toujours','trois et trois',true]],
       say:"H, deux, K. Un, N, quatre.",
       note:"La première lettre dit la région : H pour l'île de Montréal, G pour Québec, J pour les environs."},

      {t:'ana', h:"Le courriel — le point et l'arobase",
       p:"Deux signes à nommer.",
       mots:[['@','a{robase}'],['.','{point}'],['On dit','yusuf point daoud arobase courriel point c a',true]],
       say:"Yusuf point daoud, arobase, courriel point c a.",
       note:"Épelez la partie avant l'arobase si votre nom ne s'écrit pas comme il se prononce. On vous le demandera."},

      {t:'labo', h:"Dites-le à voix haute",
       p:"Choisissez ce que vous voulez entendre.",
       axes:[{id:'p', lbl:'Quoi ?', opts:[
         ['a','un numéro de téléphone'],
         ['b','un code postal'],
         ['c','un courriel'],
         ['d','faire répéter'],
         ['e','vérifier un chiffre']]}],
       out:{
         a:{w:['514 555 0198'], say:"Cinq, un, quatre. Cinq, cinq, cinq. Zéro, un, neuf, huit.", n:'trois groupes, une pause entre chaque'},
         b:{w:['H2K 1N4'], say:"H, deux, K. Un, N, quatre.", n:'trois caractères, puis trois'},
         c:{w:['yusuf.daoud@courriel.ca'], say:"Yusuf point daoud, arobase, courriel point c a.", n:'point, arobase, point'},
         d:{w:["Pardon ? Plus lentement, s'il vous plaît."], say:"Pardon ? Plus lentement, s'il vous plaît.", n:'la phrase la plus utile de la journée'},
         e:{w:['Quatorze ou quarante ?'], say:"Quatorze ou quarante ?", n:'deux secondes qui évitent une erreur'},
       },
       note:"Écrivez votre vrai numéro sur un papier, puis dites-le trois fois, lentement."},

      {t:'ex', h:"À écouter et à répéter",
       p:"Six phrases du comptoir.",
       rows:[
         ["Mon numéro est le 514 555 0198.","dix chiffres"],
         ["Mon code postal est H2K 1N4.","six caractères"],
         ["Mon courriel : yusuf point daoud arobase courriel point c a.","point et arobase"],
         ["Pardon ? Plus lentement, s'il vous plaît.","faire ralentir"],
         ["Pouvez-vous répéter le dernier chiffre ?","vérifier"],
         ["Je répète : cinq, un, quatre.","confirmer"],
       ]},

      {t:'piege', h:"Trois pièges à connaître",
       rows:[
         ["dire les chiffres deux par deux","« cinquante-cinq, cinquante-cinq »",
          "En France, on regroupe les chiffres deux par deux. Ici, on les dit <b>un par un</b>. Un groupe mal découpé rend le numéro incompréhensible."],
         ["dire « at » pour @","le mot d'ici est « arobase »",
          "En anglais on dit « at ». En français, le signe s'appelle <b>arobase</b>, et tout le monde le comprend."],
         ["ne pas oser faire répéter","le numéro reste faux dans le dossier",
          "Un chiffre mal noté, et l'appel du centre ne vous arrive jamais. Faire répéter prend cinq secondes."],
       ]},

      {t:'check', h:"Est-ce que c'est clair maintenant ?",
       p:"Quatre questions rapides.",
       qs:[
         {q:"Un numéro de téléphone a…", opts:["sept chiffres","dix chiffres"], ok:1,
          fb:"Trois pour la région, puis sept."},
         {q:"On dit les chiffres…", opts:["un par un","deux par deux"], ok:0,
          fb:"C'est l'usage d'ici."},
         {q:"Le signe @ se dit…", opts:["arobase","at"], ok:0,
          fb:"Arobase, en français."},
         {q:"Un code postal a…", opts:["six caractères","huit caractères"], ok:0,
          fb:"Trois lettres et trois chiffres, en alternance."},
       ]},
    ]
  },
};
