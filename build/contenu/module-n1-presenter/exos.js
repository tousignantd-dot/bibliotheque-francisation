const EXOS = [
 // ── JE DÉCOUVRE ─────────────────────────────────────────────
  {sec:'prep', id:'prVocab', type:'match', num:'Vocabulaire · 1', tit:'Le mot et sa définition', color:'#1D6B8F',
   sub:'Choisis un mot, puis sa définition. Six mots à la fois.', noQLbl:true, bankLbl:'Définitions', zonePh:'glisse la définition ici',
   rows: FC_CARDS.map((c,i)=>({id:'pv'+i, q:c.word, aid:'pv'+i, a:c.def}))},

  {sec:'prep', id:'pr1', type:'vf', num:'Exercice 1', tit:"Vrai ou Faux — Bonjour, je m'appelle Amina", color:'#1D6B8F',
   sub:'Écoute de nouveau le dialogue, puis réponds.', tiles:['VRAI','FAUX'],
   savoir:{h:"› Les premiers mots — à écouter et à répéter", speak:true, rows:[
     ["Se nommer","Deux mots pour dire qui on est.", ["nom","prénom"]],
     ["Dire les lettres","Quand on ne comprend pas votre nom, on vous demande ceci.", ["épeler"]],
     ["Dire où on habite","Le numéro et la rue.", ["adresse"]],
   ]},
   rows:[
    {id:'p1a', txt:"La femme s'appelle Amina.", ok:'VRAI'},
    {id:'p1b', txt:"Son nom de famille est Benali.", ok:'VRAI'},
    {id:'p1c', txt:"On lui demande d'épeler son nom.", ok:'VRAI'},
    {id:'p1d', txt:"Amina ne dit pas bonjour.", ok:'FAUX'},
   ]},

  {sec:'prep', id:'prAlpha', type:'write', num:'Exercice 2', tit:"Quelle lettre entends-tu ?", color:'#1D6B8F', cols:2,
   sub:"Ces lettres se ressemblent. Écoute, puis écris la lettre que tu entends.",
   items:[
    {q:"Lettre 1 — E ou I ?", audio:"La lettre I.", accept:["I"], ph:"une lettre"},
    {q:"Lettre 2 — E ou I ?", audio:"La lettre E.", accept:["E"], ph:"une lettre"},
    {q:"Lettre 3 — G ou J ?", audio:"La lettre G.", accept:["G"], ph:"une lettre"},
    {q:"Lettre 4 — G ou J ?", audio:"La lettre J.", accept:["J"], ph:"une lettre"},
    {q:"Lettre 5 — M ou N ?", audio:"La lettre N.", accept:["N"], ph:"une lettre"},
    {q:"Lettre 6 — M ou N ?", audio:"La lettre M.", accept:["M"], ph:"une lettre"},
   ]},

  {sec:'prep', id:'prImg', type:'imgmatch', num:'Exercice 3', tit:'Les mots du premier jour', color:'#1D6B8F',
   sub:"Glisse chaque photo sur la phrase qui la décrit.",
   images:[
    {id:'in1', src:'/assets/interactive/module-n1-presenter/images/formulaire.jpg'},
    {id:'in2', src:'/assets/interactive/module-n1-presenter/images/accueil-centre.jpg'},
    {id:'in3', src:'/assets/interactive/module-n1-presenter/images/carte-monde.jpg'},
    {id:'in4', src:'/assets/interactive/module-n1-presenter/images/salle-classe.jpg'},
    {id:'in5', src:'/assets/interactive/module-n1-presenter/images/poignee-main.jpg'},
    {id:'in6', src:'/assets/interactive/module-n1-presenter/images/porte-appartement.jpg'},
   ],
   rows:[
    {id:'in1', txt:"On écrit son nom et son adresse dessus.", ok:'in1'},
    {id:'in2', txt:"C'est ici qu'on arrive le premier jour.", ok:'in2'},
    {id:'in3', txt:"On y montre son pays.", ok:'in3'},
    {id:'in4', txt:"C'est ici qu'on apprend le français.", ok:'in4'},
    {id:'in5', txt:"On le fait pour dire bonjour.", ok:'in5'},
    {id:'in6', txt:"Le numéro est écrit à côté.", ok:'in6'},
   ]},

  {sec:'prep', id:'prNom', type:'write', num:'Exercice 4', tit:"Comment tu t'appelles ?", color:'#1D6B8F', cols:2,
   sub:"Complète d'après le dialogue.",
   savoir:{h:"› Épeler son nom", rows:[
     ["On vous le demandera souvent","Au centre, à la clinique, à la banque. Un nom qui ne vient pas d'ici ne s'écrit pas comme il se prononce : on vous demandera de l'épeler."],
     ["Une lettre à la fois, lentement","« A - M - I - N - A. » Faites une petite pause entre les lettres. C'est plus clair que de les dire vite."],
     ["Six lettres à surveiller","E et I, G et J, M et N se ressemblent beaucoup à l'oral en français. Ce sont celles qu'on fait répéter le plus souvent."],
     ["Le truc qui marche","Donnez un mot avec la lettre : « B comme bonjour ». Tout le monde le fait, même les gens d'ici."],
   ]},
   items:[
    {q:"— Comment vous appelez-vous ? — Je m'___ Amina.", accept:["appelle"], ph:"…"},
    {q:"Pouvez-vous ___ votre nom ?", accept:["épeler","epeler"], ph:"…"},
    {q:"Son nom de ___ est Benali.", accept:["famille"], ph:"…"},
    {q:"— Merci. — De ___ .", accept:["rien"], ph:"…"},
   ]},

 // ── DÉFI 1 · SE PRÉSENTER ───────────────────────────────────
  {sec:'t1', id:'t1vf', type:'vf', num:'Exercice 1', tit:"Vrai ou Faux — D'où viens-tu ?", color:'#0D7A6F',
   sub:'Écoute de nouveau le dialogue, puis réponds.', tiles:['VRAI','FAUX'],
   rows:[
    {id:'t1a', txt:"Lin vient du Vietnam.", ok:'VRAI'},
    {id:'t1b', txt:"Amina vient du Maroc.", ok:'FAUX'},
    {id:'t1c', txt:"Les deux habitent à Montréal.", ok:'VRAI'},
    {id:'t1d', txt:"Amina parle arabe.", ok:'VRAI'},
    {id:'t1e', txt:"Lin a trois enfants.", ok:'FAUX'},
    {id:'t1f', txt:"Amina a un fils de six ans.", ok:'VRAI'},
   ]},

  {sec:'t1', id:'t1etre', type:'write', num:'Exercice 2', tit:"Je suis, j'ai, je parle", color:'#0D7A6F', cols:2,
   sub:"Complète avec le bon verbe.",
   savoir:{h:"› Les cinq phrases pour se présenter", speak:true, rows:[
     ["Je m'appelle…","Le nom. C'est la première phrase, partout.", ["nom"]],
     ["Je viens de…","Le pays. « Je viens <b>d'</b>Algérie », « je viens <b>du</b> Vietnam », « je viens <b>de</b> France ».", ["pays"]],
     ["J'habite à…","La ville. « J'habite à Montréal », « j'habite à Laval ».", ["habiter"]],
     ["Je parle…","La langue. « Je parle arabe et un peu français. »", ["langue"]],
     ["J'ai…","Les enfants, l'âge. « J'ai un enfant. » « J'ai trente ans. »", ["enfant"]],
   ]},
   items:[
    {q:"Je m'___ Amina.", accept:["appelle"], ph:"…"},
    {q:"Je ___ d'Algérie.", accept:["viens"], ph:"…"},
    {q:"J'___ à Montréal.", accept:["habite"], ph:"…"},
    {q:"Je ___ arabe et français.", accept:["parle"], ph:"…"},
    {q:"J'___ un enfant.", accept:["ai"], ph:"…"},
    {q:"Je ___ mécanicienne.", accept:["suis"], ph:"…"},
   ]},

  {sec:'t1', id:'t1venir', type:'write', num:'Exercice 3', tit:"De, du, ou d' ?", color:'#0D7A6F', cols:2,
   sub:"Complète : je viens ___ …",
   savoir:{h:"› Devant le nom du pays", speak:true, rows:[
     ["d' devant une voyelle","Je viens <b>d'</b>Algérie, <b>d'</b>Haïti, <b>d'</b>Iran, <b>d'</b>Ukraine.", ["pays"]],
     ["du devant un pays masculin","Je viens <b>du</b> Vietnam, <b>du</b> Maroc, <b>du</b> Brésil, <b>du</b> Cameroun."],
     ["de devant un pays féminin","Je viens <b>de</b> France, <b>de</b> Colombie, <b>de</b> Chine, <b>de</b> Syrie."],
     ["des devant un pluriel","Je viens <b>des</b> Philippines, <b>des</b> États-Unis."],
     ["Comment savoir ?","On ne devine pas : on apprend son propre pays par cœur, et c'est tout ce qu'il faut pour se présenter."],
   ]},
   items:[
    {q:"Je viens ___ Algérie.", accept:["d'","d"], ph:"…"},
    {q:"Je viens ___ Vietnam.", accept:["du"], ph:"…"},
    {q:"Je viens ___ France.", accept:["de"], ph:"…"},
    {q:"Je viens ___ Philippines.", accept:["des"], ph:"…"},
    {q:"J'habite ___ Montréal.", accept:["à","a"], ph:"…"},
   ]},

  {sec:'t1', id:'t1b', type:'vf', num:'Exercice 4', tit:"Vrai ou Faux — Tu parles quelles langues ?", color:'#0D7A6F',
   sub:'Écoute de nouveau le dialogue, puis réponds.', tiles:['VRAI','FAUX'],
   rows:[
    {id:'lb1', txt:"Amina parle arabe.", ok:'VRAI'},
    {id:'lb2', txt:"Lin parle anglais.", ok:'VRAI'},
    {id:'lb3', txt:"Lin n'a pas d'enfants.", ok:'FAUX'},
    {id:'lb4', txt:"Le fils d'Amina a six ans.", ok:'VRAI'},
   ]},

 // ── DÉFI 2 · SALUER ET REMERCIER ────────────────────────────
  {sec:'t2', id:'t2vf', type:'vf', num:'Exercice 1', tit:'Vrai ou Faux — Merci beaucoup', color:'#B45309',
   sub:'Écoute de nouveau le dialogue, puis réponds.', tiles:['VRAI','FAUX'],
   rows:[
    {id:'q1', txt:"Amina dit qu'elle ne comprend pas.", ok:'VRAI'},
    {id:'q2', txt:"L'homme se fâche.", ok:'FAUX'},
    {id:'q3', txt:"Il répète plus lentement.", ok:'VRAI'},
    {id:'q4', txt:"Amina remercie.", ok:'VRAI'},
   ]},

  {sec:'t2', id:'t2poli', type:'write', num:'Exercice 2', tit:'Les mots de politesse', color:'#B45309', cols:2,
   sub:"Que dis-tu dans cette situation ?",
   savoir:{h:"› Six phrases à savoir par cœur", speak:true, rows:[
     ["Bonjour, bonsoir","<b>Bonjour</b> le jour, <b>bonsoir</b> le soir. On le dit en entrant, même dans un magasin.", ["bonjour","bonsoir"]],
     ["Merci, de rien","On remercie souvent ici. La réponse est <b>de rien</b>, <b>bienvenue</b>, ou <b>ça me fait plaisir</b>.", ["merci","de rien"]],
     ["Pardon","Pour s'excuser, et aussi pour faire répéter : « <b>Pardon ?</b> »", ["pardon"]],
     ["Je ne comprends pas","Ce n'est pas un échec. C'est une phrase de la langue, aussi utile que bonjour."],
     ["Plus lentement, s'il vous plaît","La phrase la plus utile de toutes : ce n'est pas le volume qui manque, c'est la vitesse.", ["lentement"]],
   ]},
   items:[
    {q:"Tu entres dans un magasin, le matin.", accept:["bonjour"], ph:"…"},
    {q:"Quelqu'un t'aide.", accept:["merci","merci beaucoup"], ph:"…"},
    {q:"On te dit merci.", accept:["de rien","bienvenue","ça me fait plaisir"], ph:"…"},
    {q:"Tu n'as pas compris.", accept:["pardon","je ne comprends pas","pardon ?"], ph:"…"},
    {q:"On parle trop vite.", accept:["plus lentement s'il vous plaît","plus lentement","moins vite s'il vous plaît"], ph:"…"},
   ]},

  {sec:'t2', id:'t2quand', type:'match', num:'Exercice 3', tit:'Quand le dit-on ?', color:'#B45309',
   sub:"Associe chaque mot au bon moment.", bankLbl:'Le moment', zonePh:'glisse ici',
   rows:[
    {id:'m1', q:"Bonjour", aid:'m1', a:"en arrivant, le jour"},
    {id:'m2', q:"Bonsoir", aid:'m2', a:"en arrivant, le soir"},
    {id:'m3', q:"Bonne journée", aid:'m3', a:"en partant, le jour"},
    {id:'m4', q:"Bonne soirée", aid:'m4', a:"en partant, le soir"},
    {id:'m5', q:"À demain", aid:'m5', a:"en partant, quand on se revoit demain"},
    {id:'m6', q:"Salut", aid:'m6', a:"entre amis, en arrivant ou en partant"},
   ]},

 // ── JE ME LANCE ─────────────────────────────────────────────
  {sec:'appli', id:'aQui', type:'vf', num:'Exercice 1', tit:'Qui parle ?', color:'#7E3F98',
   sub:"Écoute le dialogue « Au secrétariat », puis réponds.", tiles:['AMINA','LE SECRÉTAIRE'],
   rows:[
    {id:'a1', txt:"« Vous êtes une nouvelle élève ? »", ok:'LE SECRÉTAIRE'},
    {id:'a2', txt:"« Je m'appelle Amina Benali. »", ok:'AMINA'},
    {id:'a3', txt:"« Pouvez-vous épeler votre nom de famille ? »", ok:'LE SECRÉTAIRE'},
    {id:'a4', txt:"« Pardon ? Plus lentement, s'il vous plaît. »", ok:'AMINA'},
    {id:'a5', txt:"« J'habite au 4520, rue Bélanger. »", ok:'AMINA'},
   ]},

  {sec:'appli', id:'aFiche', type:'write', num:'Exercice 2', tit:'Ma fiche', color:'#7E3F98', cols:2,
   sub:"Écris ta réponse à chaque question.",
   items:[
    {q:"Comment vous appelez-vous ?", ph:"Je m'appelle…"},
    {q:"D'où venez-vous ?", ph:"Je viens de…"},
    {q:"Où habitez-vous ?", ph:"J'habite à…"},
    {q:"Quelles langues parlez-vous ?", ph:"Je parle…"},
   ]},
];
