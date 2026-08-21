const PLUS = {

  // ════════════════════════════════════════════════════════════════════════
  prPhon: {
    eye:'Mini-leçon', tit:"« En » et « on » : deux sons qui passent par le nez",
    blocs:[
      {t:'texte', h:"Pourquoi celles-là, et pourquoi maintenant",
       p:"Le français a trois voyelles nasales courantes, et deux d'entre elles se ressemblent assez pour se confondre au téléphone : celle de <b>ambulance</b> et celle de <b>nom</b>. L'air passe par le nez dans les deux cas. Ce qui change, c'est la bouche : grande ouverte pour la première, arrondie pour la seconde.",
       note:"Dans un appel d'urgence, il y a du bruit, de la peur et une seule ligne téléphonique. Le répartiteur n'a que votre voix. « Elle est tombée » et « elle est tendue » ne demandent pas la même équipe."},

      {t:'ana', h:"[ɑ̃] — le son de « ambulance », « attente », « chambre »",
       p:"Il s'écrit <b>an</b>, <b>am</b>, <b>en</b> ou <b>em</b> — quatre graphies, un seul son.",
       mots:[['La recette','ouvrez la bouche comme pour « ah », puis laissez l\'air passer par le nez'],['On écrit','an · am · en · em',true],['Dans ce module','une ambulance · l\'attente · la chambre · quarante']],
       say:"L'ambulance est arrivée quarante minutes avant la fin de l'attente.",
       note:"Le <b>m</b> apparaît devant <b>b</b> et <b>p</b> : cha<b>m</b>bre, a<b>m</b>bulance, te<b>m</b>ps. C'est une règle d'écriture, pas de prononciation."},

      {t:'ana', h:"[ɔ̃] — le son de « nom », « tombée », « salon »",
       p:"Il s'écrit <b>on</b> ou <b>om</b>. Les lèvres s'arrondissent comme pour dire « o ».",
       mots:[['La recette','arrondissez les lèvres, l\'air passe par le nez'],['On écrit','on · om',true],['Dans ce module','le nom · elle est tombée · on répond · le salon']],
       say:"On répond au téléphone dans le salon : elle est tombée.",
       note:"Mettez la main devant la bouche : pour [ɔ̃], vous sentez très peu d'air sortir. S'il en sort beaucoup, vous dites « o » et non « on »."},

      {t:'ana', h:"Les deux dans le même mot",
       p:"Beaucoup de mots de la santé contiennent les deux sons, l'un après l'autre. C'est le meilleur exercice possible.",
       mots:[['D\'abord la bouche ouverte','la t-en-sion'],['Puis les lèvres rondes','la tensi-on',true],['À dire d\'un trait','la tension · une infection · une intervention']],
       say:"La tension est bonne, mais il y a une infection.",
       note:"Dites-les au ralenti, deux fois, en exagérant la forme de la bouche. Puis à vitesse normale. La bouche apprend un mouvement, pas une règle."},

      {t:'labo', h:"Écoutez les paires, une à la fois",
       p:"Chaque paire ne diffère que par une voyelle. Choisissez-en une et écoutez-la dans sa phrase.",
       axes:[{id:'p', lbl:'Quelle paire ?', opts:[
         ['a','sans / son'],
         ['b','banc / bon'],
         ['c','temps / ton'],
         ['d','lent / long'],
         ['e','les deux sons dans la même phrase']]}],
       out:{
         a:{w:['sans / son'], say:"Elle est arrivée sans son sac et sans sa carte.", n:"« sans » ouvre la bouche, « son » l'arrondit"},
         b:{w:['banc / bon'], say:"Le banc de la salle d'attente n'est pas bon pour son dos.", n:"deux mots, deux sens : rien de commun"},
         c:{w:['temps / ton'], say:"Prends ton temps pour répondre au répartiteur.", n:"on les entend souvent l'un à côté de l'autre"},
         d:{w:['lent / long'], say:"Le triage est lent et le corridor est long.", n:"la plainte la plus fréquente d'une salle d'attente"},
         e:{w:['ambulance / on'], say:"On attend l'ambulance depuis onze minutes.", n:"la phrase à répéter dix fois"},
       },
       note:"Écoutez chaque phrase deux fois : la première pour comprendre, la seconde en ne guettant que les voyelles nasales."},

      {t:'ex', h:"À écouter et à répéter",
       p:"Six phrases prises dans les appels de ce module.",
       rows:[
         ["Une ambulance s'en vient, restez près d'elle.","[ɑ̃] trois fois"],
         ["On ne la déplace pas et on ne lui donne rien.","[ɔ̃] partout"],
         ["Elle est tombée dans l'escalier vers deux heures.","[ɔ̃] au début"],
         ["L'attente peut être longue, gardez votre téléphone chargé.","[ɑ̃] puis [ɔ̃]"],
         ["La tension est bonne, la température descend.","les deux, en alternance"],
         ["Comment s'appelle la personne, et quel âge a-t-elle ?","[ɔ̃] dans « comment » ? non : écoutez bien"],
       ]},

      {t:'piege', h:"Trois pièges des voyelles nasales",
       rows:[
         ["prononcer le n ou le m",'« ambulance » dit « am-bou-lan-ce » avec un m entendu',
          "Dans une voyelle nasale, la consonne ne se prononce pas : elle indique seulement que l'air passe par le nez. On ne dit ni « an-ne » ni « on-ne »."],
         ["dénasaliser devant une voyelle",'« une ambulance » dit « une a-mbulance »',
          "Quand la syllabe suivante commence par une voyelle ou par une double consonne, le son redevient oral : bo<b>nne</b>, a<b>nnée</b>, i<b>mm</b>édiat. Comparez : bo<b>n</b> / bo<b>nne</b>."],
         ["confondre avec [ɛ̃]",'« quinze » dit comme « quand »',
          "Il existe une troisième nasale, celle de « quinze », « un », « médecin », « bien ». Elle s'écrit in, ain, ein, en après i. Les lèvres sont étirées, pas arrondies."],
       ]},

      {t:'check', h:"Est-ce que c'est clair maintenant ?",
       p:"Quatre questions rapides.",
       qs:[
         {q:"Pour faire le son de « ambulance », la bouche est…", opts:["grande ouverte","arrondie"], ok:0,
          fb:"Grande ouverte, comme pour « ah », avec l'air qui passe par le nez."},
         {q:"« nom », « tombée », « salon » ont…", opts:["le son [ɑ̃]","le son [ɔ̃]"], ok:1,
          fb:"Ils s'écrivent tous avec on ou om : c'est le son de « nom »."},
         {q:"Dans « bonne », le son est…", opts:["nasal","oral"], ok:1,
          fb:"La double consonne coupe la nasale : bon est nasal, bonne ne l'est pas."},
         {q:"Le mot « tension » contient…", opts:["une seule nasale","les deux nasales"], ok:1,
          fb:"ten- est ouvert, -sion est arrondi. Le mot les enchaîne."},
       ]},
    ]
  },

  // ════════════════════════════════════════════════════════════════════════
  prNum: {
    eye:'Mini-leçon', tit:"8-1-1 ou 9-1-1 : la décision de dix secondes",
    blocs:[
      {t:'texte', h:"Une seule question, et elle est simple",
       p:"Devant quelqu'un qui ne va pas bien, on hésite rarement entre dix possibilités. On hésite entre <b>appeler tout de suite</b> et <b>attendre demain matin</b>. Toute la décision tient dans une question : <b>est-ce que ça peut attendre dix minutes ?</b> Si oui, le 8-1-1 vous dira quoi faire. Si non, c'est le 9-1-1, et ça ne se discute pas.",
       note:"Dans le doute entre les deux, composez le 9-1-1. Personne ne vous reprochera d'avoir appelé ; le service existe pour les gens qui ne sont pas médecins."},

      {t:'ana', h:"Le 8-1-1 — une infirmière, jour et nuit, gratuitement",
       p:"Info-Santé répond vingt-quatre heures sur vingt-quatre, toute l'année, partout au Québec.",
       mots:[['Qui répond','une infirmière, pas un médecin'],['Ce qu\'elle fait','elle évalue, elle conseille, elle oriente',true],['Ce qu\'elle ne fait pas','elle ne prescrit rien et ne pose pas de diagnostic']],
       say:"Info-Santé, bonsoir. J'appelle pour ma mère : elle fait de la fièvre depuis mercredi.",
       note:"Vous pouvez appeler pour vous-même ou pour quelqu'un d'autre. Ayez la personne près de vous : l'infirmière posera des questions auxquelles vous ne pouvez pas répondre de mémoire."},

      {t:'ana', h:"Le 9-1-1 — pour ce qui ne peut pas attendre",
       p:"Cinq signes ne se racontent jamais au 8-1-1 : on raccroche et on compose le 9-1-1.",
       mots:[['Un','une douleur à la poitrine'],['Deux et trois','une difficulté à respirer · une perte de connaissance',true],['Quatre et cinq','un saignement qu\'on n\'arrête pas · une chute d\'où la personne ne se relève pas']],
       say:"Ma mère est tombée dans l'escalier et elle ne peut pas se relever.",
       note:"Ajoutez-en un sixième, moins connu : une personne qui devient soudainement confuse, qui ne trouve plus ses mots ou dont le visage tombe d'un côté. Là, chaque minute compte."},

      {t:'ana', h:"L'ambulance et son coût",
       p:"Le transport ambulancier n'est pas gratuit au Québec, et beaucoup de gens hésitent pour cette raison. Ils ont tort.",
       mots:[['Le tarif de base','environ 125 $, plus 1,75 $ le kilomètre'],['65 ans et plus','payé, si le médecin de l\'hôpital confirme après coup que le transport était nécessaire',true],['Ce que ça ne doit jamais faire','vous faire hésiter devant l\'un des cinq signes']],
       say:"Le transport en ambulance coûte environ cent vingt-cinq dollars, plus le kilométrage.",
       note:"Amener soi-même en voiture quelqu'un qui a une douleur à la poitrine est une mauvaise économie : les ambulanciers commencent les soins dans le salon, et l'hôpital sait qu'ils arrivent."},

      {t:'labo', h:"La même hésitation, cinq soirs différents",
       p:"Choisissez une situation et voyez ce qu'il faut composer.",
       axes:[{id:'s', lbl:'Quelle situation ?', opts:[
         ['a','une fièvre qui dure depuis deux jours'],
         ['b','une chute d\'où la personne ne se relève pas'],
         ['c','un comprimé pris deux fois'],
         ['d','une douleur à la poitrine depuis dix minutes'],
         ['e','une plaie rouge depuis trois jours']]}],
       out:{
         a:{w:['8-1-1'], say:"Elle fait de la fièvre depuis deux jours et elle mange très peu.", n:"ça dure, mais ça n'empire pas d'une minute à l'autre"},
         b:{w:['9-1-1'], say:"Elle est tombée et elle ne peut pas se relever.", n:"un des cinq signes : on ne raconte pas, on compose"},
         c:{w:['8-1-1'], say:"J'ai pris mon comprimé deux fois ce matin, est-ce que c'est grave ?", n:"l'infirmière a les tableaux de doses devant elle"},
         d:{w:['9-1-1'], say:"Mon conjoint a une forte douleur à la poitrine depuis dix minutes.", n:"jamais la voiture, jamais l'attente"},
         e:{w:['8-1-1'], say:"Ma plaie au doigt est rouge depuis trois jours et j'hésite à consulter.", n:"exactement le genre d'appel pour lequel la ligne existe"},
       },
       note:"Remarquez la différence de longueur : au 8-1-1 on décrit, au 9-1-1 on annonce. Deux phrases contre une."},

      {t:'ex', h:"À écouter et à répéter",
       p:"Six phrases pour les premières secondes d'un appel.",
       rows:[
         ["J'appelle pour ma mère, elle a soixante et onze ans.","dire pour qui, et l'âge"],
         ["Elle fait de la fièvre depuis mercredi.","le fait, et depuis quand"],
         ["Elle respire bien, mais elle ne mange plus.","ce qui va, et ce qui ne va pas"],
         ["Est-ce que ça peut attendre demain matin ?","la question à poser"],
         ["Qu'est-ce qui doit me faire appeler le 9-1-1 cette nuit ?","la question qu'on oublie"],
         ["Perdre connaissance, respirer mal, devenir confuse, tomber.","répéter la liste avant de raccrocher"],
       ]},

      {t:'piege', h:"Trois erreurs qui coûtent cher",
       rows:[
         ["hésiter à cause du coût de l'ambulance","« on va y aller en auto, ça coûte moins cher »",
          "Devant l'un des cinq signes, l'ambulance n'est pas un transport : c'est le début des soins. Le coût se discute après, avec l'établissement."],
         ["raconter toute l'histoire au 9-1-1","« alors depuis mercredi elle avait de la fièvre, et hier… »",
          "Le 9-1-1 veut l'endroit, puis une phrase. Le récit complet, vous le ferez au triage, à quelqu'un dont c'est le travail de l'écouter."],
         ["ne pas répéter la liste des signes","« oui oui, d'accord, merci, bonne soirée »",
          "La liste que l'infirmière vous donne sert la nuit suivante, quand vous serez fatigué et inquiet. Répétez-la à voix haute avant de raccrocher, et notez-la."],
       ]},

      {t:'check', h:"Est-ce que c'est clair maintenant ?",
       p:"Quatre questions rapides.",
       qs:[
         {q:"Au bout du fil, au 8-1-1, il y a…", opts:["une infirmière","un médecin"], ok:0,
          fb:"Une infirmière. Elle évalue et oriente ; elle ne prescrit pas."},
         {q:"Une personne tombée qui ne peut plus se relever :", opts:["8-1-1","9-1-1"], ok:1,
          fb:"C'est l'un des cinq signes : 9-1-1."},
         {q:"Le transport en ambulance est…", opts:["toujours gratuit","facturé, avec des exceptions"], ok:1,
          fb:"Environ 125 $ plus le kilométrage ; payé pour les 65 ans et plus si le médecin confirme qu'il était nécessaire."},
         {q:"Dans le doute entre les deux numéros :", opts:["9-1-1","on attend demain"], ok:0,
          fb:"On compose le 9-1-1. C'est la règle, et elle est faite pour vous."},
       ]},
    ]
  },

  // ════════════════════════════════════════════════════════════════════════
  t1ordre: {
    eye:'Mini-leçon', tit:"Les questions du 9-1-1, dans l'ordre où elles viennent",
    blocs:[
      {t:'texte', h:"Ce n'est pas une conversation",
       p:"Un appel au 9-1-1 suit un protocole. Le répartiteur lit des questions à l'écran, dans un ordre décidé d'avance, et il tape vos réponses pendant que d'autres personnes préparent déjà le départ. Votre travail n'est pas de bien raconter : c'est de <b>répondre court et dans l'ordre</b>.",
       note:"Savoir d'avance quelles questions viennent enlève la moitié de la panique. Elles sont toujours les mêmes, quel que soit l'appel."},

      {t:'ana', h:"1 — Où ? La question qui passe avant tout",
       p:"Tant que l'adresse n'est pas prise, personne ne part. Si la ligne se coupe, l'adresse est la seule chose qui permette d'envoyer quelqu'un.",
       mots:[['Le numéro et la rue','5412, rue des Ormeaux'],['La ville et l\'appartement','à Saint-Léonard, appartement 2',true],['Le détail qui fait gagner une minute','en bas de l\'escalier intérieur']],
       say:"Cinq mille quatre cent douze, rue des Ormeaux, à Saint-Léonard, appartement deux.",
       note:"Le répartiteur répétera l'adresse. Écoutez-la et corrigez tout de suite si un chiffre est faux : c'est le seul moment où l'erreur se rattrape facilement."},

      {t:'ana', h:"2 — Le numéro de téléphone, puis « que se passe-t-il ? »",
       p:"Le numéro sert à vous rappeler si la communication tombe. Ensuite seulement vient l'évènement, en une phrase.",
       mots:[['Chiffre par chiffre','cinq un quatre, cinq cinq cinq, zéro un neuf huit'],['Une seule phrase','ma mère est tombée dans l\'escalier',true],['Pas encore','l\'histoire des deux derniers jours']],
       say:"Ma mère est tombée dans l'escalier et elle ne peut pas se relever.",
       note:"Un bon repère : sujet, verbe, où. « Ma mère est tombée dans l'escalier. » Tout le reste viendra par questions."},

      {t:'ana', h:"3 — Consciente ? Respire-t-elle ?",
       p:"Ces deux questions décident du type d'équipe et de la vitesse. Répondez oui ou non, puis une précision utile.",
       mots:[['Consciente','oui, elle me répond'],['Respiration','oui, elle respire, elle pleure mais elle respire',true],['Si vous ne savez pas','dites-le : « je ne sais pas, je ne l\'ai pas vue tomber »']],
       say:"Oui, elle me répond. Elle respire, elle pleure mais elle respire.",
       note:"« Je ne sais pas » est une bonne réponse. Une invention, non : elle peut envoyer la mauvaise équipe."},

      {t:'labo', h:"Les mêmes questions, quatre urgences différentes",
       p:"Choisissez une urgence et écoutez la réponse type à la question « dites-moi ce qui se passe ».",
       axes:[{id:'u', lbl:'Quelle urgence ?', opts:[
         ['a','une chute dans un escalier'],
         ['b','une douleur à la poitrine'],
         ['c','une personne inconsciente dans la rue'],
         ['d','un saignement qui ne s\'arrête pas'],
         ['e','une difficulté à respirer']]}],
       out:{
         a:{w:['une chute'], say:"Ma mère est tombée dans l'escalier et elle ne peut pas se relever.", n:"qui, quoi, où — trois éléments"},
         b:{w:['une douleur'], say:"Mon conjoint a une forte douleur à la poitrine depuis dix minutes.", n:"la durée compte, ici : dites-la"},
         c:{w:['inconsciente'], say:"Un homme est par terre devant le dépanneur et il ne répond pas.", n:"dehors, on donne un point que tout le monde voit"},
         d:{w:['un saignement'], say:"Mon collègue s'est coupé au bras et le saignement ne s'arrête pas.", n:"dites où saigne la personne"},
         e:{w:['respirer'], say:"Ma fille a beaucoup de difficulté à respirer depuis cinq minutes.", n:"l'âge sera demandé aussitôt : préparez-le"},
       },
       note:"Cinq urgences, une seule forme de phrase. C'est cette forme-là qu'il faut avoir en tête, pas les mots exacts."},

      {t:'ex', h:"À écouter et à répéter",
       p:"Six réponses courtes, dans l'ordre de l'appel.",
       rows:[
         ["5412, rue des Ormeaux, appartement 2, à Saint-Léonard.","l'endroit"],
         ["Le 514 555-0198.","le numéro d'où vous appelez"],
         ["Ma mère est tombée dans l'escalier.","une phrase"],
         ["Oui, elle me répond.","consciente"],
         ["Oui, elle respire normalement.","respiration"],
         ["Soixante et onze ans, et elle prend des médicaments pour la tension.","l'âge et les médicaments"],
       ]},

      {t:'piege', h:"Trois pièges de l'appel",
       rows:[
         ["commencer par le récit","« bonjour, alors voilà, depuis mercredi ma mère… »",
          "Le répartiteur vous coupera pour demander l'adresse. Donnez-la en premier, sans qu'on vous la demande, et vous aurez gagné vingt secondes."],
         ["raccrocher trop tôt","« bon, ils s'en viennent, merci, au revoir »",
          "Le répartiteur reste avec vous et donne des consignes jusqu'à l'arrivée. C'est lui qui dit quand raccrocher."],
         ["répondre longuement","« est-ce qu'elle est consciente ? — ah, vous savez, elle est fatiguée depuis… »",
          "Oui ou non, puis une précision de quatre mots. Le reste sera demandé si c'est utile."],
       ]},

      {t:'check', h:"Est-ce que c'est clair maintenant ?",
       p:"Trois questions rapides.",
       qs:[
         {q:"La première question du répartiteur porte sur…", opts:["l'endroit","ce qui s'est passé"], ok:0,
          fb:"L'endroit. Tant qu'il n'est pas pris, personne ne part."},
         {q:"Vous ignorez si la personne s'est frappé la tête. Vous dites…", opts:["« je ne sais pas »","« non, sûrement pas »"], ok:0,
          fb:"« Je ne sais pas » est une bonne réponse. Une invention peut envoyer la mauvaise équipe."},
         {q:"Quand raccroche-t-on ?", opts:["dès que l'ambulance part","quand le répartiteur le dit"], ok:1,
          fb:"Il reste en ligne avec vous et vous guide jusqu'à l'arrivée."},
       ]},
    ]
  },

  // ════════════════════════════════════════════════════════════════════════
  t1imp: {
    eye:'Mini-leçon', tit:"L'impératif présent — le mode de l'urgence",
    blocs:[
      {t:'texte', h:"Trois formes, aucun sujet",
       p:"L'impératif sert à donner un ordre, un conseil ou une consigne. Il n'a que trois personnes — <b>tu</b>, <b>nous</b>, <b>vous</b> — et le sujet ne s'écrit pas. C'est le mode qu'emploie un répartiteur, une infirmière, un ambulancier : il est court, il s'exécute, et il ne demande pas de réponse.",
       note:"Ce n'est pas de l'impolitesse. Dans une urgence, une phrase polie complète coûte trois secondes de plus, et personne n'en a."},

      {t:'ana', h:"La forme affirmative",
       p:"On prend le présent de l'indicatif et on enlève le sujet.",
       mots:[['tu restes','Reste près d\'elle.'],['nous restons','Restons calmes.',true],['vous restez','Restez en ligne avec moi.']],
       say:"Restez près d'elle et parlez-lui doucement.",
       note:"Les verbes en -er perdent leur <b>s</b> à la deuxième personne : tu regard<b>es</b> → « Regarde ! ». Les autres le gardent : tu pren<b>ds</b> → « Prends le sac. »"},

      {t:'ana', h:"La forme négative",
       p:"Le <b>ne… pas</b> entoure le verbe, exactement comme dans une phrase ordinaire.",
       mots:[['ne… pas','Ne la déplacez pas.'],['ne… rien','Ne lui donnez rien à boire.',true],['ne… jamais','Ne raccrochez jamais avant qu\'on vous le dise.']],
       say:"Ne la déplacez pas, ne la faites pas asseoir, ne lui donnez rien à boire.",
       note:"Dans une urgence, les ordres négatifs sont les plus importants : ce qu'il ne faut surtout pas faire est souvent plus décisif que ce qu'il faut faire."},

      {t:'ana', h:"Quatre irréguliers à connaître par cœur",
       p:"Ils reviennent tout le temps dans les consignes de santé.",
       mots:[['être','sois · soyons · soyez'],['avoir','aie · ayons · ayez',true],['aller et savoir','va · allons · allez — sache · sachons · sachez']],
       say:"Soyez à côté d'elle, ayez sa carte à la main, et sachez que l'aide arrive.",
       note:"« Va » perd son s, mais le reprend devant y : « Vas-y ». Petite exception, souvent entendue."},

      {t:'labo', h:"La même consigne, cinq contextes",
       p:"Choisissez un contexte et écoutez la consigne telle qu'elle se dit vraiment.",
       axes:[{id:'c', lbl:'Quel contexte ?', opts:[
         ['a','au téléphone avec le 9-1-1'],
         ['b','à l\'arrivée des ambulanciers'],
         ['c','au triage'],
         ['d','sur l\'unité de soins'],
         ['e','au congé de l\'hôpital']]}],
       out:{
         a:{w:['restez'], say:"Restez près d'elle, couvrez-la et ne la déplacez pas.", n:"trois ordres en une phrase : c'est la norme"},
         b:{w:['reculez'], say:"Reculez un peu et laissez-nous passer avec la civière.", n:"court, sans « s'il vous plaît »"},
         c:{w:['asseyez-vous'], say:"Allez vous asseoir, on vous appellera par son nom.", n:"un ordre qui contient une promesse"},
         d:{w:['appuyez'], say:"Appuyez sur la cloche si elle veut se lever, ne la levez pas seule.", n:"un ordre positif et un négatif"},
         e:{w:['revenez'], say:"Revenez à l'urgence si la fièvre remonte ou si la plaie devient rouge.", n:"la consigne qui compte le plus, à noter"},
       },
       note:"Écoutez le ton : il descend à la fin. Un ordre ne monte pas comme une question."},

      {t:'ex', h:"À écouter et à répéter",
       p:"Six consignes entendues pendant cette nuit-là.",
       rows:[
         ["Restez près d'elle et parlez-lui.","affirmatif, deux verbes"],
         ["Ne la déplacez pas.","négatif"],
         ["Couvrez-la avec une couverture.","affirmatif avec pronom"],
         ["Ne lui donnez rien à boire.","négatif avec pronom"],
         ["Allez déverrouiller la porte de l'immeuble.","aller + infinitif"],
         ["Soyez au téléphone quand ils arriveront.","irrégulier"],
       ]},

      {t:'piege', h:"Trois pièges de l'impératif",
       rows:[
         ["garder le sujet","« vous restez près d'elle » pour donner un ordre",
          "Avec le sujet, c'est une affirmation, pas un ordre. À l'impératif, on dit « Restez près d'elle. »"],
         ["laisser le s des verbes en -er","« Regardes ! »",
          "À la personne « tu », les verbes en -er perdent leur s : « Regarde ! », « Écoute ! », « Va ! » — sauf devant y : « Vas-y. »"],
         ["mal placer la négation","« Déplacez-la pas »",
          "À l'écrit et en français soutenu, le ne est obligatoire et entoure le verbe : « Ne la déplacez pas. » On l'entend tomber à l'oral familier, mais pas dans un examen ni dans un écrit."],
       ]},

      {t:'check', h:"Est-ce que c'est clair maintenant ?",
       p:"Quatre questions rapides.",
       qs:[
         {q:"Combien de personnes a l'impératif ?", opts:["trois","six"], ok:0,
          fb:"Trois : tu, nous, vous — et sans sujet écrit."},
         {q:"« tu écoutes » à l'impératif donne…", opts:["Écoutes !","Écoute !"], ok:1,
          fb:"Les verbes en -er perdent leur s à la personne « tu »."},
         {q:"L'impératif d'« être », à « vous » :", opts:["soyez","êtes"], ok:0,
          fb:"sois, soyons, soyez."},
         {q:"La forme négative correcte :", opts:["Ne la déplacez pas.","La déplacez pas."], ok:0,
          fb:"Le ne… pas entoure le verbe, et le pronom passe devant."},
       ]},
    ]
  },

  // ════════════════════════════════════════════════════════════════════════
  t1pron: {
    eye:'Mini-leçon', tit:"Le pronom et l'ordre : devant ou derrière ?",
    blocs:[
      {t:'texte', h:"Une seule règle, et elle dépend de la forme",
       p:"Avec un ordre, le pronom change de place. <b>À l'affirmatif, il suit le verbe</b> et s'y attache par un trait d'union. <b>Au négatif, il reprend sa place habituelle, devant le verbe.</b> C'est la seule construction du français où le pronom passe derrière — d'où les hésitations.",
       note:"Regardez la paire : « Couvrez-la. » / « Ne la couvrez pas. » Le même pronom, deux places, selon la forme."},

      {t:'ana', h:"Choisir le bon pronom : le, la, les ou lui, leur",
       p:"C'est la préposition qui décide, pas le sens.",
       mots:[['Sans « à »','je couvre ma mère → je la couvre'],['Avec « à »','je parle à ma mère → je lui parle',true],['Au pluriel','les ambulanciers → je les vois · aux ambulanciers → je leur ouvre']],
       say:"Je la couvre, je lui parle, et je leur ouvre la porte.",
       note:"Le test se fait avec le verbe seul : <i>parler <b>à</b> quelqu'un</i>, <i>couvrir quelqu'un</i>. Le verbe porte sa préposition avec lui ; apprenez-les ensemble."},

      {t:'ana', h:"À l'affirmatif : le pronom suit",
       p:"Trait d'union entre le verbe et le pronom. S'il y en a deux, l'objet direct passe en premier.",
       mots:[['Un pronom','Couvrez-la. · Parlez-lui. · Prenez-les.'],['Deux pronoms','Donnez-le-lui. · Dites-le-moi.',true],['me devient moi','Écoutez-moi bien.']],
       say:"Couvrez-la, parlez-lui, et dites-moi si elle répond.",
       note:"« Donnez-le-lui » surprend, mais c'est l'ordre normal à l'affirmatif : le, la, les d'abord ; moi, toi, lui, nous, vous, leur ensuite."},

      {t:'ana', h:"Au négatif : le pronom précède",
       p:"Tout revient à la place ordinaire, entre <b>ne</b> et le verbe.",
       mots:[['Un pronom','Ne la déplacez pas. · Ne lui donnez rien.'],['Deux pronoms','Ne me le dites pas maintenant.',true],['moi redevient me','Ne me faites pas répéter.']],
       say:"Ne la déplacez pas et ne lui donnez rien à boire.",
       note:"Au négatif, l'ordre des deux pronoms redevient celui de toutes les autres phrases : me, te, se, nous, vous d'abord ; le, la, les ensuite."},

      {t:'labo', h:"La même consigne, à l'affirmatif et au négatif",
       p:"Choisissez une consigne et entendez les deux formes l'une après l'autre.",
       axes:[{id:'v', lbl:'Quelle consigne ?', opts:[
         ['a','couvrir la personne'],
         ['b','déplacer la personne'],
         ['c','parler à la personne'],
         ['d','donner à boire'],
         ['e','écouter le répartiteur']]}],
       out:{
         a:{w:['couvrez-la'], say:"Couvrez-la. Ne la découvrez pas quand ils arriveront.", n:"objet direct : la"},
         b:{w:['ne la déplacez pas'], say:"Ne la déplacez pas. Déplacez plutôt ce qui gêne autour d'elle.", n:"l'ordre négatif est le plus important des deux"},
         c:{w:['parlez-lui'], say:"Parlez-lui. Ne lui parlez pas de la facture maintenant.", n:"avec à : lui"},
         d:{w:['ne lui donnez rien'], say:"Ne lui donnez rien à boire. Donnez-lui la main, c'est tout.", n:"deux verbes, deux pronoms différents"},
         e:{w:['écoutez-moi'], say:"Écoutez-moi bien. Ne me faites pas répéter, le temps compte.", n:"moi à l'affirmatif, me au négatif"},
       },
       note:"Répétez chaque paire deux fois. C'est le va-et-vient entre les deux formes qui installe la règle, pas la règle elle-même."},

      {t:'ex', h:"À écouter et à répéter",
       p:"Six phrases prises dans l'appel du Défi 1.",
       rows:[
         ["Couvrez-la avec une couverture.","affirmatif, objet direct"],
         ["Ne la déplacez pas.","négatif, objet direct"],
         ["Parlez-lui, dites-lui que l'aide s'en vient.","affirmatif, objet indirect"],
         ["Ne lui donnez rien à boire ni à manger.","négatif, objet indirect"],
         ["Écoutez-moi bien.","moi à l'affirmatif"],
         ["Ne me raccrochez pas au nez, restez en ligne.","me au négatif"],
       ]},

      {t:'piege', h:"Trois pièges des pronoms à l'impératif",
       rows:[
         ["garder « moi » au négatif","« Ne moi faites pas répéter »",
          "moi ne s'emploie qu'après le verbe, à l'affirmatif. Devant le verbe, c'est me : « Ne me faites pas répéter. »"],
         ["oublier le trait d'union","« Couvrez la »",
          "À l'affirmatif, le trait d'union est obligatoire : « Couvrez-la. » Sans lui, « la » devient un article et la phrase change de sens."],
         ["confondre le et lui","« Ne le donnez rien à boire »",
          "On donne quelque chose <b>à</b> quelqu'un : c'est donc lui. « Ne lui donnez rien à boire. »"],
       ]},

      {t:'check', h:"Est-ce que c'est clair maintenant ?",
       p:"Quatre questions rapides.",
       qs:[
         {q:"« Couvrez ___ » (votre mère), à l'affirmatif :", opts:["Couvrez-la","La couvrez"], ok:0,
          fb:"À l'affirmatif, le pronom suit le verbe avec un trait d'union."},
         {q:"« Ne ___ déplacez pas » (votre mère) :", opts:["la","lui"], ok:0,
          fb:"déplacer quelqu'un, sans à : c'est la."},
         {q:"« Ne ___ donnez rien à boire » :", opts:["la","lui"], ok:1,
          fb:"donner quelque chose à quelqu'un : c'est lui."},
         {q:"Au négatif, « moi » devient…", opts:["me","moi"], ok:0,
          fb:"« Ne me faites pas répéter. »"},
       ]},
    ]
  },

  // ════════════════════════════════════════════════════════════════════════
  t1adresse: {
    eye:'Mini-leçon', tit:"Dire où vous êtes, quand chaque seconde compte",
    blocs:[
      {t:'texte', h:"L'adresse n'est que la moitié du travail",
       p:"Un numéro et une rue amènent les ambulanciers devant l'immeuble. Ils ne les amènent pas jusqu'à la personne. Le reste — l'étage, l'appartement, la porte, le côté — se dit en une phrase, et c'est cette phrase qui fait la différence entre trois minutes et huit.",
       note:"Vous connaissez votre logement par cœur ; eux ne l'ont jamais vu, et il fait nuit."},

      {t:'ana', h:"Les mots qui situent",
       p:"Une petite liste, à avoir en tête avant d'en avoir besoin.",
       mots:[['La hauteur','au premier étage · au sous-sol · en bas de l\'escalier'],['La façade','devant l\'entrée · derrière l\'immeuble · dans la cour arrière',true],['Le repère','à côté de la pharmacie · entre la 3e et la 4e Avenue · sur le trottoir']],
       say:"Nous sommes dans l'appartement deux, en bas de l'escalier intérieur.",
       note:"Un mot pour la hauteur, un mot pour la façade, un repère : trois éléments suffisent presque toujours."},

      {t:'ana', h:"Dehors, c'est plus difficile que dedans",
       p:"Dans un parc, un stationnement, une station de métro, donnez ce que tout le monde peut voir.",
       mots:[['Une porte, un numéro','la porte 3 du stationnement souterrain'],['Un commerce','devant le dépanneur, au coin de Bélanger',true],['Un panneau, un arrêt','à l\'arrêt d\'autobus, direction est']],
       say:"Dans le parc, près du module de jeux, du côté de la rue Bélanger.",
       note:"Si vous ne savez pas où vous êtes, dites-le et lisez à voix haute ce qui est écrit autour de vous. Le répartiteur travaillera avec ça."},

      {t:'ana', h:"Ce que vous pouvez faire avant qu'on le demande",
       p:"Quatre gestes qui font gagner une minute entière.",
       mots:[['Ouvrir','déverrouiller la porte de l\'immeuble'],['Éclairer','allumer la lumière de l\'entrée et du corridor',true],['Dégager et accueillir','enfermer le chien · envoyer quelqu\'un attendre en bas']],
       say:"Je descends déverrouiller la porte et j'allume la lumière de l'entrée.",
       note:"Dites au répartiteur ce que vous faites pendant que vous le faites : il le note, et les ambulanciers l'entendent avant d'arriver."},

      {t:'labo', h:"Cinq endroits, cinq phrases",
       p:"Choisissez un endroit et écoutez comment on le décrit.",
       axes:[{id:'e', lbl:'Où êtes-vous ?', opts:[
         ['a','dans un appartement au 3e'],
         ['b','au sous-sol d\'une maison'],
         ['c','dans un stationnement'],
         ['d','dans un parc'],
         ['e','au travail, dans un entrepôt']]}],
       out:{
         a:{w:['au troisième'], say:"Au troisième étage, appartement 34, la porte est au bout du corridor à droite.", n:"étage, numéro, chemin"},
         b:{w:['au sous-sol'], say:"Au sous-sol, l'entrée est sur le côté de la maison, par la porte blanche.", n:"dites toujours par où entrer"},
         c:{w:['stationnement'], say:"Dans le stationnement souterrain, près de la porte 3, niveau moins deux.", n:"un numéro visible vaut mieux qu'une description"},
         d:{w:['dans le parc'], say:"Dans le parc, près du module de jeux, du côté de la rue Bélanger.", n:"donnez la rue la plus proche"},
         e:{w:['à l\'entrepôt'], say:"À l'entrepôt, quai de chargement numéro 4, à l'arrière du bâtiment.", n:"au travail, quelqu'un doit attendre dehors"},
       },
       note:"Aucune de ces phrases ne dépasse quinze mots. C'est la longueur d'une bonne réponse au 9-1-1."},

      {t:'ex', h:"À écouter et à répéter",
       p:"Six façons de situer un endroit.",
       rows:[
         ["5412, rue des Ormeaux, appartement 2, à Saint-Léonard.","l'adresse complète"],
         ["Elle est en bas de l'escalier intérieur.","la hauteur"],
         ["Je vous attends devant l'entrée principale.","la façade"],
         ["L'immeuble est à côté de la pharmacie.","le repère"],
         ["C'est entre la rue Bélanger et la rue Jean-Talon.","entre deux rues"],
         ["Je descends déverrouiller et j'allume la lumière.","ce que vous faites"],
       ]},

      {t:'piege', h:"Trois pièges de l'endroit",
       rows:[
         ["donner un repère que vous seul connaissez","« c'est en face de chez Ana »",
          "Donnez ce qui est écrit et visible de la rue : un numéro, une enseigne, un nom de rue."],
         ["oublier l'étage et l'appartement","« 5412, des Ormeaux » et rien d'autre",
          "L'immeuble compte douze logements. Sans l'appartement, on frappe à douze portes."],
         ["dire « ici » ou « à la maison »","« venez vite, on est à la maison »",
          "Le répartiteur ne voit pas d'où vous appelez, même sur un téléphone cellulaire — la localisation est approximative. Il faut l'adresse, dite à voix haute."],
       ]},

      {t:'check', h:"Est-ce que c'est clair maintenant ?",
       p:"Trois questions rapides.",
       qs:[
         {q:"Après le numéro et la rue, on donne…", opts:["l'étage et l'appartement","son âge"], ok:0,
          fb:"Ce qui permet de vous trouver dans l'immeuble."},
         {q:"Dehors, le meilleur repère est…", opts:["un commerce ou un numéro visible","le nom d'un voisin"], ok:0,
          fb:"Quelque chose que tout le monde peut lire ou voir."},
         {q:"Pendant que vous attendez, vous pouvez…", opts:["déverrouiller et éclairer","déplacer la personne"], ok:0,
          fb:"Ouvrir, éclairer, enfermer le chien, envoyer quelqu'un en bas."},
       ]},
    ]
  },

  // ════════════════════════════════════════════════════════════════════════
  t2recit: {
    eye:'Mini-leçon', tit:"Imparfait et passé composé : le décor et l'évènement",
    blocs:[
      {t:'texte', h:"Deux temps, deux rôles",
       p:"Au triage, on vous demandera de raconter depuis le début. Un récit compréhensible tient sur deux temps : l'<b>imparfait</b> pour ce qui durait autour de l'évènement, le <b>passé composé</b> pour l'évènement lui-même. Ce n'est pas une question de grammaire savante : c'est ce qui permet à l'infirmière de distinguer ce qui dure de ce qui vient d'arriver.",
       note:"Un récit tout entier au passé composé se lit comme une liste. Un récit tout entier à l'imparfait n'a plus d'évènement. Il faut les deux."},

      {t:'ana', h:"L'imparfait plante le décor",
       p:"Ce qui durait, ce qui se répétait, ce qui était vrai autour.",
       mots:[['Ce qui durait','elle avait de la fièvre depuis mercredi'],['Ce qui se répétait','elle mangeait deux cuillerées par repas',true],['Le décor','il faisait noir et l\'escalier était étroit']],
       say:"Elle avait de la fièvre depuis mercredi et elle mangeait très peu.",
       note:"Formation : le radical du « nous » au présent, plus -ais, -ais, -ait, -ions, -iez, -aient. Nous fais-ons → je faisais. Une seule exception : être → j'étais."},

      {t:'ana', h:"Le passé composé raconte l'évènement",
       p:"Ce qui est arrivé une fois, à un moment qu'on peut nommer.",
       mots:[['Avec avoir','j\'ai appelé le 9-1-1'],['Avec être','elle est tombée · elle s\'est levée',true],['Le participe s\'accorde avec être','elle est tombé<b>e</b> · ils sont arrivé<b>s</b>']],
       say:"Elle s'est levée à deux heures et elle est tombée dans l'escalier.",
       note:"Les verbes de mouvement et tous les verbes pronominaux prennent <b>être</b> : aller, venir, entrer, sortir, monter, descendre, tomber, rester, se lever, se blesser."},

      {t:'ana', h:"Le même verbe, deux temps, deux sens",
       p:"Ce n'est pas le verbe qui décide : c'est ce que vous voulez dire.",
       mots:[['Le décor','elle dormait quand je suis rentrée'],['Le fait',' elle a dormi quatre heures',true],['Le changement','au début c\'était rare, puis c\'est devenu quotidien']],
       say:"Elle dormait quand je suis rentrée ; elle a dormi quatre heures en tout.",
       note:"Test rapide : si vous pouvez ajouter « ce jour-là, à telle heure », c'est le passé composé. Si vous pouvez ajouter « dans ce temps-là », c'est l'imparfait."},

      {t:'labo', h:"La même nuit, racontée cinq fois",
       p:"Choisissez un moment du récit et écoutez comment les deux temps se répartissent.",
       axes:[{id:'m', lbl:'Quel moment ?', opts:[
         ['a','les deux jours d\'avant'],
         ['b','le moment de la chute'],
         ['c','l\'arrivée en bas de l\'escalier'],
         ['d','l\'appel et l\'attente'],
         ['e','l\'arrivée des ambulanciers']]}],
       out:{
         a:{w:['elle avait'], say:"Elle avait de la fièvre depuis mercredi et elle mangeait très peu.", n:"deux imparfaits : rien n'arrive encore"},
         b:{w:['elle est tombée'], say:"Vers deux heures, elle s'est levée pour aller à la toilette et elle est tombée.", n:"deux passés composés : l'évènement"},
         c:{w:['elle parlait'], say:"Quand je suis arrivée en bas, elle me parlait déjà.", n:"un de chaque : le décor et le fait, dans la même phrase"},
         d:{w:['j\'ai appelé'], say:"J'ai appelé le 9-1-1 tout de suite et je suis restée en ligne.", n:"la suite des actions"},
         e:{w:['ils sont arrivés'], say:"Ils sont arrivés sept minutes plus tard ; elle avait encore mal à la hanche.", n:"le fait, puis l'état qui durait"},
       },
       note:"Écoutez la troisième : « quand je suis arrivée, elle me parlait ». C'est la structure la plus utile du récit — un évènement dans un décor."},

      {t:'ex', h:"À écouter et à répéter",
       p:"Six phrases du récit de Marisol, au triage.",
       rows:[
         ["Elle avait de la fièvre depuis mercredi.","imparfait : ça durait"],
         ["Elle mangeait très peu depuis deux jours.","imparfait : ça se répétait"],
         ["Cette nuit, elle s'est levée pour aller à la toilette.","passé composé : un fait daté"],
         ["Elle est tombée dans l'escalier vers deux heures.","passé composé avec être"],
         ["Quand je suis arrivée en bas, elle me parlait déjà.","les deux dans une phrase"],
         ["Je n'ai pas vu la chute, j'étais en haut.","le fait, puis le décor"],
       ]},

      {t:'piege', h:"Trois pièges du récit",
       rows:[
         ["tout mettre au passé composé","« elle a eu de la fièvre, elle a mangé peu, elle est tombée »",
          "Le décor disparaît, et l'infirmière ne sait plus ce qui durait depuis deux jours. « Elle avait de la fièvre » n'est pas la même information que « elle a eu de la fièvre »."],
         ["oublier l'accord avec être","« elle est tombé »",
          "Avec l'auxiliaire être, le participe s'accorde avec le sujet : elle est tombé<b>e</b>, ils sont arrivé<b>s</b>, nous sommes resté<b>es</b>."],
         ["employer avoir avec les verbes pronominaux","« elle s'a levée »",
          "Tous les verbes pronominaux prennent être : elle <b>s'est</b> levée, je <b>me suis</b> blessé, ils <b>se sont</b> assis."],
       ]},

      {t:'check', h:"Est-ce que c'est clair maintenant ?",
       p:"Quatre questions rapides.",
       qs:[
         {q:"« Elle ___ de la fièvre depuis mercredi » :", opts:["avait","a eu"], ok:0,
          fb:"Ça durait au moment de la chute : imparfait."},
         {q:"« Elle ___ dans l'escalier vers deux heures » :", opts:["tombait","est tombée"], ok:1,
          fb:"Un évènement daté : passé composé."},
         {q:"L'auxiliaire de « se lever » :", opts:["avoir","être"], ok:1,
          fb:"Tous les verbes pronominaux prennent être."},
         {q:"« Quand je suis arrivée, elle me ___ » :", opts:["parlait","a parlé"], ok:0,
          fb:"C'était en cours quand l'autre fait est arrivé : imparfait."},
       ]},
    ]
  },

  // ════════════════════════════════════════════════════════════════════════
  t2ind: {
    eye:'Mini-leçon', tit:"Rapporter une question sans point d'interrogation",
    blocs:[
      {t:'texte', h:"À quoi ça sert, concrètement",
       p:"Pendant une hospitalisation, vous passez votre temps à répéter à quelqu'un d'autre ce qu'on vous a demandé : à votre frère, à votre employeur, à l'infirmière du quart suivant. Une question rapportée n'est plus une question : elle devient un morceau de phrase, sans inversion et sans point d'interrogation.",
       note:"C'est un des points où le niveau 5 se distingue du niveau 4 : on ne répond plus seulement aux questions, on les rapporte."},

      {t:'ana', h:"Question fermée → si",
       p:"Toute question à laquelle on répond par oui ou non devient <b>si</b>.",
       mots:[['La question','« Est-ce qu\'elle est consciente ? »'],['Rapportée','Il m\'a demandé si elle était consciente.',true],['Jamais','« il m\'a demandé est-ce qu\'elle est consciente »']],
       say:"Il m'a demandé si elle était consciente et si elle respirait normalement.",
       note:"Attention à ne pas confondre avec le <b>si</b> de condition (« si elle tombe, appelez »). Ce sont deux mots différents qui s'écrivent pareil."},

      {t:'ana', h:"« Qu'est-ce que » → ce que · « Qu'est-ce qui » → ce qui",
       p:"Les deux formes les plus fréquentes, et les plus souvent ratées.",
       mots:[['Sujet','« Qu\'est-ce qui s\'est passé ? » → ce qui s\'est passé'],['Complément','« Qu\'est-ce que vous avez vu ? » → ce que j\'ai vu',true],['Repère','ce qui est suivi d\'un verbe · ce que est suivi d\'un sujet']],
       say:"Elle m'a demandé ce qui s'était passé et ce que j'avais vu.",
       note:"Le raccourci qui marche : si la réponse commence par un verbe, c'est <b>ce qui</b> ; si elle commence par quelqu'un, c'est <b>ce que</b>."},

      {t:'ana', h:"Les autres mots ne changent pas",
       p:"où, quand, comment, combien, pourquoi, quel : ils passent tels quels.",
       mots:[['Lieu et temps','Il m\'a demandé où elle avait mal, quand elle était tombée'],['Quantité','Je ne sais pas combien de temps nous attendrons',true],['L\'ordre des mots','sujet, puis verbe — jamais d\'inversion']],
       say:"L'infirmière m'a demandé où elle avait mal et quand elle était tombée.",
       note:"L'erreur la plus visible n'est pas le mot choisi : c'est l'inversion gardée. « Il m'a demandé où avait-elle mal » ne se dit pas."},

      {t:'labo', h:"Cinq questions du triage, rapportées",
       p:"Choisissez une question et entendez-la des deux façons.",
       axes:[{id:'q', lbl:'Quelle question ?', opts:[
         ['a','Est-ce qu\'elle est consciente ?'],
         ['b','Qu\'est-ce qui s\'est passé ?'],
         ['c','Où avez-vous mal ?'],
         ['d','Quel âge a-t-elle ?'],
         ['e','Combien de temps allons-nous attendre ?']]}],
       out:{
         a:{w:['si'], say:"Il m'a demandé si elle était consciente.", n:"question fermée : si"},
         b:{w:['ce qui'], say:"Elle m'a demandé ce qui s'était passé.", n:"sujet : ce qui"},
         c:{w:['où'], say:"Elle lui a demandé où elle avait mal.", n:"le mot ne change pas, l'ordre si"},
         d:{w:['quel âge'], say:"Il m'a demandé quel âge elle avait.", n:"pas d'inversion : elle avait"},
         e:{w:['combien'], say:"Je ne sais pas combien de temps nous allons attendre.", n:"après « je ne sais pas », même construction"},
       },
       note:"« Je ne sais pas… » et « il m'a demandé… » se construisent exactement pareil. Un seul mécanisme, deux entrées."},

      {t:'ex', h:"À écouter et à répéter",
       p:"Six phrases rapportées, telles qu'on les redit au téléphone.",
       rows:[
         ["Il m'a demandé si elle était consciente.","fermée → si"],
         ["Il m'a demandé si elle prenait des médicaments.","fermée → si"],
         ["Elle m'a demandé ce qui s'était passé.","sujet → ce qui"],
         ["Elle m'a demandé ce que j'avais vu.","complément → ce que"],
         ["L'infirmière m'a demandé où elle avait mal.","où"],
         ["Je ne sais pas combien de temps ça va prendre.","combien"],
       ]},

      {t:'piege', h:"Trois pièges de la question rapportée",
       rows:[
         ["garder « est-ce que »","« il m'a demandé est-ce qu'elle respirait »",
          "« Est-ce que » n'existe que dans une vraie question. Rapportée, elle devient si : « il m'a demandé si elle respirait »."],
         ["garder l'inversion","« je ne sais pas où est-elle »",
          "Dans une question rapportée, l'ordre redevient sujet + verbe : « je ne sais pas où elle est »."],
         ["confondre ce qui et ce que","« elle m'a demandé ce que s'est passé »",
          "« Se passer » a besoin d'un sujet : c'est donc ce qui. « Elle m'a demandé ce qui s'est passé. »"],
       ]},

      {t:'check', h:"Est-ce que c'est clair maintenant ?",
       p:"Quatre questions rapides.",
       qs:[
         {q:"« Est-ce qu'elle respire ? » rapporté donne…", opts:["s'il respire","si elle respire"], ok:1,
          fb:"Question fermée : si, avec le sujet d'origine."},
         {q:"« Qu'est-ce qui s'est passé ? » devient…", opts:["ce qui s'est passé","ce que s'est passé"], ok:0,
          fb:"Le mot est sujet du verbe : ce qui."},
         {q:"« Où est-elle ? » rapporté donne…", opts:["où est-elle","où elle est"], ok:1,
          fb:"Pas d'inversion dans une question rapportée."},
         {q:"« Qu'est-ce que vous avez vu ? » devient…", opts:["ce que j'ai vu","ce qui j'ai vu"], ok:0,
          fb:"Le mot est complément : ce que."},
       ]},
    ]
  },

  // ════════════════════════════════════════════════════════════════════════
  t2triage: {
    eye:'Mini-leçon', tit:"Le triage : pourquoi l'ordre d'arrivée ne compte pas",
    blocs:[
      {t:'texte', h:"Cinq niveaux, la même échelle partout au Québec",
       p:"Toutes les urgences du Québec classent les personnes qui arrivent selon la même échelle canadienne de triage et de gravité : cinq niveaux, du plus urgent au moins urgent. L'évaluation dure moins de cinq minutes et repose sur le motif de la visite, les antécédents, les signes vitaux et quelques questions dirigées.",
       note:"Comprendre ce système change complètement une nuit d'attente. Ce n'est pas de la lenteur : c'est un ordre, et cet ordre n'est pas celui de la porte d'entrée."},

      {t:'ana', h:"Ce que veut dire chaque chiffre",
       p:"Du plus pressant au moins pressant.",
       mots:[['1 et 2','la vie est en danger, ou une atteinte grave est possible'],['3','urgent : l\'état peut se dégrader — le cas d\'Amparo',true],['4 et 5','moins urgent, puis non urgent : ce qui peut attendre longtemps']],
       say:"Je la mets à trois : une fracture possible avec de la fièvre, à soixante et onze ans.",
       note:"Un niveau 4 ou 5 n'est pas un mauvais diagnostic : c'est un bon signe. Cela veut dire que rien ne menace de s'aggraver pendant l'attente."},

      {t:'ana', h:"Ce que le triage veut entendre de vous",
       p:"Quatre minutes, quatre informations. Préparez-les pendant que vous attendez au comptoir.",
       mots:[['Ce qui est arrivé','le récit court, avec l\'heure'],['Ce qui durait avant','la fièvre depuis mercredi, le peu d\'appétit',true],['Le reste','les médicaments, les allergies, la carte d\'assurance maladie']],
       say:"Elle avait de la fièvre depuis mercredi ; cette nuit, elle est tombée dans l'escalier.",
       note:"Apportez la liste des médicaments ou la boîte elle-même. C'est la question qui bloque le plus souvent les familles, et la réponse « je ne sais pas » fait perdre du temps à tout le monde."},

      {t:'ana', h:"Votre niveau peut changer",
       p:"Le triage n'est pas une décision définitive.",
       mots:[['Si ça empire','retournez au comptoir et dites-le'],['On peut réévaluer','et reclasser à un niveau plus urgent',true],['L\'erreur fréquente','attendre en silence pour ne pas déranger']],
       say:"Sa douleur a beaucoup augmenté depuis une heure, est-ce que vous pouvez la revoir ?",
       note:"Dire qu'on va plus mal n'est pas se plaindre : c'est une information clinique, et le personnel la traite comme telle."},

      {t:'labo', h:"Cinq personnes dans la même salle d'attente",
       p:"Choisissez une personne et voyez quel niveau lui correspond.",
       axes:[{id:'p', lbl:'Qui arrive ?', opts:[
         ['a','une personne qui ne respire plus'],
         ['b','un homme de 60 ans, douleur à la poitrine'],
         ['c','une dame de 71 ans, fracture possible'],
         ['d','une coupure à recoudre'],
         ['e','un mal de gorge depuis trois jours']]}],
       out:{
         a:{w:['niveau 1'], say:"Niveau un : réanimation, on entre immédiatement.", n:"la vie est en danger"},
         b:{w:['niveau 2'], say:"Niveau deux : très urgent, une atteinte grave est possible.", n:"vu en quelques minutes"},
         c:{w:['niveau 3'], say:"Niveau trois : urgent, l'état peut se dégrader.", n:"le cas d'Amparo"},
         d:{w:['niveau 4'], say:"Niveau quatre : moins urgent, mais il faut des points de suture.", n:"l'attente peut être longue"},
         e:{w:['niveau 5'], say:"Niveau cinq : non urgent, cela aurait pu attendre le 8-1-1.", n:"la moitié des longues attentes vient de là"},
       },
       note:"Regardez la dernière : c'est exactement l'appel que le 8-1-1 aurait réglé au téléphone, gratuitement, sans quatre heures d'attente."},

      {t:'ex', h:"À écouter et à répéter",
       p:"Six phrases à dire ou à comprendre au triage.",
       rows:[
         ["C'est vous qui accompagnez madame Quintero ?","la première question"],
         ["Je prends ses signes vitaux et je lui donne une priorité.","ce que fait l'infirmière"],
         ["Chaque personne reçoit un niveau, de un à cinq.","l'échelle"],
         ["Je ne peux pas vous promettre une heure.","la réponse à attendre"],
         ["Est-ce qu'elle a des allergies ?","la question qui bloque les familles"],
         ["Sa douleur a beaucoup augmenté, pouvez-vous la revoir ?","demander une réévaluation"],
       ]},

      {t:'piege', h:"Trois pièges de l'attente",
       rows:[
         ["croire à un oubli","« ça fait deux heures, ils nous ont oubliés »",
          "Personne n'est oublié : chaque arrivée est classée, et une ambulance qui entre avec un niveau 1 déplace toute la file. Demandez plutôt : « est-ce que son niveau a changé ? »"],
         ["exiger une durée précise","« dites-moi juste combien de temps »",
          "Aucune durée ne peut être promise, et une promesse fausse serait pire. Ce qu'on peut vous dire, c'est le niveau et ce qui est prévu : radiographie, prise de sang, médecin."],
         ["partir sans le dire","« on s'en va, ça sert à rien »",
          "Prévenez le triage avant de partir. Sinon, on vous appellera, puis on vous cherchera — et le nom reste au tableau pendant des heures."],
       ]},

      {t:'check', h:"Est-ce que c'est clair maintenant ?",
       p:"Quatre questions rapides.",
       qs:[
         {q:"Combien de niveaux compte l'échelle de triage ?", opts:["trois","cinq"], ok:1,
          fb:"Cinq, de 1 (vie en danger) à 5 (non urgent)."},
         {q:"Une personne arrivée après vous passe avant. C'est…", opts:["un oubli","son niveau qui est plus urgent"], ok:1,
          fb:"L'ordre d'arrivée ne compte pas : le niveau, oui."},
         {q:"Pendant l'attente, la douleur augmente beaucoup. Vous…", opts:["attendez sans déranger","retournez le dire au triage"], ok:1,
          fb:"On peut réévaluer et reclasser. Le dire est une information, pas une plainte."},
         {q:"L'infirmière du triage peut vous promettre…", opts:["une heure précise","le niveau et ce qui est prévu"], ok:1,
          fb:"Une seule ambulance peut tout changer ; la durée ne se promet pas."},
       ]},
    ]
  },

  // ════════════════════════════════════════════════════════════════════════
  t3fut: {
    eye:'Mini-leçon', tit:"Le futur simple — annoncer ce qui s'en vient",
    blocs:[
      {t:'texte', h:"Le temps des nouvelles",
       p:"Quand vous appelez la famille depuis un corridor d'hôpital, la moitié de ce que vous dites porte sur ce qui n'est pas encore arrivé : quand elle sortira, qui viendra, ce qu'il faudra apporter. C'est le <b>futur simple</b>. À l'écrit, il est presque obligatoire ; à l'oral, il alterne avec le futur proche.",
       note:"Un seul jeu de terminaisons pour tous les verbes du français, sans exception. C'est le temps le plus régulier de la langue."},

      {t:'ana', h:"La formation : l'infinitif plus six terminaisons",
       p:"On ajoute -ai, -as, -a, -ons, -ez, -ont à l'infinitif.",
       mots:[['Verbes en -er et -ir','elle sortira · nous appellerons'],['Verbes en -re','le e tombe : attendre → elle attendra',true],['Les terminaisons','elles sont celles du verbe avoir au présent']],
       say:"Elle sortira jeudi et nous irons la chercher en voiture.",
       note:"Le repère qui aide : dans toutes les formes, il y a un <b>r</b> juste avant la terminaison. Si vous n'entendez pas ce r, ce n'est pas un futur."},

      {t:'ana', h:"Les irréguliers dont vous aurez besoin ici",
       p:"Neuf verbes couvrent presque tout ce qu'on dit dans un hôpital.",
       mots:[['Les plus fréquents','être → sera · avoir → aura · aller → ira · faire → fera'],['Les verbes de la sortie','venir → viendra · pouvoir → pourra · devoir → devra',true],['Deux autres','voir → verra · falloir → il faudra']],
       say:"Le médecin la verra demain ; il faudra une barre d'appui dans l'escalier.",
       note:"Ils sont irréguliers dans le radical seulement. Les terminaisons, elles, ne changent jamais."},

      {t:'ana', h:"Futur simple ou futur proche ?",
       p:"Les deux sont corrects ; ils ne disent pas tout à fait la même chose.",
       mots:[['Futur proche','elle va sortir — tout de suite, ou presque'],['Futur simple','elle sortira — un fait posé, plus loin',true],['À l\'écrit','le futur simple, presque toujours']],
       say:"Elle va sortir de la salle d'opération ; elle sortira de l'hôpital jeudi.",
       note:"Dans un message écrit à la famille ou à un employeur, préférez le futur simple : il est plus net et plus sobre."},

      {t:'labo', h:"Cinq annonces à faire au téléphone",
       p:"Choisissez une annonce et écoutez-la au futur simple.",
       axes:[{id:'a', lbl:'Quelle annonce ?', opts:[
         ['a','la date de sortie'],
         ['b','la visite du CLSC'],
         ['c','la marchette'],
         ['d','le rendez-vous de suivi'],
         ['e','ce qu\'il faut apporter']]}],
       out:{
         a:{w:['elle sortira'], say:"Elle sortira dans trois ou quatre jours, si elle marche avec la physiothérapeute.", n:"une condition, pas une promesse"},
         b:{w:['viendra'], say:"Une intervenante du CLSC viendra la voir avant sa sortie.", n:"venir → viendra"},
         c:{w:['devra'], say:"Elle devra marcher avec une marchette pendant quelques semaines.", n:"devoir → devra"},
         d:{w:['recevrez'], say:"Vous recevrez la date du rendez-vous de suivi au moment du congé.", n:"recevoir → recevrez"},
         e:{w:['il faudra'], say:"Il faudra apporter ses lunettes, sa robe de chambre et des pantoufles fermées.", n:"falloir → il faudra"},
       },
       note:"Cinq phrases, cinq irréguliers. Apprenez-les dans ces phrases-là plutôt qu'en liste."},

      {t:'ex', h:"À écouter et à répéter",
       p:"Six phrases pour l'appel de nouvelles.",
       rows:[
         ["Elle sortira dans trois ou quatre jours.","sortir"],
         ["Vous recevrez un résumé et les ordonnances.","recevoir"],
         ["Une intervenante du CLSC viendra avant sa sortie.","venir"],
         ["Elle devra marcher avec une marchette.","devoir"],
         ["Il faudra une barre d'appui dans l'escalier.","falloir"],
         ["Je vous appellerai dès que j'aurai la date.","appeler et avoir"],
       ]},

      {t:'piege', h:"Trois pièges du futur",
       rows:[
         ["mettre le présent après « quand »","« elle sortira quand elle marche quinze pas »",
          "En français, après quand, dès que, aussitôt que, on met le futur : « quand elle marchera quinze pas »."],
         ["oublier le r","« elle sorta » au lieu de « elle sortira »",
          "Toutes les formes du futur contiennent le r de l'infinitif. Si vous ne l'entendez pas, la forme est fausse."],
         ["employer le futur proche à l'écrit","« elle va sortir jeudi, on va aller la chercher »",
          "Ce n'est pas une faute, mais c'est de l'oral. Dans un courriel, écrivez « elle sortira jeudi et nous irons la chercher »."],
       ]},

      {t:'check', h:"Est-ce que c'est clair maintenant ?",
       p:"Quatre questions rapides.",
       qs:[
         {q:"Le futur de « venir », à « elle » :", opts:["viendra","venira"], ok:0,
          fb:"venir → viendra. Le radical change, pas la terminaison."},
         {q:"« Elle sortira quand elle ___ quinze pas » :", opts:["marche","marchera"], ok:1,
          fb:"Après quand, le futur est obligatoire en français."},
         {q:"Dans un courriel, on préfère…", opts:["le futur simple","le futur proche"], ok:0,
          fb:"Plus net et plus sobre à l'écrit."},
         {q:"Toutes les formes du futur contiennent…", opts:["un r","un s"], ok:0,
          fb:"Le r de l'infinitif : sortira, viendra, fera, aura."},
       ]},
    ]
  },

  // ════════════════════════════════════════════════════════════════════════
  t3rap: {
    eye:'Mini-leçon', tit:"Redire ce qu'on vous a dit, sans le déformer",
    blocs:[
      {t:'texte', h:"Le cœur d'un appel de nouvelles",
       p:"Vous sortez de la chambre et vous appelez votre frère. Presque tout ce que vous allez dire, quelqu'un d'autre l'a dit avant vous : la docteure, l'infirmière, la physiothérapeute. Rapporter proprement, c'est <b>garder l'information exacte</b> tout en changeant de bouche — donc changer les pronoms, les déterminants, parfois le temps.",
       note:"Rapporter n'est pas citer. Personne ne veut vous entendre imiter le médecin ; on veut savoir ce qu'il a dit."},

      {t:'ana', h:"Le verbe qui introduit, et le « que » obligatoire",
       p:"dire que, expliquer que, répondre que, ajouter que pour une affirmation ; demander de + infinitif pour un ordre.",
       mots:[['Affirmation','La docteure dit que la douleur est contrôlée.'],['Ordre','Elle m\'a demandé de vérifier les allergies.',true],['Jamais sans que','« il dit elle a une fracture » ne se dit pas']],
       say:"La docteure dit que la douleur est contrôlée et qu'elle a bien dormi.",
       note:"Si vous rapportez deux choses, répétez le que : « … que la douleur est contrôlée et <b>qu'</b>elle a bien dormi »."},

      {t:'ana', h:"Les pronoms et les déterminants changent de propriétaire",
       p:"C'est l'erreur la plus fréquente, et celle qui rend le message incompréhensible.",
       mots:[['« Votre mère sortira jeudi »','La docteure dit que ma mère sortira jeudi.'],['« Je passerai demain »','Elle dit qu\'elle passera demain.',true],['« Nous la gardons trois jours »','Ils disent qu\'ils la gardent trois jours.']],
       say:"Elle dit qu'elle passera demain et que ma mère sortira jeudi.",
       note:"Demandez-vous chaque fois : qui parle maintenant, et de qui ? Puis ajustez les mots qui désignent les personnes."},

      {t:'ana', h:"Au présent, rien ne recule",
       p:"Quand vous rapportez tout de suite avec un verbe au présent, les temps ne changent pas.",
       mots:[['Verbe introducteur au présent','Elle dit qu\'elle va bien.'],['Verbe introducteur au passé','Elle a dit qu\'elle allait bien.',true],['Le décalage','présent → imparfait · passé composé → plus-que-parfait · futur → conditionnel']],
       say:"La docteure dit qu'elle va bien ; hier, elle a dit qu'elle allait mieux.",
       note:"Au niveau 5, contentez-vous du présent : « la docteure dit que… ». C'est correct, c'est naturel, et ça évite tout le décalage des temps."},

      {t:'labo', h:"Quatre phrases entendues, quatre phrases rapportées",
       p:"Choisissez une phrase et écoutez-la telle qu'on la redit au téléphone.",
       axes:[{id:'r', lbl:'Qui a dit quoi ?', opts:[
         ['a','la docteure : « la douleur est contrôlée »'],
         ['b','la docteure : « votre mère devra marcher avec une marchette »'],
         ['c','l\'infirmière : « vérifiez les allergies »'],
         ['d','la physiothérapeute : « je passerai demain matin »'],
         ['e','l\'infirmière : « est-ce qu\'elle a des allergies ? »']]}],
       out:{
         a:{w:['dit que'], say:"La docteure dit que la douleur est contrôlée.", n:"affirmation : dire que"},
         b:{w:['ma mère'], say:"Elle dit que ma mère devra marcher avec une marchette.", n:"votre mère devient ma mère"},
         c:{w:['demandé de'], say:"L'infirmière m'a demandé de vérifier les allergies.", n:"ordre : demander de + infinitif"},
         d:{w:['qu\'elle'], say:"La physiothérapeute dit qu'elle passera demain matin.", n:"je devient elle"},
         e:{w:['demandé si'], say:"Elle m'a demandé si maman avait des allergies.", n:"question fermée : si"},
       },
       note:"Quatre mécanismes en tout : que, de + infinitif, si, et le changement de personne. Il n'y en a pas d'autres à ce niveau."},

      {t:'ex', h:"À écouter et à répéter",
       p:"Six phrases de l'appel de Marisol à son frère.",
       rows:[
         ["Écoute-moi d'abord : maman va bien.","rassurer avant de raconter"],
         ["La docteure dit que la douleur est contrôlée.","dire que"],
         ["Elle dit que maman devra marcher avec une marchette.","changement de déterminant"],
         ["Elle m'a demandé si maman avait des allergies.","question rapportée"],
         ["L'infirmière m'a demandé de vérifier son carnet.","demander de"],
         ["Les visites sont de onze heures à vingt heures.","le pratique, à la fin"],
       ]},

      {t:'piege', h:"Trois pièges du discours rapporté",
       rows:[
         ["oublier le « que »","« la docteure dit elle va bien »",
          "En français, la conjonction est obligatoire, même à l'oral rapide : « la docteure dit qu'elle va bien »."],
         ["garder le pronom d'origine","« elle a dit que je passerai demain »",
          "Si c'est la physiothérapeute qui passe, ce n'est plus « je » : « elle a dit qu'elle passerait demain »."],
         ["rapporter un ordre avec que","« elle m'a demandé que je vérifie »",
          "Avec demander, l'ordre se rapporte par de + infinitif : « elle m'a demandé de vérifier »."],
       ]},

      {t:'check', h:"Est-ce que c'est clair maintenant ?",
       p:"Quatre questions rapides.",
       qs:[
         {q:"« La docteure dit ___ la douleur est contrôlée » :", opts:["que","de"], ok:0,
          fb:"Une affirmation se rapporte avec que."},
         {q:"« Vérifiez les allergies » se rapporte par…", opts:["demander que","demander de + infinitif"], ok:1,
          fb:"« Elle m'a demandé de vérifier les allergies. »"},
         {q:"« Votre mère sortira jeudi », rapporté par vous :", opts:["ma mère","votre mère"], ok:0,
          fb:"Le déterminant change de propriétaire."},
         {q:"Avec « elle dit que », les temps…", opts:["reculent","ne changent pas"], ok:1,
          fb:"Au présent, rien ne recule. C'est la forme la plus simple, et elle suffit."},
       ]},
    ]
  },

  // ════════════════════════════════════════════════════════════════════════
  t3etapes: {
    eye:'Mini-leçon', tit:"Préparer le congé deux jours à l'avance",
    blocs:[
      {t:'texte', h:"Le matin du départ, il est trop tard",
       p:"Un congé d'hôpital s'annonce souvent la veille, parfois le matin même. Ce jour-là, tout va vite : un résumé, des ordonnances, une date de suivi, huit consignes dites debout dans un corridor. Les questions qui comptent — le transport, l'escalier, les repas, qui sera à la maison — se posent <b>avant</b>, pendant que quelqu'un a encore le temps d'y répondre.",
       note:"Une personne qui rentre chez elle sans que rien ne soit préparé revient souvent à l'urgence dans la semaine. C'est vrai pour les personnes âgées comme pour les autres."},

      {t:'ana', h:"Ce qu'on vous remet au départ",
       p:"Quatre documents, à demander par écrit.",
       mots:[['Le résumé','ce qui s\'est passé et ce qui a été fait'],['Les ordonnances','les médicaments, et ce qui change',true],['La suite','la date du rendez-vous de suivi · la demande de services à domicile']],
       say:"Au congé, vous recevrez un résumé, les ordonnances et le rendez-vous de suivi.",
       note:"Demandez que les consignes soient écrites. Personne ne retient huit choses dites une seule fois, dans un corridor, en pleine émotion."},

      {t:'ana', h:"Le mot à connaître : le CLSC",
       p:"C'est par lui que passent les services à domicile.",
       mots:[['Ce qu\'il fait','aide, soins, évaluation du logement'],['Qui fait la demande','l\'hôpital, avant la sortie',true],['À quelle condition','que quelqu\'un dise qu\'il y a un escalier et personne le jour']],
       say:"Une intervenante du CLSC passera vous voir avant sa sortie.",
       note:"Une demande faite après le retour à la maison prend beaucoup plus de temps. Dites votre situation pendant l'hospitalisation, pas après."},

      {t:'ana', h:"Dire sa situation réelle, sans gêne",
       p:"Ce sont des faits, pas des plaintes, et ils changent le plan de sortie.",
       mots:[['Le logement','un escalier intérieur, un troisième sans ascenseur'],['Les heures','je travaille de jour, personne à la maison avant dix-sept heures',true],['Ce que ça donne','une barre d\'appui, une évaluation à domicile, une aide']],
       say:"Il y a un escalier chez nous, et c'est là qu'elle est tombée.",
       note:"Taire ces faits par gêne ne rend service à personne — surtout pas à la personne qui rentre à la maison."},

      {t:'labo', h:"Cinq questions à poser, et pourquoi",
       p:"Choisissez une question et entendez la raison de la poser tôt.",
       axes:[{id:'q', lbl:'Quelle question ?', opts:[
         ['a','« Quel jour prévoyez-vous le congé ? »'],
         ['b','« Est-ce qu\'elle pourra monter un escalier ? »'],
         ['c','« Est-ce que les médicaments changent ? »'],
         ['d','« Quand est le rendez-vous de suivi ? »'],
         ['e','« Qu\'est-ce qui doit m\'inquiéter à la maison ? »']]}],
       out:{
         a:{w:['le congé'], say:"Quel jour prévoyez-vous le congé ? Je dois organiser le transport.", n:"pour prendre congé au travail"},
         b:{w:['un escalier'], say:"Est-ce qu'elle pourra monter un escalier ? Sa chambre est à l'étage.", n:"ça décide de tout le reste"},
         c:{w:['les médicaments'], say:"Est-ce que ses médicaments changent ? Je passerai à la pharmacie avant.", n:"pour ne pas y aller avec elle dans l'auto"},
         d:{w:['le suivi'], say:"Quand est le rendez-vous de suivi, et qui doit l'accompagner ?", n:"à inscrire tout de suite"},
         e:{w:['m\'inquiéter'], say:"Qu'est-ce qui doit m'inquiéter à la maison, et quand faut-il revenir ?", n:"la question la plus importante des cinq"},
       },
       note:"Notez ces cinq questions dans votre téléphone pendant l'hospitalisation. Le jour du congé, vous n'aurez qu'à les lire."},

      {t:'ex', h:"À écouter et à répéter",
       p:"Six phrases à dire avant la sortie.",
       rows:[
         ["Quel jour prévoyez-vous le congé ?","la date"],
         ["Il y a un escalier chez nous.","le logement"],
         ["Je travaille de jour, personne n'est là avant dix-sept heures.","les heures"],
         ["Est-ce que ses médicaments changent ?","la pharmacie"],
         ["Est-ce que je peux avoir les consignes par écrit ?","la demande qui sauve"],
         ["Qu'est-ce qui doit me faire revenir à l'urgence ?","les signes de retour"],
       ]},

      {t:'piege', h:"Trois pièges du congé",
       rows:[
         ["attendre le jour même","« on verra bien quand ils la laisseront sortir »",
          "Le jour même, il n'y a plus de temps pour organiser quoi que ce soit. Les questions se posent deux jours avant."],
         ["ne rien demander par écrit","« oui oui, j'ai compris, merci »",
          "Huit consignes dites une fois ne se retiennent pas. Demandez la feuille, ou notez pendant qu'on parle."],
         ["cacher les difficultés du logement","« non non, ça va aller, on s'organisera »",
          "Un escalier, un travail de jour, un logement sans ascenseur : ces faits déclenchent des services. Les taire les empêche."],
       ]},

      {t:'check', h:"Est-ce que c'est clair maintenant ?",
       p:"Quatre questions rapides.",
       qs:[
         {q:"Les questions du congé se posent…", opts:["le matin du départ","deux jours avant"], ok:1,
          fb:"Le jour même, tout va trop vite."},
         {q:"Les services à domicile passent par…", opts:["le CLSC","la pharmacie"], ok:0,
          fb:"Et la demande part de l'hôpital, avant la sortie."},
         {q:"On vous remet au congé…", opts:["un résumé, des ordonnances, un suivi","rien du tout"], ok:0,
          fb:"Demandez que les consignes soient écrites."},
         {q:"Il y a un escalier chez vous. Vous…", opts:["le dites","n'en parlez pas"], ok:0,
          fb:"C'est un fait qui change le plan de sortie."},
       ]},
    ]
  },

};
