const PLUS = {
  prSon: {
    eye:'Mini-leçon', tit:"« Ou » et « u » : deux sons, deux mots",
    blocs:[
      {t:'texte', h:"Deux sons que la bouche fait presque au même endroit",
       p:"Le mot <b>cours</b> et le mot <b>bureau</b> ne se disent pas pareil, et pourtant les lèvres avancent dans les deux cas. Ce qui change, c'est la langue : pour <b>ou</b>, elle recule au fond ; pour <b>u</b>, elle monte en avant, derrière les dents du bas. Beaucoup de langues n'ont pas le son <b>u</b> : il s'apprend, il ne se devine pas.",
       note:"Ne pas commencer par la règle. Faire écouter six paires à la suite, sans rien dire, puis demander qui entend une différence. Elle n'est pas évidente le premier jour."},

      {t:'ana', h:"Le son de « bonjour » : la langue au fond",
       p:"C'est le son des mots du centre qu'on entend le plus souvent.",
       mots:[["On dit","b{on}j{ou}r — les lèvres avancent"],["Aussi","le c{ou}rs · le c{ou}loir"],["Aussi","{ou}vert · {ou}vrir · v{ou}s"],["On ne dit pas","« le curs » ni « le culoir »",true]],
       say:"Bonjour. Le cours. Le couloir. Ouvert. Vous.",
       note:"Faire dire « ou » en tenant le son cinq secondes, comme un tuyau. C'est le son que la plupart des élèves possèdent déjà."},

      {t:'ana', h:"Le son de « une » : la langue en avant",
       p:"C'est le son du bureau, des minutes et des jours de la semaine.",
       mots:[["On dit","{u}ne min{u}te — la langue monte devant"],["Aussi","le b{u}reau · le n{u}méro"],["Aussi","l{u}ndi · bien s{û}r · s{u}r la porte"],["On ne dit pas","« le boureau » ni « loundi »",true]],
       say:"Une minute. Le bureau. Le numéro. Lundi. Bien sûr.",
       note:"L'astuce qui marche : faire dire « i », garder la langue exactement où elle est, et avancer seulement les lèvres. Le « u » sort tout seul."},

      {t:'ana', h:"Les paires du centre",
       p:"Deux mots qui ne changent que par ce son.",
       mots:[["ou / u","le c{ou}rs · bien s{û}r"],["ou / u","le c{ou}loir · le b{u}reau"],["ou / u","v{ou}s · v{u}"],["ou / u","t{ou}t · t{u}"],["Ce que ça change","Un mot compris de travers fait monter au mauvais étage.",true]],
       say:"Le cours. Bien sûr. Le couloir. Le bureau. Vous. Vu. Tout. Tu.",
       note:"Les faire écouter deux fois, puis les faire produire en cachant l'écrit. L'oreille passe avant la lettre."},

      {t:'labo', h:"Écoute les deux sons",
       p:"Choisis un son et une façon de l'entendre.",
       axes:[
         {id:'p', lbl:'Quel son ?', opts:[
           ['a','le son de « bonjour »'],
           ['b','le son de « une »'],
           ['c','les deux, à la suite']]},
         {id:'q', lbl:'Dans quoi ?', opts:[['1','un mot seul'],['2','un mot du centre'],['3','une phrase']]}],
       out:{
         a1:{w:["bonjour"], say:"Bonjour.", n:'les lèvres avancent, la langue recule'},
         a2:{w:["le cours, le couloir"], say:"Le cours. Le couloir.", n:'deux mots entendus tous les matins'},
         a3:{w:["Le cours est ouvert au bout du couloir."], say:"Le cours est ouvert au bout du couloir.", n:'trois fois le même son'},
         b1:{w:["une"], say:"Une.", n:'la langue monte en avant'},
         b2:{w:["le bureau, le numéro"], say:"Le bureau. Le numéro.", n:'deux mots du secrétariat'},
         b3:{w:["Lundi, le bureau est sûrement ouvert."], say:"Lundi, le bureau est sûrement ouvert.", n:'quatre fois le son « u »'},
         c1:{w:["cours, bien sûr"], say:"Cours. Bien sûr.", n:'la paire à entendre en premier'},
         c2:{w:["le couloir, le bureau"], say:"Le couloir. Le bureau.", n:'la paire la plus utile du module'},
         c3:{w:["Le bureau est au bout du couloir."], say:"Le bureau est au bout du couloir.", n:'les deux sons dans la même phrase'},
       },
       note:"Neuf extraits. Les faire écouter les yeux fermés, une main levée pour « ou », deux pour « u »."},

      {t:'ex', h:"À écouter et à répéter",
       p:"Six mots du centre, trois par son.",
       rows:[
         ["le cours","son de « ou »"],
         ["le couloir","son de « ou »"],
         ["ouvert","son de « ou »"],
         ["le bureau","son de « u »"],
         ["une minute","son de « u »"],
         ["lundi","son de « u »"],
       ]},

      {t:'piege', h:"Trois pièges à connaître",
       rows:[
         ["dire « le boureau » pour « le bureau »","la langue reste au fond",
          "C'est le piège numéro un. Faire dire « bi-reau », puis avancer les lèvres sans bouger la langue : on obtient « bureau »."],
         ["dire « vous » pour « vu », et l'inverse","une seule lettre change tout",
          "« Vous avez » et « vu » ne veulent rien dire ensemble. Au comptoir, « vous » revient dans chaque phrase : c'est le mot à réussir en premier."],
         ["croire que « û » se dit autrement","le petit chapeau ne s'entend pas",
          "« Bien sûr » se dit exactement comme « sur la porte ». L'accent circonflexe est une affaire d'orthographe, pas de son."],
       ]},

      {t:'check', h:"Est-ce que c'est clair maintenant ?",
       p:"Quatre questions rapides.",
       qs:[
         {q:"« Le couloir » a le son de…", opts:["bonjour","une"], ok:0,
          fb:"Le son « ou », deux fois dans le mot."},
         {q:"« Lundi » a le son de…", opts:["une","bonjour"], ok:0,
          fb:"Le son « u » : la langue monte en avant."},
         {q:"« Bien sûr » se dit comme…", opts:["sur la porte","sourd"], ok:0,
          fb:"Le petit chapeau ne change pas le son."},
         {q:"Pour dire « u », la langue…", opts:["monte en avant","recule au fond"], ok:0,
          fb:"En avant, derrière les dents du bas. Au fond, c'est « ou »."},
       ]},
    ]
  },

  prOu: {
    eye:'Mini-leçon', tit:"Dire où c'est, dans le centre",
    blocs:[
      {t:'texte', h:"Trois petits mots suffisent",
       p:"Pour dire où est une chose dans un immeuble, le français emploie presque toujours les mêmes petits mots : <b>au</b> pour l'étage, <b>dans</b> pour le couloir et le local, <b>à côté de</b> et <b>en face de</b> pour ce qui est tout près. Ces mots ne se traduisent pas un par un : ils s'apprennent avec l'endroit.",
       note:"Faire le tour du vrai centre avec le groupe, à pied, dix minutes, en nommant chaque endroit. Cette mini-leçon se retient trois fois mieux debout."},

      {t:'ana', h:"« Au » pour les étages",
       p:"Un seul mot pour tous les niveaux de l'immeuble.",
       mots:[["On dit","{au} rez-de-chaussée"],["Aussi","{au} premier étage · {au} deuxième étage"],["Aussi","{au} sous-sol"],["On ne dit pas","« en le deuxième étage » ni « dans le deuxième étage »",true]],
       say:"Au rez-de-chaussée. Au premier étage. Au deuxième étage. Au sous-sol.",
       note:"« Au » est la contraction de « à le ». Ne pas expliquer la contraction au niveau 2 : donner la forme entière, comme un mot."},

      {t:'ana', h:"« Dans » pour ce qui a des murs",
       p:"Le couloir, le local, le bureau : on est dedans.",
       mots:[["On dit","{dans} le couloir"],["Aussi","{dans} le local 214 · {dans} la classe"],["Aussi","{au bout du} couloir · {à droite} · {à gauche}"],["On ne dit pas","« sur le couloir »",true]],
       say:"Dans le couloir. Dans le local 214. Au bout du couloir. À droite.",
       note:"« Au bout du couloir » est l'expression la plus utile du module : c'est la réponse que donne le concierge neuf fois sur dix."},

      {t:'ana', h:"« À côté de » et « en face de » pour ce qui est tout près",
       p:"Deux repères, et on trouve n'importe quelle porte.",
       mots:[["On dit","{à côté de} l'entrée"],["Aussi","{à côté du} secrétariat · {en face de} l'escalier"],["Aussi","{près de} la sortie · {devant} la porte"],["On ne dit pas","« à côté l'entrée » : le <b>de</b> ne se saute pas",true]],
       say:"À côté de l'entrée. À côté du secrétariat. En face de l'escalier. Près de la sortie.",
       note:"Faire remarquer « à côté du » devant un mot masculin. Un exemple suffit ; la règle des contractions vient plus tard dans le programme."},

      {t:'labo', h:"Dis où c'est",
       p:"Choisis un endroit et une façon de le dire.",
       axes:[
         {id:'p', lbl:'Quel endroit ?', opts:[
           ['a','le secrétariat'],
           ['b','le local du cours'],
           ['c','les toilettes'],
           ['d',"l'escalier"]]},
         {id:'q', lbl:'Comment ?', opts:[['1',"avec l'étage"],['2','avec un repère'],['3','la question']]}],
       out:{
         a1:{w:["Le secrétariat est au rez-de-chaussée."], say:"Le secrétariat est au rez-de-chaussée.", n:"l'étage suffit souvent"},
         a2:{w:["Le secrétariat est à côté de l'entrée."], say:"Le secrétariat est à côté de l'entrée.", n:'un repère que tout le monde connaît'},
         a3:{w:["Où est le secrétariat ?"], say:"Où est le secrétariat ?", n:'la question à poser en arrivant'},
         b1:{w:["Le local 214 est au deuxième étage."], say:"Le local 214 est au deuxième étage.", n:"le premier chiffre donne l'étage"},
         b2:{w:["Le local 214 est au bout du couloir."], say:"Le local 214 est au bout du couloir.", n:'la réponse du concierge'},
         b3:{w:["Où est le local 214 ?"], say:"Où est le local 214 ?", n:'on donne le numéro, pas le nom du cours'},
         c1:{w:["Les toilettes sont au rez-de-chaussée."], say:"Les toilettes sont au rez-de-chaussée.", n:'utile le premier jour'},
         c2:{w:["Les toilettes sont en face de l'escalier."], say:"Les toilettes sont en face de l'escalier.", n:'« en face de » se voit tout de suite'},
         c3:{w:["Où sont les toilettes, s'il vous plaît ?"], say:"Où sont les toilettes, s'il vous plaît ?", n:'au pluriel, et avec « s\'il vous plaît »'},
         d1:{w:["L'escalier monte au deuxième étage."], say:"L'escalier monte au deuxième étage.", n:'le verbe monter dit la direction'},
         d2:{w:["L'escalier est à droite du comptoir."], say:"L'escalier est à droite du comptoir.", n:'à droite, à gauche : deux mots à savoir'},
         d3:{w:["Où est l'escalier ?"], say:"Où est l'escalier ?", n:'la question qui sauve le premier matin'},
       },
       note:"Douze phrases. Les faire produire debout, en montrant du doigt la vraie direction dans le local."},

      {t:'ex', h:"À écouter et à répéter",
       p:"Six phrases pour trouver son chemin.",
       rows:[
         ["Le secrétariat est au rez-de-chaussée.","au + étage"],
         ["Mon local est au deuxième étage.","au + étage"],
         ["Les classes sont dans le couloir.","dans"],
         ["Le comptoir est à côté de l'entrée.","à côté de"],
         ["Les toilettes sont en face de l'escalier.","en face de"],
         ["Le local 214 est au bout du couloir.","au bout du"],
       ]},

      {t:'piege', h:"Trois pièges à connaître",
       rows:[
         ["dire « le premier étage » pour l'étage de l'entrée","au Québec, l'entrée est le rez-de-chaussée",
          "Dans plusieurs pays, l'étage de la porte s'appelle « le premier ». Ici, non : c'est le rez-de-chaussée, et le premier étage est au-dessus. Un élève qui compte autrement monte toujours un étage trop haut."],
         ["oublier le « de » de « à côté de »","le mot est en trois morceaux",
          "On dit « à côté de l'entrée », jamais « à côté l'entrée ». Devant un mot masculin, les deux derniers morceaux se collent : « à côté du secrétariat »."],
         ["dire « sur le couloir »","le couloir a des murs, on est dedans",
          "« Sur » sert pour une surface : sur la table, sur la porte. Pour un endroit fermé, c'est « dans » : dans le couloir, dans le local."],
       ]},

      {t:'check', h:"Est-ce que c'est clair maintenant ?",
       p:"Quatre questions rapides.",
       qs:[
         {q:"L'étage de la porte d'entrée s'appelle…", opts:["le rez-de-chaussée","le premier étage"], ok:0,
          fb:"Le premier étage est au-dessus, au Québec."},
         {q:"On dit : les classes sont ___ le couloir.", opts:["dans","sur"], ok:0,
          fb:"Un endroit fermé prend « dans »."},
         {q:"On dit : à côté ___ l'entrée.", opts:["de","à"], ok:0,
          fb:"« À côté de » ne perd jamais son « de »."},
         {q:"Le local 302 est au…", opts:["troisième étage","deuxième étage"], ok:0,
          fb:"Le premier chiffre du numéro donne l'étage."},
       ]},
    ]
  },

  t1quest: {
    eye:'Mini-leçon', tit:"Poser sa question au comptoir",
    blocs:[
      {t:'texte', h:"Une seule question à la fois",
       p:"Au comptoir, la personne devant vous répond à trente personnes par matin. Elle répond court, et elle répond à <b>une</b> question. Le module en donne cinq, et elles couvrent presque tout : demander une chose, vérifier une chose, demander l'endroit, le jour, l'heure. La sixième — « pouvez-vous répéter ? » — est celle qui sauve les cinq autres.",
       note:"Insister sur le rythme : une question, on écoute la réponse jusqu'au bout, on la répète, puis on pose la suivante. C'est ce que le programme appelle « maintenir la communication »."},

      {t:'ana', h:"Demander une chose : « Je voudrais… »",
       p:"La formule polie, et la seule à retenir par cœur.",
       mots:[["On dit","{Je voudrais} une attestation, s'il vous plaît."],["Aussi","{Je voudrais} un horaire · {Je voudrais} parler à la direction"],["Aussi","{Est-ce que je peux} avoir une attestation ?"],["On ne dit pas","« Je veux une attestation » — c'est trop direct au comptoir",true]],
       say:"Je voudrais une attestation, s'il vous plaît. Je voudrais un horaire. Est-ce que je peux avoir une attestation ?",
       note:"« Je veux » n'est pas faux, il est impoli. La différence ne s'entend pas dans une grammaire : la faire jouer deux fois, avec le ton."},

      {t:'ana', h:"Vérifier une chose : « Est-ce que… ? »",
       p:"On répond par oui ou par non. C'est la question la plus facile à poser.",
       mots:[["On dit","{Est-ce que} le bureau est ouvert ?"],["Aussi","{Est-ce que} vous avez mon papier ?"],["Aussi","{Est-ce qu'}il y a un cours lundi ?"],["On ne dit pas","« Est-ce que ouvert le bureau ? » : la phrase garde son ordre",true]],
       say:"Est-ce que le bureau est ouvert ? Est-ce que vous avez mon papier ? Est-ce qu'il y a un cours lundi ?",
       note:"« Est-ce que » se colle devant une phrase normale, sans rien changer d'autre. C'est le seul point de la leçon qui se retient en une minute."},

      {t:'ana', h:"L'endroit, le jour, l'heure",
       p:"Trois mots de question, trois renseignements.",
       mots:[["L'endroit","{Où} est le local 214 ?"],["Le jour","{Quand} est-ce que le papier est prêt ?"],["L'heure","{À quelle heure} ouvre le secrétariat ?"],["Combien","{Combien} de temps ça prend ?"],["On ne dit pas","« Où le local ? » : le verbe ne se saute pas",true]],
       say:"Où est le local 214 ? Quand est-ce que le papier est prêt ? À quelle heure ouvre le secrétariat ? Combien de temps ça prend ?",
       note:"Faire écrire les quatre questions sur une carte à garder dans la poche. Plusieurs élèves la ressortent au comptoir pendant des mois."},

      {t:'labo', h:"Pose ta question",
       p:"Choisis ce que tu veux savoir et une façon de le demander.",
       axes:[
         {id:'p', lbl:'Tu veux quoi ?', opts:[
           ['a','un papier'],
           ['b',"l'heure d'ouverture"],
           ['c','le jour où ce sera prêt'],
           ['d','faire répéter']]},
         {id:'q', lbl:'Comment ?', opts:[['1','la forme polie'],['2','la forme courte'],['3','pour vérifier']]}],
       out:{
         a1:{w:["Je voudrais une attestation, s'il vous plaît."], say:"Je voudrais une attestation, s'il vous plaît.", n:'la phrase à savoir par cœur'},
         a2:{w:["Une attestation, s'il vous plaît."], say:"Une attestation, s'il vous plaît.", n:'trois mots, et ça marche aussi'},
         a3:{w:["Est-ce que vous avez mon attestation ?"], say:"Est-ce que vous avez mon attestation ?", n:'quand le papier est déjà demandé'},
         b1:{w:["À quelle heure ouvre le secrétariat ?"], say:"À quelle heure ouvre le secrétariat ?", n:'la question complète'},
         b2:{w:["Ça ouvre à quelle heure ?"], say:"Ça ouvre à quelle heure ?", n:"la version qu'on entend le plus"},
         b3:{w:["Est-ce que c'est ouvert le midi ?"], say:"Est-ce que c'est ouvert le midi ?", n:'oui ou non, et on est fixé'},
         c1:{w:["Quand est-ce que le papier est prêt ?"], say:"Quand est-ce que le papier est prêt ?", n:'on demande un jour, pas une date'},
         c2:{w:["C'est prêt quand ?"], say:"C'est prêt quand ?", n:'court, et poli avec le sourire'},
         c3:{w:["Jeudi, c'est ça ?"], say:"Jeudi, c'est ça ?", n:'on répète pour vérifier'},
         d1:{w:["Pouvez-vous répéter, s'il vous plaît ?"], say:"Pouvez-vous répéter, s'il vous plaît ?", n:'la phrase la plus utile du module'},
         d2:{w:["Plus lentement, s'il vous plaît."], say:"Plus lentement, s'il vous plaît.", n:'quand le mot est connu mais dit trop vite'},
         d3:{w:["Excusez-moi, je n'ai pas compris."], say:"Excusez-moi, je n'ai pas compris.", n:'on le dit, on ne fait pas semblant'},
       },
       note:"Douze phrases. Les faire jouer au comptoir imaginaire : un élève assis, un élève debout, et on échange."},

      {t:'ex', h:"À écouter et à répéter",
       p:"Six phrases du comptoir.",
       rows:[
         ["Bonjour, madame.","on salue d'abord"],
         ["Je voudrais une attestation, s'il vous plaît.","la demande"],
         ["Est-ce que le bureau est ouvert le midi ?","la vérification"],
         ["À quelle heure ouvre le secrétariat ?","l'heure"],
         ["Pouvez-vous répéter, s'il vous plaît ?","quand ça va trop vite"],
         ["Merci beaucoup. Bonne journée.","on termine"],
       ]},

      {t:'piege', h:"Trois pièges à connaître",
       rows:[
         ["poser trois questions dans la même phrase","la personne ne répond qu'à la dernière",
          "« Bonjour je voudrais une attestation et c'est où et à quelle heure ? » — la réponse portera sur l'heure, et le reste sera perdu. Une question, une réponse."],
         ["dire « Je veux » au lieu de « Je voudrais »","ce n'est pas faux, c'est sec",
          "Au Québec, on adoucit une demande. « Je voudrais » et « s'il vous plaît » suffisent : ils ne coûtent rien et ils changent tout le ton de l'échange."],
         ["répondre « oui » quand on n'a pas compris","le problème revient plus tard",
          "Dire « pouvez-vous répéter ? » est normal et bien vu. Repartir sans avoir compris le jour du rendez-vous oblige à revenir demain."],
       ]},

      {t:'check', h:"Est-ce que c'est clair maintenant ?",
       p:"Quatre questions rapides.",
       qs:[
         {q:"Pour demander poliment un papier, je dis…", opts:["Je voudrais…","Je veux…"], ok:0,
          fb:"« Je voudrais », avec « s'il vous plaît »."},
         {q:"Pour une réponse oui/non, je commence par…", opts:["Est-ce que","Où"], ok:0,
          fb:"« Est-ce que » se colle devant une phrase normale."},
         {q:"Pour l'heure d'ouverture, je demande…", opts:["À quelle heure ?","Combien ?"], ok:0,
          fb:"« Combien » sert pour une quantité ou un prix."},
         {q:"Je n'ai pas compris. Je dis…", opts:["Pouvez-vous répéter ?","Oui, oui, merci."], ok:0,
          fb:"Demander de répéter fait partie de la conversation."},
       ]},
    ]
  },

  t1etage: {
    eye:'Mini-leçon', tit:"Les étages et les numéros de local",
    blocs:[
      {t:'texte', h:"Un immeuble se compte à partir du sol",
       p:"Au Québec, l'étage de la porte d'entrée s'appelle <b>le rez-de-chaussée</b>. Celui du dessus est <b>le premier étage</b>, puis <b>le deuxième</b>, <b>le troisième</b>. Dans plusieurs pays, on compte autrement, et c'est la cause d'à peu près toutes les erreurs de local du premier mois.",
       note:"Demander au groupe comment on compte les étages dans leur pays. La comparaison prend cinq minutes et évite six semaines de malentendus."},

      {t:'ana', h:"Les mots des étages",
       p:"Cinq mots, et l'immeuble entier est nommé.",
       mots:[["En bas, la porte","le {rez-de-chaussée}"],["Au-dessus","le {premier} étage"],["Ensuite","le {deuxième} étage · le {troisième} étage"],["Encore plus haut","le {quatrième} · le {cinquième}"],["On ne dit pas","« le un étage » ni « le deux étage »",true]],
       say:"Le rez-de-chaussée. Le premier étage. Le deuxième étage. Le troisième étage. Le quatrième.",
       note:"Faire écrire les cinq mots dans l'ordre, en colonne, comme un immeuble vu de côté. La liste verticale se retient mieux."},

      {t:'ana', h:"Le numéro du local dit son étage",
       p:"Le premier chiffre suffit à trouver la porte.",
       mots:[["Le local 108","le {premier} étage — les locaux 1xx"],["Le local 214","le {deuxième} étage — les locaux 2xx"],["Le local 302","le {troisième} étage — les locaux 3xx"],["Le local 005","le {rez-de-chaussée} — les locaux 0xx"],["On ne cherche pas partout","On lit le premier chiffre, et on monte.",true]],
       say:"Le local 108 est au premier étage. Le local 214 est au deuxième étage. Le local 302 est au troisième étage.",
       note:"C'est vrai dans presque tous les centres de formation du Québec. Vérifier une fois dans le vrai immeuble, avec le groupe."},

      {t:'ana', h:"Dire le numéro à voix haute",
       p:"Un numéro de local se dit en un seul nombre.",
       mots:[["On dit","le local {deux cent quatorze}"],["Aussi","le local {cent huit} · le local {trois cent deux}"],["Aussi","le {zéro zéro cinq}, pour un local du bas"],["On ne dit pas","« local deux un quatre », sauf pour épeler lentement",true]],
       say:"Le local deux cent quatorze. Le local cent huit. Le local trois cent deux.",
       note:"Les deux façons existent au comptoir. Enseigner d'abord le nombre entier ; la lecture chiffre par chiffre sert quand on n'a pas été compris."},

      {t:'labo', h:"Trouve l'étage",
       p:"Choisis un local et une façon d'en parler.",
       axes:[
         {id:'p', lbl:'Quel local ?', opts:[
           ['a','le 005'],
           ['b','le 108'],
           ['c','le 214'],
           ['d','le 302']]},
         {id:'q', lbl:'Quoi dire ?', opts:[['1',"l'étage"],['2','la question'],['3','le chemin']]}],
       out:{
         a1:{w:["Le local 005 est au rez-de-chaussée."], say:"Le local zéro zéro cinq est au rez-de-chaussée.", n:'le zéro du début annonce le bas'},
         a2:{w:["Où est le local 005 ?"], say:"Où est le local zéro zéro cinq ?", n:'la question, avec le numéro'},
         a3:{w:["C'est en bas, à côté du secrétariat."], say:"C'est en bas, à côté du secrétariat.", n:'la réponse ordinaire du concierge'},
         b1:{w:["Le local 108 est au premier étage."], say:"Le local cent huit est au premier étage.", n:'1 pour premier'},
         b2:{w:["Est-ce que le 108 est au premier ?"], say:"Est-ce que le cent huit est au premier ?", n:'on vérifie avant de monter'},
         b3:{w:["Vous montez un étage, puis à droite."], say:"Vous montez un étage, puis à droite.", n:'deux informations, pas plus'},
         c1:{w:["Le local 214 est au deuxième étage."], say:"Le local deux cent quatorze est au deuxième étage.", n:"le local du cours d'Amel"},
         c2:{w:["Le 214, c'est à quel étage ?"], say:"Le deux cent quatorze, c'est à quel étage ?", n:'la question courte, très employée'},
         c3:{w:["Deuxième étage, au bout du couloir."], say:"Deuxième étage, au bout du couloir.", n:'la réponse en cinq mots'},
         d1:{w:["Le local 302 est au troisième étage."], say:"Le local trois cent deux est au troisième étage.", n:'3 pour troisième'},
         d2:{w:["Où est le local 302, s'il vous plaît ?"], say:"Où est le local trois cent deux, s'il vous plaît ?", n:'la forme polie complète'},
         d3:{w:["Vous prenez l'escalier, trois étages."], say:"Vous prenez l'escalier, trois étages.", n:"« prendre l'escalier » : à retenir"},
       },
       note:"Douze phrases. Faire chercher les vrais numéros du centre et refaire l'exercice avec eux."},

      {t:'ex', h:"À écouter et à répéter",
       p:"Six phrases d'étage.",
       rows:[
         ["Le secrétariat est au rez-de-chaussée.","rez-de-chaussée"],
         ["Le local 108 est au premier étage.","premier"],
         ["Le local 214 est au deuxième étage.","deuxième"],
         ["Le local 302 est au troisième étage.","troisième"],
         ["Je monte deux étages.","le verbe monter"],
         ["Je prends l'escalier.","prendre l'escalier"],
       ]},

      {t:'piege', h:"Trois pièges à connaître",
       rows:[
         ["compter l'entrée comme le premier étage","au Québec, l'entrée est le rez-de-chaussée",
          "C'est l'erreur la plus fréquente, et elle fait toujours monter un étage trop haut. Repère sûr : si on voit la rue par la porte, on est au rez-de-chaussée."],
         ["dire « le deux étage »","les étages prennent premier, deuxième, troisième",
          "On dit « le deuxième étage », jamais « le deux étage ». Seul le rez-de-chaussée n'a pas de nombre."],
         ["lire le numéro chiffre par chiffre","on dit le nombre entier",
          "« Deux cent quatorze », et non « deux, un, quatre ». La lecture chiffre par chiffre sert seulement quand on doit se faire comprendre lentement."],
       ]},

      {t:'check', h:"Est-ce que c'est clair maintenant ?",
       p:"Quatre questions rapides.",
       qs:[
         {q:"Le local 214 est au…", opts:["deuxième étage","premier étage"], ok:0,
          fb:"Le premier chiffre du numéro donne l'étage."},
         {q:"L'étage de la porte d'entrée s'appelle…", opts:["le rez-de-chaussée","le premier"], ok:0,
          fb:"Le premier étage est celui du dessus."},
         {q:"On dit…", opts:["le troisième étage","le trois étage"], ok:0,
          fb:"Premier, deuxième, troisième : jamais un simple nombre."},
         {q:"Le local 005 est…", opts:["au rez-de-chaussée","au cinquième"], ok:0,
          fb:"Le zéro du début annonce le bas de l'immeuble."},
       ]},
    ]
  },

  t2neg: {
    eye:'Mini-leçon', tit:"Dire non : « ne … pas »",
    blocs:[
      {t:'texte', h:"Deux petits mots autour du verbe",
       p:"Pour dire le contraire d'une phrase, le français met <b>ne</b> devant le verbe et <b>pas</b> derrière. Le verbe se retrouve au milieu, entre les deux. C'est presque toujours la même chose, et c'est justement ce qui rend la règle facile : <b>Je viens</b> devient <b>je ne viens pas</b>.",
       note:"Écrire une phrase positive au tableau, puis venir poser « ne » et « pas » de chaque côté du verbe avec deux papiers. Le geste vaut mieux que l'explication."},

      {t:'ana', h:"La forme ordinaire",
       p:"Le verbe est pris en sandwich.",
       mots:[["On dit","Je {ne} viens {pas} demain."],["Aussi","Je {ne} comprends {pas}."],["Aussi","Le bureau {ne} ferme {pas} à midi."],["On ne dit pas","« Je viens ne pas » ni « Je ne pas viens »",true]],
       say:"Je ne viens pas demain. Je ne comprends pas. Le bureau ne ferme pas à midi.",
       note:"Faire produire cinq phrases négatives d'affilée sur le même modèle. La place des mots s'automatise par la répétition, pas par la règle."},

      {t:'ana', h:"« Ne » devient « n' » devant une voyelle",
       p:"Quand le verbe commence par a, e, i, o, u ou par un h.",
       mots:[["On dit","Je {n'}ai pas le papier."],["Aussi","Ce {n'}est pas nécessaire."],["Aussi","Il {n'}y a pas de cours lundi."],["On ne dit pas","« Je ne ai pas » — le e tombe toujours",true]],
       say:"Je n'ai pas le papier. Ce n'est pas nécessaire. Il n'y a pas de cours lundi.",
       note:"« Ce n'est pas » et « il n'y a pas » sont les deux formes les plus entendues au secrétariat. Les faire apprendre en bloc, sans les découper."},

      {t:'ana', h:"Après « pas », « un » et « du » deviennent « de »",
       p:"C'est le seul changement que la négation impose au reste de la phrase.",
       mots:[["On dit","Il n'y a pas {de} cours."],["Aussi","Je n'ai pas {d'}attestation."],["Aussi","Il n'y a pas {de} secrétaire aujourd'hui."],["On ne dit pas","« Il n'y a pas un cours »",true]],
       say:"Il n'y a pas de cours. Je n'ai pas d'attestation. Il n'y a pas de secrétaire aujourd'hui.",
       note:"Un seul contre-exemple à connaître : « ce n'est pas un avis », où l'on nie l'identité de la chose. Ne pas l'enseigner au niveau 2, seulement l'accepter."},

      {t:'labo', h:"Mets la phrase au négatif",
       p:"Choisis une phrase et une façon de la dire.",
       axes:[
         {id:'p', lbl:'Quelle phrase ?', opts:[
           ['a','je viens au cours'],
           ['b',"j'ai le papier"],
           ['c','il y a un cours lundi'],
           ['d','le bureau est ouvert']]},
         {id:'q', lbl:'Comment ?', opts:[['1','au positif'],['2','au négatif'],['3',"à l'oral rapide"]]}],
       out:{
         a1:{w:["Je viens au cours demain."], say:"Je viens au cours demain.", n:'la phrase de départ'},
         a2:{w:["Je ne viens pas au cours demain."], say:"Je ne viens pas au cours demain.", n:'ne et pas autour du verbe'},
         a3:{w:["Je viens pas demain."], say:"Je viens pas demain.", n:"à l'oral, le « ne » disparaît souvent"},
         b1:{w:["J'ai le papier."], say:"J'ai le papier.", n:'phrase positive, deux mots'},
         b2:{w:["Je n'ai pas le papier."], say:"Je n'ai pas le papier.", n:'ne devient n\' devant une voyelle'},
         b3:{w:["J'ai pas le papier."], say:"J'ai pas le papier.", n:'très courant, mais à ne pas écrire'},
         c1:{w:["Il y a un cours lundi."], say:"Il y a un cours lundi.", n:'un cours, avec « un »'},
         c2:{w:["Il n'y a pas de cours lundi."], say:"Il n'y a pas de cours lundi.", n:'« un » devient « de »'},
         c3:{w:["Y a pas de cours lundi."], say:"Y a pas de cours lundi.", n:'la forme entendue dans le couloir'},
         d1:{w:["Le bureau est ouvert."], say:"Le bureau est ouvert.", n:'phrase du matin'},
         d2:{w:["Le bureau n'est pas ouvert."], say:"Le bureau n'est pas ouvert.", n:'ou bien : le bureau est fermé'},
         d3:{w:["Le bureau est fermé."], say:"Le bureau est fermé.", n:'plus court, et plus employé'},
       },
       note:"Douze phrases. Faire remarquer la troisième colonne : à l'oral, le « ne » tombe presque toujours. Le dire une fois, puis exiger le « ne » à l'écrit."},

      {t:'ex', h:"À écouter et à répéter",
       p:"Six phrases négatives du secrétariat.",
       rows:[
         ["Je ne viens pas demain.","ne … pas"],
         ["Je ne comprends pas.","ne … pas"],
         ["Ce n'est pas nécessaire.","n' devant une voyelle"],
         ["Il n'y a pas de cours lundi.","un → de"],
         ["Le bureau n'est pas ouvert le midi.","n' devant une voyelle"],
         ["Je n'ai pas mon attestation.","n' + un → de"],
       ]},

      {t:'piege', h:"Trois pièges à connaître",
       rows:[
         ["mettre « pas » avant le verbe","le verbe reste au milieu",
          "« Je pas viens » n'existe pas. L'ordre est toujours : sujet, <b>ne</b>, verbe, <b>pas</b>. Un geste des deux mains autour du verbe aide beaucoup."],
         ["écrire « je viens pas » dans un message","à l'oral oui, à l'écrit non",
          "Tout le monde dit « je viens pas ». Mais dans un message au secrétariat, on écrit « je ne viens pas » : c'est ce qui est attendu d'un papier."],
         ["garder « un » ou « du » après la négation","ils deviennent « de »",
          "« Il n'y a pas de cours », « je n'ai pas d'attestation ». C'est automatique, et un élève qui l'oublie se fait comprendre quand même — mais l'oreille québécoise l'entend tout de suite."],
       ]},

      {t:'check', h:"Est-ce que c'est clair maintenant ?",
       p:"Quatre questions rapides.",
       qs:[
         {q:"On dit…", opts:["Je ne viens pas.","Je pas viens."], ok:0,
          fb:"Le verbe est entre « ne » et « pas »."},
         {q:"Devant « ai », on écrit…", opts:["n'","ne"], ok:0,
          fb:"« Je n'ai pas » : le e tombe devant une voyelle."},
         {q:"Il y a un cours → au négatif…", opts:["Il n'y a pas de cours.","Il n'y a pas un cours."], ok:0,
          fb:"Après la négation, « un » devient « de »."},
         {q:"Dans un message écrit, j'écris…", opts:["je ne viens pas","je viens pas"], ok:0,
          fb:"Le « ne » se garde à l'écrit, même s'il tombe à l'oral."},
       ]},
    ]
  },

  t2imper: {
    eye:'Mini-leçon', tit:"Les consignes et les règlements du centre",
    blocs:[
      {t:'texte', h:"Ce qui est écrit sur les portes",
       p:"Un avis, une affiche, une feuille de consignes : le centre parle à tout le monde à la fois, et il le fait avec un verbe seul, sans « vous » devant. <b>Écrivez votre nom. Lisez l'avis. Fermez la porte. Soyez à l'heure.</b> Quatre mots par ligne, et personne n'est nommé.",
       note:"Apporter en classe trois vraies affiches du centre. Les élèves reconnaissent la forme avant de connaître son nom, et ça suffit au niveau 2."},

      {t:'ana', h:"La consigne : un verbe, sans sujet",
       p:"C'est la forme du « vous », mais sans le mot « vous ».",
       mots:[["On écrit","{Écrivez} votre nom."],["Aussi","{Lisez} l'avis. · {Écoutez} bien."],["Aussi","{Fermez} la porte. · {Ouvrez} votre cahier."],["On n'écrit pas","« Vous écrivez votre nom » sur une affiche",true]],
       say:"Écrivez votre nom. Lisez l'avis. Écoutez bien. Fermez la porte. Ouvrez votre cahier.",
       note:"Faire remarquer le « -ez » final, qui s'entend « é ». C'est le même son que dans « allez » et « venez » : une seule terminaison à reconnaître."},

      {t:'ana', h:"« Soyez à l'heure » — le verbe être change de forme",
       p:"C'est la consigne la plus affichée d'un centre de formation.",
       mots:[["On écrit","{Soyez} à l'heure."],["Aussi","{Soyez} présent · {Soyez} au local à huit heures"],["Aussi","{Ayez} votre carte avec vous"],["On n'écrit pas","« Êtes à l'heure »",true]],
       say:"Soyez à l'heure. Soyez présent. Ayez votre carte avec vous.",
       note:"Deux formes irrégulières, et le programme ne demande que celles-là au niveau 2. Les faire apprendre comme deux mots, pas comme une conjugaison."},

      {t:'ana', h:"Ce qui est permis, ce qui est interdit",
       p:"Quatre mots suffisent à lire n'importe quel règlement.",
       mots:[["On dit","C'est {permis}."],["Aussi","C'est {interdit} · C'est {défendu}"],["Aussi","C'est {ouvert} · C'est {fermé}"],["Aussi","C'est {possible} · Ce n'est pas {possible}"],["On ne dit pas","« C'est pas permettre »",true]],
       say:"C'est permis. C'est interdit. C'est ouvert. C'est fermé. C'est possible.",
       note:"Ces mots reviennent partout, y compris hors du centre. Les faire chercher dans la rue en devoir : cinq affiches photographiées, cinq mots retrouvés."},

      {t:'ana', h:"« Je peux » et « je dois »",
       p:"Deux verbes qui disent ce qui est possible et ce qui est obligatoire.",
       mots:[["Ce qui est possible","Je {peux} venir au comptoir le matin."],["Ce qui est obligatoire","Je {dois} prévenir avant mon absence."],["La question","Est-ce que je {peux} avoir une attestation ?"],["Le contraire","Je ne {peux} pas venir lundi.",true]],
       say:"Je peux venir au comptoir le matin. Je dois prévenir avant mon absence. Est-ce que je peux avoir une attestation ?",
       note:"Après « je peux » et « je dois », le second verbe ne change jamais : venir, prévenir, écrire. C'est le seul point de grammaire à retenir ici."},

      {t:'labo', h:"Lis la consigne",
       p:"Choisis une situation et une façon de la dire.",
       axes:[
         {id:'p', lbl:'Quelle situation ?', opts:[
           ['a',"l'heure du cours"],
           ['b',"le papier à remplir"],
           ['c','le midi au bureau'],
           ['d',"manger dans le local"]]},
         {id:'q', lbl:'Comment ?', opts:[['1',"l'affiche"],['2','ce que ça veut dire'],['3','ce que je dis']]}],
       out:{
         a1:{w:["Soyez à l'heure."], say:"Soyez à l'heure.", n:'trois mots sur la porte'},
         a2:{w:["Le cours commence à 8 h 30."], say:"Le cours commence à huit heures et demie.", n:'ce que la consigne veut dire'},
         a3:{w:["Je dois arriver avant 8 h 30."], say:"Je dois arriver avant huit heures et demie.", n:'je le dis avec « je dois »'},
         b1:{w:["Écrivez votre nom et signez."], say:"Écrivez votre nom et signez.", n:'deux consignes en une ligne'},
         b2:{w:["Il faut écrire son nom sur la feuille."], say:"Il faut écrire son nom sur la feuille.", n:'la même chose, autrement'},
         b3:{w:["Est-ce que je dois signer ?"], say:"Est-ce que je dois signer ?", n:'on demande quand on doute'},
         c1:{w:["Fermé de 12 h à 13 h."], say:"Fermé de midi à treize heures.", n:'la ligne de l\'horaire'},
         c2:{w:["Le bureau n'est pas ouvert le midi."], say:"Le bureau n'est pas ouvert le midi.", n:'ce que ça veut dire'},
         c3:{w:["Je ne peux pas venir à midi."], say:"Je ne peux pas venir à midi.", n:'je le dis avec « je peux »'},
         d1:{w:["Interdit de manger dans le local."], say:"Interdit de manger dans le local.", n:'affiche très fréquente'},
         d2:{w:["Ce n'est pas permis."], say:"Ce n'est pas permis.", n:'la formule courte'},
         d3:{w:["Où est-ce que je peux manger ?"], say:"Où est-ce que je peux manger ?", n:'la bonne question à poser'},
       },
       note:"Douze phrases. Faire relier chaque affiche à ce qu'elle oblige vraiment : c'est là que la compréhension se joue, pas dans le verbe."},

      {t:'ex', h:"À écouter et à répéter",
       p:"Six consignes du centre.",
       rows:[
         ["Écrivez votre nom.","consigne, verbe seul"],
         ["Lisez l'avis sur la porte.","consigne, verbe seul"],
         ["Fermez la porte, s'il vous plaît.","consigne polie"],
         ["Soyez à l'heure.","forme irrégulière"],
         ["C'est interdit de manger ici.","le règlement"],
         ["Je dois prévenir avant mon absence.","devoir + verbe entier"],
       ]},

      {t:'piege', h:"Trois pièges à connaître",
       rows:[
         ["écrire « Vous écrivez votre nom » sur une affiche","une consigne n'a pas de sujet",
          "L'affiche parle à tout le monde. On écrit le verbe seul : « Écrivez votre nom ». Avec « vous » devant, ce n'est plus une consigne, c'est une phrase ordinaire."],
         ["confondre « je peux » et « je dois »","l'un est possible, l'autre est obligatoire",
          "« Je peux venir » veut dire que c'est permis. « Je dois venir » veut dire qu'il le faut. Au secrétariat, la différence change complètement la réponse."],
         ["changer le deuxième verbe","après peux et dois, le verbe reste entier",
          "On dit « je dois prévenir », jamais « je dois je préviens ». Le second verbe garde sa forme de dictionnaire : venir, écrire, signer, prévenir."],
       ]},

      {t:'check', h:"Est-ce que c'est clair maintenant ?",
       p:"Quatre questions rapides.",
       qs:[
         {q:"Sur une affiche, on écrit…", opts:["Écrivez votre nom.","Vous écrivez votre nom."], ok:0,
          fb:"Une consigne n'a pas de sujet devant."},
         {q:"« Soyez à l'heure » vient du verbe…", opts:["être","avoir"], ok:0,
          fb:"C'est la forme irrégulière du verbe être."},
         {q:"« Je dois prévenir » veut dire…", opts:["c'est obligatoire","c'est permis"], ok:0,
          fb:"« Je peux », c'est permis. « Je dois », c'est obligatoire."},
         {q:"On dit…", opts:["Je peux venir.","Je peux je viens."], ok:0,
          fb:"Après « je peux », le verbe reste entier."},
       ]},
    ]
  },
};
