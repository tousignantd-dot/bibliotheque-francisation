const PLUS = {
  prPhon: {
    eye:'Mini-leçon', tit:"« Un » et « pain »",
    blocs:[
      {t:'texte', h:"Deux sons que beaucoup fondent en un seul",
       p:"« Un » et « pain » ne se prononcent pas pareil. « Brun » et « brin » non plus. Ce sont deux voyelles nasales différentes — et le français du Québec les distingue encore nettement, alors que beaucoup de francophones d'ailleurs les ont fondues.",
       note:"C'est une particularité d'ici, et elle s'entend tous les jours : « un » revient dans presque chaque phrase."},

      {t:'ana', h:"Le son de « un » — lèvres arrondies",
       p:"Les lèvres avancent et s'arrondissent, comme pour siffler. La langue reste basse.",
       mots:[['La forme écrite','{un} · {um}'],['Les lèvres','arrondies, avancées',true],['Comme dans','{un} · brun · lundi']],
       say:"Il y en a un seul, en brun.",
       note:"Autres mots : <em>chacun</em>, <em>aucun</em>, <em>parfum</em>, <em>humble</em>. La liste est courte : ce son n'apparaît que dans une poignée de mots — mais ils sont très fréquents."},

      {t:'ana', h:"Le son de « pain » — lèvres étirées",
       p:"Les lèvres s'écartent sur les côtés, comme pour sourire. La bouche est plus ouverte.",
       mots:[['Les formes écrites','{in} · {ain} · {ein} · {im}'],['Les lèvres','étirées, en sourire',true],['Comme dans','pain · brin · magasin']],
       say:"Le magasin est plein de monde ce matin.",
       note:"Autres mots : <em>linge</em>, <em>certain</em>, <em>plein</em>, <em>important</em>, <em>simple</em>. Beaucoup plus nombreux que ceux de la première famille."},

      {t:'texte', h:"Comment le savoir en lisant",
       p:"Le son de « un » ne s'écrit que <b>un</b> ou <b>um</b>. Tout le reste — <b>in</b>, <b>ain</b>, <b>ein</b>, <b>im</b>, <b>aim</b> — se dit comme « pain ». C'est une des rares règles d'orthographe française sans exception utile.",
       note:"Vous n'avez donc jamais à deviner : la graphie vous dit lequel des deux prononcer."},

      {t:'labo', h:"Écoutez les paires",
       p:"Choisissez une paire et écoutez la différence.",
       axes:[{id:'p', lbl:'Quelle paire ?', opts:[
         ['a','un / pain'],
         ['b','brun / brin'],
         ['c','lundi / linge'],
         ['d','chacun / certain'],
         ['e','aucun / magasin']]}],
       out:{
         a:{w:['{un} — lèvres arrondies'], say:"Il y en a un seul.", n:'un, um › lèvres arrondies'},
         b:{w:['{brun} — lèvres arrondies'], say:"Le modèle brun est en spécial.", n:'brun ≠ brin'},
         c:{w:['{lundi} — lèvres arrondies'], say:"On livre lundi et jeudi.", n:'un › arrondi'},
         d:{w:['{chacun} — lèvres arrondies'], say:"Chacun a sa garantie.", n:'un › arrondi'},
         e:{w:['{aucun} — lèvres arrondies'], say:"Il n'y a aucun modèle en stock.", n:'un › arrondi'},
       },
       note:"Dans les cinq paires, c'est le mot de gauche qui a les lèvres arrondies. Regardez la bouche de la personne qui parle : la différence se voit autant qu'elle s'entend."},

      {t:'ex', h:"Les mots du module",
       p:"Écoutez chacun et répétez-le en exagérant la position des lèvres.",
       rows:[
         ["Il y en a un seul.","un — arrondi"],
         ["Le modèle brun est en spécial.","brun — arrondi"],
         ["On livre lundi et jeudi.","lundi — arrondi"],
         ["Le magasin est plein de monde.","magasin, plein — étirés"],
         ["C'est un point important.","point, important — étirés"],
         ["Chacun a sa garantie.","chacun — arrondi"],
       ]},

      {t:'piege', h:"Deux pièges à connaître",
       rows:[
         ["prononcer « un » comme « in »","« un » a les lèvres arrondies",
          "C'est ce que font beaucoup de francophones d'Europe, et on vous comprendra. Mais ici, la distinction s'entend, et l'adopter aide à mieux <u>comprendre</u> ce qu'on vous dit."],
         ["chercher la règle à l'oreille","c'est la graphie qui décide",
          "<b>un</b> et <b>um</b> d'un côté ; <b>in</b>, <b>ain</b>, <b>ein</b>, <b>im</b> de l'autre. Vous n'avez qu'à regarder comment le mot s'écrit."],
       ]},

      {t:'check', h:"Est-ce que c'est clair maintenant ?",
       p:"Quatre questions rapides.",
       qs:[
         {q:"« Brun » se prononce…", opts:["comme « un »","comme « pain »"], ok:0,
          fb:"La graphie <b>un</b> donne toujours le son arrondi."},
         {q:"« Certain » se prononce…", opts:["comme « un »","comme « pain »"], ok:1,
          fb:"La graphie <b>ain</b> donne le son étiré."},
         {q:"Pour le son de « un », les lèvres sont…", opts:["arrondies","étirées"], ok:0,
          fb:"Arrondies et avancées, comme pour siffler."},
         {q:"Ce qui décide, c'est…", opts:["l'oreille","la façon dont le mot s'écrit"], ok:1,
          fb:"un et um d'un côté, in/ain/ein/im de l'autre."},
       ]},
    ]
  },

  t1adj: {
    eye:'Mini-leçon', tit:"Où mettre l'adjectif",
    blocs:[
      {t:'texte', h:"Après le nom, presque toujours",
       p:"« Une laveuse <b>silencieuse</b> », « un appareil <b>économe</b> », « un modèle <b>récent</b> ». En français, l'adjectif suit le nom dans la grande majorité des cas. C'est l'inverse de plusieurs langues, et c'est la règle par défaut.",
       note:"Si vous hésitez, mettez l'adjectif après. Vous aurez raison neuf fois sur dix."},

      {t:'ana', h:"La petite famille qui précède",
       p:"Une dizaine d'adjectifs très courants se placent avant le nom.",
       mots:[['La taille','{grand} · petit · gros'],['Le jugement','beau · bon · joli',true],['L\'âge et le rang','nouveau · vieux · jeune · premier · dernier']],
       say:"C'est un petit réfrigérateur, le dernier modèle.",
       note:"Ils sont courts, très fréquents, et ils s'apprennent comme une liste. En dehors de ceux-là, l'adjectif suit."},

      {t:'ana', h:"L'accord : genre et nombre",
       p:"L'adjectif prend la forme du nom qu'il décrit.",
       mots:[['Masculin','un appareil silencieu{x}'],['Féminin','une laveuse silencieu{se}',true],['Pluriel','des modèles récent{s}']],
       say:"Une laveuse silencieuse et des modèles récents.",
       note:"Quelques féminins irréguliers à connaître : nouveau › <b>nouvelle</b>, beau › <b>belle</b>, vieux › <b>vieille</b>, blanc › <b>blanche</b>, complet › <b>complète</b>."},

      {t:'texte', h:"Les adjectifs de mesure",
       p:"« Un local <b>large</b> d'un mètre », « un appareil <b>haut</b> de cent quarante-cinq centimètres ». Ils suivent toujours le nom et s'accordent avec lui, jamais avec le chiffre.",
       note:"À l'oral, on dit plus souvent « un local d'un mètre de large » — les deux formes sont correctes."},

      {t:'labo', h:"Avant ou après ?",
       p:"Choisissez un adjectif et voyez où il se place.",
       axes:[{id:'p', lbl:'Quel adjectif ?', opts:[
         ['a','silencieux'],
         ['b','petit'],
         ['c','économe'],
         ['d','dernier'],
         ['e','récent']]}],
       out:{
         a:{w:['une laveuse {silencieuse}'], say:"C'est une laveuse silencieuse.", n:'après le nom — règle par défaut'},
         b:{w:['un {petit} réfrigérateur'], say:"Je cherche un petit réfrigérateur.", n:'avant — il fait partie de la petite famille'},
         c:{w:['un appareil {économe}'], say:"C'est un appareil économe en eau.", n:'après le nom'},
         d:{w:['le {dernier} modèle'], say:"C'est le dernier modèle.", n:'avant — rang'},
         e:{w:['des modèles {récents}'], say:"Ce sont des modèles récents.", n:'après, et accord au pluriel'},
       },
       note:"Deux sur cinq précèdent : ce sont justement ceux de la liste. Tous les autres suivent."},

      {t:'ex', h:"Décrire un appareil",
       p:"Écoutez chaque description.",
       rows:[
         ["C'est une laveuse silencieuse.","après le nom, féminin"],
         ["C'est un appareil économe en eau.","après le nom"],
         ["Ce sont des modèles récents.","après, accord au pluriel"],
         ["Je cherche un petit réfrigérateur.","avant le nom"],
         ["C'est le dernier modèle.","avant le nom"],
         ["Une garantie complète d'un an.","après, féminin irrégulier"],
       ]},

      {t:'piege', h:"Trois pièges à connaître",
       rows:[
         ["placer tous les adjectifs avant le nom","« une laveuse silencieuse », pas « une silencieuse laveuse »",
          "C'est le réflexe des langues germaniques et de plusieurs autres. En français, l'adjectif suit — sauf la petite liste."],
         ["oublier l'accord au féminin","silencieux › silencieuse · complet › complète",
          "Le féminin change souvent la fin du mot, pas seulement l'orthographe. Ça s'entend."],
         ["accorder avec le chiffre","« un local large d'un mètre »",
          "L'adjectif s'accorde avec le nom qu'il décrit — le local — jamais avec la mesure."],
       ]},

      {t:'check', h:"Est-ce que c'est clair maintenant ?",
       p:"Quatre questions rapides.",
       qs:[
         {q:"L'adjectif se place le plus souvent…", opts:["avant le nom","après le nom"], ok:1,
          fb:"C'est la règle par défaut en français."},
         {q:"« petit » se place…", opts:["avant","après"], ok:0,
          fb:"Il fait partie de la petite famille qui précède."},
         {q:"Le féminin de « complet » est…", opts:["complète","completé"], ok:0,
          fb:"complet › complète."},
         {q:"Dans « un local large d'un mètre », l'adjectif s'accorde avec…", opts:["le mètre","le local"], ok:1,
          fb:"Toujours avec le nom qu'il décrit."},
       ]},
    ]
  },

  t1demo: {
    eye:'Mini-leçon', tit:"Ce modèle-ci, celui-là",
    blocs:[
      {t:'texte', h:"Deux appareils côte à côte",
       p:"Devant deux modèles presque identiques, il faut pouvoir désigner l'un plutôt que l'autre — sans les toucher, sans répéter leur nom à chaque phrase. Le français a deux outils pour ça, et il ne faut pas les mélanger.",
       note:"L'un <b>accompagne</b> le nom, l'autre le <b>remplace</b>. Toute la leçon tient là."},

      {t:'ana', h:"ce, cet, cette, ces — ils accompagnent",
       p:"Ils se mettent devant le nom, comme un article.",
       mots:[['Masculin','{ce} modèle'],['Devant une voyelle','{cet} appareil',true],['Féminin et pluriel','cette laveuse · ces deux-là']],
       say:"Ce modèle-ci est plus petit que celui-là.",
       note:"<b>cet</b> ne s'emploie que devant une voyelle ou un h muet : <em>cet</em> appareil, <em>cet</em> écran, <em>cet</em> homme. Devant une consonne, c'est <b>ce</b>."},

      {t:'ana', h:"celui, celle, ceux, celles — ils remplacent",
       p:"Ils prennent la place du nom, qui disparaît de la phrase.",
       mots:[['Masculin','{celui} de gauche'],['Féminin','celle-là',true],['Pluriel','ceux qui consomment le moins']],
       say:"Prenez celui de gauche, il entre partout.",
       note:"Comme dans le module des déplacements : jamais tout seul. Toujours suivi de <b>-là</b>, <b>-ci</b>, <b>qui</b>, <b>que</b> ou <b>de</b>."},

      {t:'ana', h:"-ci et -là",
       p:"Pour distinguer deux choses présentes en même temps.",
       mots:[['Le plus proche','ce modèle-{ci}'],['Le plus éloigné','ce modèle-{là}',true],['À l\'oral','-là l\'emporte souvent partout']],
       say:"Quelle est la différence entre ce modèle-ci et celui-là ?",
       note:"Dans la conversation courante, beaucoup de gens emploient <b>-là</b> pour les deux : « celui-là » et « celui-là, à côté ». Ce n'est pas une faute."},

      {t:'texte', h:"Reprendre autrement",
       p:"Une troisième façon d'éviter la répétition : changer de nom. « La laveuse » devient « <b>l'appareil</b> », « <b>le modèle</b> », « <b>la machine</b> ». C'est ce que fait le vendeur du module, et c'est très naturel à l'écrit.",
       note:"Trois mots pour la même chose : appareil (général), modèle (une version précise), machine (familier). Les alterner rend un texte beaucoup plus léger."},

      {t:'labo', h:"Accompagner ou remplacer ?",
       p:"Choisissez une phrase et voyez lequel employer.",
       axes:[{id:'p', lbl:'Quelle phrase ?', opts:[
         ['a','___ modèle-ci et celui-là'],
         ['b','___ appareil est plus économe'],
         ['c','___ laveuse fait 68 cm'],
         ['d','Prenez ___ de gauche'],
         ['e','___ est trop large']]}],
       out:{
         a:{w:['{ce} modèle-ci'], say:"Quelle est la différence entre ce modèle-ci et celui-là ?", n:'accompagne le nom « modèle »'},
         b:{w:['{cet} appareil'], say:"Cet appareil est plus économe.", n:'devant une voyelle › cet'},
         c:{w:['{cette} laveuse'], say:"Cette laveuse fait soixante-huit centimètres.", n:'féminin › cette'},
         d:{w:['Prenez {celui} de gauche'], say:"Prenez celui de gauche.", n:'remplace le nom'},
         e:{w:['{Celle-là} est trop large'], say:"Celle-là est trop large pour votre local.", n:'remplace, avec -là'},
       },
       note:"Le test : le nom est-il écrit juste après ? Si oui › ce, cet, cette. Si non › celui, celle."},

      {t:'ex', h:"Les phrases du module",
       p:"Écoutez chacune et repérez lequel des deux est employé.",
       rows:[
         ["Quelle est la différence entre ce modèle-ci et celui-là ?","les deux dans la même phrase"],
         ["Cet appareil est plus économe.","accompagne"],
         ["Cette laveuse fait soixante-huit centimètres.","accompagne"],
         ["Prenez celui de gauche.","remplace"],
         ["Celle-là est trop large.","remplace"],
         ["Ces deux modèles se ressemblent beaucoup.","accompagne, au pluriel"],
       ]},

      {t:'piege', h:"Trois pièges à connaître",
       rows:[
         ["mélanger les deux","« celui modèle » n'existe pas",
          "Soit le nom est là et on emploie <b>ce</b>, soit il disparaît et on emploie <b>celui</b>. Jamais les deux ensemble."],
         ["employer ce devant une voyelle","« cet appareil », pas « ce appareil »",
          "<b>cet</b> existe précisément pour éviter la rencontre de deux voyelles."],
         ["laisser celui tout seul","« celui-là », « celui de gauche », « celui qui »",
          "Un pronom démonstratif appelle toujours une suite."],
       ]},

      {t:'check', h:"Est-ce que c'est clair maintenant ?",
       p:"Quatre questions rapides.",
       qs:[
         {q:"Devant « appareil », on emploie…", opts:["ce","cet"], ok:1,
          fb:"Devant une voyelle, c'est <b>cet</b>."},
         {q:"« ___ de gauche est moins cher » demande…", opts:["Ce","Celui"], ok:1,
          fb:"Le nom n'est pas là : il faut le pronom."},
         {q:"« celui modèle » est…", opts:["correct","impossible"], ok:1,
          fb:"<b>celui</b> remplace le nom, il ne l'accompagne jamais."},
         {q:"-ci désigne…", opts:["le plus proche","le plus éloigné"], ok:0,
          fb:"-ci le proche, -là l'éloigné."},
       ]},
    ]
  },

  t2garantie: {
    eye:'Mini-leçon', tit:"Ce que couvre une garantie",
    blocs:[
      {t:'texte', h:"Une promesse limitée",
       p:"Une garantie n'est pas une assurance tous risques. C'est la promesse du fabricant de réparer <b>ce qui vient de l'usine</b>, pendant une période donnée. Ce que vous faites à l'appareil, lui, n'est jamais couvert.",
       note:"Cette distinction est la source de presque tous les malentendus au comptoir de service."},

      {t:'ana', h:"Ce qui est couvert : le défaut de fabrication",
       p:"Une pièce qui brise toute seule, un programme qui se dérègle, un moteur qui lâche.",
       mots:[['La cause','un {défaut de fabrication}'],['La durée','un an, en général',true],['Ce qui est payé','pièces et main-d\'œuvre']],
       say:"La garantie couvre les défauts de fabrication, pas les accidents.",
       note:"« Pièces et main-d'œuvre » veut dire que ni la pièce ni le travail du technicien ne vous sont facturés."},

      {t:'ana', h:"Ce qui n'est pas couvert",
       p:"Les accidents, la mauvaise utilisation, l'usure normale, et souvent le déplacement.",
       mots:[['Un accident','l\'appareil {tombe}'],['Une mauvaise utilisation','trois fois trop de savon',true],['Le déplacement','souvent facturé à part']],
       say:"Si c'est vous qui l'abîmez, ce n'est pas couvert.",
       note:"Le déplacement du technicien — souvent 90 $ — est le poste le plus souvent oublié. Certaines garanties prolongées le couvrent, la garantie de base rarement."},

      {t:'texte', h:"La garantie prolongée : quand ça vaut la peine",
       p:"Elle ajoute des années et couvre parfois le déplacement. Elle vaut surtout pour les appareils <b>chers à réparer</b> — réfrigérateurs, laveuses — et beaucoup moins pour les petits appareils, qu'on remplace au lieu de réparer.",
       note:"Le calcul simple : la garantie prolongée coûte-t-elle plus ou moins qu'une réparation probable ? Au-delà du tiers du prix de l'appareil, c'est rarement avantageux."},

      {t:'ana', h:"Les durées qu'on rencontre",
       p:"Elles varient selon la pièce, pas seulement selon l'appareil.",
       mots:[['L\'appareil complet','{1 an}, le plus souvent'],['Une pièce coûteuse','{5 ans} sur le compresseur',true],['La garantie prolongée','3 ans de plus, en option']],
       say:"Un an complet, cinq ans sur le compresseur.",
       note:"Le compresseur d'un réfrigérateur est la pièce la plus chère : c'est pour cela qu'il est garanti plus longtemps que le reste."},

      {t:'labo', h:"Couvert ou pas ?",
       p:"Choisissez une situation.",
       axes:[{id:'p', lbl:'Quelle situation ?', opts:[
         ['a','le moteur brise après huit mois'],
         ['b',"l'appareil tombe pendant le déménagement"],
         ['c','trois fois trop de savon'],
         ['d','panne après quatorze mois'],
         ['e','le déplacement du technicien']]}],
       out:{
         a:{w:['{couvert} — défaut de fabrication'], say:"La garantie couvre les défauts de fabrication.", n:'dans la période, sans faute de l\'usager'},
         b:{w:['{pas couvert} — accident'], say:"Si c'est vous qui l'abîmez, ce n'est pas couvert.", n:'la garantie n\'est pas une assurance'},
         c:{w:['{pas couvert} — mauvaise utilisation'], say:"Ça, ce n'est pas couvert.", n:'le mode d\'emploi donne la dose'},
         d:{w:['{pas couvert} — hors période'], say:"La garantie est d'un an.", n:'deux mois de trop'},
         e:{w:['{selon} la garantie choisie'], say:"Elle couvre aussi le déplacement du technicien.", n:'la prolongée le couvre, la base rarement'},
       },
       note:"Quatre situations sur cinq ne sont pas couvertes. C'est le rapport habituel — et c'est pourquoi il faut lire avant d'acheter, pas après."},

      {t:'ex', h:"Les phrases du module",
       p:"Écoutez chacune.",
       rows:[
         ["Un an, pièces et main-d'œuvre.","ce qui est couvert"],
         ["Si l'appareil brise, on répare sans frais.","ce qui est couvert"],
         ["La garantie couvre les défauts de fabrication, pas les accidents.","la distinction centrale"],
         ["Cent vingt dollars pour trois ans de plus.","la garantie prolongée"],
         ["Elle couvre aussi le déplacement du technicien.","ce qu'ajoute la prolongée"],
         ["Un an complet, cinq ans sur le compresseur.","des durées différentes selon la pièce"],
       ]},

      {t:'piege', h:"Trois pièges à connaître",
       rows:[
         ["croire que tout est couvert","la garantie n'est pas une assurance",
          "Elle couvre ce qui vient de l'usine. Un appareil tombé, mouillé ou mal employé ne l'est pas."],
         ["oublier le déplacement","souvent 90 $, même sous garantie",
          "La pièce et le travail sont gratuits, mais pas toujours le fait de venir chez vous. À demander avant d'acheter."],
         ["ne pas garder la facture","sans preuve d'achat, pas de garantie",
          "La date d'achat est ce qui déclenche la période. Photographiez la facture le jour même."],
       ]},

      {t:'check', h:"Est-ce que c'est clair maintenant ?",
       p:"Quatre questions rapides.",
       qs:[
         {q:"La garantie couvre…", opts:["les accidents","les défauts de fabrication"], ok:1,
          fb:"Ce qui vient de l'usine, pas ce qu'on fait à l'appareil."},
         {q:"« Pièces et main-d'œuvre » veut dire…", opts:["la pièce et le travail sont payés","seulement la pièce"], ok:0,
          fb:"Ni l'une ni l'autre ne vous est facturée."},
         {q:"Le déplacement du technicien est…", opts:["toujours gratuit","souvent facturé à part"], ok:1,
          fb:"À demander avant d'acheter."},
         {q:"Sans facture…", opts:["la garantie s'applique quand même","il n'y a pas de garantie"], ok:1,
          fb:"La date d'achat est ce qui déclenche la période."},
       ]},
    ]
  },

  t2futur: {
    eye:'Mini-leçon', tit:"Quand ça va arriver",
    blocs:[
      {t:'texte', h:"Deux façons de parler de la suite",
       p:"« Ils <b>vont livrer</b> jeudi. » « On vous <b>appellera</b> la veille. » Les deux parlent du futur. La première est la forme de la conversation, la seconde celle des engagements — et c'est celle que le magasin emploie.",
       note:"Les deux sont correctes presque partout. Vous n'avez pas à choisir la bonne : vous devez surtout comprendre les deux."},

      {t:'ana', h:"Le futur proche : aller + infinitif",
       p:"Pour ce qui est décidé, prévu, tout proche.",
       mots:[['La forme','aller + {infinitif}'],['Exemple','ils {vont livrer} jeudi',true],['Où','partout, à l\'oral']],
       say:"Ils vont livrer jeudi prochain.",
       note:"C'est la forme la plus employée dans la conversation courante. Elle se construit avec un verbe que vous connaissez déjà : <em>aller</em>."},

      {t:'ana', h:"Le futur simple : une seule terminaison",
       p:"L'infinitif, suivi de -ai, -as, -a, -ons, -ez, -ont.",
       mots:[['La base','l\'{infinitif}'],['Les terminaisons','-ai -as -a -ons -ez -ont',true],['Exemple','on vous {appellera}']],
       say:"On vous appellera la veille.",
       note:"Les verbes en <b>-re</b> perdent leur e : prendre › je prendr<b>ai</b>. C'est la seule irrégularité de forme pour les verbes réguliers."},

      {t:'ana', h:"Cinq irréguliers à connaître",
       p:"Ils ne se forment pas sur l'infinitif, mais les terminaisons ne changent pas.",
       mots:[['être · avoir','je {serai} · j\'{aurai}'],['aller · faire','j\'{irai} · je {ferai}',true],['venir','je {viendrai}']],
       say:"La livraison sera gratuite et le technicien viendra l'après-midi.",
       note:"Ces cinq-là couvrent la majorité des phrases au futur. Les apprendre comme une liste est plus rapide que de chercher une règle."},

      {t:'texte', h:"Lequel employer, et quand",
       p:"Dans un magasin, on vous parlera au <b>futur simple</b> : « on vous appellera », « la livraison sera gratuite », « le technicien viendra ». Vous pouvez répondre au <b>futur proche</b> — « je vais prendre l'installation » — sans que personne n'y trouve à redire.",
       note:"Ce qui compte, c'est de comprendre les engagements qu'on vous prend. Les produire vient ensuite."},

      {t:'labo', h:"Futur proche ou futur simple ?",
       p:"Choisissez une phrase du module.",
       axes:[{id:'p', lbl:'Quelle phrase ?', opts:[
         ['a','ils livrent jeudi'],
         ['b',"je prends l'installation"],
         ['c','on vous appelle la veille'],
         ['d',"le technicien vient l'après-midi"],
         ['e','la livraison est gratuite']]}],
       out:{
         a:{w:['Ils {vont livrer} jeudi.'], say:"Ils vont livrer jeudi prochain.", n:'futur proche — décidé, tout proche'},
         b:{w:['Je {vais prendre} l\'installation.'], say:"Je vais prendre l'installation.", n:'futur proche — une décision'},
         c:{w:['On vous {appellera} la veille.'], say:"On vous appellera la veille.", n:'futur simple — un engagement du magasin'},
         d:{w:['Le technicien {viendra} l\'après-midi.'], say:"Le technicien viendra l'après-midi.", n:'futur simple, verbe irrégulier'},
         e:{w:['La livraison {sera} gratuite.'], say:"La livraison sera gratuite au-dessus de mille dollars.", n:'futur simple, être'},
       },
       note:"Les trois dernières viennent du magasin, les deux premières de la cliente. Ce n'est pas un hasard : l'engagement se dit au futur simple."},

      {t:'ex', h:"Les phrases du module",
       p:"Écoutez chacune et repérez la forme.",
       rows:[
         ["Ils vont livrer jeudi prochain.","futur proche"],
         ["Je vais prendre l'installation.","futur proche"],
         ["On vous appellera la veille.","futur simple"],
         ["Le technicien viendra l'après-midi.","futur simple, irrégulier"],
         ["La livraison sera gratuite au-dessus de mille dollars.","futur simple, être"],
         ["Il vous appellera en partant du magasin.","futur simple"],
       ]},

      {t:'piege', h:"Trois pièges à connaître",
       rows:[
         ["oublier le double l de « appellera »","appeler › j'appellerai",
          "Quelques verbes doublent leur consonne au futur : appeler, jeter. C'est une petite liste, pas une règle générale."],
         ["former le futur sur autre chose que l'infinitif","livrer › je livrerai",
          "Pour les verbes réguliers, la base est l'infinitif entier. On ajoute simplement la terminaison."],
         ["croire qu'il faut choisir","les deux formes sont correctes",
          "Employez celle que vous maîtrisez. Ce qui compte, c'est de comprendre les deux."],
       ]},

      {t:'check', h:"Est-ce que c'est clair maintenant ?",
       p:"Quatre questions rapides.",
       qs:[
         {q:"« Ils vont livrer jeudi » est…", opts:["au futur proche","au futur simple"], ok:0,
          fb:"aller + infinitif : c'est le futur proche."},
         {q:"Le futur simple se forme sur…", opts:["l'infinitif","le participe passé"], ok:0,
          fb:"L'infinitif, plus la terminaison."},
         {q:"Le futur de « venir » est…", opts:["je venirai","je viendrai"], ok:1,
          fb:"C'est un des cinq irréguliers à connaître."},
         {q:"Dans un magasin, les engagements se disent…", opts:["au futur simple","au futur proche"], ok:0,
          fb:"« On vous appellera », « la livraison sera gratuite »."},
       ]},
    ]
  },

  t2paiement: {
    eye:'Mini-leçon', tit:"Le prix affiché n'est pas le total",
    blocs:[
      {t:'texte', h:"Ce qui s'ajoute à la caisse",
       p:"Un appareil affiché à 800 $ ne coûte pas 800 $. Les <b>taxes</b> s'ajoutent — environ 15 % au Québec — et il faut souvent compter la livraison, l'installation, la reprise de l'ancien appareil et parfois la garantie prolongée.",
       note:"L'écart entre le prix affiché et le total réel dépasse fréquemment 200 $ sur un gros appareil. Le calculer avant évite une mauvaise surprise."},

      {t:'ana', h:"Les taxes",
       p:"Deux taxes s'additionnent, et elles ne sont jamais incluses dans le prix affiché.",
       mots:[['Total','environ {15 %}'],['Sur 800 $','environ {920 $}',true],['Le repère','ajoutez un sixième, en gros']],
       say:"Le prix affiché ne comprend pas les taxes.",
       note:"Un calcul mental commode : ajouter 15 %, c'est ajouter le dixième du prix, puis la moitié de ce dixième. 800 › 80 + 40 = 120."},

      {t:'ana', h:"La livraison et l'installation",
       p:"Deux services distincts, deux prix distincts. C'est la confusion la plus coûteuse du module.",
       mots:[['La livraison','on {monte} l\'appareil'],['L\'installation','on le {branche}',true],['Le prix','60 $ et 40 $ dans ce module']],
       say:"Les livreurs la montent, mais ils ne la branchent pas.",
       note:"Beaucoup de gens découvrent le jour de la livraison que l'appareil est dans la pièce, mais pas raccordé. Demandez au moment de l'achat."},

      {t:'ana', h:"Les versements",
       p:"Payer en plusieurs fois, souvent sans frais.",
       mots:[['La formule','{12 versements} sans intérêt'],['Ce que ça veut dire','le prix divisé en douze',true],['La condition','payer à temps chaque mois']],
       say:"Douze versements sans intérêt, si vous préférez.",
       note:"« Sans intérêt » tient tant qu'on paie à temps. Un retard fait souvent tomber la gratuité et applique un taux élevé sur tout le solde — c'est écrit en petit dans le contrat."},

      {t:'texte', h:"Le bon de livraison",
       p:"Le papier qui dit <b>quoi</b>, <b>quand</b>, et <b>ce qui est inclus</b>. Tout ce qui n'y est pas écrit n'arrivera pas : la reprise de l'ancien appareil, notamment, se perd très souvent parce qu'elle n'a pas été notée.",
       note:"Relisez-le avant de signer, et gardez-en une copie. C'est votre seule preuve de ce qui a été promis."},

      {t:'labo', h:"Combien ça coûte vraiment ?",
       p:"Choisissez un poste et voyez ce qu'il ajoute.",
       axes:[{id:'p', lbl:'Quel poste ?', opts:[
         ['a','les taxes sur 800 $'],
         ['b','la livraison'],
         ["c",'l\'installation'],
         ['d','la garantie prolongée'],
         ['e','le déplacement du technicien']]}],
       out:{
         a:{w:['environ {120 $}'], say:"Le prix affiché ne comprend pas les taxes.", n:'≈ 15 %, jamais inclus'},
         b:{w:['{60 $} — ou gratuite'], say:"Soixante dollars, ou gratuite au-dessus de mille dollars.", n:'souvent gratuite au-dessus d\'un montant'},
         c:{w:['{40 $} — service à part'], say:"L'installation est un service à part, quarante dollars.", n:'la livraison ne l\'inclut pas'},
         d:{w:['{120 $} pour trois ans'], say:"Cent vingt dollars pour trois ans de plus.", n:'facultative'},
         e:{w:['environ {90 $}'], say:"Le déplacement du technicien coûte quatre-vingt-dix dollars.", n:'sauf si la prolongée le couvre'},
       },
       note:"Sur un appareil à 800 $, ces postes peuvent porter le total à plus de 1 100 $. Le savoir avant change la décision."},

      {t:'ex', h:"Les phrases du module",
       p:"Écoutez chacune.",
       rows:[
         ["Comptant, débit, crédit.","les modes de paiement"],
         ["Douze versements sans intérêt.","payer en plusieurs fois"],
         ["Soixante dollars, ou gratuite au-dessus de mille dollars.","la livraison"],
         ["L'installation est un service à part, quarante dollars.","à ne pas confondre"],
         ["Les livreurs la montent, mais ils ne la branchent pas.","la phrase à retenir"],
         ["Si c'est noté sur le bon de livraison, oui.","tout ce qui n'est pas écrit n'arrive pas"],
       ]},

      {t:'piege', h:"Trois pièges à connaître",
       rows:[
         ["calculer avec le prix affiché","ajoutez 15 % de taxes",
          "Le prix affiché n'est jamais le total au Québec. C'est différent de beaucoup de pays, où la taxe est incluse."],
         ["croire que la livraison inclut l'installation","monter n'est pas brancher",
          "Deux services, deux prix. À demander explicitement au moment de l'achat."],
         ["ne rien faire écrire","tout ce qui n'est pas sur le bon n'arrivera pas",
          "La reprise de l'ancien appareil est ce qui se perd le plus souvent. Faites-la noter."],
       ]},

      {t:'check', h:"Est-ce que c'est clair maintenant ?",
       p:"Quatre questions rapides.",
       qs:[
         {q:"Un appareil affiché à 800 $ coûte, taxes comprises…", opts:["environ 920 $","800 $"], ok:0,
          fb:"Les taxes ajoutent environ 15 %."},
         {q:"Les livreurs…", opts:["branchent l'appareil","le montent seulement"], ok:1,
          fb:"L'installation est un service à part."},
         {q:"« Douze versements sans intérêt » suppose…", opts:["rien de particulier","de payer à temps chaque mois"], ok:1,
          fb:"Un retard fait souvent tomber la gratuité."},
         {q:"La reprise de l'ancien appareil…", opts:["est automatique","doit être notée sur le bon"], ok:1,
          fb:"Tout ce qui n'est pas écrit n'arrivera pas."},
       ]},
    ]
  },

  t3mode: {
    eye:'Mini-leçon', tit:"Quatre pages sur quarante",
    blocs:[
      {t:'texte', h:"Pourquoi c'est si épais",
       p:"Un mode d'emploi vendu au Canada contient le même texte en <b>français</b>, en <b>anglais</b>, souvent en <b>espagnol</b>. Sur quarante pages, le tiers vous concerne. Et dans ce tiers, quatre pages suffisent.",
       note:"Trouver la section française prend dix secondes : elle est signalée par un onglet, une couleur ou une page de garde."},

      {t:'ana', h:"1 · L'installation",
       p:"Ce qu'il faut enlever et vérifier avant de brancher.",
       mots:[['À enlever','les {boulons de transport}'],['À vérifier','que l\'appareil est {de niveau}',true],['À raccorder','l\'eau, le renvoi, la prise']],
       say:"Il faut enlever les quatre boulons de transport.",
       note:"Les boulons bloquent le tambour pendant le transport. Oubliés, ils font sauter la machine au premier essorage — et le dommage n'est pas couvert par la garantie."},

      {t:'ana', h:"2 · La première utilisation",
       p:"Presque toujours un cycle à vide, sans linge.",
       mots:[['Ce qu\'on fait','un {cycle à vide}'],['Pourquoi','enlever ce qui reste de l\'usine',true],['Où c\'est écrit','deux lignes, page trois']],
       say:"On fait un cycle à vide, sans linge, avant tout.",
       note:"Deux lignes que personne ne lit — et qui évitent que la première brassée sorte tachée."},

      {t:'ana', h:"3 · Les avertissements",
       p:"Ce qui peut blesser ou briser l'appareil. Séparés du reste, souvent avec un triangle.",
       mots:[['Le signe','un {triangle}'],['La forme','« Ne pas… »',true],['La place','encadrés, avant le mode d\'emploi']],
       say:"Ne pas laver de vêtements imbibés de solvant.",
       note:"Sur un appareil qu'on ne connaît pas, c'est le premier bloc à lire, pas le dernier."},

      {t:'ana', h:"4 · Le tableau des problèmes",
       p:"À la fin. Deux colonnes : le problème à gauche, quoi vérifier à droite.",
       mots:[['Colonne 1','le {problème}'],['Colonne 2','quoi {vérifier}',true],['Ce que ça vaut','environ 90 $ par appel évité']],
       say:"Neuf appels sur dix se règlent avec ce tableau.",
       note:"C'est la page la plus rentable de tout le livret, et la moins lue. Cornez-la le jour de la livraison."},

      {t:'labo', h:"Dans quelle partie ?",
       p:"Choisissez une phrase et voyez où elle se trouve.",
       axes:[{id:'p', lbl:'Quelle phrase ?', opts:[
         ['a','Retirer les quatre boulons.'],
         ['b',"Ajuster les pieds pour le niveau."],
         ['c','Effectuer un cycle à vide.'],
         ['d','Ne pas laver de vêtements imbibés de solvant.'],
         ['e',"L'appareil vibre : vérifier trois choses."]]}],
       out:{
         a:{w:["l'{installation}"], say:"Il faut enlever les quatre boulons de transport.", n:'avant de brancher'},
         b:{w:["l'{installation}"], say:"Vérifiez que l'appareil est de niveau.", n:'avant de brancher'},
         c:{w:['la {première utilisation}'], say:"On fait un cycle à vide, sans linge, avant tout.", n:'page trois, deux lignes'},
         d:{w:['les {avertissements}'], say:"Ne pas laver de vêtements imbibés de solvant.", n:'encadrés, avec un triangle'},
         e:{w:['le {tableau des problèmes}'], say:"Neuf appels sur dix se règlent avec ce tableau.", n:'à la fin, deux colonnes'},
       },
       note:"Quatre parties, cinq phrases : c'est la structure complète du livret d'un électroménager."},

      {t:'ex', h:"Les phrases du module",
       p:"Écoutez chacune.",
       rows:[
         ["Il faut enlever les quatre boulons de transport.","installation"],
         ["Vérifiez que l'appareil est de niveau.","installation"],
         ["On fait un cycle à vide, sans linge, avant tout.","première utilisation"],
         ["Neuf appels sur dix se règlent avec ce tableau.","le tableau des problèmes"],
         ["Elle vibre beaucoup à l'essorage.","un problème du tableau"],
         ["Deux serviettes se collent d'un côté et le tambour tourne de travers.","la cause, et la solution"],
       ]},

      {t:'piege', h:"Trois pièges à connaître",
       rows:[
         ["jeter le livret avec l'emballage","le tableau des problèmes vaut 90 $ par appel",
          "Les livreurs repartent avec la boîte. Sortez le livret avant, et rangez-le près de l'appareil."],
         ["laisser les boulons de transport","la machine saute, et ce n'est pas couvert",
          "C'est le dommage le plus fréquent d'une première installation, et la garantie ne le couvre pas : c'est une mauvaise utilisation."],
         ["appeler le service avant de vérifier","trois choses à regarder d'abord",
          "Les boulons, le niveau, la répartition du linge. Cinq minutes contre quatre-vingt-dix dollars."],
       ]},

      {t:'check', h:"Est-ce que c'est clair maintenant ?",
       p:"Quatre questions rapides.",
       qs:[
         {q:"Sur quarante pages, combien comptent vraiment ?", opts:["quatre","vingt"], ok:0,
          fb:"Le reste, ce sont les autres langues et les détails."},
         {q:"Les boulons de transport…", opts:["se laissent en place","s'enlèvent avant le premier lavage"], ok:1,
          fb:"Sinon la machine saute, et ce n'est pas couvert."},
         {q:"Le tableau des problèmes se trouve…", opts:["au début","à la fin"], ok:1,
          fb:"Deux colonnes : le problème, quoi vérifier."},
         {q:"Avant d'appeler le service, on vérifie…", opts:["rien, on appelle","les trois choses du tableau"], ok:1,
          fb:"Neuf appels sur dix s'y règlent."},
       ]},
    ]
  },
};
