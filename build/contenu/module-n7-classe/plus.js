const PLUS = {

  prPhon: {
    eye:'Mini-leçon', tit:"Le petit « e » quand on parle à un groupe",
    blocs:[
      {t:'texte', h:"Un son qui a le droit de ne pas se dire",
       p:"Le français a un petit son qui tantôt se prononce, tantôt disparaît : le « e » de <i>demain</i>, de <i>petit</i>, de <i>regarder</i>. Les deux prononciations sont correctes. Ce n'est pas une question de soin ni de politesse : c'est la <b>place</b> du « e » dans le mot qui décide, et rien d'autre.",
       note:"Son nom savant est le <b>e caduc</b> — de « caduc », qui tombe. On l'écrit <b>[ə]</b>."},

      {t:'texte', h:"Pourquoi cette leçon arrive dans un module sur le travail d'équipe",
       p:"Parce que vous allez parler devant vingt personnes. Un exposé se dit plus lentement qu'une conversation, et l'auditoire qui vous écoute a besoin de syllabes entières. Or on ne rétablit pas tous les « e » pour autant : dire « ra-pi-de-ment » en quatre morceaux sonne appliqué et ralentit tout le propos. Savoir lesquels tiennent et lesquels tombent, c'est parler posément sans parler bizarrement.",
       note:"Et à l'écoute, c'est ce qui vous permet de reconnaître un mot que vous connaissez très bien mais qui vous arrive amputé d'une syllabe."},

      {t:'ana', h:"Il se dit — première syllabe après p, b, t, d, k, g",
       p:"Quand le mot commence par une consonne qui ferme complètement la bouche, le « e » de la première syllabe reste.",
       mots:[['On écrit','d{e}main · d{e}voir · p{e}tit · t{e}nez'],['On entend','le [ə] est là',true],['Le repère','la bouche se ferme, puis le « e » sort']],
       say:"demain, devoir, petit, tenez",
       note:"Ces consonnes ferment la bouche avant de la rouvrir : le « e » sort dans ce relâchement, et le supprimer demanderait un effort."},

      {t:'ana', h:"Il se dit — quand deux consonnes le précèdent",
       p:"S'il tombait, trois consonnes se suivraient et le mot deviendrait imprononçable.",
       mots:[['On écrit','just{e}ment · exact{e}ment · probabl{e}ment · simpl{e}ment'],['On entend','le [ə] est là',true],['La règle','deux consonnes devant, il tient']],
       say:"justement, exactement, probablement, simplement",
       note:"C'est ce cas qui explique pourquoi <i>justement</i> garde son « e » alors que <i>facilement</i> le perd : <i>st</i> contre <i>l</i>."},

      {t:'ana', h:"Il tombe — au milieu du mot, après une seule consonne",
       p:"Une seule consonne devant, et le « e » s'efface dans la conversation ordinaire comme dans un exposé.",
       mots:[['On écrit','facil{e}ment · ach{e}ter · app{e}ler · rel{e}ver'],['On entend','[fasilmɑ̃] · [aʃte] · [aple]',true],['La règle','une seule consonne devant, il tombe']],
       say:"facilement, acheter, appeler, relever",
       note:"Même chose dans <i>un médecin</i> et <i>une boulangerie</i>, que personne ne dit en quatre ou cinq syllabes."},

      {t:'ana', h:"Il tombe aussi — début de mot après r, l, m, n, s",
       p:"Au début d'un mot, si la première consonne n'est pas une de celles qui ferment la bouche, le « e » s'efface très souvent.",
       mots:[['On écrit','r{e}garder · r{e}prendre · r{e}levé'],['On entend','[ʁgaʁde] · [ʁpʁɑ̃dʁ]',true],['Le contraste','<i>demain</i> le garde, <i>regarder</i> le perd']],
       say:"regarder, reprendre, un relevé",
       note:"C'est le couple à retenir : <i>de</i> tient, <i>re</i> tombe. Deux syllabes qui se ressemblent à l'écrit et pas à l'oreille."},

      {t:'labo', h:"Écoutez la différence",
       p:"Choisissez un cas, puis un exemple.",
       axes:[
         {id:'c', lbl:'Quel cas ?', opts:[['a','la bouche se ferme'],['b','deux consonnes butent'],['c','une seule consonne'],['d','le r du début']]},
         {id:'n', lbl:'Quel exemple ?', opts:[['1','le premier'],['2','le second']]}],
       out:{
         a1:{w:["demain"], say:"demain", n:'« d » ferme la bouche : on entend « de-main »'},
         a2:{w:["petit"], say:"petit", n:'« p » ferme la bouche : on entend « pe-tit »'},
         b1:{w:["justement"], say:"justement", n:'« st » : deux consonnes, le « e » tient'},
         b2:{w:["probablement"], say:"probablement", n:'« bl » : deux consonnes, le « e » tient'},
         c1:{w:["facilement"], say:"facilement", n:'une seule consonne : « facil\'ment »'},
         c2:{w:["acheter"], say:"acheter", n:'on entend « ach\'ter », en deux syllabes'},
         d1:{w:["regarder"], say:"regarder", n:'« r » ne retient rien : « r\'garder »'},
         d2:{w:["reprendre"], say:"reprendre", n:'même chose : « r\'prendre »'},
       },
       note:"Écoutez deux fois, puis répétez à voix haute avant de passer au suivant."},

      {t:'ex', h:"Six mots que vous direz devant la classe",
       p:"À gauche, ce qui est écrit. À droite, ce qui sort de la bouche à vitesse normale.",
       rows:[
         ["demain","« de-main » — deux syllabes pleines"],
         ["justement","« jus-te-ment » — le « e » tient entre st et m"],
         ["exactement","« e-xac-te-ment » — même cas"],
         ["facilement","« facil'ment » — le « e » tombe"],
         ["acheter","« ach'ter » — deux syllabes, pas trois"],
         ["regarder","« r'garder » — le « e » du début tombe"],
       ]},

      {t:'piege', h:"Deux pièges et une bonne nouvelle",
       rows:[
         ["prononcer chaque « e » écrit","laisser tomber ceux qui tombent",
          "Devant un groupe, on ralentit le débit, on ne rajoute pas des syllabes. Dire « fa-ci-le-ment » ne rend pas le propos plus clair : ça le rend plus long et plus étrange."],
         ["croire qu'on a manqué un mot","reconnaître la forme courte",
          "Quand vous entendez [aʃte] et que vous cherchez « acheter », ce n'est pas votre vocabulaire qui manque, c'est l'entraînement à la forme amputée. Elle est la forme normale."],
         ["s'inquiéter de se tromper","aucune des deux formes ne trahit",
          "Garder un « e » qui aurait pu tomber ne crée aucun malentendu et ne choque personne. Cette leçon sert surtout à comprendre, un peu à produire, jamais à s'inquiéter."],
       ]},

      {t:'check', h:"Est-ce que c'est clair maintenant ?",
       p:"Quatre mots, une décision chacun.",
       qs:[
         {q:"Dans « demain », le « e » de la première syllabe…", opts:["se prononce","tombe"], ok:0,
          fb:"Première syllabe, et « d » ferme la bouche : il se maintient."},
         {q:"Dans « facilement », le « e » du milieu…", opts:["se prononce","tombe"], ok:1,
          fb:"Une seule consonne devant : on dit « facil'ment »."},
         {q:"Dans « exactement », deux consonnes précèdent le « e ». Il…", opts:["se maintient","tombe quand même"], ok:0,
          fb:"Sans lui, « ct » et « m » se suivraient : impossible à dire."},
         {q:"Dans « regarder », le « e » du début…", opts:["se prononce","tombe"], ok:1,
          fb:"« r » ne ferme pas la bouche : on dit « r'garder »."},
       ]},

      {t:'revoir', h:"À retenir",
       p:"Première syllabe après <b>p, b, t, d, k, g</b> : <b>on l'entend</b>. Deux consonnes devant : <b>on l'entend</b>. Une seule consonne au milieu du mot : <b>il tombe</b>. Début de mot après <b>r</b> : <b>il tombe</b>. Et devant un groupe, on ralentit le débit — on ne rajoute pas de syllabes."},
    ]
  },

  prRegistre: {
    eye:'Mini-leçon', tit:"Familier, standard, soutenu : choisir sans se tromper",
    blocs:[
      {t:'texte', h:"La bonne question n'est pas « est-ce du bon français ? »",
       p:"On croit souvent qu'il y a un français correct et un français fautif. C'est faux, et croire cela fait faire des erreurs dans les deux sens : on parle trop relâché devant un employeur, ou trop guindé avec des camarades qui vous trouvent alors distant. La vraie question est toujours : <b>est-ce le français de cette situation-là ?</b>",
       note:"Une phrase impeccable au mauvais endroit se remarque autant qu'une faute."},

      {t:'ana', h:"Le familier — entre camarades, à la pause",
       p:"Il rapproche. Négation sans <i>ne</i>, mots courts, questions avec <i>-tu</i>, phrases non terminées.",
       mots:[['On dit','« Ça marche pas, ton affaire. »'],['On dit aussi','« On se voit-tu samedi ? »'],['Ce qui le marque','le <i>ne</i> qui saute, le <i>-tu</i>, les mots comme <i>affaire</i>, <i>faque</i>',true]],
       say:"Ça marche pas, ton affaire. On se voit-tu samedi ?",
       note:"Il est parfaitement à sa place entre coéquipiers. Le danger n'est pas de l'employer : c'est de ne pas savoir qu'on l'emploie."},

      {t:'ana', h:"Le standard — en classe, au travail, avec un inconnu",
       p:"Phrases complètes, négation entière, vocabulaire précis, aucune abréviation. C'est la langue par défaut d'une équipe de travail, même quand on se tutoie.",
       mots:[['On dit','« Je ne suis pas certaine que ta méthode fonctionne. »'],['On dit aussi','« Est-ce que nous nous voyons samedi matin ? »'],['Ce qui le marque','le <i>ne</i> présent, les questions en <i>est-ce que</i>',true]],
       say:"Je ne suis pas certaine que ta méthode fonctionne.",
       note:"On tutoie ses coéquipiers et on parle standard : les deux vont très bien ensemble."},

      {t:'ana', h:"Le soutenu — devant la classe, devant un jury",
       p:"Vouvoiement de l'auditoire, tournures choisies, nombres dits en entier, aucune familiarité. Ce n'est pas de la décoration : c'est ce qui rend le propos audible du fond de la salle.",
       mots:[['On dit','« Vous constaterez que la différence est importante. »'],['On dit aussi','« Je vous remercie de votre attention. »'],['Ce qui le marque','le vouvoiement, les verbes précis, la phrase entière',true]],
       say:"Vous constaterez que la différence est importante.",
       note:"Attention à ne pas en mettre trop : un exposé entièrement soutenu devient froid. Le naturel reste la règle."},

      {t:'labo', h:"La même idée, trois façons",
       p:"Choisissez une idée, puis une variété.",
       axes:[
         {id:'i', lbl:'Quelle idée ?', opts:[['a','je ne suis pas d\'accord'],['b','je propose une date'],['c','je ne comprends pas']]},
         {id:'v', lbl:'Quelle variété ?', opts:[['1','familier'],['2','standard'],['3','soutenu']]}],
       out:{
         a1:{w:["Ben non, ça marche pas."], say:"Ben non, ça marche pas.", n:'entre camarades, à la pause'},
         a2:{w:["Je ne suis pas d'accord avec cette méthode."], say:"Je ne suis pas d'accord avec cette méthode.", n:'en équipe, en classe'},
         a3:{w:["Permettez-moi d'exprimer une réserve."], say:"Permettez-moi d'exprimer une réserve.", n:'devant un groupe ou un jury'},
         b1:{w:["On se voit-tu samedi ?"], say:"On se voit-tu samedi ?", n:'question familière, très québécoise'},
         b2:{w:["Est-ce qu'on se voit samedi matin ?"], say:"Est-ce qu'on se voit samedi matin ?", n:'la forme la plus utile en équipe'},
         b3:{w:["Vous conviendrait-il de nous voir samedi ?"], say:"Vous conviendrait-il de nous voir samedi ?", n:'à réserver à l\'écrit ou à un inconnu'},
         c1:{w:["Là, j'ai rien compris."], say:"Là, j'ai rien compris.", n:'le <i>ne</i> saute : familier'},
         c2:{w:["Je n'ai pas bien compris, peux-tu reprendre ?"], say:"Je n'ai pas bien compris, peux-tu reprendre ?", n:'standard, et parfaitement poli'},
         c3:{w:["Pourriez-vous préciser ce dernier point ?"], say:"Pourriez-vous préciser ce dernier point ?", n:'devant la classe ou une personne invitée'},
       },
       note:"Aucune des trois n'est meilleure. Chacune a son endroit, et se tromper d'endroit se remarque."},

      {t:'ex', h:"Six couples à reconnaître",
       p:"À gauche le familier, à droite le standard qui dit la même chose.",
       rows:[
         ["« Y'a rien là. »","« Ce n'est pas un problème. »"],
         ["« Faque là, on fait quoi ? »","« Quelle est la prochaine étape ? »"],
         ["« Wo, minute ! »","« Un instant, s'il te plaît. »"],
         ["« C'est correct pour moi. »","« Cela me convient. »"],
         ["« Il est ben fin. »","« Il est très aimable. »"],
         ["« On lâche pas. »","« Nous poursuivons. »"],
       ]},

      {t:'piege', h:"Trois pièges du niveau intermédiaire",
       rows:[
         ["mélanger deux variétés dans la même phrase","tenir la même du début à la fin",
          "« Je vous remercie, faque on se rappelle. » Le mélange s'entend beaucoup plus qu'une phrase entièrement familière. Choisissez, et tenez."],
         ["croire que le vouvoiement est toujours plus poli","adapter au lien, pas au niveau de langue",
          "Vouvoyer un coéquipier avec qui on travaille depuis trois semaines crée une distance que personne n'a demandée. En équipe, le tutoiement standard est la bonne combinaison."],
         ["prendre le familier pour de la mauvaise grammaire","y voir une autre variété, avec ses règles",
          "« On se voit-tu ? » n'est pas une faute : c'est une question familière du français québécois, parfaitement régulière. Elle est simplement située."],
       ]},

      {t:'check', h:"Est-ce que c'est clair maintenant ?",
       p:"Quatre situations, une décision chacune.",
       qs:[
         {q:"Vous parlez à un coéquipier pendant la rencontre de travail.", opts:["familier","standard"], ok:1,
          fb:"Standard, et tutoiement : c'est la combinaison du travail d'équipe."},
         {q:"Vous présentez votre exposé devant toute la classe.", opts:["standard soigné, vouvoiement","familier, tutoiement"], ok:0,
          fb:"On vouvoie un auditoire, même composé de camarades qu'on tutoie tous les jours."},
         {q:"« Je ne suis pas certaine que ce chiffre soit à jour. »", opts:["familier","standard"], ok:1,
          fb:"Négation complète, subjonctif après une expression de doute : standard."},
         {q:"« Faque, on garde-tu la phrase ou pas ? »", opts:["familier","soutenu"], ok:0,
          fb:"« Faque » et la question en <i>-tu</i> : familier, et très bien à la pause."},
       ]},

      {t:'revoir', h:"À retenir",
       p:"Trois variétés, une question : <b>où suis-je et à qui je parle ?</b> Avec des camarades, familier. En équipe et en classe, <b>standard</b> — c'est celle qui sert le plus. Devant un groupe ou un inconnu, standard soigné avec vouvoiement. Et jamais deux variétés dans la même phrase."},
    ]
  },

  t1conn: {
    eye:'Mini-leçon', tit:"Les panneaux de route d'un exposé",
    blocs:[
      {t:'texte', h:"Pourquoi un exposé s'écoute autrement qu'une conversation",
       p:"Dans une conversation, vous répondez à ce qui vient d'être dit : vous n'avez rien à anticiper. Devant une personne qui expose, c'est l'inverse — elle a préparé un chemin, elle vous l'annonce, et tout ce qui suit se range dans les cases qu'elle a ouvertes. Écouter un exposé, c'est d'abord attraper l'annonce du plan, puis suivre les panneaux.",
       note:"Perrine l'a fait dès sa deuxième phrase : « je vous dis où je m'en vais ». Trois cases, avant même de commencer."},

      {t:'ana', h:"Les connecteurs qui annoncent le plan",
       p:"Ils arrivent au tout début et donnent la carte entière. Notez-les : ils vous donnent la structure de vos propres notes.",
       mots:[['On entend','« Avant de commencer, je vous dis où je m\'en vais. »'],['Ou encore','« Je vais parler d\'abord de… ensuite de… et enfin de… »'],['Ce que ça vous donne','trois tiroirs à ouvrir dans votre cahier',true]],
       say:"Je vais parler d'abord de ce qu'est un îlot de chaleur, ensuite de ce que fait un arbre, et enfin de ce qui se passe chez vous.",
       note:"Si personne ne vous annonce le plan, demandez-le : « Comment allez-vous procéder ? » est une question tout à fait recevable."},

      {t:'ana', h:"Les connecteurs qui marquent les étapes",
       p:"Ils disent où vous en êtes et combien il en reste. Ce sont les plus faciles à entendre, et les plus utiles à réemployer dans votre propre exposé.",
       mots:[['On entend','premier point · deuxième point · pour finir'],['Ou encore','d\'abord · ensuite · puis · enfin'],['Ce que ça vous donne','le droit de tourner la page de vos notes',true]],
       say:"Premier point. Deuxième point. Et pour finir.",
       note:"Dans un exposé de quatre minutes, trois étapes suffisent. Au-delà, l'auditoire perd le compte."},

      {t:'ana', h:"Les connecteurs qui changent de sujet",
       p:"Ils préviennent que ce qui suit ne prolonge pas ce qui précède : on quitte un point pour un autre. Ce sont eux qu'on manque le plus souvent, et les manquer fait croire à une contradiction.",
       mots:[['On entend','quant à · en ce qui concerne · à propos de'],['Exemple','« Quant au secteur de votre centre, ce serait sous les dix pour cent. »'],['Ce que ça vous donne','un nouveau paragraphe dans vos notes',true]],
       say:"Quant au secteur de votre centre, ce serait plutôt sous les dix pour cent.",
       note:"<b>Quant à</b> + le = <b>quant au</b>, + les = <b>quant aux</b>. Et il n'a rien à voir avec <i>quand</i>, malgré la prononciation."},

      {t:'ana', h:"Les connecteurs qui reformulent et qui concluent",
       p:"Ils annoncent que rien de neuf ne vient : ce qui suit redit, en plus court, ce qui a déjà été dit. Ce sont les phrases à noter en priorité — quelqu'un vient de résumer à votre place.",
       mots:[['Reformuler','autrement dit · c\'est-à-dire · en d\'autres mots'],['Conclure','en somme · par conséquent · donc'],['Ce que ça vous donne','la phrase du résumé, toute prête',true]],
       say:"Autrement dit, un arbre ne fait pas seulement de l'ombre. En somme, c'est la canopée qu'il faut mesurer.",
       note:"<b>Autrement dit</b> vaut pour une phrase ; <b>en somme</b> rassemble un paragraphe entier et ne s'emploie qu'une fois."},

      {t:'labo', h:"Quel connecteur pour quel moment ?",
       p:"Choisissez un moment de l'exposé, puis une formule.",
       axes:[
         {id:'m', lbl:'Quel moment ?', opts:[['a','j\'annonce mon plan'],['b','je change de point'],['c','je reformule'],['d','je conclus']]},
         {id:'f', lbl:'Quelle formule ?', opts:[['1','la courante'],['2','la plus soignée']]}],
       out:{
         a1:{w:["Je vais parler d'abord de…"], say:"Je vais parler d'abord de la cause, ensuite des effets.", n:'simple et parfaitement suffisante'},
         a2:{w:["Mon exposé comprendra trois parties."], say:"Mon exposé comprendra trois parties.", n:'plus formelle, très claire pour l\'auditoire'},
         b1:{w:["Maintenant, parlons de…"], say:"Maintenant, parlons de notre quartier.", n:'le passage le plus courant à l\'oral'},
         b2:{w:["En ce qui concerne notre quartier…"], say:"En ce qui concerne notre quartier…", n:'annonce le changement sans le dire lourdement'},
         c1:{w:["Autrement dit…"], say:"Autrement dit, l'arbre refroidit l'air autour de lui.", n:'pour redire une phrase en plus simple'},
         c2:{w:["C'est-à-dire que…"], say:"C'est-à-dire que l'arbre refroidit l'air autour de lui.", n:'même usage, un ton au-dessus'},
         d1:{w:["Donc, ce qu'il faut retenir…"], say:"Donc, ce qu'il faut retenir, c'est la surface des cimes.", n:'la conclusion ordinaire d\'un exposé de classe'},
         d2:{w:["En somme…"], say:"En somme, c'est la canopée qu'il faut mesurer.", n:'rassemble tout ; une seule fois, à la toute fin'},
       },
       note:"Réemployez-les dans votre exposé de « Je me lance » : ce sont eux qui feront la différence entre une liste et un propos suivi."},

      {t:'ex', h:"Six connecteurs et ce qu'ils promettent",
       p:"À gauche ce qu'on entend, à droite ce que l'auditeur doit en faire.",
       rows:[
         ["« Avant de commencer… »","ouvrez trois tiroirs, il annonce son plan"],
         ["« Deuxième point… »","tournez la page, une étape se termine"],
         ["« Quant à… »","nouveau sujet, ne le rattachez pas au précédent"],
         ["« Autrement dit… »","rien de neuf : voici la version courte"],
         ["« Par conséquent… »","ce qui suit découle de ce qui précède"],
         ["« En somme… »","c'est la fin : tout tient dans la phrase qui vient"],
       ]},

      {t:'piege', h:"Trois pièges à l'écoute comme à la production",
       rows:[
         ["confondre « quant à » et « quand »","écouter ce qui suit",
          "« Quant à » est suivi d'un nom (quant au secteur, quant aux données) ; « quand » est suivi d'un verbe (quand nous irons). L'oreille ne les sépare pas, la suite de la phrase les sépare."],
         ["mettre un connecteur à chaque phrase","un par idée, là où on peut se perdre",
          "Un texte où chaque phrase commence par un connecteur devient illisible et un exposé qui en abuse devient mécanique. Ils servent aux virages, pas aux lignes droites."],
         ["noter la phrase entière","noter le connecteur et trois mots",
          "Pendant qu'on écrit une phrase complète, la phrase suivante passe. Un tiret, le connecteur, trois mots-clés : c'est ce qu'on relit le soir avec profit."],
       ]},

      {t:'check', h:"Est-ce que c'est clair maintenant ?",
       p:"Quatre phrases entendues : que faut-il en conclure ?",
       qs:[
         {q:"« En ce qui concerne l'arrosage… »", opts:["on change de point","on conclut"], ok:0,
          fb:"C'est un connecteur de changement de sujet : nouveau paragraphe dans vos notes."},
         {q:"« Autrement dit, la canopée compte plus que le nombre d'arbres. »", opts:["une idée nouvelle arrive","la même idée, en plus court"], ok:1,
          fb:"Rien de neuf : c'est la version résumée, celle qu'on note."},
         {q:"« Par conséquent, le secteur chauffe davantage. »", opts:["une conséquence de ce qui précède","une opinion personnelle"], ok:0,
          fb:"Il annonce que ce qui suit découle de ce qui vient d'être dit."},
         {q:"« Deuxième point : ce que fait un arbre. »", opts:["une étape du plan annoncé","la conclusion"], ok:0,
          fb:"Une étape, et il en reste au moins une autre derrière."},
       ]},

      {t:'revoir', h:"À retenir",
       p:"Quatre familles : <b>annoncer le plan</b> (avant de commencer, je vais parler d'abord de…), <b>marquer les étapes</b> (premier point, ensuite, enfin), <b>changer de sujet</b> (quant à, en ce qui concerne), <b>reformuler et conclure</b> (autrement dit, en somme, par conséquent). À l'écoute, ce sont des panneaux ; dans votre exposé, ce sont eux qui tiennent le propos debout."},
    ]
  },

  t1cond: {
    eye:'Mini-leçon', tit:"Le conditionnel du chiffre qu'on n'a pas vérifié",
    blocs:[
      {t:'texte', h:"Une syllabe qui change tout",
       p:"« L'écart <b>est</b> de dix degrés » et « l'écart <b>serait</b> de dix degrés » ne disent pas la même chose. La première affirme et vous engage : si le chiffre est faux, vous avez dit une chose fausse. La seconde rapporte : elle dit « voici ce qu'on m'a donné, je ne l'ai pas vérifié moi-même ». Dans un travail de recherche, cette syllabe-là vous protège.",
       note:"Perrine l'emploie deux fois dans la même soirée, et elle explique elle-même pourquoi : la mesure vient d'une seule journée."},

      {t:'ana', h:"Comment il se fabrique",
       p:"Le radical du futur, les terminaisons de l'imparfait. Il y a toujours un <b>r</b> juste avant la terminaison.",
       mots:[['Régulier','je parler<b>ais</b> · tu parler<b>ais</b> · il parler<b>ait</b>'],['Suite','nous parler<b>ions</b> · vous parler<b>iez</b> · elles parler<b>aient</b>'],['Le repère','le <b>r</b> avant la terminaison, toujours',true]],
       say:"je parlerais, tu parlerais, il parlerait, nous parlerions, vous parleriez, elles parleraient",
       note:"Les terminaisons sont exactement celles de l'imparfait. Le radical, exactement celui du futur. Rien à apprendre de neuf : deux choses connues, assemblées."},

      {t:'ana', h:"Les huit radicaux irréguliers à connaître",
       p:"Ce sont ceux du futur, donc vous les avez déjà rencontrés. Huit verbes couvrent presque tout ce que vous direz.",
       mots:[['Les plus fréquents','être → je ser<b>ais</b> · avoir → j\'aur<b>ais</b> · aller → j\'ir<b>ais</b> · faire → je fer<b>ais</b>'],['Les autres','pouvoir → je pourr<b>ais</b> · devoir → je devr<b>ais</b> · venir → je viendr<b>ais</b> · falloir → il faudr<b>ait</b>'],['Le repère','deux r dans pourrait, un seul dans serait',true]],
       say:"je serais, j'aurais, j'irais, je ferais, je pourrais, je devrais, je viendrais, il faudrait",
       note:"<i>Falloir</i> n'existe qu'à la troisième personne du singulier : <b>il faudrait</b>, et rien d'autre."},

      {t:'ana', h:"Le premier emploi : l'information non confirmée",
       p:"C'est celui du défi 1. La personne qui parle vous prévient qu'elle rapporte sans garantir.",
       mots:[['Dans une rencontre','« L\'écart serait d\'une dizaine de degrés. »'],['Aux nouvelles','« Il y aurait une dizaine de blessés. »'],['Dans votre exposé','« La canopée serait de dix-sept pour cent, selon la ville. »',true]],
       say:"L'écart serait d'une dizaine de degrés. La canopée serait de dix-sept pour cent, selon la ville.",
       note:"Ajoutez toujours la source après : <i>selon la ville</i>, <i>d'après la fiche</i>. Le conditionnel dit que ce n'est pas de vous ; la source dit de qui c'est."},

      {t:'ana', h:"Le deuxième emploi : la politesse",
       p:"Même forme, usage tout différent. C'est celui qui vous servira à animer, au défi 3 et dans « Je me lance ».",
       mots:[['Demander','« Pourrais-tu reprendre plus lentement ? »'],['Proposer','« On pourrait noter l\'ombre à chaque coin. »'],['Souhaiter','« Je voudrais revenir sur la question de Miguel. »',true]],
       say:"Pourrais-tu reprendre plus lentement ? On pourrait noter l'ombre à chaque coin.",
       note:"Une proposition au conditionnel laisse à l'autre la possibilité de refuser sans se fâcher. C'est l'outil de base de l'animation."},

      {t:'labo', h:"Affirmer, ou rapporter ?",
       p:"Choisissez une phrase, puis le temps du verbe.",
       axes:[
         {id:'p', lbl:'Quelle phrase ?', opts:[['a','la canopée'],['b','les jeunes arbres'],['c','le programme'],['d','la méthode']]},
         {id:'t', lbl:'Quel temps ?', opts:[['1','présent : j\'affirme'],['2','conditionnel : je rapporte']]}],
       out:{
         a1:{w:["La canopée est de dix-sept pour cent."], say:"La canopée est de dix-sept pour cent.", n:'vous en répondez : il vous faut la source sous la main'},
         a2:{w:["La canopée serait de dix-sept pour cent."], say:"La canopée serait de dix-sept pour cent.", n:'vous rapportez, et vous restez exact même si le chiffre est faux'},
         b1:{w:["Les jeunes arbres ont besoin d'eau trois ans."], say:"Les jeunes arbres ont besoin d'eau pendant trois ans.", n:'un fait général : le présent convient très bien'},
         b2:{w:["Les jeunes arbres auraient besoin d'eau trois ans."], say:"Les jeunes arbres auraient besoin d'eau pendant trois ans.", n:'inutilement prudent : le fait est établi partout'},
         c1:{w:["Le programme vise quatre cents arbres par année."], say:"Le programme vise quatre cents arbres par année.", n:'écrit dans la fiche : on peut l\'affirmer en citant'},
         c2:{w:["Le programme viserait quatre cents arbres par année."], say:"Le programme viserait quatre cents arbres par année.", n:'utile si l\'on n\'a pas retrouvé la fiche'},
         d1:{w:["Notre méthode tient debout."], say:"Notre méthode tient debout.", n:'affirmation : à ne dire qu\'après vérification'},
         d2:{w:["Notre méthode tiendrait debout, selon Perrine."], say:"Notre méthode tiendrait debout, selon Perrine.", n:'honnête tant que la réponse n\'est pas arrivée'},
       },
       note:"Trop de conditionnel affaiblit un exposé : réservez-le à ce que vous n'avez pas vérifié vous-même."},

      {t:'ex', h:"Six phrases pour votre exposé",
       p:"À gauche ce que vous diriez sans y penser, à droite ce qu'il vaut mieux dire.",
       rows:[
         ["« Il y a dix degrés d'écart. »","« L'écart serait d'une dizaine de degrés, selon l'organisme. »"],
         ["« La ville plante 400 arbres par année. »","« La ville viserait 400 arbres par année, d'après sa fiche. »"],
         ["« Un arbre sur cinq meurt. »","« Un arbre sur cinq ne survivrait pas, selon la ville. »"],
         ["« Peux-tu répéter ? »","« Pourrais-tu répéter, s'il te plaît ? »"],
         ["« On note l'ombre. »","« On pourrait noter l'ombre à chaque coin. »"],
         ["« Je veux revenir là-dessus. »","« Je voudrais revenir là-dessus un instant. »"],
       ]},

      {t:'piege', h:"Trois pièges classiques",
       rows:[
         ["« je serai » pour « je serais »","écouter le r et compter les lettres",
          "Le futur <i>je serai</i> affirme ; le conditionnel <i>je serais</i> n'affirme pas. Un <b>s</b> à la fin, et le sens de la phrase change entièrement."],
         ["confondre avec l'imparfait","chercher le r avant la terminaison",
          "<i>il parlait</i> (imparfait, pas de r) et <i>il parlerait</i> (conditionnel, un r). Les terminaisons sont les mêmes ; c'est le radical qui les distingue."],
         ["tout mettre au conditionnel par prudence","le réserver au non vérifié",
          "Un exposé entièrement au conditionnel ne rassure personne : il donne l'impression que rien n'a été vérifié. Affirmez ce que vous avez vérifié."],
       ]},

      {t:'check', h:"Est-ce que c'est clair maintenant ?",
       p:"Quatre décisions.",
       qs:[
         {q:"Un chiffre que vous avez lu dans une fiche datée et que vous citez avec sa source.", opts:["présent","conditionnel"], ok:0,
          fb:"Vous avez la source : affirmez, et nommez-la."},
         {q:"Un chiffre qu'une personne vous a donné de mémoire, sans document.", opts:["présent","conditionnel"], ok:1,
          fb:"Conditionnel, et dites de qui il vient."},
         {q:"« Il faudrait vérifier auprès de l'organisme. » Cet emploi est…", opts:["une information non confirmée","une proposition polie"], ok:1,
          fb:"C'est le second emploi : proposer sans imposer."},
         {q:"Le radical du conditionnel est celui…", opts:["du futur","de l'imparfait"], ok:0,
          fb:"Radical du futur, terminaisons de l'imparfait. D'où le r toujours présent."},
       ]},

      {t:'revoir', h:"À retenir",
       p:"<b>Radical du futur + terminaisons de l'imparfait</b>, et un <b>r</b> avant la terminaison. Deux emplois : <b>rapporter sans garantir</b> (l'écart serait de dix degrés) et <b>demander poliment</b> (pourrais-tu répéter ?). Dans un travail, le conditionnel accompagne toujours une source nommée."},
    ]
  },

  t1fait: {
    eye:'Mini-leçon', tit:"Un fait, une estimation : reconnaître lequel on entend",
    blocs:[
      {t:'texte', h:"Ce que vous notez décide de ce que vous pourrez écrire",
       p:"Pendant une rencontre, tout arrive au même rythme et sur le même ton. Trois heures plus tard, devant vos notes, vous ne savez plus lequel de ces chiffres était mesuré, lequel était approché et lequel était l'avis de la personne. Le seul moment où la distinction est facile, c'est <b>pendant</b> qu'elle parle : elle la marque, à condition qu'on l'écoute.",
       note:"Une note utile porte donc deux choses : le renseignement, et d'où il vient."},

      {t:'ana', h:"Le fait — ce qui est établi et vérifiable",
       p:"Il se dit au présent, sans prudence, et se retrouve ailleurs. Il tient devant n'importe quelle question.",
       mots:[['On entend','« Un arbre rejette de l\'eau par ses feuilles. »'],['Ou encore','« La canopée se mesure en pourcentage du territoire. »'],['Le signe','présent de l\'indicatif, aucune atténuation',true]],
       say:"Un arbre rejette de l'eau par ses feuilles, sous forme de vapeur.",
       note:"Un fait ne devient pas votre propriété pour autant : vous le citerez avec sa source, comme le reste."},

      {t:'ana', h:"L'estimation — un chiffre approché, et qui se signale",
       p:"Elle est calculée à partir de ce qu'on sait, mais elle n'a pas été mesurée dans ce cas-ci. Elle porte presque toujours un marqueur.",
       mots:[['Les marqueurs','environ · de l\'ordre de · une dizaine · on estime que'],['Le temps','le conditionnel : « ce serait », « il y aurait »'],['On entend','« L\'écart serait d\'une dizaine de degrés. »',true]],
       say:"L'écart serait d'une dizaine de degrés entre les deux secteurs.",
       note:"Une estimation n'est pas une faiblesse : c'est souvent le seul chiffre disponible. Ce qui serait fautif, c'est de la citer comme une mesure."},

      {t:'ana', h:"L'opinion — un jugement, et il a sa place",
       p:"Elle dit ce que la personne pense, pas ce qui est. On la reconnaît à un verbe de jugement ou à un mot qui évalue.",
       mots:[['Les verbes','je pense que · je trouve que · à mon avis · selon moi'],['Les mots qui évaluent','intéressant · préoccupant · insuffisant · ce n\'est pas neutre'],['On entend','« Cet angle n\'est presque jamais traité, et il est là. »',true]],
       say:"À mon avis, cet angle n'est presque jamais traité.",
       note:"Une opinion de personne-ressource vaut beaucoup — elle vient de l'expérience. Mais elle se cite comme une opinion : <i>selon Perrine Auclair, …</i>"},

      {t:'labo', h:"La même donnée, trois statuts",
       p:"Choisissez un sujet, puis un statut.",
       axes:[
         {id:'s', lbl:'Quel sujet ?', opts:[['a','la chaleur'],['b','les arbres perdus'],['c','le quartier']]},
         {id:'q', lbl:'Quel statut ?', opts:[['1','un fait'],['2','une estimation'],['3','une opinion']]}],
       out:{
         a1:{w:["L'asphalte chauffe plus qu'une pelouse."], say:"L'asphalte chauffe plus qu'une pelouse.", n:'établi, mesuré partout : un fait'},
         a2:{w:["L'écart serait d'une dizaine de degrés."], say:"L'écart serait d'une dizaine de degrés.", n:'conditionnel et « une dizaine » : une estimation'},
         a3:{w:["C'est le vrai problème du quartier."], say:"C'est le vrai problème du quartier.", n:'un jugement : une opinion, à citer comme telle'},
         b1:{w:["Un jeune arbre a besoin d'eau trois étés."], say:"Un jeune arbre a besoin d'eau pendant trois étés.", n:'établi : un fait'},
         b2:{w:["On estime la perte à un sur cinq."], say:"On estime la perte à un arbre sur cinq.", n:'« on estime » : une estimation'},
         b3:{w:["C'est un gaspillage évitable."], say:"C'est un gaspillage évitable.", n:'« gaspillage », « évitable » : une opinion'},
         c1:{w:["La surface minéralisée dépasse les trois quarts."], say:"La surface minéralisée dépasse les trois quarts du sol.", n:'chiffré et publié : un fait'},
         c2:{w:["La canopée serait sous les dix pour cent."], say:"La canopée serait sous les dix pour cent.", n:'conditionnel : une estimation'},
         c3:{w:["Ce secteur devrait être une priorité."], say:"Ce secteur devrait être une priorité.", n:'ce que la personne pense : une opinion'},
       },
       note:"Dans vos notes, un signe suffit : un tiret pour le fait, un point d'interrogation pour l'estimation, des guillemets pour l'opinion."},

      {t:'ex', h:"Six phrases, six statuts",
       p:"À gauche la phrase entendue, à droite ce qu'on écrit dans la marge.",
       rows:[
         ["« La canopée se mesure en pourcentage. »","fait — utilisable tel quel"],
         ["« Ce serait sous les dix pour cent. »","estimation — noter le conditionnel avec"],
         ["« Cet angle n'est presque jamais traité. »","opinion — citer avec son auteur"],
         ["« La mesure a été prise une seule journée. »","fait — et c'est lui qui explique l'estimation"],
         ["« On estime la perte à un sur cinq. »","estimation — « on estime » est le signe"],
         ["« Le plus difficile, c'est d'arroser. »","opinion — mais d'une personne du métier"],
       ]},

      {t:'piege', h:"Trois pièges de la prise de notes",
       rows:[
         ["noter le chiffre sans son statut","noter le chiffre et le mot qui l'accompagne",
          "« 17 % » ne vaut rien dans trois jours. « 17 % (ville, relevé l'an dernier) » se cite. « 17 % ? (elle dit serait) » se cite autrement."],
         ["prendre l'assurance pour de la certitude","écouter les marqueurs, pas le ton",
          "Une personne peut dire une estimation d'une voix très ferme. Ce n'est pas le ton qui vous renseigne, ce sont les mots : <i>environ</i>, <i>on estime</i>, le conditionnel."],
         ["jeter les opinions","les garder, en les attribuant",
          "L'opinion d'une personne qui fait le métier depuis vingt ans est souvent la partie la plus utile de la rencontre. Elle se garde — avec son nom devant."],
       ]},

      {t:'check', h:"Est-ce que c'est clair maintenant ?",
       p:"Quatre phrases : fait, estimation ou opinion ?",
       qs:[
         {q:"« Les surfaces sombres absorbent le rayonnement du soleil. »", opts:["un fait","une estimation"], ok:0,
          fb:"Établi, mesurable, sans marqueur de prudence : un fait."},
         {q:"« Il y aurait moins de dix pour cent de couverture. »", opts:["un fait","une estimation"], ok:1,
          fb:"Conditionnel : la personne rapporte sans garantir."},
         {q:"« À mon avis, ce secteur devrait être une priorité. »", opts:["une opinion","un fait"], ok:0,
          fb:"« À mon avis » et « devrait » : un jugement, à citer avec son auteur."},
         {q:"Dans vos notes, un chiffre s'écrit toujours avec…", opts:["sa source et son statut","le nom de qui parlait"], ok:0,
          fb:"D'où il vient, et s'il est mesuré ou approché. Sans ça, il est inutilisable."},
       ]},

      {t:'revoir', h:"À retenir",
       p:"<b>Un fait</b> se dit au présent, sans prudence, et se vérifie ailleurs. <b>Une estimation</b> porte un marqueur (environ, on estime, une dizaine) ou un conditionnel. <b>Une opinion</b> porte un verbe de jugement ou un mot qui évalue. Les trois se notent — jamais de la même façon."},
    ]
  },

  t2nom: {
    eye:'Mini-leçon', tit:"Remplacer une phrase par un nom",
    blocs:[
      {t:'texte', h:"L'outil numéro un du résumé",
       p:"Un résumé doit faire deux choses en même temps : dire beaucoup en peu de mots, et le dire <b>avec ses mots à soi</b>. La nominalisation fait les deux d'un seul geste. « La ville a planté quatre cents arbres » devient « la plantation de quatre cents arbres » : sept mots gagnés, et la phrase ne ressemble plus à celle du texte de départ.",
       note:"Le mot savant est <b>nominalisation</b>. Vous le rencontrerez dans les consignes de travail ; il ne désigne rien d'autre que ce geste-là."},

      {t:'ana', h:"Les noms en -tion et en -ation",
       p:"La famille la plus nombreuse. Elle vient surtout des verbes en <i>-er</i>.",
       mots:[['Le verbe','planter · observer · répartir · absorber'],['Le nom','la plantation · l\'observation · la répartition · l\'absorption'],['Le genre','tous féminins, sans exception',true]],
       say:"la plantation, l'observation, la répartition, l'absorption",
       note:"Attention à <i>absorber</i>, qui donne <b>absorption</b> et non « absorbation » : quelques verbes changent leur radical."},

      {t:'ana', h:"Les noms en -ment et en -age",
       p:"Deux familles masculines. Elles se disputent parfois le même verbe, avec une nuance.",
       mots:[['En -ment','remplacer → le remplacement · déplacer → le déplacement'],['En -age','arroser → l\'arrosage · abattre → l\'abattage · compter → le comptage'],['La nuance','-age insiste sur l\'opération, -ment sur le résultat',true]],
       say:"le remplacement, le déplacement, l'arrosage, l'abattage",
       note:"Ne cherchez pas la règle absolue : elle n'existe pas. Ces noms s'apprennent avec leur verbe, deux par deux."},

      {t:'ana', h:"Les noms sans suffixe",
       p:"Les plus courts, et les plus utiles dans un résumé. Le nom ne ressemble presque plus au verbe.",
       mots:[['Le verbe','perdre · choisir · mesurer · gagner'],['Le nom','la perte · le choix · la mesure · le gain'],['Le repère','aucun suffixe : c\'est le radical, parfois modifié',true]],
       say:"la perte, le choix, la mesure, le gain",
       note:"Ce sont ceux qui font le plus gagner de place : <i>ce qu'ils ont choisi de noter</i> devient <i>leur choix</i>."},

      {t:'labo', h:"La phrase, puis le nom",
       p:"Choisissez une action, puis la forme.",
       axes:[
         {id:'a', lbl:'Quelle action ?', opts:[['a','planter'],['b','arroser'],['c','perdre'],['d','répartir']]},
         {id:'f', lbl:'Quelle forme ?', opts:[['1','la phrase'],['2','le nom']]}],
       out:{
         a1:{w:["La ville a planté quatre cents arbres."], say:"La ville a planté quatre cents arbres.", n:'la phrase dit qui, quand, quoi'},
         a2:{w:["la plantation de quatre cents arbres"], say:"la plantation de quatre cents arbres", n:'sept mots gagnés — mais on ne sait plus qui'},
         b1:{w:["Les résidents arrosent les jeunes arbres."], say:"Les résidents arrosent les jeunes arbres.", n:'sujet et verbe, tout est là'},
         b2:{w:["l'arrosage des jeunes arbres"], say:"l'arrosage des jeunes arbres", n:'très court ; ajoutez « par les résidents » si ça compte'},
         c1:{w:["Un arbre sur cinq ne survit pas."], say:"Un arbre sur cinq ne survit pas.", n:'la phrase du texte de départ'},
         c2:{w:["la perte d'un arbre sur cinq"], say:"la perte d'un arbre sur cinq", n:'un nom sans suffixe : le plus économique'},
         d1:{w:["On a réparti les rôles au début."], say:"On a réparti les rôles au début.", n:'phrase complète, sujet vague'},
         d2:{w:["la répartition des rôles"], say:"la répartition des rôles", n:'la formule qu\'on lit dans toutes les consignes'},
       },
       note:"Écoutez les deux : la version nominale est plus dense, et c'est exactement ce qu'un résumé demande."},

      {t:'ex', h:"Huit verbes et leur nom",
       p:"Les huit dont vous aurez besoin dans ce module.",
       rows:[
         ["planter","la plantation"],
         ["arroser","l'arrosage"],
         ["abattre","l'abattage"],
         ["mesurer","la mesure"],
         ["perdre","la perte"],
         ["choisir","le choix"],
         ["répartir","la répartition"],
         ["absorber","l'absorption"],
       ]},

      {t:'piege', h:"Trois pièges, dont un grave",
       rows:[
         ["effacer qui a fait l'action","le remettre avec « par » ou « de »",
          "« la plantation de quatre cents arbres » ne dit pas qui les a plantés. Dans un résumé, c'est souvent une information qui compte : <i>la plantation, par la ville, l'an dernier</i>."],
         ["effacer aussi le moment","garder la date à côté",
          "Le nom ne porte pas de temps. Une phrase disait « a planté » — le nom ne dit plus si c'est fait, prévu ou en cours. Ajoutez l'année, toujours."],
         ["enchaîner trois noms de suite","alterner phrases et nominalisations",
          "« La mesure de l'observation de la répartition… » est illisible. La nominalisation allège une phrase sur trois, pas les trois."],
       ]},

      {t:'check', h:"Est-ce que c'est clair maintenant ?",
       p:"Quatre transformations.",
       qs:[
         {q:"« On a mesuré la canopée par avion. » →", opts:["la mesure de la canopée par avion","le mesurage de la canopée"], ok:0,
          fb:"<i>Mesurer</i> donne <b>la mesure</b>, un nom sans suffixe."},
         {q:"« Les résidents arrosent les arbres. » →", opts:["l'arrosement des arbres","l'arrosage des arbres"], ok:1,
          fb:"<b>L'arrosage</b>. La famille en -age s'impose ici."},
         {q:"Ce que la nominalisation efface, c'est…", opts:["qui agit et quand","le sujet du texte"], ok:0,
          fb:"Le nom ne porte ni personne ni temps : remettez-les si ça compte."},
         {q:"Pourquoi est-elle l'outil du résumé ?", opts:["elle raccourcit et elle éloigne du texte source","elle rend le texte plus savant"], ok:0,
          fb:"Les deux exigences du résumé, réglées d'un même geste."},
       ]},

      {t:'revoir', h:"À retenir",
       p:"Quatre familles : <b>-tion</b> (plantation), <b>-ment</b> (remplacement), <b>-age</b> (arrosage), <b>rien du tout</b> (la perte, le choix). Elle raccourcit et elle vous éloigne du texte copié. Elle efface <b>qui</b> et <b>quand</b> : remettez-les quand ils comptent."},
    ]
  },

  t2subst: {
    eye:'Mini-leçon', tit:"Reprendre une idée sans répéter le mot",
    blocs:[
      {t:'texte', h:"Le mot qui revient six fois",
       p:"Dans un premier résumé, le même mot revient à chaque phrase : arbre, arbre, arbre. Le texte devient lourd, et surtout il paraît pauvre — comme si son auteur n'avait qu'un mot. Un texte de niveau intermédiaire se reconnaît à ceci : il reprend la même chose de plusieurs façons, et le lecteur suit sans effort.",
       note:"C'est ce que le programme appelle la <b>reprise de l'information</b>. Ce n'est pas un ornement : c'est ce qui tient un texte ensemble."},

      {t:'ana', h:"Le mot plus général",
       p:"On remplace un mot précis par un mot qui l'englobe. Le lecteur fait le lien tout seul.",
       mots:[['Première mention','« La ville a planté quatre cents érables. »'],['Reprise','« Ces <b>arbres</b> seront arrosés trois ans. »'],['Autres exemples','un dépliant → ce document · une érablière → ce boisé',true]],
       say:"La ville a planté quatre cents érables. Ces arbres seront arrosés pendant trois ans.",
       note:"Le mot général doit vraiment englober le premier. « Ces plantes » pour des érables serait juste, mais bizarre : trop général."},

      {t:'ana', h:"Le mot voisin, ou synonyme",
       p:"On remplace par un mot qui dit à peu près la même chose. « À peu près » suffit : le contexte fait le reste.",
       mots:[['Première mention','« le relevé aérien de l\'an dernier »'],['Reprise','« Cette <b>mesure</b> couvre tout le territoire. »'],['Autres exemples','une rencontre → cette réunion · un désaccord → cette divergence',true]],
       say:"Le relevé aérien de l'an dernier. Cette mesure couvre tout le territoire.",
       note:"Deux synonymes ne sont jamais parfaitement égaux. Vérifiez que la nuance ne trahit pas : <i>divergence</i> est plus doux que <i>désaccord</i>."},

      {t:'ana', h:"Le nom tiré du verbe, et la description",
       p:"Deux procédés de plus, et les plus élégants. Le premier reprend l'action par son nom ; le second remplace le nom par ce qu'on en dit.",
       mots:[['Par le nom','« On a planté quatre cents arbres. Cette <b>plantation</b>… »'],['Par la description','« le stationnement du centre → ce <b>secteur minéralisé</b> »'],['Par le résumé','« Youssouf voulait compter les troncs → sa <b>proposition</b> »',true]],
       say:"On a planté quatre cents arbres. Cette plantation a coûté trois ans d'entretien.",
       note:"La description ajoute un renseignement en même temps qu'elle reprend : c'est deux choses pour le prix d'une."},

      {t:'labo', h:"Quatre façons de reprendre la même chose",
       p:"Choisissez ce qu'on reprend, puis le procédé.",
       axes:[
         {id:'r', lbl:'On reprend quoi ?', opts:[['a','quatre cents érables'],['b','la proposition de Youssouf'],['c','le stationnement']]},
         {id:'p', lbl:'Comment ?', opts:[['1','mot plus général'],['2','description'],['3','nom de l\'action']]}],
       out:{
         a1:{w:["ces arbres"], say:"ces arbres", n:'le mot général : le plus simple et le plus sûr'},
         a2:{w:["ces jeunes plants installés l'automne dernier"], say:"ces jeunes plants installés l'automne dernier", n:'la description : elle reprend et elle ajoute'},
         a3:{w:["cette plantation"], say:"cette plantation", n:'le nom tiré du verbe de la phrase précédente'},
         b1:{w:["cette idée"], say:"cette idée", n:'très général, mais parfaitement clair en contexte'},
         b2:{w:["cette méthode plus rapide mais moins précise"], say:"cette méthode plus rapide mais moins précise", n:'la description porte un jugement : attention'},
         b3:{w:["sa proposition"], say:"sa proposition", n:'un nom qui résume toute l\'action d\'une phrase'},
         c1:{w:["ce lieu"], say:"ce lieu", n:'un peu vague : à éviter s\'il y a plusieurs lieux'},
         c2:{w:["ce secteur minéralisé aux trois quarts"], say:"ce secteur minéralisé aux trois quarts", n:'reprend et renseigne en même temps'},
         c3:{w:["cet aménagement"], say:"cet aménagement", n:'le nom de ce qui a été fait à cet endroit'},
       },
       note:"Le déterminant démonstratif — <b>ce, cette, ces</b> — est presque toujours là : c'est lui qui dit au lecteur « je reprends »."},

      {t:'ex', h:"Six reprises, dans l'ordre d'un paragraphe",
       p:"Comment un même sujet se reprend six fois sans se répéter.",
       rows:[
         ["1re mention","« quatre cents érables plantés l'an dernier »"],
         ["mot général","« ces arbres »"],
         ["nom de l'action","« cette plantation »"],
         ["description","« ces jeunes plants encore tenus par des tuteurs »"],
         ["synonyme","« ces sujets », en langue d'horticulture"],
         ["pronom","« ils », quand il n'y a plus d'ambiguïté"],
       ]},

      {t:'piege', h:"Trois pièges de la reprise",
       rows:[
         ["reprendre par un mot ambigu","vérifier qu'il n'y a qu'un candidat",
          "Si le paragraphe parle d'arbres et de trottoirs, « ces éléments » ne désigne plus rien. Le lecteur s'arrête, relit, et vous avez perdu."],
         ["changer de sens en changeant de mot","choisir un synonyme vraiment voisin",
          "Reprendre « un désaccord » par « une dispute » n'est pas neutre : vous venez de raconter autre chose que ce qui s'est passé."],
         ["employer « ils » sans antécédent clair","nommer avant de pronominaliser",
          "« Ils disent que… » — qui, ils ? Le pronom se met après une reprise nominale, jamais à sa place."],
       ]},

      {t:'check', h:"Est-ce que c'est clair maintenant ?",
       p:"Quatre reprises à juger.",
       qs:[
         {q:"« quatre cents érables » repris par « ces arbres » :", opts:["un mot plus général","un synonyme"], ok:0,
          fb:"L'arbre englobe l'érable : c'est le procédé du mot général."},
         {q:"« Youssouf voulait compter les troncs » repris par « sa proposition » :", opts:["un nom qui résume l'action","une description"], ok:0,
          fb:"Un seul nom remplace toute la phrase précédente."},
         {q:"Quel mot signale presque toujours une reprise ?", opts:["ce, cette, ces","un, une, des"], ok:0,
          fb:"Le démonstratif dit au lecteur : je reparle de ce dont je viens de parler."},
         {q:"Un pronom « ils » se place…", opts:["dès la première mention","après une reprise nominale claire"], ok:1,
          fb:"Sinon personne ne sait qui sont « ils »."},
       ]},

      {t:'revoir', h:"À retenir",
       p:"Quatre procédés : le <b>mot plus général</b>, le <b>synonyme</b>, le <b>nom tiré du verbe</b>, la <b>description</b>. Presque toujours avec <b>ce, cette, ces</b>. Un texte qui ne reprend jamais se répète ; un texte qui reprend mal devient illisible."},
    ]
  },

  t2refor: {
    eye:'Mini-leçon', tit:"Autrement dit, quant à, en somme",
    blocs:[
      {t:'texte', h:"Ce que les connecteurs font au lecteur",
       p:"Un résumé sans connecteurs se lit comme une liste : chaque phrase repart de zéro, et le lecteur doit deviner lui-même le rapport entre elles. Avec deux ou trois connecteurs bien placés, les mêmes phrases se tiennent par la main. Rien n'a été ajouté au contenu ; tout a changé dans la lecture.",
       note:"Ce sont les mêmes mots que ceux du défi 1, vus de l'autre côté : là vous les entendiez, ici vous les écrivez."},

      {t:'ana', h:"Reformuler : autrement dit, c'est-à-dire, en somme",
       p:"Ils annoncent que rien de neuf ne vient : la même chose, en plus simple ou en plus court.",
       mots:[['Pour une phrase','« <b>Autrement dit</b>, l\'arbre refroidit l\'air autour de lui. »'],['Pour préciser','« <b>C\'est-à-dire</b> la surface couverte par les cimes. »'],['Pour tout un paragraphe','« <b>En somme</b>, c\'est la canopée qu\'il faut mesurer. »',true]],
       say:"Autrement dit, l'arbre refroidit l'air autour de lui. En somme, c'est la canopée qu'il faut mesurer.",
       note:"<b>En somme</b> rassemble et conclut : une seule fois par texte, à la fin. L'employer trois fois annule son effet."},

      {t:'ana', h:"Changer de sujet : quant à, en ce qui concerne, à propos de",
       p:"Ils préviennent le lecteur : je quitte ce dont je parlais, voici le point suivant.",
       mots:[['Le plus court','« <b>Quant au</b> secteur est, il n\'a pas été mesuré. »'],['Le plus courant','« <b>En ce qui concerne</b> l\'arrosage, la ville demande de l\'aide. »'],['Le plus souple','« <b>À propos de</b> la méthode, une question reste ouverte. »',true]],
       say:"Quant au secteur est, il n'a pas été mesuré. En ce qui concerne l'arrosage, la ville demande de l'aide.",
       note:"<b>Quant à</b> + le = <b>quant au</b> · + les = <b>quant aux</b>. Et il s'écrit avec un <b>t</b>, jamais comme <i>quand</i>."},

      {t:'ana', h:"Marquer la conséquence : par conséquent, donc, ainsi",
       p:"Ils disent que ce qui suit découle de ce qui précède. C'est le connecteur du raisonnement, celui qui montre que vous avez compris et pas seulement recopié.",
       mots:[['À l\'écrit','« La surface est minéralisée aux trois quarts ; <b>par conséquent</b>, le secteur chauffe. »'],['À l\'oral','« <b>Donc</b>, le secteur chauffe plus que les autres. »'],['Plus soigné','« <b>Ainsi</b> s\'explique l\'écart entre les deux rues. »',true]],
       say:"La surface est minéralisée aux trois quarts ; par conséquent, le secteur chauffe davantage.",
       note:"Le point-virgule devant <i>par conséquent</i> est la ponctuation attendue : deux propositions liées, plus fortes qu'une virgule ne le permettrait."},

      {t:'labo', h:"Le bon connecteur au bon endroit",
       p:"Choisissez ce que vous voulez faire, puis le registre.",
       axes:[
         {id:'b', lbl:'Vous voulez…', opts:[['a','redire plus simplement'],['b','changer de point'],['c','conclure'],['d','montrer la conséquence']]},
         {id:'r', lbl:'Où ?', opts:[['1','à l\'oral'],['2','à l\'écrit']]}],
       out:{
         a1:{w:["Autrement dit…"], say:"Autrement dit, l'arbre refroidit l'air.", n:'passe très bien dans un exposé'},
         a2:{w:["C'est-à-dire que…"], say:"C'est-à-dire que l'arbre refroidit l'air.", n:'un peu plus écrit, très clair'},
         b1:{w:["Maintenant, du côté de…"], say:"Maintenant, du côté de notre quartier…", n:'naturel à l\'oral, à éviter dans un texte'},
         b2:{w:["En ce qui concerne…"], say:"En ce qui concerne notre quartier…", n:'la formule attendue dans un travail écrit'},
         c1:{w:["Pour finir…"], say:"Pour finir, c'est la canopée qui compte.", n:'annonce la dernière phrase d\'un exposé'},
         c2:{w:["En somme…"], say:"En somme, c'est la canopée qu'il faut mesurer.", n:'rassemble tout le paragraphe : une seule fois'},
         d1:{w:["Donc…"], say:"Donc, le secteur chauffe plus que les autres.", n:'suffit largement à l\'oral'},
         d2:{w:["Par conséquent…"], say:"Par conséquent, le secteur chauffe davantage.", n:'la forme écrite, précédée d\'un point-virgule'},
       },
       note:"Un connecteur par idée. Dans un résumé de dix lignes, trois suffisent."},

      {t:'ex', h:"Six connecteurs et leur emploi",
       p:"À gauche le connecteur, à droite ce qu'il promet au lecteur.",
       rows:[
         ["autrement dit","la même idée, en plus simple"],
         ["c'est-à-dire","la précision de ce qui vient d'être nommé"],
         ["quant à","nouveau point ; ne rattachez pas au précédent"],
         ["en ce qui concerne","même chose, un ton plus soigné"],
         ["par conséquent","ce qui suit découle de ce qui précède"],
         ["en somme","la fin : tout tient dans cette phrase"],
       ]},

      {t:'piege', h:"Trois pièges d'écriture",
       rows:[
         ["« quand à » au lieu de « quant à »","le t de quant à",
          "Ils se prononcent pareil et ne s'écrivent pas pareil. <i>Quant à</i> est suivi d'un nom ; <i>quand</i> est suivi d'un verbe."],
         ["mettre « en somme » au milieu du texte","le garder pour la dernière phrase",
          "Il annonce que tout ce qui précède va tenir dans une phrase. S'il en reste trois paragraphes derrière, le lecteur est désorienté."],
         ["commencer chaque phrase par un connecteur","un par idée",
          "Un texte saturé de connecteurs devient plus difficile à lire qu'un texte qui n'en a pas. Ils marquent les virages, et une route a peu de virages."],
       ]},

      {t:'check', h:"Est-ce que c'est clair maintenant ?",
       p:"Quatre choix.",
       qs:[
         {q:"Vous venez d'expliquer un mécanisme et vous le redites en une phrase simple.", opts:["autrement dit","quant à"], ok:0,
          fb:"C'est exactement l'emploi de <i>autrement dit</i>."},
         {q:"Vous passez des chiffres de la ville à ceux de votre secteur.", opts:["par conséquent","quant à"], ok:1,
          fb:"Changement de point : <i>quant à notre secteur…</i>"},
         {q:"« ___ le secteur chauffe davantage. » (après une cause)", opts:["Par conséquent","En somme"], ok:0,
          fb:"Une conséquence se marque par <i>par conséquent</i>."},
         {q:"Combien de fois emploie-t-on « en somme » dans un résumé ?", opts:["une seule fois, à la fin","à chaque paragraphe"], ok:0,
          fb:"Il rassemble tout : deux fois, et il ne rassemble plus rien."},
       ]},

      {t:'revoir', h:"À retenir",
       p:"<b>Reformuler</b> : autrement dit, c'est-à-dire · <b>changer de point</b> : quant à, en ce qui concerne, à propos de · <b>conclure</b> : en somme, une seule fois · <b>conséquence</b> : par conséquent à l'écrit, donc à l'oral. Trois connecteurs suffisent dans dix lignes."},
    ]
  },

  t2garde: {
    eye:'Mini-leçon', tit:"Ce qu'un résumé garde, et pourquoi le reste sort",
    blocs:[
      {t:'texte', h:"Résumer, ce n'est pas raccourcir",
       p:"Raccourcir, c'est enlever une phrase sur deux : on obtient un texte plus court qui ne répond toujours pas à la question. Résumer, c'est partir de <b>sa</b> question et n'aller chercher dans le texte que ce qui y répond. Deux équipes qui résument la même fiche avec deux questions différentes doivent produire deux résumés différents. Si elles produisent le même, aucune des deux n'a résumé.",
       note:"D'où la règle : on écrit sa question de départ en haut de sa feuille, et on ne l'efface pas."},

      {t:'ana', h:"La question à poser devant chaque phrase",
       p:"Une seule, et elle ne se négocie pas : <b>est-ce que ceci aide à répondre à ma question ?</b>",
       mots:[['Si oui','la phrase reste, reformulée avec vos mots'],['Si non','elle sort, même si elle est vraie et intéressante'],['Si vous hésitez','elle sort : l\'hésitation est déjà une réponse',true]],
       say:"Est-ce que ceci aide à répondre à ma question de départ ?",
       note:"C'est la seule question. Toutes les autres — est-ce important ? est-ce beau ? l'ai-je cherché longtemps ? — mènent à un résumé qui déborde."},

      {t:'ana', h:"Ce qui reste presque toujours",
       p:"Quatre sortes de renseignements survivent au tri, dans à peu près tous les sujets.",
       mots:[['La définition','ce dont on parle, dit une fois, en clair'],['La cause','pourquoi la chose se produit'],['Les chiffres datés','du territoire ou du cas étudié, avec leur année'],['Les réserves de la source','ce que la source elle-même présente comme incertain',true]],
       say:"La définition, la cause, les chiffres datés, et les réserves de la source.",
       note:"La quatrième est celle qu'on oublie le plus. Reprendre la prudence d'une source, c'est ce qui distingue un travail honnête d'un travail rapide."},

      {t:'ana', h:"Ce qui sort presque toujours",
       p:"Ce qui décrit la source au lieu de décrire le sujet.",
       mots:[['Les coordonnées','téléphone, adresse, à qui s\'adresser'],['Le financement','budgets, subventions, partenaires'],['L\'histoire de l\'organisme','sa fondation, ses prix, sa mission'],['Les dates de publication','sauf celle du chiffre que vous citez',true]],
       say:"Les coordonnées, le financement, l'histoire de l'organisme.",
       note:"Ces renseignements ne sont pas inutiles : ils sont utiles à autre chose. Gardez-les dans vos notes, hors du résumé."},

      {t:'labo', h:"Deux questions, deux résumés",
       p:"Choisissez un renseignement de la fiche, puis la question de départ.",
       axes:[
         {id:'r', lbl:'Quel renseignement ?', opts:[['a','le budget du programme'],['b','les surfaces sombres'],['c','l\'arrosage sur trois ans']]},
         {id:'q', lbl:'Quelle question ?', opts:[['1','pourquoi certaines rues chauffent'],['2','comment la ville s\'y prend']]}],
       out:{
         a1:{w:["On enlève."], say:"On enlève : le budget ne dit pas pourquoi une rue chauffe.", n:'vrai, chiffré, et hors sujet'},
         a2:{w:["On garde."], say:"On garde : le budget fait partie des moyens de la ville.", n:'la même phrase change de statut avec la question'},
         b1:{w:["On garde."], say:"On garde : c'est la cause même du phénomène.", n:'le cœur de la réponse'},
         b2:{w:["On enlève."], say:"On enlève : ceci explique le problème, pas la méthode.", n:'intéressant, mais à côté de la question posée'},
         c1:{w:["On enlève, ou presque."], say:"On enlève : l'arrosage concerne l'entretien, pas la chaleur.", n:'sauf si l\'on explique pourquoi les jeunes arbres rafraîchissent peu'},
         c2:{w:["On garde."], say:"On garde : c'est la partie la plus difficile du programme.", n:'central pour une question sur la méthode'},
       },
       note:"Le même texte, deux questions, deux tris opposés. C'est la démonstration que le tri ne vient pas du texte : il vient de vous."},

      {t:'ex', h:"Six renseignements, une même question",
       p:"Question de départ : pourquoi certaines rues de Rivière-Noire sont-elles plus chaudes ?",
       rows:[
         ["les surfaces sombres absorbent le rayonnement","on garde — c'est la cause"],
         ["17 % de canopée, relevé de l'an dernier","on garde — chiffré et daté"],
         ["un arbre de deux ans rafraîchit très peu","on garde — explique l'écart entre deux rues"],
         ["le programme est financé par les travaux publics","on enlève — décrit la ville, pas la chaleur"],
         ["appeler les travaux publics pour signaler un arbre","on enlève — ce sont des coordonnées"],
         ["la ville avertit que la comparaison est délicate","on garde — c'est la réserve de la source"],
       ]},

      {t:'piege', h:"Trois pièges du tri",
       rows:[
         ["garder parce que c'est intéressant","garder parce que ça répond",
          "Le budget est un gros chiffre, la fondation de l'organisme est une jolie histoire. Ces phrases-là ne mentent pas : elles occupent la place de celles qui répondaient."],
         ["garder parce que ça a coûté du temps à trouver","accepter de jeter",
          "Deux heures de recherche pour un renseignement hors sujet, c'est deux heures. Les garder dans le résumé, c'est en plus abîmer le travail."],
         ["résumer avant d'avoir écrit sa question","écrire la question en haut de la feuille",
          "Sans question devant les yeux, on résume le texte au lieu de résumer ce qui sert. C'est le défaut que Ghislaine a repéré en trois secondes."],
       ]},

      {t:'check', h:"Est-ce que c'est clair maintenant ?",
       p:"Quatre décisions, avec la question : pourquoi certaines rues chauffent-elles ?",
       qs:[
         {q:"« La fiche a été mise à jour au mois de mai. »", opts:["on garde","on enlève"], ok:1,
          fb:"C'est la date de la fiche, pas celle d'un chiffre cité : hors résumé."},
         {q:"« Dans les secteurs touchés, la surface minéralisée dépasse les trois quarts. »", opts:["on garde","on enlève"], ok:0,
          fb:"Chiffré, sur le territoire étudié, et directement lié à la cause."},
         {q:"« La ville avertit que les comparaisons entre villes sont délicates. »", opts:["on garde","on enlève"], ok:0,
          fb:"Une réserve de la source se reprend : c'est ce qui rend le travail honnête."},
         {q:"Deux équipes résument la même fiche avec deux questions différentes. Elles doivent obtenir…", opts:["deux résumés différents","le même résumé"], ok:0,
          fb:"Sinon, aucune des deux n'a résumé : elles ont raccourci."},
       ]},

      {t:'revoir', h:"À retenir",
       p:"Une seule question devant chaque phrase : <b>est-ce que ça répond à ma question de départ ?</b> Restent presque toujours la <b>définition</b>, la <b>cause</b>, les <b>chiffres datés</b> et les <b>réserves de la source</b>. Sortent les coordonnées, le financement et l'histoire de l'organisme."},
    ]
  },

  t3anim: {
    eye:'Mini-leçon', tit:"Les six gestes de parole de qui anime",
    blocs:[
      {t:'texte', h:"Animer n'est pas présider",
       p:"On imagine celui qui anime comme celui qui décide et qui parle le plus. C'est le contraire : il parle souvent et brièvement, et presque jamais de son propre avis. Son travail tient en six gestes, et chacun se fait avec une phrase toute prête. Apprenez les six phrases, et l'animation cesse d'être une affaire de tempérament.",
       note:"C'est ce que Ghislaine dit à Neusa dès le premier jour : ce n'est pas un caractère, c'est un rôle, et un rôle s'apprend."},

      {t:'ana', h:"Ouvrir et cadrer",
       p:"Premier geste, trente secondes, et il détermine le reste. On rappelle la question, le temps dont on dispose et ce qu'on doit avoir décidé à la fin.",
       mots:[['La phrase','« Je rappelle où on en est : on cherche… Il nous reste quarante minutes. »'],['Ce que ça fait','tout le monde repart du même endroit'],['Sans ce geste','chacun repart de là où il s\'était arrêté dans sa tête',true]],
       say:"Je rappelle où on en est : on cherche pourquoi certaines rues sont plus chaudes. On a quarante minutes.",
       note:"Une rencontre qui commence sans cadrage ne rattrape jamais ce retard-là."},

      {t:'ana', h:"Donner la parole, et la reprendre",
       p:"Deuxième et troisième gestes. Donner, c'est nommer quelqu'un ; reprendre, c'est interrompre poliment celui qui garde la parole trop longtemps.",
       mots:[['Donner','« Youssouf, tu voulais commencer. »'],['Reprendre','« Je t\'arrête une seconde — Miguel n\'a pas encore répondu. »'],['Ce que ça fait','le silencieux parle, le bavard respire',true]],
       say:"Youssouf, tu voulais commencer. Je t'arrête une seconde : Miguel n'a pas encore répondu.",
       note:"Interrompre est le geste qui coûte le plus à apprendre, et c'est celui qui manque le plus. Ce n'est pas impoli : c'est le rôle."},

      {t:'ana', h:"Faire préciser",
       p:"Quatrième geste. Devant une affirmation vague, une question factuelle — jamais un jugement.",
       mots:[['Devant un chiffre','« Combien, exactement ? Et comment le sais-tu ? »'],['Devant une proposition','« Tu comptes quoi, au juste : tous les arbres ou ceux de la rue ? »'],['Ce que ça fait','le désaccord se déplace du général vers le précis',true]],
       say:"Tu comptes quoi, exactement : tous les arbres, ou seulement ceux du bord de la rue ?",
       note:"Neuf désaccords sur dix viennent d'un mot que deux personnes n'entendaient pas pareil. Faire préciser en règle la moitié."},

      {t:'ana', h:"Reformuler, et fermer",
       p:"Cinquième et sixième gestes, et les deux plus utiles. Reformuler, c'est redire la position de quelqu'un jusqu'à ce qu'il s'y reconnaisse. Fermer, c'est énumérer les décisions à voix haute pendant qu'un autre vérifie.",
       mots:[['Reformuler','« Je reformule, et tu me dis si je me trompe : tu dis que… »'],['Fermer','« Je résume les décisions, et toi, tu vérifies tes notes pendant que je parle. »'],['Ce que ça fait','personne ne sort avec une version différente',true]],
       say:"Je reformule, et tu me dis si je me trompe. Je résume les décisions : premièrement…",
       note:"Faire vérifier les décisions par la personne aux notes, à voix haute, prend deux minutes et évite une rencontre entière."},

      {t:'labo', h:"Que dire, et à quel moment ?",
       p:"Choisissez une situation, puis le geste.",
       axes:[
         {id:'s', lbl:'Que se passe-t-il ?', opts:[['a','quelqu\'un parle depuis six minutes'],['b','deux personnes se contredisent'],['c','une affirmation est vague'],['d','il reste cinq minutes']]},
         {id:'g', lbl:'Quel ton ?', opts:[['1','direct'],['2','plus enveloppé']]}],
       out:{
         a1:{w:["Je t'arrête là, Youssouf."], say:"Je t'arrête là, Youssouf.", n:'net, et parfaitement acceptable dans ce rôle'},
         a2:{w:["Je te propose qu'on entende Miguel là-dessus."], say:"Je te propose qu'on entende Miguel là-dessus.", n:'interrompt sans le dire : très efficace'},
         b1:{w:["Vous n'êtes pas en désaccord sur tout."], say:"Vous n'êtes pas en désaccord sur tout.", n:'montre que l\'écart est plus étroit qu\'il n\'y paraît'},
         b2:{w:["Je reformule les deux positions, corrigez-moi."], say:"Je reformule les deux positions, et vous me corrigez.", n:'le geste central de l\'animation'},
         c1:{w:["Combien, exactement ?"], say:"Combien, exactement ?", n:'trois mots, et la discussion devient utilisable'},
         c2:{w:["Peux-tu préciser ce que tu comptes ?"], say:"Peux-tu préciser ce que tu comptes ?", n:'même effet, un ton plus doux'},
         d1:{w:["On termine : voici les décisions."], say:"On termine : voici les décisions.", n:'ferme la rencontre au lieu de la laisser s\'éteindre'},
         d2:{w:["Je résume, et tu vérifies pendant que je parle."], say:"Je résume, et tu vérifies pendant que je parle.", n:'fait valider les décisions par une autre personne'},
       },
       note:"Aucune de ces phrases ne donne d'avis. C'est le signe qu'elles appartiennent au rôle et non à la personne."},

      {t:'ex', h:"Les six gestes, dans l'ordre d'une rencontre",
       p:"Ce que fait la personne qui anime, du début à la fin.",
       rows:[
         ["ouvrir et cadrer","« Je rappelle où on en est. On a quarante minutes. »"],
         ["donner la parole","« Youssouf, tu voulais commencer. »"],
         ["faire préciser","« Tu comptes quoi, exactement ? »"],
         ["reprendre la parole","« Je t'arrête une seconde, Miguel n'a pas répondu. »"],
         ["reformuler","« Je reformule, et vous me dites si je me trompe. »"],
         ["fermer","« Je résume les décisions ; vérifie tes notes pendant que je parle. »"],
       ]},

      {t:'piege', h:"Trois pièges de la personne qui anime",
       rows:[
         ["donner son avis en premier","le garder pour la fin, ou se le faire demander",
          "Dès que celui qui anime prend parti, les autres se rangent ou se taisent. Vous avez le droit d'avoir un avis ; annoncez alors que vous quittez un instant votre rôle."],
         ["laisser parler par politesse","interrompre, c'est le rôle",
          "Six minutes de monologue coûtent le tour de parole de quelqu'un d'autre. Interrompre n'est pas un manque de respect envers celui qui parle : c'en est un envers celui qui se tait."],
         ["fermer sans récapituler","énumérer les décisions à voix haute",
          "Une rencontre qui s'éteint faute de temps produit trois versions différentes de ce qui a été décidé, et on les découvre la semaine suivante."],
       ]},

      {t:'check', h:"Est-ce que c'est clair maintenant ?",
       p:"Quatre situations.",
       qs:[
         {q:"Deux coéquipiers se contredisent. Le premier geste est…", opts:["reformuler les deux positions","trancher tout de suite"], ok:0,
          fb:"Neuf fois sur dix, le désaccord se dégonfle pendant la reformulation."},
         {q:"Quelqu'un affirme « il y a beaucoup d'arbres ». Vous demandez…", opts:["combien, et comment le sais-tu ?","es-tu certain ?"], ok:0,
          fb:"Une question factuelle, jamais une mise en doute de la personne."},
         {q:"Interrompre celui qui parle depuis six minutes, c'est…", opts:["impoli","le rôle de qui anime"], ok:1,
          fb:"C'est ce qui protège le tour de parole des autres."},
         {q:"À la fin, on énumère les décisions…", opts:["pendant qu'une autre personne vérifie ses notes","dans le compte rendu seulement"], ok:0,
          fb:"À voix haute, vérifiées sur-le-champ : deux minutes bien employées."},
       ]},

      {t:'revoir', h:"À retenir",
       p:"Six gestes : <b>ouvrir et cadrer · donner la parole · faire préciser · reprendre la parole · reformuler · fermer sur des décisions</b>. Aucun ne demande d'avoir un avis. C'est pour cela qu'ils s'apprennent."},
    ]
  },

  t3conc: {
    eye:'Mini-leçon', tit:"Bien que, même si : dire non sans casser l'équipe",
    blocs:[
      {t:'texte', h:"Accorder d'abord, maintenir ensuite",
       p:"Dire « je ne suis pas d'accord » met l'autre en position de défendre son idée : la discussion devient un match. La concession fait autre chose — elle <b>donne raison</b> à l'autre sur un point avant de maintenir sa position. Celui qui l'entend n'a plus rien à défendre, puisqu'on vient de lui accorder son argument. C'est le geste de langue le plus utile d'une équipe.",
       note:"Miguel l'emploie dans la rencontre : « Bien que ce soit plus long, on pourrait noter autre chose. » Youssouf accepte trois répliques plus tard."},

      {t:'ana', h:"Bien que + subjonctif, toujours",
       p:"Une des rares conjonctions qui n'acceptent rien d'autre. Aucune exception.",
       mots:[['Les quatre à savoir','bien qu\'il <b>soit</b> · bien que nous <b>ayons</b> · bien que ça <b>prenne</b> · bien qu\'elle <b>puisse</b>'],['Exemple','« <b>Bien que</b> ton idée <b>soit</b> plus rapide, elle ne mesure pas ce qu\'on cherche. »'],['Sa variante','<i>malgré que</i>, aussi avec le subjonctif, moins bien reçu à l\'écrit',true]],
       say:"Bien que ton idée soit plus rapide, elle ne mesure pas ce qu'on cherche.",
       note:"Si le subjonctif vous fait hésiter, prenez <i>même si</i> : le sens est le même et la construction est plus simple."},

      {t:'ana', h:"Même si + indicatif, toujours",
       p:"Jamais de subjonctif après <i>même si</i>. C'est l'erreur la plus courante, et elle vient précisément de <i>bien que</i>.",
       mots:[['On dit','même si c\'<b>est</b> long · même si tu <b>as</b> raison · même si ça <b>prend</b> deux heures'],['On ne dit pas','« même si ce soit long »'],['Exemple','« <b>Même si</b> je <b>trouve</b> qu\'on complique, je suis d\'accord. »',true]],
       say:"Même si je trouve qu'on complique, je suis d'accord avec la méthode.",
       note:"<i>Même si</i> est plus direct, se dit très bien entre coéquipiers, et n'exige aucun subjonctif. C'est celui qu'on emploie à l'oral."},

      {t:'ana', h:"Les autres façons de concéder",
       p:"Trois de plus, dont deux très courantes à l'oral québécois.",
       mots:[['Avec un nom','<b>malgré</b> la longueur · <b>en dépit de</b> son coût'],['Avec un verbe conjugué','<b>quand même</b> · <b>tout de même</b> : « C\'est long ; on le fait quand même. »'],['En deux temps','« Tu as raison sur le fond. <b>Cela dit</b>, la méthode ne mesure pas ça. »',true]],
       say:"Tu as raison sur le fond. Cela dit, la méthode ne mesure pas ce qu'on cherche.",
       note:"« Tu as raison, cela dit… » est la forme la plus douce de toutes, et souvent la plus efficace en équipe."},

      {t:'labo', h:"La même objection, quatre formulations",
       p:"Choisissez ce que vous accordez, puis la construction.",
       axes:[
         {id:'a', lbl:'Vous accordez…', opts:[['a','que c\'est plus rapide'],['b','qu\'il a raison sur le fond'],['c','que ça prend du temps']]},
         {id:'c', lbl:'Avec quelle construction ?', opts:[['1','bien que + subjonctif'],['2','même si + indicatif'],['3','en deux phrases']]}],
       out:{
         a1:{w:["Bien que ce soit plus rapide, ça ne mesure pas la bonne chose."], say:"Bien que ce soit plus rapide, ça ne mesure pas la bonne chose.", n:'la forme écrite, la plus soignée'},
         a2:{w:["Même si c'est plus rapide, ça ne mesure pas la bonne chose."], say:"Même si c'est plus rapide, ça ne mesure pas la bonne chose.", n:'la forme orale, aussi correcte'},
         a3:{w:["C'est plus rapide, c'est vrai. Cela dit, ça ne mesure pas la bonne chose."], say:"C'est plus rapide, c'est vrai. Cela dit, ça ne mesure pas la bonne chose.", n:'la plus douce : l\'accord occupe une phrase entière'},
         b1:{w:["Bien que tu aies raison sur le fond, la méthode reste à revoir."], say:"Bien que tu aies raison sur le fond, la méthode reste à revoir.", n:'avoir au subjonctif : que tu aies'},
         b2:{w:["Même si tu as raison sur le fond, la méthode reste à revoir."], say:"Même si tu as raison sur le fond, la méthode reste à revoir.", n:'indicatif : tu as, sans hésitation'},
         b3:{w:["Tu as raison sur le fond. La méthode, elle, reste à revoir."], say:"Tu as raison sur le fond. La méthode, elle, reste à revoir.", n:'le pronom de reprise appuie le contraste'},
         c1:{w:["Bien que ça prenne deux heures, ça en vaut la peine."], say:"Bien que ça prenne deux heures, ça en vaut la peine.", n:'prendre au subjonctif : que ça prenne'},
         c2:{w:["Même si ça prend deux heures, ça en vaut la peine."], say:"Même si ça prend deux heures, ça en vaut la peine.", n:'indicatif : ça prend'},
         c3:{w:["Ça prend deux heures. On le fait quand même."], say:"Ça prend deux heures. On le fait quand même.", n:'le plus court, et très naturel à l\'oral'},
       },
       note:"Les neuf disent la même chose. Choisissez selon l'endroit : l'écrit préfère la première ligne, la rencontre préfère les deux autres."},

      {t:'ex', h:"Six concessions entendues en équipe",
       p:"À gauche ce qu'on accorde, à droite ce qu'on maintient.",
       rows:[
         ["« Bien que ce soit plus long… »","« …on pourrait noter autre chose que le nombre. »"],
         ["« Même si je trouve qu'on complique… »","« …je suis d'accord avec la méthode. »"],
         ["« Bien que la fiche donne un chiffre… »","« …il faut écrire l'année à côté. »"],
         ["« Même si le chiffre vient de la ville… »","« …on le cite avec sa source. »"],
         ["« Tu as raison sur le fond. Cela dit… »","« …la méthode ne mesure pas ça. »"],
         ["« C'est vrai que c'est plus rapide. »","« On perd quand même l'essentiel. »"],
       ]},

      {t:'piege', h:"Trois pièges de la concession",
       rows:[
         ["« même si ce soit »","« même si c'est »",
          "Le subjonctif appartient à <i>bien que</i>, jamais à <i>même si</i>. C'est l'erreur numéro un du niveau intermédiaire, et elle s'entend tout de suite."],
         ["concéder sans rien maintenir","faire suivre d'un mais, ou d'un je pense quand même",
          "« Bien que ce soit plus long… » et rien après : vous n'avez pas concédé, vous avez changé d'avis. La concession n'existe qu'avec sa suite."],
         ["concéder trois fois de suite","une fois, puis on maintient",
          "Trois concessions dans la même intervention et plus personne ne sait ce que vous pensez. Une seule, nette, puis votre position."],
       ]},

      {t:'check', h:"Est-ce que c'est clair maintenant ?",
       p:"Quatre phrases à compléter.",
       qs:[
         {q:"« ___ ce soit plus long, ça en vaut la peine. »", opts:["Bien que","Même si"], ok:0,
          fb:"<i>Soit</i> est un subjonctif : seul <i>bien que</i> l'accepte."},
         {q:"« ___ tu as raison, je maintiens ma position. »", opts:["Bien que","Même si"], ok:1,
          fb:"<i>Tu as</i> est un indicatif : c'est <i>même si</i>."},
         {q:"Une concession doit être suivie…", opts:["de ce qu'on maintient","d'un exemple"], ok:0,
          fb:"Sans la suite, ce n'est plus une concession : c'est un changement d'avis."},
         {q:"À l'oral, entre coéquipiers, on emploiera plutôt…", opts:["même si","bien que"], ok:0,
          fb:"Plus direct, plus simple, et sans subjonctif à fabriquer."},
       ]},

      {t:'revoir', h:"À retenir",
       p:"<b>Bien que + subjonctif</b> (bien que ce soit), <b>même si + indicatif</b> (même si c'est). Le sens est le même ; l'écrit préfère le premier, la rencontre préfère le second. Et une concession appelle toujours ce qu'on maintient derrière."},
    ]
  },

  t3emph: {
    eye:'Mini-leçon', tit:"Mettre en relief : c'est… qui, ce que… c'est",
    blocs:[
      {t:'texte', h:"Comment écrire l'insistance",
       p:"En parlant, vous appuyez sur le mot qui compte, et tout le monde comprend où regarder. Dans un compte rendu ou sur une diapositive, personne n'entend votre voix : la seule façon d'écrire cette insistance est de <b>construire</b> la phrase autrement. C'est ce que font les phrases emphatiques — elles ne changent rien au sens, elles déplacent l'attention.",
       note:"Le programme les appelle des phrases <b>emphatiques</b>, et il en nomme deux procédés : le clivage (c'est… qui) et le pseudoclivage (ce que…, c'est)."},

      {t:'ana', h:"C'est… qui — pour mettre en avant le sujet",
       p:"On encadre celui qui fait l'action. Le verbe s'accorde avec ce qu'on encadre, pas avec « c'est ».",
       mots:[['La phrase plate','Miguel a trouvé la solution.'],['La phrase emphatique','<b>C\'est</b> Miguel <b>qui</b> a trouvé la solution.'],['Avec un pronom','c\'est moi <b>qui</b> anime · c\'est nous <b>qui</b> avons décidé',true]],
       say:"C'est Miguel qui a trouvé la solution. C'est moi qui anime.",
       note:"« C'est moi qui <b>anime</b> », jamais « qui anim<b>e</b>nt » ni « qui animes » : le verbe suit la personne encadrée."},

      {t:'ana', h:"C'est… que — pour tout le reste",
       p:"Complément, moment, lieu, manière : tout ce qui n'est pas le sujet passe par <i>que</i>.",
       mots:[['Le complément','<b>C\'est</b> l\'ombre <b>qu\'</b>on note, pas le nombre.'],['Le moment','<b>C\'est</b> samedi <b>qu\'</b>on y va.'],['Le lieu','<b>C\'est</b> dans le secteur est <b>que</b> l\'écart est le plus grand.',true]],
       say:"C'est l'ombre qu'on note, pas le nombre. C'est samedi qu'on y va.",
       note:"Le choix entre <i>qui</i> et <i>que</i> ne dépend pas de la personne ni de la chose : il dépend de la fonction. Sujet, <i>qui</i> ; le reste, <i>que</i>."},

      {t:'ana', h:"Ce que…, c'est — annoncer avant de dire",
       p:"On pose d'abord la question dans la tête de l'autre, on répond ensuite. C'est la forme de l'animation et de l'exposé.",
       mots:[['Pour un complément','<b>Ce qu\'</b>on cherche, <b>c\'est</b> une différence entre deux rues.'],['Pour un sujet','<b>Ce qui</b> manque, <b>c\'est</b> l\'ombre au sol.'],['Pour une action','<b>Ce que</b> je propose, <b>c\'est</b> de noter les deux.',true]],
       say:"Ce qu'on cherche, c'est une différence entre deux rues. Ce qui manque, c'est l'ombre au sol.",
       note:"<b>Ce qui</b> quand la suite est le sujet du verbe, <b>ce que</b> quand elle en est le complément. Même règle que <i>qui</i> et <i>que</i>, un cran plus loin."},

      {t:'labo', h:"La phrase plate, et ses mises en relief",
       p:"Choisissez une phrase, puis ce que vous voulez mettre en avant.",
       axes:[
         {id:'p', lbl:'Quelle phrase ?', opts:[['a','Miguel note l\'ombre samedi'],['b','la canopée explique l\'écart'],['c','nous partons à dix heures']]},
         {id:'m', lbl:'Quoi mettre en avant ?', opts:[['1','la personne ou la cause'],['2','ce qu\'on fait'],['3','le moment']]}],
       out:{
         a1:{w:["C'est Miguel qui note l'ombre."], say:"C'est Miguel qui note l'ombre.", n:'sujet encadré : c\'est… qui'},
         a2:{w:["C'est l'ombre que Miguel note."], say:"C'est l'ombre que Miguel note.", n:'complément encadré : c\'est… que'},
         a3:{w:["C'est samedi que Miguel note l'ombre."], say:"C'est samedi que Miguel note l'ombre.", n:'le moment : c\'est… que'},
         b1:{w:["C'est la canopée qui explique l'écart."], say:"C'est la canopée qui explique l'écart.", n:'la cause est le sujet : qui'},
         b2:{w:["Ce que la canopée explique, c'est l'écart entre deux rues."], say:"Ce que la canopée explique, c'est l'écart entre deux rues.", n:'pseudoclivage : on annonce, puis on dit'},
         b3:{w:["C'est dans le secteur est que l'écart est le plus grand."], say:"C'est dans le secteur est que l'écart est le plus grand.", n:'le lieu s\'encadre comme le moment'},
         c1:{w:["C'est nous qui avons décidé de partir à dix heures."], say:"C'est nous qui avons décidé de partir à dix heures.", n:'accord du verbe avec nous : avons'},
         c2:{w:["Ce que nous avons décidé, c'est de partir à dix heures."], say:"Ce que nous avons décidé, c'est de partir à dix heures.", n:'la forme d\'un compte rendu'},
         c3:{w:["C'est à dix heures que nous partons."], say:"C'est à dix heures que nous partons.", n:'et non à neuf : l\'heure est l\'information'},
       },
       note:"Écoutez-les : la voix appuie déjà sur le groupe encadré. À l'écrit, la construction fait ce travail toute seule."},

      {t:'ex', h:"Six phrases, avant et après",
       p:"À gauche la phrase plate, à droite la même avec sa mise en relief.",
       rows:[
         ["Miguel a proposé de noter l'ombre.","C'est Miguel qui a proposé de noter l'ombre."],
         ["On note l'ombre, pas le nombre.","C'est l'ombre qu'on note, pas le nombre."],
         ["On y va samedi.","C'est samedi qu'on y va."],
         ["Nous cherchons une différence.","Ce que nous cherchons, c'est une différence."],
         ["L'ombre au sol manque dans ce secteur.","Ce qui manque, c'est l'ombre au sol."],
         ["J'anime la rencontre.","C'est moi qui anime la rencontre."],
       ]},

      {t:'piege', h:"Trois pièges de la mise en relief",
       rows:[
         ["« c'est moi qui anime » écrit « qui animent »","accorder avec la personne encadrée",
          "Le verbe ne s'accorde pas avec <i>c'est</i>. C'est moi qui <b>anime</b>, c'est toi qui <b>animes</b>, c'est nous qui <b>animons</b>."],
         ["employer « qui » pour un complément","sujet = qui, le reste = que",
          "« C'est l'ombre <s>qui</s> on note » est faux : <i>l'ombre</i> est complément du verbe <i>noter</i>, donc <b>que</b>."],
         ["mettre tout en relief","une par paragraphe",
          "Si chaque phrase est emphatique, plus rien ne ressort. La mise en relief marche par contraste avec des phrases ordinaires autour."],
       ]},

      {t:'check', h:"Est-ce que c'est clair maintenant ?",
       p:"Quatre choix.",
       qs:[
         {q:"« ___ Miguel ___ a trouvé la solution. »", opts:["C'est … qui","C'est … que"], ok:0,
          fb:"Miguel fait l'action : c'est le sujet, donc <i>qui</i>."},
         {q:"« ___ l'ombre ___ on note. »", opts:["C'est … qui","C'est … qu'"], ok:1,
          fb:"L'ombre est complément de <i>noter</i> : <i>que</i>."},
         {q:"« C'est nous qui ___ décidé. »", opts:["avons","ont"], ok:0,
          fb:"Le verbe s'accorde avec <i>nous</i>, la personne encadrée."},
         {q:"« ___ manque, c'est l'ombre au sol. »", opts:["Ce qui","Ce que"], ok:0,
          fb:"<i>L'ombre</i> est le sujet de <i>manque</i> : <i>ce qui</i>."},
       ]},

      {t:'revoir', h:"À retenir",
       p:"<b>C'est… qui</b> pour le sujet, avec accord du verbe sur la personne encadrée. <b>C'est… que</b> pour tout le reste. <b>Ce que…, c'est</b> pour annoncer avant de dire. Une mise en relief par paragraphe, pas davantage."},
    ]
  },

  t3rapp: {
    eye:'Mini-leçon', tit:"Rapporter au passé : tout recule d'un cran",
    blocs:[
      {t:'texte', h:"Le savoir qui fait tenir un compte rendu",
       p:"Un compte rendu est fait, du début à la fin, de phrases rapportées : Youssouf a proposé que…, Miguel a répondu que…, elle a précisé que… Sans ce mécanisme, il ne reste qu'une transcription — trois pages du dialogue, que personne ne lira. Avec lui, une page utile. C'est le savoir le plus rentable du module.",
       note:"Le verbe qui introduit est au passé, donc tout ce qui suit recule. Vous ne choisissez pas : le temps de départ décide du temps d'arrivée."},

      {t:'ana', h:"Les quatre reculs à savoir par cœur",
       p:"Quatre couples, et ils couvrent presque tout ce que vous aurez à rapporter.",
       mots:[['présent → imparfait','« Je pars » → il a dit qu\'il <b>partait</b>'],['passé composé → plus-que-parfait','« Je suis parti » → il a dit qu\'il <b>était parti</b>'],['futur → conditionnel présent','« Je partirai » → il a dit qu\'il <b>partirait</b>'],['va + infinitif → allait + infinitif','« Je vais partir » → il a dit qu\'il <b>allait partir</b>',true]],
       say:"Il a dit qu'il partait. Il a dit qu'il était parti. Il a dit qu'il partirait. Il a dit qu'il allait partir.",
       note:"Le troisième couple explique pourquoi le conditionnel du défi 1 revient ici : dans un discours rapporté au passé, il n'exprime aucune incertitude — il exprime l'avenir."},

      {t:'ana', h:"Ce qui ne bouge pas",
       p:"Trois temps sont déjà en arrière : il n'y a pas de cran de plus, et ils restent tels quels.",
       mots:[['L\'imparfait','« Je travaillais » → elle a dit qu\'elle <b>travaillait</b>'],['Le conditionnel','« Je viendrais » → elle a dit qu\'elle <b>viendrait</b>'],['Le subjonctif','« Il faut que je parte » → elle a dit qu\'il fallait qu\'elle <b>parte</b>',true]],
       say:"Elle a dit qu'elle travaillait. Elle a dit qu'elle viendrait.",
       note:"Beaucoup d'élèves reculent l'imparfait vers le plus-que-parfait par excès de zèle. Il n'y a rien à reculer."},

      {t:'ana', h:"Ce qui change aussi, et qu'on oublie",
       p:"Trois choses de plus bougent en même temps que le verbe. Les oublier produit des phrases où l'on ne sait plus de qui ni de quand on parle.",
       mots:[['Les personnes','je → il ou elle · tu → je, selon qui rapporte'],['Les possessifs','mon → son · notre → leur'],['Les repères de temps','aujourd\'hui → <b>ce jour-là</b> · demain → <b>le lendemain</b> · hier → <b>la veille</b>',true]],
       say:"Il a dit qu'il écrivait à Perrine le lendemain.",
       note:"« Il a dit qu'il écrivait demain » se comprend, mais devient faux dès qu'on relit le compte rendu trois jours plus tard. <i>Le lendemain</i> reste juste pour toujours."},

      {t:'ana', h:"La question rapportée",
       p:"Ni point d'interrogation, ni inversion, ni <i>est-ce que</i>. Trois formes seulement.",
       mots:[['Question par oui ou non','« Est-ce que tu viens ? » → elle a demandé <b>s\'il</b> venait'],['Question en quoi','« Tu comptes quoi ? » → elle a demandé <b>ce qu\'</b>il comptait'],['Question avec un mot interrogatif','« Quand pars-tu ? » → elle a demandé <b>quand</b> il partait',true]],
       say:"Elle a demandé s'il venait. Elle a demandé ce qu'il comptait exactement.",
       note:"<i>Qu'est-ce que</i> et <i>quoi</i> deviennent tous les deux <b>ce que</b>. C'est la transformation qu'on rate le plus souvent."},

      {t:'labo', h:"Du dialogue au compte rendu",
       p:"Choisissez une réplique, puis la version rapportée.",
       axes:[
         {id:'r', lbl:'Quelle réplique ?', opts:[['a','« Je propose qu\'on compte. »'],['b','« J\'ai pris la mesure en juillet. »'],['c','« Je vérifierai mes notes. »'],['d','« Tu comptes quoi ? »']]},
         {id:'v', lbl:'Quelle version ?', opts:[['1','au présent'],['2','au passé']]}],
       out:{
         a1:{w:["Il dit qu'il propose qu'on compte."], say:"Il dit qu'il propose qu'on compte.", n:'verbe introducteur au présent : rien ne recule'},
         a2:{w:["Il a dit qu'il proposait qu'on compte."], say:"Il a dit qu'il proposait qu'on compte.", n:'présent → imparfait ; le subjonctif ne bouge pas'},
         b1:{w:["Elle dit qu'elle a pris la mesure en juillet."], say:"Elle dit qu'elle a pris la mesure en juillet.", n:'passé composé conservé'},
         b2:{w:["Elle a précisé qu'elle avait pris la mesure en juillet."], say:"Elle a précisé qu'elle avait pris la mesure en juillet.", n:'passé composé → plus-que-parfait'},
         c1:{w:["Il promet qu'il vérifiera ses notes."], say:"Il promet qu'il vérifiera ses notes.", n:'futur conservé'},
         c2:{w:["Il a promis qu'il vérifierait ses notes."], say:"Il a promis qu'il vérifierait ses notes.", n:'futur → conditionnel présent'},
         d1:{w:["Elle demande ce qu'il compte."], say:"Elle demande ce qu'il compte.", n:'la question devient « ce que », sans inversion'},
         d2:{w:["Elle lui a demandé ce qu'il comptait."], say:"Elle lui a demandé ce qu'il comptait.", n:'et le présent recule à l\'imparfait'},
       },
       note:"Comparez chaque paire : c'est le temps du <b>verbe introducteur</b> qui commande tout le reste."},

      {t:'ex', h:"Six répliques de la rencontre, mises au compte rendu",
       p:"À gauche ce qui a été dit, à droite ce que Neusa a écrit le soir même.",
       rows:[
         ["« Je propose qu'on compte les arbres. »","Youssouf a proposé qu'on compte les arbres."],
         ["« Ça ne prouve rien. »","Miguel a répondu que cela ne prouvait rien."],
         ["« J'ai pris la mesure en juillet. »","Elle a précisé qu'elle avait pris la mesure en juillet."],
         ["« Je vérifierai mes notes. »","Youssouf a promis qu'il vérifierait ses notes."],
         ["« Je vais envoyer le compte rendu. »","Neusa a annoncé qu'elle allait envoyer le compte rendu."],
         ["« J'écris à Perrine demain. »","Miguel a dit qu'il écrivait à Perrine le lendemain."],
       ]},

      {t:'piege', h:"Trois pièges du discours rapporté",
       rows:[
         ["garder « demain » et « aujourd'hui »","le lendemain, ce jour-là",
          "Un compte rendu se relit des semaines plus tard. « Demain » ne veut alors plus rien dire, et personne ne sait quelle date était visée."],
         ["reculer l'imparfait","le laisser tel quel",
          "« Elle a dit qu'elle avait travaillé » ne rapporte pas « je travaillais » : ça rapporte « j'ai travaillé ». Un cran de trop change le sens."],
         ["garder l'inversion de la question","ni inversion ni point d'interrogation",
          "« Elle a demandé quand partait-il ? » n'existe pas. On écrit : elle a demandé <b>quand il partait</b>, avec un point."],
       ]},

      {t:'check', h:"Est-ce que c'est clair maintenant ?",
       p:"Quatre transformations.",
       qs:[
         {q:"« Je pars à dix heures. » → Il a dit qu'il ___ à dix heures.", opts:["partait","est parti"], ok:0,
          fb:"Présent → imparfait. Le premier des quatre reculs."},
         {q:"« Je vérifierai. » → Il a promis qu'il ___.", opts:["vérifiera","vérifierait"], ok:1,
          fb:"Futur → conditionnel présent : ici il n'exprime aucun doute, seulement l'avenir."},
         {q:"« Tu comptes quoi ? » → Elle a demandé ___ il comptait.", opts:["ce qu'","qu'est-ce qu'"], ok:0,
          fb:"<i>Quoi</i> et <i>qu'est-ce que</i> deviennent tous les deux <b>ce que</b>."},
         {q:"« Je viendrais si je pouvais. » → Elle a dit qu'elle ___ si elle pouvait.", opts:["serait venue","viendrait"], ok:1,
          fb:"Le conditionnel est déjà en arrière : il ne recule pas."},
       ]},

      {t:'revoir', h:"À retenir",
       p:"Verbe introducteur au passé, et tout recule : <b>présent → imparfait · passé composé → plus-que-parfait · futur → conditionnel · va + infinitif → allait + infinitif</b>. Ne bougent pas : imparfait, conditionnel, subjonctif. Changent aussi : les personnes, les possessifs, et <b>demain → le lendemain</b>."},
    ]
  },

  t3cr: {
    eye:'Mini-leçon', tit:"Écrire un compte rendu qui sert à quelque chose",
    blocs:[
      {t:'texte', h:"À quoi il sert, et à qui",
       p:"Un compte rendu n'est pas un souvenir de la rencontre : c'est un <b>outil</b>. Il sert d'abord à celui qui n'était pas là, qui doit pouvoir travailler dès le lendemain sans appeler personne. Il sert ensuite à ceux qui étaient là, quand ils ne se rappellent plus qui devait faire quoi. Et il sert la semaine suivante, quand quelqu'un dit « on n'avait pas décidé ça ».",
       note:"Une page. Pas deux. Un compte rendu de trois pages n'est pas lu, donc il ne sert à rien du tout."},

      {t:'ana', h:"Le cadre, en trois lignes",
       p:"Première section, et la plus courte. Elle permet à l'absent de savoir tout de suite si une décision a été prise sans lui.",
       mots:[['Ce qu\'on écrit','la date, l\'heure de début et de fin, qui était là, qui manquait'],['Exemple','« Rencontre de l\'équipe 3, mardi de 19 h 05 à 19 h 35. Présents : Youssouf, Miguel et moi. »'],['Ce qu\'on n\'écrit pas','pourquoi la personne était absente',true]],
       say:"Rencontre de l'équipe 3, mardi de dix-neuf heures cinq à dix-neuf heures trente-cinq.",
       note:"L'heure de fin n'est pas décorative : une rencontre de trente minutes et une rencontre de deux heures ne produisent pas le même genre de décisions."},

      {t:'ana', h:"Les positions, une phrase chacune",
       p:"Deuxième section. Chaque proposition est rapportée en une phrase, au discours indirect passé, avec le nom de qui l'a portée.",
       mots:[['On écrit','« Youssouf a proposé que nous descendions les deux rues samedi. »'],['On n\'écrit pas','« Youssouf : Ma proposition est simple, samedi matin on descend… »'],['Le principe','on dit ce qui a été soutenu, on ne transcrit pas',true]],
       say:"Youssouf a proposé que nous descendions les deux rues samedi matin.",
       note:"Le nom devant chaque position n'est pas une formalité : c'est ce qui permet à l'absent de savoir à qui parler s'il n'est pas d'accord."},

      {t:'ana', h:"Le désaccord, écrit et réglé",
       p:"Troisième section, celle que tout le monde escamote. On nomme l'écart, puis on dit comment il s'est refermé.",
       mots:[['On écrit','« Le désaccord ne portait pas sur le fait d\'y aller, mais sur ce que nous allions noter. »'],['Puis','« Miguel a proposé de noter l\'ombre ; Youssouf a accepté de l\'ajouter. »'],['Ce qu\'on ne fait pas','écrire « tout le monde était d\'accord » quand ce n\'était pas le cas',true]],
       say:"Le désaccord ne portait pas sur le fait d'y aller, mais sur ce que nous allions noter.",
       note:"Un compte rendu qui efface le désaccord se retourne contre son auteur à la rencontre suivante, quand la question revient intacte."},

      {t:'ana', h:"Les décisions et les engagements",
       p:"Deux dernières sections, et ce sont elles qu'on relira. Les décisions sont numérotées ; les engagements portent un nom et une date.",
       mots:[['Une décision','« Nous partons samedi à 10 h, et non à 9 h, parce que l\'ombre à 9 h ne se compare pas. »'],['Un engagement','« Miguel écrit à Perrine avant jeudi. »'],['La règle','sans nom, personne ne le fait ; sans date, tout le monde le fait la dernière semaine',true]],
       say:"Miguel écrit à Perrine avant jeudi. Youssouf apporte deux copies de la carte samedi matin.",
       note:"Une décision se donne toujours avec sa raison : c'est ce qui empêche de la rediscuter deux fois."},

      {t:'labo', h:"La même rencontre, bien ou mal rendue",
       p:"Choisissez une section, puis la version.",
       axes:[
         {id:'s', lbl:'Quelle section ?', opts:[['a','le cadre'],['b','une position'],['c','le désaccord'],['d','un engagement']]},
         {id:'v', lbl:'Quelle version ?', opts:[['1','la version faible'],['2','la version utile']]}],
       out:{
         a1:{w:["On s'est vus mardi soir."], say:"On s'est vus mardi soir.", n:'ni heure, ni présents : l\'absent ne sait rien'},
         a2:{w:["Mardi, 19 h 05 à 19 h 35. Présents : Youssouf, Miguel, moi."], say:"Mardi, de dix-neuf heures cinq à dix-neuf heures trente-cinq. Présents : Youssouf, Miguel et moi.", n:'trois lignes, et tout y est'},
         b1:{w:["On a parlé de la méthode."], say:"On a parlé de la méthode.", n:'aucune position, aucun nom : inutilisable'},
         b2:{w:["Youssouf a proposé de compter les arbres des deux rues."], say:"Youssouf a proposé de compter les arbres des deux rues.", n:'un nom, une phrase, au discours rapporté'},
         c1:{w:["Tout le monde était d'accord."], say:"Tout le monde était d'accord.", n:'faux, et la question reviendra intacte'},
         c2:{w:["Le désaccord portait sur ce qu'on note, pas sur le fait d'y aller."], say:"Le désaccord portait sur ce qu'on note, pas sur le fait d'y aller.", n:'l\'écart est nommé, donc il est réglé'},
         d1:{w:["Il faudrait écrire à Perrine."], say:"Il faudrait écrire à Perrine.", n:'ni nom ni date : personne ne le fera'},
         d2:{w:["Miguel écrit à Perrine avant jeudi."], say:"Miguel écrit à Perrine avant jeudi.", n:'un nom, un verbe, une date'},
       },
       note:"Les versions faibles ne sont pas fausses : elles sont inutilisables. C'est pire, parce que personne ne s'en aperçoit avant la semaine suivante."},

      {t:'ex', h:"Les six sections, dans l'ordre",
       p:"Le plan d'un compte rendu d'une page.",
       rows:[
         ["1. Le cadre","date, heures, présents, absents"],
         ["2. Les positions","une phrase par personne, au discours rapporté"],
         ["3. Le désaccord","ce sur quoi il portait, et comment il s'est réglé"],
         ["4. Les décisions","numérotées, chacune avec sa raison"],
         ["5. À faire","un nom, un verbe, une date par ligne"],
         ["6. La demande à l'absent","ce qu'on attend de lui, et avant quand"],
       ]},

      {t:'piege', h:"Trois pièges du compte rendu",
       rows:[
         ["transcrire le dialogue","rapporter en une phrase par position",
          "Trois pages de répliques ne se lisent pas. Ce n'est pas un procès-verbal de tribunal : c'est une page de travail."],
         ["écrire « on » partout","nommer les personnes",
          "« On a décidé, on devrait, on va vérifier » : à la fin, personne n'a rien à faire. Chaque engagement porte un nom propre."],
         ["l'envoyer trois jours plus tard","le soir même",
          "Une décision qu'un absent apprend le vendredi pour un travail du samedi n'est pas une décision : c'est une nouvelle."],
       ]},

      {t:'check', h:"Est-ce que c'est clair maintenant ?",
       p:"Quatre décisions d'écriture.",
       qs:[
         {q:"Une position d'un coéquipier s'écrit…", opts:["en une phrase rapportée, avec son nom","au mot à mot, entre guillemets"], ok:0,
          fb:"On dit ce qui a été soutenu ; on ne transcrit pas."},
         {q:"Le désaccord, dans un compte rendu…", opts:["s'écrit, avec la façon dont il s'est réglé","s'efface pour garder la bonne entente"], ok:0,
          fb:"Un désaccord effacé revient intact à la rencontre suivante."},
         {q:"Un engagement doit porter…", opts:["un nom et une date","une explication"], ok:0,
          fb:"Sans nom, personne ne le fait ; sans date, tout le monde le fait trop tard."},
         {q:"Le compte rendu part…", opts:["le soir même","avant la rencontre suivante"], ok:0,
          fb:"Le soir même : c'est ce qui permet à l'absent de travailler dès le lendemain."},
       ]},

      {t:'revoir', h:"À retenir",
       p:"Six sections, une page : <b>le cadre · les positions, une phrase et un nom chacune · le désaccord et son règlement · les décisions numérotées avec leur raison · à faire, un nom et une date par ligne · la demande à l'absent</b>. Écrit au discours indirect passé, envoyé le soir même."},
    ]
  },

};
