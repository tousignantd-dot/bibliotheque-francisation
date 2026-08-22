const PLUS = {
  prNombres: {
    eye:'Mini-leçon', tit:"Deux ou douze ? Les nombres qui se ressemblent",
    blocs:[
      {t:'texte', h:"Quatre paires font presque toutes les erreurs",
       p:"En classe, les nombres servent tout le temps : la page, l'heure, le local, le nombre de feuilles. Quatre paires se ressemblent beaucoup à l'oreille : <b>deux</b> et <b>douze</b>, <b>trois</b> et <b>treize</b>, <b>quatre</b> et <b>quatorze</b>, <b>six</b> et <b>seize</b>. Le début est presque pareil ; c'est la <b>fin</b> qui change.",
       note:"Se tromper de dix, ce n'est pas grave en classe. À la clinique ou à la banque, ça l'est. C'est pour ça qu'on l'exerce ici."},

      {t:'ana', h:"Le petit nombre est court",
       p:"Une seule partie, et c'est fini.",
       mots:[['On dit','{deux}'],['On dit','{trois}'],['On dit','{six}',true]],
       say:"Deux. Trois. Six.",
       note:"Le mot s'arrête vite. Si vous entendez un mot court, c'est un nombre avant dix."},

      {t:'ana', h:"Le grand nombre continue",
       p:"Il y a quelque chose après.",
       mots:[['On dit','{douze}'],['On dit','{treize}'],['On dit','{seize}',true]],
       say:"Douze. Treize. Seize.",
       note:"Écoutez la fin : « ze ». Deux, trois et six n'ont pas ce « ze »."},

      {t:'ana', h:"Quatre et quatorze",
       p:"Celle-là s'entend mieux que les autres.",
       mots:[['Le petit','{quatre}'],['Le grand','{quatorze}'],['Ce qui change','la partie du milieu',true]],
       say:"Quatre. Quatorze.",
       note:"« Quatorze » est plus long à dire. Comptez dans votre tête : le plus long est le plus grand."},

      {t:'labo', h:"Écoutez les huit nombres",
       p:"Choisissez un nombre.",
       axes:[{id:'n', lbl:'Quel nombre ?', opts:[
         ['a','2 et 12'],
         ['b','3 et 13'],
         ['c','4 et 14'],
         ['d','6 et 16']]}],
       out:{
         a:{w:['deux — douze'], say:"Deux. Douze.", n:'le grand finit par « ze »'},
         b:{w:['trois — treize'], say:"Trois. Treize.", n:'même début, fin différente'},
         c:{w:['quatre — quatorze'], say:"Quatre. Quatorze.", n:'le grand est plus long'},
         d:{w:['six — seize'], say:"Six. Seize.", n:'la paire la plus difficile'},
       },
       note:"Écoutez chaque paire trois fois, puis dites-la à voix haute."},

      {t:'ex', h:"On écoute, on répète",
       p:"Les nombres dans une phrase de classe.",
       rows:[
         ["Ouvrez à la page deux.","le petit nombre"],
         ["Ouvrez à la page douze.","le grand nombre"],
         ["Il y a treize personnes dans la classe.","treize, pas trois"],
         ["Le cours est au local quatorze.","quatorze, pas quatre"],
         ["La pause est courte : quinze minutes.","un grand nombre aussi"],
         ["Prenez seize feuilles.","seize, pas six"],
       ]},

      {t:'piege', h:"Trois erreurs qui reviennent",
       rows:[
         ["entendre le début seulement","« deu… » et on écrit 2",
          "Le début de « deux » et de « douze » se ressemble. Attendez la fin du mot avant d'écrire."],
         ["ne pas oser faire répéter","on ouvre à la mauvaise page",
          "Un mot suffit : « Pardon ? » L'enseignante répétera. Toute la classe le fait."],
         ["croire que c'est votre oreille","« je n'entends pas bien le français »",
          "Ce n'est pas l'oreille : ces mots se ressemblent vraiment. Les gens nés ici font répéter aussi, au téléphone."],
       ]},

      {t:'check', h:"Voyons si c'est clair",
       p:"Quatre petites questions.",
       qs:[
         {q:"« Seize » est…", opts:["plus grand que dix","plus petit que dix"], ok:0,
          fb:"Seize, c'est 16."},
         {q:"Le mot le plus long des deux est…", opts:["le petit nombre","le grand nombre"], ok:1,
          fb:"Quatre / quatorze : le grand est plus long."},
         {q:"Pour être sûr, il faut écouter…", opts:["le début du mot","la fin du mot"], ok:1,
          fb:"C'est la fin qui change : trois / treize."},
         {q:"Si vous n'êtes pas sûr, vous dites…", opts:["rien","Pardon ?"], ok:1,
          fb:"« Pardon ? » est une phrase de la langue, pas une faute."},
       ]},
    ]
  },

  prNom: {
    eye:'Mini-leçon', tit:"Un livre, une chaise — le petit mot devant",
    blocs:[
      {t:'texte', h:"En français, le nom vient rarement seul",
       p:"On ne dit pas « livre » ni « chaise » tout seul : on dit <b>un</b> livre, <b>une</b> chaise. Ce petit mot devant s'appelle un article. Il dit deux choses à la fois : qu'il y en a un, et de quel groupe le nom fait partie — le groupe des « un » ou le groupe des « une ».",
       note:"Beaucoup de langues n'ont pas ce petit mot. Si votre langue s'en passe, c'est une nouveauté à installer, pas une difficulté personnelle."},

      {t:'ana', h:"Le groupe des « un »",
       p:"On dit un devant ces noms.",
       mots:[['On dit','{un} livre'],['On dit','{un} stylo'],['On dit','{un} sac',true]],
       say:"Un livre. Un stylo. Un sac.",
       note:"On appelle ces noms « masculins ». Le mot est du vocabulaire de grammaire ; ce qui compte, c'est de retenir « un »."},

      {t:'ana', h:"Le groupe des « une »",
       p:"On dit une devant ces noms.",
       mots:[['On dit','{une} chaise'],['On dit','{une} porte'],['On dit','{une} horloge',true]],
       say:"Une chaise. Une porte. Une horloge.",
       note:"On les appelle « féminins ». Une chaise n'a rien de féminin : c'est le mot qui est ainsi, pas l'objet."},

      {t:'ana', h:"Retenir les deux ensemble",
       p:"Le mot et son article, jamais l'un sans l'autre.",
       mots:[['À éviter','apprendre « porte »'],['À faire','apprendre « {une porte} »'],['Sur votre feuille','écrivez toujours les deux',true]],
       say:"Une porte. Un livre. Une chaise. Un stylo.",
       note:"C'est le seul moyen fiable. Personne ne devine l'article ; tout le monde l'apprend avec le mot."},

      {t:'labo', h:"Un ou une ?",
       p:"Choisissez un objet de la classe.",
       axes:[{id:'o', lbl:'Quel objet ?', opts:[
         ['a','livre'],
         ['b','chaise'],
         ['c','stylo'],
         ['d','porte'],
         ['e','horloge'],
         ['f','sac']]}],
       out:{
         a:{w:['un livre'], say:"Un livre.", n:'groupe des « un »'},
         b:{w:['une chaise'], say:"Une chaise.", n:'groupe des « une »'},
         c:{w:['un stylo'], say:"Un stylo.", n:'groupe des « un »'},
         d:{w:['une porte'], say:"Une porte.", n:'groupe des « une »'},
         e:{w:['une horloge'], say:"Une horloge.", n:'devant une voyelle, on entend « un-ne »'},
         f:{w:['un sac'], say:"Un sac.", n:'groupe des « un »'},
       },
       note:"Dites chaque paire à voix haute. Le petit mot et le nom ne se séparent pas."},

      {t:'ex', h:"On écoute, on répète",
       p:"Six objets, avec leur petit mot.",
       rows:[
         ["un livre","sur la table"],
         ["un stylo","dans le sac"],
         ["une chaise","devant le pupitre"],
         ["une porte","au fond de la classe"],
         ["une horloge","au mur"],
         ["un sac","sous la chaise"],
       ]},

      {t:'piege', h:"Trois erreurs qui reviennent",
       rows:[
         ["deviner d'après l'objet","« une chaise, parce que c'est doux »",
          "Rien dans l'objet ne dit l'article. Un tapis est « un », une table est « une » : il n'y a pas de règle à trouver."],
         ["dire le nom tout seul","« donne stylo »",
          "On comprend, mais ça s'entend tout de suite. Le petit mot coûte une seconde et change beaucoup."],
         ["oublier l'article devant une voyelle","« un horloge »",
          "Devant « horloge », le son se colle et l'article s'entend mal. C'est <b>une</b> horloge — écoutez le petit « n » à la fin de « une »."],
       ]},

      {t:'check', h:"Voyons si c'est clair",
       p:"Quatre petites questions.",
       qs:[
         {q:"On dit…", opts:["un chaise","une chaise"], ok:1,
          fb:"Une chaise."},
         {q:"On dit…", opts:["un livre","une livre"], ok:0,
          fb:"Un livre."},
         {q:"L'article se devine d'après l'objet ?", opts:["oui","non"], ok:1,
          fb:"Non : il s'apprend avec le mot."},
         {q:"La bonne façon d'apprendre un mot nouveau…", opts:["le mot seul","le mot avec son article"], ok:1,
          fb:"Toujours les deux ensemble : une porte."},
       ]},
    ]
  },

  t1imper: {
    eye:'Mini-leçon', tit:"La consigne : un verbe, et on fait",
    blocs:[
      {t:'texte', h:"Deux mots, et il faut bouger",
       p:"Une consigne de classe est très courte : <b>Ouvrez le livre.</b> <b>Regardez le tableau.</b> Elle ne commence ni par « je » ni par « vous » : elle commence tout de suite par le <b>verbe</b>. Le premier mot est donc le mot le plus important — c'est lui qui dit quoi faire.",
       note:"Au niveau 1, comprendre une consigne suffit. Personne ne vous demande de la donner : c'est l'enseignante qui la donne."},

      {t:'ana', h:"Les quatre verbes du matin",
       p:"Ils reviennent tous les jours.",
       mots:[['Les oreilles','{Écoutez}'],['Les yeux','{Regardez}'],['Les mains','{Ouvrez} / {Fermez}',true]],
       say:"Écoutez. Regardez. Ouvrez. Fermez.",
       note:"Trois d'entre eux se font avec le corps : les oreilles, les yeux, les mains. C'est un bon moyen de les retenir."},

      {t:'ana', h:"Toutes finissent par le même son",
       p:"Le son « é » à la fin.",
       mots:[['On entend','écout{ez}'],['On entend','regard{ez}'],['On entend','ferm{ez}',true]],
       say:"Écoutez. Regardez. Fermez.",
       note:"Ce son « é » à la fin veut dire : à vous de le faire, maintenant. Quand vous l'entendez au début d'une phrase, préparez-vous à bouger."},

      {t:'ana', h:"Après le verbe, l'objet",
       p:"Le verbe, puis la chose.",
       mots:[['On dit','Ouvrez {le livre}.'],['On dit','Fermez {la porte}.'],['On ne dit pas','le livre ouvrez',true]],
       say:"Ouvrez le livre. Fermez la porte.",
       note:"L'ordre ne change pas : d'abord ce qu'on fait, ensuite sur quoi on le fait."},

      {t:'labo', h:"Écoutez les consignes",
       p:"Choisissez un verbe et un objet.",
       axes:[
         {id:'v', lbl:'Quel verbe ?', opts:[['a','Ouvrez'],['b','Fermez'],['c','Regardez'],['d','Écoutez']]},
         {id:'o', lbl:'Quoi ?', opts:[['1','le livre'],['2','la porte'],['3','le tableau']]}],
       out:{
         a1:{w:['Ouvrez le livre.'], say:"Ouvrez le livre.", n:'la consigne la plus fréquente'},
         a2:{w:['Ouvrez la porte.'], say:"Ouvrez la porte.", n:'on se lève et on ouvre'},
         a3:{w:['Ouvrez votre livre à la page du tableau.'], say:"Ouvrez votre livre à la page du tableau.", n:'la page est écrite au tableau'},
         b1:{w:['Fermez le livre.'], say:"Fermez le livre.", n:'souvent avant un exercice d\'écoute'},
         b2:{w:['Fermez la porte.'], say:"Fermez la porte.", n:'quand il y a du bruit dans le couloir'},
         b3:{w:['Ne regardez pas le tableau.'], say:"Ne regardez pas le tableau.", n:'la consigne au négatif : ne… pas'},
         c1:{w:['Regardez le livre.'], say:"Regardez le livre.", n:'les yeux sur la page'},
         c2:{w:['Regardez la porte.'], say:"Regardez la porte.", n:'on montre où c\'est'},
         c3:{w:['Regardez le tableau.'], say:"Regardez le tableau.", n:'les yeux vers le devant'},
         d1:{w:['Écoutez et suivez dans le livre.'], say:"Écoutez et suivez dans le livre.", n:'deux consignes ensemble'},
         d2:{w:['Écoutez : quelqu\'un frappe à la porte.'], say:"Écoutez : quelqu'un frappe à la porte.", n:'écouter, sans rien faire d\'autre'},
         d3:{w:['Écoutez, puis regardez le tableau.'], say:"Écoutez, puis regardez le tableau.", n:'l\'une après l\'autre'},
       },
       note:"Douze consignes. Faites le geste en même temps que vous écoutez : le corps retient mieux que la tête."},

      {t:'ex', h:"On écoute, on répète",
       p:"Six consignes du premier jour.",
       rows:[
         ["Écoutez bien.","les oreilles"],
         ["Regardez le tableau.","les yeux"],
         ["Ouvrez le livre.","les mains"],
         ["Fermez le livre.","les mains"],
         ["Prenez un stylo.","les mains"],
         ["Répétez après moi.","la voix"],
       ]},

      {t:'piege', h:"Trois erreurs qui reviennent",
       rows:[
         ["attendre la fin de la phrase","on écoute tout, puis on oublie le début",
          "Le mot important est le <b>premier</b>. Dès que vous l'avez, vous savez quoi faire."],
         ["regarder le voisin","on copie le geste, sans comprendre le mot",
          "C'est utile le premier jour, et c'est permis. Mais essayez d'attraper le verbe aussi : c'est lui qui sert demain."],
         ["croire qu'on doit répondre","on cherche une phrase à dire",
          "Une consigne ne demande pas de réponse. Elle demande un geste. Si vous n'avez pas compris, un seul mot suffit : « Pardon ? »"],
       ]},

      {t:'check', h:"Voyons si c'est clair",
       p:"Quatre petites questions.",
       qs:[
         {q:"Le premier mot d'une consigne, c'est…", opts:["le verbe","le nom"], ok:0,
          fb:"Ouvrez le livre : le verbe d'abord."},
         {q:"« Fermez » veut dire…", opts:["le contraire d'ouvrir","regarder"], ok:0,
          fb:"On ferme le livre, la porte, le sac."},
         {q:"Une consigne demande…", opts:["une phrase","un geste"], ok:1,
          fb:"On fait quelque chose, on ne répond pas."},
         {q:"Si vous n'avez pas compris…", opts:["vous ne dites rien","vous dites « Pardon ? »"], ok:1,
          fb:"L'enseignante répétera plus lentement."},
       ]},
    ]
  },

  t1ou: {
    eye:'Mini-leçon', tit:"Sur, dans, sous — dire où est la chose",
    blocs:[
      {t:'texte', h:"Trois mots, trois places",
       p:"Pour dire où est un objet, trois petits mots suffisent presque toujours en classe : <b>sur</b> (dessus), <b>dans</b> (à l'intérieur), <b>sous</b> (en dessous). Ils se placent avant le nom : sur la table, dans le sac, sous la chaise.",
       note:"« Sur » et « sous » se ressemblent beaucoup à l'oreille. C'est la seule vraie difficulté des trois."},

      {t:'ana', h:"sur — dessus",
       p:"L'objet touche le dessus.",
       mots:[['On dit','Le livre est {sur} la table.'],['On dit','L\'horloge est {sur} le mur.'],['On voit l\'objet','oui',true]],
       say:"Le livre est sur la table.",
       note:"On dit « sur le mur » pour ce qui est accroché : une horloge, une affiche, un calendrier."},

      {t:'ana', h:"dans — à l'intérieur",
       p:"L'objet est caché à l'intérieur d'un autre.",
       mots:[['On dit','Le stylo est {dans} le sac.'],['On dit','Les feuilles sont {dans} le livre.'],['On voit l\'objet','non',true]],
       say:"Le stylo est dans le sac.",
       note:"Si vous devez ouvrir quelque chose pour le prendre, c'est « dans »."},

      {t:'ana', h:"sous — en dessous",
       p:"L'objet est plus bas, caché par le dessus.",
       mots:[['On dit','Le sac est {sous} la chaise.'],['On dit','Le stylo est tombé {sous} la table.'],['Se ressemble à','sur',true]],
       say:"Le sac est sous la chaise.",
       note:"« Sur » et « sous » : écoutez la voyelle du milieu. Dans le doute, regardez en haut et en bas — l'objet vous le dira."},

      {t:'labo', h:"Où est l'objet ?",
       p:"Choisissez une place et un objet.",
       axes:[
         {id:'p', lbl:'Où ?', opts:[['a','sur'],['b','dans'],['c','sous']]},
         {id:'o', lbl:'Quel objet ?', opts:[['1','le livre'],['2','le stylo'],['3','le sac']]}],
       out:{
         a1:{w:['Le livre est sur la table.'], say:"Le livre est sur la table.", n:'on le voit tout de suite'},
         a2:{w:['Le stylo est sur le livre.'], say:"Le stylo est sur le livre.", n:'posé dessus'},
         a3:{w:['Le sac est sur la chaise.'], say:"Le sac est sur la chaise.", n:'la place la plus fréquente'},
         b1:{w:['Le livre est dans le sac.'], say:"Le livre est dans le sac.", n:'il faut ouvrir le sac'},
         b2:{w:['Le stylo est dans le sac.'], say:"Le stylo est dans le sac.", n:'caché à l\'intérieur'},
         b3:{w:['Le sac est dans le casier.'], say:"Le sac est dans le casier.", n:'à l\'intérieur, fermé'},
         c1:{w:['Le livre est sous la feuille.'], say:"Le livre est sous la feuille.", n:'quelque chose est par-dessus'},
         c2:{w:['Le stylo est sous la chaise.'], say:"Le stylo est sous la chaise.", n:'il est tombé'},
         c3:{w:['Le sac est sous le pupitre.'], say:"Le sac est sous le pupitre.", n:'la place de tout le monde en classe'},
       },
       note:"Neuf phrases. Regardez autour de vous et dites où sont vos affaires."},

      {t:'ex', h:"On écoute, on répète",
       p:"Six phrases de la classe.",
       rows:[
         ["Le livre est sur la table.","dessus"],
         ["Le stylo est dans le sac.","à l'intérieur"],
         ["Le sac est sous la chaise.","en dessous"],
         ["L'horloge est sur le mur.","accrochée"],
         ["Les feuilles sont dans le livre.","entre les pages"],
         ["Mon stylo est tombé sous le pupitre.","plus bas"],
       ]},

      {t:'piege', h:"Trois erreurs qui reviennent",
       rows:[
         ["confondre sur et sous","« le sac est sur la chaise » alors qu'il est dessous",
          "Ces deux mots ne diffèrent que par une voyelle. Faites le geste de la main en parlant : en haut pour « sur », en bas pour « sous »."],
         ["mettre le petit mot après","« la table sur »",
          "En français, le petit mot passe toujours devant le nom : sur la table, dans le sac, sous la chaise."],
         ["dire « dans la table »","pour un livre posé dessus",
          "« Dans » veut dire à l'intérieur. Un livre posé sur une table est <b>sur</b> la table ; un livre rangé dans un tiroir est <b>dans</b> le tiroir."],
       ]},

      {t:'check', h:"Voyons si c'est clair",
       p:"Quatre petites questions.",
       qs:[
         {q:"Le stylo est à l'intérieur du sac. On dit…", opts:["sur le sac","dans le sac"], ok:1,
          fb:"Dans le sac : il est caché à l'intérieur."},
         {q:"Le sac est par terre, la chaise est au-dessus. On dit…", opts:["sous la chaise","sur la chaise"], ok:0,
          fb:"Sous la chaise."},
         {q:"Sur, dans et sous se mettent…", opts:["avant le nom","après le nom"], ok:0,
          fb:"Sur la table, jamais « la table sur »."},
         {q:"Une horloge accrochée au mur est…", opts:["sur le mur","dans le mur"], ok:0,
          fb:"Sur le mur."},
       ]},
    ]
  },

  t2heure: {
    eye:'Mini-leçon', tit:"Lire l'heure de son cours",
    blocs:[
      {t:'texte', h:"Le nombre d'abord, le mot heure ensuite",
       p:"En français, on dit le nombre, puis le mot : <b>huit heures</b>, <b>dix heures</b>, <b>deux heures</b>. Après une heure, le mot prend un s à l'écrit — une heure, deux heures — mais il se prononce pareil. Pour un cours ou un rendez-vous, on ajoute le petit mot <b>à</b> devant : le cours commence <b>à</b> huit heures et demie.",
       note:"L'heure est ce qu'on vous demandera le plus souvent au centre : l'heure du cours, l'heure de la pause, l'heure du rendez-vous."},

      {t:'ana', h:"L'heure juste",
       p:"Rien après le nombre.",
       mots:[['8 h','huit {heures}'],['10 h','dix {heures}'],['1 h','une {heure}',true]],
       say:"Huit heures. Dix heures. Une heure.",
       note:"À une heure seulement, on dit « une heure », au singulier. Partout ailleurs, « heures »."},

      {t:'ana', h:"La demie et le quart",
       p:"Trente minutes, quinze minutes.",
       mots:[['8 h 30','huit heures {et demie}'],['8 h 15','huit heures {et quart}'],['7 h 45','huit heures {moins quart}',true]],
       say:"Huit heures et demie. Huit heures et quart. Huit heures moins quart.",
       note:"« Moins quart » veut dire avant l'heure : huit heures moins quart, c'est 7 h 45. C'est le plus difficile des trois."},

      {t:'ana', h:"Midi et minuit",
       p:"Deux heures qui ont un nom.",
       mots:[['12 h le jour','{midi}'],['12 h la nuit','{minuit}'],['On ne dit pas','douze heures',true]],
       say:"Midi. Minuit.",
       note:"Sur un horaire, c'est écrit « 12 h ». À l'oral, on dit « midi ». Ce n'est pas une faute d'écrire 12 h."},

      {t:'labo', h:"Écoutez ces heures",
       p:"Choisissez une heure.",
       axes:[{id:'h', lbl:'Quelle heure ?', opts:[
         ['a','8 h 30'],
         ['b','10 h'],
         ['c','10 h 15'],
         ['d','12 h'],
         ['e','15 h']]}],
       out:{
         a:{w:['huit heures et demie'], say:"Huit heures et demie.", n:'le début du cours de Bopha'},
         b:{w:['dix heures'], say:"Dix heures.", n:'l\'heure de la pause'},
         c:{w:['dix heures et quart'], say:"Dix heures et quart.", n:'la fin de la pause'},
         d:{w:['midi'], say:"Midi.", n:'la fin du cours'},
         e:{w:['trois heures'], say:"Trois heures.", n:'après midi, on recommence à une heure'},
       },
       note:"Cinq heures de la journée d'un élève. Dites-les à voix haute en regardant l'horloge de votre classe."},

      {t:'ex', h:"On écoute, on répète",
       p:"L'horaire du groupe en six phrases.",
       rows:[
         ["Le cours commence à huit heures et demie.","le matin"],
         ["La pause est à dix heures.","quinze minutes"],
         ["Le cours finit à midi.","pas « douze heures »"],
         ["Il est neuf heures et quart.","8 h 15 est « et quart » aussi"],
         ["Le rendez-vous est à deux heures.","l'après-midi"],
         ["Le centre ferme à quatre heures.","la fin de la journée"],
       ]},

      {t:'piege', h:"Trois erreurs qui reviennent",
       rows:[
         ["dire « douze heures »","pour 12 h",
          "À l'oral, on dit <b>midi</b>. « Douze heures » se comprend, mais personne ne le dit ici."],
         ["oublier le petit mot à","« le cours commence huit heures »",
          "Pour un moment, on met <b>à</b> : à huit heures, à midi, à dix heures."],
         ["confondre et quart et moins quart","8 h 15 et 7 h 45",
          "« Et quart » vient après l'heure ; « moins quart » vient avant. Dans le doute, dites le chiffre : huit heures quinze."],
       ]},

      {t:'check', h:"Voyons si c'est clair",
       p:"Quatre petites questions.",
       qs:[
         {q:"12 h se dit…", opts:["midi","douze heures"], ok:0,
          fb:"Midi."},
         {q:"8 h 30 se dit…", opts:["huit heures et quart","huit heures et demie"], ok:1,
          fb:"Et demie : trente minutes."},
         {q:"Devant l'heure d'un cours, on met…", opts:["à","dans"], ok:0,
          fb:"Le cours commence à midi."},
         {q:"« Huit heures moins quart », c'est…", opts:["7 h 45","8 h 15"], ok:0,
          fb:"Moins quart : avant l'heure."},
       ]},
    ]
  },

  t2jours: {
    eye:'Mini-leçon', tit:"Les jours de la semaine et l'horaire du groupe",
    blocs:[
      {t:'texte', h:"Sept jours, et quatre jours de cours",
       p:"La semaine a sept jours : <b>lundi, mardi, mercredi, jeudi, vendredi, samedi, dimanche</b>. Toujours dans cet ordre, et toujours en minuscules à l'écrit. Le groupe de Bopha vient quatre jours : de lundi à jeudi. Vendredi, samedi et dimanche, il n'y a pas de cours.",
       note:"Ici, « la fin de semaine » veut dire samedi et dimanche. En France, on dit « le week-end » ; au Québec, on dit « la fin de semaine »."},

      {t:'ana', h:"Les quatre jours de cours",
       p:"Du début de la semaine à jeudi.",
       mots:[['1','{lundi}'],['2','{mardi}'],['3 et 4','{mercredi}, {jeudi}',true]],
       say:"Lundi, mardi, mercredi, jeudi.",
       note:"Mardi et mercredi se ressemblent au début. Écoutez la suite du mot."},

      {t:'ana', h:"Les jours sans cours",
       p:"Le reste de la semaine.",
       mots:[['Pas de cours','{vendredi}'],['La fin de semaine','{samedi}, {dimanche}'],['Le centre','fermé samedi et dimanche',true]],
       say:"Vendredi. Samedi. Dimanche.",
       note:"Le vendredi, le centre est ouvert, mais le groupe de Bopha ne vient pas. Ce n'est pas la même chose qu'un congé."},

      {t:'ana', h:"Lundi ou le lundi ?",
       p:"Un petit mot qui change le sens.",
       mots:[['Une seule fois','Je viens {lundi}.'],['Toutes les semaines','Je viens {le lundi}.'],['Sur l\'horaire','le lundi, toutes les semaines',true]],
       say:"Je viens lundi. Je viens le lundi.",
       note:"« Lundi » tout seul veut dire le prochain lundi. « Le lundi » veut dire chaque lundi. L'horaire du centre parle toujours de chaque semaine."},

      {t:'labo', h:"L'horaire de la semaine",
       p:"Choisissez un jour.",
       axes:[{id:'j', lbl:'Quel jour ?', opts:[
         ['a','lundi'],
         ['b','mercredi'],
         ['c','vendredi'],
         ['d','samedi']]}],
       out:{
         a:{w:['Lundi : cours de 8 h 30 à midi.'], say:"Lundi : cours de huit heures et demie à midi.", n:'le premier jour de la semaine'},
         b:{w:['Mercredi : cours de 8 h 30 à midi.'], say:"Mercredi : cours de huit heures et demie à midi.", n:'le milieu de la semaine'},
         c:{w:['Vendredi : pas de cours.'], say:"Vendredi : pas de cours.", n:'le centre est ouvert, le groupe ne vient pas'},
         d:{w:['Samedi : le centre est fermé.'], say:"Samedi : le centre est fermé.", n:'la fin de semaine'},
       },
       note:"Regardez l'horaire affiché près de la porte de votre classe et dites vos propres jours."},

      {t:'ex', h:"On écoute, on répète",
       p:"L'horaire du groupe en six phrases.",
       rows:[
         ["Le cours est de lundi à jeudi.","quatre jours"],
         ["Vendredi, il n'y a pas de cours.","le jour libre"],
         ["Le centre est fermé la fin de semaine.","samedi et dimanche"],
         ["Le lundi, le cours commence à huit heures et demie.","toutes les semaines"],
         ["L'horaire est affiché près de la porte.","où le lire"],
         ["À lundi !","ce qu'on dit le jeudi en partant"],
       ]},

      {t:'piege', h:"Trois erreurs qui reviennent",
       rows:[
         ["écrire les jours avec une majuscule","« Lundi »",
          "En français, les jours s'écrivent en minuscules au milieu d'une phrase : « je viens lundi »."],
         ["confondre mardi et mercredi","les deux commencent par « m »",
          "Écoutez après le « m » : mar-di est court, mer-cre-di est long. Comptez les parties du mot."],
         ["croire que « pas de cours » veut dire « congé »","le centre est fermé",
          "Vendredi, le centre est ouvert : le secrétariat répond, on peut venir chercher un papier. C'est le <b>groupe</b> qui n'a pas de cours."],
       ]},

      {t:'check', h:"Voyons si c'est clair",
       p:"Quatre petites questions.",
       qs:[
         {q:"Le premier jour de la semaine est…", opts:["lundi","dimanche"], ok:0,
          fb:"Ici, la semaine commence le lundi."},
         {q:"Le groupe de Bopha vient…", opts:["quatre jours","cinq jours"], ok:0,
          fb:"De lundi à jeudi."},
         {q:"« Le lundi » veut dire…", opts:["chaque lundi","le prochain lundi"], ok:0,
          fb:"Avec « le », c'est toutes les semaines."},
         {q:"La fin de semaine, c'est…", opts:["vendredi et samedi","samedi et dimanche"], ok:1,
          fb:"Samedi et dimanche."},
       ]},
    ]
  },
};
