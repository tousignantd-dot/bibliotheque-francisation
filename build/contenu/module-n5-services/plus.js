const PLUS = {

  // ════════════════════════════════════════════════════════════════════════
  prPhon: {
    eye:'Mini-leçon', tit:"Les trois voyelles nasales, et pourquoi elles décident de tout au téléphone",
    blocs:[
      {t:'texte', h:"Trois sons qui n'existent pas dans beaucoup de langues",
       p:"Une voyelle nasale se fait en laissant passer l'air par le nez <b>en même temps</b> que par la bouche. Le français en emploie trois couramment, et l'administration les met partout : dans « att<b>en</b>te », dans « informati<b>on</b> », dans « mat<b>in</b> ». Si votre langue n'en a pas, votre oreille les entend d'abord comme une seule et même chose.",
       note:"La bonne nouvelle : elles sont trois, pas trente. Une heure de travail sérieux sur ces trois-là change la compréhension de tous les appels que vous ferez ensuite."},

      {t:'ana', h:"[ɑ̃] — le son ouvert de « attente »",
       p:"Bouche grande ouverte, langue tirée vers l'arrière. C'est le plus grave des trois.",
       mots:[['On écrit','an, am, en, em'],['On entend','la bouche ouverte, son grave',true],['Dans ce module','attente · résidence · renseignement · en vigueur']],
       say:"Le temps d'attente est d'environ quatre minutes.",
       note:"Attention : « en » se lit [ɑ̃] presque toujours, sauf après un i, où il devient [ɛ̃] — bien, rien, combien."},

      {t:'ana', h:"[ɔ̃] — le son rond de « nom »",
       p:"Lèvres arrondies et poussées vers l'avant, comme pour siffler.",
       mots:[['On écrit','on, om'],['On entend','les lèvres en rond',true],['Dans ce module','mon nom · une réponse · une information · une confirmation']],
       say:"Je vous donne mon nom et mon numéro de dossier.",
       note:"Regardez-vous dans une vitre en le disant : si vos lèvres ne forment pas un rond visible, ce n'est pas encore [ɔ̃]."},

      {t:'ana', h:"[ɛ̃] — le son étiré de « matin »",
       p:"Bouche étirée sur les côtés, comme au début d'un sourire.",
       mots:[['On écrit','in, im, ain, ein, yn'],['On entend','les lèvres étirées',true],['Dans ce module','le matin · certain · plein · le train']],
       say:"Le camion passe le mardi matin, avant sept heures.",
       note:"Au Québec, « un » et « brun » se prononcent souvent [œ̃], un quatrième son. Vous serez compris dans tous les cas si vous dites [ɛ̃] — n'en faites pas une inquiétude."},

      {t:'labo', h:"Écoutez les trois, une paire à la fois",
       p:"Choisissez une opposition et écoutez-la dans sa phrase.",
       axes:[{id:'n', lbl:'Quelle paire ?', opts:[
         ['a','[ɑ̃] contre [ɔ̃]'],
         ['b','[ɑ̃] contre [ɛ̃]'],
         ['c','[ɔ̃] contre [ɛ̃]'],
         ['d','les trois de suite'],
         ['e','la nasale qui disparaît']]}],
       out:{
         a:{w:['attente / information'], say:"Le temps d'attente et l'information sont sur le site.", n:"bouche ouverte, puis lèvres en rond"},
         b:{w:['résidence / matin'], say:"Ma preuve de résidence, je l'ai apportée ce matin.", n:"bouche ouverte, puis lèvres étirées"},
         c:{w:['réponse / certain'], say:"Je n'ai pas eu de réponse, c'est certain.", n:"lèvres en rond, puis étirées"},
         d:{w:['attente · nom · matin'], say:"En attente, j'ai donné mon nom, un mardi matin.", n:"les trois positions à la suite"},
         e:{w:['an-née, et non [ɑ̃]-née'], say:"Quatre visites gratuites par année.", n:"le n suivi d'une voyelle annule la nasale"},
       },
       note:"Écoutez chaque phrase deux fois : la première pour comprendre, la seconde en ne guettant que la voyelle."},

      {t:'ex', h:"À écouter et à répéter",
       p:"Six phrases prises dans les appels de ce module.",
       rows:[
         ["Le temps d'attente est d'environ quatre minutes.","[ɑ̃] trois fois"],
         ["Je vous donne mon nom et mon code postal.","[ɔ̃] trois fois"],
         ["Le camion passe le mardi matin.","[ɔ̃] puis [ɛ̃]"],
         ["J'aimerais un renseignement sur les tarifs en vigueur.","[ɑ̃] partout"],
         ["Je voudrais savoir si vous avez reçu ma demande.","aucune nasale : écoutez la différence"],
         ["Je n'ai pas eu de réponse, et c'est certain.","[ɔ̃] puis [ɛ̃]"],
       ]},

      {t:'piege', h:"Trois pièges de la nasale",
       rows:[
         ["nasaliser devant une voyelle","« une an-née » dit [ɑ̃-ne]",
          "Quand le n ou le m est suivi d'une voyelle, la nasale disparaît : an-née, ma-tin-ée, bon-ne. Beaucoup d'élèves nasalisent partout et deviennent difficiles à suivre."],
         ["prononcer le n final","« nom » dit « nomme »",
          "La consonne nasale ne se dit pas : elle a fondu dans la voyelle. « nom » est une seule voyelle, rien de plus."],
         ["confondre [ɔ̃] et [ɑ̃] en donnant son nom","« mon nom » / « ma-n-en »",
          "C'est l'endroit où ça coûte le plus cher : un préposé qui ne saisit pas votre nom vous fait épeler trois fois. Arrondissez franchement les lèvres."],
       ]},

      {t:'check', h:"Est-ce que c'est clair maintenant ?",
       p:"Quatre questions rapides.",
       qs:[
         {q:"Dans « attente », la voyelle nasale est…", opts:["[ɑ̃]","[ɔ̃]"], ok:0,
          fb:"Bouche ouverte, son grave : c'est [ɑ̃]."},
         {q:"Pour faire [ɔ̃], les lèvres sont…", opts:["étirées","arrondies"], ok:1,
          fb:"Arrondies et poussées en avant, comme pour siffler."},
         {q:"Dans « une année », le « an » se prononce…", opts:["[ɑ̃]","[a] — la nasale disparaît"], ok:1,
          fb:"Le n est suivi d'une voyelle : a-nnée."},
         {q:"« bien » et « combien » se terminent par…", opts:["[ɑ̃]","[ɛ̃]"], ok:1,
          fb:"Après un i, « en » devient [ɛ̃]."},
       ]},
    ]
  },

  // ════════════════════════════════════════════════════════════════════════
  prReg: {
    eye:'Mini-leçon', tit:"La langue de l'administration",
    blocs:[
      {t:'texte', h:"Ce n'est pas du français compliqué pour rien",
       p:"Un service public emploie des mots à lui parce qu'ils sont <b>précis</b> et qu'ils ont une valeur légale. « Les vidanges » et « les matières résiduelles » désignent la même chose, mais un seul des deux se trouve dans un règlement, et c'est celui-là qui décide de ce que le camion ramasse.",
       note:"Personne ne vous demande de parler comme ça avec votre voisin. Ce qu'il faut, c'est <b>reconnaître</b> ces mots et pouvoir les employer quand vous vous adressez au service."},

      {t:'ana', h:"une demande → une requête",
       p:"Le mot le plus utile de tout le module.",
       mots:[['Au quotidien','j\'ai fait une demande'],['Au service','j\'ai ouvert une requête',true],['Pourquoi','une requête porte un numéro']],
       say:"Est-ce que vous ouvrez une requête pour ma demande ?",
       note:"Une demande qui n'est pas enregistrée comme requête n'existe pas : rien à retrouver, rien à rappeler. Posez la question à voix haute."},

      {t:'ana', h:"le temps que ça prend → le délai",
       p:"Et il se compte en jours ouvrables.",
       mots:[['Au quotidien','ça prend combien de temps ?'],['Au service','quel est le délai de traitement ?',true],['Attention','trois jours ouvrables ≠ trois jours']],
       say:"Le délai de traitement est de trois jours ouvrables.",
       note:"Un délai de trois jours ouvrables donné un jeudi vous amène au mardi suivant. C'est la source de malentendu la plus fréquente."},

      {t:'ana', h:"un papier qui prouve → une pièce justificative",
       p:"Et « la personne au comptoir » est un préposé.",
       mots:[['Au quotidien','un papier de mon propriétaire'],['Au service','une pièce justificative',true],['Aussi','le monsieur au comptoir → le préposé']],
       say:"Joignez une pièce justificative à votre demande.",
       note:"« Pièce » tout court suffit souvent : deux pièces d'identité, la pièce manquante, la pièce au dossier."},

      {t:'ex', h:"Le même sens, deux registres",
       p:"Six paires à écouter et à répéter.",
       rows:[
         ["On dit « j'ai fait une demande », et au service « j'ai ouvert une requête ».","demande / requête"],
         ["On dit « ça prend combien de temps ? », et au service « quel est le délai ? ».","temps / délai"],
         ["On dit « les vidanges », et au service « les matières résiduelles ».","vidanges / matières résiduelles"],
         ["On dit « le monsieur au comptoir », et au service « le préposé ».","monsieur / préposé"],
         ["On dit « les prix d'astheure », et au service « les tarifs en vigueur ».","d'astheure / en vigueur"],
         ["On dit « les jours de semaine », et au service « les jours ouvrables ».","semaine / ouvrables"],
       ]},

      {t:'piege', h:"Deux pièges de registre",
       rows:[
         ["trop soutenu au téléphone","« Je sollicite votre bienveillante attention »",
          "Ce n'est pas mieux, c'est bizarre. Un service public parle un français clair et courant, pas un français de lettre du dix-neuvième siècle. Restez simple et poli."],
         ["trop familier à l'écrit","« Salut, mon bac est pas ramassé »",
          "Le courriel à un service commence par « Bonjour, » et emploie « vous ». Ce n'est pas de la distance : c'est ce qui fait traiter votre demande comme une demande."],
       ]},

      {t:'check', h:"Est-ce que c'est clair maintenant ?",
       p:"Trois questions rapides.",
       qs:[
         {q:"Une demande enregistrée par un service s'appelle…", opts:["une requête","une plainte"], ok:0,
          fb:"Une requête — et elle porte un numéro."},
         {q:"« Trois jours ouvrables », un jeudi, vous amène…", opts:["au dimanche","au mardi suivant"], ok:1,
          fb:"On ne compte ni le samedi ni le dimanche."},
         {q:"« En vigueur » veut dire…", opts:["qui s'applique en ce moment","qui s'appliquera bientôt"], ok:0,
          fb:"C'est ce qui compte aujourd'hui."},
       ]},
    ]
  },

  // ════════════════════════════════════════════════════════════════════════
  t1inter: {
    eye:'Mini-leçon', tit:"Demander sans questionner : la subordonnée interrogative",
    blocs:[
      {t:'texte', h:"Pourquoi une phrase plus longue est plus polie",
       p:"« Quand est-ce que le camion passe ? » est une question correcte. Mais quand on en pose quatre de suite à un préposé, l'appel devient un interrogatoire. En glissant la question <b>à l'intérieur</b> d'une phrase — « Pouvez-vous me dire quand le camion passe ? » — on demande la même chose en laissant à l'autre le choix de répondre.",
       note:"C'est un point typique du niveau 5 : on ne cherche plus à poser une question, on cherche à mener un échange suivi."},

      {t:'ana', h:"Les trois ouvertures",
       p:"Apprenez-les par cœur : après elles, tout se construit pareil.",
       mots:[['La plus courante','Pouvez-vous me dire…'],['La plus neutre','Je voudrais savoir…',true],['La plus douce','J\'aimerais savoir…']],
       say:"Pouvez-vous me dire à quelle heure il faut sortir le bac ?",
       note:"Elles marchent toutes les trois avec n'importe quel mot de question. Choisissez-en une et tenez-vous-y le temps de l'automatiser."},

      {t:'ana', h:"La règle unique : on remet l'ordre normal",
       p:"Plus de « est-ce que », plus d'inversion. Sujet, puis verbe.",
       mots:[['Question directe','Quand est-ce que le camion passe ?'],['Dans une phrase','…me dire quand le camion passe.',true],['Jamais','…me dire quand est-ce que le camion passe.']],
       say:"Je voudrais savoir quand le camion passe dans ma rue.",
       note:"La question est déjà posée par « je voudrais savoir ». La poser une deuxième fois avec « est-ce que » est l'erreur numéro un."},

      {t:'ana', h:"si — quand la réponse est oui ou non",
       p:"Le mot qui manque le plus souvent aux élèves.",
       mots:[['Question directe','Est-ce que le bac sera vidé ?'],['Dans une phrase','…savoir si le bac sera vidé.',true],['Ce n\'est pas','le « si » de la condition']],
       say:"Je voudrais savoir si le bac sera vidé cette semaine.",
       note:"« Est-ce que » se transforme toujours en « si ». Une fois qu'on tient ça, la moitié des demandes du module se construisent toutes seules."},

      {t:'ana', h:"ce que, ce qui — devant une chose",
       p:"« que » tout seul ne s'emploie pas ici.",
       mots:[['Question directe','Qu\'est-ce qu\'il faut apporter ?'],['Dans une phrase','…me dire ce qu\'il faut apporter.',true],['Sujet','Qu\'est-ce qui manque ? → …ce qui manque.']],
       say:"Pouvez-vous me dire ce qu'il faut apporter au guichet ?",
       note:"Retenez le couple : « qu'est-ce que » → « ce que » ; « qu'est-ce qui » → « ce qui »."},

      {t:'labo', h:"Transformez, puis écoutez",
       p:"Choisissez une question directe et entendez sa version en phrase.",
       axes:[{id:'q', lbl:'Quelle question ?', opts:[
         ['a','Quand est-ce que le camion passe ?'],
         ['b','Est-ce que le bac sera vidé ?'],
         ['c','Qu\'est-ce qu\'il faut apporter ?'],
         ['d','Où est le bureau le plus proche ?'],
         ['e','Combien de temps ça prend ?'],
         ['f','Comment je peux suivre ma requête ?']]}],
       out:{
         a:{w:['quand'], say:"Pouvez-vous me dire quand le camion passe dans ma rue ?", n:"le mot de question ne change pas"},
         b:{w:['si'], say:"Je voudrais savoir si le bac sera vidé cette semaine.", n:"« est-ce que » devient « si »"},
         c:{w:['ce que'], say:"Pouvez-vous me dire ce qu'il faut apporter au guichet ?", n:"« qu'est-ce que » devient « ce que »"},
         d:{w:['où'], say:"J'aimerais savoir où se trouve le bureau le plus proche.", n:"sujet et verbe reprennent l'ordre normal"},
         e:{w:['combien de temps'], say:"Je voudrais savoir combien de temps prend le traitement.", n:"le groupe entier se déplace"},
         f:{w:['comment'], say:"Pouvez-vous me dire comment je peux suivre ma requête ?", n:"rien ne s'inverse après « comment »"},
       },
       note:"Répétez chaque phrase à voix haute avant de passer à la suivante. C'est un automatisme, pas une règle à retenir."},

      {t:'piege', h:"Trois pièges",
       rows:[
         ["garder « est-ce que »","« …me dire quand est-ce que le camion passe »",
          "La question est déjà posée par « me dire ». Une seule fois suffit."],
         ["inverser le sujet","« …savoir où se trouve-t-il le bureau »",
          "Dans une subordonnée, on revient à l'ordre normal : sujet, puis verbe. « …où se trouve le bureau » ou « …où il se trouve »."],
         ["oublier « si »","« …savoir que le bac sera vidé »",
          "« Que » annonce une affirmation, pas une question. Avec « je voudrais savoir », il faut « si »."],
       ]},

      {t:'check', h:"Est-ce que c'est clair maintenant ?",
       p:"Quatre questions rapides.",
       qs:[
         {q:"« Est-ce que le formulaire est arrivé ? » devient « Je voudrais savoir… »", opts:["que le formulaire est arrivé","si le formulaire est arrivé"], ok:1,
          fb:"Réponse oui ou non : c'est « si »."},
         {q:"« Qu'est-ce qu'il faut apporter ? » devient « …me dire… »", opts:["ce qu'il faut apporter","qu'il faut apporter"], ok:0,
          fb:"« qu'est-ce que » → « ce que »."},
         {q:"Après « pouvez-vous me dire où », on écrit…", opts:["se trouve le bureau","se trouve-t-il le bureau"], ok:0,
          fb:"Pas d'inversion dans une subordonnée."},
         {q:"Cette construction sert surtout à…", opts:["être plus poli et enchaîner","poser des questions plus difficiles"], ok:0,
          fb:"C'est ce qui permet un échange suivi plutôt qu'un interrogatoire."},
       ]},
    ]
  },

  // ════════════════════════════════════════════════════════════════════════
  t1modal: {
    eye:'Mini-leçon', tit:"Pouvoir, devoir, falloir",
    blocs:[
      {t:'texte', h:"Trois verbes qui commandent les autres",
       p:"Ils ne disent pas une action : ils disent <b>comment</b> il faut prendre l'action qui suit. Est-ce possible ? Est-ce obligé ? Le verbe qui vient après reste toujours à l'infinitif : « je dois apport<b>er</b> », « vous pouvez rappel<b>er</b> », « il faut sort<b>ir</b> ».",
       note:"Dans une démarche administrative, ces trois verbes portent l'essentiel de l'information : ce que vous avez le droit de faire, ce que vous êtes obligé de faire, et ce que la règle exige de tout le monde."},

      {t:'ana', h:"pouvoir — c'est possible, c'est permis",
       p:"Et c'est aussi la façon normale de demander un service.",
       mots:[['La possibilité','Vous pouvez faire la demande en ligne.'],['La demande polie','Pouvez-vous répéter ?',true],['Le refus','Je n\'ai pas pu terminer.']],
       say:"Pouvez-vous répéter le numéro de requête, s'il vous plaît ?",
       note:"Le participe passé est <b>pu</b>, sans accent et sans e. « J'ai pu », « je n'ai pas pu »."},

      {t:'ana', h:"devoir — c'est obligé, et je sais qui",
       p:"Il y a une personne responsable dans la phrase.",
       mots:[['L\'obligation','Vous devez présenter deux pièces.'],['Au passé','J\'ai dû me déplacer.',true],['Attention','dû prend un accent au masculin singulier']],
       say:"Vous devez présenter deux pièces d'identité au comptoir.",
       note:"« dû » porte son accent uniquement au masculin singulier : dû, mais due, dus, dues."},

      {t:'ana', h:"falloir — c'est obligé, et peu importe qui",
       p:"Il ne se conjugue qu'avec « il ». C'est la forme de l'administration.",
       mots:[['La règle générale','Il faut une preuve de résidence.'],['Avec un infinitif','Il faut sortir le bac avant sept heures.',true],['Au passé','Il a fallu que je rappelle.']],
       say:"Il faut une preuve de résidence pour entrer à l'écocentre.",
       note:"Un règlement emploie « il faut » précisément parce que ça ne désigne personne : la règle vaut pour tout le monde."},

      {t:'ex', h:"À écouter et à répéter",
       p:"Six phrases d'une démarche réelle.",
       rows:[
         ["Pouvez-vous me dire ce qu'il faut apporter ?","demande polie"],
         ["Vous devez présenter deux pièces d'identité.","obligation nommée"],
         ["Il faut une preuve de résidence.","règle générale"],
         ["Je n'ai pas pu terminer ma demande en ligne.","impossibilité, au passé"],
         ["J'ai dû me déplacer au guichet.","obligation subie, au passé"],
         ["Il a fallu que je rappelle avec mon numéro.","règle + personne, au passé"],
       ]},

      {t:'piege', h:"Trois pièges",
       rows:[
         ["mettre le second verbe à autre chose qu'un infinitif","« je dois j'apporte »",
          "Après pouvoir, devoir et falloir, l'infinitif, toujours : je dois apporter."],
         ["conjuguer falloir","« nous fallons »",
          "Falloir n'existe qu'avec « il ». Pour nommer quelqu'un, on dit « il faut que nous… » avec le subjonctif."],
         ["confondre « je peux » et « je dois »","« Je peux passer demain » pour annoncer sa venue",
          "« Je peux » demande une permission ; « je dois » annonce une obligation. Au téléphone, la confusion fait dire au préposé le contraire de ce qu'on voulait."],
       ]},

      {t:'check', h:"Est-ce que c'est clair maintenant ?",
       p:"Trois questions rapides.",
       qs:[
         {q:"Le participe passé de pouvoir est…", opts:["pu","pû"], ok:0,
          fb:"« pu », sans accent."},
         {q:"Quelle forme énonce une règle sans désigner personne ?", opts:["vous devez","il faut"], ok:1,
          fb:"« Il faut » : le « il » ne remplace personne."},
         {q:"Après « il faut », le verbe est…", opts:["à l'infinitif","au présent"], ok:0,
          fb:"Il faut apporter, il faut sortir, il faut attendre."},
       ]},
    ]
  },

  // ════════════════════════════════════════════════════════════════════════
  t1notes: {
    eye:'Mini-leçon', tit:"Écrire pendant qu'on écoute",
    blocs:[
      {t:'texte', h:"Le vrai problème n'est pas la langue",
       p:"Prendre des notes au téléphone dans une langue qu'on apprend, c'est faire deux choses difficiles en même temps : comprendre, et écrire. Beaucoup d'élèves choisissent de tout comprendre et de ne rien noter — puis raccrochent et ne se souviennent d'aucun chiffre.",
       note:"La solution n'est pas d'écrire plus vite. C'est d'écrire <b>moins</b>, et de savoir d'avance quoi."},

      {t:'ana', h:"Cinq choses, jamais plus",
       p:"Préparez la feuille avant d'appeler, avec ces cinq lignes déjà écrites.",
       mots:[['1','le numéro de requête'],['2','le délai annoncé',true],['3','la date ou l\'heure']],
       say:"Je note : requête 24-118-7690, trois jours ouvrables.",
       note:"Et les deux dernières : le nom de la personne, et ce qu'il faut faire ensuite. Cinq lignes, cinq trous à remplir."},

      {t:'ana', h:"Le numéro d'abord, toujours",
       p:"C'est la seule chose qu'on ne peut pas reconstituer après coup.",
       mots:[['Un délai','s\'oublie et se redemande'],['Un numéro de requête','perdu, c\'est tout à recommencer',true],['Donc','on l\'écrit pendant qu\'il se dit']],
       say:"Vingt-quatre, cent dix-huit, sept mille six cent quatre-vingt-dix.",
       note:"Écrivez les chiffres au fur et à mesure, sans attendre la fin. Un numéro entendu en entier puis écrit de mémoire se perd une fois sur trois."},

      {t:'ana', h:"Répéter à voix haute en écrivant",
       p:"Le geste qui règle tout, et que personne n'ose faire.",
       mots:[['Ce que ça vérifie','vous avez le bon numéro'],['Ce que ça vous donne','le temps d\'écrire',true],['La formule','C\'est bien ça ?']],
       say:"Vingt-quatre, cent dix-huit, sept mille six cent quatre-vingt-dix. C'est bien ça ?",
       note:"Le silence pendant qu'on écrit met mal à l'aise et pousse à raccrocher trop vite. Répéter à voix haute remplit ce silence utilement."},

      {t:'ex', h:"Les phrases qui font ralentir sans gêner personne",
       p:"Six formules à avoir en tête avant de décrocher.",
       rows:[
         ["Un instant, je prends une feuille.","gagner cinq secondes"],
         ["Pouvez-vous répéter plus lentement, s'il vous plaît ?","la plus utile de toutes"],
         ["Je vous répète le numéro, et vous me dites si c'est bien ça.","vérifier et écrire"],
         ["Trois jours ouvrables. Donc pas avant vendredi, si je comprends bien ?","reformuler pour confirmer"],
         ["Excusez-moi, comment ça s'écrit ?","pour un nom ou une rue"],
         ["Et à qui est-ce que je parle, s'il vous plaît ?","le nom de la personne"],
       ]},

      {t:'piege', h:"Trois pièges",
       rows:[
         ["vouloir tout écrire","noter des phrases entières",
          "Vous perdez le fil de ce qui se dit. Notez des chiffres, des dates et des mots isolés — jamais des phrases."],
         ["ne pas oser faire répéter","« il va trouver que je comprends mal »",
          "Un préposé répète vingt fois par jour. Faire répéter est le signe qu'on prend la démarche au sérieux, pas qu'on parle mal."],
         ["ne pas dater la feuille","« trois jours ouvrables » sans point de départ",
          "La semaine suivante, une note sans date est inutilisable. Écrivez le jour en haut avant même de composer le numéro."],
       ]},

      {t:'check', h:"Est-ce que c'est clair maintenant ?",
       p:"Trois questions rapides.",
       qs:[
         {q:"Qu'est-ce qu'on note en premier ?", opts:["le numéro de requête","le nom du service"], ok:0,
          fb:"C'est la seule chose impossible à reconstituer."},
         {q:"Répéter le numéro à voix haute sert à…", opts:["vérifier et se donner le temps d'écrire","montrer qu'on a compris"], ok:0,
          fb:"Les deux à la fois, et c'est ce qui le rend si efficace."},
         {q:"On note…", opts:["des phrases complètes","des chiffres et des mots isolés"], ok:1,
          fb:"Écrire des phrases fait perdre le fil."},
       ]},
    ]
  },

  // ════════════════════════════════════════════════════════════════════════
  t2rel: {
    eye:'Mini-leçon', tit:"Qui, que, dont, où",
    blocs:[
      {t:'texte', h:"Ce que le niveau 5 attend vraiment",
       p:"Jusqu'ici, on pouvait dire les choses en phrases courtes : « C'est un lieu. On y apporte les vieux appareils. » Au niveau 5, on attend un discours <b>organisé</b> : « C'est un lieu <b>où</b> on apporte les vieux appareils. » Le pronom relatif est l'outil qui fait ça, et il n'y en a que quatre à tenir.",
       note:"C'est aussi ce qui permet de lire les pages officielles : elles sont écrites en phrases longues, tenues par des relatifs."},

      {t:'ana', h:"qui — il fait l'action",
       p:"Après « qui » vient tout de suite un verbe.",
       mots:[['Deux phrases','L\'encadré dit tout. Il est en haut à droite.'],['Une seule','L\'encadré qui est en haut à droite dit tout.',true],['Le repère','qui + verbe']],
       say:"C'est le préposé qui a ouvert ma requête.",
       note:"« qui » ne s'élide jamais : on écrit « qui a », jamais « qu'a »."},

      {t:'ana', h:"que — il subit l'action",
       p:"Après « que » vient un sujet, puis un verbe.",
       mots:[['Deux phrases','Le formulaire s\'est bloqué. Je l\'avais rempli.'],['Une seule','Le formulaire que j\'avais rempli s\'est bloqué.',true],['Le repère','que + sujet + verbe']],
       say:"Le formulaire que j'ai rempli s'est bloqué à la dernière page.",
       note:"« que » s'élide devant une voyelle : « la page qu'elle a lue »."},

      {t:'ana', h:"Le test de trois secondes",
       p:"Enlevez le pronom et regardez seulement ce qui suit.",
       mots:[['Un verbe tout seul','→ qui'],['Un sujet, puis un verbe','→ que',true],['Neuf cas sur dix','réglés sans grammaire']],
       say:"L'encadré qui est en haut. Le formulaire que j'ai rempli.",
       note:"Ce test vaut mieux que toutes les explications sur le sujet et le complément. Faites-le mentalement à chaque fois pendant deux semaines."},

      {t:'ana', h:"dont — il remplace « de quelque chose »",
       p:"Cherchez le « de » dans la phrase de départ.",
       mots:[['Deux phrases','J\'ai trouvé la page. Tu m\'as parlé de cette page.'],['Une seule','J\'ai trouvé la page dont tu m\'as parlé.',true],['Autres','avoir besoin de · s\'occuper de · être content de']],
       say:"La preuve de résidence dont j'ai besoin, c'est mon bail.",
       note:"Si la phrase de départ n'a pas de « de », ce n'est pas « dont ». C'est le seul test nécessaire."},

      {t:'ana', h:"où — le lieu, et aussi le moment",
       p:"La moitié de son usage est ignorée par la plupart des élèves.",
       mots:[['Le lieu','L\'écocentre où je suis allée.'],['Le moment','Le jour où le camion passe.',true],['Aussi','l\'année où je suis arrivée']],
       say:"Le mardi est le jour où le camion passe dans ma rue.",
       note:"« le jour que » s'entend beaucoup à l'oral, mais à l'écrit c'est « le jour où »."},

      {t:'labo', h:"Une phrase, un relatif",
       p:"Choisissez un cas et écoutez la phrase complète.",
       axes:[{id:'r', lbl:'Quel relatif ?', opts:[
         ['a','qui — sujet'],
         ['b','que — complément'],
         ['c','dont — avec « de »'],
         ['d','où — le lieu'],
         ['e','où — le moment'],
         ['f','que + accord du participe']]}],
       out:{
         a:{w:['qui + verbe'], say:"C'est le préposé qui a ouvert ma requête.", n:"un verbe suit directement"},
         b:{w:['que + sujet + verbe'], say:"Le formulaire que j'ai rempli s'est bloqué.", n:"un sujet s'intercale"},
         c:{w:['dont ← de'], say:"La preuve de résidence dont j'ai besoin, c'est mon bail.", n:"avoir besoin de"},
         d:{w:['où — lieu'], say:"L'écocentre où je suis allée ferme à dix-sept heures.", n:"un endroit"},
         e:{w:['où — moment'], say:"Le mardi est le jour où le camion passe.", n:"un moment, et non un lieu"},
         f:{w:['que → accord'], say:"Les pièces d'identité qu'elle a apportées étaient les bonnes.", n:"apportées, avec un e et un s"},
       },
       note:"Le dernier cas est celui qu'on oublie : avec « que », le participe passé s'accorde avec ce qui précède."},

      {t:'piege', h:"Trois pièges",
       rows:[
         ["mettre « que » là où il faut « qui »","« l'encadré que est en haut »",
          "Un verbe suit tout de suite : c'est « qui ». Et « qui » ne s'élide jamais."],
         ["oublier l'accord après « que »","« les pièces qu'elle a apporté »",
          "Avec « que », le participe s'accorde avec ce qui précède : apportées. Avec « qui », jamais d'accord de ce type."],
         ["employer « que » pour un moment","« le jour que le camion passe »",
          "À l'écrit, c'est « le jour où ». On l'entend souvent à l'oral, mais un courriel à un service se corrige."],
       ]},

      {t:'check', h:"Est-ce que c'est clair maintenant ?",
       p:"Quatre questions rapides.",
       qs:[
         {q:"« Le préposé ___ m'a répondu » : on met…", opts:["qui","que"], ok:0,
          fb:"Un verbe suit tout de suite."},
         {q:"« La page ___ tu m'as parlé » : on met…", opts:["que","dont"], ok:1,
          fb:"Parler DE quelque chose : c'est « dont »."},
         {q:"« Le jour ___ le camion passe » : à l'écrit, on met…", opts:["que","où"], ok:1,
          fb:"« où » sert aussi pour le moment."},
         {q:"« Les pièces qu'elle a ___ » : le participe…", opts:["s'accorde : apportées","ne s'accorde pas"], ok:0,
          fb:"Avec « que », il s'accorde avec ce qui précède."},
       ]},
    ]
  },

  // ════════════════════════════════════════════════════════════════════════
  t2rep: {
    eye:'Mini-leçon', tit:"La reprise de l'information",
    blocs:[
      {t:'texte', h:"Pourquoi un texte officiel devient difficile après trois lignes",
       p:"Un règlement ne va pas répéter vingt fois « la demande de carte de citoyenne ». Il écrit « celle-ci », « cette requête », « ce document ». Le texte devient court — et il devient difficile, parce qu'il faut se rappeler à tout moment de quoi on parle.",
       note:"Ce n'est pas de la lecture rapide : c'est de la lecture qui remonte. Un bon lecteur de textes officiels revient en arrière tout le temps."},

      {t:'ana', h:"Les quatre formes de reprise",
       p:"Elles font toutes la même chose : elles renvoient plus haut.",
       mots:[['Un pronom','elle, la, y, en'],['Un synonyme','la demande → la requête',true],['Un démonstratif','ce document, cette pièce']],
       say:"Apportez une preuve de résidence. Celle-ci doit dater de moins de trois mois.",
       note:"La quatrième est le mot général : « le bac, le bidon, la boîte » deviennent « ces contenants »."},

      {t:'ana', h:"La règle de lecture : remontez",
       p:"Ce qu'un mot reprend est presque toujours juste avant.",
       mots:[['Où chercher','la phrase précédente'],['Ou bien','le titre juste au-dessus',true],['Jamais','trois paragraphes plus haut']],
       say:"Votre demande a été enregistrée. Cette requête porte le numéro 24-118-7690.",
       note:"Si vous devez remonter plus loin qu'un paragraphe, c'est probablement le texte qui est mal écrit, pas vous qui lisez mal."},

      {t:'ana', h:"celui-ci, ce dernier : le plus proche",
       p:"Ils reprennent l'élément le plus proche, pas le plus important.",
       mots:[['La phrase','Joignez le formulaire et le reçu ;'],['La suite','ce dernier peut être une photo.',true],['Donc','c\'est le reçu, pas le formulaire']],
       say:"Joignez le formulaire et le reçu ; ce dernier peut être une photo.",
       note:"« Ce dernier » veut dire littéralement : le dernier nommé. Quand deux choses sont citées, c'est toujours la seconde."},

      {t:'ana', h:"y et en",
       p:"Deux petits mots qui portent beaucoup.",
       mots:[['y ← à, dans, un lieu','l\'écocentre → on y apporte…'],['en ← de','des visites → vous en avez quatre',true],['Le test','remplacez et relisez']],
       say:"Vous avez droit à quatre visites gratuites. Vous en avez déjà utilisé deux.",
       note:"Quand « y » ou « en » vous arrête, remplacez-le mentalement par le groupe complet et relisez la phrase. Elle redevient claire immédiatement."},

      {t:'piege', h:"Trois pièges",
       rows:[
         ["croire que « ce dernier » désigne le sujet principal","« le formulaire et le reçu ; ce dernier »",
          "Non : le dernier nommé, donc le reçu. C'est le contresens le plus coûteux dans une consigne officielle."],
         ["lire par-dessus les pronoms","passer sur « celle-ci » sans s'arrêter",
          "Vous croyez avoir compris et vous ratez la condition. Chaque pronom mérite une seconde d'arrêt."],
         ["confondre « celle-ci » et « celle-là »","dans une liste de deux",
          "« Celle-ci » est la plus proche, « celle-là » la plus éloignée. Dans un texte administratif, c'est presque toujours « celle-ci »."],
       ]},

      {t:'check', h:"Est-ce que c'est clair maintenant ?",
       p:"Trois questions rapides.",
       qs:[
         {q:"« Joignez le formulaire et le reçu ; ce dernier peut être une photo. » Il s'agit…", opts:["du formulaire","du reçu"], ok:1,
          fb:"« Ce dernier » = le dernier nommé."},
         {q:"« Vous en avez utilisé deux » : « en » reprend…", opts:["un lieu","une quantité de quelque chose"], ok:1,
          fb:"« en » reprend « de quelque chose »."},
         {q:"Quand un pronom vous arrête, il faut…", opts:["continuer et deviner","remonter à la phrase précédente"], ok:1,
          fb:"La reprise est presque toujours juste avant."},
       ]},
    ]
  },

  // ════════════════════════════════════════════════════════════════════════
  t2form: {
    eye:'Mini-leçon', tit:"Lire un formulaire complexe sans se faire bloquer",
    blocs:[
      {t:'texte', h:"Un formulaire n'est pas un texte : c'est une machine",
       p:"Il ne se lit pas, il se remplit — dans un ordre imposé, avec des mots qui ont un sens précis et un seul. Et quand il refuse d'avancer, il ne dit presque jamais pourquoi. Trois soirées perdues sur un formulaire viennent presque toujours d'un champ mal compris, pas d'une panne.",
       note:"Le remède : lire tous les champs <b>avant</b> d'en remplir un seul, et repérer ceux qui portent un astérisque."},

      {t:'ana', h:"Nom à la naissance",
       p:"Le champ qui arrête le plus de monde, pour rien.",
       mots:[['Ce qu\'il demande','le nom de votre acte de naissance'],['Même si','vous en portez un autre depuis',true],['Au Québec','le nom ne change pas au mariage']],
       say:"Inscrivez votre nom à la naissance, tel qu'il figure sur votre acte.",
       note:"Si vous avez changé de nom, il y a presque toujours un second champ « nom d'usage » plus bas. Cherchez-le avant d'improviser."},

      {t:'ana', h:"Champ obligatoire",
       p:"L'astérisque, et le silence du système.",
       mots:[['Le signe','*'],['Sans lui','le formulaire refuse d\'avancer',true],['Le problème','il ne dit pas toujours lequel']],
       say:"Les champs marqués d'un astérisque sont obligatoires.",
       note:"Quand une page se bloque : remontez et vérifiez chaque astérisque un par un. C'est fastidieux et c'est presque toujours ça."},

      {t:'ana', h:"L'adresse : un ordre et des abréviations",
       p:"C'est le champ qui a bloqué Leïla trois soirées de suite.",
       mots:[['L\'ordre','numéro, rue, app., ville, code postal'],['L\'abréviation','app. 3, et non « appartement 3 »',true],['Pourquoi','le système compare à sa propre base']],
       say:"7412, rue De Normanville, app. 3, Montréal, H2R 2V8.",
       note:"Un système qui vérifie votre adresse contre la sienne bute sur un mot écrit au long. Ce n'est pas votre faute, mais c'est à vous de contourner."},

      {t:'ana', h:"Pièce justificative et téléversement",
       p:"Envoyer un fichier de votre appareil vers le site.",
       mots:[['Le mot','téléverser'],['Ce qu\'on envoie','une pièce justificative',true],['À vérifier','le format et le poids maximum']],
       say:"Téléversez une pièce justificative de moins de cinq mégaoctets.",
       note:"Une photo prise avec un téléphone récent dépasse souvent la limite. Réduisez-la avant, plutôt que de recommencer le formulaire."},

      {t:'ana', h:"Le cas échéant",
       p:"Trois mots qui autorisent à laisser vide.",
       mots:[['Ce que ça veut dire','si cela s\'applique à vous'],['Donc','on peut laisser le champ vide',true],['Exemple','numéro de dossier antérieur, le cas échéant']],
       say:"Numéro de dossier antérieur, le cas échéant.",
       note:"Beaucoup d'élèves inventent une réponse par peur du vide. Un champ « le cas échéant » qui ne vous concerne pas se laisse vide, sans conséquence."},

      {t:'ex', h:"Sept mots de formulaire à reconnaître",
       p:"Ils reviennent dans tous les formulaires du Québec.",
       rows:[
         ["Nom à la naissance","celui de l'acte de naissance"],
         ["Champ obligatoire *","sans lui, rien n'avance"],
         ["Pièce justificative","le document qui prouve"],
         ["Téléverser","envoyer un fichier vers le site"],
         ["Le cas échéant","si cela s'applique"],
         ["Attestation","la case qui vous engage"],
         ["Numéro de confirmation","votre preuve d'envoi"],
       ]},

      {t:'piege', h:"Trois pièges",
       rows:[
         ["cocher l'attestation sans relire","« je déclare que tout est exact »",
          "C'est la seule ligne du formulaire qui vous engage légalement. Relisez avant de cocher, pas après."],
         ["envoyer sans garder de trace","fermer l'onglet tout de suite",
          "Photographiez l'écran de confirmation ou notez le numéro. Un envoi sans trace est un envoi à refaire."],
         ["écrire l'adresse au long","« appartement 3 »",
          "Le système attend « app. 3 ». Un détail de trois lettres qui coûte une soirée."],
       ]},

      {t:'check', h:"Est-ce que c'est clair maintenant ?",
       p:"Trois questions rapides.",
       qs:[
         {q:"Un champ suivi de « le cas échéant »…", opts:["doit être rempli","peut rester vide s'il ne vous concerne pas"], ok:1,
          fb:"« Si cela s'applique à votre situation »."},
         {q:"« Téléverser » veut dire…", opts:["envoyer un fichier vers le site","télécharger un fichier du site"], ok:0,
          fb:"De votre appareil vers le site."},
         {q:"Quand la page se bloque sans message, on vérifie…", opts:["sa connexion","les champs obligatoires"], ok:1,
          fb:"Presque toujours un astérisque vide ou mal écrit."},
       ]},
    ]
  },

  // ════════════════════════════════════════════════════════════════════════
  t2prep: {
    eye:'Mini-leçon', tit:"Les prépositions des démarches",
    blocs:[
      {t:'texte', h:"Elles ne se devinent pas, et c'est normal",
       p:"Aucune logique ne dit pourquoi on se renseigne <b>sur</b> un tarif mais qu'on s'adresse <b>à</b> un service. Chaque verbe impose la sienne, et il faut les apprendre <b>avec le verbe</b>, jamais séparément. Un élève qui apprend « s'adresser » sans son « à » l'apprendra deux fois.",
       note:"Notez-les toujours en groupe : s'adresser à · se renseigner sur · avoir besoin de · avoir droit à."},

      {t:'ana', h:"Les six du vocabulaire administratif",
       p:"Elles couvrent presque toutes les phrases de ce module.",
       mots:[['s\'adresser à','s\'adresser au service des collectes'],['se renseigner sur','se renseigner sur les tarifs',true],['avoir droit à','avoir droit à quatre visites']],
       say:"Pour ce genre de problème, il faut s'adresser au service des collectes.",
       note:"Et les trois autres : joindre à sa demande, répondre dans un délai, faire une demande par téléphone."},

      {t:'ana', h:"par — le moyen",
       p:"Comment la démarche voyage. Presque toujours sans article.",
       mots:[['Les canaux','par téléphone · par courriel'],['Aussi','par la poste · par Internet',true],['Jamais','par le téléphone']],
       say:"Vous pouvez faire votre demande par téléphone ou en ligne.",
       note:"Exception : « par la poste » garde son article. C'est la seule des quatre, et il faut la retenir telle quelle."},

      {t:'ana', h:"dans — le délai à venir",
       p:"À ne pas confondre avec « en ».",
       mots:[['dans trois jours','à partir de maintenant'],['en trois jours','la durée du travail',true],['Le service dit','dans un délai de trois jours ouvrables']],
       say:"Vous recevrez une réponse dans un délai de trois jours ouvrables.",
       note:"« Le formulaire se remplit en dix minutes » — c'est la durée. « Vous aurez une réponse dans dix jours » — c'est le moment."},

      {t:'ana', h:"avant de + infinitif",
       p:"La formule des encadrés « avant de vous déplacer ».",
       mots:[['La forme','avant de + infinitif'],['La condition','la même personne des deux côtés',true],['Sinon','avant que + subjonctif']],
       say:"Vérifiez le temps d'attente avant de vous déplacer.",
       note:"« Avant de partir, j'ai appelé » : c'est moi qui pars et moi qui appelle. Sinon : « avant qu'il ferme, j'ai appelé »."},

      {t:'piege', h:"Trois pièges",
       rows:[
         ["demander POUR quelque chose","« Je demande pour un renseignement »",
          "L'erreur la plus fréquente de tout ce module. On demande quelque chose à quelqu'un : « Je demande un renseignement au préposé. »"],
         ["mettre un article après « par »","« par le courriel »",
          "Par téléphone, par courriel, par Internet — sans article. Seul « par la poste » fait exception."],
         ["confondre « dans » et « en »","« Je l'ai fait dans dix minutes »",
          "Pour une durée, c'est « en dix minutes ». « Dans dix minutes » veut dire : à partir de maintenant."],
       ]},

      {t:'check', h:"Est-ce que c'est clair maintenant ?",
       p:"Trois questions rapides.",
       qs:[
         {q:"On se renseigne ___ les tarifs.", opts:["sur","de"], ok:0,
          fb:"Se renseigner SUR quelque chose."},
         {q:"« Vous aurez une réponse ___ trois jours » (à partir de maintenant)", opts:["en","dans"], ok:1,
          fb:"« dans » pour le moment à venir, « en » pour la durée."},
         {q:"Laquelle est correcte ?", opts:["Je demande pour un renseignement.","Je demande un renseignement au préposé."], ok:1,
          fb:"Demander quelque chose à quelqu'un, sans « pour »."},
       ]},
    ]
  },

  // ════════════════════════════════════════════════════════════════════════
  t3imp: {
    eye:'Mini-leçon', tit:"Il faut que, il manque, il reste : le « il » qui ne désigne personne",
    blocs:[
      {t:'texte', h:"La forme préférée de l'administration",
       p:"Dans « il faut deux pièces », le mot « il » ne remplace personne : ni le préposé, ni vous, ni le formulaire. C'est un sujet vide, qui sert seulement à faire tenir la phrase. Et c'est pour ça que l'administration l'emploie partout : elle énonce une règle <b>sans désigner un coupable</b>.",
       note:"Comparez : « Vous avez oublié votre signature » et « Il manque votre signature ». Même information, deux conversations complètement différentes."},

      {t:'ana', h:"il faut + nom, ou + infinitif",
       p:"Les deux formes les plus simples, et elles suffisent souvent.",
       mots:[['+ nom','Il faut une preuve de résidence.'],['+ infinitif','Il faut apporter deux pièces.',true],['Au passé','Il fallait une facture récente.']],
       say:"Il faut une preuve de résidence pour entrer à l'écocentre.",
       note:"Tant que vous ne nommez personne, restez sur ces deux formes : aucun subjonctif à faire."},

      {t:'ana', h:"il faut que + subjonctif",
       p:"Dès qu'on nomme la personne concernée.",
       mots:[['On nomme','il faut QUE vous…'],['Le verbe change','…que vous apportiez',true],['Autres','que je revienne · qu\'elle soit']],
       say:"Il faut que vous apportiez deux pièces d'identité.",
       note:"C'est le seul endroit du module où le subjonctif est obligatoire. Mais il y est vraiment obligatoire."},

      {t:'ana', h:"Les quatre subjonctifs à savoir par cœur",
       p:"Ils reviennent dans toutes les démarches.",
       mots:[['être','que je sois · que vous soyez'],['avoir','que j\'aie · que vous ayez',true],['faire, pouvoir','que je fasse · que je puisse']],
       say:"Il faut que j'aie mon numéro de requête et que je sois là avant seize heures.",
       note:"Les verbes réguliers, eux, se forment sur le « ils » du présent : ils apport-ent → que vous apport-iez. Aucun effort de mémoire."},

      {t:'ana', h:"il manque, il reste",
       p:"Et le verbe reste au singulier, même au pluriel.",
       mots:[['Ce qui n\'est pas là','Il manque une signature.'],['Au pluriel quand même','Il manque deux documents.',true],['Le temps','Il reste dix minutes.']],
       say:"Il manque deux documents à votre dossier, et il reste dix minutes.",
       note:"« Il manquent » n'existe pas. Le sujet est « il », toujours singulier — ce qui manque est le complément."},

      {t:'labo', h:"Nommer ou ne pas nommer",
       p:"Choisissez une situation et écoutez les deux façons de la dire.",
       axes:[{id:'i', lbl:'Quelle situation ?', opts:[
         ['a','une règle générale'],
         ['b','une obligation pour vous'],
         ['c','une obligation pour moi'],
         ['d','une pièce manquante'],
         ['e','du temps qui reste']]}],
       out:{
         a:{w:['il faut + nom'], say:"Il faut deux pièces d'identité.", n:"personne n'est nommé"},
         b:{w:['il faut que + subjonctif'], say:"Il faut que vous apportiez deux pièces d'identité.", n:"vous êtes nommé : subjonctif"},
         c:{w:['il faut que je…'], say:"Il faut que je revienne avec une facture récente.", n:"revenir → que je revienne"},
         d:{w:['il manque'], say:"Il manque une signature au bas de votre formulaire.", n:"un manque, pas une faute"},
         e:{w:['il reste'], say:"Il reste dix minutes avant la fermeture du comptoir.", n:"singulier, toujours"},
       },
       note:"Passez de a à b et écoutez la différence : c'est exactement le moment où le subjonctif apparaît."},

      {t:'piege', h:"Trois pièges",
       rows:[
         ["mettre l'indicatif après « il faut que »","« il faut que vous apportez »",
          "Après « il faut que », le subjonctif est obligatoire : que vous apportiez."],
         ["accorder « il manque »","« il manquent deux documents »",
          "Le sujet est « il », invariable. Ce qui manque vient après le verbe."],
         ["conjuguer falloir à d'autres personnes","« nous fallons revenir »",
          "Falloir n'existe qu'avec « il ». Pour nous : « il faut que nous revenions »."],
       ]},

      {t:'check', h:"Est-ce que c'est clair maintenant ?",
       p:"Quatre questions rapides.",
       qs:[
         {q:"« Il faut que vous ___ deux pièces. » (apporter)", opts:["apportez","apportiez"], ok:1,
          fb:"Subjonctif après « il faut que »."},
         {q:"« Il ___ deux documents à votre dossier. »", opts:["manque","manquent"], ok:0,
          fb:"Le sujet est « il », toujours singulier."},
         {q:"« Il faut que la facture ___ récente. » (être)", opts:["est","soit"], ok:1,
          fb:"que je sois, que tu sois, qu'elle soit."},
         {q:"Pourquoi l'administration préfère cette forme ?", opts:["elle est plus courte","elle énonce sans désigner de coupable"], ok:1,
          fb:"« Il manque votre signature » plutôt que « vous avez oublié »."},
       ]},
    ]
  },

  // ════════════════════════════════════════════════════════════════════════
  t3passe: {
    eye:'Mini-leçon', tit:"Raconter une démarche : passé composé et imparfait",
    blocs:[
      {t:'texte', h:"Une démarche a besoin des deux",
       p:"Au guichet, on doit raconter ce qui s'est déjà passé. Les <b>étapes</b> se disent au passé composé — j'ai appelé, j'ai rempli, je me suis déplacée. Le <b>décor</b> se dit à l'imparfait — la page se bloquait, j'attendais, il y avait douze personnes. Un récit qui n'emploie qu'un seul des deux temps sonne faux, même quand chaque phrase est correcte.",
       note:"C'est ce que le programme appelle un discours simple mais organisé : plusieurs phrases qui tiennent ensemble, pas une suite d'énoncés."},

      {t:'ana', h:"Passé composé — ce qui est arrivé, une fois",
       p:"Un fait, à un moment, terminé.",
       mots:[['Les étapes','J\'ai appelé. J\'ai rempli le formulaire.'],['Le déplacement','Je me suis déplacée au guichet.',true],['Repère','on peut mettre une date dessus']],
       say:"J'ai appelé la Ville, puis je me suis déplacée au guichet.",
       note:"Test simple : si vous pouvez ajouter « mardi dernier » sans que ce soit bizarre, c'est le passé composé."},

      {t:'ana', h:"Imparfait — ce qui durait, ce qui se répétait",
       p:"La situation autour, sans début ni fin marqués.",
       mots:[['L\'habitude','Je sortais le bac le mardi vers midi.'],['La durée','J\'attendais depuis vingt minutes.',true],['Le décor','Il y avait douze personnes.']],
       say:"Avant, je sortais le bac le mardi vers midi.",
       note:"L'habitude passée est toujours à l'imparfait — et dans ce module, c'est elle qui explique le problème."},

      {t:'ana', h:"Le verbe qui coupe",
       p:"Le schéma le plus fréquent de tout récit de démarche.",
       mots:[['Ce qui durait','J\'attendais depuis vingt minutes'],['Ce qui l\'interrompt','quand un préposé a répondu.',true],['Donc','imparfait + passé composé']],
       say:"J'attendais depuis vingt minutes quand un préposé a répondu.",
       note:"« Quand » est le mot qui annonce la coupure. Repérez-le, et les deux temps se placent tout seuls."},

      {t:'ana', h:"Être ou avoir, et l'accord",
       p:"La liste courte qui suffit ici.",
       mots:[['Avec être','aller, venir, partir, arriver, rester, revenir'],['Et','tous les verbes pronominaux',true],['L\'accord','elle s\'est présentée · elles sont revenues']],
       say:"Elle s'est présentée au guichet avec ses deux pièces d'identité.",
       note:"Avec « être », le participe s'accorde avec le sujet. Avec « avoir », il ne s'accorde pas — sauf si un « que » précède."},

      {t:'ex', h:"Un récit complet, à écouter",
       p:"Six phrases qui font une seule histoire.",
       rows:[
         ["Avant, je sortais le bac le mardi vers midi.","habitude — imparfait"],
         ["La semaine dernière, j'ai appelé la Ville.","étape — passé composé"],
         ["J'attendais depuis vingt minutes quand un préposé a répondu.","durée coupée"],
         ["Il m'a expliqué que le camion passait le matin.","étape + décor"],
         ["J'ai essayé de faire la demande en ligne, mais la page se bloquait.","étape + décor"],
         ["Alors je me suis déplacée au guichet, et tout a été réglé en dix minutes.","étapes, avec être puis avoir"],
       ]},

      {t:'piege', h:"Trois pièges",
       rows:[
         ["tout mettre au passé composé","« j'ai attendu, il a répondu, la page s'est bloquée »",
          "Chaque phrase est correcte, et le récit sonne comme une liste. Le décor a besoin de l'imparfait."],
         ["oublier l'accord avec être","« elle s'est présenté »",
          "Avec être et les pronominaux, le participe s'accorde avec le sujet : présentée."],
         ["employer le passé composé pour une habitude","« la semaine passée, j'ai sorti le bac tous les mardis »",
          "Une habitude, même finie, va à l'imparfait : « je sortais le bac tous les mardis »."],
       ]},

      {t:'check', h:"Est-ce que c'est clair maintenant ?",
       p:"Quatre questions rapides.",
       qs:[
         {q:"« Avant, je ___ le bac le mardi. » (sortir)", opts:["ai sorti","sortais"], ok:1,
          fb:"Une habitude passée : imparfait."},
         {q:"« J'___ depuis vingt minutes quand il a répondu. » (attendre)", opts:["attendais","ai attendu"], ok:0,
          fb:"Ce qui durait est à l'imparfait."},
         {q:"« Elle s'est ___ au guichet. » (présenter)", opts:["présenté","présentée"], ok:1,
          fb:"Pronominal : accord avec le sujet."},
         {q:"Dans un récit de démarche, les étapes vont…", opts:["au passé composé","à l'imparfait"], ok:0,
          fb:"Les étapes au passé composé, le décor à l'imparfait."},
       ]},
    ]
  },

};
