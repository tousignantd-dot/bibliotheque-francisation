const PLUS = {

  prProso: {
    eye:'Mini-leçon', tit:"La voix qui dit « ce n'est pas fini »",
    blocs:[
      {t:'texte', h:"Le problème n'est plus la prononciation",
       p:"À ce niveau-ci, vous prononcez les sons du français. Ce qui vous trahit encore, c'est la <b>mélodie</b> : où la voix monte, où elle descend, et où l'on respire. Une phrase de vingt-cinq mots dite sur une seule note oblige l'auditeur à travailler, et en réunion, personne ne travaille pour écouter.",
       note:"On appelle ça la <b>prosodie</b> : le rythme et la mélodie de la phrase, indépendamment des mots."},

      {t:'ana', h:"Le groupe de souffle",
       p:"Le français ne découpe pas la phrase mot par mot : il la découpe en <b>groupes de sens</b>, et chaque groupe se dit d'un seul souffle.",
       mots:[['Un groupe','{Le premier bloc}'],['Un autre','{c\'est la réception des commandes}'],['Un dernier','{avant midi}']],
       say:"Le premier bloc, c'est la réception des commandes, avant midi.",
       note:"Trois groupes, trois souffles. Entre les deux premiers, la voix reste en haut : la phrase continue."},

      {t:'texte', h:"La règle en une ligne",
       p:"<b>La voix monte tant que la phrase n'est pas finie ; elle descend au dernier groupe.</b> C'est tout. Un groupe qui finit en haut annonce une suite ; un groupe qui finit en bas ferme la porte.",
       note:"C'est pour ça qu'une énumération monte, monte, monte, puis descend au dernier élément : <i>les décisions ↗, la personne ↗, la date ↘</i>."},

      {t:'ana', h:"La montée : ça continue",
       p:"Après une subordonnée placée devant, après un groupe complément, au milieu d'une énumération.",
       mots:[['Après « si »','{Si l\'écart est en bas de vingt-cinq dollars} ↗'],['Après un groupe','{Tu compares les factures} ↗'],['Dans une liste','{les décisions} ↗ {qui les applique} ↗']],
       say:"Si l'écart est en bas de vingt-cinq dollars, tu approuves.",
       note:"La montée est petite. On ne chante pas : la voix se pose une note plus haut et reste là."},

      {t:'ana', h:"La descente : c'est fini",
       p:"Au dernier groupe d'une phrase déclarative, et sur un ordre.",
       mots:[['Fin de phrase','{et c\'est moi qui tranche.} ↘'],['Un ordre','{Envoie-le avant jeudi.} ↘'],['Une confirmation','{C\'est noté.} ↘']],
       say:"Envoie-le au groupe avant jeudi.",
       note:"Une descente franche vaut mieux qu'une descente molle : elle dit que vous avez fini, et l'autre peut parler."},

      {t:'labo', h:"Écoutez la même phrase, ouverte puis fermée",
       p:"Choisissez un groupe et la mélodie que vous voulez entendre.",
       axes:[
         {id:'g', lbl:'Quel groupe ?', opts:[['a','la description de tâches'],['b','la réunion'],['c','la paie']]},
         {id:'m', lbl:'Quelle mélodie ?', opts:[['1','↗ ça continue'],['2','↘ ça finit']]}],
       out:{
         a1:{w:["Le premier bloc, c'est la réception des commandes"], say:"Le premier bloc, c'est la réception des commandes", n:'la voix reste en haut : une suite s\'en vient'},
         a2:{w:["et c'est moi qui tranche."], say:"et c'est moi qui tranche.", n:'la voix descend : la phrase est close'},
         b1:{w:["Si je résume ce que vous venez de dire"], say:"Si je résume ce que vous venez de dire", n:'après « si », on monte toujours'},
         b2:{w:["On tranche à la réunion du seize."], say:"On tranche à la réunion du seize.", n:'une décision se dit en descendant'},
         c1:{w:["Les dix et onze août, j'ai fait quarante-quatre heures"], say:"Les dix et onze août, j'ai fait quarante-quatre heures", n:'le complément de temps est un groupe à lui seul'},
         c2:{w:["La majoration n'a pas été appliquée."], say:"La majoration n'a pas été appliquée.", n:'le fait se pose, sans monter — ce n\'est pas une question'},
       },
       note:"Écoutez, puis répétez en exagérant la montée. À l'usage, elle s'atténuera d'elle-même."},

      {t:'ex', h:"Six phrases longues, découpées",
       p:"Les barres marquent les souffles. Lisez à voix haute en respectant les groupes.",
       rows:[
         ["Le premier bloc / c'est la réception des commandes / avant midi.","3 groupes, descente sur le dernier"],
         ["Si l'écart est en bas de vingt-cinq dollars / tu approuves.","montée, puis descente"],
         ["Tu appelles le transporteur / le mardi et le jeudi / et tu notes les retards.","2 montées, 1 descente"],
         ["On veut les décisions / qui les applique / et pour quand.","énumération : 2 montées, 1 descente"],
         ["Ce que je vois / c'est que j'ai travaillé quatre heures / au-delà de quarante.","le sujet long monte"],
         ["Je vous saurais gré / de me confirmer la correction / avant le vingt-sept août.","formule d'affaires en 3 souffles"],
       ]},

      {t:'piege', h:"Trois défauts de mélodie qui s'entendent tout de suite",
       rows:[
         ["monter à la fin d'une affirmation","descendre franchement",
          "Une affirmation qui monte se lit comme une question ou comme une hésitation. Au téléphone, votre interlocuteur répondra « oui ? » au lieu d'agir."],
         ["parler sans respirer","découper en groupes de sens",
          "Une phrase de trente mots sans pause épuise l'auditeur, qui décroche au milieu et vous fait tout répéter."],
         ["accentuer chaque mot","accentuer la fin du groupe",
          "En français, l'accent tombe sur la <b>dernière syllabe du groupe</b>, jamais sur chaque mot. Accentuer partout, c'est n'accentuer nulle part."],
       ]},

      {t:'check', h:"Est-ce que c'est clair maintenant ?",
       p:"Quatre questions rapides.",
       qs:[
         {q:"« Si l'écart est en bas de vingt-cinq dollars… » : la voix…", opts:["monte","descend"], ok:0,
          fb:"La phrase n'est pas finie : elle monte."},
         {q:"En français, l'accent tombe…", opts:["sur chaque mot","sur la dernière syllabe du groupe"], ok:1,
          fb:"C'est ce qui donne au français son rythme régulier."},
         {q:"Dans une énumération de trois éléments, le troisième…", opts:["monte comme les autres","descend"], ok:1,
          fb:"La descente signale que la liste est terminée."},
         {q:"Un groupe de souffle, c'est…", opts:["un groupe de sens dit d'un trait","un nombre fixe de mots"], ok:0,
          fb:"Le sens décide du découpage, pas le nombre de mots."},
       ]},
    ]
  },

  prReg: {
    eye:'Mini-leçon', tit:"Le registre : deux façons de dire vrai",
    blocs:[
      {t:'texte', h:"Ce n'est pas une question de politesse",
       p:"On croit souvent que le registre familier est impoli et que le registre standard est poli. C'est faux, et cette idée fausse coûte cher : elle pousse à écrire des courriels ampoulés et à parler comme un livre à la machine à café. Le registre, c'est le <b>choix des mots</b> et la <b>forme de la phrase</b>, choisis selon la situation et l'interlocuteur.",
       note:"Yves n'est pas impoli quand il dit « c'est plate à dire ». Il serait ridicule s'il disait « c'est regrettable » devant la machine à café."},

      {t:'ana', h:"Ce qui change dans les mots",
       p:"Le vocabulaire familier est concret, imagé, court.",
       mots:[['Familier','une job · un gars · jaser · plate · le fun'],['Standard','un emploi · un employé · discuter · regrettable · agréable'],['Soutenu','un poste · un collaborateur · s\'entretenir · déplorable · plaisant']],
       note:"La colonne du milieu est celle du travail écrit. La troisième ne sert qu'à la correspondance très formelle : employée partout, elle sonne faux."},

      {t:'ana', h:"Ce qui change dans la phrase",
       p:"Trois marques, faciles à repérer et à corriger.",
       mots:[['Le « ne »','Familier : <i>Ça marche pas.</i> — Standard : <i>Cela {ne} fonctionne pas.</i>'],['La question','Familier : <i>Tu viens-tu ?</i> — Standard : <i>{Venez-vous} ?</i>'],['Le sujet repris','Familier : <i>Mon boss, {lui}, il dit que…</i> — Standard : <i>Ma superviseure {estime} que…</i>']],
       note:"À l'oral standard, le « ne » disparaît chez presque tout le monde. À l'écrit, son absence est une faute — sans exception."},

      {t:'texte', h:"Le vrai risque, au travail",
       p:"Ce n'est pas de parler trop familièrement : c'est d'employer le registre familier <b>par écrit</b>, dans un courriel qui sera transféré. Un message envoyé à votre superviseure peut se retrouver devant la direction. Ce qui se disait très bien à la machine à café devient, sur un écran, la preuve qu'on ne sait pas écrire.",
       note:"La règle pratique : tout ce qui s'écrit passe au registre standard. Tout ce qui se dit entre collègues suit le groupe."},

      {t:'ex', h:"Huit reformulations utiles",
       p:"À gauche ce qu'on entend, à droite ce qu'on écrit.",
       rows:[
         ["Ça marche pas, leur affaire.","Leur système ne fonctionne pas."],
         ["Ça m'a pris deux ans.","Il m'a fallu deux ans."],
         ["C'est plate à dire.","C'est regrettable."],
         ["Le gars de la découpe.","L'employé affecté à la découpe."],
         ["Elle t'a passé le grand portrait ?","Vous a-t-elle présenté l'ensemble de vos tâches ?"],
         ["Ça se jase à la machine à café.","Cela se transmet de façon informelle."],
         ["Tant qu'à faire, ajoutez-la.","Par la même occasion, ajoutez-la."],
         ["J'écoperais de ce travail-là.","Ce travail me reviendrait."],
       ]},

      {t:'piege', h:"Trois erreurs de registre au bureau",
       rows:[
         ["écrire « Salut Manon, ça marche pas leur affaire »","écrire « Bonjour Manon, leur système ne fonctionne pas »",
          "Le courriel interne peut être transféré. Le « Bonjour » et le « ne » coûtent deux secondes."],
         ["dire « Veuillez agréer » à un collègue","dire « Merci » ou « Cordialement »",
          "Le registre trop haut crée une distance qu'on n'a pas voulue, et fait croire à une plainte."],
         ["traduire mot à mot une formule de sa langue","employer la formule française d'usage",
          "Les formules d'ouverture et de clôture ne se traduisent pas : elles se remplacent."],
       ]},

      {t:'check', h:"Est-ce que c'est clair maintenant ?",
       p:"Quatre questions rapides.",
       qs:[
         {q:"Le registre familier est…", opts:["impoli","adapté à certaines situations"], ok:1,
          fb:"Il est juste entre collègues, faux dans un courriel à la direction."},
         {q:"À l'écrit, le « ne » de la négation…", opts:["s'omet comme à l'oral","s'écrit toujours"], ok:1,
          fb:"Son absence à l'écrit est une faute, sans exception."},
         {q:"« Veuillez agréer » à un collègue de bureau…", opts:["est trop soutenu","est correct"], ok:0,
          fb:"« Cordialement » suffit à l'interne."},
         {q:"La règle pratique la plus sûre…", opts:["tout ce qui s'écrit passe au standard","on écrit comme on parle"], ok:0,
          fb:"Un courriel se transfère ; il vit plus longtemps que la conversation."},
       ]},
    ]
  },

  t1normes: {
    eye:'Mini-leçon', tit:"Quatre règles qu'on ne discute pas",
    blocs:[
      {t:'texte', h:"Pourquoi les connaître par cœur",
       p:"Dans une conversation sur la paie, celui qui connaît la règle n'a pas à hausser le ton. Ces quatre règles viennent de la <b>Loi sur les normes du travail</b> et elles s'appliquent à presque tous les salariés du Québec, qu'il y ait un contrat écrit ou non. Un employeur ne peut pas offrir moins ; une entente qui donnerait moins n'a aucune valeur.",
       note:"L'organisme responsable est la <b>CNESST</b> — Commission des normes, de l'équité, de la santé et de la sécurité du travail. C'est là que l'information officielle se vérifie."},

      {t:'ana', h:"Règle 1 — les heures supplémentaires",
       p:"Au-delà de <b>quarante heures</b> dans une même semaine, chaque heure est majorée de <b>cinquante pour cent</b>.",
       mots:[['Le seuil','{quarante heures} par semaine'],['La majoration','{cinquante pour cent} du taux habituel'],['Un exemple','22 $ l\'heure → {33 $} la quarante et unième']],
       note:"Le seuil est hebdomadaire, pas quotidien : douze heures un mardi ne sont pas supplémentaires si la semaine reste sous quarante."},

      {t:'ana', h:"Règle 2 — le congé au lieu du paiement",
       p:"À la <b>demande du salarié</b>, l'employeur peut remplacer le paiement par un congé payé équivalent aux heures faites <b>plus cinquante pour cent</b>.",
       mots:[['Qui demande','le {salarié}, pas l\'employeur seul'],['Le calcul','4 heures faites → {6 heures} de congé'],['Le délai','à prendre dans les {douze mois}']],
       note:"Passé les douze mois, les heures se paient. Ce n'est pas une faveur : c'est la suite prévue par la loi."},

      {t:'ana', h:"Règle 3 — la période de repas",
       p:"Après <b>cinq heures consécutives</b> de travail, le salarié a droit à <b>trente minutes</b> pour manger.",
       mots:[['Le déclencheur','{cinq heures} consécutives'],['La durée','{trente minutes}'],['Payée ?','{non} — sauf si vous ne pouvez pas quitter votre poste']],
       note:"« Rester au comptoir au cas où un client arrive » veut dire que le repas est payé."},

      {t:'ana', h:"Règle 4 — la pause-café",
       p:"L'employeur <b>n'est pas obligé</b> d'accorder une pause. Mais s'il en accorde une, elle est <b>payée</b>.",
       mots:[['Obligatoire ?','{non}'],['Si accordée','{payée} et comptée dans les heures travaillées'],['Conséquence','elle compte pour le seuil de {quarante heures}']],
       note:"C'est la seule des quatre règles qui dépende de l'employeur — et une fois qu'il l'accorde, il ne peut plus la retirer du temps payé."},

      {t:'texte', h:"Et quand ça ne se règle pas dans l'entreprise",
       p:"Deux recours à connaître, avec leurs délais exacts. <b>Congédiement sans cause juste et suffisante</b> : il faut <b>deux ans de service continu</b>, et la plainte se dépose à la CNESST dans les <b>quarante-cinq jours</b> du congédiement. <b>Harcèlement psychologique ou sexuel</b> : la plainte se dépose dans les <b>deux ans</b> de la dernière manifestation.",
       note:"Ces délais sont courts et ils ne se rattrapent pas. Devant un doute, on appelle la CNESST avant que le délai coure, pas après."},

      {t:'ex', h:"Cinq situations, une règle chacune",
       p:"À vous de reconnaître laquelle s'applique.",
       rows:[
         ["Quarante-quatre heures travaillées, quarante-quatre payées au taux simple","majoration de 50 % sur les 4 heures au-delà de 40"],
         ["Six heures d'affilée sans avoir pu manger","droit à 30 minutes après 5 heures consécutives"],
         ["Repas pris au poste, téléphone à répondre","période de repas payée"],
         ["Deux pauses de dix minutes accordées chaque jour","payées et comptées dans les heures travaillées"],
         ["Quatre heures supplémentaires converties en congé","6 heures de congé, à prendre dans les 12 mois"],
       ]},

      {t:'piege', h:"Trois idées reçues",
       rows:[
         ["« Sans autorisation écrite, les heures ne comptent pas »","le travail fait se paie",
          "L'autorisation est une exigence interne de l'employeur. La majoration, elle, découle de la loi. Les deux se règlent, mais ce ne sont pas les mêmes choses — c'est exactement la distinction que fait Sylvain."],
         ["« Le seuil est de huit heures par jour »","le seuil légal est hebdomadaire",
          "Quarante heures par semaine. Une convention collective peut prévoir mieux ; jamais moins."],
         ["« Ma pause repas est payée, c'est normal »","elle ne l'est que si vous ne pouvez pas partir",
          "Beaucoup d'employeurs la paient par choix. C'est un avantage, pas une obligation."],
       ]},

      {t:'check', h:"Est-ce que c'est clair maintenant ?",
       p:"Quatre questions rapides.",
       qs:[
         {q:"Le seuil des heures supplémentaires est de…", opts:["8 heures par jour","40 heures par semaine"], ok:1,
          fb:"Le seuil légal est hebdomadaire."},
         {q:"Le congé qui remplace le paiement se prend dans…", opts:["12 mois","24 mois"], ok:0,
          fb:"Sinon les heures doivent être payées."},
         {q:"Une pause-café accordée est…", opts:["payée","non payée"], ok:0,
          fb:"Et elle compte dans les heures travaillées."},
         {q:"Une plainte pour congédiement sans cause juste se dépose dans…", opts:["45 jours","2 ans"], ok:0,
          fb:"45 jours, avec 2 ans de service continu exigés. Les 2 ans, c'est le délai du harcèlement."},
       ]},
    ]
  },

  t1subj: {
    eye:'Mini-leçon', tit:"Le subjonctif, ou comment dire ce qui doit arriver",
    blocs:[
      {t:'texte', h:"Ce que le subjonctif n'est pas",
       p:"Ce n'est pas un temps difficile réservé aux livres. C'est le mode de ce qui <b>n'est pas encore un fait</b> : ce qu'on veut, ce qu'il faut, ce qu'on craint, ce qu'on souhaite. L'indicatif raconte le monde tel qu'il est ; le subjonctif parle du monde tel qu'il devrait être. Dans une réclamation, on passe son temps dans le second.",
       note:"« La demande passe par ma superviseure » = un fait. « Il faut que la demande <b>passe</b> par ma superviseure » = une exigence."},

      {t:'ana', h:"La formation, en trois gestes",
       p:"Presque tous les verbes suivent le même chemin.",
       mots:[['1. Le « ils » du présent','ils {vérifient} · ils {passent} · ils {avancent}'],['2. On enlève -ent','vérifi- · pass- · avanc-'],['3. On ajoute','-e, -es, -e, {-ions}, {-iez}, -ent']],
       note:"Aux formes <i>nous</i> et <i>vous</i>, le subjonctif ressemble à l'imparfait : <i>que nous vérifiions, que vous passiez</i>. Le double « i » de <i>vérifiions</i> est correct."},

      {t:'ana', h:"Les quatre à savoir par cœur",
       p:"Ce sont ceux qui reviennent tout le temps, et ils sont irréguliers.",
       mots:[['être','que je {sois}, que nous {soyons}'],['avoir','que j\'{aie}, que nous {ayons}'],['faire','que je {fasse}'],['aller','que j\'{aille}, que nous {allions}']],
       note:"Ajoutez-en trois si vous avez le temps : <i>que je puisse</i> (pouvoir), <i>que je sache</i> (savoir), <i>qu'il faille</i> (falloir)."},

      {t:'ana', h:"Les déclencheurs du bureau",
       p:"Ce n'est pas le sens de la phrase qu'il faut deviner : c'est le mot qui précède.",
       mots:[['La nécessité','il faut que · il est nécessaire que · il est important que'],['La volonté','je souhaite que · j\'aimerais que · je demande que'],['Le but et le temps','pour que · avant que · jusqu\'à ce que'],['La condition et l\'opposition','à condition que · pourvu que · bien que · quoique']],
       note:"Apprenez la liste, pas la règle. Ces vingt expressions couvrent la quasi-totalité des cas d'un courriel professionnel."},

      {t:'texte', h:"Les faux amis : ceux qui n'en veulent pas",
       p:"Trois expressions ressemblent aux précédentes et demandent pourtant l'<b>indicatif</b>. <b>après que</b> (l'action a eu lieu, c'est un fait), <b>espérer que</b> (l'espoir se tourne vers un futur qu'on croit possible) et <b>il est probable que</b>. En revanche, <b>il est possible que</b> demande bien le subjonctif : le français distingue le probable du possible.",
       note:"<i>J'espère que la correction <b>paraîtra</b></i> · <i>Il est possible que le système <b>mêle</b> des dossiers</i>."},

      {t:'ex', h:"Huit phrases de courriel",
       p:"Toutes tirées d'une réclamation ordinaire.",
       rows:[
         ["Il faut que la demande passe par ma superviseure.","subjonctif : nécessité"],
         ["Il est important que vous ayez le document avant mercredi.","subjonctif : nécessité"],
         ["Je souhaite que la correction soit faite sur la paie du 29.","subjonctif : volonté"],
         ["Bien que la règle soit claire, le système ne l'applique pas.","subjonctif : opposition"],
         ["Pour que le dossier avance, joignez l'autorisation.","subjonctif : but"],
         ["À condition que nous fassions la demande aujourd'hui…","subjonctif : condition"],
         ["J'espère que vous comprenez ma démarche.","indicatif : espérer"],
         ["Après que la période sera fermée, plus rien ne bouge.","indicatif : après que"],
       ]},

      {t:'piege', h:"Trois pièges d'écrit",
       rows:[
         ["« après que j'aie »","« après que j'ai »",
          "Faute très répandue, y compris chez des locuteurs natifs. <i>Après que</i> introduit un fait accompli : indicatif."],
         ["« il faut que je vais »","« il faut que j'aille »",
          "<i>Aller</i> au subjonctif est irrégulier et c'est le verbe le plus employé après <i>il faut que</i>."],
         ["« bien qu'il est clair »","« bien qu'il soit clair »",
          "<i>Bien que</i> et <i>quoique</i> demandent toujours le subjonctif, même devant une évidence."],
       ]},

      {t:'check', h:"Est-ce que c'est clair maintenant ?",
       p:"Quatre questions rapides.",
       qs:[
         {q:"Le subjonctif se forme à partir du…", opts:["« ils » du présent","« je » du futur"], ok:0,
          fb:"ils vérifient → que je vérifie."},
         {q:"« Après que » demande…", opts:["le subjonctif","l'indicatif"], ok:1,
          fb:"L'action est un fait accompli."},
         {q:"« Il est possible que » demande…", opts:["le subjonctif","l'indicatif"], ok:0,
          fb:"Mais « il est probable que » demande l'indicatif."},
         {q:"« Bien que la règle ___ claire »", opts:["est","soit"], ok:1,
          fb:"Bien que + subjonctif, toujours."},
       ]},
    ]
  },

  t1pass: {
    eye:'Mini-leçon', tit:"La voix passive : l'outil du dossier qui se règle",
    blocs:[
      {t:'texte', h:"Une transformation, un effet",
       p:"La voix passive n'ajoute aucune information : elle <b>déplace le projecteur</b>. Dans « Vous n'avez pas appliqué la majoration », le projecteur est sur <i>vous</i>. Dans « La majoration n'a pas été appliquée », il est sur le fait. La première phrase demande à quelqu'un de se défendre ; la seconde demande à quelqu'un de corriger. Devinez laquelle obtient une correction.",
       note:"C'est la raison pour laquelle la langue administrative en est pleine. Ce n'est pas de la lâcheté : c'est un outil de règlement."},

      {t:'ana', h:"Comment on la fabrique",
       p:"Trois gestes, dans l'ordre.",
       mots:[['1. Le complément monte','Le système a mêlé {les dossiers} → {Les dossiers}…'],['2. Le verbe devient être + participe','a mêlé → {ont été mêlés}'],['3. L\'ancien sujet devient facultatif','{par le système} — souvent inutile']],
       say:"Les dossiers ont été mêlés par le système d'inventaire.",
       note:"Le temps du verbe <b>être</b> porte le temps de la phrase : <i>est traité</i> (présent), <i>a été traité</i> (passé composé), <i>sera traité</i> (futur)."},

      {t:'ana', h:"L'accord, qui ne pardonne pas",
       p:"Le participe passé s'accorde <b>avec le sujet</b>, toujours, sans exception.",
       mots:[['Masculin pluriel','Les dossiers ont été {mêlés}'],['Féminin pluriel','Les heures ont été {saisies}'],['Féminin singulier','La majoration n\'a pas été {appliquée}']],
       note:"C'est plus simple que l'accord avec <i>avoir</i> : il n'y a rien à chercher, le sujet est devant."},

      {t:'texte', h:"Quand ne pas l'employer",
       p:"La passive alourdit dès qu'elle s'empile. Trois passives de suite dans un paragraphe donnent un texte sans personne dedans, qu'on lit deux fois sans comprendre qui fait quoi. Réservez-la aux phrases où le <b>fait compte plus que l'auteur</b> : l'écart constaté, l'erreur, la règle. Pour votre propre demande, revenez à l'actif : « Je vous demande de corriger. »",
       note:"Le bon dosage, dans une lettre de réclamation : passive pour l'écart, active pour la demande."},

      {t:'ex', h:"Six transformations utiles",
       p:"À gauche l'accusation, à droite le constat.",
       rows:[
         ["Vous n'avez pas appliqué la majoration.","La majoration n'a pas été appliquée."],
         ["Quelqu'un a saisi 44 heures.","Quarante-quatre heures ont été saisies."],
         ["Ma superviseure a autorisé ces heures.","Ces heures ont été autorisées par ma superviseure."],
         ["On fermera la période mercredi.","La période sera fermée mercredi."],
         ["La direction doit approuver la modification.","La modification doit être approuvée par la direction."],
         ["On a corrigé les deux périodes.","Les deux périodes ont été corrigées."],
       ]},

      {t:'piege', h:"Trois confusions fréquentes",
       rows:[
         ["prendre « elle est arrivée » pour une passive","c'est un passé composé avec être",
          "Test infaillible : une passive répond à « par qui ? ». <i>Arrivée par qui ?</i> n'a pas de sens."],
         ["oublier l'accord du participe","accorder avec le sujet",
          "<i>Les heures ont été saisi</i> → <i>saisies</i>. Le sujet est juste devant : il n'y a aucune excuse."],
         ["employer « par » au lieu de « de »","garder « de » avec les verbes de sentiment",
          "<i>Elle est appréciée <b>de</b> ses collègues</i>, et non <i>par</i>. Cas rare, mais très visible."],
       ]},

      {t:'check', h:"Est-ce que c'est clair maintenant ?",
       p:"Quatre questions rapides.",
       qs:[
         {q:"Dans une passive, le participe s'accorde avec…", opts:["le sujet","le complément d'agent"], ok:0,
          fb:"Toujours avec le sujet, qui est devant."},
         {q:"« La période sera fermée mercredi » est…", opts:["au futur","au passé"], ok:0,
          fb:"C'est le verbe être qui porte le temps."},
         {q:"Le complément d'agent (« par… ») est…", opts:["obligatoire","facultatif"], ok:1,
          fb:"On l'omet quand nommer l'auteur n'apporte rien."},
         {q:"Pour formuler votre demande, mieux vaut…", opts:["la passive","l'actif"], ok:1,
          fb:"« Je vous demande de corriger » : on sait qui demande quoi."},
       ]},
    ]
  },

  t1lettre: {
    eye:'Mini-leçon', tit:"La lettre d'affaires qui règle un problème",
    blocs:[
      {t:'texte', h:"Cinq parties, pas six",
       p:"Une lettre qui règle un problème tient en cinq mouvements : on <b>rattache</b> la lettre à ce qui précède, on <b>expose</b> les faits datés et chiffrés, on <b>nomme l'écart</b>, on <b>formule une demande</b>, on <b>fixe une échéance</b> et on salue. Tout le reste — l'historique complet, les émotions, les excuses — allonge sans rien ajouter.",
       note:"Une page. Celui qui la reçoit traite trente dossiers ; au-delà d'une page, il remet la vôtre à demain."},

      {t:'ana', h:"L'objet, qui décide de tout",
       p:"C'est la seule ligne qu'on est sûr que le destinataire lira.",
       mots:[['Mauvais','{Question} · {Problème} · {Suivi}'],['Bon','{Correction des heures supplémentaires — périodes du 2 au 15 août}'],['Pourquoi','il dit {quoi} et {quand} sans ouvrir le message']],
       note:"Un objet qui se lit seul permet aussi de retrouver la lettre six mois plus tard, dans une boîte de trois mille courriels."},

      {t:'ana', h:"Les formules qui portent",
       p:"Elles sont peu nombreuses ; les apprendre une fois suffit pour dix ans.",
       mots:[['Rattacher','Je {donne suite} à notre conversation du 19 août.'],['Nommer l\'écart','{Or}, la majoration n\'a pas été appliquée.'],['Demander','Je vous {demande} de corriger les deux périodes.'],['Fixer l\'échéance','Je vous {saurais gré} de me confirmer avant le 27.'],['Annoncer les pièces','Vous trouverez {ci-joint} les deux courriels.']],
       note:"<b>Or</b> est le mot le plus utile de la lettre : il oppose le fait attendu au fait constaté, sans accuser personne."},

      {t:'texte', h:"Le ton : ni excuse ni menace",
       p:"Deux tentations, toutes deux perdantes. S'excuser (« Je suis vraiment désolée de déranger, je sais que vous êtes occupé ») affaiblit une demande légitime et invite au report. Menacer dès la première lettre (« Sinon je porte plainte ») ferme la porte à un règlement simple et met votre interlocuteur en position de défense. On expose, on demande, on date.",
       note:"Le recours existe et il reste disponible. On le garde pour la deuxième lettre, s'il y en a une — et il n'y en a presque jamais."},

      {t:'ex', h:"La lettre de Nadia, en huit lignes",
       p:"Chaque ligne fait un travail, et un seul.",
       rows:[
         ["Objet : correction des heures supplémentaires — périodes du 2 au 15 août","situer sans ouvrir"],
         ["Madame, je donne suite à notre conversation téléphonique du 19 août.","rattacher"],
         ["Les 10 et 11 août, j'ai travaillé quatre heures au-delà de quarante.","exposer, daté et chiffré"],
         ["Or, la majoration de cinquante pour cent n'a pas été appliquée.","nommer l'écart"],
         ["La période du 2 au 9 août présente le même écart.","élargir, une seule fois"],
         ["Je vous demande donc de corriger les deux périodes visées.","demander"],
         ["Vous trouverez ci-joint les deux courriels d'autorisation.","annoncer les pièces"],
         ["Je vous saurais gré de me confirmer la correction avant le 27 août.","échéance"],
       ]},

      {t:'piege', h:"Trois défauts qui font traîner un dossier",
       rows:[
         ["« Il y a un problème avec ma paie »","« 4 heures au-delà de 40, les 10 et 11 août »",
          "Sans date ni chiffre, votre interlocuteur doit chercher. Il cherchera demain."],
         ["deux demandes dans une lettre","une demande, une lettre",
          "Deux demandes produisent une réponse partielle, et il faut réécrire pour la seconde."],
         ["aucune date de retour","une échéance raisonnable",
          "« Dès que possible » ne se met pas à l'agenda. Une date, si."],
       ]},

      {t:'check', h:"Est-ce que c'est clair maintenant ?",
       p:"Quatre questions rapides.",
       qs:[
         {q:"L'objet du courriel doit…", opts:["rester vague pour intriguer","dire quoi et quand"], ok:1,
          fb:"Il doit se lire seul."},
         {q:"« Or » sert à…", opts:["opposer l'attendu au constaté","conclure la lettre"], ok:0,
          fb:"C'est le mot qui nomme l'écart sans accuser."},
         {q:"Menacer d'un recours dans la première lettre…", opts:["accélère le règlement","ferme la porte"], ok:1,
          fb:"Le recours reste disponible ; on n'a pas besoin de l'annoncer."},
         {q:"Une bonne lettre de réclamation contient…", opts:["une seule demande","toutes vos demandes"], ok:0,
          fb:"Une demande, une lettre, une réponse."},
       ]},
    ]
  },

  t2cond: {
    eye:'Mini-leçon', tit:"Deux conditionnels pour peser ses mots",
    blocs:[
      {t:'texte', h:"Le mode de celui qui veut être écouté",
       p:"En réunion, celui qui dit « je veux qu'on partage » se fait répondre non, parce qu'il n'a laissé aucune place au refus. Celui qui dit « je proposerais un partage » avance exactement la même idée en laissant à l'autre la liberté d'y venir. Le conditionnel n'est pas de la timidité : c'est ce qui permet à une proposition d'être discutée au lieu d'être combattue.",
       note:"Nadia l'emploie quatre fois dans la réunion. Elle obtient que sa proposition soit étudiée."},

      {t:'ana', h:"Le conditionnel présent",
       p:"Le radical du <b>futur</b>, les terminaisons de l'<b>imparfait</b>.",
       mots:[['Formation','proposer- + {-ais} → je {proposerais}'],['Régulier','ferait · resterait · mettrait · pourrait'],['Irréguliers utiles','je {serais} · j\'{aurais} · je {ferais} · j\'{irais} · je {voudrais} · je {pourrais}']],
       note:"Si vous savez faire le futur, vous savez faire le conditionnel : c'est le même radical."},

      {t:'ana', h:"Le conditionnel passé",
       p:"<b>avoir</b> ou <b>être</b> au conditionnel présent, plus le participe passé.",
       mots:[['Formation','{aurais} + fait · {serait} + resté'],['Le regret','On {aurait dû} demander leurs délais.'],['Le résultat manqué','Il {serait resté} vingt mille dollars.']],
       note:"<i>On aurait dû</i> est la formule la plus utile de toute la réunion : elle reconnaît une erreur sans désigner de coupable."},

      {t:'texte', h:"Ce que chacun dit vraiment",
       p:"Le <b>présent</b> parle de maintenant et de la suite : une proposition, une demande polie, une hypothèse ouverte. Le <b>passé</b> parle de ce qui ne s'est pas produit : un regret, un reproche atténué, le résultat d'une hypothèse manquée. Confondre les deux fait dire l'inverse de ce qu'on veut : « je proposerais » ouvre la discussion, « j'aurais proposé » la referme sur un reproche.",
       note:"Test rapide : si la chose peut encore arriver, présent. Si elle ne peut plus, passé."},

      {t:'ex', h:"Huit phrases de réunion",
       p:"Quatre au présent, quatre au passé.",
       rows:[
         ["Je proposerais un partage des commandes.","présent : proposition"],
         ["Ça me ferait deux heures de plus par mois.","présent : conséquence envisagée"],
         ["Est-ce que vous pourriez chiffrer l'espace ?","présent : demande polie"],
         ["J'aimerais qu'on tranche le seize.","présent : souhait"],
         ["On aurait dû demander leurs délais.","passé : regret partagé"],
         ["Il serait resté vingt mille dollars.","passé : résultat non réalisé"],
         ["On n'aurait pas dû faire circuler la soumission si vite.","passé : reproche atténué"],
         ["Si j'avais lu la page quatre, je vous en aurais parlé.","passé : hypothèse manquée"],
       ]},

      {t:'piege', h:"Trois pièges, dont un d'écrit seulement",
       rows:[
         ["écrire « je proposerai » pour une idée","« je proposerais »",
          "Un seul son à l'oral, deux sens à l'écrit : <i>-ai</i> est un futur (c'est décidé), <i>-ais</i> un conditionnel (c'est une idée). En compte rendu, la confusion crée un engagement que personne n'a pris."],
         ["« si j'aurais su »","« si j'avais su »",
          "Jamais de conditionnel après <i>si</i>. La faute est immédiatement repérée par un francophone."],
         ["employer le conditionnel pour tout adoucir","garder l'indicatif pour les faits",
          "<i>Le délai serait de dix jours</i> laisse croire que vous n'êtes pas sûre. Si c'est écrit page quatre, dites <i>est</i>."],
       ]},

      {t:'check', h:"Est-ce que c'est clair maintenant ?",
       p:"Quatre questions rapides.",
       qs:[
         {q:"Le conditionnel présent se forme sur le radical…", opts:["du futur","de l'imparfait"], ok:0,
          fb:"Radical du futur, terminaisons de l'imparfait."},
         {q:"« On aurait dû » exprime…", opts:["une proposition","un regret"], ok:1,
          fb:"Et c'est un reproche sans coupable désigné."},
         {q:"Après « si », on peut écrire…", opts:["j'aurais su","j'avais su"], ok:1,
          fb:"Jamais de -rais après si."},
         {q:"Pour un fait vérifié page quatre, on emploie…", opts:["le conditionnel","l'indicatif"], ok:1,
          fb:"Le conditionnel affaiblirait une information sûre."},
       ]},
    ]
  },

  t2conn: {
    eye:'Mini-leçon', tit:"Les connecteurs : dire le rapport exact entre deux idées",
    blocs:[
      {t:'texte', h:"Ce qu'un connecteur fait vraiment",
       p:"Un connecteur ne décore pas la phrase : il <b>annonce ce qui vient</b>. Quand votre interlocuteur entend « cependant », il sait avant même la fin de la phrase qu'une objection arrive et il se prépare à l'entendre. C'est un service qu'on lui rend — et c'est aussi ce qui vous donne le temps de formuler la suite.",
       note:"À ce niveau, le vocabulaire n'est plus le problème. Ce qui distingue une intervention efficace, c'est l'articulation."},

      {t:'ana', h:"L'opposition, en deux nuances",
       p:"Elles ne sont pas interchangeables.",
       mots:[['J\'admets et j\'objecte','{cependant} · {toutefois} · {néanmoins}'],['Je mets en balance','{en revanche} · {par contre}'],['Exemple','L\'écart est réel. {Cependant}, le délai est de dix jours.']],
       note:"<i>Par contre</i> est parfaitement correct au Québec, à l'oral comme à l'écrit courant. <i>En revanche</i> est plus soutenu ; dans une lettre d'affaires, il passe mieux."},

      {t:'ana', h:"La conséquence et l'explication",
       p:"Deux familles qu'on confond souvent, et qui vont dans des sens opposés.",
       mots:[['La conséquence suit','{par conséquent} · {donc} · {c\'est pourquoi} · {d\'où}'],['L\'explication précède','{en effet} · {car} · {en raison de}'],['Le test','« en effet » confirme ce qui vient d\'être dit ; « en fait » le {corrige}']],
       note:"<i>En effet</i> et <i>en fait</i> ne sont pas la même chose. « Le portrait change. En effet, le délai passe à dix jours » confirme. « En fait, le délai est de dix jours » corrige ce qu'on croyait."},

      {t:'ana', h:"La condition et le mode qui suit",
       p:"C'est ici qu'on se trompe le plus, parce que le mode change selon le connecteur.",
       mots:[['+ indicatif','{du moment que} · {dès lors que} · {puisque}'],['+ subjonctif','{à condition que} · {pourvu que} · {à moins que}'],['Exemple','Ça me va, {du moment que} Ferrico n\'impose pas son augmentation.']],
       note:"En cas de doute, employez <i>si</i> + indicatif : c'est toujours correct, et personne ne vous reprochera d'être simple."},

      {t:'texte', h:"Reformuler pour garder la parole",
       p:"<b>Autrement dit</b> et <b>c'est-à-dire</b> ont une vertu que les manuels ne disent pas : ils vous donnent trois secondes. Quand vous sentez que votre phrase est partie de travers, au lieu de vous excuser ou de vous taire, vous enchaînez « autrement dit… » et vous redites la même chose plus clairement. Personne n'y voit une hésitation ; tout le monde y voit un souci de clarté.",
       note:"Même service avec <i>si je résume</i> et <i>ce que je veux dire, c'est que</i>."},

      {t:'ex', h:"Huit connecteurs en situation",
       p:"Tirés de la réunion du mardi.",
       rows:[
         ["L'écart est réel. Cependant, le délai est de dix jours.","admettre puis objecter"],
         ["Ferrico livre en quatre jours ; en revanche, Lachance en demande dix.","mettre en balance"],
         ["Il faudrait doubler le stock ; par conséquent, l'économie tombe à vingt mille.","conséquence"],
         ["Ça change le portrait. En effet, tout le calcul reposait sur le prix.","confirmer et expliquer"],
         ["J'accepte, du moment que Ferrico n'impose rien avant octobre.","condition + indicatif"],
         ["Nous tranchons le seize, à condition que vous ayez les chiffres.","condition + subjonctif"],
         ["Autrement dit, je ne viens pas demander une faveur.","reformuler"],
         ["Deux fournisseurs, donc deux facturations.","conséquence brève"],
       ]},

      {t:'piege', h:"Trois emplois qui trahissent le niveau",
       rows:[
         ["commencer trois phrases de suite par « et »","varier : de plus, par ailleurs, en outre",
          "À l'oral ça passe ; à l'écrit, un texte tenu par des « et » se lit comme une liste de courses."],
         ["confondre « en effet » et « en fait »","le premier confirme, le second corrige",
          "L'erreur inverse le sens de votre phrase, et c'est l'une des plus fréquentes à ce niveau."],
         ["« malgré que »","« bien que » ou « malgré + nom »",
          "<i>Malgré que</i> est critiqué et fait tache à l'écrit. Écrivez <i>bien que le prix soit bon</i> ou <i>malgré le prix</i>."],
       ]},

      {t:'check', h:"Est-ce que c'est clair maintenant ?",
       p:"Quatre questions rapides.",
       qs:[
         {q:"« En effet » sert à…", opts:["confirmer","corriger"], ok:0,
          fb:"C'est « en fait » qui corrige."},
         {q:"« À condition que » est suivi…", opts:["de l'indicatif","du subjonctif"], ok:1,
          fb:"Alors que « du moment que » demande l'indicatif."},
         {q:"« Par contre », au Québec…", opts:["est à éviter partout","est correct à l'oral et à l'écrit courant"], ok:1,
          fb:"« En revanche » reste plus soutenu pour une lettre."},
         {q:"« Autrement dit » vous permet aussi de…", opts:["gagner quelques secondes","conclure la réunion"], ok:0,
          fb:"Et de reformuler sans avoir l'air d'hésiter."},
       ]},
    ]
  },

  t2cr: {
    eye:'Mini-leçon', tit:"Rapporter ce qui a été dit, par écrit",
    blocs:[
      {t:'texte', h:"Un compte rendu n'est pas une transcription",
       p:"C'est la première chose que Manon dit à Nadia, et c'est la seule qui compte. Personne ne relira ce que chacun a dit. Ce qu'on cherche dans un compte rendu, trois semaines plus tard, c'est : <b>qu'est-ce qui a été décidé, qui le fait, pour quand</b>. Tout le reste est du remplissage — les hésitations, les blagues, les redites, les débats qui n'ont mené à rien.",
       note:"Une réunion d'une heure tient en une demi-page. Si votre compte rendu fait trois pages, vous avez transcrit au lieu de rapporter."},

      {t:'ana', h:"Le recul des temps",
       p:"Quand le verbe introducteur est au passé, tout recule d'un cran.",
       mots:[['présent → imparfait','« Je vérifie » → elle a précisé qu\'elle {vérifiait}'],['passé composé → plus-que-parfait','« J\'ai fait le calcul » → elle a indiqué qu\'elle {avait fait}'],['futur → conditionnel','« On tranchera » → elle a annoncé qu\'on {trancherait}']],
       note:"Si le verbe introducteur est au présent (<i>elle dit que…</i>), rien ne recule. C'est le passé qui déclenche le mouvement."},

      {t:'ana', h:"Les pronoms et les repères de temps",
       p:"Ils changent aussi, et on les oublie plus souvent que les temps.",
       mots:[['Les personnes','je → {elle} · tu → {vous} ou le nom'],['Les jours','aujourd\'hui → {ce jour-là} · demain → {le lendemain} · hier → {la veille}'],['Les lieux','ici → {là} · ce bureau-ci → {ce bureau-là}']],
       note:"Un compte rendu qui garde « demain » oblige le lecteur à retrouver la date de la réunion pour comprendre."},

      {t:'ana', h:"Les questions rapportées",
       p:"Elles perdent l'inversion et le point d'interrogation.",
       mots:[['est-ce que → si','« Es-tu sûre ? » → il lui a demandé {si elle était sûre}'],['Mot interrogatif conservé','« Quand ? » → il a demandé {quand} la décision serait prise'],['qu\'est-ce que → ce que','« Qu\'est-ce qu\'on fait ? » → il a demandé {ce qu\'on ferait}']],
       note:"Écrire « il a demandé est-ce qu'elle était sûre » est la faute la plus visible du discours rapporté."},

      {t:'texte', h:"Le verbe introducteur porte l'intention",
       p:"Répéter « a dit » huit fois donne un texte plat où l'on ne distingue plus une objection d'un engagement. Le verbe fait ce travail à lui seul : <b>a rappelé</b> (c'était déjà connu), <b>a précisé</b> (il manquait un détail), <b>a objecté</b> (il n'était pas d'accord), <b>a proposé</b> (une solution), <b>s'est engagé à</b> (il le fera), <b>a reconnu</b> (il admet), <b>a demandé</b>.",
       note:"Choisir le bon verbe est un acte de rédaction, pas de style : « a proposé » et « s'est engagé à » n'ont pas les mêmes conséquences un mois plus tard."},

      {t:'ex', h:"Huit transformations de la réunion",
       p:"À gauche ce qui a été dit, à droite ce qui s'écrit.",
       rows:[
         ["« Je vérifie deux fois. »","Elle a précisé qu'elle vérifiait deux fois."],
         ["« Ça me force à doubler mon stock. »","Il a objecté que cela le forçait à doubler son stock."],
         ["« Es-tu sûre de ton affaire ? »","Il lui a demandé si elle était sûre de son information."],
         ["« On tranche à la réunion du seize. »","Elle a annoncé qu'on trancherait à la réunion du seize."],
         ["« J'ai fait le calcul. »","Elle a indiqué qu'elle avait fait le calcul."],
         ["« Envoie-le avant jeudi. »","Elle lui a demandé de l'envoyer avant le jeudi."],
         ["« C'est ma faute. »","Elle a reconnu que c'était sa faute."],
         ["« Je note les trois décisions. »","Elle s'est engagée à noter les trois décisions."],
       ]},

      {t:'piege', h:"Trois erreurs de compte rendu",
       rows:[
         ["« Il a demandé est-ce qu'elle était sûre »","« … s'il elle était sûre » → « si elle était sûre »",
          "La question rapportée n'est plus une question : ni inversion, ni « est-ce que », ni point d'interrogation."],
         ["garder « demain » et « hier »","« le lendemain », « la veille »",
          "Le lecteur du compte rendu n'était pas dans la salle et ne connaît pas la date de référence."],
         ["rapporter les propos vifs","rapporter la décision",
          "Un désaccord se note « X a objecté que… ». Les mots exacts d'un moment de tension n'ont rien à faire dans un document qui circule."],
       ]},

      {t:'check', h:"Est-ce que c'est clair maintenant ?",
       p:"Quatre questions rapides.",
       qs:[
         {q:"« Je vérifie » rapporté au passé devient…", opts:["qu'elle vérifiait","qu'elle a vérifié"], ok:0,
          fb:"Présent → imparfait."},
         {q:"« Est-ce que » rapporté devient…", opts:["si","que"], ok:0,
          fb:"Et l'inversion disparaît."},
         {q:"« Demain » rapporté devient…", opts:["le lendemain","ce jour-là"], ok:0,
          fb:"« Ce jour-là » traduit « aujourd'hui »."},
         {q:"Un compte rendu garde…", opts:["les propos de chacun","les décisions, les responsables, les dates"], ok:1,
          fb:"Le reste appartient à la réunion."},
       ]},
    ]
  },

  t3rel: {
    eye:'Mini-leçon', tit:"Auquel, dont, ce à quoi : le pronom porte la préposition",
    blocs:[
      {t:'texte', h:"Un seul principe à comprendre",
       p:"Vous savez déjà employer <i>qui</i>, <i>que</i> et <i>où</i>. Les pronoms composés servent quand le verbe de la subordonnée <b>exige une préposition</b>. On s'adresse <b>à</b> un service : le service <b>auquel</b> je m'adresse. On parle <b>de</b> quelque chose : la démarche <b>dont</b> je parle. Trouvez la préposition du verbe, et le pronom se choisit tout seul.",
       note:"C'est le seul point de grammaire de ce module où l'on gagne à se poser une question : « ce verbe demande quelle préposition ? »"},

      {t:'ana', h:"Avec « à »",
       p:"Les quatre formes, selon le genre et le nombre du nom repris.",
       mots:[['Masculin singulier','le service {auquel} je m\'adresse'],['Féminin singulier','la formation {à laquelle} elle pense'],['Pluriel','les cours {auxquels} · les questions {auxquelles}']],
       note:"Pour une personne, <i>à qui</i> est plus naturel : <i>la conseillère à qui j'ai parlé</i>. Pour une chose, seulement <i>à laquelle</i>."},

      {t:'ana', h:"Avec « de » : presque toujours « dont »",
       p:"C'est la forme la plus fréquente, et la plus simple.",
       mots:[['parler de','la démarche {dont} je parle'],['avoir besoin de','le document {dont} j\'ai besoin'],['connaître les étapes de','une démarche {dont} je ne connaissais pas les étapes']],
       note:"<b>duquel</b> ne s'emploie que dans une locution : <i>au bout duquel, à côté duquel, en raison duquel</i>. Ailleurs, <i>dont</i> gagne toujours."},

      {t:'ana', h:"Avec les autres prépositions",
       p:"On garde la préposition et on ajoute <i>lequel</i>.",
       mots:[['sur','le formulaire {sur lequel} elle a écrit'],['pour','la raison {pour laquelle} il refuse'],['avec','les collègues {avec lesquels} elle travaille'],['sans','un cours {sans lequel} elle ne progresserait pas']],
       note:"<i>avec lesquels</i> ou <i>avec qui</i> pour des personnes : les deux sont corrects, le second est plus courant à l'oral."},

      {t:'texte', h:"Quand il n'y a pas de nom devant",
       p:"Si le pronom ne reprend aucun nom mais une idée entière, on ajoute <b>ce</b> : <b>ce dont</b> (de), <b>ce à quoi</b> (à), <b>ce que</b>, <b>ce qui</b>. « <b>Ce dont</b> vous me parlez est un besoin précis » — <i>ce</i> reprend tout ce que la personne vient d'expliquer, pas un nom particulier.",
       note:"C'est aussi une excellente façon de commencer une intervention en réunion : <i>Ce à quoi je pensais, c'est…</i>"},

      {t:'ex', h:"Huit phrases du défi",
       p:"La préposition du verbe est en gras dans la colonne de droite.",
       rows:[
         ["Le service auquel je dois m'adresser.","s'adresser <b>à</b>"],
         ["Ce dont vous me parlez est un besoin précis.","parler <b>de</b>, sans nom devant"],
         ["La formation à laquelle elle pense.","penser <b>à</b>, féminin"],
         ["Une démarche dont je ne connaissais pas les étapes.","les étapes <b>de</b> la démarche"],
         ["Le formulaire sur lequel elle a écrit son numéro.","écrire <b>sur</b>"],
         ["L'entreprise dont elle vient.","venir <b>de</b>"],
         ["Ce à quoi je m'attendais, c'était un refus.","s'attendre <b>à</b>, sans nom"],
         ["Le centre au bout duquel elle marche.","au bout <b>de</b> : locution"],
       ]},

      {t:'piege', h:"Trois pièges classiques",
       rows:[
         ["« la chose que j'ai besoin »","« la chose dont j'ai besoin »",
          "<i>Avoir besoin</i> demande <i>de</i>. C'est la faute la plus fréquente de tout ce point de grammaire."],
         ["« le service que je m'adresse »","« le service auquel je m'adresse »",
          "<i>Que</i> ne peut jamais porter une préposition. Dès qu'il y a une préposition, il faut une forme composée."],
         ["« dont j'en ai besoin »","« dont j'ai besoin »",
          "<i>Dont</i> contient déjà le <i>de</i> : ajouter <i>en</i> le répète."],
       ]},

      {t:'check', h:"Est-ce que c'est clair maintenant ?",
       p:"Quatre questions rapides.",
       qs:[
         {q:"« Avoir besoin » se construit avec…", opts:["de → dont","à → auquel"], ok:0,
          fb:"J'ai besoin <b>de</b> ce document → le document dont j'ai besoin."},
         {q:"« La formation ___ elle pense »", opts:["à laquelle","dont"], ok:0,
          fb:"Penser <b>à</b> quelque chose."},
         {q:"« Dont j'en ai besoin » est…", opts:["correct","une répétition"], ok:1,
          fb:"Dont contient déjà le « de »."},
         {q:"Quand aucun nom ne précède, on emploie…", opts:["ce dont / ce à quoi","dont / auquel"], ok:0,
          fb:"Le « ce » reprend une idée entière."},
       ]},
    ]
  },

  t3hyp: {
    eye:'Mini-leçon', tit:"Si j'avais su : chiffrer ce qu'une lacune a coûté",
    blocs:[
      {t:'texte', h:"Une grammaire qui sert à convaincre",
       p:"L'hypothèse sur le passé n'est pas un exercice d'école : c'est l'outil qui transforme un souhait en argument. « J'aimerais suivre un cours » ne convainc personne. « Si j'avais su utiliser le module fournisseurs l'an dernier, j'aurais économisé quarante heures » place un chiffre devant votre superviseure. C'est la même idée, dite dans la langue où les décisions se prennent.",
       note:"Claudia Fortin le dit autrement : l'envie d'apprendre, gardez-la pour vous."},

      {t:'ana', h:"Le montage, en deux moitiés",
       p:"Chaque moitié a son temps, et ils ne s'échangent pas.",
       mots:[['La condition','{si} + plus-que-parfait'],['Le résultat','{conditionnel passé}'],['En entier','{Si} j\'{avais su}, j\'{aurais économisé} quarante heures.']],
       note:"L'ordre des deux moitiés est libre : <i>J'aurais économisé quarante heures si j'avais su</i> dit exactement la même chose."},

      {t:'ana', h:"Le plus-que-parfait",
       p:"C'est le passé du passé : <b>avoir</b> ou <b>être</b> à l'imparfait, plus le participe.",
       mots:[['avoir','j\'{avais su} · nous {avions eu} · elle {avait lu}'],['être','elle {était partie} · nous {étions arrivés}'],['Accord','avec être, on accorde : nous {étions prévenus}']],
       note:"Le même temps sert aussi à raconter : <i>Elle avait déjà tenu la comptabilité d'une école avant d'arriver ici.</i>"},

      {t:'ana', h:"Les trois hypothèses, côte à côte",
       p:"Une seule chose change : la distance avec le réel.",
       mots:[['C\'est probable','{si} + présent → futur : si vous m\'écrivez, je {répondrai}'],['C\'est imaginé','{si} + imparfait → conditionnel présent : si le cours était le jour, je m\'{inscrirais}'],['C\'est trop tard','{si} + plus-que-parfait → conditionnel passé : si j\'avais su, j\'{aurais économisé}']],
       note:"Apprenez les trois ensemble : c'est en les comparant qu'on cesse de les mélanger."},

      {t:'texte', h:"La règle absolue, sans aucune exception",
       p:"<b>Après « si » de condition, on n'écrit jamais -rais ni -rait.</b> Ni conditionnel présent, ni conditionnel passé, jamais. C'est la faute que les francophones eux-mêmes commettent et qui se remarque le plus. Retenez la formule : « les si n'aiment pas les rais ».",
       note:"Attention : le <i>si</i> d'une question rapportée n'est pas le <i>si</i> de condition, et lui accepte le conditionnel : <i>Je me demande s'il accepterait.</i>"},

      {t:'ex', h:"Huit hypothèses de travail",
       p:"Toutes servent à justifier quelque chose.",
       rows:[
         ["Si j'avais su utiliser le module, j'aurais économisé 40 heures.","chiffrer une lacune"],
         ["Si nous avions eu cette formation, nous n'aurions pas repris 12 factures.","chiffrer une conséquence"],
         ["Si elle avait lu la page quatre, elle en aurait parlé avant.","expliquer un manque"],
         ["Si le cours était offert le jour, je m'inscrirais tout de suite.","montrer sa volonté"],
         ["Si vous m'écrivez cette semaine, je répondrai avant vendredi.","engagement réel"],
         ["Si l'entreprise dépassait deux millions, la dépense serait prévue.","hypothèse sur le présent"],
         ["Si j'avais demandé plus tôt, la formation aurait commencé en septembre.","regret daté"],
         ["Si nous avions été prévenus, nous aurions doublé le stock.","reproche partagé"],
       ]},

      {t:'piege', h:"Trois pièges",
       rows:[
         ["« si j'aurais su »","« si j'avais su »",
          "La faute la plus repérée du français. Aucune exception : après si de condition, jamais de conditionnel."],
         ["oublier l'accord avec être","« si nous avions été prévenus »",
          "Au plus-que-parfait avec <i>être</i>, le participe s'accorde avec le sujet."],
         ["mélanger les trois hypothèses","choisir selon la distance au réel",
          "<i>Si j'avais su, je m'inscrirais</i> mélange le passé et le présent. Ce n'est pas toujours faux, mais dans une justification, ça brouille l'argument."],
       ]},

      {t:'check', h:"Est-ce que c'est clair maintenant ?",
       p:"Quatre questions rapides.",
       qs:[
         {q:"« Si » de condition + …", opts:["plus-que-parfait","conditionnel passé"], ok:0,
          fb:"Le conditionnel est dans l'autre moitié de la phrase."},
         {q:"« Si le cours était le jour, je ___ »", opts:["m'inscrirais","me serais inscrite"], ok:0,
          fb:"Imparfait → conditionnel présent."},
         {q:"Le plus-que-parfait se forme avec…", opts:["l'imparfait de avoir/être","le présent de avoir/être"], ok:0,
          fb:"j'avais su, elle était partie."},
         {q:"À quoi sert l'hypothèse passée, dans une demande ?", opts:["à chiffrer ce qu'une lacune a coûté","à s'excuser"], ok:0,
          fb:"C'est l'argument, pas l'excuse."},
       ]},
    ]
  },

  t3reprise: {
    eye:'Mini-leçon', tit:"Reprendre sans répéter : ce qui fait tenir un texte",
    blocs:[
      {t:'texte', h:"Le défaut qu'on ne voit pas dans son propre texte",
       p:"Relisez n'importe quel courriel écrit vite : le même nom y revient quatre fois en six lignes. Le lecteur le remarque tout de suite, l'auteur jamais. Ce n'est pas une question d'élégance : un texte qui répète oblige à relire pour savoir si l'on parle de la même chose ou d'une autre. La reprise est ce qui relie les phrases entre elles — sans elle, un paragraphe n'est qu'une suite de phrases.",
       note:"Au niveau 8, c'est le point qui sépare un texte correct d'un texte professionnel."},

      {t:'ana', h:"Quatre façons de reprendre",
       p:"De la plus simple à la plus utile.",
       mots:[['Le pronom','La soumission… {elle} · {celle-ci} · {ce dernier}'],['Le synonyme','la formation → {le cours}, {la session}'],['Le nom générique','…→ {cette démarche}, {cette solution}, {ce document}'],['La nominalisation','Lachance a livré en dix jours → {ce délai de livraison}']],
       note:"Les deux dernières sont celles qui manquent le plus souvent, et ce sont les plus efficaces."},

      {t:'ana', h:"La nominalisation, geste par geste",
       p:"On transforme le verbe de la phrase précédente en nom, et on le fait précéder d'un démonstratif.",
       mots:[['augmenter','→ {cette augmentation}, {cette hausse}'],['reporter','→ {ce report}'],['livrer en dix jours','→ {ce délai de livraison}'],['décider','→ {cette décision}']],
       note:"C'est la reprise reine du compte rendu : elle résume une phrase entière en trois mots, et elle porte un jugement discret sur ce qui vient d'être dit."},

      {t:'ana', h:"Le nom générique",
       p:"Un mot large qui range ce qui précède dans une catégorie.",
       mots:[['Pour une action','{cette démarche} · {cette mesure} · {cette initiative}'],['Pour une idée','{cette solution} · {cette proposition} · {cette approche}'],['Pour un écrit','{ce document} · {ce formulaire} · {cette lettre}']],
       note:"Le choix du nom générique n'est pas neutre : <i>cette proposition</i> et <i>cette exigence</i> ne racontent pas la même réunion."},

      {t:'texte', h:"Le danger : la reprise qui laisse un doute",
       p:"Une reprise ne vaut que si personne ne peut se tromper sur ce qu'elle remplace. « Nadia a parlé à Manon de sa demande. <b>Celle-ci</b> l'a acceptée. » Qui a accepté ? La règle est simple : <b>celui-ci</b> et <b>ce dernier</b> reprennent le <b>dernier</b> élément nommé. Dans un texte d'affaires, une ambiguïté coûte un appel téléphonique — parfois une erreur.",
       note:"Dans le doute, répétez le nom. Une répétition claire vaut mieux qu'une élégance obscure."},

      {t:'ex', h:"Six reprises en situation",
       p:"À gauche la répétition, à droite ce qu'on écrit.",
       rows:[
         ["Lachance livre en dix jours. Dix jours nous mettent en défaut.","Ce délai nous met en défaut."],
         ["J'ai suivi une formation. Cette formation portait sur…","Ce cours portait sur…"],
         ["Le fournisseur a augmenté ses prix. L'augmentation…","Cette hausse…"],
         ["Nous avons reporté la décision. La décision est notée.","Ce report est noté au compte rendu."],
         ["Le formulaire fait deux pages. Le formulaire se remplit en ligne.","Ce document se remplit en ligne."],
         ["Elle a proposé un partage. Le partage a été retenu.","Cette solution a été retenue."],
       ]},

      {t:'piege', h:"Trois pièges de reprise",
       rows:[
         ["« celle-ci » quand deux femmes précèdent","répéter le nom",
          "« Nadia a parlé à Manon ; celle-ci a accepté » : la règle dit Manon, mais votre lecteur hésitera une seconde. Une seconde de trop."],
         ["chercher un synonyme à tout prix","garder le mot juste",
          "Les termes techniques ne se remplacent pas. <i>Le compte rendu</i> reste <i>le compte rendu</i> : lui trouver un synonyme sème le doute."],
         ["« ce dernier » pour le premier élément","« le premier », « celui-là »",
          "<i>Ce dernier</i> désigne toujours le dernier nommé. L'employer autrement inverse le sens de la phrase."],
       ]},

      {t:'check', h:"Est-ce que c'est clair maintenant ?",
       p:"Quatre questions rapides.",
       qs:[
         {q:"« Ce dernier » reprend…", opts:["le dernier élément nommé","le sujet de la phrase"], ok:0,
          fb:"Toujours le dernier nommé."},
         {q:"« Lachance a livré en dix jours » → nominalisation :", opts:["ce délai de livraison","cette entreprise"], ok:0,
          fb:"Le verbe devient un nom précédé d'un démonstratif."},
         {q:"Un terme technique…", opts:["se remplace par un synonyme","se répète tel quel"], ok:1,
          fb:"Changer de mot ferait croire qu'on change de chose."},
         {q:"Devant une reprise ambiguë, mieux vaut…", opts:["répéter le nom","laisser le lecteur deviner"], ok:0,
          fb:"La clarté passe avant l'élégance."},
       ]},
    ]
  },

};
