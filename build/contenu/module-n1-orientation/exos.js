const EXOS = [
 // ── JE DÉCOUVRE ─────────────────────────────────────────────
  {sec:'prep', id:'prVocab', type:'match', num:'Vocabulaire · 1', tit:'Le mot et sa définition', color:'#1D6B8F',
   sub:'Choisis un mot, puis sa définition. Six mots à la fois.', noQLbl:true, bankLbl:'Définitions', zonePh:'glisse la définition ici',
   rows: FC_CARDS.map((c,i)=>({id:'pv'+i, q:c.word, aid:'pv'+i, a:c.def}))},

  {sec:'prep', id:'pr1', type:'vf', num:'Exercice 1', tit:'Vrai ou Faux — Les deux portes', color:'#1D6B8F',
   sub:'Écoute de nouveau le dialogue, puis réponds.', tiles:['VRAI','FAUX'],
   savoir:{h:"› Un panneau, c'est deux choses — à écouter et à répéter", speak:true, rows:[
     ["La plaque sur le mur ou sur la porte","Elle est toujours à la même hauteur, un peu au-dessus des yeux.", ["panneau"]],
     ["La petite image","Elle dit tout, même si on ne lit pas encore.", ["dessin"]],
     ["Le mot écrit à côté","Il dit la même chose que le dessin, avec des lettres.", ["mot"]],
     ["Le petit trait avec une pointe","Il ne nomme rien : il montre où aller.", ["flèche"]],
   ]},
   rows:[
    {id:'p1a', txt:"Rosa cherche les toilettes.", ok:'VRAI'},
    {id:'p1b', txt:"Il y a une seule porte.", ok:'FAUX'},
    {id:'p1c', txt:"Le même mot est écrit sur les deux portes.", ok:'VRAI'},
    {id:'p1d', txt:"Kofi ne sait pas lire le mot.", ok:'FAUX'},
   ]},

  {sec:'prep', id:'prSons', type:'vf', num:'Exercice 2', tit:'Quel son entends-tu ?', color:'#1D6B8F', accent:'#1D6B8F', cards:true, listen:true,
   sub:"Écoute le mot. Entends-tu [a], [i] ou [ou] ?", tiles:['[a]','[i]','[ou]'],
   rows:[
    {id:'so1', txt:"la", ok:'[a]'},
    {id:'so2', txt:"lit", ok:'[i]'},
    {id:'so3', txt:"loup", ok:'[ou]'},
    {id:'so4', txt:"salle", ok:'[a]'},
    {id:'so5', txt:"sortie", ok:'[i]'},
    {id:'so6', txt:"poussez", ok:'[ou]'},
   ]},

  {sec:'prep', id:'prImg', type:'imgmatch', num:'Exercice 3', tit:'Le dessin dit quoi ?', color:'#1D6B8F',
   sub:"Glisse chaque dessin sur la phrase qui le décrit.",
   images:[
    {id:'pi1', src:'/assets/interactive/module-n1-orientation/images/picto-toilettes.jpg'},
    {id:'pi2', src:'/assets/interactive/module-n1-orientation/images/picto-cafeteria.jpg'},
    {id:'pi3', src:'/assets/interactive/module-n1-orientation/images/picto-enfant.jpg'},
    {id:'pi4', src:'/assets/interactive/module-n1-orientation/images/picto-sortie.jpg'},
    {id:'pi5', src:'/assets/interactive/module-n1-orientation/images/picto-cigarette.jpg'},
    {id:'pi6', src:'/assets/interactive/module-n1-orientation/images/picto-fleche.jpg'},
   ],
   rows:[
    {id:'pi1', txt:"Un homme et une femme. Ici, ce sont les toilettes.", ok:'pi1'},
    {id:'pi2', txt:"Une fourchette et un couteau. Ici, on mange.", ok:'pi2'},
    {id:'pi3', txt:"Un grand et un petit. Ici, on laisse son enfant.", ok:'pi3'},
    {id:'pi4', txt:"Une personne qui court vers une porte. On part par ici.", ok:'pi4'},
    {id:'pi5', txt:"Une cigarette avec une barre rouge. C'est interdit.", ok:'pi5'},
    {id:'pi6', txt:"Un trait avec une pointe. Il montre où aller.", ok:'pi6'},
   ]},

  {sec:'prep', id:'prMaj', type:'write', num:'Exercice 4', tit:'Le même mot, deux écritures', color:'#1D6B8F', cols:2,
   sub:"Écris le mot en lettres minuscules.",
   savoir:{h:"› Sur les panneaux, tout est en MAJUSCULES", speak:true, rows:[
     ["Deux façons d'écrire une lettre","La grande et la petite. <span class='savoir-ex'>A et a · S et s · E et e</span>", ["majuscule"]],
     ["Les panneaux prennent les grandes","On les voit de loin. <span class='savoir-ex'>SORTIE · TOILETTES · POUSSEZ</span>", ["minuscule"]],
     ["Les livres prennent les petites","Le même mot, plus petit. <span class='savoir-ex'>sortie · toilettes · poussez</span>"],
     ["C'est le même mot","La lettre change de taille, pas de son.", ["mot"]],
   ]},
   items:[
    {q:"SORTIE →", accept:["sortie"], ph:"…"},
    {q:"ENTRÉE →", accept:["entrée","entree"], ph:"…"},
    {q:"TOILETTES →", accept:["toilettes"], ph:"…"},
    {q:"ACCUEIL →", accept:["accueil"], ph:"…"},
    {q:"POUSSEZ →", accept:["poussez"], ph:"…"},
    {q:"CAFÉTÉRIA →", accept:["cafétéria","cafeteria"], ph:"…"},
   ]},

 // ── DÉFI 1 · LE MOT SUR LA PORTE ────────────────────────────
  {sec:'t1', id:'t1vf', type:'vf', num:'Exercice 1', tit:"Vrai ou Faux — C'est écrit sur la porte", color:'#0D7A6F',
   sub:'Écoute de nouveau le dialogue, puis réponds.', tiles:['VRAI','FAUX'],
   rows:[
    {id:'t1a', txt:"Rosa lit le mot « cafétéria ».", ok:'VRAI'},
    {id:'t1b', txt:"On mange à la cafétéria, le midi.", ok:'VRAI'},
    {id:'t1c', txt:"Le dessin du service de garde montre une auto.", ok:'FAUX'},
    {id:'t1d', txt:"La fille de Rosa a quatre ans.", ok:'VRAI'},
   ]},

  {sec:'t1', id:'t1lieu', type:'match', num:'Exercice 2', tit:"Le mot et l'endroit", color:'#0D7A6F',
   sub:"Associe chaque mot du panneau à ce qu'on fait à cet endroit.", bankLbl:'Ce qu\'on y fait', zonePh:'glisse ici',
   rows:[
    {id:'lu1', q:"TOILETTES", aid:'lu1', a:"on se lave les mains"},
    {id:'lu2', q:"CAFÉTÉRIA", aid:'lu2', a:"on mange, le midi"},
    {id:'lu3', q:"ACCUEIL", aid:'lu3', a:"on pose une question"},
    {id:'lu4', q:"SERVICE DE GARDE", aid:'lu4', a:"on laisse son enfant"},
    {id:'lu5', q:"VESTIAIRE", aid:'lu5', a:"on laisse son manteau"},
    {id:'lu6', q:"SORTIE", aid:'lu6', a:"on part du bâtiment"},
   ]},

  {sec:'t1', id:'t1art', type:'write', num:'Exercice 3', tit:'Le, la ou les ?', color:'#0D7A6F', cols:2,
   sub:"Complète avec « le », « la » ou « les ».",
   savoir:{h:"› Le petit mot devant le nom du lieu", speak:true, rows:[
     ["la devant un nom féminin","<span class='savoir-ex'><b>la</b> cafétéria · <b>la</b> sortie · <b>la</b> classe</span>", ["cafétéria"]],
     ["le devant un nom masculin","<span class='savoir-ex'><b>le</b> vestiaire · <b>le</b> panneau · <b>le</b> service de garde</span>", ["vestiaire"]],
     ["les devant un nom au pluriel","<span class='savoir-ex'><b>les</b> toilettes · <b>les</b> escaliers</span>", ["toilettes"]],
     ["l' devant une voyelle","Le petit mot se colle. <span class='savoir-ex'><b>l'</b>accueil · <b>l'</b>entrée</span>", ["accueil"]],
     ["Le petit mot fait partie du mot","On l'apprend avec le nom, jamais après.", ["entrée"]],
   ]},
   items:[
    {q:"___ cafétéria est au premier étage.", accept:["la","La"], ph:"le / la / les"},
    {q:"___ toilettes sont au bout du corridor.", accept:["les","Les"], ph:"…"},
    {q:"___ vestiaire est à côté de l'entrée.", accept:["le","Le"], ph:"…"},
    {q:"___ sortie est à droite.", accept:["la","La"], ph:"…"},
    {q:"Je vais à ___ accueil.", accept:["l'","l"], ph:"…"},
    {q:"___ service de garde est au rez-de-chaussée.", accept:["le","Le"], ph:"…"},
   ]},

  {sec:'t1', id:'t1cest', type:'write', num:'Exercice 4', tit:"C'est ici, ou ce n'est pas ici ?", color:'#0D7A6F', cols:2,
   sub:"Regarde le panneau, puis complète la phrase.",
   savoir:{h:"› Deux phrases pour tout dire", speak:true, rows:[
     ["Pour nommer un endroit","On met « c'est » devant le nom. <span class='savoir-ex'><b>C'est</b> la cafétéria.</span>"],
     ["Pour dire que non","On met « ce n'est pas ». <span class='savoir-ex'><b>Ce n'est pas</b> la cafétéria.</span>"],
     ["À l'oral, on entend souvent","« C'est pas ici. » Le « ne » disparaît. C'est normal et c'est correct à l'oral.", ["ici"]],
     ["Pour demander","La même phrase, mais la voix monte à la fin. <span class='savoir-ex'>C'est ici ?</span>", ["panneau"]],
   ]},
   items:[
    {q:"Sur la porte, c'est écrit CAFÉTÉRIA. — ___ la cafétéria.", accept:["c'est","C'est","cest"], ph:"c'est / ce n'est pas"},
    {q:"Tu cherches les toilettes. Le panneau dit ACCUEIL. — ___ les toilettes.", accept:["ce n'est pas","Ce n'est pas","c'est pas"], ph:"…"},
    {q:"Tu cherches la sortie. Le panneau dit SORTIE. — ___ la sortie.", accept:["c'est","C'est","cest"], ph:"…"},
    {q:"Tu demandes à quelqu'un. — Le service de garde, ___ ici ?", accept:["c'est","C'est","cest"], ph:"…"},
   ]},

 // ── DÉFI 2 · LE PANNEAU QUI DIT QUOI FAIRE ──────────────────
  {sec:'t2', id:'t2vf', type:'vf', num:'Exercice 1', tit:'Vrai ou Faux — Poussez, tirez', color:'#B45309',
   sub:'Écoute de nouveau le dialogue, puis réponds.', tiles:['VRAI','FAUX'],
   rows:[
    {id:'t2a', txt:"La porte ne s'ouvre pas tout de suite.", ok:'VRAI'},
    {id:'t2b', txt:"Sur la porte, c'est écrit POUSSEZ.", ok:'FAUX'},
    {id:'t2c', txt:"« Tirez » veut dire : vers moi.", ok:'VRAI'},
    {id:'t2d', txt:"Le petit dessin rouge montre une cigarette.", ok:'VRAI'},
   ]},

  {sec:'t2', id:'t2ordre', type:'write', num:'Exercice 2', tit:'Poussez ou tirez ?', color:'#B45309', cols:2,
   sub:"Complète avec « poussez », « tirez » ou « entrez ».",
   savoir:{h:"› Les panneaux qui donnent un ordre finissent par -EZ", speak:true, rows:[
     ["La porte va loin de moi","<span class='savoir-ex'>POUSSEZ</span>", ["poussez"]],
     ["La porte vient vers moi","<span class='savoir-ex'>TIREZ</span>", ["tirez"]],
     ["On peut entrer","<span class='savoir-ex'>ENTREZ · SONNEZ · ATTENDEZ</span>", ["entrez"]],
     ["Tous finissent pareil","On écrit -EZ et on entend « é ». Le Z ne s'entend pas.", ["mot"]],
     ["C'est un ordre, pas une insulte","Le panneau parle à tout le monde. Il ne vous parle pas à vous en particulier."],
   ]},
   items:[
    {q:"La porte va de l'autre côté. C'est écrit ___ .", accept:["poussez","POUSSEZ"], ph:"…"},
    {q:"La porte vient vers moi. C'est écrit ___ .", accept:["tirez","TIREZ"], ph:"…"},
    {q:"Le bureau est ouvert. Sur la porte : ___ .", accept:["entrez","ENTREZ"], ph:"…"},
    {q:"Les trois mots finissent par les mêmes deux lettres : ___ .", accept:["ez","-ez","EZ"], ph:"…"},
   ]},

  {sec:'t2', id:'t2neg', type:'vf', num:'Exercice 3', tit:'Permis ou interdit ?', color:'#B45309', cards:true,
   sub:"Lis le panneau. Est-ce permis, ou est-ce interdit ?", tiles:['C\'EST PERMIS','C\'EST INTERDIT'],
   savoir:{h:"› La barre rouge veut dire non", speak:true, rows:[
     ["Un dessin sans barre","On peut le faire. <span class='savoir-ex'>C'est permis.</span>", ["permis"]],
     ["Un dessin avec une barre rouge","On ne le fait pas. <span class='savoir-ex'>C'est interdit.</span>", ["interdit"]],
     ["Les mots de l'interdiction","<span class='savoir-ex'>DÉFENSE DE FUMER · NE PAS ENTRER</span>", ["défense de fumer"]],
     ["Deux petits mots à repérer","« ne… pas » et « défense de ». Dès qu'on les voit, c'est non."],
   ]},
   rows:[
    {id:'ne1', txt:"Une cigarette avec une barre rouge.", ok:"C'EST INTERDIT"},
    {id:'ne2', txt:"ENTREZ", ok:"C'EST PERMIS"},
    {id:'ne3', txt:"DÉFENSE DE FUMER", ok:"C'EST INTERDIT"},
    {id:'ne4', txt:"NE PAS ENTRER", ok:"C'EST INTERDIT"},
    {id:'ne5', txt:"Un dessin de verre d'eau, sans barre.", ok:"C'EST PERMIS"},
    {id:'ne6', txt:"Un dessin de chien avec une barre rouge.", ok:"C'EST INTERDIT"},
   ]},

  {sec:'t2', id:'t2secours', type:'match', num:'Exercice 4', tit:'Le panneau et ce qu\'il veut dire', color:'#B45309',
   sub:"Associe chaque panneau à sa phrase.", bankLbl:'Ce que ça veut dire', zonePh:'glisse ici',
   rows:[
    {id:'se1', q:"SORTIE DE SECOURS", aid:'se1', a:"la porte verte, pour partir vite en cas de danger"},
    {id:'se2', q:"DÉFENSE DE FUMER", aid:'se2', a:"on ne fume pas ici"},
    {id:'se3', q:"POUSSEZ", aid:'se3', a:"la porte s'ouvre de l'autre côté"},
    {id:'se4', q:"TIREZ", aid:'se4', a:"la porte s'ouvre vers moi"},
    {id:'se5', q:"ENTRÉE", aid:'se5', a:"la porte par où on arrive"},
    {id:'se6', q:"SILENCE", aid:'se6', a:"on ne parle pas fort ici"},
   ]},

 // ── JE ME LANCE ─────────────────────────────────────────────
  {sec:'appli', id:'aQui', type:'vf', num:'Exercice 1', tit:'Qui parle ?', color:'#7E3F98',
   sub:"Écoute le dialogue « Le tour du centre », puis réponds.", tiles:['ROSA','MADAME PARÉ'],
   rows:[
    {id:'aq1', txt:"« C'est votre première journée ? »", ok:'MADAME PARÉ'},
    {id:'aq2', txt:"« Moi, ça fait deux semaines. »", ok:'ROSA'},
    {id:'aq3', txt:"« Et la porte verte, au fond ? »", ok:'MADAME PARÉ'},
    {id:'aq4', txt:"« C'est la sortie. Le dessin, c'est une porte. »", ok:'ROSA'},
    {id:'aq5', txt:"« Vous lisez les panneaux. »", ok:'MADAME PARÉ'},
   ]},

  {sec:'appli', id:'aPanneaux', type:'write', num:'Exercice 2', tit:'Les cinq panneaux de mon centre', color:'#7E3F98', cols:2,
   sub:"Regarde autour de toi et écris ce que dit chaque panneau.",
   items:[
    {q:"Le panneau des toilettes, chez toi, dit :", ph:"TOILETTES…"},
    {q:"Le panneau de la sortie dit :", ph:"SORTIE…"},
    {q:"Un panneau avec une barre rouge dit :", ph:"DÉFENSE DE…"},
    {q:"Un panneau sur une porte dit :", ph:"POUSSEZ / TIREZ…"},
   ]},
];
