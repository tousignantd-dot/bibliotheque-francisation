const PLUS = {

  prNasales: {
    eye:'Mini-leçon', tit:"Deux sons qui décident du mot : [ɑ̃] et [ɔ̃]",
    blocs:[
      {t:'texte', h:"Le même mot, à un son près",
       p:"Le vocabulaire du travail est plein de mots nasaux : <i>expérience, formation, permanent, fonction, production, promotion, remplacement</i>. Deux sons y reviennent sans arrêt, <b>[ɑ̃]</b> (« an », « en ») et <b>[ɔ̃]</b> (« on »). Les confondre ne rend pas la phrase incompréhensible, mais ça la rend fatigante à écouter — et une entrevue dure vingt minutes.",
       note:"Un son <b>nasal</b>, c'est un son qui passe par le nez. Posez deux doigts sur votre nez et dites « on » : ça vibre."},

      {t:'ana', h:"[ɑ̃] — la bouche ouverte, la langue en arrière",
       p:"C'est le son de « an » dans <i>permanent</i>.",
       mots:[['On écrit','{an}, {en}, {am}, {em}'],['On entend','[ɑ̃]',true],['Exemples','perman{en}t · exp{é}ri{en}ce · {en}trepôt']],
       say:"permanent, expérience, entrepôt",
       note:"La bouche s'ouvre franchement, comme pour dire « ah », et le son sort par le nez."},

      {t:'ana', h:"[ɔ̃] — les lèvres arrondies, presque un « o »",
       p:"C'est le son de « on » dans <i>formation</i>.",
       mots:[['On écrit','{on}, {om}'],['On entend','[ɔ̃]',true],['Exemples','format{ion} · f{on}ct{ion} · prom{ot}i{on}']],
       say:"formation, fonction, promotion",
       note:"Arrondissez les lèvres comme pour souffler une bougie. Si vos lèvres ne bougent pas, vous dites [ɑ̃]."},

      {t:'texte', h:"Le repère qui règle presque tout",
       p:"Les noms en <b>-tion</b> et <b>-sion</b> se disent tous <b>[ɔ̃]</b> à la fin : <i>formation, fonction, production, promotion, décision, profession</i>. Or ces mots sont partout dans une offre d'emploi. Retenez la terminaison, vous réglez la moitié des cas.",
       note:"Et l'autre moitié ? Les mots en <b>-ment</b> et <b>-ent</b> : <i>remplacement, département, permanent</i>. Ceux-là sont [ɑ̃]."},

      {t:'labo', h:"Écoutez la différence",
       p:"Choisissez un mot et le son que vous voulez entendre.",
       axes:[
         {id:'m', lbl:'Quelle famille ?', opts:[['a','les métiers'],['b','le poste'],['c','le parcours']]},
         {id:'s', lbl:'Quel son ?', opts:[['1','[ɑ̃] · an'],['2','[ɔ̃] · on']]}],
       out:{
         a1:{w:["un enseignant"], say:"un enseignant", n:'« en » au début : [ɑ̃]'},
         a2:{w:["une profession"], say:"une profession", n:'« -sion » à la fin : [ɔ̃]'},
         b1:{w:["un poste permanent"], say:"un poste permanent", n:'deux fois [ɑ̃] dans le même mot'},
         b2:{w:["une fonction"], say:"une fonction", n:'« on » puis « -tion » : deux fois [ɔ̃]'},
         c1:{w:["six ans d'expérience"], say:"six ans d'expérience", n:'« ans » et « -ence » : le même son'},
         c2:{w:["une formation"], say:"une formation", n:'« -tion » : [ɔ̃], toujours'},
       },
       note:"Écoutez deux fois, puis répétez à voix haute avant de passer au suivant."},

      {t:'ex', h:"Six paires à écouter et à répéter",
       p:"Le premier mot est [ɑ̃], le second [ɔ̃].",
       rows:[
         ["l'expérience et la formation","[ɑ̃] puis [ɔ̃]"],
         ["un poste permanent et une promotion","[ɑ̃] puis [ɔ̃]"],
         ["l'entrepôt et la production","[ɑ̃] puis [ɔ̃]"],
         ["un remplacement et une fonction","[ɑ̃] puis [ɔ̃]"],
         ["un employé compétent","deux fois [ɑ̃]"],
         ["une bonne recommandation","[ɔ̃], [ɔ̃], puis [ɑ̃] et [ɔ̃]"],
       ]},

      {t:'piege', h:"Trois pièges à connaître",
       rows:[
         ["dire « formatian »","dire « formation », lèvres arrondies",
          "C'est l'erreur la plus fréquente et la plus facile à corriger : tous les mots en <b>-tion</b> finissent par [ɔ̃]."],
         ["prononcer le « n » de « an »","le « n » ne se prononce pas, il nasalise",
          "Dans <i>permanent</i>, on n'entend aucun « n » détaché. La lettre indique seulement que l'air passe par le nez."],
         ["oublier que « em » et « am » sont [ɑ̃]","« emploi » commence comme « an »",
          "Devant un <b>b</b> ou un <b>p</b>, on écrit <b>em</b> ou <b>am</b>, mais le son ne change pas : <i>emploi, employeur, remplacement</i>."],
       ]},

      {t:'check', h:"Est-ce que c'est clair maintenant ?",
       p:"Quatre questions rapides.",
       qs:[
         {q:"« Formation » finit par le son…", opts:["[ɑ̃] · an","[ɔ̃] · on"], ok:1,
          fb:"Tous les mots en -tion finissent par [ɔ̃]."},
         {q:"« Permanent » contient…", opts:["deux fois [ɑ̃]","deux fois [ɔ̃]"], ok:0,
          fb:"« -man- » et « -nent » se disent tous deux [ɑ̃]."},
         {q:"Pour dire [ɔ̃], les lèvres sont…", opts:["arrondies","étirées"], ok:0,
          fb:"Comme pour souffler une bougie."},
         {q:"« Emploi » commence par le son…", opts:["[ɑ̃]","[ɔ̃]"], ok:0,
          fb:"« em » devant un p se dit [ɑ̃], comme « an »."},
       ]},
    ]
  },

  prMots: {
    eye:'Mini-leçon', tit:"Une racine, plusieurs mots : les fabriquer soi-même",
    blocs:[
      {t:'texte', h:"Pourquoi ça vaut la peine",
       p:"Le vocabulaire du travail n'est pas une liste de mots séparés : c'est une petite dizaine de <b>racines</b> qui se recombinent. <i>Employer</i> donne <i>un emploi, un employé, un employeur, employable</i>. <i>Former</i> donne <i>la formation, un formateur, une formatrice</i>. Apprendre la racine et les morceaux qui s'y collent vaut mieux qu'apprendre cent mots un par un.",
       note:"On appelle <b>préfixe</b> le morceau qui se colle devant, et <b>suffixe</b> celui qui se colle derrière."},

      {t:'ana', h:"Le suffixe -eur : celui qui fait l'action",
       p:"Il fabrique le nom de la personne ou de la machine qui fait quelque chose.",
       mots:[['La racine','{employ}-'],['Le suffixe','-{eur}',true],['Le mot','un employ{eur}']],
       say:"un employeur",
       note:"Même famille : <i>un formateur, un vendeur, un travailleur, un conseiller</i>. Au féminin : <i>-euse</i> (<i>une vendeuse</i>) ou <i>-trice</i> (<i>une formatrice</i>)."},

      {t:'ana', h:"Le suffixe -tion : le nom de l'action",
       p:"Il transforme un verbe en nom d'action.",
       mots:[['Le verbe','{former}'],['Le suffixe','-{ation}',true],['Le nom','la form{ation}']],
       say:"la formation",
       note:"Même famille : <i>la production, la promotion, la présentation, la recommandation</i>. Tous ces noms sont féminins — sans exception."},

      {t:'ana', h:"Le suffixe -able : ce qui est possible",
       p:"Il transforme un verbe en adjectif.",
       mots:[['Le verbe','{transfér}er'],['Le suffixe','-{able}',true],['L\'adjectif','transfér{able}']],
       say:"une expérience transférable",
       note:"<i>Transférable</i> veut dire « qu'on peut transférer ». Le Défi 1 y revient en détail."},

      {t:'labo', h:"Fabriquez le mot",
       p:"Choisissez une racine et un morceau à coller.",
       axes:[
         {id:'r', lbl:'Quelle racine ?', opts:[['a','employ-'],['b','form-'],['c','travail-']]},
         {id:'s', lbl:'Quel morceau ?', opts:[['1','-eur (qui fait)'],['2','-tion / -é (l\'action, le résultat)'],['3','-able (ce qui est possible)']]}],
       out:{
         a1:{w:["un employeur"], say:"un employeur", n:'celui qui donne le travail'},
         a2:{w:["un employé"], say:"un employé", n:'celui qui reçoit le travail'},
         a3:{w:["employable"], say:"une personne employable", n:'qu\'une entreprise peut engager'},
         b1:{w:["un formateur"], say:"un formateur", n:'celui qui donne la formation'},
         b2:{w:["la formation"], say:"la formation", n:'l\'action de former'},
         b3:{w:["formable"], say:"un employé formable", n:'rare, mais compris : qu\'on peut former'},
         c1:{w:["un travailleur"], say:"un travailleur", n:'celui qui travaille'},
         c2:{w:["le travail"], say:"le travail", n:'ici, pas de -tion : le nom est plus court'},
         c3:{w:["un horaire faisable"], say:"un horaire faisable", n:'de faire : qu\'on peut faire'},
       },
       note:"Neuf combinaisons, neuf mots vrais. C'est ce que fait le français tout le temps."},

      {t:'ex', h:"Les préfixes qui changent le sens",
       p:"Trois morceaux devant le mot, trois effets différents.",
       rows:[
         ["refaire son curriculum vitæ","re- : recommencer"],
         ["revoir sa lettre avant de l'envoyer","re- : une deuxième fois"],
         ["un dossier incomplet","in- : le contraire de complet"],
         ["une offre inacceptable","in- : le contraire d'acceptable"],
         ["déplacer un rendez-vous","dé- : défaire ce qui était placé"],
         ["désapprouver une décision","dés- : le contraire d'approuver"],
       ]},

      {t:'piege', h:"Deux pièges à connaître",
       rows:[
         ["confondre « employé » et « employeur »","l'employé reçoit, l'employeur donne",
          "C'est <b>-é</b> contre <b>-eur</b>, une seule syllabe de différence, et le sens s'inverse. En entrevue, dire « je cherche un employé » quand on cherche un emploi fait mauvais effet."],
         ["croire que tous les noms en -tion sont masculins","ils sont tous féminins",
          "<i>La</i> formation, <i>la</i> production, <i>la</i> promotion, <i>la</i> décision. C'est une des rares règles du français sans exception : profitez-en."],
       ]},

      {t:'check', h:"Est-ce que c'est clair maintenant ?",
       p:"Quatre questions rapides.",
       qs:[
         {q:"Celui qui donne le travail est…", opts:["un employé","un employeur"], ok:1,
          fb:"-eur désigne celui qui fait l'action."},
         {q:"« La formation » est un nom…", opts:["féminin","masculin"], ok:0,
          fb:"Tous les noms en -tion sont féminins."},
         {q:"« Incomplet » veut dire…", opts:["complet à moitié","pas complet"], ok:1,
          fb:"in- nie le mot qui suit."},
         {q:"Un horaire « modifiable » est un horaire…", opts:["qu'on peut modifier","déjà modifié"], ok:0,
          fb:"-able dit toujours ce qui est possible."},
       ]},
    ]
  },

  t1able: {
    eye:'Mini-leçon', tit:"Les mots en -able : dire ce qui est possible",
    blocs:[
      {t:'texte', h:"Un raccourci que les offres d'emploi adorent",
       p:"Une offre d'emploi est un texte court qui doit tout dire. Alors elle remplace « un contrat qu'on peut renouveler » par « un contrat <b>renouvelable</b> », et « une expérience qu'on peut transférer d'un emploi à l'autre » par « une expérience <b>transférable</b> ». Comprendre ce suffixe, c'est comprendre le quart d'une offre.",
       note:"Le sens ne change jamais : <b>-able</b> veut toujours dire « qu'on peut »."},

      {t:'ana', h:"Comment on le fabrique",
       p:"Trois gestes, toujours les mêmes.",
       mots:[['Le verbe','{renouveler}'],['On enlève','-er'],['On ajoute','-{able}',true],['Le résultat','renouvel{able}']],
       say:"un contrat renouvelable",
       note:"Avec les verbes en <b>-re</b>, on enlève le <b>-re</b> : <i>vendre → vendable</i>, <i>lire → lisible</i> (celui-là est irrégulier)."},

      {t:'ana', h:"La famille en -ible",
       p:"Une minorité de mots prennent <b>-ible</b> au lieu de <b>-able</b>.",
       mots:[['Le plus utile','dispon{ible}',true],['Les autres du travail','access{ible} · flex{ible} · compat{ible}'],['Le sens','le même : ce qui est possible']],
       say:"Je suis disponible dès lundi.",
       note:"Il n'y a pas de règle pour deviner. Heureusement, ils sont peu nombreux, et ce sont presque tous des mots du monde du travail : apprenez-les comme des mots de vocabulaire."},

      {t:'ana', h:"Le préfixe in- qui renverse tout",
       p:"On colle <b>in-</b> devant, et le sens s'inverse.",
       mots:[['Le mot','{acceptable}'],['Le préfixe','{in}-',true],['Le contraire','{in}acceptable']],
       say:"Ces conditions sont inacceptables.",
       note:"Devant <b>p</b> et <b>b</b>, <i>in-</i> s'écrit <b>im-</b> : <i>impossible, imprévisible</i>. Devant <b>l</b>, c'est <b>il-</b> : <i>illisible</i>."},

      {t:'labo', h:"Fabriquez l'adjectif",
       p:"Choisissez un verbe, puis la forme voulue.",
       axes:[
         {id:'v', lbl:'Quel verbe ?', opts:[['a','transférer'],['b','négocier'],['c','accepter'],['d','prévoir']]},
         {id:'f', lbl:'Quelle forme ?', opts:[['1','ce qui est possible'],['2','le contraire']]}],
       out:{
         a1:{w:["une expérience transférable"], say:"une expérience transférable", n:'qu\'on peut transférer d\'un emploi à l\'autre'},
         a2:{w:["un diplôme intransférable"], say:"un diplôme intransférable", n:'qui ne se transfère pas'},
         b1:{w:["un salaire négociable"], say:"un salaire négociable", n:'on peut en discuter'},
         b2:{w:["un salaire non négociable"], say:"un salaire non négociable", n:'ici on dit « non », pas « in- »'},
         c1:{w:["une offre acceptable"], say:"une offre acceptable", n:'qu\'on peut accepter'},
         c2:{w:["des conditions inacceptables"], say:"des conditions inacceptables", n:'in- devant une voyelle'},
         d1:{w:["un horaire prévisible"], say:"un horaire prévisible", n:'celui-là prend -ible'},
         d2:{w:["un horaire imprévisible"], say:"un horaire imprévisible", n:'im- devant un p'},
       },
       note:"Remarquez le cas de « non négociable » : quelques mots refusent le préfixe et prennent « non » devant. On les entend, on les retient."},

      {t:'ex', h:"Six phrases entendues en recherche d'emploi",
       p:"Toutes contiennent un mot en -able ou -ible.",
       rows:[
         ["Le poste est disponible immédiatement.","libre, à prendre"],
         ["Votre expérience est transférable.","elle compte ici aussi"],
         ["C'est un contrat renouvelable après un an.","on peut le prolonger"],
         ["L'horaire est flexible du lundi au jeudi.","il peut s'adapter"],
         ["Ce document est illisible : réécrivez-le.","on ne peut pas le lire"],
         ["Le salaire est négociable selon l'expérience.","on peut en discuter"],
       ]},

      {t:'piege', h:"Trois pièges à connaître",
       rows:[
         ["« un horaire adaptible »","« un horaire adaptable »",
          "La forme normale est <b>-able</b>. On ne met <b>-ible</b> que dans la petite liste apprise par cœur : <i>disponible, accessible, flexible, compatible, lisible, possible, prévisible</i>."],
         ["croire que -able veut dire « déjà fait »","-able dit « qu'on peut faire »",
          "Un horaire <i>modifiable</i> n'a pas été modifié : il <b>peut</b> l'être. C'est une possibilité, jamais un fait accompli."],
         ["dire « innégociable »","« non négociable »",
          "Quelques adjectifs refusent <i>in-</i> et prennent <i>non</i> devant, séparé par une espace. En cas de doute, <i>non</i> passe toujours."],
       ]},

      {t:'check', h:"Est-ce que c'est clair maintenant ?",
       p:"Quatre questions rapides.",
       qs:[
         {q:"Un contrat renouvelable est un contrat…", opts:["déjà renouvelé","qu'on peut renouveler"], ok:1,
          fb:"-able dit toujours la possibilité."},
         {q:"Le mot pour dire « libre, prêt à travailler » est…", opts:["disponable","disponible"], ok:1,
          fb:"C'est un des rares mots en -ible, et le plus utile de tous."},
         {q:"Le contraire de « possible » est…", opts:["impossible","inpossible"], ok:0,
          fb:"Devant un p, in- devient im-."},
         {q:"« Une expérience transférable » veut dire…", opts:["elle compte dans un autre emploi","elle est finie"], ok:0,
          fb:"C'est le mot qu'il faut employer quand votre expérience vient d'un autre pays."},
       ]},
    ]
  },

  t1ou: {
    eye:'Mini-leçon', tit:"« où » : le mot qui évite de se répéter",
    blocs:[
      {t:'texte', h:"Deux phrases qui n'en font plus qu'une",
       p:"« C'est l'entrepôt. Je travaille dans cet entrepôt. » Deux phrases, et le mot <i>entrepôt</i> dit deux fois. Avec <b>où</b>, il n'est dit qu'une fois : « C'est l'entrepôt <b>où</b> je travaille. » C'est plus court, et surtout ça fait partie de ce qu'on attend d'un discours structuré — en entrevue comme dans une lettre.",
       note:"<b>où</b> remplace toujours un <b>lieu</b> ou un <b>moment</b>. Rien d'autre."},

      {t:'ana', h:"Un lieu",
       p:"Le mot remplacé désigne un endroit.",
       mots:[['Phrase 1','C\'est l\'{entrepôt}.'],['Phrase 2','Je travaille dans cet {entrepôt}.'],['Ensemble','C\'est l\'entrepôt {où} je travaille.',true]],
       say:"C'est l'entrepôt où je travaille.",
       note:"<b>où</b> se place juste après le nom qu'il remplace. Jamais ailleurs."},

      {t:'ana', h:"Un moment",
       p:"Le mot remplacé désigne un temps : une année, un jour, un moment.",
       mots:[['Phrase 1','2024, c\'est l\'{année}.'],['Phrase 2','Je suis arrivée cette {année}-là.'],['Ensemble','2024, c\'est l\'année {où} je suis arrivée.',true]],
       say:"2024, c'est l'année où je suis arrivée.",
       note:"En français, on ne dit pas « l'année <i>quand</i> » : c'est <b>où</b>, même pour le temps. C'est la surprise de cette leçon."},

      {t:'texte', h:"« où » et « ou » : l'accent change tout",
       p:"<b>où</b> avec l'accent parle d'un lieu ou d'un moment : <i>la ville <b>où</b> j'habite</i>. <b>ou</b> sans accent propose un choix : <i>lundi <b>ou</b> mardi</i>. Le test qui ne rate jamais : si vous pouvez remplacer par <b>ou bien</b>, alors c'est <i>ou</i> sans accent.",
       note:"« Je peux commencer lundi <b>ou bien</b> mardi » : ça marche, donc pas d'accent. « L'année <b>ou bien</b> je suis arrivée » : ça ne veut rien dire, donc accent."},

      {t:'labo', h:"Reliez les deux phrases",
       p:"Choisissez ce dont vous parlez et ce que vous en dites.",
       axes:[
         {id:'n', lbl:'De quoi parlez-vous ?', opts:[['a','une entreprise'],['b','une ville'],['c','une année'],['d','un jour']]},
         {id:'s', lbl:'Que dites-vous ?', opts:[['1','j\'ai travaillé'],['2','je suis arrivée']]}],
       out:{
         a1:{w:["C'est l'entreprise où j'ai travaillé six ans."], say:"C'est l'entreprise où j'ai travaillé six ans.", n:'un lieu'},
         a2:{w:["C'est l'entreprise où je suis arrivée en 2019."], say:"C'est l'entreprise où je suis arrivée en 2019.", n:'un lieu, encore'},
         b1:{w:["Longueuil est la ville où j'ai travaillé."], say:"Longueuil est la ville où j'ai travaillé.", n:'un lieu'},
         b2:{w:["Longueuil est la ville où je suis arrivée."], say:"Longueuil est la ville où je suis arrivée.", n:'un lieu'},
         c1:{w:["2019, c'est l'année où j'ai travaillé le plus."], say:"2019, c'est l'année où j'ai travaillé le plus.", n:'un moment — et pourtant « où »'},
         c2:{w:["2024, c'est l'année où je suis arrivée au Québec."], say:"2024, c'est l'année où je suis arrivée au Québec.", n:'un moment'},
         d1:{w:["Mardi, c'est le jour où j'ai travaillé tard."], say:"Mardi, c'est le jour où j'ai travaillé tard.", n:'un moment'},
         d2:{w:["Voici le jour où je suis arrivée à l'entrevue."], say:"Voici le jour où je suis arrivée à l'entrevue.", n:'un moment'},
       },
       note:"Huit phrases, un seul mot de liaison. Lieu ou moment, c'est toujours « où »."},

      {t:'ex', h:"Six phrases utiles en entrevue",
       p:"Toutes emploient « où ».",
       rows:[
         ["C'est l'entreprise où j'ai appris le métier.","un lieu"],
         ["L'entrepôt où je travaille compte quarante employés.","un lieu"],
         ["2024 est l'année où je suis arrivée au Québec.","un moment"],
         ["Le jour où j'ai trouvé l'erreur, tout s'est réglé.","un moment"],
         ["C'est le secteur où j'ai le plus d'expérience.","un lieu, au figuré"],
         ["Il y a des moments où il faut demander de l'aide.","un moment"],
       ]},

      {t:'piege', h:"Trois pièges à connaître",
       rows:[
         ["« l'année quand je suis arrivée »","« l'année où je suis arrivée »",
          "Beaucoup de langues emploient leur mot pour « quand » ici. Le français emploie <b>où</b>, même pour le temps. C'est l'erreur la plus fréquente à ce point du cours."],
         ["« la ville ou j'habite »","« la ville où j'habite »",
          "Sans accent, <i>ou</i> propose un choix. Le test : si <b>ou bien</b> ne marche pas à la place, il faut l'accent."],
         ["placer « où » loin du nom","« où » se colle au nom qu'il remplace",
          "On dit « l'entrepôt <b>où</b> je travaille », jamais « l'entrepôt je travaille <b>où</b> ». Le mot suit immédiatement ce qu'il remplace."],
       ]},

      {t:'check', h:"Est-ce que c'est clair maintenant ?",
       p:"Quatre questions rapides.",
       qs:[
         {q:"« 2024 est l'année ___ je suis arrivée. »", opts:["où","quand"], ok:0,
          fb:"En français, même pour un moment, c'est « où »."},
         {q:"« Je commence lundi ___ mardi. »", opts:["où","ou"], ok:1,
          fb:"C'est un choix : « ou bien » marche, donc pas d'accent."},
         {q:"« où » remplace…", opts:["un lieu ou un moment","une personne"], ok:0,
          fb:"Pour une personne, ce serait « qui » ou « que »."},
         {q:"Le test qui ne rate jamais est de remplacer par…", opts:["« ou bien »","« et »"], ok:0,
          fb:"Si « ou bien » a du sens, il n'y a pas d'accent."},
       ]},
    ]
  },

  t2infpasse: {
    eye:'Mini-leçon', tit:"« Après avoir vérifié… » : l'infinitif passé",
    blocs:[
      {t:'texte', h:"La phrase qui fait professionnel",
       p:"Dans un formulaire de demande d'emploi, on décrit des tâches qui se suivent. « Je vérifiais les commandes. Ensuite, je préparais les bons de livraison. » C'est correct, mais c'est plat. Avec l'infinitif passé : « <b>Après avoir vérifié</b> les commandes, je préparais les bons de livraison. » Une seule phrase, un ordre clair, et un sujet dit une seule fois.",
       note:"Cette forme est très fréquente à l'écrit professionnel. C'est exactement ce qu'un employeur s'attend à lire."},

      {t:'ana', h:"Comment il se fabrique",
       p:"Deux morceaux, jamais plus.",
       mots:[['Le mot d\'entrée','{après}'],['L\'auxiliaire à l\'infinitif','{avoir} ou {être}',true],['Le participe passé','vérifi{é}']],
       say:"Après avoir vérifié les commandes",
       note:"On ne conjugue rien : <i>avoir</i> et <i>être</i> restent à l'infinitif. C'est ce qui rend la forme facile."},

      {t:'ana', h:"Avec « être », le participe s'accorde",
       p:"Les verbes de déplacement et les verbes pronominaux prennent <i>être</i>.",
       mots:[['Marisol dit','Après {être} arriv{ée} au Québec…',true],['Un homme dirait','Après {être} arriv{é} au Québec…'],['Au pluriel','Après {être} arriv{és}…']],
       say:"Après être arrivée au Québec, elle a suivi une formation.",
       note:"L'accord se fait avec la personne qui parle. Marisol écrit <i>arrivée</i> avec deux e."},

      {t:'ana', h:"Le contraire : « avant de » + infinitif présent",
       p:"Pour dire ce qui vient <b>après</b>, on emploie une autre forme.",
       mots:[['Ce qui vient avant','{Après avoir} rempli le formulaire'],['Ce qui vient après','{avant d\'}envoyer',true],['Ensemble','Après avoir rempli le formulaire, relisez-le avant d\'envoyer.']],
       say:"Après avoir rempli le formulaire, relisez-le avant d'envoyer.",
       note:"<b>avant de</b> + infinitif <b>présent</b>. Jamais « avant d'être parti » : ça n'existe pas."},

      {t:'labo', h:"Construisez la phrase",
       p:"Choisissez l'action qui vient d'abord et celle qui suit.",
       axes:[
         {id:'a', lbl:'D\'abord…', opts:[['a','recevoir les livraisons'],['b','vérifier les commandes'],['c','arriver au Québec']]},
         {id:'b', lbl:'…ensuite', opts:[['1','je comptais les boîtes'],['2','j\'ai suivi une formation']]}],
       out:{
         a1:{w:["Après avoir reçu les livraisons, je comptais les boîtes."], say:"Après avoir reçu les livraisons, je comptais les boîtes.", n:'avoir + participe irrégulier'},
         a2:{w:["Après avoir reçu les livraisons, j'ai suivi une formation."], say:"Après avoir reçu les livraisons, j'ai suivi une formation.", n:'la forme ne change pas'},
         b1:{w:["Après avoir vérifié les commandes, je comptais les boîtes."], say:"Après avoir vérifié les commandes, je comptais les boîtes.", n:'le cas le plus courant'},
         b2:{w:["Après avoir vérifié les commandes, j'ai suivi une formation."], say:"Après avoir vérifié les commandes, j'ai suivi une formation.", n:'avoir, toujours avoir'},
         c1:{w:["Après être arrivée au Québec, je comptais les boîtes."], say:"Après être arrivée au Québec, je comptais les boîtes.", n:'être + accord au féminin'},
         c2:{w:["Après être arrivée au Québec, j'ai suivi une formation."], say:"Après être arrivée au Québec, j'ai suivi une formation.", n:'la phrase du parcours, celle qu\'on écrit le plus'},
       },
       note:"Les deux actions ont le même sujet : c'est la condition pour employer cette forme."},

      {t:'ex', h:"Six phrases de formulaire",
       p:"Toutes viennent de la rubrique « description des tâches ».",
       rows:[
         ["Après avoir reçu les livraisons, je vérifiais les quantités.","avoir + participe"],
         ["Après avoir compté les boîtes, j'entrais les données au système.","avoir + participe"],
         ["Après être arrivée au Québec, j'ai suivi un cours de français.","être + accord"],
         ["Après avoir travaillé six ans dans les stocks, je connais le métier.","une durée"],
         ["Après m'être présentée à l'entrevue, j'ai envoyé un remerciement.","forme pronominale"],
         ["Avant d'envoyer le formulaire, relisez-le à voix haute.","le contraire : avant de + présent"],
       ]},

      {t:'piege', h:"Trois pièges à connaître",
       rows:[
         ["« Après avoir arrivé »","« Après être arrivé »",
          "<i>Arriver, partir, venir, rester, entrer, sortir</i> prennent <b>être</b>, jamais <i>avoir</i>. C'est la même liste qu'au passé composé : si vous dites « je suis arrivé », alors c'est « après être arrivé »."],
         ["« Après avoir vérifié, il préparait » avec deux sujets différents","un seul sujet pour les deux actions",
          "« Après avoir vérifié les commandes, <b>mon chef</b> partait » laisse croire que c'est le chef qui a vérifié. Si les sujets diffèrent, il faut écrire deux phrases."],
         ["« avant d'être parti »","« avant de partir »",
          "<b>avant de</b> demande toujours l'infinitif <b>présent</b>. Seul <i>après</i> prend l'infinitif passé."],
       ]},

      {t:'check', h:"Est-ce que c'est clair maintenant ?",
       p:"Quatre questions rapides.",
       qs:[
         {q:"« Après ___ les commandes, je préparais les bons. »", opts:["avoir vérifié","être vérifié"], ok:0,
          fb:"Vérifier prend avoir."},
         {q:"Marisol écrit : « Après être ___ au Québec… »", opts:["arrivé","arrivée"], ok:1,
          fb:"Avec être, le participe s'accorde avec elle."},
         {q:"« Avant de ___ , relisez votre lettre. »", opts:["envoyer","avoir envoyé"], ok:0,
          fb:"Avant de demande l'infinitif présent."},
         {q:"Pour employer cette forme, il faut que les deux actions aient…", opts:["le même sujet","des sujets différents"], ok:0,
          fb:"C'est justement ce qui permet de ne pas répéter le sujet."},
       ]},
    ]
  },

  t2inf: {
    eye:'Mini-leçon', tit:"« de », « à », ou rien : le verbe décide",
    blocs:[
      {t:'texte', h:"Le point qui trahit le plus une lettre écrite trop vite",
       p:"« J'accepte <b>de</b> travailler le samedi. » « Je suis prête <b>à</b> apprendre votre logiciel. » « Je souhaite travailler à temps plein. » Trois phrases, trois constructions différentes — et ce n'est pas le sens qui décide, c'est le <b>verbe de départ</b>. Chaque verbe garde toujours le même mot devant l'infinitif, dans toutes ses phrases, toute sa vie.",
       note:"Cela veut dire une bonne nouvelle : il n'y a rien à comprendre, seulement à retenir. Et pour une lettre de motivation, trois verbes suffisent."},

      {t:'ana', h:"Les verbes qui demandent « de »",
       p:"Le groupe le plus large.",
       mots:[['La liste utile','accepter · décider · essayer · oublier · refuser · demander · permettre'],['Le mot','{de}',true],['Un exemple','J\'accepte {de} travailler le samedi.']],
       say:"J'accepte de travailler le samedi.",
       note:"Devant une voyelle, <b>de</b> devient <b>d'</b> : <i>j'essaie <b>d'</b>arriver tôt</i>."},

      {t:'ana', h:"Les verbes qui demandent « à »",
       p:"Souvent des verbes de progression : on commence, on continue, on réussit.",
       mots:[['La liste utile','apprendre · commencer · continuer · hésiter · réussir · être prêt'],['Le mot','{à}',true],['Un exemple','Je suis prête {à} apprendre votre logiciel.']],
       say:"Je suis prête à apprendre votre logiciel.",
       note:"<i>Être prêt à</i> est la formule reine de la lettre de motivation. Retenez-la telle quelle."},

      {t:'ana', h:"Les verbes qui ne demandent rien",
       p:"L'infinitif se colle directement au verbe.",
       mots:[['La liste utile','aimer · aller · devoir · espérer · pouvoir · savoir · souhaiter · vouloir'],['Le mot','{rien}',true],['Un exemple','Je souhaite {travailler} à temps plein.']],
       say:"Je souhaite travailler à temps plein.",
       note:"Ce sont presque tous des verbes très fréquents. Ajouter « de » après <i>souhaiter</i> ou <i>vouloir</i> est une erreur qu'on entend beaucoup."},

      {t:'labo', h:"Composez votre phrase de lettre",
       p:"Choisissez le verbe de départ et ce que vous voulez dire.",
       axes:[
         {id:'v', lbl:'Quel verbe ?', opts:[['a','souhaiter'],['b','être prêt'],['c','accepter'],['d','demander']]},
         {id:'q', lbl:'Quoi ?', opts:[['1','travailler chez vous'],['2','apprendre le logiciel']]}],
       out:{
         a1:{w:["Je souhaite travailler dans votre entreprise."], say:"Je souhaite travailler dans votre entreprise.", n:'souhaiter : rien devant'},
         a2:{w:["Je souhaite apprendre votre logiciel."], say:"Je souhaite apprendre votre logiciel.", n:'toujours rien'},
         b1:{w:["Je suis prête à travailler dans votre entreprise."], say:"Je suis prête à travailler dans votre entreprise.", n:'être prêt : à'},
         b2:{w:["Je suis prête à apprendre votre logiciel."], say:"Je suis prête à apprendre votre logiciel.", n:'la phrase la plus utile du module'},
         c1:{w:["J'accepte de travailler dans votre entreprise."], say:"J'accepte de travailler dans votre entreprise.", n:'accepter : de'},
         c2:{w:["J'accepte d'apprendre votre logiciel."], say:"J'accepte d'apprendre votre logiciel.", n:'de devient d\' devant une voyelle'},
         d1:{w:["Je vous demande de me permettre de travailler chez vous."], say:"Je vous demande de me permettre de travailler chez vous.", n:'deux verbes en « de » à la suite'},
         d2:{w:["Je vous demande de m'apprendre votre logiciel."], say:"Je vous demande de m'apprendre votre logiciel.", n:'demander : de'},
       },
       note:"Huit phrases, quatre verbes. Ce sont ceux d'une lettre de motivation ordinaire."},

      {t:'ex', h:"Six phrases de lettre de motivation",
       p:"Repérez le mot qui suit le verbe.",
       rows:[
         ["Je souhaite occuper le poste de commis à l'inventaire.","souhaiter : rien"],
         ["Je suis prête à commencer dès le mois prochain.","être prêt : à"],
         ["J'accepte de travailler un samedi sur deux.","accepter : de"],
         ["Je vous demande de bien vouloir examiner ma candidature.","demander : de"],
         ["J'ai commencé à suivre des cours de français en 2024.","commencer : à"],
         ["Je peux vous rencontrer la semaine prochaine.","pouvoir : rien"],
       ]},

      {t:'piege', h:"Trois pièges à connaître",
       rows:[
         ["« Je souhaite de travailler »","« Je souhaite travailler »",
          "<i>Souhaiter, vouloir, désirer, espérer, pouvoir, devoir, savoir</i> ne prennent rien. C'est la faute la plus fréquente dans les lettres de motivation."],
         ["« Je suis prête de commencer »","« Je suis prête à commencer »",
          "<i>Être prêt</i> prend toujours <b>à</b>. Comme c'est une des trois phrases qu'on écrit dans toute lettre, l'erreur se voit tout de suite."],
         ["chercher une logique","il n'y en a pas",
          "Ni le sens, ni la forme du verbe ne permettent de deviner. C'est une information attachée au verbe, comme son genre l'est à un nom : elle s'apprend avec lui."],
       ]},

      {t:'check', h:"Est-ce que c'est clair maintenant ?",
       p:"Quatre questions rapides.",
       qs:[
         {q:"« Je souhaite ___ travailler chez vous. »", opts:["de","rien"], ok:1,
          fb:"Souhaiter ne prend rien."},
         {q:"« Je suis prête ___ apprendre. »", opts:["à","de"], ok:0,
          fb:"Être prêt prend toujours à."},
         {q:"« Je vous demande ___ examiner ma candidature. »", opts:["à","de"], ok:1,
          fb:"Demander prend de."},
         {q:"Ce qui décide du mot, c'est…", opts:["le sens de la phrase","le verbe de départ"], ok:1,
          fb:"Chaque verbe garde le sien dans toutes ses phrases."},
       ]},
    ]
  },

  t2lettre: {
    eye:'Mini-leçon', tit:"La lettre de motivation : trois paragraphes, des formules figées",
    blocs:[
      {t:'texte', h:"Ce qu'on attend vraiment de cette lettre",
       p:"Une lettre de motivation ne raconte pas votre vie : elle répond à une question précise, « pourquoi vous et pas quelqu'un d'autre ? », en une demi-page. Elle a une forme fixe et des formules qui ne s'inventent pas. C'est une bonne nouvelle : ce qui est figé se recopie, et vous ne dépensez votre français que là où il compte, dans le deuxième paragraphe.",
       note:"Elle accompagne toujours le CV. Le CV donne les faits ; la lettre dit ce qu'ils veulent dire pour ce poste-ci."},

      {t:'ana', h:"L'appel — la première ligne",
       p:"Ce qu'on écrit avant tout le reste.",
       mots:[['Sans le nom','{Madame, Monsieur,}',true],['Avec le nom','{Madame Toubaï,}'],['Jamais','Bonjour · Salut · À qui de droit']],
       say:"Madame, Monsieur,",
       note:"La virgule à la fin, et on va à la ligne. « À qui de droit » existe, mais fait vieux et distant : préférez « Madame, Monsieur, »."},

      {t:'ana', h:"Paragraphe 1 — pourquoi j'écris",
       p:"Deux informations, pas une de plus : le poste et où vous l'avez vu.",
       mots:[['La formule','Je vous {soumets ma candidature}',true],['Le poste','au poste de {commis à l\'inventaire}'],['La source','affiché sur votre site le 3 mars.']],
       say:"Je vous soumets ma candidature au poste de commis à l'inventaire, affiché sur votre site le 3 mars.",
       note:"Une entreprise affiche souvent plusieurs postes à la fois. Sans le titre exact, votre lettre ne sait pas où aller."},

      {t:'ana', h:"Paragraphe 2 — ce que j'apporte",
       p:"C'est le seul endroit où vous écrivez vraiment. Deux phrases, avec un chiffre.",
       mots:[['La durée','J\'ai {six ans d\'expérience}',true],['Le domaine','en gestion des stocks'],['La preuve','dont l\'inventaire de {800 références}.']],
       say:"J'ai six ans d'expérience en gestion des stocks, dont l'inventaire de 800 références.",
       note:"Reprenez deux ou trois mots exacts de l'offre d'emploi. L'employeur les reconnaît, et sa lecture devient facile."},

      {t:'ana', h:"Paragraphe 3 et la salutation",
       p:"Ce que vous demandez, puis la formule de sortie.",
       mots:[['La demande','Je demeure {disponible} pour vous rencontrer'],['Le remerciement','et vous remercie de l\'attention portée à ma demande.'],['La sortie','{Veuillez agréer, Madame, Monsieur, mes salutations distinguées.}',true]],
       say:"Veuillez agréer, Madame, Monsieur, mes salutations distinguées.",
       note:"La salutation reprend exactement l'appel du début. Si vous avez écrit « Madame Toubaï, », vous finissez par « Veuillez agréer, Madame Toubaï, … »."},

      {t:'labo', h:"Assemblez votre lettre",
       p:"Choisissez le paragraphe et le poste.",
       axes:[
         {id:'p', lbl:'Quel paragraphe ?', opts:[['1','pourquoi j\'écris'],['2','ce que j\'apporte'],['3','ce que je demande']]},
         {id:'e', lbl:'Quel poste ?', opts:[['a','commis à l\'inventaire'],['b','préposée aux bénéficiaires']]}],
       out:{
         '1a':{w:["Je vous soumets ma candidature au poste de commis à l'inventaire, affiché sur votre site le 3 mars."], say:"Je vous soumets ma candidature au poste de commis à l'inventaire, affiché sur votre site le 3 mars.", n:'le titre exact et la date'},
         '1b':{w:["Je vous soumets ma candidature au poste de préposée aux bénéficiaires, affiché sur votre site le 3 mars."], say:"Je vous soumets ma candidature au poste de préposée aux bénéficiaires, affiché sur votre site le 3 mars.", n:'la même formule, un autre poste'},
         '2a':{w:["J'ai six ans d'expérience en gestion des stocks, dont l'inventaire de 800 références."], say:"J'ai six ans d'expérience en gestion des stocks, dont l'inventaire de 800 références.", n:'une durée et un chiffre'},
         '2b':{w:["J'ai quatre ans d'expérience auprès de personnes âgées, dans une résidence de 60 chambres."], say:"J'ai quatre ans d'expérience auprès de personnes âgées, dans une résidence de 60 chambres.", n:'toujours un chiffre'},
         '3a':{w:["Je demeure disponible pour vous rencontrer et vous remercie de l'attention portée à ma demande."], say:"Je demeure disponible pour vous rencontrer et vous remercie de l'attention portée à ma demande.", n:'figé : à recopier'},
         '3b':{w:["Je demeure disponible pour vous rencontrer et vous remercie de l'attention portée à ma demande."], say:"Je demeure disponible pour vous rencontrer et vous remercie de l'attention portée à ma demande.", n:'la même, quel que soit le poste'},
       },
       note:"Remarquez : seul le paragraphe 2 change vraiment d'un poste à l'autre. Le reste est un moule."},

      {t:'ex', h:"Les formules à recopier telles quelles",
       p:"Six expressions figées de la lettre professionnelle.",
       rows:[
         ["Madame, Monsieur,","l'appel, quand on ne connaît pas le nom"],
         ["Je vous soumets ma candidature au poste de…","pourquoi j'écris"],
         ["Fort de six ans d'expérience, je…","une entrée en matière soutenue"],
         ["Je demeure disponible pour vous rencontrer.","ce que je demande"],
         ["Je vous remercie de l'attention portée à ma demande.","le remerciement"],
         ["Veuillez agréer, Madame, Monsieur, mes salutations distinguées.","la sortie"],
       ]},

      {t:'piege', h:"Trois pièges à connaître",
       rows:[
         ["commencer par « Bonjour »","commencer par « Madame, Monsieur, »",
          "« Bonjour » convient à un courriel entre collègues, pas à une candidature. La première ligne est la première impression."],
         ["raconter toute sa vie","une demi-page, trois paragraphes",
          "Une lettre longue n'est pas lue jusqu'au bout. Un employeur qui reçoit quarante candidatures accorde trente secondes à chacune."],
         ["oublier le titre exact du poste","le recopier mot pour mot depuis l'offre",
          "Beaucoup d'entreprises affichent plusieurs postes. Sans le titre, votre lettre ne peut pas être classée — et une lettre non classée n'est pas lue."],
       ]},

      {t:'check', h:"Est-ce que c'est clair maintenant ?",
       p:"Quatre questions rapides.",
       qs:[
         {q:"On commence une lettre de motivation par…", opts:["Bonjour,","Madame, Monsieur,"], ok:1,
          fb:"C'est l'appel professionnel standard."},
         {q:"Combien de paragraphes ?", opts:["trois","six"], ok:0,
          fb:"Pourquoi j'écris, ce que j'apporte, ce que je demande."},
         {q:"Dans le paragraphe 2, il faut absolument…", opts:["un chiffre","une excuse"], ok:0,
          fb:"Un chiffre transforme une affirmation en preuve."},
         {q:"La formule de sortie doit reprendre…", opts:["l'appel du début","le nom de l'entreprise"], ok:0,
          fb:"« Madame, Monsieur » au début, « Madame, Monsieur » à la fin."},
       ]},
    ]
  },

  t3subj: {
    eye:'Mini-leçon', tit:"Le subjonctif présent : quand le verbe d'avant l'exige",
    blocs:[
      {t:'texte', h:"Un changement de forme, pas un changement de sens",
       p:"« Je sais que vous <b>êtes</b> occupé » et « J'aimerais que vous <b>soyez</b> disponible » parlent du même verbe <i>être</i>. Ce qui change la forme, ce n'est pas le sens de la phrase : c'est le verbe qui vient <b>avant le que</b>. Certains verbes obligent le subjonctif, d'autres non. Il n'y a pas de raison à chercher — il y a une liste à retenir.",
       note:"À ce niveau, on n'a pas besoin de tous les cas. Six verbes couvrent presque tout ce qu'on dit en entrevue."},

      {t:'ana', h:"Les verbes qui obligent le subjonctif",
       p:"Ils expriment une volonté, un souhait ou une nécessité.",
       mots:[['La liste','vouloir que · aimer que · souhaiter que · préférer que · exiger que'],['Et surtout','{il faut que}',true],['Un exemple','{Il faut que} je {sois} disponible dès lundi.']],
       say:"Il faut que je sois disponible dès lundi.",
       note:"Retenez-les avec leur <i>que</i> collé : « il faut que », « j'aimerais que ». Le <i>que</i> fait partie du signal."},

      {t:'ana', h:"Les quatre irréguliers du monde du travail",
       p:"Ce sont ceux qu'on emploie le plus, et ils sont irréguliers. Apprenez-les tels quels.",
       mots:[['être','que je {sois} · que vous {soyez}'],['avoir','que j\'{aie} · que vous {ayez}'],['savoir','que vous {sachiez}',true],['pouvoir','que je {puisse} · que l\'équipe {puisse}']],
       say:"J'aimerais que vous sachiez que j'ai six ans d'expérience.",
       note:"« J'aimerais que vous sachiez… » est une des phrases les plus utiles d'une entrevue : elle sert à placer une information qu'on ne vous a pas demandée."},

      {t:'ana', h:"Les réguliers : une recette en trois gestes",
       p:"Presque tous les autres verbes suivent cette recette.",
       mots:[['On part de « ils » au présent','ils travaill{ent}'],['On enlève -ent','travaill-'],['On ajoute la terminaison','que je travaill{e}',true]],
       say:"Il faut que je travaille le samedi.",
       note:"Les terminaisons sont <b>-e, -es, -e, -ions, -iez, -ent</b>. À l'oral, trois d'entre elles ne s'entendent pas : le subjonctif est plus facile à parler qu'à écrire."},

      {t:'labo', h:"Placez votre phrase d'entrevue",
       p:"Choisissez ce que vous voulez dire et avec quel verbe.",
       axes:[
         {id:'d', lbl:'Le verbe de départ', opts:[['a','J\'aimerais que'],['b','Il faut que'],['c','Je souhaite que']]},
         {id:'s', lbl:'La suite', opts:[['1','vous / savoir'],['2','je / être disponible'],['3','l\'équipe / pouvoir compter sur moi']]}],
       out:{
         a1:{w:["J'aimerais que vous sachiez que j'ai six ans d'expérience."], say:"J'aimerais que vous sachiez que j'ai six ans d'expérience.", n:'placer une information non demandée'},
         a2:{w:["J'aimerais être disponible dès lundi."], say:"J'aimerais être disponible dès lundi.", n:'même sujet des deux côtés : pas de « que », un infinitif'},
         a3:{w:["J'aimerais que l'équipe puisse compter sur moi."], say:"J'aimerais que l'équipe puisse compter sur moi.", n:'pouvoir → puisse'},
         b1:{w:["Il faut que vous sachiez que je fais répéter si je n'ai pas compris."], say:"Il faut que vous sachiez que je fais répéter si je n'ai pas compris.", n:'un peu direct, mais correct'},
         b2:{w:["Il faut que je sois disponible dès lundi."], say:"Il faut que je sois disponible dès lundi.", n:'être → sois'},
         b3:{w:["Il faut que l'équipe puisse compter sur moi."], say:"Il faut que l'équipe puisse compter sur moi.", n:'la nécessité'},
         c1:{w:["Je souhaite que vous sachiez que je connais ce logiciel."], say:"Je souhaite que vous sachiez que je connais ce logiciel.", n:'savoir → sachiez'},
         c2:{w:["Je souhaite être disponible à temps plein."], say:"Je souhaite être disponible à temps plein.", n:'même sujet : infinitif, sans « que »'},
         c3:{w:["Je souhaite que l'équipe puisse compter sur moi."], say:"Je souhaite que l'équipe puisse compter sur moi.", n:'la formule de fin d\'entrevue'},
       },
       note:"Regardez les deux cases où le « que » disparaît : quand le sujet est le même des deux côtés, on emploie l'infinitif. C'est plus simple, et c'est ce qu'on dit vraiment."},

      {t:'ex', h:"Six phrases d'entrevue au subjonctif",
       p:"Toutes s'emploient telles quelles.",
       rows:[
         ["J'aimerais que vous sachiez que j'ai déjà utilisé un logiciel semblable.","savoir → sachiez"],
         ["Il faut que je sois honnête : je ne connais pas encore le vôtre.","être → sois"],
         ["Je souhaite que l'équipe puisse compter sur moi.","pouvoir → puisse"],
         ["L'employeur exige que chaque commis ait deux ans d'expérience.","avoir → ait"],
         ["Je préfère qu'on me répète une consigne plutôt que de me tromper.","répéter → répète"],
         ["J'espère que ma candidature vous intéresse.","espérer : pas de subjonctif !"],
       ]},

      {t:'piege', h:"Trois pièges à connaître",
       rows:[
         ["« J'espère que vous soyez bien »","« J'espère que vous allez bien »",
          "<i>Espérer</i> ressemble à <i>souhaiter</i>, mais ne prend pas le subjonctif. C'est le piège numéro un des lettres de motivation, et il se voit à la première ligne."],
         ["« Je veux que je sois disponible »","« Je veux être disponible »",
          "Quand le sujet est le même des deux côtés du <i>que</i>, on n'emploie pas de subordonnée : on met l'infinitif, sans <i>que</i>."],
         ["« il faut que je suis »","« il faut que je sois »",
          "<i>Être</i> est irrégulier au subjonctif et c'est le verbe le plus fréquent de la langue. Si vous n'en retenez qu'un, retenez celui-là."],
       ]},

      {t:'check', h:"Est-ce que c'est clair maintenant ?",
       p:"Quatre questions rapides.",
       qs:[
         {q:"« Il faut que je ___ disponible. »", opts:["suis","sois"], ok:1,
          fb:"Après « il faut que », être devient « sois »."},
         {q:"« J'espère que ma candidature vous ___ . »", opts:["intéresse","intéressât"], ok:0,
          fb:"Espérer ne demande pas le subjonctif : c'est l'indicatif ordinaire."},
         {q:"« J'aimerais que vous ___ que je parle espagnol. »", opts:["savez","sachiez"], ok:1,
          fb:"Savoir → que vous sachiez."},
         {q:"« Je veux ___ à l'heure. » (même sujet)", opts:["que je sois","être"], ok:1,
          fb:"Même sujet des deux côtés : infinitif, sans « que »."},
       ]},
    ]
  },

  t3conn: {
    eye:'Mini-leçon', tit:"Les cinq mots qui font vivre une réponse",
    blocs:[
      {t:'texte', h:"« Parlez-moi de votre expérience » n'appelle pas une phrase",
       p:"En entrevue, la question est ouverte et la réponse attendue fait trois ou quatre phrases. Mais on ne développe pas en parlant plus longtemps : on développe en <b>donnant un exemple</b>. Cinq mots servent à l'annoncer — <i>par exemple, notamment, entre autres, c'est-à-dire, ainsi</i> — et chacun d'eux prévient l'employeur que ce qui suit est du concret.",
       note:"On les appelle des <b>connecteurs</b> : des mots qui relient deux idées en disant quel lien les unit."},

      {t:'ana', h:"par exemple — le plus courant",
       p:"Il annonce un cas parmi plusieurs. À l'oral comme à l'écrit.",
       mots:[['L\'idée générale','Je faisais plusieurs tâches,'],['Le connecteur','{par exemple}',true],['Le cas','recevoir les livraisons.']],
       say:"Je faisais plusieurs tâches, par exemple recevoir les livraisons.",
       note:"Si vous n'en retenez qu'un, retenez celui-là : il ne se trompe jamais de contexte."},

      {t:'ana', h:"notamment — un peu plus soutenu",
       p:"Il souligne un cas particulièrement important parmi les autres.",
       mots:[['L\'idée générale','Je préparais les commandes,'],['Le connecteur','{notamment}',true],['Le cas mis en avant','celles qui partaient le lendemain.']],
       say:"Je préparais les commandes, notamment celles qui partaient le lendemain.",
       note:"<i>Notamment</i> fait bon effet en entrevue : il montre qu'on sait hiérarchiser."},

      {t:'ana', h:"entre autres — il y en a d'autres",
       p:"Il annonce qu'on ne nommera pas tout.",
       mots:[['L\'idée','Une entreprise comparable à la vôtre,'],['Le connecteur','{entre autres}',true],['Le point retenu','par la taille.']],
       say:"Une entreprise comparable à la vôtre, entre autres par la taille.",
       note:"Il se place aussi en fin de phrase : <i>Je m'occupais des commandes et des livraisons, entre autres.</i>"},

      {t:'ana', h:"c'est-à-dire — expliquer, pas illustrer",
       p:"Celui-là n'ajoute pas d'exemple : il reformule ce qu'on vient de dire.",
       mots:[['Le mot difficile','Je signalais les écarts,'],['Le connecteur','{c\'est-à-dire}',true],['L\'explication','les différences entre le papier et la tablette.']],
       say:"Je signalais les écarts, c'est-à-dire les différences entre le papier et la tablette.",
       note:"Très utile quand vous employez un mot technique dont vous n'êtes pas sûr : vous l'expliquez tout de suite, et l'employeur voit que vous le maîtrisez."},

      {t:'ana', h:"ainsi — la conséquence",
       p:"Il annonce ce que l'action a donné.",
       mots:[['Ce que j\'ai fait','J\'ai vérifié tous les bons de réception ;'],['Le connecteur','{ainsi}',true],['Le résultat','j\'ai trouvé l\'erreur du fournisseur.']],
       say:"J'ai vérifié tous les bons de réception ; ainsi, j'ai trouvé l'erreur du fournisseur.",
       note:"C'est le connecteur qui termine bien une réponse : il donne le résultat, et le résultat est ce dont l'employeur se souvient."},

      {t:'labo', h:"Développez la réponse",
       p:"Choisissez ce que vous racontez et le lien à marquer.",
       axes:[
         {id:'r', lbl:'Vous racontez…', opts:[['a','vos tâches'],['b','un problème réglé'],['c','un mot technique']]},
         {id:'c', lbl:'Quel lien ?', opts:[['1','un exemple'],['2','une explication'],['3','un résultat']]}],
       out:{
         a1:{w:["Je faisais plusieurs tâches, par exemple recevoir les livraisons."], say:"Je faisais plusieurs tâches, par exemple recevoir les livraisons.", n:'un cas parmi d\'autres'},
         a2:{w:["Je tenais l'inventaire, c'est-à-dire que je comptais et j'entrais les quantités."], say:"Je tenais l'inventaire, c'est-à-dire que je comptais et j'entrais les quantités.", n:'on explique le mot'},
         a3:{w:["J'entrais tout le jour même ; ainsi, les chiffres étaient toujours à jour."], say:"J'entrais tout le jour même ; ainsi, les chiffres étaient toujours à jour.", n:'le résultat de la méthode'},
         b1:{w:["J'ai déjà réglé des problèmes de stock, par exemple une livraison incomplète."], say:"J'ai déjà réglé des problèmes de stock, par exemple une livraison incomplète.", n:'l\'exemple ouvre l\'histoire'},
         b2:{w:["Il manquait trois cents pieds de planches, c'est-à-dire presque une palette entière."], say:"Il manquait trois cents pieds de planches, c'est-à-dire presque une palette entière.", n:'on traduit le chiffre'},
         b3:{w:["J'ai remonté tous les bons ; ainsi, le fournisseur nous a remboursés."], say:"J'ai remonté tous les bons ; ainsi, le fournisseur nous a remboursés.", n:'la fin qu\'on retient'},
         c1:{w:["Je connais les logiciels d'inventaire, notamment celui de mon ancien employeur."], say:"Je connais les logiciels d'inventaire, notamment celui de mon ancien employeur.", n:'un cas mis en avant'},
         c2:{w:["Je faisais la réception, c'est-à-dire la vérification des livraisons à l'arrivée."], say:"Je faisais la réception, c'est-à-dire la vérification des livraisons à l'arrivée.", n:'le réflexe qui rassure'},
         c3:{w:["J'ai appris seule ; ainsi, je sais qu'un logiciel s'apprend vite."], say:"J'ai appris seule ; ainsi, je sais qu'un logiciel s'apprend vite.", n:'le résultat sert d\'argument'},
       },
       note:"Neuf réponses. Toutes font trois lignes au lieu d'une, et aucune n'a demandé de vocabulaire nouveau."},

      {t:'ex', h:"Six réponses développées",
       p:"Chacune emploie un connecteur.",
       rows:[
         ["J'ai fait plusieurs métiers, par exemple la réception de marchandise.","un cas"],
         ["Je m'occupais des commandes, notamment des commandes urgentes.","un cas important"],
         ["L'entreprise ressemblait à la vôtre, entre autres par la taille.","il y en a d'autres"],
         ["Je faisais l'inventaire, c'est-à-dire le compte réel des produits.","une explication"],
         ["J'ai tout revérifié ; ainsi, nous avons récupéré l'argent.","un résultat"],
         ["Je suis rigoureuse ; par exemple, je note toujours les écarts le jour même.","la preuve d'une qualité"],
       ]},

      {t:'piege', h:"Trois pièges à connaître",
       rows:[
         ["employer « c'est-à-dire » pour donner un exemple","« c'est-à-dire » explique, « par exemple » illustre",
          "Après <i>c'est-à-dire</i>, on redit la même chose autrement. Après <i>par exemple</i>, on donne un cas nouveau. Les confondre embrouille l'auditeur."],
         ["annoncer un exemple et ne pas le donner","chaque connecteur doit être suivi de son contenu",
          "« Je faisais plusieurs tâches, par exemple… » et rien ensuite : c'est pire que de n'avoir rien annoncé. Ne lancez le connecteur que si l'exemple est prêt."],
         ["mettre cinq connecteurs dans une réponse","un ou deux suffisent",
          "Une réponse de quatre phrases porte un connecteur, deux au maximum. Au-delà, le discours a l'air récité."],
       ]},

      {t:'check', h:"Est-ce que c'est clair maintenant ?",
       p:"Quatre questions rapides.",
       qs:[
         {q:"Pour donner un cas nouveau, on dit…", opts:["par exemple","c'est-à-dire"], ok:0,
          fb:"« c'est-à-dire » explique, il n'illustre pas."},
         {q:"Pour reformuler un mot technique, on dit…", opts:["ainsi","c'est-à-dire"], ok:1,
          fb:"C'est exactement son rôle."},
         {q:"Pour annoncer le résultat d'une action, on dit…", opts:["ainsi","entre autres"], ok:0,
          fb:"« ainsi » introduit la conséquence."},
         {q:"Dans une réponse de quatre phrases, il faut…", opts:["un ou deux connecteurs","cinq connecteurs"], ok:0,
          fb:"Au-delà, la réponse a l'air apprise par cœur."},
       ]},
    ]
  },
};
