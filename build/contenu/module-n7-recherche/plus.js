const PLUS = {

  prE: {
    eye:'Mini-leçon', tit:"Le « e » qu'on entend et celui qui disparaît",
    blocs:[
      {t:'texte', h:"Le son le plus discret du français",
       p:"Il y a dans le français un petit son qui n'a pas de nom dans la vie courante : le « e » de <i>demander</i>, de <i>peser</i>, de <i>seulement</i>. Parfois on l'entend, parfois il s'efface entièrement. Ce ne sont pas deux façons de parler, l'une soignée et l'autre relâchée : ce sont deux prononciations également correctes, et c'est la place du « e » dans le mot qui décide.",
       note:"On l'appelle le <b>e caduc</b> — « caduc » veut dire « qui tombe ». Son symbole est <b>[ə]</b>."},

      {t:'texte', h:"Pourquoi ça compte dans une recherche d'emploi",
       p:"Vous allez téléphoner à des employeurs et écouter des messages enregistrés. Si vous cherchez « seu-le-ment » en trois morceaux, vous ne le trouverez jamais : la personne dit <i>seul'ment</i>, en deux. Le mot que vous connaissez très bien devient méconnaissable, et vous croyez avoir manqué du vocabulaire alors que vous avez seulement manqué un « e » tombé.",
       note:"C'est la première cause d'incompréhension à l'oral chez les adultes qui lisent pourtant très bien."},

      {t:'ana', h:"Cas 1 — Le « e » se maintient au début du mot après p, b, t, d, k, g",
       p:"Quand le « e » est dans la <b>première syllabe</b> et que le mot commence par une de ces consonnes qui ferment complètement la bouche, on le garde.",
       mots:[['On écrit','d{e}mander · p{e}ser · d{e}bout · un d{e}vis'],['On entend','[ə] bien présent',true],['Le repère','la bouche se ferme d\'abord, puis le « e » sort']],
       say:"demander, peser, debout, un devis",
       note:"Ces consonnes s'appellent des <b>occlusives</b> : l'air est bloqué un instant, puis relâché."},

      {t:'ana', h:"Cas 2 — Le « e » se maintient devant les sons [rj] et [lj]",
       p:"Devant un « ri » ou un « li » suivi d'une voyelle, le « e » reste, sinon le mot devient impossible à prononcer.",
       mots:[['On écrit','un at{e}lier · un hôt{e}lier · un ouvri{e}r spécialisé'],['On entend','[ə] bien présent',true],['Essayez sans','« atlier » : la langue butte']],
       say:"un atelier, un hôtelier",
       note:"C'est un cas rare, mais il ne souffre aucune exception."},

      {t:'ana', h:"Cas 3 — Le « e » se maintient aussi quand deux consonnes le précèdent",
       p:"Quand il faut deux consonnes pour arriver au « e », il reste : sans lui, trois consonnes se suivraient.",
       mots:[['On écrit','le pr{e}mier · autr{e}ment · appart{e}ment'],['On entend','[ə] bien présent',true],['La règle','deux consonnes devant → il tient']],
       say:"le premier, autrement",
       note:"C'est ce cas qui explique pourquoi <i>justement</i> garde son « e » alors que <i>seulement</i> le perd."},

      {t:'ana', h:"Cas 4 — Ailleurs, le « e » tombe presque toujours",
       p:"Au milieu du mot, quand une seule consonne le précède, il s'efface dans la conversation normale.",
       mots:[['On écrit','rapid{e}ment · seul{e}ment · la s{e}maine · la r{e}lève'],['On entend','[ʁapidmɑ̃] · [sœlmɑ̃] · [lasmɛn]',true],['La règle','une seule consonne devant → il tombe']],
       say:"rapidement, seulement, la semaine, la relève",
       note:"Un médecin devient [medsɛ̃] et une boulangerie [bulɑ̃ʒʁi] : c'est la même chose."},

      {t:'labo', h:"Écoutez la différence",
       p:"Choisissez un cas et un exemple.",
       axes:[
         {id:'c', lbl:'Quel cas ?', opts:[['a','début de mot'],['b','devant ri / li'],['c','deux consonnes'],['d','milieu de mot']]},
         {id:'n', lbl:'Quel exemple ?', opts:[['1','le premier'],['2','le second']]}],
       out:{
         a1:{w:["demander"], say:"demander", n:'« d » est une occlusive : on entend « de-man-der »'},
         a2:{w:["peser"], say:"peser", n:'« p » aussi : on entend « pe-ser »'},
         b1:{w:["un atelier"], say:"un atelier", n:'devant [lj], le « e » ne tombe jamais'},
         b2:{w:["un hôtelier"], say:"un hôtelier", n:'même cas, même prononciation'},
         c1:{w:["le premier"], say:"le premier", n:'« pr » : deux consonnes, le « e » tient'},
         c2:{w:["autrement"], say:"autrement", n:'« tr » : deux consonnes, le « e » tient'},
         d1:{w:["seulement"], say:"seulement", n:'une seule consonne : [sœlmɑ̃]'},
         d2:{w:["la relève"], say:"la relève", n:'on entend « la r\'lève »'},
       },
       note:"Écoutez deux fois, puis répétez à voix haute avant de passer au suivant."},

      {t:'ex', h:"Six mots du module, à écouter et à répéter",
       p:"À gauche, ce qui est écrit. À droite, ce qui se dit.",
       rows:[
         ["demander","« de-man-der » — le « e » se dit"],
         ["peser","« pe-ser » — le « e » se dit"],
         ["un atelier","« a-te-lier » — le « e » se dit"],
         ["rapidement","« ra-pid'ment » — le « e » tombe"],
         ["la semaine","« la s'maine » — le « e » tombe"],
         ["un médecin","« un méd'cin » — le « e » tombe"],
       ]},

      {t:'piege', h:"Deux pièges et une bonne nouvelle",
       rows:[
         ["prononcer chaque « e » écrit","laisser tomber ceux du milieu",
          "Dire « ra-pi-de-ment » en quatre morceaux se comprend, mais sonne appliqué et ralentit tout. Personne ne parle comme ça, et surtout pas au téléphone."],
         ["croire qu'on n'a pas compris le mot","reconnaître le mot amputé",
          "Quand vous entendez [lasmɛn] et que vous cherchez « la semaine », le problème n'est pas votre vocabulaire. Entraînez l'oreille à la forme courte."],
         ["s'inquiéter de se tromper","les deux formes se comprennent",
          "Garder un « e » qui aurait pu tomber ne provoque aucun malentendu. C'est à l'écoute que ça compte vraiment, pas à la production."],
       ]},

      {t:'check', h:"Est-ce que c'est clair maintenant ?",
       p:"Quatre questions rapides.",
       qs:[
         {q:"Dans « demander », le « e » de la première syllabe…", opts:["se prononce","tombe"], ok:0,
          fb:"Première syllabe, et « d » est une occlusive : il se maintient."},
         {q:"Dans « seulement », le « e » du milieu…", opts:["se prononce","tombe"], ok:1,
          fb:"Une seule consonne devant : on dit [sœlmɑ̃]."},
         {q:"Dans « un atelier », le « e »…", opts:["se prononce","tombe"], ok:0,
          fb:"Devant le son [lj], il ne tombe jamais."},
         {q:"Dans « autrement », deux consonnes précèdent le « e ». Il…", opts:["se maintient","tombe quand même"], ok:0,
          fb:"Sans lui, « tr » et « m » se suivraient : impossible à dire."},
       ]},

      {t:'revoir', h:"À retenir",
       p:"Début de mot après p, b, t, d, k, g : <b>on l'entend</b>. Devant [rj] ou [lj] : <b>on l'entend</b>. Deux consonnes devant : <b>on l'entend</b>. Partout ailleurs, au milieu du mot : <b>il tombe</b>. Entraînez l'oreille à la forme courte, c'est elle que vous entendrez au téléphone."},
    ]
  },

  prNom: {
    eye:'Mini-leçon', tit:"La nominalisation : le verbe déguisé en nom",
    blocs:[
      {t:'texte', h:"Pourquoi les textes officiels sont fatigants",
       p:"Comparez ces deux phrases. « On transforme le bois dans quatre usines de la région. » « La transformation du bois occupe quatre établissements régionaux. » Elles disent la même chose. La deuxième est plus courte, plus froide, et beaucoup plus difficile — parce que l'action a été changée en chose. C'est ce qu'on appelle la <b>nominalisation</b>, et un portrait économique en est fait à quatre-vingts pour cent.",
       note:"Ce n'est pas de la complication gratuite : un nom se compte, se compare et se met dans un tableau. Un verbe, non."},

      {t:'ana', h:"Les noms en -tion, -sion, -ation",
       p:"La plus grosse famille, et la plus régulière. Elle vient presque toujours d'un verbe en -er ou en -ir.",
       mots:[['Le verbe','transformer · fabriquer · produire · évaluer'],['Le nom','la transformation · la fabrication · la production · l\'évaluation',true],['Le genre','tous féminins, sans exception']],
       say:"la transformation, la fabrication, la production, une évaluation",
       note:"Bonne nouvelle : tous les noms en -tion sont féminins. C'est une des rares règles du français sans exception."},

      {t:'ana', h:"Les noms en -ment",
       p:"Deuxième famille. Attention à ne pas les confondre avec les adverbes en -ment, qui s'écrivent pareil mais ne sont pas des noms.",
       mots:[['Le verbe','recruter · investir · agrandir · développer'],['Le nom','le recrutement · l\'investissement · l\'agrandissement · le développement',true],['Le genre','tous masculins']],
       say:"le recrutement, un investissement, le développement",
       note:"<b>Rapidement</b> est un adverbe, <b>le recrutement</b> est un nom. Le déterminant devant les distingue à coup sûr."},

      {t:'ana', h:"Les noms en -ance et en -ence",
       p:"Plus petite famille, mais elle contient des mots très fréquents dans les textes économiques.",
       mots:[['Le verbe','croître · exiger · différer · concurrencer'],['Le nom','la croissance · l\'exigence · la différence · la concurrence',true],['Le genre','tous féminins']],
       say:"la croissance, une exigence, la concurrence",
       note:"On ne peut pas deviner entre -ance et -ence : ces mots-là s'apprennent avec leur orthographe."},

      {t:'ana', h:"Les noms sans suffixe",
       p:"Les plus courts, et les plus traîtres : rien ne signale qu'ils viennent d'un verbe.",
       mots:[['Le verbe','embaucher · demander · appeler · viser'],['Le nom','l\'embauche · la demande · l\'appel · la visée',true],['La règle','il n\'y en a pas : un par un']],
       say:"l'embauche, la demande, un appel",
       note:"Ce sont souvent les plus fréquents dans une offre d'emploi : « l'embauche », « la demande », « l'appel »."},

      {t:'labo', h:"Le verbe et son nom, côte à côte",
       p:"Choisissez une famille et un exemple.",
       axes:[
         {id:'f', lbl:'Quelle famille ?', opts:[['a','-tion'],['b','-ment'],['c','-ance'],['d','sans suffixe']]},
         {id:'n', lbl:'Quel exemple ?', opts:[['1','le premier'],['2','le second']]}],
       out:{
         a1:{w:["la transformation"], say:"On transforme l'aluminium : la transformation de l'aluminium.", n:'transformer → la transformation'},
         a2:{w:["la fabrication"], say:"On fabrique des pièces : la fabrication de pièces.", n:'fabriquer → la fabrication'},
         b1:{w:["le recrutement"], say:"On recrute peu : le recrutement est difficile.", n:'recruter → le recrutement'},
         b2:{w:["un investissement"], say:"Ils ont investi douze millions : cet investissement crée trente postes.", n:'investir → un investissement'},
         c1:{w:["la croissance"], say:"L'économie croît : la croissance a été de quatre virgule sept pour cent.", n:'croître → la croissance'},
         c2:{w:["une exigence"], say:"Le poste exige un diplôme : c'est une exigence de l'employeur.", n:'exiger → une exigence'},
         d1:{w:["l'embauche"], say:"L'usine embauche : l'embauche se fera avant janvier.", n:'embaucher → l\'embauche'},
         d2:{w:["la demande"], say:"Elle demande une rencontre : sa demande est claire.", n:'demander → la demande'},
       },
       note:"Écoutez la phrase avec le verbe, puis la phrase avec le nom. C'est la même information, deux fois."},

      {t:'texte', h:"Le sens passif, et c'est là que ça se complique",
       p:"« L'évaluation du dossier » ne veut pas dire que le dossier évalue quelque chose : il <b>est évalué</b>. Le nom garde l'action mais perd celui qui la fait, et le « de » qui suit désigne tantôt celui qui agit, tantôt celui qui subit. « La décision du comité » : c'est le comité qui décide. « L'évaluation du dossier » : personne ne sait qui évalue.",
       note:"Devant un nom en -tion suivi de « de », posez-vous la question : est-ce que ce qui suit fait l'action, ou la subit ?"},

      {t:'ex', h:"Six phrases, remises debout",
       p:"À gauche la phrase officielle, à droite ce qu'elle veut dire.",
       rows:[
         ["La transformation des ressources naturelles","on transforme le bois et le métal"],
         ["La baisse de l'embauche","on engage moins de monde"],
         ["Le comblement des postes par voie interne","on remplit les postes avec les gens de la maison"],
         ["L'évaluation comparative de vos études","on compare vos études à celles d'ici"],
         ["La mise en valeur de votre expérience","vous montrez ce que votre expérience vaut"],
         ["Une hausse de quatre virgule sept pour cent","l'économie a grandi de quatre virgule sept pour cent"],
       ]},

      {t:'piege', h:"Deux pièges",
       rows:[
         ["croire qu'on manque de vocabulaire","remettre le verbe debout",
          "Vous connaissez « transformer ». Vous butez sur « transformation » parce que la phrase autour a changé de forme, pas parce que le mot vous est inconnu."],
         ["nominaliser sa propre lettre","écrire avec des verbes",
          "Dans une lettre d'accompagnement, écrivez « j'ai formé deux techniciennes » et non « la formation de deux techniciennes ». Le nom convient au rapport officiel, pas à quelqu'un qui se présente."],
       ]},

      {t:'check', h:"Est-ce que c'est clair maintenant ?",
       p:"Quatre questions rapides.",
       qs:[
         {q:"Le nom qui vient de « fabriquer », c'est…", opts:["la fabrication","le fabriquement"], ok:0,
          fb:"Verbe en -er → nom en -tion, féminin."},
         {q:"Les noms en -tion sont…", opts:["tous féminins","tantôt l'un, tantôt l'autre"], ok:0,
          fb:"Sans exception : la transformation, la production, une exigence est en -ence."},
         {q:"« L'évaluation du dossier » veut dire…", opts:["le dossier est évalué","le dossier évalue"], ok:0,
          fb:"C'est un sens passif : le nom perd celui qui agit."},
         {q:"Dans une lettre d'accompagnement, il vaut mieux…", opts:["employer des verbes","nominaliser partout"], ok:0,
          fb:"Vous vous présentez : « j'ai formé », pas « la formation de »."},
       ]},

      {t:'revoir', h:"À retenir",
       p:"Quatre fabriques : <b>-tion</b> (féminin), <b>-ment</b> (masculin), <b>-ance / -ence</b> (féminin), et <b>rien du tout</b> (l'embauche, la demande). Pour lire : remettez le verbe debout. Pour écrire votre lettre : gardez le verbe, ne le déguisez pas."},
    ]
  },

  t1conn: {
    eye:'Mini-leçon', tit:"Les connecteurs qui font tourner un long discours",
    blocs:[
      {t:'texte', h:"Vingt minutes sans se perdre",
       p:"Une émission sur l'économie d'une région aligne des chiffres pendant vingt minutes. Ce qui empêche l'auditeur de décrocher n'est pas le contenu : ce sont une douzaine de petits mots qui annoncent chaque virage. « Quant à », « en ce qui concerne », « en somme ». Sans eux, tout se ressemble ; avec eux, on sait toujours où l'on en est.",
       note:"C'est l'outil le plus rentable du niveau : douze mots à apprendre, et un discours long devient suivable."},

      {t:'ana', h:"Ouvrir et rappeler",
       p:"Le début pose ce que l'auditeur doit savoir avant tout le reste.",
       mots:[['Les mots','d\'abord · pour commencer · rappelons que'],['Ce qu\'ils annoncent','le socle, ce qui vient avant le neuf',true],['Le réflexe','notez ce qui suit « rappelons que » : c\'est la clé du reste']],
       say:"D'abord, les chiffres. Rappelons que la région compte deux cent quatre-vingt-six mille habitants.",
       note:"« Rappelons que » est un signal fort : ce qui suit n'est pas la nouvelle, c'est ce qu'il faut savoir pour la comprendre."},

      {t:'ana', h:"Changer de sujet : les connecteurs de topicalisation",
       p:"Ce sont les plus utiles, et les plus rares dans la bouche des élèves. Ils disent : j'ai fini avec ce sujet, voici le suivant.",
       mots:[['Les mots','quant à · en ce qui concerne · à propos de · à l\'égard de'],['La construction','toujours suivis d\'un nom, en tête de phrase',true],['La contraction','quant au secteur · quant aux services · quant à la région']],
       say:"Quant aux services, ils représentent plus des trois quarts de l'emploi.",
       note:"« Quant à » n'a rien à voir avec « quand », qui parle du temps. Le « t » se prononce dans « quant à » : [kɑ̃ta]."},

      {t:'ana', h:"Ajouter un aspect nouveau du même dossier",
       p:"Ce n'est pas « en plus » : c'est « d'un autre côté de la même chose ».",
       mots:[['Les mots','par ailleurs · d\'autre part · en outre'],['Ce qu\'ils annoncent','un deuxième angle, pas un deuxième sujet',true],['La nuance','« par ailleurs » n\'oppose pas, il complète']],
       say:"Par ailleurs, la région n'est pas la seule à manquer de relève.",
       note:"Ne les confondez pas avec « en revanche » ou « pourtant », qui, eux, opposent."},

      {t:'ana', h:"Redire autrement, puis conclure",
       p:"Deux moments où le journaliste vous tend la main : il traduit, puis il résume.",
       mots:[['Redire','autrement dit · c\'est-à-dire · en d\'autres termes'],['Conclure','en somme · donc · par conséquent · au bout du compte',true],['Le réflexe','si vous ne notez qu\'une phrase, notez celle qui suit « en somme »']],
       say:"Autrement dit, la région tire deux fois plus de son sol que la moyenne. En somme : une région d'usines.",
       note:"« Autrement dit » annonce presque toujours la version simple de la phrase que vous venez de ne pas comprendre. Attendez-la."},

      {t:'labo', h:"Le même contenu, avec et sans connecteurs",
       p:"Choisissez un rôle et une version.",
       axes:[
         {id:'r', lbl:'Quel rôle ?', opts:[['a','changer de sujet'],['b','redire'],['c','conclure']]},
         {id:'v', lbl:'Quelle version ?', opts:[['1','sans connecteur'],['2','avec connecteur']]}],
       out:{
         a1:{w:["sans"], say:"La fabrication occupe onze pour cent. La construction occupe huit virgule neuf pour cent.", n:'deux phrases collées : on croit à une répétition'},
         a2:{w:["avec"], say:"La fabrication occupe onze pour cent. En ce qui concerne la construction, elle occupe huit virgule neuf pour cent.", n:'le virage est annoncé : on suit'},
         b1:{w:["sans"], say:"Le secteur primaire est à quatre virgule deux pour cent. La région tire deux fois plus de son sol que la moyenne.", n:'le lien entre les deux phrases est à deviner'},
         b2:{w:["avec"], say:"Le secteur primaire est à quatre virgule deux pour cent. Autrement dit, la région tire deux fois plus de son sol que la moyenne.", n:'la deuxième phrase traduit la première'},
         c1:{w:["sans"], say:"Une région d'usines, une main-d'œuvre qui manque, des employeurs qui répondent.", n:'on ne sait pas que c\'est la fin'},
         c2:{w:["avec"], say:"En somme : une région d'usines, une main-d'œuvre qui manque, des employeurs qui répondent.", n:'le résumé est annoncé, on écoute mieux'},
       },
       note:"Écoutez la version 1 puis la version 2. Le contenu est identique ; seule la lisibilité change."},

      {t:'ex', h:"Sept connecteurs et leur travail",
       p:"À gauche le mot, à droite ce qu'il annonce.",
       rows:[
         ["d'abord","le socle : ce qu'il faut savoir avant tout"],
         ["rappelons que","une information ancienne, nécessaire à la suite"],
         ["quant à","je change de sujet, voici le suivant"],
         ["en ce qui concerne","même chose, en un peu plus formel"],
         ["à propos de","un aspect qu'on vient d'évoquer et qu'on ouvre"],
         ["autrement dit","la version simple de ce que je viens de dire"],
         ["en somme","le résumé : la phrase à retenir"],
       ]},

      {t:'piege', h:"Trois pièges",
       rows:[
         ["« quand » à la place de « quant à »","distinguer le temps du sujet",
          "« Quand aux services » n'existe pas. « Quand » interroge sur le moment ; « quant à » annonce un sujet. Ils se prononcent presque pareil, ce qui n'aide pas."],
         ["oublier la contraction","quant au, quant aux, quant à la",
          "« Quant à les services » est une faute qui se remarque. C'est le même « à » que partout : à + les = aux."],
         ["confondre ajouter et opposer","par ailleurs ≠ en revanche",
          "« Par ailleurs » ajoute un angle ; « en revanche » contredit ce qui précède. Employer l'un pour l'autre inverse le sens de tout un paragraphe."],
       ]},

      {t:'check', h:"Est-ce que c'est clair maintenant ?",
       p:"Quatre questions rapides.",
       qs:[
         {q:"« Quant aux services » veut dire…", opts:["voici un nouveau sujet","à quel moment les services ?"], ok:0,
          fb:"C'est un connecteur de topicalisation : il annonce le sujet suivant."},
         {q:"Après « quant à », on met…", opts:["un nom","un verbe conjugué"], ok:0,
          fb:"Toujours un nom : quant à la construction, quant aux services."},
         {q:"« Autrement dit » annonce…", opts:["une traduction simple","une contradiction"], ok:0,
          fb:"C'est le moment d'écouter : la version simple arrive."},
         {q:"« Par ailleurs » sert à…", opts:["ajouter un angle","opposer deux idées"], ok:0,
          fb:"Pour opposer, c'est « en revanche » ou « pourtant »."},
       ]},

      {t:'revoir', h:"À retenir",
       p:"Quatre familles : <b>ouvrir</b> (d'abord, rappelons que) · <b>changer de sujet</b> (quant à, en ce qui concerne, à propos de) · <b>ajouter un angle</b> (par ailleurs) · <b>redire et conclure</b> (autrement dit, en somme). Douze mots, et vingt minutes de radio deviennent suivables."},
    ]
  },

  t1que: {
    eye:'Mini-leçon', tit:"La restriction avec ne… que",
    blocs:[
      {t:'texte', h:"Une négation qui ne nie rien",
       p:"« Je n'ai reçu que onze candidatures. » L'employeur a bien reçu onze candidatures : la phrase est positive. Le « ne » n'est là que par habitude de la langue, et c'est le « que » qui porte tout le sens. « ne… que » veut dire <b>seulement</b>, ni plus ni moins.",
       note:"C'est une des rares tournures où « ne » n'annonce pas une négation. D'où la confusion, qui dure souvent des années."},

      {t:'ana', h:"La construction, temps simple",
       p:"« ne » devant le verbe, « que » devant ce qu'on limite.",
       mots:[['La phrase','Il ne travaille que le jour.'],['Ce que ça veut dire','Il travaille seulement le jour, pas le soir.',true],['Ce que ça ne veut pas dire','Il ne travaille pas.']],
       say:"Il ne travaille que le jour.",
       note:"Si vous hésitez, remplacez mentalement « ne… que » par « seulement » et relisez : le sens doit tenir."},

      {t:'ana', h:"La construction, temps composé",
       p:"« ne » va devant l'auxiliaire, « que » reste collé au mot limité.",
       mots:[['La phrase','Elle n\'a envoyé que trois lettres.'],['Le découpage','ne + a envoyé + que trois lettres',true],['La faute fréquente','« Elle n\'a que envoyé trois lettres »']],
       say:"Elle n'a envoyé que trois lettres.",
       note:"Le « que » ne s'insère jamais entre l'auxiliaire et le participe : il attend le mot qu'il limite."},

      {t:'ana', h:"La place du « que » change tout",
       p:"C'est le point le plus important de cette leçon. Le « que » se colle à ce qu'on limite, et déplacer le « que » déplace le sens.",
       mots:[['Il ne travaille que le jour','pas le soir, pas la nuit'],['Il ne travaille qu\'à Jonquière','pas ailleurs',true],['Il n\'y a que lui qui travaille','les autres ne travaillent pas']],
       say:"Il ne travaille que le jour. Il ne travaille qu'à Jonquière.",
       note:"Devant une voyelle, « que » s'élide : qu'à, qu'onze, qu'un seul."},

      {t:'ana', h:"« ne pas que » : le sens s'inverse",
       p:"Ajoutez « pas », et la restriction devient son contraire.",
       mots:[['Il ne fait que produire','il produit, rien d\'autre'],['Il ne fait pas que produire','il produit, et il fait aussi autre chose',true],['Le repère','pas + que = « pas seulement »']],
       say:"Une usine ne fait pas que produire : elle vérifie aussi.",
       note:"Cette tournure est très fréquente dans les textes d'analyse. La confondre avec « ne… que » inverse le sens du paragraphe."},

      {t:'labo', h:"Le même chiffre, quatre limitations",
       p:"Choisissez ce que la phrase limite.",
       axes:[
         {id:'l', lbl:'On limite quoi ?', opts:[['a','le nombre'],['b','le lieu'],['c','le moment'],['d','rien : pas que']]},
         {id:'v', lbl:'Quelle version ?', opts:[['1','avec ne… que'],['2','avec seulement']]}],
       out:{
         a1:{w:["nombre"], say:"Il n'a reçu que onze candidatures.", n:'ce qui est limité : le nombre'},
         a2:{w:["nombre"], say:"Il a reçu seulement onze candidatures.", n:'même sens, ton plus parlé'},
         b1:{w:["lieu"], say:"Il ne recrute qu'à Jonquière.", n:'ce qui est limité : le lieu'},
         b2:{w:["lieu"], say:"Il recrute seulement à Jonquière.", n:'même sens'},
         c1:{w:["moment"], say:"Le poste n'est offert que sur le quart de jour.", n:'ce qui est limité : le moment'},
         c2:{w:["moment"], say:"Le poste est offert seulement sur le quart de jour.", n:'même sens'},
         d1:{w:["pas que"], say:"L'usine ne fait pas que produire.", n:'attention : sens inversé, elle fait autre chose aussi'},
         d2:{w:["pas que"], say:"L'usine ne produit pas seulement.", n:'même sens que la version 1'},
       },
       note:"Écoutez les deux versions : « ne… que » est la forme écrite, « seulement » la forme parlée."},

      {t:'ex', h:"Six phrases du module",
       p:"À gauche la restriction, à droite ce qu'elle veut dire.",
       rows:[
         ["Il n'a reçu que onze candidatures.","seulement onze, et c'est très peu"],
         ["Le laboratoire ne compte que sept personnes.","sept, alors qu'il en faudrait neuf"],
         ["Le poste n'est offert que sur le quart de jour.","pas de soir, pas de nuit"],
         ["Elle ne connaît que le marché de Montréal.","elle n'a jamais regardé ailleurs"],
         ["L'appel n'a duré que dix minutes.","dix minutes ont suffi"],
         ["Une usine ne fait pas que produire.","elle produit, et elle vérifie aussi"],
       ]},

      {t:'piege', h:"Trois pièges",
       rows:[
         ["lire « ne… que » comme une négation","c'est une phrase positive",
          "« Je n'ai que dix dollars » veut dire que j'ai dix dollars. Beaucoup d'élèves comprennent l'inverse pendant des années."],
         ["mettre le « que » n'importe où","le coller au mot limité",
          "« Il ne travaille que le jour » et « il n'y a que lui qui travaille » ne disent pas du tout la même chose."],
         ["confondre avec « ne pas que »","pas + que = pas seulement",
          "Une seule petite syllabe, et le sens du paragraphe se retourne."],
       ]},

      {t:'check', h:"Est-ce que c'est clair maintenant ?",
       p:"Quatre questions rapides.",
       qs:[
         {q:"« Je n'ai que dix dollars » veut dire…", opts:["j'ai dix dollars","je n'ai pas d'argent"], ok:0,
          fb:"La phrase est positive : « seulement dix dollars »."},
         {q:"Aux temps composés, le « ne » se place…", opts:["devant l'auxiliaire","devant le participe"], ok:0,
          fb:"Elle n'a envoyé que trois lettres."},
         {q:"Le « que » se place…", opts:["devant le mot limité","toujours après le verbe"], ok:0,
          fb:"C'est sa place qui décide du sens de la phrase."},
         {q:"« Il ne fait pas que produire » veut dire…", opts:["il fait aussi autre chose","il ne produit rien"], ok:0,
          fb:"Avec « pas », la restriction devient « pas seulement »."},
       ]},

      {t:'revoir', h:"À retenir",
       p:"<b>ne… que</b> = seulement, et la phrase reste positive. Le « ne » va devant le verbe ou l'auxiliaire ; le <b>« que » se colle à ce qu'on limite</b>, et c'est sa place qui fait le sens. Avec « pas » au milieu — <b>ne pas que</b> — le sens s'inverse : « pas seulement »."},
    ]
  },

  t1comp: {
    eye:'Mini-leçon', tit:"Comparer avec des chiffres : comparatifs et superlatifs",
    blocs:[
      {t:'texte', h:"Un chiffre seul ne dit rien",
       p:"« Quatre virgule deux pour cent. » Est-ce beaucoup ? On n'en sait rien. « Quatre virgule deux pour cent, contre deux pour cent pour l'ensemble du Québec » : maintenant on sait, et on sait même l'essentiel — c'est le double. Comparer n'est pas un ornement dans un texte économique : c'est la seule façon d'y donner un sens à un nombre.",
       note:"C'est aussi ce que votre exposé oral devra faire : comparer deux régions, pas les décrire l'une après l'autre."},

      {t:'ana', h:"Comparer des quantités : plus de, moins de, autant de",
       p:"Trois formes, toujours suivies d'un nom, toujours avec « de » et jamais avec un article.",
       mots:[['Plus grand','Il y a plus d\'usines ici.'],['Plus petit','Il y a moins de bureaux.',true],['Égal','Il y a autant de postes qu\'à Québec.']],
       say:"Il y a plus d'usines ici, et moins de bureaux.",
       note:"« plus des usines » n'existe pas. Le « de » ne s'accorde jamais et ne se combine jamais avec « le », « la » ou « les »."},

      {t:'ana', h:"Comparer des actions : après le verbe, sans « de »",
       p:"Quand on compare ce que font deux choses plutôt que combien il y en a, le « de » disparaît.",
       mots:[['La forme','Cette région embauche plus que la moyenne.'],['Sans « de »','on compare l\'action, pas une quantité',true],['L\'élégant','« davantage » remplace « plus », jamais devant un adjectif']],
       say:"Cette région embauche plus que la moyenne. Elle investit davantage.",
       note:"« davantage » ne se met jamais devant un adjectif : « davantage grand » est une faute, « plus grand » est la forme."},

      {t:'ana', h:"Le deuxième terme s'introduit par « que »",
       p:"Et il se laisse souvent tomber quand il va de soi.",
       mots:[['Complet','Il y a plus d\'emplois en construction que dans le primaire.'],['Abrégé','Huit virgule neuf pour cent, contre sept pour cent.',true],['Le mot des textes','« contre » remplace « que » dans les tableaux et les portraits']],
       say:"Huit virgule neuf pour cent, contre sept pour cent pour l'ensemble du Québec.",
       note:"Repérez « contre » dans un portrait économique : c'est le mot qui annonce la comparaison utile."},

      {t:'ana', h:"Le superlatif : l'article fait tout",
       p:"On passe du comparatif au superlatif en ajoutant l'article devant, et cet article s'accorde avec le nom.",
       mots:[['Masculin','le secteur le plus important'],['Féminin','la région la plus jeune',true],['Avec un nom','C\'est ici qu\'il y a le plus de postes affichés.']],
       say:"le secteur le plus important, la région la plus jeune",
       note:"Avec un nom, l'article reste « le », invariable : « le plus de postes », « le plus de candidatures »."},

      {t:'ana', h:"Les deux irréguliers, à connaître par cœur",
       p:"Ce sont les deux seuls du français courant, et ils reviennent tout le temps.",
       mots:[['bon','meilleur — jamais « plus bon »'],['bien','mieux — jamais « plus bien »',true],['Au superlatif','le meilleur · le mieux']],
       say:"Les perspectives y sont meilleures, et on y vit mieux.",
       note:"« bon » est un adjectif, « bien » un adverbe. On dit « une meilleure offre » mais « elle écrit mieux »."},

      {t:'labo', h:"Le même fait, trois façons de le dire",
       p:"Choisissez une comparaison et une forme.",
       axes:[
         {id:'c', lbl:'Quelle comparaison ?', opts:[['a','quantité'],['b','action'],['c','superlatif']]},
         {id:'f', lbl:'Quelle forme ?', opts:[['1','plus'],['2','moins']]}],
       out:{
         a1:{w:["plus de"], say:"Il y a plus d'usines dans cette région que dans la moyenne du Québec.", n:'quantité : plus de + nom'},
         a2:{w:["moins de"], say:"Il y a moins de bureaux dans cette région qu'à Montréal.", n:'quantité : moins de + nom'},
         b1:{w:["plus"], say:"Cette région embauche plus que la moyenne québécoise.", n:'action : plus, après le verbe, sans « de »'},
         b2:{w:["moins"], say:"Cette région embauche moins que Montréal en informatique.", n:'action : moins, sans « de »'},
         c1:{w:["le plus"], say:"C'est le secteur le plus important de la région.", n:'superlatif masculin'},
         c2:{w:["la moins"], say:"C'est la région la moins peuplée des trois.", n:'superlatif féminin'},
       },
       note:"Écoutez le « de » : il est là dans la quantité, absent dans l'action."},

      {t:'ex', h:"Six comparaisons du module",
       p:"À gauche la phrase, à droite ce qu'elle compare.",
       rows:[
         ["quatre virgule deux pour cent contre deux pour cent","le secteur primaire d'ici et celui du Québec"],
         ["huit virgule neuf pour cent contre sept pour cent","la construction d'ici et celle du Québec"],
         ["moins de postes ouverts et plus de candidats","le marché de Montréal"],
         ["deux fois plus que la moyenne","l'importance du sol et de la forêt"],
         ["le secteur le plus important en valeur des ventes","la fabrication dans la région"],
         ["des perspectives meilleures qu'à Montréal","un métier précis, région par région"],
       ]},

      {t:'piege', h:"Trois pièges",
       rows:[
         ["« plus des usines »","plus d'usines",
          "Le « de » de la quantité ne se combine jamais avec un article. C'est la faute la plus visible à l'écrit."],
         ["« plus bon », « plus bien »","meilleur, mieux",
          "Deux irréguliers, deux seulement. Les apprendre coûte cinq minutes et évite une faute par paragraphe."],
         ["donner un chiffre sans point de comparaison","toujours dire « contre »",
          "Dans votre exposé, un pourcentage seul ne convainc personne. Donnez toujours le chiffre auquel vous le comparez."],
       ]},

      {t:'check', h:"Est-ce que c'est clair maintenant ?",
       p:"Quatre questions rapides.",
       qs:[
         {q:"Devant un nom, on écrit…", opts:["plus d'usines","plus des usines"], ok:0,
          fb:"Le « de » de quantité ne prend jamais d'article."},
         {q:"Le comparatif de « bon », c'est…", opts:["meilleur","plus bon"], ok:0,
          fb:"Et celui de « bien » est « mieux »."},
         {q:"« Elle investit davantage » est…", opts:["correct","incorrect"], ok:0,
          fb:"« davantage » remplace « plus » après un verbe. Il ne va jamais devant un adjectif."},
         {q:"Dans un portrait économique, « contre » annonce…", opts:["une comparaison","une opposition d'opinion"], ok:0,
          fb:"« Huit virgule neuf pour cent, contre sept pour cent » : c'est le chiffre de référence."},
       ]},

      {t:'revoir', h:"À retenir",
       p:"Quantité : <b>plus de / moins de / autant de</b> + nom, sans article. Action : <b>plus / moins / autant</b> après le verbe, sans « de ». Superlatif : <b>l'article devant</b>, accordé avec le nom. Deux irréguliers : <b>meilleur</b> et <b>mieux</b>. Et jamais un chiffre sans son point de comparaison."},
    ]
  },

  t2portrait: {
    eye:'Mini-leçon', tit:"Lire un portrait économique en vingt minutes",
    blocs:[
      {t:'texte', h:"Ce n'est pas un texte, c'est un tableau déguisé",
       p:"Un portrait socioéconomique n'est pas écrit pour être lu du début à la fin. C'est un tableau qu'on a mis en phrases. Le lire ligne à ligne, en cherchant chaque mot, est la pire méthode : on met deux heures et on n'en retient rien. Ce qu'il faut, c'est savoir où regarder, et savoir quelles trois questions poser au document.",
       note:"Vous en lirez cinq ou six pour choisir une région. Une méthode de vingt minutes est donc la vraie compétence, pas la lecture intégrale."},

      {t:'ana', h:"Sa structure : un entonnoir, toujours le même",
       p:"Quel que soit le ministère qui l'écrit, l'ordre est fixe. Vous pouvez donc sauter.",
       mots:[['1. Le territoire','population, superficie, rang parmi les régions'],['2. L\'économie d\'ensemble','produit intérieur brut, emploi total, croissance',true],['3. Les secteurs','primaire, fabrication, construction, services']],
       say:"D'abord le territoire, ensuite l'économie d'ensemble, enfin les secteurs.",
       note:"Si vous cherchez un métier, votre information est au tiers du texte, dans la partie 3. Le reste est du contexte."},

      {t:'ana', h:"Sa langue : des pourcentages de l'emploi, pas des postes",
       p:"C'est la source d'erreur la plus fréquente, et elle change tout.",
       mots:[['Ce qui est écrit','la fabrication occupe 11,2 % de l\'emploi'],['Ce que ce n\'est pas','onze mille deux cents postes',true],['Pour convertir','11,2 % de 137 100, soit environ quinze mille postes']],
       say:"La fabrication occupe onze virgule deux pour cent de l'emploi total.",
       note:"L'emploi total est donné au début du document, jamais à côté du pourcentage. Notez-le avant de lire la suite."},

      {t:'ana', h:"Son seul procédé d'argumentation : la comparaison",
       p:"Il ne dit jamais « beaucoup » ni « peu ». Il donne deux chiffres et vous laisse conclure.",
       mots:[['La forme','4,2 %, contre 2,0 % pour l\'ensemble du Québec'],['Ce qu\'il faut lire','le deuxième chiffre, celui de la référence',true],['Ce qu\'on en tire','le double : c\'est une région de ressources']],
       say:"Quatre virgule deux pour cent, contre deux pour cent pour l'ensemble du Québec.",
       note:"Surlignez les « contre ». Il y en a une dizaine, et ils portent à eux seuls le message du document."},

      {t:'texte', h:"Ce qu'un portrait ne dit jamais",
       p:"Il décrit une <b>structure</b>, jamais un <b>manque</b>. Aucun portrait n'écrira « il manque des techniciennes de laboratoire ». Pour ça, il faut IMT en ligne, qui donne les perspectives d'emploi profession par profession et région par région. Les deux documents se lisent ensemble : le portrait dit de quoi la région vit, IMT dit si votre métier y trouve preneur.",
       note:"C'est pour la même raison qu'aucun portrait ne parle de salaires : ce n'est pas son objet."},

      {t:'texte', h:"Et il date",
       p:"Un portrait publié cette année contient souvent des données de l'an dernier ou de l'année d'avant. Ce n'est pas un défaut : les statistiques économiques prennent ce temps-là. Mais cela veut dire qu'une usine fermée il y a six mois y figure encore. Vérifiez la date de chaque chiffre — elle est toujours écrite — et croisez avec une source d'actualité avant de bâtir une décision de déménagement dessus.",
       note:"Dans notre portrait, le produit intérieur brut est celui de 2023 et l'emploi celui de 2025. Deux dates, dans le même document."},

      {t:'ex', h:"Les trois questions à poser au document",
       p:"Vingt minutes, trois réponses, et vous passez au portrait suivant.",
       rows:[
         ["Est-ce que mon métier existe ici ?","partie 3 : quels secteurs, et de quel type"],
         ["Est-ce qu'il y manque du monde ?","le portrait ne le dit pas — IMT en ligne le dit"],
         ["Est-ce que ma famille pourrait y vivre ?","aucun document ne répond : c'est une décision"],
       ]},

      {t:'piege', h:"Deux pièges",
       rows:[
         ["lire du début à la fin","aller à la partie qui vous concerne",
          "Deux pages de population et de superficie n'apprennent rien à quelqu'un qui cherche un laboratoire. Sautez."],
         ["prendre un pourcentage pour un nombre de postes","noter d'abord l'emploi total",
          "Onze virgule deux pour cent, c'est une part. Sans l'emploi total, c'est une information vide."],
       ]},

      {t:'check', h:"Est-ce que c'est clair maintenant ?",
       p:"Quatre questions rapides.",
       qs:[
         {q:"Dans un portrait, l'information sur les secteurs se trouve…", opts:["au tiers du texte","à la toute fin"], ok:0,
          fb:"L'ordre est fixe : territoire, économie d'ensemble, secteurs."},
         {q:"« 11,2 % de l'emploi » veut dire…", opts:["une part de l'emploi total","onze mille deux cents postes"], ok:0,
          fb:"Pour convertir, il faut l'emploi total, donné au début."},
         {q:"Pour savoir s'il manque de la main-d'œuvre, il faut…", opts:["IMT en ligne","relire le portrait"], ok:0,
          fb:"Un portrait décrit une structure, jamais un manque."},
         {q:"Le mot « contre » dans un portrait annonce…", opts:["le chiffre de référence","une objection"], ok:0,
          fb:"C'est le seul procédé d'argumentation du document."},
       ]},

      {t:'revoir', h:"À retenir",
       p:"Structure en entonnoir : <b>territoire, économie d'ensemble, secteurs</b>. Les chiffres sont des <b>parts de l'emploi</b>, pas des postes. Le mot <b>« contre »</b> porte tout le message. Un portrait décrit une structure, <b>jamais un manque</b> : pour le manque, c'est IMT en ligne."},
    ]
  },

  t2passif: {
    eye:'Mini-leçon', tit:"La phrase passive au passé composé",
    blocs:[
      {t:'texte', h:"Dire ce qui est arrivé sans dire qui l'a fait",
       p:"« L'usine a été agrandie en 2021. » Par qui ? Le texte ne le dit pas, et c'est délibéré. La phrase passive est l'outil qui permet de rapporter un événement en laissant son auteur dans l'ombre — parce qu'on l'ignore, parce que ça n'intéresse personne, ou parce qu'on préfère ne pas le nommer. Un portrait économique en est plein pour la deuxième raison.",
       note:"Ce n'est pas une tournure difficile à comprendre. Ce qui est difficile, c'est de se souvenir qu'elle cache toujours quelqu'un."},

      {t:'ana', h:"La recette : être au passé composé + participe passé",
       p:"Il y a donc deux participes de suite, et c'est ce qui déroute la première fois.",
       mots:[['Actif','On a agrandi l\'usine.'],['Passif','L\'usine a été agrandie.',true],['Le découpage','a (auxiliaire) + été (participe d\'être) + agrandie (participe du verbe)']],
       say:"On a agrandi l'usine. L'usine a été agrandie.",
       note:"« a été » se prononce en deux syllabes bien détachées : [a‿ete]. C'est le signal sonore du passif."},

      {t:'ana', h:"L'accord se fait avec le sujet, toujours",
       p:"Sans exception, et c'est la faute la plus fréquente dans les lettres.",
       mots:[['Féminin singulier','L\'usine a été agrandi<b>e</b>.'],['Masculin pluriel','Les postes ont été affich<b>és</b>.',true],['Féminin pluriel','Les candidatures ont été reç<b>ues</b>.']],
       say:"L'usine a été agrandie. Les postes ont été affichés. Les candidatures ont été reçues.",
       note:"C'est le participe du verbe qui s'accorde, pas « été », qui reste invariable."},

      {t:'ana', h:"Le complément d'agent en « par »",
       p:"On peut nommer celui qui agit. On ne le fait que si c'est une information utile.",
       mots:[['Sans agent','Le poste a été comblé.'],['Avec agent','Le poste a été comblé par le comité de sélection.',true],['La question à se poser','est-ce que savoir qui change quelque chose ?']],
       say:"Le poste a été comblé par le comité de sélection.",
       note:"Dans un portrait économique, l'agent est absent neuf fois sur dix. Dans une lettre, nommez-le : c'est plus clair."},

      {t:'ana', h:"Le complément d'agent en « de »",
       p:"Après quelques verbes de sentiment ou d'accompagnement, ce n'est pas « par » mais « de ». À reconnaître plutôt qu'à produire.",
       mots:[['Sentiment','Il est respecté de ses collègues.'],['Accompagnement','Le rapport était accompagné d\'une annexe.',true],['Connaissance','Cette usine est connue de tout le monde ici.']],
       say:"Il est respecté de ses collègues. Le rapport était accompagné d'une annexe.",
       note:"Ils sont peu nombreux : respecter, aimer, connaître, accompagner, suivre, précéder, entourer."},

      {t:'labo', h:"La même information, deux fois",
       p:"Choisissez une phrase et une voix.",
       axes:[
         {id:'p', lbl:'Quelle phrase ?', opts:[['a','l\'usine'],['b','les postes'],['c','les candidatures']]},
         {id:'v', lbl:'Quelle voix ?', opts:[['1','active'],['2','passive']]}],
       out:{
         a1:{w:["actif"], say:"On a agrandi l'usine en 2021.", n:'on sait qu\'il y a un auteur, même vague'},
         a2:{w:["passif"], say:"L'usine a été agrandie en 2021.", n:'l\'auteur disparaît, l\'usine passe devant'},
         b1:{w:["actif"], say:"L'entreprise a affiché les deux postes en février.", n:'l\'entreprise est le sujet'},
         b2:{w:["passif"], say:"Les deux postes ont été affichés en février.", n:'accord au masculin pluriel'},
         c1:{w:["actif"], say:"Le service a reçu onze candidatures.", n:'le service est le sujet'},
         c2:{w:["passif"], say:"Onze candidatures ont été reçues.", n:'accord au féminin pluriel : reçues'},
       },
       note:"Écoutez la fin du participe : c'est là que l'accord s'entend, au féminin."},

      {t:'ex', h:"Six passives du module",
       p:"À gauche la phrase, à droite ce qu'elle cache.",
       rows:[
         ["L'usine a été agrandie en 2021.","on ne sait pas qui a payé l'agrandissement"],
         ["Les deux postes ont été affichés en février.","on ne sait pas qui a décidé de les ouvrir"],
         ["Onze candidatures ont été reçues.","on ne sait pas par quel service"],
         ["Sa candidature a été retenue par le comité.","ici l'agent est nommé : le comité"],
         ["Le portrait régional a été publié l'an dernier.","par le gouvernement, mais ce n'est pas dit"],
         ["Ses études ont été évaluées par le ministère.","agent nommé : c'est une information utile"],
       ]},

      {t:'piege', h:"Trois pièges",
       rows:[
         ["oublier l'accord du participe","toujours avec le sujet",
          "« Les candidatures ont été reçu » se voit immédiatement. Le passif accorde toujours, contrairement au passé composé avec « avoir »."],
         ["croire que le passif dit quand","il ne dit que ce qui est arrivé",
          "« Le poste a été comblé » ne dit ni quand il a été affiché, ni par qui il a été comblé. Ne complétez jamais avec ce que vous imaginez."],
         ["employer le passif dans sa lettre","écrire à la voix active",
          "« Deux techniciennes ont été formées par moi » est ridicule. Écrivez « j'ai formé deux techniciennes ». Le passif convient au rapport, pas à la candidature."],
       ]},

      {t:'check', h:"Est-ce que c'est clair maintenant ?",
       p:"Quatre questions rapides.",
       qs:[
         {q:"« Les candidatures ont été… »", opts:["reçues","reçu"], ok:0,
          fb:"Le participe s'accorde avec le sujet : féminin pluriel."},
         {q:"Dans un passif, « été » s'accorde…", opts:["jamais","avec le sujet"], ok:0,
          fb:"« été » est invariable. C'est le participe du verbe qui s'accorde."},
         {q:"« Il est respecté … ses collègues »", opts:["de","par"], ok:0,
          fb:"Verbe de sentiment : le complément d'agent se met avec « de »."},
         {q:"Dans une lettre d'accompagnement, il vaut mieux…", opts:["la voix active","la voix passive"], ok:0,
          fb:"Vous vous présentez : « j'ai formé », « j'ai tenu », « j'ai analysé »."},
       ]},

      {t:'revoir', h:"À retenir",
       p:"<b>être au passé composé + participe passé</b>, et le participe <b>s'accorde avec le sujet</b>, toujours. L'agent s'introduit par <b>par</b> — ou par <b>de</b> après quelques verbes de sentiment. Le passif cache toujours quelqu'un : en lecture, demandez-vous qui. En écriture, préférez l'actif."},
    ]
  },

  t2ils: {
    eye:'Mini-leçon', tit:"« Ils » quand personne n'a été nommé",
    blocs:[
      {t:'texte', h:"Le pronom qui ne reprend rien",
       p:"« L'usine a rouvert en mars. Ils ont investi douze millions. » Qui, « ils » ? Relisez la première phrase : personne n'y est nommé au pluriel. Ce n'est pas une faute de l'auteur et ce n'est pas un mot que vous auriez manqué. C'est un <b>référent implicite</b> : « ils » désigne des décideurs que le texte a choisi de ne pas nommer.",
       note:"Le savoir change tout : au lieu de relire trois fois en cherchant votre erreur, vous continuez."},

      {t:'ana', h:"Le cas ordinaire, pour comparer",
       p:"D'habitude, un pronom reprend un groupe nommé juste avant. C'est ce à quoi vous êtes habitué.",
       mots:[['Phrase 1','Les techniciens ont signé leur contrat.'],['Phrase 2','Ils commencent lundi.',true],['« Ils » désigne','les techniciens — c\'est écrit']],
       say:"Les techniciens ont signé leur contrat. Ils commencent lundi.",
       note:"On appelle ça la reprise de l'information, et c'est ce qui tient un texte ensemble."},

      {t:'ana', h:"Le cas du niveau 7 : rien à reprendre",
       p:"Le groupe n'a jamais été nommé, et il ne le sera pas.",
       mots:[['Phrase 1','L\'usine a rouvert en mars.'],['Phrase 2','Ils ont investi douze millions.',true],['« Ils » désigne','les propriétaires, la direction — non nommés']],
       say:"L'usine a rouvert en mars. Ils ont investi douze millions.",
       note:"Le pluriel du pronom ne prouve rien : il peut renvoyer à une seule entreprise, vue comme un groupe de gens."},

      {t:'ana', h:"Ce que le contexte permet de deviner",
       p:"On ne devine pas au hasard : le paragraphe précédent donne presque toujours la famille.",
       mots:[['Le paragraphe parle d\'une usine','« ils » = la direction, les propriétaires'],['Le paragraphe parle d\'un budget','« ils » = le gouvernement, les élus',true],['Le paragraphe parle d\'un service','« ils » = les gens de ce service']],
       say:"Hafida a téléphoné aux ressources humaines. Ils lui ont demandé son curriculum vitæ.",
       note:"Le bon réflexe : remonter d'un paragraphe, pas d'une phrase. C'est là que se trouve la famille du référent."},

      {t:'texte', h:"Le « ils » du français parlé au Québec",
       p:"À l'oral, « ils » sert de « on » vague, et personne ne se demande qui : « Ils ont encore augmenté le loyer. » « Ils ferment à cinq heures. » Il se prononce souvent [i] ou [j], sans le « l » : « <i>Y ont fermé à cinq heures.</i> » Vous l'entendrez tous les jours, et vous pouvez l'employer en conversation sans crainte.",
       note:"Ne le corrigez pas chez les autres : c'est du français standard parlé, pas une négligence."},

      {t:'texte', h:"Mais pas dans votre lettre",
       p:"Ce flou est permis au journaliste et à l'auteur d'un rapport, parce que leur sujet est le fait, pas les personnes. Dans une lettre d'accompagnement, il vous dessert : « ils m'ont demandé de former deux techniciennes » laisse penser que vous ne savez pas qui vous employait. Nommez : « la direction m'a demandé », « le service de la qualité m'a confié ». Précision et responsabilité vont ensemble.",
       note:"C'est vrai aussi de « on ». Dans une candidature, « on » est presque toujours à remplacer par un vrai sujet."},

      {t:'ex', h:"Cinq « ils », et ce qu'ils désignent",
       p:"À gauche le contexte, à droite le référent probable.",
       rows:[
         ["La direction a présenté son plan au conseil. Ils ont approuvé.","le conseil — c'est lui qui approuve"],
         ["Le laboratoire compte sept personnes. Ils cherchent deux techniciens.","le laboratoire, vu comme une équipe"],
         ["Le gouvernement a publié le portrait. Ils y donnent le produit intérieur brut.","le gouvernement"],
         ["Elle a appelé les ressources humaines. Ils ont demandé son dossier.","le service des ressources humaines"],
         ["Le budget a été voté en avril. Ils avaient promis un centre de formation.","des élus — aucun nom n'est donné"],
       ]},

      {t:'piege', h:"Deux pièges",
       rows:[
         ["se croire fautif","accepter le flou du texte",
          "Quand vous ne trouvez pas le référent, ce n'est presque jamais votre lecture : c'est une information que le texte n'a pas donnée."],
         ["inventer un référent précis","rester dans la famille",
          "Répondre « le président de l'entreprise » quand le texte dit seulement « ils », c'est ajouter ce qui n'y est pas. « La direction » suffit."],
       ]},

      {t:'check', h:"Est-ce que c'est clair maintenant ?",
       p:"Quatre questions rapides.",
       qs:[
         {q:"« L'usine a rouvert. Ils ont investi. » Ici, « ils »…", opts:["n'a pas d'antécédent écrit","reprend « l'usine »"], ok:0,
          fb:"C'est un référent implicite : les décideurs, non nommés."},
         {q:"Pour deviner le référent, il faut remonter…", opts:["d'un paragraphe","d'un seul mot"], ok:0,
          fb:"La famille du référent se trouve dans le paragraphe précédent."},
         {q:"À l'oral au Québec, « ils » se prononce souvent…", opts:["[i] ou [j]","avec un « l » très net"], ok:0,
          fb:"« Y ont fermé à cinq heures. » C'est du français standard parlé."},
         {q:"Dans une lettre d'accompagnement, ce « ils » vague…", opts:["est à remplacer par un vrai sujet","convient très bien"], ok:0,
          fb:"Nommez : « la direction », « le service de la qualité »."},
       ]},

      {t:'revoir', h:"À retenir",
       p:"Un « ils » sans antécédent écrit est un <b>référent implicite</b> : les décideurs, non nommés. Remontez <b>d'un paragraphe</b> pour en trouver la famille, et acceptez le flou quand il n'y a rien. Permis au journaliste ; <b>à bannir de votre lettre</b>, où l'on nomme."},
    ]
  },

  t2subst: {
    eye:'Mini-leçon', tit:"La substitution lexicale : redire sans répéter",
    blocs:[
      {t:'texte', h:"Pourquoi un mot revient sous quatre visages",
       p:"Dans un texte suivi, le même objet est nommé plusieurs fois, et presque jamais avec le même mot : « l'usine », puis « l'établissement », puis « l'installation », puis « le site ». Ce n'est pas de la coquetterie : répéter huit fois le même mot rend un texte pénible. Mais pour le lecteur qui apprend le français, c'est un piège : on croit qu'un nouveau sujet apparaît alors qu'on nous reparle du même.",
       note:"C'est la première cause de perte du fil dans un texte informatif long — avant le vocabulaire, avant la grammaire."},

      {t:'ana', h:"Procédé 1 — le synonyme",
       p:"Un autre mot de même sens. Le plus simple, et le plus facile à repérer.",
       mots:[['Le mot','une usine'],['La reprise','une fabrique · une manufacture',true],['Le repère','les deux mots sont du même niveau de précision']],
       say:"L'usine de Jonquière emploie six cents personnes. Cette fabrique existe depuis 1943.",
       note:"Les vrais synonymes sont rares. Le plus souvent, la reprise est un peu plus générale que le mot de départ."},

      {t:'ana', h:"Procédé 2 — le mot générique",
       p:"Le procédé le plus fréquent, et le plus déroutant. On remonte d'un cran vers le général.",
       mots:[['Le mot','l\'aluminium'],['La reprise','ce métal · cette ressource · ce produit',true],['Le signal','le déterminant « ce » ou « cette » devant un mot très général']],
       say:"La région produit de l'aluminium. Ce métal représente l'essentiel de ses exportations.",
       note:"Règle pratique : un « ce » ou un « cette » devant un mot très général annonce presque toujours une reprise. Cherchez en arrière."},

      {t:'ana', h:"Procédé 3 — la nominalisation",
       p:"On reprend une action déjà racontée en la transformant en nom.",
       mots:[['Ce qui précède','L\'entreprise a embauché douze personnes.'],['La reprise','Cette embauche portera ses fruits en janvier.',true],['Le signal','« cette » + un nom qui vient d\'un verbe déjà employé']],
       say:"L'entreprise a embauché douze personnes. Cette embauche portera ses fruits en janvier.",
       note:"C'est la rencontre des deux savoirs de ce module : la nominalisation sert à reprendre l'information."},

      {t:'ana', h:"Procédé 4 — la périphrase",
       p:"On remplace le nom par une description. Fréquent pour les lieux et les personnes.",
       mots:[['Le mot','le Saguenay–Lac-Saint-Jean'],['La reprise','cette région du nord du fleuve · ce territoire de deux cent quatre-vingt-six mille habitants',true],['Le repère','plusieurs mots au lieu d\'un']],
       say:"Le Saguenay–Lac-Saint-Jean produit de l'aluminium. Cette région du nord du fleuve compte deux cent quatre-vingt-six mille habitants.",
       note:"Dans les portraits régionaux, la périphrase sert surtout à éviter de réécrire un nom de région très long."},

      {t:'labo', h:"Le même référent, quatre reprises",
       p:"Choisissez un procédé et un exemple.",
       axes:[
         {id:'p', lbl:'Quel procédé ?', opts:[['a','synonyme'],['b','générique'],['c','nominalisation'],['d','périphrase']]},
         {id:'n', lbl:'Quel exemple ?', opts:[['1','le premier'],['2','le second']]}],
       out:{
         a1:{w:["synonyme"], say:"L'usine de Jonquière. Cette fabrique existe depuis 1943.", n:'usine → fabrique'},
         a2:{w:["synonyme"], say:"Le poste affiché. Cette fonction est offerte sur le quart de jour.", n:'poste → fonction'},
         b1:{w:["générique"], say:"La région produit de l'aluminium. Ce métal part vers l'étranger.", n:'aluminium → ce métal'},
         b2:{w:["générique"], say:"Le programme d'aide à l'installation. Cette mesure vise les gens d'ailleurs.", n:'programme → cette mesure'},
         c1:{w:["nominalisation"], say:"L'entreprise a embauché douze personnes. Cette embauche était attendue.", n:'a embauché → cette embauche'},
         c2:{w:["nominalisation"], say:"On a agrandi le laboratoire. Cet agrandissement date de 2021.", n:'a agrandi → cet agrandissement'},
         d1:{w:["périphrase"], say:"Le Saguenay–Lac-Saint-Jean. Cette région du nord du fleuve.", n:'un nom long remplacé par sa description'},
         d2:{w:["périphrase"], say:"Frédérick Gauthier-Simard. Le chef du laboratoire d'Alumico.", n:'une personne remplacée par sa fonction'},
       },
       note:"Écoutez les deux phrases : c'est toujours du même objet qu'on parle."},

      {t:'texte', h:"Ce que ça vous donne en écriture",
       p:"Votre lettre y gagne autant que votre lecture. Vous voulez parler trois fois du poste sans recopier l'annonce trois fois : « ce poste », puis « cette fonction », puis « le mandat que vous décrivez ». Trois façons de désigner une seule chose. C'est ce qui distingue une lettre écrite d'une lettre remplie.",
       note:"Le seul mot qu'on répète volontiers, c'est le titre exact du poste, et seulement en tête du curriculum vitæ."},

      {t:'piege', h:"Deux pièges",
       rows:[
         ["croire à un nouveau sujet","suivre le « ce » et le « cette »",
          "« Ce métal », « cette mesure », « cette activité » : à chaque fois, cherchez en arrière. Vous n'avez pas changé de sujet."],
         ["chercher un synonyme parfait","accepter le mot plus général",
          "Une reprise est presque toujours un peu plus vague que le mot de départ. C'est normal, et c'est même son intérêt."],
       ]},

      {t:'check', h:"Est-ce que c'est clair maintenant ?",
       p:"Quatre questions rapides.",
       qs:[
         {q:"« La région produit de l'aluminium. Ce métal… » — « ce métal » désigne…", opts:["l'aluminium","un autre produit"], ok:0,
          fb:"C'est une reprise par mot générique."},
         {q:"Le signal le plus fiable d'une reprise, c'est…", opts:["« ce » ou « cette » devant un mot général","une majuscule"], ok:0,
          fb:"Un déterminant démonstratif devant un mot vague : cherchez en arrière."},
         {q:"« On a agrandi le laboratoire. Cet agrandissement… » est une reprise par…", opts:["nominalisation","périphrase"], ok:0,
          fb:"Le verbe de la phrase précédente est devenu un nom."},
         {q:"Dans votre lettre, la substitution sert à…", opts:["ne pas recopier l'annonce","allonger le texte"], ok:0,
          fb:"« ce poste », « cette fonction », « le mandat que vous décrivez »."},
       ]},

      {t:'revoir', h:"À retenir",
       p:"Quatre procédés : <b>synonyme</b>, <b>mot générique</b>, <b>nominalisation</b>, <b>périphrase</b>. Le signal en lecture est presque toujours un <b>« ce » ou « cette » devant un mot très général</b> : cherchez en arrière plutôt que d'accueillir un nouveau sujet. Et servez-vous-en pour écrire."},
    ]
  },

  t3offre: {
    eye:'Mini-leçon', tit:"Lire une offre d'emploi avant d'y répondre",
    blocs:[
      {t:'texte', h:"Une annonce se lit deux fois",
       p:"La première lecture répond à une seule question : est-ce que ce poste est pour moi ? La deuxième, plus lente, sert à autre chose : y récolter les mots avec lesquels vous allez écrire. Une offre d'emploi n'est pas seulement une description, c'est un vocabulaire imposé — et le candidat qui l'emploie se fait lire plus vite que celui qui traduit tout dans ses propres termes.",
       note:"Imprimez l'annonce et surlignez. Ce qui est surligné se retrouvera dans votre lettre."},

      {t:'ana', h:"Le titre : votre première ligne",
       p:"Il se recopie mot pour mot, à trois endroits.",
       mots:[['Dans le curriculum vitæ','en tête, juste sous votre nom'],['Dans l\'objet de la lettre','Objet : candidature au poste de…',true],['Dans le nom du fichier','nom-prenom-titre-du-poste.pdf']],
       say:"Objet : candidature au poste de technicienne de laboratoire, contrôle de la qualité.",
       note:"La personne qui reçoit quarante dossiers cherche ce titre des yeux. Ne le reformulez pas : recopiez-le."},

      {t:'ana', h:"« Exigé » et « atout » : deux mots, deux mondes",
       p:"C'est la distinction la plus importante d'une annonce, et beaucoup de candidats renoncent faute de la connaître.",
       mots:[['Exigé','sans ça, votre dossier est écarté'],['Atout','avec ça, vous passez devant les autres',true],['Le conseil','ne renoncez jamais à cause d\'un atout manquant']],
       say:"Exigences : diplôme d'études collégiales. Atouts : expérience du contrôle de la qualité.",
       note:"Regardez aussi « ou expérience équivalente » : cette formule vous ouvre la porte quand le diplôme vous manque."},

      {t:'ana', h:"Ce qui n'est pas écrit vaut de l'or",
       p:"Les silences d'une annonce sont vos questions au téléphone.",
       mots:[['Pas de salaire','« Quelle est l\'échelle salariale du poste ? »'],['Pas de nom de supérieur','« À qui la personne se rapporte-t-elle ? »',true],['Pas de nombre de postes','« Combien de personnes cherchez-vous ? »']],
       say:"Quelle est l'échelle salariale du poste, et à qui la personne se rapporte-t-elle ?",
       note:"Trois questions préparées transforment un appel banal en un nom qu'on retient."},

      {t:'ana', h:"La date de fin est une vraie date",
       p:"Elle ne se négocie pas, et elle se lit avec l'heure quand il y en a une.",
       mots:[['Ce qui est écrit','au plus tard le 30 novembre'],['Ce que ça veut dire','le 1er décembre, votre dossier n\'est pas lu',true],['Le bon réflexe','envoyer trois jours d\'avance']],
       say:"Faire parvenir votre curriculum vitæ au plus tard le 30 novembre.",
       note:"Un ennui d'imprimante ou un courriel refusé ne se prévoit pas. La marge de trois jours est la seule protection."},

      {t:'ex', h:"Les six lignes à surligner dans toute annonce",
       p:"À gauche ce qu'on cherche, à droite pourquoi.",
       rows:[
         ["le titre exact","il devient votre première ligne et votre objet"],
         ["les exigences","elles décident si votre dossier est lu"],
         ["les atouts","ils décident si vous passez devant"],
         ["les tâches","elles vous donnent les mots de votre lettre"],
         ["ce qui manque","cela devient vos questions au téléphone"],
         ["la date de fin","elle décide de tout le reste"],
       ]},

      {t:'piege', h:"Trois pièges",
       rows:[
         ["renoncer parce qu'un atout manque","distinguer exigé et atout",
          "Un atout manquant ne vous élimine pas. Une exigence manquante, oui — et encore, « ou expérience équivalente » ouvre souvent la porte."],
         ["traduire l'annonce dans ses propres mots","reprendre les termes de l'employeur",
          "Si l'annonce dit « conformité », écrivez « conformité ». C'est le mot que la personne cherche, et parfois le mot que le logiciel cherche."],
         ["envoyer le dernier jour","trois jours d'avance",
          "Le dossier en retard n'est pas lu, même excellent. C'est la façon la plus bête de perdre une candidature."],
       ]},

      {t:'check', h:"Est-ce que c'est clair maintenant ?",
       p:"Quatre questions rapides.",
       qs:[
         {q:"Le titre du poste doit être…", opts:["recopié mot pour mot","reformulé à votre façon"], ok:0,
          fb:"C'est ce que la personne cherche des yeux en ouvrant votre dossier."},
         {q:"Un atout qui vous manque…", opts:["ne vous élimine pas","vous élimine"], ok:0,
          fb:"Seules les exigences éliminent."},
         {q:"Une annonce sans salaire, c'est…", opts:["une question à poser","un mauvais signe"], ok:0,
          fb:"Les silences d'une annonce sont vos questions au téléphone."},
         {q:"On envoie son dossier…", opts:["trois jours avant la date","le jour même"], ok:0,
          fb:"Un ennui technique ne se prévoit pas."},
       ]},

      {t:'revoir', h:"À retenir",
       p:"Deux lectures : <b>est-ce pour moi</b>, puis <b>quels mots j'y prends</b>. Recopiez le <b>titre</b> mot pour mot. Distinguez <b>exigé</b> (éliminatoire) et <b>atout</b> (distinctif). Les <b>silences</b> de l'annonce sont vos questions au téléphone. Et envoyez <b>trois jours d'avance</b>."},
    ]
  },

  t3cliv: {
    eye:'Mini-leçon', tit:"Mettre en avant : le clivage et le pseudoclivage",
    blocs:[
      {t:'texte', h:"Le français n'insiste pas avec la voix",
       p:"En anglais, on appuie sur un mot et l'affaire est réglée. En français, ça ne marche pas : dire « c'est la RIGUEUR qui compte » en criant sonne étrange. Le français insiste en <b>déplaçant</b> : il sort le mot important de sa place ordinaire et l'encadre. Ces tournures s'appellent des phrases emphatiques, et une lettre d'accompagnement en a besoin d'au moins une par paragraphe.",
       note:"C'est aussi pour ça qu'un élève qui traduit mot à mot de l'anglais a l'air plat en français : il lui manque ce déplacement."},

      {t:'ana', h:"Le clivage du sujet : c'est… qui",
       p:"On sort le sujet et on l'encadre. Le verbe reste accordé avec le vrai sujet, pas avec « c'est ».",
       mots:[['Phrase ordinaire','La rigueur a fait mon métier.'],['Phrase clivée','C\'est la rigueur qui a fait mon métier.',true],['Au pluriel','Ce sont mes neuf années qui comptent.']],
       say:"C'est la rigueur qui a fait mon métier. Ce sont mes neuf années qui comptent.",
       note:"Devant un pluriel, on écrit « ce sont » à l'écrit soigné. À l'oral au Québec, « c'est » passe partout."},

      {t:'ana', h:"Le clivage d'un autre élément : c'est… que",
       p:"Lieu, temps, complément d'objet : tout ce qui n'est pas le sujet passe par « que ».",
       mots:[['Le lieu','C\'est à Alger que j\'ai appris ce métier.'],['Le temps','C\'est en 2016 que j\'ai pris la responsabilité du cahier.',true],['L\'objet','C\'est le contrôle de la qualité que je vise.']],
       say:"C'est à Alger que j'ai appris ce métier. C'est le contrôle de la qualité que je vise.",
       note:"Le verbe de la deuxième partie s'accorde normalement avec son sujet : « que j'ai appris », « que je vise »."},

      {t:'ana', h:"Qui ou que : une seule question",
       p:"Est-ce que l'élément mis en avant <b>fait</b> l'action du deuxième verbe ?",
       mots:[['Il la fait → qui','C\'est mon expérience qui compte.'],['Il ne la fait pas → que','C\'est mon expérience que je décris.',true],['Le test','remettez la phrase à plat et regardez qui est sujet']],
       say:"C'est mon expérience qui compte. C'est mon expérience que je décris.",
       note:"C'est exactement le même « qui / que » que dans les subordonnées relatives. Une seule règle pour deux emplois."},

      {t:'ana', h:"Le pseudoclivage : ce que… c'est",
       p:"Plus souple, et plus élégant dans une lettre : on annonce d'abord la catégorie, on révèle ensuite.",
       mots:[['Objet','Ce que j\'apporte, c\'est neuf ans de contrôle.'],['Sujet','Ce qui m\'intéresse, c\'est votre travail de transformation.',true],['Avec « de »','Ce dont je suis fière, c\'est le cahier tenu sans une erreur.']],
       say:"Ce que j'apporte, c'est neuf ans de contrôle. Ce qui m'intéresse, c'est votre travail de transformation.",
       note:"Variantes : « celui que… c'est », « là où… c'est ». Elles fonctionnent toutes sur le même modèle."},

      {t:'ana', h:"La virgule n'est pas décorative",
       p:"Dans le pseudoclivage, elle marque la pause avant la révélation. Sans elle, l'effet tombe.",
       mots:[['Avec la pause','Ce qui m\'intéresse, c\'est le contrôle de la qualité.'],['Sans la pause','Ce qui m\'intéresse c\'est le contrôle de la qualité.',true],['À l\'oral','la pause est ce qui fait tout l\'effet']],
       say:"Ce qui m'intéresse, c'est le contrôle de la qualité.",
       note:"Dans le clivage simple — « c'est… qui » — il n'y a au contraire aucune virgule."},

      {t:'labo', h:"La même phrase, quatre mises en avant",
       p:"Choisissez ce qu'on met en avant et la tournure.",
       axes:[
         {id:'e', lbl:'On met en avant quoi ?', opts:[['a','le sujet'],['b','le lieu'],['c','l\'objet'],['d','rien : phrase à plat']]},
         {id:'t', lbl:'Quelle tournure ?', opts:[['1','clivage'],['2','pseudoclivage']]}],
       out:{
         a1:{w:["c'est… qui"], say:"C'est la rigueur qui a fait l'essentiel de mon métier.", n:'le sujet est encadré par c\'est… qui'},
         a2:{w:["ce qui… c'est"], say:"Ce qui a fait l'essentiel de mon métier, c'est la rigueur.", n:'même sens, la révélation vient à la fin'},
         b1:{w:["c'est… que"], say:"C'est à Alger que j'ai appris ce métier.", n:'le lieu est encadré par c\'est… que'},
         b2:{w:["là où… c'est"], say:"Là où j'ai appris ce métier, c'est à Alger.", n:'variante avec « là où »'},
         c1:{w:["c'est… que"], say:"C'est le contrôle de la qualité que je vise.", n:'l\'objet est encadré par c\'est… que'},
         c2:{w:["ce que… c'est"], say:"Ce que je vise, c'est le contrôle de la qualité.", n:'pseudoclivage : le plus courant dans une lettre'},
         d1:{w:["à plat"], say:"La rigueur a fait l'essentiel de mon métier.", n:'correct, mais rien ne ressort'},
         d2:{w:["à plat"], say:"Je vise le contrôle de la qualité.", n:'correct, mais rien ne ressort'},
       },
       note:"Écoutez la version « à plat » en dernier : c'est elle qui montre ce que les autres apportent."},

      {t:'ex', h:"Six phrases pour une lettre",
       p:"À gauche la phrase à plat, à droite la version qui met en avant.",
       rows:[
         ["La rigueur a fait mon métier.","C'est la rigueur qui a fait mon métier."],
         ["J'ai appris ce métier à Alger.","C'est à Alger que j'ai appris ce métier."],
         ["Je vise le contrôle de la qualité.","Ce que je vise, c'est le contrôle de la qualité."],
         ["Votre travail de transformation m'intéresse.","Ce qui m'intéresse, c'est votre travail de transformation."],
         ["J'apporte neuf ans d'expérience.","Ce que j'apporte, c'est neuf ans d'expérience."],
         ["Mes neuf années comptent le plus.","Ce sont mes neuf années qui comptent le plus."],
       ]},

      {t:'piege', h:"Trois pièges",
       rows:[
         ["« c'est… que » à la place de « c'est… qui »","poser la question du sujet",
          "« C'est la rigueur que a fait mon métier » est une faute lourde. La rigueur fait l'action : donc « qui »."],
         ["oublier la virgule du pseudoclivage","marquer la pause",
          "« Ce qui m'intéresse c'est » se lit d'un trait et perd tout son effet. La virgule est l'effet."],
         ["trois clivages de suite","une par paragraphe",
          "Au-delà, la lettre sonne comme une publicité, et le lecteur cesse d'y croire. L'emphase ne se répète pas."],
       ]},

      {t:'check', h:"Est-ce que c'est clair maintenant ?",
       p:"Quatre questions rapides.",
       qs:[
         {q:"« C'est la rigueur ___ a fait mon métier. »", opts:["qui","que"], ok:0,
          fb:"La rigueur fait l'action du deuxième verbe : donc « qui »."},
         {q:"« C'est le contrôle de la qualité ___ je vise. »", opts:["que","qui"], ok:0,
          fb:"C'est « je » qui fait l'action : le complément prend « que »."},
         {q:"Dans « Ce que j'apporte, c'est… », la virgule est…", opts:["nécessaire","facultative"], ok:0,
          fb:"Elle marque la pause avant la révélation. C'est elle qui fait l'effet."},
         {q:"Dans une lettre, on met en avant…", opts:["une fois par paragraphe","à chaque phrase"], ok:0,
          fb:"Au-delà, l'emphase se retourne contre vous."},
       ]},

      {t:'revoir', h:"À retenir",
       p:"<b>C'est… qui</b> pour le sujet, <b>c'est… que</b> pour tout le reste — même règle que les relatives. <b>Ce que / ce qui / ce dont…, c'est</b> pour annoncer puis révéler, avec sa <b>virgule</b>. Une mise en avant par paragraphe, pas davantage."},
    ]
  },

  t3cond: {
    eye:'Mini-leçon', tit:"Le conditionnel de politesse dans une lettre",
    blocs:[
      {t:'texte', h:"La même demande, deux effets opposés",
       p:"« Je veux ce poste. » « Je souhaiterais poser ma candidature. » Le contenu est identique ; le premier se fait écarter, le second se fait lire. Le conditionnel met une petite distance entre vous et votre demande, et c'est cette distance qui la rend recevable. Dans une lettre d'affaires, l'indicatif brut ne passe pas pour direct : il passe pour brusque.",
       note:"Beaucoup d'élèves croient que le conditionnel affaiblit. C'est l'inverse : c'est lui qui vous fait entendre."},

      {t:'ana', h:"Comment il se forme",
       p:"Le radical du futur simple, les terminaisons de l'imparfait. Rien de plus.",
       mots:[['Le futur','j\'aimerai · je souhaiterai · je pourrai'],['Le conditionnel','j\'aimerais · je souhaiterais · je pourrais',true],['Les terminaisons','-ais, -ais, -ait, -ions, -iez, -aient']],
       say:"j'aimerais, tu aimerais, il aimerait, nous aimerions, vous aimeriez, ils aimeraient",
       note:"Si vous savez le futur d'un verbe, vous savez son conditionnel. Il n'y a pas d'irrégularité en plus."},

      {t:'ana', h:"Les six verbes d'une lettre",
       p:"Apprenez ces six-là et vous écrivez toutes vos lettres d'affaires.",
       mots:[['Demander pour soi','j\'aimerais · je souhaiterais · je voudrais'],['Demander à l\'autre','pourriez-vous · auriez-vous · voudriez-vous',true],['Se présenter','je serais disponible · il me ferait plaisir']],
       say:"Je souhaiterais poser ma candidature. Pourriez-vous me préciser la date d'entrée en fonction ?",
       note:"« Je voudrais » est la forme la plus neutre. « J'aimerais » est un peu plus chaleureux, « je souhaiterais » un peu plus formel."},

      {t:'ana', h:"À l'oreille : [ɛ], pas [e]",
       p:"C'est ce qui distingue le conditionnel du futur quand on parle, et la différence est réelle.",
       mots:[['Futur','je voudrai — [ʒə vudʁe]'],['Conditionnel','je voudrais — [ʒə vudʁɛ]',true],['Le repère','la bouche s\'ouvre davantage au conditionnel']],
       say:"je voudrai, je voudrais",
       note:"Beaucoup de Québécois font aussi cette distinction à l'oral. Au téléphone, elle s'entend."},

      {t:'ana', h:"Le piège du « si »",
       p:"Jamais de conditionnel après « si » d'hypothèse. C'est la faute la plus fréquente, et elle se voit tout de suite.",
       mots:[['Correct','Si j\'étais retenue, je serais disponible en janvier.'],['Incorrect','Si je serais retenue, je serais disponible.',true],['La règle','imparfait après « si », conditionnel dans l\'autre moitié']],
       say:"Si j'étais retenue, je serais disponible en janvier.",
       note:"Astuce mnémotechnique : les deux « rais » ne se rencontrent jamais de part et d'autre d'un « si »."},

      {t:'labo', h:"Brusque, ou reçu",
       p:"Choisissez une demande et un ton.",
       axes:[
         {id:'d', lbl:'Quelle demande ?', opts:[['a','poser sa candidature'],['b','demander une rencontre'],['c','demander un renseignement']]},
         {id:'t', lbl:'Quel ton ?', opts:[['1','indicatif'],['2','conditionnel']]}],
       out:{
         a1:{w:["indicatif"], say:"Je veux poser ma candidature au poste de technicienne de laboratoire.", n:'correct grammaticalement, brusque dans une lettre'},
         a2:{w:["conditionnel"], say:"Je souhaiterais poser ma candidature au poste de technicienne de laboratoire.", n:'la forme attendue dans une lettre d\'affaires'},
         b1:{w:["indicatif"], say:"Je veux vous rencontrer la semaine prochaine.", n:'on dirait un ordre'},
         b2:{w:["conditionnel"], say:"J'aimerais vous rencontrer la semaine prochaine.", n:'la demande reste ferme, le ton est juste'},
         c1:{w:["indicatif"], say:"Pouvez-vous me dire la date d'entrée en fonction ?", n:'acceptable au téléphone, sec par écrit'},
         c2:{w:["conditionnel"], say:"Pourriez-vous me préciser la date d'entrée en fonction ?", n:'la forme écrite'},
       },
       note:"Écoutez la version 1 puis la version 2. Le contenu ne change pas ; c'est vous qui changez d'image."},

      {t:'ex', h:"Huit formules pour une lettre",
       p:"À gauche la formule, à droite où elle sert.",
       rows:[
         ["Je souhaiterais poser ma candidature","premier paragraphe : ce que vous demandez"],
         ["J'aimerais vous rencontrer","dernier paragraphe : la demande de rencontre"],
         ["Pourriez-vous me préciser…","une question sur le poste"],
         ["Auriez-vous l'obligeance de…","une demande un peu plus appuyée"],
         ["Je serais disponible dès janvier","votre disponibilité"],
         ["Il me ferait plaisir de vous fournir mes références","une offre de votre part"],
         ["Je voudrais savoir si…","une question directe, ton neutre"],
         ["Si j'étais retenue, je pourrais…","une hypothèse : imparfait puis conditionnel"],
       ]},

      {t:'piege', h:"Trois pièges",
       rows:[
         ["« si je serais »","si j'étais",
          "Après « si » d'hypothèse : imparfait. Le conditionnel va dans l'autre moitié de la phrase."],
         ["croire que le conditionnel affaiblit","c'est lui qui fait lire",
          "Dans une lettre d'affaires, l'indicatif brut se lit comme une exigence. Le conditionnel est la forme normale, pas une timidité."],
         ["mélanger les tons","tenir le même du début à la fin",
          "On ne commence pas par « Je souhaiterais » pour finir par « à bientôt ! ». Le ton d'une lettre se choisit une fois."],
       ]},

      {t:'check', h:"Est-ce que c'est clair maintenant ?",
       p:"Quatre questions rapides.",
       qs:[
         {q:"« Si j'___ retenue, je serais disponible. »", opts:["étais","serais"], ok:0,
          fb:"Imparfait après « si », conditionnel dans l'autre moitié."},
         {q:"Le conditionnel se forme avec…", opts:["le radical du futur","le radical de l'imparfait"], ok:0,
          fb:"Radical du futur, terminaisons de l'imparfait."},
         {q:"Dans une lettre, « je veux ce poste »…", opts:["se lit comme une exigence","est la forme normale"], ok:0,
          fb:"Le conditionnel est ce qu'on attend d'une lettre d'affaires."},
         {q:"« je voudrais » se prononce…", opts:["[ʒə vudʁɛ]","[ʒə vudʁe]"], ok:0,
          fb:"[ɛ] au conditionnel, [e] au futur. La différence s'entend."},
       ]},

      {t:'revoir', h:"À retenir",
       p:"<b>Radical du futur + terminaisons de l'imparfait</b>. Six verbes suffisent : aimerais, souhaiterais, voudrais, pourriez-vous, auriez-vous, serais. Jamais de conditionnel <b>après « si »</b> d'hypothèse. Et le ton, une fois choisi, se tient du début à la fin."},
    ]
  },

  t3subj: {
    eye:'Mini-leçon', tit:"Le subjonctif après pour que et avant que",
    blocs:[
      {t:'texte', h:"Deux conjonctions qui ne laissent aucun choix",
       p:"Il y a beaucoup de cas où le subjonctif est une question de nuance et où l'indicatif reste possible. <b>Pour que</b> et <b>avant que</b> n'en font pas partie : après elles, le subjonctif est obligatoire, et l'indicatif est une faute. Bonne nouvelle : deux conjonctions, une seule règle, aucune exception à retenir.",
       note:"Ce sont aussi les deux dont une lettre d'accompagnement a le plus besoin : le but, et l'échéance."},

      {t:'ana', h:"Comment il se forme, en trois gestes",
       p:"Partez de la troisième personne du pluriel du présent, et rien d'autre.",
       mots:[['1. Prenez « ils »','ils finiss-ent · ils reçoiv-ent · ils perd-ent'],['2. Enlevez « -ent »','finiss- · reçoiv- · perd-',true],['3. Ajoutez','-e, -es, -e, -ions, -iez, -ent']],
       say:"que je finisse, que tu finisses, qu'il finisse, que nous finissions, que vous finissiez, qu'ils finissent",
       note:"Pour « nous » et « vous », le subjonctif ressemble à l'imparfait : que nous finissions, que vous finissiez."},

      {t:'ana', h:"Les quatre irréguliers d'une lettre",
       p:"Ils ne suivent pas la recette. Ce sont précisément ceux dont vous aurez besoin.",
       mots:[['être','que je sois · que vous soyez'],['avoir','que j\'aie · que vous ayez',true],['faire et pouvoir','que je fasse · que vous fassiez · que je puisse · que vous puissiez']],
       say:"que vous ayez, que vous soyez, que vous fassiez, que vous puissiez",
       note:"« que vous ayez » ne se prononce pas comme « vous avez ». Écoutez : [kə vu zɛje] contre [vu zave]."},

      {t:'ana', h:"Le but : pour, ou pour que",
       p:"Tout dépend du nombre de sujets. C'est le piège central de cette leçon.",
       mots:[['Un seul sujet','Je téléphone pour obtenir des précisions.'],['Deux sujets','Je téléphone pour que vous ayez mon nom en tête.',true],['La règle','même sujet → pour + infinitif ; sujets différents → pour que + subjonctif']],
       say:"Je téléphone pour obtenir des précisions. Je téléphone pour que vous ayez mon nom en tête.",
       note:"« Je téléphone pour que j'obtienne des précisions » est une faute : même sujet, donc infinitif."},

      {t:'ana', h:"Le temps : avant de, ou avant que",
       p:"Exactement la même logique, et exactement le même piège.",
       mots:[['Un seul sujet','Je vous appelle avant d\'envoyer mon dossier.'],['Deux sujets','Je vous appelle avant que le poste soit comblé.',true],['La règle','même sujet → avant de + infinitif ; sujets différents → avant que + subjonctif']],
       say:"Je vous appelle avant d'envoyer mon dossier. Je vous appelle avant que le poste soit comblé.",
       note:"Attention : « après que » demande l'indicatif, pas le subjonctif. Ce n'est pas symétrique, et personne ne sait pourquoi."},

      {t:'ana', h:"Le « ne » qui ne nie rien",
       p:"On lit parfois un « ne » après « avant que ». Il n'a aucun sens négatif.",
       mots:[['Avec','avant que le poste ne soit comblé'],['Sans','avant que le poste soit comblé',true],['Le sens','identique — la phrase reste positive']],
       say:"Je vous appelle avant que le poste ne soit comblé.",
       note:"On l'appelle le « ne » explétif. Vous pouvez l'écrire ou l'omettre ; ne le lisez jamais comme une négation."},

      {t:'labo', h:"Un sujet ou deux ?",
       p:"Choisissez une conjonction et un nombre de sujets.",
       axes:[
         {id:'c', lbl:'Quelle conjonction ?', opts:[['a','le but'],['b','le temps']]},
         {id:'s', lbl:'Combien de sujets ?', opts:[['1','un seul'],['2','deux']]}],
       out:{
         a1:{w:["pour + infinitif"], say:"Je téléphone pour obtenir des précisions sur le poste.", n:'un seul sujet : « je » téléphone et « je » obtiens'},
         a2:{w:["pour que + subjonctif"], say:"Je joins mes attestations pour que vous puissiez vérifier mes années de service.", n:'deux sujets : « je » joins, « vous » vérifiez'},
         b1:{w:["avant de + infinitif"], say:"Je vous appelle avant d'envoyer mon dossier.", n:'un seul sujet : « je » appelle et « je » envoie'},
         b2:{w:["avant que + subjonctif"], say:"Je vous appelle avant que le poste ne soit comblé.", n:'deux sujets : « je » appelle, « le poste » est comblé'},
       },
       note:"Écoutez la structure : dès qu'un deuxième sujet apparaît, la conjonction change et le subjonctif arrive."},

      {t:'ex', h:"Six phrases pour une lettre",
       p:"À gauche la phrase, à droite ce qu'elle fait.",
       rows:[
         ["pour que vous ayez mon dossier avant la fin du mois","le but, deux sujets"],
         ["pour obtenir des précisions sur l'horaire","le but, un seul sujet"],
         ["avant que le poste ne soit comblé","l'échéance, deux sujets"],
         ["avant d'envoyer mon curriculum vitæ","l'échéance, un seul sujet"],
         ["pour que la lecture soit rapide","le but : ce que vous voulez pour le lecteur"],
         ["avant que le quart de jour ne reprenne en janvier","une date que vous respectez"],
       ]},

      {t:'piege', h:"Trois pièges",
       rows:[
         ["« pour que » avec un seul sujet","pour + infinitif",
          "« Je téléphone pour que j'obtienne » est une faute. Même sujet : « pour obtenir »."],
         ["« après que » au subjonctif","après que + indicatif",
          "La symétrie est trompeuse : « avant que » demande le subjonctif, « après que » demande l'indicatif."],
         ["lire le « ne » comme une négation","c'est un « ne » explétif",
          "« Avant que le poste ne soit comblé » ne veut pas dire qu'il ne sera pas comblé."],
       ]},

      {t:'check', h:"Est-ce que c'est clair maintenant ?",
       p:"Quatre questions rapides.",
       qs:[
         {q:"« Je joins mes attestations pour que vous ___ vérifier. »", opts:["puissiez","pouvez"], ok:0,
          fb:"Après « pour que », le subjonctif est obligatoire."},
         {q:"Avec un seul sujet, on écrit…", opts:["pour + infinitif","pour que + subjonctif"], ok:0,
          fb:"« Je téléphone pour obtenir des précisions. »"},
         {q:"Après « après que », on met…", opts:["l'indicatif","le subjonctif"], ok:0,
          fb:"Ce n'est pas symétrique avec « avant que »."},
         {q:"Le « ne » de « avant que le poste ne soit comblé »…", opts:["ne nie rien","rend la phrase négative"], ok:0,
          fb:"C'est un « ne » explétif : ornemental et facultatif."},
       ]},

      {t:'revoir', h:"À retenir",
       p:"Après <b>pour que</b> et <b>avant que</b>, subjonctif obligatoire. Mais avec un <b>seul sujet</b>, on n'emploie ni l'une ni l'autre : <b>pour + infinitif</b>, <b>avant de + infinitif</b>. Quatre irréguliers à savoir : <b>que vous ayez, soyez, fassiez, puissiez</b>. Et « après que » prend l'indicatif."},
    ]
  },

  t3cv: {
    eye:'Mini-leçon', tit:"La mise en page d'un curriculum vitæ",
    blocs:[
      {t:'texte', h:"On ne lit pas un curriculum vitæ, on le balaie",
       p:"La personne qui reçoit quarante dossiers accorde d'abord une vingtaine de secondes à chacun. Elle ne lit pas : elle balaie le haut de la page pour décider si elle lira. Toute la mise en page découle de ce fait unique. Ce qui vous sert le plus doit être le plus haut, et ce qui ne sert pas doit disparaître — pas être écrit plus petit.",
       note:"Ce n'est pas une question de goût : c'est une question de vitesse de lecture."},

      {t:'ana', h:"L'ordre des rubriques n'est pas décoratif",
       p:"L'ordre habituel n'est pas obligatoire. Pour un changement de métier, il vous dessert.",
       mots:[['Ordre habituel','en-tête · profil · expérience récente · formation'],['Ordre pour un retour au métier','en-tête · titre du poste · expérience pertinente · autre expérience · formation',true],['Le principe','le plus utile en haut, pas le plus récent']],
       say:"Expérience pertinente d'abord, autre expérience professionnelle ensuite.",
       note:"Vous n'inventez rien et vous ne cachez rien : vous rangez. Tant que les dates y sont et qu'elles sont exactes, l'ordre vous appartient."},

      {t:'ana', h:"Une ou deux pages, jamais trois",
       p:"La troisième page ne se lit pas : elle se devine, et elle donne l'impression que vous ne savez pas choisir.",
       mots:[['Moins de cinq ans d\'expérience','une page'],['Cinq à vingt ans','deux pages',true],['Plus de vingt ans','toujours deux pages — on résume le début']],
       say:"Deux pages pour quinze ans de carrière, une seule en dessous de cinq ans.",
       note:"Les emplois les plus anciens tiennent en une ligne chacun : intitulé, employeur, dates. Rien de plus."},

      {t:'ana', h:"Les dates : à droite, alignées, dans un seul format",
       p:"C'est ce qui se voit avant même que le texte soit lu.",
       mots:[['Format court','2016-2025 · 2011-2016 · 2009-2011'],['Format long','mars 2016 – juin 2025',true],['La règle','le même format partout, aligné au même endroit']],
       say:"deux mille seize à deux mille vingt-cinq",
       note:"Un alignement irrégulier donne une impression de négligence en une demi-seconde, avant tout jugement sur le contenu."},

      {t:'ana', h:"Trois tâches par emploi, et un chiffre",
       p:"Pas dix tâches. Trois, choisies parce qu'elles se rattachent au poste visé.",
       mots:[['Trop vague','Responsable des analyses.'],['Précis','Analyses de conformité sur quarante lots par semaine.',true],['Le principe','un chiffre vaut trois adjectifs']],
       say:"Analyses de conformité sur quarante lots par semaine. Tenue du cahier de laboratoire. Formation de deux nouvelles techniciennes.",
       note:"Le chiffre n'a pas besoin d'être impressionnant : il a besoin d'être vrai et vérifiable."},

      {t:'texte', h:"Ce qu'on n'y met plus",
       p:"Ni photographie, ni date de naissance, ni état civil, ni nombre d'enfants, ni numéro d'assurance sociale. Ce n'est pas une question de mode : ce sont des renseignements qu'un employeur n'a pas à demander avant l'embauche, et les inscrire de vous-même n'aide personne. Pour les <b>références</b>, la mention « fournies sur demande » suffit — et on ne donne les coordonnées de quelqu'un qu'après lui avoir demandé la permission.",
       note:"Une adresse complète n'est plus nécessaire non plus : la ville suffit, avec le téléphone et le courriel."},

      {t:'texte', h:"Le nom du fichier compte aussi",
       p:"Il apparaît dans la boîte de réception avant votre nom, et il reste dans le dossier de l'employeur pendant des mois. « cv-final-2.pdf » se perd et fait mauvais effet. « zerouali-hafida-technicienne-laboratoire.pdf » se retrouve d'un coup d'œil. Envoyez en PDF, jamais dans un format qui se déforme d'un ordinateur à l'autre.",
       note:"Le même soin vaut pour l'adresse courriel : une adresse sérieuse, avec votre nom, et pas celle que vous aviez à dix-huit ans."},

      {t:'ex', h:"Les sept rubriques, dans l'ordre",
       p:"À gauche la rubrique, à droite ce qu'on y met.",
       rows:[
         ["En-tête","nom, téléphone, courriel, ville — rien d'autre"],
         ["Titre","le titre exact du poste affiché, mot pour mot"],
         ["Profil","trois lignes : années d'expérience et spécialité"],
         ["Expérience pertinente","les emplois liés au poste, trois tâches chacun"],
         ["Autre expérience professionnelle","les autres, une ligne chacun, avec les dates"],
         ["Formation","les diplômes, du plus récent au plus ancien"],
         ["Références","« fournies sur demande » — et rien de plus"],
       ]},

      {t:'piege', h:"Trois pièges",
       rows:[
         ["l'ordre chronologique à tout prix","l'ordre de l'utilité",
          "Votre expérience la plus récente n'est pas forcément la plus pertinente. Deux blocs règlent le problème sans rien cacher."],
         ["écrire plus petit pour tout faire entrer","enlever",
          "Un corps de texte réduit à huit points ne se lit pas. Ce qui ne sert pas au poste visé se retire, il ne se rétrécit pas."],
         ["« cv.pdf »","nom-prenom-titre.pdf",
          "Le nom du fichier est la première chose que l'employeur voit, et la dernière qui reste dans son dossier."],
       ]},

      {t:'check', h:"Est-ce que c'est clair maintenant ?",
       p:"Quatre questions rapides.",
       qs:[
         {q:"Pour un retour à son métier, on place en premier…", opts:["l'expérience pertinente","l'expérience la plus récente"], ok:0,
          fb:"Deux blocs : pertinente d'abord, autre expérience ensuite."},
         {q:"Un curriculum vitæ fait au maximum…", opts:["deux pages","trois pages"], ok:0,
          fb:"La troisième ne se lit pas."},
         {q:"Pour décrire une tâche, il vaut mieux…", opts:["un chiffre","trois adjectifs"], ok:0,
          fb:"« Quarante lots par semaine » vaut mieux que « responsable des analyses »."},
         {q:"Pour les références, on écrit…", opts:["fournies sur demande","les coordonnées complètes"], ok:0,
          fb:"Et on demande la permission avant de donner le nom de quelqu'un."},
       ]},

      {t:'revoir', h:"À retenir",
       p:"On <b>balaie</b> un curriculum vitæ : le plus utile en haut. <b>Deux blocs d'expérience</b> quand on revient à son métier. <b>Une ou deux pages</b>, dates alignées dans un seul format, <b>trois tâches et un chiffre</b> par emploi. Ni photo, ni date de naissance. Références « fournies sur demande », et un nom de fichier qui vous nomme."},
    ]
  },

};
