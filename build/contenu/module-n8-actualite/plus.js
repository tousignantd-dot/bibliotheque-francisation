const PLUS = {

  prInto: {
    eye:'Mini-leçon', tit:"Ce que la voix ajoute aux mots",
    blocs:[
      {t:'texte', h:"Le seul savoir de phonétique du niveau 8",
       p:"Le programme du niveau 8 ne demande plus qu'une chose à l'oreille et à la voix : produire l'<b>intonation expressive</b> — la surprise, l'admiration, la déception, la volonté, l'incompréhension. Pas un son nouveau, pas une liaison de plus : une mélodie. À ce stade, vous prononcez assez bien pour être compris. Ce qui vous reste à gagner, c'est ce que la voix ajoute par-dessus les mots.",
       note:"Une intonation plate se lit comme de l'indifférence, alors qu'elle n'est souvent que de la prudence. C'est le malentendu le plus coûteux à ce niveau-ci."},

      {t:'texte', h:"Pourquoi ça compte quand on discute d'actualité",
       p:"Dans un débat, la mélodie fait la moitié du travail. Une même phrase — « quatre voix contre trois » — peut dire l'étonnement, le reproche, la lassitude ou la simple information. Si votre voix ne choisit pas, votre interlocuteur choisira pour vous, et il choisira souvent mal. À une tribune téléphonique, où personne ne voit votre visage, il ne reste que ça.",
       note:"C'est aussi ce qui vous permet d'entendre, chez l'autre, ce qu'il ne dit pas : une concession faite du bout des lèvres s'entend avant de se comprendre."},

      {t:'ana', h:"La surprise — la voix monte d'un coup, à la fin",
       p:"La phrase part normalement, puis grimpe brusquement sur les deux ou trois dernières syllabes. Souvent une question, souvent courte, souvent annoncée par « comment ça » ou par la répétition du mot qui étonne.",
       mots:[['On dit','Quatre voix contre trois, pour onze hectares ?'],['La mélodie','plate, puis très haute à la fin',true],['Le repère','on répète le chiffre qui surprend']],
       say:"Quatre voix contre trois, pour onze hectares ?",
       note:"La surprise n'est pas le reproche. Si la voix monte trop tôt, la phrase devient un « vous vous moquez de moi »."},

      {t:'ana', h:"La déception — la voix tombe dès le début",
       p:"La mélodie descend tout de suite et ne remonte jamais. Le débit est régulier, presque lent, souvent précédé d'un petit mot isolé : « ah », « bon ».",
       mots:[['On dit',"Ah. Je pensais que l'évaluation était publique."],['La mélodie','descendante dès la première syllabe',true],['Le repère',"un « ah » ou un « bon » en tête"]],
       say:"Ah. Je pensais que l'évaluation était publique.",
       note:"Chez votre interlocuteur, c'est le signal qu'une réponse ne lui a pas plu. Il ne le dira pas ; la mélodie l'a déjà dit."},

      {t:'ana', h:"La volonté — la voix descend, et chaque mot pèse",
       p:"À l'inverse de la surprise : la mélodie descend, le débit ralentit, les syllabes se détachent. C'est la voix de l'engagement, celle d'une demande qu'on ne retirera pas.",
       mots:[['On dit','Ce document-là, je le veux avant mardi.'],['La mélodie','descendante, appuyée sur « veux »',true],['Le repère','on ne sourit pas en le disant']],
       say:"Ce document-là, je le veux avant mardi.",
       note:"Une phrase de volonté dite en montant devient une demande de permission — exactement l'inverse de ce qu'on voulait."},

      {t:'ana', h:"L'incompréhension — la voix freine au milieu",
       p:"On ne monte pas : on ralentit. Le débit se casse à l'endroit précis où le fil s'est rompu, souvent avec un petit silence avant le mot en cause.",
       mots:[['On dit',"Excusez-moi, « personne habile à voter »… ça veut dire quoi exactement ?"],['La mélodie','un creux et un silence avant le mot',true],['Le repère','on isole le mot avec la voix']],
       say:"Excusez-moi, personne habile à voter, ça veut dire quoi exactement ?",
       note:"C'est la mélodie qui dit « une seule chose m'échappe ». Sans elle, la même phrase se comprend comme « je n'ai rien suivi »."},

      {t:'labo', h:"Écoutez les quatre intentions",
       p:"Choisissez une intention et un exemple.",
       axes:[
         {id:'i', lbl:'Quelle intention ?', opts:[['a','surprise'],['b','déception'],['c','volonté'],['d','incompréhension']]},
         {id:'n', lbl:'Quel exemple ?', opts:[['1','le premier'],['2','le second']]}],
       out:{
         a1:{w:["Trois cent quarante-deux arbres ?"], say:"Trois cent quarante-deux arbres ?", n:"la voix monte d'un coup sur le chiffre"},
         a2:{w:["Comment ça, personne n'a répondu ?"], say:"Comment ça, personne n'a répondu ?", n:"« comment ça » annonce la surprise"},
         b1:{w:["Ah. Bon."], say:"Ah. Bon.", n:"deux syllabes qui tombent : la déception se passe de phrase"},
         b2:{w:["On avait trois cents signatures ce matin aussi."], say:"On avait trois cents signatures ce matin aussi.", n:"descendante du début à la fin"},
         c1:{w:["Je vais signer, et je vais le dire."], say:"Je vais signer, et je vais le dire.", n:"mélodie descendante, syllabes détachées"},
         c2:{w:["Je tiens à ce que ce soit écrit."], say:"Je tiens à ce que ce soit écrit.", n:"la voix pèse sur « tiens » et sur « écrit »"},
         d1:{w:["Attendez, je perds le fil."], say:"Attendez, je perds le fil.", n:"débit qui freine, mélodie creusée"},
         d2:{w:["Vous avez bien dit vingt et un mois ?"], say:"Vous avez bien dit vingt et un mois ?", n:"on isole le chiffre dont on n'est pas sûr"},
       },
       note:"Écoutez, puis répétez à voix haute en exagérant : l'exagération est ce qui fait entrer une mélodie dans l'oreille."},

      {t:'ex', h:"La même phrase, plusieurs intentions",
       p:"À gauche, ce qui est dit. À droite, ce que la voix ajoute.",
       rows:[
         ["Le vote a été pris à vingt-deux heures cinquante ?","surprise — la voix monte sur l'heure"],
         ["Le vote a été pris à vingt-deux heures cinquante.","constat — la voix reste plate"],
         ["Le vote a été pris à vingt-deux heures cinquante…","reproche retenu — la voix freine et laisse ouvert"],
         ["Je veux voir l'évaluation.","volonté — la voix descend, les mots pèsent"],
         ["Je veux voir l'évaluation ?","doute — la même phrase se retourne contre celui qui parle"],
         ["Bon. Je veux voir l'évaluation.","résignation puis volonté — le « bon » tombe avant le reste"],
       ]},

      {t:'piege', h:"Trois pièges de l'intonation, en débat",
       rows:[
         ["monter la voix à chaque phrase","descendre quand on affirme",
          "Une mélodie qui monte partout transforme chaque affirmation en question, et chaque demande en demande d'autorisation. C'est le défaut le plus fréquent, et il vient de la prudence."],
         ["parler d'une voix parfaitement égale","varier au moins sur les trois phrases importantes",
          "Une voix plate se lit comme de l'indifférence, jamais comme du calme. Trois phrases marquées dans une intervention de deux minutes suffisent."],
         ["mettre de la colère dans la voix pour être entendu","garder la mélodie de la volonté, qui descend",
          "La colère fait monter et accélérer ; à la radio, elle donne raison à celui qui reste calme. La voix de la volonté est plus lente que la voix de la colère, et beaucoup plus difficile à interrompre."],
       ]},

      {t:'check', h:"Est-ce que c'est clair maintenant ?",
       p:"Quatre questions rapides.",
       qs:[
         {q:"« Trois cent quarante-deux arbres ? » exprime…", opts:["la surprise","la volonté"], ok:0,
          fb:"La voix monte brusquement à la fin : c'est la marque de la surprise."},
         {q:"Pour exprimer la volonté, la mélodie…", opts:["monte à la fin","descend et appuie"], ok:1,
          fb:"Elle descend. Une volonté dite en montant devient une demande de permission."},
         {q:"Un « ah » isolé qui tombe, au début d'une phrase, annonce…", opts:["la déception","l'incompréhension"], ok:0,
          fb:"C'est la marque de la déception : la mélodie descend dès la première syllabe."},
         {q:"Une voix parfaitement égale pendant toute une intervention se lit comme…", opts:["du calme","de l'indifférence"], ok:1,
          fb:"Comme de l'indifférence, même quand elle n'est que de la prudence."},
       ]},

      {t:'revoir', h:"À retenir",
       p:"Quatre mélodies : la <b>surprise</b> monte d'un coup à la fin ; la <b>déception</b> tombe dès la première syllabe ; la <b>volonté</b> descend et appuie ; l'<b>incompréhension</b> freine et laisse un silence avant le mot en cause. Choisissez-en trois pour votre intervention et travaillez-les à voix haute."},
    ]
  },

  prFait: {
    eye:'Mini-leçon', tit:"Fait, opinion, propos rapporté",
    blocs:[
      {t:'texte', h:"Pourquoi trois catégories, et non deux",
       p:"On vous a sans doute déjà appris à séparer le fait de l'opinion. C'est utile, et c'est insuffisant : la plus grande partie de ce que vous lisez dans un journal n'est ni l'un ni l'autre. C'est du <b>propos rapporté</b> — quelqu'un a dit quelque chose, et le journal le rapporte sans le vérifier. Confondre un propos rapporté avec un fait est l'erreur la plus fréquente, et la plus utilisée.",
       note:"« Selon le promoteur, quatre-vingt-dix arbres seront abattus » n'est pas l'information « quatre-vingt-dix arbres seront abattus ». C'est l'information « le promoteur dit quatre-vingt-dix »."},

      {t:'ana', h:"Le fait — quelqu'un d'autre arriverait au même résultat",
       p:"Un fait se vérifie ailleurs, avec un document : un procès-verbal, un cadastre, un relevé, une date. Il n'a pas besoin de vous pour être vrai.",
       mots:[['On écrit','Le règlement a été adopté par quatre voix contre trois.'],['On vérifie où','au procès-verbal de la séance',true],['Le signe','un nombre, une date, un lieu, un verbe au passé']],
       say:"Le règlement a été adopté par quatre voix contre trois.",
       note:"Un fait peut être faux : c'est alors un fait erroné, pas une opinion. Ce qui en fait un fait, c'est qu'il soit vérifiable, pas qu'il soit vrai."},

      {t:'ana', h:"L'opinion — elle s'appuie, elle ne se prouve pas",
       p:"Elle porte une évaluation : trop, insuffisant, indécent, prioritaire, nécessaire. Deux personnes raisonnables peuvent ne pas être d'accord sans qu'aucune des deux se trompe.",
       mots:[['On écrit',"Céder un bien public en quatre jours est indéfendable."],['Le signe',"un adjectif de jugement, « devrait », « il faut »",true],['La bonne façon',"annoncer que c'est une opinion : « je pense que… »"]],
       say:"Céder un bien public en quatre jours est indéfendable.",
       note:"Personne ne vous reprochera d'avoir une opinion. On vous reprochera de la présenter comme un fait — et c'est ce qui fera écarter votre lettre."},

      {t:'ana', h:"Le propos rapporté — il n'engage que sa source",
       p:"Le journaliste ne dit pas que c'est vrai : il dit que quelqu'un l'a dit. Les marques sont peu nombreuses et faciles à repérer.",
       mots:[['On écrit',"Selon le service de l'urbanisme, le rezonage prendrait vingt et un mois."],['Les marques',"selon, d'après, affirme, soutient, déclare",true],['Ce que ça vaut',"exactement ce que vaut la source nommée"]],
       say:"Selon le service de l'urbanisme, le rezonage prendrait vingt et un mois.",
       note:"Une source nommée se vérifie ; « des experts », « certains », « on » ne se vérifient pas. Une information sans auteur est une information dont personne n'aura à répondre."},

      {t:'ana', h:"Le conditionnel journalistique — le plus fragile de tous",
       p:"Un conditionnel qui n'exprime ni la politesse ni l'hypothèse, mais la prudence de la rédaction : nous le rapportons, nous ne l'avons pas vérifié.",
       mots:[['On écrit',"Le terrain aurait été évalué à un peu plus de deux millions."],['Ce que ça dit',"on nous l'a dit, nous n'avons pas vu le document",true],['Votre réflexe',"chercher qui l'a dit, et si personne : ne pas s'en servir"]],
       say:"Le terrain aurait été évalué à un peu plus de deux millions.",
       note:"Ne reprenez jamais un conditionnel journalistique dans votre propre lettre : vous porteriez seul une information que personne n'assume."},

      {t:'ex', h:"La même information, trois statuts",
       p:"À gauche la phrase, à droite ce qu'elle vaut.",
       rows:[
         ["Quatre-vingt-dix arbres seront abattus.","présenté comme un fait — et il ne l'est pas"],
         ["Selon le promoteur, quatre-vingt-dix arbres seront abattus.","propos rapporté, source nommée : correct"],
         ["Quatre-vingt-dix arbres seraient abattus.","conditionnel journalistique : source non nommée"],
         ["Abattre quatre-vingt-dix arbres est excessif.","opinion, assumée comme telle"],
         ["Le comité a déposé ses feuilles de comptage le 3 octobre.","fait vérifiable"],
         ["Le comité prétend avoir compté trois cent quarante-deux arbres.","propos rapporté — mais « prétend » ajoute un jugement"],
       ]},

      {t:'piege', h:"Trois pièges dans les textes que vous lirez",
       rows:[
         ["« prétend », « admet », « reconnaît »","« dit », « affirme », « déclare »",
          "Ces verbes rapportent tous, mais les trois premiers jugent en passant : « admettre » suppose une faute, « prétendre » suppose un mensonge. Une rédaction rigoureuse s'en tient aux neutres."],
         ["un chiffre sans son unité de comparaison","le même chiffre avec ce à quoi il se compare",
          "« Onze mille dollars d'entretien » ne veut rien dire seul : c'est beaucoup pour un parc de quartier, c'est peu pour un budget municipal de quarante millions. Le chiffre isolé sert celui qui le donne."],
         ["« tout le monde sait que… »","une source, ou rien",
          "Cette formule remplace l'argument qui manque. Dès que vous la lisez, cherchez ce qu'elle recouvre : neuf fois sur dix, il n'y a rien derrière."],
       ]},

      {t:'check', h:"Est-ce que c'est clair maintenant ?",
       p:"Quatre questions rapides.",
       qs:[
         {q:"« D'après la Ville, le terrain coûtait onze mille dollars par an » est…", opts:["un fait","un propos rapporté"], ok:1,
          fb:"« D'après » nomme une source : le journal rapporte, il ne vérifie pas."},
         {q:"« Le boisé couvre onze hectares » est…", opts:["un fait","une opinion"], ok:0,
          fb:"Cela se vérifie au cadastre : c'est un fait."},
         {q:"« Le terrain aurait été évalué à deux millions » veut dire…", opts:["que c'est probable","qu'on nous l'a dit sans le vérifier"], ok:1,
          fb:"C'est le conditionnel journalistique : information rapportée, source non nommée."},
         {q:"Dans votre lettre, la meilleure façon de donner votre avis est…", opts:["de l'écrire comme un fait","de l'annoncer comme un avis"], ok:1,
          fb:"Une opinion annoncée est inattaquable ; une opinion déguisée en fait se démolit en une ligne."},
       ]},

      {t:'revoir', h:"À retenir",
       p:"Trois questions devant chaque phrase : <b>est-ce que ça se vérifie ?</b> (fait) · <b>est-ce que ça se discute ?</b> (opinion) · <b>est-ce que quelqu'un d'autre le dit ?</b> (propos rapporté). Dans votre propre texte, séparez-les à voix haute : ce que je sais, ce qu'on m'a dit, ce que j'en pense."},
    ]
  },

  t1passif: {
    eye:'Mini-leçon', tit:"La phrase qui efface celui qui a décidé",
    blocs:[
      {t:'texte', h:"Une construction, et un usage politique",
       p:"La voix passive est une construction ordinaire du français : elle sert à mettre en tête ce dont on parle. Mais elle a une propriété que rien d'autre ne possède : elle permet de <b>supprimer complètement</b> celui qui agit. « Le règlement a été adopté » est une phrase complète, correcte, et sans responsable. C'est pour cela qu'on la trouve partout dans les communiqués.",
       note:"Ce n'est pas une faute et ce n'est pas toujours malhonnête. C'est un endroit où il faut se poser une question."},

      {t:'ana', h:"Comment elle se fabrique",
       p:"Trois gestes : le complément direct passe en tête, le verbe devient être + participe passé au même temps, et l'auteur de l'action recule derrière « par » — ou disparaît.",
       mots:[['Actif',"Le conseil a adopté le règlement."],['Passif',"Le règlement a été adopté par le conseil.",true],['Passif sans agent',"Le règlement a été adopté."]],
       say:"Le conseil a adopté le règlement. Le règlement a été adopté par le conseil.",
       note:"Le temps ne change pas : passé composé actif, passé composé passif. C'est l'auxiliaire être qui porte le temps."},

      {t:'ana', h:"L'accord du participe",
       p:"Au passif, le participe s'accorde toujours avec le sujet. C'est la faute la plus visible à l'écrit, et elle se corrige en cherchant simplement de quoi on parle.",
       mots:[['Féminin',"La cession a été autorisée."],['Pluriel',"Les logements seront livrés.",true],['Négatif',"L'évaluation n'a pas été publiée."]],
       say:"La cession a été autorisée. Les logements seront livrés. L'évaluation n'a pas été publiée.",
       note:"Test rapide : remplacez le sujet par « elle » ou « ils » et écoutez la fin du participe."},

      {t:'ana', h:"Le passif sans agent, et ce qu'il cache",
       p:"Quand « par quelqu'un » manque, la phrase raconte un événement sans acteur. Parfois l'acteur est évident et inutile ; parfois il est justement ce qu'on ne veut pas nommer.",
       mots:[['Neutre',"L'assemblée a été convoquée pour jeudi."],['Suspect',"Il a été décidé de ne pas publier l'évaluation.",true],['Très suspect',"Des erreurs ont été commises."]],
       say:"Il a été décidé de ne pas publier l'évaluation. Des erreurs ont été commises.",
       note:"« Des erreurs ont été commises » est la phrase la plus célèbre de ce genre. Personne n'a rien fait, tout est arrivé tout seul."},

      {t:'labo', h:"Retournez la phrase",
       p:"Choisissez une phrase et une voix.",
       axes:[
         {id:'p', lbl:'Quelle phrase ?', opts:[['a','le règlement'],['b','les arbres'],['c',"l'évaluation"]]},
         {id:'v', lbl:'Quelle voix ?', opts:[['1','active'],['2','passive']]}],
       out:{
         a1:{w:["Le conseil a adopté le règlement."], say:"Le conseil a adopté le règlement.", n:"on sait tout de suite qui a décidé"},
         a2:{w:["Le règlement a été adopté."], say:"Le règlement a été adopté.", n:"le sujet du texte vient en tête, l'auteur disparaît"},
         b1:{w:["Le comité a compté trois cent quarante-deux arbres."], say:"Le comité a compté trois cent quarante-deux arbres.", n:"le comptage est attribué à quelqu'un"},
         b2:{w:["Trois cent quarante-deux arbres ont été comptés."], say:"Trois cent quarante-deux arbres ont été comptés.", n:"le chiffre paraît officiel : personne ne l'assume"},
         c1:{w:["La Ville n'a pas publié l'évaluation."], say:"La Ville n'a pas publié l'évaluation.", n:"un reproche adressé à quelqu'un"},
         c2:{w:["L'évaluation n'a pas été publiée."], say:"L'évaluation n'a pas été publiée.", n:"un simple état de fait, sans coupable"},
       },
       note:"Écoutez les deux versions de chaque paire : c'est la même information, et ce n'est pas le même texte."},

      {t:'ex', h:"Six passifs à interroger",
       p:"À gauche ce qui est écrit, à droite la question à poser.",
       rows:[
         ["Le terrain a été évalué.","par qui, et le document est-il public ?"],
         ["Une consultation a été tenue.","quand, et combien de personnes y étaient ?"],
         ["Le projet a été bonifié.","bonifié par qui, et sur quel point ?"],
         ["Les préoccupations ont été entendues.","entendues par qui, et qu'est-ce qui a changé ?"],
         ["Il a été convenu de reporter la décision.","convenu entre qui et qui ?"],
         ["Le dossier a été transmis au service concerné.","à quelle date, et par quel moyen ?"],
       ]},

      {t:'piege', h:"Deux confusions courantes",
       rows:[
         ["« elle est arrivée » pris pour un passif","reconnaître le passé composé des verbes de mouvement",
          "Le test : peut-on ajouter « par quelqu'un » ? « Elle est attendue par le comité » fonctionne, donc c'est un passif. « Elle est arrivée par le comité » ne veut rien dire : c'est un passé composé."],
         ["retourner un passif sans retrouver l'agent","écrire d'abord qui agit",
          "Pour passer « l'évaluation n'a pas été publiée » à l'actif, il faut savoir qui aurait dû la publier. Si vous ne le savez pas, vous venez de trouver votre question."],
       ]},

      {t:'check', h:"Est-ce que c'est clair maintenant ?",
       p:"Trois questions rapides.",
       qs:[
         {q:"« La cession a été autorisé » — qu'est-ce qui cloche ?", opts:["l'accord du participe","le temps du verbe"], ok:0,
          fb:"Le participe s'accorde avec le sujet : la cession a été autoris<b>ée</b>."},
         {q:"« Des erreurs ont été commises » ne dit pas…", opts:["ce qui est arrivé","qui les a commises"], ok:1,
          fb:"C'est exactement ce que le passif sans agent permet de ne pas dire."},
         {q:"Devant un passif sans « par », le bon réflexe est…", opts:["de noter la question « par qui ? »","de récrire la phrase"], ok:0,
          fb:"C'est souvent la meilleure question à poser à une assemblée publique."},
       ]},

      {t:'revoir', h:"À retenir",
       p:"Passif = <b>être</b> + participe passé, accordé avec le sujet, et l'auteur derrière <b>par</b> — quand il y est. Un passif sans « par » est un endroit où quelqu'un manque : notez la question plutôt que de récrire la phrase."},
    ]
  },

  t1nommer: {
    eye:'Mini-leçon', tit:"Le mot choisi n'est jamais neutre",
    blocs:[
      {t:'texte', h:"Le cadrage, expliqué en une phrase",
       p:"Deux journaux peuvent écrire sur les mêmes onze hectares sans employer un seul mot commun. L'un parle d'un <b>boisé mature</b>, l'autre d'un <b>terrain municipal sous-utilisé</b>. Ni l'un ni l'autre ne ment ; chacun a choisi le mot qui appelle la conclusion qu'il souhaite. Ce choix s'appelle le cadrage, et c'est le procédé le plus efficace de tous — parce que le lecteur croit avoir lu un fait.",
       note:"On ne s'en défend pas en se méfiant. On s'en défend en nommant l'écart : « il écrit terrain vague, le cadastre dit boisé »."},

      {t:'ana', h:"Le mot propre et le mot qui juge",
       p:"Presque chaque chose a un nom neutre et plusieurs noms orientés. Le neutre est souvent le plus administratif, et le plus ennuyeux — c'est un bon signe.",
       mots:[['Neutre',"le terrain municipal du lot 3 214"],['Orienté vers la protection',"le poumon vert du quartier",true],['Orienté vers le projet',"un terrain vague à l'abandon"]],
       say:"Le terrain municipal du lot 3 214. Le poumon vert du quartier. Un terrain vague à l'abandon.",
       note:"Dans votre lettre, employez le mot neutre au moins une fois : cela montre que vous connaissez le dossier et pas seulement votre camp."},

      {t:'ana', h:"Les mots qui grossissent et les mots qui rapetissent",
       p:"Un même geste se raconte en grand ou en petit selon le verbe et le nom choisis. Les deux versions sont défendables devant un tribunal ; elles ne produisent pas le même lecteur.",
       mots:[['En grand',"le conseil a bradé un bien public"],['En petit',"le conseil a régularisé la situation d'un lot",true],['Au milieu',"le conseil a cédé un terrain pour un dollar"]],
       say:"Le conseil a bradé un bien public. Le conseil a régularisé la situation d'un lot. Le conseil a cédé un terrain pour un dollar.",
       note:"« Céder pour un dollar » est le seul des trois qu'on peut vérifier. C'est celui à employer."},

      {t:'ana', h:"Le nom qui contient déjà la conclusion",
       p:"Certains mots portent leur jugement à l'intérieur. Les employer, c'est avoir gagné avant d'avoir argumenté — et c'est aussi ce qui rend une lettre attaquable.",
       mots:[['Le mot chargé',"un saccage · un enterrement · un cadeau au promoteur"],["Ce qu'il fait","il conclut à la place du lecteur",true],['Le remplaçant',"l'abattage de quatre-vingt-dix arbres"]],
       say:"Un saccage. L'abattage de quatre-vingt-dix arbres.",
       note:"Un mot chargé donne un instant de satisfaction et coûte la moitié de vos lecteurs. Gardez-en un, au plus, et placez-le à la fin."},

      {t:'ex', h:"Huit façons de nommer la même chose",
       p:"À gauche la désignation, à droite ce qu'elle fait entendre.",
       rows:[
         ["le boisé Sainte-Perpétue","un lieu qui a un nom, donc une histoire"],
         ["un terrain municipal sous-utilisé","une ressource qui dort et qu'on gaspille"],
         ["un actif de la Ville","un bien qui s'évalue en dollars, donc qui se vend"],
         ["les onze hectares","une surface neutre, sans arbres ni promeneurs"],
         ["le poumon vert du quartier","un organe vital dont la perte serait une atteinte"],
         ["l'ancienne cour de voirie","un endroit déjà abîmé, qu'on ne perdrait pas"],
         ["la parcelle visée par le règlement","un objet de dossier, vu du bureau"],
         ["le futur quartier Sainte-Perpétue","une chose déjà faite, dont il reste à fixer la date"],
       ]},

      {t:'piege', h:"Deux pièges quand c'est vous qui écrivez",
       rows:[
         ["employer le vocabulaire de votre camp du début à la fin","nommer la chose neutrement au moins une fois",
          "Un texte qui n'emploie que les mots d'un camp ne convainc que ce camp. La personne que vous voulez atteindre est celle qui hésite, et elle repère le vocabulaire militant en trois lignes."],
         ["reprendre le mot de l'adversaire pour le contester","le remplacer sans le commenter",
          "Répéter « terrain vague » pour dire que ce n'en est pas un installe quand même l'image dans la tête du lecteur. Écrivez « le boisé », et donnez le nombre d'arbres."],
       ]},

      {t:'check', h:"Est-ce que c'est clair maintenant ?",
       p:"Trois questions rapides.",
       qs:[
         {q:"« Un cadeau au promoteur » est un mot chargé parce qu'il…", opts:["conclut à la place du lecteur","est trop familier"], ok:0,
          fb:"Il contient déjà le jugement : le lecteur n'a plus rien à examiner."},
         {q:"La désignation la plus vérifiable est…", opts:["le poumon vert du quartier","le terrain municipal du lot 3 214"], ok:1,
          fb:"C'est la plus ennuyeuse et la seule qu'on peut aller vérifier."},
         {q:"Dans une lettre, employer une fois le mot neutre sert à…", opts:["montrer qu'on connaît le dossier","allonger le texte"], ok:0,
          fb:"C'est ce qui vous distingue d'un texte de militant, aux yeux de celui qui hésite."},
       ]},

      {t:'revoir', h:"À retenir",
       p:"Le premier écart entre deux articles n'est pas dans les chiffres : il est dans les <b>mots choisis pour nommer la chose</b>. Relevez-les, mettez-les côte à côte, et employez vous-même une désignation vérifiable — quitte à ajouter, une seule fois, le mot qui fait image."},
    ]
  },

  t2edito: {
    eye:'Mini-leçon', tit:"Démonter un texte d'opinion",
    blocs:[
      {t:'texte', h:"Un texte d'opinion est une construction",
       p:"Un éditorial n'est pas une suite d'idées : c'est un bâtiment. Une accroche, une thèse, des arguments, une concession, une réfutation, une conclusion, un appel. Quand vous connaissez les sept pièces, vous lisez trois fois plus vite et vous répondez beaucoup mieux : au lieu de contester tout le texte, vous visez la pièce faible.",
       note:"C'est aussi le plan que vous suivrez pour écrire la vôtre. On apprend d'abord à démonter."},

      {t:'ana', h:"La thèse — une phrase, et une seule",
       p:"L'idée que le texte veut faire accepter. Elle se trouve à la fin du premier paragraphe ou au début du deuxième, presque toujours. Si vous ne la trouvez pas, le texte n'en a peut-être pas.",
       mots:[['La forme',"Le conseil a eu raison d'autoriser la cession, et il fallait le faire maintenant."],['Le test',"peut-on être en désaccord avec cette phrase ?",true],['Si non',"ce n'est pas une thèse, c'est un constat"]],
       say:"Le conseil a eu raison d'autoriser la cession, et il fallait le faire maintenant.",
       note:"Repérez aussi ce que la thèse contient en plus de l'idée : ici, « maintenant » ajoute l'urgence, qui devra être défendue séparément."},

      {t:'ana', h:"La concession — la pièce qui trompe",
       p:"Le moment où l'auteur donne raison à l'autre camp. Beaucoup de lecteurs la prennent pour un aveu et s'arrêtent là. C'est l'inverse : la concession désarme l'objection avant qu'on la pose.",
       mots:[['Les marques',"Il est vrai que… · Certes… · Bien que…"],['Ce qui suit toujours',"mais, il n'en reste pas moins que",true],['Le vrai test',"la concession porte-t-elle sur un point important ?"]],
       say:"Il est vrai que le conseil a voté quatre jours après l'évaluation. Mais cela ne rend pas le projet moins nécessaire.",
       note:"Une concession sur un détail est un ornement. Une concession sur le point central est un signe d'honnêteté — et c'est là que le texte devient fort."},

      {t:'ana', h:"L'objection anticipée — « on nous dira que… »",
       p:"L'auteur formule lui-même l'argument adverse, puis y répond. C'est efficace et un peu déloyal : c'est lui qui choisit la version de l'objection à laquelle il répondra.",
       mots:[['La marque',"On nous dira que le terrain de l'aréna ferait aussi bien l'affaire."],['Le réflexe',"est-ce bien l'objection la plus forte ?",true],['Souvent',"il répond à la plus faible des objections possibles"]],
       say:"On nous dira que le terrain de l'aréna ferait aussi bien l'affaire.",
       note:"C'est le meilleur endroit pour attaquer un texte d'opinion : montrez que l'objection réelle n'était pas celle-là."},

      {t:'ana', h:"L'appel — sans lui, le texte n'a servi à personne",
       p:"La dernière phrase dit ce qu'il faut faire, et à qui. Un éditorial qui se termine par « il faudra y réfléchir » n'a rien demandé et n'obtiendra rien.",
       mots:[['La forme',"Allez à l'assemblée de jeudi et posez vos questions."],['Les deux éléments',"une action précise, un destinataire précis",true],['À noter',"l'appel révèle souvent le vrai but du texte"]],
       say:"Allez à l'assemblée de jeudi et posez vos questions.",
       note:"Lisez toujours l'appel en premier : il vous dit ce que l'auteur voulait obtenir, et donc comment lire tout le reste."},

      {t:'ex', h:"Les sept pièces, dans l'ordre habituel",
       p:"À gauche la pièce, à droite ce qu'elle fait.",
       rows:[
         ["l'accroche","donne envie de lire — on peut la retirer sans rien perdre"],
         ["la thèse","l'idée à faire accepter, en une phrase discutable"],
         ["les arguments","ce qui soutient la thèse, idéalement des faits vérifiables"],
         ["la concession","donne raison à l'autre camp sur un point"],
         ["la réfutation","répond à la concession sans la nier"],
         ["l'objection anticipée","formule l'argument adverse pour y répondre d'avance"],
         ["la conclusion et l'appel","résume, puis demande une action à quelqu'un de précis"],
       ]},

      {t:'piege', h:"Trois faiblesses à repérer, et à ne pas reproduire",
       rows:[
         ["l'argument d'évidence","un fait vérifiable",
          "« Tout le monde sait que… », « il est évident que… » : ces formules remplacent l'argument qui manque. Dans un texte, elles marquent l'endroit le plus fragile."],
         ["l'attaque de la personne","l'examen de l'argument",
          "« Le comité est composé de propriétaires aisés » ne dit rien du comptage des arbres. C'est efficace et ça ne prouve rien."],
         ["la fausse alternative","les autres possibilités",
          "« C'est ce projet-là ou rien » ferme la discussion en supposant qu'il n'existe que deux voies. Cherchez toujours la troisième : elle existe presque toujours, et souvent elle a été écartée sans étude."],
       ]},

      {t:'check', h:"Est-ce que c'est clair maintenant ?",
       p:"Quatre questions rapides.",
       qs:[
         {q:"La thèse d'un texte d'opinion se reconnaît à ce qu'on peut…", opts:["la vérifier","en être en désaccord"], ok:1,
          fb:"Une phrase avec laquelle personne ne peut être en désaccord n'est pas une thèse."},
         {q:"Une concession sert surtout à…", opts:["affaiblir le texte","désarmer l'objection avant qu'on la pose"], ok:1,
          fb:"Elle prouve que l'auteur a lu ses adversaires, et elle rend le reste plus crédible."},
         {q:"« On nous dira que… » introduit…", opts:["une objection anticipée","une conclusion"], ok:0,
          fb:"L'auteur formule lui-même l'argument adverse — celui qu'il a choisi."},
         {q:"Lire l'appel en premier permet de savoir…", opts:["ce que l'auteur veut obtenir","si le texte est long"], ok:0,
          fb:"L'appel révèle le but, et donc comment lire tout ce qui précède."},
       ]},

      {t:'revoir', h:"À retenir",
       p:"Sept pièces : accroche · <b>thèse</b> · arguments · <b>concession</b> · réfutation · objection anticipée · conclusion et <b>appel</b>. Lisez l'appel d'abord, la thèse ensuite, et cherchez la concession : c'est là que le texte est le plus honnête et le plus attaquable à la fois."},
    ]
  },

  t2conc: {
    eye:'Mini-leçon', tit:"Concéder avant d'avancer",
    blocs:[
      {t:'texte', h:"La forme la plus utile de tout le niveau 8",
       p:"Dans un débat, celui qui n'accorde jamais rien perd l'auditoire en trois minutes. La <b>concession</b> est ce qui vous rend écoutable : vous reconnaissez le point exact où l'autre a raison, puis vous avancez le vôtre. Ce n'est ni de la faiblesse ni de la politesse — c'est une technique, et le français a une demi-douzaine de tournures faites pour ça.",
       note:"La contrepartie est qu'une concession doit être vraie. Une fausse concession — « je comprends votre point de vue, mais » — ne concède rien et s'entend immédiatement."},

      {t:'ana', h:"Certes… mais · Il est vrai que… mais",
       p:"Le couple le plus employé à l'écrit. La première partie reste courte ; la seconde porte le poids de la phrase.",
       mots:[['On dit',"Certes le terrain a une valeur, mais il n'a jamais rapporté un dollar."],['La règle',"la concession d'abord, votre point ensuite",true],['Pourquoi',"le lecteur retient la seconde moitié"]],
       say:"Certes le terrain a une valeur, mais il n'a jamais rapporté un dollar.",
       note:"Ne jamais inverser : « il n'a jamais rien rapporté, certes il a une valeur » laisse l'auditeur sur l'argument adverse."},

      {t:'ana', h:"Bien que · quoique + subjonctif",
       p:"La concession en un seul bloc, plus soutenue. Ces deux connecteurs demandent le subjonctif, sans exception.",
       mots:[['On dit',"Bien que le projet soit nécessaire, la procédure reste critiquable."],['Le verbe',"soit, ait, puisse, fasse — jamais l'indicatif",true],['Variante',"Quoique le vote soit valide, il est petit."]],
       say:"Bien que le projet soit nécessaire, la procédure reste critiquable.",
       note:"C'est la faute la plus fréquente du niveau : « bien que c'est » est immédiatement repéré à l'écrit comme à l'oral."},

      {t:'ana', h:"Même si + indicatif",
       p:"Il ressemble à « bien que » et se construit à l'opposé. « Même si » pose le fait comme réel, donc l'indicatif.",
       mots:[['On dit',"Même si le vote a été serré, il est parfaitement valide."],['Le contraste',"bien que + subjonctif · même si + indicatif",true],['Nuance',"« même si » insiste plus fortement sur le fait"]],
       say:"Même si le vote a été serré, il est parfaitement valide.",
       note:"Un moyen mnémotechnique : « même si » contient « si », et « si » ne prend jamais le subjonctif."},

      {t:'ana', h:"Or — le mot qui renverse",
       p:"« Or » introduit le fait qui fait tomber ce qui précède. C'est le connecteur le plus puissant du français argumentatif, et le moins employé par ceux qui apprennent la langue.",
       mots:[['On dit',"La Ville affirme avoir tout étudié. Or, aucune étude n'existe sur le terrain de l'aréna."],['La place',"en tête de phrase, suivi d'une virgule",true],['Le sens',"voici le fait qui change tout"]],
       say:"La Ville affirme avoir tout étudié. Or, aucune étude n'existe sur le terrain de l'aréna.",
       note:"Un « or » bien placé vaut trois paragraphes. Un « or » employé comme simple « et » ne veut plus rien dire : n'en mettez qu'un par texte."},

      {t:'labo', h:"Choisissez la bonne charnière",
       p:"Choisissez un rapport et un exemple.",
       axes:[
         {id:'r', lbl:'Quel rapport ?', opts:[['a','concéder'],['b','opposer'],['c','renverser'],['d','fermer la concession']]},
         {id:'n', lbl:'Quel exemple ?', opts:[['1','le premier'],['2','le second']]}],
       out:{
         a1:{w:["Certes le besoin est réel, mais la procédure ne l'était pas."], say:"Certes le besoin est réel, mais la procédure ne l'était pas.", n:"on accorde d'abord, on avance ensuite"},
         a2:{w:["Bien que le projet soit nécessaire, je signerai le registre."], say:"Bien que le projet soit nécessaire, je signerai le registre.", n:"bien que demande le subjonctif : soit"},
         b1:{w:["Le comité compte trois cent quarante-deux arbres ; le promoteur en compte quatre-vingt-dix."], say:"Le comité compte trois cent quarante-deux arbres ; le promoteur en compte quatre-vingt-dix.", n:"deux faits mis côte à côte, sans donner raison"},
         b2:{w:["Le premier article ouvre sur les logements ; en revanche, le second ouvre sur l'heure du vote."], say:"Le premier article ouvre sur les logements ; en revanche, le second ouvre sur l'heure du vote.", n:"en revanche oppose sans concéder"},
         c1:{w:["On nous dit que tout a été étudié. Or, rien ne l'a été."], say:"On nous dit que tout a été étudié. Or, rien ne l'a été.", n:"le fait qui fait tomber ce qui précède"},
         c2:{w:["Le règlement garantit les logements. Or, la pénalité n'a jamais été appliquée ailleurs."], say:"Le règlement garantit les logements. Or, la pénalité n'a jamais été appliquée ailleurs.", n:"un or qui déplace la discussion"},
         d1:{w:["Le projet répond à un besoin ; il n'en reste pas moins que personne n'a été consulté."], say:"Le projet répond à un besoin ; il n'en reste pas moins que personne n'a été consulté.", n:"on ferme la concession sans la nier"},
         d2:{w:["Le délai est réel ; cela ne justifie pas de voter à vingt-deux heures cinquante."], say:"Le délai est réel ; cela ne justifie pas de voter à vingt-deux heures cinquante.", n:"même mouvement, formulation plus simple"},
       },
       note:"Écoutez chaque paire : le rapport logique s'entend dans la mélodie autant qu'il se lit dans le mot."},

      {t:'ex', h:"Le répertoire, en une page",
       p:"À gauche le connecteur, à droite ce qu'il fait.",
       rows:[
         ["certes… mais","concéder puis avancer, à l'écrit comme à l'oral"],
         ["bien que · quoique + subjonctif","concéder en un seul bloc, registre soutenu"],
         ["même si + indicatif","concéder en posant le fait comme certain"],
         ["il n'en reste pas moins que","fermer une concession sans la nier"],
         ["en revanche · par contre","opposer deux faits, sans donner raison à personne"],
         ["alors que · tandis que","mettre deux faits en regard dans la même phrase"],
         ["or","introduire le fait qui renverse ce qui précède"],
         ["cependant · toutefois · néanmoins","nuancer, puis poursuivre"],
       ]},

      {t:'piege', h:"Trois pièges de la concession",
       rows:[
         ["« je comprends, mais »","nommer le point exact accordé",
          "« Je comprends votre point de vue » ne concède rien du tout : c'est une formule de politesse. Dites ce que l'autre a de juste, précisément, et l'auditoire vous écoutera."],
         ["« bien que c'est »","« bien que ce soit »",
          "Bien que et quoique demandent le subjonctif. Cette faute-là se remarque plus que toutes les autres à ce niveau."],
         ["concéder trois fois dans le même texte","une concession, bien placée",
          "Trois concessions font un texte sans position. Une seule, sur le point central, fait un texte qu'on ne peut pas balayer."],
       ]},

      {t:'check', h:"Est-ce que c'est clair maintenant ?",
       p:"Quatre questions rapides.",
       qs:[
         {q:"Après « bien que », on emploie…", opts:["l'indicatif","le subjonctif"], ok:1,
          fb:"Toujours le subjonctif : bien que le projet <b>soit</b> nécessaire."},
         {q:"Après « même si », on emploie…", opts:["l'indicatif","le subjonctif"], ok:0,
          fb:"L'indicatif : même si le vote <b>a été</b> serré."},
         {q:"« Or » introduit…", opts:["une conséquence","le fait qui renverse ce qui précède"], ok:1,
          fb:"C'est sa fonction propre, et elle est puissante — un seul par texte."},
         {q:"Dans « certes… mais », l'argument qu'on retient est…", opts:["le premier","le second"], ok:1,
          fb:"Le lecteur retient la seconde moitié : placez-y votre point."},
       ]},

      {t:'revoir', h:"À retenir",
       p:"<b>Certes… mais</b> et <b>bien que</b> + subjonctif pour concéder ; <b>même si</b> + indicatif, qui leur ressemble et se construit autrement ; <b>en revanche</b> pour opposer sans concéder ; <b>or</b> pour renverser ; <b>il n'en reste pas moins que</b> pour refermer. Une concession vraie, bien placée, vaut trois arguments."},
    ]
  },

  t2subj: {
    eye:'Mini-leçon', tit:"Le subjonctif de l'opinion et du doute",
    blocs:[
      {t:'texte', h:"Une seule idée derrière tous les cas",
       p:"Le subjonctif dit que ce qui suit n'est <b>pas posé comme réel</b> : c'est souhaité, craint, apprécié, douteux, ou seulement envisagé. L'indicatif dit l'inverse : c'est posé comme un fait, même s'il est faux. Tous les cas particuliers qu'on vous a fait apprendre découlent de là.",
       note:"C'est pour cette raison que « je pense que » prend l'indicatif : quand j'affirme ce que je pense, je le pose comme réel."},

      {t:'ana', h:"La négation retourne les verbes d'opinion",
       p:"Le point le plus utile de toute la leçon, et le plus employé dans un débat.",
       mots:[['Affirmatif',"Je pense que le projet est bon."],['Négatif',"Je ne pense pas que le projet soit bon.",true],['Interrogatif',"Croyez-vous que ce soit suffisant ?"]],
       say:"Je pense que le projet est bon. Je ne pense pas que le projet soit bon.",
       note:"Même chose pour croire, trouver, être sûr, être certain, il me semble. À l'affirmative, indicatif ; niés ou questionnés, subjonctif."},

      {t:'ana', h:"Les verbes de sentiment, toujours au subjonctif",
       p:"Craindre, regretter, s'étonner, être content, trouver dommage : ce qui suit n'est pas donné comme un fait, il est donné comme ce qui me touche.",
       mots:[['On dit',"Je regrette que l'évaluation n'ait pas été publiée."],['Autre',"Je crains que ce débat ne finisse mal.",true],['Le « ne » explétif',"il ne signifie pas la négation, après craindre"]],
       say:"Je regrette que l'évaluation n'ait pas été publiée. Je crains que ce débat ne finisse mal.",
       note:"Le « ne » de « je crains qu'il ne vienne » n'est pas une négation : il vient : c'est ce que je crains. On peut l'omettre à l'oral."},

      {t:'ana', h:"Les tournures impersonnelles, et le partage",
       p:"Toutes ne fonctionnent pas pareil, et le partage suit exactement la règle du réel.",
       mots:[['Appréciation → subjonctif',"Il est important que la Ville publie l'évaluation."],['Certitude → indicatif',"Il est évident que la population veut des logements.",true],['Autres subjonctifs',"il faut que · il vaut mieux que · il est regrettable que"]],
       say:"Il est important que la Ville publie l'évaluation. Il est évident que la population veut des logements.",
       note:"Testez avec « est-ce que je pose ce fait comme réel ? » : il est certain que → oui, indicatif. Il est souhaitable que → non, subjonctif."},

      {t:'ana', h:"Les connecteurs qui l'imposent",
       p:"Certains mots de liaison entraînent le subjonctif quel que soit le sens : il n'y a rien à décider, seulement à retenir.",
       mots:[['Concession',"bien que · quoique"],['But',"pour que · afin que",true],['Condition et temps',"à moins que · avant que · sans que · pourvu que"]],
       say:"Bien que le comité ait raison, je voterai pour. Nous demandons un report pour que chacun puisse se prononcer.",
       note:"Après que demande en principe l'indicatif — l'action a eu lieu. L'usage hésite, et personne ne vous en tiendra rigueur."},

      {t:'labo', h:"Indicatif ou subjonctif ?",
       p:"Choisissez un déclencheur et un verbe.",
       axes:[
         {id:'d', lbl:'Quel déclencheur ?', opts:[['a','je pense que'],['b','je ne pense pas que'],['c','il est important que'],['d','il est certain que']]},
         {id:'v', lbl:'Quel verbe ?', opts:[['1','être'],['2','pouvoir']]}],
       out:{
         a1:{w:["Je pense que c'est nécessaire."], say:"Je pense que c'est nécessaire.", n:"affirmatif : indicatif"},
         a2:{w:["Je pense qu'on peut encore discuter."], say:"Je pense qu'on peut encore discuter.", n:"affirmatif : indicatif"},
         b1:{w:["Je ne pense pas que ce soit nécessaire."], say:"Je ne pense pas que ce soit nécessaire.", n:"nié : subjonctif — soit"},
         b2:{w:["Je ne pense pas qu'on puisse encore discuter."], say:"Je ne pense pas qu'on puisse encore discuter.", n:"nié : subjonctif — puisse"},
         c1:{w:["Il est important que ce soit public."], say:"Il est important que ce soit public.", n:"appréciation : subjonctif"},
         c2:{w:["Il est important que chacun puisse se prononcer."], say:"Il est important que chacun puisse se prononcer.", n:"appréciation : subjonctif"},
         d1:{w:["Il est certain que c'est légal."], say:"Il est certain que c'est légal.", n:"certitude : indicatif"},
         d2:{w:["Il est certain qu'on peut contester."], say:"Il est certain qu'on peut contester.", n:"certitude : indicatif"},
       },
       note:"Écoutez la différence entre « c'est » et « ce soit » : c'est tout ce qui sépare une affirmation d'un doute."},

      {t:'ex', h:"Les formes irrégulières qui couvrent presque tout",
       p:"À gauche l'infinitif, à droite le subjonctif présent.",
       rows:[
         ["être","que je sois · qu'il soit · que nous soyons · qu'ils soient"],
         ["avoir","que j'aie · qu'il ait · que nous ayons · qu'ils aient"],
         ["aller","que j'aille · que nous allions · qu'ils aillent"],
         ["faire","que je fasse · que nous fassions"],
         ["pouvoir","que je puisse · que nous puissions"],
         ["savoir","que je sache · que nous sachions"],
         ["les verbes réguliers","sur la 3e personne du pluriel : ils publient → que je publie"],
       ]},

      {t:'piege', h:"Trois pièges du subjonctif dans un débat",
       rows:[
         ["« je ne crois pas que c'est vrai »","« je ne crois pas que ce soit vrai »",
          "La négation d'un verbe d'opinion entraîne le subjonctif. C'est la construction la plus fréquente d'une discussion, donc la faute la plus souvent entendue."],
         ["« après que » au subjonctif","« après que » à l'indicatif",
          "L'action a eu lieu : après qu'il <b>a</b> parlé. La faute est si répandue que plus personne ne la relève, mais à l'écrit elle se voit."],
         ["mettre du subjonctif partout par prudence","le réserver à ses déclencheurs",
          "Un texte truffé de subjonctifs inutiles se lit aussi mal qu'un texte qui n'en a aucun. Quand vous affirmez, affirmez : l'indicatif est la forme normale du français."],
       ]},

      {t:'check', h:"Est-ce que c'est clair maintenant ?",
       p:"Quatre questions rapides.",
       qs:[
         {q:"« Je ne pense pas que ce projet ___ la solution » demande…", opts:["est","soit"], ok:1,
          fb:"Verbe d'opinion nié : subjonctif."},
         {q:"« Il est évident que la population ___ des logements » demande…", opts:["veut","veuille"], ok:0,
          fb:"« Il est évident que » pose un fait : indicatif."},
         {q:"Après « pour que », on emploie…", opts:["le subjonctif","l'indicatif"], ok:0,
          fb:"Le but n'est pas réalisé : subjonctif."},
         {q:"« Je crains qu'il ne vienne » veut dire…", opts:["j'ai peur qu'il vienne","j'ai peur qu'il ne vienne pas"], ok:0,
          fb:"Le « ne » est explétif : il ne nie rien."},
       ]},

      {t:'revoir', h:"À retenir",
       p:"Le subjonctif dit <b>ce qui n'est pas posé comme réel</b>. Trois déclencheurs à retenir avant tous les autres : les verbes d'opinion <b>niés ou questionnés</b>, les verbes de <b>sentiment</b>, et les tournures d'<b>appréciation</b> (il faut que, il est important que). Les certitudes gardent l'indicatif."},
    ]
  },

  t2trois: {
    eye:'Mini-leçon', tit:"Suivre douze minutes sans interlocuteur",
    blocs:[
      {t:'texte', h:"Pourquoi un exposé long est plus difficile qu'une conversation",
       p:"Dans une conversation, l'autre s'arrête, reformule, vous laisse le temps. Un exposé — une chronique, un discours, une conférence — ne fait rien de tout cela : il avance à son rythme, sans se soucier de vous. Le programme du niveau 8 le demande explicitement : « suivre le déroulement d'exposés bien structurés ». C'est un savoir-faire d'écoute, et il s'apprend.",
       note:"On ne rattrape jamais un exposé en essayant de tout comprendre. On le suit en cherchant sa structure."},

      {t:'ana', h:"Première écoute — de quel côté est-il ?",
       p:"Ne cherchez rien d'autre. Un exposé d'opinion annonce sa position dans les trente premières secondes, ou à la fin du premier tiers. Une fois que vous la tenez, tout le reste se range tout seul.",
       mots:[["Ce qu'on cherche","une phrase du type : je suis pour, je suis contre"],['Le repère',"« voilà », « je vous le dis tout de suite »",true],['Si on ne trouve pas',"l'exposé est informatif, pas argumentatif"]],
       say:"Je suis pour le projet du boisé Sainte-Perpétue. Voilà.",
       note:"Écoutez le ton autant que les mots : la position s'entend souvent avant d'être dite."},

      {t:'ana', h:"Deuxième écoute — les chiffres",
       p:"Notez uniquement les nombres et ce à quoi ils se rapportent. Trois ou quatre suffisent. Ce sont eux qui vous permettront de répondre : un chiffre se vérifie, une impression ne se discute pas.",
       mots:[['On note',"0,3 % · 45 logements · 2 M$ · 4 jours · 5 projets en 15 ans"],['On ne note pas',"les adjectifs, les exemples, les anecdotes",true],['Le test',"pourriez-vous répéter le chiffre à quelqu'un ?"]],
       say:"Le taux d'inoccupation est de zéro virgule trois pour cent.",
       note:"Un chiffre entendu et mal noté est pire que rien : notez-le avec son unité et sa source, ou pas du tout."},

      {t:'ana', h:"Troisième écoute — ce qui est dit deux fois",
       p:"Une répétition n'est jamais un hasard dans un texte préparé. Ce qui revient est ce à quoi l'auteur tient, et c'est souvent là que se trouve sa vraie thèse — pas dans la phrase la plus solennelle.",
       mots:[['Ici, revient trois fois',"vingt-deux heures cinquante, onze personnes"],['Ce que ça révèle',"sa vraie question est la procédure, pas le boisé",true],['Comment le noter',"une barre à chaque retour, dans la marge"]],
       say:"Un projet qui passe de justesse à vingt-deux heures cinquante ne tiendra pas dix ans.",
       note:"C'est aussi ce qui vous donne un angle de réponse : reprenez ce qui revient, pas ce qui vous a agacé."},

      {t:'ana', h:"Les charnières qui annoncent la suite",
       p:"Un exposé bien construit vous prévient de ce qui arrive. Ces quelques formules valent tous les efforts de mémoire : elles vous disent où vous en êtes.",
       mots:[['Il commence',"« trois raisons », « je vous préviens tout de suite »"],['Il pivote',"« maintenant, la partie où je me contredis »",true],['Il conclut',"« alors voici où j'arrive », « ce que je souhaite, c'est »"]],
       say:"Maintenant, la partie où je me contredis. Alors voici où j'arrive.",
       note:"Quand vous entendez « trois raisons », écrivez tout de suite 1, 2, 3 dans la marge. Vous saurez ce qui vous manque."},

      {t:'ex', h:"Une grille d'écoute en cinq lignes",
       p:"À gauche l'écoute, à droite ce qu'on y note.",
       rows:[
         ["avant d'écouter","de qui il s'agit, et de quel média"],
         ["première écoute","la position, en une phrase"],
         ["deuxième écoute","trois ou quatre chiffres, avec leur unité"],
         ["troisième écoute","ce qui revient, et la concession"],
         ["après","une seule question à poser, écrite en entier"],
       ]},

      {t:'piege', h:"Trois pièges de l'écoute longue",
       rows:[
         ["tout noter","noter cinq choses",
          "Celui qui écrit tout n'écoute plus. Une page de notes pour douze minutes est un signe que l'écoute a échoué."],
         ["s'arrêter sur un mot inconnu","le laisser passer et continuer",
          "Un mot manqué coûte une phrase ; s'arrêter dessus coûte le reste de l'exposé. Notez-le au vol dans la marge et rattrapez le fil."],
         ["écouter pour répondre","écouter pour comprendre, puis répondre",
          "Dès qu'on prépare sa réplique, on cesse d'entendre. C'est ce qui fait qu'on répond à côté dans les tribunes — et ça s'entend."],
       ]},

      {t:'check', h:"Est-ce que c'est clair maintenant ?",
       p:"Trois questions rapides.",
       qs:[
         {q:"À la première écoute d'une chronique d'opinion, on cherche…", opts:["les chiffres","la position de l'auteur"], ok:1,
          fb:"Une fois la position tenue, tout le reste se range."},
         {q:"Ce qui est dit deux ou trois fois dans un texte préparé est…", opts:["un hasard","ce à quoi l'auteur tient"], ok:1,
          fb:"C'est souvent sa vraie thèse, plus que la phrase la plus solennelle."},
         {q:"Devant un mot inconnu au milieu d'un exposé, il faut…", opts:["s'arrêter dessus","le noter et continuer"], ok:1,
          fb:"S'arrêter coûte le reste de l'exposé."},
       ]},

      {t:'revoir', h:"À retenir",
       p:"Trois écoutes, trois consignes : <b>la position</b>, puis <b>les chiffres</b>, puis <b>ce qui revient</b>. Repérez les charnières (« trois raisons », « maintenant je me contredis », « ce que je souhaite ») : elles vous disent toujours où vous en êtes."},
    ]
  },

  t3irreel: {
    eye:'Mini-leçon', tit:"Ce qui aurait pu se passer autrement",
    blocs:[
      {t:'texte', h:"La forme du reproche civilisé",
       p:"« Si la Ville avait publié l'évaluation, personne n'aurait demandé de référendum. » Cette phrase reproche quelque chose à quelqu'un sans accuser personne : elle parle d'un monde qui n'a pas eu lieu. C'est l'outil le plus utile pour critiquer une décision en restant écoutable — et c'est exactement ce que le niveau 8 attend de vous.",
       note:"Elle sert aussi au regret et à la leçon : « si j'avais parlé à l'assemblée, j'aurais eu ma réponse »."},

      {t:'ana', h:"La forme, une fois pour toutes",
       p:"Deux moitiés, deux temps, et jamais l'inverse. Après « si », le plus-que-parfait. Dans l'autre moitié, le conditionnel passé.",
       mots:[['La condition',"Si la Ville avait publié l'évaluation,"],['La conséquence',"personne n'aurait demandé de référendum.",true],['Interdit',"jamais de conditionnel après « si »"]],
       say:"Si la Ville avait publié l'évaluation, personne n'aurait demandé de référendum.",
       note:"« Si j'aurais su » est la faute la plus connue du français. Elle se corrige en se rappelant que « si » et « -rais » ne se rencontrent jamais."},

      {t:'ana', h:"Les deux moitiés peuvent s'échanger",
       p:"L'ordre ne change pas le sens ; il change ce qu'on met en avant. Quand « si » passe en second, la virgule disparaît.",
       mots:[['Ordre 1',"Si le conseil avait attendu, le vote serait passé sans bruit."],['Ordre 2',"Le vote serait passé sans bruit si le conseil avait attendu.",true],["L'effet","le premier élément est celui qu'on souligne"]],
       say:"Si le conseil avait attendu, le vote serait passé sans bruit.",
       note:"À l'oral, commencez par « si » : votre interlocuteur sait tout de suite que vous parlez d'un monde qui n'a pas eu lieu."},

      {t:'ana', h:"Le mélange des temps — hier et aujourd'hui",
       p:"Quand ce qui s'est mal fait hier produit encore ses effets, on met le passé dans la condition et le présent dans la conséquence.",
       mots:[['On dit',"S'ils avaient mieux consulté, nous n'en serions pas là aujourd'hui."],['Le sens',"la cause est passée, l'effet dure",true],['Autre',"Si j'étais arrivée plus tôt, je pourrais vous répondre."]],
       say:"S'ils avaient mieux consulté, nous n'en serions pas là aujourd'hui.",
       note:"C'est la forme la plus fréquente dans un débat public, et celle qu'on entend le moins chez ceux qui apprennent la langue."},

      {t:'ana', h:"L'accord du participe au conditionnel passé",
       p:"Avec être, le participe s'accorde avec le sujet ; avec avoir, il ne s'accorde pas avec le sujet.",
       mots:[['Avec être',"Nous serions venus plus nombreux."],['Avec avoir',"Elle aurait posé la question.",true],['Piège',"Ils seraient partis · elles seraient restées"]],
       say:"Nous serions venus plus nombreux. Elle aurait posé la question.",
       note:"À l'oral, l'accord ne s'entend presque jamais. À l'écrit, dans une lettre au journal, il se voit."},

      {t:'labo', h:"Le monde qui n'a pas eu lieu",
       p:"Choisissez une cause et une conséquence.",
       axes:[
         {id:'c', lbl:'Quelle cause ?', opts:[['a',"si l'évaluation avait été publiée"],['b',"si le vote avait eu lieu à vingt heures"],['c',"si le terrain de l'aréna avait été étudié"]]},
         {id:'e', lbl:'Quelle conséquence ?', opts:[['1','dans le passé'],['2',"encore aujourd'hui"]]}],
       out:{
         a1:{w:["Si l'évaluation avait été publiée, le comité n'aurait pas ouvert de registre."], say:"Si l'évaluation avait été publiée, le comité n'aurait pas ouvert de registre.", n:"plus-que-parfait, puis conditionnel passé"},
         a2:{w:["Si l'évaluation avait été publiée, nous ne serions pas en train d'en débattre."], say:"Si l'évaluation avait été publiée, nous ne serions pas en train d'en débattre.", n:"la cause est passée, l'effet dure encore"},
         b1:{w:["Si le vote avait eu lieu à vingt heures, la salle aurait été pleine."], say:"Si le vote avait eu lieu à vingt heures, la salle aurait été pleine.", n:"conséquence entièrement passée"},
         b2:{w:["Si le vote avait eu lieu à vingt heures, personne ne contesterait la procédure."], say:"Si le vote avait eu lieu à vingt heures, personne ne contesterait la procédure.", n:"conditionnel présent : c'est encore vrai maintenant"},
         c1:{w:["Si le terrain de l'aréna avait été étudié, la Ville aurait eu une réponse à donner."], say:"Si le terrain de l'aréna avait été étudié, la Ville aurait eu une réponse à donner.", n:"conditionnel passé"},
         c2:{w:["Si le terrain de l'aréna avait été étudié, la discussion serait différente."], say:"Si le terrain de l'aréna avait été étudié, la discussion serait différente.", n:"l'effet se poursuit"},
       },
       note:"Répétez chaque phrase à voix haute : cette construction est longue, et elle ne devient naturelle qu'en la disant."},

      {t:'ex', h:"Six phrases utiles dans un débat",
       p:"À gauche la phrase, à droite ce qu'elle fait.",
       rows:[
         ["Si nous avions su, nous serions venus.","un regret, sans accuser personne"],
         ["Si la Ville avait publié l'évaluation, je n'aurais pas signé.","un reproche adressé à une institution"],
         ["Si j'avais eu ces documents, je n'aurais pas eu besoin d'appeler.","une critique qui reste polie"],
         ["Si le projet avait été présenté en juin, il serait déjà en chantier.","montrer que le retard vient d'ailleurs"],
         ["Si vous aviez posé la question, on vous aurait répondu.","renvoyer la responsabilité"],
         ["Si nous n'avions rien dit, rien n'aurait changé.","justifier son action"],
       ]},

      {t:'piege', h:"Trois pièges",
       rows:[
         ["« si j'aurais su »","« si j'avais su »",
          "Jamais de conditionnel après « si » quand il s'agit d'une hypothèse. C'est la faute la plus repérée du français, et elle se corrige une fois pour toutes."],
         ["« si » d'hypothèse et « si » de question indirecte","les distinguer",
          "« Je me demande si la Ville publiera » n'est pas une hypothèse : c'est une question rapportée, et le futur y est permis. La règle ne vaut que pour l'hypothèse."],
         ["employer cette forme trois fois de suite","une ou deux fois, aux bons endroits",
          "Un texte entièrement au conditionnel passé donne l'impression de quelqu'un qui refait le passé au lieu de demander quelque chose. Terminez toujours sur une demande au présent."],
       ]},

      {t:'check', h:"Est-ce que c'est clair maintenant ?",
       p:"Quatre questions rapides.",
       qs:[
         {q:"Après « si » d'hypothèse, on emploie…", opts:["le plus-que-parfait","le conditionnel passé"], ok:0,
          fb:"Le conditionnel va dans l'autre moitié de la phrase."},
         {q:"« Nous ___ venus plus nombreux » se complète par…", opts:["aurions","serions"], ok:1,
          fb:"Venir se conjugue avec être : nous serions venus."},
         {q:"« S'ils avaient consulté, nous n'en serions pas là » mélange…", opts:["deux passés","un passé et un présent"], ok:1,
          fb:"La cause est passée, l'effet dure encore aujourd'hui."},
         {q:"« Je me demande si la Ville publiera » est…", opts:["une hypothèse","une question indirecte"], ok:1,
          fb:"Le futur y est permis : ce n'est pas le « si » de l'hypothèse."},
       ]},

      {t:'revoir', h:"À retenir",
       p:"<b>Si + plus-que-parfait</b>, puis <b>conditionnel passé</b> — et jamais de conditionnel derrière « si ». Quand l'effet dure encore, la seconde moitié passe au conditionnel présent. C'est la façon de reprocher une décision sans accuser personne, et il en faut une, pas cinq."},
    ]
  },

  t3emph: {
    eye:'Mini-leçon', tit:"Mettre en avant ce qui compte",
    blocs:[
      {t:'texte', h:"À l'écrit on souligne, à l'oral on construit",
       p:"Quand tout est dit sur le même ton, rien ne ressort. Le français a des tournures faites pour souligner : elles déplacent un groupe de mots et le mettent en évidence. Dans un débat, elles font la différence entre quelqu'un qu'on suit et quelqu'un qu'on écoute poliment.",
       note:"Elles ne sont pas décoratives : elles disent à l'auditoire ce qu'il doit retenir de votre intervention."},

      {t:'ana', h:"C'est… qui · c'est… que",
       p:"On extrait le groupe à souligner et on l'encadre. « Qui » si le groupe extrait est le sujet du verbe ; « que » dans tous les autres cas.",
       mots:[['Sujet extrait',"C'est la procédure qui me dérange."],['Autre groupe',"C'est à vingt-deux heures cinquante qu'on a voté.",true],['Le test',"le mot juste après « c'est… » est-il le sujet ?"]],
       say:"C'est la procédure qui me dérange. C'est à vingt-deux heures cinquante qu'on a voté.",
       note:"Attention à l'accord du verbe : « c'est moi qui <b>ai</b> posé la question », jamais « qui a »."},

      {t:'ana', h:"Ce que… c'est · ce qui… c'est",
       p:"La forme la plus employée dans une intervention publique. Elle annonce qu'un point important arrive, et donne à l'auditoire une seconde pour s'y préparer.",
       mots:[['Complément',"Ce que je demande, c'est la publication de l'évaluation."],['Sujet',"Ce qui manque, c'est une étude du terrain de l'aréna.",true],['Le repère',"« ce que » pour un complément, « ce qui » pour un sujet"]],
       say:"Ce que je demande, c'est la publication de l'évaluation.",
       note:"C'est aussi la meilleure façon de commencer la dernière phrase d'une intervention : elle annonce la conclusion sans dire « en conclusion »."},

      {t:'ana', h:"Le détachement, avec reprise par un pronom",
       p:"On sort le groupe en tête ou en fin de phrase, et on le reprend par un pronom. C'est du français parlé correct, très courant au Québec, et parfaitement acceptable à une tribune.",
       mots:[['En tête',"Ce document-là, je le veux avant mardi."],['En fin',"Il a raison sur un point, le comité.",true],['La reprise',"le, la, les, en, y — accordés au groupe détaché"]],
       say:"Ce document-là, je le veux avant mardi. Il a raison sur un point, le comité.",
       note:"À l'écrit soutenu — votre lettre au journal —, employez plutôt « c'est… que » ou « quant à » : le détachement y paraît familier."},

      {t:'ana', h:"Quant à · pour ce qui est de",
       p:"Plus soutenu, et pratique pour changer de sujet sans perdre le fil. Il annonce : je passe à autre chose, et voici de quoi je parle maintenant.",
       mots:[['On écrit',"Quant à l'évaluation, elle n'a toujours pas été publiée."],['Variante',"Pour ce qui est du délai, il vient du promoteur.",true],['Le service rendu',"passer d'un point à l'autre proprement"]],
       say:"Quant à l'évaluation, elle n'a toujours pas été publiée.",
       note:"Excellent dans une lettre de trois paragraphes : un « quant à » au début du troisième, et la structure se voit toute seule."},

      {t:'ex', h:"La même idée, cinq mises en relief",
       p:"À gauche la tournure, à droite l'effet.",
       rows:[
         ["La procédure me dérange.","phrase neutre — rien ne ressort"],
         ["C'est la procédure qui me dérange.","on écarte tout le reste : ce n'est pas le projet"],
         ["Ce qui me dérange, c'est la procédure.","on annonce, puis on livre : l'auditoire attend"],
         ["La procédure, elle me dérange.","détachement parlé, très direct"],
         ["Quant à la procédure, elle me dérange.","registre soutenu, bon en tête de paragraphe"],
         ["Ce n'est pas le projet qui me dérange, c'est la procédure.","la forme la plus forte : on écarte et on désigne"],
       ]},

      {t:'piege', h:"Trois pièges",
       rows:[
         ["« c'est moi qui a »","« c'est moi qui ai »",
          "Le verbe s'accorde avec le mot repris par « qui ». C'est moi qui ai, c'est nous qui avons, c'est vous qui avez."],
         ["deux mises en relief dans la même phrase","une seule",
          "« Ce que je veux, c'est que ce soit l'évaluation qui soit publiée » est illisible. Une par phrase, trois au plus dans une intervention."],
         ["le détachement dans une lettre officielle","« c'est… que » ou « quant à »",
          "« Le comité, il a raison » se dit très bien à la radio et se lit mal dans un journal. Le registre change, les outils changent."],
       ]},

      {t:'check', h:"Est-ce que c'est clair maintenant ?",
       p:"Trois questions rapides.",
       qs:[
         {q:"« C'est la procédure ___ me dérange » se complète par…", opts:["qui","que"], ok:0,
          fb:"« La procédure » est sujet de « me dérange » : c'est « qui »."},
         {q:"Pour annoncer sa demande à la fin d'une intervention, la meilleure tournure est…", opts:["ce que je demande, c'est…","je demande…"], ok:0,
          fb:"Elle prévient l'auditoire qu'un point important arrive."},
         {q:"Dans une lettre au journal, on évite plutôt…", opts:["quant à…","le comité, il a raison"], ok:1,
          fb:"Le détachement parlé détonne dans un texte publié."},
       ]},

      {t:'revoir', h:"À retenir",
       p:"Quatre outils : <b>c'est… qui / que</b> pour écarter le reste · <b>ce que… c'est</b> pour annoncer un point important · le <b>détachement</b> à l'oral · <b>quant à</b> à l'écrit. Une seule mise en relief par phrase, et jamais plus de trois par intervention."},
    ]
  },

  t3rel: {
    eye:'Mini-leçon', tit:"Les relatives qui portent une préposition",
    blocs:[
      {t:'texte', h:"Pourquoi c'est un savoir de lecture avant d'être un savoir d'écriture",
       p:"Dans un texte d'opinion, l'essentiel voyage dans les relatives : ce qui suit « dont », « auquel » ou « pour lesquelles » est presque toujours l'argument. Le problème n'est pas de les écrire — c'est de savoir, en lisant, à quoi le pronom renvoie, parfois trois lignes plus haut. Une phrase de six lignes se comprend dès qu'on a trouvé ça.",
       note:"C'est aussi ce qui vous permettra d'écrire des phrases longues sans qu'elles s'écroulent."},

      {t:'ana', h:"La méthode, en deux temps",
       p:"Cherchez d'abord la préposition que demande le verbe de la relative, puis le genre et le nombre de ce qu'elle reprend. Le pronom s'en déduit.",
       mots:[['Le verbe et sa préposition',"s'opposer à quelque chose"],["Ce qu'on reprend","un projet — masculin singulier",true],['Le résultat',"le projet auquel je m'oppose"]],
       say:"Le projet auquel je m'oppose. L'assemblée à laquelle j'ai assisté.",
       note:"Toute la difficulté vient de la préposition, jamais du pronom. Trouvez la préposition, le reste suit."},

      {t:'ana', h:"Dont — le pronom de « de »",
       p:"Il remplace un groupe introduit par « de », quel que soit le genre et le nombre. C'est le plus fréquent et le plus utile.",
       mots:[['Verbe en « de »',"un dossier dont tout le monde parle"],['Complément du nom',"une décision dont les conséquences sont lourdes",true],['Interdit',"jamais « dont… son » : le comité dont le porte-parole"]],
       say:"Un dossier dont tout le monde parle. Une décision dont les conséquences sont lourdes.",
       note:"« Le comité dont son porte-parole est madame Sauvé » est fautif : « dont » contient déjà le possessif."},

      {t:'ana', h:"Auquel, à laquelle, auxquels, auxquelles",
       p:"Pour la préposition « à ». Ils s'accordent avec ce qu'ils reprennent, et « auquel » est la contraction de « à lequel ».",
       mots:[['Masculin',"le projet auquel je m'oppose"],['Féminin',"l'assemblée à laquelle j'ai assisté",true],['Pluriel',"les personnes auxquelles il s'adresse"]],
       say:"Le projet auquel je m'oppose. L'assemblée à laquelle j'ai assisté. Les personnes auxquelles il s'adresse.",
       note:"Pour des personnes, « à qui » est toujours possible et souvent plus léger : les personnes à qui il s'adresse."},

      {t:'ana', h:"Lequel après les autres prépositions",
       p:"Avec sur, sous, pour, par, avec, sans, dans, autour de : la forme complète, accordée en genre et en nombre.",
       mots:[['Masculin singulier',"le terrain sur lequel on veut bâtir"],['Féminin pluriel',"les raisons pour lesquelles j'ai signé",true],['Avec « de »',"la table autour de laquelle ils discutaient"]],
       say:"Le terrain sur lequel on veut bâtir. Les raisons pour lesquelles j'ai signé.",
       note:"« Les raisons pour lesquelles » est une des tournures les plus utiles à l'écrit argumentatif : apprenez-la telle quelle."},

      {t:'ana', h:"Où, pour le lieu et pour le temps",
       p:"Il remplace souvent « dans lequel » et « pendant lequel », et allège considérablement la phrase.",
       mots:[['Lieu',"la salle où se tiendra l'assemblée"],['Temps',"le soir où le vote a été pris",true],['Comparez',"le soir pendant lequel le vote a été pris"]],
       say:"La salle où se tiendra l'assemblée. Le soir où le vote a été pris.",
       note:"Quand « où » est possible, prenez-le : votre phrase sera plus courte et se lira mieux."},

      {t:'ex', h:"Sept verbes, sept relatives",
       p:"À gauche le verbe et sa préposition, à droite la relative.",
       rows:[
         ["s'opposer à","le projet auquel je m'oppose"],
         ["assister à","l'assemblée à laquelle j'ai assisté"],
         ["parler de","le dossier dont je parle"],
         ["avoir besoin de","les documents dont j'ai besoin"],
         ["bâtir sur","le terrain sur lequel on veut bâtir"],
         ["voter pour","le règlement pour lequel ils ont voté"],
         ["se souvenir de","la soirée dont je me souviens"],
       ]},

      {t:'piege', h:"Trois pièges",
       rows:[
         ["« dont » avec un possessif","« dont » seul",
          "Le comité <s>dont son</s> porte-parole → le comité <b>dont le</b> porte-parole. « Dont » contient déjà le « de », donc déjà la possession."],
         ["oublier l'accord de « lequel »","accorder avec ce qu'on reprend",
          "Les raisons pour <b>lesquelles</b>, les documents <b>auxquels</b>, la table autour de <b>laquelle</b>. C'est le seul pronom relatif qui s'accorde."],
         ["fabriquer une relative de six lignes","couper en deux phrases",
          "Le but n'est pas d'écrire long. Si vous perdez le fil en vous relisant, votre lecteur l'a perdu avant vous."],
       ]},

      {t:'check', h:"Est-ce que c'est clair maintenant ?",
       p:"Quatre questions rapides.",
       qs:[
         {q:"« C'est un projet ___ je m'oppose » se complète par…", opts:["dont","auquel"], ok:1,
          fb:"S'opposer <b>à</b> quelque chose : auquel."},
         {q:"« Les raisons ___ j'ai signé » se complète par…", opts:["pour lesquelles","dont"], ok:0,
          fb:"« Pour » demande « lesquelles », accordé au féminin pluriel."},
         {q:"« Le comité dont son porte-parole… » est…", opts:["correct","fautif"], ok:1,
          fb:"« Dont » contient déjà le possessif : le comité dont <b>le</b> porte-parole."},
         {q:"Quand « où » est possible, il vaut mieux…", opts:["l'employer","préférer « dans lequel »"], ok:0,
          fb:"Il allège la phrase sans rien lui enlever."},
       ]},

      {t:'revoir', h:"À retenir",
       p:"Trouvez d'abord <b>la préposition du verbe</b>, puis le genre et le nombre. <b>De</b> → dont · <b>à</b> → auquel, à laquelle, auxquelles (ou « à qui » pour des personnes) · les autres → sur lequel, pour lesquelles… · lieu et temps → <b>où</b>."},
    ]
  },

  t3repli: {
    eye:'Mini-leçon', tit:"Répondre quand on vous contredit",
    blocs:[
      {t:'texte', h:"Trois réponses possibles, et une seule à éviter",
       p:"Quelqu'un vient de vous contredire en public. Vous avez trois façons de répondre : <b>concéder</b>, <b>rectifier</b>, ou <b>esquiver</b>. Les deux premières vous font gagner du terrain ; la troisième s'entend toujours et coûte plus cher que l'aveu qu'elle voulait éviter. Le choix se fait en une seconde, et il se prépare avant.",
       note:"La règle est simple : rectifier ce qui est faux et vérifiable, concéder ce qui est juste, et ne jamais esquiver."},

      {t:'ana', h:"Concéder — le point exact, pas une politesse",
       p:"Vous reconnaissez précisément ce que l'autre a de juste, puis vous avancez. Cela vous coûte une phrase et vous achète l'attention de la salle.",
       mots:[['On dit',"Vous avez raison sur la rapidité du vote. Cela ne change rien au besoin de logements."],['Ce qui compte',"nommer le point, pas dire « je vous comprends »",true],["L'effet","l'auditoire vous écoute pour la suite"]],
       say:"Vous avez raison sur la rapidité du vote. Cela ne change rien au besoin de logements.",
       note:"Concéder puis se taire est une défaite. Concéder puis avancer est une technique : la seconde phrase est obligatoire."},

      {t:'ana', h:"Rectifier — seulement ce qui se vérifie",
       p:"Vous corrigez un fait faux, calmement, avec sa source. Ne rectifiez jamais une opinion : c'est impossible, et cela vous fait passer pour arrogant.",
       mots:[['On dit',"Le procès-verbal indique quatre voix contre trois, et non l'unanimité."],['On ajoute',"la source, en trois mots",true],['On ne dit pas',"« c'est faux » tout court"]],
       say:"Le procès-verbal indique quatre voix contre trois, et non l'unanimité.",
       note:"Une rectification sans source est une contradiction de plus. Une rectification avec source ferme la question."},

      {t:'ana', h:"Esquiver — ce que ça produit vraiment",
       p:"Changer de sujet, répondre à une autre question, ou attaquer la personne. Cela s'entend, même à la radio, et surtout à la radio.",
       mots:[['On entend',"Et vous, où étiez-vous quand on a fermé l'usine ?"],['Ce que la salle comprend',"il n'a pas de réponse",true],['Le prix',"tout ce que vous direz ensuite sera écouté autrement"]],
       say:"Et vous, où étiez-vous quand on a fermé l'usine ?",
       note:"Il vaut toujours mieux dire « je ne sais pas, je vais vérifier ». C'est une phrase que personne ne peut vous reprocher."},

      {t:'ana', h:"La rumeur qu'on vous tend",
       p:"Un cas particulier, et fréquent. On vous propose une insinuation pour que vous la repreniez. Y répondre, même pour la nuancer, c'est la faire exister.",
       mots:[['On vous tend',"On dit que le promoteur serait un ami du maire."],['La mauvaise réponse',"« ça, je ne peux pas le confirmer »",true],['La bonne',"« Je n'en sais rien, et ce n'est pas mon argument. »"]],
       say:"Je n'en sais rien, et ce n'est pas mon argument.",
       note:"Vous refusez la rumeur et vous ramenez la discussion sur votre terrain, en une phrase. C'est aussi ce qui vous rendra crédible auprès de ceux qui hésitent."},

      {t:'ex', h:"Six répliques et ce qu'elles font",
       p:"À gauche la réplique, à droite le geste.",
       rows:[
         ["« Vous avez raison sur ce point-là. »","concéder — et il faut poursuivre"],
         ["« Le délai de vingt et un mois est une estimation, pas une loi. »","rectifier avec la nature de la source"],
         ["« Ce n'est pas la question que je pose. »","esquiver, en ayant l'air de recadrer"],
         ["« Je ne le sais pas, je vais vérifier. »","dire son ignorance — imbattable"],
         ["« Tout le monde sait très bien pourquoi. »","esquiver et insinuer — le pire des deux"],
         ["« C'est vrai, et cela ne règle pas le problème du calendrier. »","concéder et avancer dans la même phrase"],
       ]},

      {t:'piege', h:"Trois pièges quand on vous coupe la parole",
       rows:[
         ["élever la voix","ralentir",
          "Celui qui monte le ton perd, à la radio comme en assemblée. Ralentir oblige l'autre à ralentir aussi, et cela s'entend comme de l'assurance."],
         ["répondre à tout","choisir un point",
          "Trois objections vous sont lancées ; répondez à la plus forte, et dites-le : « je réponds sur le calendrier, qui est le vrai point »."],
         ["terminer sur ce qu'on dénonce","terminer sur ce qu'on demande",
          "La dernière phrase est la seule que beaucoup retiendront. Elle doit contenir votre demande, pas votre colère."],
       ]},

      {t:'check', h:"Est-ce que c'est clair maintenant ?",
       p:"Quatre questions rapides.",
       qs:[
         {q:"On ne rectifie que…", opts:["ce qui est vérifiable","ce qui nous déplaît"], ok:0,
          fb:"Rectifier une opinion est impossible et vous dessert."},
         {q:"Après une concession, il faut…", opts:["se taire","avancer son point"], ok:1,
          fb:"Concéder puis se taire est une défaite ; la seconde phrase est obligatoire."},
         {q:"Devant une rumeur qu'on vous tend, la bonne réponse est…", opts:["« je ne peux pas le confirmer »","« je n'en sais rien, et ce n'est pas mon argument »"], ok:1,
          fb:"La première laisse la rumeur exister ; la seconde la refuse et ramène le sujet."},
         {q:"La dernière phrase d'une intervention doit contenir…", opts:["votre demande","ce que vous dénoncez"], ok:0,
          fb:"C'est souvent la seule que l'auditoire retiendra."},
       ]},

      {t:'revoir', h:"À retenir",
       p:"<b>Concéder</b> le point exact, puis avancer · <b>rectifier</b> ce qui est faux, avec sa source · ne jamais <b>esquiver</b>, et dire « je ne sais pas » plutôt. Devant une rumeur : « je n'en sais rien, et ce n'est pas mon argument. » Terminez sur ce que vous demandez."},
    ]
  },

  t3lettre: {
    eye:'Mini-leçon', tit:"Écrire au courrier des lecteurs",
    blocs:[
      {t:'texte', h:"Deux intentions du programme dans un seul texte",
       p:"Le niveau 8 demande deux choses en production écrite pour cette situation : <b>rédiger une lettre au courrier des lecteurs</b> et <b>résumer un texte d'opinion</b>. Elles se font ensemble, et c'est même la seule façon de les faire correctement : votre lettre commence par résumer, en trois phrases honnêtes, le texte auquel elle répond. Sans ce résumé, personne ne sait de quoi vous parlez ; s'il est malhonnête, personne ne vous croit pour la suite.",
       note:"C'est aussi ce qui distingue une lettre publiable d'un commentaire de réseau social : elle prend au sérieux ce qu'elle conteste."},

      {t:'ana', h:"Le rattachement — première phrase, toujours",
       p:"Un journal publie ce qui se rattache à quelque chose de paru chez lui. Nommez le texte, sa date et son auteur avant toute chose.",
       mots:[['On écrit',"En réaction à l'éditorial « Un terrain qui ne rapportait rien », paru le 14 octobre."],['Sans ça',"la lettre n'a aucune prise et n'est pas retenue",true],['À noter',"le titre entre guillemets, la date en toutes lettres"]],
       say:"En réaction à l'éditorial paru dans votre édition du 14 octobre.",
       note:"Une lettre qui commence par « je suis outrée » et ne dit pas par quoi finit à la corbeille."},

      {t:'ana', h:"Le résumé — trois phrases, sans caricature",
       p:"Redites la thèse de l'autre et ses deux meilleurs arguments, dans ses termes à lui. C'est un exercice d'honnêteté et il se voit tout de suite.",
       mots:[['La règle',"résumez ce qu'il dit de plus fort, pas de plus faible"],['La longueur',"trois phrases, pas plus",true],['Le test',"l'auteur signerait-il votre résumé ?"]],
       say:"Votre éditorialiste soutient que la cession était nécessaire et urgente.",
       note:"Résumer en affaiblissant s'appelle un homme de paille : on démolit une version faible de l'adversaire. Le lecteur informé le repère, et votre lettre est perdue."},

      {t:'ana', h:"La position, puis les arguments",
       p:"Une phrase pour dire où vous vous situez — y compris si votre position est inattendue —, puis deux arguments, dont un tiré de votre expérience directe.",
       mots:[['La position',"Je partage sa conclusion et je signerai malgré tout le registre."],["L'argument vécu","Trois de mes collègues ont quitté la ville faute de logement.",true],["L'argument de fond","Une décision prise devant onze personnes ne tiendra pas."]],
       say:"Je partage sa conclusion et je signerai malgré tout le registre.",
       note:"Une position inattendue est ce qui fait publier une lettre : les rédactions reçoivent cent textes prévisibles pour un qui surprend."},

      {t:'ana', h:"La concession et la demande",
       p:"Reconnaissez ce que votre position coûte, puis terminez par ce que vous demandez — à quelqu'un qui peut le faire, et avec une date.",
       mots:[['La concession',"Il est vrai qu'un report mettrait le financement en péril."],['La demande',"Je demande à la Ville de publier l'évaluation avant l'ouverture du registre.",true],['Jamais',"finir par une question rhétorique ou une indignation"]],
       say:"Je demande à la Ville de publier l'évaluation avant l'ouverture du registre.",
       note:"Deux demandes au maximum. Trois, et aucune ne sera retenue."},

      {t:'ex', h:"Le plan en six lignes",
       p:"À gauche la partie, à droite ce qu'elle contient.",
       rows:[
         ["le rattachement","le titre du texte, sa date, son auteur"],
         ["le résumé","la thèse adverse et ses deux meilleurs arguments, en trois phrases"],
         ["la position","une phrase, la vôtre, même si elle surprend"],
         ["les arguments","deux, dont un vécu et un chiffré"],
         ["la concession et la réfutation","ce que votre position coûte, et pourquoi elle tient quand même"],
         ["la demande et la signature","deux demandes au plus, avec une date · nom et ville"],
       ]},

      {t:'piege', h:"Quatre pièges qui font écarter une lettre",
       rows:[
         ["s'adresser à une personne","s'adresser à la rédaction, sur une question publique",
          "« Monsieur Chamberland devrait avoir honte » ne se publie pas. « L'argument de M. Chamberland résiste mal sur un point » se publie."],
         ["dépasser trois cent cinquante mots","tenir en une page",
          "La rédaction coupe elle-même, et elle coupe la fin — c'est-à-dire votre demande."],
         ["mêler faits, opinions et rumeurs","les séparer explicitement",
          "Ce que je sais, ce qu'on m'a dit, ce que j'en pense : trois registres, trois façons de les annoncer. Les mêler vous rend attaquable en une ligne."],
         ["écrire sous le coup de la colère","écrire, puis attendre une nuit",
          "La lettre qu'on envoie le lendemain matin est presque toujours la meilleure, et c'est celle qu'on est content d'avoir signée dix ans plus tard."],
       ]},

      {t:'check', h:"Est-ce que c'est clair maintenant ?",
       p:"Quatre questions rapides.",
       qs:[
         {q:"La première phrase d'une lettre au courrier des lecteurs doit…", opts:["donner votre opinion","rattacher la lettre à un texte daté"], ok:1,
          fb:"Sans ce rattachement, la lettre n'a aucune prise et n'est pas retenue."},
         {q:"Le résumé du texte adverse doit reprendre…", opts:["ses arguments les plus faibles","ses arguments les plus forts"], ok:1,
          fb:"Résumer en affaiblissant se repère, et coûte toute la crédibilité de la suite."},
         {q:"Une lettre se termine par…", opts:["une demande précise","une question rhétorique"], ok:0,
          fb:"Adressée à quelqu'un qui peut agir, et si possible avec une date."},
         {q:"La bonne longueur est d'environ…", opts:["250 à 350 mots","600 mots"], ok:0,
          fb:"Au-delà, la rédaction coupe la fin, c'est-à-dire votre demande."},
       ]},

      {t:'revoir', h:"À retenir",
       p:"Six parties : <b>rattachement</b> daté · <b>résumé</b> honnête en trois phrases · <b>position</b> en une phrase · <b>deux arguments</b>, dont un vécu · <b>concession</b> et réfutation · <b>demande</b> précise et signature. Deux cent cinquante à trois cent cinquante mots, et une nuit avant d'envoyer."},
    ]
  },

};
