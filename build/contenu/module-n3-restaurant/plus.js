const PLUS = {
  prPhon: {
    eye:'Mini-leçon', tit:"Le « ou » de soupe et le « u » de jus",
    blocs:[
      {t:'texte', h:"Deux sons très proches, deux mots différents",
       p:"Le français sépare deux sons que beaucoup de langues confondent : le <b>ou</b> de « s<b>ou</b>pe » et le <b>u</b> de « j<b>u</b>s ». Ils se font au même endroit de la bouche, avec les lèvres rondes dans les deux cas. Ce qui change, c'est la <b>langue</b> : en arrière pour « ou », en avant pour « u ».",
       note:"Au comptoir, ça compte : « pour » et « pur », « dessous » et « dessus », « la roue » et « la rue » ne veulent pas dire la même chose."},

      {t:'ana', h:"Le son « ou » — la langue en arrière",
       p:"C'est le son de « soupe », « poulet », « pour emporter ».",
       mots:[['On écrit','s{ou}pe'],['Les lèvres','en rond, bien avancées',true],['La langue','tirée vers le fond de la bouche']],
       say:"La soupe au poulet, pour emporter.",
       note:"C'est le son de « ou » en français, et il ne s'écrit que d'une seule façon : o + u. Aucun piège d'écriture."},

      {t:'ana', h:"Le son « u » — la langue en avant",
       p:"C'est le son de « jus », « sucre », « légumes ».",
       mots:[['On écrit','j{u}s'],['Les lèvres','en rond, comme pour « ou »',true],['La langue','poussée vers les dents du bas']],
       say:"Le jus, le sucre, les légumes.",
       note:"Truc qui marche : dis « i » en gardant la langue où elle est, puis arrondis seulement les lèvres. Le son qui sort est « u »."},

      {t:'ana', h:"Les paires qui changent le sens",
       p:"Quatre paires à connaître, toutes utiles.",
       mots:[['pour / pur','p{ou}r emporter · du sucre p{u}r'],['dessous / dessus','le sac est dess{ou}s · le sel est dess{u}s',true],['la roue / la rue','la r{ou}e du chariot · la r{u}e du centre']],
       say:"Pour emporter. Du sucre pur.",
       note:"Si tu hésites devant un mot nouveau, dis-le à côté de « soupe », puis à côté de « jus ». Ton oreille choisit toute seule."},

      {t:'labo', h:"Écoute les paires",
       p:"Choisis une paire et écoute la différence.",
       axes:[{id:'p', lbl:'Quelle paire ?', opts:[
         ['a','pour / pur'],
         ['b','dessous / dessus'],
         ['c','soupe / jus'],
         ['d','poulet / légumes'],
         ['e','dans une phrase']]}],
       out:{
         a:{w:['p{ou}r / p{u}r'], say:"Pour, pur.", n:'la langue recule, puis avance'},
         b:{w:['dess{ou}s / dess{u}s'], say:"Dessous, dessus.", n:'le sens change du tout au tout'},
         c:{w:['s{ou}pe / j{u}s'], say:"La soupe, le jus.", n:'les deux mots du module'},
         d:{w:['p{ou}let / lég{u}mes'], say:"Le poulet, les légumes.", n:'les deux soupes du menu'},
         e:{w:['« Une soupe aux légumes et un jus, pour emporter. »'], say:"Une soupe aux légumes et un jus, pour emporter.", n:'les deux sons quatre fois'},
       },
       note:"Écoute chaque paire deux fois : la première pour comprendre, la seconde en fermant les yeux."},

      {t:'ex', h:"À écouter et à répéter",
       p:"Six phrases du comptoir.",
       rows:[
         ["Une soupe au poulet, s'il vous plaît.","ou trois fois"],
         ["Un jus, du sucre, une minute.","u trois fois"],
         ["Pour emporter, avec un couvercle.","ou quatre fois"],
         ["La soupe aux légumes est bonne.","les deux sons dans la même phrase"],
         ["Douze dollars pour un menu.","ou puis u"],
         ["Vous voulez du sucre dans votre café ?","ou et u côte à côte"],
       ]},

      {t:'piege', h:"Trois pièges à connaître",
       rows:[
         ["dire « ou » à la place de « u »","« un jous » au lieu de « un jus »",
          "C'est le piège le plus fréquent, et il s'entend beaucoup. La langue doit avancer, pas les lèvres."],
         ["dire « u » à la place de « ou »","« la supe » au lieu de « la soupe »",
          "Moins fréquent, mais il rend le mot méconnaissable. Pense à « soupe » comme à « poule » : la langue recule."],
         ["croire que les lèvres changent","essayer d'écarter les lèvres pour « u »",
          "Non : les lèvres sont rondes pour les deux sons. C'est la seule chose qui ne bouge pas. Tout se passe avec la langue."],
       ]},

      {t:'check', h:"Est-ce que c'est clair maintenant ?",
       p:"Quatre questions rapides.",
       qs:[
         {q:"« Soupe » a le son…", opts:["ou","u"], ok:0,
          fb:"La langue est tirée vers le fond de la bouche."},
         {q:"« Légumes » a le son…", opts:["ou","u"], ok:1,
          fb:"La langue est poussée vers les dents du bas."},
         {q:"Pour les deux sons, les lèvres sont…", opts:["rondes","écartées"], ok:0,
          fb:"C'est la langue qui change, jamais les lèvres."},
         {q:"« Pour emporter » et « du sucre pur »…", opts:["ont le même son","ont deux sons différents"], ok:1,
          fb:"« pour » a le son ou, « pur » a le son u."},
       ]},

      {t:'revoir', h:"À retenir",
       p:"Deux mots repères, et rien d'autre : <b>soupe</b> pour le son « ou », <b>jus</b> pour le son « u ». Devant un mot nouveau, dis-le à côté de l'un des deux, et garde toujours les lèvres rondes."},
    ]
  },

  prFormats: {
    eye:'Mini-leçon', tit:'Petit, moyen, grand — les trois formats',
    blocs:[
      {t:'texte', h:"Trois mots suffisent pour tout le comptoir",
       p:"Sur le tableau du menu, un même plat porte souvent trois prix. Ce ne sont pas trois plats : c'est le même, en trois <b>formats</b>. Le mot est important parce que c'est celui que le préposé emploie : « Quel format ? » Trois réponses possibles, jamais plus : <b>petit</b>, <b>moyen</b>, <b>grand</b>.",
       note:"Le programme de niveau 3 nomme précisément ce point : les types de formats. C'est un des deux seuls blocs de vocabulaire qu'il donne pour cette situation."},

      {t:'ana', h:"Les trois mots, au masculin",
       p:"Devant un mot masculin, on ne change rien.",
       mots:[['On dit','un {petit} café'],['Aussi','un format {moyen}',true],['Et','un {grand} jus']],
       say:"Un petit café, un format moyen, un grand jus.",
       note:"Café, jus, format, sac, plateau : tous masculins. C'est la moitié des mots du comptoir."},

      {t:'ana', h:"Les trois mots, au féminin",
       p:"Devant un mot féminin, on ajoute un e — et « moyen » double son n.",
       mots:[['On dit','une {petite} soupe'],['Attention','une portion {moyenne} — deux n',true],['Et','une {grande} salade']],
       say:"Une petite soupe, une portion moyenne, une grande salade.",
       note:"Soupe, salade, portion, frite, boîte : tous féminins. L'autre moitié des mots du comptoir."},

      {t:'ana', h:"La réponse la plus courte",
       p:"Quand le préposé demande le format, deux mots suffisent.",
       mots:[['Il demande','Quel format ?'],['Tu réponds','{Petit}, s\'il vous plaît.',true],['Ou encore','{Un petit}, s\'il vous plaît.']],
       say:"Quel format ? Petit, s'il vous plaît.",
       note:"On n'a pas besoin de répéter le nom du plat : il vient d'être dit. Une phrase courte, dans la file, c'est une phrase réussie."},

      {t:'labo', h:"Le format et le plat",
       p:"Choisis un plat et un format.",
       axes:[
         {id:'v', lbl:'Quel plat ?', opts:[['a','une soupe'],['b','un café'],['c','une frite'],['d','un jus']]},
         {id:'q', lbl:'Quel format ?', opts:[['1','le plus petit'],['2','le plus grand']]}],
       out:{
         a1:{w:["Une petite soupe, s'il vous plaît."], say:"Une petite soupe, s'il vous plaît.", n:'féminin : un e de plus'},
         a2:{w:["Une grande soupe, s'il vous plaît."], say:"Une grande soupe, s'il vous plaît.", n:'féminin aussi'},
         b1:{w:["Un petit café, s'il vous plaît."], say:"Un petit café, s'il vous plaît.", n:'masculin : rien à ajouter'},
         b2:{w:["Un grand café, s'il vous plaît."], say:"Un grand café, s'il vous plaît.", n:'la commande du matin'},
         c1:{w:["Une petite frite, s'il vous plaît."], say:"Une petite frite, s'il vous plaît.", n:'féminin'},
         c2:{w:["Une grande frite, s'il vous plaît."], say:"Une grande frite, s'il vous plaît.", n:'assez pour deux'},
         d1:{w:["Un petit jus, s'il vous plaît."], say:"Un petit jus, s'il vous plaît.", n:'masculin'},
         d2:{w:["Un grand jus, s'il vous plaît."], say:"Un grand jus, s'il vous plaît.", n:'huit phrases toutes prêtes'},
       },
       note:"Huit phrases, toutes correctes, toutes utilisables telles quelles au comptoir."},

      {t:'ex', h:"À écouter et à répéter",
       p:"Six phrases pour ranger les formats.",
       rows:[
         ["Une petite soupe et un grand café.","un féminin, un masculin"],
         ["Quel format ? Moyen, s'il vous plaît.","la réponse la plus courte"],
         ["Une portion moyenne de frites.","moyenne prend deux n"],
         ["Un grand jus de pomme, pour emporter.","masculin"],
         ["Une grande salade, ça suffit pour deux.","féminin"],
         ["Trois formats, trois prix, un seul plat.","le sens de la ligne du menu"],
       ]},

      {t:'piege', h:"Trois pièges à connaître",
       rows:[
         ["oublier le e au féminin","« une petit soupe »",
          "Ça ne s'entend presque pas, mais ça s'écrit. Soupe, salade, frite, portion : tous féminins."],
         ["écrire « moyene »","une portion moyene",
          "« Moyen » double son n au féminin : <b>moyenne</b>. C'est le seul des trois qui fait ça."],
         ["inventer un quatrième format","« une soupe extra-large »",
          "Chez Marcel, il y a trois formats et pas un de plus. Si tu ne sais pas, demande : « Quels formats vous avez ? »"],
       ]},

      {t:'check', h:"Est-ce que c'est clair maintenant ?",
       p:"Quatre questions rapides.",
       qs:[
         {q:"Combien de formats au comptoir ?", opts:["deux","trois"], ok:1,
          fb:"Petit, moyen, grand."},
         {q:"« Une soupe ___ » (la plus petite)", opts:["petit","petite"], ok:1,
          fb:"Soupe est féminin : on ajoute un e."},
         {q:"Le féminin de « moyen » s'écrit…", opts:["moyene","moyenne"], ok:1,
          fb:"Deux n, comme dans « ancienne »."},
         {q:"Trois prix à côté d'un même plat veulent dire…", opts:["trois plats différents","trois formats"], ok:1,
          fb:"C'est le même plat : c'est la portion qui change."},
       ]},

      {t:'revoir', h:"À retenir",
       p:"<b>Petit · moyen · grand.</b> Trois mots, dans cet ordre. Devant un mot féminin : petit<b>e</b>, moyen<b>ne</b>, grand<b>e</b>. Et quand le préposé demande « Quel format ? », un seul mot suffit pour répondre."},
    ]
  },

  t1colonnes: {
    eye:'Mini-leçon', tit:'Lire un tableau de menu sans tout lire',
    blocs:[
      {t:'texte', h:"Un menu se lit par blocs, pas ligne par ligne",
       p:"Un tableau de casse-croûte contient cinquante mots ou plus. Personne ne les lit tous, pas même les gens nés ici : on cherche d'abord le <b>titre du bloc</b> — Sandwichs, Soupes, Breuvages — puis on descend seulement dans celui qui nous intéresse. C'est une stratégie de lecture, et elle s'apprend.",
       note:"Le programme appelle ça « lire un menu simple ». La compétence n'est pas de tout comprendre : c'est de trouver vite ce qu'on cherche."},

      {t:'ana', h:"Ce qu'il y a à gauche",
       p:"Les plats, rangés par famille.",
       mots:[['Le titre','SANDWICHS'],['Dessous','au poulet · aux œufs · au jambon',true],['Ce qui suit','servis avec salade ou frites']],
       say:"Sandwichs : au poulet, aux œufs, au jambon.",
       note:"La ligne « servi avec » est écrite une seule fois, en petit, sous le titre. Elle vaut pour tous les sandwichs du bloc."},

      {t:'ana', h:"Ce qu'il y a à droite",
       p:"Les prix, alignés au bout de chaque ligne.",
       mots:[['Un seul prix','le plat n\'a qu\'un format'],['Trois prix','trois formats : petit, moyen, grand',true],['Rien du tout','le prix est compris dans le trio']],
       say:"Trois prix : petit, moyen, grand.",
       note:"Quand une ligne porte trois prix, ils sont toujours dans le même ordre : du plus petit au plus grand, de gauche à droite."},

      {t:'ana', h:"Ce qu'il y a en bas, en petit",
       p:"C'est là que se cachent les conditions.",
       mots:[['Taxes en sus','le prix de la caisse est un peu plus haut'],['Comptant et débit seulement','pas de carte de crédit',true],['🍃','le plat est sans viande']],
       say:"Taxes en sus. Comptant et débit seulement.",
       note:"Trois lignes de rien du tout, et ce sont elles qui décident. Lis-les une fois, la première fois : après, tu les connais."},

      {t:'labo', h:"Où regarder ?",
       p:"Choisis ce que tu cherches, et vois où c'est écrit.",
       axes:[{id:'q', lbl:'Tu cherches quoi ?', opts:[
         ['a','ce qu\'il y a dans le sandwich'],
         ['b','le prix'],
         ['c','les formats'],
         ['d','ce qui vient avec'],
         ['e','comment payer']]}],
       out:{
         a:{w:["Après le nom du plat : « au poulet », « aux œufs »."], say:"Au poulet, aux œufs, au jambon.", n:'à gauche, sur la ligne du plat'},
         b:{w:["Au bout de la ligne, à droite."], say:"Le prix est au bout de la ligne.", n:'toujours à droite'},
         c:{w:["Trois prix côte à côte, sur la même ligne."], say:"Petit, moyen, grand.", n:'du plus petit au plus grand'},
         d:{w:["Sous le titre du bloc : « servis avec salade ou frites »."], say:"Servis avec salade ou frites.", n:'une fois pour tout le bloc'},
         e:{w:["Tout en bas de l'affiche, en petit."], say:"Comptant et débit seulement.", n:'les conditions sont toujours en bas'},
       },
       note:"Cinq endroits, et le tableau entier devient lisible."},

      {t:'ex', h:"À écouter et à répéter",
       p:"Six questions à poser devant le tableau.",
       rows:[
         ["Qu'est-ce qu'il y a dans ce sandwich ?","la question du bloc de gauche"],
         ["Ça vient avec quoi ?","pour l'accompagnement"],
         ["Il y a combien de formats ?","pour la ligne à trois prix"],
         ["Qu'est-ce que le trio comprend ?","la ligne la plus rentable"],
         ["Quelle est la soupe du jour ?","elle change tous les jours"],
         ["Est-ce que je peux payer avec ma carte ?","la ligne du bas"],
       ]},

      {t:'piege', h:"Trois pièges à connaître",
       rows:[
         ["croire que trois prix = trois plats","une soupe qui aurait trois recettes",
          "Non : c'est le même plat, en trois portions. Le nom n'est écrit qu'une fois."],
         ["oublier la ligne « servi avec »","payer la salade deux fois",
          "L'accompagnement est déjà dans le prix du sandwich. Elle est écrite en petit, sous le titre du bloc."],
         ["additionner les prix du trio","croire que le trio coûte la somme des trois",
          "Le trio a son propre prix, plus bas. C'est justement pour ça qu'il existe."],
       ]},

      {t:'check', h:"Est-ce que c'est clair maintenant ?",
       p:"Quatre questions rapides.",
       qs:[
         {q:"Pour lire un menu, on commence par…", opts:["la première ligne","le titre des blocs"], ok:1,
          fb:"On descend ensuite seulement dans le bloc utile."},
         {q:"Trois prix sur une même ligne veulent dire…", opts:["trois formats","trois plats"], ok:0,
          fb:"Du plus petit au plus grand, de gauche à droite."},
         {q:"« Servis avec salade ou frites » veut dire…", opts:["c'est compris","ça coûte plus cher"], ok:0,
          fb:"C'est l'accompagnement, et il est dans le prix."},
         {q:"« Taxes en sus » veut dire…", opts:["le prix est final","le prix va monter un peu"], ok:1,
          fb:"À la caisse, le montant sera un peu plus élevé."},
       ]},

      {t:'revoir', h:"À retenir",
       p:"Trois gestes, toujours les mêmes : je cherche le <b>titre du bloc</b>, je descends jusqu'à mon plat, je lis le <b>prix à droite</b>. Et une fois dans ma vie, je lis les petites lignes du bas."},
    ]
  },

  t1au: {
    eye:'Mini-leçon', tit:'Au poulet, à la tomate, aux légumes',
    blocs:[
      {t:'texte', h:"Le petit mot qui dit ce qu'il y a dedans",
       p:"Sur un menu, le nom du plat ne suffit jamais : « sandwich » ne dit pas ce qu'il y a entre les deux tranches de pain. C'est le mot d'après qui le dit — <b>au</b> poulet, <b>aux</b> œufs, <b>à la</b> tomate. Quatre formes seulement, et le choix ne dépend que du mot qui suit.",
       note:"C'est la même mécanique que « à l'oignon » ou « au chocolat » : une fois comprise, elle sert dans tout le menu, et au marché aussi."},

      {t:'ana', h:"Devant un mot masculin : au",
       p:"La forme la plus fréquente du menu.",
       mots:[['On dit','un sandwich {au} poulet'],['Aussi','un sandwich au jambon',true],['Et','un muffin au chocolat']],
       say:"Un sandwich au poulet, un sandwich au jambon.",
       note:"« Au » est en réalité « à » + « le » collés ensemble. On n'écrit jamais « à le poulet » : ça n'existe pas."},

      {t:'ana', h:"Devant un mot féminin : à la",
       p:"Les deux mots restent séparés.",
       mots:[['On dit','une soupe {à la} tomate'],['Aussi','une tarte à la pomme',true],['Et','une crêpe à la banane']],
       say:"Une soupe à la tomate, une tarte à la pomme.",
       note:"Ici, rien ne se colle : « à » et « la » gardent chacun leur place."},

      {t:'ana', h:"Devant une voyelle : à l'",
       p:"Pour que ce soit prononçable.",
       mots:[['On dit','une salade {à l\'}oignon'],['Aussi','un gâteau à l\'orange',true],['Jamais','« à la oignon »']],
       say:"Une salade à l'oignon, un gâteau à l'orange.",
       note:"C'est la même règle que « de l'eau » ou « l'accompagnement » : devant une voyelle, la voyelle du petit mot tombe."},

      {t:'ana', h:"Devant un pluriel : aux",
       p:"Une seule forme pour le masculin et le féminin.",
       mots:[['On dit','une soupe {aux} légumes'],['Aussi','un sandwich aux œufs',true],['Et','un muffin aux bleuets']],
       say:"Une soupe aux légumes, un sandwich aux œufs.",
       note:"Attention : « aux œufs » se prononce « au-zeu ». Le x se réveille devant la voyelle."},

      {t:'labo', h:"Quel petit mot ?",
       p:"Choisis un plat et son contenu.",
       axes:[
         {id:'v', lbl:'Quel plat ?', opts:[['a','un sandwich'],['b','une soupe'],['c','une salade']]},
         {id:'q', lbl:'Avec quoi ?', opts:[['1','poulet'],['2','légumes'],['3','oignon']]}],
       out:{
         a1:{w:["un sandwich {au} poulet"], say:"Un sandwich au poulet.", n:'poulet est masculin'},
         a2:{w:["un sandwich {aux} légumes"], say:"Un sandwich aux légumes.", n:'légumes est pluriel'},
         a3:{w:["un sandwich {à l\'}oignon"], say:"Un sandwich à l'oignon.", n:'oignon commence par une voyelle'},
         b1:{w:["une soupe {au} poulet"], say:"Une soupe au poulet.", n:"c'est le plat qui est féminin, pas le contenu"},
         b2:{w:["une soupe {aux} légumes"], say:"Une soupe aux légumes.", n:'la soupe la plus courante du menu'},
         b3:{w:["une soupe {à l\'}oignon"], say:"Une soupe à l'oignon.", n:'un classique des casse-croûte'},
         c1:{w:["une salade {au} poulet"], say:"Une salade au poulet.", n:'même forme que le sandwich'},
         c2:{w:["une salade {aux} légumes"], say:"Une salade aux légumes.", n:'pluriel'},
         c3:{w:["une salade {à l\'}oignon"], say:"Une salade à l'oignon.", n:'neuf phrases, une seule règle'},
       },
       note:"Regarde bien : le plat à gauche ne change jamais le petit mot. C'est le mot d'après qui décide, toujours."},

      {t:'ex', h:"À écouter et à répéter",
       p:"Six commandes du menu.",
       rows:[
         ["Un sandwich au poulet, s'il vous plaît.","masculin"],
         ["Une soupe aux légumes, format moyen.","pluriel"],
         ["Un sandwich aux œufs et un jus de pomme.","le x se prononce"],
         ["Une soupe à la tomate, c'est la soupe du jour.","féminin"],
         ["Une salade à l'oignon, s'il vous plaît.","devant une voyelle"],
         ["Un sandwich sans mayonnaise.","après « sans », plus rien"],
       ]},

      {t:'piege', h:"Trois pièges à connaître",
       rows:[
         ["dire « à le »","« un sandwich à le poulet »",
          "Ça n'existe pas en français : « à » et « le » se collent obligatoirement en <b>au</b>."],
         ["regarder le plat au lieu du contenu","« une soupe à la légumes »",
          "Le plat peut être féminin et le contenu masculin ou pluriel. Le petit mot regarde ce qui vient <b>après</b> lui."],
         ["mettre quelque chose après « sans »","« sans de la mayonnaise »",
          "Après <b>sans</b>, on met le nom tout nu : sans mayonnaise, sans oignon, sans fromage."],
       ]},

      {t:'check', h:"Est-ce que c'est clair maintenant ?",
       p:"Quatre questions rapides.",
       qs:[
         {q:"« Un sandwich ___ jambon »", opts:["au","à la"], ok:0,
          fb:"Jambon est masculin."},
         {q:"« Une soupe ___ légumes »", opts:["à la","aux"], ok:1,
          fb:"Légumes est au pluriel."},
         {q:"« Une salade ___ oignon »", opts:["à la","à l'"], ok:1,
          fb:"Oignon commence par une voyelle."},
         {q:"« Un sandwich sans ___ »", opts:["mayonnaise","de la mayonnaise"], ok:0,
          fb:"Après « sans », le nom reste tout nu."},
       ]},

      {t:'revoir', h:"À retenir",
       p:"Regarde le mot qui vient <b>après</b> : masculin → <b>au</b> · féminin → <b>à la</b> · voyelle → <b>à l'</b> · pluriel → <b>aux</b>. Le nom du plat, lui, n'a aucun mot à dire."},
    ]
  },

  t1ce: {
    eye:'Mini-leçon', tit:'Ce sandwich-là, c\'est quoi ?',
    blocs:[
      {t:'texte', h:"Le mot qui sauve quand on ne sait pas le nom",
       p:"Devant un tableau de menu, il arrive qu'on ne sache pas comment se dit ce qu'on veut. On le voit sur la photo, on le montre du doigt — et il faut une phrase. Cette phrase existe, elle est courte, et tout le monde l'emploie : « <b>Ce sandwich-là</b>, c'est quoi ? »",
       note:"C'est une des stratégies les plus utiles du niveau : montrer plutôt que nommer, en attendant de savoir nommer."},

      {t:'ana', h:"Devant un mot masculin : ce",
       p:"La forme de base.",
       mots:[['On dit','{ce} sandwich'],['Aussi','ce trio · ce plateau',true],['Et','ce format · ce breuvage']],
       say:"Ce sandwich, ce trio, ce plateau.",
       note:"« Ce » se prononce comme le début de « cerise ». Il est très court : ne l'allonge pas."},

      {t:'ana', h:"Devant une voyelle : cet",
       p:"Un t apparaît, pour que ça se prononce.",
       mots:[['On dit','{cet} accompagnement'],['Aussi','cet extra · cet ustensile',true],['Jamais','« ce accompagnement »']],
       say:"Cet accompagnement, cet extra, cet ustensile.",
       note:"Le t se prononce et se colle au mot suivant : « ce-taccompagnement »."},

      {t:'ana', h:"Devant un mot féminin : cette",
       p:"Deux t et un e, mais ça se prononce comme « cet ».",
       mots:[['On dit','{cette} soupe'],['Aussi','cette salade · cette portion',true],['Et','cette caisse · cette file']],
       say:"Cette soupe, cette salade, cette portion.",
       note:"« Cet » et « cette » sonnent pareil. La différence ne se voit qu'à l'écrit — et elle dépend du genre du mot, pas du son."},

      {t:'ana', h:"Le petit -là qui montre",
       p:"Au Québec, il s'ajoute presque toujours quand on pointe du doigt.",
       mots:[['On dit','{ce sandwich-là}'],['Aussi','cette soupe-là · ce trio-là',true],['Avec la main','on montre en même temps qu\'on parle']],
       say:"Ce sandwich-là, c'est quoi ?",
       note:"Le trait d'union est obligatoire à l'écrit. À l'oral, le « -là » se prononce clairement, un peu plus fort que le reste."},

      {t:'labo', h:"Montrer un plat",
       p:"Choisis un plat et une question.",
       axes:[
         {id:'v', lbl:'Quel plat ?', opts:[['a','sandwich'],['b','soupe'],['c','accompagnement'],['d','frites']]},
         {id:'q', lbl:'Quelle question ?', opts:[['1','c\'est quoi ?'],['2','c\'est combien ?']]}],
       out:{
         a1:{w:["Ce sandwich-là, c'est quoi ?"], say:"Ce sandwich-là, c'est quoi ?", n:'masculin'},
         a2:{w:["Ce sandwich-là, c'est combien ?"], say:"Ce sandwich-là, c'est combien ?", n:'la question du prix'},
         b1:{w:["Cette soupe-là, c'est quoi ?"], say:"Cette soupe-là, c'est quoi ?", n:'féminin'},
         b2:{w:["Cette soupe-là, c'est combien ?"], say:"Cette soupe-là, c'est combien ?", n:'féminin aussi'},
         c1:{w:["Cet accompagnement-là, c'est quoi ?"], say:"Cet accompagnement-là, c'est quoi ?", n:'devant une voyelle'},
         c2:{w:["Cet accompagnement-là, c'est combien ?"], say:"Cet accompagnement-là, c'est combien ?", n:'souvent : rien, c\'est compris'},
         d1:{w:["Ces frites-là, c'est quoi ?"], say:"Ces frites-là, c'est quoi ?", n:'pluriel'},
         d2:{w:["Ces frites-là, c'est combien ?"], say:"Ces frites-là, c'est combien ?", n:'huit phrases toutes prêtes'},
       },
       note:"Huit phrases, et aucune n'a besoin du nom exact du plat. C'est exactement ce qu'on cherche."},

      {t:'ex', h:"À écouter et à répéter",
       p:"Six phrases à dire en montrant du doigt.",
       rows:[
         ["Ce sandwich-là, c'est quoi ?","masculin"],
         ["Cette soupe-là, elle est aux légumes ?","féminin"],
         ["Cet accompagnement est compris ?","devant une voyelle"],
         ["Ces breuvages-là sont dans le trio ?","pluriel"],
         ["Je voudrais ce trio-là, s'il vous plaît.","la commande la plus simple du monde"],
         ["Cette portion-là est trop grande pour moi.","féminin"],
       ]},

      {t:'piege', h:"Trois pièges à connaître",
       rows:[
         ["dire « ce » devant une voyelle","« ce accompagnement »",
          "Impossible à prononcer : deux voyelles se heurtent. C'est pour ça que le t de <b>cet</b> existe."],
         ["écrire « cet » pour un mot féminin","« cet soupe »",
          "Ça se prononce pareil, mais ça s'écrit <b>cette</b>. À l'oral personne ne s'en aperçoit ; à l'écrit, oui."],
         ["oublier le trait d'union","« ce sandwich là »",
          "Avec le trait d'union, « -là » se colle au nom : <b>ce sandwich-là</b>. Sans lui, « là » veut dire l'endroit."],
       ]},

      {t:'check', h:"Est-ce que c'est clair maintenant ?",
       p:"Quatre questions rapides.",
       qs:[
         {q:"« ___ soupe est aux légumes. »", opts:["Cet","Cette"], ok:1,
          fb:"Soupe est féminin."},
         {q:"« ___ accompagnement est compris ? »", opts:["Ce","Cet"], ok:1,
          fb:"Le mot commence par une voyelle."},
         {q:"« Cet » et « cette » se prononcent…", opts:["pareil","différemment"], ok:0,
          fb:"La différence est seulement à l'écrit."},
         {q:"Pour montrer du doigt, on ajoute…", opts:["-là","-ci"], ok:0,
          fb:"« -là » est la forme employée partout au Québec."},
       ]},

      {t:'revoir', h:"À retenir",
       p:"Masculin → <b>ce</b> · voyelle → <b>cet</b> · féminin → <b>cette</b> · pluriel → <b>ces</b>. Et une phrase à garder dans la poche : « <b>Ce sandwich-là, c'est quoi ?</b> »"},
    ]
  },

  t2voudrais: {
    eye:'Mini-leçon', tit:'Je voudrais — la formule polie du comptoir',
    blocs:[
      {t:'texte', h:"Une seule syllabe sépare le poli du sec",
       p:"« Je <b>veux</b> un café » et « Je <b>voudrais</b> un café » veulent dire la même chose. Mais la première sonne comme un ordre, et la seconde comme une demande. Au comptoir, dans un magasin, au téléphone : c'est toujours la seconde qu'on emploie. C'est ce que le programme appelle le <b>conditionnel de politesse</b>.",
       note:"Ce n'est pas une question de gentillesse personnelle : c'est la formule normale, celle que tout le monde emploie. Ne pas l'employer se remarque."},

      {t:'ana', h:"La phrase de base",
       p:"Trois morceaux, toujours dans le même ordre.",
       mots:[['On dit','{je voudrais} un café'],['Puis','ce qu\'on veut',true],['Et à la fin','s\'il vous plaît']],
       say:"Je voudrais un café, s'il vous plaît.",
       note:"Cette phrase seule permet de commander n'importe quoi, n'importe où. C'est la phrase la plus rentable du module."},

      {t:'ana', h:"Les deux autres formes, aussi bonnes",
       p:"On les entend toutes les trois dans la même file.",
       mots:[['On dit','{j\'aimerais} une soupe'],['Ou','je prendrais un jus',true],['Toutes les trois','veulent dire la même chose']],
       say:"J'aimerais une soupe. Je prendrais un jus.",
       note:"Choisis-en une et garde-la : il vaut mieux une formule bien tenue que trois à moitié."},

      {t:'ana', h:"Pour demander la permission",
       p:"Quand on ne commande pas, mais qu'on demande.",
       mots:[['On dit','{est-ce que je peux avoir} une serviette ?'],['Plus poli encore','pourrais-je avoir du sel ?',true],['Très courant','je peux avoir une cuillère, s\'il vous plaît ?']],
       say:"Est-ce que je peux avoir une serviette ?",
       note:"C'est la phrase du plateau : elle sert à demander un ustensile, un condiment, un sac, un couvercle."},

      {t:'labo', h:"Poli ou sec ?",
       p:"Choisis ce que tu veux et la façon de le demander.",
       axes:[
         {id:'v', lbl:'Tu veux quoi ?', opts:[['a','un café'],['b','une soupe'],['c','une serviette']]},
         {id:'q', lbl:'Comment ?', opts:[['1','sec'],['2','poli']]}],
       out:{
         a1:{w:["Je veux un café."], say:"Je veux un café.", n:'compris, mais dur à entendre'},
         a2:{w:["Je voudrais un café, s'il vous plaît."], say:"Je voudrais un café, s'il vous plaît.", n:'la formule du comptoir'},
         b1:{w:["Donnez-moi une soupe."], say:"Donnez-moi une soupe.", n:'un ordre, pas une demande'},
         b2:{w:["J'aimerais une soupe, s'il vous plaît."], say:"J'aimerais une soupe, s'il vous plaît.", n:'même chose, en poli'},
         c1:{w:["Une serviette."], say:"Une serviette.", n:'trop court : ça se remarque'},
         c2:{w:["Est-ce que je peux avoir une serviette ?"], say:"Est-ce que je peux avoir une serviette ?", n:'la phrase du plateau'},
       },
       note:"Compare la ligne du haut et celle du bas : c'est le même contenu, et ce n'est pas du tout la même personne qu'on entend."},

      {t:'ex', h:"À écouter et à répéter",
       p:"Six demandes polies.",
       rows:[
         ["Je voudrais un café, s'il vous plaît.","la phrase à retenir avant toutes les autres"],
         ["Je voudrais un trio au poulet, s'il vous plaît.","la commande complète"],
         ["J'aimerais une soupe aux légumes.","l'autre forme"],
         ["Est-ce que je peux avoir une cuillère ?","demander, pas commander"],
         ["Pourrais-je avoir du sel, s'il vous plaît ?","la forme la plus polie"],
         ["Merci beaucoup, bonne journée !","on finit toujours par là"],
       ]},

      {t:'piege', h:"Trois pièges à connaître",
       rows:[
         ["oublier le d","« je voudrai » au lieu de « je voudrais »",
          "Un s à la fin, et un d au milieu. « Je voudrai » est un futur : ce n'est pas la même phrase."],
         ["mettre « s'il vous plaît » au début","« S'il vous plaît je voudrais un café »",
          "Ce n'est pas faux, mais la place normale est à la fin. Là, il ferme la demande."],
         ["tutoyer le préposé","« Tu me donnes un café ? »",
          "Au comptoir, on ne se connaît pas : on vouvoie. Le tutoiement se garde pour les camarades de classe."],
       ]},

      {t:'check', h:"Est-ce que c'est clair maintenant ?",
       p:"Quatre questions rapides.",
       qs:[
         {q:"La formule polie pour commander est…", opts:["je veux","je voudrais"], ok:1,
          fb:"Une syllabe de plus, et tout change."},
         {q:"« S'il vous plaît » se met…", opts:["à la fin","au début"], ok:0,
          fb:"C'est ce qui ferme la demande."},
         {q:"Pour demander une serviette, on dit…", opts:["Une serviette.","Est-ce que je peux avoir une serviette ?"], ok:1,
          fb:"On demande, on ne commande pas."},
         {q:"Au comptoir, on…", opts:["tutoie","vouvoie"], ok:1,
          fb:"On ne connaît pas le préposé."},
       ]},

      {t:'revoir', h:"À retenir",
       p:"Une phrase, et elle ouvre toutes les portes : « <b>Je voudrais</b> … , <b>s'il vous plaît.</b> » Pour ce qui n'est pas une commande : « <b>Est-ce que je peux avoir</b> … ? »"},
    ]
  },

  t2questions: {
    eye:'Mini-leçon', tit:'Les cinq questions du préposé',
    blocs:[
      {t:'texte', h:"Ce n'est pas toi qui parles le plus",
       p:"Commander, ce n'est pas seulement dire ce qu'on veut : c'est surtout <b>répondre</b>. Le préposé pose toujours les mêmes questions, dans le même ordre, à toute la file. Cinq questions, cinq réponses de deux mots. Quand on les connaît, la file cesse d'être un moment difficile.",
       note:"Le programme met cette situation en compréhension orale autant qu'en production : « comprendre l'information donnée par le préposé ». C'est le cœur du défi."},

      {t:'ana', h:"« Ce sera tout ? »",
       p:"Il te demande si tu as fini de commander.",
       mots:[['Il dit','Ce sera tout ?'],['Tu réponds','{oui c\'est tout}, merci',true],['Ou','Non, j\'aimerais aussi une soupe']],
       say:"Ce sera tout ? Oui, c'est tout, merci.",
       note:"On entend aussi « Autre chose ? » ou « Avec ça ? » : ce sont les mêmes mots pour la même question."},

      {t:'ana', h:"« Avec salade ou avec frites ? »",
       p:"Il te fait choisir ton accompagnement.",
       mots:[['Il dit','Avec salade ou avec frites ?'],['Tu réponds','{avec salade s\'il vous plaît}',true],['Ou','Avec frites, s\'il vous plaît']],
       say:"Avec salade ou avec frites ? Avec salade, s'il vous plaît.",
       note:"Cette question ne vient que si ton plat est servi avec quelque chose. Elle te dit donc, au passage, que c'est compris dans le prix."},

      {t:'ana', h:"« Quel format ? »",
       p:"Il attend un seul mot.",
       mots:[['Il dit','{quel format} ?'],['Tu réponds','Petit, s\'il vous plaît',true],['Trois choix','petit · moyen · grand']],
       say:"Quel format ? Moyen, s'il vous plaît.",
       note:"Inutile de répéter le nom du plat : il vient d'être dit. Un mot et « s'il vous plaît », c'est parfait."},

      {t:'ana', h:"« Pour ici ou pour emporter ? »",
       p:"La question qui surprend le plus au début.",
       mots:[['Il dit','{pour ici ou pour emporter} ?'],['Tu manges sur place','Pour ici',true],['Tu pars avec','{pour emporter}']],
       say:"Pour ici ou pour emporter ? Pour ici.",
       note:"« Pour emporter » veut dire dans un sac, avec un couvercle. Si tu réponds « pour ici », le repas arrive sur un plateau."},

      {t:'ana', h:"« Débit ou comptant ? »",
       p:"Il demande comment tu paies.",
       mots:[['Il dit','{débit ou comptant} ?'],['Avec la carte','Débit, s\'il vous plaît',true],['Avec de l\'argent','Comptant, s\'il vous plaît']],
       say:"Débit ou comptant ? Débit, s'il vous plaît.",
       note:"« Comptant » veut dire en argent, en billets et en pièces. Beaucoup de casse-croûte ne prennent pas la carte de crédit."},

      {t:'labo', h:"La question et la réponse",
       p:"Choisis une question et vois la réponse à donner.",
       axes:[{id:'q', lbl:'Il te demande quoi ?', opts:[
         ['a','Ce sera tout ?'],
         ['b','Avec salade ou avec frites ?'],
         ['c','Quel format ?'],
         ['d','Pour ici ou pour emporter ?'],
         ['e','Débit ou comptant ?']]}],
       out:{
         a:{w:["Oui, c'est tout, merci."], say:"Oui, c'est tout, merci.", n:'ou : Non, j\'aimerais aussi…'},
         b:{w:["Avec salade, s'il vous plaît."], say:"Avec salade, s'il vous plaît.", n:'un des deux, jamais les deux'},
         c:{w:["Moyen, s'il vous plaît."], say:"Moyen, s'il vous plaît.", n:'un seul mot suffit'},
         d:{w:["Pour ici."], say:"Pour ici.", n:'deux mots, pas plus'},
         e:{w:["Débit, s'il vous plaît."], say:"Débit, s'il vous plaît.", n:'la carte, ou l\'argent'},
       },
       note:"Cinq questions, cinq réponses. Apprends-les par cœur : c'est vingt secondes de travail pour toute une année de dîners."},

      {t:'ex', h:"À écouter et à répéter",
       p:"Six échanges complets.",
       rows:[
         ["Ce sera tout ? — Oui, c'est tout, merci.","la fin de la commande"],
         ["Avec salade ou avec frites ? — Avec salade, s'il vous plaît.","l'accompagnement"],
         ["Quel format ? — Petit, s'il vous plaît.","un seul mot"],
         ["Pour ici ou pour emporter ? — Pour emporter.","le sac et le couvercle"],
         ["Débit ou comptant ? — Débit, s'il vous plaît.","le paiement"],
         ["Votre numéro est le 42. — Merci beaucoup.","on retient le chiffre"],
       ]},

      {t:'piege', h:"Trois pièges à connaître",
       rows:[
         ["répondre « oui » à une question à deux choix","« Avec salade ou avec frites ? — Oui. »",
          "La question offre deux choses : il faut en nommer une. « Oui » ne dit rien, et le préposé redemande."],
         ["ne pas retenir son numéro","aller au poste de ramassage sans savoir son chiffre",
          "Le numéro est dit à voix haute et écrit sur le reçu. Regarde le reçu tout de suite : c'est le plus simple."],
         ["croire que « comptant » veut dire « tout de suite »","payer comptant avec sa carte",
          "« Comptant » veut dire en argent : billets et pièces. Avec la carte, on dit « débit »."],
       ]},

      {t:'check', h:"Est-ce que c'est clair maintenant ?",
       p:"Quatre questions rapides.",
       qs:[
         {q:"« Pour emporter » veut dire…", opts:["je mange ici","je pars avec mon repas"], ok:1,
          fb:"Le repas arrive dans un sac, avec un couvercle."},
         {q:"À « Quel format ? », on répond…", opts:["par un mot","par une phrase complète"], ok:0,
          fb:"Petit, moyen ou grand — et « s'il vous plaît »."},
         {q:"« Comptant » veut dire…", opts:["en argent","avec la carte"], ok:0,
          fb:"Avec la carte, on dit « débit »."},
         {q:"À « Avec salade ou avec frites ? », répondre « oui »…", opts:["suffit","ne répond pas à la question"], ok:1,
          fb:"Il faut nommer l'un des deux."},
       ]},

      {t:'revoir', h:"À retenir",
       p:"Cinq questions, toujours les mêmes : <b>Ce sera tout ? · Avec salade ou avec frites ? · Quel format ? · Pour ici ou pour emporter ? · Débit ou comptant ?</b> Et cinq réponses de deux mots."},
    ]
  },

  t3partitif: {
    eye:'Mini-leçon', tit:'Du sel, de la moutarde, des serviettes',
    blocs:[
      {t:'texte', h:"Demander un peu de quelque chose",
       p:"Sur le plateau, il manque souvent une petite chose : du sel, de la moutarde, une serviette. On ne demande pas « un sel » — le sel ne se compte pas. On demande <b>du</b> sel : un peu, sans dire combien. Le français a un petit mot exprès pour ça, et il change selon le nom qui suit.",
       note:"Le programme nomme cette liste dans son lexique de la situation : ustensiles, serviettes de table, condiments. C'est le vocabulaire du plateau."},

      {t:'ana', h:"Devant un mot masculin : du",
       p:"Ce qui ne se compte pas et qui est masculin.",
       mots:[['On dit','{du sel}'],['Aussi','du poivre · du sucre',true],['Et','{du ketchup} · du lait']],
       say:"Du sel, du poivre, du sucre, du ketchup.",
       note:"On ne dit pas combien parce qu'on ne le sait pas : un peu, ce qu'il faut. C'est justement à ça que sert ce petit mot."},

      {t:'ana', h:"Devant un mot féminin : de la",
       p:"Les deux mots restent séparés.",
       mots:[['On dit','{de la moutarde}'],['Aussi','de la mayonnaise',true],['Et','de la crème pour le café']],
       say:"De la moutarde, de la mayonnaise, de la crème.",
       note:"Même mécanique que « à la tomate » : devant un nom féminin, rien ne se colle."},

      {t:'ana', h:"Devant une voyelle : de l'",
       p:"Pour que ce soit prononçable.",
       mots:[['On dit','{de l\'eau}'],['Aussi','de l\'huile',true],['Jamais','« de la eau »']],
       say:"De l'eau, de l'huile.",
       note:"C'est la troisième fois que cette règle revient dans le module : « à l'oignon », « l'accompagnement », « de l'eau »."},

      {t:'ana', h:"Devant un pluriel : des",
       p:"Là, on peut compter — mais on ne compte pas.",
       mots:[['On dit','{des serviettes}'],['Aussi','{des ustensiles} · des sachets',true],['Et','des frites · des légumes']],
       say:"Des serviettes, des ustensiles, des sachets.",
       note:"« Des » sert quand il y en a plusieurs et qu'on ne dit pas combien. Si tu veux en dire le nombre, dis-le : « deux serviettes »."},

      {t:'ana', h:"Quand on précise la quantité",
       p:"Après un nombre ou une mesure, tout se simplifie.",
       mots:[['On dit','{un peu de sel}'],['Aussi','deux serviettes',true],['Et','un sachet de ketchup']],
       say:"Un peu de sel, deux serviettes, un sachet de ketchup.",
       note:"Dès qu'on dit la quantité, on ne garde que <b>de</b> : un peu <b>de</b> sel, un sachet <b>de</b> ketchup. Jamais « un peu du sel »."},

      {t:'labo', h:"Quel petit mot ?",
       p:"Choisis ce que tu demandes.",
       axes:[{id:'q', lbl:'Tu demandes quoi ?', opts:[
         ['a','sel'],
         ['b','moutarde'],
         ['c','eau'],
         ['d','serviettes'],
         ['e','un peu de sel']]}],
       out:{
         a:{w:["Est-ce que je peux avoir {du} sel ?"], say:"Est-ce que je peux avoir du sel ?", n:'masculin'},
         b:{w:["Est-ce que je peux avoir {de la} moutarde ?"], say:"Est-ce que je peux avoir de la moutarde ?", n:'féminin'},
         c:{w:["Est-ce que je peux avoir {de l\'}eau ?"], say:"Est-ce que je peux avoir de l'eau ?", n:'devant une voyelle'},
         d:{w:["Est-ce que je peux avoir {des} serviettes ?"], say:"Est-ce que je peux avoir des serviettes ?", n:'pluriel'},
         e:{w:["Je voudrais juste {un peu de} sel."], say:"Je voudrais juste un peu de sel.", n:'la quantité est dite : seulement « de »'},
       },
       note:"Cinq phrases, et elles couvrent tout ce qu'on demande au bout d'un comptoir."},

      {t:'ex', h:"À écouter et à répéter",
       p:"Six demandes du plateau.",
       rows:[
         ["Est-ce que je peux avoir du sel ?","masculin"],
         ["Je voudrais de la moutarde, s'il vous plaît.","féminin"],
         ["Est-ce qu'il y a de l'eau quelque part ?","devant une voyelle"],
         ["Il me faut des serviettes de table.","pluriel"],
         ["Un peu de sucre dans le café, s'il vous plaît.","la quantité est dite"],
         ["Deux sachets de ketchup, ça suffit.","après un nombre : seulement « de »"],
       ]},

      {t:'piege', h:"Trois pièges à connaître",
       rows:[
         ["dire « un sel »","« un sel, s'il vous plaît »",
          "Le sel ne se compte pas : on en prend un peu. On dit <b>du</b> sel. Ce qui se compte, ce sont les sachets."],
         ["garder « du » après une quantité","« un peu du sel »",
          "Dès qu'on dit combien, il ne reste que <b>de</b> : un peu <b>de</b> sel, un sachet <b>de</b> ketchup."],
         ["dire « de la » devant une voyelle","« de la eau »",
          "Deux voyelles se heurtent. On dit <b>de l'</b>eau, comme « à l'oignon »."],
       ]},

      {t:'check', h:"Est-ce que c'est clair maintenant ?",
       p:"Quatre questions rapides.",
       qs:[
         {q:"« Est-ce que je peux avoir ___ moutarde ? »", opts:["du","de la"], ok:1,
          fb:"Moutarde est féminin."},
         {q:"« ___ eau », on écrit…", opts:["de la","de l'"], ok:1,
          fb:"Devant une voyelle, la voyelle tombe."},
         {q:"« Un peu ___ sel »", opts:["de","du"], ok:0,
          fb:"La quantité est dite : il ne reste que « de »."},
         {q:"Pour plusieurs serviettes, on dit…", opts:["de la serviettes","des serviettes"], ok:1,
          fb:"Au pluriel, c'est toujours « des »."},
       ]},

      {t:'revoir', h:"À retenir",
       p:"Masculin → <b>du</b> · féminin → <b>de la</b> · voyelle → <b>de l'</b> · pluriel → <b>des</b>. Et dès que tu dis la quantité, il ne reste que <b>de</b>."},
    ]
  },

  t3demander: {
    eye:'Mini-leçon', tit:'Il manque quelque chose sur mon plateau',
    blocs:[
      {t:'texte', h:"Signaler sans se fâcher, en une phrase",
       p:"Il manque une cuillère, ou le jus n'est pas là, ou ce n'est pas la bonne commande. Ça arrive à tout le monde, tous les jours, et ça se règle en une phrase courte. Le ton n'a pas besoin d'être fâché : au contraire, plus la phrase est simple et calme, plus la solution arrive vite.",
       note:"C'est un des moments où un élève de niveau 3 renonce et repart sans rien dire. Trois phrases apprises d'avance suffisent à l'éviter."},

      {t:'ana', h:"Il manque quelque chose",
       p:"Deux façons, également bonnes.",
       mots:[['On dit','{je n\'ai pas de cuillère}'],['Ou','{il manque le jus}',true],['Puis','on attend, sans rien ajouter']],
       say:"Je n'ai pas de cuillère. Il manque le jus.",
       note:"Après « je n'ai pas », on dit <b>de</b> : je n'ai pas <b>de</b> cuillère, pas <b>de</b> serviette. Jamais « je n'ai pas une cuillère »."},

      {t:'ana', h:"Demander où c'est",
       p:"Souvent, il n'y a rien à demander : c'est en libre-service.",
       mots:[['On dit','{où sont les serviettes} ?'],['Ou','Où est le ketchup ?',true],['On répond souvent','{servez-vous}']],
       say:"Où sont les serviettes ? Servez-vous.",
       note:"« Servez-vous » veut dire : prends-en toi-même, autant qu'il t'en faut, sans demander. C'est une invitation, pas un reproche."},

      {t:'ana', h:"Demander la permission",
       p:"Quand tu veux en prendre plus d'un.",
       mots:[['On dit','{est-ce que je peux en prendre deux} ?'],['Le petit mot en','remplace la chose dont on parle',true],['Réponse','Bien sûr · Servez-vous']],
       say:"Est-ce que je peux en prendre deux ?",
       note:"« En » évite de répéter : au lieu de « prendre deux serviettes », on dit « en prendre deux ». Tout le monde comprend de quoi il s'agit."},

      {t:'ana', h:"Ce n'est pas ma commande",
       p:"La phrase la plus utile du poste de ramassage.",
       mots:[['On dit','Excusez-moi, {ce n\'est pas ma commande}'],['On ajoute','J\'ai commandé un sandwich au poulet',true],['Et','Mon numéro est le 42']],
       say:"Excusez-moi, ce n'est pas ma commande.",
       note:"Le numéro règle tout : il est écrit sur ton reçu. Montre-le plutôt que de le dire, s'il y a du bruit."},

      {t:'ana', h:"Quand on n'a pas compris",
       p:"Dans le bruit, tout le monde le dit.",
       mots:[['On dit','Pardon ?'],['Ou','{pouvez-vous répéter}, s\'il vous plaît ?',true],['Ou encore','Plus lentement, s\'il vous plaît']],
       say:"Pouvez-vous répéter, s'il vous plaît ?",
       note:"Ce n'est pas impoli et ce n'est pas un aveu : un casse-croûte est un endroit bruyant, et les préposés parlent vite."},

      {t:'labo', h:"Quelle phrase dire ?",
       p:"Choisis la situation.",
       axes:[{id:'q', lbl:'Qu\'est-ce qui se passe ?', opts:[
         ['a','pas de cuillère'],
         ['b','tu cherches les serviettes'],
         ['c','tu veux du ketchup'],
         ['d','le jus manque'],
         ['e','ce n\'est pas ton plat']]}],
       out:{
         a:{w:["Excusez-moi, je n'ai pas de cuillère."], say:"Excusez-moi, je n'ai pas de cuillère.", n:'après « pas », toujours « de »'},
         b:{w:["Où sont les serviettes, s'il vous plaît ?"], say:"Où sont les serviettes, s'il vous plaît ?", n:'souvent en libre-service'},
         c:{w:["Est-ce que je peux avoir du ketchup ?"], say:"Est-ce que je peux avoir du ketchup ?", n:'un condiment : « du »'},
         d:{w:["Il manque le jus dans mon plateau."], say:"Il manque le jus dans mon plateau.", n:'court et calme'},
         e:{w:["Excusez-moi, ce n'est pas ma commande. Mon numéro est le 42."], say:"Excusez-moi, ce n'est pas ma commande. Mon numéro est le 42.", n:'le numéro règle tout'},
       },
       note:"Cinq situations, cinq phrases. Elles couvrent presque tout ce qui peut arriver au bout d'un comptoir."},

      {t:'ex', h:"À écouter et à répéter",
       p:"Six phrases du poste de ramassage.",
       rows:[
         ["Excusez-moi, je n'ai pas de cuillère.","le manque le plus fréquent"],
         ["Il manque le jus dans mon plateau.","court et calme"],
         ["Où sont les serviettes, s'il vous plaît ?","demander où"],
         ["Est-ce que je peux en prendre deux ?","le petit mot « en »"],
         ["Excusez-moi, ce n'est pas ma commande.","au poste de ramassage"],
         ["Pouvez-vous répéter, s'il vous plaît ?","dans le bruit"],
       ]},

      {t:'piege', h:"Trois pièges à connaître",
       rows:[
         ["dire « je n'ai pas une cuillère »","une cuillère au lieu de de cuillère",
          "Après une négation, « un », « une » et « des » deviennent <b>de</b> : je n'ai pas <b>de</b> cuillère."],
         ["s'excuser trop longtemps","« je suis vraiment désolé de vous déranger, peut-être que… »",
          "Une phrase suffit, et « excusez-moi » en tête. Plus c'est long, moins c'est clair dans le bruit."],
         ["partir sans rien dire","reprendre son plateau incomplet",
          "C'est le vrai risque de ce moment-là. Une cuillère qui manque se règle en trois secondes — à condition de parler."],
       ]},

      {t:'check', h:"Est-ce que c'est clair maintenant ?",
       p:"Quatre questions rapides.",
       qs:[
         {q:"« Je n'ai pas ___ cuillère. »", opts:["une","de"], ok:1,
          fb:"Après une négation, « une » devient « de »."},
         {q:"« Servez-vous » veut dire…", opts:["prends-en toi-même","attends que je te serve"], ok:0,
          fb:"C'est une invitation à se servir soi-même."},
         {q:"Au poste de ramassage, ce qui règle tout, c'est…", opts:["ton numéro","ton nom"], ok:0,
          fb:"Il est écrit sur ton reçu."},
         {q:"Demander de répéter est…", opts:["impoli","normal"], ok:1,
          fb:"Un casse-croûte est un endroit bruyant."},
       ]},

      {t:'revoir', h:"À retenir",
       p:"Trois phrases dans la poche : « <b>Je n'ai pas de</b> … » · « <b>Il manque</b> … » · « <b>Excusez-moi, ce n'est pas ma commande.</b> » Et une quatrième pour le bruit : « <b>Pouvez-vous répéter ?</b> »"},
    ]
  },

  t3plus: {
    eye:'Mini-leçon', tit:"Il n'y en a plus",
    blocs:[
      {t:'texte', h:"La réponse qu'on n'attendait pas",
       p:"On a choisi, on a fait la file, et le préposé répond : « Il n'y a <b>plus de</b> soupe. » <b>ne… plus</b> veut dire qu'il y en avait, et qu'il n'y en a maintenant plus. Ce n'est pas la même chose que « il n'y a <b>pas</b> de soupe » — celle-là voudrait dire qu'on n'en fait jamais.",
       note:"Dans un casse-croûte, ça arrive tous les jours après une heure et demie. C'est une phrase à reconnaître à l'oreille, du premier coup."},

      {t:'ana', h:"La phrase complète",
       p:"Deux morceaux autour du verbe.",
       mots:[['On dit','{il n\'y a plus de soupe}'],['Le ne','se met avant le verbe',true],['Le plus','se met après le verbe']],
       say:"Il n'y a plus de soupe aujourd'hui.",
       note:"C'est la même construction que « ne… pas » : deux morceaux qui entourent le verbe. Ici, le second est <b>plus</b>."},

      {t:'ana', h:"Après « plus », toujours « de »",
       p:"Jamais « du », jamais « des ».",
       mots:[['On dit','plus {de} soupe'],['Aussi','{plus de frites} · plus de lait',true],['Devant une voyelle','plus d\'eau']],
       say:"Plus de frites, plus de lait, plus d'eau.",
       note:"C'est la même règle qu'après une négation ordinaire : « je n'ai pas <b>de</b> cuillère », « il n'y a plus <b>de</b> frites »."},

      {t:'ana', h:"La forme courte du comptoir",
       p:"Quand le plat vient d'être nommé.",
       mots:[['Tu demandes','Un jus de pomme, s\'il vous plaît'],['Il répond','{il n\'en reste plus}',true],['Le petit mot en','remplace « de jus de pomme »']],
       say:"Il n'en reste plus. Il n'y en a plus.",
       note:"« Il n'en reste plus » et « il n'y en a plus » veulent exactement la même chose. Les deux s'entendent au comptoir."},

      {t:'ana', h:"Ce qu'on répond",
       p:"Trois phrases, et la file avance.",
       mots:[['On dit','Ce n\'est pas grave'],['Ou','{qu\'est-ce que vous avez d\'autre} ?',true],['Ou','Alors je vais prendre autre chose']],
       say:"Ce n'est pas grave. Qu'est-ce que vous avez d'autre ?",
       note:"La deuxième est la plus utile : elle relance le préposé, qui va nommer ce qui reste. C'est lui qui connaît la cuisine."},

      {t:'labo', h:"Il n'en reste plus",
       p:"Choisis ce qui manque.",
       axes:[
         {id:'v', lbl:'Il manque quoi ?', opts:[['a','la soupe'],['b','les frites'],['c','l\'eau froide']]},
         {id:'q', lbl:'Quelle forme ?', opts:[['1','la phrase complète'],['2','la forme courte']]}],
       out:{
         a1:{w:["Il n'y a {plus de} soupe aujourd'hui."], say:"Il n'y a plus de soupe aujourd'hui.", n:'masculin ou féminin : toujours « de »'},
         a2:{w:["Il n'en reste plus."], say:"Il n'en reste plus.", n:'« en » remplace « de soupe »'},
         b1:{w:["Il n'y a {plus de} frites."], say:"Il n'y a plus de frites.", n:'pluriel : « de » quand même'},
         b2:{w:["Il n'en reste plus."], say:"Il n'en reste plus.", n:'la même forme courte'},
         c1:{w:["Il n'y a {plus d\'}eau froide."], say:"Il n'y a plus d'eau froide.", n:"devant une voyelle : « d' »"},
         c2:{w:["Il n'y en a plus."], say:"Il n'y en a plus.", n:"l'autre forme courte"},
       },
       note:"Six phrases : trois que le préposé dit, trois que tu dois reconnaître à l'oreille."},

      {t:'ex', h:"À écouter et à répéter",
       p:"Six phrases de fin de journée.",
       rows:[
         ["Il n'y a plus de soupe aujourd'hui.","la phrase complète"],
         ["Il n'y a plus de frites : la friteuse est fermée.","avec la raison"],
         ["Il n'en reste plus, désolé.","la forme courte"],
         ["Il n'y a plus de trios après trois heures.","une règle de l'endroit"],
         ["Ce n'est pas grave. Qu'est-ce que vous avez d'autre ?","ta réponse"],
         ["Alors je vais prendre un sandwich.","et la file avance"],
       ]},

      {t:'piege', h:"Trois pièges à connaître",
       rows:[
         ["dire « plus des frites »","garder « des » après plus",
          "Après <b>plus</b>, il ne reste que <b>de</b> : plus <b>de</b> frites, plus <b>de</b> lait, plus <b>d'</b>eau."],
         ["confondre « plus » et « pas »","« il n'y a pas de soupe » pour « il n'y en a plus »",
          "« Pas » veut dire qu'on n'en fait jamais ; « plus » veut dire que c'est fini pour aujourd'hui. Reviens demain."],
         ["entendre le contraire","comprendre « il y en a plus » comme « il y en a beaucoup »",
          "À l'oral, le <b>ne</b> tombe souvent : « y'en a plus » veut dire qu'il n'y en a <b>pas</b>. C'est le ton qui le dit."],
       ]},

      {t:'check', h:"Est-ce que c'est clair maintenant ?",
       p:"Quatre questions rapides.",
       qs:[
         {q:"« Il n'y a plus ___ frites. »", opts:["des","de"], ok:1,
          fb:"Après « plus », il ne reste que « de »."},
         {q:"« Il n'en reste plus » veut dire…", opts:["c'est fini pour aujourd'hui","on n'en fait jamais"], ok:0,
          fb:"« Plus » dit qu'il y en avait avant."},
         {q:"Le petit mot « en » remplace…", opts:["le plat dont on parle","la personne"], ok:0,
          fb:"Il évite de répéter le nom du plat."},
         {q:"La meilleure réponse est…", opts:["« Qu'est-ce que vous avez d'autre ? »","se taire et partir"], ok:0,
          fb:"Le préposé va nommer ce qui reste."},
       ]},

      {t:'revoir', h:"À retenir",
       p:"« Il n'y a <b>plus de</b> … » ou, en plus court, « <b>Il n'en reste plus.</b> » Après <b>plus</b>, toujours <b>de</b>. Et la réponse qui relance : « <b>Qu'est-ce que vous avez d'autre ?</b> »"},
    ]
  },
};
