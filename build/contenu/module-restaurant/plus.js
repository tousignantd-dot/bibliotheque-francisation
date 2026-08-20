const PLUS = {
  prPhon: {
    eye:'Mini-leçon', tit:"Le « e » qui tombe",
    blocs:[
      {t:'texte', h:"Pourquoi le serveur parle si vite",
       p:"« Qu'est-ce que vous prenez ? » se dit souvent « qu'est-c'que vous prenez ? ». « Je vais prendre » devient « j'vais prendre ». Ce n'est pas de la négligence : en français parlé, beaucoup de <b>e</b> tombent, et la phrase se resserre.",
       note:"C'est la première cause d'incompréhension dans un restaurant bruyant — et une fois qu'on sait que le e tombe, on récupère la moitié de ce qui échappait."},

      {t:'ana', h:"Le e tombe surtout dans les petits mots",
       p:"<b>je</b>, <b>ce</b>, <b>de</b>, <b>le</b>, <b>que</b>, <b>ne</b>, <b>te</b> : ce sont eux qui perdent leur voyelle.",
       mots:[['On écrit','{je} vais prendre'],['On entend','j\'vais prendre',true],['Aussi','qu\'est-c\'que · s\'il vous plaît']],
       say:"Je vais prendre la table d'hôte.",
       note:"Ces mots sont les plus fréquents du français. C'est pour cela que la chute s'entend partout."},

      {t:'ana', h:"Le e se maintient quand il aide",
       p:"Il reste quand sa chute rendrait le mot imprononçable, ou quand on parle lentement.",
       mots:[['On écrit','je {regarde} le menu'],['On entend','tout',true],['Pourquoi','trois consonnes de suite, sinon']],
       say:"Je regarde le menu.",
       note:"Personne n'applique une règle consciente : c'est la facilité de prononciation qui décide. Vous n'avez donc pas à l'apprendre pour parler."},

      {t:'texte', h:"Ce que ça change pour vous",
       p:"Vous n'avez pas à faire tomber ces <b>e</b> — parler lentement et complètement est parfaitement correct, et souvent plus clair. Mais vous devez <b>reconnaître</b> la forme resserrée, parce que c'est celle que vous entendrez.",
       note:"Le réflexe : quand un groupe de mots semble être un seul mot inconnu, essayez de réinsérer un <b>e</b>. « Kesskvouprené » redevient « qu'est-ce que vous prenez »."},

      {t:'labo', h:"Écoutez les deux formes",
       p:"Choisissez une phrase et écoutez comment elle se resserre.",
       axes:[{id:'p', lbl:'Quelle phrase ?', opts:[
         ['a','Je vais prendre la table d\'hôte.'],
         ['b','Qu\'est-ce que vous prenez ?'],
         ['c','Je ne sais pas encore.'],
         ['d','S\'il vous plaît.'],
         ['e','Je regarde le menu.']]}],
       out:{
         a:{w:["{j'vais} prendre"], say:"Je vais prendre la table d'hôte.", n:'le e de « je » tombe'},
         b:{w:["qu'est-{c'que} vous prenez"], say:"Qu'est-ce que vous prenez ?", n:'le e de « ce » et de « que » tombent'},
         c:{w:["{j'sais} pas encore"], say:"Je ne sais pas encore.", n:'le e tombe, et le « ne » disparaît'},
         d:{w:["{s'y} vous plaît"], say:"S'il vous plaît.", n:'très resserré, dit des dizaines de fois par soir'},
         e:{w:['je {regarde} le menu'], say:"Je regarde le menu.", n:'ici le e se maintient'},
       },
       note:"La phrase c cumule deux phénomènes : le e qui tombe et le « ne » qui disparaît. C'est la forme parlée courante — à reconnaître, pas à écrire."},

      {t:'ex', h:"Les phrases du restaurant",
       p:"Écoutez chacune et repérez ce qui tombe.",
       rows:[
         ["Je vais prendre la table d'hôte.","le e de « je »"],
         ["Qu'est-ce que vous prenez ?","deux e"],
         ["Je ne sais pas encore.","le e et le « ne »"],
         ["S'il vous plaît.","très resserré"],
         ["Je regarde le menu.","le e se maintient"],
         ["Ce serait possible ?","le e se maintient"],
       ]},

      {t:'piege', h:"Trois pièges à connaître",
       rows:[
         ["chercher un mot inconnu","« kesskvouprené » est « qu'est-ce que vous prenez »",
          "Réinsérez les <b>e</b> et la phrase réapparaît. C'est le réflexe qui débloque le plus vite."],
         ["écrire ce qu'on entend","on écrit toujours le e, sans exception",
          "Cette chute n'existe qu'à l'oral. « J'vais » ne s'écrit que dans les dialogues de roman."],
         ["croire qu'il faut parler comme ça","parler complètement est plus clair",
          "Un serveur préfère largement une phrase lente et complète à une imitation approximative. Ne forcez rien."],
       ]},

      {t:'check', h:"Est-ce que c'est clair maintenant ?",
       p:"Quatre questions rapides.",
       qs:[
         {q:"Les mots qui perdent leur e sont surtout…", opts:["les petits mots","les noms"], ok:0,
          fb:"je, ce, de, le, que, ne, te."},
         {q:"À l'écrit, ce e…", opts:["se note toujours","peut disparaître"], ok:0,
          fb:"La chute n'existe qu'à l'oral."},
         {q:"Faut-il parler comme ça ?", opts:["oui, pour être compris","non, parler complètement est très bien"], ok:1,
          fb:"C'est même souvent plus clair."},
         {q:"Quand un groupe semble être un mot inconnu…", opts:["on réinsère un e","on demande à répéter"], ok:0,
          fb:"Les deux marchent, mais réinsérer un e est plus rapide."},
       ]},
    ]
  },

  prArrivee: {
    eye:'Mini-leçon', tit:"Les premières minutes",
    blocs:[
      {t:'texte', h:"On attend qu'on vous place",
       p:"Dans un restaurant avec service aux tables, on <b>ne choisit pas sa table soi-même</b>. On s'arrête à l'entrée et on attend qu'une personne vienne. Un petit panneau le dit souvent : « Veuillez attendre qu'on vous place. »",
       note:"C'est différent d'un casse-croûte ou d'une aire de restauration, où on s'installe où on veut. La règle change selon le type d'endroit."},

      {t:'ana', h:"Les trois questions de l'accueil",
       p:"Toujours les mêmes, toujours dans cet ordre.",
       mots:[['1','Vous êtes {combien} ?'],['2','Vous avez une {réservation} ?',true],['3','Vous préférez où ?']],
       say:"Bonsoir ! Vous êtes combien ?",
       note:"Trois réponses courtes suffisent : « Deux. » · « Non. » · « Près de la fenêtre, si c'est possible. »"},

      {t:'ana', h:"Ce qu'on vous donne à lire",
       p:"La carte, et parfois une ardoise pour ce qui change chaque jour.",
       mots:[['La carte','tout ce que le restaurant sert'],['L\'{ardoise}','le menu du jour, qui change',true],['Le prix','l\'ardoise est presque toujours moins chère']],
       say:"Voici la carte. Le menu du jour est sur l'ardoise.",
       note:"L'ardoise est souvent au mur ou près de l'entrée. Si vous ne la voyez pas, demandez : « qu'est-ce qu'il y a au menu du jour ? »"},

      {t:'texte', h:"La formule qui sauve",
       p:"« <b>On peut prendre deux minutes ?</b> » Personne ne s'en formalise, et cela évite de commander dans la précipitation. Le serveur repassera — c'est même ce qu'il attend.",
       note:"Beaucoup d'élèves commandent la première chose venue parce qu'ils se sentent pressés. Cette phrase règle le problème."},

      {t:'labo', h:"Que répondre ?",
       p:"Choisissez une question de l'accueil.",
       axes:[{id:'p', lbl:'Quelle question ?', opts:[
         ['a','Vous êtes combien ?'],
         ['b','Vous avez une réservation ?'],
         ['c','Vous préférez près de la fenêtre ou au fond ?'],
         ['d','Vous avez fait votre choix ?'],
         ['e','Quelque chose à boire ?']]}],
       out:{
         a:{w:['{Deux}, s\'il vous plaît.'], say:"Deux, s'il vous plaît.", n:'un chiffre suffit'},
         b:{w:['{Non}, je n\'en ai pas.'], say:"Non, je n'en ai pas. Est-ce qu'il y a de la place ?", n:'et on demande s\'il y a de la place'},
         c:{w:['{Près de la fenêtre}, si c\'est possible.'], say:"Près de la fenêtre, si c'est possible.", n:'« si c\'est possible » adoucit'},
         d:{w:['{On peut prendre deux minutes ?}'], say:"On peut prendre deux minutes avant de commander ?", n:'la formule qui sauve'},
         e:{w:['{De l\'eau}, s\'il vous plaît.'], say:"De l'eau, s'il vous plaît.", n:'l\'eau du robinet est gratuite'},
       },
       note:"Cinq questions, cinq réponses courtes. Aucune ne demande plus de six mots."},

      {t:'ex', h:"Les phrases de l'accueil",
       p:"Écoutez chacune.",
       rows:[
         ["Bonsoir ! Vous êtes combien ?","la première question"],
         ["Deux, s'il vous plaît.","la réponse"],
         ["Vous avez une réservation ?","la deuxième question"],
         ["Non, je n'en ai pas. Est-ce qu'il y a de la place ?","la réponse, avec une question"],
         ["Voici la carte. Le menu du jour est sur l'ardoise.","ce qu'on vous donne"],
         ["On peut prendre deux minutes ?","la formule qui sauve"],
       ]},

      {t:'piege', h:"Trois pièges à connaître",
       rows:[
         ["s'asseoir soi-même","on attend qu'on vous place",
          "Dans un restaurant avec service aux tables, choisir sa table soi-même surprend. Un panneau à l'entrée le dit souvent."],
         ["commander trop vite","« on peut prendre deux minutes ? »",
          "Beaucoup de gens commandent la première chose venue parce qu'ils se sentent pressés. Le serveur, lui, s'attend à repasser."],
         ["ne pas voir l'ardoise","demandez le menu du jour",
          "Elle est souvent au mur, hors du champ de vision quand on est assis. Le menu du jour est presque toujours le meilleur rapport."],
       ]},

      {t:'check', h:"Est-ce que c'est clair maintenant ?",
       p:"Quatre questions rapides.",
       qs:[
         {q:"Dans un restaurant avec service aux tables, on…", opts:["choisit sa table","attend qu'on nous place"], ok:1,
          fb:"Un panneau à l'entrée le dit souvent."},
         {q:"« Vous êtes combien ? » demande…", opts:["le nombre de personnes","votre âge"], ok:0,
          fb:"Un chiffre suffit comme réponse."},
         {q:"Le menu du jour se trouve souvent…", opts:["sur la carte","sur une ardoise"], ok:1,
          fb:"Il change chaque jour : on ne l'imprime pas."},
         {q:"Si vous n'êtes pas prêt à commander…", opts:["il faut choisir vite","on peut prendre deux minutes"], ok:1,
          fb:"Le serveur s'attend à repasser."},
       ]},
    ]
  },

  t1poli: {
    eye:'Mini-leçon', tit:"Je voudrais, pourriez-vous",
    blocs:[
      {t:'texte', h:"La forme qui adoucit",
       p:"« Je veux la table d'hôte » est correct, mais sec. Au restaurant, à un comptoir, chez le médecin, on emploie une forme plus douce — et elle tient en quelques expressions qu'on apprend telles quelles.",
       note:"Ce n'est pas une question de politesse formelle : c'est la façon normale de demander quelque chose à quelqu'un qu'on ne connaît pas."},

      {t:'ana', h:"je voudrais, j'aimerais",
       p:"Pour dire ce qu'on veut. Ce sont les formes de <em>vouloir</em> et <em>aimer</em> au conditionnel.",
       mots:[['Sec','je {veux} la table d\'hôte'],['Doux','je {voudrais} la table d\'hôte',true],['Aussi','j\'aimerais un café']],
       say:"Je voudrais la table d'hôte, avec la soupe.",
       note:"« Je prendrais » fonctionne aussi, et s'entend beaucoup au restaurant : « je prendrais le poulet »."},

      {t:'ana', h:"pourriez-vous, auriez-vous",
       p:"Pour demander quelque chose à la personne en face.",
       mots:[['Direct','{réchauffez}-le'],['Doux','{pourriez-vous} le réchauffer ?',true],['Aussi','auriez-vous une table près de la fenêtre ?']],
       say:"Pourriez-vous m'apporter l'addition ?",
       note:"<b>auriez-vous</b> sert à demander si quelque chose existe ou est disponible ; <b>pourriez-vous</b>, à demander une action."},

      {t:'ana', h:"est-ce que ce serait possible de…",
       p:"La forme la plus douce, pour une demande qui dérange un peu.",
       mots:[['La demande','faire {bouger} la cuisine'],['La forme','est-ce que ce {serait} possible de',true],['Exemple','…de le réchauffer ?']],
       say:"Est-ce que ce serait possible de le réchauffer ?",
       note:"À réserver aux demandes qui demandent du travail. Pour du sel, « est-ce que je pourrais avoir » suffit largement."},

      {t:'texte', h:"Comment ça se forme",
       p:"Ce sont les mêmes bases que le futur simple, avec les terminaisons de l'imparfait : <b>-ais, -ais, -ait, -ions, -iez, -aient</b>. « je voudrais », « il pourrait », « ce serait ». À ce niveau, apprenez-les comme des expressions toutes faites.",
       note:"Si vous connaissez le futur simple du module précédent, vous connaissez déjà la moitié de ces formes."},

      {t:'labo', h:"Adoucir la demande",
       p:"Choisissez une demande directe et voyez sa forme polie.",
       axes:[{id:'p', lbl:'Quelle demande ?', opts:[
         ['a','Je veux la table d\'hôte.'],
         ['b','Réchauffez-le.'],
         ['c','Donnez-moi l\'addition.'],
         ['d','Avez-vous une table près de la fenêtre ?'],
         ['e','Je veux du sel.']]}],
       out:{
         a:{w:['Je {voudrais} la table d\'hôte.'], say:"Je voudrais la table d'hôte.", n:'je veux › je voudrais'},
         b:{w:['{Pourriez-vous} le réchauffer ?'], say:"Pourriez-vous le réchauffer ?", n:'un ordre devient une question'},
         c:{w:['{Pourriez-vous} m\'apporter l\'addition ?'], say:"Pourriez-vous m'apporter l'addition ?", n:'même transformation'},
         d:{w:['{Auriez-vous} une table près de la fenêtre ?'], say:"Auriez-vous une table près de la fenêtre ?", n:'avez-vous › auriez-vous'},
         e:{w:['Est-ce que je {pourrais} avoir du sel ?'], say:"Est-ce que je pourrais avoir un peu de sel ?", n:'la forme la plus courante au restaurant'},
       },
       note:"Cinq demandes, cinq formes. Aucune n'est plus longue que trois mots de plus que la version directe."},

      {t:'ex', h:"Les demandes du module",
       p:"Écoutez chacune et répétez-la.",
       rows:[
         ["Je voudrais la table d'hôte.","dire ce qu'on veut"],
         ["Je prendrais le poulet, à la carte.","une autre forme, très employée"],
         ["Est-ce que je pourrais avoir un peu de sel ?","demander une petite chose"],
         ["Pourriez-vous m'apporter l'addition ?","demander une action"],
         ["Auriez-vous une table près de la fenêtre ?","demander si c'est disponible"],
         ["Est-ce que ce serait possible de le réchauffer ?","la forme la plus douce"],
       ]},

      {t:'piege', h:"Trois pièges à connaître",
       rows:[
         ["employer l'impératif tout seul","« pourriez-vous le réchauffer ? » plutôt que « réchauffez-le »",
          "L'impératif seul sonne comme un ordre. Une question fait la même chose sans brusquerie."],
         ["croire qu'il faut être très formel","« je voudrais » suffit partout",
          "Inutile de chercher des tournures compliquées. Trois ou quatre expressions couvrent tous les cas."],
         ["oublier « s'il vous plaît »","il s'ajoute à presque toutes les demandes",
          "Au Québec, il est très fréquent, y compris dans des situations informelles. Son absence se remarque."],
       ]},

      {t:'check', h:"Est-ce que c'est clair maintenant ?",
       p:"Quatre questions rapides.",
       qs:[
         {q:"Pour commander, on dit plutôt…", opts:["je veux","je voudrais"], ok:1,
          fb:"« Je prendrais » fonctionne aussi très bien."},
         {q:"Pour demander une action au serveur…", opts:["Réchauffez-le.","Pourriez-vous le réchauffer ?"], ok:1,
          fb:"Une question au conditionnel, plutôt qu'un ordre."},
         {q:"« Auriez-vous » sert à demander…", opts:["si quelque chose est disponible","de faire une action"], ok:0,
          fb:"« Pourriez-vous » demande l'action."},
         {q:"Ces formes se construisent sur…", opts:["l'infinitif, comme le futur","le participe passé"], ok:0,
          fb:"Même base que le futur simple, terminaisons de l'imparfait."},
       ]},
    ]
  },

  t1menu: {
    eye:'Mini-leçon', tit:"Lire un menu",
    blocs:[
      {t:'texte', h:"Quatre formules, quatre prix",
       p:"<b>La carte</b>, <b>le menu du jour</b>, <b>la table d'hôte</b>, <b>à la carte</b>. Ce sont quatre choses différentes, et l'écart de prix entre elles peut atteindre le double pour un repas comparable.",
       note:"Comprendre ces quatre mots est la compétence la plus rentable du module."},

      {t:'ana', h:"La carte et « à la carte »",
       p:"La carte est le document ; « à la carte » est une façon de commander.",
       mots:[['La {carte}','tout ce que le restaurant sert'],['À la {carte}','un plat seul, sans formule',true],['Le prix','chaque plat à son prix']],
       say:"Je vais prendre le poulet, mais à la carte. Sans entrée.",
       note:"Commander à la carte revient plus cher si on prend plusieurs services — mais c'est le bon choix si on n'a pas très faim."},

      {t:'ana', h:"Le menu du jour",
       p:"Un choix limité, différent chaque jour, à prix réduit.",
       mots:[['Où','sur une {ardoise}, souvent'],['Quand','le midi surtout',true],['Le prix','moins cher que la carte']],
       say:"Le menu du jour est sur l'ardoise, là-bas.",
       note:"Le midi, il comprend souvent le café ou le dessert. C'est presque toujours le meilleur rapport qualité-prix."},

      {t:'ana', h:"La table d'hôte",
       p:"Un prix fixe pour trois services : entrée, plat, dessert.",
       mots:[['Ce qui est compris','{trois} services'],['Le choix','limité, mais réel',true],['Le calcul','8 $ de plus pour deux services']],
       say:"La table d'hôte, c'est un prix fixe pour trois services.",
       note:"Table d'hôte à 32 $ contre plat seul à 24 $ : huit dollars de plus pour une entrée et un dessert. Presque toujours avantageux si on a faim."},

      {t:'texte', h:"Les mots à repérer sur un menu",
       p:"<b>servi avec</b> (ce qui vient avec le plat) · <b>au choix</b> (vous décidez) · <b>selon arrivage</b> (ça change chaque jour) · <b>supplément</b> (ça coûte plus cher) · <b>prix du marché</b> (il faut demander le prix).",
       note:"« Supplément » est le mot à ne pas manquer : il transforme un prix affiché en prix plus élevé."},

      {t:'labo', h:"Quelle formule choisir ?",
       p:"Choisissez une situation et voyez ce qui convient.",
       axes:[{id:'p', lbl:'Quelle situation ?', opts:[
         ['a','Vous avez très faim, le soir.'],
         ['b','Vous n\'avez pas très faim.'],
         ['c','Vous mangez le midi, en semaine.'],
         ['d','Vous voulez goûter le poisson frais.'],
         ['e','Vous êtes pressé.']]}],
       out:{
         a:{w:['la {table d\'hôte}'], say:"La table d'hôte, c'est un prix fixe pour trois services.", n:'trois services, huit dollars de plus'},
         b:{w:['à la {carte}'], say:"Je vais prendre le poulet, mais à la carte.", n:'un plat seul, sans entrée'},
         c:{w:['le menu du {midi}'], say:"Le menu du midi est servi jusqu'à deux heures.", n:'souvent café inclus'},
         d:{w:['le {plat du jour}'], say:"Le poisson du jour, c'est de la truite.", n:'ce que la cuisine a reçu aujourd\'hui'},
         e:{w:['le menu du {jour}'], say:"Le menu du jour est sur l'ardoise.", n:'choix limité, service plus rapide'},
       },
       note:"Un choix limité n'est pas un défaut : il veut dire que la cuisine a préparé ces plats d'avance, donc qu'ils arrivent plus vite."},

      {t:'ex', h:"Les mots du menu",
       p:"Écoutez chacun.",
       rows:[
         ["La carte, c'est tout ce qu'ils font.","le document complet"],
         ["Le menu du jour change chaque jour.","choix limité, moins cher"],
         ["La table d'hôte, un prix fixe pour trois services.","entrée, plat, dessert"],
         ["Je vais prendre le poulet, mais à la carte.","un plat seul"],
         ["La truite est servie avec des légumes et du riz.","l'accompagnement"],
         ["Le café est inclus dans le menu du midi.","ce qui vient avec"],
       ]},

      {t:'piege', h:"Trois pièges à connaître",
       rows:[
         ["confondre la carte et le menu","la carte est plus chère, le menu du jour moins",
          "En français d'ici, « le menu » désigne souvent une formule à prix fixe, pas la liste complète. La liste complète, c'est la carte."],
         ["ne pas voir la ligne « servi avec »","c'est là qu'est la vraie différence de prix",
          "Deux plats au même prix n'ont pas le même contenu si l'un est servi avec soupe et café."],
         ["oublier le mot « supplément »","le prix affiché n'est plus le bon",
          "« Table d'hôte 32 $, supplément 4 $ pour le poisson » veut dire 36 $."],
       ]},

      {t:'check', h:"Est-ce que c'est clair maintenant ?",
       p:"Quatre questions rapides.",
       qs:[
         {q:"« À la carte » veut dire…", opts:["un plat seul, sans formule","tous les plats du restaurant"], ok:0,
          fb:"La carte est le document ; à la carte est une façon de commander."},
         {q:"La table d'hôte comprend…", opts:["un plat","trois services"], ok:1,
          fb:"Entrée, plat, dessert, à prix fixe."},
         {q:"Le menu du jour est…", opts:["plus cher que la carte","moins cher"], ok:1,
          fb:"Choix limité, prix réduit."},
         {q:"« Supplément » veut dire…", opts:["c'est inclus","ça coûte plus cher"], ok:1,
          fb:"Le prix affiché n'est plus le bon."},
       ]},
    ]
  },

  t2demander: {
    eye:'Mini-leçon', tit:"Demander, et signaler",
    blocs:[
      {t:'texte', h:"Signaler n'est pas se plaindre",
       p:"Un plat froid, une commande erronée, un verre sale : on le dit. Ce n'est pas une plainte, c'est une information — et le restaurant préfère largement le savoir. Sinon il ne peut rien corriger, et il ne saura jamais pourquoi vous n'êtes pas revenu.",
       note:"C'est ce que Manon explique à Andrés, et c'est un point culturel autant que linguistique."},

      {t:'ana', h:"Pour une petite chose",
       p:"Du sel, de l'eau, un couvert, une serviette : rien de tout cela ne dérange.",
       mots:[['La formule','Est-ce que je {pourrais} avoir…'],['Exemple','…un peu de sel, s\'il vous plaît ?',true],['Le ton','ordinaire, sans excuse']],
       say:"Est-ce que je pourrais avoir un peu de sel, s'il vous plaît ?",
       note:"Inutile de s'excuser longuement : ce sont des demandes que le serveur reçoit trente fois par soir."},

      {t:'ana', h:"Pour quelque chose qui demande du travail",
       p:"Réchauffer un plat, en refaire un, changer une commande.",
       mots:[['La formule','Est-ce que ce {serait} possible de…'],['Exemple','…de le réchauffer ?',true],['Le ton','doux, mais sans hésiter']],
       say:"Est-ce que ce serait possible de le réchauffer ?",
       note:"Le serveur répondra presque toujours oui, et s'excusera. C'est son travail, et il préfère de loin le savoir maintenant."},

      {t:'ana', h:"Pour attirer l'attention",
       p:"Un mot, un regard, une main légèrement levée.",
       mots:[['On dit','{Excusez-moi}'],['On fait','on lève un peu la main',true],['On ne fait pas','claquer des doigts, dire « eh ! »']],
       say:"Excusez-moi, quand vous aurez un moment.",
       note:"« Quand vous aurez un moment » est très utile : cela dit que ce n'est pas urgent, et le serveur revient dès qu'il peut."},

      {t:'texte', h:"Ce qu'on ne signale pas",
       p:"Ce qui relève du <b>goût personnel</b> ou du <b>prix</b>. « Je n'aime pas le goût » n'est pas un problème de service, et « c'est cher » ne se discute pas avec le serveur. Le reste — température, erreur, propreté, attente anormale — se dit.",
       note:"La règle simple : si le restaurant peut y faire quelque chose, on le dit. Sinon, non."},

      {t:'labo', h:"Est-ce qu'on le dit ?",
       p:"Choisissez une situation.",
       axes:[{id:'p', lbl:'Quelle situation ?', opts:[
         ['a','Mon plat est froid.'],
         ['b','J\'avais demandé sans sauce.'],
         ['c','Je n\'aime pas le goût.'],
         ['d','Mon verre est sale.'],
         ['e','Ma commande tarde depuis 40 minutes.']]}],
       out:{
         a:{w:['{Oui} — on le dit'], say:"Excusez-moi, mon poisson est un peu froid.", n:'le restaurant peut le corriger'},
         b:{w:['{Oui} — on le dit'], say:"J'avais demandé le poulet sans sauce.", n:'une erreur de commande'},
         c:{w:['{Non} — c\'est un goût personnel'], say:"Je n'aime pas le goût, mais le plat est bien fait.", n:'le restaurant n\'y peut rien'},
         d:{w:['{Oui} — on le dit'], say:"Excusez-moi, mon verre n'est pas propre.", n:'question d\'hygiène'},
         e:{w:['{Oui} — on le dit'], say:"Excusez-moi, nous avons commandé il y a quarante minutes.", n:'un fait, pas un reproche'},
       },
       note:"Quatre sur cinq se disent. Le seul cas qu'on garde pour soi est celui du goût — parce que personne ne peut rien y faire."},

      {t:'ex', h:"Les phrases du repas",
       p:"Écoutez chacune et répétez-la.",
       rows:[
         ["Est-ce que je pourrais avoir un peu de sel, s'il vous plaît ?","une petite demande"],
         ["Excusez-moi, quand vous aurez un moment.","attirer l'attention"],
         ["Mon poisson est un peu froid.","signaler un fait"],
         ["Est-ce que ce serait possible de le réchauffer ?","demander une correction"],
         ["J'avais demandé le poulet sans sauce.","signaler une erreur"],
         ["Ce n'est pas nécessaire, mais je préfère vous le dire.","signaler sans exiger"],
       ]},

      {t:'piege', h:"Trois pièges à connaître",
       rows:[
         ["ne rien dire pour ne pas déranger","le restaurant préfère le savoir",
          "Un plat froid signalé se règle en deux minutes. Non signalé, il gâche le repas — et le restaurant ne saura jamais pourquoi."],
         ["s'excuser longuement","« excusez-moi » suffit",
          "Une demande ordinaire n'a pas besoin de justification. Trois mots et la demande."],
         ["signaler ce qui relève du goût","« je n'aime pas » n'est pas un problème de service",
          "Le restaurant ne peut rien y faire, et cela met tout le monde mal à l'aise."],
       ]},

      {t:'check', h:"Est-ce que c'est clair maintenant ?",
       p:"Quatre questions rapides.",
       qs:[
         {q:"Un plat froid…", opts:["se signale","se mange comme ça"], ok:0,
          fb:"Le restaurant préfère le savoir et le corriger."},
         {q:"Pour du sel, on dit…", opts:["Est-ce que je pourrais avoir…","Est-ce que ce serait possible de…"], ok:0,
          fb:"La deuxième forme est pour ce qui demande du travail."},
         {q:"Pour attirer l'attention…", opts:["« Excusez-moi »","on claque des doigts"], ok:0,
          fb:"Un mot et une main légèrement levée."},
         {q:"« Je n'aime pas le goût »…", opts:["se dit au serveur","se garde pour soi"], ok:1,
          fb:"Le restaurant n'y peut rien."},
       ]},
    ]
  },

  t3addition: {
    eye:'Mini-leçon', tit:"Taxes et pourboire",
    blocs:[
      {t:'texte', h:"Deux choses différentes",
       p:"Sur une addition de restaurant, les <b>taxes</b> sont presque toujours déjà comprises dans le total. Le <b>pourboire</b>, lui, ne l'est jamais : on l'ajoute soi-même. Confondre les deux fait payer trop, ou pas assez.",
       note:"C'est probablement l'information la plus utile de tout le module pour quelqu'un qui vient d'arriver."},

      {t:'ana', h:"Les taxes : déjà là",
       p:"Le total du bas comprend la TPS et la TVQ.",
       mots:[['Sur l\'addition','58,40 $ {taxes comprises}'],['Ce que ça veut dire','rien ne s\'ajoute',true],['La formule à repérer','« taxes comprises »']],
       say:"Cinquante-huit dollars et quarante, taxes comprises.",
       note:"Si la mention n'y est pas, regardez les lignes du bas : TPS et TVQ y figurent séparément, additionnées au sous-total."},

      {t:'ana', h:"Le pourboire : à ajouter",
       p:"Environ 15 % du montant <b>avant</b> taxes.",
       mots:[['Le taux','environ {15 %}'],['La base','le montant {avant} taxes',true],['Sur 50 $','7,50 $']],
       say:"Quinze pour cent du montant avant taxes, en général.",
       note:"Le calcul rapide : le dixième du montant, plus la moitié de ce dixième. 50 › 5 + 2,50 = 7,50."},

      {t:'ana', h:"Au terminal de paiement",
       p:"Il demande le pourboire <b>avant</b> le code, et propose des pourcentages.",
       mots:[['L\'ordre','pourboire, puis {code}'],['Les propositions','souvent calculées {après} taxes',true],['L\'option','« autre montant », en bas']],
       say:"Il va vous demander le pourboire en premier.",
       note:"Les pourcentages proposés étant calculés après taxes, ils donnent un montant un peu plus élevé. « Autre montant » permet d'entrer son propre chiffre."},

      {t:'texte', h:"Pourquoi ça compte, ici",
       p:"Au Québec, le pourboire fait partie du <b>revenu</b> du personnel de service, dont le salaire de base est plus bas que le salaire minimum ordinaire. Ce n'est pas un simple remerciement : c'est un usage attendu, et laisser beaucoup moins que 15 % se remarque.",
       note:"On peut donner moins si le service a vraiment été mauvais. Mais ce n'est pas la même chose que dans les pays où le service est compris."},

      {t:'labo', h:"Calculez le pourboire",
       p:"Choisissez un montant et voyez le calcul.",
       axes:[{id:'p', lbl:'Quel montant ?', opts:[
         ['a','20 $'],
         ['b','40 $'],
         ['c','50 $'],
         ['d','80 $'],
         ['e','100 $']]}],
       out:{
         a:{w:['{3 $} — 2 + 1'], say:"Sur vingt dollars, quinze pour cent font trois dollars.", n:'le dixième, plus sa moitié'},
         b:{w:['{6 $} — 4 + 2'], say:"Sur quarante dollars, six dollars.", n:'même méthode'},
         c:{w:['{7,50 $} — 5 + 2,50'], say:"Sur cinquante dollars, sept dollars et demi.", n:'le montant du module'},
         d:{w:['{12 $} — 8 + 4'], say:"Sur quatre-vingts dollars, douze dollars.", n:'même méthode'},
         e:{w:['{15 $} — 10 + 5'], say:"Sur cent dollars, quinze dollars.", n:'le cas le plus simple'},
       },
       note:"La méthode marche pour n'importe quel montant, de tête, en deux secondes."},

      {t:'ex', h:"Les phrases de l'addition",
       p:"Écoutez chacune.",
       rows:[
         ["L'addition, s'il vous plaît.","demander l'addition"],
         ["Ensemble ou séparé ?","la question du serveur"],
         ["Cinquante-huit dollars et quarante, taxes comprises.","le total"],
         ["Quinze pour cent du montant avant taxes.","le pourboire"],
         ["Ce n'est pas sur l'addition : tu l'ajoutes toi-même.","la règle à retenir"],
         ["« Autre montant », en bas, si vous préférez décider.","au terminal"],
       ]},

      {t:'piege', h:"Trois pièges à connaître",
       rows:[
         ["croire que le pourboire est compris","il ne l'est jamais au restaurant",
          "Dans plusieurs pays, le service est inclus. Ici, non — et le personnel compte dessus."],
         ["calculer sur le montant avec taxes","15 % se calcule avant taxes",
          "La différence est petite, mais les terminaux, eux, calculent souvent après. « Autre montant » permet de corriger."],
         ["ne pas répondre à « ensemble ou séparé ? »","décidez avant de demander l'addition",
          "Une fois l'addition imprimée ensemble, la séparer prend du temps. La question se règle en une seconde si elle est anticipée."],
       ]},

      {t:'check', h:"Est-ce que c'est clair maintenant ?",
       p:"Quatre questions rapides.",
       qs:[
         {q:"Les taxes, sur une addition de restaurant…", opts:["s'ajoutent au total","sont déjà comprises"], ok:1,
          fb:"« Taxes comprises » figure presque toujours."},
         {q:"Le pourboire habituel est d'environ…", opts:["15 %","5 %"], ok:0,
          fb:"Du montant avant taxes."},
         {q:"Sur 60 $, quinze pour cent font…", opts:["9 $","6 $"], ok:0,
          fb:"6 + 3 = 9."},
         {q:"Au terminal, le pourboire est demandé…", opts:["avant le code","après le code"], ok:0,
          fb:"C'est la première question de l'écran."},
       ]},
    ]
  },
};
