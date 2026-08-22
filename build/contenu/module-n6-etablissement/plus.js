const PLUS = {
  // Quinze mini-leçons. La clé d'une mini-leçon est l'`id` de l'exercice
  // qu'elle explique : c'est ce qui permet au bandeau d'aide de proposer la
  // bonne leçon après plusieurs erreurs. Une clé qui ne correspond à aucun
  // exercice n'est jamais atteignable.
  //
  // Tout bloc `ana` porte son champ `say:` — sans lui, l'extrait audio lit
  // les balises HTML à voix haute, et ça ne se découvre qu'une fois les MP3
  // payés.

  prGraphie: {
    eye:'Mini-leçon', tit:"Quand la lettre ment : ch, x, sh",
    blocs:[
      {t:'texte', h:"Pourquoi ça compte dans un établissement",
       p:"Vous entendez un mot pour la première fois dans un bureau : « psychologie », « technologie », « soixante ». Vous l'écrivez comme vous l'avez entendu, vous le cherchez, et vous ne le trouvez pas. Le mot existe pourtant — il ne s'écrit simplement pas comme il se dit. Trois cas seulement, et ils reviennent partout dans les noms de matières.",
       note:"Le programme du niveau 6 nomme ces trois cas : « ch » qui se dit comme un k, « x » qui se dit comme un s, « sh » et « sch » qui se disent comme un ch."},

      {t:'ana', h:"Cas 1 — « ch » qui se dit comme un K",
       p:"Presque toujours dans des mots venus du grec. Ce sont des mots savants, et les noms de matières en sont pleins.",
       mots:[['On écrit','la psy{ch}ologie · une {ch}ronologie · un or{ch}estre · une {ch}orale'],
             ['On entend','[k], comme dans « kilo »', true],
             ['Le repère','un mot savant, souvent avec un « y » ou un « ph » à côté']],
       say:"la psychologie, une chronologie, un orchestre, une chorale",
       note:"Attention : « chercher », « chaque », « chose » gardent le son normal. Le K est l'exception, jamais la règle."},

      {t:'ana', h:"Cas 2 — « x » qui se dit comme un S",
       p:"Dans trois nombres surtout, et vous les entendrez dix fois par rendez-vous.",
       mots:[['On écrit','si{x} · di{x} · soi{x}ante'],
             ['On entend','[s], comme dans « dis »', true],
             ['Le piège du nombre','« dix » se dit [dis] tout seul, [di] devant une consonne, [diz] devant une voyelle']],
       say:"six, dix, soixante",
       note:"« Dix dollars » se dit « di dollars ». « Dix ans » se dit « diz ans ». « Dix », tout seul, se dit « dis »."},

      {t:'ana', h:"Cas 3 — « sh » et « sch » qui se disent comme un CH",
       p:"Des mots empruntés à l'anglais ou à l'allemand, devenus courants.",
       mots:[['On écrit','un {sch}éma · un {sh}ampoing · un {sh}ort'],
             ['On entend','le son de « chat »', true],
             ['Le repère',"un mot court, venu d'ailleurs"]],
       say:"un schéma, un shampoing, un short",
       note:"« Un schéma », dans une brochure de programme, revient très souvent : c'est le dessin qui accompagne une explication."},

      {t:'labo', h:"Écoutez, puis répétez",
       p:"Choisissez un cas et un exemple.",
       axes:[
         {id:'c', lbl:'Quelles lettres ?', opts:[['a','ch qui dit K'],['b','x qui dit S'],['c','sh, sch qui disent CH']]},
         {id:'n', lbl:'Quel exemple ?', opts:[['1','le premier'],['2','le second']]}],
       out:{
         a1:{w:["la psychologie"], say:"la psychologie", n:'mot grec : « psi-co-lo-gie »'},
         a2:{w:["un orchestre"], say:"un orchestre", n:'« or-kestre », jamais « or-chestre »'},
         b1:{w:["six"], say:"six", n:'tout seul, on entend le S final'},
         b2:{w:["soixante"], say:"soixante", n:'« soi-sante », jamais « soi-ksante »'},
         c1:{w:["un schéma"], say:"un schéma", n:'trois lettres pour le son de « chat »'},
         c2:{w:["un short"], say:"un short", n:"venu de l'anglais, prononcé à la française"},
       },
       note:"Écoutez deux fois avant de répéter. C'est l'oreille qu'on entraîne, pas la mémoire."},

      {t:'ex', h:"Huit mots du module",
       p:"À gauche ce qui est écrit, à droite ce qui se dit.",
       rows:[
         ["la psychologie","« psi-co-lo-gie » — le ch fait k"],
         ["une chronologie","« cro-no-lo-gie » — le ch fait k"],
         ["un orchestre","« or-kestre » — le ch fait k"],
         ["la technologie","« tec-no-lo-gie » — le ch fait k"],
         ["six semaines","« si semaines » — le x se tait devant une consonne"],
         ["soixante","« soi-sante » — le x fait s"],
         ["un schéma","« ché-ma » — sch fait ch"],
         ["un short","« chort » — sh fait ch"],
       ]},

      {t:'piege', h:"Deux pièges, une consolation",
       rows:[
         ["chercher le mot avec la lettre entendue","chercher avec la lettre écrite",
          "Vous entendez « cronologie » et vous cherchez « cronologie » : rien. Quand un mot entendu ne se trouve pas, essayez « ch » à la place du k, et « x » à la place du s."],
         ["prononcer chaque « ch » comme dans « chat »","reconnaître les mots savants",
          "« Technologie » dite avec le son de « chat » ne se comprend pas du tout. Ces mots-là sont peu nombreux : ils s'apprennent un par un."],
         ["s'inquiéter pour « dix »","les trois formes se comprennent",
          "Personne ne vous reprendra si vous dites « diz jours ». Ce qui compte, c'est de reconnaître les trois formes à l'écoute, pas de les produire parfaitement."],
       ]},

      {t:'check', h:"Est-ce que c'est clair maintenant ?",
       p:"Quatre questions rapides.",
       qs:[
         {q:"Dans « psychologie », les lettres « ch » se disent…", opts:["comme dans chat","comme un k"], ok:1,
          fb:"C'est un mot venu du grec : « psi-co-lo-gie »."},
         {q:"Dans « soixante », la lettre « x » se dit…", opts:["comme un s","comme un ks"], ok:0,
          fb:"« Soi-sante ». Même chose dans « dix » et « six »."},
         {q:"Dans « un schéma », les lettres « sch » se disent…", opts:["comme un sk","comme dans chat"], ok:1,
          fb:"Trois lettres pour un seul son, celui de « chat »."},
         {q:"« Six semaines » se prononce…", opts:["« si semaines »","« siss semaines »"], ok:0,
          fb:"Devant une consonne, le x de « six » ne s'entend pas."},
       ]},

      {t:'revoir', h:"À retenir",
       p:"Trois cas seulement : <b>ch</b> qui dit k dans les mots savants (psychologie, orchestre), <b>x</b> qui dit s dans trois nombres (six, dix, soixante), <b>sh</b> et <b>sch</b> qui disent ch dans les mots empruntés (short, schéma)."},
    ]
  },

  prPapiers: {
    eye:'Mini-leçon', tit:"Ce qui se dit ne compte pas ; ce qui s'écrit compte",
    blocs:[
      {t:'texte', h:"La règle non écrite d'un établissement",
       p:"Dans une école, un centre, un bureau, une chose entendue au comptoir n'engage personne. Ce n'est pas de la mauvaise volonté : la personne qui vous a parlé partira, changera de poste, oubliera. Le papier, lui, reste au dossier. C'est pour cela qu'un adulte qui sait demander un écrit avance deux fois plus vite qu'un adulte qui sait bien parler.",
       note:"Le savoir du programme s'appelle « tenir compte de la présentation matérielle et de la mise en page ». Il commence ici, avec le genre de chaque papier."},

      {t:'ana', h:"Les papiers qui prouvent",
       p:"Ils disent ce qui a eu lieu, et ils ne se discutent pas.",
       mots:[['Le relevé de notes','les cours réussis et le résultat de chacun'],
             ["L'attestation de fréquentation",'les dates auxquelles vous étiez inscrit et présent', true],
             ["L'évaluation comparative",'à quel niveau d’ici se comparent des études faites ailleurs']],
       say:"un relevé de notes, une attestation de fréquentation, une évaluation comparative",
       note:"On les demande au comptoir, et jamais aucun ne s'obtient le jour même."},

      {t:'ana', h:"Les papiers qui décident",
       p:"Ils annoncent ce que l'établissement a choisi de faire. Ils portent toujours une date.",
       mots:[["L'avis officiel",'une décision, sa date et parfois sa condition'],
             ['Le plan de formation',"l'ordre des cours et le temps prévu pour chacun", true],
             ['La convocation','un lieu, une heure, et une obligation de se présenter']],
       say:"un avis officiel, un plan de formation, une convocation",
       note:"Un avis ne se conteste pas au comptoir : il se conteste par écrit, à la personne nommée dans sa dernière ligne."},

      {t:'ana', h:"Les papiers que vous écrivez",
       p:"Ce sont les seuls sur lesquels vous avez la main. Écrivez-les précisément.",
       mots:[['La demande de rencontre','ce que vous cherchez, en deux lignes'],
             ['Le courriel au secrétariat','une demande, une date, une signature', true],
             ['Le compte rendu','ce qui a été dit et décidé — demandez-le, ou faites-le']],
       say:"une demande de rencontre, un courriel au secrétariat, un compte rendu",
       note:"« Je veux de l'information » ne veut rien dire. « Je veux savoir quels préalables il me manque » veut dire quelque chose."},

      {t:'ex', h:"Cinq endroits à regarder avant de lire",
       p:"Sur n'importe quel document officiel, dans cet ordre.",
       rows:[
         ["Le nom en haut à gauche","Quel établissement parle. Il ne parle jamais au nom d'un autre."],
         ["La ligne en gras","Le genre du document, donc ce que le reste va contenir."],
         ["Votre nom et votre adresse","Une lettre adressée à quelqu'un d'autre n'engage personne."],
         ["Les deux dates","Celle où le papier a été écrit, celle avant laquelle vous devez agir."],
         ["Le numéro de dossier","Sans lui, un appel téléphonique ne mène nulle part."],
       ]},

      {t:'piege', h:"Trois pièges",
       rows:[
         ["se fier à ce qu'on vous a dit au comptoir","demander où c'est écrit",
          "« On m'avait dit que ça comptait. » Cette phrase ne sauve personne. Demandez : « Est-ce que je peux avoir ça par écrit ? » — c'est une question polie et parfaitement normale."],
         ["confondre les deux dates d'un document","souligner celle qui vous oblige",
          "La date en haut est celle de l'envoi. Celle qui compte est plus bas, souvent dans l'encadré, et c'est la seule à noter dans un calendrier."],
         ["jeter un papier qu'on croit inutile","tout garder, et laisser trier",
          "C'est le conseiller qui trie, pas vous. Une évaluation comparative ne sert pas à l'admission, mais elle explique un parcours en trente secondes."],
       ]},

      {t:'revoir', h:"À retenir",
       p:"Trois familles : ce qui <b>prouve</b> (relevé, attestation, évaluation), ce qui <b>décide</b> (avis, plan, convocation), ce que <b>vous écrivez</b> (demande, courriel, compte rendu). Et une règle : ce qui n'est pas au dossier n'existe pas."},
    ]
  },

  t1repr: {
    eye:'Mini-leçon', tit:"Le, en, y : trois mots qui renvoient en arrière",
    blocs:[
      {t:'texte', h:"Où l'on perd le fil d'un entretien",
       p:"Presque jamais sur un mot inconnu. Presque toujours sur un mot de deux lettres. « Je le sais », « j'y pense », « il en parle » : chacun renvoie à quelque chose dit trente secondes plus tôt. Ces mots sont courts, ils ne sont jamais accentués, et personne ne les répète. Si vous ne savez pas à quoi ils renvoient, la phrase devient vide — et vous continuez d'écouter en croyant comprendre.",
       note:"Le programme appelle cela la <b>reprise de l'information</b>. C'est le cœur de la grammaire du texte au niveau 6."},

      {t:'ana', h:"« le » remplace une idée entière",
       p:"Pas un objet : toute une phrase déjà dite.",
       mots:[['La phrase de départ','Je sais <u>que le test ne donne pas de diplôme</u>.'],
             ["Ce qu'on dit",'Je <b>le</b> sais.', true],
             ['Ce qui ne change jamais',"ce « le » ne s'accorde pas : ni « la », ni « les »"],
             ["Les verbes qui l'appellent",'savoir, dire, croire, ignorer, expliquer, répéter, comprendre']],
       say:"Je le sais. Il le dit. Elle l'a expliqué deux fois.",
       note:"C'est le plus difficile des trois, parce qu'on cherche un objet et qu'il n'y en a pas."},

      {t:'ana', h:"« en » remplace « de + chose »",
       p:"La préposition « de » disparaît, et le mot passe devant le verbe.",
       mots:[['La phrase de départ','Il parle <u>des préalables particuliers</u>.'],
             ["Ce qu'on dit",'Il <b>en</b> parle.', true],
             ['Aussi pour la quantité',"J'ai <u>trois relevés</u>. → J'<b>en</b> ai trois."],
             ['Mais pas pour une personne','Il parle <u>de sa conseillère</u>. → Il parle <b>d\'elle</b>.']],
       say:"Il en parle. J'en ai trois. J'en ai besoin avant février.",
       note:"Les verbes en « de » qui reviennent ici : parler de, avoir besoin de, s'occuper de, se souvenir de, dépendre de."},

      {t:'ana', h:"« y » remplace « à + chose », ou un lieu",
       p:"Même mécanique, avec la préposition « à » ou avec un endroit.",
       mots:[['Une chose','Je pense <u>à ma demande</u>. → J\'<b>y</b> pense.'],
             ['Un lieu','Elle va <u>au secrétariat</u>. → Elle <b>y</b> va.', true],
             ['Mais pas pour une personne','Je pense <u>à ma fille</u>. → Je pense <b>à elle</b>.'],
             ['Une expression à connaître',"Il <b>y</b> a — ce « y »-là ne remplace plus rien"]],
       say:"J'y pense. Elle y va. On y trouve aussi les dates.",
       note:"« On y trouve les dates » : le « y », c'est l'encadré gris. C'est la phrase exacte du dialogue."},

      {t:'labo', h:"Écoutez la phrase longue, puis la courte",
       p:"Choisissez le pronom et l'exemple.",
       axes:[
         {id:'p', lbl:'Quel pronom ?', opts:[['a','le'],['b','en'],['c','y']]},
         {id:'n', lbl:'Quel exemple ?', opts:[['1','le premier'],['2','le second']]}],
       out:{
         a1:{w:["Je le sais."], say:"Je sais que le test ne donne pas de diplôme. Je le sais.", n:'« le » remplace toute la phrase soulignée'},
         a2:{w:["Il l'a répété."], say:"Il a répété que ce n'est pas une équivalence. Il l'a répété.", n:"devant une voyelle, « le » devient « l\'​ »"},
         b1:{w:["Il en parle."], say:"Il parle des préalables particuliers. Il en parle.", n:'« en » remplace « des préalables »'},
         b2:{w:["J'en ai besoin."], say:"J'ai besoin d'un relevé de notes. J'en ai besoin.", n:'avoir besoin de : donc « en »'},
         c1:{w:["J'y pense."], say:"Je pense à ma demande d'admission. J'y pense.", n:'penser à une chose : donc « y »'},
         c2:{w:["Elle y va."], say:"Elle va au secrétariat du pavillon B. Elle y va.", n:'un lieu : donc « y »'},
       },
       note:"Écoutez d'abord la longue, puis la courte. C'est ce chemin-là que fait l'oreille pendant un entretien."},

      {t:'piege', h:"Trois pièges",
       rows:[
         ["accorder le « le » d'idée","le laisser invariable",
          "« Elle sait que c'est vrai. → Elle la sait. » ❌ Ce « le » ne désigne rien de féminin : il désigne une phrase. On dit « Elle le sait »."],
         ["employer « en » ou « y » pour une personne","garder la préposition",
          "« Je pense à ma fille. → J'y pense. » ❌ Pour une personne, on dit « Je pense à elle ». Même chose pour « de » : « Je parle de lui »."],
         ["placer le pronom après le verbe","le placer devant",
          "« Je sais le. » ❌ Ces pronoms passent toujours devant le verbe conjugué — ou devant l'infinitif s'il y a deux verbes : « Je vais en parler »."],
       ]},

      {t:'check', h:"Est-ce que c'est clair maintenant ?",
       p:"Quatre questions rapides.",
       qs:[
         {q:"« Il le savait » — le « le » remplace…", opts:["un objet","une phrase entière"], ok:1,
          fb:"C'est le « le » d'idée : il remplace une subordonnée complétive."},
         {q:"« Il parle des préalables » devient…", opts:["Il en parle","Il y parle"], ok:0,
          fb:"La préposition est « de » : donc « en »."},
         {q:"« Je pense à ma demande » devient…", opts:["J'en pense","J'y pense"], ok:1,
          fb:"La préposition est « à » et c'est une chose : donc « y »."},
         {q:"« Je pense à ma fille » devient…", opts:["J'y pense","Je pense à elle"], ok:1,
          fb:"Pour une personne, on garde la préposition et on met un pronom fort."},
       ]},

      {t:'revoir', h:"À retenir",
       p:"Trois petits mots, trois questions. <b>le</b> = une idée déjà dite. <b>en</b> = « de + chose ». <b>y</b> = « à + chose » ou un lieu. Quand vous en entendez un, reculez d'une phrase : la réponse est juste avant."},
    ]
  },

  t1celui: {
    eye:'Mini-leçon', tit:"Celui, celle, ceux, celles — et ce qui suit",
    blocs:[
      {t:'texte', h:"Désigner sans répéter",
       p:"« Il y a trois voies d'admission. La voie qui vous concerne demande le test. » On peut dire cela, mais on ne le dit pas : on dit « Celle qui vous concerne ». Le pronom démonstratif reprend un nom déjà posé et lui accroche aussitôt une petite phrase qui le distingue des autres. Sans lui, un entretien d'orientation deviendrait insupportable de répétitions.",
       note:"Le programme du niveau 6 nomme la structure : <b>pronom démonstratif + subordonnée relative</b>."},

      {t:'ana', h:"Les quatre formes, et d'où vient leur genre",
       p:"Le genre et le nombre viennent du nom qu'on ne répète pas.",
       mots:[['un masculin','<b>celui</b> — le papier → <b>celui</b> que je crains'],
             ['un féminin','<b>celle</b> — la voie → <b>celle</b> qui vous concerne', true],
             ['des masculins','<b>ceux</b> — les documents → <b>ceux</b> qui portent un sceau'],
             ['des féminins','<b>celles</b> — les preuves → <b>celles</b> qui comptent']],
       say:"celui que je crains, celle qui vous concerne, ceux qui portent un sceau, celles qui comptent",
       note:"Si vous hésitez, remettez le nom : « la voie qui vous concerne ». Le genre saute aux yeux."},

      {t:'ana', h:"Il ne reste jamais seul",
       p:"Il appelle toujours une suite. Quatre suites possibles.",
       mots:[['avec qui','celui <b>qui</b> arrive — le verbe qui suit n\'a pas de sujet'],
             ['avec que','celui <b>que</b> j\'attends — il manque un complément direct', true],
             ['avec où','celle <b>où</b> la rencontre a lieu — un lieu ou un moment'],
             ['avec dont','celle <b>dont</b> personne ne se rappelle — le verbe se construit avec « de »']],
       say:"celui qui arrive, celui que j'attends, celle où la rencontre a lieu, celle dont personne ne se rappelle",
       note:"Le test qui tranche entre « qui » et « que » : enlevez le pronom et remettez la phrase droite. Verbe sans sujet, c'est « qui » ; verbe sans objet, c'est « que »."},

      {t:'labo', h:"Écoutez les quatre suites",
       p:"Choisissez la forme et l'exemple.",
       axes:[
         {id:'f', lbl:'Quelle forme ?', opts:[['a','celui'],['b','celle'],['c','ceux / celles']]},
         {id:'n', lbl:'Quel exemple ?', opts:[['1','le premier'],['2','le second']]}],
       out:{
         a1:{w:["celui que je crains"], say:"Deux papiers sont arrivés. Celui que je crains, c'est l'avis d'une page.", n:'un papier, complément direct manquant'},
         a2:{w:["celui où la rencontre a lieu"], say:"Deux locaux portent le numéro 118. Celui où la rencontre a lieu est au fond.", n:'un local, donc un lieu'},
         b1:{w:["celle qui vous concerne"], say:"Il y a trois voies. Celle qui vous concerne demande le test.", n:'une voie, sujet manquant'},
         b2:{w:["celle dont personne ne se rappelle"], say:"De toutes les dates, celle dont personne ne se rappelle est la bonne.", n:'se rappeler de : donc « dont »'},
         c1:{w:["ceux qui portent un sceau"], say:"Parmi tous ses documents, elle garde ceux qui portent un sceau.", n:'des documents, masculin pluriel'},
         c2:{w:["celles qui ne comptent pas"], say:"Il y a des preuves qui comptent et celles qui ne comptent pas.", n:'des preuves, féminin pluriel'},
       },
       note:"Chaque exemple sort du dossier de Bintou : ce sont des phrases que vous entendrez telles quelles."},

      {t:'piege', h:"Deux pièges",
       rows:[
         ["confondre « celui que » et « ce que »","regarder s'il y a un nom avant",
          "« Ce que je dois faire » — il n'y a aucun nom, c'est une chose sans nom. « Celui que je dois remplir » — le formulaire a été nommé avant. Un nom avant : celui. Pas de nom : ce."],
         ["laisser le pronom tout seul","toujours lui donner une suite",
          "« Prends celui. » ❌ En français, il faut « celui-ci », « celui-là », « celui de Bintou » ou « celui qui… ». Seul, le pronom démonstratif n'existe pas."],
       ]},

      {t:'check', h:"Est-ce que c'est clair maintenant ?",
       p:"Trois questions rapides.",
       qs:[
         {q:"« Il y a trois voies. ___ qui vous concerne… »", opts:["Celui","Celle"], ok:1,
          fb:"Une voie est féminin : celle."},
         {q:"« Je ne sais pas ___ je dois faire. »", opts:["ce que","celui que"], ok:0,
          fb:"Aucun nom n'a été posé avant : c'est « ce que »."},
         {q:"« Deux locaux portent le même numéro. ___ où la rencontre a lieu… »", opts:["Celui","Celle"], ok:0,
          fb:"Un local est masculin : celui."},
       ]},

      {t:'revoir', h:"À retenir",
       p:"<b>celui · celle · ceux · celles</b>, jamais seuls, toujours suivis de <b>qui</b>, <b>que</b>, <b>où</b>, <b>dont</b> ou de « de… ». Le genre vient du nom qu'on ne répète pas."},
    ]
  },

  t1indir: {
    eye:'Mini-leçon', tit:"La question qui entre dans une phrase",
    blocs:[
      {t:'texte', h:"Pourquoi on ne pose pas toujours sa question directement",
       p:"Devant quelqu'un qu'on ne connaît pas, une question directe peut sonner sec : « Est-ce que ça compte ? » La même question, glissée dans une phrase — « Je me demande si ça compte » — devient une remarque, et elle se relie à ce qu'on vient de dire. C'est ainsi que parlent les adultes dans un bureau, et c'est ce qui fait qu'un entretien avance au lieu de ressembler à un questionnaire.",
       note:"Le programme du niveau 6 demande deux choses ici : l'interrogation indirecte, et la subordonnée infinitive interrogative avec mot interrogatif."},

      {t:'ana', h:"Trois choses disparaissent",
       p:"La question se range, et elle perd trois signes.",
       mots:[["Le point d'interrogation",'Où est-ce que je dépose ça <b>?</b> → …où je dépose ça<b>.</b>'],
             ["L'inversion du sujet",'Quand a-t-il lieu ? → …quand il a lieu.', true],
             ['« est-ce que »','Où est-ce que je dépose ? → …où je dépose.']],
       say:"Je voudrais savoir où je dépose mes papiers.",
       note:"Écrire « je voudrais savoir où est-ce que je dépose » est la faute la plus fréquente, à tous les niveaux."},

      {t:'ana', h:"Les deux transformations à retenir",
       p:"Deux formules deviennent deux autres formules, et c'est tout.",
       mots:[['« est-ce que » devient « si »','Est-ce que ça compte ? → Je me demande <b>si</b> ça compte.'],
             ['devant « il », « si » se colle','Est-ce qu\'il faut un rendez-vous ? → Il demande <b>s\'il</b> faut un rendez-vous.', true],
             ['« qu\'est-ce que » devient « ce que »','Qu\'est-ce que je fais ? → Je ne sais pas <b>ce que</b> je fais.'],
             ['« qu\'est-ce qui » devient « ce qui »','Qu\'est-ce qui manque ? → J\'aimerais savoir <b>ce qui</b> manque.']],
       say:"Je me demande si ça compte. Je ne sais pas ce que je dois faire.",
       note:"Les autres mots interrogatifs — où, quand, comment, pourquoi, combien — ne changent pas du tout."},

      {t:'ana', h:"Avec un infinitif, c'est encore plus court",
       p:"Quand le sujet est le même des deux côtés, on garde le mot interrogatif et on met l'infinitif.",
       mots:[['comment','Je ne sais pas <b>comment</b> m\'inscrire.'],
             ['quoi','Je ne sais pas <b>quoi</b> faire de mes six ans.', true],
             ['où','Je ne sais pas <b>où</b> déposer mes papiers.'],
             ['à qui','Je ne sais pas <b>à qui</b> m\'adresser.']],
       say:"Je ne sais pas comment m'inscrire. Je ne sais pas quoi faire de mes six ans.",
       note:"Attention : ici c'est <b>quoi</b>, jamais « que ». « Je ne sais pas que faire » existe à l'écrit soutenu, mais personne ne le dit."},

      {t:'labo', h:"Écoutez la question, puis sa forme rangée",
       p:"Choisissez le mot et l'exemple.",
       axes:[
         {id:'m', lbl:'Quel mot ?', opts:[['a','si'],['b','ce que / ce qui'],['c','avec un infinitif']]},
         {id:'n', lbl:'Quel exemple ?', opts:[['1','le premier'],['2','le second']]}],
       out:{
         a1:{w:["Je me demande si ça compte."], say:"Est-ce que ça compte ? Je me demande si ça compte.", n:'« est-ce que » devient « si »'},
         a2:{w:["Il demande s'il faut un rendez-vous."], say:"Est-ce qu'il faut un rendez-vous ? Il demande s'il faut un rendez-vous.", n:'devant « il », si se colle'},
         b1:{w:["Je ne sais pas ce que je dois faire."], say:"Qu'est-ce que je dois faire ? Je ne sais pas ce que je dois faire.", n:'« qu\'est-ce que » devient « ce que »'},
         b2:{w:["J'aimerais savoir ce qui manque."], say:"Qu'est-ce qui manque à mon dossier ? J'aimerais savoir ce qui manque à mon dossier.", n:'« qu\'est-ce qui » devient « ce qui »'},
         c1:{w:["Je ne sais pas comment m'inscrire."], say:"Comment est-ce que je m'inscris ? Je ne sais pas comment m'inscrire.", n:'même sujet des deux côtés : infinitif'},
         c2:{w:["Je ne sais pas quoi faire."], say:"Que faire de mes six ans de pharmacie ? Je ne sais pas quoi faire de mes six ans.", n:'c\'est « quoi », jamais « que »'},
       },
       note:"Ces huit phrases suffisent pour tout un rendez-vous. Apprenez-les comme des formules."},

      {t:'ex', h:"Six phrases toutes faites, pour un bureau",
       p:"À gauche ce que vous dites, à droite ce que ça fait.",
       rows:[
         ["Je me demande si mes années comptent.","poser une question sans avoir l'air d'exiger une réponse"],
         ["Je voudrais savoir où je dépose mes papiers.","demander une information précise, poliment"],
         ["Je ne sais pas ce que je dois faire.","dire qu'on est perdu, sans se plaindre"],
         ["J'aimerais savoir ce qui manque à mon dossier.","obtenir une liste plutôt qu'un avis"],
         ["Pouvez-vous me dire quand le test a lieu ?","demander une date, en laissant l'autre chercher"],
         ["Je ne sais pas comment m'inscrire.","ouvrir la porte à une explication complète"],
       ]},

      {t:'piege', h:"Deux pièges",
       rows:[
         ["garder « est-ce que » dans la phrase","le remplacer par « si »",
          "« Je voudrais savoir est-ce que ça compte. » ❌ On dit « Je voudrais savoir si ça compte ». « Est-ce que » ne survit jamais à l'entrée dans une phrase."],
         ["écrire « si il »","écrire « s'il »",
          "Devant « il » et « ils », « si » se colle : <b>s'il</b>, <b>s'ils</b>. Mais devant « elle », il ne change pas : « si elle »."],
       ]},

      {t:'revoir', h:"À retenir",
       p:"La question entre dans la phrase et perd trois choses : le point d'interrogation, l'inversion, « est-ce que ». <b>est-ce que → si</b> (et <b>s'il</b> devant « il »). <b>qu'est-ce que → ce que</b>. <b>qu'est-ce qui → ce qui</b>. Même sujet des deux côtés : mot interrogatif + infinitif."},
    ]
  },

  t2avis: {
    eye:'Mini-leçon', tit:"Lire un avis officiel en trois minutes",
    blocs:[
      {t:'texte', h:"Une page, et tout le monde la lit mal",
       p:"Un avis officiel tient sur une page et se lit en trois minutes — à condition de savoir où regarder. Le piège n'est pas le vocabulaire : c'est l'ordre. Ces lettres commencent par des politesses et par ce qui est déjà arrivé, et elles gardent pour le milieu ce qui vous oblige. Beaucoup de gens lisent la première ligne, comprennent qu'ils sont acceptés, et referment la feuille sans avoir vu la condition.",
       note:"Le programme du niveau 6 demande de « lire un avis ou un document scolaire officiel ». C'est une compétence de lecture, pas de vocabulaire."},

      {t:'ana', h:"Cinq endroits, dans cet ordre",
       p:"Regardez-les avant même de lire les phrases.",
       mots:[["L'en-tête","quel établissement parle — et il ne parle que pour lui"],
             ["La ligne en gras",'le genre du document : <b>Avis d\'admission conditionnelle</b>', true],
             ["L'encadré",'la condition ou la date : ce qui est entouré est ce qui oblige'],
             ['Les deux dates',"celle de l'envoi, en haut ; celle qui vous oblige, plus bas"],
             ['La dernière ligne','à qui vous adresser, et à quel poste téléphonique']],
       say:"un avis d'admission conditionnelle, la date limite, le numéro de dossier",
       note:"Le numéro de dossier, en petits caractères, est ce qu'on vous demandera au téléphone. Notez-le avant d'appeler."},

      {t:'ana', h:"« Conditionnelle » : ce que ça veut dire exactement",
       p:"Ni un oui, ni un non. Une place gardée, sous surveillance.",
       mots:[['Ce que le centre fait','il vous réserve une place dans un groupe précis'],
             ['Ce qu\'il ne fait pas','il ne vous admet pas encore, et il ne vous refuse pas', true],
             ['Ce qui décide','une condition écrite, remplie avant une date écrite'],
             ['Ce qui arrive sinon','la place est libérée et offerte à la personne suivante']],
       say:"Une admission conditionnelle réserve la place, elle ne la donne pas.",
       note:"« Je suis acceptée mais pas vraiment » est une lecture inquiète et fausse. La bonne lecture : la place est à vous jusqu'à la date, et personne d'autre ne peut la prendre d'ici là."},

      {t:'ex', h:"Six formules d'avis, et ce qu'elles veulent dire",
       p:"À gauche ce qui est écrit, à droite ce que ça vous demande.",
       rows:[
         ["La candidate fournira la preuve de sa réussite.","Fournissez-la. Ce futur est un ordre poli."],
         ["Les documents se déposent au secrétariat.","C'est vous qui les déposez. Personne n'est nommé."],
         ["Une place vous est réservée sous condition.","Elle est à vous, tant que la condition tient."],
         ["Aucun délai supplémentaire n'est accordé.","La date ne se négocie pas, même en expliquant bien."],
         ["Le cas échéant, la place sera libérée.","Si la condition n'est pas remplie, vous la perdez."],
         ["Veuillez agréer l'expression de nos salutations.","Rien du tout. C'est la formule de fin, elle n'oblige à rien."],
       ]},

      {t:'piege', h:"Trois pièges",
       rows:[
         ["lire le début et refermer","lire jusqu'à la date",
          "La bonne nouvelle est en haut, l'obligation est au milieu. Un avis se lit en entier, la première fois comme les suivantes."],
         ["croire qu'un avis se discute au comptoir","répondre par écrit",
          "L'agent de bureau à l'accueil n'a pas le pouvoir de changer une ligne d'un avis, et il ne l'aura jamais. La personne qui peut est nommée dans la dernière ligne."],
         ["noter la date de l'envoi","noter la date qui oblige",
          "Il y a toujours deux dates. Celle du haut est passée le jour où vous lisez ; celle du milieu est celle à écrire dans votre calendrier."],
       ]},

      {t:'check', h:"Est-ce que c'est clair maintenant ?",
       p:"Trois questions rapides.",
       qs:[
         {q:"« Une admission conditionnelle », ça veut dire…", opts:["vous êtes refusé pour l'instant","la place est gardée si une condition est remplie"], ok:1,
          fb:"La place est bien à vous, jusqu'à la date écrite."},
         {q:"« Les documents se déposent au secrétariat » — qui les dépose ?", opts:["vous","le secrétariat"], ok:0,
          fb:"Personne n'est nommé, mais neuf fois sur dix, c'est vous."},
         {q:"Sur un avis, ce qui est entouré d'un trait, c'est…", opts:["une décoration","ce qu'il ne faut surtout pas manquer"], ok:1,
          fb:"L'encadré porte la condition, la date ou le montant."},
       ]},

      {t:'revoir', h:"À retenir",
       p:"Cinq endroits : l'<b>en-tête</b>, la <b>ligne en gras</b>, l'<b>encadré</b>, les <b>deux dates</b>, la <b>dernière ligne</b>. Et une phrase à retenir : une admission conditionnelle réserve la place, elle ne la donne pas."},
    ]
  },

  t2ps: {
    eye:'Mini-leçon', tit:"Le passé simple : à reconnaître, jamais à écrire",
    blocs:[
      {t:'texte', h:"Le temps que personne ne parle",
       p:"« Le centre ouvrit ses portes en 1968. » Personne ne dit cela à voix haute, et pourtant vous le lirez sur la première page de presque toutes les brochures d'établissement. C'est le temps des livres et des historiques. Il n'apporte aucune information que vous devez retenir : il apporte le décor. Le savoir traduire en une seconde, et continuer à lire — c'est tout ce qu'on vous demande.",
       note:"Le programme du niveau 6 est très clair : <b>reconnaître</b> les verbes courants à la 3e personne, et <b>associer</b> le passé simple au passé composé. Rien de plus."},

      {t:'ana', h:"Les terminaisons à repérer",
       p:"Trois familles, et vous les reconnaîtrez toutes.",
       mots:[['Les verbes en -er','il ferm<b>a</b> · ils ferm<b>èrent</b>'],
             ['Les verbes en -ir et beaucoup d\'autres','il ouvr<b>it</b> · ils ouvr<b>irent</b>', true],
             ['Une troisième famille','il reç<b>ut</b> · ils reç<b>urent</b>']],
       say:"il ferma, ils fermèrent, il ouvrit, ils ouvrirent, il reçut, ils reçurent",
       note:"Vous ne rencontrerez presque jamais autre chose que la 3e personne : un historique parle de gens absents."},

      {t:'ana', h:"Les trois qui reviennent partout",
       p:"Apprenez ces trois-là, et vous comprendrez la moitié des historiques.",
       mots:[['être','il <b>fut</b> — il a été'],
             ['avoir','il <b>eut</b> — il a eu', true],
             ['faire','il <b>fit</b> — il a fait'],
             ['devenir','il <b>devint</b> — il est devenu']],
       say:"il fut, il eut, il fit, il devint",
       note:"« Ce fut le premier du genre » se lit « ça a été le premier du genre ». C'est exactement la même chose, dans un autre habit."},

      {t:'ex', h:"Sept formes, et ce qu'on dirait à voix haute",
       p:"À gauche la brochure, à droite la conversation.",
       rows:[
         ["Le centre ouvrit ses portes en 1968.","Le centre a ouvert ses portes en 1968."],
         ["Les commissaires décidèrent d'agrandir.","Les commissaires ont décidé d'agrandir."],
         ["L'école devint un centre d'éducation des adultes.","L'école est devenue un centre d'éducation des adultes."],
         ["Le pavillon reçut ses premiers élèves.","Le pavillon a reçu ses premiers élèves."],
         ["Les travaux durèrent deux ans.","Les travaux ont duré deux ans."],
         ["On y fit une bibliothèque.","On y a fait une bibliothèque."],
         ["Ce fut le premier du genre dans la région.","Ça a été le premier du genre dans la région."],
       ]},

      {t:'piege', h:"Deux pièges",
       rows:[
         ["essayer d'en écrire un","le laisser aux livres",
          "Un passé simple dans un courriel au secrétariat serait déplacé, et souvent faux. Écrivez au passé composé : c'est ce que tout le monde fait, y compris les gens qui écrivent les brochures."],
         ["confondre « il fut » et « il fait »","les distinguer à l'oreille",
          "« Il fut » vient de être, « il fait » vient de faire. Un seul son les sépare, et ils n'ont rien en commun. Dans un historique, « fut » est bien plus fréquent."],
       ]},

      {t:'revoir', h:"À retenir",
       p:"Trois terminaisons : <b>-a / -èrent</b>, <b>-it / -irent</b>, <b>-ut / -urent</b>. Trois verbes à savoir : <b>il fut</b>, <b>il eut</b>, <b>il fit</b>. Une seule chose à faire : traduire en passé composé dans sa tête et continuer à lire."},
    ]
  },

  t2passif: {
    eye:'Mini-leçon', tit:"« Ça se dépose » — mais par qui ?",
    blocs:[
      {t:'texte', h:"La phrase qui ne nomme personne",
       p:"« Les documents se déposent au secrétariat. » Les documents ne se déposent pas tout seuls : quelqu'un les dépose. Ce quelqu'un, c'est vous — mais la phrase ne le dit pas. L'administration écrit ainsi parce qu'elle décrit une règle valable pour tout le monde, pas le geste d'une personne. C'est logique de son côté ; du vôtre, ça produit des feuilles qui restent dans une enveloppe parce que personne ne s'est senti visé.",
       note:"Le programme du niveau 6 appelle cela « comprendre un verbe pronominal à sens passif »."},

      {t:'ana', h:"Comment on le reconnaît",
       p:"Un « se » qui ne veut pas dire « soi-même ».",
       mots:[['La forme','<b>se</b> + le verbe au présent, 3e personne'],
             ["L'accord",'avec ce qui subit l\'action : la demande <b>se dépose</b> · les demandes <b>se déposent</b>', true],
             ["Devant une voyelle",'« se » devient « s\'​ » : ce papier <b>s\'obtient</b> au comptoir'],
             ['Le sens',"personne n'est nommé, mais quelqu'un agit"]],
       say:"Les demandes se déposent au secrétariat. Ce papier s'obtient au comptoir.",
       note:"Le verbe s'accorde avec la chose, pas avec vous : « les places se prennent vite », même si c'est vous qui les prenez."},

      {t:'ana', h:"La question à se poser chaque fois",
       p:"Une seule question, et elle a presque toujours la même réponse.",
       mots:[['La phrase','Le formulaire se remplit en ligne.'],
             ['La question','Par qui ?', true],
             ['La réponse','Par vous. Dans neuf phrases sur dix, la réponse est : par vous.'],
             ["L'exception",'Quand c'+"'"+'est l\'établissement : « les résultats s\'envoient par la poste ».']],
       say:"Le formulaire se remplit en ligne. Par qui ? Par vous.",
       note:"Prenez l'habitude de dire la phrase à voix basse en vous nommant : « je dépose », « je remplis ». Elle devient tout de suite claire."},

      {t:'ex', h:"Six phrases de documents officiels",
       p:"À gauche ce qui est écrit, à droite ce que ça veut dire pour vous.",
       rows:[
         ["Les demandes se déposent au secrétariat.","Vous devez les apporter là, en personne."],
         ["Le formulaire se remplit en ligne.","Vous le remplissez vous-même, sur un ordinateur."],
         ["Ce papier s'obtient au comptoir.","Vous devez aller le demander ; il n'arrivera pas seul."],
         ["Les résultats s'envoient par la poste.","Là, c'est le centre qui agit. Vous attendez."],
         ["Le test se donne deux fois par année.","Le centre l'organise. À vous de choisir la séance."],
         ["Les places se prennent vite.","Personne n'agit dans cette phrase, sauf les autres candidats."],
       ]},

      {t:'piege', h:"Deux pièges",
       rows:[
         ["croire que ça se fera tout seul","se demander par qui",
          "« Le dossier se complète au fur et à mesure. » Personne ne le complétera à votre place. Cette phrase veut dire : complétez-le."],
         ["confondre avec le vrai « se »","regarder le sens du verbe",
          "« Elle se lave » — là, « se » veut bien dire elle-même. « Ce papier se demande au comptoir » — là, non. C'est le sens, jamais la forme, qui tranche."],
       ]},

      {t:'check', h:"Est-ce que c'est clair maintenant ?",
       p:"Trois questions rapides.",
       qs:[
         {q:"« Les demandes se déposent au secrétariat » — qui dépose ?", opts:["le secrétariat","vous"], ok:1,
          fb:"Personne n'est nommé, mais c'est vous qui les apportez."},
         {q:"« Ce papier ___ au comptoir. » (obtenir)", opts:["se obtient","s'obtient"], ok:1,
          fb:"Devant une voyelle, « se » devient « s' »."},
         {q:"« Les places ___ vite. » (prendre)", opts:["se prend","se prennent"], ok:1,
          fb:"Le verbe s'accorde avec « les places »."},
       ]},

      {t:'revoir', h:"À retenir",
       p:"<b>se</b> + verbe au présent, accordé avec la chose. Une seule question à poser : <b>par qui ?</b> Et une réponse presque toujours vraie : par vous."},
    ]
  },

  t2futur: {
    eye:'Mini-leçon', tit:"Le futur qui n'annonce pas l'avenir",
    blocs:[
      {t:'texte', h:"« La candidate fournira la preuve »",
       p:"Lue vite, cette phrase ressemble à une prédiction : on dirait que le centre suppose que vous le ferez. C'est l'inverse. Dans un document officiel, le futur simple est un ordre — un ordre poli, éloigné, qui évite de vous dire « faites ceci ». Le lire comme une possibilité, c'est manquer une obligation, et souvent une date.",
       note:"Le programme du niveau 6 le nomme sans détour : « employer des verbes au futur simple pour exprimer un impératif »."},

      {t:'ana', h:"Comment le reconnaître",
       p:"Trois indices, et ils sont toujours là ensemble.",
       mots:[["Aucun mot d'incertitude",'ni « peut-être », ni « probablement », ni « on verra »'],
             ['Un sujet à la 3e personne','<b>la candidate</b>, <b>le titulaire</b>, <b>le patient</b> — c\'est vous, nommé de loin', true],
             ['Un contexte de règle',"la phrase est dans un avis, une consigne, un règlement"]],
       say:"La candidate fournira la preuve de la réussite du test.",
       note:"Quand le sujet est « vous », c'est encore plus net : « Vous vous présenterez au local 118 » ne laisse aucun choix."},

      {t:'ana', h:"Comment on le forme",
       p:"L'infinitif, plus six terminaisons toujours les mêmes.",
       mots:[['Les terminaisons','-ai · -as · -a · -ons · -ez · -ont'],
             ['Sur un verbe régulier','déposer → vous dépos<b>erez</b> · fournir → elle fourn<b>ira</b>', true],
             ['Les irréguliers courants','être → il <b>sera</b> · avoir → il <b>aura</b> · faire → il <b>fera</b>'],
             ["Deux autres qu'on rencontre",'venir → il <b>viendra</b> · devoir → il <b>devra</b>']],
       say:"vous déposerez, elle fournira, il sera, il aura, il fera",
       note:"Pour les verbes en -re, on enlève le e final : prendre → vous prend<b>rez</b>."},

      {t:'labo', h:"L'ordre, et sa version officielle",
       p:"Choisissez le verbe et la personne.",
       axes:[
         {id:'v', lbl:'Quel verbe ?', opts:[['a','se présenter'],['b','fournir'],['c','être']]},
         {id:'p', lbl:'Quelle personne ?', opts:[['1','vous'],['2','la candidate']]}],
       out:{
         a1:{w:["Vous vous présenterez au local 118."], say:"Présentez-vous au local 118. Vous vous présenterez au local 118.", n:'même ordre, dit de loin'},
         a2:{w:["La candidate se présentera au local 118."], say:"La candidate se présentera au local 118.", n:'la 3e personne éloigne encore plus'},
         b1:{w:["Vous fournirez la preuve."], say:"Fournissez la preuve. Vous fournirez la preuve.", n:'l\'impératif devient un futur'},
         b2:{w:["La candidate fournira la preuve."], say:"La candidate fournira la preuve de la réussite du test.", n:'la phrase exacte de l\'avis'},
         c1:{w:["Vous serez à jeun."], say:"Soyez à jeun. Vous serez à jeun.", n:'être, irrégulier'},
         c2:{w:["Le patient sera à jeun."], say:"Le patient sera à jeun le matin de l'examen.", n:'la formule des hôpitaux'},
       },
       note:"Écoutez l'ordre, puis sa version officielle. C'est la même chose deux fois."},

      {t:'piege', h:"Deux pièges",
       rows:[
         ["lire ce futur comme une possibilité","le traduire à l'impératif",
          "« La candidate fournira la preuve. » ne veut pas dire « elle le fera sans doute ». Traduisez dans votre tête : « Fournissez la preuve. » Le sens apparaît d'un coup."],
         ["répondre au futur soi-même","écrire simplement",
          "Vous n'avez pas à imiter ce style. Dans votre courriel, écrivez « Je déposerai la preuve la semaine où je la recevrai » — un futur normal, pas un futur d'ordre."],
       ]},

      {t:'revoir', h:"À retenir",
       p:"Dans un document officiel, le futur simple <b>donne un ordre</b>. Traduisez-le à l'impératif : « Vous vous présenterez » = « Présentez-vous ». Formation : l'infinitif + <b>-ai, -as, -a, -ons, -ez, -ont</b>."},
    ]
  },

  t2mise: {
    eye:'Mini-leçon', tit:"La mise en page parle avant les phrases",
    blocs:[
      {t:'texte', h:"Un document se regarde avant de se lire",
       p:"Avant même la première phrase, une page officielle vous a déjà dit quatre choses : qui parle, de quoi il s'agit, à qui c'est adressé, et ce qui presse. Tout cela tient dans la disposition — un nom en haut à gauche, une ligne en gras, un trait autour d'un paragraphe, un blanc entre deux idées. Un lecteur pressé qui sait regarder comprend plus vite qu'un lecteur appliqué qui lit tout dans l'ordre.",
       note:"C'est un savoir de grammaire du texte, au même titre que les connecteurs : « tenir compte de la présentation matérielle et de la mise en page »."},

      {t:'ana', h:"Ce que dit la place d'un élément",
       p:"Chaque endroit d'une page a une fonction fixe, et elle ne change pas d'un établissement à l'autre.",
       mots:[['En haut à gauche',"le nom de l'expéditeur : quel établissement parle"],
             ['Sous l\'en-tête, en gras','le genre du document — la clé de tout le reste', true],
             ['En petits caractères','le numéro de dossier, celui du téléphone'],
             ['Dans un encadré','ce qu\'il ne faut surtout pas manquer'],
             ['Avant la signature',"la personne à qui s'adresser"]],
       say:"un en-tête, une ligne en gras, un numéro de dossier, un encadré, une signature",
       note:"Un document sans encadré demande plus d'attention : la condition y est cachée dans le corps du texte."},

      {t:'ana', h:"Le paragraphe, et pourquoi il y a du blanc",
       p:"Le blanc entre deux paragraphes n'est pas de la décoration : c'est un changement d'idée.",
       mots:[['La règle',"un paragraphe = une idée principale"],
             ['Ce que ça vous permet','lire la première phrase de chaque paragraphe, et savoir déjà de quoi il parle', true],
             ["Ce qu'on attend de vous",'écrire pareil : deux ou trois paragraphes séparés, un par idée'],
             ["L'alinéa",'le petit retrait au début — courant sur papier, rare dans un courriel']],
       say:"Un paragraphe porte une idée principale, et une seule.",
       note:"Un courriel de dix phrases sans aucun blanc se lit deux fois plus lentement. Ce n'est pas une question de goût."},

      {t:'ex', h:"Six éléments et ce qu'ils vous apprennent",
       p:"À gauche l'endroit, à droite ce qu'il dit.",
       rows:[
         ["Le nom en haut à gauche","Quel établissement parle — jamais au nom d'un autre."],
         ["La ligne en gras sous l'en-tête","Le genre du document, donc son contenu."],
         ["La suite de chiffres en petit","Le numéro sans lequel un appel ne mène nulle part."],
         ["Le passage entouré d'un trait","La condition ou la date à ne pas manquer."],
         ["Le blanc entre deux paragraphes","Un changement d'idée : une idée par paragraphe."],
         ["La dernière ligne avant la signature","À qui s'adresser, et à quel poste."],
       ]},

      {t:'revoir', h:"À retenir",
       p:"Regardez avant de lire : <b>en-tête</b>, <b>ligne en gras</b>, <b>encadré</b>, <b>dates</b>, <b>dernière ligne</b>. Et écrivez comme on vous écrit : une idée par paragraphe, un blanc entre les deux."},
    ]
  },

  t3rapports: {
    eye:'Mini-leçon', tit:"Qui décide quoi, autour d'une table",
    blocs:[
      {t:'texte', h:"Quatre personnes parlent, une seule décide",
       p:"Dans une rencontre scolaire, tout le monde parle sur le même ton et avec les mêmes politesses. Rien, dans la voix, ne dit qui a le pouvoir. C'est dans les verbes que ça se voit : l'un dit « je propose », l'autre « j'exige », un troisième « je constate ». Confondre les trois, c'est repartir en croyant qu'une chose est réglée alors qu'elle a seulement été souhaitée.",
       note:"Le programme du niveau 6 demande de « saisir les rapports entre les interlocutrices ou les interlocuteurs ». C'est une compétence d'écoute, et elle ne s'exerce nulle part ailleurs."},

      {t:'ana', h:"Les verbes de celui qui explique",
       p:"Le conseiller d'orientation n'a aucun pouvoir de décision, et c'est très bien ainsi : il peut donc tout vous dire.",
       mots:[['Ce qu\'il dit','je vous explique · je vous propose · je vous suggère · voici les trois voies'],
             ['Ce que ça vaut',"une information juste, et un chemin — pas une place", true],
             ['Ce qu\'il ne dira jamais',"« Vous êtes admise. » Il n'en a pas le droit."]],
       say:"Je vous explique les trois voies. Je vous propose de commencer par le test.",
       note:"C'est la personne à qui poser toutes ses questions, y compris celles qui font peur : rien de ce que vous lui direz ne peut vous coûter une place."},

      {t:'ana', h:"Les verbes de celle qui décide",
       p:"La responsable de l'admission tient le calendrier. Ses phrases engagent l'établissement.",
       mots:[['Ce qu\'elle dit','je veux que · j\'exige que · aucun délai n\'est accordé · c\'est noté'],
             ['Ce que ça vaut','une règle qui s\'appliquera, même si elle vous déplaît', true],
             ['Comment lui parler','en posant des conditions claires, jamais en demandant une faveur']],
       say:"Aucun délai n'est accordé après le 6 février. C'est noté.",
       note:"Quand elle dit « c'est noté », quelque chose vient d'entrer dans un dossier. Ce sont les deux mots les plus importants d'une rencontre."},

      {t:'ana', h:"Les verbes de celui qui témoigne",
       p:"L'enseignant ne décide de rien, mais son avis pèse — parce qu'il vous voit trois fois par semaine.",
       mots:[['Ce qu\'il dit','je constate · je n\'ai aucune inquiétude · elle lit mieux que…'],
             ['Ce que ça vaut','un fait observé, qui appuie ou qui nuance', true],
             ['Pourquoi l\'amener','une heure d\'entretien ne remplace pas six mois d\'observation']],
       say:"Sur le français, je n'ai aucune inquiétude. Elle lit des textes officiels depuis septembre.",
       note:"« Si je peux me permettre » est sa formule d'entrée : il demande la parole parce qu'il n'est pas là pour trancher."},

      {t:'ex', h:"Six phrases, et ce qu'elles engagent vraiment",
       p:"À gauche ce qui se dit, à droite ce que ça vaut.",
       rows:[
         ["Je vous propose de commencer par le test.","Un conseil. Rien n'est réservé pour autant."],
         ["Aucun délai n'est accordé après cette date.","Une règle. Elle s'appliquera telle quelle."],
         ["Sur le français, je n'ai aucune inquiétude.","Un témoignage. Il appuie, il ne décide pas."],
         ["C'est noté.","Quelque chose vient d'entrer au dossier."],
         ["J'aimerais que vous visitiez le laboratoire.","Un souhait. Vous pouvez proposer une autre date."],
         ["Je le déposerai la semaine où je le reçois.","Un engagement — le vôtre. Tenez-le."],
       ]},

      {t:'revoir', h:"À retenir",
       p:"Trois familles de verbes : <b>j'explique, je propose</b> (celui qui informe) · <b>j'exige, c'est noté</b> (celle qui décide) · <b>je constate</b> (celui qui témoigne). Écoutez le verbe, pas le ton."},
    ]
  },

  t3tour: {
    eye:'Mini-leçon', tit:"Prendre la parole sans couper personne",
    blocs:[
      {t:'texte', h:"Le problème n'est pas la timidité",
       p:"Beaucoup d'adultes sortent d'une rencontre sans avoir dit ce qu'ils voulaient dire. Ce n'est presque jamais un manque de courage : c'est qu'on ne sait pas où entrer. Une conversation à quatre ne laisse pas de silence — il faut donc entrer <b>pendant</b> qu'on parle, et il existe pour cela quatre ou cinq formules toutes faites que tout le monde connaît et que personne ne refuse.",
       note:"Le programme du niveau 6 le nomme : « s'introduire dans une discussion et y participer », « respecter les conventions de la communication »."},

      {t:'ana', h:"Le moment, et non le volume",
       p:"On n'entre pas dans une discussion en parlant plus fort.",
       mots:[['Le bon moment','à la fin d\'une phrase, quand la voix descend'],
             ['Le signal','un souffle, un « donc », un « bon » — la personne cherche sa suite', true],
             ['Le mauvais moment','au milieu d\'une phrase : l\'autre reprendra et vous perdrez le tour']],
       say:"Si je peux me permettre. Juste une chose. J'ajoute quelque chose.",
       note:"Écoutez la fin des phrases plutôt que leur début. C'est là que la place s'ouvre."},

      {t:'ana', h:"Les cinq formules qui ouvrent",
       p:"Elles s'apprennent une fois et servent toute une vie.",
       mots:[['Pour demander la parole','Si je peux me permettre… · Juste une chose…'],
             ['Pour compléter ce qu\'on a dit soi-même','J\'ajoute une chose.', true],
             ['Pour poser une question','Est-ce que je peux poser une question ?'],
             ['Pour vérifier','Si je comprends bien, …'],
             ['Pour ramener au sujet','Revenons à l\'essentiel.']],
       say:"Si je peux me permettre. Est-ce que je peux poser une question ? Si je comprends bien.",
       note:"« Si je comprends bien » est la plus utile de toutes : elle vous fait gagner du temps et elle force l'autre à répéter sans qu'il se sente interrompu."},

      {t:'ana', h:"Reprendre les mots d'un autre",
       p:"La façon la plus sûre d'obtenir la parole, et de la garder.",
       mots:[['La formule','Vous disiez tantôt que la place est réservée…'],
             ['Pourquoi ça marche','personne ne coupe quelqu\'un qui montre qu\'il écoutait', true],
             ['Ce que ça vous donne','le temps de préparer votre phrase pendant que vous citez'],
             ['La variante','Comme vous le disiez… · Vous parliez de…']],
       say:"Vous disiez tantôt que la place est réservée jusqu'au 6 février.",
       note:"C'est aussi un procédé de reprise de l'information : vous reprenez un référent, et le fil de la discussion tient."},

      {t:'ex', h:"Sept formules et ce qu'elles font",
       p:"À gauche ce que vous dites, à droite ce que ça produit.",
       rows:[
         ["Si je peux me permettre…","Vous prenez la parole sans couper celui qui parle."],
         ["J'ajoute une chose.","Vous complétez ce que vous venez de dire vous-même."],
         ["Si je comprends bien…","Vous vérifiez avant d'aller plus loin."],
         ["Est-ce que je peux poser une question ?","Vous demandez la parole pour interroger quelqu'un."],
         ["Vous disiez tantôt que…","Vous reprenez les mots d'un autre pour appuyer votre réponse."],
         ["Revenons à l'essentiel.","Vous ramenez la discussion au point qui compte encore."],
         ["C'est tout pour moi.","Vous rendez la parole en disant clairement que vous avez fini."],
       ]},

      {t:'piege', h:"Deux pièges",
       rows:[
         ["attendre qu'on vous donne la parole","la demander",
          "Dans une rencontre à quatre, personne ne pense à vous la donner. Ce n'est pas de l'impolitesse : chacun suit son idée. « Est-ce que je peux poser une question ? » suffit, et cela ne dérange personne."],
         ["s'excuser d'avoir une préférence","la dire simplement",
          "« Pour ma part, je préférerais y aller après le test. » Pas de « je m'excuse », pas de « c'est peut-être bête, mais ». Vous dites ce que vous voulez et pourquoi ; c'est tout ce qu'on attend de vous."],
       ]},

      {t:'revoir', h:"À retenir",
       p:"Entrez <b>à la fin d'une phrase</b>, jamais au milieu. Cinq formules suffisent : <b>Si je peux me permettre · J'ajoute une chose · Si je comprends bien · Est-ce que je peux poser une question ? · Vous disiez tantôt que…</b>"},
    ]
  },

  t3subj: {
    eye:'Mini-leçon', tit:"Ce que chacun veut qu'il arrive",
    blocs:[
      {t:'texte', h:"Le temps de ce qui n'est pas encore arrivé",
       p:"« Je veux que la preuve soit au dossier. » La preuve n'y est pas. « Il faut que quelqu'un envoie le compte rendu. » Personne ne l'a envoyé. Le subjonctif ne raconte jamais un fait : il dit ce que quelqu'un veut, exige, souhaite ou craint. Dans une rencontre, il vous avertit qu'on vient de passer du constat à la demande — et c'est exactement le moment où il faut écouter.",
       note:"Le programme du niveau 6 demande d'employer le subjonctif présent après quelques verbes introducteurs usuels suivis de « que »."},

      {t:'ana', h:"Ce sont les verbes qui déclenchent, pas le sens",
       p:"Une liste courte, et elle suffit pour toute une rencontre.",
       mots:[['La volonté','vouloir que · exiger que · demander que · préférer que'],
             ["L'obligation",'il faut que · il est nécessaire que', true],
             ['Le souhait','souhaiter que · aimer que · aimerait que'],
             ['La crainte','craindre que · avoir peur que']],
       say:"Elle veut que la preuve soit au dossier. Il faut que quelqu'un envoie le compte rendu.",
       note:"Retenez la liste, pas la règle : c'est la présence du verbe et du « que » qui décide, jamais votre impression."},

      {t:'ana', h:"Comment on le forme",
       p:"Une seule recette, et elle marche pour presque tous les verbes.",
       mots:[['On part de','la 3e personne du pluriel du présent : ils arriv<b>ent</b>'],
             ['On enlève','la terminaison -ent : arriv-', true],
             ['On ajoute','-e, -es, -e, -ions, -iez, -ent'],
             ['Ce que ça donne','que j\'arriv<b>e</b> · que tu arriv<b>es</b> · qu\'ils arriv<b>ent</b>']],
       say:"que j'arrive, que tu arrives, qu'il arrive, qu'ils arrivent",
       note:"Pour beaucoup de verbes, le subjonctif s'entend exactement comme le présent. Tant mieux : il n'y a rien à faire."},

      {t:'ana', h:"Les cinq irréguliers qu'il faut savoir",
       p:"Ceux-là ne suivent pas la recette, et ce sont ceux qui reviennent le plus.",
       mots:[['être','que je <b>sois</b> · qu\'il <b>soit</b>'],
             ['avoir','que j\'<b>aie</b> · qu\'il <b>ait</b>', true],
             ['aller','que j\'<b>aille</b> · qu\'il <b>aille</b>'],
             ['faire','que je <b>fasse</b> · qu\'il <b>fasse</b>'],
             ['savoir','que je <b>sache</b> · qu\'il <b>sache</b>']],
       say:"qu'il soit, qu'il ait, qu'il aille, qu'il fasse, qu'il sache",
       note:"Cinq formes. Apprises une fois, elles couvrent la moitié de ce que vous entendrez dans un bureau."},

      {t:'labo', h:"Écoutez la demande entière",
       p:"Choisissez le verbe introducteur et le verbe qui suit.",
       axes:[
         {id:'i', lbl:'Qui demande quoi ?', opts:[['a','elle veut que'],['b','il faut que'],['c','elle craint que']]},
         {id:'v', lbl:'Quel verbe ?', opts:[['1','être'],['2','faire']]}],
       out:{
         a1:{w:["Elle veut que la preuve soit au dossier."], say:"Elle veut que la preuve soit au dossier avant le 6 février.", n:'vouloir que + subjonctif de être'},
         a2:{w:["Elle veut qu'on fasse le compte rendu."], say:"Elle veut qu'on fasse le compte rendu tout de suite.", n:'vouloir que + subjonctif de faire'},
         b1:{w:["Il faut que tout soit prêt."], say:"Il faut que tout soit prêt avant la rencontre.", n:'il faut que + subjonctif de être'},
         b2:{w:["Il faut qu'elle fasse sa demande."], say:"Il faut qu'elle fasse sa demande cette semaine.", n:'il faut que + subjonctif de faire'},
         c1:{w:["Elle craint que ce soit trop court."], say:"Elle craint que ce soit trop court pour tout préparer.", n:'craindre que + subjonctif de être'},
         c2:{w:["Elle craint qu'il fasse tout à la dernière minute."], say:"Elle craint qu'il fasse tout à la dernière minute.", n:'craindre que + subjonctif de faire'},
       },
       note:"Écoutez la phrase entière : c'est le verbe du début qui commande la forme de la fin."},

      {t:'piege', h:"Deux pièges",
       rows:[
         ["mélanger « de » et « que »","regarder ce qui suit le verbe introducteur",
          "« Elle demande <b>que</b> vous déposiez la preuve » — subjonctif. « Elle demande <b>de</b> déposer la preuve » — infinitif. Les deux phrases sont justes ; ce qui est faux, c'est « elle demande de que vous déposiez »."],
         ["mettre un subjonctif après « espérer »","espérer se construit avec l'indicatif",
          "« J'espère qu'il soit là. » ❌ On dit « J'espère qu'il <b>sera</b> là ». Espérer est le seul verbe de souhait qui n'appelle pas le subjonctif, et c'est la faute la plus fréquente."],
       ]},

      {t:'check', h:"Est-ce que c'est clair maintenant ?",
       p:"Quatre questions rapides.",
       qs:[
         {q:"« Il faut que la preuve ___ au dossier. » (être)", opts:["est","soit"], ok:1,
          fb:"Après « il faut que », toujours le subjonctif : soit."},
         {q:"« Elle aimerait que la visite ___ lieu après. » (avoir)", opts:["ait","a"], ok:0,
          fb:"Aimer que appelle le subjonctif : qu'elle ait lieu."},
         {q:"« J'espère qu'il ___ là. » (être)", opts:["soit","sera"], ok:1,
          fb:"Espérer se construit avec l'indicatif : qu'il sera là."},
         {q:"« Elle demande ___ déposer la preuve. »", opts:["de","que"], ok:0,
          fb:"Avec « de », un infinitif. Avec « que », un subjonctif."},
       ]},

      {t:'revoir', h:"À retenir",
       p:"<b>vouloir · falloir · exiger · souhaiter · aimer · demander · craindre · préférer</b> + <b>que</b> → subjonctif. Cinq irréguliers : <b>sois · aie · aille · fasse · sache</b>. Et une exception : <b>espérer</b> prend l'indicatif."},
    ]
  },

  t3si: {
    eye:'Mini-leçon', tit:"Poser une condition avec « si »",
    blocs:[
      {t:'texte', h:"Dire non sans dire non",
       p:"« Si j'y vais avant, je vais y penser pendant l'épreuve. » Bintou ne refuse pas la visite du laboratoire : elle en déplace la date, elle dit pourquoi, et personne ne perd la face. C'est ce que permet l'hypothèse en « si » : poser une condition au lieu d'opposer un refus. Dans une rencontre où quatre personnes ont chacune leur idée, c'est l'outil le plus utile de tout le module.",
       note:"Le programme du niveau 6 demande deux constructions : si + présent pour un fait présent ou à venir, et si + passé composé pour un fait passé."},

      {t:'ana', h:"Sur un fait présent ou à venir",
       p:"Le plus fréquent, et de loin.",
       mots:[['La condition','<b>si</b> + présent'],
             ['La conséquence','au présent ou au futur', true],
             ['Un exemple','<b>Si</b> elle <b>réussit</b> le test, la preuve arrivera en janvier.'],
             ['Un autre','<b>Si</b> elle <b>a</b> une question, elle appelle le poste 4412.']],
       say:"Si elle réussit le test, la preuve arrivera en janvier.",
       note:"Le futur existe bien dans ces phrases — mais de l'autre côté de la virgule, jamais après « si »."},

      {t:'ana', h:"Sur un fait passé",
       p:"Pour raisonner sur ce qui est peut-être déjà arrivé.",
       mots:[['La condition','<b>si</b> + passé composé'],
             ['La conséquence','au présent, le plus souvent', true],
             ['Un exemple','<b>Si</b> elle <b>a déposé</b> ses papiers lundi, ils sont au dossier aujourd\'hui.'],
             ['Ce que ça veut dire',"je ne sais pas si c'est arrivé, mais si c'est arrivé, voici la suite"]],
       say:"Si elle a déposé ses papiers lundi, ils sont au dossier aujourd'hui.",
       note:"C'est la phrase à employer au téléphone quand vous vérifiez qu'un envoi est bien arrivé."},

      {t:'labo', h:"Écoutez la condition et sa suite",
       p:"Choisissez le moment et l'exemple.",
       axes:[
         {id:'m', lbl:'Quel moment ?', opts:[['a','à venir'],['b','déjà arrivé']]},
         {id:'n', lbl:'Quel exemple ?', opts:[['1','le premier'],['2','le second']]}],
       out:{
         a1:{w:["Si elle réussit, la preuve arrivera."], say:"Si elle réussit le test, la preuve arrivera en janvier.", n:'si + présent, conséquence au futur'},
         a2:{w:["Si elle a une question, elle appelle."], say:"Si elle a une question, elle appelle le poste 4412.", n:'si + présent, conséquence au présent'},
         b1:{w:["Si elle les a déposés, ils sont au dossier."], say:"Si elle a déposé ses papiers lundi, ils sont au dossier aujourd'hui.", n:'si + passé composé, conséquence au présent'},
         b2:{w:["Si le centre l'a reçu, tout est réglé."], say:"Si le centre a reçu le résultat, tout est réglé.", n:'même construction, autre sujet'},
       },
       note:"Deux constructions seulement. Le reste s'invente à partir de celles-là."},

      {t:'ex', h:"Six phrases pour poser une condition poliment",
       p:"À gauche ce que vous dites, à droite ce que ça fait.",
       rows:[
         ["Si j'y vais avant, je vais y penser pendant l'épreuve.","Vous déplacez une date sans refuser."],
         ["Si la preuve arrive en janvier, est-ce que ça suffit ?","Vous vérifiez avant de vous engager."],
         ["Si je comprends bien, la place est gardée jusqu'au 6 février.","Vous confirmez ce que vous avez entendu."],
         ["Si je rate le test, est-ce que je peux le reprendre ?","Vous préparez la suite sans dramatiser."],
         ["Si vous préférez, je peux venir un autre jour.","Vous laissez le choix à l'autre."],
         ["Si tout est déposé avant février, il n'y a plus rien à faire.","Vous résumez l'entente en une phrase."],
       ]},

      {t:'piege', h:"Deux pièges",
       rows:[
         ["mettre un futur après « si »","mettre le présent",
          "« Si elle viendra demain… » ❌ On dit « Si elle <b>vient</b> demain, on regardera son dossier ». Le futur va toujours dans la deuxième partie de la phrase."],
         ["écrire « si il »","écrire « s'il »",
          "Devant « il » et « ils », « si » se colle : <b>s'il</b>, <b>s'ils</b>. Devant « elle », rien ne change : « si elle »."],
       ]},

      {t:'revoir', h:"À retenir",
       p:"<b>si + présent</b>, conséquence au présent ou au futur. <b>si + passé composé</b>, conséquence au présent. Jamais de futur juste après « si ». Et devant « il », on écrit <b>s'il</b>."},
    ]
  },

  t3pdv: {
    eye:'Mini-leçon', tit:"Annoncer que ce qui suit est un avis",
    blocs:[
      {t:'texte', h:"Deux mots qui changent tout",
       p:"« Trois semaines, c'est trop court. » — c'est présenté comme un fait, et votre interlocuteur doit d'abord vous contredire avant de pouvoir répondre. « À mon avis, trois semaines, c'est trop court. » — c'est présenté comme un avis, et il peut donner le sien sans vous démentir. Le contenu est identique ; l'échange qui suit n'a rien à voir. C'est la différence entre une discussion et une dispute.",
       note:"Le programme du niveau 6 le nomme : « employer des connecteurs de points de vue courants »."},

      {t:'ana', h:"Ceux qui parlent de vous",
       p:"Ils se placent au début de la phrase, suivis d'une virgule.",
       mots:[['Le plus courant','<b>à mon avis</b>'],
             ['Pour vous distinguer des autres','<b>pour ma part</b> · <b>quant à moi</b>', true],
             ['Pour insister que c\'est bien vous','<b>personnellement</b>'],
             ['Un peu plus écrit','<b>selon moi</b>']],
       say:"À mon avis, votre dossier est en meilleur état que vous ne le croyez.",
       note:"« Pour ma part » est le plus utile dans une rencontre : il dit « les autres pensent peut-être autrement, et c'est correct »."},

      {t:'ana', h:"Ceux qui parlent de quelqu'un d'autre",
       p:"Suivis d'un nom, jamais d'un pronom seul.",
       mots:[['La forme','<b>selon</b> + nom · <b>d\'après</b> + nom'],
             ['Un exemple','<b>Selon</b> la responsable, aucun délai n\'est possible.', true],
             ['Ce que ça sert',"dire d'où vient l'information et à qui elle appartient"],
             ['Pourquoi c\'est utile ici','quand quatre personnes parlent, il faut savoir qui a dit quoi']],
       say:"Selon la responsable de l'admission, aucun délai n'est accordé après le 6 février.",
       note:"Confondre « à mon avis » et « selon la responsable » fait dire à quelqu'un ce qu'il n'a pas dit. Dans un compte rendu, c'est une erreur sérieuse."},

      {t:'ana', h:"Ceux qui se glissent dans la phrase",
       p:"Plus doux, plus parlés. Ils adoucissent une objection.",
       mots:[['Les trois formes','<b>je trouve que</b> · <b>il me semble que</b> · <b>j\'ai l\'impression que</b>'],
             ['Un exemple','Il me <b>semble</b> que la date devrait être écrite quelque part.', true],
             ['Quand les employer','quand vous n\'êtes pas sûr, ou quand vous contredisez quelqu\'un']],
       say:"Il me semble que la date de la visite devrait être écrite quelque part.",
       note:"« Il me semble que » est la façon la plus polie de dire « vous avez oublié quelque chose »."},

      {t:'ex', h:"Six phrases entendues dans la rencontre",
       p:"À gauche la phrase, à droite à qui appartient l'avis.",
       rows:[
         ["À mon avis, votre dossier est en bon état.","À celui qui parle. C'est son opinion."],
         ["Pour ma part, je préférerais y aller après.","À celui qui parle, par rapport aux autres."],
         ["Selon la responsable, aucun délai n'est possible.","À la responsable, pas à celui qui parle."],
         ["Personnellement, je trouve ça court.","À celui qui parle, et il insiste."],
         ["Il me semble que la date devrait être écrite.","À celui qui parle, mais il n'est pas sûr."],
         ["Aucun délai n'est accordé après cette date.","À personne : c'est présenté comme un fait."],
       ]},

      {t:'piege', h:"Deux pièges",
       rows:[
         ["dire « selon moi je pense que »","choisir l'un des deux",
          "Un seul connecteur par phrase. « Selon moi, c'est court » ou « Je pense que c'est court » — jamais les deux ensemble."],
         ["présenter son avis comme un fait","l'annoncer",
          "« C'est trop court. » oblige l'autre à vous contredire pour parler. « À mon avis, c'est trop court. » lui laisse la place de dire autre chose. C'est deux mots de plus et une discussion entière de gagnée."],
       ]},

      {t:'revoir', h:"À retenir",
       p:"Pour vous : <b>à mon avis · pour ma part · personnellement · quant à moi · selon moi</b>. Pour quelqu'un d'autre : <b>selon</b> ou <b>d'après</b> + son nom. Pour adoucir : <b>il me semble que</b>."},
    ]
  },
};
