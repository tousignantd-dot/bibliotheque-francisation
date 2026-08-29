const PLUS = {

  prInto: {
    eye:'Mini-leçon', tit:"Ce que la voix dit et que les mots ne disent pas",
    blocs:[
      {t:'texte', h:"Le seul savoir de phonétique du niveau 8",
       p:"Le programme du niveau 8 ne demande plus qu'une chose à l'oreille et à la voix : produire l'<b>intonation expressive</b>. Pas un son nouveau, pas une liaison de plus — une mélodie. À ce stade, vous prononcez déjà assez bien pour être compris ; ce qui vous reste à gagner, c'est ce que la voix ajoute par-dessus les mots. Une même phrase de six mots peut dire la surprise, l'incompréhension ou la détermination, et c'est la seule chose que votre interlocuteur retiendra.",
       note:"C'est aussi ce qui s'entend le plus vite chez quelqu'un qui apprend une langue : une intonation plate se lit comme de l'indifférence, alors qu'elle n'est souvent que de la prudence."},

      {t:'texte', h:"Pourquoi ça compte précisément dans une entrevue",
       p:"Un comité de sélection prend une décision sur quarante-cinq minutes de conversation. Il ne se souviendra ni de vos dates ni de vos chiffres : il se souviendra d'une impression. Or l'impression se fabrique presque entièrement avec la mélodie. Dire « ce poste m'intéresse » d'une voix plate est pire que de ne rien dire, parce que la phrase promet quelque chose que la voix dément. Ce qui est en jeu ici n'est donc pas la politesse : c'est la crédibilité de ce que vous affirmez.",
       note:"Deux personnes disent la même phrase ; l'une est engagée, l'autre récite. La différence tient à trois notes."},

      {t:'ana', h:"La surprise — la voix monte d'un coup, à la fin",
       p:"La phrase part normalement puis grimpe brusquement sur les deux ou trois dernières syllabes. Souvent une question, souvent courte, souvent introduite par « comment ça » ou par la répétition du mot qui étonne.",
       mots:[['On dit','Trois étapes pour un poste de superviseure ?'],['La mélodie','plate, puis très haute à la fin',true],['Le repère','on répète le mot qui surprend']],
       say:"Trois étapes pour un poste de superviseure ?",
       note:"Attention : la surprise n'est pas le reproche. Si la voix monte trop tôt, la phrase devient un « vous vous moquez de moi »."},

      {t:'ana', h:"L'incompréhension — la voix ralentit et hésite au milieu",
       p:"On ne monte pas : on freine. Le débit se casse à l'endroit précis où le fil s'est rompu, souvent avec un petit silence avant le mot en cause.",
       mots:[['On dit',"Excusez-moi, le mot « vérifiable »… vous l'entendez comment ?"],['La mélodie','un creux et un silence avant le mot',true],['Le repère','on isole le mot avec la voix']],
       say:"Excusez-moi, le mot vérifiable, vous l'entendez comment ?",
       note:"C'est la mélodie qui dit « une seule chose m'échappe ». Sans elle, la même phrase se comprend comme « je n'ai rien suivi »."},

      {t:'ana', h:"La volonté — la voix descend, et chaque mot pèse",
       p:"À l'inverse de la surprise : la mélodie descend, le débit ralentit, et les syllabes sont détachées. C'est la voix de l'engagement, celle qui convient à une négociation.",
       mots:[['On dit','Ce poste-là, je le veux, et je vais vous dire pourquoi.'],['La mélodie','descendante, appuyée sur « veux »',true],['Le repère','on ne sourit pas en le disant']],
       say:"Ce poste-là, je le veux, et je vais vous dire pourquoi.",
       note:"Le bouton fait entendre la phrase <b>trois fois</b> : ordinaire, puis avec l'accent, puis le mot seul. Écoutez ce qui change — c'est la comparaison qui rend l'accent audible, jamais l'accent tout seul. Une phrase de volonté dite avec une intonation montante devient une demande de permission. C'est exactement l'inverse de ce qu'on voulait."},

      {t:'ana', h:"La déception — la voix tombe dès le début",
       p:"La quatrième, plus rare en entrevue mais utile à reconnaître chez l'autre : la mélodie descend tout de suite et ne remonte jamais. Le débit est régulier, presque lent.",
       mots:[['On dit',"Ah. Je pensais que l'échelle était communiquée."],['La mélodie','descendante dès la première syllabe',true],['Le repère','un « ah » ou un « bon » en tête']],
       say:"Ah. Je pensais que l'échelle était communiquée.",
       note:"Chez votre interlocuteur, c'est le signal qu'une réponse ne lui a pas plu. Il ne le dira pas ; la mélodie l'a déjà dit."},

      {t:'labo', h:"Écoutez les quatre intentions",
       p:"Choisissez une intention et un exemple.",
       axes:[
         {id:'i', lbl:'Quelle intention ?', opts:[['a','surprise'],['b','incompréhension'],['c','volonté'],['d','déception']]},
         {id:'n', lbl:'Quel exemple ?', opts:[['1','le premier'],['2','le second']]}],
       out:{
         a1:{w:["Trois étapes ?"], say:"Trois étapes ?", n:'la voix monte d\'un coup sur « étapes »'},
         a2:{w:["Comment ça, l'équipe n'existe pas ?"], say:"Comment ça, l'équipe n'existe pas ?", n:'« comment ça » annonce la surprise'},
         b1:{w:["Je perds le fil."], say:"Je perds le fil.", n:'débit qui freine, mélodie creusée'},
         b2:{w:["Vous avez bien dit quatre-vingt-dix ?"], say:"Vous avez bien dit quatre-vingt-dix ?", n:'on isole le chiffre qu\'on n\'est pas sûr d\'avoir saisi'},
         c1:{w:["Je le veux, ce poste-là."], say:"Je le veux, ce poste-là.", n:'mélodie descendante, syllabes détachées'},
         c2:{w:["Je tiens à ce que ce soit écrit."], say:"Je tiens à ce que ce soit écrit.", n:'la voix pèse sur « tiens » et sur « écrit »'},
         d1:{w:["Ah. Bon."], say:"Ah. Bon.", n:'deux syllabes qui tombent : la déception se passe de phrase'},
         d2:{w:["Je pensais que c'était décidé."], say:"Je pensais que c'était décidé.", n:'descendante du début à la fin'},
       },
       note:"Écoutez, puis répétez à voix haute en exagérant : l'exagération est ce qui fait entrer une mélodie dans l'oreille."},

      {t:'ex', h:"La même idée, trois intentions",
       p:"À gauche, ce qui est dit. À droite, ce que la voix ajoute.",
       rows:[
         ["L'équipe n'existe pas encore ?","surprise — la voix monte sur « encore »"],
         ["L'équipe n'existe pas encore.","constat — la voix reste plate"],
         ["L'équipe n'existe pas encore…","incompréhension — la voix freine et laisse ouvert"],
         ["Je veux ce poste.","volonté — la voix descend, les mots pèsent"],
         ["Je veux ce poste ?","surprise ou doute — la même phrase se retourne"],
         ["Bon. Je veux ce poste.","résignation — le « bon » tombe avant le reste"],
       ]},

      {t:'piege', h:"Trois pièges de l'intonation, en entrevue",
       rows:[
         ["monter la voix à chaque phrase","descendre quand on affirme",
          "Une mélodie qui monte partout transforme chaque affirmation en question, et chaque question en demande d'autorisation. C'est le défaut le plus fréquent, et il vient de la prudence : on n'ose pas conclure."],
         ["parler d'une voix parfaitement égale","varier au moins sur les trois phrases importantes",
          "Une voix plate se lit comme de l'indifférence, jamais comme du calme. Vous n'avez pas besoin de jouer la comédie : trois phrases sur quarante-cinq minutes suffisent."],
         ["s'excuser avec la voix","garder la même mélodie qu'aux autres phrases",
          "Beaucoup de gens baissent la voix au moment de demander quelque chose — un échelon, une précision. La demande devient inaudible et l'autre croit qu'elle est négociable à zéro."],
       ]},

      {t:'check', h:"Est-ce que c'est clair maintenant ?",
       p:"Quatre questions rapides.",
       qs:[
         {q:"« Trois étapes pour un poste de superviseure ? » exprime…", opts:["la surprise","la volonté"], ok:0,
          fb:"La voix monte brusquement à la fin : c'est la marque de la surprise."},
         {q:"Pour exprimer la volonté, la mélodie…", opts:["monte à la fin","descend et appuie"], ok:1,
          fb:"Elle descend. Une volonté dite en montant devient une demande de permission."},
         {q:"Dire « je perds le fil » en freinant au milieu exprime…", opts:["l'incompréhension","la déception"], ok:0,
          fb:"Le freinage et le silence isolent l'endroit où ça a rompu."},
         {q:"Une voix parfaitement égale pendant toute l'entrevue se lit comme…", opts:["du calme","de l'indifférence"], ok:1,
          fb:"Elle se lit comme de l'indifférence, même quand elle n'est que de la prudence."},
       ]},

      {t:'revoir', h:"À retenir",
       p:"Quatre mélodies : la <b>surprise</b> monte d'un coup à la fin ; l'<b>incompréhension</b> freine et laisse un silence avant le mot en cause ; la <b>volonté</b> descend et appuie ; la <b>déception</b> tombe dès la première syllabe. Choisissez-en trois pour votre entrevue et travaillez-les à voix haute — c'est ce qui restera quand les chiffres seront oubliés."},
    ]
  },

  prRepr: {
    eye:'Mini-leçon', tit:"Reprendre sans répéter",
    blocs:[
      {t:'texte', h:"Le problème que ça résout, et celui que ça crée",
       p:"Un texte qui répète douze fois « l'entreprise » se lit vite mais se lit mal : il donne l'impression d'avoir été écrit sans relecture. Le français règle cela par la <b>reprise</b> : on nomme la chose une fois, puis on y revient autrement. Le problème, c'est que la même règle rend les documents d'entreprise difficiles à lire pour vous — parce qu'à chaque paragraphe il faut reconnaître que « cette acquisition », « ce rachat » et « l'opération de janvier » désignent une seule et même chose.",
       note:"Savoir reprendre sert donc deux fois : à écrire mieux, et surtout à lire ce que d'autres ont écrit ainsi."},

      {t:'texte', h:"Le signal à repérer : le démonstratif",
       p:"Presque toutes les reprises commencent par <b>ce</b>, <b>cet</b>, <b>cette</b> ou <b>ces</b>. Quand vous voyez « cette réorganisation » et que le mot « réorganisation » n'a jamais été écrit avant, ne cherchez pas plus loin : le démonstratif vous dit qu'il s'agit de quelque chose de déjà dit, et que ce quelque chose est dans la phrase précédente, sous une autre forme. C'est presque toujours un verbe qui a été changé en nom.",
       note:"Méthode de lecture : mettez le doigt sur le démonstratif, remontez d'une phrase, et cherchez le verbe."},

      {t:'ana', h:"Par nominalisation — le verbe devient un nom",
       p:"La reprise la plus fréquente dans les écrits d'entreprise. Le verbe de la première phrase se transforme, et le nom obtenu reprend toute l'action.",
       mots:[['La première phrase','Le Groupe Landron a racheté l\'usine.'],['La reprise','Ce rachat a été annoncé le même jour.',true],['Les fabriques','-tion, -ment, -ance, ou rien du tout']],
       say:"Le Groupe Landron a racheté l'usine. Ce rachat a été annoncé le même jour.",
       note:"Les plus utiles dans ce module : racheter → le rachat · recruter → le recrutement · réorganiser → la réorganisation · fermer → la fermeture · croître → la croissance."},

      {t:'ana', h:"Par synonymie — un mot de sens voisin",
       p:"On remplace par un autre mot, presque équivalent. Attention : « presque » fait tout le travail, et le mot choisi colore la phrase.",
       mots:[['La première phrase','Le rachat de l\'usine remonte à janvier.'],['La reprise','Cette acquisition n\'a supprimé aucun emploi.',true],['La nuance','« acquisition » est plus neutre que « rachat »']],
       say:"Le rachat de l'usine remonte à janvier. Cette acquisition n'a supprimé aucun emploi.",
       note:"Un employeur écrira « acquisition » et un syndicat écrira « rachat ». Les deux disent le même fait et pas la même chose."},

      {t:'ana', h:"Par un générique — un mot plus large",
       p:"On remonte d'un cran : plusieurs éléments se rassemblent sous un mot qui les couvre tous.",
       mots:[['La première phrase','Le tri, l\'examen écrit et l\'entrevue de groupe.'],['La reprise','Ces trois étapes précèdent la rencontre finale.',true],['Le repère','souvent avec un nombre : ces deux, ces trois']],
       say:"Le tri, l'examen écrit et l'entrevue de groupe : ces trois étapes précèdent la rencontre finale.",
       note:"L'inverse existe aussi : partir du générique et descendre au précis. On appelle ces deux mouvements l'hyperonymie et l'hyponymie."},

      {t:'ana', h:"Par une expression synthétique — toute une phrase en un groupe",
       p:"La plus difficile, et celle qui impressionne le plus en entrevue : on résume une situation entière en un seul groupe du nom.",
       mots:[['La première phrase','Après dix-huit heures, il n\'y a plus personne sur place.'],['La reprise','Cet isolement est la vraie difficulté du poste.',true],['Ce qu\'il faut','trouver le mot qui nomme la situation']],
       say:"Après dix-huit heures, il n'y a plus personne sur place. Cet isolement est la vraie difficulté du poste.",
       note:"Onze ans là-bas et cinq ans ici → « cette situation ». Neuf postes à pourvoir en quatre mois → « cette échéance ». Nommer, c'est déjà commencer à répondre."},

      {t:'labo', h:"La phrase, puis sa reprise",
       p:"Choisissez un procédé et un exemple.",
       axes:[
         {id:'p', lbl:'Quel procédé ?', opts:[['a','nominalisation'],['b','synonyme'],['c','générique'],['d','expression synthétique']]},
         {id:'n', lbl:'Quel exemple ?', opts:[['1','le premier'],['2','le second']]}],
       out:{
         a1:{w:["ce rachat"], say:"Le groupe a racheté l'usine. Ce rachat date de janvier.", n:'racheter → le rachat'},
         a2:{w:["ce recrutement"], say:"L'entreprise recrute neuf personnes. Ce recrutement occupera le poste.", n:'recruter → le recrutement'},
         b1:{w:["cette acquisition"], say:"Le rachat remonte à janvier. Cette acquisition n'a supprimé aucun emploi.", n:'rachat → acquisition'},
         b2:{w:["cette épreuve"], say:"L'examen écrit dure quatre-vingt-dix minutes. Cette épreuve élimine peu de gens.", n:'examen → épreuve'},
         c1:{w:["ces trois étapes"], say:"Le tri, l'examen et l'entrevue de groupe : ces trois étapes précèdent la fin.", n:'trois choses → un mot qui les couvre'},
         c2:{w:["ces deux personnes"], say:"Madame Éthier et monsieur Bourbonnais : ces deux personnes forment le comité.", n:'deux noms → un générique'},
         d1:{w:["cet isolement"], say:"Après dix-huit heures, il n'y a plus personne. Cet isolement est le vrai défi.", n:'une phrase entière → un mot'},
         d2:{w:["cette situation"], say:"Onze ans de supervision là-bas, cinq ans d'exécution ici : cette situation inquiète.", n:'un parcours entier → un mot'},
       },
       note:"Essayez de refaire chaque reprise sans regarder : c'est en cherchant le mot qu'on l'apprend."},

      {t:'ex', h:"Huit reprises tirées du module",
       p:"À gauche, ce qui a été dit. À droite, comment on y revient.",
       rows:[
         ["Le groupe a racheté l'usine.","ce rachat · cette acquisition · l'opération de janvier"],
         ["L'entreprise recrute neuf personnes.","ce recrutement · cette embauche · ces neuf postes"],
         ["La production a été réorganisée.","cette réorganisation · ce changement"],
         ["On a fermé la ligne onze jours.","cette fermeture · cet arrêt · ces onze jours"],
         ["Le carnet de commandes a doublé.","cette croissance · cette hausse"],
         ["Elle a approuvé une étiquette erronée.","cette erreur · cet épisode"],
         ["Il n'y a plus personne après dix-huit heures.","cet isolement · cette autonomie"],
         ["Onze ans là-bas, cinq ans ici.","cette situation · ce parcours"],
       ]},

      {t:'piege', h:"Trois pièges de la reprise",
       rows:[
         ["reprendre par un mot qui change le sens","choisir un synonyme vraiment voisin",
          "« Ce problème » à la place de « cette réorganisation » n'est pas une reprise : c'est un jugement ajouté en cachette. En entrevue, ce genre de glissement se remarque."],
         ["reprendre quelque chose qui n'a pas été dit","ne reprendre que ce qui est dans la phrase d'avant",
          "Si vous écrivez « cette décision » alors qu'aucune décision n'a été nommée, le lecteur cherche, ne trouve pas, et vous relit. C'est le défaut le plus courant des textes d'apprenants avancés."],
         ["empiler trois reprises différentes de suite","garder deux formes au maximum",
          "Rachat, acquisition, opération, transaction : quatre mots pour une chose, et le lecteur finit par croire qu'il y a eu quatre événements."],
       ]},

      {t:'check', h:"Est-ce que c'est clair maintenant ?",
       p:"Quatre questions rapides.",
       qs:[
         {q:"« Le groupe a racheté l'usine. Ce rachat… » — quel procédé ?", opts:["nominalisation","synonyme"], ok:0,
          fb:"Le verbe « racheter » est devenu le nom « rachat »."},
         {q:"Quel mot annonce presque toujours une reprise ?", opts:["un démonstratif : ce, cette, ces","un possessif : son, sa, ses"], ok:0,
          fb:"Le démonstratif dit : « j'en ai déjà parlé »."},
         {q:"« Cet isolement » pour « il n'y a plus personne après dix-huit heures », c'est…", opts:["un générique","une expression synthétique"], ok:1,
          fb:"Toute une situation est résumée en un seul groupe du nom."},
         {q:"Écrire « ce problème » à la place de « cette réorganisation »…", opts:["est une reprise correcte","ajoute un jugement"], ok:1,
          fb:"Le mot choisi colore le fait. Ce n'est plus une reprise, c'est un commentaire."},
       ]},

      {t:'revoir', h:"À retenir",
       p:"Quatre procédés : <b>nominalisation</b> (racheter → ce rachat), <b>synonyme</b> (rachat → acquisition), <b>générique</b> (trois choses → ces trois étapes), <b>expression synthétique</b> (une phrase entière → cet isolement). Le signal est toujours le même : un démonstratif. Quand vous en voyez un, remontez d'une phrase et cherchez le verbe."},
    ]
  },

  t1cond: {
    eye:'Mini-leçon', tit:"Le conditionnel présent, ou l'art de ne rien conclure",
    blocs:[
      {t:'texte', h:"Trois emplois, une seule forme",
       p:"Le conditionnel présent se fabrique en une ligne : on prend le radical du <b>futur</b> et on lui colle les terminaisons de l'<b>imparfait</b>. <i>je pourrais, tu viendrais, il faudrait, nous serions, vous auriez, elles conviendraient.</i> Ce qui change, ce n'est jamais la forme : c'est ce qu'on en fait. Il sert à dire l'incertitude, à adoucir une demande, et à proposer sans imposer — trois emplois qui reviennent constamment dans un appel de présélection, où rien n'est encore décidé pour personne.",
       note:"Les verbes irréguliers au futur le sont ici aussi : aller → j'irais · faire → je ferais · savoir → je saurais · devoir → je devrais · vouloir → je voudrais."},

      {t:'texte', h:"Pourquoi c'est le temps du téléphone",
       p:"Au moment de l'appel, l'employeur n'a rien décidé et vous non plus. Employer l'indicatif reviendrait à faire semblant du contraire : « je commence le 4 novembre » suppose qu'on vous a engagée. Le conditionnel installe exactement l'état réel des choses — c'est possible, ce n'est pas fait. C'est aussi pourquoi la personne en face l'emploie tout autant : « nous vous situerions au deuxième échelon » veut dire qu'elle peut encore bouger.",
       note:"Repérer le conditionnel dans la bouche de l'autre est donc un renseignement : tant qu'il l'emploie, la porte n'est pas fermée."},

      {t:'ana', h:"Emploi 1 — l'incertitude",
       p:"Ce qui n'est pas encore décidé, ou ce qu'on rapporte sans le garantir.",
       mots:[['On dit','Est-ce que cet horaire vous conviendrait ?'],['Ce que ça installe','rien n\'est acquis, on explore',true],['Le contraire','« cet horaire vous convient » suppose que c\'est réglé']],
       say:"Est-ce que cet horaire vous conviendrait ?",
       note:"On l'emploie aussi pour rapporter une information non confirmée : « le poste comporterait une part de recrutement »."},

      {t:'ana', h:"Emploi 2 — la politesse",
       p:"Adoucir une demande ou une objection. La forme la plus utile de tout ce module.",
       mots:[['On dit','Pourriez-vous me préciser la taille des équipes ?'],['Ce que ça installe','vous pouvez refuser sans me refuser',true],['Le contraire','« précisez-moi » est un ordre']],
       say:"Pourriez-vous me préciser la taille des équipes ?",
       note:"Trois verbes couvrent presque tout : pouvoir (pourriez-vous), vouloir (je voudrais), aimer (j'aimerais)."},

      {t:'ana', h:"Emploi 3 — la proposition",
       p:"Mettre une idée sur la table sans la planter. C'est la forme de la négociation.",
       mots:[['On dit','Je proposerais le troisième échelon à l\'embauche.'],['Ce que ça installe','une offre, pas une exigence',true],['Le contraire','« je demande le troisième » ferme la discussion']],
       say:"Je proposerais le troisième échelon à l'embauche.",
       note:"Une proposition au conditionnel se discute ; une exigence à l'indicatif s'accepte ou se refuse. Vous choisissez lequel des deux vous voulez."},

      {t:'ana', h:"Le repère écrit : -ais, jamais -ai",
       p:"À la première personne, le futur et le conditionnel se prononcent presque pareil. Seul l'écrit tranche, et la faute se voit tout de suite.",
       mots:[['Futur','je serai disponible dès novembre'],['Conditionnel','je serais disponible si vous le souhaitiez',true],['Le test','y a-t-il une condition ou une politesse ?']],
       say:"Je serai disponible dès novembre. Je serais disponible si vous le souhaitiez.",
       note:"S'il y a « si + imparfait » quelque part, ou une demande polie, c'est <b>-ais</b>. Sinon c'est le futur, en <b>-ai</b>."},

      {t:'labo', h:"La même phrase, deux modes",
       p:"Choisissez un verbe et un mode.",
       axes:[
         {id:'v', lbl:'Quel verbe ?', opts:[['a','pouvoir'],['b','vouloir'],['c','falloir'],['d','être']]},
         {id:'m', lbl:'Quel mode ?', opts:[['1','indicatif'],['2','conditionnel']]}],
       out:{
         a1:{w:["vous pouvez me préciser"], say:"Vous pouvez me préciser la taille des équipes.", n:'direct, presque un ordre'},
         a2:{w:["pourriez-vous me préciser"], say:"Pourriez-vous me préciser la taille des équipes ?", n:'poli : l\'autre peut refuser'},
         b1:{w:["je veux revenir sur ce point"], say:"Je veux revenir sur ce point.", n:'brutal en entrevue, même sans le vouloir'},
         b2:{w:["je voudrais revenir sur ce point"], say:"Je voudrais revenir sur ce point.", n:'la même chose, acceptable partout'},
         c1:{w:["il faut que je sache"], say:"Il faut que je sache ce que l'examen évalue.", n:'une nécessité affirmée'},
         c2:{w:["il faudrait que je sache"], say:"Il faudrait que je sache ce que l'examen évalue.", n:'une nécessité proposée, plus douce'},
         d1:{w:["ces années sont vérifiables"], say:"Ces années sont vérifiables.", n:'un fait'},
         d2:{w:["ces années seraient-elles vérifiables"], say:"Ces années seraient-elles vérifiables ?", n:'une question prudente'},
       },
       note:"Écoutez les deux versions à la suite : c'est en les entendant côte à côte que la nuance devient audible."},

      {t:'ex', h:"Huit formes à connaître par cœur",
       p:"À gauche l'infinitif, à droite la première personne du conditionnel.",
       rows:[
         ["être","je serais — attention : deux « r » nulle part, un seul « s »"],
         ["avoir","j'aurais"],
         ["pouvoir","je pourrais — deux « r »"],
         ["vouloir","je voudrais"],
         ["devoir","je devrais"],
         ["falloir","il faudrait — seulement à la 3e personne"],
         ["aller","j'irais"],
         ["savoir","je saurais"],
       ]},

      {t:'piege', h:"Trois pièges du conditionnel",
       rows:[
         ["écrire « je serai » quand on demande poliment","écrire « je serais »",
          "La faute la plus fréquente à l'écrit, et elle change le sens : « je serai disponible » affirme, « je serais disponible » propose. Dans un courriel de candidature, les deux ne disent pas la même chose."],
         ["mettre un conditionnel après « si »","mettre l'imparfait après « si »",
          "« Si vous pourriez » n'existe pas. On dit « si vous pouviez, je serais disponible ». Le conditionnel est dans l'autre moitié de la phrase, jamais après « si »."],
         ["employer le conditionnel pour parler du passé","employer le conditionnel passé",
          "« Hier, je serais allée » ne veut rien dire. Pour un passé qui n'a pas eu lieu, il faut « je serais allée » précédé d'un plus-que-parfait — c'est le défi 3."],
       ]},

      {t:'check', h:"Est-ce que c'est clair maintenant ?",
       p:"Quatre questions rapides.",
       qs:[
         {q:"Comment se fabrique le conditionnel présent ?", opts:["radical du futur + terminaisons de l'imparfait","radical de l'imparfait + terminaisons du futur"], ok:0,
          fb:"Radical du futur, terminaisons de l'imparfait : je pourr-ais."},
         {q:"Après « si », on écrit…", opts:["si vous pourriez","si vous pouviez"], ok:1,
          fb:"Jamais de conditionnel après « si ». L'imparfait, et le conditionnel dans l'autre moitié."},
         {q:"« Nous vous situerions au deuxième échelon » signifie que…", opts:["c'est décidé","c'est encore négociable"], ok:1,
          fb:"Le conditionnel de votre interlocuteur vous dit que la porte n'est pas fermée."},
         {q:"« Je serai disponible » et « je serais disponible »…", opts:["disent la même chose","n'ont pas le même sens"], ok:1,
          fb:"Le premier affirme, le second propose. Un « s » sépare les deux."},
       ]},

      {t:'revoir', h:"À retenir",
       p:"Radical du <b>futur</b> + terminaisons de l'<b>imparfait</b>. Trois emplois : l'<b>incertitude</b> (rien n'est décidé), la <b>politesse</b> (pourriez-vous, je voudrais), la <b>proposition</b> (je proposerais). Jamais après « si ». Et à la première personne, la faute se voit à l'œil nu : <b>-ais</b>, pas <b>-ai</b>."},
    ]
  },

  t1inter: {
    eye:'Mini-leçon', tit:"Poser une question à trois hauteurs",
    blocs:[
      {t:'texte', h:"Trois formes, trois registres, aucune faute",
       p:"« L'équipe existe déjà ? » « Est-ce que l'équipe existe déjà ? » « L'équipe existe-t-elle déjà ? » Les trois questions sont correctes et disent la même chose. Ce qui les sépare est la <b>variété de langue</b> : familière, standard, soutenue. Le programme du niveau 8 demande précisément de reconnaître ces variétés et d'en tenir compte. Un candidat qui pose ses questions à la troisième hauteur, au téléphone, se place autrement qu'un candidat qui les pose à la première — sans avoir dit un mot de plus.",
       note:"Ce n'est pas une question de correction : c'est une question de distance. On choisit la distance qui convient à la personne."},

      {t:'texte', h:"Quand employer laquelle",
       p:"La forme familière convient sur le plancher, entre collègues, et le module vous le montre : chez Boréalis, on se tutoie à l'usine. La forme standard convient partout et ne vous trahira jamais. La forme soutenue convient au téléphone avec un employeur, à l'écrit, et en entrevue — et elle a un avantage précis : elle vous fait entendre comme quelqu'un qui écrit. Le défaut à éviter est de la choisir <i>parce qu'elle est difficile</i> et de l'employer ensuite avec un contremaître, où elle sonne raide.",
       note:"La règle pratique : soutenue à l'écrit et au téléphone avec la direction, standard partout ailleurs."},

      {t:'ana', h:"La règle centrale : le nom reste devant",
       p:"Quand le sujet est un nom, on ne le déplace pas. On le laisse en tête et on le <b>reprend</b> derrière le verbe par un pronom de la troisième personne.",
       mots:[['On écrit','Le poste comporte-t-il une part de recrutement ?'],['On n\'écrit pas','« Comporte le poste… ? »',true],['Le repère','nom + verbe + trait d\'union + pronom']],
       say:"Le poste comporte-t-il une part de recrutement ?",
       note:"Le pronom s'accorde avec le nom : le poste → il · l'échelle → elle · les documents → ils · les conditions → elles."},

      {t:'ana', h:"Le « t » de liaison, et ses deux traits d'union",
       p:"Si le verbe finit par une voyelle et que le pronom commence par une voyelle, on insère un <b>-t-</b> pour éviter le choc des deux sons.",
       mots:[['Avec -t-','existe-t-elle · décidera-t-il · a-t-elle · participera-t-elle'],['Sans -t-','est-elle · sont-ils · comporte-t-il… non : comporte finit par « e »',true],['La règle sûre','verbe en -e, -a ou -c terminal muet → on met le -t-']],
       say:"L'équipe existe-t-elle ? Le comité décidera-t-il ?",
       note:"Deux traits d'union dans ce cas, jamais un seul : <b>existe-t-elle</b>, et non « existe t-elle » ni « existe-t elle »."},

      {t:'ana', h:"Aux temps composés, on inverse l'auxiliaire",
       p:"Le participe passé ne bouge pas : il reste après le pronom, à sa place normale.",
       mots:[['On écrit','L\'usine a-t-elle été rachetée en janvier ?'],['On n\'écrit pas','« L\'usine a été-t-elle rachetée ? »',true],['Le repère','l\'inversion porte sur avoir ou être']],
       say:"L'usine a-t-elle été rachetée en janvier ?",
       note:"Même chose au passif et au futur antérieur : « les postes auront-ils été pourvus avant février ? »."},

      {t:'ana', h:"Avec un mot interrogatif, il passe devant tout",
       p:"Combien, quand, pourquoi, comment, où : ils se placent en tête, et l'inversion suit derrière.",
       mots:[['On écrit','Combien de personnes l\'équipe compte-t-elle ?'],['Aussi','Pourquoi ce poste a-t-il été créé ?',true],['Le piège','ne pas ajouter « est-ce que » en plus']],
       say:"Combien de personnes l'équipe compte-t-elle ? Pourquoi ce poste a-t-il été créé ?",
       note:"« Pourquoi est-ce que ce poste a-t-il été créé ? » mélange les deux formes. On choisit l'une ou l'autre."},

      {t:'labo', h:"La même question, trois hauteurs",
       p:"Choisissez une question et un registre.",
       axes:[
         {id:'q', lbl:'Quelle question ?', opts:[['a','sur l\'équipe'],['b','sur l\'échelle'],['c','sur la formation']]},
         {id:'r', lbl:'Quel registre ?', opts:[['1','familier'],['2','standard'],['3','soutenu']]}],
       out:{
         a1:{w:["L'équipe existe déjà ?"], say:"L'équipe existe déjà ?", n:'entre collègues, sur le plancher'},
         a2:{w:["Est-ce que l'équipe existe déjà ?"], say:"Est-ce que l'équipe existe déjà ?", n:'partout, sans risque'},
         a3:{w:["L'équipe existe-t-elle déjà ?"], say:"L'équipe existe-t-elle déjà ?", n:'au téléphone avec la direction, à l\'écrit'},
         b1:{w:["L'échelle est communiquée ?"], say:"L'échelle est communiquée ?", n:'familier'},
         b2:{w:["Est-ce que l'échelle est communiquée ?"], say:"Est-ce que l'échelle est communiquée ?", n:'standard'},
         b3:{w:["L'échelle est-elle communiquée ?"], say:"L'échelle est-elle communiquée ?", n:'soutenu, sans -t- : « est » finit par une consonne'},
         c1:{w:["La formation est payée ?"], say:"La formation est payée ?", n:'familier'},
         c2:{w:["Est-ce que la formation est payée ?"], say:"Est-ce que la formation est payée ?", n:'standard'},
         c3:{w:["La formation est-elle payée ?"], say:"La formation est-elle payée ?", n:'soutenu'},
       },
       note:"Dites les trois à voix haute d'affilée : c'est la mélodie, autant que les mots, qui change de hauteur."},

      {t:'ex', h:"Huit questions prêtes pour un appel de présélection",
       p:"À gauche la forme soutenue, à droite ce qu'elle vous apprend.",
       rows:[
         ["L'équipe existe-t-elle déjà, ou faut-il la constituer ?","poste neuf ou remplacement"],
         ["Le poste comporte-t-il des responsabilités absentes de l'annonce ?","le travail réel"],
         ["Pourquoi ce poste a-t-il été créé ?","la question qui rapporte le plus"],
         ["Combien de personnes l'équipe compte-t-elle ?","l'ampleur de la charge"],
         ["À qui la personne rendra-t-elle compte ?","le supérieur immédiat"],
         ["Le processus comporte-t-il d'autres étapes ?","de quoi se préparer"],
         ["L'échelle salariale est-elle communiquée avant l'entrevue ?","la marge de négociation"],
         ["Quand la décision sera-t-elle prise ?","quand relancer, sans harceler"],
       ]},

      {t:'piege', h:"Trois pièges de l'inversion",
       rows:[
         ["déplacer le nom derrière le verbe","laisser le nom devant et le reprendre",
          "« Comporte le poste une part de recrutement ? » existe en poésie, pas dans un appel téléphonique. Le nom reste devant : « le poste comporte-t-il »."],
         ["oublier le « t » de liaison","l'ajouter entre deux traits d'union",
          "« Existe-elle ? » est impossible à prononcer, et « existe t'elle » n'existe pas. C'est <b>existe-t-elle</b>, avec deux traits d'union et aucune apostrophe."],
         ["cumuler « est-ce que » et l'inversion","choisir une seule des deux formes",
          "« Est-ce que le poste comporte-t-il… » double la question. C'est la faute qui trahit le plus sûrement quelqu'un qui vise la forme soutenue sans la maîtriser."],
       ]},

      {t:'check', h:"Est-ce que c'est clair maintenant ?",
       p:"Quatre questions rapides.",
       qs:[
         {q:"Quand le sujet est un nom, où le place-t-on ?", opts:["devant, avec reprise par un pronom","derrière le verbe"], ok:0,
          fb:"Le nom reste devant, et un pronom le reprend après le verbe."},
         {q:"« L'équipe existe___elle ? »", opts:["-t-","-"], ok:0,
          fb:"« Existe » finit par une voyelle : il faut le -t- entre deux traits d'union."},
         {q:"Au passé composé, l'inversion porte sur…", opts:["le participe passé","l'auxiliaire"], ok:1,
          fb:"L'usine a-t-elle été rachetée : c'est « a » qui bouge."},
         {q:"« Pourquoi est-ce que ce poste a-t-il été créé ? »", opts:["est correct","mélange deux formes"], ok:1,
          fb:"On choisit « est-ce que » ou l'inversion, jamais les deux."},
       ]},

      {t:'revoir', h:"À retenir",
       p:"Trois hauteurs pour une même question, et la troisième s'emploie au téléphone et à l'écrit. Le nom sujet <b>reste devant</b> et se reprend par un pronom. Un <b>-t-</b> entre deux traits d'union quand le verbe finit par une voyelle. Aux temps composés, on inverse l'<b>auxiliaire</b>. Et jamais « est-ce que » et l'inversion ensemble."},
    ]
  },

  t1refor: {
    eye:'Mini-leçon', tit:"Dire précisément ce qu'on n'a pas compris",
    blocs:[
      {t:'texte', h:"Le savoir que le programme nomme, et qu'on lit mal",
       p:"Parmi les points de lexique du niveau 8 figure celui-ci : « phrases clés pour faire clarifier les points équivoques » et « expressions pour reprendre une partie d'un discours ». Le mot qui compte est <b>partie</b>. On n'apprend pas ici à dire « je n'ai pas compris » : à votre niveau, c'est presque toujours faux. Vous avez compris quinze mots sur seize. Ce qu'il faut apprendre, c'est à dire <i>lequel</i> des seize a manqué — et cela change complètement la façon dont on vous répond.",
       note:"Dire qu'on n'a rien compris oblige l'autre à tout reprendre depuis le début, et vous fait passer pour beaucoup plus loin du compte que vous ne l'êtes."},

      {t:'texte', h:"Ce que ça produit chez l'autre",
       p:"Une demande précise se répare en dix secondes, et elle se lit comme de la rigueur : quelqu'un qui isole un mot montre qu'il a suivi tout le reste. Une demande vague coûte trois minutes à votre interlocuteur, et elle laisse une impression de fatigue. C'est particulièrement vrai au téléphone, où il n'y a ni visage ni geste pour rattraper. Vous n'avez pas besoin d'être parfait : vous avez besoin d'être précis.",
       note:"Une seule demande de clarification par conversation passe très bien. Trois de suite fatiguent, quel que soit leur niveau de précision."},

      {t:'ana', h:"Faire préciser un mot — un seul",
       p:"On ne demande pas une définition de dictionnaire : on demande ce que l'autre met dans le mot, ici, dans cette phrase-ci.",
       mots:[['On dit',"Excusez-moi, le mot « vérifiable », vous l'entendez comment ?"],['Autre forme',"Qu'est-ce que vous mettez exactement sous « polyvalence » ?",true],["Ce qu'on évite","« je ne connais pas ce mot »"]],
       say:"Excusez-moi, le mot vérifiable, vous l'entendez comment ?",
       note:"Cette formulation a un second avantage : beaucoup de mots d'entreprise sont flous, et votre question fait travailler l'autre. On l'a vu dans l'appel : « je la note »."},

      {t:'ana', h:"Faire répéter une partie seulement",
       p:"On dit jusqu'où on a suivi, et où le fil s'est rompu. L'autre reprend à cet endroit-là, pas au début.",
       mots:[['On dit',"Je vous suis jusqu'à « après dix-huit heures » ; après, je perds le fil."],['Autre forme',"Vous avez dit trois dates ; j'ai la première et la troisième.",true],['Le principe','montrer où, pas dire que']],
       say:"Je vous suis jusqu'à après dix-huit heures ; après, je perds le fil.",
       note:"Citer les mots exacts où ça a cassé est ce qui rend la réparation instantanée."},

      {t:'ana', h:"Vérifier qu'on a bien compris",
       p:"On reformule avec ses <b>propres</b> mots. Répéter les mots de l'autre ne prouve rien : on peut répéter sans comprendre.",
       mots:[['On dit','Si je comprends bien, l\'équipe reste à constituer ?'],['Autre forme','Autrement dit, c\'est le raisonnement que vous regardez.',true],['Le test','ai-je changé les mots ?']],
       say:"Si je comprends bien, l'équipe reste à constituer ?",
       note:"C'est le geste qui a le plus d'effet dans un appel : il montre que vous avez traité l'information, pas seulement reçu."},

      {t:'ana', h:"Résumer avant de conclure",
       p:"En fin d'échange, on rassemble en une phrase ce qui a été convenu. Cela ferme proprement et laisse une trace commune.",
       mots:[['On dit','En somme, trois étapes réparties sur deux semaines.'],['Autre forme','Pour résumer, vous cherchez quelqu\'un qui bâtira l\'équipe.',true],['L\'effet','on se souvient de la dernière phrase']],
       say:"En somme, trois étapes réparties sur deux semaines.",
       note:"Le résumé final est aussi une vérification : si vous vous êtes trompée, l'autre corrige tout de suite, et non trois jours plus tard."},

      {t:'labo', h:"Quatre gestes, deux formulations chacun",
       p:"Choisissez un geste et une formulation.",
       axes:[
         {id:'g', lbl:'Quel geste ?', opts:[['a','préciser un mot'],['b','faire répéter une partie'],['c','vérifier'],['d','résumer']]},
         {id:'f', lbl:'Quelle formulation ?', opts:[['1','la première'],['2','la seconde']]}],
       out:{
         a1:{w:["vous l'entendez comment ?"], say:"Le mot vérifiable, vous l'entendez comment ?", n:'on demande le sens dans cette phrase-ci'},
         a2:{w:["qu'est-ce que vous mettez sous ce mot ?"], say:"Qu'est-ce que vous mettez exactement sous polyvalence ?", n:'utile quand le mot est flou pour tout le monde'},
         b1:{w:["je vous suis jusqu'à…"], say:"Je vous suis jusqu'à dix-huit heures ; après, je perds le fil.", n:'on montre l\'endroit exact'},
         b2:{w:["j'ai la première et la troisième"], say:"Vous avez dit trois dates ; j'ai la première et la troisième.", n:'on dit ce qu\'on a, pas ce qui manque'},
         c1:{w:["si je comprends bien"], say:"Si je comprends bien, l'équipe reste à constituer ?", n:'on reformule avec ses propres mots'},
         c2:{w:["autrement dit"], say:"Autrement dit, c'est le raisonnement que vous regardez.", n:'on traduit, on n\'ajoute rien'},
         d1:{w:["en somme"], say:"En somme, trois étapes réparties sur deux semaines.", n:'on ferme en rassemblant'},
         d2:{w:["pour résumer"], say:"Pour résumer, vous cherchez quelqu'un qui bâtira l'équipe.", n:'on redit l\'essentiel du besoin'},
       },
       note:"Choisissez-en deux et apprenez-les par cœur : au téléphone, on n'a pas le temps de composer une phrase."},

      {t:'ex', h:"Ce qu'on dit, et ce que l'autre entend",
       p:"À gauche la formule, à droite l'effet réel.",
       rows:[
         ["Je n'ai pas compris.","il faut tout reprendre — trois minutes perdues"],
         ["Le mot « vérifiable », vous l'entendez comment ?","une seule chose à préciser — dix secondes"],
         ["Pardon ?","l'autre répète la phrase entière, souvent identique"],
         ["Vous avez bien dit quatre-vingt-dix, et non quarante ?","le chiffre se confirme d'un mot"],
         ["Oui, oui.","l'autre continue, et vous répondrez à côté"],
         ["Si je comprends bien, l'équipe reste à constituer ?","l'autre confirme ou corrige immédiatement"],
         ["C'est-à-dire ?","utile une fois, agaçant deux"],
         ["En somme, trois étapes sur deux semaines.","vous laissez l'impression d'avoir tout suivi"],
       ]},

      {t:'piege', h:"Trois pièges au téléphone",
       rows:[
         ["hocher la tête","dire un mot",
          "Au téléphone, votre interlocuteur n'entend rien de vos gestes. Le silence se lit comme une absence, et l'autre finit par demander « vous êtes toujours là ? »."],
         ["répondre « oui oui » à ce qu'on n'a pas saisi","poser la question tout de suite",
          "Le « oui oui » coûte dix minutes : on vous croit d'accord, on continue, et vous répondez à côté à la question suivante. Personne ne pardonne mal une demande de précision ; tout le monde remarque une réponse hors sujet."],
         ["s'excuser trois fois avant de demander","demander une fois, simplement",
          "« Excusez-moi, je suis désolée, je ne suis pas sûre, pardon… » occupe plus de place que la question elle-même et déplace l'attention sur votre gêne."],
       ]},

      {t:'check', h:"Est-ce que c'est clair maintenant ?",
       p:"Quatre questions rapides.",
       qs:[
         {q:"« Je n'ai pas compris » est le plus souvent…", opts:["exact","faux et coûteux"], ok:1,
          fb:"Vous avez compris presque tout. Nommez ce qui manque : un mot."},
         {q:"Reformuler avec les mots de l'autre…", opts:["prouve qu'on a compris","ne prouve rien"], ok:1,
          fb:"On peut répéter sans comprendre. Il faut changer les mots."},
         {q:"« Je vous suis jusqu'à dix-huit heures » sert à…", opts:["faire répéter une partie","résumer"], ok:0,
          fb:"On montre l'endroit exact où le fil s'est rompu."},
         {q:"Combien de demandes de clarification passent bien dans un appel ?", opts:["une, éventuellement deux","autant qu'il en faut"], ok:0,
          fb:"Une passe très bien. Trois fatiguent, même bien formulées."},
       ]},

      {t:'revoir', h:"À retenir",
       p:"Quatre gestes : <b>préciser un mot</b> (vous l'entendez comment ?), <b>faire répéter une partie</b> (je vous suis jusqu'à…), <b>vérifier</b> (si je comprends bien…), <b>résumer</b> (en somme…). Le principe unique : nommer précisément ce qui manque, jamais dire qu'on n'a rien compris."},
    ]
  },

  t1trois: {
    eye:'Mini-leçon', tit:"Trois étapes, et ce que chacune regarde",
    blocs:[
      {t:'texte', h:"Pourquoi un processus, et pas une entrevue",
       p:"Au-dessus d'un certain niveau de responsabilité, presque aucun employeur ne décide sur une seule rencontre. Il y a une raison simple à cela : une entrevue mesure surtout la capacité à passer une entrevue. En ajoutant un écrit et une mise en groupe, l'employeur observe trois choses différentes — comment vous raisonnez seul, comment vous êtes avec d'autres, et qui vous êtes. Chacune est éliminatoire, et rien ne s'efface entre elles : ce qu'on note à l'étape 1 est relu avant l'étape 3.",
       note:"C'est aussi ce qui rend le processus long : deux semaines entre le premier appel et la décision est un délai normal, pas un mauvais signe."},

      {t:'texte', h:"L'étape qu'on prépare, et celle qui élimine",
       p:"Tout le monde prépare l'entrevue individuelle : c'est celle qu'on imagine, celle des films, celle dont les proches parlent. Or c'est presque toujours à la <b>deuxième</b> qu'on tombe. La raison est contre-intuitive : en entrevue de groupe, les candidats croient qu'il faut briller, et ils écrasent les trois autres. L'observateur, lui, cherche exactement le contraire — quelqu'un qui écoute, qui reprend l'idée d'un autre en la nommant, et qui laisse la parole.",
       note:"Consacrez à la deuxième étape au moins autant de préparation qu'à la troisième. C'est le conseil le plus rentable de ce module."},

      {t:'ana', h:"L'examen écrit — comment vous raisonnez",
       p:"Une mise en situation impossible : plusieurs problèmes en même temps, et il faut choisir un ordre. On ne cherche pas la bonne réponse, on cherche la raison que vous donnez.",
       mots:[['Ce qu\'on donne','une ligne arrêtée, trois problèmes, quatre-vingt-dix minutes'],['Ce qu\'on regarde','l\'ordre et sa justification',true],['Ce qui échoue','un ordre sans raison, même le bon']],
       say:"On regarde l'ordre de vos décisions, et la raison que vous en donnez.",
       note:"Écrivez court, en phrases entières, et donnez toujours le « parce que ». Un tableau sans phrase ne se défend pas."},

      {t:'ana', h:"L'entrevue de groupe — comment vous êtes avec les autres",
       p:"Quatre candidats, une tâche commune, et des gens qui observent sans parler. On note qui écoute, qui construit sur l'idée d'un autre, qui coupe la parole.",
       mots:[['Ce qui sert','« Je reprends ce que monsieur Guillemette a dit… »'],['Ce qui nuit','parler le plus longtemps',true],['Ce qui tue','ne rien dire du tout']],
       say:"Je reprends ce que monsieur Guillemette a dit, et j'ajouterais une chose.",
       note:"Deux ou trois interventions bien placées valent mieux que huit. Mais zéro intervention se lit comme une absence."},

      {t:'ana', h:"L'entrevue individuelle — qui vous êtes, et ce que vous voulez",
       p:"Là seulement, on parle de votre parcours, de vos exemples, de vos conditions. C'est aussi le seul moment où l'on négocie.",
       mots:[['Ce qu\'on demande','un exemple daté, une erreur, une projection'],['Ce qu\'on négocie','l\'échelon, l\'horaire, la formation',true],['La faute','négocier avant cette étape-là']],
       say:"C'est le seul moment du processus où l'on parle d'argent.",
       note:"Demander l'échelon à l'entrevue de groupe, devant trois autres candidats, met tout le monde mal à l'aise et vous écarte."},

      {t:'labo', h:"Une phrase, une étape",
       p:"Choisissez une étape et un aspect.",
       axes:[
         {id:'e', lbl:'Quelle étape ?', opts:[['a','examen écrit'],['b','entrevue de groupe'],['c','entrevue individuelle']]},
         {id:'a', lbl:'Quel aspect ?', opts:[['1','ce qu\'on observe'],['2','ce qui fait tomber']]}],
       out:{
         a1:{w:["l'ordre et la justification"], say:"On observe l'ordre de vos décisions et la raison que vous en donnez.", n:'la bonne réponse n\'existe pas'},
         a2:{w:["un ordre sans raison"], say:"Un ordre donné sans justification ne se défend pas, même s'il est juste.", n:'écrivez toujours le « parce que »'},
         b1:{w:["l'écoute et la reprise"], say:"On observe si vous écoutez et si vous reprenez l'idée d'un autre.", n:'nommer la personne compte beaucoup'},
         b2:{w:["vouloir briller"], say:"Écraser les trois autres candidats vous écarte immédiatement.", n:'c\'est l\'étape où l\'on tombe le plus'},
         c1:{w:["les exemples datés"], say:"On demande un exemple daté, une erreur, et ce que vous en avez tiré.", n:'préparez-en trois, pas un'},
         c2:{w:["répondre en généralités"], say:"Une réponse sans date et sans chiffre ne laisse aucune trace.", n:'« je suis rigoureuse » ne prouve rien'},
       },
       note:"Chaque étape a son geste principal. Apprenez lequel avant d'y entrer."},

      {t:'ex', h:"Ce qu'on vous dira, et ce que ça veut dire",
       p:"À gauche la phrase entendue, à droite ce qu'elle annonce.",
       rows:[
         ["« Un appel d'une vingtaine de minutes, sans piège. »","présélection : disponibilité et vérification"],
         ["« Une mise en situation, quatre-vingt-dix minutes. »","examen écrit : on regarde le raisonnement"],
         ["« Vous serez quatre autour de la table. »","entrevue de groupe : on observe l'écoute"],
         ["« Nous avons quarante-cinq minutes. »","entrevue individuelle : exemples et conditions"],
         ["« Je vous envoie la convocation aujourd'hui. »","vous passez à l'étape suivante"],
         ["« Nous vous rappellerons vendredi. »","une date : notez-la, et relancez le lundi"],
         ["« Nous vous situerions au deuxième échelon. »","la négociation est ouverte"],
         ["« Nous gardons votre dossier. »","c'est un refus poli, dans neuf cas sur dix"],
       ]},

      {t:'piege', h:"Trois pièges du processus",
       rows:[
         ["préparer seulement la dernière étape","préparer surtout la deuxième",
          "C'est à l'entrevue de groupe que la majorité des candidats sont écartés, et c'est celle que personne ne travaille. Le calcul est vite fait."],
         ["croire que les étapes sont indépendantes","se rappeler que tout est relu",
          "Ce que vous avez écrit à l'examen est sur la table à l'entrevue finale. Une contradiction entre l'écrit et l'oral se voit immédiatement — et c'est arrivé dans ce module : on a demandé à Shirin d'expliquer son classement."],
         ["négocier trop tôt","attendre l'entrevue individuelle",
          "Une question d'argent posée à la présélection ou devant d'autres candidats vous fait passer pour quelqu'un qui n'a pas compris où il est."],
       ]},

      {t:'check', h:"Est-ce que c'est clair maintenant ?",
       p:"Quatre questions rapides.",
       qs:[
         {q:"À quelle étape la majorité des candidats sont-ils écartés ?", opts:["l'entrevue de groupe","l'entrevue individuelle"], ok:0,
          fb:"C'est la deuxième, et c'est celle que presque personne ne prépare."},
         {q:"À l'examen écrit, ce qui compte est…", opts:["la bonne réponse","l'ordre et sa justification"], ok:1,
          fb:"Il n'y a pas de bonne réponse : il y a des choix justifiés."},
         {q:"Ce qu'on écrit sur vous à l'étape 1…", opts:["s'efface entre les étapes","est relu avant l'étape 3"], ok:1,
          fb:"Rien ne s'efface. Le dossier se relit avant la rencontre finale."},
         {q:"On négocie l'échelon…", opts:["dès l'appel de présélection","à l'entrevue individuelle"], ok:1,
          fb:"C'est le seul moment prévu pour ça."},
       ]},

      {t:'revoir', h:"À retenir",
       p:"Trois étapes, trois observations : l'<b>écrit</b> regarde comment vous raisonnez, le <b>groupe</b> comment vous êtes avec d'autres, l'<b>individuelle</b> qui vous êtes et ce que vous voulez. Rien ne s'efface entre les trois. Préparez surtout la deuxième, et ne négociez qu'à la troisième."},
    ]
  },

  t2profil: {
    eye:'Mini-leçon', tit:"Lire un profil d'entreprise sans se faire endormir",
    blocs:[
      {t:'texte', h:"Un texte écrit pour rassurer",
       p:"Une page « À propos » ou un profil d'entreprise n'est pas un document d'information : c'est un document de présentation, relu par quelqu'un dont le métier consiste à éviter les ennuis. Tout ce qui s'y trouve est vrai ; ce qui a été retiré ne se voit pas. Le lire utilement, c'est donc lire deux textes à la fois — celui qui est là, et celui qui manque. Le second se devine à trois signes : les phrases sans sujet, les valeurs sans exemple, et les chiffres sans période.",
       note:"Le but n'est pas de se méfier : c'est de savoir quelles questions poser en entrevue, et il en sort toujours trois ou quatre."},

      {t:'texte', h:"Ce qu'on y prélève, et ce qu'on laisse",
       p:"Trois éléments valent la peine d'être notés : un <b>fait récent</b> (un rachat, un agrandissement, un contrat), un <b>chiffre</b> (l'effectif, un pourcentage, un montant), et une <b>difficulté avouée</b> (l'isolement du quart de soir, un taux à améliorer). Ces trois-là se replacent naturellement dans une réponse d'entrevue et prouvent en une phrase que vous avez lu. Tout le reste — l'année de fondation seule, les valeurs, le vocabulaire d'ambiance — ne prouve rien, parce que tout le monde peut le citer.",
       note:"Réal Bourbonnais l'annonce dans le module : « à l'entrevue individuelle, je pose toujours une question tirée du profil ». Ce n'est pas une menace, c'est un mode d'emploi."},

      {t:'ana', h:"Les faits datés sont les seuls solides",
       p:"Une année, un effectif, un pourcentage, un montant : ce sont les seuls éléments qu'on ne peut pas arranger sans mentir. Prélevez-les et laissez le reste de côté.",
       mots:[['Ce qu\'on note','deux cent dix personnes, dont cent trente-quatre à la production'],['Ce qu\'on laisse','« une entreprise à échelle humaine »',true],['Le test','est-ce que ça se vérifie ?']],
       say:"Deux cent dix personnes, dont cent trente-quatre à la production.",
       note:"Un chiffre retenu et replacé au bon moment vaut dix minutes de préparation générale."},

      {t:'ana', h:"Les phrases sans sujet — le passif qui cache",
       p:"« L'entreprise a été acquise », « une réorganisation a été menée » : ces tournures ne disent pas <b>qui</b> a décidé. C'est souvent exactement le renseignement qui vous manquerait.",
       mots:[['Ce qui est écrit','L\'entreprise a été acquise en janvier.'],['Ce qui manque','par qui, et à l\'initiative de qui',true],['Ce que ça donne','une question toute prête']],
       say:"L'entreprise a été acquise en janvier. Par qui, et à quelle initiative ?",
       note:"Notez chaque passif que vous rencontrez : la liste que vous en tirez est votre liste de questions."},

      {t:'ana', h:"Une valeur affichée n'est pas une information",
       p:"« Le respect », « l'excellence », « l'esprit d'équipe » figurent dans neuf profils sur dix et ne distinguent rien. Ce qui vaut quelque chose est une <b>pratique nommée</b>.",
       mots:[['Sans valeur','Nous plaçons l\'humain au centre.'],['Avec valeur','Un taux de roulement de onze pour cent.',true],['Le test','est-ce que ça pourrait être faux ?']],
       say:"Un taux de roulement de onze pour cent, inférieur à la moyenne du secteur.",
       note:"La règle est courte : si la phrase inverse serait absurde à écrire, la phrase ne dit rien. Aucune entreprise n'écrit « nous méprisons l'humain »."},

      {t:'ana', h:"La difficulté avouée est un cadeau",
       p:"Quand un profil reconnaît une contrainte, il vous dit ce qui inquiète l'employeur. Reprendre cette contrainte en entrevue, et y répondre, est ce qui distingue le plus vite un candidat.",
       mots:[['Ce qui est écrit','La supervision du soir s\'exerce sans soutien sur place.'],['Ce que ça dit','ils ont déjà perdu quelqu\'un là-dessus',true],['Ce qu\'on en fait','on y répond avant qu\'on le demande']],
       say:"La supervision du soir s'exerce sans soutien sur place à partir de dix-huit heures.",
       note:"Le profil de Boréalis présente cette autonomie « comme une exigence plutôt que comme une contrainte » : la formulation elle-même est un aveu."},

      {t:'labo', h:"La phrase du profil, et la question qu'elle donne",
       p:"Choisissez un type de phrase et un exemple.",
       axes:[
         {id:'t', lbl:'Quel type ?', opts:[['a','fait daté'],['b','passif sans sujet'],['c','valeur creuse'],['d','difficulté avouée']]},
         {id:'n', lbl:'Quel exemple ?', opts:[['1','le premier'],['2','le second']]}],
       out:{
         a1:{w:["deux cent dix personnes"], say:"Deux cent dix personnes, dont cent trente-quatre à la production.", n:'à noter et à replacer'},
         a2:{w:["quatre-vingt-deux pour cent"], say:"Les chaînes du soir tournent à quatre-vingt-deux pour cent.", n:'demander ce que le taux comprend'},
         b1:{w:["a été acquise"], say:"L'entreprise a été acquise par le Groupe Landron.", n:'qui a décidé, et pourquoi ?'},
         b2:{w:["a été réorganisée"], say:"La production a été réorganisée en trois quarts.", n:'à l\'initiative de qui ?'},
         c1:{w:["à échelle humaine"], say:"Une entreprise à échelle humaine.", n:'la phrase inverse serait absurde : elle ne dit rien'},
         c2:{w:["nous plaçons l'humain au centre"], say:"Nous plaçons l'humain au centre de nos décisions.", n:'aucune entreprise n\'écrit le contraire'},
         d1:{w:["sans soutien sur place"], say:"La supervision du soir s'exerce sans soutien sur place.", n:'ils ont déjà eu un problème là'},
         d2:{w:["une exigence du poste"], say:"L'entreprise présente cette autonomie comme une exigence du poste.", n:'la formulation avoue plus que le fait'},
       },
       note:"Faites cet exercice sur le profil d'une vraie entreprise avant votre prochaine entrevue : vingt minutes, trois questions."},

      {t:'ex', h:"Huit lignes d'un profil, et ce qu'elles valent",
       p:"À gauche ce qui est écrit, à droite ce qu'il faut en faire.",
       rows:[
         ["Fondée en 1985","à noter, mais tout le monde peut le citer"],
         ["Deux cent dix personnes","un chiffre solide, à replacer"],
         ["Aucun produit vendu au grand public","comprendre le vrai métier de l'entreprise"],
         ["Acquise en janvier par un groupe ontarien","le fait récent : le plus utile des trois"],
         ["Le carnet a doublé en dix-huit mois","explique pourquoi le poste existe"],
         ["Quatre-vingt-deux pour cent de capacité","demander ce que le taux comprend"],
         ["Un taux de roulement de onze pour cent","une pratique mesurée, pas une valeur"],
         ["Sans soutien sur place après dix-huit heures","la difficulté avouée : y répondre d'avance"],
       ]},

      {t:'piege', h:"Trois pièges de la lecture d'un profil",
       rows:[
         ["citer l'année de fondation en entrevue","citer le fait récent",
          "« Je sais que vous existez depuis 1985 » prouve qu'on a lu la première ligne. « Je sais que le carnet a doublé et que le troisième quart en découle » prouve qu'on a lu et compris."],
         ["retenir les valeurs affichées","retenir les chiffres",
          "Personne ne vous demandera de réciter les valeurs, et si on le fait, la question ne sert à rien. Les chiffres, eux, permettent de poser une vraie question."],
         ["lire en cherchant à être rassuré","lire en cherchant les trous",
          "Un profil est fait pour plaire. Le lire pour se convaincre qu'on veut y travailler ne sert à rien : ce qui sert, c'est d'en sortir trois questions."],
       ]},

      {t:'check', h:"Est-ce que c'est clair maintenant ?",
       p:"Quatre questions rapides.",
       qs:[
         {q:"Que faut-il prélever d'un profil d'entreprise ?", opts:["les valeurs affichées","un fait récent, un chiffre, une difficulté"], ok:1,
          fb:"Ces trois-là se replacent dans une réponse. Les valeurs, non."},
         {q:"« L'entreprise a été acquise en janvier » ne dit pas…", opts:["quand","par qui, et à quelle initiative"], ok:1,
          fb:"Le passif efface celui qui agit. C'est une question toute prête."},
         {q:"Comment reconnaître une phrase qui ne dit rien ?", opts:["elle est courte","sa version inverse serait absurde"], ok:1,
          fb:"Aucune entreprise n'écrit « nous méprisons l'humain » : donc la phrase ne distingue rien."},
         {q:"Une difficulté avouée dans un profil est…", opts:["un signal d'alarme","une occasion d'y répondre d'avance"], ok:1,
          fb:"Elle vous dit ce qui inquiète l'employeur. C'est le meilleur renseignement du document."},
       ]},

      {t:'revoir', h:"À retenir",
       p:"Prélevez trois choses : un <b>fait récent</b>, un <b>chiffre</b>, une <b>difficulté avouée</b>. Laissez les valeurs, qui ne distinguent rien. Notez chaque <b>passif</b> : c'est votre liste de questions. Et rappelez-vous qu'on vous posera une question tirée du profil — cela se voit en quinze secondes."},
    ]
  },

  t2offre: {
    eye:'Mini-leçon', tit:"Lire une offre d'emploi pour décider",
    blocs:[
      {t:'texte', h:"Deux documents, deux lectures",
       p:"Un profil d'entreprise se lit pour <b>prélever</b> : on y cherche des faits. Une offre d'emploi se lit pour <b>décider</b> : suis-je admissible, est-ce que je veux ces conditions, et à quoi est-ce que je m'engage exactement ? Ce sont deux gestes de lecture différents, et c'est pour cette raison que le module vous fait travailler les deux textes séparément. On peut très bien avoir tout compris d'une entreprise et se tromper complètement sur le poste.",
       note:"Lisez l'offre en entier avant d'en lire une ligne deux fois. Beaucoup de gens s'arrêtent aux exigences et ne lisent jamais les conditions."},

      {t:'texte', h:"L'erreur la plus coûteuse : s'éliminer soi-même",
       p:"Une majorité de candidats renoncent devant une exigence qu'ils croient absolue. Or presque toutes les exigences portent une porte, et cette porte tient en trois mots : « <b>ou l'équivalent</b> », « <b>ou expérience jugée pertinente</b> », « <b>ou toute expérience équivalente</b> ». Ces formules ne sont pas décoratives : elles sont écrites exprès, parce que l'employeur sait qu'il ne trouvera pas le profil idéal. Les chercher avant de renoncer est le geste le plus rentable de toute une recherche d'emploi.",
       note:"Dans l'offre de Boréalis, l'exigence dit « cinq années en supervision manufacturière, ou toute expérience jugée équivalente ». C'est cette porte-là que Shirin franchit avec ses onze années de Téhéran."},

      {t:'ana', h:"« Exigé » élimine, « atout » distingue",
       p:"Deux mots, deux poids complètement différents. Les confondre fait renoncer pour rien, ou postuler à l'aveugle.",
       mots:[['Exigé','ce qui vous écarte si vous ne l\'avez pas'],['Atout','ce qui vous distingue si vous l\'avez',true],['La règle','ne jamais renoncer faute d\'un atout']],
       say:"Ce qui est exigé vous écarte ; ce qui est un atout vous distingue.",
       note:"Un dossier sans aucun des atouts mais avec toutes les exigences passe. L'inverse ne passe pas."},

      {t:'ana', h:"Les trois mots qui ouvrent une exigence",
       p:"Cherchez-les systématiquement. Ils changent une porte fermée en porte entrebâillée.",
       mots:[['Les formules','« ou l\'équivalent » · « ou expérience jugée pertinente »'],['Ce qu\'elles disent','l\'employeur sait qu\'il ne trouvera pas l\'idéal',true],['Ce qu\'il faut faire','démontrer l\'équivalence, en chiffres']],
       say:"Cinq années en supervision, ou toute expérience jugée équivalente.",
       note:"Démontrer l'équivalence ne se fait pas en affirmant : ça se fait avec une taille d'équipe, un nombre d'années et un résultat."},

      {t:'ana', h:"Les conditions valent autant que le salaire",
       p:"Le salaire est une ligne parmi six ou sept. La probation, l'horaire, l'assurance, les vacances, la formation et le préavis pèsent parfois davantage sur une année de vie.",
       mots:[['Ce qu\'on lit','probation de six mois, assurance dès le premier jour'],['Ce qu\'on compare','ce que vous avez déjà, ligne par ligne',true],['Ce qui manque','tout ce dont l\'offre ne parle pas']],
       say:"Période de probation de six mois, assurance collective dès le premier jour.",
       note:"« Congé annuel selon la Loi sur les normes du travail » veut dire : le minimum légal. Deux semaines après un an, trois après trois ans de service continu chez le même employeur."},

      {t:'ana', h:"Ce qui n'est pas écrit se demande",
       p:"Une annonce muette sur un point n'est pas une annonce incomplète : c'est une annonce qui vous donne une question préparée, et presque personne ne s'en sert.",
       mots:[['Ce qui manque souvent','le nom du supérieur, la taille de l\'équipe, la raison du poste'],['Ce que ça vous donne','trois questions pour l\'appel',true],['L\'effet','vous êtes la seule à en poser']],
       say:"L'annonce ne dit pas pourquoi le poste a été créé. C'est ma première question.",
       note:"Dans le module, c'est exactement ce que fait Shirin : « l'équipe existe-t-elle, ou faut-il la constituer ? ». La réponse change tout le poste."},

      {t:'labo', h:"Chaque section, et ce qu'on en fait",
       p:"Choisissez une section de l'offre et un geste.",
       axes:[
         {id:'s', lbl:'Quelle section ?', opts:[['a','titre'],['b','exigences'],['c','atouts'],['d','conditions']]},
         {id:'g', lbl:'Quel geste ?', opts:[['1','ce qu\'on prend'],['2','ce qu\'on vérifie']]}],
       out:{
         a1:{w:["le titre exact"], say:"Superviseure ou superviseur de production, quart de soir.", n:'à recopier mot pour mot dans l\'objet du courriel'},
         a2:{w:["le lieu et l'horaire"], say:"Du lundi au vendredi, de quinze heures à vingt-trois heures trente.", n:'vérifier avant tout le reste'},
         b1:{w:["la porte de l'exigence"], say:"Cinq années en supervision, ou toute expérience jugée équivalente.", n:'chercher « ou l\'équivalent »'},
         b2:{w:["ce qui est vraiment obligatoire"], say:"Capacité démontrée à décider seul en dehors des heures de soutien.", n:'celle-là n\'a pas de porte'},
         c1:{w:["l'atout qu'on possède"], say:"Expérience du contrôle de la qualité en transformation alimentaire.", n:'à mettre en avant dès la lettre'},
         c2:{w:["l'atout qui révèle le besoin"], say:"Expérience du démarrage d'une équipe ou d'une ligne nouvelle.", n:'cet atout-là dit ce que le poste sera vraiment'},
         d1:{w:["la probation"], say:"Période de probation de six mois.", n:'six mois, c\'est long : le noter'},
         d2:{w:["ce que « selon la loi » veut dire"], say:"Congé annuel selon la Loi sur les normes du travail : le minimum.", n:'deux semaines, trois après trois ans'},
       },
       note:"Passez une vraie offre à ce filtre avant votre prochaine candidature : cinq minutes, et vous savez quoi demander."},

      {t:'ex', h:"Huit formules d'annonce, et ce qu'elles cachent",
       p:"À gauche ce qui est écrit, à droite ce que ça veut dire.",
       rows:[
         ["« ou toute expérience jugée équivalente »","la porte : à vous de démontrer l'équivalence"],
         ["« capacité démontrée à »","il faudra un exemple précis, pas une affirmation"],
         ["« selon l'échelle en vigueur »","le salaire n'est pas dit : question à poser"],
         ["« entrée en fonction dès que possible »","ils sont pressés — c'est une force pour vous"],
         ["« participer au recrutement »","une responsabilité absente du titre"],
         ["« selon la Loi sur les normes du travail »","le minimum légal, rien de plus"],
         ["« environnement en forte croissance »","attendez-vous à de la désorganisation"],
         ["« au plus tard le 3 novembre »","une vraie date : envoyez trois jours avant"],
       ]},

      {t:'piege', h:"Trois pièges de l'offre d'emploi",
       rows:[
         ["renoncer devant une exigence","chercher la porte d'abord",
          "« Cinq ans exigés » et vous en avez trois : lisez la phrase en entier. Si elle contient « ou l'équivalent », vous êtes admissible et c'est à l'employeur de trancher, pas à vous."],
         ["ne lire que les exigences","lire aussi les conditions",
          "La probation, l'horaire et les vacances décident de votre année. Beaucoup de gens acceptent un poste sans avoir lu la ligne qui les fera partir dans six mois."],
         ["réécrire le titre du poste avec ses propres mots","le recopier tel quel",
          "Le titre est ce que la personne cherche des yeux en ouvrant vingt dossiers. « Chef d'équipe soir » à la place de « superviseure de production, quart de soir » vous fait perdre trois secondes d'attention que vous n'avez pas."],
       ]},

      {t:'check', h:"Est-ce que c'est clair maintenant ?",
       p:"Quatre questions rapides.",
       qs:[
         {q:"Il vous manque un atout, mais vous avez toutes les exigences.", opts:["ne pas postuler","postuler"], ok:1,
          fb:"Un atout distingue, il n'élimine pas. Le dossier passe."},
         {q:"« Ou toute expérience jugée équivalente » signifie…", opts:["que l'exigence est ferme","que vous pouvez démontrer autre chose"], ok:1,
          fb:"C'est la porte. Il faut la franchir avec des chiffres, pas avec une affirmation."},
         {q:"« Congé annuel selon la Loi sur les normes du travail » veut dire…", opts:["quatre semaines","le minimum légal"], ok:1,
          fb:"Deux semaines après un an, trois après trois ans de service continu."},
         {q:"Le titre du poste, dans votre courriel…", opts:["se reformule","se recopie mot pour mot"], ok:1,
          fb:"C'est ce que la personne cherche des yeux dans une boîte pleine."},
       ]},

      {t:'revoir', h:"À retenir",
       p:"<b>Exigé</b> élimine, <b>atout</b> distingue. Cherchez toujours la porte : « ou l'équivalent », « ou expérience jugée pertinente ». Lisez les <b>conditions</b> aussi attentivement que les exigences. Ce qui n'est pas écrit devient une question. Et le titre du poste se recopie mot pour mot."},
    ]
  },

  t2conn: {
    eye:'Mini-leçon', tit:"Les mots qui articulent un raisonnement",
    blocs:[
      {t:'texte', h:"Ce que le niveau 8 demande, exactement",
       p:"Le programme du niveau 8 range sous « connecteurs et relations logiques » vingt et un points de savoir, et trois d'entre eux nomment la même famille : comprendre des connecteurs argumentatifs marquant l'<b>opposition ou la concession</b>, la <b>complémentation</b>, la <b>conclusion</b> — et en employer soi-même. Ce ne sont pas des mots de liaison décoratifs : ce sont les articulations d'un raisonnement. Une entrevue et une lettre d'affaires se jugent presque entièrement là-dessus.",
       note:"À ce niveau, on ne vous reprochera plus une faute d'accord ; on remarquera un raisonnement qui n'avance pas."},

      {t:'texte', h:"La concession, forme reine de l'entrevue",
       p:"De toutes ces familles, une seule change vraiment ce qu'on pense de vous : la <b>concession</b>. Elle consiste à donner raison à l'autre <i>avant</i> d'avancer votre argument. « Certes mon expérience a été acquise ailleurs, mais elle porte sur seize ans d'usine. » Ce mouvement en deux temps dit à votre interlocuteur que vous avez entendu son objection, que vous ne la niez pas, et que vous avez quand même quelque chose à répondre. Nier l'objection ferme la conversation ; la concéder l'ouvre.",
       note:"Shirin l'emploie deux fois dans l'entrevue : « bien que la question soit interdite, je comprends l'inquiétude », et « c'est vrai, mais incomplet » dans son courriel."},

      {t:'ana', h:"Opposer — deux faits vrais qui se contredisent",
       p:"Les deux propositions gardent le même poids : on ne choisit pas entre elles, on les met côte à côte.",
       mots:[['Les mots','en revanche · par contre · alors que · tandis que'],['L\'exemple','Aucune mise à pied ; en revanche, une réorganisation complète.',true],['La ponctuation','virgule après, point-virgule avant']],
       say:"L'acquisition n'a supprimé aucun emploi ; en revanche, elle a réorganisé la production.",
       note:"« Alors que » et « tandis que » s'emploient sans virgule devant, à l'intérieur de la phrase : « les habitudes sont installées alors que l'équipe est neuve »."},

      {t:'ana', h:"Concéder — reconnaître, puis avancer",
       p:"Deux constructions à connaître par cœur : « certes… mais » et « bien que » suivi du subjonctif. « Même si » fait la même chose, mais avec l'indicatif.",
       mots:[['Avec certes','Certes mon expérience vient d\'ailleurs, mais elle est vérifiable.'],['Avec bien que','Bien que la question soit interdite, je comprends l\'inquiétude.',true],['Avec même si','Même si le service part à dix-huit heures, la ligne tourne.']],
       say:"Certes mon expérience vient d'ailleurs, mais elle porte sur seize ans d'usine.",
       note:"Retenez la différence de mode : <b>bien que</b> + subjonctif, <b>même si</b> + indicatif. C'est la faute la plus fréquente à ce niveau."},

      {t:'ana', h:"Ajouter — empiler dans le même sens",
       p:"On accumule des arguments qui vont tous dans la même direction. Attention à la nuance entre les deux principaux.",
       mots:[['De plus','reste exactement sur le même sujet'],['Par ailleurs','ajoute en changeant légèrement d\'angle',true],['Les autres','en outre · qui plus est · de surcroît']],
       say:"Le carnet a doublé ; par ailleurs, un troisième quart a été ouvert.",
       note:"« Qui plus est » et « de surcroît » sont soutenus : parfaits à l'écrit, un peu appuyés à l'oral."},

      {t:'ana', h:"Conclure — fermer, une seule fois",
       p:"On tire la conséquence de ce qui précède. La règle absolue : une seule conclusion. Deux de suite annulent la première.",
       mots:[['Les mots','par conséquent · ainsi · c\'est pourquoi · en somme'],['L\'exemple','L\'équipe reste à bâtir ; par conséquent, le poste comporte du recrutement.',true],['L\'erreur','« donc… par conséquent… en conclusion… »']],
       say:"L'équipe reste à bâtir ; par conséquent, le poste comporte une part de recrutement.",
       note:"« En somme » et « bref » résument plutôt qu'ils ne concluent : ils rassemblent sans tirer de conséquence."},

      {t:'ana', h:"Reformuler — traduire, sans rien ajouter",
       p:"« Autrement dit », « c'est-à-dire », « en d'autres termes » ne sont pas des connecteurs d'argument : ils redisent la même chose autrement.",
       mots:[['Ce qu\'ils font','ils traduisent la phrase précédente'],['Ce qu\'ils ne font pas','ils n\'ajoutent aucune idée neuve',true],['L\'erreur','s\'en servir pour glisser un argument de plus']],
       say:"Les arrêts planifiés sont exclus ; autrement dit, ces dix points sont perdus.",
       note:"Un « autrement dit » suivi d'une idée nouvelle se remarque immédiatement : le lecteur cherche la correspondance et ne la trouve pas."},

      {t:'labo', h:"Le même couple de faits, six articulations",
       p:"Choisissez une famille et un exemple.",
       axes:[
         {id:'f', lbl:'Quelle famille ?', opts:[['a','opposition'],['b','concession'],['c','ajout'],['d','conclusion'],['e','reformulation']]},
         {id:'n', lbl:'Quel exemple ?', opts:[['1','le premier'],['2','le second']]}],
       out:{
         a1:{w:["en revanche"], say:"Aucune mise à pied ; en revanche, la production a été réorganisée.", n:'deux faits vrais, même poids'},
         a2:{w:["alors que"], say:"Les habitudes sont installées alors que l'équipe du soir est neuve.", n:'pas de virgule devant'},
         b1:{w:["certes… mais"], say:"Certes mon expérience vient d'ailleurs, mais elle est vérifiable.", n:'on donne raison, puis on avance'},
         b2:{w:["bien que"], say:"Bien que la question soit interdite, je comprends l'inquiétude.", n:'subjonctif obligatoire après bien que'},
         c1:{w:["par ailleurs"], say:"Le carnet a doublé ; par ailleurs, un troisième quart a été ouvert.", n:'on change légèrement d\'angle'},
         c2:{w:["de plus"], say:"Le carnet a doublé ; de plus, il devrait croître encore.", n:'on reste sur le même sujet'},
         d1:{w:["par conséquent"], say:"L'équipe reste à bâtir ; par conséquent, le poste comporte du recrutement.", n:'une seule conclusion par raisonnement'},
         d2:{w:["en somme"], say:"En somme, un processus plus lourd que la moyenne.", n:'on résume plutôt qu\'on ne conclut'},
         e1:{w:["autrement dit"], say:"Les arrêts planifiés sont exclus ; autrement dit, ces dix points sont perdus.", n:'on traduit, on n\'ajoute rien'},
         e2:{w:["c'est-à-dire"], say:"Le minimum légal, c'est-à-dire deux semaines après un an.", n:'on précise un terme'},
       },
       note:"Le même couple de faits change de sens selon le connecteur choisi. C'est ce choix-là qu'on évalue à ce niveau."},

      {t:'ex', h:"Neuf connecteurs, un emploi chacun",
       p:"À gauche le mot, à droite ce qu'il fait exactement.",
       rows:[
         ["en revanche","oppose deux faits de même poids"],
         ["alors que","oppose à l'intérieur de la phrase, sans virgule devant"],
         ["certes… mais","concède, puis avance — la forme de l'entrevue"],
         ["bien que + subjonctif","concède ; attention au mode"],
         ["même si + indicatif","concède aussi, mais avec l'indicatif"],
         ["par ailleurs","ajoute en changeant d'angle"],
         ["de plus","ajoute sur le même sujet"],
         ["par conséquent","conclut — une seule fois"],
         ["autrement dit","redit la même chose, sans rien ajouter"],
       ]},

      {t:'piege', h:"Trois pièges des connecteurs",
       rows:[
         ["« bien que » suivi de l'indicatif","« bien que » + subjonctif",
          "« Bien que la question est interdite » est une faute franche à ce niveau. C'est « soit ». Si le subjonctif vous coûte, employez « même si », qui prend l'indicatif et dit presque la même chose."],
         ["conclure deux fois de suite","conclure une seule fois",
          "« Donc, par conséquent, en conclusion » : trois conclusions annulent la première et donnent l'impression qu'on ne sait pas s'arrêter. Une phrase, un connecteur, et on passe à autre chose."],
         ["glisser une idée neuve derrière « autrement dit »","garder la même idée",
          "« Autrement dit » promet une traduction. Si ce qui suit est nouveau, le lecteur cherche la correspondance, ne la trouve pas, et relit — ce qui est exactement ce qu'on voulait éviter."],
       ]},

      {t:'check', h:"Est-ce que c'est clair maintenant ?",
       p:"Quatre questions rapides.",
       qs:[
         {q:"Après « bien que », quel mode ?", opts:["l'indicatif","le subjonctif"], ok:1,
          fb:"Bien que la question soit interdite. « Même si », lui, prend l'indicatif."},
         {q:"Quelle famille sert le plus en entrevue ?", opts:["la concession","l'ajout"], ok:0,
          fb:"Donner raison avant d'avancer : c'est ce mouvement qui change ce qu'on pense de vous."},
         {q:"« Autrement dit » sert à…", opts:["ajouter un argument","redire la même chose"], ok:1,
          fb:"Il traduit. Une idée neuve derrière lui se remarque immédiatement."},
         {q:"Combien de conclusions dans un raisonnement ?", opts:["une","autant qu'on veut"], ok:0,
          fb:"Deux de suite annulent la première."},
       ]},

      {t:'revoir', h:"À retenir",
       p:"Quatre familles : <b>opposer</b> (en revanche, alors que), <b>concéder</b> (certes… mais, bien que + subjonctif, même si + indicatif), <b>ajouter</b> (par ailleurs, de plus), <b>conclure</b> (par conséquent — une seule fois). Et à part : <b>reformuler</b> (autrement dit), qui ne fait que traduire. La concession est la forme qui compte le plus en entrevue."},
    ]
  },

  t2rel: {
    eye:'Mini-leçon', tit:"« Dont », « auquel », « laquelle »",
    blocs:[
      {t:'texte', h:"Le geste unique : regarder le verbe",
       p:"On croit devoir choisir entre « dont » et « auquel » à l'oreille. En réalité, on ne choisit rien : c'est le <b>verbe</b> qui décide, et il le fait toujours de la même façon. Si le verbe se construit avec <b>de</b> — parler de, s'occuper de, avoir besoin de, se souvenir de —, ce sera « dont ». S'il se construit avec <b>à</b> — participer à, penser à, répondre à, s'attendre à —, ce sera « auquel », « à laquelle », « auxquels » ou « auxquelles ». Une seconde de vérification, et la faute disparaît.",
       note:"Le test pratique : refaites la phrase simple. « Je participe <b>à</b> ce processus » → « le processus <b>auquel</b> je participe »."},

      {t:'texte', h:"Pourquoi ça compte pour lire un document d'entreprise",
       p:"Un profil d'entreprise et une offre d'emploi sont pleins de phrases longues, et ces relatifs y renvoient à quelque chose écrit trois lignes plus haut. « Les conditions auxquelles il est fait référence » ne veut rien dire tant qu'on n'a pas retrouvé les conditions. Savoir ce que reprend un « dont » n'est pas de la grammaire d'exercice : c'est ce qui vous permet de lire un contrat sans le relire trois fois.",
       note:"Le programme du niveau 8 range ces relatifs sous « reprise de l'information », et non sous « grammaire de la phrase ». C'est le bon endroit."},

      {t:'ana', h:"« Dont » — trois emplois, un seul mot",
       p:"Il remplace toujours « de + quelque chose », mais ce « de » vient de trois endroits différents.",
       mots:[['Le verbe','le poste dont je vous ai parlé — parler DE'],['Le nom','une entreprise dont le carnet a doublé — le carnet DE l\'entreprise',true],['La partie d\'un tout','seize personnes, dont neuf à recruter']],
       say:"Le poste dont je vous ai parlé comporte une part de recrutement.",
       note:"Le troisième emploi — la partie d'un tout — est le plus fréquent dans les textes d'entreprise, et le plus facile à reconnaître : il est presque toujours précédé d'une virgule."},

      {t:'ana', h:"Jamais « dont » et « de » ensemble",
       p:"« Dont » contient déjà le « de ». Le répéter est la faute la plus visible du niveau, et elle se voit à l'écrit comme à l'oral.",
       mots:[['On écrit','l\'entreprise dont le carnet a doublé'],['On n\'écrit pas','« dont son carnet » ni « dont le carnet de l\'entreprise »',true],['Le test','y a-t-il déjà un « de » caché ?']],
       say:"L'entreprise dont le carnet de commandes a doublé embauche forcément.",
       note:"Même chose avec le possessif : « dont son directeur » est faux ; on dit « dont le directeur »."},

      {t:'ana', h:"« Auquel » et sa famille s'accordent",
       p:"Quatre formes, et le genre et le nombre viennent du nom qui précède — jamais du verbe.",
       mots:[['Masculin singulier','le processus auquel je participe'],['Féminin singulier','l\'étape à laquelle je pense',true],['Pluriel','les documents auxquels · les conditions auxquelles']],
       say:"Le processus auquel je participe, l'étape à laquelle je pense.",
       note:"Notez la forme écrite : « auquel » et « auxquels » sont soudés, « à laquelle » et « auxquelles » aussi — mais « à laquelle » s'écrit en deux mots."},

      {t:'ana', h:"Après une autre préposition : lequel, laquelle",
       p:"Sur, dans, selon, pour, avec : pour une chose, on emploie la famille de « lequel ». Pour une personne, « qui » reste possible.",
       mots:[['Une chose','l\'échelle selon laquelle on paie · le document sur lequel je m\'appuie'],['Une personne','la personne avec qui j\'ai parlé',true],['Le figé','la raison pour laquelle']],
       say:"L'échelle selon laquelle les salaires sont fixés compte six échelons.",
       note:"« La raison pour laquelle » est une expression figée à retenir telle quelle : on ne dit ni « la raison que » ni « la raison pourquoi »."},

      {t:'ana', h:"La virgule qui change tout",
       p:"Une relative encadrée de virgules ajoute une information à tous ; sans virgules, elle restreint à un sous-ensemble. C'est un point de ponctuation du niveau 8.",
       mots:[['Sans virgules','Les candidats qui ont réussi l\'examen passeront l\'entrevue.'],['Avec virgules','Les candidats, qui ont réussi l\'examen, passeront l\'entrevue.',true],['La différence','seulement certains, ou bien tous']],
       say:"Les candidats qui ont réussi l'examen passeront l'entrevue.",
       note:"Dans la première phrase, une partie seulement passe. Dans la seconde, tous passent, et l'on précise au passage qu'ils ont réussi. Deux virgules, et le sens bascule."},

      {t:'labo', h:"Le verbe, puis le relatif",
       p:"Choisissez une construction et un exemple.",
       axes:[
         {id:'c', lbl:'Quelle construction ?', opts:[['a','verbe + DE'],['b','nom + DE'],['c','verbe + À'],['d','autre préposition']]},
         {id:'n', lbl:'Quel exemple ?', opts:[['1','le premier'],['2','le second']]}],
       out:{
         a1:{w:["dont je vous ai parlé"], say:"C'est le poste dont je vous ai parlé.", n:'parler DE quelque chose'},
         a2:{w:["dont j'ai besoin"], say:"Voici le document dont j'ai besoin.", n:'avoir besoin DE'},
         b1:{w:["dont le carnet a doublé"], say:"Une entreprise dont le carnet a doublé embauche forcément.", n:'le carnet DE l\'entreprise'},
         b2:{w:["dont neuf restent à recruter"], say:"Seize personnes, dont neuf restent à recruter.", n:'la partie d\'un tout'},
         c1:{w:["auquel je participe"], say:"Le processus auquel je participe compte trois étapes.", n:'participer À'},
         c2:{w:["auxquelles je m'attendais"], say:"Ce sont les conditions auxquelles je m'attendais.", n:'s\'attendre À, féminin pluriel'},
         d1:{w:["selon laquelle"], say:"L'échelle selon laquelle les salaires sont fixés compte six échelons.", n:'selon + laquelle'},
         d2:{w:["pour laquelle"], say:"Je ne connais pas la raison pour laquelle ce poste a été créé.", n:'expression figée'},
       },
       note:"À chaque fois, refaites d'abord la phrase simple avec le verbe : c'est elle qui donne la préposition."},

      {t:'ex', h:"Dix verbes, et le relatif qu'ils appellent",
       p:"À gauche le verbe, à droite le relatif.",
       rows:[
         ["parler de","dont"],
         ["avoir besoin de","dont"],
         ["s'occuper de","dont"],
         ["se souvenir de","dont"],
         ["participer à","auquel, à laquelle"],
         ["penser à","auquel, à laquelle"],
         ["répondre à","auquel, à laquelle"],
         ["s'attendre à","auquel, à laquelle"],
         ["s'appuyer sur","sur lequel, sur laquelle"],
         ["travailler avec (une personne)","avec qui"],
       ]},

      {t:'piege', h:"Trois pièges des relatifs",
       rows:[
         ["« dont son carnet »","« dont le carnet »",
          "« Dont » contient le « de » : ajouter un possessif derrière fait doublon. C'est la faute qu'un correcteur repère en premier à ce niveau."],
         ["« la raison que le poste existe »","« la raison pour laquelle »",
          "Expression figée. « La raison que » et « la raison pourquoi » n'existent ni l'une ni l'autre en français standard."],
         ["accorder « auquel » avec le verbe","l'accorder avec le nom qui précède",
          "« Les conditions auxquelles » : c'est « conditions » qui donne le féminin pluriel, pas « s'attendre ». Le verbe ne donne que la préposition."],
       ]},

      {t:'check', h:"Est-ce que c'est clair maintenant ?",
       p:"Quatre questions rapides.",
       qs:[
         {q:"« Je participe à ce processus » donne…", opts:["le processus dont je participe","le processus auquel je participe"], ok:1,
          fb:"Participer À : c'est « auquel ». Le verbe décide."},
         {q:"« Une entreprise ___ le carnet a doublé »", opts:["dont","auquel"], ok:0,
          fb:"Le carnet DE l'entreprise : c'est « dont »."},
         {q:"« Dont son directeur » est…", opts:["correct","fautif"], ok:1,
          fb:"« Dont » contient déjà le « de ». On dit « dont le directeur »."},
         {q:"« Les candidats, qui ont réussi l'examen, passeront » signifie…", opts:["seulement ceux qui ont réussi","tous, et ils ont réussi"], ok:1,
          fb:"Les deux virgules changent le sens : l'information s'ajoute, elle ne restreint pas."},
       ]},

      {t:'revoir', h:"À retenir",
       p:"Regardez le <b>verbe</b> : construit avec <b>de</b> → « dont » ; avec <b>à</b> → « auquel, à laquelle, auxquels, auxquelles ». Jamais « dont » et un second « de ». L'accord vient du <b>nom qui précède</b>. Après une autre préposition, « lequel » pour une chose, « qui » pour une personne. Et deux virgules autour d'une relative en changent le sens."},
    ]
  },

  t3irreel: {
    eye:'Mini-leçon', tit:"Ce qui ne s'est pas passé",
    blocs:[
      {t:'texte', h:"La structure, une fois pour toutes",
       p:"<b>Si</b> + <b>plus-que-parfait</b>, puis <b>conditionnel passé</b>. « Si j'avais fait vérifier l'étiquette, rien ne serait arrivé. » Cette phrase dit deux choses en même temps : la vérification n'a pas eu lieu, et l'accident a eu lieu. C'est ce qu'on appelle l'<b>irréel du passé</b> : on parle d'un passé qui n'existe pas, pour dire quelque chose du passé qui existe. C'est le dernier des grands temps composés du français, et le niveau 8 est celui où on l'exige.",
       note:"Règle absolue : jamais de conditionnel après « si ». « Si j'aurais » n'existe pas, et c'est la faute que tout francophone remarque instantanément."},

      {t:'texte', h:"Pourquoi c'est l'outil de l'entrevue",
       p:"On vous demandera de parler d'une erreur, ou de ce que vous feriez autrement. Répondre « j'aurais dû mieux vérifier » vous met en défaut. Répondre « si j'avais fait vérifier l'étiquette par une deuxième personne, ce qui prenait quatre minutes, rien de tout cela ne serait arrivé » dit exactement la même chose — mais la phrase parle d'un passé imaginaire, pas de vos limites. Vous montrez que vous avez compris, sans vous accuser. C'est précisément ce que fait Shirin devant le comité.",
       note:"Et la suite compte autant : après l'irréel, on dit la règle qu'on applique <b>depuis</b>. Sans elle, l'aveu reste un aveu."},

      {t:'ana', h:"Fabriquer le plus-que-parfait",
       p:"<b>Avoir</b> ou <b>être</b> à l'imparfait, plus le participe passé. C'est la moitié gauche de la phrase, celle qui suit « si ».",
       mots:[['Avec avoir','j\'avais fait · nous avions eu · elle avait demandé'],['Avec être','elle était partie · ils étaient restés',true],['L\'accord','avec être, accord avec le sujet']],
       say:"Si j'avais fait vérifier l'étiquette, si nous avions eu une deuxième signature.",
       note:"Le choix de l'auxiliaire est le même qu'au passé composé : si vous dites « je suis partie », vous direz « j'étais partie »."},

      {t:'ana', h:"Fabriquer le conditionnel passé",
       p:"<b>Avoir</b> ou <b>être</b> au conditionnel, plus le même participe passé. C'est la moitié droite.",
       mots:[['Avec avoir','j\'aurais fait · nous aurions perdu · on aurait proposé'],['Avec être','elle serait allée · rien ne serait arrivé',true],['Le repère','le participe ne change pas, l\'auxiliaire oui']],
       say:"Rien ne serait arrivé, nous aurions perdu la commande.",
       note:"Comparez : « j'avais fait » et « j'aurais fait ». Un seul mot bouge entre les deux moitiés de la phrase."},

      {t:'ana', h:"Deux étages, à ne pas mélanger",
       p:"L'irréel du présent parle d'aujourd'hui ; l'irréel du passé parle d'un moment révolu. Les deux structures se ressemblent et ne disent pas la même chose.",
       mots:[['Irréel du présent','Si j\'étais superviseure, je ferais autrement. (imparfait + conditionnel présent)'],['Irréel du passé','Si j\'avais été superviseure, j\'aurais fait autrement. (plus-que-parfait + conditionnel passé)',true],['La différence','aujourd\'hui, ou un moment fini']],
       say:"Si j'étais superviseure, je ferais autrement. Si j'avais été superviseure, j'aurais fait autrement.",
       note:"Un étage de plus des deux côtés : c'est le seul changement. Ne mélangez jamais les étages — « si j'avais été, je ferais » boite."},

      {t:'ana', h:"L'accord du participe, quand même",
       p:"Il ne disparaît pas parce que la phrase est compliquée. Avec « être », accord avec le sujet ; avec « avoir », accord seulement avec un complément direct placé devant.",
       mots:[['Avec être','elle serait partie · les caisses seraient restées'],['Avec avoir + CD devant','les caisses que nous aurions reprises',true],['Avec avoir, sinon','nous aurions repris les caisses — pas d\'accord']],
       say:"Les caisses que nous aurions reprises, elles seraient restées au quai.",
       note:"L'accord du participe passé avec avoir est un savoir explicite du niveau 8 : il est attendu, et il se voit."},

      {t:'labo', h:"La condition, puis la conséquence",
       p:"Choisissez une situation et une moitié de phrase.",
       axes:[
         {id:'s', lbl:'Quelle situation ?', opts:[['a','l\'étiquette'],['b','le rachat'],['c','l\'échelle'],['d','la ligne arrêtée']]},
         {id:'m', lbl:'Quelle moitié ?', opts:[['1','la condition'],['2','la conséquence']]}],
       out:{
         a1:{w:["si j'avais fait vérifier"], say:"Si j'avais fait vérifier l'étiquette par une deuxième personne…", n:'plus-que-parfait après si'},
         a2:{w:["rien ne serait arrivé"], say:"…rien de tout cela ne serait arrivé.", n:'conditionnel passé'},
         b1:{w:["si le groupe n'avait pas racheté"], say:"Si le groupe n'avait pas racheté l'usine…", n:'la négation encadre l\'auxiliaire'},
         b2:{w:["le poste n'aurait jamais existé"], say:"…le poste n'aurait jamais existé.", n:'« jamais » se place entre l\'auxiliaire et le participe'},
         c1:{w:["si vous m'aviez communiqué l'échelle"], say:"Si vous m'aviez communiqué l'échelle…", n:'plus-que-parfait, deuxième personne'},
         c2:{w:["j'aurais préparé une contre-proposition"], say:"…j'aurais préparé une contre-proposition.", n:'conditionnel passé, première personne'},
         d1:{w:["si la ligne était restée arrêtée"], say:"Si la ligne était restée arrêtée…", n:'auxiliaire être : accord avec le sujet'},
         d2:{w:["nous aurions perdu la commande"], say:"…nous aurions perdu la commande.", n:'auxiliaire avoir : pas d\'accord ici'},
       },
       note:"Assemblez les deux moitiés à voix haute : c'est la longueur de la phrase entière qu'il faut apprendre à tenir."},

      {t:'ex', h:"Huit phrases d'entrevue à l'irréel du passé",
       p:"À gauche la phrase, à droite ce qu'elle vous évite de dire.",
       rows:[
         ["Si j'avais fait vérifier, rien ne serait arrivé.","« j'ai été négligente »"],
         ["Si j'avais eu les données, j'aurais arrêté plus tôt.","« je n'ai pas su décider »"],
         ["Si on m'avait prévenue, j'aurais réorganisé le quart.","« personne ne me dit rien »"],
         ["Si j'avais parlé français dès la première année…","« j'ai perdu trois ans »"],
         ["Si j'avais demandé, on m'aurait peut-être proposé mieux.","« mon employeur m'a bloquée »"],
         ["Si nous n'avions pas repris les caisses, l'affaire serait allée plus loin.","« ça s'est mal terminé »"],
         ["Si vous m'aviez communiqué l'échelle, j'aurais préparé une proposition.","« vous ne jouez pas franc jeu »"],
         ["Si le groupe n'avait pas racheté l'usine, ce poste n'existerait pas.","rien : c'est un simple constat lucide"],
       ]},

      {t:'piege', h:"Trois pièges de l'irréel",
       rows:[
         ["« si j'aurais »","« si j'avais »",
          "Aucun conditionnel après « si », jamais, à aucun temps. C'est la faute que tous les francophones remarquent, y compris ceux qui n'ont aucune idée de ce qu'est un plus-que-parfait."],
         ["mélanger les deux étages","garder le même niveau des deux côtés",
          "« Si j'avais été superviseure, je ferais autrement » boite : la condition est au passé, la conséquence au présent. Soit les deux au présent, soit les deux au passé."],
         ["s'arrêter après l'irréel","ajouter la règle qu'on applique depuis",
          "« Si j'avais vérifié, rien ne serait arrivé » laisse l'histoire ouverte sur une faute. « Depuis, aucune étiquette ne part sans deux signatures » la referme sur une compétence."],
       ]},

      {t:'check', h:"Est-ce que c'est clair maintenant ?",
       p:"Quatre questions rapides.",
       qs:[
         {q:"Après « si », dans l'irréel du passé, on met…", opts:["le conditionnel passé","le plus-que-parfait"], ok:1,
          fb:"Si + plus-que-parfait. Le conditionnel est toujours dans l'autre moitié."},
         {q:"« Si j'avais été superviseure, je ferais autrement »", opts:["est correct","mélange deux étages"], ok:1,
          fb:"Condition au passé, conséquence au présent : la phrase boite."},
         {q:"« Si j'avais vérifié, rien ne serait arrivé » dit que…", opts:["la vérification a eu lieu","la vérification n'a pas eu lieu"], ok:1,
          fb:"L'irréel dit toujours que la condition ne s'est pas réalisée."},
         {q:"Après avoir raconté une erreur à l'irréel, il faut…", opts:["s'excuser","dire la règle qu'on applique depuis"], ok:1,
          fb:"Sans la règle, l'histoire reste un aveu. Avec elle, c'est une preuve de jugement."},
       ]},

      {t:'revoir', h:"À retenir",
       p:"<b>Si</b> + <b>plus-que-parfait</b>, puis <b>conditionnel passé</b>. Jamais de conditionnel après « si ». Ne mélangez pas les étages : présent avec présent, passé avec passé. L'accord du participe suit ses règles habituelles. Et terminez toujours par la règle que vous appliquez depuis."},
    ]
  },

  t3subj: {
    eye:'Mini-leçon', tit:"Le subjonctif, et les endroits où il ne va pas",
    blocs:[
      {t:'texte', h:"Ce qu'il fait, en une idée",
       p:"L'indicatif présente un fait ; le subjonctif présente un fait <b>filtré par quelqu'un</b> — par une volonté, un sentiment, un doute, une concession. « Il est important » n'affirme rien du monde : c'est un jugement, et ce qui suit passe donc au subjonctif. Ce n'est pas une difficulté supplémentaire du français : c'est une information de plus, et vous la donnez déjà en persan, en espagnol ou en arabe d'une autre manière.",
       note:"Au niveau 8, le programme en demande neuf points, dont l'emploi obligatoire après les verbes introducteurs, les adjectifs, les conjonctions et les expressions impersonnelles."},

      {t:'texte', h:"La stratégie qui marche : apprendre les déclencheurs",
       p:"On n'apprend pas le subjonctif en réfléchissant au sens à chaque phrase — c'est trop lent pour une conversation. On l'apprend par ses <b>déclencheurs</b> : une trentaine de mots après lesquels il est automatique. « Il faut que », « bien que », « pour que », « je voudrais que », « avant que », « à moins que ». Apprenez les mots, pas la théorie. Et apprenez aussi les cinq ou six exceptions, qui sont peu nombreuses et qui trahissent.",
       note:"Six formes couvrent la moitié des emplois réels : que je sois, que j'aie, que j'aille, que je fasse, que je puisse, que je sache."},

      {t:'ana', h:"Après les verbes de volonté, de sentiment, de doute",
       p:"Ces verbes ne rapportent pas un fait : ils réagissent à quelque chose. Ce qui suit passe au subjonctif.",
       mots:[['Volonté','Je tiens à ce que ce soit écrit. · Je souhaite qu\'on regarde.'],['Sentiment','Je crains que la question revienne.',true],['Doute','Je doute qu\'ils puissent répondre vendredi.']],
       say:"Je tiens à ce que ce soit écrit dans la lettre.",
       note:"Attention : « espérer que » est une exception célèbre et demande l'<b>indicatif</b> — « j'espère que vous rappellerez »."},

      {t:'ana', h:"Après une expression impersonnelle",
       p:"« Il faut que », « il est important que », « il se peut que », « il est possible que » : toutes appellent le subjonctif. Deux exceptions à retenir par cœur.",
       mots:[['La règle','Il faudrait que je sache. · Il se peut qu\'ils rappellent.'],['Les deux exceptions','il paraît que + indicatif · il me semble que + indicatif',true],['Le repère','ces deux-là rapportent, elles ne jugent pas']],
       say:"Il faudrait que je sache ce que l'examen évalue.",
       note:"« Il paraît que le groupe veut ouvrir une deuxième usine » : on rapporte une information, on ne la filtre pas. D'où l'indicatif."},

      {t:'ana', h:"Après certaines conjonctions",
       p:"Une liste courte, à apprendre telle quelle. Et une autre liste, tout aussi courte, de celles qui prennent l'indicatif.",
       mots:[['Subjonctif','bien que · quoique · pour que · afin que · avant que · à moins que · sans que'],['Indicatif','après que · même si · pendant que · parce que',true],['Le couple à ne pas rater','bien que + subjonctif, même si + indicatif']],
       say:"Bien que la question soit interdite, je comprends l'inquiétude.",
       note:"« Bien que » et « même si » disent presque la même chose et ne prennent pas le même mode. Si le subjonctif vous coûte, employez « même si »."},

      {t:'ana', h:"Après un verbe d'opinion à la forme négative",
       p:"C'est le point le plus fin du niveau, et presque personne ne l'emploie. Affirmer une opinion garde l'indicatif ; la nier ouvre le doute, donc le subjonctif.",
       mots:[['Affirmé','Je crois qu\'il a raison.'],['Nié','Je ne crois pas qu\'il ait raison.',true],['Aussi','Je ne pense pas que ce soit nécessaire.']],
       say:"Je ne crois pas qu'ils puissent répondre avant vendredi.",
       note:"Employé une fois en entrevue, ce tour se remarque — dans le bon sens. Il montre une maîtrise que la plupart des candidats n'ont pas."},

      {t:'ana', h:"Après un adjectif + que, sauf les adjectifs de certitude",
       p:"« Il est possible que », « je suis heureuse que » appellent le subjonctif. « Il est certain que », « il est évident que » gardent l'indicatif.",
       mots:[['Subjonctif','Je suis heureuse que vous m\'ayez reçue.'],['Indicatif','Il est certain qu\'elle viendra.',true],['La logique','la certitude n\'a rien à filtrer']],
       say:"Je suis heureuse que vous m'ayez reçue si rapidement.",
       note:"Les adjectifs de certitude : certain, sûr, évident, clair, exact, vrai. Tous les autres appellent le subjonctif."},

      {t:'labo', h:"Le déclencheur, et le mode",
       p:"Choisissez un déclencheur et un exemple.",
       axes:[
         {id:'d', lbl:'Quel déclencheur ?', opts:[['a','verbe de volonté'],['b','impersonnel'],['c','conjonction'],['d','opinion niée'],['e','adjectif']]},
         {id:'n', lbl:'Quel exemple ?', opts:[['1','subjonctif'],['2','exception']]}],
       out:{
         a1:{w:["je tiens à ce que ce soit écrit"], say:"Je tiens à ce que ce soit écrit dans la lettre.", n:'volonté : subjonctif'},
         a2:{w:["j'espère que vous rappellerez"], say:"J'espère que vous rappellerez vendredi.", n:'espérer que : indicatif, exception célèbre'},
         b1:{w:["il faudrait que je sache"], say:"Il faudrait que je sache ce que l'examen évalue.", n:'impersonnel : subjonctif'},
         b2:{w:["il paraît que le groupe veut"], say:"Il paraît que le groupe veut ouvrir une usine.", n:'il paraît que : indicatif'},
         c1:{w:["bien que la question soit interdite"], say:"Bien que la question soit interdite, je comprends l'inquiétude.", n:'bien que : subjonctif'},
         c2:{w:["même si l'équipe est incomplète"], say:"Même si l'équipe est incomplète, la production continue.", n:'même si : indicatif'},
         d1:{w:["je ne crois pas qu'ils puissent"], say:"Je ne crois pas qu'ils puissent répondre avant vendredi.", n:'opinion niée : subjonctif'},
         d2:{w:["je crois qu'ils peuvent"], say:"Je crois qu'ils peuvent répondre avant vendredi.", n:'opinion affirmée : indicatif'},
         e1:{w:["je suis heureuse que vous m'ayez reçue"], say:"Je suis heureuse que vous m'ayez reçue si rapidement.", n:'adjectif ordinaire : subjonctif'},
         e2:{w:["il est certain qu'elle viendra"], say:"Il est certain qu'elle viendra.", n:'adjectif de certitude : indicatif'},
       },
       note:"Écoutez chaque paire : la seconde est toujours l'exception. Ce sont les exceptions qui trahissent, pas la règle."},

      {t:'ex', h:"Six formes irrégulières à savoir sans réfléchir",
       p:"À gauche l'infinitif, à droite le subjonctif présent.",
       rows:[
         ["être","que je sois · que nous soyons · qu'ils soient"],
         ["avoir","que j'aie · que nous ayons · qu'ils aient"],
         ["aller","que j'aille · que nous allions · qu'ils aillent"],
         ["faire","que je fasse · que nous fassions · qu'ils fassent"],
         ["pouvoir","que je puisse · que nous puissions · qu'ils puissent"],
         ["savoir","que je sache · que nous sachions · qu'ils sachent"],
       ]},

      {t:'piege', h:"Trois pièges du subjonctif",
       rows:[
         ["« bien que la question est interdite »","« bien que la question soit interdite »",
          "La conjonction la plus utile de l'entrevue est aussi celle où la faute se fait le plus. Si vous doutez, remplacez par « même si », qui prend l'indicatif."],
         ["« j'espère qu'il soit disponible »","« j'espère qu'il sera disponible »",
          "« Espérer » ressemble à « souhaiter » et se comporte à l'inverse. C'est une exception qu'il faut apprendre séparément, parce qu'aucune logique ne la donne."],
         ["employer le subjonctif partout par prudence","le réserver aux déclencheurs",
          "« Je pense que ce soit intéressant » est une hypercorrection : le subjonctif y est faux. Une opinion affirmée garde l'indicatif ; seule la négation le change."],
       ]},

      {t:'check', h:"Est-ce que c'est clair maintenant ?",
       p:"Quatre questions rapides.",
       qs:[
         {q:"« Bien que » et « même si » prennent…", opts:["le même mode","des modes différents"], ok:1,
          fb:"Bien que + subjonctif, même si + indicatif. C'est le couple à ne pas rater."},
         {q:"« J'espère que… » prend…", opts:["le subjonctif","l'indicatif"], ok:1,
          fb:"Exception célèbre : j'espère que vous rappellerez."},
         {q:"« Je ne crois pas qu'il ___ raison »", opts:["a","ait"], ok:1,
          fb:"L'opinion niée ouvre le doute, donc le subjonctif."},
         {q:"« Il est certain qu'elle ___ »", opts:["vienne","viendra"], ok:1,
          fb:"Adjectif de certitude : indicatif. La certitude n'a rien à filtrer."},
       ]},

      {t:'revoir', h:"À retenir",
       p:"Apprenez les <b>déclencheurs</b>, pas la théorie : verbes de volonté, de sentiment et de doute ; expressions impersonnelles ; <b>bien que, pour que, avant que, à moins que</b> ; opinion <b>niée</b> ; adjectifs sauf ceux de certitude. Et les exceptions qui trahissent : <b>espérer que</b>, <b>il paraît que</b>, <b>il me semble que</b>, <b>après que</b>, <b>même si</b> — toutes à l'indicatif."},
    ]
  },

  t3emph: {
    eye:'Mini-leçon', tit:"Décider vous-même de ce qui est important",
    blocs:[
      {t:'texte', h:"Le problème que ça règle",
       p:"« J'apporte seize ans d'usine » est une phrase plate : elle donne l'information et laisse à l'autre le soin de décider si elle compte. « Ce que j'apporte, c'est seize ans d'usine » décide à sa place. Le contenu est identique ; l'attention ne l'est pas. Dans une conversation de quarante-cinq minutes où l'on retient trois phrases, choisir soi-même lesquelles seront ces trois-là n'est pas un ornement de style : c'est une compétence de production orale, et le programme du niveau 8 la nomme.",
       note:"Deux constructions suffisent : la <b>dislocation</b> (on détache et on reprend par un pronom) et l'<b>extraction</b> (c'est… qui, ce que… c'est)."},

      {t:'texte', h:"À employer avec parcimonie",
       p:"Une emphase par réponse, deux au maximum dans une entrevue entière. Le procédé fonctionne parce qu'il rompt la régularité ; trois de suite et il devient la régularité, donc il ne souligne plus rien. C'est la seule vraie difficulté de ce point de langue : non pas le construire, mais résister à l'employer partout une fois qu'on l'a appris.",
       note:"Choisissez d'avance vos deux phrases-clés — ce que vous apportez, et ce que vous demandez. Ce sont celles-là qui méritent la mise en relief."},

      {t:'ana', h:"La dislocation à gauche",
       p:"On sort un groupe en tête de phrase, séparé par une virgule, et on le reprend derrière par un pronom.",
       mots:[['Complément direct','Ce poste-là, je le veux.'],['Complément en « de »','De cette erreur, j\'en ai tiré une règle.',true],['Complément en « à »','À vos neuf recrues, j\'y pense depuis trois jours.']],
       say:"Ce poste-là, je le veux.",
       note:"Le pronom se choisit comme d'habitude : <b>le, la, les</b> pour un complément direct, <b>en</b> pour « de », <b>y</b> pour « à »."},

      {t:'ana', h:"La dislocation à droite",
       p:"La même chose à l'envers : le pronom d'abord, le groupe rejeté à la fin. C'est plus oral, et parfait pour appuyer une fin de réponse.",
       mots:[['On dit','Je le veux, ce poste-là.'],['Autre exemple','Elle y tient, à cette condition.',true],['L\'effet','le dernier mot reste dans l\'oreille']],
       say:"Je le veux, ce poste-là.",
       note:"À l'écrit, la dislocation à droite fait très parlé : gardez-la pour l'oral, et préférez la gauche dans un courriel."},

      {t:'ana', h:"L'extraction par « c'est… qui » et « c'est… que »",
       p:"On encadre le groupe à mettre en avant. « Qui » si ce groupe est le sujet, « que » dans tous les autres cas.",
       mots:[['Sujet → qui','C\'est moi qui avais approuvé l\'étiquette.'],['Autre fonction → que','C\'est le raisonnement que vous regardez.',true],['L\'accord','c\'est moi qui ai · c\'est nous qui avons']],
       say:"C'est moi qui avais approuvé l'étiquette.",
       note:"Le verbe s'accorde avec le mot mis en avant, pas avec « c'est » : « c'est moi qui <b>ai</b> décidé », jamais « qui a décidé »."},

      {t:'ana', h:"L'extraction par « ce que…, c'est »",
       p:"La construction la plus utile en entrevue. Trois formes selon ce que réclame le verbe.",
       mots:[['Complément direct','Ce que je demande, c\'est une contrepartie.'],['Sujet','Ce qui m\'intéresse, c\'est l\'équipe à bâtir.',true],['Complément en « de »','Ce dont j\'ai besoin, c\'est d\'une date.']],
       say:"Ce que je demande, c'est une contrepartie.",
       note:"Le choix entre « ce que », « ce qui » et « ce dont » se fait sur le verbe qui suit, exactement comme pour les relatifs du défi 2."},

      {t:'labo', h:"La phrase plate, et sa mise en relief",
       p:"Choisissez une phrase et une construction.",
       axes:[
         {id:'p', lbl:'Quelle phrase ?', opts:[['a','seize ans d\'usine'],['b','une contrepartie'],['c','l\'étiquette'],['d','ce poste']]},
         {id:'c', lbl:'Quelle forme ?', opts:[['1','plate'],['2','mise en relief']]}],
       out:{
         a1:{w:["j'apporte seize ans d'usine"], say:"J'apporte seize ans d'usine.", n:'l\'information, sans hiérarchie'},
         a2:{w:["ce que j'apporte, c'est seize ans d'usine"], say:"Ce que j'apporte, c'est seize ans d'usine.", n:'vous décidez de ce qui compte'},
         b1:{w:["je demande une contrepartie"], say:"Je demande une contrepartie.", n:'plat'},
         b2:{w:["ce que je demande, c'est une contrepartie"], say:"Ce que je demande, c'est une contrepartie.", n:'la demande devient claire et unique'},
         c1:{w:["j'avais approuvé l'étiquette"], say:"J'avais approuvé l'étiquette.", n:'plat'},
         c2:{w:["c'est moi qui avais approuvé l'étiquette"], say:"C'est moi qui avais approuvé l'étiquette.", n:'on assume, et ça s\'entend'},
         d1:{w:["je veux ce poste"], say:"Je veux ce poste.", n:'plat'},
         d2:{w:["ce poste-là, je le veux"], say:"Ce poste-là, je le veux.", n:'dislocation à gauche : le groupe puis le pronom'},
       },
       note:"Écoutez les deux versions à la suite. La différence ne tient pas aux mots, elle tient à ce qui reste après."},

      {t:'ex', h:"Huit phrases d'entrevue mises en relief",
       p:"À gauche la phrase, à droite la construction employée.",
       rows:[
         ["Ce que j'apporte, c'est seize ans d'usine.","ce que…, c'est"],
         ["Ce qui m'intéresse, c'est l'équipe à bâtir.","ce qui…, c'est"],
         ["Ce dont j'ai besoin, c'est d'une date.","ce dont…, c'est"],
         ["C'est moi qui avais approuvé l'étiquette.","c'est… qui, avec accord"],
         ["C'est le raisonnement que vous regardez.","c'est… que"],
         ["Ce poste-là, je le veux.","dislocation à gauche"],
         ["De cette erreur, j'en ai tiré une règle.","dislocation avec « en »"],
         ["Je le veux, ce poste-là.","dislocation à droite"],
       ]},

      {t:'piege', h:"Trois pièges de la mise en relief",
       rows:[
         ["« c'est moi qui a décidé »","« c'est moi qui ai décidé »",
          "Le verbe s'accorde avec le mot mis en avant. « Moi » est une première personne : donc « ai ». La faute est très fréquente et très audible."],
         ["oublier le pronom de reprise","le placer",
          "« Ce poste-là, je veux » n'est pas une phrase. La dislocation détache un groupe et laisse un vide : le pronom bouche le vide. Le, en ou y, selon le verbe."],
         ["mettre trois phrases en relief de suite","en garder deux pour toute l'entrevue",
          "Le procédé marche parce qu'il rompt la régularité. Employé partout, il redevient la régularité — et vous avez l'air de réciter."],
       ]},

      {t:'check', h:"Est-ce que c'est clair maintenant ?",
       p:"Quatre questions rapides.",
       qs:[
         {q:"« C'est moi qui ___ approuvé l'étiquette »", opts:["a","ai"], ok:1,
          fb:"Le verbe s'accorde avec « moi », première personne."},
         {q:"« Ce poste-là, je ___ veux »", opts:["le","en"], ok:0,
          fb:"« Vouloir quelque chose » : complément direct, donc « le »."},
         {q:"« Ce ___ j'ai besoin, c'est d'une date »", opts:["que","dont"], ok:1,
          fb:"Avoir besoin DE : c'est « ce dont »."},
         {q:"Combien de mises en relief dans une entrevue ?", opts:["une ou deux","à chaque réponse"], ok:0,
          fb:"Le procédé s'use. Deux phrases-clés, choisies d'avance."},
       ]},

      {t:'revoir', h:"À retenir",
       p:"Deux outils. La <b>dislocation</b> : on détache un groupe et on le reprend par <b>le, en</b> ou <b>y</b>. L'<b>extraction</b> : « c'est… qui » pour un sujet, « c'est… que » sinon, et « ce que / ce qui / ce dont…, c'est » selon le verbe. Accordez le verbe avec le mot mis en avant. Et n'en employez pas plus de deux."},
    ]
  },

  t3interdit: {
    eye:'Mini-leçon', tit:"Les questions qu'on n'a pas le droit de vous poser",
    blocs:[
      {t:'texte', h:"La règle, et où elle se trouve",
       p:"Au Québec, l'article 18.1 de la <b>Charte des droits et libertés de la personne</b> interdit à quiconque d'exiger, dans un formulaire de demande d'emploi ou lors d'une entrevue, un renseignement portant sur l'un des motifs de discrimination énumérés à l'article 10. Ce n'est pas une règle de politesse ni une pratique d'entreprise : c'est une loi québécoise, elle s'applique à tous les employeurs, et elle couvre <b>toutes</b> les étapes — le formulaire, l'examen préembauche, l'entrevue.",
       note:"C'est la Commission des droits de la personne et des droits de la jeunesse qui reçoit les plaintes en matière de discrimination à l'embauche."},

      {t:'texte', h:"Pourquoi ce n'est pas un savoir de citoyenneté mais de langue",
       p:"On pourrait croire que ce point relève du cours de citoyenneté. Il relève d'abord de votre cours de français, pour une raison précise : ce qui est difficile n'est pas de savoir que la question est interdite — c'est de <b>répondre</b>. Il faut, en trois secondes, ne pas se soumettre, ne pas se fâcher, ne pas mentir, et ne pas perdre le poste. Cela demande une phrase construite d'avance, et cette phrase est un objet de langue.",
       note:"Shirin en donne le modèle dans le module. Relisez sa réponse : elle répond à l'inquiétude, puis elle ferme le reste, et elle ne s'excuse pas."},

      {t:'ana', h:"Les quatorze motifs de l'article 10",
       p:"Aucun d'eux ne peut faire l'objet d'une question en entrevue, sauf si le renseignement est fondé sur les aptitudes ou qualités requises par l'emploi.",
       mots:[['Personne','la race, la couleur, le sexe, l\'identité ou l\'expression de genre, la grossesse, l\'orientation sexuelle'],['Situation','l\'état civil, l\'âge, la condition sociale, le handicap',true],['Origine et opinions','la religion, les convictions politiques, la langue, l\'origine ethnique ou nationale']],
       say:"La race, la couleur, le sexe, l'âge, la religion, l'origine ethnique ou nationale.",
       note:"« L'âge, sauf dans la mesure prévue par la loi » : on peut vérifier qu'une personne a l'âge légal pour un emploi qui l'exige, et rien de plus."},

      {t:'ana', h:"L'exception, et sa limite exacte",
       p:"Une question redevient permise quand le renseignement est fondé sur les <b>aptitudes ou qualités requises par l'emploi</b>. C'est étroit, et ça se vérifie phrase par phrase.",
       mots:[['Permis','Pouvez-vous soulever des caisses de vingt kilos ?'],['Interdit','Avez-vous un problème de dos ?',true],['La différence','on demande ce que le poste exige, jamais l\'état de la personne']],
       say:"Pouvez-vous soulever des caisses de vingt kilos de façon répétée ?",
       note:"Le test qui marche : la question porte-t-elle sur la <b>tâche</b>, ou sur la <b>personne</b> ? La tâche est permise, la personne ne l'est pas."},

      {t:'ana', h:"Les deux questions jumelles",
       p:"Presque toutes les questions interdites ont une jumelle permise qui cherche exactement le même renseignement utile. C'est là qu'il faut ramener la conversation.",
       mots:[['Interdit','Avez-vous des enfants en bas âge ?'],['Permis','Êtes-vous disponible de quinze heures à vingt-trois heures trente ?',true],['Ce que ça vous dit','l\'employeur cherche la disponibilité, pas les enfants']],
       say:"Êtes-vous disponible de quinze heures à vingt-trois heures trente, cinq jours par semaine ?",
       note:"Reconnaître la jumelle est ce qui rend la réponse facile : vous répondez à la vraie inquiétude, et vous laissez tomber le reste."},

      {t:'ana', h:"La phrase à préparer d'avance",
       p:"Trois temps, et pas un de plus. On répond à l'inquiétude, on ferme le reste, on ne s'excuse pas.",
       mots:[['Temps 1','Je vais vous répondre sur ce qui vous intéresse : je suis disponible cinq jours sur cinq.'],['Temps 2','Pour le reste, je préfère ne pas répondre.',true],['Temps 3','on enchaîne sur autre chose, sans silence']],
       say:"Je vais vous répondre sur ce qui vous intéresse. Pour le reste, je préfère ne pas répondre.",
       note:"Le ton compte autant que les mots : mélodie descendante, calme, sans reproche. On ne se plaint pas ; on referme."},

      {t:'labo', h:"La question interdite, et sa jumelle permise",
       p:"Choisissez un sujet et une version.",
       axes:[
         {id:'s', lbl:'Quel sujet ?', opts:[['a','la famille'],['b','la santé'],['c','l\'origine'],['d','la religion']]},
         {id:'v', lbl:'Quelle version ?', opts:[['1','interdite'],['2','permise']]}],
       out:{
         a1:{w:["Avez-vous des enfants ?"], say:"Avez-vous des enfants en bas âge à la maison ?", n:'état civil et situation familiale : interdit'},
         a2:{w:["Êtes-vous disponible de soir ?"], say:"Êtes-vous disponible de quinze heures à vingt-trois heures trente ?", n:'la disponibilité : permis'},
         b1:{w:["Avez-vous un problème de dos ?"], say:"Avez-vous déjà eu un problème de dos ?", n:'handicap : interdit'},
         b2:{w:["Pouvez-vous soulever vingt kilos ?"], say:"Pouvez-vous soulever des caisses de vingt kilos de façon répétée ?", n:'l\'aptitude requise : permis'},
         c1:{w:["Dans quel pays êtes-vous née ?"], say:"Dans quel pays êtes-vous née ?", n:'origine nationale : interdit'},
         c2:{w:["Êtes-vous autorisée à travailler au Canada ?"], say:"Êtes-vous légalement autorisée à travailler au Canada ?", n:'une condition d\'emploi : permis'},
         d1:{w:["Votre religion vous empêche-t-elle de travailler le soir ?"], say:"Est-ce que votre religion vous empêcherait de travailler certains soirs ?", n:'religion : interdit'},
         d2:{w:["Y a-t-il des dates où vous ne seriez pas disponible ?"], say:"Y a-t-il des dates auxquelles vous ne seriez pas disponible cette année ?", n:'la disponibilité, encore : permis'},
       },
       note:"Chaque paire cherche le même renseignement utile. Une seule des deux a le droit de le chercher."},

      {t:'ex', h:"Huit questions, et de quel côté elles tombent",
       p:"À gauche la question, à droite le verdict.",
       rows:[
         ["Êtes-vous disponible cinq jours par semaine ?","permise — porte sur la tâche"],
         ["Avez-vous des enfants en bas âge ?","interdite — état civil"],
         ["Avez-vous déjà supervisé plus de quinze personnes ?","permise — l'expérience du poste"],
         ["Quel âge avez-vous ?","interdite — l'âge"],
         ["Êtes-vous autorisée à travailler au Canada ?","permise — une condition d'emploi"],
         ["Dans quel pays êtes-vous née ?","interdite — origine nationale"],
         ["Accepteriez-vous une formation de deux jours à Mississauga ?","permise — une exigence du poste"],
         ["Prévoyez-vous une grossesse cette année ?","interdite — grossesse"],
       ]},

      {t:'piege', h:"Trois pièges au moment de répondre",
       rows:[
         ["répondre pour ne pas déplaire","répondre à la jumelle permise",
          "Répondre à une question interdite ne vous protège pas : cela installe le renseignement dans la salle, où il servira à quelqu'un sans que vous le sachiez. Vous n'êtes pas obligée, et refuser ne peut pas vous être reproché."],
         ["citer la loi et se fâcher","nommer la chose une fois, calmement",
          "« Vous n'avez pas le droit de me demander ça » est exact et coûte l'entrevue. La formule qui marche est plus douce et tout aussi ferme : « pour le reste, je préfère ne pas répondre »."],
         ["mentir","ne rien dire sur le sujet",
          "Un mensonge découvert plus tard peut justifier un congédiement. Le silence, lui, est un droit. La distance entre les deux est toute la différence."],
       ]},

      {t:'check', h:"Est-ce que c'est clair maintenant ?",
       p:"Quatre questions rapides.",
       qs:[
         {q:"Quel texte interdit ces questions ?", opts:["la Loi sur les normes du travail","la Charte des droits et libertés de la personne"], ok:1,
          fb:"L'article 18.1 de la Charte, qui renvoie aux motifs de l'article 10."},
         {q:"« Pouvez-vous soulever vingt kilos ? » est…", opts:["permise","interdite"], ok:0,
          fb:"Elle porte sur une aptitude requise par l'emploi, pas sur la personne."},
         {q:"Refuser de répondre à une question interdite…", opts:["peut vous être reproché","ne peut pas vous être reproché"], ok:1,
          fb:"C'est un droit. Le silence sur ces sujets ne se retourne pas contre vous."},
         {q:"La meilleure réponse consiste à…", opts:["citer la loi","répondre à l'inquiétude réelle, puis fermer"], ok:1,
          fb:"On répond à la disponibilité, et on dit calmement qu'on préfère ne pas répondre au reste."},
       ]},

      {t:'revoir', h:"À retenir",
       p:"L'article <b>18.1</b> de la Charte interdit toute question portant sur les quatorze motifs de l'article 10, à toutes les étapes. L'exception est étroite : le renseignement doit être fondé sur une <b>aptitude requise par l'emploi</b>. Chaque question interdite a une jumelle permise : répondez à celle-là, puis fermez le reste sans vous excuser."},
    ]
  },

  t3courriel: {
    eye:'Mini-leçon', tit:"Le courriel qui suit l'entrevue",
    blocs:[
      {t:'texte', h:"D'où vient cette tâche",
       p:"La situation « Recherche d'emploi » du niveau 8 ne comporte <b>aucune</b> intention de production écrite : trois intentions, toutes orales ou en compréhension. Ce courriel vient donc des <b>attentes de fin de cours</b>, qui demandent que l'adulte « rédige des lettres ou des courriels d'affaires ayant des objectifs particuliers en s'assurant que leur forme et leur contenu sont appropriés », et qu'il « résume les propos de son interlocuteur ». C'est écrit ici pour qu'on ne prenne pas cette tâche pour une invention hors programme.",
       note:"C'est aussi, en pratique, l'écrit le plus rentable de toute une recherche d'emploi — et presque personne ne l'envoie."},

      {t:'texte', h:"Ce qu'il fait vraiment",
       p:"On l'appelle « courriel de remerciement », et c'est trompeur : remercier occupe une phrase. Le vrai travail du courriel est ailleurs. Il vous donne une <b>deuxième chance</b> sur un point, un seul, que vous avez mal expliqué — et vous savez toujours lequel, parce que vous y avez repensé dans l'auto en rentrant. Il met aussi par écrit ce qui a été convenu de vive voix. Ce qui n'est pas écrit se rediscute ; ce qui est écrit ne se rediscute plus.",
       note:"Le moment compte : dans les vingt-quatre heures. Passé deux jours, il arrive après la décision et ne sert plus qu'à faire poli."},

      {t:'ana', h:"L'objet — retrouvable dans six semaines",
       p:"Il reprend le titre du poste tel qu'il est écrit dans l'annonce, et il porte une date. Pas de « Merci », pas de « Suivi ».",
       mots:[['On écrit','Entrevue du 25 octobre — poste de superviseure de production, quart de soir'],['On n\'écrit pas','« Merci ! » ou « Ma candidature »',true],['Pourquoi','une boîte de réception contient trois cents messages']],
       say:"Entrevue du vingt-cinq octobre, poste de superviseure de production, quart de soir.",
       note:"Un objet précis se retrouve par une recherche six semaines plus tard, quand un poste semblable s'ouvre. Un objet vague est perdu le jour même."},

      {t:'ana', h:"Le premier paragraphe — remercier, une phrase",
       p:"Court, précis, daté. On ne s'étend pas : la longueur du remerciement ne mesure pas la sincérité, elle mesure l'embarras.",
       mots:[['On écrit','Je vous remercie du temps que vous m\'avez accordé hier après-midi.'],['On n\'écrit pas','trois phrases de gratitude',true],['Le repère','une phrase, et on passe au travail']],
       say:"Je vous remercie du temps que vous m'avez accordé hier après-midi.",
       note:"Nommez les deux personnes dans l'appel de formule si le comité était à deux : « Madame Éthier, Monsieur Bourbonnais, »."},

      {t:'ana', h:"Le deuxième paragraphe — la reprise, en trois mouvements",
       p:"C'est le cœur du courriel. On annonce qu'on revient sur un point, on dit ce qu'on a répondu, puis on complète avec des faits vérifiables.",
       mots:[['Annoncer','Je souhaiterais revenir sur un point que j\'ai mal expliqué.'],['Concéder','C\'est vrai, mais incomplet.',true],['Compléter','j\'ai formé onze opérateurs et rédigé deux fiches de démarrage']],
       say:"Je souhaiterais revenir sur un point que j'ai mal expliqué.",
       note:"Notez la concession : on ne se dédit pas, on complète. Se contredire par écrit après coup fait bien pire que la réponse imparfaite de la veille."},

      {t:'ana', h:"Le troisième paragraphe — confirmer et rester joignable",
       p:"On remet par écrit ce qui a été convenu, sans en changer un mot, et on donne un numéro de téléphone.",
       mots:[['Confirmer','Comme convenu, je vous fais parvenir les attestations traduites.'],['Rester joignable','Je demeure disponible pour toute précision, au 819 555-0148.',true],['Ne pas faire','ajouter une demande qu\'on n\'a pas osé formuler']],
       say:"Comme convenu, je vous fais parvenir en pièce jointe les attestations traduites.",
       note:"« Comme convenu » est une formule de travail, pas une politesse : elle rappelle qu'un accord existe, et elle le fige."},

      {t:'labo', h:"Chaque paragraphe, et son travail",
       p:"Choisissez un paragraphe et un aspect.",
       axes:[
         {id:'p', lbl:'Quel paragraphe ?', opts:[['a','l\'objet'],['b','le remerciement'],['c','la reprise'],['d','la confirmation']]},
         {id:'a', lbl:'Quel aspect ?', opts:[['1','ce qu\'on écrit'],['2','l\'erreur à éviter']]}],
       out:{
         a1:{w:["Entrevue du 25 octobre — poste de superviseure"], say:"Entrevue du vingt-cinq octobre, poste de superviseure de production.", n:'retrouvable dans six semaines'},
         a2:{w:["« Merci ! »"], say:"Merci !", n:'introuvable le lendemain'},
         b1:{w:["Je vous remercie du temps accordé hier."], say:"Je vous remercie du temps que vous m'avez accordé hier après-midi.", n:'une phrase, datée'},
         b2:{w:["trois phrases de gratitude"], say:"Je tiens à vous remercier chaleureusement, encore une fois, du temps précieux.", n:'la longueur mesure l\'embarras'},
         c1:{w:["Je souhaiterais revenir sur un point."], say:"Je souhaiterais revenir sur un point que j'ai mal expliqué.", n:'on annonce, puis on complète avec des faits'},
         c2:{w:["revenir sur trois points"], say:"Je souhaiterais revenir sur trois points de notre entretien.", n:'trois reprises se lisent comme une entrevue ratée'},
         d1:{w:["Comme convenu, je vous fais parvenir…"], say:"Comme convenu, je vous fais parvenir les attestations traduites.", n:'ce qui est écrit ne se rediscute plus'},
         d2:{w:["une demande nouvelle"], say:"J'aimerais par ailleurs revenir sur la question du salaire.", n:'négocier par courriel ce qu\'on n\'a pas osé dire se retourne toujours'},
       },
       note:"Un seul point de reprise, jamais trois. C'est la règle la plus importante de tout ce courriel."},

      {t:'ex', h:"Les huit pièces d'un courriel d'affaires",
       p:"À gauche la pièce, à droite ce qu'elle fait.",
       rows:[
         ["L'objet, avec le titre du poste et la date","rend le message retrouvable"],
         ["L'appel de formule, avec les deux noms","dit à qui l'on parle"],
         ["Le remerciement, une phrase","referme l'entrevue"],
         ["L'annonce de la reprise","prévient qu'on revient sur un point"],
         ["Les faits vérifiables","remplacent l'affirmation par la preuve"],
         ["La confirmation de ce qui est convenu","fige l'accord"],
         ["La disponibilité et le numéro","rend la réponse facile"],
         ["La formule de clôture et la signature","tient le registre jusqu'au bout"],
       ]},

      {t:'piege', h:"Trois pièges du courriel de suivi",
       rows:[
         ["revenir sur trois points","revenir sur un seul",
          "Trois reprises se lisent comme un aveu d'entrevue ratée, et le lecteur se demande ce que vous avez encore mal dit. Choisissez celui qui pèse, et laissez les deux autres."],
         ["ajouter une demande nouvelle","confirmer seulement",
          "Négocier par écrit ce qu'on n'a pas osé demander en personne se retourne toujours contre celui qui écrit : il paraît avoir attendu d'être seul devant son clavier."],
         ["l'envoyer trois jours plus tard","l'envoyer le lendemain matin",
          "Le comité écrit ses notes dans les vingt-quatre heures. Après, votre message arrive sur une décision déjà prise et ne change plus rien."],
       ]},

      {t:'check', h:"Est-ce que c'est clair maintenant ?",
       p:"Quatre questions rapides.",
       qs:[
         {q:"Le vrai travail du courriel de suivi est…", opts:["remercier","reprendre un point mal expliqué"], ok:1,
          fb:"Le remerciement occupe une phrase. Le reste travaille."},
         {q:"Combien de points reprend-on ?", opts:["un seul","autant qu'on veut"], ok:0,
          fb:"Trois reprises se lisent comme un aveu d'entrevue ratée."},
         {q:"Peut-on y ajouter une demande qu'on n'a pas osé formuler ?", opts:["oui, c'est le moment","non, jamais"], ok:1,
          fb:"Le courriel confirme et complète. Il n'ouvre pas."},
         {q:"Quand faut-il l'envoyer ?", opts:["dans les vingt-quatre heures","dans la semaine"], ok:0,
          fb:"Le comité écrit ses notes tout de suite. Après, c'est trop tard."},
       ]},

      {t:'revoir', h:"À retenir",
       p:"Un <b>objet</b> retrouvable. Un <b>remerciement</b> d'une phrase. <b>Un seul</b> point repris, annoncé, concédé, puis complété par des faits vérifiables. Une <b>confirmation</b> de ce qui a été convenu, mot pour mot. Un numéro de téléphone. Et tout cela dans les vingt-quatre heures."},
    ]
  },

};
