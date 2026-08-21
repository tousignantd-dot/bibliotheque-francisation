const EXOS = [
 // ── JE DÉCOUVRE ─────────────────────────────────────────────
  {sec:'prep', id:'prVocab', type:'match', num:'Vocabulaire · 1', tit:"Les seize mots de l'inscription", color:'#0D7A6F',
   sub:"Prends un mot de l'inscription, puis glisse dessus sa définition. Six à la fois.", noQLbl:true, bankLbl:'Définitions', zonePh:'glisse la définition ici',
   rows: FC_CARDS.map((c,i)=>({id:'pv'+i, q:c.word, aid:'pv'+i, a:c.def}))},

  {sec:'prep', id:'pr1', type:'vf', num:'Exercice 1', tit:"Vrai ou Faux — Je voudrais m'inscrire", color:'#0D7A6F',
   sub:"Réécoute Yara et madame Bourgeois au comptoir, puis réponds.", tiles:['VRAI','FAUX'],
   savoir:{h:"› Les mots du secrétariat — à écouter et à répéter", speak:true, rows:[
     ["Le bureau où on s'inscrit","On y va avec ses papiers, jamais avec ses cahiers.", ["secrétariat"]],
     ["La feuille pleine de cases","On la remplit une case à la fois.", ["formulaire"]],
     ["Le petit espace vide","Une case, une réponse. Jamais deux.", ["case"]],
     ["Ce qu'on fait pour entrer dans un cours","On donne son nom, sa date de naissance, son adresse.", ["inscription"]],
   ]},
   rows:[
    {id:'p1a', txt:"Yara veut s'inscrire au cours de français.", ok:'VRAI'},
    {id:'p1b', txt:"Madame Bourgeois dit que c'est le mauvais endroit.", ok:'FAUX'},
    {id:'p1c', txt:"Le formulaire a beaucoup de cases.", ok:'VRAI'},
    {id:'p1d', txt:"Yara remplit le formulaire toute seule.", ok:'FAUX'},
    {id:'p1e', txt:"On commence par le nom.", ok:'VRAI'},
   ]},

  {sec:'prep', id:'prAlpha', type:'vf', num:'Exercice 2', tit:"La lettre finit par « é » ou par « è » ?", color:'#0D7A6F', accent:'#0D7A6F', cards:true, listen:true,
   sub:"Écoute chaque lettre de l'alphabet. Est-ce qu'on entend « é » ou « è » ?", tiles:['SON « É »','SON « È »'],
   savoir:{h:"› L'alphabet se dit en deux familles", rows:[
     ["La famille du « é »","<span class='savoir-ex'><b>B</b>é · <b>C</b>é · <b>D</b>é · <b>G</b>é · <b>P</b>é · <b>T</b>é · <b>V</b>é</span>"],
     ["La famille du « è »","<span class='savoir-ex'>è<b>F</b> · è<b>L</b> · è<b>M</b> · è<b>N</b> · è<b>R</b> · è<b>S</b></span>"],
     ["Dans la première famille","la lettre vient <b>avant</b> le son."],
     ["Dans la deuxième famille","la lettre vient <b>après</b> le son."],
     ["Le piège du comptoir","<span class='savoir-ex'><b>B</b> et <b>V</b> · <b>M</b> et <b>N</b> · <b>G</b> et <b>J</b> — on dit alors « B comme bonjour ».</span>"],
   ]},
   rows:[
    {id:'al1', txt:"la lettre B", ok:'SON « É »'},
    {id:'al2', txt:"la lettre F", ok:'SON « È »'},
    {id:'al3', txt:"la lettre D", ok:'SON « É »'},
    {id:'al4', txt:"la lettre M", ok:'SON « È »'},
    {id:'al5', txt:"la lettre P", ok:'SON « É »'},
    {id:'al6', txt:"la lettre S", ok:'SON « È »'},
    {id:'al7', txt:"la lettre T", ok:'SON « É »'},
    {id:'al8', txt:"la lettre L", ok:'SON « È »'},
   ]},

  // ── prImg — l'exercice à photos, en attente des images ───────────────
  // Écrit d'abord en `imgmatch` sur six photos du secrétariat. Le compte
  // fal.ai était verrouillé faute de crédit (« User is locked. Reason:
  // TOP_UP ») le jour de la production : une seule des six images est sortie.
  // Un glisser-déposer de photos avec cinq vignettes cassées ne vaut rien, et
  // laisser l'exercice tel quel aurait mis l'écart sous les yeux de l'élève.
  // Il est donc rendu en `match` — les mêmes six phrases, associées au mot du
  // secrétariat qu'elles décrivent — et le module est complet sans image.
  //
  // Pour le rendre à sa forme d'origine quand les six fichiers de
  // `assets/interactive/module-n2-inscription/images/` existeront : remettre
  // `type:'imgmatch'`, le bloc `images:` avec is1…is6, et les six `rows` avec
  // leur `ok:'isN'`. Les noms de fichiers sont dans `gen_images.py`, dans
  // l'ordre des six phrases ci-dessous.
  {sec:'prep', id:'prImg', type:'match', num:'Exercice 3', tit:"Ce qu'on voit au secrétariat", color:'#0D7A6F',
   sub:"Prends une phrase du secrétariat, puis glisse dessus le mot qui va avec.", bankLbl:'Les mots', zonePh:'glisse le mot ici',
   rows:[
    {id:'is1', q:"Le comptoir où on donne ses papiers.", aid:'is1', a:"le secrétariat"},
    {id:'is2', q:"La feuille avec des cases vides.", aid:'is2', a:"un formulaire"},
    {id:'is3', q:"Le tableau de liège où on affiche les annonces.", aid:'is3', a:"un babillard"},
    {id:'is4', q:"La feuille des jours et des mois de l'année.", aid:'is4', a:"un calendrier"},
    {id:'is5', q:"Le nom écrit à la main au bas d'une page.", aid:'is5', a:"une signature"},
    {id:'is6', q:"La petite carte avec un nom et une photo.", aid:'is6', a:"une pièce d'identité"},
   ]},

  {sec:'prep', id:'prQuel', type:'write', num:'Exercice 4', tit:"Quel est votre nom ?", color:'#0D7A6F', cols:2,
   sub:"Complète chaque question avec « quel » ou « quelle ».",
   savoir:{h:"› Les questions du comptoir", speak:true, rows:[
     ["Devant un mot masculin","<span class='savoir-ex'><b>Quel</b> est votre nom ? · <b>Quel</b> est votre prénom ?</span>", ["prénom"]],
     ["Devant un mot féminin","<span class='savoir-ex'><b>Quelle</b> est votre adresse ? · <b>Quelle</b> est votre date de naissance ?</span>", ["adresse"]],
     ["Les deux se disent pareil","On entend « kèl » dans les deux cas. Seule l'écriture change.", ["date de naissance"]],
     ["Plus court, au comptoir","<span class='savoir-ex'>Votre nom, s'il vous plaît. · Votre courriel ?</span>", ["courriel"]],
     ["Quand la question va trop vite","<span class='savoir-ex'>Pouvez-vous répéter, s'il vous plaît ?</span>"],
   ]},
   items:[
    {q:"___ est votre nom de famille ?", accept:["Quel","quel"], ph:"Quel / Quelle"},
    {q:"___ est votre adresse ?", accept:["Quelle","quelle"], ph:"…"},
    {q:"___ est votre prénom ?", accept:["Quel","quel"], ph:"…"},
    {q:"___ est votre date de naissance ?", accept:["Quelle","quelle"], ph:"…"},
    {q:"___ est votre numéro de téléphone ?", accept:["Quel","quel"], ph:"…"},
    {q:"___ est votre scolarité ?", accept:["Quelle","quelle"], ph:"…"},
   ]},

 // ── DÉFI 1 · LA PETITE ANNONCE ──────────────────────────────
  {sec:'t1', id:'t1vf', type:'vf', num:'Exercice 1', tit:"Vrai ou Faux — L'annonce sur le babillard", color:'#1D6B8F',
   sub:"Réécoute Marco et Yara devant le babillard, puis réponds.", tiles:['VRAI','FAUX'],
   rows:[
    {id:'q1', txt:"Marco montre une annonce à Yara.", ok:'VRAI'},
    {id:'q2', txt:"C'est une annonce pour un cours d'anglais.", ok:'FAUX'},
    {id:'q3', txt:"Le cours commence le 7 septembre.", ok:'VRAI'},
    {id:'q4', txt:"Le cours est le soir.", ok:'FAUX'},
    {id:'q5', txt:"L'inscription se fait au local 005.", ok:'VRAI'},
   ]},

  {sec:'t1', id:'t1annonce', type:'vf', num:'Exercice 2', tit:"Lire l'annonce affichée", color:'#1D6B8F',
   sub:"Lis l'annonce dans le bandeau noir, puis réponds.", tiles:['VRAI','FAUX'],
   savoir:{h:"› COURS DE FRANÇAIS — Centre Delorme", rows:[
     ["Cours","Français, niveau 2 · groupe du matin"],
     ["Dates","du lundi 7 septembre au vendredi 11 décembre"],
     ["Horaire","du lundi au vendredi, de 8 h 30 à 12 h 30"],
     ["Lieu","Centre Delorme, local 214, deuxième étage"],
     ["Inscription","du 24 au 28 août, de 9 h à 15 h, au local 005"],
     ["À apporter","une pièce d'identité"],
   ]},
   rows:[
    {id:'r1', txt:"Le cours finit le 11 décembre.", ok:'VRAI'},
    {id:'r2', txt:"Le cours est le samedi.", ok:'FAUX'},
    {id:'r3', txt:"Le cours dure quatre heures par jour.", ok:'VRAI'},
    {id:'r4', txt:"L'inscription se fait au mois d'août.", ok:'VRAI'},
    {id:'r5', txt:"On s'inscrit dans le local du cours.", ok:'FAUX'},
    {id:'r6', txt:"Il faut apporter une pièce d'identité.", ok:'VRAI'},
   ]},

  {sec:'t1', id:'t1date', type:'write', num:'Exercice 3', tit:"Une date écrite en chiffres", color:'#1D6B8F', cols:2,
   sub:"Écris le mois de chaque date. Regarde bien où sont les chiffres.",
   savoir:{h:"› Les trois façons d'écrire une date", speak:true, rows:[
     ["En toutes lettres","<span class='savoir-ex'>le 7 septembre 2026</span> — c'est la plus claire.", ["date"]],
     ["Avec des barres","<span class='savoir-ex'>07/09/2026</span> — jour, mois, année."],
     ["Avec des traits, à l'envers","<span class='savoir-ex'>2026-09-07</span> — année, mois, jour. C'est la forme des papiers du gouvernement."],
     ["Le mois est toujours au milieu","Le nombre du milieu ne dépasse jamais 12."],
     ["Les douze mois","<span class='savoir-ex'>01 janvier · 02 février · 03 mars · 04 avril · 05 mai · 06 juin</span>"],
     ["La suite","<span class='savoir-ex'>07 juillet · 08 août · 09 septembre · 10 octobre · 11 novembre · 12 décembre</span>", ["cours"]],
   ]},
   items:[
    {q:"07/09/2026 → le 7 ___ 2026", accept:["septembre"], ph:"le mois"},
    {q:"2026-12-11 → le 11 ___ 2026", accept:["décembre","decembre"], ph:"…"},
    {q:"24/08/2026 → le 24 ___ 2026", accept:["août","aout"], ph:"…"},
    {q:"1994-03-07 → le 7 ___ 1994", accept:["mars"], ph:"…"},
    {q:"05/01/2027 → le 5 ___ 2027", accept:["janvier"], ph:"…"},
    {q:"2026-10-02 → le 2 ___ 2026", accept:["octobre"], ph:"…"},
   ]},

  {sec:'t1', id:'t1heure', type:'write', num:'Exercice 4', tit:"À 8 h 30, du lundi au vendredi", color:'#1D6B8F', cols:2,
   sub:"Complète avec « à », « de », « à » ou « du… au ».",
   savoir:{h:"› Dire quand, en trois petits mots", speak:true, rows:[
     ["Une heure : à","<span class='savoir-ex'>Le cours commence <b>à</b> 8 h 30.</span>", ["horaire"]],
     ["Du début à la fin : de… à","<span class='savoir-ex'><b>De</b> 8 h 30 <b>à</b> 12 h 30.</span>", ["cours"]],
     ["Deux jours, deux dates : du… au","<span class='savoir-ex'><b>Du</b> lundi <b>au</b> vendredi. · <b>Du</b> 24 <b>au</b> 28 août.</span>", ["date"]],
     ["Un jour de la semaine : le","<span class='savoir-ex'><b>Le</b> lundi, il y a un cours.</span>"],
     ["L'heure s'écrit avec un h","<span class='savoir-ex'>8 h 30 · 12 h 30 · 9 h · 15 h</span>", ["lieu"]],
   ]},
   items:[
    {q:"Le cours commence ___ 8 h 30.", accept:["à","a"], ph:"à / de / du"},
    {q:"Le cours est ___ 8 h 30 à 12 h 30.", accept:["de"], ph:"…"},
    {q:"Le cours est du lundi ___ vendredi.", accept:["au"], ph:"…"},
    {q:"L'inscription est ___ 24 au 28 août.", accept:["du"], ph:"…"},
    {q:"Le secrétariat ferme ___ 15 h.", accept:["à","a"], ph:"…"},
   ]},

  {sec:'t1', id:'t1notes', type:'write', num:'Exercice 5', tit:"Je prends mes notes", color:'#1D6B8F', cols:2,
   sub:"Relis l'annonce de l'exercice 2, puis remplis ta fiche de notes.",
   savoir:{h:"› Prendre en note : quatre mots suffisent", speak:true, rows:[
     ["On n'écrit pas la phrase","On écrit seulement le renseignement.", ["annonce"]],
     ["Quatre choses, toujours les mêmes","<span class='savoir-ex'>quoi · quand · à quelle heure · où</span>"],
     ["Les chiffres avant les mots","Une date et une heure se copient <b>exactement</b>.", ["date"]],
     ["Le lieu se copie aussi","<span class='savoir-ex'>local 005 · local 214</span>", ["lieu"]],
     ["On relit une fois","Un chiffre mal copié, et on arrive le mauvais jour.", ["horaire"]],
   ]},
   items:[
    {q:"Cours : ___", accept:["français","francais","cours de français","cours de francais"], ph:"quoi ?"},
    {q:"Premier jour : le ___ septembre", accept:["7"], ph:"quand ?"},
    {q:"Dernier jour : le ___ décembre", accept:["11"], ph:"…"},
    {q:"Heure : de ___ à 12 h 30", accept:["8 h 30","8h30","8 h30","8h 30"], ph:"…"},
    {q:"Local du cours : ___", accept:["214","local 214","le 214"], ph:"où ?"},
    {q:"Local de l'inscription : ___", accept:["005","local 005","le 005","5"], ph:"…"},
   ]},

  {sec:'t1', id:'t1b', type:'vf', num:'Exercice 6', tit:"Vrai ou Faux — J'appelle le secrétariat", color:'#1D6B8F',
   sub:"Réécoute l'appel de Yara au secrétariat, puis réponds.", tiles:['VRAI','FAUX'],
   rows:[
    {id:'s1', txt:"Yara téléphone pour le cours de français.", ok:'VRAI'},
    {id:'s2', txt:"L'inscription est du 24 au 28 août.", ok:'VRAI'},
    {id:'s3', txt:"Le secrétariat ouvre à 15 h.", ok:'FAUX'},
    {id:'s4', txt:"Le local 005 est au deuxième étage.", ok:'FAUX'},
    {id:'s5', txt:"Yara doit apporter une pièce d'identité.", ok:'VRAI'},
   ]},

 // ── DÉFI 2 · LE FORMULAIRE D'INSCRIPTION ────────────────────
  {sec:'t2', id:'t2vf', type:'vf', num:'Exercice 1', tit:"Vrai ou Faux — Case par case", color:'#B45309',
   sub:"Réécoute madame Bourgeois et Yara au comptoir, puis réponds.", tiles:['VRAI','FAUX'],
   rows:[
    {id:'u1', txt:"Le nom de famille de Yara, c'est Haddad.", ok:'VRAI'},
    {id:'u2', txt:"Sa date de naissance, c'est le 7 mars 1994.", ok:'VRAI'},
    {id:'u3', txt:"Elle habite rue Papineau, à Montréal.", ok:'VRAI'},
    {id:'u4', txt:"Elle a fait neuf années d'école.", ok:'FAUX'},
    {id:'u5', txt:"Le nombre d'années d'école va dans la case « scolarité ».", ok:'VRAI'},
   ]},

  {sec:'t2', id:'t2case', type:'match', num:'Exercice 2', tit:"La case et ce qu'on écrit dedans", color:'#B45309',
   sub:"Associe chaque case du formulaire à ce que Yara écrit dedans.", bankLbl:"Ce que Yara écrit", zonePh:'glisse ici',
   rows:[
    {id:'c1', q:"Nom de famille", aid:'c1', a:"HADDAD"},
    {id:'c2', q:"Prénom", aid:'c2', a:"Yara"},
    {id:'c3', q:"Date de naissance", aid:'c3', a:"1994-03-07"},
    {id:'c4', q:"Adresse", aid:'c4', a:"3420, rue Papineau, Montréal"},
    {id:'c5', q:"Téléphone", aid:'c5', a:"514 555-0182"},
    {id:'c6', q:"Courriel", aid:'c6', a:"yara.haddad@courriel.ca"},
    {id:'c7', q:"Scolarité", aid:'c7', a:"11 ans"},
    {id:'c8', q:"Signature", aid:'c8', a:"son nom écrit à la main"},
   ]},

  {sec:'t2', id:'t2form', type:'write', num:'Exercice 3', tit:"Remplir les cases", color:'#B45309', cols:2,
   sub:"Lis le formulaire dans le bandeau noir, puis écris le nom de la bonne case.",
   savoir:{h:"› FORMULAIRE D'INSCRIPTION — Centre Delorme", speak:true, rows:[
     ["Case 1 — Nom de famille","En lettres majuscules, comme sur la pièce d'identité.", ["nom de famille"]],
     ["Case 2 — Prénom","Une majuscule au début, le reste en petites lettres.", ["prénom"]],
     ["Case 3 — Date de naissance","Année, mois, jour : 1994-03-07.", ["date de naissance"]],
     ["Case 4 — Adresse","Le numéro, la rue, la ville, le code postal.", ["adresse"]],
     ["Case 5 — Téléphone et courriel","Dix chiffres pour le téléphone.", ["courriel"]],
     ["Case 6 — Scolarité","Le nombre d'années d'école, en chiffres.", ["scolarité"]],
     ["Au bas de la page","La date du jour et la signature.", ["signature"]],
   ]},
   items:[
    {q:"J'écris HADDAD dans la case ___ .", accept:["nom de famille","nom","Nom de famille"], ph:"le nom de la case"},
    {q:"J'écris 1994-03-07 dans la case ___ .", accept:["date de naissance","Date de naissance","naissance"], ph:"…"},
    {q:"J'écris 3420, rue Papineau dans la case ___ .", accept:["adresse","Adresse"], ph:"…"},
    {q:"J'écris 11 dans la case ___ .", accept:["scolarité","scolarite","Scolarité"], ph:"…"},
    {q:"J'écris mon nom à la main au bas de la page : c'est la ___ .", accept:["signature","Signature"], ph:"…"},
   ]},

  {sec:'t2', id:'t2mon', type:'write', num:'Exercice 4', tit:"Mon, ma, mes — votre, vos", color:'#B45309', cols:2,
   sub:"Complète le dialogue du comptoir avec « mon », « ma », « mes », « votre » ou « vos ».",
   savoir:{h:"› Le mot qui dit à qui c'est", speak:true, rows:[
     ["La secrétaire parle de toi","<span class='savoir-ex'><b>votre</b> nom · <b>votre</b> adresse · <b>vos</b> papiers</span>", ["adresse"]],
     ["Toi, tu parles de toi","<span class='savoir-ex'><b>mon</b> nom · <b>ma</b> rue · <b>mes</b> papiers</span>", ["nom de famille"]],
     ["Un mot masculin : mon","<span class='savoir-ex'><b>mon</b> prénom · <b>mon</b> courriel</span>", ["prénom"]],
     ["Un mot féminin : ma","<span class='savoir-ex'><b>ma</b> date de naissance · <b>ma</b> signature</span>", ["signature"]],
     ["Plusieurs choses : mes, vos","<span class='savoir-ex'><b>mes</b> papiers · <b>vos</b> cases</span>", ["case"]],
     ["Devant une voyelle, on dit mon","<span class='savoir-ex'><b>mon</b> adresse</span>, jamais « ma adresse »."],
   ]},
   items:[
    {q:"Madame Bourgeois demande : « ___ nom de famille, s'il vous plaît. »", accept:["Votre","votre"], ph:"votre / vos"},
    {q:"Yara répond : « ___ nom de famille, c'est Haddad. »", accept:["Mon","mon"], ph:"mon / ma / mes"},
    {q:"« ___ date de naissance ? » — « Le 7 mars 1994. »", accept:["Votre","votre"], ph:"…"},
    {q:"« Voici ___ papiers, madame. »", accept:["mes"], ph:"…"},
    {q:"« ___ signature, en bas de la page. »", accept:["Votre","votre"], ph:"…"},
    {q:"« ___ adresse, c'est 3420, rue Papineau. »", accept:["Mon","mon"], ph:"…"},
   ]},

  {sec:'t2', id:'t2b', type:'vf', num:'Exercice 5', tit:"Vrai ou Faux — Comment ça s'écrit ?", color:'#B45309',
   sub:"Réécoute Yara qui épelle son nom, puis réponds.", tiles:['VRAI','FAUX'],
   savoir:{h:"› Épeler pour être bien écrit", speak:true, rows:[
     ["On demande","<span class='savoir-ex'>Comment ça s'écrit ? · Vous pouvez épeler ?</span>", ["nom de famille"]],
     ["On dit la lettre deux fois s'il le faut","<span class='savoir-ex'>deux D · deux L · deux S</span>"],
     ["On aide avec un mot connu","<span class='savoir-ex'>B comme bonjour · D comme dimanche · M comme merci</span>"],
     ["On ralentit","<span class='savoir-ex'>Doucement, s'il vous plaît.</span>", ["case"]],
     ["On vérifie à la fin","<span class='savoir-ex'>C'est bien écrit ? · Vous pouvez me le montrer ?</span>", ["formulaire"]],
   ]},
   rows:[
    {id:'v1', txt:"Madame Bourgeois demande comment s'écrit le nom.", ok:'VRAI'},
    {id:'v2', txt:"Il y a deux D dans Haddad.", ok:'VRAI'},
    {id:'v3', txt:"Madame Bourgeois hésite entre B et D.", ok:'VRAI'},
    {id:'v4', txt:"Yara épelle aussi le nom de sa rue.", ok:'VRAI'},
    {id:'v5', txt:"Yara ne vérifie pas ce qui est écrit.", ok:'FAUX'},
   ]},

 // ── JE ME LANCE ─────────────────────────────────────────────
  {sec:'appli', id:'aQui', type:'vf', num:'Exercice 1', tit:'Qui parle ?', color:'#7E3F98',
   sub:"Écoute le dialogue « C'est moi qui explique », puis réponds.", tiles:['YARA','HAMID'],
   rows:[
    {id:'w1', txt:"« Je ne comprends pas cette case. »", ok:'HAMID'},
    {id:'w2', txt:"« C'est le nombre d'années d'école. »", ok:'YARA'},
    {id:'w3', txt:"« Neuf ans. »", ok:'HAMID'},
    {id:'w4', txt:"« Tu écris ton nom à la main, au bas de la page. »", ok:'YARA'},
    {id:'w5', txt:"« Le cours commence quand ? »", ok:'HAMID'},
   ]},

  {sec:'appli', id:'aMoi', type:'write', num:'Exercice 2', tit:'Et toi, ton inscription ?', color:'#7E3F98', cols:2,
   sub:"Écris ta réponse en pensant à ta vraie inscription.",
   items:[
    {q:"Quel est ton nom de famille ?", ph:"Mon nom de famille, c'est…"},
    {q:"Quelle est ta date de naissance ?", ph:"Ma date de naissance, c'est le…"},
    {q:"Ton cours commence à quelle heure ?", ph:"Mon cours commence à…"},
    {q:"Où est le secrétariat de ton centre ?", ph:"Le secrétariat est…"},
   ]},
];
