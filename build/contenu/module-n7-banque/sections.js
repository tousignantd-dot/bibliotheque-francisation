const SECTIONS = [
  {id:'prep', no:'<img class="icon-svg tno-play" src="/assets/interactive/module-n7-banque/icons/play.svg" alt="">', title:'Je découvre', color:'#0D7A6F',
   lead:"Lire les quatre chiffres qui comptent sur un relevé, entendre la différence entre un taux, un montant et une durée, et dire ce qu'on n'a pas compris au lieu de faire oui de la tête.",
   intro:"Marlène Saint-Preux, quarante et un ans, arrivée d'Haïti il y a huit ans, est technicienne au contrôle de la qualité à la Fromagerie des Bois-Francs, à Victoriaville. Elle n'a jamais sauté un paiement de sa vie. Elle doit pourtant neuf mille quatre cent douze dollars sur une carte de crédit, et le solde n'a baissé que de quatre cents dollars en un an. À la pause de dix heures, sa collègue Huguette lui fait un calcul sur un coin de table, et Marlène comprend d'un coup ce que le mot « minimum » veut dire.",
   dialogue:'prep', next:{id:'t1', tit:'Défi 1 · Emprunter moins cher', sub:"Écouter un conseiller présenter trois façons d'emprunter, et comparer ce qu'elles coûtent vraiment."}},

  {id:'t1', no:'1', title:'Défi 1 · Emprunter moins cher', color:'#1D6B8F',
   lead:"S'informer sur des produits financiers liés au crédit : comprendre un taux, comparer trois façons d'emprunter, poser une question au conditionnel et savoir ce que dit un dossier de crédit.",
   intro:"Défi 1 — Une dette ne se règle pas seulement en payant plus : elle se règle souvent en la remplaçant par une dette moins chère. Encore faut-il entendre la différence entre neuf et quarante-cinq et dix-neuf et quatre-vingt-dix, et savoir que le taux le plus bas n'est pas toujours le bon choix. Damien Rouillard n'essaie pas de vendre quelque chose à Marlène : il lui pose une question sur elle-même avant de lui conseiller quoi que ce soit.",
   dialogue:'t1', next:{id:'t2', tit:"Défi 2 · Faire travailler l'argent", sub:"Lire une documentation comparative sur l'épargne, et savoir jusqu'où l'argent déposé est protégé."}},

  {id:'t2', no:'2', title:"Défi 2 · Faire travailler l'argent", color:'#B45309',
   lead:"S'informer par écrit sur des produits financiers liés à l'épargne : lire un document qui compare, reconnaître une phrase passive, et distinguer trois régimes qui ne servent pas au même projet.",
   intro:"Défi 2 — Six mille deux cents dollars dorment dans un compte chèque depuis deux ans. Ce n'est pas beaucoup, et c'est justement pour ça que le choix compte : à ce niveau-là, une mauvaise décision fiscale coûte plus cher qu'un mauvais rendement. Nathalie Pomerleau commence par une question qui n'a rien de financier — quand est-ce que vous en avez besoin ? — et tout le reste en découle.",
   dialogue:'t2', next:{id:'t3', tit:"Défi 3 · Une opération que je n'ai pas faite", sub:"Contester de vive voix puis par écrit, et savoir ce que la loi rembourse."}},

  {id:'t3', no:'3', title:"Défi 3 · Une opération que je n'ai pas faite", color:'#3B49A0',
   lead:"Signaler une opération non autorisée, mettre en relief ce qui compte, employer le subjonctif après un verbe de volonté, et écrire une lettre de réclamation qui laisse une trace.",
   intro:"Défi 3 — Sept cent quatre-vingts dollars apparaissent sur le relevé, le quatorze, chez un commerçant dont Marlène n'a jamais entendu le nom. Sa carte n'a jamais quitté son portefeuille. C'est le seul moment du module où c'est elle qui parle le plus : elle décrit, elle demande, elle vérifie, et elle finit par écrire — parce qu'un appel ne laisse aucune trace et qu'une lettre, oui.",
   dialogue:'t3', next:{id:'appli', tit:'Je me lance', sub:"Poser vos questions à un conseiller, comparer deux produits à voix haute, puis écrire votre lettre."}},

  {id:'appli', no:'<img class="icon-svg tno-play" src="/assets/interactive/module-n7-banque/icons/play.svg" alt="">', title:'Je me lance', color:'#7E3F98', custom:true,
   lead:"S'informer de vive voix sur un produit financier, exposer les avantages et les inconvénients de deux produits pour décider, puis rédiger une lettre de réclamation.",
   intro:"Je me lance — C'est à vous : vous vous informez auprès d'un conseiller sans rien signer, vous pesez deux produits à voix haute pour arriver à une décision, puis vous écrivez la lettre qui conteste l'opération."},

  {id:'retiens', no:'✓', title:'Je retiens des mots', color:'#A5335F', custom:true,
   lead:"Rassembler les mots du relevé, de l'emprunt, de l'épargne et de la contestation.",
   intro:"Je retiens des mots — Notez vos mots utiles, révisez avec les cartes mémoire, puis évaluez ce que vous êtes maintenant capable de faire."},
];
