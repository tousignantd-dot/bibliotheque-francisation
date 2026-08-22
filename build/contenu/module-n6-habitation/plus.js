const PLUS = {

  prGraphie: {
    eye:'Mini-leçon', tit:"Le chantier parle grec, anglais et allemand",
    blocs:[
      {t:'texte', h:"Pourquoi trois groupes de lettres se lisent de travers",
       p:"Le vocabulaire technique du bâtiment n'est pas né en français. Il est venu du grec par la science, de l'anglais par les matériaux, de l'allemand par la géologie. Chaque langue a laissé son orthographe et le français a gardé, à peu près, sa prononciation d'origine. D'où trois groupes de lettres qui ne se lisent pas comme on les écrit — et qui reviennent tous les trois dans une conversation de chantier.",
       note:"Ce sont exactement les quatre points que le programme du niveau 6 inscrit à la graphie-phonie : le k écrit ch, le s écrit x, le son de « chat » écrit sh ou sch."},

      {t:'ana', h:"Le grec — ch qui se dit k",
       p:"Les mots savants passés par le grec gardent leur k, même écrit ch. Ce sont les mots des plans, des mesures et des produits.",
       mots:[['On écrit','un ar{ch}itecte · la te{ch}nique · le {ch}lore · une or{ch}idée'],
             ['On entend','[k], comme dans « kilo »', true],
             ['Le repère','un mot qui sent l\'école ou le laboratoire, souvent avec un « y » ou un « ph » pas loin']],
       say:"un architecte, la technique, le chlore, une orchidée",
       note:"Le reste des mots en ch garde le son normal : chantier, chauffage, planche, marchandise. Le k est l'exception, et elle se compte sur les doigts."},

      {t:'ana', h:"Les nombres — x qui se dit s",
       p:"Trois nombres très courants et un nom de ville. Rien d'autre, ou presque, mais on les dit vingt fois par jour sur un chantier.",
       mots:[['On écrit','di{x} · si{x} · soi{x}ante · Bru{x}elles'],
             ['On entend','[s], comme dans « sac »', true],
             ['Ce qui change tout','ce qui vient juste après le nombre']],
       say:"dix, six, soixante, Bruxelles",
       note:"« Six semaines » se dit « si semaines ». « Six heures » se dit « siz heures ». « Il y en a six » se dit « sisse ». Trois formes, un seul mot écrit."},

      {t:'ana', h:"L'anglais et l'allemand — sh et sch qui se disent comme dans « chat »",
       p:"Des mots empruntés tels quels, et gardés tels quels. Le français leur a seulement mis sa bouche.",
       mots:[['On écrit','un {sch}éma · le {sch}iste · le {sh}ampoing · un {sh}ort'],
             ['On entend','le son de « chat »', true],
             ['Le repère','un mot court, venu d\'ailleurs, souvent technique ou vestimentaire']],
       say:"un schéma, le schiste, le shampoing, un short",
       note:"« Un schéma » revient sans arrêt dans un rapport : c'est le dessin qui accompagne une explication. Le lire « skéma » ferait chercher longtemps dans un dictionnaire."},

      {t:'labo', h:"Écoutez, puis répétez",
       p:"Choisissez la famille, puis l'exemple.",
       axes:[
         {id:'f', lbl:'Quelle famille ?', opts:[['g','le grec : ch qui dit K'],['n','les nombres : x qui dit S'],['e','l\'emprunt : sh, sch qui disent CH']]},
         {id:'r', lbl:'Quel exemple ?', opts:[['1','le premier'],['2','le second']]}],
       out:{
         g1:{w:["un architecte"], say:"un architecte", n:'« ar-ki-tecte » : le ch se ramasse en un k sec'},
         g2:{w:["la technique"], say:"la technique", n:'« tec-nique » — jamais le ch de « chantier »'},
         n1:{w:["six"], say:"six", n:'isolé, le x s\'entend clairement : « sisse »'},
         n2:{w:["soixante"], say:"soixante", n:'« soi-sante », deux syllabes, aucun k'},
         e1:{w:["un schéma"], say:"un schéma", n:'trois lettres, un seul son : « ché-ma »'},
         e2:{w:["le schiste"], say:"le schiste", n:'« chiste » — une pierre qui se fend en feuillets'},
       },
       note:"Deux écoutes avant d'ouvrir la bouche. Ce qui se travaille ici est l'oreille ; la bouche suit toute seule."},

      {t:'ex', h:"Les mots du module, colonne de gauche et colonne de droite",
       p:"À gauche l'orthographe, à droite ce qu'on entend.",
       rows:[
         ["un architecte","« ar-ki-tecte » — le ch fait k"],
         ["la technique","« tec-nique » — le ch fait k"],
         ["le chlore","« clore » — le ch fait k"],
         ["une orchidée","« or-ki-dée » — le ch fait k"],
         ["six semaines","« si semaines » — le x tombe devant une consonne"],
         ["six heures","« siz heures » — le x se lie devant une voyelle"],
         ["soixante centimètres","« soi-sante » — un s au milieu, pas un ks"],
         ["un schéma","« ché-ma » — sch fait ch"],
         ["le schiste","« chiste » — sch fait ch"],
         ["un short","« chort » — sh fait ch"],
       ]},

      {t:'piege', h:"Trois ennuis de chantier, et comment les éviter",
       rows:[
         ["répéter le mot comme on l'a entendu","le faire écrire",
          "Vous entendez « tecnique » et personne ne vous comprend quand vous écrivez « tecnique ». Sur un chantier, demandez qu'on vous écrive le mot : personne ne s'en formalise, tout le monde le fait."],
         ["lire « schéma » comme « skéma »","se rappeler que sch = ch, toujours",
          "En français, jamais « sk ». Ni dans schéma, ni dans schiste, ni dans schéma de plomberie. La règle n'a pas d'exception courante."],
         ["s'inquiéter du x de « six »","se dire que les trois formes passent",
          "Dire « siss semaines » ne fera lever un sourcil à personne. Ce qu'il faut, c'est reconnaître les trois formes à l'écoute — pas les placer parfaitement."],
       ]},

      {t:'check', h:"Quatre questions, une minute",
       p:"Sans revenir en arrière.",
       qs:[
         {q:"Dans « architecte », les lettres « ch » se disent…", opts:["comme dans chantier","comme un k"], ok:1,
          fb:"Mot passé par le grec : « ar-ki-tecte »."},
         {q:"Le x de « soixante » sonne…", opts:["comme un s","comme un ks"], ok:0,
          fb:"Deux syllabes : soi-sante. Même chose pour six et dix."},
         {q:"Le sch de « schiste » sonne…", opts:["comme un sk","comme dans chat"], ok:1,
          fb:"Trois lettres ramassées en un seul son."},
         {q:"« Six semaines » se prononce…", opts:["« si semaines »","« sisse semaines »"], ok:0,
          fb:"Devant une consonne, le x disparaît."},
       ]},

      {t:'revoir', h:"À retenir",
       p:"Trois familles seulement : <b>ch</b> qui dit k dans les mots savants (architecte, technique, chlore), <b>x</b> qui dit s dans les nombres (six, dix, soixante), <b>sh</b> et <b>sch</b> qui disent ch dans les emprunts (schéma, schiste, short). Trois familles, et tout le reste du français se lit normalement."},
    ]
  },

  prMots: {
    eye:'Mini-leçon', tit:"Le mot du métier et le mot de tous les jours",
    blocs:[
      {t:'texte', h:"Deux façons de dire la même chose",
       p:"Sur le trottoir, Léandre dit « l'eau part mal le long du mur ». Dans son rapport, Kettly Alcindor écrit « l'écoulement des eaux de surface est déficient ». C'est le même fait, la même maison, la même flaque. Ce qui change est la forme : le trottoir emploie des verbes, le rapport emploie des noms. Et ces noms-là ne sont pas d'autres mots : ce sont les mêmes verbes, habillés d'un suffixe.",
       note:"Le programme du niveau 6 demande d'employer préfixes et suffixes, et d'exploiter les familles de mots pour la nominalisation. C'est ce qui rend un document technique lisible."},

      {t:'ana', h:"Les trois suffixes qui fabriquent des noms",
       p:"Ils transforment l'action en chose. Ce sont ceux qu'on rencontre dans un rapport et dans une soumission.",
       mots:[['-age','creuser → le <b>creusage</b> · nettoyer → le <b>nettoyage</b> · sécher → le <b>séchage</b>'],
             ['-ment','écouler → l\'<b>écoulement</b> · effondrer → un <b>effondrement</b> · dédommager → un <b>dédommagement</b>'],
             ['-tion, -ation','rénover → une <b>rénovation</b> · installer → une <b>installation</b> · inspecter → une <b>inspection</b>', true],
             ['-ure','fissurer → une <b>fissure</b> · couvrir → une <b>couverture</b> · ouvrir → une <b>ouverture</b>']],
       say:"le séchage, l'écoulement, une rénovation, une fissure",
       note:"Le genre suit le suffixe : -age et -ment sont masculins, -tion et -ure sont féminines. Une règle qui ne se trompe presque jamais, et qui règle l'article du même coup."},

      {t:'ana', h:"Le suffixe -able : ce qu'on peut faire",
       p:"Il s'ajoute au verbe et en fait une qualité. Sur une maison, il décide souvent de la valeur des choses.",
       mots:[['habiter','un sous-sol <b>habitable</b>, une fois qu\'il est sec et éclairé'],
             ['réparer','une fissure <b>réparable</b>, tant qu\'elle ne bouge plus'],
             ['payer','un solde <b>payable</b> en trois versements', true],
             ['Le contraire','on met <b>in-</b>, <b>im-</b> ou <b>ir-</b> devant : inhabitable, imprévisible, irréparable']],
       say:"habitable, réparable, payable, inhabitable",
       note:"« Un sous-sol inhabitable » n'est pas un jugement de goût : c'est un mot qui a des conséquences, sur un permis comme sur une vente."},

      {t:'ana', h:"Les deux préfixes du chantier : re- et dé-",
       p:"L'un refait, l'autre défait. Sur un chantier, la moitié des verbes commencent par l'un des deux, parce qu'on travaille presque toujours sur ce qui existe déjà.",
       mots:[['re-, ré- refait','faire → <b>refaire</b> · couler → <b>recouler</b> · aménager → <b>réaménager</b>'],
             ['dé- défait','monter → <b>démonter</b> · brancher → <b>débrancher</b> · encombrer → <b>désencombrer</b>'],
             ['dés- devant une voyelle','humidifier → <b>déshumidifier</b> · installer → <b>désinstaller</b>', true],
             ['Le cas de « r- » tout court','ouvrir → <b>rouvrir</b>, pas « reouvrir » · entrer → <b>rentrer</b>']],
       say:"refaire, recouler, démonter, déshumidifier",
       note:"« Déshumidifier » se dit tous les jours pendant quatre semaines, dans ce module : c'est le verbe de l'attente."},

      {t:'labo', h:"Du verbe au nom, et du nom au verbe",
       p:"Choisissez un suffixe, puis un exemple.",
       axes:[
         {id:'s', lbl:'Quel suffixe ?', opts:[['a','-age'],['m','-ment'],['t','-tion']]},
         {id:'x', lbl:'Quel exemple ?', opts:[['1','le premier'],['2','le second']]}],
       out:{
         a1:{w:["sécher","le séchage"], say:"sécher, le séchage", n:'quatre semaines de séchage, c\'est une ligne de la soumission'},
         a2:{w:["nettoyer","le nettoyage"], say:"nettoyer, le nettoyage", n:'le nettoyage du chantier est parfois exclu du prix'},
         m1:{w:["écouler","l'écoulement"], say:"écouler, l'écoulement", n:'l\'écoulement des eaux de surface : la phrase du rapport'},
         m2:{w:["dédommager","un dédommagement"], say:"dédommager, un dédommagement", n:'un mot qu\'on espère ne jamais avoir à employer'},
         t1:{w:["rénover","une rénovation"], say:"rénover, une rénovation", n:'le mot du permis : permis de rénovation'},
         t2:{w:["inspecter","une inspection"], say:"inspecter, une inspection", n:'l\'inspection vient avant tout le reste'},
       },
       note:"Faites l'aller-retour dans les deux sens : du verbe au nom, puis du nom au verbe. C'est le second sens qui sert à lire un rapport."},

      {t:'ex', h:"Huit paires du module",
       p:"À gauche la langue de tous les jours, à droite celle des documents.",
       rows:[
         ["l'eau part mal","l'écoulement est déficient"],
         ["on refait le sous-sol","la rénovation du sous-sol"],
         ["quelqu'un est venu voir la maison","l'inspection du bâtiment"],
         ["on attend que ça sèche","la période de séchage"],
         ["on met de l'isolant","l'isolation des murs"],
         ["le mur a fendu","une fissure au mur de fondation"],
         ["on peut y vivre","le sous-sol est habitable"],
         ["on paiera en trois fois","le solde est payable en trois versements"],
       ]},

      {t:'piege', h:"Deux faux amis de la famille",
       rows:[
         ["dire « l'isolement des murs »","dire « l'isolation »",
          "L'<b>isolation</b> est le matériau et le travail ; l'<b>isolement</b> est le fait d'être seul. Deux suffixes, deux mondes. Sur une soumission, on ne lit jamais « isolement »."],
         ["dire « une réparation » pour l'objet","garder le nom pour l'action",
          "La réparation est le travail, pas la pièce. « J'ai payé la réparation » se dit ; « j'ai posé une réparation » ne se dit pas."],
       ]},

      {t:'check', h:"Trois questions",
       p:"Vite, sans réfléchir longtemps.",
       qs:[
         {q:"Le nom du verbe « sécher » est…", opts:["le séchement","le séchage"], ok:1,
          fb:"-age : le séchage. Masculin, comme tous les -age."},
         {q:"« Inhabitable » veut dire…", opts:["qu'on ne peut pas y vivre","qu'on n'y vit pas en ce moment"], ok:0,
          fb:"-able dit « qu'on peut » ; in- le renverse."},
         {q:"Le nom du verbe « inspecter » est…", opts:["une inspectation","une inspection"], ok:1,
          fb:"-tion, et le mot est féminin."},
       ]},

      {t:'revoir', h:"À retenir",
       p:"Un document technique dit avec des <b>noms</b> ce qu'on dit avec des <b>verbes</b>. Retrouvez le verbe caché dans le nom — écoulement, rénovation, séchage, inspection — et la phrase devient une phrase ordinaire."},
    ]
  },

  prEtapes: {
    eye:'Mini-leçon', tit:"Pourquoi un chantier ne commence pas par les travaux",
    blocs:[
      {t:'texte', h:"L'ordre coûte de l'argent",
       p:"On croit qu'un chantier commence quand quelqu'un arrive avec des outils. En réalité, tout ce qui décide du prix final se joue avant : ce qu'on a fait vérifier, ce qu'on a fait écrire, ce qu'on a fait autoriser. Une étape sautée ne se rattrape pas — elle se repaie.",
       note:"Ce n'est pas de la grammaire, mais c'est ce que la situation du programme demande de comprendre : de l'information reliée à des travaux de réparation ou de rénovation."},

      {t:'ana', h:"Les six étapes, et ce que chacune met dans vos mains",
       p:"Chacune produit un objet : un rapport, une confirmation, un document, un délai. Une étape qui ne produit rien n'a pas été faite.",
       mots:[['1. l\'inspection','un rapport écrit qui décrit l\'état réel, sans proposer de travaux'],
             ['2. la licence','la certitude que l\'entreprise a le droit d\'exécuter ces travaux', true],
             ['3. la soumission','un prix par ligne, et surtout une liste d\'exclusions'],
             ['4. le permis','l\'accord de la municipalité, et le nombre de jours qu\'il faut attendre'],
             ['5. l\'échéancier','la date de chaque étape, séchage compris'],
             ['6. la réunion de chantier','les réponses aux questions restées en suspens, devant tout le monde']],
       say:"l'inspection, la licence, la soumission, le permis, l'échéancier, la réunion de chantier",
       note:"Trois faits québécois, et le module n'en avance pas d'autres : au Québec, un entrepreneur qui exécute des travaux de construction pour autrui doit détenir une licence de la Régie du bâtiment, vérifiable au registre public de la Régie ; la plupart des municipalités exigent un permis pour certains travaux, et les exigences varient de l'une à l'autre ; avant de creuser, la localisation des infrastructures souterraines se demande gratuitement à Info-Excavation."},

      {t:'ana', h:"Ce qu'une inspection fait, et ce qu'elle ne fait pas",
       p:"C'est l'étape la plus mal comprise, parce qu'elle ne répare rien et qu'elle coûte quand même.",
       mots:[['Elle constate','elle décrit ce qui est, à une date donnée, avec des chiffres'],
             ['Elle dit ses limites','ce qui était fermé n\'a pas été vu, et le rapport l\'écrit', true],
             ['Elle ne propose rien','aucun entrepreneur recommandé, aucun travail chiffré'],
             ['Sa force vient de là','celle qui l\'a écrite n\'avait aucun intérêt dans les travaux à venir']],
       say:"elle constate, elle dit ses limites, elle ne propose rien",
       note:"Si le même papier constatait et proposait, il ne vaudrait plus rien : le jour d'un désaccord, on lui reprocherait de s'être vendu à lui-même."},

      {t:'ex', h:"Les questions à poser à chaque étape",
       p:"Une par étape. Elles se posent au téléphone, en trente secondes.",
       rows:[
         ["avant l'inspection","Est-ce que votre rapport écrit les limites de ce que vous avez pu voir ?"],
         ["avant de signer","Quel est votre numéro de licence, et quel est son état au registre ?"],
         ["à la soumission","Quelles sont les exclusions, et qu'arrive-t-il si vous trouvez un imprévu ?"],
         ["au permis","Quel délai je dois prévoir, et quels documents vous manquent ?"],
         ["à l'échéancier","Le séchage est-il compté dans les six semaines, ou après ?"],
         ["à la réunion","Vous m'écrivez ça aujourd'hui, ou je le note et je vous l'envoie ?"],
       ]},

      {t:'piege', h:"Les deux raccourcis les plus chers",
       rows:[
         ["accepter un prix donné de vive voix","demander une soumission écrite, détaillée",
          "Un chiffre lancé sur le pas de la porte n'engage personne, et il est toujours plus bas que la vraie facture. Ce n'est pas de la malhonnêteté : c'est qu'on ne peut pas chiffrer ce qu'on n'a pas détaillé."],
         ["se fier au permis qu'un voisin a obtenu","téléphoner à sa propre municipalité",
          "Les exigences varient d'une ville à l'autre, et parfois d'un secteur à l'autre. La seule réponse qui vous concerne est celle de votre municipalité, pour votre adresse."],
       ]},

      {t:'check', h:"Trois questions",
       qs:[
         {q:"Un rapport d'inspection recommande-t-il un entrepreneur ?", opts:["oui, c'est son travail","non, et c'est voulu"], ok:1,
          fb:"Il constate. C'est de là que lui vient sa valeur."},
         {q:"La licence d'entrepreneur se vérifie…", opts:["au registre public de la Régie du bâtiment","auprès du voisin qui l'a engagé"], ok:0,
          fb:"Le registre est public et se consulte en ligne."},
         {q:"Les exigences de permis sont-elles les mêmes partout au Québec ?", opts:["oui","non, elles varient d'une municipalité à l'autre"], ok:1,
          fb:"C'est à votre municipalité qu'on les demande, et à personne d'autre."},
       ]},

      {t:'revoir', h:"À retenir",
       p:"Six étapes, et chacune produit un papier ou une date : <b>l'inspection</b>, <b>la licence</b>, <b>la soumission</b>, <b>le permis</b>, <b>l'échéancier</b>, <b>la réunion de chantier</b>. Une étape dont il ne reste rien d'écrit n'a pas eu lieu."},
    ]
  },

  t1cause: {
    eye:'Mini-leçon', tit:"Remonter du visible à ce qui l'a produit",
    blocs:[
      {t:'texte', h:"Ce qu'on voit arrive toujours en second",
       p:"Une tache au plafond, une fente dans un mur, un plancher qui gondole : personne ne répare ça. Ce sont des résultats. La cause est ailleurs — presque toujours dehors, presque toujours une histoire d'eau, et presque toujours plus banale qu'on ne le croit. Un homme de métier commence par le visible parce que c'est ce que vous lui montrez, mais il n'y reste pas trente secondes.",
       note:"C'est aussi la matière grammaticale du défi : les connecteurs de cause et de conséquence, que le programme du niveau 6 range dans la grammaire du texte."},

      {t:'ana', h:"Les mots qui annoncent une cause",
       p:"Ils préviennent : ce qui suit explique ce qui précède.",
       mots:[['parce que + phrase','Le mur fend <b>parce que</b> le sol pousse dessus.'],
             ['à cause de + nom','La fondation est humide <b>à cause de</b> la gouttière.', true],
             ['grâce à + nom','Le sol reste sec <b>grâce à</b> la nouvelle pente.'],
             ['car, en effet','L\'injection attendra, <b>car</b> le mur reçoit encore de l\'eau.']],
       say:"parce que, à cause de, grâce à, car",
       note:"« À cause de » annonce un mauvais résultat, « grâce à » un bon. Les inverser fait sourire : « à cause de vos bons conseils » se dit, mais pas comme on le croit."},

      {t:'ana', h:"Les mots qui annoncent une conséquence",
       p:"Ils préviennent : ce qui suit découle de ce qui précède.",
       mots:[['donc, alors','Le sol pousse, <b>donc</b> le mur fend.'],
             ['de sorte que','L\'eau reste au pied du mur, <b>de sorte que</b> la fondation ne sèche jamais.', true],
             ['par conséquent','La cause n\'a pas été traitée ; <b>par conséquent</b>, la fissure est revenue.'],
             ['d\'où + nom','Le sol se gorge d\'eau, <b>d\'où</b> la pression sur le mur.']],
       say:"donc, de sorte que, par conséquent, d'où",
       note:"« D'où » est suivi d'un nom, jamais d'une phrase : « d'où la pression », pas « d'où le mur pousse »."},

      {t:'labo', h:"La même situation, dite dans les deux sens",
       p:"Choisissez un fait du module, puis le sens de la phrase.",
       axes:[
         {id:'p', lbl:'Quel fait ?', opts:[['a','la gouttière'],['b','le sol tassé'],['c','le mur refermé trop tôt']]},
         {id:'s', lbl:'Dans quel sens ?', opts:[['1','la cause d\'abord'],['2','le résultat d\'abord']]}],
       out:{
         a1:{w:["La gouttière se vide au pied du mur, donc le sol reste gorgé d'eau."], say:"La gouttière se vide au pied du mur, donc le sol reste gorgé d'eau.", n:'cause, puis conséquence : c\'est l\'ordre du diagnostic'},
         a2:{w:["Le sol reste gorgé d'eau à cause de la gouttière."], say:"Le sol reste gorgé d'eau à cause de la gouttière.", n:'résultat, puis cause : c\'est l\'ordre de la plainte'},
         b1:{w:["La terre s'est tassée, de sorte que la pente ramène l'eau vers la maison."], say:"La terre s'est tassée, de sorte que la pente ramène l'eau vers la maison.", n:'« de sorte que » se met toujours devant la conséquence'},
         b2:{w:["La pente ramène l'eau vers la maison parce que la terre s'est tassée."], say:"La pente ramène l'eau vers la maison parce que la terre s'est tassée.", n:'« parce que » répond à la question « pourquoi ? »'},
         c1:{w:["On a refermé le mur trop tôt, d'où la moisissure derrière le gypse."], say:"On a refermé le mur trop tôt, d'où la moisissure derrière le gypse.", n:'« d\'où » est suivi d\'un nom : la moisissure'},
         c2:{w:["La moisissure est apparue parce qu'on avait refermé le mur trop tôt."], say:"La moisissure est apparue parce qu'on avait refermé le mur trop tôt.", n:'notez le plus-que-parfait : le mur avait été refermé avant'},
       },
       note:"Le sens du diagnostic va de la cause au résultat ; le sens de la plainte va du résultat à la cause. Savoir faire les deux, c'est pouvoir suivre un homme de métier et lui répondre."},

      {t:'ex', h:"Six couples du module",
       p:"À gauche la cause, à droite le résultat.",
       rows:[
         ["la descente de gouttière se vide au pied du mur","le sol est gorgé d'eau à chaque orage"],
         ["le sol gorgé d'eau pousse sur la fondation","le mur de fondation fend en biais"],
         ["la terre s'est tassée avec les années","la pente ramène l'eau vers la maison"],
         ["la fondation reste humide","le taux d'humidité atteint dix-neuf pour cent"],
         ["on referme un mur encore humide","la moisissure pousse derrière le gypse neuf"],
         ["on n'a traité que le résultat","la fissure revient trois ans plus tard"],
       ]},

      {t:'piege', h:"Le piège qui coûte le plus cher",
       rows:[
         ["faire réparer ce qu'on voit","poser la question du « si je répare seulement ça »",
          "« Si je répare la fissure et que rien d'autre ne change, est-ce qu'elle revient ? » Cette phrase-là, posée à voix haute devant l'entrepreneur, vaut plusieurs milliers de dollars. S'il répond oui, vous savez que vous regardez un résultat."],
         ["croire qu'une cause explique tout","accepter qu'il y en ait deux ou trois",
          "La gouttière ET la pente ET le drain d'origine. Les causes s'additionnent souvent, et traiter une seule des trois ne règle qu'un tiers du problème."],
       ]},

      {t:'check', h:"Trois questions",
       qs:[
         {q:"Une fissure dans un mur de fondation est…", opts:["une cause","un résultat"], ok:1,
          fb:"Elle est ce qu'on voit. La cause est dehors."},
         {q:"« D'où » est suivi…", opts:["d'un nom","d'une phrase complète"], ok:0,
          fb:"« D'où la pression sur le mur » — jamais « d'où le mur pousse »."},
         {q:"« À cause de » annonce…", opts:["un bon résultat","un mauvais résultat"], ok:1,
          fb:"Pour un bon résultat, on emploie « grâce à »."},
       ]},

      {t:'revoir', h:"À retenir",
       p:"Le visible est un <b>résultat</b> ; la cause est ailleurs. Le test : « si je répare seulement ça, est-ce que ça revient ? ». Et deux familles de mots pour le dire — <b>parce que, à cause de, car</b> du côté de la cause ; <b>donc, de sorte que, par conséquent, d'où</b> du côté du résultat."},
    ]
  },

  t1repr: {
    eye:'Mini-leçon', tit:"Le petit mot qui porte toute une phrase",
    blocs:[
      {t:'texte', h:"Ce qui rend une explication difficile à suivre",
       p:"Fernand Trudelle parle vingt minutes sans reprendre son souffle. Le vocabulaire n'est pas le problème : il explique de lui-même ce que veut dire « injecter » ou « reprofiler ». Ce qui fait perdre le fil, ce sont trois lettres. « Je la répare », « on en a parlé », « il faut y penser » — et il faut savoir, chaque fois, de quoi il vient de parler. Le référent est parfois à trois répliques de distance.",
       note:"Le programme du niveau 6 y consacre quatre points de grammaire du texte : associer le pronom « le » à une subordonnée complétive, « en » à un GPrép inanimé, « où » à son antécédent, et reconnaître les deux référents quand le pronom CD est absent."},

      {t:'ana', h:"le, la, l', les — pour ce qui suit le verbe sans préposition",
       p:"On dit « je répare quelque chose », sans petit mot entre les deux. Le pronom est alors le, la, l' ou les.",
       mots:[['la fissure','Je vois la fissure. Je <b>la</b> répare la semaine prochaine.'],
             ['le rapport','Doïna a lu le rapport. Elle <b>l\'</b>a relu deux fois.', true],
             ['les gouttières','On rallonge les gouttières. On <b>les</b> rallonge d\'un mètre.'],
             ['Le test','remplacez le nom par « ça » : si « je répare ça » se dit, c\'est le, la ou les.']],
       say:"je la répare, elle l'a relu, on les rallonge",
       note:"Devant une voyelle, « le » et « la » deviennent « l' ». « Je l'ai relu » ne dit pas si c'est masculin ou féminin — seul le participe le dirait à l'écrit."},

      {t:'ana', h:"le — pour toute une idée, pas pour un objet",
       p:"C'est l'emploi que le niveau 6 ajoute, et c'est le plus difficile. « Le » reprend alors une phrase entière.",
       mots:[['ce qu\'on vient de dire','Le sous-sol est encore humide. Doïna <b>le</b> sait.'],
             ['une chose annoncée','Il faut attendre quatre semaines. Fernand me <b>l\'</b>a dit deux fois.', true],
             ['une question','Est-ce que le permis va sortir à temps ? Personne ne <b>le</b> sait.'],
             ['Le test','remplacez par « cela » : « Doïna sait cela » — oui, donc c\'est ce « le »-là.']],
       say:"Doïna le sait, Fernand me l'a dit, personne ne le sait",
       note:"Ce « le » ne s'accorde jamais : il ne remplace pas un nom, il remplace une idée. « Elle l'a su » et non « elle l'a sue »."},

      {t:'ana', h:"en et y — pour ce qui vient après une préposition",
       p:"Ils remplacent un groupe introduit par « de » ou par « à ». Le choix ne se fait pas au son : il se fait sur le verbe.",
       mots:[['parler <b>de</b> quelque chose → <b>en</b>','On a parlé du taux d\'humidité. On <b>en</b> a reparlé hier.'],
             ['avoir besoin <b>de</b> → <b>en</b>','Vous avez besoin d\'une réserve ? Vous <b>en</b> aurez besoin.', true],
             ['penser <b>à</b> quelque chose → <b>y</b>','Il faut penser au permis. J\'<b>y</b> pense tous les jours.'],
             ['un lieu → <b>y</b>','Le sous-sol ? On <b>y</b> descend par la cuisine.']],
       say:"on en a reparlé, vous en aurez besoin, j'y pense, on y descend",
       note:"Le seul travail à faire est de retrouver la préposition du verbe. Parler DE, avoir besoin DE, s'occuper DE → en. Penser À, s'habituer À, aller À → y."},

      {t:'labo', h:"Deux phrases, un pronom",
       p:"Choisissez le verbe, puis le pronom qu'il commande.",
       axes:[
         {id:'v', lbl:'Quel verbe ?', opts:[['r','réparer quelque chose'],['p','parler de quelque chose'],['s','penser à quelque chose']]},
         {id:'e', lbl:'Quel exemple ?', opts:[['1','le premier'],['2','le second']]}],
       out:{
         r1:{w:["Je vois la fissure. Je la répare demain."], say:"Je vois la fissure. Je la répare demain.", n:'réparer quelque chose : aucune préposition, donc « la »'},
         r2:{w:["Doïna a lu le rapport. Elle l'a relu hier soir."], say:"Doïna a lu le rapport. Elle l'a relu hier soir.", n:'lire quelque chose : « le », qui devient « l\' » devant une voyelle'},
         p1:{w:["On a parlé du taux d'humidité. On en a reparlé hier."], say:"On a parlé du taux d'humidité. On en a reparlé hier.", n:'parler DE : le pronom est « en »'},
         p2:{w:["Il y a deux solutions. Fernand en a proposé une troisième."], say:"Il y a deux solutions. Fernand en a proposé une troisième.", n:'« en » reprend aussi une quantité : une troisième de ces solutions'},
         s1:{w:["Il faut penser au permis. J'y pense tous les jours."], say:"Il faut penser au permis. J'y pense tous les jours.", n:'penser À : le pronom est « y »'},
         s2:{w:["La maison repose sur cette fondation. On ne peut pas y toucher."], say:"La maison repose sur cette fondation. On ne peut pas y toucher.", n:'toucher À quelque chose : encore « y »'},
       },
       note:"Refaites le laboratoire en cachant la seconde phrase : c'est en la reconstruisant qu'on installe le réflexe."},

      {t:'ex', h:"Huit reprises du dialogue",
       p:"À gauche ce qui a été dit, à droite ce que le pronom reprend.",
       rows:[
         ["Je la répare seulement après","la fissure"],
         ["Elle l'a relu deux fois","le rapport d'inspection"],
         ["Il faut y penser tout de suite","au permis municipal"],
         ["On en a reparlé dans le rapport","du taux d'humidité"],
         ["Doïna le sait","que le sous-sol n'est pas sec"],
         ["Fernand en a proposé une troisième","des solutions"],
         ["On ne peut pas y toucher sans plan","à la fondation"],
         ["Léandre le lui a déconseillé","de faire les travaux lui-même"],
       ]},

      {t:'piege', h:"Trois confusions classiques",
       rows:[
         ["choisir le pronom au son","le choisir sur le verbe",
          "« J'en pense » n'existe pas, parce qu'on pense À. « J'y parle » n'existe pas non plus, parce qu'on parle DE. Cherchez la préposition, jamais l'oreille."],
         ["accorder le « le » d'une idée","le laisser invariable",
          "« Elle l'a su » et non « elle l'a sue » : ce « le » reprend une phrase entière, et une phrase n'a pas de genre."],
         ["répéter le nom par prudence","le reprendre",
          "Répéter « la fissure » six fois dans un paragraphe se lit comme un texte d'enfant. Le niveau 6 demande justement l'inverse : reprendre sans répéter."],
       ]},

      {t:'check', h:"Quatre questions",
       qs:[
         {q:"« On a parlé de la soumission. On ___ a parlé hier. »", opts:["en","y"], ok:0,
          fb:"Parler DE quelque chose : le pronom est « en »."},
         {q:"« Il faut penser au séchage. Il faut ___ penser. »", opts:["en","y"], ok:1,
          fb:"Penser À quelque chose : le pronom est « y »."},
         {q:"Dans « Doïna le sait », « le » reprend…", opts:["un objet","toute une idée"], ok:1,
          fb:"Remplacez par « cela » : ça marche, donc c'est une idée."},
         {q:"« Elle l'a su » ou « elle l'a sue » ?", opts:["elle l'a su","elle l'a sue"], ok:0,
          fb:"Ce « le »-là ne s'accorde jamais."},
       ]},

      {t:'revoir', h:"À retenir",
       p:"Le pronom se choisit sur le <b>verbe</b>, jamais au son. Verbe sans préposition → <b>le, la, les</b>. Verbe avec <b>de</b> → <b>en</b>. Verbe avec <b>à</b>, ou un lieu → <b>y</b>. Et un « le » à part, qui reprend une idée entière et ne s'accorde jamais."},
    ]
  },

  t1pqp: {
    eye:'Mini-leçon', tit:"Ce qui était déjà arrivé avant",
    blocs:[
      {t:'texte', h:"Un diagnostic remonte le temps",
       p:"Un homme de métier ne raconte pas une histoire dans l'ordre. Il part d'aujourd'hui — « le mur est fendu » —, puis il recule d'un cran — « quand vous avez acheté, elle était déjà là » —, puis d'un autre — « quelqu'un avait condamné le puisard avant vous ». Chaque recul demande un temps de verbe différent, et le plus-que-parfait est celui du dernier cran.",
       note:"Le programme du niveau 6 le formule ainsi : comprendre que le plus-que-parfait désigne une action précédant une autre action passée, et comprendre l'antériorité quand le point de référence est décalé."},

      {t:'ana', h:"Sa forme : imparfait de l'auxiliaire + participe passé",
       p:"Rien de neuf à apprendre : c'est le passé composé dont l'auxiliaire passe à l'imparfait.",
       mots:[['avec avoir','j\'<b>avais vu</b> · tu <b>avais lu</b> · il <b>avait fait</b> · nous <b>avions posé</b>'],
             ['avec être','elle <b>était venue</b> · ils <b>étaient partis</b>', true],
             ['aux verbes pronominaux','la terre <b>s\'était tassée</b> · la fissure <b>s\'était ouverte</b>'],
             ['à la forme négative','le plan <b>n\'était pas parti</b> le jour prévu']],
       say:"j'avais vu, elle était venue, la terre s'était tassée",
       note:"Le choix de l'auxiliaire est le même qu'au passé composé : ce qui va avec « être » au passé composé y reste."},

      {t:'ana', h:"Ce qu'il fait dans une phrase",
       p:"Il place une action avant une autre action déjà passée. Il y a donc toujours deux moments dans le passé, et il occupe le plus ancien.",
       mots:[['deux moments','Quand nous <u>avons acheté</u> la maison, la fissure <b>s\'était</b> déjà <b>ouverte</b>.'],
             ['le mot qui l\'annonce','<b>déjà</b>, presque toujours : « il l\'avait déjà noté ».', true],
             ['dans une explication','Fernand a retrouvé le problème vite : l\'inspectrice l\'<b>avait noté</b>.'],
             ['dans un rapport','En 1961, on a coulé la dalle ; personne n\'<b>avait posé</b> de membrane à l\'époque.']],
       say:"la fissure s'était déjà ouverte, l'inspectrice l'avait noté",
       note:"Quand vous entendez « déjà » dans un récit au passé, le plus-que-parfait n'est jamais loin. C'est le meilleur repère à l'écoute."},

      {t:'labo', h:"Deux actions, deux temps",
       p:"Choisissez un couple d'actions, puis regardez laquelle vient en premier.",
       axes:[
         {id:'c', lbl:'Quel couple ?', opts:[['a','acheter / la fissure'],['b','ouvrir / le puisard'],['c','comprendre / relire']]},
         {id:'o', lbl:'Quoi montrer ?', opts:[['1','la phrase'],['2','l\'ordre réel']]}],
       out:{
         a1:{w:["Quand nous avons acheté la maison, la fissure s'était déjà ouverte."], say:"Quand nous avons acheté la maison, la fissure s'était déjà ouverte.", n:'deux moments passés dans la même phrase'},
         a2:{w:["1. la fissure s'ouvre — 2. on achète la maison"], say:"D'abord la fissure s'ouvre, ensuite on achète la maison.", n:'le plus-que-parfait occupe toujours le moment le plus ancien'},
         b1:{w:["Quand l'équipe a ouvert le plancher, quelqu'un avait condamné le puisard bien avant."], say:"Quand l'équipe a ouvert le plancher, quelqu'un avait condamné le puisard bien avant.", n:'« bien avant » renforce ce que le temps dit déjà'},
         b2:{w:["1. quelqu'un condamne le puisard — 2. l'équipe ouvre le plancher"], say:"D'abord quelqu'un condamne le puisard, ensuite l'équipe ouvre le plancher.", n:'des années séparent les deux'},
         c1:{w:["Doïna a compris la deuxième explication, parce qu'elle avait relu le rapport la veille."], say:"Doïna a compris la deuxième explication, parce qu'elle avait relu le rapport la veille.", n:'la cause est antérieure : donc plus-que-parfait'},
         c2:{w:["1. elle relit le rapport — 2. elle comprend l'explication"], say:"D'abord elle relit le rapport, ensuite elle comprend l'explication.", n:'l\'ordre des mots n\'est pas l\'ordre des choses'},
       },
       note:"Le second axe est l'exercice réel : refaire la ligne du temps à partir de la phrase. C'est ce que le programme appelle comprendre l'antériorité."},

      {t:'ex', h:"Six phrases du diagnostic",
       p:"À gauche la phrase, à droite ce qui s'est passé en premier.",
       rows:[
         ["Quand ils ont acheté, la fissure s'était déjà ouverte.","l'ouverture de la fissure"],
         ["L'inspectrice l'avait noté dans son rapport.","la note de l'inspectrice"],
         ["Le sol poussait, parce que la terre s'était tassée.","le tassement de la terre"],
         ["On a ouvert : quelqu'un avait condamné le puisard.","la condamnation du puisard"],
         ["Elle a compris, parce qu'elle avait relu le rapport.","la relecture du rapport"],
         ["Le permis a tardé : le plan n'était pas parti à temps.","le plan resté sur la table"],
       ]},

      {t:'piege', h:"Deux erreurs, et ce qu'elles font entendre",
       rows:[
         ["tout mettre au passé composé","garder le plus-que-parfait pour ce qui est plus ancien",
          "« Quand on a acheté, la fissure s'est ouverte » veut dire qu'elle s'est ouverte le jour de l'achat. Ce n'est pas ce que vous vouliez dire, et l'entrepreneur, lui, l'entend."],
         ["oublier l'accord avec être","accorder le participe comme au passé composé",
          "« La terre s'était tassé » n'existe pas : « s'était tassée ». Les mêmes règles qu'au passé composé continuent de s'appliquer."],
       ]},

      {t:'check', h:"Trois questions",
       qs:[
         {q:"Le plus-que-parfait se forme avec l'auxiliaire à…", opts:["l'imparfait","au présent"], ok:0,
          fb:"avais vu, était venue : l'auxiliaire est à l'imparfait."},
         {q:"« Quand il est arrivé, on avait déjà coulé la dalle. » Qu'est-ce qui vient en premier ?", opts:["son arrivée","la coulée de la dalle"], ok:1,
          fb:"Le plus-que-parfait occupe le moment le plus ancien."},
         {q:"Le mot qui accompagne le plus souvent le plus-que-parfait est…", opts:["déjà","toujours"], ok:0,
          fb:"« Il l'avait déjà noté » : c'est le meilleur repère à l'écoute."},
       ]},

      {t:'revoir', h:"À retenir",
       p:"<b>Auxiliaire à l'imparfait + participe passé.</b> Il dit : c'était <b>déjà</b> fait avant l'autre action passée. Dans un diagnostic, il occupe toujours le moment le plus ancien — et c'est lui qui vous dit que le problème ne date pas de vous."},
    ]
  },

  t1faire: {
    eye:'Mini-leçon', tit:"Faire faire, laisser faire — les deux verbes du propriétaire",
    blocs:[
      {t:'texte', h:"Le titre du module est une leçon de grammaire",
       p:"« Faire faire des travaux » : deux fois le même verbe, et il ne veut pas dire la même chose les deux fois. Le premier « faire » ne parle pas de travail, il parle de décision. C'est vous qui faites faire ; c'est un autre qui fait. Entre les deux, il y a un contrat, une soumission et un prix — et c'est très exactement ce que ce module raconte.",
       note:"Le programme du niveau 6 range ces tournures dans les auxiliaires factitifs : employer faire + infinitif avec par, employer laisser + infinitif."},

      {t:'ana', h:"faire + infinitif : c'est un autre qui exécute",
       p:"Le sujet décide, commande, paie. Il ne pose pas les mains dessus.",
       mots:[['au présent','Je <b>fais injecter</b> la fissure. · Elle <b>fait refaire</b> la pente.'],
             ['au passé composé','Il <b>a fait poser</b> une membrane. · On <b>a fait venir</b> un spécialiste.', true],
             ['dire par qui, avec <b>par</b>','Je fais injecter la fissure <b>par</b> un sous-traitant.'],
             ['le participe ne s\'accorde pas','La fissure qu\'il a <b>fait</b> injecter — jamais « faite ».']],
       say:"je fais injecter, elle fait refaire, il a fait poser",
       note:"Le participe « fait » suivi d'un infinitif reste invariable, toujours. C'est une des rares règles d'accord qui n'a aucune exception."},

      {t:'ana', h:"laisser + infinitif : on n'empêche pas",
       p:"Personne n'agit. On permet, ou bien on attend que ça se fasse tout seul.",
       mots:[['attendre','On <b>laisse sécher</b> quatre semaines.'],
             ['permettre','Doïna n\'a pas <b>laissé</b> Marius <b>toucher</b> au panneau électrique.', true],
             ['ne pas empêcher','Ne <b>laissez</b> pas la gouttière <b>se vider</b> au pied du mur.'],
             ['la nuance','« laisser » n\'engage aucune dépense ; « faire » en engage toujours une.']],
       say:"on laisse sécher, ne laissez pas la gouttière se vider",
       note:"Sur une soumission, « faire sécher » se facture — il y a un déshumidificateur en location. « Laisser sécher » ne se facture pas : on attend."},

      {t:'labo', h:"La même action, trois rapports",
       p:"Choisissez une action, puis qui s'en occupe.",
       axes:[
         {id:'a', lbl:'Quelle action ?', opts:[['i','injecter la fissure'],['s','sécher le mur'],['p','poser le gypse']]},
         {id:'q', lbl:'Qui agit ?', opts:[['1','je le fais moi-même'],['2','je le fais faire'],['3','je laisse faire']]}],
       out:{
         i1:{w:["J'injecte la fissure moi-même."], say:"J'injecte la fissure moi-même.", n:'à éviter : l\'injection sous pression est un métier'},
         i2:{w:["Je fais injecter la fissure par un spécialiste."], say:"Je fais injecter la fissure par un spécialiste.", n:'la phrase exacte de Fernand Trudelle'},
         i3:{w:["Je laisse la fissure travailler encore un hiver."], say:"Je laisse la fissure travailler encore un hiver.", n:'ne rien faire est aussi une décision — et elle se paie'},
         s1:{w:["Je sèche le mur avec un déshumidificateur."], say:"Je sèche le mur avec un déshumidificateur.", n:'j\'agis : il y a un appareil et une facture'},
         s2:{w:["Je fais sécher le mur pendant quatre semaines."], say:"Je fais sécher le mur pendant quatre semaines.", n:'même chose, dit du point de vue de celui qui décide'},
         s3:{w:["Je laisse sécher le mur pendant quatre semaines."], say:"Je laisse sécher le mur pendant quatre semaines.", n:'j\'attends : aucun appareil, aucune ligne de soumission'},
         p1:{w:["Je pose le gypse avec Marius la fin de semaine."], say:"Je pose le gypse avec Marius la fin de semaine.", n:'possible, et c\'est une façon de baisser le prix'},
         p2:{w:["Je fais poser le gypse par l'équipe de Fernand."], say:"Je fais poser le gypse par l'équipe de Fernand.", n:'c\'est le poste 4 de la soumission'},
         p3:{w:["Je laisse l'équipe poser le gypse à sa façon."], say:"Je laisse l'équipe poser le gypse à sa façon.", n:'« laisser » dit ici qu\'on ne se mêle pas de la méthode'},
       },
       note:"Les trois colonnes du laboratoire sont les trois façons de mener un chantier, et elles n'ont pas le même prix. La grammaire suit la dépense."},

      {t:'ex', h:"Six phrases du module",
       p:"À gauche la phrase, à droite qui pose les mains dessus.",
       rows:[
         ["Je fais injecter la fissure.","un sous-traitant spécialisé"],
         ["On laisse sécher quatre semaines.","personne : on attend"],
         ["Fernand a fait refaire la pente du terrain.","son sous-traitant en excavation"],
         ["Doïna n'a pas laissé Marius toucher au panneau.","personne : elle a empêché"],
         ["On fait entrer l'électricien mardi.","l'électricien, qui vient parce qu'on l'appelle"],
         ["Ne laissez pas l'eau s'accumuler au pied du mur.","personne : c'est une mise en garde"],
       ]},

      {t:'piege', h:"Deux erreurs qui changent la facture",
       rows:[
         ["dire « je fais sécher » quand on attend","dire « je laisse sécher »",
          "« Faire sécher » suppose un appareil et un coût ; « laisser sécher » suppose du temps. Devant un entrepreneur, ces deux phrases n'appellent pas la même ligne sur la soumission."],
         ["accorder le participe « fait »","le laisser invariable devant un infinitif",
          "« La fissure qu'il a fait injecter » — jamais « faite ». Le participe de « faire » suivi d'un infinitif ne s'accorde jamais."],
       ]},

      {t:'check', h:"Trois questions",
       qs:[
         {q:"« Je fais injecter la fissure » veut dire…", opts:["que je l'injecte moi-même","que quelqu'un l'injecte pour moi"], ok:1,
          fb:"Faire + infinitif : un autre exécute."},
         {q:"Pour dire par qui, on emploie…", opts:["par","avec"], ok:0,
          fb:"« Je fais injecter la fissure par un spécialiste. »"},
         {q:"« La fissure qu'il a ___ injecter » :", opts:["fait","faite"], ok:0,
          fb:"Devant un infinitif, « fait » reste invariable."},
       ]},

      {t:'revoir', h:"À retenir",
       p:"<b>Faire + infinitif</b> : vous décidez, un autre exécute, et « par » dit qui. <b>Laisser + infinitif</b> : personne n'agit, on permet ou on attend. Et le participe <b>fait</b> devant un infinitif ne s'accorde jamais."},
    ]
  },

  t2rapport: {
    eye:'Mini-leçon', tit:"Lire un rapport d'inspection sans le lire en entier",
    blocs:[
      {t:'texte', h:"Onze pages qu'on ne lit jamais du début à la fin",
       p:"Un rapport d'inspection n'est pas fait pour être lu comme un livre. Il est fait pour qu'on y retrouve une chose précise, deux ans plus tard, au téléphone, pendant qu'un entrepreneur attend au bout du fil. Tout, dans sa présentation, sert à ça : les sections numérotées, les constatations chiffrées, les photos, et une section de limites que personne ne lit et qui est la plus importante.",
       note:"Le programme du niveau 6 demande de tenir compte de la présentation matérielle et de la mise en page. C'est ici que ça se joue, plus que dans n'importe quel autre écrit du module."},

      {t:'ana', h:"Ce que la présentation vous dit avant les phrases",
       p:"Quatre signaux, et ils se lisent en trois secondes, avant même de commencer une phrase.",
       mots:[['un titre en majuscules','une section commence, et elle porte sur une seule partie du bâtiment'],
             ['un numéro devant','on pourra y revenir en le citant : « la constatation 2 »', true],
             ['un chiffre avec une unité','dix-neuf pour cent, un mètre, quarante centimètres : ça se remesure'],
             ['une section « limites »','ce que l\'inspection n\'a pas pu voir, et donc ce qu\'elle ne garantit pas']],
       say:"un titre, un numéro, un chiffre avec une unité, une section de limites",
       note:"Au téléphone, ne dites jamais « à la page du mur ». Dites « la section 2, la fissure oblique ». Vous serez compris tout de suite, et pris au sérieux."},

      {t:'ana', h:"Les quatre choses qu'un rapport ne fait pas",
       p:"Ce qu'il ne fait pas est aussi utile à savoir que ce qu'il fait, parce que c'est ce que vous irez chercher ailleurs.",
       mots:[['il ne chiffre pas les travaux','aucun prix, aucune estimation : c\'est le travail de la soumission'],
             ['il ne recommande personne','aucun entrepreneur nommé, et c\'est ce qui fait sa valeur', true],
             ['il ne voit pas derrière les murs','une inspection est visuelle, non destructive'],
             ['il ne vaut qu\'à sa date','« l\'état observé le 18 septembre », et pas deux ans plus tard']],
       say:"il ne chiffre pas, il ne recommande personne, il ne voit pas derrière les murs",
       note:"Une inspectrice qui recommanderait un entrepreneur et qui constaterait en même temps aurait un intérêt dans les travaux. Son rapport ne vaudrait plus rien devant un désaccord."},

      {t:'ex', h:"Où chercher quoi",
       p:"Six renseignements, et la section où ils se trouvent.",
       rows:[
         ["l'année de construction","section 1, Historique du bâtiment"],
         ["l'état de la fondation","section 2, Fondation et drainage"],
         ["le taux d'humidité d'un mur","section 2, dans la phrase chiffrée"],
         ["ce qui n'a pas pu être vérifié","section 3, à la fin du paragraphe"],
         ["ce qui n'a pas été ouvert","section 4, Limites de l'inspection"],
         ["la date et l'heure de la visite","tout en haut, avec le numéro de dossier"],
       ]},

      {t:'piege', h:"Deux façons de mal se servir d'un rapport",
       rows:[
         ["y chercher un prix","aller chercher le prix dans une soumission",
          "Un rapport qui donnerait un prix aurait choisi son camp. C'est pour ça qu'il n'en donne pas — et non parce qu'il est incomplet."],
         ["croire que ce qui n'y est pas n'existe pas","lire la section des limites",
          "« Non vérifié » n'est pas « en bon état ». La dalle de Doïna n'avait pas de membrane, et le rapport ne l'avait pas dit : il avait écrit qu'il n'avait pas pu le vérifier. Ce n'est pas la même chose."],
       ]},

      {t:'check', h:"Trois questions",
       qs:[
         {q:"Un rapport d'inspection donne-t-il un prix ?", opts:["oui","non"], ok:1,
          fb:"Il constate ; la soumission chiffre."},
         {q:"« La présence d'une membrane n'est ni confirmée ni infirmée » veut dire…", opts:["qu'il n'y en a pas","qu'on ne sait pas"], ok:1,
          fb:"Non vérifié n'est pas en bon état."},
         {q:"Pour citer une constatation au téléphone, on dit…", opts:["la page du mur","la section 2"], ok:1,
          fb:"C'est à ça que servent les numéros."},
       ]},

      {t:'revoir', h:"À retenir",
       p:"Un rapport se lit <b>par sections</b>, jamais en entier. Il <b>constate</b> et il <b>chiffre</b> ; il ne propose rien et ne recommande personne. Et sa section la plus utile est celle des <b>limites</b> : ce qu'il n'a pas pu voir."},
    ]
  },

  t2mise: {
    eye:'Mini-leçon', tit:"Deux papiers, deux métiers",
    blocs:[
      {t:'texte', h:"Le même chantier, décrit deux fois",
       p:"Sur la table de Doïna, deux documents parlent de la même maison la même semaine, et ils ne se contredisent pas : ils ne font pas le même travail. Le rapport décrit ce qui est ; la soumission décrit ce qui sera fait. Confondre les deux, c'est aller chercher un prix dans le premier et une vérité dans le second — et n'en trouver ni dans l'un ni dans l'autre.",
       note:"Savoir d'avance ce qu'un papier va donner, c'est déjà la moitié de la lecture. C'est le geste que le module installe."},

      {t:'ana', h:"Le rapport d'inspection",
       p:"Écrit par quelqu'un qui ne fera pas les travaux, et payé par vous.",
       mots:[['son verbe','constater : il dit ce qu\'il a vu, à une date, avec des chiffres'],
             ['sa mise en page','des sections numérotées, une constatation par paragraphe, des photos', true],
             ['sa langue','impersonnelle, sans « je » ; parfois du passé simple dans l\'historique'],
             ['sa partie décisive','les limites : ce qui n\'a pas pu être vu']],
       say:"constater, des sections numérotées, une langue sans je, les limites",
       note:"C'est le seul des deux papiers qui n'a rien à vendre. Voilà pourquoi il pèse lourd le jour d'un désaccord."},

      {t:'ana', h:"La soumission",
       p:"Écrite par celui qui exécutera, et gratuite — jusqu'à ce qu'on signe.",
       mots:[['son verbe','proposer : elle dit ce qu\'elle fera, et pour combien'],
             ['sa mise en page','des postes numérotés, un prix par ligne, un total, un échéancier', true],
             ['sa durée de vie','trente jours, en général, et la date est écrite en haut'],
             ['sa partie décisive','les exclusions : ce qui n\'est pas dans le prix']],
       say:"proposer, un prix par ligne, trente jours, les exclusions",
       note:"Les exclusions sont écrites en petit, en bas, après le total. Ce n'est pas un hasard : c'est là que la facture finale se joue."},

      {t:'labo', h:"Où chercher ce renseignement",
       p:"Choisissez ce que vous cherchez, puis voyez dans quel papier aller.",
       axes:[
         {id:'q', lbl:'Vous cherchez…', opts:[['h','un chiffre sur l\'état du bâtiment'],['p','un montant'],['d','une date']]},
         {id:'n', lbl:'Lequel ?', opts:[['1','le premier exemple'],['2','le second']]}],
       out:{
         h1:{w:["le taux d'humidité du mur nord"], say:"le taux d'humidité du mur nord", n:'le rapport, section 2, dans la phrase chiffrée'},
         h2:{w:["l'année de construction de la maison"], say:"l'année de construction de la maison", n:'le rapport, section 1, écrite au passé des récits'},
         p1:{w:["l'acompte à verser à la signature"], say:"l'acompte à verser à la signature", n:'la soumission, juste sous le total'},
         p2:{w:["le prix du séchage assisté"], say:"le prix du séchage assisté", n:'la soumission, poste 3 des postes inclus'},
         d1:{w:["la date de l'inspection"], say:"la date de l'inspection", n:'le rapport, tout en haut, avec le numéro de dossier'},
         d2:{w:["la date jusqu'à laquelle le prix tient"], say:"la date jusqu'à laquelle le prix tient", n:'la soumission, première ligne : valide trente jours'},
       },
       note:"Refaites le laboratoire en vous demandant chaque fois : est-ce que je cherche un état, ou une intention ? L'état est dans le rapport, l'intention dans la soumission."},

      {t:'ex', h:"Six renseignements, deux papiers",
       rows:[
         ["le taux d'humidité du mur nord","le rapport, section 2"],
         ["le montant à verser à la signature","la soumission, sous le total"],
         ["l'année de construction","le rapport, section 1"],
         ["ce qui n'est pas compris dans le prix","la soumission, tout en bas"],
         ["ce que l'inspectrice n'a pas pu voir","le rapport, section 4"],
         ["la durée de validité du prix","la soumission, première ligne"],
       ]},

      {t:'piege', h:"Deux confusions de table de cuisine",
       rows:[
         ["chercher un prix dans le rapport","le chercher dans la soumission",
          "Un rapport qui chiffrerait des travaux se placerait du côté de celui qui les fait. Il n'en donne pas, exprès."],
         ["croire la soumission sur l'état du bâtiment","croire le rapport",
          "Une soumission décrit ce qu'elle fera, pas ce qui est. Si les deux papiers ne disent pas la même chose sur l'état d'un mur, c'est le rapport qui l'emporte."],
       ]},

      {t:'check', h:"Trois questions",
       qs:[
         {q:"Le mot « exclusions » appartient…", opts:["au rapport","à la soumission"], ok:1,
          fb:"C'est la partie la plus utile d'une soumission, et la plus vite sautée."},
         {q:"Le mot « limites » appartient…", opts:["au rapport","à la soumission"], ok:0,
          fb:"Ce que l'inspection n'a pas pu voir."},
         {q:"Combien de temps un prix de soumission tient-il, en général ?", opts:["trente jours","toujours"], ok:0,
          fb:"Et la date de départ est écrite en haut."},
       ]},

      {t:'revoir', h:"À retenir",
       p:"Le <b>rapport</b> constate un état, par sections numérotées, et sa partie décisive est celle des <b>limites</b>. La <b>soumission</b> propose des travaux, par postes chiffrés, et sa partie décisive est celle des <b>exclusions</b>. Un état contre une intention : ils ne se contredisent jamais vraiment."},
    ]
  },

  t2ou: {
    eye:'Mini-leçon', tit:"« où » : un endroit, mais aussi un moment",
    blocs:[
      {t:'texte', h:"Le mot qui colle deux phrases",
       p:"« Le mur nord présente dix-neuf pour cent d'humidité. La fissure a été relevée dans ce mur. » Deux phrases, et le nom du mur écrit deux fois. Un rapport technique ne peut pas se permettre ça : il aurait trois cents phrases et il répéterait le même mot toutes les deux lignes. « Où » sert exactement à ça — coller les deux, et ne nommer le mur qu'une seule fois.",
       note:"Le programme du niveau 6 le demande deux fois : associer le pronom relatif de lieu ou de temps « où » à son antécédent, et employer des phrases subordonnées relatives avec « où »."},

      {t:'ana', h:"« où » pour un endroit",
       p:"C'est l'emploi qu'on connaît déjà, et le plus simple.",
       mots:[['un mur','Le mur nord, <b>où</b> la fissure a été relevée, est le plus humide.'],
             ['une pièce','Le coin du sous-sol <b>où</b> le puisard se trouve reste froid.', true],
             ['une ville','Saint-Jérôme, <b>où</b> ils habitent depuis deux ans.'],
             ['Le test','on pourrait dire « dans lequel », « sur lequel », « auquel ».']],
       say:"le mur nord où la fissure a été relevée, le coin où le puisard se trouve",
       note:"« Où » remplace ici tout un groupe : dans ce mur, dans ce coin, dans cette ville. Un seul mot pour trois."},

      {t:'ana', h:"« où » pour un moment",
       p:"C'est l'emploi que le niveau 6 ajoute, et c'est le plus fréquent à l'écrit — alors qu'il n'a rien à voir avec un lieu.",
       mots:[['un jour','Le jour <b>où</b> on a ouvert le plancher, tout a changé.'],
             ['une année','L\'année <b>où</b> la maison fut construite, on ne posait pas de membrane.', true],
             ['un moment','Le moment <b>où</b> le béton est sec est celui où l\'on referme.'],
             ['une semaine','La semaine <b>où</b> le permis est arrivé, l\'équipe est revenue.']],
       say:"le jour où, l'année où, le moment où, la semaine où",
       note:"On n'écrit jamais « le jour que ». Ça s'entend beaucoup à l'oral, ça ne s'écrit pas, et un correcteur le relève chaque fois."},

      {t:'labo', h:"Coller deux phrases en une",
       p:"Choisissez le mot de départ, puis regardez la phrase soudée.",
       axes:[
         {id:'m', lbl:'Quel mot ?', opts:[['a','le mur'],['b','le jour'],['c','l\'année']]},
         {id:'e', lbl:'Quoi voir ?', opts:[['1','les deux phrases'],['2','la phrase soudée']]}],
       out:{
         a1:{w:["Le mur nord est le plus humide. La fissure a été relevée dans ce mur."], say:"Le mur nord est le plus humide. La fissure a été relevée dans ce mur.", n:'le nom du mur est écrit deux fois'},
         a2:{w:["Le mur nord, où la fissure a été relevée, est le plus humide."], say:"Le mur nord, où la fissure a été relevée, est le plus humide.", n:'une seule phrase, et deux virgules qui encadrent l\'ajout'},
         b1:{w:["Tout a changé ce jour-là. On a ouvert le plancher ce jour-là."], say:"Tout a changé ce jour-là. On a ouvert le plancher ce jour-là.", n:'« ce jour-là » revient deux fois'},
         b2:{w:["Le jour où on a ouvert le plancher, tout a changé."], say:"Le jour où on a ouvert le plancher, tout a changé.", n:'« où » pour un moment : l\'emploi le plus fréquent à l\'écrit'},
         c1:{w:["La maison fut construite en 1961. On ne posait pas de membrane cette année-là."], say:"La maison fut construite en 1961. On ne posait pas de membrane cette année-là.", n:'deux faits, deux phrases'},
         c2:{w:["L'année où la maison fut construite, on ne posait pas de membrane."], say:"L'année où la maison fut construite, on ne posait pas de membrane.", n:'la phrase du rapport, en une seule ligne'},
       },
       note:"Faites l'exercice à l'envers aussi : prenez une phrase avec « où » et coupez-la en deux. C'est ce qu'on fait dans sa tête pour comprendre un rapport."},

      {t:'ex', h:"La virgule change le sens",
       p:"À gauche sans virgule, à droite avec.",
       rows:[
         ["Le mur où la fissure a été relevée…","dit lequel des murs : il y en a plusieurs"],
         ["Le mur nord, où la fissure a été relevée, …","ajoute un renseignement sur un mur déjà nommé"],
         ["Le jour où le permis est arrivé…","dit lequel des jours"],
         ["Le 18 septembre, où l'inspection a eu lieu, …","ajoute un renseignement sur une date déjà nommée"],
       ]},

      {t:'piege', h:"Deux erreurs, une à l'oral, une à l'écrit",
       rows:[
         ["écrire « le jour que je suis arrivée »","écrire « le jour où »",
          "« Que » s'entend beaucoup et se dit sans problème entre amis. Dans un courriel à un entrepreneur, il se voit tout de suite."],
         ["oublier les virgules autour de l'ajout","les mettre des deux côtés, ou d'aucun",
          "« Le mur nord où la fissure a été relevée est le plus humide » se lit comme s'il y avait plusieurs murs nord. Une virgule d'un seul côté est toujours une erreur."],
       ]},

      {t:'check', h:"Trois questions",
       qs:[
         {q:"« Le jour ___ on a ouvert le plancher »", opts:["que","où"], ok:1,
          fb:"« Où » vaut aussi pour un moment."},
         {q:"« Où » peut remplacer…", opts:["seulement un lieu","un lieu ou un moment"], ok:1,
          fb:"Et l'emploi temporel est le plus fréquent à l'écrit."},
         {q:"Les virgules autour d'une relative en « où »…", opts:["se mettent des deux côtés ou d'aucun","se mettent au choix"], ok:0,
          fb:"Une seule virgule est toujours une erreur."},
       ]},

      {t:'revoir', h:"À retenir",
       p:"<b>« Où »</b> rattache un <b>lieu</b> — le mur où, le coin où — et un <b>moment</b> — le jour où, l'année où, le moment où. Jamais « le jour que ». Et les virgules vont par deux, ou pas du tout."},
    ]
  },

  t2subj: {
    eye:'Mini-leçon', tit:"La langue de la demande écrite",
    blocs:[
      {t:'texte', h:"Pourquoi ce temps-là et pas un autre",
       p:"« Ajoutez une phrase à la soumission » est un ordre. « J'aimerais que vous ajoutiez une phrase à la soumission » est une demande — ferme, polie, et impossible à prendre de travers. La différence tient au verbe qui suit « que », et ce verbe est au subjonctif. Ce n'est pas une politesse décorative : c'est la forme normale de la demande écrite en français.",
       note:"Le programme du niveau 6 y consacre cinq points, dont : employer obligatoirement le subjonctif présent après quelques verbes introducteurs usuels + que, et distinguer un verbe introducteur + de d'un verbe introducteur + que."},

      {t:'ana', h:"Les verbes qui l'imposent",
       p:"Après eux, quand « que » suit, le verbe suivant se met au subjonctif. Sans exception.",
       mots:[['la nécessité','il faut <b>que</b> · il est important <b>que</b> · il vaut mieux <b>que</b>'],
             ['la volonté','je veux <b>que</b> · j\'exige <b>que</b> · je demande <b>que</b>', true],
             ['le souhait','je souhaite <b>que</b> · j\'aimerais <b>que</b> · je préfère <b>que</b>'],
             ['le doute et l\'attente','je ne crois pas <b>que</b> · en attendant <b>que</b> · avant <b>que</b>']],
       say:"il faut que, je veux que, je souhaite que, avant que",
       note:"Les verbes d'opinion positifs ne le prennent pas : « je crois que le mur est sec », indicatif. À la forme négative, oui : « je ne crois pas que le mur soit sec »."},

      {t:'ana', h:"Sa forme, en une règle et cinq exceptions",
       p:"On part du « ils » du présent, on enlève -ent, on ajoute les terminaisons.",
       mots:[['la règle','ils sèch<s>ent</s> → que je <b>sèche</b> · ils finiss<s>ent</s> → que tu <b>finisses</b> · ils écriv<s>ent</s> → qu\'il <b>écrive</b>'],
             ['être et avoir','que je <b>sois</b> · que nous <b>soyons</b> · que j\'<b>aie</b> · que vous <b>ayez</b>', true],
             ['faire, aller, pouvoir','que je <b>fasse</b> · que j\'<b>aille</b> · que je <b>puisse</b>'],
             ['« nous » et « vous »','ils ressemblent à l\'imparfait : que nous <b>fassions</b>, que vous <b>écriviez</b>']],
       say:"que je sèche, que je sois, que j'aie, que je fasse, que je puisse",
       note:"Cinq irréguliers — être, avoir, faire, aller, pouvoir — et vous avez de quoi écrire une demande complète."},

      {t:'ana', h:"« de » + infinitif, ou « que » + subjonctif ?",
       p:"C'est la question qui décide, et elle est simple : est-ce la même personne des deux côtés ?",
       mots:[['même personne → de + infinitif','Je souhaite <b>recevoir</b> la soumission jeudi.'],
             ['personne différente → que + subjonctif','Je souhaite que vous m\'<b>envoyiez</b> la soumission jeudi.', true],
             ['même personne','Il faut <b>vérifier</b> la licence avant de signer.'],
             ['personne différente','Il faut que <b>vous</b> vérifiiez la licence avant de signer.']],
       say:"je souhaite recevoir, je souhaite que vous envoyiez",
       note:"« Je souhaite que je reçoive » ne se dit pas. Quand c'est vous des deux côtés, l'infinitif est obligatoire."},

      {t:'labo', h:"La même demande, deux registres",
       p:"Choisissez une demande, puis la façon de la formuler.",
       axes:[
         {id:'d', lbl:'Quelle demande ?', opts:[['a','écrire une phrase dans la soumission'],['b','envoyer les deux prix'],['c','attendre que le mur soit sec']]},
         {id:'f', lbl:'Comment ?', opts:[['1','à l\'impératif'],['2','au subjonctif']]}],
       out:{
         a1:{w:["Ajoutez cette phrase à la soumission."], say:"Ajoutez cette phrase à la soumission.", n:'court, clair — et sec, dans un courriel'},
         a2:{w:["J'aimerais que vous ajoutiez cette phrase à la soumission."], say:"J'aimerais que vous ajoutiez cette phrase à la soumission.", n:'la même demande, et elle passe partout'},
         b1:{w:["Envoyez-moi les deux prix aujourd'hui."], say:"Envoyez-moi les deux prix aujourd'hui.", n:'utile au téléphone, entre gens qui se connaissent'},
         b2:{w:["Je souhaite que vous m'envoyiez les deux prix aujourd'hui."], say:"Je souhaite que vous m'envoyiez les deux prix aujourd'hui.", n:'écrit, daté, et impossible à comprendre de travers'},
         c1:{w:["Ne refermez pas les cloisons avant que ce soit sec."], say:"Ne refermez pas les cloisons avant que ce soit sec.", n:'notez : « avant que » commande lui aussi le subjonctif'},
         c2:{w:["Il faut que le mur soit sec avant qu'on referme les cloisons."], say:"Il faut que le mur soit sec avant qu'on referme les cloisons.", n:'deux subjonctifs dans la même phrase, et c\'est correct'},
       },
       note:"L'impératif n'est pas interdit : il est seulement plus dur à l'écrit qu'à l'oral. Dans un courriel à quelqu'un que vous payez, le subjonctif tient mieux la relation."},

      {t:'ex', h:"Huit demandes du module",
       rows:[
         ["Il faut que le mur soit sec.","être"],
         ["J'aimerais que vous écriviez cette phrase.","écrire"],
         ["Kettly souhaite que Doïna ait une réserve.","avoir"],
         ["Le service des permis exige que le plan parte cette semaine.","partir"],
         ["Il est important que nous fassions vérifier la licence.","faire"],
         ["Fernand demande que Doïna réponde avant le 15.","répondre"],
         ["Je veux que tout imprévu fasse l'objet d'un avis écrit.","faire"],
         ["Il faudrait que vous puissiez commencer avant les pluies.","pouvoir"],
       ]},

      {t:'piege', h:"Trois erreurs fréquentes",
       rows:[
         ["« après que » au subjonctif","« après que » + indicatif",
          "« Avant que » commande le subjonctif ; « après que » ne le commande pas. On écrit « après qu'il a signé », pas « après qu'il ait signé » — même si presque tout le monde dit le contraire."],
         ["« je souhaite que je reçoive »","« je souhaite recevoir »",
          "Quand c'est la même personne des deux côtés, l'infinitif est obligatoire. La phrase avec « que » est simplement impossible."],
         ["« il faut que je vais »","« il faut que j'aille »",
          "Aller est l'un des cinq irréguliers. Que j'aille, que tu ailles, qu'il aille, que nous allions."],
       ]},

      {t:'check', h:"Quatre questions",
       qs:[
         {q:"« Il faut que le mur ___ sec. »", opts:["est","soit"], ok:1,
          fb:"Après « il faut que », le subjonctif est obligatoire."},
         {q:"« Je souhaite ___ la soumission jeudi. » (c'est moi qui la reçois)", opts:["recevoir","que je reçoive"], ok:0,
          fb:"Même personne des deux côtés : infinitif."},
         {q:"« Avant qu'il ___ » demande…", opts:["le subjonctif","l'indicatif"], ok:0,
          fb:"« Avant que » le commande ; « après que » non."},
         {q:"« Il faut que j'___ au bureau des permis. »", opts:["aille","vais"], ok:0,
          fb:"Aller : que j'aille."},
       ]},

      {t:'revoir', h:"À retenir",
       p:"Après <b>il faut que, je veux que, je souhaite que, j'aimerais que, j'exige que, avant que</b> : subjonctif, toujours. Cinq irréguliers à savoir — <b>sois, aie, fasse, aille, puisse</b>. Et quand c'est la même personne des deux côtés, on emploie l'infinitif."},
    ]
  },

  t2ps: {
    eye:'Mini-leçon', tit:"Le passé qu'on lit et qu'on n'entend jamais",
    blocs:[
      {t:'texte', h:"Trois lignes de rapport qui font sursauter",
       p:"« La résidence fut construite en 1961. Les propriétaires précédents refirent la toiture en 1998 et remplacèrent la fournaise en 2011. » Personne ne parle comme ça, et personne ne devrait essayer. C'est le temps des récits écrits : les contes, les romans, les livres d'histoire — et les sections « historique » des documents techniques, qui en héritent parce qu'elles recopient des archives.",
       note:"Le programme du niveau 6 est explicite sur ce que l'on doit en faire : reconnaître les verbes courants à la 3e personne, et associer le passé simple au passé composé. Rien de plus, et surtout pas l'écrire."},

      {t:'ana', h:"Comment on le reconnaît, sans l'apprendre",
       p:"Trois terminaisons couvrent presque tout ce que vous rencontrerez. Toutes à la 3e personne, parce qu'un récit écrit parle de quelqu'un d'autre.",
       mots:[['-a et -èrent (verbes en -er)','il coul<b>a</b> · ils remplac<b>èrent</b> · elle relev<b>a</b> · ils condamn<b>èrent</b>'],
             ['-it et -irent','il fin<b>it</b> · ils refi<b>rent</b> · elle part<b>it</b>', true],
             ['-ut et -urent','il f<b>ut</b> · ils e<b>urent</b> · elle p<b>ut</b>'],
             ['le repère infaillible','un verbe qui ressemble à un verbe connu, dans un texte écrit au passé, à la 3e personne']],
       say:"il coula, ils remplacèrent, il finit, il fut, ils eurent",
       note:"Vous n'avez jamais à le produire. Vous avez seulement à le traduire dans votre tête, en une fraction de seconde : c'est un passé composé."},

      {t:'ana', h:"La traduction, mot pour mot",
       p:"Toujours la même opération : passé simple à gauche, passé composé à droite.",
       mots:[['fut construite','a été construite'],
             ['refirent','ont refait', true],
             ['remplacèrent','ont remplacé'],
             ['ne fut consignée','n\'a pas été consignée']],
       say:"fut construite, a été construite, refirent, ont refait",
       note:"Le sens ne change pas d'un iota. Seul le registre change : l'un s'écrit, l'autre se dit."},

      {t:'labo', h:"Écrit, puis dit",
       p:"Choisissez une phrase du rapport, puis voyez comment on la dit.",
       axes:[
         {id:'p', lbl:'Quelle phrase ?', opts:[['a','la construction'],['b','la toiture'],['c','les archives']]},
         {id:'v', lbl:'Quelle version ?', opts:[['1','celle du rapport'],['2','celle qu\'on dit']]}],
       out:{
         a1:{w:["La résidence fut construite en 1961."], say:"La résidence fut construite en 1961.", n:'la phrase telle qu\'elle est écrite'},
         a2:{w:["La maison a été construite en 1961."], say:"La maison a été construite en 1961.", n:'la même chose, au téléphone'},
         b1:{w:["Les propriétaires précédents refirent la toiture en 1998."], say:"Les propriétaires précédents refirent la toiture en 1998.", n:'refirent : passé simple de refaire, 3e personne du pluriel'},
         b2:{w:["Les anciens propriétaires ont refait la toiture en 1998."], say:"Les anciens propriétaires ont refait la toiture en 1998.", n:'et « précédents » devient « anciens » : le registre suit'},
         c1:{w:["Aucune autre intervention majeure ne fut consignée."], say:"Aucune autre intervention majeure ne fut consignée.", n:'fut consignée : passé simple passif'},
         c2:{w:["On n'a rien noté d'autre d'important."], say:"On n'a rien noté d'autre d'important.", n:'la phrase entière change de registre, pas seulement le verbe'},
       },
       note:"Le troisième couple montre l'essentiel : ce n'est pas seulement le temps du verbe qui change, c'est toute la phrase. Le passé simple ne voyage jamais seul."},

      {t:'ex', h:"Huit formes du rapport",
       p:"À gauche ce qui est écrit, à droite ce que vous diriez.",
       rows:[
         ["la résidence fut construite","la résidence a été construite"],
         ["les propriétaires refirent la toiture","les propriétaires ont refait la toiture"],
         ["ils remplacèrent la fournaise","ils ont remplacé la fournaise"],
         ["aucune intervention ne fut consignée","aucune intervention n'a été consignée"],
         ["l'inspectrice releva une fissure","l'inspectrice a relevé une fissure"],
         ["le sol se tassa peu à peu","le sol s'est tassé peu à peu"],
         ["quelqu'un condamna le puisard","quelqu'un a condamné le puisard"],
         ["elle eut le rapport en main","elle a eu le rapport en main"],
       ]},

      {t:'piege', h:"Deux erreurs, dont une qu'on vous a peut-être enseignée",
       rows:[
         ["essayer de l'employer","le laisser aux textes écrits",
          "Un passé simple dans un courriel à un entrepreneur ne fait pas savant : il fait bizarre. Le programme demande de le reconnaître, jamais de le produire, et c'est une bonne nouvelle."],
         ["confondre « il fut » et « il fit »","regarder la voyelle",
          "« Il fut » vient d'être ; « il fit » vient de faire. Une lettre, deux verbes très fréquents. « La maison fut construite » — être. « Il fit poser une membrane » — faire."],
       ]},

      {t:'check', h:"Trois questions",
       qs:[
         {q:"« Ils refirent la toiture » se dit…", opts:["ils ont refait la toiture","ils refaisaient la toiture"], ok:0,
          fb:"Le passé simple se traduit toujours par un passé composé."},
         {q:"Le programme demande de…", opts:["écrire le passé simple","le reconnaître et le traduire"], ok:1,
          fb:"Reconnaître les verbes courants à la 3e personne, et rien de plus."},
         {q:"« Il fut » vient du verbe…", opts:["être","faire"], ok:0,
          fb:"« Il fit » viendrait de faire."},
       ]},

      {t:'revoir', h:"À retenir",
       p:"Le passé simple se <b>lit</b> et ne se <b>dit</b> pas. Trois familles de terminaisons — <b>-a / -èrent</b>, <b>-it / -irent</b>, <b>-ut / -urent</b> —, presque toujours à la 3e personne. Et une seule opération à faire : le traduire en passé composé."},
    ]
  },

  t3si: {
    eye:'Mini-leçon', tit:"Poser une condition, et obtenir une réponse",
    blocs:[
      {t:'texte', h:"Une décision de chantier se prend en hypothèses",
       p:"Au sous-sol, le 8 avril, personne ne sait ce qui va se passer. Deux solutions, deux prix, deux délais, un permis qui prendra le temps qu'il prendra, et une pluie que personne ne contrôle. Doïna ne peut pas demander « ce sera prêt le 12 mai ? ». Elle doit demander « si le permis sort dans dix jours, est-ce que ce sera prêt ? ». C'est une autre question, et c'est la seule à laquelle un homme de métier honnête peut répondre.",
       note:"Le programme du niveau 6 demande d'exprimer la condition dans une hypothèse avec le marqueur « si », et d'employer l'indicatif présent après « si » dans les hypothèses réalistes."},

      {t:'ana', h:"La forme, et la seule règle à retenir",
       p:"Deux moitiés séparées par une virgule. Ce qui se passe après « si » n'est jamais ce qu'on croit.",
       mots:[['après si → le présent','<b>Si</b> le permis <b>sort</b> dans dix jours, …'],
             ['après la virgule → le futur','…, le sous-sol <b>sera</b> prêt le 12 mai.', true],
             ['ou le présent','<b>Si</b> l\'eau <b>revient</b>, vous <b>refaites</b> tout.'],
             ['ou l\'impératif','<b>Si</b> le mur n\'<b>est</b> pas sec, <b>ne refermez pas</b> les cloisons.']],
       say:"si le permis sort, le sous-sol sera prêt",
       note:"La règle tient en cinq mots : jamais de futur après « si ». Le futur va de l'autre côté de la virgule, et seulement là."},

      {t:'ana', h:"L'hypothèse sur un fait passé",
       p:"Quand la condition porte sur quelque chose de déjà arrivé, « si » est suivi du passé composé — et la suite reste au présent.",
       mots:[['un fait passé','<b>Si</b> quelqu\'un <b>a condamné</b> le puisard avant nous, ce n\'<b>est</b> pas notre faute.'],
             ['un fait qu\'on découvre','<b>S\'ils ont coulé</b> la dalle sans membrane, ça <b>explique</b> tout.', true],
             ['la suite reste au présent','…, alors la soumission ne <b>couvre</b> pas ces travaux.'],
             ['le mot « alors » est facultatif','on l\'ajoute pour marquer la conséquence à l\'oral']],
       say:"si quelqu'un a condamné le puisard, ce n'est pas notre faute",
       note:"Cette forme-là est celle des désaccords de chantier : elle sert à établir qui répond de quoi, sans accuser personne."},

      {t:'labo', h:"La même situation, trois conditions",
       p:"Choisissez la condition, puis la suite.",
       axes:[
         {id:'c', lbl:'Quelle condition ?', opts:[['p','le permis sort à temps'],['e','l\'eau revient un jour'],['m','le mur n\'est pas sec']]},
         {id:'s', lbl:'Quelle suite ?', opts:[['1','au futur'],['2','au présent ou à l\'impératif']]}],
       out:{
         p1:{w:["Si le permis sort dans dix jours, le sous-sol sera prêt le 12 mai."], say:"Si le permis sort dans dix jours, le sous-sol sera prêt le 12 mai.", n:'la question exacte que Doïna pose à Fernand'},
         p2:{w:["Si le permis sort dans dix jours, on commence tout de suite."], say:"Si le permis sort dans dix jours, on commence tout de suite.", n:'le présent vaut aussi pour l\'avenir proche'},
         e1:{w:["Si l'eau revient, vous referez tout le plancher."], say:"Si l'eau revient, vous referez tout le plancher.", n:'futur après la virgule : c\'est l\'avertissement de Kettly'},
         e2:{w:["Si l'eau revient, appelez-moi avant de casser quoi que ce soit."], say:"Si l'eau revient, appelez-moi avant de casser quoi que ce soit.", n:'impératif : la condition devient une consigne'},
         m1:{w:["Si le mur n'est pas sec, la moisissure poussera derrière le gypse."], say:"Si le mur n'est pas sec, la moisissure poussera derrière le gypse.", n:'futur : on annonce une conséquence certaine'},
         m2:{w:["Si le mur n'est pas sec, ne refermez pas les cloisons."], say:"Si le mur n'est pas sec, ne refermez pas les cloisons.", n:'impératif : la phrase la plus utile des trois'},
       },
       note:"Les trois suites sont correctes. Le futur annonce, le présent constate, l'impératif ordonne — et sur un chantier, c'est l'impératif qui empêche les erreurs."},

      {t:'ex', h:"Six hypothèses du Défi 3",
       rows:[
         ["Si le permis sort dans dix jours,","le sous-sol sera prêt le 12 mai."],
         ["Si vous choisissez le plancher flottant,","on commence lundi."],
         ["Si l'eau revient un jour,","vous referez tout."],
         ["S'il pleut trois semaines de suite,","l'échéancier saute."],
         ["Si je ne signe pas avant le 15,","la soumission ne sera plus valide."],
         ["Si quelqu'un a condamné le puisard avant nous,","ce n'est pas dans le prix."],
       ]},

      {t:'piege', h:"Deux pièges, dont le plus fréquent de tout le niveau",
       rows:[
         ["« si le permis sortira »","« si le permis sort »",
          "Jamais de futur juste après « si ». C'est la faute la plus fréquente, à tous les niveaux, et c'est aussi la plus facile à corriger : le futur va après la virgule."],
         ["confondre « si » de condition et « si » de question","regarder s'il y a une virgule et une suite",
          "« Je ne sais pas si le permis sortira » n'est pas une condition : c'est une question rapportée, et là le futur est correct. La condition, elle, a toujours deux moitiés."],
       ]},

      {t:'check', h:"Quatre questions",
       qs:[
         {q:"« Si le permis ___ dans dix jours… »", opts:["sortira","sort"], ok:1,
          fb:"Jamais de futur juste après « si »."},
         {q:"Après la virgule, on peut mettre…", opts:["seulement le futur","le futur, le présent ou l'impératif"], ok:1,
          fb:"Les trois sont corrects, et ils ne disent pas la même chose."},
         {q:"« Si quelqu'un a condamné le puisard » : après « si », c'est…", opts:["un passé composé","un futur"], ok:0,
          fb:"L'hypothèse porte sur un fait déjà arrivé."},
         {q:"« Je ne sais pas si le permis sortira » est…", opts:["une condition","une question rapportée"], ok:1,
          fb:"Pas de virgule, pas de deuxième moitié : ce n'est pas une hypothèse."},
       ]},

      {t:'revoir', h:"À retenir",
       p:"Deux moitiés, une virgule. Après <b>si</b> : le <b>présent</b> — ou le passé composé si le fait est déjà arrivé. Après la virgule : le <b>futur</b>, le <b>présent</b> ou l'<b>impératif</b>. Et jamais, jamais de futur juste après « si »."},
    ]
  },

  t3quest: {
    eye:'Mini-leçon', tit:"La question qui obtient une réponse",
    blocs:[
      {t:'texte', h:"Pourquoi « c'est long ? » ne sert à rien",
       p:"« C'est long, vos travaux ? » — « Ça dépend. » Personne n'a menti : la question ne demandait rien de précis, la réponse n'a rien donné de précis. « Combien de jours ouvrables entre l'injection et la pose du gypse ? » obtient un nombre, tout de suite, et ce nombre s'écrit. Une bonne question de chantier contient toujours un chiffre, une date ou un document.",
       note:"C'est la seconde moitié de l'intention du programme : comprendre de l'information ET poser des questions reliées à des travaux de réparation ou de rénovation. La première moitié se travaillait au Défi 1 ; celle-ci se travaille ici."},

      {t:'ana', h:"« quel » devant un nom : la question qui force un choix",
       p:"Il oblige l'autre à nommer une chose précise, et il rend « ça dépend » très difficile à dire.",
       mots:[['quel + nom masculin','<b>Quel</b> délai dois-je prévoir pour le permis ?'],
             ['quelle + nom féminin','<b>Quelle</b> garantie donnez-vous sur l\'injection ?', true],
             ['quels, quelles au pluriel','<b>Quels</b> travaux ne sont pas compris ? · <b>Quelles</b> sont les exclusions ?'],
             ['avec une préposition','À <b>quelle</b> date commencez-vous ? · De <b>quel</b> montant parle-t-on ?']],
       say:"quel délai, quelle garantie, quels travaux, à quelle date",
       note:"Il s'accorde avec le nom qui le suit, pas avec vous. « Quelle garantie » parce que garantie est féminin."},

      {t:'ana', h:"La question indirecte : plus douce, et aussi précise",
       p:"On la loge derrière « je voudrais savoir », « j'aimerais savoir », « dites-moi ». Elle passe mieux au téléphone.",
       mots:[['avec un infinitif','Je voudrais savoir <b>quoi faire</b> si l\'eau revient.'],
             ['avec un mot interrogatif','J\'aimerais savoir <b>quand payer</b> et <b>où signer</b>.', true],
             ['avec « à qui »','Je ne sais pas <b>à qui m\'adresser</b> pour le permis.'],
             ['sans point d\'interrogation','« Je voudrais savoir quand payer. » — c\'est une phrase déclarative.']],
       say:"je voudrais savoir quoi faire, j'aimerais savoir quand payer",
       note:"Pas d'inversion et pas de point d'interrogation : « je voudrais savoir quand vous commencez », et non « quand commencez-vous »."},

      {t:'labo', h:"De la question vague à la question précise",
       p:"Choisissez la question vague, puis sa version qui obtient une réponse.",
       axes:[
         {id:'v', lbl:'Quelle question vague ?', opts:[['a','« C\'est long ? »'],['b','« Il y a une garantie ? »'],['c','« Ça va coûter plus cher ? »']]},
         {id:'f', lbl:'Quelle forme ?', opts:[['1','directe, avec quel'],['2','indirecte, avec savoir']]}],
       out:{
         a1:{w:["Quel délai en jours ouvrables entre l'injection et la pose du gypse ?"], say:"Quel délai en jours ouvrables entre l'injection et la pose du gypse ?", n:'un chiffre est demandé, un chiffre sera donné'},
         a2:{w:["Je voudrais savoir combien de jours ouvrables séparent les deux étapes."], say:"Je voudrais savoir combien de jours ouvrables séparent les deux étapes.", n:'même précision, ton plus doux'},
         b1:{w:["Quelle garantie donnez-vous sur l'injection, et pour combien de temps ?"], say:"Quelle garantie donnez-vous sur l'injection, et pour combien de temps ?", n:'deux questions en une : la nature et la durée'},
         b2:{w:["J'aimerais savoir quelle garantie s'applique à l'injection."], say:"J'aimerais savoir quelle garantie s'applique à l'injection.", n:'« quelle » fonctionne aussi dans une question indirecte'},
         c1:{w:["Quel montant s'ajoute au total si vous trouvez un imprévu ?"], say:"Quel montant s'ajoute au total si vous trouvez un imprévu ?", n:'la question et l\'hypothèse dans la même phrase'},
         c2:{w:["Je voudrais savoir quoi faire si vous trouvez autre chose."], say:"Je voudrais savoir quoi faire si vous trouvez autre chose.", n:'infinitif après « savoir » : la forme la plus courte'},
       },
       note:"Les deux formes valent. La directe va plus vite en réunion ; l'indirecte passe mieux au téléphone et par écrit."},

      {t:'ex', h:"Les cinq questions à poser avant de signer",
       p:"Elles tiennent en trente secondes, et elles se posent dans cet ordre.",
       rows:[
         ["1","Quel est le prix total, taxes comprises ?"],
         ["2","Quels travaux ne sont pas compris ?"],
         ["3","Quel est le délai, séchage compris ?"],
         ["4","Qu'arrive-t-il si vous trouvez une condition non visible ?"],
         ["5","Quelle garantie, sur quoi, et pendant combien de temps — par écrit ?"],
       ]},

      {t:'piege', h:"Trois façons de perdre de l'information",
       rows:[
         ["poser une question fermée","la poser avec « quel » ou « combien »",
          "« Il y a une garantie ? » se répond par oui. « Quelle garantie, et pendant combien de temps ? » se répond par une phrase. La différence est dans le premier mot."],
         ["faire semblant de connaître un mot","demander ce qu'il veut dire",
          "« Qu'est-ce que ça veut dire, reprofiler ? » Personne n'a jamais perdu d'argent en posant cette question. Beaucoup en ont perdu en hochant la tête."],
         ["poser cinq questions d'un coup","les poser une à la fois",
          "« Allez-y. Une à la fois, s'il vous plaît. » C'est la phrase de Doïna au Défi 3, et c'est la bonne : une question posée seule obtient une réponse complète."],
       ]},

      {t:'check', h:"Trois questions",
       qs:[
         {q:"« ___ garantie donnez-vous ? »", opts:["Quel","Quelle"], ok:1,
          fb:"Garantie est féminin, donc « quelle »."},
         {q:"« Je voudrais savoir quand vous commencez » prend-il un point d'interrogation ?", opts:["oui","non"], ok:1,
          fb:"C'est une question indirecte : phrase déclarative, point final."},
         {q:"Une bonne question de chantier contient…", opts:["un chiffre, une date ou un document","le mot s'il vous plaît"], ok:0,
          fb:"C'est ce qui empêche la réponse « ça dépend »."},
       ]},

      {t:'revoir', h:"À retenir",
       p:"<b>Quel, quelle, quels, quelles</b> devant un nom force une réponse précise. <b>Je voudrais savoir + mot interrogatif</b> fait la même chose, plus doucement, et sans point d'interrogation. Et une bonne question porte toujours sur un <b>chiffre</b>, une <b>date</b> ou un <b>document</b>."},
    ]
  },

  t3conn: {
    eye:'Mini-leçon', tit:"Prévenir qu'on va donner un exemple, ou un avis",
    blocs:[
      {t:'texte', h:"Deux petits mots qui changent le statut de ce qui suit",
       p:"« La peinture n'est pas comprise. Ça vaut la peine de la faire soi-même. » Deux phrases collées, et celui qui écoute ne sait pas laquelle est un fait et laquelle est une opinion. Ajoutez trois mots : « D'après la soumission, la peinture n'est pas comprise ; à mon avis, ça vaut la peine de la faire soi-même. » Rien n'a changé sauf le statut de chaque phrase — et c'est tout ce qui compte devant quelqu'un que vous payez.",
       note:"Le programme du niveau 6 demande d'employer des connecteurs de points de vue courants et des connecteurs d'exemplification et d'illustration courants. Les deux familles vont ensemble parce qu'elles font le même travail : elles annoncent."},

      {t:'ana', h:"Annoncer un exemple",
       p:"Ils préviennent : ce qui suit n'est pas une idée nouvelle, c'est la même idée, en plus concret.",
       mots:[['les plus courants','<b>par exemple</b> · <b>notamment</b> · <b>entre autres</b>'],
             ['les plus soutenus','<b>ainsi</b> · <b>c\'est le cas de</b> · <b>tel que</b>', true],
             ['à l\'oral','<b>prenons</b> · <b>mettons</b> · <b>disons</b> · <b>comme</b>'],
             ['dans un texte','ils se mettent en tête de phrase, suivis d\'une virgule']],
       say:"par exemple, notamment, entre autres, ainsi",
       note:"« Notamment » ne veut pas dire « surtout ». Il veut dire « entre autres choses » : il annonce un élément d'une liste plus longue, pas le plus important."},

      {t:'ana', h:"Annoncer un point de vue",
       p:"Ils préviennent : ce qui suit n'est pas un fait, c'est quelqu'un qui parle.",
       mots:[['le mien','<b>à mon avis</b> · <b>selon moi</b> · <b>personnellement</b> · <b>quant à moi</b>'],
             ['celui d\'un autre','<b>d\'après l\'inspectrice</b> · <b>selon Fernand</b> · <b>pour la Ville</b>', true],
             ['celui d\'un document','<b>d\'après la soumission</b> · <b>selon le rapport</b> · <b>aux termes du contrat</b>'],
             ['prudent','<b>il me semble que</b> · <b>si je comprends bien</b> · <b>si vous voulez mon avis</b>']],
       say:"à mon avis, selon moi, d'après le rapport, il me semble que",
       note:"« Selon » et « d'après » servent aux deux : selon moi, selon le rapport. C'est le mot qui suit qui dit si l'avis est le vôtre ou celui d'un autre."},

      {t:'labo', h:"Un fait, une opinion, et ce qui les sépare",
       p:"Choisissez le sujet, puis ce que vous voulez marquer.",
       axes:[
         {id:'s', lbl:'Quel sujet ?', opts:[['a','les exclusions'],['b','le séchage'],['c','les deux solutions']]},
         {id:'t', lbl:'Quoi marquer ?', opts:[['1','un fait, avec sa source'],['2','une opinion, avec la mienne']]}],
       out:{
         a1:{w:["D'après la soumission, le permis et la peinture ne sont pas compris."], say:"D'après la soumission, le permis et la peinture ne sont pas compris.", n:'la source est nommée : personne ne peut me la reprocher'},
         a2:{w:["À mon avis, la peinture vaut la peine d'être faite par nous."], say:"À mon avis, la peinture vaut la peine d'être faite par nous.", n:'c\'est une opinion, et elle est annoncée comme telle'},
         b1:{w:["Selon le rapport, le taux d'humidité est de dix-neuf pour cent."], say:"Selon le rapport, le taux d'humidité est de dix-neuf pour cent.", n:'un chiffre, et le papier d\'où il vient'},
         b2:{w:["Personnellement, je préfère attendre une semaine de plus."], say:"Personnellement, je préfère attendre une semaine de plus.", n:'la préférence est nommée, elle ne se déguise pas en fait'},
         c1:{w:["D'après Fernand, la première solution demande neuf jours ouvrables de plus."], say:"D'après Fernand, la première solution demande neuf jours ouvrables de plus.", n:'un délai attribué à celui qui l\'a annoncé'},
         c2:{w:["Quant à moi, je ne veux pas payer deux fois."], say:"Quant à moi, je ne veux pas payer deux fois.", n:'la phrase qui a décidé de tout le Défi 3'},
       },
       note:"Refaites le laboratoire à voix haute en marquant un petit silence après le connecteur. C'est ce silence qui fait comprendre que la suite change de nature."},

      {t:'ex', h:"Le même contenu, deux statuts",
       rows:[
         ["Plusieurs postes sont exclus, notamment le permis.","un fait, avec un exemple"],
         ["À mon avis, la première solution est la plus sûre.","une opinion, annoncée"],
         ["D'après le rapport, l'humidité est de dix-neuf pour cent.","un fait, avec sa source"],
         ["Ainsi, la dalle n'a pas été vérifiée par en dessous.","un exemple de ce qui précède"],
         ["Quant à moi, je ne signerais rien sans les deux prix.","une opinion, prudente"],
         ["Il reste des questions, notamment le délai du permis.","un fait, avec un exemple"],
       ]},

      {t:'piege', h:"Deux erreurs de conversation",
       rows:[
         ["enchaîner un fait et une opinion sans rien entre les deux","annoncer la seconde",
          "Celui qui vous écoute prend alors votre opinion pour un fait, et il vous la ressort la semaine suivante comme si vous l'aviez lue quelque part."],
         ["employer « notamment » pour dire « surtout »","employer « surtout »",
          "« Notamment » annonce un élément parmi d'autres. Si vous voulez dire que c'est le plus important, dites « surtout » ou « en particulier »."],
       ]},

      {t:'check', h:"Trois questions",
       qs:[
         {q:"« Notamment » annonce…", opts:["le plus important","un élément parmi d'autres"], ok:1,
          fb:"Pour le plus important, on dit « surtout »."},
         {q:"« D'après le rapport » annonce…", opts:["un fait avec sa source","une opinion personnelle"], ok:0,
          fb:"La source est nommée, donc ce n'est pas vous qui l'affirmez."},
         {q:"Le connecteur se place…", opts:["en tête de phrase, suivi d'une virgule","à la fin de la phrase"], ok:0,
          fb:"Il annonce : il doit donc venir avant."},
       ]},

      {t:'revoir', h:"À retenir",
       p:"Deux familles, et elles annoncent toutes les deux. <b>Par exemple, notamment, entre autres, ainsi</b> : ce qui suit est un exemple. <b>À mon avis, selon moi, d'après le rapport, il me semble que</b> : ce qui suit est un point de vue. Devant quelqu'un que vous payez, séparer les deux vaut de l'argent."},
    ]
  },

  t3courriel: {
    eye:'Mini-leçon', tit:"Mettre par écrit ce qui n'a été dit que de vive voix",
    blocs:[
      {t:'texte', h:"Le courriel du soir, après la réunion",
       p:"Le 8 avril, quatre personnes ont parlé pendant quarante minutes au sous-sol. Le soir, il en reste ce que chacun a retenu — et ce n'est pas la même chose chez les quatre. Un courriel de dix lignes écrit le soir même règle ça pour de bon : il redit ce qui a été dit, il demande ce qui manque, et il porte une date. Ce n'est pas de la méfiance : c'est ce qui permet à tout le monde de travailler.",
       note:"La situation du programme n'a aucune intention de production écrite. Celle-ci vient des attentes de fin de cours du niveau 6 : « dans ses relations professionnelles, il rédige un courriel ou une lettre en respectant les conventions habituelles » et « il rédige un court texte en organisant ses idées à l'aide de paragraphes »."},

      {t:'ana', h:"Les six morceaux, et le travail de chacun",
       p:"Chacun fait une chose, et une seule. Un courriel dont un morceau manque se lit deux fois.",
       mots:[['l\'objet','assez précis pour qu\'on sache de quoi il s\'agit sans ouvrir : « Imprévu du 8 avril — confirmation des deux options »'],
             ['la formule d\'appel','elle nomme la personne : « Bonjour Monsieur Trudelle, »', true],
             ['le rappel','d\'où l\'on part, en une phrase, dès la première ligne'],
             ['ce qu\'on a compris','redit dans ses mots, pour que l\'autre puisse corriger'],
             ['la demande','une chose, claire, avec un délai'],
             ['la signature','le nom, et à quel titre on écrit']],
       say:"l'objet, la formule d'appel, le rappel, ce qu'on a compris, la demande, la signature",
       note:"L'ordre compte : le rappel avant ce qu'on a compris, et la demande après. Un courriel qui commence par la demande se lit comme une mise en demeure."},

      {t:'ana', h:"Trois paragraphes, une idée par paragraphe",
       p:"C'est ce que les attentes de fin de cours appellent organiser ses idées à l'aide de paragraphes. Sur un écran, ça se voit avant même qu'on lise.",
       mots:[['premier paragraphe','pourquoi j\'écris, et de quelle rencontre je parle'],
             ['deuxième paragraphe','ce que j\'ai compris : les deux solutions, les deux prix, les deux délais', true],
             ['troisième paragraphe','ce que je demande, et pour quand'],
             ['entre les deux','une ligne vide, pas un alinéa : c\'est l\'usage du courriel']],
       say:"pourquoi j'écris, ce que j'ai compris, ce que je demande",
       note:"Trois paragraphes de trois ou quatre phrases valent mieux qu'un bloc de douze. Le bloc ne se lit pas : il se survole, et la demande se perd au milieu."},

      {t:'labo', h:"La même phrase, deux façons de l'écrire",
       p:"Choisissez le morceau, puis la version.",
       axes:[
         {id:'m', lbl:'Quel morceau ?', opts:[['o','l\'objet'],['c','ce qu\'on a compris'],['d','la demande']]},
         {id:'v', lbl:'Quelle version ?', opts:[['1','à éviter'],['2','à écrire']]}],
       out:{
         o1:{w:["Objet : question"], say:"Objet : question", n:'ne dit rien ; le message sera ouvert en dernier'},
         o2:{w:["Objet : imprévu du 8 avril — confirmation des deux options"], say:"Objet : imprévu du 8 avril — confirmation des deux options", n:'une date, un sujet, et pas une phrase complète'},
         c1:{w:["Vous m'avez dit qu'il y avait un problème."], say:"Vous m'avez dit qu'il y avait un problème.", n:'trop vague pour que l\'autre puisse corriger'},
         c2:{w:["Vous m'avez présenté deux solutions : casser la dalle, 6 800 $ et neuf jours, ou poser un plancher flottant, 1 900 $ et deux jours."], say:"Vous m'avez présenté deux solutions : casser la dalle, six mille huit cents dollars et neuf jours, ou poser un plancher flottant, mille neuf cents dollars et deux jours.", n:'chiffré : s\'il y a une erreur, elle se voit tout de suite'},
         d1:{w:["Pourriez-vous me revenir là-dessus quand vous pourrez ?"], say:"Pourriez-vous me revenir là-dessus quand vous pourrez ?", n:'aucune date : la demande dormira'},
         d2:{w:["J'aimerais que vous m'écriviez les deux prix et les deux délais aujourd'hui."], say:"J'aimerais que vous m'écriviez les deux prix et les deux délais aujourd'hui.", n:'un subjonctif, une chose demandée, une date'},
       },
       note:"Les trois versions de droite ont un point commun : elles contiennent un chiffre ou une date. C'est ce qui distingue un courriel qui obtient une réponse d'un courriel qu'on lit et qu'on referme."},

      {t:'ex', h:"Le courriel de Doïna, morceau par morceau",
       rows:[
         ["Objet : imprévu du 8 avril — confirmation des deux options","dire le sujet sans qu'on ait à ouvrir"],
         ["Bonjour Monsieur Trudelle,","nommer la personne"],
         ["Je vous écris à la suite de notre rencontre d'hier, au sous-sol.","dire d'où l'on part"],
         ["Vous m'avez présenté deux solutions : …","redire ce qu'on a compris, avec les chiffres"],
         ["J'aimerais que vous m'écriviez les deux prix aujourd'hui.","demander une chose, avec un délai"],
         ["Doïna Petrescu, propriétaire, rue des Mésanges","se nommer, et dire à quel titre"],
       ]},

      {t:'piege', h:"Trois courriels qui n'obtiennent rien",
       rows:[
         ["mettre trois demandes dans un seul message","n'en mettre qu'une",
          "Trois demandes obtiennent au mieux une réponse. Écrivez deux courriels, ou numérotez les demandes 1, 2, 3 — mais ne les mêlez pas dans une phrase."],
         ["écrire un seul bloc de douze phrases","faire trois paragraphes",
          "Un bloc ne se lit pas, il se survole, et c'est toujours la demande qui se perd. Une ligne vide entre les paragraphes coûte une seconde et change tout."],
         ["écrire « quand vous pourrez »","écrire une date",
          "« Quand vous pourrez » veut dire jamais. « Aujourd'hui », « avant vendredi », « d'ici le 15 » se répondent — ou se refusent, ce qui est déjà un renseignement."],
       ]},

      {t:'check', h:"Trois questions",
       qs:[
         {q:"Un bon objet de courriel est…", opts:["une phrase complète","un groupe de mots précis"], ok:1,
          fb:"« Imprévu du 8 avril — confirmation des deux options »."},
         {q:"Combien de demandes par courriel ?", opts:["une","autant qu'on veut"], ok:0,
          fb:"Trois demandes obtiennent au mieux une réponse."},
         {q:"Entre deux paragraphes de courriel, on met…", opts:["un alinéa","une ligne vide"], ok:1,
          fb:"C'est l'usage du courriel, et ça se voit avant qu'on lise."},
       ]},

      {t:'revoir', h:"À retenir",
       p:"Six morceaux — <b>objet, appel, rappel, ce qu'on a compris, demande, signature</b> — et trois paragraphes, une idée chacun. Une seule demande, et toujours une <b>date</b>. Écrire le soir même ce qui a été dit dans la journée n'est pas de la méfiance : c'est ce qui permet de travailler."},
    ]
  },
};
