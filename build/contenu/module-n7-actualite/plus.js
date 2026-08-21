const PLUS = {

  prE: {
    eye:'Mini-leçon', tit:"Le « e » qu'on entend et celui qui disparaît",
    blocs:[
      {t:'texte', h:"Le son le plus discret du français",
       p:"Il y a dans le français un petit son qui n'a pas de nom dans la vie courante : le « e » de <i>petit</i>, de <i>demain</i>, de <i>samedi</i>. Parfois on l'entend, parfois il s'efface complètement. Et ce n'est pas de la négligence : ce sont deux prononciations correctes, choisies selon la place du « e » dans le mot.",
       note:"On l'appelle le <b>e caduc</b> — « caduc » veut dire « qui tombe ». Son symbole est <b>[ə]</b>."},

      {t:'texte', h:"Pourquoi ça compte pour comprendre la radio",
       p:"Un reportage se dit vite. Si vous cherchez « main-te-nant » en trois morceaux, vous ne le trouverez jamais : le journaliste dit <i>main-t'nant</i>, en deux. Le mot que vous connaissez très bien devient méconnaissable, et vous croyez avoir manqué du vocabulaire alors que vous avez seulement manqué un « e » tombé.",
       note:"C'est la première cause d'incompréhension à l'oral chez les adultes qui lisent pourtant très bien."},

      {t:'ana', h:"Cas 1 — Le « e » se maintient au début du mot après p, b, t, d, k, g",
       p:"Quand le « e » est dans la <b>première syllabe</b> et que le mot commence par une de ces consonnes qui ferment complètement la bouche, on le garde.",
       mots:[['On écrit','p{e}tit · d{e}main · t{e}nir · d{e}gré · d{e}hors'],['On entend','[ə] bien présent',true],['Le repère','la bouche se ferme d\'abord, puis le « e » sort']],
       say:"petit, demain, tenir, un degré, dehors",
       note:"Ces consonnes s'appellent des <b>occlusives</b> : l'air est bloqué un instant, puis relâché."},

      {t:'ana', h:"Cas 2 — Le « e » se maintient devant les sons [rj] et [lj]",
       p:"Devant un « ri » ou un « li » suivi d'une voyelle, le « e » reste, sinon le mot devient impossible à dire.",
       mots:[['On écrit','un at{e}lier · un hôt{e}lier · une chev{a}lière'],['On entend','[ə] bien présent',true],['Essayez sans','« atlier » : la langue butte']],
       say:"un atelier, un hôtelier",
       note:"C'est un cas rare, mais il ne souffre aucune exception."},

      {t:'ana', h:"Cas 3 — Ailleurs, le « e » tombe presque toujours",
       p:"Au milieu du mot, quand une seule consonne le précède, il s'efface dans la conversation normale.",
       mots:[['On écrit','sam{e}di · ach{e}ter · maint{e}nant · la s{e}maine'],['On entend','[samdi] · [aʃte] · [mɛ̃tnɑ̃]',true],['La règle','une seule consonne devant → il tombe']],
       say:"samedi, acheter, maintenant, la semaine",
       note:"Attention : s'il y a <b>deux</b> consonnes devant, il revient — <i>appartement</i>, <i>justement</i>, <i>autrement</i> gardent leur « e »."},

      {t:'labo', h:"Écoutez la différence",
       p:"Choisissez un mot et le cas qui vous intéresse.",
       axes:[
         {id:'c', lbl:'Quel cas ?', opts:[['a','début de mot'],['b','devant ri / li'],['c','milieu de mot']]},
         {id:'n', lbl:'Quel exemple ?', opts:[['1','le premier'],['2','le second']]}],
       out:{
         a1:{w:["petit"], say:"petit", n:'« p » est une occlusive : le « e » reste'},
         a2:{w:["demain"], say:"demain", n:'« d » aussi : on entend « de-main »'},
         b1:{w:["un atelier"], say:"un atelier", n:'devant [lj], le « e » ne tombe jamais'},
         b2:{w:["un hôtelier"], say:"un hôtelier", n:'même cas, même prononciation'},
         c1:{w:["samedi"], say:"samedi", n:'deux syllabes à l\'oral : [samdi]'},
         c2:{w:["maintenant"], say:"maintenant", n:'[mɛ̃tnɑ̃] — c\'est ça qu\'on entend à la radio'},
       },
       note:"Écoutez deux fois, puis répétez à voix haute avant de passer au suivant."},

      {t:'ex', h:"Six mots du module, à écouter et à répéter",
       p:"À gauche, ce qui est écrit. À droite, ce qui se dit.",
       rows:[
         ["petit","« pe-tit » — le « e » se dit"],
         ["demain","« de-main » — le « e » se dit"],
         ["un atelier","« a-te-lier » — le « e » se dit"],
         ["samedi","« sam'di » — le « e » tombe"],
         ["maintenant","« main-t'nant » — le « e » tombe"],
         ["franchement","« franch'ment » — le « e » tombe"],
       ]},

      {t:'piege', h:"Deux pièges et une bonne nouvelle",
       rows:[
         ["prononcer chaque « e » écrit","laisser tomber ceux du milieu",
          "Dire « ma-in-te-nant » en quatre morceaux se comprend, mais sonne appliqué et ralentit tout. Personne ne parle comme ça."],
         ["croire qu'on n'a pas compris le mot","reconnaître le mot amputé",
          "Quand vous entendez [samdi] et que vous cherchez « samedi », le problème n'est pas votre vocabulaire. Entraînez l'oreille à la forme courte."],
         ["s'inquiéter de se tromper","les deux formes se comprennent",
          "Bonne nouvelle : garder un « e » qui aurait pu tomber ne provoque aucun malentendu. C'est seulement à l'écoute que ça compte vraiment."],
       ]},

      {t:'check', h:"Est-ce que c'est clair maintenant ?",
       p:"Quatre questions rapides.",
       qs:[
         {q:"Dans « demain », le « e »…", opts:["se prononce","tombe"], ok:0,
          fb:"Première syllabe, et « d » est une occlusive : il se maintient."},
         {q:"Dans « samedi », le « e » du milieu…", opts:["se prononce","tombe"], ok:1,
          fb:"Une seule consonne devant : on dit [samdi]."},
         {q:"Dans « un atelier », le « e »…", opts:["se prononce","tombe"], ok:0,
          fb:"Devant le son [lj], il ne tombe jamais."},
         {q:"Si deux consonnes précèdent le « e », il…", opts:["revient","tombe quand même"], ok:0,
          fb:"C'est le cas d'« appartement » ou de « justement »."},
       ]},
    ]
  },

  prFaitOpinion: {
    eye:'Mini-leçon', tit:"Séparer le fait de l'opinion",
    blocs:[
      {t:'texte', h:"La question à se poser, et une seule",
       p:"« Est-ce que je pourrais aller vérifier ? » Si oui, c'est un <b>fait</b>. Si la réponse dépend de qui on interroge, c'est une <b>opinion</b>. C'est tout. Le fait n'est pas forcément vrai — il peut être faux — mais il est <i>vérifiable</i>, et c'est ça qui le définit.",
       note:"« La consigne est de trente cents » est un fait. Un fait <b>faux</b>, mais un fait : on peut aller le contredire."},

      {t:'texte', h:"Pourquoi c'est le travail le plus utile",
       p:"Quand on suit l'actualité dans une langue qu'on apprend, on comprend d'abord les mots, puis les phrases, puis les informations. Le dernier étage, c'est celui-ci : savoir lesquelles de ces informations engagent celui qui parle et lesquelles ne l'engagent pas. C'est ce qui permet de discuter d'une nouvelle sans se faire emporter par le ton de celui qui la raconte.",
       note:"Le programme du niveau 7 le formule ainsi : distinguer l'information factuelle des opinions lorsque la distinction est explicite."},

      {t:'ana', h:"Les marques du fait",
       p:"Il se mesure, se date, se compte, se nomme.",
       mots:[['Des chiffres','cent quarante mètres carrés · huit places · quinze minutes'],
             ['Des dates','le 1er novembre 2023 · le 14 octobre'],
             ['Des noms précis','le comité exécutif · le conseil municipal'],
             ['Un verbe neutre','est · a été retenu · comprend',true]],
       note:"Le fait n'a besoin d'aucun adjectif pour tenir debout."},

      {t:'ana', h:"Les marques de l'opinion",
       p:"Elle apprécie, elle juge, elle réclame.",
       mots:[['Des adjectifs de valeur','ridicule · scandaleux · excellent · inacceptable'],
             ['Des adverbes','trop · enfin · encore une fois · malheureusement'],
             ['Des verbes','je trouve · je pense · il faudrait · on devrait',true],
             ['Des questions rhétoriques','« Faut-il vraiment attendre encore un an ? »']],
       note:"Aucun de ces mots ne se vérifie. Deux personnes de bonne foi peuvent les employer en sens contraire."},

      {t:'texte', h:"Le cas difficile : le faux fait",
       p:"Certaines phrases ont la forme d'un constat et le contenu d'un jugement. <i>« Ce projet a été imposé au quartier. »</i> Grammaticalement, c'est une phrase passive au passé composé, comme <i>« le local a été retenu »</i>. Mais « retenir » se constate, tandis qu'« imposer » suppose déjà qu'on a mal agi.",
       note:"Le test : remplacez le mot par un synonyme neutre. « Imposé » → « recommandé ». Si le sens change beaucoup, il y avait un jugement caché."},

      {t:'ex', h:"Six phrases du dossier, triées",
       p:"À gauche la phrase, à droite ce qu'elle est.",
       rows:[
         ["Le local est vide depuis deux ans.","FAIT — on peut aller voir"],
         ["Ce local vide fait honte au quartier.","OPINION — « faire honte » se discute"],
         ["Deux places seront réservées quinze minutes.","FAIT — c'est écrit dans la recommandation"],
         ["Quinze minutes, c'est une idée de bureau.","OPINION — jugement sur ceux qui décident"],
         ["Personne ne connaît les heures d'ouverture.","FAIT — la conseillère l'a confirmé"],
         ["La Ville a décidé sans nous.","OPINION — « sans nous » interprète une procédure"],
       ]},

      {t:'check', h:"Est-ce que c'est clair maintenant ?",
       p:"Quatre questions rapides.",
       qs:[
         {q:"Un fait, c'est une information…", opts:["vraie","vérifiable"], ok:1,
          fb:"Un fait peut être faux. Ce qui le définit, c'est qu'on peut aller voir."},
         {q:"« Il faudrait un deuxième dépôt » est…", opts:["un fait","une opinion"], ok:1,
          fb:"« Il faudrait » réclame quelque chose : c'est un avis."},
         {q:"Une chronique contient…", opts:["seulement des opinions","des faits et des opinions"], ok:1,
          fb:"Les faits y sont souvent exacts : c'est ce qui donne du poids au jugement."},
         {q:"« Le projet a été imposé » est…", opts:["un constat neutre","un jugement déguisé"], ok:1,
          fb:"« Imposé » suppose déjà une faute. « Recommandé » serait le mot neutre."},
       ]},

      {t:'revoir', h:"À retenir",
       p:"Une seule question : <b>est-ce que je pourrais aller vérifier ?</b> Oui → fait. Ça dépend de qui on demande → opinion. Et méfiez-vous des verbes qui jugent en ayant l'air de constater."},
    ]
  },

  t1cond: {
    eye:'Mini-leçon', tit:"Le conditionnel de l'information non confirmée",
    blocs:[
      {t:'texte', h:"Un temps qui veut dire « attention »",
       p:"À la radio, vous entendrez deux phrases presque identiques : <i>« Le local <b>est</b> loué pour cinq ans »</i> et <i>« Le local <b>serait</b> loué pour cinq ans »</i>. Un seul son change, et pourtant tout change : dans le premier cas le journaliste répond de l'information, dans le second il vous prévient qu'il ne l'a pas vérifiée.",
       note:"Ce n'est pas de la politesse ni de l'hésitation : c'est une règle de métier. Affirmer sans avoir vérifié est une faute professionnelle."},

      {t:'ana', h:"Comment il se forme",
       p:"Le radical du futur simple, plus les terminaisons de l'imparfait.",
       mots:[['Le radical','celui du futur : ouvrir → il ouvrir{a}'],
             ['Les terminaisons','-ais · -ais · -ait · -ions · -iez · -aient'],
             ['Le résultat','il ouvrir{ait} · ils ouvrir{aient}',true],
             ['Ça se prononce','[ɛ] au singulier comme au pluriel']],
       note:"<b>il ouvrira</b> (futur) et <b>il ouvrirait</b> (conditionnel) ne diffèrent que par la fin. C'est peu, et c'est décisif."},

      {t:'ana', h:"Les trois verbes du journaliste",
       p:"Ce sont ceux qui reviennent dans presque tous les reportages.",
       mots:[['être','il ser{ait} · ils ser{aient}'],
             ['avoir','il aur{ait} · ils aur{aient}'],
             ['pouvoir','il pourr{ait} · ils pourr{aient}',true],
             ['devoir','il devr{ait}']],
       say:"il serait, il aurait, il pourrait, il devrait",
       note:"Apprenez ces quatre-là par cœur et vous reconnaîtrez l'immense majorité des cas."},

      {t:'texte', h:"Les mots qui l'annoncent",
       p:"Le conditionnel arrive rarement seul. Il est presque toujours précédé d'une formule qui dit d'où vient l'information : <b>selon nos informations</b>, <b>selon une source proche du dossier</b>, <b>on apprend que</b>, <b>il semble que</b>, <b>d'après ce qu'on nous rapporte</b>.",
       note:"Quand vous entendez « selon nos informations », préparez-vous : le verbe qui suit sera au conditionnel, et l'information n'est pas confirmée."},

      {t:'labo', h:"Confirmé ou pas ?",
       p:"Choisissez une phrase et la version que vous voulez entendre.",
       axes:[
         {id:'p', lbl:'Quelle phrase ?', opts:[['a','le local'],['b','les travaux'],['c','les heures']]},
         {id:'v', lbl:'Quelle version ?', opts:[['1','confirmée'],['2','non confirmée']]}],
       out:{
         a1:{w:["Le local est loué pour cinq ans."], say:"Le local est loué pour cinq ans.", n:'présent : le journaliste répond de l\'information'},
         a2:{w:["Le local serait loué pour cinq ans."], say:"Le local serait loué pour cinq ans.", n:'conditionnel : on le lui a dit, il n\'a pas vérifié'},
         b1:{w:["Les travaux commencent au printemps."], say:"Les travaux commencent au printemps.", n:'c\'est établi'},
         b2:{w:["Les travaux commenceraient au printemps."], say:"Les travaux commenceraient au printemps.", n:'à prendre avec précaution'},
         c1:{w:["Le dépôt est ouvert six jours sur sept."], say:"Le dépôt est ouvert six jours sur sept.", n:'confirmé'},
         c2:{w:["Le dépôt serait ouvert six jours sur sept."], say:"Le dépôt serait ouvert six jours sur sept.", n:'la Ville l\'indique, sans l\'écrire noir sur blanc'},
       },
       note:"Écoutez la fin du verbe. C'est le seul endroit où la différence se joue."},

      {t:'piege', h:"Trois pièges",
       rows:[
         ["confondre avec la politesse","reconnaître le contexte",
          "<i>« Pourriez-vous répéter ? »</i> est aussi un conditionnel, mais c'est de la politesse, pas du doute. Dans un reportage, c'est du doute."],
         ["confondre avec l'hypothèse","chercher le « si »",
          "<i>« S'il ouvrait, ce serait mieux »</i> : là, le conditionnel dépend d'un « si » imaginaire. Pas de « si » dans la phrase ? C'est de l'information non confirmée."],
         ["croire que le conditionnel veut dire faux","il veut dire non vérifié",
          "Une information au conditionnel se révèle souvent exacte. Le journaliste dit seulement qu'il ne la garantit pas encore."],
       ]},

      {t:'check', h:"Est-ce que c'est clair maintenant ?",
       p:"Quatre questions rapides.",
       qs:[
         {q:"« Les travaux commenceraient au printemps » signifie…", opts:["c'est confirmé","ce n'est pas confirmé"], ok:1,
          fb:"Conditionnel présent, sans « si » : information non vérifiée."},
         {q:"Le conditionnel se forme sur le radical…", opts:["de l'imparfait","du futur simple"], ok:1,
          fb:"Radical du futur, terminaisons de l'imparfait."},
         {q:"« Selon nos informations » annonce…", opts:["un présent","un conditionnel"], ok:1,
          fb:"C'est le signal le plus fiable."},
         {q:"Une information au conditionnel est…", opts:["fausse","non vérifiée"], ok:1,
          fb:"Elle se révèle souvent exacte — mais elle n'est pas garantie."},
       ]},

      {t:'revoir', h:"À retenir",
       p:"<b>-ait</b> à la fin du verbe dans un reportage, sans « si » dans la phrase : le journaliste vous dit qu'il n'a pas vérifié. Écoutez la fin des verbes, c'est là que se cache l'avertissement."},
    ]
  },

  t1conn: {
    eye:'Mini-leçon', tit:"Les connecteurs qui tiennent un long discours",
    blocs:[
      {t:'texte', h:"Trois minutes sans se perdre",
       p:"Un reportage n'est pas une liste d'informations : c'est un parcours. Le journaliste vous prend au début et vous dépose à la fin, et pour que vous ne décrochiez pas en route, il pose des panneaux. Ces panneaux sont les <b>connecteurs</b>. Les repérer, c'est comme suivre les numéros de sortie sur une autoroute : même si vous manquez un bout de paysage, vous savez où vous êtes.",
       note:"C'est une stratégie d'écoute autant qu'un point de grammaire."},

      {t:'ana', h:"Ouvrir : ce qu'il faut savoir avant",
       p:"Le journaliste pose le décor et rappelle ce qui est déjà connu.",
       mots:[['Annoncer le plan','d\'abord · premièrement · commençons par'],
             ['Rappeler l\'acquis','rappelons que · on se souviendra que'],
             ['Ce que ça vous dit','ce qui suit est du contexte, pas la nouvelle',true]],
       note:"« Rappelons que » signale une information ancienne. Si vous la connaissez déjà, vous pouvez relâcher l'attention deux secondes."},

      {t:'ana', h:"Changer de sujet : la topicalisation",
       p:"Le journaliste ferme un aspect et en ouvre un autre. Ce sont les connecteurs les plus utiles à l'écoute.",
       mots:[['Les formules','quant à · en ce qui concerne · à propos de · à l\'égard de'],
             ['Un exemple','<i>Quant à la date d\'ouverture, elle n\'est pas arrêtée.</i>'],
             ['Ce que ça vous dit','nouveau sujet — remettez-vous en marche',true]],
       note:"Elles sont toujours suivies du sujet dont on va parler. Le mot qui vient juste après vous donne le thème du paragraphe."},

      {t:'ana', h:"Ajouter, reformuler, conclure",
       p:"Les trois derniers rôles.",
       mots:[['Ajouter un aspect','par ailleurs · d\'autre part'],
             ['Redire plus simplement','autrement dit · c\'est-à-dire · en d\'autres termes'],
             ['Résumer ou conclure','en somme · donc · par conséquent',true]],
       note:"<b>Autrement dit</b> est un cadeau : le journaliste vient de dire quelque chose de technique et il le retraduit. Si vous avez manqué la version savante, la version simple arrive."},

      {t:'texte', h:"La différence entre « en somme » et « par conséquent »",
       p:"On les confond souvent. <b>En somme</b> résume : il rassemble ce qui vient d'être dit, sans rien ajouter. <b>Par conséquent</b> conclut : il tire une conséquence, donc il ajoute quelque chose de nouveau. <i>« En somme : un local vide, deux emplacements, une décision en octobre »</i> résume. <i>« Le local est plus grand, par conséquent le comité l'a retenu »</i> explique.",
       note:"À l'écrit, employer « par conséquent » là où il n'y a aucune conséquence est l'erreur la plus visible."},

      {t:'ex', h:"Les sept panneaux du reportage",
       p:"Dans l'ordre où ils apparaissent.",
       rows:[
         ["D'abord, les faits.","on ouvre"],
         ["Rappelons que la consigne est de dix cents…","contexte connu"],
         ["Autrement dit, il y a de plus en plus de contenants…","traduction simple"],
         ["Quant à la date d'ouverture…","nouveau sujet"],
         ["Par ailleurs, tout le monde n'accueille pas…","autre aspect"],
         ["En ce qui concerne les heures d'ouverture…","nouveau sujet"],
         ["En somme : un local vide, deux emplacements…","résumé final"],
       ]},

      {t:'piege', h:"Deux pièges",
       rows:[
         ["entendre « par ailleurs » comme « en plus »","c'est « d'un autre côté »",
          "« En plus » ajoute dans la même direction. « Par ailleurs » ouvre un autre angle du même dossier, souvent contraire."],
         ["croire que « quant à » veut dire « quand »","ça n'a aucun rapport",
          "<i>Quant à</i> introduit un sujet ; <i>quand</i> introduit un moment. Ils se ressemblent à l'oreille et ne se ressemblent en rien."],
       ]},

      {t:'check', h:"Est-ce que c'est clair maintenant ?",
       p:"Quatre questions rapides.",
       qs:[
         {q:"« Quant à » annonce…", opts:["un moment","un nouveau sujet"], ok:1,
          fb:"Le mot qui suit vous donne le thème du paragraphe."},
         {q:"« Autrement dit » annonce…", opts:["une reformulation simple","une conséquence"], ok:0,
          fb:"Le journaliste retraduit ce qu'il vient de dire."},
         {q:"« En somme » sert à…", opts:["résumer","tirer une conséquence"], ok:0,
          fb:"Pour la conséquence, c'est « par conséquent »."},
         {q:"« Par ailleurs » veut dire…", opts:["en plus, dans le même sens","d'un autre côté"], ok:1,
          fb:"Il ouvre un autre angle, souvent contraire."},
       ]},
    ]
  },

  t2passif: {
    eye:'Mini-leçon', tit:"La phrase passive, ou l'art de ne pas nommer",
    blocs:[
      {t:'texte', h:"Pourquoi les articles en sont pleins",
       p:"Lisez n'importe quel article informatif : personne n'y agit. <i>Le communiqué a été publié. Le local a été retenu. La décision sera prise.</i> Ce n'est pas un tic d'écriture. C'est que dans une nouvelle, ce qui compte est souvent <b>ce qui est arrivé</b>, et non celui qui l'a fait.",
       note:"Le français appelle ça la <b>voix passive</b> : le sujet de la phrase subit l'action au lieu de la faire."},

      {t:'ana', h:"Comment on la fabrique",
       p:"Deux morceaux, toujours les mêmes.",
       mots:[['Le verbe être','au temps voulu : a été · sera · est'],
             ['Le participe passé','publié · retenu · pris · fixé'],
             ['Au passé composé','a été + participe passé',true],
             ['Un exemple','Le comité a retenu le local → Le local <b>a été retenu</b>']],
       note:"C'est <i>être</i> qui porte le temps. Le participe, lui, ne bouge pas."},

      {t:'ana', h:"L'accord se fait avec le sujet",
       p:"C'est la faute la plus fréquente, et la plus facile à éviter.",
       mots:[['Masculin singulier','Le dossier a été dépos{é}'],
             ['Féminin singulier','La décision a été pris{e}'],
             ['Masculin pluriel','Les locaux ont été visit{és}'],
             ['Féminin pluriel','Les heures ont été fix{ées}',true]],
       note:"Regardez le sujet, pas le complément. C'est lui qui commande la terminaison."},

      {t:'texte', h:"« Par » : présent, ou absent",
       p:"Quand on veut nommer celui qui agit, on l'introduit par <b>par</b> : <i>Le local a été retenu <b>par le comité</b>.</i> Mais très souvent, on ne le nomme pas : <i>Le communiqué a été publié hier soir.</i> Parfois parce que ça n'a pas d'importance, parfois parce qu'on ne le sait pas — et parfois parce que ça arrange tout le monde.",
       note:"C'est un point de lecture critique autant que de grammaire. Devant une passive sans « par », demandez-vous toujours : <i>qui</i> a fait ça ?"},

      {t:'texte', h:"Le cas de « de »",
       p:"Avec quelques verbes de sentiment ou de connaissance, l'auteur de l'action est introduit par <b>de</b> et non par <i>par</i> : <i>Cette décision est critiquée <b>de</b> tous. Il est respecté <b>de</b> ses employés. Elle est connue <b>de</b> tout le quartier.</i>",
       note:"C'est rare, un peu littéraire, et il suffit de savoir le reconnaître à la lecture."},

      {t:'ex', h:"Six passives de l'article, décortiquées",
       p:"À gauche la passive, à droite la phrase active correspondante.",
       rows:[
         ["Le communiqué a été publié.","Le service des communications a publié le communiqué."],
         ["Le local a été retenu par le comité.","Le comité a retenu le local."],
         ["La décision sera prise le 14 octobre.","Le conseil prendra la décision le 14 octobre."],
         ["Deux places seraient réservées.","On réserverait deux places."],
         ["Les heures n'ont pas été fixées.","On n'a pas fixé les heures."],
         ["La rue avait été refaite quatre ans plus tôt.","La Ville avait refait la rue quatre ans plus tôt."],
       ]},

      {t:'piege', h:"Trois pièges",
       rows:[
         ["accorder avec le complément","accorder avec le sujet",
          "<i>❌ La décision a été pris par le conseil.</i> → <i>✅ La décision a été pris<b>e</b>.</i> « Le conseil » est masculin, mais ce n'est pas le sujet."},
         ["oublier « été »","être + participe",
          "<i>❌ Le local a retenu par le comité.</i> Sans « été », la phrase dit le contraire : c'est le local qui retient quelqu'un."],
         ["employer la passive partout","alterner",
          "Un texte tout en passives devient froid et lourd. Les articles alternent : deux ou trois passives, puis une active."},
       ]},

      {t:'check', h:"Est-ce que c'est clair maintenant ?",
       p:"Quatre questions rapides.",
       qs:[
         {q:"« La décision a été ___ par le conseil. »", opts:["pris","prise"], ok:1,
          fb:"Accord avec « la décision », féminin singulier."},
         {q:"Une passive sans « par », ça veut dire…", opts:["personne n'a agi","on ne dit pas qui a agi"], ok:1,
          fb:"Quelqu'un a agi ; la phrase choisit de ne pas le nommer."},
         {q:"Dans « a été publié », c'est ___ qui porte le temps.", opts:["être","le participe"], ok:0,
          fb:"« a été » : c'est le verbe être au passé composé."},
         {q:"« Il est respecté de ses employés » est…", opts:["une faute","une passive correcte"], ok:1,
          fb:"Certains verbes introduisent l'agent par « de »."},
       ]},
    ]
  },

  t2indirect: {
    eye:'Mini-leçon', tit:"Rapporter des paroles quand le récit est au passé",
    blocs:[
      {t:'texte', h:"Le point de référence recule",
       p:"Quand vous racontez maintenant ce que quelqu'un a dit hier, vous vous placez à hier. Et depuis hier, ce qui était déjà fait est encore plus loin, ce qui restait à venir n'est pas encore arrivé. Le français rend ce déplacement visible en changeant les temps : c'est ce qu'on appelle la <b>concordance</b>.",
       note:"Cela ne se produit que si le verbe qui introduit est au passé. <i>Elle dit qu'elle viendra</i> ne change rien ; <i>elle a dit qu'elle viendrait</i>, oui."},

      {t:'ana', h:"Les trois déplacements",
       p:"Un tableau à connaître, et rien de plus.",
       mots:[['Ce qui était déjà fait','passé composé → <b>plus-que-parfait</b>'],
             ['Ce qui était en cours','présent → <b>imparfait</b>'],
             ['Ce qui restait à venir','futur → <b>conditionnel présent</b>',true],
             ['Variante parlée','futur proche → <b>allait</b> + infinitif']],
       note:"Trois lignes. Presque tout le discours indirect au passé tient là-dedans."},

      {t:'ana', h:"Le plus-que-parfait : ce qui précède le passé",
       p:"Avoir ou être à l'imparfait, plus le participe passé.",
       mots:[['La forme','il av{ait} perdu · elle ét{ait} venue'],
             ['Direct','« J\'ai perdu des clients. »'],
             ['Rapporté','Il a expliqué qu\'il <b>avait perdu</b> des clients.',true]],
       say:"Il a expliqué qu'il avait perdu des clients.",
       note:"C'est le temps du récit dans le récit : un passé vu depuis un autre passé."},

      {t:'ana', h:"Le conditionnel de postériorité",
       p:"L'avenir raconté depuis le passé.",
       mots:[['Direct','« Je vous rappellerai. »'],
             ['Rapporté','Elle a promis qu\'elle me <b>rappellerait</b>.'],
             ['Autre tournure','Elle a dit qu\'elle <b>allait</b> me rappeler.',true],
             ['Ce n\'est pas du doute','elle a bien promis — c\'est du futur, vu d\'hier']],
       say:"Elle a promis qu'elle me rappellerait.",
       note:"C'est ici que le module se referme sur lui-même : le même conditionnel qui, au Défi 1, marquait le doute, marque ici la postériorité. Le verbe introducteur tranche."},

      {t:'texte', h:"Ce qui change aussi, et qu'on oublie",
       p:"Les temps ne sont pas seuls à reculer. Les repères de temps et de lieu suivent : <b>hier</b> devient <i>la veille</i>, <b>demain</b> devient <i>le lendemain</i>, <b>maintenant</b> devient <i>alors</i>, <b>ici</b> devient <i>là</i>. Et les pronoms changent de personne : <i>« je vous rappellerai »</i> devient <i>elle <b>me</b> rappellerait</i>.",
       note:"Dans un article, c'est souvent au pronom qu'on repère qu'une parole est rapportée."},

      {t:'labo', h:"La même parole, direct et rapporté",
       p:"Choisissez une parole et la version que vous voulez entendre.",
       axes:[
         {id:'p', lbl:'Quelle parole ?', opts:[['a','le dossier'],['b','le rappel'],['c','les clients']]},
         {id:'v', lbl:'Quelle version ?', opts:[['1','au style direct'],['2','rapportée au passé']]}],
       out:{
         a1:{w:["« Le dossier est à l'étude. »"], say:"Le dossier est à l'étude.", n:'présent'},
         a2:{w:["Elle a précisé que le dossier était à l'étude."], say:"Elle a précisé que le dossier était à l'étude.", n:'présent → imparfait'},
         b1:{w:["« Je vous rappellerai. »"], say:"Je vous rappellerai.", n:'futur simple'},
         b2:{w:["Elle a promis qu'elle me rappellerait."], say:"Elle a promis qu'elle me rappellerait.", n:'futur → conditionnel, et « vous » → « me »'},
         c1:{w:["« J'ai perdu des clients. »"], say:"J'ai perdu des clients.", n:'passé composé'},
         c2:{w:["Il a expliqué qu'il avait perdu des clients."], say:"Il a expliqué qu'il avait perdu des clients.", n:'passé composé → plus-que-parfait'},
       },
       note:"Écoutez les deux versions à la suite : c'est le meilleur moyen d'entendre le déplacement."},

      {t:'piege', h:"Trois pièges",
       rows:[
         ["garder le futur","le futur devient conditionnel",
          "<i>❌ Elle a dit qu'elle me rappellera.</i> → <i>✅ qu'elle me rappellerait.</i> Après un verbe introducteur au passé, le futur ne survit pas."},
         ["lire le conditionnel comme un doute","regarder le verbe introducteur",
          "<i>Elle a promis qu'elle viendrait</i> ne dit aucun doute : elle a promis. C'est <i>selon nos informations, elle viendrait</i> qui doute."},
         ["oublier de changer les pronoms","« vous » devient « me »",
          "<i>« Je vous rappellerai » → elle a dit qu'elle <b>me</b> rappellerait.</i> Sans ce changement, on ne sait plus qui parle à qui."},
       ]},

      {t:'check', h:"Est-ce que c'est clair maintenant ?",
       p:"Quatre questions rapides.",
       qs:[
         {q:"« J'ai reçu l'analyse » rapporté au passé devient…", opts:["qu'il a reçu","qu'il avait reçu"], ok:1,
          fb:"Passé composé → plus-que-parfait."},
         {q:"« Je vous rappellerai » rapporté au passé devient…", opts:["qu'elle rappellera","qu'elle rappellerait"], ok:1,
          fb:"Futur → conditionnel présent."},
         {q:"La concordance se déclenche quand le verbe introducteur est…", opts:["au présent","au passé"], ok:1,
          fb:"« Elle dit que » ne change rien ; « elle a dit que », oui."},
         {q:"« Demain » devient, dans un récit au passé…", opts:["le lendemain","la veille"], ok:0,
          fb:"« Hier » devient « la veille » ; « demain », « le lendemain »."},
       ]},
    ]
  },

  t2nom: {
    eye:'Mini-leçon', tit:"La nominalisation : quand le verbe devient un nom",
    blocs:[
      {t:'texte', h:"La langue des titres",
       p:"Comparez : <i>« Le dépôt ouvrira en mars »</i> et <i>« Ouverture du dépôt en mars »</i>. Le second est plus court, commence par l'événement, et tient dans un titre. C'est la <b>nominalisation</b> : transformer un verbe en nom. Les journaux vivent de ce procédé, et les documents administratifs encore plus.",
       note:"Savoir la défaire — retrouver le verbe derrière le nom — est ce qui permet de comprendre un titre d'un coup d'œil."},

      {t:'ana', h:"Les suffixes qui reviennent",
       p:"Cinq terminaisons couvrent presque tout.",
       mots:[['-tion / -ation','installer → l\'installa{tion} · décider → la déci{sion}'],
             ['-ment','stationner → le stationne{ment}'],
             ['-ure','ouvrir → l\'ouvert{ure} · fermer → la fermet{ure}'],
             ['-age','dépanner → le dépann{age}',true],
             ['sans suffixe','reporter → le report · appeler → l\'appel']],
       note:"Le genre suit le suffixe : <b>-tion</b> et <b>-ure</b> sont féminins, <b>-ment</b> et <b>-age</b> sont masculins. C'est une règle presque sans exception."},

      {t:'ana', h:"Ce que devient le reste de la phrase",
       p:"Le complément se raccroche avec « de ».",
       mots:[['Phrase verbale','On a fermé <b>le local</b>.'],
             ['Phrase nominale','la fermeture <b>du</b> local'],
             ['Le sujet aussi','Les citoyens participent → la participation <b>des</b> citoyens',true]],
       note:"« de + le » donne « du », « de + les » donne « des ». C'est le seul calcul à faire."},

      {t:'texte', h:"Ce qu'on gagne et ce qu'on perd",
       p:"On gagne en concision : <i>« Report de la décision »</i> tient en quatre mots. Mais on perd deux choses, et ce n'est pas anodin : le nom ne dit ni <b>qui</b> a agi, ni <b>quand</b>. « Report de la décision » ne dit pas qui a reporté, ni si c'est fait ou prévu.",
       note:"C'est très commode pour informer vite — et très commode aussi pour ne pas désigner de responsable. Un titre nominal mérite toujours qu'on lise l'article."},

      {t:'ex', h:"Huit couples verbe / nom du dossier",
       p:"À gauche le verbe, à droite le nom.",
       rows:[
         ["installer","l'installation"],
         ["ouvrir","l'ouverture"],
         ["fermer","la fermeture"],
         ["stationner","le stationnement"],
         ["décider","la décision"],
         ["reporter","le report"],
         ["participer","la participation"],
         ["s'inquiéter","l'inquiétude"],
       ]},

      {t:'piege', h:"Deux pièges",
       rows:[
         ["inventer le nom","vérifier qu'il existe",
          "Tous les verbes n'ont pas de nom en -tion. <i>❌ la retenition</i> pour « retenir » : le nom est <b>la rétention</b>, et il ne s'emploie pas ici. Dans le doute, gardez le verbe."},
         ["se tromper de genre","suivre le suffixe",
          "<b>-tion</b> et <b>-ure</b> : féminin. <b>-ment</b> et <b>-age</b> : masculin. <i>la décision, l'ouverture, le stationnement, le dépannage.</i>"},
       ]},

      {t:'check', h:"Est-ce que c'est clair maintenant ?",
       p:"Quatre questions rapides.",
       qs:[
         {q:"Le nom formé sur « ouvrir » est…", opts:["l'ouvrement","l'ouverture"], ok:1,
          fb:"Suffixe -ure, et le nom est féminin."},
         {q:"« Stationnement » est…", opts:["masculin","féminin"], ok:0,
          fb:"Les noms en -ment sont masculins."},
         {q:"« Report de la décision » nous dit qui a reporté ?", opts:["oui","non"], ok:1,
          fb:"C'est précisément ce que la nominalisation efface."},
         {q:"« On a fermé le local » devient…", opts:["la fermeture du local","la fermeture le local"], ok:0,
          fb:"Le complément se raccroche avec « de » : de + le = du."},
       ]},
    ]
  },

  t3conc: {
    eye:'Mini-leçon', tit:"La concession : donner raison pour mieux objecter",
    blocs:[
      {t:'texte', h:"Le mouvement en deux temps",
       p:"Concéder, c'est accorder quelque chose à celui qui ne pense pas comme vous, puis maintenir votre objection. <i>« Bien que le projet parte d'une bonne intention, la décision s'est prise sans nous. »</i> La première moitié désarme le lecteur ; la seconde le garde. C'est la façon la plus efficace d'être en désaccord sans qu'on cesse de vous lire.",
       note:"C'est aussi ce que le programme attend au niveau 7 : comprendre <i>et</i> exprimer la concession."},

      {t:'ana', h:"« bien que » demande le subjonctif",
       p:"Sans exception. C'est la seule chose à retenir absolument.",
       mots:[['être','bien que ce <b>soit</b> · bien qu\'ils <b>soient</b>'],
             ['avoir','bien qu\'il <b>ait</b> · bien qu\'ils <b>aient</b>'],
             ['pouvoir','bien qu\'elle <b>puisse</b>'],
             ['venir','bien que ça <b>vienne</b>',true],
             ['faire','bien qu\'il <b>fasse</b>']],
       say:"bien que ce soit, bien qu'il ait, bien qu'elle puisse",
       note:"Les mêmes cinq verbes reviennent sans cesse. Apprenez ces formes-là, le reste suivra."},

      {t:'ana', h:"« même si » demande l'indicatif",
       p:"Jamais de subjonctif après « même si ». Jamais.",
       mots:[['Présent','même si je <b>trouve</b> son ton fort'],
             ['Imparfait','même si le local <b>était</b> plus petit'],
             ['Passé composé','même si la Ville <b>a consulté</b> le comité',true],
             ['Ce que ça ajoute','une nuance d\'hypothèse : « admettons que »']],
       say:"Même si je trouve son ton un peu fort, elle a raison.",
       note:"C'est la construction la plus sûre pour un élève : si vous hésitez sur le subjonctif, employez « même si »."},

      {t:'ana', h:"Les autres marqueurs",
       p:"Quatre de plus, tous très courants.",
       mots:[['malgré + nom','malgré le retard · malgré son ton'],
             ['pourtant','C\'est un bon projet. Pourtant, personne n\'est content.'],
             ['quand même','Le local est petit ; il fera quand même l\'affaire.'],
             ['par contre','L\'idée est bonne. Par contre, la date est mauvaise.',true]],
       note:"<b>Malgré</b> est suivi d'un <b>nom</b>, jamais d'une phrase. <i>❌ malgré qu'il soit tard</i> — dites <i>bien qu'il soit tard</i>."},

      {t:'texte', h:"L'ordre décide de ce qu'on retient",
       p:"Mettez la concession en premier et l'objection en second : <i>« Bien que ce soit une bonne idée, la consultation a manqué. »</i> Le lecteur retient la consultation. Inversez, et il retient la bonne idée. Rien n'a changé dans les faits, tout a changé dans l'effet.",
       note:"C'est le premier outil de celui qui écrit un commentaire ou un billet. Décidez ce que vous voulez qu'on retienne, et mettez-le en deuxième."},

      {t:'ex', h:"Six concessions à réutiliser",
       p:"Prêtes à recopier dans votre billet.",
       rows:[
         ["Bien que le projet soit utile, …","reconnaître l'utilité, objecter sur autre chose"],
         ["Bien qu'il ait consulté le comité, …","reconnaître la démarche, objecter sur l'étendue"],
         ["Même si je comprends son point de vue, …","reconnaître l'autre, garder le sien"],
         ["Même si les chiffres sont exacts, …","reconnaître les faits, contester la conclusion"],
         ["Malgré une bonne intention, …","concession courte, avec un nom"],
         ["C'est un bon projet. Par contre, …","deux phrases, plus simple à écrire"],
       ]},

      {t:'piege', h:"Trois pièges",
       rows:[
         ["bien que + indicatif","bien que + subjonctif",
          "<i>❌ Bien que c'est une bonne idée…</i> → <i>✅ Bien que <b>ce soit</b> une bonne idée…</i> C'est l'erreur numéro un."],
         ["même si + subjonctif","même si + indicatif",
          "<i>❌ Même si ce soit tard…</i> → <i>✅ Même si <b>c'est</b> tard…</i> Les deux marqueurs se ressemblent et ne se conduisent pas pareil."},
         ["malgré que","bien que",
          "<i>malgré que</i> s'entend, mais reste critiqué à l'écrit. Dans un texte que vous signez, écrivez <b>bien que</b>."],
       ]},

      {t:'check', h:"Est-ce que c'est clair maintenant ?",
       p:"Quatre questions rapides.",
       qs:[
         {q:"« Bien que le projet ___ utile »", opts:["est","soit"], ok:1,
          fb:"« Bien que » demande le subjonctif, toujours."},
         {q:"« Même si je ___ son ton fort »", opts:["trouve","trouve au subjonctif"], ok:0,
          fb:"« Même si » demande l'indicatif : je trouve."},
         {q:"« Malgré » est suivi…", opts:["d'un nom","d'une phrase"], ok:0,
          fb:"Malgré le retard, malgré son ton. Pas « malgré qu'il »."},
         {q:"Ce que le lecteur retient, c'est…", opts:["la première moitié","la seconde moitié"], ok:1,
          fb:"D'où l'ordre : concession d'abord, objection ensuite."},
       ]},

      {t:'revoir', h:"À retenir",
       p:"<b>Bien que</b> + subjonctif · <b>Même si</b> + indicatif · <b>Malgré</b> + nom. Et l'ordre qui convainc : on accorde d'abord, on objecte ensuite."},
    ]
  },

  t3clivage: {
    eye:'Mini-leçon', tit:"Mettre en relief : c'est… qui, c'est… que",
    blocs:[
      {t:'texte', h:"Insister sans élever la voix",
       p:"En français, on ne peut pas insister sur un mot en le disant plus fort, comme dans beaucoup de langues. Il faut le <b>déplacer</b> et l'<b>encadrer</b>. <i>« Farida devrait l'écrire »</i> devient <i>« <b>C'est</b> Farida <b>qui</b> devrait l'écrire »</i> : le nom passe en tête, encadré, et il devient le cœur de la phrase.",
       note:"On appelle ça le <b>clivage</b> : la phrase est fendue en deux pour loger l'élément important à l'avant."},

      {t:'ana', h:"Encadrer le sujet : c'est… qui",
       p:"Quand l'élément mis en avant est celui qui fait l'action.",
       mots:[['La forme','c\'est … qui + verbe'],
             ['Un exemple','C\'est le comité <b>qui</b> a retenu Boisjoli.'],
             ['L\'accord surprend','c\'est <b>moi qui suis</b> · c\'est <b>vous qui avez</b>',true]],
       say:"C'est le comité qui a retenu Boisjoli.",
       note:"Après « qui », le verbe s'accorde avec l'élément encadré, pas avec « c'est ». <i>C'est vous qui <b>devriez</b> poser la question.</i>"},

      {t:'ana', h:"Encadrer tout le reste : c'est… que",
       p:"Un lieu, un moment, un complément : tout passe par « que ».",
       mots:[['Un moment','C\'est le 14 octobre <b>qu\'</b>on décide.'],
             ['Un lieu','C\'est rue Boisjoli <b>que</b> le dépôt ouvrira.'],
             ['Un complément','C\'est cette question-là <b>que</b> je pose.'],
             ['Un point de vue','C\'est sur ce point <b>qu\'</b>elle a raison.',true]],
       say:"C'est le 14 octobre qu'on décide.",
       note:"Le repère est simple : <b>qui</b> si ce qui suit manque d'un sujet, <b>que</b> dans tous les autres cas."},

      {t:'ana', h:"Encadrer une idée entière : ce qui… c'est",
       p:"Pour mettre en avant non pas un mot, mais toute une chose.",
       mots:[['Sujet','<b>Ce qui</b> m\'inquiète, <b>c\'est</b> les heures d\'ouverture.'],
             ['Complément','<b>Ce que</b> je demande, <b>c\'est</b> une réponse claire.'],
             ['Manque','<b>Ce qui</b> manque, <b>ce n\'est pas</b> une opinion de plus.',true]],
       say:"Ce qui manque, ce n'est pas une opinion de plus.",
       note:"C'est la tournure la plus utile pour ouvrir un billet de blogue : elle annonce d'emblée de quoi vous allez parler."},

      {t:'labo', h:"La phrase plate et la phrase en relief",
       p:"Choisissez une phrase et la version que vous voulez entendre.",
       axes:[
         {id:'p', lbl:'Quelle phrase ?', opts:[['a','le comité'],['b','la date'],['c','les heures']]},
         {id:'v', lbl:'Quelle version ?', opts:[['1','sans relief'],['2','avec relief']]}],
       out:{
         a1:{w:["Le comité a retenu Boisjoli."], say:"Le comité a retenu Boisjoli.", n:'phrase ordinaire'},
         a2:{w:["C'est le comité qui a retenu Boisjoli."], say:"C'est le comité qui a retenu Boisjoli.", n:'le sujet est encadré : c\'est… qui'},
         b1:{w:["Le conseil décide le 14 octobre."], say:"Le conseil décide le 14 octobre.", n:'phrase ordinaire'},
         b2:{w:["C'est le 14 octobre que le conseil décide."], say:"C'est le 14 octobre que le conseil décide.", n:'un moment encadré : c\'est… que'},
         c1:{w:["Les heures d'ouverture m'inquiètent."], say:"Les heures d'ouverture m'inquiètent.", n:'phrase ordinaire'},
         c2:{w:["Ce qui m'inquiète, c'est les heures d'ouverture."], say:"Ce qui m'inquiète, c'est les heures d'ouverture.", n:'toute l\'idée est encadrée'},
       },
       note:"Écoutez les deux : la seconde n'est pas plus longue pour rien, elle dirige votre attention."},

      {t:'piege', h:"Trois pièges",
       rows:[
         ["choisir « que » à la place de « qui »","tester le sujet",
          "<i>❌ C'est le comité que a retenu…</i> Après le blanc, « a retenu » n'a pas de sujet : il faut <b>qui</b>."],
         ["oublier l'accord après « qui »","le verbe suit l'élément encadré",
          "<i>❌ C'est moi qui est venue.</i> → <i>✅ C'est moi qui <b>suis</b> venue.</i>"},
         ["en mettre partout","un par paragraphe",
          "La mise en relief perd tout effet si chaque phrase en porte une. Réservez-la à ce qui compte vraiment."},
       ]},

      {t:'check', h:"Est-ce que c'est clair maintenant ?",
       p:"Quatre questions rapides.",
       qs:[
         {q:"« C'est le comité ___ a retenu le local. »", opts:["qui","que"], ok:0,
          fb:"« a retenu » a besoin d'un sujet : qui."},
         {q:"« C'est le 14 octobre ___ on décide. »", opts:["qui","qu'"], ok:1,
          fb:"Un moment : c'est… que."},
         {q:"« C'est vous qui ___ raison. »", opts:["a","avez"], ok:1,
          fb:"Le verbe s'accorde avec « vous »."},
         {q:"Pour mettre en avant une idée entière, on emploie…", opts:["c'est… qui","ce qui… c'est"], ok:1,
          fb:"« Ce qui manque, c'est… »"},
       ]},
    ]
  },

  t3nuance: {
    eye:'Mini-leçon', tit:"Restreindre, reformuler, conclure",
    blocs:[
      {t:'texte', h:"Trois outils pour être précis sans être long",
       p:"Quand on écrit un commentaire ou un billet, la place manque. Trois procédés permettent de dire beaucoup en peu de mots : restreindre (<b>ne… que</b>), reformuler (<b>autrement dit</b>) et conclure (<b>par conséquent</b>). Ils sont au programme du niveau 7 et ils reviennent dans tous les textes d'opinion.",
       note:"Ce sont aussi trois façons de montrer qu'on maîtrise la langue : ils sont rares chez les débutants."},

      {t:'ana', h:"ne… que : « seulement », et ce n'est pas une négation",
       p:"Deux morceaux qui encadrent le verbe, comme « ne… pas », mais avec un sens tout différent.",
       mots:[['La forme','ne + verbe + que + l\'élément restreint'],
             ['Un exemple','Le dépôt <b>n\'</b>ouvrira <b>qu\'</b>au printemps.'],
             ['Le sens','il ouvrira — mais pas avant le printemps',true],
             ['À comparer','Il <b>ne</b> répond <b>pas</b>. (rien) · Il <b>ne</b> répond <b>qu\'</b>aux courriels. (à ça seulement)']],
       say:"Le dépôt n'ouvrira qu'au printemps.",
       note:"« Que » se place juste devant ce qu'on restreint. Déplacez-le, et le sens change : <i>Je ne lis que le samedi</i> ≠ <i>Je ne lis le journal que le samedi</i>."},

      {t:'ana', h:"Reformuler : traduire ce qu'on vient de dire",
       p:"On vient d'écrire quelque chose de technique ou d'abstrait, et on le redit simplement.",
       mots:[['autrement dit','le plus courant, à l\'oral comme à l\'écrit'],
             ['c\'est-à-dire','sert aussi à définir un mot au passage'],
             ['en d\'autres termes','plus soutenu'],
             ['en somme','résume plusieurs phrases d\'un coup',true]],
       note:"Écrire « autrement dit » vous oblige à formuler deux fois la même idée. C'est un excellent exercice : si la seconde version ne vient pas, c'est que la première n'était pas claire."},

      {t:'ana', h:"Conclure : tirer une conséquence",
       p:"Attention, ce n'est pas la même chose que résumer.",
       mots:[['donc','courant, neutre, s\'emploie partout'],
             ['par conséquent','plus formel, à l\'écrit'],
             ['c\'est pourquoi','met la cause en avant'],
             ['La différence','<b>en somme</b> résume · <b>par conséquent</b> ajoute une conséquence',true]],
       note:"<i>« Le local est plus grand, par conséquent le comité l'a retenu. »</i> Il y a bien une conséquence. <i>« Par conséquent, merci de votre attention »</i> n'en a aucune : c'est la faute à éviter."},

      {t:'ex', h:"Six formules à réutiliser dans votre billet",
       p:"À gauche la formule, à droite ce qu'elle fait.",
       rows:[
         ["Le dépôt n'ouvrira qu'au printemps.","restreint : il ouvrira, mais pas avant"],
         ["La Ville ne fournit que le local.","restreint : elle fournit ça, rien d'autre"],
         ["Autrement dit, il faut un endroit où aller.","reformule plus simplement"],
         ["En somme : un bon projet, une question sans réponse.","résume tout"],
         ["Par conséquent, le comité l'a retenu.","tire une conséquence"],
         ["C'est pourquoi je pose la question.","met la cause en avant"],
       ]},

      {t:'piege', h:"Trois pièges",
       rows:[
         ["lire « ne… que » comme une négation","c'est « seulement »",
          "<i>Il n'a répondu qu'à deux questions</i> ne veut pas dire qu'il n'a pas répondu. Il a répondu à deux."},
         ["placer « que » n'importe où","juste devant l'élément restreint",
          "<i>Je ne lis <b>que</b> le journal le samedi</i> (rien d'autre que le journal) ≠ <i>Je ne lis le journal <b>que</b> le samedi</i> (aucun autre jour)."},
         ["conclure sans conséquence","garder « en somme » pour résumer",
          "« Par conséquent » annonce un effet. S'il n'y en a pas, employez « en somme » ou ne mettez rien."},
       ]},

      {t:'check', h:"Est-ce que c'est clair maintenant ?",
       p:"Quatre questions rapides.",
       qs:[
         {q:"« Il ne répond qu'aux courriels » veut dire…", opts:["il ne répond pas","il répond aux courriels seulement"], ok:1,
          fb:"« ne… que » signifie « seulement »."},
         {q:"Pour redire une idée plus simplement, on emploie…", opts:["autrement dit","par conséquent"], ok:0,
          fb:"« Par conséquent » tire une conséquence."},
         {q:"« En somme » sert à…", opts:["résumer","conclure sur un effet"], ok:0,
          fb:"Résumer. Pour l'effet, c'est « par conséquent »."},
         {q:"Où se place « que » dans « ne… que » ?", opts:["devant le verbe","devant ce qu'on restreint"], ok:1,
          fb:"Sa place change le sens de la phrase."},
       ]},
    ]
  },

};
