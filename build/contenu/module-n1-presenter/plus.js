const PLUS = {
  prAlpha: {
    eye:'Mini-leçon', tit:"Épeler son nom",
    blocs:[
      {t:'texte', h:"On vous le demandera souvent",
       p:"Au centre, à la clinique, à la banque, au téléphone. Un nom qui ne vient pas d'ici ne s'écrit pas comme il se prononce : la personne en face ne peut pas le deviner. Elle vous demandera de l'<b>épeler</b> — de dire les lettres une par une.",
       note:"Ce n'est pas un signe qu'on parle mal. On demande aussi aux gens nés ici d'épeler leur nom de famille."},

      {t:'ana', h:"Une lettre à la fois",
       p:"Lentement, avec une petite pause.",
       mots:[['On écrit','Amina'],['On épelle','A — M — I — N — A',true],['On ne dit pas','« amina » vite']],
       say:"A, M, I, N, A. Amina.",
       note:"Dire le mot en entier après l'avoir épelé aide la personne à vérifier."},

      {t:'ana', h:"Les lettres qui se ressemblent",
       p:"Trois paires font presque toutes les erreurs.",
       mots:[['E et I','« eu » et « i »'],['G et J','« jé » et « ji »'],['M et N','« èm » et « èn »',true]],
       say:"E, I. G, J. M, N.",
       note:"Si votre nom en contient une, attendez-vous à la répéter. Ce n'est pas votre faute."},

      {t:'ana', h:"Le truc qui marche",
       p:"Donner un mot avec la lettre.",
       mots:[['On dit','B comme bonjour'],['Ou','M comme maman'],['Tout le monde le fait','même les gens d\'ici',true]],
       say:"B comme bonjour, E comme enfant, N comme non.",
       note:"Choisissez d'avance un mot par lettre difficile de votre nom. Vous n'aurez plus à chercher."},

      {t:'labo', h:"Épelez ces noms",
       p:"Choisissez un nom et écoutez.",
       axes:[{id:'p', lbl:'Quel nom ?', opts:[
         ['a','Amina'],
         ['b','Benali'],
         ['c','Lin'],
         ['d','Tremblay'],
         ['e','votre nom']]}],
       out:{
         a:{w:['A — M — I — N — A'], say:"A, M, I, N, A. Amina.", n:'cinq lettres, deux A'},
         b:{w:['B — E — N — A — L — I'], say:"B, E, N, A, L, I. Benali.", n:'attention au E et au I'},
         c:{w:['L — I — N'], say:"L, I, N. Lin.", n:'trois lettres seulement'},
         d:{w:['T — R — E — M — B — L — A — Y'], say:"T, R, E, M, B, L, A, Y. Tremblay.", n:'un nom d\'ici, long à épeler'},
         e:{w:['à vous'], say:"Et maintenant, votre nom.", n:'écrivez-le, puis épelez-le à voix haute'},
       },
       note:"Écoutez, puis répétez. Faites une pause entre chaque lettre."},

      {t:'ex', h:"À écouter et à répéter",
       p:"Six phrases du premier jour.",
       rows:[
         ["Comment vous appelez-vous ?","la question"],
         ["Je m'appelle Amina.","la réponse"],
         ["Pouvez-vous épeler ?","on vous le demandera"],
         ["A, M, I, N, A.","lentement"],
         ["B comme bonjour.","le truc qui marche"],
         ["Mon nom de famille, c'est Benali.","le nom de famille"],
       ]},

      {t:'piege', h:"Trois pièges à connaître",
       rows:[
         ["épeler vite","« amina » d'un seul souffle",
          "Vite, les lettres se collent et personne ne les distingue. Une petite pause entre chaque lettre suffit."],
         ["mélanger nom et prénom","« Benali Amina » ou « Amina Benali » ?",
          "Ici, on dit et on écrit d'abord le <b>prénom</b>, puis le <b>nom de famille</b> : Amina Benali. Sur les formulaires, les deux cases sont séparées et nommées."],
         ["ne pas oser faire répéter","on écrit votre nom de travers, et ça reste",
          "Un nom mal écrit sur un dossier suit longtemps. Demandez à voir, ou épelez une deuxième fois."],
       ]},

      {t:'check', h:"Est-ce que c'est clair maintenant ?",
       p:"Quatre questions rapides.",
       qs:[
         {q:"« Épeler », c'est…", opts:["dire les lettres une par une","parler vite"], ok:0,
          fb:"Une lettre à la fois, avec une petite pause."},
         {q:"Ici, on dit d'abord…", opts:["le nom de famille","le prénom"], ok:1,
          fb:"Amina Benali : le prénom, puis le nom de famille."},
         {q:"« B comme bonjour » sert à…", opts:["rendre la lettre claire","dire bonjour"], ok:0,
          fb:"C'est le truc que tout le monde emploie."},
         {q:"On vous demande d'épeler parce que…", opts:["vous parlez mal","le nom ne se devine pas"], ok:1,
          fb:"On le demande aussi aux gens nés ici."},
       ]},
    ]
  },

  t1etre: {
    eye:'Mini-leçon', tit:"Les cinq phrases pour se présenter",
    blocs:[
      {t:'texte', h:"Cinq phrases, et c'est tout",
       p:"Se présenter tient en cinq phrases : <b>je m'appelle</b>, <b>je viens de</b>, <b>j'habite à</b>, <b>je parle</b>, <b>j'ai</b>. Ce sont les mêmes partout — au centre, chez le médecin, au travail, avec un voisin. Une fois sues, elles servent toute la vie.",
       note:"Il n'est pas nécessaire de tout dire à chaque fois. Le nom suffit souvent."},

      {t:'ana', h:"Je m'appelle, je suis",
       p:"Deux façons de dire qui on est.",
       mots:[['Le nom','Je {m\'appelle} Amina.'],['Le métier','Je {suis} mécanicienne.'],['Le pays','Je {suis} algérienne.',true]],
       say:"Je m'appelle Amina. Je suis algérienne.",
       note:"Devant un métier ou une nationalité, on ne met pas « un » ni « une » : « je suis mécanicienne », pas « je suis une mécanicienne »."},

      {t:'ana', h:"J'ai",
       p:"Pour les enfants et pour l'âge.",
       mots:[['Les enfants','J\'{ai} un enfant.'],['L\'âge','J\'{ai} trente ans.'],['La négation','Je n\'{ai pas} d\'enfants.',true]],
       say:"J'ai un enfant. Il a six ans.",
       note:"En français, on <b>a</b> un âge : « j'ai trente ans », et non « je suis trente ans »."},

      {t:'ana', h:"Je parle",
       p:"Sans article devant la langue.",
       mots:[['On dit','Je {parle} arabe.'],['Aussi','Je parle {un peu} français.'],['On ne dit pas','je parle l\'arabe',true]],
       say:"Je parle arabe et un peu français.",
       note:"« Un peu » est une phrase honnête et très utile au début. Personne ne s'attend à ce que vous parliez parfaitement."},

      {t:'labo', h:"Présentez-vous",
       p:"Choisissez une phrase et une personne.",
       axes:[
         {id:'p', lbl:'Quelle phrase ?', opts:[['a','le nom'],['b','le pays'],['c','la langue'],['d','les enfants']]},
         {id:'q', lbl:'Qui parle ?', opts:[['1','Amina'],['2','Lin'],['3','vous']]}],
       out:{
         a1:{w:["Je m'appelle Amina."], say:"Je m'appelle Amina.", n:'la première phrase, partout'},
         a2:{w:["Moi, c'est Lin."], say:"Moi, c'est Lin.", n:'plus court, entre camarades'},
         a3:{w:["Je m'appelle…"], say:"Je m'appelle…", n:'dites votre nom, puis épelez-le'},
         b1:{w:["Je viens d'Algérie."], say:"Je viens d'Algérie.", n:"d' devant une voyelle"},
         b2:{w:["Je viens du Vietnam."], say:"Je viens du Vietnam.", n:'du devant un pays masculin'},
         b3:{w:["Je viens de…"], say:"Je viens de…", n:'apprenez votre pays par cœur'},
         c1:{w:["Je parle arabe et un peu français."], say:"Je parle arabe et un peu français.", n:'« un peu » est honnête et utile'},
         c2:{w:["Je parle vietnamien et anglais."], say:"Je parle vietnamien et anglais.", n:'sans article devant la langue'},
         c3:{w:["Je parle…"], say:"Je parle…", n:'nommez toutes vos langues : c\'est une force'},
         d1:{w:["J'ai un fils. Il a six ans."], say:"J'ai un fils. Il a six ans.", n:'on a un âge, en français'},
         d2:{w:["J'ai deux enfants."], say:"J'ai deux enfants.", n:'le nombre devant'},
         d3:{w:["J'ai… / Je n'ai pas d'enfants."], say:"Je n'ai pas d'enfants.", n:'la négation : n\'ai pas d\''},
       },
       note:"Douze phrases. Choisissez les vôtres et dites-les à voix haute trois fois."},

      {t:'ex', h:"À écouter et à répéter",
       p:"Les cinq phrases, dans l'ordre.",
       rows:[
         ["Je m'appelle Amina Benali.","le nom"],
         ["Je viens d'Algérie.","le pays"],
         ["J'habite à Montréal.","la ville"],
         ["Je parle arabe et un peu français.","les langues"],
         ["J'ai un fils. Il a six ans.","la famille"],
         ["Je suis mécanicienne.","le métier"],
       ]},

      {t:'piege', h:"Trois pièges à connaître",
       rows:[
         ["« je suis une mécanicienne »","je suis mécanicienne",
          "Devant un métier ou une nationalité, pas d'article : « je suis infirmière », « je suis brésilien »."],
         ["« je suis trente ans »","j'ai trente ans",
          "En français, l'âge se dit avec <b>avoir</b>. C'est différent de beaucoup de langues, et l'erreur est très fréquente."],
         ["« je parle le français »","je parle français",
          "Sans article devant la langue, après le verbe parler. On dit toutefois « j'apprends <b>le</b> français »."],
       ]},

      {t:'check', h:"Est-ce que c'est clair maintenant ?",
       p:"Quatre questions rapides.",
       qs:[
         {q:"Pour l'âge, on emploie…", opts:["avoir","être"], ok:0,
          fb:"J'ai trente ans."},
         {q:"« Je suis… » devant un métier prend…", opts:["un article","pas d'article"], ok:1,
          fb:"Je suis mécanicienne."},
         {q:"Après « je parle », on met…", opts:["la langue seule","l'article puis la langue"], ok:0,
          fb:"Je parle arabe."},
         {q:"« Je n'ai pas d'enfants » est…", opts:["correct","incorrect"], ok:0,
          fb:"À la négation, « un » devient « d' »."},
       ]},
    ]
  },

  t1venir: {
    eye:'Mini-leçon', tit:"De, du, d' — devant le pays",
    blocs:[
      {t:'texte', h:"Un petit mot qui change",
       p:"« Je viens <b>d'</b>Algérie », « je viens <b>du</b> Vietnam », « je viens <b>de</b> France », « je viens <b>des</b> Philippines ». Le petit mot change selon le pays — et il ne se devine pas. La bonne nouvelle : vous n'avez besoin d'apprendre que le vôtre.",
       note:"Personne ne connaît la forme de tous les pays, même parmi les gens nés ici."},

      {t:'ana', h:"d' devant une voyelle",
       p:"Le plus facile à entendre.",
       mots:[['On dit','Je viens {d\'}Algérie.'],['Aussi','d\'Haïti · d\'Iran · d\'Ukraine'],['Pourquoi','le pays commence par une voyelle',true]],
       say:"Je viens d'Algérie.",
       note:"Le H de Haïti ne compte pas : on dit « d'Haïti », comme devant une voyelle."},

      {t:'ana', h:"du et de",
       p:"Selon le genre du pays.",
       mots:[['Masculin','Je viens {du} Vietnam.'],['Féminin','Je viens {de} France.'],['Aussi','du Maroc, du Brésil · de Chine, de Syrie',true]],
       say:"Je viens du Vietnam. Je viens de France.",
       note:"Les pays qui finissent par -e sont souvent féminins : la France, la Chine, la Syrie. Souvent, pas toujours."},

      {t:'ana', h:"des devant un pluriel",
       p:"Quelques pays sont au pluriel.",
       mots:[['On dit','Je viens {des} Philippines.'],['Aussi','des États-Unis · des Pays-Bas'],['Ils sont rares','trois ou quatre en tout',true]],
       say:"Je viens des Philippines.",
       note:"Le nom du pays est écrit au pluriel : c'est le signe qu'il faut « des »."},

      {t:'labo', h:"Choisissez un pays",
       p:"Écoutez la phrase complète.",
       axes:[{id:'p', lbl:'Quel pays ?', opts:[
         ['a','Algérie'],
         ['b','Vietnam'],
         ['c','France'],
         ['d','Philippines'],
         ['e','Haïti'],
         ['f','Colombie']]}],
       out:{
         a:{w:["Je viens d'Algérie."], say:"Je viens d'Algérie.", n:"d' — voyelle"},
         b:{w:['Je viens du Vietnam.'], say:"Je viens du Vietnam.", n:'du — masculin'},
         c:{w:['Je viens de France.'], say:"Je viens de France.", n:'de — féminin'},
         d:{w:['Je viens des Philippines.'], say:"Je viens des Philippines.", n:'des — pluriel'},
         e:{w:["Je viens d'Haïti."], say:"Je viens d'Haïti.", n:"d' — le H ne compte pas"},
         f:{w:['Je viens de Colombie.'], say:"Je viens de Colombie.", n:'de — féminin'},
       },
       note:"Trouvez le vôtre dans la liste, ou demandez-le à votre enseignante. Puis apprenez-le par cœur."},

      {t:'ex', h:"À écouter et à répéter",
       p:"Six phrases.",
       rows:[
         ["Je viens d'Algérie.","d' — voyelle"],
         ["Je viens du Vietnam.","du — masculin"],
         ["Je viens de France.","de — féminin"],
         ["Je viens des Philippines.","des — pluriel"],
         ["J'habite à Montréal.","à — devant une ville"],
         ["J'habite au Canada.","au — devant un pays masculin"],
       ]},

      {t:'piege', h:"Trois pièges à connaître",
       rows:[
         ["confondre la ville et le pays","« j'habite à Canada »",
          "Devant une <b>ville</b> : à Montréal, à Laval, à Québec. Devant un <b>pays</b> : au Canada, en France, au Vietnam."],
         ["chercher une règle simple","il n'y en a pas",
          "Le genre des pays s'apprend un par un. Pour se présenter, un seul suffit : le vôtre."],
         ["oublier l'apostrophe","« je viens de Algérie »",
          "Devant une voyelle, « de » devient « d' » et se colle au mot : d'Algérie."],
       ]},

      {t:'check', h:"Est-ce que c'est clair maintenant ?",
       p:"Quatre questions rapides.",
       qs:[
         {q:"Je viens ___ Algérie.", opts:["d'","du"], ok:0,
          fb:"Devant une voyelle, toujours « d' »."},
         {q:"Je viens ___ Vietnam.", opts:["de","du"], ok:1,
          fb:"Le Vietnam est masculin."},
         {q:"J'habite ___ Montréal.", opts:["à","au"], ok:0,
          fb:"Devant une ville : à."},
         {q:"Je viens ___ Philippines.", opts:["de","des"], ok:1,
          fb:"Le nom est au pluriel."},
       ]},
    ]
  },

  t2poli: {
    eye:'Mini-leçon', tit:"Saluer, remercier, faire répéter",
    blocs:[
      {t:'texte', h:"Six phrases, et on est poli partout",
       p:"<b>Bonjour</b>, <b>merci</b>, <b>de rien</b>, <b>pardon</b>, <b>je ne comprends pas</b>, <b>plus lentement, s'il vous plaît</b>. Six phrases suffisent pour être poli dans tous les commerces et tous les bureaux. Les deux dernières sont les plus utiles — et celles qu'on ose le moins dire.",
       note:"Ici, on dit bonjour en entrant dans un magasin, même si on n'achète rien."},

      {t:'ana', h:"Bonjour, bonsoir",
       p:"Selon le moment de la journée.",
       mots:[['Le jour','{Bonjour}'],['Le soir','{Bonsoir}'],['En partant','Bonne journée · Bonne soirée',true]],
       say:"Bonjour ! Bonne journée !",
       note:"« Bonjour » se dit en arrivant. En partant, on dit « bonne journée » ou « bonne soirée » — pas « bonjour »."},

      {t:'ana', h:"Merci, de rien",
       p:"On remercie beaucoup, ici.",
       mots:[['On dit','{Merci} beaucoup.'],['On répond','{De rien.}'],['Ou','Bienvenue · Ça me fait plaisir',true]],
       say:"Merci beaucoup. — De rien.",
       note:"Au Québec, « bienvenue » veut souvent dire « de rien ». Ce n'est pas une invitation à entrer."},

      {t:'ana', h:"Je ne comprends pas",
       p:"Une phrase de la langue, comme les autres.",
       mots:[['On dit','{Pardon ?}'],['Ou','Je ne {comprends} pas.'],['Le mieux','{Plus lentement}, s\'il vous plaît.',true]],
       say:"Pardon ? Plus lentement, s'il vous plaît.",
       note:"Ce n'est pas le volume qui manque, c'est la vitesse. Demander de ralentir marche mieux que de faire répéter."},

      {t:'labo', h:"Que dites-vous ?",
       p:"Choisissez une situation.",
       axes:[{id:'p', lbl:'Quelle situation ?', opts:[
         ['a','vous entrez le matin'],
         ['b','vous entrez le soir'],
         ['c','on vous aide'],
         ['d','on vous dit merci'],
         ['e','vous ne comprenez pas'],
         ['f','vous partez']]}],
       out:{
         a:{w:['Bonjour !'], say:"Bonjour !", n:'même si on n\'achète rien'},
         b:{w:['Bonsoir !'], say:"Bonsoir !", n:'à partir de la fin de l\'après-midi'},
         c:{w:['Merci beaucoup.'], say:"Merci beaucoup.", n:'on remercie souvent, ici'},
         d:{w:['De rien.'], say:"De rien.", n:'ou « bienvenue », qui veut dire la même chose'},
         e:{w:["Pardon ? Plus lentement, s'il vous plaît."], say:"Pardon ? Plus lentement, s'il vous plaît.", n:'la phrase la plus utile du module'},
         f:{w:['Bonne journée !'], say:"Bonne journée !", n:'en partant, jamais « bonjour »'},
       },
       note:"Six situations, six phrases. Elles reviennent chaque jour."},

      {t:'ex', h:"À écouter et à répéter",
       p:"Six phrases de politesse.",
       rows:[
         ["Bonjour, madame.","en arrivant"],
         ["Merci beaucoup.","pour remercier"],
         ["De rien.","la réponse"],
         ["Pardon ?","pour faire répéter"],
         ["Je ne comprends pas.","c'est permis"],
         ["Plus lentement, s'il vous plaît.","la meilleure"],
       ]},

      {t:'piege', h:"Trois pièges à connaître",
       rows:[
         ["dire « bonjour » en partant","on dit « bonne journée »",
          "« Bonjour » sert à arriver. Pour partir : bonne journée, bonne soirée, à demain, au revoir."],
         ["faire oui de la tête sans comprendre","et se tromper de salle, de jour, de prix",
          "Dire « je ne comprends pas » n'est pas un échec : c'est une phrase de la langue, aussi normale que bonjour."],
         ["croire que « bienvenue » veut dire « entrez »","ici, ça veut dire « de rien »",
          "Quand vous dites merci et qu'on vous répond « bienvenue », on ne vous invite pas : on vous répond."],
       ]},

      {t:'check', h:"Est-ce que c'est clair maintenant ?",
       p:"Quatre questions rapides.",
       qs:[
         {q:"En partant, le matin, on dit…", opts:["bonjour","bonne journée"], ok:1,
          fb:"« Bonjour » sert à arriver."},
         {q:"On vous dit merci. Vous répondez…", opts:["de rien","merci"], ok:0,
          fb:"Ou « bienvenue », qui veut dire la même chose ici."},
         {q:"Vous n'avez pas compris. Le mieux est…", opts:["de faire oui de la tête","de demander de parler plus lentement"], ok:1,
          fb:"Ce n'est pas le volume qui manque, c'est la vitesse."},
         {q:"« Bienvenue », après un merci, veut dire…", opts:["entrez","de rien"], ok:1,
          fb:"C'est la réponse habituelle à « merci » au Québec."},
       ]},
    ]
  },
};
