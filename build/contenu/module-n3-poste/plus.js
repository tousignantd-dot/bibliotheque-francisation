const PLUS = {
  prPhon: {
    eye:'Mini-leçon', tit:"Le « eu » fermé de deux et le « eu » ouvert de neuf",
    blocs:[
      {t:'texte', h:"Deux lettres, deux sons",
       p:"Les lettres <b>e</b> et <b>u</b> ensemble ne se disent pas toujours de la même façon. Il y a le <b>eu</b> de « d<b>eu</b>x », dit avec la bouche presque fermée et arrondie, et le <b>eu</b> de « n<b>eu</b>f », dit avec la bouche plus ouverte. Au bureau de poste, les deux reviennent sans arrêt : « deux kilos », « neuf heures », « un peu », « l'expéditeur ».",
       note:"Personne ne te corrigera si tu te trompes. Mais « deux heures » et « neuf heures » ne sont pas la même heure, et c'est là que ça compte."},

      {t:'ana', h:"Le son fermé — comme dans « deux »",
       p:"La bouche est petite et ronde, comme pour siffler. Le son est court et fermé.",
       mots:[['On écrit','d{eu}x'],['Aussi','j{eu}di, un p{eu}, mi{eu}x',true],['La bouche','arrondie, presque fermée']],
       say:"Deux, jeudi, un peu, mieux.",
       note:"On l'entend surtout quand le mot se termine par ce son : d<b>eu</b>x, un p<b>eu</b>, mi<b>eu</b>x, monsi<b>eu</b>r."},

      {t:'ana', h:"Le son ouvert — comme dans « neuf »",
       p:"La bouche s'ouvre davantage. Le son est plus large, et il y a toujours une consonne prononcée derrière.",
       mots:[['On écrit','n{eu}f'],['Aussi','une h{eu}re, l\'expédit{eu}r',true],['La bouche','plus ouverte, détendue']],
       say:"Neuf, une heure, l'expéditeur, plusieurs.",
       note:"C'est le son de tous les mots en <b>-eur</b> : l'expédit<b>eur</b>, le fact<b>eur</b>, une err<b>eur</b>, l'ordinat<b>eur</b>."},

      {t:'ana', h:"La règle qui décide presque toujours",
       p:"Regarde ce qu'il y a après les lettres e-u.",
       mots:[['Rien après, ou un e muet','d{eu}x, un p{eu}, jeudi : son fermé'],['Une consonne prononcée','n{eu}f, une h{eu}re, l\'expédit{eu}r : son ouvert',true],['Le cas des mots en -eur','toujours ouvert, sans exception utile']],
       say:"Deux. Neuf. Un peu. Une heure.",
       note:"Cette règle-là n'est pas parfaite dans toute la langue, mais elle règle tous les mots du bureau de poste."},

      {t:'labo', h:"Écoute les paires",
       p:"Choisis une paire et écoute la différence.",
       axes:[{id:'p', lbl:'Quelle paire ?', opts:[
         ['a','deux / neuf'],
         ['b','jeudi / une heure'],
         ['c','un peu / plusieurs'],
         ['d',"monsieur / l'expéditeur"],
         ['e','dans une phrase']]}],
       out:{
         a:{w:['d{eu}x / n{eu}f'], say:"Deux. Neuf.", n:'fermé, puis ouvert'},
         b:{w:['j{eu}di / une h{eu}re'], say:"Jeudi. Une heure.", n:'les deux mots des heures d\'ouverture'},
         c:{w:['un p{eu} / plusi{eu}rs'], say:"Un peu. Plusieurs.", n:'deux quantités, deux sons'},
         d:{w:["monsi{eu}r / l'expédit{eu}r"], say:"Monsieur. L'expéditeur.", n:'deux mots du comptoir'},
         e:{w:["« Deux colis, jeudi, à neuf heures. »"], say:"Deux colis, jeudi, à neuf heures.", n:'les deux sons deux fois chacun'},
       },
       note:"Écoute chaque paire deux fois : la première pour comprendre, la seconde en fermant les yeux."},

      {t:'ex', h:"À écouter et à répéter",
       p:"Six phrases du bureau de poste.",
       rows:[
         ["Ça ouvre à neuf heures, le jeudi.","les deux sons dans la même phrase"],
         ["Deux kilos et cent grammes.","son fermé"],
         ["L'expéditeur est en haut à gauche.","son ouvert"],
         ["Elle parle un peu vite pour moi.","son fermé"],
         ["Il y a plusieurs personnes devant moi.","son ouvert"],
         ["Merci monsieur, bonne journée.","son fermé"],
       ]},

      {t:'piege', h:"Trois pièges à connaître",
       rows:[
         ["confondre « deux » et « neuf »","dire « à deux heures » pour « à neuf heures »",
          "C'est le piège coûteux : tu arrives sept heures trop tard. Devant une heure, répète toujours : « Neuf heures ? Neuf ? »"],
         ["prononcer les lettres séparément","dire « dé-u » au lieu de « deux »",
          "Non : e et u ensemble font un seul son, jamais deux. La bouche ne bouge pas au milieu du mot."],
         ["oublier le son ouvert dans -eur","dire « l'expéditeu » avec la bouche fermée",
          "Tous les mots en <b>-eur</b> demandent la bouche ouverte, et le <b>r</b> se prononce : expédit<b>eur</b>, fact<b>eur</b>, err<b>eur</b>."],
       ]},

      {t:'check', h:"Est-ce que c'est clair maintenant ?",
       p:"Quatre questions rapides.",
       qs:[
         {q:"« Jeudi » a le son…", opts:["fermé, comme deux","ouvert, comme neuf"], ok:0,
          fb:"Rien de prononcé après : la bouche reste petite."},
         {q:"« Une heure » a le son…", opts:["fermé, comme deux","ouvert, comme neuf"], ok:1,
          fb:"Il y a un r prononcé derrière : la bouche s'ouvre."},
         {q:"« L'expéditeur » a le son…", opts:["fermé, comme deux","ouvert, comme neuf"], ok:1,
          fb:"Tous les mots en -eur sont ouverts."},
         {q:"Ce qui décide du son, c'est…", opts:["la lettre qui suit","la première lettre du mot"], ok:0,
          fb:"Une consonne prononcée derrière : son ouvert. Rien derrière : son fermé."},
       ]},

      {t:'revoir', h:"À retenir",
       p:"Deux mots repères, et rien d'autre : <b>deux</b> pour le son fermé, <b>neuf</b> pour le son ouvert. Devant un mot nouveau, regarde ce qu'il y a après les lettres e-u — une consonne prononcée, et la bouche s'ouvre."},
    ]
  },

  prPoli: {
    eye:'Mini-leçon', tit:"Je voudrais — la politesse au comptoir",
    blocs:[
      {t:'texte', h:"Le même verbe, deux façons de le dire",
       p:"« Je <b>veux</b> » et « je <b>voudrais</b> » veulent dire la même chose. Mais devant un comptoir, « je veux » sonne comme un ordre, et « je voudrais » sonne comme une demande. Cette petite différence-là décide de tout le reste de la conversation. Le programme de niveau 3 la nomme précisément : employer <b>vouloir</b>, <b>pouvoir</b> et <b>aimer</b> au conditionnel de politesse.",
       note:"Ce n'est pas une question de grammaire savante : c'est la première chose qu'on entend de toi, et c'est ce qui donne le ton."},

      {t:'ana', h:"Je voudrais — pour dire ce qu'on vient faire",
       p:"C'est la phrase qui ouvre presque toutes les démarches.",
       mots:[['On dit',"je {voudrais} envoyer ce colis"],['Aussi',"je {voudrais} des timbres",true],['Et',"je {voudrais} savoir combien ça coûte"]],
       say:"Je voudrais envoyer ce colis. Je voudrais des timbres.",
       note:"Après « je voudrais », on met soit un <b>nom</b> (des timbres), soit un <b>verbe à l'infinitif</b> (envoyer, savoir)."},

      {t:'ana', h:"J'aimerais — un peu plus doux encore",
       p:"On l'emploie surtout devant un achat ou un souhait.",
       mots:[['On dit',"j'{aimerais} un carnet de timbres"],['Aussi',"j'{aimerais} acheter une boîte",true],['Et',"j'{aimerais} savoir si c'est possible"]],
       say:"J'aimerais un carnet de timbres. J'aimerais acheter une boîte.",
       note:"« Je voudrais » et « j'aimerais » s'échangent presque toujours. Choisis celui qui te vient le plus vite."},

      {t:'ana', h:"Est-ce que je pourrais — pour demander la permission",
       p:"Quand tu ne sais pas si la chose est permise ou possible.",
       mots:[['On dit',"est-ce que je {pourrais} payer par carte"],['Aussi',"est-ce que je {pourrais} revenir demain",true],['Et',"est-ce que je {pourrais} voir les enveloppes"]],
       say:"Est-ce que je pourrais payer par carte ? Est-ce que je pourrais revenir demain ?",
       note:"La réponse attendue est oui ou non. C'est la différence avec « je voudrais », qui annonce une intention."},

      {t:'ana', h:"Est-ce que vous pouvez — pour demander un service",
       p:"Là, ce n'est plus toi qui fais quelque chose : c'est la personne devant toi.",
       mots:[['On dit',"est-ce que vous {pouvez} répéter"],['Aussi',"est-ce que vous {pouvez} parler moins vite",true],['Et',"est-ce que vous {pouvez} l'écrire"]],
       say:"Est-ce que vous pouvez répéter, s'il vous plaît ? Est-ce que vous pouvez parler moins vite ?",
       note:"Ces trois phrases-là valent de l'or quand on débute. Personne ne se fâche : au comptoir, on les entend tous les jours."},

      {t:'labo', h:"Construis ta demande",
       p:"Choisis une formule et ce que tu veux.",
       axes:[
         {id:'f', lbl:'Quelle formule ?', opts:[['a','Je voudrais'],['b',"J'aimerais"],['c','Est-ce que je pourrais']]},
         {id:'q', lbl:'Quoi ?', opts:[['1','envoyer ce colis'],['2','des timbres'],['3','payer par carte']]}],
       out:{
         a1:{w:["Je voudrais envoyer ce colis, s'il vous plaît."], say:"Je voudrais envoyer ce colis, s'il vous plaît.", n:'la phrase d\'ouverture la plus utile'},
         a2:{w:["Je voudrais des timbres, s'il vous plaît."], say:"Je voudrais des timbres, s'il vous plaît.", n:'un nom après la formule'},
         a3:{w:["Je voudrais payer par carte."], say:"Je voudrais payer par carte.", n:'correct, mais annonce plutôt qu\'elle demande'},
         b1:{w:["J'aimerais envoyer ce colis, s'il vous plaît."], say:"J'aimerais envoyer ce colis, s'il vous plaît.", n:'un peu plus doux'},
         b2:{w:["J'aimerais des timbres, s'il vous plaît."], say:"J'aimerais des timbres, s'il vous plaît.", n:'parfait pour un achat'},
         b3:{w:["J'aimerais payer par carte."], say:"J'aimerais payer par carte.", n:'poli, mais on attend une permission'},
         c1:{w:["Est-ce que je pourrais envoyer ce colis aujourd'hui ?"], say:"Est-ce que je pourrais envoyer ce colis aujourd'hui ?", n:'on demande si c\'est possible'},
         c2:{w:["Est-ce que je pourrais avoir des timbres ?"], say:"Est-ce que je pourrais avoir des timbres ?", n:'très poli'},
         c3:{w:["Est-ce que je pourrais payer par carte ?"], say:"Est-ce que je pourrais payer par carte ?", n:'la meilleure des neuf : la réponse est oui ou non'},
       },
       note:"Neuf phrases, toutes correctes. Choisis-en deux et apprends-les par cœur : elles ouvrent tous les comptoirs."},

      {t:'ex', h:"À écouter et à répéter",
       p:"Six phrases pour ouvrir une démarche.",
       rows:[
         ["Bonjour. Je voudrais envoyer ce colis, s'il vous plaît.","l'ouverture complète"],
         ["J'aimerais un carnet de timbres.","un achat"],
         ["Est-ce que je pourrais payer par carte de débit ?","une permission"],
         ["Est-ce que vous pouvez répéter, s'il vous plaît ?","un service"],
         ["Je voudrais savoir combien de temps ça prend.","une question polie"],
         ["Merci beaucoup. Bonne journée.","la sortie"],
       ]},

      {t:'piege', h:"Trois pièges à connaître",
       rows:[
         ["dire « je veux »","« Je veux un timbre. »",
          "Ce n'est pas faux, mais ça sonne dur, comme un enfant qui exige. Un seul mot change tout : <b>je voudrais</b>."],
         ["oublier « s'il vous plaît »","« Donnez-moi trois timbres. »",
          "Sans lui, la demande devient un ordre. Il se met à la fin, et il ne coûte rien."],
         ["dire « je voudrais avoir besoin »","mélanger deux formules polies",
          "Une seule à la fois : soit <b>je voudrais</b>, soit <b>j'aurais besoin de</b>. Les deux ensemble ne se disent pas."],
       ]},

      {t:'check', h:"Est-ce que c'est clair maintenant ?",
       p:"Quatre questions rapides.",
       qs:[
         {q:"Pour dire ce que tu viens faire, tu dis…", opts:["Je veux envoyer ce colis.","Je voudrais envoyer ce colis."], ok:1,
          fb:"« Je voudrais » : c'est la formule du comptoir."},
         {q:"Après « je voudrais », on peut mettre…", opts:["un nom ou un verbe à l'infinitif","seulement un nom"], ok:0,
          fb:"Je voudrais des timbres. Je voudrais envoyer."},
         {q:"Pour demander si c'est permis, tu dis…", opts:["Est-ce que je pourrais…","J'aimerais…"], ok:0,
          fb:"« Est-ce que je pourrais » appelle un oui ou un non."},
         {q:"Pour faire répéter, tu dis…", opts:["Est-ce que vous pouvez répéter ?","Je voudrais répéter."], ok:0,
          fb:"C'est la personne devant toi qui répète, pas toi."},
       ]},

      {t:'revoir', h:"À retenir",
       p:"Quatre phrases, apprises par cœur, suffisent pour ouvrir n'importe quelle démarche : <b>Je voudrais…</b>, <b>J'aimerais…</b>, <b>Est-ce que je pourrais…</b>, <b>Est-ce que vous pouvez répéter, s'il vous plaît ?</b>"},
    ]
  },

  t1quest: {
    eye:'Mini-leçon', tit:"Les cinq questions qui servent chaque fois",
    blocs:[
      {t:'texte', h:"Au comptoir, personne ne devine",
       p:"La préposée répond à ce qu'on lui demande, et à rien d'autre. Le prix n'est pas affiché, le délai non plus, et les deux changent selon le poids et la destination. C'est donc à toi de poser les questions. Il y en a cinq, toujours les mêmes, et elles se recopient d'une démarche à l'autre.",
       note:"Ce n'est pas de l'impolitesse de poser des questions : c'est ce que le comptoir attend de toi."},

      {t:'ana', h:"Combien — pour le prix",
       p:"La question la plus fréquente de toutes.",
       mots:[['On dit','{combien} est-ce que ça coûte'],['Plus court','ça coûte {combien}',true],['Et','{combien} ça fait en tout']],
       say:"Combien est-ce que ça coûte ? Ça coûte combien ?",
       note:"Les deux se disent. « Ça coûte combien ? » est plus courant à l'oral, au Québec comme ailleurs."},

      {t:'ana', h:"Combien de temps — pour le délai",
       p:"On demande des jours, jamais des heures.",
       mots:[['On dit','{combien de temps} est-ce que ça prend'],['Aussi','ça prend {combien de temps}',true],['Et','ça arrive {quand}']],
       say:"Combien de temps est-ce que ça prend ? Ça prend combien de temps ?",
       note:"Attention à ne pas confondre avec « combien » tout seul, qui demande un prix. Les deux mots de plus changent la réponse."},

      {t:'ana', h:"Est-ce que — pour une réponse oui ou non",
       p:"On le met au début, et le reste de la phrase ne bouge pas.",
       mots:[['On dit','{est-ce que} je peux payer par carte'],['Aussi','{est-ce que} le repérage est compris',true],['Et','{est-ce que} vous êtes ouverts samedi']],
       say:"Est-ce que je peux payer par carte ? Est-ce que le repérage est compris ?",
       note:"C'est le plus facile des cinq : tu prends une phrase normale et tu colles « est-ce que » devant."},

      {t:'ana', h:"Où et qu'est-ce que — pour l'endroit et pour la chose",
       p:"Deux questions courtes, très utiles au comptoir.",
       mots:[['Pour un endroit','{où} est-ce que je mets mon adresse'],['Pour une chose','{qu\'est-ce que} je dois écrire',true],['Et','{qu\'est-ce qu\'}il faut apporter']],
       say:"Où est-ce que je mets mon adresse ? Qu'est-ce qu'il faut apporter ?",
       note:"« Où » attend un endroit, « qu'est-ce que » attend une chose. Ne les mélange pas : la réponse ne servirait à rien."},

      {t:'labo', h:"Pose ta question",
       p:"Choisis ce que tu veux savoir.",
       axes:[
         {id:'q', lbl:'Tu veux savoir…', opts:[['a','le prix'],['b','le délai'],['c','si c\'est possible'],['d','quoi apporter']]},
         {id:'s', lbl:'Sur quoi ?', opts:[['1','le colis'],['2','le recommandé']]}],
       out:{
         a1:{w:["Combien est-ce que ça coûte, pour ce colis ?"], say:"Combien est-ce que ça coûte, pour ce colis ?", n:'le prix'},
         a2:{w:["Combien est-ce que ça coûte, le recommandé ?"], say:"Combien est-ce que ça coûte, le recommandé ?", n:'un prix de service'},
         b1:{w:["Combien de temps est-ce que ça prend, pour Calgary ?"], say:"Combien de temps est-ce que ça prend, pour Calgary ?", n:'le délai'},
         b2:{w:["Combien de temps est-ce que ça prend, le recommandé ?"], say:"Combien de temps est-ce que ça prend, le recommandé ?", n:'un délai de service'},
         c1:{w:["Est-ce que je peux envoyer ce colis aujourd'hui ?"], say:"Est-ce que je peux envoyer ce colis aujourd'hui ?", n:'oui ou non'},
         c2:{w:["Est-ce que le recommandé est plus cher ?"], say:"Est-ce que le recommandé est plus cher ?", n:'oui ou non'},
         d1:{w:["Qu'est-ce qu'il faut écrire sur la boîte ?"], say:"Qu'est-ce qu'il faut écrire sur la boîte ?", n:'une chose'},
         d2:{w:["Qu'est-ce qu'il faut apporter pour un recommandé ?"], say:"Qu'est-ce qu'il faut apporter pour un recommandé ?", n:'une chose'},
       },
       note:"Huit questions, toutes utilisables telles quelles au comptoir. Répète-les à voix haute avant d'y aller."},

      {t:'ex', h:"À écouter et à répéter",
       p:"Six questions du comptoir.",
       rows:[
         ["Combien est-ce que ça coûte, pour Calgary ?","le prix"],
         ["Combien de temps est-ce que ça prend ?","le délai"],
         ["Est-ce que je peux payer par carte de débit ?","oui ou non"],
         ["Où est-ce que j'écris mon adresse ?","un endroit"],
         ["Qu'est-ce qu'il faut apporter ?","une chose"],
         ["Est-ce que vous pouvez répéter le prix, s'il vous plaît ?","faire répéter"],
       ]},

      {t:'piege', h:"Trois pièges à connaître",
       rows:[
         ["demander « combien » pour un délai","« Combien pour Calgary ? » quand on veut savoir les jours",
          "« Combien » tout seul demande un prix. Pour les jours, il faut les trois mots : <b>combien de temps</b>."],
         ["oublier « est-ce que »","« Je peux payer par carte ? » dit trop vite",
          "Ce n'est pas faux à l'oral, mais l'intonation seule est difficile à réussir quand on débute. <b>Est-ce que</b> devant, et la question est claire."],
         ["poser deux questions à la fois","« Combien ça coûte et combien de temps ça prend ? »",
          "Une seule question, une seule réponse. Sinon tu retiendras la deuxième et tu oublieras la première."],
       ]},

      {t:'check', h:"Est-ce que c'est clair maintenant ?",
       p:"Quatre questions rapides.",
       qs:[
         {q:"Pour connaître le prix, tu demandes…", opts:["Combien est-ce que ça coûte ?","Combien de temps est-ce que ça prend ?"], ok:0,
          fb:"« Combien » seul : la réponse est en dollars."},
         {q:"Pour connaître le délai, tu demandes…", opts:["Combien ?","Combien de temps ?"], ok:1,
          fb:"Trois mots, et la réponse est en jours."},
         {q:"« Est-ce que » sert à obtenir…", opts:["un oui ou un non","un prix"], ok:0,
          fb:"La phrase derrière ne change pas d'ordre."},
         {q:"« Qu'est-ce qu'il faut apporter ? » attend…", opts:["une chose","un endroit"], ok:0,
          fb:"Pour un endroit, ce serait « où »."},
       ]},

      {t:'revoir', h:"À retenir",
       p:"Cinq questions, apprises une fois pour toutes : <b>Combien est-ce que ça coûte ?</b> · <b>Combien de temps est-ce que ça prend ?</b> · <b>Est-ce que…?</b> · <b>Où est-ce que…?</b> · <b>Qu'est-ce que…?</b> Elles servent au bureau de poste, mais aussi à la banque, à l'épicerie et au bureau de l'école."},
    ]
  },

  t1prix: {
    eye:'Mini-leçon', tit:"Comprendre un prix et un délai qu'on te dit vite",
    blocs:[
      {t:'texte', h:"Le problème n'est pas le prix, c'est la vitesse",
       p:"La préposée dit « vingt-deux dollars » en une seconde et demie. Tu comprends « deux » et « dollars », et il te manque le reste. Ce n'est pas un problème de vocabulaire : c'est un problème de vitesse. Il existe une façon simple de s'en sortir, et elle tient en une phrase : <b>on répète le prix à voix haute</b>.",
       note:"Répéter n'est pas impoli. Au comptoir, c'est même ce que fait la préposée elle-même quand elle veut être sûre."},

      {t:'ana', h:"Répéter pour vérifier",
       p:"Tu redis le chiffre, avec une intonation de question.",
       mots:[['On dit','{vingt-deux dollars} ?'],['Ou','vous avez dit {vingt-deux} ?',true],['Ou encore','{vingt-deux}, c\'est bien ça ?']],
       say:"Vingt-deux dollars ? Vous avez dit vingt-deux ?",
       note:"Trois façons, la même fonction. La plus courte marche très bien : le chiffre seul, avec la voix qui monte."},

      {t:'ana', h:"Faire répéter quand tu n'as rien saisi",
       p:"Deux phrases suffisent, et elles ne s'usent pas.",
       mots:[['On dit','est-ce que vous pouvez {répéter}'],['Ou','pouvez-vous parler {un peu moins vite}',true],['Ou encore','est-ce que vous pouvez {l\'écrire}']],
       say:"Est-ce que vous pouvez répéter, s'il vous plaît ? Pouvez-vous parler un peu moins vite ?",
       note:"La troisième est la plus efficace de toutes quand il s'agit d'un chiffre : un prix écrit ne se comprend pas de travers."},

      {t:'ana', h:"Les prix du bureau de poste, en toutes lettres",
       p:"Les chiffres qui reviennent, dits comme la préposée les dit.",
       mots:[['Un timbre à l\'unité','{un dollar quarante-quatre}'],['En carnet','{un dollar vingt-quatre} par timbre',true],['Le recommandé','{treize dollars quinze}, en plus']],
       say:"Un dollar quarante-quatre. Un dollar vingt-quatre. Treize dollars quinze.",
       note:"Au Québec, on dit souvent le prix sans le mot « et » : « treize quinze », « vingt-deux et cinquante »."},

      {t:'ana', h:"Les délais, en jours ouvrables",
       p:"Un « jour ouvrable », c'est un jour où on travaille : pas le samedi, pas le dimanche, pas les jours fériés.",
       mots:[['On entend','un ou deux {jours ouvrables}'],['Aussi','à peu près {une semaine}',true],['Et','ça dépend de la {destination}']],
       say:"Un ou deux jours ouvrables. À peu près une semaine.",
       note:"« Deux jours ouvrables » un vendredi veut dire mardi, pas dimanche. C'est la source d'erreur la plus fréquente."},

      {t:'labo', h:"Vérifie ce qu'on vient de te dire",
       p:"Choisis le prix entendu et la façon de vérifier.",
       axes:[
         {id:'p', lbl:'Tu as entendu…', opts:[['a','vingt-deux dollars'],['b','treize dollars quinze'],['c','huit dollars cinquante']]},
         {id:'m', lbl:'Comment vérifier ?', opts:[['1','en répétant'],['2','en faisant écrire']]}],
       out:{
         a1:{w:["Vingt-deux dollars ? C'est bien ça ?"], say:"Vingt-deux dollars ? C'est bien ça ?", n:'le plus rapide'},
         a2:{w:["Est-ce que vous pouvez l'écrire, s'il vous plaît ?"], say:"Est-ce que vous pouvez l'écrire, s'il vous plaît ?", n:'le plus sûr'},
         b1:{w:["Treize dollars quinze ? C'est bien ça ?"], say:"Treize dollars quinze ? C'est bien ça ?", n:'le prix du recommandé'},
         b2:{w:["Est-ce que vous pouvez me l'écrire ?"], say:"Est-ce que vous pouvez me l'écrire ?", n:'aucun risque d\'erreur'},
         c1:{w:["Huit dollars cinquante ? C'est bien ça ?"], say:"Huit dollars cinquante ? C'est bien ça ?", n:'le prix du mandat-poste'},
         c2:{w:["Est-ce que vous pouvez l'écrire sur le reçu ?"], say:"Est-ce que vous pouvez l'écrire sur le reçu ?", n:'et tu repars avec la preuve'},
       },
       note:"Six phrases, six façons de ne pas payer un prix qu'on n'a pas compris."},

      {t:'ex', h:"À écouter et à répéter",
       p:"Six phrases pour ne rien perdre.",
       rows:[
         ["Vingt-deux dollars ? C'est bien ça ?","répéter pour vérifier"],
         ["Est-ce que vous pouvez répéter, s'il vous plaît ?","faire répéter"],
         ["Pouvez-vous parler un peu moins vite ?","ralentir la personne"],
         ["Un ou deux jours ouvrables, c'est ça ?","vérifier un délai"],
         ["Est-ce que vous pouvez l'écrire ?","la solution des chiffres"],
         ["Alors : vingt-deux dollars, une semaine. Merci.","résumer avant de partir"],
       ]},

      {t:'piege', h:"Trois pièges à connaître",
       rows:[
         ["dire oui sans avoir compris","hocher la tête pour ne pas déranger",
          "C'est la pire des solutions : tu paies un prix que tu n'as pas choisi. Une question de trois secondes évite tout."],
         ["confondre « jours » et « jours ouvrables »","compter le samedi et le dimanche",
          "Un jour ouvrable est un jour de semaine. « Deux jours ouvrables » un vendredi, c'est mardi."],
         ["oublier que le poids change le prix","croire qu'un colis a un prix fixe",
          "Le prix dépend du poids, de la taille et de la distance. C'est pour ça qu'on pèse la boîte avant de le dire."],
       ]},

      {t:'check', h:"Est-ce que c'est clair maintenant ?",
       p:"Quatre questions rapides.",
       qs:[
         {q:"Tu n'as pas compris le prix. Tu…", opts:["dis oui pour ne pas déranger","demandes de répéter"], ok:1,
          fb:"On te le redira sans problème, chaque fois."},
         {q:"« Deux jours ouvrables », un vendredi, ça veut dire…", opts:["dimanche","mardi"], ok:1,
          fb:"Le samedi et le dimanche ne comptent pas."},
         {q:"La meilleure façon d'être sûr d'un chiffre…", opts:["le faire écrire","le répéter dans sa tête"], ok:0,
          fb:"Un chiffre écrit ne se comprend pas de travers."},
         {q:"Le prix d'un colis dépend…", opts:["du poids et de la distance","seulement de la boîte"], ok:0,
          fb:"C'est pour ça qu'on le pèse d'abord."},
       ]},

      {t:'revoir', h:"À retenir",
       p:"Une seule habitude à prendre, et elle vaut pour tous les comptoirs : <b>répète à voix haute le chiffre qu'on vient de te dire</b>. Si tu ne l'as pas saisi, demande de répéter ; si c'est important, demande qu'on l'écrive."},
    ]
  },

  t2contenu: {
    eye:'Mini-leçon', tit:"Dire ce qu'il y a dans la boîte",
    blocs:[
      {t:'texte', h:"Une question qui n'est pas une indiscrétion",
       p:"« Qu'est-ce qu'il y a dans la boîte ? » se demande à chaque envoi, à tout le monde. Ce n'est pas de la curiosité : certaines choses ne peuvent pas voyager, et d'autres coûtent plus cher parce qu'elles sont fragiles. Il faut donc savoir répondre en une phrase courte, et il y a quatre façons de le faire.",
       note:"Une réponse vague — « des affaires », « des choses » — fait poser une deuxième question. Nomme les objets."},

      {t:'ana', h:"Il y a — la façon la plus simple",
       p:"Elle marche pour une chose comme pour dix, au masculin comme au féminin.",
       mots:[['On dit','{il y a} des vêtements et un livre'],['Aussi','{il y a} deux chandails',true],['Et','{il y a} un cadre, c\'est fragile']],
       say:"Il y a des vêtements et un livre. Il y a deux chandails.",
       note:"À l'oral, on entend souvent « y'a » : « Y'a des vêtements. » C'est la même phrase, dite vite."},

      {t:'ana', h:"Contenir — le mot de la préposée",
       p:"C'est le verbe qu'on lit sur les formulaires et qu'on entend au comptoir.",
       mots:[['On dit','la boîte {contient} des vêtements'],['Aussi','ça {contient} un livre',true],['La question','qu\'est-ce que ça {contient} ?']],
       say:"La boîte contient des vêtements. Qu'est-ce que ça contient ?",
       note:"Tu n'as pas besoin de l'employer pour te faire comprendre, mais tu dois le reconnaître quand on te le dit."},

      {t:'ana', h:"C'est et ce sont — pour dire ce que c'est",
       p:"Une chose au singulier, plusieurs choses au pluriel.",
       mots:[['Au singulier','{c\'est} un cadeau pour mon frère'],['Au pluriel','{ce sont} des vêtements d\'hiver',true],['À l\'oral','on entend souvent « c\'est » dans les deux cas']],
       say:"C'est un cadeau pour mon frère. Ce sont des vêtements d'hiver.",
       note:"Au Québec, « c'est des vêtements » se dit couramment à l'oral. « Ce sont » reste la forme écrite."},

      {t:'ana', h:"Rien de — pour rassurer",
       p:"Les trois questions de sécurité reviennent chaque fois, dans le même ordre.",
       mots:[['On répond','{rien} de fragile'],['Aussi','{rien} de liquide',true],['Et','{rien} de dangereux']],
       say:"Rien de fragile. Rien de liquide. Rien de dangereux.",
       note:"Après « rien », il y a toujours <b>de</b>, puis un adjectif au masculin : rien de fragile, jamais « rien de fragiles »."},

      {t:'labo', h:"Réponds à la préposée",
       p:"Choisis ce qu'il y a dans ta boîte et comment le dire.",
       axes:[
         {id:'c', lbl:"Qu'est-ce qu'il y a ?", opts:[['a','des vêtements'],['b','un livre'],['c','de la vaisselle']]},
         {id:'f', lbl:'Comment le dire ?', opts:[['1','avec « il y a »'],['2','avec « c\'est »']]}],
       out:{
         a1:{w:["Il y a des vêtements. Rien de fragile."], say:"Il y a des vêtements. Rien de fragile.", n:'la réponse la plus fréquente'},
         a2:{w:["Ce sont des vêtements d'hiver."], say:"Ce sont des vêtements d'hiver.", n:'pluriel : ce sont'},
         b1:{w:["Il y a un livre et rien d'autre."], say:"Il y a un livre et rien d'autre.", n:'une seule chose'},
         b2:{w:["C'est un livre, un cadeau pour mon frère."], say:"C'est un livre, un cadeau pour mon frère.", n:'singulier : c\'est'},
         c1:{w:["Il y a de la vaisselle. C'est fragile."], say:"Il y a de la vaisselle. C'est fragile.", n:'à dire absolument'},
         c2:{w:["C'est de la vaisselle : attention, c'est fragile."], say:"C'est de la vaisselle : attention, c'est fragile.", n:'on écrira « fragile » sur la boîte'},
       },
       note:"Six réponses complètes. Prends celle qui correspond à ta boîte et apprends-la telle quelle."},

      {t:'ex', h:"À écouter et à répéter",
       p:"Six réponses de comptoir.",
       rows:[
         ["Il y a des vêtements et un livre.","la réponse type"],
         ["Rien de fragile, rien de liquide.","les questions de sécurité"],
         ["C'est un cadeau pour mon frère.","une chose"],
         ["Ce sont des livres d'école.","plusieurs choses"],
         ["Attention, il y a de la vaisselle : c'est fragile.","à signaler"],
         ["La boîte contient deux chandails.","le mot de la préposée"],
       ]},

      {t:'piege', h:"Trois pièges à connaître",
       rows:[
         ["répondre « des affaires »","« Il y a des affaires. »",
          "Ça ne dit rien, et on te reposera la question. Nomme les objets : des vêtements, un livre, un cadre."],
         ["oublier « de » après « rien »","« rien fragile »",
          "Il faut toujours le petit mot : <b>rien de</b> fragile, <b>rien de</b> liquide, <b>rien de</b> dangereux."],
         ["cacher qu'un objet est fragile","ne rien dire pour payer moins cher",
          "Si l'objet casse en route, tu ne seras pas remboursé. Dire « c'est fragile » protège ton envoi, ça ne le complique pas."],
       ]},

      {t:'check', h:"Est-ce que c'est clair maintenant ?",
       p:"Quatre questions rapides.",
       qs:[
         {q:"« Qu'est-ce qu'il y a dans la boîte ? » Tu réponds…", opts:["Des affaires.","Il y a des vêtements et un livre."], ok:1,
          fb:"On nomme les objets, en une phrase."},
         {q:"Après « rien », il faut…", opts:["de","que"], ok:0,
          fb:"Rien de fragile, rien de liquide."},
         {q:"Pour plusieurs choses, à l'écrit, on dit…", opts:["C'est des vêtements.","Ce sont des vêtements."], ok:1,
          fb:"« C'est » se dit à l'oral, « ce sont » s'écrit."},
         {q:"Il y a de la vaisselle dans ta boîte. Tu…", opts:["le dis tout de suite","ne dis rien"], ok:0,
          fb:"C'est fragile : le dire protège ton envoi."},
       ]},

      {t:'revoir', h:"À retenir",
       p:"Une phrase, et deux mots de plus : <b>Il y a…</b> pour nommer, et <b>rien de fragile</b> pour rassurer. Avec ces deux-là, la question du contenu est réglée en cinq secondes."},
    ]
  },

  t2pron: {
    eye:'Mini-leçon', tit:"Je vais le prendre — annoncer son choix en trois mots",
    blocs:[
      {t:'texte', h:"On ne répète pas ce qui vient d'être dit",
       p:"La préposée vient de dire « le colis standard, vingt-deux dollars ». Tu n'as pas besoin de répondre « je vais prendre le colis standard » : ce serait long et un peu bizarre. On dit <b>je vais le prendre</b>. Ce petit mot <b>le</b> remplace tout ce qui vient d'être nommé. Le programme de niveau 3 nomme ce point : les pronoms personnels compléments directs.",
       note:"Trois mots au lieu de six, et ça sonne comme quelqu'un qui a l'habitude. C'est la phrase la plus rentable du module."},

      {t:'ana', h:"Le — une chose masculine déjà nommée",
       p:"On dit « le » parce qu'on dirait « un colis », « un carnet », « un reçu ».",
       mots:[['On dit','je vais {le} prendre'],['Aussi','je vais {le} garder',true],['Et','je vais {le} payer par carte']],
       say:"Je vais le prendre. Je vais le garder.",
       note:"Le mot remplacé n'est pas répété : c'est justement à ça qu'il sert."},

      {t:'ana', h:"La — une chose féminine déjà nommée",
       p:"On dit « la » parce qu'on dirait « une enveloppe », « une boîte », « une lettre ».",
       mots:[['On dit','je vais {la} prendre'],['Aussi','je vais {la} poster demain',true],['Et','je vais {la} garder']],
       say:"Je vais la prendre. Je vais la poster demain.",
       note:"Devant une voyelle, « le » et « la » deviennent <b>l'</b> : je vais l'envoyer, je vais l'écrire."},

      {t:'ana', h:"Les — plusieurs choses déjà nommées",
       p:"Une seule forme, masculin comme féminin.",
       mots:[['On dit','je vais {les} prendre'],['Aussi','je vais {les} prendre tous les deux',true],['Et','je vais {les} envoyer ensemble']],
       say:"Je vais les prendre. Je vais les envoyer ensemble.",
       note:"C'est le plus facile des quatre : dès qu'il y a plusieurs choses, c'est « les »."},

      {t:'ana', h:"En — quand on dit un nombre",
       p:"Dès qu'un nombre apparaît, ce n'est plus « le », « la » ni « les » : c'est <b>en</b>.",
       mots:[['On dit','je vais {en} prendre trois'],['Aussi','je vais {en} prendre un',true],['Et','j\'{en} voudrais deux, s\'il vous plaît']],
       say:"Je vais en prendre trois. J'en voudrais deux, s'il vous plaît.",
       note:"Le nombre se met <b>à la fin</b> : je vais en prendre trois. Jamais « je vais en trois prendre »."},

      {t:'ana', h:"La place du petit mot",
       p:"Il se glisse devant le verbe qui compte, jamais après.",
       mots:[['On dit','je vais {le} prendre'],['On ne dit pas','je vais prendre {le}',true],['Avec deux verbes','il va devant le deuxième']],
       say:"Je vais le prendre. Je vais en prendre trois.",
       note:"Dans « je vais prendre », c'est <b>prendre</b> qui porte le sens : le petit mot se met juste devant lui."},

      {t:'labo', h:"Annonce ton choix",
       p:"Choisis ce qu'on vient de te proposer.",
       axes:[
         {id:'o', lbl:'On te propose…', opts:[['a','le colis standard'],['b','cette enveloppe-là'],['c','des timbres'],['d','les deux carnets']]},
         {id:'r', lbl:'Ta réponse', opts:[['1','oui, tout de suite'],['2','avec un nombre']]}],
       out:{
         a1:{w:["Le standard ? Oui, je vais le prendre."], say:"Le standard ? Oui, je vais le prendre.", n:'masculin : le'},
         a2:{w:["Je vais en prendre un seulement."], say:"Je vais en prendre un seulement.", n:'un nombre : en'},
         b1:{w:["Oui, je vais la prendre."], say:"Oui, je vais la prendre.", n:'féminin : la'},
         b2:{w:["Je vais en prendre trois, s'il vous plaît."], say:"Je vais en prendre trois, s'il vous plaît.", n:'un nombre : en'},
         c1:{w:["Oui, j'en voudrais, s'il vous plaît."], say:"Oui, j'en voudrais, s'il vous plaît.", n:'sans nombre, c\'est quand même « en »'},
         c2:{w:["Je vais en prendre douze."], say:"Je vais en prendre douze.", n:'un carnet, c\'est douze timbres'},
         d1:{w:["Oui, je vais les prendre."], say:"Oui, je vais les prendre.", n:'pluriel : les'},
         d2:{w:["Je vais en prendre deux."], say:"Je vais en prendre deux.", n:'un nombre : en'},
       },
       note:"Huit réponses, huit situations réelles du comptoir. Note celle qui te ressemble le plus."},

      {t:'ex', h:"À écouter et à répéter",
       p:"Six réponses très courtes.",
       rows:[
         ["Oui, je vais le prendre.","une chose masculine"],
         ["Je vais la prendre aussi.","une chose féminine"],
         ["Je vais les prendre tous les deux.","plusieurs choses"],
         ["Je vais en prendre trois.","avec un nombre"],
         ["J'en voudrais douze, s'il vous plaît.","un carnet complet"],
         ["Non merci, je vais le laisser.","refuser poliment"],
       ]},

      {t:'piege', h:"Trois pièges à connaître",
       rows:[
         ["mettre le petit mot après le verbe","« Je vais prendre le. »",
          "Il se met toujours <b>devant</b> le verbe : je vais <b>le</b> prendre. C'est l'ordre inverse de beaucoup d'autres langues."],
         ["dire « le » avec un nombre","« Je vais le prendre trois. »",
          "Dès qu'un nombre apparaît, c'est <b>en</b> : je vais <b>en</b> prendre trois."],
         ["répéter la chose au complet","« Je vais prendre le colis standard. »",
          "Ce n'est pas faux, mais on vient de le nommer. Trois mots suffisent, et ça sonne plus naturel."],
       ]},

      {t:'check', h:"Est-ce que c'est clair maintenant ?",
       p:"Quatre questions rapides.",
       qs:[
         {q:"« Le colis standard ? » Tu réponds…", opts:["Je vais le prendre.","Je vais prendre le."], ok:0,
          fb:"Le petit mot passe devant le verbe."},
         {q:"« Des enveloppes ? » Tu en veux trois. Tu dis…", opts:["Je vais les prendre trois.","Je vais en prendre trois."], ok:1,
          fb:"Un nombre : c'est « en »."},
         {q:"« Cette boîte-là ? » Tu réponds…", opts:["Je vais la prendre.","Je vais le prendre."], ok:0,
          fb:"Une boîte est féminine."},
         {q:"« Les deux carnets ? » Tu réponds…", opts:["Je vais les prendre.","Je vais la prendre."], ok:0,
          fb:"Plusieurs choses : « les »."},
       ]},

      {t:'revoir', h:"À retenir",
       p:"Quatre phrases de trois mots, et le comptoir est réglé : <b>je vais le prendre</b> · <b>je vais la prendre</b> · <b>je vais les prendre</b> · <b>je vais en prendre trois</b>. Le petit mot passe devant le verbe, et le nombre va à la fin."},
    ]
  },

  t2donnez: {
    eye:'Mini-leçon', tit:"Donnez-moi — demander sans donner d'ordre",
    blocs:[
      {t:'texte', h:"Un verbe qui commence la phrase",
       p:"Au comptoir, on entend souvent des phrases qui commencent par un verbe : « Donnez-moi un carnet », « Montrez-moi les enveloppes », « Répétez le prix ». C'est l'<b>impératif</b>, et le programme de niveau 3 le nomme. Ce qui décide si la phrase est polie ou brutale, ce n'est pas le verbe : c'est ce qu'on met autour.",
       note:"« Donnez-moi un carnet » tout sec sonne dur. « Donnez-moi un carnet, s'il vous plaît » est parfaitement poli."},

      {t:'ana', h:"La forme de base : le verbe, puis -moi",
       p:"On enlève le « vous » et on colle « moi » derrière, avec un petit trait.",
       mots:[['On dit','{donnez-moi} un carnet de timbres'],['Aussi','{montrez-moi} les enveloppes',true],['Et','{expliquez-moi} la différence']],
       say:"Donnez-moi un carnet de timbres. Montrez-moi les enveloppes.",
       note:"Le trait d'union est obligatoire à l'écrit : <b>donnez-moi</b>, jamais « donnez moi »."},

      {t:'ana', h:"Sans « moi », quand on ne demande rien pour soi",
       p:"Certains verbes n'ont pas besoin du « moi ».",
       mots:[['On dit','{répétez} le prix, s\'il vous plaît'],['Aussi','{attendez} un instant',true],['Et','{regardez} le code postal']],
       say:"Répétez le prix, s'il vous plaît. Attendez un instant.",
       note:"« Répétez-moi le prix » se dit aussi, mais « répétez » seul est plus léger et tout aussi correct."},

      {t:'ana', h:"Les trois mots qui rendent la phrase polie",
       p:"Ils ne changent pas le sens, ils changent le ton — et le ton est tout.",
       mots:[['Au début','{bonjour}, donnez-moi un carnet'],['À la fin','donnez-moi un carnet, {s\'il vous plaît}',true],['En partant','{merci beaucoup}, bonne journée']],
       say:"Bonjour. Donnez-moi un carnet, s'il vous plaît. Merci beaucoup.",
       note:"Trois mots, deux secondes, et la même demande devient agréable. C'est l'investissement le plus rentable du français."},

      {t:'ana', h:"La forme longue, pour une demande inhabituelle",
       p:"Quand ce que tu demandes sort de l'ordinaire, allonge la phrase.",
       mots:[['On dit','{est-ce que vous pourriez} me donner un carnet'],['Aussi','{est-ce que vous pourriez} vérifier',true],['Et','{est-ce que ce serait possible} de']],
       say:"Est-ce que vous pourriez me donner un carnet ? Est-ce que vous pourriez vérifier ?",
       note:"Plus la demande dérange, plus la phrase s'allonge. C'est une règle qui vaut dans presque toutes les langues."},

      {t:'labo', h:"Formule ta demande",
       p:"Choisis ce que tu veux et le ton.",
       axes:[
         {id:'d', lbl:'Tu demandes…', opts:[['a','un carnet de timbres'],['b','trois enveloppes'],['c','le reçu']]},
         {id:'t', lbl:'Quel ton ?', opts:[['1','court et poli'],['2','très poli']]}],
       out:{
         a1:{w:["Donnez-moi un carnet de timbres, s'il vous plaît."], say:"Donnez-moi un carnet de timbres, s'il vous plaît.", n:'la forme normale du comptoir'},
         a2:{w:["Est-ce que vous pourriez me donner un carnet de timbres ?"], say:"Est-ce que vous pourriez me donner un carnet de timbres ?", n:'plus long, plus doux'},
         b1:{w:["Donnez-moi trois enveloppes, s'il vous plaît."], say:"Donnez-moi trois enveloppes, s'il vous plaît.", n:'le nombre devant la chose'},
         b2:{w:["Est-ce que je pourrais avoir trois enveloppes ?"], say:"Est-ce que je pourrais avoir trois enveloppes ?", n:'une autre façon, très employée'},
         c1:{w:["Donnez-moi le reçu, s'il vous plaît."], say:"Donnez-moi le reçu, s'il vous plaît.", n:'on le demande toujours'},
         c2:{w:["Est-ce que je pourrais avoir un reçu ?"], say:"Est-ce que je pourrais avoir un reçu ?", n:'même chose, en plus doux'},
       },
       note:"Six demandes. Les trois de gauche suffisent au quotidien ; celles de droite servent quand tu demandes un effort."},

      {t:'ex', h:"À écouter et à répéter",
       p:"Six demandes de comptoir.",
       rows:[
         ["Donnez-moi un carnet de timbres, s'il vous plaît.","la demande type"],
         ["Montrez-moi les enveloppes, s'il vous plaît.","voir avant d'acheter"],
         ["Répétez le prix, s'il vous plaît.","faire répéter"],
         ["Expliquez-moi la différence, s'il vous plaît.","comprendre avant de choisir"],
         ["Donnez-moi le reçu, s'il vous plaît.","repartir avec la preuve"],
         ["Est-ce que vous pourriez vérifier l'adresse ?","une demande inhabituelle"],
       ]},

      {t:'piege', h:"Trois pièges à connaître",
       rows:[
         ["oublier le trait d'union","écrire « donnez moi »",
          "À l'écrit, il est obligatoire : <b>donnez-moi</b>, <b>montrez-moi</b>, <b>expliquez-moi</b>."],
         ["oublier « s'il vous plaît »","« Donnez-moi trois timbres. »",
          "Sans lui, la phrase est un ordre. Avec lui, c'est une demande. C'est le seul mot qui change quelque chose."],
         ["dire « donne-moi » à un inconnu","tutoyer la préposée",
          "Au comptoir, on vouvoie : c'est <b>donnez</b>-moi, pas « donne-moi ». « Donne-moi » se réserve à la famille et aux amis."],
       ]},

      {t:'check', h:"Est-ce que c'est clair maintenant ?",
       p:"Quatre questions rapides.",
       qs:[
         {q:"À la préposée, tu dis…", opts:["Donne-moi un carnet.","Donnez-moi un carnet."], ok:1,
          fb:"On vouvoie au comptoir."},
         {q:"Ce qui rend la demande polie, c'est…", opts:["« s'il vous plaît » à la fin","le ton de la voix seulement"], ok:0,
          fb:"Trois mots, et tout change."},
         {q:"À l'écrit, on écrit…", opts:["donnez moi","donnez-moi"], ok:1,
          fb:"Le trait d'union est obligatoire."},
         {q:"Pour une demande inhabituelle, tu dis…", opts:["Est-ce que vous pourriez…","Donnez-moi…"], ok:0,
          fb:"Plus la demande dérange, plus la phrase s'allonge."},
       ]},

      {t:'revoir', h:"À retenir",
       p:"Une formule et un mot : <b>Donnez-moi… , s'il vous plaît.</b> Le verbe d'abord, « moi » avec un trait d'union, et « s'il vous plaît » à la fin. Si la demande sort de l'ordinaire, allonge : <b>Est-ce que vous pourriez…?</b>"},
    ]
  },

  t2adresse: {
    eye:'Mini-leçon', tit:"Écrire une adresse sur une boîte",
    blocs:[
      {t:'texte', h:"Deux adresses, deux places",
       p:"Sur un colis, il y a toujours <b>deux</b> adresses. Celle de la personne qui envoie — l'<b>expéditeur</b> — va en haut à gauche, en petit. Celle de la personne qui reçoit — le <b>destinataire</b> — va au milieu, en plus gros. Si la boîte ne se rend pas, elle revient à l'adresse du haut : c'est pour ça qu'on l'écrit.",
       note:"Beaucoup de gens oublient l'adresse de l'expéditeur. Un colis sans elle, qui ne se rend pas, est un colis perdu."},

      {t:'ana', h:"L'ordre des lignes, toujours le même",
       p:"Quatre lignes, dans cet ordre, sans jamais changer.",
       mots:[['Ligne 1','le nom de la {personne}'],['Ligne 2','le {numéro} et la {rue}, puis l\'appartement',true],['Ligne 3','la {ville}, la {province}, le {code postal}']],
       say:"Le nom. Le numéro et la rue. La ville, la province et le code postal.",
       note:"Au Québec, la province s'écrit entre parenthèses juste après la ville : Québec (Québec), Calgary (Alberta)."},

      {t:'ana', h:"Le code postal, six caractères",
       p:"Trois lettres et trois chiffres, qui alternent, avec une espace au milieu.",
       mots:[['La forme','une lettre, un chiffre, une lettre'],['Puis','une espace, puis trois autres',true],['Exemple','G1J 3K7 · T2M 3P4']],
       say:"G, un, J, trois, K, sept.",
       note:"Il se dit lettre par lettre et chiffre par chiffre, lentement. Personne ne dit « G mille cent quarante-trois »."},

      {t:'ana', h:"Épeler quand on te le demande",
       p:"Ton nom et ta rue ne seront pas compris du premier coup : c'est normal.",
       mots:[['On dit','B, E, R, R, A, D, A'],['Pour aider','B comme dans {Bernard}',true],['Et','deux R, comme dans {arriver}']],
       say:"B, E, R, R, A, D, A. B comme dans Bernard.",
       note:"Donner un mot repère pour chaque lettre difficile — B comme Bernard, D comme Denise — évite tous les malentendus."},

      {t:'ana', h:"Écrire lisiblement, en lettres détachées",
       p:"L'écriture attachée se lit mal, surtout les chiffres.",
       mots:[['On écrit','en {lettres détachées}'],['Le stylo','noir ou bleu foncé, jamais pâle',true],['Le ruban','jamais par-dessus l\'adresse']],
       say:"En lettres détachées, au stylo noir.",
       note:"Du ruban transparent collé sur l'adresse fait briller le papier et empêche la machine de la lire. On colle à côté."},

      {t:'labo', h:"Place chaque élément",
       p:"Choisis une adresse et une place.",
       axes:[
         {id:'a', lbl:'Quelle adresse ?', opts:[['a',"celle de l'expéditeur"],['b','celle du destinataire']]},
         {id:'p', lbl:'Quelle ligne ?', opts:[['1','le nom'],['2','la rue'],['3','la ville et le code']]}],
       out:{
         a1:{w:["Yassine Berrada, en haut à gauche, en petit."], say:"Yassine Berrada, en haut à gauche, en petit.", n:"l'expéditeur, ligne 1"},
         a2:{w:["2145, 8e Avenue, appartement 3."], say:"Deux mille cent quarante-cinq, huitième Avenue, appartement trois.", n:"l'expéditeur, ligne 2"},
         a3:{w:["Québec (Québec) G1J 3K7."], say:"Québec, Québec, G, un, J, trois, K, sept.", n:"l'expéditeur, ligne 3"},
         b1:{w:["Karim Berrada, au milieu, en plus gros."], say:"Karim Berrada, au milieu, en plus gros.", n:'le destinataire, ligne 1'},
         b2:{w:["780, 14e Rue Nord-Ouest."], say:"Sept cent quatre-vingts, quatorzième Rue Nord-Ouest.", n:'le destinataire, ligne 2'},
         b3:{w:["Calgary (Alberta) T2M 3P4."], say:"Calgary, Alberta, T, deux, M, trois, P, quatre.", n:'le destinataire, ligne 3'},
       },
       note:"Six lignes, et l'adresse complète est faite. Recopie-les sur une feuille avant d'écrire sur la boîte."},

      {t:'ex', h:"À écouter et à répéter",
       p:"Six phrases pour dicter une adresse.",
       rows:[
         ["Mon adresse est le 2145, 8e Avenue, appartement 3.","dire son adresse"],
         ["À Québec, code postal G1J 3K7.","la ville et le code"],
         ["Mon nom s'écrit B, E, R, R, A, D, A.","épeler"],
         ["B comme dans Bernard, avec deux R.","aider à comprendre"],
         ["Est-ce que je mets mon adresse en haut à gauche ?","vérifier la place"],
         ["Est-ce que vous pouvez répéter le code postal ?","faire répéter un code"],
       ]},

      {t:'piege', h:"Trois pièges à connaître",
       rows:[
         ["oublier l'adresse de l'expéditeur","n'écrire que celle du destinataire",
          "Si le colis ne se rend pas, il n'a nulle part où revenir. C'est ainsi qu'un colis se perd pour de bon."],
         ["coller du ruban sur l'adresse","protéger le papier avec du ruban transparent",
          "Le ruban fait briller le papier et la machine ne lit plus rien. Colle le ruban <b>à côté</b>, jamais dessus."],
         ["dire le code postal comme un nombre","« G mille cent quarante-trois »",
          "Il se dit caractère par caractère : G, un, J, trois, K, sept. Lentement, avec une pause au milieu."],
       ]},

      {t:'check', h:"Est-ce que c'est clair maintenant ?",
       p:"Quatre questions rapides.",
       qs:[
         {q:"L'adresse de l'expéditeur va…", opts:["en haut à gauche","au milieu"], ok:0,
          fb:"Au milieu, c'est celle du destinataire."},
         {q:"Un code postal canadien a…", opts:["six caractères","cinq chiffres"], ok:0,
          fb:"Trois lettres et trois chiffres qui alternent."},
         {q:"Le ruban transparent se colle…", opts:["sur l'adresse, pour la protéger","à côté de l'adresse"], ok:1,
          fb:"Sur l'adresse, la machine ne lit plus rien."},
         {q:"Si le colis ne se rend pas, il revient…", opts:["à l'expéditeur","au bureau de poste le plus proche"], ok:0,
          fb:"D'où l'importance de l'adresse du haut."},
       ]},

      {t:'revoir', h:"À retenir",
       p:"Deux adresses, deux places : l'<b>expéditeur</b> en haut à gauche, le <b>destinataire</b> au milieu. Trois lignes chacune — le nom, la rue, puis la ville avec le code postal. En lettres détachées, et pas de ruban par-dessus."},
    ]
  },

  t3avis: {
    eye:'Mini-leçon', tit:"Le carton d'avis : ce qu'il dit et ce qu'il ne dit pas",
    blocs:[
      {t:'texte', h:"Un carton qui ne parle pas fort",
       p:"Tu rentres du travail et il y a un petit carton dans ta boîte aux lettres. Il ne ressemble pas à une facture, il n'a l'air de rien, et beaucoup de gens le mettent de côté. C'est une erreur : ce carton veut dire qu'un <b>colis t'attend</b>, et qu'il ne t'attendra pas indéfiniment.",
       note:"Le carton s'appelle un <b>avis de livraison</b>. On le laisse quand personne ne peut recevoir ou signer le colis."},

      {t:'ana', h:"Ce que le carton te dit",
       p:"Quatre renseignements, toujours les mêmes.",
       mots:[['Où','le {bureau de poste} où le colis attend'],['À partir de quand','une {date} et une {heure}',true],['Jusqu\'à quand','{quinze jours}, pas un de plus']],
       say:"Le bureau de poste, la date, l'heure, et quinze jours.",
       note:"L'heure compte : un colis avisé le matin n'est souvent prêt qu'à partir de treize heures le lendemain."},

      {t:'ana', h:"Ce qu'il faut apporter — les deux, chaque fois",
       p:"Un seul des deux ne suffit pas.",
       mots:[['Le premier','le {carton} lui-même'],['Le second','une {pièce d\'identité} avec photo',true],['Par exemple','un {permis de conduire}, un {passeport}']],
       say:"Le carton et une pièce d'identité avec photo.",
       note:"Le nom sur la pièce d'identité doit être celui du carton. Sans ça, on ne te remettra pas le colis."},

      {t:'ana', h:"Le compte à rebours de quinze jours",
       p:"Il commence le jour où le carton est laissé.",
       mots:[['Après cinq jours','un deuxième carton, l\'{avis final}'],['Après quinze jours','le colis {retourne à l\'expéditeur}',true],['Et ensuite','il faut tout recommencer, et payer deux fois']],
       say:"Après cinq jours, un avis final. Après quinze jours, le colis retourne à l'expéditeur.",
       note:"Quinze <b>jours civils</b>, samedis et dimanches compris — pas quinze jours ouvrables. C'est plus court qu'on ne pense."},

      {t:'ana', h:"Ce que le carton ne dit pas",
       p:"Deux choses qu'il faut demander toi-même au comptoir.",
       mots:[['Il ne dit pas','ce qu\'il y a {dans le colis}'],['Il ne dit pas','qui l\'a {envoyé}, pas toujours',true],['Il ne dit pas','si quelqu\'un d\'autre peut le {ramasser}']],
       say:"Est-ce que quelqu'un d'autre peut le ramasser à ma place ?",
       note:"Cette dernière question se pose souvent : la réponse dépend du service, et elle se demande au comptoir."},

      {t:'labo', h:"Que faire avec ton carton ?",
       p:"Choisis ta situation.",
       axes:[
         {id:'s', lbl:'Ta situation', opts:[['a','tu as le carton'],['b','tu as perdu le carton'],['c','tu ne peux pas y aller']]},
         {id:'q', lbl:'Tu veux…', opts:[['1','le colis'],['2','plus de temps']]}],
       out:{
         a1:{w:["Bonjour. Je viens chercher un colis. Voici mon avis et mon permis de conduire."], say:"Bonjour. Je viens chercher un colis. Voici mon avis et mon permis de conduire.", n:'la phrase complète'},
         a2:{w:["Est-ce que vous pouvez le garder plus longtemps ?"], say:"Est-ce que vous pouvez le garder plus longtemps ?", n:'la réponse est souvent non'},
         b1:{w:["J'ai perdu mon avis. Est-ce que vous pouvez chercher avec mon adresse ?"], say:"J'ai perdu mon avis. Est-ce que vous pouvez chercher avec mon adresse ?", n:'la pièce d\'identité reste obligatoire'},
         b2:{w:["Jusqu'à quand est-ce que vous le gardez ?"], say:"Jusqu'à quand est-ce que vous le gardez ?", n:'pour connaître ta date limite'},
         c1:{w:["Est-ce que quelqu'un d'autre peut venir le chercher à ma place ?"], say:"Est-ce que quelqu'un d'autre peut venir le chercher à ma place ?", n:'à demander avant d\'envoyer quelqu\'un'},
         c2:{w:["Quelles sont vos heures d'ouverture le samedi ?"], say:"Quelles sont vos heures d'ouverture le samedi ?", n:'souvent la vraie solution'},
       },
       note:"Six phrases, six situations. La dernière est celle qui règle le plus de problèmes."},

      {t:'ex', h:"À écouter et à répéter",
       p:"Six phrases pour aller chercher un colis.",
       rows:[
         ["Bonjour. Je viens chercher un colis.","l'ouverture"],
         ["Voici mon avis et ma pièce d'identité.","les deux, ensemble"],
         ["Jusqu'à quand est-ce que vous le gardez ?","connaître sa date limite"],
         ["Est-ce que quelqu'un d'autre peut le ramasser ?","préparer un plan B"],
         ["Quelles sont vos heures d'ouverture le samedi ?","trouver un moment possible"],
         ["Merci beaucoup. Bonne journée.","la sortie"],
       ]},

      {t:'piege', h:"Trois pièges à connaître",
       rows:[
         ["laisser traîner le carton","« J'irai la semaine prochaine. »",
          "Quinze jours civils, c'est deux fins de semaine et onze jours de travail. Ça passe vite, et après, le colis repart."],
         ["n'apporter que le carton","oublier la pièce d'identité",
          "Il faut les <b>deux</b>. Sans pièce d'identité avec photo, on ne te remettra rien, même avec le carton en main."],
         ["croire que quinze jours ouvrables","compter seulement les jours de semaine",
          "Ce sont quinze <b>jours civils</b> : les samedis et les dimanches comptent. Deux semaines pleines, pas trois."],
       ]},

      {t:'check', h:"Est-ce que c'est clair maintenant ?",
       p:"Quatre questions rapides.",
       qs:[
         {q:"Le carton dans ta boîte aux lettres veut dire…", opts:["un colis t'attend au bureau de poste","tu dois de l'argent"], ok:0,
          fb:"C'est un avis de livraison."},
         {q:"Pour ramasser le colis, il faut apporter…", opts:["le carton seulement","le carton et une pièce d'identité"], ok:1,
          fb:"Les deux, chaque fois."},
         {q:"Le colis est gardé…", opts:["quinze jours","deux mois"], ok:0,
          fb:"Quinze jours civils, puis retour à l'expéditeur."},
         {q:"Après cinq jours, tu reçois…", opts:["un avis final","rien du tout"], ok:0,
          fb:"Un deuxième carton, pour rappeler."},
       ]},

      {t:'revoir', h:"À retenir",
       p:"Un carton dans la boîte aux lettres veut dire <b>un colis t'attend</b>. Apporte le <b>carton</b> et une <b>pièce d'identité avec photo</b>, et vas-y dans les <b>quinze jours</b>. Passé ce délai, le colis retourne à celui qui l'a envoyé."},
    ]
  },

  t3dem: {
    eye:'Mini-leçon', tit:"Ce carton-là — montrer ce qu'on a devant soi",
    blocs:[
      {t:'texte', h:"Le mot qui remplace le doigt",
       p:"Au comptoir, tu poses une boîte et tu dis « ce colis-là ». Tu montres un carton et tu dis « ce carton-là ». Ces petits mots — <b>ce</b>, <b>cet</b>, <b>cette</b>, <b>ces</b> — servent à désigner une chose qu'on a devant soi. Le programme de niveau 3 les nomme : les déterminants démonstratifs.",
       note:"Sans eux, il faut décrire l'objet en entier. Avec eux, un mot suffit : la personne regarde ce que tu montres."},

      {t:'ana', h:"Ce — devant un mot masculin",
       p:"On l'emploie quand on dirait « un colis », « un carton », « un reçu ».",
       mots:[['On dit','{ce} colis'],['Aussi','{ce} carton, {ce} reçu',true],['Et','{ce} timbre-là']],
       say:"Ce colis. Ce carton. Ce reçu.",
       note:"C'est le plus court des quatre, et le plus fréquent au comptoir."},

      {t:'ana', h:"Cet — devant une voyelle",
       p:"Le mot reste masculin, mais on ajoute un t pour que ça se prononce.",
       mots:[['On dit','{cet} avis'],['Aussi','{cet} envoi',true],['On ne dit pas','« ce avis »']],
       say:"Cet avis. Cet envoi.",
       note:"« Ce avis » est impossible à prononcer : deux voyelles collées. Le t se glisse au milieu pour aider la bouche."},

      {t:'ana', h:"Cette — devant un mot féminin",
       p:"On l'emploie quand on dirait « une boîte », « une lettre », « une enveloppe ».",
       mots:[['On dit','{cette} boîte'],['Aussi','{cette} enveloppe, {cette} lettre',true],['Et','{cette} adresse-là']],
       say:"Cette boîte. Cette enveloppe. Cette lettre.",
       note:"« Cet » et « cette » se prononcent presque pareil. À l'écrit, c'est le genre du mot qui décide."},

      {t:'ana', h:"Ces — devant un pluriel",
       p:"Une seule forme, masculin comme féminin.",
       mots:[['On dit','{ces} timbres'],['Aussi','{ces} enveloppes',true],['Et','{ces} boîtes-là']],
       say:"Ces timbres. Ces enveloppes.",
       note:"Ne pas confondre avec <b>ses</b>, qui veut dire « à lui » ou « à elle ». Ça se prononce pareil et ça ne s'écrit pas pareil."},

      {t:'ana', h:"Le « -là » qu'on ajoute au Québec",
       p:"Il se colle au nom, avec un trait d'union, et il insiste.",
       mots:[['On dit','{ce carton-là}'],['Aussi','{cette boîte-là}, {ces timbres-là}',true],['Ce que ça ajoute','celui-là et pas un autre']],
       say:"Ce carton-là. Cette boîte-là. Ces timbres-là.",
       note:"On l'entend partout au Québec, à l'oral comme à l'écrit familier. Il est correct et il rend la phrase plus claire."},

      {t:'labo', h:"Montre ce que tu tiens",
       p:"Choisis l'objet et ce que tu veux en dire.",
       axes:[
         {id:'o', lbl:'Quel objet ?', opts:[['a','un carton'],['b','un avis'],['c','une boîte'],['d','des timbres']]},
         {id:'p', lbl:'Tu veux…', opts:[['1',"en parler"],['2','poser une question']]}],
       out:{
         a1:{w:["J'ai trouvé ce carton-là dans ma boîte aux lettres."], say:"J'ai trouvé ce carton-là dans ma boîte aux lettres.", n:'masculin : ce'},
         a2:{w:["Qu'est-ce que ce carton-là veut dire ?"], say:"Qu'est-ce que ce carton-là veut dire ?", n:'la question de départ du défi'},
         b1:{w:["Cet avis dit que mon colis est arrivé."], say:"Cet avis dit que mon colis est arrivé.", n:"voyelle : cet"},
         b2:{w:["Est-ce que cet avis est encore bon ?"], say:"Est-ce que cet avis est encore bon ?", n:'à cause des quinze jours'},
         c1:{w:["Je voudrais envoyer cette boîte-là."], say:"Je voudrais envoyer cette boîte-là.", n:'féminin : cette'},
         c2:{w:["Combien coûte cette boîte-là ?"], say:"Combien coûte cette boîte-là ?", n:'on montre en parlant'},
         d1:{w:["Je vais prendre ces timbres-là."], say:"Je vais prendre ces timbres-là.", n:'pluriel : ces'},
         d2:{w:["Est-ce que ces timbres-là sont encore bons ?"], say:"Est-ce que ces timbres-là sont encore bons ?", n:'une vraie question de comptoir'},
       },
       note:"Huit phrases, toutes dites en montrant quelque chose. Le geste et le mot vont ensemble."},

      {t:'ex', h:"À écouter et à répéter",
       p:"Six phrases pour montrer et demander.",
       rows:[
         ["J'ai trouvé ce carton-là dans ma boîte aux lettres.","masculin"],
         ["Cet avis dit que mon colis est arrivé.","devant une voyelle"],
         ["Je voudrais envoyer cette boîte-là.","féminin"],
         ["Est-ce que ces timbres-là sont encore bons ?","pluriel"],
         ["Combien coûte cette enveloppe-là ?","une question de prix"],
         ["Ce colis-là part aujourd'hui ?","vérifier un départ"],
       ]},

      {t:'piege', h:"Trois pièges à connaître",
       rows:[
         ["dire « ce avis »","oublier le t devant une voyelle",
          "Impossible à prononcer. C'est <b>cet</b> avis, <b>cet</b> envoi, <b>cet</b> appartement."],
         ["confondre « ces » et « ses »","écrire « ses timbres » pour « ces timbres »",
          "<b>Ces</b> montre ce qu'on a devant soi. <b>Ses</b> dit à qui c'est. Ça se prononce pareil, mais ça ne veut pas dire la même chose."],
         ["oublier le trait d'union du -là","écrire « ce carton là »",
          "Le <b>-là</b> se colle au nom avec un trait d'union : ce carton<b>-là</b>, cette boîte<b>-là</b>."],
       ]},

      {t:'check', h:"Est-ce que c'est clair maintenant ?",
       p:"Quatre questions rapides.",
       qs:[
         {q:"Devant « avis », on dit…", opts:["ce avis","cet avis"], ok:1,
          fb:"Deux voyelles collées : le t s'ajoute."},
         {q:"Devant « boîte », on dit…", opts:["ce boîte","cette boîte"], ok:1,
          fb:"Une boîte est féminine."},
         {q:"« Ces timbres » veut dire…", opts:["les timbres que je montre","les timbres qui sont à lui"], ok:0,
          fb:"« À lui », ce serait « ses timbres »."},
         {q:"Le « -là » du Québec s'écrit…", opts:["ce carton là","ce carton-là"], ok:1,
          fb:"Avec un trait d'union, collé au nom."},
       ]},

      {t:'revoir', h:"À retenir",
       p:"Quatre mots pour montrer : <b>ce</b> colis · <b>cet</b> avis · <b>cette</b> boîte · <b>ces</b> timbres. Et au Québec, ajoute <b>-là</b> pour insister : ce carton-là, celui que tu tiens dans ta main."},
    ]
  },

  t3suivre: {
    eye:'Mini-leçon', tit:"Déménager sans perdre son courrier",
    blocs:[
      {t:'texte', h:"Le courrier ne suit pas tout seul",
       p:"Quand tu déménages, personne ne prévient la poste à ta place. Les lettres continuent d'arriver à l'ancienne adresse, et la personne qui habite là maintenant n'a aucune raison de te les apporter. Il existe un service qui règle ça : on fait <b>suivre</b> son courrier à la nouvelle adresse, pendant un temps donné.",
       note:"Ça se demande au comptoir ou sur Internet, et ça se paie. Ce n'est pas gratuit, mais ça coûte moins cher qu'un chèque perdu."},

      {t:'ana', h:"Ce que le service fait",
       p:"Il prend ton courrier à l'ancienne adresse et le réexpédie à la nouvelle.",
       mots:[['Ça suit','les {lettres} ordinaires'],['Ça suit','le {courrier recommandé}',true],['Ça suit','les {magazines} auxquels tu es abonné']],
       say:"Les lettres, le courrier recommandé et les magazines.",
       note:"C'est déjà l'essentiel : la banque, l'école, l'employeur et le gouvernement écrivent par lettre ordinaire."},

      {t:'ana', h:"Ce que le service ne fait pas",
       p:"Deux exceptions importantes, à connaître avant de compter dessus.",
       mots:[['Ça ne suit pas','les {colis}'],['Ça ne suit pas','les {enveloppes prépayées}',true],['Donc','pour tes commandes, change l\'adresse toi-même']],
       say:"Les colis ne suivent pas. Les enveloppes prépayées non plus.",
       note:"C'est le point que tout le monde découvre trop tard : une commande envoyée à l'ancienne adresse y reste."},

      {t:'ana', h:"Combien de temps, et quand le demander",
       p:"Le service a une durée maximale, et un bon moment pour être demandé.",
       mots:[['Durée maximale','{douze mois}'],['Quand le demander','{avant} le déménagement, pas après',true],['Combien de temps avant','quelques {jours} suffisent']],
       say:"Jusqu'à douze mois. Avant le déménagement, pas après.",
       note:"Demandé après coup, le service ne rattrape pas ce qui est déjà parti à l'ancienne adresse."},

      {t:'ana', h:"Ce que la poste ne fait pas à ta place",
       p:"Faire suivre son courrier n'est pas un changement d'adresse officiel.",
       mots:[['À prévenir toi-même','ta {banque}, ton {employeur}'],['Aussi','l\'{école} des enfants, le {gouvernement}',true],['Le service','te donne le {temps} de le faire']],
       say:"La banque, l'employeur, l'école, le gouvernement.",
       note:"Le service fait suivre pendant douze mois : c'est une année pour prévenir tout le monde, pas une solution définitive."},

      {t:'labo', h:"Demande le service au comptoir",
       p:"Choisis ta question.",
       axes:[
         {id:'q', lbl:'Tu veux savoir…', opts:[['a','comment le demander'],['b','combien de temps'],['c','ce qui suit']]},
         {id:'t', lbl:'Ton ton', opts:[['1','direct'],['2','très poli']]}],
       out:{
         a1:{w:["Je déménage le premier juillet. Comment est-ce que je fais suivre mon courrier ?"], say:"Je déménage le premier juillet. Comment est-ce que je fais suivre mon courrier ?", n:'la question de départ'},
         a2:{w:["Est-ce que je pourrais faire suivre mon courrier à ma nouvelle adresse ?"], say:"Est-ce que je pourrais faire suivre mon courrier à ma nouvelle adresse ?", n:'plus doux'},
         b1:{w:["Pendant combien de temps est-ce que ça dure ?"], say:"Pendant combien de temps est-ce que ça dure ?", n:'la réponse est douze mois'},
         b2:{w:["Est-ce que je pourrais savoir combien de temps ça dure ?"], say:"Est-ce que je pourrais savoir combien de temps ça dure ?", n:'la même question, en plus long'},
         c1:{w:["Est-ce que les colis suivent aussi ?"], say:"Est-ce que les colis suivent aussi ?", n:'la question qui sauve une commande'},
         c2:{w:["Est-ce que vous pouvez m'expliquer ce qui suit et ce qui ne suit pas ?"], say:"Est-ce que vous pouvez m'expliquer ce qui suit et ce qui ne suit pas ?", n:'la plus complète des six'},
       },
       note:"Six phrases. La question sur les colis est celle qu'on oublie et qu'il faut poser."},

      {t:'ex', h:"À écouter et à répéter",
       p:"Six phrases pour un déménagement.",
       rows:[
         ["Je déménage le premier juillet.","annoncer"],
         ["Est-ce que je pourrais faire suivre mon courrier ?","demander le service"],
         ["Pendant combien de temps est-ce que ça dure ?","la durée"],
         ["Est-ce que les colis suivent aussi ?","la question importante"],
         ["Voici mon ancienne adresse et ma nouvelle adresse.","donner les deux"],
         ["Qu'est-ce qu'il faut apporter pour faire la demande ?","se préparer"],
       ]},

      {t:'piege', h:"Trois pièges à connaître",
       rows:[
         ["croire que les colis suivent","commander quelque chose à l'ancienne adresse",
          "Ils ne suivent pas. Change l'adresse toi-même sur tous les sites où tu commandes, avant de déménager."],
         ["demander le service après le déménagement","« Je le ferai quand je serai installé. »",
          "Ce qui est déjà parti à l'ancienne adresse n'est pas rattrapé. Demande-le quelques jours <b>avant</b>."],
         ["croire que c'est un changement d'adresse officiel","ne prévenir personne d'autre",
          "La poste fait suivre, elle ne prévient pas ta banque ni ton employeur. Ces douze mois servent à le faire toi-même."],
       ]},

      {t:'check', h:"Est-ce que c'est clair maintenant ?",
       p:"Quatre questions rapides.",
       qs:[
         {q:"Le service fait suivre…", opts:["les lettres, mais pas les colis","tout, y compris les colis"], ok:0,
          fb:"Les colis ne suivent jamais."},
         {q:"La durée maximale est de…", opts:["douze mois","trois mois"], ok:0,
          fb:"Une année complète, au maximum."},
         {q:"Le meilleur moment pour le demander…", opts:["avant le déménagement","le mois suivant"], ok:0,
          fb:"Après, ce qui est parti est parti."},
         {q:"Ta banque est prévenue…", opts:["par la poste","par toi"], ok:1,
          fb:"Le service fait suivre, il ne prévient personne."},
       ]},

      {t:'revoir', h:"À retenir",
       p:"Trois chiffres et une exception : <b>douze mois</b> au maximum, à demander <b>avant</b> le déménagement, et les <b>colis ne suivent pas</b>. Pendant cette année-là, préviens toi-même ta banque, ton employeur et l'école."},
    ]
  },
};
