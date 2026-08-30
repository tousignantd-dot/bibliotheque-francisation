const EXOS = [
 // ── JE DÉCOUVRE ─────────────────────────────────────────────
  {sec:'prep', id:'prVocab', type:'match', num:'Vocabulaire · 1', tit:'Le mot et sa définition', color:'#0D7A6F',
   sub:'Choisis un mot, puis sa définition. Six mots à la fois.', noQLbl:true, bankLbl:'Définitions', zonePh:'glisse la définition ici',
   rows: FC_CARDS.map((c,i)=>({id:'pv'+i, q:c.word, aid:'pv'+i, a:c.def}))},

  {sec:'prep', id:'pr1', type:'vf', num:'Exercice 1', tit:"Vrai ou Faux — Bonjour, madame Roy", color:'#0D7A6F',
   sub:'Écoute de nouveau le dialogue, puis réponds.', tiles:['VRAI','FAUX'],
   savoir:{h:"› Les mots de l'immeuble — à écouter et à répéter", speak:true, rows:[
     ["La personne d'à côté","Elle habite le même immeuble. On la croise souvent.", ["voisin"]],
     ["La grande maison","Plusieurs logements, les uns au-dessus des autres.", ["immeuble"]],
     ["Le petit mot du jour","On le dit en arrivant et en partant.", ["salutation"]],
   ]},
   rows:[
    {id:'p1a', txt:"Nadia dit bonjour à madame Roy.", ok:'VRAI'},
    {id:'p1b', txt:"Madame Roy demande : « Ça va ? »", ok:'VRAI'},
    {id:'p1c', txt:"Nadia va travailler ce matin.", ok:'FAUX'},
    {id:'p1d', txt:"Le cours de Nadia commence à huit heures et demie.", ok:'VRAI'},
    {id:'p1e', txt:"Les deux voisines se disent « à demain ».", ok:'VRAI'},
   ]},

  {sec:'prep', id:'prSons', masque:true, type:'vf', num:'Exercice 2', tit:"Question ou réponse ?", color:'#0D7A6F', accent:'#0D7A6F', cards:true, listen:true,
   sub:"Écoute chaque phrase. Est-ce que la voix monte à la fin (une question) ou descend (une réponse) ?", tiles:['QUESTION','RÉPONSE'],
   savoir:{h:"› La voix monte, ou la voix descend", rows:[
     ["La voix monte à la fin","C'est une question. <span class='savoir-ex'>Ça va ↗ ? · Tu travailles ↗ ?</span>"],
     ["La voix descend à la fin","C'est une réponse. <span class='savoir-ex'>Ça va ↘. · Je travaille ↘.</span>"],
     ["Les mêmes mots, deux sens","« Ça va » est une question ou une réponse. C'est la voix qui décide, pas les mots."],
   ]},
   rows:[
    {id:'in1', txt:"Ça va ?", ok:'QUESTION'},
    {id:'in2', txt:"Ça va bien, merci.", ok:'RÉPONSE'},
    {id:'in3', txt:"Tu travailles ce soir ?", ok:'QUESTION'},
    {id:'in4', txt:"Je travaille ce soir.", ok:'RÉPONSE'},
    {id:'in5', txt:"Vous allez bien ?", ok:'QUESTION'},
    {id:'in6', txt:"Je vais bien.", ok:'RÉPONSE'},
   ]},

  {sec:'prep', id:'prImg', type:'imgmatch', num:'Exercice 3', tit:"Le moment et le lieu", color:'#0D7A6F',
   sub:"Glisse chaque photo sur la phrase qui la décrit.",
   images:[
    {id:'ib1', src:'/assets/interactive/module-n2-bonjour/images/entree-immeuble.jpg'},
    {id:'ib2', src:'/assets/interactive/module-n2-bonjour/images/matin-dejeuner.jpg'},
    {id:'ib3', src:'/assets/interactive/module-n2-bonjour/images/apres-midi-centre.jpg'},
    {id:'ib4', src:'/assets/interactive/module-n2-bonjour/images/soir-fenetre.jpg'},
    {id:'ib5', src:'/assets/interactive/module-n2-bonjour/images/porte-tenue.jpg'},
    {id:'ib6', src:'/assets/interactive/module-n2-bonjour/images/carte-table.jpg'},
   ],
   rows:[
    {id:'ib1', txt:"On se croise ici, en arrivant et en partant.", ok:'ib1'},
    {id:'ib2', txt:"Le premier repas de la journée.", ok:'ib2'},
    {id:'ib3', txt:"L'après-midi, à l'école des adultes.", ok:'ib3'},
    {id:'ib4', txt:"Le soir, il fait noir dehors.", ok:'ib4'},
    {id:'ib5', txt:"Quelqu'un tient la porte pour aider.", ok:'ib5'},
    {id:'ib6', txt:"Une carte écrite pour une fête.", ok:'ib6'},
   ]},

  {sec:'prep', id:'prMoment', type:'match', num:'Exercice 4', tit:'Quel mot, à quel moment ?', color:'#0D7A6F',
   sub:"Associe chaque situation à ce qu'on dit.", bankLbl:'Ce qu\'on dit', zonePh:'glisse ici',
   rows:[
    {id:'m1', q:"Tu arrives au centre à huit heures du matin.", aid:'m1', a:"Bonjour !"},
    {id:'m2', q:"Tu arrives chez ta voisine à sept heures du soir.", aid:'m2', a:"Bonsoir !"},
    {id:'m3', q:"Tu pars le matin, et la personne reste.", aid:'m3', a:"Bonne journée !"},
    {id:'m4', q:"Tu pars après le souper.", aid:'m4', a:"Bonne soirée !"},
    {id:'m5', q:"Tu vas revoir la personne demain matin.", aid:'m5', a:"À demain !"},
    {id:'m6', q:"Tu parles à un ami de ton âge, dans la rue.", aid:'m6', a:"Salut !"},
   ]},

 // ── DÉFI 1 · ÇA VA ? ET TOI ? ───────────────────────────────
  {sec:'t1', id:'t1vf', type:'vf', num:'Exercice 1', tit:"Vrai ou Faux — Salut, Samir !", color:'#1D6B8F',
   sub:'Écoute de nouveau le dialogue, puis réponds.', tiles:['VRAI','FAUX'],
   rows:[
    {id:'s1', txt:"Nadia et Samir se disent « salut ».", ok:'VRAI'},
    {id:'s2', txt:"Samir prend le métro le matin.", ok:'VRAI'},
    {id:'s3', txt:"Nadia prend l'autobus.", ok:'FAUX'},
    {id:'s4', txt:"Nadia travaille le soir.", ok:'VRAI'},
    {id:'s5', txt:"Samir travaille le samedi.", ok:'VRAI'},
   ]},

  {sec:'t1', id:'t1tuvous', type:'write', num:'Exercice 2', tit:'Tu ou vous ?', color:'#1D6B8F', cols:2,
   sub:"Complète chaque phrase avec « tu » ou « vous ».",
   savoir:{h:"› Deux façons de parler à une personne", speak:true, rows:[
     ["« tu » — les proches","Un ami, un camarade de classe, un enfant, la famille.", ["voisin"]],
     ["« vous » — les autres","Une personne plus âgée, un commis, un professeur, quelqu'un qu'on ne connaît pas."],
     ["Le verbe change aussi","<span class='savoir-ex'><b>tu</b> vas · <b>vous</b> allez — <b>tu</b> travailles · <b>vous</b> travaillez</span>", ["travailler"]],
     ["Dans le doute, « vous »","On ne fâche jamais personne avec « vous ». On passe à « tu » quand l'autre le propose."],
     ["Chacun son mot","Madame Roy dit « tu » à Nadia. Nadia dit « vous » à madame Roy. C'est normal : elle est plus âgée."],
   ]},
   items:[
    {q:"Nadia à madame Roy : « Et ___ , ça va ? »", accept:["vous"], ph:"tu / vous"},
    {q:"Nadia à Samir : « Et ___ , ça va ? »", accept:["toi","tu"], ph:"…"},
    {q:"Madame Roy à Nadia : « ___ vas au centre ? »", accept:["tu","Tu"], ph:"…"},
    {q:"Nadia à madame Roy : « ___ allez bien ? »", accept:["vous","Vous"], ph:"…"},
    {q:"À une personne que tu ne connais pas : « ___ travaillez ici ? »", accept:["vous","Vous"], ph:"…"},
   ]},

  {sec:'t1', id:'t1verbes', type:'write', num:'Exercice 3', tit:'Ma journée, au présent', color:'#1D6B8F', cols:2,
   sub:"Complète avec le verbe entre parenthèses.",
   savoir:{h:"› Les verbes de la journée, au présent", speak:true, rows:[
     ["Le matin","<span class='savoir-ex'>je <b>déjeune</b> · je <b>pars</b> · je <b>marche</b></span>", ["déjeuner"]],
     ["Le jour","<span class='savoir-ex'>j'<b>étudie</b> · je <b>travaille</b> · je <b>dîne</b></span>", ["travailler"]],
     ["Le soir","<span class='savoir-ex'>je <b>soupe</b> · je <b>regarde</b> la télé · je <b>dors</b></span>", ["soir"]],
     ["Les verbes en -er : je -e, tu -es","<span class='savoir-ex'>je déjeun<b>e</b> · tu déjeun<b>es</b> · vous déjeun<b>ez</b></span>"],
     ["Deux verbes à part","<b>aller</b> : je vais, tu vas, vous allez. <b>prendre</b> : je prends, tu prends, vous prenez."],
     ["Devant une voyelle, « je » devient « j' »","<span class='savoir-ex'>j'étudie · j'arrive · j'habite</span>"],
   ]},
   items:[
    {q:"Le matin, je ___ à sept heures. (déjeuner)", accept:["déjeune","dejeune"], ph:"un verbe"},
    {q:"Je ___ jusqu'au centre. (marcher)", accept:["marche"], ph:"…"},
    {q:"L'après-midi, j' ___ à la maison. (étudier)", accept:["étudie","etudie"], ph:"…"},
    {q:"Le soir, je ___ à la pharmacie. (travailler)", accept:["travaille"], ph:"…"},
    {q:"Samir ___ le métro le matin. (prendre)", accept:["prend"], ph:"…"},
    {q:"Et toi, tu ___ au centre à pied ? (aller)", accept:["vas"], ph:"…"},
   ]},

  {sec:'t1', id:'t1repond', type:'match', num:'Exercice 4', tit:'La question et sa réponse', color:'#1D6B8F',
   sub:"Associe chaque question à une réponse possible.", bankLbl:'Une réponse', zonePh:'glisse ici',
   rows:[
    {id:'q1', q:"Ça va ?", aid:'q1', a:"Ça va bien, merci. Et toi ?"},
    {id:'q2', q:"Tu arrives comment, le matin ?", aid:'q2', a:"Je marche. J'habite près du centre."},
    {id:'q3', q:"Tu travailles ?", aid:'q3', a:"Oui, le soir, dans une pharmacie."},
    {id:'q4', q:"Tu fais quoi, l'après-midi ?", aid:'q4', a:"J'étudie à la maison."},
    {id:'q5', q:"Tu soupes à quelle heure ?", aid:'q5', a:"À neuf heures, avec ma sœur."},
    {id:'q6', q:"Tu es fatiguée ?", aid:'q6', a:"Un peu. Ma journée est longue."},
   ]},

  {sec:'t1', id:'t1b', type:'vf', num:'Exercice 5', tit:'Vrai ou Faux — Ma journée', color:'#1D6B8F',
   sub:'Écoute de nouveau le dialogue, puis réponds.', tiles:['VRAI','FAUX'],
   rows:[
    {id:'j1', txt:"Nadia déjeune à sept heures.", ok:'VRAI'},
    {id:'j2', txt:"Elle prend l'autobus jusqu'au centre.", ok:'FAUX'},
    {id:'j3', txt:"Elle étudie l'après-midi.", ok:'VRAI'},
    {id:'j4', txt:"Elle soupe à six heures.", ok:'FAUX'},
    {id:'j5', txt:"Elle soupe avec sa sœur.", ok:'VRAI'},
   ]},

 // ── DÉFI 2 · MERCI ET BONNE FÊTE ────────────────────────────
  {sec:'t2', id:'t2vf', type:'vf', num:'Exercice 1', tit:"Vrai ou Faux — Pouvez-vous m'aider ?", color:'#B45309',
   sub:'Écoute de nouveau le dialogue, puis réponds.', tiles:['VRAI','FAUX'],
   rows:[
    {id:'a1', txt:"Madame Roy demande de l'aide à Nadia.", ok:'VRAI'},
    {id:'a2', txt:"Ses sacs sont lourds.", ok:'VRAI'},
    {id:'a3', txt:"Nadia refuse d'aider.", ok:'FAUX'},
    {id:'a4', txt:"Madame Roy habite au deuxième étage.", ok:'VRAI'},
    {id:'a5', txt:"Nadia répond : « Ce n'est rien. »", ok:'VRAI'},
   ]},

  {sec:'t2', id:'t2aide', type:'write', num:'Exercice 2', tit:"Demander de l'aide", color:'#B45309', cols:2,
   sub:"Que dis-tu dans chaque situation ?",
   savoir:{h:"› Trois phrases pour demander de l'aide", speak:true, rows:[
     ["On commence toujours par « excusez-moi »","<span class='savoir-ex'>Excusez-moi… · Excuse-moi… (à un ami)</span>"],
     ["Avec « pouvoir »","<span class='savoir-ex'><b>Pouvez-vous</b> m'aider ? · <b>Peux-tu</b> m'aider ?</span>", ["de l'aide"]],
     ["Avec « avoir besoin de »","<span class='savoir-ex'>J'ai <b>besoin d'</b>aide. · J'ai <b>besoin d'</b>un sac.</span>"],
     ["Dire ce qu'on veut, tout de suite après","<span class='savoir-ex'>Pouvez-vous tenir la <b>porte</b> ? · Pouvez-vous répéter ?</span>", ["porte"]],
     ["Quand on aide, on répond","<span class='savoir-ex'>Oui, bien sûr. · Ce n'est rien. · Ça me fait plaisir.</span>"],
   ]},
   items:[
    {q:"Tes sacs sont lourds. Tu demandes de l'aide à une voisine.", accept:["pouvez-vous m'aider ?","pouvez-vous m'aider","excusez-moi, pouvez-vous m'aider ?"], ph:"…"},
    {q:"Tu demandes la même chose à un ami.", accept:["peux-tu m'aider ?","peux-tu m'aider","excuse-moi, peux-tu m'aider ?"], ph:"…"},
    {q:"Tu as les mains pleines devant la porte.", accept:["pouvez-vous tenir la porte ?","pouvez-vous tenir la porte","pouvez-vous ouvrir la porte ?"], ph:"…"},
    {q:"Tu n'as pas compris. Tu veux qu'on répète.", accept:["pouvez-vous répéter ?","pouvez-vous répéter","excusez-moi, pouvez-vous répéter ?"], ph:"…"},
    {q:"Quelqu'un te dit merci. Que réponds-tu ?", accept:["ce n'est rien","ce n'est rien.","de rien","ça me fait plaisir"], ph:"…"},
   ]},

  {sec:'t2', id:'t2merci', type:'write', num:'Exercice 3', tit:'Merci, et bonne fête', color:'#B45309', cols:2,
   sub:"Complète avec le petit mot qui manque.",
   savoir:{h:"› Remercier et souhaiter", speak:true, rows:[
     ["Merci, tout court","<span class='savoir-ex'>Merci. · Merci beaucoup. · Merci mille fois.</span>"],
     ["Merci <b>pour</b> + une chose","<span class='savoir-ex'>Merci <b>pour</b> la soupe. · Merci <b>pour</b> votre aide.</span>", ["de l'aide"]],
     ["Bonne + le nom de la chose","<span class='savoir-ex'><b>Bonne</b> journée · <b>Bonne</b> soirée · <b>Bonne</b> fête · <b>Bonne</b> santé</span>", ["fête"]],
     ["Bon + un nom masculin","<span class='savoir-ex'><b>Bon</b> anniversaire · <b>Bon</b> voyage · <b>Bon</b> cours</span>"],
     ["Sur une carte, on écrit court","<span class='savoir-ex'>Bonne fête ! Bonne santé ! Merci pour tout.</span>", ["carte de vœux"]],
   ]},
   items:[
    {q:"___ pour la soupe, madame Roy.", accept:["merci","Merci"], ph:"…"},
    {q:"C'est sa fête samedi. On lui dit : « ___ fête ! »", accept:["bonne","Bonne"], ph:"bon / bonne"},
    {q:"Il part en voyage. On lui dit : « ___ voyage ! »", accept:["bon","Bon"], ph:"…"},
    {q:"Tu pars le matin. Tu dis : « ___ journée ! »", accept:["bonne","Bonne"], ph:"…"},
    {q:"Elle te dit merci. Tu réponds : « Ce n'est ___ . »", accept:["rien"], ph:"…"},
   ]},

  {sec:'t2', id:'t2carte', type:'match', num:'Exercice 4', tit:'Quelle carte pour quelle occasion ?', color:'#B45309',
   sub:"Associe chaque carte au moment où on la donne.", bankLbl:'Quand on la donne', zonePh:'glisse ici',
   rows:[
    {id:'c1', q:"« Bonne fête ! »", aid:'c1', a:"le jour de l'anniversaire d'une personne"},
    {id:'c2', q:"« Merci pour tout »", aid:'c2', a:"quand quelqu'un nous a beaucoup aidés"},
    {id:'c3', q:"« Bonne santé ! »", aid:'c3', a:"à une personne malade, ou au jour de l'An"},
    {id:'c4', q:"« Félicitations ! »", aid:'c4', a:"quand une personne réussit un examen"},
    {id:'c5', q:"« Bienvenue ! »", aid:'c5', a:"à une personne qui arrive dans l'immeuble"},
    {id:'c6', q:"« Bon voyage ! »", aid:'c6', a:"à une personne qui part loin en avion"},
   ]},

  {sec:'t2', id:'t2b', type:'vf', num:'Exercice 5', tit:'Vrai ou Faux — Merci pour la soupe', color:'#B45309',
   sub:'Écoute de nouveau le dialogue, puis réponds.', tiles:['VRAI','FAUX'],
   rows:[
    {id:'f1', txt:"Madame Roy donne de la soupe à Nadia.", ok:'VRAI'},
    {id:'f2', txt:"Nadia dit : « Merci pour la soupe. »", ok:'VRAI'},
    {id:'f3', txt:"La fête de madame Roy est dimanche.", ok:'FAUX'},
    {id:'f4', txt:"Madame Roy a soixante-dix ans samedi.", ok:'VRAI'},
   ]},

 // ── JE ME LANCE ─────────────────────────────────────────────
  {sec:'appli', id:'aQui', type:'vf', num:'Exercice 1', tit:'Qui parle ?', color:'#7E3F98',
   sub:"Écoute le dialogue « Bonne fête, madame Roy ! », puis réponds.", tiles:['NADIA','MADAME ROY'],
   rows:[
    {id:'z1', txt:"« C'est pour vous. »", ok:'NADIA'},
    {id:'z2', txt:"« Une carte ! Merci, Nadia. »", ok:'MADAME ROY'},
    {id:'z3', txt:"« Bonne fête ! Bonne santé ! »", ok:'NADIA'},
    {id:'z4', txt:"« Entre, je fais du thé. »", ok:'MADAME ROY'},
    {id:'z5', txt:"« Merci, mais je travaille à six heures. »", ok:'NADIA'},
   ]},

  {sec:'appli', id:'aMoi', type:'write', num:'Exercice 2', tit:'Et toi, ta journée ?', color:'#7E3F98', cols:2,
   sub:"Écris ta réponse à chaque question.",
   items:[
    {q:"Qu'est-ce que tu fais le matin ?", ph:"Le matin, je…"},
    {q:"Comment est-ce que tu viens au centre ?", ph:"Je…"},
    {q:"Qu'est-ce que tu fais l'après-midi ?", ph:"L'après-midi, je…"},
    {q:"Qu'est-ce que tu dis à ton voisin quand tu pars le matin ?", ph:"Je dis…"},
   ]},
];
