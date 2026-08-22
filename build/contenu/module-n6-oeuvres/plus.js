const PLUS = {

  prGraphie: {
    eye:'Mini-leçon', tit:"Quand les lettres mentent : ch, x, sh",
    blocs:[
      {t:'texte', h:"Trois cas où l'écriture trompe l'oreille",
       p:"Le cinéma est plein de mots savants — chronologie, orchestre, chorégraphie — et de mots empruntés — flash-back, schéma. Tous s'écrivent avec des lettres qui ne se disent pas comme on croit. Ce n'est pas grave dans la vie courante ; ça devient gênant le jour où l'on entend un mot pour la première fois, où l'on va le chercher dans un dictionnaire, et où l'on ne le trouve pas, parce qu'on l'a écrit comme on l'a entendu.",
       note:"Le programme du niveau 6 nomme ces trois cas et rien d'autre : « ch » qui se dit comme un k, « x » qui se dit comme un s, et « sh » ou « sch » qui se disent comme un ch."},

      {t:'ana', h:"Cas 1 — « ch » qui se dit comme un K",
       p:"Presque toujours dans des mots venus du grec. Ce sont des mots savants, et le vocabulaire des arts en est plein.",
       mots:[['On écrit','la {ch}ronologie · un or{ch}estre · une {ch}orale · une {ch}orégraphie'],
             ['On entend','[k], comme dans « kilo »', true],
             ['Le repère','un mot savant, souvent avec « y », « ph » ou « rh » à côté']],
       say:"la chronologie, un orchestre, une chorale, une chorégraphie",
       note:"Attention : « chercher », « chaque », « chose » gardent le son normal. Le K est l'exception, pas la règle — mais dans les mots du cinéma et de la musique, il revient sans arrêt."},

      {t:'ana', h:"Cas 2 — « x » qui se dit comme un S",
       p:"Dans quelques nombres et quelques noms de lieux, très fréquents dans une biographie remplie de dates.",
       mots:[['On écrit','di{x} · si{x} · soi{x}ante · Bru{x}elles'],
             ['On entend','[s], comme dans « dis »', true],
             ['Le piège du nombre','« dix » se dit [dis] tout seul, [di] devant un nom qui commence par une consonne, et [diz] devant une voyelle']],
       say:"dix, six, soixante, Bruxelles",
       note:"Dix minutes se dit « di minutes ». Dix ans se dit « diz ans ». Dix, tout seul, se dit « dis »."},

      {t:'ana', h:"Cas 3 — « sh » et « sch » qui se disent comme un CH",
       p:"Des mots empruntés à l'anglais ou à l'allemand, et devenus courants dans le vocabulaire du cinéma.",
       mots:[['On écrit','un fla{sh}-back · un {sch}éma · un {sh}érif'],
             ['On entend','[ʃ], le son de « chat »', true],
             ['Le repère','un mot qui vient d\'ailleurs, souvent court']],
       say:"un flash-back, un schéma, un shérif",
       note:"« Un flash-back » est le mot anglais du retour en arrière. On l'entend beaucoup au ciné-club — et il se prononce à la française, avec le son de « chat »."},

      {t:'labo', h:"Écoutez, puis répétez",
       p:"Choisissez un cas et un exemple.",
       axes:[
         {id:'c', lbl:'Quelles lettres ?', opts:[['a','ch qui dit K'],['b','x qui dit S'],['c','sh, sch qui disent CH']]},
         {id:'n', lbl:'Quel exemple ?', opts:[['1','le premier'],['2','le second']]}],
       out:{
         a1:{w:["la chronologie"], say:"la chronologie", n:'mot grec : « cro-no-lo-gie »'},
         a2:{w:["un orchestre"], say:"un orchestre", n:'« or-kestre », jamais « or-chestre »'},
         b1:{w:["dix"], say:"dix", n:'tout seul, on entend le S final'},
         b2:{w:["soixante"], say:"soixante", n:'« soi-sante », jamais « soi-ksante »'},
         c1:{w:["un schéma"], say:"un schéma", n:'trois lettres pour le son de « chat »'},
         c2:{w:["un flash-back"], say:"un flash-back", n:'venu de l\'anglais, prononcé à la française'},
       },
       note:"Écoutez deux fois avant de répéter. C'est l'oreille qu'on entraîne, pas la mémoire."},

      {t:'ex', h:"Huit mots du module",
       p:"À gauche ce qui est écrit, à droite ce qui se dit.",
       rows:[
         ["la chronologie","« cro-no-lo-gie » — le ch fait k"],
         ["un orchestre","« or-kestre » — le ch fait k"],
         ["une chorale","« co-rale » — le ch fait k"],
         ["une chorégraphie","« co-ré-gra-phie » — le ch fait k"],
         ["dix minutes","« di minutes » — le x se tait devant une consonne"],
         ["soixante-dix","« soi-sante-dis » — le x fait s"],
         ["un schéma","« ché-ma » — sch fait ch"],
         ["un flash-back","« flach-back » — sh fait ch"],
       ]},

      {t:'piege', h:"Deux pièges, une consolation",
       rows:[
         ["chercher le mot avec la lettre entendue","chercher avec la lettre écrite",
          "Vous entendez « cronologie » et vous cherchez « cronologie » : rien. Quand un mot entendu ne se trouve pas, essayez « ch » à la place du k, et « x » à la place du s."],
         ["prononcer chaque « ch » comme dans « chat »","reconnaître les mots savants",
          "« Orchestre » dit avec le son de « chat » ne se comprend pas du tout. Ces mots-là sont peu nombreux : ils s'apprennent un par un."],
         ["s'inquiéter pour « dix »","les trois formes se comprennent",
          "Personne ne vous reprendra si vous dites « diz minutes ». Ce qui compte, c'est de reconnaître les trois formes à l'écoute, pas de les produire parfaitement."],
       ]},

      {t:'check', h:"Est-ce que c'est clair maintenant ?",
       p:"Quatre questions rapides.",
       qs:[
         {q:"Dans « chronologie », les lettres « ch » se disent…", opts:["comme dans chat","comme un k"], ok:1,
          fb:"C'est un mot venu du grec : « cro-no-lo-gie »."},
         {q:"Dans « soixante », la lettre « x » se dit…", opts:["comme un s","comme un ks"], ok:0,
          fb:"« Soi-sante ». Même chose dans « dix » et « six »."},
         {q:"Dans « un flash-back », les lettres « sh » se disent…", opts:["comme un s","comme dans chat"], ok:1,
          fb:"C'est le son de « chat », même si le mot vient de l'anglais."},
         {q:"« Dix minutes » se prononce…", opts:["« di minutes »","« diss minutes »"], ok:0,
          fb:"Devant une consonne, le x de « dix » ne s'entend pas."},
       ]},

      {t:'revoir', h:"À retenir",
       p:"Trois cas seulement, mais fréquents dans les arts : <b>ch</b> qui dit k dans les mots savants (chronologie, orchestre, chorale), <b>x</b> qui dit s dans les nombres et quelques noms de lieux (dix, six, soixante), <b>sh</b> et <b>sch</b> qui disent ch dans les mots empruntés (flash-back, schéma)."},
    ]
  },

  prGenres: {
    eye:'Mini-leçon', tit:"Savoir d'avance ce qu'un texte va donner",
    blocs:[
      {t:'texte', h:"La question à se poser avant de lire",
       p:"« Qu'est-ce que ce texte va me donner ? » On perd beaucoup de temps à chercher dans un texte ce qu'il ne contient pas : une opinion dans une biographie, une histoire dans une bande-annonce, une fin dans un résumé. Reconnaître le genre en trois secondes, c'est se donner les bonnes attentes — et c'est plus utile que de connaître dix mots de plus.",
       note:"Autour d'un film, il y a toujours quatre textes et un seul film. Aucun des quatre ne remplace le film."},

      {t:'ana', h:"Les quatre textes, et ce que chacun donne",
       p:"Ils ne se ressemblent ni par la longueur, ni par le ton, ni par ce qu'ils permettent.",
       mots:[['La bande-annonce','deux minutes, une voix hors champ, aucune fin — faite pour donner envie'],
             ['La biographie','des dates et un parcours, souvent au passé simple — elle parle de la personne, jamais de l\'histoire du film'],
             ['La critique','un texte signé, publié après la sortie — le seul où quelqu\'un dit « je »', true],
             ['Le résumé','un ou deux paragraphes qui racontent sans juger, et qui s\'arrêtent avant le dénouement']],
       say:"la bande-annonce, la biographie, la critique, le résumé",
       note:"Le générique, lui, n'est pas un texte à lire : c'est une liste. Mais c'est là qu'on trouve qui a fait le montage."},

      {t:'ana', h:"Ce qu'aucun des quatre ne donne",
       p:"C'est la partie la plus utile de la leçon, et la plus vite oubliée.",
       mots:[['Le déroulement complet','il n\'est nulle part ailleurs que dans le film'],
             ['Le dénouement','le résumé s\'arrête avant ; la critique le tait par politesse'],
             ['Ce que vous en penserez','la critique donne l\'avis d\'un seul, jamais le vôtre', true]],
       say:"Le déroulement complet n'est nulle part ailleurs que dans le film.",
       note:"C'est pour ça qu'un ciné-club projette avant de discuter, et jamais l'inverse."},

      {t:'ex', h:"Six phrases, et de quel texte elles viennent",
       p:"À gauche la phrase, à droite le texte d'où elle sort.",
       rows:[
         ["« Elle croyait n'avoir que des boîtes à faire. »","la bande-annonce — une phrase, aucune suite"],
         ["« Elle entra dans une salle de montage en 1972. »","la biographie — une date, un passé simple"],
         ["« Mon vrai reproche est ailleurs. »","la critique — quelqu'un dit « mon »"],
         ["« Estelle revient vider la maison de sa mère en trois jours. »","le résumé — l'histoire, sans jugement"],
         ["« Montage : Aurélie Pichette. »","le générique — une liste de noms"],
         ["« Il y a un moment où l'image devient plus froide. »","aucun des quatre — ça, c'est le film"],
       ]},

      {t:'check', h:"Est-ce que c'est clair maintenant ?",
       p:"Quatre questions rapides.",
       qs:[
         {q:"Pour savoir ce que raconte un film, il vaut mieux lire…", opts:["la bande-annonce","le résumé"], ok:1,
          fb:"Le résumé raconte ; la bande-annonce montre trois images et se tait."},
         {q:"Le seul texte où quelqu'un dit « je », c'est…", opts:["la critique","la biographie"], ok:0,
          fb:"Une critique est signée et assume son avis. Une biographie n'en donne aucun."},
         {q:"Une biographie parle surtout…", opts:["de l'histoire du film","du parcours de la personne"], ok:1,
          fb:"Elle dit d'où vient la réalisatrice, pas ce qui arrive à ses personnages."},
         {q:"Un résumé s'arrête…", opts:["avant le dénouement","après le générique"], ok:0,
          fb:"Raconter la fin dans un résumé, c'est gâcher le film à celui qui le lit."},
       ]},

      {t:'revoir', h:"À retenir",
       p:"Quatre textes autour d'un film : la <b>bande-annonce</b> donne envie, la <b>biographie</b> situe la personne, la <b>critique</b> juge et signe, le <b>résumé</b> raconte sans juger. Le <b>déroulement complet</b>, lui, n'est que dans le film."},
    ]
  },

  prChamp: {
    eye:'Mini-leçon', tit:"Le mot précis fait le travail à ta place",
    blocs:[
      {t:'texte', h:"Un champ lexical, ce n'est pas une liste de mots à apprendre",
       p:"C'est un groupe de mots qui parlent de la même chose, et qui se distinguent par un détail. « Film » suffit pour se faire comprendre. « Court métrage » évite d'avoir à expliquer pourquoi ça ne durait que douze minutes. Le mot précis porte l'information à ta place : c'est du temps de parole gagné, et c'est ce que le niveau 6 appelle exprimer le détail ou la nuance.",
       note:"Le programme donne lui-même l'exemple du cinéma : documentaire, film, reportage, court métrage. Et celui du logis : condo, maison, château, villa."},

      {t:'ana', h:"Le champ lexical du cinéma, par ce qui les distingue",
       p:"Ce n'est pas la difficulté du mot qui compte, c'est le détail qu'il porte.",
       mots:[['La durée','un <b>court métrage</b> (moins de 20 minutes) · un <b>long métrage</b> (plus d\'une heure)'],
             ['La nature','un <b>documentaire</b> montre des faits réels · une <b>fiction</b> invente'],
             ['Le découpage','une <b>série</b> en épisodes · un <b>téléfilm</b> en une seule fois', true],
             ['La partie','une <b>scène</b> (un lieu, d\'un seul tenant) · un <b>plan</b> (sans coupure de caméra)']],
       say:"un court métrage, un long métrage, un documentaire, une série, une scène",
       note:"Un mot précis mal employé fait plus de dégâts qu'un mot vague bien employé. Dans le doute, dis « un film » et ajoute la durée."},

      {t:'ana', h:"Le même mécanisme dans le jugement",
       p:"C'est là que le niveau 6 se distingue du niveau 5 : ce n'est plus « c'est bon » ou « c'est mauvais ».",
       mots:[['Trop vague','c\'est bon · c\'est plate · j\'ai aimé'],
             ['Plus précis','<b>convaincant</b> · <b>lent</b> · <b>touchant</b> · <b>invraisemblable</b>'],
             ['Encore plus précis','<b>un parti pris</b> · <b>un reproche</b> · <b>une maladresse</b>', true],
             ['Ce que ça change','« lent » se discute, « plate » ne se discute pas']],
       say:"convaincant, lent, touchant, un parti pris, un reproche, une maladresse",
       note:"Un adjectif précis appelle une réponse ; un adjectif vague ferme la discussion. C'est vrai d'un film comme de tout le reste."},

      {t:'ex', h:"Six fois le mot vague, six fois le mot précis",
       p:"À gauche ce qu'on dit d'abord, à droite ce qu'on peut dire.",
       rows:[
         ["« J'ai vu un film de douze minutes. »","« J'ai vu un court métrage. »"],
         ["« C'est un film avec des vraies affaires. »","« C'est un documentaire. »"],
         ["« Le bout où elle ouvre l'armoire. »","« La scène de l'armoire. »"],
         ["« Ils repassent tous ses films. »","« Ils font une rétrospective. »"],
         ["« C'était bon. »","« Le personnage de la voisine est convaincant. »"],
         ["« C'était long. »","« La première demi-heure est lente. »"],
       ]},

      {t:'check', h:"Est-ce que c'est clair maintenant ?",
       p:"Quatre questions rapides.",
       qs:[
         {q:"Un film de douze minutes s'appelle…", opts:["un court métrage","un téléfilm"], ok:0,
          fb:"Moins de vingt minutes : c'est un court métrage."},
         {q:"Une « scène », c'est…", opts:["un morceau dans un seul lieu","tout le film"], ok:0,
          fb:"Un lieu, d'un seul tenant. Quand le lieu change, la scène est finie."},
         {q:"Entre « c'était plate » et « la première demi-heure est lente »…", opts:["c'est pareil","la seconde se discute"], ok:1,
          fb:"La seconde nomme un moment précis : on peut y répondre."},
         {q:"Chercher le mot précis, ça sert surtout à…", opts:["avoir l'air savant","dire le détail sans l'expliquer"], ok:1,
          fb:"Le mot porte l'information : tu n'as plus à l'ajouter."},
       ]},

      {t:'revoir', h:"À retenir",
       p:"Un <b>champ lexical</b> range des mots proches et les distingue par un détail : durée, nature, découpage. Cherche toujours le mot le plus précis que tu connais ; s'il n'existe pas, garde le mot vague et ajoute le détail."},
    ]
  },

  t1sign: {
    eye:'Mini-leçon', tit:"Avant ou après ? La seule question à tenir",
    blocs:[
      {t:'texte', h:"Un film qui recule, et un spectateur qui décroche",
       p:"« Les Marées de novembre » tient en trois jours et recule quatre fois jusqu'en 1978. Ce n'est pas rare : la moitié des films le font. Ce qui fait décrocher, ce n'est pas la difficulté des mots — c'est de ne plus savoir en quelle année on est. Une seule question suffit à ne pas se perdre, à condition de la tenir jusqu'au générique.",
       note:"Ce module s'appuie sur un film inventé. La méthode, elle, marche sur n'importe quel film que vous verrez ensuite."},

      {t:'ana', h:"Les trois signaux de ce film-ci",
       p:"Chaque réalisateur a les siens, et il les annonce dès les premières minutes.",
       mots:[['L\'image','elle devient plus froide, presque grise'],
             ['La musique','elle s\'arrête net'],
             ['Le son','le bruit de la mer revient', true],
             ['Ils arrivent ensemble','les trois d\'un coup : c\'est ce qui les rend reconnaissables']],
       say:"L'image devient plus froide, la musique s'arrête, le bruit de la mer revient.",
       note:"Le son est le signal le plus sûr. On peut manquer une couleur en lisant les sous-titres ; on manque rarement un bruit de mer."},

      {t:'ana', h:"Ce qui trahit l'époque, dans n'importe quel film",
       p:"Quand les signaux vous échappent, il reste ceci — et ça ne trompe presque jamais.",
       mots:[['L\'âge des personnages','le frère a dix-neuf ans dans les retours en arrière, et il n\'apparaît jamais aujourd\'hui'],
             ['Les objets','une lampe, un téléphone, une automobile datent une scène en une seconde'],
             ['La place d\'un objet','la lettre est dans le tiroir avant, dans la poche après', true],
             ['La lumière','vendredi il fait noir, samedi il fait gris, dimanche il neige']],
       say:"L'âge des personnages, les objets, la place d'un objet, la lumière.",
       note:"Un objet qui change de place date une scène plus sûrement qu'une date affichée à l'écran."},

      {t:'ex', h:"Six moments, et ce qui permet de les situer",
       p:"À gauche le moment, à droite l'indice.",
       rows:[
         ["Estelle descend de l'autobus devant l'église","elle arrive : c'est le début des trois jours"],
         ["Le jeune homme et son chien au bout du quai","le frère a dix-neuf ans : nous sommes en 1978"],
         ["Quelqu'un écrit une lettre à la lampe","la lettre n'est pas encore dans le tiroir"],
         ["La mère dit « ton frère avait le même manteau »","la mère parle à Estelle adulte : aujourd'hui"],
         ["Le bateau quitte le quai, la musique s'arrête","deux signaux d'un coup : 1978"],
         ["Estelle relit la lettre sur une boîte","la lettre est trouvée : après le samedi"],
       ]},

      {t:'piege', h:"Trois façons de se perdre",
       rows:[
         ["croire qu'un jeune homme est forcément le fils","écouter ce que les personnages disent des liens",
          "La phrase « ton frère avait le même manteau » place tout le reste. Elle dure une seconde et elle est facile à manquer, surtout en lisant les sous-titres."],
         ["attendre qu'un carton annonce la date","chercher les signaux du réalisateur",
          "Presque aucun film n'affiche « 1978 » à l'écran. C'est l'image et le son qui le disent."],
         ["abandonner après une scène perdue","reprendre à la scène suivante",
          "Se perdre une fois ne coûte rien. Ce qui coûte, c'est de cesser de se poser la question."],
       ]},

      {t:'check', h:"Est-ce que c'est clair maintenant ?",
       p:"Quatre questions rapides.",
       qs:[
         {q:"La question à se poser à chaque changement d'image, c'est…", opts:["qui parle ?","avant ou après ?"], ok:1,
          fb:"Une seule question, tenue jusqu'au générique."},
         {q:"Le signal le plus sûr, dans ce film, c'est…", opts:["la couleur de l'image","le bruit de la mer"], ok:1,
          fb:"On peut manquer une couleur ; on manque rarement un son."},
         {q:"Un objet qui change de place…", opts:["date une scène","ne veut rien dire"], ok:0,
          fb:"La lettre est dans le tiroir avant, dans la poche après."},
         {q:"La réalisatrice casse sa propre règle…", opts:["une fois, exprès","trois fois, par erreur"], ok:0,
          fb:"Une règle cassée une fois est un effet ; cassée trois fois, c'est une erreur."},
       ]},

      {t:'revoir', h:"À retenir",
       p:"Une seule question, à chaque changement d'image : <b>avant ou après ?</b> Les signaux du film — image, musique, son — répondent presque toujours. Sinon, regardez l'âge des personnages, les objets et la lumière."},
    ]
  },

  t1pqp: {
    eye:'Mini-leçon', tit:"Le plus-que-parfait : reculer d'un cran",
    blocs:[
      {t:'texte', h:"Le temps du retour en arrière",
       p:"Le passé composé raconte ce qui est arrivé. Le plus-que-parfait raconte ce qui était déjà arrivé avant. C'est un cran de plus vers l'arrière, et c'est exactement le travail d'un retour en arrière au cinéma. Un film s'en passe — il montre les images. Un texte, lui, ne peut pas s'en passer : c'est le seul moyen de dire au lecteur qu'il vient de reculer.",
       note:"Le programme dit : comprendre l'antériorité avec le plus-que-parfait quand le point de référence est décalé. « Décalé » veut dire : le repère n'est pas aujourd'hui, c'est un moment du passé."},

      {t:'ana', h:"Comment il se fabrique",
       p:"Deux morceaux, toujours les mêmes.",
       mots:[['L\'auxiliaire à l\'imparfait','<b>avait</b> ou <b>était</b>'],
             ['Le participe passé','pris · parti · écrit · vu'],
             ['Ensemble','elle <b>avait pris</b> · il <b>était parti</b> · elles s\'<b>étaient vues</b>', true],
             ['L\'accord','avec « être », le participe s\'accorde avec le sujet : elle était partie']],
       say:"elle avait pris, il était parti, elles s'étaient vues, elle était partie",
       note:"Si vous savez faire le passé composé, vous savez déjà faire le plus-que-parfait : c'est le même participe, avec l'auxiliaire à l'imparfait."},

      {t:'ana', h:"Ce qu'il change au sens",
       p:"Trois phrases, trois moments différents. Le verbe seul les distingue.",
       mots:[['Aujourd\'hui','Elle <b>lit</b> la lettre.'],
             ['Un moment du passé','Elle <b>a lu</b> la lettre samedi.'],
             ['Avant ce moment-là','La lettre <b>avait été écrite</b> en 1978.', true],
             ['Le lecteur y gagne','il sait, sans qu\'on le lui dise, qu\'on vient de reculer de quarante ans']],
       say:"Elle lit la lettre. Elle a lu la lettre samedi. La lettre avait été écrite en 1978.",
       note:"C'est pour ça qu'une biographie et un résumé de film en sont pleins : ils racontent des choses qui ne sont pas arrivées dans l'ordre."},

      {t:'ex', h:"Six phrases du film",
       p:"À gauche la phrase, à droite ce que le plus-que-parfait vous apprend.",
       rows:[
         ["Elle arrive le soir : elle avait pris l'autobus du matin.","le voyage a commencé avant son arrivée"],
         ["La lettre avait été écrite trois semaines avant le départ.","la lettre est plus vieille que le naufrage"],
         ["Il était parti un matin de novembre.","le départ précède tout ce qu'on voit"],
         ["Le film avait été présenté à Sherbrooke en premier.","avant les autres villes"],
         ["Elle n'avait pas entendu la phrase de la mère.","elle avait déjà décroché quand la scène est arrivée"],
         ["La mère avait rangé les photos dans le tiroir.","bien avant qu'Estelle ouvre le tiroir"],
       ]},

      {t:'piege', h:"Deux pièges",
       rows:[
         ["« elle a pris l'autobus du matin, mais elle arrive le soir »","« elle avait pris l'autobus du matin »",
          "Avec le passé composé, les deux actions paraissent au même moment, et le lecteur cherche pourquoi ça ne colle pas. Le plus-que-parfait règle tout."],
         ["oublier l'accord avec « être »","elle était partie, elles étaient venues",
          "Avec l'auxiliaire « être », le participe s'accorde avec le sujet — exactement comme au passé composé."],
       ]},

      {t:'check', h:"Est-ce que c'est clair maintenant ?",
       p:"Quatre questions rapides.",
       qs:[
         {q:"Le plus-que-parfait se fabrique avec…", opts:["l'auxiliaire à l'imparfait","l'auxiliaire au présent"], ok:0,
          fb:"avait, était — puis le participe passé."},
         {q:"« La lettre avait été écrite en 1978 » veut dire…", opts:["elle a été écrite avant le moment dont on parle","elle est en train de s'écrire"], ok:0,
          fb:"Un cran plus loin dans le passé."},
         {q:"Dans un résumé de film, il sert surtout à…", opts:["allonger les phrases","placer les retours en arrière"], ok:1,
          fb:"C'est le seul moyen de dire au lecteur qu'on recule."},
         {q:"« Il était parti » : le participe s'accorde…", opts:["avec le sujet","jamais"], ok:0,
          fb:"Avec l'auxiliaire « être », il s'accorde avec le sujet."},
       ]},

      {t:'revoir', h:"À retenir",
       p:"Le <b>plus-que-parfait</b> = auxiliaire à l'imparfait (<b>avait</b>, <b>était</b>) + participe passé. Il place une action <b>avant</b> une autre action passée. C'est le temps des retours en arrière, à l'écrit."},
    ]
  },

  t1imp: {
    eye:'Mini-leçon', tit:"L'imparfait : ce qui était en train de se passer",
    blocs:[
      {t:'texte', h:"Ce qui avance, et ce qui tient",
       p:"Dans un récit, deux temps se partagent le travail. Le passé composé fait avancer l'histoire : une action, puis une autre. L'imparfait, lui, fait tenir le décor : ce qui durait, ce qui était commencé et pas fini. Un film utilise l'image pour ça ; un texte utilise l'imparfait.",
       note:"Le programme le formule ainsi : comprendre et employer l'imparfait pour signifier une action en cours dans le passé, avec ou sans « être en train de »."},

      {t:'ana', h:"Les deux formes, et ce qu'elles changent",
       p:"Elles disent la même chose ; la seconde insiste davantage.",
       mots:[['Sans « être en train de »','Elle <b>lisait</b> les sous-titres.'],
             ['Avec','Elle <b>était en train de lire</b> les sous-titres.'],
             ['Le sens','identique — l\'action est commencée et pas finie', true],
             ['Quand choisir la longue','quand on veut souligner l\'interruption : « j\'étais en train de le dire »']],
       say:"Elle lisait les sous-titres. Elle était en train de lire les sous-titres.",
       note:"La forme longue est plus fréquente à l'oral, la courte à l'écrit. Aucune des deux n'est plus correcte."},

      {t:'ana', h:"Le partage du travail avec le passé composé",
       p:"Dans la même phrase, les deux temps ne font pas le même métier.",
       mots:[['L\'imparfait','le décor, ce qui durait : elle <b>vidait</b> la cuisine'],
             ['Le passé composé','l\'événement, ce qui arrive : le téléphone <b>a sonné</b>'],
             ['Ensemble','Elle <b>vidait</b> la cuisine quand le téléphone <b>a sonné</b>.', true],
             ['Le test','peut-on mettre « pendant que » devant ? Si oui, c\'est l\'imparfait']],
       say:"Elle vidait la cuisine quand le téléphone a sonné.",
       note:"Inverser les deux change tout : « elle a vidé la cuisine quand le téléphone sonnait » ne raconte plus la même scène."},

      {t:'ex', h:"Six couples du film",
       p:"À gauche ce qui durait, à droite ce qui est arrivé.",
       rows:[
         ["Elle lisait les sous-titres","quand la mère a dit la phrase"],
         ["Gilles dormait dans la troisième rangée","quand la scène du quai est passée"],
         ["Le vent soufflait depuis deux jours","quand le bateau est parti"],
         ["Elle vidait la cuisine","quand elle a trouvé la lettre"],
         ["La voisine attendait depuis quarante ans","quand Estelle a frappé"],
         ["La musique jouait","quand l'image est devenue grise"],
       ]},

      {t:'check', h:"Est-ce que c'est clair maintenant ?",
       p:"Quatre questions rapides.",
       qs:[
         {q:"« Elle lisait » et « elle était en train de lire »…", opts:["disent la même chose","disent deux choses différentes"], ok:0,
          fb:"Même sens ; la seconde forme insiste seulement davantage."},
         {q:"Dans « elle vidait la cuisine quand le téléphone a sonné », ce qui durait, c'est…", opts:["vider la cuisine","sonner"], ok:0,
          fb:"L'imparfait porte ce qui durait ; le passé composé, l'événement."},
         {q:"Le test le plus simple, c'est d'essayer d'ajouter…", opts:["« pendant que »","« hier »"], ok:0,
          fb:"Pendant qu'elle vidait la cuisine… — si ça passe, c'est l'imparfait."},
         {q:"Dans un récit, l'imparfait sert surtout à…", opts:["faire avancer l'histoire","tenir le décor"], ok:1,
          fb:"C'est le passé composé qui fait avancer."},
       ]},

      {t:'revoir', h:"À retenir",
       p:"L'<b>imparfait</b> montre une action <b>commencée et pas finie</b> : elle lisait, il dormait, le vent soufflait. Le passé composé, lui, fait avancer l'histoire. Le test : si « pendant que » passe devant, c'est l'imparfait."},
    ]
  },

  t1ordre: {
    eye:'Mini-leçon', tit:"Trouver l'ordre sans les mots « avant » et « après »",
    blocs:[
      {t:'texte', h:"Un film n'a pas de narrateur pour vous dire « ensuite »",
       p:"Dans une chronique de radio, quelqu'un dit « premièrement, deuxièmement ». Dans un film, personne ne le dit. L'ordre est pourtant là, porté par autre chose : un verbe, un temps, un objet, une lumière. Apprendre à le lire, c'est apprendre à raconter un film sans se tromper — et c'est ce que la production de « Je me lance » demande.",
       note:"Le programme le formule ainsi : comprendre l'ordre des étapes à partir d'indices linguistiques autres que les connecteurs de temps."},

      {t:'ana', h:"Quatre indices, du plus visible au plus discret",
       p:"Le premier saute aux yeux ; les trois autres se travaillent.",
       mots:[['Les connecteurs','d\'abord, ensuite, enfin, puis — les seuls qui le disent'],
             ['Le verbe','« <b>revenir</b> » suppose qu\'on y est déjà allé ; « <b>rouvrir</b> », qu\'on avait fermé'],
             ['Le temps','un plus-que-parfait recule d\'un cran, toujours', true],
             ['L\'objet','la lettre est dans le tiroir avant, dans la poche après']],
       say:"D'abord, ensuite, enfin. Revenir suppose qu'on y est déjà allé.",
       note:"Le verbe est l'indice le plus fréquent et le moins remarqué. Revenir, rentrer, rouvrir, redonner : le « re- » place la scène à lui seul."},

      {t:'ana', h:"Deux ordres qui ne se confondent pas",
       p:"C'est la difficulté propre à ce film — et à la moitié des films.",
       mots:[['L\'ordre du récit','celui dans lequel le film vous montre les choses'],
             ['L\'ordre de l\'histoire','celui dans lequel elles sont arrivées'],
             ['Ils diffèrent','quatre fois dans « Les Marées de novembre »', true],
             ['Ce qu\'on raconte à quelqu\'un','l\'ordre de l\'histoire — sinon on le perd en trois phrases']],
       say:"L'ordre du récit et l'ordre de l'histoire ne sont pas le même ordre.",
       note:"Quand vous racontez un film à quelqu'un, remettez tout dans l'ordre de l'histoire. Le film peut se permettre de mélanger ; vous, non."},

      {t:'ex', h:"Les trois jours, remis à plat",
       p:"À gauche le rang, à droite ce qui se passe.",
       rows:[
         ["Bien avant le film","une lettre est écrite, trois semaines avant le départ du bateau"],
         ["Déjà fait au premier plan","Estelle prend l'autobus du matin, qui tombe en panne à Matane"],
         ["Vendredi soir","elle arrive au village et ouvre la maison"],
         ["Samedi","elle vide la cuisine et trouve la lettre"],
         ["Dimanche","elle va frapper chez la voisine"],
         ["Après le générique","le ciné-club discute une demi-heure"],
       ]},

      {t:'check', h:"Est-ce que c'est clair maintenant ?",
       p:"Quatre questions rapides.",
       qs:[
         {q:"« Elle revient au village » indique…", opts:["qu'elle y était déjà allée","qu'elle y va pour la première fois"], ok:0,
          fb:"Le « re- » place la scène à lui seul."},
         {q:"Un plus-que-parfait, dans un récit…", opts:["recule d'un cran","avance d'un cran"], ok:0,
          fb:"Toujours vers l'arrière, sans exception."},
         {q:"L'ordre du récit et l'ordre de l'histoire…", opts:["sont toujours les mêmes","diffèrent souvent"], ok:1,
          fb:"Ils diffèrent quatre fois dans ce film-ci."},
         {q:"Quand on raconte un film à quelqu'un, on suit…", opts:["l'ordre de l'histoire","l'ordre du récit"], ok:0,
          fb:"Sinon on perd son interlocuteur en trois phrases."},
       ]},

      {t:'revoir', h:"À retenir",
       p:"Quand les connecteurs manquent, l'ordre se lit ailleurs : dans le <b>verbe</b> (revenir, rouvrir), dans le <b>temps</b> (le plus-que-parfait recule), dans la place d'un <b>objet</b>, dans la <b>lumière</b>. Et pour raconter : toujours l'ordre de l'histoire."},
    ]
  },

  t1temps: {
    eye:'Mini-leçon', tit:"Les mots qui placent un moment",
    blocs:[
      {t:'texte', h:"« Avant » tout seul ne dit rien",
       p:"Avant quoi ? Après quoi ? Un marqueur de temps utile porte un repère ou une durée : la veille, le lendemain, trois semaines plus tôt, depuis deux jours. Sans lui, un récit se lit comme une liste de choses arrivées on ne sait quand — et c'est le défaut le plus fréquent dans les résumés de film.",
       note:"Ces marqueurs sont les mêmes dans un résumé de film, dans une biographie et dans un courriel qui raconte un événement."},

      {t:'ana', h:"Reculer, avancer, mesurer",
       p:"Six mots qui font presque tout le travail.",
       mots:[['Le jour d\'avant','<b>la veille</b> — Estelle était arrivée la veille.'],
             ['Le jour d\'après','<b>le lendemain</b> — Le lendemain, elle a vidé la cuisine.'],
             ['Reculer d\'une durée','<b>trois semaines plus tôt</b>, <b>quarante ans auparavant</b>', true],
             ['Depuis quand ça dure','<b>depuis deux jours</b> — ça a commencé et ça continue'],
             ['Le point de départ','<b>dès son arrivée</b>, <b>à partir de ce moment-là</b>']],
       say:"la veille, le lendemain, trois semaines plus tôt, depuis deux jours, dès son arrivée",
       note:"« La veille » et « le lendemain » se rapportent à un jour dont on parle — pas à aujourd'hui. Pour aujourd'hui, on dit « hier » et « demain »."},

      {t:'ex', h:"Six phrases, six repères",
       p:"À gauche la phrase, à droite ce que le marqueur ajoute.",
       rows:[
         ["Elle arrive le vendredi soir ; le lendemain, elle vide la cuisine.","le samedi, sans avoir à le nommer"],
         ["La lettre avait été écrite trois semaines avant le départ.","une distance mesurée, pas vague"],
         ["Le vent soufflait depuis deux jours.","ça a commencé avant et ça continue"],
         ["Elle n'avait pas revu la voisine depuis quarante ans.","la durée du silence entre elles"],
         ["Dès son arrivée, elle a compris que trois jours ne suffiraient pas.","le point de départ exact"],
         ["Il était parti un matin de novembre.","un moment situé, sans date précise"],
       ]},

      {t:'piege', h:"Deux confusions courantes",
       rows:[
         ["« hier » dans un récit au passé","« la veille »",
          "« Hier » se compte à partir d'aujourd'hui. Dans un récit qui se passe en novembre 1978, « hier » ne veut plus rien dire : c'est « la veille »."],
         ["« depuis » pour une action finie","« il y a »",
          "« Il est parti depuis deux jours » se dit, mais « il est parti il y a deux jours » est plus clair. « Depuis » va avec ce qui dure encore."],
       ]},

      {t:'check', h:"Est-ce que c'est clair maintenant ?",
       p:"Quatre questions rapides.",
       qs:[
         {q:"Dans un récit au passé, le jour d'avant se dit…", opts:["hier","la veille"], ok:1,
          fb:"« Hier » se compte à partir d'aujourd'hui, pas à partir du récit."},
         {q:"« Depuis deux jours » veut dire…", opts:["ça a commencé et ça continue","c'est fini depuis deux jours"], ok:0,
          fb:"« Depuis » va avec ce qui dure encore."},
         {q:"« Dès son arrivée » marque…", opts:["le point de départ","la fin"], ok:0,
          fb:"À partir de ce moment-là, et pas avant."},
         {q:"Un marqueur utile porte…", opts:["un repère ou une durée","seulement le mot avant"], ok:0,
          fb:"« Avant » tout seul ne place rien."},
       ]},

      {t:'revoir', h:"À retenir",
       p:"<b>La veille</b> / <b>le lendemain</b> pour reculer ou avancer d'un jour dans un récit ; <b>trois semaines plus tôt</b> pour mesurer ; <b>depuis</b> pour ce qui dure encore ; <b>dès</b> pour le point de départ."},
    ]
  },

  t2texte: {
    eye:'Mini-leçon', tit:"Lire une biographie sans se perdre",
    blocs:[
      {t:'texte', h:"Dix lignes, et tout ce qui arrête un lecteur",
       p:"Une biographie de ciné-club tient sur une demi-feuille. Elle est pourtant plus difficile qu'un dialogue de trente répliques, et pour trois raisons : ses verbes sont à un temps qu'on ne parle jamais, ses dates ne sont pas dans l'ordre, et elle est pleine de petits mots — le, en, y, où — qui renvoient à la phrase d'avant.",
       note:"C'est le cœur du niveau 6. Ce qui est difficile n'est plus le vocabulaire : c'est la cohésion, c'est-à-dire ce qui tient le texte ensemble."},

      {t:'ana', h:"Trois obstacles, trois gestes",
       p:"Chacun se règle par un geste précis, à faire pendant la lecture et non après.",
       mots:[['Les verbes au passé simple','les traduire dans sa tête : elle naquit → elle est née'],
             ['Les dates dans le désordre','faire une ligne du temps au crayon, dans la marge'],
             ['Les petits mots','reculer d\'une phrase, jamais plus loin', true],
             ['Ce qu\'on ne fait pas','chercher chaque mot inconnu au dictionnaire — on perd le fil, qui est le vrai enjeu']],
       say:"Traduire le passé simple, faire une ligne du temps, reculer d'une phrase.",
       note:"Trois gestes, dans cet ordre. Le troisième est le plus rentable : c'est celui qui empêche de comprendre une phrase à l'envers."},

      {t:'ana', h:"Ce qu'une biographie donne et ne donne pas",
       p:"Elle sert à situer une personne, jamais à comprendre un film.",
       mots:[['Elle donne','un parcours, des dates, des choix de métier'],
             ['Elle donne parfois','une phrase de la personne, entre guillemets'],
             ['Elle ne donne jamais','l\'histoire du film, ni un avis sur lui', true],
             ['Pourquoi on la lit quand même','elle explique souvent une forme : onze ans de montage, et un film construit en morceaux']],
       say:"Elle donne un parcours et des dates. Elle ne donne jamais l'histoire du film.",
       note:"« Elle apprit son métier au montage » explique pourquoi ce film-là est monté en quatre retours en arrière. C'est le lien le plus utile qu'une biographie puisse offrir."},

      {t:'ex', h:"La ligne du temps d'Aurélie Pichette",
       p:"À gauche l'année, à droite ce qui arrive.",
       rows:[
         ["1951","naissance à Rimouski"],
         ["1968","départ pour Montréal, à dix-sept ans"],
         ["1972","entrée dans une salle de montage — onze ans"],
         ["1979","premier court métrage, douze minutes, trois projections"],
         ["1994","« Les Marées de novembre », huit salles, onze semaines à Sherbrooke"],
         ["2007","elle cesse de tourner ; elle enseigne jusqu'en 2019"],
         ["2016","rétrospective à la salle Beauchemin"],
       ]},

      {t:'check', h:"Est-ce que c'est clair maintenant ?",
       p:"Quatre questions rapides.",
       qs:[
         {q:"Le premier geste devant une biographie, c'est…", opts:["chercher les mots inconnus","traduire les verbes au passé simple"], ok:1,
          fb:"Les mots inconnus attendront ; le fil, non."},
         {q:"Pour retrouver à quoi renvoie « y », il faut…", opts:["reculer d'une phrase","relire tout le texte"], ok:0,
          fb:"Le référent est presque toujours dans la phrase d'avant."},
         {q:"Une biographie raconte…", opts:["le parcours de la personne","l'histoire du film"], ok:0,
          fb:"Le film, c'est le résumé qui le raconte."},
         {q:"Onze ans de montage expliquent…", opts:["la forme du film","le prix des billets"], ok:0,
          fb:"Un film construit en morceaux par quelqu'un qui a passé onze ans à assembler des morceaux."},
       ]},

      {t:'revoir', h:"À retenir",
       p:"Trois gestes pendant la lecture : <b>traduire</b> le passé simple, <b>ranger</b> les dates sur une ligne du temps, <b>reculer d'une phrase</b> pour chaque petit mot. Et se souvenir qu'une biographie situe une personne, jamais un film."},
    ]
  },

  t2ps: {
    eye:'Mini-leçon', tit:"Le passé simple : le lire, jamais l'écrire",
    blocs:[
      {t:'texte', h:"Un temps qu'on lit toute sa vie et qu'on ne dit jamais",
       p:"« Elle naquit », « elle entra », « il fut ». Personne ne parle comme ça, et personne ne vous demandera de le faire. Mais ce temps est partout dans ce qu'on lit : les biographies, les romans, les contes, le texte des documentaires. Le programme du niveau 6 demande une seule chose à son sujet : le reconnaître, et l'associer au passé composé.",
       note:"Écrire un passé simple est exactement ce qu'il ne faut pas faire à ce stade. Le reconnaître suffit, et c'est déjà beaucoup."},

      {t:'ana', h:"Les terminaisons qui reviennent, à la 3e personne",
       p:"C'est la seule personne qu'on rencontre vraiment dans un texte écrit.",
       mots:[['En -a','elle tourn<b>a</b>, elle quitt<b>a</b>, elle entr<b>a</b> — les verbes en -er'],
             ['En -it','elle part<b>it</b>, il fin<b>it</b>, elle sort<b>it</b>'],
             ['En -ut','il f<b>ut</b>, elle p<b>ut</b>, il v<b>oulut</b>', true],
             ['En -int','elle v<b>int</b>, il t<b>int</b>, elle rev<b>int</b>']],
       say:"elle tourna, elle partit, il fut, elle vint",
       note:"Au pluriel, on ajoute -èrent, -irent, -urent, -inrent : elles tournèrent, ils partirent, ils furent, elles vinrent."},

      {t:'ana', h:"Ce qu'il veut dire, exactement",
       p:"Rien de plus solennel, rien de plus ancien : la même chose que le passé composé.",
       mots:[['Le sens','une action finie, à un moment précis du passé'],
             ['La différence','elle est de <b>registre</b>, pas de sens : l\'un s\'écrit, l\'autre se parle'],
             ['La traduction','elle naquit = elle est née · il fut = il a été', true],
             ['Où vous ne le verrez jamais','dans un courriel, un message, une conversation, une consigne']],
       say:"elle naquit, elle est née ; il fut, il a été",
       note:"Un texte au passé simple n'est pas plus difficile : il est seulement écrit dans un registre soutenu."},

      {t:'ex', h:"Huit verbes de la biographie",
       p:"À gauche ce qui est écrit, à droite ce qu'on dirait.",
       rows:[
         ["elle naquit à Rimouski","elle est née à Rimouski"],
         ["elle quitta la Gaspésie","elle a quitté la Gaspésie"],
         ["elle entra dans une salle de montage","elle est entrée dans une salle de montage"],
         ["elle apprit son métier","elle a appris son métier"],
         ["le film sortit en 1994","le film est sorti en 1994"],
         ["la critique fut sévère","la critique a été sévère"],
         ["le public revint","le public est revenu"],
         ["elle refusa de parler","elle a refusé de parler"],
       ]},

      {t:'piege', h:"Le piège d'une seule lettre",
       rows:[
         ["lire « elle vint » comme « elle vient »","une seule lettre, quarante ans d'écart",
          "« Elle vint » est du passé ; « elle vient » est du présent. Dans une biographie, c'est presque toujours le passé — mais vérifiez la date de la phrase."],
         ["essayer d'écrire au passé simple","écrire au passé composé",
          "Personne ne vous le demandera, et une forme inventée se voit tout de suite. Le passé composé est juste, partout, tout le temps."],
       ]},

      {t:'check', h:"Est-ce que c'est clair maintenant ?",
       p:"Quatre questions rapides.",
       qs:[
         {q:"« Elle entra » se traduit par…", opts:["elle est entrée","elle entre"], ok:0,
          fb:"Passé simple = passé composé, en registre écrit."},
         {q:"On rencontre le passé simple surtout…", opts:["dans les conversations","dans les biographies et les romans"], ok:1,
          fb:"Jamais dans une conversation, jamais dans un courriel."},
         {q:"Le programme demande de…", opts:["le reconnaître","l'écrire"], ok:0,
          fb:"Reconnaître les verbes courants à la 3e personne, et rien de plus."},
         {q:"« Il fut sévère » veut dire…", opts:["il a été sévère","il sera sévère"], ok:0,
          fb:"C'est du passé, pas du futur."},
       ]},

      {t:'revoir', h:"À retenir",
       p:"Le <b>passé simple</b> se lit et ne se parle pas. Quatre terminaisons à la 3e personne : <b>-a</b>, <b>-it</b>, <b>-ut</b>, <b>-int</b>. On le traduit en passé composé dans sa tête, et on continue de lire."},
    ]
  },

  t2ou: {
    eye:'Mini-leçon', tit:"« Où » : un seul mot, un lieu ou un moment",
    blocs:[
      {t:'texte', h:"Un mot qui fait deux métiers",
       p:"« Sherbrooke, où il avait été présenté en premier » parle d'une ville. « L'année où elle cessa de tourner » parle d'un moment. C'est le même mot, écrit pareil, et rien ne les distingue sauf ce qui vient juste avant. Une fois qu'on le sait, on cesse de buter dessus — et on gagne le droit d'écrire des phrases plus longues.",
       note:"Le programme du niveau 6 le demande deux fois : associer le pronom relatif « où » à son antécédent, et employer des phrases subordonnées relatives avec « où », complément de lieu ou de temps."},

      {t:'ana', h:"Le lieu",
       p:"Le mot qui précède « où » désigne un endroit.",
       mots:[['Deux phrases','Le film a tenu l\'affiche à Sherbrooke. Il y avait été présenté en premier.'],
             ['Une seule','Il a tenu l\'affiche à Sherbrooke, <b>où</b> il avait été présenté en premier.'],
             ['Les mots qui l\'annoncent','une ville, un village, une salle, une maison, un endroit', true],
             ['Ce que ça remplace','« dans cette ville », « à cet endroit-là »']],
       say:"Il a tenu l'affiche à Sherbrooke, où il avait été présenté en premier.",
       note:"« Où » évite de répéter le nom du lieu. Sans lui, il faut écrire « dans cette ville », ce qui alourdit tout de suite."},

      {t:'ana', h:"Le temps",
       p:"Le mot qui précède « où » désigne un moment.",
       mots:[['Deux phrases','Elle cessa de tourner en 2007. Cette année-là, elle commença à enseigner.'],
             ['Une seule','2007 est l\'année <b>où</b> elle cessa de tourner.'],
             ['Les mots qui l\'annoncent','une année, un jour, un matin, un moment, une époque', true],
             ['Attention','on ne dit pas « l\'année quand » ni « le jour que » : c\'est « où »']],
       say:"2007 est l'année où elle cessa de tourner.",
       note:"C'est la faute la plus fréquente à ce niveau : « le jour que je suis arrivée ». La forme juste est « le jour où je suis arrivée »."},

      {t:'ex', h:"Six phrases réunies",
       p:"À gauche deux phrases, à droite une seule.",
       rows:[
         ["Elle est née dans une famille. Personne n'y allait au cinéma.","une famille où personne n'allait au cinéma"],
         ["Elle est entrée dans une salle de montage. Elle y a appris son métier.","la salle de montage où elle a appris son métier"],
         ["Le film est sorti en 1994. Cette année-là…","1994, l'année où le film est sorti"],
         ["Il y a un moment. L'image devient plus froide à ce moment-là.","un moment où l'image devient plus froide"],
         ["Estelle revient au village. Elle avait grandi là.","le village où elle avait grandi"],
         ["L'autobus est tombé en panne ce jour-là.","le jour où l'autobus est tombé en panne"],
       ]},

      {t:'piege', h:"Deux confusions",
       rows:[
         ["« le jour que je suis arrivée »","« le jour où je suis arrivée »",
          "Avec un mot de temps, c'est « où » et jamais « que ». C'est la faute la plus fréquente au niveau 6."],
         ["« ou » sans accent","« où » avec accent",
          "« Ou » veut dire « l'un ou l'autre » : mercredi ou jeudi. « Où » est le relatif, ou la question « où est-il ? ». Un seul accent, deux sens sans rapport."],
       ]},

      {t:'check', h:"Est-ce que c'est clair maintenant ?",
       p:"Quatre questions rapides.",
       qs:[
         {q:"Dans « l'année où elle cessa de tourner », « où » désigne…", opts:["un lieu","un moment"], ok:1,
          fb:"Le mot qui précède est « année » : c'est du temps."},
         {q:"Pour savoir lequel des deux, il faut regarder…", opts:["le mot juste avant","le verbe qui suit"], ok:0,
          fb:"Une ville → lieu ; une année → temps."},
         {q:"« Le jour que je suis arrivée » est…", opts:["correct","fautif"], ok:1,
          fb:"Avec un mot de temps, c'est « où »."},
         {q:"« Tu viens mercredi ou jeudi » s'écrit…", opts:["ou, sans accent","où, avec accent"], ok:0,
          fb:"Ici, c'est « l'un ou l'autre » : pas d'accent."},
       ]},

      {t:'revoir', h:"À retenir",
       p:"<b>Où</b> remplace un complément de <b>lieu</b> (la ville où…) ou de <b>temps</b> (l'année où…). Le mot juste avant dit lequel. Jamais « le jour que » : toujours « le jour où »."},
    ]
  },

  t2repr: {
    eye:'Mini-leçon', tit:"Le, en, y : ne pas répéter sans perdre le lecteur",
    blocs:[
      {t:'texte', h:"Trois mots de deux lettres qui font tomber les lecteurs",
       p:"Un texte bien écrit ne répète pas. À la place, il pose « le », « en » ou « y », et il compte sur vous pour retrouver de quoi il parle. Ça marche très bien en langue maternelle, où on le fait sans y penser. En français appris, c'est le premier endroit où l'on décroche — et on ne s'en aperçoit pas, parce qu'on continue de lire.",
       note:"Le programme y consacre quatre savoirs d'un coup : associer « le » à son référent, associer « en » à son référent, associer « où » à son antécédent, et employer des procédés de substitution lexicale."},

      {t:'ana', h:"Chacun remplace un genre de groupe précis",
       p:"Ils ne sont pas interchangeables : c'est ce qui permet de deviner juste.",
       mots:[['<b>le</b>','remplace <b>toute une idée</b>, une subordonnée complète — Elle a appris son métier au montage. Elle <b>le</b> répète partout.'],
             ['<b>en</b>','remplace un groupe avec <b>de</b> — Elle parle rarement de son court métrage. Elle n\'<b>en</b> parle qu\'à ses étudiants.'],
             ['<b>y</b>','remplace un groupe avec <b>à</b> ou un <b>lieu</b> — Une rétrospective eut lieu à la salle. Elle <b>y</b> vint.', true],
             ['Le geste','reculer d\'une phrase, et chercher un groupe qui commence par « de » ou par « à »']],
       say:"le remplace une idée, en remplace un groupe avec de, y remplace un lieu ou un groupe avec à",
       note:"Si vous ne trouvez pas le référent dans la phrase d'avant, ce n'est presque jamais vous : c'est le texte qui est mal écrit."},

      {t:'ana', h:"La substitution lexicale : reprendre par un autre mot",
       p:"L'autre façon de ne pas se répéter, et celle qui distingue un texte adulte d'un texte d'école.",
       mots:[['Par un synonyme','le film → l\'œuvre → ce long métrage'],
             ['Par un mot plus général','les Marées de novembre → ce film → cette histoire'],
             ['Par une nominalisation','elle a cessé de tourner → cet arrêt, cette décision', true],
             ['Le risque','changer de mot au point qu\'on ne sache plus de quoi on parle']],
       say:"le film, l'œuvre, ce long métrage, cette histoire, cette décision",
       note:"Deux reprises différentes suffisent. À la troisième, le lecteur commence à se demander si vous parlez encore de la même chose."},

      {t:'ex', h:"Six reprises de la biographie",
       p:"À gauche le petit mot, à droite ce qu'il remplace.",
       rows:[
         ["Elle <b>y</b> resta onze ans.","dans la salle de montage"],
         ["Elle <b>y</b> vint, et elle refusa de parler.","à la salle Beauchemin"],
         ["Le public, lui, <b>revint</b>.","le public, repris par « lui » pour l'opposer à la critique"],
         ["Elle <b>le</b> répète dans chaque entrevue.","qu'elle a appris son métier au montage"],
         ["Elle n'<b>en</b> parle qu'à ses étudiants.","de son premier court métrage"],
         ["Bruno <b>en</b> a compté quatre.","des retours en arrière"],
       ]},

      {t:'check', h:"Est-ce que c'est clair maintenant ?",
       p:"Quatre questions rapides.",
       qs:[
         {q:"« Elle y vint » — « y » remplace…", opts:["un lieu","une personne"], ok:0,
          fb:"« Y » remplace un lieu, ou un groupe avec « à »."},
         {q:"« Elle n'en parle qu'à ses étudiants » — « en » remplace…", opts:["un groupe avec « de »","un groupe avec « à »"], ok:0,
          fb:"Parler DE quelque chose → en."},
         {q:"« Elle le répète partout » — « le » remplace…", opts:["un objet","toute une idée"], ok:1,
          fb:"Une subordonnée complète : qu'elle a appris son métier au montage."},
         {q:"Pour retrouver le référent, on recule…", opts:["d'une phrase","au début du texte"], ok:0,
          fb:"Presque toujours la phrase d'avant, jamais plus loin."},
       ]},

      {t:'revoir', h:"À retenir",
       p:"<b>le</b> = toute une idée · <b>en</b> = un groupe avec « de » · <b>y</b> = un lieu ou un groupe avec « à ». Et pour éviter la répétition d'un nom : un synonyme, un mot plus général — deux fois, pas trois."},
    ]
  },

  t2idees: {
    eye:'Mini-leçon', tit:"L'idée principale, et tout le reste",
    blocs:[
      {t:'texte', h:"Résumer, c'est jeter",
       p:"Un résumé n'est pas un texte plus court : c'est un texte dont on a retiré les détails. Encore faut-il savoir lesquels sont des détails. Le test est simple et il ne se discute pas : retirez la phrase. Si le paragraphe tient encore debout, c'était un détail.",
       note:"C'est ce savoir qui rend possible la production écrite du module : raconter un film en deux paragraphes suppose d'avoir jeté les trois quarts."},

      {t:'ana', h:"Les reconnaître",
       p:"Deux questions, et on a fini.",
       mots:[['L\'idée principale','répond à : de quoi parle ce paragraphe ?'],
             ['Le détail','répond à : quand ? combien ? où exactement ?'],
             ['Le test du retrait','enlevez la phrase ; si rien ne s\'écroule, c\'était un détail', true],
             ['La place habituelle','l\'idée principale ouvre souvent le paragraphe — souvent, pas toujours']],
       say:"De quoi parle ce paragraphe ? Quand ? Combien ? Où exactement ?",
       note:"Un chiffre est presque toujours un détail. Presque : « onze ans de montage » porte tout le paragraphe, parce que c'est ce qui explique la suite."},

      {t:'ex', h:"Un paragraphe, trié",
       p:"À gauche la phrase, à droite ce qu'elle est.",
       rows:[
         ["Elle a appris son métier au montage, et non dans une école.","idée principale — tout le paragraphe y mène"],
         ["Elle est née à Rimouski en 1951.","détail — la date situe, elle n'explique rien"],
         ["Son premier long métrage n'est venu qu'après quinze ans.","idée principale — c'est le fait du paragraphe"],
         ["Le court métrage durait douze minutes.","détail — on peut l'enlever"],
         ["La critique fut sévère, mais le public est revenu.","idée principale — l'opposition est le sujet"],
         ["Le film est sorti dans huit salles.","détail — il précise, il ne porte pas"],
       ]},

      {t:'piege', h:"Deux erreurs de tri",
       rows:[
         ["garder tous les chiffres","garder ceux qui expliquent",
          "Onze ans de montage explique la forme du film : on le garde. Huit salles ne fait que préciser : on le jette."],
         ["prendre la première phrase pour l'idée principale","faire le test du retrait",
          "C'est souvent vrai, et c'est parfois faux. Le test, lui, ne se trompe pas."],
       ]},

      {t:'check', h:"Est-ce que c'est clair maintenant ?",
       p:"Quatre questions rapides.",
       qs:[
         {q:"Le test le plus sûr, c'est…", opts:["retirer la phrase et voir","compter les mots"], ok:0,
          fb:"Si le paragraphe tient encore, c'était un détail."},
         {q:"« Le film est sorti dans huit salles » est…", opts:["une idée principale","un détail"], ok:1,
          fb:"Ça précise, ça ne porte pas le paragraphe."},
         {q:"Un chiffre est…", opts:["toujours un détail","souvent un détail, pas toujours"], ok:1,
          fb:"Onze ans de montage explique la forme du film."},
         {q:"Résumer, c'est surtout…", opts:["raccourcir les phrases","jeter les détails"], ok:1,
          fb:"Un résumé n'est pas un texte plus court : c'est un texte trié."},
       ]},

      {t:'revoir', h:"À retenir",
       p:"L'<b>idée principale</b> répond à « de quoi parle ce paragraphe ? ». Le <b>détail</b> précise, date, chiffre. Le test : retirez la phrase — si rien ne s'écroule, c'était un détail."},
    ]
  },

  t3texte: {
    eye:'Mini-leçon', tit:"Lire une critique : ce qu'elle dit, pas ce qu'on croit",
    blocs:[
      {t:'texte', h:"On répond presque toujours à la mauvaise phrase",
       p:"Quand un texte nous contrarie, on lit vite et on retient une version un peu plus grosse que l'original. Charbonneau n'a pas écrit que la voisine est inutile : il a écrit qu'elle arrive trop tard. Ce n'est pas la même chose, et c'est beaucoup plus difficile à contredire. Lire une critique, c'est d'abord repérer ce qu'elle reproche exactement.",
       note:"Le module est bâti sur une critique inventée, signée d'un nom inventé, à propos d'un film inventé. La méthode, elle, s'applique à n'importe quel texte d'opinion."},

      {t:'ana', h:"Trois façons de dire du mal sans le dire",
       p:"Un critique expérimenté évite les mots durs : ils sont trop faciles à réfuter.",
       mots:[['Les guillemets de distance','un film qu\'on dit <b>« ambitieux »</b> — le mot est là, mais l\'auteur ne le reprend pas à son compte'],
             ['La comparaison','<b>avance à la vitesse d\'un déménagement</b> — jamais le mot « lent », et pourtant on l\'a compris'],
             ['Le compliment retourné','un beau film <b>qui a manqué de peu d\'être un grand film</b>', true],
             ['Ce qu\'il ne fait jamais','écrire « c\'est mauvais » — une phrase qu\'on peut lui renvoyer telle quelle']],
       say:"un film qu'on dit ambitieux, avance à la vitesse d'un déménagement, un beau film qui a manqué d'être un grand film",
       note:"Les guillemets autour d'un seul mot sont le procédé le plus fréquent, et le plus facile à manquer quand on lit vite."},

      {t:'ana', h:"Les trois questions à se poser sur un reproche",
       p:"Avant de répondre à quelqu'un, savoir précisément ce qu'il a dit.",
       mots:[['Sur quoi porte-t-il ?','un moment du film, un personnage, une forme — jamais une personne'],
             ['Est-il vérifiable ?','« la première demi-heure est lente » se vérifie ; « ça manque d\'âme » ne se vérifie pas'],
             ['Est-il assumé ?','« mon vrai reproche est ailleurs » — il annonce lui-même ce qui compte', true],
             ['Ce qu\'on peut en faire','accorder ce qui est vérifiable, discuter le reste']],
       say:"Sur quoi porte-t-il ? Est-il vérifiable ? Est-il assumé ?",
       note:"Un reproche vérifiable est un cadeau : on peut lui accorder un point et garder tout le reste de son avis."},

      {t:'ex', h:"Ce qu'il écrit, et ce qu'on croit qu'il écrit",
       p:"À gauche la version rapide, à droite le texte exact.",
       rows:[
         ["« Il dit que le film est mauvais. »","« un film qu'on dit ambitieux, faute de savoir quoi en dire »"],
         ["« Il dit que le début est ennuyant. »","« sa première demi-heure avance à la vitesse d'un déménagement »"],
         ["« Il dit que c'est une maladresse. »","« on comprend que ce n'est pas une maladresse : c'est un parti pris »"],
         ["« Il dit que les retours en arrière sont ratés. »","« ils sont amenés si discrètement qu'on met vingt minutes à comprendre »"],
         ["« Il dit que la voisine est inutile. »","« le personnage de la voisine arrive trop tard »"],
         ["« Il dit qu'il a détesté. »","« un beau film qui a manqué de peu d'être un grand film »"],
       ]},

      {t:'check', h:"Est-ce que c'est clair maintenant ?",
       p:"Quatre questions rapides.",
       qs:[
         {q:"Des guillemets autour d'un seul mot veulent souvent dire…", opts:["que le mot est important","que l'auteur ne le prend pas à son compte"], ok:1,
          fb:"C'est une façon polie de refuser le mot."},
         {q:"« Arrive trop tard » et « est inutile »…", opts:["disent la même chose","ne disent pas la même chose"], ok:1,
          fb:"Le premier vise un moment, le second un personnage."},
         {q:"Un reproche vérifiable, c'est…", opts:["un cadeau","un piège"], ok:0,
          fb:"On peut lui accorder un point et garder le reste de son avis."},
         {q:"« Un beau film qui a manqué d'être un grand film » est…", opts:["un compliment franc","un reproche présenté en compliment"], ok:1,
          fb:"C'est le procédé le plus poli, et le plus dur."},
       ]},

      {t:'revoir', h:"À retenir",
       p:"Avant de répondre à une critique : <b>relire la phrase exacte</b>. Repérer les <b>guillemets de distance</b>, les <b>comparaisons</b> et les <b>compliments retournés</b>. Puis se demander sur quoi le reproche porte, et s'il est vérifiable."},
    ]
  },

  t3adj: {
    eye:'Mini-leçon', tit:"Un grand film, un film grand",
    blocs:[
      {t:'texte', h:"La place d'un mot, et tout le sens change",
       p:"« Un grand film » et « un film grand » ne veulent pas dire la même chose. Le premier parle d'importance, le second de taille. Une poignée d'adjectifs se comportent ainsi, et ce sont justement ceux qui reviennent dans les critiques et dans les conversations sur les œuvres. Les connaître, c'est éviter de dire le contraire de ce qu'on pense.",
       note:"Le programme les nomme : grand, propre, drôle, ancien, nouveau. Cinq mots, et c'est tout — mais ils sont partout."},

      {t:'ana', h:"Les cinq, avant et après",
       p:"Avant le nom : un jugement, un rang. Après le nom : ce qui se mesure ou se voit.",
       mots:[['grand','un <b>grand</b> film (important) · un homme <b>grand</b> (sa taille)'],
             ['ancien','une <b>ancienne</b> salle (elle ne l\'est plus) · une salle <b>ancienne</b> (vieille)'],
             ['drôle','un <b>drôle</b> de personnage (étrange) · un personnage <b>drôle</b> (qui fait rire)', true],
             ['propre','sa <b>propre</b> règle (la sienne) · une salle <b>propre</b> (bien nettoyée)'],
             ['nouveau','son <b>nouveau</b> film (le dernier) · un film <b>nouveau</b> (d\'un genre inédit)']],
       say:"un grand film, un homme grand, une ancienne salle, une salle ancienne, un drôle de personnage, un personnage drôle",
       note:"« Sa propre règle » revient dans ce module : la réalisatrice casse sa propre règle une fois. Ça ne veut pas dire que la règle est bien nettoyée."},

      {t:'ana', h:"La règle sous la règle",
       p:"Elle marche pour ces cinq-là, et elle explique aussi les autres adjectifs.",
       mots:[['Après le nom','ce qui se mesure, se voit, se vérifie — la couleur, la taille, l\'âge, la nationalité'],
             ['Avant le nom','ce qui juge ou classe — beau, joli, bon, mauvais, grand, petit'],
             ['Le déplacement','déplacer l\'adjectif, c\'est passer du mesurable au jugement', true],
             ['Le test','« Est-ce que je peux le mesurer ? » Si oui, il passe après.']],
       say:"Ce qui se mesure passe après le nom ; ce qui juge passe avant.",
       note:"Un film long dure longtemps ; un long film aussi, mais avec un soupçon de reproche. La nuance est faible ici, forte pour les cinq de la liste."},

      {t:'ex', h:"Six groupes, six sens",
       p:"À gauche le groupe, à droite ce qu'il veut dire.",
       rows:[
         ["un grand film","un film qui compte, marquant"],
         ["un film long","un film qui dure, en minutes"],
         ["une ancienne salle de cinéma","un local qui n'est plus une salle"],
         ["une salle ancienne","une salle vieille, construite il y a longtemps"],
         ["un drôle de personnage","un personnage étrange, difficile à situer"],
         ["un personnage drôle","un personnage qui fait rire"],
       ]},

      {t:'piege', h:"Deux malentendus",
       rows:[
         ["« sa propre règle » compris comme « sa règle bien nettoyée »","« sa règle à elle »",
          "Avant le nom, « propre » veut dire « qui appartient à ». Après, il veut dire « pas sale »."],
         ["« un drôle de film » pour dire « un film amusant »","« un film drôle »",
          "« Un drôle de film » veut dire un film bizarre. On peut vexer quelqu'un sans le vouloir."],
       ]},

      {t:'check', h:"Est-ce que c'est clair maintenant ?",
       p:"Quatre questions rapides.",
       qs:[
         {q:"« Une ancienne salle de cinéma » veut dire…", opts:["une salle vieille","un local qui n'en est plus une"], ok:1,
          fb:"Avant le nom, « ancien » veut dire « qui ne l'est plus »."},
         {q:"« Un drôle de personnage » veut dire…", opts:["un personnage étrange","un personnage amusant"], ok:0,
          fb:"Amusant, ce serait « un personnage drôle »."},
         {q:"Un adjectif qui se mesure se place…", opts:["avant le nom","après le nom"], ok:1,
          fb:"La taille, la couleur, l'âge : après."},
         {q:"« Sa propre règle » veut dire…", opts:["sa règle à elle","une règle bien nettoyée"], ok:0,
          fb:"Avant le nom, « propre » marque l'appartenance."},
       ]},

      {t:'revoir', h:"À retenir",
       p:"Cinq adjectifs changent de sens selon leur place : <b>grand, ancien, drôle, propre, nouveau</b>. Avant le nom, ils jugent ou classent ; après, ils décrivent ce qui se mesure."},
    ]
  },

  t3subj: {
    eye:'Mini-leçon', tit:"Le subjonctif après un verbe introducteur",
    blocs:[
      {t:'texte', h:"Ce n'est pas un temps, c'est une conséquence",
       p:"On n'emploie pas le subjonctif parce qu'on veut : on l'emploie parce qu'un certain verbe, suivi de « que », l'oblige. Il faut que, je veux que, je doute que, il vaut mieux que. Le verbe commande, et le subjonctif suit. C'est pour ça qu'on l'apprend par la liste des verbes, jamais par le sens.",
       note:"Le programme du niveau 6 le dit ainsi : employer obligatoirement le subjonctif présent après quelques verbes introducteurs usuels + que."},

      {t:'ana', h:"Comment on le fabrique",
       p:"Une seule règle, et quatre irréguliers à savoir par cœur.",
       mots:[['Le point de départ','la 3e personne du pluriel du présent : ils <b>viennent</b>, ils <b>prennent</b>'],
             ['On enlève -ent','que je vien<b>ne</b>, que tu prenn<b>es</b>, qu\'elle arriv<b>e</b>'],
             ['Les quatre irréguliers','être → que je <b>sois</b> · avoir → que j\'<b>aie</b> · aller → que j\'<b>aille</b> · faire → que je <b>fasse</b>', true],
             ['À l\'oreille','pour beaucoup de verbes, le subjonctif se dit comme le présent : qu\'elle arrive, elle arrive']],
       say:"que je vienne, que tu prennes, que je sois, que j'aie, que j'aille, que je fasse",
       note:"C'est une bonne nouvelle : pour la majorité des verbes en -er, personne n'entend la différence. Le subjonctif ne s'entend vraiment que sur les quatre irréguliers."},

      {t:'ana', h:"Les verbes qui le demandent, et ceux qui trompent",
       p:"Cette liste-là est courte. Apprenez-la, et vous aurez fait quatre-vingts pour cent du travail.",
       mots:[['Ils le demandent','il faut que · il vaut mieux que · je veux que · je souhaite que · je doute que'],
             ['Ils ne le demandent pas','je pense que · je crois que · j\'espère que · il paraît que'],
             ['Le piège de la négation','je ne crois pas que… le demande, alors que je crois que… ne le demande pas', true],
             ['Ce qu\'il ne dit jamais','le futur — « il faut qu\'elle arrive » ne parle pas de demain']],
       say:"il faut que, il vaut mieux que, je veux que, je doute que, je pense que, je crois que",
       note:"« J'espère que » ne demande pas le subjonctif, alors que « je souhaite que » le demande. C'est arbitraire, et il n'y a rien à comprendre : c'est à retenir."},

      {t:'ex', h:"Six phrases du module",
       p:"À gauche le verbe introducteur, à droite la phrase entière.",
       rows:[
         ["il faut que","Il faut que la voisine arrive tard."],
         ["je doute que","Je doute que le public ait appris ces signaux."],
         ["il vaut mieux que","Il vaut mieux que tu voies le film avant de lire la critique."],
         ["il souhaite que","Bruno souhaite que Thérèse écrive au journal."],
         ["il faudrait qu'on","Il faudrait qu'on soit plus attentif au son."],
         ["je pense que","Je pense que le personnage est nécessaire. — pas de subjonctif"],
       ]},

      {t:'piege', h:"Deux fautes fréquentes",
       rows:[
         ["« je pense qu'elle soit nécessaire »","« je pense qu'elle est nécessaire »",
          "« Penser que » et « croire que » ne demandent pas le subjonctif. C'est l'erreur la plus courante à ce niveau, et elle vient d'une bonne intention."],
         ["« il faut qu'elle arrivera »","« il faut qu'elle arrive »",
          "Le subjonctif ne connaît pas le futur. « Il faut que » parle de ce qui est nécessaire, pas de demain."],
       ]},

      {t:'check', h:"Est-ce que c'est clair maintenant ?",
       p:"Quatre questions rapides.",
       qs:[
         {q:"Après « il faut que », on emploie…", opts:["le subjonctif","le futur"], ok:0,
          fb:"Il faut qu'elle arrive, jamais « qu'elle arrivera »."},
         {q:"Après « je pense que », on emploie…", opts:["le subjonctif","l'indicatif"], ok:1,
          fb:"Je pense qu'elle est nécessaire."},
         {q:"« que je fasse » vient du verbe…", opts:["faire","falloir"], ok:0,
          fb:"C'est l'un des quatre irréguliers à retenir."},
         {q:"On fabrique le subjonctif à partir de…", opts:["la 3e personne du pluriel du présent","l'infinitif"], ok:0,
          fb:"Ils viennent → que je vienne."},
       ]},

      {t:'revoir', h:"À retenir",
       p:"Le subjonctif suit certains verbes + <b>que</b> : il faut que, il vaut mieux que, je veux que, je doute que. Il ne suit <b>pas</b> je pense que, je crois que, j'espère que. Quatre irréguliers : <b>sois, aie, aille, fasse</b>."},
    ]
  },

  t3si: {
    eye:'Mini-leçon', tit:"Poser une condition avec « si »",
    blocs:[
      {t:'texte', h:"La conjonction qui permet de discuter sans se fâcher",
       p:"« Si on manque le signal une fois, on se perd pour vingt minutes. » Cette phrase dit exactement la même chose que « celui qui n'a pas compris n'a pas regardé », mais elle ne vise personne : elle pose une condition. C'est ce qui la rend discutable — et une opinion qu'on peut discuter vaut mieux qu'une opinion qui ferme la porte.",
       note:"Le programme demande deux choses : comprendre l'hypothèse réaliste sur un fait passé (si + passé composé) et employer l'hypothèse réaliste sur un fait présent ou à venir (si + présent)."},

      {t:'ana', h:"Les deux formes réalistes",
       p:"Réaliste veut dire : ça peut arriver, ou c'est peut-être arrivé.",
       mots:[['Sur le présent ou l\'avenir','<b>si + présent</b>, puis présent ou futur — Si tu <b>manques</b> le signal, tu <b>te perds</b>.'],
             ['Sur le passé','<b>si + passé composé</b>, puis présent ou futur — Si tu <b>as lu</b> la critique, tu <b>regardes</b> le film autrement.'],
             ['Jamais de futur après « si »','on n\'écrit pas « si tu manqueras »', true],
             ['Ce qui suit, lui, peut être au futur','Si tu écris au journal, ils <b>publieront</b> ta lettre.']],
       say:"Si tu manques le signal, tu te perds. Si tu as lu la critique, tu regardes le film autrement.",
       note:"La faute « si + futur » est la plus fréquente de toutes, à tous les niveaux, et elle s'entend immédiatement."},

      {t:'ana', h:"Le « si » qui n'est pas une condition",
       p:"Le même mot introduit aussi une question rapportée — et là, le futur est permis.",
       mots:[['Une condition','<b>Si</b> tu écris au journal, ils publieront ta lettre.'],
             ['Une question rapportée','Je me demande <b>si</b> le journal publiera ma lettre.'],
             ['Comment les distinguer','la question rapportée suit un verbe comme se demander, savoir, ignorer', true],
             ['Ce que ça change','dans la question rapportée, le futur est permis et souvent nécessaire']],
       say:"Si tu écris au journal, ils publieront ta lettre. Je me demande si le journal publiera ma lettre.",
       note:"C'est le même mot et deux emplois sans rapport. Le verbe qui précède dit lequel."},

      {t:'ex', h:"Six hypothèses du module",
       p:"À gauche la condition, à droite la conséquence.",
       rows:[
         ["Si tu manques le bruit de la mer","tu ne sais plus en quelle année tu es"],
         ["Si le public n'a jamais appris ces signaux","il ne peut pas les reconnaître"],
         ["Si tu lis la critique avant la projection","tu regarderas le film autrement"],
         ["Si on rate le signal une seule fois","on se perd pour vingt minutes"],
         ["Si Thérèse écrit au journal","ils publieront sa réponse"],
         ["Je me demande si le journal","publiera sa lettre la semaine prochaine"],
       ]},

      {t:'piege', h:"La faute à ne plus faire",
       rows:[
         ["« si tu manqueras le signal »","« si tu manques le signal »",
          "Jamais de futur après « si » quand il pose une condition. C'est la faute la plus fréquente et la plus audible."],
         ["« si vous n'avez pas compris, c'est que vous n'avez pas regardé »","« si on les manque une fois, on se perd »",
          "La première vise la personne et ferme la discussion ; la seconde pose une condition et laisse répondre. Grammaticalement, les deux sont justes."],
       ]},

      {t:'check', h:"Est-ce que c'est clair maintenant ?",
       p:"Quatre questions rapides.",
       qs:[
         {q:"Après « si » qui pose une condition, on met…", opts:["le présent","le futur"], ok:0,
          fb:"Si tu manques, jamais « si tu manqueras »."},
         {q:"« Je me demande si elle reviendra » est…", opts:["une condition","une question rapportée"], ok:1,
          fb:"Après « se demander », le futur est permis."},
         {q:"La conséquence, elle, peut être…", opts:["au futur","jamais au futur"], ok:0,
          fb:"Si tu écris, ils publieront."},
         {q:"Poser une condition plutôt qu'accuser permet…", opts:["de fermer la discussion","de laisser répondre"], ok:1,
          fb:"C'est tout l'intérêt de « si » dans une discussion."},
       ]},

      {t:'revoir', h:"À retenir",
       p:"<b>Si + présent</b> → présent ou futur. <b>Si + passé composé</b> → présent ou futur. <b>Jamais de futur après « si »</b> quand il pose une condition. Après « je me demande si », le futur est permis."},
    ]
  },

  t3guill: {
    eye:'Mini-leçon', tit:"Accorder un point, puis répondre",
    blocs:[
      {t:'texte', h:"Ce qui distingue un avis d'une humeur",
       p:"Un avis qu'on peut discuter a trois marques : il s'annonce comme un avis, il accorde quelque chose à l'autre, et il s'appuie sur un moment précis. Sans la première, il se lit comme un fait. Sans la deuxième, il se lit comme une attaque. Sans la troisième, il ne se lit pas du tout.",
       note:"C'est ici que le niveau 6 se sépare du niveau 5. Au 5, on dit ce qu'on a aimé et pourquoi. Au 6, on tient un avis nuancé devant quelqu'un qui n'est pas d'accord."},

      {t:'ana', h:"Annoncer que ce qui suit est un avis",
       p:"Quatre formules, et la différence entre un fait et une opinion devient visible.",
       mots:[['Les plus courantes','<b>à mon avis</b> · <b>pour ma part</b> · <b>personnellement</b> · <b>je trouve que</b>'],
             ['Ce qu\'elles font','elles préviennent le lecteur : ce qui suit n\'est pas vérifiable'],
             ['Sans elles','« La voisine arrive au bon moment » se lit comme un fait, et se conteste comme un fait', true],
             ['Où les placer','en tête de phrase, presque toujours']],
       say:"à mon avis, pour ma part, personnellement, je trouve que",
       note:"Ce n'est pas de la modestie : c'est de la précision. Annoncer un avis, c'est dire à l'autre où il peut vous contredire."},

      {t:'ana', h:"Accorder un point, et concéder",
       p:"Le geste qui donne du poids à tout ce qui suit.",
       mots:[['Accorder','<b>c\'est vrai que</b>… · <b>j\'admets que</b>… · <b>il a raison sur</b>…'],
             ['Puis retourner','<b>mais</b> · <b>par contre</b> · <b>en revanche</b> · <b>cela dit</b>'],
             ['Concéder sans changer d\'avis','<b>même si</b>… · <b>bien que</b>… · <b>quand même</b>', true],
             ['Pourquoi ça marche','celui qui vient d\'être approuvé écoute la suite ; celui qui vient d\'être contredit prépare sa réponse']],
       say:"C'est vrai que le début est lent, mais c'est un parti pris.",
       note:"« Bien que » demande le subjonctif : bien que le début soit lent. « Même si » demande l'indicatif : même si le début est lent."},

      {t:'ana', h:"Les guillemets qui prennent une distance",
       p:"Le troisième outil, plus discret, et qui se lit plus qu'il ne s'écrit.",
       mots:[['Autour d\'une phrase entière','ce sont les <b>mots exacts</b> de quelqu\'un — il écrit : « mon vrai reproche est ailleurs »'],
             ['Autour d\'un seul mot','l\'auteur <b>ne le prend pas à son compte</b> — un film qu\'on dit « ambitieux »'],
             ['Comment les distinguer','une citation est annoncée : deux points, « il écrit », « selon lui »', true],
             ['À l\'écrit, prudence','un mot entre guillemets se voit ; employé à tort, il passe pour de l\'ironie']],
       say:"Il écrit : mon vrai reproche est ailleurs. Un film qu'on dit ambitieux.",
       note:"À l'oral, on ne les entend pas — d'où « entre guillemets », qu'on dit à voix haute pour les rendre audibles."},

      {t:'ex', h:"Six intentions, six formules",
       p:"À gauche ce qu'on veut faire, à droite comment on le dit.",
       rows:[
         ["annoncer un avis","Pour ma part, je trouve que la lenteur est voulue."],
         ["accorder un point avant de répondre","C'est vrai que la première demi-heure est lente, mais…"],
         ["mettre un mot à distance","un film qu'on dit « ambitieux »"],
         ["concéder sans changer d'avis","Même si les signaux sont discrets, ils existent."],
         ["citer les mots exacts","Il écrit : « mon vrai reproche est ailleurs »."],
         ["fermer la discussion — à éviter","Si vous n'avez pas compris, c'est que vous n'avez pas regardé."],
       ]},

      {t:'piege', h:"Deux façons de perdre son interlocuteur",
       rows:[
         ["« il a tort »","« il a raison sur la lenteur, mais pas sur les signaux »",
          "Contredire en bloc oblige l'autre à tout défendre. Accorder un point ouvre une vraie discussion."],
         ["« celui qui n'a pas compris n'a pas regardé »","« si on manque le signal, on se perd »",
          "La première phrase ne se répond pas. Un avis auquel on ne peut rien répondre n'est plus une opinion : c'est une fin de discussion."],
       ]},

      {t:'check', h:"Est-ce que c'est clair maintenant ?",
       p:"Quatre questions rapides.",
       qs:[
         {q:"« Pour ma part » sert à…", opts:["annoncer un avis","citer quelqu'un"], ok:0,
          fb:"Elle prévient : ce qui suit n'est pas un fait."},
         {q:"Accorder un point avant de répondre…", opts:["affaiblit ce qu'on dit","donne du poids à la suite"], ok:1,
          fb:"Celui qui vient d'être approuvé écoute la suite."},
         {q:"« Bien que le début soit lent » emploie…", opts:["le subjonctif","l'indicatif"], ok:0,
          fb:"« Bien que » demande le subjonctif ; « même si » demande l'indicatif."},
         {q:"Des guillemets autour d'un seul mot disent…", opts:["que le mot est important","que l'auteur ne le reprend pas à son compte"], ok:1,
          fb:"C'est une mise à distance polie."},
       ]},

      {t:'revoir', h:"À retenir",
       p:"Un avis discutable a trois marques : il <b>s'annonce</b> (à mon avis, pour ma part), il <b>accorde un point</b> (c'est vrai que…, mais), et il <b>s'appuie</b> sur un moment précis. Les <b>guillemets</b> autour d'un mot le mettent à distance."},
    ]
  },

};
