const PLUS = {

  prReg: {
    eye:'Mini-leçon', tit:"Quatre façons de dire la même chose",
    blocs:[
      {t:'texte', h:"Ce n'est pas une échelle du bien au mal",
       p:"On croit souvent qu'il y a une bonne façon de parler et des façons fautives. C'est faux, et c'est même l'inverse : chaque registre est juste à sa place et faux ailleurs. Dire « l'auditoire a répondu avec chaleur » à sa voisine dans l'autobus sonne aussi étrange que dire « c'était plate » dans un procès-verbal.",
       note:"Un adulte qui apprend le français au Québec entend surtout du familier, et écrit surtout du standard. C'est l'écart entre les deux qui demande du travail."},

      {t:'ana', h:"Le familier — entre gens qui se connaissent",
       p:"À la maison, à la pause, entre collègues du même rang. Phrases courtes, mots raccourcis, tutoiement.",
       mots:[['Ce qui se dit','« C\'était plate. » · « Y a des bouts où j\'ai décroché. » · « Ça m\'a fait capoter. »'],['Les signes','le « ne » disparaît, « il y a » devient « y a », les mots se coupent'],['Où','corridor, pause, souper de famille']],
       say:"C'était plate. Y a des bouts où j'ai décroché. Ça m'a fait capoter.",
       note:"Le familier n'est pas du mauvais français : c'est du français qui suppose qu'on se connaît."},

      {t:'ana', h:"Le standard — avec presque tout le monde",
       p:"Au travail, avec un commerçant, dans une réunion ordinaire. C'est le registre par défaut, celui qui ne choque nulle part.",
       mots:[['Ce qui se dit','« Je n\'ai pas trouvé le temps long. » · « J\'ai perdu le fil deux ou trois fois. » · « La salle a beaucoup ri. »'],['Les signes','phrases complètes, « ne » présent, vocabulaire courant'],['Où','réunion, comptoir, courriel de travail']],
       say:"Je n'ai pas trouvé le temps long. J'ai perdu le fil deux ou trois fois.",
       note:"Si vous hésitez, c'est celui-là. On ne se trompe jamais gravement en parlant standard."},

      {t:'ana', h:"Le soutenu — à l'écrit, et devant un auditoire",
       p:"Dans un compte rendu, une critique, une lettre officielle, un exposé. Vocabulaire choisi, phrases construites, aucune familiarité.",
       mots:[['Ce qu\'on lit','« Le rythme m\'a paru lent par moments. » · « Mon attention a fléchi. » · « L\'auditoire a répondu avec chaleur. »'],['Les signes','mots plus rares, tournures impersonnelles, aucune contraction'],['Où','compte rendu, critique de journal, lettre']],
       say:"Le rythme m'a paru lent par moments. Mon attention a fléchi.",
       note:"Attention : soutenu ne veut pas dire compliqué. Une phrase soutenue reste claire, sinon elle a raté son but."},

      {t:'labo', h:"Le même avis, dans les trois registres",
       p:"Choisissez une idée et un registre.",
       axes:[
         {id:'i', lbl:'Quel jugement ?', opts:[['a','le film est lent'],['b','la salle a ri'],['c','la fin m\'a touchée']]},
         {id:'r', lbl:'Devant qui ?', opts:[['1','familier'],['2','standard'],['3','soutenu']]}],
       out:{
         a1:{w:["C'était donc ben long."], say:"C'était donc ben long.", n:'entre collègues, à la pause'},
         a2:{w:["J'ai trouvé le début un peu long."], say:"J'ai trouvé le début un peu long.", n:'en réunion'},
         a3:{w:["Le rythme du premier quart d'heure m'a paru lent."], say:"Le rythme du premier quart d'heure m'a paru lent.", n:'au compte rendu'},
         b1:{w:["Le monde a ri en masse."], say:"Le monde a ri en masse.", n:'familier, très québécois'},
         b2:{w:["La salle a beaucoup ri."], say:"La salle a beaucoup ri.", n:'standard, passe partout'},
         b3:{w:["L'auditoire a répondu avec chaleur."], say:"L'auditoire a répondu avec chaleur.", n:'soutenu, pour un écrit'},
         c1:{w:["La fin, ça m'a virée à l'envers."], say:"La fin, ça m'a virée à l'envers.", n:'familier'},
         c2:{w:["J'ai été très touchée par la fin."], say:"J'ai été très touchée par la fin.", n:'standard'},
         c3:{w:["Cette dernière scène m'a profondément émue."], say:"Cette dernière scène m'a profondément émue.", n:'soutenu'},
       },
       note:"Trois habits, un seul corps : l'avis ne change pas d'un bouton."},

      {t:'ex', h:"Six paires à connaître",
       p:"À gauche ce qu'on dit, à droite ce qu'on écrit.",
       rows:[
         ["c'est plate","le rythme m'a paru lent"],
         ["j'ai décroché","mon attention a fléchi"],
         ["en masse","beaucoup, considérablement"],
         ["le monde","les gens, le public, l'auditoire"],
         ["ça m'a fait capoter","cela m'a beaucoup impressionnée"],
         ["y a un bout où…","il y a un passage où…"],
       ]},

      {t:'piege', h:"Trois pièges de registre",
       rows:[
         ["mélanger deux registres dans la même phrase","tenir un seul registre du début à la fin",
          "« L'auditoire a répondu avec chaleur, c'était vraiment le fun » : la deuxième moitié détruit la première. Choisissez avant de commencer la phrase, pas au milieu."],
         ["croire que le soutenu impressionne","choisir le registre de la situation",
          "Employer du soutenu à la pause fait rire, et pas de la bonne façon. Le registre juste est celui que la situation demande, jamais le plus haut."],
         ["éviter le familier par prudence","le comprendre, même sans l'employer",
          "Vous n'êtes pas obligé de dire « en masse ». Mais si vous ne le comprenez pas, vous perdez la moitié de ce qui se dit autour de vous au travail."],
       ]},

      {t:'check', h:"Est-ce que c'est clair maintenant ?",
       p:"Quatre situations, un registre chacune.",
       qs:[
         {q:"Vous écrivez le compte rendu du comité. Vous employez…", opts:["le familier","le standard ou le soutenu"], ok:1,
          fb:"Un écrit qui sera lu par huit personnes ne se rédige pas comme un message à sa sœur."},
         {q:"« Y a des bouts où j'ai décroché » est…", opts:["familier","soutenu"], ok:0,
          fb:"« Y a » pour « il y a », « des bouts » pour « des passages » : deux signes du familier."},
         {q:"Devant la classe, pour votre exposé, vous visez…", opts:["le standard","le familier"], ok:0,
          fb:"Le standard : complet, clair, sans familiarité, mais sans raideur non plus."},
         {q:"Employer le soutenu à la pause-café, c'est…", opts:["une erreur de registre","toujours mieux"], ok:0,
          fb:"Le registre le plus haut n'est pas le meilleur : c'est celui qui convient qui l'est."},
       ]},

      {t:'revoir', h:"À retenir",
       p:"<b>Familier</b> entre proches, <b>standard</b> presque partout, <b>soutenu</b> à l'écrit et devant un auditoire. L'avis reste le même ; seule la façon de le dire change. En cas de doute, le standard."},
    ]
  },

  prAvis: {
    eye:'Mini-leçon', tit:"Un goût, un avis, un argument",
    blocs:[
      {t:'texte', h:"Trois mots qu'on confond, et une réunion perdue",
       p:"« J'aime pas ça » ferme la porte. « Le film est lent » l'entrouvre. « Le film est assez lent pour que la moitié de la salle décroche » la tient ouverte. Les trois phrases viennent de la même personne et disent la même préférence : une seule permet de continuer à parler.",
       note:"Ce n'est pas une question de politesse. C'est une question de ce que l'autre peut faire de votre phrase."},

      {t:'ana', h:"Le goût — vrai pour vous, et fermé",
       p:"Il porte sur vous, pas sur l'œuvre. Personne ne peut le contredire, et personne ne peut le reprendre non plus.",
       mots:[['On l\'entend ainsi','« Moi, l\'humour, j\'embarque jamais. » · « C\'est ma chanson préférée. »'],['Le signe','le sujet est « moi », « je », et il n\'y a pas de parce que'],['La réponse possible','« ah bon »']],
       say:"Moi, l'humour, j'embarque jamais. C'est ma chanson préférée.",
       note:"Un goût n'est pas une faute. Mais dans un comité, il ne compte pas."},

      {t:'ana', h:"L'avis — il porte sur l'œuvre",
       p:"Il dit quelque chose de l'œuvre elle-même, que d'autres personnes ont vue aussi.",
       mots:[['On l\'entend ainsi','« Le premier quart d\'heure est lent. » · « Le refrain monte trop haut. »'],['Le signe','le sujet est l\'œuvre ou une de ses parties'],['La réponse possible','« oui » ou « non, regarde… »']],
       say:"Le premier quart d'heure est lent. Le refrain monte trop haut.",
       note:"À ce stade, on peut être d'accord ou pas. C'est ce qu'on veut."},

      {t:'ana', h:"L'argument — l'avis plus sa raison vérifiable",
       p:"Il ajoute le pourquoi, appuyé sur un fait que les autres peuvent aller vérifier.",
       mots:[['On l\'entend ainsi','« Le début est lent : aucune parole n\'est échangée avant la douzième minute. »'],['Le signe','un chiffre, un moment, une scène nommée'],['La réponse possible','on peut aller compter']],
       say:"Le début est lent : aucune parole n'est échangée avant la douzième minute.",
       note:"C'est le seul des trois qui déplace une réunion."},

      {t:'ex', h:"Trois montées, du goût à l'argument",
       p:"La même personne, trois fois, de plus en plus utile.",
       rows:[
         ["J'aime pas les films tranquilles.","je décroche quand une scène dure plus de trois minutes sans parole"],
         ["Le spectacle est bon.","on a ri deux fois en six minutes, mais jamais aux mêmes endroits"],
         ["La chanson est belle.","le refrain revient quatre fois et il change de sens chaque fois"],
       ]},

      {t:'labo', h:"Transformer un goût en argument",
       p:"Choisissez une œuvre et un niveau.",
       axes:[
         {id:'o', lbl:'Laquelle des trois ?', opts:[['a','le sketch'],['b','la chanson'],['c','le film']]},
         {id:'n', lbl:'Goût, ou argument ?', opts:[['1','un goût'],['2','un argument']]}],
       out:{
         a1:{w:["Moi, ça me fait pas rire."], say:"Moi, ça me fait pas rire.", n:'rien à répondre'},
         a2:{w:["L'ironie demande qu'on rétablisse tout seul, et la moitié du groupe ne le fera pas."], say:"L'ironie demande qu'on rétablisse tout seul, et la moitié du groupe ne le fera pas.", n:'discutable, donc utile'},
         b1:{w:["J'aime pas sa voix."], say:"J'aime pas sa voix.", n:'rien à répondre'},
         b2:{w:["Le refrain monte trop haut pour elle, et elle le manque une fois sur trois."], say:"Le refrain monte trop haut pour elle, et elle le manque une fois sur trois.", n:'vérifiable'},
         c1:{w:["C'est plate, un film."], say:"C'est plate, un film.", n:'rien à répondre'},
         c2:{w:["Le premier quart d'heure ne contient aucune parole, et c'est long pour un groupe."], say:"Le premier quart d'heure ne contient aucune parole, et c'est long pour un groupe.", n:'on peut aller compter'},
       },
       note:"Passer du premier au second coûte une phrase, et rapporte toute la réunion."},

      {t:'piege', h:"Trois pièges",
       rows:[
         ["donner son goût en croyant donner un avis","ajouter le pourquoi et un moment",
          "« C'est bon » sonne comme un jugement, mais rien ne s'y accroche. Quiconque n'est pas d'accord n'a qu'à dire « moi non », et vous êtes à égalité de rien du tout."],
         ["empiler cinq raisons","en donner une, précise",
          "Cinq raisons molles se réfutent une par une. Une raison appuyée sur un moment que tout le monde a vu tient toute seule."],
         ["donner son avis pour un fait","l'annoncer comme un avis",
          "« Ce film est ennuyant » ferme la discussion et braque. « J'ai trouvé le début long » dit exactement la même chose et laisse à l'autre le droit d'avoir vu autre chose."],
       ]},

      {t:'check', h:"Est-ce que c'est clair maintenant ?",
       p:"Quatre phrases, un classement chacune.",
       qs:[
         {q:"« Le refrain revient quatre fois. » C'est…", opts:["un fait","un goût"], ok:0,
          fb:"On peut compter. C'est un fait, et il peut servir d'appui."},
         {q:"« Moi, j'haïs ça, les longs métrages. » C'est…", opts:["un goût","un argument"], ok:0,
          fb:"Vrai pour la personne, et rien à y répondre."},
         {q:"Ce qui manque le plus souvent à un avis, c'est…", opts:["le moment précis","la politesse"], ok:0,
          fb:"Le troisième morceau est presque toujours celui qu'on oublie."},
         {q:"« J'ai trouvé le début long » plutôt que « le début est long » sert à…", opts:["annoncer que c'est un avis","être plus poli"], ok:0,
          fb:"Ce n'est pas de la politesse : c'est dire d'où l'on parle."},
       ]},

      {t:'revoir', h:"À retenir",
       p:"Un <b>goût</b> parle de vous. Un <b>avis</b> parle de l'œuvre. Un <b>argument</b> parle de l'œuvre et donne un moment que tout le monde peut aller voir. Autour d'une table, seul le troisième fait bouger quelque chose."},
    ]
  },

  t1trans: {
    eye:'Mini-leçon', tit:"Lire un sketch pour voir comment il est fait",
    blocs:[
      {t:'texte', h:"Pourquoi on transcrit une chose qui se dit",
       p:"Un sketch transcrit ne fait plus rire, et c'est exactement ce qu'on cherche. Une fois le ton, le silence et la salle enlevés, il ne reste que les mots — et l'on voit enfin où le procédé se trouve. C'est un peu comme regarder une maison sans son revêtement : ce n'est plus beau, mais on comprend comment elle tient.",
       note:"C'est aussi la seule façon de citer un passage précis dans un commentaire : « quand il dit que la pièce est heureuse dans le système »."},

      {t:'ana', h:"Premier repérage : ce que personne ne peut croire",
       p:"Une phrase que nul ne dirait sérieusement est presque toujours l'endroit du procédé.",
       mots:[['Dans le sketch','« J\'adore ça, attendre. » · « Elle est heureuse, dans le système. »'],['La question à se poser','qui pourrait dire cela sérieusement ?'],['Ce qu\'on trouve','l\'ironie, l\'exagération, la personnification']],
       say:"J'adore ça, attendre. Elle est heureuse, dans le système.",
       note:"Le français ne marque pas l'ironie à l'écrit : ni ponctuation, ni mot. C'est le contenu, et lui seul, qui prévient."},

      {t:'ana', h:"Le repérage 2 — suivez les changements de voix",
       p:"Deux-points, guillemets, « il dit », « je lui réponds » : chaque fois, une autre personne parle par la bouche de l'humoriste.",
       mots:[['Dans le sketch','elle me dit : « Monsieur… » · je lui réponds : « Madame… » · il dit : « C\'est dans le système. »'],['Combien','trois voix en six lignes'],['Pourquoi','le comique vient du passage d\'une voix à l\'autre']],
       say:"Elle me dit : Monsieur, ça fait quarante minutes.",
       note:"Comptez-les : un bon sketch en contient beaucoup plus qu'on ne croit."},

      {t:'ana', h:"Le repérage 3 — la chute est la dernière phrase",
       p:"Elle ferme l'histoire, elle est courte, et rien ne vient après elle.",
       mots:[['La première chute','« Madame, moi ça fait trente ans. »'],['La chute finale','« Je pense qu\'il est au deuxième, derrière la porte barrée. »'],['Le signe','on n\'explique jamais une chute']],
       say:"Madame, moi ça fait trente ans.",
       note:"Un sketch contient plusieurs petites chutes et une grande, à la toute fin."},

      {t:'ex', h:"Quatre passages, quatre procédés",
       p:"À gauche le passage, à droite ce qu'il fait.",
       rows:[
         ["J'adore ça, attendre.","dit le contraire de ce qu'il pense"],
         ["une chemise bleue, un écran, une phrase toute faite","garde trois traits et jette le reste"],
         ["Elle est heureuse, dans le système.","donne une vie à une pièce d'entrepôt"],
         ["derrière la porte qui est toujours barrée","pousse l'idée jusqu'à l'impossible"],
       ]},

      {t:'piege', h:"Deux pièges de lecture",
       rows:[
         ["prendre l'ironie au premier degré","chercher ce qui ne peut pas être vrai",
          "C'est ce que fait Gaétan : « il vient de le dire ». Oui, il l'a dit — et non, il ne le pense pas. Le français écrit ne le signale nulle part : c'est à vous de rétablir."],
         ["chercher la chute au milieu","la chercher à la fin",
          "Un sketch qui ne fait pas rire à la troisième ligne n'a pas raté. Il n'est pas fini. Lisez jusqu'au point final avant de juger."],
       ]},

      {t:'check', h:"Est-ce que c'est clair maintenant ?",
       p:"Trois questions sur la lecture d'un sketch.",
       qs:[
         {q:"Comment le français écrit signale-t-il l'ironie ?", opts:["il ne la signale pas","par un point d'exclamation"], ok:0,
          fb:"Aucun signe. C'est le contenu invraisemblable qui prévient."},
         {q:"Où se trouve la chute ?", opts:["à la fin","au milieu"], ok:0,
          fb:"Toujours à la fin, et jamais expliquée."},
         {q:"« Il dit : “C'est dans le système.” » est…", opts:["une parole rapportée mot pour mot","une invention de l'humoriste"], ok:0,
          fb:"Deux-points et guillemets : ce sont les mots exacts, du moins il le prétend."},
       ]},

      {t:'revoir', h:"À retenir",
       p:"Trois repères pour lire un sketch : ce qui <b>ne peut pas être vrai</b> (le procédé), les <b>changements de voix</b> (les paroles rapportées), et la <b>dernière phrase</b> (la chute). Le reste est du décor, et le décor est utile aussi."},
    ]
  },

  t1proc: {
    eye:'Mini-leçon', tit:"Nommer ce qui fait rire",
    blocs:[
      {t:'texte', h:"Pourquoi il faut des noms",
       p:"« C'était drôle » n'apprend rien. « Il fonctionne par ironie d'un bout à l'autre » dit quelque chose de vrai sur le spectacle, et prévient qui a besoin de l'être. Ces six mots sont ceux du programme, et ce sont ceux qu'emploient les gens qui parlent d'humour au Québec.",
       note:"Ils ne servent pas à faire savant : ils servent à prévenir un groupe de trente-huit personnes de ce qui l'attend."},

      {t:'ana', h:"L'ironie et le sarcasme — deux voisins, un fossé",
       p:"Tous deux disent le contraire de ce qu'ils pensent. La différence est dans la cible.",
       mots:[['L\'ironie','« J\'adore attendre. » Elle vise une situation. Personne n\'est blessé.'],['Le sarcasme','« Bravo, tu as encore trouvé le moyen d\'être en retard. » Il vise une personne, et il veut faire mal.'],['Le repère','demandez-vous qui reçoit le coup']],
       say:"L'ironie vise une situation. Le sarcasme vise une personne.",
       note:"Le sketch de Réjean Cadorette est ironique et jamais sarcastique : il ne s'en prend à personne, pas même au gérant."},

      {t:'ana', h:"La caricature — deux traits, et le reste à la poubelle",
       p:"On ne copie pas quelqu'un : on choisit deux ou trois choses et on les grossit.",
       mots:[['Les trois traits du gérant','l\'écran, la chemise bleue, la phrase toute faite'],['Ce qui est jeté','tout le reste de la personne'],['La limite','on caricature une fonction, pas une personne réelle']],
       say:"L'écran, la chemise bleue, et la phrase toute faite.",
       note:"C'est ce qui permet à chacun de reconnaître son propre patron sans que personne ne soit visé."},

      {t:'ana', h:"Le burlesque et l'absurde",
       p:"Le premier fait rire par le corps, le second par une idée qui ne tient plus debout.",
       mots:[['Burlesque','la chute, l\'objet qui casse, le geste maladroit, la poursuite'],['Absurde','« le système est au deuxième, derrière la porte barrée »'],['Ce qui les sépare','l\'un se voit, l\'autre se pense']],
       say:"Le burlesque se voit. L'absurde se pense.",
       note:"Le burlesque traverse toutes les langues ; l'absurde demande de comprendre chaque mot. Pour un groupe mêlé, ce n'est pas indifférent."},

      {t:'ana', h:"L'autodérision — rire de soi en premier",
       p:"Se moquer de soi-même avant que quiconque n'en ait l'idée. C'est ce que fait un humoriste qui parle de ses trente ans de comptoir.",
       mots:[['Dans le sketch','« Trente ans, j\'ai cherché le système. Je ne l\'ai jamais trouvé. »'],['L\'effet','le public se met de son côté'],['Le risque','aucun, et c\'est pourquoi tant de gens l\'emploient']],
       say:"Trente ans, j'ai cherché le système. Je ne l'ai jamais trouvé.",
       note:"C'est aussi ce qui autorise la caricature du gérant : il s'est mis lui-même dans le tas d'abord."},

      {t:'labo', h:"Le procédé et sa phrase",
       p:"Choisissez un ressort comique, puis un exemple.",
       axes:[
         {id:'p', lbl:'Quel ressort comique ?', opts:[['a','ironie'],['b','caricature'],['c','absurde'],['d','autodérision']]},
         {id:'n', lbl:'Lequel des deux ?', opts:[['1','le premier'],['2','le second']]}],
       out:{
         a1:{w:["J'adore ça, attendre."], say:"J'adore ça, attendre.", n:'il déteste, et tout le monde le sait'},
         a2:{w:["On appelle ça le service à la clientèle."], say:"On appelle ça le service à la clientèle.", n:'le nom officiel contre la réalité'},
         b1:{w:["Un jeune homme très bien, très propre, une chemise bleue."], say:"Un jeune homme très bien, très propre, une chemise bleue.", n:'trois traits, rien d\'autre'},
         b2:{w:["Il regarde son écran, puis il dit : c'est dans le système."], say:"Il regarde son écran, puis il dit : c'est dans le système.", n:'un geste et une formule'},
         c1:{w:["Elle est heureuse, dans le système."], say:"Elle est heureuse, dans le système.", n:'une pièce qui a une vie'},
         c2:{w:["Je pense qu'il est au deuxième, derrière la porte barrée."], say:"Je pense qu'il est au deuxième, derrière la porte barrée.", n:'un lieu pour une abstraction'},
         d1:{w:["Trente ans au comptoir des pièces. Trente ans."], say:"Trente ans au comptoir des pièces. Trente ans.", n:'il commence par se placer bas'},
         d2:{w:["Je l'ai cherché, je ne l'ai jamais trouvé."], say:"Je l'ai cherché, je ne l'ai jamais trouvé.", n:'il se donne le mauvais rôle'},
       },
       note:"Le sketch en emploie quatre en six minutes, et jamais le sarcasme."},

      {t:'piege', h:"Deux pièges",
       rows:[
         ["appeler sarcasme toute moquerie","réserver sarcasme à ce qui blesse",
          "Un spectacle entier peut être ironique sans un seul sarcasme. Confondre les deux fait dire d'un humoriste doux qu'il est méchant."],
         ["croire que caricature veut dire dessin","garder le sens large",
          "En français, la caricature est d'abord une manière de représenter : elle vaut pour un dessin, une imitation, une description en trois mots."],
       ]},

      {t:'check', h:"Est-ce que c'est clair maintenant ?",
       p:"Quatre phrases à classer.",
       qs:[
         {q:"« J'adore attendre », dit par quelqu'un qui déteste attendre, c'est…", opts:["de l'ironie","du sarcasme"], ok:0,
          fb:"Ça vise une situation, pas une personne."},
         {q:"Garder l'écran, la chemise et la phrase toute faite, c'est…", opts:["une caricature","de l'absurde"], ok:0,
          fb:"Deux ou trois traits grossis, le reste jeté."},
         {q:"Chercher pendant trente ans un système qui serait « derrière une porte barrée », c'est…", opts:["de l'absurde","du burlesque"], ok:0,
          fb:"Une idée poussée jusqu'où plus rien ne tient. Rien à voir avec le corps."},
         {q:"Un humoriste qui se donne le mauvais rôle pratique…", opts:["l'autodérision","le sarcasme"], ok:0,
          fb:"Il rit de lui-même en premier, et le public se range de son côté."},
       ]},

      {t:'revoir', h:"À retenir",
       p:"<b>Ironie</b> : contre une situation. <b>Sarcasme</b> : contre une personne, et ça fait mal. <b>Caricature</b> : deux traits grossis. <b>Burlesque</b> : le corps. <b>Absurde</b> : l'idée qui ne tient plus. <b>Autodérision</b> : rire de soi d'abord."},
    ]
  },

  t1inc: {
    eye:'Mini-leçon', tit:"« dit-il » — le verbe passe devant",
    blocs:[
      {t:'texte', h:"Une inversion, et rien d'autre",
       p:"L'incise est le petit morceau qui dit qui parle : <i>dit-elle</i>, <i>répondis-je</i>, <i>reprend le gérant</i>. Elle se glisse après les paroles rapportées, ou au milieu, toujours entre virgules. Sa seule particularité est que le sujet y passe après le verbe — c'est la seule inversion obligatoire du français ordinaire, avec la question.",
       note:"Sans les incises, un dialogue rapporté devient illisible au bout de trois répliques."},

      {t:'ana', h:"Avec un pronom : trait d'union",
       p:"Le pronom sujet se colle au verbe par un trait d'union.",
       mots:[['On écrit','dit-<b>elle</b> · répond-<b>il</b> · demandai-<b>je</b> · ajoutons-<b>nous</b>'],['Ce qui bouge','le sujet passe derrière'],['Le signe','le trait d\'union, jamais l\'espace seule']],
       say:"dit-elle, répond-il, demandai-je",
       note:"Le trait d'union n'est pas décoratif : sans lui, la phrase se lit comme un ordre."},

      {t:'ana', h:"Le -t- de liaison",
       p:"Quand le verbe finit par une voyelle et que le sujet est <i>il</i>, <i>elle</i> ou <i>on</i>, on glisse un t entre deux traits d'union.",
       mots:[['On écrit','répond<b>-t-il</b> · demanda<b>-t-elle</b> · pensa<b>-t-on</b> · ajoute<b>-t-elle</b>'],['Pourquoi','deux voyelles ne se suivent pas'],['Attention','ce t ne veut rien dire : il sert seulement à séparer']],
       say:"répond-t-il, demanda-t-elle, pensa-t-on",
       note:"On l'appelle un « t euphonique » : il est là pour l'oreille."},

      {t:'ana', h:"Avec un nom : pas de trait d'union",
       p:"Si le sujet est un groupe du nom, il passe aussi derrière, mais sans trait d'union.",
       mots:[['On écrit','reprend <b>le gérant</b> · murmure <b>Marilou</b> · ajoute <b>la conseillère</b>'],['Pas de trait d\'union','le trait d\'union est réservé aux pronoms'],['Le verbe reste devant','c\'est la règle commune aux deux cas']],
       say:"reprend le gérant, murmure Marilou",
       note:"Un nom propre s'y met très bien : « dit Ghyslaine » est parfaitement correct."},

      {t:'ana', h:"Les verbes qui s'emploient en incise",
       p:"Ce sont les verbes de parole, et un intrus.",
       mots:[['Les courants','dire, répondre, demander, ajouter, reprendre, crier, murmurer, songer'],['L\'intrus','<b>faire</b>, qui veut alors dire « dire » : « Bien sûr », fit-il.'],['Ce qui ne s\'y met pas','les verbes qui ne disent rien : marcher, ouvrir, regarder']],
       say:"Bien sûr, fit-il.",
       note:"« Fit-il » est un peu littéraire ; à l'oral, on dit « qu'il fait »."},

      {t:'labo', h:"Transformer une phrase en incise",
       p:"Choisissez un sujet et un verbe.",
       axes:[
         {id:'s', lbl:'Qui parle ?', opts:[['a','elle'],['b','il'],['c','le gérant']]},
         {id:'v', lbl:'Quel verbe de parole ?', opts:[['1','dire'],['2','répondre'],['3','ajouter']]}],
       out:{
         a1:{w:["dit-elle"], say:"dit-elle", n:'pas de -t-, le verbe finit par une consonne'},
         a2:{w:["répond-elle"], say:"répond-elle", n:'le d se prononce comme un t'},
         a3:{w:["ajoute-t-elle"], say:"ajoute-t-elle", n:'le verbe finit par une voyelle : -t-'},
         b1:{w:["dit-il"], say:"dit-il", n:'la liaison se fait toute seule'},
         b2:{w:["répond-il"], say:"répond-il", n:'même chose'},
         b3:{w:["ajoute-t-il"], say:"ajoute-t-il", n:'voyelle plus il : -t- obligatoire'},
         c1:{w:["dit le gérant"], say:"dit le gérant", n:'un nom : pas de trait d\'union'},
         c2:{w:["répond le gérant"], say:"répond le gérant", n:'idem'},
         c3:{w:["ajoute le gérant"], say:"ajoute le gérant", n:'aucun -t- non plus'},
       },
       note:"Le -t- n'apparaît qu'avec il, elle ou on, et seulement après une voyelle."},

      {t:'ex', h:"Six incises du module",
       p:"À gauche l'ordre ordinaire, à droite l'incise.",
       rows:[
         ["elle dit","dit-elle"],
         ["je réponds","répondis-je"],
         ["il ajoute","ajoute-t-il"],
         ["elle demande","demande-t-elle"],
         ["le gérant reprend","reprend le gérant"],
         ["on pense","pense-t-on"],
       ]},

      {t:'piege', h:"Trois pièges",
       rows:[
         ["garder l'ordre normal","inverser toujours",
          "« Ça fait quarante minutes », elle dit. Non : « dit-elle ». L'incise n'accepte pas l'ordre sujet-verbe, jamais."],
         ["oublier le -t-","le mettre dès qu'il y a deux voyelles",
          "« ajoute-elle » n'existe pas. Dès que le verbe finit par une voyelle et que le sujet est il, elle ou on : -t-."],
         ["mettre un trait d'union avec un nom","le réserver aux pronoms",
          "« dit-le gérant » est faux. Le trait d'union relie un verbe à un pronom, jamais à un nom."],
       ]},

      {t:'check', h:"Est-ce que c'est clair maintenant ?",
       p:"Quatre formes à trancher.",
       qs:[
         {q:"« Ça fait trente ans », ___ (je réponds)", opts:["répondis-je","je réponds"], ok:0,
          fb:"Le verbe passe devant, trait d'union avec le pronom."},
         {q:"« C'est dans le système », ___ (il ajoute)", opts:["ajoute-t-il","ajoute-il"], ok:0,
          fb:"Le verbe finit par une voyelle : le t est obligatoire."},
         {q:"« Je vérifie », ___ (le gérant reprend)", opts:["reprend le gérant","reprend-le gérant"], ok:0,
          fb:"Un nom ne prend pas de trait d'union."},
         {q:"L'incise est encadrée par…", opts:["des virgules","des parenthèses"], ok:0,
          fb:"Virgules avant et après, quand elle est au milieu."},
       ]},

      {t:'revoir', h:"À retenir",
       p:"Dans une incise, le <b>verbe passe devant le sujet</b>. Avec un pronom : <b>trait d'union</b>, et un <b>-t-</b> si le verbe finit par une voyelle devant <i>il, elle, on</i>. Avec un nom : rien du tout, juste l'inversion."},
    ]
  },

  t1guil: {
    eye:'Mini-leçon', tit:"Ses mots, ou les vôtres ?",
    blocs:[
      {t:'texte', h:"Une promesse faite au lecteur",
       p:"Ouvrir des guillemets, c'est promettre que ce sont exactement ces mots-là. Écrire « il a dit que… », c'est promettre seulement le contenu. Les deux sont honnêtes ; ce qui ne l'est pas, c'est de mettre entre guillemets une phrase qu'on a arrangée.",
       note:"Dans un compte rendu de réunion, cette différence compte : une citation engage la personne citée."},

      {t:'ana', h:"Le discours direct — deux-points, guillemets, majuscule",
       p:"On annonce, on ouvre, on cite, on ferme.",
       mots:[['La ponctuation','Il dit<b> : « </b>C\'est dans le système.<b> »</b>'],['Dans l\'ordre','deux-points, espace, guillemet ouvrant, majuscule, point, guillemet fermant'],['Ce que ça promet','les mots exacts']],
       say:"Il dit : C'est dans le système.",
       note:"Au Québec comme en France, on emploie les guillemets français « » avec une espace à l'intérieur."},

      {t:'ana', h:"Le discours rapporté — « que », et rien d'autre",
       p:"On raconte le contenu à sa façon, sans guillemets.",
       mots:[['La forme','Il dit <b>que</b> c\'est dans le système.'],['Le mot obligatoire','<b>que</b> — jamais absent'],['Ce que ça promet','le sens, pas les mots']],
       say:"Il dit que c'est dans le système.",
       note:"Pour une question rapportée, « que » devient « si » : elle demande s'il en reste."},

      {t:'ana', h:"Ce qui bouge quand on passe de l'un à l'autre",
       p:"Trois choses changent, toujours les mêmes.",
       mots:[['Les pronoms','« <b>je</b> reviens » devient qu\'<b>elle</b> revenait'],['Le temps','présent devient imparfait quand le verbe introducteur est au passé'],['Les mots du temps','<b>demain</b> devient <b>le lendemain</b>, <b>hier</b> devient <b>la veille</b>']],
       say:"Elle m'a dit qu'elle revenait le lendemain.",
       note:"C'est ce triple déplacement qui rend le discours rapporté difficile — et qui rend la citation exacte plus sûre."},

      {t:'ex', h:"Cinq paires",
       p:"À gauche les mots exacts, à droite la version rapportée.",
       rows:[
         ["Elle me dit : « Ça fait quarante minutes. »","Elle m'a dit que ça faisait quarante minutes."],
         ["Il dit : « C'est dans le système. »","Il a dit que c'était dans le système."],
         ["Je réponds : « Moi, ça fait trente ans. »","J'ai répondu que ça faisait trente ans pour moi."],
         ["Elle demande : « Est-ce qu'il en reste ? »","Elle a demandé s'il en restait."],
         ["Ghyslaine dit : « Tu rédiges le compte rendu. »","Ghyslaine a dit que je rédigeais le compte rendu."],
       ]},

      {t:'piege', h:"Trois pièges",
       rows:[
         ["arranger une phrase entre guillemets","citer exactement, ou ne pas citer",
          "Si vous n'êtes pas sûr des mots, écrivez « il a dit que ». Des guillemets sur une phrase reconstruite, dans un compte rendu, sont une faute lourde."],
         ["laisser tomber le « que »","le mettre à chaque fois",
          "« Il a dit c'était dans le système » n'existe pas en français. Le que est obligatoire, même quand l'anglais s'en passe."],
         ["garder le « je » du discours direct","déplacer les pronoms",
          "« Elle a dit que je reviens demain » veut dire que c'est vous qui revenez. Le pronom doit suivre celui qui parle."],
       ]},

      {t:'check', h:"Est-ce que c'est clair maintenant ?",
       p:"Quatre transformations.",
       qs:[
         {q:"« Elle m'a dit qu'elle revenait le lendemain » est…", opts:["du discours rapporté","une citation exacte"], ok:0,
          fb:"Pas de guillemets, un « que », des pronoms déplacés."},
         {q:"Quel signe annonce une citation exacte ?", opts:["les deux-points","la virgule"], ok:0,
          fb:"Deux-points, puis guillemets ouvrants."},
         {q:"« Est-ce qu'il en reste ? » rapporté donne…", opts:["elle a demandé s'il en restait","elle a demandé que il en restait"], ok:0,
          fb:"Une question rapportée passe par « si », jamais par « que »."},
         {q:"Dans un compte rendu, citer entre guillemets une phrase reconstruite est…", opts:["une faute","permis si le sens y est"], ok:0,
          fb:"Les guillemets promettent les mots exacts. Sinon, on écrit « que »."},
       ]},

      {t:'revoir', h:"À retenir",
       p:"<b>Deux-points + guillemets</b> = les mots exacts. <b>« que » sans guillemets</b> = le contenu, à votre façon. En passant du premier au second, les <b>pronoms</b>, le <b>temps</b> et les <b>mots du temps</b> se déplacent."},
    ]
  },

  t1emph: {
    eye:'Mini-leçon', tit:"Mettre un mot en avant sans crier",
    blocs:[
      {t:'texte', h:"Le français n'accentue pas, il déplace",
       p:"Dans d'autres langues, il suffit d'appuyer sur un mot pour le mettre en avant. En français, l'accent ne suffit pas : on construit une phrase autour du mot. C'est ce qu'on appelle le clivage, et c'est le geste le plus utile de tout ce module — un avis, c'est une chose qui compte plus que les autres.",
       note:"Le français parlé du Québec en fait un usage constant : « c'est ça que je disais », « c'est lui qui m'a appelée »."},

      {t:'ana', h:"C'est… qui — quand c'est le sujet qui compte",
       p:"On encadre le sujet, et le reste de la phrase suit derrière « qui ».",
       mots:[['Sans mise en avant','Le ton fait rire.'],['La phrase clivée','<b>C\'est le ton qui</b> fait rire.'],['L\'accord','le verbe suit ce qu\'on met en avant : c\'est moi qui <b>ai</b>']],
       say:"C'est le ton qui fait rire.",
       note:"Avec un pluriel, « c'est » devient « ce sont » : ce sont les silences qui font le film."},

      {t:'ana', h:"C'est… que — pour le complément, le lieu, le moment",
       p:"Complément, moment, lieu, manière : tout ce qui n'est pas le sujet passe par « que ».",
       mots:[['Un complément mis en avant','<b>C\'est ce passage que</b> j\'ai préféré.'],['Un moment','<b>C\'est à la fin qu\'</b>il exagère.'],['Un lieu','<b>C\'est dans un sous-sol qu\'</b>elle chante.']],
       say:"C'est à la fin qu'il exagère.",
       note:"Le test : si vous pouvez remplacer par « qui », c'est un sujet ; sinon, c'est « que »."},

      {t:'ana', h:"Ce qui… c'est — pour annoncer avant de livrer",
       p:"On dit d'abord de quoi on va parler, puis on le donne. L'auditoire attend, et il écoute mieux.",
       mots:[['La forme','<b>Ce qui</b> me fait rire, <b>c\'est</b> l\'écart entre la phrase et la vérité.'],['La variante','<b>Ce que</b> je retiens, <b>c\'est</b> la quatrième nuit.'],['Le choix','« ce qui » si c\'est le sujet, « ce que » si c\'est le complément']],
       say:"Ce qui me fait rire, c'est l'écart entre la phrase et la vérité.",
       note:"C'est la forme la plus efficace devant un groupe : elle crée une seconde d'attente."},

      {t:'labo', h:"La même idée, trois mises en relief",
       p:"Choisissez une idée et une forme.",
       axes:[
         {id:'i', lbl:'Quel jugement ?', opts:[['a','le ton fait rire'],['b','j\'ai aimé la quatrième nuit'],['c','Gaétan a le meilleur argument']]},
         {id:'f', lbl:'Quelle mise en avant ?', opts:[['1','phrase ordinaire'],['2','clivée'],['3','annoncée']]}],
       out:{
         a1:{w:["Le ton fait rire."], say:"Le ton fait rire.", n:'rien n\'est mis en avant'},
         a2:{w:["C'est le ton qui fait rire."], say:"C'est le ton qui fait rire.", n:'le sujet est encadré'},
         a3:{w:["Ce qui fait rire, c'est le ton."], say:"Ce qui fait rire, c'est le ton.", n:'on annonce, puis on livre'},
         b1:{w:["J'ai aimé la quatrième nuit."], say:"J'ai aimé la quatrième nuit.", n:'phrase plate'},
         b2:{w:["C'est la quatrième nuit que j'ai aimée."], say:"C'est la quatrième nuit que j'ai aimée.", n:'complément encadré, accord du participe'},
         b3:{w:["Ce que j'ai aimé, c'est la quatrième nuit."], say:"Ce que j'ai aimé, c'est la quatrième nuit.", n:'la forme d\'un exposé'},
         c1:{w:["Gaétan a le meilleur argument."], say:"Gaétan a le meilleur argument.", n:'ordinaire'},
         c2:{w:["C'est Gaétan qui a le meilleur argument."], say:"C'est Gaétan qui a le meilleur argument.", n:'et non quelqu\'un d\'autre'},
         c3:{w:["Celui qui a le meilleur argument, c'est Gaétan."], say:"Celui qui a le meilleur argument, c'est Gaétan.", n:'annonce avec « celui qui »'},
       },
       note:"Les trois disent la même chose. La troisième est celle qu'on retient."},

      {t:'piege', h:"Trois pièges",
       rows:[
         ["c'est moi qui a","c'est moi qui ai",
          "Le pronom « qui » reprend « moi » : le verbe se met à la première personne. C'est la faute la plus fréquente de toute la leçon, et elle s'entend."],
         ["mettre « que » partout","« qui » pour le sujet",
          "« C'est le ton que fait rire » est faux. Le ton fait quelque chose : il est sujet, donc « qui »."],
         ["cliver trois fois de suite","une par idée",
          "Si tout est en avant, plus rien ne l'est. Une mise en relief par idée, et le reste en phrases ordinaires."],
       ]},

      {t:'check', h:"Est-ce que c'est clair maintenant ?",
       p:"Quatre choix.",
       qs:[
         {q:"« C'est moi qui ___ ri le premier. »", opts:["ai","a"], ok:0,
          fb:"« Qui » reprend « moi » : première personne."},
         {q:"« ___ le ton qui fait rire. »", opts:["C'est","Ce sont"], ok:0,
          fb:"Un seul élément au singulier : c'est."},
         {q:"« ___ les silences qui font le film. »", opts:["Ce sont","C'est"], ok:0,
          fb:"Pluriel : ce sont."},
         {q:"Pour annoncer avant de livrer, on emploie…", opts:["ce qui… c'est","c'est… que"], ok:0,
          fb:"« Ce qui me frappe, c'est… » : l'auditoire attend une seconde."},
       ]},

      {t:'revoir', h:"À retenir",
       p:"<b>C'est… qui</b> pour le sujet, <b>c'est… que</b> pour le reste, <b>ce qui… c'est</b> pour annoncer. Le verbe s'accorde avec ce qu'on met en avant, et l'on n'en met qu'un par idée."},
    ]
  },

  t2paroles: {
    eye:'Mini-leçon', tit:"Lire une chanson comme un texte",
    blocs:[
      {t:'texte', h:"Deux choses dites d'un seul coup",
       p:"Une chanson raconte quelque chose qu'on peut filmer — une femme, trois étages, deux sacs — et dit en même temps quelque chose qu'on ne peut pas filmer. La deuxième chose n'est jamais nommée : si elle l'était, la chanson deviendrait un discours. Comprendre une chanson, c'est tenir les deux ensemble sans en écraser une.",
       note:"C'est exactement ce que Nadia Ferron refuse de dire en entrevue : « si je vous la dis, elle cesse d'être la deuxième »."},

      {t:'ana', h:"La structure, d'abord",
       p:"Trouvez le morceau qui revient mot pour mot : c'est le refrain. Le reste s'organise autour.",
       mots:[['Le couplet','change chaque fois, fait avancer l\'histoire, se retient mal'],['Le refrain','ne change pas, dit le sens, se retient tout seul'],['La fin','souvent un seul vers, qui déplace quelque chose']],
       say:"Le couplet raconte, le refrain dit ce que cela veut dire.",
       note:"Ici : couplet, refrain, couplet, refrain, puis un seul vers de fin."},

      {t:'ana', h:"Ce qui se filme et ce qui ne se filme pas",
       p:"Passez la chanson en deux colonnes, et la deuxième colonne est le cœur.",
       mots:[['Ça se filme','la glace, les deux sacs, la rampe neuve, la fenêtre allumée, la boîte de carton'],['Ça ne se filme pas','« le troisième étage a des idées sur moi » · « je n\'arrive jamais »'],['La règle','une chanson pose la deuxième au milieu de la première']],
       say:"Le troisième étage a des idées sur moi.",
       note:"Un escalier n'a pas d'idées : la phrase est impossible, donc elle est une image."},

      {t:'ana', h:"Les mots qui reviennent",
       p:"Une répétition dans une chanson courte n'est jamais un hasard.",
       mots:[['Le verbe','<b>monter</b> — trois fois dans le refrain seul'],['Le nombre','<b>neuf</b> — neuf ans, neuf fois'],['Ce que la tournure dit','un mouvement qui recommence et n\'aboutit pas']],
       say:"Je monte, je monte, et je n'arrive jamais.",
       note:"Comptez les répétitions avant de chercher le sens : elles vous y mènent."},

      {t:'ex', h:"Ce qu'on voit, ce que ça veut dire",
       p:"À gauche l'image, à droite ce qu'elle porte.",
       rows:[
         ["la rampe neuve, et rien d'autre de neuf","on répare le petit, on laisse le reste"],
         ["la boîte de carton qui attend depuis neuf ans","un déménagement toujours remis"],
         ["« j'avais dit l'an prochain, je l'ai dit neuf fois »","une promesse qu'on se fait à soi-même"],
         ["« le sac est moins lourd »","quelque chose a changé, et ce n'est pas le sac"],
       ]},

      {t:'piege', h:"Deux pièges",
       rows:[
         ["chercher un message caché unique","accepter plusieurs lectures",
          "L'auteure elle-même dit que chacun met ce qu'il veut derrière « ils ». Une image ouverte n'a pas une réponse : elle a une direction."],
         ["ne lire que le refrain","lire les couplets d'abord",
          "Le refrain ne se comprend qu'après les couplets. C'est eux qui donnent les sacs, la glace et les neuf ans, sans lesquels le refrain n'est qu'une phrase étrange."],
       ]},

      {t:'check', h:"Est-ce que c'est clair maintenant ?",
       p:"Trois questions, trois décisions.",
       qs:[
         {q:"Le morceau qui revient mot pour mot s'appelle…", opts:["le refrain","le couplet"], ok:0,
          fb:"Le refrain ne change pas ; les couplets, si."},
         {q:"« Le troisième étage a des idées sur moi » est…", opts:["une image","un fait"], ok:0,
          fb:"Un escalier ne pense pas : la phrase parle d'autre chose."},
         {q:"Un mot répété trois fois dans une chanson courte…", opts:["mérite qu'on s'y arrête","est un remplissage"], ok:0,
          fb:"Une chanson est trop courte pour du remplissage."},
       ]},

      {t:'revoir', h:"À retenir",
       p:"D'abord la <b>structure</b> (couplet, refrain), puis la séparation entre <b>ce qui se filme</b> et <b>ce qui ne se filme pas</b>, puis les <b>répétitions</b>. Ce qui n'est pas nommé reste ouvert : c'est voulu."},
    ]
  },

  t2repr: {
    eye:'Mini-leçon', tit:"Reprendre sans se répéter",
    blocs:[
      {t:'texte', h:"Un texte tient par ses reprises",
       p:"Dans un texte suivi, on ne renomme pas chaque chose à chaque phrase : on la reprend. Un pronom, un synonyme, un mot plus général. C'est ce qui fait la différence entre une suite de phrases et un texte — et c'est ce qui rend un texte difficile à suivre quand la reprise est floue.",
       note:"C'est le savoir de niveau 7 le plus utile hors de la classe : il sert dans une lettre, une critique, un compte rendu."},

      {t:'ana', h:"Le pronom qui regarde en arrière",
       p:"Il n'a aucun sens propre : il prend celui de ce qui précède.",
       mots:[['Exemple','La rampe est neuve. Ils <b>l\'</b>ont refaite en septembre.'],['Ce que « l\' » reprend','la rampe'],['La règle','on ne l\'emploie que si le lecteur peut retrouver quoi, sans hésiter']],
       say:"La rampe est neuve. Ils l'ont refaite en septembre.",
       note:"Le pronom est le plus léger des procédés, et le plus dangereux : il ne pardonne pas l'ambiguïté."},

      {t:'ana', h:"Le « ils » qui ne reprend rien",
       p:"Le français emploie souvent « ils » sans que personne n'ait été nommé. Il désigne alors ceux qui décident, et qu'on ne rencontre pas.",
       mots:[['Dans la chanson','<b>Ils</b> ont refait la rampe, <b>ils</b> n\'ont rien refait d\'autre.'],['Ailleurs','<b>Ils</b> ont encore augmenté le loyer. · <b>Ils</b> annoncent de la neige.'],['Son effet sur le lecteur','ça laisse chacun mettre le nom qu\'il veut']],
       say:"Ils ont refait la rampe, ils n'ont rien refait d'autre.",
       note:"Ce n'est pas une faute : c'est un emploi courant, et il est ici un choix d'écriture."},

      {t:'ana', h:"« le » pour une phrase entière, « en » pour un « de »",
       p:"Deux pronoms qui ne remplacent pas un nom simple.",
       mots:[['« le » pour une phrase','J\'avais dit l\'an prochain. Je <b>l\'</b>ai dit neuf fois.'],['« en » pour un GPrép en de','Elle parle <b>de son escalier</b>. Elle <b>en</b> parle tout le temps.'],['« y » pour un lieu','La boîte est dans le corridor. Elle <b>y</b> est depuis neuf ans.']],
       say:"Je l'ai dit neuf fois. Elle en parle tout le temps.",
       note:"Cherchez la préposition : « de » appelle en, « à » ou un lieu appellent y."},

      {t:'ana', h:"La substitution lexicale — un autre mot, et un jugement",
       p:"Au lieu d'un pronom, on emploie un autre mot. Il ajoute quelque chose au passage.",
       mots:[['Neutre','le film · le long métrage · l\'œuvre'],['Avec un jugement','cette petite merveille · ce long métrage bavard'],['Plus général','l\'œuvre, la pièce, le spectacle — ce qu\'on appelle un mot générique']],
       say:"le film, le long métrage, l'œuvre, cette petite merveille",
       note:"Dans une critique, c'est là que passe l'opinion, sans qu'aucune phrase ne l'annonce."},

      {t:'labo', h:"Quelle reprise employer ?",
       p:"Choisissez une phrase de départ et un procédé.",
       axes:[
         {id:'p', lbl:'Quelle amorce ?', opts:[['a','J\'ai vu le film jeudi.'],['b','Elle parle de son escalier.'],['c','J\'avais dit l\'an prochain.']]},
         {id:'r', lbl:'Repris comment ?', opts:[['1','un pronom'],['2','un autre mot']]}],
       out:{
         a1:{w:["Je l'ai trouvé long au début."], say:"Je l'ai trouvé long au début.", n:'« l\' » reprend le film'},
         a2:{w:["Ce long métrage m'a surprise."], say:"Ce long métrage m'a surprise.", n:'substitution lexicale'},
         b1:{w:["Elle en parle depuis neuf ans."], say:"Elle en parle depuis neuf ans.", n:'« de son escalier » devient en'},
         b2:{w:["Elle parle de cet escalier-là dans toutes ses entrevues."], say:"Elle parle de cet escalier-là dans toutes ses entrevues.", n:'reprise par un démonstratif'},
         c1:{w:["Je l'ai dit neuf fois."], say:"Je l'ai dit neuf fois.", n:'« l\' » reprend toute la phrase'},
         c2:{w:["Cette promesse-là, je l'ai faite neuf fois."], say:"Cette promesse-là, je l'ai faite neuf fois.", n:'un nom résume la phrase : nominalisation'},
       },
       note:"La dernière transformation — une phrase qui devient un nom — s'appelle une nominalisation. C'est le procédé de la langue écrite."},

      {t:'piege', h:"Trois pièges",
       rows:[
         ["le pronom qui flotte","reprendre le nom",
          "« Marilou parle à Ghyslaine de sa chanson. Elle l'aime. » Qui aime quoi ? Deux noms devant, un pronom derrière : récrivez."],
         ["répéter le même nom partout","varier les reprises",
          "« Le film… Le film… Le film… » : c'est correct et c'est illisible. Alternez pronom, synonyme, mot générique."],
         ["employer « en » là où il faut « y »","chercher la préposition",
          "On parle <b>de</b> quelque chose : en. On pense <b>à</b> quelque chose : y. La préposition du verbe décide, pas l'oreille."],
       ]},

      {t:'check', h:"Est-ce que c'est clair maintenant ?",
       p:"Quatre reprises.",
       qs:[
         {q:"« Elle parle de son escalier. Elle ___ parle tout le temps. »", opts:["en","y"], ok:0,
          fb:"« de » appelle en."},
         {q:"« La boîte est dans le corridor. Elle ___ est depuis neuf ans. »", opts:["y","en"], ok:0,
          fb:"Un lieu appelle y."},
         {q:"Dans la chanson, « ils » désigne…", opts:["des gens jamais nommés","le propriétaire, nommé plus haut"], ok:0,
          fb:"Personne n'est nommé, et c'est un choix de l'auteure."},
         {q:"« Cette promesse-là » à la place de « j'avais dit l'an prochain » est…", opts:["une nominalisation","un pronom"], ok:0,
          fb:"Une phrase devenue un nom : c'est le procédé de l'écrit."},
       ]},

      {t:'revoir', h:"À retenir",
       p:"Reprendre, c'est <b>un pronom</b> (le, en, y, ils), <b>un autre mot</b> (synonyme, mot générique) ou <b>un nom qui résume une phrase</b>. La seule règle absolue : le lecteur doit retrouver de quoi on parle sans revenir en arrière."},
    ]
  },

  t2int: {
    eye:'Mini-leçon', tit:"Jusqu'à quel point, et avec quelle conséquence",
    blocs:[
      {t:'texte', h:"Le degré transforme un goût en argument",
       p:"« Le film est lent » : on peut vous répondre « moi je ne trouve pas ». « Le film est assez lent pour que la moitié de la salle décroche » : on ne peut plus. Vous avez donné un degré et sa conséquence, et la conséquence se vérifie. C'est la construction la plus utile de tout le module pour la réunion de jeudi.",
       note:"On l'appelle la subordonnée corrélative : deux morceaux qui se répondent, l'intensité d'un côté, la conséquence de l'autre."},

      {t:'ana', h:"si / tellement + adjectif ou adverbe + que",
       p:"La conséquence a lieu pour de vrai : indicatif après « que ».",
       mots:[['Avec un adjectif de degré','Le vent est <b>tellement</b> froid <b>qu\'</b>elle oublie de compter.'],['Avec un adverbe de manière','Elle chante <b>si</b> fort <b>qu\'</b>on l\'entend dehors.'],['Le mode','indicatif — ça se produit']],
       say:"Le vent est tellement froid qu'elle oublie de compter.",
       note:"« si » et « tellement » sont interchangeables ici. « si » est un peu plus soutenu."},

      {t:'ana', h:"tellement de / tant de + nom + que",
       p:"Devant un nom, il faut le « de ».",
       mots:[['La forme','Il y a <b>tellement de</b> monde <b>que</b> nous restons debout.'],['Variante','Il a raconté <b>tant d\'</b>histoires <b>que</b> personne n\'a vu l\'heure.'],['L\'élision','tant de + voyelle donne tant d\'']],
       say:"Il y a tellement de monde que nous restons debout.",
       note:"Jamais « si de » : avec un nom, c'est tellement de ou tant de."},

      {t:'ana', h:"trop / assez + pour que + subjonctif",
       p:"Ici, la conséquence n'a pas lieu, ou elle est seulement rendue possible. D'où le subjonctif.",
       mots:[['Empêchement','Le refrain monte <b>trop</b> haut <b>pour qu\'</b>elle le <b>réussisse</b> chaque soir.'],['Possibilité','La salle est <b>assez</b> petite <b>pour qu\'</b>on l\'<b>entende</b> sans micro.'],['Le mode','subjonctif, sans exception']],
       say:"Le refrain monte trop haut pour qu'elle le réussisse chaque soir.",
       note:"Retenez la paire : « que » indicatif, « pour que » subjonctif."},

      {t:'ana', h:"Même personne des deux côtés : pour + infinitif",
       p:"Quand c'est la même personne des deux côtés, on allège.",
       mots:[['Deux sujets','Elle est trop fatiguée <b>pour que</b> nous <b>sortions</b>.'],['Une seule personne','Elle est trop fatiguée <b>pour sortir</b>.'],['Le test','demandez qui fait quoi de chaque côté']],
       say:"Elle est trop fatiguée pour sortir.",
       note:"C'est plus court et plus naturel : préférez-le chaque fois que c'est possible."},

      {t:'labo', h:"Le degré et sa conséquence",
       p:"Choisissez une idée et une tournure.",
       axes:[
         {id:'i', lbl:'Quel jugement ?', opts:[['a','le film est lent'],['b','la salle est petite'],['c','le billet coûte cher']]},
         {id:'t', lbl:'Quel dosage ?', opts:[['1','tellement… que'],['2','trop / assez… pour que']]}],
       out:{
         a1:{w:["Le film est tellement lent que la moitié de la salle décroche."], say:"Le film est tellement lent que la moitié de la salle décroche.", n:'la conséquence a lieu : indicatif'},
         a2:{w:["Le film est assez lent pour que la moitié de la salle décroche."], say:"Le film est assez lent pour que la moitié de la salle décroche.", n:'subjonctif après pour que'},
         b1:{w:["La salle est tellement petite qu'on entend tout."], say:"La salle est tellement petite qu'on entend tout.", n:'indicatif'},
         b2:{w:["La salle est assez petite pour qu'on l'entende sans micro."], say:"La salle est assez petite pour qu'on l'entende sans micro.", n:'entende, subjonctif'},
         c1:{w:["Le billet coûte tellement cher que nous hésitons."], say:"Le billet coûte tellement cher que nous hésitons.", n:'indicatif'},
         c2:{w:["Le billet coûte trop cher pour que nous puissions y aller."], say:"Le billet coûte trop cher pour que nous puissions y aller.", n:'puissions, subjonctif'},
       },
       note:"Même idée, deux constructions, deux modes. Le mode dit si la chose arrive."},

      {t:'piege', h:"Trois pièges",
       rows:[
         ["pour qu'on peut","pour qu'on puisse",
          "Après « pour que », l'indicatif n'existe pas. C'est la faute la plus repérable de cette leçon, et elle se corrige en apprenant sept subjonctifs."],
         ["si de monde","tellement de monde",
          "Devant un nom, « si » ne s'emploie pas. Tellement de, tant de, beaucoup de : tous prennent le « de »."],
         ["pour que + même sujet","pour + infinitif",
          "« Elle est trop fatiguée pour qu'elle sorte » est lourd et fautif. Même personne des deux côtés : « pour sortir »."],
       ]},

      {t:'check', h:"Est-ce que c'est clair maintenant ?",
       p:"Quatre choix.",
       qs:[
         {q:"« Le billet coûte trop cher pour que nous ___ y aller. »", opts:["puissions","pouvons"], ok:0,
          fb:"Pour que appelle le subjonctif, toujours."},
         {q:"« Il y a ___ monde que nous restons debout. »", opts:["tellement de","si"], ok:0,
          fb:"Devant un nom : tellement de, ou tant de."},
         {q:"« Le vent est tellement froid qu'elle ___ de compter. »", opts:["oublie","oublierait"], ok:0,
          fb:"Après « que » seul, l'indicatif présent : la conséquence a lieu pour de vrai."},
         {q:"Même sujet des deux côtés, on écrit…", opts:["pour + infinitif","pour que + subjonctif"], ok:0,
          fb:"« trop fatiguée pour sortir », plus court et plus juste."},
       ]},

      {t:'revoir', h:"À retenir",
       p:"<b>si / tellement… que</b> + indicatif : ça arrive. <b>tellement de / tant de</b> + nom. <b>trop / assez… pour que</b> + subjonctif : c'est empêché ou rendu possible. Même sujet des deux côtés : <b>pour</b> + infinitif."},
    ]
  },

  t2gen: {
    eye:'Mini-leçon', tit:"La musique, ou cette musique-là",
    blocs:[
      {t:'texte', h:"Un même nom, deux portées",
       p:"« La musique, ça me calme » ne parle d'aucune musique en particulier : ça parle de la musique en général. « La musique de ce film est trop forte » parle d'une chose qu'on peut aller écouter. Le nom est le même ; ce qui change est le déterminant, le complément et le pronom de reprise.",
       note:"L'exemple du programme est lui-même musical, et ce n'est pas un hasard : c'est avec les arts qu'on glisse le plus souvent du général au particulier sans s'en rendre compte."},

      {t:'ana', h:"Le sens général — et son pronom « ça »",
       p:"On parle de toute une catégorie. Le pronom de reprise est presque toujours « ça ».",
       mots:[['Avec un défini','<b>La</b> musique, <b>ça</b> me calme.'],['Avec un indéfini singulier','<b>Un</b> réfrigérateur, <b>ça</b> dure quinze ans.'],['Avec un pluriel','<b>Les</b> longs métrages, <b>ça</b> dure plus d\'une heure.']],
       say:"La musique, ça me calme. Un bon film, ça ne s'explique pas.",
       note:"Le « ça » est le signe le plus sûr : il ne reprend jamais une chose précise."},

      {t:'ana', h:"Le sens spécifique, accroché au réel par un complément",
       p:"Un complément, une relative, un démonstratif : quelque chose montre du doigt.",
       mots:[['Un complément qui accroche','La musique <b>de ce film</b> intervient onze fois.'],['Une relative','La chanson <b>qu\'elle a chantée en rappel</b> n\'est pas sur son disque.'],['Avec un démonstratif','<b>Ce</b> film-<b>là</b> m\'a endormie.']],
       say:"La musique de ce film intervient onze fois.",
       note:"Sans accroche, le nom reste général. L'accroche est ce qui le fait descendre dans le monde."},

      {t:'ana', h:"« Il y a… qui » — le spécifique du français parlé",
       p:"À l'oral, on n'introduit presque jamais une chose nouvelle en sujet direct.",
       mots:[['Ce qu\'on dit','<b>Il y a un</b> gars <b>qui</b> a ri tout seul.'],['Ce qui ne se dit pas','Un gars a ri tout seul.'],['Où','partout, dans toute conversation en français du Québec']],
       say:"Il y a un gars qui a ri tout seul dans la salle.",
       note:"La forme écrite « Un gars a ri » est correcte, mais elle sonne comme un roman."},

      {t:'ex', h:"Quatre paires",
       p:"À gauche le général, à droite le spécifique.",
       rows:[
         ["La musique, ça me calme.","La musique de ce film est trop forte."],
         ["Un bon sketch, ça finit par une chute.","Il y a un sketch qui parle d'un comptoir de pièces."],
         ["Le cinéma, ça coûte moins cher que le théâtre.","Le cinéma de la rue Notre-Dame a cent quatre-vingts places."],
         ["Les chansons tristes, ça ne me dérange pas.","La chanson du rappel n'est pas sur son disque."],
       ]},

      {t:'piege', h:"Deux pièges",
       rows:[
         ["juger une œuvre par sa catégorie","juger l'œuvre elle-même",
          "« Les films lents, ça m'endort » ne dit rien du film qu'on vient de voir. C'est un goût sur une catégorie, et il empêche de regarder ce qu'on a devant soi."],
         ["reprendre une chose précise par « ça »","employer il, elle, le, la",
          "« Ce film-là, ça m'a plu » se dit, mais dérive vers le général. Écrivez « il m'a plu » : vous parlez de celui-là et de nul autre."],
       ]},

      {t:'check', h:"Est-ce que c'est clair maintenant ?",
       p:"Quatre phrases.",
       qs:[
         {q:"« Un bon film, ça ne s'explique pas » parle…", opts:["de tous les bons films","d'un film précis"], ok:0,
          fb:"Le « ça » reprend une catégorie entière."},
         {q:"« La chanson qu'elle a chantée en rappel » est…", opts:["spécifique","général"], ok:0,
          fb:"La relative l'accroche à une chanson qu'on peut nommer."},
         {q:"Le signe le plus sûr du sens général est…", opts:["le pronom ça","le déterminant la"], ok:0,
          fb:"« La » sert aux deux ; « ça » ne sert qu'au général."},
         {q:"À l'oral, on introduit une chose nouvelle par…", opts:["il y a… qui","le sujet direct"], ok:0,
          fb:"« Il y a un gars qui… » : la forme normale de la conversation."},
       ]},

      {t:'revoir', h:"À retenir",
       p:"<b>Général</b> : catégorie entière, repris par <b>ça</b>. <b>Spécifique</b> : accroché par un complément, une relative ou un démonstratif, repris par <b>il, elle, le, la</b>. Un avis honnête porte sur le spécifique."},
    ]
  },

  t3crit: {
    eye:'Mini-leçon', tit:"Lire une critique sans se faire porter",
    blocs:[
      {t:'texte', h:"Une critique n'est pas un résumé",
       p:"Elle contient trois sortes de phrases : des faits qu'on peut vérifier, des jugements qui n'engagent que son auteur, et une recommandation à la fin. Le lecteur pressé ne retient que la dernière. Le lecteur qui sait lire commence par séparer les deux premières — et découvre souvent que le jugement tient à très peu de choses.",
       note:"C'est le même travail que dans un article d'actualité, avec ceci de particulier : ici le journaliste a le droit de donner son avis, et il est même payé pour ça."},

      {t:'ana', h:"Les faits — quelqu'un d'autre peut aller compter",
       p:"Une durée, un lieu, un nombre, une date.",
       mots:[['Dans la critique','« Le film dure une heure cinquante. » · « Elle intervient onze fois. »'],['Le test','deux personnes qui vérifient trouvent la même chose'],['L\'usage qu\'on en fait','on s\'en sert pour appuyer, ou pour contredire']],
       say:"Le film dure une heure cinquante. Elle intervient onze fois.",
       note:"Un fait faux dans une critique est une erreur ; un jugement faux n'existe pas."},

      {t:'ana', h:"Les jugements — ils valent ce que vaut leur appui",
       p:"Un adjectif, un superlatif, une impression.",
       mots:[['Sans appui','« Le premier quart d\'heure m\'a paru interminable. »'],['Avec appui','« …aucune parole n\'est échangée avant la douzième minute. »'],['Le repère','cherchez la phrase juste après le jugement']],
       say:"Le premier quart d'heure m'a paru interminable.",
       note:"Un bon critique appuie ; un critique pressé enchaîne les adjectifs."},

      {t:'ana', h:"La nuance — le mot qui annonce le virage",
       p:"« Bien que », « malgré », « certes… mais », « cela dit ».",
       mots:[['Dans la critique','« <b>Bien que</b> le rythme demeure lent, la deuxième heure tient sans effort. »'],['Ce qui se voit','le critique a vu l\'objection et il y répond d\'avance'],['Le poids que ça donne','beaucoup : un texte sans nuance est une publicité']],
       say:"Bien que le rythme demeure lent, la deuxième heure tient sans effort.",
       note:"Repérez ces mots-là et vous avez le plan du texte en trente secondes."},

      {t:'ana', h:"La recommandation — la seule réponse à votre question",
       p:"Presque toujours à la dernière ligne, souvent assortie d'une condition.",
       mots:[['Ici','« À voir, donc, mais pas un soir de fatigue. »'],['Ailleurs','« à voir absolument » · « on peut attendre » · « à réserver aux amateurs »'],['Attention','la condition est la moitié la plus utile']],
       say:"À voir, donc, mais pas un soir de fatigue.",
       note:"« Mais pas un soir de fatigue » vous dit plus que les quarante lignes précédentes."},

      {t:'labo', h:"Fait, jugement, ou nuance ?",
       p:"Choisissez un passage et voyez ce qu'il est.",
       axes:[
         {id:'p', lbl:'Quel passage ?', opts:[['a','le film dure une heure cinquante'],['b','le début m\'a paru interminable'],['c','bien que le rythme demeure lent…']]},
         {id:'q', lbl:'Quoi savoir ?', opts:[['1','ce que c\'est'],['2','ce qu\'on en fait']]}],
       out:{
         a1:{w:["Un fait."], say:"Un fait, vérifiable avec une montre.", n:'personne ne peut le contester'},
         a2:{w:["On s'en sert pour appuyer un jugement."], say:"On s'en sert pour appuyer un jugement.", n:'un fait seul ne dit rien'},
         b1:{w:["Un jugement, sans appui pour l'instant."], say:"Un jugement, sans appui pour l'instant.", n:'on peut ne pas être d\'accord'},
         b2:{w:["On cherche la phrase suivante, qui l'appuie ou non."], say:"On cherche la phrase suivante, qui l'appuie ou non.", n:'ici, elle l\'appuie'},
         c1:{w:["Une concession."], say:"Une concession.", n:'le critique accorde avant de maintenir'},
         c2:{w:["On y lit le plan du texte."], say:"On y lit le plan du texte.", n:'l\'objection, puis la réponse'},
       },
       note:"Trois passages, trois usages. Une critique bien faite a les trois."},

      {t:'piege', h:"Deux pièges",
       rows:[
         ["lire seulement la dernière ligne","lire les faits d'abord",
          "« À voir » ne vous dit pas si c'est pour vous. Les faits — la durée, le sujet, le rythme — le disent beaucoup mieux."],
         ["prendre un jugement pour un fait","chercher le verbe",
          "« Le film est trop long » a l'air d'un fait. « M'a paru », « je trouve », « à mon avis » sont les marques d'un jugement ; leur absence n'en fait pas une vérité."],
       ]},

      {t:'check', h:"Est-ce que c'est clair maintenant ?",
       p:"Quatre passages à classer.",
       qs:[
         {q:"« Elle intervient onze fois. » C'est…", opts:["un fait","un jugement"], ok:0,
          fb:"On peut compter."},
         {q:"« C'est la plus belle scène du film. » C'est…", opts:["un jugement","un fait"], ok:0,
          fb:"Un superlatif d'appréciation : personne ne peut le vérifier."},
         {q:"« Bien que le rythme demeure lent… » annonce…", opts:["une nuance","un fait"], ok:0,
          fb:"Le critique accorde un point avant de maintenir le sien."},
         {q:"La partie la plus utile de la recommandation est souvent…", opts:["la condition","le verbe"], ok:0,
          fb:"« mais pas un soir de fatigue » : c'est là que se trouve le conseil."},
       ]},

      {t:'revoir', h:"À retenir",
       p:"Dans une critique : les <b>faits</b> se vérifient, les <b>jugements</b> valent ce que vaut leur appui, les mots de <b>nuance</b> donnent le plan, et la <b>recommandation finale</b> tient dans sa condition."},
    ]
  },

  t3conc: {
    eye:'Mini-leçon', tit:"Accorder un point, puis tenir le sien",
    blocs:[
      {t:'texte', h:"La concession n'est pas une reculade",
       p:"Donner raison à l'autre sur un point avant de lui répondre est ce qui rend la suite audible. Ce n'est pas de la politesse et ce n'est pas une faiblesse : c'est une technique, et elle ne fonctionne qu'à une condition — le point accordé doit être réellement vrai. Une concession sur un faux point s'entend tout de suite et retourne la table contre vous.",
       note:"C'est exactement ce que fait Marilou : « c'est vrai qu'on peut regarder un film chez soi », et Gaétan écoute la suite."},

      {t:'ana', h:"bien que + subjonctif",
       p:"Le marqueur de l'écrit et de la réunion. Il annonce d'entrée qu'une objection suit.",
       mots:[['La forme','<b>Bien que</b> le film <b>soit</b> lent, il tient.'],['Le mode','subjonctif, toujours, sans une seule exception'],['Où','compte rendu, exposé, lettre, réunion']],
       say:"Bien que le film soit lent, il tient.",
       note:"« Quoique » se construit de la même façon et veut dire la même chose."},

      {t:'ana', h:"même si + indicatif",
       p:"Le marqueur de la conversation. Aucun risque de faute de mode.",
       mots:[['La forme','<b>Même si</b> le film <b>est</b> lent, il tient.'],['Le mode','indicatif'],['Où','partout, à l\'oral surtout']],
       say:"Même si le film est lent, il tient.",
       note:"Si vous n'êtes pas sûr du subjonctif, employez celui-ci : il dit exactement la même chose."},

      {t:'ana', h:"malgré + nom",
       p:"Pas de verbe conjugué après « malgré ». Il faut transformer.",
       mots:[['La forme','<b>Malgré</b> sa <b>lenteur</b>, le film tient.'],['La transformation à faire','lent devient <b>la lenteur</b> · long devient <b>la longueur</b> · cher devient <b>le prix</b>'],['La faute','« malgré qu\'il soit lent » est à éviter à l\'écrit']],
       say:"Malgré sa lenteur, le film tient.",
       note:"Cette transformation d'un adjectif en nom s'appelle une nominalisation, et c'est la marque de la langue écrite."},

      {t:'ana', h:"Où placer la concession",
       p:"Avant votre position, jamais après. La deuxième moitié de la phrase est celle qu'on retient.",
       mots:[['Bon ordre','Bien que ce soit cher, <b>j\'y vais</b>.'],['Mauvais ordre','J\'y vais, <b>bien que ce soit cher</b>.'],['Ce que ça déplace','la première finit sur votre décision, la seconde sur l\'obstacle']],
       say:"Bien que ce soit cher, j'y vais.",
       note:"C'est vrai à l'oral comme à l'écrit, et c'est la moitié du travail."},

      {t:'labo', h:"Trois marqueurs, une seule idée",
       p:"Choisissez une objection et un marqueur.",
       axes:[
         {id:'o', lbl:'Quelle objection ?', opts:[['a','le film est lent'],['b','le billet est cher'],['c','la salle est petite']]},
         {id:'m', lbl:'Quel mot de concession ?', opts:[['1','bien que'],['2','même si'],['3','malgré']]}],
       out:{
         a1:{w:["Bien que le film soit lent, il tient."], say:"Bien que le film soit lent, il tient.", n:'subjonctif de être'},
         a2:{w:["Même si le film est lent, il tient."], say:"Même si le film est lent, il tient.", n:'indicatif'},
         a3:{w:["Malgré sa lenteur, le film tient."], say:"Malgré sa lenteur, le film tient.", n:'un nom, pas un verbe'},
         b1:{w:["Bien que le billet soit cher, il reste dans le budget."], say:"Bien que le billet soit cher, il reste dans le budget.", n:'subjonctif'},
         b2:{w:["Même si le billet est cher, il reste dans le budget."], say:"Même si le billet est cher, il reste dans le budget.", n:'indicatif'},
         b3:{w:["Malgré son prix, le billet reste dans le budget."], say:"Malgré son prix, le billet reste dans le budget.", n:'cher devient le prix'},
         c1:{w:["Bien que la salle soit petite, on y entend très bien."], say:"Bien que la salle soit petite, on y entend très bien.", n:'subjonctif'},
         c2:{w:["Même si la salle est petite, on y entend très bien."], say:"Même si la salle est petite, on y entend très bien.", n:'indicatif'},
         c3:{w:["Malgré sa petite taille, la salle sonne très bien."], say:"Malgré sa petite taille, la salle sonne très bien.", n:'un groupe du nom'},
       },
       note:"Trois formes, un seul geste : accorder, puis maintenir."},

      {t:'ex', h:"Les sept subjonctifs à savoir par cœur",
       p:"Ce sont ceux qui reviennent dans toutes les concessions.",
       rows:[
         ["être","qu'il soit · que nous soyons"],
         ["avoir","qu'il ait · que nous ayons"],
         ["faire","qu'il fasse · que nous fassions"],
         ["aller","qu'il aille · que nous allions"],
         ["pouvoir","qu'il puisse · que nous puissions"],
         ["savoir","qu'il sache · que nous sachions"],
         ["vouloir","qu'il veuille · que nous voulions"],
       ]},

      {t:'piege', h:"Trois pièges",
       rows:[
         ["bien qu'il est","bien qu'il soit",
          "Après « bien que », l'indicatif n'existe pas. Si le subjonctif ne vient pas, changez de marqueur : « même s'il est »."],
         ["malgré qu'il soit","malgré sa lenteur",
          "« Malgré que » existe, mais il est critiqué et il détonne à l'écrit. Après malgré, un nom."],
         ["accorder un point faux","accorder ce qui est vrai",
          "« C'est vrai que c'est un mauvais film, mais… » : personne ne vous croit, et vous venez de perdre votre propre position."],
       ]},

      {t:'check', h:"Est-ce que c'est clair maintenant ?",
       p:"Quatre formes.",
       qs:[
         {q:"« Bien que le film ___ lent, il tient. »", opts:["soit","est"], ok:0,
          fb:"Bien que appelle le subjonctif."},
         {q:"« Même si le billet ___ cher, j'y vais. »", opts:["est","soit"], ok:0,
          fb:"Même si appelle l'indicatif."},
         {q:"Ce qui suit « malgré », c'est…", opts:["un nom","un verbe conjugué"], ok:0,
          fb:"Malgré sa lenteur, malgré son prix, malgré le froid."},
         {q:"Où se place la concession, déjà ?", opts:["avant sa position","après sa position"], ok:0,
          fb:"On finit sur ce qu'on veut faire retenir."},
       ]},

      {t:'revoir', h:"À retenir",
       p:"<b>Bien que</b> + subjonctif (écrit, réunion), <b>même si</b> + indicatif (partout), <b>malgré</b> + nom. Toujours <b>avant</b> votre position, et toujours sur un point <b>réellement vrai</b>."},
    ]
  },

  t3si: {
    eye:'Mini-leçon', tit:"Si c'était différent, je dirais autre chose",
    blocs:[
      {t:'texte', h:"Supposer, c'est déplacer la discussion sans attaquer personne",
       p:"« Si le budget était de deux mille dollars, je proposerais l'humour. » Marilou n'a contredit personne, et pourtant elle vient de dire exactement pourquoi elle refuse. L'hypothèse est l'outil le plus courtois d'une réunion : elle transporte le désaccord dans un monde qui n'existe pas, où il ne blesse personne.",
       note:"Le même temps sert à demander poliment — « pourriez-vous », « je voudrais ». Une forme, deux emplois."},

      {t:'ana', h:"La règle tient sur une ligne",
       p:"Si + imparfait, puis conditionnel présent. Et jamais l'inverse.",
       mots:[['La forme','<b>Si</b> le budget <b>était</b> plus grand, je <b>proposerais</b> l\'humour.'],['Ce que la phrase suppose','le budget n\'est pas plus grand'],['Ce qui ne se dit jamais','« si j\'aurais » n\'existe pas']],
       say:"Si le budget était plus grand, je proposerais l'humour.",
       note:"L'ordre des deux moitiés peut s'inverser : « je proposerais l'humour si le budget était plus grand »."},

      {t:'ana', h:"Comment se fabrique le conditionnel",
       p:"Le radical du futur, les terminaisons de l'imparfait. Il y a toujours un r avant la terminaison.",
       mots:[['Régulier','je propos<b>erais</b> · tu chant<b>erais</b> · elle finir<b>ait</b>'],['Les six terminaisons, sans exception','-rais, -rais, -rait, -rions, -riez, -raient'],['Le signe','le <b>r</b>, qui le distingue de l\'imparfait']],
       say:"je proposerais, tu chanterais, elle finirait",
       note:"À l'oral, « je proposerai » et « je proposerais » se ressemblent beaucoup : c'est le contexte qui tranche."},

      {t:'ana', h:"Les sept radicaux irréguliers",
       p:"Ce sont les mêmes qu'au futur : apprenez-les une fois, ils servent deux fois.",
       mots:[['Les voici','aller <b>j\'irais</b> · faire <b>je ferais</b> · venir <b>je viendrais</b> · voir <b>je verrais</b>'],['Et encore','vouloir <b>je voudrais</b> · devoir <b>je devrais</b> · pouvoir <b>je pourrais</b>'],['Impersonnel','falloir <b>il faudrait</b>']],
       say:"j'irais, je ferais, je viendrais, je verrais, je voudrais, je pourrais",
       note:"« Il faudrait » est probablement la forme la plus utile de toute la liste dans une réunion."},

      {t:'ana', h:"Le même temps pour demander",
       p:"Le conditionnel enlève à une demande ce qu'elle a de brusque.",
       mots:[['Demander','<b>Pourriez</b>-vous nous réserver dix places ?'],['Vouloir','Je <b>voudrais</b> deux billets pour jeudi.'],['Suggérer','Il <b>faudrait</b> décider avant lundi.']],
       say:"Pourriez-vous nous réserver dix places ? Je voudrais deux billets.",
       note:"« Je veux deux billets » n'est pas impoli en soi, mais « je voudrais » est ce que tout le monde dit."},

      {t:'labo', h:"L'hypothèse, ou la politesse ?",
       p:"Choisissez un verbe, puis ce qu'on en fait.",
       axes:[
         {id:'v', lbl:'Quel verbe de parole ?', opts:[['a','pouvoir'],['b','vouloir'],['c','aller']]},
         {id:'e', lbl:'Supposer, ou demander ?', opts:[['1','hypothèse'],['2','politesse']]}],
       out:{
         a1:{w:["Si je pouvais choisir seule, je prendrais le film."], say:"Si je pouvais choisir seule, je prendrais le film.", n:'imparfait puis conditionnel'},
         a2:{w:["Pourriez-vous nous réserver dix places ?"], say:"Pourriez-vous nous réserver dix places ?", n:'une demande, pas une supposition'},
         b1:{w:["Si nous voulions rire, nous choisirions l'humour."], say:"Si nous voulions rire, nous choisirions l'humour.", n:'un monde qui n\'existe pas'},
         b2:{w:["Je voudrais deux billets pour jeudi."], say:"Je voudrais deux billets pour jeudi.", n:'la formule ordinaire au comptoir'},
         c1:{w:["Si le film durait une heure, Gaétan irait avec nous."], say:"Si le film durait une heure, Gaétan irait avec nous.", n:'radical irrégulier : ir-'},
         c2:{w:["Nous irions volontiers, si cela vous convient."], say:"Nous irions volontiers, si cela vous convient.", n:'atténuation polie'},
       },
       note:"Même forme, deux mondes : l'un imagine, l'autre demande."},

      {t:'piege', h:"Trois pièges",
       rows:[
         ["si j'aurais","si j'avais",
          "Le conditionnel ne se met jamais après « si ». C'est la faute la plus reconnaissable du français, et elle se corrige d'un coup : après si, imparfait."],
         ["confondre futur et conditionnel","chercher le r et la terminaison",
          "« Je proposerai » (futur, ça va arriver) et « je proposerais » (conditionnel, ça dépend). Un seul s à l'écrit, et tout change."],
         ["employer l'hypothèse pour se cacher","dire ensuite ce qu'on pense",
          "« Si nous étions vingt, je dirais oui » ne dit pas ce que vous pensez du spectacle. Faites suivre d'une phrase claire."],
       ]},

      {t:'check', h:"Est-ce que c'est clair maintenant ?",
       p:"Quatre choix.",
       qs:[
         {q:"« Si j'___ le temps, je viendrais. »", opts:["avais","aurais"], ok:0,
          fb:"Après si : imparfait. Jamais de conditionnel."},
         {q:"« Si nous avions plus d'argent, nous ___ (aller) au spectacle. »", opts:["irions","allerions"], ok:0,
          fb:"Radical irrégulier : ir-."},
         {q:"« Pourriez-vous… » est…", opts:["une demande polie","une hypothèse"], ok:0,
          fb:"Même forme, autre emploi : le contexte tranche."},
         {q:"Le conditionnel se reconnaît à…", opts:["un r avant la terminaison","un s final"], ok:0,
          fb:"Radical du futur, donc toujours un r."},
       ]},

      {t:'revoir', h:"À retenir",
       p:"<b>Si + imparfait, conditionnel présent.</b> Jamais de conditionnel après <i>si</i>. Le conditionnel se fabrique avec le <b>radical du futur</b> et les <b>terminaisons de l'imparfait</b>, et il sert aussi à <b>demander poliment</b>."},
    ]
  },

  t3conn: {
    eye:'Mini-leçon', tit:"Six mots qui tiennent une réunion debout",
    blocs:[
      {t:'texte', h:"Ils ne disent rien, et sans eux on ne suit plus",
       p:"« Quant à », « autrement dit », « en somme » ne portent aucune information. Ils disent seulement ce que vous êtes en train de faire : passer à un autre point, redire plus simplement, conclure. Dans une discussion à huit personnes, c'est ce qui permet à chacun de savoir où l'on en est.",
       note:"Ce sont les mots que Ghyslaine emploie pour tenir la réunion : « en ce qui concerne l'argent », « autrement dit », « en somme »."},

      {t:'ana', h:"Annoncer de quoi on va parler",
       p:"On prévient avant de dire, et l'auditoire se prépare.",
       mots:[['Changer de point','<b>Quant à</b> la chanson, elle est magnifique.'],['Cadrer un aspect','<b>En ce qui concerne</b> l\'argent, les trois entrent dans le budget.'],['Variante','<b>À propos de</b> la salle, elle ne compte que cent vingt places.']],
       say:"Quant à la chanson, elle est magnifique. En ce qui concerne l'argent, les trois entrent dans le budget.",
       note:"« Quant à » ne s'écrit jamais « quand à » : il n'a rien à voir avec le temps."},

      {t:'ana', h:"Redire la même chose, plus simplement",
       p:"On reformule pour vérifier qu'on a été compris, ou pour faire confirmer ce qu'on vient d'entendre.",
       mots:[['Reformuler','<b>Autrement dit</b>, il ne resterait rien pour le transport.'],['Vérifier','<b>Si je comprends bien</b>, nous partons de la même heure.'],['Résumer une explication','<b>En d\'autres mots</b>, la garantie ne couvre plus rien.']],
       say:"Autrement dit, il ne resterait rien pour le transport.",
       note:"C'est aussi la façon polie de faire répéter sans avouer qu'on n'a pas compris."},

      {t:'ana', h:"Ramasser et conclure",
       p:"On rassemble tout ce qui vient d'être dit avant de trancher.",
       mots:[['Ramasser','<b>En somme</b> : le film pour le prix, l\'humour pour l\'ambiance.'],['Tirer la suite','<b>Par conséquent</b>, nous voterons à main levée.'],['Variante','<b>Donc</b>, <b>en définitive</b>, <b>au total</b>']],
       say:"En somme : le film pour le prix, l'humour pour l'ambiance. Par conséquent, nous voterons.",
       note:"« En somme » résume, « par conséquent » déduit. Ce n'est pas la même chose."},

      {t:'ana', h:"Revenir en arrière pour nuancer",
       p:"On vient d'affirmer quelque chose, et on l'adoucit sans le retirer.",
       mots:[['Nuancer','<b>Cela dit</b>, le spectacle reste très bon.'],['Concéder','<b>Cela étant</b>, l\'argument de Gaétan tient.'],['Variante familière','<b>ceci dit</b> — courant, mais critiqué à l\'écrit']],
       say:"Cela dit, le spectacle reste très bon.",
       note:"« Cela dit » se place en tête de phrase, suivi d'une virgule."},

      {t:'ex', h:"Six connecteurs et leur travail",
       p:"À gauche le connecteur, à droite le travail qu'il fait.",
       rows:[
         ["quant à","je passe au point suivant"],
         ["en ce qui concerne","je cadre l'aspect dont je vais parler"],
         ["autrement dit","je redis la même chose plus simplement"],
         ["en somme","je ramasse tout avant de conclure"],
         ["par conséquent","je tire la suite logique"],
         ["cela dit","je nuance ce que je viens d'affirmer"],
       ]},

      {t:'piege', h:"Trois pièges",
       rows:[
         ["quand à","quant à",
          "Deux mots différents. « Quand » est le temps, « quant à » veut dire « pour ce qui est de ». L'orthographe se voit tout de suite dans un compte rendu."],
         ["en somme pour dire donc","en somme résume, donc déduit",
          "« En somme, nous voterons » est bancal : on n'a rien résumé. Employez « par conséquent » ou « donc »."],
         ["en semer à chaque phrase","un par mouvement",
          "Trois connecteurs dans deux phrases donnent l'impression d'un texte administratif. Un par changement de sujet suffit."],
       ]},

      {t:'check', h:"Est-ce que c'est clair maintenant ?",
       p:"Quatre emplois.",
       qs:[
         {q:"Pour passer au point suivant, on emploie…", opts:["quant à","autrement dit"], ok:0,
          fb:"« Quant à la chanson… » : on change de sujet."},
         {q:"Pour redire plus simplement, on emploie…", opts:["autrement dit","par conséquent"], ok:0,
          fb:"« Autrement dit » reformule."},
         {q:"« ___ , nous voterons à main levée. »", opts:["Par conséquent","En somme"], ok:0,
          fb:"On tire une conséquence, on ne résume pas."},
         {q:"L'orthographe correcte est…", opts:["quant à","quand à"], ok:0,
          fb:"Rien à voir avec le temps."},
       ]},

      {t:'revoir', h:"À retenir",
       p:"<b>Quant à / en ce qui concerne</b> annoncent. <b>Autrement dit</b> reformule. <b>En somme</b> ramasse. <b>Par conséquent</b> déduit. <b>Cela dit</b> nuance. Un par mouvement, pas davantage."},
    ]
  },

  t3plan: {
    eye:'Mini-leçon', tit:"Le plan d'un commentaire d'une minute trente",
    blocs:[
      {t:'texte', h:"Quatre morceaux, toujours les mêmes",
       p:"Résumé, avis, moment précis, concession. Dans cet ordre, cela tient en une minute trente et personne ne peut vous répondre « ah bon ». C'est le plan de l'intervention de Marilou jeudi, c'est le plan de la production orale de « Je me lance », et c'est celui de la lettre que vous écrirez ensuite.",
       note:"On l'oublie presque toujours au troisième morceau. Notez-le sur un papier avant de parler."},

      {t:'ana', h:"1. Le résumé — deux ou trois phrases, sans la fin",
       p:"Ceux qui n'ont pas vu l'œuvre doivent pouvoir suivre. Au présent, comme toujours quand on raconte une œuvre.",
       mots:[['Ce qu\'on donne','le lieu, les personnages, la situation de départ'],['Ce qu\'on ne donne jamais','le dénouement'],['La longueur','deux ou trois phrases, pas davantage']],
       say:"Ça se passe dans une boulangerie de nuit, à Gatineau, sur huit nuits de travail.",
       note:"Raconter toute l'histoire est la faute la plus courante : votre auditoire décroche avant votre avis."},

      {t:'ana', h:"2. L'avis, annoncé comme un avis",
       p:"Un verbe qui dit que c'est vous qui parlez.",
       mots:[['Les verbes','je propose · j\'ai trouvé · il m\'a semblé · j\'ai été touchée'],['Ce qu\'il ne faut pas dire','« ce film est ennuyant », qui se présente comme un fait'],['Pourquoi','l\'autre peut ne pas être d\'accord sans vous contredire']],
       say:"Je propose le film. J'ai trouvé la deuxième heure très forte.",
       note:"Une mise en relief va très bien ici : « ce qui m'a convaincue, c'est… »."},

      {t:'ana', h:"3. Le moment précis — le morceau qui convainc",
       p:"Un seul, court, que les autres peuvent retrouver.",
       mots:[['Un bon moment','« À la quatrième nuit, il la laisse pétrir seule et sort fumer. »'],['Un mauvais moment','« Il y a plein de belles scènes. »'],['La longueur','une phrase']],
       say:"À la quatrième nuit, il la laisse pétrir seule et il sort fumer.",
       note:"C'est le morceau qui manque presque toujours, et c'est le seul que personne ne peut balayer."},

      {t:'ana', h:"4. La concession — avant votre position",
       p:"Accordez le point vrai, puis maintenez.",
       mots:[['La forme parlée','« C\'est vrai que… » · « Je te l\'accorde… »'],['À l\'écrit','« Bien que… » · « Malgré… »'],['La place','avant ce que vous voulez faire retenir']],
       say:"C'est vrai que le premier quart d'heure est lent.",
       note:"Si vous n'avez rien à accorder, cherchez encore : il y a toujours quelque chose de vrai dans l'objection."},

      {t:'labo', h:"Les quatre morceaux, sur les trois œuvres",
       p:"Choisissez une œuvre et un morceau.",
       axes:[
         {id:'o', lbl:'Laquelle des trois ?', opts:[['a','le film'],['b','le sketch'],['c','la chanson']]},
         {id:'m', lbl:'Quelle partie du plan ?', opts:[['1','le résumé'],['2','le moment précis'],['3','la concession']]}],
       out:{
         a1:{w:["Un boulanger de cinquante-huit ans, une étudiante de dix-neuf ans, huit nuits de travail."], say:"Un boulanger de cinquante-huit ans, une étudiante de dix-neuf ans, huit nuits de travail.", n:'trois éléments, pas la fin'},
         a2:{w:["À la quatrième nuit, il la laisse pétrir seule et sort fumer."], say:"À la quatrième nuit, il la laisse pétrir seule et sort fumer.", n:'dix secondes de film'},
         a3:{w:["C'est vrai qu'on peut regarder un film chez soi."], say:"C'est vrai qu'on peut regarder un film chez soi.", n:'un point réellement vrai'},
         b1:{w:["Un homme qui a fait trente ans au comptoir des pièces raconte son travail."], say:"Un homme qui a fait trente ans au comptoir des pièces raconte son travail.", n:'une phrase suffit'},
         b2:{w:["Quand il répond à la cliente : Madame, moi ça fait trente ans."], say:"Quand il répond à la cliente : Madame, moi ça fait trente ans.", n:'la chute, citée'},
         b3:{w:["Je te l'accorde : dans une salle, le rire est contagieux."], say:"Je te l'accorde : dans une salle, le rire est contagieux.", n:'l\'argument de l\'autre, repris'},
         c1:{w:["Une femme monte ses sacs d'épicerie au troisième étage, et c'est tout."], say:"Une femme monte ses sacs d'épicerie au troisième étage, et c'est tout.", n:'ce qui se voit'},
         c2:{w:["Le vers où elle dit qu'elle l'a dit neuf fois."], say:"Le vers où elle dit qu'elle l'a dit neuf fois.", n:'un vers, pas un couplet'},
         c3:{w:["C'est vrai que le refrain monte trop haut pour elle."], say:"C'est vrai que le refrain monte trop haut pour elle.", n:'le défaut, reconnu'},
       },
       note:"Douze phrases, quatre morceaux, trois œuvres : le plan tient sur toutes."},

      {t:'piege', h:"Trois pièges",
       rows:[
         ["raconter le film au complet","deux ou trois phrases, sans la fin",
          "Le résumé n'est pas le but : c'est ce qui permet aux autres de suivre votre avis. Passé une minute, plus personne n'attend l'avis."],
         ["donner cinq raisons","en donner une, précise",
          "Cinq raisons molles se réfutent une par une. Un moment précis que tout le monde a vu ne se réfute pas."],
         ["mettre la concession à la fin","la mettre avant",
          "« Le film tient, bien qu'il soit lent » finit sur la lenteur. « Bien qu'il soit lent, le film tient » finit sur votre position."],
       ]},

      {t:'check', h:"Est-ce que c'est clair maintenant ?",
       p:"Quatre questions sur le plan.",
       qs:[
         {q:"Le résumé se fait…", opts:["au présent, sans la fin","au passé, avec la fin"], ok:0,
          fb:"On raconte une œuvre au présent, et on garde le dénouement."},
         {q:"Le morceau qu'on oublie le plus souvent est…", opts:["le moment précis","l'avis"], ok:0,
          fb:"C'est pourtant le seul qui convainc."},
         {q:"Où se place la concession, déjà ?", opts:["avant sa position","tout à la fin, après la position"], ok:0,
          fb:"On finit sur ce qu'on veut faire retenir."},
         {q:"« Il y a plein de belles scènes » est…", opts:["un moment trop vague","un bon moment précis"], ok:0,
          fb:"Personne ne peut aller vérifier « plein »."},
       ]},

      {t:'revoir', h:"À retenir",
       p:"<b>Résumé</b> (deux ou trois phrases, sans la fin) · <b>avis</b> (annoncé comme un avis) · <b>moment précis</b> (un seul, court) · <b>concession</b> (avant votre position, sur un point vrai). Une minute trente, et la discussion peut commencer."},
    ]
  },

};
