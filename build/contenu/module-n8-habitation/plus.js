const PLUS = {

  prInto: {
    eye:'Mini-leçon', tit:"Trois mélodies pour un même refus",
    blocs:[
      {t:'texte', h:"Le programme du niveau 8 ne demande plus qu'une chose à la voix",
       p:"Aucun son nouveau, aucune liaison de plus : une <b>mélodie</b>. À ce stade, votre prononciation vous fait comprendre, et ce n'est plus là que se joue votre crédibilité. Elle se joue dans la courbe que suit votre voix pendant les six mots d'une phrase — parce que c'est la seule chose dont votre interlocuteur se souviendra dix minutes plus tard.",
       note:"On croit souvent qu'une voix égale est une voix calme. Au téléphone, elle s'entend comme une voix qui n'y tient pas."},

      {t:'texte', h:"Pourquoi ça décide de la suite d'un dossier",
       p:"La personne qui vous répond traite trente appels par jour et décide, en deux minutes, si votre affaire mérite une note au registre. Elle ne retiendra ni votre numéro de dossier ni vos montants. Elle retiendra si vous aviez l'air de quelqu'un qui rappellera. Dire « je conteste cette décision » d'une voix qui remonte à la fin annonce le contraire des mots employés — et c'est le contraire qui s'entend.",
       note:"Rien à voir avec le volume. Une contestation efficace se dit doucement, mais avec une courbe qui descend."},

      {t:'ana', h:"La surprise — la courbe saute d'un cran à la fin",
       p:"Les premiers mots sont plats, puis les deux ou trois dernières syllabes montent d'un coup, comme une marche. Elle sert quand on répète le mot qui étonne, ou quand on commence par « comment ça ».",
       mots:[['Ce qu\'on dit',"Vous me dites que le drain n'a pas été entretenu ?"],['Le mouvement','une marche vers le haut, sur les derniers mots',true],['Comment la trouver','répétez le mot qui vous étonne']],
       say:"Vous me dites que le drain n'a pas été entretenu ?",
       note:"Si la marche arrive trop tôt, au milieu de la phrase, la surprise devient un reproche — et vous perdez la personne."},

      {t:'ana', h:"L'incompréhension — la courbe se casse au milieu",
       p:"Rien ne monte. Le débit se met à traîner exactement à l'endroit où vous avez décroché, avec un blanc juste avant le mot en cause. C'est le blanc qui fait tout le travail.",
       mots:[['Ce qu\'on dit',"Excusez-moi, le mot « exclusion »… vous l'employez comment ?"],['Le mouvement','un creux, et un blanc avant le mot',true],['Comment la trouver','ralentissez sur un seul mot, pas sur la phrase']],
       say:"Excusez-moi, le mot exclusion, vous l'employez comment ?",
       note:"Cette courbe-là dit « une chose précise m'a manqué ». Dite d'un trait, la même phrase dit « je n'ai rien compris depuis le début »."},

      {t:'ana', h:"La volonté — la courbe descend, et le débit s'alourdit",
       p:"Le contraire exact de la surprise : la voix va vers le bas, les syllabes se séparent, et on marque une pause avant le dernier groupe. C'est la courbe d'une décision déjà prise.",
       mots:[['Ce qu\'on dit','Je veux une réponse écrite, et je l\'aurai.'],['Le mouvement','vers le bas, avec appui sur « veux »',true],['Comment la trouver','dites-la sans sourire, le menton bas']],
       say:"Je veux une réponse écrite, et je l'aurai.",
       note:"La même phrase avec une courbe montante demande la permission de vouloir. C'est le renversement le plus coûteux du module."},

      {t:'ana', h:"La déception — la courbe tombe au premier mot",
       p:"La quatrième, celle qu'on produit rarement et qu'on entend souvent chez l'autre : ça descend dès la première syllabe, sans jamais se relever, et le débit reste très régulier.",
       mots:[['Ce qu\'on dit',"Ah. Je pensais que la facture était au dossier."],['Le mouvement','vers le bas dès le premier son',true],['Comment la trouver','un « ah » ou un « bon » posé devant']],
       say:"Ah. Je pensais que la facture était au dossier.",
       note:"Quand vous l'entendez chez votre interlocuteur, une de vos réponses vient de le contrarier. Il ne vous le dira pas."},

      {t:'labo', h:"Les quatre courbes, à l'écoute",
       p:"Choisissez une intention et un exemple.",
       axes:[
         {id:'i', lbl:'Quelle intention ?', opts:[['a','surprise'],['b','incompréhension'],['c','volonté'],['d','déception']]},
         {id:'n', lbl:'Quel exemple ?', opts:[['1','le premier'],['2','le second']]}],
       out:{
         a1:{w:["Quatre pages ?"], say:"Quatre pages ?", n:'la marche tombe sur « pages »'},
         a2:{w:["Comment ça, la facture n'est pas au dossier ?"], say:"Comment ça, la facture n'est pas au dossier ?", n:'« comment ça » prévient qu\'une marche arrive'},
         b1:{w:["Là, je décroche."], say:"Là, je décroche.", n:'la voix traîne, la courbe se creuse'},
         b2:{w:["Vous avez bien dit soixante jours ?"], say:"Vous avez bien dit soixante jours ?", n:'on met un blanc devant le chiffre douteux'},
         c1:{w:["Je le fais rouvrir, ce dossier-là."], say:"Je le fais rouvrir, ce dossier-là.", n:'vers le bas, syllabes séparées'},
         c2:{w:["Ce sera par écrit, et motivé."], say:"Ce sera par écrit, et motivé.", n:'appui sur « écrit » et sur « motivé »'},
         d1:{w:["Ah. Bon."], say:"Ah. Bon.", n:'deux syllabes qui tombent, et la phrase est inutile'},
         d2:{w:["Je croyais que c'était réglé."], say:"Je croyais que c'était réglé.", n:'vers le bas d\'un bout à l\'autre'},
       },
       note:"Écoutez, puis refaites la courbe en l'exagérant deux fois plus que nécessaire. On réduit ensuite ; on ne trouve jamais une courbe en la murmurant."},

      {t:'ex', h:"Cinq fois presque les mêmes mots",
       p:"À gauche, la phrase. À droite, l'intention que la courbe lui donne.",
       rows:[
         ["La facture n'est pas au dossier ?","surprise — marche vers le haut sur « dossier »"],
         ["La facture n'est pas au dossier.","simple constat — la courbe ne bouge pas"],
         ["La facture n'est pas au dossier…","incompréhension — ça traîne et ça reste ouvert"],
         ["Je veux une réponse écrite.","volonté — vers le bas, chaque mot pèse"],
         ["Je veux une réponse écrite ?","doute — la phrase se retourne contre vous"],
         ["Bon. Je veux une réponse écrite.","abandon — le « bon » tombe avant le reste"],
       ]},

      {t:'piege', h:"Trois courbes qui trahissent, au téléphone",
       rows:[
         ["finir chaque phrase vers le haut","aller vers le bas dès qu'on affirme",
          "Une courbe qui remonte partout change toutes vos affirmations en questions et toutes vos demandes en sollicitations. Ça ne vient pas de la timidité : ça vient de la politesse, qu'on croit devoir mettre dans la voix."],
         ["tenir la même note du début à la fin","bouger sur les trois phrases qui comptent",
          "Une courbe plate ne passe pas pour du sang-froid, elle passe pour du désintérêt. Trois phrases sur un appel de dix minutes suffisent : l'annonce, la demande, le délai."],
         ["s'excuser avec la voix au moment de demander","garder exactement la courbe des phrases précédentes",
          "Beaucoup de gens baissent le volume juste avant leur demande, comme s'ils s'excusaient de la faire. L'autre entend alors une demande déjà négociable, et il la traite comme telle."],
       ]},

      {t:'check', h:"Est-ce que c'est clair maintenant ?",
       p:"Quatre questions pour vérifier.",
       qs:[
         {q:"« Vous me dites que le drain n'a pas été entretenu ? » exprime…", opts:["la surprise","la volonté"], ok:0,
          fb:"La marche vers le haut sur les derniers mots est la signature de la surprise."},
         {q:"Pour la volonté, la courbe…", opts:["remonte à la fin","va vers le bas et s'alourdit"], ok:1,
          fb:"Vers le bas. Une volonté qui remonte demande la permission de vouloir."},
         {q:"Un blanc juste avant un mot, avec un débit qui traîne, exprime…", opts:["l'incompréhension","la déception"], ok:0,
          fb:"Le blanc isole l'endroit exact où vous avez décroché."},
         {q:"Une voix qui ne bouge pas de tout l'appel s'entend comme…", opts:["du sang-froid","du désintérêt"], ok:1,
          fb:"Du désintérêt — même quand ce n'est que de la prudence."},
       ]},

      {t:'revoir', h:"À retenir",
       p:"Quatre courbes : la <b>surprise</b> saute d'un cran sur les derniers mots ; l'<b>incompréhension</b> traîne et laisse un blanc devant le mot en cause ; la <b>volonté</b> va vers le bas et s'alourdit ; la <b>déception</b> tombe au premier son. Pour un appel de contestation, travaillez la troisième — c'est la seule des quatre que vous aurez à produire."},
    ]
  },

  prPqp: {
    eye:'Mini-leçon', tit:"Le plus-que-parfait, ou l'étage du dessous",
    blocs:[
      {t:'texte', h:"Le problème qu'il résout",
       p:"Vous racontez un sinistre. Tout s'est passé au passé — mais pas au même passé. Il y a ce qui s'est produit ce soir-là, et il y a ce qui existait déjà avant. Si vous racontez les deux au passé composé, votre auditeur ne saura pas dans quel ordre les choses sont arrivées, et l'ordre est précisément votre argument. Le plus-que-parfait est l'étage du dessous : il dit ce qui <b>s'était</b> passé avant ce qui <b>s'est</b> passé.",
       note:"Une contestation est un récit ordonné. Celui qui mélange les étages perd son lecteur en trois lignes."},

      {t:'ana', h:"Comment il se forme",
       p:"L'auxiliaire à l'imparfait, plus le participe passé. Rien de neuf : ce sont les mêmes auxiliaires et les mêmes accords qu'au passé composé, seulement décalés d'un cran vers l'arrière.",
       mots:[['Avec avoir',"j'avais nettoyé · nous avions gardé · ils avaient conclu"],['Avec être',"elle était descendue · l'eau était montée",true],['Aux pronominaux',"je m'étais absentée · ils s'étaient plaints"]],
       say:"J'avais nettoyé le drain. L'eau était montée. Je m'étais absentée.",
       note:"Le choix de l'auxiliaire ne change jamais d'un temps à l'autre : ce qui se dit « je suis descendue » se dit « j'étais descendue »."},

      {t:'ana', h:"Premier emploi — l'antériorité dans un récit",
       p:"Deux faits passés, et l'un précède l'autre. Le fait principal se met au passé composé, celui d'avant au plus-que-parfait.",
       mots:[['Le fait principal',"L'eau est montée par le drain."],['Ce qui précède',"L'orage avait duré trois heures.",true],['Ensemble',"L'eau est montée parce que l'orage avait duré trois heures."]],
       say:"L'eau est montée par le drain, parce que l'orage avait duré trois heures.",
       note:"Le mot qui déclenche le plus souvent cet emploi : « parce que », « quand », « après que », « puisque »."},

      {t:'ana', h:"Deuxième emploi — le passé lointain, seul",
       p:"Il n'y a alors aucun autre passé après lui : le plus-que-parfait dit simplement que c'est très ancien, et rangé. C'est la forme des rapports d'expertise quand ils parlent de l'histoire d'un immeuble.",
       mots:[['On dit',"Le drain avait été refait en 2019."],['Ce que ça ajoute','c\'est loin, et c\'est clos',true],['Au présent du récit',"Aujourd'hui, il est libre sur toute sa longueur."]],
       say:"Le drain de fondation avait été refait en 2019, par l'ancien propriétaire.",
       note:"Comparez : « le drain a été refait en 2019 » rattache le fait à aujourd'hui ; « avait été refait » le range dans une autre époque."},

      {t:'ex', h:"Les deux étages, côte à côte",
       p:"À gauche, ce qui s'est passé. À droite, ce qui s'était passé avant.",
       rows:[
         ["J'ai réclamé le 15 septembre.","J'avais pris vingt photographies la veille."],
         ["L'expert est arrivé le 16.","Les boîtes étaient restées deux jours dans l'eau."],
         ["Il a fermé le dossier.","Une entreprise avait nettoyé le drain en mai."],
         ["J'ai compris le motif en octobre.","J'avais reçu le rapport le matin même."],
         ["Le sous-sol s'est inondé.","Rien de tel ne s'était produit en sept ans."],
       ]},

      {t:'piege', h:"Trois pièges d'accord",
       rows:[
         ["l'eau était monté","l'eau était montée",
          "Avec l'auxiliaire <b>être</b>, le participe s'accorde toujours avec le sujet. « L'eau » est féminin singulier : montée."],
         ["la facture que j'avais gardé","la facture que j'avais gardée",
          "Avec <b>avoir</b>, le participe s'accorde avec le complément direct <b>placé avant</b>. Ici « que » remplace « la facture », placée avant : gardée."],
         ["j'avais nettoyée le drain","j'avais nettoyé le drain",
          "Le complément est placé <b>après</b> : aucun accord. C'est le cas le plus fréquent, et c'est celui qu'on sur-corrige."],
       ]},

      {t:'check', h:"Est-ce que c'est clair maintenant ?",
       p:"Trois questions rapides.",
       qs:[
         {q:"« Il a fermé le dossier sans savoir qu'une entreprise ___ le drain. »", opts:["a nettoyé","avait nettoyé"], ok:1,
          fb:"Le nettoyage précède la fermeture : c'est l'étage du dessous."},
         {q:"« Les boîtes ___ deux jours dans l'eau. »", opts:["étaient restées","étaient resté"], ok:0,
          fb:"Auxiliaire être, sujet féminin pluriel : restées."},
         {q:"« Le drain avait été refait en 2019 » signale…", opts:["un passé lointain et clos","un fait tout récent"], ok:0,
          fb:"C'est le second emploi : très ancien, et rangé."},
       ]},

      {t:'revoir', h:"À retenir",
       p:"<b>Auxiliaire à l'imparfait + participe passé.</b> Deux emplois : ce qui s'était passé <b>avant</b> un autre fait passé, et un passé <b>lointain</b> sans suite. Les accords sont ceux du passé composé — être avec le sujet, avoir avec le complément direct placé avant."},
    ]
  },

  t1rap: {
    eye:'Mini-leçon', tit:"Lire un rapport d'expertise",
    blocs:[
      {t:'texte', h:"À qui ce document s'adresse, et pourquoi ça change tout",
       p:"Un rapport d'expertise n'est pas écrit pour vous. Son destinataire est l'assureur qui l'a commandé et payé. Vous le lisez par-dessus l'épaule de quelqu'un — c'est pourquoi il ne s'adresse jamais à vous, ne répond jamais à vos objections, et ne prend jamais la peine d'expliquer un mot. Ce n'est ni de l'arrogance ni de la mauvaise foi : c'est un document professionnel adressé à un professionnel.",
       note:"Le corollaire est encourageant : ce document n'a pas été écrit pour vous convaincre. Il a été écrit pour être exact, et l'exactitude se vérifie."},

      {t:'texte', h:"Sa structure, toujours la même",
       p:"Cinq blocs, dans cet ordre : le <b>mandat</b> (ce qu'on a demandé à l'expert), les <b>constatations</b> (ce qu'il a vu et mesuré), les <b>renseignements obtenus</b> (ce qu'on lui a dit), l'<b>analyse</b> (ce qu'il en déduit) et la <b>conclusion</b>. Repérez ces cinq blocs avant de lire une seule ligne. La conclusion se comprend mal si l'on ne sait pas de quel bloc chaque fait provient.",
       note:"Le mandat est le bloc que personne ne lit, et c'est souvent le plus utile : un expert à qui l'on n'a pas demandé d'inspecter le drain n'a pas inspecté le drain."},

      {t:'ana', h:"Ce qui a été vu — les verbes de constat",
       p:"Le bloc le plus solide, et le plus difficile à contester. L'expert engage sa signature sur ce qu'il affirme avoir vu de ses yeux ou mesuré avec un instrument.",
       mots:[['Les verbes',"j'ai constaté · j'ai mesuré · j'ai photographié · j'ai relevé"],['Ce que ça vaut','beaucoup : c\'est vérifiable',true],['Ce qu\'on en fait','on l\'accepte, et on cherche ce qu\'il ne dit pas']],
       say:"J'ai constaté une ligne de mouillure à quinze centimètres du plancher.",
       note:"On ne conteste pas un constat ; on remarque ce qu'il ne couvre pas. Une ligne de mouillure mesurée ne dit rien de la cause."},

      {t:'ana', h:"Ce qui a été dit — les verbes de rapport",
       p:"L'expert transmet une information qu'il n'a pas vérifiée. Il le signale, discrètement, par une formule et souvent par un conditionnel.",
       mots:[['Les formules',"selon l'assurée · il m'a été rapporté · le service rapporte"],['Le conditionnel',"le drain n'aurait pas été entretenu",true],['Ce que ça vaut','peu, tant que ce n\'est pas confirmé']],
       say:"Selon l'assurée, aucun refoulement ne se serait produit depuis 2019.",
       note:"Ce conditionnel-là n'est pas une politesse : c'est un aveu. Il veut dire « je le rapporte, je ne l'ai pas vérifié »."},

      {t:'ana', h:"Ce qui est déduit — les verbes de précaution",
       p:"Le bloc où tout se joue. L'expert propose une explication, et le vocabulaire de la précaution le dit à chaque ligne.",
       mots:[['Les formules',"il appert que · tout indique que · la cause probable est"],['Les adoucisseurs',"laisse supposer · pourrait résulter de",true],['Ce qu\'on en fait','on l\'oppose à une autre explication']],
       say:"Il appert que l'obstruction s'est formée progressivement, ce qui laisse supposer une absence d'entretien.",
       note:"Une déduction se discute avec une déduction, ou mieux : avec un constat. Une caméra passée dans le tuyau vaut dix « il appert que »."},

      {t:'ex', h:"Trois phrases, trois poids",
       p:"À gauche, la phrase du rapport. À droite, ce qu'elle vaut réellement.",
       rows:[
         ["J'ai mesuré une pente de deux centimètres sur trois mètres.","Constat mesuré — solide, vérifiable par un tiers."],
         ["La grille présente un dépôt brunâtre.","Constat visuel — solide, mais ne dit ni depuis quand ni pourquoi."],
         ["Selon l'assurée, aucun refoulement ne s'est produit depuis 2019.","Rapporté — non vérifié, et pourtant écrit."],
         ["Le drain n'aurait pas été entretenu.","Rapporté au conditionnel — l'expert n'en répond pas."],
         ["Il appert que l'obstruction s'est formée progressivement.","Déduction — c'est ici qu'on conteste."],
         ["Aucune inspection par caméra n'a été effectuée.","Aveu — la vérification décisive manque."],
       ]},

      {t:'piege', h:"Trois erreurs de lecture qui coûtent un dossier",
       rows:[
         ["s'arrêter à la conclusion","lire d'abord le mandat et les constatations",
          "La conclusion est la partie la plus faible du document : c'est une opinion. Les deux premiers blocs sont ceux qui contiennent vos arguments."],
         ["croire qu'un rapport détaillé est un rapport solide","compter les constats et compter les déductions",
          "Quatre pages peuvent contenir six constats et douze déductions. La longueur ne prouve rien ; la proportion, oui."],
         ["ne pas comparer le rapport à la lettre","les mettre côte à côte, un crayon à la main",
          "C'est exactement là qu'on trouve les contradictions — un tuyau pour un autre, une date pour une autre. Elles apparaissent à la troisième lecture, jamais à la première."],
       ]},

      {t:'check', h:"Est-ce que c'est clair maintenant ?",
       p:"Trois questions rapides.",
       qs:[
         {q:"« Il appert que » annonce…", opts:["une déduction","un constat"], ok:0,
          fb:"C'est la formule type de l'analyse : une explication proposée, pas une observation."},
         {q:"Le bloc le plus difficile à contester est…", opts:["la conclusion","les constatations"], ok:1,
          fb:"Ce que l'expert a vu et mesuré engage sa signature et se vérifie."},
         {q:"« Le drain n'aurait pas été entretenu » : ce conditionnel signifie…", opts:["une politesse","une information non vérifiée"], ok:1,
          fb:"C'est un aveu discret : l'expert rapporte sans avoir vérifié."},
       ]},

      {t:'revoir', h:"À retenir",
       p:"Cinq blocs : <b>mandat</b>, <b>constatations</b>, <b>renseignements obtenus</b>, <b>analyse</b>, <b>conclusion</b>. Trois sortes de phrases : ce qui a été <b>vu</b> (j'ai constaté), ce qui a été <b>dit</b> (selon l'assurée), ce qui est <b>déduit</b> (il appert que). Cherchez un constat qui vous serve, une déduction sans appui, et une contradiction avec la lettre. Une seule des trois suffit."},
    ]
  },

  t1rel: {
    eye:'Mini-leçon', tit:"Dont, auquel, sur laquelle : suivre le fil d'une phrase longue",
    blocs:[
      {t:'texte', h:"Pourquoi les documents officiels en sont pleins",
       p:"Un contrat, un rapport, une décision : trois genres qui empilent les précisions dans une seule phrase, parce que couper la phrase risquerait de séparer une condition de ce qu'elle conditionne. Le pronom relatif est ce qui permet cet empilement. Ne pas le suivre, ce n'est pas manquer un détail : c'est perdre la moitié de ce qu'on lit.",
       note:"C'est aussi ce qui rend ces textes fatigants pour tout le monde, y compris pour les gens dont c'est la langue maternelle. Vous n'êtes pas seul devant cette difficulté."},

      {t:'ana', h:"<b>dont</b> — il remplace « de + quelque chose »",
       p:"Le plus fréquent, et le plus mal compris. Cherchez toujours le <b>de</b> caché : il est dans le verbe, ou dans le lien entre deux noms.",
       mots:[['Deux noms',"le drain, dont la grille est bouchée = la grille de ce drain"],['Un verbe en « de »',"un élément dont l'assuré a la charge",true],['Autre exemple',"la clause dont nous discutons = discuter de la clause"]],
       say:"Le drain, dont la grille est bouchée, se trouve au centre de la dalle.",
       note:"Un test simple : remplacez « dont » par « de lui », « d'elle », « de cela ». Si la phrase tient, « dont » est le bon choix."},

      {t:'ana', h:"<b>lequel</b> et ses formes contractées",
       p:"Dès qu'une autre préposition entre en jeu, « dont » ne convient plus. On emploie « lequel », qui s'accorde et se contracte avec « à » et « de ».",
       mots:[['Contractions',"à + lequel = auquel · à + lesquels = auxquels"],['De',"de + lequel = duquel · de + lesquelles = desquelles",true],['Non contractées',"à laquelle · sur lequel · dans laquelle · par lesquels"]],
       say:"L'article auquel la lettre renvoie · la clause sur laquelle ils s'appuient.",
       note:"« à laquelle » et « de laquelle » ne se contractent jamais : c'est la seule irrégularité à retenir."},

      {t:'ana', h:"Le verbe commande, pas le nom",
       p:"C'est la méthode, et elle marche à tous les coups. Trouvez le verbe qui suit le relatif, demandez-vous quelle préposition ce verbe exige, et vous avez la forme.",
       mots:[['renvoyer à',"l'article auquel la lettre renvoie"],['s\'appuyer sur',"la clause sur laquelle ils s'appuient",true],['avoir la charge de',"un élément dont il a la charge"]],
       say:"L'article auquel la lettre renvoie porte sur le défaut d'entretien.",
       note:"L'erreur la plus fréquente vient d'un verbe traduit de sa langue maternelle : « discuter de quelque chose » en français, mais pas dans toutes les langues."},

      {t:'ana', h:"Pour une personne, on préfère <b>qui</b>",
       p:"Après une préposition, une personne se reprend par « qui » plutôt que par « lequel ». Ce n'est pas une règle absolue, c'est un usage — mais il s'entend.",
       mots:[['On dit',"l'expert à qui j'ai parlé · la personne avec qui j'ai ouvert le dossier"],['On évite',"l'expert auquel j'ai parlé",true],['On garde lequel',"quand il faut lever une ambiguïté"]],
       say:"L'expert à qui j'ai parlé est venu deux jours après l'orage.",
       note:"« Auquel » pour une personne n'est pas fauté ; il sonne seulement plus administratif."},

      {t:'ex', h:"Le relatif et ce qu'il remplace",
       p:"À gauche, la phrase. À droite, ce que le relatif reprend.",
       rows:[
         ["L'article 7.3, auquel la lettre renvoie","la lettre renvoie à l'article 7.3"],
         ["Le drain, dont la grille est bouchée","la grille de ce drain"],
         ["L'exclusion sur laquelle l'assureur s'appuie","il s'appuie sur cette exclusion"],
         ["La facture, au bas de laquelle figure la date","au bas de cette facture"],
         ["Les photographies sur lesquelles nous appuyons la demande","nous nous appuyons sur ces photographies"],
         ["Le service auquel la demande est adressée","on adresse la demande à ce service"],
       ]},

      {t:'piege', h:"Trois pièges",
       rows:[
         ["l'article que la lettre renvoie","l'article auquel la lettre renvoie",
          "« Renvoyer » exige « à ». Le simple « que » ne peut pas porter une préposition : c'est l'erreur la plus répandue."],
         ["le drain que la grille est bouchée","le drain dont la grille est bouchée",
          "Il y a un « de » caché entre les deux noms : la grille <b>du</b> drain."],
         ["la clause à laquelle nous discutons","la clause dont nous discutons",
          "On discute <b>de</b> quelque chose. Le verbe décide, jamais l'oreille."],
       ]},

      {t:'texte', h:"La virgule change le sens, et personne ne le dit",
       p:"Sans virgule, la relative <b>distingue</b> : « le drain qui est bouché » suppose qu'il y en a plusieurs et désigne celui-là. Avec des virgules, elle <b>ajoute</b> : « le drain, qui est bouché, » suppose qu'il n'y en a qu'un et donne un renseignement de plus. Dans un contrat, cette différence-là vaut de l'argent : « les dommages qui résultent d'un défaut d'entretien » n'exclut qu'une partie des dommages, tandis que « les dommages, qui résultent d'un défaut d'entretien, » les exclurait tous.",
       note:"Quand une virgule change ce qu'un contrat couvre, elle se lit deux fois."},

      {t:'check', h:"Est-ce que c'est clair maintenant ?",
       p:"Trois questions rapides.",
       qs:[
         {q:"« Un élément ___ l'assuré a la charge »", opts:["dont","auquel"], ok:0,
          fb:"Avoir la charge <b>de</b> quelque chose : c'est « dont »."},
         {q:"« La clause ___ ils s'appuient »", opts:["dont","sur laquelle"], ok:1,
          fb:"S'appuyer <b>sur</b> : la préposition n'est pas « de »."},
         {q:"Ce qui décide de la forme du relatif, c'est…", opts:["le nom qui précède","le verbe qui suit"], ok:1,
          fb:"Le verbe, et la préposition qu'il exige."},
       ]},

      {t:'revoir', h:"À retenir",
       p:"<b>dont</b> quand la préposition cachée est « de ». <b>auquel, à laquelle, sur lequel, dans laquelle…</b> pour toutes les autres. <b>à qui, avec qui</b> pour les personnes. La méthode tient en une phrase : trouvez le verbe, trouvez sa préposition, et la forme suit."},
    ]
  },

  t1pass: {
    eye:'Mini-leçon', tit:"Le passif, ou l'art de ne nommer personne",
    blocs:[
      {t:'texte', h:"Ce que le passif fait, et pourquoi il est partout ici",
       p:"« Le drain n'a pas été entretenu. » Lisez-la deux fois. Elle affirme quelque chose de grave — quelqu'un a manqué à une obligation — et elle ne dit pas qui. C'est tout le travail du passif : mettre en sujet ce qui subit l'action, et laisser dans l'ombre celui qui l'a faite. Dans un rapport d'expertise, dans une lettre de refus, dans une décision administrative, il est employé à chaque paragraphe, et rarement par hasard.",
       note:"Le passif n'est pas malhonnête. Il est prudent : l'expert ne veut pas écrire « madame Vlaicu n'a pas entretenu son drain », parce qu'il ne l'a pas vérifié."},

      {t:'ana', h:"Le geste de lecture : « par qui ? »",
       p:"Devant tout passif d'un document officiel, posez la question à voix haute. Si la phrase ne peut pas y répondre, elle affirme beaucoup moins qu'elle n'en a l'air.",
       mots:[['La phrase',"Le drain n'a pas été entretenu."],['La question','par qui ? — la phrase ne le dit pas',true],['Ce qu\'on en tire','l\'affirmation n\'est appuyée sur personne']],
       say:"Le drain n'a pas été entretenu. Par qui ? La phrase ne le dit pas.",
       note:"C'est exactement là que se gagne une révision : en rétablissant le nom manquant et en montrant qu'il ne convient pas."},

      {t:'ana', h:"Les verbes pronominaux à sens passif",
       p:"Ils ont l'air actifs et ne le sont pas. Personne ne forme, personne ne constate, personne n'adresse : le pronom « se » remplace un agent qu'on ne veut pas nommer.",
       mots:[['On lit',"une obstruction se forme lentement"],['Autres exemples',"ce dommage se constate après coup · la demande s'adresse par écrit",true],['Ce que ça cache','qui forme ? qui constate ? qui adresse ?']],
       say:"Une obstruction se forme lentement. La demande s'adresse par écrit.",
       note:"Très fréquents dans la langue administrative, et souvent utiles : « la demande s'adresse par écrit » évite d'écrire « vous devez écrire »."},

      {t:'ana', h:"Les tournures impersonnelles",
       p:"La forme la plus effacée des trois : le sujet « il » ne désigne rien du tout. C'est celle des mandats et des conclusions.",
       mots:[['On lit',"il nous a été demandé de déterminer la cause"],['Autres',"il appert que · il a été constaté que · il est établi que",true],['Ce que ça cache','qui a demandé ? qui a constaté ?']],
       say:"Il nous a été demandé de déterminer la cause du refoulement.",
       note:"« Il nous a été demandé » veut dire « la Mutuelle nous a demandé ». Le nom du client de l'expert n'apparaît nulle part, et pourtant il compte."},

      {t:'texte', h:"Quand vous écrivez, faites exactement l'inverse",
       p:"Une contestation nomme les agents. « Plomberie Chartier a nettoyé le drain le 3 mai. » « Monsieur Lauzière a passé une caméra le 19 octobre. » Un sujet, un verbe, une date : c'est ce qui se vérifie, donc ce qui pèse. Chaque fois que vous vous surprenez à écrire « il a été procédé à un nettoyage », récrivez avec un nom propre. Vous verrez la phrase raccourcir de moitié.",
       note:"Une seule exception : la concession. « Un dépôt a bien été observé » est plus habile que « votre expert a observé un dépôt » — on concède le fait sans concéder l'autorité de celui qui l'a vu."},

      {t:'ex', h:"Rendre son sujet à la phrase",
       p:"À gauche, ce qu'on lit. À droite, ce que ça veut dire.",
       rows:[
         ["Le dossier a été fermé la semaine dernière.","Le service des sinistres a fermé le dossier."],
         ["Aucune inspection n'a été effectuée.","L'expert n'a pas inspecté le drain."],
         ["Il nous a été demandé de déterminer la cause.","La Mutuelle nous a demandé de déterminer la cause."],
         ["Cette information n'a pas été transmise.","Personne ne me l'a demandée."],
         ["Une réponse motivée doit être rendue.","L'assureur doit rendre une réponse motivée."],
         ["Ce type d'obstruction se constate à la caméra.","On ne le constate qu'à la caméra — et on ne l'a pas fait."],
       ]},

      {t:'piege', h:"Trois pièges",
       rows:[
         ["la facture a été transmis","la facture a été transmise",
          "Au passif, le participe s'accorde <b>toujours</b> avec le sujet. Aucun cas ne fait exception."],
         ["il a été constaté que le drain était bouché depuis dix ans","qui l'a constaté, et comment ?",
          "Un impersonnel suivi d'une affirmation forte est le point faible d'un rapport. Demandez la source : elle est parfois absente du document."],
         ["écrire soi-même « il a été procédé au nettoyage »","« Plomberie Chartier a nettoyé le drain le 3 mai »",
          "Imiter la langue administrative pour se donner du sérieux est le réflexe le plus contre-productif d'une demande de révision. Nommez, datez, chiffrez."],
       ]},

      {t:'check', h:"Est-ce que c'est clair maintenant ?",
       p:"Trois questions rapides.",
       qs:[
         {q:"« Une obstruction se forme lentement » est…", opts:["un pronominal à sens passif","une phrase active ordinaire"], ok:0,
          fb:"Personne ne forme quoi que ce soit : le « se » remplace un agent absent."},
         {q:"Devant un passif de document officiel, le premier geste est de…", opts:["demander « par qui ? »","chercher le temps du verbe"], ok:0,
          fb:"C'est la question qui révèle ce que la phrase n'affirme pas."},
         {q:"Dans votre propre lettre, il vaut mieux…", opts:["imiter la langue administrative","nommer, dater, chiffrer"], ok:1,
          fb:"Un sujet, un verbe, une date : c'est ce qui se vérifie."},
       ]},

      {t:'revoir', h:"À retenir",
       p:"Trois façons de ne nommer personne : le <b>passif</b> (le drain n'a pas été entretenu), le <b>pronominal passif</b> (une obstruction se forme) et l'<b>impersonnel</b> (il appert que). Le geste de lecture est toujours le même : <b>par qui ?</b> Et quand c'est vous qui écrivez, faites l'inverse : un nom, un verbe, une date."},
    ]
  },

  t2lettre: {
    eye:'Mini-leçon', tit:"La lettre de refus, et ce qu'elle contient sans le dire",
    blocs:[
      {t:'texte', h:"Une page pour un dossier de quatre",
       p:"Une lettre de refus est un résumé. Tout ce qu'elle affirme s'appuie sur des documents que vous n'avez pas encore, et elle ne les joint jamais. C'est pourquoi le premier geste n'est pas de répondre, mais de demander : le rapport intégral, et la disposition du contrat invoquée. Répondre avant d'avoir lu, c'est contester un résumé qu'on n'a pas vérifié.",
       note:"Ces deux documents s'obtiennent sur simple demande, gratuitement, et la lettre le dit souvent elle-même — dans le paragraphe que personne ne lit."},

      {t:'ana', h:"Ce qu'il faut relever en premier : la disposition",
       p:"Un numéro d'article ou un titre de clause. C'est ce qui transforme un refus en décision motivée, et c'est ce qui vous dit quel texte aller lire.",
       mots:[['On cherche',"l'exclusion prévue à l'article 7.3 de votre contrat"],['S\'il n\'y en a pas','la décision n\'est pas motivée',true],['Ce qu\'on fait alors','on demande par écrit qu\'elle le soit']],
       say:"Cette situation est visée par l'exclusion prévue à l'article sept point trois de votre contrat.",
       note:"Une lettre qui dit seulement « votre demande est refusée » ne vous donne rien à contester. Exiger la motivation est un droit, et c'est un premier gain."},

      {t:'ana', h:"Le mot qui décide n'est jamais mis en évidence",
       p:"Il est au milieu d'un paragraphe, en caractères ordinaires. Ici, tout tient à trois mots : « drain de plancher ». C'est en les comparant au rapport qu'apparaît la contradiction.",
       mots:[['La lettre dit',"un défaut d'entretien du drain de plancher"],['Le rapport dit',"l'obstruction du drain de fondation",true],['Ce que ça vaut','deux documents, deux tuyaux : une révision']],
       say:"La lettre parle du drain de plancher ; le rapport parle du drain de fondation.",
       note:"Lisez ces lettres avec un crayon, et soulignez chaque nom d'objet. Les contradictions se voient à la troisième lecture, jamais à la première."},

      {t:'ana', h:"La phrase qui distingue la protection de l'exclusion",
       p:"Les bonnes lettres la contiennent, et elle est instructive : elle reconnaît que vous êtes couvert, et refuse quand même. Ne discutez donc jamais de votre protection : ce n'est pas le sujet.",
       mots:[['La lettre dit',"votre contrat comporte bien l'avenant"],['Puis',"ce n'est pas l'absence de protection qui fonde la décision",true],['Le sujet réel','l\'application de l\'exclusion, et rien d\'autre']],
       say:"Ce n'est pas l'absence de protection qui fonde la présente décision, mais l'application de l'exclusion.",
       note:"Beaucoup de gens répondent en prouvant qu'ils sont assurés. Personne ne le conteste — et pendant ce temps l'exclusion tient toujours."},

      {t:'texte', h:"Le paragraphe « recours », le seul qui vous soit utile",
       p:"Il est presque toujours en fin de lettre : comment demander une révision, à qui écrire, dans quel délai. Il est écrit en petit, sans titre voyant, et c'est pourtant la seule partie du document qui vous donne une action à faire. Lisez-le en premier, puis remontez.",
       note:"Notez aussi la <b>date de réception</b> de la lettre, pas celle qu'elle porte : les délais se comptent de la réception, et c'est vous qui devrez en faire la preuve."},

      {t:'ex', h:"Ce que chaque paragraphe fait",
       p:"À gauche, le paragraphe. À droite, son travail réel.",
       rows:[
         ["Objet : réclamation 2026-41837, sinistre du 14 septembre","Rattacher la lettre à un dossier — à recopier dans toute réponse."],
         ["Nous ne pouvons donner suite à votre demande.","Annoncer la décision, en une phrase, sans motif."],
         ["L'expertise conclut que les dommages résultent d'un défaut d'entretien…","Donner le motif — et le mot qui décide est ici."],
         ["Cette situation est visée par l'exclusion de l'article 7.3.","Motiver : sans ce numéro, la décision est incomplète."],
         ["Votre contrat comporte bien l'avenant…","Prévenir la mauvaise objection, et fermer cette porte."],
         ["Vous pouvez adresser une demande de révision écrite…","Ouvrir la suite : c'est le seul paragraphe utile."],
       ]},

      {t:'piege', h:"Trois réactions qui font perdre du temps",
       rows:[
         ["répondre le jour même, par téléphone, en colère","demander le rapport, et rappeler dans la semaine",
          "L'appel du premier jour ne laisse aucune trace utile et vous prive de l'effet de l'argument que vous n'avez pas encore."],
         ["prouver qu'on est bien assuré","discuter l'exclusion, et elle seule",
          "La lettre l'a déjà reconnu. Répondre là-dessus revient à défendre un point que personne n'attaque."],
         ["jeter l'enveloppe","noter la date de réception au crayon sur la lettre",
          "Les délais se comptent de la réception. Sans cette date, vous plaiderez sur la parole."],
       ]},

      {t:'check', h:"Est-ce que c'est clair maintenant ?",
       p:"Trois questions rapides.",
       qs:[
         {q:"Une lettre de refus sans numéro d'article est…", opts:["une décision non motivée","une décision définitive"], ok:0,
          fb:"Vous pouvez exiger par écrit qu'elle soit motivée."},
         {q:"Le paragraphe le plus utile d'une lettre de refus est…", opts:["le motif","celui des recours"], ok:1,
          fb:"C'est le seul qui vous donne une action à faire, et il est en petit."},
         {q:"Les délais se comptent à partir de…", opts:["la date de la lettre","la date de réception"], ok:1,
          fb:"De la réception — notez-la au crayon sur la lettre."},
       ]},

      {t:'revoir', h:"À retenir",
       p:"Cherchez d'abord la <b>disposition invoquée</b>, puis le <b>mot qui décide</b>, puis le <b>paragraphe des recours</b>. Demandez le rapport intégral avant de répondre. Ne défendez jamais votre protection : ce n'est pas ce qu'on vous refuse. Et notez la date de réception."},
    ]
  },

  t2conc: {
    eye:'Mini-leçon', tit:"Concéder pour être lu",
    blocs:[
      {t:'texte', h:"Le calcul, et il n'est pas moral",
       p:"Une contestation qui nie tout se lit en dix secondes et se classe comme une plainte de plus. Une contestation qui commence par reconnaître ce qui est vrai oblige son lecteur à continuer, parce qu'elle ne ressemble plus à ce qu'il lit tous les jours. Ce n'est pas de la politesse : c'est le calcul le plus rentable de tout le dossier. Trois lignes de concession font lire les quinze suivantes.",
       note:"Concéder n'est jamais renoncer. On donne raison sur un point mesuré, puis on avance sur les autres — et le fait d'avoir donné raison une fois rend le reste crédible."},

      {t:'ana', h:"<b>bien que</b> et <b>quoique</b> — subjonctif obligatoire",
       p:"Les deux marqueurs les plus soutenus, ceux d'une lettre. Ils sont toujours suivis du subjonctif, sans exception.",
       mots:[['On écrit',"Bien que le rapport soit détaillé, il ne conclut rien de vérifiable."],['Autre',"Quoique la visite ait duré vingt-cinq minutes, aucune caméra n'a été passée.",true],['Jamais',"bien que le rapport est détaillé"]],
       say:"Bien que le rapport soit détaillé, il ne conclut rien de vérifiable.",
       note:"Placés en tête de phrase, ils annoncent d'emblée que la suite va retourner ce qu'on vient d'accorder. C'est leur force."},

      {t:'ana', h:"<b>même si</b> — indicatif, toujours",
       p:"Le plus courant à l'oral, et le seul de la famille qui refuse le subjonctif. C'est la faute la plus fréquente des apprenants avancés, et elle s'entend tout de suite.",
       mots:[['On dit',"Même si l'obstruction est ancienne, elle n'explique pas une soirée."],['Jamais',"même si l'obstruction soit ancienne",true],['Le repère','« même si » = « si », et « si » n\'a jamais de subjonctif']],
       say:"Même si l'obstruction est ancienne, elle n'explique pas une inondation en une seule soirée.",
       note:"Le repère est fiable : partout où l'on peut remplacer par « si », l'indicatif s'impose."},

      {t:'ana', h:"<b>certes… mais</b> et <b>il n'en reste pas moins que</b>",
       p:"Deux temps, deux phrases. C'est le registre écrit d'une demande de révision, et la forme la plus élégante de la concession.",
       mots:[['Premier temps',"Certes, ce n'est pas vous qui avez rendu la décision ;"],['Second temps',"il n'en reste pas moins que c'est à vous que j'écris.",true],['Variante',"j'en conviens ; toutefois, …"]],
       say:"Certes, ce n'est pas vous qui avez rendu la décision ; il n'en reste pas moins que c'est à vous que j'écris.",
       note:"« Il n'en reste pas moins que » est suivi de l'indicatif. La formule est longue à écrire et vaut son poids : elle annonce une conclusion qu'on ne peut pas éviter."},

      {t:'ana', h:"<b>en revanche</b>, <b>toutefois</b>, <b>par contre</b> — opposer sans concéder",
       p:"Ceux-là n'accordent rien : ils mettent deux faits côte à côte, à poids égal. Utiles quand il n'y a rien à concéder.",
       mots:[['On écrit',"Le contrat couvre le refoulement ; en revanche, il exclut le défaut d'entretien."],['Registres',"toutefois (soutenu) · en revanche (courant) · par contre (familier au Québec)",true],['Différence','la concession accorde, l\'opposition juxtapose']],
       say:"Le contrat couvre le refoulement ; en revanche, il exclut le défaut d'entretien.",
       note:"Dans une lettre, préférez « toutefois » ou « cependant ». « Par contre » est parfaitement compris, mais il baisse le registre d'un cran."},

      {t:'texte', h:"L'ordre décide de qui gagne",
       p:"Ce qu'on met en second l'emporte, toujours. « Le drain était vieux, mais il avait été nettoyé » plaide pour vous. « Le drain avait été nettoyé, mais il était vieux » plaide contre vous — avec exactement les mêmes mots. Concédez donc en premier, sans exception, et gardez votre fait le plus solide pour la fin de la phrase.",
       note:"C'est vrai de la phrase, et c'est vrai de la lettre entière : le paragraphe de concession se place avant les faits, jamais après."},

      {t:'ex', h:"Concéder, puis retourner",
       p:"À gauche, ce qu'on accorde. À droite, ce qu'on en fait.",
       rows:[
         ["Certes, un dépôt a bien été observé sur la grille…","… il n'en reste pas moins qu'aucune mesure n'a été prise."],
         ["Bien que la visite ait eu lieu deux jours après…","… elle n'a duré que vingt-cinq minutes."],
         ["Même si le drain a douze ans…","… il a été nettoyé cinq mois avant le sinistre."],
         ["J'en conviens, la franchise reste due…","… toutefois, elle ne fonde pas le refus."],
         ["Quoique le rapport soit signé par un expert certifié…","… il repose sur une déduction, non sur une inspection."],
       ]},

      {t:'piege', h:"Trois pièges",
       rows:[
         ["même si le rapport soit détaillé","même si le rapport est détaillé",
          "« Même si » veut l'indicatif, toujours. C'est la faute qui trahit le plus vite un apprenant avancé."],
         ["bien que le rapport est détaillé","bien que le rapport soit détaillé",
          "L'inverse exact, et les deux se commettent souvent le même jour. Retenez le couple : bien que → subjonctif, même si → indicatif."],
         ["concéder à la fin de la lettre","concéder au début, avant les faits",
          "Une concession placée après les arguments annule ce qu'on vient d'établir. Placée avant, elle le rend crédible."],
       ]},

      {t:'check', h:"Est-ce que c'est clair maintenant ?",
       p:"Trois questions rapides.",
       qs:[
         {q:"Après « bien que », le verbe se met…", opts:["à l'indicatif","au subjonctif"], ok:1,
          fb:"Subjonctif, sans exception."},
         {q:"Après « même si », le verbe se met…", opts:["à l'indicatif","au subjonctif"], ok:0,
          fb:"Indicatif : « même si » est un « si »."},
         {q:"Dans une phrase avec « mais », l'élément qui l'emporte est…", opts:["le premier","le second"], ok:1,
          fb:"Ce qui vient après « mais » gagne. Concédez donc en premier."},
       ]},

      {t:'revoir', h:"À retenir",
       p:"<b>bien que</b> et <b>quoique</b> + subjonctif. <b>même si</b> + indicatif. <b>certes…, mais…</b> et <b>il n'en reste pas moins que</b> pour l'écrit. <b>toutefois, en revanche</b> pour opposer sans accorder. Et la règle qui prime : ce qu'on met en second l'emporte."},
    ]
  },

  t2irr: {
    eye:'Mini-leçon', tit:"L'hypothèse irréelle, l'arme tranquille",
    blocs:[
      {t:'texte', h:"Pourquoi elle convainc mieux qu'une contradiction",
       p:"Contredire quelqu'un l'oblige à se défendre. L'hypothèse irréelle fait autre chose : elle accepte provisoirement ce qu'il affirme, en déroule la conséquence, et laisse voir que cette conséquence ne s'est pas produite. Vous n'avez rien nié, personne n'a été mis en cause, et l'argument est tombé tout seul. C'est la forme la plus utile de tout ce module.",
       note:"« Si le drain avait été bouché depuis des années, l'eau serait remontée bien avant — et rien de tel ne s'est produit en sept ans. » Deux phrases, et une expertise s'écroule."},

      {t:'ana', h:"Sur le présent — si + imparfait, conditionnel présent",
       p:"On imagine autre chose que ce qui est. Les deux moitiés vont ensemble et ne se mélangent jamais.",
       mots:[['La condition',"Si j'étais couverte pour ce sinistre,"],['La conséquence',"je recevrais dix-huit mille quatre cents dollars.",true],['Jamais',"si je serais couverte"]],
       say:"Si j'étais couverte pour ce sinistre, je recevrais dix-huit mille quatre cents dollars.",
       note:"Jamais de conditionnel après « si » : c'est la faute la plus remarquée du français, et elle se corrige en une seconde."},

      {t:'ana', h:"Sur le passé — si + plus-que-parfait, conditionnel passé",
       p:"On imagine autre chose que ce qui a été. C'est le montage de la contestation, parce qu'un dossier parle toujours d'un événement passé.",
       mots:[['La condition',"Si l'obstruction s'était formée progressivement,"],['La conséquence',"des remontées se seraient produites à chaque pluie.",true],['Le fait qui manque',"aucune n'est survenue depuis 2019."]],
       say:"Si l'obstruction s'était formée progressivement, des remontées se seraient produites à chaque forte pluie.",
       note:"Ajoutez toujours la troisième phrase : celle qui constate que la conséquence est absente. Sans elle, ce n'est qu'une supposition."},

      {t:'ana', h:"L'irréel du passé sert aussi de reproche courtois",
       p:"Il dit ce qui aurait pu être fait, et par qui, sans jamais accuser. C'est un reproche que la forme grammaticale rend acceptable.",
       mots:[['On écrit',"Si l'on m'avait demandé la facture, je l'aurais envoyée le premier jour."],['Ce que ça dit','personne ne me l\'a demandée',true],['Ce que ça évite',"vous avez négligé de me la demander"]],
       say:"Si l'on m'avait demandé la facture, je l'aurais envoyée le premier jour.",
       note:"La même idée dite à l'indicatif serait une accusation. Dite ainsi, elle est un constat, et elle passe."},

      {t:'ana', h:"La condition sans « si »",
       p:"Le niveau 8 demande de la reconnaître sous trois autres formes. Elles sont fréquentes dans les documents et à l'oral soutenu.",
       mots:[['Le gérondif',"En passant une caméra, on aurait su tout de suite."],['L\'infinitif',"À lire le rapport, on comprend l'inverse de la lettre.",true],['Le conditionnel seul',"Un drain bouché depuis dix ans aurait débordé plus tôt."]],
       say:"En passant une caméra, on aurait su tout de suite. Un drain bouché depuis dix ans aurait débordé plus tôt.",
       note:"La troisième forme est la plus élégante à l'écrit : la condition n'est même pas énoncée, elle est contenue dans le sujet."},

      {t:'ex', h:"Deux montages, à ne pas mélanger",
       p:"À gauche, la condition. À droite, la conséquence.",
       rows:[
         ["Si j'étais couverte (imparfait)","je recevrais l'indemnité (conditionnel présent)"],
         ["Si la lettre nommait le bon drain","la décision se comprendrait mieux"],
         ["Si le drain avait été bouché (plus-que-parfait)","l'eau serait remontée bien avant (conditionnel passé)"],
         ["Si on m'avait demandé la facture","je l'aurais envoyée le premier jour"],
         ["Si l'expert avait passé une caméra","il aurait vu que le drain était libre"],
       ]},

      {t:'piege', h:"Trois pièges",
       rows:[
         ["si j'aurais su","si j'avais su",
          "Jamais de conditionnel après « si ». C'est la faute la plus connue du français, et la plus vite remarquée."],
         ["si le drain était bouché, l'eau serait remontée bien avant","si le drain avait été bouché, l'eau serait remontée",
          "Les deux moitiés doivent appartenir au même montage. Ici l'événement est passé : plus-que-parfait, puis conditionnel passé."],
         ["s'arrêter à l'hypothèse","ajouter le fait qui manque",
          "« … et aucune remontée n'est survenue depuis 2019. » Sans cette phrase, votre hypothèse ne prouve rien du tout."],
       ]},

      {t:'check', h:"Est-ce que c'est clair maintenant ?",
       p:"Trois questions rapides.",
       qs:[
         {q:"« Si l'obstruction ___ progressive, elle aurait laissé des traces. »", opts:["avait été","aurait été"], ok:0,
          fb:"Après « si », jamais de conditionnel : plus-que-parfait."},
         {q:"Le montage de l'irréel du passé est…", opts:["si + imparfait, conditionnel présent","si + plus-que-parfait, conditionnel passé"], ok:1,
          fb:"C'est celui d'une contestation, puisqu'un dossier parle d'un événement passé."},
         {q:"Ce qu'il faut ajouter après une hypothèse irréelle, c'est…", opts:["le fait qui montre que la conséquence est absente","une deuxième hypothèse"], ok:0,
          fb:"Sans lui, l'hypothèse n'est qu'une supposition."},
       ]},

      {t:'revoir', h:"À retenir",
       p:"Deux montages : <b>si + imparfait → conditionnel présent</b> (sur le présent) et <b>si + plus-que-parfait → conditionnel passé</b> (sur le passé). Jamais de conditionnel après « si ». Et jamais d'hypothèse sans la phrase qui constate que la conséquence ne s'est pas produite."},
    ]
  },

  t3etapes: {
    eye:'Mini-leçon', tit:"Les portes du recours, et l'ordre où l'on y frappe",
    blocs:[
      {t:'texte', h:"Ce que presque personne ne sait",
       p:"Un refus d'assurance n'est pas une fin. Il existe une suite, elle est écrite dans les règlements du Québec, et elle est gratuite jusqu'à la dernière étape. Le problème n'est pas qu'elle soit cachée : elle est publiée. Le problème est qu'elle comporte des étapes qui s'ouvrent l'une l'autre, et que sauter la première fait perdre les suivantes.",
       note:"Cette mini-leçon décrit l'état du droit au Québec au moment où le module a été écrit. Les délais et les seuils changent : vérifiez-les sur le site de l'organisme avant d'agir."},

      {t:'ana', h:"Première porte — le service du traitement des plaintes de l'entreprise",
       p:"Tout commence là, et rien ne commence ailleurs. Une plainte, au sens du règlement, est un reproche ou une insatisfaction <b>communiqué</b> à l'entreprise, dans lequel on demande une <b>mesure correctrice</b>. Elle peut être faite verbalement : l'entreprise doit alors aider à la formuler et la <b>consigner</b> par écrit à son registre.",
       mots:[['Ce qu\'on fait','on demande quelque chose de précis, et on garde copie'],['Ce que ça déclenche','le dossier s\'ouvre et les délais commencent à courir',true],['Ce qui est plus sûr','écrire, ou demander une confirmation écrite de son appel']],
       say:"Une plainte peut être communiquée verbalement ou par écrit, et l'entreprise doit alors la consigner.",
       note:"Un appel compte, et l'entreprise doit le consigner. Écrire reste plus sûr : c'est vous qui devrez prouver la date de réception."},

      {t:'ana', h:"Deuxième porte — la réponse finale",
       p:"L'entreprise doit accuser réception, consigner la plainte à son registre, et transmettre une réponse finale écrite dans les soixante jours de la réception.",
       mots:[['Le délai','soixante jours, quatre-vingt-dix en circonstances exceptionnelles'],['Ce que « finale » veut dire','la dernière position de l\'entreprise, pas la vôtre',true],['Ce qu\'elle doit contenir','la disposition, le fait retenu, la conclusion']],
       say:"Une réponse finale écrite et motivée doit être transmise dans les soixante jours de la réception.",
       note:"Un délai porté à quatre-vingt-dix jours doit vous être annoncé, avec sa raison. Un silence n'est pas une prolongation."},

      {t:'ana', h:"Troisième porte — le transfert du dossier à l'Autorité",
       p:"Une fois la réponse finale reçue — ou le délai écoulé sans réponse —, vous pouvez demander à l'Autorité des marchés financiers que votre dossier lui soit transmis.",
       mots:[['Ce que l\'Autorité fait','elle examine, elle surveille, elle peut proposer une conciliation'],['Ce qu\'elle ne fait pas','elle ne renverse rien et n\'ordonne aucune indemnité',true],['La condition','la conciliation exige le consentement des deux parties']],
       say:"L'Autorité examine le dossier et peut proposer un service de règlement des différends.",
       note:"Savoir d'avance ce qu'un organisme ne peut pas faire évite d'attendre des mois une décision qui ne viendra jamais de lui."},

      {t:'ana', h:"Quatrième porte — le tribunal civil",
       p:"C'est la seule qui puisse condamner quelqu'un à payer. La division des petites créances entend les demandes jusqu'à un certain montant, sans avocat, et beaucoup de dossiers d'assurance s'y règlent.",
       mots:[['Ce qu\'on y obtient','un jugement exécutoire'],['Ce que ça demande','du temps, des pièces, et une demande écrite',true],['Le conseil','y aller avec le dossier des trois étapes précédentes']],
       say:"La division des petites créances entend certaines demandes sans avocat.",
       note:"Les trois premières étapes ne sont pas une perte de temps même si l'on finit là : elles constituent le dossier qu'on y dépose."},

      {t:'texte', h:"Ne confondez pas les portes",
       p:"Un différend avec votre <b>assureur</b> relève de l'Autorité des marchés financiers. Un différend avec votre <b>locataire</b> ou votre <b>propriétaire</b> relève du Tribunal administratif du logement — et une décision de ce tribunal se conteste autrement : par une demande de rétractation, ou par une permission d'appeler à la Cour du Québec, dans les trente jours. Deux systèmes distincts, deux séries de délais.",
       note:"Frapper à la mauvaise porte fait perdre des semaines, et parfois un droit. C'est l'erreur la plus coûteuse de tout ce module."},

      {t:'ex', h:"Chaque étape et son document",
       p:"À gauche, ce que vous faites. À droite, ce qu'il vous en reste.",
       rows:[
         ["Écrire au service du traitement des plaintes","Un accusé de réception, et une date"],
         ["Attendre la réponse finale","Une position écrite et motivée"],
         ["Demander le transfert du dossier","Un avis de transfert et un numéro"],
         ["Accepter une conciliation","Une entente, si les deux parties y consentent"],
         ["Déposer aux petites créances","Un jugement, exécutoire"],
       ]},

      {t:'piege', h:"Trois erreurs de parcours",
       rows:[
         ["téléphoner et ne garder aucune trace de son appel","écrire, même trois lignes, et garder copie",
          "L'appel compte et doit être consigné, mais sans trace, la date de réception sera votre parole contre la leur."],
         ["attendre indéfiniment la réponse","compter soixante jours à partir de la réception",
          "Passé ce délai sans réponse ni justification, vous pouvez demander le transfert comme si vous aviez reçu un refus."],
         ["s'adresser au Tribunal administratif du logement pour un refus d'assurance","s'adresser à l'Autorité des marchés financiers",
          "Deux systèmes, deux compétences. Le Tribunal ne traite pas les assureurs, et l'Autorité ne traite pas les baux."],
       ]},

      {t:'check', h:"Est-ce que c'est clair maintenant ?",
       p:"Trois questions rapides.",
       qs:[
         {q:"Une plainte faite au téléphone…", opts:["doit être consignée par l'entreprise","n'a aucune valeur"], ok:0,
          fb:"L'entreprise doit la consigner et aider à la formuler. Écrire reste plus sûr pour la preuve de la date."},
         {q:"L'Autorité des marchés financiers peut…", opts:["ordonner l'indemnisation","examiner et proposer une conciliation"], ok:1,
          fb:"Elle n'est pas un tribunal et ne renverse aucune décision."},
         {q:"Un différend avec votre locataire relève…", opts:["du Tribunal administratif du logement","de l'Autorité des marchés financiers"], ok:0,
          fb:"Deux systèmes distincts, avec des délais distincts."},
       ]},

      {t:'revoir', h:"À retenir",
       p:"Quatre portes, dans l'ordre : <b>écrire à l'entreprise</b>, <b>attendre la réponse finale</b> (soixante jours), <b>demander le transfert</b> à l'Autorité des marchés financiers, puis, s'il le faut, <b>les petites créances</b>. Et deux systèmes à ne pas confondre : l'assureur relève de l'Autorité, le bail relève du Tribunal administratif du logement."},
    ]
  },

  t3sub: {
    eye:'Mini-leçon', tit:"Le subjonctif de ce qu'on demande",
    blocs:[
      {t:'texte', h:"Ce qu'il signale, et ce qu'il ne signale pas",
       p:"On répète souvent que le subjonctif exprime le doute. C'est faux, et cette explication a fait perdre du temps à beaucoup de gens. Le subjonctif ne dit rien sur la réalité de ce qui suit : il dit que la phrase ne se contente pas de <b>rapporter</b> un fait. Après une volonté, une nécessité, une émotion, une condition, le français change de mode — que le fait se réalise ou non.",
       note:"« Je veux qu'il vienne » n'exprime aucun doute sur sa venue. C'est le verbe « vouloir » qui commande le mode, pas la probabilité."},

      {t:'ana', h:"Les verbes de volonté et de demande",
       p:"C'est la structure même d'une demande de révision : un verbe de volonté, « que », puis le subjonctif. Vous en écrirez trois dans la même lettre.",
       mots:[['On écrit',"Je demande que le dossier soit rouvert."],['Autres',"je souhaite qu'une autre personne l'examine · je tiens à ce que la réponse me parvienne",true],['La forme','verbe de volonté + que + subjonctif']],
       say:"Je demande que le dossier soit rouvert et que la contre-expertise soit examinée.",
       note:"« Je tiens à ce que » demande bien « à ce que », et non « que » seul : c'est la construction du verbe « tenir à »."},

      {t:'ana', h:"Les expressions impersonnelles, et leurs deux exceptions",
       p:"Très fréquentes à l'écrit administratif, elles appellent presque toutes le subjonctif — presque.",
       mots:[['Subjonctif',"il faut que · il est important que · il serait souhaitable que"],['Indicatif',"il paraît que · il me semble que",true],['Le repère','ce qui affirme garde l\'indicatif']],
       say:"Il est important que la réponse me parvienne par écrit. Il me semble que le rapport parle d'un autre drain.",
       note:"Les deux exceptions ont ceci de commun qu'elles <b>rapportent</b> quelque chose plutôt que de le vouloir. C'est cohérent avec la règle générale."},

      {t:'ana', h:"Adjectif + que, et la certitude qui fait exception",
       p:"Une émotion ou une appréciation appellent le subjonctif ; une certitude garde l'indicatif.",
       mots:[['Subjonctif',"je suis surprise que le rapport fasse état d'un autre drain"],['Indicatif',"je suis certaine que la facture est au dossier",true],['Le repère','sûr, certain, convaincu, évident → indicatif']],
       say:"Je suis surprise que le rapport fasse état d'un autre drain. Je suis certaine que la facture est au dossier.",
       note:"Nié, l'adjectif de certitude bascule : « je ne suis pas certaine que la facture soit au dossier »."},

      {t:'ana', h:"Les conjonctions qui l'exigent, et celles qui le refusent",
       p:"Une liste courte à connaître par cœur, parce qu'elle revient dans toutes les lettres officielles.",
       mots:[['Subjonctif',"afin que · pour que · bien que · avant que · à moins que · sans que · jusqu'à ce que"],['Indicatif',"après que · parce que · puisque · pendant que · même si",true],['Le repère','ce qui est déjà arrivé garde l\'indicatif']],
       say:"Afin que le dossier soit complet, je joins la facture. Après que la réponse sera arrivée, je déciderai.",
       note:"« Après que » avec le subjonctif est si répandu qu'on l'entend partout ; à l'écrit soutenu, l'indicatif reste la forme attendue."},

      {t:'ana', h:"Le verbe d'opinion nié",
       p:"À la forme affirmative, l'indicatif. À la forme négative ou interrogative, le subjonctif — parce que la phrase cesse d'affirmer.",
       mots:[['Affirmatif',"Je crois que cette conclusion est fondée."],['Nié',"Je ne crois pas que cette conclusion soit fondée.",true],['Utile ici','c\'est la formule d\'une contestation polie']],
       say:"Je ne crois pas que cette conclusion soit fondée sur une observation directe.",
       note:"C'est la façon la plus courtoise de dire qu'on n'est pas d'accord : on ne dit pas que c'est faux, on dit qu'on ne le croit pas."},

      {t:'ex', h:"Les formes du subjonctif présent qui reviennent",
       p:"À gauche, l'infinitif. À droite, la forme après « que ».",
       rows:[
         ["être","que je sois · qu'il soit · qu'ils soient"],
         ["avoir","que j'aie · qu'il ait · qu'ils aient"],
         ["faire","que je fasse · qu'il fasse · qu'ils fassent"],
         ["pouvoir","que je puisse · qu'il puisse · qu'ils puissent"],
         ["venir","que je vienne · qu'il vienne · qu'ils viennent"],
         ["recevoir","que je reçoive · qu'il reçoive · qu'ils reçoivent"],
         ["parvenir","que je parvienne · qu'il parvienne · qu'ils parviennent"],
       ]},

      {t:'piege', h:"Trois pièges",
       rows:[
         ["après que le dossier soit rouvert","après que le dossier sera rouvert",
          "« Après que » veut l'indicatif : ce qui suit est présenté comme réalisé. « Avant que », lui, veut le subjonctif."],
         ["il me semble que ce soit une erreur","il me semble que c'est une erreur",
          "« Il me semble » rapporte une impression et garde l'indicatif, contrairement à « il faut que » ou « il est possible que »."],
         ["je tiens que la réponse soit écrite","je tiens à ce que la réponse soit écrite",
          "Le verbe est « tenir à ». La construction complète est « tenir à ce que »."],
       ]},

      {t:'check', h:"Est-ce que c'est clair maintenant ?",
       p:"Trois questions rapides.",
       qs:[
         {q:"« Il me semble que le rapport ___ d'un autre drain. »", opts:["parle","parlerait"], ok:0,
          fb:"« Il me semble que » garde l'indicatif : c'est une des deux exceptions."},
         {q:"« Je ne crois pas que cette conclusion ___ fondée. »", opts:["est","soit"], ok:1,
          fb:"Le verbe d'opinion nié appelle le subjonctif."},
         {q:"« Afin que le dossier ___ complet, je joins la facture. »", opts:["soit","est"], ok:0,
          fb:"« Afin que » exige le subjonctif."},
       ]},

      {t:'revoir', h:"À retenir",
       p:"Le subjonctif ne dit pas le doute : il dit que la phrase ne rapporte pas un fait. Quatre déclencheurs : les <b>verbes de volonté</b> (je demande que), les <b>expressions impersonnelles</b> (il est important que — sauf « il paraît que » et « il me semble que »), les <b>adjectifs</b> (sauf ceux de certitude) et certaines <b>conjonctions</b> (afin que, bien que, avant que, jusqu'à ce que)."},
    ]
  },

  t3rev: {
    eye:'Mini-leçon', tit:"Écrire une demande de révision",
    blocs:[
      {t:'texte', h:"Ce que c'est, exactement",
       p:"Ce n'est ni une lettre de plainte ni une lettre de colère. C'est un document qui demande à une entreprise de réexaminer une décision qu'elle a rendue, en lui donnant des raisons qu'elle n'avait pas au moment de la rendre. Tout le reste — l'indignation, l'histoire de votre semaine, ce que vous pensez de l'expert — nuit à cet objectif et ne sert à personne.",
       note:"Le lecteur de cette lettre est un employé qui en lit trente par semaine. Il cherche trois choses : le numéro du dossier, ce que vous demandez, et pourquoi il devrait le faire."},

      {t:'ana', h:"L'objet, en une ligne, avec trois dates",
       p:"Numéro de réclamation, date du sinistre, date de la décision contestée. Sans elles, votre lettre attend qu'on la rattache à quelque chose, et cela peut prendre une semaine.",
       mots:[['On écrit',"Objet : demande de révision — réclamation 2026-41837"],['On complète',"sinistre du 14 septembre 2026, décision du 12 octobre 2026",true],['Ce que ça évite','une lettre qui circule sans dossier']],
       say:"Objet : demande de révision, réclamation 2026-41837, décision du 12 octobre 2026.",
       note:"Recopiez le numéro tel qu'il figure sur la lettre de refus, chiffre pour chiffre. Un numéro approché ne se retrouve pas."},

      {t:'ana', h:"Citer le motif dans les mots de l'assureur",
       p:"Entre guillemets, précédés de deux points. On ne conteste pas une décision qu'on aurait reformulée à sa façon : on conteste celle qui a été rendue.",
       mots:[['On écrit',"Votre lettre motive le refus ainsi : « les dommages résultent d'un défaut d'entretien du drain de plancher »."],['Puis on retourne',"Or le rapport ne traite pas du drain de plancher.",true],['La ponctuation','deux points, guillemets, point final hors des guillemets']],
       say:"Votre lettre motive le refus ainsi : les dommages résultent d'un défaut d'entretien du drain de plancher.",
       note:"Le mot « Or » qui ouvre la phrase suivante est le pivot de toute la lettre. Il annonce que ce qui vient contredit ce qu'on vient de citer."},

      {t:'ana', h:"Concéder, en trois lignes, puis avancer",
       p:"Un paragraphe court qui reconnaît la part exacte de raison de l'autre. Il coûte trois lignes et fait lire les quinze suivantes.",
       mots:[['On écrit',"Certes, un dépôt a bien été observé sur la grille ;"],['On retourne',"il n'en reste pas moins qu'aucune mesure n'a été prise.",true],['Ce qu\'on ne fait pas','contester le constat lui-même']],
       say:"Certes, un dépôt a bien été observé sur la grille ; il n'en reste pas moins qu'aucune mesure n'a été prise.",
       note:"On concède le <b>constat</b> et on discute la <b>déduction</b>. Contester ce que l'expert dit avoir vu est le meilleur moyen de perdre sa crédibilité."},

      {t:'ana', h:"Opposer des faits, jamais des sentiments",
       p:"Une date, une entreprise, un nombre de pages, un nombre de photographies. « Je trouve cela injuste » n'entre dans aucun registre ; « le drain a été nettoyé le 3 mai par Plomberie Chartier » y entre tel quel.",
       mots:[['Un fait',"Le drain a été nettoyé le 3 mai 2026 par Plomberie Chartier."],['Sa pièce',"la facture acquittée est jointe",true],['La règle','un fait sans pièce jointe se perd entre deux services']],
       say:"Le drain de plancher a été nettoyé le 3 mai 2026 par Plomberie Chartier ; la facture acquittée est jointe.",
       note:"Numérotez vos pièces jointes et nommez-les dans le texte. Un dossier qui se vérifie sans effort se vérifie."},

      {t:'ana', h:"Demander, précisément, et rappeler le délai",
       p:"Trois demandes numérotées valent mieux qu'un paragraphe d'indignation. Et rappeler le délai dit à votre lecteur que la lettre sera relue à cette date-là.",
       mots:[['Demande 1',"que le dossier soit rouvert"],['Demande 2',"que la contre-expertise soit examinée par une autre personne",true],['Demande 3',"qu'une réponse finale écrite et motivée soit transmise dans les soixante jours"]],
       say:"Je demande que le dossier soit rouvert, que la contre-expertise soit examinée, et qu'une réponse motivée me soit transmise.",
       note:"Ces trois demandes s'écrivent au subjonctif après « je demande que » — c'est l'exercice 3 de ce défi, et il n'était pas là par hasard."},

      {t:'ex', h:"La lettre, paragraphe par paragraphe",
       p:"À gauche, le paragraphe. À droite, son travail.",
       rows:[
         ["Objet : demande de révision — réclamation, sinistre, décision","Rattacher au dossier en une ligne"],
         ["Je vous adresse une demande de révision de la décision du…","Dire ce que la lettre est, sans détour"],
         ["Votre lettre motive le refus ainsi : « … ». Or…","Citer, puis retourner"],
         ["Certes… ; il n'en reste pas moins que…","Concéder ce qui est vrai"],
         ["Le drain a été nettoyé le 3 mai… La contre-expertise établit…","Opposer des faits, avec leurs pièces"],
         ["Si l'obstruction s'était formée progressivement…","Dérouler l'hypothèse, et constater qu'elle est fausse"],
         ["Je demande que… que… et que…","Trois demandes précises"],
         ["Je demeure disponible au 819 555-0173.","Se rendre joignable"],
       ]},

      {t:'piege', h:"Trois erreurs qui font classer une lettre",
       rows:[
         ["raconter toute l'histoire depuis le début","donner les trois dates, puis les faits contestés",
          "Le lecteur connaît le dossier : il l'a sous les yeux. Ce qu'il n'a pas, c'est ce que vous apportez de neuf."],
         ["écrire « je trouve cela inacceptable »","écrire « aucune inspection par caméra n'a été effectuée »",
          "Le premier ne se consigne nulle part. Le second entre au dossier tel quel, et sera lu par la personne suivante."],
         ["menacer de poursuites dès la première lettre","rappeler le délai de soixante jours",
          "Une menace prématurée fait passer le dossier au service juridique, où il ralentit. Le délai, lui, oblige sans braquer."],
       ]},

      {t:'check', h:"Est-ce que c'est clair maintenant ?",
       p:"Trois questions rapides.",
       qs:[
         {q:"Le motif du refus se cite…", opts:["dans les mots de l'assureur, entre guillemets","reformulé avec vos mots"], ok:0,
          fb:"On conteste la décision rendue, pas une reformulation."},
         {q:"Dans la concession, on accorde…", opts:["le constat","la déduction"], ok:0,
          fb:"On concède ce que l'expert a vu, et on discute ce qu'il en tire."},
         {q:"La lettre se termine par…", opts:["une menace de poursuite","des demandes précises et un rappel du délai"], ok:1,
          fb:"Trois demandes numérotées, le délai, et un numéro de téléphone."},
       ]},

      {t:'revoir', h:"À retenir",
       p:"Objet avec les <b>trois dates</b>. Une phrase qui dit ce que la lettre est. Le motif <b>cité</b>, puis retourné par « Or ». Une <b>concession</b> de trois lignes. Des <b>faits</b> avec leurs pièces. Une <b>hypothèse irréelle</b>. Trois <b>demandes</b> au subjonctif. Un numéro de téléphone. Rien d'autre."},
    ]
  },

  t3emph: {
    eye:'Mini-leçon', tit:"Mettre en avant, et dire quand ce sera fait",
    blocs:[
      {t:'texte', h:"Pourquoi l'emphase compte dans une lettre courte",
       p:"Sur trois paragraphes, une seule phrase sera relue. L'emphase désigne laquelle. Elle n'ajoute aucune information — elle réorganise la phrase pour que l'essentiel arrive à l'endroit où l'œil s'arrête. C'est de la mise en page faite avec de la grammaire.",
       note:"« Ce que je conteste, c'est le motif, non le montant. » Comparez avec « je conteste le motif et non le montant » : mêmes mots, deux poids différents."},

      {t:'ana', h:"<b>Ce qui / ce que / ce dont…, c'est</b>",
       p:"La forme la plus utile. Le choix entre les trois dépend du verbe, exactement comme pour les relatifs.",
       mots:[['Ce qui (sujet)',"Ce qui m'étonne, c'est l'absence d'inspection."],['Ce que (complément)',"Ce que je demande, c'est une réponse motivée.",true],['Ce dont (verbe en « de »)',"Ce dont je dispose, c'est d'une facture acquittée."]],
       say:"Ce que je demande, c'est une réponse écrite et motivée.",
       note:"Le test est le même qu'au défi 1 : quel verbe, et quelle préposition ? Étonner quelque chose, demander quelque chose, disposer <b>de</b> quelque chose."},

      {t:'ana', h:"<b>C'est… qui</b> / <b>c'est… que</b>",
       p:"On isole un élément et on le pousse en tête. « Qui » si cet élément est le sujet, « que » s'il est complément.",
       mots:[['Sujet → qui',"C'est Plomberie Chartier qui est intervenue en mai."],['Complément → que',"C'est le drain de fondation que le rapport décrit.",true],['L\'effet','on répond à une question qui n\'a pas été posée']],
       say:"C'est le drain de fondation que le rapport décrit, et non le drain de plancher.",
       note:"Cette forme sert à corriger sans contredire : elle dit « ce n'est pas ce que vous croyez » sans jamais l'écrire."},

      {t:'ana', h:"La dislocation — la forme parlée de l'emphase",
       p:"On annonce l'élément, puis on le reprend par un pronom. À l'oral, c'est ce que tout le monde fait ; à l'écrit, on la réserve à un registre familier.",
       mots:[['À gauche',"Ce dossier-là, je le fais rouvrir."],['À droite',"Je vous l'envoie dans l'heure, la facture.",true],['Au téléphone','parfaitement naturel · dans une lettre, non']],
       say:"Ce dossier-là, je le fais rouvrir. La facture, je vous l'envoie dans l'heure.",
       note:"C'est la seule des quatre formes qui change de registre. Employez-la au téléphone, jamais dans la demande de révision."},

      {t:'ana', h:"Le futur antérieur après <b>quand</b>",
       p:"Il dit qu'une action sera terminée avant qu'une autre commence. Deux futurs de suite ne diraient pas cet ordre-là.",
       mots:[['On écrit',"Quand vous aurez reçu ma lettre, le délai commencera à courir."],['Autre',"Je vous rappellerai quand le service aura examiné la contre-expertise.",true],['La forme','avoir ou être au futur + participe passé']],
       say:"Quand vous aurez reçu ma lettre, le délai de soixante jours commencera à courir.",
       note:"Dans un échéancier, c'est le temps qui rend l'ordre des choses indiscutable. Très utile dans la dernière phrase d'une lettre."},

      {t:'ana', h:"<b>aller</b> + infinitif passé",
       p:"Plus rare, et précieux : une action à venir, présentée comme déjà accomplie à un moment donné.",
       mots:[['On écrit',"D'ici vendredi, je vais avoir envoyé toutes les pièces."],['Ce que ça dit','ce sera fait, et fait avant cette date',true],['La forme','aller au présent + avoir ou être + participe']],
       say:"D'ici vendredi, je vais avoir envoyé toutes les pièces du dossier.",
       note:"On l'emploie surtout à l'oral, pour rassurer sur un délai qu'on tiendra."},

      {t:'ex', h:"La même phrase, mise en avant autrement",
       p:"À gauche, la phrase ordinaire. À droite, ce qu'elle devient.",
       rows:[
         ["Je conteste le motif, pas le montant.","Ce que je conteste, c'est le motif, non le montant."],
         ["L'absence d'inspection m'étonne.","Ce qui m'étonne, c'est l'absence d'inspection."],
         ["Je dispose d'une facture acquittée.","Ce dont je dispose, c'est d'une facture acquittée."],
         ["Le rapport décrit le drain de fondation.","C'est le drain de fondation que le rapport décrit."],
         ["Plomberie Chartier est intervenue en mai.","C'est Plomberie Chartier qui est intervenue en mai."],
         ["Je fais rouvrir ce dossier.","Ce dossier-là, je le fais rouvrir."],
       ]},

      {t:'piege', h:"Trois pièges",
       rows:[
         ["ce que j'ai besoin, c'est d'une réponse","ce dont j'ai besoin, c'est d'une réponse",
          "Avoir besoin <b>de</b> : c'est « ce dont ». La faute est très fréquente, y compris chez les locuteurs natifs."],
         ["c'est le drain de fondation qui le rapport décrit","c'est le drain de fondation que le rapport décrit",
          "L'élément mis en avant est complément du verbe « décrire » : « que »."],
         ["quand vous recevrez ma lettre, le délai commencera","quand vous aurez reçu ma lettre, le délai commencera",
          "Deux futurs ne disent pas l'ordre. Le futur antérieur dit que la première action sera terminée."],
       ]},

      {t:'check', h:"Est-ce que c'est clair maintenant ?",
       p:"Trois questions rapides.",
       qs:[
         {q:"« ___ je dispose, c'est d'une facture acquittée. »", opts:["Ce que","Ce dont"], ok:1,
          fb:"Disposer <b>de</b> : c'est « ce dont »."},
         {q:"« C'est Plomberie Chartier ___ est intervenue. »", opts:["qui","que"], ok:0,
          fb:"L'élément mis en avant est le sujet du verbe : « qui »."},
         {q:"« Quand vous ___ ma lettre, le délai commencera. »", opts:["recevrez","aurez reçu"], ok:1,
          fb:"Le futur antérieur marque que la première action est terminée."},
       ]},

      {t:'revoir', h:"À retenir",
       p:"Quatre façons de mettre en avant : <b>ce qui / ce que / ce dont…, c'est</b> · <b>c'est… qui / que</b> · la <b>dislocation</b> (à l'oral seulement) · et, pour l'ordre des choses, le <b>futur antérieur après quand</b>. Dans une lettre de trois paragraphes, une seule phrase sera relue : choisissez laquelle."},
    ]
  },
};
