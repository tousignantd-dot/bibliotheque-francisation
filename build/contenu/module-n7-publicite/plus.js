const PLUS = {

  prDebit: {
    eye:'Mini-leçon', tit:"Le « e » que la vitesse fait disparaître",
    blocs:[
      {t:'texte', h:"Le seul son du français qui a le droit de ne pas se dire",
       p:"Il y a dans le français un petit son qui tantôt se dit, tantôt ne se dit pas : le « e » de <i>semaine</i>, de <i>rapidement</i>, de <i>depuis</i>. Ce ne sont pas deux façons de parler, l'une soignée et l'autre relâchée. Ce sont deux prononciations également correctes, et c'est la place du « e » dans le mot qui décide, pas le niveau de langue.",
       note:"On l'appelle le <b>e caduc</b> — « caduc » veut dire « qui tombe ». Il s'écrit <b>[ə]</b>."},

      {t:'texte', h:"Pourquoi cette leçon est dans un module sur la publicité",
       p:"Une capsule de radio finit par cinq secondes dites deux fois plus vite que le reste. À cette vitesse-là, tous les « e » qui peuvent tomber tombent : <i>gratuitement</i> devient <i>gratuit'ment</i>, <i>la semaine</i> devient <i>la s'maine</i>. Vous connaissez très bien ces mots — et vous ne les reconnaissez pas. Ce n'est pas un manque de vocabulaire, c'est un manque d'entraînement à la forme courte.",
       note:"On croit alors avoir manqué du vocabulaire, alors qu'on a manqué une syllabe."},

      {t:'ana', h:"Il tient — quand le mot commence par p, b, t, d, k, g",
       p:"Dans la <b>première syllabe</b>, après une consonne qui ferme complètement la bouche, le « e » reste.",
       mots:[['On écrit','d{e}puis · d{e}vant · t{e}nir · d{e}bout'],['On entend','le [ə] est bien là',true],['Le repère','la bouche se ferme, puis le « e » sort']],
       say:"depuis, devant, tenir, debout",
       note:"Ces six consonnes ferment complètement la bouche avant de la rouvrir : le « e » sort dans ce relâchement."},

      {t:'ana', h:"Il tient — quand deux consonnes le précèdent",
       p:"S'il fallait le laisser tomber, trois consonnes se suivraient et le mot deviendrait impossible à dire.",
       mots:[['On écrit','autr{e}ment · le pr{e}mier · vendr{e}di · un appart{e}ment'],['On entend','le [ə] est bien là',true],['La règle','deux consonnes devant, il reste']],
       say:"autrement, le premier, vendredi",
       note:"C'est ce cas qui explique pourquoi <i>autrement</i> garde son « e » alors que <i>rapidement</i> le perd."},

      {t:'ana', h:"Il tient — devant les sons [rj] et [lj]",
       p:"Devant un « ri » ou un « li » suivi d'une voyelle, le « e » ne tombe jamais.",
       mots:[['On écrit','un at{e}lier · un ouvri{e}r · un hôt{e}lier'],['On entend','le [ə] est bien là',true],['Essayez sans','« atlier » : la langue butte']],
       say:"un atelier, un ouvrier",
       note:"Cas rare, mais sans aucune exception."},

      {t:'ana', h:"Il tombe — partout ailleurs, au milieu du mot",
       p:"Quand une seule consonne le précède et qu'on est au milieu du mot, il s'efface dans la conversation normale, et complètement dans un débit rapide.",
       mots:[['On écrit','seul{e}ment · rapid{e}ment · gratuit{e}ment · la s{e}maine · sam{e}di'],['On entend','[sœlmɑ̃] · [ʁapidmɑ̃] · [lasmɛn]',true],['La règle','une seule consonne devant, il tombe']],
       say:"seulement, rapidement, gratuitement, la semaine, samedi",
       note:"C'est la même chose dans <i>un médecin</i> [medsɛ̃] et <i>une boulangerie</i> [bulɑ̃ʒʁi]."},

      {t:'labo', h:"Écoutez la différence",
       p:"Choisissez un cas et un exemple.",
       axes:[
         {id:'c', lbl:'Quel cas ?', opts:[['a','la bouche se ferme'],['b','deux consonnes butent'],['c','un ri ou un li suit'],['d','rien ne le retient']]},
         {id:'n', lbl:'Quel exemple ?', opts:[['1','le premier'],['2','le second']]}],
       out:{
         a1:{w:["depuis"], say:"depuis", n:'« d » est une occlusive : on entend « de-puis »'},
         a2:{w:["devant"], say:"devant", n:'même cas : on entend « de-vant »'},
         b1:{w:["autrement"], say:"autrement", n:'« tr » : deux consonnes, le « e » tient'},
         b2:{w:["le premier"], say:"le premier", n:'« pr » : deux consonnes, le « e » tient'},
         c1:{w:["un atelier"], say:"un atelier", n:'devant [lj], le « e » ne tombe jamais'},
         c2:{w:["un ouvrier"], say:"un ouvrier", n:'devant [rj], même chose'},
         d1:{w:["gratuitement"], say:"gratuitement", n:'une seule consonne : « gratuit\'ment »'},
         d2:{w:["la semaine"], say:"la semaine", n:'on entend « la s\'maine »'},
       },
       note:"Écoutez deux fois, puis répétez à voix haute avant de passer au suivant."},

      {t:'ex', h:"Six mots de la mention légale, à écouter et à répéter",
       p:"À gauche, ce qui est écrit. À droite, ce qui se dit à pleine vitesse.",
       rows:[
         ["seulement","« seul'ment » — le « e » tombe"],
         ["gratuitement","« gratuit'ment » — le « e » tombe"],
         ["rapidement","« rapid'ment » — le « e » tombe"],
         ["depuis","« de-puis » — le « e » se dit"],
         ["autrement","« au-tre-ment » — le « e » se dit"],
         ["un atelier","trois syllabes pleines, le « e » tient"],
       ]},

      {t:'piege', h:"Deux pièges et une bonne nouvelle",
       rows:[
         ["prononcer chaque « e » écrit","laisser tomber ceux du milieu",
          "Dire « ra-pi-de-ment » en quatre morceaux se comprend, mais sonne appliqué et ralentit tout. Personne ne parle comme ça, et surtout pas dans une capsule de trente secondes."],
         ["croire qu'on a manqué un mot","reconnaître le mot amputé",
          "Quand vous entendez [lasmɛn] et que vous cherchez « la semaine », le problème n'est pas votre vocabulaire. Entraînez l'oreille à la forme courte, c'est celle que vous entendrez."],
         ["s'inquiéter de se tromper","aucune des deux formes ne trahit",
          "Garder un « e » qui aurait pu tomber ne provoque aucun malentendu. C'est à l'écoute que ça compte, pas à la production."],
       ]},

      {t:'check', h:"Est-ce que c'est clair maintenant ?",
       p:"Quatre mots, une décision chacun.",
       qs:[
         {q:"Dans « depuis », le « e » de la première syllabe…", opts:["se prononce","tombe"], ok:0,
          fb:"Première syllabe, et « d » est une occlusive : il se maintient."},
         {q:"Dans « gratuitement », le « e » du milieu…", opts:["se prononce","tombe"], ok:1,
          fb:"Une seule consonne devant : on dit « gratuit'ment »."},
         {q:"Dans « autrement », deux consonnes précèdent le « e ». Il…", opts:["se maintient","tombe quand même"], ok:0,
          fb:"Sans lui, « tr » et « m » se suivraient : impossible à dire."},
         {q:"Dans « un atelier », le « e »…", opts:["se prononce","tombe"], ok:0,
          fb:"Devant le son [lj], il ne tombe jamais."},
       ]},

      {t:'revoir', h:"À retenir",
       p:"Début de mot après p, b, t, d, k, g : <b>on l'entend</b>. Deux consonnes devant : <b>on l'entend</b>. Devant [rj] ou [lj] : <b>on l'entend</b>. Partout ailleurs, au milieu du mot : <b>il tombe</b>, et il tombe deux fois plus sûrement quand la voix accélère."},
    ]
  },

  prDit: {
    eye:'Mini-leçon', tit:"Ce qui est promis et ce qui est seulement suggéré",
    blocs:[
      {t:'texte', h:"La seule question qui compte devant une annonce",
       p:"Une publicité contient deux sortes de phrases, et elles ne se ressemblent pas du tout. Les unes affirment quelque chose de vérifiable : un prix, une durée, une quantité, un rang. Les autres donnent une impression : un mieux-être, une confiance, un avenir. Les premières engagent l'annonceur devant la loi ; les secondes ne l'engagent à rien du tout.",
       note:"Savoir les séparer, c'est tout ce que ce module demande. Le reste n'est que de la pratique."},

      {t:'ana', h:"Une affirmation se prouve, donc se conteste",
       p:"Elle porte sur un fait qu'on peut aller vérifier.",
       mots:[['Exemples','« Plus de vingt appareils neufs. » · « Frais de soixante dollars. » · « Le plus grand centre de la région. »'],['Ce qui se passe si c\'est faux','représentation trompeuse, et vous avez un recours',true],['Le signe','un chiffre, un rang, une date, un fait']],
       say:"Plus de vingt appareils neufs. Le plus grand centre de la région.",
       note:"Un superlatif est une affirmation : « le plus grand » se compare à tout le reste, donc se vérifie."},

      {t:'ana', h:"Une suggestion ne se prouve pas, donc ne se conteste pas",
       p:"Elle donne une impression sans jamais affirmer un fait.",
       mots:[['Exemples','« Vos nuits valent mieux que ça. » · « Prenez enfin soin de vous. » · « Un environnement plus chaleureux. »'],['Ce qui se passe si c\'est faux','rien : il n\'y a rien à contredire',true],['Le signe','pas un seul mot vérifiable']],
       say:"Vos nuits valent mieux que ça. Prenez enfin soin de vous.",
       note:"Ce n'est pas illégal. C'est simplement vide, et c'est ce qu'il faut savoir en écoutant."},

      {t:'ex', h:"Les trois mots qui annoncent une suggestion",
       p:"Quand l'un des trois paraît, votre oreille doit se lever.",
       rows:[
         ["pourrait, pourraient","le conditionnel : une possibilité, jamais une promesse"],
         ["jusqu'à","la limite haute, présentée comme si c'était le cas ordinaire"],
         ["plus, sans deuxième terme","un comparatif que vous compléterez vous-même"],
       ]},

      {t:'check', h:"À vous",
       p:"Affirmé, ou suggéré ?",
       qs:[
         {q:"« Nos entraîneurs pourraient vous faire découvrir un corps que vous ne connaissez pas. »", opts:["affirmé","suggéré"], ok:1,
          fb:"Le conditionnel : rien n'est promis, donc rien ne peut être contredit."},
         {q:"« Frais d'adhésion de soixante dollars applicables. »", opts:["affirmé","suggéré"], ok:0,
          fb:"Un montant précis : c'est vérifiable, et ça engage."},
         {q:"« Jusqu'à quarante pour cent de rabais. »", opts:["affirmé","suggéré"], ok:1,
          fb:"« Jusqu'à » annonce le meilleur cas. Un seul article peut suffire à le justifier."},
         {q:"« Le plus grand centre de la Rivière-du-Nord. »", opts:["affirmé","suggéré"], ok:0,
          fb:"Un superlatif se compare à tout le reste : s'il est faux, c'est trompeur."},
       ]},

      {t:'piege', h:"Le piège du mot par mot",
       rows:[
         ["juger chaque phrase à part","juger l'impression d'ensemble",
          "La loi regarde l'impression générale que l'annonce donne, et non chaque mot pris isolément. Une annonce dont toutes les phrases sont exactes peut être trompeuse."],
         ["croire qu'une suggestion est illégale","comprendre qu'elle est seulement vide",
          "Personne ne peut reprocher à un annonceur d'avoir écrit « prenez soin de vous ». Ce qu'on lui reproche, c'est de placer cette phrase là où vous cherchiez un prix."],
       ]},

      {t:'revoir', h:"À retenir",
       p:"Posez toujours la même question : <b>qu'est-ce que je pourrais reprocher si ce n'était pas vrai ?</b> Si vous ne trouvez rien à reprocher, c'est que rien ne vous a été promis."},
    ]
  },

  t1capsule: {
    eye:'Mini-leçon', tit:"Comment une capsule de trente secondes est bâtie",
    blocs:[
      {t:'texte', h:"Trente secondes, et pas une de plus",
       p:"Une capsule de radio est un objet minuté à la seconde près. Chaque seconde coûte de l'argent, et rien n'y est laissé au hasard : ni l'ordre des idées, ni le moment où le nom apparaît, ni la vitesse à laquelle la fin est dite. Quand vous connaissez le plan, vous savez quoi écouter et à quel moment.",
       note:"Le plan qui suit est celui de presque toutes les capsules commerciales, quel que soit le produit."},

      {t:'ana', h:"Les quatre temps",
       p:"Ils s'enchaînent toujours dans le même ordre.",
       mots:[['1. L\'accroche','une question, un malaise, une saison : « Cet hiver… », « Vous ne dormez plus comme avant. »'],['2. La promesse','ce que vous obtiendriez — souvent au conditionnel',true],['3. L\'offre','le chiffre : un prix, un rabais, une durée limitée'],['4. Le nom et le slogan','répétés, sur la musique — et juste après, la mention légale']],
       say:"L'accroche, la promesse, l'offre, le nom et le slogan.",
       note:"La mention légale n'est pas un cinquième temps : elle est collée à la fin, hors musique, et elle est dite au double du débit."},

      {t:'ex', h:"La capsule d'Élan Cardio, temps par temps",
       p:"Le même texte, découpé.",
       rows:[
         ["Cet hiver, à Élan Cardio, prenez enfin soin de vous.","l'accroche : la saison, le nom, un verbe à l'impératif"],
         ["Nos entraîneurs pourraient vous faire découvrir un corps que vous ne connaissez pas.","la promesse, au conditionnel : rien n'est garanti"],
         ["Plus de vingt appareils neufs. Un environnement plus chaleureux.","un chiffre vrai, suivi d'un comparatif vide"],
         ["Seulement neuf quatre-vingt-dix-neuf par semaine.","l'offre : la plus petite unité de temps possible"],
         ["Élan Cardio, le plus grand centre de la Rivière-du-Nord.","le nom, le rang, la musique : ce que vous retiendrez"],
         ["Offre valable sur adhésion de douze mois, frais de soixante dollars…","la mention légale : tout ce qui manquait, en cinq secondes"],
       ]},

      {t:'texte', h:"Pourquoi le prix est donné par semaine",
       p:"Neuf dollars quatre-vingt-dix-neuf par semaine, c'est cinq cent dix-neuf dollars par année. Les deux chiffres disent la même chose ; le premier se laisse écouter, le second fait réfléchir. Le choix de l'unité de temps est le procédé le plus simple et le plus efficace de tout le métier : par jour pour une assurance, par semaine pour un abonnement, par mois pour une voiture.",
       note:"Votre réflexe : ramenez tout à l'année, tout de suite, avant même de continuer à écouter."},

      {t:'check', h:"À vous",
       p:"Trois questions sur le plan.",
       qs:[
         {q:"Dans quel temps de la capsule trouve-t-on presque toujours le conditionnel ?", opts:["l'accroche","la promesse","la mention légale"], ok:1,
          fb:"La promesse : c'est là qu'on donne une image du résultat sans s'engager."},
         {q:"Où se trouve la durée de l'engagement ?", opts:["dans l'offre","dans la mention légale"], ok:1,
          fb:"Presque toujours à la fin, au double du débit."},
         {q:"Pourquoi le prix est-il annoncé par semaine ?", opts:["parce que le prélèvement est hebdomadaire","parce que le nombre paraît plus petit"], ok:1,
          fb:"Et ici, le prélèvement n'est même pas hebdomadaire : il se fait aux quatre semaines."},
       ]},

      {t:'revoir', h:"À retenir",
       p:"Accroche, promesse, offre, nom. Puis, hors musique et au double du débit, la mention légale. <b>Écoutez la fin d'abord</b> : c'est la partie la plus courte et la plus utile."},
    ]
  },

  t1cond: {
    eye:'Mini-leçon', tit:"Le conditionnel présent, entre la promesse et la politesse",
    blocs:[
      {t:'texte', h:"Un temps, deux métiers",
       p:"Le conditionnel présent sert à deux choses très différentes, et vous allez rencontrer les deux dans ce module. En publicité, il présente un résultat comme possible sans jamais s'y engager. Au téléphone, il rend une demande polie. Même forme, deux usages : c'est le contexte qui tranche, jamais la conjugaison.",
       note:"Ne pas confondre avec le futur simple, qui, lui, affirme."},

      {t:'ana', h:"Comment il se fabrique",
       p:"Le radical du futur, les terminaisons de l'imparfait. Un seul mécanisme pour tous les verbes.",
       mots:[['Les terminaisons','-ais · -ais · -ait · -ions · -iez · -aient'],['Le signe qui ne trompe pas','il y a toujours un r juste avant la terminaison',true],['Exemples réguliers','je parlerais · nous choisirions · vous prendriez']],
       say:"je parlerais, nous choisirions, vous prendriez",
       note:"C'est ce <b>r</b> qui distingue <i>je parlerais</i> (conditionnel) de <i>je parlais</i> (imparfait)."},

      {t:'ana', h:"Les radicaux irréguliers, à savoir par cœur",
       p:"Ce sont les mêmes qu'au futur simple : les apprendre une fois sert deux fois.",
       mots:[['être → ser-','je serais · nous serions'],['avoir → aur-','j\'aurais · vous auriez',true],['aller → ir- · faire → fer-','j\'irais · je ferais'],['pouvoir → pourr- · voir → verr-','je pourrais · je verrais'],['venir → viendr- · vouloir → voudr-','je viendrais · je voudrais'],['devoir → devr- · savoir → saur-','je devrais · je saurais']],
       say:"je serais, j'aurais, j'irais, je ferais, je pourrais, je verrais",
       note:"Six verbes couvrent presque tout ce que vous aurez à dire."},

      {t:'ana', h:"Emploi 1 — l'incertitude, celle de la publicité",
       p:"Le fait est présenté comme possible. Rien n'est affirmé, donc rien n'est contestable.",
       mots:[['L\'annonce dit','« Ce produit pourrait réduire vos coûts. »'],['Ce qu\'elle promet','rien du tout',true],['Si elle avait dit','« Ce produit réduit vos coûts », elle devrait le prouver']],
       say:"Ce produit pourrait réduire vos coûts.",
       note:"C'est le procédé le plus courant de la publicité, et le plus difficile à attaquer."},

      {t:'ana', h:"Emploi 2 — la politesse, celle du téléphone",
       p:"Le même temps adoucit une demande. C'est celui que vous emploierez dans « Je me lance ».",
       mots:[['Sec','Confirmez-moi le montant total.'],['Poli','Pourriez-vous me confirmer le montant total ?',true],['Encore mieux','J\'aimerais savoir ce qui n\'était pas écrit dans l\'annonce.']],
       say:"Pourriez-vous me confirmer le montant total ? J'aimerais savoir ce qui n'était pas écrit.",
       note:"Trois verbes suffisent : <i>pourriez-vous</i>, <i>j'aimerais</i>, <i>je voudrais</i>."},

      {t:'labo', h:"Le même verbe, les deux emplois",
       p:"Choisissez un verbe et un emploi.",
       axes:[
         {id:'v', lbl:'Quel verbe ?', opts:[['a','pouvoir'],['b','aimer'],['c','être']]},
         {id:'e', lbl:'Quel emploi ?', opts:[['1','la publicité'],['2','le téléphone']]}],
       out:{
         a1:{w:["Nos entraîneurs pourraient vous faire découvrir un corps que vous ne connaissez pas."], say:"Nos entraîneurs pourraient vous faire découvrir un corps que vous ne connaissez pas.", n:'incertitude : aucun résultat garanti'},
         a2:{w:["Pourriez-vous me confirmer le montant total ?"], say:"Pourriez-vous me confirmer le montant total ?", n:'politesse : la demande est adoucie'},
         b1:{w:["Vous aimeriez enfin dormir une nuit complète."], say:"Vous aimeriez enfin dormir une nuit complète.", n:'incertitude : on vous prête un désir'},
         b2:{w:["J'aimerais recevoir une confirmation écrite."], say:"J'aimerais recevoir une confirmation écrite.", n:'politesse : « je veux » serait brusque'},
         c1:{w:["Ce forfait serait le mieux adapté à votre situation."], say:"Ce forfait serait le mieux adapté à votre situation.", n:'incertitude : « est » aurait engagé le vendeur'},
         c2:{w:["Je serais disponible jeudi en avant-midi."], say:"Je serais disponible jeudi en avant-midi.", n:'politesse : on laisse la porte ouverte'},
       },
       note:"Écoutez les six phrases : la forme est identique, l'intention ne l'est pas."},

      {t:'piege', h:"Trois pièges",
       rows:[
         ["je pourrai","je pourrais",
          "Le futur affirme, le conditionnel n'affirme pas. À l'oral, les deux se ressemblent beaucoup. Dans une annonce, quand vous hésitez, c'est presque toujours le conditionnel."],
         ["si j'aurais le temps","si j'avais le temps",
          "Jamais de conditionnel après « si ». C'est l'imparfait qui va dans la condition, et le conditionnel dans la conséquence : « Si j'avais le temps, je lirais tout. »"],
         ["nous serions heureux, donc c'est promis","nous serions heureux ne promet rien",
          "Une formule de politesse au conditionnel est une formule, pas un engagement. Faites confirmer par écrit ce qui compte."],
       ]},

      {t:'check', h:"À vous",
       p:"Quatre questions.",
       qs:[
         {q:"« Ce matelas améliorerait votre sommeil. » L'annonceur s'engage-t-il ?", opts:["oui","non"], ok:1,
          fb:"Le conditionnel présente le résultat comme possible : rien n'est promis."},
         {q:"Quelle est la forme correcte : « Si j'___ le temps, je lirais tout. »", opts:["aurais","avais"], ok:1,
          fb:"Imparfait dans la condition, conditionnel dans la conséquence."},
         {q:"Quel radical pour « voir » au conditionnel ?", opts:["voir-","verr-"], ok:1,
          fb:"je verrais, tu verrais, il verrait — comme au futur."},
         {q:"« Pourriez-vous m'envoyer le contrat ? » : quel emploi ?", opts:["l'incertitude","la politesse"], ok:1,
          fb:"C'est la formule à employer au téléphone dans « Je me lance »."},
       ]},

      {t:'revoir', h:"À retenir",
       p:"Radical du futur, terminaisons de l'imparfait, un <b>r</b> avant la terminaison. En publicité, il ouvre une porte sans rien garantir ; au téléphone, il rend une demande polie. Le contexte décide."},
    ]
  },

  t1comp: {
    eye:'Mini-leçon', tit:"Comparer, et comparer à rien",
    blocs:[
      {t:'texte', h:"Le comparatif le plus courant est incomplet",
       p:"« Un environnement plus chaleureux. » Plus chaleureux que quoi ? La phrase ne le dit pas, et ce silence n'est pas un oubli : c'est le procédé. Un comparatif sans deuxième terme laisse votre tête placer elle-même le point de comparaison — et elle y met toujours ce qui arrange l'annonce.",
       note:"On appelle ça un <b>comparatif tronqué</b>. Comptez-les dans la prochaine annonce que vous verrez : il y en a souvent trois ou quatre."},

      {t:'ana', h:"Les trois degrés du comparatif",
       p:"Avec un adjectif ou un adverbe, la structure est toujours la même.",
       mots:[['Supériorité','plus … que : ce centre est plus grand que celui de la rue Parent'],['Infériorité','moins … que : le tarif est moins élevé que l\'an dernier',true],['Égalité','aussi … que : il est aussi cher que son voisin']],
       say:"plus grand que, moins élevé que, aussi cher que",
       note:"Le deuxième terme s'introduit toujours par <b>que</b>."},

      {t:'ana', h:"Avec un nom, on ajoute « de »",
       p:"La forme change légèrement, et l'égalité change de mot.",
       mots:[['Supériorité','plus de : plus de vingt appareils'],['Infériorité','moins de : moins de frais que chez le concurrent',true],['Égalité','autant de : autant de membres que l\'an passé']],
       say:"plus de vingt appareils, moins de frais, autant de membres",
       note:"« Plus de vingt » est une quantité chiffrée, donc vérifiable. Ce n'est pas un comparatif tronqué."},

      {t:'ana', h:"Le superlatif engage vraiment",
       p:"Il compare à tout le reste, dans un ensemble nommé. C'est pour ça qu'on en voit moins.",
       mots:[['La forme','le / la / les plus … de · le / la / les moins … de'],['Exemples','le plus grand centre de la Rivière-du-Nord · le meilleur prix en ville',true],['Ce que ça coûte','un superlatif faux est une représentation trompeuse']],
       say:"le plus grand centre de la région, le meilleur prix en ville",
       note:"Les agences préfèrent le comparatif vague au superlatif précis, et vous savez maintenant pourquoi."},

      {t:'ex', h:"Les deux irréguliers, à ne jamais rater",
       p:"Ils reviennent dans une annonce sur deux.",
       rows:[
         ["bon → meilleur","un meilleur prix — jamais « plus bon »"],
         ["bien → mieux","on y dort mieux — jamais « plus bien »"],
         ["le meilleur","le superlatif de « bon »"],
         ["le mieux","le superlatif de « bien »"],
       ]},

      {t:'piege', h:"Deux pièges",
       rows:[
         ["plus bon, plus bien","meilleur, mieux",
          "Deux formes irrégulières, aucune exception. « Meilleur » accompagne un nom ; « mieux » accompagne un verbe."],
         ["confondre « plus de vingt » et « plus chaleureux »","un chiffre n'est pas une impression",
          "« Plus de vingt appareils » est une quantité vérifiable. « Plus chaleureux » ne se vérifie pas. Le même mot « plus », deux natures très différentes."],
       ]},

      {t:'check', h:"À vous",
       p:"Quatre questions.",
       qs:[
         {q:"« Des résultats plus rapides. » Que manque-t-il ?", opts:["le deuxième terme de la comparaison","un adjectif"], ok:0,
          fb:"Plus rapides que quoi ? Rien n'est dit, donc rien n'est vérifiable."},
         {q:"Quelle forme est correcte ?", opts:["un plus bon prix","un meilleur prix"], ok:1,
          fb:"« Bon » devient « meilleur », toujours."},
         {q:"« Plus de vingt appareils neufs. » Est-ce vérifiable ?", opts:["oui","non"], ok:0,
          fb:"C'est une quantité chiffrée : on peut aller les compter."},
         {q:"« Le plus grand centre de la région » est…", opts:["un comparatif","un superlatif"], ok:1,
          fb:"Et un superlatif engage l'annonceur : s'il est faux, c'est trompeur."},
       ]},

      {t:'revoir', h:"À retenir",
       p:"Devant tout « plus », posez la question à voix haute : <b>plus que quoi ?</b> Si l'annonce ne répond pas, elle n'a rien dit. Et rappelez-vous que <b>meilleur</b> et <b>mieux</b> n'ont pas de forme en « plus »."},
    ]
  },

  t1que: {
    eye:'Mini-leçon', tit:"« Ne… que » : une limite déguisée en négation",
    blocs:[
      {t:'texte', h:"Le mot « ne » vous trompe",
       p:"« Il ne reste que trois jours. » Votre oreille entend « ne » et se prépare à une négation. Or il n'y en a aucune : il reste bel et bien trois jours. « Ne… que » ne nie pas, il <b>limite</b>. C'est la tournure la plus courante du français de tous les jours, et l'une des plus mal comprises quand on l'apprend.",
       note:"Elle veut dire exactement la même chose que <i>seulement</i>, en plus soutenu et en plus fréquent à l'oral."},

      {t:'ana', h:"Où se placent les deux morceaux",
       p:"« ne » devant le verbe, « que » juste devant ce qu'on limite. Et c'est la place de « que » qui décide du sens.",
       mots:[['On limite la somme','Elle n\'a payé que trente dollars.'],['On limite l\'action','Elle n\'a que payé trente dollars — elle n\'a rien fait d\'autre.',true],['On limite le temps','Il ne reste que trois jours.']],
       say:"Elle n'a payé que trente dollars. Il ne reste que trois jours.",
       note:"Déplacer « que » d'un mot change complètement la phrase. Placez-le contre ce que vous voulez limiter."},

      {t:'ana', h:"Aux temps composés et devant une voyelle",
       p:"Deux petites règles de forme, sans exception.",
       mots:[['Temps composé','que se place après le participe : ils n\'ont annoncé que le prix'],['Devant une voyelle','ne → n\' et que → qu\' : il n\'y a qu\'un matelas',true],['Avec un infinitif','elle ne veut que comprendre']],
       say:"Ils n'ont annoncé que le prix. Il n'y a qu'un matelas.",
       note:"Le double apostrophe de « il n'y a qu'un » surprend, mais il est correct."},

      {t:'texte', h:"Pourquoi la publicité l'emploie tant",
       p:"« Il ne reste que trois jours » dit d'abord <i>dépêchez-vous</i>, et seulement ensuite <i>trois jours</i>. La même information écrite « la vente finit jeudi » ne presse personne. La restriction crée une rareté, et la rareté empêche de comparer — c'est tout ce qu'on lui demande.",
       note:"Et le lundi suivant, la même vente recommence sous un autre nom. Ce n'est pas illégal, mais ce n'est pas non plus un hasard."},

      {t:'labo', h:"La même phrase, trois placements",
       p:"Choisissez où mettre « que ».",
       axes:[
         {id:'p', lbl:'On limite quoi ?', opts:[['a','la somme'],['b','l\'action'],['c','la personne']]},
         {id:'n', lbl:'Quelle phrase ?', opts:[['1','le paiement'],['2','la lecture']]}],
       out:{
         a1:{w:["Elle n'a payé que trente dollars."], say:"Elle n'a payé que trente dollars.", n:'la somme est limitée : trente, pas plus'},
         a2:{w:["Elle n'a lu que la grosse ligne."], say:"Elle n'a lu que la grosse ligne.", n:'ce qui a été lu est limité'},
         b1:{w:["Elle n'a que payé : elle n'a rien signé."], say:"Elle n'a que payé : elle n'a rien signé.", n:'l\'action est limitée, pas la somme'},
         b2:{w:["Elle n'a que lu : elle n'a rien décidé."], say:"Elle n'a que lu : elle n'a rien décidé.", n:'même chose : c\'est le geste qui est limité'},
         c1:{w:["Il n'y a qu'elle qui a payé."], say:"Il n'y a qu'elle qui a payé.", n:'la personne est limitée : elle, et personne d\'autre'},
         c2:{w:["Il n'y a qu'elle qui a lu le bas de la page."], say:"Il n'y a qu'elle qui a lu le bas de la page.", n:'même structure, autre verbe'},
       },
       note:"Trois placements, trois sens. C'est le seul point vraiment difficile de cette tournure."},

      {t:'piege', h:"Trois pièges",
       rows:[
         ["entendre une négation","entendre une limite",
          "« Il ne reste que trois jours » veut dire qu'il en reste trois. Si l'on voulait nier, on dirait « il ne reste pas trois jours »."],
         ["ne … pas que","attention, celui-là nie la limite",
          "« Il n'y a pas que le prix » veut dire : il y a le prix, et autre chose aussi. C'est presque le contraire de « il n'y a que le prix »."],
         ["oublier le « ne » à l'oral","on l'entend rarement, il s'écrit toujours",
          "Au Québec, on entend souvent « il reste que trois jours ». À l'écrit, et dans une lettre de réclamation, le « ne » est obligatoire."],
       ]},

      {t:'check', h:"À vous",
       p:"Quatre questions.",
       qs:[
         {q:"« Il ne reste que trois jours. » Combien de jours restent-ils ?", opts:["aucun","trois"], ok:1,
          fb:"Ce n'est pas une négation : c'est une limite."},
         {q:"« Elle n'a payé que trente dollars » limite…", opts:["la somme","l'action"], ok:0,
          fb:"« que » est collé à « trente dollars », donc c'est la somme."},
         {q:"« Il n'y a pas que le prix qui compte » veut dire…", opts:["seul le prix compte","le prix compte, et autre chose aussi"], ok:1,
          fb:"« pas que » nie la limite : il y a autre chose."},
         {q:"Complétez : « Il ___ y a ___ un matelas à quarante pour cent. »", opts:["n' … qu'","ne … que"], ok:0,
          fb:"Devant une voyelle, les deux mots s'élident."},
       ]},

      {t:'revoir', h:"À retenir",
       p:"<b>ne + verbe + que + ce qu'on limite.</b> Ce n'est pas une négation, c'est un « seulement » en deux morceaux. Et en publicité, il sert toujours à la même chose : créer une urgence pour empêcher de comparer."},
    ]
  },

  t1proc: {
    eye:'Mini-leçon', tit:"Six procédés, et ce qu'ils font à celui qui écoute",
    blocs:[
      {t:'texte', h:"Un procédé n'est pas un mensonge",
       p:"Aucun des six procédés de cet exercice n'est illégal en soi. Chacun peut s'employer honnêtement. Ce qui les rend intéressants, c'est qu'ils travaillent tous de la même façon : ils vous laissent faire vous-même le pas que l'annonce n'a pas voulu faire. Repérer le procédé, ce n'est donc pas accuser l'annonceur — c'est reprendre ce pas à son compte.",
       note:"C'est exactement ce que le programme appelle « comprendre un message implicite »."},

      {t:'ex', h:"Les six, avec leur effet",
       p:"À gauche, ce qu'on entend. À droite, ce que ça produit.",
       rows:[
         ["le conditionnel : « pourraient »","une image du résultat, sans engagement"],
         ["le comparatif tronqué : « plus chaleureux »","vous choisissez vous-même le point de comparaison"],
         ["le prix par semaine","un petit nombre à la place d'un gros"],
         ["la restriction : « il ne reste que »","une urgence qui empêche de comparer"],
         ["« jusqu'à quarante pour cent »","le meilleur cas donné pour le cas ordinaire"],
         ["la mention légale au double du débit","l'obligation respectée sans le risque d'être compris"],
       ]},

      {t:'ana', h:"Les trois questions qui démontent n'importe quelle annonce",
       p:"Dans cet ordre, et à voix haute si possible.",
       mots:[['1','Qu\'est-ce qui est chiffré ? — c\'est la seule partie vérifiable'],['2','Qu\'est-ce qui manque ? — la durée, le total, le point de comparaison',true],['3','Qu\'est-ce que j\'ai conclu tout seul ? — c\'est là qu\'est le message implicite']],
       say:"Qu'est-ce qui est chiffré ? Qu'est-ce qui manque ? Qu'est-ce que j'ai conclu tout seul ?",
       note:"Trois questions, vingt secondes. Vous en aurez besoin dans votre exposé de « Je me lance »."},

      {t:'check', h:"À vous",
       p:"Trois questions.",
       qs:[
         {q:"« Jusqu'à quarante pour cent de rabais » garantit un rabais de quarante pour cent sur…", opts:["tous les articles","au moins un article"], ok:1,
          fb:"« Jusqu'à » annonce la limite haute. Un seul article peut suffire à la justifier."},
         {q:"Le prix par semaine sert surtout à…", opts:["refléter le prélèvement réel","faire paraître le montant petit"], ok:1,
          fb:"Ici, le prélèvement se fait même aux quatre semaines, pas chaque semaine."},
         {q:"Repérer un procédé, c'est…", opts:["accuser l'annonceur de mentir","reprendre à son compte la conclusion qu'on allait tirer"], ok:1,
          fb:"Aucun de ces six procédés n'est illégal en soi."},
       ]},

      {t:'revoir', h:"À retenir",
       p:"Trois questions suffisent : <b>qu'est-ce qui est chiffré, qu'est-ce qui manque, qu'est-ce que j'ai conclu tout seul ?</b> La troisième est celle qui trouve le message implicite."},
    ]
  },

  t2depliant: {
    eye:'Mini-leçon', tit:"Lire un dépliant du bas vers le haut",
    blocs:[
      {t:'texte', h:"Deux textes sur la même feuille",
       p:"Un dépliant contient toujours deux textes qui ne s'adressent pas à la même personne. Le haut est écrit pour vous faire venir : gros caractères, photo, prix. Le bas est écrit pour protéger l'annonceur en cas de plainte : petits caractères, phrases longues, verbes au passif. Le premier vous parle ; le second parle de vous, à quelqu'un d'autre.",
       note:"C'est pour ça qu'on le lit à l'envers : le bas est la partie qui vous engage."},

      {t:'ana', h:"Les quatre questions à poser à un dépliant",
       p:"Dans cet ordre. Chacune a une réponse chiffrée quelque part sur la feuille — ou nulle part, et c'est déjà une réponse.",
       mots:[['1. Combien en tout la première année ?','multipliez, puis ajoutez ce qui se paie une seule fois'],['2. Pendant combien de temps suis-je tenu ?','cherchez terme, minimal, engagement, adhésion de … mois',true],['3. Qu\'est-ce qui s\'ajoute ?','frais d\'adhésion, frais de dossier, frais d\'activation, taxes'],['4. Comment est-ce que je sors ?','le délai, la façon, et ce qu\'il en coûte']],
       say:"Combien en tout ? Pendant combien de temps ? Qu'est-ce qui s'ajoute ? Comment est-ce que je sors ?",
       note:"Si le dépliant ne répond pas à la quatrième, le contrat, lui, y répond — et c'est le contrat qui vous lie."},

      {t:'ex', h:"Les mots qui annoncent une condition",
       p:"Quand l'un de ces mots paraît, il y a une somme ou une durée derrière.",
       rows:[
         ["terme minimal, adhésion de … mois","la durée de l'engagement"],
         ["exigible, applicable, en sus","une somme qui s'ajoute"],
         ["unique, à la signature","une somme qu'on paie une seule fois"],
         ["prélevé aux … semaines","la vraie fréquence, souvent différente du prix annoncé"],
         ["sans préavis","l'entreprise peut changer ce que vous venez de lire"],
         ["équivalant à … mensualités","le prix de la sortie"],
       ]},

      {t:'texte', h:"L'astérisque, et ce qui arrive quand il n'y a rien en bas",
       p:"Un astérisque est un renvoi : il annonce qu'une condition existe ailleurs sur la page. S'il y en a un et que vous ne trouvez aucune condition, ce n'est pas une bonne nouvelle. Cela veut dire que la promesse est faite sans que la condition soit écrite nulle part — et une promesse à laquelle rien ne correspond est précisément ce que la loi appelle une représentation trompeuse.",
       note:"Votre geste : photographiez le dépliant en entier, bas de page compris, avant de signer quoi que ce soit."},

      {t:'check', h:"À vous",
       p:"Trois questions.",
       qs:[
         {q:"Par où commence-t-on la lecture d'un dépliant ?", opts:["par le haut","par la plus petite ligne du bas"], ok:1,
          fb:"C'est le bas qui vous engage."},
         {q:"« Prélevé aux quatre semaines » sur une année de cinquante-deux semaines, ça fait…", opts:["douze prélèvements","treize prélèvements"], ok:1,
          fb:"Cinquante-deux divisé par quatre : treize, et non douze."},
         {q:"Un astérisque sans condition écrite, c'est…", opts:["moins grave","plus grave"], ok:1,
          fb:"Une promesse à laquelle rien ne correspond."},
       ]},

      {t:'revoir', h:"À retenir",
       p:"Quatre questions : <b>combien en tout, pendant combien de temps, qu'est-ce qui s'ajoute, comment est-ce que je sors ?</b> Et lisez toujours le bas avant le haut."},
    ]
  },

  t2efface: {
    eye:'Mini-leçon', tit:"La phrase passive, ou l'art d'effacer celui qui agit",
    blocs:[
      {t:'texte', h:"Personne n'agit, donc personne n'est responsable",
       p:"« Des frais sont exigibles. » « Le tarif est prélevé. » « L'offre peut être modifiée. » Dans ces trois phrases, quelqu'un exige, prélève et modifie — mais ce quelqu'un n'apparaît nulle part. C'est la phrase passive sans agent, et les conditions écrites en sont faites. L'effet est puissant : ce qui arrive semble arriver tout seul, comme la pluie.",
       note:"Ce n'est pas de la mauvaise foi automatique : le passif sert aussi quand l'auteur est évident ou sans intérêt. Mais dans un contrat, il vaut la peine de se demander qui a disparu."},

      {t:'ana', h:"Comment on passe de l'actif au passif",
       p:"Trois mouvements, toujours les mêmes.",
       mots:[['Actif','Le centre prélève le tarif.'],['Passif avec agent','Le tarif est prélevé par le centre.',true],['Passif sans agent','Le tarif est prélevé.'],['La recette','être conjugué + participe passé accordé avec le sujet']],
       say:"Le centre prélève le tarif. Le tarif est prélevé par le centre. Le tarif est prélevé.",
       note:"Le complément devient sujet ; le sujet passe derrière « par », ou disparaît."},

      {t:'ana', h:"L'accord, qui trahit le passif",
       p:"Le participe s'accorde toujours avec le sujet. C'est le signe le plus sûr qu'on est au passif.",
       mots:[['Masculin singulier','Le tarif est prélevé.'],['Féminin singulier','L\'offre est modifiée.',true],['Féminin pluriel','Les conditions ont été changées.'],['Masculin pluriel','Les frais seront facturés.']],
       say:"Le tarif est prélevé. L'offre est modifiée. Les conditions ont été changées.",
       note:"Ne pas confondre avec le passé composé avec « être », où il n'y a pas d'agent possible : <i>elle est partie</i> n'est pas un passif."},

      {t:'ana', h:"Au passé composé et au futur",
       p:"On empile les auxiliaires, et la phrase s'allonge encore.",
       mots:[['Passé composé','Le prix a été augmenté le premier mars.'],['Futur simple','Ce montant vous sera facturé en avril.',true],['Avec un modal','L\'offre peut être modifiée sans préavis.']],
       say:"Le prix a été augmenté. Ce montant vous sera facturé. L'offre peut être modifiée.",
       note:"Plus il y a d'auxiliaires, plus l'auteur est loin — et plus la phrase est difficile."},

      {t:'ana', h:"L'agent introduit par « de »",
       p:"Un cas plus rare, avec les verbes de sentiment, d'accompagnement ou de connaissance.",
       mots:[['Avec « de »','Ce centre est fréquenté de tout le quartier.'],['Le même cas ailleurs','Le dépliant était accompagné d\'un coupon.',true],['Ailleurs, c\'est « par »','Le tarif est prélevé par le centre.']],
       say:"Ce centre est fréquenté de tout le quartier. Le dépliant était accompagné d'un coupon.",
       note:"À reconnaître, pas à produire : c'est une tournure de langue écrite soutenue."},

      {t:'piege', h:"Deux pièges",
       rows:[
         ["confondre passif et passé composé avec être","cherchez l'agent possible",
          "« Elle est partie » ne peut pas se dire « par quelqu'un » : ce n'est pas un passif. « Le tarif est prélevé » le peut : c'en est un."],
         ["croire que le passif est toujours suspect","il est souvent normal",
          "« Le magasin a été construit en 1998 » n'efface personne d'important. Le réflexe utile n'est pas la méfiance : c'est la question."],
       ]},

      {t:'check', h:"À vous",
       p:"Quatre questions.",
       qs:[
         {q:"« Des frais sont exigibles à la signature. » Qui exige ?", opts:["la phrase ne le dit pas","le client"], ok:0,
          fb:"C'est exactement le point : l'auteur a été effacé."},
         {q:"« Les conditions ont été changées. » À quel temps ?", opts:["passé composé passif","imparfait"], ok:0,
          fb:"« ont été » + participe : passé composé au passif."},
         {q:"Laquelle est un passif ?", opts:["Elle est partie sans signer.","Le contrat est signé chaque jour."], ok:1,
          fb:"On peut ajouter « par quelqu'un » à la deuxième, pas à la première."},
         {q:"Dans « Ce centre est fréquenté de tout le quartier », l'agent est introduit par…", opts:["par","de"], ok:1,
          fb:"Un cas rare, avec certains verbes : à reconnaître, pas à produire."},
       ]},

      {t:'revoir', h:"À retenir",
       p:"<b>Être + participe passé accordé avec le sujet.</b> Devant chaque phrase passive d'un contrat, écrivez l'auteur en marge. Si vous n'arrivez pas à le nommer, vous venez de trouver la question à poser au téléphone."},
    ]
  },

  t2conc: {
    eye:'Mini-leçon', tit:"Accorder quelque chose, et maintenir quand même",
    blocs:[
      {t:'texte', h:"La tournure des lettres qui aboutissent",
       p:"« Bien que le prix hebdomadaire soit exact, l'annonce donne une fausse impression. » Cette phrase fait deux choses en même temps : elle reconnaît que l'autre a raison sur un point, et elle maintient la demande. C'est la concession, et c'est ce qui sépare une lettre de réclamation solide d'une lettre de colère.",
       note:"Une lettre qui nie tout se répond en une ligne. Une lettre qui concède se lit jusqu'au bout."},

      {t:'ana', h:"Avec le subjonctif : bien que, quoique, malgré que",
       p:"Trois marqueurs, un seul mode. Ce sont les plus soutenus, et les plus utiles à l'écrit.",
       mots:[['bien que','Bien que le prix soit exact, l\'annonce est trompeuse.'],['quoique','Quoique l\'offre paraisse avantageuse, elle coûte plus cher.',true],['malgré que','Malgré qu\'il ait signé, il conteste.']],
       say:"Bien que le prix soit exact. Quoique l'offre paraisse avantageuse.",
       note:"« Malgré que » est admis, mais « bien que » passe mieux dans une lettre formelle."},

      {t:'ana', h:"Avec l'indicatif : même si",
       p:"Un seul marqueur, et c'est le plus fréquent à l'oral. Il ne prend jamais le subjonctif.",
       mots:[['Correct','Même si vous avez lu les conditions, vous pouvez contester.'],['Correct','Même si la vente finit jeudi, je prends le temps de comparer.',true],['Jamais','« même si ce soit », « même si vous ayez » : ces formes n\'existent pas']],
       say:"Même si vous avez lu les conditions, vous pouvez contester.",
       note:"C'est l'erreur la plus fréquente du niveau : « même si » + subjonctif."},

      {t:'ana', h:"Sans verbe : malgré + un nom",
       p:"La forme la plus courte, et souvent la plus élégante.",
       mots:[['Avec un nom','Malgré l\'astérisque, le total n\'apparaît nulle part.'],['Avec un nom abstrait','Malgré ces explications, la somme reste inchangée.',true],['Les deux « malgré »','« malgré que » demande un verbe au subjonctif ; « malgré » tout court, un nom']],
       say:"Malgré l'astérisque, le total n'apparaît nulle part.",
       note:"Si vous hésitez sur le mode, cette forme vous évite la question."},

      {t:'labo', h:"La même idée, trois marqueurs",
       p:"Choisissez un marqueur et une idée.",
       axes:[
         {id:'m', lbl:'Quel marqueur ?', opts:[['a','bien que'],['b','même si'],['c','malgré']]},
         {id:'i', lbl:'Quelle idée ?', opts:[['1','le prix est exact'],['2','j\'ai signé']]}],
       out:{
         a1:{w:["Bien que le prix soit exact, l'annonce est trompeuse."], say:"Bien que le prix soit exact, l'annonce est trompeuse.", n:'subjonctif : soit'},
         a2:{w:["Bien que j'aie signé, je demande l'annulation."], say:"Bien que j'aie signé, je demande l'annulation.", n:'subjonctif : aie'},
         b1:{w:["Même si le prix est exact, l'annonce est trompeuse."], say:"Même si le prix est exact, l'annonce est trompeuse.", n:'indicatif : est'},
         b2:{w:["Même si j'ai signé, je demande l'annulation."], say:"Même si j'ai signé, je demande l'annulation.", n:'indicatif : ai signé'},
         c1:{w:["Malgré l'exactitude du prix, l'annonce est trompeuse."], say:"Malgré l'exactitude du prix, l'annonce est trompeuse.", n:'un nom, pas de verbe'},
         c2:{w:["Malgré ma signature, je demande l'annulation."], say:"Malgré ma signature, je demande l'annulation.", n:'un nom, pas de verbe'},
       },
       note:"Les six phrases disent la même chose. Le choix se fait sur le ton, pas sur le sens."},

      {t:'piege', h:"Trois pièges",
       rows:[
         ["même si le prix soit exact","même si le prix est exact",
          "« Même si » ne prend jamais le subjonctif. Aucune exception."],
         ["bien que le prix est exact","bien que le prix soit exact",
          "L'inverse est vrai aussi : « bien que » ne prend jamais l'indicatif."],
         ["confondre concession et opposition","la concession accorde d'abord",
          "« Le prix est bas, mais l'engagement est long » met deux faits côte à côte. « Bien que le prix soit bas… » commence par donner raison, puis maintient. C'est plus fort dans une lettre."],
       ]},

      {t:'check', h:"À vous",
       p:"Quatre questions.",
       qs:[
         {q:"« Bien que le prix ___ exact. »", opts:["est","soit"], ok:1,
          fb:"« Bien que » demande le subjonctif."},
         {q:"« Même si vous ___ signé. »", opts:["avez","ayez"], ok:0,
          fb:"« Même si » demande l'indicatif."},
         {q:"Quelle forme s'emploie avec un nom, sans verbe ?", opts:["malgré","malgré que"], ok:0,
          fb:"« Malgré que » demande un verbe au subjonctif."},
         {q:"Pourquoi la concession est-elle utile dans une lettre de réclamation ?", opts:["parce qu'elle montre qu'on a lu et compris","parce qu'elle est plus courte"], ok:0,
          fb:"Elle donne raison sur un point précis, ce qui rend le reste crédible."},
       ]},

      {t:'revoir', h:"À retenir",
       p:"<b>Bien que, quoique, malgré que</b> → subjonctif. <b>Même si</b> → indicatif. <b>Malgré</b> → un nom. Et rappelez-vous à quoi ça sert : accorder quelque chose à l'autre partie rend votre demande plus forte, pas plus faible."},
    ]
  },

  t2refo: {
    eye:'Mini-leçon', tit:"Redire en clair : les connecteurs de reformulation",
    blocs:[
      {t:'texte', h:"Traduire pour soi avant de décider",
       p:"« Terme minimal de douze mois » et « vous payez pendant un an même si vous cessez d'y aller » disent exactement la même chose. La deuxième phrase est celle que vous devez écrire dans la marge. Reformuler n'est pas un exercice d'école : c'est le geste qui transforme une condition écrite en décision.",
       note:"Et à l'oral, c'est le geste qui vérifie qu'on a bien compris son interlocuteur."},

      {t:'ana', h:"Les connecteurs qui annoncent une reformulation",
       p:"Ils préviennent : ce qui suit répète ce qui précède, en plus clair.",
       mots:[['autrement dit','le plus courant, à l\'oral comme à l\'écrit'],['en d\'autres mots · c\'est-à-dire','même emploi, même place',true],['en somme · bref','ils reformulent ET ils concluent : ils annoncent la fin'],['si je comprends bien','à l\'oral, pour faire confirmer par l\'autre']],
       say:"autrement dit, c'est-à-dire, en somme, si je comprends bien",
       note:"« En somme » ne se met pas au milieu d'une explication : il annonce qu'on arrive au bout."},

      {t:'ex', h:"Six conditions, traduites",
       p:"À gauche, ce que le dépliant écrit. À droite, ce que ça veut dire.",
       rows:[
         ["terme minimal de douze mois","autrement dit, vous payez un an, même sans y aller"],
         ["frais uniques exigibles à la signature","autrement dit, une somme de plus, tout de suite"],
         ["prélevé aux quatre semaines","autrement dit, treize fois par année, pas douze"],
         ["taxes en sus","autrement dit, ajoutez environ quinze pour cent"],
         ["peut être modifiée sans préavis","autrement dit, rien de ceci ne vous est garanti demain"],
         ["certaines conditions s'appliquent","en somme, il y a des règles qu'on ne vous dira qu'en succursale"],
       ]},

      {t:'texte', h:"À l'oral, la reformulation est une arme polie",
       p:"« Si je comprends bien, je m'engage pour douze mois et je paie soixante dollars de plus aujourd'hui. C'est bien ça ? » Cette phrase oblige l'autre à confirmer ou à corriger, sans jamais l'accuser. Elle est particulièrement utile au téléphone, où rien n'est écrit — et c'est celle que vous emploierez dans « Je me lance ».",
       note:"Notez la réponse et l'heure de l'appel. Puis demandez la même chose par écrit."},

      {t:'check', h:"À vous",
       p:"Trois questions.",
       qs:[
         {q:"Quel connecteur annonce qu'on arrive à la conclusion ?", opts:["autrement dit","en somme"], ok:1,
          fb:"« En somme » et « bref » reformulent et concluent à la fois."},
         {q:"« Prélevé aux quatre semaines », c'est combien de fois par année ?", opts:["douze","treize"], ok:1,
          fb:"Cinquante-deux semaines divisées par quatre."},
         {q:"Pourquoi dire « si je comprends bien » au téléphone ?", opts:["pour gagner du temps","pour obliger l'autre à confirmer ou à corriger"], ok:1,
          fb:"Et sans jamais l'accuser de quoi que ce soit."},
       ]},

      {t:'revoir', h:"À retenir",
       p:"<b>Autrement dit</b>, <b>c'est-à-dire</b>, <b>en d'autres mots</b> reformulent. <b>En somme</b> et <b>bref</b> reformulent et concluent. <b>Si je comprends bien</b> fait confirmer. Écrivez la traduction dans la marge : c'est là que la décision se prend."},
    ]
  },

  t2prix: {
    eye:'Mini-leçon', tit:"Le prix annoncé est le prix payé",
    blocs:[
      {t:'texte', h:"Une règle simple, et souvent ignorée",
       p:"Au Québec, le prix qu'un commerçant annonce doit être le montant total que vous aurez à débourser. Ce n'est pas un idéal : c'est une obligation. Aucun frais ne peut apparaître à la caisse s'il n'était pas dans le prix affiché — sauf la TPS et la TVQ, qui sont les deux seules exceptions.",
       note:"Frais d'administration, frais de dossier, frais de préparation, frais imposés par une loi et gardés par le commerçant : tout cela doit être compris dans le prix annoncé."},

      {t:'ana', h:"Les trois volets de la règle",
       p:"Ils se tiennent, et le troisième est celui qu'on oublie.",
       mots:[['Tout inclus','le prix annoncé est le montant total à débourser'],['Sauf les taxes','la TPS et la TVQ peuvent s\'ajouter à la caisse',true],['La taille compte','le prix total doit ressortir plus nettement que les montants qui le composent']],
       say:"Le prix annoncé est le montant total. Seules la TPS et la TVQ peuvent s'ajouter.",
       note:"Le troisième volet vise exactement les annonces qui affichent en gros un petit versement et en petit le total."},

      {t:'ex', h:"Le calcul, pas à pas",
       p:"L'annonce d'Élan Cardio, ramenée à l'année.",
       rows:[
         ["9,99 $ par semaine","le chiffre annoncé, en gros caractères"],
         ["× 52 semaines","519,48 $ pour l'année"],
         ["+ 60 $ de frais d'adhésion","579,48 $"],
         ["+ taxes","environ 666 $ la première année"],
         ["Ce que l'annonce disait","« neuf quatre-vingt-dix-neuf »"],
         ["Le rapport entre les deux","environ soixante-six fois"],
       ]},

      {t:'texte', h:"Ce que ça vous donne concrètement",
       p:"Si le montant demandé à la caisse dépasse le prix affiché, vous n'avez pas à payer la différence, et le commerçant est en défaut. Gardez l'annonce — une photo suffit — parce que c'est elle qui prouve le prix. Et rappelez-vous que la règle vaut pour la circulaire, le dépliant, l'affiche en magasin et le site web : le format ne change rien.",
       note:"Un rabais annoncé doit aussi être un vrai rabais, calculé sur un prix réellement pratiqué avant."},

      {t:'check', h:"À vous",
       p:"Quatre questions.",
       qs:[
         {q:"Quelles sommes peuvent s'ajouter au prix annoncé ?", opts:["les frais d'administration","la TPS et la TVQ"], ok:1,
          fb:"Elles sont les deux seules exceptions."},
         {q:"Le prix total doit ressortir…", opts:["autant que les montants qui le composent","plus nettement qu'eux"], ok:1,
          fb:"C'est ce troisième volet qui vise les annonces à petit versement."},
         {q:"9,99 $ par semaine sur cinquante-deux semaines, c'est…", opts:["519,48 $","479,52 $"], ok:0,
          fb:"9,99 × 52 = 519,48."},
         {q:"Si la caisse demande plus que le prix affiché…", opts:["vous devez payer la différence","le commerçant est en défaut"], ok:1,
          fb:"Gardez une photo de l'annonce : c'est elle qui prouve le prix."},
       ]},

      {t:'revoir', h:"À retenir",
       p:"<b>Le prix annoncé est le prix payé</b>, taxes exceptées, et le total doit ressortir plus nettement que ses morceaux. Ramenez toujours à l'année, et photographiez l'annonce."},
    ]
  },

  t3ils: {
    eye:'Mini-leçon', tit:"Le « ils » que personne ne présente",
    blocs:[
      {t:'texte', h:"Un pronom sans antécédent",
       p:"« Ils me l'ont envoyée. » « Ils ont encore augmenté les prix. » « Ils disent que c'est le meilleur produit. » Dans ces trois phrases, « ils » ne reprend personne : aucun nom n'a été donné avant. Le référent est <b>implicite</b> — celui qui parle tient pour acquis que vous voyez de qui il s'agit. Le plus souvent, c'est vrai. Parfois, c'est le procédé lui-même.",
       note:"Le programme du niveau 7 nomme ce savoir : comprendre que le référent du pronom « ils » peut être implicite."},

      {t:'ana', h:"Les trois questions qui trouvent le référent",
       p:"Dans cet ordre, et la réponse vient presque toujours à la deuxième.",
       mots:[['1','De quoi parle la phrase ? — un produit, une loi, un prix, une enseigne'],['2','Qui, dans ce domaine-là, pose ce genre de geste ? — une entreprise, un organisme, un gouvernement',true],['3','Quelqu\'un a-t-il été nommé deux ou trois phrases plus haut ?']],
       say:"De quoi parle la phrase ? Qui pose ce geste ? Qui a été nommé avant ?",
       note:"Le référent est presque toujours un <b>groupe</b> : une entreprise, un organisme, une autorité — jamais une personne précise."},

      {t:'ex', h:"Six « ils », six référents",
       p:"À gauche, la phrase. À droite, qui elle désigne.",
       rows:[
         ["Ils me l'ont envoyée gratuitement.","l'entreprise qui fabrique ou vend le produit"],
         ["Ils ont changé les conditions en janvier.","le commerçant avec qui on a signé"],
         ["Ils interdisent la publicité aux enfants, ici.","la loi, le législateur québécois"],
         ["Ils reçoivent les plaintes du public.","l'organisme compétent"],
         ["Ils vérifient la langue des enseignes.","l'Office québécois de la langue française"],
         ["Ils disent que c'est le meilleur produit.","personne : aucun nom n'existe derrière"],
       ]},

      {t:'texte', h:"Le cas où « ils » sert à donner une caution qui n'existe pas",
       p:"« Ils disent que c'est le meilleur produit sur le marché. » Qui, ils ? Des essais ? Des clients ? Des spécialistes ? La phrase donne l'impression qu'une autorité existe, sans jamais la nommer — et une autorité qu'on ne peut pas nommer ne peut pas non plus être vérifiée. C'est le même mécanisme que le comparatif tronqué, appliqué aux personnes.",
       note:"Votre réflexe : remplacez « ils » à voix haute par un nom précis. Si vous n'y arrivez pas, notez la question."},

      {t:'piege', h:"Deux pièges",
       rows:[
         ["chercher un nom masculin pluriel dans la phrase d'avant","il n'y en a pas toujours",
          "Le « ils » implicite n'a pas d'antécédent écrit. Le chercher dans le texte fait perdre du temps : il faut le déduire du domaine."],
         ["croire que c'est incorrect","c'est du français normal",
          "Ce « ils » est parfaitement correct et très fréquent, à l'oral comme à l'écrit. Ce qu'il faut, ce n'est pas le corriger : c'est savoir qui il désigne."],
       ]},

      {t:'check', h:"À vous",
       p:"Trois questions.",
       qs:[
         {q:"« Ils ont augmenté le tarif en janvier. » Qui, le plus probablement ?", opts:["l'entreprise avec qui on a signé","les autres clients"], ok:0,
          fb:"Le geste — augmenter un tarif — désigne son auteur."},
         {q:"Le référent implicite de « ils » est le plus souvent…", opts:["une personne précise","un groupe : entreprise, organisme, autorité"], ok:1,
          fb:"C'est ce qui permet de le déduire du domaine dont on parle."},
         {q:"« Ils disent que c'est le meilleur. » Que faut-il en conclure ?", opts:["une autorité l'affirme","personne n'est nommé, donc rien n'est vérifiable"], ok:1,
          fb:"Une caution qu'on ne peut pas nommer n'est pas une caution."},
       ]},

      {t:'revoir', h:"À retenir",
       p:"Le « ils » implicite désigne presque toujours <b>un groupe déduit du domaine</b>. Remplacez-le à voix haute par un nom précis : si vous n'y arrivez pas, vous venez de trouver ce qui manque à l'annonce."},
    ]
  },

  t3int: {
    eye:'Mini-leçon', tit:"Si petit qu'on ne le lit pas : l'intensité et sa conséquence",
    blocs:[
      {t:'texte', h:"Deux idées liées par un degré",
       p:"« Le caractère est petit » et « on ne le lit pas » sont deux faits séparés. « Le caractère est si petit qu'on ne le lit pas » n'en fait qu'un seul : le second découle du premier, à cause du degré. C'est la tournure qui décrit le mieux les procédés de ce module — trop rapide, trop petit, tellement de conditions.",
       note:"Le programme appelle ces phrases des <b>subordonnées corrélatives</b>. Le nom est savant, la mécanique ne l'est pas."},

      {t:'ana', h:"Modèle 1 — si / tellement + que",
       p:"Le degré est tel qu'une conséquence en découle. Après « que », l'indicatif.",
       mots:[['Avec un adjectif','Le caractère est si petit qu\'on ne le lit pas.'],['Avec un adverbe','La voix va tellement vite qu\'on ne comprend rien.',true],['Avec un nom','Il y a tellement de conditions que personne ne les lit.']],
       say:"Le caractère est si petit qu'on ne le lit pas. La voix va tellement vite qu'on ne comprend rien.",
       note:"Avec un nom, c'est <b>tellement de</b>, jamais « si de »."},

      {t:'ana', h:"Modèle 2 — assez / suffisamment + pour",
       p:"Le degré est suffisant pour qu'une chose devienne possible.",
       mots:[['+ infinitif','La mention est assez rapide pour passer inaperçue.'],['+ pour que + subjonctif','Le prix est assez bas pour qu\'on signe sans réfléchir.',true],['Autre forme','L\'annonce est suffisamment habile pour qu\'on l\'étudie.']],
       say:"La mention est assez rapide pour passer inaperçue. Le prix est assez bas pour qu'on signe sans réfléchir.",
       note:"L'infinitif quand le sujet est le même ; « pour que » + subjonctif quand il change."},

      {t:'ana', h:"Modèle 3 — trop + pour",
       p:"Le degré est excessif : la chose devient impossible.",
       mots:[['+ infinitif','La capsule est trop courte pour être comprise.'],['+ pour que + subjonctif','L\'écriture est trop fine pour que je la lise sans lunettes.',true],['Le sens','« trop » ferme la porte ; « assez » l\'ouvre']],
       say:"La capsule est trop courte pour être comprise. L'écriture est trop fine pour que je la lise.",
       note:"« Trop » n'est pas une insistance : c'est un excès qui empêche."},

      {t:'labo', h:"La même paire d'idées, trois modèles",
       p:"Choisissez un modèle et une paire.",
       axes:[
         {id:'m', lbl:'Quel modèle ?', opts:[['a','si … que'],['b','assez … pour'],['c','trop … pour']]},
         {id:'p', lbl:'Quelle paire ?', opts:[['1','le caractère'],['2','la mention']]}],
       out:{
         a1:{w:["Le caractère est si petit qu'on ne le lit pas."], say:"Le caractère est si petit qu'on ne le lit pas.", n:'après « que » : indicatif'},
         a2:{w:["La mention est si rapide qu'on n'en retient rien."], say:"La mention est si rapide qu'on n'en retient rien.", n:'même structure'},
         b1:{w:["Le caractère est assez petit pour passer inaperçu."], say:"Le caractère est assez petit pour passer inaperçu.", n:'même sujet : infinitif'},
         b2:{w:["La mention est assez rapide pour qu'on l'oublie."], say:"La mention est assez rapide pour qu'on l'oublie.", n:'sujet différent : subjonctif'},
         c1:{w:["Le caractère est trop petit pour être lu."], say:"Le caractère est trop petit pour être lu.", n:'excès : la chose devient impossible'},
         c2:{w:["La mention est trop rapide pour que je la comprenne."], say:"La mention est trop rapide pour que je la comprenne.", n:'subjonctif après « pour que »'},
       },
       note:"Six phrases, trois nuances : la conséquence, la possibilité, l'impossibilité."},

      {t:'piege', h:"Trois pièges",
       rows:[
         ["si de conditions","tellement de conditions",
          "Devant un nom, « si » ne s'emploie pas. C'est « tellement de » ou « tant de »."],
         ["pour qu'on comprend","pour qu'on comprenne",
          "Après « pour que », le subjonctif est obligatoire. Après « que » tout court, c'est l'indicatif."],
         ["employer « trop » pour insister","trop veut dire : à l'excès",
          "« C'est trop beau » en français standard veut dire que ça dépasse la mesure. Pour insister, c'est « très »."],
       ]},

      {t:'check', h:"À vous",
       p:"Quatre questions.",
       qs:[
         {q:"« Il y a ___ conditions que personne ne les lit. »", opts:["si de","tellement de"], ok:1,
          fb:"Devant un nom, « tellement de » ou « tant de »."},
         {q:"« La voix va si vite qu'on ne ___ rien. » Quel mode ?", opts:["comprend","comprenne"], ok:0,
          fb:"Après « que » tout court : indicatif."},
         {q:"« Le prix est assez bas pour qu'on ___ sans réfléchir. »", opts:["signe","signera"], ok:0,
          fb:"Après « pour que » : subjonctif."},
         {q:"« Trop courte pour être comprise » veut dire…", opts:["très courte","si courte que c'est impossible"], ok:1,
          fb:"« Trop » marque un excès qui empêche."},
       ]},

      {t:'revoir', h:"À retenir",
       p:"<b>si / tellement + que</b> + indicatif : la conséquence. <b>assez / suffisamment + pour (que)</b> : la possibilité. <b>trop + pour (que)</b> : l'impossibilité. Après <b>pour que</b>, toujours le subjonctif."},
    ]
  },

  t3gen: {
    eye:'Mini-leçon', tit:"Un matelas en général, ou ce matelas-là",
    blocs:[
      {t:'texte', h:"Le même groupe de mots, deux sens",
       p:"« Un matelas, ça dure une dizaine d'années. » « Il y a un matelas qui est à quarante pour cent. » Les deux phrases commencent par « un matelas », et elles ne parlent pas du tout de la même chose. La première parle de la <b>catégorie entière</b> ; la seconde, d'un <b>objet précis</b>, celui du fond du magasin. Ce n'est pas le déterminant qui décide : c'est la structure de la phrase.",
       note:"On appelle le premier sens <b>générique</b> et le second <b>spécifique</b>."},

      {t:'ana', h:"Le sens générique — toute la catégorie",
       p:"On énonce une vérité qui vaut pour tous les objets de la sorte.",
       mots:[['Avec un / une','Un matelas, ça dure dix ans.'],['Avec les','Les rabais, ça revient chaque saison.',true],['Avec du / de la','Du papier, ça se recycle bien.'],['Le signe le plus sûr','la reprise par ça']],
       say:"Un matelas, ça dure dix ans. Les rabais, ça revient chaque saison.",
       note:"La reprise par <b>ça</b> est presque toujours le signe du générique."},

      {t:'ana', h:"Le sens spécifique — un cas particulier",
       p:"On parle d'un objet qu'on pourrait montrer du doigt.",
       mots:[['Avec « il y a … qui »','Il y a un matelas qui est à quarante pour cent.'],['Avec ce / cette … -là','Cet abonnement-là vous engage pour douze mois.',true],['Avec un complément','La capsule de la rue Parent passe trois fois par heure.']],
       say:"Il y a un matelas qui est à quarante pour cent. Cet abonnement-là vous engage pour douze mois.",
       note:"« Il y a … qui » est la structure spécifique la plus fréquente du français parlé du Québec."},

      {t:'texte', h:"Pourquoi la publicité passe sans arrêt de l'un à l'autre",
       p:"Elle affirme au générique — « un bon matelas, ça change une vie » — parce qu'une vérité générale ne se conteste pas. Puis elle vous laisse appliquer cette vérité au produit précis qu'elle vend, ce qu'elle n'a jamais promis. Le glissement se fait dans votre tête, et il ne laisse aucune trace dans le texte.",
       note:"C'est le message implicite dans sa forme la plus pure : l'annonce dit vrai, et vous concluez faux."},

      {t:'ex', h:"Le test en trois mots",
       p:"Ajoutez « en général » à la phrase, et écoutez si elle tient.",
       rows:[
         ["Un matelas, ça dure dix ans, en général.","tient : générique"],
         ["Il y a un matelas à quarante pour cent, en général.","ne tient pas : spécifique"],
         ["La publicité, ça travaille par répétition, en général.","tient : générique"],
         ["La capsule passe trois fois par heure, en général.","ne tient pas vraiment : spécifique"],
       ]},

      {t:'check', h:"À vous",
       p:"Quatre questions.",
       qs:[
         {q:"« Les abonnements de gym, ça se signe trop vite. »", opts:["générique","spécifique"], ok:0,
          fb:"La reprise par « ça » et la vérité générale : c'est du générique."},
         {q:"« Cet abonnement-là vous engage pour douze mois. »", opts:["générique","spécifique"], ok:1,
          fb:"« -là » désigne un objet précis."},
         {q:"Quel est le signe le plus sûr du sens générique ?", opts:["le déterminant « un »","la reprise par « ça »"], ok:1,
          fb:"« Un » sert aux deux sens : c'est la structure qui tranche."},
         {q:"Pourquoi la publicité affirme-t-elle au générique ?", opts:["parce qu'une vérité générale ne se conteste pas","parce que c'est plus court"], ok:0,
          fb:"Et vous faites vous-même le glissement vers le produit précis."},
       ]},

      {t:'revoir', h:"À retenir",
       p:"Reprise par <b>ça</b> et vérité générale → générique. <b>Il y a … qui</b>, <b>ce … -là</b>, un complément de temps ou de lieu → spécifique. Le test : ajoutez « en général » et voyez si la phrase tient."},
    ]
  },

  t3ou: {
    eye:'Mini-leçon', tit:"Trois portes, et comment choisir la bonne",
    blocs:[
      {t:'texte', h:"Trois organismes, trois compétences",
       p:"Une publicité qui cloche peut relever de trois autorités différentes au Québec, et se tromper de porte fait perdre des semaines. La question à se poser n'est pas « qui est le plus fort ? » mais « de quoi s'agit-il exactement ? ». La réponse tient presque toujours en un mot : le prix, la forme, ou la langue.",
       note:"Les trois existent, elles ne se marchent pas sur les pieds, et rien n'empêche de s'adresser à deux d'entre elles."},

      {t:'ana', h:"L'Office de la protection du consommateur",
       p:"Il applique la Loi sur la protection du consommateur. C'est la porte du prix et du contrat.",
       mots:[['Ce qui relève de lui','le prix annoncé, la représentation trompeuse, l\'omission d\'un fait important'],['Et aussi','la publicité destinée aux personnes de moins de treize ans',true],['Ce qu\'il peut faire','recevoir la plainte, informer, enquêter, poursuivre']],
       say:"l'Office de la protection du consommateur",
       note:"C'est un organisme du gouvernement du Québec, et la loi qu'il applique a force obligatoire."},

      {t:'ana', h:"Normes de la publicité",
       p:"C'est l'organisme qui administre le Code canadien des normes de la publicité, en quatorze articles. C'est la porte de la forme du message.",
       mots:[['Ce qui relève de lui','la publicité déguisée, les témoignages, la publicité comparative'],['Comment ça marche','il reçoit les plaintes du public et les soumet à un conseil',true],['Sa portée','un code de l\'industrie, appliqué à l\'échelle du pays']],
       say:"Normes de la publicité",
       note:"L'article 2 du Code porte sur les techniques de publicité déguisée ; l'article 7, sur les témoignages."},

      {t:'ana', h:"L'Office québécois de la langue française",
       p:"Il applique la Charte de la langue française. C'est la porte de la langue de l'affichage.",
       mots:[['Ce qui relève de lui','la langue des enseignes, des affiches, de la publicité commerciale'],['Ce que la Charte demande','l\'affichage se fait en français ; s\'il est bilingue, le français doit être nettement prédominant',true],['Depuis juin 2025','une marque dans une autre langue visible de la rue : le français occupe un espace au moins deux fois plus grand']],
       say:"l'Office québécois de la langue française",
       note:"« Nettement prédominant » a une définition précise : espace deux fois plus grand, même visibilité, même permanence, même éclairage."},

      {t:'ex', h:"Six situations, trois portes",
       p:"À gauche, ce qui arrive. À droite, à qui on s'adresse.",
       rows:[
         ["la caisse demande plus que le prix affiché","l'Office de la protection du consommateur"],
         ["une vidéo payée ne dit pas qu'elle est payée","Normes de la publicité"],
         ["une annonce de jouet vise des enfants de dix ans","l'Office de la protection du consommateur"],
         ["un témoignage vante un produit jamais utilisé","Normes de la publicité"],
         ["une enseigne est en anglais, avec trois mots de français","l'Office québécois de la langue française"],
         ["une annonce tait des frais qui s'ajoutent","l'Office de la protection du consommateur"],
       ]},

      {t:'texte', h:"Avant de vous plaindre : gardez la preuve",
       p:"Une plainte sans trace n'aboutit presque jamais. Photographiez l'annonce en entier, bas de page compris. Notez la date, l'heure, la station ou le nom du site. Conservez le dépliant et le contrat. Et écrivez d'abord au commerçant : beaucoup de dossiers se règlent là, et une lettre datée est la meilleure pièce du dossier suivant.",
       note:"C'est précisément la lettre que vous écrirez dans « Je me lance »."},

      {t:'check', h:"À vous",
       p:"Quatre questions.",
       qs:[
         {q:"Une vidéo commanditée qui ne le dit pas : quelle porte ?", opts:["Normes de la publicité","l'Office québécois de la langue française"], ok:0,
          fb:"Publicité déguisée : article 2 du Code canadien."},
         {q:"Une publicité qui vise des enfants de dix ans : quelle porte ?", opts:["Normes de la publicité","l'Office de la protection du consommateur"], ok:1,
          fb:"C'est une interdiction de la Loi sur la protection du consommateur."},
         {q:"« Nettement prédominant » veut dire un espace…", opts:["légèrement plus grand","au moins deux fois plus grand"], ok:1,
          fb:"Avec la même visibilité, la même permanence et le même éclairage."},
         {q:"Quel est le premier geste avant toute plainte ?", opts:["téléphoner à un avocat","photographier l'annonce en entier"], ok:1,
          fb:"Une plainte sans trace n'aboutit presque jamais."},
       ]},

      {t:'revoir', h:"À retenir",
       p:"<b>Le prix et le contrat</b> → l'Office de la protection du consommateur. <b>La forme du message</b> → Normes de la publicité. <b>La langue de l'affichage</b> → l'Office québécois de la langue française. Et dans les trois cas : la preuve d'abord."},
    ]
  },

};
