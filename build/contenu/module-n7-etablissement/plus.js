const PLUS = {

  // ── JE DÉCOUVRE ─────────────────────────────────────────────

  prFiche: {
    eye:'Mini-leçon', tit:"Lire une fiche de programme jusqu'au bas de la page",
    blocs:[
      {t:'texte', h:"Le haut d'une fiche donne envie, le bas engage",
       p:"Une fiche de programme est écrite pour deux lectures. La première prend deux minutes : le métier, la durée, la photo. La seconde prend dix minutes et se fait un crayon à la main : les conditions d'admission, les préalables, ce qu'il faut faire après le diplôme. Presque personne ne fait la seconde, et c'est pourtant elle qui décide si vous pouvez vous inscrire — et quand.",
       note:"Une fiche ne cache rien. Elle range simplement l'important là où l'œil ne va pas : au bas, en petits caractères, sous des titres administratifs."},

      {t:'ana', h:"Ce qu'il faut avoir AVANT",
       p:"Les conditions d'admission d'un diplôme d'études professionnelles ont trois portes, et la troisième existe pour les personnes qui n'ont pas fait leur secondaire ici.",
       mots:[['Première porte','le diplôme d\'études secondaires, ou un diplôme reconnu équivalent'],
             ['Deuxième porte','16 ans au 30 septembre, et les unités demandées du secondaire', true],
             ['Troisième porte','18 ans et les préalables fonctionnels, avec le test de développement général']],
       say:"Les conditions d'admission ont trois portes, et la troisième est celle du test de développement général.",
       note:"Le test de développement général ne doit être précédé d'aucun exercice préparatoire ni d'aucun prétest : c'est une règle du ministère, et elle explique pourquoi personne ne vous vendra jamais un cours de préparation."},

      {t:'ana', h:"Ce qui vient APRÈS le diplôme",
       p:"Pour plusieurs métiers, le diplôme n'est pas le dernier papier. Un ordre professionnel délivre le droit d'exercer, et il ajoute ses propres conditions.",
       mots:[['Le diplôme','il atteste que la formation est réussie'],
             ['Le permis','il est délivré par l\'ordre professionnel, pas par l\'école', true],
             ['Ce qu\'il faut de plus','réussir l\'examen professionnel de l\'ordre']],
       say:"Le diplôme atteste la formation ; c'est l'ordre professionnel qui délivre le permis.",
       note:"Le savoir d'avance change le plan de carrière qu'on présente en entrevue : on annonce deux étapes au lieu d'une, et le comité entend quelqu'un qui a lu jusqu'au bout."},

      {t:'ana', h:"Combien de places, et pour combien de demandes",
       p:"Un programme contingenté classe les dossiers. Le nombre de places et le nombre de demandes de l'année précédente sont presque toujours écrits quelque part, et ils changent la façon de préparer sa candidature.",
       mots:[['Ce que ça veut dire','on n\'est pas comparé à une note de passage, on est comparé aux autres'],
             ['Ce que ça change','tout ce qui distingue compte, y compris ce qui n\'est pas scolaire', true],
             ['Ce que ça ne veut pas dire','être refusé ne veut pas dire être insuffisant']],
       say:"Un programme contingenté ne compare pas à une note de passage : il compare les dossiers entre eux.",
       note:"C'est la phrase qui fait la différence entre se décourager et recommencer l'an prochain avec une case de plus."},

      {t:'ex', h:'Sept lignes de fiche, et ce qu\'elles veulent dire',
       p:"À gauche, ce qui est écrit. À droite, ce qu'il faut en faire.",
       rows:[
         ["« 1 800 heures, temps plein, jour »","On ne peut pas garder cinq quarts de travail : l'horaire se règle avant, pas après."],
         ["« Mène au métier d'infirmière auxiliaire »","Vérifier tout de suite s'il y a un ordre professionnel."],
         ["« Examen professionnel de l'Ordre »","Une étape de plus après le diplôme : à nommer dans son plan de carrière."],
         ["« DES ou diplôme reconnu équivalent »","Première porte : la plus simple, quand on l'a."],
         ["« 16 ans au 30 septembre + unités »","Deuxième porte : ce sont les unités du secondaire d'ici qui comptent."],
         ["« Préalables fonctionnels, TDG »","Troisième porte : celle qui s'ouvre à 18 ans sans diplôme d'ici."],
         ["« 24 places, 68 demandes »","Programme contingenté : la lettre et l'entrevue décideront."],
       ]},

      {t:'check', h:'Quatre questions sur la fiche du Ruisseau-Vert',
       p:"Répondez sans relire le document.",
       qs:[
         {q:"Le diplôme suffit-il pour exercer le métier ?", opts:["oui","non, il faut aussi le permis de l'Ordre"], ok:1,
          fb:"Le permis est délivré par l'Ordre, et il exige de réussir son examen professionnel."},
         {q:"Une personne de 19 ans sans unités du secondaire d'ici…", opts:["ne peut pas s'inscrire","peut passer par les préalables fonctionnels"], ok:1,
          fb:"C'est la troisième porte : le test de développement général, à partir de 18 ans."},
         {q:"Peut-on se préparer au test de développement général ?", opts:["oui, avec un prétest","non, aucun exercice préparatoire ne doit le précéder"], ok:1,
          fb:"La règle est claire, et elle vaut pour tout le Québec."},
         {q:"« Contingenté » veut dire…", opts:["difficile","plus de demandes que de places"], ok:1,
          fb:"Le classement, pas la difficulté. On peut être bon et rester quatrième."},
       ]},

      {t:'piege', h:'Trois lignes qu\'on lit trop vite',
       rows:[
         ["lire « mène au métier de… » et s'arrêter là","chercher le mot « ordre », « permis » ou « examen » plus bas",
          "Une année entière de formation peut se terminer sur la découverte qu'il reste un examen à passer."],
         ["croire qu'une expérience de travail remplace un préalable","vérifier la case, puis demander comment la remplir",
          "L'expérience compte pour le comité, jamais pour la condition d'admission. Ce sont deux guichets différents."],
         ["ne pas noter le nombre de places","le chercher, et lire le nombre de demandes de l'an dernier",
          "Deux chiffres changent complètement la façon d'écrire sa lettre : vingt-quatre places pour soixante-huit demandes, ce n'est pas un formulaire, c'est une candidature."],
       ]},

      {t:'revoir', h:'À retenir',
       p:"Trois questions à poser à n'importe quelle fiche : <b>qu'est-ce qu'il faut avoir avant</b> (les trois portes de l'admission), <b>combien de temps et à quel rythme</b> (l'horaire se règle avant), <b>le diplôme suffit-il pour travailler</b> (l'ordre professionnel et son examen). Les trois réponses sont toujours écrites, jamais mises en avant."},
    ]
  },

  prReg: {
    eye:'Mini-leçon', tit:'Familier, standard, soutenu — et lequel choisir',
    blocs:[
      {t:'texte', h:"Ce n'est pas une question de politesse, mais de distance",
       p:"Les trois niveaux de langue sont polis. Ce qui les sépare, c'est la distance qu'ils supposent entre les personnes. Le familier suppose qu'on se connaît ; le standard, qu'on se parle pour une raison ; le soutenu, qu'on ne se connaîtra pas. Employer le familier avec un comité de sélection, ce n'est pas être impoli : c'est proposer une intimité que personne n'a offerte, et cela se remarque plus qu'une faute d'accord.",
       note:"Le programme du niveau 7 demande de « reconnaître les variétés de langue dans la situation de communication et d'en tenir compte ». Reconnaître d'abord : le choix vient tout seul ensuite."},

      {t:'ana', h:"Ce qui trahit le familier",
       p:"Trois marques, et elles se repèrent à l'oreille avant de se comprendre.",
       mots:[['La question sans marque',"« Ça commence quand, la job ? » — ni « est-ce que », ni inversion"],
             ['Les mots tronqués',"la job, le prof, le stage de sec quatre", true],
             ['Le « ne » qui tombe',"« J'ai pas eu de nouvelles » au lieu de « je n'ai pas eu »"]],
       say:"Ça commence quand, la job ? J'ai pas eu de nouvelles.",
       note:"Le familier n'est pas fautif : il est juste entre proches. Rania le parle avec Ghyslaine et personne n'y trouve à redire."},

      {t:'ana', h:"Ce qui trahit le soutenu",
       p:"Des formules figées, un vocabulaire abstrait, des phrases longues. À l'oral il sonne récité ; dans une lettre formelle, il est exactement à sa place.",
       mots:[['Les formules',"« Veuillez agréer… », « Je vous saurais gré de… »"],
             ['Le vocabulaire',"prendre connaissance, formuler une demande, accuser réception", true],
             ['Le piège',"réciter du soutenu en entrevue fait l'effet d'un masque"]],
       say:"Je vous saurais gré de bien vouloir accuser réception de mon dossier.",
       note:"Écrivez soutenu, parlez standard. C'est la répartition la plus sûre, et c'est celle que le centre emploie avec vous."},

      {t:'ana', h:"Le standard, celui de l'entrevue",
       p:"Phrases complètes, « ne » de négation prononcé, vouvoiement, questions avec « est-ce que » ou par inversion, aucun mot coupé.",
       mots:[['La question',"« À quel moment la formation commence-t-elle ? »"],
             ['La négation entière',"« Je n'ai reçu aucune nouvelle depuis le 12 mars. »", true],
             ['Le remerciement',"« Je vous remercie de m'avoir reçue ce matin. »"]],
       say:"Je vous remercie de m'avoir reçue ce matin.",
       note:"Le standard n'est pas un français appauvri : c'est celui des documents officiels, de la radio et des rencontres professionnelles."},

      {t:'labo', h:'La même chose, dans les trois niveaux',
       p:"Choisissez ce que vous voulez dire, puis à qui.",
       axes:[
         {id:'q', lbl:'Vous voulez…', opts:[['r','remercier'],['d','demander une date'],['n','dire que vous êtes sans nouvelles']]},
         {id:'a', lbl:'À qui parlez-vous ?', opts:[['f','à une collègue'],['s','au comité, en personne'],['e','au centre, par écrit']]}],
       out:{
         rf:{w:["Merci ben, là, c'était le fun."], say:"Merci ben, là, c'était le fun.", n:'familier — entre collègues, personne n\'y trouve à redire'},
         rs:{w:["Je vous remercie de m'avoir reçue ce matin."], say:"Je vous remercie de m'avoir reçue ce matin.", n:'standard — le niveau de l\'entrevue'},
         re:{w:["Je vous remercie de l'attention portée à ma candidature."], say:"Je vous remercie de l'attention portée à ma candidature.", n:'soutenu — la lettre'},
         df:{w:["Ça commence quand, la job ?"], say:"Ça commence quand, la job ?", n:'familier — question sans marque interrogative'},
         ds:{w:["À quel moment la formation commence-t-elle ?"], say:"À quel moment la formation commence-t-elle ?", n:'standard — l\'inversion suffit, sans effort'},
         de:{w:["Pourriez-vous me préciser la date du début de la formation ?"], say:"Pourriez-vous me préciser la date du début de la formation ?", n:'soutenu — le conditionnel de politesse par écrit'},
         nf:{w:["J'ai pas eu de nouvelles pantoute."], say:"J'ai pas eu de nouvelles pantoute.", n:'familier — le « ne » tombe, et « pantoute » est d\'ici'},
         ns:{w:["Je n'ai reçu aucune nouvelle depuis l'entrevue du 12 mars."], say:"Je n'ai reçu aucune nouvelle depuis l'entrevue du 12 mars.", n:'standard — la négation entière, et une date'},
         ne:{w:["À ce jour, je n'ai reçu aucune communication au sujet de ma candidature."], say:"À ce jour, je n'ai reçu aucune communication au sujet de ma candidature.", n:'soutenu — impersonnel, sans reproche'},
       },
       note:"Remarquez que le contenu ne change jamais : c'est la distance qui change. Une même personne emploie les trois dans la même journée."},

      {t:'check', h:'Quatre décisions de niveau',
       p:"Choisissez ce qui convient à la situation.",
       qs:[
         {q:"Au téléphone avec le secrétariat du centre :", opts:["« Bonjour, c'est Rania, j'appelle pour ma job. »","« Bonjour, Rania Nassar, dossier 41-2887. »"], ok:1,
          fb:"Standard : nom complet, numéro de dossier, phrase entière."},
         {q:"Dans la lettre de motivation, pour fermer :", opts:["« Merci beaucoup pour votre temps ! »","« Veuillez agréer, Madame, Monsieur, mes salutations distinguées. »"], ok:1,
          fb:"La lettre formelle se ferme sur une formule de courtoisie, pas sur un remerciement."},
         {q:"En entrevue, pour dire qu'on n'a pas compris :", opts:["« Hein ? »","« Pardon, pourriez-vous répéter la question ? »"], ok:1,
          fb:"Standard, avec un conditionnel de politesse. Faire répéter est normal."},
         {q:"Avec une collègue, à la pause :", opts:["« Je vous saurais gré de me transmettre l'horaire. »","« Tu m'enverras l'horaire ? »"], ok:1,
          fb:"Le soutenu entre collègues sonne faux, et il met de la distance là où il n'en faut pas."},
       ]},

      {t:'piege', h:'Trois glissements qui se remarquent',
       rows:[
         ["laisser tomber le « ne » en entrevue","le prononcer, même si personne d'autre ne le fait",
          "À l'oral courant, tout le monde le laisse tomber. En entrevue, il vous coûte un dixième de seconde et il s'entend."],
         ["employer « appliquer » pour une candidature","dire « poser sa candidature », « soumettre son dossier »",
          "« J'ai appliqué sur le programme » vient de l'anglais et se remarque immédiatement dans un centre de formation."],
         ["forcer le soutenu à l'oral","garder les formules pour la lettre",
          "Une phrase de trois subordonnées récitée en entrevue fait l'effet inverse de celui qu'on cherche : le comité entend qu'elle a été apprise par cœur."],
       ]},

      {t:'revoir', h:'À retenir',
       p:"Trois niveaux, trois distances. Le <b>familier</b> pour qui vous connaît ; le <b>standard</b> pour l'entrevue, le téléphone et le comptoir ; le <b>soutenu</b> pour la lettre. La règle qui simplifie tout : tenez-vous un cran <b>au-dessus</b> du niveau de l'autre, jamais un cran en dessous."},
    ]
  },

  prE: {
    eye:'Mini-leçon', tit:"Le « e » qu'on garde et le « e » qui tombe",
    blocs:[
      {t:'texte', h:"Le petit son qui décide de la longueur d'un mot",
       p:"Le français d'ici laisse tomber beaucoup de « e » : on dit « s'maine », « j'te l'dis », « pt'être ». Mais il y a des endroits où le « e » se maintient toujours, et les rater rend un mot méconnaissable. Ce ne sont pas des exceptions à apprendre une par une : ce sont deux règles, et elles tiennent en deux lignes.",
       note:"Le programme du niveau 7 range ce point sous « système prosodique » : maintenir le e quand il est suivi de [rj] ou [lj], et dans la syllabe initiale quand celle-ci commence par une consonne occlusive."},

      {t:'ana', h:"Première règle : le « e » devant un « ri » ou un « li »",
       p:"Quand le « e » est suivi d'un son « ri » ou « li » — l'écrit « rions », « rier », « lier » —, il se garde toujours. Sans lui, le mot devient imprononçable.",
       mots:[['On garde',"nous se-rions · vous fe-riez · un ate-lier · un ouv-rier"],
             ['On entend la différence',"« nous serions » a trois syllabes, jamais deux", true],
             ['Où ça se produit',"le conditionnel de « nous » et de « vous », et les noms en -ier, -lier, -rier"]],
       say:"Nous serions disponibles, et vous feriez le stage à l'atelier.",
       note:"C'est la règle qui compte le plus en entrevue : le conditionnel de politesse à « nous » et à « vous » y revient sans arrêt."},

      {t:'ana', h:"Deuxième règle : le « e » de la première syllabe après p, t, k, b, d, g",
       p:"Quand le mot commence par une consonne dure — p, t, c/qu, b, d, g — suivie d'un « e », ce « e » se maintient.",
       mots:[['On garde',"te-nir · de-mander · pe-tite · que-relle · de-venir"],
             ['On laisse tomber ailleurs',"s(e)maine · r(e)garder · c(e)pendant · j(e) le dis", true],
             ['Le test',"prononcez sans le « e » : si la bouche bloque, il faut le garder"]],
       say:"Il faut tenir bon et demander une petite précision.",
       note:"Ce sont des consonnes qui ferment complètement la bouche — on les appelle occlusives. Après elles, l'enchaînement sans « e » est impossible à dire vite."},

      {t:'labo', h:'Écoutez les deux traitements',
       p:"Choisissez un mot, puis la façon de le dire.",
       axes:[
         {id:'m', lbl:'Quel mot ?', opts:[['a','serions'],['b','demander'],['c','semaine']]},
         {id:'t', lbl:'Comment ?', opts:[['g','le e gardé'],['p','le e tombé']]}],
       out:{
         ag:{w:["nous serions disponibles"], say:"Nous serions disponibles dès septembre.", n:'la bonne forme : le e est suivi de « rions », il se garde'},
         ap:{w:["nous srions"], say:"Nous serions disponibles dès septembre.", n:'impossible à dire, et c\'est justement pourquoi la règle existe'},
         bg:{w:["demander une précision"], say:"Je voudrais demander une précision.", n:'la bonne forme : « d » est une occlusive, le e se maintient'},
         bp:{w:["dmander une précision"], say:"Je voudrais demander une précision.", n:'la bouche bloque sur « dm » : le e est obligatoire'},
         cg:{w:["une semaine complète"], say:"Il reste une semaine complète avant l'entrevue.", n:'on peut le garder, mais personne ne le fait à l\'oral courant'},
         cp:{w:["une s'maine complète"], say:"Il reste une semaine complète avant l'entrevue.", n:'la forme normale d\'ici : « s » n\'est pas une occlusive, le e tombe'},
       },
       note:"Écoutez d'abord sans lire. Ce qui se travaille ici est le nombre de syllabes, pas les lettres."},

      {t:'ex', h:'Huit mots du module',
       p:"À gauche le mot, à droite ce qui se passe.",
       rows:[
         ["nous serions","le e se garde — suivi de « rions »"],
         ["vous feriez","le e se garde — suivi de « riez »"],
         ["un atelier","le e se garde — suivi de « lier »"],
         ["un ouvrier","le e se garde — suivi de « rier »"],
         ["tenir, devenir","le e se garde — première syllabe après une occlusive"],
         ["demander, petite","le e se garde — même règle"],
         ["une semaine","le e tombe — « s » n'est pas une occlusive"],
         ["je le dis, samedi","le e tombe — l'oral courant d'ici"],
       ]},

      {t:'check', h:'Quatre mots, gardé ou tombé',
       p:"Dites sans écouter.",
       qs:[
         {q:"« vous feriez »", opts:["le e se garde","le e tombe"], ok:0,
          fb:"Suivi de « riez » : trois syllabes, toujours."},
         {q:"« samedi matin »", opts:["le e se garde","le e tombe"], ok:1,
          fb:"« Sam'di » : c'est la forme normale, à l'oral comme à la radio."},
         {q:"« demander »", opts:["le e se garde","le e tombe"], ok:0,
          fb:"Après un « d », la bouche ne peut pas enchaîner sans lui."},
         {q:"« vous me rappelez »", opts:["le e se garde","le e tombe"], ok:1,
          fb:"« Vous m'rappelez » : le « m » n'est pas une occlusive."},
       ]},

      {t:'piege', h:'Trois erreurs de débit',
       rows:[
         ["dire « nous srions » pour aller vite","garder le e devant « rions » et « riez »",
          "C'est le mot le plus fréquent du conditionnel de politesse : il vaut la peine d'être dit au complet."],
         ["prononcer tous les « e » pour être clair","laisser tomber ceux qui tombent",
          "Un français où tous les « e » sont dits sonne récité, et il ralentit tellement le débit qu'il devient plus difficile à suivre, pas plus facile."],
         ["croire que c'est du relâchement","c'est la prononciation standard d'ici",
          "La radio de Radio-Canada dit « s'maine ». Ce n'est ni familier ni négligé."],
       ]},

      {t:'revoir', h:'À retenir',
       p:"Deux règles. Le <b>e se garde</b> devant un son « ri » ou « li » — <i>se-rions, fe-riez, ate-lier, ouv-rier</i> — et dans la <b>première syllabe</b> après p, t, c, b, d, g — <i>te-nir, de-mander, pe-tite</i>. Partout ailleurs, il tombe, et c'est la prononciation normale du Québec."},
    ]
  },

  // ── DÉFI 1 · LA LETTRE DE MOTIVATION ────────────────────────

  t1lettre: {
    eye:'Mini-leçon', tit:"La lettre de motivation, paragraphe par paragraphe",
    blocs:[
      {t:'texte', h:"Elle répond à une question que personne n'écrit",
       p:"Le formulaire demande vos coordonnées, vos diplômes et vos disponibilités. La lettre, elle, répond à la seule question que le comité se pose vraiment : pourquoi vous, et pas la personne suivante ? Une lettre qui explique pourquoi le métier est beau répond à côté — les soixante-sept autres candidatures le trouvent beau aussi.",
       note:"Le programme du niveau 7 range ce travail sous « assurer la structure et la progression des différents types d'informations dans une lettre formelle ». Structure et progression : trois paragraphes, un par idée, dans un ordre qui ne se change pas."},

      {t:'ana', h:"Premier paragraphe : ce que je demande, et pourquoi ici",
       p:"Deux phrases, pas plus. La demande, puis une raison qui ne pourrait pas être écrite pour un autre établissement.",
       mots:[['La demande',"« Je vous soumets ma candidature au programme… pour l'entrée du mois d'août. »"],
             ['La raison propre au centre',"« … parce que le premier stage y a lieu avant Noël. »", true],
             ['Ce qu\'on évite',"« Votre établissement a une excellente réputation. » — vrai partout, donc nulle part"]],
       say:"Je vous soumets ma candidature au programme, pour l'entrée du mois d'août.",
       note:"Cette raison-là se trouve en lisant la fiche du programme. Dix minutes de lecture, une phrase que personne d'autre n'écrira."},

      {t:'ana', h:"Deuxième paragraphe : les faits, et le trou expliqué",
       p:"Un fait daté vaut trois adjectifs. Et s'il manque quelque chose au parcours, c'est ici qu'on le dit — une phrase, sans excuse, sans détour.",
       mots:[['L\'adjectif qui ne prouve rien',"« Je suis patiente, responsable et à l'écoute. »"],
             ['Le fait qui prouve',"« Depuis cinq ans, à l'unité prothétique, j'accompagne douze résidents. »", true],
             ['Le trou, en une phrase',"« L'établissement a fermé pendant ma troisième année ; je n'ai pas obtenu de diplôme. »"]],
       say:"Depuis cinq ans, à l'unité prothétique, j'accompagne douze résidents.",
       note:"Ce qui inquiète un comité n'est jamais le trou : c'est de le découvrir tout seul, après avoir lu la lettre. Expliqué, il devient un renseignement de plus ; caché, il devient un doute."},

      {t:'ana', h:"Troisième paragraphe : où je vais, et ce que je fais déjà",
       p:"C'est celui qui distingue, et c'est celui que presque personne n'écrit. Une formation contingentée cherche des personnes qui finissent.",
       mots:[['Où je vais',"« Après le diplôme, je souhaite obtenir mon permis de l'Ordre. »"],
             ['Ce que je fais déjà',"« Je suis, depuis janvier, un cours de français écrit le mercredi soir. »", true],
             ['Ce qui est réglé',"« J'ai obtenu par écrit le passage à deux quarts de fin de semaine. »"]],
       say:"Après le diplôme, je souhaite obtenir mon permis de l'Ordre.",
       note:"« Ce que je fais déjà » est la phrase la plus forte de toute la lettre : elle prouve que le projet existait avant la candidature."},

      {t:'ex', h:'Sept parties, et ce que chacune fait',
       p:"L'ordre ne se change pas.",
       rows:[
         ["Le lieu et la date","Permettent de dire, six semaines plus tard : « ma lettre du 26 février »."],
         ["L'objet","Six ou sept mots, sans verbe conjugué."],
         ["La formule d'appel","« Madame, Monsieur, » quand on ne sait pas qui lira."],
         ["Paragraphe 1","La demande, et pourquoi cet établissement-là."],
         ["Paragraphe 2","Les faits datés, et le trou expliqué."],
         ["Paragraphe 3","L'après-diplôme, et ce qui est déjà commencé."],
         ["La formule de courtoisie","Ferme sans rien demander de plus."],
       ]},

      {t:'check', h:'Quatre choix de rédaction',
       p:"Laquelle des deux entre dans la lettre ?",
       qs:[
         {q:"Pour l'objet :", opts:["« Je souhaiterais vous soumettre ma candidature au programme de santé, assistance et soins infirmiers pour l'année prochaine »","« Candidature au programme Santé, assistance et soins infirmiers »"], ok:1,
          fb:"Un objet n'est pas une phrase : c'est une étiquette."},
         {q:"Pour dire qu'on est fiable :", opts:["« Je suis une personne responsable. »","« Depuis cinq ans, je n'ai manqué aucun quart de travail. »"], ok:1,
          fb:"Le fait se vérifie ; l'adjectif se déclare."},
         {q:"Pour la formation non terminée :", opts:["ne pas en parler","l'expliquer en une phrase et passer à la suite"], ok:1,
          fb:"Elle paraîtra de toute façon au relevé de notes joint."},
         {q:"Pour finir :", opts:["« Merci beaucoup pour votre temps ! »","« Veuillez agréer, Madame, Monsieur, mes salutations distinguées. »"], ok:1,
          fb:"On ne remercie pas d'avance de ce qui n'a pas encore été accordé."},
       ]},

      {t:'piege', h:'Trois lettres sur quatre font ceci',
       rows:[
         ["raconter le métier au lieu de se raconter","chaque phrase doit contenir un fait qui vous appartient",
          "« Le métier d'infirmière auxiliaire est essentiel » : le comité le sait, et cette phrase ne lui apprend rien sur vous."],
         ["accumuler les adjectifs","un fait daté, un chiffre, un lieu",
          "Trois adjectifs occupent une ligne et ne prouvent rien. Une date et un nombre occupent la même ligne et se vérifient."],
         ["oublier le troisième paragraphe","dire où l'on va et ce qu'on fait déjà",
          "C'est le paragraphe qui sépare deux dossiers autrement identiques, et c'est celui qu'on saute quand on écrit tard le soir."],
       ]},

      {t:'revoir', h:'À retenir',
       p:"Trois paragraphes, un par idée : <b>ce que je demande et pourquoi ici</b> · <b>les faits datés, et le trou expliqué en une phrase</b> · <b>où je vais après le diplôme et ce que je fais déjà</b>. Un fait daté vaut trois adjectifs, et la question à laquelle la lettre répond n'est jamais écrite sur le formulaire."},
    ]
  },

  t1topic: {
    eye:'Mini-leçon', tit:'Annoncer son sujet : quant à, en ce qui concerne, à l\'égard de',
    blocs:[
      {t:'texte', h:"Les mots qui disent « voici de quoi je parle maintenant »",
       p:"Dans une lettre formelle, on n'a pas la place d'écrire un paragraphe d'introduction avant chaque idée. Les connecteurs de topicalisation font ce travail en trois mots : ils préviennent le lecteur du changement de sujet avant qu'il ne l'ait deviné. Sans eux, un paragraphe de six lignes se lit deux fois.",
       note:"Le programme du niveau 7 les nomme explicitement : « employer des connecteurs de topicalisation : quant à, à l'égard de, à propos de, en ce qui concerne, etc. »"},

      {t:'ana', h:"Quant à — le plus court, le plus employé",
       p:"Il annonce un sujet nouveau, presque toujours en tête de phrase, et il est toujours suivi d'un groupe du nom.",
       mots:[['La forme',"quant à mes disponibilités · quant au transport · quant aux stages"],
             ['La contraction',"quant à + le = quant au · quant à + les = quant aux", true],
             ['Ce qu\'il ne fait jamais',"il ne se met pas devant un verbe conjugué"]],
       say:"Quant à mes disponibilités, elles sont réglées depuis février.",
       note:"Ne pas confondre avec « quand », qui parle du temps. À l'oral, ils se ressemblent ; à l'écrit, la faute se voit tout de suite."},

      {t:'ana', h:"En ce qui concerne — le plus neutre",
       p:"Plus long, plus administratif, il passe partout et ne choque jamais. C'est celui à employer quand on hésite.",
       mots:[['La forme',"en ce qui concerne le préalable · en ce qui concerne ma formation"],
             ['La variante parlée',"pour ce qui est du transport, pour ce qui est des stages", true],
             ['Où le mettre',"en tête de phrase, suivi d'une virgule"]],
       say:"En ce qui concerne le préalable de mathématiques, je suis inscrite à la mise à niveau.",
       note:"« Pour ce qui est de » est la forme orale de la même chose. En entrevue, c'est elle qui sonne juste ; dans la lettre, préférez « en ce qui concerne »."},

      {t:'ana', h:"À l'égard de — le plus formel",
       p:"Réservé à l'écrit soutenu, et le plus souvent à une personne ou à une décision.",
       mots:[['La forme',"à l'égard de ma candidature · à l'égard des personnes candidates"],
             ['Ce qu\'il porte',"une décision, une obligation, une attitude", true],
             ['Le registre',"trop lourd pour une conversation, juste dans une lettre"]],
       say:"La décision rendue à l'égard de ma candidature m'a été communiquée le 10 avril.",
       note:"C'est aussi celui qu'emploient les avis administratifs que vous recevrez : le reconnaître à la lecture compte autant que savoir l'écrire."},

      {t:'check', h:'Quatre débuts de paragraphe',
       p:"Choisissez ce qui convient.",
       qs:[
         {q:"Dans une lettre, devant « mes disponibilités » :", opts:["Quand mes disponibilités","Quant à mes disponibilités"], ok:1,
          fb:"« Quant à » annonce un sujet ; « quand » situe dans le temps."},
         {q:"Devant « les stages » :", opts:["Quant à les stages","Quant aux stages"], ok:1,
          fb:"La contraction est obligatoire, comme avec « à »."},
         {q:"En entrevue, à l'oral :", opts:["Pour ce qui est du transport, j'ai mon permis.","À l'égard du transport, je détiens un permis."], ok:0,
          fb:"« À l'égard de » sonne récité à l'oral."},
         {q:"Ces connecteurs servent à…", opts:["relier deux idées","annoncer le sujet qui vient"], ok:1,
          fb:"Ils annoncent. Pour relier, il faut « donc », « parce que », « par contre »."},
       ]},

      {t:'piege', h:'Trois emplois qui ratent',
       rows:[
         ["écrire « quand à » au lieu de « quant à »","penser à « quantité », qui a le même début",
          "La faute est fréquente et elle se voit dans une lettre formelle, où l'on a eu le temps de relire."],
         ["mettre deux « quant à » dans le même paragraphe","un connecteur, un sujet, donc un paragraphe",
          "Deux annonces de sujet veulent dire deux sujets : coupez le paragraphe en deux, il sera plus clair."],
         ["s'en servir pour relier","ils annoncent, ils ne relient pas",
          "« Quant à » ne remplace ni « donc », ni « parce que ». Un texte qui n'a que des annonces n'a aucune progression."],
       ]},

      {t:'revoir', h:'À retenir',
       p:"<b>Quant à</b> + un nom, le plus court · <b>en ce qui concerne</b>, le plus neutre · <b>à l'égard de</b>, le plus formel · <b>pour ce qui est de</b>, celui de l'oral. Ils annoncent le sujet du paragraphe, ils ne relient pas les idées entre elles."},
    ]
  },

  t1nom: {
    eye:'Mini-leçon', tit:'Le nom que la lettre écrit à la place du verbe',
    blocs:[
      {t:'texte', h:"Pourquoi la langue administrative nomme au lieu de conjuguer",
       p:"« Vous avez décidé » devient « votre décision ». « J'ai été admise » devient « mon admission ». Ce n'est pas une manie : le nom permet de parler de l'action sans dire qui la fait ni quand. C'est ce qui rend un avis officiel neutre — et froid. Le savoir lire, c'est retrouver sous chaque nom un verbe et, sous le verbe, quelqu'un.",
       note:"Le programme du niveau 7 demande d'« exploiter les familles de mots pour la nominalisation » et d'« employer des procédés de substitution lexicale pour reprendre un référent ». Les deux vont ensemble : le nom sert aussi à reprendre ce qui vient d'être dit sans le répéter."},

      {t:'ana', h:"Les suffixes qui reviennent dans un dossier",
       p:"Trois familles suffisent à comprendre presque tout le vocabulaire de l'admission.",
       mots:[['-tion, féminin',"admettre → l'admission · sélectionner → la sélection · inscrire → l'inscription"],
             ['-ment, masculin',"classer → le classement · se désister → le désistement · traiter → le traitement", true],
             ['-ance, -ence, féminin',"exiger → l'exigence · reconnaître → la reconnaissance"]],
       say:"L'admission, la sélection, l'inscription, le classement, le désistement.",
       note:"Le genre suit le suffixe, presque sans exception : -tion et -ance sont féminins, -ment est masculin. C'est une des rares règles de genre qui tiennent."},

      {t:'ana', h:"Reprendre sans répéter",
       p:"Le nom sert aussi à éviter la répétition d'une phrase entière : on nomme ce qui vient d'être dit, et on continue.",
       mots:[['Avant',"« Le comité a étudié les dossiers. Le comité a étudié les dossiers en trois jours. »"],
             ['Après',"« Le comité a étudié les dossiers. Cette étude a duré trois jours. »", true],
             ['Ce que ça permet',"enchaîner deux phrases sans que la seconde recommence la première"]],
       say:"Le comité a étudié les dossiers. Cette étude a duré trois jours.",
       note:"C'est ce que le programme appelle la substitution lexicale. Dans une lettre de trois paragraphes, c'est ce qui empêche de dire « ma candidature » huit fois."},

      {t:'ex', h:'Douze mots du dossier',
       p:"Le verbe à gauche, le nom à droite.",
       rows:[
         ["admettre","l'admission"],
         ["sélectionner","la sélection"],
         ["s'inscrire","l'inscription"],
         ["classer","le classement"],
         ["se désister","le désistement"],
         ["exiger","l'exigence"],
         ["reconnaître","la reconnaissance"],
         ["décider","la décision"],
         ["recevoir","la réception"],
         ["former","la formation"],
         ["poser sa candidature","la candidature"],
         ["retenir","la rétention — mais on dit « les personnes retenues »"],
       ]},

      {t:'check', h:'Quatre transformations',
       p:"Trouvez le nom sans regarder le tableau.",
       qs:[
         {q:"« Une personne s'est désistée » →", opts:["un désistage","un désistement"], ok:1,
          fb:"-ment, masculin. C'est le mot qui fait bouger une liste d'attente."},
         {q:"« Le centre reconnaît vos acquis » →", opts:["la reconnaissance","la reconnaissation"], ok:0,
          fb:"Famille irrégulière : reconnaître → reconnaissance."},
         {q:"« Le programme exige un préalable » →", opts:["une exigence","une exigeance"], ok:0,
          fb:"Sans « a » : exigence."},
         {q:"« J'ai posé ma candidature » — en anglais, on dirait « apply ». En français d'ici :", opts:["j'ai appliqué","j'ai posé ma candidature"], ok:1,
          fb:"« Appliquer sur un programme » se remarque tout de suite dans un centre de formation."},
       ]},

      {t:'piege', h:'Trois pièges de la langue administrative',
       rows:[
         ["croire qu'un nom est plus poli qu'un verbe","choisir le nom quand on veut de la distance, le verbe quand on veut de la clarté",
          "« La réception de votre dossier » est neutre ; « nous avons reçu votre dossier » est clair. Dans votre lettre à vous, la clarté vaut mieux."],
         ["lire un avis sans chercher qui agit","sous chaque nom, un verbe ; sous chaque verbe, quelqu'un",
          "« Le refus de votre demande » ne dit pas qui a refusé. Si la réponse compte, il faut téléphoner et le demander."],
         ["inventer un nom qui n'existe pas","vérifier dans la famille du mot",
          "« Candidater » n'existe pas en français d'ici : on pose sa candidature, on soumet un dossier."],
       ]},

      {t:'revoir', h:'À retenir',
       p:"Trois suffixes portent presque tout le vocabulaire de l'admission : <b>-tion</b> (admission, sélection, inscription), <b>-ment</b> (classement, désistement), <b>-ance / -ence</b> (reconnaissance, exigence). Le nom sert à rester neutre et à reprendre sans répéter — et à la lecture, il sert à se demander qui agit."},
    ]
  },

  t1plan: {
    eye:'Mini-leçon', tit:'La mise en page d\'une lettre formelle',
    blocs:[
      {t:'texte', h:"Ce qui se voit avant d'être lu",
       p:"Une lettre formelle se juge en deux secondes, avant le premier mot : y a-t-il une date ? un objet ? des paragraphes séparés ? une signature ? Le comité en lit soixante-huit dans la même journée, et celles qui sont mal disposées coûtent un effort qu'il n'a pas à faire. La mise en page n'est pas de la décoration : c'est de la politesse rendue visible.",
       note:"Le programme du niveau 7 range ce point sous « tenir compte de la présentation matérielle et de la mise en page » : découper, disposer, formuler et présenter le contenu."},

      {t:'ana', h:"Le haut : lieu, date, objet",
       p:"Trois lignes, dans cet ordre, avant toute phrase.",
       mots:[['Le lieu et la date',"Granby, le 26 février — pas « 26/02 », pas « lundi »"],
             ['L\'objet',"Objet : Candidature au programme Santé, assistance et soins infirmiers", true],
             ['Ce que ça donne',"six semaines plus tard, on peut dire « ma lettre du 26 février »"]],
       say:"Granby, le 26 février. Objet : candidature au programme.",
       note:"Sans date, une lettre ne se relance pas : on ne peut pas dire « ma lettre du… », et l'autre ne peut pas la retrouver dans une pile."},

      {t:'ana', h:"Le milieu : la formule d'appel et les paragraphes",
       p:"Une formule d'appel, puis des paragraphes séparés par une ligne blanche, un par idée.",
       mots:[['Quand on ne sait pas qui lira',"Madame, Monsieur,"],
             ['Quand on sait',"Monsieur Fiset, — le nom, jamais le prénom seul", true],
             ['Les paragraphes',"trois, séparés, jamais un bloc de vingt lignes"]],
       say:"Madame, Monsieur, je vous soumets ma candidature.",
       note:"La virgule après la formule d'appel est obligatoire, et la phrase qui suit commence par une majuscule."},

      {t:'ana', h:"Le bas : courtoisie, signature, pièces jointes",
       p:"On ferme, on signe, et on annonce ce qui est joint.",
       mots:[['La courtoisie',"Veuillez agréer, Madame, Monsieur, mes salutations distinguées."],
             ['La signature',"le prénom et le nom, écrits au complet", true],
             ['Les pièces',"« Vous trouverez ci-joint… » — la liste de ce qui accompagne"]],
       say:"Veuillez agréer, Madame, Monsieur, mes salutations distinguées.",
       note:"La formule reprend exactement les mots de la formule d'appel : si l'on a écrit « Madame, Monsieur, » en haut, on les reprend en bas."},

      {t:'ex', h:'Sept parties, sept fonctions',
       p:"C'est l'ordre, et il ne change pas.",
       rows:[
         ["Lieu et date","Situer la lettre dans le temps."],
         ["Objet","Dire de quoi il s'agit en six mots."],
         ["Formule d'appel","S'adresser à quelqu'un."],
         ["Paragraphe 1","Demander, et dire pourquoi ici."],
         ["Paragraphe 2","Prouver par des faits."],
         ["Paragraphe 3","Dire l'après, et ce qui est commencé."],
         ["Courtoisie et signature","Fermer, signer, annoncer les pièces."],
       ]},

      {t:'check', h:'Quatre détails de disposition',
       p:"Vrai ou faux, en une seconde.",
       qs:[
         {q:"La date peut s'écrire « 26/02 ».", opts:["oui","non, on écrit le mois en lettres"], ok:1,
          fb:"« Granby, le 26 février » : c'est la forme d'une lettre formelle."},
         {q:"L'objet se termine par un point.", opts:["oui","non, ce n'est pas une phrase"], ok:1,
          fb:"Un objet est une étiquette, sans verbe conjugué et sans point final."},
         {q:"On peut écrire « Bonjour, » comme formule d'appel.", opts:["dans une candidature, non","toujours"], ok:0,
          fb:"« Bonjour » convient à un courriel entre collègues, pas à une candidature."},
         {q:"Les pièces jointes s'annoncent dans la lettre.", opts:["oui","non, l'enveloppe suffit"], ok:0,
          fb:"« Vous trouverez ci-joint… » : sans cette phrase, une pièce perdue ne se remarque jamais."},
       ]},

      {t:'piege', h:'Trois lettres qui se disqualifient sans une faute',
       rows:[
         ["un seul bloc de vingt lignes","trois paragraphes séparés par une ligne blanche",
          "Le contenu peut être excellent : personne ne le lira jusqu'au bout."],
         ["aucune date","toujours le lieu et la date en haut",
          "Six semaines plus tard, au téléphone, vous n'aurez aucune façon de nommer votre propre lettre."],
         ["une formule d'appel qui ne correspond pas à la formule finale","reprendre les mêmes mots en haut et en bas",
          "« Madame, Monsieur, » en haut et « Monsieur le Directeur » en bas : le lecteur comprend que la lettre a été recopiée."],
       ]},

      {t:'revoir', h:'À retenir',
       p:"Sept parties, dans l'ordre : <b>lieu et date · objet · formule d'appel · trois paragraphes · courtoisie et signature</b>. La date permet de nommer la lettre plus tard, l'objet la fait classer, les paragraphes la font lire, et la formule finale reprend les mots de la formule d'appel."},
    ]
  },

  // ── DÉFI 2 · L'ENTREVUE DE SÉLECTION ────────────────────────

  t2cond: {
    eye:'Mini-leçon', tit:'Le conditionnel présent, en entrevue',
    blocs:[
      {t:'texte', h:"Le temps qui laisse à l'autre la place de dire non",
       p:"« Vous pouvez me dire la date ? » et « Pourriez-vous me dire la date ? » demandent exactement la même chose. La seconde obtient une réponse plus souvent, parce qu'elle laisse à l'autre la possibilité de refuser — et c'est précisément pour cela qu'il accepte. En entrevue, c'est le temps de vos questions ; il n'est jamais celui de vos engagements.",
       note:"Le programme du niveau 7 en donne cinq emplois, dont deux servent ici : le conditionnel de politesse, et le conditionnel de l'hypothèse dans le présent ou l'avenir."},

      {t:'ana', h:"Comment il se fabrique",
       p:"Radical du futur simple, terminaisons de l'imparfait. Il n'y a rien d'autre à savoir : tout verbe irrégulier au futur l'est au conditionnel, de la même façon.",
       mots:[['Les terminaisons',"-ais, -ais, -ait, -ions, -iez, -aient"],
             ['Les six de l\'entrevue',"pourriez · voudrais · serait · aurais · saurais · devrais", true],
             ['Le son',"la finale se dit [ɛ], comme dans « mais » — et « nous serions » garde son e"]],
       say:"Pourriez-vous me préciser la date ? Je voudrais savoir si les cours se donnent le jour.",
       note:"Le « e » de « nous serions » et de « vous feriez » se maintient toujours : c'est la règle vue dans « Je découvre », et c'est au conditionnel qu'elle sert le plus."},

      {t:'ana', h:"Dans une question : demander sans exiger",
       p:"Le contenu de la demande ne change pas. Ce qui change, c'est la place que vous prenez en la faisant.",
       mots:[['Sans conditionnel',"« Vous pouvez répéter la question ? »"],
             ['Avec',"« Pourriez-vous répéter la question ? »", true],
             ['Là où ça compte le plus',"quand on demande quelque chose qu'on n'est pas sûr d'obtenir"]],
       say:"Pourriez-vous répéter la question, s'il vous plaît ?",
       note:"Faire répéter n'est pas un aveu de faiblesse : un comité préfère répéter une question plutôt qu'entendre une réponse à côté."},

      {t:'ana', h:"Dans une hypothèse : si + imparfait, puis conditionnel",
       p:"On parle de quelque chose qui n'est pas décidé. Le verbe après « si » est à l'imparfait, jamais au conditionnel.",
       mots:[['La forme',"Si j'étais admise en janvier, je garderais mes deux quarts."],
             ['L\'erreur qui s\'entend',"« Si je serais admise » — jamais", true],
             ['À quoi ça sert en entrevue',"montrer qu'on a prévu le cas où l'on ne serait pas retenue"]],
       say:"Si j'étais admise en janvier, je garderais mes deux quarts de fin de semaine.",
       note:"Répondre à une question hypothétique sans hésiter est un des rares gestes qui distinguent réellement une candidature : la plupart des gens répondent « je ne sais pas »."},

      {t:'labo', h:'La même demande, deux façons',
       p:"Choisissez une demande, puis la forme.",
       axes:[
         {id:'d', lbl:'Vous demandez…', opts:[['a','la date de la décision'],['b','de répéter'],['c','un exemple']]},
         {id:'f', lbl:'Comment ?', opts:[['p','à l\'indicatif'],['c','au conditionnel']]}],
       out:{
         ap:{w:["Vous me dites la date de la décision ?"], say:"Vous me dites la date de la décision ?", n:'correct, mais sec : la question ressemble à une exigence'},
         ac:{w:["Pourriez-vous me dire à quel moment la décision sera communiquée ?"], say:"Pourriez-vous me dire à quel moment la décision sera communiquée ?", n:'la forme d\'entrevue : la même question, une porte de sortie offerte'},
         bp:{w:["Vous pouvez répéter ?"], say:"Vous pouvez répéter ?", n:'passe entre collègues, un peu court devant un comité'},
         bc:{w:["Pourriez-vous répéter la question, s'il vous plaît ?"], say:"Pourriez-vous répéter la question, s'il vous plaît ?", n:'on fait répéter sans s\'excuser d\'exister'},
         cp:{w:["Donnez-moi un exemple."], say:"Donnez-moi un exemple.", n:'l\'impératif nu : à éviter avec qui vous évalue'},
         cc:{w:["Auriez-vous un exemple à me donner ?"], say:"Auriez-vous un exemple à me donner ?", n:'la demande la plus utile de toute l\'entrevue'},
       },
       note:"Écoutez la différence de longueur : le conditionnel coûte trois syllabes de plus, et c'est tout ce qu'il coûte."},

      {t:'check', h:'Quatre formes à trancher',
       p:"Une seule est juste.",
       qs:[
         {q:"« Si j'___ admise en janvier… »", opts:["serais","étais"], ok:1,
          fb:"Après « si », l'imparfait. Le conditionnel vient dans l'autre moitié de la phrase."},
         {q:"Pour s'engager sur une disponibilité :", opts:["« Je serais disponible dès septembre. »","« Je serai disponible dès septembre. »"], ok:1,
          fb:"Quand la chose est réglée, on dit « serai ». Le conditionnel laisserait croire que ça dépend encore."},
         {q:"« Nous ___ prêtes à commencer en janvier. »", opts:["serions","srions"], ok:0,
          fb:"Le « e » se maintient : trois syllabes, se-rions."},
         {q:"« ___-vous s'il reste des places ? »", opts:["Savez","Sauriez"], ok:1,
          fb:"Les deux sont corrects ; le conditionnel est celui de l'entrevue."},
       ]},

      {t:'piege', h:'Trois erreurs de conditionnel',
       rows:[
         ["mettre un conditionnel après « si »","imparfait après « si », conditionnel dans l'autre moitié",
          "C'est l'erreur la plus repérée du niveau, et elle s'entend immédiatement."],
         ["employer le conditionnel pour s'engager","« je serai », quand c'est réglé",
          "« Je serais disponible » laisse penser qu'il reste une condition. En entrevue, c'est exactement ce qu'il ne faut pas laisser penser."],
         ["confondre -rai et -rais à l'écrit","-rai = c'est décidé · -rais = ça dépend",
          "Une lettre qui écrit « je serai présente » engage ; « je serais présente » n'engage à rien, et le lecteur le voit."],
       ]},

      {t:'revoir', h:'À retenir',
       p:"Radical du futur, terminaisons de l'imparfait. Il sert à <b>demander</b> — pourriez-vous, je voudrais, auriez-vous — et à <b>supposer</b> — si j'étais admise, je garderais. Jamais de conditionnel après <b>si</b>, et jamais de conditionnel pour s'engager : <i>je serai</i>, quand c'est réglé."},
    ]
  },

  t2emph: {
    eye:'Mini-leçon', tit:'Mettre en avant ce qui compte',
    blocs:[
      {t:'texte', h:"À l'écrit on souligne, à l'oral on encadre",
       p:"Une réponse de vingt mots arrive plate devant un comité, et c'est le dernier mot qui reste — rarement le bon. La mise en relief est ce qui remplace le surligneur : elle prend un élément de la phrase et le met dans un cadre, « c'est… qui », « c'est… que », « ce que… c'est ». Le contenu est identique ; ce qu'on entend ne l'est pas.",
       note:"Le programme du niveau 7 les appelle les phrases emphatiques, et il en donne quatre modèles : le clivage du sujet, le clivage des autres éléments, le pseudo-clivage du groupe du nom, et le pseudo-clivage avec « ce que… c'est »."},

      {t:'ana', h:"C'est… qui — pour le sujet",
       p:"On encadre celui ou ce qui fait l'action.",
       mots:[['Avant',"Mon horaire a décidé de tout."],
             ['Après',"C'est mon horaire qui a décidé de tout.", true],
             ['L\'accord',"C'est moi qui suis allée la voir — jamais « qui est »"]],
       say:"C'est mon horaire qui a décidé de tout.",
       note:"Après « qui », le verbe prend la personne de ce qu'on encadre. « C'est moi qui suis », « c'est vous qui avez » : c'est la 1re personne qu'on rate le plus."},

      {t:'ana', h:"C'est… que — pour tout le reste",
       p:"Le complément, le lieu, le temps, la manière : tout ce qui n'est pas le sujet s'encadre avec « que ».",
       mots:[['Le lieu',"C'est à l'unité prothétique que je travaille."],
             ['La manière',"C'est en travaillant de nuit que j'ai appris à observer.", true],
             ['Le temps',"C'est depuis janvier que je suis un cours du soir."]],
       say:"C'est en travaillant de nuit que j'ai appris à observer.",
       note:"C'est la forme qui répond le mieux à une question ouverte : elle place la réponse au début de la phrase, au lieu de la faire attendre."},

      {t:'ana', h:"Ce que… c'est — pour annoncer que le cœur arrive",
       p:"La plus utile des trois en entrevue. Elle prévient l'interlocuteur qu'il doit écouter la fin de la phrase.",
       mots:[['Avec un complément',"Ce que je veux, c'est être celle qu'on va chercher."],
             ['Avec un sujet',"Ce qui me manque, c'est un préalable de mathématiques.", true],
             ['Le choix',"« ce que » quand il y a un complément, « ce qui » quand c'est le sujet"]],
       say:"Ce que je veux, c'est être celle qu'on va chercher.",
       note:"Employée deux fois dans une entrevue, elle porte. Employée à chaque réponse, elle devient un tic — et elle s'entend comme tel."},

      {t:'labo', h:'La même phrase, trois mises en relief',
       p:"Choisissez ce que vous voulez mettre en avant.",
       axes:[
         {id:'p', lbl:'Phrase de départ', opts:[['a','J\'ai appris à observer en travaillant de nuit'],['b','Il me manque un préalable']]},
         {id:'m', lbl:'Vous mettez en avant…', opts:[['s','le sujet'],['c','le complément'],['r','le cœur de la réponse']]}],
       out:{
         as:{w:["C'est moi qui ai appris à observer, personne ne me l'a montré."], say:"C'est moi qui ai appris à observer, personne ne me l'a montré.", n:'clivage du sujet — attention à l\'accord : qui ai, pas qui a'},
         ac:{w:["C'est en travaillant de nuit que j'ai appris à observer."], say:"C'est en travaillant de nuit que j'ai appris à observer.", n:'clivage du complément — la forme la plus utile en entrevue'},
         ar:{w:["Ce que la nuit m'a appris, c'est à observer."], say:"Ce que la nuit m'a appris, c'est à observer.", n:'pseudo-clivage — la réponse arrive à la fin, et on l\'attend'},
         bs:{w:["C'est un préalable qui me manque, rien d'autre."], say:"C'est un préalable qui me manque, rien d'autre.", n:'clivage du sujet — « un préalable » est ce qui manque'},
         bc:{w:["C'est en mathématiques que le préalable me manque."], say:"C'est en mathématiques que le préalable me manque.", n:'clivage du complément — on précise la matière'},
         br:{w:["Ce qui me manque, c'est un préalable de mathématiques."], say:"Ce qui me manque, c'est un préalable de mathématiques.", n:'pseudo-clivage — « ce qui », parce que c\'est le sujet'},
       },
       note:"Trois façons de dire la même chose, trois choses différentes entendues. C'est tout l'intérêt de la mise en relief."},

      {t:'check', h:'Quatre accords et deux choix',
       p:"Une seule forme est juste.",
       qs:[
         {q:"« C'est moi qui ___ allée la voir. »", opts:["est","suis"], ok:1,
          fb:"« Qui » reprend « moi » : première personne."},
         {q:"« C'est vous qui ___ mon dossier. »", opts:["a","avez"], ok:1,
          fb:"« Qui » reprend « vous » : deuxième personne du pluriel."},
         {q:"« ___ me manque, c'est un préalable. »", opts:["Ce que","Ce qui"], ok:1,
          fb:"Le préalable est le sujet de « manque » : « ce qui »."},
         {q:"« ___ je veux, c'est finir la formation. »", opts:["Ce que","Ce qui"], ok:0,
          fb:"« Je veux quelque chose » : complément, donc « ce que »."},
       ]},

      {t:'piege', h:'Trois emplois qui se retournent',
       rows:[
         ["« c'est moi qui est »","c'est moi qui suis",
          "L'accord à la première personne est celui qu'on rate le plus, et il est très audible."],
         ["mettre en relief à chaque phrase","deux fois dans une entrevue, pas dix",
          "La mise en relief attire l'attention. Utilisée partout, elle n'attire plus rien et devient un tic de langage."],
         ["encadrer ce qui n'est pas important","choisir l'élément qui répond à la question posée",
          "« C'est à huit heures que je me lève » quand on demande pourquoi vous voulez le diplôme : la forme est juste, le choix est raté."],
       ]},

      {t:'revoir', h:'À retenir',
       p:"<b>C'est… qui</b> pour le sujet (attention à l'accord : <i>c'est moi qui suis</i>) · <b>C'est… que</b> pour le lieu, le temps, la manière, le complément · <b>Ce que / ce qui… c'est</b> pour annoncer que la réponse arrive. Deux emplois par entrevue portent ; dix deviennent un tic."},
    ]
  },

  t2conc: {
    eye:'Mini-leçon', tit:'Concéder sans s\'effacer : bien que, même si, malgré',
    blocs:[
      {t:'texte', h:"Voir l'objection avant qu'on vous la pose",
       p:"Un comité de sélection connaît vos points faibles avant de vous rencontrer : ils sont dans le dossier. Un candidat qui n'en parle pas a l'air de n'avoir rien regardé ; un candidat qui ne parle que de ça se disqualifie tout seul. La concession fait les deux choses à la fois : elle reconnaît l'obstacle, puis elle dit pourquoi il n'arrête rien.",
       note:"Le programme du niveau 7 demande de « comprendre l'expression de la concession avec des marqueurs courants : bien que, malgré que » et d'« exprimer la concession avec le marqueur même si »."},

      {t:'ana', h:"Bien que + subjonctif",
       p:"Le marqueur le plus formel des trois, et le seul qui impose le subjonctif — sans aucune exception.",
       mots:[['La forme',"Bien que j'aie déjà suivi ce cours, je le referais."],
             ['Les quatre verbes qu\'on emploie',"j'aie · je sois · ce soit · il puisse", true],
             ['Le registre',"écrit, ou oral soigné — c'est celui de l'entrevue et de la lettre"]],
       say:"Bien que j'aie déjà suivi ce cours en Syrie, je le referais sans discuter.",
       note:"« Malgré que » existe, mais il est contesté et il vaut mieux l'éviter à l'écrit. « Bien que » ne l'est jamais."},

      {t:'ana', h:"Même si + indicatif",
       p:"L'exacte symétrie de l'autre : jamais de subjonctif après « même si ». C'est le marqueur le plus courant à l'oral.",
       mots:[['La forme',"Même si l'horaire est serré, il est prévu depuis février."],
             ['Ce qu\'il ajoute',"une insistance : « oui, même dans ce cas-là »", true],
             ['L\'erreur symétrique',"« même si ce soit » — jamais"]],
       say:"Même si l'horaire est serré, il est prévu et écrit depuis février.",
       note:"Les deux marqueurs disent la même chose ; ce qui les sépare est le mode du verbe qui suit. C'est une des rares paires où l'erreur est purement mécanique."},

      {t:'ana', h:"Malgré + un nom",
       p:"Le plus court, et le seul qui ne se met pas devant un verbe conjugué.",
       mots:[['La forme',"Malgré la distance, je serai là tous les matins."],
             ['Ce qui le suit',"toujours un groupe du nom : la distance, mon accent, l'horaire", true],
             ['Devant un verbe',"il faut « malgré le fait que » — lourd ; dites plutôt « bien que »"]],
       say:"Malgré la distance, je serai au centre à huit heures tous les matins.",
       note:"« Malgré » est très efficace en tête de réponse : il pose l'obstacle en trois mots et libère toute la phrase pour la réponse."},

      {t:'ex', h:'Six concessions d\'entrevue',
       p:"L'obstacle d'abord, la réponse ensuite.",
       rows:[
         ["Bien que je n'aie pas encore mon préalable,","je suis inscrite à la mise à niveau de septembre."],
         ["Même si l'horaire est serré,","il est prévu et écrit depuis février."],
         ["Malgré la distance,","je serai au centre à huit heures tous les matins."],
         ["Bien que la formation soit à temps plein,","j'ai gardé deux quarts de fin de semaine seulement."],
         ["Même si j'écris lentement,","je ne remets jamais une note incomplète."],
         ["Malgré mon accent,","on me comprend au téléphone : je parle lentement et j'épelle."],
       ]},

      {t:'check', h:'Quatre modes à choisir',
       p:"Subjonctif ou indicatif ?",
       qs:[
         {q:"« Bien que ce ___ ma deuxième demande… »", opts:["est","soit"], ok:1,
          fb:"« Bien que » impose le subjonctif, toujours."},
         {q:"« Même si ce ___ ma deuxième demande… »", opts:["est","soit"], ok:0,
          fb:"« Même si » impose l'indicatif, toujours. C'est l'erreur symétrique."},
         {q:"« ___ la distance, je serai là. »", opts:["Malgré","Bien que"], ok:0,
          fb:"« La distance » est un nom : « malgré »."},
         {q:"Dans quel ordre en entrevue ?", opts:["la réponse, puis l'obstacle","l'obstacle, puis la réponse"], ok:1,
          fb:"Dans l'autre sens, le comité n'entend que l'obstacle : c'est le dernier mot qui reste."},
       ]},

      {t:'piege', h:'Trois concessions qui se retournent contre soi',
       rows:[
         ["s'excuser au lieu de concéder","une phrase pour l'obstacle, deux pour la réponse",
          "« Je sais que je ne suis pas la meilleure candidate » n'est pas une concession : c'est un argument contre soi, offert gratuitement."],
         ["concéder ce qui n'a pas été demandé","répondre à l'objection du dossier, pas à toutes",
          "Trois concessions dans une même réponse donnent l'impression d'une liste de défauts préparée à l'avance."],
         ["finir sur l'obstacle","toujours finir sur ce qui est réglé",
          "« Je suis inscrite à la mise à niveau, bien que je n'aie pas mon préalable » laisse le comité sur le manque. Inversez."],
       ]},

      {t:'revoir', h:'À retenir',
       p:"<b>Bien que</b> + subjonctif · <b>Même si</b> + indicatif · <b>Malgré</b> + un nom. Toujours dans cet ordre : l'obstacle d'abord, la réponse ensuite — sinon le comité n'entend que l'obstacle."},
    ]
  },

  // ── DÉFI 3 · LE SUIVI, APRÈS ────────────────────────────────

  t3avis: {
    eye:'Mini-leçon', tit:'Lire un avis administratif sans se décourager',
    blocs:[
      {t:'texte', h:"Quatre choses à y chercher, dans cet ordre",
       p:"Une lettre de décision se lit deux fois. La première fois, on cherche le mot qui dit oui ou non, et on s'arrête là — c'est la lecture qui décourage. La seconde se fait un crayon à la main : qu'est-ce qui a été décidé exactement ? sur quoi ? à quelle date ? et qui est nommé ? Ce sont ces quatre renseignements qui permettent de faire quelque chose ensuite.",
       note:"Un avis ne dit presque jamais la cinquième chose, celle qui compte le plus : ce qu'il faudrait changer. Elle ne s'obtient qu'au téléphone, et seulement si l'on appelle."},

      {t:'ana', h:"« Retenue » n'est pas « admise »",
       p:"Deux mots voisins, deux situations complètement différentes. C'est le mot qu'on lit le plus vite et qu'on comprend le moins.",
       mots:[['Retenue',"le dossier a passé la sélection"],
             ['Admise',"il y avait une place", true],
             ['Entre les deux',"la liste d'attente — retenue sans place"]],
       say:"Votre candidature a été retenue, mais aucune place ne peut vous être offerte pour le moment.",
       note:"Une personne retenue est déjà passée devant les deux tiers des candidatures. Le lui dire change la façon dont elle prépare l'année suivante."},

      {t:'ana', h:"Cherchez la phrase qui contient une date",
       p:"C'est la seule qui vous donne prise. Une décision sans date ne se relance pas ; une décision datée se relance la veille.",
       mots:[['Exemples de dates utiles',"« examinés à la mi-décembre » · « actif jusqu'au 30 juin »"],
             ['Ce qu\'on en fait',"on note la date, et on appelle avant, jamais après", true],
             ['Le piège',"« dès que possible » et « sous peu » ne sont pas des dates"]],
       say:"Les dossiers en vue de cette entrée sont examinés à la mi-décembre.",
       note:"Rappeler en février un dossier qui se regarde en décembre, c'est rappeler pour rien. La date est le renseignement le plus utile de toute la lettre."},

      {t:'ana', h:"Cherchez le nom d'une personne",
       p:"Un avis signé par une fonction ne se rappelle pas. Un avis qui nomme quelqu'un, oui — avec son poste téléphonique.",
       mots:[['Ce qu\'on cherche',"« vous pouvez joindre monsieur X, conseiller pédagogique, au poste 2244 »"],
             ['S\'il n\'y a personne',"la personne qui vous a reçue en entrevue", true],
             ['Ce qu\'on ne fait pas',"écrire une seconde lettre à personne"]],
       say:"Pour toute question relative à la présente décision, vous pouvez joindre le conseiller pédagogique au poste 2244.",
       note:"C'est cette ligne-là, en bas de page et en petits caractères, qui transforme un refus en démarche."},

      {t:'ex', h:'Sept formules d\'avis, et ce qu\'elles veulent dire',
       p:"À gauche ce qui est écrit, à droite ce que ça veut dire.",
       rows:[
         ["« votre candidature a été retenue »","le dossier a passé la sélection"],
         ["« il ne nous a pas été possible de vous offrir une place »","il n'y a pas de place, ce n'est pas un refus du dossier"],
         ["« votre nom est inscrit sur la liste d'attente »","vous serez appelée si quelqu'un se désiste"],
         ["« le rang n'est pas communiqué »","inutile de le redemander ; demandez autre chose"],
         ["« votre dossier demeure actif jusqu'au 30 juin »","rien à refaire d'ici là"],
         ["« les dossiers sont examinés à la mi-décembre »","la date à noter, et à devancer d'une semaine"],
         ["« vous pouvez joindre monsieur X au poste 2244 »","la porte d'entrée : c'est là qu'on appelle"],
       ]},

      {t:'check', h:'Quatre lectures rapides',
       p:"Que faut-il en conclure ?",
       qs:[
         {q:"« Votre candidature a été retenue. » suivi de « aucune place disponible » :", opts:["vous êtes refusée","vous êtes retenue sans place"], ok:1,
          fb:"C'est la liste d'attente, et c'est très différent d'un refus."},
         {q:"« Le rang n'est pas communiqué. » :", opts:["insister au téléphone","demander plutôt ce qui ferait la différence"], ok:1,
          fb:"Le rang change tous les jours ; ce qui ne change pas, c'est ce qui manque au dossier."},
         {q:"« Les dossiers sont examinés à la mi-décembre. » — vous rappelez :", opts:["en février","au début de décembre"], ok:1,
          fb:"Avant la date, jamais après : après, tout est décidé."},
         {q:"L'avis nomme une personne et un poste téléphonique :", opts:["c'est une formule de politesse","c'est la porte d'entrée, et il faut s'en servir"], ok:1,
          fb:"Cette ligne existe parce que quelqu'un doit répondre. Très peu de gens appellent."},
       ]},

      {t:'piege', h:'Trois façons de mal lire une décision',
       rows:[
         ["s'arrêter au premier paragraphe","lire jusqu'au bas de la page, où sont les dates et les noms",
          "Le paragraphe qui dit ce qu'il faut faire ensuite est presque toujours l'avant-dernier."],
         ["prendre « retenue » pour « admise »","chercher le mot « place »",
          "Deux candidates lisent la même lettre : l'une comprend qu'elle a réussi, l'autre qu'elle est refusée. Ni l'une ni l'autre n'a raison."],
         ["répondre par écrit à un avis","téléphoner à la personne nommée",
          "Une lettre entre dans une pile. Un appel obtient en trois minutes ce que la lettre ne dira jamais : ce qu'il faudrait changer."],
       ]},

      {t:'revoir', h:'À retenir',
       p:"Quatre renseignements à extraire : <b>ce qui a été décidé</b> (« retenue » n'est pas « admise »), <b>sur quoi</b>, <b>à quelle date</b> — la seule qui donne prise —, et <b>qui est nommé</b>. La cinquième chose, ce qu'il faudrait changer, ne s'obtient qu'au téléphone."},
    ]
  },

  t3rap: {
    eye:'Mini-leçon', tit:'Rapporter ce qui a été dit : le discours indirect au passé',
    blocs:[
      {t:'texte', h:"La phrase qui transforme une plainte en suivi",
       p:"« Je rappelle encore » ferme une porte. « Vous m'aviez dit de vous rappeler après la décision » l'ouvre — et c'est la même personne, le même dossier, le même jour. Rapporter exactement ce qui a été dit, et par qui, est le geste central d'un appel de suivi. Encore faut-il que les temps suivent, parce que le moment d'où l'on parle a reculé.",
       note:"Le programme du niveau 7 appelle cela « la postériorité quand le point de référence est décalé, notamment dans le discours indirect au passé », et « le plus-que-parfait pour exprimer l'antériorité »."},

      {t:'ana', h:"Le présent devient imparfait",
       p:"Ce qui était vrai au moment où on l'a dit se raconte à l'imparfait.",
       mots:[['On avait dit',"« Le stage arrive tôt dans l'année. »"],
             ['On rapporte',"Vous m'aviez dit que le stage arrivait tôt.", true],
             ['Pourquoi',"le moment d'où l'on parle a reculé, donc le temps recule avec lui"]],
       say:"Vous m'aviez dit que le stage arrivait tôt dans l'année.",
       note:"Le mouvement est mécanique : chaque temps recule d'un cran. Il suffit de savoir de quel cran il s'agit."},

      {t:'ana', h:"Le futur devient conditionnel — ou « aller » à l'imparfait",
       p:"C'est la postériorité : au moment du récit, la chose n'était pas encore arrivée.",
       mots:[['Forme écrite',"Il m'avait répondu que le stage arriverait avant Noël."],
             ['Forme parlée',"Vous m'aviez dit que vous alliez me rappeler.", true],
             ['Les deux sont justes',"la seconde est plus fréquente au téléphone"]],
       say:"Vous m'aviez dit que vous alliez me rappeler après la décision.",
       note:"« Aller » à l'imparfait plus l'infinitif est la forme la plus naturelle à l'oral d'ici, et elle est parfaitement correcte."},

      {t:'ana', h:"Le passé composé devient plus-que-parfait",
       p:"C'est l'antériorité : l'action est plus vieille que le récit qu'on en fait.",
       mots:[['On avait dit',"« J'ai déposé mon dossier le 26 février. »"],
             ['On rapporte',"J'ai expliqué que j'avais déposé mon dossier le 26 février.", true],
             ['La forme',"l'auxiliaire à l'imparfait, plus le participe passé"]],
       say:"J'ai expliqué que j'avais déposé mon dossier le 26 février.",
       note:"C'est le temps qui permet de raconter deux passés à la fois : celui de l'appel, et celui de ce qui s'était passé avant."},

      {t:'labo', h:'La même parole, rapportée trois fois',
       p:"Choisissez ce qui a été dit, puis le moment d'où vous le rapportez.",
       axes:[
         {id:'p', lbl:'On vous avait dit…', opts:[['a','« Le stage arrive tôt »'],['b','« Je vais vous rappeler »'],['c','« J\'ai reçu votre dossier »']]},
         {id:'q', lbl:'Vous rapportez…', opts:[['d','au présent'],['p','au passé']]}],
       out:{
         ad:{w:["Vous me dites que le stage arrive tôt."], say:"Vous me dites que le stage arrive tôt.", n:'même moment : rien ne bouge'},
         ap:{w:["Vous m'aviez dit que le stage arrivait tôt."], say:"Vous m'aviez dit que le stage arrivait tôt.", n:'présent devenu imparfait'},
         bd:{w:["Vous me dites que vous allez me rappeler."], say:"Vous me dites que vous allez me rappeler.", n:'même moment : « allez » reste au présent'},
         bp:{w:["Vous m'aviez dit que vous alliez me rappeler."], say:"Vous m'aviez dit que vous alliez me rappeler.", n:'postériorité : « aller » passe à l\'imparfait'},
         cd:{w:["Vous me dites que vous avez reçu mon dossier."], say:"Vous me dites que vous avez reçu mon dossier.", n:'même moment : passé composé'},
         cp:{w:["Vous m'aviez dit que vous aviez reçu mon dossier."], say:"Vous m'aviez dit que vous aviez reçu mon dossier.", n:'antériorité : plus-que-parfait'},
       },
       note:"Un seul mouvement, trois applications : présent → imparfait, futur → conditionnel, passé composé → plus-que-parfait."},

      {t:'check', h:'Quatre reculs de temps',
       p:"Quel temps faut-il ?",
       qs:[
         {q:"« Les places sont limitées. » → La lettre disait que les places ___ limitées.", opts:["sont","étaient"], ok:1,
          fb:"Présent → imparfait."},
         {q:"« Nous examinerons les dossiers en décembre. » → Elle m'avait précisé qu'on les ___ en décembre.", opts:["examinera","examinerait"], ok:1,
          fb:"Futur → conditionnel : c'est la postériorité."},
         {q:"« J'ai fait deux ans d'études. » → J'avais dit que j'___ deux ans d'études.", opts:["ai fait","avais fait"], ok:1,
          fb:"Passé composé → plus-que-parfait."},
         {q:"« Rappelez-moi. » → Vous m'aviez demandé de vous ___.", opts:["rappeliez","rappeler"], ok:1,
          fb:"Un ordre rapporté passe à l'infinitif, avec « de »."},
       ]},

      {t:'piege', h:'Trois façons de rater un rappel',
       rows:[
         ["rapporter sans reculer les temps","présent → imparfait, futur → conditionnel",
          "« Vous m'aviez dit que le stage arrive tôt » : la phrase se comprend, mais elle sonne traduite."],
         ["reprocher au lieu de rapporter","« vous m'aviez dit », jamais « vous aviez promis »",
          "« Promis » met l'autre en défaut dès la deuxième phrase, et il n'y a plus rien à obtenir ensuite."],
         ["rapporter sans nommer qui a parlé","« monsieur X m'avait dit », avec la date de la rencontre",
          "Une parole sans auteur ni date ne se vérifie pas, et la personne au bout du fil ne peut rien en faire."],
       ]},

      {t:'revoir', h:'À retenir',
       p:"Quand le verbe qui introduit est au passé, tout recule d'un cran : <b>présent → imparfait</b>, <b>futur → conditionnel</b> (ou <i>aller</i> à l'imparfait), <b>passé composé → plus-que-parfait</b>, <b>ordre → infinitif avec « de »</b>. On rapporte, on ne reproche pas."},
    ]
  },

  t3que: {
    eye:'Mini-leçon', tit:'Limiter, conclure, reformuler — les trois dernières minutes',
    blocs:[
      {t:'texte', h:"Trois phrases, et l'appel se termine sur ce qui est convenu",
       p:"La fin d'un appel décide de ce qu'on en retient. Trois outils suffisent : une restriction qui montre qu'on ne demande pas tout, une conséquence qui dit ce qu'on va faire, une reformulation qui fait confirmer. Trente secondes, et l'appel se termine sur une entente plutôt que sur un refus.",
       note:"Le programme du niveau 7 demande de « comprendre la restriction avec le marqueur ne… que », d'« exprimer la conséquence : donc, par conséquent » et d'« employer des connecteurs de reformulation courants : autrement dit, en somme »."},

      {t:'ana', h:"Ne… que : limiter, et non nier",
       p:"C'est le point le plus mal compris de la liste. « Ne… que » ne dit pas non : il dit « rien de plus que ».",
       mots:[['La forme',"Il ne me manque qu'un préalable."],
             ['Ce que ça fait entendre',"tout le reste est en règle — c'est une bonne nouvelle", true],
             ['La place de « que »',"juste devant ce qu'on limite"]],
       say:"Il ne me manque qu'un préalable de mathématiques.",
       note:"La place de « que » change tout : « je ne travaille que les fins de semaine » (rien d'autre) et « je ne travaille pas que les fins de semaine » (aussi d'autres jours) sont deux affirmations opposées."},

      {t:'ana', h:"Donc, par conséquent : conclure",
       p:"Ils annoncent ce que vous tirez de ce qui vient d'être dit. C'est ce qui prouve que vous avez écouté.",
       mots:[['À l\'oral',"Le rang ne se communique pas ; je ne le demanderai donc plus."],
             ['À l\'écrit',"Les dossiers sont examinés en décembre ; par conséquent, je vous rappellerai le 10.", true],
             ['La différence',"« donc » se dit, « par conséquent » s'écrit"]],
       say:"Les dossiers sont examinés à la mi-décembre ; par conséquent, je vous rappellerai le 10.",
       note:"Tirer soi-même la conclusion évite de la faire tirer par l'autre. C'est aussi ce qui vous fait proposer une date au lieu d'en attendre une."},

      {t:'ana', h:"Autrement dit, en somme : faire confirmer",
       p:"La phrase la plus utile de tout l'appel : elle résume l'entente et oblige l'autre à confirmer ou à corriger.",
       mots:[['La forme',"Autrement dit, je m'inscris à la mise à niveau et je vous rappelle en décembre ?"],
             ['La variante',"En somme, ce n'est pas mon entrevue qui a manqué, c'est une case.", true],
             ['Ce que ça évite',"raccrocher sur un malentendu, et refaire l'appel un mois plus tard"]],
       say:"Autrement dit, je m'inscris à la mise à niveau et je vous rappelle en décembre ?",
       note:"On la dit avec l'intonation d'une question, même quand on est sûr. C'est ce qui laisse à l'autre la possibilité de corriger un détail."},

      {t:'ex', h:'La fin d\'un appel, phrase par phrase',
       p:"Trente secondes, dans cet ordre.",
       rows:[
         ["Restriction","« Il ne me manque qu'un préalable ; le reste du dossier est complet. »"],
         ["Restriction (2)","« Je ne vous appelle que pour savoir quoi faire d'ici l'an prochain. »"],
         ["Conséquence","« Les dossiers se regardent en décembre ; je vous rappellerai donc le 10. »"],
         ["Reformulation","« Autrement dit, je m'inscris à la mise à niveau et je vous rappelle ? »"],
         ["Confirmation attendue","« C'est exactement ça. »"],
         ["Clôture","« Merci de m'avoir rappelée ; je vous reparle le 10 décembre. »"],
       ]},

      {t:'check', h:'Quatre phrases de fin',
       p:"Laquelle fait ce qu'on veut ?",
       qs:[
         {q:"« Je ne travaille que les fins de semaine » veut dire :", opts:["aussi d'autres jours","rien d'autre que les fins de semaine"], ok:1,
          fb:"« Ne… que » limite à ce qui suit « que »."},
         {q:"« Je ne travaille pas que les fins de semaine » veut dire :", opts:["aussi d'autres jours","seulement les fins de semaine"], ok:0,
          fb:"La négation porte sur la restriction elle-même : donc, pas seulement."},
         {q:"Pour finir un appel :", opts:["« Merci beaucoup, bonne journée. »","« Autrement dit, je m'inscris et je vous rappelle en décembre ? »"], ok:1,
          fb:"La reformulation fait confirmer l'entente ; le remerciement seul laisse tout ouvert."},
         {q:"« Par conséquent » convient surtout :", opts:["à l'écrit","au téléphone"], ok:0,
          fb:"À l'oral, « donc » suffit et sonne juste."},
       ]},

      {t:'piege', h:'Trois fins d\'appel qui ne servent à rien',
       rows:[
         ["raccrocher sur un « merci »","reformuler l'entente avant de remercier",
          "Sans reformulation, rien n'est convenu : le mois suivant, l'appel recommence au complet."],
         ["ne fixer aucune date","proposer une date soi-même",
          "« Je vous rappellerai » n'engage personne. « Je vous rappelle le 10 décembre » vous engage, et c'est ce qu'on veut."],
         ["employer « ne… que » comme une négation","il limite, il ne nie pas",
          "« Je n'ai qu'une question » annonce une question ; « je n'ai pas de question » met fin à l'appel. Un mot d'écart."],
       ]},

      {t:'revoir', h:'À retenir',
       p:"<b>Ne… que</b> limite sans nier, et « que » se place devant ce qu'on limite. <b>Donc</b> se dit, <b>par conséquent</b> s'écrit. <b>Autrement dit</b> et <b>en somme</b> font confirmer l'entente — et un appel qui se termine sans date recommence au complet la fois suivante."},
    ]
  },

  t3tel: {
    eye:'Mini-leçon', tit:'Un appel de suivi tient en trois minutes',
    blocs:[
      {t:'texte', h:"Ce qui distingue un suivi d'une plainte",
       p:"Les deux appels commencent pareil : quelqu'un attend une réponse qui n'est pas venue. Ce qui les sépare tient dans la première minute. Le suivi se présente, dit pourquoi il appelle, rapporte ce qui avait été convenu, puis demande ce qu'il peut faire. La plainte raconte, s'indigne, et demande qu'on fasse quelque chose. Le premier obtient souvent quelque chose ; le second, presque jamais.",
       note:"Le programme du niveau 7 range le vocabulaire de cet appel dans la situation elle-même : « phrases clés pour se présenter, exposer le motif de l'appel et mettre fin à une conversation téléphonique »."},

      {t:'ana', h:"Premier temps : se présenter en trois éléments",
       p:"Le nom, le numéro de dossier, le lien avec l'établissement. Rien d'autre, et dans cet ordre.",
       mots:[['La formule',"Bonjour, Rania Nassar, dossier 41-2887."],
             ['Le lien',"J'ai passé l'entrevue du 12 mars.", true],
             ['Pourquoi le numéro tout de suite',"la personne ouvre le dossier pendant que vous parlez"]],
       say:"Bonjour, Rania Nassar, dossier 41-2887. J'ai passé l'entrevue du 12 mars.",
       note:"Donner le numéro de dossier dans les dix premières secondes fait gagner deux minutes à tout le monde, et met l'autre de votre côté avant que vous ayez demandé quoi que ce soit."},

      {t:'ana', h:"Deuxième temps : le motif, en une phrase, avant l'histoire",
       p:"On dit pourquoi on appelle avant de raconter. L'histoire vient après, et seulement si on la demande.",
       mots:[['La formule',"Je vous appelle au sujet de la lettre du 10 avril."],
             ['Ce qu\'on ajoute ensuite',"Vous m'aviez dit de vous rappeler après la décision.", true],
             ['Ce qu\'on ne fait pas',"commencer par « ça fait trois semaines que… »"]],
       say:"Je vous appelle au sujet de la lettre que j'ai reçue le 10 avril.",
       note:"Une personne qui reçoit trente appels par jour décide en dix secondes si elle vous transfère ou non. Le motif est ce qui décide."},

      {t:'ana', h:"Troisième temps : conclure sur une suite",
       p:"On reformule, on propose une date, on remercie. Dans cet ordre, et jamais l'inverse.",
       mots:[['La reformulation',"Autrement dit, je m'inscris à la mise à niveau et je vous rappelle en décembre ?"],
             ['La date',"Je vous reparle le 10 décembre.", true],
             ['Le numéro',"laissé lentement, chiffre par chiffre, et répété une fois"]],
       say:"Autrement dit, je m'inscris à la mise à niveau et je vous rappelle en décembre ?",
       note:"La question qui ouvre presque toujours quelque chose, et que presque personne ne pose : « qu'est-ce que je peux faire d'ici là ? »"},

      {t:'ex', h:'Neuf phrases, trois moments',
       p:"À gauche la phrase, à droite son moment.",
       rows:[
         ["« Bonjour, Rania Nassar, dossier 41-2887. »","je me présente"],
         ["« J'ai passé l'entrevue du 12 mars. »","je me présente"],
         ["« Je suis préposée au CHSLD des Quatre-Vents. »","je me présente"],
         ["« Je vous appelle au sujet de la lettre de lundi. »","j'expose le motif"],
         ["« Vous m'aviez dit de vous rappeler après la décision. »","j'expose le motif"],
         ["« Ce que je voudrais savoir, c'est ce que je peux faire. »","j'expose le motif"],
         ["« Autrement dit, je m'inscris et je vous rappelle ? »","je conclus"],
         ["« Je vous laisse mon numéro : 450 555-0192. »","je conclus"],
         ["« Merci de m'avoir rappelée ; je vous reparle le 10. »","je conclus"],
       ]},

      {t:'check', h:'Quatre décisions d\'appel',
       p:"Que faites-vous ?",
       qs:[
         {q:"La personne au secrétariat ne peut pas donner le renseignement :", opts:["insister","demander à qui s'adresser, et laisser un message précis"], ok:1,
          fb:"Elle n'a pas le droit, pas l'envie de vous nuire. Le message précis, lui, se transmet."},
         {q:"Vous laissez un message. Vous dites :", opts:["« Rania a appelé, qu'on me rappelle. »","le nom, le dossier, le motif en une phrase et le numéro"], ok:1,
          fb:"Un message sans motif ne se traite pas : il attend qu'on vous rejoigne pour savoir ce que vous voulez."},
         {q:"On vous rappelle. Vous commencez par :", opts:["raconter depuis le début","remercier, puis rappeler le motif en une phrase"], ok:1,
          fb:"L'autre a votre dossier devant lui : il lui manque une phrase, pas une histoire."},
         {q:"L'appel se termine sans date :", opts:["c'est normal","proposer une date avant de raccrocher"], ok:1,
          fb:"Sans date, l'appel suivant recommence au complet."},
       ]},

      {t:'piege', h:'Trois appels qui n\'obtiennent rien',
       rows:[
         ["raconter avant de dire pourquoi on appelle","le motif en une phrase, dans les vingt premières secondes",
          "Au bout d'une minute d'histoire, l'autre n'écoute plus : il cherche encore ce que vous voulez."],
         ["demander une faveur","demander ce qu'on peut faire soi-même",
          "« Est-ce qu'on pourrait me passer devant ? » ferme la conversation. « Qu'est-ce que je peux faire d'ici l'an prochain ? » l'ouvre."],
         ["parler des autres candidats","parler de son propre dossier",
          "Ce que les autres ont ou n'ont pas ne se discute pas au téléphone, et la personne au bout du fil n'a pas le droit d'en parler."],
       ]},

      {t:'revoir', h:'À retenir',
       p:"Trois temps : <b>je me présente</b> (nom, dossier, lien) · <b>j'expose le motif</b> en une phrase, avant l'histoire, en rapportant ce qui avait été dit · <b>je conclus</b> en reformulant et en proposant une date. Et la question qui ouvre presque toujours quelque chose : « qu'est-ce que je peux faire d'ici là ? »"},
    ]
  },

};
