const PLUS = {
  prPhon: {
    eye:'Mini-leçon', tit:"La liaison des quantités",
    blocs:[
      {t:'texte', h:"« Deux œufs » se dit « deu-zeu »",
       p:"Quand un mot finit par une consonne muette et que le mot suivant commence par une voyelle, cette consonne se réveille et se prononce avec le mot d'après. C'est la <b>liaison</b>. Devant les quantités, elle est <b>obligatoire</b> — et c'est ce qui rend « deux œufs » méconnaissable.",
       note:"Ce n'est pas du français rapide ou familier : c'est la prononciation normale, celle de tout le monde."},

      {t:'ana', h:"Devant une voyelle : la liaison se fait",
       p:"Le nombre et le nom se prononcent d'un seul souffle.",
       mots:[['On écrit','deux œufs'],['On entend','deu{z}œufs',true],['Aussi','trois oranges › troi{z}oranges']],
       say:"Je voudrais deux œufs et trois oranges.",
       note:"Autres exemples : six oignons, dix ananas, cent euros, un ananas, les épices."},

      {t:'ana', h:"Devant une consonne : pas de liaison",
       p:"Le nombre garde sa forme habituelle, et la consonne finale reste muette.",
       mots:[['On écrit','deux poires'],['On entend','deu poires',true],['Aussi','trois tomates › troi tomates']],
       say:"Je voudrais deux poires et trois tomates.",
       note:"C'est le même nombre, prononcé de deux façons selon le mot qui suit. Comme pour la chute des consonnes, c'est le mot d'après qui décide."},

      {t:'texte', h:"Le cas de six et dix",
       p:"Ces deux nombres changent trois fois. Seuls : « si<b>ss</b> », « di<b>ss</b> ». Devant une consonne : « si », « di ». Devant une voyelle : « si<b>z</b> », « di<b>z</b> ».",
       note:"« J'en veux six. » (siss) · « six citrons » (si) · « six oignons » (siz). Trois prononciations pour un seul mot."},

      {t:'labo', h:"Écoutez les paires",
       p:"Choisissez une paire et écoutez la différence.",
       axes:[{id:'p', lbl:'Quelle paire ?', opts:[
         ['a','deux œufs / deux poires'],
         ['b','trois oranges / trois tomates'],
         ['c','six oignons / six citrons'],
         ['d','un ananas / un kilo'],
         ['e','cent euros / cent grammes']]}],
       out:{
         a:{w:['deu{z}œufs'], say:"Je voudrais deux œufs.", n:'voyelle après › liaison obligatoire'},
         b:{w:['troi{z}oranges'], say:"Je voudrais trois oranges.", n:'voyelle après › liaison obligatoire'},
         c:{w:['si{z}oignons'], say:"Je voudrais six oignons.", n:'six devient « siz » devant une voyelle'},
         d:{w:['u{n}ananas'], say:"Je voudrais un ananas.", n:'le n de « un » se prononce'},
         e:{w:['cen{t}euros'], say:"Ça fait cent euros.", n:'le t de « cent » se réveille'},
       },
       note:"Écoutez chaque paire deux fois de suite : le même nombre, deux prononciations. C'est le mot suivant qui décide, jamais le nombre."},

      {t:'ex', h:"Les quantités du module",
       p:"Écoutez chacune et répétez-la à voix haute.",
       rows:[
         ["Je voudrais deux œufs.","liaison — deu-zeufs"],
         ["Je voudrais deux poires.","pas de liaison"],
         ["Je voudrais trois oranges.","liaison — troi-zoranges"],
         ["Je voudrais six oignons.","liaison — si-zoignons"],
         ["Je voudrais six citrons.","pas de liaison — si citrons"],
         ["Ça fait cent grammes.","pas de liaison"],
       ]},

      {t:'piege', h:"Trois pièges à connaître",
       rows:[
         ["chercher un mot inconnu","« deuzeufs » est bien « deux œufs »",
          "Si un groupe de mots vous semble être un seul mot inconnu, essayez de le couper avant la voyelle. Le nombre réapparaît."],
         ["ne pas faire la liaison","« deux œufs », jamais « deu — œufs »",
          "Devant les quantités, la liaison est obligatoire. La sauter s'entend immédiatement et rend la phrase plus difficile à suivre."],
         ["faire la liaison partout","« cent grammes », pas « cent-t-grammes »",
          "Devant une consonne, il n'y a pas de liaison. En ajouter une est aussi étrange que d'en oublier une."],
       ]},

      {t:'check', h:"Est-ce que c'est clair maintenant ?",
       p:"Quatre questions rapides.",
       qs:[
         {q:"« Deux œufs » se prononce…", opts:["deu œufs","deu-zeufs"], ok:1,
          fb:"La liaison est obligatoire devant une voyelle."},
         {q:"Ce qui décide de la liaison, c'est…", opts:["le nombre","le mot qui suit"], ok:1,
          fb:"Le même nombre se prononce de deux façons."},
         {q:"« Six citrons » se prononce…", opts:["si citrons","siz citrons"], ok:0,
          fb:"Devant une consonne, le x de six est muet."},
         {q:"« Cent grammes » demande…", opts:["une liaison","aucune liaison"], ok:1,
          fb:"« grammes » commence par une consonne."},
       ]},
    ]
  },

  t1part: {
    eye:'Mini-leçon', tit:"Du, de la, des",
    blocs:[
      {t:'texte', h:"Une quantité qu'on ne compte pas",
       p:"On ne dit pas « je veux poulet », ni « je veux le poulet » quand on en veut simplement une certaine quantité. Le français a une forme pour cela : <b>du</b>, <b>de la</b>, <b>de l'</b>, <b>des</b>. C'est ce qu'on emploie à l'épicerie du matin au soir.",
       note:"« Je voudrais du poulet » veut dire : une certaine quantité de poulet, sans dire laquelle."},

      {t:'ana', h:"Les quatre formes",
       p:"C'est le genre et le nombre du nom qui décident, jamais la quantité.",
       mots:[['Masculin','{du} poulet'],['Féminin','de la truite',true],['Voyelle','de l\'eau · Pluriel : des poitrines']],
       say:"Je voudrais du poulet et de la truite.",
       note:"Aucun rapport avec la quantité : « du poulet » peut désigner deux cents grammes comme trois kilos."},

      {t:'ana', h:"À la forme négative : toujours « de »",
       p:"Les quatre formes se réduisent à une seule.",
       mots:[['Affirmatif','je prends {du} riz'],['Négatif','je ne prends pas {de} riz',true],['Aussi','il n\'y a pas de tomates']],
       say:"Je ne prends pas de riz aujourd'hui.",
       note:"C'est une des rares règles du français qui n'a pas d'exception : après une négation, c'est <b>de</b> ou <b>d'</b>."},

      {t:'ana', h:"Après une quantité précise : « de » aussi",
       p:"Dès qu'on donne un poids, un volume ou un nombre, on repasse à <b>de</b>.",
       mots:[['Sans quantité','{du} bœuf haché'],['Avec quantité','une livre {de} bœuf haché',true],['Aussi','deux cents grammes de jambon']],
       say:"Je voudrais une livre de bœuf haché.",
       note:"Autres exemples : un kilo <b>de</b> riz, un litre <b>d'</b>eau, une douzaine <b>d'</b>œufs, beaucoup <b>de</b> monde."},

      {t:'texte', h:"Le test en une seconde",
       p:"<b>Une négation ou une quantité ?</b> › <b>de</b>. <b>Sinon</b> › du, de la, de l', des, selon le nom. Ce test couvre tout ce dont vous avez besoin à ce niveau.",
       note:"Écrivez-le au dos de votre liste d'épicerie la première semaine. Après, il devient automatique."},

      {t:'labo', h:"Quelle forme ?",
       p:"Choisissez une phrase et voyez ce qui décide.",
       axes:[{id:'p', lbl:'Quelle phrase ?', opts:[
         ['a','Je voudrais ___ poulet.'],
         ['b','Est-ce qu\'il y a ___ truite ?'],
         ['c','Je ne prends pas ___ riz.'],
         ['d','Une livre ___ bœuf haché.'],
         ['e','Elle achète ___ poitrines.']]}],
       out:{
         a:{w:['Je voudrais {du} poulet.'], say:"Je voudrais du poulet, s'il vous plaît.", n:'masculin, pas de négation › du'},
         b:{w:["Est-ce qu'il y a {de la} truite ?"], say:"Est-ce qu'il y a de la truite aujourd'hui ?", n:'féminin › de la'},
         c:{w:['Je ne prends pas {de} riz.'], say:"Je ne prends pas de riz aujourd'hui.", n:'négation › de, toujours'},
         d:{w:['Une livre {de} bœuf haché.'], say:"Je voudrais une livre de bœuf haché.", n:'quantité précise › de'},
         e:{w:['Elle achète {des} poitrines.'], say:"Elle achète des poitrines de poulet.", n:'pluriel › des'},
       },
       note:"Comparez a et d : le même produit, deux formes. C'est la quantité qui a changé, pas le nom."},

      {t:'ex', h:"Les phrases du module",
       p:"Écoutez chacune et repérez la forme.",
       rows:[
         ["Je voudrais du poulet, s'il vous plaît.","du — masculin"],
         ["Est-ce qu'il y a de la truite aujourd'hui ?","de la — féminin"],
         ["Elle achète des poitrines de poulet.","des — pluriel"],
         ["Je ne prends pas de riz aujourd'hui.","de — négation"],
         ["Je voudrais une livre de bœuf haché.","de — quantité précise"],
         ["Il n'y a plus de grand format.","de — négation"],
       ]},

      {t:'piege', h:"Trois pièges à connaître",
       rows:[
         ["employer l'article défini","« je voudrais du poulet », pas « le poulet »",
          "« Le poulet » désigne un poulet précis, connu des deux personnes. Au comptoir, on en veut une certaine quantité : c'est <b>du</b>."],
         ["garder du, de la, des après une négation","« pas de riz », jamais « pas du riz »",
          "Cette règle n'a pas d'exception. C'est une des plus faciles à corriger et une des plus visibles."],
         ["oublier le « de » après une quantité","« une livre de bœuf », pas « une livre du bœuf »",
          "Poids, volume, nombre : dès qu'il y a une mesure, c'est <b>de</b> tout seul."],
       ]},

      {t:'check', h:"Est-ce que c'est clair maintenant ?",
       p:"Quatre questions rapides.",
       qs:[
         {q:"« Je voudrais ___ truite » demande…", opts:["du","de la"], ok:1,
          fb:"Truite est féminin."},
         {q:"« Je ne prends pas ___ riz » demande…", opts:["du","de"], ok:1,
          fb:"Après une négation, toujours <b>de</b>."},
         {q:"« Une livre ___ bœuf haché » demande…", opts:["de","du"], ok:0,
          fb:"Après une quantité précise, <b>de</b> tout seul."},
         {q:"Ce qui décide entre du et de la, c'est…", opts:["la quantité","le genre du nom"], ok:1,
          fb:"La quantité n'y change rien."},
       ]},
    ]
  },

  t1garde: {
    eye:'Mini-leçon', tit:"Ça se garde deux jours",
    blocs:[
      {t:'texte', h:"Une phrase qui ne parle de personne",
       p:"« Le poisson se garde deux jours. » Qui le garde ? Personne en particulier — tout le monde. Cette construction sert à donner une information <b>générale</b> sur une chose, sans nommer qui fait l'action. Elle est partout dans l'alimentation.",
       note:"C'est plus court et plus naturel que « on garde le poisson deux jours », et bien plus employé."},

      {t:'ana', h:"Comment ça se construit",
       p:"La chose devient le sujet, et on ajoute <b>se</b> devant le verbe.",
       mots:[['Avec « on »','on garde le poisson'],['Avec « se »','le poisson {se garde}',true],['Le sujet','la chose, pas la personne']],
       say:"Le poisson frais se garde deux jours.",
       note:"Le verbe s'accorde avec la chose : « les conserves <b>se conservent</b> », au pluriel."},

      {t:'ana', h:"Les verbes de l'alimentation",
       p:"Toute une famille fonctionne ainsi.",
       mots:[['Conserver','ça {se garde} · ça se conserve'],['Cuisiner','ça {se mange} · ça se cuisine',true],['Préparer','ça se congèle · ça se réchauffe']],
       say:"Ce fruit se mange cru et ce plat se cuisine en vingt minutes.",
       note:"Vous les entendrez à chaque comptoir : « ça se garde combien de temps ? » est probablement la question la plus posée d'une épicerie."},

      {t:'texte', h:"Ailleurs aussi",
       p:"Cette construction déborde largement l'alimentation. « Ça <b>se dit</b> beaucoup ici. » « Ça <b>ne se fait pas</b>. » « Ce mot <b>s'écrit</b> avec deux l. » « Ça <b>se comprend</b>. »",
       note:"« Ça ne se fait pas » est une phrase culturelle très utile : elle dit qu'une chose n'est pas interdite, mais qu'on ne la fait pas ici."},

      {t:'ana', h:"À ne pas confondre",
       p:"Le même petit mot <b>se</b> sert à deux choses différentes.",
       mots:[['Il fait l\'action sur lui','il {se} lave'],['La chose, en général','ça {se} lave à l\'eau froide',true],['Le test','y a-t-il une personne ?']],
       say:"Il se lave les mains. Ce chandail se lave à l'eau froide.",
       note:"Si le sujet est une <b>personne</b>, elle fait l'action sur elle-même. Si le sujet est une <b>chose</b>, la phrase ne parle de personne."},

      {t:'labo', h:"Transformez la phrase",
       p:"Choisissez une phrase avec « on » et voyez ce qu'elle devient.",
       axes:[{id:'p', lbl:'Quelle phrase ?', opts:[
         ['a','On garde le poisson deux jours.'],
         ['b','On congèle ce poisson trois mois.'],
         ['c','On mange ce fruit cru.'],
         ['d','On conserve les conserves des mois.'],
         ['e','On ne dit pas ça ici.']]}],
       out:{
         a:{w:['Le poisson {se garde} deux jours.'], say:"Le poisson frais se garde deux jours.", n:'la chose devient le sujet'},
         b:{w:['Ce poisson {se congèle} trois mois.'], say:"Ce poisson se congèle trois mois.", n:'même construction'},
         c:{w:['Ce fruit {se mange} cru.'], say:"Ce fruit se mange cru.", n:'même construction'},
         d:{w:['Les conserves {se conservent} des mois.'], say:"Les conserves se conservent des mois.", n:'pluriel : le verbe s\'accorde'},
         e:{w:['Ça {ne se dit pas} ici.'], say:"Ça ne se dit pas ici.", n:'négation : ne … pas autour de « se + verbe »'},
       },
       note:"Remarquez d : le verbe s'accorde avec « les conserves », pas avec une personne. C'est la seule difficulté."},

      {t:'ex', h:"Les phrases du module",
       p:"Écoutez chacune.",
       rows:[
         ["Le poisson frais se garde deux jours.","conservation"],
         ["Ce poisson se congèle trois mois.","conservation"],
         ["Le bœuf haché se garde le moins longtemps.","conservation"],
         ["Ce fruit se mange cru.","préparation"],
         ["Ce plat se cuisine en vingt minutes.","préparation"],
         ["Ça ne se dit pas ici.","hors alimentation"],
       ]},

      {t:'piege', h:"Trois pièges à connaître",
       rows:[
         ["oublier l'accord au pluriel","« les conserves se conservent »",
          "Le verbe s'accorde avec la chose, qui est le sujet. Au pluriel, il prend la marque du pluriel."],
         ["chercher qui fait l'action","personne en particulier",
          "« Ça se garde deux jours » ne dit pas qui garde. C'est justement l'intérêt de la construction."],
         ["confondre avec le verbe pronominal ordinaire","« il se lave » et « ça se lave »",
          "Sujet personne › il fait l'action sur lui-même. Sujet chose › la phrase est générale."],
       ]},

      {t:'check', h:"Est-ce que c'est clair maintenant ?",
       p:"Quatre questions rapides.",
       qs:[
         {q:"« Le poisson se garde deux jours » dit…", opts:["qui le garde","comment on le garde en général"], ok:1,
          fb:"La phrase ne nomme personne."},
         {q:"Au pluriel, on écrit…", opts:["les conserves se conserve","les conserves se conservent"], ok:1,
          fb:"Le verbe s'accorde avec la chose."},
         {q:"« Ça ne se fait pas » veut dire…", opts:["c'est interdit","on ne le fait pas ici"], ok:1,
          fb:"C'est un usage, pas une interdiction."},
         {q:"Dans « il se lave », le sujet est…", opts:["une personne","une chose"], ok:0,
          fb:"Il fait l'action sur lui-même : c'est l'autre emploi de « se »."},
       ]},
    ]
  },

  t2en: {
    eye:'Mini-leçon', tit:"Le petit mot « en »",
    blocs:[
      {t:'texte', h:"Ne pas répéter ce qu'on achète",
       p:"« — Combien de poitrines voulez-vous ? — J'<b>en</b> veux quatre. » Sans ce petit mot, il faudrait répéter « poitrines » à chaque phrase. <b>en</b> remplace le produit et garde la quantité.",
       note:"C'est le compagnon de <b>y</b> : l'un remplace un lieu, l'autre une quantité. Tous les deux se placent devant le verbe."},

      {t:'ana', h:"Sa place : devant le verbe",
       p:"Comme tous les petits pronoms du français, il précède le verbe.",
       mots:[['La forme','j\'{en} veux quatre'],['Jamais','« je veux en quatre »',true],['Aussi','il m\'en reste · j\'en prends deux']],
       say:"J'en veux quatre.",
       note:"Au passé composé, il passe devant l'auxiliaire : « j'<b>en</b> ai pris deux »."},

      {t:'ana', h:"La quantité reste à la fin",
       p:"C'est la différence avec les autres pronoms : le nombre ou la mesure se garde.",
       mots:[['Le produit','remplacé par {en}'],['La quantité','reste : {quatre}',true],['Aussi','j\'en prends une livre']],
       say:"J'en prends une livre.",
       note:"« J'en veux » tout seul est correct mais vague. Au comptoir, on donne presque toujours la quantité après."},

      {t:'ana', h:"À la forme négative",
       p:"<b>en</b> reste collé devant le verbe, entre le <b>ne</b> et le verbe.",
       mots:[['Affirmatif','j\'{en} prends deux'],['Négatif','je n\'{en} prends pas',true],['Aussi','il n\'y en a plus']],
       say:"Je n'en prends pas aujourd'hui.",
       note:"« Il n'y <b>en</b> a plus » est une des phrases les plus entendues dans un magasin. Elle contient <b>y</b> et <b>en</b> à la fois."},

      {t:'texte', h:"Le repère qui règle tout",
       p:"<b>y</b> remplace un <u>lieu</u> : « j'y vais ». <b>en</b> remplace une <u>quantité</u> : « j'en prends deux ». Les deux se mettent devant le verbe, et aucun des deux ne se répète après.",
       note:"Si vous avez fait le module sur les déplacements, vous connaissez déjà la moitié de cette leçon."},

      {t:'labo', h:"Remplacez le produit",
       p:"Choisissez une phrase du comptoir.",
       axes:[{id:'p', lbl:'Quelle phrase ?', opts:[
         ['a','Je veux quatre poitrines.'],
         ['b','Il me reste du bœuf haché.'],
         ['c','Je prends deux savons.'],
         ["d",'Il n\'y a plus de riz.'],
         ['e','Je ne prends pas de petits sacs.']]}],
       out:{
         a:{w:["J'{en} veux quatre."], say:"J'en veux quatre.", n:'le produit est remplacé, le nombre reste'},
         b:{w:["Il m'{en} reste."], say:"Il m'en reste, oui.", n:'devant le verbe, après le pronom « m\' »'},
         c:{w:["J'{en} prends deux."], say:"J'en prends deux.", n:'le nombre reste à la fin'},
         d:{w:["Il n'y {en} a plus."], say:"Il n'y en a plus.", n:'y et en dans la même phrase'},
         e:{w:["Je n'{en} prends pas."], say:"Je n'en prends pas de petits.", n:'négation : en reste devant le verbe'},
       },
       note:"La phrase d contient les deux pronoms : « y » pour le lieu implicite, « en » pour le produit. C'est la phrase la plus fréquente d'un magasin."},

      {t:'ex', h:"Les phrases du module",
       p:"Écoutez chacune et repérez le petit mot.",
       rows:[
         ["J'en veux quatre.","en — les poitrines"],
         ["Il m'en reste, oui.","en — du bœuf haché"],
         ["J'en prends deux.","en — des savons"],
         ["Il n'y en a plus.","en — du riz"],
         ["Je n'en prends pas de petits.","en — des sacs"],
         ["Vous en voulez combien ?","en — le produit demandé"],
       ]},

      {t:'piege', h:"Trois pièges à connaître",
       rows:[
         ["placer en après le verbe","« j'en veux quatre », jamais « je veux en quatre »",
          "Comme <b>y</b>, le pronom <b>en</b> se colle devant le verbe. C'est l'inverse de plusieurs langues."],
         ["répéter le produit après en","« j'en prends deux », pas « j'en prends deux poitrines »",
          "Le produit est déjà dans le <b>en</b>. Le redire est une faute qui s'entend tout de suite."],
         ["oublier en dans la réponse","« — Vous en voulez combien ? — Quatre. »",
          "Répondre par le nombre seul se comprend, mais « j'en veux quatre » est la forme complète et naturelle."],
       ]},

      {t:'check', h:"Est-ce que c'est clair maintenant ?",
       p:"Quatre questions rapides.",
       qs:[
         {q:"« Je veux quatre poitrines » devient…", opts:["j'en veux quatre","je veux en quatre"], ok:0,
          fb:"<b>en</b> se met devant le verbe."},
         {q:"Après avoir dit « en », faut-il répéter le produit ?", opts:["oui","non, il est déjà dedans"], ok:1,
          fb:"C'est tout l'intérêt du mot."},
         {q:"« en » remplace…", opts:["un lieu","une quantité"], ok:1,
          fb:"C'est <b>y</b> qui remplace un lieu."},
         {q:"À la forme négative, « en » se place…", opts:["entre ne et le verbe","après pas"], ok:0,
          fb:"« Je n'<b>en</b> prends pas. »"},
       ]},
    ]
  },

  t2unite: {
    eye:'Mini-leçon', tit:"Livres, kilos et grammes",
    blocs:[
      {t:'texte', h:"Deux systèmes dans la même phrase",
       p:"Au Québec, les étiquettes sont en <b>grammes et kilogrammes</b> — c'est le système officiel. Mais à l'oral, pour la viande et les fruits, la <b>livre</b> reste très employée. Vous entendrez les deux dans la même conversation, et c'est normal.",
       note:"Personne ne vous corrigera si vous commandez en grammes. La balance affiche les deux."},

      {t:'ana', h:"La livre",
       p:"Une unité héritée du système impérial, encore vivante dans l'alimentation.",
       mots:[['1 livre','≈ {454} grammes'],['1 kilo','≈ 2,2 livres',true],['Une livre et demie','≈ 680 g']],
       say:"Quatre poitrines, ça fait environ une livre et demie.",
       note:"Repère commode : une livre, c'est <b>un peu moins</b> qu'un demi-kilo. Un kilo, c'est un peu plus de deux livres."},

      {t:'ana', h:"Les repères à mémoriser",
       p:"Quatre équivalences suffisent pour tout le quotidien.",
       mots:[['100 g','une petite tranche de jambon'],['250 g','une demi-livre',true],['500 g','un peu plus d\'une livre']],
       say:"Donnez-moi deux cents grammes de jambon tranché mince.",
       note:"Deux cents grammes de jambon font environ une douzaine de tranches minces : c'est la commande la plus courante."},

      {t:'ana', h:"Les liquides",
       p:"Toujours en litres et en millilitres, sans exception.",
       mots:[['1 litre','1000 ml'],['1 tasse','≈ {250} ml',true],['1 cuillère à soupe','≈ 15 ml']],
       say:"Diluer trente millilitres dans quatre litres d'eau tiède.",
       note:"Les recettes d'ici mélangent tasses et millilitres. Les deux repères ci-dessus permettent de passer de l'un à l'autre."},

      {t:'texte', h:"Commander dans l'unité qu'on veut",
       p:"« Une livre » et « cinq cents grammes » sont tous les deux compris et acceptés. Choisissez celle que vous maîtrisez, et regardez la balance : elle affiche le poids et le prix, et vous pouvez toujours dire « un peu moins » ou « un peu plus ».",
       note:"« Un peu plus, ça va ? » est la phrase que la personne au comptoir dira presque toujours. Répondre « oui, parfait » suffit."},

      {t:'labo', h:"Combien ça fait ?",
       p:"Choisissez une quantité et voyez son équivalent.",
       axes:[{id:'p', lbl:'Quelle quantité ?', opts:[
         ['a','une livre'],
         ['b','une livre et demie'],
         ['c','deux cents grammes'],
         ['d','un kilo'],
         ['e','trente millilitres']]}],
       out:{
         a:{w:['≈ {454} grammes'], say:"Une livre, c'est environ quatre cent cinquante grammes.", n:'un peu moins qu\'un demi-kilo'},
         b:{w:['≈ {680} grammes'], say:"Quatre poitrines, ça fait environ une livre et demie.", n:'la commande de poulet du module'},
         c:{w:['≈ une {douzaine} de tranches'], say:"Deux cents grammes, ça vous en fait une douzaine de tranches.", n:'la commande de jambon du module'},
         d:{w:['≈ {2,2} livres'], say:"Un kilo, c'est un peu plus de deux livres.", n:'le repère le plus utile'},
         e:{w:['≈ deux {cuillères} à soupe'], say:"Trente millilitres, c'est deux cuillères à soupe.", n:'la dose du nettoyant'},
       },
       note:"Les cinq quantités viennent du module. Elles couvrent presque toutes les commandes ordinaires."},

      {t:'ex', h:"Les quantités du module",
       p:"Écoutez chacune.",
       rows:[
         ["Quatre poitrines, ça fait environ une livre et demie.","viande au poids"],
         ["Une livre de bœuf haché.","commande simple"],
         ["Deux cents grammes de jambon tranché mince.","charcuterie"],
         ["Un sac de riz de huit kilos.","produits secs"],
         ["Diluer trente millilitres dans quatre litres d'eau.","liquide"],
         ["Ça fait cinq dollars quarante.","le prix, à vérifier"],
       ]},

      {t:'piege', h:"Trois pièges à connaître",
       rows:[
         ["confondre livre et kilo","une livre ≈ 454 g, pas 1000 g",
          "Commander « un kilo » en pensant « une livre » double la quantité — et le prix."],
         ["croire qu'il faut choisir un système","les deux sont acceptés partout",
          "Commandez dans l'unité que vous connaissez. La balance et la personne au comptoir font la conversion."],
         ["ne pas vérifier le prix","« ça fait combien ? » avant de repartir",
          "Le poids exact est rarement celui demandé : la personne coupe « un peu plus ». Le prix final n'est donc jamais celui qu'on avait calculé."],
       ]},

      {t:'check', h:"Est-ce que c'est clair maintenant ?",
       p:"Quatre questions rapides.",
       qs:[
         {q:"Une livre vaut environ…", opts:["454 grammes","1000 grammes"], ok:0,
          fb:"Un peu moins qu'un demi-kilo."},
         {q:"Un kilo vaut environ…", opts:["une livre","deux livres"], ok:1,
          fb:"2,2 livres, plus précisément."},
         {q:"Les liquides se mesurent…", opts:["en livres","en litres et millilitres"], ok:1,
          fb:"Toujours, sans exception."},
         {q:"Peut-on commander en grammes plutôt qu'en livres ?", opts:["oui, partout","non, il faut employer la livre"], ok:0,
          fb:"Les deux sont compris et acceptés."},
       ]},
    ]
  },

  t3etiq: {
    eye:'Mini-leçon', tit:"Les trois lignes qui comptent",
    blocs:[
      {t:'texte', h:"Quarante chiffres, trois utiles",
       p:"Un tableau de valeur nutritive contient une quarantaine de chiffres. Trois seulement servent au quotidien : la <b>portion</b>, le <b>sodium</b> et les <b>sucres</b>. Le reste ne s'examine que si on cherche quelque chose de précis.",
       note:"Farida a mis deux ans à comprendre cela. Ça se dit en une minute."},

      {t:'ana', h:"La portion, tout en haut",
       p:"C'est la ligne la plus importante, et la plus ignorée.",
       mots:[['Où','la {première} ligne'],['Ce que ça dit','tous les chiffres valent pour ça',true],['Le piège','ce n\'est pas le contenant']],
       say:"La portion, en haut. Tout le tableau parle de cette portion-là.",
       note:"Deux marques qui affichent des portions différentes ne se comparent pas directement : il faut d'abord ramener au même poids."},

      {t:'ana', h:"Le sodium et les sucres",
       p:"Les deux lignes qui varient le plus d'une marque à l'autre.",
       mots:[['Marque A','{240} mg de sodium'],['Marque B','{80} mg de sodium',true],['L\'écart','du simple au triple']],
       say:"Deux cent quarante milligrammes contre quatre-vingts.",
       note:"C'est exactement l'écart du dialogue du module, entre deux pâtes de tomate qui se ressemblent."},

      {t:'ana', h:"La colonne du pourcentage",
       p:"À droite, une colonne dit si c'est beaucoup ou peu, sans qu'on ait à calculer.",
       mots:[['5 % ou moins','c\'est {peu}'],['15 % ou plus','c\'est {beaucoup}',true],['Entre les deux','c\'est moyen']],
       say:"Cinq pour cent ou moins, c'est peu. Quinze pour cent ou plus, c'est beaucoup.",
       note:"Ce repère est officiel et il figure sur les documents de Santé Canada. Il vaut pour toutes les lignes du tableau."},

      {t:'texte', h:"La date : deux choses différentes",
       p:"<b>« Meilleur avant »</b> est une date de <u>qualité</u> : après, le goût ou la texture changent, mais l'aliment n'est pas dangereux. <b>« Date limite d'utilisation »</b> est une date de <u>sécurité</u> : après, on ne consomme pas. On la trouve surtout sur les préparations pour nourrissons et quelques produits frais.",
       note:"Confondre les deux fait jeter beaucoup de nourriture encore bonne — ou en garder qui ne l'est plus."},

      {t:'labo', h:"Où regarder ?",
       p:"Choisissez une question et voyez où se trouve la réponse.",
       axes:[{id:'p', lbl:'Quelle question ?', opts:[
         ['a','Ces chiffres valent pour combien ?'],
         ['b','Est-ce que c\'est salé ?'],
         ['c','Est-ce que c\'est sucré ?'],
         ['d','Est-ce que 15 %, c\'est beaucoup ?'],
         ['e','Est-ce encore bon après la date ?']]}],
       out:{
         a:{w:['la {portion}, en haut'], say:"La portion, en haut. Tout le tableau parle de cette portion-là.", n:'jamais le contenant entier'},
         b:{w:['la ligne du {sodium}'], say:"Regardez la ligne du sodium.", n:'la ligne qui varie le plus'},
         c:{w:['la ligne des {sucres}'], say:"Ensuite le sodium, et le sucre.", n:'l\'autre ligne à surveiller'},
         d:{w:['{oui} — 15 % ou plus'], say:"Quinze pour cent ou plus, c'est beaucoup.", n:'le repère officiel'},
         e:{w:['{oui} si « meilleur avant »'], say:"« Meilleur avant » veut dire que le goût change après.", n:'qualité, pas danger'},
       },
       note:"La dernière est celle qui économise le plus d'argent : « meilleur avant » n'est pas une date de danger."},

      {t:'ex', h:"Les phrases du module",
       p:"Écoutez chacune.",
       rows:[
         ["La portion, en haut. Tout le tableau parle de cette portion-là.","la ligne à lire en premier"],
         ["Ensuite le sodium, et le sucre.","les deux lignes qui varient"],
         ["Deux cent quarante milligrammes contre quatre-vingts.","l'écart entre deux marques"],
         ["Le tableau est toujours au dos, en noir et blanc.","toujours au même endroit"],
         ["« Meilleur avant » veut dire que le goût change après.","une date de qualité"],
         ["« Date limite d'utilisation », ça, c'est sérieux.","une date de sécurité"],
       ]},

      {t:'piege', h:"Trois pièges à connaître",
       rows:[
         ["comparer sans regarder la portion","deux marques, deux portions différentes",
          "Les chiffres ne se comparent que si les portions sont les mêmes. Sinon, c'est une comparaison fausse."],
         ["jeter après « meilleur avant »","c'est une date de qualité",
          "Beaucoup d'aliments restent parfaitement bons après cette date. Fiez-vous à l'odeur et à l'aspect."],
         ["lire tout le tableau","trois lignes suffisent",
          "Portion, sodium, sucres. Le reste ne se lit que si vous cherchez quelque chose de précis."],
       ]},

      {t:'check', h:"Est-ce que c'est clair maintenant ?",
       p:"Quatre questions rapides.",
       qs:[
         {q:"Les chiffres du tableau valent pour…", opts:["le contenant entier","la portion indiquée en haut"], ok:1,
          fb:"C'est la ligne la plus importante du tableau."},
         {q:"15 % dans la colonne de droite, c'est…", opts:["peu","beaucoup"], ok:1,
          fb:"5 % ou moins, c'est peu ; 15 % ou plus, c'est beaucoup."},
         {q:"« Meilleur avant » est une date…", opts:["de qualité","de danger"], ok:0,
          fb:"C'est « date limite d'utilisation » qui est une date de sécurité."},
         {q:"Le tableau se trouve…", opts:["toujours au dos","à un endroit différent selon la marque"], ok:0,
          fb:"Toujours au même endroit, en noir et blanc."},
       ]},
    ]
  },

  t3mode: {
    eye:'Mini-leçon', tit:"Un mode d'emploi en trois blocs",
    blocs:[
      {t:'texte', h:"Toujours le même ordre",
       p:"Le mode d'emploi d'un produit d'entretien tient en trois blocs, toujours disposés de la même façon : la <b>dose</b> en haut, les <b>étapes</b> au milieu, les <b>avertissements</b> en bas. Une fois qu'on le sait, on trouve ce qu'on cherche en cinq secondes.",
       note:"C'est vrai des nettoyants, des savons, des détachants — et de la plupart des produits vendus en épicerie."},

      {t:'ana', h:"1 · La dose, en haut",
       p:"Combien de produit, dans combien d'eau.",
       mots:[['La formule','{Diluer} 30 ml dans 4 litres'],['L\'outil','un bouchon doseur',true],['L\'équivalent','30 ml ≈ 2 c. à soupe']],
       say:"Diluer trente millilitres dans quatre litres d'eau tiède.",
       note:"Presque toutes les bouteilles ont un bouchon doseur. Deux fois trop de produit ne nettoie pas mieux : ça laisse un film collant."},

      {t:'ana', h:"2 · Les étapes, au milieu",
       p:"À l'impératif, dans l'ordre où il faut les faire.",
       mots:[['Étape 1','{Appliquer} sur la surface'],['Étape 2','Laisser agir deux minutes',true],['Étape 3','Rincer à l\'eau claire']],
       say:"Rincer à l'eau claire.",
       note:"Le verbe est souvent à l'infinitif dans les textes imprimés (« diluer », « rincer ») plutôt qu'à l'impératif. Cela veut dire la même chose."},

      {t:'ana', h:"3 · Les avertissements, en bas",
       p:"Séparés du reste, souvent en gras, avec un triangle.",
       mots:[['Le plus important','{Ne pas mélanger} avec un produit chloré'],['Le plus fréquent','Tenir hors de la portée des enfants',true],['Le signe','un triangle']],
       say:"Ne pas mélanger avec un produit chloré.",
       note:"Cet avertissement n'est pas une formalité : un nettoyant et de l'eau de Javel dégagent un gaz toxique. C'est un accident domestique courant."},

      {t:'texte', h:"Les mesures dont vous avez besoin",
       p:"<b>30 ml</b> ≈ deux cuillères à soupe · <b>15 ml</b> ≈ une cuillère à soupe · <b>250 ml</b> ≈ une tasse · <b>1 litre</b> = 1000 ml. Avec ces quatre repères, tous les modes d'emploi d'épicerie deviennent lisibles.",
       note:"Si vous n'avez pas de bouchon doseur, une cuillère à soupe de cuisine fait très bien l'affaire."},

      {t:'labo', h:"Dans quel bloc ?",
       p:"Choisissez une phrase et voyez où elle se trouve.",
       axes:[{id:'p', lbl:'Quelle phrase ?', opts:[
         ['a','Diluer 30 ml dans 4 litres.'],
         ['b','Laisser agir deux minutes.'],
         ["c",'Rincer à l\'eau claire.'],
         ['d','Ne pas mélanger avec un produit chloré.'],
         ['e','Tenir hors de la portée des enfants.']]}],
       out:{
         a:{w:['la {dose} — en haut'], say:"Diluer trente millilitres dans quatre litres d'eau tiède.", n:'combien de produit, dans combien d\'eau'},
         b:{w:['les {étapes} — au milieu'], say:"Laisser agir deux minutes.", n:'dans l\'ordre où il faut les faire'},
         c:{w:['les {étapes} — au milieu'], say:"Rincer à l'eau claire.", n:'la dernière étape, presque toujours'},
         d:{w:['les {avertissements} — en bas'], say:"Ne pas mélanger avec un produit chloré.", n:'en gras, avec un triangle'},
         e:{w:['les {avertissements} — en bas'], say:"Tenir hors de la portée des enfants.", n:'sur tous les produits d\'entretien'},
       },
       note:"Trois blocs, cinq phrases : c'est la structure complète d'une étiquette de nettoyant."},

      {t:'ex', h:"Le mode d'emploi complet",
       p:"Écoutez chaque ligne, dans l'ordre.",
       rows:[
         ["Diluer trente millilitres dans quatre litres d'eau tiède.","la dose"],
         ["Utiliser le bouchon doseur fourni.","la dose"],
         ["Laisser agir deux minutes.","une étape"],
         ["Rincer à l'eau claire.","une étape"],
         ["Ne pas mélanger avec un produit chloré.","un avertissement"],
         ["Tenir hors de la portée des enfants.","un avertissement"],
       ]},

      {t:'piege', h:"Trois pièges à connaître",
       rows:[
         ["en mettre plus pour mieux nettoyer","deux fois la dose ne nettoie pas mieux",
          "Le produit laisse un film collant qui attire la saleté. La dose est calculée : c'est la bonne."],
         ["sauter les avertissements","ils sont en bas, pas parce qu'ils sont moins importants",
          "Ils sont séparés du reste justement pour être trouvés vite. C'est la partie à lire en premier sur un produit qu'on ne connaît pas."],
         ["mélanger deux produits","un nettoyant et de l'eau de Javel dégagent un gaz toxique",
          "C'est l'accident domestique le plus fréquent avec les produits d'entretien. L'avertissement est sur presque toutes les bouteilles."],
       ]},

      {t:'check', h:"Est-ce que c'est clair maintenant ?",
       p:"Quatre questions rapides.",
       qs:[
         {q:"La dose se trouve…", opts:["en haut","en bas"], ok:0,
          fb:"Dose en haut, étapes au milieu, avertissements en bas."},
         {q:"Trente millilitres, c'est environ…", opts:["une tasse","deux cuillères à soupe"], ok:1,
          fb:"Une tasse, c'est 250 ml."},
         {q:"Mettre deux fois la dose…", opts:["nettoie mieux","laisse un film collant"], ok:1,
          fb:"La dose est calculée. En mettre plus nuit au résultat."},
         {q:"« Ne pas mélanger avec un produit chloré » est…", opts:["une formalité","un vrai danger"], ok:1,
          fb:"Le mélange dégage un gaz toxique."},
       ]},
    ]
  },
};
