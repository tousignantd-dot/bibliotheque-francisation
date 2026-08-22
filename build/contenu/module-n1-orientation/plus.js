const PLUS = {
  prSons: {
    eye:'Mini-leçon', tit:"Trois sons pour commencer : [a], [i], [ou]",
    blocs:[
      {t:'texte', h:"Trois sons, et beaucoup de mots",
       p:"Le français a beaucoup de sons. Trois d'entre eux se disent partout, dans presque tous les mots du centre : <b>[a]</b>, <b>[i]</b> et <b>[ou]</b>. Ce sont les trois plus faciles à entendre et les trois plus faciles à dire — on commence par eux.",
       note:"Ces trois sons existent dans presque toutes les langues du monde. Vous les connaissez déjà : il faut seulement les reconnaître à l'écrit."},

      {t:'ana', h:"[a] — la bouche grande ouverte",
       p:"On écrit <b>a</b>.",
       mots:[['Dans un mot court','l{a} · s{a}lle'],['Dans un mot du centre','c{a}fétéri{a}'],['La bouche','grande ouverte, la langue en bas',true]],
       say:"La. Salle. Cafétéria.",
       note:"C'est le son le plus ouvert du français. Mettez un doigt entre les dents : il passe."},

      {t:'ana', h:"[i] — la bouche presque fermée",
       p:"On écrit <b>i</b>, ou parfois <b>y</b>.",
       mots:[['Dans un mot court','l{i}t · {i}c{i}'],['Dans un mot du centre','sort{i}e'],['La bouche','étirée sur les côtés, comme un sourire',true]],
       say:"Lit. Ici. Sortie.",
       note:"Souriez en le disant : le son sort tout seul."},

      {t:'ana', h:"[ou] — les lèvres en rond",
       p:"Il s'écrit avec <b>deux</b> lettres : <b>ou</b>.",
       mots:[['Dans un mot court','l{ou}p · n{ou}s'],['Dans un mot du centre','p{ou}ssez'],['La bouche','les lèvres serrées en rond, en avant',true]],
       say:"Loup. Nous. Poussez.",
       note:"Deux lettres, un seul son. C'est la première chose surprenante de l'écriture française — et la plus utile à savoir tout de suite."},

      {t:'labo', h:"Écoutez et comparez",
       p:"Choisissez une paire de mots.",
       axes:[{id:'p', lbl:'Quelle paire ?', opts:[
         ['a','la / lit'],
         ['b','la / loup'],
         ['c','lit / loup'],
         ['d','salle / sortie'],
         ['e','sortie / poussez']]}],
       out:{
         a:{w:['la','lit'], say:"La. Lit.", n:'[a] bouche ouverte, [i] bouche étirée'},
         b:{w:['la','loup'], say:"La. Loup.", n:'[a] bouche ouverte, [ou] lèvres en rond'},
         c:{w:['lit','loup'], say:"Lit. Loup.", n:'les deux sont fermés, mais les lèvres changent'},
         d:{w:['salle','sortie'], say:"Salle. Sortie.", n:'deux mots du centre, deux sons différents'},
         e:{w:['sortie','poussez'], say:"Sortie. Poussez.", n:'[i] puis [ou] : le sourire, puis le rond'},
       },
       note:"Écoutez deux fois, puis répétez à voix haute. Regardez vos lèvres dans une vitre."},

      {t:'ex', h:"À écouter et à répéter",
       p:"Six mots du centre.",
       rows:[
         ["la salle","[a] deux fois"],
         ["la cafétéria","[a] trois fois"],
         ["ici","[i] deux fois"],
         ["la sortie","[i] à la fin"],
         ["poussez","[ou] au début"],
         ["nous","[ou] à la fin"],
       ]},

      {t:'piege', h:"Trois pièges à connaître",
       rows:[
         ["lire « ou » comme deux sons","« o-u »",
          "Non : <b>ou</b> s'écrit avec deux lettres mais se dit d'un seul son, les lèvres en rond. C'est la règle qui surprend le plus au début."],
         ["confondre [i] et [ou]","« sortie » et « sortou »",
          "Les deux sont fermés, mais les lèvres ne font pas la même chose : étirées pour [i], en rond pour [ou]."],
         ["croire qu'il faut tout savoir d'un coup","le français a beaucoup d'autres sons",
          "Trois suffisent pour commencer. Les autres viendront avec les mots, pas avant."],
       ]},

      {t:'check', h:"Est-ce que c'est clair maintenant ?",
       p:"Quatre questions rapides.",
       qs:[
         {q:"Dans « poussez », on entend…", opts:["[ou]","[i]"], ok:0,
          fb:"Les lèvres en rond, au début du mot."},
         {q:"« ou » s'écrit avec deux lettres et se dit…", opts:["en deux sons","en un seul son"], ok:1,
          fb:"Deux lettres, un seul son."},
         {q:"Pour dire [i], la bouche est…", opts:["étirée comme un sourire","grande ouverte"], ok:0,
          fb:"Souriez : le son sort tout seul."},
         {q:"Dans « cafétéria », on entend [a]…", opts:["une fois","plusieurs fois"], ok:1,
          fb:"Trois fois, en comptant le a final."},
       ]},
    ]
  },

  prMaj: {
    eye:'Mini-leçon', tit:"MAJUSCULES et minuscules — le même mot",
    blocs:[
      {t:'texte', h:"Deux tailles pour chaque lettre",
       p:"En français, chaque lettre s'écrit de deux façons : la <b>grande</b> — on dit une <b>majuscule</b> — et la <b>petite</b> — une <b>minuscule</b>. A et a, S et s, E et e. Ce sont les mêmes lettres et le même son. Seule la taille change.",
       note:"C'est la première chose à savoir pour lire un panneau : sinon on croit voir un mot nouveau alors qu'on le connaît déjà."},

      {t:'ana', h:"Les panneaux prennent les grandes",
       p:"Pour qu'on les voie de loin.",
       mots:[['Sur la porte','{SORTIE}'],['Sur le mur','{TOILETTES}'],['Toutes les lettres','sont grandes, du début à la fin',true]],
       say:"Sortie. Toilettes.",
       note:"Presque tous les panneaux du Québec sont écrits ainsi. C'est une habitude, pas une règle de grammaire."},

      {t:'ana', h:"Les livres prennent les petites",
       p:"Le même mot, en plus petit.",
       mots:[['Dans le cahier','{sortie}'],['Dans le livre','{toilettes}'],['C\'est le même mot','même lettres, même son',true]],
       say:"Sortie. Toilettes.",
       note:"Quand vous copiez un panneau dans votre cahier, vous avez le droit d'écrire en grandes lettres. C'est plus facile au début."},

      {t:'ana', h:"Une lettre change beaucoup de forme",
       p:"Quelques paires à regarder de près.",
       mots:[['Presque pareilles','C et c · S et s · O et o'],['Un peu différentes','E et e · A et a'],['Très différentes','G et g · R et r · D et d',true]],
       say:"C, c. S, s. E, e. G, g. R, r.",
       note:"Les trois dernières paires demandent un peu de temps. Ce n'est pas vous : elles ne se ressemblent vraiment pas."},

      {t:'labo', h:"Le même mot, deux fois",
       p:"Choisissez un mot du centre.",
       axes:[{id:'p', lbl:'Quel mot ?', opts:[
         ['a','sortie'],
         ['b','entrée'],
         ['c','toilettes'],
         ['d','accueil'],
         ['e','cafétéria']]}],
       out:{
         a:{w:['SORTIE','sortie'], say:"Sortie.", n:'six lettres, deux écritures'},
         b:{w:['ENTRÉE','entrée'], say:"Entrée.", n:"l'accent reste sur le É, même en grande lettre"},
         c:{w:['TOILETTES','toilettes'], say:"Toilettes.", n:'neuf lettres : un mot long à reconnaître'},
         d:{w:['ACCUEIL','accueil'], say:"Accueil.", n:'deux C, et un U qui ne s\'entend pas'},
         e:{w:['CAFÉTÉRIA','cafétéria'], say:"Cafétéria.", n:'quatre syllabes : ca-fé-té-ria'},
       },
       note:"Lisez la grande, puis la petite. C'est le même mot : votre œil doit finir par les voir ensemble."},

      {t:'ex', h:"À écouter et à répéter",
       p:"Six mots, deux écritures.",
       rows:[
         ["SORTIE — sortie","la porte par où on part"],
         ["ENTRÉE — entrée","la porte par où on arrive"],
         ["TOILETTES — toilettes","les lavabos"],
         ["ACCUEIL — accueil","le comptoir du début"],
         ["POUSSEZ — poussez","la porte va loin de moi"],
         ["CAFÉTÉRIA — cafétéria","on y mange à midi"],
       ]},

      {t:'piege', h:"Trois pièges à connaître",
       rows:[
         ["croire que c'est un autre mot","SORTIE et sortie",
          "C'est le même mot. Si vous connaissez l'un, vous connaissez l'autre : la lettre change de taille, pas de son."],
         ["chercher l'accent sur la grande lettre","ENTREE au lieu de ENTRÉE",
          "Beaucoup de panneaux au Québec oublient les accents sur les majuscules. Le mot reste le même et se dit pareil."],
         ["écrire son nom tout en majuscules dans un cahier","ROSA au lieu de Rosa",
          "Sur un formulaire, on le demande souvent — c'est plus lisible. Dans une phrase, seule la première lettre du nom est grande."],
       ]},

      {t:'check', h:"Est-ce que c'est clair maintenant ?",
       p:"Quatre questions rapides.",
       qs:[
         {q:"SORTIE et sortie, c'est…", opts:["le même mot","deux mots différents"], ok:0,
          fb:"La taille change, pas le mot."},
         {q:"Sur les panneaux, on écrit surtout en…", opts:["minuscules","majuscules"], ok:1,
          fb:"On les voit de plus loin."},
         {q:"La grande lettre se dit…", opts:["plus fort","pareil"], ok:1,
          fb:"Même lettre, même son."},
         {q:"« Une majuscule », c'est…", opts:["la grande lettre","la petite lettre"], ok:0,
          fb:"La petite s'appelle une minuscule."},
       ]},
    ]
  },

  t1art: {
    eye:'Mini-leçon', tit:"Le, la, les, l' — devant le nom d'un lieu",
    blocs:[
      {t:'texte', h:"Un petit mot devant chaque nom",
       p:"En français, un nom ne vient presque jamais tout seul : il y a un petit mot devant. <b>le</b> vestiaire, <b>la</b> cafétéria, <b>les</b> toilettes, <b>l'</b>accueil. Ce petit mot ne veut rien dire à lui seul — mais on l'entend, et on l'attend.",
       note:"Beaucoup de langues n'ont pas ce petit mot. Si le français est votre deuxième langue, c'est peut-être la chose la plus étrange du début."},

      {t:'ana', h:"le et la",
       p:"Selon le nom, pas selon la personne.",
       mots:[['Masculin','{le} vestiaire · {le} panneau'],['Féminin','{la} cafétéria · {la} sortie'],['On ne devine pas','on apprend le petit mot avec le nom',true]],
       say:"Le vestiaire. La cafétéria.",
       note:"Le nom d'un lieu n'a rien d'un homme ni d'une femme : « masculin » et « féminin » sont ici deux étiquettes, rien de plus."},

      {t:'ana', h:"les, quand il y en a plusieurs",
       p:"Ou quand le mot est toujours au pluriel.",
       mots:[['Plusieurs','{les} panneaux · {les} portes'],['Toujours pluriel','{les} toilettes'],['On entend un [e]','« lé »',true]],
       say:"Les panneaux. Les toilettes.",
       note:"« Les toilettes » est toujours au pluriel en français, même s'il n'y a qu'une seule petite salle. C'est ainsi."},

      {t:'ana', h:"l' devant une voyelle",
       p:"Le petit mot se colle au nom.",
       mots:[['On dit','{l\'}accueil · {l\'}entrée'],['On ne dit pas','le accueil · la entrée'],['On entend un seul mot','« laccueil »',true]],
       say:"L'accueil. L'entrée.",
       note:"C'est pour éviter deux voyelles collées. Le français n'aime pas cela, et il le montre souvent."},

      {t:'labo', h:"Choisissez un lieu",
       p:"Écoutez le nom avec son petit mot.",
       axes:[{id:'p', lbl:'Quel lieu ?', opts:[
         ['a','cafétéria'],
         ['b','vestiaire'],
         ['c','toilettes'],
         ['d','accueil'],
         ['e','sortie'],
         ['f','service de garde']]}],
       out:{
         a:{w:['la cafétéria'], say:"La cafétéria.", n:'féminin'},
         b:{w:['le vestiaire'], say:"Le vestiaire.", n:'masculin'},
         c:{w:['les toilettes'], say:"Les toilettes.", n:'toujours au pluriel'},
         d:{w:["l'accueil"], say:"L'accueil.", n:"l' devant une voyelle"},
         e:{w:['la sortie'], say:"La sortie.", n:'féminin'},
         f:{w:['le service de garde'], say:"Le service de garde.", n:'masculin, et trois mots ensemble'},
       },
       note:"Apprenez toujours le petit mot avec le nom. « Cafétéria » seul ne s'apprend pas ; « la cafétéria », oui."},

      {t:'ex', h:"À écouter et à répéter",
       p:"Six lieux du centre.",
       rows:[
         ["la cafétéria","on y mange"],
         ["les toilettes","toujours au pluriel"],
         ["le vestiaire","on y laisse son manteau"],
         ["l'accueil","le comptoir du début"],
         ["l'entrée","la porte par où on arrive"],
         ["le service de garde","pour les petits enfants"],
       ]},

      {t:'piege', h:"Trois pièges à connaître",
       rows:[
         ["dire le nom tout seul","« cafétéria, s'il vous plaît »",
          "On comprendra, mais on entend tout de suite qu'il manque quelque chose. Dites « la cafétéria »."],
         ["chercher une logique","pourquoi « le » vestiaire et « la » sortie ?",
          "Il n'y en a pas. Le petit mot s'apprend avec le nom, comme une seule pièce."],
         ["dire « le toilettes »","le mot est toujours au pluriel",
          "On dit <b>les</b> toilettes, même pour une seule salle."],
       ]},

      {t:'check', h:"Est-ce que c'est clair maintenant ?",
       p:"Quatre questions rapides.",
       qs:[
         {q:"___ toilettes sont au fond.", opts:["Le","Les"], ok:1,
          fb:"Toujours au pluriel."},
         {q:"Je vais à ___ accueil.", opts:["l'","le"], ok:0,
          fb:"Devant une voyelle, le petit mot se colle."},
         {q:"___ cafétéria est ouverte.", opts:["Le","La"], ok:1,
          fb:"Cafétéria est féminin."},
         {q:"On apprend le petit mot…", opts:["avec le nom","plus tard"], ok:0,
          fb:"Les deux ensemble, comme une seule pièce."},
       ]},
    ]
  },

  t1cest: {
    eye:'Mini-leçon', tit:"C'est · Ce n'est pas · C'est ici ?",
    blocs:[
      {t:'texte', h:"Trois phrases suffisent devant une porte",
       p:"Devant un panneau, on ne fait que trois choses : on <b>nomme</b> — « C'est la cafétéria » ; on <b>corrige</b> — « Ce n'est pas la cafétéria » ; on <b>demande</b> — « C'est ici ? ». Trois phrases, et tout le module tient dedans.",
       note:"« C'est » est la phrase la plus courte du français et l'une des plus utiles. Elle sert à nommer n'importe quoi."},

      {t:'ana', h:"C'est — pour nommer",
       p:"On met le nom juste après, avec son petit mot.",
       mots:[['On dit','{C\'est} la cafétéria.'],['Aussi','{C\'est} le vestiaire.'],['On ne dit pas','c\'est cafétéria',true]],
       say:"C'est la cafétéria. C'est le vestiaire.",
       note:"Le petit mot — le, la, les — reste toujours là, même après « c'est »."},

      {t:'ana', h:"Ce n'est pas — pour dire que non",
       p:"Deux petits mots autour du verbe : ne… pas.",
       mots:[['On dit','{Ce n\'est pas} l\'accueil.'],['À l\'oral, souvent','{C\'est pas} l\'accueil.'],['Les deux sont bons','le second est simplement plus rapide',true]],
       say:"Ce n'est pas l'accueil. C'est pas l'accueil.",
       note:"Au Québec, on entend « c'est pas » tout le temps, dans toutes les situations. Écrivez « ce n'est pas » ; dites ce que vous voulez."},

      {t:'ana', h:"C'est ici ? — pour demander",
       p:"Les mêmes mots, la voix qui monte.",
       mots:[['On affirme','C\'est ici. ↓'],['On demande','C\'est ici ? ↑'],['Rien ne change','sauf la voix, à la fin',true]],
       say:"C'est ici. C'est ici ?",
       note:"C'est la façon la plus simple de poser une question en français : garder la phrase et monter la voix. Elle marche partout."},

      {t:'labo', h:"Devant quel panneau ?",
       p:"Choisissez un panneau et une phrase.",
       axes:[
         {id:'p', lbl:'Quel panneau ?', opts:[['a','CAFÉTÉRIA'],['b','ACCUEIL'],['c','SORTIE']]},
         {id:'q', lbl:'Quelle phrase ?', opts:[['1','je nomme'],['2','je dis que non'],['3','je demande']]}],
       out:{
         a1:{w:["C'est la cafétéria."], say:"C'est la cafétéria.", n:'on nomme ce qu\'on voit'},
         a2:{w:["Ce n'est pas la cafétéria."], say:"Ce n'est pas la cafétéria.", n:'ne… pas autour du verbe'},
         a3:{w:["La cafétéria, c'est ici ?"], say:"La cafétéria, c'est ici ?", n:'la voix monte à la fin'},
         b1:{w:["C'est l'accueil."], say:"C'est l'accueil.", n:"l' devant une voyelle"},
         b2:{w:["Ce n'est pas l'accueil."], say:"Ce n'est pas l'accueil.", n:'à l\'oral : « c\'est pas »'},
         b3:{w:["L'accueil, c'est ici ?"], say:"L'accueil, c'est ici ?", n:'on nomme, puis on demande'},
         c1:{w:["C'est la sortie."], say:"C'est la sortie.", n:'féminin : la sortie'},
         c2:{w:["Ce n'est pas la sortie."], say:"Ce n'est pas la sortie.", n:'utile devant une porte fermée'},
         c3:{w:["La sortie, c'est ici ?"], say:"La sortie, c'est ici ?", n:'la question la plus courte'},
       },
       note:"Neuf phrases. Choisissez-en trois et dites-les à voix haute devant une vraie porte."},

      {t:'ex', h:"À écouter et à répéter",
       p:"Six phrases devant une porte.",
       rows:[
         ["C'est la cafétéria.","je nomme"],
         ["C'est le vestiaire.","je nomme"],
         ["Ce n'est pas ici.","je dis que non"],
         ["C'est pas ici.","à l'oral"],
         ["Les toilettes, c'est ici ?","je demande"],
         ["Merci, madame.","je remercie"],
       ]},

      {t:'piege', h:"Trois pièges à connaître",
       rows:[
         ["oublier le petit mot","« c'est cafétéria »",
          "Après « c'est », le nom garde toujours son petit mot : « c'est <b>la</b> cafétéria »."],
         ["croire que « c'est pas » est une faute","tout le monde le dit",
          "À l'oral, le « ne » tombe presque toujours. Ce n'est pas familier au point de déranger : c'est le français parlé ordinaire. À l'écrit, on garde « ce n'est pas »."],
         ["ne pas oser demander","tourner en rond dans le corridor",
          "« C'est ici ? » fait trois mots et on vous répondra toujours. C'est la phrase à sortir dès qu'un doute se présente."],
       ]},

      {t:'check', h:"Est-ce que c'est clair maintenant ?",
       p:"Quatre questions rapides.",
       qs:[
         {q:"Pour nommer un lieu, on dit…", opts:["c'est","il y a"], ok:0,
          fb:"C'est la cafétéria."},
         {q:"Après « c'est », le nom garde…", opts:["son petit mot","rien"], ok:0,
          fb:"C'est <b>la</b> cafétéria."},
         {q:"Pour demander, on change…", opts:["les mots","la voix"], ok:1,
          fb:"La voix monte à la fin."},
         {q:"« C'est pas ici » est…", opts:["une faute","du français parlé ordinaire"], ok:1,
          fb:"À l'écrit, on écrit « ce n'est pas »."},
       ]},
    ]
  },

  t2ordre: {
    eye:'Mini-leçon', tit:"POUSSEZ, TIREZ — les panneaux qui donnent un ordre",
    blocs:[
      {t:'texte', h:"Un mot, un geste",
       p:"Certains panneaux ne nomment aucun endroit : ils disent <b>quoi faire</b>. POUSSEZ, TIREZ, ENTREZ, SONNEZ, ATTENDEZ. Tous finissent par les mêmes deux lettres — <b>-EZ</b> — et tous demandent un geste, tout de suite.",
       note:"Ces mots ne s'adressent à personne en particulier. Le panneau parle à tout le monde qui passe."},

      {t:'ana', h:"POUSSEZ — la porte va loin de moi",
       p:"La main pousse vers l'avant.",
       mots:[['Sur la porte','{POUSSEZ}'],['Le geste','la main pousse, le bras se tend'],['On entend','« pou-ssé » — le Z ne se dit pas',true]],
       say:"Poussez.",
       note:"Souvent, une plaque de métal large remplace la poignée : c'est le signe qu'il faut pousser, même sans mot."},

      {t:'ana', h:"TIREZ — la porte vient vers moi",
       p:"La main tire vers soi.",
       mots:[['Sur la porte','{TIREZ}'],['Le geste','la main serre la poignée et ramène'],['On entend','« ti-ré » — le Z ne se dit pas non plus',true]],
       say:"Tirez.",
       note:"Une vraie poignée à saisir, plutôt qu'une plaque plate : c'est presque toujours qu'il faut tirer."},

      {t:'ana', h:"-EZ à la fin, « é » dans l'oreille",
       p:"Toujours pareil, sur tous les panneaux.",
       mots:[['On écrit','pouss{ez} · tir{ez} · entr{ez}'],['On entend','poussé · tiré · entré'],['Le Z','ne se prononce jamais ici',true]],
       say:"Poussez. Tirez. Entrez.",
       note:"Cette terminaison revient partout en français, bien au-delà des panneaux. La reconnaître maintenant fait gagner des mois."},

      {t:'labo', h:"Quel panneau ?",
       p:"Choisissez un mot et voyez le geste.",
       axes:[{id:'p', lbl:'Quel mot ?', opts:[
         ['a','POUSSEZ'],
         ['b','TIREZ'],
         ['c','ENTREZ'],
         ['d','SONNEZ'],
         ['e','ATTENDEZ']]}],
       out:{
         a:{w:['POUSSEZ'], say:"Poussez.", n:'la porte va de l\'autre côté'},
         b:{w:['TIREZ'], say:"Tirez.", n:'la porte vient vers moi'},
         c:{w:['ENTREZ'], say:"Entrez.", n:'on peut entrer sans frapper'},
         d:{w:['SONNEZ'], say:"Sonnez.", n:'il y a un petit bouton à côté'},
         e:{w:['ATTENDEZ'], say:"Attendez.", n:'on reste devant la porte, sans entrer'},
       },
       note:"Cinq mots, cinq gestes. Faites le geste en écoutant : la main s'en souvient mieux que l'œil."},

      {t:'ex', h:"À écouter et à répéter",
       p:"Six panneaux à l'impératif.",
       rows:[
         ["POUSSEZ","la porte va loin de moi"],
         ["TIREZ","la porte vient vers moi"],
         ["ENTREZ","on peut entrer"],
         ["SONNEZ","il y a un bouton"],
         ["ATTENDEZ","on reste dehors un moment"],
         ["ÉCRIVEZ VOTRE NOM","au comptoir de l'accueil"],
       ]},

      {t:'piege', h:"Trois pièges à connaître",
       rows:[
         ["prononcer le Z","« poussèze »",
          "Le Z de -EZ ne se dit pas. On entend « poussé », « tiré », « entré »."],
         ["se sentir visé","« pourquoi on me donne un ordre ? »",
          "Le panneau ne s'adresse à personne : il dit la même chose à tout le monde qui passe. Ce n'est pas impoli."],
         ["tirer une porte qui dit POUSSEZ","et rester bloqué devant",
          "Tout le monde le fait, y compris les gens nés ici. Regardez la poignée : une plaque plate se pousse, une vraie poignée se tire."],
       ]},

      {t:'check', h:"Est-ce que c'est clair maintenant ?",
       p:"Quatre questions rapides.",
       qs:[
         {q:"POUSSEZ veut dire…", opts:["la porte va loin de moi","la porte vient vers moi"], ok:0,
          fb:"On pousse vers l'avant."},
         {q:"Dans « tirez », le Z…", opts:["se prononce","ne se prononce pas"], ok:1,
          fb:"On entend « tiré »."},
         {q:"Ces mots finissent tous par…", opts:["-EZ","-ER"], ok:0,
          fb:"Sur les panneaux, c'est toujours -EZ."},
         {q:"Une plaque de métal plate sur la porte veut dire…", opts:["poussez","tirez"], ok:0,
          fb:"Une vraie poignée, elle, se tire."},
       ]},
    ]
  },

  t2neg: {
    eye:'Mini-leçon', tit:"La barre rouge, et les mots qui disent non",
    blocs:[
      {t:'texte', h:"Le dessin dit non avant le mot",
       p:"Un rond rouge, une barre rouge en travers : c'est <b>interdit</b>. Ce dessin se comprend dans le monde entier, avant même de savoir lire. Le mot écrit à côté ne fait que répéter la même chose — <b>DÉFENSE DE FUMER</b>, <b>NE PAS ENTRER</b>.",
       note:"Vous savez déjà lire ces panneaux-là. Ce qui est nouveau, ce sont les mots écrits à côté."},

      {t:'ana', h:"Sans barre, c'est permis",
       p:"Le dessin montre ce qu'on peut faire.",
       mots:[['On voit','un dessin seul'],['Ça veut dire','{c\'est permis}'],['Exemple','une fontaine d\'eau : on peut boire',true]],
       say:"C'est permis.",
       note:"Un dessin bleu ou vert, sans barre, indique presque toujours quelque chose de permis ou d'utile."},

      {t:'ana', h:"Avec une barre rouge, c'est interdit",
       p:"Le rond et la barre suffisent.",
       mots:[['On voit','un dessin barré de rouge'],['Ça veut dire','{c\'est interdit}'],['Exemple','une cigarette barrée : on ne fume pas',true]],
       say:"C'est interdit.",
       note:"Au Québec, il est interdit de fumer dans tous les bâtiments publics, et à neuf mètres des portes. Le panneau le rappelle, la loi l'oblige."},

      {t:'ana', h:"Les deux mots à repérer",
       p:"Dès qu'on les voit, c'est non.",
       mots:[['Le premier','{DÉFENSE DE} FUMER'],['Le second','{NE PAS} ENTRER'],['Les deux ensemble','ne… pas · défense de',true]],
       say:"Défense de fumer. Ne pas entrer.",
       note:"« Défense de » et « ne pas » sont les deux façons d'écrire une interdiction sur un panneau. Il n'y en a presque pas d'autres."},

      {t:'labo', h:"Permis ou interdit ?",
       p:"Choisissez un panneau.",
       axes:[{id:'p', lbl:'Quel panneau ?', opts:[
         ['a','une cigarette barrée'],
         ['b','ENTREZ'],
         ['c','DÉFENSE DE FUMER'],
         ['d','NE PAS ENTRER'],
         ['e','un chien barré'],
         ['f','SORTIE DE SECOURS']]}],
       out:{
         a:{w:["C'est interdit."], say:"C'est interdit.", n:'la barre rouge dit non'},
         b:{w:["C'est permis."], say:"C'est permis.", n:'on peut entrer sans frapper'},
         c:{w:["C'est interdit."], say:"C'est interdit.", n:'« défense de » : le mot de l\'interdiction'},
         d:{w:["C'est interdit."], say:"C'est interdit.", n:'« ne… pas » autour du verbe'},
         e:{w:["C'est interdit."], say:"C'est interdit.", n:'les chiens ne rentrent pas dans le centre'},
         f:{w:["C'est permis, en cas de danger."], say:"C'est permis, en cas de danger.", n:'la porte verte, seulement s\'il y a un danger'},
       },
       note:"Six panneaux. Cinq disent non, un dit oui — mais seulement quand il le faut."},

      {t:'ex', h:"À écouter et à répéter",
       p:"Six panneaux d'interdiction ou de permission.",
       rows:[
         ["C'est interdit.","la barre rouge"],
         ["C'est permis.","pas de barre"],
         ["Défense de fumer.","partout dans le centre"],
         ["Ne pas entrer.","la porte reste fermée"],
         ["Silence.","on ne parle pas fort"],
         ["Sortie de secours.","la porte verte, en cas de danger"],
       ]},

      {t:'piege', h:"Trois pièges à connaître",
       rows:[
         ["ouvrir une porte de sortie de secours pour aller plus vite","une alarme part, et tout le monde sort",
          "La porte verte ne s'ouvre qu'en cas de danger. Le reste du temps, on prend la sortie ordinaire."],
         ["fumer juste devant la porte","c'est interdit aussi",
          "Au Québec, la loi demande neuf mètres entre une porte de bâtiment public et une cigarette allumée."],
         ["croire qu'un panneau sans mot ne dit rien","le dessin suffit",
          "Un rond rouge barré est une interdiction complète, même sans un seul mot écrit. Le dessin est le message."],
       ]},

      {t:'check', h:"Est-ce que c'est clair maintenant ?",
       p:"Quatre questions rapides.",
       qs:[
         {q:"Une barre rouge veut dire…", opts:["c'est interdit","c'est permis"], ok:0,
          fb:"Le rond rouge barré est une interdiction."},
         {q:"« Défense de fumer » veut dire…", opts:["on peut fumer","on ne fume pas"], ok:1,
          fb:"« Défense de » annonce toujours une interdiction."},
         {q:"La sortie de secours sert…", opts:["tous les jours","en cas de danger"], ok:1,
          fb:"Le reste du temps, on prend la sortie ordinaire."},
         {q:"Un panneau sans mot écrit…", opts:["ne dit rien","dit quand même quelque chose"], ok:1,
          fb:"Le dessin est le message."},
       ]},
    ]
  },
};
