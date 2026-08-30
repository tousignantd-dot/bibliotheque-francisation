const EXOS = [
 // ── JE DÉCOUVRE ─────────────────────────────────────────────
  {sec:'prep', id:'prVocab', type:'match', num:'Vocabulaire · 1', tit:"Chaque mot, ce qu'il veut dire", color:'#1D6B8F',
   sub:'Prends un mot, puis va chercher sa définition.', noQLbl:true, bankLbl:'Définitions', zonePh:'glisse la définition ici',
   rows: FC_CARDS.map((c,i)=>({id:'pv'+i, q:c.word, aid:'pv'+i, a:c.def}))},

  {sec:'prep', id:'pr1', type:'vf', num:'Exercice 1', tit:'Vrai ou Faux — Voici ta place', color:'#1D6B8F',
   sub:'Réécoute le dialogue. Ensuite, réponds.', tiles:['VRAI','FAUX'],
   savoir:{h:"› Six objets de la classe — à écouter et à répéter", speak:true, rows:[
     ["On s'assoit dessus","Il y en a un par personne dans la classe.", ["chaise"]],
     ["On l'ouvre pour lire","Il a beaucoup de pages.", ["livre"]],
     ["On écrit avec","Bleu ou noir.", ["stylo"]],
     ["On met le livre dedans","On le porte sur l'épaule.", ["sac"]],
     ["On l'ouvre pour entrer","Elle est au fond de la classe.", ["porte"]],
     ["Elle est ronde, au mur","Elle donne l'heure.", ["horloge"]],
   ]},
   rows:[
    {id:'p1a', txt:"La femme s'appelle Bopha.", ok:'VRAI'},
    {id:'p1b', txt:"Madame Cyr donne un livre à Bopha.", ok:'VRAI'},
    {id:'p1c', txt:"Madame Cyr donne un sac à Bopha.", ok:'FAUX'},
    {id:'p1d', txt:"Le tableau est devant la classe.", ok:'VRAI'},
    {id:'p1e', txt:"Bopha ne dit pas merci.", ok:'FAUX'},
   ]},

  {sec:'prep', id:'prNombres', masque:true, type:'vf', num:'Exercice 2', tit:'Petit nombre ou grand nombre ?', color:'#1D6B8F', accent:'#1D6B8F', cards:true, listen:true,
   sub:"Écoute bien. Ces nombres se ressemblent beaucoup.", tiles:['AVANT DIX','APRÈS DIX'],
   rows:[
    {id:'nba', txt:"deux", ok:'AVANT DIX'},
    {id:'nbb', txt:"douze", ok:'APRÈS DIX'},
    {id:'nbc', txt:"trois", ok:'AVANT DIX'},
    {id:'nbd', txt:"treize", ok:'APRÈS DIX'},
    {id:'nbe', txt:"quatre", ok:'AVANT DIX'},
    {id:'nbf', txt:"quatorze", ok:'APRÈS DIX'},
    {id:'nbg', txt:"six", ok:'AVANT DIX'},
    {id:'nbh', txt:"seize", ok:'APRÈS DIX'},
   ]},

  {sec:'prep', id:'prImg', type:'imgmatch', num:'Exercice 3', tit:'La salle de classe', color:'#1D6B8F',
   sub:"Chaque photo va sur la phrase qui va avec.",
   images:[
    {id:'cl1', src:'/assets/interactive/module-n1-classe/images/salle-vide.jpg'},
    {id:'cl2', src:'/assets/interactive/module-n1-classe/images/tableau-blanc.jpg'},
    {id:'cl3', src:'/assets/interactive/module-n1-classe/images/fenetre-classe.jpg'},
    {id:'cl4', src:'/assets/interactive/module-n1-classe/images/sac-sous-chaise.jpg'},
    {id:'cl5', src:'/assets/interactive/module-n1-classe/images/livre-ouvert.jpg'},
    {id:'cl6', src:'/assets/interactive/module-n1-classe/images/horaire-mur.jpg'},
   ],
   rows:[
    {id:'cl1', txt:"C'est la salle où Bopha apprend le français.", ok:'cl1'},
    {id:'cl2', txt:"L'enseignante écrit dessus, devant la classe.", ok:'cl2'},
    {id:'cl3', txt:"On l'ouvre quand il fait chaud dans la classe.", ok:'cl3'},
    {id:'cl4', txt:"Le sac est sous la chaise.", ok:'cl4'},
    {id:'cl5', txt:"Le livre est ouvert sur la table.", ok:'cl5'},
    {id:'cl6', txt:"La feuille des jours et des heures, près de la porte.", ok:'cl6'},
   ]},

  {sec:'prep', id:'prNom', type:'write', num:'Exercice 4', tit:'Un ou une ?', color:'#1D6B8F', cols:2,
   sub:"Écris « un » ou « une » devant le mot.",
   savoir:{h:"› Un devant les uns, une devant les autres", speak:true, rows:[
     ["Chaque nom a son mot","En français, on ne dit pas « livre » tout seul : on dit <b>un</b> livre, <b>une</b> chaise. Le petit mot vient toujours avant.", ["livre","chaise"]],
     ["On ne le devine pas","Rien dans l'objet ne dit « un » ou « une ». Une chaise n'est pas plus féminine qu'un livre. C'est le mot qui décide, pas la chose."],
     ["Alors, on apprend les deux ensemble","Ne retenez jamais « stylo » : retenez <b>un stylo</b>. Ne retenez jamais « porte » : retenez <b>une porte</b>.", ["stylo","porte"]],
     ["Devant une voyelle, on entend mal","<b>une</b> horloge, <b>un</b> ordinateur : le petit mot se colle au nom et disparaît presque. Écoutez la fin : « un<b>e</b> » finit par un petit « n ».", ["horloge"]],
   ]},
   items:[
    {q:"___ livre", accept:["un"], ph:"un / une"},
    {q:"___ chaise", accept:["une"], ph:"…"},
    {q:"___ stylo", accept:["un"], ph:"…"},
    {q:"___ porte", accept:["une"], ph:"…"},
    {q:"___ horloge", accept:["une"], ph:"…"},
    {q:"___ sac", accept:["un"], ph:"…"},
   ]},

 // ── DÉFI 1 · LA CONSIGNE ────────────────────────────────────
  {sec:'t1', id:'t1vf', type:'vf', num:'Exercice 1', tit:'Vrai ou Faux — Ouvrez le livre', color:'#0D7A6F',
   sub:'Réécoute le dialogue. Ensuite, réponds.', tiles:['VRAI','FAUX'],
   rows:[
    {id:'t1a', txt:"Madame Cyr dit d'ouvrir le livre.", ok:'VRAI'},
    {id:'t1b', txt:"Bopha comprend tout de suite.", ok:'FAUX'},
    {id:'t1c', txt:"Madame Cyr répète plus lentement.", ok:'VRAI'},
    {id:'t1d', txt:"Ivan dit qu'il ne comprend pas.", ok:'VRAI'},
    {id:'t1e', txt:"Le tableau est derrière la classe.", ok:'FAUX'},
   ]},

  {sec:'t1', id:'t1imper', type:'write', num:'Exercice 2', tit:'Le premier mot de la consigne', color:'#0D7A6F', cols:2,
   sub:"Complète la consigne de madame Cyr.",
   savoir:{h:"› Quatre consignes à reconnaître tout de suite", speak:true, rows:[
     ["Le premier mot est le verbe","Une consigne ne commence pas par « je » ni par « vous » : elle commence par le verbe. <span class='savoir-ex'><b>Ouvrez</b> le livre.</span>"],
     ["Écoutez","Ne parlez pas, n'écrivez pas : les oreilles seulement.", ["écouter"]],
     ["Regardez","Les yeux vers le tableau, vers la page, vers l'objet montré.", ["regarder"]],
     ["Ouvrez","Le livre, le sac, la fenêtre, la porte.", ["ouvrir"]],
     ["Fermez","Le contraire. Le livre, le sac, la fenêtre, la porte.", ["fermer"]],
     ["Toutes finissent par le même son","Écout<b>ez</b>, regard<b>ez</b>, ouvr<b>ez</b>, ferm<b>ez</b>. C'est le son « é » de la fin, et il dit : à vous de le faire."],
   ]},
   items:[
    {q:"___ le livre à la page huit.", accept:["Ouvrez","ouvrez"], ph:"le verbe"},
    {q:"___ le tableau : les mots sont écrits dessus.", accept:["Regardez","regardez"], ph:"…"},
    {q:"___ bien : je dis le mot deux fois.", accept:["Écoutez","écoutez","Ecoutez","ecoutez"], ph:"…"},
    {q:"___ la porte, il y a du bruit.", accept:["Fermez","fermez"], ph:"…"},
   ]},

  {sec:'t1', id:'t1geste', type:'match', num:'Exercice 3', tit:'Qu\'est-ce que je fais ?', color:'#0D7A6F',
   sub:"Associe chaque consigne au bon geste.", bankLbl:'Le geste', zonePh:'glisse ici',
   rows:[
    {id:'g1', q:"Écoutez.", aid:'g1', a:"Je ne parle pas. J'ouvre les oreilles."},
    {id:'g2', q:"Regardez le tableau.", aid:'g2', a:"Je lève les yeux vers le devant de la classe."},
    {id:'g3', q:"Ouvrez le livre.", aid:'g3', a:"Je prends le livre et je le mets à plat."},
    {id:'g4', q:"Fermez le livre.", aid:'g4', a:"Je mets les deux pages ensemble."},
    {id:'g5', q:"Prenez un stylo.", aid:'g5', a:"Je mets le stylo dans ma main."},
    {id:'g6', q:"Répétez après moi.", aid:'g6', a:"Je dis le même mot, à voix haute."},
   ]},

  {sec:'t1', id:'t1ou', type:'write', num:'Exercice 4', tit:'Sur, dans ou sous ?', color:'#0D7A6F', cols:2,
   sub:"Où est l'objet ? Complète la phrase.",
   savoir:{h:"› Trois petits mots pour dire où", speak:true, rows:[
     ["sur","Dessus, sur le dessus. <span class='savoir-ex'>Le livre est <b>sur</b> la chaise.</span>", ["chaise"]],
     ["dans","À l'intérieur, on ne le voit pas. <span class='savoir-ex'>Le stylo est <b>dans</b> le sac.</span>", ["sac"]],
     ["sous","En dessous, plus bas. <span class='savoir-ex'>Le sac est <b>sous</b> la chaise.</span>"],
     ["Le petit mot vient avant","On dit « sur la table », jamais « la table sur ». En français, le petit mot passe devant."],
   ]},
   items:[
    {q:"Le livre est ___ la table.", accept:["sur"], ph:"sur / dans / sous"},
    {q:"Mon stylo est ___ mon sac.", accept:["dans"], ph:"…"},
    {q:"Le sac de Bopha est ___ la chaise.", accept:["sous"], ph:"…"},
    {q:"L'horloge est ___ le mur.", accept:["sur"], ph:"…"},
    {q:"Les feuilles sont ___ le livre.", accept:["dans"], ph:"…"},
   ]},

  {sec:'t1', id:'t1b', type:'vf', num:'Exercice 5', tit:'Vrai ou Faux — Où est mon stylo ?', color:'#0D7A6F',
   sub:'Réécoute le dialogue. Ensuite, réponds.', tiles:['VRAI','FAUX'],
   rows:[
    {id:'ob1', txt:"Bopha cherche son stylo.", ok:'VRAI'},
    {id:'ob2', txt:"Le stylo est sur la table.", ok:'FAUX'},
    {id:'ob3', txt:"Le stylo est sous la chaise.", ok:'VRAI'},
    {id:'ob4', txt:"Le livre de Bopha est dans son sac.", ok:'VRAI'},
   ]},

 // ── DÉFI 2 · L'HEURE ET L'HORAIRE ───────────────────────────
  {sec:'t2', id:'t2vf', type:'vf', num:'Exercice 1', tit:'Vrai ou Faux — À quelle heure ?', color:'#B45309',
   sub:'Réécoute le dialogue. Ensuite, réponds.', tiles:['VRAI','FAUX'],
   rows:[
    {id:'h1', txt:"Le cours finit à midi.", ok:'VRAI'},
    {id:'h2', txt:"La pause est à neuf heures.", ok:'FAUX'},
    {id:'h3', txt:"La pause dure quinze minutes.", ok:'VRAI'},
    {id:'h4', txt:"Demain, le cours commence à huit heures et demie.", ok:'VRAI'},
   ]},

  {sec:'t2', id:'t2heure', type:'write', num:'Exercice 2', tit:'Quelle heure est-il ?', color:'#B45309', cols:2,
   sub:"Il manque un mot. Écris-le.",
   savoir:{h:"› Lire l'heure de son cours", speak:true, rows:[
     ["Le nombre, puis le mot heure","On dit le nombre en premier : <span class='savoir-ex'>huit <b>heures</b></span>. Après une heure, le mot prend un s : une heure, deux heures.", ["heure"]],
     ["La demie et le quart","Huit heures <b>et demie</b>, c'est 8 h 30. Huit heures <b>et quart</b>, c'est 8 h 15. Huit heures <b>moins quart</b>, c'est 7 h 45."],
     ["Midi","À douze heures, on ne dit pas « douze heures » : on dit <b>midi</b>. Le soir, à minuit, on dit minuit.", ["midi"]],
     ["Le petit mot à","Pour l'heure d'un rendez-vous ou d'un cours, on met <b>à</b> devant. <span class='savoir-ex'>Le cours commence <b>à</b> huit heures et demie.</span>"],
     ["Ce qu'on écrit","Sur l'horaire du centre, l'heure s'écrit avec un h : 8 h 30, 10 h, 12 h. On le lit « huit heures trente », « dix heures », « midi »."],
   ]},
   items:[
    {q:"Il est huit ___ et demie.", accept:["heures"], ph:"…"},
    {q:"Le cours finit à ___ .", accept:["midi"], ph:"…"},
    {q:"La pause est ___ dix heures.", accept:["à","a"], ph:"…"},
    {q:"8 h 30, c'est huit heures ___ demie.", accept:["et"], ph:"…"},
    {q:"12 h, ce n'est pas douze heures : c'est ___ .", accept:["midi"], ph:"…"},
   ]},

  {sec:'t2', id:'t2jours', type:'vf', num:'Exercice 3', tit:"L'horaire de Bopha", color:'#B45309',
   sub:"Regarde l'horaire dans l'encadré. Y a-t-il un cours ce jour-là ?", tiles:['COURS','PAS DE COURS'],
   savoir:{h:"› L'horaire du groupe de Bopha", speak:true, rows:[
     ["Lundi, mardi, mercredi, jeudi","Cours de 8 h 30 à midi. Pause à 10 h, quinze minutes."],
     ["Vendredi","Pas de cours. Le centre est ouvert, mais le groupe ne vient pas."],
     ["Samedi, dimanche","La fin de semaine. Le centre est fermé."],
     ["Quatre jours par semaine","Une semaine a sept jours ; Bopha vient quatre fois.", ["semaine"]],
     ["Où le lire","L'horaire est affiché près de la porte de la classe.", ["horaire"]],
   ]},
   rows:[
    {id:'j1', txt:"lundi", ok:'COURS'},
    {id:'j2', txt:"mardi", ok:'COURS'},
    {id:'j3', txt:"mercredi", ok:'COURS'},
    {id:'j4', txt:"jeudi", ok:'COURS'},
    {id:'j5', txt:"vendredi", ok:'PAS DE COURS'},
    {id:'j6', txt:"samedi", ok:'PAS DE COURS'},
    {id:'j7', txt:"dimanche", ok:'PAS DE COURS'},
   ]},

  {sec:'t2', id:'t2lire', type:'write', num:'Exercice 4', tit:"Lire l'horaire", color:'#B45309', cols:2,
   sub:"Réponds avec l'horaire de l'exercice 3.",
   items:[
    {q:"Le cours commence à ___ heures et demie.", accept:["huit","8"], ph:"…"},
    {q:"Le cours finit à ___ .", accept:["midi","12 h","douze heures"], ph:"…"},
    {q:"La pause est à ___ heures.", accept:["dix","10"], ph:"…"},
    {q:"Le jour sans cours, c'est ___ .", accept:["vendredi","le vendredi"], ph:"…"},
    {q:"Bopha vient au centre ___ jours par semaine.", accept:["quatre","4"], ph:"…"},
   ]},

 // ── JE ME LANCE ─────────────────────────────────────────────
  {sec:'appli', id:'aQui', type:'vf', num:'Exercice 1', tit:'Qui parle ?', color:'#7E3F98',
   sub:"Écoute le dialogue « Lundi, mardi, mercredi », puis réponds.", tiles:['BOPHA','IVAN'],
   rows:[
    {id:'a1', txt:"« Tu viens vendredi ? »", ok:'IVAN'},
    {id:'a2', txt:"« Il n'y a pas de cours. »", ok:'BOPHA'},
    {id:'a3', txt:"« Regarde l'horaire. »", ok:'BOPHA'},
    {id:'a4', txt:"« Quatre jours. Et vendredi, non. »", ok:'IVAN'},
    {id:'a5', txt:"« Bonne fin de semaine. »", ok:'BOPHA'},
   ]},

  {sec:'appli', id:'aMoi', type:'write', num:'Exercice 2', tit:'Ma classe à moi', color:'#7E3F98', cols:2,
   sub:"Écris ta réponse. Un mot ou trois mots, c'est assez.",
   items:[
    {q:"Nomme trois objets sur ta table.", ph:"un livre, …"},
    {q:"À quelle heure ton cours commence-t-il ?", ph:"à …"},
    {q:"À quelle heure ton cours finit-il ?", ph:"à …"},
    {q:"Quel jour n'y a-t-il pas de cours ?", ph:"…"},
   ]},
];
