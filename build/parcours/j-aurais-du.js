// ═══════════════════════════════════════════════════════════════════════════
// Point express — Revenir sur ce qu'on n'a pas fait
//
// Savoirs n7-s25 (conditionnel) et n7-s21 (l'antériorité). Une ORDONNANCE :
// l'enseignant l'envoie à un élève qui dit « je devais appeler » ou « j'ai dû
// appeler » là où il veut dire « j'aurais dû appeler ». Dix minutes, dix
// écrans.
//
// ── Ce dont il se sépare, et d'abord de son voisin d'étagère ───────────────
// Le niveau 7 porte déjà « Demander sans brusquer » — le conditionnel de
// POLITESSE, celui qui ouvre une demande encore possible. Celui-ci porte le
// conditionnel PASSÉ, celui d'une chose qui ne se fera plus. La distinction
// est faite dès le titre, et l'écran 1 oppose les deux formes de front :
// « je voudrais appeler » (c'est à venir) contre « j'aurais dû appeler »
// (c'est perdu). Un élève qui a fait les deux points ne doit jamais pouvoir
// croire qu'il s'agit du même outil poli.
//
// Trois mini-leçons du dépôt effleurent la chose et toutes la manquent de la
// même façon : « Ce qui aurait pu ne pas arriver » et « Ce qui aurait pu se
// passer autrement » l'installent dans un récit de sinistre — l'élève y
// apprend une forme narrative, pas une phrase à dire à quelqu'un ; « Deux
// conditionnels pour peser ses mots » l'aligne à côté de la politesse, donc
// exactement là où la confusion se fabrique. Les cinq écarts tenus :
//
//   1. INDUCTIF. L'élève range huit phrases selon UNE question qui n'a rien
//      de grammatical — « est-ce que c'est encore possible ? » — avant qu'on
//      lui dise qu'il y a deux formes. La règle de l'écran 3 est écrite
//      comme le constat de ce tri.
//   2. PARTIEL, JAMAIS LA LISTE. Aucun tableau de conjugaison du
//      conditionnel passé. Un TEST : deux mots après le sujet, et le second
//      est un participe → c'est fini. Il marche sur un verbe jamais vu.
//   3. LE CAS QUI SAUVE EST DIT EN DERNIER (écran 8). « Il aurait fallu »
//      ne vise personne, et c'est la formule qui permet de faire un reproche
//      au travail sans en faire un. La nommer d'entrée aurait donné une
//      troisième forme à retenir au lieu d'une sortie de secours.
//   4. LE MÉTALANGAGE ARRIVE APRÈS. « Conditionnel passé » n'est écrit qu'à
//      l'écran 3, la chose ayant été maniée huit fois.
//   5. EXEMPLES VARIÉS, JAMAIS CEUX D'UN MODULE. Un guichet de centre de
//      formation, un texto à un collègue, un courriel à un fournisseur, une
//      conversation avec un propriétaire, une réunion d'équipe.
//
// Aucun média. Le sujet est une faute d'écriture et de choix de mots : elle
// s'entend parfaitement, elle ne se corrige qu'en la voyant.
// ═══════════════════════════════════════════════════════════════════════════

const PARCOURS = {
  slug:     'j-aurais-du',
  titre:    "Revenir sur ce qu'on n'a pas fait",
  surtitre: "Point express · 10 minutes",
  niveau:   7,
  savoir:   'n7-s25 · n7-s21',
};

const ECRANS = [

  // ── 1. Une décision, sans aucune règle donnée. ───────────────────────────
  {
    id:   'depart',
    type: 'verif',
    eye:  'Une question, pour commencer',
    menu: 'Trois phrases',
    titre: "Vous êtes devant un bureau fermé. Quelle phrase dit que c'est perdu ?",
    consigne: "Vous vous êtes déplacé au centre de formation sans téléphoner, et c'est fermé. "
            + "Répondez avec ce que vous savez déjà — c'est fait exprès.",
    options: [
      { txt: "«&nbsp;J'aurais dû téléphoner avant de venir.&nbsp;»", juste: true },
      { txt: "«&nbsp;Je voudrais téléphoner avant de venir.&nbsp;»",
        rat_t: "Celle-là est polie, mais elle parle d'une chose encore possible.",
        rat: "C'est la forme des demandes&nbsp;: elle ouvre quelque chose. Or vous êtes déjà "
           + "devant la porte fermée&nbsp;: il n'y a plus rien à ouvrir. Retenez ce mot "
           + "«&nbsp;voudrais&nbsp;»&nbsp;: on le rencontrera encore, et c'est lui qui fait "
           + "tomber la moitié des élèves à l'écrit." },
      { txt: "«&nbsp;Je devrais téléphoner avant de venir.&nbsp;»",
        rat_t: "C'est un bon conseil — pour la prochaine fois.",
        rat: "Elle dit ce qu'il serait sage de faire <b>maintenant ou plus tard</b>. Un collègue "
           + "à qui vous la dites comprendra que vous n'avez pas encore appelé et que vous "
           + "pouvez le faire. Ce n'est pas votre situation&nbsp;: le déplacement est fait." },
    ],
    pourquoi: "La première. Gardez-la en tête&nbsp;: elle revient au dernier écran, et vous "
            + "verrez ce qui l'a changée.",
    attente: "Choisissez une réponse pour continuer.",
  },

  // ── 2. On trie AVANT de savoir. C'est ici que le point se sépare. ────────
  {
    id:   'tri-encore-possible',
    type: 'tri',
    eye:  'À vous de trancher',
    menu: 'Huit phrases',
    titre: "Huit phrases entendues cette semaine. Est-ce qu'on peut encore agir ?",
    consigne: "Aucune règle ne vous a été donnée — normal. Une seule question&nbsp;: après cette "
            + "phrase, la personne peut-elle encore faire quelque chose, ou est-ce joué&nbsp;?",
    colonnes: [
      { id: 'ouvert', t: "On peut encore agir", b: "On peut encore agir" },
      { id: 'joue',   t: "C'est joué",          b: "C'est joué" },
    ],
    items: [
      { txt: "Je devrais relire mon contrat avant de signer.", sous: "chez un propriétaire", ok: 'ouvert',
        rat: "Le contrat n'est pas signé. La personne se donne une consigne pour tout de suite&nbsp;: "
           + "rien n'est perdu.",
        pourquoi: "Rien n'est signé : tout reste possible." },
      { txt: "J'aurais dû relire mon contrat avant de signer.", sous: "trois mois plus tard", ok: 'joue',
        rat: "Le contrat est signé depuis trois mois. La phrase ne prépare rien&nbsp;: elle regarde "
           + "en arrière une décision qu'on ne reprendra pas.",
        pourquoi: "C'est signé. La phrase regarde en arrière." },
      { txt: "Tu pourrais m'envoyer le fichier ce matin ?", sous: "un texto à un collègue", ok: 'ouvert',
        rat: "C'est une demande. Le collègue a sa matinée devant lui, et il peut répondre oui.",
        pourquoi: "Une demande : le collègue peut encore l'envoyer." },
      { txt: "Tu aurais pu m'envoyer le fichier ce matin.", sous: "le même collègue, en fin de journée", ok: 'joue',
        rat: "La matinée est passée. Ce n'est plus une demande — c'est un reproche, et ça s'entend&nbsp;: "
           + "on y revient à l'écran 7.",
        pourquoi: "La matinée est passée : c'est un reproche." },
      { txt: "Il faudrait prévenir le propriétaire du dégât.", sous: "une conversation entre voisins", ok: 'ouvert',
        rat: "Personne n'a encore appelé, et la phrase sert justement à lancer le geste.",
        pourquoi: "Personne n'a appelé : le geste reste à faire." },
      { txt: "Il aurait fallu prévenir le propriétaire du dégât.", sous: "la semaine suivante, devant l'assureur", ok: 'joue',
        rat: "L'assureur constate ce qui manque au dossier. Personne ne peut retourner prévenir la "
           + "semaine dernière&nbsp;: la phrase règle des comptes avec le passé.",
        pourquoi: "On ne prévient pas la semaine dernière." },
      { txt: "Je voudrais un rendez-vous avec la conseillère.", sous: "au guichet du centre", ok: 'ouvert',
        rat: "La forme la plus courante de la demande polie. Elle attend une réponse&nbsp;: «&nbsp;oui, "
           + "mardi à neuf heures&nbsp;».",
        pourquoi: "Une demande polie : elle attend une réponse." },
      { txt: "J'aurais voulu un rendez-vous avec la conseillère.", sous: "le lendemain, en sortant", ok: 'joue',
        rat: "Celui-là trompe, parce que les deux phrases se ressemblent beaucoup. Mais la seconde "
           + "constate qu'on ne l'a pas eu&nbsp;: c'est un regret, et le guichet est fermé.",
        pourquoi: "Le rendez-vous n'a pas été obtenu." },
    ],
    attente: "Tranchez les huit phrases pour continuer.",
  },

  // ── 3. La règle, écrite comme un constat de ce qu'il vient de faire. ─────
  {
    id:   'le-test',
    type: 'notion',
    eye:  'Ce que vous venez de faire',
    menu: 'Le test',
    titre: "Vous avez trié sur un mot de plus, pas sur le sens des phrases.",
    paras: [
      "Regardez vos deux colonnes. À gauche, un seul mot porte le verbe&nbsp;: <i>devrais</i>, "
      + "<i>pourrais</i>, <i>faudrait</i>, <i>voudrais</i>. À droite, il y en a <b>deux</b>&nbsp;: "
      + "<i>aurais dû</i>, <i>aurais pu</i>, <i>aurait fallu</i>, <i>aurais voulu</i>. Vous n'avez "
      + "pas eu besoin de le savoir pour trier juste — mais c'est bien ce que vous avez lu.",

      "<b>Le test, à appliquer sur n'importe quelle phrase&nbsp;:</b> comptez les mots du verbe. "
      + "<b>Un seul mot</b>, la chose est encore possible. <b>Deux mots, dont le second finit "
      + "comme un participe</b> (<i>dû</i>, <i>pu</i>, <i>fallu</i>, <i>voulu</i>, <i>parlé</i>, "
      + "<i>fini</i>)&nbsp;: la chose ne se fera plus.",

      "Ces deux mots s'appellent le <b>conditionnel passé</b>&nbsp;: le verbe <i>avoir</i> à la "
      + "forme polie que vous connaissez déjà, plus le participe. Vous n'avez pas besoin du nom "
      + "pour vous en servir, mais votre enseignant l'emploiera.",
    ],
    retenir: "Un mot&nbsp;: c'est encore possible. <b>Deux mots, dont un participe&nbsp;: c'est "
           + "joué.</b>",
    attente: "Lisez, puis continuez.",
  },

  // ── 4. Le piège de l'obligation réellement remplie. ──────────────────────
  {
    id:   'jai-du-ou-jaurais-du',
    type: 'verif',
    eye:  'Le piège',
    menu: '« J\'ai dû »',
    titre: "« J'ai dû partir à midi » et « j'aurais dû partir à midi » : une seule dit un regret.",
    consigne: "Nadia est partie à midi, elle n'avait pas le choix, et elle l'explique à son "
            + "employeur le lendemain. Quelle phrase écrit-elle&nbsp;?",
    options: [
      { txt: "«&nbsp;J'ai dû partir à midi&nbsp;: ma fille était malade.&nbsp;»", juste: true },
      { txt: "«&nbsp;J'aurais dû partir à midi&nbsp;: ma fille était malade.&nbsp;»",
        rat_t: "Celle-là dit à votre employeur que vous n'êtes pas partie.",
        rat: "Les deux mots la font basculer dans le regret&nbsp;: elle raconte un départ qui "
           + "<b>n'a pas eu lieu</b>. Nadia est bel et bien partie&nbsp;; sa phrase raconterait "
           + "donc autre chose que sa journée. C'est la faute la plus coûteuse du point&nbsp;: "
           + "elle ne casse aucune règle, elle change les faits." },
      { txt: "«&nbsp;Je devais partir à midi&nbsp;: ma fille était malade.&nbsp;»",
        rat_t: "Elle est correcte, mais elle laisse la fin en suspens.",
        rat: "«&nbsp;Je devais&nbsp;» annonce une intention et laisse l'employeur se demander "
           + "si vous êtes partie ou non — on l'emploie justement quand la suite a changé "
           + "(«&nbsp;je devais partir, mais je suis restée&nbsp;»). Nadia veut dire que c'est fait." },
    ],
    pourquoi: "<b>«&nbsp;J'ai dû&nbsp;» = je l'ai fait, sans le choix. «&nbsp;J'aurais dû&nbsp;» = "
            + "je ne l'ai pas fait, et je le regrette.</b> Un seul mot d'écart, deux journées "
            + "différentes.",
    attente: "Choisissez une réponse pour continuer.",
  },

  // ── 5. Les trois verbes qui portent presque tout. ────────────────────────
  {
    id:   'trois-verbes',
    type: 'notion',
    eye:  'Ce qui suffit',
    menu: 'Trois verbes',
    titre: "Trois verbes couvrent presque tous les regrets qu'on écrit.",
    paras: [
      "<b>J'aurais dû</b> — ce qu'il fallait faire et que je n'ai pas fait&nbsp;: "
      + "«&nbsp;<i>J'aurais dû garder la facture.</i>&nbsp;» "
      + "<b>J'aurais pu</b> — ce qui était possible et que je n'ai pas fait&nbsp;: "
      + "«&nbsp;<i>J'aurais pu payer en ligne, ça m'aurait évité le déplacement.</i>&nbsp;» "
      + "<b>Il aurait fallu</b> — ce qui manquait, sans dire qui&nbsp;: "
      + "«&nbsp;<i>Il aurait fallu deux signatures.</i>&nbsp;»",

      "Ce qui vient après ne bouge jamais&nbsp;: c'est l'<b>infinitif</b>, le verbe dans sa "
      + "forme du dictionnaire. J'aurais dû <i>garder</i>, tu aurais pu <i>envoyer</i>, il "
      + "aurait fallu <i>prévenir</i>. Aucune fin de mot à choisir, aucun accord à faire&nbsp;: "
      + "c'est la partie facile, et elle est facile pour tout le monde.",

      "Une seule chose s'écrit et ne s'entend pas&nbsp;: le participe de <i>devoir</i> porte un "
      + "accent — <b>dû</b>, jamais «&nbsp;du&nbsp;». C'est ce qui distingue "
      + "«&nbsp;j'aurais dû&nbsp;» de «&nbsp;j'aurais du café&nbsp;», et un correcteur "
      + "automatique ne le voit pas toujours.",
    ],
    retenir: "<b>dû · pu · fallu</b>, puis le verbe à l'infinitif. Rien d'autre ne change.",
    attente: "Lisez, puis continuez.",
  },

  // ── 6. Trier des phrases écrites. ────────────────────────────────────────
  {
    id:   'tri-ecrites',
    type: 'tri',
    eye:  'À vous de trancher',
    menu: 'Six phrases',
    titre: "Six phrases écrites. Lesquelles sont correctes ?",
    consigne: "Regardez deux choses seulement&nbsp;: le mot qui suit «&nbsp;aurais&nbsp;», et "
            + "celui qui vient après lui.",
    colonnes: [
      { id: 'ok',   t: 'Correct',   b: 'Correct' },
      { id: 'faux', t: 'Une faute', b: 'Une faute' },
    ],
    items: [
      { txt: "J'aurais du vous prévenir plus tôt.", ok: 'faux',
        rat: "Tout le reste est juste&nbsp;: c'est l'accent qui manque. «&nbsp;<b>dû</b>&nbsp;» "
           + "avec l'accent est le participe du verbe <i>devoir</i>&nbsp;; «&nbsp;du&nbsp;» sans "
           + "accent est le petit mot de «&nbsp;du pain&nbsp;».",
        pourquoi: "Il manque l'accent : j'aurais dû." },
      { txt: "Tu aurais pu me le dire avant la réunion.", ok: 'ok',
        rat: "Deux mots pour le verbe, puis l'infinitif&nbsp;: la phrase est bien bâtie. Elle est "
           + "dure à entendre, mais elle est correcte.",
        pourquoi: "aurais pu + dire : juste." },
      { txt: "J'aurais dû envoyé les documents lundi.", ok: 'faux',
        rat: "C'est la faute de ceux qui ont bien compris qu'on parle du passé&nbsp;: ils mettent "
           + "tout au passé. Mais après <i>dû</i>, le verbe ne bouge pas&nbsp;: "
           + "«&nbsp;j'aurais dû <b>envoyer</b>&nbsp;».",
        pourquoi: "Après « dû », l'infinitif : envoyer." },
      { txt: "Il aurait fallu joindre une preuve d'achat.", ok: 'ok',
        rat: "La formule impersonnelle&nbsp;: elle constate ce qui manquait sans nommer qui aurait "
           + "dû le faire. On y revient à l'écran 8.",
        pourquoi: "Elle constate sans accuser. Juste." },
      { txt: "Nous aurions dus attendre la confirmation.", ok: 'faux',
        rat: "Le pluriel du sujet a déteint sur le participe. <i>Dû</i> ne prend jamais de "
           + "«&nbsp;s&nbsp;» ici — c'est le verbe qui suit qui porte le sens, et lui non plus ne "
           + "bouge pas&nbsp;: «&nbsp;nous aurions <b>dû attendre</b>&nbsp;».",
        pourquoi: "Aucun « s » : nous aurions dû attendre." },
      { txt: "J'aurais voulu vous rencontrer avant votre départ.", ok: 'ok',
        rat: "Un regret poli, et très utile&nbsp;: il dit qu'on a manqué quelque chose sans le "
           + "reprocher à personne. Deux mots, puis l'infinitif.",
        pourquoi: "Un regret poli, correctement bâti." },
    ],
    attente: "Tranchez les six phrases pour continuer.",
  },

  // ── 7. Le reproche : la même forme, un autre destinataire. ───────────────
  {
    id:   'le-reproche',
    type: 'verif',
    eye:  'Vérification',
    menu: 'Au travail',
    titre: "« Tu aurais pu » adressé à quelqu'un d'autre n'est plus un regret.",
    consigne: "Un collègue n'a pas transmis une commande, et le client a attendu deux jours. Vous "
            + "en parlez à la réunion d'équipe, devant tout le monde. Que dites-vous&nbsp;?",
    options: [
      { txt: "«&nbsp;Il aurait fallu transmettre la commande le mardi. On se donne quelle façon de "
           + "faire pour la suite&nbsp;?&nbsp;»", juste: true },
      { txt: "«&nbsp;Tu aurais pu transmettre la commande, quand même.&nbsp;»",
        rat_t: "Rien n'est faux dans la phrase — c'est l'endroit qui ne va pas.",
        rat: "Elle est correctement bâtie, et elle se dit très bien entre amis. Mais devant "
           + "l'équipe, «&nbsp;tu aurais pu&nbsp;» nomme un responsable et n'offre aucune sortie&nbsp;: "
           + "votre collègue se défendra au lieu de régler la commande. Le «&nbsp;quand même&nbsp;» "
           + "à la fin ajoute encore du reproche." },
      { txt: "«&nbsp;J'aurais dû vérifier moi-même que la commande était partie.&nbsp;»",
        rat_t: "Elle est juste, mais elle change de sujet.",
        rat: "Prendre le blâme sur soi désamorce, et c'est parfois exactement ce qu'il faut dire. "
           + "Ici, le problème n'est pas votre vérification&nbsp;: c'est un envoi qui n'est pas "
           + "parti. La phrase laisse la vraie question sans réponse." },
    ],
    pourquoi: "<b>Le regret parle de soi&nbsp;; le reproche parle de l'autre.</b> Même forme, deux "
            + "effets — et devant témoin, le second se paie. La formule impersonnelle passe "
            + "partout&nbsp;: c'est le prochain écran.",
    attente: "Choisissez une réponse pour continuer.",
  },

  // ── 8. La sortie de secours, gardée pour la fin. ─────────────────────────
  {
    id:   'il-aurait-fallu',
    type: 'notion',
    eye:  'Ce qui reste',
    menu: '« Il aurait fallu »',
    titre: "« Il aurait fallu » ne vise personne, et c'est tout son intérêt.",
    paras: [
      "On l'a gardée pour la fin parce qu'elle ne sert à rien tant qu'on ne sait pas ce qu'elle "
      + "remplace. «&nbsp;<i>Il aurait fallu envoyer le formulaire avant le 30.</i>&nbsp;» — la "
      + "phrase dit exactement ce qui manque, et personne autour de la table ne se sent accusé. "
      + "C'est la formule des comptes rendus, des réunions et des lettres officielles.",

      "Le «&nbsp;il&nbsp;» ne désigne personne&nbsp;: ce n'est ni vous, ni votre collègue. C'est le "
      + "même «&nbsp;il&nbsp;» que dans «&nbsp;il pleut&nbsp;». Rien ne s'accorde avec lui, jamais.",

      "Et quand vous voulez, au contraire, que la responsabilité se voie, vous avez les deux autres "
      + "à portée&nbsp;: <b>j'aurais dû</b> pour la prendre, <b>tu auriez pu</b> pour la donner. "
      + "Ce n'est plus une question de grammaire&nbsp;: les trois phrases sont correctes, et vous "
      + "choisissez laquelle vous voulez faire entendre.",
    ],
    retenir: "<b>Il aurait fallu…</b> dit ce qui manquait sans dire qui. C'est la formule qui passe "
           + "partout, à l'écrit comme en réunion.",
    attente: "Lisez, puis continuez.",
  },

  // ── 9. Écrire, pas reconnaître. ──────────────────────────────────────────
  {
    id:   'a-vous-decrire',
    type: 'verif',
    eye:  'Vérification',
    menu: 'Votre courriel',
    titre: "Vous écrivez à un fournisseur qui a livré en retard. Quelle version tient d'un bout à l'autre ?",
    consigne: "Vous voulez dire trois choses&nbsp;: la livraison devait arriver le 12, personne ne "
            + "vous a prévenu, et vous demandez qu'on vous avertisse la prochaine fois.",
    options: [
      { txt: "«&nbsp;La livraison devait arriver le 12. Il aurait fallu nous prévenir du retard&nbsp;; "
           + "nous aurions pu reporter l'installation.&nbsp;»", juste: true },
      { txt: "«&nbsp;La livraison devait arriver le 12. Il aurait fallu nous prévenu du retard&nbsp;; "
           + "nous aurions pu reporté l'installation.&nbsp;»",
        rat_t: "Le choix des formules est excellent. Ce sont les deux verbes qui ont suivi le passé.",
        rat: "Vous avez pris les bonnes formules, et vous les avez fait suivre d'un participe parce "
           + "que la phrase parle d'hier. Mais après <i>fallu</i> et après <i>pu</i>, le verbe reste "
           + "à l'infinitif&nbsp;: «&nbsp;il aurait fallu <b>prévenir</b>&nbsp;», «&nbsp;nous aurions "
           + "pu <b>reporter</b>&nbsp;»." },
      { txt: "«&nbsp;La livraison devait arriver le 12. Vous auriez dû nous prévenir du retard&nbsp;; "
           + "j'ai dû reporter l'installation.&nbsp;»",
        rat_t: "Elle est correcte — et elle est deux fois plus dure que ce que vous vouliez.",
        rat: "Aucune faute&nbsp;: «&nbsp;vous auriez dû&nbsp;» et «&nbsp;j'ai dû&nbsp;» sont bien "
           + "bâtis. Mais la première met la faute sur le fournisseur nommément, et la seconde "
           + "annonce que l'installation est <b>déjà</b> reportée&nbsp;: vous fermez la porte au "
           + "lieu de demander un usage pour la suite." },
    ],
    pourquoi: "L'impersonnelle pour le manquement, le conditionnel passé pour ce qui aurait pu se "
            + "faire, et l'infinitif après les deux. <b>C'est tout le point en deux lignes.</b>",
    attente: "Choisissez une réponse pour continuer.",
  },

  // ── 10. La fermeture : le même cas qu'à l'écran 1. ───────────────────────
  {
    id:   'fermeture',
    type: 'verif',
    eye:  'La dernière',
    menu: 'Pour finir',
    titre: "On revient devant le bureau fermé. Cette fois, vous écrivez à la conseillère.",
    consigne: "Vous voulez lui dire que vous vous êtes déplacé pour rien, et obtenir un rendez-vous. "
            + "Que choisissez-vous&nbsp;?",
    options: [
      { txt: "«&nbsp;Je me suis déplacé mardi&nbsp;: j'aurais dû téléphoner avant. Je voudrais "
           + "convenir d'un rendez-vous cette semaine.&nbsp;»", juste: true },
      { txt: "«&nbsp;Je me suis déplacé mardi&nbsp;: j'aurais dû téléphoner avant. J'aurais voulu "
           + "convenir d'un rendez-vous cette semaine.&nbsp;»",
        rat_t: "La première moitié est exactement juste. C'est la seconde qui ferme la porte.",
        rat: "«&nbsp;J'aurais voulu&nbsp;» est un regret&nbsp;: il dit que le rendez-vous n'aura pas "
           + "lieu. Or vous en demandez un pour cette semaine, et il est encore possible&nbsp;: "
           + "c'est «&nbsp;je voudrais&nbsp;» qu'il faut, en un seul mot." },
      { txt: "«&nbsp;Je me suis déplacé mardi&nbsp;: vous auriez dû afficher vos heures d'ouverture. "
           + "Je voudrais convenir d'un rendez-vous cette semaine.&nbsp;»",
        rat_t: "Correcte, et c'est un reproche adressé à la personne dont vous attendez un service.",
        rat: "La forme est juste, la demande est claire — mais vous ouvrez par «&nbsp;vous auriez "
           + "dû&nbsp;». Si vous tenez à parler de l'affichage, l'impersonnelle le dit sans viser "
           + "personne&nbsp;: «&nbsp;il aurait fallu que les heures soient affichées&nbsp;»." },
    ],
    pourquoi: "Vous avez fait les trois choses&nbsp;: compter les mots du verbe pour savoir si "
            + "c'est joué, garder l'infinitif après <i>dû</i>, et choisir entre le regret et la "
            + "demande selon ce qui est encore possible.",
    attente: "Choisissez une réponse pour finir.",
  },

];
