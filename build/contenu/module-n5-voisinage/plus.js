const PLUS = {

  // ════════════════════════════════════════════════════════════════════════
  prPhon: {
    eye:'Mini-leçon', tit:"L’intonation : ce que la voix dit avant les mots",
    blocs:[
      {t:'texte', h:"La même phrase, deux sens",
       p:"« Vous venez samedi. » et « Vous venez samedi ? » s’écrivent avec les mêmes mots, dans le même ordre. Il n’y a ni « est-ce que », ni inversion. Une seule chose les sépare : la voix. Elle monte à la fin de la question, elle descend à la fin de l’affirmation. C’est la façon la plus courante de poser une question en français parlé du Québec, et c’est celle que vous entendrez le plus souvent dans un escalier ou au téléphone.",
       note:"Pour une oreille neuve, c’est la difficulté numéro un du français parlé : la question ne s’annonce par aucun mot. Si vous n’entendez pas la montée, vous croyez qu’on vous informe alors qu’on vous demande quelque chose — et votre silence passe pour de l’impolitesse."},

      {t:'ana', h:"La voix monte : on demande",
       p:"À la fin d’une question sans mot interrogatif, la voix monte comme une marche qu’on gravit. Plus la montée est nette, plus la question s’entend.",
       mots:[["Une invitation","Vous venez samedi ? · C’est dans la ruelle ?"],["Une vérification","Il faut apporter quelque chose ? · Vous travaillez ce jour-là ?",true],["Une surprise polie","Vous avez changé d’horaire ? · Vous étiez déjà là il y a douze ans ?"]],
       say:"Vous venez samedi ? Il faut apporter quelque chose ?",
       note:"Au téléphone, la montée doit être plus forte qu’en personne : la ligne mange les nuances, et la personne ne voit pas votre visage."},

      {t:'ana', h:"La voix descend : on affirme, ou on demande autrement",
       p:"La voix descend à la fin d’une affirmation. Et elle descend aussi à la fin d’une question qui commence par un mot interrogatif : le mot a déjà posé la question, la voix n’a plus besoin de monter.",
       mots:[["Une affirmation","La fête est le 7 juin. · Je vous réponds cette semaine."],["Une question en quand, où, qui","Quand est-ce que ça commence ? · Qui organise la fête ?",true],["Un ordre, une consigne","Répondez-moi avant jeudi. · Apportez votre chaise."]],
       say:"La fête est le 7 juin. Quand est-ce que ça commence ?",
       note:"C’est la découverte qui surprend le plus : une question peut très bien finir en descendant. Ce n’est pas le point d’interrogation qui fait monter la voix, c’est l’absence de mot interrogatif."},

      {t:'ana', h:"La voix monte au milieu : on n’a pas fini",
       p:"Dans une phrase longue, la voix monte légèrement à chaque virgule pour dire « attendez, ce n’est pas terminé », et elle ne descend qu’à la toute fin.",
       mots:[["Une invitation complète","Le samedi 7 juin, ↗ de midi à quatre heures, ↗ dans la ruelle. ↘"],["Une énumération","Un plat, ↗ une chaise, ↗ et votre bonne humeur. ↘",true],["Un message téléphonique","C’est Ndeye Faye, ↗ du troisième, ↗ je vous rappelle. ↘"]],
       say:"Le samedi 7 juin, de midi à quatre heures, dans la ruelle.",
       note:"C’est exactement ce qui rend une invitation facile à noter au téléphone : chaque montée dit à celui qui écrit « il y a une autre information après »."},

      {t:'ana', h:"L’exclamation ne monte pas : elle éclate",
       p:"Une exclamation part haut et redescend, avec plus de force sur la première syllabe. Elle ne se prononce pas comme une question.",
       mots:[["Féliciter","Quelle bonne nouvelle ! · Félicitations !"],["Dire son plaisir","Comme je suis contente ! · Que c’est beau !",true],["Réagir à un chiffre","Sept ans ! · Deux cents personnes !"]],
       say:"Quelle bonne nouvelle ! Comme je suis contente pour vous !",
       note:"Une exclamation dite avec une voix qui monte a l’air d’un doute. « Quelle bonne nouvelle ? » et « Quelle bonne nouvelle ! » sont deux choses très différentes, et la première blesse."},

      {t:'labo', h:"Écoutez la même phrase autrement",
       p:"Choisissez une phrase et écoutez ce que la voix en fait.",
       axes:[{id:'p', lbl:'Quelle phrase ?', opts:[
         ['a','Vous venez samedi'],
         ['b','La fête est le 7 juin'],
         ['c','Quand est-ce que ça commence'],
         ['d','Quelle bonne nouvelle'],
         ['e','Les trois à la suite']]}],
       out:{
         a:{w:['une invitation'], say:"Vous venez samedi ?", n:"question sans mot interrogatif : la voix monte à la fin"},
         b:{w:['une invitation'], say:"La fête est le 7 juin, de midi à quatre heures.", n:"montée à la virgule, descente à la fin"},
         c:{w:['une invitation'], say:"Quand est-ce que ça commence ?", n:"le mot « quand » a posé la question : la voix descend"},
         d:{w:['des félicitations'], say:"Quelle bonne nouvelle !", n:"l’exclamation part haut et redescend"},
         e:{w:['une invitation'], say:"Vous venez samedi ? La fête est le 7 juin. Quelle bonne nouvelle !", n:"une montée, une descente, une exclamation"},
       },
       note:"Écoutez chaque phrase deux fois : la première pour comprendre les mots, la seconde en ne guettant que la dernière syllabe."},

      {t:'ex', h:"À écouter et à répéter",
       p:"Six phrases prises dans les dialogues du module.",
       rows:[
         ["Vous arrivez du travail ?","la voix monte : c’est une question"],
         ["Je finis à trois heures maintenant.","la voix descend : c’est une réponse"],
         ["Et s’il pleut ?","question très courte, montée très nette"],
         ["On reporte au dimanche.","affirmation : rien ne monte"],
         ["Comment ça s’est passé ?","« comment » pose la question, la voix descend"],
         ["Quelle bonne nouvelle !","exclamation : haut, puis descente"],
       ]},

      {t:'piege', h:"Trois pièges de l’intonation",
       rows:[
         ["croire qu’il faut « est-ce que » pour poser une question","« Est-ce que vous venez samedi ? » dit à chaque fois",
          "Correct, mais lourd à l’oral. Entre voisins, on dit « Vous venez samedi ? » et on laisse la voix faire le travail. Gardez « est-ce que » pour l’écrit et pour les situations officielles."],
         ["dire une exclamation comme une question","« Quelle bonne nouvelle ? » avec la voix qui monte",
          "Vous avez l’air de mettre la nouvelle en doute. L’exclamation part haut sur « quelle » et redescend jusqu’au point. Exercez-vous : la première syllabe est la plus forte."],
         ["laisser tomber la voix au milieu d’une énumération","« Le 7 juin. ↘ De midi à quatre heures. ↘ »",
          "Chaque descente dit « j’ai fini ». Votre interlocuteur croit que l’information est complète et arrête d’écrire. Montez à chaque virgule tant qu’il reste quelque chose à dire."],
       ]},

      {t:'check', h:"Est-ce que c’est clair maintenant ?",
       p:"Quatre questions rapides.",
       qs:[
         {q:"« Vous venez samedi ? » — la voix…", opts:["monte à la fin","descend à la fin"], ok:0,
          fb:"Elle monte : il n’y a aucun mot interrogatif, c’est la voix qui pose la question."},
         {q:"« Qui organise la fête ? » — la voix…", opts:["monte à la fin","descend à la fin"], ok:1,
          fb:"Elle descend. Le mot « qui » a déjà posé la question."},
         {q:"Dans une longue phrase, à la virgule, la voix…", opts:["monte un peu","descend"], ok:0,
          fb:"Elle monte un peu : c’est ce qui dit « ce n’est pas fini »."},
         {q:"« Quelle bonne nouvelle ! » se dit…", opts:["comme une question","haut, puis en descendant"], ok:1,
          fb:"Haut sur « quelle », puis en descendant. Dite comme une question, elle exprime le doute."},
       ]},
    ]
  },

  // ════════════════════════════════════════════════════════════════════════
  prReg: {
    eye:'Mini-leçon', tit:"La bonne distance avec un voisin",
    blocs:[
      {t:'texte', h:"Chaleureux et vouvoyé, ce n’est pas contradictoire",
       p:"Marisol et Réjean se croisent depuis trois ans. Ils se parlent avec chaleur, ils s’entraident, ils vont manger à la même table au mois de juin — et ils se vouvoient. Entre voisins d’un même immeuble, le <b>vous</b> est la règle par défaut, et il ne dit rien de froid : il dit seulement qu’on ne se connaît pas encore assez pour avoir décidé le contraire.",
       note:"Le tutoiement s’installe quand quelqu’un le propose, presque toujours à voix haute : « on peut se tutoyer, hein ? ». Tant que personne ne l’a proposé, restez au vous — c’est le choix qui ne vexe jamais."},

      {t:'ana', h:"Ce qui se demande sans risque",
       p:"Tous ces sujets sont partagés : ils concernent l’immeuble ou la vie de quartier, pas l’intimité de la personne.",
       mots:[["L’immeuble et la ruelle","Vous savez quand ils ramassent le bac brun ? · Il y a longtemps que vous habitez ici ?"],["Le temps, les travaux, le stationnement","Ils ont fini de creuser la rue ? · Vous avez eu de l’eau au sous-sol, vous aussi ?",true],["Le travail, en général","Vous avez changé d’horaire ? · Vous travaillez de nuit, je pense ?"]],
       say:"Il y a longtemps que vous habitez ici ? Vous avez changé d’horaire ?",
       note:"Une bonne question de voisinage porte sur quelque chose que vous partagez tous les deux. C’est ce qui la rend facile à poser et facile à recevoir."},

      {t:'ana', h:"Ce qui ne se demande pas",
       p:"Ces questions ne sont interdites par aucune règle. Elles ferment simplement la porte que vous veniez d’ouvrir.",
       mots:[["L’argent","Vous payez combien de loyer ? · Vous gagnez combien ?"],["Les papiers, la santé, l’âge","Vous avez vos papiers ? · Vous êtes malade ? · Vous avez quel âge ?",true],["La vie privée","Pourquoi votre mari n’habite plus ici ? · Vous êtes séparée ?"]],
       say:"Vous payez combien de loyer ? Vous avez vos papiers ?",
       note:"Si la personne veut vous en parler, elle en parlera d’elle-même. Le rôle du voisin est d’être disponible, pas curieux."},

      {t:'ana', h:"Monsieur, madame, et le nom de famille",
       p:"Dans beaucoup d’immeubles, les voisins s’appellent par leur nom de famille pendant des années.",
       mots:[["La forme normale","Bonjour monsieur Deslauriers. · Madame Faye, vous avez une minute ?"],["Quand on ne sait pas le nom","Bonjour ! · Excusez-moi… · Vous êtes du deuxième, je pense ?",true],["Ce qu’on évite","Hé, la madame ! · Monsieur ! (crié dans la cour)"]],
       say:"Bonjour monsieur Deslauriers. Madame Faye, vous avez une minute ?",
       note:"Employer le nom de famille avec « monsieur » ou « madame » n’est pas distant : c’est la façon normale de nommer quelqu’un qu’on respecte et qu’on ne fréquente pas encore."},

      {t:'labo', h:"La même intention, deux façons",
       p:"Choisissez ce que vous voulez faire, et écoutez la version qui passe.",
       axes:[{id:'i', lbl:'Que voulez-vous faire ?', opts:[
         ['a','Engager la conversation'],
         ['b','Offrir de l’aide'],
         ['c','Refuser une invitation'],
         ['d','Demander un service']]}],
       out:{
         a:{w:['le voisinage'], say:"Il y a longtemps que vous habitez ici ? Moi, ça fait trois ans.", n:"une question partagée, et une information donnée en retour"},
         b:{w:['une corvée'], say:"Je peux vous aider à monter vos sacs, si vous voulez.", n:"une offre précise, facile à refuser"},
         c:{w:['un empêchement'], say:"Merci beaucoup, mais je travaille ce jour-là. On se reprend ?", n:"merci, refus, raison, contre-proposition"},
         d:{w:['arroser'], say:"Est-ce que je peux vous demander un service ? Ce n’est pas urgent.", n:"on annonce le service avant de le demander"},
       },
       note:"Dans les quatre cas, la phrase laisse à l’autre une porte de sortie. C’est ce qui distingue une demande de voisin d’une demande d’ami."},

      {t:'ex', h:"À écouter et à répéter",
       p:"Six phrases qui ouvrent une conversation d’escalier.",
       rows:[
         ["Bonjour monsieur Deslauriers, vous arrivez du travail ?","le nom, puis une question partagée"],
         ["Vous savez quand ils ramassent le bac brun ?","la question la plus utile des premiers mois"],
         ["Je peux vous aider à monter vos sacs ?","une offre précise, sans insistance"],
         ["Excusez-moi, vous êtes du deuxième, je pense ?","quand on ne connaît pas encore le nom"],
         ["On peut se tutoyer, si vous voulez.","la seule façon d’installer le tutoiement"],
         ["Si vous avez besoin de quelque chose, je suis au 2.","on donne son étage, pas son numéro de téléphone"],
       ]},

      {t:'piege', h:"Trois pièges de la conversation de voisinage",
       rows:[
         ["tutoyer d’emblée parce qu’on est du même âge","« Tu habites ici depuis longtemps ? » au premier bonjour",
          "Rien de grave, mais ça peut surprendre et forcer l’autre à vous suivre. Le vous ne vexe jamais ; le tu peut mettre mal à l’aise. Attendez qu’on vous le propose, ou proposez-le franchement."],
         ["poser une question personnelle en croyant s’intéresser","« Vous avez eu vos papiers ? » dit avec bienveillance",
          "L’intention est bonne, l’effet est mauvais : la personne doit soit mentir, soit raconter une chose difficile devant les boîtes aux lettres. Parlez de l’immeuble ; le reste viendra si elle le veut."],
         ["se justifier deux fois en refusant","« Je travaille, et puis mon fils est malade, et j’ai aussi… »",
          "Une raison suffit. Accumuler les raisons donne l’impression qu’aucune n’est vraie. Une phrase, puis une contre-proposition, puis on passe à autre chose."],
       ]},

      {t:'check', h:"Est-ce que c’est clair maintenant ?",
       p:"Quatre questions rapides.",
       qs:[
         {q:"Entre voisins d’un même immeuble, on se…", opts:["tutoie d’emblée","vouvoie tant que personne n’a proposé autre chose"], ok:1,
          fb:"On se vouvoie. Le tutoiement s’installe quand quelqu’un le propose à voix haute."},
         {q:"« Vous payez combien de loyer ? » est une question…", opts:["normale entre voisins","trop personnelle"], ok:1,
          fb:"Trop personnelle. L’argent, les papiers, la santé et la vie privée ne se demandent pas."},
         {q:"Appeler quelqu’un « madame Faye » est…", opts:["distant","la façon normale de nommer une voisine"], ok:1,
          fb:"C’est la façon normale. Le nom de famille avec madame ou monsieur marque le respect, pas la distance."},
         {q:"Pour refuser une invitation, combien de raisons faut-il donner ?", opts:["une","le plus possible"], ok:0,
          fb:"Une seule, en une phrase. Plusieurs raisons donnent l’impression qu’aucune n’est vraie."},
       ]},
    ]
  },

  // ════════════════════════════════════════════════════════════════════════
  t1acc: {
    eye:'Mini-leçon', tit:"Accepter, refuser, ou demander à réfléchir",
    blocs:[
      {t:'texte', h:"Trois réponses, et une seule à éviter",
       p:"Devant une invitation, il n’existe que trois réponses utiles : oui, non, ou « laissez-moi jusqu’à jeudi ». Toutes les trois sont polies et toutes les trois rendent service à celui qui organise. La quatrième — « peut-être », « on verra », « je vais essayer » — n’est pas une réponse : elle transfère le travail à l’autre, qui devra revenir vous chercher.",
       note:"C’est exactement ce que Réjean dit à Marisol dans l’escalier : « Répondez-moi, hein. Un peut-être, ça ne se met pas sur une liste. » Vingt-deux personnes l’an dernier, ça veut dire vingt-deux réponses claires à obtenir."},

      {t:'ana', h:"Accepter en trois temps",
       p:"Un oui seul est correct mais froid. La formule complète tient en trois mouvements, et elle prend cinq secondes.",
       mots:[["Le oui","C’est oui. · Volontiers. · Avec plaisir. · Comptez sur moi."],["Le plaisir ou le merci","Merci de m’avoir invitée. · Ça me fait bien plaisir.",true],["Ce que vous ferez","J’apporterai un plat. · Je serai là vers midi. · Je viendrai avec mes enfants."]],
       say:"C’est oui, avec plaisir. Merci de m’avoir invitée : j’apporterai un plat.",
       note:"Le troisième mouvement est celui qu’on oublie, et c’est le plus utile : il dit à l’organisateur ce qu’il peut inscrire sur sa liste."},

      {t:'ana', h:"Refuser en quatre temps",
       p:"L’ordre compte plus que les mots. Le merci vient avant le refus, sinon le refus arrive comme une porte qui claque.",
       mots:[["Le merci","Merci beaucoup de l’invitation. · C’est gentil d’avoir pensé à moi."],["Le refus, net","Je ne pourrai pas être là. · Malheureusement, je ne pourrai pas venir.",true],["La raison, une phrase","Je travaille ce jour-là. · Je reçois de la famille cette fin de semaine."],["La porte laissée ouverte","Si c’est reporté au dimanche, je serai libre. · On se reprend cet été ?"]],
       say:"Merci beaucoup de l’invitation. Malheureusement, je ne pourrai pas venir : je travaille ce jour-là. On se reprend cet été ?",
       note:"Madame Faye fait exactement ces quatre mouvements dans le dialogue du défi 1, et Réjean le remarque : « Elle a bien fait de me le dire tout de suite. »"},

      {t:'ana', h:"Demander à réfléchir, avec une date",
       p:"Un délai est une réponse, à condition qu’il porte une date. Sans date, ce n’est pas un délai, c’est un flou.",
       mots:[["La demande de délai","Est-ce que je peux vous répondre d’ici jeudi ?"],["L’engagement de rappel","Je vérifie mon horaire et je vous le dis demain sans faute.",true],["Ce qui n’est pas un délai","Je vais voir. · Peut-être. · Si j’ai le temps. · On verra bien."]],
       say:"Est-ce que je peux vous répondre d’ici jeudi ? Je vérifie mon horaire ce soir.",
       note:"Et tenez le délai. Une réponse donnée jeudi comme promis vaut mieux qu’un oui donné tout de suite et repris le vendredi."},

      {t:'labo', h:"La même invitation, trois réponses",
       p:"Réjean vous invite à la fête de la ruelle. Choisissez votre réponse.",
       axes:[{id:'r', lbl:'Que répondez-vous ?', opts:[
         ['a','Oui'],
         ['b','Non'],
         ['c','Non, mais…'],
         ['d','Laissez-moi réfléchir']]}],
       out:{
         a:{w:['une invitation'], say:"C’est oui, avec plaisir. J’apporterai un plat pour six personnes.", n:"oui, plaisir, et ce que vous ferez"},
         b:{w:['un empêchement'], say:"Merci beaucoup, mais je ne pourrai pas être là : je travaille ce jour-là.", n:"merci, refus, raison — trois mouvements"},
         c:{w:['reporter'], say:"Je ne pourrai pas venir le samedi. Par contre, si c’est reporté au dimanche, je serai libre.", n:"le refus qui laisse une porte ouverte"},
         d:{w:['une invitation'], say:"Est-ce que je peux vous répondre d’ici jeudi ? Je dois vérifier mon horaire.", n:"un délai avec une date, pas un « on verra »"},
       },
       note:"Les quatre réponses sont bonnes. La seule mauvaise est celle qui n’est pas dans la liste : « je vais essayer »."},

      {t:'ex', h:"À écouter et à répéter",
       p:"Six réponses complètes, prêtes à l’emploi.",
       rows:[
         ["C’est oui, avec plaisir. J’apporterai un dessert.","accepter, avec ce qu’on apporte"],
         ["Volontiers ! J’y serai vers midi et demi.","accepter, avec l’heure d’arrivée"],
         ["Merci beaucoup, mais je travaille ce samedi-là.","refuser, avec la raison"],
         ["C’est gentil, malheureusement je suis prise cette fin de semaine.","refuser poliment, sans détailler"],
         ["Je ne pourrai pas venir, mais on se reprend cet été ?","refuser en laissant la porte ouverte"],
         ["Est-ce que je peux vous répondre d’ici jeudi ?","un délai avec une date"],
       ]},

      {t:'piege', h:"Trois pièges de la réponse à une invitation",
       rows:[
         ["répondre « peut-être » pour être poli","« Peut-être, on verra bien »",
          "Dans beaucoup de cultures, un refus direct est impoli et « peut-être » veut dire non. Au Québec, « peut-être » veut dire « peut-être » : on vous inscrira sur la liste et on vous attendra. Un non clair est reçu comme une politesse, pas comme un rejet."],
         ["refuser sans remercier","« Non, je peux pas, je travaille. »",
          "Ce n’est pas le non qui blesse, c’est le merci qui manque. Une seconde de plus, et la même phrase devient chaleureuse : « Merci de l’invitation, mais je travaille ce jour-là. »"],
         ["accepter sans dire ce qu’on apporte","« Oui, oui, je vais être là. »",
          "L’organisateur doit alors vous relancer pour savoir s’il compte un plat de plus. Ajoutez toujours la troisième phrase : ce que vous apportez, ou l’heure à laquelle vous arrivez."],
       ]},

      {t:'check', h:"Est-ce que c’est clair maintenant ?",
       p:"Quatre questions rapides.",
       qs:[
         {q:"Dans un refus, le merci se dit…", opts:["avant le refus","après la raison"], ok:0,
          fb:"Avant. Le merci ouvre, le refus suit, la raison explique, la contre-proposition ferme."},
         {q:"« Je vais essayer » est…", opts:["une réponse claire","une réponse qui n’en est pas une"], ok:1,
          fb:"Ce n’est pas une réponse : l’organisateur devra revenir vous chercher."},
         {q:"Un délai est acceptable s’il…", opts:["porte une date","est court"], ok:0,
          fb:"S’il porte une date. « D’ici jeudi » est un délai ; « bientôt » n’en est pas un."},
         {q:"En acceptant, la troisième phrase dit…", opts:["pourquoi vous venez","ce que vous apporterez ou à quelle heure vous arrivez"], ok:1,
          fb:"Ce que vous ferez. C’est ce que l’organisateur inscrit sur sa liste."},
       ]},
    ]
  },

  // ════════════════════════════════════════════════════════════════════════
  t1just: {
    eye:'Mini-leçon', tit:"Dire pourquoi : parce que, comme, puisque, donc",
    blocs:[
      {t:'texte', h:"Une raison, quatre façons de l’attacher",
       p:"Au niveau 5, le programme ne demande plus seulement d’accepter ou de refuser : il demande de le faire <b>avec justification</b>. La difficulté n’est pas de trouver la raison — c’est de l’attacher correctement à la réponse. Quatre petits mots font ce travail, et ils ne se placent pas au même endroit dans la phrase. C’est leur place, plus que leur sens, qui les distingue.",
       note:"Retenez la géométrie avant le sens : <b>comme</b> et <b>puisque</b> ouvrent la phrase, <b>parce que</b> se met au milieu, <b>donc</b> annonce la conséquence. Si vous savez où ils vont, vous ne les confondrez plus."},

      {t:'ana', h:"parce que — la réponse d’abord, la raison ensuite",
       p:"Le plus courant, le plus sûr, celui qu’on peut employer dans presque tous les cas.",
       mots:[["Accepter","J’accepte avec plaisir, parce que ça fait trois ans que je ne connais personne."],["Refuser","Je ne peux pas venir parce que je travaille ce jour-là.",true],["Répondre à « pourquoi ? »","— Pourquoi elle ne vient pas ? — Parce qu’elle travaille de midi à minuit."]],
       say:"Je ne peux pas venir parce que je travaille ce jour-là.",
       note:"Une seule restriction : « parce que » ne commence pas une phrase, sauf quand il répond à la question « pourquoi ? ». C’est d’ailleurs son seul emploi en tête de phrase."},

      {t:'ana', h:"comme — la raison d’abord, la réponse ensuite",
       p:"<b>Comme</b> se met en tête de phrase et annonce la raison avant la réponse. Il prépare l’autre à ce qui vient.",
       mots:[["Devant un refus","Comme je travaille de midi à minuit, je ne pourrai pas venir."],["Devant une décision","Comme il pleut, on reporte la fête au dimanche.",true],["Ce qui est impossible","Je ne pourrai pas venir comme je travaille. ✗"]],
       say:"Comme je travaille de midi à minuit, je ne pourrai pas venir.",
       note:"« Comme » ne va jamais au milieu d’une phrase. C’est l’erreur la plus fréquente, parce que dans beaucoup de langues le mot équivalent, lui, peut s’y mettre."},

      {t:'ana', h:"puisque — la raison que l’autre connaît déjà",
       p:"<b>Puisque</b> s’emploie quand la raison est connue des deux personnes. Il dit : « nous savons tous les deux que… ».",
       mots:[["Une raison partagée","Puisque vous finissez à trois heures maintenant, passez donc prendre un café."],["Un fait visible","Puisqu’il pleut, on reporte au dimanche.",true],["Ce qui sonne mal","Puisque je pars au Sénégal, je ne peux pas venir. (si l’autre l’ignore)"]],
       say:"Puisque vous finissez à trois heures maintenant, passez donc prendre un café.",
       note:"Employé avec une raison que l’autre ignore, « puisque » sonne comme un reproche : vous avez l’air de dire « vous devriez le savoir »."},

      {t:'ana', h:"donc — la conséquence, pas la raison",
       p:"<b>Donc</b> travaille dans l’autre sens : la raison a déjà été donnée, il annonce ce qui en découle.",
       mots:[["Après une raison","Je travaille ce samedi-là, donc je ne pourrai pas être là."],["Après un calcul","Le plat est pour vingt personnes, donc j’ai besoin de deux plaques.",true],["À l’oral, en tête de phrase","Donc, on se voit dimanche ? (récapituler)"]],
       say:"Je travaille ce samedi-là, donc je ne pourrai pas être là.",
       note:"Un test simple : remplacez par « c’est pourquoi ». Si la phrase tient, c’est bien « donc » qu’il fallait."},

      {t:'labo', h:"La même raison, quatre attaches",
       p:"Choisissez le mot, et écoutez comment la phrase se réorganise autour de lui.",
       axes:[{id:'m', lbl:'Quel mot ?', opts:[
         ['a','parce que'],
         ['b','comme'],
         ['c','puisque'],
         ['d','donc'],
         ['e','c’est que']]}],
       out:{
         a:{w:['un empêchement'], say:"Je ne pourrai pas venir parce que je travaille ce jour-là.", n:"réponse, puis raison"},
         b:{w:['un empêchement'], say:"Comme je travaille ce jour-là, je ne pourrai pas venir.", n:"raison en tête, puis réponse"},
         c:{w:['reporter'], say:"Puisqu’il pleut, on reporte la fête au dimanche.", n:"la raison, tout le monde la voit déjà"},
         d:{w:['un empêchement'], say:"Je travaille ce jour-là, donc je ne pourrai pas venir.", n:"raison, puis conséquence"},
         e:{w:['un empêchement'], say:"Je ne pourrai pas venir : c’est que je travaille de nuit cette semaine-là.", n:"tournure parlée, qui annonce l’explication"},
       },
       note:"Les cinq phrases disent la même chose. Choisissez selon l’endroit où vous voulez mettre la raison : avant, après, ou annoncée."},

      {t:'ex', h:"À écouter et à répéter",
       p:"Six phrases du module, avec leur attache.",
       rows:[
         ["J’accepte avec plaisir, parce que ça fait trois ans que je ne connais personne.","la raison la plus vraie du module"],
         ["Comme je travaille de midi à minuit, je ne pourrai pas venir.","raison en tête : le refus s’annonce"],
         ["Puisqu’il pleut, on reporte au dimanche.","tout le monde voit qu’il pleut"],
         ["Le plat est pour vingt personnes, donc j’ai besoin de deux plaques.","une conséquence, pas une raison"],
         ["Je ne peux pas venir : c’est que je pars au Sénégal ce jour-là.","l’explication s’annonce"],
         ["Elle a refusé parce qu’elle avait déjà un empêchement.","raison rapportée, au passé"],
       ]},

      {t:'piege', h:"Trois pièges des mots de justification",
       rows:[
         ["mettre « comme » au milieu de la phrase","« Je ne pourrai pas venir comme je travaille »",
          "Impossible en français. « Comme » ouvre la phrase : « Comme je travaille, je ne pourrai pas venir. » Au milieu, il faut « parce que »."],
         ["commencer une phrase par « parce que » hors réponse","« Parce que je travaille, je ne viens pas. »",
          "On l’entend, mais ce n’est pas soigné. « Parce que » en tête de phrase sert à répondre à « pourquoi ? ». Sinon, employez « comme »."],
         ["employer « puisque » pour une raison inconnue de l’autre","« Puisque je pars au Sénégal… » dit à quelqu’un qui l’ignore",
          "« Puisque » suppose une raison partagée. Si l’autre ne la connaît pas, vous avez l’air de lui reprocher son ignorance. Employez « parce que » ou « comme »."],
       ]},

      {t:'check', h:"Est-ce que c’est clair maintenant ?",
       p:"Quatre questions rapides.",
       qs:[
         {q:"« Comme » se place…", opts:["en tête de phrase","au milieu"], ok:0,
          fb:"En tête, toujours. Au milieu, c’est « parce que »."},
         {q:"« Puisque » s’emploie quand la raison est…", opts:["nouvelle pour l’autre","déjà connue des deux"], ok:1,
          fb:"Déjà connue. Sinon, il sonne comme un reproche."},
         {q:"« Donc » annonce…", opts:["la raison","la conséquence"], ok:1,
          fb:"La conséquence. Test : remplacez par « c’est pourquoi »."},
         {q:"« Parce que » peut ouvrir une phrase…", opts:["pour répondre à « pourquoi ? »","jamais"], ok:0,
          fb:"Oui, pour répondre à « pourquoi ? ». C’est son seul emploi en tête de phrase."},
       ]},
    ]
  },

  // ════════════════════════════════════════════════════════════════════════
  t1fut: {
    eye:'Mini-leçon', tit:"Le futur simple : la promesse qu’on tient",
    blocs:[
      {t:'texte', h:"Pourquoi le futur, dans un module sur les invitations",
       p:"Accepter une invitation, c’est promettre quelque chose : d’être là, d’apporter un plat, de répondre avant jeudi. Le futur simple est le temps de ces promesses. Il ne remplace pas le futur proche — « je vais apporter un dessert » est parfaitement correct — mais il est plus net, et il est le temps normal de l’écrit : un courriel de réponse à une invitation s’écrit au futur simple.",
       note:"C’est aussi le temps du message téléphonique du défi 2 : « je vous rappellerai », « je passerai vers midi ». Un répondeur ne discute pas : ce qu’on y dit doit être une promesse claire."},

      {t:'ana', h:"La formation : l’infinitif, plus six terminaisons",
       p:"Le futur simple est le temps le plus régulier du français. On part de l’infinitif entier, on ajoute les terminaisons — qui sont celles du verbe <b>avoir</b> au présent.",
       mots:[["Verbes en -er et -ir","apporter → j’apporterai · finir → je finirai · sortir → je sortirai"],["Verbes en -re : le e tombe","répondre → je répondrai · prendre → je prendrai · écrire → j’écrirai",true],["Les six terminaisons","-ai · -as · -a · -ons · -ez · -ont"]],
       say:"J’apporterai un plat, je finirai vers quatre heures et je vous répondrai jeudi.",
       note:"Un repère utile : à toutes les personnes, on entend le <b>r</b> avant la terminaison. Si vous n’entendez pas ce r, vous n’êtes pas au futur."},

      {t:'ana', h:"Les huit irréguliers des invitations",
       p:"Huit verbes changent de radical, et ce sont précisément les huit dont on a besoin pour répondre à une invitation.",
       mots:[["Être, avoir, aller, faire","je serai · j’aurai · j’irai · je ferai"],["Venir, pouvoir, vouloir, devoir","je viendrai · je pourrai · je voudrai · je devrai",true],["Dans une phrase","Je serai là vers midi ; je pourrai rester jusqu’à trois heures."]],
       say:"Je serai là vers midi, j’apporterai un plat et je pourrai rester jusqu’à trois heures.",
       note:"Les terminaisons, elles, ne changent jamais : seul le radical est irrégulier. Apprenez les huit radicaux une fois, et le reste suit."},

      {t:'ana', h:"Après « quand » et « dès que », le futur reste au futur",
       p:"C’est le point qui surprend le plus, parce que beaucoup de langues mettent le présent à cet endroit.",
       mots:[["Avec quand","Je vous préviendrai quand je saurai mon horaire."],["Avec dès que","Dès qu’il fera beau, on sortira les tables.",true],["Ce qu’on ne dit pas","Je vous préviendrai quand je sais mon horaire. ✗"]],
       say:"Je vous préviendrai quand je saurai mon horaire.",
       note:"Retenez la phrase entière plutôt que la règle : « quand je saurai », « dès qu’il fera beau », « quand vous arriverez ». Trois modèles suffisent."},

      {t:'labo', h:"La même promesse, deux temps",
       p:"Choisissez ce que vous promettez, et comparez le futur proche et le futur simple.",
       axes:[{id:'p', lbl:'Que promettez-vous ?', opts:[
         ['a','Apporter un plat'],
         ['b','Être là à midi'],
         ['c','Répondre jeudi'],
         ['d','Prévenir quand vous saurez']]}],
       out:{
         a:{w:['un plat à partager'], say:"Je vais apporter un plat. J’apporterai un plat pour six personnes.", n:"le second est plus net, et c’est celui qui s’écrit"},
         b:{w:['une invitation'], say:"Je vais être là vers midi. Je serai là vers midi.", n:"être → je serai : le premier irrégulier à retenir"},
         c:{w:['une invitation'], say:"Je vais vous répondre jeudi. Je vous répondrai jeudi.", n:"répondre perd son e : je répondrai"},
         d:{w:['prévenir'], say:"Je vous préviendrai quand je saurai mon horaire.", n:"après « quand », le futur reste au futur"},
       },
       note:"Les deux formes sont correctes à l’oral. À l’écrit, et dans un message qu’on laisse, préférez le futur simple."},

      {t:'ex', h:"À écouter et à répéter",
       p:"Six promesses tirées du module.",
       rows:[
         ["J’apporterai un plat pour six personnes.","le verbe le plus utile de la fête"],
         ["Je serai là vers midi et demi.","être : je serai"],
         ["Nous sortirons les tables à onze heures.","nous : -ons, après le r"],
         ["Il fera le tour des portes le matin même.","faire : il fera"],
         ["Je vous répondrai d’ici jeudi, sans faute.","répondre perd son e"],
         ["Dès qu’il fera beau, on installera tout dehors.","après « dès que », le futur reste"],
       ]},

      {t:'piege', h:"Trois pièges du futur simple",
       rows:[
         ["oublier le r","« je répondai » au lieu de « je répondrai »",
          "Le r est la marque du futur, à toutes les personnes. Sans lui, on entend un passé simple ou rien du tout. Dites lentement : ré-pon-<b>d-r</b>-ai."],
         ["mettre le présent après « quand »","« quand je sais mon horaire »",
          "En français, si l’action est à venir, « quand » est suivi du futur : « quand je saurai mon horaire ». Beaucoup de langues font l’inverse, d’où l’erreur."],
         ["confondre j’aurai et j’irai","« j’aurai à la fête » pour « j’irai à la fête »",
          "avoir → j’aurai ; aller → j’irai. Deux radicaux très proches à l’oreille, deux verbes très différents. On <b>ira</b> à la fête ; on <b>aura</b> du plaisir."],
       ]},

      {t:'check', h:"Est-ce que c’est clair maintenant ?",
       p:"Quatre questions rapides.",
       qs:[
         {q:"Le futur simple se forme sur…", opts:["l’infinitif","le participe passé"], ok:0,
          fb:"Sur l’infinitif entier, plus les terminaisons -ai, -as, -a, -ons, -ez, -ont."},
         {q:"« venir » au futur donne…", opts:["je venirai","je viendrai"], ok:1,
          fb:"Je viendrai. C’est l’un des huit irréguliers à savoir par cœur."},
         {q:"Après « quand », pour une action à venir, on met…", opts:["le présent","le futur"], ok:1,
          fb:"Le futur : « quand je saurai », « quand vous arriverez »."},
         {q:"Dans un courriel de réponse à une invitation, on emploie plutôt…", opts:["le futur proche","le futur simple"], ok:1,
          fb:"Le futur simple : c’est le temps de l’écrit et des engagements."},
       ]},
    ]
  },

  // ════════════════════════════════════════════════════════════════════════
  t2acc: {
    eye:'Mini-leçon', tit:"Le répondeur de la maison n’est pas celui du bureau",
    blocs:[
      {t:'texte', h:"Deux répondeurs, deux métiers",
       p:"Au travail, votre message d’accueil parle au nom de votre employeur : il nomme l’organisation, votre service, une autre ressource pour ce qui presse, et il ne dit jamais pourquoi vous êtes absent. Chez vous, c’est l’inverse : le message est court, il ne nomme presque rien, et sa qualité se mesure à ce qu’il ne dit pas. Un message d’accueil personnel s’écoute par n’importe qui — y compris par quelqu’un qui compose au hasard.",
       note:"C’est la seule chose que ce module et le module « Le travail par écrit » ont en commun, et ils s’en servent en sens contraire. Si vous avez fait l’autre module, désapprenez la moitié de ce que vous y avez appris quand vous enregistrez chez vous."},

      {t:'ana', h:"Les quatre éléments d’un message personnel",
       p:"Quinze à vingt secondes, quatre phrases. Il n’en faut pas davantage.",
       mots:[["Le repère","Bonjour, vous avez bien rejoint le 514 555-0112."],["L’absence, sans raison","Je ne peux pas vous répondre pour le moment.",true],["La demande","Laissez-moi un message et je vous rappellerai."],["Le merci","Merci, et bonne journée."]],
       say:"Bonjour, vous avez bien rejoint le 514 555-0112. Je ne peux pas vous répondre pour le moment. Laissez-moi un message et je vous rappellerai. Merci.",
       note:"Le numéro plutôt que le nom, si vous préférez : « vous avez bien rejoint le 514 555-0112 » suffit à rassurer celui qui appelle et ne donne rien à celui qui cherche."},

      {t:'ana', h:"Ce qu’on ne met jamais",
       p:"Chacun de ces éléments a déjà servi à quelqu’un de mal intentionné, et aucun ne rend service à celui qui appelle.",
       mots:[["Votre adresse","…au 7412, rue De Normanville, logement 2. ✗"],["Votre absence datée","Je suis en voyage jusqu’au 20 juillet. ✗",true],["Vos horaires","Je travaille de nuit du lundi au jeudi. ✗"],["Les enfants","Ici la famille Vergara, Marisol, Diego et les petits. ✗"]],
       say:"Je suis en voyage jusqu’au 20 juillet.",
       note:"Dire qu’on est en voyage sur son répondeur revient à afficher les dates de son absence sur la porte. Si vous partez, dites-le aux personnes concernées — comme Ndeye Faye le fait dans son message : à une voisine, pas à tout le monde."},

      {t:'ana', h:"Laisser un message, maintenant : cinq mouvements",
       p:"Enregistrer son propre message et en laisser un chez quelqu’un d’autre sont deux exercices différents. Le second est plus difficile, parce que le répondeur ne fait pas répéter.",
       mots:[["Qui, et d’où","Bonsoir madame Vergara, c’est Ndeye Faye, du troisième."],["Pourquoi, en une phrase","Je voulais vous dire deux choses.",true],["Les faits, lentement","Je pars du 10 au 20 juillet."],["Ce que vous attendez","Rappelez-moi si ça vous intéresse."],["Comment et quand vous joindre","Au 514 555-0148, après trois heures. Pas avant, je dors."]],
       say:"Bonsoir madame Vergara, c’est Ndeye Faye, du troisième. Rappelez-moi au 514 555-0148, après trois heures de l’après-midi.",
       note:"Le cinquième mouvement est celui qu’on oublie le plus. Sans le moment, on vous rappelle à huit heures du matin ; sans le numéro, on ne vous rappelle pas du tout."},

      {t:'labo', h:"Écoutez la différence",
       p:"Le même besoin, dit de deux façons.",
       axes:[{id:'v', lbl:'Quelle version ?', opts:[
         ['a','Message d’accueil : au bureau'],
         ['b','Message d’accueil : à la maison'],
         ['c','Message laissé : trop court'],
         ['d','Message laissé : complet']]}],
       out:{
         a:{w:['un répondeur'], say:"Vous êtes bien à la Coopérative d’aide à domicile. Je ne suis pas disponible ; pour une urgence, faites le poste onze.", n:"l’organisation d’abord, une autre ressource ensuite"},
         b:{w:['un répondeur'], say:"Bonjour, vous avez bien rejoint le 514 555-0112. Laissez-moi un message et je vous rappellerai.", n:"quatre phrases, aucune information personnelle"},
         c:{w:['un mot'], say:"Bonjour, c’est moi, rappelle-moi.", n:"ni nom, ni raison, ni numéro : ce message ne produira rien"},
         d:{w:['prévenir'], say:"Bonsoir madame Vergara, c’est Ndeye Faye, du troisième. Je cherche quelqu’un pour arroser mes plantes du 10 au 20 juillet. Rappelez-moi au 514 555-0148, après trois heures.", n:"qui, pourquoi, les dates, la demande, le numéro et le moment"},
       },
       note:"Écoutez le troisième deux fois : c’est le message que tout le monde laisse quand il est pressé, et c’est celui qui oblige à rappeler trois fois."},

      {t:'ex', h:"À écouter et à répéter",
       p:"Six phrases de répondeur.",
       rows:[
         ["Bonjour, vous avez bien rejoint le 514 555-0112.","le repère, sans le nom si vous préférez"],
         ["Je ne peux pas vous répondre pour le moment.","l’absence, sans jamais dire pourquoi"],
         ["Laissez-moi un message et je vous rappellerai.","futur simple : c’est une promesse"],
         ["Bonsoir madame Vergara, c’est Ndeye Faye, du troisième.","qui parle, et d’où : la première phrase"],
         ["Je voulais vous dire deux choses.","on annonce le nombre : l’autre prend un crayon"],
         ["Rappelez-moi après trois heures, pas avant, je dors.","le moment, sans lequel on vous réveille"],
       ]},

      {t:'piege', h:"Trois pièges du répondeur",
       rows:[
         ["dire « c’est moi »","« Allô, c’est moi, rappelle-moi »",
          "Sur un répondeur, personne n’est « moi ». Donnez votre nom au complet et un repère : « c’est Ndeye Faye, du troisième ». Même à quelqu’un que vous connaissez bien."],
         ["annoncer son voyage sur son message d’accueil","« Je suis à l’extérieur jusqu’au 20 juillet »",
          "C’est l’équivalent d’un mot sur la porte. Prévenez les gens concernés directement, et laissez votre message d’accueil habituel pendant votre absence."],
         ["donner le numéro trop vite, à la fin","« …au 514 555-0148 merci bonne journée » d’un trait",
          "Le numéro est la seule partie du message qu’il faut ralentir. Dites-le deux fois si vous n’êtes pas certain d’avoir été clair : c’est vingt secondes de plus, et un rappel de gagné."],
       ]},

      {t:'check', h:"Est-ce que c’est clair maintenant ?",
       p:"Quatre questions rapides.",
       qs:[
         {q:"Sur son message d’accueil personnel, on donne…", opts:["son adresse","son numéro ou son nom, rien de plus"], ok:1,
          fb:"Le numéro ou le nom. Jamais l’adresse, les horaires ou les dates d’absence."},
         {q:"Un message d’accueil personnel dure…", opts:["quinze à vingt secondes","une minute"], ok:0,
          fb:"Quinze à vingt secondes. Au-delà, on raccroche."},
         {q:"En laissant un message, la première phrase donne…", opts:["la raison de l’appel","qui vous êtes et d’où"], ok:1,
          fb:"Qui vous êtes, avec un repère. La raison vient dans la deuxième phrase."},
         {q:"Le numéro se donne…", opts:["au début, rapidement","à la fin, lentement, avec le moment où l’on peut vous joindre"], ok:1,
          fb:"À la fin et lentement, suivi du moment. Sans le moment, on vous rappelle pendant que vous dormez."},
       ]},
    ]
  },

  // ════════════════════════════════════════════════════════════════════════
  t2pron: {
    eye:'Mini-leçon', tit:"Ne pas tout répéter : le, lui, y, en",
    blocs:[
      {t:'texte', h:"Pourquoi ces mots-là arrivent au niveau 5",
       p:"Au début, on répète : « J’ai appelé madame Faye. J’ai laissé un message à madame Faye. Je vais rappeler madame Faye. » C’est clair, mais ce n’est plus du français au bout de trois phrases. Le programme du niveau 5 appelle ça la <b>reprise de l’information</b> : remplacer ce qui a déjà été dit par un petit mot, pour que la phrase suivante avance au lieu de piétiner.",
       note:"C’est aussi ce qui rend un message téléphonique écoutable. Un message qui répète trois fois le même nom dure deux fois plus longtemps et se comprend moins bien."},

      {t:'ana', h:"le, la, les — sans préposition",
       p:"Ils remplacent un complément qui suit directement le verbe : on <b>écoute</b> quelque chose, on <b>appelle</b> quelqu’un, on <b>arrose</b> des plantes.",
       mots:[["Une chose","J’écoute le message → Je l’écoute."],["Une personne","J’appelle madame Faye → Je l’appelle.",true],["Un pluriel","J’arrose les plantes → Je les arrose."]],
       say:"J’écoute le message. Je l’écoute. J’arrose les plantes. Je les arrose.",
       note:"Devant une voyelle, <b>le</b> et <b>la</b> deviennent <b>l’</b> : je l’écoute, je l’appelle. Au pluriel, <b>les</b> ne change jamais."},

      {t:'ana', h:"lui, leur — la personne annoncée par « à »",
       p:"On <b>parle à</b> quelqu’un, on <b>écrit à</b> quelqu’un, on <b>laisse un message à</b> quelqu’un, on <b>répond à</b> quelqu’un.",
       mots:[["Une personne","Je laisse un message à Ndeye → Je lui laisse un message."],["Homme ou femme, c’est pareil","Je réponds à Réjean → Je lui réponds.",true],["Plusieurs personnes","J’écris aux voisins → Je leur écris."]],
       say:"Je lui laisse un message. Je leur écris à tous les deux.",
       note:"<b>Leur</b> pronom ne prend jamais de s : « je leur écris ». Le <b>leurs</b> avec un s est un déterminant : « leurs enfants ». Deux mots différents qui s’écrivent presque pareil."},

      {t:'ana', h:"y et en — le lieu, la quantité, la préposition",
       p:"<b>Y</b> remplace ce qui est annoncé par <b>à</b> quand il ne s’agit pas d’une personne, et tous les lieux. <b>En</b> remplace ce qui est annoncé par <b>de</b>, et les quantités.",
       mots:[["y : un lieu","Je vais à la fête → J’y vais."],["y : une chose avec « à »","Je pense à son départ → J’y pense.",true],["en : une quantité","Je fais des empanadas → J’en fais."],["en : avec un nombre","J’ai besoin de deux plaques → J’en ai besoin de deux."]],
       say:"J’y vais samedi. J’en fais vingt, comme l’année passée.",
       note:"Avec un nombre, le nombre reste après le verbe : « j’en fais vingt », « j’en ai besoin de deux ». C’est ce qui surprend le plus la première fois."},

      {t:'ana', h:"Où ils se placent",
       p:"Devant le verbe, toujours. Une seule exception : l’impératif affirmatif, où ils passent derrière avec un trait d’union.",
       mots:[["Présent","Je lui téléphone. · Je les arrose."],["Avec deux verbes","Je vais lui téléphoner. · Je dois les arroser.",true],["Impératif affirmatif","Téléphone-lui ! · Rappelez-moi !"],["Impératif négatif","Ne lui téléphone pas. · Ne les arrose pas."]],
       say:"Je vais lui téléphoner ce soir. Rappelez-moi après trois heures.",
       note:"« Rappelez-moi » et « ne me rappelez pas » : le pronom saute d’un côté à l’autre du verbe selon que l’ordre est positif ou négatif. Retenez les deux phrases ensemble."},

      {t:'labo', h:"La phrase avec, et la phrase sans",
       p:"Choisissez une phrase du module et écoutez-la se raccourcir.",
       axes:[{id:'p', lbl:'Quelle phrase ?', opts:[
         ['a','Écouter le message'],
         ['b','Laisser un message à madame Faye'],
         ['c','Aller à la fête'],
         ['d','Faire des empanadas'],
         ['e','Arroser les plantes']]}],
       out:{
         a:{w:['un répondeur'], say:"J’écoute le message. Je l’écoute deux fois.", n:"le message : complément direct, donc « le »"},
         b:{w:['un mot'], say:"Je laisse un message à madame Faye. Je lui laisse un message.", n:"à quelqu’un : donc « lui »"},
         c:{w:['une invitation'], say:"Je vais à la fête de la ruelle. J’y vais avec un plat.", n:"un lieu : donc « y »"},
         d:{w:['un plat à partager'], say:"Je fais des empanadas. J’en fais vingt.", n:"une quantité : donc « en », et le nombre reste"},
         e:{w:['arroser'], say:"J’arrose les plantes du troisième. Je les arrose deux fois par semaine.", n:"les plantes : complément direct pluriel, donc « les »"},
       },
       note:"Le test le plus rapide : regardez s’il y a une préposition avant le complément. Pas de préposition → le, la, les. « à » + personne → lui, leur. « à » + chose ou lieu → y. « de » ou une quantité → en."},

      {t:'ex', h:"À écouter et à répéter",
       p:"Six phrases du module, avant et après.",
       rows:[
         ["J’écoute le message. Je l’écoute.","complément direct"],
         ["Je laisse un message à Ndeye. Je lui laisse un message.","à + personne"],
         ["J’écris aux voisins. Je leur écris.","à + plusieurs personnes"],
         ["Je vais à la fête. J’y vais.","un lieu"],
         ["Je fais des empanadas. J’en fais.","une quantité"],
         ["Rappelez-moi après trois heures.","impératif : le pronom passe derrière"],
       ]},

      {t:'piege', h:"Trois pièges des pronoms",
       rows:[
         ["employer « y » pour une personne","« Je pense à ma sœur → j’y pense » ✗",
          "Pour une personne, on garde la préposition et le pronom fort : « je pense <b>à elle</b> ». « Y » ne remplace jamais une personne."],
         ["écrire « leurs » quand il s’agit du pronom","« Je leurs écris » ✗",
          "Le pronom <b>leur</b> ne prend jamais de s : « je leur écris ». Le <b>leurs</b> avec un s accompagne un nom : « leurs enfants »."],
         ["placer le pronom après le verbe hors impératif","« Je téléphone-lui » ✗",
          "Le pronom se met devant le verbe : « je lui téléphone ». Il ne passe derrière qu’à l’impératif affirmatif : « téléphone-lui ! »."],
       ]},

      {t:'check', h:"Est-ce que c’est clair maintenant ?",
       p:"Quatre questions rapides.",
       qs:[
         {q:"« Je laisse un message à Ndeye » devient…", opts:["Je la laisse un message","Je lui laisse un message"], ok:1,
          fb:"« à » + une personne → lui. Le complément direct reste : un message."},
         {q:"« Je vais à la fête » devient…", opts:["J’y vais","J’en vais"], ok:0,
          fb:"Un lieu → y. « En » sert pour « de » et pour les quantités."},
         {q:"« Je fais vingt empanadas » devient…", opts:["J’en fais vingt","Je les fais vingt"], ok:0,
          fb:"Une quantité → en, et le nombre reste après le verbe."},
         {q:"À l’impératif affirmatif, le pronom se place…", opts:["devant le verbe","derrière, avec un trait d’union"], ok:1,
          fb:"Derrière : « rappelez-moi ». Au négatif, il repasse devant : « ne me rappelez pas »."},
       ]},
    ]
  },

  // ════════════════════════════════════════════════════════════════════════
  t2rap: {
    eye:'Mini-leçon', tit:"D’un message entendu à un mot écrit",
    blocs:[
      {t:'texte', h:"Le seul exercice du module qui se fait deux fois",
       p:"Écouter un message, c’est une chose. Le redire à quelqu’un d’autre, c’en est une autre : il faut changer les personnes, changer l’ordre des mots dans les questions, jeter les bonjours et garder les chiffres. C’est ce que le programme appelle <b>rédiger un mot avec les notes prises en écoutant un message téléphonique</b>, et c’est l’intention la plus exigeante de toute la situation.",
       note:"Le test de Réjean, dans le dialogue, est le bon : « Si votre fils lit ce papier, est-ce qu’il comprend ? » Un mot s’écrit pour quelqu’un qui n’a pas entendu le message."},

      {t:'ana', h:"Une affirmation → « dit que »",
       p:"Le verbe change de personne. C’est là que se font presque toutes les erreurs.",
       mots:[["Ce qu’on entend","« Je ne peux pas venir à la fête. »"],["Ce qu’on écrit","Elle dit qu’elle ne peut pas venir à la fête.",true],["Autre exemple","« Je travaille de midi à minuit. » → Elle dit qu’elle travaille de midi à minuit."]],
       say:"Elle dit qu’elle ne peut pas venir à la fête.",
       note:"« Je » devient « elle » ou « il ». « Mon » devient « son ». « Chez moi » devient « chez elle ». Relisez toujours votre mot en cherchant les « je » oubliés."},

      {t:'ana', h:"Une question fermée → « demande si »",
       p:"Une question à laquelle on répond par oui ou par non se rapporte avec <b>si</b>. « Est-ce que » disparaît complètement.",
       mots:[["Ce qu’on entend","« Est-ce que vous êtes libre en juillet ? »"],["Ce qu’on écrit","Elle demande si vous êtes libre en juillet.",true],["Devant « il »","« Est-ce qu’il pleut ? » → Elle demande s’il pleut."]],
       say:"Elle demande si vous êtes libre en juillet.",
       note:"Devant <b>il</b> et <b>ils</b>, « si » devient <b>s’</b> : « s’il pleut », « s’ils viennent ». Devant « elle », il ne change pas : « si elle vient »."},

      {t:'ana', h:"Une question ouverte → le mot interrogatif reste",
       p:"Le mot qui pose la question — quand, où, qui, comment, pourquoi — se garde tel quel. Mais l’ordre redevient celui d’une phrase normale.",
       mots:[["Ce qu’on entend","« Quand est-ce que vous partez ? »"],["Ce qu’on écrit","Elle demande quand vous partez.",true],["Pas d’inversion","« Qui a la clé ? » → Elle demande qui a la clé."]],
       say:"Elle demande quand vous partez et qui a la clé.",
       note:"On n’écrit jamais « elle demande quand partez-vous ». L’inversion appartient à la question directe ; dans un mot rapporté, elle disparaît."},

      {t:'ana', h:"Un ordre ou une demande → « de » + infinitif",
       p:"L’impératif ne se rapporte pas tel quel : il devient un infinitif annoncé par <b>de</b>.",
       mots:[["Ce qu’on entend","« Rappelez-moi après trois heures. »"],["Ce qu’on écrit","Elle demande de la rappeler après trois heures.",true],["Au négatif","« N’appelez pas le matin. » → Elle demande de ne pas appeler le matin."]],
       say:"Elle demande de la rappeler après trois heures et de ne pas appeler le matin.",
       note:"Au négatif, <b>ne pas</b> reste collé devant l’infinitif : « de ne pas appeler », jamais « de n’appeler pas »."},

      {t:'labo', h:"Le message, puis le mot",
       p:"Choisissez une phrase du message de madame Faye et voyez ce qu’elle devient sur le papier.",
       axes:[{id:'r', lbl:'Quelle phrase du message ?', opts:[
         ['a','Je ne peux pas venir'],
         ['b','Est-ce que vous êtes libre'],
         ['c','Quand partez-vous'],
         ['d','Rappelez-moi après trois heures'],
         ['e','Le mot au complet']]}],
       out:{
         a:{w:['un mot'], say:"Elle dit qu’elle ne peut pas venir à la fête du 7 juin.", n:"« je » devient « elle »"},
         b:{w:['un mot'], say:"Elle demande si vous êtes libre du 10 au 20 juillet.", n:"« est-ce que » disparaît, « si » le remplace"},
         c:{w:['prévenir'], say:"Elle demande quand vous partez en vacances.", n:"le mot interrogatif reste, l’inversion tombe"},
         d:{w:['prévenir'], say:"Elle demande de la rappeler après trois heures de l’après-midi.", n:"l’impératif devient « de » + infinitif"},
         e:{w:['un mot'], say:"Ndeye Faye, du 3e, a appelé mardi soir. Elle dit qu’elle ne peut pas venir à la fête. Elle demande si vous pouvez arroser ses plantes du 10 au 20 juillet, et de la rappeler au 514 555-0148 après quinze heures.", n:"trois phrases, et tout y est"},
       },
       note:"Écoutez la dernière : c’est le mot complet, celui qu’un autre que vous peut lire et exécuter sans rappeler personne."},

      {t:'ex', h:"À écouter et à répéter",
       p:"Six transformations, dites l’une après l’autre.",
       rows:[
         ["Elle dit qu’elle ne peut pas venir.","affirmation rapportée"],
         ["Elle dit qu’elle travaille de midi à minuit.","le « je » a disparu"],
         ["Elle demande si vous êtes libre en juillet.","question fermée"],
         ["Elle demande s’il pleut chez nous.","« si » devient « s’ » devant il"],
         ["Elle demande quand vous partez.","question ouverte, sans inversion"],
         ["Elle demande de ne pas appeler le matin.","ordre négatif rapporté"],
       ]},

      {t:'piege', h:"Trois pièges du discours rapporté",
       rows:[
         ["garder « est-ce que »","« Elle demande est-ce que vous êtes libre » ✗",
          "« Est-ce que » n’existe que dans la question directe. Rapporté, il devient <b>si</b> : « elle demande si vous êtes libre »."],
         ["garder l’inversion","« Elle demande quand partez-vous » ✗",
          "Après « elle demande », on écrit une phrase normale : sujet, verbe. « Elle demande quand vous partez »."],
         ["oublier de changer la personne","« Elle dit que je ne peux pas venir » ✗",
          "Ce n’est plus elle qui parle, c’est vous qui rapportez. « Je » devient « elle » : « elle dit qu’elle ne peut pas venir ». Relisez en cherchant les « je »."],
       ]},

      {t:'check', h:"Est-ce que c’est clair maintenant ?",
       p:"Quatre questions rapides.",
       qs:[
         {q:"« Est-ce que vous venez ? » rapporté donne…", opts:["Elle demande si vous venez","Elle demande est-ce que vous venez"], ok:0,
          fb:"« Est-ce que » devient « si » dans une question fermée rapportée."},
         {q:"« Quand partez-vous ? » rapporté donne…", opts:["Elle demande quand partez-vous","Elle demande quand vous partez"], ok:1,
          fb:"Le mot interrogatif reste, l’inversion disparaît."},
         {q:"« Rappelez-moi » rapporté donne…", opts:["Elle demande de la rappeler","Elle demande qu’elle rappelle"], ok:0,
          fb:"Un ordre devient « de » + infinitif."},
         {q:"Dans un mot rapporté, « je » devient…", opts:["« je »","« elle » ou « il »"], ok:1,
          fb:"La personne change, parce que ce n’est plus elle qui parle."},
       ]},
    ]
  },

  // ════════════════════════════════════════════════════════════════════════
  t3pc: {
    eye:'Mini-leçon', tit:"Raconter : ce qui est arrivé, ce qui était là",
    blocs:[
      {t:'texte', h:"Deux temps, deux rôles — pas deux niveaux de difficulté",
       p:"Beaucoup d’élèves croient que l’imparfait est « plus difficile » que le passé composé, ou qu’il vient « après ». Ce n’est pas ça du tout : les deux temps racontent la même histoire, mais ils n’y font pas le même travail. Le passé composé fait avancer le récit ; l’imparfait plante le décor autour. Une nouvelle racontée entièrement au passé composé est une liste ; racontée entièrement à l’imparfait, elle ne commence jamais.",
       note:"C’est l’outil dont vous avez besoin pour l’intention « donner des nouvelles » : trois phrases au passé composé pour ce qui est arrivé, une ou deux à l’imparfait pour dire comment c’était."},

      {t:'ana', h:"Le passé composé fait avancer",
       p:"Un événement, à un moment précis, qu’on pourrait numéroter dans l’histoire.",
       mots:[["Les étapes","J’ai eu ma citoyenneté mercredi. · J’ai pris trois jours de congé."],["Ce qui arrive une fois","On a chanté à la fin. · Elle a pleuré un peu.",true],["Les marqueurs","hier · mercredi dernier · une fois · tout à coup · en 2019"]],
       say:"J’ai eu ma citoyenneté mercredi dernier et j’ai pris trois jours de congé.",
       note:"Chaque fois que quelqu’un pourrait vous demander « et ensuite ? », vous êtes au passé composé."},

      {t:'ana', h:"L’imparfait plante le décor",
       p:"Ce qu’il y avait autour : les lieux, les gens, le temps qu’il faisait, ce qu’on ressentait. Rien n’avance pendant un imparfait.",
       mots:[["Le lieu et les gens","On était deux cents dans la salle. · Il y avait des drapeaux partout."],["L’apparence","Mon fils portait sa chemise blanche.",true],["L’habitude d’avant","Avant, elle travaillait toujours de nuit."],["Les marqueurs","avant · à l’époque · chaque année · tous les jours · pendant que"]],
       say:"On était deux cents dans la salle, et il y avait des drapeaux partout.",
       note:"Chaque fois que quelqu’un pourrait demander « c’était comment ? », vous êtes à l’imparfait."},

      {t:'ana', h:"Les deux dans la même phrase",
       p:"C’est le cas le plus fréquent, et le plus utile : un décor à l’imparfait, puis un événement au passé composé qui arrive dedans.",
       mots:[["Décor, puis événement","Je ne m’y attendais pas quand ils ont commencé à chanter."],["Météo, puis décision","Il pleuvait, donc on a reporté la fête au dimanche.",true],["Situation, puis rupture","Elle travaillait de nuit depuis six ans quand elle a changé d’horaire."]],
       say:"Il pleuvait, donc on a reporté la fête au dimanche.",
       note:"Une bonne nouvelle se raconte presque toujours ainsi : la situation d’avant à l’imparfait, le moment qui change tout au passé composé."},

      {t:'ana', h:"L’accord du participe passé, en deux lignes",
       p:"Avec <b>être</b>, le participe s’accorde avec le sujet. Avec <b>avoir</b>, il ne s’accorde pas avec le sujet.",
       mots:[["Avec être","Je suis allée à la fête. · Elles sont venues ensemble."],["Avec avoir","J’ai apporté un plat. · Elles ont chanté.",true],["Les verbes qui prennent être","aller, venir, arriver, partir, entrer, sortir, monter, descendre, rester, tomber, naître, mourir, et les verbes en se-"]],
       say:"Je suis allée à la fête et j’ai apporté un plat.",
       note:"Au féminin, l’accord avec « être » s’entend rarement — « allé » et « allée » se disent pareil — mais il se voit dans un courriel. C’est là qu’il compte."},

      {t:'labo', h:"La même nouvelle, racontée",
       p:"Choisissez une phrase et écoutez ce que chaque temps y fait.",
       axes:[{id:'t', lbl:'Quelle phrase ?', opts:[
         ['a','L’événement'],
         ['b','Le décor'],
         ['c','Les deux ensemble'],
         ['d','L’habitude d’avant'],
         ['e','La nouvelle au complet']]}],
       out:{
         a:{w:['la citoyenneté'], say:"J’ai eu ma citoyenneté mercredi dernier.", n:"passé composé : un fait, une date"},
         b:{w:['une cérémonie'], say:"On était deux cents dans une grande salle, avec des drapeaux partout.", n:"imparfait : rien n’avance, tout se décrit"},
         c:{w:['une cérémonie'], say:"Je ne m’y attendais pas quand ils ont commencé à chanter.", n:"décor à l’imparfait, événement au passé composé"},
         d:{w:['la citoyenneté'], say:"Avant, je travaillais toujours de nuit.", n:"imparfait d’habitude : ce qui se répétait"},
         e:{w:['fêter'], say:"J’ai eu ma citoyenneté mercredi. On était deux cents dans la salle, il y avait des drapeaux partout et mon fils portait sa chemise blanche. À la fin, tout le monde a chanté et j’ai pleuré un peu.", n:"deux événements, trois décors, une nouvelle complète"},
       },
       note:"Écoutez la dernière deux fois : c’est le modèle exact du courriel que vous écrirez dans « Je me lance »."},

      {t:'ex', h:"À écouter et à répéter",
       p:"Six phrases de nouvelles.",
       rows:[
         ["J’ai eu ma citoyenneté mercredi dernier.","l’événement, avec sa date"],
         ["On était deux cents dans la grande salle.","le décor"],
         ["Il y avait des drapeaux sur tous les murs.","le décor, encore"],
         ["À la fin, tout le monde a chanté ensemble.","un événement dans le décor"],
         ["Je ne m’y attendais pas.","un état : imparfait"],
         ["Avant, elle travaillait toujours de nuit.","une habitude d’avant"],
       ]},

      {t:'piege', h:"Trois pièges du récit au passé",
       rows:[
         ["tout raconter au passé composé","« J’ai eu ma citoyenneté. On a été deux cents. Il y a eu des drapeaux. »",
          "La phrase est compréhensible mais elle sonne comme une liste. « On était deux cents », « il y avait des drapeaux » : le décor se décrit à l’imparfait."],
         ["employer l’imparfait pour un fait daté","« Mercredi dernier, j’avais ma citoyenneté » ✗",
          "Un fait précis, à une date précise, va au passé composé : « j’ai eu ma citoyenneté ». L’imparfait ferait croire à une habitude."],
         ["oublier l’accord avec être","« Je suis allé » écrit par une femme",
          "Avec <b>être</b>, le participe s’accorde avec le sujet : une femme écrit « je suis allée ». Ça ne s’entend pas, mais ça se lit."],
       ]},

      {t:'check', h:"Est-ce que c’est clair maintenant ?",
       p:"Quatre questions rapides.",
       qs:[
         {q:"« On était deux cents dans la salle » est…", opts:["un événement","un décor"], ok:1,
          fb:"Un décor : rien n’avance. D’où l’imparfait."},
         {q:"« Mercredi dernier, j’… ma citoyenneté »", opts:["ai eu","avais"], ok:0,
          fb:"Un fait daté → passé composé : « j’ai eu ma citoyenneté »."},
         {q:"Le test « et ensuite ? » annonce…", opts:["le passé composé","l’imparfait"], ok:0,
          fb:"Le passé composé. Le test « c’était comment ? » annonce l’imparfait."},
         {q:"Une femme écrit…", opts:["je suis allé","je suis allée"], ok:1,
          fb:"Avec être, le participe s’accorde avec le sujet."},
       ]},
    ]
  },

  // ════════════════════════════════════════════════════════════════════════
  t3exc: {
    eye:'Mini-leçon', tit:"Féliciter : quel, quelle, comme, que",
    blocs:[
      {t:'texte', h:"Trois secondes pour dire la bonne chose",
       p:"Quand quelqu’un vous annonce une bonne nouvelle, vous avez environ trois secondes. Si la première phrase est une question — « ça a pris combien de temps ? » — la personne se sent interrogée. Si c’est une exclamation — « quelle bonne nouvelle ! » — elle se sent accompagnée. Le programme du niveau 5 en fait une intention à part entière : <b>féliciter quelqu’un</b>. Elle tient dans quatre petits mots et dans un accord.",
       note:"Marisol le fait exactement ainsi dans le dialogue : « Quelle bonne nouvelle ! Félicitations, madame Faye ! » — deux exclamations, et seulement ensuite « comment ça s’est passé ? »."},

      {t:'ana', h:"quel, quelle, quels, quelles + un nom",
       p:"C’est la formule la plus employée. Le mot s’accorde avec le nom qui suit, exactement comme un déterminant.",
       mots:[["Masculin singulier","Quel beau projet ! · Quel courage !"],["Féminin singulier","Quelle bonne nouvelle ! · Quelle belle journée !",true],["Pluriel","Quels beaux enfants ! · Quelles belles photos !"]],
       say:"Quelle bonne nouvelle ! Quel beau projet !",
       note:"À l’oral, les quatre formes se prononcent pareil. À l’écrit, l’accord est ce qui se voit en premier — et c’est justement dans un message de félicitations qu’on ne veut pas se tromper."},

      {t:'ana', h:"comme et que + une phrase complète",
       p:"Après <b>comme</b> et <b>que</b>, il faut un sujet et un verbe : une phrase entière, pas un nom seul.",
       mots:[["Avec comme","Comme je suis contente pour vous ! · Comme ça a dû être long !"],["Avec que, plus soutenu","Que c’est beau ! · Qu’il doit être fier de vous !",true],["Ce qui est impossible","Comme bonne nouvelle ! ✗ · Que courage ! ✗"]],
       say:"Comme je suis contente pour vous ! Que c’est beau !",
       note:"Au Québec, on entend souvent « c’est-tu beau ! » : c’est du registre familier, très chaleureux à l’oral, et ça ne s’écrit pas dans un courriel."},

      {t:'ana', h:"Les félicitations toutes faites",
       p:"Elles ne s’inventent pas, elles se retiennent. Cinq suffisent pour toutes les occasions.",
       mots:[["Les directes","Félicitations ! · Bravo ! · Toutes mes félicitations !"],["Celles qui vous incluent","Je suis vraiment content pour vous. · Vous devez être fière.",true],["Celle qui ouvre la porte","Ça se fête ! · Il faut fêter ça."]],
       say:"Félicitations ! Je suis vraiment contente pour vous. Il faut fêter ça.",
       note:"<b>Félicitations</b> prend toujours un s, et on félicite <b>pour</b> quelque chose : « félicitations pour votre citoyenneté »."},

      {t:'ana', h:"Ce qui gâche une félicitation",
       p:"Trois habitudes très répandues, toutes dites avec de bonnes intentions.",
       mots:[["La ramener à soi","Moi, ça m’a pris deux ans seulement. ✗"],["Minimiser","Enfin, ce n’est qu’un papier. ✗",true],["Enchaîner sur un problème","Félicitations ! En passant, votre vélo bloque le hangar. ✗"]],
       say:"Félicitations ! Comme je suis contente pour vous.",
       note:"Une félicitation vit seule pendant au moins une phrase. Le reste — vos nouvelles, vos questions, le vélo dans le hangar — peut attendre trente secondes."},

      {t:'labo', h:"La même nouvelle, quatre réactions",
       p:"Madame Faye vient d’obtenir sa citoyenneté. Choisissez votre réaction.",
       axes:[{id:'f', lbl:'Comment réagissez-vous ?', opts:[
         ['a','Avec « quelle »'],
         ['b','Avec « comme »'],
         ['c','Avec « que »'],
         ['d','Avec une formule toute faite'],
         ['e','La réaction complète']]}],
       out:{
         a:{w:['des félicitations'], say:"Quelle bonne nouvelle ! Quelle belle journée pour vous !", n:"quel s’accorde avec le nom qui suit"},
         b:{w:['des félicitations'], say:"Comme je suis contente pour vous !", n:"comme + sujet + verbe"},
         c:{w:['la citoyenneté'], say:"Que c’est beau, cette photo de la cérémonie !", n:"que + phrase, registre un peu plus soutenu"},
         d:{w:['des félicitations'], say:"Félicitations, madame Faye ! Vous devez être fière.", n:"la formule directe, puis ce que l’autre ressent"},
         e:{w:['fêter'], say:"Quelle bonne nouvelle ! Félicitations ! Comme je suis contente pour vous. Il faut fêter ça.", n:"exclamation, félicitation, sentiment, invitation"},
       },
       note:"La dernière est le modèle : quatre phrases courtes, aucune question. Les questions viennent après."},

      {t:'ex', h:"À écouter et à répéter",
       p:"Six félicitations, prêtes à dire.",
       rows:[
         ["Quelle bonne nouvelle !","l’exclamation la plus employée"],
         ["Félicitations pour votre citoyenneté !","on félicite « pour » quelque chose"],
         ["Comme je suis contente pour vous !","comme + phrase complète"],
         ["Que c’est beau !","que + phrase, plus soutenu"],
         ["Vous devez être fière.","ce que l’autre ressent, dit à sa place"],
         ["Il faut fêter ça !","la phrase qui transforme la nouvelle en lien"],
       ]},

      {t:'piege', h:"Trois pièges des félicitations",
       rows:[
         ["mettre un nom après « comme »","« Comme bonne nouvelle ! » ✗",
          "Après « comme », il faut une phrase : « comme je suis contente ! ». Avec un nom seul, c’est « quelle » : « quelle bonne nouvelle ! »."],
         ["oublier l’accord de « quel »","« Quel bonne nouvelle » ✗",
          "« Nouvelle » est féminin : « quelle bonne nouvelle ». À l’oral personne n’entend la différence ; à l’écrit, tout le monde la voit."],
         ["poser une question avant de féliciter","« Ça a pris combien de temps ? »",
          "La question est légitime, mais elle vient en deuxième. En premier, l’exclamation : sinon la personne a l’impression d’être interrogée au lieu d’être fêtée."],
       ]},

      {t:'check', h:"Est-ce que c’est clair maintenant ?",
       p:"Quatre questions rapides.",
       qs:[
         {q:"Devant un nom seul, on emploie…", opts:["comme","quel / quelle"], ok:1,
          fb:"« Quelle bonne nouvelle ! ». « Comme » demande une phrase complète."},
         {q:"« Comme je suis contente ! » est…", opts:["correct","incorrect"], ok:0,
          fb:"Correct : « comme » est suivi d’un sujet et d’un verbe."},
         {q:"« Félicitations » s’écrit…", opts:["toujours avec un s","sans s au singulier"], ok:0,
          fb:"Toujours avec un s, et on félicite « pour » quelque chose."},
         {q:"Devant une bonne nouvelle, la première phrase est…", opts:["une question","une exclamation"], ok:1,
          fb:"Une exclamation. Les questions viennent ensuite, et elles sont ouvertes."},
       ]},
    ]
  },

};
