const PLUS = {

  prGraphie: {
    eye:'Mini-leçon', tit:"Quand les lettres mentent : ch, x, sh",
    blocs:[
      {t:'texte', h:"Trois cas où l'écriture trompe l'oreille",
       p:"Le français écrit une chose et en dit souvent une autre. Ce n'est pas grave dans la vie courante — on finit par savoir. Ça devient gênant le jour où l'on entend un mot pour la première fois à la radio : on le comprend, on va le chercher dans un dictionnaire, et on ne le trouve pas, parce qu'on l'a écrit comme on l'a entendu.",
       note:"Le programme du niveau 6 nomme ces trois cas : « ch » qui se dit comme un k, « x » qui se dit comme un s, et « sh » ou « sch » qui se disent comme un ch."},

      {t:'ana', h:"Cas 1 — « ch » qui se dit comme un K",
       p:"Presque toujours dans des mots venus du grec. Ce sont des mots savants, et il y en a partout dans les médias.",
       mots:[['On écrit','une {ch}ronique · la te{ch}nique · un {ch}œur · la psy{ch}ologie'],
             ['On entend','[k], comme dans « kilo »', true],
             ['Le repère','un mot savant, souvent avec « y » ou « ph » à côté']],
       say:"une chronique, la technique, un chœur, la psychologie",
       note:"Attention : « chercher », « chaque », « chose » gardent le son normal. Le K est l'exception, pas la règle."},

      {t:'ana', h:"Cas 2 — « x » qui se dit comme un S",
       p:"Dans quelques nombres et quelques noms de lieux, très fréquents.",
       mots:[['On écrit','di{x} · si{x} · soi{x}ante · Bru{x}elles'],
             ['On entend','[s], comme dans « dis »', true],
             ['Le piège du nombre','« dix » se dit [dis] tout seul, [di] devant un nom qui commence par une consonne, et [diz] devant une voyelle']],
       say:"dix, six, soixante, Bruxelles",
       note:"Dix dollars se dit « di dollars ». Dix ans se dit « diz ans ». Dix, tout seul, se dit « dis »."},

      {t:'ana', h:"Cas 3 — « sh » et « sch » qui se disent comme un CH",
       p:"Des mots empruntés à l'anglais, à l'allemand ou à l'hébreu, et devenus courants.",
       mots:[['On écrit','un {sh}érif · un {sh}ort · un {sch}éma'],
             ['On entend','[ʃ], le son de « chat »', true],
             ['Le repère','un mot qui vient d\'ailleurs, souvent court']],
       say:"un shérif, un short, un schéma",
       note:"« Un schéma », dans une chronique pratique, revient très souvent : c'est le dessin qui accompagne une explication."},

      {t:'labo', h:"Écoutez, puis répétez",
       p:"Choisissez un cas et un exemple.",
       axes:[
         {id:'c', lbl:'Quelles lettres ?', opts:[['a','ch qui dit K'],['b','x qui dit S'],['c','sh, sch qui disent CH']]},
         {id:'n', lbl:'Quel exemple ?', opts:[['1','le premier'],['2','le second']]}],
       out:{
         a1:{w:["une chronique"], say:"une chronique", n:'mot grec : « cro-nique »'},
         a2:{w:["la technique"], say:"la technique", n:'même famille : « tec-nique »'},
         b1:{w:["dix"], say:"dix", n:'tout seul, on entend le S final'},
         b2:{w:["soixante"], say:"soixante", n:'« soi-sante », jamais « soi-ksante »'},
         c1:{w:["un schéma"], say:"un schéma", n:'trois lettres pour le son de « chat »'},
         c2:{w:["un shérif"], say:"un shérif", n:'venu de l\'anglais, prononcé à la française'},
       },
       note:"Écoutez deux fois avant de répéter. C'est l'oreille qu'on entraîne, pas la mémoire."},

      {t:'ex', h:"Huit mots du module",
       p:"À gauche ce qui est écrit, à droite ce qui se dit.",
       rows:[
         ["une chronique","« cro-nique » — le ch fait k"],
         ["la technique","« tec-nique » — le ch fait k"],
         ["un chœur","« keur » — le ch fait k"],
         ["la psychologie","« psi-co-lo-gie » — le ch fait k"],
         ["dix jours","« di jours » — le x se tait devant une consonne"],
         ["soixante","« soi-sante » — le x fait s"],
         ["un schéma","« ché-ma » — sch fait ch"],
         ["un short","« chort » — sh fait ch"],
       ]},

      {t:'piege', h:"Deux pièges, une consolation",
       rows:[
         ["chercher le mot avec la lettre entendue","chercher avec la lettre écrite",
          "Vous entendez « cronique » et vous cherchez « cronique » : rien. Quand un mot entendu ne se trouve pas, essayez « ch » à la place du k, et « x » à la place du s."],
         ["prononcer chaque « ch » comme dans « chat »","reconnaître les mots savants",
          "« Technique » dit à la française avec le son de « chat » ne se comprend pas du tout. Ces mots-là sont peu nombreux : ils s'apprennent un par un."],
         ["s'inquiéter pour « dix »","les trois formes se comprennent",
          "Personne ne vous reprendra si vous dites « diz jours ». Ce qui compte, c'est de reconnaître les trois formes à l'écoute, pas de les produire parfaitement."],
       ]},

      {t:'check', h:"Est-ce que c'est clair maintenant ?",
       p:"Quatre questions rapides.",
       qs:[
         {q:"Dans « chronique », les lettres « ch » se disent…", opts:["comme dans chat","comme un k"], ok:1,
          fb:"C'est un mot venu du grec : « cro-nique »."},
         {q:"Dans « soixante », la lettre « x » se dit…", opts:["comme un s","comme un ks"], ok:0,
          fb:"« Soi-sante ». Même chose dans « dix » et « six »."},
         {q:"Dans « un schéma », les lettres « sch » se disent…", opts:["comme un sk","comme dans chat"], ok:1,
          fb:"Trois lettres pour un seul son, celui de « chat »."},
         {q:"« Dix dollars » se prononce…", opts:["« di dollars »","« diss dollars »"], ok:0,
          fb:"Devant une consonne, le x de « dix » ne s'entend pas."},
       ]},

      {t:'revoir', h:"À retenir",
       p:"Trois cas seulement, mais fréquents dans les médias : <b>ch</b> qui dit k dans les mots savants (chronique, technique), <b>x</b> qui dit s dans les nombres et quelques noms de lieux (dix, six, soixante), <b>sh</b> et <b>sch</b> qui disent ch dans les mots empruntés (short, schéma)."},
    ]
  },

  prPonct: {
    eye:'Mini-leçon', tit:"Le tiret et les guillemets, à la lecture",
    blocs:[
      {t:'texte', h:"Deux signes qui portent du sens, pas de la décoration",
       p:"Dans un journal, le tiret et les guillemets ne sont pas là pour aérer la page. Chacun dit quelque chose au lecteur, et ne pas le lire, c'est perdre une information. Le programme du niveau 6 les nomme tous les deux : comprendre l'utilisation du tiret, et employer les guillemets pour encadrer un mot qu'on désire souligner ou nuancer.",
       note:"Ce sont deux signes qu'on rencontre bien avant d'avoir à les écrire. On les apprend donc d'abord en lecteur."},

      {t:'ana', h:"Le tiret, trois emplois",
       p:"Le même signe, trois travaux différents. C'est la place dans la phrase qui les distingue.",
       mots:[['Après une phrase complète','il ouvre une <b>énumération</b>'],
             ['En tête de ligne','il marque un <b>changement de locuteur</b>'],
             ['En paire, au milieu','il encadre une <b>précision</b>, comme des parenthèses', true],
             ['Ce qu\'il ne fait jamais','remplacer un point ou une virgule ordinaire']],
       say:"Trois étapes — le marchand, la lettre, le tribunal.",
       note:"Le tiret de la paire s'ouvre et se ferme. Un tiret seul au milieu d'une phrase est presque toujours le premier des trois emplois."},

      {t:'ana', h:"Les guillemets, deux emplois très différents",
       p:"L'un rend les mots à quelqu'un, l'autre les met à distance. Confondre les deux fait tout comprendre à l'envers.",
       mots:[['Autour d\'une phrase entière','ce sont les <b>mots exacts</b> de quelqu\'un'],
             ['Autour d\'un seul mot','l\'auteur <b>ne le prend pas à son compte</b>', true],
             ['Le repère','une citation est annoncée : « elle a dit », « selon lui », deux points'],
             ['L\'autre repère','le mot entre guillemets est souvent un mot du langage courant']],
       say:"Sa laveuse était « irréparable », paraît-il.",
       note:"« L'appareil était irréparable » et « L'appareil était “irréparable” » ne disent pas la même chose : dans le second, l'auteur doute du mot."},

      {t:'ex', h:"Six exemples, et ce qu'ils veulent dire",
       p:"À gauche la phrase, à droite ce que le signe apporte.",
       rows:[
         ["Trois étapes — le marchand, la lettre, le tribunal.","Le tiret annonce la liste qui suit."],
         ["— Et si le marchand refuse ?","Quelqu'un d'autre prend la parole."],
         ["La durée raisonnable — celle de la loi — dépend du prix.","Précision ajoutée, qu'on pourrait retirer."],
         ["Elle a répondu : « Je vous rappelle jeudi. »","Ses mots exacts, rien de reformulé."],
         ["On lui a dit que l'appareil était « fini ».","L'auteur rapporte le mot sans le reprendre à son compte."],
         ["Le journal publie les lettres « signées de leur auteur ».","Formule officielle du journal, citée telle quelle."],
       ]},

      {t:'check', h:"Est-ce que c'est clair maintenant ?",
       p:"Quatre questions rapides.",
       qs:[
         {q:"Un tiret en tête de ligne, dans un texte, veut dire…", opts:["une liste commence","quelqu'un d'autre parle"], ok:1,
          fb:"C'est le tiret de dialogue : il remplace le nom du locuteur."},
         {q:"Deux tirets au milieu d'une phrase servent à…", opts:["encadrer une précision","séparer deux phrases"], ok:0,
          fb:"Ils fonctionnent comme des parenthèses : on peut retirer ce qu'ils encadrent."},
         {q:"Des guillemets autour d'un seul mot veulent souvent dire…", opts:["c'est un mot important","l'auteur ne reprend pas ce mot à son compte"], ok:1,
          fb:"C'est une façon polie de dire : ce n'est pas moi qui le qualifie ainsi."},
         {q:"« Je vous rappelle jeudi » entre guillemets, après deux points, c'est…", opts:["une citation","une mise à distance"], ok:0,
          fb:"Phrase entière annoncée par deux points : ce sont les mots exacts de la personne."},
       ]},

      {t:'revoir', h:"À retenir",
       p:"Le <b>tiret</b> ouvre une liste, marque qui parle, ou encadre une précision. Les <b>guillemets</b> citent les mots exacts de quelqu'un — ou, autour d'un seul mot, disent que l'auteur s'en méfie."},
    ]
  },

  prGenres: {
    eye:'Mini-leçon', tit:"Savoir d'avance ce qu'un texte va donner",
    blocs:[
      {t:'texte', h:"La question à se poser avant de lire",
       p:"« Qu'est-ce que ce texte va me donner ? » On perd beaucoup de temps à chercher dans un genre ce qu'il ne contient pas : une opinion dans un fait divers, une démarche dans un documentaire, un fait vérifié dans une lettre de lecteur. Reconnaître le genre en trois secondes, c'est se donner les bonnes attentes — et c'est plus utile que de connaître dix mots de plus.",
       note:"Les quatre intentions du niveau 6 pour cette situation nomment exactement ces genres : la chronique pratique, l'entrevue, le documentaire, le fait divers et le courrier des lecteurs."},

      {t:'ana', h:"Les signes qui trahissent le genre, en trois secondes",
       p:"On les repère sans lire, à l'œil ou à l'oreille.",
       mots:[['Une signature et une photo d\'auteur','chronique — c\'est quelqu\'un, chaque semaine'],
             ['Des questions courtes et des réponses longues','entrevue'],
             ['Une voix seule, au passé, sur des images','documentaire', true],
             ['Un titre en majuscules, quinze lignes, aucun nom d\'auteur','fait divers'],
             ['Une lettre, un nom de ville sous la signature','courrier des lecteurs']],
       say:"une chronique, une entrevue, un documentaire, un fait divers, le courrier des lecteurs",
       note:"Le nom de ville sous la signature est propre au courrier des lecteurs : les journalistes, eux, ne le mettent jamais."},

      {t:'ana', h:"Ce que chaque genre ne fera jamais",
       p:"C'est souvent plus utile à savoir que ce qu'il fait.",
       mots:[['La chronique pratique','ne raconte pas un événement de la semaine'],
             ['L\'entrevue','ne dit rien que l\'invité ne veuille dire'],
             ['Le documentaire','ne parle presque jamais de cette semaine-ci', true],
             ['Le fait divers','ne cherche pas de coupable et ne tire pas de leçon'],
             ['Le courrier des lecteurs','n\'engage jamais le journal']],
       say:"Le fait divers ne cherche pas de coupable et ne tire pas de leçon.",
       note:"Un lecteur qui lit un jugement dans un fait divers l'y a mis lui-même. C'est très fréquent, et c'est ce qui alimente les rumeurs."},

      {t:'ex', h:"Une même affaire, cinq traitements",
       p:"Le sujet est le même : les appareils qui brisent trop vite.",
       rows:[
         ["Chronique pratique","« Voici les trois étapes à suivre si votre laveuse brise. »"],
         ["Entrevue","« Madame Vaugeois, qu'est-ce qui vous préoccupe le plus ? »"],
         ["Documentaire","« En 1924, les fabricants se réunirent à Genève. »"],
         ["Fait divers","« Un incendie a détruit deux logements de la rue Sainte-Marguerite. »"],
         ["Courrier des lecteurs","« À mon avis, on demande beaucoup trop aux consommateurs. »"],
       ]},

      {t:'check', h:"Est-ce que c'est clair maintenant ?",
       p:"Quatre questions rapides.",
       qs:[
         {q:"Pour savoir quoi faire d'un appareil brisé, on cherche…", opts:["un fait divers","une chronique pratique"], ok:1,
          fb:"C'est le seul genre qui donne une démarche en étapes."},
         {q:"Un nom de ville sous une signature annonce…", opts:["une lettre de lecteur","un article de journaliste"], ok:0,
          fb:"Les journalistes n'indiquent pas leur ville de résidence."},
         {q:"Un fait divers contient…", opts:["des faits et l'avis du journal","des faits seulement"], ok:1,
          fb:"Aucun avis, jamais. C'est ce qui le définit."},
         {q:"Le journal est-il d'accord avec les lettres qu'il publie ?", opts:["pas nécessairement","oui, sinon il ne les publierait pas"], ok:0,
          fb:"L'encadré du journal le dit : les opinions n'engagent que ceux qui les signent."},
       ]},

      {t:'revoir', h:"À retenir",
       p:"Reconnaître le genre avant de lire, c'est savoir ce qu'on va y trouver — et surtout ce qu'on n'y trouvera pas."},
    ]
  },

  t1ordre: {
    eye:'Mini-leçon', tit:"Suivre une démarche en étapes",
    blocs:[
      {t:'texte', h:"Ce qu'il faut retenir d'une chronique pratique",
       p:"Pas les mots : l'ordre. Une chronique pratique donne une démarche, et une démarche dont on saute une étape ne fonctionne pas — dans le cas de la garantie légale, elle fait même perdre le recours. Quand vous écoutez, comptez les étapes sur vos doigts. Le reste s'oublie sans dommage.",
       note:"Le programme du niveau 6 demande de « comprendre l'ordre des étapes d'une consigne à partir d'indices linguistiques autres que les connecteurs de temps ». C'est exactement ce qui suit."},

      {t:'ana', h:"Les rangs annoncés — les plus faciles",
       p:"Le locuteur numérote. Rien à deviner.",
       mots:[['À l\'écrit et dans les exposés','premièrement · deuxièmement · troisièmement'],
             ['À l\'oral, plus courant','d\'abord · ensuite · puis · enfin', true],
             ['Pour la dernière étape','en dernier recours · si rien ne marche'],
             ['Attention','« finalement » ne veut pas dire « enfin » au Québec : il veut souvent dire « en fin de compte »']],
       say:"premièrement, deuxièmement, troisièmement",
       note:"« En dernier recours » place une étape à la fin sans la numéroter, et prévient qu'on n'y va pas de gaieté de cœur."},

      {t:'ana', h:"Les rangs cachés — ceux qu'il faut apprendre à voir",
       p:"Aucun mot d'ordre, et pourtant la place de l'étape est fixée.",
       mots:[['Dans une condition','<b>Si ça ne bouge pas</b>, vous écrivez. → cette étape ne vient qu\'après un échec'],
             ['Dans un verbe','Vous <b>retournez</b> voir le marchand. → « retourner » suppose une première visite', true],
             ['Dans un adverbe','Vous écrivez <b>alors</b> une lettre. → « alors » veut dire : à ce moment-là de la démarche'],
             ['Dans un temps','Une fois la lettre <b>envoyée</b>, vous attendez. → le participe passé place l\'antériorité']],
       say:"Si ça ne bouge pas, vous écrivez une mise en demeure.",
       note:"C'est le point le plus difficile de l'écoute au niveau 6, et il ne s'entend qu'en cherchant le sens, pas les mots."},

      {t:'ex', h:"La démarche de la chronique, telle qu'elle a été dite",
       p:"À gauche ce que dit la chroniqueuse, à droite le rang que ça donne.",
       rows:[
         ["« Gardez vos factures. »","Avant tout, dès le jour de l'achat."],
         ["« Vous retournez voir le commerçant. »","Étape 1 — « retournez » dit qu'on y est déjà allé."],
         ["« Si ça ne bouge pas, vous écrivez. »","Étape 2 — seulement si l'étape 1 a échoué."],
         ["« Vous donnez un délai de dix jours. »","Dans l'étape 2, pas une étape à part."],
         ["« Troisièmement, les petites créances. »","Étape 3 — annoncée, et la dernière."],
         ["« J'y reviens toujours : l'Office. »","Hors démarche — possible à n'importe quel moment."],
       ]},

      {t:'check', h:"Est-ce que c'est clair maintenant ?",
       p:"Quatre questions rapides.",
       qs:[
         {q:"« Vous retournez voir le commerçant » suppose…", opts:["qu'on y est déjà allé","que c'est la première visite"], ok:0,
          fb:"Le verbe « retourner » place l'étape à lui seul."},
         {q:"« Si ça ne bouge pas, vous écrivez » veut dire que la lettre…", opts:["se fait en même temps","se fait après un premier refus"], ok:1,
          fb:"La condition place l'étape : elle ne sert que si la précédente a échoué."},
         {q:"Que faut-il retenir en priorité d'une chronique pratique ?", opts:["l'ordre des étapes","le vocabulaire technique"], ok:0,
          fb:"Le vocabulaire se retrouve ; l'ordre, non."},
         {q:"Appeler l'Office, c'est…", opts:["l'étape 2","possible à tout moment"], ok:1,
          fb:"La chroniqueuse y revient sans le numéroter : ce n'est pas dans la suite."},
       ]},

      {t:'revoir', h:"À retenir",
       p:"Comptez les étapes, pas les mots. Et cherchez les rangs cachés : une condition en « si », un verbe comme « retourner », un participe passé — chacun place une étape sans jamais dire « ensuite »."},
    ]
  },

  t1repr: {
    eye:'Mini-leçon', tit:"Le, en, y : trois mots qui renvoient en arrière",
    blocs:[
      {t:'texte', h:"Pourquoi on perd le fil d'une chronique",
       p:"Ce n'est presque jamais à cause d'un mot inconnu. C'est à cause d'un mot de deux lettres. « Je vous en parle », « je le sais », « on y trouve tout » : chacun renvoie à quelque chose dit plus tôt, et si vous ne savez pas à quoi, la phrase devient vide. Ces mots-là sont courts, jamais accentués, et le locuteur ne les répète pas.",
       note:"Le programme appelle ça la <b>reprise de l'information</b>. C'est le cœur de la grammaire du texte au niveau 6."},

      {t:'ana', h:"« le » remplace une idée entière",
       p:"Pas un objet : toute une phrase déjà dite.",
       mots:[['La phrase de départ','Je sais <u>que la garantie court encore</u>.'],
             ['Ce qu\'on dit','Je <b>le</b> sais.', true],
             ['Ce qui ne change jamais','ce « le » ne s\'accorde pas : ni « la », ni « les »'],
             ['Les verbes qui l\'appellent','savoir, dire, croire, penser, ignorer, expliquer, répondre']],
       say:"Je le sais. Il le dit. Elle l'a expliqué.",
       note:"C'est le plus difficile des trois, parce qu'on cherche un objet et qu'il n'y en a pas."},

      {t:'ana', h:"« en » remplace « de + chose »",
       p:"Une préposition « de » disparaît, et le mot passe devant le verbe.",
       mots:[['La phrase de départ','Elle parle <u>de la garantie légale</u>.'],
             ['Ce qu\'on dit','Elle <b>en</b> parle.', true],
             ['Aussi pour la quantité','J\'ai <u>trois factures</u>. → J\'<b>en</b> ai trois.'],
             ['Mais pas pour une personne','Elle parle <u>de son voisin</u>. → Elle parle <b>de lui</b>.']],
       say:"Elle en parle. J'en ai trois. J'en ai besoin.",
       note:"Les verbes en « de » qui reviennent ici : parler de, avoir besoin de, s'occuper de, se souvenir de, se plaindre de."},

      {t:'ana', h:"« y » remplace « à + chose », ou un lieu",
       p:"Même mécanique, avec la préposition « à » ou avec un endroit.",
       mots:[['Une chose','Je pense <u>à ma facture</u>. → J\'<b>y</b> pense.'],
             ['Un lieu','Il va <u>aux petites créances</u>. → Il <b>y</b> va.', true],
             ['Mais pas pour une personne','Je pense <u>à ma sœur</u>. → Je pense <b>à elle</b>.'],
             ['Une expression à connaître','Il <b>y</b> a — le « y » n\'y remplace plus rien']],
       say:"J'y pense. Il y va. On y trouve tout.",
       note:"« On y trouve les modèles » : le « y », c'est l'Office. C'est la phrase exacte de la chronique."},

      {t:'labo', h:"Écoutez la phrase courte et sa phrase longue",
       p:"Choisissez le pronom et l'exemple.",
       axes:[
         {id:'p', lbl:'Quel pronom ?', opts:[['a','le'],['b','en'],['c','y']]},
         {id:'n', lbl:'Quel exemple ?', opts:[['1','le premier'],['2','le second']]}],
       out:{
         a1:{w:["Je le sais."], say:"Je sais que la garantie court encore. Je le sais.", n:'« le » remplace toute la phrase soulignée'},
         a2:{w:["Il l'a expliqué."], say:"Il a expliqué que la loi s'applique encore. Il l'a expliqué.", n:'devant une voyelle, « le » devient « l\'​ »'},
         b1:{w:["Elle en parle."], say:"Elle parle de la garantie légale. Elle en parle.", n:'« en » remplace « de la garantie légale »'},
         b2:{w:["J'en ai besoin."], say:"J'ai besoin d'une pièce de rechange. J'en ai besoin.", n:'avoir besoin de : donc « en »'},
         c1:{w:["J'y pense."], say:"Je pense à ma facture. J'y pense.", n:'penser à une chose : donc « y »'},
         c2:{w:["On y trouve tout."], say:"On trouve tout à l'Office. On y trouve tout.", n:'un lieu : donc « y »'},
       },
       note:"Écoutez d'abord la phrase longue, puis la courte. C'est ce chemin-là que fait l'oreille quand elle suit une chronique."},

      {t:'piege', h:"Trois pièges",
       rows:[
         ["accorder le « le » d'idée","le laisser invariable",
          "« Elle sait que c'est vrai. → Elle la sait. » ❌ Ce « le » ne désigne rien de féminin : il désigne une phrase. On dit « Elle le sait »."],
         ["employer « en » ou « y » pour une personne","garder la préposition",
          "« Je pense à ma sœur. → J'y pense. » ❌ Pour une personne, on dit « Je pense à elle ». Même chose pour « de » : « Je parle de lui »."],
         ["placer le pronom après le verbe","le placer devant",
          "« Je sais le. » ❌ En français, ces pronoms passent toujours devant le verbe conjugué — ou devant l'infinitif quand il y a deux verbes : « Je vais en parler »."],
       ]},

      {t:'check', h:"Est-ce que c'est clair maintenant ?",
       p:"Quatre questions rapides.",
       qs:[
         {q:"« Il le sait » — le « le » remplace…", opts:["un objet","une phrase entière"], ok:1,
          fb:"C'est le « le » d'idée : il remplace une subordonnée complétive."},
         {q:"« Elle parle de la garantie » devient…", opts:["Elle en parle","Elle y parle"], ok:0,
          fb:"La préposition est « de » : donc « en »."},
         {q:"« Je pense à ma facture » devient…", opts:["J'en pense","J'y pense"], ok:1,
          fb:"La préposition est « à » et c'est une chose : donc « y »."},
         {q:"« Je pense à ma sœur » devient…", opts:["J'y pense","Je pense à elle"], ok:1,
          fb:"Pour une personne, on garde la préposition et on met un pronom fort."},
       ]},

      {t:'revoir', h:"À retenir",
       p:"Trois petits mots, trois questions. <b>le</b> = une idée déjà dite. <b>en</b> = « de + chose ». <b>y</b> = « à + chose » ou un lieu. Quand vous en entendez un, reculez d'une phrase : la réponse est juste avant."},
    ]
  },

  t1rel: {
    eye:'Mini-leçon', tit:"Qui, que, où : dire long en une phrase",
    blocs:[
      {t:'texte', h:"Pourquoi les journaux en sont pleins",
       p:"Un journal doit dire beaucoup en peu de place. Plutôt que deux phrases — « J'ai écrit une lettre. Cette lettre est restée sans réponse. » — il en fait une : « La lettre que j'ai écrite est restée sans réponse. » Le nom reste au centre, et une petite phrase vient s'accrocher derrière lui.",
       note:"Le programme du niveau 6 nomme cette structure : déterminant + nom + subordonnée relative."},

      {t:'ana', h:"« qui » : le verbe qui suit n'a pas de sujet",
       p:"On accroche une action au nom, et le nom en est l'auteur.",
       mots:[['Deux phrases','C\'est une chronique. Elle passe le mardi.'],
             ['Une seule','C\'est une chronique <b>qui</b> passe le mardi.', true],
             ['Le test','après « qui », il manque le sujet du verbe'],
             ['Jamais d\'apostrophe','« qui » ne devient jamais « qu\'​ » devant une voyelle']],
       say:"C'est une chronique qui passe le mardi.",
       note:"« Qui elle passe » ❌ : le pronom est déjà le sujet, on ne le double pas."},

      {t:'ana', h:"« que » : le verbe qui suit a son sujet, mais pas d'objet",
       p:"On accroche au nom une action qu'on lui fait subir.",
       mots:[['Deux phrases','Voici la lettre. Elle a écrit cette lettre.'],
             ['Une seule','Voici la lettre <b>qu\'</b>elle a écrite.', true],
             ['Le test','après « que », le sujet est là ; c\'est l\'objet qui manque'],
             ['L\'accord','le participe passé s\'accorde avec ce qui précède : la lettre qu\'elle a écrit<b>e</b>']],
       say:"Voici la lettre qu'elle a écrite.",
       note:"C'est le seul endroit du module où le participe passé s'accorde avec avoir. Ça surprend, et c'est bien la règle."},

      {t:'ana', h:"« où » : un lieu — et aussi un moment",
       p:"Le second emploi est celui qu'on n'attend pas, et il est très fréquent.",
       mots:[['Un lieu','l\'endroit <b>où</b> on trouve les modèles'],
             ['Un moment','le jour <b>où</b> le commerçant a rappelé', true],
             ['Encore un moment','l\'année <b>où</b> l\'entente a été signée · l\'époque <b>où</b> tout se réparait'],
             ['Ce qu\'on dit à tort','« le jour que » ❌ — courant à l\'oral, mais fautif à l\'écrit']],
       say:"Le jour où le commerçant a rappelé, elle était au travail.",
       note:"Retenez la série : le jour où, le moment où, l'année où, l'époque où. Après un nom de temps, c'est toujours « où »."},

      {t:'ex', h:"Six phrases du module",
       p:"À gauche la phrase, à droite ce qui l'a décidée.",
       rows:[
         ["une chronique qui passe le mardi","« qui » — il manquait le sujet de « passe »"],
         ["la lettre qu'elle a écrite","« que » — il manquait l'objet de « a écrite »"],
         ["le jour où il a rappelé","« où » — un moment"],
         ["l'endroit où on trouve les modèles","« où » — un lieu"],
         ["un organisme qui ne prend pas votre dossier","« qui » — le sujet manquait"],
         ["la facture que le marchand lui a remise","« que » — l'objet manquait, et le participe s'accorde"],
       ]},

      {t:'piege', h:"Trois pièges",
       rows:[
         ["« le jour que »","« le jour où »",
          "Très fréquent à l'oral, et compris de tous — mais à l'écrit, dans une lettre au journal, il se remarque tout de suite."],
         ["doubler le sujet après « qui »","laisser « qui » faire le travail",
          "« une chronique qui elle passe le mardi » ❌. « Qui » EST le sujet : ajouter « elle » le répète."],
         ["oublier l'accord après « que »","accorder le participe passé",
          "« la lettre qu'elle a écrit » ❌ → « écrite ». Ce qui précède « que » commande l'accord."],
       ]},

      {t:'check', h:"Est-ce que c'est clair maintenant ?",
       p:"Quatre questions rapides.",
       qs:[
         {q:"« C'est une démarche ___ prend du temps. »", opts:["qui","que"], ok:0,
          fb:"« Prend » n'a pas de sujet : c'est « qui »."},
         {q:"« Voici la pièce ___ il a commandée. »", opts:["qui","qu'"], ok:1,
          fb:"« Il » est le sujet ; c'est l'objet qui manque."},
         {q:"« Je me souviens du jour ___ il a rappelé. »", opts:["que","où"], ok:1,
          fb:"Après un nom de temps, c'est « où »."},
         {q:"« La lettre qu'elle a écrit___ »", opts:["écrit","écrite"], ok:1,
          fb:"Le participe s'accorde avec « la lettre », placée avant."},
       ]},

      {t:'revoir', h:"À retenir",
       p:"Enlevez le mot et remettez la phrase droite. Si le verbe se retrouve sans sujet → <b>qui</b>. S'il lui manque un objet → <b>que</b>. Si c'est un endroit ou un moment → <b>où</b>."},
    ]
  },

  t1exempl: {
    eye:'Mini-leçon', tit:"Les mots qui annoncent un exemple",
    blocs:[
      {t:'texte', h:"Un signal précieux quand on écoute",
       p:"Quand un chroniqueur dit « par exemple », il vous prévient : ce qui vient ne contient aucune information nouvelle. Il va redire autrement ce qu'il vient de dire. C'est un moment de repos pour l'oreille — et une deuxième chance de comprendre la phrase précédente.",
       note:"Le programme demande d'employer des connecteurs d'exemplification et d'illustration courants. Les reconnaître à l'oral vient d'abord."},

      {t:'ana', h:"Les cinq à connaître",
       p:"Ils ne sont pas interchangeables : chacun annonce une sorte d'exemple.",
       mots:[['par exemple','un cas quelconque, le plus simple'],
             ['notamment','un cas parmi d\'autres, choisi exprès', true],
             ['ainsi','un cas qui démontre — plus écrit'],
             ['comme','une comparaison avec du connu'],
             ['prenons, c\'est le cas de','un cas qu\'on va développer']],
       say:"par exemple, notamment, ainsi, comme, prenons",
       note:"« Notamment » dit toujours : il y en a d'autres que je ne nomme pas. C'est une nuance, et elle compte."},

      {t:'ana', h:"Le piège d'« ainsi »",
       p:"Le même mot, deux sens tout à fait différents.",
       mots:[['Avec une virgule, en tête','<b>Ainsi</b>, une photo de la facture peut tout changer. = par exemple'],
             ['Sans virgule, dans la phrase','Il faut procéder <b>ainsi</b>. = de cette façon', true],
             ['Ce qui tranche','la place et la virgule, rien d\'autre'],
             ['À l\'oral','une petite pause après « ainsi » signale le premier sens']],
       say:"Ainsi, une photo de la facture peut tout changer.",
       note:"Le premier sens est celui des chroniques et des articles ; le second, celui des modes d'emploi."},

      {t:'ex', h:"Six phrases de la chronique",
       p:"À gauche la phrase, à droite ce que le connecteur annonce.",
       rows:[
         ["« Par exemple, il peut avoir été mal conçu. »","un cas quelconque parmi trois"],
         ["« Certains recours, notamment les petites créances… »","un cas choisi, il y en a d'autres"],
         ["« Ainsi, trente secondes valent des centaines de dollars. »","un cas qui démontre le propos"],
         ["« Un organisme public comme l'Office… »","une comparaison avec du connu"],
         ["« Prenons une laveuse de sept cent quatre-vingts dollars. »","un cas entier qu'on va développer"],
         ["« C'est le cas de madame Berthiaume. »","un cas réel, nommé"],
       ]},

      {t:'check', h:"Est-ce que c'est clair maintenant ?",
       p:"Quatre questions rapides.",
       qs:[
         {q:"Après « par exemple », l'information qui vient est…", opts:["nouvelle","une illustration de ce qui précède"], ok:1,
          fb:"C'est pour ça que c'est un repos : rien de neuf à retenir."},
         {q:"« Notamment » veut dire…", opts:["seulement celui-là","celui-là parmi d'autres"], ok:1,
          fb:"Il annonce toujours qu'il en existe d'autres."},
         {q:"« Ainsi, » en tête de phrase avec une virgule veut dire…", opts:["de cette façon","par exemple"], ok:1,
          fb:"C'est la virgule et la place qui décident."},
         {q:"« Prenons une laveuse de 780 $ » annonce…", opts:["un cas développé","une simple comparaison"], ok:0,
          fb:"Le chroniqueur s'arrête et raconte un cas entier."},
       ]},

      {t:'revoir', h:"À retenir",
       p:"Un connecteur d'exemple vous dit : détendez-vous, je reformule. <b>par exemple</b> (un cas), <b>notamment</b> (un parmi d'autres), <b>ainsi</b> (un cas qui démontre), <b>comme</b> (une comparaison), <b>prenons</b> (un cas développé)."},
    ]
  },

  t2pqp: {
    eye:'Mini-leçon', tit:"Le plus-que-parfait : ce qui s'était passé avant",
    blocs:[
      {t:'texte', h:"Deux passés dans la même phrase",
       p:"« Ils avaient jeté l'appareil avant de nous appeler. » Deux actions, toutes deux terminées, mais pas au même moment : d'abord jeter, ensuite appeler. Le français a un temps exprès pour dire « celle-là était déjà faite » : le plus-que-parfait. Sans lui, on entend deux actions et on ne sait pas laquelle est venue en premier.",
       note:"Le programme du niveau 6 le nomme ainsi : comprendre que le plus-que-parfait désigne une action précédant une autre action passée."},

      {t:'ana', h:"Comment il se fabrique",
       p:"Rien de neuf : le passé composé, avec l'auxiliaire à l'imparfait.",
       mots:[['Le passé composé','j\'ai compris · elle est partie · nous avons écrit'],
             ['Le plus-que-parfait','j\'<b>avais</b> compris · elle <b>était</b> partie · nous <b>avions</b> écrit', true],
             ['L\'auxiliaire ne change jamais de camp','« je suis parti » donne « j\'étais parti », jamais « j\'avais parti »'],
             ['L\'accord suit la même règle','elle était part<b>ie</b> · les pièces étaient arriv<b>ées</b>']],
       say:"J'avais compris. Elle était partie. Nous avions écrit.",
       note:"Si vous savez faire le passé composé, vous savez déjà faire le plus-que-parfait. Il n'y a qu'un mot à changer."},

      {t:'ana', h:"Les mots qui l'annoncent",
       p:"Dès que l'un d'eux paraît dans un récit au passé, attendez-vous à lui.",
       mots:[['déjà','Ils avaient <b>déjà</b> payé deux fois.'],
             ['la veille, l\'année d\'avant','Elle avait téléphoné <b>la veille</b>.', true],
             ['avant de, avant que','Ils avaient jeté l\'appareil <b>avant de</b> nous appeler.'],
             ['parce que','Il a rappelé <b>parce qu\'</b>il avait reçu la lettre.']],
       say:"Ils avaient déjà payé deux fois avant de nous appeler.",
       note:"« Parce que » est le plus intéressant : la cause est presque toujours antérieure, donc au plus-que-parfait."},

      {t:'labo', h:"Écoutez la différence",
       p:"La même phrase, deux ordres différents.",
       axes:[
         {id:'t', lbl:'Quel temps ?', opts:[['a','passé composé'],['b','plus-que-parfait']]},
         {id:'n', lbl:'Quel exemple ?', opts:[['1','le premier'],['2','le second']]}],
       out:{
         a1:{w:["Elle a téléphoné."], say:"Elle a téléphoné à l'Office.", n:'une action, sans rien avant'},
         a2:{w:["Il a reçu la lettre."], say:"Il a reçu la lettre.", n:'une action, sans rien avant'},
         b1:{w:["Elle avait téléphoné."], say:"Elle avait téléphoné à l'Office la veille.", n:'l\'appel précède autre chose de passé'},
         b2:{w:["Il avait reçu la lettre."], say:"Il a rappelé parce qu'il avait reçu la lettre.", n:'la lettre arrive avant l\'appel'},
       },
       note:"Deux syllabes de différence, et l'ordre des événements change complètement."},

      {t:'piege', h:"Trois pièges",
       rows:[
         ["changer d'auxiliaire","garder le même qu'au passé composé",
          "« j'avais parti » ❌ → « j'étais parti ». Le verbe garde son auxiliaire à tous les temps composés."],
         ["l'employer partout dans un récit","le réserver à ce qui précède",
          "Un récit au passé se fait au passé composé et à l'imparfait. Le plus-que-parfait n'apparaît que pour un retour en arrière."],
         ["le confondre avec l'imparfait","écouter l'auxiliaire",
          "« elle était » (imparfait, un état) et « elle était partie » (plus-que-parfait, une action antérieure) ne disent pas du tout la même chose."],
       ]},

      {t:'check', h:"Est-ce que c'est clair maintenant ?",
       p:"Quatre questions rapides.",
       qs:[
         {q:"« Ils avaient jeté l'appareil avant de nous appeler. » Que s'est-il passé en premier ?", opts:["l'appel","le fait de jeter"], ok:1,
          fb:"Le plus-que-parfait marque l'action déjà faite."},
         {q:"Le plus-que-parfait se forme avec l'auxiliaire…", opts:["à l'imparfait","au futur"], ok:0,
          fb:"avoir ou être à l'imparfait, plus le participe passé."},
         {q:"« Je suis parti » donne au plus-que-parfait…", opts:["j'avais parti","j'étais parti"], ok:1,
          fb:"L'auxiliaire ne change jamais de camp."},
         {q:"« Il a rappelé parce qu'il ___ la lettre. »", opts:["a reçu","avait reçu"], ok:1,
          fb:"La cause précède l'effet : plus-que-parfait."},
       ]},

      {t:'revoir', h:"À retenir",
       p:"Auxiliaire à l'imparfait + participe passé. Il dit une seule chose, et elle est précieuse : <b>c'était déjà fait</b>. Dans une entrevue, c'est presque toujours là que se cache la vraie cause."},
    ]
  },

  t2ps: {
    eye:'Mini-leçon', tit:"Le passé simple : le reconnaître, jamais l'écrire",
    blocs:[
      {t:'texte', h:"Un temps qu'on n'a pas à apprendre",
       p:"Le passé simple ne se parle pas. Personne, au Québec, ne dit « je mangeai » ni « nous partîmes ». On le rencontre dans les documentaires, les romans, les livres d'histoire — et c'est tout. Le programme du niveau 6 est explicite : il demande de <b>reconnaître les verbes courants à la 3e personne</b> et de les associer au passé composé. Rien de plus.",
       note:"C'est une bonne nouvelle : vous avez à comprendre une dizaine de formes, pas à conjuguer un temps entier."},

      {t:'ana', h:"Les trois familles de terminaisons",
       p:"On ne regarde que la 3e personne, singulier et pluriel.",
       mots:[['Verbes en -er','il fix{a} · ils fix{èrent} · il dur{a} · ils dur{èrent}'],
             ['Verbes en -ir','il fin{it} · ils fin{irent} · il part{it} · ils part{irent}', true],
             ['Quelques verbes courants','il f{ut} · ils f{urent} · il e{ut} · ils e{urent} · il conn{ut}'],
             ['Le repère','une terminaison courte, sans « r » de futur ni « ai » d\'imparfait']],
       say:"il fixa, ils fixèrent, il finit, ils finirent, il fut, ils furent",
       note:"Trois à connaître par cœur, parce qu'ils reviennent partout : <b>il fut</b> (= il a été), <b>il eut</b> (= il a eu), <b>ils firent</b> (= ils ont fait)."},

      {t:'ana', h:"Ce qu'il faut en faire dans sa tête",
       p:"Le traduire en passé composé, tout de suite, et continuer d'écouter.",
       mots:[['il se réunirent → ','ils se sont réunis'],
             ['ils fixèrent → ','ils ont fixé', true],
             ['l\'entente dura → ','l\'entente a duré'],
             ['elle ne fut connue que plus tard → ','elle n\'a été connue que plus tard']],
       say:"Ils se réunirent. Ils se sont réunis.",
       note:"Le sens est exactement le même. Seul le ton change : le passé simple est écrit, distant, définitif."},

      {t:'ex', h:"L'extrait du documentaire, ligne par ligne",
       p:"À gauche ce que dit la narratrice, à droite ce qu'on dirait en parlant.",
       rows:[
         ["les fabricants se réunirent à Genève","les fabricants se sont réunis à Genève"],
         ["ils fixèrent une durée de vie maximale","ils ont fixé une durée de vie maximale"],
         ["l'entente dura seize ans","l'entente a duré seize ans"],
         ["elle ne fut connue que plus tard","elle n'a été connue que plus tard"],
         ["des chercheurs retrouvèrent les documents","des chercheurs ont retrouvé les documents"],
         ["le public en eut la preuve","le public en a eu la preuve"],
       ]},

      {t:'piege', h:"Deux pièges d'oreille",
       rows:[
         ["confondre « il fixa » et « il fixera »","écouter la fin du mot",
          "« Fixa » est du passé, « fixera » est du futur. Dans un documentaire qui raconte 1924, c'est du passé."],
         ["chercher à l'employer soi-même","le laisser aux livres",
          "Écrire « je reçus votre lettre » dans un courriel au journal serait bizarre et daté. Écrivez « j'ai reçu »."],
       ]},

      {t:'check', h:"Est-ce que c'est clair maintenant ?",
       p:"Quatre questions rapides.",
       qs:[
         {q:"« Ils fixèrent » veut dire…", opts:["ils ont fixé","ils fixeront"], ok:0,
          fb:"C'est du passé simple : équivalent du passé composé."},
         {q:"Où rencontre-t-on le passé simple ?", opts:["dans les conversations","dans les documentaires et les romans"], ok:1,
          fb:"Jamais à l'oral spontané, jamais dans une lettre."},
         {q:"« Il fut » se traduit par…", opts:["il a été","il sera"], ok:0,
          fb:"C'est le passé simple d'« être »."},
         {q:"Le programme demande de…", opts:["l'écrire","le reconnaître"], ok:1,
          fb:"Reconnaître à la 3e personne, et associer au passé composé."},
       ]},

      {t:'revoir', h:"À retenir",
       p:"Trois familles : <b>-a / -èrent</b>, <b>-it / -irent</b>, <b>-ut / -urent</b>. Traduisez-le en passé composé dans votre tête et poursuivez. Vous n'aurez jamais à l'écrire."},
    ]
  },

  t2subj: {
    eye:'Mini-leçon', tit:"Le subjonctif après il faut que, je veux que…",
    blocs:[
      {t:'texte', h:"Ce que le subjonctif signale",
       p:"Il ne dit pas un fait. Il dit ce qu'on veut, ce qu'on exige, ce qu'on souhaite, ce qu'on craint. « Il faut que les pièces existent » : justement, elles n'existent pas toujours — c'est ce qu'on réclame. Un indicatif dirait le contraire : « les pièces existent » serait un constat.",
       note:"Le programme du niveau 6 demande d'employer le subjonctif présent après quelques verbes introducteurs usuels suivis de « que »."},

      {t:'ana', h:"Les six verbes introducteurs à retenir",
       p:"Après chacun d'eux, suivi de « que », le subjonctif est obligatoire.",
       mots:[['la nécessité','il faut que · il est important que'],
             ['la volonté','je veux que · je demande que', true],
             ['le souhait','je souhaite que · j\'aimerais que'],
             ['la crainte','j\'ai peur que · je crains que']],
       say:"il faut que, je veux que, je souhaite que, j'ai peur que",
       note:"Retenez-les comme des blocs sonores, pas comme une règle. C'est ainsi qu'on les emploie sans y penser."},

      {t:'ana', h:"Comment il se forme, à l'oral",
       p:"Un seul geste : on part du présent, 3e personne du pluriel.",
       mots:[['On prend','ils écriv{ent} · ils appell{ent} · ils gard{ent}'],
             ['On enlève -ent','que j\'écriv{e} · qu\'ils appell{ent} · qu\'elle gard{e}', true],
             ['Ce qui surprend','pour beaucoup de verbes, ça s\'entend exactement comme le présent'],
             ['Les six irréguliers','que je sois · que j\'aie · que j\'aille · que je fasse · que je puisse · que je sache']],
       say:"que j'écrive, qu'ils appellent, que je sois, que j'aie, que je fasse, que je sache",
       note:"Si vous ne retenez que six formes, retenez ces six-là : elles couvrent la moitié des subjonctifs qu'on entend."},

      {t:'ana', h:"Ce qui ne demande PAS le subjonctif",
       p:"Un verbe qui présente un fait garde l'indicatif. C'est l'erreur la plus fréquente dans l'autre sens.",
       mots:[['je pense que','je pense qu\'il <b>a</b> raison'],
             ['je crois que','je crois qu\'elle <b>viendra</b>', true],
             ['je sais que','je sais que la garantie <b>court</b> encore'],
             ['j\'espère que','j\'espère qu\'il <b>rappellera</b> — jamais « qu\'il rappelle »']],
       say:"Je pense qu'il a raison. J'espère qu'il rappellera.",
       note:"« Espérer » est le grand piège : il ressemble à « souhaiter », mais il prend l'indicatif."},

      {t:'labo', h:"Écoutez les deux côtés",
       p:"Le même verbe, avec un introducteur puis l'autre.",
       axes:[
         {id:'m', lbl:'Quel mode ?', opts:[['a','subjonctif'],['b','indicatif']]},
         {id:'n', lbl:'Quel exemple ?', opts:[['1','le premier'],['2','le second']]}],
       out:{
         a1:{w:["Il faut qu'ils existent."], say:"Il faut que les pièces existent.", n:'nécessité : subjonctif'},
         a2:{w:["Je souhaite qu'ils appellent."], say:"Je souhaite qu'ils appellent avant de jeter.", n:'souhait : subjonctif'},
         b1:{w:["Je sais qu'elles existent."], say:"Je sais que les pièces existent.", n:'constat : indicatif'},
         b2:{w:["J'espère qu'ils appelleront."], say:"J'espère qu'ils appelleront avant de jeter.", n:'espérer : indicatif, malgré le sens'},
       },
       note:"Écoutez le début de la phrase, pas la fin : c'est l'introducteur qui décide de tout."},

      {t:'check', h:"Est-ce que c'est clair maintenant ?",
       p:"Quatre questions rapides.",
       qs:[
         {q:"« Il faut que les pièces ___ . »", opts:["existent","existeront"], ok:0,
          fb:"Après « il faut que », subjonctif obligatoire."},
         {q:"« J'espère qu'il ___ . »", opts:["rappelle","rappellera"], ok:1,
          fb:"« Espérer » prend l'indicatif, malgré le sens de souhait."},
         {q:"Pour former le subjonctif, on part de…", opts:["l'infinitif","la 3e personne du pluriel du présent"], ok:1,
          fb:"On enlève « -ent » et on ajoute les terminaisons."},
         {q:"« Je pense que » demande…", opts:["l'indicatif","le subjonctif"], ok:0,
          fb:"Il présente un fait : indicatif."},
       ]},

      {t:'revoir', h:"À retenir",
       p:"Le subjonctif dit ce qu'on <b>veut</b>, jamais ce qui <b>est</b>. Après <i>il faut que, je veux que, je souhaite que, j'ai peur que</i> : subjonctif. Après <i>je pense que, je sais que, j'espère que</i> : indicatif."},
    ]
  },

  t2dequ: {
    eye:'Mini-leçon', tit:"« de » et un infinitif, ou « que » et un subjonctif",
    blocs:[
      {t:'texte', h:"Une question à se poser, et une seule",
       p:"« Est-ce que c'est la même personne qui fait les deux choses ? » Si oui, un infinitif suffit et on n'a pas besoin de subjonctif du tout. Si non, il faut « que » et le subjonctif. Cette question règle presque tous les cas, et elle épargne beaucoup de conjugaisons.",
       note:"Le programme le formule ainsi : distinguer un verbe introducteur + de et un verbe introducteur + que."},

      {t:'ana', h:"Un seul sujet : de + infinitif",
       p:"La deuxième action est faite par la même personne.",
       mots:[['La phrase','Je vous demande <b>d\'</b>être prudent.'],
             ['Qui demande ? qui est prudent ?','moi qui demande, vous à qui je le demande — un seul verbe conjugué', true],
             ['Les verbes de cette famille','demander de · accepter de · refuser de · éviter de · essayer de · oublier de'],
             ['Deux sans « de »','vouloir et espérer : je veux <b>partir</b> · j\'espère <b>gagner</b>']],
       say:"Je vous demande d'être prudent. Je veux partir.",
       note:"L'infinitif est plus court, plus simple, et toujours juste quand le sujet est le même."},

      {t:'ana', h:"Deux sujets : que + subjonctif",
       p:"Les deux actions ont deux auteurs différents.",
       mots:[['La phrase','Je demande <b>que</b> les pièces <b>soient</b> disponibles.'],
             ['Qui demande ? qui est disponible ?','moi d\'un côté, les pièces de l\'autre : deux sujets', true],
             ['Même chose après','avant que · pour que · bien que · jusqu\'à ce que'],
             ['Le repère','si vous pouvez nommer deux sujets différents, c\'est « que »']],
       say:"Je demande que les pièces soient disponibles.",
       note:"« Avant que le juge entende la cause » : moi je parle, le juge entend. Deux sujets, donc subjonctif."},

      {t:'ex', h:"Six phrases de l'entrevue",
       p:"À gauche la phrase, à droite pourquoi.",
       rows:[
         ["Je vous demande d'être prudent.","un seul sujet → de + infinitif"],
         ["Je demande que les pièces soient disponibles.","deux sujets → que + subjonctif"],
         ["Elle souhaite aider les gens.","elle souhaite, elle aide → infinitif"],
         ["Elle souhaite que les gens appellent.","elle souhaite, les gens appellent → que"],
         ["Il faut éviter de jeter trop vite.","un seul sujet → de + infinitif"],
         ["Il faut que la personne ait gardé ses preuves.","deux sujets → que + subjonctif"],
       ]},

      {t:'piege', h:"Trois pièges",
       rows:[
         ["répéter le sujet avec « que »","employer l'infinitif",
          "« Je veux que je comprenne » ❌ → « Je veux comprendre ». Avec le même sujet, on ne double jamais."],
         ["mettre « de » après vouloir","ne rien mettre",
          "« Je veux de partir » ❌ → « Je veux partir ». Vouloir et espérer se passent de préposition."],
         ["employer l'indicatif après « avant que »","le subjonctif",
          "« avant que le juge entend » ❌ → « avant que le juge entende ». Ces conjonctions demandent toujours le subjonctif."],
       ]},

      {t:'check', h:"Est-ce que c'est clair maintenant ?",
       p:"Quatre questions rapides.",
       qs:[
         {q:"« Je vous demande ___ être prudent. »", opts:["d'","que vous soyez"], ok:0,
          fb:"Les deux se disent, mais l'infinitif est le plus naturel ici."},
         {q:"« Elle souhaite ___ les gens appellent. »", opts:["de","que"], ok:1,
          fb:"Deux sujets différents : « que » et le subjonctif."},
         {q:"« Je veux ___ comprendre. »", opts:["de","rien"], ok:1,
          fb:"Vouloir n'a pas de préposition devant l'infinitif."},
         {q:"« Avant que le juge ___ la cause. »", opts:["entend","entende"], ok:1,
          fb:"« Avant que » demande le subjonctif."},
       ]},

      {t:'revoir', h:"À retenir",
       p:"Une question : <b>même sujet ?</b> Oui → de + infinitif (ou rien, après vouloir et espérer). Non → que + subjonctif."},
    ]
  },

  t2idees: {
    eye:'Mini-leçon', tit:"Idée principale, idée secondaire",
    blocs:[
      {t:'texte', h:"Pourquoi ça compte plus qu'on ne croit",
       p:"Écouter une entrevue de vingt minutes en essayant de tout retenir ne marche pas. Ce qu'on retient, c'est trois ou quatre idées principales, et le reste sert à les appuyer. Savoir lesquelles sont principales, c'est ce qui permet de résumer ensuite — et de rédiger un texte en paragraphes, ce que le niveau 6 demande à l'écrit.",
       note:"« Idée principale ou secondaire » fait partie du métalangage du niveau 6 : ce sont des mots que l'élève doit pouvoir employer."},

      {t:'ana', h:"Le test de l'idée principale",
       p:"Répétez-la à quelqu'un qui n'a rien entendu.",
       mots:[['Si elle se comprend seule','c\'est une idée principale'],
             ['Si elle laisse une question','c\'est une idée secondaire', true],
             ['Exemple principal','Un appareil qu\'on ne peut pas réparer est jetable.'],
             ['Exemple secondaire','Nos lignes sonnent pendant trois jours. → trois jours après quoi ?']],
       say:"Un appareil qu'on ne peut pas réparer est jetable.",
       note:"Ce test se fait en une seconde, et il ne se trompe presque jamais."},

      {t:'ana', h:"Où se cache l'idée principale d'une entrevue",
       p:"Trois endroits, presque toujours les mêmes.",
       mots:[['Après une question courte','« Laquelle vous préoccupe le plus ? » — ce qui suit est central'],
             ['Après « ce que je veux dire, c\'est »','l\'invité se corrige et resserre', true],
             ['Dans la dernière réponse','on demande souvent « un mot pour finir »'],
             ['Rarement au début','les premières minutes servent à présenter, pas à dire']],
       say:"Laquelle des trois vous préoccupe le plus ?",
       note:"Les questions courtes d'un animateur ne sont pas des transitions : ce sont ses vraies questions."},

      {t:'ex', h:"Six phrases de l'entrevue, triées",
       p:"À gauche la phrase, à droite ce qu'elle est.",
       rows:[
         ["Trois problèmes se cachent derrière la même expression.","PRINCIPALE — se comprend seule"],
         ["Nos lignes sonnent pendant trois jours.","SECONDAIRE — après quoi ?"],
         ["Un appareil qu'on ne peut réparer est jetable.","PRINCIPALE — c'est sa thèse"],
         ["L'entente a duré seize ans.","SECONDAIRE — un détail de l'exemple"],
         ["Une lettre écrite laisse une trace.","PRINCIPALE — c'est son conseil"],
         ["Les documents étaient dans des archives d'entreprise.","SECONDAIRE — une précision"],
       ]},

      {t:'check', h:"Est-ce que c'est clair maintenant ?",
       p:"Quatre questions rapides.",
       qs:[
         {q:"Une idée secondaire, répétée seule…", opts:["se comprend","laisse une question"], ok:1,
          fb:"C'est exactement le test."},
         {q:"Après « par exemple », vient…", opts:["une idée secondaire","une idée principale"], ok:0,
          fb:"Un exemple illustre : il dépend de ce qui précède."},
         {q:"Dans une entrevue, l'idée principale se trouve souvent…", opts:["dans les premières minutes","après une question courte"], ok:1,
          fb:"Les premières minutes servent à présenter."},
         {q:"À quoi sert cette distinction, à l'écrit ?", opts:["à écrire en paragraphes","à écrire plus long"], ok:0,
          fb:"Un paragraphe porte une idée principale ; les autres phrases la servent."},
       ]},

      {t:'revoir', h:"À retenir",
       p:"Une idée principale se tient debout toute seule. Une idée secondaire laisse une question. Trois ou quatre principales par entrevue, pas davantage — c'est tout ce qu'il faut retenir."},
    ]
  },

  t3si: {
    eye:'Mini-leçon', tit:"L'hypothèse avec « si »",
    blocs:[
      {t:'texte', h:"Le mot des lettres de lecteurs",
       p:"« Si les gens savaient que ça marche, ils écriraient. » « Si je dois écrire une lettre chaque fois, je vais y passer mes soirées. » Les deux lettres du journal en sont pleines, et ce n'est pas un hasard : « si » permet de reprocher sans accuser personne, et de proposer sans exiger. C'est l'outil de la discussion polie.",
       note:"Le programme demande d'exprimer la condition dans une hypothèse avec le marqueur « si », et d'employer l'indicatif présent après « si » dans les hypothèses réalistes."},

      {t:'ana', h:"L'hypothèse réaliste — la plus fréquente",
       p:"Ça peut arriver pour de vrai. Après « si », le présent.",
       mots:[['La condition','<b>si</b> + présent : si le marchand refuse…'],
             ['La suite, au présent','… vous <b>avez</b> un recours.'],
             ['La suite, au futur','… vous <b>écrirez</b> une mise en demeure.', true],
             ['La suite, à l\'impératif','… <b>écrivez</b>-lui.']],
       say:"Si le marchand refuse, vous écrirez une mise en demeure.",
       note:"Trois suites possibles, un seul temps après « si ». C'est la moitié du travail."},

      {t:'ana', h:"Sur un fait déjà passé",
       p:"On ne sait pas si c'est arrivé ; on dit ce qui suit dans ce cas-là.",
       mots:[['La forme','<b>si</b> + passé composé, puis présent ou futur'],
             ['L\'exemple','<b>Si</b> vous <b>avez gardé</b> la facture, vous <b>pouvez</b> réclamer.', true],
             ['Un autre','<b>Si</b> le technicien <b>est venu</b> deux fois, notez les dates.'],
             ['Ce que ça n\'est pas','ce n\'est pas un regret : c\'est une condition qu\'on ignore encore']],
       say:"Si vous avez gardé la facture, vous pouvez réclamer.",
       note:"Très fréquent dans les chroniques pratiques : le chroniqueur ne sait pas ce que l'auditeur a fait."},

      {t:'ana', h:"« si » qui n'est pas une condition",
       p:"Le même mot sert à rapporter une question. Il n'y a alors aucune hypothèse.",
       mots:[['La question directe','« Est-ce que le marchand a rappelé ? »'],
             ['Rapportée','Il demande <b>si</b> le marchand a rappelé.', true],
             ['Le repère','un verbe de question devant : demander, savoir, se demander, vérifier'],
             ['Et ici, le futur est permis','Je me demande <b>s\'il</b> rappellera.']],
       say:"Il demande si le marchand a rappelé.",
       note:"C'est le seul cas où « si » accepte un futur — parce que ce n'est pas une condition."},

      {t:'labo', h:"Écoutez les trois emplois",
       p:"Choisissez l'emploi et l'exemple.",
       axes:[
         {id:'e', lbl:'Quel emploi ?', opts:[['a','condition réaliste'],['b','sur un fait passé'],['c','question rapportée']]},
         {id:'n', lbl:'Quel exemple ?', opts:[['1','le premier'],['2','le second']]}],
       out:{
         a1:{w:["Si le marchand refuse, écrivez."], say:"Si le marchand refuse, écrivez une mise en demeure.", n:'présent après « si », impératif après'},
         a2:{w:["Si tu téléphones, tu sauras."], say:"Si tu téléphones à l'Office, tu sauras tout de suite.", n:'présent après « si », futur après'},
         b1:{w:["Si vous avez gardé la facture…"], say:"Si vous avez gardé la facture, vous pouvez réclamer.", n:'passé composé après « si »'},
         b2:{w:["Si le technicien est venu…"], say:"Si le technicien est venu deux fois, notez les dates.", n:'même forme, autre verbe'},
         c1:{w:["Il demande si le marchand a rappelé."], say:"Il demande si le marchand a rappelé.", n:'aucune condition : une question rapportée'},
         c2:{w:["Je me demande s'il rappellera."], say:"Je me demande s'il rappellera.", n:'le futur est permis ici, et seulement ici'},
       },
       note:"Le premier emploi est de loin le plus fréquent. Si vous n'en retenez qu'un, retenez celui-là."},

      {t:'piege', h:"Trois pièges",
       rows:[
         ["mettre un futur après « si »","mettre le présent",
          "« Si le marchand refusera » ❌ → « Si le marchand refuse ». C'est la faute la plus fréquente, et elle s'entend tout de suite."],
         ["mettre un conditionnel après « si »","mettre l'imparfait",
          "« Si les gens sauraient » ❌ → « Si les gens savaient, ils écriraient ». Le conditionnel va dans l'autre moitié de la phrase, jamais après « si »."],
         ["croire que tout « si » est une condition","chercher le verbe devant",
          "« Il demande si… » n'est pas une hypothèse. S'il y a un verbe de question devant, c'est une interrogation rapportée."],
       ]},

      {t:'check', h:"Est-ce que c'est clair maintenant ?",
       p:"Quatre questions rapides.",
       qs:[
         {q:"« Si le marchand ___ , vous écrirez. »", opts:["refuse","refusera"], ok:0,
          fb:"Jamais de futur après « si » quand c'est une condition."},
         {q:"« Si les gens savaient, ils ___ . »", opts:["écriraient","écriront"], ok:0,
          fb:"Imparfait après « si », conditionnel après : c'est l'hypothèse moins probable."},
         {q:"« Si vous avez gardé la facture, vous ___ réclamer. »", opts:["pouvez","pourriez"], ok:0,
          fb:"Passé composé après « si », présent ou futur après."},
         {q:"« Il demande si le marchand rappellera. » Le futur est-il permis ?", opts:["oui","non"], ok:0,
          fb:"Ce n'est pas une condition : c'est une question rapportée."},
       ]},

      {t:'revoir', h:"À retenir",
       p:"Après un <b>si</b> de condition, jamais de futur ni de conditionnel. Présent (ça peut arriver), passé composé (sur un fait qu'on ignore), imparfait (moins probable). Et méfiez-vous du <b>si</b> qui rapporte une question : il ne suit aucune de ces règles."},
    ]
  },

  t3pdv: {
    eye:'Mini-leçon', tit:"Annoncer un avis comme un avis",
    blocs:[
      {t:'texte', h:"Pourquoi ces trois mots changent tout",
       p:"« On demande trop aux consommateurs » se lit comme une affirmation, et se conteste durement. « À mon avis, on demande trop aux consommateurs » se lit comme un point de vue, et invite à répondre. Le contenu est le même ; l'accueil ne l'est pas. Dans une lettre au journal, ces trois mots décident de la façon dont on sera lu.",
       note:"Le programme demande d'employer des connecteurs de point de vue courants. C'est une compétence sociale autant que grammaticale."},

      {t:'ana', h:"Les cinq qui parlent de soi",
       p:"Ils se placent en tête de phrase, suivis d'une virgule.",
       mots:[['le plus neutre','à mon avis · selon moi'],
             ['le plus poli en désaccord','pour ma part — il annonce souvent une objection', true],
             ['le plus personnel','personnellement · pour ma part'],
             ['le plus soutenu','à mon sens · j\'estime que']],
       say:"À mon avis, selon moi, pour ma part, personnellement",
       note:"« Pour ma part » est le plus utile des cinq : il dit « voici où je me situe », sans dire que l'autre a tort."},

      {t:'ana', h:"Ceux qui renvoient à quelqu'un d'autre",
       p:"On rapporte un avis ou une information sans s'en porter garant.",
       mots:[['selon + nom','<b>Selon</b> le Service de sécurité incendie, le feu serait parti du sous-sol.'],
             ['d\'après + nom','<b>D\'après</b> la chroniqueuse, dix jours suffisent.', true],
             ['paraît-il','L\'appareil était irréparable, <b>paraît-il</b>.'],
             ['à ma connaissance','<b>À ma connaissance</b>, personne n\'a posé la question.']],
       say:"Selon le Service de sécurité incendie, le feu serait parti du sous-sol.",
       note:"« À ma connaissance » est précieux : il dit « je peux me tromper » sans affaiblir le reste de la lettre."},

      {t:'ex', h:"Six formules, et leur effet",
       p:"À gauche la formule, à droite ce qu'elle produit chez le lecteur.",
       rows:[
         ["À mon avis, …","J'annonce un avis ; on peut ne pas être d'accord."],
         ["Pour ma part, …","Je me situe, sans dire que l'autre a tort."],
         ["Personnellement, …","J'assume ; le ton est un peu plus vif."],
         ["Selon l'Office, …","Ce n'est pas moi qui l'affirme."],
         ["Paraît-il","On me l'a dit, je n'en réponds pas."],
         ["À ma connaissance, …","Je crois que c'est exact, mais je peux ignorer quelque chose."],
       ]},

      {t:'piege', h:"Trois pièges",
       rows:[
         ["les empiler","en choisir un",
          "« À mon avis, je pense personnellement que… » ❌ Un seul suffit ; trois donnent l'air de s'excuser."],
         ["les employer sur un fait","les réserver aux avis",
          "« À mon avis, l'incendie a détruit deux logements » ❌ Un fait n'a pas besoin d'être annoncé comme un avis : il se vérifie."],
         ["dire « selon moi je pense »","dire « selon moi » ou « je pense »",
          "Les deux disent la même chose. Ensemble, ils se répètent."],
       ]},

      {t:'check', h:"Est-ce que c'est clair maintenant ?",
       p:"Quatre questions rapides.",
       qs:[
         {q:"« Pour ma part » annonce souvent…", opts:["un accord total","un désaccord poli"], ok:1,
          fb:"C'est la formule de celui qui se situe autrement, sans agresser."},
         {q:"« Selon le Service de sécurité incendie » veut dire…", opts:["je l'affirme","eux l'affirment"], ok:1,
          fb:"On rapporte sans se porter garant."},
         {q:"Combien de connecteurs de point de vue par phrase ?", opts:["un","deux ou trois"], ok:0,
          fb:"Un seul. Les empiler affaiblit."},
         {q:"« À mon avis, l'incendie a fait six sinistrés » est…", opts:["correct","mal employé"], ok:1,
          fb:"C'est un fait : il n'a pas besoin d'être présenté comme un avis."},
       ]},

      {t:'revoir', h:"À retenir",
       p:"Un avis annoncé se discute ; un avis nu s'attaque. Un seul connecteur par phrase, en tête, suivi d'une virgule — et jamais sur un fait."},
    ]
  },

  t3subst: {
    eye:'Mini-leçon', tit:"Reprendre un mot sans le redire",
    blocs:[
      {t:'texte', h:"Ce qui sépare un texte d'une liste",
       p:"« Ma laveuse a brisé. Ma laveuse avait trois ans. J'ai appelé le marchand de la laveuse. » Trois phrases justes, et un texte qu'on ne lit pas. Le français lie ses phrases en reprenant autrement ce dont il vient de parler — c'est ce qui donne l'impression que le texte avance au lieu de tourner en rond.",
       note:"Le programme du niveau 6 nomme ces procédés : synonymie, antonymie, nominalisation, champ lexical, substitution lexicale."},

      {t:'ana', h:"Par un synonyme, ou par un mot plus général",
       p:"Le procédé le plus simple, et le plus employé dans les journaux.",
       mots:[['Un synonyme','la laveuse → l\'<b>appareil</b> → la <b>machine</b>'],
             ['Un mot plus général','une laveuse, une sécheuse → ces <b>électroménagers</b> → ces <b>objets</b>', true],
             ['Un synonyme de verbe','causer → <b>provoquer</b> · choisir → <b>opter pour</b> · réussir / <b>échouer</b>'],
             ['Le sens monte d\'un cran','et le lecteur suit sans effort, parce que le premier mot est encore frais']],
       say:"la laveuse, l'appareil, la machine",
       note:"Attention à ne pas monter trop haut trop vite : « la chose » après « la laveuse » perd le lecteur."},

      {t:'ana', h:"Par un nom tiré du verbe — la nominalisation",
       p:"L'action de la phrase précédente devient le sujet de la suivante.",
       mots:[['Le marchand a refusé.','Devant ce <b>refus</b>, j\'ai écrit à l\'Office.'],
             ['J\'ai demandé une réparation.','Ma <b>demande</b> est restée sans réponse.', true],
             ['Le technicien est venu deux fois.','Cette <b>visite</b> n\'a rien réglé.'],
             ['Les suffixes qui reviennent','-tion (réparer / réparation) · -ment (rembourser / remboursement) · -ure (ouvrir / ouverture)']],
       say:"Le marchand a refusé. Devant ce refus, j'ai écrit à l'Office.",
       note:"C'est le procédé le plus élégant, et celui qui fait le plus « écrit ». Les titres de journaux en vivent."},

      {t:'ana', h:"Par un déterminant",
       p:"Le plus économique : on garde le mot et on change ce qui est devant.",
       mots:[['Démonstratif','J\'ai écrit une lettre. <b>Cette</b> lettre est restée sans réponse.'],
             ['Possessif','J\'ai écrit une lettre. <b>Ma</b> lettre est restée sans réponse.', true],
             ['Défini','J\'ai acheté une laveuse. <b>La</b> laveuse a brisé après trois ans.'],
             ['Le signal','un déterminant démonstratif dit toujours : on en a déjà parlé']],
       say:"J'ai écrit une lettre. Cette lettre est restée sans réponse.",
       note:"À la lecture, « ce », « cette », « ces » sont des flèches qui pointent en arrière. Suivez-les."},

      {t:'ex', h:"Six reprises, tirées du module",
       p:"À gauche la première phrase, à droite la reprise.",
       rows:[
         ["Ma laveuse a brisé.","Cette machine avait trois ans."],
         ["Le marchand a refusé.","Devant ce refus, j'ai écrit."],
         ["J'ai demandé une réparation.","Ma demande est restée sans réponse."],
         ["Le technicien est venu deux fois.","Cette visite n'a rien réglé."],
         ["Le feu a détruit deux logements.","Cet incendie a fait six sinistrés."],
         ["Elle a choisi d'écrire.","Elle a opté pour la lettre."],
       ]},

      {t:'piege', h:"Trois pièges",
       rows:[
         ["prendre un synonyme approximatif","vérifier qu'il dit la même chose",
          "« Réparer » et « remplacer » ne sont pas synonymes — et c'est justement la question de tout ce module."],
         ["monter trop vite au mot général","garder un cran d'écart",
          "« Ma laveuse a brisé. La chose avait trois ans. » ❌ Le lecteur ne suit plus."],
         ["reprendre un mot dont on n'a pas parlé","introduire d'abord",
          "« Cette visite n'a rien réglé » ❌ si aucune visite n'a été mentionnée avant. Un démonstratif pointe en arrière : il faut qu'il y ait quelque chose derrière."],
       ]},

      {t:'check', h:"Est-ce que c'est clair maintenant ?",
       p:"Quatre questions rapides.",
       qs:[
         {q:"« Le marchand a refusé. Devant ce ___ … »", opts:["refus","refusement"], ok:0,
          fb:"Le nom de « refuser » est « refus », sans suffixe."},
         {q:"« Cette machine » après « ma laveuse » est…", opts:["une reprise par mot général","une répétition"], ok:0,
          fb:"On monte d'un cran, et le lecteur suit."},
         {q:"Un déterminant démonstratif signale…", opts:["une nouveauté","qu'on en a déjà parlé"], ok:1,
          fb:"« ce », « cette », « ces » pointent toujours en arrière."},
         {q:"« Réparer » et « remplacer » sont…", opts:["synonymes","deux choses différentes"], ok:1,
          fb:"C'est toute la question du module : la garantie légale vise la réparation."},
       ]},

      {t:'revoir', h:"À retenir",
       p:"Quatre façons de ne pas répéter : un <b>synonyme</b>, un <b>mot plus général</b>, un <b>nom tiré du verbe</b>, un <b>déterminant démonstratif</b>. Choisissez-en une, pas quatre dans la même phrase."},
    ]
  },

};
