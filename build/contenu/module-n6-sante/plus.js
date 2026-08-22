const PLUS = {
  // Dix-sept mini-leçons. La clé d'une mini-leçon est l'`id` de l'exercice
  // qu'elle explique : c'est ce qui permet au bandeau d'aide de proposer la
  // bonne leçon après plusieurs erreurs. Une clé qui ne correspond à aucun
  // exercice n'est jamais atteignable.
  //
  // Tout bloc `ana` porte son champ `say:` — sans lui, l'extrait audio lit
  // les balises HTML à voix haute, et ça ne se découvre qu'une fois les MP3
  // payés. Même chose pour chaque sortie de laboratoire.
  //
  // Aucune de ces leçons ne donne de conseil de santé. Celles qui touchent au
  // vocabulaire médical expliquent ce qu'un mot veut dire dans une phrase,
  // jamais ce qu'il faudrait faire si on l'entend.

  prGraphie: {
    eye:'Mini-leçon', tit:"Le mot qu'on a entendu et qu'on ne retrouve pas",
    blocs:[
      {t:'texte', h:"Un corridor, un mot, et rien dans le dictionnaire",
       p:"Quelqu'un vous dit « é-co-gra-fie » entre deux portes. Vous rentrez chez vous, vous l'écrivez comme il sonnait, vous le cherchez : rien. Le mot existe pourtant, et il est même courant — il ne s'écrit simplement pas comme il se dit. Cela n'arrive que dans trois familles de mots, et les mots de la santé sont dedans, parce qu'ils viennent presque tous du grec ancien.",
       note:"Ce savoir est celui du niveau 6 pour les huit modules du cours : associer des phonèmes à des graphèmes inhabituels. Ici, on l'apprend sur les mots qu'on entend dans un hôpital."},

      {t:'ana', h:"Quand la bouche dit k et que la page écrit ch",
       p:"C'est la famille la plus utile des trois, parce que c'est celle des noms d'examens, de spécialités et d'analyses. Ces mots sont longs, ils ont l'air savants, et ils voisinent souvent un y ou un ph.",
       mots:[['Sur le papier','une é{ch}ographie · {ch}ronique · un psy{ch}iatre · le {ch}olestérol'],
             ["À l'oreille",'un k net et sec, celui de « carte » ou de « clinique »', true],
             ['Le signe qui ne trompe presque jamais',"un mot de science : essayez le k avant tout le reste"]],
       say:"une échographie, chronique, un psychiatre, le cholestérol",
       note:"Cela ne concerne pas « chercher », « chaque », « chambre » ni « chaise ». La famille savante tient sur une carte, et une fois apprise elle ne se rediscute plus."},

      {t:'ana', h:"Quand la bouche dit s et que la page écrit x",
       p:"Trois nombres, pas un de plus. Mais ce sont trois nombres qu'un secrétariat vous dira quinze fois : un étage, un poste téléphonique, un nombre de semaines avant le rappel.",
       mots:[['Sur le papier','si{x} · di{x} · soi{x}ante-dix'],
             ["À l'oreille",'un s franc, celui de la fin d'+"'"+'« autobus »', true],
             ["Ce qui bouge à la fin",'seul, le s s'+"'"+'entend ; devant une consonne, il tombe ; devant une voyelle, il devient z']],
       say:"six, dix, soixante-dix",
       note:"Essayez avec un vrai délai : « dans six », puis « six semaines », puis « six ans ». Le mot ne change pas ; c'est sa fin qui s'adapte à ce qui suit."},

      {t:'ana', h:"Quand la bouche dit ch et que la page écrit sh ou sch",
       p:"Trois mots venus d'ailleurs et installés ici depuis longtemps. Ils sont brefs, et rien dans leur orthographe ne prévient de la façon dont ils se prononcent.",
       mots:[['Sur le papier','un {sch}éma · un {sh}ampoing · un {sh}ort'],
             ["À l'oreille",'le même souffle que « chat », sans aucun k', true],
             ['Où vous les croiserez ici',"le schéma des étages du feuillet, le shampoing sur une liste de produits, le short demandé pour un examen à l'effort"]],
       say:"un schéma, un shampoing, un short",
       note:"Gardez surtout « un schéma » : c'est le dessin qui explique un parcours de trois paragraphes en un coup d'œil, et il figure sur presque tous les feuillets."},

      {t:'labo', h:"Une famille, un exemple, deux écoutes",
       p:"Prenez une famille, puis l'un de ses deux exemples.",
       axes:[
         {id:'c', lbl:'Quelle famille ?', opts:[['a','la page écrit ch, la bouche dit k'],['b','la page écrit x, la bouche dit s'],['c','la page écrit sh ou sch, la bouche dit ch']]},
         {id:'n', lbl:'Quel exemple ?', opts:[['1','le premier'],['2','le second']]}],
       out:{
         a1:{w:["une échographie"], say:"une échographie", n:'cinq syllabes, et le k arrive dès la deuxième'},
         a2:{w:["un psychiatre"], say:"un psychiatre", n:'psi-kiatre : deux consonnes silencieuses, puis un k'},
         b1:{w:["six"], say:"six", n:'tout seul, le mot finit sur un s parfaitement audible'},
         b2:{w:["soixante-dix"], say:"soixante-dix", n:'deux x dans le même mot, et deux fois le même s'},
         c1:{w:["un schéma"], say:"un schéma", n:'trois lettres à la file, un seul souffle en sortie'},
         c2:{w:["un short"], say:"un short", n:'le mot a voyagé, la prononciation reste française'},
       },
       note:"Écoutez deux fois avant d'ouvrir la bouche. Ce qui se travaille ici est l'oreille ; la langue suit toute seule quelques jours plus tard."},

      {t:'ex', h:"Huit mots d'hôpital, lus puis entendus",
       p:"À gauche ce que vous trouverez sur un papier, à droite ce qu'une secrétaire vous dira.",
       rows:[
         ["une échographie","é-co-gra-fie : un k, puis un f"],
         ["un psychiatre","psi-kiatre, comme dans psychologie"],
         ["le cholestérol","co-les-té-rol, aucun souffle de chat"],
         ["la technique","tec-nique, comme dans technologie"],
         ["six semaines","si semaines : la fin tombe devant la consonne"],
         ["dix heures","diz heures : la fin devient z devant la voyelle"],
         ["un schéma","ché-ma : trois lettres pour un seul son"],
         ["un short","chort, prononcé à la française"],
       ]},

      {t:'piege', h:"Deux réflexes à changer, et un à ne pas prendre",
       rows:[
         ["taper le mot exactement comme il sonnait","essayer la lettre qui ne se prononce pas",
          "« écografie » ne donne rien. Prenez l'habitude d'essayer un ch devant un k et un x devant un s : le mot sort presque toujours dès la première tentative."],
         ["mettre le souffle de chat partout où il y a ch","retenir la courte liste des mots savants",
          "Prononcer « te-chnique » ou « psy-chiatre » à la façon de « chat » rend le mot introuvable pour celui qui vous écoute. Ces mots-là se comptent sur les doigts d'une main."],
         ["vouloir maîtriser les trois formes de six","viser à comprendre le délai qu'on vous donne",
          "Personne à l'accueil ne vous reprendra sur « siz semaines ». Ce qui compte est de comprendre la date ; la produire sans faute viendra plus tard, ou pas du tout."],
       ]},

      {t:'check', h:"Quatre questions, pour vérifier",
       p:"Une bonne réponse par question.",
       qs:[
         {q:"Dans « échographie », le groupe ch se prononce…", opts:["comme dans chat","comme un k"], ok:1,
          fb:"Un mot venu du grec : é-co-gra-fie, avec un k parfaitement audible."},
         {q:"Dans « soixante-dix », la lettre x se prononce…", opts:["comme un s","comme le groupe ks"], ok:0,
          fb:"Soi-sante-dis : le x y travaille comme dans six et dans dix."},
         {q:"Dans « un schéma », le groupe sch se prononce…", opts:["comme le groupe sk","comme dans chat"], ok:1,
          fb:"Trois lettres écrites à la file, un seul souffle à la sortie."},
         {q:"« Six semaines » se prononce…", opts:["si semaines","sisse semaines"], ok:0,
          fb:"Devant une consonne, la fin de six disparaît entièrement."},
       ]},

      {t:'revoir', h:"À garder de cette leçon",
       p:"Trois familles : <b>ch</b> se dit k dans les mots de science et de médecine (échographie, psychiatre, cholestérol) ; <b>x</b> se dit s dans six, dix et soixante ; <b>sh</b> et <b>sch</b> se disent comme dans chat (schéma, short). Devant un mot introuvable au dictionnaire, essayez la lettre qui ne se prononce pas."},
    ]
  },

  prPapiers: {
    eye:'Mini-leçon', tit:"Ce qu'on met dans son sac la veille",
    blocs:[
      {t:'texte', h:"Sept mois d'attente et vingt minutes de rendez-vous",
       p:"Un rendez-vous en spécialité, c'est un long silence suivi d'un très court moment. Ce qui se joue en vingt minutes se prépare la veille, sur la table de la cuisine, en dix minutes. Ce n'est pas une question de mémoire ni de courage : c'est une question de sac. Ce qui n'est pas dans le sac n'existera pas dans le bureau.",
       note:"Le savoir du programme s'appelle « tenir compte de la présentation matérielle et de la mise en page ». Il commence ici, avec ce que chaque papier sert à faire."},

      {t:'ana', h:"Les papiers qui vous font entrer",
       p:"Sans eux, la matinée s'arrête au comptoir.",
       mots:[["La carte d'assurance maladie",'ce qu'+"'"+'on présente avant même d'+"'"+'avoir dit un mot'],
             ['La lettre de convocation',"l'heure, l'étage, la salle et le nom de la personne qu'on va voir", true],
             ['Une pièce avec photo',"demandée dans certains services, jamais nulle part comme deuxième carte"]],
       say:"la carte d'assurance maladie, la lettre de convocation, une pièce avec photo",
       note:"Sur une convocation, le nom de famille est écrit avant le prénom. « Charest, Sylvine » : Charest est le nom. Le savoir évite de demander « le docteur Sylvine » au comptoir."},

      {t:'ana', h:"Les papiers que l'hôpital n'a pas",
       p:"Il n'a que ce qui a été fait chez lui. Tout le reste, c'est vous qui l'apportez.",
       mots:[["Les résultats d'un laboratoire privé","faits ailleurs, donc absents du dossier"],
             ["Les papiers d'un autre pays","à apporter tels quels, même dans une autre langue", true],
             ["La liste de tout ce que vous prenez","ordonnances, vitamines, tisanes, produits rapportés d'ailleurs"]],
       say:"les résultats d'un laboratoire privé, les papiers d'un autre pays, la liste de tout ce que vous prenez",
       note:"« Je ne prends rien » est presque toujours faux. Tout ce qui se prend compte, y compris ce qui s'achète sans ordonnance — et c'est exactement pour ça qu'on pose la question."},

      {t:'ana', h:"Les papiers que vous écrivez vous-même",
       p:"Ce sont les seuls sur lesquels vous avez la main. Ils tiennent sur une feuille.",
       mots:[['Vos trois questions',"écrites la veille, dans l'ordre d'importance"],
             ['Vos antécédents',"les évènements de santé déjà arrivés, en une ligne chacun", true],
             ['Un crayon',"pour noter les dates plutôt que d'essayer de les retenir"]],
       say:"vos trois questions, vos antécédents, un crayon",
       note:"Une fois assis devant quelqu'un, personne ne se rappelle ce qu'il voulait demander. Ce n'est pas de la nervosité : c'est ainsi pour tout le monde, dans toutes les langues."},

      {t:'ex', h:"Cinq questions à se poser avant de partir",
       p:"Dans cet ordre, la veille au soir.",
       rows:[
         ["Où, exactement ?","le pavillon, l'étage et la salle — vingt minutes de marge la première fois"],
         ["Qui vais-je voir ?","le nom de famille d'abord ; savoir lequel des deux mots est le nom"],
         ["Qu'est-ce que je prends ?","tout, y compris ce qui s'achète sans papier"],
         ["Qu'est-ce qui n'est pas au dossier ?","ce qui a été fait ailleurs qu'ici"],
         ["Qu'est-ce que je veux savoir ?","trois questions écrites valent mieux que dix questions pensées"],
       ]},

      {t:'piege', h:"Trois erreurs qui coûtent un rendez-vous",
       rows:[
         ["trier ses papiers d'avance et n'apporter que l'utile","tout apporter et laisser trier l'autre",
          "Vous ne pouvez pas savoir ce qui servira : c'est le métier de la personne en face. Le papier que vous jugez inutile est souvent celui qui explique tout."],
         ["répondre « rien » à la question des médicaments","noter même les vitamines",
          "Ce n'est pas un piège ni un contrôle : la question sert à comprendre ce qui circule dans votre corps. Un produit rapporté d'un voyage compte autant qu'une ordonnance."],
         ["se dire qu'on posera ses questions au bon moment","les écrire la veille",
          "Le bon moment n'arrive pas : il y a le récit, puis l'examen, puis la conclusion, et la porte est ouverte. Une feuille sur les genoux, elle, est encore là à la fin."],
       ]},

      {t:'check', h:"Trois questions, pour vérifier",
       p:"Une bonne réponse par question.",
       qs:[
         {q:"Sur une convocation, « Charest, Sylvine » : quel est le nom de famille ?", opts:["Sylvine","Charest"], ok:1,
          fb:"Le nom de famille est écrit en premier, en majuscules quand la machine le permet."},
         {q:"Des résultats faits dans un laboratoire privé…", opts:["sont automatiquement au dossier de l'hôpital","doivent être apportés sur papier"], ok:1,
          fb:"L'hôpital ne voit que ce qui a été fait chez lui. Le reste voyage avec vous."},
         {q:"Combien de questions vaut-il mieux écrire la veille ?", opts:["trois, dans l'ordre d'importance","le plus possible, pour ne rien oublier"], ok:0,
          fb:"Trois questions posées valent mieux que douze questions notées et jamais sorties de la poche."},
       ]},

      {t:'revoir', h:"Ce qu'il faut garder",
       p:"Cinq questions la veille : <b>où</b>, <b>qui</b>, <b>ce que je prends</b>, <b>ce qui n'est pas au dossier</b>, <b>ce que je veux savoir</b>. Tout apporter, ne rien trier soi-même, et sortir de la maison avec un crayon."},
    ]
  },

  t1amorce: {
    eye:'Mini-leçon', tit:"Parler à quelqu'un qui ne vous doit rien",
    blocs:[
      {t:'texte', h:"Le seul endroit d'un hôpital sans guichet",
       p:"Partout ailleurs dans un établissement, quelqu'un est payé pour vous répondre. Dans une salle d'attente, non : la personne à côté de vous n'a aucune obligation, et c'est précisément ce qui rend la conversation possible. Personne n'évalue votre français, personne ne remplit un formulaire. C'est le meilleur exercice de langue de la matinée, et il est gratuit.",
       note:"Le programme du niveau 6 nomme cette intention à part : « échanger avec quelqu'un dans la salle d'attente ». Elle n'existe à aucun niveau plus bas."},

      {t:'ana', h:"Ce dont on parle, et ce dont on ne parle pas",
       p:"La règle tient en une phrase : on parle de ce qui est à tout le monde, jamais de ce qui est à l'autre.",
       mots:[['Ce qui est à tout le monde',"l'attente, l'heure, le stationnement, le froid, le café de la machine"],
             ["Ce qui appartient à l'autre","ce qu'il a, pourquoi il est là, ce qu'on lui a dit, son âge", true],
             ['Ce qui se donne, jamais ne se demande',"si l'autre raconte sa maladie, c'est son choix ; on ne le provoque pas"]],
       say:"l'attente, l'heure, le stationnement, ce qu'il a, pourquoi il est là",
       note:"Cette frontière n'est pas propre au Québec, mais elle y est nette. Une question sur la santé de quelqu'un qu'on ne connaît pas met mal à l'aise, même posée gentiment."},

      {t:'ana', h:"Trois amorces qui marchent partout",
       p:"Elles se répondent en un mot par quelqu'un qui n'a pas envie de parler, et en dix minutes par quelqu'un qui en a envie. C'est tout leur mérite.",
       mots:[['« Vous attendez depuis longtemps ? »',"la plus sûre : elle porte sur ce qu'on partage"],
             ['« Ça avance, vous pensez ? »',"la même, en plus léger, quand la salle est pleine", true],
             ['« C'+"'"+'est bien ici, la salle C ? »',"une vraie question, à laquelle on ne peut pas ne pas répondre"]],
       say:"Vous attendez depuis longtemps ? Ça avance, vous pensez ? C'est bien ici, la salle C ?",
       note:"Si la réponse est courte et ne revient pas vers vous, on s'arrête. Ce n'est pas un refus de vous : c'est un refus de parler, et il est légitime."},

      {t:'ana', h:"Ce qui transforme deux phrases polies en conversation",
       p:"Trois gestes, dans cet ordre. Ils s'apprennent une fois et servent partout ailleurs.",
       mots:[["Reprendre un mot de l'autre",'« — C'+"'"+'est ma femme qui est là-dedans. — Ah, vous l'+"'"+'attendez tout ce temps-là ? »'],
             ['Donner un peu de soi',"« Chez nous, c'était pareil avec mon père. » — sans quoi ça devient un interrogatoire", true],
             ["Réagir avant d'enchaîner","« Ça, c'est une bonne nouvelle. » plutôt que de repartir aussitôt sur soi"]],
       say:"Ah, vous l'attendez tout ce temps-là ? Chez nous, c'était pareil avec mon père. Ça, c'est une bonne nouvelle.",
       note:"Reprendre un mot de l'autre est ce que le programme appelle « s'introduire dans une discussion et y participer ». C'est aussi le geste qui vous laisse le temps de chercher vos mots."},

      {t:'ex', h:"Sept phrases et leur travail",
       p:"Chacune fait une chose et une seule.",
       rows:[
         ["Vous attendez depuis longtemps ?","ouvrir sur ce qui est commun"],
         ["Ah, vous l'attendez tout ce temps-là ?","reprendre un mot pour montrer qu'on écoutait"],
         ["Chez nous, c'était pareil.","donner un peu de soi"],
         ["Fatiguée comment, exactement ?","demander une précision, une fois l'autre lancé"],
         ["Je ne veux pas être indiscret, par exemple.","annoncer qu'on s'arrête si ça va trop loin"],
         ["Ça, c'est une bonne nouvelle.","réagir sans enchaîner sur soi"],
         ["Bon, ils vous appellent. Bonne chance.","terminer sans avoir à se justifier"],
       ]},

      {t:'piege', h:"Trois façons de faire fuir son voisin de banquette",
       rows:[
         ["demander ce que l'autre a","attendre qu'il le dise, ou ne jamais le savoir",
          "« Vous êtes ici pour quoi ? » est la seule question vraiment déplacée dans une salle d'attente. Tout le reste se pardonne."],
         ["enchaîner tout de suite sur son propre cas","réagir d'abord à ce qui vient d'être dit",
          "L'autre raconte l'opération de sa femme, et vous parlez de votre cousin. La conversation meurt là. Un « ça n'a pas dû être facile » avant de continuer change tout."],
         ["s'excuser de son français","parler, tout simplement",
          "« Excusez mon français » ouvre une conversation sur vous au lieu d'une conversation avec vous. Personne dans une salle d'attente ne juge un accent : tout le monde attend."],
       ]},

      {t:'check', h:"Trois questions, pour vérifier",
       p:"Une bonne réponse par question.",
       qs:[
         {q:"Quelle amorce est la plus sûre ?", opts:["« Vous êtes ici pour quoi ? »","« Vous attendez depuis longtemps ? »"], ok:1,
          fb:"L'attente appartient à tout le monde ; la raison de la visite appartient à l'autre."},
         {q:"Votre voisin répond en deux mots et ne vous demande rien. Vous…", opts:["reposez une autre question","vous arrêtez là"], ok:1,
          fb:"Ce n'est pas un refus de vous : c'est un refus de parler, et il se respecte sans commentaire."},
         {q:"L'autre vient de raconter quelque chose de difficile. Le mieux est de…", opts:["réagir à ce qu'il a dit avant de parler de soi","raconter tout de suite un cas semblable"], ok:0,
          fb:"Réagir d'abord, enchaîner ensuite. C'est ce qui distingue une conversation d'une suite de monologues."},
       ]},

      {t:'revoir', h:"Ce qu'il faut garder",
       p:"On parle de <b>ce qui est à tout le monde</b> — l'attente, l'heure, le froid — et jamais de ce qui appartient à l'autre. On <b>reprend un mot</b> de ce qu'il vient de dire, on <b>donne un peu de soi</b>, on <b>réagit avant d'enchaîner</b>, et on termine sans se justifier."},
    ]
  },

  t1pqp: {
    eye:'Mini-leçon', tit:"Le passé d'avant le passé",
    blocs:[
      {t:'texte', h:"Deux évènements, et lequel vient en premier",
       p:"Raconter, ce n'est pas énumérer. Quand Leyla dit « je suis venue au rendez-vous, mon médecin avait envoyé la demande en avril », elle place deux moments l'un derrière l'autre sans avoir à dire lequel est le plus vieux : la forme du verbe le dit à sa place. C'est ça, le plus-que-parfait — le seul temps dont le travail est de reculer d'un cran.",
       note:"Le programme du niveau 6 l'écrit ainsi : « comprendre l'antériorité avec le plus-que-parfait quand le point de référence est décalé »."},

      {t:'ana', h:"Comment il se forme",
       p:"Deux morceaux, et vous les connaissez déjà tous les deux.",
       mots:[["L'auxiliaire, mis à l'imparfait",'j\'avais · tu avais · il avait · nous avions · vous aviez · ils avaient — ou j\'étais, il était…'],
             ['Le participe passé',"le même qu'au passé composé : attendu, dormi, pensé, venu, parti", true],
             ["Le choix de l'auxiliaire","exactement le même qu'au passé composé : si vous dites « je suis venue », vous direz « j'étais venue »"]],
       say:"j'avais attendu, elle était venue, nous avions pensé, ils étaient partis",
       note:"Rien de neuf à apprendre : c'est votre passé composé avec l'auxiliaire à l'imparfait. Un seul changement, appliqué partout."},

      {t:'ana', h:"Les accords ne changent pas non plus",
       p:"Ce sont les règles du passé composé, sans une exception de plus.",
       mots:[['Avec être, on accorde avec le sujet',"elle était venue · ils étaient passés · elles étaient arrivées"],
             ['Avec avoir, on n'+"'"+'accorde pas',"elle avait attendu · ils avaient pensé — le participe ne bouge pas", true],
             ["Sauf le complément direct placé devant","les feuilles qu'elle avait apportées — cas rare, à reconnaître plus qu'à produire"]],
       say:"elle était venue, ils étaient passés, elle avait attendu, les feuilles qu'elle avait apportées",
       note:"Si vous hésitez sur l'accord, demandez-vous d'abord quel auxiliaire vous auriez mis au passé composé. La réponse est déjà là."},

      {t:'labo', h:"Le même verbe, aux deux passés",
       p:"Choisissez un verbe, puis le temps.",
       axes:[
         {id:'v', lbl:'Quel verbe ?', opts:[['a','attendre'],['b','venir'],['c','comprendre']]},
         {id:'t', lbl:'Quel temps ?', opts:[['1','passé composé'],['2','plus-que-parfait']]}],
       out:{
         a1:{w:["elle a attendu sept mois"], say:"elle a attendu sept mois", n:'un fait passé, raconté depuis aujourd\'hui'},
         a2:{w:["elle avait attendu sept mois"], say:"elle avait attendu sept mois", n:'un fait déjà accompli au moment dont on parle'},
         b1:{w:["elle est venue en octobre"], say:"elle est venue en octobre", n:'auxiliaire être, accord avec le sujet'},
         b2:{w:["elle était venue en octobre"], say:"elle était venue en octobre", n:'même auxiliaire, même accord, un cran plus loin'},
         c1:{w:["il a compris tout de suite"], say:"il a compris tout de suite", n:'auxiliaire avoir, aucun accord'},
         c2:{w:["il avait compris tout de suite"], say:"il avait compris tout de suite", n:'avant l\'autre évènement passé du récit'},
       },
       note:"Écoutez la différence : elle ne tient qu'à l'auxiliaire, et pourtant elle change complètement l'ordre des évènements."},

      {t:'ex', h:"Six récits, deux temps chacun",
       p:"À gauche, le moment dont on parle ; à droite, ce qui s'était passé avant.",
       rows:[
         ["Elle est arrivée fatiguée.","Elle avait pourtant dormi neuf heures."],
         ["En novembre, elle a vu la spécialiste.","Son médecin avait envoyé la demande en avril."],
         ["Elle n'a rien fait au mois de mars.","Elle avait pensé que c'était l'hiver."],
         ["En août, la femme de Gilles voulait annuler.","Elle avait perdu le courage d'attendre."],
         ["Tout était au dossier ce matin-là.","Les prélèvements avaient été faits au printemps."],
         ["Elle a trouvé la salle sans hésiter.","Elle était venue une fois, en octobre."],
       ]},

      {t:'piege', h:"Deux façons de brouiller un récit",
       rows:[
         ["mettre l'imparfait partout dans un récit","garder l'imparfait pour le décor",
          "« Je dormais neuf heures » décrit une habitude ; « j'avais dormi neuf heures » raconte une nuit précise, avant le matin dont on parle. Les deux existent, ils ne disent pas la même chose."],
         ["croire que le plus-que-parfait est un temps rare et littéraire","l'entendre dans toutes les conversations",
          "Il est partout dès qu'on raconte : « j'avais laissé faire », « on avait passé proche d'annuler », « elle avait arrêté de porter ça toute seule ». Le passé simple, lui, est littéraire ; celui-ci, non."],
         ["laisser le participe invariable après être","refaire le réflexe du passé composé",
          "« Elle était venu » se corrige tout seul si l'on se demande d'abord : au passé composé, je dirais « elle est venue ». L'accord suit l'auxiliaire, pas le temps."],
       ]},

      {t:'check', h:"Quatre questions, pour vérifier",
       p:"Une bonne réponse par question.",
       qs:[
         {q:"« Elle est venue au rendez-vous. Son médecin ___ la demande sept mois plus tôt. »", opts:["a envoyé","avait envoyé"], ok:1,
          fb:"L'envoi vient avant la visite : on recule d'un cran."},
         {q:"Comment se forme le plus-que-parfait ?", opts:["l'auxiliaire à l'imparfait + le participe passé","l'auxiliaire au présent + l'infinitif"], ok:0,
          fb:"C'est le passé composé, avec l'auxiliaire à l'imparfait. Rien d'autre ne change."},
         {q:"« Elles ___ arrivées avant l'ouverture. »", opts:["étaient","avaient"], ok:0,
          fb:"Arriver se conjugue avec être, au plus-que-parfait comme au passé composé — et le participe s'accorde."},
         {q:"Dans un récit, entendre « avait » suivi d'un participe veut dire que…", opts:["la personne recule d'un cran dans le temps","la personne parle du présent"], ok:0,
          fb:"C'est le signal le plus fiable qu'il y a : on quitte le fil pour raconter ce qui précède."},
       ]},

      {t:'revoir', h:"Ce qu'il faut garder",
       p:"<b>Auxiliaire à l'imparfait + participe passé.</b> Le même auxiliaire et les mêmes accords qu'au passé composé. Il sert à placer un évènement <b>avant</b> un autre évènement déjà passé — et à l'écoute, « avait » ou « était » suivis d'un participe annoncent qu'on recule d'un cran."},
    ]
  },

  t1aspect: {
    eye:'Mini-leçon', tit:"Être après, être pour, passer proche",
    blocs:[
      {t:'texte', h:"Ce que les manuels ne disent pas et que la salle d'attente dit tout de suite",
       p:"Gilles ouvre la conversation par « vous êtes après attendre depuis longtemps ? ». Aucun cours ne vous a préparé à cette phrase-là, et pourtant elle est parfaitement ordinaire ici. Le français du Québec a quatre tournures qui disent où en est une action : commencée, imminente, retenue de justesse, ou évitée de peu. Les comprendre coûte dix minutes ; ne pas les comprendre coûte la moitié d'une conversation.",
       note:"Le programme du niveau 6 les nomme : « comprendre être après, être pour, être sur le bord de, passer proche de + verbe à l'infinitif ». Il demande de les comprendre, pas de les produire."},

      {t:'ana', h:"Être après + infinitif — c'est en train de se faire",
       p:"La plus fréquente des quatre, et celle qui déroute le plus, parce que « après » ne parle pas du tout de temps ici.",
       mots:[['Ce qu'+"'"+'on entend',"je suis après attendre · il est après remplir ses papiers · elle était après manger"],
             ['Ce que ça veut dire',"exactement « être en train de » — l'action est commencée et pas finie", true],
             ["Ce qu'on écrit à la place","je suis en train d'attendre ; dans un courriel, on n'écrit pas « après »"]],
       say:"je suis après attendre, il est après remplir ses papiers, je suis en train d'attendre",
       note:"Ne cherchez pas de logique dans « après » : la tournure est ancienne et elle est venue de France avant de s'y perdre. Il faut la reconnaître, pas la comprendre."},

      {t:'ana', h:"Être pour et être sur le bord de — c'est sur le point d'arriver",
       p:"Les deux disent l'imminence, mais pas avec la même force.",
       mots:[["Être pour + infinitif","j'étais pour partir quand ils m'ont appelée — soit « j'allais partir »"],
             ["Être sur le bord de + infinitif","je suis sur le bord de pleurer — à un cheveu, et retenu de justesse", true],
             ['La nuance',"« être pour » est neutre ; « sur le bord de » dit une émotion ou un effort"]],
       say:"j'étais pour partir, je suis sur le bord de pleurer, j'allais partir",
       note:"Attention à ne pas confondre « j'étais pour partir » avec « c'est pour vous » : la première a un verbe à l'infinitif derrière, la seconde un nom ou un pronom."},

      {t:'ana', h:"Passer proche de + infinitif — ça a failli arriver",
       p:"Celle-ci parle du passé, et elle a une particularité : le résultat est toujours négatif.",
       mots:[['Ce qu'+"'"+'on entend',"on a passé proche d'annuler · j'ai passé proche de manquer mon autobus"],
             ['Ce que ça veut dire',"on a failli annuler — donc on n'a PAS annulé", true],
             ['La faute de compréhension',"comprendre « on a annulé » est le contresens exact, et il arrive tout le temps"]],
       say:"on a passé proche d'annuler, j'ai passé proche de manquer mon autobus, on a failli annuler",
       note:"Le même piège existe avec « il s'en est fallu de peu » et « à un cheveu près » : dans les trois cas, la chose ne s'est pas produite."},

      {t:'ex', h:"Six phrases entendues, six traductions",
       p:"À gauche, ce qui se dit ; à droite, ce que ça veut dire.",
       rows:[
         ["Je suis après attendre.","Je suis en train d'attendre."],
         ["Il est après remplir sa feuille.","Il est en train de remplir sa feuille."],
         ["J'étais pour partir.","J'allais partir."],
         ["Je suis sur le bord de pleurer.","Je me retiens de pleurer, de justesse."],
         ["On a passé proche d'annuler.","On a failli annuler — et on ne l'a pas fait."],
         ["Ça fait deux heures que je suis là.","J'attends depuis deux heures, et j'attends encore."],
       ]},

      {t:'piege', h:"Trois façons de se tromper de sens",
       rows:[
         ["comprendre « après » comme un moment","le comprendre comme « en train de »",
          "« Je suis après manger » ne veut pas dire « j'ai fini de manger ». C'est exactement le contraire : c'est en cours."],
         ["comprendre « passé proche de » comme un fait accompli","chercher le verbe qui suit",
          "« On a passé proche d'annuler » veut dire qu'on n'a pas annulé. Si vous entendez cette tournure, la chose n'est pas arrivée."],
         ["employer ces tournures dans un courriel ou un formulaire","garder être en train de, aller, faillir",
          "Elles sont justes à l'oral et déplacées à l'écrit administratif. Écrire « j'étais pour annuler mon rendez-vous » dans un courriel au secrétariat détonne."],
       ]},

      {t:'check', h:"Quatre questions, pour vérifier",
       p:"Une bonne réponse par question.",
       qs:[
         {q:"« Je suis après attendre » veut dire…", opts:["j'ai fini d'attendre","je suis en train d'attendre"], ok:1,
          fb:"« Être après + infinitif » dit toujours qu'une action est en cours."},
         {q:"« On a passé proche d'annuler » veut dire…", opts:["on a annulé","on n'a pas annulé"], ok:1,
          fb:"C'est « on a failli » : la chose ne s'est pas produite."},
         {q:"Laquelle des quatre dit une émotion retenue de justesse ?", opts:["être sur le bord de","être après"], ok:0,
          fb:"« Je suis sur le bord de pleurer » : à un cheveu, et ça se voit."},
         {q:"Dans un courriel au secrétariat, on écrit…", opts:["j'étais pour annuler","j'allais annuler"], ok:1,
          fb:"Ces tournures sont de l'oral. À l'écrit, on emploie aller, être en train de, faillir."},
       ]},

      {t:'revoir', h:"Ce qu'il faut garder",
       p:"<b>Être après</b> = être en train de. <b>Être pour</b> = aller (imminent). <b>Être sur le bord de</b> = à un cheveu, souvent une émotion. <b>Passer proche de</b> = avoir failli, donc <b>ne pas l'avoir fait</b>. Les quatre se comprennent ; à l'écrit, on écrit les équivalents."},
    ]
  },

  t1repr: {
    eye:'Mini-leçon', tit:"Redire la même chose sans employer le même mot",
    blocs:[
      {t:'texte', h:"Ce qui tient un texte ensemble",
       p:"Prenez n'importe quel paragraphe qui vous a paru difficile et regardez ce qui s'y répète : presque rien. Le même sujet y est nommé quatre fois de quatre façons — « une fatigue », « cette fatigue », « ce malaise », « le problème ». Rien n'a changé, et pourtant chaque phrase paraît neuve. Suivre un texte au niveau 6, c'est d'abord savoir que ces quatre groupes désignent la même chose.",
       note:"Le programme parle de « reprendre des référents par une variété de déterminants possessifs, démonstratifs et définis » et d'« employer des procédés de substitution lexicale »."},

      {t:'ana', h:"Reprendre en changeant seulement le déterminant",
       p:"Le nom reste, le petit mot devant change. C'est la reprise la plus simple et la plus fréquente.",
       mots:[['Le démonstratif — je montre celui dont je viens de parler',"une fatigue est apparue… → <b>cette</b> fatigue dure encore"],
             ['Le possessif — je le rattache à quelqu'+"'"+'un',"Gilles accompagne sa femme… → <b>sa</b> patience étonne tout le monde", true],
             ['Le défini — c'+"'"+'est déjà connu, on ne le présente plus',"une lettre est arrivée… → <b>la</b> lettre était courte"]],
       say:"cette fatigue, sa patience, la lettre",
       note:"Passer de « une » à « la » n'est pas décoratif : c'est le signal que la chose a déjà été présentée. Un texte qui garde « une » partout donne l'impression qu'on recommence à chaque phrase."},

      {t:'ana', h:"Reprendre en changeant de mot",
       p:"Trois façons, de la plus facile à la plus utile.",
       mots:[['Le synonyme',"un rendez-vous → une rencontre ; une feuille → un papier"],
             ['Le mot plus général',"une échographie, une prise de sang → <b>cet examen</b> ; le rendez-vous, la lettre, l'appel → <b>cette démarche</b>", true],
             ['Le nom tiré du verbe',"elle a attendu → <b>cette attente</b> ; elle est arrivée en retard → <b>ce retard</b>"]],
       say:"cet examen, cette démarche, cette attente, ce retard",
       note:"Le mot plus général est celui qui sauve quand aucun synonyme ne vient. Il suffit de monter d'un cran : un objet, un papier, une démarche, une question, un problème."},

      {t:'ana', h:"Le nom tiré du verbe, celui des documents",
       p:"C'est le procédé le plus employé par les textes administratifs, et c'est pour ça qu'ils paraissent difficiles.",
       mots:[['attendre → l'+"'"+'attente',"il a fallu attendre. Cette attente a duré sept mois."],
             ['arriver → l'+"'"+'arrivée',"elle est arrivée à neuf heures. Son arrivée est notée au dossier.", true],
             ['prélever → le prélèvement',"on a prélevé du sang. Le prélèvement date de mars."]],
       say:"cette attente, son arrivée, le prélèvement",
       note:"Le Défi 3 revient là-dessus en entier : c'est exactement ce qui sépare ce que vous dites de ce que la médecin écrit."},

      {t:'ex', h:"Sept reprises, tirées du dossier de Leyla",
       p:"À gauche, la première phrase ; à droite, la reprise.",
       rows:[
         ["Une fatigue est apparue en février.","Cette fatigue n'est jamais repartie."],
         ["Elle a attendu sept mois.","Ce délai lui a paru interminable."],
         ["On a demandé une échographie et une prise de sang.","Ces examens se font au rez-de-chaussée."],
         ["Gilles accompagne sa femme depuis deux ans.","Sa patience étonne tout le monde."],
         ["Leyla et son fils se parlent le dimanche.","Leurs appels durent une heure."],
         ["Il a fallu attendre toute la matinée.","Cette attente est la partie la plus dure."],
         ["Elle est repartie sans savoir ce qu'elle avait.","Cette incertitude pèse plus que la fatigue."],
       ]},

      {t:'piege', h:"Trois défauts de reprise",
       rows:[
         ["répéter le nom à chaque phrase","changer le déterminant, au minimum",
          "« La docteure a expliqué. La docteure a demandé des examens. La docteure a dit que la docteure allait écrire. » Le texte n'est pas faux : il est illisible."],
         ["reprendre par un mot plus précis que le premier","monter d'un cran, jamais descendre",
          "Si l'on a dit « un examen », on peut reprendre par « cet examen ». On ne peut pas reprendre par « cette échographie » si personne n'a dit qu'il s'agissait d'une échographie."],
         ["employer « ce » pour quelque chose de neuf","présenter d'abord avec « un » ou « une »",
          "« Cette fatigue » en première phrase d'un courriel laisse le lecteur chercher de quelle fatigue on parle. Le démonstratif reprend ; il ne présente pas."],
       ]},

      {t:'check', h:"Quatre questions, pour vérifier",
       p:"Une bonne réponse par question.",
       qs:[
         {q:"« Elle a attendu sept mois. ___ délai lui a paru long. »", opts:["Un","Ce"], ok:1,
          fb:"Le démonstratif reprend ce qui vient d'être dit ; « un » le présenterait comme neuf."},
         {q:"Le nom tiré du verbe « attendre » est…", opts:["l'attendage","l'attente"], ok:1,
          fb:"Irrégulier, et à apprendre en paire : attendre / l'attente."},
         {q:"Après « une échographie et une prise de sang », on peut reprendre par…", opts:["ces examens","cette échographie"], ok:0,
          fb:"On monte d'un cran vers le mot plus général. On ne redescend pas vers un seul des deux."},
         {q:"À quoi sert la reprise, au fond ?", opts:["à faire plus joli","à faire tenir un texte ensemble"], ok:1,
          fb:"C'est ce qui permet au lecteur de savoir qu'on parle encore de la même chose."},
       ]},

      {t:'revoir', h:"Ce qu'il faut garder",
       p:"Deux moyens : changer le <b>déterminant</b> (une fatigue → <b>cette</b> fatigue, <b>sa</b> fatigue, <b>la</b> fatigue) ou changer le <b>mot</b> (un synonyme, un mot plus général, le nom tiré du verbe). Quand rien ne vient, montez d'un cran : <b>cet examen</b>, <b>cette démarche</b>, <b>ce papier</b>."},
    ]
  },

  t2precis: {
    eye:'Mini-leçon', tit:"Ce qui se travaille et ce qui ne se travaille pas",
    blocs:[
      {t:'texte', h:"Vingt minutes, et personne ne devine",
       p:"« Comment allez-vous ? » est une question de politesse partout ailleurs. Dans un bureau de consultation, c'en est une vraie, et « ça va » est une réponse perdue. Ce n'est pas une question de courage ni de vocabulaire savant : la personne devant vous n'a que ce que vous dites. Ce que vous ne dites pas n'existe pas, et ce que vous dites en adjectifs ne se compare à rien dans six semaines.",
       note:"L'intention du programme est « s'informer auprès d'un spécialiste à propos d'un problème de santé ». S'informer suppose d'abord d'avoir informé."},

      {t:'ana', h:"Premier réflexe — un repère de temps plutôt qu'une durée floue",
       p:"« Depuis un bout de temps » ne se note pas dans un dossier. Une date, oui.",
       mots:[['Ce qui ne sert pas',"depuis un bout de temps · ça fait longtemps · depuis un certain temps"],
             ['Ce qui sert',"depuis février · depuis le mois où mon fils a déménagé · depuis huit mois", true],
             ['Le truc',"accrochez le début à un évènement dont vous vous souvenez, plutôt qu'à une date devinée"]],
       say:"depuis un bout de temps, depuis février, depuis le mois où mon fils a déménagé",
       note:"Un évènement personnel est un repère plus fiable qu'une date : personne ne se trompe sur le mois où son fils a déménagé."},

      {t:'ana', h:"Deuxième réflexe — un changement plutôt qu'un état",
       p:"On ne compare pas ce que vous ressentez à ce que ressentent les autres. On le compare à ce que vous ressentiez avant.",
       mots:[["Ce qui ne se travaille pas",'je suis fatiguée · je me sens mal · je n'+"'"+'ai pas d'+"'"+'énergie'],
             ['Ce qui se travaille',"vers dix heures, il faut que je m'assoie ; avant, je ne m'assoyais pas", true],
             ['Pourquoi',"un changement a une date, se vérifie et se recompare dans six semaines"]],
       say:"je suis fatiguée, vers dix heures il faut que je m'assoie, avant je ne m'assoyais pas",
       note:"C'est le conseil que Gilles donne dans la salle d'attente, et c'est le même que donnerait n'importe quel professionnel."},

      {t:'ana', h:"Troisième réflexe — une scène plutôt qu'un adjectif",
       p:"Une scène se refait dans six semaines et se compare. Un adjectif, non.",
       mots:[['Un adjectif',"je manque de souffle · je suis essoufflée"],
             ['Une scène',"chez madame Turcotte, il y a douze marches ; avant je les montais en parlant, là j'arrête de parler", true],
             ['Le format',"un lieu, un nombre, un avant, un maintenant — quatre éléments et c'est fait"]],
       say:"je manque de souffle, il y a douze marches, avant je les montais en parlant",
       note:"Douze marches, ce n'est pas un détail pittoresque : c'est une mesure. Dans six semaines, on remontera les mêmes douze marches."},

      {t:'ex', h:"Six phrases, avant et après",
       p:"À gauche, ce qu'on dit d'habitude ; à droite, ce qui peut servir.",
       rows:[
         ["Je suis fatiguée.","Vers dix heures, il faut que je m'assoie ; avant, non."],
         ["Ça fait un bout de temps.","Depuis février, le mois où mon fils a déménagé."],
         ["Je manque de souffle.","Je montais douze marches en parlant ; maintenant j'arrête de parler."],
         ["Je ne prends rien.","Rien d'ordonnance, mais des vitamines tous les jours l'hiver."],
         ["Des fois ça va, des fois moins.","Le samedi est meilleur ; les autres jours se ressemblent."],
         ["Ce n'est pas si pire.","Ça dure depuis huit mois et ça change ma façon de travailler."],
       ]},

      {t:'piege', h:"Trois habitudes qui coûtent cher",
       rows:[
         ["minimiser","dire ce qui est, sans le peser",
          "« Il y a plus malade que moi », « je ne veux pas déranger » : vous ne dérangez pas, vous êtes le rendez-vous. Minimiser fait sortir un problème du dossier."],
         ["chercher le mot juste et se taire en attendant","décrire au lieu de nommer",
          "« Je ne connais pas le mot, mais c'est comme quand on se lève trop vite » est une excellente phrase. Un professionnel a l'habitude, et c'est même ce qu'il préfère entendre."],
         ["répondre à la question suivante avant d'avoir fini la précédente","finir sa phrase",
          "Le silence après votre réponse n'est pas un reproche : c'est de la place qu'on vous laisse. Le remplir trop vite fait perdre la moitié de ce que vous aviez à dire."],
       ]},

      {t:'check', h:"Trois questions, pour vérifier",
       p:"Une bonne réponse par question.",
       qs:[
         {q:"Laquelle de ces réponses est utilisable ?", opts:["Je suis fatiguée tout le temps.","Vers dix heures, il faut que je m'assoie ; avant, non."], ok:1,
          fb:"Un changement daté vaut dix adjectifs."},
         {q:"Le mot vous manque. Le mieux est de…", opts:["décrire avec vos mots à vous","attendre de retrouver le bon mot"], ok:0,
          fb:"« C'est comme quand on se lève trop vite » dit exactement ce qu'il faut."},
         {q:"« Il y a plus malade que moi » est…", opts:["une marque de politesse utile","une phrase qui fait perdre un renseignement"], ok:1,
          fb:"Minimiser ne rend service à personne, et surtout pas à la personne qui vous reçoit."},
       ]},

      {t:'revoir', h:"Ce qu'il faut garder",
       p:"Trois réflexes : un <b>repère de temps</b> accroché à un évènement, un <b>changement</b> plutôt qu'un état, une <b>scène</b> plutôt qu'un adjectif. Et deux interdits : minimiser, et se taire parce que le mot manque."},
    ]
  },

  t2inf: {
    eye:'Mini-leçon', tit:"De, à, ou rien du tout",
    blocs:[
      {t:'texte', h:"Une hésitation qui revient dix fois par jour",
       p:"« Elle m'a demandé de noter », « j'ai commencé à comprendre », « je dois passer des examens ». Trois phrases, trois façons différentes d'accrocher un infinitif au verbe qui précède — et aucune règle ne les explique. C'est une habitude, verbe par verbe, comme le genre des noms. La bonne nouvelle, c'est qu'il y en a peu à retenir pour parler d'une consultation.",
       note:"Le programme du niveau 6 en fait un savoir à part : « employer des phrases subordonnées infinitives CD, avec subordonnant de, avec subordonnant à, sans subordonnant »."},

      {t:'ana', h:"Ceux qui demandent « de »",
       p:"Ce sont souvent des verbes de demande, d'arrêt ou d'évitement — ceux d'une consultation, justement.",
       mots:[['La liste utile ici',"demander de · essayer de · arrêter de · éviter de · accepter de · oublier de · finir de · permettre de · refuser de"],
             ['Dans une phrase',"la docteure m'a demandé <b>de</b> noter mes journées · j'ai arrêté <b>de</b> monter en parlant", true],
             ["Devant une voyelle","<b>de</b> devient <b>d'</b> : elle a évité <b>d'</b>en parler · j'ai oublié <b>d'</b>apporter la feuille"]],
       say:"elle m'a demandé de noter mes journées, j'ai arrêté de monter en parlant, j'ai oublié d'apporter la feuille",
       note:"Repère approximatif mais utile : quand le verbe parle de ce qu'on fait faire à quelqu'un d'autre, c'est souvent « de »."},

      {t:'ana', h:"Ceux qui demandent « à »",
       p:"Souvent des verbes de commencement, d'effort ou de progression.",
       mots:[['La liste utile ici',"commencer à · continuer à · apprendre à · aider à · réussir à · hésiter à · se mettre à · arriver à"],
             ['Dans une phrase',"je commence <b>à</b> comprendre ce qu'elle cherche · Gilles a aidé sa femme <b>à</b> tenir", true],
             ["Il ne change jamais","« à » n'a pas de forme élidée : on écrit toujours à, même devant une voyelle"]],
       say:"je commence à comprendre, Gilles a aidé sa femme à tenir, elle a réussi à dire ce qui avait changé",
       note:"Repère approximatif : quand le verbe parle d'un mouvement vers quelque chose — commencer, apprendre, arriver —, c'est souvent « à »."},

      {t:'ana', h:"Ceux qui ne demandent rien",
       p:"Ce sont les plus fréquents de la langue, et c'est là que la faute se glisse.",
       mots:[['La liste',"vouloir · pouvoir · devoir · falloir · savoir · aller · venir · préférer · espérer · aimer · faire · laisser"],
             ['Dans une phrase',"je dois passer d'autres prélèvements · elle veut savoir ce qui a changé", true],
             ['La faute la plus fréquente à ce niveau',"« je dois <s>de</s> passer », « je peux <s>de</s> venir » — ces verbes ne veulent rien du tout"]],
       say:"je dois passer d'autres prélèvements, elle veut savoir ce qui a changé, je peux revenir en janvier",
       note:"Ce sont justement les verbes qu'on emploie le plus. Un « de » de trop après « devoir » ou « pouvoir » s'entend tout de suite."},

      {t:'ana', h:"La question qui entre dans la phrase",
       p:"Après savoir, demander, se demander, on peut poser une question sans point d'interrogation.",
       mots:[['Avec un mot interrogatif',"je ne sais pas <b>quoi</b> répondre · je ne sais pas <b>comment</b> le dire · je me demande <b>où</b> aller"],
             ["C'est quoi, jamais que","« je ne sais pas <s>que</s> répondre » ne se dit pas : devant un infinitif, c'est <b>quoi</b>", true],
             ["Le sujet est le même des deux côtés","c'est ce qui permet l'infinitif : je ne sais pas / je réponds → je ne sais pas quoi répondre"]],
       say:"je ne sais pas quoi répondre, je ne sais pas comment le dire, je me demande où aller",
       note:"Leyla emploie cette forme dans le bureau : « je ne sais pas quoi vous répondre pour la moyenne ». C'est une phrase d'adulte, et elle est parfaitement polie."},

      {t:'ex', h:"Huit phrases du dossier",
       p:"Le verbe, ce qui le suit, et l'infinitif.",
       rows:[
         ["demander","de","Elle m'a demandé de noter mes journées."],
         ["arrêter","de","J'ai arrêté de parler en montant l'escalier."],
         ["éviter","d'","Il faudrait éviter d'oublier les résultats."],
         ["commencer","à","Je commence à monter plus lentement."],
         ["réussir","à","Elle a réussi à dire ce qui avait changé."],
         ["hésiter","à","Elle hésitait à demander une attestation."],
         ["devoir","—","Je dois passer d'autres prélèvements."],
         ["savoir","quoi","Je ne savais pas quoi répondre."],
       ]},

      {t:'piege', h:"Trois erreurs et leur correction",
       rows:[
         ["mettre « de » après devoir, pouvoir, vouloir","ne rien mettre",
          "« Je dois de passer » n'existe pas. Ces verbes-là collent directement à l'infinitif, et ce sont ceux qu'on emploie le plus souvent."],
         ["écrire « je ne sais pas que faire »","écrire « je ne sais pas quoi faire »",
          "Devant un infinitif, la question se pose avec quoi. « Que faire ? » existe, seul, comme titre — pas après « je ne sais pas »."],
         ["apprendre les listes séparément du verbe","apprendre le verbe avec son petit mot",
          "Retenir « demander de » comme un seul bloc coûte le même effort que retenir « demander », et vous n'hésiterez plus jamais."],
       ]},

      {t:'check', h:"Quatre questions, pour vérifier",
       p:"Une bonne réponse par question.",
       qs:[
         {q:"« La docteure m'a demandé ___ noter mes journées. »", opts:["de","à"], ok:0,
          fb:"Demander de : un bloc à retenir tel quel."},
         {q:"« Je commence ___ comprendre. »", opts:["de","à"], ok:1,
          fb:"Commencer à, continuer à, apprendre à : les verbes de mouvement vers quelque chose."},
         {q:"« Je dois ___ passer d'autres examens. »", opts:["de","rien du tout"], ok:1,
          fb:"Devoir, pouvoir, vouloir, savoir : rien entre le verbe et l'infinitif."},
         {q:"« Je ne sais pas ___ répondre. »", opts:["que","quoi"], ok:1,
          fb:"Devant un infinitif, la question se pose toujours avec quoi."},
       ]},

      {t:'revoir', h:"Ce qu'il faut garder",
       p:"<b>de</b> : demander, arrêter, éviter, essayer, oublier, accepter. <b>à</b> : commencer, continuer, apprendre, aider, réussir, hésiter. <b>rien</b> : vouloir, pouvoir, devoir, falloir, savoir, aller, préférer. Et devant un infinitif, la question se pose avec <b>quoi</b>, jamais avec « que »."},
    ]
  },

  t2ou: {
    eye:'Mini-leçon', tit:"« Où » ne parle pas que des endroits",
    blocs:[
      {t:'texte', h:"Un mot de trois lettres qui recolle deux phrases",
       p:"« Février est le mois. Ma fatigue a commencé ce mois-là. » Deux phrases courtes, un lecteur qui trébuche. « Février est le mois où ma fatigue a commencé » : une phrase, aucune répétition, et le lien est dit. C'est tout le travail du pronom relatif — et « où » est le seul qui serve à la fois pour un lieu et pour un moment.",
       note:"Le programme demande deux choses : « associer le pronom relatif de lieu ou de temps où à son antécédent » et « employer des phrases subordonnées relatives avec le pronom relatif où »."},

      {t:'ana', h:"L'emploi qu'on connaît — le lieu",
       p:"Celui-là ne pose de problème à personne.",
       mots:[['Ce qu'+"'"+'il remplace',"la salle. J'attends dans cette salle. → la salle <b>où</b> j'attends"],
             ['Dans le dossier de Leyla',"le laboratoire, <b>où</b> vous êtes entrée ce matin · la seule salle <b>où</b> on peut parler à quelqu'un", true],
             ['Ce qu'+"'"+'il évite',"une deuxième phrase avec « dans cette salle », « à cet endroit », « là »"]],
       say:"la salle où j'attends, le laboratoire où vous êtes entrée ce matin",
       note:"Le mot juste avant « où » s'appelle son antécédent : c'est lui que la suite de la phrase vient préciser. Le repérer, c'est comprendre la phrase."},

      {t:'ana', h:"L'emploi qu'on oublie — le moment",
       p:"C'est celui-ci qui manque au français d'un adulte de niveau 6, et il est partout dans un récit.",
       mots:[['Avec un nom de temps',"le jour <b>où</b> · le mois <b>où</b> · l'année <b>où</b> · le matin <b>où</b> · l'époque <b>où</b> · le moment <b>où</b>"],
             ['Dans le dossier de Leyla',"le mois <b>où</b> mon fils a déménagé · le jour <b>où</b> j'aurai les résultats", true],
             ["Ce qu'on met à sa place, à tort","« le jour quand », « le jour que » — les deux se disent, aucun des deux ne s'écrit"]],
       say:"le jour où j'aurai les résultats, le mois où mon fils a déménagé, au moment où on l'a appelée",
       note:"« Quand » commence une phrase et ne s'accroche pas à un nom : « quand j'aurai les résultats, je vous appellerai » est juste, « le jour quand j'aurai » ne l'est pas."},

      {t:'ana', h:"L'accent, et ce qu'il change",
       p:"Deux mots différents, qui s'écrivent presque pareil et ne se prononcent pas autrement.",
       mots:[['<b>où</b> avec accent — il relie',"la salle <b>où</b> j'attends · le jour <b>où</b> elle rappellera"],
             ['<b>ou</b> sans accent — il sépare deux possibilités',"le lundi <b>ou</b> le jeudi · apportez la feuille <b>ou</b> envoyez-la", true],
             ['Le test',"remplacez par « ou bien » : si la phrase tient, c'est celui sans accent"]],
       say:"la salle où j'attends, le lundi ou le jeudi, apportez la feuille ou envoyez-la",
       note:"C'est un des rares accents du français qui distingue deux mots sans rien changer à la prononciation. Le test de « ou bien » ne se trompe jamais."},

      {t:'labo', h:"Deux phrases soudées en une",
       p:"Choisissez un cas, puis regardez ce que donne la soudure.",
       axes:[
         {id:'c', lbl:'Quel cas ?', opts:[['a','un lieu'],['b','un moment']]},
         {id:'n', lbl:'Quel exemple ?', opts:[['1','le premier'],['2','le second']]}],
       out:{
         a1:{w:["le laboratoire où vous êtes entrée ce matin"], say:"le laboratoire où vous êtes entrée ce matin", n:'antécédent : le laboratoire'},
         a2:{w:["la seule salle où on peut parler à quelqu'un"], say:"la seule salle où on peut parler à quelqu'un", n:'antécédent : la salle'},
         b1:{w:["le mois où mon fils a déménagé"], say:"le mois où mon fils a déménagé", n:'antécédent : le mois — un temps, pas un lieu'},
         b2:{w:["le jour où j'aurai les résultats"], say:"le jour où j'aurai les résultats", n:'antécédent : le jour — et le verbe peut être au futur'},
       },
       note:"Dans les quatre cas, le mot juste avant « où » est l'antécédent. C'est lui qu'il faut repérer d'abord, à l'écoute comme à la lecture."},

      {t:'ex', h:"Six phrases recollées",
       p:"À gauche, les deux phrases ; à droite, la phrase unique.",
       rows:[
         ["Février est le mois. Ma fatigue a commencé ce mois-là.","Février est le mois où ma fatigue a commencé."],
         ["Le laboratoire est en bas. Vous êtes entrée là ce matin.","Le laboratoire est en bas, où vous êtes entrée ce matin."],
         ["Elle rappellera un jour. Elle aura les résultats ce jour-là.","Elle rappellera le jour où elle aura les résultats."],
         ["C'est la seule salle. On peut y parler à quelqu'un.","C'est la seule salle où on peut parler à quelqu'un."],
         ["On l'a appelée à un moment. Elle parlait avec Gilles.","Au moment où on l'a appelée, elle parlait avec Gilles."],
         ["Elle est arrivée une année. Il neigeait en mai cette année-là.","L'année où elle est arrivée, il neigeait en mai."],
       ]},

      {t:'piege', h:"Trois faux pas de ce point-ci",
       rows:[
         ["écrire « le jour quand »","écrire « le jour où »",
          "« Quand » ouvre une phrase entière ; il ne s'accroche jamais à un nom. C'est la faute la plus fréquente, et elle s'entend."],
         ["écrire « le jour que »","écrire « le jour où »",
          "« Le jour que je l'ai vue » se dit couramment à l'oral et ne s'écrit pas. À l'écrit, un nom de temps appelle « où »."],
         ["oublier l'accent","faire le test de « ou bien »",
          "« La salle ou j'attends » ne veut rien dire, et le lecteur le sent avant de comprendre pourquoi. Si « ou bien » ne marche pas, mettez l'accent."],
       ]},

      {t:'check', h:"Quatre questions, pour vérifier",
       p:"Une bonne réponse par question.",
       qs:[
         {q:"« Février est le mois ___ ma fatigue a commencé. »", opts:["quand","où"], ok:1,
          fb:"Un nom de temps appelle « où », jamais « quand »."},
         {q:"« Elle vient le lundi ___ le jeudi. »", opts:["ou","où"], ok:0,
          fb:"On peut dire « ou bien » : c'est celui sans accent."},
         {q:"Dans « le laboratoire où vous êtes entrée », l'antécédent est…", opts:["le laboratoire","vous"], ok:0,
          fb:"C'est le nom juste avant « où » que la suite vient préciser."},
         {q:"« Le jour ___ j'aurai les résultats, je vous appelle. »", opts:["que","où"], ok:1,
          fb:"« Le jour que » se dit, mais ne s'écrit pas."},
       ]},

      {t:'revoir', h:"Ce qu'il faut garder",
       p:"<b>où</b> relie une phrase à un nom, et ce nom peut être un <b>lieu</b> (la salle où j'attends) ou un <b>moment</b> (le jour où j'aurai les résultats). Ni « quand », ni « que » ne le remplacent. Et l'accent se vérifie par « ou bien »."},
    ]
  },

  t2subj: {
    eye:'Mini-leçon', tit:"Quand « il faudrait » n'est pas une suggestion",
    blocs:[
      {t:'texte', h:"La politesse qui fait perdre une consigne",
       p:"« Il faudrait que vous passiez d'autres prélèvements. » Un adulte qui arrive d'ailleurs entend une proposition polie ; ce n'en est pas une. Le français des professionnels adoucit ses consignes — il faudrait, j'aimerais que, il vaudrait mieux —, et cet adoucissement ne retire rien. Reconnaître ces formules, c'est éviter de repartir en croyant qu'on avait le choix.",
       note:"Le programme demande d'« employer obligatoirement le subjonctif présent après quelques verbes introducteurs usuels + que » et de « distinguer un verbe introducteur + de et un verbe introducteur + que »."},

      {t:'ana', h:"Les verbes qui déclenchent le subjonctif",
       p:"Ce sont ceux de la volonté, de l'obligation, du souhait et de la crainte. C'est le verbe qui décide, pas le sens général de la phrase.",
       mots:[["L'obligation","il faut que · il faudrait que · il est nécessaire que · exiger que"],
             ['Le souhait et la préférence',"j'aimerais que · je voudrais que · je préfère que · il vaut mieux que", true],
             ['La crainte',"je crains que · j'ai peur que · j'ai bien peur que"]],
       say:"il faut que, il faudrait que, j'aimerais que, il vaut mieux que, je crains que",
       note:"À l'inverse, « je pense que », « je vois que », « il est certain que » n'appellent pas le subjonctif : ils constatent au lieu de demander."},

      {t:'ana', h:"Comment on le forme",
       p:"Une seule opération, à partir d'une forme que vous connaissez déjà.",
       mots:[['La recette',"la 3e personne du pluriel du présent, moins <b>-ent</b>, plus <b>-e, -es, -e, -ions, -iez, -ent</b>"],
             ['Un exemple',"ils not<s>ent</s> → que je not<b>e</b> · que vous not<b>iez</b> · qu'ils not<b>ent</b>", true],
             ['Ce qui surprend',"à « nous » et « vous », la forme ressemble à l'imparfait : que nous notions, que vous notiez"]],
       say:"que je note, que vous notiez, qu'ils notent, que nous notions",
       note:"Aux trois personnes du singulier et à la troisième du pluriel, le subjonctif des verbes en -er sonne exactement comme le présent. C'est pour ça qu'on ne l'entend pas toujours."},

      {t:'ana', h:"Cinq irréguliers, et ils suffisent",
       p:"Cinq, et ils couvrent presque tout ce que vous entendrez dans un bureau.",
       mots:[['être et avoir',"que je sois, que vous soyez · que j'aie, que vous ayez"],
             ['aller et faire',"que j'aille, que vous alliez · que je fasse, que vous fassiez", true],
             ['pouvoir',"que je puisse, que vous puissiez"]],
       say:"que je sois, que j'aie, que j'aille, que je fasse, que je puisse",
       note:"Apprenez-les avec « que » devant : c'est ainsi qu'ils apparaissent, et jamais autrement."},

      {t:'ex', h:"Sept consignes entendues dans un bureau",
       p:"À gauche, ce qu'on entend ; à droite, ce que ça veut dire pour vous.",
       rows:[
         ["Il faut que vous passiez d'autres prélèvements.","C'est une obligation, dite simplement."],
         ["Il faudrait que vous notiez vos journées.","C'est la même obligation, dite poliment."],
         ["J'aimerais que vous soyez joignable en avant-midi.","On vous demande de répondre au téléphone."],
         ["Il vaut mieux que ce soit court et régulier.","On vous dit comment faire, pas si le faire."],
         ["Je préfère que vous alliez la voir avec la lettre.","On vous indique dans quel ordre faire les choses."],
         ["Je crains qu'elle fasse tout à la dernière minute.","On exprime une inquiétude, pas une consigne."],
         ["Il faut que chacun puisse dire la suite.","On veut que personne ne reparte sans savoir."],
       ]},

      {t:'piege', h:"Trois façons de se tromper",
       rows:[
         ["entendre « il faudrait » comme un conseil facultatif","l'entendre comme « il faut »",
          "Le conditionnel adoucit le ton, il ne retire pas l'obligation. Si vous n'êtes pas sûr, demandez : « est-ce que c'est obligatoire ou est-ce que c'est un conseil ? » La question est parfaitement normale."],
         ["mélanger « demander de » et « demander que »","regarder le mot qui suit",
          "Après <b>de</b>, un infinitif : elle demande de noter. Après <b>que</b>, un subjonctif : elle demande que vous notiez. Les deux phrases sont justes, les deux constructions ne se mélangent pas."],
         ["mettre le subjonctif après « je pense que »","le garder pour la demande",
          "« Je pense que c'est grave » constate ; « je crains que ce soit grave » redoute. Seul le second appelle le subjonctif."],
       ]},

      {t:'check', h:"Quatre questions, pour vérifier",
       p:"Une bonne réponse par question.",
       qs:[
         {q:"« Il faudrait que vous ___ vos journées. »", opts:["notez","notiez"], ok:1,
          fb:"Après « il faudrait que », subjonctif : que vous notiez."},
         {q:"« Il faudrait que » veut dire…", opts:["c'est facultatif","c'est obligatoire, dit poliment"], ok:1,
          fb:"Le conditionnel adoucit le ton et ne retire rien."},
         {q:"« Elle demande ___ noter vos journées. »", opts:["de","que"], ok:0,
          fb:"Après « de », un infinitif. Après « que », il faudrait « que vous notiez »."},
         {q:"Lequel n'appelle pas le subjonctif ?", opts:["je crains que","je pense que"], ok:1,
          fb:"« Je pense que » constate : « je pense que c'est grave »."},
       ]},

      {t:'revoir', h:"Ce qu'il faut garder",
       p:"Après <b>il faut que</b>, <b>il faudrait que</b>, <b>j'aimerais que</b>, <b>il vaut mieux que</b>, <b>je crains que</b> : le subjonctif. Formation : 3e personne du pluriel moins -ent, plus les terminaisons. Cinq irréguliers : <b>sois, aie, aille, fasse, puisse</b>. Et « il faudrait » est une obligation, pas une suggestion."},
    ]
  },

  t2exempl: {
    eye:'Mini-leçon', tit:"Annoncer son exemple",
    blocs:[
      {t:'texte', h:"Pourquoi un exemple doit être présenté",
       p:"« Notez ce qui a changé, l'heure où vous devez vous asseoir. » Le lecteur hésite : est-ce que c'est la seule chose à noter ? « Notez ce qui a changé, par exemple l'heure où vous devez vous asseoir. » Deux mots, et l'hésitation disparaît. Un exemple non annoncé se prend pour la règle, et une règle sans exemple ne se retient pas.",
       note:"Le programme demande d'« employer des connecteurs d'exemplification et d'illustration courants »."},

      {t:'ana', h:"Les cinq qu'il faut avoir",
       p:"Ils ne se remplacent pas tout à fait l'un l'autre : chacun a sa place dans la phrase et son degré de formalité.",
       mots:[['par exemple',"le passe-partout, entre virgules, à peu près partout dans la phrase"],
             ['comme',"collé au nom, sans virgule : un examen <b>comme</b> une prise de sang", true],
             ['notamment, entre autres, ainsi',"plus écrits ; « ainsi » ouvre la phrase suivante et se fait suivre d'une virgule"]],
       say:"par exemple, comme, notamment, entre autres, ainsi",
       note:"« Entre autres » suppose une liste plus longue qu'on ne cite pas ; « notamment » désigne un élément qu'on veut faire ressortir. La nuance est mince et personne ne vous en tiendra rigueur."},

      {t:'ana', h:"Où chacun se place",
       p:"C'est la place, plus que le sens, qui les distingue.",
       mots:[['Au milieu, entre virgules',"Notez tout, <b>par exemple</b> l'heure du lever."],
             ['Collé au nom, sans virgule',"des examens <b>comme</b> une échographie ou une prise de sang", true],
             ['En tête de la phrase suivante',"Tout ce qui se prend compte. <b>Ainsi</b>, les vitamines comptent aussi."]],
       say:"Notez tout, par exemple l'heure du lever. Des examens comme une échographie. Ainsi, les vitamines comptent aussi.",
       note:"« Par exemple » peut aussi ouvrir une phrase : « Par exemple, notez l'heure du lever. » C'est le seul des cinq à être aussi souple."},

      {t:'ana', h:"Ne pas le confondre avec « c'est-à-dire »",
       p:"Deux gestes différents, que beaucoup d'adultes mélangent longtemps.",
       mots:[["L'exemple donne un cas parmi d'autres","des examens, <b>par exemple</b> une prise de sang — il y en a d'autres"],
             ["« c'est-à-dire » redit la même chose autrement","une anémie, <b>c'est-à-dire</b> un sang qui transporte moins bien l'oxygène", true],
             ['Le test',"si l'on peut remplacer par « autrement dit », c'est « c'est-à-dire » ; sinon, c'est un exemple"]],
       say:"des examens, par exemple une prise de sang ; une anémie, c'est-à-dire un sang qui transporte moins bien l'oxygène",
       note:"« C'est-à-dire » est le mot le plus utile de tous quand on cherche à se faire comprendre : il permet de redire ce qu'on vient de dire, en plus simple."},

      {t:'ex', h:"Six phrases du dossier",
       p:"Le connecteur, et pourquoi celui-là.",
       rows:[
         ["Notez ce qui a changé, par exemple l'heure du lever.","le passe-partout, au milieu de la phrase"],
         ["Certains examens se font sans rendez-vous, comme une prise de sang.","collé au nom, sans virgule"],
         ["Apportez tout ce qui vient d'ailleurs, notamment les résultats privés.","on fait ressortir un élément précis"],
         ["Le feuillet répond à plusieurs questions, entre autres celle des heures de visite.","la liste est plus longue qu'on ne le dit"],
         ["Tout ce qui se prend compte. Ainsi, les vitamines comptent aussi.","ouvre la phrase suivante, ton plus soutenu"],
         ["Une anémie légère, c'est-à-dire un sang qui transporte moins bien l'oxygène.","ce n'est pas un exemple : c'est la même chose autrement"],
       ]},

      {t:'piege', h:"Deux confusions et une habitude à prendre",
       rows:[
         ["employer « par exemple » pour reformuler","employer « c'est-à-dire »",
          "« Une anémie, par exemple un sang qui transporte moins bien l'oxygène » laisse croire qu'il y a d'autres anémies possibles. Ce n'est pas un cas parmi d'autres, c'est la définition."],
         ["mettre une virgule après « comme »","le coller au nom",
          "« un examen comme, une prise de sang » coupe la phrase en deux. « Comme » ne s'isole jamais entre virgules."],
         ["donner un adjectif et s'arrêter là","ajouter par exemple et une scène",
          "Chaque fois que vous employez « fatiguée », « essoufflée », « étourdie », enchaînez avec « par exemple » et une situation. C'est ce qui transforme une plainte en renseignement."],
       ]},

      {t:'check', h:"Trois questions, pour vérifier",
       p:"Une bonne réponse par question.",
       qs:[
         {q:"« Une anémie, ___ un sang qui transporte moins bien l'oxygène. »", opts:["par exemple","c'est-à-dire"], ok:1,
          fb:"On redit la même chose autrement : c'est une définition, pas un exemple."},
         {q:"Lequel se colle au nom, sans virgule ?", opts:["comme","notamment"], ok:0,
          fb:"« un examen comme une prise de sang » : aucune virgule."},
         {q:"Lequel ouvre la phrase suivante ?", opts:["ainsi","entre autres"], ok:0,
          fb:"« Ainsi, les vitamines comptent aussi. » — en tête, suivi d'une virgule."},
       ]},

      {t:'revoir', h:"Ce qu'il faut garder",
       p:"<b>par exemple</b> (partout, entre virgules) · <b>comme</b> (collé au nom) · <b>notamment</b> et <b>entre autres</b> (plus écrits) · <b>ainsi</b> (en tête de phrase). Et <b>c'est-à-dire</b> n'est pas un exemple : il redit la même chose autrement."},
    ]
  },

  t3feuillet: {
    eye:'Mini-leçon', tit:"Lire une feuille qui vous demande quelque chose",
    blocs:[
      {t:'texte', h:"Trois parties, et une seule vous concerne vraiment",
       p:"Un feuillet d'information ressemble à un texte, mais ce n'en est pas un : c'est une liste déguisée. Il est fait pour être parcouru en trente secondes par quelqu'un d'inquiet, et non lu ligne à ligne par quelqu'un de reposé. Le lire comme un texte, du début à la fin, est la meilleure façon de manquer les trois endroits qui vous demandent quelque chose.",
       note:"L'intention du programme est « comprendre de l'information sur un problème de santé ». Un feuillet de procédure en fait partie : c'est le premier écrit qu'on vous remet."},

      {t:'ana', h:"Les trois endroits à trouver en premier",
       p:"Toujours les mêmes, sur n'importe quel feuillet, dans n'importe quel établissement.",
       mots:[['« Avant »',"ce qu'il faut apporter et préparer — la seule partie qui se fait la veille"],
             ['« Après »',"ce qu'on vous remet, et ce que vous en faites", true],
             ['Un numéro de téléphone',"souvent en bas ou dans un encadré ; c'est ce qu'on cherche à sept heures du soir"]],
       say:"avant, après, un numéro de téléphone",
       note:"Le reste — la présentation du service, les horaires, l'historique — est là pour rassurer. Ce n'est pas inutile, mais ce n'est pas ce qui vous demande d'agir."},

      {t:'ana', h:"Comment un feuillet est construit",
       p:"Quatre marques visuelles, et chacune veut dire quelque chose.",
       mots:[["Les titres en gras","découpent le temps : avant, pendant, après, si quelque chose ne va pas"],
             ["Les listes à puces ou à tirets","ce qu'il faut faire, un élément par ligne — comptez-les", true],
             ["L'encadré","ce qu'il ne faut surtout pas manquer : un numéro, une date, une condition"]],
       say:"les titres en gras, les listes à tirets, l'encadré",
       note:"Si vous ne lisez qu'une chose sur une page administrative, lisez ce qui est entouré d'un trait. C'est vrai d'un feuillet comme d'un avis."},

      {t:'ana', h:"Ce qu'un bon feuillet ne fait pas",
       p:"Savoir ce qu'il ne contient pas évite d'y chercher ce qui n'y est pas.",
       mots:[["Il ne parle pas de vous","il décrit un fonctionnement, valable pour tout le monde"],
             ["Il ne donne pas de résultat","aucun chiffre vous concernant n'y figure jamais", true],
             ["Il ne remplace pas une question","tout ce qui n'y est pas se demande au numéro qui y est écrit"]],
       say:"il ne parle pas de vous, il ne donne pas de résultat, il ne remplace pas une question",
       note:"C'est pour ça qu'un feuillet se garde des années : rien dedans ne périme, sauf le numéro de téléphone."},

      {t:'ex', h:"Cinq questions à poser à un feuillet",
       p:"Dans cet ordre, la première fois qu'on l'ouvre.",
       rows:[
         ["Qu'est-ce qu'on me demande d'apporter ?","le paragraphe « avant »"],
         ["Qu'est-ce qu'on me demande de préparer ?","souvent la même phrase, souvent oubliée"],
         ["Qu'est-ce que je vais recevoir ?","le paragraphe « après »"],
         ["Qui j'appelle, et quand ?","le numéro, avec les heures d'ouverture"],
         ["Où je le range ?","à la vue, jamais dans un tiroir avec les garanties"],
       ]},

      {t:'piege', h:"Trois façons de perdre un feuillet utile",
       rows:[
         ["le lire du début à la fin comme un texte","chercher d'abord « avant », « après » et le numéro",
          "Un feuillet se parcourt. Les trois parties qui vous demandent quelque chose se trouvent en dix secondes quand on sait quoi chercher."],
         ["le ranger avec les papiers importants","le laisser à la vue",
          "Un papier bien rangé est un papier introuvable. Le feuillet sert le soir où une question se pose, pas le jour où l'on classe."],
         ["croire qu'il explique la maladie","aller chercher l'explication ailleurs",
          "Un feuillet de procédure explique comment ça se passe, jamais ce que vous avez. Pour ça, il y a la personne au bout du numéro."],
       ]},

      {t:'check', h:"Trois questions, pour vérifier",
       p:"Une bonne réponse par question.",
       qs:[
         {q:"Sur un feuillet, où trouve-t-on ce qu'il faut apporter ?", opts:["dans le paragraphe « avant »","dans la présentation du service"], ok:0,
          fb:"« Avant » est la seule partie qui se fait la veille."},
         {q:"Un encadré contient…", opts:["l'historique du service","ce qu'il ne faut surtout pas manquer"], ok:1,
          fb:"Un numéro, une date, une condition : ce qu'on entoure d'un trait est ce qui compte."},
         {q:"Un feuillet d'information explique…", opts:["ce que vous avez","comment ça se passe ici"], ok:1,
          fb:"C'est un feuillet de procédure. Ce qui vous concerne est dans le compte rendu, pas ici."},
       ]},

      {t:'revoir', h:"Ce qu'il faut garder",
       p:"Trois endroits à trouver tout de suite : <b>avant</b>, <b>après</b>, et le <b>numéro de téléphone</b>. Les titres découpent le temps, les tirets comptent les gestes, l'encadré porte l'essentiel. Et un feuillet se garde <b>à la vue</b>."},
    ]
  },

  t3compte: {
    eye:'Mini-leçon', tit:"Lire une lettre qui n'est pas écrite pour vous",
    blocs:[
      {t:'texte', h:"Deux médecins qui se parlent, et vous en avez la copie",
       p:"Un compte rendu de consultation ne vous est pas adressé : il va du spécialiste au médecin qui a fait la demande. Vous en recevez une copie parce que c'est votre dossier. C'est ce qui explique le vocabulaire : ce n'est pas de la condescendance, c'est une langue de métier, écrite pour être courte et pour vouloir dire la même chose partout au pays.",
       note:"Le programme demande de « comprendre des textes expressifs, informatifs, injonctifs, narratifs, descriptifs ». Une lettre professionnelle en est un, et pas le plus facile."},

      {t:'ana', h:"Les sept parties, toujours dans le même ordre",
       p:"Repérez-les une fois, et tous les comptes rendus que vous recevrez dans votre vie se liront pareil.",
       mots:[["L'en-tête et la date","d'où vient la lettre, et quand elle a été écrite"],
             ["À qui elle est adressée","le médecin qui a fait la demande, nommé par son nom", true],
             ['Qui est vu, et pourquoi',"votre nom, votre âge, votre métier, et le motif de la consultation"]],
       say:"l'en-tête et la date, à qui elle est adressée, qui est vu et pourquoi",
       note:"Votre métier figure dans la lettre parce qu'il compte : une fatigue chez une aide à domicile qui monte des escaliers toute la journée ne se lit pas comme une fatigue chez quelqu'un d'assis."},

      {t:'ana', h:"Les quatre parties suivantes",
       p:"Ce sont celles qui portent l'information, et la quatrième est la seule qui vous demande quelque chose.",
       mots:[["Ce que la personne a raconté","souvent introduit par « la patiente rapporte » — ce sont vos mots, traduits"],
             ["Ce qui a été observé ou relevé","les résultats, les mesures, ce qui vient d'ailleurs que de vous", true],
             ["La conduite proposée, puis ce qui reste à décider","le plan, souvent à tirets ; et ce qu'on ne sait pas encore"]],
       say:"la patiente rapporte, ce qui a été observé, la conduite proposée",
       note:"« La patiente rapporte » n'est pas une mise en doute : c'est la façon de distinguer ce que vous avez dit de ce que le médecin a constaté lui-même. Les deux comptent, pas de la même façon."},

      {t:'ana', h:"Trois formules à décoder",
       p:"Elles reviennent dans presque toutes les lettres, et elles se comprennent une fois pour toutes.",
       mots:[["« d'étiologie à préciser »","on ne connaît pas encore la cause, et on la cherche"],
             ["« sera revue à la clinique externe »","c'est décidé, écrit au futur parce que l'administration écrit ainsi", true],
             ["« aucun diagnostic retenu à ce stade »","on refuse de nommer trop vite, et c'est une protection"]],
       say:"d'étiologie à préciser, sera revue à la clinique externe, aucun diagnostic retenu à ce stade",
       note:"Ces trois formules disent ce qu'on ne sait pas ou ce qui est décidé. Une lettre qui les emploie est une lettre honnête, pas une lettre évasive."},

      {t:'ex', h:"Six lignes et leur traduction",
       p:"À gauche, ce que la lettre écrit ; à droite, ce que ça veut dire.",
       rows:[
         ["Motif de la consultation","pourquoi vous avez été envoyée"],
         ["La patiente rapporte…","voici ce que vous avez raconté"],
         ["d'étiologie à préciser","on ne sait pas encore pourquoi"],
         ["Conduite proposée","voici le plan, en autant d'étapes qu'il y a de tirets"],
         ["sera revue à la clinique externe","on vous rappellera : c'est décidé"],
         ["aucun diagnostic retenu à ce stade","on ne met pas de nom là-dessus aujourd'hui"],
       ]},

      {t:'piege', h:"Trois lectures qui font mal pour rien",
       rows:[
         ["lire « aucun diagnostic » comme un échec","le lire comme une prudence",
          "Une lettre qui ne nomme rien dit que la recherche continue. Un nom posé trop vite est beaucoup plus difficile à retirer d'un dossier qu'à y mettre."],
         ["chercher son cas dans le vocabulaire savant","chercher le paragraphe « conduite proposée »",
          "C'est le seul qui vous demande quelque chose. Le reste est du renseignement entre professionnels, et vous pouvez le faire traduire."],
         ["ne pas oser demander la traduction d'un mot","la demander à la liaison ou à son médecin",
          "Traduire ces mots-là fait partie du travail de quelqu'un, quelque part dans l'établissement. Ce n'est ni une faveur ni un aveu."],
       ]},

      {t:'check', h:"Quatre questions, pour vérifier",
       p:"Une bonne réponse par question.",
       qs:[
         {q:"À qui un compte rendu de consultation est-il adressé ?", opts:["au patient","au médecin qui a fait la demande"], ok:1,
          fb:"Vous en avez une copie parce que c'est votre dossier, pas parce qu'il vous est adressé."},
         {q:"« La patiente rapporte » introduit…", opts:["ce que le médecin a constaté","ce que la personne a raconté"], ok:1,
          fb:"C'est ainsi qu'on distingue votre récit des observations du médecin."},
         {q:"« Sera revue à la clinique externe » veut dire…", opts:["c'est peut-être prévu","c'est décidé"], ok:1,
          fb:"Le futur simple, dans un document, écrit une décision et non une possibilité."},
         {q:"Quel paragraphe vous demande quelque chose ?", opts:["la conduite proposée","le motif de la consultation"], ok:0,
          fb:"Le plan, souvent présenté à tirets. Comptez-les : vous saurez ce qu'on attend de vous."},
       ]},

      {t:'revoir', h:"Ce qu'il faut garder",
       p:"Sept parties, toujours dans le même ordre. Celle qui vous concerne est la <b>conduite proposée</b>. Trois formules à connaître : <b>d'étiologie à préciser</b> (on cherche), <b>sera revue</b> (c'est décidé), <b>aucun diagnostic retenu à ce stade</b> (on ne nomme pas trop vite). Et la traduction se demande."},
    ]
  },

  t3mots: {
    eye:'Mini-leçon', tit:"Le même sens, deux vocabulaires",
    blocs:[
      {t:'texte', h:"Ce n'est pas une autre information, c'est une traduction",
       p:"Leyla lit « fatigue persistante d'apparition progressive » et se demande qui a dit ça. C'est elle. « Ça ne part pas » est devenu « persistante » ; « au début, je pensais que c'était l'hiver » est devenu « d'apparition progressive ». Rien n'a été ajouté et rien n'a été retiré : le même contenu a changé de vocabulaire, comme on change de vêtement pour aller quelque part.",
       note:"Le programme parle d'« exploiter des champs lexicaux pour exprimer le détail ou la nuance » et d'« employer des synonymes de mots en rapport avec le vocabulaire courant »."},

      {t:'ana', h:"Ce que le vocabulaire du dossier fait au vôtre",
       p:"Trois opérations, toujours les mêmes.",
       mots:[['Il condense',"« ça ne part pas depuis huit mois » → <b>persistante</b>"],
             ['Il date sans dire de date',"« au début je pensais que c'était l'hiver » → <b>d'apparition progressive</b>", true],
             ['Il mesure',"« je montais l'escalier en parlant » → <b>tolérance à l'effort</b>"]],
       say:"persistante, d'apparition progressive, tolérance à l'effort",
       note:"Ces mots-là ne sont pas plus savants : ils sont plus courts, et ils veulent dire la même chose pour tous les professionnels du pays. C'est leur seule raison d'être."},

      {t:'ana', h:"Les paires les plus utiles à connaître",
       p:"Elles reviendront dans tous les documents que vous recevrez.",
       mots:[["« ça dure » → chronique, persistant","« ça revient » → récidivant, à répétition"],
             ["« petit à petit » → progressif","« d'un coup » → brutal, soudain", true],
             ["« on ne sait pas pourquoi » → d'étiologie à préciser","« ça n'a pas de nom encore » → sans diagnostic retenu"]],
       say:"chronique, persistant, progressif, brutal, d'étiologie à préciser",
       note:"Apprenez-les en paires, jamais seules : c'est le mot courant qui vous fera retrouver le mot savant, et non l'inverse."},

      {t:'ana', h:"Et dans l'autre sens",
       p:"Savoir traduire du dossier vers la parole est aussi utile — c'est ce que vous ferez ce soir au téléphone.",
       mots:[["« persistante »","« ça ne part pas »"],
             ["« réduction de la tolérance à l'effort »","« je suis essoufflée plus vite qu'avant »", true],
             ["« réévaluation à la réception des résultats »","« elle me rappelle quand elle aura les résultats »"]],
       say:"ça ne part pas, je suis essoufflée plus vite qu'avant, elle me rappelle quand elle aura les résultats",
       note:"Un mot qu'on peut redire dans sa propre langue courante est un mot compris. Un mot qu'on ne peut que répéter ne l'est pas encore."},

      {t:'ex', h:"Sept traductions, dans les deux sens",
       p:"À gauche, ce que Leyla a dit ; à droite, ce que la lettre écrit.",
       rows:[
         ["Je suis fatiguée et ça ne part pas.","fatigue persistante"],
         ["Au début, je pensais que c'était l'hiver.","d'apparition progressive"],
         ["Avant, je montais l'escalier en parlant.","réduction de la tolérance à l'effort"],
         ["On ne sait pas encore pourquoi.","d'étiologie à préciser"],
         ["Elle me rappelle quand elle aura les résultats.","réévaluation à la réception des résultats"],
         ["Elle n'a pas voulu me donner de réponse aujourd'hui.","aucun diagnostic retenu à ce stade"],
         ["Je note mes journées sur une feuille.","relevé quotidien tenu par la patiente"],
       ]},

      {t:'piege', h:"Trois réactions à éviter",
       rows:[
         ["croire qu'on a dit autre chose que ce qu'on a dit","chercher sa propre phrase dessous",
          "Neuf fois sur dix, chaque groupe de mots savants correspond à une phrase que vous avez prononcée. Cherchez-la : vous la trouverez."],
         ["adopter le vocabulaire du dossier pour parler à ses proches","garder ses mots à soi",
          "Dire « j'ai une réduction de la tolérance à l'effort » à sa sœur ne communique rien. Les mots de la lettre servent au laboratoire ; les vôtres servent à votre monde."],
         ["se taire devant un mot inconnu","le faire traduire",
          "Un mot qu'on n'ose pas demander reste toute la vie. Et c'est le travail de quelqu'un, dans l'établissement, de vous le traduire."],
       ]},

      {t:'check', h:"Trois questions, pour vérifier",
       p:"Une bonne réponse par question.",
       qs:[
         {q:"« Fatigue persistante » reprend quelle phrase ?", opts:["« je suis fatiguée et ça ne part pas »","« je suis fatiguée le samedi »"], ok:0,
          fb:"Persistante condense « ça dure et ça ne part pas »."},
         {q:"« D'apparition progressive » veut dire…", opts:["c'est arrivé d'un coup","c'est venu petit à petit"], ok:1,
          fb:"Le contraire serait « brutal » ou « soudain »."},
         {q:"Pour parler à sa sœur, il vaut mieux…", opts:["employer les mots de la lettre","employer ses mots à soi"], ok:1,
          fb:"Les mots du dossier servent entre professionnels ; ils ne communiquent rien à la maison."},
       ]},

      {t:'revoir', h:"Ce qu'il faut garder",
       p:"Le vocabulaire du dossier <b>condense</b>, <b>date</b> et <b>mesure</b> ce que vous avez dit. Apprenez les paires dans les deux sens : « ça dure » ↔ <b>chronique</b>, « petit à petit » ↔ <b>progressif</b>, « on ne sait pas pourquoi » ↔ <b>d'étiologie à préciser</b>. Et gardez vos mots pour vos proches."},
    ]
  },

  t3nom: {
    eye:'Mini-leçon', tit:"Faire un nom avec un verbe",
    blocs:[
      {t:'texte', h:"Le procédé qui rend les documents difficiles",
       p:"« Il a fallu attendre sept mois » se dit. « Cette attente a duré sept mois » s'écrit. Le contenu est identique ; ce qui change, c'est qu'un verbe est devenu un nom. Tous les documents administratifs fonctionnent ainsi, et c'est la seule raison pour laquelle ils paraissent difficiles à quelqu'un qui parle déjà très bien. Ce n'est pas du vocabulaire nouveau : ce sont des mots que vous connaissez, habillés autrement.",
       note:"Le programme le nomme : « exploiter les familles de mots pour la nominalisation ou l'adjectivation : la vie familiale : la vie de famille ; il fait de la fièvre : il est fiévreux »."},

      {t:'ana', h:"À quoi ça sert vraiment",
       p:"Deux services, et le second est celui qui compte au niveau 6.",
       mots:[['Écrire court',"« on a prélevé du sang en mars » → « le prélèvement de mars »"],
             ['Reprendre sans répéter',"« il a fallu attendre. <b>Cette attente</b> l'a découragée. »", true],
             ['Ce que ça permet',"passer d'une phrase à un groupe de mots qu'on peut déplacer dans la phrase suivante"]],
       say:"le prélèvement de mars, cette attente l'a découragée",
       note:"C'est le lien direct avec le Défi 1 : la nominalisation est l'un des trois moyens de reprendre un référent sans le répéter."},

      {t:'ana', h:"Les terminaisons qui se devinent",
       p:"Elles couvrent la grande majorité des cas et se devinent une fois qu'on les a vues.",
       mots:[['-ment',"prélever → le prélève<b>ment</b> · changer → le change<b>ment</b> · traiter → le traite<b>ment</b>"],
             ['-tion, -sion',"consulter → la consulta<b>tion</b> · apparaître → l'appari<b>tion</b> · décider → la déci<b>sion</b>", true],
             ['-ure, -age, -ité',"ouvrir → l'ouvert<b>ure</b> · dépister → le dépist<b>age</b> · fatigué → la fatigabil<b>ité</b>"]],
       say:"le prélèvement, la consultation, l'apparition, l'ouverture",
       note:"Devinez d'abord, vérifiez ensuite. Un nom en -ment ou en -tion tiré d'un verbe que vous connaissez a de bonnes chances d'exister."},

      {t:'ana', h:"Les irrégulières, qui s'apprennent en paires",
       p:"Aucune règle ne les donne. Il y en a peu, elles sont fréquentes, et elles se retiennent en une soirée.",
       mots:[['attendre → l'+"'"+'attente',"répondre → la réponse · suivre → le suivi"],
             ['partir → le départ',"venir → la venue · vivre → la vie · mourir → la mort", true],
             ["choisir → le choix","souffrir → la souffrance · guérir → la guérison"]],
       say:"l'attente, la réponse, le suivi, le départ, le choix",
       note:"Notez-les par deux, jamais seules. « Attendre / l'attente » est un seul objet à mémoriser ; « l'attente » toute seule n'accroche à rien."},

      {t:'ana', h:"Et l'adjectif tiré du nom",
       p:"Le programme le demande dans la même ligne, et l'exemple qu'il donne est justement médical.",
       mots:[["la fièvre → fiévreux, fiévreuse","« elle fait de la fièvre » → « elle est fiévreuse »"],
             ["le cœur → cardiaque","« un problème du cœur » → « un problème cardiaque »", true],
             ["des mois → chronique","« ça dure depuis des mois » → « c'est chronique »"]],
       say:"elle est fiévreuse, un problème cardiaque, c'est chronique",
       note:"Attention aux adjectifs médicaux tirés du grec ou du latin : ils ne ressemblent pas au nom français. Cœur donne cardiaque, poumon donne pulmonaire, rein donne rénal."},

      {t:'ex', h:"Huit paires du dossier",
       p:"Le verbe ou l'adjectif, puis le nom.",
       rows:[
         ["attendre","l'attente"],
         ["prélever","le prélèvement"],
         ["consulter","la consultation"],
         ["suivre","le suivi"],
         ["répondre","la réponse"],
         ["apparaître","l'apparition"],
         ["arriver en retard","le retard"],
         ["ne pas savoir","l'incertitude"],
       ]},

      {t:'piege', h:"Trois pièges de la nominalisation",
       rows:[
         ["inventer un nom en -ment quand il n'existe pas","vérifier les six irrégulières",
          "« L'attendement » n'existe pas, et « le répondement » non plus. Attendre, répondre, suivre, partir, choisir, venir : ces six-là s'apprennent, elles ne se devinent pas."],
         ["se tromper de genre","apprendre le nom avec son article",
          "« Le consultation » sonne faux dès la première syllabe. Retenez « la consultation », « le prélèvement », « l'attente » avec le petit mot devant."],
         ["nominaliser tout ce qu'on écrit","garder les verbes quand on parle",
          "Un courriel à sa sœur écrit en noms devient illisible : « mon attente a duré sept mois et ma consultation a eu lieu le 12 ». Dites plutôt « j'ai attendu sept mois et je l'ai vue le 12 »."],
       ]},

      {t:'check', h:"Quatre questions, pour vérifier",
       p:"Une bonne réponse par question.",
       qs:[
         {q:"Le nom tiré de « attendre » est…", opts:["l'attendement","l'attente"], ok:1,
          fb:"Irrégulier, et à retenir en paire : attendre / l'attente."},
         {q:"Le nom tiré de « prélever » est…", opts:["le prélèvement","la prélevure"], ok:0,
          fb:"Terminaison en -ment, la plus régulière de toutes."},
         {q:"« Elle fait de la fièvre » donne quel adjectif ?", opts:["fiévreuse","fièvreuse"], ok:0,
          fb:"Fiévreuse, avec un accent aigu : l'accent change quand la syllabe change."},
         {q:"Dans un courriel à un proche, il vaut mieux…", opts:["employer des noms","garder les verbes"], ok:1,
          fb:"La nominalisation sert à lire les documents, pas à écrire à sa famille."},
       ]},

      {t:'revoir', h:"Ce qu'il faut garder",
       p:"Régulières : <b>-ment</b> (prélèvement), <b>-tion</b> (consultation), <b>-ure</b> (ouverture). Irrégulières, à apprendre en paires : <b>attendre / l'attente</b>, <b>répondre / la réponse</b>, <b>suivre / le suivi</b>, <b>partir / le départ</b>. Et l'adjectif suit la même logique : la fièvre → <b>fiévreuse</b>."},
    ]
  },

  t3ps: {
    eye:'Mini-leçon', tit:"Le temps des brochures et des romans",
    blocs:[
      {t:'texte', h:"Le seul temps français qu'on vous demande de ne pas apprendre",
       p:"Vous le rencontrerez dans une brochure d'association, dans l'histoire d'une fondation, dans un roman, dans un documentaire. Vous ne l'entendrez jamais dans une conversation et vous ne l'écrirez jamais vous-même. Le programme est explicite là-dessus : le reconnaître à la 3e personne, et savoir à quel passé composé il correspond. Rien de plus, et c'est un soulagement.",
       note:"Le programme du niveau 6 demande de « reconnaître les verbes courants à la 3e personne » et d'« associer le passé simple au passé composé »."},

      {t:'ana', h:"Le texte d'où sortent les exemples",
       p:"Un feuillet de l'association des usagers, posé sur la table de la salle d'attente. C'est exactement le genre d'écrit où l'on tombe dessus.",
       mots:[["Ce que la page montre","« Jeanne Loiselle attendit onze mois son premier rendez-vous. »"],
             ["La suite","« Elle comprit ce jour-là que personne ne l'attendait, elle. »", true],
             ["La fin","« Elle réunit six personnes dans une cuisine et l'association naquit ainsi, en 1979. »"]],
       say:"Jeanne Loiselle attendit onze mois son premier rendez-vous. Elle comprit ce jour-là que personne ne l'attendait, elle. Elle réunit six personnes dans une cuisine et l'association naquit ainsi, en 1979.",
       note:"Lisez-le à voix haute en remplaçant chaque verbe par un passé composé : « elle a attendu », « elle a compris », « elle a réuni », « elle est née ». Le texte ne perd rien."},

      {t:'ana', h:"Trois familles de terminaisons",
       p:"Trois familles, à la 3e personne du singulier et du pluriel — les deux seules que vous croiserez.",
       mots:[["-a et -èrent, pour les verbes en -er","elle not<b>a</b> · ils not<b>èrent</b> · elle arriv<b>a</b> · ils arriv<b>èrent</b>"],
             ["-it et -irent, pour beaucoup d'autres","elle compr<b>it</b> · ils compr<b>irent</b> · elle réun<b>it</b> · elle attend<b>it</b>", true],
             ["-ut et -urent, pour un troisième groupe","il fall<b>ut</b> · ils d<b>urent</b> · elle p<b>ut</b> · ils v<b>oulurent</b>"]],
       say:"elle nota, ils notèrent, elle comprit, ils comprirent, il fallut, ils durent",
       note:"Attention à un faux ami : « elle réunit » s'écrit pareil au présent et au passé simple. C'est le reste de la phrase — et souvent une date — qui tranche."},

      {t:'ana', h:"Les trois qu'on voit partout",
       p:"Apprenez ces trois-là et vous comprendrez la moitié des textes historiques.",
       mots:[["il fut","= il a été · elle fut = elle a été"],
             ["il eut","= il a eu · ils eurent = ils ont eu", true],
             ["il fit","= il a fait · ils firent = ils ont fait"]],
       say:"il fut, il eut, il fit, ils eurent, ils firent",
       note:"Ne les confondez pas avec le subjonctif imparfait — « qu'il fût » — que vous ne rencontrerez à peu près jamais et qu'aucun programme ne demande."},

      {t:'ex', h:"Sept formes et leur équivalent parlé",
       p:"À gauche, ce qui est écrit ; à droite, ce que vous diriez.",
       rows:[
         ["elle attendit onze mois","elle a attendu onze mois"],
         ["elle comprit ce jour-là","elle a compris ce jour-là"],
         ["elle réunit six personnes","elle a réuni six personnes"],
         ["l'association naquit ainsi","l'association est née ainsi"],
         ["les bénévoles se relayèrent","les bénévoles se sont relayés"],
         ["il fallut deux ans","il a fallu deux ans"],
         ["ce fut le premier groupe","ça a été le premier groupe"],
       ]},

      {t:'piege', h:"Trois efforts inutiles",
       rows:[
         ["essayer de le conjuguer","le traduire et continuer à lire",
          "Personne ne vous demandera d'écrire un passé simple. Le temps passé à apprendre ses formes serait mieux employé sur le plus-que-parfait, que vous emploierez tous les jours."],
         ["s'arrêter dessus au milieu d'un texte","le lire comme un passé composé",
          "Dans un document, le passé simple porte le décor et jamais l'information qui vous concerne. Il raconte la fondation de l'association, pas votre rendez-vous."],
         ["le confondre avec le présent","chercher la date",
          "« Elle réunit » peut être un présent ou un passé simple. Dans un récit daté — « en 1979 » —, c'est un passé simple. Le contexte décide toujours."],
       ]},

      {t:'check', h:"Quatre questions, pour vérifier",
       p:"Une bonne réponse par question.",
       qs:[
         {q:"« Elle attendit onze mois » veut dire…", opts:["elle attend onze mois","elle a attendu onze mois"], ok:1,
          fb:"Terminaison -it : un passé, à traduire en passé composé."},
         {q:"« Il fallut deux ans » correspond à…", opts:["il a fallu deux ans","il faudra deux ans"], ok:0,
          fb:"-ut est la troisième famille de terminaisons du passé simple."},
         {q:"Où rencontrerez-vous ce temps ?", opts:["dans un courriel du secrétariat","dans une brochure d'association"], ok:1,
          fb:"Brochures, romans, documentaires, histoires de fondation. Jamais dans une lettre qui vous demande quelque chose."},
         {q:"Le programme demande de…", opts:["le reconnaître","l'écrire correctement"], ok:0,
          fb:"Reconnaître à la 3e personne, et associer au passé composé. Rien de plus."},
       ]},

      {t:'revoir', h:"Ce qu'il faut garder",
       p:"Trois familles de terminaisons : <b>-a / -èrent</b>, <b>-it / -irent</b>, <b>-ut / -urent</b>. Trois formes à connaître : <b>il fut</b>, <b>il eut</b>, <b>il fit</b>. On le traduit en passé composé dans sa tête et on continue à lire — on ne l'écrit jamais."},
    ]
  },

  t3ponct: {
    eye:'Mini-leçon', tit:"Trois signes qui portent du sens",
    blocs:[
      {t:'texte', h:"Un texte administratif ne souligne rien : il ponctue",
       p:"Cherchez du gras dans un compte rendu : vous n'en trouverez pas. Cherchez des mots soulignés : pas davantage. Tout ce qu'un autre lecteur voit tout de suite est porté par la ponctuation — un tiret qui ouvre une étape, deux virgules qui encadrent un ajout, des guillemets qui prennent leurs distances. Sauter les signes, c'est perdre exactement ce que le document met en évidence.",
       note:"Le programme du niveau 6 demande de « comprendre l'utilisation du tiret », d'« employer la virgule pour encadrer un GN détaché » et d'« employer les guillemets pour encadrer un mot que l'on désire souligner ou nuancer »."},

      {t:'ana', h:"Le tiret — deux emplois, un seul signe",
       p:"C'est la place dans la page qui distingue les deux, jamais la forme du trait.",
       mots:[["En début de ligne, il énumère","Conduite proposée : — de nouveaux prélèvements ; — un relevé quotidien ; — une réévaluation."],
             ["Dans un dialogue, il change de personne","— Vous attendez depuis longtemps ? — Depuis neuf heures et demie.", true],
             ["Ce qu'il faut en faire dans un document","les compter : autant de tirets, autant de choses attendues de vous"]],
       say:"de nouveaux prélèvements, un relevé quotidien, une réévaluation",
       note:"C'est le réflexe le plus rentable de tout le module : devant un compte rendu, comptez les tirets du paragraphe « conduite proposée » avant de lire quoi que ce soit d'autre."},

      {t:'ana', h:"La virgule — celle qui encadre un ajout",
       p:"Deux virgules autour d'un groupe détaché : on ajoute un renseignement sans casser la phrase.",
       mots:[["Ce que ça donne","Madame Demirci, 41 ans, a été vue ce jour."],
             ["Un autre exemple","La patiente, aide à domicile, travaille le matin.", true],
             ["Un test qui tranche à tout coup","retirez ce qui est entre les deux virgules : si la phrase tient encore, c'était bien un ajout"]],
       say:"Madame Demirci, 41 ans, a été vue ce jour. La patiente, aide à domicile, travaille le matin.",
       note:"Deux virgules, jamais une. Une virgule seule au milieu d'un groupe détaché est la faute la plus fréquente à l'écrit, à tous les niveaux."},

      {t:'ana', h:"Les guillemets — prendre ses distances",
       p:"Ils encadrent un mot qu'on cite ou dont on se méfie. Dans un document professionnel, c'est presque toujours le premier cas.",
       mots:[["Citer le mot de quelqu'un d'autre","Elle a dit se sentir « correcte »."],
             ["Nuancer un mot qu'on n'assume pas","Un examen dit « de routine ».", true],
             ["Ce que ça vous apprend","celui qui écrit ne reprend pas le mot à son compte : il le rapporte"]],
       say:"Elle a dit se sentir « correcte ». Un examen dit « de routine ».",
       note:"En français, les guillemets sont des chevrons — « » — et ils portent une espace à l'intérieur, de chaque côté. Les guillemets droits de l'anglais s'emploient de plus en plus, mais l'usage soigné garde les chevrons."},

      {t:'ex', h:"Six emplois et leur travail",
       p:"Le signe, et ce qu'il fait à cet endroit.",
       rows:[
         ["Conduite proposée : — de nouveaux prélèvements","le tiret ouvre une étape du plan"],
         ["— Vous attendez depuis longtemps ?","le tiret change de personne qui parle"],
         ["Madame Demirci, 41 ans, a été vue.","les virgules encadrent un ajout"],
         ["La patiente, aide à domicile, travaille le matin.","les virgules encadrent un ajout"],
         ["Elle a dit se sentir « correcte ».","les guillemets citent le mot de quelqu'un"],
         ["Un examen dit « de routine ».","les guillemets nuancent un mot"],
       ]},

      {t:'piege', h:"Trois habitudes à corriger",
       rows:[
         ["mettre une seule virgule autour d'un ajout","en mettre deux, ou aucune",
          "« Madame Demirci, 41 ans a été vue » se lit mal : le lecteur cherche où l'ajout se termine. Les deux virgules travaillent ensemble, comme deux parenthèses."],
         ["lire un paragraphe à tirets comme un texte suivi","compter les tirets",
          "Chaque tiret est une étape, et le nombre de tirets est le nombre de choses attendues de vous. C'est l'information la plus utile de la page, et elle se lit sans lire."],
         ["prendre les guillemets pour de l'ironie","les lire comme une mise à distance",
          "« Elle a dit se sentir " + '« correcte »' + " » n'est pas moqueur : c'est la façon d'écrire que ce mot est le sien, et non celui du médecin."],
       ]},

      {t:'check', h:"Quatre questions, pour vérifier",
       p:"Une bonne réponse par question.",
       qs:[
         {q:"Dans un compte rendu, compter les tirets sert à…", opts:["savoir combien de choses on attend de vous","savoir la longueur du texte"], ok:0,
          fb:"Un tiret, une étape. C'est le réflexe le plus rentable devant un document."},
         {q:"Combien de virgules encadrent un groupe détaché ?", opts:["une","deux"], ok:1,
          fb:"Deux, comme deux parenthèses. Une seule laisse la phrase ouverte."},
         {q:"« Elle a dit se sentir « correcte » » : les guillemets disent que…", opts:["le médecin trouve le mot ridicule","le mot est celui de la patiente"], ok:1,
          fb:"C'est une mise à distance, pas une moquerie."},
         {q:"Le tiret sert aussi, ailleurs, à…", opts:["marquer le changement de personne dans un dialogue","séparer deux paragraphes"], ok:0,
          fb:"Deux emplois pour un seul signe : la place dans la page les distingue."},
       ]},

      {t:'revoir', h:"Ce qu'il faut garder",
       p:"Le <b>tiret</b> énumère les étapes d'un plan et change de personne dans un dialogue. Les <b>deux virgules</b> encadrent un ajout qu'on pourrait retirer. Les <b>guillemets</b> disent que le mot est celui de quelqu'un d'autre. Devant un document : comptez d'abord les tirets."},
    ]
  },
};
