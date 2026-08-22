const PLUS = {

  prGraphie: {
    eye:'Mini-leçon', tit:"Quand les lettres mentent : ch, x, sh",
    blocs:[
      {t:'texte', h:"Trois cas où l'écriture trompe l'oreille",
       p:"Le français écrit une chose et en dit souvent une autre. Ce n'est pas grave dans la vie de tous les jours : on finit par savoir. Ça devient gênant le jour où l'on entend un mot pour la première fois et qu'on veut le retrouver dans un dictionnaire. On le cherche avec la lettre entendue, et il n'y est pas.",
       note:"Le programme du niveau 6 nomme exactement ces trois cas : « ch » qui se dit comme un k, « x » qui se dit comme un s, et « sh » ou « sch » qui se disent comme un ch."},

      {t:'ana', h:"Cas 1 — « ch » qui se dit comme un K",
       p:"Presque toujours dans des mots venus du grec. Ce sont des mots savants, et il y en a beaucoup plus qu'on ne pense.",
       mots:[['On écrit','une {ch}orale · la te{ch}nique · un é{ch}o · la psy{ch}ologie'],
             ['On entend','[k], comme dans « kilo »', true],
             ['Le repère','un mot savant, souvent avec « y » ou « ph » à côté']],
       say:"une chorale, la technique, un écho, la psychologie",
       note:"Attention : « chercher », « chaque », « chose », « chignon » gardent le son normal. Le K est l'exception, pas la règle."},

      {t:'ana', h:"Cas 2 — « x » qui se dit comme un S",
       p:"Dans quelques nombres et quelques noms de lieux, tous très fréquents.",
       mots:[['On écrit','di{x} · si{x} · soi{x}ante · Bru{x}elles'],
             ['On entend','[s], comme dans « dis »', true],
             ['Le piège du nombre','« dix » se dit [dis] tout seul, [di] devant une consonne, [diz] devant une voyelle']],
       say:"dix, six, soixante, Bruxelles",
       note:"Dix dollars se dit « di dollars ». Dix ans se dit « diz ans ». Dix, tout seul, se dit « dis »."},

      {t:'ana', h:"Cas 3 — « sh » et « sch » qui se disent comme un CH",
       p:"Des mots empruntés à l'anglais ou à l'allemand, et devenus courants au Québec.",
       mots:[['On écrit','un {sh}ort · du {sh}ampoing · un {sch}éma'],
             ['On entend','[ʃ], le son de « chat »', true],
             ['Le repère','un mot venu d\'ailleurs, souvent court']],
       say:"un short, du shampoing, un schéma",
       note:"Ces mots-là sont ceux qu'on prononce le plus souvent à l'anglaise sans s'en rendre compte. En français, « short » commence comme « chat »."},

      {t:'labo', h:"Écoute, puis répète",
       p:"Choisis un cas et un exemple.",
       axes:[
         {id:'c', lbl:'Quelles lettres ?', opts:[['a','ch qui dit K'],['b','x qui dit S'],['c','sh, sch qui disent CH']]},
         {id:'n', lbl:'Quel exemple ?', opts:[['1','le premier'],['2','le second']]}],
       out:{
         a1:{w:["une chorale"], say:"une chorale", n:'mot grec : « co-rale »'},
         a2:{w:["la technique"], say:"la technique", n:'« tec-nique », jamais « te-chnique »'},
         b1:{w:["dix"], say:"dix", n:'tout seul, on entend le S final'},
         b2:{w:["soixante"], say:"soixante", n:'« soi-sante », jamais « soi-ksante »'},
         c1:{w:["un schéma"], say:"un schéma", n:'trois lettres pour le son de « chat »'},
         c2:{w:["un short"], say:"un short", n:'à la française : « chort »'},
       },
       note:"Écoute deux fois avant de répéter. C'est l'oreille qu'on entraîne, pas la mémoire."},

      {t:'ex', h:"Huit mots, écrits et dits",
       p:"À gauche ce qui est écrit, à droite ce qui se dit.",
       rows:[
         ["une chorale","« co-rale » — le ch fait k"],
         ["la technique","« tec-nique » — le ch fait k"],
         ["un écho","« é-co » — le ch fait k"],
         ["la psychologie","« psi-co-lo-gie » — le ch fait k"],
         ["dix jours","« di jours » — le x se tait devant une consonne"],
         ["soixante","« soi-sante » — le x fait s"],
         ["un schéma","« ché-ma » — sch fait ch"],
         ["du shampoing","« cham-poin » — sh fait ch"],
       ]},

      {t:'piege', h:"Deux pièges, une consolation",
       rows:[
         ["chercher le mot avec la lettre entendue","chercher avec la lettre écrite",
          "Tu entends « corale » et tu cherches « corale » : rien. Quand un mot entendu reste introuvable, essaie « ch » à la place du k, et « x » à la place du s."],
         ["prononcer tous les « ch » comme dans « chat »","reconnaître les mots savants",
          "« Technique » dit avec le son de « chat » ne se comprend pas du tout. Ces mots-là ne sont pas nombreux : ils s'apprennent un par un."],
         ["s'inquiéter pour « dix »","les trois formes se comprennent",
          "Personne ne te reprendra si tu dis « diz jours ». Ce qui compte, c'est de reconnaître les trois formes à l'écoute."],
       ]},

      {t:'check', h:"Est-ce que c'est clair maintenant ?",
       p:"Quatre questions rapides.",
       qs:[
         {q:"Dans « chorale », les lettres « ch » se disent…", opts:["comme dans chat","comme un k"], ok:1,
          fb:"C'est un mot venu du grec : « co-rale »."},
         {q:"Dans « soixante », la lettre « x » se dit…", opts:["comme un s","comme un ks"], ok:0,
          fb:"« Soi-sante ». Même chose dans « dix » et « six »."},
         {q:"Dans « un schéma », les lettres « sch » se disent…", opts:["comme un sk","comme dans chat"], ok:1,
          fb:"Trois lettres pour un seul son, celui de « chat »."},
         {q:"« Dix dollars » se prononce…", opts:["« di dollars »","« disse dollars »"], ok:0,
          fb:"Devant une consonne, le x de « dix » ne s'entend pas."},
       ]},

      {t:'revoir', h:"À retenir",
       p:"Trois cas seulement : <b>ch</b> qui dit k dans les mots savants (chorale, technique, écho), <b>x</b> qui dit s dans les nombres et quelques noms de lieux (dix, six, soixante), <b>sh</b> et <b>sch</b> qui disent ch dans les mots empruntés (short, shampoing, schéma)."},
    ]
  },

  prCourriel: {
    eye:'Mini-leçon', tit:"Lire la forme d'un courriel avant d'en lire le texte",
    blocs:[
      {t:'texte', h:"Un long courriel se regarde avant de se lire",
       p:"Devant quatre paragraphes, la première chose à faire n'est pas de lire le premier mot. C'est de regarder la page : combien de blancs, combien de paragraphes, quel objet, quelle formule d'appel. En dix secondes, on sait déjà combien de nouvelles arrivent et sur quel ton.",
       note:"Le programme du niveau 6 appelle ça « tenir compte de la présentation matérielle et de la mise en page ». C'est un savoir de lecture, pas d'écriture."},

      {t:'ana', h:"L'objet : trois à six mots, lus en premier",
       p:"Celui qui écrit le met en dernier ; celui qui reçoit le lit avant tout le reste. Il annonce le sujet et souvent le ton.",
       mots:[['Un objet qui informe','Des nouvelles, enfin'],
             ['Un objet qui inquiète','Important — à lire aujourd\'hui', true],
             ['Un objet vide','Bonjour · Question · Suite'],
             ['La règle','un objet doit pouvoir se lire seul, six mois plus tard, dans une liste de cent courriels']],
       say:"Objet : Des nouvelles, enfin",
       note:"Un courriel sans objet arrive comme quelqu'un qui entre sans frapper : on l'ouvre, mais on ne sait pas encore de quoi il s'agit."},

      {t:'ana', h:"La formule d'appel : à qui, et de quelle façon",
       p:"Deux mots, et tout le ton du courriel est donné.",
       mots:[['Amical','Chère Marisol, · Salut Ousmane,'],
             ['Poli mais distant','Madame, · Monsieur Bourbeau,', true],
             ['Formel','Madame la Coordonnatrice,'],
             ['Ce qu\'elle décide','le tutoiement ou le vouvoiement de tout le reste du texte']],
       say:"Chère Marisol,",
       note:"Une formule d'appel amicale suivie d'un vouvoiement sonne faux. On choisit une fois, et on s'y tient jusqu'à la signature."},

      {t:'ana', h:"Les paragraphes : un blanc, une idée",
       p:"Le blanc entre deux paragraphes n'est pas de la décoration. Il annonce un changement d'idée, et il permet de compter les nouvelles sans les lire.",
       mots:[['Compter les blancs','quatre paragraphes, quatre idées principales'],
             ['Lire les premières phrases','elles donnent le plan du courriel', true],
             ['Ce qui va toujours à part','la mauvaise nouvelle, et l\'opinion'],
             ['Ce qu\'il ne faut pas faire','tout écrire d\'un bloc : le lecteur ne sait plus où une nouvelle finit']],
       say:"Il y a une nouvelle triste, et je la garde pour la fin.",
       note:"Ousmane place le décès de son oncle dans le dernier paragraphe, seul. C'est un choix, et ce choix se lit."},

      {t:'ex', h:"Les six parties, et ce que chacune apprend",
       p:"Aucune n'est là pour faire joli.",
       rows:[
         ["l'objet","de quoi il sera question, et sur quel ton"],
         ["la formule d'appel","à qui on écrit, et si on le tutoie"],
         ["le premier paragraphe","la nouvelle principale, celle qui ne peut pas attendre"],
         ["les blancs","combien d'idées différentes arrivent"],
         ["la première phrase de chaque paragraphe","l'idée principale de ce paragraphe"],
         ["la salutation et la signature","que c'est fini, et quel lien unit les deux personnes"],
       ]},

      {t:'piege', h:"Trois façons de mal lire un long courriel",
       rows:[
         ["lire du premier au dernier mot, une seule fois","regarder d'abord, lire ensuite",
          "Une lecture linéaire d'un texte long fait perdre le fil au troisième paragraphe. Regarde la forme, lis les premières phrases, puis reviens."],
         ["répondre à chaque phrase","répondre à chaque paragraphe",
          "Un courriel de quatre paragraphes appelle quatre réactions, pas quarante. Une par idée principale suffit."],
         ["ignorer l'objet","le lire comme un titre",
          "L'objet est écrit après le texte, par quelqu'un qui sait de quoi il a parlé. C'est le meilleur résumé que tu auras."],
       ]},

      {t:'revoir', h:"À retenir",
       p:"Avant de lire : l'<b>objet</b> annonce le sujet, la <b>formule d'appel</b> annonce le ton, les <b>blancs</b> comptent les idées, et la <b>première phrase</b> de chaque paragraphe donne le plan. Dix secondes de regard épargnent deux relectures."},
    ]
  },

  prEvts: {
    eye:'Mini-leçon', tit:"Répondre à une nouvelle sans se tromper de ton",
    blocs:[
      {t:'texte', h:"Le mot juste existe, et il est court",
       p:"Dans toutes les langues, les grandes nouvelles de la vie appellent des réponses toutes faites. Ce ne sont pas des formules vides : ce sont des phrases que tout le monde reconnaît, et qui permettent de dire quelque chose au moment où l'on ne sait pas quoi dire.",
       note:"Le savoir du programme parle des « mots en rapport avec les évènements racontés : naissance, mariage, enterrement, accident, voyage »."},

      {t:'ana', h:"Les bonnes nouvelles",
       p:"On félicite, et on nomme la personne concernée. Une félicitation qui ne nomme personne ne fait pas plaisir.",
       mots:[['Une naissance','Félicitations à vous deux ! Comment va la maman ?'],
             ['Un mariage','Quelle belle nouvelle ! Vous descendez pour l\'occasion ?', true],
             ['Un nouvel emploi','Bravo, tu le mérites. Ça commence quand ?'],
             ['Ce qu\'on évite','« Enfin ! » — qui laisse entendre que ça a trop tardé']],
       say:"Félicitations à vous deux ! Comment va la maman ?",
       note:"Au Québec, « félicitations » s'emploie pour une réussite et pour un heureux évènement. On ne dit pas « bonne chance » à quelqu'un qui vient d'accoucher."},

      {t:'ana', h:"Les mauvaises nouvelles",
       p:"On offre ses condoléances, et on ne demande jamais de détails. La règle est simple : parler de la personne, jamais de l'évènement.",
       mots:[['Un décès','Toutes mes condoléances. Je pense à toi et à ta famille.'],
             ['Un accident','Bon rétablissement à lui. Est-ce qu\'il remarche ?', true],
             ['Une maladie','J\'espère que ça va aller. Dis-moi si je peux faire quelque chose.'],
             ['Ce qu\'on ne demande pas','comment c\'est arrivé, ce qu\'il a fait, qui est responsable']],
       say:"Toutes mes condoléances. Je pense à toi et à ta famille.",
       note:"« Condoléances » est toujours au pluriel, et toujours accompagné : mes condoléances, toutes mes condoléances, mes sincères condoléances."},

      {t:'ana', h:"Les nouvelles qui ne sont ni bonnes ni mauvaises",
       p:"Un déménagement, un retour aux études, l'arrivée d'un proche. La bonne réponse est une question sur ce qui vient après.",
       mots:[['Un déménagement','Et le nouveau quartier, vous vous y plaisez ?'],
             ['L\'arrivée d\'un proche','Ça doit vous faire du bien de l\'avoir avec vous.', true],
             ['Un retour aux études','Ça te reprend combien de soirs par semaine ?'],
             ['Le principe','on demande le présent, pas le passé']],
       say:"Et le nouveau quartier, vous vous y plaisez ?",
       note:"Ces nouvelles-là sont les plus fréquentes et les plus mal traitées : on les laisse souvent sans réponse, faute de savoir quoi en dire."},

      {t:'piege', h:"Trois réponses qui referment une conversation",
       rows:[
         ["Nous aussi, on a déménagé l'an passé.","Et le nouveau quartier, vous vous y plaisez ?",
          "Comparer avec soi-même déplace la conversation vers soi. Ce n'est pas malpoli, mais l'autre cesse de raconter."],
         ["Il est mort de quoi ?","Toutes mes condoléances.",
          "La cause d'un décès ne se demande pas. Si la personne veut la dire, elle la dira."],
         ["Ça va aller, ce n'est pas grave.","J'espère que ça va aller. Dis-moi si je peux aider.",
          "Décider à la place de l'autre que ce n'est pas grave lui enlève le droit de trouver ça grave."],
       ]},

      {t:'check', h:"Quatre nouvelles, quatre réponses",
       p:"Choisis la réponse juste.",
       qs:[
         {q:"« Mon oncle est décédé en février. »", opts:["Toutes mes condoléances.","Bon rétablissement !"], ok:0,
          fb:"Le rétablissement, c'est pour quelqu'un de blessé ou de malade."},
         {q:"« Mon beau-frère s'est cassé la cheville. »", opts:["Félicitations !","Bon rétablissement à lui."], ok:1,
          fb:"On souhaite le rétablissement, et on demande des nouvelles de la personne."},
         {q:"« Notre fille est née le 14 mars. »", opts:["Félicitations à vous deux !","Mes condoléances."], ok:0,
          fb:"On félicite, et on nomme les parents ou l'enfant."},
         {q:"« Nous avons déménagé en juin. »", opts:["Nous aussi.","Vous vous y plaisez ?"], ok:1,
          fb:"Une question sur le présent ouvre la conversation ; une comparaison la referme."},
       ]},

      {t:'revoir', h:"À retenir",
       p:"Bonne nouvelle : on <b>félicite</b> et on nomme quelqu'un. Décès : <b>toutes mes condoléances</b>, et aucune question. Accident ou maladie : <b>bon rétablissement</b>, et on demande des nouvelles de la personne. Le reste : une question sur ce qui vient après."},
    ]
  },

  t1texte: {
    eye:'Mini-leçon', tit:"Suivre le fil d'un texte long",
    blocs:[
      {t:'texte', h:"Ce qui est difficile n'est pas le vocabulaire",
       p:"Le courriel d'Ousmane ne contient presque aucun mot rare. Et pourtant Marisol l'a lu deux fois sans être sûre d'avoir compris. C'est que la difficulté d'un texte long n'est pas dans les mots : elle est dans ce qui les relie. Qui est « il » ? Qu'est-ce que « la » remplace ? Qu'est-ce qui est arrivé avant quoi ?",
       note:"C'est ce qui sépare le niveau 6 des niveaux précédents. Au niveau 5, on raconte ; ici, on suit."},

      {t:'ana', h:"Les quatre fils d'un texte suivi",
       p:"Quatre choses relient les phrases entre elles. Les quatre se lisent, et les quatre se perdent.",
       mots:[['Les reprises','le, la, en, y, celui-là — ils renvoient en arrière'],
             ['Les temps','le plus-que-parfait recule d\'un cran, l\'imparfait plante le décor', true],
             ['Les connecteurs','pourtant, donc, d\'ailleurs — ils annoncent la suite'],
             ['La mise en page','un blanc, un paragraphe, un tiret : ils découpent']],
       say:"Quand je t'ai écrit, on l'avait déjà vendue.",
       note:"Un texte de niveau 6 se lit deux fois : une fois pour les faits, une fois pour les liens. La deuxième lecture est la vraie."},

      {t:'ana', h:"Le geste à prendre : reculer d'une phrase",
       p:"Chaque fois qu'un petit mot apparaît sans nom, on remonte. C'est un geste, pas une règle de grammaire.",
       mots:[['On lit','on l\'avait déjà vendue'],
             ['On recule','la phrase d\'avant parle de la rue Perreault', true],
             ['On conclut','« l\' » = la maison de la rue Perreault'],
             ['On avance','et on ne se pose plus la question pour le reste du paragraphe']],
       say:"On l'avait déjà vendue quand je t'ai écrit.",
       note:"Ce geste prend deux secondes et fait gagner une relecture complète."},

      {t:'ex', h:"Cinq passages du courriel, et ce qu'il faut y voir",
       p:"À gauche ce qui est écrit, à droite le lien qu'il faut faire.",
       rows:[
         ["on l'avait déjà vendue","« l' » = la maison ; le plus-que-parfait la vend avant le courriel"],
         ["elle s'installait à peine quand il est tombé","les deux se touchent : octobre et novembre"],
         ["il est retourné travailler en avril","« retourner » dit qu'il y travaillait déjà avant"],
         ["je la garde pour la fin","« la » = la nouvelle triste, annoncée mais pas encore dite"],
         ["nous descendons dans ta région","« descendre » : du nord vers le sud, une façon de dire du Québec"],
       ]},

      {t:'piege', h:"Trois façons de perdre le fil",
       rows:[
         ["lire vite les petits mots","les lire comme des noms",
          "« Le », « en », « y » sont les mots les plus courts et les plus chargés du texte. Ils portent chacun une phrase entière."],
         ["croire que l'ordre du texte est l'ordre du temps","chercher les dates et les temps",
          "Ousmane parle du décès de son oncle en dernier, mais il est arrivé en février, avant le mariage de septembre."],
         ["s'arrêter au premier mot inconnu","continuer jusqu'au point",
          "Dans un texte long, le sens d'un mot inconnu arrive souvent deux lignes plus loin, tout seul."],
       ]},

      {t:'revoir', h:"À retenir",
       p:"Un texte long ne se lit pas mot à mot. On regarde d'abord sa <b>forme</b>, on lit ensuite pour les <b>faits</b>, puis on relit pour les <b>liens</b> : les reprises, les temps, les connecteurs. Devant un petit mot sans nom, on recule d'une phrase."},
    ]
  },

  t1repr: {
    eye:'Mini-leçon', tit:"Reprendre sans répéter : le, en, y",
    blocs:[
      {t:'texte', h:"Pourquoi la langue fait ça",
       p:"Personne n'écrit « J'ai vendu la maison de la rue Perreault. La maison de la rue Perreault était trop petite. » On remplace, et c'est tant mieux : un texte qui répète tout est illisible. Mais chaque remplacement laisse au lecteur un petit travail à faire.",
       note:"Le programme appelle ce savoir la « reprise de l'information ». C'est le premier des cinq savoirs de grammaire du texte du niveau 6."},

      {t:'ana', h:"« le » : une idée entière, ou un nom précis",
       p:"Deux emplois très différents sous le même mot.",
       mots:[['Une idée entière','Je sais <u>qu\'elle arrive vendredi</u>. → Je <b>le</b> sais.'],
             ['Un nom précis','Il a vendu <u>la maison</u>. → Il <b>l\'</b>a vendue.', true],
             ['La différence à l\'écrit','le « le » d\'idée ne s\'accorde jamais ; l\'autre fait accorder le participe'],
             ['Où il se place','devant le verbe, toujours : je le sais · je ne le savais pas']],
       say:"Je le sais depuis mardi.",
       note:"Au passé composé avec « avoir », le participe s'accorde avec le complément placé devant : « il l'a vendue » — parce que « l' » remplace « la maison »."},

      {t:'ana', h:"« en » : de + chose",
       p:"Il remplace un groupe qui commence par « de », mais seulement pour une chose.",
       mots:[['Une chose','Il parle <u>de son déménagement</u>. → Il <b>en</b> parle.'],
             ['Une quantité','Il a <u>deux sœurs</u>. → Il <b>en</b> a deux.', true],
             ['Une personne : on garde la préposition','Il parle <u>de sa sœur</u>. → Il parle <b>d\'elle</b>.'],
             ['Le repère','cherche un « de » dans la phrase d\'avant']],
       say:"Il en parle dans tout le deuxième paragraphe.",
       note:"« En » est le pronom le plus fréquent du français parlé, et le plus invisible : on l'entend à peine."},

      {t:'ana', h:"« y » : à + chose, ou un lieu",
       p:"Deux emplois, et les deux sont fréquents dans un courriel de nouvelles.",
       mots:[['À + chose','Je pense <u>à ce courriel</u>. → J\'<b>y</b> pense.'],
             ['Un lieu','Il n\'est pas allé <u>aux funérailles</u>. → Il n\'<b>y</b> est pas allé.', true],
             ['Une personne : jamais « y »','Je pense <u>à ma sœur</u>. → Je pense <b>à elle</b>.'],
             ['Où il se place','devant le verbe, comme les autres']],
       say:"Il n'y est pas allé.",
       note:"« Vous vous y plaisez ? » : « y » remplace « dans le nouveau quartier ». C'est la façon la plus courte de demander si un déménagement s'est bien passé."},

      {t:'labo', h:"Choisis le pronom",
       p:"Choisis ce qui est remplacé, et vois ce que ça donne.",
       axes:[
         {id:'q', lbl:'On remplace quoi ?', opts:[['a','une idée entière'],['b','de + chose'],['c','à + chose ou un lieu']]},
         {id:'n', lbl:'Quel exemple ?', opts:[['1','le premier'],['2','le second']]}],
       out:{
         a1:{w:["Je le sais."], say:"Je le sais.", n:'remplace « qu\'elle arrive vendredi »'},
         a2:{w:["Il ne le savait pas."], say:"Il ne le savait pas.", n:'le pronom reste devant le verbe, même à la négative'},
         b1:{w:["Il en parle."], say:"Il en parle.", n:'remplace « de son déménagement »'},
         b2:{w:["Il en a deux."], say:"Il en a deux.", n:'remplace « deux sœurs » : on garde le nombre'},
         c1:{w:["J'y pense."], say:"J'y pense.", n:'remplace « à ce courriel »'},
         c2:{w:["Il n'y est pas allé."], say:"Il n'y est pas allé.", n:'remplace « aux funérailles »'},
       },
       note:"Trois pronoms suffisent à faire la moitié des reprises d'un texte français."},

      {t:'piege', h:"Trois erreurs très fréquentes",
       rows:[
         ["Je pense à elle → J'y pense (pour une personne)","J'y pense seulement pour une chose",
          "« Y » et « en » ne remplacent pas les personnes. Pour une personne, on garde la préposition : à elle, de lui, d'eux."],
         ["Il l'a vendu (la maison)","Il l'a vendue",
          "Quand « l' » remplace un nom féminin et qu'il est placé devant le verbe, le participe s'accorde."],
         ["Je sais le → Je le sais","le pronom passe devant le verbe",
          "En français, le pronom complément ne suit jamais le verbe conjugué. Avec deux verbes, il se colle à l'infinitif : « je vais en parler »."],
       ]},

      {t:'check', h:"Quatre phrases à compléter",
       p:"Choisis le bon pronom.",
       qs:[
         {q:"Il parle de son déménagement. Il ___ parle beaucoup.", opts:["en","y"], ok:0,
          fb:"« De + chose » se remplace par « en »."},
         {q:"Il n'est pas allé aux funérailles. Il n'___ est pas allé.", opts:["en","y"], ok:1,
          fb:"Un lieu se remplace par « y »."},
         {q:"Je sais qu'elle arrive vendredi. Je ___ sais.", opts:["le","en"], ok:0,
          fb:"Une phrase entière se remplace par « le », qui ne s'accorde jamais."},
         {q:"Je pense souvent à ma sœur. Je pense souvent ___.", opts:["y","à elle"], ok:1,
          fb:"Pour une personne, on garde la préposition."},
       ]},

      {t:'revoir', h:"À retenir",
       p:"<b>le</b> remplace une idée entière ou un nom précis ; <b>en</b> remplace « de + chose » ; <b>y</b> remplace « à + chose » ou un lieu. Jamais pour une personne : on garde alors la préposition. Tous se placent <b>devant le verbe</b>."},
    ]
  },

  t1pqp: {
    eye:'Mini-leçon', tit:"Le plus-que-parfait : reculer d'un cran",
    blocs:[
      {t:'texte', h:"Un temps qui ne raconte rien de nouveau",
       p:"Le plus-que-parfait n'ajoute aucun évènement. Il en <b>replace</b> un. Il dit : cette action-là était déjà finie quand l'autre est arrivée. C'est le seul temps du français dont le travail soit de mettre de l'ordre.",
       note:"Le programme du niveau 6 demande seulement de le <b>comprendre</b> : « comprendre que le plus-que-parfait désigne une action précédant une autre action passée »."},

      {t:'ana', h:"Comment il se forme",
       p:"Comme le passé composé, mais avec l'auxiliaire à l'imparfait.",
       mots:[['Avec avoir','j\'avais fini · il avait vendu · nous avions lu'],
             ['Avec être','elle était arrivée · ils étaient partis', true],
             ['Aux verbes pronominaux','elle s\'était installée · ils s\'étaient revus'],
             ['La différence avec le passé composé','« il a vendu » (auxiliaire au présent) · « il avait vendu » (auxiliaire à l\'imparfait)']],
       say:"Quand je t'ai écrit, on avait déjà vendu la maison.",
       note:"Si tu sais faire un passé composé, tu sais faire un plus-que-parfait : il n'y a qu'un auxiliaire à changer."},

      {t:'ana', h:"Ce qu'il change dans un récit",
       p:"Deux phrases, les mêmes mots, deux histoires différentes.",
       mots:[['Sans lui','Kadiatou est arrivée. Mon beau-frère est tombé. → dans cet ordre'],
             ['Avec lui','Kadiatou était arrivée depuis un mois quand il est tombé. → elle avant lui', true],
             ['Ce qu\'on apprend en plus','une date qui n\'est écrite nulle part : octobre'],
             ['Pourquoi ça compte','une sœur arrivée après l\'accident n\'aurait aidé personne']],
       say:"Kadiatou était arrivée depuis un mois quand l'accident est arrivé.",
       note:"C'est exactement ce que Marisol n'avait pas vu à sa première lecture. Le calcul ne se fait pas avec des dates : il se fait avec un temps de verbe."},

      {t:'ex', h:"Six phrases du courriel",
       p:"À gauche la phrase, à droite ce qu'elle place avant quoi.",
       rows:[
         ["Quand je t'ai écrit, on l'avait déjà vendue.","la vente vient avant le courriel d'avril"],
         ["Kadiatou était arrivée depuis un mois.","son arrivée vient avant l'accident de novembre"],
         ["Il n'avait pas encore repris le travail.","le courriel est écrit avant son retour d'avril"],
         ["Marisol avait lu le courriel deux fois.","les deux lectures viennent avant la conversation"],
         ["Assia était née trois mois plus tôt.","la naissance vient avant le déménagement de juin"],
         ["Le programme avait compté douze duos.","la première année vient avant l'automne dont on parle"],
       ]},

      {t:'piege', h:"Trois confusions",
       rows:[
         ["Quand je t'ai écrit, on a vendu la maison.","on avait vendu",
          "Au passé composé, la vente se ferait au moment du courriel. Le sens change complètement."],
         ["elle était arrivé","elle était arrivée",
          "Avec « être », le participe s'accorde avec le sujet, comme au passé composé."],
         ["il avait tombé","il était tombé",
          "Les verbes qui se conjuguent avec « être » au passé composé gardent « être » au plus-que-parfait."],
       ]},

      {t:'check', h:"Quatre questions",
       p:"Une seule réponse est juste.",
       qs:[
         {q:"« Quand je t'ai écrit, on l'avait déjà vendue. » La vente a eu lieu…", opts:["avant le courriel","après le courriel"], ok:0,
          fb:"Le plus-que-parfait recule d'un cran : c'était déjà fait."},
         {q:"Le plus-que-parfait se forme avec l'auxiliaire…", opts:["au présent","à l'imparfait"], ok:1,
          fb:"j'avais fini, elle était partie."},
         {q:"« Elle était arrivée depuis un mois quand il est tombé. » Elle est arrivée…", opts:["un mois avant la chute","un mois après la chute"], ok:0,
          fb:"L'accident est en novembre : elle est donc arrivée en octobre."},
         {q:"Quelle forme est juste ?", opts:["ils s'étaient installés","ils s'avaient installés"], ok:0,
          fb:"Les verbes pronominaux prennent toujours « être »."},
       ]},

      {t:'revoir', h:"À retenir",
       p:"<b>Auxiliaire à l'imparfait + participe passé.</b> Il n'ajoute pas d'évènement : il en place un <b>avant</b> un autre évènement passé. Avec « être », le participe s'accorde avec le sujet. Deux mots l'accompagnent souvent : <b>déjà</b> et <b>ne… pas encore</b>."},
    ]
  },

  t1ordre: {
    eye:'Mini-leçon', tit:"Retrouver l'ordre quand le texte ne le donne pas",
    blocs:[
      {t:'texte', h:"L'ordre du récit n'est pas l'ordre du temps",
       p:"On raconte rarement dans l'ordre. On commence par la nouvelle la plus importante, on garde la triste pour la fin, on revient en arrière pour expliquer. Celui qui écrit le sait ; celui qui lit doit refaire le calcul.",
       note:"Dans le courriel d'Ousmane, le décès de février est raconté après le mariage de septembre. Sept évènements, deux ordres différents."},

      {t:'ana', h:"Les quatre indices d'ordre",
       p:"Aucun n'est un mot de temps comme « ensuite ». Ce sont des indices, pas des étiquettes.",
       mots:[['Les dates','le 14 mars · en juin · le samedi 12'],
             ['Les durées','depuis un mois · trois mois sans marcher · au bout de six mois', true],
             ['Le plus-que-parfait','on l\'avait déjà vendue → la vente est avant'],
             ['Les verbes qui contiennent un avant','il est <b>re</b>tourné travailler → il y travaillait déjà']],
       say:"Il est retourné travailler en avril, à temps partiel.",
       note:"Le quatrième indice est le plus discret : un simple préfixe « re- » place un évènement dans le temps."},

      {t:'ex', h:"Deux ans en sept dates",
       p:"L'ordre du temps, celui que le courriel ne donne pas d'un coup.",
       rows:[
         ["le 14 mars","naissance d'Assia, encore rue Perreault"],
         ["en juin","déménagement à l'autre bout de la ville"],
         ["en octobre","arrivée de Kadiatou, venue de Conakry"],
         ["en novembre","chute du beau-frère au garage"],
         ["en février","décès de l'oncle Mamadou, au pays"],
         ["en avril","retour au travail à temps partiel"],
         ["le 12 septembre","mariage de la cousine, à Sainte-Madeleine"],
       ]},

      {t:'piege', h:"Deux calculs qu'on rate souvent",
       rows:[
         ["« depuis un mois » = il y a un mois qu'on en parle","= ça a commencé un mois plus tôt",
          "« Elle était arrivée depuis un mois » place son arrivée un mois avant l'autre évènement, pas un mois avant le courriel."],
         ["ce qui est raconté en dernier est arrivé en dernier","le dernier paragraphe recule souvent",
          "La nouvelle triste se met à la fin par politesse, pas par chronologie."],
       ]},

      {t:'revoir', h:"À retenir",
       p:"Quatre indices donnent l'ordre : les <b>dates</b>, les <b>durées</b>, le <b>plus-que-parfait</b>, et les <b>verbes qui supposent un avant</b> (retourner, revenir, reprendre). Le dernier paragraphe d'un courriel n'est presque jamais le dernier évènement."},
    ]
  },

  t2desc: {
    eye:'Mini-leçon', tit:"Décrire quelqu'un pour qu'on le reconnaisse",
    blocs:[
      {t:'texte', h:"Décrire pour raconter, décrire pour retrouver",
       p:"Ce ne sont pas les mêmes descriptions. Pour raconter, on donne ce qui frappe : un beau sourire, un air fatigué. Pour retrouver quelqu'un dans un terminus, on donne ce qui se voit de loin et ce qui ne change pas. Un beau sourire ne sert à rien à vingt pieds.",
       note:"L'intention du programme est « décrire quelqu'un », en production orale. Les attentes de fin de cours précisent : « il décrit de façon détaillée les caractéristiques physiques »."},

      {t:'ana', h:"L'ordre qui fonctionne : de loin vers près",
       p:"Quatre temps, toujours dans le même ordre. Celui qui écoute cherche dans cet ordre-là.",
       mots:[['1. La silhouette','taille, carrure, âge approximatif : ce qu\'on voit à vingt pieds'],
             ['2. Les vêtements et le bagage','un foulard vert, une longue veste grise, une grosse valise rouge', true],
             ['3. Le visage et les cheveux','visage allongé, cheveux ondulés attachés en chignon bas, lunettes rondes'],
             ['4. Le signe particulier','une petite cicatrice au-dessus du sourcil gauche']],
       say:"Une femme de taille moyenne, avec un foulard vert et une grosse valise rouge.",
       note:"Le signe particulier vient en dernier parce qu'il ne se voit que de près. Il sert à être sûr, pas à chercher."},

      {t:'ana', h:"Les mots du visage et des cheveux",
       p:"Le programme les nomme : « visage allongé, doigts effilés, cheveux ondulés ».",
       mots:[['La forme du visage','allongé · rond · carré · ovale'],
             ['Les cheveux','raides · ondulés · frisés · crépus — détachés, en queue de cheval, en chignon', true],
             ['Les traits','les pommettes hautes · le menton fin · le nez droit'],
             ['Ce qui se voit de loin','les lunettes, la barbe, un crâne rasé, la couleur d\'un vêtement']],
       say:"Elle a le visage allongé et des cheveux ondulés attachés en chignon bas.",
       note:"« Elle a le visage allongé » ou « elle a un visage allongé » : les deux se disent. Avec « le », on décrit ; avec « un », on ajoute."},

      {t:'ex', h:"Une description complète, en quatre temps",
       p:"Celle que Marisol donne à Ghislain, remise dans l'ordre.",
       rows:[
         ["De loin","une femme de taille moyenne, plutôt mince, dans la trentaine"],
         ["Ce qu'elle porte","un foulard vert, une longue veste grise, une grosse valise rouge à roulettes"],
         ["De près","un visage allongé, les pommettes hautes, des cheveux ondulés en chignon bas"],
         ["Ce qui ne trompe pas","des lunettes rondes à monture dorée, et une cicatrice au-dessus du sourcil gauche"],
       ]},

      {t:'piege', h:"Trois descriptions inutilisables",
       rows:[
         ["Elle est jolie et elle a l'air gentille.","Taille moyenne, cheveux ondulés attachés, lunettes rondes.",
          "Ce qui dépend de celui qui regarde ne se cherche pas dans une foule."],
         ["Elle a une grande valise… enfin, elle est de taille moyenne.","Elle est de taille moyenne ; sa valise est grosse.",
          "Quand un adjectif peut se rapporter à deux noms, il faut refaire la phrase, pas ajouter une correction."],
         ["Elle a une cicatrice au sourcil.","D'abord la silhouette, la cicatrice en dernier.",
          "Un signe particulier donné en premier envoie l'autre chercher un détail invisible à distance."],
       ]},

      {t:'revoir', h:"À retenir",
       p:"Quatre temps, de loin vers près : la <b>silhouette</b>, les <b>vêtements</b>, le <b>visage et les cheveux</b>, le <b>signe particulier</b>. On donne ce qui se voit et ce qui ne change pas — jamais ce qui dépend de celui qui regarde."},
    ]
  },

  t2adj: {
    eye:'Mini-leçon', tit:"Accorder les adjectifs quand on décrit",
    blocs:[
      {t:'texte', h:"Ce qui ne s'entend pas doit quand même s'écrire",
       p:"« Grande » s'entend. « Ondulés » ne s'entend pas du tout. Dans une description écrite, la moitié des accords sont muets : c'est pourquoi il faut chercher le nom des yeux, et non de l'oreille.",
       note:"Le programme demande d'« appliquer les principales règles d'accord en genre et en nombre » des adjectifs."},

      {t:'ana', h:"La règle de base",
       p:"L'adjectif prend le genre et le nombre du nom qu'il accompagne, où qu'il soit dans la phrase.",
       mots:[['Masculin singulier','un visage allongé · un foulard vert'],
             ['Féminin singulier','une veste grise · une valise rouge', true],
             ['Masculin pluriel','des cheveux ondulés · des yeux verts'],
             ['Féminin pluriel','des lunettes rondes · des pommettes hautes']],
       say:"une longue veste grise et des cheveux ondulés",
       note:"« Cheveux » est masculin pluriel, « lunettes » est féminin pluriel : ces deux noms-là décident de presque tous les accords d'une description."},

      {t:'ana', h:"Trois cas particuliers, tous fréquents ici",
       p:"Ils reviennent dans chaque description physique.",
       mots:[['Adjectif déjà en « e »','un homme mince · une femme mince — rien ne change au féminin'],
             ['Couleur en deux mots','une casquette bleu marine · des yeux vert clair — invariable', true],
             ['Adjectif après « être », « avoir l\'air »','elle est grande · ils ont l\'air fatigués'],
             ['Le piège du pluriel','« mince » ne change pas au féminin, mais prend un « s » au pluriel']],
       say:"une casquette bleu marine et un manteau brun",
       note:"« Une casquette bleue » s'accorde ; « une casquette bleu marine » ne s'accorde pas. C'est le second mot qui bloque l'accord."},

      {t:'ex', h:"Huit accords de la description",
       p:"À gauche le groupe, à droite la raison de l'accord.",
       rows:[
         ["un visage allongé","masculin singulier — visage"],
         ["une longue veste grise","féminin singulier — veste, deux fois"],
         ["des cheveux ondulés","masculin pluriel — cheveux"],
         ["des lunettes rondes","féminin pluriel — lunettes"],
         ["les pommettes hautes","féminin pluriel — pommettes"],
         ["une casquette bleu marine","invariable — couleur en deux mots"],
         ["elle est grande","attribut, féminin singulier — elle"],
         ["ils ont l'air fatigués","attribut, masculin pluriel — ils"],
       ]},

      {t:'check', h:"Quatre choix",
       p:"Une seule forme est juste.",
       qs:[
         {q:"des cheveux…", opts:["ondulé","ondulés"], ok:1, fb:"« Cheveux » est masculin pluriel."},
         {q:"des lunettes…", opts:["rondes","ronds"], ok:0, fb:"« Lunettes » est féminin pluriel."},
         {q:"une casquette…", opts:["bleu marine","bleue marine"], ok:0, fb:"Une couleur en deux mots ne s'accorde jamais."},
         {q:"Elle est…", opts:["grand","grande"], ok:1, fb:"L'attribut s'accorde avec le sujet."},
       ]},

      {t:'revoir', h:"À retenir",
       p:"L'adjectif s'accorde avec <b>le nom</b>, même quand l'accord ne s'entend pas. Trois cas à connaître : les adjectifs déjà en « e » (mince), les couleurs en deux mots (bleu marine, invariables), et l'attribut après « être » ou « avoir l'air », qui s'accorde avec le sujet."},
    ]
  },

  t2place: {
    eye:'Mini-leçon', tit:"Avant ou après le nom : ce n'est pas la même chose",
    blocs:[
      {t:'texte', h:"Cinq adjectifs qui changent de sens en changeant de place",
       p:"La plupart des adjectifs français se placent après le nom, et quelques-uns avant. Mais cinq ou six d'entre eux font les deux — et ils ne veulent pas dire la même chose selon l'endroit où on les met. Ghislain le sait : il préfère « mon ancien manteau de travail » à « mon vieux manteau ».",
       note:"Le savoir du programme s'appelle « connaître le sens de certains adjectifs selon leur place : grand, propre, drôle, ancien, nouveau »."},

      {t:'ana', h:"ancien, grand, propre",
       p:"Les trois plus fréquents. Avant le nom, le sens est figuré ; après, il est concret.",
       mots:[['ancien','<b>avant</b> : d\'autrefois — mon ancien manteau · <b>après</b> : très vieux — un manteau ancien'],
             ['grand','<b>avant</b> : important — un grand homme · <b>après</b> : de haute taille — un homme grand', true],
             ['propre','<b>avant</b> : à soi — sa propre valise · <b>après</b> : lavé — une valise propre'],
             ['Le principe','avant le nom, l\'adjectif juge ; après, il décrit']],
       say:"mon ancien manteau de travail",
       note:"« Un grand homme » et « un homme grand » : la première expression parle d'une vie, la seconde d'une taille."},

      {t:'ana', h:"drôle, pauvre, seul",
       p:"Trois autres, un peu moins fréquents mais très courants à l'oral.",
       mots:[['drôle','<b>avant</b>, avec « de » : bizarre — une drôle de journée · <b>après</b> : amusant — une journée drôle'],
             ['pauvre','<b>avant</b> : qu\'on plaint — ce pauvre homme · <b>après</b> : sans argent — un homme pauvre', true],
             ['seul','<b>avant</b> : un et pas plus — une seule valise · <b>après</b> : sans personne — une femme seule'],
             ['À l\'oreille','rien ne les distingue : c\'est la place, et rien d\'autre']],
       say:"une drôle de journée",
       note:"« Une seule valise » et « une valise seule » : la première dit le nombre, la seconde dit qu'elle est abandonnée sur le quai."},

      {t:'ex', h:"Six paires à ne pas confondre",
       p:"À gauche l'expression, à droite son sens.",
       rows:[
         ["son ancien manteau","celui qu'il portait autrefois"],
         ["un manteau ancien","un manteau très vieux, presque une antiquité"],
         ["un grand homme","un homme important"],
         ["un homme grand","un homme de haute taille"],
         ["sa propre valise","la valise qui lui appartient"],
         ["une valise propre","une valise qui n'est pas sale"],
       ]},

      {t:'piege', h:"Deux malentendus faciles",
       rows:[
         ["Il m'a parlé de son grand frère : il doit mesurer six pieds.","« grand frère » = l'aîné",
          "Avec « frère » et « sœur », « grand » et « petit » disent l'âge, jamais la taille."],
         ["J'ai apporté ma propre valise : elle sort du lavage.","ma propre valise = la mienne",
          "Avant le nom, « propre » insiste sur l'appartenance. Pour dire qu'elle est nettoyée, il faut la placer après."],
       ]},

      {t:'revoir', h:"À retenir",
       p:"<b>Avant le nom, l'adjectif juge ; après, il décrit.</b> ancien, grand, propre, drôle, pauvre, seul : six adjectifs à deux sens. C'est la place, et seulement la place, qui décide."},
    ]
  },

  t2ou: {
    eye:'Mini-leçon', tit:"Qui, que, où : tout dire en une seule phrase",
    blocs:[
      {t:'texte', h:"Pourquoi le niveau 6 y tient",
       p:"« Il y a un banc. Le banc fait face au guichet. Attends là. » Trois phrases, et le lien se perd. « Attends près du banc qui fait face au guichet » : une seule, et rien ne se perd. La subordonnée relative sert exactement à ça — garder le fil au lieu de le couper.",
       note:"Le programme demande deux choses ici : « employer des phrases subordonnées relatives avec le pronom relatif où » et « employer la structure Dét + nom + subordonnée relative »."},

      {t:'ana', h:"qui, que : le sujet et le complément",
       p:"Le choix ne dépend pas du sens, mais de ce qui suit.",
       mots:[['qui','suivi d\'un verbe — la femme <b>qui</b> porte un foulard vert'],
             ['que','suivi d\'un autre sujet — le manteau <b>qu\'</b>il porte depuis quinze ans', true],
             ['Le test','si un nom ou un pronom suit tout de suite, c\'est « que »'],
             ['L\'élision','« que » devient « qu\' » devant une voyelle ; « qui » ne s\'élide jamais']],
       say:"la femme qui porte un foulard vert",
       note:"« Qui » ne perd jamais son « i », même devant « il » : « l'homme qui a parlé », jamais « qu'a parlé »."},

      {t:'ana', h:"où : un lieu, mais aussi un moment",
       p:"Le second emploi est celui qu'on oublie, et c'est celui que le programme nomme.",
       mots:[['Un lieu','la ville <b>où</b> il travaille · le terminus <b>où</b> l\'autobus arrive'],
             ['Un moment','l\'automne <b>où</b> ma sœur est arrivée · le jour <b>où</b> il est tombé', true],
             ['Ce qu\'on ne dit pas','« le jour que je suis arrivé » — on entend cette forme, elle ne s\'écrit pas'],
             ['Le repère','après un nom de temps — jour, moment, année, époque, automne']],
       say:"le jour où il est tombé",
       note:"En français parlé du Québec, on entend souvent « le jour que ». À l'écrit, et au niveau 6, c'est « où »."},

      {t:'ana', h:"Dét + nom + relative : une description complète en un groupe",
       p:"C'est la structure du niveau : tout le portrait tient dans un seul groupe du nom.",
       mots:[['Le début','une femme de taille moyenne'],
             ['La relative','qui porte des lunettes rondes', true],
             ['Une deuxième','et qui tire une grosse valise rouge'],
             ['Le tout','une femme de taille moyenne qui porte des lunettes rondes et qui tire une grosse valise rouge']],
       say:"une femme de taille moyenne qui porte des lunettes rondes et qui tire une grosse valise rouge",
       note:"Deux relatives suffisent. Trois ou quatre, et celui qui écoute perd le début de la phrase."},

      {t:'labo', h:"Assemble la phrase",
       p:"Choisis le pronom relatif et vois ce qu'il relie.",
       axes:[
         {id:'p', lbl:'Quel pronom ?', opts:[['a','qui'],['b','que'],['c','où']]},
         {id:'n', lbl:'Quel exemple ?', opts:[['1','le premier'],['2','le second']]}],
       out:{
         a1:{w:["le banc qui fait face au guichet"], say:"le banc qui fait face au guichet", n:'un verbe suit tout de suite'},
         a2:{w:["une valise qui a des roulettes"], say:"une valise qui a des roulettes", n:'« qui » est le sujet de « a »'},
         b1:{w:["la femme que tu cherches"], say:"la femme que tu cherches", n:'« tu » suit : c\'est « que »'},
         b2:{w:["le manteau qu'il porte depuis quinze ans"], say:"le manteau qu'il porte depuis quinze ans", n:'élision devant « il »'},
         c1:{w:["la ville où il travaille"], say:"la ville où il travaille", n:'un lieu'},
         c2:{w:["le jour où il est tombé"], say:"le jour où il est tombé", n:'un moment — jamais « que »'},
       },
       note:"Trois pronoms font presque toutes les relatives du français courant."},

      {t:'piege', h:"Trois erreurs à surveiller",
       rows:[
         ["le jour que je suis arrivé","le jour où je suis arrivé",
          "Après un nom de temps, c'est « où ». On l'entend souvent autrement ; à l'écrit, non."],
         ["la femme qu'attend l'autobus","la femme qui attend l'autobus",
          "« Qui » ne s'élide jamais. Si un verbe suit, c'est « qui », quel que soit le son."],
         ["une femme qui porte des lunettes qui a une valise qui est rouge","deux relatives au maximum",
          "Trois relatives enfilées se comprennent à l'écrit et jamais à l'oral. Coupe la phrase."],
       ]},

      {t:'revoir', h:"À retenir",
       p:"<b>qui</b> quand un verbe suit, <b>que</b> quand un autre sujet suit, <b>où</b> pour un lieu <i>et</i> pour un moment. La structure du niveau 6 : <b>Dét + nom + relative</b>, deux relatives au maximum."},
    ]
  },

  t3art: {
    eye:'Mini-leçon', tit:"Lire un article de journal de quartier",
    blocs:[
      {t:'texte', h:"Un genre qui mêle deux époques",
       p:"Un article de journal local raconte presque toujours deux choses à la fois : d'où ça vient, et ce qui s'en vient. Le premier paragraphe remonte à vingt ans, au passé simple ; le deuxième parle de cet automne, au présent. Reconnaître le passage de l'un à l'autre, c'est déjà la moitié de la lecture.",
       note:"L'intention du programme est ici en production écrite : « informer un destinataire par courriel du contenu d'un article d'intérêt général ». Pour informer, il faut d'abord lire juste."},

      {t:'ana', h:"Les quatre paragraphes d'un article de ce type",
       p:"Ils sont presque toujours dans cet ordre. Le savoir permet de trouver une information sans tout lire.",
       mots:[['1. L\'histoire','d\'où vient l\'organisme, en quelle année, à cause de quoi'],
             ['2. La nouvelle','ce qui se lance maintenant, pour qui, combien de temps', true],
             ['3. La citation','ce que dit une personne de l\'organisme, entre guillemets'],
             ['4. Le pratique','les dates, les inscriptions, le téléphone, les chiffres']],
       say:"Les inscriptions se prennent jusqu'au 30 septembre.",
       note:"Quand on cherche une date limite, on commence par le dernier paragraphe. Quand on cherche l'essentiel, on lit le deuxième."},

      {t:'ana', h:"Ce qui est un fait, ce qui est une parole rapportée",
       p:"Un article donne les deux, et il les sépare toujours par un signe.",
       mots:[['Un fait','Chaque duo s\'engage pour six mois.'],
             ['Une parole rapportée','« Personne n\'est là pour aider l\'autre », précise la coordonnatrice.', true],
             ['Un mot que le journal ne prend pas à son compte','un programme de « parrainage »'],
             ['Ce que le journal ne fait pas','dire ce qu\'il en pense — ça, c\'est la page d\'opinion']],
       say:"« Personne n'est là pour aider l'autre », précise la coordonnatrice.",
       note:"Dans un article d'information, tout ce qui ressemble à une opinion est entre guillemets et appartient à quelqu'un d'autre."},

      {t:'ex', h:"Cinq questions, cinq endroits",
       p:"Où chercher, dans un article comme celui-là.",
       rows:[
         ["De quand date l'organisme ?","premier paragraphe"],
         ["Qu'est-ce qui se lance cet automne ?","deuxième paragraphe"],
         ["Combien de temps ça dure ?","deuxième paragraphe"],
         ["Qui parle, et pour dire quoi ?","troisième paragraphe, entre guillemets"],
         ["Jusqu'à quand peut-on s'inscrire ?","dernier paragraphe"],
       ]},

      {t:'revoir', h:"À retenir",
       p:"Quatre paragraphes : l'<b>histoire</b>, la <b>nouvelle</b>, la <b>citation</b>, le <b>pratique</b>. Ce qui ressemble à une opinion est entre guillemets et appartient à quelqu'un. Pour une date limite, on commence par la fin."},
    ]
  },

  t3ps: {
    eye:'Mini-leçon', tit:"Le passé simple : le reconnaître, et rien de plus",
    blocs:[
      {t:'texte', h:"Un temps qu'on lit et qu'on n'écrit jamais",
       p:"« Tout commença dans un sous-sol d'église. » Personne ne parle comme ça, et personne n'écrit comme ça dans un courriel. Mais les journaux, les documentaires, les romans et les contes s'en servent tous les jours. Il faut donc le reconnaître — pas le produire.",
       note:"Le programme est très clair là-dessus : « reconnaître les verbes courants à la 3e personne » et « associer le passé simple au passé composé ». Deux verbes de reconnaissance."},

      {t:'ana', h:"Les terminaisons à repérer, 3e personne",
       p:"Il n'y a que deux personnes à connaître : il/elle, et ils/elles. Le reste ne se rencontre presque jamais.",
       mots:[['Verbes en -er','il commenç<b>a</b> · elles se réuni<b>rent</b> — attention, « -rent » et non « -èrent » pour les autres'],
             ['Verbes en -ir','il part<b>it</b> · ils fin<b>irent</b>', true],
             ['Beaucoup d\'autres','il p<b>ut</b> · elles v<b>oulurent</b> · il rec<b>ut</b>'],
             ['Le repère qui ne trompe pas','un « a », un « it » ou un « ut » à la fin, sans auxiliaire devant']],
       say:"Tout commença dans un sous-sol d'église.",
       note:"Il n'y a jamais d'auxiliaire au passé simple : « il commença », et non « il a commencé ». C'est le signe le plus visible."},

      {t:'ana', h:"Les quatre à savoir par cœur",
       p:"Ce sont les plus fréquents de tous, et les moins reconnaissables.",
       mots:[['être','il f<b>ut</b> → il a été'],
             ['avoir','il e<b>ut</b> → il a eu', true],
             ['faire','il f<b>it</b> → il a fait'],
             ['venir','il v<b>int</b> · ils v<b>inrent</b> → il est venu']],
       say:"Il fut le premier président de l'organisme.",
       note:"« Il fut », « il eut », « il fit », « il vint » : quatre formes courtes qui reviennent dans presque tous les récits."},

      {t:'ana', h:"Ce que ce temps ajoute au récit",
       p:"Il ne change rien aux faits. Il change la distance.",
       mots:[['Au passé composé','Une dizaine de familles se sont réunies en 1998. → ça reste proche'],
             ['Au passé simple','Une dizaine de familles se réunirent en 1998. → c\'est de l\'histoire', true],
             ['Où le journal l\'emploie','quand il remonte à dix ou vingt ans'],
             ['Où il ne l\'emploie jamais','pour la fête de samedi dernier']],
       say:"Une dizaine de familles se réunirent un jeudi soir.",
       note:"Si un article emploie le passé simple pour un évènement d'hier, c'est qu'il veut lui donner un air de légende. Ça se remarque."},

      {t:'ex', h:"Huit formes, et ce que tu dirais, toi",
       p:"À gauche le journal, à droite la conversation.",
       rows:[
         ["tout commença","tout a commencé"],
         ["elles se réunirent","elles se sont réunies"],
         ["elles ne se quittèrent plus","elles ne se sont plus quittées"],
         ["il fut le premier président","il a été le premier président"],
         ["le local eut trois adresses","le local a eu trois adresses"],
         ["le quartier fit sa fête","le quartier a fait sa fête"],
         ["vingt familles vinrent","vingt familles sont venues"],
         ["le programme compta douze duos","le programme a compté douze duos"],
       ]},

      {t:'check', h:"Quatre reconnaissances",
       p:"Quel verbe se cache derrière la forme ?",
       qs:[
         {q:"« il fut »", opts:["être","faire"], ok:0, fb:"« Il fut » = il a été."},
         {q:"« ils vinrent »", opts:["voir","venir"], ok:1, fb:"« Ils vinrent » = ils sont venus."},
         {q:"« elle fit »", opts:["faire","finir"], ok:0, fb:"« Elle fit » = elle a fait."},
         {q:"Le passé simple s'emploie…", opts:["dans un courriel à un ami","dans un article qui remonte à vingt ans"], ok:1,
          fb:"Jamais dans une conversation ni dans un courriel."},
       ]},

      {t:'revoir', h:"À retenir",
       p:"Aucun auxiliaire, et une terminaison en <b>-a</b>, <b>-rent</b>, <b>-it</b>, <b>-irent</b>, <b>-ut</b> ou <b>-urent</b>. Quatre formes à connaître par cœur : <b>il fut</b>, <b>il eut</b>, <b>il fit</b>, <b>il vint</b>. On le remplace dans sa tête par un passé composé — et on ne l'écrit jamais soi-même."},
    ]
  },

  t3conn: {
    eye:'Mini-leçon', tit:"Les connecteurs : deviner la suite d'une demi-phrase d'avance",
    blocs:[
      {t:'texte', h:"Ce que gagne celui qui les lit",
       p:"Un connecteur annonce ce qui s'en vient avant que ça arrive. « Pourtant » prévient qu'on va dire le contraire ; « donc » prévient qu'on va conclure. Celui qui les lit avance plus vite et se trompe moins. Celui qui les saute lit deux fois.",
       note:"« Connecteurs et relations logiques » est le savoir de grammaire du texte le plus fourni du niveau 6 : huit points à lui seul."},

      {t:'ana', h:"Les quatre familles",
       p:"Quatre relations, et presque tous les connecteurs y entrent.",
       mots:[['Ajouter','de plus · d\'ailleurs · en outre — la suite va dans le même sens'],
             ['Opposer','pourtant · cependant · en revanche — la suite va contre', true],
             ['Expliquer','car · parce que · en effet — la suite dit pourquoi'],
             ['Conclure','donc · c\'est pourquoi · ainsi — la suite est le résultat']],
       say:"Le programme est gratuit. Pourtant, il reste des places.",
       note:"« Ainsi » appartient à deux familles : il conclut, mais il annonce aussi un exemple. C'est le seul qui soit vraiment ambigu."},

      {t:'ana', h:"Les connecteurs de temps, qui ordonnent le récit",
       p:"Ils ne donnent pas de date, mais ils mettent en ordre.",
       mots:[['Le rang','d\'abord · ensuite · enfin'],
             ['Le point de départ','depuis · à partir de', true],
             ['La durée écoulée','au bout de · après'],
             ['Ce qu\'ils remplacent','les dates, quand celui qui écrit ne les a pas']],
       say:"Au bout de six mois, les deux familles se voyaient encore.",
       note:"« Depuis 1998 » dit un point de départ ; « au bout de six mois » dit une durée écoulée. Les deux se confondent facilement."},

      {t:'ex', h:"Huit connecteurs, huit annonces",
       p:"À gauche le mot, à droite ce qu'il te promet.",
       rows:[
         ["pourtant","ce qui suit va contre ce que tu viens de lire"],
         ["d'ailleurs","ce qui suit ajoute, dans le même sens"],
         ["car","ce qui suit explique pourquoi"],
         ["c'est pourquoi","ce qui suit est le résultat"],
         ["par exemple","ce qui suit illustre, sans rien ajouter de nouveau"],
         ["d'abord","c'est le premier de plusieurs"],
         ["depuis","le point de départ d'une durée qui continue"],
         ["au bout de","une durée déjà écoulée"],
       ]},

      {t:'piege', h:"Deux confusions coûteuses",
       rows:[
         ["lire « pourtant » comme « donc »","« pourtant » annonce le contraire",
          "Confondre l'opposition et la conséquence fait comprendre l'inverse de ce qui est écrit."],
         ["« depuis six mois » = « il y a six mois »","« depuis » dit que ça dure encore",
          "« Il habite ici depuis six mois » : il y habite toujours. « Il est arrivé il y a six mois » : c'est fini."],
       ]},

      {t:'check', h:"Quatre suites à deviner",
       p:"Que va dire la phrase suivante ?",
       qs:[
         {q:"« Le programme est gratuit. Pourtant… »", opts:["il reste des places","tout le monde s'inscrit"], ok:0,
          fb:"« Pourtant » annonce le contraire de ce qu'on attendrait."},
         {q:"« Marisol travaille vendredi. C'est pourquoi… »", opts:["Ghislain ira au terminus","elle aime son métier"], ok:0,
          fb:"« C'est pourquoi » annonce une conséquence."},
         {q:"« Elle n'est pas venue, car… »", opts:["elle travaillait de nuit","elle viendra demain"], ok:0,
          fb:"« Car » annonce une explication."},
         {q:"« Les activités sont libres : une marche, un souper, par exemple… »", opts:["une visite au marché","c'est gratuit"], ok:0,
          fb:"« Par exemple » annonce un élément de la même liste."},
       ]},

      {t:'revoir', h:"À retenir",
       p:"Quatre familles : <b>ajouter</b> (d'ailleurs), <b>opposer</b> (pourtant), <b>expliquer</b> (car), <b>conclure</b> (donc, c'est pourquoi). Plus les connecteurs de temps, qui ordonnent sans dater. Un connecteur se lit <b>avant</b> la phrase qu'il annonce."},
    ]
  },

  t3ponct: {
    eye:'Mini-leçon', tit:"Le tiret, les guillemets, et la virgule du groupe détaché",
    blocs:[
      {t:'texte', h:"Trois signes qui portent du sens",
       p:"Dans un journal, ces signes ne sont pas là pour aérer la page. Chacun dit quelque chose, et ne pas le lire, c'est perdre une information. On les rencontre bien avant d'avoir à les écrire : on les apprend donc d'abord en lecteur.",
       note:"Le programme du niveau 6 nomme les trois : comprendre le tiret, employer les guillemets pour souligner ou nuancer un mot, employer la virgule pour encadrer un groupe détaché."},

      {t:'ana', h:"Le tiret, trois emplois",
       p:"Le même signe, trois travaux. C'est la place dans la phrase qui les distingue.",
       mots:[['Après une phrase complète','il ouvre une <b>énumération</b>'],
             ['En tête de ligne','il marque un <b>changement de locuteur</b>', true],
             ['En paire, au milieu','il encadre une <b>précision</b>, comme des parenthèses'],
             ['Ce qu\'il ne fait jamais','remplacer un point ou une virgule ordinaire']],
       say:"Trois activités — une marche, un souper, une visite au marché.",
       note:"Le tiret de la paire s'ouvre et se ferme. Un tiret seul au milieu d'une phrase est presque toujours le premier emploi."},

      {t:'ana', h:"Les guillemets, deux emplois opposés",
       p:"L'un rend les mots à quelqu'un ; l'autre les met à distance. Les confondre fait tout lire à l'envers.",
       mots:[['Autour d\'une phrase entière','ce sont les <b>mots exacts</b> de quelqu\'un'],
             ['Autour d\'un seul mot','l\'auteur <b>ne le prend pas à son compte</b>', true],
             ['Le repère de la citation','elle est annoncée : « dit-elle », « précise la coordonnatrice »'],
             ['Le repère de la distance','le mot est courant, et souvent celui de quelqu\'un d\'autre']],
       say:"L'organisme parle de « duos » plutôt que de « parrainage ».",
       note:"« Un programme de parrainage » et « un programme de “parrainage” » ne disent pas la même chose : dans le second, le journal se met à part du mot."},

      {t:'ana', h:"La virgule du groupe détaché",
       p:"Deux virgules autour d'un nom qui en explique un autre. On peut retirer le groupe sans casser la phrase.",
       mots:[['La forme','Le Fil d\'ici<b>,</b> l\'organisme du quartier<b>,</b> occupe deux locaux.'],
             ['Le test','retire le groupe : la phrase tient encore', true],
             ['L\'erreur fréquente','une seule virgule au lieu de deux'],
             ['À quoi ça sert','ajouter une explication sans faire une phrase de plus']],
       say:"Le Fil d'ici, l'organisme du quartier, occupe deux locaux.",
       note:"Une virgule ouvrante sans virgule fermante laisse le lecteur suspendu : c'est l'erreur de ponctuation la plus fréquente à l'écrit."},

      {t:'ex', h:"Six exemples, et ce qu'ils apportent",
       p:"À gauche la phrase, à droite ce que le signe ajoute.",
       rows:[
         ["Trois activités — une marche, un souper, une visite.","Le tiret annonce la liste qui suit."],
         ["— Et si personne ne s'inscrit ?","Quelqu'un d'autre prend la parole."],
         ["Le mot parrainage — que l'organisme refuse — suppose une aide.","Précision ajoutée, qu'on pourrait retirer."],
         ["« Les deux familles apprennent », précise-t-elle.","Ce sont ses mots exacts."],
         ["un programme de « parrainage »","Le journal ne prend pas ce mot à son compte."],
         ["Le Fil d'ici, l'organisme du quartier, occupe deux locaux.","Une explication glissée entre deux virgules."],
       ]},

      {t:'revoir', h:"À retenir",
       p:"Le <b>tiret</b> ouvre une liste, marque qui parle, ou encadre une précision. Les <b>guillemets</b> citent quelqu'un (phrase entière) ou prennent une distance (un seul mot). Les <b>deux virgules</b> encadrent un groupe qu'on pourrait retirer."},
    ]
  },

  t3plan: {
    eye:'Mini-leçon', tit:"Informer quelqu'un du contenu d'un article",
    blocs:[
      {t:'texte', h:"Informer n'est pas donner son avis",
       p:"Quand tu écris à quelqu'un pour lui parler d'un article, il ne l'a pas lu. Tout ce qu'il en saura viendra de toi. S'il ne peut plus distinguer ce que le journal a écrit de ce que tu en penses, tu ne l'as pas informé : tu lui as donné ton opinion en lui faisant croire que c'était une nouvelle.",
       note:"C'est l'une des quatre intentions du programme pour cette situation : « informer un destinataire par courriel du contenu d'un article d'intérêt général »."},

      {t:'ana', h:"Les quatre paragraphes, dans cet ordre",
       p:"Chacun a un travail, et un seul.",
       mots:[['1. D\'où ça vient','J\'ai lu ça dans L\'Écho de la Yamaska de cette semaine.'],
             ['2. Les faits','ce que c\'est, pour qui, combien de temps, à quel rythme', true],
             ['3. Ton avis, annoncé','À mon avis, ça conviendrait bien à Kadiatou.'],
             ['4. Ce qu\'on peut faire','Les inscriptions se prennent jusqu\'au 30 septembre.']],
       say:"J'ai lu ça dans L'Écho de la Yamaska de cette semaine.",
       note:"Un courriel d'information sans quatrième paragraphe se lit et s'oublie. Une date limite ou un numéro de téléphone lui donne une suite."},

      {t:'ana', h:"Les trois mots qui séparent le fait de l'avis",
       p:"Ils ne coûtent rien et ils changent tout.",
       mots:[['Pour annoncer un avis','à mon avis · pour ma part · je trouve que'],
             ['Pour rapporter un fait','selon l\'article · le journal écrit que · la coordonnatrice dit que', true],
             ['Pour marquer un doute','il semble que · si j\'ai bien compris'],
             ['Ce qu\'on n\'écrit pas','« C\'est une excellente idée » au milieu du résumé']],
       say:"À mon avis, ça conviendrait bien à Kadiatou.",
       note:"Trois mots suffisent. Sans eux, celui qui lit attribue ton opinion au journal — et il la répétera comme un fait."},

      {t:'ex', h:"Un courriel d'information, phrase par phrase",
       p:"Le plan, avec une phrase pour chaque temps.",
       rows:[
         ["Objet","Un programme de jumelage à Saint-Hyacinthe"],
         ["Paragraphe 1","J'ai lu un article dans L'Écho de la Yamaska de cette semaine."],
         ["Paragraphe 2","Un organisme du quartier jumelle des familles pour six mois, à raison d'une rencontre aux deux semaines."],
         ["Paragraphe 3","À mon avis, ça conviendrait bien à Kadiatou, qui ne connaît personne ici."],
         ["Paragraphe 4","Les inscriptions se prennent jusqu'au 30 septembre, au local ou par téléphone."],
         ["Dernière ligne","Écris-moi ce que tu en penses. Marisol"],
       ]},

      {t:'piege', h:"Trois façons de mal informer",
       rows:[
         ["Il y a un super programme, tu devrais t'inscrire !","Le journal décrit un programme de jumelage de six mois.",
          "Tout est avis, aucun fait. Celui qui lit ne sait toujours pas ce que c'est."],
         ["Ils font du parrainage pour les nouveaux arrivants.","L'organisme parle de « duos » et refuse le mot « parrainage ».",
          "Résumer avec le mot que la source a justement refusé, c'est la déformer."],
         ["copier l'article au complet dans le courriel","trois ou quatre faits choisis",
          "Un article recopié n'est pas un résumé : celui qui lit refait tout le travail que tu devais faire."],
       ]},

      {t:'revoir', h:"À retenir",
       p:"Quatre paragraphes : <b>d'où ça vient</b>, <b>les faits</b>, <b>ton avis annoncé comme un avis</b>, <b>ce qu'on peut faire</b>. Trois mots séparent le fait de l'opinion : « selon l'article » d'un côté, « à mon avis » de l'autre."},
    ]
  },

};
