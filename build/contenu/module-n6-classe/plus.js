const PLUS = {
  // Treize mini-leçons. La clé d'une mini-leçon est l'`id` de l'exercice
  // qu'elle explique : c'est ce qui permet au bandeau d'aide de proposer la
  // bonne leçon après plusieurs erreurs. Une clé qui ne correspond à aucun
  // exercice n'est jamais atteignable.
  //
  // Tout bloc `ana` porte son champ `say:` — sans lui, l'extrait audio lit
  // les balises HTML à voix haute, et ça ne se découvre qu'une fois les MP3
  // payés.
  //
  // Trois savoirs de ce module sont communs à tout le niveau 6 — la
  // graphie-phonie, la reprise de l'information, le passé simple — et les
  // huit modules du niveau les rencontrent tous. La leçon a donc été écrite
  // ici **en repartant de zéro**, ancrée dans le travail de recherche : un
  // module voisin a déjà payé 9 % de coïncidence pour avoir repris la
  // structure d'une mini-leçon du pilote.

  prGraphie: {
    eye:'Mini-leçon', tit:"Le mot qu'on ne trouve pas au dictionnaire",
    blocs:[
      {t:'texte', h:"Le moment exact où ça vous arrive",
       p:"Vous cherchez de l'information. Quelqu'un prononce un mot, vous l'écrivez comme vous l'avez entendu, vous le tapez dans le catalogue de la bibliothèque — et il n'y a rien. Le mot existe pourtant. Il ne s'écrit simplement pas comme il se dit, parce qu'il porte une lettre qu'on n'entend pas. Trois familles suffisent à expliquer presque tous ces échecs de recherche.",
       note:"Le programme du niveau 6 les nomme ainsi : associer des phonèmes à des graphèmes inhabituels — ch qui vaut k, x qui vaut s, sh et sch qui valent ch."},

      {t:'ana', h:"Première famille — un ch qui sonne k",
       p:"Ce sont des mots de science et de savoir. Vous les rencontrerez sur une liste de sujets de recherche bien avant de les entendre dans une conversation.",
       mots:[['Ce que la page montre','le {ch}lore · un {ch}ronomètre · une or{ch}idée · le {ch}aos'],
             ['Ce que la bouche fait','un k sec, comme au début de « cabane »', true],
             ['Le signe qui ne trompe pas','un mot long, savant, souvent voisin d\'un y ou d\'un ph']],
       say:"le chlore, un chronomètre, une orchidée, le chaos",
       note:"« Chercher », « chaque » et « chose » n'ont rien à voir avec cette famille. Le k ne concerne qu'une petite liste, apprise une fois."},

      {t:'ana', h:"Deuxième famille — un x qui sonne s",
       p:"Trois nombres, pas un de plus. Mais ce sont trois nombres qu'une consigne écrite vous donnera vingt fois : nombre de pages, nombre de sources, date de remise.",
       mots:[['Ce que la page montre','si{x} · di{x} · soi{x}ante'],
             ['Ce que la bouche fait','un s franc, comme à la fin d\'« autobus »', true],
             ['Ce qui bouge selon la suite','seul, on entend le s ; devant une consonne, il disparaît ; devant une voyelle, il devient z']],
       say:"six, dix, soixante",
       note:"Essayez sur une échéance : « le six » se dit sisse, « six novembre » se dit si novembre, « six ans » se dit siz ans. Même mot, trois fins."},

      {t:'ana', h:"Troisième famille — sh et sch qui sonnent ch",
       p:"Des mots venus d'ailleurs et installés chez nous. Ils sont brefs, et rien dans leur écriture ne prévient l'œil.",
       mots:[['Ce que la page montre','un {sch}éma · un {sh}ampoing · un {sh}ort'],
             ['Ce que la bouche fait','le souffle de « chat », exactement', true],
             ['Le signe qui ne trompe pas','un mot court, souvent un objet du quotidien']],
       say:"un schéma, un shampoing, un short",
       note:"Retenez « un schéma » avant les autres : une page d'information municipale en contient presque toujours un, et c'est lui qui explique la démarche d'un coup d'œil."},

      {t:'labo', h:"Le mot entendu, puis répété",
       p:"Choisissez une famille, puis un exemple.",
       axes:[
         {id:'f', lbl:'Quelle famille ?', opts:[['a','ch qui sonne k'],['b','x qui sonne s'],['c','sh et sch qui sonnent ch']]},
         {id:'n', lbl:'Quel exemple ?', opts:[['1','le premier'],['2','le second']]}],
       out:{
         a1:{w:["le chlore"], say:"le chlore", n:'deux syllabes, la première commence par un k'},
         a2:{w:["une orchidée"], say:"une orchidée", n:'or-ki-dée, jamais or-chi-dée'},
         b1:{w:["dix"], say:"dix", n:'isolé, le mot se termine par un s bien net'},
         b2:{w:["soixante"], say:"soixante", n:'soi-sante : aucun k au milieu'},
         c1:{w:["un schéma"], say:"un schéma", n:'trois consonnes écrites, un seul souffle'},
         c2:{w:["un shampoing"], say:"un shampoing", n:'le mot vient de loin, la bouche reste française'},
       },
       note:"Écoutez deux fois avant d'ouvrir la bouche. Ce qu'on entraîne ici, c'est l'oreille ; la langue suit toute seule."},

      {t:'ex', h:"Huit mots, vus puis dits",
       p:"À gauche ce que vous lirez, à droite ce que vous entendrez.",
       rows:[
         ["le chlore","clore, avec un k au début"],
         ["un chronomètre","cro-no-mètre, sans aucun souffle de chat"],
         ["l'archéologie","ar-ké-o-lo-gie, en cinq temps"],
         ["la technique","tec-nique, comme technologie"],
         ["six sources","si sources : le x disparaît devant la consonne"],
         ["soixante","soi-sante, jamais soi-ksante"],
         ["un schéma","ché-ma, trois lettres pour un souffle"],
         ["un short","chort, à la française"],
       ]},

      {t:'piege', h:"Ce qui bloque une recherche, et ce qui n'est pas grave",
       rows:[
         ["taper le mot exactement comme on l'a entendu","essayer la lettre muette avant d'abandonner",
          "Vous cherchez « cronomètre » et le catalogue reste vide. Prenez l'habitude d'essayer un ch devant un k et un x devant un s : le mot apparaît presque toujours du premier coup, et vous venez de gagner un quart d'heure."],
         ["donner à tous les ch le souffle de chat","apprendre la petite liste savante",
          "Prononcer « technique » avec le souffle de « chat » rend le mot méconnaissable, et personne ne devinera. Ces mots-là se comptent sur les doigts : une carte suffit."],
         ["se crisper sur les trois façons de dire six","viser la reconnaissance, pas la perfection",
          "Personne ne vous reprendra sur « siz jours ». Ce qu'il faut, c'est comprendre l'échéance qu'on vous donne. La produire parfaitement viendra plus tard, ou pas du tout, et la grille d'évaluation ne l'évalue pas."],
       ]},

      {t:'check', h:"Vérifions en quatre questions",
       p:"Une seule bonne réponse chaque fois.",
       qs:[
         {q:"Dans « un chronomètre », les lettres ch produisent…", opts:["le souffle de chat","un k"], ok:1,
          fb:"Cro-no-mètre. Le mot vient du grec, comme presque tous ceux de cette famille."},
         {q:"Dans « soixante », la lettre x produit…", opts:["un s","le groupe ks"], ok:0,
          fb:"Soi-sante. Le x y fait le même travail que dans six et dans dix."},
         {q:"Dans « un schéma », les lettres sch produisent…", opts:["le groupe sk","le souffle de chat"], ok:1,
          fb:"Trois consonnes à l'œil, un seul souffle à l'oreille."},
         {q:"« Six sources » se dit…", opts:["si sources","sisse sources"], ok:0,
          fb:"Devant une consonne, la fin de six s'efface complètement."},
       ]},

      {t:'revoir', h:"Ce qu'il faut garder",
       p:"Trois familles, et rien d'autre : <b>ch</b> sonne k dans les mots de science (chlore, orchidée, technique) ; <b>x</b> sonne s dans six, dix et soixante ; <b>sh</b> et <b>sch</b> prennent le souffle de chat (schéma, short). Devant un mot introuvable au catalogue, essayez la lettre muette avant de renoncer."},
    ]
  },

  prEtapes: {
    eye:'Mini-leçon', tit:"Trois semaines, et où elles passent vraiment",
    blocs:[
      {t:'texte', h:"Le calendrier que personne ne vous donne",
       p:"Une consigne dit ce qu'il faut remettre et quand. Elle ne dit jamais comment répartir le temps, et c'est pourtant là que se joue la note. Toutes les équipes qui coulent un travail de recherche font la même chose : elles cherchent longtemps, elles écrivent vite, et elles ne relisent pas. Voici l'ordre inverse, et pourquoi il vaut mieux.",
       note:"Rien de tout ceci n'est une règle de français. C'est de la méthode, et c'est la partie du travail qu'on n'enseigne presque jamais."},

      {t:'ana', h:"Semaine 1 — décider",
       p:"Le sujet et les sources. Rien d'écrit encore, et c'est normal : cette semaine-là ne produit aucune page, et elle décide de tout le reste.",
       mots:[['Ce qui doit être fini','le sujet approuvé et trois sources trouvées'],
             ['Le signe que ça va bien','vous pouvez dire votre sujet en une phrase à quelqu\'un qui ne l\'a pas lu', true],
             ['Le signe que ça va mal','vous avez douze pages imprimées et aucune question précise']],
       say:"Semaine un : décider. Le sujet approuvé et trois sources trouvées.",
       note:"Une équipe qui n'a pas de sujet approuvé le vendredi de la première semaine a déjà perdu une semaine, et elle ne le sait pas encore."},

      {t:'ana', h:"Semaine 2 — écrire",
       p:"Le plan d'abord, le texte ensuite. Jamais l'inverse : on ne déplace pas un paragraphe déjà écrit sans le réécrire au complet.",
       mots:[['Ce qui doit être fini','le plan, puis un premier texte complet, même imparfait'],
             ['Le bon réflexe','écrire la bibliographie en même temps que le texte, pas après', true],
             ['Ce qui fait perdre deux jours','chercher encore des sources pendant qu\'on écrit']],
       say:"Semaine deux : écrire. Le plan d'abord, puis un premier texte complet.",
       note:"Un premier texte laid mais complet vaut mieux que trois beaux paragraphes et un trou. Ce qui est complet se corrige ; ce qui manque se réécrit."},

      {t:'ana', h:"Semaine 3 — corriger et répéter",
       p:"Deux tâches distinctes, et la deuxième est celle qu'on oublie.",
       mots:[['La relecture à voix haute','à trois, ensemble : c\'est la seule façon de faire disparaître les coutures entre trois écritures'],
             ['La répétition de l\'exposé','trois fois, chronomètre en main', true],
             ['La vérité sur les cinq minutes','la première répétition dure toujours huit minutes, sans exception']],
       say:"Semaine trois : corriger et répéter. La relecture à voix haute, puis l'exposé trois fois.",
       note:"Répéter un exposé n'est pas de l'orgueil : c'est ce qui permet de ne pas lire sa feuille, et de ne pas lire sa feuille est explicitement demandé."},

      {t:'ex', h:"Ce qui se décide à chaque moment",
       p:"Six moments, six décisions. Aucune ne se rattrape à l'étape suivante.",
       rows:[
         ["La formation de l'équipe","Qui fait quoi. Le dire à voix haute et l'écrire, sinon deux personnes feront la même partie."],
         ["Le choix du sujet","Une question précise, pas un thème. « Le bac brun » n'est pas une question."],
         ["La recherche des sources","Trois genres différents, avec leur date, notées pendant la lecture."],
         ["L'écriture du plan","Une ligne par idée principale. C'est le squelette, il se corrige en deux minutes."],
         ["La rédaction","Un paragraphe par ligne du plan, plus la bibliographie."],
         ["La préparation de l'exposé","Ce qu'on dira en cinq minutes, répété jusqu'à tenir dans le temps."],
       ]},

      {t:'piege', h:"Les trois façons de perdre une semaine",
       rows:[
         ["chercher avant d'avoir un sujet approuvé","faire approuver, puis chercher",
          "Deux semaines de lecture sur une question que l'enseignante va refuser, ça s'est vu. L'approbation prend deux minutes et ne coûte rien."],
         ["se partager le travail au lieu de le faire ensemble","écrire chacun sa partie, puis relire à trois",
          "Trois textes collés bout à bout se reconnaissent à la première page : le ton change, les mots changent, les mêmes choses sont dites deux fois. La relecture commune est ce qui fait la différence, et elle prend une heure."],
         ["préparer l'exposé la veille","répéter trois fois dans la dernière semaine",
          "Cinq minutes, c'est très court. Sans répétition, on en dit la moitié en huit minutes, on se fait couper, et on n'arrive jamais à la conclusion — qui est justement la partie évaluée."],
       ]},

      {t:'check', h:"Vérifions en trois questions",
       p:"Une seule bonne réponse chaque fois.",
       qs:[
         {q:"Quand faut-il écrire la bibliographie ?", opts:["pendant qu'on lit les sources","la veille de la remise"], ok:0,
          fb:"Retrouver trois jours plus tard la page d'où venait une phrase prend plus de temps que de l'avoir notée sur le coup."},
         {q:"Qu'est-ce qui vient avant le texte ?", opts:["le plan","la conclusion"], ok:0,
          fb:"Un plan se corrige en deux traits de crayon ; un texte déjà écrit se réécrit au complet."},
         {q:"Combien de fois répéter un exposé de cinq minutes ?", opts:["une fois suffit","trois fois, chronomètre en main"], ok:1,
          fb:"La première répétition dure toujours huit minutes. C'est la deuxième et la troisième qui la ramènent à cinq."},
       ]},

      {t:'revoir', h:"À retenir",
       p:"Semaine 1 : <b>décider</b> — le sujet et les sources. Semaine 2 : <b>écrire</b> — le plan, puis le texte. Semaine 3 : <b>corriger et répéter</b>. La semaine qui ne produit aucune page est celle qui décide de la note."},
    ]
  },

  t1cons: {
    eye:'Mini-leçon', tit:"Une consigne ne se lit pas, elle se démonte",
    blocs:[
      {t:'texte', h:"Pourquoi deux personnes lisent la même feuille différemment",
       p:"Marisol a compris deux documents à remettre, Youssef un seul. Aucun des deux n'a mal lu au sens ordinaire : ils ont lu comme on lit un texte, en suivant le sens général. Or une consigne n'a pas de sens général. Chaque phrase y porte une obligation distincte, et rien n'est jamais dit deux fois. Il faut donc une autre façon de lire.",
       note:"C'est la seule intention de communication que le programme rattache à cette situation, au niveau 6 : comprendre de l'information liée à un sujet de recherche. Elle commence par la consigne, avant les sources."},

      {t:'ana', h:"Un crayon, et sept verbes",
       p:"Lisez une ligne à la fois et soulignez chaque verbe qui vous dit de faire quelque chose. Comptez-les à la fin : c'est le nombre de choses que vous devez faire.",
       mots:[['Les verbes à souligner','choisira · cherchera · remettra · présentera · sera organisé'],
             ['Ce qu\'ils ont en commun','ils sont au futur, et ce futur donne un ordre', true],
             ['Ce qu\'il faut en faire','les recopier en liste, dans l\'ordre, sur une feuille à part']],
       say:"choisira, cherchera, remettra, présentera, sera organisé",
       note:"Cette liste-là, c'est votre plan de travail. Elle est déjà écrite dans la consigne : personne ne vous demande de l'inventer."},

      {t:'ana', h:"Les trois choses qu'on saute toujours",
       p:"Ce ne sont jamais les mêmes phrases qui manquent : ce sont toujours les mêmes endroits.",
       mots:[['Ce qui suit un point-virgule','la moitié des conditions vivent après un point-virgule, et l\'œil s\'arrête au point'],
             ['La deuxième moitié d\'une longue phrase','« un texte de deux pages et le plan qui a servi à l\'écrire » — la partie qui manque est presque toujours celle d\'après le « et »', true],
             ['La dernière ligne du document','c\'est là qu\'on met ce qui n\'est pas négociable, l\'échéance en particulier']],
       say:"Ce qui suit un point-virgule. La deuxième moitié d'une longue phrase. La dernière ligne du document.",
       note:"Relisez uniquement ces trois endroits avant de ranger la feuille. Deux minutes, et c'est là que se trouvent les erreurs de compréhension les plus coûteuses."},

      {t:'ex', h:"Six questions à poser à n'importe quelle consigne",
       p:"Si vous ne pouvez pas répondre à l'une d'elles, la réponse est dans la feuille et vous ne l'avez pas encore trouvée.",
       rows:[
         ["Quoi ?","Combien de documents, sous quelle forme, de quelle longueur."],
         ["Avec qui ?","Seul, à deux, à trois. Et qui forme les équipes."],
         ["Pour quand ?","La date, et ce qui arrive après cette date."],
         ["Dans quel ordre ?","Ce qui doit être fini avant que le reste commence."],
         ["Évalué comment ?","Le barème, ligne par ligne."],
         ["Et si ça ne marche pas ?","Ce que la consigne prévoit — il y a presque toujours une phrase pour ça."],
       ]},

      {t:'piege', h:"Trois façons de mal lire une consigne",
       rows:[
         ["la lire une fois, en entier, sans crayon","la lire une ligne à la fois, en soulignant",
          "Une lecture continue produit une impression générale, et une impression générale ne remet aucun document. Le crayon est ce qui transforme la lecture en liste."],
         ["croire que ce qui n'est pas dit est permis","demander avant l'échéance, jamais après",
          "Une consigne ne peut pas tout prévoir. Ce qu'elle ne dit pas se demande, et la demande elle-même compte : venir dire qu'il manque une source, avant la date, se discute. Après, non."],
         ["ranger la feuille après l'avoir lue","la ressortir avant d'écrire et avant de remettre",
          "Une consigne se lit trois fois : au début, avant d'écrire, et une dernière fois la feuille à la main juste avant de remettre. La troisième lecture prend quatre minutes et sauve des points chaque session."],
       ]},

      {t:'check', h:"Vérifions en trois questions",
       p:"Une seule bonne réponse chaque fois.",
       qs:[
         {q:"Que faut-il remettre, selon la consigne du groupe 402 ?", opts:["un texte de deux pages","un texte de deux pages et le plan"], ok:1,
          fb:"La partie qui manque est presque toujours celle d'après le « et »."},
         {q:"Où trouve-t-on ce qui n'est pas négociable ?", opts:["dans la première phrase","souvent dans la dernière ligne"], ok:1,
          fb:"L'échéance et ce qui arrive après sont presque toujours à la fin du document."},
         {q:"Combien de fois se lit une consigne ?", opts:["une fois, attentivement","trois fois : au début, avant d'écrire, avant de remettre"], ok:1,
          fb:"La troisième lecture prend quatre minutes et rattrape ce qui aurait coûté des points."},
       ]},

      {t:'revoir', h:"À retenir",
       p:"Une consigne se lit <b>une ligne à la fois, avec un crayon</b>. On souligne les verbes qui ordonnent, on en fait une liste, et on relit trois endroits : après un point-virgule, après un « et », et la dernière ligne. Ce qui n'est pas écrit se demande <b>avant</b> l'échéance."},
    ]
  },

  t1grille: {
    eye:'Mini-leçon', tit:"Une grille se lit avant d'écrire, jamais après",
    blocs:[
      {t:'texte', h:"Ce qu'on gagne à la lire au bon moment",
       p:"Presque tout le monde découvre la grille d'évaluation en même temps que sa note. Lue à ce moment-là, elle ne sert qu'à expliquer un résultat qu'on ne peut plus changer. Lue avant d'écrire, elle dit exactement où mettre son temps — et le temps, dans un travail de trois semaines, est la seule ressource qui manque.",
       note:"L'enseignante donne la grille en même temps que la consigne. Ce n'est pas une politesse : c'est ce qui permet de viser."},

      {t:'ana', h:"Chaque ligne contient un mot qui décide",
       p:"Soulignez-le. C'est ce mot-là que la personne qui corrige cherchera dans votre texte, et rien d'autre.",
       mots:[['Contenu, huit points','le mot est <b>distingue</b> : ce qu\'un document affirme, et ce que l\'équipe en pense'],
             ['Sources, quatre points','le mot est <b>nommée</b> : dans le texte et dans la bibliographie, avec sa date', true],
             ['Organisation, quatre points','le mot est <b>relient</b> : les idées se suivent, elles ne s\'empilent pas']],
       say:"Contenu : distingue. Sources : nommée. Organisation : relient.",
       note:"Un texte peut être juste, complet et bien écrit, et perdre huit points sur vingt parce qu'il ne distingue jamais le fait de l'opinion."},

      {t:'ana', h:"Où mettre son temps, selon le barème",
       p:"Les points ne sont pas répartis au hasard : ce qui vaut le plus est ce qui prend le plus de temps. Mais l'inverse est intéressant aussi.",
       mots:[['Ce qui coûte deux semaines','le contenu, huit points — lire, comprendre, comparer'],
             ['Ce qui coûte une heure','l\'organisation, quatre points — découper, aérer, relier', true],
             ['Le meilleur rendement','ces quatre points-là. Ils se gagnent le dernier soir et se perdent tout aussi vite']],
       say:"Le contenu coûte deux semaines. L'organisation coûte une heure, et vaut quatre points.",
       note:"Ce n'est pas un conseil pour travailler moins. C'est un conseil pour ne pas remettre un travail de deux semaines habillé en dix minutes."},

      {t:'ex', h:"Ce qui est évalué, ce qui ne l'est pas",
       p:"La deuxième colonne compte autant que la première.",
       rows:[
         ["Évalué : ce que disent les sources","Rapporté, avec la source nommée."],
         ["Évalué : la distinction fait / opinion","« La ville écrit que… » et non « il est prouvé que… »."],
         ["Évalué : la construction de la phrase","La phrase tient debout, les accords suivent, la ponctuation aussi."],
         ["Évalué : le découpage en paragraphes","Une idée par paragraphe, un blanc entre eux."],
         ["Jamais évalué : l'accent","Ni à l'oral, ni dans l'idée qu'on s'en fait."],
         ["Jamais évalué : la vitesse","Un exposé lent et clair vaut mieux qu'un exposé rapide."],
       ]},

      {t:'piege', h:"Trois erreurs de lecture d'une grille",
       rows:[
         ["croire que la note va à l'équipe","lire la phrase qui dit à qui va la note",
          "Dans cette grille-ci, la note est donnée à chaque personne selon la partie qu'elle a écrite et présentée. Ça change tout : personne n'a à porter le travail des deux autres, et personne ne coule à cause d'eux."],
         ["viser la longueur","viser le nombre d'idées",
          "Aucune ligne de la grille ne parle de longueur. Deux pages bien découpées valent plus que quatre pages où tout se suit sans blanc."],
         ["s'inquiéter de son accent","travailler ce qui est écrit dans la grille",
          "L'accent n'est évalué nulle part, à aucun niveau du programme. Cette inquiétude-là fait taire des adultes qui auraient beaucoup à dire, et elle ne repose sur rien."],
       ]},

      {t:'check', h:"Vérifions en trois questions",
       p:"Une seule bonne réponse chaque fois.",
       qs:[
         {q:"Quelle ligne vaut le plus de points ?", opts:["le contenu, huit points","l'organisation, quatre points"], ok:0,
          fb:"Huit sur vingt. C'est aussi la ligne qui demande le plus de temps."},
         {q:"Une source citée sans date…", opts:["compte quand même","ne compte pas"], ok:1,
          fb:"La grille le dit en toutes lettres. Notez la date pendant que vous lisez."},
         {q:"L'accent est-il évalué ?", opts:["non, ni à l'écrit ni à l'oral","oui, dans la ligne « langue »"], ok:0,
          fb:"La ligne « langue » évalue la phrase, les accords et la ponctuation. Rien d'autre."},
       ]},

      {t:'revoir', h:"À retenir",
       p:"Une grille se lit <b>avant</b> d'écrire. Chaque ligne contient un mot qui décide — <i>distingue</i>, <i>nommée</i>, <i>relient</i> — et le barème dit où mettre son temps. Ce qui n'y figure pas n'est pas évalué : ni l'accent, ni la vitesse, ni la longueur."},
    ]
  },

  t1ordre: {
    eye:'Mini-leçon', tit:"L'ordre des étapes quand rien ne dit « d'abord »",
    blocs:[
      {t:'texte', h:"Un texte qui range sans le dire",
       p:"Dans un mode d'emploi, tout est numéroté. Dans une consigne de travail, presque rien ne l'est : les étapes sont dans des phrases ordinaires, et l'ordre se cache dans des mots de deux syllabes qu'on lit sans les voir. Le programme du niveau 6 nomme précisément ce savoir : comprendre l'ordre des étapes d'une consigne à partir d'indices linguistiques autres que les connecteurs de temps.",
       note:"« D'abord », « ensuite », « enfin » sont les connecteurs de temps ordinaires. Ce sont ceux qu'on apprend au niveau 3, et ce sont ceux qui manquent ici."},

      {t:'ana', h:"Les quatre indices qui rangent",
       p:"Chacun place une action avant ou après une autre, sans jamais dire « premièrement ».",
       mots:[['une fois','ce qui suit est fini avant que le reste commence : une fois le sujet approuvé, cherchez'],
             ['avant de','le verbe qui suit vient en second, même s\'il est écrit en premier', true],
             ['dès que','non seulement « ensuite », mais « pas avant » : dès que vous avez trois sources'],
             ['sans avoir','une interdiction déguisée : ne commencez pas sans avoir lu la grille']],
       say:"une fois, avant de, dès que, sans avoir",
       note:"Ces quatre-là couvrent presque toutes les consignes que vous lirez, à l'école comme au travail."},

      {t:'ana', h:"Le piège de « avant de »",
       p:"C'est le seul des quatre qui inverse l'ordre de lecture, et c'est pour cela qu'il se manque.",
       mots:[['Ce qui est écrit en premier','« Avant de choisir… » — le verbe choisir arrive en premier dans la phrase'],
             ['Ce qui se fait en premier','lire la liste : c\'est la deuxième moitié de la phrase', true],
             ['La façon de vérifier','récrivez la phrase à l\'endroit : lisez la liste, puis choisissez']],
       say:"Avant de choisir, lisez la liste au complet. On lit d'abord, on choisit ensuite.",
       note:"Prenez l'habitude de récrire ces phrases à l'endroit sur votre feuille de plan. Une seule inversion, dans une consigne, décale tout le reste."},

      {t:'ex', h:"Six phrases, six ordres",
       p:"À gauche la phrase de la consigne, à droite ce qu'elle vous dit de faire en premier.",
       rows:[
         ["Une fois le sujet approuvé, cherchez trois sources.","Faire approuver le sujet."],
         ["Avant de choisir, lisez la liste au complet.","Lire la liste."],
         ["Dès que vous avez trois sources, écrivez le plan.","Trouver la troisième source."],
         ["Ne commencez pas à écrire sans avoir lu la grille.","Lire la grille."],
         ["Le texte se terminera par une bibliographie.","Rien encore : c'est la dernière partie."],
         ["L'équipe présentera ensuite son compte rendu.","Rien encore : l'oral vient après la remise."],
       ]},

      {t:'piege', h:"Trois façons de se tromper d'ordre",
       rows:[
         ["suivre l'ordre des phrases sur la page","suivre les indices, pas la mise en page",
          "Une consigne n'est pas toujours écrite dans l'ordre où les choses se font. Elle est écrite dans l'ordre où l'auteur y a pensé."],
         ["lire « avant de » comme « d'abord »","récrire la phrase à l'endroit",
          "« Avant de choisir, lisez » ne veut pas dire « choisissez d'abord ». C'est exactement le contraire, et l'erreur coûte une semaine de recherche sur un sujet qui sera refusé."],
         ["croire que « dès que » signifie seulement « ensuite »","entendre aussi le « pas avant »",
          "« Dès que vous avez trois sources » veut dire : deux ne suffisent pas. C'est une condition, pas seulement un moment."],
       ]},

      {t:'check', h:"Vérifions en trois questions",
       p:"Une seule bonne réponse chaque fois.",
       qs:[
         {q:"« Avant de choisir, lisez la liste. » Que fait-on en premier ?", opts:["choisir","lire la liste"], ok:1,
          fb:"Le verbe écrit en premier n'est pas l'action faite en premier. C'est le seul des quatre indices qui inverse."},
         {q:"« Dès que vous avez trois sources, écrivez le plan. » Avec deux sources ?", opts:["on peut commencer le plan","on n'écrit pas encore le plan"], ok:1,
          fb:"« Dès que » pose une condition : pas avant."},
         {q:"« Une fois le sujet approuvé, cherchez. » L'approbation arrive…", opts:["avant la recherche","après la recherche"], ok:0,
          fb:"Ce qui suit « une fois » est terminé avant que le reste commence."},
       ]},

      {t:'revoir', h:"À retenir",
       p:"Quatre indices rangent les étapes sans dire « d'abord » : <b>une fois</b> (fini avant), <b>avant de</b> (inverse l'ordre de lecture), <b>dès que</b> (pas avant), <b>sans avoir</b> (interdiction déguisée). Récrivez chaque phrase à l'endroit sur votre feuille de plan."},
    ]
  },

  t1inf: {
    eye:'Mini-leçon', tit:"De, à, ou rien : le verbe qui en appelle un autre",
    blocs:[
      {t:'texte', h:"Deux verbes, et un petit mot entre les deux",
       p:"« Elle demande de remettre le plan. » « Ils ont réussi à trouver une source. » « Ils espèrent finir. » Trois phrases de la même forme : un verbe conjugué, puis un verbe à l'infinitif. Ce qui change entre les trois, c'est ce qu'il y a au milieu — « de », « à », ou rien du tout. Et ce choix ne s'explique pas : il appartient au premier verbe, comme sa couleur.",
       note:"Le programme les appelle des subordonnées infinitives. Le nom importe peu ; ce qui compte, c'est de savoir à quelle famille appartient chaque verbe."},

      {t:'ana', h:"La famille « de »",
       p:"La plus nombreuse. Les verbes qui demandent, qui décident et qui oublient.",
       mots:[['Les huit à connaître','demander · oublier · choisir · décider · accepter · éviter · permettre · essayer'],
             ['La forme','de, ou d\' devant une voyelle : il a oublié d\'écrire son nom', true],
             ['Un exemple de la consigne','elle demande de remettre le plan en même temps que le texte']],
       say:"demander, oublier, choisir, décider, accepter, éviter, permettre, essayer",
       note:"Astuce : ces verbes-là parlent presque tous d'une décision ou d'un manque. Ce n'est pas une règle, mais ça aide à se souvenir."},

      {t:'ana', h:"La famille « à »",
       p:"Les verbes du mouvement et de l'apprentissage : quelque chose se met en marche ou s'apprend.",
       mots:[['Les sept à connaître','réussir · apprendre · commencer · aider · hésiter · arriver · se mettre'],
             ['La forme','à ne change jamais, même devant une voyelle : ils ont commencé à écrire', true],
             ['Un exemple du module','Marisol a appris à juger une source en deux questions']],
       say:"réussir, apprendre, commencer, aider, hésiter, arriver, se mettre",
       note:"« Commencer à » est le plus fréquent des sept. Si vous n'en retenez qu'un, retenez celui-là."},

      {t:'ana', h:"La famille qui ne veut rien",
       p:"Les plus courants de la langue, et ceux où l'erreur s'entend le plus.",
       mots:[['Les huit à connaître','espérer · vouloir · pouvoir · devoir · savoir · aimer · préférer · aller'],
             ['La forme','rien du tout : ils espèrent finir avant le 24 novembre', true],
             ['La faute à éviter','ils espèrent de finir — jamais, dans aucun contexte']],
       say:"espérer, vouloir, pouvoir, devoir, savoir, aimer, préférer, aller",
       note:"Ces huit verbes reviennent dans presque toutes vos phrases. Les fixer une fois règle la moitié du problème pour de bon."},

      {t:'ex', h:"Huit phrases du module",
       p:"À gauche la phrase, à droite ce qui explique le choix.",
       rows:[
         ["Elle demande de remettre le plan.","demander → famille « de »."],
         ["Il a oublié d'écrire son nom.","oublier → « de », devenu « d' » devant la voyelle."],
         ["Ils ont réussi à trouver une source.","réussir → famille « à »."],
         ["Marisol a appris à juger une source.","apprendre → famille « à »."],
         ["Ils ont choisi de garder le bac brun.","choisir → famille « de »."],
         ["Ils espèrent finir avant le 24.","espérer → rien du tout."],
         ["Ils voudraient écrire leur plan ce soir.","vouloir → rien du tout."],
         ["Ils ont commencé à écrire le lundi soir.","commencer → famille « à »."],
       ]},

      {t:'piege', h:"Trois pièges",
       rows:[
         ["ajouter « de » après vouloir ou espérer","apprendre les huit verbes qui ne veulent rien",
          "« Je veux de partir » s'entend souvent, et c'est la faute la plus repérable de toutes, parce que ces verbes-là reviennent à chaque phrase."],
         ["chercher une logique","apprendre le verbe avec sa préposition",
          "Pourquoi « commencer à » et « décider de » ? Il n'y a pas de réponse. On n'apprend pas la règle, on apprend le verbe et sa préposition ensemble, comme on apprend le genre d'un nom."],
         ["oublier l'apostrophe de « de »","dire la phrase à voix haute",
          "« De écrire » ne se prononce pas : la bouche le refuse avant que l'œil le voie. Dire la phrase règle la question à tous les coups."],
       ]},

      {t:'check', h:"Vérifions en quatre questions",
       p:"Une seule bonne réponse chaque fois.",
       qs:[
         {q:"Ils ont réussi ___ trouver une source.", opts:["de","à"], ok:1,
          fb:"réussir appartient à la famille « à », comme commencer et apprendre."},
         {q:"Ils espèrent ___ finir avant le 24.", opts:["rien du tout","de"], ok:0,
          fb:"espérer ne veut aucune préposition, comme vouloir, pouvoir et devoir."},
         {q:"Elle a oublié ___ écrire son nom.", opts:["de","d'"], ok:1,
          fb:"Devant une voyelle, « de » devient « d' ». La bouche le fait toute seule."},
         {q:"Ils ont décidé ___ garder le sujet.", opts:["de","à"], ok:0,
          fb:"décider appartient à la famille « de », avec demander, choisir et accepter."},
       ]},

      {t:'revoir', h:"À retenir",
       p:"Trois familles, apprises avec le verbe : <b>de</b> (demander, oublier, choisir, décider, accepter, éviter, permettre, essayer), <b>à</b> (réussir, apprendre, commencer, aider, hésiter, arriver, se mettre), <b>rien</b> (espérer, vouloir, pouvoir, devoir, savoir, aimer, préférer, aller). En cas de doute, remplacez l'infinitif par « quelque chose »."},
    ]
  },

  t1imper: {
    eye:'Mini-leçon', tit:"Donne-le-moi",
    blocs:[
      {t:'texte', h:"La phrase la plus utile entre camarades",
       p:"Dans une équipe, on se demande des choses vingt fois par jour : le plan, la feuille, les trois sources, la date. Sans la forme courte, on tourne autour — « est-ce que tu pourrais peut-être me le donner ». Avec elle, une demande tient en trois mots collés : <b>donne-le-moi</b>. Ce n'est ni sec ni impoli : c'est ce que les gens disent réellement.",
       note:"Le programme du niveau 6 le formule ainsi : employer des phrases impératives avec combinaison de pronoms, le / la / les + moi / nous."},

      {t:'ana', h:"L'ordre ne bouge jamais",
       p:"Le verbe, puis la chose, puis la personne. Trois morceaux, deux traits d'union, toujours dans cet ordre.",
       mots:[['Le verbe à l\'impératif','donne · montre · rends · envoie · explique · redis'],
             ['La chose','le · la · les — selon ce dont on parle', true],
             ['La personne','moi · nous — jamais « me » ni « te » ici']],
       say:"Donne-le-moi. Montre-les-moi. Envoyez-la-nous.",
       note:"« Donne-moi-le » se dit dans certaines régions, mais ce n'est pas ce que le programme demande ni ce que vous lirez : la chose passe toujours avant la personne."},

      {t:'ana', h:"Le « s » qui disparaît, et qui ne revient pas",
       p:"Un verbe en -er perd son « s » à l'impératif. C'est une règle qu'on connaît déjà ; ce qui trompe, c'est de croire qu'il revient quand un pronom suit.",
       mots:[['La forme seule','donne · montre · envoie — sans s'],
             ['La forme avec pronoms','donne-le-moi · montre-les-nous — toujours sans s', true],
             ['Les verbes des autres groupes','rends-le-moi · redis-la-moi — le s appartient au verbe, il reste']],
       say:"Donne-le-moi. Rends-le-moi. Redis-la-moi.",
       note:"Le « s » qu'on ajoute parfois (« vas-y », « donnes-en ») n'apparaît que devant « y » et « en ». Ce n'est pas notre cas ici."},

      {t:'ex', h:"Six demandes de tous les jours",
       p:"À gauche la façon longue, à droite la façon courte.",
       rows:[
         ["Tu dois me remettre le plan.","Remets-le-moi."],
         ["Tu dois me montrer les sources.","Montre-les-moi."],
         ["Vous devez nous envoyer la grille.","Envoyez-la-nous."],
         ["Tu dois me rendre le cahier.","Rends-le-moi."],
         ["Vous devez nous expliquer les étapes.","Expliquez-les-nous."],
         ["Tu dois me redire la date.","Redis-la-moi."],
       ]},

      {t:'piege', h:"Trois pièges",
       rows:[
         ["mettre la personne avant la chose","garder l'ordre chose, puis personne",
          "« Donne-moi-le » se dit ici et là, mais la forme écrite et enseignée est « donne-le-moi ». Dans un travail écrit, l'autre forme sera corrigée."],
         ["remettre le s du verbe en -er","laisser le verbe tel quel",
          "« Donnes-le-moi » n'existe pas. Le s ne revient que devant « y » et « en » : vas-y, donnes-en."],
         ["employer la même forme à la négative","apprendre les deux séparément",
          "À la négative, tout change de place : « Ne me le donne pas. » Les pronoms repassent devant le verbe et l'ordre s'inverse. N'essayez pas de relier les deux formes : apprenez-les comme deux phrases différentes."],
       ]},

      {t:'check', h:"Vérifions en trois questions",
       p:"Une seule bonne réponse chaque fois.",
       qs:[
         {q:"Comment demander le plan, à quelqu'un qu'on tutoie ?", opts:["Donne-moi-le.","Donne-le-moi."], ok:1,
          fb:"La chose d'abord, la personne ensuite. C'est l'ordre à retenir."},
         {q:"Comment demander la grille, pour deux personnes, en vouvoyant ?", opts:["Envoyez-la-nous.","Envoyez-nous-la."], ok:0,
          fb:"Même ordre : la chose, puis la personne."},
         {q:"À la forme négative, où vont les pronoms ?", opts:["derrière le verbe","devant le verbe"], ok:1,
          fb:"« Ne me le donne pas. » L'ordre s'inverse aussi : la personne repasse devant la chose."},
       ]},

      {t:'revoir', h:"À retenir",
       p:"<b>Verbe, chose, personne</b>, reliés par des traits d'union : donne<b>-le-moi</b>, montre<b>-les-nous</b>. Le verbe en -er garde sa forme sans « s ». À la négative, tout repasse devant : ne me le donne pas."},
    ]
  },

  t2src: {
    eye:'Mini-leçon', tit:"Lire un texte suivi sans perdre le fil",
    blocs:[
      {t:'texte', h:"Ce que le niveau 6 vous demande vraiment",
       p:"Jusqu'ici, on vous demandait de comprendre des phrases. À partir d'ici, on vous demande de suivre un texte : de savoir, à la quatrième phrase, de quoi parlait la deuxième. C'est un autre travail, et il ne s'obtient pas en connaissant plus de mots. Il s'obtient en repérant ce qui relie les phrases entre elles.",
       note:"Le pilote du niveau 6 l'a écrit en une ligne, et elle vaut pour les huit modules du niveau : le 5 raconte, le 7 démasque, le 6 suit un fil."},

      {t:'ana', h:"Trois questions à poser à un document, avant de le lire",
       p:"Trente secondes, et elles changent tout ce que vous lirez ensuite.",
       mots:[['Qui parle ?','une ville, un journal, une personne — ce n\'est jamais « Internet »'],
             ['Qu\'est-ce que cette personne veut ?','informer, convaincre, se défendre, vendre', true],
             ['De quand ça date ?','une page de 2019 sur une collecte qui a changé en 2023 dit des choses fausses sans mentir']],
       say:"Qui parle ? Qu'est-ce que cette personne veut ? De quand ça date ?",
       note:"Ces trois questions sont exactement celles que madame Ouimet pose à l'équipe, une fois par document. Elles ne changent jamais."},

      {t:'ana', h:"Ce qui relie les phrases, et qu'il faut voir",
       p:"Un texte tient par quatre sortes de fils. Les reconnaître, c'est cesser de relire trois fois le même paragraphe.",
       mots:[['Les pronoms','le, en, y, celui, celle — ils renvoient à quelque chose de déjà dit'],
             ['Les reprises par un nom','« cette distribution », « ce ramassage » — le nom résume la phrase d\'avant', true],
             ['Les connecteurs','par exemple, c\'est-à-dire, notamment, en revanche'],
             ['Les temps','un plus-que-parfait recule d\'un cran, un passé simple raconte le décor']],
       say:"Les pronoms, les reprises par un nom, les connecteurs, les temps.",
       note:"Ce sont les quatre savoirs de grammaire du texte que le niveau 6 travaille. Ils ne servent à rien d'autre qu'à ça : tenir un texte du début à la fin."},

      {t:'ex', h:"Comment lire une page d'information",
       p:"Dans cet ordre, et pas dans un autre.",
       rows:[
         ["Le titre et l'en-tête","Qui publie. Une ville ne parle jamais au nom d'un journal, et l'inverse non plus."],
         ["La date","Elle décide de ce que vaut le reste."],
         ["Les intertitres","Ils donnent le plan du document en dix secondes."],
         ["Le premier mot de chaque paragraphe","Souvent un connecteur : il dit ce que le paragraphe fait."],
         ["Ce qui est en gras ou encadré","La condition, le chiffre, l'interdiction."],
         ["Le reste, une fois seulement","Vous savez déjà où vous allez : la lecture est deux fois plus rapide."],
       ]},

      {t:'piege', h:"Trois pièges de lecture",
       rows:[
         ["lire du début à la fin, une fois, lentement","regarder d'abord, lire ensuite",
          "Une lecture linéaire d'une page dense laisse une impression et aucune information précise. Trente secondes de repérage rendent la lecture deux fois plus efficace."],
         ["confondre ce que le texte dit et ce qu'on en pense","souligner les deux d'une couleur différente",
          "C'est exactement ce que la ligne « contenu » de la grille regarde, et ça vaut huit points sur vingt. Un travail qui écrit « il est prouvé que » là où sa source écrivait « selon nous » perd ces points-là."],
         ["citer une page sans noter sa date","tout noter pendant la lecture",
          "Retrouver la date trois jours plus tard prend plus de temps que de l'avoir écrite, et une source sans date ne compte pas dans cette grille."],
       ]},

      {t:'check', h:"Vérifions en trois questions",
       p:"Une seule bonne réponse chaque fois.",
       qs:[
         {q:"Que fait-on avant de lire une page d'information ?", opts:["on la lit au complet","on regarde qui publie, la date et les intertitres"], ok:1,
          fb:"Trente secondes de repérage, et la lecture devient deux fois plus rapide."},
         {q:"« Internet » est-il une source ?", opts:["non : une source a un auteur et une date","oui, si la page existe encore"], ok:0,
          fb:"Une source, c'est un document précis, avec qui l'a publié et quand."},
         {q:"Qu'est-ce qui tient un texte suivi ?", opts:["le vocabulaire","les pronoms, les reprises, les connecteurs et les temps"], ok:1,
          fb:"Ce sont les quatre fils du niveau 6. Le vocabulaire, lui, se cherche au dictionnaire."},
       ]},

      {t:'revoir', h:"À retenir",
       p:"Avant de lire : <b>qui parle</b>, <b>ce qu'il veut</b>, <b>de quand ça date</b>. Pendant la lecture : les <b>pronoms</b>, les <b>reprises par un nom</b>, les <b>connecteurs</b> et les <b>temps</b>. Ce sont eux qui relient les phrases, et les suivre, c'est ça, comprendre un texte."},
    ]
  },

  t2repr: {
    eye:'Mini-leçon', tit:"Ce que remplacent le, en et y",
    blocs:[
      {t:'texte', h:"Un accident de lecture, pas un détail de grammaire",
       p:"« La ville affirme que le plastique est refusé. Youssef ne le croit pas. » Si vous ne voyez pas ce que « le » remplace, vous croirez que Youssef ne croit pas la ville en général — alors qu'il ne croit pas cette phrase-là. Dans un travail de recherche, ce genre d'erreur ne se voit pas : on écrit tranquillement le contraire de sa source, et la correctrice, elle, le voit tout de suite.",
       note:"C'est le savoir le plus caractéristique du niveau 6, et celui qui distingue vraiment ce niveau du 3 et du 5."},

      {t:'ana', h:"« le » ramasse une phrase entière",
       p:"Il ne désigne pas un objet : il désigne ce qui vient d'être dit. C'est pour ça qu'il ne s'accorde jamais.",
       mots:[['Ce qu\'il remplace','une phrase complète, souvent introduite par « que »'],
             ['Un exemple','Elle pense que la collecte fonctionne. → Elle <b>le</b> pense.', true],
             ['Devant une voyelle','il devient l\' : elle <b>l\'</b>avait dit deux fois']],
       say:"Elle pense que la collecte fonctionne. Elle le pense.",
       note:"Ce « le »-là ne devient jamais « la » ni « les », même si la phrase parle d'une femme ou de plusieurs choses. Il n'a pas de genre parce qu'une phrase n'en a pas."},

      {t:'ana', h:"« en » reprend ce qui suit « de », et les quantités",
       p:"Deux emplois, et le second est le plus fréquent dans un texte d'information.",
       mots:[['Après un groupe en « de »','Ils ont besoin d\'une source. → Ils <b>en</b> ont besoin.'],
             ['Après une quantité','Le bulletin donne trois chiffres. Nous <b>en</b> gardons un seul.', true],
             ['Pour une personne, c\'est autre chose','Il parle de sa coéquipière. → Il parle <b>d\'elle</b>.']],
       say:"Ils ont besoin d'une source. Ils en ont besoin.",
       note:"Devant une quantité, « en » est presque toujours obligatoire en français, là où beaucoup de langues le laissent tomber. « J'en veux deux », jamais « je veux deux »."},

      {t:'ana', h:"« y » reprend ce qui suit « à », et les lieux",
       p:"Le plus facile des trois à repérer, parce qu'il est court et qu'il se place toujours juste avant le verbe.",
       mots:[['Après un groupe en « à »','Elle pense à son exposé. → Elle <b>y</b> pense.'],
             ['Pour un lieu','Elle va à la bibliothèque. → Elle <b>y</b> va.', true],
             ['Dans un texte écrit','L\'équipe met ses sources dans la bibliographie. → Elle <b>y</b> met ses sources.']],
       say:"Elle pense à son exposé. Elle y pense.",
       note:"« y » ne s'emploie pas pour une personne : on ne dit pas « j'y pense » en parlant de quelqu'un, mais « je pense à elle »."},

      {t:'ex', h:"Sept renvois du module",
       p:"À gauche la phrase, à droite ce que le petit mot remplace.",
       rows:[
         ["Le bulletin donne trois chiffres. Nous n'en avons gardé qu'un.","des trois chiffres du bulletin"],
         ["La lectrice croit que la collecte ne sert à rien. Youssef ne le croit pas.","que la collecte ne sert à rien"],
         ["Marisol travaille à la bibliothèque. Elle y passe ses jeudis.","à la bibliothèque"],
         ["Le texte finit par une bibliographie. L'équipe y met ses sources.","dans la bibliographie"],
         ["Il leur manque une source. Ils en cherchent une depuis lundi.","une source"],
         ["L'enseignante a dit que le retard ne se discute pas. Elle l'a répété.","que le retard ne se discute pas"],
         ["Le plan est resté sur la table. Youssef l'a oublié là.","le plan"],
       ]},

      {t:'piege', h:"Trois pièges",
       rows:[
         ["passer par-dessus sans s'arrêter","reculer d'une phrase, chaque fois",
          "Ces mots font deux lettres et ne se prononcent presque pas. C'est justement pour ça qu'on les saute — et qu'on perd le fil sans le sentir."],
         ["accorder le « le » de la phrase reprise","le laisser tel quel, toujours",
          "« Elle la pense » en parlant d'une idée : non. Une phrase n'a pas de genre, et ce « le »-là ne change jamais."],
         ["employer « y » pour une personne","garder la préposition et le pronom disjoint",
          "« J'y pense » en parlant de sa coéquipière ne se dit pas. C'est « je pense à elle ». Même chose avec « en » : « je parle d'elle », pas « j'en parle »."],
       ]},

      {t:'check', h:"Vérifions en quatre questions",
       p:"Une seule bonne réponse chaque fois.",
       qs:[
         {q:"« Elle pense que le plan est bon. Elle ___ pense. »", opts:["le","y"], ok:0,
          fb:"« le » ramasse toute la phrase qui suit « que »."},
         {q:"« Ils ont besoin d'une source. Ils ___ ont besoin. »", opts:["y","en"], ok:1,
          fb:"« en » reprend ce qui suivait « de »."},
         {q:"« Elle va à la bibliothèque. Elle ___ va. »", opts:["y","en"], ok:0,
          fb:"« y » reprend un lieu, et ce qui suivait « à »."},
         {q:"Le « le » d'une phrase reprise s'accorde-t-il ?", opts:["jamais","au féminin si la phrase parle d'une femme"], ok:0,
          fb:"Une phrase n'a ni genre ni nombre. Ce « le » ne bouge pas."},
       ]},

      {t:'revoir', h:"À retenir",
       p:"<b>le</b> ramasse une phrase entière et ne s'accorde jamais. <b>en</b> reprend ce qui suivait « de », et les quantités. <b>y</b> reprend ce qui suivait « à », et les lieux. Ni « en » ni « y » ne s'emploient pour une personne. À chaque fois : reculez d'une phrase et demandez-vous ce que ça remplace."},
    ]
  },

  t2ou: {
    eye:'Mini-leçon', tit:"Où : un lieu, mais aussi un moment",
    blocs:[
      {t:'texte', h:"La surprise du niveau 6",
       p:"On apprend « où » très tôt, comme le mot du lieu : la ville où j'habite, la page où je l'ai lu. Ce que presque personne n'apprend, c'est qu'il sert aussi pour le temps : l'année où, le jour où, le moment où. Dans les autres langues, ce sont deux mots différents — et c'est exactement pour ça que celui-ci se manque, même après des années de français.",
       note:"Le programme le formule ainsi : employer des phrases subordonnées relatives avec le pronom relatif où, complément de lieu ou de temps."},

      {t:'ana', h:"Le « où » de lieu",
       p:"Celui qu'on connaît. Il accroche une phrase entière à un nom d'endroit.",
       mots:[['La forme','nom d\'endroit + où + une phrase complète'],
             ['Un exemple','Voici la page <b>où</b> il a trouvé la liste.', true],
             ['Ce qu\'il évite','Voici la page. Il a trouvé la liste dans cette page. — deux phrases, une répétition']],
       say:"Voici la page où il a trouvé la liste.",
       note:"Le nom d'endroit peut être un vrai lieu (la ville, la bibliothèque) ou une place dans un document (la page, le paragraphe, le tableau)."},

      {t:'ana', h:"Le « où » de temps",
       p:"Le même mot, un autre travail. Il s'accroche à un nom de moment, jamais à un verbe.",
       mots:[['Les noms qui l\'appellent','l\'année · le jour · le moment · la semaine · l\'époque · la fois'],
             ['Un exemple','C\'est l\'année <b>où</b> le conseil a adopté le règlement.', true],
             ['La faute fréquente','« l\'année que le conseil a adopté » — on entend « que », c\'est « où »']],
       say:"C'est l'année où le conseil a adopté le règlement.",
       note:"Le test est simple : si le mot juste avant est un nom de temps, c'est « où ». Il n'y a pas d'exception à retenir."},

      {t:'ana', h:"Qui, que, où : lequel des trois",
       p:"Une seule question à poser, et elle porte sur ce qui manque après le mot.",
       mots:[['Il manque le sujet du verbe','une lectrice <b>qui</b> écrit souvent'],
             ['Il manque le complément direct','la page <b>qu\'</b>il a trouvée', true],
             ['Il ne manque rien, et le nom est un lieu ou un moment','la page <b>où</b> il a trouvé la liste']],
       say:"une lectrice qui écrit souvent, la page qu'il a trouvée, la page où il a trouvé la liste",
       note:"La même phrase peut prendre les trois, et parler de trois choses différentes. C'est le seul point de cette leçon qui demande de la lenteur."},

      {t:'ex', h:"Huit phrases, trois mots",
       p:"À gauche la phrase, à droite ce qui explique le choix.",
       rows:[
         ["l'année où le conseil a adopté le règlement","« l'année » est un nom de temps."],
         ["la page où il a trouvé la liste","« la page » est un endroit du document."],
         ["la page qu'elle a trouvée en premier","il manque le complément direct de « trouver »."],
         ["une lectrice qui écrit souvent","il manque le sujet de « écrit »."],
         ["le jour où ils ont remis leur plan","« le jour » est un nom de temps."],
         ["la ville où Marisol habite","« la ville » est un lieu."],
         ["le tableau qu'ils ont recopié","il manque le complément direct de « recopier »."],
         ["le moment où une équipe se perd","« le moment » est un nom de temps."],
       ]},

      {t:'piege', h:"Trois pièges",
       rows:[
         ["dire « l'année que »","dire « l'année où »",
          "C'est la faute la plus fréquente du niveau, et elle s'entend même chez des gens qui parlent très bien. Un nom de temps appelle « où »."],
         ["confondre où et ou","regarder l'accent",
          "« ou » sans accent veut dire « ou bien ». « où » avec accent est celui de cette leçon. À l'écrit, l'accent est la seule différence, et il compte dans la ligne « langue » de la grille."],
         ["couper la phrase en deux pour éviter le problème","garder la phrase longue",
          "Trois phrases courtes qui répètent le même nom se lisent moins bien qu'une phrase tenue. La grille appelle ça l'organisation, et c'est là que ces quatre points se gagnent."],
       ]},

      {t:'check', h:"Vérifions en quatre questions",
       p:"Une seule bonne réponse chaque fois.",
       qs:[
         {q:"« C'est l'année ___ le règlement a été adopté. »", opts:["que","où"], ok:1,
          fb:"« l'année » est un nom de temps : c'est « où »."},
         {q:"« Voici la page ___ elle a trouvée en premier. »", opts:["qu'","où"], ok:0,
          fb:"Il manque le complément direct de « trouver » : c'est « que », devenu « qu' »."},
         {q:"« Une lectrice ___ écrit souvent au bulletin. »", opts:["que","qui"], ok:1,
          fb:"Il manque le sujet du verbe « écrit »."},
         {q:"« ou » sans accent veut dire…", opts:["ou bien","à quel endroit"], ok:0,
          fb:"L'accent est la seule différence à l'écrit, et il change complètement le sens."},
       ]},

      {t:'revoir', h:"À retenir",
       p:"<b>où</b> accroche une phrase à un nom de <b>lieu</b> (la page où, la ville où) ou de <b>temps</b> (l'année où, le jour où, le moment où). Pour choisir entre qui, que et où : regardez ce qui manque après le mot — le sujet, le complément direct, ou rien."},
    ]
  },

  t2subst: {
    eye:'Mini-leçon', tit:"Reprendre sans répéter",
    blocs:[
      {t:'texte', h:"Ce qui sépare un texte d'une liste",
       p:"Lisez deux paragraphes qui commencent tous les deux par « la collecte des matières organiques ». Ça se lit comme une liste : chaque paragraphe repart de zéro, rien ne monte. Maintenant, remplacez le deuxième par « ce ramassage ». Le texte avance. C'est tout l'écart entre un travail qui obtient ses quatre points d'organisation et un travail qui les perd.",
       note:"Le programme l'appelle : employer des procédés de substitution lexicale pour reprendre un référent — synonymie, nominalisation, et le reste."},

      {t:'ana', h:"Fabriquer un nom à partir d'un verbe",
       p:"C'est le procédé le plus utile, et il tient dans cinq suffixes.",
       mots:[['-tion et -sion','distribuer → la distribution · décider → la décision'],
             ['-age','ramasser → le ramassage · trier → le triage', true],
             ['-ment','traiter → le traitement · enfouir → l\'enfouissement'],
             ['-ure et le nom nu','ouvrir → l\'ouverture · se plaindre → une plainte']],
       say:"la distribution, la décision, le ramassage, le traitement, l'enfouissement",
       note:"Aucun de ces suffixes ne se devine. Quand vous rencontrez un verbe utile dans une source, notez son nom en même temps : ça se fait en trois secondes et ça sert toute la session."},

      {t:'ana', h:"Le déterminant qui fait le lien",
       p:"Le nom seul ne suffit pas : il faut dire au lecteur qu'il s'agit de ce dont on vient de parler.",
       mots:[['Avec « ce, cette, ces »','Les gens se sont plaints. <b>Ces</b> plaintes ont duré un an.'],
             ['Sans déterminant démonstratif','Les gens se sont plaints. Des plaintes ont duré un an. — le lecteur croit qu\'on parle d\'autre chose', true],
             ['Le possessif fait le même travail','La ville a lancé la collecte. <b>Son</b> premier hiver fut difficile.']],
       say:"Les gens se sont plaints. Ces plaintes ont duré un an.",
       note:"C'est le mot le plus court de la phrase qui fait tout le travail de liaison. Le retirer suffit à casser le fil."},

      {t:'ana', h:"L'autre procédé : le synonyme",
       p:"Plus simple, et parfois plus juste : on change de mot sans changer de chose.",
       mots:[['la collecte','le ramassage'],
             ['un document','une source, un écrit, une page', true],
             ['une échéance','une date limite, un délai']],
       say:"la collecte, le ramassage, un document, une source, une échéance, une date limite",
       note:"Un synonyme n'est jamais parfaitement égal. « Ramassage » est plus concret que « collecte » ; choisissez celui qui dit le mieux ce que vous voulez dire, pas seulement celui qui évite la répétition."},

      {t:'ex', h:"Sept reprises du dossier",
       p:"À gauche la phrase, à droite la façon de la reprendre.",
       rows:[
         ["On enfouit les matières organiques.","l'enfouissement des matières organiques"],
         ["La ville a distribué les bacs au printemps.","cette distribution du printemps"],
         ["Le camion ramasse le bac chaque semaine.","ce ramassage hebdomadaire"],
         ["Les habitants se sont plaints de l'odeur.","ces plaintes au sujet de l'odeur"],
         ["On traite les résidus dans une usine.","le traitement des résidus"],
         ["Le conseil a décidé de garder la collecte.","cette décision du conseil"],
         ["Beaucoup de gens trient mal leurs déchets.","le mauvais tri des déchets"],
       ]},

      {t:'piege', h:"Trois pièges",
       rows:[
         ["répéter le nom complet à chaque paragraphe","reprendre avec ce, cette, ces",
          "« La collecte des matières organiques » trois fois en une page se remarque immédiatement, et le texte donne l'impression de tourner en rond."],
         ["changer de mot sans prévenir","garder le démonstratif",
          "Passer de « la collecte » à « le ramassage » sans « ce » devant fait croire au lecteur qu'on parle d'autre chose. Un seul mot manquant, et le fil casse."],
         ["chercher un synonyme à tout prix","répéter plutôt que de dire faux",
          "Un mot précis répété vaut mieux qu'un synonyme approximatif. « Biométhanisation » n'a pas de synonyme, et personne ne vous reprochera de l'écrire deux fois."],
       ]},

      {t:'check', h:"Vérifions en trois questions",
       p:"Une seule bonne réponse chaque fois.",
       qs:[
         {q:"« On enfouit les matières. » Le nom correspondant est…", opts:["l'enfouissement","l'enfouissage"], ok:0,
          fb:"Suffixe -ment. Il ne se devine pas : il se note en même temps que le verbe."},
         {q:"Que faut-il devant le nom de reprise ?", opts:["un démonstratif : ce, cette, ces","un article : un, une, des"], ok:0,
          fb:"« Ces plaintes » renvoie à ce qui vient d'être dit ; « des plaintes » parle d'autre chose."},
         {q:"Un mot précis sans synonyme, comme « biométhanisation »…", opts:["se remplace par un mot approchant","se répète sans gêne"], ok:1,
          fb:"Un synonyme approximatif fait plus de dégâts qu'une répétition."},
       ]},

      {t:'revoir', h:"À retenir",
       p:"Pour reprendre sans répéter : fabriquez un <b>nom</b> à partir du verbe (-tion, -age, -ment, -sion, -ure) et posez devant un <b>démonstratif</b> — ce, cette, ces. Ou bien changez de mot, à condition qu'il dise vraiment la même chose."},
    ]
  },

  t2ps: {
    eye:'Mini-leçon', tit:"Le passé simple, à reconnaître et à traduire",
    blocs:[
      {t:'texte', h:"Un temps que personne ne parle",
       p:"Le bulletin municipal raconte les débuts de la collecte : « le conseil adopta le règlement », « les premiers bacs arrivèrent en avril ». Aucun Québécois ne dit ça à voix haute. Aucun courriel ne s'écrit comme ça. Et pourtant, dès qu'un texte raconte une histoire — l'historique d'une ville, la vie d'une entreprise, un roman —, ce temps apparaît et il faut le lire sans ralentir.",
       note:"Le programme demande deux choses seulement : reconnaître les verbes courants à la troisième personne, et associer le passé simple au passé composé. Rien de plus, et surtout pas d'en produire."},

      {t:'ana', h:"Les terminaisons à reconnaître",
       p:"Trois séries. Vous n'avez pas à savoir laquelle appartient à quel verbe : il suffit de les reconnaître au passage.",
       mots:[['Verbes en -er : -a et -èrent','il adopta · ils adoptèrent · elle arriva · elles arrivèrent'],
             ['Beaucoup d\'autres : -it et -irent','elle partit · elles partirent · il choisit · ils choisirent', true],
             ['Un troisième groupe : -ut et -urent','il disparut · ils disparurent · il reçut · ils reçurent']],
       say:"il adopta, ils adoptèrent, elle partit, elles partirent, il disparut, ils disparurent",
       note:"Attention à « il choisit » et « il finit » : au passé simple, ils s'écrivent exactement comme au présent. C'est le contexte qui tranche, et le contexte est toujours un récit."},

      {t:'ana', h:"Les trois formes qui reviennent partout",
       p:"Elles sont si courtes qu'on ne les reconnaît pas comme des verbes, et elles se rencontrent à toutes les pages d'un historique.",
       mots:[['il fut','il a été — ce fut la première collecte de la région'],
             ['il eut','il a eu — il y eut deux années difficiles', true],
             ['il fit','il a fait — la ville fit imprimer un dépliant']],
       say:"il fut, il a été. Il eut, il a eu. Il fit, il a fait.",
       note:"Apprenez ces trois-là et vous comprendrez la moitié des textes historiques que vous rencontrerez, en français comme dans une brochure de musée."},

      {t:'ex', h:"Sept phrases du bulletin municipal",
       p:"À gauche ce qui est écrit, à droite ce qu'on dirait.",
       rows:[
         ["le conseil adopta le règlement","le conseil a adopté le règlement"],
         ["les premiers bacs arrivèrent en avril","les premiers bacs sont arrivés en avril"],
         ["la collecte ne commença qu'en juin","la collecte n'a commencé qu'en juin"],
         ["la ville choisit la biométhanisation","la ville a choisi la biométhanisation"],
         ["il y eut deux années difficiles","il y a eu deux années difficiles"],
         ["les plaintes disparurent peu à peu","les plaintes ont disparu peu à peu"],
         ["on installa un point de dépôt","on a installé un point de dépôt"],
       ]},

      {t:'piege', h:"Trois pièges",
       rows:[
         ["essayer d'en écrire dans son travail","écrire au passé composé, toujours",
          "Un passé simple mal formé se voit à trois mètres et n'apporte aucun point. La grille demande une langue juste, pas une langue ancienne."],
         ["s'arrêter sur chaque forme inconnue","traduire dans sa tête et continuer",
          "Dans un document, le passé simple porte le décor, jamais l'information dont vous avez besoin. Ralentir dessus fait perdre le fil du paragraphe."],
         ["confondre « il choisit » présent et passé simple","regarder autour",
          "Les deux s'écrivent pareil pour certains verbes. Si le paragraphe raconte une histoire avec des dates, c'est du passé simple. C'est le seul test, et il suffit."],
       ]},

      {t:'check', h:"Vérifions en trois questions",
       p:"Une seule bonne réponse chaque fois.",
       qs:[
         {q:"« Le conseil adopta » se dit…", opts:["le conseil a adopté","le conseil adoptera"], ok:0,
          fb:"Terminaison -a : un verbe en -er, à la troisième personne du singulier, au passé."},
         {q:"« Il y eut » veut dire…", opts:["il y a","il y a eu"], ok:1,
          fb:"C'est le passé simple de « avoir ». Une des trois formes à connaître par cœur."},
         {q:"Faut-il savoir écrire au passé simple ?", opts:["non : seulement le reconnaître","oui, pour les travaux écrits"], ok:0,
          fb:"Le programme demande de le reconnaître et de l'associer au passé composé. Rien d'autre."},
       ]},

      {t:'revoir', h:"À retenir",
       p:"Trois séries de terminaisons — <b>-a / -èrent</b>, <b>-it / -irent</b>, <b>-ut / -urent</b> — et trois formes par cœur : <b>il fut</b>, <b>il eut</b>, <b>il fit</b>. On le traduit en passé composé dans sa tête et on continue à lire. On ne l'écrit jamais soi-même."},
    ]
  },

  t2avant: {
    eye:'Mini-leçon', tit:"Le plus-que-parfait, ou le passé du passé",
    blocs:[
      {t:'texte', h:"Deux dates, et un travail qui dit le contraire de sa source",
       p:"« La ville avait distribué les bacs, mais la collecte ne commença qu'en juin. » Lue vite, cette phrase dit que tout est arrivé ensemble. Lue comme il faut, elle dit que les gens ont eu un bac vide sur leur balcon pendant deux mois — et c'est exactement le détail qui fait un bon travail de recherche. Un seul temps de verbe sépare les deux lectures.",
       note:"Le programme le formule ainsi : comprendre que le plus-que-parfait désigne une action précédant une autre action passée."},

      {t:'ana', h:"Comment il se reconnaît",
       p:"Deux mots, toujours les mêmes, et l'un des deux est à l'imparfait.",
       mots:[['La forme','avait ou était, puis le participe passé'],
             ['Des exemples','il avait lu · elle était partie · on avait décidé · personne ne leur avait expliqué', true],
             ['Le réflexe','dès que vous voyez « avait » suivi d\'un participe, reculez d\'un cran dans le temps']],
       say:"il avait lu, elle était partie, on avait décidé",
       note:"« Avait » tout seul n'est qu'un imparfait : « il avait un bac ». C'est le participe qui suit qui fait le plus-que-parfait : « il avait reçu un bac »."},

      {t:'ana', h:"Ce qu'il fait dans une phrase",
       p:"Il place un fait avant un autre fait passé. Les mots de liaison, eux, ne disent rien de l'ordre.",
       mots:[['Avec « quand »','Quand Marisol trouva la page, Youssef <b>avait déjà lu</b> l\'article. — Youssef d\'abord'],
             ['Avec « parce que »','Ils se plaignirent parce que personne ne leur <b>avait expliqué</b> la règle. — l\'explication manquante d\'abord', true],
             ['Sans le plus-que-parfait','Ils se plaignirent parce que personne ne leur expliqua la règle. — les deux se suivent']],
       say:"Quand Marisol trouva la page, Youssef avait déjà lu l'article.",
       note:"« Déjà » accompagne souvent le plus-que-parfait et le rend plus visible. Mais il n'est pas obligatoire, et son absence ne change rien à l'ordre."},

      {t:'ex', h:"Sept phrases, deux ordres",
       p:"À gauche la phrase, à droite ce qui est arrivé en premier.",
       rows:[
         ["La ville avait distribué les bacs quand la collecte commença.","La distribution des bacs."],
         ["Le conseil adopta le règlement, puis il fit imprimer le dépliant.","L'adoption du règlement."],
         ["Quand Marisol trouva la page, Youssef avait déjà lu l'article.","La lecture de l'article."],
         ["L'équipe remit son plan, et l'enseignante le corrigea le soir même.","La remise du plan."],
         ["Ils se plaignirent parce que personne ne leur avait expliqué la règle.","L'explication qui n'a pas été donnée."],
         ["Danièle sortit les documents, puis elle posa deux questions.","La sortie des documents."],
         ["La lectrice écrivit parce qu'elle avait vu un sac de plastique.","Le sac de plastique vu dans le bac."],
       ]},

      {t:'piege', h:"Trois pièges",
       rows:[
         ["se fier au mot de liaison","se fier au temps du verbe",
          "« Parce que », « quand », « mais » ne disent rien de l'ordre. C'est le plus-que-parfait, et lui seul, qui recule un fait d'un cran."],
         ["confondre imparfait et plus-que-parfait","chercher le participe passé",
          "« Il avait un bac » est un imparfait : un état. « Il avait reçu un bac » est un plus-que-parfait : un fait antérieur. Un mot de plus, et le sens change complètement."],
         ["inverser deux dates dans un travail","refaire la ligne de temps sur une feuille",
          "Deux points et une flèche entre eux : trente secondes. C'est la vérification la moins chère de tout le travail, et c'est l'erreur la plus coûteuse à la correction."],
       ]},

      {t:'check', h:"Vérifions en trois questions",
       p:"Une seule bonne réponse chaque fois.",
       qs:[
         {q:"« La ville avait distribué les bacs quand la collecte commença. » Quoi d'abord ?", opts:["la distribution","le début de la collecte"], ok:0,
          fb:"Le plus-que-parfait recule d'un cran : la distribution est arrivée avant."},
         {q:"« Il avait un bac » est…", opts:["un plus-que-parfait","un imparfait"], ok:1,
          fb:"Il manque le participe passé. « Il avait reçu un bac » serait un plus-que-parfait."},
         {q:"Qu'est-ce qui dit l'ordre dans « parce qu'elle avait vu » ?", opts:["« parce que »","le plus-que-parfait"], ok:1,
          fb:"Les mots de liaison ne disent rien de l'ordre. Le temps du verbe, lui, le dit."},
       ]},

      {t:'revoir', h:"À retenir",
       p:"<b>avait</b> ou <b>était</b> + participe passé = un fait arrivé <b>avant</b> un autre fait passé. Le mot de liaison ne dit rien de l'ordre ; le temps du verbe le dit. En cas de doute, tracez la ligne de temps : deux points, une flèche."},
    ]
  },
};
