const PLUS = {
  prSon: {
    eye:'Mini-leçon', tit:"Un seul son, trois orthographes : eau, au, o",
    blocs:[
      {t:'texte', h:"Le son ne vous dira jamais comment l'écrire",
       p:"« L'eau », « chaud », « une photo » : dans ces trois mots, votre bouche fait exactement la même chose. Un seul son, [o], et trois façons de l'écrire. Aucune règle de prononciation ne peut vous départager, parce qu'il n'y a rien à entendre. Ce qui décide, c'est la <b>famille du mot</b> et la <b>place du son</b> dans le mot.",
       note:"C'est la difficulté la plus fréquente à l'écrit chez les adultes en francisation, et elle ne vient pas de l'oreille : elle vient de l'orthographe du français, qui a gardé trois graphies anciennes pour un son qui s'est simplifié."},

      {t:'ana', h:"eau — presque toujours à la fin d'un mot",
       p:"C'est la graphie la plus visible, et elle se place au bout.",
       mots:[['On écrit','l\'eau · le bureau · le nouveau'],['La place','à la fin du mot, presque toujours',true],['Exception connue','beaucoup — le « eau » est au début']],
       say:"L'eau tombait du plafond.",
       note:"Un mot qui finit par le son [o] et qui compte deux syllabes ou plus s'écrit souvent « eau » : un chapeau, un cadeau, un morceau, un rideau."},

      {t:'ana', h:"au — au début ou au milieu, souvent devant une consonne",
       p:"La graphie du milieu de mot.",
       mots:[['On écrit','chaud · une chaudière · aussi'],['La place','au début ou au milieu',true],['Un cas à part','un tuyau — « au » à la fin']],
       say:"Elle a mis une chaudière par terre.",
       note:"Devant un « d », un « t », un « s » ou un « ss », c'est presque toujours « au » : chaud, haut, la cause, aussi, la faute."},

      {t:'ana', h:"o — la graphie courte, souvent dans les mots savants",
       p:"Une seule lettre, dans des mots venus du latin, du grec, ou raccourcis.",
       mots:[['On écrit','une photo · un numéro · trop'],['La place','partout, mais surtout dans les mots courts',true],['Avec accent','bientôt · le côté — « ô » se prononce pareil']],
       say:"Voici mon numéro de dossier.",
       note:"Attention : le « o » sans accent ne se prononce pas toujours [o]. Dans « une porte » ou « un dossier », il est plus ouvert. C'est le « ô » et le « o » de fin de mot qui sont fermés."},

      {t:'labo', h:"Écoutez, puis regardez l'orthographe",
       p:"Choisissez un mot du module et vérifiez comment son son [o] s'écrit.",
       axes:[{id:'m', lbl:'Quel mot ?', opts:[
         ['a','l\'eau'],
         ['b','une chaudière'],
         ['c','une photo'],
         ['d','chaud'],
         ['e','le bureau'],
         ['f','un tuyau'],
         ['g','trop']]}],
       out:{
         a:{w:["l'eau → EAU"], say:"L'eau tombait du plafond.", n:"fin de mot, deux lettres muettes après"},
         b:{w:['une chaudière → AU'], say:"Elle a mis une chaudière par terre.", n:"milieu de mot, devant un « d »"},
         c:{w:['une photo → O'], say:"J'ai pris vingt-deux photos.", n:"mot court, graphie savante"},
         d:{w:['chaud → AU'], say:"Le réservoir était encore chaud.", n:"devant un « d » final muet"},
         e:{w:['le bureau → EAU'], say:"Le bureau du propriétaire est fermé le samedi.", n:"fin de mot, deux syllabes"},
         f:{w:['un tuyau → AU'], say:"Le tuyau était fissuré depuis longtemps.", n:"fin de mot, mais « au » : l'exception à retenir"},
         g:{w:['trop → O'], say:"C'est trop de bruit pour une chambre.", n:"mot court, « p » muet"},
       },
       note:"Écoutez chaque mot deux fois : la première pour le son, la seconde en regardant l'orthographe. C'est la paire son + image qui se retient, jamais le son tout seul."},

      {t:'ex', h:"À écouter et à répéter",
       p:"Neuf phrases du module, une par mot.",
       rows:[
         ["L'eau tombait du plafond.","eau → EAU"],
         ["Elle a mis une chaudière par terre.","chaudière → AU"],
         ["J'ai pris vingt-deux photos.","photo → O"],
         ["Le réservoir était encore chaud.","chaud → AU"],
         ["Le bureau du propriétaire est fermé le samedi.","bureau → EAU"],
         ["Voici mon numéro de dossier.","numéro → O"],
         ["Le tuyau était fissuré depuis longtemps.","tuyau → AU"],
         ["Le nouveau plancher arrive lundi.","nouveau → EAU"],
         ["C'est trop de bruit pour une chambre.","trop → O"],
       ]},

      {t:'piege', h:"Trois pièges à connaître",
       rows:[
         ["croire que l'oreille aide","« je vais l'entendre »",
          "Non. Les trois graphies se prononcent exactement pareil. Ce qui aide, c'est de voir le mot écrit souvent — pas de l'écouter mieux."],
         ["oublier les lettres muettes","« chaud » écrit « chau »",
          "Beaucoup de mots en [o] finissent par une consonne qu'on n'entend pas : chaud, trop, haut, le mot. Cherchez le féminin ou un mot de la même famille : chaude, chaudière."],
         ["mettre « eau » partout","« chaudeau », « photeau »",
          "« eau » est fréquent, mais il ne va pas partout. Devant une consonne prononcée, ce n'est jamais « eau » : la cause, l'assèchement, aussi."],
       ]},

      {t:'check', h:"Est-ce que c'est clair maintenant ?",
       p:"Quatre questions rapides.",
       qs:[
         {q:"« eau » se trouve le plus souvent…", opts:["au début du mot","à la fin du mot"], ok:1,
          fb:"le bureau, le nouveau, un morceau : le son [o] final s'écrit souvent « eau »."},
         {q:"Devant un « d » ou un « t », on écrit plutôt…", opts:["au","eau"], ok:0,
          fb:"chaud, haut, la faute : c'est « au » qui vient devant ces consonnes."},
         {q:"« un tuyau » est intéressant parce que…", opts:["c'est « au » à la fin d'un mot","c'est « eau » au milieu"], ok:0,
          fb:"C'est l'exception à retenir : le son [o] final s'y écrit « au »."},
         {q:"Pour choisir la bonne graphie, le meilleur moyen est…", opts:["d'écouter mieux","de connaître le mot écrit"], ok:1,
          fb:"L'oreille ne peut pas trancher : les trois graphies sonnent pareil."},
       ]},

      {t:'revoir', h:"À retenir en une ligne",
       p:"Le son [o] ne s'entend qu'une façon et s'écrit trois : <b>eau</b> à la fin des mots longs, <b>au</b> au milieu et devant une consonne, <b>o</b> dans les mots courts et savants."},
    ]
  },

  prDegat: {
    eye:'Mini-leçon', tit:"Décrire un dégât : le mot juste, pièce par pièce",
    blocs:[
      {t:'texte', h:"« C'est brisé » ne donne rien à personne",
       p:"Un propriétaire, un assureur et un entrepreneur ne travaillent pas avec des impressions : ils travaillent avec des descriptions. Dire « il y a de l'eau » ne permet ni de chiffrer, ni de dater, ni de décider de l'urgence. Une bonne description tient en trois éléments : <b>quoi</b>, <b>où exactement</b>, <b>de quelle taille</b>.",
       note:"C'est aussi ce qui vous protège. Une description précise faite le jour même vaut, plus tard, plus qu'une longue explication faite de mémoire."},

      {t:'ana', h:"Le verbe qui va avec chaque surface",
       p:"Chaque matériau a son verbe, et c'est celui-là qu'on attend de vous.",
       mots:[['Le plafond','coule, puis il cerne'],['La peinture','cloque, puis elle se décolle',true],['Le plancher de bois','gonfle, puis il gondole']],
       say:"Le plancher a commencé à gondoler.",
       note:"Employer le verbe du métier fait gagner du temps : la personne au bout du fil sait immédiatement à quel stade en est le dommage."},

      {t:'ana', h:"Situer, sans approximation",
       p:"Trois repères suffisent : la pièce, le mur, la hauteur.",
       mots:[['La pièce','dans la chambre'],['Le mur ou le coin','dans le coin nord, au-dessus du lit',true],['La taille','environ un mètre de diamètre']],
       say:"Un cerne brun d'environ un mètre au plafond de la chambre.",
       note:"« Environ » n'est pas un défaut : c'est une mesure honnête. Ce qui nuit, c'est « assez gros » ou « pas mal grand »."},

      {t:'ana', h:"Séparer le bâtiment de vos biens",
       p:"Deux listes, dès la première description.",
       mots:[['Le bâtiment','le plafond, le plancher, les murs, la plomberie'],['Vos biens','le matelas, les meubles, les papiers, les vêtements',true],['Pourquoi','deux assureurs différents']],
       say:"Le plafond appartient à l'immeuble, le matelas m'appartient.",
       note:"Faire cette séparation dès le premier appel vous évite d'être renvoyé d'une porte à l'autre pendant deux semaines."},

      {t:'labo', h:"Du flou au précis",
       p:"Choisissez une phrase vague et voyez ce qu'elle devient.",
       axes:[{id:'p', lbl:'Quelle phrase ?', opts:[
         ['a','« Il y a de l\'eau. »'],
         ['b','« Le mur est abîmé. »'],
         ['c','« Le plancher est bizarre. »'],
         ['d','« J\'ai perdu des affaires. »']]}],
       out:{
         a:{w:["Un cerne brun d'environ un mètre au plafond de la chambre, dans le coin nord."], say:"Un cerne brun d'environ un mètre au plafond de la chambre.", n:"quoi + où + taille"},
         b:{w:["La peinture cloque sur environ trente centimètres, à mi-hauteur du mur de la cuisine."], say:"La peinture cloque sur environ trente centimètres.", n:"le verbe du métier fait la différence"},
         c:{w:["Le plancher gondole sur trois lattes, le long du mur extérieur."], say:"Le plancher gondole sur trois lattes.", n:"une mesure comptable : trois lattes"},
         d:{w:["Un matelas double humide sur un coin et une boîte de documents complètement trempée."], say:"Une boîte de documents complètement trempée.", n:"des biens nommés, donc chiffrables"},
       },
       note:"Dans les quatre cas, la phrase précise n'est pas plus longue : elle est mieux choisie."},

      {t:'ex', h:"À écouter et à répéter",
       p:"Cinq descriptions à réutiliser telles quelles.",
       rows:[
         ["Un cerne brun d'environ un mètre au plafond de la chambre.","quoi, où, taille"],
         ["Le plancher gondole sur trois lattes le long du mur.","une mesure comptable"],
         ["La peinture cloque à mi-hauteur du mur de la cuisine.","le verbe juste"],
         ["Ça coulait sans arrêt de six heures à sept heures.","la durée et le rythme"],
         ["Je ne peux plus coucher dans ma chambre depuis trois nuits.","l'usage empêché"],
       ]},

      {t:'piege', h:"Trois pièges à connaître",
       rows:[
         ["décrire ses émotions","« c'est un cauchemar »",
          "Compréhensible, mais inutilisable. Gardez une phrase pour dire que c'est difficile, et donnez le reste en faits."],
         ["oublier l'usage empêché","« le plafond est taché »",
          "C'est la ligne qui fonde une compensation. Sans « je ne peux plus dormir dans cette pièce », il n'y a qu'un dommage matériel."],
         ["tout réparer avant de faire constater","« j'ai déjà repeint »",
          "Limiter les dégâts, oui ; réparer, non. Ce qui est réparé n'est plus prouvable, et la facture reste alors la vôtre."],
       ]},

      {t:'check', h:"Est-ce que c'est clair maintenant ?",
       p:"Quatre questions rapides.",
       qs:[
         {q:"Le plancher de bois qui a bu de l'eau…", opts:["cloque","gondole"], ok:1,
          fb:"Le bois gondole ; c'est la peinture qui cloque."},
         {q:"« Environ un mètre » est…", opts:["une mesure honnête","une imprécision à éviter"], ok:0,
          fb:"Une estimation annoncée vaut mieux qu'un adjectif vague."},
         {q:"Le matelas abîmé relève de…", opts:["l'assurance du propriétaire","votre assurance"], ok:1,
          fb:"Le bâtiment est à lui, vos biens sont à vous."},
         {q:"Avant que l'assureur passe, il faut…", opts:["ne rien jeter","tout nettoyer"], ok:0,
          fb:"Un bien jeté est un bien qu'on ne peut plus faire constater."},
       ]},

      {t:'revoir', h:"À retenir en une ligne",
       p:"Une description utile dit <b>quoi</b>, <b>où exactement</b>, <b>de quelle taille</b> — avec le verbe du métier — puis ce que ça vous empêche de faire."},
    ]
  },

  t1temps: {
    eye:'Mini-leçon', tit:"Imparfait ou passé composé : raconter un sinistre",
    blocs:[
      {t:'texte', h:"Deux temps, deux rôles, jamais interchangeables",
       p:"Quand vous racontez un dégât, vous faites deux choses en même temps : vous <b>décrivez la situation</b> — il faisait noir, l'eau coulait, je ne savais pas d'où ça venait — et vous <b>énumérez les événements</b> — je me suis levée, j'ai mis une chaudière, j'ai appelé. Le français donne un temps à chacune de ces deux tâches. Ce n'est pas une question de durée réelle : c'est une question de rôle dans le récit.",
       note:"C'est pour cette raison qu'un même verbe peut aller aux deux temps selon la phrase : « il pleuvait quand je suis sorti » et « il a plu toute la journée » sont tous les deux corrects, et ne disent pas la même chose."},

      {t:'ana', h:"L'imparfait — le décor, ce qui durait",
       p:"Il répond à : c'était comment, à ce moment-là ?",
       mots:[['Formation','le radical de « nous » + -ais, -ais, -ait, -ions, -iez, -aient'],['Exemple','nous coul-ons → il coulait',true],['Le seul irrégulier','être → j\'étais']],
       say:"L'eau coulait déjà quand je me suis réveillée.",
       note:"Test simple : si vous pouvez ajouter « pendant tout ce temps-là » sans que la phrase devienne bizarre, c'est l'imparfait."},

      {t:'ana', h:"Le passé composé — l'événement, ce qui est arrivé une fois",
       p:"Il répond à : qu'est-ce qui s'est passé ?",
       mots:[['Formation','avoir ou être au présent + participe passé'],['Avec avoir','j\'ai mis, j\'ai appelé, il a lâché',true],['Avec être','je me suis levée, elle est montée']],
       say:"Je me suis levée à six heures et j'ai appelé le propriétaire.",
       note:"Chaque passé composé fait avancer l'histoire d'un cran. Si vous pouvez mettre « et puis » devant, c'est le bon temps."},

      {t:'ana', h:"Les deux dans la même phrase",
       p:"C'est la forme normale du récit de sinistre.",
       mots:[['Le décor','L\'eau coulait déjà'],['coupé par l\'événement','quand je me suis réveillée',true],['Le mot charnière','« quand » introduit l\'événement, « pendant que » le décor']],
       say:"Il faisait encore noir quand le réservoir a lâché.",
       note:"Retenez la paire : <b>quand</b> + passé composé, <b>pendant que</b> + imparfait. Elle règle à elle seule la moitié des hésitations."},

      {t:'ana', h:"L'accord du participe passé avec être",
       p:"Avec « être », le participe s'accorde comme un adjectif.",
       mots:[['Elle','elle est montée · elle s\'est levée'],['Ils','ils sont partis',true],['Avec avoir','pas d\'accord avec le sujet : elle a mis, ils ont appelé']],
       say:"Elle est montée voir le chauffe-eau.",
       note:"Les verbes pronominaux — se lever, se réveiller, s'inquiéter — prennent tous « être »."},

      {t:'labo', h:"La même histoire, phrase par phrase",
       p:"Choisissez une phrase du récit de Mariama et voyez pourquoi c'est ce temps-là.",
       axes:[{id:'r', lbl:'Quelle phrase ?', opts:[
         ['a','Il faisait encore noir.'],
         ['b','Je me suis levée à six heures.'],
         ['c','L\'eau tombait du plafond.'],
         ['d','J\'ai mis une chaudière par terre.'],
         ['e','Le chauffe-eau avait quinze ans.'],
         ['f','Le plombier a remplacé le réservoir.']]}],
       out:{
         a:{w:['imparfait — décor'], say:"Il faisait encore noir.", n:"un état, pas un événement"},
         b:{w:['passé composé — événement'], say:"Je me suis levée à six heures.", n:"une fois, à une heure précise ; avec être, donc accord"},
         c:{w:['imparfait — ce qui durait'], say:"L'eau tombait du plafond.", n:"ça durait depuis un moment"},
         d:{w:['passé composé — événement'], say:"J'ai mis une chaudière par terre.", n:"un geste, terminé"},
         e:{w:['imparfait — état ancien'], say:"Le chauffe-eau avait quinze ans.", n:"une caractéristique, pas un fait nouveau"},
         f:{w:['passé composé — événement'], say:"Le plombier a remplacé le réservoir.", n:"fait daté, avec avoir, pas d'accord"},
       },
       note:"Relisez les six phrases dans l'ordre : vous entendez le récit avancer aux passés composés et se poser aux imparfaits."},

      {t:'ex', h:"À écouter et à répéter",
       p:"Six phrases du récit, dans l'ordre.",
       rows:[
         ["Il faisait encore noir et tout le monde dormait.","décor"],
         ["Le réservoir a lâché vers trois heures du matin.","événement"],
         ["L'eau coulait déjà quand je me suis réveillée.","les deux ensemble"],
         ["Je me suis levée et j'ai mis une chaudière.","deux événements"],
         ["Je ne savais pas encore d'où ça venait.","décor"],
         ["En rentrant du travail, j'ai vu que la tache avait doublé.","événement"],
       ]},

      {t:'piege', h:"Trois pièges à connaître",
       rows:[
         ["choisir selon la durée réelle","« ça a duré longtemps, donc imparfait »",
          "Non : « il a plu pendant trois jours » est bien un passé composé. Ce qui compte est le rôle dans le récit, pas le temps qu'a pris la chose."],
         ["mettre tout au passé composé","« il a fait noir, l'eau a tombé »",
          "Le récit devient une liste et on ne sait plus ce qui est le décor. En plus, « l'eau a tombé » n'existe pas : c'est « tomber » avec être, « l'eau est tombée »."],
         ["oublier l'accord avec être","« je me suis levé » pour une femme",
          "Avec être, le participe s'accorde avec le sujet : levée, montée, partie. Avec avoir, non."],
       ]},

      {t:'check', h:"Est-ce que c'est clair maintenant ?",
       p:"Quatre questions rapides.",
       qs:[
         {q:"« Pendant que je travaillais » demande…", opts:["l'imparfait","le passé composé"], ok:0,
          fb:"« pendant que » laisse durer : imparfait."},
         {q:"« Quand je me suis réveillée » est…", opts:["le décor","l'événement qui coupe"], ok:1,
          fb:"« quand » + passé composé introduit l'événement."},
         {q:"« Le chauffe-eau avait quinze ans » est à l'imparfait parce que…", opts:["c'est un état","ça a duré quinze ans"], ok:0,
          fb:"C'est une caractéristique de la situation, pas un fait nouveau."},
         {q:"Avec « avoir », le participe s'accorde-t-il avec le sujet ?", opts:["oui","non"], ok:1,
          fb:"Seulement avec « être » : elle est montée, mais elle a mis."},
       ]},

      {t:'revoir', h:"À retenir en une ligne",
       p:"L'<b>imparfait</b> plante le décor de ce qui durait ; le <b>passé composé</b> fait avancer l'histoire d'un événement à la fois. <b>Quand</b> + passé composé, <b>pendant que</b> + imparfait."},
    ]
  },

  t1ger: {
    eye:'Mini-leçon', tit:"Le gérondif : « en rentrant », « en ouvrant »",
    blocs:[
      {t:'texte', h:"Une forme courte pour dire deux choses à la fois",
       p:"« Quand je suis rentrée du travail, j'ai vu la tache » et « En rentrant du travail, j'ai vu la tache » disent la même chose. La deuxième est plus courte, plus fluide, et c'est celle que le programme du niveau 5 attend de vous. C'est le <b>gérondif</b> : « en » suivi du participe présent.",
       note:"Il sert à deux choses seulement : dire que deux actions se font en même temps, ou dire comment on s'y est pris. Rien d'autre — et c'est ce qui le rend facile."},

      {t:'ana', h:"Comment il se forme",
       p:"Une seule règle, à partir du présent.",
       mots:[['On prend « nous »','nous rentr-ons'],['On enlève -ons, on ajoute -ant','rentrant',true],['On met « en » devant','en rentrant']],
       say:"En rentrant du travail, j'ai vu que la tache avait doublé.",
       note:"La forme est invariable : elle ne s'accorde jamais, ni en genre ni en nombre. En rentrant, qu'on soit un, deux ou dix."},

      {t:'ana', h:"Les trois formes irrégulières",
       p:"Elles ne suivent pas la règle du « nous », et ce sont les seules.",
       mots:[['être','en étant'],['avoir','en ayant',true],['savoir','en sachant']],
       say:"En sachant que l'assureur passerait, je n'ai rien jeté.",
       note:"Apprenez-les ensemble, en trois mots : étant, ayant, sachant."},

      {t:'ana', h:"Premier emploi : en même temps",
       p:"Deux actions du même sujet, dans le même moment.",
       mots:[['On dit','En ouvrant la porte, j\'ai senti l\'humidité.'],['Ce que ça veut dire','j\'ouvrais et je sentais, au même moment',true],['Sans gérondif','Quand j\'ai ouvert la porte, j\'ai senti l\'humidité.']],
       say:"En ouvrant la porte de la chambre, elle a senti l'humidité.",
       note:"C'est l'emploi le plus fréquent dans un récit de sinistre : on découvre quelque chose en faisant autre chose."},

      {t:'ana', h:"Deuxième emploi : la manière ou le moyen",
       p:"Comment on s'y est pris.",
       mots:[['On dit','Elle a limité les dommages en plaçant une chaudière.'],['Question','comment ? — en plaçant une chaudière',true],['Autre exemple','On prouve un dégât en prenant des photos datées.']],
       say:"On prouve un dégât en prenant des photos datées.",
       note:"Dans cet emploi, le gérondif remplace « parce que » ou « grâce au fait que », en beaucoup plus court."},

      {t:'ana', h:"La règle du sujet unique",
       p:"C'est la seule vraie contrainte, et c'est là que se font les fautes.",
       mots:[['Correct','En rentrant, j\'ai vu la tache. — c\'est moi qui rentre et moi qui vois'],['Incorrect','En rentrant, la tache avait doublé. — la tache ne rentre pas',true],['La solution','Pendant que je rentrais, … ou Quand je suis rentrée, …']],
       say:"En rentrant, j'ai vu que la tache avait doublé.",
       note:"Avant d'écrire un gérondif, posez-vous la question : qui fait cette action ? Si ce n'est pas le sujet de la phrase, il faut une subordonnée."},

      {t:'labo', h:"Transformez",
       p:"Choisissez une phrase et voyez sa forme au gérondif.",
       axes:[{id:'g', lbl:'Quelle phrase ?', opts:[
         ['a','Quand je suis rentrée du travail…'],
         ['b','Quand elle a ouvert la porte…'],
         ['c','Parce qu\'elle a placé une chaudière…'],
         ['d','Quand il est monté au troisième…'],
         ['e','Comme je savais que l\'assureur passerait…']]}],
       out:{
         a:{w:['en rentrant'], say:"En rentrant du travail, j'ai vu que la tache avait doublé.", n:"nous rentrons → rentrant"},
         b:{w:['en ouvrant'], say:"En ouvrant la porte de la chambre, elle a senti l'humidité.", n:"nous ouvrons → ouvrant"},
         c:{w:['en plaçant'], say:"Elle a limité les dommages en plaçant une chaudière sous la fuite.", n:"la manière : comment ?"},
         d:{w:['en montant'], say:"En montant au troisième, Kim a trouvé le réservoir percé.", n:"deux actions du même sujet"},
         e:{w:['en sachant'], say:"En sachant que l'assureur passerait, je n'ai rien jeté.", n:"forme irrégulière : savoir → sachant"},
       },
       note:"Dans les cinq cas, la phrase perd deux ou trois mots et gagne en fluidité. C'est exactement ce que vise le niveau 5."},

      {t:'ex', h:"À écouter et à répéter",
       p:"Six phrases du module.",
       rows:[
         ["En rentrant du travail, j'ai vu que la tache avait doublé.","simultanéité"],
         ["En ouvrant la porte, elle a senti l'humidité.","simultanéité"],
         ["Elle a limité les dommages en plaçant une chaudière.","manière"],
         ["On prouve un dégât en prenant des photos datées.","moyen"],
         ["En montant au troisième, Kim a trouvé le réservoir percé.","simultanéité"],
         ["En sachant que l'assureur passerait, je n'ai rien jeté.","forme irrégulière"],
       ]},

      {t:'piege', h:"Trois pièges à connaître",
       rows:[
         ["changer de sujet en cours de route","« En rentrant, la tache avait doublé »",
          "La tache ne rentre pas. Le gérondif appartient au sujet de la phrase — ici, il faut « Quand je suis rentrée, la tache avait doublé »."],
         ["accorder le participe présent","« en rentrantes »",
          "Jamais. Le gérondif est invariable, toujours."],
         ["confondre avec l'adjectif verbal","« une fuite coulante » et « en coulant »",
          "L'adjectif décrit et s'accorde ; le gérondif dit comment ou quand, et ne s'accorde pas. Un « en » devant règle la question."],
       ]},

      {t:'check', h:"Est-ce que c'est clair maintenant ?",
       p:"Quatre questions rapides.",
       qs:[
         {q:"Le gérondif se forme à partir de…", opts:["l'infinitif","la forme « nous » du présent"], ok:1,
          fb:"nous rentrons → en rentrant."},
         {q:"« savoir » au gérondif donne…", opts:["en sachant","en savant"], ok:0,
          fb:"C'est l'une des trois formes irrégulières : étant, ayant, sachant."},
         {q:"Le gérondif et le verbe principal doivent avoir…", opts:["le même sujet","des sujets différents"], ok:0,
          fb:"C'est la contrainte à retenir ; sinon, on emploie une subordonnée."},
         {q:"« Elle a limité les dommages en plaçant une chaudière » exprime…", opts:["la manière","le temps"], ok:0,
          fb:"C'est le second emploi : comment elle s'y est prise."},
       ]},

      {t:'revoir', h:"À retenir en une ligne",
       p:"<b>en</b> + le radical de « nous » + <b>-ant</b>. Deux emplois : en même temps, ou de quelle manière. Une contrainte : le même sujet que le verbe principal."},
    ]
  },

  t2sens: {
    eye:'Mini-leçon', tit:"Lire un avis officiel sans se faire avoir",
    blocs:[
      {t:'texte', h:"Un avis est court, et pourtant il engage",
       p:"Une feuille affichée dans une entrée d'immeuble tient en quinze lignes. Elle vous dit ce qui va se passer, ce que vous devez faire, et ce qui arrivera si vous ne le faites pas. Les trois informations sont toujours là, dans cet ordre, et elles sont écrites dans une langue qui n'est celle de personne — ni parlée, ni littéraire : la langue administrative.",
       note:"Cette langue-là revient partout : l'école de vos enfants, la ville, Hydro-Québec, votre assureur. La reconnaître une fois, c'est la reconnaître toujours."},

      {t:'ana', h:"Le titre : à qui ça s'adresse",
       p:"La première ligne trie les destinataires.",
       mots:[['On lit','Avis aux locataires · Avis aux occupants des logements 3 et 4'],['On cherche','son numéro de logement',true],['On lit quand même','le bruit ne lit pas les numéros']],
       say:"Un avis était affiché dans l'entrée.",
       note:"Si votre logement n'est pas nommé mais que les travaux sont dans l'immeuble, l'avis vous concerne indirectement — c'est souvent lui qui explique le bruit."},

      {t:'ana', h:"Les dates : trois données, jamais deux",
       p:"Un avis complet donne un début, une fin et une plage horaire.",
       mots:[['Le début','du mercredi 12 novembre'],['La fin','au vendredi 14 novembre',true],['Les heures','entre 8 h et 17 h']],
       say:"Les travaux auront lieu du 12 au 14 novembre, entre 8 h et 17 h.",
       note:"Un avis qui donne un jour sans heure est incomplet : vous avez le droit de demander la plage horaire, et de la demander par écrit."},

      {t:'ana', h:"L'obligation : la partie qui vous coûte du temps",
       p:"Elle est presque toujours écrite en tournure impersonnelle.",
       mots:[['On lit','Il est nécessaire que les occupants libèrent l\'accès.'],['Ça veut dire','tassez vos meubles le long de ce mur',true],['Autre forme','Veuillez prévoir un accès au logement.']],
       say:"Il est nécessaire que les occupants libèrent l'accès au mur touché.",
       note:"Traduisez toujours cette phrase-là dans vos mots, à la première personne : « je dois tasser le lit et la commode ». C'est ce que vous noterez sur votre fiche."},

      {t:'ana', h:"La conséquence : trois formules à reconnaître",
       p:"Elles annoncent ce qui arrivera si vous ne suivez pas la consigne.",
       mots:[['À défaut','si vous ne le faites pas'],['Le cas échéant','si ça se produit',true],['Faute de quoi','sinon']],
       say:"À défaut, l'entrepreneur communiquera avec le propriétaire.",
       note:"Ces trois-là sont le signal le plus utile de tout l'avis : elles marquent le paragraphe qui vous engage réellement."},

      {t:'ana', h:"Les lignes en petit",
       p:"C'est là que se trouve ce qui justifiera votre demande plus tard.",
       mots:[['Le bruit','Le bruit des appareils est important et continu.'],['La durée réelle','un second passage pourrait être planifié',true],['Les services','aucune interruption du service d\'eau n\'est prévue']],
       say:"Le bruit des appareils est important et continu.",
       note:"Ce sont ces lignes qui disent ce que les travaux vous enlèvent. Notez-les : trois nuits de sommeil sont un préjudice, et un préjudice se demande."},

      {t:'labo', h:"De la langue d'avis au français de tous les jours",
       p:"Choisissez une formule et voyez ce qu'elle dit vraiment.",
       axes:[{id:'a', lbl:'Quelle formule ?', opts:[
         ['a','Veuillez prévoir un accès au logement.'],
         ['b','À défaut, l\'entrepreneur communiquera avec le propriétaire.'],
         ['c','Il est nécessaire que les occupants libèrent l\'accès.'],
         ['d','Le cas échéant, un second passage sera planifié.'],
         ['e','Nous vous prions de nous aviser dans les meilleurs délais.']]}],
       out:{
         a:{w:["Arrangez-vous pour que quelqu'un puisse ouvrir."], say:"Veuillez prévoir un accès au logement.", n:"« veuillez » = l'impératif poli des écrits"},
         b:{w:["Si vous ne le faites pas, il appellera le propriétaire."], say:"À défaut, l'entrepreneur communiquera avec le propriétaire.", n:"la formule de conséquence"},
         c:{w:["Vous devez tasser vos meubles le long de ce mur."], say:"Il est nécessaire que les occupants libèrent l'accès.", n:"impersonnel + subjonctif"},
         d:{w:["Si ça arrive, on reviendra une autre fois."], say:"Le cas échéant, un second passage sera planifié.", n:"conséquence + passif"},
         e:{w:["Répondez-nous le plus vite possible."], say:"Nous vous prions de nous aviser dans les meilleurs délais.", n:"« dans les meilleurs délais » = vite, sans date précise"},
       },
       note:"« Dans les meilleurs délais » ne veut rien dire de précis. Si un délai compte pour vous, demandez une date."},

      {t:'ex', h:"À écouter et à répéter",
       p:"Six phrases d'avis, telles qu'elles s'écrivent.",
       rows:[
         ["Avis aux occupants des logements 3 et 4.","le destinataire"],
         ["Des travaux d'assèchement seront effectués du 12 au 14 novembre.","le passif"],
         ["Il est nécessaire que les occupants libèrent l'accès au mur touché.","l'obligation"],
         ["Veuillez prévoir un accès au logement entre 8 h et 17 h.","l'impératif poli"],
         ["À défaut, l'entrepreneur communiquera avec le propriétaire.","la conséquence"],
         ["Le bruit des appareils est important et continu.","la ligne en petit"],
       ]},

      {t:'piege', h:"Trois pièges à connaître",
       rows:[
         ["ne lire que le gros titre","« ah, des travaux »",
          "Le titre ne dit ni quand, ni ce que vous devez faire. Les deux tiers de l'information sont dans les six lignes du bas."],
         ["croire qu'un avis lu n'engage à rien","« je n'ai rien signé »",
          "Un avis lu sans réponse est un avis accepté. Si quelque chose ne vous convient pas, écrivez-le le jour même."],
         ["laisser passer « dans les meilleurs délais »","« ils vont s'en occuper »",
          "Cette formule n'est pas un délai. Demandez une date, par écrit, et gardez la réponse."],
       ]},

      {t:'check', h:"Est-ce que c'est clair maintenant ?",
       p:"Quatre questions rapides.",
       qs:[
         {q:"« À défaut » annonce…", opts:["ce qui arrivera si vous ne faites rien","une exception à la règle"], ok:0,
          fb:"C'est la formule de conséquence, comme « faute de quoi »."},
         {q:"« Veuillez prévoir un accès » veut dire…", opts:["quelqu'un doit pouvoir ouvrir","vous devez rester chez vous"], ok:0,
          fb:"Un voisin ou une clé peuvent suffire ; l'avis demande un accès, pas votre présence."},
         {q:"Les lignes en petit servent surtout à…", opts:["décorer","dire ce que les travaux vous enlèvent"], ok:1,
          fb:"Et c'est ce qui fonde une demande de compensation."},
         {q:"Un avis complet donne…", opts:["une date","un début, une fin et une plage horaire"], ok:1,
          fb:"Trois données. Sinon, demandez le reste par écrit."},
       ]},

      {t:'revoir', h:"À retenir en une ligne",
       p:"Un avis dit toujours trois choses : <b>ce qui va se passer</b>, <b>ce que vous devez faire</b>, <b>ce qui arrive si vous ne le faites pas</b>. La troisième commence par « à défaut », « le cas échéant » ou « faute de quoi »."},
    ]
  },

  t2imperso: {
    eye:'Mini-leçon', tit:"« Il est nécessaire de… » : la langue des avis",
    blocs:[
      {t:'texte', h:"Pourquoi un avis ne dit jamais « vous devez »",
       p:"Un avis officiel évite de désigner qui commande et qui obéit. Il présente l'obligation comme si elle venait de la situation elle-même : « il est nécessaire de », « les travaux seront effectués », « veuillez prévoir ». Personne ne s'adresse à personne, et pourtant vous êtes tenu de faire quelque chose. Ces trois tournures — <b>l'impersonnel</b>, <b>le passif</b>, <b>« veuillez »</b> — sont la charpente de tout document administratif au Québec.",
       note:"Savoir les lire vous protège ; savoir les écrire vous ouvre des portes. Une lettre de locataire rédigée dans cette langue-là est lue autrement qu'un message de colère."},

      {t:'ana', h:"La phrase impersonnelle",
       p:"Le sujet « il » ne désigne personne : il occupe la place, rien de plus.",
       mots:[['Obligation','Il est nécessaire de libérer l\'accès.'],['Interdiction','Il est interdit de fumer dans les corridors.',true],['Constat','Il y aura du bruit pendant trois jours.']],
       say:"Il est nécessaire de libérer l'accès au mur touché.",
       note:"Suivi de <b>de</b> + infinitif quand personne n'est visé ; suivi de <b>que</b> + subjonctif quand on précise qui : « il est nécessaire que <b>vous</b> libériez »."},

      {t:'ana', h:"Le passif",
       p:"On dit ce qui sera fait sans dire par qui.",
       mots:[['Formation','être au temps voulu + participe passé'],['Futur','Les travaux seront effectués du 12 au 14.',true],['Accord','Vous serez avisés — le participe s\'accorde avec le sujet']],
       say:"Des travaux d'assèchement seront effectués du 12 au 14 novembre.",
       note:"Le passif est utile aussi dans vos lettres : « aucune réponse ne m'a été transmise » est plus ferme et moins accusateur que « vous ne m'avez pas répondu »."},

      {t:'ana', h:"« Veuillez » + infinitif",
       p:"L'impératif poli des documents écrits.",
       mots:[['On écrit','Veuillez prévoir un accès au logement.'],['Autre exemple','Veuillez nous aviser de votre disponibilité.',true],['Il ne se conjugue pas','« veuillez », et rien d\'autre']],
       say:"Veuillez prévoir un accès au logement.",
       note:"C'est la forme la plus courtoise et la plus neutre pour demander quelque chose par écrit. Elle ne vieillit pas et ne choque personne."},

      {t:'ana', h:"Les trois formules de conséquence",
       p:"Elles introduisent ce qui arrive si la consigne n'est pas suivie.",
       mots:[['À défaut','si vous ne le faites pas'],['Faute de quoi','sinon',true],['Le cas échéant','si le cas se présente']],
       say:"À défaut, l'entrepreneur communiquera avec le propriétaire.",
       note:"Employez-les dans vos propres lettres : « Faute de réponse d'ici le 30 novembre, je transmettrai le dossier. » C'est ferme sans être menaçant."},

      {t:'labo', h:"Du parlé à l'écrit administratif",
       p:"Choisissez une phrase de tous les jours et voyez comment un avis l'écrirait.",
       axes:[{id:'i', lbl:'Quelle phrase ?', opts:[
         ['a','Vous devez libérer l\'accès au mur.'],
         ['b','On fera les travaux du 12 au 14.'],
         ['c','Ne fumez pas dans les corridors.'],
         ['d','Prévoyez un accès, s\'il vous plaît.'],
         ['e','Si vous ne le faites pas, on appellera le propriétaire.'],
         ['f','On vous préviendra la veille.']]}],
       out:{
         a:{w:["Il est nécessaire de libérer l'accès au mur."], say:"Il est nécessaire de libérer l'accès au mur.", n:"impersonnel + de + infinitif"},
         b:{w:["Les travaux seront effectués du 12 au 14."], say:"Les travaux seront effectués du 12 au 14 novembre.", n:"passif au futur"},
         c:{w:["Il est interdit de fumer dans les corridors."], say:"Il est interdit de fumer dans les corridors.", n:"impersonnel d'interdiction"},
         d:{w:["Veuillez prévoir un accès au logement."], say:"Veuillez prévoir un accès au logement.", n:"l'impératif poli"},
         e:{w:["À défaut, nous communiquerons avec le propriétaire."], say:"À défaut, nous communiquerons avec le propriétaire.", n:"formule de conséquence"},
         f:{w:["Vous serez avisés la veille."], say:"Vous serez avisés vingt-quatre heures d'avance.", n:"passif, participe accordé"},
       },
       note:"Remarquez que la version administrative n'est jamais plus longue. Elle est seulement plus impersonnelle."},

      {t:'ex', h:"À écouter et à répéter",
       p:"Six phrases à réutiliser dans vos propres lettres.",
       rows:[
         ["Il est nécessaire de libérer l'accès au mur touché.","impersonnel"],
         ["Les travaux seront effectués du 12 au 14 novembre.","passif"],
         ["Veuillez prévoir un accès au logement.","impératif poli"],
         ["Vous serez avisés vingt-quatre heures d'avance.","passif accordé"],
         ["À défaut, nous communiquerons avec le propriétaire.","conséquence"],
         ["Aucune réponse ne m'a été transmise à ce jour.","passif, dans une lettre de locataire"],
       ]},

      {t:'piege', h:"Trois pièges à connaître",
       rows:[
         ["conjuguer « veuillez »","« veux-tu prévoir », « veuilles »",
          "Cette forme est figée : « veuillez », toujours, et rien d'autre."],
         ["oublier l'accord du participe au passif","« vous serez avisé » pour plusieurs personnes",
          "Le participe s'accorde avec le sujet : vous serez avisés, les travaux seront effectués, la porte sera ouverte."],
         ["croire que l'impersonnel est plus faible","« ce n'est pas vraiment une obligation »",
          "Au contraire : « il est interdit de » a exactement la même force que « vous ne devez pas », en plus difficile à discuter."],
       ]},

      {t:'check', h:"Est-ce que c'est clair maintenant ?",
       p:"Quatre questions rapides.",
       qs:[
         {q:"Dans « il est nécessaire de partir », « il » désigne…", opts:["personne","le propriétaire"], ok:0,
          fb:"C'est un sujet impersonnel : il occupe la place, sans désigner quelqu'un."},
         {q:"« Les travaux seront effectués » est…", opts:["un passif","un impersonnel"], ok:0,
          fb:"être + participe passé : on dit ce qui sera fait sans dire par qui."},
         {q:"« Veuillez » se conjugue-t-il ?", opts:["oui","non"], ok:1,
          fb:"La forme est figée."},
         {q:"« Faute de quoi » veut dire…", opts:["sinon","par erreur"], ok:0,
          fb:"C'est une formule de conséquence, comme « à défaut »."},
       ]},

      {t:'revoir', h:"À retenir en une ligne",
       p:"Trois tournures tiennent tout document administratif : <b>il est nécessaire de</b> (l'impersonnel), <b>seront effectués</b> (le passif), <b>veuillez</b> (l'impératif poli). Et « à défaut » annonce la suite."},
    ]
  },

  t2subj: {
    eye:'Mini-leçon', tit:"Le subjonctif présent, et quand il est obligatoire",
    blocs:[
      {t:'texte', h:"Un mode qu'on n'utilise jamais tout seul",
       p:"Le subjonctif n'apparaît pas au début d'une phrase : il vient <b>après un mot qui l'appelle</b>. « Il faut que », « pour que », « avant que » : ce sont ces mots-là qu'il faut connaître, pas le mode lui-même. Apprenez la liste des déclencheurs, et le subjonctif se met tout seul.",
       note:"Bonne nouvelle : au niveau 5, quatre déclencheurs suffisent pour la vie courante, et ils reviennent tous dans les avis et les lettres du logement."},

      {t:'ana', h:"Comment il se forme",
       p:"À partir de la forme « ils » du présent.",
       mots:[['On prend « ils »','ils libèr-ent'],['On enlève -ent, on ajoute -e, -es, -e, -ions, -iez, -ent','que je libère',true],['Le « que » fait partie du paquet','que je libère, que tu libères, qu\'il libère']],
       say:"Il est nécessaire que les occupants libèrent l'accès.",
       note:"Pour beaucoup de verbes, la forme du subjonctif ressemble à celle du présent. Ce n'est pas un problème : ce qui compte, c'est qu'elle soit juste."},

      {t:'ana', h:"Les quatre irréguliers à connaître",
       p:"Ceux-là s'apprennent par cœur, et ils reviennent partout.",
       mots:[['être','que je sois · que nous soyons'],['avoir','que j\'aie · que nous ayons',true],['faire','que je fasse'],['aller','que j\'aille · que nous allions']],
       say:"Il faut que vous soyez présent mercredi matin.",
       note:"Un cinquième, plus rare mais utile ici : pouvoir → que je puisse. « Pour que les ouvriers puissent travailler. »"},

      {t:'ana', h:"Déclencheur 1 : l'obligation",
       p:"Il faut que, il est nécessaire que, il est important que.",
       mots:[['On dit','Il faut que vous soyez présent.'],['Autre','Il est nécessaire que les occupants libèrent l\'accès.',true],['Ce n\'est pas un choix','ces trois-là appellent toujours le subjonctif']],
       say:"Il faut que vous soyez présent mercredi matin.",
       note:"C'est le déclencheur le plus fréquent des avis de travaux et des lettres d'école."},

      {t:'ana', h:"Déclencheur 2 : le but",
       p:"Pour que, afin que.",
       mots:[['On dit','Tassez le lit pour que les ouvriers puissent travailler.'],['Plus formel','afin que tout aille vite',true],['Différence avec « pour »','« pour » + infinitif quand c\'est le même sujet']],
       say:"Tassez la commode pour que les ouvriers puissent travailler.",
       note:"Même sujet : « Je tasse le lit <b>pour libérer</b> le mur. » Sujets différents : « Je tasse le lit <b>pour que les ouvriers puissent</b> travailler. »"},

      {t:'ana', h:"Déclencheur 3 : avant que — et le piège d'après que",
       p:"Ce qui n'est pas encore arrivé demande le subjonctif ; ce qui est fini, non.",
       mots:[['Avant que','Prenez vos photos avant que tout sèche.'],['Après que','Après qu\'il est parti, j\'ai tout rangé. — indicatif',true],['La logique','ce qui est fini est réel ; ce qui vient est incertain']],
       say:"Prenez vos photos avant que la tache sèche.",
       note:"« Après que » suivi du subjonctif est une faute très répandue, y compris chez les locuteurs natifs. Vous, vous saurez pourquoi."},

      {t:'ana', h:"La règle des deux sujets",
       p:"Le subjonctif ne sert que si les deux verbes ont des sujets différents.",
       mots:[['Deux sujets','Il faut que vous libériez l\'accès.'],['Un seul sujet','Il faut libérer l\'accès. — infinitif',true],['Même chose avec le but','pour libérer / pour que vous libériez']],
       say:"Il faut que vous libériez l'accès au mur.",
       note:"Cette règle vous évite la moitié des subjonctifs : quand il n'y a personne de précis, l'infinitif suffit et il est plus simple."},

      {t:'labo', h:"Conjuguez",
       p:"Choisissez un verbe et voyez sa forme au subjonctif dans une phrase du module.",
       axes:[{id:'v', lbl:'Quel verbe ?', opts:[
         ['a','être'],
         ['b','avoir'],
         ['c','faire'],
         ['d','aller'],
         ['e','pouvoir'],
         ['f','libérer'],
         ['g','prendre']]}],
       out:{
         a:{w:['que je sois · que vous soyez'], say:"Il faut que vous soyez présent mercredi matin.", n:"irrégulier"},
         b:{w:["que j'aie · que nous ayons"], say:"Il faut que j'aie une réponse écrite du propriétaire.", n:"irrégulier"},
         c:{w:['que je fasse · que nous fassions'], say:"Il est important que nous fassions constater les dommages.", n:"irrégulier"},
         d:{w:["que j'aille · que tout aille"], say:"Afin que tout aille vite, laissez une clé à la voisine.", n:"irrégulier"},
         e:{w:['que je puisse · qu\'ils puissent'], say:"Tassez la commode pour que les ouvriers puissent travailler.", n:"irrégulier, très utile"},
         f:{w:['que je libère · qu\'ils libèrent'], say:"Il est nécessaire que les occupants libèrent l'accès.", n:"régulier : ils libèrent → que je libère"},
         g:{w:['que je prenne · qu\'il prenne'], say:"Il faut que le propriétaire prenne une décision cette semaine.", n:"régulier : ils prennent → qu'il prenne"},
       },
       note:"Les cinq premiers sont à apprendre par cœur ; les deux derniers se déduisent de la forme « ils »."},

      {t:'ex', h:"À écouter et à répéter",
       p:"Six phrases du module.",
       rows:[
         ["Il faut que vous soyez présent mercredi matin.","obligation"],
         ["Il est nécessaire que les occupants libèrent l'accès.","obligation"],
         ["Tassez la commode pour que les ouvriers puissent travailler.","but"],
         ["Prenez vos photos avant que la tache sèche.","avant que"],
         ["Il est important que nous fassions constater les dommages.","obligation"],
         ["Il faut que j'aie une réponse écrite du propriétaire.","obligation"],
       ]},

      {t:'piege', h:"Trois pièges à connaître",
       rows:[
         ["mettre le subjonctif après « après que »","« après qu'il soit parti »",
          "Non : ce qui est fini est réel, donc indicatif. « Après qu'il est parti. » Beaucoup de gens se trompent ; ce n'en est pas moins une faute."],
         ["employer le subjonctif avec un seul sujet","« il faut que je libère l'accès » quand personne n'est visé",
          "Quand il n'y a pas de sujet précis, l'infinitif suffit : « il faut libérer l'accès ». Plus court, plus sûr."],
         ["oublier « que »","« il faut vous soyez là »",
          "Le « que » n'est pas facultatif : il fait partie du déclencheur."],
       ]},

      {t:'check', h:"Est-ce que c'est clair maintenant ?",
       p:"Quatre questions rapides.",
       qs:[
         {q:"Le subjonctif se forme à partir de…", opts:["la forme « ils » du présent","l'infinitif"], ok:0,
          fb:"ils libèrent → que je libère."},
         {q:"« Après que » demande…", opts:["le subjonctif","l'indicatif"], ok:1,
          fb:"Ce qui est fini est réel : indicatif."},
         {q:"« pour que » et « pour » se distinguent par…", opts:["le nombre de sujets","le niveau de langue"], ok:0,
          fb:"Un seul sujet : pour + infinitif. Deux sujets : pour que + subjonctif."},
         {q:"« que je puisse » est le subjonctif de…", opts:["pouvoir","poser"], ok:0,
          fb:"Irrégulier, et très fréquent dans les demandes."},
       ]},

      {t:'revoir', h:"À retenir en une ligne",
       p:"Quatre déclencheurs : <b>il faut que</b>, <b>il est nécessaire que</b>, <b>pour que</b>, <b>avant que</b>. Quatre irréguliers : <b>sois</b>, <b>aie</b>, <b>fasse</b>, <b>aille</b>. Un seul sujet ? l'infinitif suffit."},
    ]
  },

  t3emph: {
    eye:'Mini-leçon', tit:"Mettre en avant : « c'est… qui », « ce que…, c'est »",
    blocs:[
      {t:'texte', h:"À l'oral, la voix ; à l'écrit, une tournure",
       p:"Quand vous parlez, vous appuyez sur le mot important et tout le monde comprend ce qui compte. À l'écrit, la voix ne passe pas : il faut une construction. Le français en a trois, et elles servent exactement à ça — <b>encadrer le mot important</b> pour qu'on ne puisse pas le manquer. C'est ce que le programme du niveau 5 appelle la phrase emphatique.",
       note:"Dans une lettre de réclamation, elles sont l'outil le plus utile que vous ayez : elles disent ce qui compte sans hausser le ton."},

      {t:'ana', h:"c'est … qui — pour mettre en avant le sujet",
       p:"Ce qui fait l'action.",
       mots:[['À plat','Le chauffe-eau a lâché.'],['En avant','C\'est le chauffe-eau qui a lâché.',true],['Avec un pronom','C\'est moi qui ai appelé.']],
       say:"C'est le chauffe-eau du logement du dessus qui a lâché.",
       note:"Le verbe qui suit s'accorde avec ce qu'on encadre : « c'est moi qui <b>ai</b> appelé », et non « qui a appelé »."},

      {t:'ana', h:"c'est … que — pour mettre en avant tout le reste",
       p:"Le complément, le lieu, le moment.",
       mots:[['Le complément','C\'est le propriétaire que j\'ai appelé.'],['Le moment','C\'est le 10 novembre que le dégât est arrivé.',true],['Le lieu','C\'est dans la chambre que l\'eau tombait.']],
       say:"C'est pendant la nuit que le dégât est arrivé.",
       note:"« qui » si le mot encadré fait l'action, « que » dans tous les autres cas. C'est le seul choix à faire."},

      {t:'ana', h:"ce qui / ce que …, c'est",
       p:"La forme la plus forte, et celle qui ouvre bien une lettre.",
       mots:[['Sujet','Ce qui m\'inquiète, c\'est l\'humidité dans le matelas.'],['Complément','Ce que je demande, c\'est une réduction de loyer.',true],['La virgule','elle est obligatoire avant « c\'est »']],
       say:"Ce que je demande, c'est une réduction de loyer pour trois nuits.",
       note:"Cette tournure fait attendre l'information : le lecteur arrive à « c'est » en sachant qu'il va apprendre l'essentiel."},

      {t:'ana', h:"La dislocation, à l'oral",
       p:"On sort le mot, et on le reprend par un pronom.",
       mots:[['On dit','Le plafond, il coule encore.'],['Ou dans l\'autre sens','Je ne l\'ai pas jeté, mon matelas.',true],['La virgule','elle marque la pause qu\'on entend']],
       say:"Mon matelas, je ne l'ai pas jeté.",
       note:"C'est du français parlé tout à fait correct, très fréquent au Québec. À l'écrit, on lui préfère les trois tournures précédentes."},

      {t:'labo', h:"La même phrase, mise en avant autrement",
       p:"Choisissez ce que vous voulez mettre en avant dans « Le chauffe-eau du dessus a lâché pendant la nuit ».",
       axes:[{id:'e', lbl:'On met en avant…', opts:[
         ['a','le chauffe-eau'],
         ['b','pendant la nuit'],
         ['c','ce qui inquiète'],
         ['d','ce qu\'on demande'],
         ['e','la personne qui a appelé']]}],
       out:{
         a:{w:["C'est le chauffe-eau du dessus qui a lâché."], say:"C'est le chauffe-eau du logement du dessus qui a lâché.", n:"sujet → qui"},
         b:{w:["C'est pendant la nuit que le dégât est arrivé."], say:"C'est pendant la nuit que le dégât est arrivé.", n:"moment → que"},
         c:{w:["Ce qui m'inquiète, c'est l'humidité dans le matelas."], say:"Ce qui m'inquiète, c'est l'humidité dans le matelas.", n:"ce qui …, c'est"},
         d:{w:["Ce que je demande, c'est une réduction de loyer."], say:"Ce que je demande, c'est une réduction de loyer pour trois nuits.", n:"ce que …, c'est"},
         e:{w:["C'est moi qui ai appelé le propriétaire."], say:"C'est moi qui ai appelé le propriétaire à six heures et demie.", n:"accord du verbe avec « moi »"},
       },
       note:"Cinq façons de dire la même histoire, cinq messages différents. Choisissez selon ce que vous voulez qu'on retienne."},

      {t:'ex', h:"À écouter et à répéter",
       p:"Six phrases pour une lettre de réclamation.",
       rows:[
         ["C'est le chauffe-eau du dessus qui a lâché.","le sujet"],
         ["C'est pendant la nuit que le dégât est arrivé.","le moment"],
         ["Ce qui m'inquiète, c'est l'humidité dans le matelas.","ce qui …, c'est"],
         ["Ce que je demande, c'est une réduction de loyer.","ce que …, c'est"],
         ["C'est moi qui ai appelé le propriétaire.","accord avec « moi »"],
         ["Ce qui m'empêche de dormir, c'est le bruit des appareils.","ce qui …, c'est"],
       ]},

      {t:'piege', h:"Trois pièges à connaître",
       rows:[
         ["se tromper de « qui » ou « que »","« c'est le chauffe-eau que a lâché »",
          "Si le mot encadré fait l'action, c'est « qui ». Sinon, « que ». Une seule question à se poser."],
         ["oublier l'accord après « c'est moi qui »","« c'est moi qui a appelé »",
          "Le verbe s'accorde avec « moi » : c'est moi qui <b>ai</b> appelé, c'est nous qui <b>avons</b> écrit."],
         ["empiler deux emphases","« Ce que je demande, c'est que c'est une réduction »",
          "Une seule par phrase. Deux s'annulent et rendent la phrase illisible."],
       ]},

      {t:'check', h:"Est-ce que c'est clair maintenant ?",
       p:"Quatre questions rapides.",
       qs:[
         {q:"Pour mettre en avant le sujet, on emploie…", opts:["c'est … qui","c'est … que"], ok:0,
          fb:"« qui » quand le mot encadré fait l'action."},
         {q:"« C'est moi qui … appelé » se complète par…", opts:["a","ai"], ok:1,
          fb:"Le verbe s'accorde avec « moi »."},
         {q:"« Ce que je demande, c'est… » sert surtout à…", opts:["ouvrir une demande","conclure poliment"], ok:0,
          fb:"C'est la tournure qui annonce l'essentiel."},
         {q:"« Mon matelas, je ne l'ai pas jeté » est…", opts:["une faute","du français parlé correct"], ok:1,
          fb:"C'est une dislocation, très courante à l'oral."},
       ]},

      {t:'revoir', h:"À retenir en une ligne",
       p:"<b>c'est … qui</b> pour le sujet, <b>c'est … que</b> pour le reste, <b>ce qui/ce que …, c'est</b> pour l'essentiel d'une lettre. Une seule emphase par phrase."},
    ]
  },

  t3conn: {
    eye:'Mini-leçon', tit:"Cause et conséquence : les mots qui font tenir une demande",
    blocs:[
      {t:'texte', h:"Une demande, c'est un raisonnement en trois temps",
       p:"« J'ai perdu trois nuits de sommeil. Ce n'est pas de ma faute. Je demande une compensation. » Trois phrases posées côte à côte ne font pas une argumentation : ce sont les <b>connecteurs</b> qui les relient et qui montrent que la troisième découle des deux premières. Sans eux, le lecteur doit faire le travail lui-même — et il ne le fera pas.",
       note:"C'est exactement ce que le programme du niveau 5 appelle un discours simple mais <b>organisé</b> : des phrases liées entre elles, pas des phrases alignées."},

      {t:'ana', h:"La cause qu'on suppose connue",
       p:"puisque · étant donné que · comme",
       mots:[['On écrit','Étant donné que la fuite venait d\'en haut, je ne suis pas responsable.'],['Ce que ça fait','présente la raison comme non discutable',true],['« comme »','toujours en tête de phrase']],
       say:"Étant donné que la fuite venait du logement du dessus, je ne suis pas responsable.",
       note:"C'est le connecteur de la première partie d'une lettre : vous rappelez un fait que le destinataire connaît déjà."},

      {t:'ana', h:"La cause qu'on apporte comme information",
       p:"parce que · car",
       mots:[['On écrit','Je n\'ai pas dormi dans ma chambre parce que le matelas était humide.'],['Ce que ça fait','répond à « pourquoi ? »',true],['« car »','plus écrit, jamais en tête de phrase']],
       say:"Je n'ai pas dormi dans ma chambre parce que le matelas était humide.",
       note:"Différence avec « puisque » : « parce que » apprend quelque chose au lecteur, « puisque » lui rappelle ce qu'il sait."},

      {t:'ana', h:"La conséquence",
       p:"c'est pourquoi · par conséquent · donc",
       mots:[['On écrit','Le logement était inutilisable ; par conséquent, je demande une réduction.'],['Sa place','juste avant la demande',true],['« donc »','plus léger, très bien à l\'oral']],
       say:"Par conséquent, je demande une réduction de loyer équivalant à trois jours.",
       note:"C'est le connecteur de la demande elle-même. Il annonce au lecteur que ce qui suit est ce que vous voulez."},

      {t:'ana', h:"Le deux-points qui explique",
       p:"Une ponctuation qui remplace un connecteur entier.",
       mots:[['On écrit','Je n\'ai rien jeté : je voulais tout faire constater.'],['Ce que ça vaut','« parce que », en plus net',true],['Attention','ici il annonce une cause, pas une liste']],
       say:"Je n'ai rien jeté : je voulais tout faire constater.",
       note:"Le programme du niveau 5 attend précisément ce deux-points-là — celui qui précède une cause ou une explication."},

      {t:'ana', h:"La virgule après une cause en tête de phrase",
       p:"Quand la subordonnée vient d'abord, une virgule ferme le morceau.",
       mots:[['On écrit','Comme la fuite venait d\'en haut, j\'ai averti ma voisine.'],['Sans virgule','la phrase se lit deux fois',true],['Si la cause vient après','pas de virgule : j\'ai averti ma voisine parce que…']],
       say:"Comme la fuite venait d'en haut, j'ai averti ma voisine avant le propriétaire.",
       note:"Cette virgule n'est pas décorative : elle est attendue à l'évaluation de fin de cours."},

      {t:'labo', h:"Assemblez une argumentation",
       p:"Choisissez une pièce de la lettre de Mariama.",
       axes:[{id:'c', lbl:'Quelle pièce ?', opts:[
         ['a','le rappel des faits'],
         ['b','la cause connue'],
         ['c','la cause expliquée'],
         ['d','l\'explication au deux-points'],
         ['e','la demande']]}],
       out:{
         a:{w:["Le 10 novembre au matin, un dégât d'eau est survenu dans ma chambre."], say:"Le 10 novembre au matin, un dégât d'eau est survenu dans ma chambre.", n:"daté, au passé composé"},
         b:{w:["Étant donné que la cause se trouvait dans un autre logement, je ne suis pas responsable."], say:"Étant donné que la cause se trouvait dans un autre logement, je ne suis pas responsable.", n:"cause connue + virgule"},
         c:{w:["Je n'ai pas pu occuper ma chambre parce que les appareils tournaient jour et nuit."], say:"Je n'ai pas pu occuper ma chambre parce que les appareils tournaient jour et nuit.", n:"cause apportée comme information"},
         d:{w:["Je n'ai rien jeté : je voulais tout faire constater."], say:"Je n'ai rien jeté : je voulais tout faire constater.", n:"le deux-points explicatif"},
         e:{w:["Par conséquent, je demande une réduction de loyer équivalant à trois jours."], say:"Par conséquent, je demande une réduction de loyer équivalant à trois jours.", n:"la conséquence, juste avant le chiffre"},
       },
       note:"Lisez les cinq pièces à la suite : vous avez une lettre complète, et elle tient debout toute seule."},

      {t:'ex', h:"À écouter et à répéter",
       p:"Six phrases liées, à reprendre telles quelles.",
       rows:[
         ["Étant donné que la fuite venait d'en haut, je ne suis pas responsable.","cause connue"],
         ["Comme personne ne répondait, j'ai appelé un plombier d'urgence.","cause connue, en tête"],
         ["Je n'ai pas dormi dans ma chambre parce que le matelas était humide.","cause expliquée"],
         ["Je n'ai rien jeté : je voulais tout faire constater.","le deux-points"],
         ["Le logement était inutilisable ; par conséquent, je demande une réduction.","conséquence"],
         ["La cause a été confirmée par un plombier ; je vous demande donc de me répondre.","conséquence légère"],
       ]},

      {t:'piege', h:"Trois pièges à connaître",
       rows:[
         ["empiler les connecteurs","« Comme… parce que… donc… par conséquent… »",
          "Une cause, une conséquence, puis on change de phrase. Trois connecteurs dans une phrase font un paragraphe illisible."],
         ["oublier la virgule de la cause en tête","« Comme la fuite venait d'en haut j'ai averti… »",
          "La virgule ferme la subordonnée. Sans elle, on lit « d'en haut j'ai » et il faut recommencer."],
         ["employer le deux-points pour une liste ici","« J'ai perdu : un matelas, une commode »",
          "Ce n'est pas faux, mais ce n'est pas ce qu'on travaille : le deux-points attendu au niveau 5 est celui qui annonce une cause ou une explication."],
       ]},

      {t:'check', h:"Est-ce que c'est clair maintenant ?",
       p:"Quatre questions rapides.",
       qs:[
         {q:"« Puisque » présente une cause…", opts:["que le lecteur connaît déjà","qu'on lui apprend"], ok:0,
          fb:"« parce que » apprend, « puisque » rappelle."},
         {q:"« Par conséquent » se place…", opts:["juste avant la demande","au début de la lettre"], ok:0,
          fb:"C'est le connecteur qui annonce ce que vous voulez."},
         {q:"Dans « Je n'ai rien jeté : je voulais tout faire constater », le deux-points vaut…", opts:["« et »","« parce que »"], ok:1,
          fb:"Il annonce une cause ou une explication."},
         {q:"Après une cause placée en tête de phrase, il faut…", opts:["une virgule","rien"], ok:0,
          fb:"La virgule ferme la subordonnée, et elle est attendue à l'évaluation."},
       ]},

      {t:'revoir', h:"À retenir en une ligne",
       p:"<b>Étant donné que</b> rappelle, <b>parce que</b> explique, <b>par conséquent</b> demande, et le <b>deux-points</b> remplace un « parce que » en plus net. Virgule obligatoire après une cause en tête de phrase."},
    ]
  },

  t3lettre: {
    eye:'Mini-leçon', tit:"Écrire une demande qui aboutit",
    blocs:[
      {t:'texte', h:"Une lettre de demande n'est pas une lettre de colère",
       p:"Vous avez raison, et ça ne suffit pas. Une demande obtient une réponse quand elle est <b>facile à traiter</b> : des faits datés, un montant, une date limite. Le destinataire doit pouvoir dire oui en trente secondes. Tout ce qui l'oblige à réfléchir, à chercher ou à se défendre travaille contre vous.",
       note:"C'est aussi ce qui rend la lettre utile plus tard : si l'affaire va plus loin, un juge administratif lira exactement les mêmes cinq éléments."},

      {t:'ana', h:"Partie 1 — les faits, datés",
       p:"Deux phrases, pas trois.",
       mots:[['On écrit','Le 10 novembre au matin, un dégât d\'eau est survenu dans ma chambre.'],['Puis','La fuite provenait du chauffe-eau du logement situé au-dessus du mien.',true],['Les temps','passé composé pour l\'événement, imparfait pour l\'état']],
       say:"Le 10 novembre au matin, un dégât d'eau est survenu dans ma chambre.",
       note:"La date en tête de phrase. C'est la première chose que cherche celui qui lit."},

      {t:'ana', h:"Partie 2 — ce que vous avez perdu, chiffré",
       p:"Une durée, une pièce, un usage empêché.",
       mots:[['On écrit','Les travaux ont duré trois jours, pendant lesquels je n\'ai pas pu occuper ma chambre.'],['Toujours un chiffre','trois jours, trois nuits, un tiers du logement',true],['Jamais','« très longtemps », « c\'était terrible »']],
       say:"Les travaux ont duré trois jours, pendant lesquels je n'ai pas pu occuper ma chambre.",
       note:"« Pendant lesquels » est la tournure exacte pour relier une durée à ce qu'elle vous a coûté. Elle vaut la peine d'être apprise telle quelle."},

      {t:'ana', h:"Partie 3 — la cause, sans accuser",
       p:"Vous établissez que vous n'y êtes pour rien.",
       mots:[['On écrit','Étant donné que la cause se trouvait dans un autre logement, je ne suis pas responsable des dommages.'],['Ce qu\'on évite','« c\'est votre faute », « vous avez négligé »',true],['Pourquoi','une personne accusée se défend au lieu de payer']],
       say:"Étant donné que la cause se trouvait dans un autre logement, je ne suis pas responsable des dommages.",
       note:"Le ton neutre n'est pas de la faiblesse : c'est ce qui laisse à l'autre la possibilité d'accepter sans perdre la face."},

      {t:'ana', h:"Partie 4 — la demande, chiffrée",
       p:"Un montant ou une proportion, et la période.",
       mots:[['On écrit','Par conséquent, je demande une réduction de loyer équivalant à trois jours, soit 90 $.'],['Comment calculer','le loyer mensuel divisé par 30, multiplié par le nombre de jours',true],['Sans chiffre','on vous répondra « on verra »']],
       say:"Par conséquent, je demande une réduction de loyer équivalant à trois jours, soit 90 $.",
       note:"Une demande chiffrée force une réponse chiffrée. C'est le seul moyen de sortir du vague."},

      {t:'ana', h:"Partie 5 — le délai, et la suite annoncée",
       p:"Une date, et ce qui se passera après.",
       mots:[['On écrit','Je vous saurais gré de me répondre avant le 30 novembre.'],['Si besoin','Faute de réponse, je transmettrai le dossier au Tribunal administratif du logement.',true],['Ce n\'est pas une menace','c\'est une information']],
       say:"Je vous saurais gré de me répondre avant le 30 novembre.",
       note:"Annoncer la suite calmement est plus efficace que menacer : la phrase reste vraie, et elle se relit bien."},

      {t:'labo', h:"La lettre, partie par partie",
       p:"Choisissez une partie et voyez la phrase modèle.",
       axes:[{id:'l', lbl:'Quelle partie ?', opts:[
         ['a','les faits'],
         ['b','ce que j\'ai perdu'],
         ['c','la cause'],
         ['d','la demande'],
         ['e','le délai']]}],
       out:{
         a:{w:["Le 10 novembre au matin, un dégât d'eau est survenu dans ma chambre."], say:"Le 10 novembre au matin, un dégât d'eau est survenu dans ma chambre.", n:"date en tête"},
         b:{w:["Les travaux ont duré trois jours, pendant lesquels je n'ai pas pu occuper ma chambre."], say:"Les travaux ont duré trois jours, pendant lesquels je n'ai pas pu occuper ma chambre.", n:"une durée chiffrée"},
         c:{w:["Étant donné que la cause se trouvait dans un autre logement, je ne suis pas responsable."], say:"Étant donné que la cause se trouvait dans un autre logement, je ne suis pas responsable.", n:"cause, sans accusation"},
         d:{w:["Par conséquent, je demande une réduction de loyer équivalant à trois jours, soit 90 $."], say:"Par conséquent, je demande une réduction de loyer équivalant à trois jours, soit 90 $.", n:"un montant"},
         e:{w:["Je vous saurais gré de me répondre avant le 30 novembre."], say:"Je vous saurais gré de me répondre avant le 30 novembre.", n:"une date limite"},
       },
       note:"Cinq phrases, cinq lignes. Une lettre de demande efficace n'a pas besoin d'être longue."},

      {t:'ex', h:"À écouter et à répéter",
       p:"Les cinq phrases de la lettre, plus la formule d'ouverture.",
       rows:[
         ["Monsieur, je fais suite au dégât d'eau survenu dans mon logement.","l'ouverture"],
         ["Le 10 novembre au matin, un dégât d'eau est survenu dans ma chambre.","les faits"],
         ["Les travaux ont duré trois jours, pendant lesquels je n'ai pas pu occuper ma chambre.","la perte"],
         ["Étant donné que la cause se trouvait dans un autre logement, je ne suis pas responsable.","la cause"],
         ["Par conséquent, je demande une réduction de loyer équivalant à trois jours, soit 90 $.","la demande"],
         ["Je vous saurais gré de me répondre avant le 30 novembre.","le délai"],
       ]},

      {t:'piege', h:"Trois pièges à connaître",
       rows:[
         ["raconter au lieu de demander","trois paragraphes de récit et pas de demande",
          "Le destinataire cherche ce que vous voulez. S'il ne le trouve pas en dix secondes, il classe la lettre."],
         ["demander sans chiffre","« une compensation raisonnable »",
          "Personne ne chiffrera à votre place, et « raisonnable » ne veut rien dire. Calculez : loyer ÷ 30 × nombre de jours."],
         ["menacer dès la première lettre","« sinon j'irai au Tribunal »",
          "Gardez cette phrase pour la mise en demeure, qui vient après. Une menace envoyée trop tôt durcit tout de suite la discussion."],
       ]},

      {t:'check', h:"Est-ce que c'est clair maintenant ?",
       p:"Quatre questions rapides.",
       qs:[
         {q:"Une demande de réduction de loyer s'adresse…", opts:["à votre assureur","au propriétaire"], ok:1,
          fb:"L'assureur couvre vos biens ; la réduction de loyer se demande au propriétaire."},
         {q:"Le montant demandé se calcule…", opts:["au jugé","loyer ÷ 30 × nombre de jours"], ok:1,
          fb:"Un calcul simple, et vérifiable par l'autre partie."},
         {q:"« Je vous saurais gré de me répondre avant le 30 » sert à…", opts:["fixer un délai","remercier"], ok:0,
          fb:"C'est la formule courtoise pour poser une date limite."},
         {q:"La menace d'aller au Tribunal a sa place…", opts:["dès la première lettre","dans la mise en demeure"], ok:1,
          fb:"Chaque étape a son ton ; on ne brûle pas la première."},
       ]},

      {t:'revoir', h:"À retenir en une ligne",
       p:"Cinq lignes : <b>les faits datés</b>, <b>la perte chiffrée</b>, <b>la cause sans accusation</b>, <b>la demande avec un montant</b>, <b>le délai</b>. Rien de plus."},
    ]
  },
};
