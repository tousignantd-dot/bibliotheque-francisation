const PLUS = {
  prPhon: {
    eye:'Mini-leçon', tit:"Le « an » de absence et le « in » de matin",
    blocs:[
      {t:'texte', h:"Deux sons qui passent par le nez",
       p:"En français, une partie de l'air sort par le <b>nez</b> pour certaines voyelles : on les appelle des voyelles <b>nasales</b>. Deux d'entre elles reviennent sans arrêt au comptoir du secrétariat : le <b>an</b> de « abs<b>en</b>ce » et le <b>in</b> de « mat<b>in</b> ». Elles servent à dire quand : lu<b>n</b>di mat<b>in</b>, dema<b>in</b>, tr<b>en</b>te, r<b>en</b>dez-vous.",
       note:"Beaucoup de langues n'ont aucune voyelle nasale. Si ton oreille les mélange, ce n'est pas un défaut : c'est un son que tu n'as jamais eu à distinguer avant."},

      {t:'ana', h:"Le son « an » — la bouche grande ouverte",
       p:"C'est le son de « absence », « enfant », « trente ».",
       mots:[['On écrit','abs{en}ce'],['Aussi écrit','an : enf{an}t · av{an}t',true],['Aussi écrit','am, em devant b et p : sept{em}bre']],
       say:"Une absence, un enfant, avant trente jours.",
       note:"La bouche est ouverte comme pour dire « a », mais l'air passe aussi par le nez. Les lèvres ne sont pas rondes."},

      {t:'ana', h:"Le son « in » — la bouche étirée",
       p:"C'est le son de « matin », « demain », « vingt ».",
       mots:[['On écrit','mat{in}'],['Aussi écrit','ain : dem{ain}',true],['Aussi écrit','ein, en après i : v{ing}t · b{ien}']],
       say:"Demain matin, à vingt heures.",
       note:"Les lèvres s'étirent sur les côtés, presque comme pour sourire. C'est le contraire de la bouche ouverte du « an »."},

      {t:'ana', h:"Le mot qui contient les deux",
       p:"« Un enfant le matin » : les deux sons dans quatre mots.",
       mots:[['Le son an','{en}fant · abs{en}ce'],['Le son in','mat{in} · dema{in}',true],['Le piège','« en » après i se dit « in » : b{ien}, r{ien}']],
       say:"Mon enfant a un rendez-vous demain matin.",
       note:"Retiens cette phrase-là : elle est exactement celle qu'on dit au comptoir, et elle contient les deux sons trois fois."},

      {t:'labo', h:"Écoute les paires",
       p:"Choisis une paire et écoute la différence.",
       axes:[{id:'p', lbl:'Quelle paire ?', opts:[
         ['a','an / in'],
         ['b','absence / matin'],
         ['c','trente / vingt'],
         ['d','enfant / demain'],
         ['e','dans une phrase']]}],
       out:{
         a:{w:['{an} / {in}'], say:"An, in.", n:'la bouche ouverte, puis étirée'},
         b:{w:['abs{en}ce / mat{in}'], say:"Absence, matin.", n:'les deux mots repères'},
         c:{w:['tr{en}te / v{in}gt'], say:"Trente, vingt.", n:'deux nombres du comptoir'},
         d:{w:['{en}fant / dema{in}'], say:"Enfant, demain.", n:'le son est à la fin du second'},
         e:{w:["« Mon enfant a un rendez-vous demain matin. »"], say:"Mon enfant a un rendez-vous demain matin.", n:'les deux sons, trois fois'},
       },
       note:"Écoute chaque paire deux fois : la première pour comprendre, la seconde en fermant les yeux."},

      {t:'ex', h:"À écouter et à répéter",
       p:"Six phrases du comptoir.",
       rows:[
         ["Je vais être absente demain matin.","an puis in"],
         ["Mon enfant a un rendez-vous.","an trois fois"],
         ["Le trente septembre, à vingt heures.","les deux sons"],
         ["Avant le cours, je passe au comptoir.","an deux fois"],
         ["Lundi matin, ça va bien.","in trois fois"],
         ["Une absence prévenue, c'est différent.","an au début et au milieu"],
       ]},

      {t:'piege', h:"Trois pièges à connaître",
       rows:[
         ["prononcer la lettre n","dire « ab-sen-ne-ce »",
          "Dans « absence », le n ne se prononce pas tout seul : il rend la voyelle nasale, puis il disparaît. La langue ne touche pas le palais."],
         ["croire que « en » se dit toujours « an »","les mots « bien », « rien », « combien »",
          "Après un i, les lettres e et n se disent « in ». C'est pour ça que « bien » rime avec « matin » et non avec « avant »."],
         ["mélanger « trente » et « vingt »","donner une date au comptoir",
          "Là, la confusion change la journée. Dis le nombre, puis répète-le : la secrétaire le répète aussi, exprès."],
       ]},

      {t:'check', h:"Est-ce que c'est clair maintenant ?",
       p:"Quatre questions rapides.",
       qs:[
         {q:"« Absence » a le son…", opts:["an","in"], ok:0,
          fb:"La bouche est ouverte : c'est le son de « avant »."},
         {q:"« Demain » a le son…", opts:["an","in"], ok:1,
          fb:"Les lettres a, i, n ensemble se disent « in »."},
         {q:"Dans ces sons, l'air passe…", opts:["par la bouche seulement","par le nez aussi"], ok:1,
          fb:"C'est pour ça qu'on les appelle des voyelles nasales."},
         {q:"« Bien » a le son…", opts:["an","in"], ok:1,
          fb:"Après un i, « en » se dit « in » : bien, rien, combien."},
       ]},

      {t:'revoir', h:"À retenir",
       p:"Deux mots repères, et rien d'autre : <b>absence</b> pour le son « an », <b>matin</b> pour le son « in ». Quand tu hésites devant un mot nouveau, dis-le à côté de l'un des deux et écoute lequel se ressemble."},
    ]
  },

  prSalut: {
    eye:'Mini-leçon', tit:"Bonjour madame : parler à quelqu'un du centre",
    blocs:[
      {t:'texte', h:"Trois secondes qui changent tout",
       p:"Au comptoir, on ne commence jamais par sa demande. On salue, on dit <b>madame</b> ou <b>monsieur</b>, et seulement après on explique pourquoi on est là. Ces trois secondes ne sont pas de la décoration : elles disent que tu sais où tu es et à qui tu parles. Le programme les nomme les <b>formules d'appel et de salutation</b>.",
       note:"Une demande qui commence par « Je veux un papier » se fait servir quand même — mais moins bien, et plus lentement. C'est ainsi partout."},

      {t:'ana', h:"Saluer",
       p:"Deux mots, dans cet ordre.",
       mots:[['On dit','{bonjour} madame'],['Ou','bonjour monsieur',true],['Jamais','« bonjour » tout seul au comptoir']],
       say:"Bonjour, madame. Bonjour, monsieur.",
       note:"Il y a une petite pause entre « bonjour » et « madame » : deux mots, pas un seul."},

      {t:'ana', h:"Vouvoyer",
       p:"Au centre, on dit vous à tout le personnel.",
       mots:[['On dit','{vous} pouvez'],['Et','est-ce que vous avez un papier ?',true],['On garde tu','pour les camarades de classe']],
       say:"Est-ce que vous pouvez répéter, s'il vous plaît ?",
       note:"Le <b>vous</b> de politesse s'écrit et se conjugue comme le vous de plusieurs personnes. Une seule personne, une seule différence : elle ne se voit pas."},

      {t:'ana', h:"Votre et vos",
       p:"Ce sont les mots qui vont avec vous.",
       mots:[['Une chose','{votre} nom · votre groupe'],['Plusieurs','{vos} journées · vos papiers',true],['Ta réponse','mon nom · mes journées']],
       say:"Votre nom ? Votre groupe ? Vos journées d'absence ?",
       note:"Écoute le mot qu'elle emploie : le tien est son miroir. Elle dit « votre nom », tu réponds « mon nom, c'est… »."},

      {t:'labo', h:"La même demande, plus ou moins polie",
       p:"Choisis une demande et une façon de la dire.",
       axes:[
         {id:'d', lbl:'Quelle demande ?', opts:[['a','une attestation'],['b','garder son billet'],['c','une photocopie']]},
         {id:'f', lbl:'Comment ?', opts:[['1','trop direct'],['2','au comptoir']]}],
       out:{
         a1:{w:["Je veux une attestation."], say:"Je veux une attestation.", n:'compris, mais sec'},
         a2:{w:["Bonjour, madame. J'aimerais une attestation de fréquentation, s'il vous plaît."], say:"Bonjour, madame. J'aimerais une attestation de fréquentation, s'il vous plaît.", n:'salutation, demande, formule'},
         b1:{w:["Je garde mon billet."], say:"Je garde mon billet.", n:"tu annonces au lieu de demander"},
         b2:{w:["Est-ce que je peux garder l'original, s'il vous plaît ?"], say:"Est-ce que je peux garder l'original, s'il vous plaît ?", n:'une question, pas une décision'},
         c1:{w:["Faites une photocopie."], say:"Faites une photocopie.", n:"c'est un ordre"},
         c2:{w:["Pourriez-vous faire une photocopie, s'il vous plaît ?"], say:"Pourriez-vous faire une photocopie, s'il vous plaît ?", n:'la même chose, en demande'},
       },
       note:"Les six phrases veulent dire la même chose. Trois ouvrent la porte, trois la laissent lourde."},

      {t:'ex', h:"À écouter et à répéter",
       p:"Six formules à savoir par cœur.",
       rows:[
         ["Bonjour, madame.","la première phrase, toujours"],
         ["Est-ce que je peux vous parler, s'il vous plaît ?","demander avant d'expliquer"],
         ["Mon nom, c'est Nawel Belkacem, groupe 12.","nom, prénom, groupe"],
         ["Pouvez-vous répéter plus lentement, s'il vous plaît ?","à dire sans hésiter"],
         ["Merci beaucoup, madame.","avant de partir"],
         ["Bonne journée.","la dernière phrase, toujours"],
       ]},

      {t:'piege', h:"Trois pièges à connaître",
       rows:[
         ["tutoyer la secrétaire","dire « tu peux m'aider ? »",
          "Au centre, tout le personnel se vouvoie : secrétaire, enseignante, direction. Le tu est pour les camarades de classe, et pour eux seulement."],
         ["dire « madame » sans « bonjour »","commencer par « Madame ! »",
          "Appeler quelqu'un par « madame » toute seule sonne comme un ordre. Le mot va après « bonjour », jamais tout seul."],
         ["oublier son groupe","donner seulement son nom",
          "La secrétaire ne peut rien inscrire sans le groupe : deux élèves peuvent porter le même nom. Nom, prénom, groupe : les trois, toujours."],
       ]},

      {t:'check', h:"Est-ce que c'est clair maintenant ?",
       p:"Quatre questions rapides.",
       qs:[
         {q:"Au comptoir, on commence par…", opts:["sa demande","bonjour madame"], ok:1,
          fb:"La salutation d'abord, la demande ensuite."},
         {q:"À la secrétaire, on dit…", opts:["tu","vous"], ok:1,
          fb:"Tout le personnel du centre se vouvoie."},
         {q:"« ___ journées d'absence sont justifiées » — elle dit…", opts:["Vos","Mes"], ok:0,
          fb:"Elle parle de tes journées à toi : elle dit « vos »."},
         {q:"Après « merci beaucoup », on ajoute…", opts:["bonne journée","c'est tout"], ok:0,
          fb:"« Bonne journée » ferme la démarche : c'est la fin normale."},
       ]},

      {t:'revoir', h:"À retenir",
       p:"Quatre phrases suffisent pour toute une démarche : <b>Bonjour, madame.</b> — <b>Mon nom, c'est…, groupe…</b> — <b>Est-ce que je peux… ?</b> — <b>Merci beaucoup. Bonne journée.</b> Entre les deux, tu mets ce que tu as à dire."},
    ]
  },

  t1futur: {
    eye:'Mini-leçon', tit:"Je vais être absente : annoncer avant",
    blocs:[
      {t:'texte', h:"Prévenir, c'est parler de demain",
       p:"Quand tu viens au comptoir <b>avant</b> ton absence, tu parles d'une chose qui n'est pas encore arrivée. Le français a une forme faite exactement pour ça, et elle est facile : le verbe <b>aller</b> au présent, suivi d'un second verbe qui ne change jamais. « Je <b>vais être</b> absente. » · « Je <b>vais manquer</b> le cours de jeudi. »",
       note:"On l'appelle le <b>futur proche</b>. C'est le futur de la vie de tous les jours : celui du comptoir, du téléphone et de la porte de la classe."},

      {t:'ana', h:"La forme",
       p:"Deux verbes, l'un derrière l'autre.",
       mots:[['On dit','{je vais} être absente'],['Le second verbe','ne change jamais : être, manquer, arriver',true],['On n\'ajoute rien','pas de « à », pas de « de »']],
       say:"Je vais être absente jeudi matin.",
       note:"Le premier verbe porte la personne ; le second dit ce qui va se passer. C'est tout le mécanisme."},

      {t:'ana', h:"Les quatre formes utiles",
       p:"Au comptoir, il n'en faut pas plus.",
       mots:[['Moi','je {vais}'],['Toi','tu vas',true],['Ma fille, mon fils','il, elle va · ils, elles vont']],
       say:"Je vais arriver en retard. Ma fille va avoir un rendez-vous.",
       note:"« Nous allons » existe aussi, mais au comptoir on parle presque toujours de soi ou de son enfant."},

      {t:'ana', h:"La forme négative",
       p:"Ne et pas entourent le verbe aller.",
       mots:[['On dit','je {ne vais pas} être là'],['À l\'oral','« je vais pas être là » s\'entend beaucoup',true],['Au comptoir','dis la forme complète']],
       say:"Je ne vais pas être là lundi.",
       note:"Les deux morceaux se placent autour du <b>premier</b> verbe seulement. Le second reste au bout, tout seul."},

      {t:'labo', h:"Avant ou après l'absence ?",
       p:"Choisis une personne et un moment.",
       axes:[
         {id:'p', lbl:'Qui ?', opts:[['a','moi'],['b','ma fille'],['c','mes enfants']]},
         {id:'m', lbl:'Quand ?', opts:[['1','avant : ce n\'est pas arrivé'],['2','après : c\'est fini']]}],
       out:{
         a1:{w:["Je vais être absente jeudi."], say:"Je vais être absente jeudi.", n:'futur proche'},
         a2:{w:["J'ai été absente jeudi."], say:"J'ai été absente jeudi.", n:'passé : tu viens justifier'},
         b1:{w:["Ma fille va avoir un rendez-vous."], say:"Ma fille va avoir un rendez-vous.", n:'elle : va'},
         b2:{w:["Ma fille a eu un rendez-vous."], say:"Ma fille a eu un rendez-vous.", n:'c\'est passé'},
         c1:{w:["Mes enfants vont manquer l'école."], say:"Mes enfants vont manquer l'école.", n:'ils : vont'},
         c2:{w:["Mes enfants ont manqué l'école."], say:"Mes enfants ont manqué l'école.", n:'c\'est passé'},
       },
       note:"La secrétaire n'écrit pas la même chose dans les deux colonnes : à gauche « absence prévenue », à droite « absence à justifier »."},

      {t:'ex', h:"À écouter et à répéter",
       p:"Six phrases à dire au comptoir.",
       rows:[
         ["Je vais être absente jeudi, l'avant-midi.","la phrase de base"],
         ["Je vais manquer le cours de vendredi.","un autre verbe, même forme"],
         ["Je vais arriver en retard demain matin.","un retard s'annonce aussi"],
         ["Ma fille va avoir un rendez-vous à neuf heures.","elle : va"],
         ["Je ne vais pas être là lundi et mardi.","la négative"],
         ["Je vais revenir mercredi.","dire aussi quand on revient"],
       ]},

      {t:'piege', h:"Trois pièges à connaître",
       rows:[
         ["conjuguer le second verbe","« je vais suis absente »",
          "Un seul verbe se conjugue : aller. Le second reste tel qu'il est dans le dictionnaire — être, manquer, arriver."],
         ["ajouter un petit mot entre les deux","« je vais à être absente »",
          "Rien ne se met entre les deux verbes. Ni à, ni de, ni pour."],
         ["employer le futur proche pour hier","« demain je vais être absente hier »",
          "Cette forme ne parle que de ce qui n'est pas encore arrivé. Pour une absence finie, on dit « j'ai été absente »."],
       ]},

      {t:'check', h:"Est-ce que c'est clair maintenant ?",
       p:"Quatre questions rapides.",
       qs:[
         {q:"« Ma fille ___ avoir un rendez-vous. »", opts:["va","vais"], ok:0,
          fb:"Elle, il : va. Je : vais."},
         {q:"Le second verbe se met…", opts:["à l'infinitif","au présent"], ok:0,
          fb:"Il ne change jamais : être, manquer, arriver."},
         {q:"« Je ne vais pas être là » — ne et pas entourent…", opts:["aller","être"], ok:0,
          fb:"Ils entourent le premier verbe seulement."},
         {q:"Tu viens justifier une absence d'hier. Tu dis…", opts:["je vais être absente","j'ai été absente"], ok:1,
          fb:"C'est fini : le futur proche ne convient plus."},
       ]},

      {t:'revoir', h:"À retenir",
       p:"<b>Je vais</b> + un verbe qui ne bouge pas. C'est la forme de toute annonce faite à l'avance : une absence, un retard, un départ. Et pour la nier, <b>ne… pas</b> autour de « vais »."},
    ]
  },

  t1jours: {
    eye:'Mini-leçon', tit:"Jeudi ou le jeudi : un seul mot de différence",
    blocs:[
      {t:'texte', h:"Le petit mot qui change tout",
       p:"« <b>Jeudi</b>, je vais être absente » et « <b>Le jeudi</b>, je vais être absente » ne veulent pas dire la même chose. Sans <b>le</b> : une seule journée, celle qui vient. Avec <b>le</b> : tous les jeudis, toutes les semaines. La secrétaire n'écrit pas la même chose selon ce que tu dis.",
       note:"C'est un des rares endroits où un mot de deux lettres décide seul du sens de la phrase. Le programme du niveau 3 le nomme explicitement."},

      {t:'ana', h:"Sans « le » : une fois",
       p:"C'est ce qu'on dit presque toujours au comptoir.",
       mots:[['On dit','{jeudi}, je vais être absente'],['Ça veut dire','jeudi qui vient, une seule journée',true],['On peut ajouter','jeudi prochain · jeudi le 12 mars']],
       say:"Jeudi, je vais être absente.",
       note:"Si on est mardi, « jeudi » veut dire dans deux jours. Personne ne se pose la question."},

      {t:'ana', h:"Avec « le » : chaque semaine",
       p:"C'est un horaire, pas une absence.",
       mots:[['On dit','{le jeudi}, je travaille'],['Ça veut dire','tous les jeudis, toutes les semaines',true],['Autre exemple','le lundi, mon fils va à la piscine']],
       say:"Le jeudi, je travaille : c'est toutes les semaines.",
       note:"Au comptoir, cette forme sert quand on explique pourquoi on manque toujours le même jour."},

      {t:'ana', h:"Les sept jours et la date",
       p:"Ils ne prennent jamais de majuscule.",
       mots:[['Dans l\'ordre','{lundi mardi mercredi} jeudi vendredi'],['La fin de semaine','samedi · dimanche',true],['La date','jeudi {le 12 mars} — le chiffre d\'abord']],
       say:"Lundi, mardi, mercredi, jeudi, vendredi.",
       note:"En français, « le 12 mars » : le chiffre, puis le mois. Jamais « mars 12 », qui vient de l'anglais."},

      {t:'labo', h:"Une fois ou toutes les semaines ?",
       p:"Choisis un jour et un sens.",
       axes:[
         {id:'j', lbl:'Quel jour ?', opts:[['a','jeudi'],['b','lundi'],['c','vendredi']]},
         {id:'s', lbl:'Quel sens ?', opts:[['1','une seule fois'],['2','toutes les semaines']]}],
       out:{
         a1:{w:["Jeudi, je vais être absente."], say:"Jeudi, je vais être absente.", n:'une journée'},
         a2:{w:["Le jeudi, je vais être absente."], say:"Le jeudi, je vais être absente.", n:'tous les jeudis'},
         b1:{w:["Lundi, j'ai un rendez-vous."], say:"Lundi, j'ai un rendez-vous.", n:'lundi prochain'},
         b2:{w:["Le lundi, j'ai un rendez-vous."], say:"Le lundi, j'ai un rendez-vous.", n:'chaque semaine'},
         c1:{w:["Vendredi, c'est mon dernier jour de cours."], say:"Vendredi, c'est mon dernier jour de cours.", n:'une date précise'},
         c2:{w:["Le vendredi, je finis plus tôt."], say:"Le vendredi, je finis plus tôt.", n:'un horaire'},
       },
       note:"Lis les six phrases à voix haute. La différence s'entend à peine — et pourtant elle décide de tout."},

      {t:'ex', h:"À écouter et à répéter",
       p:"Six phrases avec un jour.",
       rows:[
         ["Jeudi, je vais être absente.","une journée"],
         ["Le jeudi, je travaille.","toutes les semaines"],
         ["Jeudi prochain, le 12 mars.","le jour et la date"],
         ["J'ai manqué lundi passé.","une journée finie"],
         ["Du lundi au mercredi, j'étais malade.","trois journées"],
         ["Le vendredi, je finis à midi.","un horaire"],
       ]},

      {t:'piege', h:"Trois pièges à connaître",
       rows:[
         ["mettre « le » sans le vouloir","« le jeudi je vais être absente »",
          "Tu viens d'annoncer que tu manqueras tous les jeudis de la session. La secrétaire va te le faire répéter — et elle a raison."],
         ["écrire la date à l'anglaise","« mars 12 »",
          "En français, le chiffre vient d'abord : le 12 mars. Dans un courriel au secrétariat, c'est la seule forme acceptée."],
         ["mettre une majuscule aux jours","« Jeudi », « Lundi » au milieu d'une phrase",
          "Les jours et les mois s'écrivent en minuscules en français, sauf au début d'une phrase."],
       ]},

      {t:'check', h:"Est-ce que c'est clair maintenant ?",
       p:"Quatre questions rapides.",
       qs:[
         {q:"« Le lundi, je travaille » veut dire…", opts:["lundi prochain","tous les lundis"], ok:1,
          fb:"Avec « le », c'est chaque semaine."},
         {q:"Pour une seule absence, on dit…", opts:["jeudi","le jeudi"], ok:0,
          fb:"Sans « le » : une seule journée."},
         {q:"On écrit la date…", opts:["le 12 mars","mars 12"], ok:0,
          fb:"Le chiffre d'abord, le mois ensuite."},
         {q:"« jeudi » au milieu d'une phrase prend…", opts:["une majuscule","une minuscule"], ok:1,
          fb:"Les jours ne prennent pas de majuscule en français."},
       ]},

      {t:'revoir', h:"À retenir",
       p:"<b>Jeudi</b> = une fois. <b>Le jeudi</b> = chaque semaine. Et au comptoir, ajoute la date : « jeudi prochain, le 12 mars ». Avec les deux, plus personne ne peut se tromper."},
    ]
  },

  t2temps: {
    eye:'Mini-leçon', tit:"Dire exactement quelles journées ont été manquées",
    blocs:[
      {t:'texte', h:"La secrétaire écrit des dates, pas des impressions",
       p:"Quand tu reviens après une absence, la seule chose qu'on te demandera est : <b>quelles journées</b> ? Ni pourquoi en détail, ni comment tu te sens. Il faut donc savoir nommer des jours passés avec précision — et c'est un petit groupe de mots, toujours les mêmes.",
       note:"Une réponse vague — « la semaine passée, je pense » — oblige à redemander. Une réponse précise règle la démarche en trente secondes."},

      {t:'ana', h:"Ce qui vient de finir",
       p:"Les mots les plus courts, et les plus utiles.",
       mots:[['On dit','{hier}'],['Ou','{avant-hier} : deux jours avant',true],['Et','ce matin · cet avant-midi']],
       say:"J'ai manqué le cours hier et avant-hier.",
       note:"« Hier » ne prend jamais de préposition : on ne dit pas « à hier » ni « le hier »."},

      {t:'ana', h:"La semaine qui est finie",
       p:"Au Québec, un mot plutôt qu'un autre.",
       mots:[['On dit','{la semaine passée}'],['On entend aussi','la semaine dernière',true],['Le contraire','la semaine prochaine']],
       say:"J'ai été absente la semaine passée.",
       note:"« Passée » et « dernière » veulent dire la même chose ; « passée » s'entend beaucoup plus au comptoir, au Québec."},

      {t:'ana', h:"Du premier au dernier jour",
       p:"La formule exacte, celle qu'écrit le billet.",
       mots:[['On dit','{du lundi au mercredi}'],['Les deux jours','sont compris dans le compte',true],['Sur un billet','« du 3 au 5 mars »']],
       say:"Le billet dit : du lundi au mercredi.",
       note:"Trois journées, pas deux : lundi, mardi et mercredi. C'est la source d'erreur la plus fréquente."},

      {t:'ana', h:"Combien de temps",
       p:"Deux mots à ne pas confondre.",
       mots:[['C\'est fini','{pendant trois jours}'],['Ça continue','{depuis lundi}',true],['Question','depuis quand ? · pendant combien de temps ?']],
       say:"Je suis malade depuis lundi. Je n'ai pas pu venir pendant trois jours.",
       note:"<b>Pendant</b> compte une durée finie. <b>Depuis</b> part d'un jour et arrive jusqu'à aujourd'hui : si tu dis « depuis lundi », tu es encore malade."},

      {t:'labo', h:"La même absence, quatre façons de la dire",
       p:"Choisis une absence et une façon.",
       axes:[
         {id:'a', lbl:'Quelle absence ?', opts:[['a','trois jours de grippe'],['b','une demi-journée']]},
         {id:'f', lbl:'Comment la dire ?', opts:[['1','les journées'],['2','du… au…'],['3','la durée']]}],
       out:{
         a1:{w:["J'ai manqué lundi, mardi et mercredi."], say:"J'ai manqué lundi, mardi et mercredi.", n:'une date à la fois'},
         a2:{w:["J'ai été absente du lundi au mercredi."], say:"J'ai été absente du lundi au mercredi.", n:'la formule du billet'},
         a3:{w:["Je n'ai pas pu venir pendant trois jours."], say:"Je n'ai pas pu venir pendant trois jours.", n:'la durée, sans les dates'},
         b1:{w:["J'ai manqué jeudi, l'avant-midi."], say:"J'ai manqué jeudi, l'avant-midi.", n:'le jour et le moment'},
         b2:{w:["J'étais absente de neuf heures à midi."], say:"J'étais absente de neuf heures à midi.", n:'du… au… pour les heures'},
         b3:{w:["Je suis partie pendant deux heures."], say:"Je suis partie pendant deux heures.", n:'une durée courte'},
       },
       note:"Les trois façons sont bonnes. La plus utile au comptoir est la première : les journées, l'une après l'autre."},

      {t:'ex', h:"À écouter et à répéter",
       p:"Six phrases pour revenir après une absence.",
       rows:[
         ["J'ai été absente la semaine passée.","situer la semaine"],
         ["J'ai manqué lundi, mardi et mercredi.","les journées, dans l'ordre"],
         ["Le billet dit : du 3 au 5 mars.","lire la date du papier"],
         ["Je suis malade depuis lundi.","ça continue"],
         ["Je n'ai pas pu venir pendant trois jours.","c'est fini"],
         ["Je suis revenue hier.","le retour aussi se dit"],
       ]},

      {t:'piege', h:"Trois pièges à connaître",
       rows:[
         ["confondre depuis et pendant","« je suis malade pendant lundi »",
          "Depuis + un jour de départ ; pendant + une durée. « Depuis lundi » : ça dure encore. « Pendant trois jours » : c'est fini."],
         ["compter mal « du… au… »","dire deux jours pour « du lundi au mercredi »",
          "Le premier et le dernier jour sont compris. Du lundi au mercredi, ça fait trois journées."],
         ["dire « la semaine passée » pour avant-hier","une absence de mardi dernier",
          "Si on est jeudi, mardi n'est pas la semaine passée : c'est cette semaine. Nomme le jour plutôt que la semaine."],
       ]},

      {t:'check', h:"Est-ce que c'est clair maintenant ?",
       p:"Quatre questions rapides.",
       qs:[
         {q:"« Du lundi au mercredi », ça fait…", opts:["deux journées","trois journées"], ok:1,
          fb:"Les deux journées du bout sont comprises."},
         {q:"« Je suis malade depuis lundi » veut dire…", opts:["c'est fini","ça dure encore"], ok:1,
          fb:"Depuis part d'un jour et arrive jusqu'à aujourd'hui."},
         {q:"Pour une durée finie, on dit…", opts:["pendant","depuis"], ok:0,
          fb:"Pendant trois jours : c'est terminé."},
         {q:"Au comptoir, la réponse la plus utile est…", opts:["les journées, une à une","« la semaine passée, je pense »"], ok:0,
          fb:"Précise : la secrétaire écrit des dates."},
       ]},

      {t:'revoir', h:"À retenir",
       p:"Trois formules, et l'affaire est réglée : <b>hier</b> · <b>la semaine passée</b> · <b>du lundi au mercredi</b>. Ajoute <b>depuis</b> si tu es encore malade, <b>pendant</b> si c'est fini."},
    ]
  },

  t2poss: {
    eye:'Mini-leçon', tit:"Mon billet, votre dossier : à qui est le papier",
    blocs:[
      {t:'texte', h:"Deux personnes, deux séries de mots",
       p:"Au comptoir, il y a toujours deux personnes et beaucoup de papiers. Les mots qui disent à qui appartient quoi sont donc partout : <b>mon</b> billet, <b>votre</b> dossier, <b>mes</b> journées, <b>vos</b> papiers. Ils sont peu nombreux et ils vont deux par deux — ce qu'elle dit avec <b>votre</b>, tu le reprends avec <b>mon</b>.",
       note:"On les appelle des <b>déterminants possessifs</b>. Ils se placent devant le nom, exactement à la place de « le » ou « la »."},

      {t:'ana', h:"Ce qui est à moi",
       p:"Trois formes, selon le nom qui suit.",
       mots:[['Masculin','{mon billet} · mon dossier'],['Féminin','{ma fille} · ma carte',true],['Pluriel','{mes papiers} · mes journées']],
       say:"Mon billet, ma fille, mes papiers.",
       note:"Ce n'est pas la personne qui décide — c'est le mot d'après. « Mon billet » même si celui qui parle est une femme."},

      {t:'ana', h:"Ce qui est à vous",
       p:"Deux formes seulement.",
       mots:[['Une chose','{votre dossier} · votre nom'],['Plusieurs','{vos journées} · vos papiers',true],['Aucun changement','masculin ou féminin, c\'est pareil']],
       say:"Votre dossier, votre nom, vos journées d'absence.",
       note:"« Votre » ne fait pas de différence entre masculin et féminin : une forme de moins à retenir."},

      {t:'ana', h:"Devant une voyelle, ma devient mon",
       p:"Trois mots du module sont concernés.",
       mots:[['On dit','{mon absence}, pas « ma absence »'],['Aussi','{mon attestation}',true],['Et','mon enseignante · mon adresse']],
       say:"Mon absence, mon attestation, mon enseignante.",
       note:"Ces mots restent féminins : on écrit « mon attestation est prête », pas « prêt ». C'est la prononciation qui a changé le déterminant, pas le genre."},

      {t:'labo', h:"Elle demande, tu réponds",
       p:"Choisis ce qu'elle demande et lis ta réponse.",
       axes:[
         {id:'q', lbl:'Elle demande…', opts:[['a','le nom'],['b','le groupe'],['c','les journées'],['d','le papier']]}],
       out:{
         a:{w:["— Votre nom ? — Mon nom, c'est Nawel Belkacem."], say:"Votre nom ? Mon nom, c'est Nawel Belkacem.", n:'votre → mon'},
         b:{w:["— Votre groupe ? — Mon groupe, c'est le 12."], say:"Votre groupe ? Mon groupe, c'est le douze.", n:'votre → mon'},
         c:{w:["— Vos journées d'absence ? — Mes journées : lundi, mardi et mercredi."], say:"Vos journées d'absence ? Mes journées : lundi, mardi et mercredi.", n:'vos → mes'},
         d:{w:["— Votre billet ? — Voici mon billet."], say:"Votre billet ? Voici mon billet.", n:'votre → mon'},
       },
       note:"Le mot qu'elle emploie t'annonce le tien. Écoute-le : c'est un miroir, il n'y a rien à décider."},

      {t:'ex', h:"À écouter et à répéter",
       p:"Six échanges du comptoir.",
       rows:[
         ["Voici mon billet de la clinique.","masculin : mon"],
         ["Ma fille avait un rendez-vous.","féminin : ma"],
         ["J'ai perdu mes papiers.","pluriel : mes"],
         ["J'inscris l'absence dans votre dossier.","elle parle de toi"],
         ["Vos journées sont justifiées.","pluriel : vos"],
         ["Je viens chercher mon attestation.","voyelle : mon, pas ma"],
       ]},

      {t:'piege', h:"Trois pièges à connaître",
       rows:[
         ["choisir d'après la personne","dire « ma billet » parce qu'on est une femme",
          "Le déterminant s'accorde avec le <b>nom qui suit</b>, jamais avec celui qui parle. Un homme dit « ma fille », une femme dit « mon billet »."],
         ["dire « ma absence »","les mots qui commencent par une voyelle",
          "Devant a, e, i, o, u et h muet, « ma » devient « mon » : mon absence, mon attestation, mon adresse."],
         ["répondre avec « votre »","« — Votre nom ? — Votre nom, c'est Nawel. »",
          "« Votre » désigne la personne à qui tu parles. Pour parler de toi, c'est « mon » ou « mes »."],
       ]},

      {t:'check', h:"Est-ce que c'est clair maintenant ?",
       p:"Quatre questions rapides.",
       qs:[
         {q:"« ___ fille a un rendez-vous. »", opts:["Ma","Mon"], ok:0,
          fb:"« Fille » est féminin et commence par une consonne."},
         {q:"« Je viens chercher ___ attestation. »", opts:["ma","mon"], ok:1,
          fb:"Devant une voyelle, ma devient mon."},
         {q:"Elle dit « vos journées », tu réponds…", opts:["mes journées","vos journées"], ok:0,
          fb:"Vos → mes : c'est un miroir."},
         {q:"Le déterminant s'accorde avec…", opts:["la personne qui parle","le nom qui suit"], ok:1,
          fb:"Toujours le nom qui suit."},
       ]},

      {t:'revoir', h:"À retenir",
       p:"<b>mon · ma · mes</b> pour ce qui est à toi, <b>votre · vos</b> pour ce qui est à elle ou dans son bureau. Et devant une voyelle, toujours <b>mon</b> : mon absence, mon attestation."},
    ]
  },

  t3avant: {
    eye:'Mini-leçon', tit:"Avant de partir : mettre les démarches dans l'ordre",
    blocs:[
      {t:'texte', h:"Tout le défi 3 tient dans un ordre",
       p:"Une attestation demandée <b>avant</b> le départ se prépare en trois jours. Demandée <b>après</b>, le dossier est fermé et tout devient plus long. Le français dit cet ordre avec deux petites formules : <b>avant de</b> + un verbe, et <b>avant</b> + un nom ou une heure.",
       note:"C'est une leçon de grammaire et une leçon de démarche en même temps : ici, la forme et la vie disent la même chose."},

      {t:'ana', h:"Avant de + un verbe",
       p:"Le verbe qui suit ne change jamais.",
       mots:[['On dit','{avant de partir}'],['Aussi','{avant de signer} · avant de décider',true],['Devant une voyelle','avant d\'arrêter · avant d\'entrer']],
       say:"Avant de partir, demandez votre attestation.",
       note:"« De » devient « d' » devant une voyelle : avant d'arrêter, avant d'aller la voir."},

      {t:'ana', h:"Avant + un nom ou une heure",
       p:"Sans « de » : ce qui suit n'est pas un verbe.",
       mots:[['On dit','{avant le cours}'],['Ou','{avant 9 heures}',true],['Ou','avant votre départ · avant vendredi']],
       say:"Je passe au comptoir avant le cours, avant neuf heures.",
       note:"Comment choisir : si le mot suivant est une action, il faut « de ». Si c'est une chose, une heure ou un jour, non."},

      {t:'ana', h:"Après, son contraire",
       p:"Il se construit plus simplement.",
       mots:[['On dit','{après le cours}'],['Ou','après midi · après vendredi',true],['Attention','« après avoir signé » est une forme du niveau suivant']],
       say:"Après le cours, je vais voir mon enseignante.",
       note:"Au niveau 3, garde « après » devant un nom ou une heure : c'est suffisant pour tout dire au comptoir."},

      {t:'labo', h:"Les trois démarches, dans l'ordre",
       p:"Choisis une étape et vois ce qu'on dit.",
       axes:[{id:'e', lbl:'Quelle étape ?', opts:[
         ['a','1 — venir le dire'],
         ['b','2 — donner la date'],
         ['c','3 — demander le papier'],
         ['d','4 — signer'],
         ['e','ce qu\'il ne faut pas faire']]}],
       out:{
         a:{w:["Avant de partir, je viens le dire au comptoir."], say:"Avant de partir, je viens le dire au comptoir.", n:'avant de + verbe'},
         b:{w:["Mon dernier jour de cours est le vendredi 28 mars."], say:"Mon dernier jour de cours est le vendredi vingt-huit mars.", n:'la date, dite et répétée'},
         c:{w:["Je demande mon attestation avant mon départ."], say:"Je demande mon attestation avant mon départ.", n:'avant + nom'},
         d:{w:["Avant de signer, je lis le formulaire au complet."], say:"Avant de signer, je lis le formulaire au complet.", n:'on lit toujours avant de signer'},
         e:{w:["Téléphoner deux semaines après être parti."], say:"Téléphoner deux semaines après être parti.", n:'trop tard : le dossier est fermé'},
       },
       note:"Les quatre premières étapes tiennent en une visite de cinq minutes. La cinquième coûte des semaines."},

      {t:'ex', h:"À écouter et à répéter",
       p:"Six phrases de la dernière démarche.",
       rows:[
         ["Avant de partir, je demande mon attestation.","la phrase la plus importante"],
         ["Avant de signer, je lis le formulaire.","toujours, partout"],
         ["Je passe au comptoir avant le cours.","avant + nom"],
         ["Il faut téléphoner avant neuf heures.","avant + heure"],
         ["Après le cours, je vais voir mon enseignante.","après + nom"],
         ["Avant d'arrêter, j'en parle à mon enseignante.","d' devant une voyelle"],
       ]},

      {t:'piege', h:"Trois pièges à connaître",
       rows:[
         ["oublier le « de »","« avant partir »",
          "Devant un verbe, il faut « de » : avant <b>de</b> partir. C'est l'erreur la plus fréquente, et elle s'entend tout de suite."],
         ["mettre « de » devant un nom","« avant de le cours »",
          "Devant un nom, une heure ou un jour : pas de « de ». Avant le cours, avant neuf heures, avant vendredi."],
         ["demander l'attestation après","partir puis téléphoner",
          "Ce n'est pas une faute de français, mais c'est la seule erreur du module qui coûte vraiment quelque chose. Le papier se demande avant."],
       ]},

      {t:'check', h:"Est-ce que c'est clair maintenant ?",
       p:"Quatre questions rapides.",
       qs:[
         {q:"« ___ partir, demandez votre attestation. »", opts:["Avant de","Avant"], ok:0,
          fb:"Devant un verbe : avant de."},
         {q:"« Je passe au comptoir ___ le cours. »", opts:["avant de","avant"], ok:1,
          fb:"Devant un nom : avant, sans « de »."},
         {q:"Devant une voyelle, « avant de » devient…", opts:["avant d'","avant que"], ok:0,
          fb:"Avant d'arrêter, avant d'entrer."},
         {q:"L'attestation se demande…", opts:["avant de partir","après le départ"], ok:0,
          fb:"Après, le dossier est fermé."},
       ]},

      {t:'revoir', h:"À retenir",
       p:"Un verbe après ? <b>avant de</b>. Un nom, une heure, un jour ? <b>avant</b>, tout court. Et la phrase à emporter du module : <b>avant de partir, je demande mon attestation</b>."},
    ]
  },

  t3demande: {
    eye:'Mini-leçon', tit:"Quatre demandes qui ouvrent le comptoir",
    blocs:[
      {t:'texte', h:"Demander, ce n'est pas exiger",
       p:"Tout ce que tu viens chercher au secrétariat se demande : un papier, une permission, une explication, une répétition. Le français a une formule pour chacune, et elles sont courtes. Les apprendre par cœur vaut mieux que de les inventer sur place, parce qu'au comptoir on est pressé et souvent intimidé.",
       note:"Ces quatre formules servent partout ailleurs : à la clinique, à la banque, au bureau de la garderie. Ce n'est pas du vocabulaire de centre de formation."},

      {t:'ana', h:"Demander une chose",
       p:"Plus doux que « je veux », aussi clair.",
       mots:[['On dit','{j\'aimerais une attestation}'],['Ou','je voudrais un formulaire',true],['On ajoute','s\'il vous plaît, toujours']],
       say:"J'aimerais une attestation de fréquentation, s'il vous plaît.",
       note:"« Je veux » n'est pas impoli en soi, mais il ferme la porte. « J'aimerais » demande la même chose et laisse la personne dire oui."},

      {t:'ana', h:"Demander la permission",
       p:"La question la plus utile du comptoir.",
       mots:[['On dit','{est-ce que je peux} garder l\'original ?'],['Ou','est-ce que je peux revenir demain ?',true],['Plus court','je peux… ? avec la voix qui monte']],
       say:"Est-ce que je peux garder l'original ?",
       note:"Elle ne demande rien de plus qu'une réponse par oui ou par non : c'est ce qui la rend facile à comprendre et à donner."},

      {t:'ana', h:"Demander un service",
       p:"Le conditionnel, en un seul mot.",
       mots:[['On dit','{pourriez-vous} faire une photocopie ?'],['Aussi','pourriez-vous répéter ?',true],['Plus simple','est-ce que vous pouvez… ?']],
       say:"Pourriez-vous faire une photocopie, s'il vous plaît ?",
       note:"« Pourriez-vous » et « est-ce que vous pouvez » valent la même chose. Le premier est un peu plus poli, le second plus courant."},

      {t:'ana', h:"Demander une explication",
       p:"Deux questions qui règlent presque tout.",
       mots:[['On dit','{qu\'est-ce que je dois apporter} ?'],['Ou','{quand est-ce que} l\'attestation sera prête ?',true],['Et','pouvez-vous répéter {plus lentement} ?']],
       say:"Qu'est-ce que je dois apporter ? Quand est-ce que ce sera prêt ?",
       note:"Demander une répétition n'est jamais impoli. Ce qui pose un problème, c'est de repartir sans avoir compris."},

      {t:'labo', h:"La demande, la réponse",
       p:"Choisis ce que tu veux obtenir.",
       axes:[{id:'d', lbl:'Tu veux…', opts:[
         ['a','le papier'],
         ['b','garder ton billet'],
         ['c','une photocopie'],
         ['d','savoir quel jour'],
         ['e','faire répéter']]}],
       out:{
         a:{w:["— J'aimerais une attestation de fréquentation, s'il vous plaît.","— Certainement. Elle sera prête vendredi."], say:"J'aimerais une attestation de fréquentation, s'il vous plaît.", n:'demander une chose'},
         b:{w:["— Est-ce que je peux garder l'original ?","— Bien sûr. Je fais une photocopie."], say:"Est-ce que je peux garder l'original ?", n:'demander la permission'},
         c:{w:["— Pourriez-vous faire une photocopie, s'il vous plaît ?","— Un instant, je vous la fais."], say:"Pourriez-vous faire une photocopie, s'il vous plaît ?", n:'demander un service'},
         d:{w:["— Quand est-ce que l'attestation sera prête ?","— Dans trois jours, au comptoir."], say:"Quand est-ce que l'attestation sera prête ?", n:'demander une explication'},
         e:{w:["— Pouvez-vous répéter plus lentement, s'il vous plaît ?","— Oui. Vendredi le 28 mars."], say:"Pouvez-vous répéter plus lentement, s'il vous plaît ?", n:'ne jamais repartir sans avoir compris'},
       },
       note:"Cinq demandes, cinq réponses courtes. C'est exactement le rythme d'une visite au comptoir."},

      {t:'ex', h:"À écouter et à répéter",
       p:"Six phrases à savoir par cœur.",
       rows:[
         ["J'aimerais une attestation, s'il vous plaît.","demander une chose"],
         ["Est-ce que je peux garder l'original ?","demander la permission"],
         ["Pourriez-vous faire une photocopie ?","demander un service"],
         ["Qu'est-ce que je dois apporter ?","demander une explication"],
         ["Quand est-ce que ce sera prêt ?","demander un délai"],
         ["Pouvez-vous répéter plus lentement, s'il vous plaît ?","faire répéter"],
       ]},

      {t:'piege', h:"Trois pièges à connaître",
       rows:[
         ["commencer par « je veux »","« je veux mon papier »",
          "La demande est comprise, mais elle sonne comme un ordre. « J'aimerais » coûte deux syllabes de plus et change tout le ton."],
         ["ne pas oser faire répéter","repartir sans avoir compris la date",
          "Une date mal comprise, c'est un papier qu'on vient chercher le mauvais jour. « Pouvez-vous répéter plus lentement ? » est une phrase d'adulte, pas d'enfant."],
         ["poser deux questions à la fois","« et le billet, et l'attestation, et mon dossier ? »",
          "Une question, une réponse. Au comptoir, la personne note en même temps qu'elle parle : deux questions ensemble en font perdre une."],
       ]},

      {t:'check', h:"Est-ce que c'est clair maintenant ?",
       p:"Quatre questions rapides.",
       qs:[
         {q:"Pour demander un papier, on dit…", opts:["je veux","j'aimerais"], ok:1,
          fb:"« J'aimerais » demande la même chose, plus doucement."},
         {q:"« ___ je peux garder l'original ? »", opts:["Est-ce que","Pourriez-vous"], ok:0,
          fb:"C'est une permission qui te concerne : est-ce que je peux."},
         {q:"Pour un service, on dit…", opts:["pourriez-vous","je peux"], ok:0,
          fb:"Le service, c'est l'autre qui le rend : pourriez-vous."},
         {q:"Faire répéter, c'est…", opts:["impoli","normal"], ok:1,
          fb:"Tout le monde le fait. Repartir sans comprendre, non."},
       ]},

      {t:'revoir', h:"À retenir",
       p:"Quatre formules et une visite entière tient debout : <b>j'aimerais…</b> · <b>est-ce que je peux… ?</b> · <b>pourriez-vous… ?</b> · <b>qu'est-ce que… ?</b> Ajoute <b>s'il vous plaît</b> à chacune, et tu n'as plus à réfléchir."},
    ]
  },
};
