const PLUS = {
  prPhon: {
    eye:'Mini-leçon', tit:"Le « an » de content et le « in » de voisin",
    blocs:[
      {t:'texte', h:"Deux sons qui passent par le nez",
       p:"Le français a des voyelles <b>nasales</b> : l'air sort par le nez en même temps que par la bouche. Deux d'entre elles se croisent sans arrêt dans un escalier d'immeuble : le <b>an</b> de « cont<b>en</b>t » et le <b>in</b> de « vois<b>in</b> ». Beaucoup de langues n'en ont aucune, et l'oreille les confond au début.",
       note:"Ce n'est pas un détail de prononciation : « un voisin » et « un voisant » ne veulent rien dire de pareil, et l'interlocuteur cherche le mot au lieu d'écouter la suite."},

      {t:'ana', h:"Le son « an » — la bouche grande ouverte",
       p:"C'est le son de « content », « comment », « en avant ».",
       mots:[['On écrit','cont{en}t'],['Aussi écrit','an : appartem{an}… non : appartem{ent}',true],['Aussi écrit','am, em devant b et p : ch{am}bre']],
       say:"Comment allez-vous ? Je suis content.",
       note:"La mâchoire descend, les lèvres restent plates. C'est le son le plus ouvert des deux."},

      {t:'ana', h:"Le son « in » — la bouche étirée",
       p:"C'est le son de « voisin », « matin », « invitation ».",
       mots:[['On écrit','vois{in}'],['Aussi écrit','ain, ein : dem{ain} · pl{ein}',true],['Aussi écrit','un : lundi · quelqu{un}']],
       say:"Mon voisin part le matin.",
       note:"Les coins de la bouche s'écartent, comme pour sourire. Si tu souris en le disant, tu es dans le bon son."},

      {t:'ana', h:"Le mot qui contient les deux",
       p:"« Une invitation » traverse les deux sons en trois syllabes.",
       mots:[['On dit','{in}-vi-ta-ti{on}'],['Au début','le son de voisin',true],['À la fin','le son de content, arrondi : « on »']],
       say:"J'ai glissé une invitation sous la porte.",
       note:"Retiens ce mot comme mot repère du module : il te redonne les deux sons chaque fois que tu le prononces."},

      {t:'labo', h:"Écoute les paires",
       p:"Choisis une paire et écoute la différence.",
       axes:[{id:'p', lbl:'Quelle paire ?', opts:[
         ['a','content / voisin'],
         ['b','comment / demain'],
         ['c','en avant / le matin'],
         ['d','appartement / invitation'],
         ['e','dans une phrase']]}],
       out:{
         a:{w:['cont{en}t / vois{in}'], say:"Content, voisin.", n:'la bouche s\'ouvre, puis s\'étire'},
         b:{w:['comm{en}t / dem{ain}'], say:"Comment, demain.", n:'deux écritures différentes, deux sons différents'},
         c:{w:['{en} av{an}t / le mat{in}'], say:"En avant, le matin.", n:'trois fois « an », puis « in »'},
         d:{w:['appartem{ent} / {in}vitation'], say:"Un appartement, une invitation.", n:'les deux mots de l\'immeuble'},
         e:{w:['« Mon voisin est content de son appartement. »'], say:"Mon voisin est content de son appartement.", n:'les deux sons dans la même phrase'},
       },
       note:"Écoute chaque paire deux fois : la première pour comprendre, la seconde en fermant les yeux."},

      {t:'ex', h:"À écouter et à répéter",
       p:"Six phrases de l'escalier.",
       rows:[
         ["Mon voisin part travailler le matin.","in trois fois"],
         ["Je suis content de vous connaître.","an deux fois"],
         ["L'escalier monte en avant de l'immeuble.","an trois fois"],
         ["J'ai reçu une invitation ce matin.","in puis an"],
         ["Comment s'appelle le concierge ?","an au début et à la fin"],
         ["Demain, quelqu'un va venir.","in trois fois"],
       ]},

      {t:'piege', h:"Trois pièges à connaître",
       rows:[
         ["prononcer la lettre n","dire « voi-si-ne » pour « voisin »",
          "Dans « voisin », le n ne se prononce pas tout seul : il rend la voyelle nasale, puis il disparaît. La bouche ne se ferme pas à la fin. Attention : « une voisine » se prononce bien avec le n — le e final le réveille."],
         ["croire que « en » se dit « en »","le mot « content »",
          "Les lettres e et n ensemble se disent « an ». C'est l'écriture la plus fréquente du son, et la plus trompeuse pour qui lit avant d'écouter."],
         ["mélanger « un » et « une »","« un voisin » et « une voisine »",
          "« Un » se dit avec le son de voisin ; « une » se dit avec un u bien net et un e à la fin. Ce sont deux mots que rien ne rapproche à l'oreille."],
       ]},

      {t:'check', h:"Est-ce que c'est clair maintenant ?",
       p:"Quatre questions rapides.",
       qs:[
         {q:"« Voisin » a le son…", opts:["an","in"], ok:1,
          fb:"Les coins de la bouche s'écartent, comme pour sourire."},
         {q:"« Content » a le son…", opts:["an","in"], ok:0,
          fb:"Les lettres e et n ensemble se disent « an »."},
         {q:"Dans ces sons, l'air passe…", opts:["par la bouche seulement","par le nez aussi"], ok:1,
          fb:"C'est pour ça qu'on les appelle des voyelles nasales."},
         {q:"Dans « une voisine », le n…", opts:["se prononce","ne se prononce pas"], ok:0,
          fb:"Le e final réveille le n : voi-si-ne. Sans lui, le son devient nasal."},
       ]},

      {t:'revoir', h:"À retenir",
       p:"Deux mots repères, et rien d'autre : <b>content</b> pour le son « an », <b>voisin</b> pour le son « in ». Quand tu hésites devant un mot nouveau, dis-le à côté de l'un des deux et écoute lequel se ressemble."},
    ]
  },

  prPresente: {
    eye:'Mini-leçon', tit:"Se présenter, et présenter quelqu'un",
    blocs:[
      {t:'texte', h:"Deux gestes différents, deux phrases différentes",
       p:"Se <b>présenter</b>, c'est donner son propre nom. <b>Présenter quelqu'un</b>, c'est donner le nom d'une troisième personne aux deux autres. Dans un immeuble, les deux arrivent dans la même minute : tu dis ton nom, puis celui de la personne qui est avec toi.",
       note:"Dans un escalier, on ajoute presque toujours l'étage au nom : « Rachid Belkacem, du troisième. » C'est ce qui permet à l'autre de te replacer le lendemain."},

      {t:'ana', h:"Donner son nom",
       p:"Trois façons, de la plus complète à la plus rapide.",
       mots:[['La phrase entière','{Je m\'appelle} Rachid Belkacem.'],['Plus court','Rachid Belkacem, du troisième.',true],['La question','Comment vous appelez-vous ?']],
       say:"Bonjour, je m'appelle Rachid Belkacem, du troisième.",
       note:"« Je m'appelle » se prononce en trois morceaux collés : jeu-ma-pelle. Le e de « je » disparaît presque."},

      {t:'ana', h:"Dire où on habite dans l'immeuble",
       p:"Le renseignement que le voisin attend juste après le nom.",
       mots:[['On dit','{J\'habite au} troisième.'],['Avec le numéro','J\'habite au 3A.',true],['Depuis quand','Je suis arrivé il y a trois semaines.']],
       say:"J'habite au troisième, au 3A.",
       note:"Le h de « habite » ne se prononce pas : on entend « ja-bite ». C'est pour ça qu'on écrit « j'habite » et non « je habite »."},

      {t:'ana', h:"Présenter quelqu'un d'autre",
       p:"Trois formules, de la plus polie à la plus simple.",
       mots:[['Poli','{Je vous présente} ma sœur, Leïla.'],['Avec quelqu\'un qu\'on tutoie','Je te présente ma sœur.',true],['Tous les jours','Voici ma sœur. · C\'est ma sœur.']],
       say:"Madame Lachapelle, je vous présente ma sœur.",
       note:"On commence par nommer la personne à qui on parle — « Madame Lachapelle, … » — puis on présente. C'est l'ordre poli."},

      {t:'ana', h:"Répondre quand on vous présente",
       p:"Un seul mot suffit, et il s'écrit de deux façons.",
       mots:[['Un homme répond','{Enchanté.}'],['Une femme répond','{Enchantée.}',true],['On peut ajouter','Enchantée. Bienvenue dans l\'immeuble.']],
       say:"Bonjour, enchantée !",
       note:"Le son est exactement le même dans les deux cas. Seule l'écriture change, et cela ne s'entend jamais."},

      {t:'labo', h:"Qui présente qui ?",
       p:"Choisis la personne et la formule.",
       axes:[
         {id:'p', lbl:'Tu présentes qui ?', opts:[['a','ta sœur'],['b','ton mari'],['c','ton garçon'],['d','ta voisine']]},
         {id:'f', lbl:'Quelle formule ?', opts:[['1','polie'],['2','de tous les jours']]}],
       out:{
         a1:{w:["Je vous présente ma sœur, Leïla."], say:"Je vous présente ma sœur, Leïla.", n:'avec quelqu\'un qu\'on vouvoie'},
         a2:{w:["Voici ma sœur, Leïla."], say:"Voici ma sœur, Leïla.", n:'plus court, tout aussi correct'},
         b1:{w:["Je vous présente mon mari, Karim."], say:"Je vous présente mon mari, Karim.", n:'le lien familial vient avant le prénom'},
         b2:{w:["C'est mon mari, Karim."], say:"C'est mon mari, Karim.", n:'« c\'est » sert pour une personne comme pour une chose'},
         c1:{w:["Je vous présente mon garçon, Sami. Il a quatre ans."], say:"Je vous présente mon garçon, Sami. Il a quatre ans.", n:'avec un enfant, on donne souvent l\'âge'},
         c2:{w:["Voici Sami, mon petit garçon."], say:"Voici Sami, mon petit garçon.", n:'le prénom peut passer en premier'},
         d1:{w:["Je vous présente madame Lachapelle, ma voisine du deuxième."], say:"Je vous présente madame Lachapelle, ma voisine du deuxième.", n:'l\'étage complète la présentation'},
         d2:{w:["C'est madame Lachapelle, du deuxième."], say:"C'est madame Lachapelle, du deuxième.", n:'la forme qu\'on entend dans l\'escalier'},
       },
       note:"Huit phrases, toutes correctes, toutes utilisables telles quelles dès demain matin."},

      {t:'ex', h:"À écouter et à répéter",
       p:"Six phrases de première rencontre.",
       rows:[
         ["Bonjour, je m'appelle Rachid Belkacem.","le nom en premier"],
         ["J'habite au troisième, au 3A.","l'étage juste après"],
         ["Nous sommes arrivés il y a trois semaines.","depuis quand"],
         ["Madame Lachapelle, je vous présente ma sœur.","la formule polie"],
         ["Voici mon petit garçon. Il a quatre ans.","la formule courte"],
         ["Bonjour, enchantée. Bienvenue dans l'immeuble.","la réponse"],
       ]},

      {t:'piege', h:"Trois pièges à connaître",
       rows:[
         ["dire « mon nom est »","« Mon nom est Rachid. »",
          "Cette phrase se comprend, mais elle ne se dit pas en français courant. On dit « je m'appelle » ou simplement son nom."],
         ["oublier le mot « me »","« Je appelle Rachid. »",
          "Le verbe est « s'appeler » : je m'appelle, tu t'appelles, il s'appelle. Le petit mot devant n'est jamais facultatif."],
         ["présenter sans nommer le lien","« Voici Leïla. »",
          "Correct, mais l'autre ne sait pas qui c'est. Ajoute toujours le lien : ma sœur, mon mari, ma voisine, mon garçon."],
       ]},

      {t:'check', h:"Est-ce que c'est clair maintenant ?",
       p:"Quatre questions rapides.",
       qs:[
         {q:"On dit…", opts:["Je appelle Rachid.","Je m'appelle Rachid."], ok:1,
          fb:"Le verbe est « s'appeler » : le petit mot « m' » fait partie du verbe."},
         {q:"Pour présenter poliment sa sœur…", opts:["Je vous présente ma sœur.","Ma sœur est là."], ok:0,
          fb:"« Je vous présente » est la formule qu'on emploie avec quelqu'un qu'on vouvoie."},
         {q:"Une femme répond…", opts:["Enchanté.","Enchantée."], ok:1,
          fb:"Le son est le même ; seule l'écriture change."},
         {q:"Après son nom, dans un immeuble, on donne…", opts:["son étage","son âge"], ok:0,
          fb:"L'étage permet au voisin de te replacer le lendemain."},
       ]},

      {t:'revoir', h:"À retenir",
       p:"Trois phrases seulement : <b>Je m'appelle…</b> pour toi, <b>J'habite au…</b> pour ta porte, <b>Je vous présente…</b> pour la personne qui t'accompagne. Et un seul mot pour répondre : <b>enchanté</b> ou <b>enchantée</b>."},
    ]
  },

  t1perm: {
    eye:'Mini-leçon', tit:'Demander la permission, du plus simple au plus poli',
    blocs:[
      {t:'texte', h:"Une phrase avant vaut mieux qu'une chicane après",
       p:"Dans un immeuble, la cour, la remise, le corridor et la corde à linge appartiennent à tout le monde en même temps. Personne n'en est propriétaire, et personne n'a le droit de tout prendre. La phrase qui règle cela est courte : <b>Est-ce que je peux… ?</b>",
       note:"Demander la permission n'est pas se rabaisser. C'est la façon normale de partager un espace, et c'est ce qui fait qu'on te répondra oui la prochaine fois."},

      {t:'ana', h:"La question de tous les jours",
       p:"Courte, directe, parfaitement correcte entre voisins.",
       mots:[['On dit','{Est-ce que je peux} mettre mon vélo dans la remise ?'],['Le verbe','pouvoir : je peux, tu peux, il peut',true],['Encore plus court','Je peux mettre mon vélo dans la remise ?']],
       say:"Est-ce que je peux mettre mon vélo dans la remise ?",
       note:"« Est-ce que » ne veut rien dire tout seul : c'est le signal qu'une question commence. À l'oral, beaucoup de gens le laissent tomber et montent seulement la voix à la fin."},

      {t:'ana', h:"La même question, en plus poli",
       p:"Un seul morceau change, et tout s'adoucit.",
       mots:[['On dit','{Est-ce que je pourrais} l\'accrocher au mur ?'],['La marque','le -rais de « pourrais »',true],['Aussi','Je voudrais… · Est-ce qu\'il serait possible de…']],
       say:"Est-ce que je pourrais l'accrocher au mur du fond ?",
       note:"C'est la forme à employer avec quelqu'un qu'on connaît peu, ou quand on demande quelque chose d'un peu plus gros que d'habitude."},

      {t:'ana', h:"Demander la permission de quelqu'un d'autre",
       p:"Plus rare, plus formelle, très utile devant le concierge.",
       mots:[['On dit','{Est-ce que vous permettez} que je passe par la cour ?'],['Le nom','la {permission}',true],['Ce qu\'on en fait','on la demande, on la donne, on la refuse']],
       say:"Est-ce que vous permettez que je passe par la cour ?",
       note:"« Il faut la permission du concierge » : là, le mot désigne le droit lui-même, pas la phrase qui le demande."},

      {t:'ana', h:"Ce qui n'est pas permis",
       p:"La façon d'annoncer une interdiction sans se fâcher.",
       mots:[['On dit','{Ce n\'est pas permis} de bloquer la sortie.'],['Aussi','Je préfère que non. · J\'aimerais mieux pas.',true],['Avec la raison','…parce que c\'est la sortie de secours.']],
       say:"Ce n'est pas permis de bloquer la sortie de secours.",
       note:"En français du Québec, un refus poli s'accompagne presque toujours de sa raison. Sans raison, il sonne sec."},

      {t:'labo', h:"La même demande, deux niveaux de politesse",
       p:"Choisis ce que tu demandes et à qui.",
       axes:[
         {id:'d', lbl:'Tu demandes quoi ?', opts:[['a','la remise'],['b','la corde à linge'],['c','la clé'],['d','passer par la cour']]},
         {id:'n', lbl:'À qui ?', opts:[['1','une voisine que tu connais'],['2','le concierge, que tu connais peu']]}],
       out:{
         a1:{w:["Est-ce que je peux mettre mon vélo dans la remise ?"], say:"Est-ce que je peux mettre mon vélo dans la remise ?", n:'la forme de tous les jours'},
         a2:{w:["Est-ce que je pourrais mettre mon vélo dans la remise ?"], say:"Est-ce que je pourrais mettre mon vélo dans la remise ?", n:'le -rais adoucit la demande'},
         b1:{w:["Est-ce que je peux étendre mon linge dehors ?"], say:"Est-ce que je peux étendre mon linge dehors ?", n:'court, entre voisines'},
         b2:{w:["Est-ce que je pourrais utiliser la corde à linge ?"], say:"Est-ce que je pourrais utiliser la corde à linge ?", n:'plus prudent avec quelqu\'un qu\'on connaît peu'},
         c1:{w:["Est-ce que je peux avoir la clé de la remise ?"], say:"Est-ce que je peux avoir la clé de la remise ?", n:'on demande la chose directement'},
         c2:{w:["Est-ce que vous pourriez me prêter la clé deux minutes ?"], say:"Est-ce que vous pourriez me prêter la clé deux minutes ?", n:'« vous pourriez » : la demande porte sur l\'autre'},
         d1:{w:["Est-ce que je peux passer par la cour ?"], say:"Est-ce que je peux passer par la cour ?", n:'simple et suffisant'},
         d2:{w:["Est-ce que vous permettez que je passe par la cour ?"], say:"Est-ce que vous permettez que je passe par la cour ?", n:'la forme la plus polie des trois'},
       },
       note:"Remarque le déplacement : « je peux » demande pour toi, « vous pourriez » demande à l'autre de faire quelque chose."},

      {t:'ex', h:"À écouter et à répéter",
       p:"Six phrases de palier.",
       rows:[
         ["Excusez-moi de vous déranger.","la phrase qui ouvre"],
         ["Est-ce que je peux mettre mon vélo dans la remise ?","la demande simple"],
         ["Est-ce que je pourrais l'accrocher au mur ?","la demande polie"],
         ["Bien sûr, allez-y. Il y a de la place au fond.","la permission donnée"],
         ["Je préfère que non : c'est la sortie de secours.","le refus avec sa raison"],
         ["Merci, c'est gentil. Bonne journée.","la phrase qui ferme"],
       ]},

      {t:'piege', h:"Trois pièges à connaître",
       rows:[
         ["dire « je veux »","« Je veux mettre mon vélo dans la remise. »",
          "« Je veux » annonce une décision, pas une demande. Entre voisins, il sonne comme une porte qu'on pousse. Dis « je peux » ou « je voudrais »."],
         ["oublier de dire pourquoi","« Est-ce que je peux entrer dans la remise ? »",
          "Une demande sans raison inquiète. Une phrase suffit : « Mon vélo gêne dans le corridor. »"],
         ["insister après un refus","redemander deux fois la même chose",
          "Quand la réponse est « je préfère que non », on remercie et on cherche une autre solution. Insister coûte la permission suivante."],
       ]},

      {t:'check', h:"Est-ce que c'est clair maintenant ?",
       p:"Quatre questions rapides.",
       qs:[
         {q:"La demande la plus polie est…", opts:["Est-ce que je peux…","Est-ce que je pourrais…"], ok:1,
          fb:"Le -rais de « pourrais » adoucit toute la phrase."},
         {q:"« Je préfère que non » veut dire…", opts:["oui, mais plus tard","non, poliment"], ok:1,
          fb:"C'est un refus. Il se respecte comme un non."},
         {q:"Après un refus, on…", opts:["remercie et on cherche autre chose","redemande le lendemain"], ok:0,
          fb:"Insister coûte la permission suivante."},
         {q:"« La permission » désigne…", opts:["la phrase qu'on dit","le droit qu'on te donne"], ok:1,
          fb:"On demande la permission, on la donne, on la refuse."},
       ]},

      {t:'revoir', h:"À retenir",
       p:"Trois phrases, dans l'ordre : <b>Excusez-moi de vous déranger.</b> — <b>Est-ce que je peux… ?</b> (ou <b>je pourrais</b>, si tu connais peu la personne) — <b>Merci, c'est gentil.</b> Entre les deux, une phrase pour dire pourquoi."},
    ]
  },

  t1pron: {
    eye:'Mini-leçon', tit:"Le, la, les, lui : ne pas répéter le mot",
    blocs:[
      {t:'texte', h:"Le français déteste répéter",
       p:"« Mon vélo gêne. Je vais mettre mon vélo dans la remise. » Personne ne parle ainsi. On remplace le deuxième « mon vélo » par un petit mot : <b>je vais le mettre dans la remise</b>. Ce petit mot se choisit selon ce qu'il remplace, et il se place toujours au même endroit.",
       note:"C'est le point de grammaire qui fait le plus vite « parler comme tout le monde ». Quatre mots à ranger, et la phrase devient naturelle."},

      {t:'ana', h:"Une chose masculine : le",
       p:"Il remplace un nom masculin déjà nommé.",
       mots:[['On dit','Mon vélo ? Je {le} mets dans la remise.'],['Aussi','Le courrier ? Je {le} monte.',true],['Devant une voyelle','Je {l\'}accroche au mur.']],
       say:"Mon vélo ? Je le mets dans la remise.",
       note:"Devant a, e, i, o, u, le mot perd sa voyelle : je l'accroche, je l'ouvre, je l'apporte."},

      {t:'ana', h:"Une chose féminine : la",
       p:"Il remplace un nom féminin déjà nommé.",
       mots:[['On dit','La tondeuse ? Je {la} laisse passer.'],['Aussi','La clé ? Le concierge {la} garde.',true],['Devant une voyelle','L\'affiche ? Je {l\'}ai vue ce matin.']],
       say:"La tondeuse ? Je la laisse passer.",
       note:"Au son, « je le mets » et « je la mets » ne se distinguent que par une voyelle. Écoute-la : c'est elle qui dit de quoi on parle."},

      {t:'ana', h:"Plusieurs choses : les",
       p:"Un seul mot pour le masculin et le féminin.",
       mots:[['On dit','Mes clés ? Je {les} remets ce soir.'],['Aussi','Mes boîtes ? Je {les} vide ce soir.',true],['Toujours','le s se prononce devant une voyelle : je {les} ai vues']],
       say:"Mes clés ? Je les remets ce soir.",
       note:"Rien à choisir au pluriel : « les » sert dans tous les cas. C'est le plus facile des quatre."},

      {t:'ana', h:"Une personne à qui on parle : lui",
       p:"Quand le mot « à » est devant la personne.",
       mots:[['On dit','Je parle {à} monsieur Nadeau → je {lui} parle.'],['Aussi','Je dis merci {à} ma voisine → je {lui} dis merci.',true],['Le test','le verbe demande-t-il « à quelqu\'un » ?']],
       say:"Monsieur Nadeau est en bas : je lui parle tout de suite.",
       note:"« Lui » vaut pour un homme comme pour une femme. C'est le petit mot qui surprend le plus au début."},

      {t:'ana', h:"Où se place le petit mot",
       p:"Une seule règle, et une seule exception.",
       mots:[['La règle','toujours {avant} le verbe : je {le} mets'],['Avec deux verbes','avant le second : je vais {le} mettre',true],['L\'exception','à l\'impératif, il passe après : accrochez-{le} !']],
       say:"Accrochez-le au mur du fond, s'il vous plaît.",
       note:"À l'impératif, le petit mot se colle au verbe avec un trait d'union : accrochez-le, dis-lui, remets-les."},

      {t:'labo', h:"Remplace le mot",
       p:"Choisis ce dont tu parles et le moment.",
       axes:[
         {id:'o', lbl:'Tu parles de quoi ?', opts:[['a','mon vélo'],['b','la clé'],['c','mes clés'],['d','monsieur Nadeau']]},
         {id:'t', lbl:'Quel verbe ?', opts:[['1','maintenant'],['2','tout à l\'heure']]}],
       out:{
         a1:{w:["Je le mets dans la remise."], say:"Je le mets dans la remise.", n:'masculin singulier'},
         a2:{w:["Je vais le mettre dans la remise."], say:"Je vais le mettre dans la remise.", n:'avec deux verbes, il passe avant le second'},
         b1:{w:["Le concierge la garde chez lui."], say:"Le concierge la garde chez lui.", n:'féminin singulier'},
         b2:{w:["Je vais la lui demander."], say:"Je vais la lui demander.", n:'deux petits mots, dans cet ordre'},
         c1:{w:["Je les remets ce soir."], say:"Je les remets ce soir.", n:'pluriel : un seul mot possible'},
         c2:{w:["Je vais les remettre ce soir."], say:"Je vais les remettre ce soir.", n:'même place qu\'au singulier'},
         d1:{w:["Je lui parle tout de suite."], say:"Je lui parle tout de suite.", n:'on parle À quelqu\'un : lui'},
         d2:{w:["Je vais lui demander la clé."], say:"Je vais lui demander la clé.", n:'on demande À quelqu\'un : lui'},
       },
       note:"Regarde la place : le petit mot est toujours collé devant le verbe qui compte, jamais après."},

      {t:'ex', h:"À écouter et à répéter",
       p:"Six phrases d'immeuble.",
       rows:[
         ["Mon vélo gêne : je vais le mettre dans la remise.","le, masculin"],
         ["La clé ? Le concierge la garde chez lui.","la, féminin"],
         ["J'ai trouvé des clés : je vais les remettre ce soir.","les, pluriel"],
         ["Monsieur Nadeau est en bas : je vais lui demander.","lui, la personne"],
         ["Madame Lachapelle m'a aidé : je vais lui dire merci.","lui, au féminin aussi"],
         ["Accrochez-le au mur du fond.","à l'impératif, il passe après"],
       ]},

      {t:'piege', h:"Trois pièges à connaître",
       rows:[
         ["placer le petit mot après le verbe","« Je mets le dans la remise. »",
          "En français, il vient avant : je le mets. La seule exception est l'impératif : accrochez-le."],
         ["employer « le » pour une personne à qui on parle","« Je le parle. »",
          "Le verbe « parler » demande « à quelqu'un » : je lui parle. Le test tient en une question — le verbe demande-t-il « à » ?"],
         ["répéter le nom quand même","« Mon vélo, je le mets mon vélo dans la remise. »",
          "Une seule fois suffit : ou le nom, ou le petit mot, jamais les deux dans la même phrase."],
       ]},

      {t:'check', h:"Est-ce que c'est clair maintenant ?",
       p:"Quatre questions rapides.",
       qs:[
         {q:"« Mes clés ? Je ___ remets. »", opts:["le","les"], ok:1,
          fb:"Au pluriel, un seul mot possible : les."},
         {q:"« Je parle à monsieur Nadeau » devient…", opts:["je le parle","je lui parle"], ok:1,
          fb:"Le verbe demande « à quelqu'un » : c'est « lui »."},
         {q:"Le petit mot se place…", opts:["avant le verbe","après le verbe"], ok:0,
          fb:"Sauf à l'impératif : accrochez-le."},
         {q:"« La tondeuse ? Je ___ laisse passer. »", opts:["le","la"], ok:1,
          fb:"« Tondeuse » est féminin : la."},
       ]},

      {t:'revoir', h:"À retenir",
       p:"Quatre mots, un tableau : <b>le</b> (une chose masculine), <b>la</b> (une chose féminine), <b>les</b> (plusieurs), <b>lui</b> (une personne, quand le verbe demande « à »). Et une place : <b>devant le verbe</b>."},
    ]
  },

  t2inv: {
    eye:'Mini-leçon', tit:"Ce qu'une invitation doit toujours dire",
    blocs:[
      {t:'texte', h:"Une invitation sans jour n'est pas une invitation",
       p:"« Il faudrait se voir un de ces jours » n'invite personne : c'est une intention. Une vraie invitation donne trois renseignements — le <b>jour</b>, l'<b>heure</b>, l'<b>endroit</b> — et souvent deux de plus : qui est invité, et ce qu'on apporte.",
       note:"Le test est simple : la personne peut-elle inscrire quelque chose sur son calendrier avec ce que tu viens de dire ? Si non, il manque un renseignement."},

      {t:'ana', h:"Le jour",
       p:"Un jour nommé, jamais « bientôt ».",
       mots:[['On dit','{C\'est samedi.}'],['Avec la date','samedi le 14 · samedi prochain',true],['Pas','« un de ces jours », « bientôt »']],
       say:"C'est samedi, chez nous.",
       note:"Les noms de jours ne prennent jamais de majuscule en français : samedi, dimanche, lundi."},

      {t:'ana', h:"L'heure",
       p:"En chiffres, et répétée à la fin de la conversation.",
       mots:[['On dit','{À deux heures.}'],['À l\'écrit','à 14 h — avec une espace avant le h',true],['On la répète','Alors, samedi, deux heures.']],
       say:"Samedi, à deux heures.",
       note:"Au Québec, on dit « deux heures » à l'oral même quand on écrit « 14 h ». Les deux sont justes, chacune à sa place."},

      {t:'ana', h:"L'endroit",
       p:"La porte devant laquelle il faut frapper.",
       mots:[['On dit','{Chez nous}, au 3A.'],['Les trois formes','chez nous · chez vous · chez eux',true],['Ailleurs','dans la cour · dans l\'entrée']],
       say:"Ça se passe chez nous, au 3A.",
       note:"« Chez » ne s'emploie qu'avec une personne : chez nous, chez Manon, chez le concierge. Jamais « chez la cour »."},

      {t:'ana', h:"Qui est invité, et ce qu'on apporte",
       p:"Les deux questions que l'invité pose de toute façon.",
       mots:[['On demande','{Qui vient ?} · Qui est-ce qui vient ?'],['On répond','Les voisins de l\'immeuble.',true],['Ce qu\'on apporte','{Apportez seulement votre bonne humeur.}']],
       say:"Apportez seulement votre bonne humeur.",
       note:"« Apportez seulement votre bonne humeur » est la façon polie de dire « rien ». Elle laisse tout de même la porte ouverte à ceux qui insistent."},

      {t:'labo', h:"Une invitation, cinq renseignements",
       p:"Choisis le renseignement et la façon de le demander.",
       axes:[
         {id:'r', lbl:'Quel renseignement ?', opts:[['a','le jour'],['b','l\'heure'],['c','l\'endroit'],['d','ce qu\'on apporte']]},
         {id:'s', lbl:'Qui parle ?', opts:[['1','celui qui invite'],['2','celui qui est invité']]}],
       out:{
         a1:{w:["On fait un petit café samedi."], say:"On fait un petit café samedi.", n:'le jour, donné d\'emblée'},
         a2:{w:["C'est quand, exactement ?"], say:"C'est quand, exactement ?", n:'la question la plus courante'},
         b1:{w:["Samedi, à deux heures."], say:"Samedi, à deux heures.", n:'le jour et l\'heure ensemble'},
         b2:{w:["Et c'est à quelle heure ?"], say:"Et c'est à quelle heure ?", n:'« à quelle heure », en trois mots'},
         c1:{w:["Chez nous, au 3A."], say:"Chez nous, au 3A.", n:'l\'étage et le numéro de porte'},
         c2:{w:["C'est où ? Chez vous ?"], say:"C'est où ? Chez vous ?", n:'« où » suffit'},
         d1:{w:["Apportez seulement votre bonne humeur."], say:"Apportez seulement votre bonne humeur.", n:'la façon polie de dire « rien »'},
         d2:{w:["Est-ce que j'apporte quelque chose ?"], say:"Est-ce que j'apporte quelque chose ?", n:'la question de politesse'},
       },
       note:"Les quatre questions de droite sont celles que tu entendras si tu oublies un renseignement."},

      {t:'ex', h:"À écouter et à répéter",
       p:"Six phrases d'invitation.",
       rows:[
         ["On fait un petit café chez nous. Est-ce que vous voulez venir ?","l'invitation elle-même"],
         ["C'est samedi, à deux heures, au 3A.","les trois renseignements d'un coup"],
         ["Qui est-ce qui vient ? Les voisins de l'immeuble.","qui est invité"],
         ["Est-ce que j'apporte quelque chose ?","la question de l'invité"],
         ["Apportez seulement votre bonne humeur.","la réponse polie"],
         ["Alors, à samedi, deux heures !","on répète en partant"],
       ]},

      {t:'piege', h:"Trois pièges à connaître",
       rows:[
         ["inviter sans donner de jour","« Venez donc prendre un café un jour. »",
          "La personne dira oui par politesse et ne viendra jamais, parce qu'il n'y a rien à noter."],
         ["mettre une majuscule aux jours","« Samedi » au milieu d'une phrase",
          "En français, les noms de jours et de mois s'écrivent en minuscules : samedi, novembre."],
         ["dire « chez » devant un lieu","« chez la cour », « chez le troisième »",
          "« Chez » ne va qu'avec une personne. Pour un lieu, on dit « dans la cour », « au troisième »."],
       ]},

      {t:'check', h:"Est-ce que c'est clair maintenant ?",
       p:"Quatre questions rapides.",
       qs:[
         {q:"Une invitation doit toujours donner…", opts:["le jour, l'heure et l'endroit","le nom des invités"], ok:0,
          fb:"Ce sont les trois renseignements sans lesquels rien ne se note."},
         {q:"On écrit…", opts:["Samedi 14","samedi 14"], ok:1,
          fb:"Les noms de jours ne prennent pas de majuscule."},
         {q:"« Apportez seulement votre bonne humeur » veut dire…", opts:["apportez un dessert","n'apportez rien"], ok:1,
          fb:"C'est la façon polie de dire « rien »."},
         {q:"On dit…", opts:["chez la cour","dans la cour"], ok:1,
          fb:"« Chez » ne s'emploie qu'avec une personne."},
       ]},

      {t:'revoir', h:"À retenir",
       p:"Trois renseignements, toujours : <b>quand</b>, <b>à quelle heure</b>, <b>où</b>. Deux de plus si tu peux : <b>qui vient</b> et <b>ce qu'on apporte</b>. Et une phrase pour finir : « Alors, à samedi ! »"},
    ]
  },

  t2futur: {
    eye:'Mini-leçon', tit:"Ce qui va arriver, et ce qui aura lieu",
    blocs:[
      {t:'texte', h:"Deux futurs, deux usages",
       p:"Le français a deux façons de parler de ce qui n'est pas encore arrivé. À l'oral, on emploie presque toujours le <b>futur proche</b> : « je <b>vais apporter</b> mes biscuits ». À l'écrit — sur un carton d'invitation, une affiche —, on emploie le <b>futur simple</b> : « la fête <b>aura lieu</b> samedi ».",
       note:"Les deux sont corrects partout. Ce n'est pas une question de justesse, c'est une question d'endroit : l'un s'entend, l'autre se lit."},

      {t:'ana', h:"Le futur proche, celui de l'oral",
       p:"Deux morceaux : le verbe « aller », puis le verbe qui ne change pas.",
       mots:[['On dit','{Je vais apporter} mes biscuits.'],['La recette','aller + l\'infinitif',true],['Toutes les personnes','je vais · tu vas · il va · nous allons · vous allez · ils vont']],
       say:"Je vais apporter mes biscuits, j'insiste.",
       note:"Le second verbe ne bouge jamais : apporter, faire, venir, voir. C'est ce qui rend ce futur si facile."},

      {t:'ana', h:"Ce que le futur proche donne à entendre",
       p:"Quelque chose de décidé, et de proche.",
       mots:[['Décidé','{Elle va faire} des gâteaux.'],['Proche','{On va se voir} samedi.',true],['Presque sûr','Il va pleuvoir cet après-midi.']],
       say:"Ma sœur va faire des gâteaux. On va se voir samedi.",
       note:"« Proche » ne veut pas dire « dans une heure ». Ça veut dire : c'est arrangé, ça s'en vient."},

      {t:'ana', h:"Le futur simple, celui de l'écrit",
       p:"Un seul verbe, avec une terminaison qui contient toujours un r.",
       mots:[['On écrit','{La fête aura lieu} samedi.'],['La marque','le r : aur-a, ser-a, viendr-a',true],['Aussi','Nous vous attendr{ons} à 14 h.']],
       say:"La fête aura lieu samedi, à deux heures.",
       note:"C'est la forme des cartons d'invitation, des affiches et des avis punaisés dans l'entrée. Tu la liras plus souvent que tu ne l'écriras."},

      {t:'ana', h:"Trois formes à connaître par cœur",
       p:"Les trois qui reviennent dans toutes les invitations.",
       mots:[['Il y a → ','Il y {aura} du café.'],['C\'est → ','Ce {sera} chez nous.',true],['Nous sommes → ','Nous {serons} une dizaine.']],
       say:"Il y aura du café. Ce sera chez nous.",
       note:"Ces trois-là ne se déduisent d'aucune règle : elles s'apprennent telles quelles, comme trois mots de vocabulaire."},

      {t:'ana', h:"Le mot de l'écrit qui va avec",
       p:"On l'écrit, on ne le dit jamais.",
       mots:[['Sur le carton','{Confirmez SVP}'],['Ce que ça veut dire','dites-moi si vous venez',true],['À l\'oral','Vous me le direz ? · Faites-moi signe.']],
       say:"Confirmez SVP avant vendredi.",
       note:"SVP est l'abréviation de « s'il vous plaît ». Elle s'écrit en majuscules et sans points."},

      {t:'labo', h:"À l'oral ou sur le carton ?",
       p:"Choisis la phrase et l'endroit où elle va.",
       axes:[
         {id:'p', lbl:'Quelle phrase ?', opts:[['a','la rencontre'],['b','le café'],['c','l\'endroit'],['d','la réponse']]},
         {id:'e', lbl:'Où ?', opts:[['1','dans l\'escalier'],['2','sur le carton']]}],
       out:{
         a1:{w:["On va se voir samedi, à deux heures."], say:"On va se voir samedi, à deux heures.", n:'futur proche, à l\'oral'},
         a2:{w:["La rencontre aura lieu le samedi 14, à 14 h."], say:"La rencontre aura lieu le samedi 14, à 14 h.", n:'futur simple, à l\'écrit'},
         b1:{w:["Je vais faire du café et des gâteaux."], say:"Je vais faire du café et des gâteaux.", n:'aller + infinitif'},
         b2:{w:["Il y aura du café, du thé et des gâteaux."], say:"Il y aura du café, du thé et des gâteaux.", n:'« il y aura », à retenir par cœur'},
         c1:{w:["Ça va se passer chez nous, au 3A."], say:"Ça va se passer chez nous, au 3A.", n:'la forme parlée'},
         c2:{w:["Ce sera chez nous, au 3A."], say:"Ce sera chez nous, au 3A.", n:'« ce sera », à retenir par cœur'},
         d1:{w:["Vous me direz si vous venez ?"], say:"Vous me direz si vous venez ?", n:'la question, à l\'oral'},
         d2:{w:["Confirmez SVP avant vendredi."], say:"Confirmez SVP avant vendredi.", n:'la formule, à l\'écrit seulement'},
       },
       note:"Colonne de gauche : ce que tu dis dans l'escalier. Colonne de droite : ce que tu écris sur le carton."},

      {t:'ex', h:"À écouter et à répéter",
       p:"Six phrases de samedi prochain.",
       rows:[
         ["Je vais apporter mes biscuits, j'insiste.","futur proche"],
         ["Ma sœur va faire des gâteaux.","futur proche"],
         ["On va se voir samedi, alors !","futur proche"],
         ["La fête aura lieu samedi, à deux heures.","futur simple"],
         ["Il y aura du café et des gâteaux.","à retenir par cœur"],
         ["Ce sera chez nous, au 3A.","à retenir par cœur"],
       ]},

      {t:'piege', h:"Trois pièges à connaître",
       rows:[
         ["conjuguer le second verbe","« Je vais apporte mes biscuits. »",
          "Après « aller », le verbe ne change jamais : apporter, faire, venir. Il reste tel qu'il est dans le dictionnaire."],
         ["oublier le r du futur simple","« la fête aua lieu »",
          "Toutes les formes du futur simple contiennent un r : aura, sera, viendra, attendrons. C'est le seul indice constant."],
         ["dire « confirmez SVP » à l'oral","dans une conversation",
          "C'est une formule écrite. À l'oral, on dit : « Vous me le direz ? » ou « Faites-moi signe. »"],
       ]},

      {t:'check', h:"Est-ce que c'est clair maintenant ?",
       p:"Quatre questions rapides.",
       qs:[
         {q:"À l'oral, on dit surtout…", opts:["j'apporterai","je vais apporter"], ok:1,
          fb:"Le futur proche est celui de la conversation."},
         {q:"Après « aller », le verbe…", opts:["se conjugue","ne change pas"], ok:1,
          fb:"Je vais apporter, tu vas apporter, il va apporter."},
         {q:"Sur un carton d'invitation, on écrit…", opts:["la fête va être samedi","la fête aura lieu samedi"], ok:1,
          fb:"Le futur simple est la forme de l'écrit."},
         {q:"« Confirmez SVP » veut dire…", opts:["dites-moi si vous venez","apportez quelque chose"], ok:0,
          fb:"SVP est l'abréviation de « s'il vous plaît »."},
       ]},

      {t:'revoir', h:"À retenir",
       p:"Dans l'escalier : <b>je vais…</b>, <b>elle va…</b>, <b>on va…</b>. Sur le carton : <b>aura lieu</b>, <b>il y aura</b>, <b>ce sera</b>, <b>confirmez SVP</b>. Deux listes courtes, et chacune à sa place."},
    ]
  },

  t2compl: {
    eye:'Mini-leçon', tit:"Le compliment, et la phrase qui s'exclame",
    blocs:[
      {t:'texte', h:"Un compliment ouvre une porte",
       p:"Dans un immeuble, le compliment est ce qui transforme un salut en conversation. Il est court, il porte sur une chose précise, et il se dit une seule fois. En français, il prend presque toujours la forme d'une phrase qui <b>s'exclame</b> : elle commence par <b>que</b>, <b>comme</b>, <b>quel</b> ou <b>quelle</b>, et elle finit par un point d'exclamation.",
       note:"Un compliment porte sur ce que la personne a <b>fait</b> — un plat, une porte repeinte, un vêtement choisi — plutôt que sur ce qu'elle est. C'est ce qui le rend facile à recevoir."},

      {t:'ana', h:"Complimenter ce qu'on mange",
       p:"Deux mots au choix, et ils s'échangent librement.",
       mots:[['On dit','{Que c\'est bon !}'],['Ou bien','{Comme c\'est bon !}',true],['Aussi','C\'est délicieux ! · C\'est vraiment bon !']],
       say:"Que c'est bon, ces biscuits-là !",
       note:"« Que » et « comme » veulent dire exactement la même chose ici. Choisis celui qui te vient : personne ne les distingue."},

      {t:'ana', h:"Complimenter la personne",
       p:"Le compliment porte sur ce qu'elle a fait.",
       mots:[['On dit','{Vous cuisinez bien !}'],['En tutoyant','{Tu cuisines bien !}',true],['Aussi','Vous avez du talent ! · C\'est vous qui l\'avez fait ?']],
       say:"Vous cuisinez bien, madame !",
       note:"« C'est vous qui l'avez fait ? » est un compliment déguisé en question. C'est la forme la plus fréquente au Québec."},

      {t:'ana', h:"Complimenter un vêtement",
       p:"Une formule toute faite, avec « ça ».",
       mots:[['On dit','{Ça vous va bien !}'],['En tutoyant','{Ça te va bien !}',true],['Aussi','Il est beau, votre manteau !']],
       say:"Votre manteau neuf ? Ça vous va bien !",
       note:"« Ça » remplace le vêtement dont on parle. On ne dit jamais « il vous va bien » pour un manteau : la formule est figée."},

      {t:'ana', h:"Complimenter une chose : quel, quelle",
       p:"Le mot change selon le genre du nom qui suit.",
       mots:[['Devant un nom féminin','{Quelle} belle porte !'],['Devant un nom masculin','{Quel} beau salon !',true],['Au pluriel','Quels beaux enfants ! · Quelles belles fleurs !']],
       say:"Quelle belle porte ! Quel beau salon !",
       note:"Les quatre formes se prononcent de la même façon. Seule l'écriture change, et seulement à l'écrit."},

      {t:'ana', h:"Répondre à un compliment",
       p:"On remercie, tout simplement.",
       mots:[['On dit','{Merci, c\'est gentil.}'],['Aussi','Merci ! Ça me fait plaisir.',true],['Pas','« Non, ce n\'est pas vrai. » · « Ce n\'est rien. »']],
       say:"Merci, c'est gentil.",
       note:"Refuser un compliment met l'autre mal à l'aise : il vient de dire quelque chose de vrai, et on le contredit. Un merci suffit."},

      {t:'labo', h:"Quel compliment, à quelle occasion ?",
       p:"Choisis ce que tu complimentes et la forme.",
       axes:[
         {id:'c', lbl:'Tu complimentes quoi ?', opts:[['a','les biscuits'],['b','la porte repeinte'],['c','le manteau'],['d','le salon']]},
         {id:'f', lbl:'Quelle forme ?', opts:[['1','avec que / comme'],['2','avec quel / quelle / ça']]}],
       out:{
         a1:{w:["Que c'est bon, ces biscuits-là !"], say:"Que c'est bon, ces biscuits-là !", n:'« que » + c\'est + adjectif'},
         a2:{w:["Quels bons biscuits !"], say:"Quels bons biscuits !", n:'« quels » + nom masculin pluriel'},
         b1:{w:["Comme elle est belle, votre porte !"], say:"Comme elle est belle, votre porte !", n:'« comme » + une phrase entière'},
         b2:{w:["Quelle belle porte !"], say:"Quelle belle porte !", n:'« quelle » + nom féminin'},
         c1:{w:["Comme il est beau, votre manteau !"], say:"Comme il est beau, votre manteau !", n:'« comme » + une phrase entière'},
         c2:{w:["Ça vous va bien !"], say:"Ça vous va bien !", n:'la formule figée du vêtement'},
         d1:{w:["Que c'est beau, chez vous !"], say:"Que c'est beau, chez vous !", n:'« que » + c\'est + adjectif'},
         d2:{w:["Quel beau salon vous avez !"], say:"Quel beau salon vous avez !", n:'« quel » + nom masculin'},
       },
       note:"Les huit phrases sont justes. Choisis celle qui te vient le plus vite : un compliment tardif ne vaut plus rien."},

      {t:'ex', h:"À écouter et à répéter",
       p:"Six compliments de voisinage.",
       rows:[
         ["Que c'est bon, ces biscuits-là !","que + c'est"],
         ["Comme c'est gentil d'avoir pensé à moi !","comme + c'est"],
         ["Vous cuisinez bien, madame !","le verbe de la personne"],
         ["Quelle belle porte ! C'est vous qui l'avez peinte ?","quelle, au féminin"],
         ["Quel beau salon vous avez !","quel, au masculin"],
         ["Merci, c'est gentil.","la réponse"],
       ]},

      {t:'piege', h:"Trois pièges à connaître",
       rows:[
         ["refuser le compliment","« Non, ce n'est pas si bon. »",
          "Cela met l'autre mal à l'aise. On remercie : « Merci, c'est gentil. » Rien de plus."],
         ["confondre quel et quelle","« Quel belle porte ! »",
          "Le mot s'accorde avec le nom qui suit : quel salon, quelle porte. À l'oral, personne n'entend la différence ; à l'écrit, elle se voit tout de suite."],
         ["complimenter la personne elle-même","« Vous êtes belle. »",
          "Entre voisins qui se connaissent peu, cela met mal à l'aise. Complimente ce que la personne a fait ou choisi, jamais son corps."],
       ]},

      {t:'check', h:"Est-ce que c'est clair maintenant ?",
       p:"Quatre questions rapides.",
       qs:[
         {q:"« ___ belle porte ! »", opts:["Quel","Quelle"], ok:1,
          fb:"« Porte » est féminin : quelle."},
         {q:"Pour un manteau, on dit…", opts:["Ça vous va bien !","Il vous va bien !"], ok:0,
          fb:"La formule est figée avec « ça »."},
         {q:"À un compliment, on répond…", opts:["Merci, c'est gentil.","Non, ce n'est rien."], ok:0,
          fb:"On remercie, tout simplement."},
         {q:"« Que c'est bon ! » et « Comme c'est bon ! »…", opts:["veulent dire la même chose","sont différents"], ok:0,
          fb:"Les deux mots s'échangent librement."},
       ]},

      {t:'revoir', h:"À retenir",
       p:"Quatre départs de phrase : <b>Que c'est…</b>, <b>Comme c'est…</b>, <b>Quel / Quelle…</b>, <b>Ça vous va bien !</b> Et une seule réponse : <b>Merci, c'est gentil.</b>"},
    ]
  },

  t3adj: {
    eye:'Mini-leçon', tit:"Décrire : l'accord et la place de l'adjectif",
    blocs:[
      {t:'texte', h:"Décrire, c'est faire reconnaître",
       p:"Quand un chat, des clés ou une personne se perdent dans un immeuble, tout se joue sur la description. Elle se construit avec des <b>adjectifs</b> — roux, gros, blanc, petit —, et deux choses les gouvernent : ils <b>s'accordent</b> avec le nom, et ils se <b>placent</b> avant ou après lui.",
       note:"L'ordre compte autant que les mots : d'abord ce qui se voit de loin, ensuite le détail qui ne trompe pas. « Roux, assez gros, avec une tache blanche sous le menton. »"},

      {t:'ana', h:"L'adjectif s'accorde avec le nom",
       p:"Au féminin, on ajoute le plus souvent un e.",
       mots:[['Masculin','un chat {roux} · un collier {bleu}'],['Féminin','une tuque {rousse} · une porte {bleue}',true],['Le e s\'entend','blanc → blan{che} · court → cour{te}']],
       say:"Un chat roux, une porte bleue, une tache blanche.",
       note:"Le e du féminin réveille souvent la consonne muette : « blanc » se dit « blan », mais « blanche » se dit « blanche »."},

      {t:'ana', h:"Au pluriel, on ajoute un s",
       p:"Un s qui s'écrit et qui ne s'entend pas.",
       mots:[['On écrit','des cheveux {gris} et {courts}'],['Aussi','des lunettes {rouges}',true],['Déjà en s','gris, roux : rien à ajouter']],
       say:"Elle a des cheveux gris et courts, et des lunettes rouges.",
       note:"Les adjectifs qui finissent déjà par s ou x ne changent pas au pluriel masculin : un chat roux, des chats roux."},

      {t:'ana', h:"La plupart se placent APRÈS le nom",
       p:"Les couleurs, les formes, les matières, les états.",
       mots:[['On dit','un chat {roux} · un collier {bleu}'],['Aussi','un ourson {usé} · un escalier {extérieur}',true],['Deux ensemble','un chat roux et gros']],
       say:"Un chat roux, un ourson usé, un escalier extérieur.",
       note:"C'est le cas général. Si tu hésites, place l'adjectif après : tu auras raison neuf fois sur dix."},

      {t:'ana', h:"Quelques-uns se placent AVANT",
       p:"Les plus courts et les plus courants, à apprendre en petite liste.",
       mots:[['On dit','un {petit} ourson · une {grande} dame'],['Aussi','un {beau} chat · un {vieux} vélo · un {gros} chat',true],['La liste','petit, grand, beau, joli, vieux, gros, bon, jeune']],
       say:"Un petit ourson, une grande dame, un vieux vélo.",
       note:"Huit adjectifs, et ce sont les seuls à retenir. Tous les autres passent après le nom."},

      {t:'ana', h:"L'ordre qui aide l'autre à reconnaître",
       p:"De loin vers le détail, jamais l'inverse.",
       mots:[['D\'abord','la couleur : {roux}'],['Ensuite','la taille : {assez gros}',true],['Enfin','le détail : {une tache blanche sous le menton}']],
       say:"Il est roux, assez gros, avec une tache blanche sous le menton.",
       note:"Commencer par le détail perd l'interlocuteur : il ne sait pas encore de quel animal on parle."},

      {t:'labo', h:"Accorde et place",
       p:"Choisis ce que tu décris et l'adjectif.",
       axes:[
         {id:'n', lbl:'Tu décris quoi ?', opts:[['a','un chat'],['b','une porte'],['c','des cheveux'],['d','des lunettes']]},
         {id:'a', lbl:'Quel adjectif ?', opts:[['1','une couleur'],['2','un adjectif de la petite liste']]}],
       out:{
         a1:{w:["un chat roux"], say:"Un chat roux.", n:'la couleur passe après'},
         a2:{w:["un gros chat"], say:"Un gros chat.", n:'« gros » fait partie de la petite liste'},
         b1:{w:["une porte bleue"], say:"Une porte bleue.", n:'féminin : bleu prend un e'},
         b2:{w:["une belle porte"], say:"Une belle porte.", n:'« beau » devient « belle » au féminin'},
         c1:{w:["des cheveux gris"], say:"Des cheveux gris.", n:'« gris » finit déjà par s : rien à ajouter'},
         c2:{w:["des cheveux courts"], say:"Des cheveux courts.", n:'un s au pluriel, qui ne s\'entend pas'},
         d1:{w:["des lunettes rouges"], say:"Des lunettes rouges.", n:'féminin pluriel : un s au bout'},
         d2:{w:["des petites lunettes"], say:"Des petites lunettes.", n:'« petit » passe avant le nom'},
       },
       note:"Huit groupes, quatre accords différents. Relis-les à voix haute : ce qui s'entend, ce sont les féminins."},

      {t:'ex', h:"À écouter et à répéter",
       p:"Six descriptions de l'immeuble.",
       rows:[
         ["Caramel est un chat roux, assez gros.","couleur puis taille"],
         ["Il a une tache blanche sous le menton.","le détail qui ne trompe pas"],
         ["Il porte un collier bleu, sans médaille.","ce qu'il porte"],
         ["La dame du premier a les cheveux gris et courts.","deux adjectifs au pluriel"],
         ["Elle porte des lunettes rouges.","féminin pluriel"],
         ["Sur les clés, il y a un petit ourson en tissu.","« petit » passe avant"],
       ]},

      {t:'piege', h:"Trois pièges à connaître",
       rows:[
         ["oublier le e du féminin","« une porte bleu »",
          "Il ne s'entend pas toujours, mais il s'écrit toujours : une porte bleue, une tuque rousse, une tache blanche."],
         ["placer la couleur avant le nom","« un roux chat »",
          "Les couleurs passent toujours après : un chat roux, une porte bleue, des lunettes rouges."],
         ["commencer la description par le détail","« Il a une tache blanche… »",
          "L'autre ne sait pas encore de quoi tu parles. Donne d'abord la couleur et la taille, puis le détail."],
       ]},

      {t:'check', h:"Est-ce que c'est clair maintenant ?",
       p:"Quatre questions rapides.",
       qs:[
         {q:"On écrit…", opts:["une porte bleu","une porte bleue"], ok:1,
          fb:"Le e du féminin s'écrit toujours, même s'il ne s'entend pas."},
         {q:"La couleur se place…", opts:["avant le nom","après le nom"], ok:1,
          fb:"Un chat roux, une porte bleue, des lunettes rouges."},
         {q:"Lequel se place avant le nom ?", opts:["roux","petit"], ok:1,
          fb:"« Petit » fait partie de la petite liste : petit, grand, beau, joli, vieux, gros, bon, jeune."},
         {q:"Une bonne description commence par…", opts:["ce qui se voit de loin","le détail précis"], ok:0,
          fb:"La couleur et la taille d'abord ; le détail ensuite."},
       ]},

      {t:'revoir', h:"À retenir",
       p:"Deux gestes : <b>accorder</b> (un e au féminin, un s au pluriel) et <b>placer</b> (après le nom, sauf les huit petits : petit, grand, beau, joli, vieux, gros, bon, jeune). Et un ordre : <b>couleur, taille, détail</b>."},
    ]
  },

  t3int: {
    eye:'Mini-leçon', tit:'Très, assez, un peu, trop',
    blocs:[
      {t:'texte', h:"Quatre mots qui disent combien",
       p:"« Il est gros » ne dit pas grand-chose : gros comment ? Quatre petits mots règlent la question — <b>très</b>, <b>assez</b>, <b>un peu</b>, <b>trop</b> — et ils se placent tous au même endroit : juste <b>devant</b> l'adjectif.",
       note:"Ils changent complètement le sens d'une description. « Assez gros » et « trop gros » ne décrivent pas le même chat, et surtout, le second contient un reproche."},

      {t:'ana', h:"Très — beaucoup",
       p:"Le degré le plus élevé, sans idée de problème.",
       mots:[['On dit','Il est {très} peureux.'],['Aussi','Elle a été {très} gentille.',true],['Avec un verbe','Merci {beaucoup} — jamais « merci très »']],
       say:"Il est très peureux avec les gens qu'il ne connaît pas.",
       note:"« Très » va avec un adjectif ou un adverbe. Avec un verbe, on emploie « beaucoup » : j'aime beaucoup, je travaille beaucoup."},

      {t:'ana', h:"Assez — pas mal, mais pas énormément",
       p:"Un degré moyen, souvent plus haut que la moyenne.",
       mots:[['On dit','Il est {assez} gros.'],['Ce que ça dit','plus gros que la moyenne, sans plus',true],['Autre sens','J\'en ai assez ! — là, c\'est de la lassitude']],
       say:"Il est assez gros, mon chat.",
       note:"« Assez » est le mot des descriptions honnêtes : il n'exagère pas, et c'est exactement ce qu'il faut sur une affiche."},

      {t:'ana', h:"Un peu — un petit peu seulement",
       p:"Trois mots qui n'en font qu'un.",
       mots:[['On dit','L\'ourson est {un peu} usé.'],['Ce que ça dit','on le voit, mais ce n\'est pas grave',true],['Pas','« un peu » ne s\'emploie pas avec un adjectif positif : pas « un peu beau »']],
       say:"L'ourson est un peu usé, il a servi longtemps.",
       note:"« Un peu » va surtout avec des adjectifs qui décrivent un défaut ou un état : un peu usé, un peu peureux, un peu fatigué."},

      {t:'ana', h:"Trop — plus qu'il ne faudrait",
       p:"Le seul des quatre qui annonce un problème.",
       mots:[['On dit','Mon vélo prend {trop} de place.'],['Aussi','L\'escalier est {trop} étroit.',true],['Avec un nom','trop {de} place · trop {de} monde']],
       say:"Mon vélo prend trop de place dans le corridor.",
       note:"« Trop » dit toujours qu'il y a quelque chose à corriger. Ne l'emploie pas pour un compliment : « votre gâteau est trop bon » se dit entre amis, jamais chez une voisine qu'on connaît peu."},

      {t:'ana', h:"Où ils se placent",
       p:"Une seule position, pour les quatre.",
       mots:[['La règle','toujours {devant} l\'adjectif'],['Ensemble','{très} peureux · {assez} gros · {un peu} usé',true],['Jamais','« peureux très », « gros assez »']],
       say:"Très peureux, assez gros, un peu usé.",
       note:"Avec un nom, « trop » et « un peu » demandent le mot « de » : trop de place, un peu de café."},

      {t:'labo', h:"Le même adjectif, quatre degrés",
       p:"Choisis l'adjectif et le degré.",
       axes:[
         {id:'a', lbl:'Quel adjectif ?', opts:[['a','peureux'],['b','gros'],['c','étroit'],['d','gentille']]},
         {id:'d', lbl:'Quel degré ?', opts:[['1','très'],['2','assez'],['3','trop']]}],
       out:{
         a1:{w:["Il est très peureux."], say:"Il est très peureux.", n:'il se sauve dès qu\'on approche'},
         a2:{w:["Il est assez peureux."], say:"Il est assez peureux.", n:'il se méfie, sans plus'},
         a3:{w:["Il est trop peureux pour qu'on le prenne."], say:"Il est trop peureux pour qu'on le prenne.", n:'« trop » annonce une conséquence'},
         b1:{w:["Il est très gros."], say:"Il est très gros.", n:'nettement plus gros que les autres'},
         b2:{w:["Il est assez gros."], say:"Il est assez gros.", n:'la formule de l\'affiche : honnête'},
         b3:{w:["Il est trop gros pour passer par là."], say:"Il est trop gros pour passer par là.", n:'un problème, avec sa conséquence'},
         c1:{w:["L'escalier est très étroit."], say:"L'escalier est très étroit.", n:'un constat'},
         c2:{w:["L'escalier est assez étroit."], say:"L'escalier est assez étroit.", n:'un constat prudent'},
         c3:{w:["L'escalier est trop étroit pour monter un divan."], say:"L'escalier est trop étroit pour monter un divan.", n:'ce qui empêche de faire quelque chose'},
         d1:{w:["Elle a été très gentille avec nous."], say:"Elle a été très gentille avec nous.", n:'un remerciement'},
         d2:{w:["Elle a été assez gentille pour nous aider."], say:"Elle a été assez gentille pour nous aider.", n:'« assez… pour » : suffisamment'},
         d3:{w:["Elle est trop gentille, elle ne dit jamais non."], say:"Elle est trop gentille, elle ne dit jamais non.", n:'même un compliment devient un reproche'},
       },
       note:"Regarde la troisième ligne : « trop » appelle presque toujours une suite en « pour »."},

      {t:'ex', h:"À écouter et à répéter",
       p:"Six phrases du troisième défi.",
       rows:[
         ["Caramel est très peureux : il se sauve tout le temps.","très"],
         ["Il est assez gros, mais ce n'est pas un gros chat.","assez"],
         ["L'ourson des clés est un peu usé.","un peu"],
         ["Mon vélo prend trop de place dans le corridor.","trop de + nom"],
         ["Madame Lachapelle a été très gentille avec nous.","très"],
         ["L'escalier est trop étroit pour monter un divan.","trop… pour"],
       ]},

      {t:'piege', h:"Trois pièges à connaître",
       rows:[
         ["employer « très » avec un verbe","« Merci très. »",
          "Avec un verbe, c'est « beaucoup » : merci beaucoup, j'aime beaucoup, ça m'aide beaucoup."],
         ["confondre « assez » et « trop »","« Il est trop gros » sur une affiche",
          "« Trop » annonce un problème. Sur une affiche de chat perdu, on écrit « assez gros » : on décrit, on ne se plaint pas."],
         ["oublier le « de »","« trop place », « un peu café »",
          "Devant un nom, il faut « de » : trop de place, un peu de café, trop de monde dans l'escalier."],
       ]},

      {t:'check', h:"Est-ce que c'est clair maintenant ?",
       p:"Quatre questions rapides.",
       qs:[
         {q:"Lequel annonce un problème ?", opts:["assez","trop"], ok:1,
          fb:"« Trop » dit toujours qu'il y a quelque chose à corriger."},
         {q:"Ces mots se placent…", opts:["devant l'adjectif","après l'adjectif"], ok:0,
          fb:"Très peureux, assez gros, un peu usé. Jamais l'inverse."},
         {q:"Avec un verbe, on dit…", opts:["merci très","merci beaucoup"], ok:1,
          fb:"« Très » va avec un adjectif ; « beaucoup » va avec un verbe."},
         {q:"On écrit…", opts:["trop place","trop de place"], ok:1,
          fb:"Devant un nom, il faut « de »."},
       ]},

      {t:'revoir', h:"À retenir",
       p:"Quatre mots, un seul endroit — <b>devant l'adjectif</b>. <b>Très</b> = beaucoup. <b>Assez</b> = pas mal. <b>Un peu</b> = juste un peu. <b>Trop</b> = il y a un problème. Et devant un nom, n'oublie pas le <b>de</b>."},
    ]
  },
};
