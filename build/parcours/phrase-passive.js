// ═══════════════════════════════════════════════════════════════════════════
// Point express — La phrase passive : retrouver qui a agi
//
// Savoir n7-s07 (Formes de phrases · Phrases passives). Une ORDONNANCE :
// l'enseignant l'envoie à un élève qui bute sur une lettre administrative.
// Dix minutes, dix écrans.
//
// ── Ce qui le sépare des mini-leçons existantes ────────────────────────────
// Sept mini-leçons du dépôt traitent déjà la phrase passive — dont
// `module-n7-actualite` (« La phrase passive, ou l'art de ne pas nommer »),
// `module-n7-banque`, `module-n7-emploi`, `module-n8-habitation`. Toutes
// suivent le même plan : à quoi ça sert, comment on la FABRIQUE (être +
// participe), l'accord avec le sujet, « par » et « de », les pièges d'accord.
// Un élève envoyé ici les a probablement lues : les redire ne servirait à rien.
// Les cinq écarts tenus :
//
//   1. ENTRÉE PAR LA COMPRÉHENSION, PAS PAR LA PRODUCTION. C'est l'écart
//      principal, et il est voulu : un niveau 7 se fait très bien comprendre
//      sans jamais produire un seul passif, mais il doit décoder une lettre
//      qui lui refuse quelque chose. On ne lui demande donc JAMAIS d'en
//      fabriquer une. On lui demande de dire QUI A AGI — écrans 1, 2, 7, 10 —
//      et l'accord du participe, qui occupe la moitié des mini-leçons, n'est
//      pas traité du tout : il ne sert qu'à écrire.
//   2. INDUCTIF. L'élève range six phrases d'une lettre reçue AVANT qu'on lui
//      dise ce qu'est une passive. La règle de l'écran 3 est écrite comme un
//      constat de ce qu'il vient de faire.
//   3. PARTIEL, JAMAIS LA LISTE. Aucun tableau de formation. Deux questions à
//      se poser dans l'ordre — « qui subit ? » puis « qui a fait ça ? » — qui
//      marchent sur une phrase jamais vue.
//   4. LE MÉTALANGAGE ARRIVE APRÈS. « Passive » n'est écrit qu'à l'écran 3, et
//      « agent » à l'écran 5, une fois la chose manipulée.
//   5. EXEMPLES VARIÉS, JAMAIS CEUX D'UN MODULE. Une lettre d'un programme de
//      formation, un avis de la Ville, un courriel d'employeur, un formulaire
//      scolaire. L'élève doit décoder n'importe quelle enveloppe brune.
//
// Aucun média : ces phrases arrivent par la poste et par courriel. Elles se
// lisent, elles ne s'entendent pas — c'est le sujet même du point.
// ═══════════════════════════════════════════════════════════════════════════

const PARCOURS = {
  slug:     'phrase-passive',
  titre:    "« A été refusée » : retrouver qui a agi",
  surtitre: "Point express · 10 minutes",
  niveau:   7,
  savoir:   'n7-s07',
};

const ECRANS = [

  // ── 1. Une décision, sans aucune règle donnée. ───────────────────────────
  {
    id:   'depart',
    type: 'verif',
    eye:  'Une question, pour commencer',
    menu: 'Une lettre',
    titre: "Une lettre arrive : « Votre demande a été refusée. » Qui a refusé ?",
    consigne: "Répondez avec ce que vous savez déjà — c'est fait exprès. Il n'y a rien d'autre "
            + "dans la phrase&nbsp;: c'est toute la ligne.",
    options: [
      { txt: "La phrase ne le dit pas — c'est l'organisme qui signe la lettre.", juste: true },
      { txt: "Personne&nbsp;: la demande a été refusée toute seule, par le système.",
        rat_t: "Une demande ne se refuse pas toute seule.",
        rat: "C'est l'impression exacte que la phrase veut donner, et c'est pour ça qu'elle est "
           + "écrite ainsi. Mais quelqu'un a lu votre dossier et a décidé. La phrase choisit de "
           + "ne pas le nommer&nbsp;; elle ne dit pas qu'il n'existe pas." },
      { txt: "Vous&nbsp;: c'est vous, le sujet de la phrase.",
        rat_t: "Vous êtes dans la phrase, mais vous n'y faites rien.",
        rat: "«&nbsp;Votre demande&nbsp;» est bien en tête de phrase, et c'est ce qui trompe&nbsp;: "
           + "en français, le premier groupe est d'habitude celui qui agit. Ici, c'est l'inverse — "
           + "votre demande <b>subit</b> le refus. Retenez cette bizarrerie, on y revient." },
    ],
    pourquoi: "La phrase ne nomme pas celui qui a refusé. <b>Ce n'est pas un oubli</b>, et vous "
            + "allez voir dans deux écrans comment retrouver la personne à qui parler.",
    attente: "Choisissez une réponse pour continuer.",
  },

  // ── 2. On trie AVANT de savoir. C'est ici que le point se sépare. ────────
  {
    id:   'tri-qui-agit',
    type: 'tri',
    eye:  'À vous de trancher',
    menu: 'Six lignes',
    titre: "Six lignes d'une même lettre. Dans chacune, qui fait l'action ?",
    consigne: "Aucune règle ne vous a été donnée — normal. Lisez chaque ligne et demandez-vous "
            + "simplement&nbsp;: qui <b>fait</b>&nbsp;? Si la ligne ne le dit pas, rangez-la à droite.",
    colonnes: [
      { id: 'dit',  t: "La phrase le dit",     b: "La phrase le dit" },
      { id: 'tait', t: "La phrase ne le dit pas", b: "Elle ne le dit pas" },
    ],
    items: [
      { txt: "Le comité a étudié votre dossier le 12 mars.", ok: 'dit',
        rat: "«&nbsp;Le comité&nbsp;» est en tête, et c'est lui qui étudie. Rien à chercher&nbsp;: "
           + "vous savez à qui vous adresser.",
        pourquoi: "Le comité. C'est écrit." },
      { txt: "Votre dossier a été étudié le 12 mars.", ok: 'tait',
        rat: "La même journée, la même action — et cette fois personne. Comparez les deux lignes "
           + "côte à côte&nbsp;: c'est exactement le même événement, raconté sans son auteur.",
        pourquoi: "Le même fait, sans son auteur." },
      { txt: "Une place vous a été offerte pour la session d'automne.", ok: 'tait',
        rat: "Vous recevez la place, mais qui l'offre&nbsp;? L'école, le ministère, le "
           + "programme&nbsp;? La ligne se garde bien de le dire.",
        pourquoi: "Quelqu'un offre, mais on ne sait pas qui." },
      { txt: "Nous avons transmis votre dossier au service des admissions.", ok: 'dit',
        rat: "«&nbsp;Nous&nbsp;»&nbsp;: l'organisme qui écrit se nomme lui-même. C'est rare dans "
           + "une lettre, et c'est toujours un bon signe pour vous.",
        pourquoi: "Nous — celui qui écrit se nomme." },
      { txt: "Les documents manquants devront être fournis avant le 30 mai.", ok: 'tait',
        rat: "Celui-là est le plus important de la lettre, et le plus dangereux&nbsp;: la ligne "
           + "n'a pas de sujet vivant du tout. Personne n'est nommé — pourtant quelqu'un doit "
           + "agir, et c'est <b>vous</b>.",
        pourquoi: "Personne n'est nommé — et pourtant c'est vous qui devez agir." },
      { txt: "La directrice signera votre attestation cette semaine.", ok: 'dit',
        rat: "«&nbsp;La directrice&nbsp;» agit&nbsp;: un nom, une fonction, une personne à qui "
           + "téléphoner si rien n'arrive.",
        pourquoi: "La directrice. Une personne à qui parler." },
    ],
    attente: "Tranchez les six lignes pour continuer.",
  },

  // ── 3. La règle, écrite comme un constat de ce qu'il vient de faire. ─────
  {
    id:   'les-deux-questions',
    type: 'notion',
    eye:  'Ce que vous venez de faire',
    menu: 'Les deux questions',
    titre: "Vous n'avez pas cherché la grammaire. Vous avez cherché la personne.",
    paras: [
      "Regardez votre colonne de droite&nbsp;: les trois lignes ont la même construction — "
      + "<b>a été étudié</b>, <b>vous a été offerte</b>, <b>devront être fournis</b>. À chaque "
      + "fois, la même petite pièce&nbsp;: une forme du verbe <i>être</i>, puis un participe. "
      + "Cette construction s'appelle la <b>phrase passive</b>. Son travail est de raconter une "
      + "action <b>sans nommer celui qui la fait</b>.",

      "<b>Les deux questions, à poser dans cet ordre sur n'importe quelle ligne&nbsp;:</b><br>"
      + "1. Est-ce que le premier groupe <b>fait</b> l'action, ou est-ce qu'il la <b>subit</b>&nbsp;?<br>"
      + "2. S'il la subit&nbsp;: <b>qui a fait ça&nbsp;?</b>",

      "Et quand la lettre ne répond pas à la deuxième question, la réponse est presque toujours "
      + "la même&nbsp;: <b>c'est celui qui signe la lettre</b>. C'est lui qu'on appelle, c'est son "
      + "nom qu'on écrit en haut de sa réponse.",
    ],
    retenir: "<i>Être</i> + participe = quelqu'un a agi, et on ne le nomme pas. "
           + "<b>Demandez toujours&nbsp;: qui&nbsp;?</b>",
    attente: "Lisez, puis continuez.",
  },

  // ── 4. Le piège de la ressemblance : toutes les « est + participe »
  //       ne sont pas des passives. ────────────────────────────────────────
  {
    id:   'la-ressemblance',
    type: 'verif',
    eye:  'Le cas qui trompe',
    menu: 'Deux « est partie »',
    titre: "« Elle est convoquée » et « elle est partie » se ressemblent. Une seule cache quelqu'un.",
    consigne: "Dans laquelle de ces trois phrases <b>quelqu'un d'autre</b> a fait l'action&nbsp;?",
    options: [
      { txt: "Votre conjointe est convoquée le 8 avril.", juste: true },
      { txt: "Votre conjointe est partie avant la fin de la rencontre.",
        rat_t: "Même forme, et pourtant personne d'autre n'agit.",
        rat: "«&nbsp;Est partie&nbsp;» ressemble à s'y méprendre à «&nbsp;est convoquée&nbsp;». "
           + "Mais essayez d'ajouter <b>par quelqu'un</b>&nbsp;: «&nbsp;elle est partie par "
           + "quelqu'un&nbsp;» ne veut rien dire. C'est elle qui part, toute seule&nbsp;: "
           + "c'est simplement du passé." },
      { txt: "Votre conjointe est inquiète depuis la lettre.",
        rat_t: "Ici, il n'y a même pas d'action.",
        rat: "«&nbsp;Inquiète&nbsp;» décrit un état, pas quelque chose qui arrive. Le test "
           + "fonctionne encore&nbsp;: «&nbsp;inquiète par quelqu'un&nbsp;» ne se dit pas. "
           + "Aucune personne cachée à chercher." },
    ],
    pourquoi: "<b>Le test&nbsp;: essayez d'ajouter «&nbsp;par quelqu'un&nbsp;».</b> Si la phrase "
            + "tient — «&nbsp;convoquée par quelqu'un&nbsp;» — alors une personne est cachée, et "
            + "il faut la trouver. Sinon, il n'y a personne à chercher.",
    attente: "Choisissez une réponse pour continuer.",
  },

  // ── 5. Quand la lettre nomme quand même : « par », et le « de » du
  //       programme. ─────────────────────────────────────────────────────────
  {
    id:   'quand-elle-nomme',
    type: 'notion',
    eye: 'Quand la réponse est écrite',
    menu: 'Par, et de',
    titre: "Parfois la lettre répond elle-même à votre deuxième question.",
    paras: [
      "Quand une phrase passive veut bien nommer celui qui agit, elle l'introduit par <b>par</b>, "
      + "et il arrive tout à la fin&nbsp;: «&nbsp;<i>Votre demande a été refusée <b>par le comité "
      + "d'admission</b>.</i>&nbsp;» C'est la meilleure ligne que vous puissiez lire dans une "
      + "lettre&nbsp;: elle vous donne le nom du bureau à appeler. Ce nom s'appelle "
      + "l'<b>agent</b>.",

      "Un petit nombre de verbes emploient <b>de</b> au lieu de <i>par</i>&nbsp;: "
      + "«&nbsp;<i>Ce projet est appuyé <b>de</b> tous les partenaires.</i>&nbsp;» "
      + "«&nbsp;<i>Le nouvel horaire a été bien accueilli <b>du</b> personnel.</i>&nbsp;» "
      + "Il n'y a rien à apprendre par cœur — il suffit de savoir que ce petit mot-là joue le "
      + "même rôle que <i>par</i>&nbsp;: il vous donne le nom.",

      "Le reste du temps, la fin de la phrase ne porte ni <i>par</i> ni <i>de</i>. C'est le cas "
      + "le plus fréquent, et c'est celui qui vous concerne&nbsp;: la question reste ouverte, et "
      + "c'est à vous de la poser.",
    ],
    retenir: "<b>Par</b> — et parfois <b>de</b> — annonce le nom que vous cherchiez. "
           + "Pas de <i>par</i>&nbsp;: la question reste entière.",
    attente: "Lisez, puis continuez.",
  },

  // ── 6. Trier des lignes reçues : passive ou non. ─────────────────────────
  {
    id:   'tri-passive',
    type: 'tri',
    eye:  'À vous de trancher',
    menu: 'Six lignes reçues',
    titre: "Six lignes d'avis reçus. Dans lesquelles une personne est-elle cachée ?",
    consigne: "Un seul geste&nbsp;: essayez d'ajouter «&nbsp;par quelqu'un&nbsp;» à la fin. "
            + "Si la phrase tient, quelqu'un est caché.",
    colonnes: [
      { id: 'cache', t: "Quelqu'un est caché", b: "Quelqu'un est caché" },
      { id: 'non',   t: "Personne n'agit",      b: "Personne n'agit" },
    ],
    items: [
      { txt: "La rue Beaubien sera fermée du 4 au 9 juin.", ok: 'cache',
        rat: "«&nbsp;Fermée par quelqu'un&nbsp;»&nbsp;: la phrase tient. La Ville, un "
           + "entrepreneur — l'avis ne le dit pas, mais une décision a été prise.",
        pourquoi: "La Ville, un entrepreneur. L'avis ne le dit pas." },
      { txt: "Le bureau est fermé le lundi.", ok: 'non',
        rat: "Celui-là est le plus difficile des six, parce que le mot «&nbsp;fermé&nbsp;» est le "
           + "même que dans la ligne précédente. Mais ici, il décrit un <b>état</b> habituel, pas "
           + "un geste&nbsp;: «&nbsp;le bureau est fermé par quelqu'un le lundi&nbsp;» ne se dit pas.",
        pourquoi: "Un état, pas un geste. Rien à chercher." },
      { txt: "Votre paiement a été reçu le 3 du mois.", ok: 'cache',
        rat: "Quelqu'un a encaissé, enregistré, coché quelque part. Le service de la "
           + "facturation&nbsp;— et c'est lui qu'on appelle si le montant est faux.",
        pourquoi: "Le service qui encaisse. À appeler si le montant est faux." },
      { txt: "Votre enfant est arrivé en retard trois fois ce mois-ci.", ok: 'non',
        rat: "Le verbe <i>arriver</i> se conjugue avec <i>être</i>, et c'est ce qui trompe. Mais "
           + "«&nbsp;arrivé par quelqu'un&nbsp;» ne veut rien dire&nbsp;: c'est l'enfant qui "
           + "arrive, tout seul. Du passé, pas une passive.",
        pourquoi: "L'enfant arrive lui-même. Du passé, rien de plus." },
      { txt: "Une amende de 148 $ vous a été imposée.", ok: 'cache',
        rat: "Quelqu'un a signé cette amende, et son bureau est écrit quelque part sur "
           + "l'avis&nbsp;: c'est là qu'on conteste.",
        pourquoi: "Quelqu'un a signé. C'est là qu'on conteste." },
      { txt: "Le formulaire est disponible au comptoir.", ok: 'non',
        rat: "«&nbsp;Disponible&nbsp;» n'est pas un participe qui vient d'un verbe qu'on subit&nbsp;: "
           + "c'est une qualité du formulaire, comme «&nbsp;gratuit&nbsp;» ou «&nbsp;bleu&nbsp;». "
           + "Rien ni personne n'agit.",
        pourquoi: "Une qualité, pas une action." },
    ],
    attente: "Tranchez les six lignes pour continuer.",
  },

  // ── 7. Le cas qui coûte cher : la passive qui cache une obligation. ──────
  {
    id:   'lobligation-cachee',
    type: 'verif',
    eye:  'Vérification',
    menu: 'Qui doit agir ?',
    titre: "« Les documents manquants devront être fournis avant le 30 mai. »",
    consigne: "Cette ligne est au milieu d'une lettre de trois paragraphes. "
            + "<b>Qui doit faire quelque chose&nbsp;?</b>",
    options: [
      { txt: "Vous. C'est à vous de les envoyer avant le 30 mai.", juste: true },
      { txt: "L'organisme&nbsp;: c'est lui qui doit aller chercher les documents.",
        rat_t: "La phrase ne dit pas le contraire — et c'est bien le problème.",
        rat: "Rien dans la ligne ne vous nomme, alors on peut lire ce qu'on veut. Mais posez-vous "
           + "la question de l'écran 3&nbsp;: qui a ces documents&nbsp;? Vous. C'est donc vous qui "
           + "devez les fournir. <b>Une passive sans personne, dans une lettre qui vous est "
           + "adressée, désigne presque toujours le destinataire.</b>" },
      { txt: "Personne en particulier&nbsp;: c'est une simple information.",
        rat_t: "C'est une date limite, pas une information.",
        rat: "«&nbsp;Devront&nbsp;» annonce une obligation, et une obligation appartient toujours "
           + "à quelqu'un. La phrase l'a effacé — ne l'effacez pas à votre tour&nbsp;: c'est le "
           + "genre de ligne qui fait perdre une place, un remboursement ou une session." },
    ],
    pourquoi: "<b>Une passive sans agent, dans une lettre qui vous est adressée, veut presque "
            + "toujours dire «&nbsp;vous&nbsp;».</b> Quand une ligne comme celle-là porte une "
            + "date, elle est pour vous jusqu'à preuve du contraire.",
    attente: "Choisissez une réponse pour continuer.",
  },

  // ── 8. Dit en dernier : et vous, vous n'avez pas à en écrire. ────────────
  {
    id:   'vous-nen-ecrivez-pas',
    type: 'notion',
    eye:  'Ce qui reste',
    menu: 'Et pour écrire ?',
    titre: "Vous n'avez pas besoin d'en fabriquer une seule.",
    paras: [
      "On a gardé ceci pour la fin, et c'est volontaire&nbsp;: <b>rien ne vous oblige à écrire des "
      + "phrases passives.</b> Elles servent aux organismes, qui doivent écrire à des milliers de "
      + "personnes sans nommer d'employé. Vous, vous écrivez à un bureau précis, sur votre dossier "
      + "précis. Nommer qui agit est votre avantage, pas votre faiblesse.",

      "Quand vous répondez, faites donc l'inverse de la lettre&nbsp;: remettez les personnes. "
      + "«&nbsp;<i>Votre demande a été refusée</i>&nbsp;» devient, dans votre réponse&nbsp;: "
      + "«&nbsp;<i><b>Qui</b> a refusé ma demande, et pour quelle raison&nbsp;?</i>&nbsp;» "
      + "«&nbsp;<i>Les documents devront être fournis</i>&nbsp;» devient&nbsp;: "
      + "«&nbsp;<i><b>Je vous envoie</b> les trois documents demandés.</i>&nbsp;»",

      "C'est plus court, plus clair, et ça oblige votre interlocuteur à répondre avec un nom. "
      + "Autrement dit&nbsp;: la passive est une chose que vous devez <b>lire</b>, pas une chose "
      + "que vous devez apprendre à produire.",
    ],
    retenir: "Elle vous arrive, vous ne l'écrivez pas. <b>Dans votre réponse, remettez les "
           + "personnes&nbsp;: qui, et quoi.</b>",
    attente: "Lisez, puis continuez.",
  },

  // ── 9. Écrire, pas reconnaître : répondre à la lettre. ───────────────────
  {
    id:   'votre-reponse',
    type: 'verif',
    eye:  'Vérification',
    menu: 'Votre réponse',
    titre: "Vous répondez à la lettre. Quelle version obtiendra une vraie réponse ?",
    consigne: "Trois premières lignes possibles pour votre courriel. Une seule oblige le bureau à "
            + "vous répondre avec une information.",
    options: [
      { txt: "«&nbsp;Vous m'écrivez que ma demande a été refusée. Qui a pris cette décision, et sur "
           + "quel motif&nbsp;?&nbsp;»", juste: true },
      { txt: "«&nbsp;Ma demande a été refusée sans motif et je trouve que c'est injuste.&nbsp;»",
        rat_t: "Vous reprenez leur phrase, et donc leur silence.",
        rat: "En recopiant «&nbsp;a été refusée&nbsp;», vous laissez la décision sans auteur — "
           + "exactement là où la lettre l'avait mise. Le bureau peut vous répondre sans jamais "
           + "nommer personne. Le reste de votre phrase dit ce que vous ressentez, pas ce que "
           + "vous demandez." },
      { txt: "«&nbsp;Il a été décidé que je devais recevoir une explication.&nbsp;»",
        rat_t: "Vous avez appris à en fabriquer une — et c'est ce qu'il ne faut pas faire.",
        rat: "La construction est correcte, et c'est ce qui la rend tentante. Mais elle efface "
           + "<b>vous</b>&nbsp;: on ne sait plus qui décide, ni qui demande. Écrivez "
           + "«&nbsp;<i>Je demande une explication écrite</i>&nbsp;»&nbsp;: c'est plus court, et on "
           + "sait à qui répondre." },
    ],
    pourquoi: "Vous avez rendu à la phrase les deux choses qu'elle avait retirées&nbsp;: "
            + "<b>qui a agi</b>, et <b>pourquoi</b>. C'est tout le point en une ligne.",
    attente: "Choisissez une réponse pour continuer.",
  },

  // ── 10. La fermeture : le même cas qu'à l'écran 1. ───────────────────────
  {
    id:   'fermeture',
    type: 'verif',
    eye:  'La dernière',
    menu: 'Pour finir',
    titre: "On revient à la lettre du début, avec une ligne de plus.",
    consigne: "«&nbsp;<i>Votre demande a été refusée. Une nouvelle demande pourra être déposée "
            + "après le 1<sup>er</sup> septembre.</i>&nbsp;» Que faites-vous&nbsp;?",
    options: [
      { txt: "Je téléphone à l'organisme qui signe&nbsp;: je demande qui a refusé, et je note que "
           + "c'est à moi de redéposer après le 1<sup>er</sup> septembre.", juste: true },
      { txt: "J'attends&nbsp;: la lettre dit qu'une nouvelle demande sera déposée après le "
           + "1<sup>er</sup> septembre.",
        rat_t: "C'est exactement le piège de l'écran 7, et il coûte une session.",
        rat: "«&nbsp;Pourra être déposée&nbsp;» ne nomme personne — donc rien ne dit que "
           + "l'organisme le fera. Dans une lettre qui vous est adressée, une passive sans "
           + "personne veut dire <b>vous</b>. Si vous attendez, il ne se passera rien." },
      { txt: "Je réponds tout de suite par écrit&nbsp;: «&nbsp;Il a été demandé que mon dossier "
           + "soit révisé.&nbsp;»",
        rat_t: "Vous avez repris leur façon d'écrire.",
        rat: "La phrase est correcte, mais elle efface qui demande&nbsp;: vous. Un bureau qui lit "
           + "ça ne sait pas de qui vient la demande de révision. Écrivez «&nbsp;<i>Je demande la "
           + "révision de mon dossier</i>&nbsp;» — et gardez la question de l'écran 1&nbsp;: "
           + "qui a refusé&nbsp;?" },
    ],
    pourquoi: "Vous avez fait les deux gestes du point&nbsp;: retrouver <b>qui a agi</b> quand la "
            + "phrase ne le dit pas, et comprendre que <b>c'est vous</b> quand personne n'est nommé.",
    attente: "Choisissez une réponse pour finir.",
  },

];
