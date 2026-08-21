const PLUS = {

  // ════════════════════════════════════════════════════════════════════════
  prPhon: {
    eye:'Mini-leçon', tit:"Le son de « in » et le son de « on »",
    blocs:[
      {t:'texte', h:"Deux voyelles du nez, et presque tous les mots de la nouvelle",
       p:"Ouvrez n'importe quel fait divers et comptez : un incendie, un témoin, un voisin, le matin, la fin, une plainte, important d'un côté ; une inondation, un cabanon, la prévention, une déclaration, un soupçon, le nombre de l'autre. Ces deux sons portent la moitié du vocabulaire du module. Ils se ressemblent parce que l'air passe par le nez dans les deux cas — mais la bouche ne fait pas du tout la même chose, et c'est là-dessus qu'on s'appuie.",
       note:"Les confondre ne fait pas seulement une faute de prononciation : « un bain » devient « un bon », « la fin » devient « le fond », et la personne en face vous fait répéter au milieu de votre récit."},

      {t:'ana', h:"Le son de « in » : les lèvres étirées, plates",
       p:"Les coins de la bouche partent sur les côtés, comme au début d'un sourire. La langue reste en avant, l'air sort par le nez. Quatre orthographes, un seul son : in, ain, ein, im.",
       mots:[["Dans le sinistre","un incendie · éteindre · la fin"],["Dans les gens","un témoin · un voisin · un copain",true],["Dans le temps","le matin · demain · un an et demi"]],
       say:"Un incendie. Un témoin. Le matin.",
       note:"« Incendie » est le mot le plus utile de la liste : il commence par le son de « in » et il finit par un « i » ordinaire. Dites-le en trois temps — in-cen-die — avant de le dire vite."},

      {t:'ana', h:"Le son de « on » : les lèvres en petit rond",
       p:"Les lèvres se ferment en rond, comme pour siffler ; la langue recule ; l'air sort encore par le nez. Deux orthographes seulement : on et om.",
       mots:[["Dans les mots longs","une inondation · la prévention · une déclaration"],["Dans les lieux","un cabanon · une maison · un balcon",true],["Dans les mots courts","le nombre · un soupçon · ils sont"]],
       say:"Une inondation. Un cabanon. La prévention.",
       note:"Les mots en -tion sont tous là : déclaration, inondation, prévention, information, question. Un seul geste des lèvres, et six mots du module tombent d'un coup."},

      {t:'ana', h:"Le geste qui règle tout, et qui se voit",
       p:"Mettez la main à deux centimètres devant la bouche. Sur « in », la main sent une fente large et plate. Sur « on », un petit rond serré. Ce n'est pas une image : c'est physiquement la seule différence entre les deux sons.",
       mots:[["Les paires à sentir","fin / fond · main / mon · bain / bon"],["Les paires du module","un témoin / un cabanon · la fin / le fond",true],["La phrase à deux sons","un incendie important dans une maison"]],
       say:"Fin, fond. Main, mon. Bain, bon.",
       note:"Regardez les lèvres de la personne qui parle quand vous le pouvez. Une bonne moitié de l'écoute passe par les yeux, et personne ne vous le dit jamais."},

      {t:'labo', h:"Écoutez la paire, puis le mot dans sa phrase",
       p:"Choisissez une paire et écoutez la différence, puis le mot replacé dans une phrase du journal.",
       axes:[{id:'p', lbl:'Quelle paire ?', opts:[
         ['a','fin / fond'],
         ['b','main / mon'],
         ['c','bain / bon'],
         ['d','un témoin / un cabanon'],
         ['e','les quatre à la suite']]}],
       out:{
         a:{w:['un incendie'], say:"Fin. Fond. La fin de l'incendie, au fond de la rue.", n:"« in » lèvres plates, « on » lèvres rondes"},
         b:{w:['un témoin'], say:"Main. Mon. Le témoin a levé la main devant mon garage.", n:"la même consonne, deux voyelles du nez"},
         c:{w:['un cabanon'], say:"Bain. Bon. Le cabanon est en bon état.", n:"écoutez la voyelle, pas la consonne"},
         d:{w:['un témoin','un cabanon'], say:"Un témoin. Un cabanon. Un témoin a vu quelqu'un sortir du cabanon.", n:"la paire qui revient dans tout le défi 3"},
         e:{w:['un incendie','un cabanon'], say:"Fin, fond. Main, mon. Bain, bon. Témoin, cabanon.", n:"quatre paires à la suite, sans reprendre son souffle"},
       },
       note:"Écoutez chaque paire deux fois : la première pour entendre les deux mots, la seconde en ne guettant que la position de vos propres lèvres."},

      {t:'ex', h:"À écouter et à répéter",
       p:"Six phrases prises dans les faits divers du module.",
       rows:[
         ["Un incendie a détruit un immeuble de la rue Alexandre.","« in » au début, puis rien d'autre"],
         ["L'inondation a touché une dizaine de maisons.","« on » trois fois de suite"],
         ["Un témoin a vu quelqu'un sortir du cabanon.","« in », puis « on » : la paire du module"],
         ["La déclaration du porte-parole est dans le journal.","« on » deux fois, sans forcer"],
         ["Le voisin a donné son numéro à la police.","« in », puis « on » dans la même phrase"],
         ["La prévention commence par une porte barrée.","« on » deux fois au début"],
       ]},

      {t:'piege', h:"Trois pièges des voyelles du nez",
       rows:[
         ["prononcer le « n » ou le « m » qui suit","« incendi-enne », avec un n bien détaché",
          "Dans une voyelle du nez, la lettre n ne se prononce pas : elle indique seulement que l'air passe par le nez. La langue ne touche rien. Le n s'entend seulement quand une voyelle suit : « un incendie » se dit « un-n-incendie »."],
         ["ouvrir les lèvres sur « on »","« un cabanan » au lieu de « un cabanon »",
          "Les lèvres doivent se fermer en rond. Si elles restent larges, le mot change de famille et n'existe plus. Exercez-vous devant une vitre : le rond doit être visible de l'extérieur."],
         ["croire que l'orthographe décide","« ain » et « ein » lus comme deux sons différents",
          "in, ain, ein, im donnent tous le même son : incendie, main, plein, important. Ne cherchez pas quatre prononciations là où il n'y en a qu'une — c'est l'oreille qui commande, pas l'écriture."],
       ]},

      {t:'check', h:"Est-ce que c'est clair maintenant ?",
       p:"Quatre questions rapides.",
       qs:[
         {q:"Dans « un cabanon », les lèvres…", opts:["s'étirent sur les côtés","se ferment en petit rond"], ok:1,
          fb:"Elles se ferment en rond. C'est le geste du son de « on »."},
         {q:"« Plein » contient le son…", opts:["de « in »","de « on »"], ok:0,
          fb:"Celui de « in ». Le « ein » se dit comme le « in » de « fin »."},
         {q:"Dans « incendie », le n du début…", opts:["se prononce","ne se prononce pas"], ok:1,
          fb:"Il ne se prononce pas : il indique seulement que l'air passe par le nez."},
         {q:"Les mots en -tion contiennent…", opts:["le son de « on »","le son de « in »"], ok:0,
          fb:"Celui de « on » : déclaration, inondation, prévention, question."},
       ]},
    ]
  },

  // ════════════════════════════════════════════════════════════════════════
  prMot: {
    eye:'Mini-leçon', tit:"Le sinistre, le délit, et ce qui vient après",
    blocs:[
      {t:'texte', h:"Deux familles, et on ne les mélange pas",
       p:"Tous les faits divers du monde se rangent dans deux boîtes. Dans la première, ce qui arrive sans que personne l'ait voulu : un incendie, une inondation, une tempête, un accident. Dans la seconde, ce que quelqu'un a fait : un vol, une entrée par effraction, un méfait. Le vocabulaire n'est pas le même, les gens qui parlent ne sont pas les mêmes, et la fin de l'article n'est pas la même non plus.",
       note:"Savoir dans quelle boîte on est vous donne d'avance la moitié des mots de l'article : si c'est un sinistre, on parlera de sinistrés et de Croix-Rouge ; si c'est un délit, on parlera de suspect et de plainte."},

      {t:'ana', h:"La famille du sinistre",
       p:"Personne n'est responsable, ou pas encore. Les gens touchés ne sont pas des victimes d'un crime : ce sont des sinistrés. On les héberge, on les habille, on les reloge.",
       mots:[["Ce qui arrive","un incendie · une inondation · une tempête"],["Les gens touchés","un sinistré · un résident · un locataire",true],["Ceux qui viennent","les pompiers · la Croix-Rouge · la Ville"]],
       say:"Un incendie. Une inondation. Un sinistré.",
       note:"Au Québec, c'est la Croix-Rouge canadienne qui héberge et qui habille les sinistrés, à la demande de la municipalité. C'est pourquoi son nom revient à la fin de presque tous les articles d'incendie."},

      {t:'ana', h:"La famille du délit",
       p:"Quelqu'un a agi. La police cherche, et le journal fait attention à ses mots : tant qu'un tribunal n'a rien dit, on écrit « présumé ».",
       mots:[["Ce qui est fait","un vol · une entrée par effraction · un méfait"],["Qui on cherche","un suspect · un voleur présumé",true],["Ce qu'on fait","porter plainte · signaler · noter le numéro"]],
       say:"Un vol. Un suspect. La prévention.",
       note:"Un suspect n'est pas un coupable, et un journal sérieux ne les confond jamais. Quand vous racontez la nouvelle, gardez la même prudence : « la police cherche un suspect », pas « ils ont trouvé le voleur »."},

      {t:'ana', h:"Ce qui vient après, dans les deux cas",
       p:"Une enquête commence toujours : après un feu, pour trouver d'où il est parti ; après un vol, pour trouver qui est entré. Elle prend du temps, et l'article se termine presque toujours par la même phrase.",
       mots:[["Le travail","une enquête · un enquêteur · une cause",true],["Ceux qui parlent","un témoin · un porte-parole · une déclaration"],["Ce qui prévient","un avertissement · la prévention"]],
       say:"Une enquête. Un enquêteur. Une déclaration.",
       note:"« L'enquête se poursuit » veut dire qu'on ne sait pas encore. Ce n'est pas une formule vide : c'est la façon polie de dire que tout ce qui a été raconté avant reste à confirmer."},

      {t:'labo', h:"Un mot, sa phrase, et la famille où il vit",
       p:"Choisissez un mot et écoutez-le dans une phrase du journal.",
       axes:[{id:'m', lbl:'Quel mot ?', opts:[
         ['a','un fait divers'],
         ['b','le chapeau'],
         ['c','un sinistré'],
         ['d','une enquête'],
         ['e','un avertissement']]}],
       out:{
         a:{w:['un fait divers'], say:"Elle lit les faits divers avant tout le reste du journal.", n:"le genre d'article, pas son contenu"},
         b:{w:['le chapeau'], say:"Lis le chapeau : tu sauras la nouvelle en deux lignes.", n:"les lignes en gras sous le titre"},
         c:{w:['un sinistré'], say:"Onze sinistrés ont été hébergés par la Croix-Rouge.", n:"la famille du sinistre"},
         d:{w:['une enquête','un enquêteur'], say:"L'enquête dira si le feu est parti de la cuisine.", n:"ce qui vient après, dans les deux familles"},
         e:{w:['un avertissement'], say:"Un avertissement de pluie abondante avait été émis la veille.", n:"ce qui prévient, avant que ça arrive"},
       },
       note:"Écoutez chaque mot deux fois : une fois seul, une fois dans sa phrase. C'est la phrase qui fixe le mot dans la mémoire, pas le mot tout seul."},

      {t:'ex', h:"À écouter et à répéter",
       p:"Six phrases, trois de chaque famille.",
       rows:[
         ["Un incendie a détruit quatre logements de la rue Alexandre.","le sinistre, en une phrase"],
         ["Onze sinistrés ont été hébergés par la Croix-Rouge.","ce qui reste, à la fin"],
         ["Un avertissement de pluie abondante avait été émis la veille.","ce qui prévenait, avant"],
         ["Une trentaine de vélos ont été volés dans le quartier.","le délit, en chiffres"],
         ["Aucun suspect n'a été arrêté pour l'instant.","la prudence du journal"],
         ["L'enquête se poursuit et rien n'est confirmé.","la phrase de la fin"],
       ]},

      {t:'piege', h:"Trois confusions de mots à éviter",
       rows:[
         ["dire « victime » pour un sinistré","« les victimes de l'incendie ont été hébergées »",
          "On parle de victimes quand quelqu'un a fait du tort à quelqu'un. Dans un incendie accidentel, ce sont des sinistrés. Le mot « victime » ajoute un coupable qui n'existe peut-être pas."],
         ["dire « voleur » avant le tribunal","« la police a arrêté le voleur »",
          "Tant que rien n'est jugé, c'est un suspect, ou un voleur présumé. Un journal qui écrit autrement se fait poursuivre. Reprenez la même prudence quand vous racontez."],
         ["confondre enquête et jugement","« l'enquête a décidé que c'était la friteuse »",
          "Une enquête cherche ; elle ne décide pas. Elle conclut, elle établit une cause probable. C'est pourquoi le journal écrit « le feu serait parti de la cuisine » — au conditionnel, tant que ce n'est pas certain."],
       ]},

      {t:'check', h:"Est-ce que c'est clair maintenant ?",
       p:"Quatre questions rapides.",
       qs:[
         {q:"Les gens qui perdent leur logement dans un feu sont…", opts:["des sinistrés","des victimes"], ok:0,
          fb:"Des sinistrés. « Victime » suppose que quelqu'un leur a fait du tort."},
         {q:"Tant que rien n'est prouvé, la police cherche…", opts:["un voleur","un suspect"], ok:1,
          fb:"Un suspect. Le journal écrit même « un voleur présumé »."},
         {q:"« L'enquête se poursuit » veut dire…", opts:["qu'on ne sait pas encore","que le dossier est fermé"], ok:0,
          fb:"Qu'on ne sait pas encore. C'est la phrase qui termine presque tous les faits divers."},
         {q:"Un avertissement d'Environnement Canada arrive…", opts:["après l'évènement","avant l'évènement"], ok:1,
          fb:"Avant. C'est ce qui le distingue du reste de l'article."},
       ]},
    ]
  },

  // ════════════════════════════════════════════════════════════════════════
  t1pc: {
    eye:'Mini-leçon', tit:"Le passé composé, ou ce qui est arrivé",
    blocs:[
      {t:'texte', h:"Deux morceaux, et le sens est dans le deuxième",
       p:"Le passé composé porte bien son nom : il est composé de deux morceaux. D'abord un verbe conjugué au présent — avoir ou être —, ensuite le participe passé, qui porte le sens. « Le feu a détruit l'immeuble » : « a » ne veut rien dire tout seul, « détruit » dit tout. C'est la construction qui raconte les évènements d'un fait divers, du premier au dernier paragraphe.",
       note:"Quand un francophone vous corrige, c'est presque toujours sur le premier morceau — le mauvais auxiliaire — ou sur l'accord du second. Le participe lui-même, vous l'avez déjà."},

      {t:'ana', h:"La grande majorité prend « avoir »",
       p:"Détruire, brûler, commencer, appeler, voir, entendre, perdre, dire, demander, distribuer, héberger, voler, signaler. Avec avoir, le participe ne change pas quand le complément vient après le verbe.",
       mots:[["Le feu et ses suites","le feu a éclaté · il a détruit · il a brûlé",true],["Les gens","il a cogné · elle a perdu · ils ont appelé"],["Les services","la Ville a distribué · la Croix-Rouge a hébergé"]],
       say:"Le feu a éclaté. Il a détruit l'immeuble. La Croix-Rouge a hébergé les sinistrés.",
       note:"« Le feu a éclaté » et « le feu s'est déclaré » veulent dire la même chose. Le second se lit plus souvent dans le journal ; le premier se dit plus souvent à table."},

      {t:'ana', h:"Une petite liste prend « être »",
       p:"Aller, venir, arriver, partir, entrer, sortir, monter, descendre, rester, tomber, naître, mourir, passer — et tous les verbes qui commencent par « se ». Ici, le participe s'accorde avec le sujet : un s au pluriel, un e au féminin.",
       mots:[["Les secours","les pompiers sont arrivés · ils sont entrés"],["Les gens","une résidente est sortie · il s'est réveillé",true],["L'eau et le feu","l'eau est montée · la rivière est sortie de son lit"]],
       say:"Les pompiers sont arrivés. Une résidente est sortie. Il s'est réveillé.",
       note:"Le test rapide : si le verbe dit un déplacement ou un changement d'état, essayez « être ». Ce n'est pas une règle parfaite, mais elle attrape onze des treize verbes de la liste."},

      {t:'ana', h:"Les participes qu'un fait divers emploie tous les jours",
       p:"Apprenez-les comme des mots de vocabulaire, pas comme des règles. Ce sont eux que vous lirez chaque semaine et que vous direz chaque fois que vous raconterez.",
       mots:[["Le sinistre","détruit · brûlé · éclaté · évacué · inondé",true],["L'intervention","appelé · signalé · hébergé · pompé · fermé"],["Le délit","volé · retrouvé · arrêté · perdu · disparu"]],
       say:"Détruit. Évacué. Volé. Retrouvé.",
       note:"Six de ces participes sont irréguliers : détruit, perdu, disparu, arrêté est régulier, mais « il a dû », « il a pu », « il a fallu » vous attendent au tournant. Notez-les à mesure, dans votre liste de mots."},

      {t:'labo', h:"La même phrase, avec les deux auxiliaires",
       p:"Choisissez un verbe et écoutez la phrase complète, avec l'auxiliaire qui lui convient.",
       axes:[{id:'v', lbl:'Quel verbe ?', opts:[
         ['a','éclater — le feu'],
         ['b','arriver — les pompiers'],
         ['c','se réveiller — un locataire'],
         ['d','héberger — la Croix-Rouge'],
         ['e','les quatre à la suite']]}],
       out:{
         a:{w:['un incendie'], say:"Le feu a éclaté vers quatre heures du matin.", n:"avoir · le participe ne bouge pas"},
         b:{w:['évacuer'], say:"Les pompiers sont arrivés huit minutes après l'appel.", n:"être · un s, parce que « les pompiers »"},
         c:{w:['évacuer'], say:"Un locataire s'est réveillé et il a cogné à toutes les portes.", n:"être avec « se », puis avoir"},
         d:{w:['un sinistré'], say:"La Croix-Rouge a hébergé les onze sinistrés.", n:"avoir · le complément suit, pas d'accord"},
         e:{w:['un incendie','un sinistré'], say:"Le feu a éclaté. Un locataire s'est réveillé. Les pompiers sont arrivés. La Croix-Rouge a hébergé les sinistrés.", n:"le récit complet, en quatre évènements"},
       },
       note:"Écoutez la dernière option en entier : c'est exactement ce que vous aurez à dire au jeu de rôle, et ça tient en quinze secondes."},

      {t:'ex', h:"À écouter et à répéter",
       p:"Six phrases, dans l'ordre du récit.",
       rows:[
         ["Le feu a éclaté vers quatre heures du matin.","avoir · l'évènement de départ"],
         ["Un locataire s'est réveillé et a cogné à toutes les portes.","être · verbe en « se »"],
         ["Les pompiers sont arrivés huit minutes après l'appel.","être · accord au pluriel"],
         ["Personne n'a été blessé.","la négation autour de l'auxiliaire"],
         ["Onze personnes ont perdu leur logement.","avoir · participe irrégulier"],
         ["La Croix-Rouge les a hébergées pour la nuit.","le pronom devant, l'accord derrière"],
       ]},

      {t:'piege', h:"Trois pièges du passé composé",
       rows:[
         ["mettre « avoir » avec les verbes de déplacement","« il a arrivé », « elle a sorti de la maison »",
          "Arriver, partir, entrer, sortir, monter, descendre, rester, tomber prennent être : il est arrivé, elle est sortie. Un francophone l'entend immédiatement, et c'est la correction la plus fréquente au niveau 5."],
         ["oublier l'accord avec « être »","« les pompiers sont arrivé »",
          "Avec être, le participe s'accorde avec le sujet, comme un adjectif : arrivé, arrivée, arrivés, arrivées. Ça ne s'entend presque pas, mais ça se voit dans le courriel de « Je me lance »."],
         ["placer la négation autour du participe","« il a ne pas été blessé »",
          "Le ne et le pas entourent le premier morceau : « il n'a pas été blessé », « la Ville n'a pas voulu dire quand ». Le participe reste collé derrière, toujours."],
       ]},

      {t:'check', h:"Est-ce que c'est clair maintenant ?",
       p:"Quatre questions rapides.",
       qs:[
         {q:"« Les pompiers ___ arrivés » se complète par…", opts:["ont","sont"], ok:1,
          fb:"Sont. Arriver est un verbe de déplacement : il prend être."},
         {q:"Avec « avoir », le participe s'accorde avec le sujet ?", opts:["oui, toujours","non, pas quand le complément suit"], ok:1,
          fb:"Non. « La Croix-Rouge a hébergé les sinistrés » — aucun accord."},
         {q:"La négation se place…", opts:["autour de l'auxiliaire","autour du participe"], ok:0,
          fb:"Autour de l'auxiliaire : « il n'a pas été blessé »."},
         {q:"Tous les verbes en « se » prennent…", opts:["avoir","être"], ok:1,
          fb:"Être : il s'est réveillé, elle s'est levée, ils se sont sauvés."},
       ]},
    ]
  },

  // ════════════════════════════════════════════════════════════════════════
  t1imp: {
    eye:'Mini-leçon', tit:"L'imparfait, ou le décor autour de l'évènement",
    blocs:[
      {t:'texte', h:"Le temps le plus régulier du français",
       p:"L'imparfait n'a qu'une série de terminaisons — ais, ais, ait, ions, iez, aient — et elles valent pour tous les verbes de la langue, sans exception. On les colle au radical du « nous » du présent : nous dormons donne il dormait, nous faisons donne il faisait, nous prenons donne elle prenait. Un seul verbe échappe à la règle, et c'est « être » : j'étais, tu étais, il était.",
       note:"C'est le temps le plus facile du français et le plus mal employé par les personnes qui l'apprennent — non pas parce que la forme est difficile, mais parce qu'on ne sait pas quand s'en servir."},

      {t:'ana', h:"Ce qu'on met à l'imparfait",
       p:"Tout ce qui était déjà là quand l'évènement est arrivé : l'heure, le temps qu'il faisait, ce que les gens faisaient, l'état des choses. Rien n'y commence, rien n'y finit.",
       mots:[["L'heure et le temps","il était quatre heures · il ventait · il pleuvait",true],["Ce que les gens faisaient","tout le monde dormait · elle lisait le journal"],["L'état des choses","l'immeuble avait quatre logements · la rue était déserte"]],
       say:"Il était quatre heures. Tout le monde dormait. La rue était déserte.",
       note:"Ces trois phrases-là ouvrent le deuxième paragraphe de presque tous les faits divers d'incendie. Elles ne racontent rien ; elles installent la scène pour que le reste se comprenne."},

      {t:'ana', h:"Les mots qui appellent l'imparfait",
       p:"Certains mots annoncent que la situation durait. Dès que vous les voyez ou que vous les employez, le verbe qui suit est presque toujours à l'imparfait.",
       mots:[["La durée","depuis trois jours · pendant que · encore",true],["L'habitude","chaque matin · tous les mardis · toujours"],["Le décor","il y avait · c'était · on voyait"]],
       say:"La rivière montait depuis trois jours. Chaque matin, elle lisait le journal.",
       note:"« Depuis » est le plus fiable des trois. « La rivière montait depuis trois jours » : impossible de mettre le passé composé là, la phrase ne veut plus rien dire."},

      {t:'ana', h:"La phrase à deux temps, celle qu'il faut savoir par cœur",
       p:"L'imparfait plante la toile de fond, le passé composé y accroche l'évènement. Les deux dans la même phrase, séparés par « quand » ou « pendant que ».",
       mots:[["Le feu","il dormait quand il a entendu l'alarme",true],["L'eau","l'eau montait déjà quand la Ville a distribué les sacs"],["Le vol","le cabanon était ouvert quand ils sont entrés"]],
       say:"Il dormait quand il a entendu l'alarme. L'eau montait déjà quand la Ville a distribué les sacs.",
       note:"Dites ces deux phrases à voix haute cinq fois. Cette structure-là revient dans chaque récit du module, dans chaque fait divers du journal, et dans à peu près toutes les histoires qu'on raconte à table."},

      {t:'labo', h:"Le décor, puis l'évènement",
       p:"Choisissez une scène et écoutez le décor à l'imparfait, suivi de l'évènement au passé composé.",
       axes:[{id:'s', lbl:'Quelle scène ?', opts:[
         ['a',"l'incendie de la rue Alexandre"],
         ['b',"l'inondation de la rue des Peupliers"],
         ['c','les vols de vélos du quartier'],
         ['d','les trois scènes à la suite']]}],
       out:{
         a:{w:['un incendie'], say:"Il était quatre heures et tout le monde dormait. Le feu a éclaté dans la cuisine du deuxième.", n:"deux imparfaits, puis un passé composé"},
         b:{w:['une inondation'], say:"La rivière montait depuis trois jours. Lundi, la Ville a distribué des sacs de sable.", n:"la durée, puis l'évènement daté"},
         c:{w:['un cabanon','un vol'], say:"Les portes des cabanons n'étaient pas barrées. En un mois, une trentaine de vélos ont disparu.", n:"l'état des choses, puis le bilan"},
         d:{w:['un incendie','une inondation','un vol'], say:"Il était quatre heures et tout le monde dormait. La rivière montait depuis trois jours. Les cabanons n'étaient pas barrés.", n:"trois décors, sans les évènements"},
       },
       note:"La dernière option ne donne que les décors. Écoutez-la : vous entendrez que rien ne se passe. C'est exactement ce que fait un récit tout à l'imparfait."},

      {t:'ex', h:"À écouter et à répéter",
       p:"Six phrases de décor, prises dans les trois nouvelles du module.",
       rows:[
         ["Il était quatre heures du matin.","le seul verbe irrégulier"],
         ["Tout le monde dormait dans l'immeuble.","radical du « nous » du présent"],
         ["La rivière montait depuis trois jours.","« depuis » appelle l'imparfait"],
         ["L'immeuble avait quatre logements.","l'état des choses"],
         ["Les portes des cabanons n'étaient pas barrées.","négation à l'imparfait"],
         ["Pendant que les pompiers travaillaient, la police fermait la rue.","deux imparfaits en même temps"],
       ]},

      {t:'piege', h:"Trois pièges de l'imparfait",
       rows:[
         ["raconter tout le fait divers à l'imparfait","« le feu éclatait, les pompiers arrivaient, ils éteignaient »",
          "L'imparfait ne fait pas avancer l'histoire : il la met en pause. Un récit entièrement à l'imparfait donne une scène figée où rien n'arrive jamais. Les évènements veulent le passé composé."],
         ["oublier le i de « nous » et « vous »","« nous travaillons » au lieu de « nous travaillions »",
          "Aux deux premières personnes du pluriel, l'imparfait ajoute un i : nous travaillions, vous travailliez. Ça ne s'entend presque pas dans certains verbes, mais ça se voit à l'écrit — et le courriel de « Je me lance » est à l'écrit."],
         ["mettre le passé composé après « depuis »","« la rivière est montée depuis trois jours »",
          "« Depuis » dit qu'une chose durait encore : imparfait. « La rivière montait depuis trois jours. » Le passé composé fermerait la durée, et « depuis » la garde ouverte : les deux se contredisent."],
       ]},

      {t:'check', h:"Est-ce que c'est clair maintenant ?",
       p:"Quatre questions rapides.",
       qs:[
         {q:"Combien de verbes sont irréguliers à l'imparfait ?", opts:["un seul, être","une trentaine"], ok:0,
          fb:"Un seul : être. Tous les autres suivent le radical du « nous » du présent."},
         {q:"« La rivière ___ depuis trois jours » se complète par…", opts:["est montée","montait"], ok:1,
          fb:"Montait. « Depuis » garde la durée ouverte : imparfait."},
         {q:"L'imparfait sert à…", opts:["faire avancer l'histoire","planter le décor"], ok:1,
          fb:"Planter le décor. Les évènements se disent au passé composé."},
         {q:"À la première personne du pluriel, on écrit…", opts:["nous travaillions","nous travaillons"], ok:0,
          fb:"Nous travaillions, avec un i : c'est la marque de l'imparfait."},
       ]},
    ]
  },

  // ════════════════════════════════════════════════════════════════════════
  t1tri: {
    eye:'Mini-leçon', tit:"Choisir entre les deux, phrase par phrase",
    blocs:[
      {t:'texte', h:"Ce n'est pas le verbe qui décide, c'est vous",
       p:"On enseigne souvent le passé composé et l'imparfait comme si certains verbes appartenaient à l'un et d'autres à l'autre. C'est faux, et c'est ce qui rend le choix difficile. Le même verbe va des deux côtés selon ce que vous voulez dire : « la police a fermé la rue à cinq heures » raconte un évènement ; « la rue était fermée toute la journée » décrit une situation. Deux vérités, deux phrases, un seul verbe.",
       note:"La bonne question n'est jamais « quel temps prend ce verbe ? ». Elle est « est-ce que je raconte ce qui est arrivé, ou est-ce que je décris ce qui était là ? »."},

      {t:'ana', h:"Premier test : est-ce que ça a un début et une fin ?",
       p:"Si l'action commence et se termine dans le récit, c'est un évènement : passé composé. Si la chose était simplement là, sans début visible, c'est le décor : imparfait.",
       mots:[["Un début et une fin","le feu a éclaté · les pompiers sont arrivés",true],["Ni début ni fin","il ventait · la rue était déserte"],["Le doute se lève au test","la rue a été fermée / la rue était fermée"]],
       say:"Le feu a éclaté. Il ventait. La rue a été fermée à cinq heures.",
       note:"Ce test échoue rarement. Quand il échoue, c'est que la phrase peut vraiment se dire des deux façons — et alors les deux sont correctes, elles disent seulement deux choses différentes."},

      {t:'ana', h:"Deuxième test : est-ce que je peux compter ?",
       p:"Si vous pouvez dire combien de fois, c'est un évènement. Si vous ne pouvez pas, la chose durait.",
       mots:[["On compte","il a cogné à quatre portes · elle a appelé deux fois"],["On ne compte pas","il pleuvait · elle lisait le journal",true],["L'habitude ne se compte pas","chaque mardi, elle lisait l'hebdomadaire"]],
       say:"Il a cogné à quatre portes. Il pleuvait depuis trois jours.",
       note:"Attention à l'habitude : « chaque mardi, elle lisait le journal » se répétait souvent, mais on ne compte pas les fois — c'est une habitude, donc l'imparfait."},

      {t:'ana', h:"Ce que le choix change pour la personne qui écoute",
       p:"Quelqu'un qui n'a rien lu a besoin des deux temps. Le décor lui permet de se représenter la scène ; les évènements lui permettent de suivre l'histoire. Enlevez l'un des deux, et le récit cesse de fonctionner.",
       mots:[["Tout au passé composé","une liste sèche, sans scène"],["Tout à l'imparfait","une photo où rien n'arrive",true],["Les deux","un récit qu'on peut suivre"]],
       say:"Il était quatre heures, tout le monde dormait, et le feu a éclaté dans la cuisine du deuxième.",
       note:"Écoutez cette phrase : deux imparfaits, un passé composé, et vous voyez la scène. C'est le modèle de la première phrase de votre récit au jeu de rôle."},

      {t:'labo', h:"La même information, dite des deux façons",
       p:"Choisissez une paire et écoutez la différence de sens.",
       axes:[{id:'p', lbl:'Quelle paire ?', opts:[
         ['a','la rue fermée'],
         ['b',"l'eau dans le sous-sol"],
         ['c','le journal du mardi'],
         ['d','les trois paires à la suite']]}],
       out:{
         a:{w:['un incendie'], say:"La police a fermé la rue à cinq heures. La rue était fermée toute la journée.", n:"l'évènement, puis la situation"},
         b:{w:['une inondation'], say:"L'eau est entrée dans le sous-sol vers minuit. L'eau montait déjà dans le sous-sol.", n:"un moment précis, puis une durée"},
         c:{w:['un hebdomadaire'], say:"Elle a lu le journal mardi matin. Chaque mardi, elle lisait le journal.", n:"une fois, puis une habitude"},
         d:{w:['un fait divers'], say:"La police a fermé la rue à cinq heures. La rue était fermée toute la journée. L'eau est entrée vers minuit. L'eau montait déjà.", n:"écoutez le glissement à chaque fois"},
       },
       note:"Aucune de ces phrases n'est fausse. Elles disent deux choses différentes, et c'est vous qui choisissez laquelle vous voulez dire."},

      {t:'ex', h:"À écouter et à répéter",
       p:"Six phrases où les deux temps se croisent.",
       rows:[
         ["Il dormait quand le feu a éclaté.","décor, puis évènement"],
         ["Pendant que les pompiers travaillaient, la police a fermé la rue.","durée, puis évènement"],
         ["La rivière montait depuis trois jours quand la Ville a réagi.","durée longue, réaction tardive"],
         ["Les cabanons n'étaient pas barrés : trente vélos ont disparu.","cause au décor, conséquence à l'évènement"],
         ["Elle lisait son journal quand Sylvain est entré.","habitude interrompue"],
         ["Il faisait noir et personne n'a rien vu.","décor, puis absence d'évènement"],
       ]},

      {t:'piege', h:"Trois pièges du choix",
       rows:[
         ["chercher une liste de verbes","« être et avoir vont toujours à l'imparfait »",
          "Faux : « il a été blessé », « elle a eu peur » sont des évènements au passé composé. Aucun verbe n'appartient à un temps ; c'est le sens de votre phrase qui décide."],
         ["inverser les deux temps dans la phrase à deux temps","« il a dormi quand il entendait l'alarme »",
          "L'imparfait porte la situation qui durait, le passé composé l'évènement qui l'interrompt. Inversés, les deux verbes racontent le contraire de ce qui s'est passé : il aurait dormi à cause de l'alarme."],
         ["croire qu'une longue durée impose l'imparfait","« la rue était fermée pendant six heures » vs « a été fermée »",
          "Une durée fermée, avec un début et une fin, peut très bien aller au passé composé : « la rue a été fermée pendant six heures ». Ce qui compte, ce n'est pas la longueur, c'est de savoir si l'on regarde la chose de l'extérieur ou de l'intérieur."],
       ]},

      {t:'check', h:"Est-ce que c'est clair maintenant ?",
       p:"Quatre questions rapides.",
       qs:[
         {q:"Le premier test à appliquer est…", opts:["quel verbe c'est","si ça a un début et une fin"], ok:1,
          fb:"S'il y a un début et une fin. Le verbe n'y est pour rien."},
         {q:"« Chaque mardi, elle ___ le journal » se complète par…", opts:["lisait","a lu"], ok:0,
          fb:"Lisait : une habitude ne se compte pas, elle dure."},
         {q:"Dans « il dormait quand le feu a éclaté », l'évènement est…", opts:["dormait","a éclaté"], ok:1,
          fb:"A éclaté. « Dormait » est le décor qu'il vient interrompre."},
         {q:"Un récit tout au passé composé donne…", opts:["une liste sèche","une scène vivante"], ok:0,
          fb:"Une liste. Il manque le décor pour que l'autre voie la scène."},
       ]},
    ]
  },

  // ════════════════════════════════════════════════════════════════════════
  t2que: {
    eye:'Mini-leçon', tit:"que, si, ce que — les trois portes du discours rapporté",
    blocs:[
      {t:'texte', h:"Trois mots, et rien d'autre à retenir",
       p:"Rapporter ce que quelqu'un a dit, en français, tient dans trois mots de liaison. Une affirmation entre par « que ». Une question par oui ou non entre par « si ». Une question en « quoi » entre par « ce que » ou « ce qui ». Les autres mots interrogatifs — où, quand, comment, pourquoi, combien — se recopient tels quels. C'est tout, et ça vaut pour la langue entière.",
       note:"Le niveau 5 rapporte au présent : « la Ville dit que… ». Le passé — « la Ville avait dit que… » — vient plus tard. Tant que le verbe qui introduit reste au présent, rien ne bouge dans ce qui suit."},

      {t:'ana', h:"Une affirmation entre par « que »",
       p:"On nomme la personne, on met le verbe de parole au présent, puis « que », puis la phrase telle qu'elle a été dite — avec les pronoms ajustés. Devant une voyelle, « que » devient « qu' ».",
       mots:[["Les services","le porte-parole dit que · la Ville affirme que",true],["Les gens","un témoin raconte que · une résidente explique que"],["Devant une voyelle","il dit qu'on ne sait pas · elle explique qu'elle a perdu"]],
       say:"Le porte-parole dit que l'enquête se poursuit. Elle explique qu'elle a tout perdu.",
       note:"Le verbe qu'on choisit ajoute une couleur : dire est neutre, affirmer est appuyé, expliquer éclaire, raconter met en récit, annoncer donne du neuf, rappeler renvoie à du déjà dit."},

      {t:'ana', h:"Une question par oui ou non entre par « si »",
       p:"Quand la question attend un oui ou un non, on la rapporte avec « si ». Le point d'interrogation disparaît, l'inversion disparaît, le « est-ce que » disparaît.",
       mots:[["La question directe","« Allez-vous refaire le fossé ? »"],["Rapportée","elle demande si la Ville va refaire le fossé",true],["Autres exemples","il demande si la rue rouvrira · on demande s'il y a des blessés"]],
       say:"Elle demande si la Ville va refaire le fossé. On demande s'il y a des blessés.",
       note:"« Si » ne s'élide que devant « il » et « ils » : s'il, s'ils. Devant « elle », on garde « si elle » en toutes lettres. C'est une des rares règles d'orthographe qui ne se discute pas."},

      {t:'ana', h:"Une question en « quoi » entre par « ce que » ou « ce qui »",
       p:"« Que faites-vous ? » devient « on demande ce que la Ville fait ». « Qu'est-ce qui a causé le feu ? » devient « on demande ce qui a causé le feu ». La différence : « ce qui » quand la suite n'a pas de sujet à elle, « ce que » quand elle en a un.",
       mots:[["La suite a un sujet","ce que la Ville fait · ce qu'il a vu"],["La suite n'a pas de sujet","ce qui a causé le feu · ce qui s'est passé",true],["Les autres mots restent","il demande où · elle demande quand · on demande pourquoi"]],
       say:"On demande ce que la Ville fait. On demande ce qui a causé le feu.",
       note:"Le test : mettez la personne juste après. « ce que la Ville fait » — la Ville est là, donc « ce que ». « ce qui a causé le feu » — personne à mettre, donc « ce qui »."},

      {t:'labo', h:"La parole directe, puis la même rapportée",
       p:"Choisissez une parole du module et écoutez-la deux fois : telle qu'elle a été dite, puis rapportée.",
       axes:[{id:'p', lbl:'Quelle parole ?', opts:[
         ['a',"« L'enquête se poursuit. »"],
         ['b',"« Allez-vous refaire le fossé ? »"],
         ['c',"« Que faites-vous pour les vols ? »"],
         ['d',"« Notez le numéro de série. »"],
         ['e','les quatre à la suite']]}],
       out:{
         a:{w:['une enquête','une déclaration'], say:"L'enquête se poursuit. Le porte-parole dit que l'enquête se poursuit.", n:"une affirmation · que"},
         b:{w:['une déclaration'], say:"Allez-vous refaire le fossé ? Une résidente demande si la Ville va refaire le fossé.", n:"une question fermée · si"},
         c:{w:['un enquêteur'], say:"Que faites-vous pour les vols ? Un journaliste demande ce que la police fait pour les vols.", n:"une question en quoi · ce que"},
         d:{w:['la prévention','un vol'], say:"Notez le numéro de série. La police demande aux gens de noter le numéro de série.", n:"un ordre · demander à quelqu'un de"},
         e:{w:['une déclaration','une enquête'], say:"Le porte-parole dit que l'enquête se poursuit. Une résidente demande si la Ville va refaire le fossé. Un journaliste demande ce que la police fait. La police demande aux gens de noter leur numéro.", n:"les quatre portes, à la suite"},
       },
       note:"La quatrième porte est un bonus : un ordre rapporté ne prend ni que, ni si, ni ce que — il prend « demander à quelqu'un de » suivi d'un infinitif."},

      {t:'ex', h:"À écouter et à répéter",
       p:"Six phrases rapportées, du module.",
       rows:[
         ["Le porte-parole dit que l'enquête se poursuit.","que · affirmation"],
         ["La Ville affirme qu'elle a distribué des sacs de sable.","qu' devant une voyelle"],
         ["Une résidente demande si la Ville va refaire le fossé.","si · question fermée"],
         ["Sylvain demande ce que les pompiers ont trouvé.","ce que · la suite a un sujet"],
         ["Teresa demande ce qui a causé l'inondation.","ce qui · la suite n'a pas de sujet"],
         ["Le journal écrit qu'on ne connaît pas encore la cause.","qu' · un sujet impersonnel"],
       ]},

      {t:'piege', h:"Trois pièges du discours rapporté",
       rows:[
         ["garder le point d'interrogation","« elle demande si la Ville va refaire le fossé ? »",
          "Une question rapportée n'est plus une question : c'est un récit. Elle finit par un point. Le point d'interrogation reviendrait seulement si la phrase entière était une question : « Est-ce qu'elle demande si… ? »"],
         ["garder l'inversion ou le « est-ce que »","« il demande est-ce que la rue rouvrira »",
          "Le « est-ce que » et l'inversion sont des outils de la question directe. Rapportée, la phrase reprend l'ordre normal : sujet, verbe, complément. « Il demande si la rue rouvrira. »"],
         ["employer « que » pour une question","« elle demande que la Ville va refaire le fossé »",
          "« Que » n'introduit que des affirmations. Avec une question fermée, c'est « si ». La phrase avec « que » veut dire tout autre chose : elle exige que la Ville le fasse."],
       ]},

      {t:'check', h:"Est-ce que c'est clair maintenant ?",
       p:"Quatre questions rapides.",
       qs:[
         {q:"« Est-ce que la rue rouvrira ? » se rapporte avec…", opts:["que","si"], ok:1,
          fb:"Si : c'est une question par oui ou non."},
         {q:"« Qu'est-ce qui a causé le feu ? » se rapporte avec…", opts:["ce qui","ce que"], ok:0,
          fb:"Ce qui : la suite n'a pas de sujet à elle."},
         {q:"Une question rapportée se termine par…", opts:["un point d'interrogation","un point"], ok:1,
          fb:"Un point. Ce n'est plus une question, c'est un récit."},
         {q:"« Où le feu a-t-il commencé ? » se rapporte avec…", opts:["ce que","où"], ok:1,
          fb:"Où, tel quel : les mots comme où, quand, comment ne changent pas."},
       ]},
    ]
  },

  // ════════════════════════════════════════════════════════════════════════
  t2pron: {
    eye:'Mini-leçon', tit:"Quand la parole change de main",
    blocs:[
      {t:'texte', h:"La personne disait « je » ; vous, vous dites « elle »",
       p:"C'est le morceau qu'on oublie, et c'est celui qui fait sourire les francophones. Quand une résidente dit « j'ai tout perdu dans mon sous-sol », elle parle d'elle. Quand vous rapportez sa phrase, vous parlez d'elle aussi — mais de l'extérieur. Le « je » devient « elle », le « mon » devient « son ». Tout ce qui lui appartenait dans sa phrase lui appartient encore, vu d'ailleurs.",
       note:"Cette transformation-là est mécanique : il n'y a rien à comprendre, seulement un petit tableau à savoir. Une fois qu'il est là, on ne se trompe plus."},

      {t:'ana', h:"Le tableau à connaître par cœur",
       p:"Six lignes, et vous avez tout. Elles marchent dans les deux sens : de la parole directe à la parole rapportée, et l'inverse.",
       mots:[["Les sujets","je → il, elle · nous → ils, elles",true],["Les possessifs","mon, ma, mes → son, sa, ses · notre, nos → leur, leurs"],["Les compléments","me → le, la, lui · moi → lui, elle"]],
       say:"J'ai perdu mes outils. Il dit qu'il a perdu ses outils.",
       note:"Le possessif suit toujours le sujet : si « je » devient « il », alors « mon » devient forcément « son ». On ne peut pas changer l'un sans l'autre."},

      {t:'ana', h:"Le « vous » se règle en regardant qui écoute",
       p:"Si le porte-parole s'adressait à vous et à vos voisins, son « vous » devient « nous » quand vous rapportez à un voisin. S'il s'adressait à d'autres gens, il devient « les résidents » ou « eux ».",
       mots:[["Il vous parlait à vous","« Vous devez évacuer » → il dit que nous devons évacuer",true],["Il parlait à d'autres","il demande aux résidents d'évacuer"],["Le journal rapporte","on demande aux gens de noter leur numéro"]],
       say:"Il dit que nous devons évacuer. Il demande aux résidents d'évacuer.",
       note:"C'est le seul endroit où il faut réfléchir plutôt que d'appliquer le tableau. Posez-vous la question une seconde : à qui la personne parlait-elle ?"},

      {t:'ana', h:"Ce qui ne change pas, et c'est une bonne nouvelle",
       p:"Quand le verbe qui introduit reste au présent — dit, explique, raconte, demande —, le temps de la phrase rapportée ne bouge pas. Le passé composé reste au passé composé, l'imparfait reste à l'imparfait, le futur reste au futur.",
       mots:[["Le passé reste","« j'ai tout perdu » → elle dit qu'elle a tout perdu",true],["L'imparfait reste","« l'eau montait » → il raconte que l'eau montait"],["Le futur reste","« la rue rouvrira » → on dit que la rue rouvrira"]],
       say:"Elle dit qu'elle a tout perdu. Il raconte que l'eau montait déjà.",
       note:"C'est ce qui rend le discours rapporté abordable au niveau 5. Quand le verbe qui introduit passe au passé — « elle a dit que… » —, les temps bougent, et cela s'apprend plus tard."},

      {t:'labo', h:"La phrase de la personne, puis la vôtre",
       p:"Choisissez une parole et écoutez-la des deux côtés du miroir.",
       axes:[{id:'p', lbl:'Quelle parole ?', opts:[
         ['a','la résidente inondée'],
         ['b','les pompiers'],
         ['c','le commerçant'],
         ['d','le locataire réveillé'],
         ['e','les quatre à la suite']]}],
       out:{
         a:{w:['une inondation','une déclaration'], say:"J'ai tout perdu dans mon sous-sol. Elle raconte qu'elle a tout perdu dans son sous-sol.", n:"je → elle · mon → son"},
         b:{w:['évacuer'], say:"Nous pompons depuis mercredi. Les pompiers expliquent qu'ils pompent depuis mercredi.", n:"nous → ils"},
         c:{w:['un témoin','un vol'], say:"J'ai vu trois vélos dans une remorque. Le commerçant dit qu'il a vu trois vélos dans une remorque.", n:"je → il · le passé composé reste"},
         d:{w:['un incendie'], say:"Mes voisins sont sortis avant moi. Il dit que ses voisins sont sortis avant lui.", n:"mes → ses · moi → lui"},
         e:{w:['une déclaration','un témoin'], say:"Elle raconte qu'elle a tout perdu dans son sous-sol. Ils expliquent qu'ils pompent depuis mercredi. Il dit qu'il a vu trois vélos. Il dit que ses voisins sont sortis avant lui.", n:"quatre paroles, toutes rendues à leur propriétaire"},
       },
       note:"Écoutez surtout la quatrième : « avant moi » devient « avant lui ». C'est le petit mot de la fin qu'on laisse traîner le plus souvent."},

      {t:'ex', h:"À écouter et à répéter",
       p:"Six paroles rapportées, avec le déplacement complet.",
       rows:[
         ["Elle raconte qu'elle a tout perdu dans son sous-sol.","je → elle, mon → son"],
         ["Les pompiers expliquent qu'ils pompent depuis mercredi.","nous → ils"],
         ["Le commerçant dit qu'il a vu trois vélos dans une remorque.","je → il"],
         ["La police annonce que leur enquête se poursuit.","notre → leur"],
         ["Le locataire raconte qu'il a cogné à toutes les portes.","je → il, passé composé gardé"],
         ["Elle dit que ses voisins sont sortis avant elle.","mes → ses, moi → elle"],
       ]},

      {t:'piege', h:"Trois pièges du déplacement",
       rows:[
         ["laisser le « je » dans la phrase rapportée","« elle raconte que j'ai tout perdu »",
          "Cette phrase dit que c'est vous qui avez tout perdu. Le sens change complètement, et l'erreur passe inaperçue à l'écrit. Relisez toujours en vous demandant de qui parle chaque pronom."],
         ["changer le sujet sans changer le possessif","« il dit qu'il a perdu mes outils »",
          "Si le sujet devient « il », le possessif devient « ses ». Les deux vont ensemble. Un possessif oublié transforme les outils du témoin en vos outils à vous."],
         ["oublier le pronom de la fin","« il dit que ses voisins sont sortis avant moi »",
          "« Moi » devient « lui ». Ce petit mot est en fin de phrase, on l'a déjà en tête quand on la commence, et c'est exactement pour ça qu'on l'oublie."],
       ]},

      {t:'check', h:"Est-ce que c'est clair maintenant ?",
       p:"Quatre questions rapides.",
       qs:[
         {q:"« J'ai perdu mes clés », dit-elle. Rapporté :", opts:["elle dit qu'elle a perdu ses clés","elle dit qu'elle a perdu mes clés"], ok:0,
          fb:"Ses clés. Le possessif suit le sujet."},
         {q:"« Nous pompons » devient…", opts:["ils pompent","nous pompons"], ok:0,
          fb:"Ils pompent : « nous » devient « ils » quand vous parlez d'eux."},
         {q:"Quand le verbe qui introduit est au présent, le temps de la suite…", opts:["ne change pas","recule d'un cran"], ok:0,
          fb:"Ne change pas. C'est ce qui rend le procédé simple au niveau 5."},
         {q:"« Avant moi » devient…", opts:["avant lui","avant moi"], ok:0,
          fb:"Avant lui. Même les petits mots de la fin se déplacent."},
       ]},
    ]
  },

  // ════════════════════════════════════════════════════════════════════════
  t2qui: {
    eye:'Mini-leçon', tit:"Nommer sa source, ou faire une rumeur",
    blocs:[
      {t:'texte', h:"Trois mots séparent une nouvelle d'une rumeur",
       p:"« Le feu est parti d'une friteuse. » Qui le dit ? Si personne ne le sait, cette phrase ne peut être ni vérifiée ni corrigée : elle circulera telle quelle, et le propriétaire de l'immeuble apprendra un jour que tout le quartier le tient pour un imprudent. Ajoutez trois mots — « les pompiers disent que » — et la même information devient une nouvelle, avec une adresse où aller la vérifier.",
       note:"C'est le meilleur rapport effort-résultat de tout le module : trois mots, et votre récit change de nature."},

      {t:'ana', h:"Les formules qui ne portent personne",
       p:"Elles ne sont pas interdites — on les emploie tous. Mais elles annoncent une information sans propriétaire, et il faut le dire quand on s'en sert.",
       mots:[["Les plus courantes","il paraît que · on dit que · j'ai entendu dire que",true],["Les collectives","tout le monde dit que · les gens racontent que"],["La façon honnête","ça, je ne l'ai lu nulle part"]],
       say:"Il paraît que le propriétaire n'avait pas d'assurance. Ça, je ne l'ai lu nulle part.",
       note:"Dire « ça, je ne l'ai lu nulle part » ne vous fait pas paraître ignorant : ça vous fait paraître fiable. La personne en face sait désormais ce qu'elle peut répéter et ce qu'elle doit garder pour elle."},

      {t:'ana', h:"Les formules qui tiennent debout",
       p:"Chacune porte un nom, un service ou une source qu'on peut aller voir. C'est ce que fait le journal à chaque paragraphe.",
       mots:[["Un service","le Service de sécurité incendie dit que · la Ville affirme que",true],["Une personne","un témoin raconte que · une résidente demande si"],["Une source écrite","selon L'Écho des Cantons · d'après le journal"]],
       say:"Le Service de sécurité incendie dit que le feu serait parti de la cuisine. Selon L'Écho des Cantons, onze personnes ont été hébergées.",
       note:"Remarquez le conditionnel dans la première : « serait parti ». Le journal l'emploie tant que l'enquête n'a rien conclu. Vous pouvez faire pareil, ou dire simplement « ce n'est pas encore certain »."},

      {t:'ana', h:"Le porte-parole n'exprime pas son avis",
       p:"Quand une porte-parole de la Ville parle, ce n'est pas sa position à elle : c'est celle de la Ville. C'est pour ça que le journal écrit « la Ville dit que » et non « madame Untel pense que ».",
       mots:[["Ce qu'on écrit","la Ville dit que · les pompiers expliquent que",true],["Ce qu'on n'écrit pas","la porte-parole pense que · elle croit que"],["Quand c'est un avis personnel","un résident trouve que · un commerçant estime que"]],
       say:"La Ville dit qu'elle a distribué des sacs de sable dès lundi.",
       note:"La nuance a l'air petite. Elle est énorme : la première phrase engage une institution, la seconde n'engage qu'une personne. Un service peut être tenu de faire ce qu'il a annoncé."},

      {t:'labo', h:"La même information, avec et sans source",
       p:"Choisissez une information et écoutez-la des deux façons.",
       axes:[{id:'i', lbl:'Quelle information ?', opts:[
         ['a','la cause du feu'],
         ['b','les sacs de sable'],
         ['c','les trois vélos'],
         ['d','les trois à la suite']]}],
       out:{
         a:{w:['un incendie','une enquête'], say:"Il paraît que le feu est parti d'une friteuse. Le Service de sécurité incendie dit que le feu serait parti de la cuisine du deuxième.", n:"sans source, puis avec"},
         b:{w:['une inondation','une déclaration'], say:"On dit que la Ville n'a rien fait. La Ville affirme qu'elle a distribué des sacs de sable dès lundi.", n:"une rumeur, puis une déclaration"},
         c:{w:['un témoin','un vol'], say:"Tout le monde dit qu'il y a une gang de voleurs. Un commerçant raconte qu'il a vu trois vélos dans une remorque, vers minuit.", n:"un on-dit, puis un témoignage"},
         d:{w:['une déclaration','un fait divers'], say:"Le Service de sécurité incendie dit que le feu serait parti de la cuisine. La Ville affirme qu'elle a distribué des sacs de sable. Un commerçant raconte qu'il a vu trois vélos dans une remorque.", n:"trois informations, trois propriétaires"},
       },
       note:"Écoutez la longueur : la version avec source est à peine plus longue. Ce n'est pas le temps qui manque, c'est l'habitude."},

      {t:'ex', h:"À écouter et à répéter",
       p:"Six phrases qui nomment leur source.",
       rows:[
         ["Le Service de sécurité incendie dit que l'enquête se poursuit.","un service municipal"],
         ["Une porte-parole de la Ville explique que les sacs ont été distribués lundi.","une porte-parole, la position de la Ville"],
         ["Un témoin raconte qu'il a vu quelqu'un sortir du cabanon.","une personne présente"],
         ["Selon L'Écho des Cantons, onze personnes ont été hébergées.","une source écrite"],
         ["La Sûreté du Québec demande de signaler tout vol, même petit.","le corps de police"],
         ["Ça, par exemple, je ne l'ai lu nulle part.","l'aveu qui vous rend fiable"],
       ]},

      {t:'piege', h:"Trois façons de perdre sa source sans le vouloir",
       rows:[
         ["commencer par l'information et oublier de dire d'où elle vient","« le feu est parti d'une friteuse, il paraît »",
          "La source ajoutée après coup, à la fin, se perd : la personne a déjà retenu l'information. Nommez la source d'abord, l'information ensuite. C'est l'ordre du journal, et ce n'est pas un hasard."],
         ["mêler le fait et la source dans la même phrase que votre avis","« les pompiers disent que c'était une friteuse et c'est n'importe quoi »",
          "Deux phrases. La première rapporte, la seconde donne votre avis, annoncé comme tel. Mêlées, on ne sait plus ce que les pompiers ont dit et ce que vous en pensez."],
         ["transformer un service en personne","« la madame de la Ville a dit que… »",
          "Ce n'est pas son avis, c'est la position de la Ville. Dites « la Ville dit que » ou « une porte-parole de la Ville explique que ». La différence engage quelqu'un."],
       ]},

      {t:'check', h:"Est-ce que c'est clair maintenant ?",
       p:"Quatre questions rapides.",
       qs:[
         {q:"« Il paraît que » nous apprend…", opts:["qui parle","rien sur la source"], ok:1,
          fb:"Rien. C'est ce qui en fait une rumeur plutôt qu'une nouvelle."},
         {q:"La source se nomme…", opts:["avant l'information","après, si on y pense"], ok:0,
          fb:"Avant. Après, la personne a déjà retenu l'information toute seule."},
         {q:"Quand une porte-parole parle, elle exprime…", opts:["son avis personnel","la position de son service"], ok:1,
          fb:"La position de son service. C'est pourquoi on écrit « la Ville dit que »."},
         {q:"« Le feu serait parti de la cuisine » : le conditionnel dit…", opts:["que ce n'est pas confirmé","que c'est certain"], ok:0,
          fb:"Que ce n'est pas confirmé. Le journal l'emploie tant que l'enquête n'a rien conclu."},
       ]},
    ]
  },

  // ════════════════════════════════════════════════════════════════════════
  t3fait: {
    eye:'Mini-leçon', tit:"Le fait, l'opinion, et la ligne entre les deux",
    blocs:[
      {t:'texte', h:"Une seule question suffit",
       p:"« Est-ce qu'on peut aller vérifier ? » Trente vélos volés en un mois : on compte, on vérifie, c'est un fait. « C'est de la négligence » : rien à vérifier, quelqu'un juge, c'est une opinion. La question marche sur toutes les phrases du journal, et elle marche aussi sur les vôtres. Elle prend une seconde et elle règle tout.",
       note:"Un fait peut être faux — « cinquante vélos ont été volés » est vérifiable, donc c'est un fait, simplement inexact. Une opinion, elle, n'est ni vraie ni fausse : elle est partagée ou non."},

      {t:'ana', h:"Les mots qui trahissent l'opinion",
       p:"Dès qu'un de ces mots paraît, quelqu'un juge. Vous avez le droit de demander qui, et la personne en face a le droit de vous le demander.",
       mots:[["Les quantités jugées","trop · pas assez · beaucoup trop"],["Les jugements","inacceptable · scandaleux · normal",true],["Les recommandations","il faudrait · on devrait · ils n'ont qu'à"]],
       say:"C'est inacceptable. Il faudrait installer des caméras. Ils n'ont qu'à barrer leur porte.",
       note:"« Il faudrait » est le plus discret des trois : il a l'air d'un constat, mais il propose une action, donc il juge que la situation actuelle ne convient pas."},

      {t:'ana', h:"Les mots qui marquent le fait",
       p:"Des chiffres, des dates, des lieux, des noms de services. Rien de tout cela ne se discute : on l'accepte ou on va vérifier.",
       mots:[["Les chiffres","une trentaine · quatre logements · onze personnes",true],["Le temps et le lieu","vers quatre heures · rue Alexandre · en un mois"],["Les sources","le Service de police recommande · la Croix-Rouge a hébergé"]],
       say:"Une trentaine de vélos ont été volés en un mois. La Croix-Rouge a hébergé onze personnes.",
       note:"Un fait divers bien fait tient dans ces mots-là. C'est pourquoi il est court : les chiffres, les lieux et les noms prennent peu de place."},

      {t:'ana', h:"La façon de faire, en deux phrases",
       p:"D'abord les faits, avec leur source. Ensuite votre avis, annoncé comme tel. Jamais les deux mêlés dans la même phrase.",
       mots:[["La phrase de fait","la police dit qu'une trentaine de vélos ont disparu",true],["La phrase d'avis","moi, ce qui me surprend, c'est le nombre"],["Ce qu'il ne faut pas","la police dit qu'il y a eu trente vols et c'est scandaleux"]],
       say:"La police dit qu'une trentaine de vélos ont disparu. Moi, ce qui me surprend, c'est le nombre.",
       note:"Quand vous mêlez les deux, la personne en face répétera le tout comme si c'était écrit dans le journal. C'est exactement ainsi qu'une opinion devient une information."},

      {t:'labo', h:"Le fait, puis l'opinion qu'on en tire",
       p:"Choisissez une nouvelle et écoutez le fait, puis l'avis qu'on peut en tirer.",
       axes:[{id:'n', lbl:'Quelle nouvelle ?', opts:[
         ['a',"l'incendie"],
         ['b',"l'inondation"],
         ['c','les vols de vélos'],
         ['d','les trois à la suite']]}],
       out:{
         a:{w:['un incendie','un sinistré'], say:"Onze personnes ont perdu leur logement. Moi, ce qui me frappe, c'est qu'un seul locataire a réveillé tout l'immeuble.", n:"un fait vérifiable, puis un avis annoncé"},
         b:{w:['une inondation','un avertissement'], say:"Un avertissement de pluie abondante avait été émis la veille. Moi, ce qui me dérange, c'est qu'on n'ait pas prévenu la rue.", n:"un fait daté, puis un jugement"},
         c:{w:['un vol','la prévention'], say:"Une trentaine de vélos ont été volés en un mois. Moi, ce qui me surprend, c'est le nombre.", n:"un chiffre, puis une réaction"},
         d:{w:['un fait divers'], say:"Onze personnes ont perdu leur logement. Un avertissement avait été émis la veille. Une trentaine de vélos ont disparu en un mois.", n:"trois faits seuls, sans aucun avis"},
       },
       note:"La dernière option ne donne que des faits. Écoutez-la : c'est plat, et c'est normal. Un fait divers est plat ; c'est vous qui ajoutez le relief, et vous dites que c'est vous."},

      {t:'ex', h:"À écouter et à répéter",
       p:"Six phrases, trois faits et trois opinions.",
       rows:[
         ["Une trentaine de vélos ont été volés en un mois.","un chiffre · un fait"],
         ["Laisser son cabanon ouvert, c'est de la négligence.","un jugement · une opinion"],
         ["Le Service de police recommande de noter le numéro de série.","une source · un fait"],
         ["Il faudrait installer des caméras dans les ruelles.","« il faudrait » · une opinion"],
         ["L'incendie a détruit quatre logements de la rue Alexandre.","un lieu, un chiffre · un fait"],
         ["Moi, ce qui me dérange, c'est qu'on n'ait rien fait avant.","annoncé comme un avis"],
       ]},

      {t:'piege', h:"Trois façons de faire passer un avis pour un fait",
       rows:[
         ["le glisser dans une phrase de fait","« la police dit qu'il y a eu trente vols, ce qui est scandaleux »",
          "Le « ce qui est scandaleux » a l'air de faire partie de ce que la police a dit. Coupez : deux phrases, et la deuxième commence par « moi »."],
         ["employer un chiffre vague pour appuyer un jugement","« il y en a eu des centaines »",
          "Un chiffre exagéré reste un fait — un fait faux. Si vous ne savez pas, dites « une trentaine, d'après le journal ». Un chiffre inventé décrédibilise tout le reste de votre récit."],
         ["dire « c'est normal » ou « tout le monde sait »","« tout le monde sait que ce quartier-là est mal surveillé »",
          "« Tout le monde sait » n'est pas une source : c'est un jugement qui se déguise en évidence. Demandez-vous qui, exactement, sait cela — et dites-le, ou renoncez à la phrase."],
       ]},

      {t:'check', h:"Est-ce que c'est clair maintenant ?",
       p:"Quatre questions rapides.",
       qs:[
         {q:"La question qui sépare les deux est…", opts:["est-ce que c'est vrai ?","est-ce qu'on peut vérifier ?"], ok:1,
          fb:"Est-ce qu'on peut vérifier. Un fait peut être faux et rester un fait."},
         {q:"« Il faudrait installer des caméras » est…", opts:["un fait","une opinion"], ok:1,
          fb:"Une opinion : ça propose une action, donc ça juge la situation."},
         {q:"Les faits et l'avis se disent…", opts:["dans deux phrases séparées","dans la même phrase"], ok:0,
          fb:"Dans deux phrases. Mêlés, on ne sait plus ce qui vient du journal."},
         {q:"« Cinquante vélos ont été volés », si c'est inexact, est…", opts:["une opinion","un fait faux"], ok:1,
          fb:"Un fait faux : c'est vérifiable, donc c'est un fait, simplement erroné."},
       ]},
    ]
  },

  // ════════════════════════════════════════════════════════════════════════
  t3disl: {
    eye:'Mini-leçon', tit:"Moi, ce qui me…, c'est…",
    blocs:[
      {t:'texte', h:"Le français annonce avant de dire",
       p:"« Le nombre me surprend » est une phrase correcte que personne ne dit. On dit « moi, ce qui me surprend, c'est le nombre ». C'est plus long, et c'est pourtant partout : à la radio, à table, au travail. La phrase prévient d'abord — attention, je vais donner mon avis, et voici ce que je ressens — puis elle livre l'information. À l'oral, ça donne à l'autre le temps de vous suivre.",
       note:"Cette construction s'appelle la mise en relief. Elle est un des marqueurs les plus nets d'un français aisé : celui qui l'emploie n'a plus l'air de traduire depuis sa langue."},

      {t:'ana', h:"Deux moules, à apprendre tels quels",
       p:"Ce qui me + verbe, c'est + un nom. Ce que je + verbe, c'est + un nom. On emploie « ce qui » quand le morceau mis en relief est le sujet du verbe, « ce que » quand il en est le complément.",
       mots:[["Avec ce qui","ce qui me surprend · ce qui me dérange · ce qui me rassure",true],["Avec ce que","ce que je trouve inquiétant · ce que je ne comprends pas"],["La suite","c'est le nombre · c'est la vitesse · c'est le silence de la Ville"]],
       say:"Moi, ce qui me surprend, c'est le nombre. Ce que je ne comprends pas, c'est le silence de la Ville.",
       note:"Le test : mettez le verbe seul. « Le nombre me surprend » — « le nombre » est sujet, donc « ce qui ». « Je trouve ça inquiétant » — « ça » est complément, donc « ce que »."},

      {t:'ana', h:"Un nom, ou une phrase entière",
       p:"Si la suite est un nom, c'est « c'est ». Si la suite est une phrase avec un verbe, c'est « c'est que ». Une syllabe de différence, et c'est celle qu'on oublie.",
       mots:[["Un nom → c'est","ce qui me surprend, c'est le nombre"],["Une phrase → c'est que","ce qui me dérange, c'est que les gens laissent tout ouvert",true],["Les deux dans un souffle","ce qui me frappe, c'est le nombre, et c'est qu'on n'en parle pas"]],
       say:"Ce qui me surprend, c'est le nombre. Ce qui me dérange, c'est que les gens laissent tout ouvert.",
       note:"Écoutez la deuxième : « c'est que » suivi d'une phrase complète, avec son sujet et son verbe. C'est la forme la plus utile des deux, et la plus oubliée."},

      {t:'ana', h:"Le « moi » du début, et les mots pour tourner",
       p:"Le pronom détaché en tête dit « voici mon point de vue, il n'engage que moi ». Il est presque obligatoire quand on répond à quelqu'un qui vient de donner le sien. Et quand on n'est pas d'accord, on accorde d'abord, on tourne ensuite.",
       mots:[["Annoncer que c'est soi","moi, · personnellement, · à mon avis,",true],["Accorder","c'est vrai que · je comprends que · il y a du vrai là-dedans"],["Tourner","par contre · cependant · n'empêche que"]],
       say:"C'est vrai que ça aide de barrer sa porte. Par contre, ça n'excuse pas celui qui entre.",
       note:"Accorder puis tourner n'est pas seulement plus poli : c'est plus efficace. La personne en face vous écoute encore, parce que vous venez de lui donner raison sur un point."},

      {t:'labo', h:"L'avis plat, puis l'avis mis en relief",
       p:"Choisissez un avis et écoutez-le deux fois : à plat, puis avec la mise en relief.",
       axes:[{id:'a', lbl:'Quel avis ?', opts:[
         ['a','le nombre de vols'],
         ['b','les cabanons ouverts'],
         ['c','le silence de la Ville'],
         ['d','la réponse à Sylvain'],
         ['e','les quatre à la suite']]}],
       out:{
         a:{w:['un vol'], say:"Le nombre me surprend. Moi, ce qui me surprend, c'est le nombre.", n:"un nom · c'est"},
         b:{w:['un cabanon'], say:"Ça me dérange que les gens laissent tout ouvert. Ce qui me dérange, c'est que les gens laissent tout ouvert.", n:"une phrase · c'est que"},
         c:{w:['une déclaration'], say:"Je ne comprends pas le silence de la Ville. Ce que je ne comprends pas, c'est le silence de la Ville.", n:"complément · ce que"},
         d:{w:['la prévention'], say:"C'est vrai que ça aide de barrer sa porte. Par contre, ça n'excuse pas celui qui entre.", n:"accorder, puis tourner"},
         e:{w:['un vol','un cabanon','la prévention'], say:"Moi, ce qui me surprend, c'est le nombre. Ce qui me dérange, c'est que les gens laissent tout ouvert. Ce que je ne comprends pas, c'est le silence de la Ville. Par contre, ça n'excuse pas celui qui entre.", n:"quatre avis, quatre formes"},
       },
       note:"Comparez la version plate et la version en relief : la première est correcte, la seconde est celle qu'on entend. La différence tient en cinq mots."},

      {t:'ex', h:"À écouter et à répéter",
       p:"Six phrases d'opinion, prises dans la discussion du défi 3.",
       rows:[
         ["Moi, ce qui me surprend, c'est le nombre.","moi + ce qui + c'est"],
         ["Ce qui me dérange, c'est que les gens laissent tout ouvert.","c'est que + une phrase"],
         ["Ce que je trouve inquiétant, c'est le retour des mêmes vols.","ce que + complément"],
         ["Ce qui me rassure, c'est qu'on demande de signaler chaque vol.","c'est que + une phrase"],
         ["C'est vrai que ça aide. Par contre, ça n'excuse rien.","accorder, puis tourner"],
         ["Personnellement, je trouve ça inquiétant, parce que trente en un mois, ce n'est plus du hasard.","l'avis, puis sa raison"],
       ]},

      {t:'piege', h:"Trois pièges de la mise en relief",
       rows:[
         ["oublier le « que » devant une phrase","« ce qui me dérange, c'est les gens laissent tout ouvert »",
          "Quand la suite a un verbe conjugué, il faut « c'est que ». Sans lui, deux phrases se collent l'une à l'autre sans lien, et l'oreille française bute dessus immédiatement."],
         ["confondre ce qui et ce que","« ce que me surprend, c'est le nombre »",
          "« Le nombre me surprend » : le nombre est sujet, donc « ce qui ». Le test consiste à remettre la phrase à plat et à regarder si le morceau mis en relief fait le verbe ou le subit."],
         ["donner un avis sans le justifier","« moi, je trouve ça inacceptable. » et rien d'autre",
          "Un avis sans raison ne se discute pas : la personne en face ne peut ni vous suivre ni vous répondre. Ajoutez « parce que », ou un deux-points suivi de la raison. Une phrase de plus, et votre avis devient une position."],
       ]},

      {t:'check', h:"Est-ce que c'est clair maintenant ?",
       p:"Quatre questions rapides.",
       qs:[
         {q:"« Ce qui me dérange, c'est ___ les gens laissent tout ouvert. »", opts:["c'est","c'est que"], ok:1,
          fb:"C'est que : la suite est une phrase avec un verbe conjugué."},
         {q:"« Le nombre me surprend » se met en relief avec…", opts:["ce qui","ce que"], ok:0,
          fb:"Ce qui : « le nombre » est le sujet de « surprend »."},
         {q:"Le « moi » en tête de phrase sert à…", opts:["annoncer que c'est votre avis","insister lourdement"], ok:0,
          fb:"Annoncer que c'est votre avis. C'est poli, pas insistant."},
         {q:"Après « c'est vrai que… », on tourne avec…", opts:["par contre","donc"], ok:0,
          fb:"Par contre, cependant, n'empêche que. On accorde d'abord, on tourne ensuite."},
       ]},
    ]
  },

  // ════════════════════════════════════════════════════════════════════════
  t3imp: {
    eye:'Mini-leçon', tit:"Les phrases impersonnelles, ou dire sans viser personne",
    blocs:[
      {t:'texte', h:"Un « il » qui ne remplace personne",
       p:"« Il faut noter son numéro de série. » Qui est ce « il » ? Personne. Il n'est là que parce qu'un verbe français a besoin d'un sujet, et il ne désigne rien du tout. C'est ce vide qui rend la phrase utile : elle énonce une règle générale, valable pour tout le monde, sans montrer personne du doigt. Le français en est plein — pour la météo, pour l'heure, pour les conseils, pour l'existence des choses.",
       note:"Comparez « tu devrais barrer ton cabanon » et « il vaut mieux barrer son cabanon ». Même conseil, mais le second ne vise personne : on peut le dire à quelqu'un qui vient justement de se faire voler."},

      {t:'ana', h:"Les six qui servent tous les jours",
       p:"Toutes se poursuivent par un infinitif, sauf « il arrive que » et « il y a ». Le degré d'obligation change de l'une à l'autre : il faut est ferme, il faudrait est adouci, il vaut mieux est un conseil.",
       mots:[["L'obligation","il faut · il faudrait · il est important de",true],["Le conseil","il vaut mieux · il est préférable de"],["Le reste","il arrive que · il y a · il manque · il reste"]],
       say:"Il faut noter son numéro de série. Il vaut mieux barrer son cabanon. Il arrive que des vélos restent à la police.",
       note:"« Il faudrait » est celui qui passe le mieux dans une discussion : il propose sans commander, et il laisse à l'autre la place de répondre."},

      {t:'ana', h:"Le verbe reste au singulier, toujours",
       p:"Le sujet est « il », pas ce qui suit. Cela vaut aussi pour « il y a », « il manque », « il reste », « il s'agit de ».",
       mots:[["Il y a","il y a eu trente vols · il y a onze sinistrés",true],["Il manque, il reste","il manque deux vélos · il reste quatre logements"],["Il s'agit de","il s'agit de trois cabanons ouverts"]],
       say:"Il y a eu une trentaine de vols. Il manque encore deux vélos.",
       note:"« Il y ont eu » n'existe pas, et pourtant on l'entend souvent chez les personnes qui apprennent : le pluriel qui suit tire l'oreille vers un accord qui ne vient jamais."},

      {t:'ana', h:"La météo et l'heure y passent aussi",
       p:"Vous les employez déjà : ce sont exactement les phrases qui plantaient le décor au défi 1. Un même « il » vide, un même verbe au singulier.",
       mots:[["Le temps qu'il fait","il pleuvait depuis trois jours · il ventait fort"],["L'heure","il était quatre heures du matin",true],["L'existence","il y avait quatre logements dans l'immeuble"]],
       say:"Il pleuvait depuis trois jours. Il était quatre heures du matin.",
       note:"C'est un bon rappel : le décor du défi 1 et les conseils du défi 3 se construisent pareil. Une même mécanique sert deux fois dans le module."},

      {t:'labo', h:"Le conseil qui vise, et celui qui ne vise personne",
       p:"Choisissez un conseil et écoutez-le des deux façons.",
       axes:[{id:'c', lbl:'Quel conseil ?', opts:[
         ['a','le numéro de série'],
         ['b','le cabanon barré'],
         ['c','le fossé à refaire'],
         ['d','signaler chaque vol'],
         ['e','les quatre à la suite']]}],
       out:{
         a:{w:['la prévention','un vol'], say:"Tu devrais noter ton numéro de série. Il est important de noter son numéro de série.", n:"le conseil qui vise, puis celui qui ne vise personne"},
         b:{w:['un cabanon'], say:"Barre donc ton cabanon. Il vaut mieux barrer son cabanon, même pour une heure.", n:"l'ordre, puis le conseil général"},
         c:{w:['une inondation'], say:"La Ville doit refaire le fossé. Il faudrait refaire le fossé avant l'automne.", n:"l'accusation, puis la proposition"},
         d:{w:['un vol','un suspect'], say:"Vous devez signaler chaque vol. Il faut signaler chaque vol, même petit.", n:"la consigne, puis la règle"},
         e:{w:['la prévention','un cabanon'], say:"Il est important de noter son numéro de série. Il vaut mieux barrer son cabanon. Il faudrait refaire le fossé avant l'automne. Il faut signaler chaque vol, même petit.", n:"quatre règles, aucun doigt pointé"},
       },
       note:"Écoutez la dernière option en entier. Aucune de ces quatre phrases ne vise quelqu'un, et elles disent pourtant tout ce qu'il y a à dire."},

      {t:'ex', h:"À écouter et à répéter",
       p:"Six phrases impersonnelles du module.",
       rows:[
         ["Il faut noter le numéro de série de son vélo.","obligation ferme"],
         ["Il faudrait refaire le fossé avant l'automne.","obligation adoucie"],
         ["Il vaut mieux barrer son cabanon, même pour une heure.","conseil"],
         ["Il arrive que des vélos restent à la police.","fréquence"],
         ["Il y a eu une trentaine de vols en un mois.","existence · verbe au singulier"],
         ["Il est important de signaler chaque vol, même petit.","règle générale"],
       ]},

      {t:'piege', h:"Trois pièges des phrases impersonnelles",
       rows:[
         ["accorder le verbe avec ce qui suit","« il y ont eu trente vols »",
          "Le sujet est « il », qui est toujours singulier. « Il y a eu trente vols », « il manque deux vélos », « il reste quatre logements ». Le pluriel qui suit ne compte pas."],
         ["oublier le « de » après « il est important »","« il est important noter son numéro »",
          "« Il est important de », « il est préférable de », « il est nécessaire de » : la préposition fait partie de la tournure. « Il faut » et « il vaut mieux » sont les deux seules qui s'en passent."],
         ["employer « il faut » quand on veut discuter","« il faut refaire le fossé » dit à quelqu'un qui n'est pas d'accord",
          "« Il faut » ferme la discussion : c'est une obligation, il n'y a rien à répondre. Si vous voulez que l'autre réagisse, dites « il faudrait » ou « il vaudrait mieux ». Une syllabe, et la conversation reste ouverte."],
       ]},

      {t:'check', h:"Est-ce que c'est clair maintenant ?",
       p:"Quatre questions rapides.",
       qs:[
         {q:"Dans « il faut noter son numéro », le « il » désigne…", opts:["personne","la police"], ok:0,
          fb:"Personne. C'est un sujet vide, exigé par la grammaire."},
         {q:"« Il ___ eu trente vols » se complète par…", opts:["y a","y ont"], ok:0,
          fb:"Y a. Le sujet est « il », toujours singulier."},
         {q:"Pour laisser la discussion ouverte, on dit…", opts:["il faut","il faudrait"], ok:1,
          fb:"Il faudrait : ça propose au lieu de commander."},
         {q:"« Il est important ___ signaler chaque vol. »", opts:["de","—"], ok:0,
          fb:"De. La préposition fait partie de la tournure."},
       ]},
    ]
  },

};
