const EXOS = [
 // ── JE DÉCOUVRE ─────────────────────────────────────────────
  {sec:'prep', id:'prVocab', type:'match', num:'Vocabulaire · 1', tit:'Le mot et sa définition', color:'#1D6B8F',
   sub:'Choisis un mot, puis sa définition. Six mots à la fois.', noQLbl:true, bankLbl:'Définitions', zonePh:'glisse la définition ici',
   rows: FC_CARDS.map((c,i)=>({id:'pv'+i, q:c.word, aid:'pv'+i, a:c.def}))},

  {sec:'prep', id:'pr1', type:'vf', num:'Exercice 1', tit:"Vrai ou Faux — À la table d'inscription", color:'#1D6B8F',
   sub:'Écoute de nouveau le dialogue, puis réponds.', tiles:['VRAI','FAUX'],
   savoir:{h:"› Les mots de la fiche — à écouter et à répéter", speak:true, rows:[
     ["Le moment et la feuille","On s'inscrit, et on reçoit une feuille de papier.", ["une inscription","une fiche"]],
     ["Le petit rectangle","On écrit un seul renseignement dedans : un nom, un chiffre, une rue.", ["une case"]],
     ["Écrire dans toutes les cases","C'est ce qu'on demande le premier jour. Rien ne doit rester vide.", ["remplir"]],
   ]},
   rows:[
    {id:'p1a', txt:"Yusuf vient pour l'inscription.", ok:'VRAI'},
    {id:'p1b', txt:"La fiche a huit cases.", ok:'VRAI'},
    {id:'p1c', txt:"Madame Côté ne l'aide pas.", ok:'FAUX'},
    {id:'p1d', txt:"On commence par le nom.", ok:'VRAI'},
    {id:'p1e', txt:"On écrit en lettres majuscules.", ok:'VRAI'},
   ]},

  {sec:'prep', id:'prSons', type:'vf', num:'Exercice 2', tit:"Treize ou trente ?", color:'#1D6B8F', accent:'#1D6B8F', cards:true, listen:true,
   sub:"Écoute le nombre. Est-ce qu'il finit par le son « ze » ou par le son « te » ?", tiles:['LE SON « ZE »','LE SON « TE »'],
   savoir:{h:"› Deux nombres qui se ressemblent", speak:true, rows:[
     ["13 et 30","La fin change tout : trei<b>ze</b>, tren<b>te</b>.", ["treize","trente"]],
     ["14 et 40","Quator<b>ze</b>, quaran<b>te</b>.", ["quatorze","quarante"]],
     ["15 et 50","Quin<b>ze</b>, cinquan<b>te</b>. Ici, même le début change.", ["quinze","cinquante"]],
   ]},
   rows:[
    {id:'ps1', txt:"treize", ok:'LE SON « ZE »'},
    {id:'ps2', txt:"trente", ok:'LE SON « TE »'},
    {id:'ps3', txt:"quatorze", ok:'LE SON « ZE »'},
    {id:'ps4', txt:"quarante", ok:'LE SON « TE »'},
    {id:'ps5', txt:"quinze", ok:'LE SON « ZE »'},
    {id:'ps6', txt:"cinquante", ok:'LE SON « TE »'},
    {id:'ps7', txt:"seize", ok:'LE SON « ZE »'},
    {id:'ps8', txt:"soixante", ok:'LE SON « TE »'},
   ]},

  {sec:'prep', id:'prImg', type:'imgmatch', num:'Exercice 3', tit:"Ce qu'on voit le jour de l'inscription", color:'#1D6B8F',
   sub:"Glisse chaque photo sur la phrase qui la décrit.",
   images:[
    {id:'im1', src:'/assets/interactive/module-n1-inscription/images/table-inscription.jpg'},
    {id:'im2', src:'/assets/interactive/module-n1-inscription/images/fiche-cases.jpg'},
    {id:'im3', src:'/assets/interactive/module-n1-inscription/images/main-stylo.jpg'},
    {id:'im4', src:'/assets/interactive/module-n1-inscription/images/boite-lettres.jpg'},
    {id:'im5', src:'/assets/interactive/module-n1-inscription/images/telephone-papier.jpg'},
    {id:'im6', src:'/assets/interactive/module-n1-inscription/images/ecran-courriel.jpg'},
   ],
   rows:[
    {id:'im1', txt:"La table où on s'inscrit, le premier jour.", ok:'im1'},
    {id:'im2', txt:"Une feuille avec des cases vides.", ok:'im2'},
    {id:'im3', txt:"Une main qui écrit dans une case.", ok:'im3'},
    {id:'im4', txt:"On y reçoit son courrier. Le numéro est écrit dessus.", ok:'im4'},
    {id:'im5', txt:"On y compose dix chiffres.", ok:'im5'},
    {id:'im6', txt:"On y lit ses messages.", ok:'im6'},
   ]},

  {sec:'prep', id:'prCases', type:'write', num:'Exercice 4', tit:"Une case, un renseignement", color:'#1D6B8F', cols:2,
   sub:"Complète d'après le dialogue.",
   savoir:{h:"› Comment on remplit une fiche, ici", rows:[
     ["Une case = une seule chose","On n'écrit pas son nom et son adresse dans la même case. Une case, un renseignement."],
     ["En lettres majuscules","DAOUD, YUSUF. On le demande souvent : les lettres détachées se lisent sans erreur."],
     ["Rien ne reste vide","Quand une case ne vous concerne pas, on écrit un trait : —. Une case vide fait croire à un oubli."],
     ["On peut demander","« Qu'est-ce que j'écris ici ? » est une phrase normale. Personne ne remplit sa première fiche tout seul."],
   ]},
   items:[
    {q:"NOM DE FAMILLE : ___", accept:["Daoud","DAOUD","daoud"], ph:"…"},
    {q:"PRÉNOM : ___", accept:["Yusuf","YUSUF","yusuf"], ph:"…"},
    {q:"Il y a huit ___ dans la fiche.", accept:["cases"], ph:"…"},
    {q:"Madame Côté dit : « Écrivez en lettres ___ . »", accept:["majuscules"], ph:"…"},
   ]},

 // ── DÉFI 1 · LE NOM ET LA DATE DE NAISSANCE ─────────────────
  {sec:'t1', id:'t1vf', type:'vf', num:'Exercice 1', tit:"Vrai ou Faux — Quel est votre nom de famille ?", color:'#0D7A6F',
   sub:'Écoute de nouveau le dialogue, puis réponds.', tiles:['VRAI','FAUX'],
   rows:[
    {id:'t1a', txt:"Le nom de famille de Yusuf est Daoud.", ok:'VRAI'},
    {id:'t1b', txt:"Son prénom est Yusuf.", ok:'VRAI'},
    {id:'t1c', txt:"Il n'épelle pas son nom.", ok:'FAUX'},
    {id:'t1d', txt:"Madame Côté coche « F ».", ok:'FAUX'},
    {id:'t1e', txt:"« H » veut dire « homme ».", ok:'VRAI'},
   ]},

  {sec:'t1', id:'t1quel', type:'write', num:'Exercice 2', tit:"Quel ou quelle ?", color:'#0D7A6F', cols:2,
   sub:"Complète chaque question.",
   savoir:{h:"› Quel ou quelle — la question de la fiche", speak:true, rows:[
     ["Devant un mot masculin : quel","<b>Quel</b> est votre nom de famille ? <b>Quel</b> est votre prénom ?", ["le nom de famille","le prénom"]],
     ["Devant un mot féminin : quelle","<b>Quelle</b> est votre adresse ? <b>Quelle</b> est votre date de naissance ?", ["l'adresse","la date de naissance"]],
     ["À l'oreille, c'est pareil","<span class='savoir-ex'>quel</span> et <span class='savoir-ex'>quelle</span> se disent exactement de la même façon. La différence ne se voit qu'à l'écrit."],
     ["Le mot qui décide est celui d'après","Ce n'est pas vous qui êtes masculin ou féminin : c'est le mot de la case. Un homme dit « quelle est mon adresse ? »."],
   ]},
   items:[
    {q:"___ est votre nom de famille ?", accept:["Quel","quel"], ph:"…"},
    {q:"___ est votre prénom ?", accept:["Quel","quel"], ph:"…"},
    {q:"___ est votre adresse ?", accept:["Quelle","quelle"], ph:"…"},
    {q:"___ est votre date de naissance ?", accept:["Quelle","quelle"], ph:"…"},
    {q:"___ est votre numéro de téléphone ?", accept:["Quel","quel"], ph:"…"},
    {q:"___ est votre année de naissance ?", accept:["Quelle","quelle"], ph:"…"},
   ]},

  {sec:'t1', id:'t1civil', type:'match', num:'Exercice 3', tit:'Madame, monsieur, F, H', color:'#0D7A6F',
   sub:"Associe chaque mot de la fiche à ce qu'il veut dire.", bankLbl:'Ce que ça veut dire', zonePh:'glisse ici',
   savoir:{h:"› Les mots courts de la case du haut", rows:[
     ["Le titre de civilité","<b>Madame</b> devant le nom d'une femme, <b>monsieur</b> devant celui d'un homme. Sur une fiche, ils sont souvent écrits en court : Mme, M."],
     ["La case du sexe","Deux lettres seulement : <b>F</b> pour femme, <b>H</b> pour homme. Certaines fiches écrivent plutôt <b>M</b> pour masculin et <b>F</b> pour féminin."],
     ["Attention au F","Sur une fiche, F veut dire <b>femme</b>. Sur une autre, F veut dire <b>féminin</b>. C'est la même case et la même réponse."],
   ]},
   rows:[
    {id:'cv1', q:"Madame", aid:'cv1', a:"devant le nom d'une femme"},
    {id:'cv2', q:"Monsieur", aid:'cv2', a:"devant le nom d'un homme"},
    {id:'cv3', q:"Mme", aid:'cv3', a:"madame, écrit en court"},
    {id:'cv4', q:"F", aid:'cv4', a:"la case du sexe : femme"},
    {id:'cv5', q:"H", aid:'cv5', a:"la case du sexe : homme"},
    {id:'cv6', q:"M", aid:'cv6', a:"masculin, sur certaines fiches"},
   ]},

  {sec:'t1', id:'t1date', type:'write', num:'Exercice 4', tit:"Le jour, le mois, l'année", color:'#0D7A6F', cols:2,
   sub:"Yusuf est né le 12 mars 1992. Complète.",
   savoir:{h:"› L'ordre de la date, ici", speak:true, rows:[
     ["Le jour, puis le mois, puis l'année","Le 12 mars 1992 s'écrit <span class='savoir-ex'>12 / 03 / 1992</span>.", ["la date de naissance"]],
     ["Le mois s'écrit en chiffres","Janvier 01 · février 02 · mars 03 · avril 04 · mai 05 · juin 06 · juillet 07 · août 08 · septembre 09 · octobre 10 · novembre 11 · décembre 12."],
     ["Deux chiffres partout","Le 5 janvier s'écrit 05 / 01. On ajoute un zéro devant les nombres d'un seul chiffre."],
     ["L'année a quatre chiffres","1992, et non 92. Une fiche demande l'année complète.", ["l'année"]],
     ["Ce n'est pas pareil partout","Dans plusieurs pays, le mois vient avant le jour. Une date mal lue vous vieillit ou vous rajeunit de plusieurs mois."],
   ]},
   items:[
    {q:"Le jour : ___", accept:["12"], ph:"…"},
    {q:"Le mois de mars s'écrit ___", accept:["03","3"], ph:"…"},
    {q:"L'année : ___", accept:["1992"], ph:"…"},
    {q:"Le 5 janvier s'écrit ___ / 01", accept:["05","5"], ph:"…"},
    {q:"Dans quel ordre ? Le jour, le ___ , l'année.", accept:["mois"], ph:"…"},
    {q:"Le mois de septembre s'écrit ___", accept:["09","9"], ph:"…"},
   ]},

  {sec:'t1', id:'t1nais', type:'vf', num:'Exercice 5', tit:"Vrai ou Faux — Quelle est votre date de naissance ?", color:'#0D7A6F',
   sub:'Écoute de nouveau le dialogue, puis réponds.', tiles:['VRAI','FAUX'],
   rows:[
    {id:'tn1', txt:"Yusuf est né le douze mars.", ok:'VRAI'},
    {id:'tn2', txt:"Il est né en 1982.", ok:'FAUX'},
    {id:'tn3', txt:"Mars est le mois numéro trois.", ok:'VRAI'},
    {id:'tn4', txt:"Ici, on écrit le mois avant le jour.", ok:'FAUX'},
   ]},

 // ── DÉFI 2 · L'ADRESSE ET LE TÉLÉPHONE ──────────────────────
  {sec:'t2', id:'t2vf', type:'vf', num:'Exercice 1', tit:"Vrai ou Faux — J'écris quoi dans cette case ?", color:'#B45309',
   sub:'Écoute de nouveau le dialogue, puis réponds.', tiles:['VRAI','FAUX'],
   rows:[
    {id:'tv1', txt:"Carlos habite avenue Papineau.", ok:'VRAI'},
    {id:'tv2', txt:"Il habite à l'appartement 4.", ok:'VRAI'},
    {id:'tv3', txt:"« Tél. » veut dire téléphone.", ok:'VRAI'},
    {id:'tv4', txt:"Un numéro de téléphone a six chiffres.", ok:'FAUX'},
    {id:'tv5', txt:"Yusuf dit qu'il demande souvent.", ok:'VRAI'},
   ]},

  {sec:'t2', id:'t2abrev', type:'match', num:'Exercice 2', tit:'Les petits mots coupés', color:'#B45309',
   sub:"Associe chaque abréviation au mot complet.", bankLbl:'Le mot complet', zonePh:'glisse ici',
   savoir:{h:"› Les abréviations de la fiche", speak:true, rows:[
     ["Un mot coupé, un point","Le point dit que le mot n'est pas fini : <b>av.</b> pour avenue, <b>boul.</b> pour boulevard, <b>app.</b> pour appartement.", ["l'adresse","un appartement"]],
     ["Deux lettres pour la province","<b>QC</b> veut dire Québec. On l'écrit après la ville, sans point : <span class='savoir-ex'>Montréal, QC</span>."],
     ["Trois lettres et trois chiffres","C'est ce qui vient après la province, et ce n'est jamais un mot.", ["le code postal"]],
     ["Le téléphone en trois lettres","<b>Tél.</b> On écrit dix chiffres après.", ["le téléphone"]],
     ["Deux qu'on voit encore","<b>n°</b> pour numéro, <b>C.P.</b> pour case postale — une boîte au bureau de poste, quand on n'a pas d'adresse à soi."],
   ]},
   rows:[
    {id:'ab1', q:"app.", aid:'ab1', a:"un appartement"},
    {id:'ab2', q:"av.", aid:'ab2', a:"une avenue"},
    {id:'ab3', q:"boul.", aid:'ab3', a:"un boulevard"},
    {id:'ab4', q:"QC", aid:'ab4', a:"Québec, la province"},
    {id:'ab5', q:"Tél.", aid:'ab5', a:"le téléphone"},
    {id:'ab6', q:"C.P.", aid:'ab6', a:"une case postale"},
    {id:'ab7', q:"n°", aid:'ab7', a:"un numéro"},
   ]},

  {sec:'t2', id:'t2adresse', type:'write', num:'Exercice 3', tit:"J'écris mon adresse", color:'#B45309', cols:2,
   sub:"Écris le mot complet.",
   savoir:{h:"› L'adresse, de haut en bas", speak:true, rows:[
     ["La première ligne","Le numéro, une virgule, puis la rue : <span class='savoir-ex'>3120, avenue Papineau</span>.", ["l'adresse"]],
     ["L'appartement, à côté ou en dessous","<span class='savoir-ex'>app. 4</span>, ou <span class='savoir-ex'>3120, av. Papineau, app. 4</span>.", ["un appartement"]],
     ["La deuxième ligne","La ville, la province, le code postal : <span class='savoir-ex'>Montréal, QC  H2K 1N4</span>."],
     ["Le numéro d'abord","Ici, le numéro vient <b>avant</b> le nom de la rue. Dans plusieurs pays, c'est l'inverse."],
   ]},
   items:[
    {q:"3120, ___ Papineau   (av.)", accept:["avenue"], ph:"…"},
    {q:"___ 4   (app.)", accept:["appartement","Appartement"], ph:"…"},
    {q:"Montréal, ___   (QC)", accept:["Québec","Quebec","québec","quebec"], ph:"…"},
    {q:"___ : 514 555 0198   (Tél.)", accept:["Téléphone","téléphone"], ph:"…"},
    {q:"940, ___ Saint-Laurent   (boul.)", accept:["boulevard"], ph:"…"},
   ]},

  {sec:'t2', id:'t2tel', type:'write', num:'Exercice 4', tit:'Le téléphone, le code postal, le courriel', color:'#B45309', cols:2,
   sub:"Complète.",
   savoir:{h:"› Les chiffres qu'on dit tout haut", speak:true, rows:[
     ["Dix chiffres, trois groupes","<span class='savoir-ex'>514 · 555 · 0198</span>. On dit les chiffres un par un, jamais « cinq cent quatorze ».", ["le téléphone"]],
     ["Trois lettres, trois chiffres","<span class='savoir-ex'>H2K 1N4</span>. Une lettre, un chiffre, une lettre — puis un chiffre, une lettre, un chiffre.", ["le code postal"]],
     ["Le signe @ se dit « arobase »","<span class='savoir-ex'>yusuf point daoud arobase courriel point c a</span>. Le point se dit « point », jamais autrement.", ["le courriel"]],
     ["Faites répéter","Un chiffre mal entendu, et personne ne peut vous joindre. « Pouvez-vous répéter, plus lentement ? » se dit à chaque fois qu'il le faut."],
   ]},
   items:[
    {q:"Un numéro de téléphone a ___ chiffres.", accept:["dix","10"], ph:"…"},
    {q:"Un code postal a trois lettres et trois ___ .", accept:["chiffres"], ph:"…"},
    {q:"Dans H2K 1N4, la première lettre est ___ .", accept:["H","h"], ph:"…"},
    {q:"Dans un courriel, le signe @ se dit ___ .", accept:["arobase","une arobase","l'arobase"], ph:"…"},
    {q:"On dit les chiffres du téléphone un par ___ .", accept:["un"], ph:"…"},
   ]},

 // ── JE ME LANCE ─────────────────────────────────────────────
  {sec:'appli', id:'aQui', type:'vf', num:'Exercice 1', tit:'Qui parle ?', color:'#7E3F98',
   sub:"Écoute le dialogue « Je relis votre fiche », puis réponds.", tiles:['YUSUF','MADAME CÔTÉ'],
   rows:[
    {id:'aq1', txt:"« Quel est votre code postal ? »", ok:'MADAME CÔTÉ'},
    {id:'aq2', txt:"« H, deux, K. Un, N, quatre. »", ok:'YUSUF'},
    {id:'aq3', txt:"« Pardon ? Plus lentement, s'il vous plaît. »", ok:'YUSUF'},
    {id:'aq4', txt:"« Votre fiche est complète. Bienvenue ! »", ok:'MADAME CÔTÉ'},
    {id:'aq5', txt:"« yusuf point daoud, arobase, courriel point c a. »", ok:'YUSUF'},
   ]},

  {sec:'appli', id:'aFiche', type:'write', num:'Exercice 2', tit:'Ma fiche', color:'#7E3F98', cols:2,
   sub:"Écris ta réponse à chaque question. Ce sont tes vrais renseignements.",
   items:[
    {q:"Quel est votre nom de famille ?", ph:"Mon nom de famille est…"},
    {q:"Quel est votre prénom ?", ph:"Mon prénom est…"},
    {q:"Quelle est votre date de naissance ?", ph:"Je suis né le… / Je suis née le…"},
    {q:"Quelle est votre adresse ?", ph:"J'habite au…"},
    {q:"Quel est votre numéro de téléphone ?", ph:"Mon numéro est…"},
   ]},
];
