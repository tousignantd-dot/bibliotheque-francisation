// ═══════════════════════════════════════════════════════════════════════════
// Point express — Un mot en -ant, et la question qui décide du s
//
// Savoir n8-s16 (Noms et GN : expansions du noyau, GAdj détaché), avec
// n8-s58 (orthographier le vocabulaire des situations du cours). Une
// ORDONNANCE : l'enseignant l'envoie à un élève dont les textes portent des
// « équivalents » là où il fallait « équivalant », ou l'inverse — dans une
// demande d'équivalence, un rapport, une lettre au ministère.
//
// ── Ce qui le sépare des mini-leçons existantes ────────────────────────────
// Aucune mini-leçon du dépôt ne traite le mot en -ant pour lui-même. Quatre
// s'en approchent, et c'est le problème :
//   · « Décrire : l'accord et la place de l'adjectif »
//   · « Accorder les adjectifs quand on décrit »
//   · « Chauffé, chauffée, chauffés : l'adjectif suit le nom »
//   · « Où mettre l'adjectif »
// Toutes enseignent la même chose — un adjectif s'accorde avec son nom — et
// c'est justement cette règle, bien apprise, qui fabrique la faute : l'élève
// voit un mot collé à un nom pluriel et ajoute le s. « Des documents
// équivalant à une preuve » lui semble alors une coquille.
//
// Les cinq écarts tenus :
//
//   1. INDUCTIF, ET SUR LE SENS AVANT L'ORTHOGRAPHE. L'élève range six mots
//      en -ant sans qu'aucune règle ne soit dite, et le tri ne porte pas sur
//      le s : il porte sur ce que le mot fait dans la phrase.
//   2. UN TEST, JAMAIS LA LISTE. Pas de tableau des paires. Une question qui
//      marche sur un mot jamais vu — « est-ce que quelque chose suit, qui
//      appartient au verbe ? » — doublée d'un contrôle mécanique, l'essai de
//      la négation.
//   3. L'ORTHOGRAPHE ARRIVE APRÈS (écran 5), comme conséquence : le mot qui
//      reste un verbe garde le u et le qu du verbe.
//   4. LE CAS PAR DÉFAUT EN DERNIER (écran 8) : la grande majorité des mots
//      en -ant sont de simples adjectifs qui ne posent aucune question. Le
//      dire d'entrée ferait croire que tout est piège.
//   5. EXEMPLES PRIS À PLUSIEURS SITUATIONS, JAMAIS À UN MODULE : une demande
//      d'équivalence de diplômes, une offre d'emploi, un règlement
//      d'immeuble, un rapport d'inspection, un formulaire d'assurance.
//
// Aucun média : les deux formes se prononcent exactement pareil — c'est le
// sujet même du point. Il n'y a rien à écouter, tout est dans l'écrit.
// ═══════════════════════════════════════════════════════════════════════════

const PARCOURS = {
  slug:     'un-enfant-obeissant',
  titre:    "Un mot en -ant, et la question qui décide du s",
  surtitre: "Point express · 10 minutes",
  niveau:   8,
  savoir:   'n8-s16',
};

const ECRANS = [

  // ── 1. Une décision, sans aucune règle donnée. ───────────────────────────
  {
    id:   'depart',
    type: 'verif',
    eye:  'Une question, pour commencer',
    menu: 'Deux phrases',
    titre: "Deux phrases d'une demande d'équivalence. Laquelle est correctement écrite ?",
    consigne: "Vous joignez à votre dossier des attestations qui valent une preuve de "
            + "résidence. Répondez avec ce que vous savez déjà — ou au feeling. On expliquera "
            + "après&nbsp;: c'est fait exprès.",
    options: [
      { txt: "Je joins des documents équivalant à une preuve de résidence.", juste: true },
      { txt: "Je joins des documents équivalents à une preuve de résidence.",
        rat_t: "C'est la faute de ceux qui connaissent bien la règle de l'accord.",
        rat: "Vous avez vu un mot juste après un nom au pluriel, et vous l'avez accordé. C'est "
           + "le bon réflexe neuf fois sur dix. Ici, «&nbsp;équivalant&nbsp;» n'est pas en train "
           + "de décrire les documents&nbsp;: il dit ce qu'ils <b>font</b> — ils équivalent à une "
           + "preuve. Regardez ce qui le suit&nbsp;: «&nbsp;à une preuve&nbsp;»." },
      { txt: "Je joins des documents équivalents à une preuve de résidences.",
        rat_t: "Deux s de trop, et le second se voit tout de suite.",
        rat: "«&nbsp;Résidences&nbsp;» au pluriel n'a pas de sens ici&nbsp;: vous ne prouvez "
           + "qu'une adresse. Cette erreur-là se corrige à la relecture&nbsp;; l'autre, celle du "
           + "mot en -ant, ne se corrige que si l'on sait quoi chercher." },
    ],
    pourquoi: "Gardez la phrase en tête&nbsp;: on y revient au dernier écran, dans une version "
            + "où c'est l'autre orthographe qui sera juste.",
    attente: "Choisissez une réponse pour continuer.",
  },

  // ── 2. On trie AVANT de savoir, et pas sur le s. ─────────────────────────
  {
    id:   'tri-role',
    type: 'tri',
    eye:  'À vous de trancher',
    menu: 'Six mots en -ant',
    titre: "Six mots en -ant, tirés de vrais documents. Que fait chacun dans sa phrase ?",
    consigne: "Ne regardez pas encore l'orthographe. Pour chaque mot souligné, "
            + "demandez-vous&nbsp;: est-ce qu'il <b>décrit</b> une qualité du nom, ou est-ce "
            + "qu'il dit une <b>action</b> que ce nom fait&nbsp;?",
    colonnes: [
      { id: 'qualite', t: "Il décrit une qualité", b: "Une qualité" },
      { id: 'action',  t: "Il dit une action",     b: "Une action" },
    ],
    items: [
      { txt: "Nous cherchons des candidats <b>motivants</b> pour leur équipe.",
        sous: "une offre d'emploi", ok: 'qualite',
        rat: "Rien ne suit le mot&nbsp;: on ne dit pas qui ils motivent, ni quand. C'est une "
           + "manière d'être des candidats, comme «&nbsp;compétents&nbsp;» ou "
           + "«&nbsp;sérieux&nbsp;» — un mot qu'on pourrait remplacer par un autre adjectif.",
        pourquoi: "Une manière d'être : comme « compétents »." },
      { txt: "Les locataires <b>négligeant</b> le tri des matières recyclables recevront un avis.",
        sous: "un règlement d'immeuble", ok: 'action',
        rat: "Quelque chose suit le mot, et ce quelque chose lui appartient&nbsp;: <i>le tri des "
           + "matières recyclables</i>. Ce n'est pas une qualité des locataires, c'est ce que "
           + "certains d'entre eux font.",
        pourquoi: "Il a un complément : « négligeant quoi ? »." },
      { txt: "Le rapport signale des montants <b>différant</b> d'un relevé à l'autre.",
        sous: "un rapport de vérification", ok: 'action',
        rat: "«&nbsp;D'un relevé à l'autre&nbsp;» complète le mot&nbsp;: les montants sont en "
           + "train de différer entre deux documents. C'est un constat de mouvement, pas une "
           + "description.",
        pourquoi: "Il dit ce que les montants font entre deux relevés." },
      { txt: "Les deux offres proposent des salaires <b>équivalents</b>.",
        sous: "une comparaison d'offres d'emploi", ok: 'qualite',
        rat: "Le mot ferme la phrase&nbsp;: rien ne le suit. Il dit simplement comment sont les "
           + "salaires — pareils. On pourrait écrire «&nbsp;des salaires comparables&nbsp;» sans "
           + "rien changer d'autre.",
        pourquoi: "Rien ne suit : c'est une qualité des salaires." },
      { txt: "Toute personne <b>résidant</b> au Québec depuis un an peut faire la demande.",
        sous: "un formulaire d'admission", ok: 'action',
        rat: "«&nbsp;Au Québec depuis un an&nbsp;» dit où et depuis quand&nbsp;: ce sont des "
           + "compléments du verbe <i>résider</i>. La phrase pose une condition à remplir, elle "
           + "ne décrit personne.",
        pourquoi: "Où, et depuis quand : ce sont les compléments d'un verbe." },
      { txt: "Le comité a trouvé vos arguments <b>convaincants</b>.",
        sous: "une réponse à une demande de révision", ok: 'qualite',
        rat: "Le mot dit l'effet que les arguments produisent, comme «&nbsp;solides&nbsp;» ou "
           + "«&nbsp;clairs&nbsp;». Rien ne le suit&nbsp;: on ne dit pas <i>qui</i> ils "
           + "convainquent.",
        pourquoi: "Comme « solides » : une qualité, sans complément." },
    ],
    attente: "Tranchez les six cas pour continuer.",
  },

  // ── 3. La règle, écrite comme un constat de ce qu'il vient de faire. ─────
  {
    id:   'le-test',
    type: 'notion',
    eye:  'Ce que vous venez de faire',
    menu: 'Le test',
    titre: "Vous avez rangé les six mots sans regarder une seule fois leur terminaison.",
    paras: [
      "Relisez votre colonne «&nbsp;une action&nbsp;»&nbsp;: à chaque fois, <b>quelque chose "
      + "suit le mot et lui appartient</b> — <i>le tri des matières</i>, <i>d'un relevé à "
      + "l'autre</i>, <i>au Québec depuis un an</i>. Dans l'autre colonne, le mot est seul&nbsp;: "
      + "il ferme le groupe, ou il n'est suivi que d'un autre mot du même genre.",

      "<b>Le test, sur n'importe quel mot en -ant&nbsp;:</b> demandez-vous <i>est-ce que quelque "
      + "chose le suit, qui répond à «&nbsp;quoi&nbsp;», «&nbsp;à qui&nbsp;», «&nbsp;où&nbsp;», "
      + "«&nbsp;comment&nbsp;»&nbsp;?</i> Si oui, le mot est resté un <b>verbe</b>&nbsp;: il ne "
      + "s'accorde jamais, quel que soit le nom devant lui. Si non, c'est un <b>adjectif</b>, et "
      + "il s'accorde comme tous les adjectifs.",

      "<b>Le contrôle qui confirme&nbsp;: essayez d'y glisser une négation.</b> «&nbsp;Les "
      + "locataires <b>ne</b> négligeant <b>pas</b> le tri&nbsp;» se dit&nbsp;; «&nbsp;des "
      + "salaires ne équivalents pas&nbsp;» ne veut rien dire. Seul un verbe accepte la "
      + "négation — et un verbe ne prend jamais de s d'accord.",

      "Les deux formes portent des noms&nbsp;: la forme invariable est le <b>participe "
      + "présent</b>, celle qui s'accorde l'<b>adjectif verbal</b>. Vous n'en aviez pas besoin "
      + "pour trancher les six cas, mais un correcteur les écrira dans la marge.",
    ],
    retenir: "Quelque chose suit qui appartient au mot → c'est un verbe, <b>jamais de s</b>. "
           + "Le mot est seul → c'est un adjectif, <b>il s'accorde</b>.",
    attente: "Lisez, puis continuez.",
  },

  // ── 4. Le piège du nom pluriel juste devant. ─────────────────────────────
  {
    id:   'le-pluriel-devant',
    type: 'verif',
    eye:  'Le piège',
    menu: 'Le nom au pluriel',
    titre: "Le nom est au pluriel, et le mot en -ant est juste derrière lui.",
    consigne: "Vous rédigez une note interne. Le sens voulu&nbsp;: les employés qui remplacent "
            + "un collègue absent touchent une prime. Quelle phrase écrivez-vous&nbsp;?",
    options: [
      { txt: "Les employés remplaçant un collègue absent touchent une prime.", juste: true },
      { txt: "Les employés remplaçants un collègue absent touchent une prime.",
        rat_t: "Vous avez accordé sur «&nbsp;les employés&nbsp;», qui est juste devant.",
        rat: "C'est exactement le piège&nbsp;: le nom au pluriel colle au mot, et l'œil accorde "
           + "tout seul. Mais «&nbsp;un collègue absent&nbsp;» suit le mot et lui appartient — "
           + "on remplace <b>quelqu'un</b>. C'est donc un verbe&nbsp;: il reste nu. Le contrôle "
           + "le confirme&nbsp;: «&nbsp;les employés <b>ne</b> remplaçant <b>pas</b> un "
           + "collègue&nbsp;» se dit très bien." },
      { txt: "Les employés remplaçants touchent une prime pour un collègue absent.",
        rat_t: "L'accord devient correct, mais la phrase ne dit plus la même chose.",
        rat: "En déplaçant le complément, vous avez fabriqué un vrai adjectif — et il faut alors "
           + "bien le s. Le problème est ailleurs&nbsp;: votre note dit maintenant que la prime "
           + "est versée <i>pour</i> un collègue absent, ce qui n'est pas la règle que vous "
           + "annoncez. Déplacer les mots pour éviter une difficulté fait souvent changer le "
           + "sens." },
    ],
    pourquoi: "Le nom qui précède ne décide de rien. <b>Ce qui décide est ce qui suit</b> — et "
            + "ici, il suit un complément.",
    attente: "Choisissez une réponse pour continuer.",
  },

  // ── 5. L'orthographe, présentée comme une conséquence. ───────────────────
  {
    id:   'lorthographe-suit',
    type: 'notion',
    eye:  'La conséquence',
    menu: "L'orthographe",
    titre: "Pour quelques mots, ce n'est pas seulement le s qui change.",
    paras: [
      "Le mot resté verbe <b>garde l'orthographe du verbe</b>&nbsp;; devenu adjectif, il se "
      + "simplifie. Cela ne touche qu'une poignée de mots, mais ce sont ceux des documents "
      + "officiels&nbsp;: <i>en <b>convainquant</b> le comité</i> contre <i>des arguments "
      + "<b>convaincants</b></i>&nbsp;; <i>les articles <b>précédant</b> celui-ci</i> contre "
      + "<i>l'année <b>précédente</b></i>&nbsp;; <i>un horaire <b>fatiguant</b> les "
      + "employés</i> contre <i>une réunion <b>fatigante</b></i>.",

      "Il n'y a rien à mémoriser ici, et surtout pas une liste&nbsp;: <b>si vous savez conjuguer "
      + "le verbe, vous savez écrire la forme verbale.</b> <i>Nous convainquons</i> donne "
      + "<i>convainquant</i>&nbsp;; <i>nous fatiguons</i> donne <i>fatiguant</i>&nbsp;; "
      + "<i>nous négligeons</i> donne <i>négligeant</i>. L'adjectif, lui, s'écrit comme on "
      + "l'entend&nbsp;: <i>convaincant</i>, <i>fatigant</i>, <i>négligent</i>.",

      "Ces deux orthographes ne s'entendent pas&nbsp;: <i>équivalant</i> et <i>équivalent</i> se "
      + "prononcent exactement pareil. C'est pour cela que la faute traverse des années sans "
      + "être remarquée — elle n'existe qu'au moment où vous écrivez.",
    ],
    retenir: "Le verbe garde son orthographe de conjugaison. L'adjectif s'écrit plus "
           + "simplement — et lui seul prend un s.",
    attente: "Lisez, puis continuez.",
  },

  // ── 6. Trier des phrases écrites : correct ou faute. ─────────────────────
  {
    id:   'tri-ecrites',
    type: 'tri',
    eye:  'À vous de trancher',
    menu: 'Six phrases',
    titre: "Six phrases telles qu'elles ont été écrites. Lesquelles tiennent ?",
    consigne: "Une seule question à chaque fois&nbsp;: est-ce que quelque chose suit le mot en "
            + "-ant et lui appartient&nbsp;?",
    colonnes: [
      { id: 'ok',   t: 'Correcte',  b: 'Correcte' },
      { id: 'faux', t: 'Une faute', b: 'Une faute' },
    ],
    items: [
      { txt: "Les personnes résidant à l'extérieur du Québec doivent remplir l'annexe B.", ok: 'ok',
        rat: "«&nbsp;À l'extérieur du Québec&nbsp;» suit le mot et lui appartient&nbsp;: c'est un "
           + "verbe, il reste nu même après un nom au pluriel.",
        pourquoi: "Un complément suit : pas de s." },
      { txt: "Nous avons reçu deux offres équivalant.", ok: 'faux',
        rat: "Rien ne suit le mot&nbsp;: on ne dit pas à quoi les offres équivalent. Sans "
           + "complément, ce n'est plus un verbe mais un adjectif — «&nbsp;deux offres "
           + "<b>équivalentes</b>&nbsp;».",
        pourquoi: "Il faut « équivalentes » : rien ne suit." },
      { txt: "Le vérificateur a relevé des écarts importants et des chiffres divergents.", ok: 'ok',
        rat: "Les deux mots ferment leur groupe et disent comment sont les chiffres. Ce sont des "
           + "adjectifs ordinaires, accordés comme il faut.",
        pourquoi: "Deux adjectifs seuls, deux accords justes." },
      { txt: "Les documents précédents la signature du bail ont été perdus.", ok: 'faux',
        rat: "«&nbsp;La signature du bail&nbsp;» suit le mot&nbsp;: les documents précèdent "
           + "<b>quelque chose</b>. C'est un verbe, donc «&nbsp;précéd<b>ant</b>&nbsp;», sans s "
           + "et avec un a.",
        pourquoi: "Il faut « précédant » : un complément suit." },
      { txt: "Nous cherchons une réponse convaincante avant vendredi.", ok: 'ok',
        rat: "Le mot est seul et décrit la réponse&nbsp;: adjectif, accordé au féminin singulier, "
           + "et écrit dans sa forme simple.",
        pourquoi: "Adjectif seul : accord et orthographe simple." },
      { txt: "Des employés négligents les consignes de sécurité ont été rencontrés.", ok: 'faux',
        rat: "Deux choses en même temps&nbsp;: «&nbsp;les consignes de sécurité&nbsp;» suit le "
           + "mot, donc pas de s — et c'est la forme du verbe qu'il faut, "
           + "«&nbsp;néglige<b>a</b>nt&nbsp;», celle de <i>nous négligeons</i>.",
        pourquoi: "Il faut « négligeant » : le verbe, avec son a." },
    ],
    attente: "Tranchez les six phrases pour continuer.",
  },

  // ── 7. Le mot qui est devenu un nom, à ne pas confondre. ─────────────────
  {
    id:   'devenu-un-nom',
    type: 'verif',
    eye:  'Vérification',
    menu: 'Le troisième cas',
    titre: "Certains de ces mots sont aussi devenus des noms. Lequel écrivez-vous ?",
    consigne: "Vous rédigez l'avis d'une assemblée de copropriétaires. Vous voulez dire&nbsp;: "
            + "les gens qui habitent l'immeuble ont le droit de vote.",
    options: [
      { txt: "Les résidents de l'immeuble ont le droit de vote.", juste: true },
      { txt: "Les résidants de l'immeuble ont le droit de vote.",
        rat_t: "Vous avez appliqué la règle du verbe à un mot qui n'est plus un verbe.",
        rat: "«&nbsp;De l'immeuble&nbsp;» ne complète pas un verbe ici&nbsp;: il complète un "
           + "<b>nom</b>, comme dans «&nbsp;les locataires de l'immeuble&nbsp;». Le mot désigne "
           + "des personnes, il prend un déterminant («&nbsp;les&nbsp;») et il se met au "
           + "pluriel&nbsp;: c'est un nom, et le nom s'écrit <i>résident</i>." },
      { txt: "Les personnes résidents dans l'immeuble ont le droit de vote.",
        rat_t: "Ici, le mot redevient un verbe — et vous lui avez laissé le s.",
        rat: "«&nbsp;Dans l'immeuble&nbsp;» suit le mot et lui appartient&nbsp;: la forme juste "
           + "serait «&nbsp;les personnes <b>résidant</b> dans l'immeuble&nbsp;». Elle est "
           + "correcte, mais plus lourde que le nom tout court." },
    ],
    pourquoi: "Le repère est simple&nbsp;: si le mot porte un déterminant devant lui "
            + "(<i>les</i>, <i>un</i>, <i>ces</i>), il est devenu un <b>nom</b>. Il désigne des "
            + "personnes ou des choses, et il s'écrit comme l'adjectif.",
    attente: "Choisissez une réponse pour continuer.",
  },

  // ── 8. Le cas par défaut, dit en dernier. ────────────────────────────────
  {
    id:   'la-plupart-ne-posent-rien',
    type: 'notion',
    eye:  'Ce qui reste',
    menu: 'La majorité',
    titre: "La plupart des mots en -ant ne posent aucune question.",
    paras: [
      "On l'a gardé pour la fin exprès. <i>Un enfant obéissant, une réunion intéressante, des "
      + "résultats encourageants, une explication suffisante</i>&nbsp;: dans la vie courante, "
      + "l'immense majorité de ces mots ferment leur groupe, ne sont suivis de rien, et "
      + "s'accordent comme n'importe quel adjectif. Vous n'avez rien à surveiller.",

      "Ce qui demande une seconde d'attention tient à un seul signalement&nbsp;: <b>vous voyez un "
      + "mot en -ant, et quelque chose le suit</b>. C'est là — et seulement là — qu'il faut se "
      + "poser la question. Ailleurs, écrivez sans y penser.",

      "Et c'est dans les écrits officiels que le cas se présente&nbsp;: une demande "
      + "d'équivalence, un règlement, un formulaire, un rapport. Ce sont les documents où l'on "
      + "pose des conditions — <i>toute personne détenant…</i>, <i>les dossiers comportant…</i>, "
      + "<i>les pièces attestant…</i> — et poser une condition, c'est décrire une action.",
    ],
    retenir: "Un mot en -ant suivi de <b>rien</b>&nbsp;: accordez, sans y penser. Un mot en -ant "
           + "suivi de <b>quelque chose</b>&nbsp;: posez la question.",
    attente: "Lisez, puis continuez.",
  },

  // ── 9. Choisir une version entière, dans un document à enjeu. ────────────
  {
    id:   'la-lettre',
    type: 'verif',
    eye:  'Vérification',
    menu: 'La lettre',
    titre: "Une phrase de votre lettre au comité d'admission. Quelle version tient ?",
    consigne: "Vous voulez dire deux choses&nbsp;: vos cours suivis à l'étranger valent ceux "
            + "d'ici, et vos relevés le prouvent. Trois versions du même passage&nbsp;: une "
            + "seule est correcte de bout en bout.",
    options: [
      { txt: "Vous trouverez ci-joint des relevés attestant des cours équivalents à ceux du "
           + "programme.", juste: true },
      { txt: "Vous trouverez ci-joint des relevés attestants des cours équivalant à ceux du "
           + "programme.",
        rat_t: "Les deux mots ont été échangés&nbsp;: chacun a pris la forme de l'autre.",
        rat: "«&nbsp;Attestant&nbsp;» est suivi de «&nbsp;des cours&nbsp;» — il atteste quelque "
           + "chose, donc pas de s. «&nbsp;Équivalents&nbsp;», lui, décrit les cours et n'est "
           + "suivi que d'une comparaison&nbsp;: il s'accorde. La question est la même pour les "
           + "deux, et elle donne deux réponses différentes." },
      { txt: "Vous trouverez ci-joint des relevés attestant des cours équivalant à ceux du "
           + "programme.",
        rat_t: "Le premier mot est juste. C'est le second qui a suivi par imitation.",
        rat: "Vous avez bien vu qu'«&nbsp;attestant&nbsp;» a un complément. Mais "
           + "«&nbsp;à ceux du programme&nbsp;» n'est pas un complément du même genre&nbsp;: "
           + "c'est une comparaison, comme dans «&nbsp;des cours <i>semblables</i> à ceux du "
           + "programme&nbsp;». Le test de la négation tranche&nbsp;: on ne dit pas «&nbsp;des "
           + "cours n'équivalant pas à ceux du programme&nbsp;» dans cette phrase-ci, on dirait "
           + "«&nbsp;non équivalents&nbsp;»." },
    ],
    pourquoi: "Deux mots en -ant dans une même phrase, deux réponses différentes. <b>La question "
            + "se pose mot par mot</b>, jamais une fois pour toute la phrase.",
    attente: "Choisissez une réponse pour continuer.",
  },

  // ── 10. La fermeture : la phrase de l'écran 1, retournée. ────────────────
  {
    id:   'fermeture',
    type: 'verif',
    eye:  'La dernière',
    menu: 'Pour finir',
    titre: "On revient à la demande d'équivalence, mais la phrase a changé de forme.",
    consigne: "Cette fois, vous écrivez la ligne suivante&nbsp;: vous parlez de deux diplômes qui "
            + "ont la même valeur, sans dire à quoi ils équivalent. Que choisissez-vous&nbsp;?",
    options: [
      { txt: "Les deux diplômes sont considérés comme équivalents par le ministère.",
        juste: true },
      { txt: "Les deux diplômes sont considérés comme équivalant par le ministère.",
        rat_t: "C'était l'orthographe juste à l'écran 1 — la phrase n'est plus la même.",
        rat: "Rien ne suit le mot ici&nbsp;: on ne dit pas à quoi les diplômes équivalent. Sans "
           + "complément, ce n'est plus un verbe&nbsp;; c'est une qualité des diplômes, comme "
           + "«&nbsp;valides&nbsp;» ou «&nbsp;reconnus&nbsp;». Il s'accorde donc, et il perd son "
           + "a." },
      { txt: "Les deux diplômes sont considérés comme équivalents au programme par le ministère.",
        rat_t: "L'orthographe est juste, mais vous avez ajouté ce que la consigne demandait de "
             + "ne pas dire.",
        rat: "Le mot reste bien un adjectif — «&nbsp;au programme&nbsp;» est une comparaison, "
           + "pas un complément de verbe, exactement comme à l'écran précédent. Mais la phrase "
           + "annonce maintenant une équivalence précise que votre dossier devra prouver&nbsp;: "
           + "dans une lettre officielle, on n'affirme pas plus que ce qu'on peut appuyer." },
    ],
    pourquoi: "Vous avez fait les trois choses&nbsp;: regarder ce qui suit le mot, essayer la "
            + "négation quand le doute restait, et laisser le nom au pluriel décider de rien. "
            + "<b>Le même mot, deux phrases, deux orthographes.</b>",
    attente: "Choisissez une réponse pour finir.",
  },

];
