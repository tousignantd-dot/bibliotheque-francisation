const PLUS = {

  // ════════════════════════════════════════════════════════════════════════
  prPhon: {
    eye:'Mini-leçon', tit:"La liaison : quand deux mots n’en font qu’un",
    blocs:[
      {t:'texte', h:"Ce que l’oreille entend, et que l’œil ne voit pas",
       p:"Beaucoup de mots français finissent par une lettre qu’on ne prononce pas : le <b>s</b> de « les », le <b>n</b> de « un », le <b>z</b> de « chez », le <b>x</b> de « deux ». Cette lettre dort. Mais si le mot suivant commence par une voyelle, elle se réveille et se colle à lui. C’est la liaison. Rien ne change à l’écrit ; tout change à l’oreille.",
       note:"À l’accueil, vous passez la journée au téléphone. La personne au bout du fil ne voit ni votre bouche ni vos mains : elle n’a que le rythme de vos mots. Une phrase sans liaisons arrive hachée, et il faut la faire répéter."},

      {t:'ana', h:"Les liaisons qui se font toujours",
       p:"Elles se font entre deux mots qui forment un seul groupe : un déterminant et son nom, un pronom et son verbe.",
       mots:[["Après un déterminant","les_heures · un_appel · ces_employés · deux_appels"],["Après un pronom sujet","vous_avez · nous_attendons · ils_ont · on_arrive",true],["Après un petit mot","très_occupée · en_avant · chez_elle · dans_une_heure"]],
       say:"Vous avez un appel en attente depuis dix minutes.",
       note:"Retenez le principe plutôt que la liste : plus les deux mots sont soudés par le sens, plus la liaison est obligatoire."},

      {t:'ana', h:"Les liaisons qu’on ne fait jamais",
       p:"Elles sont moins nombreuses, mais très fréquentes dans les phrases du bureau.",
       mots:[["Après « et »","et / elle · et / un formulaire · et / après"],["Après un nom au singulier","le bureau / ouvert · un appel / urgent",true],["Devant un h aspiré","en / haut · les / haricots · le / hall"]],
       say:"Le bureau ouvert et un formulaire, en haut de l’escalier.",
       note:"« Et » ne fait jamais de liaison, dans aucun cas : c’est la seule règle de cette leçon qui n’a aucune exception."},

      {t:'ana', h:"La lettre change de son",
       p:"Quand elle se réveille, la lettre ne se prononce pas toujours comme elle s’écrit.",
       mots:[["s et x se disent « z »","les_heures · deux_appels · vous_avez"],["d se dit « t »","un grand_immeuble · quand_il arrive",true],["f se dit « v »","neuf_heures · neuf_ans"]],
       say:"Il est neuf heures et vous avez deux appels.",
       note:"C’est ce qui rend « les heures » difficile à reconnaître pour une oreille neuve : on cherche un mot qui commencerait par « z »."},

      {t:'labo', h:"Écoutez la même phrase, avec et sans",
       p:"Choisissez un groupe de mots et écoutez-le dans une phrase du module.",
       axes:[{id:'g', lbl:'Quel groupe de mots ?', opts:[
         ['a','vous avez'],
         ['b','un appel'],
         ['c','les heures'],
         ['d','et elle'],
         ['e','tout ensemble']]}],
       out:{
         a:{w:['vous avez'], say:"Vous avez trois messages dans votre boîte vocale.", n:"le s de « vous » se dit « z »"},
         b:{w:['un appel'], say:"Un appel urgent est entré pendant la réunion.", n:"le n de « un » se colle à « appel »"},
         c:{w:['les heures'], say:"Les heures sont inscrites au registre chaque semaine.", n:"on entend « lé-zeur »"},
         d:{w:['et elle'], say:"Elle a signé le formulaire, et elle l’a envoyé à la paie.", n:"aucune liaison après « et », jamais"},
         e:{w:['tout ensemble'], say:"Vous avez un appel, et elle vous rappellera dans les heures qui viennent.", n:"trois liaisons faites, une refusée"},
       },
       note:"Écoutez chaque phrase deux fois : la première pour comprendre, la seconde en ne guettant que les endroits où deux mots se collent."},

      {t:'ex', h:"À écouter et à répéter",
       p:"Six phrases prises dans les appels de ce module.",
       rows:[
         ["Vous êtes bien à la Coopérative d’aide à domicile.","« vous_êtes » : la liaison ouvre la phrase"],
         ["Un instant, je vous prie, je vérifie au registre.","« un_instant » se dit d’un seul souffle"],
         ["Nous avons deux employés à l’accueil ce matin.","trois liaisons de suite"],
         ["Il est neuf heures et il n’est pas encore arrivé.","« neuf_heures » se dit « neu-veur »"],
         ["Elle a laissé son numéro et elle attend un rappel.","liaison après « elle », rien après « et »"],
         ["En haut de la page, en avant du formulaire.","« en / haut » non, « en_avant » oui"],
       ]},

      {t:'piege', h:"Trois pièges de la liaison",
       rows:[
         ["faire la liaison après « et »","« et_il est parti »",
          "Aucune liaison après « et », dans aucun cas, quelle que soit la lettre qui suit. C’est le seul mot du français qui refuse absolument la liaison."],
         ["prononcer la lettre telle qu’elle s’écrit","« les heures » dit « lé-seur »",
          "Le <b>s</b> et le <b>x</b> de liaison se disent « z ». On entend « lé-<b>z</b>eur », « deu-<b>z</b>appels », « vou-<b>z</b>avez »."],
         ["lier un nom singulier à ce qui suit","« un appel_urgent » dit avec un l entendu",
          "Après un nom au singulier, la liaison ne se fait pas : « un appel / urgent ». Au pluriel, elle se fait : « des appels_urgents »."],
       ]},

      {t:'check', h:"Est-ce que c’est clair maintenant ?",
       p:"Quatre questions rapides.",
       qs:[
         {q:"Dans « les heures », le s se prononce…", opts:["« s »","« z »"], ok:1,
          fb:"« z ». On entend « lé-zeur », ce qui surprend la première fois."},
         {q:"Après « et », on fait la liaison…", opts:["parfois","jamais"], ok:1,
          fb:"Jamais. C’est la seule règle sans exception de cette leçon."},
         {q:"« en haut » se dit…", opts:["avec une liaison","sans liaison"], ok:1,
          fb:"Sans : le h de « haut » est aspiré, il bloque la liaison."},
         {q:"« neuf heures » se prononce…", opts:["« neu-feur »","« neu-veur »"], ok:1,
          fb:"Le f devient « v » devant « heures » et « ans ». Ailleurs, il reste « f »."},
       ]},
    ]
  },

  // ════════════════════════════════════════════════════════════════════════
  prReg: {
    eye:'Mini-leçon', tit:"Deux façons de parler dans le même immeuble",
    blocs:[
      {t:'texte', h:"Le tutoiement s’arrête à la porte du bureau",
       p:"Dans le corridor, à la cuisine, devant le photocopieur, on se tutoie et on parle vite : c’est ce qui rend une équipe agréable. Dès qu’on décroche le téléphone ou qu’on ouvre un courriel, tout change : on vouvoie, on nomme l’établissement, on emploie des formules. Ce n’est pas de la froideur, et ce n’est pas une question de respect envers la personne : c’est que dans ces moments-là, ce n’est plus vous qui parlez, c’est l’organisation.",
       note:"C’est exactement ce que Ghislain dit à Dorine : « Ce n’est pas Dorine qui répond au poste vingt-deux, c’est la coopérative. » Même madame Thériault, qu’elle connaît depuis un an, sera vouvoyée au téléphone."},

      {t:'ana', h:"Ouvrir : l’établissement d’abord, soi ensuite",
       p:"L’ordre n’est pas décoratif : la personne veut d’abord savoir si elle a composé le bon numéro.",
       mots:[["Au téléphone","Coopérative d’aide à domicile de Rosemont, bonjour."],["Dans une boîte vocale","Vous êtes bien à la Coopérative d’aide à domicile de Rosemont. Ici Dorine Kabeya, à l’accueil.",true],["Dans un courriel","Bonjour madame Thériault, · Bonjour, · Madame, Monsieur,"]],
       say:"Coopérative d’aide à domicile de Rosemont, bonjour.",
       note:"« Allô ? » et « Oui, allô ? » sont des ouvertures personnelles. Au travail, elles font croire à la personne qu’elle s’est trompée de numéro."},

      {t:'ana', h:"Faire patienter, transférer, s’excuser",
       p:"Quatre phrases suffisent pour toute une journée à l’accueil.",
       mots:[["Attendre","Un instant, je vous prie. · Ne quittez pas, je vérifie."],["Transférer","Je vous transfère au poste onze. · Je vous passe le service technique.",true],["S’excuser","Je suis désolée de l’attente. · Excusez-moi, la ligne est occupée."]],
       say:"Un instant, je vous prie. Ne quittez pas, je vérifie au registre.",
       note:"« Attends », « bouge pas », « deux secondes » sont parfaits dans un corridor et déplacés au téléphone. Ils ne sont pas impolis : ils sont hors contexte."},

      {t:'ana', h:"Fermer sans traîner",
       p:"La fin d’un appel se joue en deux phrases. Une seule chose compte : que la personne sache ce qui va se passer ensuite.",
       mots:[["Ce que vous ferez","Je vous rappelle dans les meilleurs délais. · Je transmets le message aujourd’hui."],["La politesse","Merci de votre appel. · Bonne journée. · Au revoir.",true],["Ce qu’on ne dit pas","Bye · C’est beau · Pas de trouble · Correct, là"]],
       say:"Je transmets le message aujourd’hui. Merci de votre appel, bonne journée.",
       note:"Vouvoyer ne veut pas dire allonger. Les phrases restent courtes, une idée à la fois : un message poli et interminable est un message raté."},

      {t:'labo', h:"La même chose, dite des deux façons",
       p:"Choisissez une situation et écoutez les deux versions.",
       axes:[{id:'s', lbl:'Quelle situation ?', opts:[
         ['a','Demander d’attendre'],
         ['b','Dire qu’on s’en occupe'],
         ['c','Demander de répéter'],
         ['d','Dire au revoir'],
         ['e','Demander un numéro']]}],
       out:{
         a:{w:['un instant'], say:"Dans le corridor : attends deux secondes. Au téléphone : un instant, je vous prie.", n:"la deuxième version prend une seconde de plus"},
         b:{w:['je m’en occupe'], say:"Dans le corridor : c’est beau, je m’en occupe. Au téléphone : je m’en occupe aujourd’hui, madame.", n:"« c’est beau » n’a pas d’équivalent poli : il disparaît"},
         c:{w:['répéter'], say:"Dans le corridor : hein ? Au téléphone : pourriez-vous répéter, s’il vous plaît ?", n:"la faute la plus fréquente des premiers jours"},
         d:{w:['bonne journée'], say:"Dans le corridor : bye, à demain. Au téléphone : merci de votre appel, bonne journée.", n:"« bye » ne se met jamais dans une boîte vocale"},
         e:{w:['votre numéro'], say:"Dans le corridor : c’est quoi ton numéro ? Au téléphone : pourriez-vous me donner votre numéro de téléphone ?", n:"« c’est quoi » devient « pourriez-vous me donner »"},
       },
       note:"Écoutez les deux versions à la suite : ce n’est pas le vocabulaire qui change le plus, c’est le début de la phrase."},

      {t:'ex', h:"À écouter et à répéter",
       p:"Six phrases de la journée d’une personne à l’accueil.",
       rows:[
         ["Coopérative d’aide à domicile de Rosemont, bonjour.","l’ouverture, toujours la même"],
         ["Un instant, je vous prie, je vérifie au registre.","faire patienter"],
         ["Je vous transfère au poste onze, ne quittez pas.","transférer"],
         ["Pourriez-vous me répéter votre numéro, s’il vous plaît ?","faire répéter sans dire « hein »"],
         ["Je transmets votre message dès aujourd’hui.","dire ce qui va se passer"],
         ["Merci de votre appel, bonne journée.","fermer"],
       ]},

      {t:'piege', h:"Trois pièges du registre au travail",
       rows:[
         ["tutoyer parce qu’on connaît la personne","« Salut madame Thériault, comment ça va ? »",
          "Au téléphone, on vouvoie même les gens qu’on croise depuis un an. Le tutoiement reprend dès qu’on se revoit en personne, dans le corridor."],
         ["dire pourquoi on n’est pas disponible","« Je suis en réunion jusqu’à trois heures. »",
          "Dans un message d’accueil, la raison ne regarde personne, et elle vieillit : elle continuera de se répéter demain, quand la réunion sera finie."],
         ["allonger pour être poli","« Je m’excuse infiniment de vous déranger avec cette petite question qui… »",
          "La politesse tient dans le début et la fin de la phrase, pas dans sa longueur. Une phrase courte et vouvoyée est parfaitement polie."],
       ]},

      {t:'check', h:"Est-ce que c’est clair maintenant ?",
       p:"Quatre questions rapides.",
       qs:[
         {q:"Au téléphone, on nomme d’abord…", opts:["soi-même","l’établissement"], ok:1,
          fb:"L’établissement : la personne veut savoir si elle a le bon numéro."},
         {q:"« C’est beau, pas de trouble » se dit…", opts:["au téléphone","entre collègues"], ok:1,
          fb:"Entre collègues. Ce n’est pas impoli : c’est hors contexte au téléphone."},
         {q:"Dans un message d’accueil, on explique pourquoi on est absent…", opts:["oui","non"], ok:1,
          fb:"Non. La raison ne regarde personne et le message la répétera demain encore."},
         {q:"Vouvoyer oblige à faire des phrases…", opts:["plus longues","aussi courtes"], ok:1,
          fb:"Aussi courtes. La politesse est au début et à la fin, pas dans la longueur."},
       ]},
    ]
  },

  // ════════════════════════════════════════════════════════════════════════
  t1acc: {
    eye:'Mini-leçon', tit:"Le message d’accueil : trente secondes, six morceaux",
    blocs:[
      {t:'texte', h:"Un texte qu’on écrit une fois et qui parle mille fois",
       p:"Un message d’accueil n’est pas une conversation : c’est un texte enregistré, qui se répète à l’identique pour chaque personne qui appelle, y compris celles qui appellent quatre fois dans la même journée. C’est pour ça qu’on l’écrit avant de l’enregistrer, qu’on le lit à voix haute, et qu’on le refait si un mot ne va pas.",
       note:"L’intention du programme, ici, est « enregistrer un message téléphonique ». Elle a l’air modeste ; c’est en réalité une production orale préparée, écrite d’avance, et jugée par tous ceux qui appellent."},

      {t:'ana', h:"Morceaux 1 et 2 — qui vous êtes, et que vous n’êtes pas là",
       p:"Les deux premières phrases décident si la personne écoute la suite.",
       mots:[["L’établissement d’abord","Vous êtes bien à la Coopérative d’aide à domicile de Rosemont."],["Vous ensuite","Ici Dorine Kabeya, à l’accueil.",true],["L’absence, sans la raison","Je ne suis pas disponible en ce moment."]],
       say:"Vous êtes bien à la Coopérative d’aide à domicile de Rosemont. Ici Dorine Kabeya, à l’accueil. Je ne suis pas disponible en ce moment.",
       note:"« Je suis en réunion », « je suis en congé jusqu’au 12 » : ces précisions sont fausses dès le lendemain, et le message continue de les dire."},

      {t:'ana', h:"Morceau 3 — trois choses, pas cinq",
       p:"On demande le nom, le numéro et la raison. C’est tout ce qu’une personne pressée peut retenir.",
       mots:[["La formule","Laissez-moi votre nom, votre numéro de téléphone et la raison de votre appel."],["À l’impératif","Laissez-moi… · Indiquez-moi… · Précisez…",true],["Ce qu’on n’ajoute pas","l’heure de l’appel · votre adresse · votre numéro de dossier"]],
       say:"Laissez-moi votre nom, votre numéro de téléphone et la raison de votre appel.",
       note:"Si vous avez vraiment besoin d’une quatrième information, dites-la en dernier et seule : « et, si vous en avez un, votre numéro de dossier »."},

      {t:'ana', h:"Morceaux 4, 5 et 6 — le rappel, la sortie, la politesse",
       p:"La fin du message est celle qu’on retient le mieux, avec le début.",
       mots:[["Le rappel, au futur simple","Je vous rappellerai dans les meilleurs délais."],["La porte de sortie","Pour une urgence, faites le poste onze.",true],["La politesse","Merci et bonne journée."]],
       say:"Je vous rappellerai dans les meilleurs délais. Pour une urgence, faites le poste onze. Merci et bonne journée.",
       note:"La porte de sortie est le morceau qu’on oublie, et le seul qui rende service à quelqu’un qui ne peut pas attendre."},

      {t:'labo', h:"Le même message, quatre situations",
       p:"Choisissez une situation et écoutez le message qui lui convient.",
       axes:[{id:'m', lbl:'Quelle situation ?', opts:[
         ['a','Une journée normale'],
         ['b','Une semaine de vacances'],
         ['c','Un poste partagé à deux'],
         ['d','Une ligne qui ne rappelle pas'],
         ['e','Le message complet']]}],
       out:{
         a:{w:['un message d\'accueil'], say:"Je ne suis pas disponible en ce moment. Je vous rappellerai dans les meilleurs délais.", n:"aucune date : le message reste vrai tous les jours"},
         b:{w:['rappeler'], say:"Je suis absente jusqu’au lundi 26 août. Pour toute question d’ici là, faites le poste dix-neuf.", n:"ici la date se dit : le message sera changé au retour"},
         c:{w:['l\'accueil'], say:"Vous êtes bien à l’accueil. Laissez votre message : Kevin ou moi vous rappellerons.", n:"« nous » plutôt que « je » quand deux personnes se partagent la ligne"},
         d:{w:['la paie'], say:"Cette ligne ne reçoit pas de messages. Pour joindre la paie, écrivez à l’adresse indiquée sur votre relevé.", n:"il faut le dire : sinon les gens parlent dans le vide"},
         e:{w:['une boîte vocale'], say:"Vous êtes bien à la Coopérative d’aide à domicile de Rosemont. Ici Dorine Kabeya, à l’accueil. Je ne suis pas disponible en ce moment. Laissez-moi votre nom, votre numéro de téléphone et la raison de votre appel. Je vous rappellerai dans les meilleurs délais. Pour une urgence, faites le poste onze. Merci et bonne journée.", n:"vingt-huit secondes, six morceaux"},
       },
       note:"Comptez à voix haute pendant l’écoute : un message qui dépasse quarante secondes perd la moitié de ceux qui appellent."},

      {t:'ex', h:"À écouter et à répéter",
       p:"Les six morceaux, un par un.",
       rows:[
         ["Vous êtes bien à la Coopérative d’aide à domicile de Rosemont.","l’établissement"],
         ["Ici Dorine Kabeya, à l’accueil.","soi-même, et sa fonction"],
         ["Je ne suis pas disponible en ce moment.","l’absence, sans la raison"],
         ["Laissez-moi votre nom, votre numéro de téléphone et la raison de votre appel.","les trois choses"],
         ["Je vous rappellerai dans les meilleurs délais.","le rappel, au futur simple"],
         ["Pour une urgence, faites le poste onze. Merci et bonne journée.","la sortie et la politesse"],
       ]},

      {t:'piege', h:"Trois pièges du message d’accueil",
       rows:[
         ["promettre une heure","« Je vous rappellerai avant seize heures. »",
          "Cette promesse se répétera le jour de votre congé, où elle sera fausse. « Dans les meilleurs délais » vieillit bien."],
         ["oublier de dire son nom","« Vous êtes bien au poste vingt-deux. Laissez un message. »",
          "La personne ne sait pas à qui elle parle et n’ose pas laisser de détails. Se nommer coûte deux secondes."],
         ["ne pas changer le message avant de partir","le message de tous les jours pendant une semaine de vacances",
          "Pendant une semaine, tout le monde entend « je vous rappellerai dans les meilleurs délais » et attend pour rien. On enregistre un message d’absence avant de partir, et on remet l’autre au retour."],
       ]},

      {t:'check', h:"Est-ce que c’est clair maintenant ?",
       p:"Quatre questions rapides.",
       qs:[
         {q:"Combien de renseignements demande-t-on ?", opts:["trois","cinq"], ok:0,
          fb:"Trois : le nom, le numéro, la raison. Au-delà, personne ne retient."},
         {q:"On dit pourquoi on n’est pas disponible…", opts:["toujours","jamais"], ok:1,
          fb:"Jamais dans le message de tous les jours. La raison ne regarde personne."},
         {q:"Le morceau le plus souvent oublié est…", opts:["la porte de sortie","la politesse"], ok:0,
          fb:"La porte de sortie — et c’est le seul qui aide quelqu’un de pressé."},
         {q:"Un bon message dure environ…", opts:["trente secondes","deux minutes"], ok:0,
          fb:"Trente secondes. Au-delà, la personne raccroche avant le bip."},
       ]},
    ]
  },

  // ════════════════════════════════════════════════════════════════════════
  t1imp: {
    eye:'Mini-leçon', tit:"L’impératif, et où se met le pronom",
    blocs:[
      {t:'texte', h:"Le temps de tous les écrits de travail",
       p:"Un message d’accueil, une note collée sur un appareil, un courriel qui demande quelque chose : tous sont faits d’impératifs. C’est le temps qui donne une consigne sans dire « vous ». Il n’a que trois personnes — <i>tu</i>, <i>nous</i>, <i>vous</i> — et il n’a jamais de pronom sujet devant lui.",
       note:"Au travail, c’est presque toujours la forme en « vous » qu’on emploie : <i>Laissez</i>, <i>Appuyez</i>, <i>Envoyez</i>. La forme en « tu » sert entre collègues, la forme en « nous » pour inviter le groupe."},

      {t:'ana', h:"Comment on le forme",
       p:"On prend la forme du présent et on enlève le pronom sujet. Un seul détail change.",
       mots:[["Vous","vous laissez → laissez · vous appuyez → appuyez"],["Nous","nous laissons → laissons · nous envoyons → envoyons",true],["Tu — le s tombe aux verbes en -er","tu laisses → laisse · tu rappelles → rappelle · mais tu finis → finis"]],
       say:"Laissez votre nom. Laissons un message. Laisse ton numéro.",
       note:"Le <b>s</b> revient quand le verbe est suivi de <b>y</b> ou <b>en</b> : « vas-y », « parles-en ». C’est pour l’oreille, pas pour la grammaire."},

      {t:'ana', h:"Phrase affirmative : le pronom passe derrière",
       p:"C’est le seul cas du français où le pronom se met après le verbe, avec un trait d’union.",
       mots:[["Un pronom","Laissez-moi un message. · Rappelez-la. · Envoyez-le."],["me devient moi, te devient toi","Dites-moi. · Assoyez-vous. · Assois-toi.",true],["Deux pronoms : direct, puis indirect","Donnez-le-moi. · Envoyez-la-lui."]],
       say:"Laissez-moi un message et rappelez-la avant midi.",
       note:"Les traits d’union ne sont pas décoratifs : ils marquent que le groupe se prononce d’un seul souffle, comme un seul mot."},

      {t:'ana', h:"Phrase négative : tout revient dans l’ordre habituel",
       p:"Dès qu’il y a une négation, le pronom reprend sa place normale, devant le verbe, sans trait d’union.",
       mots:[["Un pronom","Ne me rappelez pas après midi. · Ne la faites pas attendre."],["Deux pronoms","Ne me le donnez pas. · Ne la lui envoyez pas.",true],["Et « moi » redevient « me »","Dites-moi → Ne me dites pas."]],
       say:"Ne me rappelez pas après midi et ne la faites pas attendre.",
       note:"Retenez la règle par l’image : l’affirmative pousse le pronom derrière ; la négative, en l’encadrant, le ramène devant."},

      {t:'labo', h:"La même consigne, affirmative puis négative",
       p:"Choisissez une consigne et écoutez ses deux formes.",
       axes:[{id:'c', lbl:'Quelle consigne ?', opts:[
         ['a','laisser un message'],
         ['b','rappeler quelqu’un'],
         ['c','envoyer le formulaire'],
         ['d','donner son numéro'],
         ['e','deux pronoms à la fois']]}],
       out:{
         a:{w:['un message d\'accueil'], say:"Laissez-moi un message. Ne me laissez pas de message après dix-sept heures.", n:"« moi » derrière, « me » devant"},
         b:{w:['rappeler'], say:"Rappelez-la avant midi. Ne la rappelez pas après midi.", n:"le pronom saute d’un côté à l’autre du verbe"},
         c:{w:['un formulaire'], say:"Envoyez-le à la paie. Ne l’envoyez pas sans la signature.", n:"« le » devient « l’ » devant une voyelle"},
         d:{w:['la paie'], say:"Donnez-moi votre numéro. Ne me donnez pas votre numéro personnel.", n:"la négation ramène « me » devant"},
         e:{w:['une autorisation d\'absence'], say:"Donnez-le-moi aujourd’hui. Ne me le donnez pas demain.", n:"deux pronoms : l’ordre s’inverse aussi"},
       },
       note:"Répétez chaque paire à voix haute jusqu’à ce que le déplacement du pronom devienne un réflexe, pas un calcul."},

      {t:'ex', h:"À écouter et à répéter",
       p:"Six consignes prises dans les écrits de ce module.",
       rows:[
         ["Laissez-moi votre nom et votre numéro.","affirmative, pronom derrière"],
         ["Ne me laissez pas de message sur cette ligne.","négative, pronom devant"],
         ["Rappelez-la avant midi, s’il vous plaît.","un seul pronom"],
         ["Envoyez-le à la paie dès aujourd’hui.","« le » remplace le formulaire"],
         ["Ne la lui envoyez pas sans la signature.","deux pronoms, à la négative"],
         ["Donnez-le-moi avant vendredi.","deux pronoms, à l’affirmative"],
       ]},

      {t:'piege', h:"Trois pièges de l’impératif",
       rows:[
         ["garder le pronom sujet","« Vous laissez-moi un message. »",
          "L’impératif n’a jamais de pronom sujet devant lui. Ni « vous », ni « tu », ni « nous »."],
         ["laisser le pronom derrière à la négative","« Ne rappelez-la pas. »",
          "Dès qu’il y a une négation, le pronom revient devant le verbe : « Ne la rappelez pas. » Sans trait d’union."],
         ["garder le s à la deuxième personne","« Écoutes ce message. »",
          "Les verbes en -er perdent leur s : « Écoute ce message. » Les autres le gardent : « Finis ta note. »"],
       ]},

      {t:'check', h:"Est-ce que c’est clair maintenant ?",
       p:"Quatre questions rapides.",
       qs:[
         {q:"À l’affirmative, le pronom se met…", opts:["devant le verbe","après le verbe"], ok:1,
          fb:"Après, avec un trait d’union : « Rappelez-la »."},
         {q:"À la négative, le pronom se met…", opts:["devant le verbe","après le verbe"], ok:0,
          fb:"Devant, sans trait d’union : « Ne la rappelez pas »."},
         {q:"« Tu écoutes » à l’impératif donne…", opts:["Écoutes","Écoute"], ok:1,
          fb:"Écoute. Les verbes en -er perdent leur s à cette personne."},
         {q:"« Dites-moi » à la négative donne…", opts:["Ne me dites pas","Ne dites-moi pas"], ok:0,
          fb:"Ne me dites pas : « moi » redevient « me » et repasse devant."},
       ]},
    ]
  },

  // ════════════════════════════════════════════════════════════════════════
  t1rap: {
    eye:'Mini-leçon', tit:"Rapporter ce que la personne a dit",
    blocs:[
      {t:'texte', h:"Le geste qui transforme un appel en note",
       p:"Quand vous prenez un message, vous n’êtes plus celle qui parle : vous êtes celle qui raconte ce que quelqu’un d’autre a dit. Le français a une façon précise de faire ça, et elle change trois choses à la fois : le mot qui relie les deux phrases, les pronoms, et l’ordre des mots dans la question.",
       note:"Le programme du niveau 5 le dit dans ses attentes de fin de cours : « Il rapporte le sens général des propos de quelqu’un au présent en employant les pronoms et les déterminants appropriés. » C’est exactement l’exercice de la note d’appel."},

      {t:'ana', h:"Une affirmation → « que »",
       p:"Le plus simple des trois cas, et le plus fréquent dans une note.",
       mots:[["Ce qu’on entend","« Je ne peux pas venir mercredi. »"],["Ce qu’on écrit","Elle dit qu’elle ne peut pas venir mercredi.",true],["Ce qui change","je → elle · mon → son · ici → là"]],
       say:"Elle dit qu’elle ne peut pas venir mercredi.",
       note:"Le verbe qui rapporte reste au présent : <i>elle dit</i>, <i>elle demande</i>, <i>il explique</i>. La note est lue le jour même : rien n’oblige à passer au passé."},

      {t:'ana', h:"Une question par oui ou non → « si »",
       p:"C’est le cas qui trahit le plus vite quelqu’un qui débute.",
       mots:[["Ce qu’on entend","« Est-ce que quelqu’un peut passer ? »"],["Ce qu’on écrit","Elle demande si quelqu’un peut passer.",true],["Ce qui disparaît","est-ce que · l’inversion · le point d’interrogation"]],
       say:"Elle demande si quelqu’un peut passer avant jeudi.",
       note:"Jamais « elle demande si est-ce que ». Jamais de point d’interrogation à la fin : la phrase entière est une affirmation, même si elle contient une question."},

      {t:'ana', h:"Une question avec un mot interrogatif → le mot reste",
       p:"Le mot de la question — quand, où, combien, comment, pourquoi, qui — reste en place ; c’est l’ordre des mots qui redevient ordinaire.",
       mots:[["Ce qu’on entend","« Quand est-ce que vous me rappelez ? »"],["Ce qu’on écrit","Elle demande quand nous la rappelons.",true],["Deux cas à part","qu’est-ce que → ce que · qu’est-ce qui → ce qui"]],
       say:"Elle demande quand nous la rappelons et ce qu’il faut préparer.",
       note:"L’erreur typique est de garder l’inversion : « elle demande quand la rappelons-nous ». Après le mot interrogatif, on remet sujet puis verbe."},

      {t:'labo', h:"Cinq phrases entendues, cinq phrases écrites",
       p:"Choisissez une phrase du message de madame Thériault.",
       axes:[{id:'p', lbl:'Quelle phrase ?', opts:[
         ['a','Elle annonce quelque chose'],
         ['b','Elle pose une question fermée'],
         ['c','Elle pose une question ouverte'],
         ['d','Elle demande quelque chose'],
         ['e','Elle donne un ordre poli']]}],
       out:{
         a:{w:['une abréviation'], say:"Elle dit que son aide du mercredi ne pourra pas venir cette semaine.", n:"« que » relie, les pronoms changent"},
         b:{w:['rappeler'], say:"Elle demande si quelqu’un d’autre peut passer avant jeudi.", n:"« si », sans « est-ce que »"},
         c:{w:['un message d\'accueil'], say:"Elle demande quand nous pourrons la rappeler.", n:"« quand » reste, l’inversion disparaît"},
         d:{w:['l\'accueil'], say:"Elle demande ce qu’il faut préparer avant son rendez-vous.", n:"« qu’est-ce que » devient « ce que »"},
         e:{w:['une tâche'], say:"Elle demande de la rappeler avant midi.", n:"un ordre devient « de » plus l’infinitif"},
       },
       note:"Écoutez, puis écrivez la phrase de mémoire avant de la réécouter. C’est ce qu’on fait en vrai, avec un message qu’on ne peut pas repasser trois fois."},

      {t:'ex', h:"À écouter et à répéter",
       p:"Six phrases de note d’appel.",
       rows:[
         ["Elle dit que son aide ne viendra pas cette semaine.","affirmation rapportée"],
         ["Elle demande si quelqu’un peut passer avant jeudi.","question fermée"],
         ["Elle demande quand nous la rappelons.","question ouverte"],
         ["Elle demande où se trouve le formulaire.","« où » suivi du verbe"],
         ["Elle demande ce qu’il faut apporter.","« qu’est-ce que » devenu « ce que »"],
         ["Elle demande de la rappeler avant midi.","un ordre rapporté"],
       ]},

      {t:'piege', h:"Trois pièges du discours rapporté",
       rows:[
         ["garder « est-ce que »","« Elle demande si est-ce que quelqu’un peut venir. »",
          "« Si » remplace « est-ce que » : il ne s’ajoute pas à lui. Une seule des deux formes survit."],
         ["garder le point d’interrogation","« Elle demande quand nous la rappelons ? »",
          "La phrase entière affirme quelque chose : elle se termine par un point. Le point d’interrogation appartient à la question directe."],
         ["oublier de changer les pronoms","« Elle dit que je ne peux pas venir. »",
          "En rapportant, « je » devient « elle » : « Elle dit qu’elle ne peut pas venir. » Sinon la note fait croire que c’est vous qui ne venez pas."],
       ]},

      {t:'check', h:"Est-ce que c’est clair maintenant ?",
       p:"Quatre questions rapides.",
       qs:[
         {q:"« Est-ce que c’est prêt ? » rapporté devient…", opts:["… demande si c’est prêt","… demande est-ce que c’est prêt"], ok:0,
          fb:"« si » remplace « est-ce que » ; il ne s’ajoute pas."},
         {q:"Une phrase rapportée se termine par…", opts:["un point","un point d’interrogation"], ok:0,
          fb:"Un point : la phrase entière affirme, même si elle contient une question."},
         {q:"« Qu’est-ce qu’il faut faire ? » devient…", opts:["ce qu’il faut faire","qu’est-ce qu’il faut faire"], ok:0,
          fb:"« qu’est-ce que » devient « ce que » à l’intérieur d’une phrase."},
         {q:"Dans une note, le verbe qui rapporte est au…", opts:["présent","passé simple"], ok:0,
          fb:"Au présent : « elle dit », « elle demande ». La note est lue le jour même."},
       ]},
    ]
  },

  // ════════════════════════════════════════════════════════════════════════
  t1note: {
    eye:'Mini-leçon', tit:"La note d’appel : six lignes qui suffisent",
    blocs:[
      {t:'texte', h:"Le test d’une bonne note",
       p:"Posez la note sur le bureau de quelqu’un d’autre et partez en congé. Si cette personne peut agir sans vous téléphoner, la note est bonne. Si elle doit vous appeler pour comprendre, la note ne valait pas la peine d’être écrite : autant ne rien noter du tout.",
       note:"C’est ce que dit Ghislain à Dorine : « Six lignes, et je peux agir sans vous poser une seule question. »"},

      {t:'ana', h:"Les six lignes, dans l’ordre",
       p:"Toujours les mêmes, toujours dans cet ordre : c’est ce qui permet de les remplir en écoutant.",
       mots:[["Qui, quand, où","Mme Thériault · mardi 9 h 10 · 5680 Beaubien, app. 3"],["Pourquoi, et ce qu’elle demande","son aide du mercredi ne vient pas · veut un remplacement",true],["Comment la joindre, ce qui presse","514 225-1440 · rappeler avant midi"]],
       say:"Madame Thériault, mardi neuf heures dix. Elle demande un remplacement avant son rendez-vous de jeudi.",
       note:"Écrivez la ligne « comment la joindre » pendant que la personne parle, pas après : le numéro est ce qu’on perd le plus souvent."},

      {t:'ana', h:"Les abréviations qui se comprennent partout",
       p:"Une abréviation utile est une abréviation que votre collègue lit sans hésiter.",
       mots:[["Temps et lieu","RDV (rendez-vous) · app. (appartement) · a.m. et p.m."],["Communication","tél. (téléphone) · réf. (référence) · SVP",true],["Ce qu’on n’abrège pas","les noms de personnes · les motifs · les montants"]],
       say:"RDV jeudi a.m. — tél. cinq un quatre, deux deux cinq, quatorze quarante.",
       note:"Une abréviation inventée ce matin n’est pas une abréviation : c’est un code personnel. Elle n’a sa place que dans vos propres brouillons."},

      {t:'ana', h:"Ce qu’une note ne contient jamais",
       p:"Trois choses alourdissent une note sans rien lui ajouter.",
       mots:[["Vos impressions","« elle avait l’air fâchée » · « encore elle »"],["Les mots exacts, entre guillemets","une note résume, elle ne transcrit pas",true],["Les répétitions de la personne","elle l’a dit trois fois : écrivez-le une fois"]],
       say:"Une note résume ; elle ne transcrit pas et elle ne juge pas.",
       note:"Une note reste dans un dossier bien plus longtemps qu’on ne croit, et elle peut être lue par la personne concernée. Écrivez ce que vous assumeriez à voix haute devant elle."},

      {t:'labo', h:"Quatre appels, quatre notes",
       p:"Choisissez un appel et écoutez la note qu’il donne.",
       axes:[{id:'a', lbl:'Quel appel ?', opts:[
         ['a','Une cliente demande un remplacement'],
         ['b','Un fournisseur annonce un retard'],
         ['c','Une collègue est malade'],
         ['d','Un appel sans motif clair'],
         ['e','Le bas de la note']]}],
       out:{
         a:{w:['une abréviation'], say:"Mme Thériault, 5680 Beaubien, app. 3. Aide du mercredi absente. Demande un remplacement avant son RDV de jeudi. Tél. 514 225-1440. Rappeler avant midi.", n:"les six lignes, complètes"},
         b:{w:['le bac à papier'], say:"Fournisseur de papier. Livraison de jeudi reportée à lundi. Demande de confirmer la réception. Tél. au dossier. Rien d’urgent.", n:"même structure, appel banal"},
         c:{w:['le registre des heures'], say:"Amel, ce matin. Absente aujourd’hui, malade. Reprend demain si ça va mieux. Demande d’aviser Ghislain. Tél. cellulaire.", n:"une absence se note comme le reste"},
         d:{w:['une tâche'], say:"Homme, n’a pas donné son nom. Demande à parler à la directrice, ne dit pas pourquoi. Rappellera lui-même en après-midi. Aucun numéro laissé.", n:"écrire ce qui manque est aussi une information"},
         e:{w:['l\'accueil'], say:"Note prise par Dorine Kabeya, le mardi 20 mai, à neuf heures dix.", n:"la date et le nom, toujours en bas"},
       },
       note:"Remarquez la dernière : dire « aucun numéro laissé » vaut mieux que de laisser la ligne vide, qui fait croire à un oubli."},

      {t:'ex', h:"À écouter et à répéter",
       p:"Six lignes de note, telles qu’on les écrit.",
       rows:[
         ["Mme Thériault, 5680 Beaubien, app. 3.","qui, et où"],
         ["Son aide du mercredi ne viendra pas cette semaine.","pourquoi elle appelle"],
         ["Elle demande un remplacement avant son RDV de jeudi.","ce qu’elle demande"],
         ["Tél. : 514 225-1440.","comment la joindre"],
         ["Rappeler avant midi ; après, elle ne répond pas.","ce qui presse"],
         ["Note prise par Dorine Kabeya, le mardi 20 mai.","la date et le nom"],
       ]},

      {t:'piege', h:"Trois pièges de la note d’appel",
       rows:[
         ["noter sans le numéro","« Mme Thériault a appelé, rappeler. »",
          "Sans numéro, votre collègue doit chercher dans un dossier ou vous appeler. Le numéro se note pendant que la personne parle."],
         ["inventer ses abréviations","« Rmplc mrcr av. RDV jd »",
          "Personne d’autre ne lit ça, et vous non plus dans trois jours. RDV, app., tél., a.m. : celles-là suffisent."],
         ["oublier la date et le nom","une note anonyme au milieu d’un bureau",
          "Sans date, on ne sait pas si l’appel date de ce matin ou de mardi passé. Sans nom, on ne sait pas à qui demander ce qui manque."],
       ]},

      {t:'check', h:"Est-ce que c’est clair maintenant ?",
       p:"Quatre questions rapides.",
       qs:[
         {q:"Une bonne note se reconnaît à ce que…", opts:["elle est courte","on peut agir sans appeler celui qui l’a écrite"], ok:1,
          fb:"C’est le seul vrai test. Une note courte mais incomplète ne vaut rien."},
         {q:"On écrit ses impressions sur la personne…", opts:["oui, ça aide","non, jamais"], ok:1,
          fb:"Jamais. Une note peut être lue longtemps, et par la personne concernée."},
         {q:"« app. » veut dire…", opts:["appel","appartement"], ok:1,
          fb:"Appartement. « tél. » est l’abréviation du téléphone."},
         {q:"La date et le nom se mettent…", opts:["en haut, en gros","en bas de la note"], ok:1,
          fb:"En bas, et ils prennent quatre secondes à écrire."},
       ]},
    ]
  },

  // ════════════════════════════════════════════════════════════════════════
  t2mode: {
    eye:'Mini-leçon', tit:"Les verbes qu’on retrouve sur tous les appareils",
    blocs:[
      {t:'texte', h:"Trente verbes pour tout le matériel d’un bureau",
       p:"Un mode d’emploi n’écrit pas comme un roman. Il emploie une trentaine de verbes, toujours les mêmes, et il les répète. Ces verbes-là ne servent pas seulement pour le photocopieur : ils reviennent sur le lave-vaisselle de la cuisine, sur le terminal de paiement du dépanneur, sur le guichet de la banque et sur l’écran du téléphone. Les apprendre une fois, c’est cesser d’avoir peur des appareils.",
       note:"C’est ce que le programme appelle « vocabulaire lié aux directives d’utilisation » et il en nomme quatre : appuyer, insérer, verrouiller, confirmer."},

      {t:'ana', h:"Les verbes du doigt : appuyer, insérer, retirer",
       p:"Ceux qui décrivent un geste de la main sur l’appareil.",
       mots:[["appuyer sur","presser un bouton, une touche, l’écran"],["insérer dans","faire entrer une carte, une feuille, une clé dans une fente",true],["retirer","sortir ce qui était resté dedans : votre carte, votre original"]],
       say:"Appuyez sur le bouton vert, insérez votre carte, puis retirez votre original.",
       note:"« Retirer » est le verbe des choses qu’on oublie. Presque tous les appareils publics le disent à la fin, et presque personne ne l’écoute."},

      {t:'ana', h:"Les verbes de la décision : confirmer, annuler, verrouiller",
       p:"Ceux qui portent sur ce que l’appareil va faire, pas sur la main.",
       mots:[["confirmer","dire oui une seconde fois, pour valider un choix"],["annuler","arrêter avant que ce soit fait",true],["verrouiller","bloquer l’accès, ou protéger par un code"]],
       say:"Confirmez l’adresse, ou annulez pour recommencer.",
       note:"Confirmer et annuler sont presque toujours côte à côte sur un écran. Lisez lequel est à gauche avant d’appuyer : la place change d’un appareil à l’autre."},

      {t:'ana', h:"Les verbes de l’endroit : placer, refermer",
       p:"Ceux qui viennent toujours avec une indication de lieu.",
       mots:[["placer","Placez la feuille face vers le bas, dans le coin en haut à gauche."],["refermer","Refermez bien la porte de côté.",true],["La préposition ne se choisit pas","appuyer sur · insérer dans · placer dans, sur · retirer de"]],
       say:"Placez la feuille dans le chargeur, puis refermez bien le couvercle.",
       note:"Apprenez le verbe avec sa préposition, comme un seul mot : « appuyer-sur », « insérer-dans ». Séparés, ils se mélangent."},

      {t:'labo', h:"Le même verbe, quatre appareils",
       p:"Choisissez un verbe et écoutez-le là où vous le rencontrerez.",
       axes:[{id:'v', lbl:'Quel verbe ?', opts:[
         ['a','appuyer'],
         ['b','insérer'],
         ['c','confirmer'],
         ['d','verrouiller'],
         ['e','retirer']]}],
       out:{
         a:{w:['un photocopieur'], say:"Appuyez sur le bouton vert. Appuyez sur le carré rouge pour arrêter. Appuyez deux secondes pour éteindre.", n:"toujours « appuyer sur », jamais « appuyer le »"},
         b:{w:['le bac à papier'], say:"Insérez votre carte dans la fente. Insérez le papier dans le bac du bas.", n:"toujours « insérer dans »"},
         c:{w:['un mode d\'emploi'], say:"Confirmez l’adresse courriel. Confirmez le montant. Confirmez en appuyant sur OK.", n:"une seconde fois, pour être sûr"},
         d:{w:['des directives'], say:"Verrouillez l’écran en partant. Verrouillez la porte du local à onze heures.", n:"un écran ou une porte, même verbe"},
         e:{w:['un bourrage de papier'], say:"Retirez votre carte. Retirez votre original sous le couvercle. Retirez la feuille coincée, sans forcer.", n:"le verbe de ce qu’on oublie"},
       },
       note:"Répétez chaque série à voix haute : c’est la préposition qu’il faut retenir, plus encore que le verbe."},

      {t:'ex', h:"À écouter et à répéter",
       p:"Six directives, telles qu’un appareil les écrit.",
       rows:[
         ["Appuyez sur Numériser.","appuyer + sur"],
         ["Insérez votre carte dans la fente.","insérer + dans"],
         ["Placez la feuille face vers le bas.","placer + un endroit"],
         ["Confirmez l’adresse courriel.","confirmer, sans préposition"],
         ["Refermez bien la porte de côté.","refermer, et « bien »"],
         ["Retirez votre original avant de partir.","le geste qu’on oublie"],
       ]},

      {t:'piege', h:"Trois pièges du vocabulaire des appareils",
       rows:[
         ["oublier la préposition","« Appuyez le bouton vert. »",
          "On appuie <b>sur</b> quelque chose. Sans la préposition, la phrase se comprend mais elle se remarque tout de suite."],
         ["confondre le chargeur et le bac à papier","mettre les feuilles blanches dans le chargeur",
          "Le chargeur est en haut : il reçoit ce qu’on veut copier. Le bac à papier est en bas : il reçoit les feuilles blanches, celles qui sortiront."],
         ["confondre annuler et éteindre","appuyer trois secondes sur le bouton d’arrêt pour annuler une copie",
          "« Annuler » arrête une seule tâche ; éteindre coupe tout, et le collègue qui attendait ses vingt copies recommence depuis le début."],
       ]},

      {t:'check', h:"Est-ce que c’est clair maintenant ?",
       p:"Quatre questions rapides.",
       qs:[
         {q:"On appuie…", opts:["sur un bouton","un bouton"], ok:0,
          fb:"Sur. La préposition fait partie du verbe : « appuyer sur »."},
         {q:"Le bac à papier reçoit…", opts:["les feuilles à copier","les feuilles blanches"], ok:1,
          fb:"Les feuilles blanches. Ce qu’on veut copier va dans le chargeur, en haut."},
         {q:"« Confirmer » veut dire…", opts:["dire oui une seconde fois","recommencer"], ok:0,
          fb:"Dire oui une seconde fois, pour valider un choix déjà fait."},
         {q:"Le verbe des choses qu’on oublie est…", opts:["retirer","placer"], ok:0,
          fb:"Retirer : sa carte, son original, sa monnaie. Les appareils le disent, personne ne l’écoute."},
       ]},
    ]
  },

  // ════════════════════════════════════════════════════════════════════════
  t2ordre: {
    eye:'Mini-leçon', tit:"Les mots qui mettent les gestes en file",
    blocs:[
      {t:'texte', h:"Sans eux, l’ordre se perd",
       p:"Écrivez « Refermez la porte. Tirez la feuille. » et quelqu’un refermera la porte avant de tirer la feuille — parce que c’est écrit dans cet ordre, et qu’on lit vite. Les marqueurs de temps sont là pour empêcher ça. Ils coûtent trois mots et ils rendent une marche à suivre impossible à lire à l’envers.",
       note:"Le programme les nomme deux fois dans les savoirs du niveau 5 : « marqueurs de temps », pour la démarche administrative et pour les directives d’utilisation. Ce sont les mêmes."},

      {t:'ana', h:"La file simple : d’abord, ensuite, puis, enfin",
       p:"Quatre mots, quatre places. C’est la façon la plus lisible d’écrire quatre gestes.",
       mots:[["Le premier","D’abord, levez le couvercle."],["Ceux du milieu","Ensuite, choisissez le nombre de copies. Puis, appuyez sur le bouton vert.",true],["Le dernier","Enfin, reprenez votre original."]],
       say:"D’abord, levez le couvercle. Ensuite, choisissez le nombre de copies. Puis, appuyez sur le bouton vert. Enfin, reprenez votre original.",
       note:"L’autre façon est de numéroter : premièrement, deuxièmement, troisièmement. Choisissez l’une des deux et tenez-la jusqu’à la dernière ligne : mélanger les deux se remarque."},

      {t:'ana', h:"Le geste qui attend l’autre : une fois que, après avoir",
       p:"Quand il ne faut surtout pas commencer le second avant que le premier soit fini.",
       mots:[["une fois que + phrase","Une fois que l’écran est vert, appuyez sur Démarrer."],["après avoir + participe passé","Après avoir choisi le format, appuyez sur Confirmer.",true],["lorsque, quand + phrase","Lorsque la copie est sortie, reprenez votre original."]],
       say:"Une fois que l’écran est vert, appuyez sur Démarrer.",
       note:"« Après avoir » exige que ce soit la même personne qui fasse les deux gestes. « Une fois que » n’a pas cette contrainte : on peut attendre que l’appareil, lui, ait fini."},

      {t:'ana', h:"Ce qui vient avant tout : avant de",
       p:"La forme des avertissements, parce qu’elle met la condition en premier, là où on la lit.",
       mots:[["avant de + infinitif","Avant de tirer la feuille, ouvrez la porte de côté."],["Comparez","Ouvrez la porte de côté avant de tirer la feuille.",true],["La différence","la première version est lue par quelqu’un qui n’a encore rien fait"]],
       say:"Avant de tirer la feuille, ouvrez la porte de côté.",
       note:"Dans un avertissement, l’ordre des mots compte autant que les mots : ce qui est écrit en premier est ce qui sera lu avant le geste."},

      {t:'labo', h:"La même marche à suivre, quatre appareils",
       p:"Choisissez une opération et écoutez-la, ordonnée.",
       axes:[{id:'o', lbl:'Quelle opération ?', opts:[
         ['a','Faire une copie'],
         ['b','Numériser vers un courriel'],
         ['c','Remplir le bac à papier'],
         ['d','Régler un bourrage'],
         ['e','Verrouiller en partant']]}],
       out:{
         a:{w:['un photocopieur'], say:"D’abord, levez le couvercle. Ensuite, placez la feuille face vers le bas. Puis, appuyez sur le bouton vert. Enfin, reprenez votre original.", n:"quatre gestes, quatre marqueurs"},
         b:{w:['un mode d\'emploi'], say:"D’abord, placez le document dans le chargeur. Ensuite, appuyez sur Numériser. Puis, entrez l’adresse courriel. Enfin, confirmez.", n:"la page trente-quatre du livret, en quatre lignes"},
         c:{w:['le bac à papier'], say:"Avant d’ouvrir le bac, vérifiez le format du papier. Une fois le bac ouvert, placez la pile bien à plat. Enfin, refermez sans forcer.", n:"un avertissement en tête"},
         d:{w:['un bourrage de papier'], say:"Avant de tirer la feuille, ouvrez la porte de côté. Ensuite, tirez lentement, d’un seul mouvement. Enfin, refermez bien la porte.", n:"trois gestes, et le mot « lentement »"},
         e:{w:['des directives'], say:"Une fois que tout le monde est parti, éteignez l’écran. Puis, verrouillez la porte du local.", n:"« une fois que » attend une condition"},
       },
       note:"Écoutez, puis récrivez la marche à suivre de mémoire. C’est ce qu’on fait quand on écrit une demi-page pour ses collègues."},

      {t:'ex', h:"À écouter et à répéter",
       p:"Six phrases ordonnées.",
       rows:[
         ["D’abord, levez le couvercle.","le premier geste"],
         ["Ensuite, choisissez le nombre de copies.","le deuxième"],
         ["Puis, appuyez sur le gros bouton vert.","le troisième"],
         ["Enfin, reprenez votre original.","le dernier, et le plus oublié"],
         ["Avant de tirer la feuille, ouvrez la porte de côté.","un avertissement"],
         ["Une fois que l’écran est vert, vous pouvez recommencer.","une condition à attendre"],
       ]},

      {t:'piege', h:"Trois pièges des marqueurs de temps",
       rows:[
         ["mélanger les deux systèmes","« D’abord… Deuxièmement… Puis… Quatrièmement… »",
          "Les mots ou les nombres, mais pas les deux. Le lecteur cherche alors s’il a sauté une étape."],
         ["oublier la virgule","« D’abord levez le couvercle. »",
          "Un marqueur en tête de phrase prend une virgule : « D’abord, levez le couvercle. » Placé au milieu, il n’en prend pas : « Levez ensuite le couvercle. »"],
         ["employer « après » tout seul","« Après appuyez sur le bouton vert. »",
          "« Après » demande quelque chose derrière lui : « après avoir choisi le format », « après la copie ». Seul, en tête de phrase, c’est « ensuite » qu’il faut."],
       ]},

      {t:'check', h:"Est-ce que c’est clair maintenant ?",
       p:"Quatre questions rapides.",
       qs:[
         {q:"Le dernier geste s’annonce par…", opts:["enfin","ensuite"], ok:0,
          fb:"Enfin, ou finalement. « Ensuite » sert au milieu de la liste."},
         {q:"« Avant de » est suivi…", opts:["d’un infinitif","d’une phrase complète"], ok:0,
          fb:"D’un infinitif : « avant de tirer », « avant d’ouvrir »."},
         {q:"Un marqueur en tête de phrase prend…", opts:["une virgule","rien"], ok:0,
          fb:"Une virgule. Au milieu de la phrase, il n’en prend pas."},
         {q:"« Après avoir choisi » exige que les deux gestes soient faits…", opts:["par la même personne","par n’importe qui"], ok:0,
          fb:"Par la même personne. Sinon on emploie « une fois que »."},
       ]},
    ]
  },

  // ════════════════════════════════════════════════════════════════════════
  t2cons: {
    eye:'Mini-leçon', tit:"Impératif ou infinitif : deux façons d’écrire une consigne",
    blocs:[
      {t:'texte', h:"Le même geste, deux tons",
       p:"« Appuyez sur le bouton vert » et « Appuyer sur le bouton vert » demandent exactement la même chose. La première s’adresse à quelqu’un ; la seconde ne s’adresse à personne. C’est toute la différence, et elle décide de laquelle vous emploierez selon ce que vous écrivez.",
       note:"Ce choix se fait au début, pas en cours de route. Une demi-page qui mélange les deux formes se lit mal et donne l’impression d’avoir été écrite à deux mains."},

      {t:'ana', h:"L’impératif — quand vous parlez à vos collègues",
       p:"Il s’adresse à une personne. Il est plus chaleureux, un peu plus long.",
       mots:[["Où on l’emploie","une note collée au mur · un courriel · une consigne dite de vive voix"],["Comment ça sonne","Appuyez sur le bouton vert. · Placez la feuille dans le chargeur.",true],["À la négative","N’ouvrez pas la porte du bas. · Ne forcez pas."]],
       say:"Appuyez sur le bouton vert, puis placez la feuille dans le chargeur.",
       note:"C’est la forme que Dorine et Kevin choisissent pour leur demi-page : ils écrivent à des gens qu’ils connaissent, dans un corridor où ils passent tous les jours."},

      {t:'ana', h:"L’infinitif — quand vous écrivez une affiche",
       p:"Il ne s’adresse à personne en particulier. Plus court, plus neutre, un peu plus froid.",
       mots:[["Où on l’emploie","un livret d’appareil · une affiche · une recette · un formulaire"],["Comment ça sonne","Appuyer sur le bouton vert. · Placer la feuille dans le chargeur.",true],["À la négative","Ne pas ouvrir la porte du bas. · Ne pas forcer."]],
       say:"Appuyer sur le bouton vert, puis placer la feuille dans le chargeur.",
       note:"C’est la forme du livret de quatre-vingts pages, et c’est une des raisons pour lesquelles personne ne le lit avec plaisir."},

      {t:'ana', h:"La négation, le seul vrai piège",
       p:"Les deux formes ne nient pas de la même façon, et c’est là qu’on se trompe en passant de l’une à l’autre.",
       mots:[["Impératif : la négation entoure","N’ouvrez pas. · Ne forcez pas. · Ne laissez pas votre original."],["Infinitif : les deux mots restent collés devant","Ne pas ouvrir. · Ne pas forcer. · Ne pas laisser son original.",true],["Ce qui change aussi","votre → son, vos → ses : l’infinitif ne parle à personne"]],
       say:"N’ouvrez pas la porte du bas. Ne pas ouvrir la porte du bas.",
       note:"Écoutez les deux phrases à la suite : « ne … pas » qui s’écarte, « ne pas » qui reste soudé. C’est le seul détail à retenir de cette leçon."},

      {t:'labo', h:"La même consigne dans les deux formes",
       p:"Choisissez une consigne et écoutez ses deux versions.",
       axes:[{id:'c', lbl:'Quelle consigne ?', opts:[
         ['a','Appuyer sur Numériser'],
         ['b','Insérer sa carte'],
         ['c','Ne pas forcer'],
         ['d','Ne pas laisser son original'],
         ['e','Verrouiller en partant']]}],
       out:{
         a:{w:['un mode d\'emploi'], say:"Appuyez sur Numériser. Appuyer sur Numériser.", n:"affirmatif : seule la terminaison change"},
         b:{w:['le bac à papier'], say:"Insérez votre carte dans la fente. Insérer sa carte dans la fente.", n:"« votre » devient « sa » à l’infinitif"},
         c:{w:['un bourrage de papier'], say:"Ne forcez pas sur la feuille coincée. Ne pas forcer sur la feuille coincée.", n:"la négation s’ouvre, puis se soude"},
         d:{w:['des directives'], say:"Ne laissez pas votre original sur la vitre. Ne pas laisser son original sur la vitre.", n:"deux changements dans la même phrase"},
         e:{w:['une tâche'], say:"Verrouillez l’écran en partant. Verrouiller l’écran en partant.", n:"l’affiche du local, et le courriel du collègue"},
       },
       note:"Dites-vous à chaque fois : « est-ce que j’écris à quelqu’un, ou est-ce que j’écris une affiche ? » La réponse choisit la forme."},

      {t:'ex', h:"À écouter et à répéter",
       p:"Six consignes, trois de chaque forme.",
       rows:[
         ["Appuyez sur le bouton vert.","impératif, à vos collègues"],
         ["Appuyer sur le bouton vert.","infinitif, sur l’affiche"],
         ["Ne forcez pas sur la feuille.","impératif négatif"],
         ["Ne pas forcer sur la feuille.","infinitif négatif"],
         ["Refermez bien la porte de côté.","impératif"],
         ["Ne pas laisser son original sur la vitre.","infinitif, avec « son »"],
       ]},

      {t:'piege', h:"Trois pièges des consignes écrites",
       rows:[
         ["mélanger les deux formes","« Levez le couvercle. Puis placer la feuille. »",
          "Choisissez au début et tenez-vous-y. Le mélange donne l’impression que deux personnes ont écrit la note."],
         ["nier à l’infinitif comme à l’impératif","« Ne ouvrir pas la porte. »",
          "À l’infinitif, les deux mots de la négation restent collés devant : « Ne pas ouvrir la porte. »"],
         ["ajouter « vous devez »","« Vous devez appuyer sur le bouton vert. »",
          "C’est plus long et ça n’ajoute rien : une consigne dit déjà qu’il faut le faire. « Appuyez sur le bouton vert » suffit."],
       ]},

      {t:'check', h:"Est-ce que c’est clair maintenant ?",
       p:"Quatre questions rapides.",
       qs:[
         {q:"« Ne pas ouvrir » est…", opts:["un impératif","un infinitif"], ok:1,
          fb:"Un infinitif : les deux mots de la négation restent devant le verbe."},
         {q:"Pour une note écrite à ses collègues, on choisit…", opts:["l’impératif","l’infinitif"], ok:0,
          fb:"L’impératif : elle s’adresse à quelqu’un."},
         {q:"« Insérez votre carte » à l’infinitif donne…", opts:["Insérer votre carte","Insérer sa carte"], ok:1,
          fb:"« Insérer sa carte » : l’infinitif ne parle à personne, donc « votre » devient « sa »."},
         {q:"Mélanger les deux formes dans une même note…", opts:["se remarque","n’a aucune importance"], ok:0,
          fb:"Se remarque tout de suite, et rend la note plus difficile à suivre."},
       ]},
    ]
  },

  // ════════════════════════════════════════════════════════════════════════
  t2pb: {
    eye:'Mini-leçon', tit:"Où s’arrête ce qu’on répare soi-même",
    blocs:[
      {t:'texte', h:"Une règle, et elle tient en une phrase",
       p:"Ce qui s’ouvre par une porte prévue à cette fin et se règle sans outil, vous le faites. Ce qui demande de forcer, de dévisser ou de deviner, vous ne le faites pas. Et vous ne le faites surtout pas deux fois : un appareil qu’on force deux fois passe d’une réparation de dix minutes à une réparation de trois jours.",
       note:"Cette règle n’est pas propre au photocopieur. Elle vaut pour le lave-vaisselle de la cuisine, la déchiqueteuse, la machine à café et le terminal de paiement."},

      {t:'ana', h:"Ce que vous faites vous-même",
       p:"Trois situations, et vous n’avez besoin de personne.",
       mots:[["Le bourrage simple","ouvrir la porte de côté, tirer lentement, refermer"],["Le bac vide","vérifier le format, poser la pile bien à plat, refermer sans forcer",true],["L’écran qui pose une question","lire, répondre, confirmer — la plupart des blocages sont là"]],
       say:"Ouvrez la porte de côté, tirez la feuille lentement, puis refermez bien.",
       note:"« Lentement » et « d’un seul mouvement » ne sont pas des politesses : une feuille tirée par saccades se déchire, et le morceau qui reste dedans, lui, demande le service technique."},

      {t:'ana', h:"Ce qui n’est jamais à vous",
       p:"Cinq signes qui font arrêter tout de suite et appeler.",
       mots:[["Ce qui se sent ou s’entend","une odeur de brûlé · de la fumée · un bruit sec et répété"],["Ce qui se voit","un liquide sous l’appareil · un écran rouge après un redémarrage",true],["Ce qu’on fait alors","on n’insiste pas, on débranche si c’est sûr, on appelle le poste dix-neuf"]],
       say:"Il y a une odeur de brûlé : je n’insiste pas, j’appelle le poste dix-neuf.",
       note:"Un appareil qui sent le brûlé et qu’on redémarre « juste pour voir » est la façon la plus rapide de transformer un problème en accident."},

      {t:'ana', h:"Ce qu’il faut dire au téléphone",
       p:"L’appel dure trente secondes s’il contient les bons mots, et cinq minutes s’il n’en contient aucun.",
       mots:[["Le message exact de l’écran","« erreur E-042, bac 2 » — mot pour mot, chiffre pour chiffre"],["L’appareil et l’endroit","le photocopieur du corridor du deuxième étage",true],["Ce que vous avez déjà essayé","« j’ai ouvert la porte de côté, il n’y avait rien »"]],
       say:"Erreur E zéro quarante-deux, bac deux, sur le photocopieur du deuxième étage.",
       note:"« Ça ne marche pas » fait déplacer quelqu’un pour rien. Le code d’erreur fait venir la bonne pièce du premier coup."},

      {t:'labo', h:"Cinq situations devant l’appareil",
       p:"Choisissez une situation et écoutez ce qu’il faut faire.",
       axes:[{id:'s', lbl:'Quelle situation ?', opts:[
         ['a','Une feuille coincée'],
         ['b','Le bac est vide'],
         ['c','Une odeur de brûlé'],
         ['d','La feuille s’est déchirée'],
         ['e','Un liquide sous l’appareil']]}],
       out:{
         a:{w:['un bourrage de papier'], say:"J’ouvre la porte de côté, je tire la feuille lentement, je referme. L’écran redevient vert.", n:"trois gestes, sans outil : c’est à vous"},
         b:{w:['le bac à papier'], say:"Je vérifie le format, je pose la pile bien à plat, je referme sans forcer.", n:"aucune permission à demander"},
         c:{w:['un photocopieur'], say:"Je n’insiste pas. Je débranche si l’accès est sûr et j’appelle le poste dix-neuf.", n:"un des cinq signes qui arrêtent tout"},
         d:{w:['des directives'], say:"Un morceau est resté à l’intérieur. Je n’essaie pas de le sortir : j’appelle le poste dix-neuf.", n:"ce qui demande de deviner n’est pas à vous"},
         e:{w:['un mode d\'emploi'], say:"Je ne touche à rien, je préviens les collègues et j’appelle le poste dix-neuf.", n:"un liquide sous un appareil branché : jamais soi-même"},
       },
       note:"Remarquez que les trois derniers se règlent par le même geste : cesser, et appeler avec les bons mots."},

      {t:'ex', h:"À écouter et à répéter",
       p:"Six phrases à dire devant un appareil.",
       rows:[
         ["J’ouvre la porte de côté et je tire la feuille lentement.","le bourrage simple"],
         ["Je vérifie le format avant de remplir le bac.","le bac à papier"],
         ["L’écran demande de confirmer l’adresse : je confirme.","la plupart des blocages"],
         ["Je n’insiste pas : j’appelle le poste dix-neuf.","la phrase qui sauve un appareil"],
         ["Erreur E-042, bac 2, photocopieur du deuxième étage.","ce qu’on dit au téléphone"],
         ["J’ai déjà ouvert la porte de côté, il n’y avait rien.","ce qu’on a essayé"],
       ]},

      {t:'piege', h:"Trois pièges devant un appareil bloqué",
       rows:[
         ["recommencer dix fois","relancer la copie après chaque message d’erreur",
          "Chaque relance ajoute une feuille dans l’appareil. Après trois essais, le bourrage simple est devenu un empilement que personne ne démêle sans outil."],
         ["dire « ça ne marche pas »","au téléphone, sans le code d’erreur",
          "Le service technique se déplace sans savoir quoi apporter. Le code affiché à l’écran vaut trois minutes d’explications."],
         ["forcer sur une feuille coincée","tirer par petits coups jusqu’à ce qu’elle vienne",
          "Elle vient — en deux morceaux. Le morceau resté à l’intérieur est exactement ce qui fait passer d’une réparation de dix minutes à une réparation de trois jours."],
       ]},

      {t:'check', h:"Est-ce que c’est clair maintenant ?",
       p:"Quatre questions rapides.",
       qs:[
         {q:"Une feuille coincée derrière la porte de côté, c’est…", opts:["à vous","au service technique"], ok:0,
          fb:"À vous : ça s’ouvre par une porte prévue à cette fin et se règle sans outil."},
         {q:"Une odeur de brûlé, on…", opts:["redémarre pour voir","arrête et on appelle"], ok:1,
          fb:"On arrête. Redémarrer « juste pour voir » transforme un problème en accident."},
         {q:"Au téléphone, on donne d’abord…", opts:["le code d’erreur exact","son opinion sur l’appareil"], ok:0,
          fb:"Le code exact : il fait venir la bonne pièce du premier coup."},
         {q:"Une feuille déchirée dont un morceau reste dedans…", opts:["se règle soi-même","demande le service technique"], ok:1,
          fb:"Demande le service technique : sortir un morceau invisible, c’est deviner."},
       ]},
    ]
  },

  // ════════════════════════════════════════════════════════════════════════
  t3etapes: {
    eye:'Mini-leçon', tit:"Une démarche administrative, du début à la confirmation",
    blocs:[
      {t:'texte', h:"Ce qu’une démarche a de particulier",
       p:"Ce n’est pas une demande : c’est une suite d’étapes obligatoires, dans un ordre fixe, dont chacune laisse une trace. On peut être tenté d’en sauter une quand on est pressé — mais le formulaire arrivé à la paie sans signature revient trois jours plus tard, et on a perdu plus de temps qu’on n’en avait gagné.",
       note:"C’est l’intention centrale de la situation « Emploi » au niveau 5 : comprendre des explications sur les principales étapes d’une démarche administrative simple, puis savoir les nommer soi-même."},

      {t:'ana', h:"Étapes 1 et 2 — vérifier, puis prendre le papier",
       p:"Les deux étapes qu’on saute le plus souvent, et qui coûtent le plus cher quand on les saute.",
       mots:[["Vérifier","au registre des heures : combien de jours il reste, et lesquels sont payés"],["Prendre le formulaire","au babillard du corridor, à côté du calendrier de l’équipe",true],["Pourquoi dans cet ordre","demander cinq jours quand il en reste trois fait perdre un aller-retour"]],
       say:"Je vérifie au registre combien de jours il me reste, puis je prends le formulaire au babillard.",
       note:"Vous avez le droit de savoir ce que le registre des heures contient sur vous. Le consulter n’est pas une faveur qu’on vous fait."},

      {t:'ana', h:"Étapes 3 et 4 — remplir, puis faire signer",
       p:"Le formulaire ne part nulle part tant qu’il n’est pas complet et signé.",
       mots:[["Les deux dates","le premier jour d’absence et le jour du retour au travail"],["La personne qui remplace","son nom, et pour quelle partie de la journée",true],["La signature","celle du chef d’équipe, sur le formulaire, pas dans un courriel"]],
       say:"J’inscris les deux dates et le nom de la personne qui me remplace, puis je le fais signer.",
       note:"« Une semaine » n’est pas une date. La case « retour » sert à savoir quel matin quelqu’un vous attend à l’accueil."},

      {t:'ana', h:"Étapes 5 et 6 — envoyer, puis attendre la confirmation",
       p:"La dernière étape est celle qu’on croit facultative, et c’est la seule qui rende le congé réel.",
       mots:[["Envoyer","le formulaire signé va au service de la paie"],["Attendre la confirmation","c’est la paie qui répond, par courriel, et c’est ce courriel qui compte",true],["Relancer","si rien n’arrive après quelques jours : un silence n’est pas un oui"]],
       say:"J’envoie le formulaire signé à la paie, puis j’attends la confirmation par courriel.",
       note:"Gardez ce courriel. C’est la seule preuve que le congé a été accordé, et c’est celle qu’on vous demandera si quelqu’un a oublié."},

      {t:'labo', h:"Les six étapes, une à une",
       p:"Choisissez une étape et écoutez ce qu’on y fait exactement.",
       axes:[{id:'e', lbl:'Quelle étape ?', opts:[
         ['a','1 — vérifier'],
         ['b','2 et 3 — prendre et remplir'],
         ['c','4 — faire signer'],
         ['d','5 et 6 — envoyer et attendre'],
         ['e','les six d’un trait']]}],
       out:{
         a:{w:['le registre des heures'], say:"Je regarde au registre des heures combien de jours il me reste, et lesquels sont payés.", n:"avant de demander quoi que ce soit"},
         b:{w:['un formulaire'], say:"Je prends le formulaire au babillard, puis j’inscris les deux dates et le nom de la personne qui me remplace.", n:"deux dates, jamais « une semaine »"},
         c:{w:['une autorisation d\'absence'], say:"Je fais signer le formulaire par mon chef d’équipe avant de l’envoyer.", n:"sans signature, il revient"},
         d:{w:['la paie'], say:"J’envoie le formulaire signé à la paie et j’attends la confirmation par courriel. Si rien n’arrive, je relance.", n:"un silence n’est pas un oui"},
         e:{w:['une tâche'], say:"Vérifier, prendre le formulaire, le remplir, le faire signer, l’envoyer à la paie, attendre la confirmation.", n:"six verbes : c’est ce qu’il faut savoir redire"},
       },
       note:"La dernière piste est celle à répéter jusqu’à la savoir : six verbes, dans l’ordre, sans notes."},

      {t:'ex', h:"À écouter et à répéter",
       p:"Les six étapes, telles qu’on les dit à quelqu’un.",
       rows:[
         ["D’abord, je vérifie combien de jours il me reste.","étape 1"],
         ["Ensuite, je prends le formulaire au babillard.","étape 2"],
         ["Puis je le remplis : les deux dates, et qui me remplace.","étape 3"],
         ["Après, je le fais signer par mon chef d’équipe.","étape 4"],
         ["Ensuite, je l’envoie à la paie.","étape 5"],
         ["Enfin, j’attends la confirmation par courriel.","étape 6"],
       ]},

      {t:'piege', h:"Trois pièges d’une démarche administrative",
       rows:[
         ["se contenter d’un oui de vive voix","« Ghislain m’a dit que c’était correct. »",
          "Une entente de corridor ne vaut rien au mois d’août, quand tout le monde a oublié la conversation. Tant que la confirmation n’est pas écrite, le congé n’existe pas."],
         ["écrire une durée au lieu de deux dates","« une semaine en août »",
          "La case « retour » sert à savoir quel matin quelqu’un vous attend. Une durée oblige à calculer, et on calcule mal."],
         ["confondre la règle de l’employeur et la loi","« Il faut trois semaines d’avance, c’est la loi. »",
          "Le délai de trois semaines vient de la coopérative. La loi, elle, oblige l’employeur à faire connaître les dates de vacances au moins quatre semaines à l’avance. Savoir d’où vient une règle permet de savoir si elle se discute."],
       ]},

      {t:'check', h:"Est-ce que c’est clair maintenant ?",
       p:"Quatre questions rapides.",
       qs:[
         {q:"La première étape est…", opts:["prendre le formulaire","vérifier ce qu’il reste"], ok:1,
          fb:"Vérifier : demander cinq jours quand il en reste trois fait perdre un aller-retour."},
         {q:"Le formulaire va à la paie…", opts:["signé","tel quel, la paie fera signer"], ok:0,
          fb:"Signé. Sans signature, il revient trois jours plus tard."},
         {q:"Tant que la confirmation écrite n’est pas arrivée…", opts:["le congé est accordé","le congé n’existe pas"], ok:1,
          fb:"Il n’existe pas. Un silence n’est pas un oui : on relance."},
         {q:"Le délai de trois semaines vient…", opts:["de la loi","de l’employeur"], ok:1,
          fb:"De l’employeur. La loi impose quatre semaines à l’employeur pour annoncer les dates de vacances."},
       ]},
    ]
  },

  // ════════════════════════════════════════════════════════════════════════
  t3fut: {
    eye:'Mini-leçon', tit:"Le futur simple, le temps des absences annoncées",
    blocs:[
      {t:'texte', h:"Pourquoi lui, et pas le futur proche",
       p:"À l’oral, « je vais être absente » se dit très bien et personne ne vous reprendra. Mais un message d’accueil, une réponse automatique et un formulaire sont des écrits, et l’écrit préfère le futur simple : « je serai absente », « je répondrai à mon retour ». C’est plus court, plus net, et c’est la forme attendue.",
       note:"Les attentes de fin de cours du niveau 5 le disent : l’adulte « écrit un texte descriptif simple pour décrire ses projets à court terme en employant de manière appropriée le futur simple ou le futur proche ». Ici, la situation choisit."},

      {t:'ana', h:"Comment il se forme",
       p:"L’infinitif entier, plus six terminaisons qui ne changent jamais.",
       mots:[["Les terminaisons","-ai, -as, -a, -ons, -ez, -ont"],["Sur un verbe en -er ou -ir","je rappellerai · vous finirez · elle partira",true],["Sur un verbe en -re, le e tombe","répondre → je répondrai · prendre → il prendra"]],
       say:"Je vous rappellerai et je répondrai à vos courriels.",
       note:"Les terminaisons sont celles du verbe « avoir » au présent : ai, as, a, (av)ons, (av)ez, ont. C’est ainsi que le futur s’est formé, il y a très longtemps."},

      {t:'ana', h:"Les irréguliers du bureau",
       p:"Huit verbes changent de base. Ce sont, évidemment, les huit qu’on emploie tous les jours.",
       mots:[["Les quatre premiers","être → je serai · avoir → j’aurai · faire → je ferai · aller → j’irai"],["Les quatre suivants","pouvoir → je pourrai · devoir → je devrai · voir → je verrai · venir → je viendrai",true],["Ce qui ne change jamais","les terminaisons : elles sont les mêmes pour tous"]],
       say:"Je serai absente, j’aurai peu de temps, mais je pourrai répondre lundi.",
       note:"Repérez le double r de « pourrai » et de « verrai » : il s’entend, et c’est lui qui distingue « je verrai » de « je vais »."},

      {t:'ana', h:"Après « quand » et « dès que », le futur",
       p:"Le français ne fait pas comme beaucoup d’autres langues, et c’est une faute très fréquente.",
       mots:[["On écrit","Je vous répondrai dès que je serai de retour."],["Et non","Je vous répondrai dès que je suis de retour.",true],["Les mots concernés","quand · dès que · lorsque · aussitôt que · tant que"]],
       say:"Je vous répondrai dès que je serai de retour au bureau.",
       note:"Deux futurs dans la même phrase, donc : celui de l’action principale, et celui d’après « dès que ». C’est correct, et c’est même obligatoire."},

      {t:'labo', h:"Le futur simple dans les quatre écrits du module",
       p:"Choisissez un écrit et écoutez comment le futur y apparaît.",
       axes:[{id:'e', lbl:'Quel écrit ?', opts:[
         ['a','Le message d’accueil'],
         ['b','La réponse automatique'],
         ['c','La note d’appel'],
         ['d','La demande de congé'],
         ['e','Les irréguliers ensemble']]}],
       out:{
         a:{w:['rappeler'], say:"Je vous rappellerai dans les meilleurs délais.", n:"un seul futur, et il suffit"},
         b:{w:['une réponse automatique'], say:"Je serai absente du 19 au 23 août. Je ne lirai pas mes courriels. Je répondrai à mon retour, le lundi 26.", n:"trois futurs, trois lignes"},
         c:{w:['une abréviation'], say:"Elle dit que son aide ne viendra pas cette semaine et qu’elle rappellera demain.", n:"un futur à l’intérieur d’une phrase rapportée"},
         d:{w:['un formulaire'], say:"Kevin prendra les appels de l’avant-midi et Amel ceux de l’après-midi.", n:"le futur des ententes"},
         e:{w:['la paie'], say:"Je serai, j’aurai, je ferai, j’irai, je pourrai, je devrai, je verrai, je viendrai.", n:"les huit irréguliers, à répéter"},
       },
       note:"La dernière piste se répète comme une gamme : huit verbes, dans l’ordre, jusqu’à ce qu’ils viennent sans réfléchir."},

      {t:'ex', h:"À écouter et à répéter",
       p:"Six phrases au futur simple, tirées des écrits de ce module.",
       rows:[
         ["Je serai absente du 19 au 23 août.","être, l’irrégulier le plus fréquent"],
         ["Je répondrai à vos courriels à mon retour.","répondre : le e de l’infinitif tombe"],
         ["Kevin prendra les appels de l’avant-midi.","prendre, même règle"],
         ["Vous pourrez le joindre au poste dix-neuf.","pouvoir, et son double r"],
         ["Nous aurons une réponse de la paie avant vendredi.","avoir"],
         ["Je vous écrirai dès que je serai de retour.","deux futurs dans la même phrase"],
       ]},

      {t:'piege', h:"Trois pièges du futur simple",
       rows:[
         ["mettre le présent après « dès que »","« Je répondrai dès que je suis de retour. »",
          "Après quand, dès que, lorsque, tant que, le français met le futur : « dès que je serai de retour »."],
         ["oublier le e des verbes en -er","« je rappelrai », « j’appelrai »",
          "Le e de l’infinitif reste : rappeler → je rappell<b>e</b>rai. On l’écrit même si on l’entend à peine."],
         ["confondre je serai et je serais","« Je serais absente du 19 au 23 août. »",
          "« Je serai » annonce un fait ; « je serais » suppose une condition. Dans une réponse automatique, c’est bien un fait."],
       ]},

      {t:'check', h:"Est-ce que c’est clair maintenant ?",
       p:"Quatre questions rapides.",
       qs:[
         {q:"« Répondre » au futur, à je, donne…", opts:["je répondrai","je répondrerai"], ok:0,
          fb:"Le e final de l’infinitif tombe pour les verbes en -re."},
         {q:"Après « dès que », on met…", opts:["le présent","le futur"], ok:1,
          fb:"Le futur : « dès que je serai de retour »."},
         {q:"« Pouvoir » au futur, à vous, donne…", opts:["vous pourrez","vous pouvrez"], ok:0,
          fb:"Vous pourrez, avec deux r qui s’entendent."},
         {q:"Dans une réponse automatique, on écrit…", opts:["je serai absente","je serais absente"], ok:0,
          fb:"« Je serai » : c’est un fait annoncé, pas une supposition."},
       ]},
    ]
  },

  // ════════════════════════════════════════════════════════════════════════
  t3int: {
    eye:'Mini-leçon', tit:"Poser sa question à l’intérieur d’une phrase",
    blocs:[
      {t:'texte', h:"La même question, en plus poli",
       p:"« Combien de jours me reste-t-il ? » n’a rien d’impoli, mais c’est direct. Devant un supérieur, dans un bureau, on emploie souvent une autre forme : « Je voudrais savoir combien de jours il me reste. » La question devient un morceau de phrase. Elle perd son inversion, son « est-ce que » et son point d’interrogation — et elle gagne beaucoup.",
       note:"C’est la forme des demandes au travail, à l’oral comme dans un courriel. C’est aussi celle qui permet d’enchaîner trois questions sans avoir l’air d’un interrogatoire."},

      {t:'ana', h:"Les trois amorces utiles",
       p:"Elles se suivent toutes d’une phrase ordinaire, jamais d’une question.",
       mots:[["Je voudrais savoir…","Je voudrais savoir si la journée est payée."],["Pourriez-vous me dire…","Pourriez-vous me dire quand je recevrai la réponse.",true],["J’aimerais comprendre…","J’aimerais comprendre ce qu’il faut écrire dans cette case."]],
       say:"Je voudrais savoir si la journée est payée, et quand je recevrai la réponse.",
       note:"« Pourriez-vous me dire où est-ce que je dois l’envoyer ? » est la faute typique : on garde l’amorce polie et la question directe en même temps. Il faut choisir."},

      {t:'ana', h:"Question fermée → « si »",
       p:"Toute question à laquelle on répond par oui ou par non devient une phrase avec « si ».",
       mots:[["La question directe","« Est-ce que la journée est payée ? »"],["À l’intérieur d’une phrase","Je voudrais savoir si la journée est payée.",true],["Ce qui disparaît","est-ce que · l’inversion · le point d’interrogation"]],
       say:"Je voudrais savoir si la journée est payée.",
       note:"Jamais « si est-ce que ». « Si » remplace « est-ce que » : il ne s’ajoute pas à lui."},

      {t:'ana', h:"Question ouverte → le mot reste, l’ordre change",
       p:"Quand, où, combien, comment, pourquoi, qui : le mot garde sa place en tête, mais ce qui suit redevient une phrase ordinaire.",
       mots:[["On garde le mot","quand · où · combien · comment · pourquoi · qui"],["On remet sujet, puis verbe","Pourriez-vous me dire quand je recevrai la réponse.",true],["Deux cas à part","qu’est-ce que → ce que · qu’est-ce qui → ce qui"]],
       say:"Pourriez-vous me dire quand je recevrai la réponse et qui me remplacera.",
       note:"L’erreur la plus fréquente est de garder l’inversion : « pourriez-vous me dire quand recevrai-je la réponse ». Après le mot interrogatif, sujet puis verbe."},

      {t:'labo', h:"Cinq questions à poser dans le bureau du chef d’équipe",
       p:"Choisissez une question et écoutez ses deux versions.",
       axes:[{id:'q', lbl:'Quelle question ?', opts:[
         ['a','Combien de jours il reste'],
         ['b','Si la journée est payée'],
         ['c','Quand la réponse arrivera'],
         ['d','Où envoyer le formulaire'],
         ['e','Ce qu’il faut remplir']]}],
       out:{
         a:{w:['le registre des heures'], say:"Combien de jours me reste-t-il ? Je voudrais savoir combien de jours il me reste.", n:"l’inversion disparaît"},
         b:{w:['une autorisation d\'absence'], say:"Est-ce que la journée est payée ? Je voudrais savoir si la journée est payée.", n:"« est-ce que » devient « si »"},
         c:{w:['la paie'], say:"Quand est-ce que je recevrai la réponse ? Pourriez-vous me dire quand je recevrai la réponse.", n:"le mot reste, l’ordre change"},
         d:{w:['un formulaire'], say:"Où est-ce que j’envoie le formulaire ? J’aimerais savoir où j’envoie le formulaire.", n:"même mouvement avec « où »"},
         e:{w:['une tâche'], say:"Qu’est-ce qu’il faut remplir ? J’aimerais savoir ce qu’il faut remplir.", n:"« qu’est-ce que » devient « ce que »"},
       },
       note:"Écoutez les deux versions à la suite : la seconde n’est pas plus longue de beaucoup, et elle change tout le ton de l’échange."},

      {t:'ex', h:"À écouter et à répéter",
       p:"Six questions telles qu’on les pose à un supérieur.",
       rows:[
         ["Je voudrais savoir combien de jours il me reste.","question fermée sur un nombre"],
         ["Je voudrais savoir si la journée est payée.","« si », sans « est-ce que »"],
         ["Pourriez-vous me dire quand je recevrai la réponse.","« quand » suivi de sujet et verbe"],
         ["J’aimerais savoir où j’envoie le formulaire.","« où »"],
         ["J’aimerais savoir ce qu’il faut écrire dans cette case.","« ce que »"],
         ["Je voudrais savoir qui me remplacera l’après-midi.","« qui »"],
       ]},

      {t:'piege', h:"Trois pièges de l’interrogation indirecte",
       rows:[
         ["garder l’inversion","« Pourriez-vous me dire quand recevrai-je la réponse. »",
          "Après le mot interrogatif, l’ordre redevient ordinaire : sujet, puis verbe. « quand je recevrai la réponse »."],
         ["garder « est-ce que »","« Je voudrais savoir si est-ce que c’est payé. »",
          "« Si » remplace « est-ce que ». Les deux ensemble ne se disent jamais."],
         ["mettre un point d’interrogation","« Je voudrais savoir quand je recevrai la réponse ? »",
          "La phrase entière n’est pas une question : elle dit ce que vous voudriez savoir. Elle se termine par un point."],
       ]},

      {t:'check', h:"Est-ce que c’est clair maintenant ?",
       p:"Quatre questions rapides.",
       qs:[
         {q:"« Est-ce que c’est payé ? » devient…", opts:["… savoir si c’est payé","… savoir si est-ce que c’est payé"], ok:0,
          fb:"« Si » remplace « est-ce que » ; les deux ensemble ne se disent pas."},
         {q:"Après « quand », dans une phrase indirecte, on met…", opts:["sujet puis verbe","verbe puis sujet"], ok:0,
          fb:"Sujet puis verbe : « quand je recevrai la réponse »."},
         {q:"La phrase entière se termine par…", opts:["un point","un point d’interrogation"], ok:0,
          fb:"Un point : elle dit ce que vous voudriez savoir, elle ne demande pas directement."},
         {q:"« Qu’est-ce qui manque ? » devient…", opts:["ce qui manque","ce que manque"], ok:0,
          fb:"« Ce qui », parce que le mot est sujet du verbe."},
       ]},
    ]
  },

  // ════════════════════════════════════════════════════════════════════════
  t3courriel: {
    eye:'Mini-leçon', tit:"La réponse automatique : cinq lignes pour une semaine",
    blocs:[
      {t:'texte', h:"Elle ne s’excuse pas : elle empêche d’attendre",
       p:"Beaucoup de réponses automatiques commencent par des regrets. Ce n’est pas leur rôle. Leur rôle est qu’une personne qui vous écrit sache en dix secondes trois choses : vous n’êtes pas là, jusqu’à quand, et à qui s’adresser d’ici là. Tout ce qui n’est pas ça peut être retiré.",
       note:"C’est l’une des sept intentions de la situation « Emploi » au niveau 5, et c’est la plus courte à produire : cinq lignes, écrites une fois, qui travaillent pendant une semaine."},

      {t:'ana', h:"Les cinq lignes, dans l’ordre",
       p:"Aucune n’est facultative, et aucune n’a besoin d’être longue.",
       mots:[["1 et 2","Bonjour. Je suis absente du 19 au 23 août."],["3 et 4","Je ne lirai pas mes courriels pendant cette période. Pour toute question, écrivez à Kevin Dorais ou faites le poste dix-neuf.",true],["5","Je répondrai à votre message à mon retour, le lundi 26 août."]],
       say:"Bonjour. Je suis absente du 19 au 23 août. Je ne lirai pas mes courriels pendant cette période. Pour toute question, écrivez à Kevin Dorais ou faites le poste dix-neuf. Je répondrai à votre message à mon retour, le lundi 26 août.",
       note:"La ligne 3 est celle qu’on oublie, et elle est utile : sans elle, la personne suppose que vous lisez vos courriels le soir, et elle attend."},

      {t:'ana', h:"La date du retour, jamais la durée",
       p:"Une durée oblige le lecteur à calculer, et il calcule à partir du mauvais jour.",
       mots:[["On écrit","Je serai de retour le lundi 26 août."],["On n’écrit pas","Je suis absente une semaine. · Je reviens dans dix jours.",true],["On donne le jour ET la date","« le lundi 26 août » se vérifie d’un coup d’œil sur un calendrier"]],
       say:"Je serai de retour le lundi 26 août.",
       note:"Le jour de la semaine évite une erreur fréquente : celui qui lit croit que vous revenez le 26, mais le 26 est un dimanche et personne ne vous trouve."},

      {t:'ana', h:"La personne à joindre, avec de quoi la joindre",
       p:"Un nom seul ne sert à rien. Et cette personne doit être prévenue avant que son nom paraisse.",
       mots:[["Le nom et le moyen","Kevin Dorais, poste dix-neuf · amel@… , poste dix-huit"],["Prévenir la personne","elle recevra vos courriels toute la semaine : c’est une politesse élémentaire",true],["Quand la mettre en marche","le vendredi avant de partir, pas le lundi de votre départ"]],
       say:"Pour toute question, écrivez à Kevin Dorais ou faites le poste dix-neuf.",
       note:"Et éteignez-la le matin du retour, avant toute autre chose : une réponse automatique qui tourne encore trois jours après le retour fait perdre trois jours à tout le monde."},

      {t:'labo', h:"Quatre absences, quatre réponses automatiques",
       p:"Choisissez une situation et écoutez la réponse qui lui convient.",
       axes:[{id:'a', lbl:'Quelle absence ?', opts:[
         ['a','Une semaine de vacances'],
         ['b','Une journée seulement'],
         ['c','Une absence sans date de retour'],
         ['d','Un départ définitif'],
         ['e','La version complète']]}],
       out:{
         a:{w:['une réponse automatique'], say:"Je suis absente du 19 au 23 août et je serai de retour le lundi 26 août.", n:"deux dates, un jour de semaine"},
         b:{w:['une autorisation d\'absence'], say:"Je suis absente aujourd’hui et je répondrai demain matin.", n:"pour une journée, trois lignes suffisent"},
         c:{w:['la paie'], say:"Je suis absente pour une durée indéterminée. Pour toute question, écrivez à Kevin Dorais, poste dix-neuf.", n:"quand on ne sait pas, on le dit"},
         d:{w:['l\'accueil'], say:"Je ne travaille plus à la Coopérative d’aide à domicile de Rosemont. Vos messages ne seront pas transférés. Écrivez à l’accueil, poste vingt-deux.", n:"il faut dire que les messages se perdent"},
         e:{w:['un formulaire'], say:"Bonjour. Je suis absente du 19 au 23 août. Je ne lirai pas mes courriels pendant cette période. Pour toute question, écrivez à Kevin Dorais ou faites le poste dix-neuf. Je répondrai à votre message à mon retour, le lundi 26 août. Salutations, Dorine Kabeya, accueil.", n:"cinq lignes et une signature"},
       },
       note:"Remarquez la troisième et la quatrième : dire ce qu’on ne sait pas, ou dire que les messages se perdent, vaut mieux que de laisser croire."},

      {t:'ex', h:"À écouter et à répéter",
       p:"Les cinq lignes, une par une.",
       rows:[
         ["Bonjour.","une seule ligne, et elle suffit"],
         ["Je suis absente du 19 au 23 août.","les deux dates"],
         ["Je ne lirai pas mes courriels pendant cette période.","la ligne qu’on oublie"],
         ["Pour toute question, écrivez à Kevin Dorais ou faites le poste dix-neuf.","le nom, et de quoi le joindre"],
         ["Je répondrai à votre message à mon retour, le lundi 26 août.","le jour et la date"],
         ["Salutations, Dorine Kabeya, accueil.","la signature, avec la fonction"],
       ]},

      {t:'piege', h:"Trois pièges de la réponse automatique",
       rows:[
         ["donner une durée au lieu d’une date","« Je suis absente une semaine. »",
          "Une semaine à partir de quand ? Le lecteur calcule à partir du jour où il lit, et il se trompe. Donnez le jour et la date du retour."],
         ["mettre le nom d’un collègue sans le prévenir","« Écrivez à Kevin Dorais. »",
          "Kevin recevra vos courriels toute la semaine. Le prévenir avant est une politesse élémentaire, et ça évite qu’il réponde « je ne suis au courant de rien »."],
         ["oublier de l’éteindre au retour","la réponse tourne encore le mercredi suivant",
          "Tout le monde continue d’écrire à Kevin, qui continue de transférer. On l’éteint le matin du retour, avant de lire ses courriels."],
       ]},

      {t:'check', h:"Est-ce que c’est clair maintenant ?",
       p:"Quatre questions rapides.",
       qs:[
         {q:"On écrit…", opts:["la durée de l’absence","la date du retour"], ok:1,
          fb:"La date du retour, avec le jour de la semaine : « le lundi 26 août »."},
         {q:"On met la réponse en marche…", opts:["le vendredi avant de partir","le lundi matin de son départ"], ok:0,
          fb:"Le vendredi : le lundi matin, vous n’êtes déjà plus là pour le faire."},
         {q:"Avant de mettre le nom d’un collègue, on…", opts:["le prévient","ne dit rien, c’est normal"], ok:0,
          fb:"On le prévient : il recevra vos courriels toute la semaine."},
         {q:"On l’éteint…", opts:["quelques jours après le retour","le matin du retour"], ok:1,
          fb:"Le matin du retour, avant toute autre chose."},
       ]},
    ]
  },

};
