const PLUS = {

  // ════════════════════════════════════════════════════════════════════════
  prPhon: {
    eye:'Mini-leçon', tit:"Le son « é » et le son « è »",
    blocs:[
      {t:'texte', h:"Deux « e » qui ne s'ouvrent pas pareil",
       p:"Le français a deux façons de dire la lettre « e » quand elle porte un accent ou qu'elle finit un mot. Le premier son est fermé, bref, la bouche presque close : c'est le « é » de relevé, de secrétariat, d'annoncer. Le second est ouvert, plus long, la mâchoire descend d'un doigt : c'est le « è » de conseillère, de pièce, d'après. Toutes les langues n'ont pas les deux, et beaucoup d'élèves les rendent par un seul son intermédiaire, qui n'est ni l'un ni l'autre.",
       note:"Dans ce module, ce n'est pas une question d'accent : c'est une question de sens. « Je voudrais parler » et « je voudrai parler » ne se distinguent que par ce son — et l'une des deux phrases ne se dit pas au comptoir."},

      {t:'ana', h:"Le « é » fermé : la mâchoire reste haute",
       p:"Les lèvres s'étirent sur les côtés, la mâchoire ne bouge presque pas, le son est bref. On l'écrit de quatre façons, et toutes les quatre sont dans le vocabulaire du bureau.",
       mots:[["Avec l'accent aigu","un relevé · l'échéance · signé · autorisé"],["À la fin d'un verbe : -er, -ez","annoncer · remplir et rapporter · vous devez · vous signerez",true],["Dans les petits mots : -es","les dates · des papiers · mes documents"]],
       say:"Un relevé. Annoncer. Vous devez.",
       note:"Le « -er » d'un infinitif se dit exactement comme un « é ». C'est pourquoi « annoncer » et « annoncé » sont identiques à l'oreille : c'est la grammaire qui les sépare, jamais le son."},

      {t:'ana', h:"Le « è » ouvert : la mâchoire descend",
       p:"La bouche s'ouvre d'un doigt, la langue reste basse, le son dure plus longtemps. Six orthographes, un seul son.",
       mots:[["Avec l'accent grave ou circonflexe","une pièce · après · une échéance · la fenêtre"],["Avec « ai » et « ei »","je voudrais · j'aimerais · une semaine · seize",true],["À la fin : -et, -ère, -elle","un billet · une conseillère · elle appelle"]],
       say:"Une conseillère. Je voudrais. Après.",
       note:"« Une échéance » porte les deux sons à la suite : é-ché-ance, avec un « é » fermé deux fois. « Après » n'en porte qu'un, ouvert. Dites-les l'un après l'autre pour sentir la mâchoire bouger."},

      {t:'ana', h:"Le piège de la politesse : -ais contre -ai",
       p:"C'est la seule opposition de ce module qui change vraiment la phrase. Le conditionnel de politesse se termine par « -ais », qui se dit avec un « è » ouvert. Le futur se termine par « -ai », qui se dit avec un « é » fermé.",
       mots:[["La demande polie, en « è »","je voudrais · j'aimerais · je pourrais · je souhaiterais"],["Le futur, en « é »","je voudrai · j'aimerai · je pourrai · je reviendrai",true],["Ce qu'on entend au comptoir","je voudrais savoir si · j'aimerais comprendre pourquoi"]],
       say:"Je voudrais savoir. Je reviendrai.",
       note:"Une personne qui dit « je voudrai savoir » au comptoir est comprise quand même — mais elle a l'air d'annoncer ce qu'elle voudra demain. Ouvrez la bouche sur la dernière syllabe, et la demande redevient une demande."},

      {t:'labo', h:"Écoutez la paire, puis le mot dans sa phrase",
       p:"Choisissez une paire et écoutez la différence, puis le mot replacé dans une phrase du centre.",
       axes:[{id:'p', lbl:'Quelle paire ?', opts:[
         ['a','les / lait'],
         ['b','fée / fait'],
         ['c','le relevé / la conseillère'],
         ['d','je voudrai / je voudrais'],
         ['e','les quatre à la suite']]}],
       out:{
         a:{w:['un relevé'], say:"Les. Lait. Les dates du relevé sont exactes.", n:"« les » ferme, « lait » ouvre"},
         b:{w:['une échéance'], say:"Fée. Fait. L'échéance est faite pour être respectée.", n:"deux mots courts, deux mâchoires"},
         c:{w:['un relevé','une conseillère'], say:"Le relevé. La conseillère. La conseillère a demandé le relevé.", n:"la paire du module, dans une seule phrase"},
         d:{w:['le secrétariat'], say:"Je voudrai. Je voudrais. Je voudrais parler au secrétariat.", n:"le futur, puis la demande polie"},
         e:{w:['un relevé','une conseillère'], say:"Les, lait. Fée, fait. Le relevé, la conseillère. Je voudrai, je voudrais.", n:"quatre paires à la suite, sans reprendre son souffle"},
       },
       note:"Écoutez chaque paire deux fois : la première pour entendre les deux mots, la seconde en gardant deux doigts sous le menton pour sentir la mâchoire descendre sur le second."},

      {t:'ex', h:"À écouter et à répéter",
       p:"Six phrases prises dans les dialogues du module.",
       rows:[
         ["Je voudrais savoir si je garde ma place.","« è » deux fois : voudrais, place"],
         ["Le relevé des apprentissages vient du ministère.","« é » trois fois de suite"],
         ["La conseillère reçoit sur rendez-vous après midi.","« è » au milieu et à la fin"],
         ["Vous devez signer cet avis et le rapporter.","« é » de devez, de signer, de rapporter"],
         ["L'échéance est écrite en gras, tout en haut.","deux « é » fermés, puis un « è » ouvert"],
         ["J'aimerais comprendre ce que vous demandez.","« è » au début, « é » à la fin"],
       ]},

      {t:'piege', h:"Trois pièges des deux « e »",
       rows:[
         ["dire un seul son entre les deux","un « e » mou qui ne ferme ni n'ouvre",
          "C'est le défaut le plus courant, et le plus discret : personne ne vous corrige, mais on vous fait répéter. Exagérez pendant une semaine — bouche presque fermée sur « é », mâchoire tombée sur « è » — puis relâchez : il en restera juste assez."],
         ["fermer le « -ais » du conditionnel","« je voudré savoir » au lieu de « je voudrais savoir »",
          "La demande polie devient un futur, et l'oreille québécoise l'entend tout de suite. C'est la seule erreur de prononciation de ce module qui change ce que la phrase dit."],
         ["croire que l'accent écrit décide toujours","« une semaine » n'a aucun accent et se dit avec « è »",
          "Le son ne se lit pas seulement à l'accent : « ai », « ei », « -et » et « -ère » donnent tous un « è » sans le moindre accent écrit. C'est l'oreille qui commande, l'orthographe ne fait que suivre."],
       ]},

      {t:'check', h:"Est-ce que c'est clair maintenant ?",
       p:"Quatre questions rapides.",
       qs:[
         {q:"Dans « annoncer », la fin se dit…", opts:["comme « é »","comme « è »"], ok:0,
          fb:"Comme « é ». Le « -er » d'un infinitif se dit toujours ainsi."},
         {q:"« Je voudrais » se termine par…", opts:["un « é » fermé","un « è » ouvert"], ok:1,
          fb:"Un « è » ouvert. C'est ce qui en fait une demande polie et non un futur."},
         {q:"« Une semaine » contient…", opts:["un « è » ouvert","un « é » fermé"], ok:0,
          fb:"Un « è » ouvert, écrit « ai », sans accent."},
         {q:"Sur le son « è », la mâchoire…", opts:["reste haute","descend d'un doigt"], ok:1,
          fb:"Elle descend. C'est ce que vous sentez avec deux doigts sous le menton."},
       ]},
    ]
  },

  // ════════════════════════════════════════════════════════════════════════
  prMot: {
    eye:'Mini-leçon', tit:"Quatre papiers qu'on confond tout le temps",
    blocs:[
      {t:'texte', h:"Un centre fonctionne au papier, même quand tout est en ligne",
       p:"Dans un centre d'éducation des adultes, chaque démarche produit un document, et chaque document a un sens précis. On croit souvent qu'il s'agit du même papier sous quatre noms : ce n'est pas le cas. Deux vont du centre vers vous — l'avis et l'attestation. Un va de vous vers le centre — le formulaire. Et un vient d'ailleurs, du ministère — le relevé des apprentissages. Se tromper de nom au comptoir, c'est repartir sans ce qu'on était venu chercher.",
       note:"Le mot « papier » ne fait de mal à personne dans une conversation, mais il ne suffit pas au comptoir : la personne en face doit savoir quoi ouvrir dans le système."},

      {t:'ana', h:"L'avis : le centre décide et vous informe",
       p:"Il vient de l'établissement, il annonce une décision déjà prise, il porte des dates et il demande souvent une signature. On ne discute pas un avis : on le lit, on le signe, on le rapporte.",
       mots:[["Ce qu'il contient toujours","un objet en une ligne · au moins une date · ce que vous devez faire"],["Les avis qu'on reçoit ici","avis de confirmation d'absence · avis de changement de groupe",true],["Ce qu'on en fait","le lire deux fois · le signer · en garder une copie"]],
       say:"L'avis arrive par courriel et il faut le signer.",
       note:"Un avis qui vous surprend ne se conteste pas par courriel : on prend un rendez-vous. Répondre à un avis par une explication écrite fait perdre une semaine à tout le monde."},

      {t:'ana', h:"Le formulaire : c'est vous qui écrivez au centre",
       p:"La même feuille pour tout le monde, avec des cases. C'est ce qui fait entrer votre demande dans le dossier. Une demande faite seulement de vive voix n'existe nulle part le lendemain matin.",
       mots:[["Ce qu'il demande","vos coordonnées · des dates · un motif en une phrase"],["Où le trouver","au comptoir du secrétariat · souvent en ligne, sur le site du centre",true],["Ce qui le rend recevable","signé · daté · remis avant l'échéance"]],
       say:"Ce formulaire se remet au secrétariat avant le départ.",
       note:"La case « motif » attend une phrase, pas un paragraphe. « Opération d'un proche à l'étranger » suffit ; le détail médical ne regarde pas le dossier scolaire."},

      {t:'ana', h:"L'attestation et le relevé : deux preuves, deux moments",
       p:"L'attestation prouve où vous êtes aujourd'hui. Le relevé prouve ce que vous avez réussi hier. Ce ne sont ni les mêmes bureaux, ni les mêmes délais.",
       mots:[["L'attestation de fréquentation","imprimée au secrétariat, sur-le-champ · pour un employeur, un propriétaire, un service"],["Le relevé des apprentissages","envoyé par le ministère · plusieurs semaines après la fin du cours",true],["La question à poser au comptoir","« C'est pour prouver que je suis inscrite, ou pour prouver ce que j'ai réussi ? »"]],
       say:"Son employeur demande une attestation de fréquentation scolaire.",
       note:"Demander un relevé en février, c'est demander une chose que personne au centre ne peut imprimer. Le comptoir vous le dira poliment — mais vous aurez fait le voyage pour rien."},

      {t:'labo', h:"Un mot, sa phrase, et le sens exact",
       p:"Choisissez un papier et écoutez-le dans une phrase du centre.",
       axes:[{id:'m', lbl:'Quel document ?', opts:[
         ['a','un avis'],
         ['b','un formulaire'],
         ['c','une attestation'],
         ['d','un relevé'],
         ['e','une pièce justificative']]}],
       out:{
         a:{w:['un avis'], say:"L'avis arrive par courriel et il faut le signer.", n:"du centre vers vous, avec des dates"},
         b:{w:['un formulaire'], say:"Ce formulaire se remet au secrétariat avant le départ.", n:"de vous vers le centre, avec des cases"},
         c:{w:['une attestation'], say:"Son employeur demande une attestation de fréquentation scolaire.", n:"la preuve d'aujourd'hui, imprimée tout de suite"},
         d:{w:['un relevé'], say:"Le relevé des apprentissages arrive après la fin du cours.", n:"la preuve de ce qui est réussi, envoyée par le ministère"},
         e:{w:['une pièce justificative'], say:"Elle apportera sa pièce justificative à son retour.", n:"ce qui prouve le motif : billet, lettre, reçu"},
       },
       note:"Écoutez chaque mot deux fois : une fois seul, une fois dans sa phrase. C'est la phrase qui fixe le mot dans la mémoire, pas le mot tout seul."},

      {t:'ex', h:"À écouter et à répéter",
       p:"Six phrases à dire au comptoir sans hésiter.",
       rows:[
         ["Je viens vous remettre mon formulaire d'absence signé.","de vous vers le centre"],
         ["J'ai reçu un avis et je viens le rapporter.","du centre vers vous"],
         ["Je voudrais une attestation de fréquentation, s'il vous plaît.","la preuve d'aujourd'hui"],
         ["Est-ce que mon relevé des apprentissages est déjà parti ?","la preuve de ce qui est réussi"],
         ["J'apporterai ma pièce justificative à mon retour.","ce qui prouve le motif"],
         ["Est-ce que je peux garder une copie de ce document ?","la phrase qui sauve un dossier"],
       ]},

      {t:'piege', h:"Trois confusions qui font perdre un voyage",
       rows:[
         ["demander un relevé au secrétariat","« Je voudrais mon relevé de notes, s'il vous plaît. »",
          "Le relevé des apprentissages est un document du ministère, produit après la fin du cours. Le secrétariat ne peut pas l'imprimer. Ce que vous cherchez, en cours de session, c'est une attestation de fréquentation."],
         ["répondre à un avis par un courriel","« Bonjour, je voulais expliquer pourquoi… »",
          "Un avis annonce une décision. Un courriel d'explication n'ouvre aucun dossier et n'arrête aucune échéance. Si la décision vous pose un problème, demandez un rendez-vous — et remettez quand même l'avis signé."],
         ["croire qu'une demande orale suffit","« Je l'ai dit à madame au comptoir la semaine passée. »",
          "Une conversation ne laisse aucune trace dans un système. Le formulaire, lui, en laisse une, datée. C'est pour ça qu'on vous le fait remplir même quand vous venez de tout expliquer de vive voix."],
       ]},

      {t:'check', h:"Est-ce que c'est clair maintenant ?",
       p:"Quatre questions rapides.",
       qs:[
         {q:"Le document qui va de vous vers le centre s'appelle…", opts:["un formulaire","un avis"], ok:0,
          fb:"Un formulaire. L'avis, lui, va du centre vers vous."},
         {q:"Pour prouver à un employeur que vous êtes inscrit, il faut…", opts:["un relevé","une attestation"], ok:1,
          fb:"Une attestation de fréquentation, imprimée au secrétariat sur-le-champ."},
         {q:"Le relevé des apprentissages vient…", opts:["du ministère","du secrétariat"], ok:0,
          fb:"Du ministère, plusieurs semaines après la fin du cours."},
         {q:"Un avis reçu se…", opts:["signe et se rapporte","commente par courriel"], ok:0,
          fb:"Il se signe et se rapporte. Un problème se règle en rendez-vous, pas en réponse écrite."},
       ]},
    ]
  },

  // ════════════════════════════════════════════════════════════════════════
  t1int: {
    eye:'Mini-leçon', tit:"La question glissée dans une phrase",
    blocs:[
      {t:'texte', h:"Pourquoi ne pas poser la question directement",
       p:"Une question directe est courte et efficace : « Est-ce que je garde ma place ? » Il n'y a rien de fautif là-dedans. Le problème apparaît quand il y en a trois de suite : au comptoir, cela devient un interrogatoire, et la personne en face se met à répondre par oui et par non au lieu d'expliquer. La question glissée dans une phrase — « Je voudrais savoir si je garde ma place » — dit exactement la même chose, mais elle laisse à l'autre le temps de chercher, de nuancer, d'ajouter ce que vous n'avez pas pensé à demander.",
       note:"Le programme du niveau 5 parle de discours simples mais organisés. C'est précisément ça : la même information, rangée autrement, pour que la conversation continue au lieu de s'arrêter à chaque réponse."},

      {t:'ana', h:"« Est-ce que » devient « si »",
       p:"C'est la transformation la plus utile du module. Le « est-ce que » disparaît, le « si » prend sa place, et le point d'interrogation s'en va avec lui.",
       mots:[["La forme directe","Est-ce que je garde ma place ? · Est-ce que le formulaire est prêt ?"],["La forme glissée","Je voudrais savoir si je garde ma place. · Pourriez-vous me dire si le formulaire est prêt.",true],["Ce qui ne change jamais","le sujet reste devant le verbe · le reste de la phrase ne bouge pas"]],
       say:"Je voudrais savoir si je garde ma place dans le groupe.",
       note:"Ce « si » n'a rien à voir avec le « si » de la condition (« si je pars, je préviens »). Ici, il ne pose aucune condition : il porte une question."},

      {t:'ana', h:"Les mots de question se replacent tels quels",
       p:"Quand, où, pourquoi, comment, combien de : ceux-là passent sans changer une lettre. Il n'y a qu'à supprimer l'inversion du sujet et le point d'interrogation.",
       mots:[["Le temps","Pourriez-vous me dire quand je dois remettre le formulaire."],["Le lieu","Je voudrais savoir où se donne le rattrapage.",true],["La quantité et la manière","J'aimerais savoir combien de jours ça prend. · Dites-moi comment il faut remplir la case."]],
       say:"Pourriez-vous me dire quand je dois remettre le formulaire.",
       note:"« Quand dois-je » devient « quand je dois ». C'est l'inversion qui tombe, jamais le mot de question — et c'est là que la plupart des erreurs se logent."},

      {t:'ana', h:"« Qu'est-ce que » devient « ce que »",
       p:"La deuxième transformation à retenir, et la dernière. Le « qu'est-ce que » devient « ce que », le « qu'est-ce qui » devient « ce qui ».",
       mots:[["Complément","Qu'est-ce qu'il faut écrire ? → Je ne sais pas ce qu'il faut écrire."],["Sujet","Qu'est-ce qui manque ? → Dites-moi ce qui manque dans mon dossier.",true],["Les quatre entrées à connaître","Je voudrais savoir… · Pourriez-vous me dire… · Je ne sais pas… · J'aimerais comprendre…"]],
       say:"Je ne sais pas ce qu'il faut écrire dans la case du motif.",
       note:"« Ce que » et « ce qui » se choisissent comme « que » et « qui » : si le mot fait l'action, c'est « ce qui » ; s'il la subit, c'est « ce que »."},

      {t:'labo', h:"La même demande, des deux façons",
       p:"Choisissez une demande et écoutez-la posée directement, puis glissée dans une phrase.",
       axes:[{id:'d', lbl:'Quelle demande ?', opts:[
         ['a','garder sa place'],
         ['b','la date de remise'],
         ['c','ce qu'+"'"+'il faut écrire'],
         ['d','le lieu du rattrapage'],
         ['e','le délai de réponse']]}],
       out:{
         a:{w:['une absence'], say:"Est-ce que je garde ma place ? Je voudrais savoir si je garde ma place.", n:"est-ce que devient si"},
         b:{w:['une échéance'], say:"Quand dois-je remettre le formulaire ? Pourriez-vous me dire quand je dois remettre le formulaire.", n:"l'inversion tombe, le mot de question reste"},
         c:{w:['un motif'], say:"Qu'est-ce qu'il faut écrire ? Je ne sais pas ce qu'il faut écrire.", n:"qu'est-ce que devient ce que"},
         d:{w:['un rattrapage','un local'], say:"Le rattrapage se donne où ? J'aimerais comprendre où se donne le rattrapage.", n:"le mot de question passe devant"},
         e:{w:['un délai'], say:"Ça prend combien de jours ? Je voudrais savoir combien de jours ça prend.", n:"la quantité se glisse comme le reste"},
       },
       note:"Répétez chaque paire deux fois : la première pour entendre la transformation, la seconde en ne disant que la version glissée."},

      {t:'ex', h:"À écouter et à répéter",
       p:"Six demandes glissées, prêtes à servir au comptoir.",
       rows:[
         ["Je voudrais savoir si mon absence est autorisée.","la plus utile du module"],
         ["Pourriez-vous me dire quand la réponse arrivera.","un point, pas un point d'interrogation"],
         ["Je ne sais pas ce qu'il faut mettre dans la case du motif.","ce que, sans est-ce que"],
         ["J'aimerais comprendre pourquoi ma demande a été refusée.","pourquoi se replace tel quel"],
         ["Dites-moi ce qui manque dans mon dossier, s'il vous plaît.","ce qui, parce que le mot fait l'action"],
         ["Je voudrais savoir combien de temps prend un transfert.","la question du délai, en fin de conversation"],
       ]},

      {t:'piege', h:"Trois pièges de l'interrogative indirecte",
       rows:[
         ["laisser le « est-ce que » au milieu","« Je voudrais savoir est-ce que je garde ma place. »",
          "C'est la faute la plus visible de ce défi. Le « est-ce que » et le « si » font le même travail : il ne peut pas y en avoir deux. Dès qu'une phrase commence par « je voudrais savoir », le « est-ce que » devient « si »."],
         ["garder l'inversion du sujet","« Pourriez-vous me dire quand dois-je remettre le papier. »",
          "L'inversion appartient à la question directe. Dans une phrase, le sujet revient devant son verbe : « quand je dois remettre le papier »."],
         ["mettre un point d'interrogation à la fin","« Je voudrais savoir si je garde ma place ? »",
          "La phrase n'est plus une question : c'est une déclaration qui en contient une. Elle finit par un point. L'exception : quand la phrase porteuse est elle-même une question — « Pourriez-vous me dire quand ça ouvre ? » —, le point d'interrogation appartient au « pourriez-vous »."],
       ]},

      {t:'check', h:"Est-ce que c'est clair maintenant ?",
       p:"Quatre questions rapides.",
       qs:[
         {q:"« Est-ce que » devient…", opts:["si","que"], ok:0,
          fb:"« si ». C'est la transformation la plus utile du défi."},
         {q:"« Quand dois-je partir ? » devient…", opts:["quand dois-je partir","quand je dois partir"], ok:1,
          fb:"« quand je dois partir » : l'inversion tombe, le mot de question reste."},
         {q:"« Je voudrais savoir si le local est libre » se termine par…", opts:["un point","un point d'interrogation"], ok:0,
          fb:"Un point. La phrase est une déclaration qui contient une question."},
         {q:"« Qu'est-ce qui manque ? » devient…", opts:["ce que manque","ce qui manque"], ok:1,
          fb:"« ce qui manque » : le mot fait l'action, donc « ce qui »."},
       ]},
    ]
  },

  // ════════════════════════════════════════════════════════════════════════
  t1fut: {
    eye:'Mini-leçon', tit:"Le futur simple, ou comment rassurer un bureau",
    blocs:[
      {t:'texte', h:"Annoncer une absence, c'est promettre un retour",
       p:"Quand vous dites à un centre que vous partez trois semaines, la première question qui se pose de l'autre côté du comptoir n'est pas « pourquoi ? » mais « et après ? ». Une absence prévue se termine par trois phrases au futur : je reviendrai le tant, je vous apporterai ceci, je m'inscrirai au rattrapage. C'est ce qui transforme une absence en un plan, et c'est ce qui fait garder votre place.",
       note:"Le futur simple est aussi le temps de la demande écrite. Une lettre au conditionnel du début à la fin donne l'impression que rien n'est décidé ; le futur, lui, engage."},

      {t:'ana', h:"Une seule série de terminaisons pour tous les verbes",
       p:"On les colle à l'infinitif, et elles ne changent jamais : -ai, -as, -a, -ons, -ez, -ont. Ce qui varie d'un verbe à l'autre, c'est seulement ce qui vient avant elles.",
       mots:[["Les verbes en -er et -ir","je remplirai · j'annoncerai · nous rattraperons"],["Les verbes en -re : le e tombe","je remettrai · j'écrirai · vous prendrez",true],["Le « r » qu'on entend toujours","c'est lui qui signale le futur à l'oreille"]],
       say:"Je reviendrai en classe le 30 mars.",
       note:"Le son du futur, c'est le « r » suivi d'un « é » fermé : reviendr-ai, apporter-ai. Quand vous ne l'entendez pas, ce n'est pas un futur."},

      {t:'ana', h:"Les six radicaux irréguliers dont vous aurez besoin",
       p:"Six verbes changent de forme avant les terminaisons. Ce sont exactement les six dont on se sert au comptoir : apprenez-les comme six mots, pas comme une règle.",
       mots:[["Les trois premiers","être → je serai · avoir → j'aurai · aller → j'irai"],["Les trois autres","faire → je ferai · venir → je viendrai · pouvoir → je pourrai",true],["Dans une phrase de comptoir","je serai absente · j'aurai le papier · je viendrai vous voir"]],
       say:"Je serai absente du 9 au 27 mars inclusivement.",
       note:"« Je serai » et « je saurai » se ressemblent et ne veulent pas dire la même chose. Au comptoir, c'est presque toujours « je serai » qu'il faut."},

      {t:'ana', h:"Futur simple ou futur proche ?",
       p:"Les deux existent et les deux sont corrects. Ce qui les sépare, c'est le registre : le futur proche appartient à la conversation, le futur simple à ce qui s'écrit et à ce qui s'annonce.",
       mots:[["Entre camarades","Je vais revenir lundi. · Je vais m'inscrire au rattrapage."],["Au comptoir et par écrit","Je reviendrai le 30 mars. · Je m'inscrirai au rattrapage dès mon retour.",true],["Ce qu'il ne faut pas mélanger","une même lettre ne passe pas de l'un à l'autre à chaque phrase"]],
       say:"Je vous apporterai la pièce justificative à mon retour.",
       note:"Dans une demande écrite, choisissez le futur simple et tenez-le du début à la fin. L'alternance entre les deux formes se remarque et donne un texte mal tenu."},

      {t:'labo', h:"La promesse, verbe par verbe",
       p:"Choisissez un verbe et écoutez la phrase de comptoir qu'il permet.",
       axes:[{id:'v', lbl:'Quel verbe ?', opts:[
         ['a','revenir'],
         ['b','être'],
         ['c','apporter'],
         ['d','faire'],
         ['e','pouvoir']]}],
       out:{
         a:{w:['une absence'], say:"Je reviendrai en classe le lundi 30 mars.", n:"venir → viendr- : radical irrégulier"},
         b:{w:['une absence'], say:"Je serai absente du 9 au 27 mars inclusivement.", n:"être → ser- : le plus fréquent des six"},
         c:{w:['une pièce justificative'], say:"Je vous apporterai la pièce justificative à mon retour.", n:"verbe régulier : l'infinitif entier reste"},
         d:{w:['un rattrapage'], say:"Je ferai le rattrapage du midi deux fois par semaine.", n:"faire → fer- : à ne pas confondre avec ferai de fermer"},
         e:{w:['une session'], say:"Je pourrai reprendre les évaluations à la fin de la session.", n:"pouvoir → pourr- : deux r, et ça s'entend"},
       },
       note:"Dites chaque phrase deux fois, la seconde en insistant sur le « r » qui précède la terminaison : c'est lui qui porte le futur."},

      {t:'ex', h:"À écouter et à répéter",
       p:"Six promesses qui font garder une place.",
       rows:[
         ["Je serai absente à partir du 9 mars.","être, le plus utile des six"],
         ["Je reviendrai en classe le lundi 30 mars.","venir, radical irrégulier"],
         ["Je vous apporterai la pièce justificative dès mon retour.","verbe régulier, infinitif entier"],
         ["Je m'inscrirai au rattrapage du midi.","verbe pronominal, même terminaison"],
         ["Vous recevrez ma demande écrite avant vendredi.","recevoir → recevr-"],
         ["Je pourrai reprendre les évaluations en avril.","pouvoir → pourr-, deux r"],
       ]},

      {t:'piege', h:"Trois pièges du futur",
       rows:[
         ["confondre « je voudrais » et « je voudrai »","« Je voudrai savoir si je garde ma place. »",
          "Le premier demande poliment, maintenant ; le second annonce ce que vous voudrez plus tard. Au comptoir, c'est toujours le premier — et il se dit avec un « è » ouvert."],
         ["oublier le « r » des verbes en -re","« je remettai » au lieu de « je remettrai »",
          "Les verbes en -re perdent leur « e » mais gardent leur « r » : remettre → je remettrai, écrire → j'écrirai, prendre → je prendrai. Sans le « r », il n'y a plus de futur du tout."],
         ["mélanger les deux futurs dans une même lettre","« Je vais revenir le 30 et je m'inscrirai au rattrapage. »",
          "Ce n'est pas une faute de grammaire, c'est une faute de tenue : le lecteur sent le changement de registre au milieu de la phrase. Choisissez le futur simple pour tout ce qui s'écrit."],
       ]},

      {t:'check', h:"Est-ce que c'est clair maintenant ?",
       p:"Quatre questions rapides.",
       qs:[
         {q:"Le futur de « venir » à la première personne est…", opts:["je venirai","je viendrai"], ok:1,
          fb:"« je viendrai » : venir prend le radical irrégulier viendr-."},
         {q:"Dans une demande écrite, on emploie plutôt…", opts:["le futur simple","le futur proche"], ok:0,
          fb:"Le futur simple, et on le tient du début à la fin."},
         {q:"« Je serai » vient du verbe…", opts:["savoir","être"], ok:1,
          fb:"« être ». « Je saurai » vient de savoir, et ce n'est pas ce qu'on dit au comptoir."},
         {q:"Le futur de « remettre » est…", opts:["je remettrai","je remettai"], ok:0,
          fb:"« je remettrai » : le « e » tombe, le « r » reste."},
       ]},
    ]
  },

  // ════════════════════════════════════════════════════════════════════════
  t1tri: {
    eye:'Mini-leçon', tit:"Reconnaître une question glissée en une seconde",
    blocs:[
      {t:'texte', h:"Trois signes, et c'est réglé",
       p:"Distinguer une question directe d'une question glissée n'est pas un exercice d'école : c'est ce qui vous permet de relire votre propre courriel avant de l'envoyer. Trois signes suffisent, et ils se voient tous les trois d'un coup d'œil : le point final, la place du sujet, et la présence ou l'absence de « est-ce que ».",
       note:"Cette leçon ne vous apprend rien de neuf sur la grammaire — elle vous donne un réflexe de relecture. Ce sont deux choses différentes, et la seconde est celle qui sert au quotidien."},

      {t:'ana', h:"Signe 1 : le point final",
       p:"Une question directe finit par un point d'interrogation. Une question glissée finit par un point — sauf si la phrase qui la porte est elle-même une question.",
       mots:[["Directe","Est-ce que le local est libre ?"],["Glissée","Je me demande si le local est libre.",true],["L'exception","Pourriez-vous me dire si le local est libre ?"]],
       say:"Je me demande si le local est libre.",
       note:"Dans l'exception, le point d'interrogation appartient au « pourriez-vous », pas à la question glissée. C'est la seule subtilité de ce signe."},

      {t:'ana', h:"Signe 2 : la place du sujet",
       p:"Dans une question directe soutenue, le sujet passe derrière le verbe. Cette inversion ne survit jamais au passage dans une phrase.",
       mots:[["Le sujet derrière : directe","Quand dois-je remettre le papier ? · Où se trouve le local ?"],["Le sujet devant : glissée","… quand je dois remettre le papier. · … où le local se trouve.",true],["Le repère visuel","un trait d'union entre le verbe et le pronom signale toujours une directe"]],
       say:"Pourriez-vous me dire quand je dois remettre le formulaire.",
       note:"Le trait d'union de « dois-je », « puis-je », « avez-vous » est le signe le plus rapide à repérer dans un texte que vous relisez."},

      {t:'ana', h:"Signe 3 : le « est-ce que »",
       p:"Il n'appartient qu'à la question directe. Rencontré au milieu d'une phrase, c'est toujours une erreur.",
       mots:[["Directe","Est-ce que ma demande est arrivée ?"],["Glissée","Je voudrais savoir si ma demande est arrivée.",true],["Jamais","Je voudrais savoir est-ce que ma demande est arrivée."]],
       say:"Je voudrais savoir si ma demande est arrivée.",
       note:"Un « est-ce que » précédé de « je voudrais savoir », « dites-moi » ou « j'aimerais comprendre » se remplace mécaniquement par « si »."},

      {t:'labo', h:"La même phrase, dans les deux formes",
       p:"Choisissez une phrase et écoutez la version directe, puis la version glissée.",
       axes:[{id:'f', lbl:'Quelle phrase ?', opts:[
         ['a','la place dans le groupe'],
         ['b','la date de remise'],
         ['c','le contenu du motif'],
         ['d','le lieu du rattrapage'],
         ['e','les quatre à la suite']]}],
       out:{
         a:{w:['une absence'], say:"Est-ce que je garde ma place ? Je voudrais savoir si je garde ma place.", n:"le est-ce que devient si"},
         b:{w:['une échéance'], say:"Quand dois-je remettre le formulaire ? Pourriez-vous me dire quand je dois le remettre.", n:"le trait d'union disparaît"},
         c:{w:['un motif'], say:"Qu'est-ce qu'il faut écrire ? Je ne sais pas ce qu'il faut écrire.", n:"qu'est-ce que devient ce que"},
         d:{w:['un rattrapage'], say:"Le rattrapage se donne où ? J'aimerais comprendre où se donne le rattrapage.", n:"le mot de question passe devant"},
         e:{w:['un formulaire','une échéance'], say:"Est-ce que le formulaire est prêt ? Je voudrais savoir si le formulaire est prêt. Quand est l'échéance ? Pourriez-vous me dire quand est l'échéance.", n:"deux paires à la suite, pour l'oreille"},
       },
       note:"Écoutez chaque paire en fermant les yeux : la version directe monte à la fin, la version glissée descend. C'est le quatrième signe, celui qu'on n'écrit pas."},

      {t:'ex', h:"À écouter et à répéter",
       p:"Six phrases : trois directes, trois glissées, en alternance.",
       rows:[
         ["Est-ce que mon absence est autorisée ?","directe : est-ce que, point d'interrogation"],
         ["Je voudrais savoir si mon absence est autorisée.","glissée : si, point final"],
         ["Quand dois-je apporter ma pièce justificative ?","directe : trait d'union, sujet derrière"],
         ["Dites-moi quand je dois apporter ma pièce justificative.","glissée : sujet devant"],
         ["Qu'est-ce qui manque dans mon dossier ?","directe : qu'est-ce qui"],
         ["J'aimerais comprendre ce qui manque dans mon dossier.","glissée : ce qui"],
       ]},

      {t:'piege', h:"Trois pièges de relecture",
       rows:[
         ["le point d'interrogation en trop","« Je voudrais savoir si vous avez reçu ma demande ? »",
          "La phrase commence par une déclaration : elle finit par un point. Ce point d'interrogation est la trace de la question directe qu'on avait d'abord en tête — et il se voit tout de suite dans un courriel."],
         ["l'inversion oubliée en chemin","« Dites-moi où se trouve-t-il. »",
          "Le « -t-il » n'a plus rien à faire là : le sujet est déjà devant. On écrit « Dites-moi où il se trouve. »"],
         ["croire qu'une glissée est plus polie en soi","« Je voudrais savoir si vous pourriez éventuellement peut-être… »",
          "La question glissée n'est pas une formule magique : empilée avec trois précautions, elle devient illisible. Une entrée, une question, et on s'arrête."],
       ]},

      {t:'check', h:"Est-ce que c'est clair maintenant ?",
       p:"Quatre questions rapides.",
       qs:[
         {q:"« Dites-moi ce qui manque. » est…", opts:["une question glissée","une question directe"], ok:0,
          fb:"Une question glissée : sujet devant, point final, pas de « est-ce que »."},
         {q:"Un trait d'union dans « dois-je » signale…", opts:["une directe","une glissée"], ok:0,
          fb:"Une question directe : c'est l'inversion du sujet."},
         {q:"« Pourriez-vous me dire si c'est ouvert ? » se termine par un point d'interrogation parce que…", opts:["la question glissée en demande un","la phrase porteuse est une question"], ok:1,
          fb:"C'est le « pourriez-vous » qui le demande, pas la question glissée."},
         {q:"Un « est-ce que » au milieu d'une phrase est…", opts:["toujours une erreur","parfois accepté"], ok:0,
          fb:"Toujours une erreur : il se remplace par « si »."},
       ]},
    ]
  },

  // ════════════════════════════════════════════════════════════════════════
  t2prep: {
    eye:'Mini-leçon', tit:"Les petits mots qui portent les dates",
    blocs:[
      {t:'texte', h:"Un avis officiel tient dans ses prépositions",
       p:"Retirez d'un avis les mots « à partir du », « jusqu'au », « d'ici le », « avant le », « dès » et « en cas de », et il ne reste plus qu'une liste de chiffres. Ce sont ces six mots-là qui disent lequel de ces chiffres commence quelque chose, lequel le termine, et lequel vous concerne personnellement. Les lire vite est la compétence la plus rentable de ce défi : elle vous fait gagner une semaine chaque fois.",
       note:"Le programme du niveau 5 accorde douze points de savoir aux prépositions et au groupe prépositionnel. Ce n'est pas un hasard : c'est là que se joue la compréhension d'un document officiel."},

      {t:'ana', h:"Le début et la fin : « à partir du » et « jusqu'au »",
       p:"Ils vont par paire. L'un ouvre la période, l'autre la ferme, et une période annoncée avec un seul des deux est une période sans fin.",
       mots:[["Le début","à partir du 9 mars · dès le 9 mars · du 9 mars"],["La fin","jusqu'au 27 mars · au 27 mars inclusivement",true],["La paire complète","du 9 mars au 27 mars inclusivement"]],
       say:"Je serai absente à partir du 9 mars, jusqu'au 27 inclusivement.",
       note:"« Inclusivement » n'est pas un mot d'ornement : sans lui, personne ne sait si le 27 est dedans ou dehors. Quand vous écrivez une date de fin, mettez-le."},

      {t:'ana', h:"L'échéance : « d'ici le » et « avant le »",
       p:"Ces deux-là ne parlent pas de votre situation : ils parlent de ce que vous devez faire, et de la limite après laquelle il sera trop tard.",
       mots:[["Vous avez jusqu'à cette date","d'ici le 6 mars · au plus tard le 6 mars"],["Strictement avant cette date","avant le 27 mars",true],["Ce qu'ils ont en commun","ils annoncent toujours une action de votre part, jamais du centre"]],
       say:"Le formulaire signé doit nous parvenir d'ici le 6 mars.",
       note:"Strictement, « avant le 27 » exclut le 27 et « d'ici le 27 » l'inclut. Beaucoup d'avis emploient les deux pour la même idée : en cas de doute, faites la chose deux jours plus tôt et la question ne se pose plus."},

      {t:'ana', h:"La condition : « dès » et « en cas de »",
       p:"Le premier dit « aussitôt que », le second dit « si cela arrive ». Ils ouvrent presque toujours le paragraphe qu'on saute — et c'est celui qui coûte le plus cher.",
       mots:[["Aussitôt que","dès votre retour · dès la réception de l'avis"],["Si cela arrive","en cas de prolongation · en cas d'absence non motivée",true],["Ce qui les suit","un nom, jamais un verbe conjugué : en cas de prolongation, pas en cas que vous prolongez"]],
       say:"En cas de prolongation, il faut appeler avant la fin de l'absence.",
       note:"« En cas de » est suivi d'un nom. Si vous n'avez qu'un verbe sous la main, écrivez plutôt « si » : « si vous devez rester plus longtemps »."},

      {t:'labo', h:"La même date, six sens différents",
       p:"Choisissez une préposition et écoutez la phrase d'avis qu'elle produit.",
       axes:[{id:'p', lbl:'Quelle préposition ?', opts:[
         ['a','à partir du'],
         ['b',"jusqu'au"],
         ['c',"d'ici le"],
         ['d','avant le'],
         ['e','en cas de']]}],
       out:{
         a:{w:['une absence'], say:"Votre absence est autorisée à partir du 9 mars.", n:"le 9 est le premier jour concerné"},
         b:{w:['une absence'], say:"Votre absence court jusqu'au 27 mars inclusivement.", n:"le 27 est dedans, grâce à inclusivement"},
         c:{w:['un formulaire','une échéance'], say:"Le formulaire signé doit nous parvenir d'ici le 6 mars.", n:"l'échéance : après, c'est trop tard"},
         d:{w:['un délai'], say:"Veuillez communiquer avec le secrétariat avant le 27 mars.", n:"strictement avant : le 27 n'est plus dedans"},
         e:{w:['une prolongation'], say:"En cas de prolongation, communiquez avec nous sans tarder.", n:"la condition, suivie d'un nom"},
       },
       note:"Écoutez les cinq à la suite en gardant la même date en tête : c'est le mot qui change, jamais le chiffre, et c'est le mot qui décide de ce que vous devez faire."},

      {t:'ex', h:"À écouter et à répéter",
       p:"Six phrases d'avis, telles qu'elles s'écrivent.",
       rows:[
         ["Votre absence est autorisée du 9 mars au 27 mars inclusivement.","la paire complète, en une phrase"],
         ["Le formulaire doit nous parvenir d'ici le 6 mars.","l'échéance"],
         ["Passé cette date, la demande n'est plus recevable.","la conséquence de l'échéance"],
         ["Dès votre retour, présentez-vous au secrétariat.","aussitôt que"],
         ["En cas de prolongation, communiquez avec nous avant le 27.","la condition, puis une seconde limite"],
         ["Le retour en classe est prévu pour le lundi 30 mars.","un rappel, et non une échéance"],
       ]},

      {t:'piege', h:"Trois pièges des dates dans un avis",
       rows:[
         ["prendre un rappel pour une échéance","croire que le 30 mars, date de retour, demande une action",
          "Une date de retour vous informe ; une échéance vous oblige. Cherchez le verbe : « le retour est prévu » n'exige rien de vous, « doit nous parvenir » exige tout."],
         ["lire « d'ici le 6 » comme « le 6 »","attendre le 6 pour porter le formulaire",
          "« D'ici le 6 » veut dire à n'importe quel moment jusqu'au 6, et le 6 est déjà tard : un formulaire remis le jour de l'échéance ne laisse aucune marge si une case manque."],
         ["oublier « inclusivement » quand on écrit","« Je serai absente jusqu'au 27 mars. »",
          "Le lecteur ne sait pas si vous rentrez le 27 ou le 28. Écrivez « jusqu'au 27 mars inclusivement » et donnez en plus la date de retour : « je reviendrai le 30 »."],
       ]},

      {t:'check', h:"Est-ce que c'est clair maintenant ?",
       p:"Quatre questions rapides.",
       qs:[
         {q:"« D'ici le 6 mars » veut dire…", opts:["le 6 mars au plus tard","le 6 mars exactement"], ok:0,
          fb:"Au plus tard le 6. Vous pouvez le faire avant, jamais après."},
         {q:"Le mot qui rend une date de fin sans ambiguïté est…", opts:["prévu","inclusivement"], ok:1,
          fb:"« inclusivement » : sans lui, on ne sait pas si le dernier jour est dedans."},
         {q:"« En cas de » est suivi…", opts:["d'un nom","d'un verbe conjugué"], ok:0,
          fb:"D'un nom : en cas de prolongation, en cas d'absence."},
         {q:"Dans un avis, l'échéance est celle qui…", opts:["vous informe","vous oblige à agir"], ok:1,
          fb:"Celle qui vous oblige. Les autres dates ne sont que des rappels."},
       ]},
    ]
  },

  // ════════════════════════════════════════════════════════════════════════
  t2rep: {
    eye:'Mini-leçon', tit:"À quoi renvoie « celui-ci » ?",
    blocs:[
      {t:'texte', h:"Un document officiel ne répète jamais un mot",
       p:"Un avis parle d'un formulaire, d'une demande, d'un avis et d'un local en quatre paragraphes. S'il répétait chaque fois le mot, il ferait trois pages et personne ne le lirait. Il reprend donc : « ce document », « cette demande », « celui-ci », « le », « y ». Lire un document officiel, c'est en grande partie savoir à quoi chaque reprise renvoie — et écrire proprement, c'est reprendre à son tour sans laisser le lecteur deviner.",
       note:"Le programme du niveau 5 consacre six points de savoir à la reprise de l'information. C'est un des rares endroits où lire et écrire demandent exactement la même compétence, dans les deux sens."},

      {t:'ana', h:"« ce » + un nom plus général : la reprise la plus sûre",
       p:"On reprend le mot par un mot qui le contient : formulaire → document, demande → dossier, absence → situation. Impossible de se tromper de renvoi, et c'est la reprise à employer quand c'est vous qui écrivez.",
       mots:[["Sur un papier","le formulaire → ce document · l'avis → ce document"],["Sur une démarche","ma demande de transfert → cette demande · mon absence → cette situation",true],["Sur un moment","le 6 mars → cette date · la session d'hiver → cette période"]],
       say:"Remplissez le formulaire : ce document doit nous parvenir avant le 6 mars.",
       note:"Le mot repris doit être plus général, jamais plus précis. « Le formulaire → cette feuille » fonctionne mal : on ne sait plus si c'est la même feuille ou une autre."},

      {t:'ana', h:"« celui-ci » et sa famille : le nom le plus proche",
       p:"Celui-ci, celle-ci, ceux-ci, celles-ci renvoient au dernier nom du bon genre et du bon nombre. Quand vous lisez, remontez d'un mot à la fois jusqu'au premier nom qui s'accorde.",
       mots:[["Masculin singulier","le retour → celui-ci · le formulaire → celui-ci"],["Féminin singulier","la demande → celle-ci · l'échéance → celle-ci",true],["Au pluriel","les documents → ceux-ci · les dates → celles-ci"]],
       say:"Le retour est prévu le 30 mars : celui-ci n'est pas une échéance.",
       note:"« Celui-là » existe aussi, et il désigne le plus éloigné quand deux noms sont en concurrence : « le formulaire et l'avis : celui-ci se signe, celui-là se remplit »."},

      {t:'ana', h:"« le », « la », « les » et « y » : les petits mots",
       p:"Ce sont les reprises les plus courtes, et donc les plus faciles à mal lire. « Le » remplace un nom déjà déterminé ; « y » remplace un lieu ou un nom introduit par « à ».",
       mots:[["Un objet déjà nommé","Signez l'avis et rapportez-le au secrétariat."],["Un lieu","Passez au secrétariat : j'y serai jusqu'à seize heures.",true],["Une chose introduite par « à »","Je pense à ma demande. → J'y pense."]],
       say:"Signez cet avis et rapportez-le au secrétariat.",
       note:"« Rapportez-le » avec un trait d'union à l'impératif, « je le rapporte » sans trait d'union au présent. C'est la seule difficulté d'écriture de ces petits mots."},

      {t:'labo', h:"Quelle reprise, pour quel mot ?",
       p:"Choisissez une reprise et écoutez la phrase où elle travaille.",
       axes:[{id:'r', lbl:'Quelle reprise ?', opts:[
         ['a','ce document'],
         ['b','celui-ci'],
         ['c','celle-ci'],
         ['d','le'],
         ['e','y']]}],
       out:{
         a:{w:['un formulaire'], say:"Remplissez le formulaire : ce document doit nous parvenir avant le 6 mars.", n:"un mot plus général, jamais ambigu"},
         b:{w:['une échéance'], say:"Le retour est prévu le 30 mars : celui-ci n'est pas une échéance.", n:"le dernier nom masculin singulier"},
         c:{w:['une prolongation'], say:"J'ai envoyé ma demande de prolongation : celle-ci a été reçue le 4 avril.", n:"le dernier nom féminin singulier"},
         d:{w:['un avis'], say:"Signez cet avis et rapportez-le au secrétariat.", n:"le pronom le plus court, et le plus discret"},
         e:{w:['le secrétariat'], say:"Passez au secrétariat : j'y serai jusqu'à seize heures.", n:"un lieu, remplacé par une seule lettre"},
       },
       note:"Après chaque phrase, redites-la en remettant le mot entier à la place de la reprise. Si elle veut encore dire la même chose, vous avez compris le renvoi."},

      {t:'ex', h:"À écouter et à répéter",
       p:"Six phrases prises dans l'avis du module.",
       rows:[
         ["Veuillez signer cet avis et le rapporter au secrétariat.","le = l'avis"],
         ["Le formulaire est en ligne : ce document se remplit à l'écran.","ce document = le formulaire"],
         ["Votre demande a été reçue : celle-ci sera traitée en dix jours.","celle-ci = la demande"],
         ["Le rattrapage a lieu au local 118 : j'y serai le mardi midi.","y = au local 118"],
         ["Deux dates figurent ici : celle-ci est une échéance, celle-là un rappel.","deux reprises en concurrence"],
         ["J'ai gardé une copie de ce document, comme vous me l'aviez dit.","le = de garder une copie"],
       ]},

      {t:'piege', h:"Trois pièges de la reprise",
       rows:[
         ["employer « celui-ci » loin de son nom","trois phrases plus bas, alors que quatre noms ont passé",
          "« Celui-ci » désigne le nom masculin singulier le plus proche. Au-delà d'une phrase, le lecteur remonte et se trompe. Écrivez alors « ce document », « cette demande » : le renvoi redevient certain."],
         ["reprendre par un mot plus précis","« le document → ce formulaire »",
          "La reprise doit aller du précis vers le général, jamais l'inverse. En remontant vers le précis, vous ajoutez une information que le lecteur n'a pas — et il croit qu'il s'agit d'un autre papier."],
         ["oublier l'accord de la reprise","« ma demande … celui-ci a été reçu »",
          "Demande est féminin : c'est « celle-ci a été reçue ». L'accord de la reprise est le premier signe qu'on relit pour vérifier à quoi elle renvoie — s'il est faux, le renvoi l'est presque toujours aussi."],
       ]},

      {t:'check', h:"Est-ce que c'est clair maintenant ?",
       p:"Quatre questions rapides.",
       qs:[
         {q:"« Celui-ci » renvoie…", opts:["au nom masculin le plus proche","au sujet de la phrase"], ok:0,
          fb:"Au nom masculin singulier le plus proche, en remontant."},
         {q:"Quand vous écrivez, la reprise la plus sûre est…", opts:["« ce » + un nom général","« celui-ci »"], ok:0,
          fb:"« ce document », « cette demande » : le renvoi ne peut pas être mal lu."},
         {q:"Dans « j'y serai avant midi », « y » remplace…", opts:["un lieu","une personne"], ok:0,
          fb:"Un lieu, ou un nom introduit par « à »."},
         {q:"Une reprise doit aller…", opts:["du général vers le précis","du précis vers le général"], ok:1,
          fb:"Du précis vers le général : formulaire → document, jamais l'inverse."},
       ]},
    ]
  },

  // ════════════════════════════════════════════════════════════════════════
  t3sub: {
    eye:'Mini-leçon', tit:"Le subjonctif des démarches",
    blocs:[
      {t:'texte', h:"Trois entrées, et tout le module y passe",
       p:"Le subjonctif fait peur parce qu'on l'apprend comme une liste de cas. Dans une démarche administrative, il n'en sert que trois : « il faut que » pour dire l'obligation, « pour que » pour dire le but, « bien que » pour reconnaître ce qui va contre. Trois entrées, cinq verbes irréguliers, et vous écrivez une demande complète sans jamais buter dessus.",
       note:"« Il faut que je travaille » n'est pas la même phrase que « je dois travailler ». La première dit que la nécessité vient d'ailleurs — du loyer, de l'employeur, de la vie. C'est ce qui permet d'expliquer sans se plaindre."},

      {t:'ana', h:"Comment le former : une seule opération",
       p:"On prend le radical du « ils » au présent et on colle -e, -es, -e, -ions, -iez, -ent. Neuf verbes sur dix y passent sans histoire.",
       mots:[["Les verbes en -er","ils travaillent → que je travaille · ils demandent → que je demande"],["Les verbes en -ir et -re","ils finissent → que je finisse · ils écrivent → que j'écrive",true],["Ce qui ne change pas","le « que » est toujours devant : que je, que tu, qu'il"]],
       say:"Il faut que je travaille le matin pour payer mon loyer.",
       note:"Pour beaucoup de verbes en -er, le subjonctif ressemble au présent : « que je travaille » et « je travaille » s'écrivent pareil. Ce n'est pas une difficulté, c'est une chance."},

      {t:'ana', h:"Les cinq irréguliers à savoir par cœur",
       p:"Cinq verbes changent de forme, et ce sont exactement ceux dont une demande a besoin. Apprenez-les comme cinq mots.",
       mots:[["Les trois d'abord","être → que je sois · avoir → que j'aie · aller → que j'aille"],["Les deux autres","faire → que je fasse · pouvoir → que je puisse",true],["Dans une demande","il faut que je sois là · pour que je puisse suivre le cours"]],
       say:"Il faut que vous soyez au secrétariat avant seize heures.",
       note:"« Que j'aille » (aller) et « que j'aie » (avoir) se ressemblent à l'écrit et se distinguent à l'oreille. Le premier a un son de « y » au milieu, le second n'en a pas."},

      {t:'ana', h:"« pour que » ou « pour » ? La question des deux sujets",
       p:"C'est la seule vraie décision à prendre. Deux personnes différentes de chaque côté : « pour que » et le subjonctif. La même personne des deux côtés : « pour » et l'infinitif.",
       mots:[["Deux sujets : pour que + subjonctif","Pour que le transfert se fasse, il me faut une demande écrite."],["Un seul sujet : pour + infinitif","Je vous écris pour demander un changement de groupe.",true],["Le test","dites la phrase à voix haute : si c'est vous des deux côtés, pas de « que »"]],
       say:"Pour que le transfert se fasse, il me faut une demande écrite.",
       note:"La même règle vaut pour « avant que » et « avant de », « afin que » et « afin de ». Une fois la question des deux sujets comprise, elle sert partout."},

      {t:'labo', h:"La même demande, avec chaque entrée",
       p:"Choisissez une entrée et écoutez la phrase de demande qu'elle produit.",
       axes:[{id:'e', lbl:'Quelle entrée ?', opts:[
         ['a','il faut que'],
         ['b','pour que'],
         ['c','bien que'],
         ['d','pour + infinitif'],
         ['e','les quatre à la suite']]}],
       out:{
         a:{w:['un transfert'], say:"Il faut que je travaille le matin, donc il faut que je change de groupe.", n:"l'obligation qui vient d'ailleurs"},
         b:{w:['un formulaire'], say:"Pour que le transfert se fasse, il faut que je remplisse le formulaire.", n:"le but, avec deux sujets différents"},
         c:{w:['un délai'], say:"Bien que le délai soit court, je vais remplir la demande ce soir.", n:"la concession : ce qui va contre, reconnu"},
         d:{w:['une conseillère'], say:"Je vous écris pour demander un rendez-vous avec la conseillère.", n:"un seul sujet : pour + infinitif"},
         e:{w:['un transfert','un délai'], say:"Il faut que je travaille. Pour que le transfert se fasse, il me faut une demande écrite. Bien que le délai soit court, je l'écrirai ce soir.", n:"les trois entrées dans une seule demande"},
       },
       note:"La cinquième sortie est une demande complète en trois phrases. Apprenez-la telle quelle : elle sert de patron pour la production écrite."},

      {t:'ex', h:"À écouter et à répéter",
       p:"Six phrases de demande, toutes au subjonctif.",
       rows:[
         ["Il faut que je travaille le matin pour payer mon loyer.","l'obligation qui vient d'ailleurs"],
         ["Pour que le transfert se fasse, il me faut une demande écrite.","deux sujets, donc « pour que »"],
         ["Il faut que vous soyez au secrétariat avant seize heures.","être, le plus fréquent des cinq"],
         ["Bien que le délai soit court, je remplirai le formulaire ce soir.","la concession"],
         ["Il faut que j'aille chercher mon attestation avant vendredi.","aller, le plus irrégulier"],
         ["Pour que je puisse suivre le cours du soir, il faut changer mon groupe.","pouvoir, avec deux sujets"],
       ]},

      {t:'piege', h:"Trois pièges du subjonctif",
       rows:[
         ["mettre un infinitif après « il faut que »","« Il faut que travailler le matin. »",
          "« Il faut » tout seul se suit d'un infinitif : « il faut travailler ». Dès qu'un « que » apparaît, il faut un sujet et un verbe conjugué : « il faut que je travaille »."],
         ["employer « pour que » avec un seul sujet","« Je vous écris pour que je demande un transfert. »",
          "Les deux côtés sont « je » : on écrit « pour demander un transfert ». Le « pour que » ne sert que lorsque la seconde partie a un autre sujet que la première."],
         ["confondre « que j'aie » et « que j'aille »","« Il faut que j'aie chercher mon attestation. »",
          "« Que j'aie » vient d'avoir, « que j'aille » vient d'aller. Ici, on va chercher quelque chose : c'est « que j'aille ». À l'oreille, le second a un son de « y » que le premier n'a pas."],
       ]},

      {t:'check', h:"Est-ce que c'est clair maintenant ?",
       p:"Quatre questions rapides.",
       qs:[
         {q:"Après « il faut que », le verbe est…", opts:["à l'infinitif","au subjonctif"], ok:1,
          fb:"Au subjonctif. C'est « il faut » sans « que » qui se suit d'un infinitif."},
         {q:"« Je vous écris ___ demander un transfert. »", opts:["pour","pour que"], ok:0,
          fb:"« pour » : le sujet est le même des deux côtés."},
         {q:"Le subjonctif de « pouvoir » à la première personne est…", opts:["que je puisse","que je peux"], ok:0,
          fb:"« que je puisse » : l'un des cinq irréguliers du module."},
         {q:"« Il faut que je travaille » plutôt que « je dois travailler » sert à…", opts:["expliquer sans se plaindre","paraître plus poli"], ok:0,
          fb:"À montrer que la nécessité vient d'ailleurs, pas d'un caprice."},
       ]},
    ]
  },

  // ════════════════════════════════════════════════════════════════════════
  t3emph: {
    eye:'Mini-leçon', tit:"Mettre un mot devant tous les autres",
    blocs:[
      {t:'texte', h:"La même information, mais à la bonne place",
       p:"« L'horaire me bloque » est une phrase exacte, plate, et oubliée aussitôt dite. « Ce qui me bloque, c'est l'horaire » dit rigoureusement la même chose — mais l'horaire est maintenant au bout de la phrase, à l'endroit où l'oreille s'arrête et où la mémoire retient. C'est ce que la grammaire appelle une phrase emphatique, et le programme du niveau 5 lui accorde quatre points de savoir.",
       note:"Dans une demande, cette tournure fait une chose que rien d'autre ne fait aussi bien : elle sépare le problème du reste. « Ce qui me bloque, c'est l'horaire, pas le cours » évite à la personne en face de chercher ce qui ne va pas dans son enseignement."},

      {t:'ana', h:"« Ce qui … c'est » quand le mot fait l'action",
       p:"Dans la phrase plate, si le mot mis en avant était le sujet, la reprise se fait par « ce qui ».",
       mots:[["Phrase plate","L'horaire me bloque. · Une attestation me manque."],["Phrase emphatique","Ce qui me bloque, c'est l'horaire. · Ce qui me manque, c'est une attestation.",true],["Le test","le mot faisait-il l'action ? alors « ce qui »"]],
       say:"Ce qui me bloque, c'est l'horaire du matin, pas le cours.",
       note:"La virgule avant « c'est » n'est pas facultative : elle marque la pause qu'on fait en parlant, et sans elle la phrase se lit d'un trait, ce qui annule tout l'effet."},

      {t:'ana', h:"« Ce que … c'est » quand le mot subit l'action",
       p:"Si le mot mis en avant était complément — je demande quelque chose, je ne comprends pas quelque chose —, la reprise se fait par « ce que ».",
       mots:[["Phrase plate","Je demande un transfert. · Je ne comprends pas la date."],["Phrase emphatique","Ce que je demande, c'est un transfert. · Ce que je ne comprends pas, c'est la date.",true],["Devant une voyelle","ce qu'il me faut · ce qu'on me demande"]],
       say:"Ce que je demande, c'est un transfert au groupe du soir.",
       note:"« Ce que » s'élide devant une voyelle : « ce qu'il me faut ». « Ce qui », lui, ne s'élide jamais — c'est un moyen rapide de vérifier lequel des deux on a écrit."},

      {t:'ana', h:"« c'est que » quand la suite est une phrase entière",
       p:"Dès qu'un verbe conjugué suit, il faut ajouter « que ». Sans lui, la phrase s'arrête au milieu.",
       mots:[["Un nom suit : c'est","Ce qui me bloque, c'est l'horaire."],["Une phrase suit : c'est que","Ce qui me bloque, c'est que le cours finit à midi et demi.",true],["Le repère","cherchez un verbe conjugué après « c'est » : s'il y en a un, il faut « que »"]],
       say:"Ce qui me dérange, c'est que le cours finit à midi et demi.",
       note:"C'est la faute la plus fréquente de ce défi, et elle s'entend : « ce qui me bloque, c'est le cours finit à midi » laisse la personne en face attendre la fin de la phrase."},

      {t:'labo', h:"La phrase plate, puis la phrase emphatique",
       p:"Choisissez une idée et écoutez-la dite des deux façons.",
       axes:[{id:'i', lbl:'Quelle idée ?', opts:[
         ['a',"l'horaire"],
         ['b','le transfert'],
         ['c',"l'attestation"],
         ['d','la date en gras'],
         ['e','les quatre à la suite']]}],
       out:{
         a:{w:['une session'], say:"L'horaire me bloque. Ce qui me bloque, c'est l'horaire du matin.", n:"sujet, donc ce qui"},
         b:{w:['un transfert'], say:"Je demande un transfert. Ce que je demande, c'est un transfert au groupe du soir.", n:"complément, donc ce que"},
         c:{w:['une attestation'], say:"Une attestation me manque. Ce qui me manque, c'est une attestation pour mon employeur.", n:"sujet, donc ce qui"},
         d:{w:['une échéance'], say:"Je ne comprends pas la date en gras. Ce que je ne comprends pas, c'est la date en gras.", n:"complément, donc ce que"},
         e:{w:['un transfert','une attestation'], say:"Ce qui me bloque, c'est l'horaire. Ce que je demande, c'est un transfert. Ce qui me manque, c'est une attestation.", n:"trois emphases à la suite — à ne jamais faire dans une vraie lettre"},
       },
       note:"La cinquième sortie montre exactement ce qu'il ne faut pas faire : trois emphases de suite et plus rien n'est mis en avant. Une par demande, au début."},

      {t:'ex', h:"À écouter et à répéter",
       p:"Six phrases emphatiques, telles qu'on les dit dans un bureau.",
       rows:[
         ["Ce qui me bloque, c'est l'horaire, pas le cours.","la phrase qui ouvre la demande"],
         ["Ce que je demande, c'est un transfert au groupe du soir.","complément mis en avant"],
         ["Ce qui me manque, c'est une attestation pour mon employeur.","sujet mis en avant"],
         ["Ce que je ne comprends pas, c'est la date écrite en gras.","une question posée sans point d'interrogation"],
         ["Ce qui me dérange, c'est que le cours finit à midi et demi.","une phrase suit, donc « c'est que »"],
         ["Ce qui compte pour moi, c'est de finir le cours cette année.","un infinitif suit : « c'est de »"],
       ]},

      {t:'piege', h:"Trois pièges de la phrase emphatique",
       rows:[
         ["oublier le « que » devant une phrase","« Ce qui me dérange, c'est le cours finit à midi. »",
          "Un verbe conjugué suit : il faut « c'est que le cours finit à midi ». Sans ce mot, la phrase reste ouverte et l'auditeur attend la suite."],
         ["confondre « ce qui » et « ce que »","« Ce que me bloque, c'est l'horaire. »",
          "Dans la phrase plate, l'horaire faisait l'action : il bloque. C'est donc « ce qui ». Le test tient en une seconde et il ne rate jamais."],
         ["en mettre trois de suite","une lettre entière écrite en phrases emphatiques",
          "Cette tournure éclaire ce qui compte. Trois de suite, et plus rien n'est éclairé : le lecteur ne sait plus quel est le vrai problème. Une seule, au début, puis des phrases ordinaires."],
       ]},

      {t:'check', h:"Est-ce que c'est clair maintenant ?",
       p:"Quatre questions rapides.",
       qs:[
         {q:"« ___ je demande, c'est un transfert. »", opts:["Ce que","Ce qui"], ok:0,
          fb:"« Ce que » : le transfert subit l'action, il est complément."},
         {q:"« Ce qui me dérange, c'est ___ le cours finit tôt. »", opts:["que","–"], ok:0,
          fb:"« que » : une phrase entière suit, avec un verbe conjugué."},
         {q:"« Ce qui » peut-il s'élider en « ce qu' » ?", opts:["oui","non"], ok:1,
          fb:"Non, jamais. Seul « ce que » s'élide — c'est un bon moyen de vérification."},
         {q:"Dans une demande écrite, on emploie cette tournure…", opts:["une fois, au début","à chaque paragraphe"], ok:0,
          fb:"Une fois, au début. Répétée, elle n'éclaire plus rien."},
       ]},
    ]
  },

  // ════════════════════════════════════════════════════════════════════════
  t3con: {
    eye:'Mini-leçon', tit:"Les six connecteurs d'une demande",
    blocs:[
      {t:'texte', h:"Une demande, c'est une suite de raisons",
       p:"Ce qui sépare une demande d'une plainte, ce n'est pas la politesse : c'est l'enchaînement. Une plainte énumère des choses désagréables. Une demande pose une situation, en tire une conséquence, et propose une solution dont elle accepte le prix. Six mots suffisent à tenir cet enchaînement, et ils se répartissent en trois paires : la cause, la conséquence, et l'objection.",
       note:"Le programme du niveau 5 parle de connecteurs et de relations logiques. Ce sont eux — et c'est la différence entre un discours organisé et une suite de phrases justes."},

      {t:'ana', h:"La cause : « parce que », « comme », « puisque »",
       p:"Les trois disent pourquoi, mais ils ne se placent pas au même endroit et ne supposent pas la même chose de la part du lecteur.",
       mots:[["Après, le plus courant","Je demande un transfert parce que je travaille le matin."],["Avant, le plus élégant à l'écrit","Comme je travaille le matin, je ne peux plus suivre le cours de jour.",true],["Quand l'autre sait déjà","Puisque mon absence était motivée, ma place a été conservée."]],
       say:"Comme je travaille le matin, je ne peux plus suivre le cours de jour.",
       note:"« Comme » ne s'emploie qu'en tête de phrase — c'est ce qui le distingue de « parce que », qui ne s'emploie jamais en tête. « Puisque » suppose que la raison est connue : employé pour une raison nouvelle, il sonne comme un reproche."},

      {t:'ana', h:"La conséquence : « donc » et « c'est pourquoi »",
       p:"Ils annoncent ce qui découle de ce qui vient d'être dit. Le second est plus soutenu et convient mieux à une lettre.",
       mots:[["À l'oral et dans une note","Je travaille le matin, donc je ne peux plus venir le jour."],["Dans une demande écrite","Mon horaire a changé ; c'est pourquoi je vous demande un transfert.",true],["Ce qu'ils ont en commun","ils viennent toujours après la cause, jamais avant"]],
       say:"Mon horaire a changé, c'est pourquoi je vous demande un transfert.",
       note:"Une demande bien tenue place « c'est pourquoi » à un seul endroit : juste avant la phrase où l'on demande. C'est le pivot de la lettre."},

      {t:'ana', h:"L'objection : « par contre » et « bien que »",
       p:"Ils annoncent ce qui va dans l'autre sens. Dans une demande, ce sont eux qui montrent que vous avez pesé ce que vous demandez.",
       mots:[["Après une phrase complète","Le soir, c'est quatre soirs par semaine. Par contre, ça se place avec mon horaire."],["Devant une subordonnée, avec le subjonctif","Bien que le délai soit court, je remplirai le formulaire ce soir.",true],["Ce qu'ils évitent","de faire croire qu'on n'a pas vu la difficulté"]],
       say:"Bien que le délai soit court, je remplirai le formulaire ce soir.",
       note:"Une demande qui ne reconnaît aucune difficulté paraît naïve, et une demande qui n'en reconnaît que des difficultés paraît découragée. Une objection, une seule, et reconnue : c'est le bon dosage."},

      {t:'labo', h:"Le même contenu, connecteur par connecteur",
       p:"Choisissez un connecteur et écoutez la phrase de demande qu'il produit.",
       axes:[{id:'c', lbl:'Quel connecteur ?', opts:[
         ['a','parce que'],
         ['b','comme'],
         ['c','donc'],
         ['d',"c'est pourquoi"],
         ['e','par contre']]}],
       out:{
         a:{w:['un transfert'], say:"Je demande un transfert parce que je travaille le matin.", n:"la cause, après"},
         b:{w:['une session'], say:"Comme mon horaire a changé, je ne peux plus suivre le cours de jour.", n:"la cause, en tête de phrase"},
         c:{w:['un local'], say:"Je finis à trois heures, donc je peux être au local à six heures.", n:"la conséquence, à l'oral"},
         d:{w:['un transfert'], say:"Mon horaire a changé ; c'est pourquoi je vous demande un transfert.", n:"la conséquence, à l'écrit"},
         e:{w:['un délai'], say:"Le délai est de dix jours. Par contre, je peux commencer avant la réponse.", n:"l'objection, reconnue et dépassée"},
       },
       note:"Écoutez les cinq à la suite : c'est la charpente d'une demande complète, dans l'ordre où elle s'écrit."},

      {t:'ex', h:"À écouter et à répéter",
       p:"Six phrases, dans l'ordre d'une vraie demande.",
       rows:[
         ["Comme j'ai commencé un emploi, mon horaire a changé.","la cause, en tête"],
         ["Le cours de jour finit à midi et demi, donc je dois partir avant la fin.","la conséquence"],
         ["C'est pourquoi je vous demande un transfert au groupe du soir.","le pivot de la demande"],
         ["Bien que le groupe du soir demande quatre soirs, cela me convient.","l'objection, reconnue"],
         ["Par contre, je ne pourrai pas commencer avant le 20 avril.","la nuance, honnête"],
         ["Puisque ma demande est déjà au dossier, je n'ajoute rien d'autre.","la raison que l'autre connaît"],
       ]},

      {t:'piege', h:"Trois pièges des connecteurs",
       rows:[
         ["commencer une lettre par « parce que »","« Parce que je travaille le matin, je vous écris. »",
          "« Parce que » répond à une question qui n'a pas encore été posée. En tête de phrase, c'est « comme » qu'on emploie : « Comme je travaille le matin… »."],
         ["employer « puisque » pour une raison nouvelle","« Puisque j'ai trouvé un emploi, je veux changer de groupe. »",
          "« Puisque » suppose que le lecteur connaît déjà la raison. S'il l'apprend en vous lisant, la tournure sonne comme un reproche. Employez « comme » ou « parce que »."],
         ["accumuler les causes","trois « parce que » dans le même paragraphe",
          "Une raison suffit, et c'est la plus forte qu'il faut garder. Trois raisons empilées donnent l'impression qu'aucune ne tient toute seule — c'est l'effet exactement contraire à celui qu'on cherche."],
       ]},

      {t:'check', h:"Est-ce que c'est clair maintenant ?",
       p:"Quatre questions rapides.",
       qs:[
         {q:"En tête de phrase, on emploie…", opts:["comme","parce que"], ok:0,
          fb:"« comme ». « Parce que » ne s'emploie jamais en tête de phrase."},
         {q:"« C'est pourquoi » annonce…", opts:["une cause","une conséquence"], ok:1,
          fb:"Une conséquence, et c'est le pivot d'une demande écrite."},
         {q:"Après « bien que », le verbe est…", opts:["au subjonctif","à l'indicatif"], ok:0,
          fb:"Au subjonctif : « bien que le délai soit court »."},
         {q:"Dans une demande, il vaut mieux donner…", opts:["une raison forte","trois raisons"], ok:0,
          fb:"Une seule, la plus forte. Trois raisons empilées s'affaiblissent l'une l'autre."},
       ]},
    ]
  },

};
