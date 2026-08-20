const EXOS = [
 // ── JE DÉCOUVRE ─────────────────────────────────────────────
  {sec:'prep', id:'prVocab', type:'match', num:'Vocabulaire · 1', tit:'Le mot et sa définition', color:'#0D7A6F',
   sub:'Choisis un mot, puis sa définition. Six mots à la fois.', noQLbl:true, bankLbl:'Définitions', zonePh:'glisse la définition ici',
   rows: FC_CARDS.map((c,i)=>({id:'pv'+i, q:c.word, aid:'pv'+i, a:c.def}))},

  {sec:'prep', id:'pr1', type:'vf', num:'Exercice 1', tit:"Vrai ou Faux — Où est la bibliothèque ?", color:'#0D7A6F',
   sub:'Écoute de nouveau le dialogue, puis réponds.', tiles:['VRAI','FAUX'],
   savoir:{h:"› Les mots de la rue — à écouter et à répéter", speak:true, rows:[
     ["Où on marche","Deux mots pour se repérer dans la rue.", ["trottoir","coin"]],
     ["Ce qui arrête","On tourne souvent juste après.", ["feu"]],
     ["Sans tourner","La direction la plus simple.", ["tout droit"]],
   ]},
   rows:[
    {id:'p1a', txt:"Hassan cherche la bibliothèque.", ok:'VRAI'},
    {id:'p1b', txt:"La bibliothèque est très loin.", ok:'FAUX'},
    {id:'p1c', txt:"Il faut tourner à droite après le feu.", ok:'VRAI'},
    {id:'p1d', txt:"C'est à trente minutes à pied.", ok:'FAUX'},
   ]},

  {sec:'prep', id:'prHeure', type:'vf', num:'Exercice 2', tit:"Quelle heure entends-tu ?", color:'#0D7A6F', accent:'#0D7A6F', cards:true, listen:true,
   sub:"Écoute bien. Ces heures se ressemblent.", tiles:['LA PREMIÈRE','LA DEUXIÈME'],
   rows:[
    {id:'hra', txt:"huit heures dix", ok:'LA PREMIÈRE'},
    {id:'hrb', txt:"huit heures et demie", ok:'LA DEUXIÈME'},
    {id:'hrc', txt:"deux heures", ok:'LA PREMIÈRE'},
    {id:'hrd', txt:"douze heures", ok:'LA DEUXIÈME'},
    {id:'hre', txt:"trois heures et quart", ok:'LA PREMIÈRE'},
    {id:'hrf', txt:"treize heures", ok:'LA DEUXIÈME'},
   ]},

  {sec:'prep', id:'prImg', type:'imgmatch', num:'Exercice 3', tit:'Dans la rue', color:'#0D7A6F',
   sub:"Glisse chaque photo sur la phrase qui la décrit.",
   images:[
    {id:'ia1', src:'/assets/interactive/module-n2-autobus/images/arret-autobus.jpg'},
    {id:'ia2', src:'/assets/interactive/module-n2-autobus/images/feu-circulation.jpg'},
    {id:'ia3', src:'/assets/interactive/module-n2-autobus/images/plan-quartier.jpg'},
    {id:'ia4', src:'/assets/interactive/module-n2-autobus/images/horaire-affiche.jpg'},
    {id:'ia5', src:'/assets/interactive/module-n2-autobus/images/coin-rue.jpg'},
    {id:'ia6', src:'/assets/interactive/module-n2-autobus/images/avis-porte.jpg'},
   ],
   rows:[
    {id:'ia1', txt:"On attend l'autobus ici.", ok:'ia1'},
    {id:'ia2', txt:"Rouge, jaune, vert.", ok:'ia2'},
    {id:'ia3', txt:"Le quartier vu d'en haut.", ok:'ia3'},
    {id:'ia4', txt:"Il dit les heures de passage.", ok:'ia4'},
    {id:'ia5', txt:"Ici, deux rues se rencontrent.", ok:'ia5'},
    {id:'ia6', txt:"Un papier affiché sur une porte.", ok:'ia6'},
   ]},

  {sec:'prep', id:'prLieu', type:'match', num:'Exercice 4', tit:'Les lieux du quartier', color:'#0D7A6F',
   sub:"Associe chaque lieu à ce qu'on y fait.", bankLbl:'Ce quon y fait', zonePh:'glisse ici',
   rows:[
    {id:'l1', q:"la bibliothèque", aid:'l1', a:"emprunter des livres, gratuitement"},
    {id:'l2', q:"le CLSC", aid:'l2', a:"voir une infirmière ou un médecin"},
    {id:'l3', q:"la pharmacie", aid:'l3', a:"acheter des médicaments"},
    {id:'l4', q:"le bureau de poste", aid:'l4', a:"envoyer une lettre ou un colis"},
    {id:'l5', q:"le parc", aid:'l5', a:"marcher, jouer, se reposer dehors"},
    {id:'l6', q:"la piscine", aid:'l6', a:"nager, l'hiver comme l'été"},
   ]},

 // ── DÉFI 1 · DEMANDER SON CHEMIN ────────────────────────────
  {sec:'t1', id:'t1vf', type:'vf', num:'Exercice 1', tit:"Vrai ou Faux — Je répète pour être sûr", color:'#1D6B8F',
   sub:'Écoute de nouveau le dialogue, puis réponds.', tiles:['VRAI','FAUX'],
   rows:[
    {id:'t1a', txt:"Hassan demande de répéter plus lentement.", ok:'VRAI'},
    {id:'t1b', txt:"Il faut tourner à gauche au feu.", ok:'FAUX'},
    {id:'t1c', txt:"Hassan répète tout le chemin à la fin.", ok:'VRAI'},
    {id:'t1d', txt:"La bibliothèque est au coin, à gauche.", ok:'VRAI'},
   ]},

  {sec:'t1', id:'t1direction', type:'write', num:'Exercice 2', tit:'Les mots de la direction', color:'#1D6B8F', cols:2,
   sub:"Complète avec le mot qui convient.",
   savoir:{h:"› Cinq mots, et on va partout", speak:true, rows:[
     ["Tout droit","Sans tourner. « Continuez <b>tout droit</b> jusqu'au feu. »", ["tout droit"]],
     ["À droite, à gauche","Les deux côtés. « Tournez <b>à droite</b> après le feu. »", ["droite","gauche"]],
     ["Jusqu'à","Le point où l'on s'arrête. « <b>Jusqu'au</b> feu », « <b>jusqu'à</b> la rue Bélanger »."],
     ["Au coin de","Là où deux rues se rencontrent. « C'est <b>au coin</b>. »", ["coin"]],
     ["Après, avant","L'ordre des choses. « <b>Après</b> le feu », « <b>avant</b> le parc »."],
   ]},
   items:[
    {q:"Continuez ___ droit jusqu'au feu.", accept:["tout"], ph:"…"},
    {q:"Tournez ___ droite après le feu.", accept:["à","a"], ph:"…"},
    {q:"C'est au ___ de la rue Bélanger.", accept:["coin"], ph:"…"},
    {q:"Marchez ___ au parc.", accept:["jusqu'","jusqu"], ph:"…"},
    {q:"La pharmacie est ___ le feu, à gauche.", accept:["après","apres","avant"], ph:"…"},
   ]},

  {sec:'t1', id:'t1repeter', type:'write', num:'Exercice 3', tit:'Répéter pour être sûr', color:'#1D6B8F', cols:2,
   sub:"Que dis-tu pour vérifier ?",
   savoir:{h:"› Trois façons de vérifier", speak:true, rows:[
     ["Répéter le mot important","On vous dit « au feu, à droite » : vous répétez « à droite au feu ». La personne corrige si c'est faux.", ["droite"]],
     ["Redire tout le chemin","« Tout droit, à droite au feu, au coin à gauche. C'est ça ? » Trois choses, dans l'ordre."],
     ["Donner les deux possibilités","« À droite ou à gauche ? » La personne répond en un mot.", ["gauche"]],
     ["Demander plus lentement","« Plus lentement, s'il vous plaît. » Ce n'est pas le volume qui manque, c'est la vitesse."],
   ]},
   items:[
    {q:"On parle trop vite.", accept:["plus lentement s'il vous plaît","plus lentement","pouvez-vous répéter plus lentement"], ph:"…"},
    {q:"Tu veux vérifier tout le chemin.", accept:["c'est ça ?","c'est ça","est-ce que c'est ça ?"], ph:"…"},
    {q:"Tu n'es pas sûr du côté.", accept:["à droite ou à gauche ?","à droite ou à gauche","droite ou gauche ?"], ph:"…"},
    {q:"Tu veux savoir la distance.", accept:["c'est loin ?","c'est loin","c'est loin d'ici ?"], ph:"…"},
   ]},

  {sec:'t1', id:'t1b', type:'vf', num:'Exercice 4', tit:"Vrai ou Faux — C'est loin ?", color:'#1D6B8F',
   sub:'Écoute de nouveau le dialogue, puis réponds.', tiles:['VRAI','FAUX'],
   rows:[
    {id:'lb1', txt:"Le CLSC est près du parc.", ok:'VRAI'},
    {id:'lb2', txt:"À pied, c'est cinq minutes.", ok:'FAUX'},
    {id:'lb3', txt:"L'autobus 51 va au CLSC.", ok:'VRAI'},
    {id:'lb4', txt:"L'arrêt est devant l'école.", ok:'VRAI'},
   ]},

 // ── DÉFI 2 · L'AUTOBUS ET L'HORAIRE ─────────────────────────
  {sec:'t2', id:'t2vf', type:'vf', num:'Exercice 1', tit:'Vrai ou Faux — Le prochain autobus', color:'#B45309',
   sub:'Écoute de nouveau le dialogue, puis réponds.', tiles:['VRAI','FAUX'],
   rows:[
    {id:'q1', txt:"Le 51 passe à cet arrêt.", ok:'VRAI'},
    {id:'q2', txt:"Il passe aux trente minutes.", ok:'FAUX'},
    {id:'q3', txt:"Le prochain est à huit heures dix.", ok:'VRAI'},
    {id:'q4', txt:"Le dernier autobus est à onze heures et quart.", ok:'VRAI'},
   ]},

  {sec:'t2', id:'t2horaire', type:'write', num:'Exercice 2', tit:"Lire un horaire", color:'#B45309', cols:2,
   sub:"Complète : que dit l'horaire ?",
   savoir:{h:"› Ce qu'un horaire dit", speak:true, rows:[
     ["La fréquence","« Aux quinze minutes » : un autobus toutes les quinze minutes. Aux heures de pointe, c'est plus souvent.", ["horaire"]],
     ["Le premier et le dernier","Le dernier passage est la ligne la plus importante : après, il faut marcher ou payer un taxi.", ["heure"]],
     ["Semaine ou fin de semaine","Deux colonnes différentes. Le samedi et le dimanche, les autobus passent moins souvent."],
     ["La direction","Un même numéro va dans deux sens. Vérifiez le nom écrit devant l'autobus, pas seulement le numéro.", ["direction"]],
     ["La correspondance","Le petit papier — ou la carte — qui rend le deuxième autobus gratuit pendant deux heures.", ["correspondance"]],
   ]},
   items:[
    {q:"« Aux quinze minutes » veut dire : un autobus toutes les ___ minutes.", accept:["15","quinze"], ph:"un nombre"},
    {q:"Le ___ autobus passe à onze heures et quart.", accept:["dernier"], ph:"…"},
    {q:"La fin de semaine, les autobus passent ___ souvent.", accept:["moins"], ph:"…"},
    {q:"Le petit papier qui rend le deuxième autobus gratuit est la ___ .", accept:["correspondance"], ph:"…"},
    {q:"Il faut vérifier le numéro et la ___ .", accept:["direction"], ph:"…"},
   ]},

  {sec:'t2', id:'t2avis', type:'match', num:'Exercice 3', tit:'Que dit cet avis ?', color:'#B45309',
   sub:"Associe chaque avis à ce qu'il veut dire.", bankLbl:'Ce que ça veut dire', zonePh:'glisse ici',
   rows:[
    {id:'av1', q:"« Fermé le lundi 5 septembre »", aid:'av1', a:"c'est un jour férié : revenez mardi"},
    {id:'av2', q:"« Ouvert de 8 h à 16 h »", aid:'av2', a:"les heures d'ouverture de la journée"},
    {id:'av3', q:"« Arrêt déplacé — travaux »", aid:'av3', a:"l'autobus s'arrête ailleurs, plus loin"},
    {id:'av4', q:"« Service réduit »", aid:'av4', a:"il y a moins d'autobus que d'habitude"},
    {id:'av5', q:"« Sur rendez-vous seulement »", aid:'av5', a:"il faut téléphoner avant de venir"},
   ]},

  {sec:'t2', id:'t2b', type:'vf', num:'Exercice 4', tit:'Vrai ou Faux — Un avis sur la porte', color:'#B45309',
   sub:'Écoute de nouveau le dialogue, puis réponds.', tiles:['VRAI','FAUX'],
   rows:[
    {id:'b1', txt:"Le CLSC est fermé le lundi 5 septembre.", ok:'VRAI'},
    {id:'b2', txt:"C'est fermé parce qu'il y a des travaux.", ok:'FAUX'},
    {id:'b3', txt:"Le 5 septembre est un jour férié.", ok:'VRAI'},
    {id:'b4', txt:"Mardi, ils ouvrent à huit heures.", ok:'VRAI'},
   ]},

 // ── JE ME LANCE ─────────────────────────────────────────────
  {sec:'appli', id:'aQui', type:'vf', num:'Exercice 1', tit:'Qui parle ?', color:'#7E3F98',
   sub:"Écoute le dialogue « Une correspondance », puis réponds.", tiles:['HASSAN','LE CHAUFFEUR'],
   rows:[
    {id:'a1', txt:"« Je vais à l'hôpital. C'est le bon autobus ? »", ok:'HASSAN'},
    {id:'a2', txt:"« Vous devez prendre le 32. »", ok:'LE CHAUFFEUR'},
    {id:'a3', txt:"« Où est l'arrêt ? »", ok:'HASSAN'},
    {id:'a4', txt:"« Gardez votre correspondance. »", ok:'LE CHAUFFEUR'},
    {id:'a5', txt:"« Ma correspondance ? »", ok:'HASSAN'},
   ]},

  {sec:'appli', id:'aTrajet', type:'write', num:'Exercice 2', tit:'Mon trajet', color:'#7E3F98', cols:2,
   sub:"Écris ta réponse à chaque question.",
   items:[
    {q:"Où allez-vous chaque semaine ?", ph:"Je vais à…"},
    {q:"Quel autobus prenez-vous ?", ph:"Je prends le…"},
    {q:"Où est l'arrêt ?", ph:"L'arrêt est…"},
    {q:"Combien de temps ça prend ?", ph:"Ça prend…"},
   ]},
];
