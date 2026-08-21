const PLUS = {
  prPhon: {
    eye:'Mini-leçon', tit:"Le « u » de jupe et le « ou » de rouge",
    blocs:[
      {t:'texte', h:"Deux sons que beaucoup de langues n'ont pas",
       p:"Le français a deux sons très proches à l'oreille et très différents dans la bouche : le <b>u</b> de « jupe » et le <b>ou</b> de « rouge ». Beaucoup de langues n'ont que le second. On entend alors « roge » pour rouge, ou « bou » pour bu — et surtout, on confond deux mots différents.",
       note:"Dans un magasin, ça compte : « une jupe » et « une joupe » n'existent pas toutes les deux, mais « tu » et « tout », « pull » et « poule », oui."},

      {t:'ana', h:"Le son « u » — la bouche petite, la langue en avant",
       p:"C'est le son de « jupe », « tissu », « uni ».",
       mots:[['On écrit','j{u}pe'],['Les lèvres','en rond, très petites',true],['La langue','poussée vers les dents du haut']],
       say:"Une jupe unie, en tissu.",
       note:"Truc : dis « i » longuement, puis arrondis les lèvres sans bouger la langue. Le son qui sort est le « u »."},

      {t:'ana', h:"Le son « ou » — la bouche en rond, la langue au fond",
       p:"C'est le son de « rouge », « foulard », « bouton ».",
       mots:[['On écrit','r{ou}ge'],['Les lèvres','en rond, un peu plus ouvertes',true],['La langue','tirée vers le fond de la bouche']],
       say:"Un foulard rouge à boutons.",
       note:"C'est le son qui existe dans presque toutes les langues. Ce n'est donc pas celui-là qu'il faut travailler : c'est l'autre."},

      {t:'ana', h:"Ce qui les distingue, c'est la langue",
       p:"Les lèvres se ressemblent ; la langue, non.",
       mots:[['u','langue en AVANT'],['ou','langue en ARRIÈRE'],['Le test','mets un doigt sous le menton : ça bouge',true]],
       say:"Jupe, rouge. Jupe, rouge.",
       note:"Si tu ne sens aucune différence entre les deux mots, c'est que la langue ne bouge pas. Elle doit bouger."},

      {t:'labo', h:"Écoute les paires",
       p:"Choisis une paire et écoute la différence.",
       axes:[{id:'p', lbl:'Quelle paire ?', opts:[
         ['a','jupe / joue'],
         ['b','pull / poule'],
         ['c','tissu / tissou'],
         ['d','uni / ouvert'],
         ['e','dans une phrase']]}],
       out:{
         a:{w:['j{u}pe / j{ou}e'], say:"Une jupe, une joue.", n:'u devant, ou derrière'},
         b:{w:['p{u}ll / p{ou}le'], say:"Un pull, une poule.", n:'deux mots bien réels'},
         c:{w:['tiss{u}'], say:"Le tissu est doux.", n:'le mot du magasin'},
         d:{w:['{u}ni / {ou}vert'], say:"Un chandail uni, le magasin ouvert.", n:'les deux sons en début de mot'},
         e:{w:['« Le pull rouge est uni. »'], say:"Le pull rouge est uni.", n:'les deux sons dans la même phrase'},
       },
       note:"Écoute chaque paire deux fois : la première pour comprendre, la seconde en fermant les yeux."},

      {t:'ex', h:"À écouter et à répéter",
       p:"Six phrases du magasin.",
       rows:[
         ["Je cherche une jupe unie.","u trois fois"],
         ["Le foulard rouge est en rabais.","ou deux fois"],
         ["Ce tissu est doux.","u puis ou"],
         ["Le blouson a un capuchon.","ou trois fois"],
         ["Il manque un bouton au pull.","ou puis u"],
         ["Le manteau est en nylon, pas en laine.","ni l'un ni l'autre"],
       ]},

      {t:'piege', h:"Trois pièges à connaître",
       rows:[
         ["remplacer u par ou","« joupe » au lieu de « jupe »",
          "C'est le piège le plus courant. Reviens au truc : dire « i », puis arrondir les lèvres sans bouger la langue."],
         ["croire que la lettre décide","le u de « bouton » ne se dit pas « u »",
          "Quand u et o sont côte à côte, ils font un seul son : « ou ». On lit la paire de lettres, pas chaque lettre."],
         ["oublier que u est aussi un mot","« tu » et « tout » n'ont pas le même sens",
          "Là, la confusion change vraiment la phrase. Ce n'est pas un détail d'accent."],
       ]},

      {t:'check', h:"Est-ce que c'est clair maintenant ?",
       p:"Quatre questions rapides.",
       qs:[
         {q:"« Jupe » a le son…", opts:["u","ou"], ok:0,
          fb:"La langue est en avant."},
         {q:"« Foulard » a le son…", opts:["u","ou"], ok:1,
          fb:"Les lettres o et u ensemble font « ou »."},
         {q:"Ce qui distingue les deux sons, c'est…", opts:["les lèvres","la langue"], ok:1,
          fb:"Les lèvres sont presque pareilles dans les deux."},
         {q:"Pour trouver le « u », on part du son…", opts:["i","a"], ok:0,
          fb:"On dit « i », puis on arrondit les lèvres."},
       ]},
    ]
  },

  prGenre: {
    eye:'Mini-leçon', tit:'Un manteau, une tuque',
    blocs:[
      {t:'texte', h:"Le genre ne se devine pas, il s'apprend",
       p:"En français, chaque vêtement est masculin ou féminin, et rien dans l'objet ne le dit. Un manteau et une veste servent à la même chose ; l'un est masculin, l'autre féminin. Il n'y a donc rien à comprendre — il y a quelque chose à <b>ranger</b> : on apprend toujours le mot avec son déterminant.",
       note:"Écris « un manteau » dans ton carnet, jamais « manteau » tout seul. C'est deux lettres de plus et ça règle la question pour toujours."},

      {t:'ana', h:"Les masculins du module",
       p:"Six mots à retenir avec « un ».",
       mots:[['On dit','{un} manteau'],['Aussi','un chandail · un pantalon · un foulard'],['Et','un cintre · un rabais',true]],
       say:"Un manteau, un chandail, un pantalon.",
       note:"Beaucoup de vêtements du haut et du bas sont masculins, mais ce n'est pas une règle : « une chemise » et « une veste » sont féminines."},

      {t:'ana', h:"Les féminins du module",
       p:"Six mots à retenir avec « une ».",
       mots:[['On dit','{une} tuque'],['Aussi','une jupe · une cabine · une étiquette'],['Et','une facture · une taille',true]],
       say:"Une tuque, une jupe, une facture.",
       note:"Les mots qui finissent par un e muet sont souvent féminins — souvent, pas toujours : « un cintre » finit par un e."},

      {t:'ana', h:"Ceux qui vont toujours par deux",
       p:"Les vêtements qui se portent en paire sont au pluriel.",
       mots:[['On dit','{des} bottes'],['Aussi','des mitaines · des gants · des bas'],['Pour en compter une','une {paire de} bottes',true]],
       say:"Des bottes, des mitaines, une paire de gants.",
       note:"On ne dit jamais « une botte » en magasinant : on achète les deux ensemble."},

      {t:'labo', h:"Un, une ou des ?",
       p:"Choisis un vêtement et vois son déterminant.",
       axes:[
         {id:'v', lbl:'Quel vêtement ?', opts:[['a','manteau'],['b','tuque'],['c','bottes'],['d','chandail']]},
         {id:'q', lbl:'Quelle phrase ?', opts:[['1','je cherche…'],['2','j\'achète…']]}],
       out:{
         a1:{w:["Je cherche un manteau."], say:"Je cherche un manteau.", n:'masculin'},
         a2:{w:["J'achète un manteau noir."], say:"J'achète un manteau noir.", n:'la couleur suit le nom'},
         b1:{w:["Je cherche une tuque."], say:"Je cherche une tuque.", n:'féminin'},
         b2:{w:["J'achète une tuque grise."], say:"J'achète une tuque grise.", n:'l\'adjectif prend un e'},
         c1:{w:["Je cherche des bottes."], say:"Je cherche des bottes.", n:'toujours au pluriel'},
         c2:{w:["J'achète une paire de bottes."], say:"J'achète une paire de bottes.", n:'pour en compter une seule'},
         d1:{w:["Je cherche un chandail."], say:"Je cherche un chandail.", n:'masculin'},
         d2:{w:["J'achète un chandail de laine."], say:"J'achète un chandail de laine.", n:'la matière avec « de »'},
       },
       note:"Huit phrases, toutes correctes, toutes utilisables telles quelles au magasin."},

      {t:'ex', h:"À écouter et à répéter",
       p:"Six phrases du magasin.",
       rows:[
         ["Je cherche un manteau d'hiver.","masculin"],
         ["Elle porte une tuque de laine.","féminin"],
         ["Il me faut des bottes chaudes.","pluriel"],
         ["Où est la cabine d'essayage ?","féminin"],
         ["Gardez la facture, s'il vous plaît.","féminin"],
         ["J'achète une paire de mitaines.","une paire de"],
       ]},

      {t:'piege', h:"Trois pièges à connaître",
       rows:[
         ["apprendre le mot tout seul","« manteau » sans « un »",
          "Sans le déterminant, le genre se perd, et il faudra le réapprendre à chaque fois. Note-le toujours avec l'article."],
         ["chercher une logique","« le manteau est plus gros, donc masculin »",
          "Il n'y en a aucune. Une veste est féminine et un manteau masculin, pour la même chose portée au même endroit."],
         ["mettre une paire au singulier","« une botte »",
          "On dit « des bottes » ou « une paire de bottes ». « Une botte » existe, mais désigne une seule chaussure — ce qu'on n'achète jamais."],
       ]},

      {t:'check', h:"Est-ce que c'est clair maintenant ?",
       p:"Quatre questions rapides.",
       qs:[
         {q:"On dit…", opts:["un tuque","une tuque"], ok:1,
          fb:"Tuque est féminin."},
         {q:"On dit…", opts:["un manteau","une manteau"], ok:0,
          fb:"Manteau est masculin."},
         {q:"Pour acheter des chaussures d'hiver, on dit…", opts:["une botte","des bottes"], ok:1,
          fb:"Elles vont par deux."},
         {q:"La meilleure façon d'apprendre un vêtement, c'est…", opts:["le mot seul","le mot avec son article"], ok:1,
          fb:"Le genre ne se devine pas : il se range avec le mot."},
       ]},
    ]
  },

  t1adj: {
    eye:'Mini-leçon', tit:"La couleur après le vêtement",
    blocs:[
      {t:'texte', h:"Un mot d'ordre : le vêtement d'abord",
       p:"En français, la couleur se place <b>après</b> le nom. On dit « un manteau noir », jamais « un noir manteau ». C'est l'inverse de l'anglais et de plusieurs autres langues, et c'est la première chose qu'on entend quand quelqu'un apprend le français.",
       note:"Bonne nouvelle : la règle n'a pas d'exception pour les couleurs. Le vêtement, puis la couleur, toujours."},

      {t:'ana', h:"Au féminin, on ajoute un e",
       p:"Le vêtement décide de la forme de la couleur.",
       mots:[['Masculin','un manteau noi{r}'],['Féminin','une tuque noi{re}',true],['Aussi','gris → grise · vert → verte · bleu → bleue']],
       say:"Un manteau noir, une tuque noire.",
       note:"Souvent, on entend la différence : « gri » devient « grize », « ver » devient « verte ». Le e fait sonner la consonne d'avant."},

      {t:'ana', h:"Au pluriel, on ajoute un s",
       p:"Deux bottes, deux fois la couleur.",
       mots:[['Un','une botte brun{e}'],['Deux','des bottes brun{es}',true],['Masculin pluriel','des gants gri{s} — déjà un s']],
       say:"Des bottes brunes, des gants gris.",
       note:"Le s ne s'entend pas. Il s'écrit — et l'étiquette, la facture et le courriel s'écrivent."},

      {t:'ana', h:"Les couleurs qui ne changent pas",
       p:"Quatre finissent déjà par un e, deux ne bougent jamais.",
       mots:[['Déjà en e','{rouge} · jaune · rose · beige'],['Jamais rien','{marine} · marron · turquoise',true],['Donc','une tuque rouge, des mitaines rouges']],
       say:"Une tuque rouge, des mitaines rouges.",
       note:"« Marine » et « marron » viennent d'un nom de chose : la mer, le marron. Un nom employé comme couleur ne s'accorde pas."},

      {t:'ana', h:"Pâle et foncé bloquent tout",
       p:"Dès qu'on précise la nuance, plus rien ne s'accorde.",
       mots:[['Simple','des mitaines bleu{es}'],['Avec nuance','des mitaines {bleu pâle}',true],['Aussi','un manteau gris foncé · une jupe vert pâle']],
       say:"Des mitaines bleu pâle, un manteau gris foncé.",
       note:"C'est une règle vraie et souvent ignorée, même par des gens d'ici. Écrire « bleues pâles » ne bloquera personne, mais « bleu pâle » est juste."},

      {t:'labo', h:"Compose ta phrase",
       p:"Choisis un vêtement et une couleur.",
       axes:[
         {id:'v', lbl:'Quel vêtement ?', opts:[['a','un manteau'],['b','une tuque'],['c','des bottes'],['d','des mitaines']]},
         {id:'c', lbl:'Quelle couleur ?', opts:[['1','noir'],['2','gris'],['3','rouge']]}],
       out:{
         a1:{w:["Je cherche un manteau noir."], say:"Je cherche un manteau noir.", n:'masculin singulier : rien à ajouter'},
         a2:{w:["Je cherche un manteau gris."], say:"Je cherche un manteau gris.", n:'gris finit déjà par un s'},
         a3:{w:["Je cherche un manteau rouge."], say:"Je cherche un manteau rouge.", n:'rouge ne change jamais'},
         b1:{w:["Je cherche une tuque noire."], say:"Je cherche une tuque noire.", n:'féminin : un e de plus'},
         b2:{w:["Je cherche une tuque grise."], say:"Je cherche une tuque grise.", n:'le s se prononce z'},
         b3:{w:["Je cherche une tuque rouge."], say:"Je cherche une tuque rouge.", n:'déjà en e : rien ne bouge'},
         c1:{w:["Je cherche des bottes noires."], say:"Je cherche des bottes noires.", n:'féminin pluriel : e puis s'},
         c2:{w:["Je cherche des bottes grises."], say:"Je cherche des bottes grises.", n:'e puis s, comme noires'},
         c3:{w:["Je cherche des bottes rouges."], say:"Je cherche des bottes rouges.", n:'seulement le s'},
         d1:{w:["Je cherche des mitaines noires."], say:"Je cherche des mitaines noires.", n:'même forme que bottes'},
         d2:{w:["Je cherche des mitaines grises."], say:"Je cherche des mitaines grises.", n:'même forme'},
         d3:{w:["Je cherche des mitaines rouges."], say:"Je cherche des mitaines rouges.", n:'même forme'},
       },
       note:"Douze phrases prêtes à dire au magasin. Change seulement le vêtement et la couleur."},

      {t:'ex', h:"À écouter et à répéter",
       p:"Six phrases entendues au magasin.",
       rows:[
         ["Je cherche un manteau noir.","masculin"],
         ["Elle porte une tuque grise.","féminin, on entend le z"],
         ["Il achète des bottes brunes.","féminin pluriel"],
         ["Voici un chandail vert.","masculin, le t est muet"],
         ["Ce sont des mitaines bleues.","féminin pluriel"],
         ["J'aime le manteau bleu foncé.","avec la nuance, rien ne s'accorde"],
       ]},

      {t:'piege', h:"Trois pièges à connaître",
       rows:[
         ["mettre la couleur devant","« un noir manteau »",
          "C'est compris, mais c'est immédiatement reconnu comme une erreur d'apprenant. Le vêtement d'abord, toujours."],
         ["accorder rouge au féminin","« une tuque rouge », pas « rougee »",
          "Rouge, jaune, rose et beige finissent déjà par un e : au féminin, on n'ajoute rien."],
         ["accorder après pâle ou foncé","« des mitaines bleues pâles »",
          "Dès qu'une nuance s'ajoute, l'ensemble ne s'accorde plus : « des mitaines bleu pâle »."],
       ]},

      {t:'check', h:"Est-ce que c'est clair maintenant ?",
       p:"Quatre questions rapides.",
       qs:[
         {q:"On dit…", opts:["un manteau noir","un noir manteau"], ok:0,
          fb:"La couleur vient après le nom."},
         {q:"Une tuque de couleur grise, c'est…", opts:["une tuque gris","une tuque grise"], ok:1,
          fb:"Au féminin, on ajoute un e."},
         {q:"Des bottes de couleur rouge, c'est…", opts:["des bottes rouges","des bottes rougees"], ok:0,
          fb:"Rouge finit déjà par un e ; on n'ajoute que le s."},
         {q:"Avec « pâle », on écrit…", opts:["des mitaines bleues pâles","des mitaines bleu pâle"], ok:1,
          fb:"La nuance bloque l'accord."},
       ]},
    ]
  },

  t1taille: {
    eye:'Mini-leçon', tit:'Taille, pointure et essayage',
    blocs:[
      {t:'texte', h:"Trois lettres à connaître avant d'entrer",
       p:"Ici, la taille d'un vêtement s'écrit presque toujours <b>P</b>, <b>M</b> ou <b>G</b> — petit, moyen, grand — avec parfois <b>TP</b> et <b>TG</b> aux deux bouts. Les chiffres existent aussi, surtout pour les pantalons et les robes. Si tu viens d'un pays qui emploie un autre système, ton chiffre ne se traduit pas : il faut essayer.",
       note:"Aucune honte à ne pas savoir sa taille. La bonne phrase est : « Je ne connais pas ma taille ici, je vais essayer. »"},

      {t:'ana', h:"La taille, pour le vêtement",
       p:"Ce qui se porte sur le corps.",
       mots:[['On demande','Vous portez quelle {taille} ?'],['On répond','Du {moyen}, je pense.',true],['Sur l\'étiquette','P · M · G · TG']],
       say:"Vous portez quelle taille ? Du moyen, je pense.",
       note:"« Je fais du moyen » et « je porte du moyen » se disent tous les deux."},

      {t:'ana', h:"La pointure, pour le pied",
       p:"Ce qui se porte aux pieds a son propre mot.",
       mots:[['On demande','Quelle {pointure} faites-vous ?'],['On répond','Je fais du {sept}.',true],['Le piège','ce n\'est jamais « la taille » des bottes']],
       say:"Quelle pointure faites-vous ? Je fais du sept.",
       note:"Les pointures d'ici ne sont pas celles de l'Europe : un 38 européen est environ un 7 ici."},

      {t:'ana', h:"Dire ce qui ne va pas",
       p:"Un adjectif et un endroit du corps, c'est assez.",
       mots:[['Trop petit','c\'est trop {serré} aux épaules'],['Trop grand','c\'est un peu {large}'],['Trop long','les manches sont trop {longues}',true]],
       say:"C'est trop serré aux épaules.",
       note:"Nommer l'endroit est ce qui aide vraiment la conseillère : « serré » seul ne dit pas s'il faut une autre taille ou une autre coupe."},

      {t:'labo', h:"Demande une autre taille",
       p:"Choisis le problème et la suite.",
       axes:[
         {id:'p', lbl:'Quel problème ?', opts:[['a','trop serré'],['b','trop grand'],['c','manches longues']]},
         {id:'q', lbl:'Que demandes-tu ?', opts:[['1','une autre taille'],['2','un autre modèle']]}],
       out:{
         a1:{w:["C'est trop serré. Vous l'avez en grand ?"], say:"C'est trop serré. Vous l'avez en grand ?", n:'la demande la plus simple'},
         a2:{w:["C'est trop serré aux épaules. Vous avez une autre coupe ?"], say:"C'est trop serré aux épaules. Vous avez une autre coupe ?", n:'quand la taille au-dessus serait trop grande'},
         b1:{w:["C'est un peu large. Vous l'avez en moyen ?"], say:"C'est un peu large. Vous l'avez en moyen ?", n:'on descend d\'une taille'},
         b2:{w:["C'est un peu large. Vous avez un autre modèle ?"], say:"C'est un peu large. Vous avez un autre modèle ?", n:'même taille, coupe différente'},
         c1:{w:["Les manches sont trop longues. Vous l'avez en petit ?"], say:"Les manches sont trop longues. Vous l'avez en petit ?", n:'les manches suivent la taille'},
         c2:{w:["Les manches sont trop longues. Vous avez un modèle plus court ?"], say:"Les manches sont trop longues. Vous avez un modèle plus court ?", n:'utile quand le reste va bien'},
       },
       note:"Six phrases, toutes prêtes à dire dans une cabine d'essayage."},

      {t:'ex', h:"À écouter et à répéter",
       p:"Six phrases du défi.",
       rows:[
         ["Vous portez quelle taille ?","la question du magasin"],
         ["Je ne connais pas ma taille ici.","la phrase qui sauve"],
         ["Je peux l'essayer ?","avant d'entrer dans la cabine"],
         ["Où est la cabine d'essayage ?","la question suivante"],
         ["C'est trop serré aux épaules.","adjectif et endroit"],
         ["Vous l'avez en grand ?","demander l'autre taille"],
       ]},

      {t:'piege', h:"Trois pièges à connaître",
       rows:[
         ["traduire son chiffre","« je fais du 42 »",
          "Les systèmes ne se correspondent pas d'un pays à l'autre. Le seul moyen sûr est d'essayer, et personne ne trouvera ça étrange."],
         ["dire « taille » pour les bottes","les pieds ont une pointure",
          "On sera compris, mais le mot juste est « pointure ». Il ne sert qu'aux chaussures — c'est facile à retenir."],
         ["acheter sans essayer","« ça devrait faire »",
          "Un manteau se porte par-dessus un chandail : essaie avec ce que tu portes l'hiver, pas en t-shirt."],
       ]},

      {t:'check', h:"Est-ce que c'est clair maintenant ?",
       p:"Quatre questions rapides.",
       qs:[
         {q:"Sur l'étiquette, M veut dire…", opts:["moyen","mince"], ok:0,
          fb:"P, M, G : petit, moyen, grand."},
         {q:"Pour des bottes, on demande…", opts:["la taille","la pointure"], ok:1,
          fb:"La pointure ne sert qu'aux chaussures."},
         {q:"Le manteau presse aux épaules. Tu dis…", opts:["c'est trop large","c'est trop serré"], ok:1,
          fb:"Serré veut dire trop petit."},
         {q:"Tu ne connais pas ta taille ici. Tu dis…", opts:["rien, tu devines","je vais essayer"], ok:1,
          fb:"Essayer est la seule façon d'en être sûr."},
       ]},
    ]
  },

  t2comparer: {
    eye:'Mini-leçon', tit:'Plus cher, moins cher, aussi cher',
    blocs:[
      {t:'texte', h:"Comparer, c'est trois mots",
       p:"Pour comparer deux articles, le français emploie trois mots seulement : <b>plus</b>, <b>moins</b> et <b>aussi</b>, suivis de l'adjectif et de <b>que</b>. « Les bottes sont <b>moins</b> chères <b>que</b> le manteau. » Une fois ce moule appris, il sert pour le prix, la chaleur, la longueur, la qualité — tout.",
       note:"C'est aussi ce qui permet de dire son choix à voix haute : « Je prends celles-ci, elles sont moins chères. »"},

      {t:'ana', h:"Plus … que — davantage",
       p:"L'article a davantage de la qualité nommée.",
       mots:[['Le moule','{plus} + adjectif + {que}'],['Exemple','La laine est {plus} chaude {que} l\'acrylique.',true],['Le prix','Ce manteau est plus cher que l\'autre.']],
       say:"La laine est plus chaude que l'acrylique.",
       note:"Attention : « plus cher » veut dire qu'il coûte davantage, pas qu'il est meilleur."},

      {t:'ana', h:"Moins … que — pas autant",
       p:"C'est le contraire exact.",
       mots:[['Le moule','{moins} + adjectif + {que}'],['Exemple','Les bottes sont {moins} chères {que} le manteau.',true],['Utile','C\'est le mot qui décide un achat.']],
       say:"Les bottes sont moins chères que le manteau.",
       note:"En magasinant, « moins cher » est la phrase la plus utile du module."},

      {t:'ana', h:"Aussi … que — la même chose",
       p:"Les deux articles se valent sur ce point.",
       mots:[['Le moule','{aussi} + adjectif + {que}'],['Exemple','Ce chandail est {aussi} chaud {que} l\'autre.',true],['Attention','« aussi » veut aussi dire « en plus » — le {que} lève le doute.']],
       say:"Ce chandail est aussi chaud que l'autre.",
       note:"Sans le « que », « aussi » change de sens : « je prends aussi une tuque » veut dire « en plus »."},

      {t:'ana', h:"Deux formes irrégulières",
       p:"Deux mots refusent le moule.",
       mots:[['bon','→ {meilleur}, jamais « plus bon »'],['bien','→ {mieux}, jamais « plus bien »',true],['Exemple','La laine est meilleure pour l\'hiver.']],
       say:"La laine est meilleure que l'acrylique pour l'hiver.",
       note:"Ce sont les deux seules du niveau. « Meilleur » s'accorde comme un adjectif : meilleur, meilleure, meilleurs, meilleures."},

      {t:'labo', h:"Compare deux articles",
       p:"Choisis les deux articles et ce que tu compares.",
       axes:[
         {id:'a', lbl:'Quels articles ?', opts:[['a','deux paires de bottes'],['b','deux tuques'],['c','deux manteaux']]},
         {id:'q', lbl:'Tu compares…', opts:[['1','le prix'],['2','la chaleur'],['3','rien : c\'est pareil']]}],
       out:{
         a1:{w:["Celles-ci sont moins chères que celles-là."], say:"Celles-ci sont moins chères que celles-là.", n:'65 $ contre 99 $'},
         a2:{w:["Celles-là sont plus chaudes : elles sont doublées en laine."], say:"Celles-là sont plus chaudes : elles sont doublées en laine.", n:'la doublure décide'},
         a3:{w:["Les deux paires sont aussi chaudes l'une que l'autre."], say:"Les deux paires sont aussi chaudes l'une que l'autre.", n:'quand rien ne départage'},
         b1:{w:["Celle-ci est plus chère que celle-là."], say:"Celle-ci est plus chère que celle-là.", n:'22 $ contre 14 $'},
         b2:{w:["La tuque de laine est plus chaude que celle en acrylique."], say:"La tuque de laine est plus chaude que celle en acrylique.", n:'la matière décide'},
         b3:{w:["Les deux tuques sont aussi douces l'une que l'autre."], say:"Les deux tuques sont aussi douces l'une que l'autre.", n:'même toucher'},
         c1:{w:["Ce manteau est moins cher que l'autre."], say:"Ce manteau est moins cher que l'autre.", n:'la phrase du magasin'},
         c2:{w:["Ce manteau est plus chaud : il a un capuchon."], say:"Ce manteau est plus chaud : il a un capuchon.", n:'un détail qui compte en janvier'},
         c3:{w:["Les deux manteaux sont aussi chauds l'un que l'autre."], say:"Les deux manteaux sont aussi chauds l'un que l'autre.", n:'il faudra choisir autrement'},
       },
       note:"Neuf comparaisons, toutes utilisables telles quelles devant deux articles."},

      {t:'ex', h:"À écouter et à répéter",
       p:"Six comparaisons du magasin.",
       rows:[
         ["Ces bottes sont moins chères.","le mot qui décide"],
         ["La laine est plus chaude que l'acrylique.","la matière"],
         ["Les deux manteaux sont aussi chauds.","égalité"],
         ["Celui-ci est plus long que celui-là.","la longueur"],
         ["La laine est meilleure pour janvier.","irrégulier : meilleure"],
         ["Je prends celles-ci : elles coûtent moins cher.","dire son choix"],
       ]},

      {t:'piege', h:"Trois pièges à connaître",
       rows:[
         ["oublier le « que »","« les bottes sont moins chères »",
          "La phrase reste en l'air : moins chères que quoi ? Nomme le deuxième article, ou dis « que l'autre »."],
         ["dire « plus bon »","le français dit « meilleur »",
          "C'est l'erreur la plus entendue. « Plus bon » n'existe pas ; « meilleur » le remplace, et il s'accorde."],
         ["ne pas accorder l'adjectif","« ces bottes sont plus cher »",
          "Comparer ne dispense pas d'accorder : « plus chères », au féminin pluriel comme les bottes."],
       ]},

      {t:'check', h:"Est-ce que c'est clair maintenant ?",
       p:"Quatre questions rapides.",
       qs:[
         {q:"65 $ contre 99 $ : les premières sont…", opts:["plus chères","moins chères"], ok:1,
          fb:"Elles coûtent moins."},
         {q:"Le mot qui ferme la comparaison est…", opts:["que","de"], ok:0,
          fb:"Plus … que, moins … que, aussi … que."},
         {q:"Le comparatif de « bon » est…", opts:["plus bon","meilleur"], ok:1,
          fb:"« Plus bon » n'existe pas."},
         {q:"Deux prix identiques : on dit…", opts:["aussi cher que","autant cher que"], ok:0,
          fb:"Avec un adjectif, c'est « aussi »."},
       ]},
    ]
  },

  t2celui: {
    eye:'Mini-leçon', tit:'Celui-ci, celui-là',
    blocs:[
      {t:'texte', h:"Montrer sans répéter le nom",
       p:"Devant deux manteaux, on ne dit pas « le manteau bleu est moins cher que le manteau noir ». On dit « <b>celui-ci</b> est moins cher que <b>celui-là</b> ». Ces mots remplacent le vêtement dont on parle, et ils vont presque toujours avec le doigt qui montre.",
       note:"Dans un magasin, montrer et dire « celui-là, s'il vous plaît » est parfaitement poli. C'est même plus clair qu'une longue description."},

      {t:'ana', h:"Quatre formes, selon le vêtement",
       p:"La forme suit le genre et le nombre du mot remplacé.",
       mots:[['un manteau','{celui}'],['une tuque','{celle}'],['des gants','{ceux} · des bottes → {celles}',true]],
       say:"Celui, celle, ceux, celles.",
       note:"C'est le seul endroit où il faut connaître le genre du vêtement. D'où l'exercice « un ou une ? » de la première section."},

      {t:'ana', h:"-ci pour près, -là pour loin",
       p:"Le petit mot collé au bout dit la distance.",
       mots:[['Près de moi','celui{-ci}'],['Plus loin','celui{-là}',true],['Ensemble','Celui-ci est en nylon, celui-là est en laine.']],
       say:"Celui-ci est en nylon, celui-là est en laine.",
       note:"On les emploie surtout par deux, pour opposer. Seul, « celui-là » suffit quand on montre du doigt."},

      {t:'ana', h:"Ne pas confondre avec ce et cette",
       p:"Deux familles voisines, deux emplois différents.",
       mots:[['Suivi du nom','{ce} manteau · {cette} tuque'],['À la place du nom','{celui-ci} · {celle-ci}',true],['Jamais','« ce celui-ci »']],
       say:"Ce manteau-ci, ou celui-ci.",
       note:"« Ce manteau-ci » et « celui-ci » disent la même chose. Le premier garde le nom, le second le remplace."},

      {t:'labo', h:"Montre du doigt",
       p:"Choisis le vêtement et la distance.",
       axes:[
         {id:'v', lbl:'Quel vêtement ?', opts:[['a','un manteau'],['b','une tuque'],['c','des bottes'],['d','des gants']]},
         {id:'d', lbl:'Où est-il ?', opts:[['1','près de toi'],['2','plus loin']]}],
       out:{
         a1:{w:["Celui-ci est à combien ?"], say:"Celui-ci est à combien ?", n:'masculin singulier'},
         a2:{w:["Je voudrais essayer celui-là."], say:"Je voudrais essayer celui-là.", n:'masculin singulier, plus loin'},
         b1:{w:["Celle-ci est en laine ?"], say:"Celle-ci est en laine ?", n:'féminin singulier'},
         b2:{w:["Je préfère celle-là."], say:"Je préfère celle-là.", n:'féminin singulier, plus loin'},
         c1:{w:["Celles-ci sont en liquidation ?"], say:"Celles-ci sont en liquidation ?", n:'féminin pluriel'},
         c2:{w:["Je prends celles-là."], say:"Je prends celles-là.", n:'féminin pluriel, plus loin'},
         d1:{w:["Ceux-ci sont trop grands."], say:"Ceux-ci sont trop grands.", n:'masculin pluriel'},
         d2:{w:["Vous avez ceux-là en noir ?"], say:"Vous avez ceux-là en noir ?", n:'masculin pluriel, plus loin'},
       },
       note:"Huit phrases prêtes à dire, le doigt tendu."},

      {t:'ex', h:"À écouter et à répéter",
       p:"Six phrases du magasin.",
       rows:[
         ["Celui-ci est à combien ?","masculin, près"],
         ["Celle-là est plus chaude.","féminin, loin"],
         ["Celles-ci sont en liquidation.","féminin pluriel"],
         ["Je prends ceux-là.","masculin pluriel"],
         ["Celui-ci est moins cher que celui-là.","les deux ensemble"],
         ["Ce manteau-ci me va bien.","avec le nom gardé"],
       ]},

      {t:'piege', h:"Trois pièges à connaître",
       rows:[
         ["oublier -ci ou -là","« celui est moins cher »",
          "« Celui » ne se dit jamais tout seul dans cette phrase. Il faut « celui-ci », « celui-là », ou une suite : « celui que je préfère »."],
         ["se tromper de genre","« celui-ci » pour une tuque",
          "La forme suit le mot remplacé : une tuque est féminine, donc « celle-ci »."],
         ["doubler le démonstratif","« ce celui-ci »",
          "On choisit : ou bien « ce manteau-ci », ou bien « celui-ci ». Jamais les deux."],
       ]},

      {t:'check', h:"Est-ce que c'est clair maintenant ?",
       p:"Quatre questions rapides.",
       qs:[
         {q:"Pour une tuque tout près, on dit…", opts:["celui-ci","celle-ci"], ok:1,
          fb:"Tuque est féminin."},
         {q:"Pour des bottes plus loin, on dit…", opts:["celles-là","ceux-là"], ok:0,
          fb:"Bottes est féminin pluriel."},
         {q:"« -ci » veut dire…", opts:["près","loin"], ok:0,
          fb:"-ci pour près, -là pour loin."},
         {q:"On peut dire…", opts:["ce celui-ci","ce manteau-ci"], ok:1,
          fb:"On garde le nom, ou on le remplace — pas les deux."},
       ]},
    ]
  },

  t3entretien: {
    eye:'Mini-leçon', tit:"L'étiquette d'entretien",
    blocs:[
      {t:'texte', h:"Cinq dessins, et une règle qui les explique tous",
       p:"Dans le col ou sur le côté, une petite étiquette de tissu porte quatre ou cinq dessins. Elle dit comment laver le vêtement sans l'abîmer. Une seule règle suffit pour commencer : un dessin <b>barré</b> d'une croix veut toujours dire <b>ne pas faire</b>.",
       note:"C'est l'intention « lire une étiquette » du programme. Elle vaut de l'argent : un chandail de laine passé à la sécheuse devient un chandail d'enfant."},

      {t:'ana', h:"Le bassin — laver",
       p:"Un petit bac d'eau vu de face.",
       mots:[['Le dessin','un bassin avec de l\'eau'],['Le chiffre dedans','la température : {30} = eau froide',true],['Une main dedans','laver à la {main}']],
       say:"Laver à trente degrés, à l'eau froide.",
       note:"Barré, il veut dire « ne pas laver à l'eau » : le vêtement va chez le nettoyeur."},

      {t:'ana', h:"Le carré avec un rond — la sécheuse",
       p:"Un carré, et un cercle à l'intérieur.",
       mots:[['Le dessin','un carré contenant un rond'],['Barré','{ne pas} mettre à la sécheuse',true],['Les points','la chaleur : un point = doux']],
       say:"Ne pas mettre à la sécheuse.",
       note:"C'est le dessin le plus important à reconnaître. La sécheuse est ce qui abîme le plus le linge d'hiver."},

      {t:'ana', h:"Le triangle — le javellisant",
       p:"Un triangle vide.",
       mots:[['Le dessin','un triangle'],['Barré','{ne pas} javelliser',true],['Sur la couleur','le javellisant fait des taches jaunes']],
       say:"Ne pas javelliser.",
       note:"Le javellisant blanchit. Sur un vêtement de couleur, il ne nettoie pas : il décolore, et ça ne se répare pas."},

      {t:'ana', h:"Le fer et le rond",
       p:"Les deux derniers dessins.",
       mots:[['Le fer','repasser · les points disent la chaleur'],['Le rond','le nettoyage {à sec}, chez le nettoyeur',true],['Barrés','ne pas repasser · ne pas nettoyer à sec']],
       say:"Ne pas repasser. Nettoyage à sec seulement.",
       note:"Le rond avec une lettre dedans est une consigne pour le nettoyeur, pas pour toi : il saura la lire."},

      {t:'ana', h:"Ne pas + infinitif",
       p:"La forme employée sur toutes les étiquettes.",
       mots:[['On écrit','{Ne pas} javelliser.'],['On ne dit pas','« Ne javellisez pas » — trop long pour une étiquette',true],['Aussi','Ne pas mettre à la sécheuse. Ne pas repasser.']],
       say:"Ne pas mettre à la sécheuse. Ne pas javelliser.",
       note:"Cette forme courte se retrouve partout : sur les portes, sur les machines, sur les médicaments. Elle vaut la peine d'être reconnue."},

      {t:'labo', h:"Que dit ce dessin ?",
       p:"Choisis un dessin et vois ce qu'il veut dire.",
       axes:[
         {id:'d', lbl:'Quel dessin ?', opts:[['a','le bassin'],['b','le carré à rond'],['c','le triangle'],['d','le fer']]},
         {id:'b', lbl:'Est-il barré ?', opts:[['1','non'],['2','oui']]}],
       out:{
         a1:{w:["Laver à la machine, à trente degrés."], say:"Laver à la machine, à trente degrés.", n:'le chiffre donne la température'},
         a2:{w:["Ne pas laver à l'eau."], say:"Ne pas laver à l'eau.", n:'ce vêtement va chez le nettoyeur'},
         b1:{w:["On peut mettre à la sécheuse, chaleur douce."], say:"On peut mettre à la sécheuse, chaleur douce.", n:'un point = doux'},
         b2:{w:["Ne pas mettre à la sécheuse."], say:"Ne pas mettre à la sécheuse.", n:'le plus important à reconnaître'},
         c1:{w:["On peut javelliser."], say:"On peut javelliser.", n:'rare, et seulement sur du blanc'},
         c2:{w:["Ne pas javelliser."], say:"Ne pas javelliser.", n:'sinon, des taches jaunes'},
         d1:{w:["Repasser à chaleur moyenne."], say:"Repasser à chaleur moyenne.", n:'deux points = moyen'},
         d2:{w:["Ne pas repasser."], say:"Ne pas repasser.", n:'le fer ferait fondre le tissu'},
       },
       note:"Huit lectures d'étiquette. Barré ou non : c'est la seule chose à regarder en premier."},

      {t:'ex', h:"À écouter et à répéter",
       p:"Six consignes d'étiquette.",
       rows:[
         ["Laver à trente degrés.","eau froide"],
         ["Ne pas mettre à la sécheuse.","le plus fréquent"],
         ["Ne pas javelliser.","le triangle barré"],
         ["Ne pas repasser.","le fer barré"],
         ["Nettoyage à sec seulement.","le rond"],
         ["Sécher à plat.","souvent écrit en mots"],
       ]},

      {t:'piege', h:"Trois pièges à connaître",
       rows:[
         ["croire que le chiffre est un prix","30 dans le bassin, c'est 30 degrés",
          "L'étiquette d'entretien ne parle jamais d'argent. Le prix est sur l'autre étiquette, en carton."],
         ["laver la laine à l'eau chaude","le chandail rapetisse et ne revient pas",
          "C'est l'accident le plus courant. L'eau froide et le séchage à plat sauvent un chandail de laine."],
         ["jeter l'étiquette","elle est cousue pour rester",
          "On la coupe parce qu'elle pique — et six mois plus tard, plus personne ne sait comment laver le vêtement. Prends-la en photo avant de la couper."],
       ]},

      {t:'check', h:"Est-ce que c'est clair maintenant ?",
       p:"Quatre questions rapides.",
       qs:[
         {q:"Un dessin barré veut dire…", opts:["ne pas faire","faire doucement"], ok:0,
          fb:"C'est la règle qui explique tous les dessins."},
         {q:"Le 30 dans le bassin, c'est…", opts:["le prix","la température"], ok:1,
          fb:"Trente degrés : de l'eau froide."},
         {q:"Le carré avec un rond parle de…", opts:["la sécheuse","le fer"], ok:0,
          fb:"Le fer a la forme d'un fer."},
         {q:"Sur un chandail de couleur, le javellisant…", opts:["nettoie mieux","fait des taches"], ok:1,
          fb:"Il décolore, et ça ne se répare pas."},
       ]},
    ]
  },
};
