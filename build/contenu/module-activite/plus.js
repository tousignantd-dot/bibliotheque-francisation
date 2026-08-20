const PLUS = {
  prTarif: {
    eye:'Mini-leçon', tit:"Entendre les chiffres du premier coup",
    blocs:[
      {t:'texte', h:"Le moment où tout se joue",
       p:"On comprend toute la conversation, et puis arrive le montant. « Quatre-vingt-quinze » ou « quatre-vingt-cinq » ? Une syllabe sépare dix dollars. Les chiffres sont le seul endroit d'une inscription où se tromper coûte vraiment quelque chose.",
       note:"Bonne nouvelle : il n'y a que trois dizaines difficiles en français, et elles reviennent tout le temps."},

      {t:'ana', h:"Les trois dizaines difficiles",
       p:"70, 80 et 90 ne sont pas des mots simples : ce sont des calculs.",
       mots:[['70','soixante-{dix}'],['80','quatre-vingts',true],['90','quatre-vingt-{dix}']],
       say:"Quatre-vingt-cinq dollars pour les résidents.",
       note:"Le reste est régulier : vingt, trente, quarante, cinquante, soixante, cent. Ce sont bien ces trois-là qui font hésiter."},

      {t:'ana', h:"Le piège de 60 et 70",
       p:"« Soixante » et « soixante-dix » commencent exactement pareil. Il faut écouter la suite.",
       mots:[['60','soixante — {rien} après'],['70','soixante-{dix}',true],['75','soixante-{quinze}']],
       say:"Soixante-quinze dollars.",
       note:"Le même piège existe entre 80 et 90 : « quatre-vingts » s'arrête, « quatre-vingt-dix » continue. Attendez la fin du mot."},

      {t:'ana', h:"Les heures officielles",
       p:"Les horaires écrits emploient les heures de 13 à 24. À l'oral, les gens disent souvent l'autre forme.",
       mots:[['Écrit','19 h'],['Dit souvent','{sept} heures du soir',true],['Écrit','21 h — neuf heures']],
       say:"C'est de dix-neuf à vingt et une heures.",
       note:"Les deux formes sont correctes. Un dépliant écrira 19 h ; la personne au comptoir dira « sept heures ». C'est la même heure."},

      {t:'texte', h:"Le réflexe qui règle tout",
       p:"<b>Faites répéter le montant.</b> « Quatre-vingt-cinq, c'est bien ça ? » Personne ne trouve cela impoli — au contraire, la personne en face est soulagée. Un montant mal entendu se découvre au moment de payer, et c'est bien plus embarrassant.",
       note:"Cette phrase de six mots est la plus rentable de la séance. Apprenez-la telle quelle."},

      {t:'labo', h:"Écoutez et comparez",
       p:"Choisissez une paire de nombres qui se ressemblent.",
       axes:[{id:'p', lbl:'Quelle paire ?', opts:[
         ['a','85 et 95'],
         ['b','60 et 75'],
         ['c','110 et 120'],
         ['d','9 h et 19 h'],
         ['e','12 et 20 semaines']]}],
       out:{
         a:{w:['quatre-vingt-{cinq} dollars'], say:"Quatre-vingt-cinq dollars pour les résidents.", n:'85 — écoutez la fin : cinq, pas quinze'},
         b:{w:['soixante-{quinze} dollars'], say:"Soixante-quinze dollars.", n:'75 — il y a un mot après « soixante »'},
         c:{w:['cent {dix} dollars'], say:"Cent dix dollars pour les autres.", n:'110 — cent, puis dix'},
         d:{w:['{neuf} heures'], say:"De neuf heures à dix heures.", n:'9 h — le matin'},
         e:{w:['{douze} semaines'], say:"Douze semaines, de septembre à décembre.", n:'12 — la durée de la session'},
       },
       note:"Réécoutez chaque extrait deux fois avant de regarder la réponse. La deuxième écoute est presque toujours la bonne."},

      {t:'ex', h:"Les chiffres du module",
       p:"Écoutez chacun et répétez-le à voix haute.",
       rows:[
         ["Quatre-vingt-cinq dollars pour les résidents.","85 $ — le tarif résident"],
         ["Cent dix pour les autres.","110 $ — le tarif non-résident"],
         ["De neuf heures à dix heures.","9 h à 10 h — le cours du samedi"],
         ["Douze semaines, de septembre à décembre.","12 — la session"],
         ["C'est de dix-neuf à vingt et une heures.","19 h à 21 h — la chorale"],
         ["Trente dollars pour dix semaines.","30 $ et 10 semaines"],
       ]},

      {t:'piege', h:"Trois pièges à connaître",
       rows:[
         ["confondre cinq et quinze","« quatre-vingt-cinq » et « quatre-vingt-quinze »",
          "Dix dollars d'écart, une syllabe de différence. C'est l'erreur la plus fréquente sur les prix. Faites répéter."],
         ["s'arrêter d'écouter à « soixante »","« soixante » ou « soixante-quinze » ?",
          "Le nombre n'est pas fini. Attendez la fin du mot avant de noter quoi que ce soit."],
         ["croire que 19 h et 7 h sont deux heures différentes","19 h = sept heures du soir",
          "Le dépliant écrit 19 h, la personne dit « sept heures ». C'est le même moment."],
       ]},

      {t:'check', h:"Est-ce que c'est clair maintenant ?",
       p:"Quatre questions rapides.",
       qs:[
         {q:"« Quatre-vingt-quinze » vaut…", opts:["85","95"], ok:1,
          fb:"quatre-vingt + quinze = 95."},
         {q:"Si vous entendez « soixante » et que la personne continue…", opts:["c'est 60","le nombre n'est pas fini"], ok:1,
          fb:"« soixante-quinze », « soixante-dix » : attendez la fin."},
         {q:"19 h correspond à…", opts:["sept heures du soir","neuf heures du soir"], ok:0,
          fb:"19 − 12 = 7. Sept heures du soir."},
         {q:"Faire répéter un montant est…", opts:["impoli","tout à fait normal"], ok:1,
          fb:"C'est même ce que font les gens d'ici."},
       ]},
    ]
  },

  t1imperso: {
    eye:'Mini-leçon', tit:"Il faut, il est important de",
    blocs:[
      {t:'texte', h:"Une règle qui ne vise personne",
       p:"« Il faut une preuve de résidence. » Ce <b>il</b> ne désigne personne : ce n'est ni vous, ni moi, ni la personne au comptoir. C'est une forme <b>impersonnelle</b>, et elle sert à énoncer une règle qui vaut pour tout le monde.",
       note:"C'est la langue des dépliants, des formulaires et des consignes. Vous la lirez plus souvent que vous ne la direz."},

      {t:'ana', h:"il faut + un nom ou un verbe",
       p:"La forme la plus courte et la plus fréquente à l'oral.",
       mots:[['Avec un nom','{il faut} une preuve'],['Avec un verbe','il faut arriver à l\'heure',true],['Jamais','« il faut que j\'arrive » à l\'écrit simple']],
       say:"Il faut une preuve de résidence pour le tarif résident.",
       note:"Cette forme ne dit pas <em>qui</em> doit le faire. C'est justement ce qui la rend commode : elle s'adresse à tout le monde à la fois."},

      {t:'ana', h:"il est + adjectif + de + verbe",
       p:"La forme écrite, celle des dépliants et des affiches.",
       mots:[['La structure','il est {important} de'],['Autres adjectifs','préférable · nécessaire · interdit',true],['Exemple','il est préférable de rester']],
       say:"Il est important d'arriver dix minutes d'avance.",
       note:"« Il est interdit de » est la version stricte. « Il est préférable de » est un conseil, pas une obligation — la nuance compte."},

      {t:'ana', h:"Quand la personne compte : que + subjonctif",
       p:"Pour désigner quelqu'un en particulier, on ajoute <b>que</b>. Le verbe qui suit change alors de forme.",
       mots:[['Sans personne','il faut arriver tôt'],['Avec personne','il faut {que vous soyez} là',true],['Autre','il est important qu\'il n\'ait pas peur']],
       say:"Il faut que vous soyez là à neuf heures.",
       note:"Cette forme s'appelle le subjonctif. Le programme du cours demande de la <b>reconnaître</b>, pas de la produire — c'est un objectif raisonnable."},

      {t:'texte', h:"Ce que ça change pour vous",
       p:"Quand vous entendez <b>il faut</b> ou <b>il est important</b>, une condition arrive. Notez-la. C'est presque toujours quelque chose à apporter, une heure à respecter, ou un document à fournir — c'est-à-dire exactement ce qui vous fera revenir une deuxième fois si vous l'oubliez.",
       note:"Écoutez ces deux expressions comme une sonnette : ce qui suit est important."},

      {t:'labo', h:"Quelle forme, et pourquoi ?",
       p:"Choisissez une phrase du module.",
       axes:[{id:'p', lbl:'Quelle phrase ?', opts:[
         ['a','une preuve de résidence'],
         ['b',"arriver dix minutes d'avance"],
         ['c','les parents restent dans la salle'],
         ['d','vous êtes là à neuf heures'],
         ["e","il n'a pas peur de l'eau"]]}],
       out:{
         a:{w:['{Il faut} une preuve de résidence.'], say:"Il faut une preuve de résidence.", n:'il faut + un nom — le plus court'},
         b:{w:["{Il est important d'}arriver d'avance."], say:"Il est important d'arriver dix minutes d'avance.", n:'il est + adjectif + de + verbe'},
         c:{w:['{Il est préférable que} les parents restent.'], say:"Il est préférable que les parents restent dans la salle.", n:'que + subjonctif — un conseil, pas une obligation'},
         d:{w:['{Il faut que} vous soyez là.'], say:"Il faut que vous soyez là à neuf heures.", n:'que + subjonctif — la personne est désignée'},
         e:{w:["{Il est important qu'}il n'ait pas peur."], say:"Il est important qu'il n'ait pas peur de l'eau.", n:'que + subjonctif — la seule vraie condition'},
       },
       note:"Comparez b et c : « il est important de » ne vise personne, « il est préférable que » vise les parents. Le <b>que</b> fait toute la différence."},

      {t:'ex', h:"Les conditions du module",
       p:"Écoutez chacune. Qu'est-ce qui est exigé, au juste ?",
       rows:[
         ["Il faut une preuve de résidence.","un document"],
         ["Il est important d'arriver dix minutes d'avance.","une heure"],
         ["Il faut apporter un maillot et une serviette.","du matériel"],
         ["Il est préférable que les parents restent dans la salle.","un conseil, pas une obligation"],
         ["Il faut que vous soyez là à neuf heures.","une heure, pour vous en particulier"],
         ["Il est important qu'il n'ait pas peur de l'eau.","la seule condition d'admission"],
       ]},

      {t:'piege', h:"Trois pièges à connaître",
       rows:[
         ["confondre obligatoire et préférable","« il faut » oblige, « il est préférable » conseille",
          "Un bonnet de bain obligatoire vous empêche d'entrer dans l'eau. Un conseil, non. Écoutez lequel des deux vous entendez."],
         ["chercher qui est ce « il »","il ne désigne personne",
          "Dans « il faut », le <b>il</b> est vide. Ne cherchez pas de quelle personne on parle : la règle s'adresse à tout le monde."],
         ["vouloir produire le subjonctif tout de suite","le reconnaître suffit à ce niveau",
          "« Il faut arriver tôt » est parfaitement correct et évite le subjonctif. Employez-le sans hésiter."],
       ]},

      {t:'check', h:"Est-ce que c'est clair maintenant ?",
       p:"Quatre questions rapides.",
       qs:[
         {q:"Dans « il faut une preuve », le mot « il » désigne…", opts:["la personne au comptoir","personne"], ok:1,
          fb:"C'est une forme impersonnelle : le <b>il</b> est vide."},
         {q:"« Il est préférable que » annonce…", opts:["une obligation","un conseil"], ok:1,
          fb:"« Il faut » oblige ; « il est préférable » conseille."},
         {q:"Après « il faut que », le verbe…", opts:["change de forme","reste au présent ordinaire"], ok:0,
          fb:"C'est le subjonctif : « que vous soyez », « qu'il ait »."},
         {q:"À ce niveau, on vous demande…", opts:["de produire le subjonctif","de le reconnaître"], ok:1,
          fb:"Le reconnaître suffit. « Il faut arriver tôt » évite la difficulté."},
       ]},
    ]
  },

  t1sup: {
    eye:'Mini-leçon', tit:"Le plus, le moins",
    blocs:[
      {t:'texte', h:"Choisir parmi trente activités",
       p:"Un dépliant municipal contient une trentaine d'activités. Pour choisir, on compare : la moins chère, la plus proche, celle qui a le plus de places. C'est le <b>superlatif</b>, et il se construit en ajoutant un seul petit mot.",
       note:"Vous savez déjà comparer deux choses. Le superlatif compare une chose à <b>toutes</b> les autres."},

      {t:'ana', h:"Comparer deux choses",
       p:"C'est ce que vous savez déjà faire : plus, moins ou aussi, suivi de <b>que</b>.",
       mots:[['Supérieur','{plus} chère que'],['Inférieur','moins chère que',true],['Égal','aussi chère que']],
       say:"La natation est plus chère que la chorale.",
       note:"L'adjectif s'accorde avec ce dont on parle : plus cher, plus chère, plus chers, plus chères."},

      {t:'ana', h:"Comparer avec tout le reste",
       p:"On ajoute <b>le</b>, <b>la</b> ou <b>les</b> devant plus ou moins. C'est tout.",
       mots:[['Deux choses','moins chère que'],['Toutes les choses','{la moins} chère',true],['Le groupe','la moins chère de toutes']],
       say:"C'est la moins chère de toutes les activités.",
       note:"Le petit mot s'accorde avec le nom : <b>le</b> cours le plus court, <b>l'</b>activité la plus chère, <b>les</b> places les moins chères."},

      {t:'texte', h:"Le groupe se marque avec « de »",
       p:"Ce à quoi on compare s'introduit par <b>de</b>, jamais par « dans » : « la moins chère <b>de</b> toutes », « le plus proche <b>du</b> quartier », « la meilleure <b>de</b> la session ».",
       note:"C'est une des rares constructions où le français n'a qu'une seule possibilité. Tant mieux."},

      {t:'ana', h:"Le cas de « bon »",
       p:"<b>bon</b> ne suit pas la règle : il devient <b>meilleur</b>, et « le meilleur » au superlatif.",
       mots:[['Comparaison','{meilleur} que'],['Superlatif','le {meilleur}',true],['Jamais','« plus bon »']],
       say:"C'est le meilleur moment de la semaine.",
       note:"L'adverbe <em>bien</em> a la même particularité : il devient <b>mieux</b>. « Elle nage mieux que l'an passé. »"},

      {t:'labo', h:"Deux choses, ou toutes ?",
       p:"Choisissez une phrase et voyez quelle forme elle demande.",
       axes:[{id:'p', lbl:'Quelle phrase ?', opts:[
         ['a','la natation et la chorale'],
         ['b','la chorale et les trente activités'],
         ['c','le cours du samedi et celui du mardi'],
         ['d','les places de ce dépliant'],
         ['e','le jeudi soir, pour Rosa']]}],
       out:{
         a:{w:['La natation est {plus chère que} la chorale.'], say:"La natation est plus chère que la chorale.", n:'deux choses › plus … que'},
         b:{w:["C'est {la moins chère de} toutes."], say:"C'est la moins chère de toutes les activités.", n:'toutes les choses › le superlatif'},
         c:{w:['Le samedi est {plus proche que} le mardi.'], say:"Le cours du samedi est plus proche que celui du mardi.", n:'deux choses › plus … que'},
         d:{w:['Ce sont {les moins chères} du dépliant.'], say:"Ces places-là sont les moins chères du dépliant.", n:'pluriel › les moins'},
         e:{w:["C'est {le meilleur} moment de la semaine."], say:"C'est le meilleur moment de la semaine.", n:'bon › meilleur, jamais « plus bon »'},
       },
       note:"Le test : y a-t-il un <b>que</b> après ? Alors on compare deux choses. Sinon, c'est un superlatif."},

      {t:'ex', h:"Les comparaisons du module",
       p:"Écoutez chacune et repérez la forme.",
       rows:[
         ["La natation est plus chère que la chorale.","comparaison — deux choses"],
         ["C'est la moins chère de toutes les activités.","superlatif"],
         ["Le cours du samedi est plus proche que celui du mardi.","comparaison"],
         ["C'est celle qui a le moins de places disponibles.","superlatif"],
         ["Ces places-là sont les moins chères du dépliant.","superlatif au pluriel"],
         ["C'est le meilleur moment de la semaine.","superlatif irrégulier"],
       ]},

      {t:'piege', h:"Trois pièges à connaître",
       rows:[
         ["dire « plus bon »","c'est « meilleur »",
          "Un seul adjectif fait exception, mais c'est un des plus employés. « Meilleur que », « le meilleur »."],
         ["oublier l'accord du petit mot","« la moins chère », « les moins chères »",
          "le, la ou les s'accorde avec le nom, exactement comme un article."],
         ["employer « dans » au lieu de « de »","« la moins chère de toutes », pas « dans toutes »",
          "Le groupe de comparaison s'introduit toujours par <b>de</b>. C'est mécanique."],
       ]},

      {t:'check', h:"Est-ce que c'est clair maintenant ?",
       p:"Quatre questions rapides.",
       qs:[
         {q:"« La chorale est ___ chère de toutes » demande…", opts:["moins","la moins"], ok:1,
          fb:"On compare à toutes les autres : c'est un superlatif."},
         {q:"Le contraire de « pire » pour l'adjectif bon, c'est…", opts:["plus bon","meilleur"], ok:1,
          fb:"« Plus bon » n'existe pas."},
         {q:"Le groupe de comparaison s'introduit par…", opts:["de","dans"], ok:0,
          fb:"« la moins chère <b>de</b> toutes »."},
         {q:"S'il y a un « que » après, on compare…", opts:["deux choses","une chose à toutes les autres"], ok:0,
          fb:"« plus chère <b>que</b> » compare deux choses."},
       ]},
    ]
  },

  t2imper: {
    eye:'Mini-leçon', tit:"Prenez-la, ne la lâchez pas",
    blocs:[
      {t:'texte', h:"Le petit mot qui change de place",
       p:"Au bord d'une piscine, les consignes sont courtes : « Prenez-la. » « Ne la lâchez pas. » Le pronom est le même, le verbe est le même — mais il n'est pas au même endroit. C'est la seule chose à comprendre.",
       note:"Cette règle vaut pour toutes les consignes, pas seulement à la piscine : recettes, modes d'emploi, consignes de sécurité."},

      {t:'ana', h:"À l'affirmative : le pronom suit",
       p:"Il se colle après le verbe, avec un trait d'union.",
       mots:[['La forme','{Prenez-la}'],['Le trait d\'union','obligatoire',true],['Autres','Compte-les · Envoie-le']],
       say:"Prenez la planche à deux mains. Tenez-la bien devant vous.",
       note:"Autres exemples du module : <em>regarde-moi</em>, <em>assieds-toi</em>, <em>mets-toi à côté de Sofia</em>, <em>laissez-les au bord</em>."},

      {t:'ana', h:"À la négative : le pronom précède",
       p:"Tout change de place. Le pronom repasse devant le verbe, et le trait d'union disparaît.",
       mots:[['La forme','{Ne la lâchez pas}'],['Trait d\'union','aucun',true],['Autres','Ne te lève pas · Ne les jetez pas']],
       say:"Ne la lâchez pas.",
       note:"Le <b>ne</b> et le <b>pas</b> entourent l'ensemble « pronom + verbe ». Le pronom est à l'intérieur."},

      {t:'ana', h:"me devient moi, te devient toi",
       p:"À l'affirmative seulement. À la négative, ils reprennent leur forme courte.",
       mots:[['Affirmatif','Regarde-{moi}'],['Négatif','Ne {me} regarde pas',true],['Aussi','Assieds-toi / Ne te lève pas']],
       say:"Mateo, regarde-moi. Souffle dans l'eau.",
       note:"C'est la seule irrégularité de la leçon, et elle ne touche que deux pronoms."},

      {t:'texte', h:"Deux pronoms ensemble",
       p:"« Donne les serviettes aux enfants » devient « <b>Donne-les-leur</b>. » L'ordre est : verbe, puis <b>le / la / les</b>, puis <b>moi / lui / leur</b>. C'est la forme la plus difficile du français parlé courant — il suffit de la reconnaître.",
       note:"Vous l'entendrez souvent. Vous n'avez pas à la produire pour être compris."},

      {t:'labo', h:"Affirmatif ou négatif ?",
       p:"Choisissez une consigne du module.",
       axes:[{id:'p', lbl:'Quelle consigne ?', opts:[
         ['a','tenir la planche'],
         ['b','ne pas lâcher la planche'],
         ['c','compter les enfants'],
         ['d','ne pas chercher l\'enfant'],
         ['e','donner les serviettes aux enfants']]}],
       out:{
         a:{w:['{Tenez-la} bien devant vous.'], say:"Tenez-la bien devant vous.", n:'affirmatif › le pronom suit, trait d\'union'},
         b:{w:['{Ne la lâchez pas.}'], say:"Ne la lâchez pas.", n:'négatif › le pronom précède, sans trait d\'union'},
         c:{w:['{Compte-les} quand ils entrent.'], say:"Compte-les quand ils entrent dans l'eau.", n:'affirmatif › le pronom suit'},
         d:{w:['{Ne le cherche pas} toi-même.'], say:"Tu ne le cherches pas toi-même.", n:'négatif › le pronom précède'},
         e:{w:['{Donne-les-leur} à la sortie.'], say:"Donne-les-leur à la sortie, pas avant.", n:'deux pronoms : le/la/les puis moi/lui/leur'},
       },
       note:"Comparez a et b : le même verbe, le même pronom, deux places différentes. C'est toute la leçon."},

      {t:'ex', h:"Les consignes du module",
       p:"Écoutez chacune et repérez la place du pronom.",
       rows:[
         ["Tenez-la bien devant vous.","affirmatif — après le verbe"],
         ["Ne la lâchez pas.","négatif — avant le verbe"],
         ["Mets-toi à côté de Sofia.","affirmatif — toi, pas te"],
         ["Ne te lève pas, reste assis.","négatif — te, forme courte"],
         ["Compte-les quand ils entrent dans l'eau.","affirmatif"],
         ["Donne-les-leur à la sortie.","deux pronoms"],
       ]},

      {t:'piege', h:"Trois pièges à connaître",
       rows:[
         ["garder le pronom après le verbe à la négative","« ne la lâchez pas », jamais « ne lâchez-la pas »",
          "À la négative, tout revient devant. C'est l'erreur la plus fréquente, parce qu'on garde en tête la forme affirmative."],
         ["oublier le trait d'union","« prenez-la », pas « prenez la »",
          "Sans trait d'union, « prenez la » attend un nom : prenez la planche. Le trait d'union montre que le pronom remplace le nom."],
         ["dire « regarde-me »","c'est « regarde-moi »",
          "À l'affirmative, me devient moi et te devient toi. Deux pronoms, une seule règle à retenir."],
       ]},

      {t:'check', h:"Est-ce que c'est clair maintenant ?",
       p:"Quatre questions rapides.",
       qs:[
         {q:"« Ne lâchez pas la planche » devient…", opts:["Ne lâchez-la pas","Ne la lâchez pas"], ok:1,
          fb:"À la négative, le pronom passe devant le verbe."},
         {q:"« Prenez la planche » devient…", opts:["Prenez-la","La prenez"], ok:0,
          fb:"À l'affirmative, le pronom suit, avec un trait d'union."},
         {q:"À l'affirmative, « me » devient…", opts:["moi","m'"], ok:0,
          fb:"« Regarde-moi », « écoute-moi »."},
         {q:"Le trait d'union s'emploie…", opts:["aux deux formes","seulement à l'affirmative"], ok:1,
          fb:"À la négative, il n'y en a pas."},
       ]},
    ]
  },

  t2quant: {
    eye:'Mini-leçon', tit:"Chaque, plusieurs, quelques",
    blocs:[
      {t:'texte', h:"Dire combien sans donner de chiffre",
       p:"« Chaque cours », « plusieurs parents », « quelques places ». Ces mots disent une quantité sans la compter. Ils sont partout dans les consignes et les dépliants, et chacun impose sa propre forme au nom qui suit.",
       note:"Trois mots, trois comportements différents. C'est ce qui les rend faciles à confondre."},

      {t:'ana', h:"chaque — un par un, au singulier",
       p:"Toujours suivi d'un nom au <b>singulier</b>. Il insiste sur le fait qu'on les prend un à la fois.",
       mots:[['Le nom qui suit','{singulier}'],['Exemple','chaque cours',true],['Jamais','« chaque cours<u>s</u> »']],
       say:"Chaque cours reprend ce qui a été vu.",
       note:"« Chaque enfant doit avoir son propre bonnet » : un enfant à la fois, un bonnet chacun. C'est le sens même du mot."},

      {t:'ana', h:"plusieurs — un bon nombre, au pluriel",
       p:"Toujours suivi d'un nom au <b>pluriel</b>. Plus que deux, sans dire combien.",
       mots:[['Le nom qui suit','{pluriel}'],['Exemple','plusieurs parents',true],['Jamais','« plusieurs parent »']],
       say:"Plusieurs parents s'installent devant la vitre.",
       note:"<b>plusieurs</b> ne change jamais de forme : il n'a pas de masculin ni de féminin."},

      {t:'ana', h:"quelques — un petit nombre",
       p:"Pluriel aussi, mais peu. C'est le mot qui dit qu'il n'en reste pas beaucoup.",
       mots:[['Le nom qui suit','{pluriel}'],['Exemple','quelques places',true],['Attention','« quelque chose » est autre chose']],
       say:"Il reste quelques places dans la chorale.",
       note:"Ne pas confondre avec <b>quelque chose</b>, qui est un mot différent et toujours au singulier."},

      {t:'texte', h:"tous les — sans exception",
       p:"« <b>Tous les</b> samedis, de neuf à dix heures. » Cette forme veut dire exactement la même chose que « chaque samedi ». Les deux sont justes ; « tous les » est plus fréquent à l'oral.",
       note:"À l'oral, on entend aussi <b>bien des</b> pour « beaucoup de » : « bien des parents arrivent en retard »."},

      {t:'labo', h:"Singulier ou pluriel après ?",
       p:"Choisissez un déterminant et voyez ce qu'il exige.",
       axes:[{id:'p', lbl:'Quel déterminant ?', opts:[
         ['a','chaque'],
         ['b','plusieurs'],
         ['c','quelques'],
         ['d','tous les'],
         ['e','bien des']]}],
       out:{
         a:{w:['{chaque} cours'], say:"Chaque cours reprend ce qui a été vu.", n:'nom au singulier — un par un'},
         b:{w:['{plusieurs} parents'], say:"Plusieurs parents s'installent devant la vitre.", n:'nom au pluriel — un bon nombre'},
         c:{w:['{quelques} places'], say:"Il reste quelques places dans la chorale.", n:'nom au pluriel — peu'},
         d:{w:['{tous les} samedis'], say:"Le cours a lieu tous les samedis.", n:'nom au pluriel — sans exception'},
         e:{w:['{bien des} parents'], say:"Bien des parents arrivent en retard.", n:'nom au pluriel — beaucoup, à l\'oral'},
       },
       note:"Un seul des cinq demande le singulier : <b>chaque</b>. C'est le seul point à retenir absolument."},

      {t:'ex', h:"Les quantités du module",
       p:"Écoutez chacune et repérez le nom qui suit.",
       rows:[
         ["Chaque cours reprend ce qui a été vu.","singulier"],
         ["Chaque enfant doit avoir son propre bonnet.","singulier"],
         ["Plusieurs parents s'installent devant la vitre.","pluriel"],
         ["Il reste quelques places dans la chorale.","pluriel"],
         ["Le cours a lieu tous les samedis.","pluriel"],
         ["Bien des parents arrivent en retard.","pluriel, à l'oral"],
       ]},

      {t:'piege', h:"Trois pièges à connaître",
       rows:[
         ["mettre un s après chaque","« chaque cours », jamais « chaques »",
          "<b>chaque</b> ne prend jamais de s et le nom qui suit reste au singulier. C'est le contraire de ce qu'on attendrait."],
         ["confondre quelques et quelque chose","deux mots différents",
          "« quelques places » (plusieurs) et « quelque chose » (une chose indéterminée) n'ont rien à voir."],
         ["croire que plusieurs s'accorde","il ne change jamais",
          "« plusieurs parents », « plusieurs activités » : la même forme au masculin et au féminin."],
       ]},

      {t:'check', h:"Est-ce que c'est clair maintenant ?",
       p:"Quatre questions rapides.",
       qs:[
         {q:"Après « chaque », le nom est…", opts:["au singulier","au pluriel"], ok:0,
          fb:"« chaque cours », « chaque enfant »."},
         {q:"« Plusieurs » au féminin s'écrit…", opts:["plusieures","plusieurs"], ok:1,
          fb:"Il ne change jamais de forme."},
         {q:"« Tous les samedis » veut dire…", opts:["la même chose que chaque samedi","seulement certains samedis"], ok:0,
          fb:"Les deux formes sont équivalentes."},
         {q:"« Il reste quelques places » veut dire…", opts:["beaucoup de places","peu de places"], ok:1,
          fb:"<b>quelques</b> annonce un petit nombre."},
       ]},
    ]
  },

  t3depliant: {
    eye:'Mini-leçon', tit:"Lire un dépliant en deux minutes",
    blocs:[
      {t:'texte', h:"Quatre pages, trente activités",
       p:"Un dépliant municipal n'est pas fait pour être lu en entier. Il est fait pour qu'on y <b>trouve</b> quelque chose. Quatre conventions suffisent, et elles sont les mêmes d'une ville à l'autre.",
       note:"Une fois ces quatre conventions connues, n'importe quel dépliant se lit en deux minutes."},

      {t:'ana', h:"La colonne de gauche : le tri",
       p:"Elle donne le nom de l'activité et l'âge demandé. Si l'âge ne convient pas, rien d'autre ne compte : passez à la ligne suivante.",
       mots:[['Ce qu\'on y lit','le nom et l\'{âge}'],['À quoi ça sert','éliminer vite',true],['Le réflexe','lire l\'âge en premier']],
       say:"Regarde d'abord la colonne de gauche : c'est le nom de l'activité et l'âge.",
       note:"Commencer par ce qui vous <b>élimine</b> — l'âge, le jour, le tarif — fait gagner beaucoup de temps."},

      {t:'ana', h:"Les trois chiffres, toujours dans le même ordre",
       p:"Tarif résident, tarif non-résident, nombre de semaines.",
       mots:[['Premier','{85} — résident'],['Deuxième','110 — non-résident',true],['Troisième','12 — semaines']],
       say:"Le premier, c'est le prix pour les résidents. Le deuxième, pour les autres.",
       note:"Un écart important entre les deux premiers chiffres rend la preuve de résidence très rentable : ici, vingt-cinq dollars."},

      {t:'ana', h:"Les symboles renvoient à la légende",
       p:"Une étoile, un astérisque, une couleur : chacun a un sens, expliqué en bas de la page.",
       mots:[['Le symbole','une {étoile}'],['Ce que ça dit','peu de places',true],['Où le lire','la légende, en bas']],
       say:"Ça veut dire qu'il reste peu de places. En bas de la page, la légende l'explique.",
       note:"La légende est toujours en petits caractères. C'est justement là que se trouve l'information qui change une décision."},

      {t:'texte', h:"Ce qu'un dépliant ne dit jamais",
       p:"S'il reste vraiment des places <b>aujourd'hui</b>. Le dépliant a été imprimé des semaines avant la session : l'étoile signale qu'il y en avait peu à l'impression, rien de plus. Pour l'état réel des places, il faut téléphoner ou regarder en ligne.",
       note:"C'est la limite du papier, et elle est bonne à connaître avant de se déplacer pour rien."},

      {t:'labo', h:"Où chercher ?",
       p:"Choisissez une question et voyez où se trouve la réponse.",
       axes:[{id:'p', lbl:'Quelle question ?', opts:[
         ['a','Mon garçon a-t-il le bon âge ?'],
         ['b','Combien je vais payer ?'],
         ['c','Combien de temps ça dure ?'],
         ["d",'Que veut dire cette étoile ?'],
         ['e','Reste-t-il des places aujourd\'hui ?']]}],
       out:{
         a:{w:['la colonne de {gauche}'], say:"C'est le nom de l'activité et l'âge.", n:'à côté du nom de l\'activité'},
         b:{w:['le {premier} chiffre'], say:"Le premier, c'est le prix pour les résidents.", n:'si vous habitez la ville'},
         c:{w:['le {troisième} chiffre'], say:"Le troisième, c'est le nombre de semaines.", n:'la durée de la session'},
         d:{w:['la {légende}, en bas'], say:"En bas de la page, la légende l'explique.", n:'toujours en petits caractères'},
         e:{w:['{nulle part} — téléphonez'], say:"Alors inscris-toi cette semaine. Les places partent vite.", n:'le dépliant est imprimé longtemps d\'avance'},
       },
       note:"La dernière est la plus utile : savoir ce qu'un document <b>ne dit pas</b> évite un déplacement inutile."},

      {t:'ex', h:"Le vocabulaire du dépliant",
       p:"Écoutez chacun.",
       rows:[
         ["Regarde d'abord la colonne de gauche.","le tri par âge"],
         ["Le premier, c'est le prix pour les résidents.","le tarif"],
         ["Le troisième, c'est le nombre de semaines.","la durée"],
         ["Ça veut dire qu'il reste peu de places.","le symbole"],
         ["En bas de la page, la légende l'explique.","la légende"],
         ["C'est la moins chère de toutes.","la comparaison"],
       ]},

      {t:'piege', h:"Trois pièges à connaître",
       rows:[
         ["lire le dépliant du début à la fin","commencez par ce qui vous élimine",
          "Quatre pages, trente activités : lire en entier prend vingt minutes. Trier par âge et par jour en prend deux."],
         ["ignorer la légende","c'est là que se trouve l'information qui décide",
          "Les symboles ne veulent rien dire tout seuls. La légende est en bas, en petit — c'est précisément pour ça qu'il faut la chercher."],
         ["croire le dépliant sur les places","il a été imprimé des semaines avant",
          "Pour savoir s'il reste des places aujourd'hui, il n'y a qu'un moyen : téléphoner."],
       ]},

      {t:'check', h:"Est-ce que c'est clair maintenant ?",
       p:"Quatre questions rapides.",
       qs:[
         {q:"Le premier des trois chiffres est…", opts:["le tarif résident","le nombre de semaines"], ok:0,
          fb:"Tarif résident, tarif non-résident, nombre de semaines."},
         {q:"La légende se trouve…", opts:["en haut de la page","en bas de la page"], ok:1,
          fb:"Toujours en bas, en petits caractères."},
         {q:"Pour savoir s'il reste des places aujourd'hui…", opts:["on lit l'étoile","on téléphone"], ok:1,
          fb:"Le dépliant a été imprimé longtemps d'avance."},
         {q:"Par quoi commencer la lecture ?", opts:["par ce qui m'élimine","par la première page"], ok:0,
          fb:"L'âge, le jour, le tarif : on trie d'abord."},
       ]},
    ]
  },

  t3registre: {
    eye:'Mini-leçon', tit:"Deux façons de dire la même chose",
    blocs:[
      {t:'texte', h:"Kevin et Louise disent la même chose",
       p:"« Envoye, embarque ! » et « Entrez dans l'eau, s'il vous plaît. » Ce sont deux façons de dire exactement la même chose. Aucune des deux n'est fautive. Ce qui change, c'est la <b>situation</b> — et c'est ça qu'il faut apprendre.",
       note:"Le programme du cours demande de reconnaître la variété de langue et d'en tenir compte. Pas d'en préférer une."},

      {t:'ana', h:"Le registre standard : au comptoir",
       p:"On vouvoie, on parle plus lentement, les phrases sont complètes.",
       mots:[['Le pronom','{vous}'],['La phrase','complète',true],['Exemple','Entrez dans l\'eau, s\'il vous plaît.']],
       say:"Entrez dans l'eau, s'il vous plaît. On commence bientôt.",
       note:"C'est ce que vous entendrez au comptoir, à la clinique, à la banque, chez un employeur. C'est aussi la langue de l'écrit."},

      {t:'ana', h:"Le registre familier : au bord de la piscine",
       p:"On tutoie, les phrases sont courtes, certains mots sont propres au Québec.",
       mots:[['Le pronom','{tu}'],['La phrase','courte, directe',true],['Exemple','Envoye, embarque !']],
       say:"Envoye, embarque ! On commence dans deux minutes !",
       note:"« Envoye » veut dire « vas-y, dépêche-toi ». « Embarque » veut dire « entre, monte ». Deux mots très employés ici, et absents des manuels."},

      {t:'texte', h:"Comment savoir lequel employer",
       p:"Trois repères simples. <b>Un inconnu, un service, un employeur</b> › standard, et vous. <b>Un collègue, un ami, quelqu'un de votre âge dans une activité</b> › familier, et tu. <b>Dans le doute</b> › standard : personne n'a jamais été vexé d'être vouvoyé.",
       note:"Un moniteur peut vous tutoyer sans que vous ayez à le tutoyer en retour. Ce n'est pas un manque de respect de sa part."},

      {t:'ana', h:"Ce qu'il faut faire quand on ne comprend pas",
       p:"Demander de répéter autrement. C'est exactement ce que fait Rosa, et Kevin reformule immédiatement.",
       mots:[['La phrase','{Pardon ?} Je n\'ai pas compris.'],['Autre','Pouvez-vous répéter, s\'il vous plaît ?',true],['Résultat','on vous répond en standard']],
       say:"Pardon ? Je n'ai pas compris.",
       note:"Personne ne s'en formalise. Au contraire : la plupart des gens passent spontanément au registre standard quand on le leur demande."},

      {t:'labo', h:"Familier ou standard ?",
       p:"Choisissez une paire et écoutez les deux versions.",
       axes:[{id:'p', lbl:'Quelle paire ?', opts:[
         ['a',"entrer dans l'eau"],
         ['b','demander le prix'],
         ['c','demander s\'il reste des places'],
         ['d','demander un document'],
         ['e','rassurer quelqu\'un']]}],
       out:{
         a:{w:['{Envoye, embarque !}'], say:"Envoye, embarque ! On commence dans deux minutes !", n:'familier — au bord de la piscine'},
         b:{w:['{Ça coûte combien, ton affaire ?}'], say:"Ça coûte combien, ton affaire ?", n:'familier — entre gens qui se connaissent'},
         c:{w:['{Y reste-tu des places ?}'], say:"Y reste-tu des places ?", n:'familier — le « -tu » de la question au Québec'},
         d:{w:['{Veuillez apporter votre preuve.}'], say:"Veuillez apporter votre preuve de résidence au premier cours.", n:'standard écrit — un dépliant, un courriel'},
         e:{w:["{C'est correct, pas de trouble.}"], say:"C'est correct, pas de trouble.", n:'familier — très employé au Québec'},
       },
       note:"Le « -tu » de « y reste-tu des places ? » n'est pas le pronom <em>tu</em> : c'est une marque de question propre au français du Québec. Elle s'entend partout."},

      {t:'ex', h:"Les mêmes phrases, deux registres",
       p:"Écoutez chaque paire.",
       rows:[
         ["Envoye, embarque !","familier"],
         ["Entrez dans l'eau, s'il vous plaît.","standard"],
         ["Ça coûte combien, ton affaire ?","familier"],
         ["Quel est le tarif pour les résidents ?","standard"],
         ["C'est correct, pas de trouble.","familier"],
         ["Il n'y a aucun problème, madame.","standard"],
       ]},

      {t:'piege', h:"Trois malentendus fréquents",
       rows:[
         ["croire que le familier est incorrect","les deux registres sont du bon français",
          "Ce n'est pas une question de correction, mais de situation. Employer le standard entre amis sonne aussi étrange que l'inverse."],
         ["tutoyer parce qu'on a été tutoyé","un moniteur peut vous tutoyer sans réciprocité",
          "Dans le doute, continuez à vouvoyer. La personne vous dira elle-même « tu peux me tutoyer » si elle le souhaite."],
         ["faire semblant d'avoir compris","« Pardon ? Je n'ai pas compris. »",
          "Cinq mots, et l'autre reformule aussitôt en standard. C'est la phrase la plus utile de la leçon."],
       ]},

      {t:'check', h:"Est-ce que c'est clair maintenant ?",
       p:"Quatre questions rapides.",
       qs:[
         {q:"« Envoye, embarque ! » est…", opts:["une faute de français","du français familier"], ok:1,
          fb:"C'est du bon français, dans la bonne situation."},
         {q:"Au comptoir d'un centre municipal, on emploie…", opts:["le registre standard","le registre familier"], ok:0,
          fb:"Un service, un inconnu : on vouvoie."},
         {q:"Si un moniteur vous tutoie, vous devez…", opts:["le tutoyer aussi","continuer à vouvoyer si vous préférez"], ok:1,
          fb:"Le tutoiement n'est pas obligatoirement réciproque."},
         {q:"Quand vous ne comprenez pas, la meilleure phrase est…", opts:["« Pardon ? Je n'ai pas compris. »","hocher la tête"], ok:0,
          fb:"La personne reformulera aussitôt."},
       ]},
    ]
  },
};
