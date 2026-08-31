// ═══════════════════════════════════════════════════════════════════════════
// Point express — S'opposer sans avoir l'air de se contredire
//
// Savoir n6-s02 (Connecteurs et relations logiques). Une ORDONNANCE :
// l'enseignant l'envoie à un élève dont les textes empilent les « mais », ou
// dont l'opposition se lit comme une contradiction. Dix minutes, dix écrans.
//
// ── Ce qui le sépare des mini-leçons existantes ────────────────────────────
// Six mini-leçons du dépôt traitent l'opposition, toutes par la CONCESSION et
// toutes aux niveaux 7 et 8 :
//   · `module-n7-actualite` — « La concession : donner raison pour mieux
//     objecter » ; `module-n7-habitation` — « … pour être écouté ».
//   · `module-n7-logement` — « Concéder d'abord, demander ensuite ».
//   · `module-n8-actualite` — « Concéder avant d'avancer » ;
//     `module-n8-emmenagement` — « Concéder, puis avancer » ;
//     `module-n8-habitation` — « Concéder pour être lu ».
// Toutes enseignent une stratégie d'argumentation — céder du terrain avant de
// demander — et toutes tournent autour de « bien que » et du subjonctif. Aucune
// ne distingue les DEUX RELATIONS que l'élève confond réellement : comparer
// deux faits qui coexistent, et signaler un résultat contraire à l'attente.
// Les cinq écarts tenus :
//
//   1. INDUCTIF. L'élève range huit phrases en deux relations AVANT qu'on lui
//      dise qu'il y en a deux. La règle de l'écran 3 est écrite comme un
//      constat de ce qu'il vient de faire.
//   2. PARTIEL, JAMAIS LA LISTE. Pas de tableau des connecteurs d'opposition,
//      pas de « bien que » + subjonctif — un autre point express s'en charge.
//      Un TEST unique : la deuxième moitié est-elle une surprise, ou un autre
//      cas ? Il marche sur un connecteur jamais vu.
//   3. « MAIS » EST DIT EN DERNIER (écran 8), alors que c'est le premier mot
//      que l'élève connaît. Le nommer d'entrée ferait croire que les autres
//      sont des variantes décoratives ; ils ne disent pas la même chose.
//   4. LE MÉTALANGAGE ARRIVE APRÈS. « Opposition » et « concession » ne sont
//      écrits qu'à l'écran 3, la chose triée huit fois.
//   5. EXEMPLES VARIÉS, JAMAIS CEUX D'UN MODULE. Un texto, une note de
//      service, un courriel de candidature, un compte rendu, une conversation
//      d'atelier. L'élève doit reconnaître la faute partout.
//
// Aucun média : le choix du connecteur et sa ponctuation ne s'entendent pas —
// à l'oral, une pause suffit. C'est un point d'écrit.
// ═══════════════════════════════════════════════════════════════════════════

const PARCOURS = {
  slug:     'mais-pourtant-alors-que',
  titre:    "S'opposer sans avoir l'air de se contredire",
  surtitre: "Point express · 10 minutes",
  niveau:   6,
  savoir:   'n6-s02',
};

const ECRANS = [

  // ── 1. Une décision, sans aucune règle donnée. ───────────────────────────
  {
    id:   'depart',
    type: 'verif',
    eye:  'Une question, pour commencer',
    menu: 'Deux faits',
    titre: "« J'ai envoyé mon dossier il y a six semaines. ___, je n'ai eu aucune réponse. »",
    consigne: "Répondez avec ce que vous savez déjà — ou au feeling. On expliquera après&nbsp;: "
            + "c'est fait exprès.",
    options: [
      { txt: "Pourtant", juste: true },
      { txt: "Alors que",
        rat_t: "Ce mot ne peut pas rester seul devant un point.",
        rat: "«&nbsp;Alors que&nbsp;» relie <b>deux faits dans la même phrase</b>&nbsp;: "
           + "«&nbsp;<i>Je n'ai eu aucune réponse, alors que mon voisin a été rappelé en trois "
           + "jours.</i>&nbsp;» Placé après un point, il laisse la phrase en suspens — le lecteur "
           + "attend la suite qui ne vient pas." },
      { txt: "Donc",
        rat_t: "C'est le mot du sens inverse.",
        rat: "«&nbsp;Donc&nbsp;» annonce une conséquence normale&nbsp;: on s'y attendait. Or ici "
           + "c'est le contraire — on avait toutes les raisons d'attendre une réponse, et il n'y "
           + "en a pas eu. Le mot cherché est celui de la <b>surprise</b>." },
    ],
    pourquoi: "«&nbsp;Pourtant&nbsp;». Gardez ces deux faits en tête&nbsp;: on y revient au "
            + "dernier écran, dans un courriel où la phrase ne s'écrira plus tout à fait pareil.",
    attente: "Choisissez une réponse pour continuer.",
  },

  // ── 2. On trie AVANT de savoir. C'est ici que le point se sépare. ────────
  {
    id:   'tri-relation',
    type: 'tri',
    eye:  'À vous de trancher',
    menu: 'Huit phrases',
    titre: "Huit phrases lues cette semaine. Qu'est-ce que la deuxième moitié fait ?",
    consigne: "Aucune règle ne vous a été donnée — normal. Une seule question devant chaque "
            + "phrase&nbsp;: est-ce qu'on <b>compare deux situations différentes</b>, ou est-ce "
            + "que le résultat est le <b>contraire de ce qu'on attendait</b>&nbsp;?",
    colonnes: [
      { id: 'compare',  t: "On compare deux cas", b: "On compare" },
      { id: 'surprise', t: "C'est une surprise",  b: "C'est une surprise" },
    ],
    items: [
      { txt: "Mon frère adore l'hiver, alors que moi je ne sors plus de décembre à mars.",
        sous: "une conversation d'atelier", ok: 'compare',
        rat: "Personne n'est surpris&nbsp;: deux personnes, deux goûts, et la phrase les met "
           + "côte à côte. Rien n'a mal tourné, on constate une différence.",
        pourquoi: "Deux personnes, deux goûts. On les met côte à côte." },
      { txt: "J'avais pris rendez-vous deux mois d'avance&nbsp;; pourtant, la clinique m'a "
           + "annulée la veille.",
        sous: "un message à une amie", ok: 'surprise',
        rat: "Prendre rendez-vous deux mois d'avance devait garantir la place. Le résultat "
           + "contredit ce qu'on avait le droit d'attendre — c'est ça, la surprise.",
        pourquoi: "Le résultat contredit ce qu'on attendait." },
      { txt: "Le premier logement était au sous-sol, alors que le second donnait sur la rue.",
        sous: "un compte rendu de visites", ok: 'compare',
        rat: "Deux logements, deux descriptions. La phrase range les faits l'un en face de "
           + "l'autre pour aider à choisir&nbsp;; elle n'annonce aucune déception.",
        pourquoi: "Deux logements comparés, sans déception." },
      { txt: "Il a suivi la formation au complet. Il a pourtant échoué à l'examen final.",
        sous: "une note de service", ok: 'surprise',
        rat: "Suivre la formation au complet laissait attendre la réussite. L'échec vient "
           + "démentir cette attente — et remarquez que le mot s'est glissé au milieu de la "
           + "phrase&nbsp;: il se déplace, on y reviendra.",
        pourquoi: "La formation laissait attendre la réussite." },
      { txt: "Les bureaux ferment à seize heures, alors que la ligne téléphonique répond "
           + "jusqu'à vingt heures.",
        sous: "une page de renseignements", ok: 'compare',
        rat: "Deux services, deux horaires, présentés ensemble pour qu'on s'y retrouve. C'est "
           + "une mise en parallèle, pas une plainte.",
        pourquoi: "Deux horaires mis en parallèle." },
      { txt: "J'ai relu le bail trois fois&nbsp;; pourtant, j'ai manqué la clause des frais de "
           + "retard.",
        sous: "un message à un intervenant", ok: 'surprise',
        rat: "Trois relectures auraient dû suffire. Le résultat va contre l'effort, et celui qui "
           + "écrit le souligne exprès.",
        pourquoi: "Trois relectures auraient dû suffire." },
      { txt: "Ma sœur travaille de nuit, alors que son conjoint commence à six heures du matin.",
        sous: "un texto", ok: 'compare',
        rat: "Deux horaires dans une même maison, mis face à face. La phrase explique une "
           + "situation, elle ne s'étonne de rien.",
        pourquoi: "Deux horaires dans la même maison, face à face." },
      { txt: "Le colis était marqué « fragile ». Il est pourtant arrivé écrasé.",
        sous: "une réclamation", ok: 'surprise',
        rat: "L'étiquette était là pour empêcher exactement ce qui est arrivé. C'est le cas le "
           + "plus clair de résultat contraire à l'attente.",
        pourquoi: "L'étiquette devait empêcher ce qui est arrivé." },
    ],
    attente: "Tranchez les huit phrases pour continuer.",
  },

  // ── 3. La règle, écrite comme un constat de ce qu'il vient de faire. ─────
  {
    id:   'le-test',
    type: 'notion',
    eye:  'Ce que vous venez de faire',
    menu: 'Le test',
    titre: "Vous avez séparé ce qui se compare de ce qui déçoit.",
    paras: [
      "Regardez votre colonne «&nbsp;on compare&nbsp;»&nbsp;: à chaque fois, les deux faits sont "
      + "<b>également normaux</b>. Personne n'a tort, rien n'a mal tourné, on met deux cas côte à "
      + "côte. Dans l'autre colonne, la deuxième moitié <b>dément</b> ce que la première laissait "
      + "attendre.",

      "<b>Le test, à appliquer sur n'importe quelle phrase&nbsp;:</b> ajoutez mentalement "
      + "«&nbsp;et c'est normal&nbsp;» après la deuxième moitié. Si ça passe, vous comparez — "
      + "employez <b>alors que</b> ou <b>tandis que</b>. Si ça sonne faux, c'est une surprise — "
      + "employez <b>pourtant</b>.",

      "Ces deux relations portent des noms que votre enseignant emploiera&nbsp;: comparer deux "
      + "cas, c'est l'<b>opposition</b>&nbsp;; annoncer un résultat contraire à l'attente, c'est "
      + "la <b>concession</b>. Vous n'avez pas besoin des mots pour choisir juste, mais vous les "
      + "entendrez.",
    ],
    retenir: "Ajoutez «&nbsp;et c'est normal&nbsp;». Ça passe&nbsp;: <b>alors que</b>. Ça sonne "
           + "faux&nbsp;: <b>pourtant</b>.",
    attente: "Lisez, puis continuez.",
  },

  // ── 4. Le piège central : « alors que » a deux sens. ─────────────────────
  {
    id:   'alors-que-deux-sens',
    type: 'verif',
    eye:  'Le piège du double sens',
    menu: 'Deux « alors que »',
    titre: "« Elle est arrivée alors que la réunion commençait. » Qu'est-ce que ça dit ?",
    consigne: "Appliquez le test de l'écran précédent, puis regardez ce qui reste.",
    options: [
      { txt: "Elle est arrivée au moment où la réunion commençait.", juste: true },
      { txt: "Elle est arrivée, et c'est étonnant vu que la réunion commençait.",
        rat_t: "Vous cherchez une surprise, et il n'y en a pas.",
        rat: "Rien n'est démenti ici&nbsp;: arriver au début d'une réunion n'a rien d'inattendu. "
           + "Le mot ne dit d'ailleurs jamais la surprise — c'est «&nbsp;pourtant&nbsp;» qui la "
           + "porte. Ici, il ne fait que situer un <b>moment</b>." },
      { txt: "Elle est arrivée, contrairement aux autres, qui commençaient la réunion.",
        rat_t: "C'est la lecture « comparaison », et elle est la plus tentante.",
        rat: "Vous avez appliqué ce qui marchait aux huit phrases précédentes, et c'était "
           + "raisonnable. Mais «&nbsp;alors que&nbsp;» a <b>deux emplois</b>&nbsp;: comparer, et "
           + "dire le moment — comme «&nbsp;pendant que&nbsp;». C'est le contenu de la phrase qui "
           + "tranche, jamais le mot seul. Ici, on parle d'une heure d'arrivée." },
    ],
    pourquoi: "<b>«&nbsp;Alors que&nbsp;» sert deux fois&nbsp;:</b> comparer deux cas, ou situer "
            + "un moment. Quand le doute est possible à l'écrit, «&nbsp;<b>tandis que</b>&nbsp;» "
            + "pour comparer et «&nbsp;<b>au moment où</b>&nbsp;» pour l'heure lèvent l'ambiguïté.",
    attente: "Choisissez une réponse pour continuer.",
  },

  // ── 5. Où chaque mot se pose, et la ponctuation qui va avec. ─────────────
  {
    id:   'la-place',
    type: 'notion',
    eye:  'La deuxième moitié',
    menu: 'La place des mots',
    titre: "Ils ne se posent pas au même endroit, et la ponctuation change avec.",
    paras: [
      "<b>Alors que</b> et <b>tandis que</b> ouvrent une deuxième phrase à l'intérieur de la "
      + "première&nbsp;: il faut un sujet et un verbe derrière eux, et une virgule devant. "
      + "«&nbsp;<i>Le loyer est resté le même, alors que le chauffage a doublé.</i>&nbsp;» Ils "
      + "peuvent aussi commencer la phrase&nbsp;: «&nbsp;<i>Alors que le chauffage a doublé, le "
      + "loyer est resté le même.</i>&nbsp;»",

      "<b>Pourtant</b> n'ouvre rien&nbsp;: il se glisse dans une phrase qui se tient déjà toute "
      + "seule, et il se déplace. En tête après un point ou un point-virgule — "
      + "«&nbsp;<i>Pourtant, personne ne m'a rappelée.</i>&nbsp;» — ou au milieu, juste après le "
      + "verbe&nbsp;: «&nbsp;<i>Personne ne m'a pourtant rappelée.</i>&nbsp;» Les deux sont "
      + "corrects&nbsp;; la seconde est plus posée.",

      "<b>Cependant</b> et <b>toutefois</b> se placent comme «&nbsp;pourtant&nbsp;» et disent la "
      + "même chose en plus formel — ce sont eux qu'on écrit dans un courriel de travail. "
      + "<b>Par contre</b> a le même sens mais reste familier&nbsp;: parfait dans un texto, à "
      + "éviter dans une lettre.",
    ],
    retenir: "«&nbsp;Alors que&nbsp;» attend une phrase derrière lui. "
           + "«&nbsp;Pourtant&nbsp;» s'insère dans une phrase déjà complète et se déplace.",
    attente: "Lisez, puis continuez.",
  },

  // ── 6. Trier des phrases écrites. ────────────────────────────────────────
  {
    id:   'tri-ecrites',
    type: 'tri',
    eye:  'À vous de trancher',
    menu: 'Six phrases',
    titre: "Six phrases écrites. Lesquelles tiennent ?",
    consigne: "Deux choses à vérifier&nbsp;: la relation est-elle la bonne (comparaison ou "
            + "surprise), et le mot a-t-il derrière lui ce qu'il réclame&nbsp;?",
    colonnes: [
      { id: 'ok',   t: 'Correct',   b: 'Correct' },
      { id: 'faux', t: 'Une faute', b: 'Une faute' },
    ],
    items: [
      { txt: "J'ai payé le premier du mois, pourtant j'ai reçu un avis de retard.", ok: 'ok',
        rat: "Payer à temps devait empêcher l'avis&nbsp;: le résultat dément l'attente, et le mot "
           + "est le bon. La virgule suffit à l'accrocher.",
        pourquoi: "Le résultat dément l'attente. Juste." },
      { txt: "Mon horaire est de jour, pourtant celui de ma collègue est de soir.", ok: 'faux',
        rat: "Rien de surprenant&nbsp;: deux personnes, deux horaires, et c'est normal. Ce sont "
           + "deux cas mis en parallèle&nbsp;: «&nbsp;<b>alors que</b> celui de ma collègue est de "
           + "soir&nbsp;».",
        pourquoi: "Deux cas normaux : « alors que », pas « pourtant »." },
      { txt: "Le premier appartement était bruyant, alors que le second donnait sur une ruelle "
           + "tranquille.", ok: 'ok',
        rat: "Comparaison franche, virgule devant, sujet et verbe derrière. Les deux "
           + "vérifications passent.",
        pourquoi: "Deux logements comparés, construction complète. Juste." },
      { txt: "J'ai relu le contrat. Alors que je n'ai rien vu.", ok: 'faux',
        rat: "Deux problèmes d'un coup&nbsp;: la relation est une surprise (relire aurait dû "
           + "suffire), et le mot reste suspendu après un point sans deuxième fait à comparer. "
           + "«&nbsp;<b>Je n'ai pourtant rien vu.</b>&nbsp;»",
        pourquoi: "Une surprise, et « alors que » reste suspendu." },
      { txt: "Bien que le loyer soit élevé, mais le logement est proche du métro.", ok: 'faux',
        rat: "L'opposition est dite <b>deux fois</b>&nbsp;: une fois par «&nbsp;bien que&nbsp;», "
           + "une fois par «&nbsp;mais&nbsp;». Il faut en retirer un — «&nbsp;<i>Bien que le loyer "
           + "soit élevé, le logement est proche du métro</i>&nbsp;» ou «&nbsp;<i>Le loyer est "
           + "élevé, mais le logement est proche du métro</i>&nbsp;».",
        pourquoi: "L'opposition est dite deux fois : il faut en retirer une." },
      { txt: "Les frais sont payables en ligne&nbsp;; toutefois, le guichet reste ouvert le "
           + "samedi.", ok: 'ok',
        rat: "Deux phrases complètes, un point-virgule, et le connecteur en tête de la seconde. "
           + "C'est la construction des avis officiels, et elle est juste.",
        pourquoi: "Deux phrases complètes, connecteur bien placé. Juste." },
    ],
    attente: "Tranchez les six phrases pour continuer.",
  },

  // ── 7. Ce qu'on écrit, et à qui. ─────────────────────────────────────────
  {
    id:   'ce-quon-ecrit',
    type: 'verif',
    eye:  'Vérification',
    menu: "À l'écrit",
    titre: "Vous répondez à une offre d'emploi. Vous n'avez pas toute l'expérience demandée.",
    consigne: "Vous voulez le dire sans vous éliminer, et faire lire ce qui suit.",
    options: [
      { txt: "«&nbsp;Je n'ai pas les cinq ans demandés&nbsp;; j'ai toutefois occupé ce poste "
           + "pendant trois ans dans un centre semblable.&nbsp;»",
        juste: true },
      { txt: "«&nbsp;Je n'ai pas les cinq ans demandés. Pourtant j'ai occupé ce poste pendant "
           + "trois ans.&nbsp;»",
        rat_t: "Le mot est bon, le registre ne l'est pas tout à fait.",
        rat: "«&nbsp;Pourtant&nbsp;» dit bien la surprise, et rien n'est faux. Mais dans une "
           + "lettre de candidature, il sonne un peu vif — comme si vous répliquiez à "
           + "l'employeur. «&nbsp;<b>Toutefois</b>&nbsp;» et «&nbsp;<b>cependant</b>&nbsp;» disent "
           + "exactement la même chose sur un ton de lettre." },
      { txt: "«&nbsp;Je n'ai pas les cinq ans demandés, alors que j'ai occupé ce poste pendant "
           + "trois ans.&nbsp;»",
        rat_t: "La relation choisie n'est pas la bonne.",
        rat: "«&nbsp;Alors que&nbsp;» met deux faits sur le même plan, comme deux cas également "
           + "normaux&nbsp;: la phrase se lit comme si vous constatiez froidement l'écart. Or "
           + "vous voulez dire que la seconde moitié <b>vient corriger</b> l'impression laissée "
           + "par la première. C'est une concession, pas une comparaison." },
    ],
    pourquoi: "<b>Ce qui vient après le connecteur est ce que le lecteur retiendra.</b> On place "
            + "donc le point faible avant, et l'argument après — c'est tout l'intérêt de la "
            + "concession dans une lettre.",
    attente: "Choisissez une réponse pour continuer.",
  },

  // ── 8. « Mais », dit en dernier : c'est le mot par défaut. ───────────────
  {
    id:   'mais-en-dernier',
    type: 'notion',
    eye:  'Ce qui reste',
    menu: "Le mot « mais »",
    titre: "« Mais » fait les deux, et c'est pour ça qu'on l'a gardé pour la fin.",
    paras: [
      "On ne l'a pas nommé une seule fois jusqu'ici, exprès. <b>Mais</b> peut comparer deux cas "
      + "et annoncer une surprise&nbsp;: «&nbsp;<i>Mon horaire est de jour, mais celui de ma "
      + "collègue est de soir</i>&nbsp;» et «&nbsp;<i>J'ai payé à temps, mais j'ai reçu un "
      + "avis</i>&nbsp;» sont tous les deux corrects. C'est le mot par défaut, et il ne se trompe "
      + "jamais.",

      "Son défaut est là&nbsp;: comme il dit les deux, il ne dit pas <b>lequel</b>. Un texte où "
      + "chaque paragraphe s'articule sur «&nbsp;mais&nbsp;» oblige le lecteur à deviner à chaque "
      + "fois. Choisir «&nbsp;alors que&nbsp;» ou «&nbsp;toutefois&nbsp;» ne fait pas plus "
      + "savant&nbsp;: ça épargne un effort à celui qui lit.",

      "Une seule contrainte à retenir&nbsp;: il se met <b>au milieu</b>, après une virgule, et il "
      + "ne se double jamais. «&nbsp;<i>Bien que… mais…</i>&nbsp;», "
      + "«&nbsp;<i>Malgré… mais…</i>&nbsp;»&nbsp;: l'opposition est déjà dite, le second mot est "
      + "de trop. C'est la faute la plus fréquente au niveau 6, et elle ne s'entend presque pas "
      + "à l'oral.",
    ],
    retenir: "<b>Mais</b> ne se trompe jamais, et ne précise rien. Une opposition ne se dit "
           + "qu'<b>une seule fois</b> dans une phrase.",
    attente: "Lisez, puis continuez.",
  },

  // ── 9. Écrire, pas reconnaître. ──────────────────────────────────────────
  {
    id:   'a-vous-decrire',
    type: 'verif',
    eye:  'Vérification',
    menu: 'Votre message',
    titre: "Un message à un propriétaire. Quelle version tient d'un bout à l'autre ?",
    consigne: "Nadia a signalé le chauffage il y a trois semaines et rien n'a bougé. Elle ajoute "
            + "que le logement voisin, lui, a été réparé. Trois versions&nbsp;: une seule est "
            + "correcte partout.",
    options: [
      { txt: "J'ai signalé le problème il y a trois semaines&nbsp;; rien n'a pourtant été fait, "
           + "alors que le logement voisin a été réparé en deux jours.",
        juste: true },
      { txt: "J'ai signalé le problème il y a trois semaines&nbsp;; rien n'a pourtant été fait, "
           + "pourtant le logement voisin a été réparé en deux jours.",
        rat_t: "La première moitié est juste. C'est la seconde qui répète.",
        rat: "«&nbsp;Rien n'a pourtant été fait&nbsp;» est exactement la bonne relation&nbsp;: un "
           + "signalement devait mener à une réparation. Mais la comparaison avec le voisin n'est "
           + "pas une surprise de plus — ce sont deux cas mis face à face, donc "
           + "«&nbsp;<b>alors que</b>&nbsp;»." },
      { txt: "Bien que j'aie signalé le problème il y a trois semaines, mais rien n'a été fait, "
           + "alors que le logement voisin a été réparé en deux jours.",
        rat_t: "La fin est parfaite. C'est le début qui dit l'opposition deux fois.",
        rat: "«&nbsp;Alors que le logement voisin…&nbsp;» est juste&nbsp;: une vraie comparaison. "
           + "Mais «&nbsp;bien que&nbsp;» et «&nbsp;mais&nbsp;» font le même travail dans la même "
           + "phrase&nbsp;: il faut en retirer un. La phrase est trop chargée pour un message "
           + "qu'on veut voir traité." },
    ],
    pourquoi: "Une surprise, puis une comparaison, chacune dite une seule fois avec son mot. "
            + "<b>C'est tout le point en une phrase.</b>",
    attente: "Choisissez une réponse pour continuer.",
  },

  // ── 10. La fermeture : le même cas qu'à l'écran 1. ───────────────────────
  {
    id:   'fermeture',
    type: 'verif',
    eye:  'La dernière',
    menu: 'Pour finir',
    titre: "On revient au début : six semaines, et aucune réponse.",
    consigne: "Cette fois, ce n'est plus une remarque à une amie&nbsp;: vous écrivez au bureau "
            + "qui a votre dossier, et vous voulez une réponse. Que choisissez-vous&nbsp;?",
    options: [
      { txt: "«&nbsp;J'ai transmis mon dossier le 12 mai&nbsp;; je n'ai toutefois reçu aucun "
           + "accusé de réception à ce jour.&nbsp;»",
        juste: true },
      { txt: "«&nbsp;J'ai transmis mon dossier le 12 mai. Pourtant, je n'ai eu aucune "
           + "réponse.&nbsp;»",
        rat_t: "C'est la phrase de l'écran 1 — et elle était juste là-bas.",
        rat: "La relation est la bonne et rien n'est incorrect. Mais elle a changé de "
           + "destinataire&nbsp;: devant un bureau, «&nbsp;pourtant&nbsp;» en tête sonne comme un "
           + "reproche, et un reproche fait répondre sur la forme plutôt que sur le fond. "
           + "«&nbsp;Toutefois&nbsp;» dit la même chose et laisse la demande intacte." },
      { txt: "«&nbsp;J'ai transmis mon dossier le 12 mai, alors que je n'ai reçu aucune "
           + "réponse.&nbsp;»",
        rat_t: "Le ton est meilleur, la relation est fausse.",
        rat: "«&nbsp;Alors que&nbsp;» met les deux faits sur le même plan, comme s'il était normal "
           + "d'envoyer un dossier et normal de n'avoir pas de réponse. Or c'est justement ce que "
           + "vous contestez&nbsp;: l'envoi devait entraîner un accusé de réception. C'est une "
           + "surprise, pas une comparaison." },
    ],
    pourquoi: "Vous avez fait les trois choses&nbsp;: distinguer la comparaison de la surprise, "
            + "poser le mot là où sa construction l'exige, et l'ajuster à la personne qui va lire.",
    attente: "Choisissez une réponse pour finir.",
  },

];
