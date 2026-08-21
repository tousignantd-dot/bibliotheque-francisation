const PLUS = {
  prPhon: {
    eye:'Mini-leçon', tit:"Le « ch » de chambre et le « s » de salon",
    blocs:[
      {t:'texte', h:"Deux sons qui se ressemblent, et une annonce entière qui en dépend",
       p:"Presque tous les mots du logement portent l'un des deux : une <b>ch</b>ambre, le <b>ch</b>auffage, <b>ch</b>ercher — ou le <b>s</b>alon, le <b>s</b>ous-sol, la <b>s</b>alle de bain. Si on les confond, « chauffé » devient « sauvé » et « les chaises » devient « les seize ».",
       note:"Ce qui change, c'est la langue et les lèvres : pour <b>ch</b>, la langue recule et les lèvres s'avancent, comme pour souffler ; pour <b>s</b>, la langue reste en avant, derrière les dents du haut, et les lèvres ne bougent pas."},

      {t:'ana', h:"Le son « ch » — les lèvres en avant",
       p:"C'est le son de « chambre », « chauffage », « chercher », « chèque ».",
       mots:[['On écrit','{ch}ambre'],['Aussi','{ch}auffage, {ch}er{ch}er, {ch}èque',true],['Les lèvres','avancées, comme pour souffler sur une cuillère']],
       say:"Une chambre. Le chauffage. Chercher un logement. Un chèque.",
       note:"Presque toujours écrit <b>ch</b>. Dans le mot <b>chose</b>, le ch est au début et le s au milieu : c'est un bon mot d'entraînement."},

      {t:'ana', h:"Le son « s » — la langue en avant",
       p:"C'est le son de « salon », « sous-sol », « salle », « cuisine ».",
       mots:[['On écrit','{s}alon'],['Aussi','{s}ous-{s}ol, {s}alle de bain',true],['Et','la {s}alle, le {s}ous-{s}ol, {s}amedi']],
       say:"Le salon. Le sous-sol. La salle de bain.",
       note:"Il s'écrit <b>s</b> au début d'un mot, <b>ss</b> entre deux voyelles (adre<b>ss</b>e), et parfois <b>c</b> devant e ou i (pi<b>c</b>e, <b>c</b>inq)."},

      {t:'ana', h:"Le piège : un seul s entre deux voyelles se dit « z »",
       p:"Trois mots du module tombent dedans, et ils reviennent tout le temps.",
       mots:[['cuisine','cui{s}ine — on entend z'],['maison','mai{s}on — on entend z',true],['chaise','chai{s}e — on entend z']],
       say:"La cuisine. La maison. Une chaise.",
       note:"Pour garder le son <b>s</b> entre deux voyelles, il faut deux s : <b>adresse</b>, <b>poussière</b>. Un seul s se dit « z »."},

      {t:'labo', h:"Écoute les paires",
       p:"Choisis une paire et écoute la différence.",
       axes:[{id:'p', lbl:'Quelle paire ?', opts:[
         ['a','chaise / seize'],
         ['b','chauffé / sauvé'],
         ['c','chambre / salon'],
         ['d','cuisine / cousine'],
         ['e','dans une phrase']]}],
       out:{
         a:{w:['{ch}aise / {s}eize'], say:"Une chaise. Seize.", n:'ch au début, puis s au début'},
         b:{w:['{ch}auffé / {s}auvé'], say:"Chauffé. Sauvé.", n:'deux mots très différents'},
         c:{w:['{ch}ambre / {s}alon'], say:"Une chambre. Un salon.", n:'les deux pièces du logement'},
         d:{w:['cui{s}ine / cou{s}ine'], say:"La cuisine. Ma cousine.", n:'le s se dit z dans les deux'},
         e:{w:["« La chambre est à côté de la salle de bain. »"], say:"La chambre est à côté de la salle de bain.", n:'ch une fois, s trois fois'},
       },
       note:"Écoute chaque paire deux fois : la première pour comprendre, la seconde en fermant les yeux."},

      {t:'ex', h:"À écouter et à répéter",
       p:"Six phrases de la visite.",
       rows:[
         ["Le logement est chauffé et éclairé.","ch deux fois"],
         ["Le salon est à côté de la cuisine.","s trois fois"],
         ["Je cherche une chambre de plus.","ch deux fois"],
         ["La buanderie est au sous-sol.","s trois fois"],
         ["Les chaises restent dans la cuisine.","ch, puis s"],
         ["La salle de bain est au fond du couloir.","s deux fois"],
       ]},

      {t:'piege', h:"Trois pièges à connaître",
       rows:[
         ["dire « sauffé » pour « chauffé »","« Le logement est sauffé. »",
          "C'est le mot le plus important de l'annonce : il dit qui paie le chauffage. Avance bien les lèvres avant de commencer le mot."],
         ["prononcer le s de « cuisine » comme un vrai s","« la cuiSSine »",
          "Un seul s entre deux voyelles se dit toujours « z » : cui<b>z</b>ine, mai<b>z</b>on, chai<b>z</b>e. Deux s pour garder le son s."],
         ["oublier que « ch » se lit parfois « k »","« un chœur », « une chorale »",
          "C'est rare, et aucun mot du logement n'est concerné. Dans ce module, <b>ch</b> se dit toujours comme dans <b>chambre</b>."],
       ]},

      {t:'check', h:"Est-ce que c'est clair maintenant ?",
       p:"Quatre questions rapides.",
       qs:[
         {q:"« Chauffage » commence par le son…", opts:["ch","s"], ok:0,
          fb:"Les lèvres s'avancent."},
         {q:"« Sous-sol » commence par le son…", opts:["ch","s"], ok:1,
          fb:"La langue reste derrière les dents du haut."},
         {q:"Dans « cuisine », le s se dit…", opts:["s","z"], ok:1,
          fb:"Un seul s entre deux voyelles se dit z."},
         {q:"Pour garder le son s entre deux voyelles, on écrit…", opts:["un s","deux s"], ok:1,
          fb:"Comme dans « adresse »."},
       ]},

      {t:'revoir', h:"À retenir",
       p:"Deux mots repères, et rien d'autre : <b>chambre</b> pour le son « ch », <b>salon</b> pour le son « s ». Devant un mot nouveau, dis-le à côté de l'un des deux. Et souviens-toi qu'un seul <b>s</b> entre deux voyelles se dit « z »."},
    ]
  },

  prGenre: {
    eye:'Mini-leçon', tit:"Un ou une : le genre des pièces",
    blocs:[
      {t:'texte', h:"Le genre ne se devine pas, il s'apprend avec le mot",
       p:"En français, chaque nom est masculin ou féminin, et rien dans l'objet ne le dit : un <b>salon</b> et une <b>cuisine</b> sont deux pièces d'un même logement. Ce n'est pas une question de logique, c'est une question de mémoire — et la mémoire va beaucoup plus vite si on apprend l'article <b>avec</b> le mot.",
       note:"Ne note jamais « chambre » dans ton carnet : note « <b>une</b> chambre ». Les deux mots ensemble, toujours."},

      {t:'ana', h:"Les pièces masculines",
       p:"Elles prennent <b>un</b> et, ensuite, l'adjectif ne change pas.",
       mots:[['On dit','{un} salon'],['Aussi','{un} balcon, {un} couloir',true],['Et','{un} sous-sol, {un} escalier']],
       say:"Un salon. Un balcon. Un couloir. Un sous-sol.",
       note:"Beaucoup de ces mots finissent par <b>-on</b>, <b>-oir</b> ou <b>-ier</b>. Ce n'est pas une règle sûre, mais ça aide à deviner."},

      {t:'ana', h:"Les pièces féminines",
       p:"Elles prennent <b>une</b>, et l'adjectif qui suit prend un <b>e</b>.",
       mots:[['On dit','{une} cuisine'],['Aussi','{une} chambre, {une} salle de bain',true],['Et','{une} fenêtre, {une} porte']],
       say:"Une cuisine. Une chambre. Une salle de bain. Une fenêtre.",
       note:"Beaucoup finissent par <b>-ine</b>, <b>-elle</b>, <b>-ambre</b>, <b>-être</b>. Encore une fois : ça aide, ça ne décide pas."},

      {t:'ana', h:"Au pluriel : des, pour les deux",
       p:"Le genre ne s'entend plus au pluriel — mais il revient dès qu'un adjectif arrive.",
       mots:[['Masculin pluriel','{des} salons, {des} balcons'],['Féminin pluriel','{des} chambres, {des} cuisines',true],['Avec un adjectif','des chambres ferm{ées}, des balcons ferm{és}']],
       say:"Des salons. Des chambres. Des chambres fermées.",
       note:"C'est pour ça que le genre compte, même quand on ne l'entend pas : il ressort à l'écrit, dans le <b>e</b> de l'adjectif."},

      {t:'labo', h:"Choisis une pièce, écoute son article",
       p:"Six pièces du logement, avec leur article.",
       axes:[{id:'p', lbl:'Quelle pièce ?', opts:[
         ['a','le salon'],
         ['b','la cuisine'],
         ['c','la chambre'],
         ['d','la salle de bain'],
         ['e','le balcon'],
         ['f','le sous-sol']]}],
       out:{
         a:{w:['{un} salon'], say:"Un salon. Le salon est grand.", n:'masculin'},
         b:{w:['{une} cuisine'], say:"Une cuisine. La cuisine est chauffée.", n:'féminin'},
         c:{w:['{une} chambre'], say:"Une chambre. La chambre est fermée.", n:'féminin'},
         d:{w:['{une} salle de bain'], say:"Une salle de bain. La salle de bain est au fond.", n:'féminin'},
         e:{w:['{un} balcon'], say:"Un balcon. Le balcon est derrière.", n:'masculin'},
         f:{w:['{un} sous-sol'], say:"Un sous-sol. Le sous-sol est propre.", n:'masculin'},
       },
       note:"Répète chaque pièce avec son article, jamais toute seule."},

      {t:'ex', h:"À écouter et à répéter",
       p:"Six phrases avec un article.",
       rows:[
         ["Le logement a un salon et deux chambres.","un, masculin"],
         ["Il y a une cuisine avec un balcon.","une, puis un"],
         ["Mon garçon veut une chambre à lui.","une, féminin"],
         ["La salle de bain est au fond du couloir.","la, féminin"],
         ["La buanderie est dans un sous-sol propre.","un, masculin"],
         ["L'immeuble a un escalier extérieur.","un, masculin"],
       ]},

      {t:'piege', h:"Trois pièges à connaître",
       rows:[
         ["traduire le genre de sa langue","« un cuisine », parce que c'est masculin ailleurs",
          "Le genre change d'une langue à l'autre : le même objet peut être masculin ici et féminin là. Il n'y a rien à traduire — il faut réapprendre le mot avec son article français."],
         ["apprendre le mot tout seul","noter « chambre » dans son carnet",
          "Trois secondes de gagnées, et un doute pour des années. Note toujours <b>une chambre</b>."],
         ["croire que le pluriel efface le genre","« des chambres fermés »",
          "Au pluriel, on n'entend plus le genre, mais on l'écrit toujours : des chambres ferm<b>ées</b>, avec un e avant le s."],
       ]},

      {t:'check', h:"Est-ce que c'est clair maintenant ?",
       p:"Quatre questions rapides.",
       qs:[
         {q:"On dit…", opts:["un cuisine","une cuisine"], ok:1,
          fb:"Cuisine est féminin."},
         {q:"On dit…", opts:["un balcon","une balcon"], ok:0,
          fb:"Balcon est masculin."},
         {q:"Au pluriel, les deux genres prennent…", opts:["des","les deux articles"], ok:0,
          fb:"« des » sert aux deux."},
         {q:"Dans son carnet, on note…", opts:["chambre","une chambre"], ok:1,
          fb:"L'article fait partie du mot."},
       ]},

      {t:'revoir', h:"À retenir",
       p:"L'article fait partie du mot : <b>un</b> salon, <b>une</b> cuisine, <b>un</b> balcon, <b>une</b> chambre. On ne l'apprend pas après — on l'apprend en même temps."},
    ]
  },

  t1abrev: {
    eye:'Mini-leçon', tit:"Lire une annonce écrite en abrégé",
    blocs:[
      {t:'texte', h:"Une annonce se paie à la ligne, alors elle coupe tout",
       p:"Une petite annonce de logement n'est pas écrite comme une phrase : c'est une <b>liste de renseignements</b>, séparés par des virgules ou des points, sans verbe. Les mots longs sont coupés et remplacés par un point : <b>ét.</b> pour étage, <b>stat.</b> pour stationnement, <b>juill.</b> pour juillet. Une fois qu'on connaît les dix abréviations habituelles, toutes les annonces se lisent.",
       note:"Le point qui suit une abréviation ne finit pas une phrase : il dit que le mot est coupé. « 2e ét. » se lit « deuxième étage »."},

      {t:'ana', h:"Le nombre de pièces : 3 ½, 4 ½, 5 ½",
       p:"Le chiffre compte les pièces, et le demi compte la salle de bain.",
       mots:[['Un 1 ½','une seule pièce, avec un coin cuisine'],['Un 3 ½','une chambre fermée, un salon, une cuisine',true],['Un 4 ½','deux chambres fermées, un salon, une cuisine']],
       say:"Un trois et demie. Un quatre et demie. Un cinq et demie.",
       note:"On dit « un quatre et demie », jamais « un quatre et demi » : l'usage québécois accorde au féminin, parce qu'on sous-entend « pièce »."},

      {t:'ana', h:"Ce qui est compris dans le loyer",
       p:"Deux abréviations, et elles décident du vrai prix du logement.",
       mots:[['ch.','{chauffé} — le chauffage est payé'],['écl.','{éclairé} — l\'électricité est payée',true],['n/c','non chauffé — le chauffage est à ta charge']],
       say:"Chauffé et éclairé. Non chauffé.",
       note:"Un logement non chauffé à 1 000 $ coûte plus cher, l'hiver, qu'un logement chauffé à 1 080 $. C'est le premier calcul à faire."},

      {t:'ana', h:"L'endroit et la date",
       p:"Les deux derniers renseignements de presque toutes les annonces.",
       mots:[['2e ét.','{deuxième étage}'],['s.-sol','{sous-sol}, en bas du rez-de-chaussée',true],['libre 1er juill.','{libre le premier juillet}']],
       say:"Deuxième étage. Sous-sol. Libre le premier juillet.",
       note:"Au Québec, la plupart des baux commencent le <b>1er juillet</b> : c'est la journée du déménagement, et les annonces du printemps parlent presque toutes de cette date."},

      {t:'labo', h:"Choisis une abréviation",
       p:"Six abréviations qu'on trouve dans presque toutes les annonces.",
       axes:[{id:'a', lbl:'Quelle abréviation ?', opts:[
         ['a','4 ½'],
         ['b','2e ét.'],
         ['c','ch. et écl.'],
         ['d','s.-sol'],
         ['e','stat.'],
         ['f','libre 1er juill.']]}],
       out:{
         a:{w:['{quatre et demie}'], say:"Un quatre et demie : deux chambres fermées.", n:'deux chambres fermées'},
         b:{w:['{deuxième étage}'], say:"Deuxième étage.", n:'il faut monter un escalier'},
         c:{w:['{chauffé et éclairé}'], say:"Chauffé et éclairé.", n:'chauffage et électricité compris'},
         d:{w:['{sous-sol}'], say:"Au sous-sol.", n:'en bas du rez-de-chaussée'},
         e:{w:['{stationnement}'], say:"Avec stationnement.", n:'une place pour l\'auto'},
         f:{w:['{libre le premier juillet}'], say:"Libre le premier juillet.", n:'la date de déménagement habituelle'},
       },
       note:"Lis chaque abréviation à voix haute en phrase complète : c'est ainsi qu'on la retient."},

      {t:'ex', h:"À écouter et à répéter",
       p:"Six lignes d'annonce, lues en entier.",
       rows:[
         ["Quatre et demie à louer, rue Chabot, Villeray.","le logement"],
         ["Deuxième étage, deux chambres fermées.","la place"],
         ["Cuisine avec balcon arrière.","les pièces"],
         ["Chauffé, éclairé. Non meublé.","ce qui est compris"],
         ["Buanderie au sous-sol. Pas de stationnement.","l'immeuble"],
         ["Libre le premier juillet. Onze cent cinquante dollars.","la date et le prix"],
       ]},

      {t:'piege', h:"Trois pièges à connaître",
       rows:[
         ["confondre « éclairé » et « ensoleillé »","croire que le logement a beaucoup de fenêtres",
          "<b>Éclairé</b> ne parle pas de la lumière du soleil : il dit que le compte d'<b>électricité</b> est compris dans le loyer. Pour la lumière naturelle, l'annonce dirait « ensoleillé »."],
         ["lire « n/c » comme « non compris »","croire que rien n'est compris",
          "<b>n/c</b> veut dire <b>non chauffé</b> : c'est le chauffage qui n'est pas compris. Le reste peut l'être."],
         ["compter le demi comme une pièce","croire qu'un 4 ½ a quatre chambres",
          "Le demi est la <b>salle de bain</b>, et le chiffre compte toutes les pièces : un 4 ½ a deux chambres, un salon et une cuisine."],
       ]},

      {t:'check', h:"Est-ce que c'est clair maintenant ?",
       p:"Quatre questions rapides.",
       qs:[
         {q:"« ch. et écl. » veut dire…", opts:["chambre et escalier","chauffé et éclairé"], ok:1,
          fb:"Chauffage et électricité compris."},
         {q:"Un 4 ½ a…", opts:["deux chambres fermées","quatre chambres"], ok:0,
          fb:"Le chiffre compte toutes les pièces."},
         {q:"Le demi, dans « 4 ½ », c'est…", opts:["la salle de bain","un placard"], ok:0,
          fb:"Toujours la salle de bain."},
         {q:"« Libre 1er juill. » veut dire…", opts:["libre le premier juillet","libre en juin"], ok:0,
          fb:"C'est la date de déménagement habituelle."},
       ]},

      {t:'revoir', h:"À retenir",
       p:"Une annonce, c'est une liste. Cherche toujours quatre choses dans cet ordre : <b>le nombre de pièces</b>, <b>ce qui est compris</b>, <b>la date</b>, <b>le prix</b>. Le reste est du détail."},
    ]
  },

  t1annonce: {
    eye:'Mini-leçon', tit:"Le vrai prix d'un logement",
    blocs:[
      {t:'texte', h:"Le loyer écrit n'est pas toujours ce qu'on paie",
       p:"Deux logements affichés au même prix peuvent coûter cent dollars de différence par mois. Ce qui décide, ce n'est pas le nombre écrit en gros : c'est la petite ligne qui dit ce qui est <b>compris</b>. Le chauffage, l'électricité, le stationnement, la buanderie : chacun s'ajoute ou non.",
       note:"Avant de comparer deux annonces, il faut donc ramener les deux au même point : le loyer, <b>plus</b> tout ce qui n'est pas compris."},

      {t:'ana', h:"Écrire un prix en français",
       p:"Le loyer d'un logement s'écrit toujours de la même façon.",
       mots:[['On écrit','1 150 $'],['On n\'écrit pas','$1150',true],['Le signe','après le nombre, avec une espace']],
       say:"Mille cent cinquante dollars. Onze cent cinquante dollars.",
       note:"On dit les deux : « mille cent cinquante » ou « onze cent cinquante ». La seconde forme est très courante au Québec pour les prix."},

      {t:'ana', h:"Ce qui s'ajoute au loyer",
       p:"Quatre postes qui reviennent, et l'ordre de grandeur de chacun.",
       mots:[['Le chauffage','environ 90 $ par mois l\'hiver, si l\'annonce dit « non chauffé »'],['L\'électricité','environ 40 $ par mois, si elle n\'est pas comprise',true],['La buanderie','deux dollars la brassée, au sous-sol']],
       say:"Le chauffage. L'électricité. La buanderie.",
       note:"Ces montants sont des ordres de grandeur, pas des tarifs officiels. Ils servent à comparer deux annonces, pas à prévoir un budget exact."},

      {t:'ana', h:"La date, aussi importante que le prix",
       p:"Un logement parfait, libre au mauvais moment, ne sert à rien.",
       mots:[['libre le 1er juillet','{libre le premier juillet} — la date habituelle'],['libre imm.','libre immédiatement : on peut entrer tout de suite',true],['Le bail','presque toujours {douze mois}']],
       say:"Libre le premier juillet. Libre immédiatement.",
       note:"Si ton bail actuel finit le 30 juin et que le nouveau logement est libre le 1er août, tu paies deux loyers ou tu n'as pas de logement pendant un mois."},

      {t:'labo', h:"Deux annonces, un même prix affiché",
       p:"Choisis une annonce et écoute ce qu'elle coûte vraiment.",
       axes:[{id:'a', lbl:'Quelle annonce ?', opts:[
         ['a','A · 1 150 $, chauffé et éclairé'],
         ['b','B · 1 150 $, non chauffé'],
         ['c','La différence']]}],
       out:{
         a:{w:['1 150 $ tout compris'], say:"Mille cent cinquante dollars, chauffage et électricité compris.", n:'rien ne s\'ajoute'},
         b:{w:['1 150 $ + le chauffage + l\'électricité'], say:"Mille cent cinquante dollars, plus le chauffage et l'électricité.", n:'environ cent trente dollars de plus l\'hiver'},
         c:{w:['A est moins cher que B'], say:"L'annonce A est moins chère que l'annonce B.", n:'même prix affiché, pas le même prix payé'},
       },
       note:"C'est le calcul à faire avant d'appeler, pas après avoir visité."},

      {t:'ex', h:"À écouter et à répéter",
       p:"Six phrases pour parler d'un prix.",
       rows:[
         ["Le loyer est de mille cent cinquante dollars.","le prix affiché"],
         ["Le chauffage est compris dans le loyer.","rien à ajouter"],
         ["L'électricité n'est pas comprise.","à payer en plus"],
         ["Il faut compter quatre-vingt-dix dollars de chauffage l'hiver.","l'ordre de grandeur"],
         ["Le logement est libre le premier juillet.","la date"],
         ["Le bail est de douze mois.","la durée"],
       ]},

      {t:'piege', h:"Trois pièges à connaître",
       rows:[
         ["comparer deux loyers sans regarder ce qui est compris","« Les deux sont à 1 150 $, c'est pareil. »",
          "Non : l'un peut coûter cent trente dollars de plus par mois. Le chiffre affiché ne dit rien tout seul."],
         ["écrire le prix avec le signe devant","« $1150 »",
          "En français, le signe de dollar se met <b>après</b> le nombre, avec une espace : 1 150 $."],
         ["oublier la date de son propre bail","choisir un logement libre le 1er août",
          "Si ton bail finit le 30 juin, tu paies un mois pour rien. La date se vérifie avant de visiter."],
       ]},

      {t:'check', h:"Est-ce que c'est clair maintenant ?",
       p:"Quatre questions rapides.",
       qs:[
         {q:"« Chauffé » veut dire…", opts:["le chauffage est compris","il fait chaud"], ok:0,
          fb:"C'est une question d'argent, pas de température."},
         {q:"On écrit un loyer…", opts:["$1 150","1 150 $"], ok:1,
          fb:"Le signe se met après."},
         {q:"Un bail dure d'habitude…", opts:["six mois","douze mois"], ok:1,
          fb:"Du 1er juillet au 30 juin."},
         {q:"Avant de comparer deux annonces, on regarde…", opts:["le prix seulement","le prix et ce qui est compris"], ok:1,
          fb:"Les deux ensemble, toujours."},
       ]},

      {t:'revoir', h:"À retenir",
       p:"Quatre questions devant une annonce : <b>combien de pièces</b>, <b>qu'est-ce qui est compris</b>, <b>à quelle date</b>, <b>combien ça coûte vraiment</b>. La quatrième dépend de la deuxième."},
    ]
  },

  t1adj: {
    eye:'Mini-leçon', tit:"Chauffé, chauffée, chauffés : l'adjectif suit le nom",
    blocs:[
      {t:'texte', h:"L'adjectif prend le genre et le nombre de son nom",
       p:"Un adjectif ne vit pas tout seul : il accompagne un nom, et il change de forme avec lui. Un logement <b>chauffé</b>, une cuisine <b>chauffée</b>, des logements <b>chauffés</b>, des cuisines <b>chauffées</b>. Le mot est le même ; c'est sa fin qui bouge.",
       note:"Deux gestes, toujours dans cet ordre : féminin, on ajoute un <b>e</b> ; pluriel, on ajoute un <b>s</b>. Les deux ensemble donnent <b>-es</b>."},

      {t:'ana', h:"Masculin singulier : la forme de base",
       p:"C'est la forme du dictionnaire, et celle des annonces.",
       mots:[['On écrit','un logement chauff{é}'],['Aussi','un balcon arri{ère}, un sous-sol propre',true],['Dans l\'annonce','« chauffé, éclairé, meublé » parle du logement']],
       say:"Un logement chauffé. Un balcon arrière. Un sous-sol propre.",
       note:"Une annonce écrit tout au masculin singulier parce qu'elle parle du <b>logement</b>, qui est masculin."},

      {t:'ana', h:"Féminin : on ajoute un e",
       p:"Devant un nom féminin, l'adjectif prend un <b>e</b>.",
       mots:[['On écrit','une cuisine chauff{ée}'],['Aussi','une chambre ferm{ée}, une porte arri{ère}',true],['Attention','arrière et propre ont déjà un e : ils ne bougent pas']],
       say:"Une cuisine chauffée. Une chambre fermée. Une porte arrière.",
       note:"Un adjectif qui finit déjà par <b>e</b> ne change pas au féminin : propre, arrière, moderne, libre."},

      {t:'ana', h:"Pluriel : on ajoute un s",
       p:"Et si c'est féminin pluriel, on met les deux : <b>-es</b>.",
       mots:[['Masculin pluriel','des logements chauff{és}'],['Féminin pluriel','des chambres ferm{ées}',true],['On n\'entend rien','les deux se disent pareil']],
       say:"Des logements chauffés. Des chambres fermées.",
       note:"C'est une différence d'écriture, pas de prononciation. Elle compte quand même : elle est corrigée à l'examen."},

      {t:'ana', h:"Deux adjectifs où le féminin s'entend",
       p:"La plupart ne changent pas de son. Ces deux-là, oui — et ils reviennent souvent.",
       mots:[['compris / comprise','le chauffage {compris}, l\'électricité {comprise}'],['inclus / incluse','le stationnement inclus, la place incluse',true],['grand / grande','un grand salon, une grande cuisine']],
       say:"Le chauffage est compris. L'électricité est comprise.",
       note:"Au masculin, la dernière consonne se tait ; au féminin, le <b>e</b> la réveille. C'est pour ça qu'on entend la différence."},

      {t:'labo', h:"Choisis un nom, écoute son adjectif",
       p:"Le même adjectif, quatre formes.",
       axes:[{id:'n', lbl:'Quel nom ?', opts:[
         ['a','un logement'],
         ['b','une cuisine'],
         ['c','des logements'],
         ['d','des chambres']]}],
       out:{
         a:{w:['un logement chauff{é}'], say:"Un logement chauffé.", n:'masculin singulier'},
         b:{w:['une cuisine chauff{ée}'], say:"Une cuisine chauffée.", n:'féminin singulier'},
         c:{w:['des logements chauff{és}'], say:"Des logements chauffés.", n:'masculin pluriel'},
         d:{w:['des chambres chauff{ées}'], say:"Des chambres chauffées.", n:'féminin pluriel'},
       },
       note:"Les quatre se disent exactement pareil. Seule l'écriture change."},

      {t:'ex', h:"À écouter et à répéter",
       p:"Six phrases avec un adjectif.",
       rows:[
         ["Le logement est chauffé et éclairé.","masculin singulier"],
         ["La cuisine est chauffée, elle aussi.","féminin singulier"],
         ["Les deux chambres sont fermées.","féminin pluriel"],
         ["Le chauffage est compris dans le loyer.","on n'entend pas le s"],
         ["L'électricité est comprise dans le loyer.","on entend le z"],
         ["Le balcon arrière donne sur la cour.","déjà un e, rien à ajouter"],
       ]},

      {t:'piege', h:"Trois pièges à connaître",
       rows:[
         ["oublier le e au féminin","« la cuisine est chauffé »",
          "On ne l'entend pas, mais il s'écrit. Cherche toujours le nom auquel l'adjectif se rapporte, puis regarde son genre."],
         ["ajouter un e à un adjectif qui en a déjà un","« une porte arrièree »",
          "Propre, arrière, libre, moderne : ils finissent déjà par e et ne changent pas au féminin."],
         ["dire « comprise » au masculin","« le chauffage est comprise »",
          "Ici, la différence s'entend : <b>compris</b> pour le chauffage, <b>comprise</b> pour l'électricité. Écoute la fin du mot."],
       ]},

      {t:'check', h:"Est-ce que c'est clair maintenant ?",
       p:"Quatre questions rapides.",
       qs:[
         {q:"« La cuisine est… »", opts:["chauffé","chauffée"], ok:1,
          fb:"Cuisine est féminin."},
         {q:"« Les deux chambres sont… »", opts:["fermés","fermées"], ok:1,
          fb:"Féminin pluriel : e puis s."},
         {q:"« L'électricité est… »", opts:["compris","comprise"], ok:1,
          fb:"Et ici, ça s'entend."},
         {q:"« Une porte… »", opts:["arrière","arrièree"], ok:0,
          fb:"Il a déjà un e."},
       ]},

      {t:'revoir', h:"À retenir",
       p:"Cherche le nom, regarde son genre et son nombre, puis complète l'adjectif : rien au masculin, <b>e</b> au féminin, <b>s</b> au pluriel, <b>es</b> aux deux."},
    ]
  },

  t2poli: {
    eye:'Mini-leçon', tit:"Je voudrais, j'aimerais, est-ce que je pourrais",
    blocs:[
      {t:'texte', h:"Au téléphone, la politesse remplace le sourire",
       p:"Quand on parle en personne, le visage adoucit tout. Au téléphone, il ne reste que les mots — et « je veux visiter » sonne dur, même quand on ne le pense pas. Trois formules suffisent à changer tout un appel : <b>je voudrais</b>, <b>j'aimerais</b>, <b>est-ce que je pourrais</b>.",
       note:"Ce sont les formes du conditionnel. On ne les analyse pas ici : on les apprend comme des blocs, tels quels."},

      {t:'ana', h:"Je voudrais — la formule d'entrée",
       p:"C'est « je veux », mais poli. On l'emploie dès la première phrase.",
       mots:[['On dit','{je voudrais} visiter le logement'],['Aussi','{je voudrais} un renseignement',true],['On ne dit pas','« je veux visiter », qui est sec']],
       say:"Je voudrais visiter le logement, s'il vous plaît.",
       note:"Après « je voudrais », le verbe ne change jamais : je voudrais <b>visiter</b>, je voudrais <b>savoir</b>, je voudrais <b>parler</b>."},

      {t:'ana', h:"J'aimerais — un peu plus doux encore",
       p:"Très employé au téléphone, surtout avant une question.",
       mots:[['On dit','{j\'aimerais} poser trois questions'],['Aussi','{j\'aimerais} savoir si c\'est chauffé',true],['Même règle','le verbe qui suit ne change pas']],
       say:"J'aimerais poser trois questions, si vous avez une minute.",
       note:"« J'aimerais savoir » est la façon la plus douce de poser une question difficile : le prix, l'argent, une date."},

      {t:'ana', h:"Est-ce que je pourrais — demander une permission",
       p:"Quand la réponse dépend de l'autre personne, on demande si c'est possible.",
       mots:[['On dit','{est-ce que je pourrais} le visiter'],['Un peu plus direct','{est-ce que je peux} venir demain',true],['On répond','« Bien sûr » ou « Malheureusement, non »']],
       say:"Est-ce que je pourrais le visiter samedi ?",
       note:"<b>Pourrais</b> est plus poli que <b>peux</b>, mais les deux sont corrects. Au téléphone avec une personne qu'on ne connaît pas, prends « pourrais »."},

      {t:'labo', h:"La même demande, quatre façons",
       p:"Choisis une formule et écoute-la dans une phrase.",
       axes:[{id:'f', lbl:'Quelle formule ?', opts:[
         ['a','je veux'],
         ['b','je voudrais'],
         ['c','j\'aimerais'],
         ['d','est-ce que je pourrais']]}],
       out:{
         a:{w:['je veux visiter le logement'], say:"Je veux visiter le logement.", n:'trop sec au téléphone'},
         b:{w:['{je voudrais} visiter le logement'], say:"Je voudrais visiter le logement, s'il vous plaît.", n:'poli, et suffisant'},
         c:{w:['{j\'aimerais} visiter le logement'], say:"J'aimerais visiter le logement.", n:'doux, très employé'},
         d:{w:['{est-ce que je pourrais} visiter le logement'], say:"Est-ce que je pourrais visiter le logement ?", n:'le plus poli des quatre'},
       },
       note:"Les trois derniers sont bons. Le premier se garde pour un ami."},

      {t:'ex', h:"À écouter et à répéter",
       p:"Six phrases d'un appel poli.",
       rows:[
         ["Bonjour, madame. Je vous appelle pour l'annonce.","l'entrée en matière"],
         ["J'aimerais poser trois questions, si vous avez une minute.","demander la parole"],
         ["Je voudrais savoir si le chauffage est compris.","une question douce"],
         ["Est-ce que je pourrais le visiter cette semaine ?","demander une permission"],
         ["Pouvez-vous répéter l'adresse, s'il vous plaît ?","faire répéter"],
         ["Merci beaucoup, madame. Bonne journée.","la sortie"],
       ]},

      {t:'piege', h:"Trois pièges à connaître",
       rows:[
         ["dire « je veux » au téléphone","« Je veux voir le logement. »",
          "Ce n'est pas une faute de grammaire, c'est une faute de ton. La personne peut décider de ne pas rappeler."],
         ["oublier de dire pourquoi on appelle","commencer par « Bonjour, ça va ? »",
          "La deuxième phrase doit dire pourquoi tu appelles : « Je vous appelle pour l'annonce du quatre et demie. » Sans ça, la personne ne sait pas à qui elle parle."],
         ["changer le verbe qui suit","« je voudrais je visite »",
          "Après <b>je voudrais</b>, <b>j'aimerais</b>, <b>je pourrais</b>, le verbe reste à l'infinitif : visiter, savoir, venir, parler."],
       ]},

      {t:'check', h:"Est-ce que c'est clair maintenant ?",
       p:"Quatre questions rapides.",
       qs:[
         {q:"Au téléphone, on dit plutôt…", opts:["je veux visiter","je voudrais visiter"], ok:1,
          fb:"Trois lettres de plus, tout un ton."},
         {q:"Après « je voudrais », le verbe…", opts:["ne change pas","se conjugue"], ok:0,
          fb:"Il reste à l'infinitif."},
         {q:"Le plus poli des quatre, c'est…", opts:["est-ce que je pourrais","est-ce que je peux"], ok:0,
          fb:"« Pourrais », pour une personne qu'on ne connaît pas."},
         {q:"La deuxième phrase de l'appel dit…", opts:["comment on va","pourquoi on appelle"], ok:1,
          fb:"« Je vous appelle pour l'annonce. »"},
       ]},

      {t:'revoir', h:"À retenir",
       p:"Trois blocs, à apprendre tels quels : <b>je voudrais</b> + verbe, <b>j'aimerais</b> + verbe, <b>est-ce que je pourrais</b> + verbe. Et <b>s'il vous plaît</b> à la fin."},
    ]
  },

  t2trois: {
    eye:'Mini-leçon', tit:"Trois questions, préparées avant d'appeler",
    blocs:[
      {t:'texte', h:"On n'improvise pas un appel dans une langue nouvelle",
       p:"Au téléphone, il n'y a ni gestes, ni visage, ni papier à montrer. Une personne qui n'a rien préparé oublie la moitié de ce qu'elle voulait demander et rappelle deux heures plus tard. Trois questions écrites sur un bout de papier, avant de composer le numéro, suffisent : <b>l'argent</b>, <b>la place</b>, <b>la date</b>.",
       note:"Écris-les vraiment. Une feuille devant soi change complètement un appel — c'est ce que font aussi les personnes qui parlent français depuis toujours."},

      {t:'ana', h:"Question 1 · L'argent",
       p:"C'est celle qui change le plus le prix réel du logement.",
       mots:[['On demande','{est-ce que le chauffage est compris}'],['Ou','est-ce que l\'électricité est comprise',true],['On note','le loyer, puis ce qui s\'ajoute']],
       say:"Est-ce que le chauffage est compris dans le loyer ?",
       note:"Si la réponse est non, demande tout de suite : « Ça coûte à peu près combien par mois l'hiver ? »"},

      {t:'ana', h:"Question 2 · La place",
       p:"L'annonce dit « 4 ½ », mais il vaut mieux entendre le détail.",
       mots:[['On demande','{combien il y a de chambres}'],['Ou','est-ce que les chambres sont fermées',true],['On note','le nombre, et s\'il y a une porte']],
       say:"Combien il y a de chambres fermées ?",
       note:"Une « chambre » sans porte n'est pas une chambre pour tout le monde. La question vaut la peine d'être posée."},

      {t:'ana', h:"Question 3 · La date",
       p:"Un logement libre au mauvais moment ne sert à rien.",
       mots:[['On demande','{à quelle date c\'est libre}'],['Puis','{est-ce que je pourrais visiter}',true],['On note','le jour et l\'heure du rendez-vous']],
       say:"À quelle date est-ce que c'est libre ?",
       note:"La troisième question amène naturellement la demande de visite : c'est le but de l'appel."},

      {t:'ana', h:"Et si on n'a pas compris",
       p:"Au téléphone, c'est fréquent, et ce n'est pas grave.",
       mots:[['On dit','{pouvez-vous répéter}'],['Ou','plus lentement, s\'il vous plaît',true],['Ou','pouvez-vous épeler la rue ?']],
       say:"Pardon, pouvez-vous répéter, s'il vous plaît ?",
       note:"Faire répéter deux fois est normal. Raccrocher sans avoir compris l'adresse ne l'est pas."},

      {t:'labo', h:"Choisis une question, écoute-la",
       p:"Les quatre phrases de l'appel, dans l'ordre.",
       axes:[{id:'q', lbl:'Quelle question ?', opts:[
         ['a','1 · l\'argent'],
         ['b','2 · la place'],
         ['c','3 · la date'],
         ['d','4 · la visite'],
         ['e','faire répéter']]}],
       out:{
         a:{w:['{est-ce que le chauffage est compris}'], say:"Est-ce que le chauffage est compris dans le loyer ?", n:'la question du vrai prix'},
         b:{w:['{combien il y a de chambres}'], say:"Combien il y a de chambres fermées ?", n:'la question de la place'},
         c:{w:["{à quelle date c'est libre}"], say:"À quelle date est-ce que le logement est libre ?", n:'la question du calendrier'},
         d:{w:['{est-ce que je pourrais visiter}'], say:"Est-ce que je pourrais le visiter cette semaine ?", n:'le but de l\'appel'},
         e:{w:['{pouvez-vous répéter}'], say:"Pardon, pouvez-vous répéter, s'il vous plaît ?", n:'à employer sans gêne'},
       },
       note:"Répète les quatre à la suite : c'est exactement l'appel que tu vas faire."},

      {t:'ex', h:"À écouter et à répéter",
       p:"Six phrases de l'appel.",
       rows:[
         ["Bonjour, je vous appelle pour l'annonce du quatre et demie.","dire pourquoi on appelle"],
         ["Est-ce que le chauffage est compris dans le loyer ?","question 1"],
         ["Combien il y a de chambres fermées ?","question 2"],
         ["À quelle date est-ce que le logement est libre ?","question 3"],
         ["Est-ce que je pourrais le visiter cette semaine ?","la demande"],
         ["Samedi, dix heures, rue Chabot. C'est bien ça ?","vérifier avant de raccrocher"],
       ]},

      {t:'piege', h:"Trois pièges à connaître",
       rows:[
         ["poser les trois questions d'un coup","« Est-ce que c'est chauffé, il y a combien de chambres et c'est libre quand ? »",
          "La personne ne répondra qu'à la dernière. Une question, une réponse, puis la suivante."],
         ["raccrocher sans répéter le rendez-vous","dire seulement « d'accord, merci »",
          "Répète toujours le jour, l'heure et l'adresse à voix haute. C'est le seul moment où une erreur peut encore se corriger."],
         ["ne rien noter","tout garder dans sa tête",
          "Trois logements en deux jours, et tout se mélange. Écris le prix, la date et l'adresse pendant que la personne parle."],
       ]},

      {t:'check', h:"Est-ce que c'est clair maintenant ?",
       p:"Quatre questions rapides.",
       qs:[
         {q:"La première question à poser porte sur…", opts:["ce qui est compris dans le loyer","la couleur des murs"], ok:0,
          fb:"C'est elle qui change le vrai prix."},
         {q:"On pose les questions…", opts:["toutes ensemble","une à la fois"], ok:1,
          fb:"Une question, une réponse."},
         {q:"Avant de raccrocher, on…", opts:["répète le rendez-vous","remercie seulement"], ok:0,
          fb:"Le jour, l'heure et l'adresse."},
         {q:"Si on n'a pas compris, on dit…", opts:["rien, pour ne pas déranger","pouvez-vous répéter, s'il vous plaît"], ok:1,
          fb:"C'est normal et attendu."},
       ]},

      {t:'revoir', h:"À retenir",
       p:"Trois questions sur un papier avant d'appeler : <b>l'argent</b>, <b>la place</b>, <b>la date</b>. Puis la demande de visite, puis la répétition du rendez-vous."},
    ]
  },

  t2futur: {
    eye:'Mini-leçon', tit:"Je vais venir : parler de bientôt",
    blocs:[
      {t:'texte', h:"Deux verbes, et le second ne bouge jamais",
       p:"Pour dire ce qui va arriver bientôt, le français prend le verbe <b>aller</b> au présent, puis pose derrière lui le verbe qui compte, sans le changer : <b>je vais venir</b>, <b>nous allons visiter</b>, <b>il va être libre</b>. C'est ce qu'on appelle le futur proche, et c'est de loin ce qu'on entend le plus.",
       note:"Il n'y a rien à conjuguer deux fois : seul <b>aller</b> change. Le second verbe reste comme dans le dictionnaire."},

      {t:'ana', h:"Les six formes d'aller",
       p:"Ce sont les seules à retenir. Le reste suit tout seul.",
       mots:[['je / tu','je {vais}, tu {vas}'],['il / elle','il {va}, elle {va}',true],['nous / vous / ils','nous {allons}, vous {allez}, ils {vont}']],
       say:"Je vais. Tu vas. Il va. Nous allons. Vous allez. Ils vont.",
       note:"Trois formes se ressemblent à l'oreille — <b>vais</b>, <b>vas</b>, <b>va</b> — mais ce qui les distingue, c'est le mot d'avant : je, tu, il."},

      {t:'ana', h:"Le futur proche au téléphone",
       p:"C'est le temps de la prise de rendez-vous.",
       mots:[['Pour un rendez-vous','{je vais venir} samedi matin'],['Pour un rappel','{je vais vous rappeler} demain',true],['Pour une visite','{nous allons visiter} à dix heures']],
       say:"Je vais venir samedi matin. Je vais vous rappeler demain.",
       note:"On l'emploie même pour des choses très proches : « Je vais raccrocher », « Je vais noter l'adresse »."},

      {t:'ana', h:"Aller tout seul, et aller + verbe",
       p:"Le même verbe, deux sens : c'est ce qui suit qui décide.",
       mots:[['Un déplacement','je vais {à Villeray} — je me déplace'],['Un futur proche','je vais {visiter} — ça arrive bientôt',true],['Les deux','je vais aller à Villeray']],
       say:"Je vais à Villeray. Je vais visiter le logement.",
       note:"Si le mot qui suit est un lieu, c'est un déplacement. Si c'est un verbe, c'est le futur proche."},

      {t:'labo', h:"Choisis une personne",
       p:"La même phrase, six sujets.",
       axes:[{id:'s', lbl:'Qui parle ?', opts:[
         ['a','je'],
         ['b','tu'],
         ['c','il / elle'],
         ['d','nous'],
         ['e','vous'],
         ['f','ils / elles']]}],
       out:{
         a:{w:['je {vais} visiter'], say:"Je vais visiter le logement samedi.", n:'vais'},
         b:{w:['tu {vas} visiter'], say:"Tu vas visiter le logement samedi.", n:'vas'},
         c:{w:['elle {va} visiter'], say:"Elle va visiter le logement samedi.", n:'va'},
         d:{w:['nous {allons} visiter'], say:"Nous allons visiter le logement samedi.", n:'allons'},
         e:{w:['vous {allez} visiter'], say:"Vous allez visiter le logement samedi.", n:'allez'},
         f:{w:['ils {vont} visiter'], say:"Ils vont visiter le logement samedi.", n:'vont'},
       },
       note:"Le second verbe, <b>visiter</b>, ne bouge dans aucune des six."},

      {t:'ex', h:"À écouter et à répéter",
       p:"Six phrases au futur proche.",
       rows:[
         ["Je vais venir samedi matin avec mon mari.","je vais"],
         ["Nous allons visiter le logement à dix heures.","nous allons"],
         ["Le logement va être libre le premier juillet.","il va"],
         ["Est-ce que tu vas appeler la propriétaire ?","tu vas"],
         ["Mes voisins vont déménager la semaine prochaine.","ils vont"],
         ["Je vais vous rappeler demain matin.","je vais"],
       ]},

      {t:'piege', h:"Trois pièges à connaître",
       rows:[
         ["conjuguer le deuxième verbe","« je vais je viens »",
          "Un seul verbe se conjugue : <b>aller</b>. Le second reste comme dans le dictionnaire : venir, visiter, appeler."],
         ["confondre nous allons et ils vont","« nous vont visiter »",
          "<b>Nous allons</b>, <b>ils vont</b>. Les deux formes ne se ressemblent pas : c'est celle du « nous » qui surprend, parce qu'elle repart du verbe aller en entier."],
         ["employer le futur proche pour une habitude","« je vais aller à l'école tous les jours »",
          "Le futur proche dit ce qui arrive <b>bientôt</b>, une fois. Pour une habitude, on emploie le présent : « je vais à l'école tous les jours »."],
       ]},

      {t:'check', h:"Est-ce que c'est clair maintenant ?",
       p:"Quatre questions rapides.",
       qs:[
         {q:"« Nous ___ visiter »", opts:["allons","vont"], ok:0,
          fb:"Nous allons."},
         {q:"Après « je vais », le verbe…", opts:["se conjugue","ne change pas"], ok:1,
          fb:"Il reste à l'infinitif."},
         {q:"« Je vais à Villeray », c'est…", opts:["un déplacement","un futur proche"], ok:0,
          fb:"Ce qui suit est un lieu."},
         {q:"« Le logement ___ être libre »", opts:["va","vont"], ok:0,
          fb:"Un seul logement : il va."},
       ]},

      {t:'revoir', h:"À retenir",
       p:"<b>aller</b> au présent + le verbe qui ne change pas. Six formes à savoir : vais, vas, va, allons, allez, vont. Et c'est tout le futur proche."},
    ]
  },

  t3prep: {
    eye:'Mini-leçon', tit:"Dire où : au fond, à côté, en bas",
    blocs:[
      {t:'texte', h:"Pendant une visite, tout se dit avec deux ou trois petits mots",
       p:"La propriétaire ne fait pas de longues phrases : elle dit « <b>au fond du</b> couloir », « <b>à côté de</b> la salle de bain », « <b>en bas de</b> l'escalier ». Ces petits mots portent toute l'information. Les comprendre, c'est savoir où on va ; les employer, c'est pouvoir décrire le logement à quelqu'un d'autre.",
       note:"Beaucoup se terminent par <b>de</b>. Devant « le », ce <b>de</b> devient <b>du</b> : au fond <b>du</b> couloir, à côté <b>du</b> salon. Devant une voyelle, il devient <b>de l'</b> : en bas <b>de l'</b>escalier."},

      {t:'ana', h:"Au fond de — tout au bout",
       p:"C'est la dernière porte, celle qu'on voit devant soi.",
       mots:[['On dit','{au fond du couloir}'],['Aussi','au fond de la pièce, au fond de la cour',true],['Devant le','de + le = du']],
       say:"Les deux chambres sont au fond du couloir.",
       note:"Ne pas confondre avec <b>au bout de</b>, qui veut dire la même chose et s'emploie autant. Les deux sont bons."},

      {t:'ana', h:"À côté de — juste à côté",
       p:"Les deux choses se touchent, ou presque.",
       mots:[['On dit','{à côté de la salle de bain}'],['Devant le','à côté du salon',true],['Devant une voyelle','à côté de l\'escalier']],
       say:"La petite chambre est à côté de la salle de bain.",
       note:"<b>À côté de</b> dit qu'on est tout près ; <b>près de</b> dit qu'on n'est pas loin. « L'école est près d'ici » ne veut pas dire qu'elle est collée à l'immeuble."},

      {t:'ana', h:"Au — pour un étage, un niveau",
       p:"Devant un étage ou un niveau, c'est un simple <b>au</b>.",
       mots:[['On dit','{au sous-sol}'],['Aussi','{au deuxième étage}, au rez-de-chaussée',true],['On ne dit pas','« dans le sous-sol » pour un immeuble']],
       say:"La buanderie est au sous-sol. Le logement est au deuxième étage.",
       note:"Au Québec, le <b>rez-de-chaussée</b> est au niveau de la rue, et le premier étage est au-dessus. Un « 2e étage » est donc à deux escaliers de la rue."},

      {t:'ana', h:"Derrière, devant, en bas de",
       p:"Trois derniers, qui reviennent dans toutes les visites.",
       mots:[['Derrière','{derrière la cuisine} — le balcon arrière'],['Devant','devant l\'immeuble — la rue',true],['En bas de','{en bas de l\'escalier} — on descend']],
       say:"Le balcon est derrière la cuisine. Les laveuses sont en bas de l'escalier.",
       note:"« En haut de » est son contraire : les chambres sont en haut de l'escalier, dans une maison à deux étages."},

      {t:'labo', h:"Choisis un endroit du logement",
       p:"Six phrases entendues pendant la visite.",
       axes:[{id:'e', lbl:'Quel endroit ?', opts:[
         ['a','les chambres'],
         ['b','la salle de bain'],
         ['c','la buanderie'],
         ['d','le balcon'],
         ['e','le logement'],
         ['f','les laveuses']]}],
       out:{
         a:{w:['{au fond du couloir}'], say:"Les deux chambres sont au fond du couloir.", n:'tout au bout'},
         b:{w:['{à côté de la salle de bain}'], say:"La petite chambre est à côté de la salle de bain.", n:'les deux portes se touchent'},
         c:{w:['{au sous-sol}'], say:"La buanderie est au sous-sol.", n:'en bas du rez-de-chaussée'},
         d:{w:['{derrière la cuisine}'], say:"Le balcon est derrière la cuisine.", n:'sur la cour arrière'},
         e:{w:['{au deuxième étage}'], say:"Le logement est au deuxième étage.", n:'deux escaliers depuis la rue'},
         f:{w:["{en bas de l'escalier}"], say:"Les laveuses sont en bas de l'escalier.", n:'il faut descendre'},
       },
       note:"Répète chaque phrase en montrant du doigt un endroit de la classe : le geste installe le sens."},

      {t:'ex', h:"À écouter et à répéter",
       p:"Six phrases de la visite.",
       rows:[
         ["Les deux chambres sont au fond du couloir.","au fond du"],
         ["La petite chambre est à côté de la salle de bain.","à côté de"],
         ["La buanderie est au sous-sol.","au"],
         ["Le balcon est derrière la cuisine.","derrière"],
         ["Le logement est au deuxième étage.","au"],
         ["Les laveuses sont en bas de l'escalier.","en bas de"],
       ]},

      {t:'piege', h:"Trois pièges à connaître",
       rows:[
         ["oublier de coller de et le","« au fond de le couloir »",
          "<b>de + le</b> donne toujours <b>du</b> : au fond <b>du</b> couloir, à côté <b>du</b> salon, en bas <b>du</b> balcon."],
         ["dire « dans le sous-sol » d'un immeuble","« la buanderie est dans le sous-sol »",
          "Pour un niveau d'immeuble, on dit <b>au</b> sous-sol, <b>au</b> deuxième étage, <b>au</b> rez-de-chaussée. « Dans » servirait à parler de l'intérieur d'une pièce."],
         ["confondre le rez-de-chaussée et le premier étage","croire que le 1er étage est au niveau de la rue",
          "Au niveau de la rue, c'est le <b>rez-de-chaussée</b>. Le premier étage est déjà un escalier plus haut."],
       ]},

      {t:'check', h:"Est-ce que c'est clair maintenant ?",
       p:"Quatre questions rapides.",
       qs:[
         {q:"On dit…", opts:["au fond de le couloir","au fond du couloir"], ok:1,
          fb:"de + le = du."},
         {q:"Pour un niveau d'immeuble, on dit…", opts:["au sous-sol","dans le sous-sol"], ok:0,
          fb:"Au, pour un niveau."},
         {q:"Le niveau de la rue s'appelle…", opts:["le premier étage","le rez-de-chaussée"], ok:1,
          fb:"Le premier étage est au-dessus."},
         {q:"« À côté de » veut dire…", opts:["tout près","assez loin"], ok:0,
          fb:"Les deux choses se touchent."},
       ]},

      {t:'revoir', h:"À retenir",
       p:"Cinq blocs, et une visite entière se décrit : <b>au fond du</b>, <b>à côté de</b>, <b>au</b> (un étage), <b>derrière</b>, <b>en bas de</b>. Et n'oublie pas que <b>de + le</b> fait <b>du</b>."},
    ]
  },

  t3neg: {
    eye:'Mini-leçon', tit:"Il n'y a pas de : répondre non",
    blocs:[
      {t:'texte', h:"Après « pas », l'article disparaît",
       p:"C'est l'une des rares règles vraiment simples du français, et l'une des plus utiles pendant une visite. Quand on dit qu'une chose n'existe pas, l'article <b>un</b>, <b>une</b>, <b>des</b>, <b>du</b> se change en un seul mot : <b>de</b>. Il y a <b>un</b> stationnement → il n'y a pas <b>de</b> stationnement.",
       note:"Une seule forme, quel que soit le genre et le nombre : pas <b>de</b> stationnement, pas <b>de</b> buanderie, pas <b>de</b> meubles."},

      {t:'ana', h:"La forme de base : pas de",
       p:"C'est celle qu'on entend dix fois dans une visite.",
       mots:[['On dit','{il n\'y a pas de stationnement}'],['Aussi','il n\'y a pas de buanderie',true],['On ne dit pas','« pas un stationnement »']],
       say:"Il n'y a pas de stationnement dans la cour.",
       note:"Attention à ne pas garder l'article de la phrase positive : « il y a <b>un</b> balcon » devient « il n'y a pas <b>de</b> balcon »."},

      {t:'ana', h:"Devant une voyelle : pas d'",
       p:"Le <b>e</b> tombe et on colle avec une apostrophe.",
       mots:[['On dit','{il n\'y a pas d\'ascenseur}'],['Aussi','pas d\'électroménagers, pas d\'eau chaude',true],['Et','{je n\'ai pas d\'auto}']],
       say:"Il n'y a pas d'ascenseur dans l'immeuble.",
       note:"Même règle qu'avec <b>le</b> et <b>la</b>, qui deviennent <b>l'</b> devant une voyelle. Le français n'aime pas deux voyelles qui se suivent."},

      {t:'ana', h:"Au pluriel, c'est encore de",
       p:"La règle ne change pas : ni <b>des</b>, ni <b>les</b>.",
       mots:[['On dit','{il n\'y a pas de meubles}'],['Aussi','il n\'y a pas de rideaux',true],['On ne dit pas','« pas des meubles »']],
       say:"Le logement est vide : il n'y a pas de meubles.",
       note:"C'est le piège le plus fréquent, parce que beaucoup de langues gardent le pluriel. Ici, un seul mot suffit."},

      {t:'ana', h:"Devant un adjectif : ne… pas, sans de",
       p:"Le <b>de</b> ne sert que devant un nom.",
       mots:[['On dit','{ce n\'est pas compris}'],['Aussi','le logement n\'est pas meublé',true],['Jamais','« ce n\'est pas de compris »']],
       say:"Internet, ce n'est pas compris dans le loyer.",
       note:"Pose-toi une seule question : est-ce qu'il y a un <b>nom</b> après ? Si oui, <b>de</b>. Si c'est un adjectif, rien."},

      {t:'labo', h:"Choisis une réponse de la visite",
       p:"Cinq façons de dire non, entendues pendant la visite.",
       axes:[{id:'r', lbl:'Quelle réponse ?', opts:[
         ['a','le stationnement'],
         ['b','l\'ascenseur'],
         ['c','les meubles'],
         ['d','internet'],
         ['e','l\'auto']]}],
       out:{
         a:{w:["{il n'y a pas de stationnement}"], say:"Il n'y a pas de stationnement dans la cour.", n:'nom masculin : de'},
         b:{w:["{il n'y a pas d'ascenseur}"], say:"Il n'y a pas d'ascenseur dans l'immeuble.", n:'voyelle : d\''},
         c:{w:["{il n'y a pas de meubles}"], say:"Il n'y a pas de meubles : le logement est vide.", n:'pluriel : encore de'},
         d:{w:["{ce n'est pas compris}"], say:"Internet, ce n'est pas compris dans le loyer.", n:'adjectif : rien'},
         e:{w:["{je n'ai pas d'auto}"], say:"Ça ne fait rien, je n'ai pas d'auto.", n:'voyelle : d\''},
       },
       note:"Les cinq se disent pendant une visite ordinaire. Apprends-les comme des blocs."},

      {t:'ex', h:"À écouter et à répéter",
       p:"Six réponses négatives.",
       rows:[
         ["Il n'y a pas de stationnement dans la cour.","pas de"],
         ["Il n'y a pas d'ascenseur : c'est un vieil immeuble.","pas d'"],
         ["Le logement est vide : il n'y a pas de meubles.","pas de, au pluriel"],
         ["Internet n'est pas compris dans le loyer.","ne… pas, sans de"],
         ["Nous n'avons pas d'auto, alors ça ne fait rien.","pas d'"],
         ["Il n'y a pas de buanderie dans cet immeuble-là.","pas de"],
       ]},

      {t:'piege', h:"Trois pièges à connaître",
       rows:[
         ["garder l'article de la phrase positive","« il n'y a pas un stationnement »",
          "Un, une, des, du : tous deviennent <b>de</b> après « pas ». C'est la règle entière."],
         ["garder le pluriel","« il n'y a pas des meubles »",
          "Au pluriel aussi, c'est <b>de</b> : il n'y a pas <b>de</b> meubles."],
         ["mettre de devant un adjectif","« ce n'est pas de compris »",
          "Le <b>de</b> ne sert que devant un nom. Devant un adjectif, on met seulement <b>ne… pas</b>."],
       ]},

      {t:'check', h:"Est-ce que c'est clair maintenant ?",
       p:"Quatre questions rapides.",
       qs:[
         {q:"« Il n'y a pas ___ stationnement »", opts:["de","un"], ok:0,
          fb:"Toujours de, après pas."},
         {q:"« Il n'y a pas ___ ascenseur »", opts:["de","d'"], ok:1,
          fb:"Devant une voyelle, le e tombe."},
         {q:"« Il n'y a pas ___ meubles »", opts:["des","de"], ok:1,
          fb:"Au pluriel aussi."},
         {q:"« Internet n'est pas ___ compris »", opts:["de","rien"], ok:1,
          fb:"Compris est un adjectif."},
       ]},

      {t:'revoir', h:"À retenir",
       p:"Après <b>pas</b>, l'article devient <b>de</b> — ou <b>d'</b> devant une voyelle, au singulier comme au pluriel. Et devant un adjectif, on ne met rien du tout."},
    ]
  },

  t3rec: {
    eye:'Mini-leçon', tit:"Avant de dire oui : le bail et l'argent",
    blocs:[
      {t:'texte', h:"Trois choses à savoir, et elles protègent le locataire",
       p:"Louer un logement au Québec suit des règles écrites, les mêmes pour tout le monde. Elles ne sont pas là pour compliquer la vie : elles existent pour éviter qu'on demande à quelqu'un de payer ce qu'il ne doit pas. Trois d'entre elles suffisent à un premier logement — <b>le bail</b>, <b>sa durée</b>, et <b>l'argent qu'on donne</b>.",
       note:"Ce ne sont pas des habitudes locales : ce sont des règles de loi, et elles s'appliquent partout au Québec, dans tous les logements."},

      {t:'ana', h:"Le bail, un formulaire unique",
       p:"C'est le papier qu'on signe, et il est le même dans toute la province.",
       mots:[['On dit','{le bail}'],['Qui le fait','le Tribunal administratif du logement',true],['Ce qu\'il dit','qui, où, combien, à partir de quand']],
       say:"Le bail commence le premier juillet.",
       note:"Le Tribunal administratif du logement s'appelait la <b>Régie du logement</b> jusqu'en 2020. Les deux noms se disent encore."},

      {t:'ana', h:"Douze mois, et il se renouvelle tout seul",
       p:"La durée habituelle, et ce qui arrive à la fin.",
       mots:[['La durée','{douze mois}, du 1er juillet au 30 juin'],['À la fin','il se renouvelle tout seul',true],['Pour partir','il faut écrire au propriétaire, à l\'avance']],
       say:"Le bail dure douze mois.",
       note:"Le renouvellement automatique est une <b>protection</b> : personne ne peut te mettre dehors parce que l'année est finie."},

      {t:'ana', h:"L'argent : jamais de dépôt",
       p:"C'est la règle la moins connue, et celle qui coûte le plus cher quand on l'ignore.",
       mots:[['On ne donne pas','{un dépôt} de garantie — c\'est interdit'],['On ne donne pas','le dernier mois d\'avance',true],['On donne','{le premier loyer}, le premier jour du bail']],
       say:"Au Québec, un dépôt de garantie est interdit.",
       note:"Un propriétaire peut demander le premier mois de loyer, et rien d'autre. S'il demande davantage, tu as le droit de refuser."},

      {t:'ana', h:"Ce qu'on n'a pas le droit de te refuser",
       p:"La Charte des droits et libertés de la personne protège aussi les locataires.",
       mots:[['Les enfants','on ne peut pas te refuser parce que tu as {des enfants}'],['L\'origine','ni à cause de ton pays, de ta langue ou de ta religion',true],['Si ça arrive','tu peux t\'adresser au Tribunal administratif du logement']],
       say:"On ne peut pas refuser un logement à des enfants.",
       note:"On peut te demander une preuve de revenus, ce qui est permis. On ne peut pas te refuser à cause de ta famille ou de ton origine."},

      {t:'labo', h:"Choisis une situation",
       p:"Quatre situations qui arrivent vraiment.",
       axes:[{id:'s', lbl:'Quelle situation ?', opts:[
         ['a','on te demande 500 $ de dépôt'],
         ['b','on te demande de signer aujourd\'hui'],
         ['c','on te dit non à cause des enfants'],
         ['d','on te demande le premier mois']]}],
       out:{
         a:{w:['{un dépôt}'], say:"Un dépôt de garantie est interdit au Québec.", n:'tu peux refuser'},
         b:{w:['{je vais y penser}'], say:"Je vais y penser et je vous rappelle demain.", n:'personne ne signe le jour même'},
         c:{w:['{des enfants}'], say:"On ne peut pas refuser un logement à des enfants.", n:'la Charte l\'interdit'},
         d:{w:['{le premier loyer}'], say:"On paie le premier loyer le premier jour du bail.", n:'ça, c\'est permis'},
       },
       note:"Trois de ces quatre demandes sont interdites. La quatrième est normale."},

      {t:'ex', h:"À écouter et à répéter",
       p:"Six phrases à savoir dire.",
       rows:[
         ["Le bail commence le premier juillet.","la date"],
         ["Le bail dure douze mois.","la durée"],
         ["Est-ce que je dois donner de l'argent aujourd'hui ?","la question à poser"],
         ["Au Québec, un dépôt de garantie est interdit.","la règle"],
         ["Je vais y penser et je vous rappelle demain.","ne pas signer tout de suite"],
         ["Est-ce que je peux lire le bail avant de signer ?","une question toujours permise"],
       ]},

      {t:'piege', h:"Trois pièges à connaître",
       rows:[
         ["donner un dépôt pour être sûr d'avoir le logement","payer 500 $ d'avance à la visite",
          "C'est interdit, et cet argent est très difficile à récupérer. Un propriétaire honnête ne le demandera pas."],
         ["signer le jour de la visite","« Si vous ne signez pas maintenant, je le donne à quelqu'un d'autre. »",
          "Tu peux toujours dire : « Je vais y penser et je vous rappelle demain. » Un logement qui exige une signature immédiate mérite qu'on se méfie."],
         ["croire qu'un bail verbal ne compte pas","accepter une entente à l'oral",
          "Une entente verbale est valable au Québec, mais elle est impossible à prouver. Demande toujours le formulaire écrit."],
       ]},

      {t:'check', h:"Est-ce que c'est clair maintenant ?",
       p:"Quatre questions rapides.",
       qs:[
         {q:"Un dépôt de garantie, au Québec, c'est…", opts:["normal","interdit"], ok:1,
          fb:"Seul le premier mois peut être demandé."},
         {q:"Un bail dure d'habitude…", opts:["douze mois","six mois"], ok:0,
          fb:"Du 1er juillet au 30 juin."},
         {q:"À la fin du bail, il…", opts:["se renouvelle tout seul","s'arrête"], ok:0,
          fb:"C'est une protection pour le locataire."},
         {q:"On peut te refuser un logement parce que tu as des enfants ?", opts:["oui","non"], ok:1,
          fb:"La Charte des droits l'interdit."},
       ]},

      {t:'revoir', h:"À retenir",
       p:"Le <b>bail</b> est un formulaire officiel de douze mois qui se renouvelle tout seul. On ne donne <b>jamais de dépôt</b> : seulement le premier loyer, le premier jour. Et personne ne peut te refuser un logement à cause de tes enfants."},
    ]
  },
};
