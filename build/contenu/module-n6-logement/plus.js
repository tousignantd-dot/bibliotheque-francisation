const PLUS = {

  prGraphie: {
    eye:'Mini-leçon', tit:'Quand la lettre ment sur le son',
    blocs:[
      {t:'texte', h:"Le jour où l'orthographe vous fait perdre une heure",
       p:"Vous entendez un mot au téléphone, dans un bureau, à la radio. Vous voulez le retrouver ensuite : vous le tapez comme vous l'avez entendu, et rien ne sort. Ce n'est pas votre oreille qui a failli, c'est l'orthographe qui n'a pas suivi la prononciation. Trois groupes de lettres font ce coup-là, et ce sont toujours les mêmes.",
       note:"Le programme du niveau 6 les nomme un par un dans sa rubrique de graphie-phonie : le son k écrit ch, le son s écrit x, le son de « chat » écrit sh ou sch."},

      {t:'ana', h:"CH qui se dit K — les mots venus du grec",
       p:"Ce sont des mots d'étude, de science et de musique. Ils sont arrivés en français par le grec, et le grec écrivait cette lettre-là.",
       mots:[['On lit','une {ch}orale · la te{ch}nologie · un psy{ch}ologue · le {ch}aos'],
             ['On entend','[k] — « co-rale », « psi-cologue »', true],
             ['Le repère','un mot d\'école ou de science, souvent avec un y quelque part']],
       say:"une chorale, la technologie, un psychologue, le chaos",
       note:"Ne cherchez pas de règle : « chercher », « chaque », « chambre », « chauffage » gardent le son ordinaire. Le k est l'exception, et elle s'apprend mot par mot."},

      {t:'ana', h:"X qui se dit S — les nombres, presque uniquement",
       p:"Le x français a plusieurs vies : dans « taxi » il se dit ks, dans « deuxième » il se dit z, et dans quelques nombres il se dit tout simplement s.",
       mots:[['On lit','di{x}-huit · soi{x}ante-quinze · si{x} · di{x}'],
             ['On entend','[s] — « di-suit », « soi-sante-quinze »', true],
             ['Ce qui suit décide','seul : on entend le s · devant une consonne : il se tait · devant une voyelle : il se lie']],
       say:"dix-huit, soixante-quinze, six mois, dix jours",
       note:"« Dix jours » se dit « di jours ». « Dix ans » se dit « diz ans ». Les trois formes du même mot se comprennent : personne ne vous reprendra là-dessus."},

      {t:'ana', h:"SH et SCH qui se disent comme dans « chat »",
       p:"Des mots empruntés à d'autres langues et entrés tels quels dans le français d'ici. Ils gardent leur orthographe d'origine et prennent notre prononciation.",
       mots:[['On lit','un {sch}éma · un {s}u{sh}i · un fla{sh} · un t-{sh}irt'],
             ['On entend','le son de « chat », un seul son', true],
             ['Le repère','un mot court, venu d\'ailleurs, souvent récent']],
       say:"un schéma, un sushi, un flash, un t-shirt",
       note:"Le piège n'est pas l'orthographe, c'est l'anglais : beaucoup de ces mots existent aussi en anglais, et l'habitude tire vers la prononciation anglaise. En français, la bouche reste au même endroit que dans « chercher »."},

      {t:'labo', h:'Écoutez, puis répétez',
       p:"Choisissez un groupe de lettres, puis un mot.",
       axes:[
         {id:'g', lbl:'Quel groupe ?', opts:[['k','ch qui dit K'],['s','x qui dit S'],['h','sh et sch']]},
         {id:'n', lbl:'Quel mot ?', opts:[['1','le premier'],['2','le second']]}],
       out:{
         k1:{w:["une chorale"], say:"une chorale", n:'« co-rale » : le ch tombe, le k reste'},
         k2:{w:["un psychologue"], say:"un psychologue", n:'« psi-co-logue » : deux pièges dans le même mot'},
         s1:{w:["dix-huit"], say:"dix-huit", n:'« di-suit » : le x se colle à la voyelle qui suit'},
         s2:{w:["soixante-quinze"], say:"soixante-quinze", n:'« soi-sante » : jamais de k au milieu'},
         h1:{w:["un schéma"], say:"un schéma", n:'trois lettres, un seul son'},
         h2:{w:["un flash"], say:"un flash", n:'la voyelle est française : « fla-che », pas « flæsh »'},
       },
       note:"Écoutez deux fois avant d'ouvrir la bouche. Ce qui se travaille ici est l'oreille ; la bouche suit toute seule."},

      {t:'ex', h:'Huit mots, écrits et dits',
       p:"À gauche ce que vous lisez, à droite ce que vous entendez.",
       rows:[
         ["une chorale","« co-rale » — le ch fait k"],
         ["la technologie","« tec-nologie » — le ch fait k"],
         ["un psychologue","« psi-cologue » — le ch fait k"],
         ["le chaos","« ca-o » — le ch fait k et le s se tait"],
         ["dix-huit","« di-suit » — le x fait s"],
         ["soixante-quinze","« soi-sante-quinze » — le x fait s"],
         ["un schéma","« ché-ma » — sch fait ch"],
         ["un sushi","« sou-chi » — sh fait ch"],
       ]},

      {t:'check', h:'Quatre questions, une minute',
       p:"Sans revenir en arrière.",
       qs:[
         {q:"Dans « psychologue », les lettres ch se disent…", opts:["comme dans chat","comme un k"], ok:1,
          fb:"Mot venu du grec : « psi-co-logue »."},
         {q:"Le x de « dix-huit » sonne…", opts:["comme un s","comme un ks"], ok:0,
          fb:"« Di-suit ». Le x se lie à la voyelle du mot suivant."},
         {q:"« Un schéma » commence par…", opts:["le son de chat","le son sk"], ok:0,
          fb:"Les trois lettres se ramassent en un seul son."},
         {q:"« Dix jours » se dit…", opts:["« di jours »","« diss jours »"], ok:0,
          fb:"Devant une consonne, le x se tait complètement."},
       ]},

      {t:'piege', h:'Trois ennuis courants, trois sorties',
       rows:[
         ["chercher un mot avec la mauvaise orthographe","essayer ch à la place de k",
          "Vous entendez « tecnologie » et vous cherchez « tecnologie » : rien. Devant un son k qui ne se trouve pas, essayez systématiquement ch."],
         ["prononcer tous les ch comme dans chat","repérer les mots d'école",
          "« Psychologue » dit avec le son de chat ne se comprend pas. Ces mots-là sont peu nombreux, et ce sont presque toujours des mots d'étude."],
         ["dire les emprunts à l'anglaise","garder la bouche du français",
          "« Un t-shirt » et « un flash » sont français depuis longtemps. La voyelle se dit à la française : « ti-cheurt », « fla-che »."],
       ]},

      {t:'revoir', h:'À retenir',
       p:"Trois cas, et rien d'autre : <b>ch</b> qui dit k dans les mots d'étude (chorale, technologie, psychologue, chaos), <b>x</b> qui dit s dans les nombres (dix-huit, soixante-quinze), <b>sh</b> et <b>sch</b> qui disent ch dans les emprunts (schéma, sushi, flash, t-shirt)."},
    ]
  },

  prDeux: {
    eye:'Mini-leçon', tit:'Sous-louer, céder, résilier : trois portes différentes',
    blocs:[
      {t:'texte', h:"Le mot que vous employez décide de ce qui vous arrive",
       p:"Les trois mots parlent du même moment de la vie : vous ne pouvez plus, ou ne voulez plus, occuper votre logement jusqu'au bout du bail. Ils ne mènent pourtant pas au même endroit, et le choix ne se rattrape pas facilement. Employer le mauvais mot dans un avis écrit, c'est demander une chose en croyant en demander une autre.",
       note:"Le savoir lexical de la situation, au niveau 6, nomme les trois : résiliation, cession, sous-location. C'est le seul endroit du programme où ces mots figurent."},

      {t:'ana', h:"Sous-louer : je prête, et je garde",
       p:"Vous confiez votre logement à quelqu'un pour une période qui a une fin. Votre bail ne bouge pas.",
       mots:[['Qui reste au bail','vous, du premier au dernier jour'],
             ['Qui doit le loyer au locateur','vous — le sous-locataire vous doit le loyer, à vous', true],
             ['Quand ça finit','à la date écrite dans votre entente, et vous revenez'],
             ['Le risque','si le sous-locataire abîme ou ne paie pas, c\'est vous qu\'on ira voir']],
       say:"sous-louer, je prête mon logement et je garde mon bail",
       note:"C'est la porte de ceux qui partent pour un temps : un contrat ailleurs, une formation, une année aux études, un retour au pays."},

      {t:'ana', h:"Céder son bail : je transmets, et je sors",
       p:"Une autre personne prend votre place au bail. Elle continue le contrat tel quel, au même prix, jusqu'à la même date.",
       mots:[['Qui reste au bail','l\'autre personne — vous, vous en sortez'],
             ['Qui doit le loyer au locateur','la personne à qui vous avez cédé', true],
             ['Quand ça finit','ça ne finit pas pour vous : vous êtes parti pour de bon'],
             ['Le risque','se tromper de porte : une cession ne se reprend pas en juillet']],
       say:"céder son bail, je transmets le contrat et je sors du dossier",
       note:"C'est la porte de ceux qui déménagent définitivement avant la fin de leur bail."},

      {t:'ana', h:"Résilier : je mets fin, et la loi encadre",
       p:"Mettre fin au bail avant son terme n'est pas une décision libre. La loi ne le permet que dans des situations précises, et il faut passer par un avis en bonne et due forme.",
       mots:[['Qui reste au bail','personne : le bail s\'éteint'],
             ['Ce que ça demande','une des situations prévues par la loi, et un avis écrit', true],
             ['Ce que ce n\'est pas','« j\'ai trouvé mieux ailleurs » n\'est pas un motif de résiliation'],
             ['Où se renseigner','au service de renseignements du Tribunal, avant d\'écrire quoi que ce soit']],
       say:"résilier, je mets fin au bail dans les cas que la loi prévoit",
       note:"Ce module ne traite pas la résiliation en détail : le mot est là pour que vous ne le confondiez pas avec les deux autres."},

      {t:'ex', h:'La même situation, trois issues',
       p:"À gauche ce que la personne veut, à droite la porte qui lui convient.",
       rows:[
         ["Je pars six mois et je reviens","sous-location"],
         ["Je déménage à Rimouski pour de bon en février","cession de bail"],
         ["Je veux garder mon loyer bas pour l'an prochain","sous-location"],
         ["Ma sœur prendra le logement à ma place jusqu'à la fin","cession de bail"],
         ["Je ne veux plus être responsable de rien","cession de bail"],
         ["J'accepte de répondre si l'autre ne paie pas","sous-location"],
         ["Je pars aux études une session, puis je rentre","sous-location"],
         ["Je quitte le Québec en mars et je ne reviens pas","cession de bail"],
       ]},

      {t:'piege', h:'Deux confusions qui coûtent cher',
       rows:[
         ["croire qu'on est libéré parce qu'on a sous-loué","relire la ligne des obligations",
          "La sous-location ne vous enlève rien. Le locateur ne connaît que vous : il vous réclamera le loyer impayé, et c'est ensuite à vous de vous retourner vers votre sous-locataire."],
         ["écrire « je veux céder mon bail » en pensant sous-louer","choisir le mot avant d'écrire l'avis",
          "L'avis fait courir un délai et engage une démarche. Un avis de cession ne demande pas la même chose qu'un avis de sous-location, et la réponse ne sera pas la même non plus."],
         ["croire que déménager suffit à résilier","téléphoner avant d'annoncer quoi que ce soit",
          "Un déménagement pour convenance personnelle ne met pas fin à un bail. Beaucoup de gens l'apprennent après avoir déjà donné leur parole ailleurs."],
       ]},

      {t:'check', h:'Trois questions',
       qs:[
         {q:"Farida part six mois et revient le 1er juillet. Elle doit…", opts:["céder son bail","sous-louer"], ok:1,
          fb:"Elle veut reprendre son logement : la cession ne le lui permettrait pas."},
         {q:"Pendant une sous-location, qui doit le loyer au locateur ?", opts:["le sous-locataire","le locataire de départ"], ok:1,
          fb:"Le locateur ne connaît que son locataire. Le sous-locataire, lui, doit le loyer au locataire."},
         {q:"Une cession de bail…", opts:["a une date de retour","n'a pas de retour prévu"], ok:1,
          fb:"Celui qui cède sort du contrat pour de bon."},
       ]},

      {t:'revoir', h:'À retenir',
       p:"Une seule question à se poser : <b>après, qui est encore au bail ?</b> Vous → sous-location. L'autre personne → cession. Personne → résiliation."},
    ]
  },

  prMots: {
    eye:'Mini-leçon', tit:'Le verbe caché sous le nom',
    blocs:[
      {t:'texte', h:"Pourquoi les textes de logement sont si secs",
       p:"« La reconduction du bail s'effectue de plein droit. » En parlant, on dirait : « le bail continue tout seul ». Même chose, deux habits. Un texte de droit préfère les noms parce qu'un nom se numérote, se cite et se met en titre. Le lecteur, lui, a besoin de refaire le chemin à l'envers : trouver le verbe sous le nom, et la phrase redevient simple.",
       note:"Le programme demande d'employer préfixes et suffixes et d'exploiter les familles de mots pour la nominalisation. C'est exactement ce travail-là."},

      {t:'ana', h:"Le suffixe -tion : l'action devenue chose",
       p:"Le plus fréquent dans un texte administratif. Il transforme un verbe en nom d'action.",
       mots:[['louer','la <b>location</b> du logement'],
             ['sous-louer','la <b>sous-location</b> du 5 janvier au 28 juin'],
             ['résilier','la <b>résiliation</b> du bail', true],
             ['occuper','l\'<b>occupation</b> des lieux']],
       say:"la location, la sous-location, la résiliation, l'occupation",
       note:"Ces noms sont tous féminins. C'est une règle qui ne se trompe presque jamais : un nom en -tion prend « la » ou « une »."},

      {t:'ana', h:"Le suffixe -ment : l'action, ou son résultat",
       p:"Le second par ordre de fréquence, et il donne des noms masculins.",
       mots:[['renouveler','le <b>renouvellement</b> du bail'],
             ['consentir','le <b>consentement</b> du locateur'],
             ['payer','le <b>paiement</b> du loyer', true],
             ['loger','un <b>logement</b> de quatre pièces et demie']],
       say:"le renouvellement, le consentement, le paiement, un logement",
       note:"Attention à l'orthographe de « paiement » : le i reste, contrairement au verbe « il paie » qui peut aussi s'écrire « il paye »."},

      {t:'ana', h:"Deux noms qui ne suivent aucune règle",
       p:"Ils reviennent partout dans ce dossier et ils s'apprennent tels quels.",
       mots:[['céder','la <b>cession</b> — et non « la cédation »'],
             ['indemniser','une <b>indemnité</b> — et non « une indemnisement »', true],
             ['Le préfixe sous-','louer → <b>sous</b>-louer : « en dessous de », donc « qui dépend de »'],
             ['Ce qu\'il change','un sous-locataire dépend du locataire, jamais directement du locateur']],
       say:"la cession, une indemnité, un sous-locataire",
       note:"« Cession » se prononce comme « session », et ce n'est pas le même mot du tout. Dans un écrit, le contexte suffit à les distinguer."},

      {t:'ex', h:'Ce qu\'on dit, ce qu\'on lit',
       p:"À gauche la phrase parlée, à droite la phrase du document.",
       rows:[
         ["le bail continue tout seul","la reconduction du bail"],
         ["il accepte","son consentement"],
         ["elle prête son logement six mois","la sous-location"],
         ["il passe son bail à quelqu'un","la cession du bail"],
         ["on met fin au bail","la résiliation du bail"],
         ["elle paie le premier du mois","le paiement du loyer"],
         ["il habitera là jusqu'en juin","l'occupation des lieux jusqu'en juin"],
         ["il veut être remboursé de ses frais","une indemnité pour ses dépenses"],
       ]},

      {t:'piege', h:'Trois faux pas',
       rows:[
         ["fabriquer un nom qui n'existe pas","employer le verbe",
          "On ne dit pas « une cédation » ni « un sous-louage ». En cas de doute, écrivez le verbe : « je veux sous-louer » est parfaitement clair, et personne ne vous reprochera une phrase simple."],
         ["confondre « location » et « sous-location »","lire le préfixe",
          "Dans un avis, écrire « location » à la place de « sous-location » change la nature de ce que vous demandez. Le préfixe n'est pas décoratif."],
         ["se tromper de genre","se fier au suffixe",
          "-tion appelle « la », -ment appelle « le ». « Le consentement », « la résiliation » : c'est mécanique, et ça évite la moitié des fautes d'accord."],
       ]},

      {t:'revoir', h:'À retenir',
       p:"Sous chaque nom d'un texte officiel, il y a un verbe. <b>-tion</b> et <b>-ment</b> en fabriquent la plupart ; <b>cession</b> et <b>indemnité</b> sont les deux irréguliers du dossier. Retrouver le verbe, c'est comprendre la phrase."},
    ]
  },

  t1vf: {
    eye:'Mini-leçon', tit:'Ce qu\'un service de renseignements peut faire pour vous',
    blocs:[
      {t:'texte', h:"Gratuit, anonyme, et il répond au téléphone",
       p:"Le Tribunal administratif du logement tient un service de renseignements. On y explique la règle, on y dit quel papier fait quoi, on y donne des délais. On n'y prend pas votre dossier en main et on n'y décide rien : ce sont deux choses différentes, et il vaut mieux le savoir avant d'appeler.",
       note:"Farida a téléphoné avant de parler à son locateur, et c'est ce qui a changé toute la conversation du Défi 2. Elle est arrivée avec des mots exacts et une date."},

      {t:'ana', h:"Ce qu'on peut demander",
       p:"Des questions de règle, posées sur une situation réelle.",
       mots:[['Une règle','« Est-ce que je dois aviser par écrit ? »'],
             ['Un délai','« À partir de quel jour comptent les quinze jours ? »', true],
             ['Un mot','« Quelle différence entre sous-louer et céder ? »'],
             ['Un papier','« Qu\'est-ce que je dois écrire dans mon avis ? »']],
       say:"une règle, un délai, un mot, un papier",
       note:"Préparez vos questions par écrit avant d'appeler. Trois questions notées valent mieux que dix questions qui viennent en parlant."},

      {t:'ana', h:"Ce qu'on ne peut pas demander",
       p:"Il y a une frontière, et le préposé la rappellera lui-même.",
       mots:[['Une décision','personne au téléphone ne tranchera votre cas'],
             ['Un conseil de stratégie','« Est-ce que je vais gagner ? » n\'a pas de réponse là', true],
             ['Une intervention','le service n\'appellera pas votre locateur à votre place'],
             ['Un document rédigé','on vous dit ce qu\'un avis doit contenir, pas ce qu\'il doit dire de vous']],
       say:"une décision, un conseil, une intervention, un document",
       note:"Ce n'est pas de la mauvaise volonté : le même organisme tranche les litiges. Il ne peut pas conseiller une partie et juger l'autre."},

      {t:'ex', h:'Quatre questions bien posées',
       p:"À gauche la question vague, à droite la même, précise.",
       rows:[
         ["Est-ce que j'ai le droit de sous-louer ?","Je pars six mois et je reviens : est-ce que c'est une sous-location ?"],
         ["Il a combien de temps ?","Les quinze jours comptent à partir de quel jour, exactement ?"],
         ["Il peut refuser ?","Est-ce qu'un refus doit être écrit et motivé ?"],
         ["Il me demande de l'argent","Est-ce qu'il peut fixer un montant d'avance, ou seulement réclamer ses dépenses réelles ?"],
       ]},

      {t:'piege', h:'Deux erreurs de départ',
       rows:[
         ["appeler avant d'avoir un nom","trouver la personne d'abord",
          "Un avis sans nom ne fait courir aucun délai. Tant que vous n'avez trouvé personne, vous ne pouvez rien enclencher — et la réponse au téléphone restera générale."],
         ["prendre une explication pour une décision","noter ce qui est dit, et à quelle date",
          "Le préposé explique la règle. Ce n'est pas un jugement, et ça ne lie personne. Ce que ça vous donne, c'est de savoir de quoi vous parlez."],
       ]},

      {t:'revoir', h:'À retenir',
       p:"Un service de renseignements vous donne <b>la règle, les délais et les mots</b>. Il ne prend pas de décision, il n'écrit pas à votre place et il n'appelle pas votre locateur. Appelez avec vos questions notées, et notez ce qu'on vous répond."},
    ]
  },

  t1page: {
    eye:'Mini-leçon', tit:"Lire une page de droits sans s'y perdre",
    blocs:[
      {t:'texte', h:"Un texte qui ne parle de personne, et qui parle de vous",
       p:"Une fiche de droits est écrite pour des milliers de situations à la fois. Elle dit « le locataire », jamais « vous » ; elle dit « le cas échéant », « il est réputé », « de plein droit ». Cette langue-là n'est pas faite pour vous décourager : elle est faite pour être vraie dans tous les cas. Votre travail est de la traduire en une phrase qui commence par « moi, je ».",
       note:"C'est l'intention unique de la situation, au programme du niveau 6 : « s'informer sur ses droits et ses obligations en consultant un site Web »."},

      {t:'ana', h:"L'ordre est presque toujours le même",
       p:"Quatre morceaux, dans cet ordre. Le connaître fait gagner la moitié du temps de lecture.",
       mots:[['1. Ce que c\'est','une définition, et souvent la distinction avec ce qui lui ressemble'],
             ['2. Ce que vous devez faire','l\'action, la forme, le contenu obligatoire'],
             ['3. Le délai','le nombre de jours, et à partir de quand il court', true],
             ['4. Ce qui arrive après','le refus, les frais, les recours']],
       say:"la définition, l'obligation, le délai, la suite",
       note:"Le troisième morceau est celui qu'on saute quand on lit vite, et c'est le seul qui a une date. Commencez par lui si vous êtes pressé."},

      {t:'ana', h:"Quatre tournures à décoder",
       p:"Elles reviennent dans toutes les fiches, et chacune a une traduction simple.",
       mots:[['« est réputé avoir consenti »','la loi considère qu\'il a dit oui, même s\'il n\'a rien dit'],
             ['« doit faire connaître »','il est obligé de le dire, et de le dire à vous', true],
             ['« peut exiger »','il a le droit de demander — pas celui d\'obtenir n\'importe quoi'],
             ['« demeure tenu de »','ça reste sur vos épaules, malgré tout le reste']],
       say:"est réputé avoir consenti, doit faire connaître, peut exiger, demeure tenu de",
       note:"« Peut » et « doit » ne se lisent jamais assez lentement. Un texte de droits ne les emploie jamais l'un pour l'autre."},

      {t:'ex', h:'La fiche, traduite en « moi, je »',
       p:"À gauche la ligne de la page, à droite ce qu'elle veut dire pour Farida.",
       rows:[
         ["Le locataire doit aviser le locateur par écrit","Je dois écrire, pas seulement en parler"],
         ["L'avis indique le nom et l'adresse de la personne","Je dois avoir trouvé quelqu'un avant d'écrire"],
         ["Quinze jours à compter de la réception","Mon délai part du jour où il l'a eu en main"],
         ["Il est réputé avoir consenti","Son silence me dit oui"],
         ["Il ne peut refuser sans un motif sérieux","Un « je n'aime pas ça » ne tient pas"],
         ["Il doit faire connaître par écrit les motifs","J'ai droit à une réponse écrite qui explique"],
         ["Le remboursement des dépenses raisonnables","Ses frais réels, oui ; un montant inventé, non"],
         ["Le locataire demeure tenu de ses obligations","Je reste responsable du loyer, même à Sept-Îles"],
       ]},

      {t:'check', h:'Trois questions de lecture',
       qs:[
         {q:"Dans une fiche de droits, le délai se trouve le plus souvent…", opts:["au début","au milieu"], ok:1,
          fb:"Le début définit, la fin donne les recours. Le chiffre est entre les deux."},
         {q:"« Il est réputé avoir consenti » veut dire…", opts:["il a signé","son silence vaut oui"], ok:1,
          fb:"C'est la loi qui décide de la valeur du silence."},
         {q:"Une fiche officielle dit « vous »…", opts:["souvent","presque jamais"], ok:1,
          fb:"Elle dit « le locataire ». Traduisez-la vous-même en « moi, je »."},
       ]},

      {t:'piege', h:'Trois façons de mal lire une fiche',
       rows:[
         ["lire seulement le premier paragraphe","descendre jusqu'au délai",
          "Le premier paragraphe définit. Il ne dit jamais ce qu'il faut faire ni quand. C'est l'erreur que Gilles met en garde dès le premier dialogue."],
         ["prendre une page trouvée n'importe où pour une source","regarder qui écrit et depuis quand",
          "Une page de blogue, un forum, une vidéo peuvent avoir raison — ou dater d'avant un changement. La date de mise à jour et le nom de l'organisme sont la première chose à regarder."],
         ["croire que la fiche règle votre cas","téléphoner pour la partie qui vous concerne",
          "Une fiche donne la règle générale. Le cas particulier — le vôtre — se vérifie au téléphone, gratuitement."],
       ]},

      {t:'revoir', h:'À retenir',
       p:"Quatre morceaux : <b>ce que c'est · ce que je dois faire · le délai · ce qui arrive après</b>. Lisez les intertitres d'abord, l'encadré ensuite, le délai en troisième. Et traduisez chaque ligne en « moi, je »."},
    ]
  },

  t1mise: {
    eye:'Mini-leçon', tit:'Ce que la mise en page dit avant les mots',
    blocs:[
      {t:'texte', h:"On lit une page avant de la lire",
       p:"Avant même la première phrase, une page vous a déjà appris quatre choses : de quoi elle traite, quand elle a été écrite, combien d'étapes elle contient, et ce qu'elle juge le plus important. Tout cela se voit en trois secondes, sans lire un mot. C'est un savoir du programme au niveau 6, et c'est celui qui fait gagner le plus de temps.",
       note:"Le programme l'appelle « tenir compte de la présentation matérielle et de la mise en page ». Il vaut pour ce que vous lisez et pour ce que vous écrivez."},

      {t:'ana', h:"Les six repères d'une page Web officielle",
       p:"Ils sont presque toujours là, et toujours à la même place.",
       mots:[['Le titre, tout en haut','de quoi ça parle — et si vous êtes au bon endroit'],
             ['La date de mise à jour','si ce que vous lisez tient encore', true],
             ['Les intertitres numérotés','combien d\'étapes, et dans quel ordre'],
             ['Le gras','le mot exact à employer dans vos papiers'],
             ['L\'encadré','ce que l\'auteur ne veut surtout pas que vous manquiez'],
             ['Le lien souligné','qu\'une autre page traite le point plus au long']],
       say:"le titre, la date, les intertitres, le gras, l'encadré, le lien",
       note:"Le gras n'est pas une décoration : dans une fiche de droits, il marque les termes qui ont une valeur précise. Ce sont ceux à recopier tels quels dans un avis."},

      {t:'ana', h:"Les mêmes repères, quand c'est vous qui écrivez",
       p:"Un courriel bien découpé se lit en quinze secondes ; le même texte en un bloc se lit deux fois, ou pas du tout.",
       mots:[['Un objet','ce que votre titre est à la page : de quoi il s\'agit'],
             ['Un paragraphe par idée','trois idées, trois paragraphes, une ligne blanche entre eux', true],
             ['Une date par fait','« le 18 novembre », jamais « l\'autre jour »'],
             ['Une demande à la fin','le lecteur pressé lit le début et la fin']],
       say:"un objet, un paragraphe par idée, une date par fait, une demande à la fin",
       note:"C'est aussi la deuxième attente de fin de cours du niveau : « rédiger un court texte en organisant ses idées à l'aide de paragraphes »."},

      {t:'ex', h:'Le même contenu, deux mises en page',
       p:"À gauche ce qui décourage, à droite ce qui se lit.",
       rows:[
         ["un seul bloc de douze lignes","trois paragraphes séparés"],
         ["« bonjour j'ai une question »","un objet : « Avis de sous-location — logement 2 »"],
         ["« l'autre jour je vous ai parlé »","« le 18 novembre, je vous ai remis »"],
         ["la demande noyée au milieu","la demande seule, au dernier paragraphe"],
         ["tout au même niveau","les dates et les noms en gras"],
         ["aucune signature","le nom, le logement, le téléphone"],
       ]},

      {t:'piege', h:'Deux habitudes à défaire',
       rows:[
         ["commencer à lire par la première ligne","balayer les intertitres d'abord",
          "Trois secondes de survol donnent la carte du texte. Sans elle, vous lisez sans savoir où vous allez, et vous ne voyez pas venir le délai."],
         ["croire qu'un texte long est un texte sérieux","juger sur le découpage",
          "Un texte bien découpé est un texte dont l'auteur a réfléchi à ce qu'il voulait dire. Un bloc compact cache souvent une pensée en désordre — y compris la vôtre."],
       ]},

      {t:'revoir', h:'À retenir',
       p:"Six repères : <b>titre, date, intertitres, gras, encadré, lien</b>. Ils servent à lire vite, et ils servent à écrire clair — un objet, un paragraphe par idée, une date par fait, la demande à la fin."},
    ]
  },

  t1en: {
    eye:'Mini-leçon', tit:'« en » et « le » : ne pas tout redire',
    blocs:[
      {t:'texte', h:"Le mot le plus court est celui qui fait perdre le fil",
       p:"Un texte suivi ne répète pas ses mots : il les reprend. « Il en dispose », « elle le sait », « celui-ci doit ». Ces petits mots portent tout le sens de la phrase, et ils ne disent pas eux-mêmes à quoi ils renvoient. Savoir les rattacher, c'est la différence entre lire un texte et le suivre.",
       note:"Le programme appelle cela la reprise de l'information, et c'est l'un des trois savoirs de grammaire du texte qui distinguent le niveau 6 des niveaux plus bas."},

      {t:'ana', h:"« en » reprend ce qui vient après « de »",
       p:"Le verbe commande. Si le verbe demande « de », le pronom sera « en ».",
       mots:[['parler <b>de</b> quelque chose','La page parle du délai. → Elle <b>en</b> parle.'],
             ['avoir besoin <b>de</b>','Elle a besoin d\'une preuve. → Elle <b>en</b> a besoin.', true],
             ['disposer <b>de</b>','Il dispose de quinze jours. → Il <b>en</b> dispose.'],
             ['répondre <b>de</b>','Je réponds du loyer. → J\'<b>en</b> réponds.']],
       say:"elle en parle, elle en a besoin, il en dispose, j'en réponds",
       note:"« En » remplace des choses, pas des personnes. Pour une personne, on garde « de lui », « d'elle » : « je parle de lui »."},

      {t:'ana', h:"« le » reprend toute une idée",
       p:"Pas un objet : la phrase entière qui précède. C'est l'emploi que le niveau 6 demande.",
       mots:[['savoir','Le silence vaut consentement. Elle <b>le</b> sait.'],
             ['dire','Qu\'il doit écrire ? La page <b>le</b> dit deux fois.', true],
             ['ignorer','Que le délai court ? Il <b>l\'</b>ignorait.'],
             ['ce que ce n\'est pas','« Je le vois » où « le » = le papier : ça, c\'est l\'emploi ordinaire']],
       say:"elle le sait, la page le dit, il l'ignorait",
       note:"Le test : essayez de remplacer « le » par « cela ». Si la phrase tient, c'est bien une idée entière qui est reprise."},

      {t:'labo', h:'Choisissez le pronom',
       p:"Prenez un verbe, puis une reprise.",
       axes:[
         {id:'v', lbl:'Quel verbe ?', opts:[['a','parler de'],['b','savoir'],['c','avoir besoin de']]},
         {id:'f', lbl:'Quelle forme ?', opts:[['1','au présent'],['2','au passé composé']]}],
       out:{
         a1:{w:["elle en parle"], say:"elle en parle", n:'« parler de » → en, devant le verbe'},
         a2:{w:["elle en a parlé"], say:"elle en a parlé", n:'devant l\'auxiliaire, jamais devant le participe'},
         b1:{w:["elle le sait"], say:"elle le sait", n:'« le » reprend toute l\'idée d\'avant'},
         b2:{w:["elle l'a su"], say:"elle l'a su", n:'le devient l\' devant une voyelle'},
         c1:{w:["elle en a besoin"], say:"elle en a besoin", n:'« besoin de » → en'},
         c2:{w:["elle en a eu besoin"], say:"elle en a eu besoin", n:'en reste devant le premier verbe conjugué'},
       },
       note:"Le pronom se place devant le verbe conjugué, et aux temps composés devant l'auxiliaire. C'est la seule position possible en français."},

      {t:'ex', h:'Huit reprises du dossier',
       p:"À gauche la phrase complète, à droite la même sans répétition.",
       rows:[
         ["Il dispose de quinze jours.","Il en dispose."],
         ["Elle a besoin d'un accusé de réception.","Elle en a besoin."],
         ["Elle répond du paiement du loyer.","Elle en répond."],
         ["Nicolas a parlé de ses références.","Il en a parlé."],
         ["Elle sait que le silence vaut consentement.","Elle le sait."],
         ["La page dit que l'avis doit être écrit.","La page le dit."],
         ["Il ignorait que le délai courait déjà.","Il l'ignorait."],
         ["Elle a gardé une copie de chaque papier.","Elle en a gardé une."],
       ]},

      {t:'piege', h:'Trois erreurs, et leur remède',
       rows:[
         ["placer le pronom après le verbe","le mettre devant, toujours",
          "« Elle sait le » ne se dit pas. En français, le pronom passe devant le verbe conjugué : « elle le sait »."],
         ["employer « en » pour une personne","garder « de lui », « d'elle »",
          "« Je parle de monsieur Tardif » ne donne pas « j'en parle » mais « je parle de lui ». « En » est réservé aux choses."],
         ["placer le pronom devant le participe","le mettre devant l'auxiliaire",
          "« Elle a en parlé » est impossible. C'est « elle en a parlé » : le pronom colle au verbe conjugué, qui est l'auxiliaire."],
       ]},

      {t:'revoir', h:'À retenir',
       p:"Posez la question au verbe. <b>De quoi ?</b> → « en ». <b>Quoi, comme idée entière ?</b> → « le ». Et dans les deux cas, le pronom se place devant le verbe conjugué."},
    ]
  },

  t1ou: {
    eye:'Mini-leçon', tit:'« où » : un endroit, et aussi un moment',
    blocs:[
      {t:'texte', h:"Le mot qui recolle deux phrases",
       p:"« Le trois décembre est une date. Le délai finit ce jour-là. » Deux phrases courtes, un lecteur qui attend. « Le trois décembre est le jour où le délai finit » : une seule phrase, et l'information est liée. Les pronoms relatifs servent à cela, et « où » est celui que le programme du niveau 6 met en avant.",
       note:"Le savoir est écrit ainsi : « employer des phrases subordonnées relatives avec le pronom relatif où, complément de lieu ou de temps »."},

      {t:'ana', h:"« où » pour un lieu",
       p:"L'emploi que tout le monde connaît. Il remplace un complément de lieu.",
       mots:[['le quartier','Limoilou est le quartier <b>où</b> elle habite.'],
             ['l\'endroit','Le sous-sol est l\'endroit <b>où</b> se trouve la buanderie.', true],
             ['la ville','Sept-Îles est la ville <b>où</b> elle travaillera six mois.'],
             ['Le test','remplacez par « dans lequel », « à cet endroit » : si ça tient, c\'est « où »']],
       say:"le quartier où elle habite, l'endroit où se trouve la buanderie",
       note:"Après « le pays », « la rue », « l'immeuble », « la pièce » : toujours « où », jamais « que »."},

      {t:'ana', h:"« où » pour un moment",
       p:"C'est celui qu'on oublie, et c'est celui qui marque un texte soigné.",
       mots:[['le jour','Le trois décembre est le jour <b>où</b> le délai prend fin.'],
             ['l\'année','L\'année <b>où</b> elle est arrivée, elle ne parlait pas français.', true],
             ['le mois','Le mois <b>où</b> elle part est janvier.'],
             ['le moment','Le délai court à partir du moment <b>où</b> il reçoit l\'avis.']],
       say:"le jour où le délai prend fin, l'année où elle est arrivée",
       note:"« Le jour que je suis arrivée » s'entend beaucoup à l'oral. À l'écrit, dans un avis ou un courriel, écrivez « où » : c'est une des marques les plus visibles d'un texte tenu."},

      {t:'labo', h:'Qui, que ou où ?',
       p:"Prenez ce que le mot remplace, puis un exemple.",
       axes:[
         {id:'r', lbl:'Il remplace…', opts:[['q','le sujet'],['c','le complément direct'],['l','un lieu ou un moment']]},
         {id:'n', lbl:'Quel exemple ?', opts:[['1','le premier'],['2','le second']]}],
       out:{
         q1:{w:["le locateur qui refuse"], say:"le locateur qui refuse", n:'« il refuse » → qui'},
         q2:{w:["la page qui explique tout"], say:"la page qui explique tout", n:'« elle explique » → qui'},
         c1:{w:["l'avis qu'elle a remis"], say:"l'avis qu'elle a remis", n:'« elle l\'a remis » → que'},
         c2:{w:["la page qu'elle a lue"], say:"la page qu'elle a lue", n:'« elle l\'a lue » → que, et le participe s\'accorde'},
         l1:{w:["le quartier où elle habite"], say:"le quartier où elle habite", n:'un lieu → où'},
         l2:{w:["le jour où le délai finit"], say:"le jour où le délai finit", n:'un moment → où aussi'},
       },
       note:"Trois essais suffisent pour trancher : « il » → qui ; « le, la, les » → que ; « là, à ce moment-là » → où."},

      {t:'ex', h:'Deux phrases devenues une',
       p:"À gauche les deux phrases, à droite la phrase liée.",
       rows:[
         ["Limoilou est un quartier. Elle y habite.","Limoilou est le quartier où elle habite."],
         ["Le 3 décembre est une date. Le délai finit ce jour-là.","Le 3 décembre est le jour où le délai finit."],
         ["Voici un avis. Elle l'a remis le 18.","Voici l'avis qu'elle a remis le 18."],
         ["Un locateur refuse. Il doit écrire ses motifs.","Le locateur qui refuse doit écrire ses motifs."],
         ["Elle est arrivée cette année-là. Elle ne parlait pas français.","L'année où elle est arrivée, elle ne parlait pas français."],
         ["Le sous-sol est un endroit. La buanderie s'y trouve.","Le sous-sol est l'endroit où se trouve la buanderie."],
       ]},

      {t:'check', h:'Trois questions',
       qs:[
         {q:"« Le mois ___ elle part est janvier. »", opts:["que","où"], ok:1,
          fb:"Un moment : c'est « où », même si l'oreille dit autre chose."},
         {q:"« L'avis ___ elle a remis porte un nom. »", opts:["qu'","où"], ok:0,
          fb:"« Elle l'a remis » : complément direct, donc « que »."},
         {q:"« Le locateur ___ refuse doit écrire. »", opts:["qui","que"], ok:0,
          fb:"« Il refuse » : c'est le sujet, donc « qui »."},
       ]},

      {t:'revoir', h:'À retenir',
       p:"<b>où</b> rattache un lieu <i>et</i> un moment : le quartier où, le jour où, l'année où. <b>qui</b> remplace un sujet, <b>que</b> un complément direct. Trois essais — « il », « le », « là » — et le doute est levé."},
    ]
  },

  t1ps: {
    eye:'Mini-leçon', tit:'Le passé simple : le lire, jamais l\'écrire',
    blocs:[
      {t:'texte', h:"Un temps qu'on rencontre et qu'on n'emploie pas",
       p:"Personne, au Québec, ne dit « je pris le bail » ou « il fut créé ». Le passé simple ne se parle plus depuis longtemps. Il survit à l'écrit : dans les romans, les contes, les notices historiques, les encadrés « un peu d'histoire » que les sites officiels aiment beaucoup. Vous le rencontrerez donc en lisant, et seulement en lisant.",
       note:"Le programme du niveau 6 ne demande que deux choses : « reconnaître les verbes courants à la 3e personne » et « associer le passé simple au passé composé ». Rien sur la production."},

      {t:'ana', h:"Les terminaisons de la 3e personne",
       p:"Ce sont les seules à connaître : un texte au passé simple raconte, donc il parle de « il », « elle », « ils ».",
       mots:[['verbes en -er','il adopt<b>a</b> · ils adopt<b>èrent</b>'],
             ['verbes en -ir','il fin<b>it</b> · ils fin<b>irent</b>', true],
             ['beaucoup d\'autres','il reç<b>ut</b> · ils reç<b>urent</b> · il l<b>ut</b> · ils l<b>urent</b>'],
             ['venir et tenir','il v<b>int</b> · ils v<b>inrent</b> · il t<b>int</b> · ils t<b>inrent</b>']],
       say:"il adopta, il finit, il reçut, il vint",
       note:"Le pluriel se reconnaît toujours au groupe -rent à la fin. Si vous voyez -èrent, -irent, -urent, -inrent : c'est du passé simple, au pluriel."},

      {t:'ana', h:"Trois irréguliers qui sont partout",
       p:"Courts, étranges, et impossibles à confondre avec autre chose une fois qu'on les connaît.",
       mots:[['être','il <b>fut</b> · ils <b>furent</b> — « il a été »'],
             ['avoir','il <b>eut</b> · ils <b>eurent</b> — « il a eu »', true],
             ['faire','il <b>fit</b> · ils <b>firent</b> — « il a fait »'],
             ['Le piège','« il fut » n\'est pas un futur ; « il eut » n\'est pas un présent']],
       say:"il fut, il eut, il fit",
       note:"Ces trois-là suffisent à débloquer la plupart des phrases. « La Régie fut créée en 1980 » : « a été créée »."},

      {t:'ex', h:'L\'encadré historique, traduit',
       p:"À gauche le texte écrit, à droite ce qu'on dirait.",
       rows:[
         ["Le législateur adopta une loi.","Le législateur a adopté une loi."],
         ["La Régie du logement fut créée en 1980.","La Régie du logement a été créée en 1980."],
         ["Elle devint le Tribunal administratif du logement.","Elle est devenue le Tribunal administratif du logement."],
         ["Le nouveau nom entra en vigueur en 2020.","Le nouveau nom est entré en vigueur en 2020."],
         ["Les locataires eurent un recours nouveau.","Les locataires ont eu un recours nouveau."],
         ["Elle lut la page trois fois.","Elle a lu la page trois fois."],
         ["Elle prit un crayon.","Elle a pris un crayon."],
         ["Ils firent la démarche ensemble.","Ils ont fait la démarche ensemble."],
       ]},

      {t:'piege', h:'Deux malentendus fréquents',
       rows:[
         ["prendre « il fut » pour un futur","essayer le passé composé",
          "La ressemblance avec « futur » est une coïncidence. Devant une forme courte qui vous étonne dans un texte écrit, remplacez-la par un passé composé : si la phrase tient, c'était un passé simple."],
         ["vouloir en employer pour faire sérieux","écrire au passé composé",
          "Un courriel au passé simple ne fait pas sérieux : il fait bizarre. Dans un avis, dans une lettre, dans un courriel, le passé composé est le seul temps juste."],
       ]},

      {t:'revoir', h:'À retenir',
       p:"Le passé simple s'écrit et ne se parle pas. Repérez <b>-a, -it, -ut, -int</b> au singulier et <b>-rent</b> au pluriel ; retenez <b>fut, eut, fit</b> ; et traduisez toujours en passé composé pour comprendre."},
    ]
  },

  t1conn: {
    eye:'Mini-leçon', tit:'Prévenir votre lecteur de ce qui vient',
    blocs:[
      {t:'texte', h:"Trois mots qui évitent un malentendu",
       p:"Sans connecteur, le lecteur ne sait pas si votre phrase suivante ajoute une règle, donne un exemple ou exprime votre opinion. Il le devine, souvent mal. « Par exemple » et « à mon avis » coûtent deux mots et retirent tout le risque. Dans un dossier de logement, ce n'est pas un raffinement : c'est ce qui empêche votre locateur de croire que vous inventez la loi.",
       note:"Le programme demande deux familles au niveau 6 : les connecteurs d'exemplification et d'illustration, et les connecteurs de point de vue."},

      {t:'ana', h:"Annoncer un exemple",
       p:"Ils préviennent : ce qui suit n'est pas une règle nouvelle, c'est un cas de la règle précédente.",
       mots:[['par exemple','le plus simple, et jamais déplacé'],
             ['notamment','quand vous ne donnez qu\'un cas parmi plusieurs', true],
             ['entre autres','même emploi, un peu plus parlé'],
             ['ainsi','plus soutenu, en tête de phrase : « Ainsi, un défaut de paiement… »']],
       say:"par exemple, notamment, entre autres, ainsi",
       note:"Sans eux, votre exemple passe pour une deuxième règle — et votre interlocuteur croira que vous en ajoutez."},

      {t:'ana', h:"Annoncer un point de vue",
       p:"Ils disent : ce qui suit n'est plus le texte, c'est moi.",
       mots:[['à mon avis','le plus courant, à l\'oral comme à l\'écrit'],
             ['selon moi','même chose, un peu plus ferme', true],
             ['pour ma part','quand d\'autres avis viennent d\'être exposés'],
             ['personnellement','à garder pour l\'oral : à l\'écrit, il alourdit']],
       say:"à mon avis, selon moi, pour ma part, personnellement",
       note:"Dans une lettre à un locateur, un avis annoncé se discute ; un avis non annoncé passe pour une affirmation de droit, et il sera contredit."},

      {t:'ana', h:"Rapporter, opposer, résumer",
       p:"Trois autres familles, plus rares mais indispensables dans un dossier.",
       mots:[['rapporter','<b>selon</b> la page du Tribunal · <b>d\'après</b> monsieur Tardif'],
             ['opposer','<b>en revanche</b> · <b>par contre</b> · <b>cependant</b> · <b>toutefois</b>', true],
             ['résumer','<b>autrement dit</b> · <b>bref</b> · <b>en somme</b>'],
             ['conclure','<b>ainsi</b> · <b>de cette façon</b> · <b>donc</b>']],
       say:"selon, d'après, en revanche, autrement dit",
       note:"« Selon » vous met à l'abri : vous rapportez sans vous porter garant. C'est exactement ce qu'il faut faire d'une règle qu'on vient de lire sur un site."},

      {t:'ex', h:'La même phrase, avec et sans',
       p:"À gauche ce qui prête à confusion, à droite ce qui ne s'y prête plus.",
       rows:[
         ["Le motif doit être sérieux. Un défaut de paiement.","Le motif doit être sérieux. Par exemple, un défaut de paiement."],
         ["Ce refus ne tient pas.","À mon avis, ce refus ne tient pas."],
         ["Le silence vaut consentement.","Selon la page du Tribunal, le silence vaut consentement."],
         ["Il peut réclamer ses frais. Il ne peut pas fixer un montant.","Il peut réclamer ses frais. En revanche, il ne peut pas fixer un montant."],
         ["J'ai lu, j'ai appelé, j'ai écrit.","J'ai lu, j'ai appelé, j'ai écrit : bref, j'ai suivi les étapes."],
         ["J'ai gardé une copie. Je peux prouver la date.","J'ai gardé une copie. Ainsi, je peux prouver la date."],
       ]},

      {t:'piege', h:'Deux excès à éviter',
       rows:[
         ["mettre un connecteur à chaque phrase","un par idée, pas plus",
          "Un texte saturé de « donc », « ainsi », « en effet » devient illisible. Le connecteur sert quand le lien n'est pas évident ; quand il l'est, il alourdit."],
         ["donner son avis sans le dire","annoncer d'un seul mot",
          "« Ce refus n'est pas valable » est une affirmation de droit, et vous n'êtes pas un tribunal. « À mon avis, ce refus n'est pas valable » est une opinion, et personne ne peut vous la reprocher."],
       ]},

      {t:'revoir', h:'À retenir',
       p:"Quatre familles pour un dossier : <b>exemple</b> (par exemple, notamment), <b>point de vue</b> (à mon avis, selon moi), <b>source</b> (selon, d'après), <b>opposition</b> (en revanche, cependant). Un par idée, jamais un par phrase."},
    ]
  },

  t2avis: {
    eye:'Mini-leçon', tit:'Un avis écrit, et pourquoi il tient debout',
    blocs:[
      {t:'texte', h:"Un avis n'est pas une demande de permission",
       p:"C'est la chose la plus difficile à admettre, et c'est celle qui change tout. Un avis informe l'autre partie et fait partir un compte à rebours. Il ne quête rien. Écrit à la bonne date, avec les bons renseignements, il travaille tout seul : au quinzième jour, quelque chose se produit, que le locateur ait répondu ou non.",
       note:"Farida n'écrit pas « accepteriez-vous que… ». Elle écrit « je vous avise de mon intention de ». La différence n'est pas de politesse : elle est juridique."},

      {t:'ana', h:"Les cinq renseignements qui doivent y être",
       p:"Il en manque un, et l'avis ne vaut plus grand-chose.",
       mots:[['La date','celle du jour où vous écrivez, en toutes lettres ou en chiffres'],
             ['Ce que vous annoncez','le mot exact : sous-location, et pas « location »', true],
             ['Qui','le nom <b>et</b> l\'adresse de la personne proposée'],
             ['Quand','les dates de début et de fin de la sous-location'],
             ['Le rappel du délai','quinze jours à compter de la réception']],
       say:"la date, ce que vous annoncez, qui, quand, le rappel du délai",
       note:"Le nom et l'adresse ne sont pas une formalité : ce sont eux qui permettent au locateur de vérifier, et c'est parce qu'il peut vérifier qu'un délai peut lui être imposé."},

      {t:'ana', h:"Trois façons de dater sa remise",
       p:"Le délai part de la réception. Vous devez donc pouvoir dire quel jour l'autre l'a eu.",
       mots:[['Faire signer une copie','le plus simple : une ligne, une date, une signature'],
             ['Un envoi qui laisse une trace','vous gardez le reçu, sans discussion possible', true],
             ['Deux témoins','le moins solide, mais mieux que rien'],
             ['Ce qui ne vaut rien','« je le lui ai dit dans l\'escalier mardi »']],
       say:"faire signer une copie, un envoi qui laisse une trace, deux témoins",
       note:"Farida demande une signature « pour la date, pas pour l'accord ». Beaucoup de locateurs refusent de signer parce qu'ils croient s'engager : le dire évite le refus."},

      {t:'ex', h:'Ce qui affaiblit un avis, et ce qui le renforce',
       p:"À gauche l'avis qui ne tient pas, à droite le même, solide.",
       rows:[
         ["« Je voudrais peut-être sous-louer. »","« Je vous avise de mon intention de sous-louer. »"],
         ["« à une personne sérieuse »","« à monsieur Nicolas Trudel, 745, avenue du Bourg-Royal »"],
         ["« pour quelques mois »","« du 5 janvier au 28 juin inclusivement »"],
         ["« j'espère que vous serez d'accord »","« vous disposez de quinze jours pour me répondre »"],
         ["sans date en haut","« Québec, le 18 novembre »"],
         ["sans signature","« Farida Belkacem, logement 2 »"],
       ]},

      {t:'check', h:'Trois questions',
       qs:[
         {q:"Un avis de sous-location sert à…", opts:["demander la permission","informer et faire courir un délai"], ok:1,
          fb:"C'est ce qui le distingue d'une lettre ordinaire."},
         {q:"Un avis sans nom de personne…", opts:["fait courir le délai quand même","ne fait courir aucun délai"], ok:1,
          fb:"Le locateur doit pouvoir vérifier qui on lui propose."},
         {q:"Faire signer une copie de son avis prouve…", opts:["l'accord du locateur","la date de réception"], ok:1,
          fb:"Rien d'autre — et c'est déjà l'essentiel."},
       ]},

      {t:'revoir', h:'À retenir',
       p:"Cinq renseignements : <b>la date, ce que vous annoncez, qui, quand, le délai</b>. Une preuve de réception. Et une phrase qui informe, jamais qui quête."},
    ]
  },

  t2reponse: {
    eye:'Mini-leçon', tit:'Peser un refus sans se fâcher',
    blocs:[
      {t:'texte', h:"Une lettre de refus n'est pas un bloc",
       p:"On la lit d'un coup, on se sent visé, on répond mal. Or une lettre de refus contient des morceaux de valeur très inégale : une date qui est un fait, une décision qui est un droit, des motifs dont certains tiennent et d'autres non, et parfois une demande qui n'a rien à faire là. Les séparer avant de répondre, c'est la moitié du travail.",
       note:"La lettre de monsieur Tardif est écrite exprès pour ça : elle est correcte sur un point, discutable sur deux autres."},

      {t:'ana', h:"Découper la lettre en quatre",
       p:"Prenez un crayon et marquez chaque passage de la lettre selon ce qu'il est.",
       mots:[['Un fait','« remis en main propre le 18 novembre » — vérifiable, personne ne le conteste'],
             ['Un droit exercé','« je n\'accepte pas » — il en a le droit, la question est ailleurs', true],
             ['Un motif','à peser un par un : celui-ci regarde-t-il la personne ou le logement ?'],
             ['Une demande à part','les 200 $ ne sont ni un fait ni un motif : c\'est autre chose']],
       say:"un fait, un droit exercé, un motif, une demande à part",
       note:"Répondre à tout en une phrase indignée fait perdre les trois quarts du terrain. Répondre morceau par morceau, calmement, le garde."},

      {t:'ana', h:"Les deux motifs de la lettre, pesés",
       p:"La page du site donnait le critère : le motif doit regarder la personne proposée ou le logement, et pouvoir se montrer.",
       mots:[['« je préfère les personnes en emploi »','une préférence — elle ne se vérifie pas et ne regarde pas cette personne-ci'],
             ['« un défaut de paiement en 2024 »','un fait vérifiable, qui regarde bien la personne proposée', true],
             ['Ce qui les distingue','l\'un se prouve, l\'autre s\'affirme'],
             ['Ce que ça ne dit pas','ce n\'est pas à vous de trancher : c\'est au Tribunal, s\'il est saisi']],
       say:"une préférence, un fait vérifiable",
       note:"Il ne s'agit pas de gagner une discussion dans un escalier. Il s'agit de savoir lequel des deux motifs mérite une réponse, et lequel mérite une question."},

      {t:'ana', h:"Les 200 $ : la question à poser",
       p:"Une somme peut être due, mais pas n'importe comment.",
       mots:[['Ce que le site permet','le remboursement des <b>dépenses raisonnables</b> que la sous-location occasionne'],
             ['Ce que ça veut dire','une dépense réelle, faite, chiffrable — une vérification de crédit, par exemple', true],
             ['Ce que ça ne dit pas','un tarif fixe, décidé d\'avance, sans rapport avec une dépense'],
             ['La question à écrire','« Pourriez-vous me préciser à quelles dépenses ce montant correspond ? »']],
       say:"des dépenses raisonnables, une dépense réelle, la question à écrire",
       note:"Poser la question par écrit vaut mieux que refuser par écrit : ou bien la réponse justifie la somme, ou bien elle ne vient pas."},

      {t:'ex', h:'Répondre, morceau par morceau',
       p:"À gauche la ligne de la lettre, à droite ce qu'on en fait.",
       rows:[
         ["« reçu en main propre le 18 novembre »","on l'accepte : c'est notre propre preuve"],
         ["« je réponds dans le délai de quinze jours »","c'est exact : le silence n'a pas joué"],
         ["« je n'accepte pas la sous-location »","c'est son droit ; on regarde les motifs"],
         ["« je préfère les personnes en emploi »","on demande en quoi cela regarde monsieur Trudel"],
         ["« un défaut de paiement en 2024 »","on vérifie, et on en parle à monsieur Trudel"],
         ["« j'exige 200 $ »","on demande par écrit à quelles dépenses cela correspond"],
       ]},

      {t:'piege', h:'Trois réactions qui coûtent cher',
       rows:[
         ["répondre le soir même, fâché","attendre le lendemain matin",
          "Une lettre écrite en colère donne des arguments à l'autre partie, et elle reste au dossier. Le délai qui vous concerne, lui, est déjà passé : vous avez le temps."],
         ["discuter dans l'escalier","tout mettre par écrit",
          "Ce qui se dit dans un escalier ne se prouve pas. Chaque question, chaque réponse : par écrit, daté, gardé."],
         ["décider soi-même que le refus est illégal","poser des questions et se renseigner",
          "Personne d'autre que le Tribunal n'apprécie un motif. Votre travail est de savoir quoi demander et à qui — pas de rendre un jugement."],
       ]},

      {t:'revoir', h:'À retenir',
       p:"Découpez la lettre : <b>les faits, la décision, chaque motif, les demandes d'argent</b>. Un motif se pèse à deux questions — <i>regarde-t-il la personne ou le logement ?</i> et <i>peut-il se montrer ?</i> Le reste se demande par écrit."},
    ]
  },

  t2pqp: {
    eye:'Mini-leçon', tit:'Le plus-que-parfait : ce qui était déjà fait',
    blocs:[
      {t:'texte', h:"Deux passés dans la même phrase",
       p:"« Il a refusé parce qu'un locataire lui avait causé des ennuis. » Deux choses passées, et l'ordre n'est pas celui des mots : les ennuis sont d'il y a six ans, le refus est de novembre. Ce n'est pas la place dans la phrase qui le dit, c'est le temps du verbe. Un lecteur qui ne repère pas le plus-que-parfait met les événements dans le désordre.",
       note:"Le programme du niveau 6 le formule ainsi : « comprendre que le plus-que-parfait désigne une action précédant une autre action passée »."},

      {t:'ana', h:"Comment il se forme",
       p:"Rien de neuf : le passé composé avec l'auxiliaire à l'imparfait.",
       mots:[['avec avoir','j\'<b>avais</b> lu · elle <b>avait</b> écrit · ils <b>avaient</b> reçu'],
             ['avec être','il <b>était</b> parti · elle <b>était</b> arrivée', true],
             ['pronominal','elle s\'<b>était</b> trompée de mot'],
             ['La différence avec le passé composé','« j\'ai lu » (l\'auxiliaire au présent) · « j\'avais lu » (à l\'imparfait)']],
       say:"j'avais lu, elle avait écrit, il était parti, elle s'était trompée",
       note:"Si vous savez faire un passé composé, vous savez faire un plus-que-parfait : il ne reste qu'à mettre l'auxiliaire à l'imparfait."},

      {t:'ana', h:"Les mots qui l'annoncent",
       p:"Ils sont peu nombreux et ils reviennent tout le temps dans un dossier.",
       mots:[['déjà','elle <b>avait déjà</b> lu la page trois fois'],
             ['la veille','il <b>avait</b> vérifié le dossier <b>la veille</b>', true],
             ['deux ans plus tôt','son cousin <b>avait</b> sous-loué <b>deux ans plus tôt</b>'],
             ['avant','elle <b>avait</b> tout noté <b>avant</b> de téléphoner']],
       say:"déjà, la veille, deux ans plus tôt, avant",
       note:"Quand l'un de ces mots paraît dans un récit au passé, cherchez le plus-que-parfait : il est presque toujours dans la même phrase."},

      {t:'ex', h:'Remettre les faits dans l\'ordre',
       p:"À gauche la phrase, à droite ce qui s'est passé en premier.",
       rows:[
         ["Quand elle a remis son avis, elle avait lu la page trois fois.","la lecture"],
         ["Il a refusé parce qu'un locataire lui avait causé des ennuis.","les ennuis"],
         ["Elle a téléphoné après qu'elle avait noté ses questions.","les questions notées"],
         ["Le 29 novembre, il a écrit : il avait vérifié le dossier la veille.","la vérification"],
         ["Nicolas a accepté : elle lui avait tout expliqué au téléphone.","l'explication"],
         ["Elle a pu prouver la date parce qu'elle avait fait signer sa copie.","la signature"],
       ]},

      {t:'piege', h:'Deux confusions',
       rows:[
         ["employer l'imparfait à sa place","se demander s'il y a deux passés",
          "« Elle lisait la page » raconte une action en cours. « Elle avait lu la page » dit que c'était fini avant autre chose. Les deux sont au passé ; un seul situe."],
         ["oublier l'accord avec être","regarder le sujet",
          "« Elle était partie », « ils étaient arrivés » : avec être, le participe s'accorde avec le sujet, exactement comme au passé composé."],
       ]},

      {t:'revoir', h:'À retenir',
       p:"Auxiliaire à l'<b>imparfait</b> + participe passé. Il dit : <b>c'était déjà fait avant</b>. Cherchez-le près de <i>déjà</i>, <i>la veille</i>, <i>avant</i>, <i>deux ans plus tôt</i>."},
    ]
  },

  t2subj: {
    eye:'Mini-leçon', tit:'« Il faut que » et ce qui vient après',
    blocs:[
      {t:'texte', h:"Le temps de ce qui n'est pas encore arrivé",
       p:"« Il faut que vous répondiez par écrit. » Au moment où on le dit, la réponse n'existe pas : elle est demandée, voulue, exigée. Le subjonctif est le temps de cela — de ce qui est visé et non constaté. Dans une lettre à un locateur, c'est le temps de toutes vos demandes, et il vaut mieux le tenir : « il faut que vous répondez » se remarque immédiatement.",
       note:"Le programme demande d'employer le subjonctif présent après quelques verbes introducteurs usuels, et de distinguer verbe + de de verbe + que."},

      {t:'ana', h:"Les verbes qui l'imposent",
       p:"Volonté, obligation, souhait : rien n'est encore fait quand on parle.",
       mots:[['il faut que','Il faut que vous <b>répondiez</b> par écrit.'],
             ['je veux que','Je veux que Nicolas <b>sache</b> à quoi s\'en tenir.', true],
             ['j\'exige que','Il exige qu\'on lui <b>paie</b> deux cents dollars.'],
             ['je souhaite que','Je souhaite que vous <b>preniez</b> le temps de vérifier.']],
       say:"il faut que vous répondiez, je veux que Nicolas sache",
       note:"« Il ne faut pas que » impose le subjonctif tout autant : « il ne faut pas qu'un locataire parte sans avertir »."},

      {t:'ana', h:"Les verbes qui ne l'imposent pas",
       p:"C'est le piège de l'exercice, et l'erreur la plus fréquente à ce niveau.",
       mots:[['espérer que','J\'espère qu\'il <b>répondra</b> avant le 3 décembre.'],
             ['penser que, croire que','Je pense qu\'il <b>a</b> tort.', true],
             ['voir que, savoir que','Je vois qu\'il <b>est</b> pressé.'],
             ['Pourquoi','ces verbes constatent ou prévoient : le fait est posé comme réel']],
       say:"j'espère qu'il répondra, je pense qu'il a tort",
       note:"« Espérer » ressemble à « souhaiter » et ne se construit pas pareil. C'est une bizarrerie du français, et elle s'apprend telle quelle."},

      {t:'labo', h:'Que ou de ?',
       p:"Prenez un verbe, puis une construction.",
       axes:[
         {id:'v', lbl:'Quel verbe ?', opts:[['d','demander'],['f','falloir'],['e','espérer']]},
         {id:'c', lbl:'Quelle construction ?', opts:[['1','avec de'],['2','avec que']]}],
       out:{
         d1:{w:["je demande de répondre par écrit"], say:"je demande de répondre par écrit", n:'de + infinitif : un seul sujet'},
         d2:{w:["je demande que vous répondiez par écrit"], say:"je demande que vous répondiez par écrit", n:'que + subjonctif : deux sujets'},
         f1:{w:["il faut répondre par écrit"], say:"il faut répondre par écrit", n:'sans que : infinitif, valable pour tout le monde'},
         f2:{w:["il faut que vous répondiez"], say:"il faut que vous répondiez", n:'avec que : subjonctif, adressé à quelqu\'un'},
         e1:{w:["j'espère recevoir une réponse"], say:"j'espère recevoir une réponse", n:'espérer + infinitif : même sujet'},
         e2:{w:["j'espère que vous répondrez"], say:"j'espère que vous répondrez", n:'espérer que : indicatif, jamais subjonctif'},
       },
       note:"Deux sujets différents appellent « que » ; un seul sujet appelle l'infinitif. Le sens ne change pas, la construction si."},

      {t:'ex', h:'Six formes à savoir par cœur',
       p:"Elles couvrent la moitié des cas d'un dossier.",
       rows:[
         ["être","qu'il soit — « il faut que ce soit écrit »"],
         ["avoir","qu'il ait — « il faut que j'aie son adresse »"],
         ["faire","qu'il fasse — « il faut qu'il fasse la vérification »"],
         ["aller","qu'il aille — « il faut qu'elle aille au bureau »"],
         ["savoir","qu'il sache — « je veux qu'il sache la date »"],
         ["pouvoir","qu'il puisse — « pour qu'il puisse vérifier »"],
       ]},

      {t:'piege', h:'Trois fautes qui se voient tout de suite',
       rows:[
         ["« il faut que vous répondez »","« il faut que vous répondiez »",
          "C'est la faute la plus visible du niveau. Après « il faut que », le verbe change de forme, sans exception."],
         ["« j'espère qu'il réponde »","« j'espère qu'il répondra »",
          "Espérer prend l'indicatif. Souhaiter prend le subjonctif. Les deux verbes veulent presque la même chose et ne se construisent pas pareil."],
         ["« je demande que répondre »","« je demande de répondre »",
          "Après « que », il faut un sujet et un verbe conjugué. Pour un infinitif, c'est « de »."],
       ]},

      {t:'revoir', h:'À retenir',
       p:"<b>Vouloir, falloir, exiger, souhaiter</b> + que → subjonctif. <b>Espérer, penser, croire, voir</b> + que → indicatif. Un seul sujet → <b>de</b> + infinitif. Six formes à retenir : soit, ait, fasse, aille, sache, puisse."},
    ]
  },

  t2si: {
    eye:'Mini-leçon', tit:'Poser une condition sans s\'engager',
    blocs:[
      {t:'texte', h:"Le temps des suites possibles",
       p:"La fin de ce dossier tient tout entière dans des hypothèses : s'il refuse, si le délai passe, si le sous-locataire ne paie pas. Une hypothèse permet de parler d'une suite sans la provoquer et sans s'y engager. C'est très utile quand on discute avec quelqu'un de méfiant : « si vous ne répondez pas » n'est pas une menace, c'est une information.",
       note:"Le programme demande l'hypothèse réaliste sur un fait présent ou à venir : si + présent, puis la conséquence."},

      {t:'ana', h:"La règle, et ses trois suites",
       p:"Après « si », le présent. Dans l'autre moitié de la phrase, trois choix.",
       mots:[['suite au présent','S\'il ne répond pas, il <b>est</b> réputé avoir consenti.'],
             ['suite au futur','Si vous donnez vos références, je les <b>appellerai</b>.', true],
             ['suite à l\'impératif','Si tu veux une preuve, <b>fais</b> signer ta copie.'],
             ['Ce qui ne change jamais','le verbe après « si » reste au présent, quelle que soit la suite']],
       say:"s'il ne répond pas, il est réputé avoir consenti",
       note:"Le choix de la suite change le ton, pas le sens : le présent constate, le futur promet, l'impératif conseille."},

      {t:'ana', h:"Les deux « si » qu'on confond",
       p:"Deux mots identiques, deux emplois qui n'ont rien à voir.",
       mots:[['le si de la condition','<b>Si</b> vous ne payez pas, je reste responsable.'],
             ['le si de la question rapportée','Je ne sais pas <b>si</b> il répondra à temps.', true],
             ['Comment les distinguer','le premier se remplace par « dans le cas où » ; le second, par « oui ou non »'],
             ['Ce que ça change','le futur est interdit après le premier, permis après le second']],
       say:"si vous ne payez pas, je ne sais pas s'il répondra",
       note:"« Je ne sais pas s'il répondra » est correct. « S'il répondra pas d'ici mardi, je rappelle » ne l'est pas. Le test de « dans le cas où » tranche en une seconde."},

      {t:'labo', h:'Choisissez votre suite',
       p:"Prenez une condition, puis le ton que vous voulez donner.",
       axes:[
         {id:'c', lbl:'Quelle condition ?', opts:[['a','s\'il ne répond pas'],['b','si vous ne payez pas']]},
         {id:'t', lbl:'Quel ton ?', opts:[['1','je constate'],['2','j\'annonce'],['3','je conseille']]}],
       out:{
         a1:{w:["s'il ne répond pas, il est réputé avoir consenti"], say:"s'il ne répond pas, il est réputé avoir consenti", n:'présent : je rapporte la règle'},
         a2:{w:["s'il ne répond pas, je signerai le 4 décembre"], say:"s'il ne répond pas, je signerai le 4 décembre", n:'futur : j\'annonce ce que je ferai'},
         a3:{w:["s'il ne répond pas, appelez le service de renseignements"], say:"s'il ne répond pas, appelez le service de renseignements", n:'impératif : je conseille'},
         b1:{w:["si vous ne payez pas, je reste responsable"], say:"si vous ne payez pas, je reste responsable", n:'présent : je constate un fait'},
         b2:{w:["si vous ne payez pas, le locateur me poursuivra"], say:"si vous ne payez pas, le locateur me poursuivra", n:'futur : j\'annonce la suite'},
         b3:{w:["si vous ne pouvez pas payer, prévenez-moi tout de suite"], say:"si vous ne pouvez pas payer, prévenez-moi tout de suite", n:'impératif : je demande'},
       },
       note:"Trois tons, une seule règle : le verbe après « si » ne bouge pas."},

      {t:'ex', h:'Six hypothèses du dossier',
       p:"À gauche la condition, à droite la suite.",
       rows:[
         ["s'il ne répond pas d'ici le 3 décembre","la loi considère qu'il a consenti"],
         ["si le refus est appuyé sur un motif sérieux","la sous-location ne se fait pas"],
         ["si vous ne payez pas le loyer","c'est moi que le locateur poursuivra"],
         ["si vous recevez du monde","ce n'est pas un problème avant onze heures"],
         ["si le locateur exige des frais","il doit dire à quoi ils correspondent"],
         ["si elle part sans avertir","elle reste responsable de son bail"],
       ]},

      {t:'check', h:'Trois questions',
       qs:[
         {q:"« Si vous ___ pas, je reste responsable. »", opts:["ne paierez","ne payez"], ok:1,
          fb:"Jamais de futur après le si de condition."},
         {q:"« Je ne sais pas s'il ___ à temps. »", opts:["répondra","réponde"], ok:0,
          fb:"Ce si-là est une question rapportée : le futur y est permis."},
         {q:"Après « si » de condition, le verbe est…", opts:["au présent","au futur"], ok:0,
          fb:"Toujours au présent, quelle que soit la suite."},
       ]},

      {t:'revoir', h:'À retenir',
       p:"<b>Si + présent</b>, puis présent, futur ou impératif. Jamais de futur après le « si » de condition — mais il est permis après le « si » qui veut dire « oui ou non »."},
    ]
  },

  t2courriel: {
    eye:'Mini-leçon', tit:'Le courriel qui obtient une réponse écrite',
    blocs:[
      {t:'texte', h:"Ce que vous voulez, c'est de l'écrit en retour",
       p:"Un courriel à un locateur n'a pas pour but de vider une querelle : il a pour but d'obtenir une réponse écrite, datée, qui dit quelque chose de précis. Tout ce qui sert ce but a sa place ; tout le reste — ce que vous pensez de lui, ce qu'il vous a dit dans l'escalier, ce que votre voisine en pense — travaille contre vous.",
       note:"C'est la troisième attente de fin de cours du niveau : « dans ses relations professionnelles, il rédige un courriel ou une lettre en respectant les conventions habituelles »."},

      {t:'ana', h:"Les sept parties, dans l'ordre",
       p:"Elles ne se déplacent pas, et aucune ne se saute.",
       mots:[['L\'objet','cinq ou six mots, sans verbe conjugué : « Avis de sous-location — logement 2 »'],
             ['La formule d\'appel','« Monsieur Tardif, » — le nom, une virgule, retour à la ligne', true],
             ['Premier paragraphe','pourquoi vous écrivez, et à quel document vous vous rapportez'],
             ['Deuxième paragraphe','les faits, les dates, les noms, dans l\'ordre'],
             ['Troisième paragraphe','ce que vous demandez, et pour quand'],
             ['La salutation','fermée, sans familiarité'],
             ['La signature','nom, numéro de logement, téléphone']],
       say:"l'objet, la formule d'appel, les trois paragraphes, la salutation, la signature",
       note:"Trois paragraphes, jamais un seul bloc. Le lecteur doit voir d'un coup d'œil combien de choses vous lui dites."},

      {t:'ana', h:"Le ton : ferme et poli en même temps",
       p:"Ce n'est pas contradictoire, et cela tient à trois ou quatre tournures.",
       mots:[['La demande au conditionnel','« <b>Pourriez-vous</b> me confirmer par écrit… »'],
             ['L\'obligation impersonnelle','« <b>Il faut que</b> votre réponse soit écrite » plutôt que « vous devez »', true],
             ['La source citée','« <b>Selon</b> la page du Tribunal… » plutôt que « la loi dit »'],
             ['L\'avis annoncé','« <b>À mon avis</b>, ce motif ne regarde pas monsieur Trudel »']],
       say:"pourriez-vous, il faut que, selon, à mon avis",
       note:"Le conditionnel ne veut pas dire que vous doutez de votre droit : il laisse à l'autre la place de répondre, et c'est cette place-là qui fait venir la réponse."},

      {t:'ex', h:'La même phrase, deux versions',
       p:"À gauche ce qui ferme la porte, à droite ce qui la laisse ouverte.",
       rows:[
         ["« Vous devez me répondre. »","« Pourriez-vous me confirmer votre réponse par écrit ? »"],
         ["« Vous n'avez pas le droit de refuser. »","« À mon avis, ce motif ne regarde pas monsieur Trudel. »"],
         ["« La loi dit que… »","« Selon la page du Tribunal administratif du logement… »"],
         ["« Vos 200 $ sont illégaux. »","« Pourriez-vous préciser à quelles dépenses ce montant correspond ? »"],
         ["« Comme je vous l'ai dit l'autre jour »","« Comme je vous l'ai écrit le 18 novembre »"],
         ["« Bonjour, »","« Monsieur Tardif, »"],
       ]},

      {t:'piege', h:'Trois choses à ne pas mettre dans un courriel',
       rows:[
         ["ce que vous pensez de la personne","ce que vous attendez d'elle",
          "Un jugement sur quelqu'un reste écrit et se retourne toujours. Une demande datée, elle, appelle une réponse."],
         ["trois sujets dans le même message","un message, un sujet",
          "L'avis, les frais et la fenêtre du salon qui ferme mal : trois courriels. Un message à trois sujets reçoit une réponse à un seul."],
         ["une question sans délai","« d'ici le 3 décembre »",
          "« Quand vous pourrez » n'obtient jamais rien. Une date, même souple, transforme une question en demande."],
       ]},

      {t:'revoir', h:'À retenir',
       p:"Sept parties : <b>objet, appel, trois paragraphes, salutation, signature</b>. Un sujet par message, une date par fait, la demande au conditionnel à la fin. Le but est simple : obtenir de l'écrit en retour."},
    ]
  },

};
