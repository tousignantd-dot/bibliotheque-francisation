const PLUS = {

  pr1: {
    eye:'Mini-leçon', tit:"Ce qui se décide dans les premières heures",
    blocs:[
      {t:'texte', h:"Une réclamation se gagne ou se perd le jour même",
       p:"Tout ce que vous ferez pendant les six semaines qui suivent dépendra de trois gestes posés dans les heures qui suivent le dommage : réclamer une copie signée de l'inventaire, photographier avec une date visible, et ne rien accepter par téléphone. Aucun de ces gestes ne coûte d'argent, aucun ne demande de connaître le droit, et ils décident pourtant du sort du dossier.",
       note:"Ce n'est pas une question de méfiance. Personne ne ment ; simplement, six semaines plus tard, plus personne ne se souvient de rien."},

      {t:'texte', h:"Ce qui n'est pas noté n'a pas eu lieu",
       p:"L'inventaire signé au départ est la seule photographie de l'état de vos meubles avant qu'ils entrent dans le camion. Un dommage qui n'y figure pas est réputé ne pas avoir existé à ce moment-là — et c'est précisément ce qui vous sert, si l'inventaire ne note rien et que le meuble arrive fendu. La feuille joue donc dans les deux sens : elle protège le transporteur des dommages anciens, et elle vous protège des dommages nouveaux.",
       note:"Réclamez la copie signée avant que le camion parte. Après, elle devient une faveur."},

      {t:'ex', h:"Trois gestes, trois raisons",
       p:"À gauche, ce qu'on fait. À droite, ce que ça règle six semaines plus tard.",
       rows:[
         ["Réclamer la copie signée de l'inventaire","Prouver l'état des biens avant le transport"],
         ["Photographier avec l'horodatage activé","Situer le dommage dans le temps, à la minute"],
         ["Noter l'heure d'arrivée et de départ du camion","Délimiter la période où quelqu'un d'autre avait la garde"],
         ["Écrire le nom du chauffeur","Pouvoir citer un témoin, plus tard, sans le chercher"],
         ["Ne rien signer d'autre sur place","Éviter une décharge de responsabilité déguisée en accusé de réception"],
         ["Ne pas jeter le bien abîmé","Un bien jeté avant l'examen de l'expert n'est plus indemnisable"],
       ]},

      {t:'piege', h:"Trois réflexes qui coûtent cher le premier jour",
       rows:[
         ["dire « on verra ça plus tard, je suis épuisée »","poser les trois gestes avant de défaire une boîte",
          "Le jour du déménagement est le pire moment pour faire de la paperasse, et c'est le seul où elle vaut quelque chose. Vingt minutes ce soir-là valent six semaines de courriels."],
         ["nettoyer, réparer ou jeter tout de suite","laisser en l'état et photographier",
          "Le réflexe d'ordre est le pire ennemi d'une réclamation. L'assureur indemnise ce que son expert peut constater ; ce que vous avez déjà réparé n'a jamais existé pour lui."],
         ["accepter au téléphone « on va s'arranger »","demander la proposition par écrit",
          "Une entente verbale ne se prouve pas, et elle peut fermer le dossier chez votre assureur sans que vous l'ayez voulu. Remerciez, demandez un courriel, ne dites pas oui."],
       ]},

      {t:'check', h:"Quatre décisions du premier soir",
       p:"Quatre questions, vite fait.",
       qs:[
         {q:"Le vaisselier est fendu. Vous le faites réparer tout de suite ?", opts:["Oui, avant que ça empire","Non, on photographie et on attend l'expert"], ok:1,
          fb:"Un bien réparé ou jeté avant l'examen n'est plus indemnisable. On photographie, on garde, on attend."},
         {q:"Le déménageur propose au téléphone « cent vingt piastres et on n'en parle plus ».", opts:["On accepte, c'est réglé","On demande la proposition par écrit"], ok:1,
          fb:"Un montant encaissé peut fermer votre dossier d'assurance tout seul. Rien ne se refuse, rien ne s'accepte : on demande par écrit."},
         {q:"Vous n'avez pas de facture pour les livres abîmés.", opts:["La réclamation est perdue","Une photo datée ou un relevé peut servir de preuve"], ok:1,
          fb:"Une preuve n'est pas forcément une facture. Photo datée, relevé de carte, courriel de confirmation : tout se plaide."},
         {q:"Personne ne surveillait le balcon pendant l'averse. Vous le dites ?", opts:["Non, ça affaiblirait le dossier","Oui, et ça rend crédible le reste"], ok:1,
          fb:"Concéder le point faible achète l'attention sur les points forts. C'est un calcul, pas une politesse."},
       ]},

      {t:'revoir', h:"À retenir",
       p:"Trois gestes le jour même : la <b>copie signée</b> de l'inventaire, des <b>photos datées</b>, et <b>rien d'accepté</b> de vive voix. Trois interdits : ne pas réparer, ne pas jeter, ne pas encaisser. Et une règle de conduite qui vaut pour tout le module : <b>concéder tout de suite le point qui ne tient pas</b>."},
    ]
  },

  prInto: {
    eye:'Mini-leçon', tit:"Quatre mélodies, et ce qu'elles engagent",
    blocs:[
      {t:'texte', h:"La seule chose que le niveau 8 demande encore à l'oreille",
       p:"Le programme du niveau 8 ne demande plus qu'une chose à l'oreille et à la voix : produire l'<b>intonation expressive</b>. Pas un son nouveau, pas une liaison de plus — une mélodie. À ce stade, votre prononciation est assez bonne pour qu'on vous comprenne ; ce qui vous reste à gagner est ce que la voix ajoute par-dessus les mots. Une même phrase de six mots peut dire la surprise, la déception ou la détermination, et c'est souvent la seule chose que votre interlocuteur retiendra.",
       note:"Une intonation plate se lit comme de l'indifférence, alors qu'elle n'est le plus souvent que de la prudence."},

      {t:'texte', h:"Pourquoi ça compte au téléphone, précisément",
       p:"Au téléphone, votre interlocuteur n'a rien d'autre. Pas votre visage, pas vos papiers, pas la fente dans le panneau du meuble. Il a une voix, et il décide à partir d'elle si vous êtes quelqu'un qui se plaint ou quelqu'un qui a raison. Dire « je conteste ce point » d'une voix qui monte à la fin transforme votre position en demande de permission — et l'autre entendra une question là où vous vouliez poser un fait.",
       note:"C'est exactement ce que dit l'experte à la fin du défi 2 : « si vous m'aviez appelée en criant, je vous aurais lu la clause. » La voix décide de la suite."},

      {t:'ana', h:"La surprise — tout se joue sur les deux dernières syllabes",
       p:"La phrase part normalement, puis grimpe brusquement sur les deux ou trois dernières syllabes. Souvent une question courte, souvent introduite par « comment ça » ou par la reprise du mot qui étonne.",
       mots:[['On dit','Cent vingt dollars pour le meuble de ma mère ?'],['La mélodie','plate, puis très haute à la fin',true],['Le repère','on répète le chiffre qui surprend']],
       say:"Cent vingt dollars pour le meuble de ma mère ?",
       note:"La surprise n'est pas le reproche. Si la voix monte trop tôt, la phrase devient « vous vous moquez de moi »."},

      {t:'ana', h:"La déception — la voix tombe dès la première syllabe",
       p:"Elle descend tout de suite et ne remonte jamais. Le débit est régulier, presque lent, et la phrase commence souvent par un « ah » ou un « bon » qui tombe avant le reste.",
       mots:[['On dit',"Ah. Je pensais que l'inventaire réglait la question."],['La mélodie','descendante du premier mot',true],['Le repère','un « ah » ou un « bon » en tête']],
       say:"Ah. Je pensais que l'inventaire réglait la question.",
       note:"Chez votre interlocuteur, c'est le signal qu'une réponse ne lui a pas plu. Il ne le dira pas ; la mélodie l'a déjà dit."},

      {t:'ana', h:"La volonté — la mélodie descend et les syllabes se détachent",
       p:"À l'inverse de la surprise : la mélodie descend, le débit ralentit, les syllabes se détachent. C'est la voix de l'engagement, et la seule qui convient à une négociation.",
       mots:[['On dit','Ce point-là, je le conteste, et je vais vous dire pourquoi.'],['La mélodie','descendante, appuyée sur « conteste »',true],['Le repère','on ne sourit pas en le disant']],
       say:"Ce point-là, je le conteste, et je vais vous dire pourquoi.",
       note:"La même phrase dite en montant devient une demande d'autorisation. C'est exactement l'inverse de ce qu'on voulait."},

      {t:'ana', h:"L'incompréhension — la voix freine au milieu",
       p:"On ne monte pas : on ralentit. Le débit se casse à l'endroit précis où le fil s'est rompu, avec un petit silence avant le mot en cause.",
       mots:[['On dit',"Le mot « subrogation »… vous l'entendez comment ?"],['La mélodie','un creux et un silence avant le mot',true],['Le repère',"on isole le mot avec la voix"]],
       say:"Le mot subrogation, vous l'entendez comment ?",
       note:"Le freinage seul dit « un mot m'échappe ». Sans lui, on entend « je n'ai rien suivi du tout »."},

      {t:'labo', h:"Les quatre intentions, à l'oreille",
       p:"Choisissez l'intention, puis l'exemple.",
       axes:[
         {id:'i', lbl:'Quelle intention ?', opts:[['a','surprise'],['b','déception'],['c','volonté'],['d','incompréhension']]},
         {id:'n', lbl:'Quel exemple ?', opts:[['1','le premier'],['2','le second']]}],
       out:{
         a1:{w:["Soixante cents la livre ?"], say:"Soixante cents la livre ?", n:'la voix monte d\'un coup sur « livre »'},
         a2:{w:["Comment ça, la rampe était déjà croche ?"], say:"Comment ça, la rampe était déjà croche ?", n:'« comment ça » annonce la surprise'},
         b1:{w:["Ah. Bon."], say:"Ah. Bon.", n:'deux syllabes qui tombent : la déception se passe de phrase'},
         b2:{w:["Je croyais que c'était couvert."], say:"Je croyais que c'était couvert.", n:'descendante du début à la fin'},
         c1:{w:["Je le conteste, ce point-là."], say:"Je le conteste, ce point-là.", n:'mélodie descendante, syllabes détachées'},
         c2:{w:["Je tiens à l'avoir par écrit."], say:"Je tiens à l'avoir par écrit.", n:'la voix pèse sur « tiens » et sur « écrit »'},
         d1:{w:["Attendez, je perds le fil."], say:"Attendez, je perds le fil.", n:'débit qui freine, mélodie creusée'},
         d2:{w:["Vous avez bien dit cinq cents ?"], say:"Vous avez bien dit cinq cents ?", n:'on isole le chiffre dont on n\'est pas sûr'},
       },
       note:"Répétez chaque exemple en forçant le trait. On rabat tout seul ensuite ; c'est en forçant qu'une mélodie s'installe."},

      {t:'ex', h:"La même idée, quatre intentions",
       p:"À gauche les mots ; à droite ce que la voix en fait.",
       rows:[
         ["Le meuble n'est pas couvert ?","surprise — la voix monte sur « couvert »"],
         ["Le meuble n'est pas couvert.","constat — la mélodie ne bouge pas"],
         ["Le meuble n'est pas couvert…","déception — la voix tombe et laisse ouvert"],
         ["Je veux la révision.","volonté — la mélodie descend, chaque mot porte"],
         ["Je veux la révision ?","la même phrase se retourne en doute"],
         ["Bon. Je demande la révision.","résignation — le « bon » tombe le premier"],
       ]},

      {t:'piege', h:"Trois défauts d'intonation au téléphone",
       rows:[
         ["faire monter la voix à la fin de chaque phrase","descendre quand on affirme",
          "Une mélodie qui monte partout transforme chaque affirmation en question et chaque question en demande d'autorisation. C'est le défaut le plus fréquent, et il vient de la prudence : on n'ose pas conclure."],
         ["tenir la même note du début à la fin","varier sur les trois phrases importantes",
          "Une voix plate se lit comme de l'indifférence, jamais comme du calme. Trois phrases variées dans un appel de vingt minutes suffisent."],
         ["baisser la voix au moment de demander","demander sur la même mélodie que le reste",
          "Beaucoup de gens s'effacent en formulant leur demande. Elle devient inaudible, et l'autre en conclut qu'elle est négociable à zéro."],
       ]},

      {t:'check', h:"Quatre mélodies à reconnaître",
       p:"Quatre questions, vite fait.",
       qs:[
         {q:"« Soixante cents la livre ? » exprime…", opts:["la surprise","la volonté"], ok:0,
          fb:"La montée brusque des dernières syllabes est la marque de la surprise."},
         {q:"Quand on affirme ce qu'on veut, la mélodie…", opts:["monte sur la fin","descend et pèse"], ok:1,
          fb:"Elle descend. Dite en montant, la même phrase quémande une permission."},
         {q:"« Ah. Bon. » dit avec une voix qui tombe exprime…", opts:["de la déception","de l'incompréhension"], ok:0,
          fb:"La chute dès la première syllabe est la marque de la déception."},
         {q:"Une voix parfaitement égale pendant tout l'appel se lit comme…", opts:["du calme","de l'indifférence polie"], ok:1,
          fb:"Comme de l'indifférence polie, alors qu'elle n'est que de la prudence."},
       ]},

      {t:'revoir', h:"À retenir",
       p:"Quatre mélodies : la <b>surprise</b> monte d'un coup à la fin ; la <b>déception</b> tombe dès la première syllabe ; la <b>volonté</b> descend et appuie ; l'<b>incompréhension</b> freine et laisse un silence avant le mot en cause. Au téléphone, votre interlocuteur n'a que cela pour vous juger."},
    ]
  },

  prPass: {
    eye:'Mini-leçon', tit:"La phrase passive, et qui elle efface",
    blocs:[
      {t:'texte', h:"La même scène, un autre sujet",
       p:"Le complément direct de la phrase active devient le sujet de la phrase passive, et celui qui agissait passe derrière, précédé de « par » — ou disparaît. <b>Le chauffeur a signé l'inventaire</b> devient <b>l'inventaire a été signé par le chauffeur</b>, puis, si l'on veut, <b>l'inventaire a été signé</b>. Rien n'a changé dans la réalité ; ce qui a changé, c'est de quoi la phrase parle, et qui elle nomme.",
       note:"C'est la seule transformation du français qui permet de décrire une action sans dire qui l'a faite. D'où sa fortune dans les contrats."},

      {t:'texte', h:"La recette, et le seul point de difficulté",
       p:"<b>être</b> au temps du verbe actif, plus le <b>participe passé</b>, accordé avec le sujet comme un adjectif. Présent : on exclut → <b>est exclu</b>. Passé composé : on a refusé → <b>a été refusé</b>. Futur : on refusera → <b>sera refusé</b>. Plus-que-parfait : on avait offert → <b>avait été offert</b>. La seule difficulté est de mettre « être » au bon temps : le participe, lui, ne bouge jamais.",
       note:"Repère : le nombre de mots augmente d'un à chaque étage. est exclu · a été exclu · avait été exclu."},

      {t:'texte', h:"Pourquoi les contrats l'adorent",
       p:"Parce qu'il permet de ne pas dire qui agit. « Sont exclus les dommages causés aux biens meubles » — exclus par qui ? Par l'assureur qui a rédigé la phrase, mais il n'apparaît nulle part. « Il a été établi que l'entreprise avait la garde du bien » — établi par qui, sur quelle base ? Chaque fois que vous lisez un passif sans « par », demandez-vous qui a disparu. C'est souvent exactement le renseignement qui manque, et c'est presque toujours une bonne question à poser.",
       note:"Ce n'est pas un procédé malhonnête, c'est un procédé d'écriture. Mais il faut savoir le défaire pour lire."},

      {t:'ex', h:"Défaire un passif pour voir qui manque",
       p:"À gauche, la phrase du contrat. À droite, la question qu'elle laisse ouverte.",
       rows:[
         ["Sont exclus les dommages causés aux biens meubles.","Exclus par qui, et depuis quelle version du contrat ?"],
         ["Il a été établi que l'entreprise avait la garde du bien.","Établi par qui, à partir de quelle pièce ?"],
         ["La décision vous sera communiquée par écrit.","Par qui, et dans quel délai exactement ?"],
         ["Le dommage retenu s'établit à neuf cent quarante dollars.","Retenu par qui, et écarté sur quoi ?"],
         ["La responsabilité est régie par le contrat de transport.","Quel contrat, quelle clause, signée quand ?"],
         ["Aucune déclaration de valeur n'a été proposée.","Voilà le passif qui sert l'assuré : il pose le fait sans accuser."],
       ]},

      {t:'piege', h:"Trois confusions autour du passif",
       rows:[
         ["« le meuble est fendu » comme preuve d'un dommage","« le meuble a été fendu pendant le portage »",
          "Le premier décrit un état, qui peut dater de trente ans. Le second décrit une action, située dans le temps. Devant un assureur, seul le second pèse quelque chose."],
         ["mettre le participe au temps voulu","mettre l'auxiliaire être au temps voulu",
          "On écrit « a été refusé » et non « a refusé été ». Le participe reste au participe ; c'est « être » qui voyage dans les temps."],
         ["laisser le participe invariable","accorder avec le sujet, comme un adjectif",
          "La rampe a été <b>tordue</b>, les boîtes ont été <b>laissées</b>, les dommages sont <b>exclus</b>. L'oubli se voit immédiatement à l'écrit."],
       ]},

      {t:'check', h:"Quatre décisions sur le passif",
       p:"Quatre questions, vite fait.",
       qs:[
         {q:"« On a refusé la réclamation » au passif donne…", opts:["la réclamation a été refusée","la réclamation est refusée"], ok:0,
          fb:"Passé composé actif → passé composé passif : « a été refusée »."},
         {q:"Dans « il a été établi que… », qui a établi ?", opts:["c'est écrit plus loin","la phrase ne le dit pas, et c'est le point"], ok:1,
          fb:"Le passif sans « par » efface l'agent. C'est presque toujours une bonne question à poser."},
         {q:"« Aucune déclaration ne m'a été proposée » est utile parce que…", opts:["c'est plus poli","cela pose le fait sans accuser une personne"], ok:1,
          fb:"Le fait devient discutable ; nommer le chauffeur le rendrait niable."},
         {q:"« Les boîtes ont été laissé dehors » — que corrige-t-on ?", opts:["l'auxiliaire","l'accord du participe : laissées"], ok:1,
          fb:"Le participe s'accorde avec le sujet : les boîtes ont été laissées."},
       ]},

      {t:'revoir', h:"À retenir",
       p:"<b>être</b> au temps du verbe + <b>participe accordé</b>. Le passif déplace le sujet et permet d'<b>effacer celui qui agit</b> : dans un contrat, cherchez toujours qui a disparu. Et retenez la phrase qui vous servira : « aucune déclaration de valeur ne m'a été proposée » se discute, « votre chauffeur ne me l'a pas proposée » se nie."},
    ]
  },

  t11: {
    eye:'Mini-leçon', tit:"Les six mots qui décident d'une police",
    blocs:[
      {t:'texte', h:"Trois protections dans un seul contrat",
       p:"Une police de locataire n'est pas une protection, c'en est trois, et elles n'ont rien à voir entre elles. La <b>section des biens</b> paie ce qui vous appartient. La <b>responsabilité civile</b> paie ce que vous faites subir aux autres. Les <b>frais de subsistance</b> paient le supplément si votre logement devient inhabitable. Trois plafonds différents, parfois trois franchises différentes.",
       note:"Premier réflexe devant un refus : la réclamation refusée sous une section peut parfois être présentée sous une autre."},

      {t:'texte', h:"La franchise, et le calcul qu'on ne fait jamais",
       p:"La franchise est la part qui reste toujours à votre charge, et elle s'applique <b>par sinistre</b>, jamais par objet. Avec une franchise de cinq cents dollars : un dommage de mille deux cents vous rapporte sept cents ; un dommage de quatre cents ne vous rapporte rien du tout, et déclarer ne servirait qu'à inscrire un dossier à votre nom. Faites la soustraction avant de décrocher le téléphone.",
       note:"Une franchise plus haute fait baisser la prime. C'est le seul levier vraiment efficace sur le prix d'une police."},

      {t:'texte', h:"Valeur à neuf ou valeur au jour du sinistre",
       p:"Deux façons d'indemniser, et l'écart entre les deux peut atteindre les trois quarts du montant. La <b>valeur au jour du sinistre</b> retranche la dépréciation : un téléviseur de huit ans vous est remboursé au prix d'un téléviseur de huit ans, c'est-à-dire presque rien. La <b>valeur à neuf</b> paie l'équivalent neuf, souvent sur présentation d'une preuve de remplacement. Une seule ligne du sommaire dit laquelle vous avez, et c'est celle que personne ne lit.",
       note:"« Sur présentation d'une preuve de remplacement » veut dire : on vous verse d'abord la valeur au jour du sinistre, et le complément quand vous avez racheté."},

      {t:'ex', h:"Six mots, six effets concrets",
       p:"À gauche le mot, à droite ce qu'il change pour vous.",
       rows:[
         ["une prime","Ce que vous payez par année, quoi qu'il arrive"],
         ["une franchise","Ce qui se soustrait à chaque sinistre, quoi qu'il arrive"],
         ["un plafond","Le maximum que l'assureur versera, jamais une promesse"],
         ["une sous-limite","Un plafond particulier caché sous le plafond général"],
         ["un avenant","Une protection ajoutée par écrit à un contrat qui ne l'offrait pas"],
         ["une exclusion","Un cas annoncé d'avance comme non couvert : à lire en premier"],
       ]},

      {t:'texte', h:"Les exclusions se lisent avant les protections",
       p:"C'est contre-intuitif et c'est pourtant l'ordre utile. Les protections décrivent un monde généreux ; les exclusions décrivent le vrai contrat. Les trois quarts des refus s'appuient sur une exclusion, et la plupart d'entre elles sont raisonnables — l'usure, la négligence, le vice caché, les biens confiés à un transporteur professionnel. Ce que vous cherchez en les lisant, ce n'est pas une injustice : c'est de savoir d'avance sur quoi vous n'êtes pas couvert.",
       note:"Le jour où l'une d'elles vous est opposée, vous n'aurez plus qu'à en lire les mots exacts. Vous saurez déjà laquelle."},

      {t:'piege', h:"Trois idées fausses sur une police d'assurance",
       rows:[
         ["« je suis assurée, donc je suis couverte »","« je suis assurée pour ceci, jusqu'à ce montant, moins la franchise »",
          "Aucune police ne couvre tout. Savoir pour quoi et jusqu'où est la seule façon de ne pas être surpris au pire moment."],
         ["« cinquante mille dollars, c'est ce que je vais toucher »","c'est le maximum, jamais un montant garanti",
          "Ce que vous toucherez dépend de l'inventaire, du mode d'indemnisation et de la franchise. Le plafond ne se rencontre presque jamais."],
         ["« mes bijoux sont dans les cinquante mille »","ils sont dans leur sous-limite, à deux mille",
          "Les sous-limites sont le piège le plus fréquent : bijoux, argent comptant, vélos, instruments, objets d'art. Au-delà, il faut un avenant et une déclaration."],
       ]},

      {t:'check', h:"Quatre calculs à faire de tête",
       p:"Quatre questions, vite fait.",
       qs:[
         {q:"Franchise de 500 $, dommage de 940 $. Vous touchez…", opts:["940 $","440 $"], ok:1,
          fb:"La franchise se soustrait : 940 moins 500 égale 440."},
         {q:"Franchise de 500 $, dommage de 400 $. Vous…", opts:["réclamez quand même","ne réclamez pas, ça ne rapporterait rien"], ok:1,
          fb:"Rien ne serait versé, et un dossier serait inscrit à votre nom pour rien."},
         {q:"Trois objets abîmés dans un même dégât d'eau. La franchise s'applique…", opts:["trois fois","une seule fois"], ok:1,
          fb:"Par sinistre, jamais par objet. C'est un seul événement."},
         {q:"Une bague de 3 500 $ sous une sous-limite de 2 000 $, sans avenant. Vous touchez au plus…", opts:["3 500 $","2 000 $"], ok:1,
          fb:"La sous-limite plafonne, et pas un cent de plus sans avenant ni déclaration."},
       ]},

      {t:'revoir', h:"À retenir",
       p:"Trois protections (<b>biens</b>, <b>responsabilité civile</b>, <b>frais de subsistance</b>), une <b>franchise</b> qui se soustrait par sinistre, un <b>mode d'indemnisation</b> qui change tout, des <b>sous-limites</b> cachées sous le plafond, des <b>avenants</b> qui ajoutent et des <b>exclusions</b> qui retirent. Lisez les exclusions en premier."},
    ]
  },

  t1clar: {
    eye:'Mini-leçon', tit:"Faire clarifier, résumer, faire le point",
    blocs:[
      {t:'texte', h:"Vous ne comprendrez pas tout, et ce n'est pas le problème",
       p:"Dans une conversation technique menée dans une langue qui n'est pas la première, il y aura des mots qui vous échapperont. C'est certain, c'est normal, et personne n'en tirera de conclusion. Le seul comportement qui vous nuit est de faire semblant : le malentendu ne disparaît pas, il se paie dix minutes plus tard, quand vous répondez à côté d'une question que vous aviez mal saisie.",
       note:"Trois secondes pour faire préciser un mot, contre dix minutes pour rattraper une réponse à côté. Le calcul n'est pas serré."},

      {t:'texte', h:"Faire clarifier, une fois, sur le mot qui compte",
       p:"« Qu'entendez-vous exactement par “valeur à neuf” ? » · « Le mot “avenant”, vous l'employez dans quel sens ? » · « Pouvez-vous me redire ça autrement ? » Ces trois formules coûtent trois secondes et vous font passer pour rigoureuse plutôt que perdue. La limite : une fois, sur le mot qui décide de quelque chose. Trois fois de suite sur des mots secondaires, et vous perdez le fil pour de bon.",
       note:"Choisissez : dans une explication de dix minutes, il y a un ou deux mots qui portent la décision. Ce sont ceux-là."},

      {t:'texte', h:"Résumer, c'est reformuler avec ses mots à soi",
       p:"« Je résume, pour être certaine : je déclare, je monte un inventaire avec des preuves datées, j'attends l'expert. » Le résumé n'est utile que s'il emploie <b>vos</b> mots : répéter ceux de l'autre ne prouve rien du tout, ni à lui ni à vous. C'est le seul moyen de découvrir un malentendu pendant qu'il ne coûte encore rien, et le programme du niveau 8 le nomme explicitement parmi ce qu'on attend de vous.",
       note:"Placez-le à deux endroits : au milieu d'une explication longue, et juste avant de raccrocher."},

      {t:'ex', h:"Six formules, six moments",
       p:"À gauche ce qu'on dit, à droite le moment où on le dit.",
       rows:[
         ["Qu'entendez-vous exactement par… ?","Dès qu'un mot technique décide de quelque chose"],
         ["Sur quelle clause vous appuyez-vous ?","Dès qu'une décision vous est annoncée"],
         ["Ce montant, il est avant ou après la franchise ?","Avant d'accepter un chiffre, jamais après"],
         ["Reprenons les trois points l'un après l'autre.","Au début d'une conversation qui en contient plusieurs"],
         ["Je résume, pour être certaine : …","Au milieu, puis à la fin"],
         ["Je vous envoie les pièces aujourd'hui.","En raccrochant, toujours"],
       ]},

      {t:'texte', h:"Celui qui structure mène la conversation",
       p:"« Reprenons les trois points l'un après l'autre » n'est pas une formule de politesse : c'est une prise de contrôle. Dans une conversation longue, la personne qui découpe décide de l'ordre, du temps passé sur chaque point et du moment où l'on passe au suivant. Ce n'est pas nécessairement celle qui a le dossier devant elle. Annoncer le nombre de points, puis les prendre dans l'ordre, est ce qui empêche une décision défavorable de se noyer dans le reste.",
       note:"C'est ce qu'Amira fait dès la troisième réplique du défi 2, et c'est pour cela que l'appel se déroule à son avantage."},

      {t:'piege', h:"Trois façons de mal faire préciser",
       rows:[
         ["« je n'ai rien compris »","« le mot “subrogation”, vous l'entendez comment ? »",
          "La première phrase oblige l'autre à tout recommencer et donne l'impression d'un mur. La seconde désigne le point exact et se règle en une phrase."],
         ["répéter les mots de l'autre pour résumer","reformuler avec ses propres mots",
          "Répéter ne prouve rien : on peut répéter une phrase qu'on n'a pas comprise. Seule la reformulation révèle un malentendu."],
         ["poser toutes ses questions à la fin","les poser au fil de l'eau, une à la fois",
          "À la fin, l'autre a déjà l'esprit ailleurs et répond vite. Au fil de l'eau, chaque réponse corrige la suite de l'explication."],
       ]},

      {t:'check', h:"Quatre réflexes de conversation",
       p:"Quatre questions, vite fait.",
       qs:[
         {q:"Un mot technique vous échappe. Vous…", opts:["faites semblant et vérifierez après","le faites préciser tout de suite, une fois"], ok:1,
          fb:"Trois secondes maintenant, contre une réponse à côté dix minutes plus tard."},
         {q:"Résumer efficacement, c'est…", opts:["répéter les mots de l'autre","reformuler avec les siens"], ok:1,
          fb:"Répéter ne prouve rien. Seule la reformulation fait apparaître un malentendu."},
         {q:"On vous annonce un refus. La première question est…", opts:["« pourquoi ? »","« sur quelle clause vous appuyez-vous ? »"], ok:1,
          fb:"« Pourquoi » appelle une opinion ; « quelle clause » appelle un texte, qu'on pourra relire."},
         {q:"Dans une conversation à trois points, qui mène ?", opts:["celui qui a le dossier","celui qui découpe et annonce l'ordre"], ok:1,
          fb:"Structurer est une prise de contrôle, et elle est offerte à qui la prend."},
       ]},

      {t:'revoir', h:"À retenir",
       p:"Faire clarifier <b>une fois, sur le mot qui compte</b>. Faire préciser une clause plutôt qu'une raison. Résumer <b>avec ses propres mots</b>, au milieu et à la fin. Découper une conversation longue en points annoncés. Et fermer sur une <b>action datée</b>, sinon l'échange se répétera dans huit jours."},
    ]
  },

  t1subj: {
    eye:'Mini-leçon', tit:"Le subjonctif présent, et ce qui le déclenche",
    blocs:[
      {t:'texte', h:"Un mode, pas un temps",
       p:"Le subjonctif ne situe rien dans le temps : il dit comment celui qui parle considère le fait. Avec l'indicatif, le fait est posé comme réel. Avec le subjonctif, il est envisagé, voulu, craint, concédé — mais pas affirmé. « Je sais qu'elle <b>vient</b> » contre « je veux qu'elle <b>vienne</b> » : dans le second cas, elle n'est peut-être jamais venue.",
       note:"C'est pourquoi il apparaît presque toujours dans une subordonnée, après « que » : il faut un verbe principal pour dire comment on considère le fait."},

      {t:'texte', h:"Comment il se fabrique, en une règle et six exceptions",
       p:"On prend la troisième personne du pluriel du présent, on retire <b>-ent</b>, on ajoute <b>-e, -es, -e, -ions, -iez, -ent</b>. <span class='savoir-ex'>ils écriv<s>ent</s> → que j'écrive · ils finiss<s>ent</s> → que tu finisses · ils envoi<s>ent</s> → qu'elle envoie.</span> Les formes « nous » et « vous » se prennent, elles, sur l'imparfait : que nous envoy<b>ions</b>, que vous envoy<b>iez</b>. Six verbes seulement échappent à tout : être, avoir, aller, faire, pouvoir, savoir.",
       note:"Vouloir et valoir sont irréguliers eux aussi (que je veuille, qu'il vaille), mais ils suivent au moins la terminaison."},

      {t:'labo', h:"Les six irréguliers, en entier",
       p:"Choisissez un verbe et une personne.",
       axes:[
         {id:'v', lbl:'Quel verbe ?', opts:[['e','être'],['a','avoir'],['g','aller'],['f','faire'],['p','pouvoir'],['s','savoir']]},
         {id:'p', lbl:'Quelle personne ?', opts:[['1','je / il'],['2','nous']]}],
       out:{
         e1:{w:["que je sois"], say:"que je sois", n:'sois, sois, soit — la seule forme sans -e'},
         e2:{w:["que nous soyons"], say:"que nous soyons", n:'soyons, soyez'},
         a1:{w:["que j'aie"], say:"que j'aie", n:'aie, aies, ait — sans s à la troisième personne'},
         a2:{w:["que nous ayons"], say:"que nous ayons", n:'ayons, ayez'},
         g1:{w:["que j'aille"], say:"que j'aille", n:'aille, ailles, aille'},
         g2:{w:["que nous allions"], say:"que nous allions", n:'allions, alliez — la forme régulière revient'},
         f1:{w:["que je fasse"], say:"que je fasse", n:'fasse partout, sauf fassions et fassiez'},
         f2:{w:["que nous fassions"], say:"que nous fassions", n:'fassions, fassiez'},
         p1:{w:["que je puisse"], say:"que je puisse", n:'puisse, puisses, puisse'},
         p2:{w:["que nous puissions"], say:"que nous puissions", n:'puissions, puissiez'},
         s1:{w:["que je sache"], say:"que je sache", n:'sache, saches, sache'},
         s2:{w:["que nous sachions"], say:"que nous sachions", n:'sachions, sachiez'},
       },
       note:"Apprenez-les comme un bloc : ils reviennent dans huit phrases sur dix, et les autres verbes se déduisent de la règle."},

      {t:'ex', h:"Ce qui le déclenche, et ce qui ne le déclenche pas",
       p:"À gauche, subjonctif. À droite, indicatif — et l'idée est parfois la même.",
       rows:[
         ["il faut que vous déclariez","il est certain que vous déclarerez"],
         ["j'aimerais qu'on revoie","j'espère qu'on revoit"],
         ["bien que la clause soit claire","même si la clause est claire"],
         ["je ne crois pas que ce soit couvert","je crois que c'est couvert"],
         ["avant que l'expert vienne","après que l'expert est venu"],
         ["à moins que vous ayez une pièce","parce que vous avez une pièce"],
         ["pour que le dossier avance","puisque le dossier avance"],
         ["sans que personne s'en aperçoive","alors que personne ne s'en aperçoit"],
       ]},

      {t:'texte', h:"Les trois emplois qui servent dans une réclamation",
       p:"<b>La nécessité</b> : « il faut que je déclare aujourd'hui », « il est nécessaire que la clause soit citée » — c'est l'emploi que le programme du niveau 8 nomme en toutes lettres. <b>Le souhait poli</b> : « j'aimerais que la décision me parvienne par écrit », qui demande sans exiger. <b>La concession</b> : « bien que la clause existe, elle vise le transport », qui reconnaît avant de retourner. Trois emplois, et vous avez de quoi mener toute la conversation du défi 2.",
       note:"Le quatrième, le doute — « je ne crois pas que cette exclusion puisse s'appliquer » —, est le plus poli des désaccords."},

      {t:'piege', h:"Quatre déclencheurs qui trompent",
       rows:[
         ["« même si la clause soit claire »","« même si la clause est claire »",
          "« Bien que » veut le subjonctif, « même si » veut l'indicatif, et les deux disent pourtant la même chose. C'est la confusion la plus fréquente du niveau."],
         ["« après que vous ayez envoyé »","« après que vous aurez envoyé »",
          "« Avant que » veut le subjonctif — l'événement n'a pas eu lieu. « Après que » veut l'indicatif — il a eu lieu. L'usage courant les mêle ; l'écrit soigné ne les mêle pas."],
         ["« j'espère que ce soit réglé »","« j'espère que ce sera réglé »",
          "Espérer est optimiste : il pose le fait comme probable, donc indicatif. Souhaiter, vouloir et aimer, eux, appellent le subjonctif."],
         ["« je pense que ce soit couvert »","« je pense que c'est couvert »",
          "Penser et croire à la forme affirmative posent le fait : indicatif. À la forme négative ou interrogative, le doute revient et le subjonctif avec lui."],
       ]},

      {t:'check', h:"Quatre décisions sur le mode",
       p:"Quatre questions, vite fait.",
       qs:[
         {q:"« Bien que la clause ___ claire »", opts:["est","soit"], ok:1,
          fb:"« Bien que » veut le subjonctif, toujours."},
         {q:"« Même si la clause ___ claire »", opts:["est","soit"], ok:0,
          fb:"« Même si » veut l'indicatif, alors que l'idée est la même."},
         {q:"« Il faut que vous ___ une preuve datée »", opts:["avez","ayez"], ok:1,
          fb:"La nécessité déclenche le subjonctif : que vous ayez."},
         {q:"« J'espère que le dossier ___ réglé cette semaine »", opts:["sera","soit"], ok:0,
          fb:"Espérer pose le fait comme probable : indicatif futur."},
       ]},

      {t:'revoir', h:"À retenir",
       p:"Radical de la <b>troisième personne du pluriel</b>, plus les terminaisons ; <b>nous</b> et <b>vous</b> sur l'imparfait ; six irréguliers à savoir par cœur. Trois déclencheurs utiles ici : la <b>nécessité</b> (il faut que), le <b>souhait</b> (j'aimerais que), la <b>concession</b> (bien que). Et un piège permanent : <i>bien que</i> + subjonctif, <i>même si</i> + indicatif."},
    ]
  },

  t1rel: {
    eye:'Mini-leçon', tit:"Le pronom relatif après une préposition",
    blocs:[
      {t:'texte', h:"Ce que ça résout, et pourquoi les contrats en sont pleins",
       p:"Une phrase relative relie deux idées sans répéter le nom. <b>La clause. Vous vous appuyez sur cette clause.</b> devient <b>la clause sur laquelle vous vous appuyez</b>. Le gain est réel : une seule phrase, un seul mouvement de lecture. Le coût aussi : dès qu'un texte en enchaîne trois, il faut savoir à quoi chacune renvoie, et c'est exactement ce qui rend un contrat illisible à qui ne les maîtrise pas.",
       note:"Vous n'avez donc pas à les aimer : vous avez à savoir les défaire pour lire, et à en produire deux ou trois pour écrire."},

      {t:'texte', h:"La règle en trois mots : préposition + lequel",
       p:"<b>lequel</b> s'accorde avec le nom qu'il reprend : lequel, laquelle, lesquels, lesquelles. Avec la préposition <b>à</b>, il se soude : auquel, à laquelle, auxquels, auxquelles. Avec <b>de</b>, il se soude aussi : duquel, de laquelle, desquels, desquelles. Avec toutes les autres — sur, dans, par, pour, avec, sans, chez — il reste séparé : sur lequel, dans laquelle, par lesquels.",
       note:"« à laquelle » ne se soude pas à l'écrit, contrairement à « auquel ». C'est une bizarrerie d'orthographe, pas une règle de grammaire."},

      {t:'ex', h:"La phrase simple, puis la relative",
       p:"À gauche, les deux phrases séparées. À droite, la relative — et remarquez que la préposition ne change jamais.",
       rows:[
         ["Vous vous appuyez sur cette clause.","la clause sur laquelle vous vous appuyez"],
         ["Je me fie à cette évaluation.","l'évaluation à laquelle je me fie"],
         ["Je ne renonce pas à ce point.","le point auquel je ne renonce pas"],
         ["Je vous parle de ce meuble.","le meuble dont je vous parle"],
         ["Tout passe par ce numéro.","le numéro par lequel tout passe"],
         ["Je négocie avec cette personne.","la personne avec qui je négocie"],
         ["Mon estimation repose sur ces annonces.","les annonces sur lesquelles repose mon estimation"],
         ["Le meuble a été porté dans cet escalier.","l'escalier dans lequel le meuble a été porté"],
       ]},

      {t:'texte', h:"« dont » et ses limites",
       p:"<b>dont</b> remplace « de + quelque chose », et il couvre à lui seul la moitié des besoins : le meuble <b>dont</b> je vous parle, une clause <b>dont</b> le sens est équivoque, les avenants <b>dont</b> je bénéficie. Sa limite est nette et se retient : il ne s'emploie <b>jamais</b> après une autre préposition. On dit « au bas <b>duquel</b> », « à côté <b>duquel</b> », « au terme <b>desquels</b> » — jamais « au bas dont ».",
       note:"Repère pratique : si le groupe qui précède contient déjà une préposition (au bas de, à côté de, en vertu de), c'est duquel, pas dont."},

      {t:'texte', h:"Les deux raccourcis : « qui » et « où »",
       p:"Après une préposition, pour une <b>personne</b>, le français préfère <b>qui</b> : la personne <b>à qui</b> j'ai parlé, l'expert <b>avec qui</b> je négocie, l'ébéniste <b>chez qui</b> je suis allée. « à laquelle » n'est pas faux, il est seulement lourd. Et pour un <b>lieu</b> ou un <b>moment</b>, <b>où</b> remplace tout : le jour <b>où</b> le camion est reparti, l'escalier <b>où</b> le meuble a été fendu.",
       note:"« où » ne s'emploie que pour un lieu ou un temps. « La question où je pense » ne se dit pas : c'est « à laquelle »."},

      {t:'piege', h:"Trois erreurs de relatif, et le repère qui les évite",
       rows:[
         ["choisir le relatif au jugé","refaire la phrase simple et écouter la préposition",
          "« Je me fie <b>à</b> » donne « à laquelle » ; « je compte <b>sur</b> » donne « sur laquelle ». La préposition appartient au verbe et ne se devine pas : elle se retrouve en refaisant la phrase."],
         ["« au bas dont la page »","« au bas de laquelle »",
          "« dont » ne survit à aucune préposition qui le précède. Dès qu'il y en a une, on repasse à duquel, de laquelle, desquels."],
         ["« la clause dont je m'appuie »","« la clause sur laquelle je m'appuie »",
          "S'appuyer se construit avec « sur », pas avec « de ». L'erreur vient de l'habitude de « dont », qui semble aller partout."],
       ]},

      {t:'check', h:"Quatre relatifs à placer",
       p:"Quatre questions, vite fait.",
       qs:[
         {q:"« Le point ___ je ne renonce pas » (renoncer à…)", opts:["dont","auquel"], ok:1,
          fb:"Renoncer se construit avec « à » : auquel."},
         {q:"« La clause ___ le sens est équivoque »", opts:["dont","à laquelle"], ok:0,
          fb:"« le sens de la clause » : dont remplace « de + la clause »."},
         {q:"« L'expert ___ je négocie » (négocier avec…)", opts:["avec lequel","avec qui"], ok:1,
          fb:"Les deux sont corrects, mais pour une personne on préfère « avec qui »."},
         {q:"« Le jour ___ le camion est reparti »", opts:["où","pendant lequel"], ok:0,
          fb:"« où » couvre le lieu et le moment, et il est plus léger."},
       ]},

      {t:'revoir', h:"À retenir",
       p:"<b>Préposition + lequel</b>, accordé au nom repris ; soudé avec <i>à</i> et <i>de</i>. <b>dont</b> pour « de quelque chose », mais jamais derrière une autre préposition. <b>qui</b> pour les personnes, <b>où</b> pour les lieux et les moments. Et le seul repère fiable : <b>refaire la phrase simple</b> et écouter quelle préposition le verbe réclame."},
    ]
  },

  t1prop: {
    eye:'Mini-leçon', tit:"Lire un sommaire de police",
    blocs:[
      {t:'texte', h:"Deux pages qui résument soixante",
       p:"Le sommaire n'est pas le contrat : c'est le résumé que l'assureur en fait, et il est envoyé chaque année avec le renouvellement. Il est exact, mais il ne contient <b>aucune exclusion détaillée</b>. On y lit ses plafonds, ses franchises et son mode d'indemnisation en trois minutes ; on va chercher les exclusions dans le contrat lui-même, qui dort dans un tiroir depuis la signature.",
       note:"Trois minutes par année, au moment du renouvellement. C'est le meilleur rapport effort-résultat de toute cette affaire."},

      {t:'ex', h:"Ce qu'on cherche, section par section",
       p:"À gauche, où regarder. À droite, ce qu'on note.",
       rows:[
         ["Section A — vos biens","Le plafond, la franchise, et surtout le mode d'indemnisation"],
         ["Les sous-limites","Bijoux, argent, vélos, instruments : les montants qui plafonnent en dessous du plafond"],
         ["Section B — responsabilité civile","Le montant par événement, et le fait qu'il n'y a pas de franchise"],
         ["Section C — frais de subsistance","Le pourcentage et la durée maximale"],
         ["Les avenants","Ce qu'ils ajoutent, et leur franchise propre, souvent différente"],
         ["Le pied de page","Le délai de déclaration, la prime, et le nombre de versements"],
       ]},

      {t:'texte', h:"Un plafond n'est pas une promesse",
       p:"« Jusqu'à cinquante mille dollars » ne signifie pas qu'on vous versera cinquante mille dollars : cela signifie qu'on ne dépassera pas ce montant. Ce que vous toucherez dépend de trois choses, dans cet ordre — ce que votre inventaire démontre, le mode d'indemnisation, puis la franchise. Le plafond, lui, n'est presque jamais atteint : il ne sert qu'à décider si votre police est trop petite pour ce que vous possédez.",
       note:"L'exercice utile, une fois dans sa vie : faire le tour de son logement et estimer le coût de tout racheter neuf. La plupart des gens sous-estiment de moitié."},

      {t:'texte', h:"Les sous-limites, ou le piège du plafond confortable",
       p:"Sous le plafond global se cachent presque toujours des plafonds particuliers : deux mille dollars pour l'ensemble des bijoux, trois cents pour l'argent comptant, mille cinq cents pour les vélos, deux mille pour les instruments de musique. Un objet qui dépasse sa sous-limite est couvert jusqu'à ce montant, et pas un cent de plus, même si le plafond général est de cinquante mille. Pour aller au-delà, il faut un <b>avenant</b> et une <b>déclaration de valeur</b>, parfois une évaluation.",
       note:"C'est la découverte la plus désagréable d'un sinistre, et elle se prévient en trois minutes de lecture."},

      {t:'piege', h:"Trois lignes qu'on saute et qu'on ne devrait pas",
       rows:[
         ["le mode d'indemnisation","une seule ligne, souvent au bas d'un bloc",
          "« Valeur à neuf » ou « valeur au jour du sinistre » : c'est la ligne qui a le plus d'effet sur ce que vous toucherez, et c'est celle que personne ne lit."],
         ["la franchise des avenants","elle est souvent différente de la principale",
          "Un avenant de refoulement d'égout porte fréquemment une franchise de mille dollars quand le contrat de base en a cinq cents. Rien ne le signale à l'écran."],
         ["le délai de déclaration","une date, pas une recommandation",
          "Passé le délai inscrit, l'assureur peut refuser sans examiner. Trente jours paraît long le jour du sinistre et court six semaines plus tard."],
       ]},

      {t:'check', h:"Quatre lectures du sommaire",
       p:"Quatre questions, vite fait.",
       qs:[
         {q:"« Jusqu'à 50 000 $ » signifie…", opts:["ce que vous toucherez","le maximum que l'assureur versera"], ok:1,
          fb:"Un plafond n'est jamais un montant garanti."},
         {q:"Une bague de 3 500 $ sous une sous-limite de 2 000 $ demande…", opts:["rien à faire de particulier","un avenant et une déclaration de valeur"], ok:1,
          fb:"Au-delà de la sous-limite, il faut ajouter la protection par écrit."},
         {q:"La section « responsabilité civile » sert quand…", opts:["vos biens sont abîmés","vous causez un dommage à autrui"], ok:1,
          fb:"C'est la protection de ce que vous faites subir, pas de ce que vous possédez."},
         {q:"Un avenant peut porter…", opts:["la même franchise que le contrat","une franchise différente, souvent plus élevée"], ok:1,
          fb:"Souvent différente, et rien ne le signale : il faut lire la ligne."},
       ]},

      {t:'revoir', h:"À retenir",
       p:"Le sommaire donne les <b>plafonds</b>, les <b>franchises</b> et le <b>mode d'indemnisation</b> ; le contrat donne les <b>exclusions</b>. Un plafond est un maximum, jamais une promesse. Les <b>sous-limites</b> sont le vrai piège, et elles se règlent par un avenant. Trois minutes par année, au renouvellement."},
    ]
  },

  t21: {
    eye:'Mini-leçon', tit:"Contester sans se faire raccrocher au nez",
    blocs:[
      {t:'texte', h:"Un désaccord se conduit, il ne s'exprime pas",
       p:"La différence entre une réclamation qui aboutit et une qui s'enlise ne tient presque jamais au dossier : elle tient à la conduite de la conversation. La personne en face n'a pas décidé de vous nuire, elle applique un texte, et elle a la possibilité — non l'obligation — de porter votre cas plus haut. Tout votre travail consiste à lui donner envie de le faire, et à lui en fournir les moyens.",
       note:"« Si vous m'aviez appelée en criant, je vous aurais lu la clause et j'aurais raccroché. » C'est l'experte elle-même qui le dit, à la fin du défi 2."},

      {t:'texte', h:"Étape 1 — accepter d'abord ce qui est juste",
       p:"Un dossier contient presque toujours un point qui ne tient pas. Le lâcher tout de suite, à voix haute, et le nommer, coûte ce point-là et achète l'attention sur les autres. Amira accepte le montant des livres, puis accepte le refus sur la rampe — deux concessions en trois répliques — et c'est ce qui lui vaut d'être écoutée sur le troisième point. Celui qui conteste tout en bloc se fait lire la clause.",
       note:"Ce n'est pas une politesse ni une faiblesse : c'est le calcul le plus rentable de toute la conversation."},

      {t:'texte', h:"Étape 2 — exiger la clause, mot pour mot",
       p:"« Sur quelle clause vous appuyez-vous ? », puis « pouvez-vous me la relire ? Je veux les mots exacts. » Un refus sans clause n'est pas un refus : c'est une opinion, et elle se retire. Un refus avec clause devient un texte, et un texte se lit — c'est là que se trouvent presque toujours les brèches. Ici, la clause dit « pendant leur transport », et le meuble a été fendu pendant le portage. La distinction n'est pas une astuce : c'est le contrat lui-même qui l'écrit.",
       note:"Notez la clause par écrit pendant qu'on vous la lit. Elle sera le premier paragraphe de votre lettre."},

      {t:'ex', h:"Les cinq étapes, et la phrase qui les ouvre",
       p:"À gauche l'étape, à droite ce qu'on dit pour l'ouvrir.",
       rows:[
         ["1. Découper","Reprenons les trois points l'un après l'autre."],
         ["2. Concéder","Celle-là, je l'accepte. Elle est logique et la clause est claire."],
         ["3. Exiger la clause","Sur quelle clause vous appuyez-vous, exactement ?"],
         ["4. Retourner","Certes la clause existe. Or elle parle du transport."],
         ["5. Proposer","Ce que je propose, c'est huit cent cinquante dollars, contre ma renonciation."],
       ]},

      {t:'texte', h:"Étape 3 — une pièce datée derrière chaque affirmation",
       p:"« Le meuble était en parfait état » ne pèse rien : c'est un souvenir. « L'inventaire signé à huit heures ne note aucun dommage, et la photographie horodatée à onze heures vingt-deux montre la fente » pèse tout : ce sont deux documents et un intervalle de trois heures pendant lequel quelqu'un d'autre avait la garde. Datez chaque affirmation, ou taisez-la — une affirmation sans date affaiblit celles qui en ont une.",
       note:"Trois pièces datées valent mieux que dix pièces en vrac. Numérotez-les, et citez-les par leur numéro."},

      {t:'texte', h:"Étape 4 — proposer un chiffre, toujours",
       p:"Une contestation sans proposition reste sur un bureau : personne ne sait quoi en faire, et elle attend qu'on ait le temps. Un compromis chiffré, appuyé sur une estimation extérieure, donne à votre interlocutrice quelque chose de concret à soumettre à son réviseur — un dossier qui se règle plutôt qu'un dossier qui s'ouvre. Offrez toujours une contrepartie : la renonciation à toute autre réclamation en est une, et elle ne vous coûte rien si vous n'avez plus rien à réclamer.",
       note:"Le chiffre se justifie : trois annonces comparables, une évaluation écrite, une facture d'origine. Un chiffre sorti de nulle part se refuse sans discussion."},

      {t:'piege', h:"Quatre façons de perdre un dossier qui tient",
       rows:[
         ["tout contester en bloc","concéder d'abord ce qui est juste",
          "Le refus de principe se traite comme du bruit. Une concession explicite change complètement la lecture de la suite."],
         ["s'emporter, même une fois","garder la mélodie basse et le débit lent",
          "Une seule phrase criée referme la conversation pour de bon, et vous ne saurez jamais ce qu'elle vous a coûté."],
         ["encaisser un chèque du tiers responsable","remercier, ne rien signer, ne rien encaisser",
          "Un montant accepté d'un tiers ferme le dossier tout seul, sans que personne vous en avertisse. C'est le piège le plus coûteux du module."],
         ["accepter la décision de vive voix","demander la décision par écrit, avec la clause",
          "Ce qui n'est pas écrit n'existe pas six semaines plus tard, et la personne qui vous a parlé aura changé de dossier."],
       ]},

      {t:'check', h:"Quatre décisions dans une contestation",
       p:"Quatre questions, vite fait.",
       qs:[
         {q:"Un point de votre réclamation ne tient pas. Vous…", opts:["le défendez quand même","le concédez tout de suite, à voix haute"], ok:1,
          fb:"Le concéder coûte ce point-là et achète l'attention sur les autres."},
         {q:"On vous annonce un refus sans citer de clause. C'est…", opts:["un refus","une opinion, et vous demandez la clause"], ok:1,
          fb:"Un refus sans clause se retire. Exigez le texte, et notez-le."},
         {q:"Le déménageur vous envoie un chèque pendant la révision. Vous…", opts:["l'encaissez, c'est toujours ça","ne l'encaissez pas"], ok:1,
          fb:"Un montant encaissé ferme le dossier d'assurance tout seul."},
         {q:"Votre contestation se termine par…", opts:["« je compte sur vous »","une proposition chiffrée et une contrepartie"], ok:1,
          fb:"Sans chiffre, la contestation reste sur un bureau. Avec, elle se traite."},
       ]},

      {t:'revoir', h:"À retenir",
       p:"Cinq étapes : <b>découper</b>, <b>concéder</b> ce qui est juste, <b>exiger la clause</b> mot pour mot, <b>retourner</b> le texte avec une pièce datée, <b>proposer un chiffre</b> avec une contrepartie. Et deux interdits : ne rien encaisser tant que la révision est ouverte, ne rien accepter qui ne soit pas écrit."},
    ]
  },

  t2refus: {
    eye:'Mini-leçon', tit:"Lire une lettre de décision",
    blocs:[
      {t:'texte', h:"Elle a toujours la même charpente",
       p:"Le numéro de dossier, un rappel des faits, ce qui est accepté avec son montant, ce qui est refusé avec sa clause, la marche à suivre pour contester. Cinq blocs, dans cet ordre, dans toutes les compagnies. Cherchez-les à la première lecture : une lettre à laquelle il en manque un est incomplète, et vous pouvez le dire — une décision qui ne cite aucune clause, en particulier, ne se défend pas.",
       note:"Lisez-la deux fois : une fois pour la charpente, une fois pour les mots. Ce sont deux lectures différentes."},

      {t:'texte', h:"Le montant annoncé n'est pas le montant versé",
       p:"Presque toujours, le chiffre du corps de la lettre est celui du <b>dommage retenu</b> ; la franchise se soustrait plus loin, parfois en une demi-ligne, parfois dans un tableau. Neuf cent quarante devient quatre cent quarante, et l'écart n'est pas caché : il est simplement ailleurs. Faites vous-même la soustraction avant de vous réjouir ou de vous fâcher.",
       note:"« Dommage retenu » est le mot à repérer : il annonce toujours un chiffre avant franchise."},

      {t:'ex', h:"Cinq formules et ce qu'elles annoncent",
       p:"À gauche ce que la lettre écrit, à droite ce que cela veut dire.",
       rows:[
         ["le dommage retenu s'établit à…","un montant avant franchise, à recalculer"],
         ["il a été établi que…","personne n'est nommé : demandez par qui et sur quelle pièce"],
         ["la clause X se lit comme suit","le point d'appui du refus, et donc de votre contestation"],
         ["la responsabilité est régie par…","on vous renvoie à un autre contrat, souvent celui d'un tiers"],
         ["dans les soixante jours suivant la réception","une vraie date : notez-la le jour même"],
       ]},

      {t:'texte', h:"La clause citée est votre point d'appui",
       p:"Elle est reproduite entre guillemets parce que l'assureur y est tenu, et c'est le seul endroit de la lettre où l'on vous donne un texte plutôt qu'un jugement. Relisez-la lentement, mot par mot. Les termes qu'elle emploie sont ceux que le réviseur devra défendre, et un mot qui ne recouvre pas exactement votre situation est une brèche. « Pendant leur transport » ne veut pas dire « pendant le service de déménagement » : ce n'est pas vous qui inventez la distinction, c'est le contrat qui l'écrit.",
       note:"Recopiez la clause dans votre lettre, entre guillemets, avant de la discuter. On ne discute bien que ce qu'on a d'abord cité fidèlement."},

      {t:'piege', h:"Trois lectures trop rapides",
       rows:[
         ["lire le montant et s'arrêter là","chercher la ligne de la franchise",
          "L'écart entre le dommage retenu et la somme versée n'est jamais caché, mais il n'est jamais à côté du premier chiffre non plus."],
         ["lire « refusé » comme définitif","lire jusqu'au paragraphe de la révision",
          "Toute lettre de décision contient une voie de recours, et un délai. Beaucoup de dossiers se ferment simplement parce que personne n'a lu ce paragraphe."],
         ["accepter un refus sans clause","demander la clause par écrit",
          "Un refus qui ne cite aucun texte n'est pas défendable devant un réviseur, et souvent il se retire dès qu'on le demande."],
       ]},

      {t:'check', h:"Quatre lectures d'une décision",
       p:"Quatre questions, vite fait.",
       qs:[
         {q:"« Le dommage retenu s'établit à 940 $ » veut dire que vous recevrez…", opts:["940 $","940 $ moins la franchise"], ok:1,
          fb:"Le montant retenu est toujours avant franchise. Faites la soustraction."},
         {q:"« Il a été établi que… » appelle quelle question ?", opts:["combien ?","par qui, et sur quelle pièce ?"], ok:1,
          fb:"Le passif efface celui qui a établi. C'est souvent la question qui débloque le dossier."},
         {q:"La clause citée entre guillemets sert d'abord à…", opts:["justifier l'assureur","vous donner le texte que vous allez discuter"], ok:1,
          fb:"C'est le seul texte de la lettre, donc le seul point d'appui solide."},
         {q:"Le délai de révision est…", opts:["indicatif","une vraie date, après laquelle le dossier se ferme"], ok:1,
          fb:"Notez-la le jour de la réception, et envoyez une semaine d'avance."},
       ]},

      {t:'revoir', h:"À retenir",
       p:"Cinq blocs : <b>dossier</b>, <b>faits</b>, <b>accepté</b>, <b>refusé avec sa clause</b>, <b>recours</b>. Le montant annoncé est <b>avant franchise</b>. Le passif cache l'auteur : demandez par qui. Et la <b>clause citée</b> est le texte sur lequel toute votre contestation va s'appuyer."},
    ]
  },

  t2irr: {
    eye:'Mini-leçon', tit:"Ce qui aurait pu ne pas arriver",
    blocs:[
      {t:'texte', h:"La règle, en une seule ligne, et la faute en une ligne",
       p:"<b>Si + plus-que-parfait, conditionnel passé.</b> « Si j'<b>avais lu</b> le connaissement, je ne l'<b>aurais</b> pas <b>signé</b>. » La faute la plus fréquente est de mettre un conditionnel après « si » : « si j'aurais lu » ne se dit ni ne s'écrit, et cela s'entend immédiatement. Après « si », jamais de conditionnel — c'est la seule chose à retenir absolument.",
       note:"Moyen mnémotechnique : les deux « r » du conditionnel ne franchissent jamais le « si »."},

      {t:'texte', h:"Comment se forment les deux temps",
       p:"<b>Plus-que-parfait</b> : avoir ou être à l'<b>imparfait</b> + participe passé. j'avais lu · elle était partie · nous avions reçu. <b>Conditionnel passé</b> : avoir ou être au <b>conditionnel présent</b> + participe passé. j'aurais refusé · elle serait restée · nous aurions accepté. Les deux se construisent donc de la même façon, avec le même participe : seul l'auxiliaire change de temps.",
       note:"Si vous savez dire « j'avais lu » et « j'aurais lu », vous savez faire toutes les phrases de ce type."},

      {t:'labo', h:"Les deux moitiés de la phrase",
       p:"Choisissez un verbe et la moitié de phrase à entendre.",
       axes:[
         {id:'v', lbl:'Quel verbe ?', opts:[['l','lire'],['o','offrir'],['n','noter'],['s','savoir']]},
         {id:'m', lbl:'Quelle moitié ?', opts:[['1','la condition (si…)'],['2','la conséquence']]}],
       out:{
         l1:{w:["Si j'avais lu le contrat"], say:"Si j'avais lu le contrat", n:'plus-que-parfait : avais + participe'},
         l2:{w:["je ne l'aurais pas signé."], say:"je ne l'aurais pas signé.", n:'conditionnel passé : aurais + participe'},
         o1:{w:["Si on m'avait offert une déclaration"], say:"Si on m'avait offert une déclaration", n:'avait offert — la condition ne s\'est pas réalisée'},
         o2:{w:["j'en aurais fait une."], say:"j'en aurais fait une.", n:'aurais fait — donc je n\'en ai pas fait'},
         n1:{w:["Si le chauffeur avait noté la fente"], say:"Si le chauffeur avait noté la fente", n:'avait noté — il ne l\'a pas notée'},
         n2:{w:["nous ne discuterions pas aujourd'hui."], say:"nous ne discuterions pas aujourd'hui.", n:'ici le conditionnel présent : la conséquence est dans le présent'},
         s1:{w:["Si j'avais su"], say:"Si j'avais su", n:'savoir est irrégulier : su'},
         s2:{w:["j'aurais posé la question avant."], say:"j'aurais posé la question avant.", n:'aurais posé — je ne l\'ai pas posée'},
       },
       note:"Écoutez les deux moitiés à la suite : c'est la mélodie de la phrase entière qui la fait retenir, pas la règle."},

      {t:'texte', h:"Ce qu'elle dit vraiment, et pourquoi elle est utile ici",
       p:"L'hypothèse irréelle affirme deux choses à la fois : que la condition ne s'est pas réalisée, et qu'elle ne se réalisera plus. « Si on m'avait offert une déclaration de valeur, j'en aurais fait une » veut dire, en clair : <b>on ne me l'a pas offerte</b>. C'est un regret et c'est aussi un reproche, mais un reproche qui ne nomme personne — d'où son extraordinaire utilité dans une négociation. Vous désignez une faute sans accuser quiconque, et l'autre la voit très bien.",
       note:"Une ou deux fois dans une conversation, elle porte. Cinq fois, elle devient de la plainte et se retourne contre vous."},

      {t:'ex', h:"Retourner l'hypothèse contre soi : la concession",
       p:"À gauche l'hypothèse qui accuse, à droite celle qui concède — et la seconde est souvent la plus efficace.",
       rows:[
         ["Si vos hommes avaient rentré les boîtes…","Si j'avais surveillé le balcon, elles seraient restées au sec."],
         ["Si on m'avait expliqué le connaissement…","Si j'avais pris cinq minutes pour le lire, j'aurais compris."],
         ["Si le chauffeur avait noté la fente…","Si j'avais photographié le meuble au départ, ce serait réglé."],
         ["Si vous m'aviez prévenue du délai…","Si j'avais noté la date à la réception, je n'aurais pas attendu."],
       ]},

      {t:'piege', h:"Trois erreurs sur l'irréel du passé",
       rows:[
         ["« si j'aurais lu »","« si j'avais lu »",
          "Jamais de conditionnel après « si ». C'est la faute la plus repérable du français, et elle discrédite tout le reste de la phrase."],
         ["« la photo que j'aurais pris »","« la photo que j'aurais prise »",
          "Avec avoir, le participe s'accorde avec le complément direct placé avant. « que » reprend « la photo », donc prise."],
         ["« elles seraient resté au sec »","« elles seraient restées au sec »",
          "Avec être, le participe s'accorde avec le sujet, toujours."],
       ]},

      {t:'check', h:"Quatre phrases à compléter de tête",
       p:"Quatre questions, vite fait.",
       qs:[
         {q:"« Si j'___ le contrat, je ne l'aurais pas signé. »", opts:["aurais lu","avais lu"], ok:1,
          fb:"Après « si », plus-que-parfait. Jamais de conditionnel."},
         {q:"« Si on me l'avait offerte, j'___ une déclaration. »", opts:["aurais fait","avais fait"], ok:0,
          fb:"La conséquence prend le conditionnel passé : j'aurais fait."},
         {q:"« Si on m'avait offert une déclaration, j'en aurais fait une » veut dire…", opts:["on me l'a offerte","on ne me l'a pas offerte"], ok:1,
          fb:"L'irréel du passé affirme que la condition ne s'est pas réalisée."},
         {q:"« Les pièces qu'elle aurait ___ » (envoyer)", opts:["envoyé","envoyées"], ok:1,
          fb:"Le complément direct « que » est placé avant : accord au féminin pluriel."},
       ]},

      {t:'revoir', h:"À retenir",
       p:"<b>Si + plus-que-parfait, conditionnel passé.</b> Jamais de conditionnel après « si ». Elle dit que la condition <b>ne s'est pas réalisée</b>, donc elle désigne une faute sans nommer personne. Retournez-la contre vous une fois : c'est la façon la plus efficace de concéder."},
    ]
  },

  t2conc: {
    eye:'Mini-leçon', tit:"Concéder, puis avancer",
    blocs:[
      {t:'texte', h:"La structure en deux temps, et rien d'autre",
       p:"Toute l'argumentation de ce module tient dans un mouvement à deux temps. <b>Temps 1</b> : vous reconnaissez ce qui est vrai chez l'autre, franchement, sans réserve. <b>Temps 2</b> : vous posez ce qui est vrai chez vous, et c'est là que va votre argument. Ce n'est pas de la politesse : c'est ce qui empêche votre interlocuteur de dépenser son énergie à vous prouver un point que vous venez de lui accorder.",
       note:"Une concession à moitié faite ne compte pas. « C'est peut-être vrai, mais » n'est pas une concession, c'est une contestation déguisée."},

      {t:'labo', h:"Les deux temps, à écouter",
       p:"Choisissez un connecteur de concession et le retournement qui suit.",
       axes:[
         {id:'c', lbl:'Quelle concession ?', opts:[['a','certes'],['b','bien que'],['c','je vous l\'accorde']]},
         {id:'r', lbl:'Quel retournement ?', opts:[['1','mais'],['2','or'],['3','il n\'en demeure pas moins que']]}],
       out:{
         a1:{w:["Certes la clause existe, mais elle vise le transport."], say:"Certes la clause existe, mais elle vise le transport.", n:'le couple le plus simple, et le plus sûr'},
         a2:{w:["Certes la clause existe. Or le meuble a été fendu dans l'escalier."], say:"Certes la clause existe. Or le meuble a été fendu dans l'escalier.", n:'« or » introduit le fait, pas l\'opinion'},
         a3:{w:["Certes j'ai signé. Il n'en demeure pas moins que personne ne me l'a fait lire."], say:"Certes j'ai signé. Il n'en demeure pas moins que personne ne me l'a fait lire.", n:'la locution la plus soutenue : réservez-la à l\'écrit'},
         b1:{w:["Bien que la clause soit claire, mais elle vise le transport."], say:"Bien que la clause soit claire, elle vise le transport.", n:'attention : avec « bien que », on ne met PAS « mais »'},
         b2:{w:["Bien que la clause soit claire, elle ne recouvre pas le portage."], say:"Bien que la clause soit claire, elle ne recouvre pas le portage.", n:'« bien que » suffit à lui seul, et il veut le subjonctif'},
         b3:{w:["Bien que j'aie signé, il n'en demeure pas moins que rien ne m'a été lu."], say:"Bien que j'aie signé, il n'en demeure pas moins que rien ne m'a été lu.", n:'lourd, mais correct à l\'écrit'},
         c1:{w:["Je vous l'accorde, mais l'inventaire ne notait rien."], say:"Je vous l'accorde, mais l'inventaire ne notait rien.", n:'la forme parlée, très efficace au téléphone'},
         c2:{w:["Je vous l'accorde. Or la photo est datée de onze heures vingt-deux."], say:"Je vous l'accorde. Or la photo est datée de onze heures vingt-deux.", n:'concession parlée, retournement écrit : le mélange fonctionne'},
         c3:{w:["Je vous l'accorde. Il n'en demeure pas moins que la garde était au transporteur."], say:"Je vous l'accorde. Il n'en demeure pas moins que la garde était au transporteur.", n:'le plus formel des trois retournements'},
       },
       note:"Écoutez-les tous les neuf, puis choisissez-en deux : vous n'en emploierez jamais plus dans une même conversation."},

      {t:'texte', h:"« Or », le mot le plus utile et le moins employé",
       p:"« Or » n'oppose pas deux opinions : il introduit <b>le fait</b> qui rend la conclusion inévitable. « La clause vise le transport. <b>Or</b>, le meuble a été fendu dans l'escalier. Donc la clause ne s'applique pas. » C'est la charnière d'un raisonnement en trois temps, et c'est ce qui distingue une argumentation d'une simple protestation. Il n'existe pas d'équivalent parlé exact : au téléphone, on dit « et justement », ou on marque un temps.",
       note:"« Or » ne s'emploie qu'une fois par raisonnement. Deux « or » dans un paragraphe, et le lecteur ne sait plus lequel porte la conclusion."},

      {t:'ex', h:"Les connecteurs, rangés par force",
       p:"À gauche le connecteur, à droite le registre où il vit.",
       rows:[
         ["je vous l'accorde · c'est vrai","parlé, chaleureux, très efficace au téléphone"],
         ["certes · il est vrai que","écrit et parlé soutenu, la valeur sûre"],
         ["bien que · quoique (+ subjonctif)","écrit, et il se suffit à lui-même"],
         ["même si (+ indicatif)","écrit et parlé, plus léger que « bien que »"],
         ["mais · pourtant · cependant","le retournement ordinaire, partout"],
         ["en revanche · par contre","oppose deux choses distinctes, pas deux aspects d'une même"],
         ["or","introduit le fait qui décide — écrit surtout"],
         ["il n'en demeure pas moins que","le plus formel : une fois par lettre, jamais deux"],
       ]},

      {t:'texte', h:"Annoncer ses arguments avant de les donner",
       p:"« Mes deux arguments sont les suivants : d'une part…, d'autre part… » Deux arguments annoncés se retiennent ; deux arguments empilés se perdent. L'annonce coûte une demi-phrase et produit deux effets : votre interlocuteur sait quand vous aurez fini, donc il vous écoute au lieu de chercher une ouverture, et il ne peut pas traiter le premier en oubliant le second. À l'écrit, c'est ce qui fait la différence entre une lettre lue et une lettre parcourue.",
       note:"Trois arguments annoncés commencent à ressembler à un plaidoyer. Deux est le bon nombre."},

      {t:'piege', h:"Quatre erreurs de connecteur",
       rows:[
         ["« bien que la clause est claire »","« bien que la clause soit claire »",
          "« Bien que » et « quoique » veulent le subjonctif ; « même si » veut l'indicatif. Même idée, deux modes."],
         ["« bien que…, mais… »","« bien que…, … »",
          "« Bien que » porte déjà l'opposition. Y ajouter « mais » double le connecteur et alourdit la phrase sans rien apporter."],
         ["« malgré que la clause existe »","« malgré l'existence de cette clause »",
          "« Malgré » et « en dépit de » se font suivre d'un nom. « Malgré que » est fautif dans un écrit soigné."],
         ["« par contre » dans une lettre d'affaires","« en revanche »",
          "Les deux sont corrects, mais « en revanche » est attendu dans un écrit formel québécois. C'est une question d'usage, pas de grammaire."],
       ]},

      {t:'check', h:"Quatre choix de connecteur",
       p:"Quatre questions, vite fait.",
       qs:[
         {q:"« ___ la clause soit claire, elle vise le transport. »", opts:["Bien que","Même si"], ok:0,
          fb:"« soit » est un subjonctif : c'est « bien que » qui le commande."},
         {q:"« La clause vise le transport. ___, le meuble a été fendu dans l'escalier. »", opts:["Cependant","Or"], ok:1,
          fb:"« Or » introduit le fait qui rend la conclusion inévitable."},
         {q:"Une concession efficace commence par…", opts:["« c'est peut-être vrai, mais »","« certes » ou « je vous l'accorde »"], ok:1,
          fb:"Une concession à moitié faite ne compte pas : elle se lit comme une contestation déguisée."},
         {q:"Dans une lettre d'affaires, on préfère…", opts:["par contre","en revanche"], ok:1,
          fb:"Question d'usage : « en revanche » est attendu dans l'écrit formel."},
       ]},

      {t:'revoir', h:"À retenir",
       p:"Deux temps : <b>concéder franchement</b>, puis <b>retourner</b>. <i>Bien que</i> + subjonctif, <i>même si</i> + indicatif, <i>malgré</i> + nom. <b>Or</b> introduit le fait qui décide, une seule fois par raisonnement. Et annoncez vos arguments : <i>d'une part…, d'autre part…</i>"},
    ]
  },

  t2emph: {
    eye:'Mini-leçon', tit:"Mettre en relief ce qui compte",
    blocs:[
      {t:'texte', h:"Une phrase ordinaire met tout sur le même plan",
       p:"« Je conteste le refus complet, pas votre évaluation » se comprend, mais rien n'y ressort. « <b>Ce que je conteste, c'est</b> le refus complet, pas votre évaluation » oblige votre interlocuteur à attendre la fin de la phrase pour savoir de quoi il s'agit — et c'est exactement l'effet recherché. L'emphase ne rend pas la phrase plus vraie ; elle décide de ce qu'on retiendra d'elle.",
       note:"En français, l'ordre des mots est rigide. L'emphase est le seul moyen de faire ce que d'autres langues font avec l'accent tonique."},

      {t:'ex', h:"Les trois tournures, sur la même idée",
       p:"À gauche la phrase ordinaire, à droite les mises en relief possibles.",
       rows:[
         ["Le portage a fendu le meuble.","C'est le portage qui a fendu le meuble."],
         ["Je demande la révision du troisième point.","Ce que je demande, c'est la révision du troisième point."],
         ["La photo a été prise à onze heures vingt-deux.","C'est à onze heures vingt-deux que la photo a été prise."],
         ["Je conteste ce point-là.","Ce point-là, je le conteste."],
         ["Les albums ont le plus souffert.","Ce sont les albums qui ont le plus souffert."],
         ["Personne ne m'a proposé de déclaration.","Ce qui m'étonne, c'est que personne ne m'ait proposé de déclaration."],
       ]},

      {t:'texte', h:"Tournure 1 — c'est … qui / c'est … que",
       p:"On encadre le groupe à mettre en avant. <b>qui</b> quand ce groupe est le sujet du verbe : « c'est le portage <b>qui</b> a fendu le meuble ». <b>que</b> dans tous les autres cas — complément, lieu, moment, manière : « c'est à onze heures vingt-deux <b>que</b> la photo a été prise ». C'est la tournure la plus courante et la plus discrète des trois.",
       note:"Au pluriel, l'écrit soigné demande « ce sont » : ce sont les albums qui… À l'oral, « c'est les albums » se dit et ne choque personne."},

      {t:'texte', h:"Tournure 2 — ce qui / ce que … , c'est",
       p:"On annonce d'abord, on nomme ensuite. « <b>Ce que</b> je demande, <b>c'est</b> la révision du troisième point. » « <b>Ce qui</b> m'étonne, <b>c'est</b> qu'aucune déclaration ne m'ait été proposée. » C'est la plus forte à l'oral, parce qu'elle crée une attente : votre interlocuteur ne peut pas vous couper avant la fin. Choisissez « ce qui » quand le groupe mis en avant est sujet, « ce que » quand il est complément.",
       note:"C'est aussi celle qui permet de dire, en une phrase, ce qu'on conteste ET ce qu'on ne conteste pas. Elle vaut un paragraphe."},

      {t:'texte', h:"Tournure 3 — la reprise par un pronom",
       p:"« Ce point-là, je <b>le</b> conteste. » « Le vaisselier, <b>il</b> était intact à huit heures. » « Cette clause, je <b>l'</b>ai relue trois fois. » On détache le groupe en tête, puis on le reprend par un pronom. Très fréquente à l'oral québécois, très efficace au téléphone, et à éviter dans une lettre d'affaires, où elle sonne relâchée.",
       note:"C'est la seule des trois qui change de registre selon le canal. Employez-la en parlant, pas en écrivant."},

      {t:'piege', h:"Trois abus de l'emphase",
       rows:[
         ["trois emphases dans un paragraphe","une, deux au maximum",
          "Enchaînées, elles donnent un ton théâtral qui affaiblit exactement ce qu'elles devaient renforcer. Réservez-les au point que vous voulez qu'on retienne."],
         ["« c'est les deux boîtes qui » dans une lettre","« ce sont les deux boîtes qui »",
          "Le pluriel est attendu à l'écrit soigné. À l'oral, personne n'y prête attention."],
         ["« c'est le portage que a fendu »","« c'est le portage qui a fendu »",
          "« qui » quand le groupe encadré est sujet du verbe qui suit ; « que » dans tous les autres cas. Le test : remplacez par « il » ou « le »."],
       ]},

      {t:'check', h:"Quatre relations à mettre en relief",
       p:"Quatre questions, vite fait.",
       qs:[
         {q:"« C'est le portage ___ a fendu le meuble. »", opts:["qui","que"], ok:0,
          fb:"Le portage est sujet du verbe « a fendu » : qui."},
         {q:"« C'est à onze heures ___ la photo a été prise. »", opts:["qui","que"], ok:1,
          fb:"Le groupe encadré n'est pas sujet : que."},
         {q:"Dans une lettre, « le vaisselier, il était intact » est…", opts:["parfait","trop relâché : préférez une autre tournure"], ok:1,
          fb:"La reprise par un pronom appartient à l'oral. À l'écrit, elle sonne relâchée."},
         {q:"Combien d'emphases dans un même paragraphe ?", opts:["autant de fois qu'on veut","une, deux au maximum"], ok:1,
          fb:"Enchaînées, elles s'annulent : le lecteur ne sait plus ce qui compte."},
       ]},

      {t:'revoir', h:"À retenir",
       p:"Trois tournures : <b>c'est … qui / que</b> (discrète), <b>ce que … , c'est</b> (la plus forte à l'oral), <b>la reprise par un pronom</b> (parlée seulement). Une ou deux par paragraphe, jamais plus. Et la phrase à emporter : « <b>ce que je conteste, c'est</b> le refus complet, <b>pas</b> votre évaluation »."},
    ]
  },

  t2lettre: {
    eye:'Mini-leçon', tit:"Écrire une demande de révision",
    blocs:[
      {t:'texte', h:"Sept fonctions, dans cet ordre",
       p:"Une demande de révision n'est pas une lettre libre : c'est une suite de sept fonctions, et l'ordre compte autant que le contenu. <b>1.</b> L'objet, avec le numéro de dossier. <b>2.</b> Ce que vous acceptez. <b>3.</b> Ce que vous contestez, en une phrase. <b>4.</b> La concession, puis le retournement. <b>5.</b> Les pièces, numérotées et datées. <b>6.</b> La proposition chiffrée avec sa contrepartie. <b>7.</b> La demande de réponse écrite et la formule de politesse.",
       note:"Vous venez de lire ce modèle dans l'exercice 6. Écrivez le vôtre en gardant les sept fonctions dans le même ordre."},

      {t:'texte', h:"Pourquoi ce que vous acceptez vient en premier",
       p:"C'est contre-intuitif et c'est pourtant décisif. La personne qui ouvre votre lettre traite peut-être quarante dossiers cette semaine, et la première chose qu'elle cherche à savoir est de quel genre de correspondance il s'agit. Un premier paragraphe qui accepte deux points sur trois lui apprend en dix secondes qu'elle n'a pas affaire à un refus de principe — et elle lit la suite d'une tout autre façon.",
       note:"Le même mécanisme qu'au téléphone, et il fonctionne encore mieux à l'écrit, parce que rien ne vient adoucir un texte hostile."},

      {t:'ex', h:"Les sept fonctions, et la formule qui les ouvre",
       p:"À gauche la fonction, à droite comment on l'écrit.",
       rows:[
         ["1. Identifier le dossier","Objet : demande de révision — dossier 8-4-1-7-2-6"],
         ["2. Accepter","Je vous confirme d'abord mon accord sur les deux premiers éléments…"],
         ["3. Contester","Je conteste en revanche le troisième élément, soit…"],
         ["4. Concéder et retourner","Certes, la clause 7.3 existe… Or elle exclut les dommages « pendant leur transport »…"],
         ["5. Appuyer","…l'inventaire signé à huit heures (pièce 1)… la photographie horodatée (pièce 2)…"],
         ["6. Proposer","Je propose en conséquence un règlement de huit cent cinquante dollars, contre…"],
         ["7. Clore","Je vous saurais gré de me communiquer votre décision par écrit…"],
       ]},

      {t:'texte', h:"Un seul point contesté par lettre",
       p:"C'est la contrainte la plus utile et la plus difficile à tenir. Une lettre qui conteste trois points en obtient zéro : le lecteur choisit le plus faible, y répond, et considère l'ensemble comme traité. Une lettre qui en conteste un seul, appuyé sur deux pièces datées, oblige à répondre sur ce point-là. Si vous avez vraiment deux désaccords sérieux, écrivez deux lettres, à deux semaines d'intervalle.",
       note:"Corollaire : choisissez celui qui a le plus de chances, pas celui qui vous fâche le plus. Ce ne sont pas toujours les mêmes."},

      {t:'texte', h:"Le chiffre, et pourquoi il doit venir de l'extérieur",
       p:"Un montant que vous avancez sans le justifier se refuse sans discussion : rien n'oblige personne à en discuter. Un montant appuyé sur une évaluation écrite et trois annonces comparables devient une pièce du dossier, que le réviseur peut citer à son tour dans sa propre note. Vous ne lui demandez pas une faveur : vous lui fournissez une justification toute faite pour dire oui.",
       note:"Et offrez une contrepartie. « Contre ma renonciation à toute autre réclamation dans ce dossier » ne vous coûte rien si vous n'avez plus rien à réclamer, et cela transforme une demande en échange."},

      {t:'piege', h:"Quatre défauts qui font classer une lettre",
       rows:[
         ["oublier le numéro de dossier en objet","le mettre en objet, avant tout le reste",
          "Sans lui, la lettre arrive dans une pile générale et se traite trois semaines plus tard, si elle se traite."],
         ["contester trois points à la fois","un seul, appuyé sur deux pièces datées",
          "Le lecteur répondra au plus faible et considérera l'ensemble comme traité. Deux désaccords sérieux font deux lettres."],
         ["employer un ton indigné","poser les faits et proposer un chiffre",
          "L'indignation est légitime et elle ne se transmet pas par écrit : elle se lit comme du bruit, et elle donne une raison de refuser."],
         ["terminer sans rien demander","demander une décision écrite avec sa clause",
          "Une lettre qui ne demande rien de précis ne reçoit rien de précis. Nommez ce que vous attendez, et sous quelle forme."],
       ]},

      {t:'check', h:"Quatre décisions de rédaction",
       p:"Quatre questions, vite fait.",
       qs:[
         {q:"Le premier paragraphe du corps de la lettre…", opts:["annonce le désaccord","dit ce que vous acceptez"], ok:1,
          fb:"Accepter d'abord montre que vous n'êtes pas dans le refus de principe, et change la lecture de la suite."},
         {q:"Vous avez trois désaccords. Vous écrivez…", opts:["une lettre pour les trois","une lettre pour le plus solide"], ok:1,
          fb:"Une lettre qui conteste tout obtient zéro : le lecteur répond au point le plus faible."},
         {q:"Votre montant doit être…", opts:["rond et raisonnable","justifié par une pièce extérieure"], ok:1,
          fb:"Un chiffre sans justification se refuse sans discussion."},
         {q:"La lettre se termine par…", opts:["« je compte sur votre compréhension »","une demande de décision écrite avec sa clause"], ok:1,
          fb:"Nommez ce que vous attendez et sous quelle forme, sinon vous ne l'obtiendrez pas."},
       ]},

      {t:'revoir', h:"À retenir",
       p:"Sept fonctions dans l'ordre : <b>objet et numéro</b>, <b>ce que j'accepte</b>, <b>ce que je conteste</b> (un seul point), <b>concession et retournement</b>, <b>pièces numérotées et datées</b>, <b>proposition chiffrée avec contrepartie</b>, <b>demande de réponse écrite</b>. Le ton reste posé du début à la fin — l'indignation se lit comme du bruit."},
    ]
  },

};
