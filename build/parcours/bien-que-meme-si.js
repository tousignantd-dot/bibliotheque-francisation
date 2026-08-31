// ═══════════════════════════════════════════════════════════════════════════
// Point express — Donner un point sans céder le vôtre
//
// Savoirs n7-s03 (concession : bien que, malgré que, même si) et n7-s27 (le
// subjonctif obligatoire après certaines conjonctions). Une ORDONNANCE :
// l'enseignant l'envoie à un élève dont les échanges s'arrêtent à « oui,
// mais », ou qui écrit « bien que c'est ». Dix minutes, dix écrans.
//
// ── Ce qui le sépare des mini-leçons existantes ────────────────────────────
// Le dépôt en porte cinq sur la concession, et les cinq font la même chose :
// elles donnent la LISTE des marqueurs, puis un exemple par marqueur.
//   · « Bien que, même si : dire non sans casser l'équipe » — un tableau à
//     quatre entrées, dans un contexte de travail unique.
//   · « La concession : donner raison pour mieux objecter » et « … pour être
//     écouté » — deux formulations d'un même conseil de ton, sans jamais dire
//     où le verbe change.
//   · « Accorder quelque chose, et maintenir quand même » — le mot d'ordre,
//     pas le moyen.
// Un élève qui les a lues sait qu'il faut concéder et ne sait toujours pas
// écrire la phrase. Les cinq écarts tenus :
//
//   1. INDUCTIF, ET SUR UNE QUESTION QUI N'EST PAS GRAMMATICALE. L'écran 2 ne
//      demande pas de reconnaître un marqueur : il demande QUELLE MOITIÉ de
//      la phrase la personne défend. L'élève découvre seul que la moitié qui
//      porte le marqueur est celle qu'on abandonne.
//   2. PARTIEL, JAMAIS LA LISTE. Aucun tableau de conjonctions ni de
//      subjonctif. Un TEST à deux temps : « bien que » veut une forme de
//      verbe qu'on n'est pas sûr d'écrire ; « même si » n'en veut aucune —
//      donc en cas de doute, on écrit « même si », et la phrase est juste.
//   3. LE CAS PAR DÉFAUT EN DERNIER. L'ORDRE des deux moitiés (écran 8) est
//      ce qui décide si la lettre est lue jusqu'au bout, et c'est justement
//      ce qu'aucune conjugaison ne dit.
//   4. LE MÉTALANGAGE APRÈS. « Concession » et « subjonctif » n'apparaissent
//      qu'aux écrans 3 et 5, la chose ayant été maniée huit fois.
//   5. EXEMPLES VARIÉS, JAMAIS CEUX D'UN MODULE. Une négociation de loyer, un
//      refus d'employeur, un cours exigeant, un colis abîmé, une réunion de
//      voisins, une lettre à un service à la clientèle.
//
// Aucun média : « bien que le loyer soit » et « bien que le loyer est » se
// distinguent à l'écrit, et l'élève à qui l'on envoie ce point l'écrit.
// ═══════════════════════════════════════════════════════════════════════════

const PARCOURS = {
  slug:     'bien-que-meme-si',
  titre:    "Donner un point sans céder le vôtre",
  surtitre: "Point express · 10 minutes",
  niveau:   7,
  savoir:   'n7-s03 · n7-s27',
};

const ECRANS = [

  // ── 1. Une décision, sans aucune règle donnée. ───────────────────────────
  {
    id:   'depart',
    type: 'verif',
    eye:  'Une question, pour commencer',
    menu: 'Trois réponses',
    titre: "Votre propriétaire annonce une hausse de 40 $. Quelle réponse garde votre position ?",
    consigne: "Il vous explique que les taxes municipales ont augmenté — et c'est vrai. Vous "
            + "trouvez la hausse trop forte. Répondez avec ce que vous savez déjà&nbsp;: c'est "
            + "fait exprès.",
    options: [
      { txt: "«&nbsp;Bien que les taxes aient augmenté, une hausse de 40&nbsp;$ reste trop forte "
           + "pour moi.&nbsp;»", juste: true },
      { txt: "«&nbsp;Les taxes ont augmenté, donc une hausse de 40&nbsp;$ est normale.&nbsp;»",
        rat_t: "Vous venez de lui donner raison sur toute la ligne.",
        rat: "«&nbsp;Donc&nbsp;» tire une conséquence&nbsp;: vous acceptez son argument <b>et</b> "
           + "sa conclusion. La phrase est parfaitement correcte, et elle met fin à la "
           + "discussion — dans son sens à lui." },
      { txt: "«&nbsp;Les taxes n'ont pas augmenté tant que ça.&nbsp;»",
        rat_t: "Vous déplacez la discussion sur un terrain qu'il connaît mieux que vous.",
        rat: "Contredire le fait vous oblige à sortir des chiffres, et c'est lui qui a le compte "
           + "de taxes. Vous perdez votre vrai sujet — le montant de la hausse — sans l'avoir "
           + "défendu une seule fois." },
    ],
    pourquoi: "La première. Elle accorde le fait <b>et</b> maintient votre position. Gardez-la en "
            + "tête&nbsp;: elle revient au dernier écran, par écrit cette fois.",
    attente: "Choisissez une réponse pour continuer.",
  },

  // ── 2. On trie AVANT de savoir, et sur une question non grammaticale. ────
  {
    id:   'tri-quelle-moitie',
    type: 'tri',
    eye:  'À vous de trancher',
    menu: 'Huit phrases',
    titre: "Huit phrases en deux moitiés. Laquelle la personne défend-elle vraiment ?",
    consigne: "Aucune règle ne vous a été donnée — normal. Demandez-vous seulement ceci&nbsp;: si "
            + "l'autre ne devait retenir qu'une moitié de la phrase, laquelle voudrait-on qu'il "
            + "retienne&nbsp;?",
    colonnes: [
      { id: 'debut', t: "Le début", b: "Le début" },
      { id: 'fin',   t: "La fin",   b: "La fin" },
    ],
    items: [
      { txt: "Bien que le loyer soit élevé, l'appartement me convient.", sous: "à une amie, après une visite", ok: 'fin',
        rat: "Le prix est reconnu au passage, mais la personne dit qu'elle prend l'appartement. "
           + "C'est cette moitié-là qu'on retiendra.",
        pourquoi: "Elle prend l'appartement. Le prix est mis de côté." },
      { txt: "Je prends l'appartement, même si le loyer est élevé.", sous: "la même personne, au propriétaire", ok: 'debut',
        rat: "Les deux moitiés ont changé de place, et l'idée défendue avec elles. Ce qui compte est "
           + "en tête cette fois&nbsp;: elle prend.",
        pourquoi: "Même idée qu'au-dessus, dans l'autre ordre." },
      { txt: "Même si je comprends votre situation, je ne peux pas repousser la date.", sous: "une conseillère à un élève", ok: 'fin',
        rat: "La compréhension est réelle et elle ne change rien&nbsp;: la date tient. C'est le "
           + "refus que l'élève doit entendre.",
        pourquoi: "La date tient. Le reste est de la politesse." },
      { txt: "Je peux vous accorder une semaine, bien que le règlement dise le contraire.", sous: "la même conseillère, un autre jour", ok: 'debut',
        rat: "Elle accorde vraiment la semaine. Le règlement est mentionné pour qu'on sache que "
           + "c'est une faveur, pas pour la retirer.",
        pourquoi: "La semaine est accordée. Le règlement est en second." },
      { txt: "Vous avez raison pour le bruit ; je vais quand même garder mon chien.", sous: "entre voisins, dans l'entrée", ok: 'fin',
        rat: "Le voisin obtient qu'on lui donne raison, et rien d'autre. «&nbsp;Quand même&nbsp;» "
           + "annonce que la suite ne bougera pas.",
        pourquoi: "Le chien reste. Le reste est une politesse." },
      { txt: "Le cours est exigeant, mais il me plaît beaucoup.", sous: "à un ami qui hésite à s'inscrire", ok: 'fin',
        rat: "L'ami retiendra qu'il faut s'inscrire. La difficulté est dite d'abord pour qu'on ne "
           + "l'accuse pas de l'avoir cachée.",
        pourquoi: "Il conseille le cours. La difficulté est un préalable." },
      { txt: "Il me plaît beaucoup, ce cours, même s'il est exigeant.", sous: "le même ami, la semaine suivante", ok: 'debut',
        rat: "Même contenu, ordre inverse. La difficulté est reléguée à la fin, où elle pèse moins.",
        pourquoi: "L'ordre a changé, l'idée défendue aussi." },
      { txt: "Bien que le colis soit arrivé abîmé, je ne demande pas de remboursement.", sous: "à un service à la clientèle", ok: 'fin',
        rat: "Celui-là trompe, parce que le dommage est la chose la plus frappante de la phrase. "
           + "Mais la personne écrit pour dire qu'elle ne réclame rien&nbsp;: c'est sa décision "
           + "qui compte.",
        pourquoi: "Elle ne réclame rien. C'est ce qu'elle annonce." },
    ],
    attente: "Tranchez les huit phrases pour continuer.",
  },

  // ── 3. La règle, écrite comme un constat de ce qu'il vient de faire. ─────
  {
    id:   'la-moitie-qui-porte-le-mot',
    type: 'notion',
    eye:  'Ce que vous venez de faire',
    menu: 'Le test',
    titre: "La moitié que vous avez mise de côté portait toujours le même petit mot.",
    paras: [
      "Relisez vos huit phrases. Chaque fois, la moitié <b>abandonnée</b> commence par "
      + "<i>bien que</i>, <i>même si</i>, ou se laisse annoncer par <i>mais</i> et "
      + "<i>quand même</i>. L'autre moitié — celle sans petit mot — est celle qu'on défend. "
      + "Ce n'est pas une question de place&nbsp;: vous avez trié des débuts et des fins dans "
      + "les deux sens.",

      "<b>Le test, à appliquer sur n'importe quelle phrase&nbsp;:</b> trouvez le marqueur. Ce "
      + "qui est <b>avec lui</b> est ce que vous accordez à l'autre. Ce qui est <b>à côté</b> est "
      + "ce que vous maintenez. Écrire une phrase de ce genre, c'est donc décider d'abord de quel "
      + "côté du marqueur vous rangez chaque idée.",

      "Ce mouvement s'appelle une <b>concession</b>&nbsp;: on donne un point pour être écouté sur "
      + "le sien. C'est ce qui distingue une réclamation qu'on lit d'une réclamation qu'on classe. "
      + "Vous n'avez pas besoin du mot pour vous en servir, mais votre enseignant l'emploiera.",
    ],
    retenir: "Ce qui est <b>avec</b> le marqueur, vous le donnez. Ce qui est <b>à côté</b>, vous "
           + "le gardez.",
    attente: "Lisez, puis continuez.",
  },

  // ── 4. Le piège du verbe. ────────────────────────────────────────────────
  {
    id:   'le-verbe-apres',
    type: 'verif',
    eye:  'Le piège du verbe',
    menu: 'Le verbe',
    titre: "« Bien que le loyer est élevé » : tout le monde l'écrit, et ça ne s'écrit pas.",
    consigne: "Fatou répond par courriel à son propriétaire. Elle veut accorder que le loyer du "
            + "quartier a monté, et maintenir sa demande. Quelle ligne écrit-elle&nbsp;?",
    options: [
      { txt: "«&nbsp;Bien que les loyers du quartier <b>aient</b> monté, je vous demande d'étaler "
           + "la hausse sur deux ans.&nbsp;»", juste: true },
      { txt: "«&nbsp;Bien que les loyers du quartier <b>ont</b> monté, je vous demande d'étaler la "
           + "hausse sur deux ans.&nbsp;»",
        rat_t: "C'est la faute de ceux qui ont bien compris le sens.",
        rat: "Le fait est vrai, donc on écrit le verbe comme on l'écrit d'habitude&nbsp;: "
           + "«&nbsp;ils ont monté&nbsp;». C'est logique, et ce n'est pas ce que la langue "
           + "demande&nbsp;: après <i>bien que</i>, le verbe prend une <b>autre forme</b>. On "
           + "verra à l'écran suivant comment ne jamais avoir à la chercher." },
      { txt: "«&nbsp;Bien que les loyers du quartier <b>montent</b>, je vous demande d'étaler la "
           + "hausse sur deux ans.&nbsp;»",
        rat_t: "La forme du verbe est juste. C'est le moment qui a glissé.",
        rat: "Après <i>bien que</i>, «&nbsp;montent&nbsp;» est bien la forme attendue — mais elle "
           + "parle de ce qui monte <b>en ce moment</b>. Fatou parle d'une hausse déjà faite, "
           + "celle qui sert d'argument au propriétaire&nbsp;: il lui faut le passé." },
    ],
    pourquoi: "Après <i>bien que</i>, le verbe change de forme, et cette forme ne se devine pas "
            + "toujours. La bonne nouvelle est à l'écran suivant&nbsp;: <b>vous n'êtes jamais "
            + "obligé de la chercher.</b>",
    attente: "Choisissez une réponse pour continuer.",
  },

  // ── 5. La parade : « même si » ne demande rien. ──────────────────────────
  {
    id:   'meme-si-la-parade',
    type: 'notion',
    eye:  'La parade',
    menu: '« Même si »',
    titre: "« Même si » se construit avec le verbe que vous écrivez déjà.",
    paras: [
      "<i>Bien que</i> réclame une forme particulière du verbe — le <b>subjonctif</b>&nbsp;: "
      + "«&nbsp;bien qu'il <b>soit</b>&nbsp;», «&nbsp;bien qu'ils <b>aient</b>&nbsp;», "
      + "«&nbsp;bien que je <b>puisse</b>&nbsp;». <i>Même si</i> n'en réclame aucune&nbsp;: "
      + "«&nbsp;même s'il <b>est</b>&nbsp;», «&nbsp;même s'ils <b>ont</b>&nbsp;», «&nbsp;même si "
      + "je <b>peux</b>&nbsp;». Vous écrivez le verbe comme dans n'importe quelle phrase.",

      "<b>D'où la parade, et c'est tout ce qu'il faut retenir de cet écran&nbsp;:</b> si la forme "
      + "après <i>bien que</i> ne vient pas toute seule, écrivez <b>même si</b>. Les deux disent "
      + "la même chose, les deux s'écrivent dans une lettre officielle, et personne ne vous "
      + "reprochera d'avoir choisi celle que vous maîtrisez.",

      "Une seule différence de ton, et elle est mince&nbsp;: <i>bien que</i> sonne un peu plus "
      + "écrit, <i>même si</i> passe aussi bien à l'oral. Réservez <i>bien que</i> aux verbes "
      + "dont vous êtes sûr — ils sont peu nombreux et ce sont toujours les mêmes&nbsp;: "
      + "<i>soit</i>, <i>ait</i>, <i>puisse</i>, <i>fasse</i>.",
    ],
    retenir: "<b>Un doute sur le verbe&nbsp;? Écrivez «&nbsp;même si&nbsp;».</b> La phrase dit la "
           + "même chose et elle est juste.",
    attente: "Lisez, puis continuez.",
  },

  // ── 6. Trier des phrases écrites. ────────────────────────────────────────
  {
    id:   'tri-ecrites',
    type: 'tri',
    eye:  'À vous de trancher',
    menu: 'Six phrases',
    titre: "Six phrases écrites. Lesquelles sont correctes ?",
    consigne: "Regardez le marqueur, puis le verbe qui le suit. Rien d'autre.",
    colonnes: [
      { id: 'ok',   t: 'Correct',   b: 'Correct' },
      { id: 'faux', t: 'Une faute', b: 'Une faute' },
    ],
    items: [
      { txt: "Bien que le dossier est complet, la décision tarde.", ok: 'faux',
        rat: "Le sens est bon et l'ordre des deux moitiés aussi. Mais après <i>bien que</i>, "
           + "il faut «&nbsp;<b>soit</b> complet&nbsp;» — ou, plus simple, écrire "
           + "«&nbsp;<b>même si</b> le dossier est complet&nbsp;».",
        pourquoi: "Bien que le dossier soit complet." },
      { txt: "Même si le dossier est complet, la décision tarde.", ok: 'ok',
        rat: "La même phrase, avec le marqueur qui ne demande rien au verbe. Elle est juste et "
           + "elle dit exactement la même chose.",
        pourquoi: "« Même si » prend le verbe ordinaire." },
      { txt: "Bien qu'il ait déjà répondu, je vais le relancer.", ok: 'ok',
        rat: "«&nbsp;Ait&nbsp;» est la forme attendue après <i>bien que</i>, et c'est une des "
           + "quatre qu'on rencontre tout le temps.",
        pourquoi: "Bien qu'il ait : la forme est juste." },
      { txt: "Même s'il aurait déjà répondu, je vais le relancer.", ok: 'faux',
        rat: "Le marqueur ne demandait rien&nbsp;: c'est l'élève qui a ajouté une forme prudente "
           + "de son propre chef. Après <i>même si</i>, on écrit le fait tel qu'il est&nbsp;: "
           + "«&nbsp;même s'il <b>a</b> déjà répondu&nbsp;».",
        pourquoi: "Même s'il a déjà répondu." },
      { txt: "Le montant est élevé ; je vais quand même signer.", ok: 'ok',
        rat: "«&nbsp;Quand même&nbsp;» ne commence pas une moitié de phrase&nbsp;: il se glisse "
           + "près du verbe qu'on maintient. Rien à conjuguer autrement.",
        pourquoi: "« Quand même » se pose près du verbe." },
      { txt: "Quand même le montant est élevé, je vais signer.", ok: 'faux',
        rat: "«&nbsp;Quand même&nbsp;» n'ouvre pas une phrase&nbsp;: ce n'est pas un marqueur de "
           + "tête comme <i>bien que</i>. Ici il faut «&nbsp;<b>Même si</b> le montant est "
           + "élevé, je vais signer&nbsp;».",
        pourquoi: "« Quand même » ne s'emploie pas en tête." },
    ],
    attente: "Tranchez les six phrases pour continuer.",
  },

  // ── 7. « Quand même » : le marqueur qu'on entend le plus. ────────────────
  {
    id:   'quand-meme',
    type: 'verif',
    eye:  'Vérification',
    menu: '« Quand même »',
    titre: "« Quand même » est celui que vous entendrez le plus, et il ne s'écrit pas au même endroit.",
    consigne: "Vous avez visité un logement. Il est trop petit, et il est à cinq minutes de votre "
            + "travail. Vous décidez de le prendre et vous le dites à une amie. Que dites-vous&nbsp;?",
    options: [
      { txt: "«&nbsp;Il est petit, mais je vais quand même le prendre&nbsp;: je serai à cinq "
           + "minutes du travail.&nbsp;»", juste: true },
      { txt: "«&nbsp;Il est petit, quand même je vais le prendre&nbsp;: je serai à cinq minutes du "
           + "travail.&nbsp;»",
        rat_t: "Vous avez traité «&nbsp;quand même&nbsp;» comme «&nbsp;même si&nbsp;».",
        rat: "C'est l'erreur naturelle, puisque les deux contiennent le mot «&nbsp;même&nbsp;». "
           + "Mais <i>quand même</i> n'ouvre jamais une moitié de phrase&nbsp;: il se pose "
           + "<b>à côté du verbe</b> qu'on maintient — «&nbsp;je vais <b>quand même</b> le "
           + "prendre&nbsp;»." },
      { txt: "«&nbsp;Bien qu'il est petit, je vais le prendre&nbsp;: je serai à cinq minutes du "
           + "travail.&nbsp;»",
        rat_t: "Le bon marqueur, la mauvaise forme de verbe — et vous aviez la parade.",
        rat: "<i>Bien que</i> demande «&nbsp;bien qu'il <b>soit</b> petit&nbsp;». Et puisque c'est "
           + "une conversation avec une amie, le plus simple reste «&nbsp;même s'il est "
           + "petit&nbsp;», ou la phrase à «&nbsp;quand même&nbsp;»." },
    ],
    pourquoi: "<b>Trois places, trois marqueurs&nbsp;:</b> <i>bien que</i> et <i>même si</i> "
            + "ouvrent une moitié, <i>mais</i> fait la charnière, <i>quand même</i> se glisse "
            + "près du verbe. Le sens ne change pas&nbsp;; la place, oui.",
    attente: "Choisissez une réponse pour continuer.",
  },

  // ── 8. Ce qui décide vraiment : l'ordre. Gardé pour la fin. ──────────────
  {
    id:   'lordre-des-moities',
    type: 'notion',
    eye:  'Ce qui reste',
    menu: "L'ordre",
    titre: "L'ordre des deux moitiés décide si on vous lit jusqu'au bout.",
    paras: [
      "On a gardé ceci pour la fin parce que ça ne sert à rien tant qu'on ne sait pas bâtir la "
      + "phrase. Les deux ordres sont corrects, et ils ne produisent pas le même effet.",

      "<b>Concession d'abord&nbsp;:</b> «&nbsp;<i>Bien que votre facture soit exacte, le service "
      + "n'a jamais été rendu.</i>&nbsp;» Le lecteur voit d'abord que vous avez compris son "
      + "point de vue&nbsp;; il baisse la garde, puis reçoit le vôtre. C'est l'ordre des lettres "
      + "de réclamation et des demandes.",

      "<b>Concession à la fin&nbsp;:</b> «&nbsp;<i>Le service n'a jamais été rendu, bien que votre "
      + "facture soit exacte.</i>&nbsp;» On commence par frapper. C'est l'ordre d'un rapport ou "
      + "d'un constat, quand la relation n'est pas en jeu — et c'est le mauvais ordre quand vous "
      + "voulez obtenir quelque chose de la personne qui lit.",

      "Dans les deux cas, la moitié que vous défendez reste la même&nbsp;: celle qui n'a pas de "
      + "marqueur. Vous ne changez pas votre position&nbsp;; vous changez l'ordre dans lequel on "
      + "la reçoit.",
    ],
    retenir: "<b>Vous voulez obtenir quelque chose&nbsp;? La concession d'abord.</b> Vous "
           + "constatez&nbsp;? Votre point d'abord.",
    attente: "Lisez, puis continuez.",
  },

  // ── 9. Écrire, pas reconnaître. ──────────────────────────────────────────
  {
    id:   'a-vous-decrire',
    type: 'verif',
    eye:  'Vérification',
    menu: 'Votre lettre',
    titre: "Vous écrivez au service à la clientèle. Quelle version tient d'un bout à l'autre ?",
    consigne: "Un électroménager a été livré avec deux semaines de retard. Le marchand vous "
            + "répond que le fabricant était en rupture — c'est vrai. Vous demandez un geste "
            + "commercial, et vous voulez être lu.",
    options: [
      { txt: "«&nbsp;Même si la rupture venait du fabricant, c'est avec vous que j'ai signé le "
           + "contrat. Je vous demande un geste sur la livraison.&nbsp;»", juste: true },
      { txt: "«&nbsp;Bien que la rupture venait du fabricant, c'est avec vous que j'ai signé le "
           + "contrat. Je vous demande un geste sur la livraison.&nbsp;»",
        rat_t: "L'ordre est excellent. C'est le marqueur qui ne va pas avec ce verbe.",
        rat: "Vous avez mis la concession en tête, exactement comme il faut. Mais après <i>bien "
           + "que</i>, il faudrait «&nbsp;<b>vînt</b>&nbsp;», une forme que personne n'écrit "
           + "dans une lettre ordinaire. C'est précisément le cas où l'on remplace par "
           + "<b>même si</b>&nbsp;: la phrase devient juste sans rien perdre." },
      { txt: "«&nbsp;C'est avec vous que j'ai signé le contrat, même si la rupture venait du "
           + "fabricant. Je vous demande un geste sur la livraison.&nbsp;»",
        rat_t: "Aucune faute. Mais vous frappez avant d'avoir rien accordé.",
        rat: "La phrase est correcte et le marqueur est le bon. Seulement, vous ouvrez sur le "
           + "reproche&nbsp;: le lecteur se défend dès la première ligne. Vous demandez un "
           + "geste — c'est l'ordre «&nbsp;concession d'abord&nbsp;» qui sert votre demande." },
    ],
    pourquoi: "La concession en tête, le marqueur qui ne réclame rien au verbe, et votre demande "
            + "dans la moitié sans marqueur. <b>C'est tout le point en deux lignes.</b>",
    attente: "Choisissez une réponse pour continuer.",
  },

  // ── 10. La fermeture : le même cas qu'à l'écran 1. ───────────────────────
  {
    id:   'fermeture',
    type: 'verif',
    eye:  'La dernière',
    menu: 'Pour finir',
    titre: "On revient à la hausse de loyer. Cette fois, vous l'écrivez.",
    consigne: "Le propriétaire maintient les 40&nbsp;$ et vous demande votre réponse par écrit. "
            + "Vous acceptez le principe d'une hausse et vous contestez le montant. Que "
            + "choisissez-vous&nbsp;?",
    options: [
      { txt: "«&nbsp;Même si vos taxes ont augmenté, une hausse de 40&nbsp;$ dépasse ce que je "
           + "peux assumer. Je vous propose 20&nbsp;$ cette année et 20&nbsp;$ l'an "
           + "prochain.&nbsp;»", juste: true },
      { txt: "«&nbsp;Bien que vos taxes ont augmenté, une hausse de 40&nbsp;$ dépasse ce que je "
           + "peux assumer. Je vous propose 20&nbsp;$ cette année et 20&nbsp;$ l'an "
           + "prochain.&nbsp;»",
        rat_t: "C'est la phrase de l'écran 1, et le verbe n'a pas suivi le marqueur.",
        rat: "À l'oral, on vous aurait comprise sans broncher. À l'écrit, <i>bien que</i> demande "
           + "«&nbsp;<b>aient</b> augmenté&nbsp;» — ou bien vous employez <b>même si</b>, et vous "
           + "gardez le verbe tel quel. Vous avez les deux sorties&nbsp;; c'est celle-là qui "
           + "n'existe pas." },
      { txt: "«&nbsp;Une hausse de 40&nbsp;$ dépasse ce que je peux assumer, même si vos taxes ont "
           + "augmenté. Je ne paierai pas plus.&nbsp;»",
        rat_t: "La phrase est juste. C'est la lettre qui n'obtiendra rien.",
        rat: "Le marqueur et le verbe vont ensemble, aucun problème de langue. Mais vous ouvrez "
           + "sur le refus, vous refermez sur «&nbsp;je ne paierai pas plus&nbsp;», et vous ne "
           + "proposez rien&nbsp;: il ne reste à votre propriétaire qu'à trancher contre vous." },
    ],
    pourquoi: "Vous avez fait les trois choses&nbsp;: ranger chaque idée du bon côté du marqueur, "
            + "choisir un marqueur que votre verbe accepte, et mettre la concession en tête "
            + "puisque vous demandez quelque chose.",
    attente: "Choisissez une réponse pour finir.",
  },

];
