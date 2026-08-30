// ═══════════════════════════════════════════════════════════════════════════
// Point express — L'accord du participe passé avec avoir
//
// Savoir n8-s21. Une ORDONNANCE : l'enseignant l'envoie à un élève dont un
// texte écrit montre la faute. Dix minutes, dix écrans.
//
// ── Ce dont il s'écarte, et comment ────────────────────────────────────────
// Sept modules énoncent déjà la règle, toujours dans la même phrase et
// toujours au passage : `module-n8-emmenagement`, `module-n8-habitation`,
// `module-n8-recherche`, `module-n7-achat` — « avec avoir, le participe
// s'accorde avec le complément direct placé avant » — et l'exemple est
// toujours le relatif « que ». Elle y est un paragraphe dans une mini-leçon
// qui parle d'autre chose (le plus-que-parfait, l'irréel du passé). Aucune
// ne donne de quoi la mettre en oeuvre. Les cinq écarts :
//
//   1. INDUCTIF, ET LE TRI DONNE LA RÈGLE. L'élève range huit phrases selon
//      l'endroit où se trouve la réponse à « quoi ? » — une tâche mécanique,
//      faisable sans rien savoir. Toutes les phrases sont correctes : c'est
//      en relisant sa propre colonne, à l'écran 3, qu'il voit que les
//      participes y ont pris une lettre. La règle est le constat de son tri.
//   2. UN TEST, PAS UN ÉNONCÉ. Les sept mini-leçons donnent la règle ; ce
//      point donne le geste — poser « quoi ? » APRÈS le verbe, et regarder
//      si la réponse est déjà passée. Un énoncé se récite, un test se fait.
//   3. TROIS DÉCLENCHEURS, JAMAIS LA LISTE. Le pronom, le relatif « que »,
//      la question « quelle ». Les cas rares (en, les verbes pronominaux,
//      l'infinitif qui suit) sont laissés dehors et l'écran 5 le dit.
//   4. ON DIT QUE ÇA NE S'ENTEND PAS, PUIS ON DIT QUAND ÇA S'ENTEND.
//      L'écran 7 est celui qu'aucune mini-leçon n'écrit : « envoyé /
//      envoyée » ne se distingue pas, « écrit / écrite » et « pris / prise »
//      s'entendent parfaitement. Se relire à voix haute ne trouve donc la
//      faute que sur une poignée de verbes — et ce sont ceux où elle coûte
//      le plus cher.
//   5. LE COMPLÉMENT INDIRECT EST TRAITÉ (écran 8) parce que c'est là que le
//      test se casse : « je leur ai écrit » a bien quelque chose avant le
//      verbe, et rien ne s'accorde. Aucune des sept mini-leçons n'en parle.
//
// Ce point ne recoupe pas `passe-compose-etre-avoir.js`, qui traite le CHOIX
// de l'auxiliaire et l'accord avec ÊTRE. Aucun de ses verbes n'est repris ici
// (rester, partir, arriver, tomber, devenir, sortir, attendre, oublier,
// téléphoner, payer), ni aucun de ses personnages. Deux points express sur le
// participe passé ne doivent pas se répondre.
//
// Aucun média, et c'est le sujet même : cette faute n'existe qu'à l'écrit.
// C'est un choix défendable, et le brief l'assume.
// ═══════════════════════════════════════════════════════════════════════════

const PARCOURS = {
  slug:     'accord-participe-avoir',
  titre:    "L'accord du participe passé avec avoir",
  surtitre: "Point express · 10 minutes",
  niveau:   8,
  savoir:   'n8-s21',
};

const ECRANS = [

  // ── 1. Une décision, sans aucune règle donnée. ───────────────────────────
  {
    id:   'depart',
    type: 'verif',
    eye:  'Une question, pour commencer',
    menu: 'Deux phrases',
    titre: "Une seule de ces deux phrases est correcte. Laquelle ?",
    consigne: "Répondez avec ce que vous savez déjà — ou au feeling. On expliquera après&nbsp;: "
            + "c'est fait exprès.",
    options: [
      { txt: "Voici la lettre que j'ai écrit lundi.",
        rat_t: "Il manque une lettre à la fin de «&nbsp;écrit&nbsp;».",
        rat: "Regardez l'autre phrase&nbsp;: le même verbe y est écrit autrement. Ce n'est pas "
           + "une faute d'inattention — c'est une règle, et c'est celle qui résiste le plus "
           + "longtemps chez les gens qui écrivent bien par ailleurs." },
      { txt: "Voici la lettre que j'ai écrite lundi.", juste: true },
      { txt: "Les deux s'écrivent.",
        rat_t: "Une seule s'écrit, et la différence n'est pas cosmétique.",
        rat: "Elle ne dépend ni du sens, ni du niveau de langue, ni de qui écrit. Elle dépend "
           + "d'une seule chose, mécanique, que vous allez trouver vous-même à l'écran "
           + "suivant." },
    ],
    pourquoi: "«&nbsp;La lettre que j'ai <b>écrite</b>&nbsp;». Gardez la phrase telle quelle "
            + "pour l'instant. Notez seulement qu'on dit très bien «&nbsp;<b>j'ai écrit la "
            + "lettre</b>&nbsp;», sans rien ajouter&nbsp;: c'est le même verbe et le même "
            + "objet.",
    attente: "Choisissez une réponse pour continuer.",
  },

  // ── 2. Le tri qui donne la règle. Tâche mécanique, aucune règle donnée. ──
  {
    id:   'ou-est-le-quoi',
    type: 'tri',
    eye:  'À vous de trancher',
    menu: 'Huit phrases',
    titre: "Huit phrases. Posez « quoi ? » après le verbe, et dites où est la réponse.",
    consigne: "Les huit phrases sont correctes&nbsp;: il n'y a rien à corriger. On vous demande "
            + "seulement <b>où se trouve la réponse</b> — après le verbe, avant le verbe, ou "
            + "nulle part.",
    colonnes: [
      { id: 'apres', t: 'La réponse vient après', b: 'Après' },
      { id: 'avant', t: 'La réponse est déjà passée', b: 'Avant' },
      { id: 'rien',  t: "Il n'y a pas de réponse",  b: 'Aucune' },
    ],
    items: [
      { txt: "J'ai reçu la facture jeudi.", sous: "reçu quoi&nbsp;?", ok: 'apres',
        rat: "Vous posez la question, et la réponse arrive juste derrière&nbsp;: "
           + "«&nbsp;la facture&nbsp;». Elle est <i>après</i> le verbe.",
        pourquoi: "Reçu quoi ? — la facture, juste après." },
      { txt: "La facture que j'ai reçue jeudi.", sous: "reçue quoi&nbsp;?", ok: 'avant',
        rat: "Vous posez la question et il n'y a rien derrière. La réponse est «&nbsp;que&nbsp;», "
           + "et «&nbsp;que&nbsp;» remplace «&nbsp;la facture&nbsp;», qui est <i>devant</i>. "
           + "Vous êtes passé dessus avant d'arriver au verbe.",
        pourquoi: "« que » remplace la facture, déjà passée." },
      { txt: "Soraya a envoyé les deux lettres.", sous: "envoyé quoi&nbsp;?", ok: 'apres',
        rat: "«&nbsp;Les deux lettres&nbsp;», et elles arrivent après le verbe. L'ordre "
           + "ordinaire du français&nbsp;: qui, quoi, quand.",
        pourquoi: "Envoyé quoi ? — les deux lettres, après." },
      { txt: "Elle les a envoyées lundi.", sous: "envoyées quoi&nbsp;?", ok: 'avant',
        rat: "La réponse est «&nbsp;les&nbsp;», ce petit mot coincé devant le verbe. "
           + "Il remplace les deux lettres — et il est <i>avant</i>. C'est le déclencheur le "
           + "plus fréquent de tous.",
        pourquoi: "« les » remplace les lettres, et il est devant." },
      { txt: "Quelle photo avez-vous prise ?", sous: "prise quoi&nbsp;?", ok: 'avant',
        rat: "Une question renverse l'ordre&nbsp;: «&nbsp;quelle photo&nbsp;» est ce qu'on a "
           + "pris, et elle ouvre la phrase. La réponse est donc passée avant le verbe.",
        pourquoi: "« quelle photo » ouvre la phrase : c'est déjà passé." },
      { txt: "Il a pris trois photos du logement.", sous: "pris quoi&nbsp;?", ok: 'apres',
        rat: "«&nbsp;Trois photos&nbsp;», derrière le verbe. Comparez avec la phrase "
           + "précédente&nbsp;: même verbe, même objet, et la place change tout.",
        pourquoi: "Pris quoi ? — trois photos, après." },
      { txt: "Nous avons beaucoup hésité.", sous: "hésité quoi&nbsp;?", ok: 'rien',
        rat: "La question ne veut rien dire ici. On hésite, un point&nbsp;: il n'y a pas de "
           + "chose sur laquelle le verbe tombe. «&nbsp;Beaucoup&nbsp;» dit combien, pas quoi.",
        pourquoi: "On n'hésite pas quelque chose. Pas de réponse." },
      { txt: "Kaléb a travaillé jusqu'à minuit.", sous: "travaillé quoi&nbsp;?", ok: 'rien',
        rat: "«&nbsp;Jusqu'à minuit&nbsp;» répond à <i>jusqu'à quand</i>, pas à <i>quoi</i>. "
           + "Beaucoup de phrases n'ont aucune réponse à «&nbsp;quoi&nbsp;», et ce sont les "
           + "plus simples de toutes.",
        pourquoi: "Jusqu'à minuit dit quand, pas quoi." },
    ],
    attente: "Tranchez les huit phrases pour continuer.",
  },

  // ── 3. La règle, écrite comme un constat de ce qu'il vient de faire. ─────
  {
    id:   'le-test',
    type: 'notion',
    eye:  'Ce que vous venez de faire',
    menu: 'Le test',
    titre: "Relisez votre colonne du milieu. Les trois y ont pris une lettre.",
    paras: [
      "Reçu<b>e</b>, envoyé<b>es</b>, pris<b>e</b>. Les trois phrases où la réponse à "
      + "«&nbsp;quoi&nbsp;?&nbsp;» était <b>déjà passée</b>. Et dans les cinq autres — celles "
      + "où la réponse venait après, ou n'existait pas — pas une lettre n'a bougé&nbsp;: reçu, "
      + "envoyé, pris, hésité, travaillé. On vous a fait ranger huit phrases&nbsp;; vous venez "
      + "de séparer la règle entière.",

      "Elle s'écrit en une ligne. Avec <b>avoir</b>, le participe passé ne s'accorde que si la "
      + "réponse à «&nbsp;quoi&nbsp;?&nbsp;» est placée <b>avant</b> le verbe. Il s'accorde "
      + "alors avec elle, comme un adjectif&nbsp;: la facture reçu<b>e</b>, les lettres "
      + "envoyé<b>es</b>.",

      "Le petit mot devant le participe — <i>ai</i>, <i>a</i>, <i>avons</i> — s'appelle "
      + "l'<b>auxiliaire</b>, et la réponse à «&nbsp;quoi&nbsp;?&nbsp;» s'appelle le "
      + "<b>complément direct</b>. Vous n'avez pas besoin des noms pour vous en servir, mais "
      + "votre enseignant les emploiera. <i>Ce point ne parle que de «&nbsp;avoir&nbsp;»&nbsp;: "
      + "avec «&nbsp;être&nbsp;», c'est une autre mécanique.</i>",

      "<b>Le test, à vous poser sur n'importe quelle phrase&nbsp;:</b> je pose "
      + "«&nbsp;quoi&nbsp;?&nbsp;» juste après le verbe. Est-ce que la réponse arrive derrière, "
      + "ou est-ce que je suis déjà passé dessus&nbsp;? Déjà passé → j'accorde. Tout le reste → "
      + "je n'écris rien de plus.",
    ],
    retenir: "<b>La réponse est-elle déjà passée&nbsp;?</b> Si oui, le participe s'accorde avec "
           + "elle. Sinon, il ne bouge pas — et c'est le cas le plus fréquent, de loin.",
    attente: "Lisez, puis continuez.",
  },

  // ── 4. Trier des phrases, maintenant qu'il a le test. ────────────────────
  {
    id:   'tri-correct',
    type: 'tri',
    eye:  'À vous de trancher',
    menu: 'Six phrases',
    titre: "Six phrases écrites. Passez le test sur chacune.",
    consigne: "Posez «&nbsp;quoi&nbsp;?&nbsp;» après le verbe, regardez où est la réponse, "
            + "puis regardez la fin du participe.",
    colonnes: [
      { id: 'ok',   t: 'Correct',   b: 'Correct' },
      { id: 'faux', t: 'Une faute', b: 'Une faute' },
    ],
    items: [
      { txt: "J'ai relu la lettre trois fois.", ok: 'ok',
        rat: "Relu quoi&nbsp;? La lettre — et elle arrive <i>après</i>. Rien à ajouter au "
           + "participe, même si «&nbsp;lettre&nbsp;» est un mot féminin. C'est la place qui "
           + "décide, jamais le mot tout seul.",
        pourquoi: "La réponse vient après. Le participe ne bouge pas." },
      { txt: "La lettre que j'ai relu trois fois.", ok: 'faux',
        rat: "Même verbe, même lettre, mais «&nbsp;que&nbsp;» est passé avant le verbe. "
           + "Il faut «&nbsp;que j'ai <b>relue</b>&nbsp;». C'est exactement la paire de "
           + "l'écran 1.",
        pourquoi: "Il faut « que j'ai relue »." },
      { txt: "Vos photos ? Je les ai reçues ce matin.", ok: 'ok',
        rat: "«&nbsp;Les&nbsp;» remplace «&nbsp;vos photos&nbsp;» et se tient devant le "
           + "verbe&nbsp;: la réponse est déjà passée, donc reçu<b>es</b>, féminin pluriel. "
           + "Les deux moitiés sont justes.",
        pourquoi: "« les » est devant, et l'accord suit." },
      { txt: "Quelle date avez-vous inscrit sur le formulaire ?", ok: 'faux',
        rat: "Inscrit quoi&nbsp;? «&nbsp;Quelle date&nbsp;» — et elle ouvre la phrase, donc "
           + "elle est passée avant le verbe. Il faut «&nbsp;inscrit<b>e</b>&nbsp;». "
           + "Une question renverse l'ordre&nbsp;; le test, lui, ne change pas.",
        pourquoi: "Il faut « avez-vous inscrite »." },
      { txt: "Elle a rempli les trois formulaires.", ok: 'ok',
        rat: "Rempli quoi&nbsp;? Les trois formulaires, <i>après</i> le verbe. Le participe "
           + "reste tel quel — et il resterait tel quel même s'il y en avait trente.",
        pourquoi: "La réponse vient après. Rien à ajouter." },
      { txt: "Les trois formulaires qu'elle a rempli.", ok: 'faux',
        rat: "«&nbsp;Qu'&nbsp;» remplace les trois formulaires, placés devant&nbsp;: "
           + "«&nbsp;qu'elle a <b>remplis</b>&nbsp;», masculin pluriel. C'est la troisième "
           + "fois que le même verbe change de forme selon la place — c'est tout ce qu'il y a "
           + "à retenir.",
        pourquoi: "Il faut « qu'elle a remplis »." },
    ],
    attente: "Tranchez les six phrases pour continuer.",
  },

  // ── 5. Trois déclencheurs. Pas la liste, et on le dit. ───────────────────
  {
    id:   'trois-declencheurs',
    type: 'notion',
    eye: "Ce qui met la réponse devant",
    menu: 'Trois déclencheurs',
    titre: "Une chose ne passe devant le verbe que de trois façons.",
    paras: [
      "<b>Un pronom</b> — <i>le, la, les, l'</i>. «&nbsp;Je <b>les</b> ai vus au comptoir.&nbsp;» "
      + "C'est le plus fréquent des trois, et le plus discret&nbsp;: deux ou trois lettres, "
      + "coincées entre le sujet et l'auxiliaire. Pour savoir quoi accorder, il faut savoir ce "
      + "que le pronom remplace — et ça, c'est dans la phrase d'avant.",

      "<b>Le relatif « que »</b> — «&nbsp;les documents <b>que</b> j'ai signés&nbsp;». Il "
      + "reprend le mot juste devant lui. C'est le déclencheur le plus visible, parce qu'on "
      + "voit le mot repris à un centimètre de distance.",

      "<b>La question « quel, quelle, quels, quelles »</b> — «&nbsp;<b>Quelles</b> pièces "
      + "avez-vous jointes&nbsp;?&nbsp;» Une question renverse l'ordre de la phrase et fait "
      + "passer devant ce qui serait venu derrière. On l'oublie presque toujours, parce qu'on "
      + "ne pense pas à accorder en posant une question.",

      "<b>Il en existe d'autres</b>, plus rares, et ce point express ne les traite pas. "
      + "Ces trois-là couvrent presque tout ce que vous écrirez cette année&nbsp;: un courriel, "
      + "une demande, un rapport. Cherchez-les des yeux avant d'envoyer.",
    ],
    retenir: "Un pronom, un «&nbsp;que&nbsp;», un «&nbsp;quelle&nbsp;». "
           + "<b>Quand vous en voyez un, vous avez une décision à prendre.</b>",
    attente: "Lisez, puis continuez.",
  },

  // ── 6. Le pronom : il faut savoir ce qu'il remplace. ─────────────────────
  {
    id:   'le-pronom',
    type: 'verif',
    eye:  'Vérification',
    menu: 'Le pronom',
    titre: "Soraya écrit à son propriétaire.",
    consigne: "«&nbsp;<i>Bonjour. J'ai fait trois demandes de réparation depuis le mois de "
            + "mars.</i>&nbsp;» Quelle est la phrase suivante&nbsp;?",
    options: [
      { txt: "« Je vous les ai envoyées par courriel chaque fois. »", juste: true },
      { txt: "« Je vous les ai envoyé par courriel chaque fois. »",
        rat_t: "Vous avez vu le pronom, et vous n'avez pas cherché ce qu'il remplace.",
        rat: "«&nbsp;Les&nbsp;» reprend «&nbsp;trois demandes&nbsp;», qui est dans la phrase "
           + "<b>d'avant</b>. C'est ce qui rend ce déclencheur difficile&nbsp;: le mot à "
           + "accorder n'est pas dans la phrase que vous êtes en train d'écrire. "
           + "Trois demandes, féminin pluriel&nbsp;: envoyé<b>es</b>." },
      { txt: "« J'ai envoyées trois demandes par courriel chaque fois. »",
        rat_t: "Vous avez accordé, mais la réponse est derrière le verbe.",
        rat: "Ici, «&nbsp;trois demandes&nbsp;» arrive <i>après</i>&nbsp;: le test dit de ne "
           + "rien ajouter. On écrit «&nbsp;j'ai envoyé trois demandes&nbsp;». Accorder par "
           + "prudence est aussi faux que ne pas accorder — la règle n'est pas «&nbsp;dans le "
           + "doute, mettre un e&nbsp;»." },
    ],
    pourquoi: "«&nbsp;Je vous les ai <b>envoyées</b>&nbsp;». Le pronom vous oblige à remonter "
            + "d'une phrase pour savoir ce que vous accordez. <b>Quand vous vous relisez, "
            + "arrêtez-vous sur chaque <i>le, la, les</i> placé devant un auxiliaire.</b>",
    attente: "Choisissez une réponse pour continuer.",
  },

  // ── 7. Ce qu'aucune mini-leçon n'écrit : quand ça s'entend. ──────────────
  {
    id:   'on-ne-lentend-pas',
    type: 'notion',
    eye:  'Pourquoi la faute dure',
    menu: "Ce qu'on n'entend pas",
    titre: "« Je les ai envoyé » et « je les ai envoyées » se prononcent exactement pareil.",
    paras: [
      "C'est pour ça que cette règle traverse des années sans être corrigée. Vous vous relisez "
      + "à voix haute, tout sonne juste, et la faute est encore là. Elle n'existe qu'au moment "
      + "où quelqu'un vous lit — un employeur, un fonctionnaire, un comité.",

      "Mais ce n'est pas vrai de tous les verbes, et il faut le savoir. Les participes qui "
      + "finissent par une consonne, eux, <b>s'entendent</b>&nbsp;: écri<b>t</b> et "
      + "écri<b>te</b>, pri<b>s</b> et pri<b>se</b>, fai<b>t</b> et fai<b>te</b>, mi<b>s</b> et "
      + "mi<b>se</b>, offer<b>t</b> et offer<b>te</b>. Là, l'oreille sert — et là, tout le "
      + "monde entend la faute, y compris ceux qui ne sauraient pas l'expliquer.",

      "Retenez donc les deux moitiés&nbsp;: sur la grande majorité des verbes, se relire à voix "
      + "haute <b>ne trouve rien</b> et il faut chercher des yeux&nbsp;; sur cette petite "
      + "poignée-là, la faute s'entend à trois mètres. Ce sont les verbes les plus courants du "
      + "français écrit — écrire, prendre, faire, mettre. C'est là qu'elle coûte le plus cher.",
    ],
    retenir: "Se relire à voix haute ne suffit pas. <b>Cherchez les pronoms et les "
           + "«&nbsp;que&nbsp;» des yeux</b>, ligne par ligne, avant d'envoyer.",
    attente: "Lisez, puis continuez.",
  },

  // ── 8. Le piège : quelque chose devant qui n'est pas la réponse à « quoi ». ─
  {
    id:   'a-qui-pas-quoi',
    type: 'verif',
    eye:  'Le cas qui trompe',
    menu: 'À qui, pas quoi',
    titre: "Un mot placé devant ne déclenche rien s'il ne répond pas à « quoi ? ».",
    consigne: "Kaléb parle de deux propriétaires à qui il a fait une demande. "
            + "Quelle phrase est correcte&nbsp;?",
    options: [
      { txt: "« Les deux propriétaires à qui j'ai écrit n'ont pas répondu. »", juste: true },
      { txt: "« Les deux propriétaires à qui j'ai écrits n'ont pas répondu. »",
        rat_t: "Il y a bien quelque chose devant. Ce n'est pas la réponse à «&nbsp;quoi&nbsp;?&nbsp;».",
        rat: "«&nbsp;Écrit quoi&nbsp;?&nbsp;» — un courriel, une lettre&nbsp;; ce n'est pas dit. "
           + "Les propriétaires répondent à «&nbsp;<b>à qui</b>&nbsp;», ce qui est une autre "
           + "question. Le test est précis exprès&nbsp;: il demande <i>quoi</i>, jamais "
           + "<i>à qui</i>." },
      { txt: "« Je leur ai écrits la semaine passée. »",
        rat_t: "«&nbsp;Leur&nbsp;» est devant le verbe, et il ne déclenche rien non plus.",
        rat: "C'est le même piège en plus court. «&nbsp;Leur&nbsp;» veut dire "
           + "«&nbsp;<b>à eux</b>&nbsp;»&nbsp;: encore une réponse à «&nbsp;à qui&nbsp;?&nbsp;». "
           + "Deux pronoms se ressemblent et ne font pas la même chose&nbsp;: "
           + "<i>les</i> déclenche l'accord, <i>leur</i> ne le déclenche jamais." },
    ],
    pourquoi: "Ce n'est pas «&nbsp;y a-t-il un mot avant le verbe&nbsp;?&nbsp;», c'est "
            + "«&nbsp;<b>la réponse à quoi&nbsp;? est-elle avant le verbe&nbsp;?</b>&nbsp;» "
            + "Un mot qui répond à <i>à qui</i>, <i>à quoi</i>, <i>de quoi</i> peut être placé "
            + "où il veut&nbsp;: il ne change rien au participe.",
    attente: "Choisissez une réponse pour continuer.",
  },

  // ── 9. Trois décisions dans une seule phrase. ────────────────────────────
  {
    id:   'trois-decisions',
    type: 'verif',
    eye:  'Vérification',
    menu: 'Trois décisions',
    titre: "Nadège rend compte d'un dossier. Une seule version tient d'un bout à l'autre.",
    consigne: "Trois décisions dans la même phrase. Passez le test sur chacune, dans l'ordre.",
    options: [
      { txt: "J'ai envoyé la demande lundi, la commis l'a reçue mardi, "
           + "et les pièces que j'avais jointes étaient complètes.",
        juste: true },
      { txt: "J'ai envoyée la demande lundi, la commis l'a reçu mardi, "
           + "et les pièces que j'avais jointes étaient complètes.",
        rat_t: "Les deux premières sont inversées.",
        rat: "«&nbsp;Envoyé quoi&nbsp;? la demande&nbsp;» — elle arrive <i>après</i>, donc rien "
           + "à ajouter. «&nbsp;Reçu quoi&nbsp;? l'&nbsp;» — ce pronom remplace la demande et "
           + "il est <i>devant</i>, donc «&nbsp;reçu<b>e</b>&nbsp;». Vous avez accordé là où il "
           + "ne fallait pas, et pas là où il fallait. La troisième était bonne." },
      { txt: "J'ai envoyé la demande lundi, la commis l'a reçue mardi, "
           + "et les pièces que j'avais joint étaient complètes.",
        rat_t: "Les deux premières sont justes. La troisième est tombée.",
        rat: "Vous avez tenu les deux premières décisions et lâché la dernière — c'est ce qui "
           + "arrive presque toujours, parce qu'elle est loin du début de la phrase. "
           + "«&nbsp;Que&nbsp;» reprend «&nbsp;les pièces&nbsp;», placées devant&nbsp;: "
           + "«&nbsp;que j'avais <b>jointes</b>&nbsp;»." },
    ],
    pourquoi: "Une réponse après le verbe, un pronom devant, un «&nbsp;que&nbsp;» devant. "
            + "<b>Trois décisions, prises l'une après l'autre, avec le même test à chaque "
            + "fois.</b> Une phrase longue n'est pas une règle de plus&nbsp;: c'est la même, "
            + "appliquée trois fois.",
    attente: "Choisissez une réponse pour continuer.",
  },

  // ── 10. La fermeture : la lettre de l'écran 1. ───────────────────────────
  {
    id:   'fermeture',
    type: 'verif',
    eye:  'La dernière',
    menu: 'Pour finir',
    titre: "On revient à la lettre du début. Cette fois, il y en a deux.",
    consigne: "Soraya écrit&nbsp;: «&nbsp;<i>J'ai écrit deux lettres au propriétaire. "
            + "Les deux lettres que j'ai ___ sont restées sans réponse.</i>&nbsp;» "
            + "Qu'est-ce qu'elle met dans le trou&nbsp;?",
    options: [
      { txt: "écrites", juste: true },
      { txt: "écrit",
        rat_t: "C'est la faute de l'écran 1, au pluriel.",
        rat: "«&nbsp;Que&nbsp;» reprend «&nbsp;les deux lettres&nbsp;», placées juste devant. "
           + "La réponse à «&nbsp;quoi&nbsp;?&nbsp;» est déjà passée, donc le participe "
           + "s'accorde&nbsp;: féminin pluriel, «&nbsp;écrit<b>es</b>&nbsp;». Remarquez que la "
           + "première phrase, elle, s'écrit bien «&nbsp;j'ai <b>écrit</b> deux lettres&nbsp;» "
           + "— même verbe, même objet, autre place." },
      { txt: "écrit ou écrites, les deux se défendent",
        rat_t: "Une seule tient, et c'est un savoir attendu à votre niveau.",
        rat: "Il n'y a pas de doute à avoir&nbsp;: le test répond, à chaque fois, sans "
           + "hésitation. Et celui-ci s'<b>entend</b> — «&nbsp;écrites&nbsp;» finit par un "
           + "<i>t</i> qu'on prononce. C'est l'un des rares où l'oreille suffit, et c'est "
           + "précisément celui-là qu'on vous entend rater." },
    ],
    pourquoi: "«&nbsp;Les deux lettres que j'ai <b>écrites</b>&nbsp;». Vous avez fait les deux "
            + "phrases de l'écran 1 dans le bon sens&nbsp;: pas d'accord quand la réponse suit, "
            + "accord quand elle est déjà passée. <b>C'est toute la règle, et vous n'en aurez "
            + "jamais besoin d'une autre.</b>",
    attente: "Choisissez une réponse pour finir.",
  },

];
