const PLUS = {
  prLieu: {
    eye:'Mini-leçon', tit:"Où on va : à la, au, à l'",
    blocs:[
      {t:'texte', h:"Un tout petit mot qui change trois fois",
       p:"Pour dire où on va, on emploie <b>à</b> : « je vais <b>à</b> Montréal ». Mais devant le nom d'un lieu, <b>à</b> se colle à l'article et change de forme : <b>à la</b>, <b>au</b>, <b>à l'</b>. C'est le même mot chaque fois — seule la forme change, selon le lieu.",
       note:"Personne ne l'apprend d'un coup. On l'entend, on le répète, et un jour il vient tout seul."},

      {t:'ana', h:"à la — devant un lieu féminin",
       p:"Bibliothèque, pharmacie, banque, clinique.",
       mots:[['On dit','Je vais {à la} bibliothèque.'],['Aussi','Je vais {à la} pharmacie.'],['On ne dit pas','je vais à bibliothèque',true]],
       say:"Je vais à la bibliothèque. Je vais à la pharmacie.",
       note:"Si vous dites « <b>une</b> bibliothèque », c'est féminin : ce sera « à la »."},

      {t:'ana', h:"au — devant un lieu masculin",
       p:"Parc, marché, CLSC, dépanneur.",
       mots:[['On dit','Je vais {au} parc.'],['Aussi','Je vais {au} marché.'],['On ne dit pas','je vais à le parc',true]],
       say:"Je vais au parc. Je vais au marché.",
       note:"« À le » n'existe pas en français. Les deux mots se collent toujours et donnent <b>au</b>."},

      {t:'ana', h:"à l' — devant une voyelle",
       p:"École, hôpital, arrêt, épicerie.",
       mots:[['On dit','Je vais {à l\'}école.'],['Aussi','Je vais {à l\'}hôpital.'],['Masculin ou féminin','ça ne change rien ici',true]],
       say:"Je vais à l'école. Je vais à l'hôpital.",
       note:"Devant une voyelle — a, e, i, o, u — et devant un <b>h</b> muet, c'est toujours « à l' »."},

      {t:'labo', h:"Où allez-vous ?",
       p:"Choisissez un lieu et une phrase.",
       axes:[
         {id:'p', lbl:'Quel lieu ?', opts:[
           ['a','la bibliothèque'],
           ['b','le parc'],
           ['c',"l'hôpital"],
           ['d','la pharmacie'],
           ['e','le CLSC']]},
         {id:'q', lbl:'Quelle phrase ?', opts:[['1','je vais'],['2','je cherche'],['3',"c'est loin ?"]]}],
       out:{
         a1:{w:["Je vais à la bibliothèque."], say:"Je vais à la bibliothèque.", n:'féminin : à la'},
         a2:{w:["Je cherche la bibliothèque."], say:"Je cherche la bibliothèque.", n:'après « je cherche », pas de à'},
         a3:{w:["La bibliothèque, c'est loin ?"], say:"La bibliothèque, c'est loin ?", n:'la question la plus utile'},
         b1:{w:["Je vais au parc."], say:"Je vais au parc.", n:'masculin : au'},
         b2:{w:["Je cherche le parc."], say:"Je cherche le parc.", n:'le lieu seul, avec son article'},
         b3:{w:["Le parc, c'est loin ?"], say:"Le parc, c'est loin ?", n:'on met le lieu devant'},
         c1:{w:["Je vais à l'hôpital."], say:"Je vais à l'hôpital.", n:"h muet : à l'"},
         c2:{w:["Je cherche l'hôpital."], say:"Je cherche l'hôpital.", n:"l' devant la voyelle"},
         c3:{w:["L'hôpital, c'est loin ?"], say:"L'hôpital, c'est loin ?", n:'à demander avant de partir à pied'},
         d1:{w:["Je vais à la pharmacie."], say:"Je vais à la pharmacie.", n:'féminin : à la'},
         d2:{w:["Je cherche une pharmacie."], say:"Je cherche une pharmacie.", n:"« une » : n'importe laquelle"},
         d3:{w:["La pharmacie, c'est loin ?"], say:"La pharmacie, c'est loin ?", n:'il y en a souvent une près'},
         e1:{w:["Je vais au CLSC."], say:"Je vais au CLSC.", n:'masculin : au'},
         e2:{w:["Je cherche le CLSC."], say:"Je cherche le CLSC.", n:'on épelle les trois lettres'},
         e3:{w:["Le CLSC, c'est loin ?"], say:"Le CLSC, c'est loin ?", n:'C, L, S, C — lentement'},
       },
       note:"Quinze phrases. Dites à voix haute celles des lieux où vous allez vraiment."},

      {t:'ex', h:"À écouter et à répéter",
       p:"Six phrases pour sortir de chez soi.",
       rows:[
         ["Je vais à la bibliothèque.","à la — féminin"],
         ["Je vais au parc.","au — masculin"],
         ["Je vais à l'école.","à l' — voyelle"],
         ["Excusez-moi, je cherche la pharmacie.","pour demander"],
         ["C'est loin d'ici ?","la question qui suit"],
         ["Merci beaucoup. Bonne journée !","pour finir"],
       ]},

      {t:'piege', h:"Trois pièges à connaître",
       rows:[
         ["« je vais à le parc »","je vais au parc",
          "« À le » n'existe pas. Les deux mots se collent et donnent <b>au</b>. C'est une règle sans exception."],
         ["« je vais à bibliothèque »","je vais à la bibliothèque",
          "En français, un lieu garde presque toujours son article : <b>la</b> bibliothèque, <b>le</b> parc. Seuls les noms de villes n'en ont pas : « je vais à Montréal »."],
         ["« à la hôpital »","à l'hôpital",
          "Devant une voyelle ou un <b>h</b> muet, « la » et « le » deviennent <b>l'</b>. On dit donc « à l'hôpital », jamais « à la hôpital »."],
       ]},

      {t:'check', h:"Est-ce que c'est clair maintenant ?",
       p:"Quatre questions rapides.",
       qs:[
         {q:"Je vais ___ parc.", opts:["à le","au"], ok:1,
          fb:"« À le » n'existe pas : ça donne toujours <b>au</b>."},
         {q:"Je vais ___ pharmacie.", opts:["à la","au"], ok:0,
          fb:"Une pharmacie : c'est féminin, donc « à la »."},
         {q:"Je vais ___ école.", opts:["à la","à l'"], ok:1,
          fb:"Devant une voyelle, c'est toujours « à l' »."},
         {q:"Devant un nom de ville, on dit…", opts:["à Montréal","à la Montréal"], ok:0,
          fb:"Les villes n'ont pas d'article : « à Montréal », « à Québec »."},
       ]},
    ]
  },

  t1direction: {
    eye:'Mini-leçon', tit:"Les mots de la direction",
    blocs:[
      {t:'texte', h:"Six mots suffisent",
       p:"Quand on vous indique un chemin, la réponse tient presque toujours dans les mêmes six mots : <b>tout droit</b>, <b>à droite</b>, <b>à gauche</b>, <b>jusqu'à</b>, <b>au coin</b>, <b>après</b>. Sachez les six, et vous comprendrez la plupart des réponses — même dites vite.",
       note:"Vous n'avez pas besoin de comprendre toute la phrase. Ces six mots-là portent l'information."},

      {t:'ana', h:"Où tourner",
       p:"Trois directions, et c'est tout.",
       mots:[['Sans tourner','Continuez {tout droit}.'],['Vers la droite','Tournez {à droite}.'],['Vers la gauche','Tournez {à gauche}.',true]],
       say:"Tout droit. À droite. À gauche.",
       note:"Beaucoup de gens montrent la direction avec la main en même temps. Regardez la main : elle confirme le mot."},

      {t:'ana', h:"Jusqu'où",
       p:"Le mot qui dit où s'arrêter.",
       mots:[['On dit','Continuez {jusqu\'au} feu.'],['Aussi','Marchez {jusqu\'à la} pharmacie.'],['Le sens','allez, puis arrêtez-vous là',true]],
       say:"Continuez jusqu'au feu. Marchez jusqu'à la pharmacie.",
       note:"« Jusqu'à » suit la même règle que « à » : jusqu'<b>au</b> feu, jusqu'<b>à la</b> pharmacie, jusqu'<b>à l'</b>école."},

      {t:'ana', h:"Le repère",
       p:"Ce qu'on cherche des yeux en marchant.",
       mots:[['Le carrefour','C\'est {au coin}.'],['L\'ordre','{Après} le feu, à droite.'],['La distance','C\'est à {dix minutes} à pied.',true]],
       say:"C'est au coin. Après le feu, à droite. Dix minutes à pied.",
       note:"Un repère est plus sûr qu'un nom de rue : un feu, une pharmacie, une école se voient de loin."},

      {t:'labo', h:"Comprendre une direction",
       p:"Choisissez un mot et une situation.",
       axes:[
         {id:'p', lbl:'Quel mot ?', opts:[
           ['a','tout droit'],
           ['b','à droite'],
           ['c',"jusqu'à"],
           ['d','au coin'],
           ['e','après']]},
         {id:'q', lbl:'Où ?', opts:[['1','à pied'],['2',"à l'arrêt"]]}],
       out:{
         a1:{w:["Continuez tout droit sur le trottoir."], say:"Continuez tout droit sur le trottoir.", n:'sans tourner'},
         a2:{w:["L'arrêt est tout droit, devant l'école."], say:"L'arrêt est tout droit, devant l'école.", n:'un repère : l\'école'},
         b1:{w:["Tournez à droite au feu."], say:"Tournez à droite au feu.", n:'le feu dit où tourner'},
         b2:{w:["L'arrêt est à droite, de l'autre côté."], say:"L'arrêt est à droite, de l'autre côté.", n:'traverser la rue'},
         c1:{w:["Marchez jusqu'à la pharmacie."], say:"Marchez jusqu'à la pharmacie.", n:"jusqu'à la — féminin"},
         c2:{w:["Restez dans l'autobus jusqu'au parc."], say:"Restez dans l'autobus jusqu'au parc.", n:"jusqu'au — masculin"},
         d1:{w:["La bibliothèque est au coin."], say:"La bibliothèque est au coin.", n:'où deux rues se rencontrent'},
         d2:{w:["L'arrêt est au coin, près du dépanneur."], say:"L'arrêt est au coin, près du dépanneur.", n:'deux repères valent mieux qu\'un'},
         e1:{w:["Après le feu, tournez à gauche."], say:"Après le feu, tournez à gauche.", n:'d\'abord le feu, ensuite gauche'},
         e2:{w:["Descendez après le pont."], say:"Descendez après le pont.", n:'pour savoir quand sonner'},
       },
       note:"Écoutez chaque phrase deux fois : la première pour le sens, la seconde pour la répéter."},

      {t:'ex', h:"À écouter et à répéter",
       p:"Six phrases qu'on vous dira.",
       rows:[
         ["Vous continuez tout droit.","le début, presque toujours"],
         ["Jusqu'au feu.","où s'arrêter"],
         ["Après le feu, à droite.","l'ordre compte"],
         ["C'est au coin, à gauche.","l'arrivée"],
         ["C'est à dix minutes à pied.","la distance"],
         ["Vous ne pouvez pas la manquer.","ça veut dire : c'est très visible"],
       ]},

      {t:'piege', h:"Trois pièges à connaître",
       rows:[
         ["confondre droite et tout droit","deux mots très proches, deux sens différents",
          "<b>Tout droit</b> veut dire : ne tournez pas. <b>À droite</b> veut dire : tournez de ce côté. Dans le doute, montrez avec la main et demandez « comme ça ? »."],
         ["« jusqu'à le feu »","jusqu'au feu",
          "« Jusqu'à » se colle à l'article comme « à » : jusqu'<b>au</b> feu, jusqu'<b>à la</b> banque, jusqu'<b>à l'</b>école."],
         ["partir sans avoir compris","on marche dix minutes dans le mauvais sens",
          "Répétez ce que vous avez compris avant de partir. La personne corrigera tout de suite si c'est faux — c'est plus rapide que de revenir."],
       ]},

      {t:'check', h:"Est-ce que c'est clair maintenant ?",
       p:"Quatre questions rapides.",
       qs:[
         {q:"« Tout droit » veut dire…", opts:["ne pas tourner","tourner à droite"], ok:0,
          fb:"Tout droit : on continue dans la même direction."},
         {q:"« Jusqu'au feu » veut dire…", opts:["avant le feu","allez jusque-là, puis arrêtez"], ok:1,
          fb:"« Jusqu'à » dit où s'arrêter."},
         {q:"« C'est au coin » veut dire…", opts:["où deux rues se rencontrent","au bout de la ville"], ok:0,
          fb:"Le coin, c'est le carrefour de deux rues."},
         {q:"« Vous ne pouvez pas la manquer » veut dire…", opts:["c'est très visible","c'est fermé"], ok:0,
          fb:"C'est une façon de dire : vous allez la voir tout de suite."},
       ]},
    ]
  },

  t1repeter: {
    eye:'Mini-leçon', tit:"Répéter pour être sûr",
    blocs:[
      {t:'texte', h:"La technique qui remplace le vocabulaire",
       p:"Vous ne comprendrez pas tout, et ce n'est pas grave. Ce qui compte, c'est de <b>redire</b> ce que vous avez compris : « Tout droit, à droite au feu. C'est ça ? » La personne corrige tout de suite, ou confirme. En deux secondes, vous savez si vous pouvez partir.",
       note:"Les gens d'ici le font aussi entre eux, au téléphone et au travail. Ce n'est pas une marque de faiblesse : c'est de la prudence."},

      {t:'ana', h:"Faire ralentir",
       p:"Trois phrases, à savoir par cœur.",
       mots:[['Le plus utile','{Plus lentement}, s\'il vous plaît.'],['Pour réentendre','Vous pouvez {répéter} ?'],['Poliment','{Pardon}, je n\'ai pas compris.',true]],
       say:"Plus lentement, s'il vous plaît. Vous pouvez répéter ?",
       note:"Le problème n'est presque jamais le volume : c'est la vitesse. Demandez « plus lentement », pas « plus fort »."},

      {t:'ana', h:"Redire pour vérifier",
       p:"On répète, puis on demande confirmation.",
       mots:[['On redit','Tout droit, à droite au feu.'],['On vérifie','{C\'est ça ?}'],['Ou','{C\'est bien ça ?}',true]],
       say:"Tout droit, à droite au feu. C'est ça ?",
       note:"Redites seulement les mots importants — la direction et le repère. Pas besoin de refaire la phrase entière."},

      {t:'ana', h:"Quand on n'a saisi qu'un mot",
       p:"Répétez ce seul mot, avec une question dans la voix.",
       mots:[['On a entendu','« …au feu… »'],['On dit','{Au feu ?}'],['La personne reprend','oui, au feu, à droite',true]],
       say:"Au feu ? Oui, au feu, à droite.",
       note:"Un seul mot répété sur un ton de question suffit à relancer la personne. C'est la façon la plus rapide de se faire aider."},

      {t:'labo', h:"Que dites-vous ?",
       p:"Choisissez une difficulté et une réponse.",
       axes:[
         {id:'p', lbl:'Le problème ?', opts:[
           ['a','on parle trop vite'],
           ['b',"on n'a rien compris"],
           ['c','on a compris à moitié'],
           ['d','on veut vérifier']]},
         {id:'q', lbl:'Avec qui ?', opts:[['1','un inconnu dans la rue'],['2','une camarade de classe']]}],
       out:{
         a1:{w:["Plus lentement, s'il vous plaît."], say:"Plus lentement, s'il vous plaît.", n:'vouvoiement avec un inconnu'},
         a2:{w:["Plus lentement, s'il te plaît."], say:"Plus lentement, s'il te plaît.", n:'tutoiement entre camarades'},
         b1:{w:["Pardon, je n'ai pas compris. Vous pouvez répéter ?"], say:"Pardon, je n'ai pas compris. Vous pouvez répéter ?", n:'poli et clair'},
         b2:{w:["Je n'ai pas compris. Tu peux répéter ?"], say:"Je n'ai pas compris. Tu peux répéter ?", n:'plus court, entre camarades'},
         c1:{w:["Au feu ? Et après ?"], say:"Au feu ? Et après ?", n:'le mot saisi, puis la relance'},
         c2:{w:["Au feu ? Et après ?"], say:"Au feu ? Et après ?", n:'la même phrase marche partout'},
         d1:{w:["Tout droit, à droite au feu. C'est ça ?"], say:"Tout droit, à droite au feu. C'est ça ?", n:'redire, puis vérifier'},
         d2:{w:["Donc à droite au feu. C'est bien ça ?"], say:"Donc à droite au feu. C'est bien ça ?", n:'« donc » annonce le résumé'},
       },
       note:"Apprenez-en deux par cœur. Deux suffisent pour ne jamais rester bloqué."},

      {t:'ex', h:"À écouter et à répéter",
       p:"Six phrases à avoir toujours prêtes.",
       rows:[
         ["Pardon, vous pouvez répéter ?","la première à apprendre"],
         ["Plus lentement, s'il vous plaît.","c'est la vitesse, pas le volume"],
         ["Je n'ai pas compris.","une phrase honnête et suffisante"],
         ["Au feu ? Et après ?","un mot, puis la relance"],
         ["Tout droit, à droite au feu. C'est ça ?","redire, puis vérifier"],
         ["Merci beaucoup, madame.","toujours"],
       ]},

      {t:'piege', h:"Trois pièges à connaître",
       rows:[
         ["dire oui sans avoir compris","on repart, et on se perd",
          "Un « oui » poli coûte dix minutes de marche dans le mauvais sens. Dire « je n'ai pas compris » n'a jamais fâché personne."],
         ["demander « plus fort »","la personne crie, et c'est toujours trop vite",
          "Ce n'est presque jamais le volume qui manque. Demandez <b>plus lentement</b> : c'est ce dont vous avez réellement besoin."],
         ["répéter toute la phrase","on s'emmêle et on perd le fil",
          "Redites seulement les mots importants : la direction et le repère. « À droite au feu » suffit à faire vérifier."],
       ]},

      {t:'check', h:"Est-ce que c'est clair maintenant ?",
       p:"Quatre questions rapides.",
       qs:[
         {q:"On parle trop vite. On demande…", opts:["plus fort","plus lentement"], ok:1,
          fb:"C'est la vitesse qui gêne, pas le volume."},
         {q:"Redire ce qu'on a compris sert à…", opts:["se faire corriger tout de suite","être poli"], ok:0,
          fb:"La personne confirme ou corrige en deux secondes."},
         {q:"On n'a saisi qu'un mot. On dit…", opts:["rien, on part","« au feu ? »"], ok:1,
          fb:"Un seul mot, sur un ton de question, relance la personne."},
         {q:"Dire « je n'ai pas compris », c'est…", opts:["normal et utile","impoli"], ok:0,
          fb:"Tout le monde le dit, y compris les gens nés ici."},
       ]},
    ]
  },

  t2horaire: {
    eye:'Mini-leçon', tit:"L'heure de l'autobus",
    blocs:[
      {t:'texte', h:"Deux façons de dire la même heure",
       p:"À l'arrêt, l'écran affiche <b>8 h 15</b>. Mais la personne à côté de vous dira « huit heures et quart ». Les deux disent la même chose. L'écran et le papier emploient les chiffres ; les gens emploient <b>et quart</b>, <b>et demie</b>, <b>moins le quart</b>. Il faut comprendre les deux.",
       note:"Les horaires officiels vont jusqu'à 24 h : « 20 h 10 », c'est huit heures dix du soir."},

      {t:'ana', h:"Les quarts et la demie",
       p:"Trois expressions couvrent presque tout.",
       mots:[['8 h 15','huit heures {et quart}'],['8 h 30','huit heures {et demie}'],['8 h 45','neuf heures {moins le quart}',true]],
       say:"Huit heures et quart. Huit heures et demie. Neuf heures moins le quart.",
       note:"À 8 h 45, on annonce déjà <b>neuf</b> heures : moins le quart se compte sur l'heure qui vient."},

      {t:'ana', h:"Dans combien de temps",
       p:"L'autre question, aussi utile que l'heure.",
       mots:[['On demande','Il passe {à quelle heure} ?'],['Ou','Il passe {dans} combien de temps ?'],['On répond','{Dans} cinq minutes.',true]],
       say:"Il passe à quelle heure ? Dans cinq minutes.",
       note:"« Dans cinq minutes » compte à partir de maintenant. « À cinq heures » donne une heure fixe. Les deux ne se confondent pas."},

      {t:'ana', h:"La fréquence",
       p:"Une expression d'ici, à connaître.",
       mots:[['On dit','Il passe {aux quinze minutes}.'],['Le sens','8 h, 8 h 15, 8 h 30…'],['Le dernier','Le {dernier} passe à onze heures et quart.',true]],
       say:"Il passe aux quinze minutes. Le dernier passe à onze heures et quart.",
       note:"« Aux quinze minutes » veut dire : toutes les quinze minutes. Demandez toujours l'heure du <b>dernier</b> autobus si vous rentrez le soir."},

      {t:'labo', h:"Dire l'heure",
       p:"Choisissez une heure et une façon de le dire.",
       axes:[
         {id:'p', lbl:'Quelle heure ?', opts:[
           ['a','8 h 10'],
           ['b','8 h 15'],
           ['c','8 h 30'],
           ['d','8 h 45'],
           ['e','20 h 10']]},
         {id:'q', lbl:'Comment ?', opts:[['1',"comme l'écran"],['2','comme les gens']]}],
       out:{
         a1:{w:["8 h 10"], say:"Huit heures dix.", n:'les minutes se disent telles quelles'},
         a2:{w:["huit heures dix"], say:"Huit heures dix.", n:'ici, les deux se disent pareil'},
         b1:{w:["8 h 15"], say:"Huit heures quinze.", n:"sur l'écran de l'arrêt"},
         b2:{w:["huit heures et quart"], say:"Huit heures et quart.", n:'ce que dira la personne à côté'},
         c1:{w:["8 h 30"], say:"Huit heures trente.", n:"sur l'horaire papier"},
         c2:{w:["huit heures et demie"], say:"Huit heures et demie.", n:'la plus employée des trois'},
         d1:{w:["8 h 45"], say:"Huit heures quarante-cinq.", n:'les chiffres, sans surprise'},
         d2:{w:["neuf heures moins le quart"], say:"Neuf heures moins le quart.", n:'attention : on annonce neuf'},
         e1:{w:["20 h 10"], say:"Vingt heures dix.", n:"l'horaire officiel va jusqu'à 24 h"},
         e2:{w:["huit heures dix, le soir"], say:"Huit heures dix, le soir.", n:'« le soir » lève le doute'},
       },
       note:"Écoutez les deux colonnes pour la même heure. C'est en les entendant côte à côte qu'on les relie."},

      {t:'ex', h:"À écouter et à répéter",
       p:"Six phrases à l'arrêt d'autobus.",
       rows:[
         ["Est-ce que le 51 passe ici ?","d'abord, vérifier l'arrêt"],
         ["Il passe à quelle heure ?","la question de base"],
         ["Le prochain est à huit heures dix.","la réponse"],
         ["Dans cinq minutes.","à partir de maintenant"],
         ["Il passe aux quinze minutes.","la fréquence"],
         ["Le dernier passe à onze heures et quart.","à demander le soir"],
       ]},

      {t:'piege', h:"Trois pièges à connaître",
       rows:[
         ["confondre « à » et « dans »","« à cinq minutes » ou « dans cinq minutes » ?",
          "<b>Dans</b> cinq minutes : à partir de maintenant. <b>À</b> cinq heures : une heure fixe. « À cinq minutes » se dit seulement d'une distance : « c'est à cinq minutes à pied »."],
         ["« huit heures moins le quart » pour 8 h 45","neuf heures moins le quart",
          "Moins le quart se compte sur l'heure <b>qui vient</b>. À 8 h 45, l'heure qui vient est neuf heures."],
         ["oublier le dernier autobus","on se retrouve à pied, le soir",
          "Beaucoup de lignes s'arrêtent vers onze heures. Demandez l'heure du dernier passage avant de partir, pas après."],
       ]},

      {t:'check', h:"Est-ce que c'est clair maintenant ?",
       p:"Quatre questions rapides.",
       qs:[
         {q:"8 h 30 se dit aussi…", opts:["huit heures et demie","huit heures et quart"], ok:0,
          fb:"Et demie : trente minutes."},
         {q:"8 h 45 se dit aussi…", opts:["huit heures moins le quart","neuf heures moins le quart"], ok:1,
          fb:"Moins le quart se compte sur l'heure qui vient."},
         {q:"« Dans cinq minutes » veut dire…", opts:["à partir de maintenant","à cinq heures"], ok:0,
          fb:"« Dans » compte à partir du moment où on parle."},
         {q:"« Il passe aux quinze minutes » veut dire…", opts:["une fois, à 15 minutes","toutes les quinze minutes"], ok:1,
          fb:"8 h, 8 h 15, 8 h 30, 8 h 45…"},
       ]},
    ]
  },
};
