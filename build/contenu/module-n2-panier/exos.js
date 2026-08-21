const EXOS = [
 // ── JE DÉCOUVRE ─────────────────────────────────────────────
  {sec:'prep', id:'prVocab', type:'match', num:'Vocabulaire · 1', tit:'Le mot et sa définition', color:'#0D7A6F',
   sub:'Choisis un mot, puis sa définition. Six mots à la fois.', noQLbl:true, bankLbl:'Définitions', zonePh:'glisse la définition ici',
   rows: FC_CARDS.map((c,i)=>({id:'pv'+i, q:c.word, aid:'pv'+i, a:c.def}))},

  {sec:'prep', id:'pr1', type:'vf', num:'Exercice 1', tit:"Vrai ou Faux — La circulaire du mardi", color:'#0D7A6F',
   sub:'Écoute de nouveau le dialogue, puis réponds.', tiles:['VRAI','FAUX'],
   savoir:{h:"› Les mots du magasin — à écouter et à répéter", speak:true, rows:[
     ["Le papier des prix","Il arrive dans la boîte aux lettres, une fois par semaine.", ["circulaire","spécial"]],
     ["Où sont les produits","On marche entre les tablettes, dans l'allée.", ["allée","tablette"]],
     ["Ce qu'on porte","On met dedans ce qu'on achète.", ["panier"]],
   ]},
   rows:[
    {id:'p1a', txt:"La circulaire arrive le mardi.", ok:'VRAI'},
    {id:'p1b', txt:"La circulaire est un journal.", ok:'FAUX'},
    {id:'p1c', txt:"Les chiffres de la circulaire sont les prix.", ok:'VRAI'},
    {id:'p1d', txt:"« Spécial » veut dire : plus cher cette semaine.", ok:'FAUX'},
   ]},

  {sec:'prep', id:'prSons', type:'vf', num:'Exercice 2', tit:"Le son [s] ou le son [z] ?", color:'#0D7A6F', accent:'#0D7A6F', cards:true, listen:true,
   sub:"Écoute chaque mot. Entends-tu [s] comme dans « salade », ou [z] comme dans « cerise » ?", tiles:['[s]','[z]'],
   savoir:{h:"› La lettre s se dit de deux façons", rows:[
     ["Entre deux voyelles, on dit [z]","une ceri<b>s</b>e, du rai<b>s</b>in, une framboi<b>s</b>e — le s est doux."],
     ["Deux s, on dit [s]","une sauci<b>ss</b>e, un de<b>ss</b>ert, un poi<b>ss</b>on — le s est dur."],
     ["Au début du mot, on dit [s]","<b>s</b>alade, <b>s</b>avon, <b>s</b>ac."],
   ]},
   rows:[
    {id:'so1', txt:"un dessert", ok:'[s]'},
    {id:'so2', txt:"une cerise", ok:'[z]'},
    {id:'so3', txt:"de la saucisse", ok:'[s]'},
    {id:'so4', txt:"du raisin", ok:'[z]'},
    {id:'so5', txt:"de la salade", ok:'[s]'},
    {id:'so6', txt:"une framboise", ok:'[z]'},
   ]},

  {sec:'prep', id:'prImg', type:'imgmatch', num:'Exercice 3', tit:"À l'épicerie", color:'#0D7A6F',
   sub:"Glisse chaque photo sur la phrase qui la décrit.",
   images:[
    {id:'ip1', src:'/assets/interactive/module-n2-panier/images/circulaire-table.jpg'},
    {id:'ip2', src:'/assets/interactive/module-n2-panier/images/allee-epicerie.jpg'},
    {id:'ip3', src:'/assets/interactive/module-n2-panier/images/panier-plein.jpg'},
    {id:'ip4', src:'/assets/interactive/module-n2-panier/images/balance-fruits.jpg'},
    {id:'ip5', src:'/assets/interactive/module-n2-panier/images/produits-entretien.jpg'},
    {id:'ip6', src:'/assets/interactive/module-n2-panier/images/caisse-epicerie.jpg'},
   ],
   rows:[
    {id:'ip1', txt:"Le papier des prix de la semaine.", ok:'ip1'},
    {id:'ip2', txt:"On marche ici, entre deux tablettes.", ok:'ip2'},
    {id:'ip3', txt:"On met les achats dedans.", ok:'ip3'},
    {id:'ip4', txt:"Elle dit le poids des fruits.", ok:'ip4'},
    {id:'ip5', txt:"Le savon et les produits pour laver.", ok:'ip5'},
    {id:'ip6', txt:"On paie ici, avant de sortir.", ok:'ip6'},
   ]},

  {sec:'prep', id:'prRayon', type:'match', num:'Exercice 4', tit:'Où est ce produit ?', color:'#0D7A6F',
   sub:"Associe chaque produit au rayon où il se trouve.", bankLbl:'Le rayon', zonePh:'glisse ici',
   rows:[
    {id:'r1', q:"le lait", aid:'r1', a:"les produits laitiers, au fond du magasin"},
    {id:'r2', q:"les pommes", aid:'r2', a:"les fruits et légumes, près de l'entrée"},
    {id:'r3', q:"le savon à vaisselle", aid:'r3', a:"les produits d'entretien, allée 7"},
    {id:'r4', q:"le pain", aid:'r4', a:"la boulangerie, près des caisses"},
    {id:'r5', q:"le poulet", aid:'r5', a:"la viande, au comptoir froid"},
    {id:'r6', q:"le riz", aid:'r6', a:"les produits secs, au milieu de l'allée"},
   ]},

 // ── DÉFI 1 · LIRE LA CIRCULAIRE ─────────────────────────────
  {sec:'t1', id:'t1vf', type:'vf', num:'Exercice 1', tit:"Vrai ou Faux — Deux pour neuf dollars", color:'#1D6B8F',
   sub:'Écoute de nouveau le dialogue, puis réponds.', tiles:['VRAI','FAUX'],
   rows:[
    {id:'t1a', txt:"« 2 pour 9 $ » : Aminata achète deux paquets.", ok:'VRAI'},
    {id:'t1b1', txt:"Un seul paquet coûte neuf dollars.", ok:'FAUX'},
    {id:'t1c', txt:"Un seul paquet coûte six dollars.", ok:'VRAI'},
    {id:'t1d', txt:"« 3,99 $ le kilo » est le prix des pommes.", ok:'VRAI'},
   ]},

  {sec:'t1', id:'t1prix', type:'write', num:'Exercice 2', tit:'Lire un prix', color:'#1D6B8F', cols:2,
   sub:"Complète avec le mot ou le nombre qui convient.",
   savoir:{h:"› Ce que les chiffres de la circulaire veulent dire", speak:true, rows:[
     ["3,99 $","On écrit une virgule. On dit « trois dollars quatre-vingt-dix-neuf ». Avant la virgule, les dollars ; après, les cents.", ["prix"]],
     ["3,99 $ / kg","Le prix d'un kilo. Si tu prends un demi-kilo, tu payes la moitié.", ["kilo"]],
     ["2 pour 9 $","Deux produits ensemble pour neuf dollars. Un seul produit coûte plus cher.", ["spécial"]],
     ["1,29 $ ch.","« ch. » veut dire « chacun » : un dollar vingt-neuf pour un seul produit."],
     ["la douzaine","Douze ensemble, dans la même boîte. C'est le format des œufs.", ["douzaine"]],
   ]},
   items:[
    {q:"« 2 pour 9 $ » : je prends ___ paquets.", accept:["2","deux"], ph:"un nombre"},
    {q:"« 2 pour 9 $ » : je paye ___ dollars.", accept:["9","neuf"], ph:"…"},
    {q:"« 3,99 $ » : il y a trois dollars et ___ cents.", accept:["99","quatre-vingt-dix-neuf"], ph:"…"},
    {q:"Le mot ___ veut dire : moins cher cette semaine.", accept:["spécial","special","« spécial »"], ph:"…"},
    {q:"« 3,99 $ / kg » est le prix d'un ___ .", accept:["kilo"], ph:"…"},
   ]},

  {sec:'t1', id:'t1des', type:'write', num:'Exercice 3', tit:'un, une, des — et « pas de »', color:'#1D6B8F', cols:2,
   sub:"Complète chaque phrase de la liste d'Aminata.",
   savoir:{h:"› Les petits mots devant le produit", speak:true, rows:[
     ["un — masculin","<span class='savoir-ex'><b>un</b> litre de lait, <b>un</b> kilo de riz, <b>un</b> sac</span>"],
     ["une — féminin","<span class='savoir-ex'><b>une</b> douzaine d'œufs, <b>une</b> boîte, <b>une</b> liste</span>", ["liste"]],
     ["des — plusieurs","<span class='savoir-ex'><b>des</b> pommes, <b>des</b> oranges, <b>des</b> œufs</span>"],
     ["À la forme négative, tout devient « de »","« J'ai du riz » → « je n'ai <b>pas de</b> riz ». « J'ai des œufs » → « je n'ai <b>pas d'</b>œufs »."],
     ["Devant une voyelle, « de » devient « d' »","<span class='savoir-ex'>pas <b>d'</b>œufs, pas <b>d'</b>oranges, pas <b>d'</b>eau</span>"],
   ]},
   items:[
    {q:"Je prends ___ litre de lait.", accept:["un"], ph:"un / une / des"},
    {q:"Je prends ___ douzaine d'œufs.", accept:["une"], ph:"…"},
    {q:"Je prends ___ oranges.", accept:["des"], ph:"…"},
    {q:"Je n'ai pas ___ riz.", accept:["de"], ph:"…"},
    {q:"Il n'y a pas ___ œufs dans le frigo.", accept:["d'","d","de"], ph:"…"},
   ]},

  {sec:'t1', id:'t1b', type:'vf', num:'Exercice 4', tit:'Vrai ou Faux — Ma liste', color:'#1D6B8F',
   sub:'Écoute de nouveau le dialogue, puis réponds.', tiles:['VRAI','FAUX'],
   rows:[
    {id:'lb1', txt:"Aminata écrit sa liste avant de partir.", ok:'VRAI'},
    {id:'lb2', txt:"Elle a encore du riz chez elle.", ok:'FAUX'},
    {id:'lb3', txt:"Les oranges sont en spécial.", ok:'VRAI'},
    {id:'lb4', txt:"Le sac d'oranges pèse deux kilos.", ok:'VRAI'},
   ]},

 // ── DÉFI 2 · L'ÉTIQUETTE ET L'AFFICHETTE ────────────────────
  {sec:'t2', id:'t2vf', type:'vf', num:'Exercice 1', tit:"Vrai ou Faux — C'est dans quelle allée ?", color:'#B45309',
   sub:'Écoute de nouveau le dialogue, puis réponds.', tiles:['VRAI','FAUX'],
   rows:[
    {id:'q1', txt:"Le savon à vaisselle est dans l'allée 7.", ok:'VRAI'},
    {id:'q2', txt:"Il est sur la tablette du haut.", ok:'FAUX'},
    {id:'q3', txt:"Le grand format coûte 4,29 $.", ok:'VRAI'},
    {id:'q4', txt:"Aminata répète le prix avant de partir.", ok:'VRAI'},
   ]},

  {sec:'t2', id:'t2combien', type:'write', num:'Exercice 2', tit:'La question courte', color:'#B45309', cols:2,
   sub:"Que dis-tu dans chaque situation ?",
   savoir:{h:"› Quatre questions, et on trouve tout", speak:true, rows:[
     ["Pour le prix","<span class='savoir-ex'>C'est <b>combien</b> ? · Ça coûte <b>combien</b> ?</span>", ["prix"]],
     ["Pour le rayon","<span class='savoir-ex'>C'est <b>où</b> ? · C'est dans quelle <b>allée</b> ?</span>", ["allée"]],
     ["Pour le format","<span class='savoir-ex'>C'est <b>quel format</b> ? · C'est le kilo ou le sac ?</span>"],
     ["Le mot interrogatif va à la fin","On ne dit pas « combien ça coûte ? » mais « ça coûte <b>combien</b> ? ». C'est la façon la plus simple, et elle est correcte."],
     ["Quand on n'a pas compris","<span class='savoir-ex'>Pouvez-vous répéter ? · Plus lentement, s'il vous plaît.</span>"],
   ]},
   items:[
    {q:"Tu veux savoir le prix.", accept:["c'est combien ?","c'est combien","ça coûte combien ?","ça coûte combien"], ph:"…"},
    {q:"Tu cherches le rayon d'un produit.", accept:["c'est où ?","c'est où","c'est dans quelle allée ?","c'est dans quelle allée"], ph:"…"},
    {q:"Tu veux savoir si c'est le kilo ou le sac.", accept:["c'est quel format ?","c'est quel format","quel format ?"], ph:"…"},
    {q:"Tu n'as pas compris le prix.", accept:["pouvez-vous répéter ?","pouvez-vous répéter","plus lentement, s'il vous plaît","répétez, s'il vous plaît"], ph:"…"},
    {q:"Tu veux savoir si le spécial est encore bon.", accept:["c'est encore le spécial ?","c'est encore le spécial"], ph:"…"},
   ]},

  {sec:'t2', id:'t2mesure', type:'write', num:'Exercice 3', tit:'Un kilo de riz, un litre de lait', color:'#B45309', cols:2,
   sub:"Complète avec « de » ou « d' ».",
   savoir:{h:"› La mesure, puis « de », puis le produit", speak:true, rows:[
     ["Le poids","Pour ce qui se pèse : le gramme et le kilo. Mille grammes font un kilo.", ["kilo","gramme"]],
     ["Le liquide","Pour ce qui se verse : le millilitre et le litre.", ["litre"]],
     ["La quantité","Pour ce qui se compte : la douzaine, le paquet, le sac, la boîte.", ["sac"]],
     ["Toujours « de » entre les deux","<span class='savoir-ex'>un kilo <b>de</b> riz · un litre <b>de</b> lait · un sac <b>de</b> pommes</span>"],
     ["Pas d'article après « de »","On dit « un litre <b>de</b> lait », jamais « un litre de <b>le</b> lait ». Le produit vient tout seul."],
     ["Devant une voyelle, « d' »","<span class='savoir-ex'>une douzaine <b>d'</b>œufs · un sac <b>d'</b>oranges</span>", ["étiquette","affichette"]],
   ]},
   items:[
    {q:"un litre ___ lait", accept:["de"], ph:"de / d'"},
    {q:"un kilo ___ riz", accept:["de"], ph:"…"},
    {q:"une douzaine ___ œufs", accept:["d'","d"], ph:"…"},
    {q:"un sac ___ oranges", accept:["d'","d"], ph:"…"},
    {q:"cent grammes ___ fromage", accept:["de"], ph:"…"},
   ]},

  {sec:'t2', id:'t2etiq', type:'match', num:'Exercice 4', tit:'Que dit ce petit papier ?', color:'#B45309',
   sub:"Associe chaque écriture à ce qu'elle veut dire.", bankLbl:'Ce que ça veut dire', zonePh:'glisse ici',
   rows:[
    {id:'e1', q:"« 908 g »", aid:'e1', a:"le poids : presque un kilo"},
    {id:'e2', q:"« 1 L »", aid:'e2', a:"un litre : du lait, du jus ou de l'eau"},
    {id:'e3', q:"« 3,99 $ / kg »", aid:'e3', a:"le prix d'un seul kilo"},
    {id:'e4', q:"« 2 pour 9 $ »", aid:'e4', a:"deux produits ensemble, pour neuf dollars"},
    {id:'e5', q:"« Meilleur avant : 12 mai »", aid:'e5', a:"la date : à manger avant ce jour"},
    {id:'e6', q:"« Grand format »", aid:'e6', a:"la grosse bouteille, pas la petite"},
   ]},

  {sec:'t2', id:'t2b', type:'vf', num:'Exercice 5', tit:'Vrai ou Faux — Un kilo ou un sac ?', color:'#B45309',
   sub:'Écoute de nouveau le dialogue, puis réponds.', tiles:['VRAI','FAUX'],
   rows:[
    {id:'b1', txt:"Il y a deux affichettes pour les oranges.", ok:'VRAI'},
    {id:'b2', txt:"Le sac d'oranges coûte 3,99 $.", ok:'VRAI'},
    {id:'b3', txt:"« 908 g » est un prix.", ok:'FAUX'},
    {id:'b4', txt:"908 grammes, c'est presque un kilo.", ok:'VRAI'},
   ]},

 // ── JE ME LANCE ─────────────────────────────────────────────
  {sec:'appli', id:'aQui', type:'vf', num:'Exercice 1', tit:'Qui parle ?', color:'#7E3F98',
   sub:"Écoute le dialogue « À la caisse », puis réponds.", tiles:['AMINATA','LE COMMIS'],
   rows:[
    {id:'a1', txt:"« Ça fait vingt-six dollars quinze. »", ok:'LE COMMIS'},
    {id:'a2', txt:"« Le poulet est en spécial. J'ai la circulaire. »", ok:'AMINATA'},
    {id:'a3', txt:"« Montrez-moi, s'il vous plaît. »", ok:'LE COMMIS'},
    {id:'a4', txt:"« Ça fait combien maintenant ? »", ok:'AMINATA'},
    {id:'a5', txt:"« Vous avez un sac ? »", ok:'LE COMMIS'},
   ]},

  {sec:'appli', id:'aListe', type:'write', num:'Exercice 2', tit:'Ma liste de la semaine', color:'#7E3F98', cols:2,
   sub:"Écris ta réponse à chaque question.",
   items:[
    {q:"Quel produit achètes-tu chaque semaine ?", ph:"J'achète…"},
    {q:"Dans quel format ? (le kilo, le litre, le sac…)", ph:"Un…"},
    {q:"Combien ça coûte ?", ph:"Ça coûte…"},
    {q:"Dans quel rayon est-ce que tu le trouves ?", ph:"Dans le rayon…"},
   ]},
];
