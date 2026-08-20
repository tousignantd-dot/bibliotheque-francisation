const PLUS = {
  prPhon: {
    eye:'Mini-leçon', tit:"Quand la voix insiste",
    blocs:[
      {t:'texte', h:"La même phrase, deux intentions",
       p:"En français, on ne change pas les mots pour montrer qu'on est surpris ou qu'on trouve ça énorme : <b>on change la voix</b>. La syllabe importante monte plus haut, dure plus longtemps, et se prononce plus fort. C'est ce qu'on appelle l'<b>accent d'insistance</b>.",
       note:"Comparez « Elle portait des sandales. » et « Des sandales ! » — mêmes mots, deux messages complètement différents."},

      {t:'ana', h:"La phrase neutre : on informe",
       p:"La voix descend tranquillement jusqu'au point. Aucune syllabe ne ressort.",
       mots:[['Ce qu\'on fait','on donne une information'],['La voix','elle descend',true],['Comme dans','Elle portait des {san}dales.']],
       say:"Elle portait des sandales à l'aéroport.",
       note:"C'est la façon normale de raconter. Vous l'entendez toute la journée, à la radio comme au travail."},

      {t:'ana', h:"La phrase exclamative : on insiste",
       p:"Une syllabe est nettement plus haute et plus longue que les autres, et la phrase est souvent très courte.",
       mots:[['Ce qu\'on fait','on réagit, on s\'étonne'],['La voix','elle monte fort',true],['Comme dans','Des {SAN}dales !']],
       say:"Des sandales ! En janvier !",
       note:"Souvent, la personne ne répète que le mot qui la surprend. C'est plus fort qu'une phrase complète."},

      {t:'texte', h:"Ce que ça change pour vous",
       p:"Vous n'êtes pas obligé de produire cet accent parfaitement. Mais vous devez le <b>reconnaître</b> : c'est lui qui vous dit si votre interlocuteur est surpris, choqué, admiratif — ou s'il constate simplement un fait.",
       note:"Si quelqu'un vous répond « Cinq heures et quart ! », il ne vous demande pas l'heure : il trouve que c'est très tôt."},

      {t:'labo', h:"Écoutez la différence",
       p:"Choisissez une paire et écoutez les deux versions l'une après l'autre.",
       axes:[{id:'p', lbl:'Quelle paire ?', opts:[['a','les sandales'],['b','cinq heures et quart'],['c','six ans'],['d','onze voyages']]}],
       out:{
         a:{w:['Elle portait des {san}dales.'], say:"Elle portait des sandales à l'aéroport.", n:'neutre — on informe'},
         b:{w:['Je me lève à cinq heures et {quart}.'], say:"Je me lève à cinq heures et quart.", n:'neutre — on informe'},
         c:{w:['Elle joue depuis {six} ans.'], say:"Elle joue dans cette équipe depuis six ans.", n:'neutre — on informe'},
         d:{w:['Ils ont fait onze {vo}yages.'], say:"Ils ont fait onze voyages en voiture.", n:'neutre — on informe'},
       },
       note:"Réécoutez ensuite l'exercice 2 : les phrases courtes sont celles où la voix insiste."},

      {t:'ex', h:"Les exclamations du module",
       p:"Écoutez chacune et répétez en exagérant la montée de la voix.",
       rows:[
         ["Des sandales ! En janvier !","surprise — la voix monte sur « san- »"],
         ["Cinq heures et quart !","étonnement — la voix monte sur « cinq »"],
         ["Six ans dans la même équipe !","admiration — la voix monte sur « six »"],
         ["Onze voyages !","incrédulité — tout le groupe monte"],
         ["Tu ferais ça ?","surprise reconnaissante — la voix monte à la fin"],
         ["Félicitations !","joie — la voix monte sur « -tions »"],
       ]},

      {t:'piege', h:"Deux malentendus fréquents",
       rows:[
         ["croire qu'une exclamation est une question","« Des sandales ! » n'attend pas de réponse",
          "Une question demande une information. Une exclamation <b>réagit</b> à ce que vous venez de dire. Souvent, il suffit de confirmer : « Oui, je ne savais pas. »"],
         ["parler toujours sur le même ton","une phrase française n'est jamais plate",
          "Si toutes vos phrases ont la même voix, vos interlocuteurs vous trouveront difficile à suivre. Laissez monter la voix sur le mot qui compte le plus pour vous."],
       ]},

      {t:'check', h:"Est-ce que c'est clair maintenant ?",
       p:"Trois questions rapides. Elles ne comptent pas dans votre score.",
       qs:[
         {q:"Pour insister en français, on change surtout…", opts:["les mots de la phrase","la hauteur et la durée de la voix"], ok:1,
          fb:"Les mots restent les mêmes. C'est la <b>voix</b> qui porte l'insistance."},
         {q:"« Cinq heures et quart ! » veut dire…", opts:["je trouve ça très tôt","quelle heure est-il ?"], ok:0,
          fb:"C'est une réaction, pas une question. La personne s'étonne."},
         {q:"Les phrases où on insiste sont souvent…", opts:["longues et complètes","très courtes"], ok:1,
          fb:"On répète souvent le seul mot qui surprend : « Des sandales ! »"},
       ]},
    ]
  },

  t1rel: {
    eye:'Mini-leçon', tit:"qui, que, où : coller deux phrases ensemble",
    blocs:[
      {t:'texte', h:"Le problème qu'ils résolvent",
       p:"Quand deux phrases parlent du <b>même mot</b>, on ne veut pas le répéter. Les pronoms relatifs <b>qui</b>, <b>que</b> et <b>où</b> servent à coller les deux phrases en une seule, en gardant le mot une seule fois.",
       note:"« Je prends un autobus. Cet autobus s'arrête loin. » devient « Je prends un autobus <b>qui</b> s'arrête loin. »"},

      {t:'ana', h:"qui — il n'y a pas d'autre sujet après",
       p:"Après <b>qui</b>, le verbe arrive tout de suite. <b>qui</b> est lui-même le sujet du verbe qui suit.",
       mots:[['Ce qui suit','un verbe, directement'],['Le pronom est','le sujet',true],['Comme dans','une collègue {qui} m\'a parlé']],
       say:"C'est une collègue qui m'a parlé du centre.",
       note:"Autres exemples : le tournoi <b>qui</b> commence en avril · ma voisine <b>qui</b> m'a amenée · les gens <b>qui</b> jouent le jeudi."},

      {t:'ana', h:"que — il y a un autre sujet après",
       p:"Après <b>que</b>, on trouve un sujet (je, tu, elle, mon frère…), puis le verbe. La chose dont on parle est le <b>complément</b> de ce verbe.",
       mots:[['Ce qui suit','un sujet, puis un verbe'],['Le pronom est','le complément direct',true],['Comme dans','le trajet {que} je fais']],
       say:"C'est le trajet que je fais chaque semaine.",
       note:"Autres exemples : l'autobus <b>que</b> je prends · les gens <b>que</b> je vois · le manteau <b>que</b> mon cousin avait apporté."},

      {t:'ana', h:"où — un lieu, ou un moment",
       p:"<b>où</b> reprend un endroit. Mais il reprend aussi un <b>moment</b> : le jour où, l'année où, le soir où.",
       mots:[['Ce qui précède','un lieu ou un moment'],['Le pronom est','un complément de lieu ou de temps',true],['Comme dans','le gymnase {où} on joue']],
       say:"Le gymnase où on joue est au sous-sol.",
       note:"C'est la partie que les élèves oublient : « l'année <b>où</b> je suis arrivée » est aussi correct que « le parc <b>où</b> je vais »."},

      {t:'texte', h:"Le test en trois secondes",
       p:"Regardez uniquement ce qui vient <b>juste après le trou</b>. Un <b>verbe</b> ? C'est <b>qui</b>. Un <b>sujet</b> (je, tu, il, elle, on, nous, mon frère) ? C'est <b>que</b>. Et si le mot d'avant est un lieu ou un moment, pensez d'abord à <b>où</b>.",
       note:"Ce test ne se trompe presque jamais. Faites-le à voix basse avant d'écrire."},

      {t:'labo', h:"Essayez le test",
       p:"Choisissez une phrase et regardez ce qui vient après le trou.",
       axes:[{id:'p', lbl:'Quelle phrase ?', opts:[
         ['a',"L'autobus ___ je prends"],
         ['b',"une collègue ___ m'a parlé"],
         ['c',"le gymnase ___ on joue"],
         ['d',"les gens ___ je vois"],
         ['e',"l'année ___ je suis arrivée"]]}],
       out:{
         a:{w:["L'autobus {que} je prends"], say:"L'autobus que je prends s'arrête loin.", n:"après le trou : « je » → un sujet → que"},
         b:{w:["une collègue {qui} m'a parlé"], say:"C'est une collègue qui m'a parlé du centre.", n:"après le trou : « m'a parlé » → un verbe → qui"},
         c:{w:["le gymnase {où} on joue"], say:"Le gymnase où on joue est au sous-sol.", n:"avant le trou : un lieu → où"},
         d:{w:["les gens {que} je vois"], say:"Les gens que je vois le jeudi sont ma famille.", n:"après le trou : « je » → un sujet → que"},
         e:{w:["l'année {où} je suis arrivée"], say:"L'année où je suis arrivée, il faisait moins vingt.", n:"avant le trou : un moment → où"},
       },
       note:"Remarquez que <b>que</b> et <b>où</b> sont tous les deux suivis d'un sujet. C'est le mot <u>d'avant</u> qui les départage."},

      {t:'ex', h:"Les phrases du module",
       p:"Écoutez chacune et repérez le pronom relatif.",
       rows:[
         ["C'est une collègue qui m'a parlé du centre.","qui — sujet du verbe « a parlé »"],
         ["C'est le trajet que je fais chaque semaine.","que — « je » suit, donc complément"],
         ["Le gymnase où on joue est au sous-sol.","où — un lieu"],
         ["Les gens que je vois le jeudi sont ma famille.","que — « je » suit"],
         ["Le tournoi qui commence en avril dure deux jours.","qui — sujet du verbe « commence »"],
         ["L'année où je suis arrivée, il faisait froid.","où — un moment, pas un lieu"],
       ]},

      {t:'piege', h:"Trois pièges à connaître",
       rows:[
         ["choisir « qui » parce que la personne est humaine","« les gens que je vois » et non « les gens qui je vois »",
          "<b>qui</b> et <b>que</b> ne dépendent <u>pas</u> de la personne ou de la chose. Ils dépendent uniquement de ce qui suit : un verbe, ou un sujet."],
         ["oublier que « où » sert aussi pour le temps","« le jour où » est correct",
          "En anglais on dirait <em>when</em>. En français, c'est <b>où</b> : le jour <b>où</b>, l'année <b>où</b>, le moment <b>où</b>."],
         ["écrire « qu'il » au lieu de « qui »","« la personne qui est arrivée »",
          "<b>que</b> devient <b>qu'</b> devant une voyelle, mais <b>qui</b> ne se raccourcit <u>jamais</u> : on écrit toujours « qui il », « qui elle », « qui est »."],
       ]},

      {t:'check', h:"Est-ce que c'est clair maintenant ?",
       p:"Quatre questions rapides.",
       qs:[
         {q:"« Le tournoi ___ commence en avril » demande…", opts:["qui","que"], ok:0,
          fb:"« commence » est un verbe : c'est <b>qui</b>."},
         {q:"« Le manteau ___ mon cousin avait apporté » demande…", opts:["qui","que"], ok:1,
          fb:"« mon cousin » est un sujet : c'est <b>que</b>."},
         {q:"« L'année ___ je suis arrivée » demande…", opts:["que","où"], ok:1,
          fb:"« l'année » est un moment : c'est <b>où</b>, même si ce n'est pas un lieu."},
         {q:"Le choix entre qui et que dépend…", opts:["de ce qui suit le pronom","du fait que ce soit une personne ou une chose"], ok:0,
          fb:"Un verbe après › <b>qui</b>. Un sujet après › <b>que</b>. La personne ou la chose n'y change rien."},
       ]},
    ]
  },

  t2temps: {
    eye:'Mini-leçon', tit:"Raconter : le décor et les évènements",
    blocs:[
      {t:'texte', h:"Deux temps qui travaillent ensemble",
       p:"Pour raconter une histoire au passé, le français a besoin des <b>deux</b> temps en même temps. L'<b>imparfait</b> peint le décor : comment c'était, ce qui durait, ce qui se répétait. Le <b>passé composé</b> raconte les évènements : ce qui est arrivé, une fois, à un moment précis.",
       note:"C'est comme un film : l'imparfait, c'est le paysage derrière. Le passé composé, c'est ce que font les personnages."},

      {t:'ana', h:"L'imparfait — le décor",
       p:"Rien n'avance. On décrit une situation, une habitude, un sentiment qui durait.",
       mots:[['Ce que ça dit','comment c\'était'],['Ça dure','oui, longtemps ou souvent',true],['Comme dans','je {portais} une veste']],
       say:"À l'aéroport, je portais une veste et des sandales.",
       note:"Autres exemples : il <b>faisait</b> trente degrés · je <b>regardais</b> la neige · mon cousin m'<b>attendait</b> · on n'<b>avait</b> pas de camion."},

      {t:'ana', h:"Le passé composé — l'évènement",
       p:"L'histoire avance. Chaque phrase est un pas de plus.",
       mots:[['Ce que ça dit','ce qui est arrivé'],['Ça dure','non, c\'est un moment',true],['Comme dans','je {suis arrivée} le douze janvier']],
       say:"Je suis arrivée le douze janvier.",
       note:"Autres exemples : j'<b>ai eu</b> mal aux oreilles · une voisine m'<b>a emmenée</b> glisser · j'<b>ai compris</b> ce jour-là · on <b>a fait</b> onze voyages."},

      {t:'texte', h:"Le test des « combien de fois »",
       p:"Posez-vous la question : <b>est-ce que je peux compter ?</b> Si vous pouvez dire « une fois, le douze janvier » → <b>passé composé</b>. Si c'était tous les jours, pendant des mois, sans qu'on puisse compter → <b>imparfait</b>.",
       note:"« Les trois premiers mois, je ne <b>sortais</b> pas » : impossible de compter, c'est une situation qui a duré. Imparfait."},

      {t:'ana', h:"L'accord avec être",
       p:"Au passé composé, quatorze verbes de mouvement et tous les verbes pronominaux se construisent avec <b>être</b>. Dans ce cas, le participe s'accorde avec le sujet, comme un adjectif.",
       mots:[['Avec être','le participe s\'accorde'],['Une femme dit','je suis arriv{ée}',true],['Plusieurs disent','on est parti{s}']],
       say:"Je suis arrivée le douze janvier.",
       note:"Avec <b>avoir</b>, rien ne bouge : « j'ai eu », « on a fait », « elle a choisi » — jamais de -e ni de -s."},

      {t:'labo', h:"Le décor ou l'évènement ?",
       p:"Choisissez une phrase de l'histoire de Mariama.",
       axes:[{id:'p', lbl:'Quelle phrase ?', opts:[
         ['a','arriver le douze janvier'],
         ['b','porter une veste et des sandales'],
         ['c','avoir mal aux oreilles'],
         ['d','regarder la neige pendant trois mois'],
         ['e','comprendre ce jour-là']]}],
       out:{
         a:{w:['Je {suis arrivée} le douze janvier.'], say:"Je suis arrivée le douze janvier.", n:'évènement — une date précise → passé composé'},
         b:{w:['Je {portais} une veste et des sandales.'], say:"Je portais une veste et des sandales.", n:'décor — c\'est la situation → imparfait'},
         c:{w:["J'{ai eu} mal aux oreilles."], say:"J'ai eu mal aux oreilles.", n:'évènement — au moment où les portes s\'ouvrent → passé composé'},
         d:{w:['Je {regardais} la neige par la fenêtre.'], say:"Je regardais la neige par la fenêtre.", n:'décor — tous les jours pendant trois mois → imparfait'},
         e:{w:["J'{ai compris} ce jour-là."], say:"J'ai compris ce jour-là qu'on pouvait aimer l'hiver.", n:'évènement — un jour précis → passé composé'},
       },
       note:"Remarquez que « ce jour-là » et « le douze janvier » annoncent le passé composé, tandis que « pendant trois mois » annonce l'imparfait."},

      {t:'ex', h:"L'histoire complète, dans l'ordre",
       p:"Écoutez le récit phrase par phrase. Repérez l'alternance.",
       rows:[
         ["Je suis arrivée le douze janvier.","évènement"],
         ["À l'aéroport, je portais une veste et des sandales.","décor"],
         ["Chez moi, il faisait trente degrés le matin même.","décor"],
         ["J'ai eu mal aux oreilles.","évènement"],
         ["Mon cousin m'attendait avec un manteau.","décor"],
         ["Les trois premiers mois, je ne sortais pas.","décor"],
         ["Une voisine m'a emmenée glisser.","évènement"],
         ["J'ai compris ce jour-là qu'on pouvait aimer l'hiver.","évènement"],
       ]},

      {t:'piege', h:"Trois pièges à connaître",
       rows:[
         ["tout raconter au passé composé","« il faisait froid » et non « il a fait froid »",
          "Une histoire uniquement au passé composé se comprend, mais elle sonne comme une liste. Le décor a besoin de l'imparfait pour respirer."],
         ["oublier l'accord avec être","une femme écrit « je suis arriv<b>ée</b> »",
          "Avec <b>être</b>, le participe s'accorde avec le sujet : arrivée, partie, restées. C'est la faute la plus visible à l'écrit."],
         ["mettre un -s au participe avec avoir","« j'ai eu », jamais « j'ai eus »",
          "Avec <b>avoir</b>, le participe ne bouge pas, quel que soit le sujet : nous avons <em>fait</em>, elles ont <em>compris</em>."],
       ]},

      {t:'check', h:"Est-ce que c'est clair maintenant ?",
       p:"Quatre questions rapides.",
       qs:[
         {q:"« Les trois premiers mois, je ne ___ pas » demande…", opts:["sortais","suis sortie"], ok:0,
          fb:"Trois mois qu'on ne peut pas compter : c'est du décor, donc l'<b>imparfait</b>."},
         {q:"« Un jour, une voisine m'___ glisser » demande…", opts:["emmenait","a emmenée"], ok:1,
          fb:"« Un jour » annonce un évènement précis : <b>passé composé</b>."},
         {q:"Une femme écrit correctement…", opts:["je suis arrivé","je suis arrivée"], ok:1,
          fb:"Avec <b>être</b>, le participe s'accorde avec le sujet."},
         {q:"Avec l'auxiliaire avoir, le participe…", opts:["s'accorde avec le sujet","ne change pas"], ok:1,
          fb:"« elle a compris », « nous avons fait » — rien ne bouge."},
       ]},
    ]
  },

  t2liaison: {
    eye:'Mini-leçon', tit:"Le [t] qu'on entend et qu'on n'écrit pas",
    blocs:[
      {t:'texte', h:"Un son qui n'est pas dans le mot",
       p:"Quand vous entendez « je suis-<b>t</b>-arrivée » ou « tu es-<b>t</b>-allé », vous n'avez pas mal entendu. Beaucoup de gens, au Québec comme ailleurs, ajoutent un <b>[t]</b> entre le verbe <em>être</em> et le participe passé. Ce [t] ne s'écrit pas.",
       note:"On l'appelle une <b>liaison analogique</b> : la voix imite les autres liaisons du français (« il est-t-arrivé », où le t existe vraiment)."},

      {t:'ana', h:"Où vous l'entendez",
       p:"Surtout avec <b>je suis</b> et <b>tu es</b>, suivis d'un participe qui commence par une voyelle.",
       mots:[['Ce qu\'on écrit','je suis arrivée'],['Ce qu\'on entend','je suis {t}arrivée',true],['Aussi','tu es {t}allé']],
       say:"Je suis arrivée le douze janvier.",
       note:"Le [t] apparaît parce que le mot suivant commence par une voyelle : <em>arrivée</em>, <em>allé</em>, <em>entrée</em>, <em>parti</em>… non, pas <em>parti</em> : celui-là commence par une consonne."},

      {t:'ana', h:"Où vous ne l'entendez pas",
       p:"Avec l'auxiliaire <b>avoir</b>, il n'y a pas de liaison de ce type.",
       mots:[['Ce qu\'on écrit','j\'ai eu mal'],['Ce qu\'on entend','j\'ai eu mal',true],['Pas de','[t] ajouté']],
       say:"J'ai eu mal aux oreilles.",
       note:"C'est un bon repère à l'oreille : entendre ce [t] vous dit que l'auxiliaire est <b>être</b>, donc que le participe s'accorde."},

      {t:'texte', h:"Faut-il le dire vous-même ?",
       p:"<b>Non.</b> Ce [t] n'est pas obligatoire et il n'appartient pas au français soigné. Vous n'avez pas à le produire. Mais vous devez le <b>reconnaître</b>, sinon vous chercherez un mot qui n'existe pas.",
       note:"Le programme du cours demande de le <em>reconnaître</em>, pas de le produire. C'est exactement le bon objectif."},

      {t:'labo', h:"Avec ou sans [t] ?",
       p:"Choisissez une phrase et écoutez le début.",
       axes:[{id:'p', lbl:'Quelle phrase ?', opts:[
         ['a','je suis arrivée'],
         ['b',"j'ai eu mal"],
         ['c','tu es allée au tournoi'],
         ['d','on a fait onze voyages'],
         ['e','je suis entrée dans le gymnase']]}],
       out:{
         a:{w:['je suis {t}arrivée'], say:"Je suis arrivée le douze janvier.", n:'être + voyelle → le [t] apparaît'},
         b:{w:["j'ai eu mal"], say:"J'ai eu mal aux oreilles.", n:'avoir → pas de [t]'},
         c:{w:['tu es {t}allée'], say:"Tu es allée au tournoi ?", n:'être + voyelle → le [t] apparaît'},
         d:{w:['on a fait onze voyages'], say:"On a fait onze voyages.", n:'avoir → pas de [t]'},
         e:{w:['je suis {t}entrée'], say:"Je suis entrée dans le gymnase.", n:'être + voyelle → le [t] apparaît'},
       },
       note:"Écoutez « je suis arrivée » puis « j'ai eu mal » l'un après l'autre : la différence saute à l'oreille."},

      {t:'ex', h:"Les phrases à écouter",
       p:"Écoutez et notez mentalement si le [t] est là.",
       rows:[
         ["Je suis arrivée le douze janvier.","[t] — auxiliaire être"],
         ["J'ai eu mal aux oreilles.","pas de [t] — auxiliaire avoir"],
         ["Tu es allée au tournoi ?","[t] — auxiliaire être"],
         ["J'ai compris ce jour-là.","pas de [t] — auxiliaire avoir"],
         ["Je suis entrée dans le gymnase.","[t] — auxiliaire être"],
         ["Elle a choisi son nom hier soir.","pas de [t] — auxiliaire avoir"],
       ]},

      {t:'piege', h:"Deux malentendus fréquents",
       rows:[
         ["écrire le [t] qu'on entend","on écrit « je suis arrivée », jamais « je suis t'arrivée »",
          "Ce son n'existe qu'à l'oral. À l'écrit, il n'y a rien entre l'auxiliaire et le participe."],
         ["croire qu'on a mal entendu le verbe","« je suis-t-allée » est bien « je suis allée »",
          "Si un mot vous semble commencer par un [t] inconnu, essayez de l'enlever : le mot réapparaît."],
       ]},

      {t:'check', h:"Est-ce que c'est clair maintenant ?",
       p:"Trois questions rapides.",
       qs:[
         {q:"Ce [t] entre l'auxiliaire et le participe…", opts:["s'écrit","ne s'écrit jamais"], ok:1,
          fb:"Il n'existe qu'à l'oral. Rien ne s'écrit."},
         {q:"On l'entend surtout avec…", opts:["l'auxiliaire être","l'auxiliaire avoir"], ok:0,
          fb:"« je suis-t-arrivée », « tu es-t-allée » — avec <b>être</b>."},
         {q:"Devez-vous le prononcer vous-même ?", opts:["oui, c'est obligatoire","non, il suffit de le reconnaître"], ok:1,
          fb:"Le programme demande de le <b>reconnaître</b> pour comprendre, pas de le produire."},
       ]},
    ]
  },

  t2y: {
    eye:'Mini-leçon', tit:"y et là : ne pas répéter le lieu",
    blocs:[
      {t:'texte', h:"Pourquoi on remplace",
       p:"Répéter le lieu à chaque phrase alourdit tout : « Je vais au centre communautaire. Je vais au centre communautaire chaque jeudi. » Le français a deux petits mots pour éviter ça : <b>y</b> et <b>là</b>.",
       note:"Ce n'est pas du luxe. Un francophone qui répète le lieu trois fois se fait interrompre — on comprend qu'il cherche ses mots."},

      {t:'ana', h:"y — devant le verbe",
       p:"<b>y</b> remplace un lieu introduit par <b>à, au, aux, dans, chez, sur</b>. Il se place <b>avant</b> le verbe, collé à lui.",
       mots:[['Ce qu\'il remplace','à / au / dans / chez + lieu'],['Sa place','avant le verbe',true],['Comme dans','j\'{y} vais le jeudi']],
       say:"J'y vais le jeudi.",
       note:"Au passé composé, <b>y</b> passe devant l'auxiliaire : « j'<b>y</b> suis allée deux fois »."},

      {t:'ana', h:"là — après le verbe",
       p:"<b>là</b> montre un endroit dont on vient de parler, et se place plutôt <b>après</b> le verbe. Il est plus concret, plus proche du geste de montrer du doigt.",
       mots:[['Ce qu\'il remplace','un lieu déjà nommé'],['Sa place','après le verbe',true],['Comme dans','on mangeait {là} tous les soirs']],
       say:"On mangeait là tous les soirs.",
       note:"« Je suis restée <b>là</b> trois heures » · « Le balcon ? On mangeait <b>là</b>. » — souvent en réponse à une question."},

      {t:'texte', h:"Comment choisir",
       p:"Avec un verbe de <b>déplacement</b> (aller, retourner, se rendre), prenez <b>y</b>. Pour dire qu'on <b>reste</b> ou qu'on <b>fait quelque chose</b> à un endroit déjà nommé, <b>là</b> passe souvent mieux.",
       note:"Les deux sont corrects dans beaucoup de phrases. Ne bloquez pas là-dessus : l'important est de ne pas répéter le lieu."},

      {t:'labo', h:"Remplacez le lieu",
       p:"Choisissez une phrase et voyez ce qu'elle devient.",
       axes:[{id:'p', lbl:'Quelle phrase ?', opts:[
         ['a','Je vais au centre communautaire.'],
         ['b','Elle joue dans cette équipe.'],
         ['c','On mangeait sur le balcon.'],
         ['d','Je suis allée à Québec.'],
         ['e','Elle est restée dans le vestiaire.']]}],
       out:{
         a:{w:["J'{y} vais le jeudi."], say:"J'y vais le jeudi.", n:'au + lieu, verbe de déplacement → y'},
         b:{w:['Elle {y} joue depuis six ans.'], say:"Elle y joue depuis six ans.", n:'dans + lieu → y, devant le verbe'},
         c:{w:['On mangeait {là} tous les soirs.'], say:"On mangeait là tous les soirs.", n:'lieu déjà nommé, on y fait quelque chose → là'},
         d:{w:["J'{y} suis allée le mois passé."], say:"J'y suis allée le mois passé.", n:'au passé composé, y passe devant l\'auxiliaire'},
         e:{w:['Elle est restée {là} trois heures.'], say:"Elle est restée là trois heures.", n:'rester + lieu déjà nommé → là'},
       },
       note:"Comparez a et c : le même endroit, mais « aller » appelle <b>y</b> et « manger » appelle <b>là</b>."},

      {t:'ex', h:"Les phrases du module",
       p:"Écoutez chacune et repérez le petit mot.",
       rows:[
         ["J'y vais le jeudi.","y — devant le verbe"],
         ["Elle y joue depuis six ans.","y — devant le verbe"],
         ["J'y suis allée le mois passé.","y — devant l'auxiliaire"],
         ["On mangeait là tous les soirs.","là — après le verbe"],
         ["Elle est restée là trois heures.","là — après le verbe"],
         ["Ils y habitent depuis mars.","y — devant le verbe"],
       ]},

      {t:'piege', h:"Trois pièges à connaître",
       rows:[
         ["répéter le lieu après y","« j'y vais » et non « j'y vais au centre »",
          "Si vous dites <b>y</b>, le lieu est déjà dedans. Le redire est une faute et ça s'entend tout de suite."],
         ["placer y après le verbe","« j'y vais », jamais « je vais y »",
          "<b>y</b> se colle <u>devant</u> le verbe. C'est l'inverse de l'anglais, et c'est ce qui demande le plus de pratique."],
         ["oublier y avec le futur proche","on dit « je vais y aller »",
          "Avec deux verbes, <b>y</b> se place devant celui qui porte le sens : « je vais <b>y</b> aller », « je dois <b>y</b> retourner »."],
       ]},

      {t:'check', h:"Est-ce que c'est clair maintenant ?",
       p:"Quatre questions rapides.",
       qs:[
         {q:"« Je vais au gymnase » devient…", opts:["j'y vais","je vais y"], ok:0,
          fb:"<b>y</b> se met devant le verbe : « j'y vais »."},
         {q:"Au passé composé, y se place…", opts:["devant l'auxiliaire","après le participe"], ok:0,
          fb:"« j'<b>y</b> suis allée » — devant l'auxiliaire."},
         {q:"« On mangeait sur le balcon » devient plutôt…", opts:["on y mangeait","on mangeait là"], ok:1,
          fb:"Les deux se disent, mais <b>là</b> est plus naturel ici : on parle d'un endroit déjà nommé."},
         {q:"Après avoir dit « j'y vais », faut-il nommer le lieu ?", opts:["oui, pour être clair","non, il est déjà dans le y"], ok:1,
          fb:"Le redire est une faute : <b>y</b> contient déjà le lieu."},
       ]},
    ]
  },

  t3carte: {
    eye:'Mini-leçon', tit:"La carte postale et la carte de vœux",
    blocs:[
      {t:'texte', h:"Deux cartes, deux buts",
       p:"Les deux tiennent en quelques lignes, mais elles ne servent pas à la même chose. La <b>carte postale</b> raconte <b>où vous êtes</b> et ce que vous y faites. La <b>carte de vœux</b> <b>félicite</b> ou <b>souhaite</b> quelque chose à quelqu'un, à l'occasion d'un évènement.",
       note:"Se tromper de genre se remarque tout de suite : raconter son voyage sur une carte de naissance met l'attention au mauvais endroit."},

      {t:'ana', h:"La carte postale — quatre parties",
       p:"On la lit en dix secondes. Elle suit presque toujours le même ordre.",
       mots:[['1','Bonjour Fatou,'],['2','Je t\'écris de {Québec}',true],['3','Hier, on a visité le Vieux-Port'],['4','Tu me manques. Je t\'embrasse.']],
       say:"Je t'écris de Québec, il neige depuis hier.",
       note:"Les verbes y sont au <b>présent</b> (où je suis, ce que je vois) et au <b>passé composé</b> (ce que j'ai fait hier)."},

      {t:'ana', h:"La carte de vœux — trois lignes",
       p:"Encore plus court. On félicite, on souhaite, on signe.",
       mots:[['1','Félicitations à vous deux !'],['2','Je vous souhaite {beaucoup de bonheur}',true],['3','Mariama']],
       say:"Félicitations à vous deux ! Je vous souhaite beaucoup de bonheur.",
       note:"On ne raconte pas sa propre vie sur une carte de vœux. Elle parle de l'autre, pas de soi."},

      {t:'texte', h:"Les formules qui vont avec l'occasion",
       p:"Chaque évènement a ses mots. <b>Naissance</b> : « Bienvenue au petit ! Toutes nos félicitations. » · <b>Mariage</b> : « Beaucoup de bonheur à vous deux. » · <b>Nouvel An</b> : « Meilleurs vœux pour la nouvelle année. » · <b>Décès</b> : « Mes sincères condoléances. »",
       note:"Ces formules sont figées : on ne les invente pas, on les réutilise telles quelles. C'est une bonne nouvelle — il y en a une dizaine à connaître, pas plus."},

      {t:'labo', h:"Quelle carte, quelle phrase ?",
       p:"Choisissez une occasion et voyez ce qu'on écrit.",
       axes:[{id:'p', lbl:'Quelle occasion ?', opts:[
         ['a','un voyage à Québec'],
         ['b','une naissance'],
         ['c','un mariage'],
         ['d','le Nouvel An'],
         ['e','un déménagement']]}],
       out:{
         a:{w:["Je t'écris de {Québec}, il neige depuis hier."], say:"Je t'écris de Québec, il neige depuis hier.", n:'carte postale — où je suis, ce que je fais'},
         b:{w:['Bienvenue à la petite {Aminata} !'], say:"Bienvenue à la petite Aminata ! Toutes nos félicitations.", n:'carte de vœux — on félicite'},
         c:{w:['Beaucoup de {bonheur} à vous deux.'], say:"Beaucoup de bonheur à vous deux.", n:'carte de vœux — on souhaite'},
         d:{w:['Meilleurs {vœux} pour la nouvelle année.'], say:"Meilleurs vœux pour la nouvelle année.", n:'carte de vœux — formule figée'},
         e:{w:['Bonne {installation} dans votre nouveau chez-vous !'], say:"Bonne installation dans votre nouveau chez-vous !", n:'carte de vœux — on souhaite'},
       },
       note:"Une seule des cinq est une carte postale. Toutes les autres félicitent ou souhaitent."},

      {t:'ex', h:"Des phrases de vraies cartes",
       p:"Écoutez et devinez de quelle carte chacune vient.",
       rows:[
         ["Je t'écris de la terrasse d'un café, en face du fleuve.","carte postale"],
         ["Félicitations à vous deux pour cette belle nouvelle !","carte de vœux"],
         ["Hier, on a marché dans le Vieux-Port toute la journée.","carte postale"],
         ["Je vous souhaite beaucoup de bonheur avec le petit.","carte de vœux"],
         ["Il fait moins quinze, mais le soleil est magnifique.","carte postale"],
         ["Meilleurs vœux pour la nouvelle année, à toi et à ta famille.","carte de vœux"],
       ]},

      {t:'piege', h:"Trois pièges à connaître",
       rows:[
         ["écrire une lettre au lieu d'une carte","trois à six phrases suffisent",
          "Une carte n'est pas une lettre. Si vous avez besoin de dix phrases, écrivez un courriel."],
         ["parler de soi sur une carte de vœux","« je vous souhaite » et non « moi, cette année… »",
          "La carte de vœux est tournée vers l'autre. On peut signer, mais on ne raconte pas sa propre vie."],
         ["oublier de signer","le nom, seul, à la fin",
          "Sur une carte, on signe simplement de son prénom. Pas de « cordialement », pas de formule longue."],
       ]},

      {t:'check', h:"Est-ce que c'est clair maintenant ?",
       p:"Quatre questions rapides.",
       qs:[
         {q:"« Hier, on a visité le Vieux-Port » vient…", opts:["d'une carte postale","d'une carte de vœux"], ok:0,
          fb:"On raconte où on est et ce qu'on y fait : c'est une <b>carte postale</b>."},
         {q:"Sur une carte de vœux, on parle surtout…", opts:["de soi","de la personne à qui on écrit"], ok:1,
          fb:"On félicite ou on souhaite : la carte est tournée vers l'autre."},
         {q:"Pour une naissance, on écrit…", opts:["Meilleurs vœux pour la nouvelle année","Bienvenue au petit ! Toutes nos félicitations"], ok:1,
          fb:"Chaque occasion a sa formule figée."},
         {q:"La bonne longueur d'une carte, c'est…", opts:["trois à six phrases","une page complète"], ok:0,
          fb:"Une carte se lit en dix secondes. Au-delà, écrivez un courriel."},
       ]},
    ]
  },

  t3cause: {
    eye:'Mini-leçon', tit:"grâce à ou à cause de",
    blocs:[
      {t:'texte', h:"La même question, deux réponses",
       p:"Les deux répondent à « pourquoi ? ». Mais ils ne sont pas neutres : <b>grâce à</b> annonce que le résultat est <b>heureux</b>, <b>à cause de</b> qu'il est <b>malheureux</b> ou au moins ennuyeux.",
       note:"Choisir le mauvais change le sens de la phrase. « À cause de ma voisine, j'ai aimé l'hiver » laisse entendre que c'est un problème."},

      {t:'ana', h:"grâce à — le bon résultat",
       p:"On remercie, on reconnaît une aide. Souvent une personne, parfois une chose.",
       mots:[['Ce que ça annonce','un résultat heureux'],['Suivi de','un nom ou un pronom',true],['Comme dans','{grâce à} cette voisine']],
       say:"Grâce à cette voisine, j'ai compris qu'on pouvait aimer l'hiver.",
       note:"Autres exemples : <b>grâce au</b> covoiturage · <b>grâce à</b> ses coéquipières · <b>grâce à</b> toi."},

      {t:'ana', h:"à cause de — le résultat ennuyeux",
       p:"On explique un problème, un empêchement, un départ.",
       mots:[['Ce que ça annonce','un résultat ennuyeux'],['Suivi de','un nom ou un pronom',true],['Comme dans','{à cause du} bruit']],
       say:"On est partis à cause du bruit.",
       note:"Autres exemples : <b>à cause de</b> la pluie · <b>à cause de</b> son horaire · <b>à cause des</b> voisins."},

      {t:'ana', h:"La fusion avec le et les",
       p:"Les deux se fusionnent avec le déterminant qui suit. C'est là que les fautes arrivent.",
       mots:[['à cause de + le','à cause {du}'],['à cause de + les','à cause {des}',true],['grâce à + le','grâce {au}']],
       say:"Grâce au covoiturage, elle n'attend plus l'autobus.",
       note:"On n'écrit jamais « à cause de le bruit » ni « grâce à le covoiturage ». La fusion est obligatoire."},

      {t:'texte', h:"Et si je veux enchaîner sur un verbe ?",
       p:"<b>grâce à</b> et <b>à cause de</b> sont toujours suivis d'un <b>nom</b> ou d'un <b>pronom</b>, jamais d'un verbe conjugué. Pour un verbe, prenez <b>parce que</b>.",
       note:"« Je suis restée <b>parce qu'</b>il faisait froid » — et non « à cause de il faisait froid »."},

      {t:'labo', h:"Heureux ou ennuyeux ?",
       p:"Choisissez une phrase et voyez lequel s'impose.",
       axes:[{id:'p', lbl:'Quelle phrase ?', opts:[
         ['a','la voisine qui l\'a emmenée glisser'],
         ['b','le bruit du bar en bas'],
         ['c','le covoiturage du jeudi'],
         ['d','la pluie du premier juillet'],
         ['e','la collègue qui lui a parlé du centre']]}],
       out:{
         a:{w:['{Grâce à} cette voisine'], say:"Grâce à cette voisine, j'ai aimé l'hiver.", n:'résultat heureux → grâce à'},
         b:{w:['{à cause du} bruit'], say:"On est partis à cause du bruit.", n:'résultat ennuyeux → à cause de + du'},
         c:{w:['{Grâce au} covoiturage'], say:"Grâce au covoiturage, elle n'attend plus l'autobus.", n:'résultat heureux → grâce à + au'},
         d:{w:['{à cause de la} pluie'], say:"Le déménagement a été long à cause de la pluie.", n:'résultat ennuyeux → à cause de + la'},
         e:{w:['{Grâce à} sa collègue'], say:"Grâce à sa collègue, elle a découvert le centre.", n:'résultat heureux → grâce à'},
       },
       note:"Le test le plus rapide : remplacez par « heureusement » ou « malheureusement » et écoutez lequel sonne juste."},

      {t:'ex', h:"Les phrases du module",
       p:"Écoutez chacune et repérez la cause.",
       rows:[
         ["Grâce à cette voisine, j'ai aimé l'hiver.","résultat heureux"],
         ["On est partis à cause du bruit.","résultat ennuyeux"],
         ["Grâce au covoiturage, elle n'attend plus l'autobus.","résultat heureux"],
         ["Elle a manqué deux entraînements à cause de son horaire.","résultat ennuyeux"],
         ["Grâce à ses coéquipières, elle s'est fait des amies.","résultat heureux"],
         ["Le déménagement a été long à cause de la pluie.","résultat ennuyeux"],
       ]},

      {t:'piege', h:"Trois pièges à connaître",
       rows:[
         ["oublier la fusion","« à cause du bruit », jamais « à cause de le bruit »",
          "de + le = <b>du</b>, de + les = <b>des</b>, à + le = <b>au</b>, à + les = <b>aux</b>. La fusion est obligatoire en français."],
         ["mettre un verbe après","« parce qu'il faisait froid »",
          "<b>grâce à</b> et <b>à cause de</b> ne prennent qu'un nom ou un pronom. Pour un verbe conjugué, c'est <b>parce que</b>."],
         ["employer « à cause de » pour une bonne nouvelle","« grâce à mes amies » et non « à cause de mes amies »",
          "Dire « à cause de mes amies, je me suis fait des amies » fait entendre un reproche. Le choix n'est jamais neutre."],
       ]},

      {t:'check', h:"Est-ce que c'est clair maintenant ?",
       p:"Quatre questions rapides.",
       qs:[
         {q:"« ___ cette voisine, j'ai aimé l'hiver » demande…", opts:["Grâce à","À cause de"], ok:0,
          fb:"Le résultat est heureux : <b>grâce à</b>."},
         {q:"« Ils sont partis ___ bruit » demande…", opts:["à cause du","à cause de le"], ok:0,
          fb:"de + le = <b>du</b>. La fusion est obligatoire."},
         {q:"Après grâce à, on peut mettre…", opts:["un verbe conjugué","un nom ou un pronom"], ok:1,
          fb:"Pour un verbe, il faut <b>parce que</b>."},
         {q:"« Grâce à » et « à cause de » sont…", opts:["interchangeables","porteurs d'un jugement différent"], ok:1,
          fb:"L'un annonce du bon, l'autre du mauvais. Ce n'est jamais neutre."},
       ]},
    ]
  },
};
