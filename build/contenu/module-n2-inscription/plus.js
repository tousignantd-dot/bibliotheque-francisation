const PLUS = {
  prAlpha: {
    eye:'Mini-leçon', tit:"Épeler son nom sans se tromper",
    blocs:[
      {t:'texte', h:"Un nom mal écrit suit une personne des années",
       p:"Au secrétariat, personne ne connaît ton nom. La personne qui l'écrit l'entend pour la première fois. Si elle met un <b>B</b> au lieu d'un <b>D</b>, ton nom restera faux sur tous les papiers du centre. Épeler, c'est dire ton nom une lettre à la fois pour qu'il soit écrit juste.",
       note:"Insister sur l'enjeu : ce n'est pas un exercice d'alphabet, c'est une réparation qui coûte cher si elle n'est pas faite tout de suite."},

      {t:'ana', h:"La famille du son « é » : la lettre vient avant",
       p:"Sept lettres se disent avec le son « é » à la fin.",
       mots:[["On dit","{B} — « bé »"],["Aussi","{C} · {D} · {G}"],["Aussi","{P} · {T} · {V}"],["On ne dit pas","« èb » ni « èd » : le son vient après",true]],
       say:"Bé. Cé. Dé. Gé. Pé. Té. Vé.",
       note:"Les faire répéter en série, dans l'ordre donné. C'est la moitié des lettres difficiles du niveau."},

      {t:'ana', h:"La famille du son « è » : la lettre vient après",
       p:"Six lettres commencent par le son « è ».",
       mots:[["On dit","{F} — « èf »"],["Aussi","{L} · {M} · {N}"],["Aussi","{R} · {S}"],["On ne dit pas","« fé » ni « mé » : le son vient avant",true]],
       say:"Èf. Èl. Èm. Èn. Èr. Ès.",
       note:"Faire remarquer la bouche : dans cette famille, on ouvre d'abord, on ferme ensuite."},

      {t:'ana', h:"Les quatre paires qui font écrire faux",
       p:"Au téléphone comme au comptoir, ce sont toujours les mêmes.",
       mots:[["B et V","{B} comme bonjour · {V} comme vendredi"],["M et N","{M} comme merci · {N} comme novembre"],["G et J","{G} comme gare · {J} comme jeudi"],["E et I","{E} comme école · {I} comme immeuble"],["On ne répète pas la lettre seule","On ajoute un mot connu, c'est plus sûr",true]],
       say:"B comme bonjour. V comme vendredi. M comme merci. N comme novembre.",
       note:"Faire choisir à chacun un mot pour B, V, M et N, et le garder toute l'année. Un mot familier vaut mieux qu'un mot juste."},

      {t:'labo', h:"Écoute la lettre",
       p:"Choisis une famille et une lettre.",
       axes:[
         {id:'p', lbl:'Quelle famille ?', opts:[
           ['a','le son « é »'],
           ['b','le son « è »'],
           ['c','les paires du comptoir']]},
         {id:'q', lbl:'Laquelle ?', opts:[['1','la première'],['2','la deuxième'],['3','les deux, à la suite']]}],
       out:{
         a1:{w:["B"], say:"La lettre B.", n:'« bé » — la lettre vient avant le son'},
         a2:{w:["D"], say:"La lettre D.", n:'« dé » — même famille que B'},
         a3:{w:["B, D"], say:"La lettre B. La lettre D.", n:'deux lettres proches, une seule consonne les sépare'},
         b1:{w:["F"], say:"La lettre F.", n:'« èf » — le son vient avant la lettre'},
         b2:{w:["M"], say:"La lettre M.", n:'« èm » — même famille que F'},
         b3:{w:["F, M"], say:"La lettre F. La lettre M.", n:'les deux commencent par « è »'},
         c1:{w:["B comme bonjour"], say:"B comme bonjour.", n:'la façon la plus sûre de donner un B'},
         c2:{w:["V comme vendredi"], say:"V comme vendredi.", n:'et voilà le V, sans erreur possible'},
         c3:{w:["B comme bonjour, V comme vendredi"], say:"B comme bonjour. V comme vendredi.", n:'la paire qui sauve le plus de formulaires'},
       },
       note:"Neuf extraits. Les faire écouter les yeux fermés, puis écrire la lettre entendue."},

      {t:'ex', h:"À écouter et à répéter",
       p:"Six façons de faire écrire son nom.",
       rows:[
         ["Comment ça s'écrit ?","la question que la secrétaire pose"],
         ["Vous pouvez épeler ?","la même question, plus polie"],
         ["Doucement, s'il vous plaît.","quand on va trop vite"],
         ["Il y a deux D.","pour une lettre double"],
         ["D comme dimanche.","quand la personne hésite"],
         ["C'est bien écrit ?","la vérification finale"],
       ]},

      {t:'piege', h:"Trois pièges à connaître",
       rows:[
         ["épeler trop vite","une lettre par seconde",
          "La personne écrit pendant que tu parles. Une lettre, une seconde. Si elle s'arrête, tu t'arrêtes aussi."],
         ["dire la lettre à l'anglaise","tu es au Québec",
          "En anglais, le E se dit « i » et le I se dit « aïe ». En français, le E se dit « eu » et le I se dit « i ». Une seule lettre, deux noms : c'est l'erreur la plus fréquente au comptoir."],
         ["ne pas vérifier à la fin","demande à voir",
          "« C'est bien écrit ? » prend deux secondes. Corriger un nom dans un dossier prend une semaine."],
       ]},

      {t:'check', h:"Est-ce que c'est clair maintenant ?",
       p:"Quatre questions rapides.",
       qs:[
         {q:"La lettre B se dit…", opts:["« bé »","« èb »"], ok:0,
          fb:"B, C, D, G, P, T, V : la lettre vient avant le son « é »."},
         {q:"La lettre M se dit…", opts:["« èm »","« mé »"], ok:0,
          fb:"F, L, M, N, R, S : le son « è » vient avant la lettre."},
         {q:"Quand la personne hésite entre B et V, tu dis…", opts:["« B comme bonjour »","« B, B, B »"], ok:0,
          fb:"Un mot connu enlève tout doute. Répéter la lettre n'en enlève aucun."},
         {q:"À la fin, tu…", opts:["vérifies ce qui est écrit","pars tout de suite"], ok:0,
          fb:"« C'est bien écrit ? » — c'est ce que fait Yara avec madame Bourgeois."},
       ]},
    ]
  },

  prQuel: {
    eye:'Mini-leçon', tit:"Les questions qu'on te pose au comptoir",
    blocs:[
      {t:'texte', h:"Six questions, toujours les mêmes",
       p:"Une inscription, c'est six questions courtes. Elles reviennent au secrétariat, à la clinique, à la banque : <b>quel est votre nom ?</b>, <b>quelle est votre adresse ?</b>, et ainsi de suite. Quand on les reconnaît, on n'a plus besoin de tout comprendre pour répondre.",
       note:"Faire écouter les six questions avant toute explication de grammaire. La reconnaissance vient d'abord ; l'accord vient après."},

      {t:'ana', h:"Devant un mot masculin : quel",
       p:"On écrit « quel » quand le mot qui suit est masculin.",
       mots:[["On dit","{Quel} est votre nom ?"],["Aussi","{Quel} est votre prénom ?"],["Aussi","{Quel} est votre courriel ?"],["On ne dit pas","« Quelle est votre nom ? »",true]],
       say:"Quel est votre nom ? Quel est votre prénom ?",
       note:"Le masculin : nom, prénom, courriel, numéro, téléphone, cours, local."},

      {t:'ana', h:"Devant un mot féminin : quelle",
       p:"On écrit « quelle » quand le mot qui suit est féminin.",
       mots:[["On dit","{Quelle} est votre adresse ?"],["Aussi","{Quelle} est votre date de naissance ?"],["Aussi","{Quelle} est votre scolarité ?"],["Attention","à l'oreille, quel et quelle se disent pareil"]],
       say:"Quelle est votre adresse ? Quelle est votre date de naissance ?",
       note:"Le féminin : adresse, date, ville, rue, heure, scolarité, signature. Faire apprendre les deux listes comme des blocs."},

      {t:'ana', h:"La version courte, celle qu'on entend vraiment",
       p:"Au comptoir, la question tombe souvent sans « quel ».",
       mots:[["On dit","{Votre nom}, s'il vous plaît."],["Aussi","{Votre adresse} ?"],["Aussi","{Vous habitez où} ?"],["Réponse possible","Trois ou quatre mots suffisent"]],
       say:"Votre nom, s'il vous plaît. Votre adresse ?",
       note:"C'est la forme la plus fréquente. La reconnaître évite de rester muet devant une question qu'on croyait connaître."},

      {t:'labo', h:"Pose la question",
       p:"Choisis un renseignement et une façon de demander.",
       axes:[
         {id:'p', lbl:'Quel renseignement ?', opts:[
           ['a','le nom'],
           ['b',"l'adresse"],
           ['c','la date de naissance'],
           ['d','le téléphone']]},
         {id:'q', lbl:'Comment ?', opts:[['1','la question complète'],['2','la version courte'],['3','la réponse']]}],
       out:{
         a1:{w:["Quel est votre nom ?"], say:"Quel est votre nom ?", n:'nom est masculin : quel'},
         a2:{w:["Votre nom, s'il vous plaît."], say:"Votre nom, s'il vous plaît.", n:'la forme du comptoir'},
         a3:{w:["Haddad. H, A, deux D, A, D."], say:"Haddad. H, A, deux D, A, D.", n:'on répond, puis on épelle'},
         b1:{w:["Quelle est votre adresse ?"], say:"Quelle est votre adresse ?", n:'adresse est féminin : quelle'},
         b2:{w:["Votre adresse ?"], say:"Votre adresse ?", n:'deux mots suffisent'},
         b3:{w:["3420, rue Papineau, à Montréal."], say:"3420, rue Papineau, à Montréal.", n:'le numéro, la rue, la ville'},
         c1:{w:["Quelle est votre date de naissance ?"], say:"Quelle est votre date de naissance ?", n:'date est féminin : quelle'},
         c2:{w:["Vous êtes né quand ?"], say:"Vous êtes né quand ?", n:'très courant à l’oral'},
         c3:{w:["Le 7 mars 1994."], say:"Le 7 mars 1994.", n:'le jour, le mois, l’année'},
         d1:{w:["Quel est votre numéro de téléphone ?"], say:"Quel est votre numéro de téléphone ?", n:'numéro est masculin : quel'},
         d2:{w:["Votre téléphone ?"], say:"Votre téléphone ?", n:'la forme la plus courte'},
         d3:{w:["514 555-0182."], say:"5 1 4. 5 5 5. 0 1 8 2.", n:'dix chiffres, dits par petits groupes'},
       },
       note:"Douze extraits. Faire jouer la paire question-réponse debout, deux par deux."},

      {t:'ex', h:"À écouter et à répéter",
       p:"Les six questions de l'inscription.",
       rows:[
         ["Quel est votre nom de famille ?","la première case"],
         ["Quel est votre prénom ?","la deuxième"],
         ["Quelle est votre date de naissance ?","année, mois, jour"],
         ["Quelle est votre adresse ?","numéro, rue, ville"],
         ["Quel est votre numéro de téléphone ?","dix chiffres"],
         ["Quelle est votre scolarité ?","le nombre d'années d'école"],
       ]},

      {t:'piege', h:"Trois pièges à connaître",
       rows:[
         ["chercher la différence à l'oreille","il n'y en a pas",
          "« Quel » et « quelle » se disent exactement pareil. La différence ne se voit qu'à l'écrit. Inutile de tendre l'oreille : il faut connaître le mot qui suit."],
         ["répondre par une phrase entière","trois mots suffisent",
          "« Quel est votre prénom ? » — « Yara. » C'est une réponse complète et polie. Une phrase entière n'est pas plus juste, elle est seulement plus longue."],
         ["ne rien dire quand on n'a pas compris","dis-le",
          "« Pouvez-vous répéter, s'il vous plaît ? » fait partie du français, pas de l'échec. La personne au comptoir répète tous les jours."],
       ]},

      {t:'check', h:"Est-ce que c'est clair maintenant ?",
       p:"Quatre questions rapides.",
       qs:[
         {q:"« ___ est votre adresse ? »", opts:["Quelle","Quel"], ok:0,
          fb:"Adresse est un mot féminin : quelle."},
         {q:"« ___ est votre prénom ? »", opts:["Quel","Quelle"], ok:0,
          fb:"Prénom est un mot masculin : quel."},
         {q:"Quel et quelle se prononcent…", opts:["de la même façon","de deux façons"], ok:0,
          fb:"Les deux se disent « kèl ». Seule l'écriture change."},
         {q:"Une bonne réponse au comptoir fait…", opts:["trois ou quatre mots","une phrase complète"], ok:0,
          fb:"Court et clair. C'est ce que fait Yara : « Haddad. »"},
       ]},
    ]
  },

  t1date: {
    eye:'Mini-leçon', tit:"Lire une date écrite en chiffres",
    blocs:[
      {t:'texte', h:"Une date, trois façons de l'écrire",
       p:"L'annonce dit <b>le 7 septembre</b>. Le formulaire demande <b>2026-09-07</b>. Le reçu porte <b>07/09/2026</b>. Ce sont trois écritures du même jour. Savoir passer de l'une à l'autre, c'est ne plus se tromper de semaine.",
       note:"Apporter en classe un vrai formulaire, un vrai reçu et un vrai calendrier : les trois formes se rencontrent le même jour dans la vraie vie."},

      {t:'ana', h:"La date en toutes lettres",
       p:"C'est celle des annonces et des affiches.",
       mots:[["On écrit","le 7 {septembre} 2026"],["Aussi","le 11 {décembre} 2026"],["Le mois ne prend pas de majuscule","{septembre}, pas « Septembre »"],["On ne dit pas","« le septembre 7 » : le jour vient avant",true]],
       say:"Le 7 septembre 2026. Le 11 décembre 2026.",
       note:"Faire écrire les douze mois au tableau, en petites lettres. La majuscule est l'erreur la plus fréquente et vient de l'anglais."},

      {t:'ana', h:"La date avec des barres",
       p:"C'est celle des reçus et des chèques : jour, mois, année.",
       mots:[["On écrit","{07/09/2026} — le 7 septembre"],["Aussi","{24/08/2026} — le 24 août"],["Le nombre du milieu","c'est toujours le mois"],["On ne lit pas","« le 9 juillet » : le premier nombre est le jour",true]],
       say:"Zéro sept, zéro neuf, deux mille vingt-six.",
       note:"Faire remarquer que le nombre du milieu ne dépasse jamais 12. C'est le seul repère dont un débutant a besoin."},

      {t:'ana', h:"La date des papiers officiels",
       p:"Année, mois, jour. C'est la forme des formulaires du gouvernement.",
       mots:[["On écrit","{2026-09-07} — le 7 septembre 2026"],["Aussi","{1994-03-07} — le 7 mars 1994"],["L'année vient en premier","quatre chiffres, puis deux, puis deux"],["Le mois reste au milieu","c'est la seule chose qui ne bouge jamais"]],
       say:"Deux mille vingt-six, zéro neuf, zéro sept.",
       note:"C'est la forme demandée dans la case « date de naissance » du module. La faire écrire par chacun avec sa vraie date."},

      {t:'labo', h:"Passe d'une forme à l'autre",
       p:"Choisis une date et une écriture.",
       axes:[
         {id:'p', lbl:'Quelle date ?', opts:[
           ['a','le premier cours'],
           ['b','le dernier cours'],
           ["c","l'inscription"],
           ['d','la naissance de Yara']]},
         {id:'q', lbl:'Quelle écriture ?', opts:[['1','en toutes lettres'],['2','avec des barres'],['3','année, mois, jour']]}],
       out:{
         a1:{w:["le 7 septembre 2026"], say:"Le 7 septembre 2026.", n:'la forme de l’annonce'},
         a2:{w:["07/09/2026"], say:"Zéro sept, barre, zéro neuf, barre, deux mille vingt-six.", n:'jour, mois, année'},
         a3:{w:["2026-09-07"], say:"Deux mille vingt-six, zéro neuf, zéro sept.", n:'la forme du formulaire'},
         b1:{w:["le 11 décembre 2026"], say:"Le 11 décembre 2026.", n:'le dernier jour du cours'},
         b2:{w:["11/12/2026"], say:"Onze, barre, douze, barre, deux mille vingt-six.", n:'attention : 11 est le jour, 12 est le mois'},
         b3:{w:["2026-12-11"], say:"Deux mille vingt-six, douze, onze.", n:'les mêmes chiffres, l’ordre inverse'},
         c1:{w:["du 24 au 28 août 2026"], say:"Du 24 au 28 août 2026.", n:'cinq jours d’inscription'},
         c2:{w:["24/08/2026"], say:"Vingt-quatre, barre, zéro huit, barre, deux mille vingt-six.", n:'le premier jour seulement'},
         c3:{w:["2026-08-24"], say:"Deux mille vingt-six, zéro huit, vingt-quatre.", n:'la forme des papiers'},
         d1:{w:["le 7 mars 1994"], say:"Le 7 mars 1994.", n:'la date de naissance de Yara'},
         d2:{w:["07/03/1994"], say:"Zéro sept, barre, zéro trois, barre, mille neuf cent quatre-vingt-quatorze.", n:'mars est le troisième mois'},
         d3:{w:["1994-03-07"], say:"Mille neuf cent quatre-vingt-quatorze, zéro trois, zéro sept.", n:'ce que Yara écrit dans sa case'},
       },
       note:"Douze extraits. Faire écrire sa propre date de naissance dans les trois formes, sur une seule ligne."},

      {t:'ex', h:"À écouter et à répéter",
       p:"Les douze mois de l'année.",
       rows:[
         ["janvier, février, mars","01, 02, 03"],
         ["avril, mai, juin","04, 05, 06"],
         ["juillet, août, septembre","07, 08, 09"],
         ["octobre, novembre, décembre","10, 11, 12"],
         ["le 7 septembre","le premier jour du cours"],
         ["le 11 décembre","le dernier jour du cours"],
       ]},

      {t:'piege', h:"Trois pièges à connaître",
       rows:[
         ["lire 07/09 comme « le 9 juillet »","le jour vient en premier",
          "Au Québec, dans cette écriture, le premier nombre est le jour et le deuxième est le mois. C'est l'inverse de l'habitude américaine, et ça change tout : sept septembre, pas neuf juillet."],
         ["écrire le mois avec une majuscule","les mois sont en petites lettres",
          "On écrit <b>le 7 septembre</b>, jamais « le 7 Septembre ». Les noms de mois et les jours de la semaine ne prennent pas de majuscule en français."],
         ["recopier une date sans la relire","relis-la une fois",
          "Un chiffre de travers, et on se présente une semaine trop tard. Quand tu prends une date en note, redis-la à voix haute pendant que tu l'écris."],
       ]},

      {t:'check', h:"Est-ce que c'est clair maintenant ?",
       p:"Quatre questions rapides.",
       qs:[
         {q:"07/09/2026, c'est…", opts:["le 7 septembre","le 9 juillet"], ok:0,
          fb:"Le premier nombre est le jour, le deuxième est le mois."},
         {q:"Dans 2026-09-07, le 09 est…", opts:["le mois","le jour"], ok:0,
          fb:"Le mois est toujours au milieu, dans les trois écritures."},
         {q:"On écrit…", opts:["le 7 septembre","le 7 Septembre"], ok:0,
          fb:"Pas de majuscule aux mois ni aux jours de la semaine."},
         {q:"Le nombre du milieu ne dépasse jamais…", opts:["12","31"], ok:0,
          fb:"Il y a douze mois. C'est le repère le plus simple."},
       ]},
    ]
  },

  t1heure: {
    eye:'Mini-leçon', tit:"Dire quand : à, de… à, du… au",
    blocs:[
      {t:'texte', h:"Trois petits mots pour tout l'horaire",
       p:"L'annonce tient en une ligne : <b>du lundi au vendredi, de 8 h 30 à 12 h 30</b>. Trois mots portent tout le sens — <b>à</b> pour une heure, <b>de… à</b> pour une durée, <b>du… au</b> pour deux dates ou deux jours. Le reste, ce sont des chiffres.",
       note:"Écrire la ligne de l'annonce au tableau et la décomposer mot à mot. Cette seule ligne contient toute la leçon."},

      {t:'ana', h:"Une seule heure : à",
       p:"On emploie « à » quand on donne un moment précis.",
       mots:[["On dit","Le cours commence {à} 8 h 30."],["Aussi","Le secrétariat ferme {à} 15 h."],["Aussi","Je viens {à} midi."],["On ne dit pas","« commence 8 h 30 » : il faut le à",true]],
       say:"Le cours commence à 8 h 30. Le secrétariat ferme à 15 h.",
       note:"Faire dire à chacun l'heure de son propre cours, avec le « à »."},

      {t:'ana', h:"Du début à la fin : de… à",
       p:"Deux heures, une durée.",
       mots:[["On dit","{De} 8 h 30 {à} 12 h 30."],["Aussi","{De} 9 h {à} 15 h."],["Sans le premier mot","Le cours est {de} quatre heures."],["On ne dit pas","« entre 8 h 30 à 12 h 30 »",true]],
       say:"De 8 h 30 à 12 h 30. De 9 h à 15 h.",
       note:"Faire calculer la durée à voix haute : de 8 h 30 à 12 h 30, ça fait quatre heures. Le calcul rend la tournure concrète."},

      {t:'ana', h:"Deux jours, deux dates : du… au",
       p:"On emploie « du… au » avec les jours de la semaine et les dates.",
       mots:[["On dit","{Du} lundi {au} vendredi."],["Aussi","{Du} 24 {au} 28 août."],["Aussi","{Du} 7 septembre {au} 11 décembre."],["On ne dit pas","« de lundi à vendredi » pour un horaire",true]],
       say:"Du lundi au vendredi. Du 24 au 28 août.",
       note:"« Du… au » veut dire que les deux jours sont compris. Le vendredi est un jour de cours, le 28 août est un jour d'inscription."},

      {t:'ana', h:"Un jour qui revient chaque semaine : le",
       p:"Avec « le », le jour revient toutes les semaines.",
       mots:[["On dit","{Le} lundi, il y a un cours."],["Différent","{Lundi}, il y a un examen — une seule fois"],["Aussi","{Le} matin, de 8 h 30 à 12 h 30."],["On ne dit pas","« au lundi »",true]],
       say:"Le lundi, il y a un cours. Lundi, il y a un examen.",
       note:"La différence entre « le lundi » et « lundi » est un savoir du programme (déterminant défini et fréquence). Deux phrases suffisent à l'installer."},

      {t:'labo', h:"Construis l'horaire",
       p:"Choisis un renseignement et une forme.",
       axes:[
         {id:'p', lbl:'Quel renseignement ?', opts:[
           ["a","l'heure du début"],
           ['b','la durée du matin'],
           ['c','les jours de la semaine'],
           ["d","les jours de l'inscription"]]},
         {id:'q', lbl:'Comment ?', opts:[['1','la phrase courte'],['2','la phrase complète'],['3','la question']]}],
       out:{
         a1:{w:["à 8 h 30"], say:"À 8 h 30.", n:'un seul moment : à'},
         a2:{w:["Le cours commence à 8 h 30."], say:"Le cours commence à 8 h 30.", n:'la phrase de l’annonce'},
         a3:{w:["Le cours commence à quelle heure ?"], say:"Le cours commence à quelle heure ?", n:'la question du comptoir'},
         b1:{w:["de 8 h 30 à 12 h 30"], say:"De 8 h 30 à 12 h 30.", n:'un début et une fin'},
         b2:{w:["Le cours est de 8 h 30 à 12 h 30."], say:"Le cours est de 8 h 30 à 12 h 30.", n:'quatre heures de classe'},
         b3:{w:["Le cours finit à quelle heure ?"], say:"Le cours finit à quelle heure ?", n:'la deuxième question à poser'},
         c1:{w:["du lundi au vendredi"], say:"Du lundi au vendredi.", n:'cinq jours, les deux compris'},
         c2:{w:["Il y a un cours du lundi au vendredi."], say:"Il y a un cours du lundi au vendredi.", n:'la ligne de l’annonce'},
         c3:{w:["C'est quels jours ?"], say:"C'est quels jours ?", n:'la question la plus courte'},
         d1:{w:["du 24 au 28 août"], say:"Du 24 au 28 août.", n:'cinq jours d’inscription'},
         d2:{w:["L'inscription est du 24 au 28 août."], say:"L'inscription est du 24 au 28 août.", n:'à recopier dans ses notes'},
         d3:{w:["L'inscription, c'est quand ?"], say:"L'inscription, c'est quand ?", n:'la question de Yara au téléphone'},
       },
       note:"Douze extraits. Faire reconstruire l'annonce complète à l'oral, à partir des quatre premières sorties."},

      {t:'ex', h:"À écouter et à répéter",
       p:"L'horaire du Centre Delorme.",
       rows:[
         ["Le cours commence à 8 h 30.","une heure : à"],
         ["Le cours est de 8 h 30 à 12 h 30.","une durée : de… à"],
         ["C'est du lundi au vendredi.","deux jours : du… au"],
         ["L'inscription est du 24 au 28 août.","deux dates : du… au"],
         ["Le secrétariat ouvre à 9 h.","une heure : à"],
         ["Le lundi, il y a un cours.","chaque semaine : le"],
       ]},

      {t:'piege', h:"Trois pièges à connaître",
       rows:[
         ["dire « de lundi à vendredi »","c'est du lundi au vendredi",
          "Avec les jours et les dates, on emploie <b>du… au</b>. « De… à » sert aux heures : de 8 h 30 à 12 h 30."],
         ["oublier le « à » devant l'heure","il ne se saute jamais",
          "On dit « le cours commence <b>à</b> 8 h 30 ». Sans le à, la phrase n'existe pas en français, même si le sens se devine."],
         ["confondre « le lundi » et « lundi »","un mot change tout",
          "<b>Le lundi</b>, c'est chaque semaine. <b>Lundi</b> tout court, c'est une seule fois, celui qui arrive. Un seul mot sépare un horaire d'un rendez-vous."],
       ]},

      {t:'check', h:"Est-ce que c'est clair maintenant ?",
       p:"Quatre questions rapides.",
       qs:[
         {q:"« Le cours est ___ 8 h 30 à 12 h 30. »", opts:["de","du"], ok:0,
          fb:"Avec des heures : de… à."},
         {q:"« C'est ___ lundi au vendredi. »", opts:["du","de"], ok:0,
          fb:"Avec des jours et des dates : du… au."},
         {q:"« Le lundi, il y a un cours » veut dire…", opts:["chaque semaine","une seule fois"], ok:0,
          fb:"Le déterminant « le » dit que le jour revient."},
         {q:"De 8 h 30 à 12 h 30, ça fait…", opts:["quatre heures","trois heures"], ok:0,
          fb:"Quatre heures : c'est un avant-midi complet de francisation."},
       ]},
    ]
  },

  t1notes: {
    eye:'Mini-leçon', tit:"Prendre une annonce en note",
    blocs:[
      {t:'texte', h:"On ne recopie pas : on retient quatre choses",
       p:"Devant une annonce, on n'écrit jamais toute la phrase. On écrit <b>quoi</b>, <b>quand</b>, <b>à quelle heure</b>, <b>où</b>. Quatre lignes, quelques chiffres, et l'annonce peut disparaître : tu as tout ce qu'il te faut.",
       note:"C'est l'intention de production écrite du programme pour cette situation. La faire pratiquer sur une vraie annonce affichée dans le centre."},

      {t:'ana', h:"Quoi : le nom de la chose",
       p:"Deux ou trois mots, jamais une phrase.",
       mots:[["On écrit","{cours de français}"],["Aussi","{niveau 2}"],["Aussi","{groupe du matin}"],["On n'écrit pas","« Il y a un cours de français au Centre Delorme »",true]],
       say:"Cours de français. Niveau 2. Groupe du matin.",
       note:"Faire barrer au crayon, dans l'annonce projetée, tout ce qui n'est pas un renseignement. Il reste très peu de mots."},

      {t:'ana', h:"Quand : les dates, copiées exactement",
       p:"Les chiffres se recopient sans les changer.",
       mots:[["On écrit","{7 septembre} — début"],["Aussi","{11 décembre} — fin"],["Aussi","{24 au 28 août} — inscription"],["On ne écrit pas de mémoire","on regarde l'annonce en écrivant",true]],
       say:"Du 7 septembre au 11 décembre. Inscription du 24 au 28 août.",
       note:"Faire recopier en regardant, puis vérifier lettre à lettre avec l'annonce. C'est la seule façon d'attraper l'erreur de chiffre."},

      {t:'ana', h:"À quelle heure, et où",
       p:"Les deux derniers renseignements, les plus courts.",
       mots:[["On écrit","{8 h 30 à 12 h 30}"],["Aussi","{lundi au vendredi}"],["Aussi","{local 214}"],["Aussi","{inscription : local 005}"]],
       say:"De 8 h 30 à 12 h 30. Local 214. Inscription au local 005.",
       note:"Insister sur les deux locaux différents : celui du cours et celui de l'inscription. C'est l'erreur que fait tout le monde la première fois."},

      {t:'labo', h:"Écris ta note",
       p:"Choisis une ligne de la fiche.",
       axes:[
         {id:'p', lbl:'Quelle ligne ?', opts:[
           ['a','quoi'],
           ['b','quand'],
           ['c','à quelle heure'],
           ['d','où']]},
         {id:'q', lbl:'Quelle forme ?', opts:[['1','la note courte'],['2','la phrase entière'],['3','la question à poser']]}],
       out:{
         a1:{w:["cours de français, niveau 2"], say:"Cours de français, niveau 2.", n:'quatre mots suffisent'},
         a2:{w:["C'est un cours de français de niveau 2."], say:"C'est un cours de français de niveau 2.", n:'trop long pour une note'},
         a3:{w:["C'est quel cours ?"], say:"C'est quel cours ?", n:'à poser si l’annonce ne le dit pas'},
         b1:{w:["7 sept. au 11 déc."], say:"Du 7 septembre au 11 décembre.", n:'on abrège les mois en écrivant'},
         b2:{w:["Le cours commence le 7 septembre."], say:"Le cours commence le 7 septembre.", n:'la phrase complète, pour parler'},
         b3:{w:["Ça commence quand ?"], say:"Ça commence quand ?", n:'la question de Yara'},
         c1:{w:["8 h 30 à 12 h 30"], say:"De 8 h 30 à 12 h 30.", n:'les chiffres seuls'},
         c2:{w:["Le cours est de 8 h 30 à 12 h 30."], say:"Le cours est de 8 h 30 à 12 h 30.", n:'la phrase de l’annonce'},
         c3:{w:["C'est à quelle heure ?"], say:"C'est à quelle heure ?", n:'la question à poser au téléphone'},
         d1:{w:["local 214 · inscription 005"], say:"Local 214. Inscription au local 005.", n:'deux locaux, deux lignes'},
         d2:{w:["L'inscription se fait au local 005."], say:"L'inscription se fait au local 005.", n:'à ne pas confondre avec le local du cours'},
         d3:{w:["C'est où, l'inscription ?"], say:"C'est où, l'inscription ?", n:'la question qui évite un étage de marche'},
       },
       note:"Douze extraits. Faire écrire la fiche complète en quatre lignes, chronomètre en main : deux minutes suffisent."},

      {t:'ex', h:"À écouter et à répéter",
       p:"La fiche de notes, ligne par ligne.",
       rows:[
         ["Cours : français, niveau 2","quoi"],
         ["Début : le 7 septembre","quand"],
         ["Fin : le 11 décembre","quand"],
         ["Heure : de 8 h 30 à 12 h 30","à quelle heure"],
         ["Local du cours : 214","où"],
         ["Inscription : local 005, du 24 au 28 août","où et quand"],
       ]},

      {t:'piege', h:"Trois pièges à connaître",
       rows:[
         ["recopier toute l'annonce","quatre lignes suffisent",
          "Recopier prend dix minutes et ne sert à rien : on ne relit jamais un paragraphe. Quatre lignes se relisent en dix secondes, dans l'autobus."],
         ["confondre les deux locaux","le cours et l'inscription ne sont pas au même endroit",
          "Le cours est au local 214, l'inscription au local 005. Deux étages les séparent. Écris les deux, avec leur étiquette."],
         ["écrire de mémoire, après","écris pendant que tu lis",
          "Une date lue puis écrite deux minutes plus tard change de chiffre une fois sur trois. Le papier et le crayon sortent avant de commencer à lire."],
       ]},

      {t:'check', h:"Est-ce que c'est clair maintenant ?",
       p:"Quatre questions rapides.",
       qs:[
         {q:"Dans une note, on écrit…", opts:["quatre renseignements","toute l'annonce"], ok:0,
          fb:"Quoi, quand, à quelle heure, où. Rien de plus."},
         {q:"Le local du cours et le local de l'inscription…", opts:["sont différents","sont les mêmes"], ok:0,
          fb:"Le 214 pour le cours, le 005 pour l'inscription."},
         {q:"On écrit les dates…", opts:["en regardant l'annonce","de mémoire"], ok:0,
          fb:"On copie en regardant, puis on relit une fois."},
         {q:"Une bonne note tient en…", opts:["quatre lignes","une page"], ok:0,
          fb:"Quatre lignes se relisent en dix secondes."},
       ]},
    ]
  },

  t2form: {
    eye:'Mini-leçon', tit:"Les cases d'un formulaire",
    blocs:[
      {t:'texte', h:"Une case, une réponse",
       p:"Un formulaire fait peur parce qu'il est plein. Mais chaque case demande <b>une seule chose</b>, et les cases se ressemblent d'un papier à l'autre : le nom, le prénom, la date de naissance, l'adresse, le téléphone. Quand on connaît les six premières, on peut remplir presque n'importe quel formulaire du Québec.",
       note:"Distribuer un vrai formulaire vierge — inscription, bibliothèque, carte de la ville — et faire retrouver les six cases connues avant toute explication."},

      {t:'ana', h:"Le nom et le prénom",
       p:"Les deux premières cases, et les deux plus souvent inversées.",
       mots:[["Nom de famille","{HADDAD} — en lettres majuscules"],["Prénom","{Yara} — une majuscule, puis des petites lettres"],["Sur la pièce d'identité","les deux sont écrits, dans cet ordre"],["On n'écrit pas","son prénom dans la case du nom",true]],
       say:"Nom de famille : Haddad. Prénom : Yara.",
       note:"Beaucoup de pays écrivent le nom avant le prénom, d'autres l'inverse. Faire lire à chacun sa propre pièce d'identité : c'est elle qui tranche."},

      {t:'ana', h:"La date de naissance et l'adresse",
       p:"Deux cases, deux formes imposées.",
       mots:[["Date de naissance","{1994-03-07} — année, mois, jour"],["Adresse","{3420, rue Papineau}"],["Puis","{Montréal} et le code postal"],["On n'écrit pas","le nom de son pays dans la case adresse",true]],
       say:"Date de naissance : 1994-03-07. Adresse : 3420, rue Papineau, Montréal.",
       note:"La case adresse veut l'adresse d'ici, celle où le centre peut poster une lettre. C'est un malentendu fréquent en première inscription."},

      {t:'ana', h:"La scolarité et la signature",
       p:"La case qu'on ne comprend pas, et celle qu'on oublie.",
       mots:[["Scolarité","{11} — le nombre d'années d'école"],["On compte","l'école primaire, l'école secondaire, le reste"],["Signature","son nom écrit {à la main}, au bas de la page"],["Un formulaire sans signature","n'est pas un formulaire",true]],
       say:"Scolarité : onze ans. Signature, au bas de la page.",
       note:"« Scolarité » est le mot du programme et personne ne le comprend la première fois. Le dire autrement : combien d'années d'école ?"},

      {t:'labo', h:"Remplis la case",
       p:"Choisis une case et ce que tu veux savoir.",
       axes:[
         {id:'p', lbl:'Quelle case ?', opts:[
           ['a','nom et prénom'],
           ['b','date de naissance'],
           ['c','adresse'],
           ['d','scolarité']]},
         {id:'q', lbl:'Quoi ?', opts:[['1','la question de la secrétaire'],['2','la réponse'],['3','ce qu\'on demande si on ne comprend pas']]}],
       out:{
         a1:{w:["Votre nom de famille, s'il vous plaît."], say:"Votre nom de famille, s'il vous plaît.", n:'la première question, toujours'},
         a2:{w:["Haddad. Mon prénom, c'est Yara."], say:"Haddad. Mon prénom, c'est Yara.", n:'nom d’abord, prénom ensuite'},
         a3:{w:["Le nom de famille ou le prénom ?"], say:"Le nom de famille ou le prénom ?", n:'une question qui évite tout un formulaire à refaire'},
         b1:{w:["Quelle est votre date de naissance ?"], say:"Quelle est votre date de naissance ?", n:'date est féminin : quelle'},
         b2:{w:["Le 7 mars 1994."], say:"Le 7 mars 1994.", n:'à l’oral, en toutes lettres'},
         b3:{w:["J'écris l'année en premier ?"], say:"J'écris l'année en premier ?", n:'la forme change d’un formulaire à l’autre'},
         c1:{w:["Quelle est votre adresse ?"], say:"Quelle est votre adresse ?", n:'le numéro, la rue, la ville'},
         c2:{w:["3420, rue Papineau, à Montréal."], say:"3420, rue Papineau, à Montréal.", n:'l’adresse d’ici, pas celle du pays'},
         c3:{w:["Avec le code postal ?"], say:"Avec le code postal ?", n:'presque toujours oui'},
         d1:{w:["Combien d'années d'école ?"], say:"Combien d'années d'école ?", n:'la vraie question derrière le mot « scolarité »'},
         d2:{w:["Onze ans."], say:"Onze ans.", n:'un chiffre suffit'},
         d3:{w:["C'est quoi, cette case ?"], say:"C'est quoi, cette case ?", n:'la phrase qui débloque tout le reste'},
       },
       note:"Douze extraits. Les faire jouer deux par deux, un élève tenant le formulaire, l'autre le crayon."},

      {t:'ex', h:"À écouter et à répéter",
       p:"Les sept cases du formulaire.",
       rows:[
         ["Nom de famille","en lettres majuscules"],
         ["Prénom","une majuscule au début"],
         ["Date de naissance","année, mois, jour"],
         ["Adresse","numéro, rue, ville"],
         ["Téléphone","dix chiffres"],
         ["Scolarité","le nombre d'années d'école"],
         ["Signature","son nom à la main, en bas"],
       ]},

      {t:'piege', h:"Trois pièges à connaître",
       rows:[
         ["mettre son prénom dans la case du nom","regarde ta pièce d'identité",
          "Le nom de famille est celui des parents ; le prénom est celui que les parents ont choisi. Sur ta carte, ils sont écrits l'un sous l'autre, chacun avec son étiquette."],
         ["laisser une case vide sans le dire","demande",
          "Une case vide arrête tout le dossier. Si tu ne comprends pas, dis « c'est quoi, cette case ? ». Personne ne se fâche : la secrétaire répond à cette question dix fois par jour."],
         ["oublier de signer","le formulaire n'est pas fini",
          "Un formulaire sans signature n'est pas accepté. La signature, c'est ton nom écrit à la main, au bas de la page, à côté de la date du jour."],
       ]},

      {t:'check', h:"Est-ce que c'est clair maintenant ?",
       p:"Quatre questions rapides.",
       qs:[
         {q:"Dans la case « scolarité », on écrit…", opts:["le nombre d'années d'école","le nom de son école"], ok:0,
          fb:"Un chiffre. Yara écrit onze."},
         {q:"Le nom de famille, c'est…", opts:["Haddad","Yara"], ok:0,
          fb:"Haddad est le nom de famille ; Yara est le prénom."},
         {q:"Quand tu ne comprends pas une case, tu…", opts:["demandes","laisses vide"], ok:0,
          fb:"« C'est quoi, cette case ? » — la phrase la plus utile du défi."},
         {q:"Un formulaire est fini quand…", opts:["il est signé","les cases sont remplies"], ok:0,
          fb:"La signature au bas de la page fait partie du formulaire."},
       ]},
    ]
  },

  t2mon: {
    eye:'Mini-leçon', tit:"Mon, ma, mes — votre, vos",
    blocs:[
      {t:'texte', h:"Deux personnes, deux séries de mots",
       p:"Au comptoir, deux personnes parlent de la même chose : ton nom. La secrétaire dit <b>votre</b> nom ; toi, tu dis <b>mon</b> nom. Ce sont les mêmes renseignements, avec un mot différent devant. Six mots en tout, et tout le dialogue de l'inscription tient dedans.",
       note:"Faire jouer le dialogue du défi 2 en changeant de rôle à mi-chemin : le passage de « votre » à « mon » s'entend tout seul."},

      {t:'ana', h:"La secrétaire parle de toi : votre, vos",
       p:"Une seule chose : votre. Plusieurs choses : vos.",
       mots:[["On dit","{votre} nom · {votre} adresse"],["Aussi","{votre} date de naissance"],["Plusieurs","{vos} papiers · {vos} coordonnées"],["On ne dit pas","« vos nom »",true]],
       say:"Votre nom. Votre adresse. Vos papiers.",
       note:"« Votre » ne change pas au masculin ni au féminin. C'est le mot le plus facile de la leçon : une seule forme au singulier."},

      {t:'ana', h:"Toi, tu parles de toi : mon, ma, mes",
       p:"Ici, la forme change avec le mot qui suit.",
       mots:[["Masculin","{mon} nom · {mon} prénom · {mon} courriel"],["Féminin","{ma} rue · {ma} signature"],["Plusieurs","{mes} papiers · {mes} enfants"],["On ne dit pas","« ma nom »",true]],
       say:"Mon nom. Ma rue. Mes papiers.",
       note:"Trois formes seulement. Les faire répéter avec des mots du module, jamais avec des mots abstraits."},

      {t:'ana', h:"Le cas qui surprend : mon adresse",
       p:"Devant une voyelle, le mot féminin prend « mon ».",
       mots:[["On dit","{mon} adresse"],["Aussi","{mon} école"],["Aussi","{mon} inscription"],["On ne dit pas","« ma adresse » : c'est trop difficile à dire",true]],
       say:"Mon adresse. Mon école. Mon inscription.",
       note:"La raison est phonétique : deux voyelles collées se disent mal. Donner la règle en un mot — devant a, e, i, o, u, on dit mon — et passer."},

      {t:'labo', h:"Change de rôle",
       p:"Choisis un renseignement et une personne.",
       axes:[
         {id:'p', lbl:'Quel renseignement ?', opts:[
           ['a','le nom de famille'],
           ["b","l'adresse"],
           ['c','les papiers'],
           ['d','la signature']]},
         {id:'q', lbl:'Qui parle ?', opts:[['1','la secrétaire'],['2','toi'],['3','les deux, à la suite']]}],
       out:{
         a1:{w:["Votre nom de famille ?"], say:"Votre nom de famille ?", n:'une seule chose : votre'},
         a2:{w:["Mon nom de famille, c'est Haddad."], say:"Mon nom de famille, c'est Haddad.", n:'nom est masculin : mon'},
         a3:{w:["Votre nom de famille ? Mon nom, c'est Haddad."], say:"Votre nom de famille ? Mon nom, c'est Haddad.", n:'la paire complète du comptoir'},
         b1:{w:["Votre adresse ?"], say:"Votre adresse ?", n:'votre ne change jamais'},
         b2:{w:["Mon adresse, c'est 3420, rue Papineau."], say:"Mon adresse, c'est 3420, rue Papineau.", n:'adresse est féminin, mais commence par une voyelle : mon'},
         b3:{w:["Votre adresse ? Mon adresse, c'est rue Papineau."], say:"Votre adresse ? Mon adresse, c'est rue Papineau.", n:'à écouter deux fois : le mot change, la chose non'},
         c1:{w:["Vos papiers, s'il vous plaît."], say:"Vos papiers, s'il vous plaît.", n:'plusieurs choses : vos'},
         c2:{w:["Voici mes papiers."], say:"Voici mes papiers.", n:'plusieurs choses : mes'},
         c3:{w:["Vos papiers ? Voici mes papiers."], say:"Vos papiers ? Voici mes papiers.", n:'le pluriel des deux côtés'},
         d1:{w:["Votre signature, en bas."], say:"Votre signature, en bas de la page.", n:'la dernière demande'},
         d2:{w:["Ma signature est en bas."], say:"Ma signature est en bas de la page.", n:'signature est féminin : ma'},
         d3:{w:["Votre signature ? Ma signature est en bas."], say:"Votre signature ? Ma signature est en bas.", n:'la fin du formulaire, en deux répliques'},
       },
       note:"Douze extraits. Faire écouter la sortie 3 de chaque ligne : c'est là que le changement de mot s'entend."},

      {t:'ex', h:"À écouter et à répéter",
       p:"Six paires du comptoir.",
       rows:[
         ["Votre nom ? — Mon nom, c'est Haddad.","masculin : mon"],
         ["Votre prénom ? — Mon prénom, c'est Yara.","masculin : mon"],
         ["Votre adresse ? — Mon adresse, c'est rue Papineau.","voyelle : mon"],
         ["Votre rue ? — Ma rue, c'est Papineau.","féminin : ma"],
         ["Vos papiers ? — Voici mes papiers.","pluriel : mes"],
         ["Votre signature ? — Ma signature est en bas.","féminin : ma"],
       ]},

      {t:'piege', h:"Trois pièges à connaître",
       rows:[
         ["dire « ma adresse »","c'est mon adresse",
          "Adresse est un mot féminin, mais il commence par une voyelle. Devant a, e, i, o, u, le féminin prend <b>mon</b> : mon adresse, mon école, mon inscription."],
         ["répondre « votre nom, c'est Haddad »","c'est mon nom",
          "« Votre » désigne la personne à qui on parle. Quand tu réponds, tu parles de toi : <b>mon</b> nom. C'est l'erreur la plus fréquente du défi 2."],
         ["dire « vos nom »","vos est un pluriel",
          "Un seul nom, un seul mot : <b>votre</b>. « Vos » ne s'emploie que devant plusieurs choses : vos papiers, vos enfants."],
       ]},

      {t:'check', h:"Est-ce que c'est clair maintenant ?",
       p:"Quatre questions rapides.",
       qs:[
         {q:"« ___ adresse, c'est rue Papineau. »", opts:["Mon","Ma"], ok:0,
          fb:"Devant une voyelle, le féminin prend mon."},
         {q:"La secrétaire dit…", opts:["votre nom","mon nom"], ok:0,
          fb:"Elle parle de toi : votre."},
         {q:"« Voici ___ papiers. »", opts:["mes","mon"], ok:0,
          fb:"Plusieurs choses : mes."},
         {q:"Combien de formes pour parler de toi ?", opts:["trois : mon, ma, mes","une seule"], ok:0,
          fb:"Mon, ma, mes. Et une seule pour « votre » au singulier."},
       ]},
    ]
  },
};
