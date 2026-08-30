// ═══════════════════════════════════════════════════════════════════════════
// Point express — « Je dois » et « je peux »
//
// Savoir n2-s27 (auxiliaires de modalité). Dix minutes, dix écrans.
// Une ORDONNANCE : l'enseignant l'envoie à un élève qui dit « je peux partir »
// pour annoncer qu'il part, ou « je dois » pour demander une permission.
//
// ── Ce qui le sépare des mini-leçons ───────────────────────────────────────
// Cinq existent déjà, et l'élève en a lu au moins une :
//   · `module-n2-classe`, « Demander la permission » — la formule
//     « Est-ce que je peux + infinitif », les trois réponses, les trois pièges.
//     Tout est là, du côté de la FORME.
//   · `module-n2-secretaire`, « Les consignes et les règlements du centre » —
//     un bloc de quatre lignes sur « je peux / je dois ».
//   · `module-n3-horaire` et `module-n3-pharmacie`, « Pouvoir, devoir,
//     falloir » — les trois verbes en tableau, avec un labo à deux axes.
//   · `module-n4-etablissement`, « Devoir, il faut, il faudrait ».
// Toutes donnent les formes. Aucune ne donne le moyen de CHOISIR, et aucune
// ne travaille l'écoute — or c'est là que l'élève perd pied.
//
// Les cinq écarts tenus :
//   1. INDUCTIF. L'élève range six phrases avant qu'aucun des trois verbes ne
//      soit nommé. La règle de l'écran 4 est écrite comme un constat.
//   2. UN TEST, PAS UN TABLEAU. « Mettez à la place : c'est obligatoire, ou
//      c'est permis ? » Il marche sur une phrase jamais vue, et il marche même
//      quand la phrase ne contient aucun des trois verbes.
//   3. LA RÉPONSE TRAHIT LE VERBE (écran 5). « Non, c'est interdit » répond à
//      « je peux » ; « Non, ce n'est pas nécessaire » répond à « je dois ».
//      C'est la moitié qui manque partout et c'est celle qui s'entend.
//   4. L'OBLIGATION SE DÉGUISE. Dans la vraie vie, « il faut » ne se dit
//      presque jamais : on met un ordre sur une affiche (« Soyez à l'heure »)
//      ou on emploie le présent (« Vous prévenez la secrétaire »). Deux des
//      six cas du tri sont de ceux-là ; aucune mini-leçon ne les traite.
//   5. LE MÉTALANGAGE ARRIVE APRÈS. « Devoir », « pouvoir » et « il faut » ne
//      sont nommés qu'à l'écran 4, une fois la chose manipulée. Et jamais un
//      seul tableau de conjugaison : ce n'est pas ce qui manque à l'élève.
//
// Extraits : `module-n2-secretaire`, rejoués par chemin. Aucun média neuf.
// Le texte est montré partout où l'élève lit, caché nulle part : au niveau 2,
// lire et entendre en même temps est un appui, pas une triche — le point ne
// porte pas sur la discrimination auditive.
// ═══════════════════════════════════════════════════════════════════════════

const PARCOURS = {
  slug:     'devoir-et-pouvoir',
  module:   'module-n2-secretaire',
  titre:    "« Je dois » et « je peux »",
  surtitre: "Point express · 10 minutes",
  niveau:   2,
  savoir:   'n2-s27',
};

const ECRANS = [

  // ── 1. On tranche AVANT de savoir. ───────────────────────────────────────
  {
    id:   'depart',
    type: 'verif',
    eye:  'Une question, pour commencer',
    menu: 'Deux phrases',
    titre: "Vous travaillez au comptoir. Un élève arrive. Il dit une de ces deux phrases.",
    consigne: "«&nbsp;Je dois partir à midi.&nbsp;» · «&nbsp;Est-ce que je peux partir à midi&nbsp;?&nbsp;» "
            + "Laquelle attend une réponse de vous&nbsp;? "
            + "Répondez avec ce que vous savez déjà — c'est fait exprès.",
    options: [
      { txt: "La deuxième. Il me demande quelque chose.", juste: true },
      { txt: "La première. Il me demande quelque chose.",
        rat_t: "Avec la première, il vous informe.",
        rat: "«&nbsp;Je dois partir&nbsp;» veut dire&nbsp;: c'est déjà décidé, je n'ai pas le "
           + "choix. Il vous prévient, il ne vous demande rien. Vous pouvez répondre "
           + "«&nbsp;d'accord&nbsp;»&nbsp;— vous ne décidez pas." },
      { txt: "Les deux. C'est la même chose dite autrement.",
        rat_t: "Ce n'est pas la même chose du tout.",
        rat: "Dans l'une, il part et il vous le dit. Dans l'autre, il part <b>si vous dites "
           + "oui</b>. Un seul petit mot change, et c'est vous qui décidez, ou pas." },
    ],
    pourquoi: "Un mot change, et la personne qui décide change avec lui. "
            + "<b>C'est tout ce point express.</b>",
    attente: "Choisissez une réponse pour continuer.",
  },

  // ── 2. On écoute. Toujours aucune règle. ─────────────────────────────────
  {
    id:   'ecoute',
    type: 'notion',
    eye:  'Écoutez au comptoir',
    menu: 'Sami demande',
    titre: "C'est le premier jour de Sami. Il demande quelque chose. On lui répond.",
    paras: [
      "Écoutez la question, puis la réponse. Sami veut savoir <b>s'il est obligé</b> "
      + "d'écrire un papier quand il est absent.",

      "Regardez la réponse d'Amel&nbsp;: elle ne dit pas seulement «&nbsp;non&nbsp;». "
      + "Elle dit ce qu'il faut faire à la place. Gardez cette réponse en tête&nbsp;: "
      + "on y revient à l'écran 5.",
    ],
    sons: [
      { fichier: 'appli/line_07_sami.mp3', qui: 'Sami',
        texte: "Je dois écrire un papier ?", montrer: true },
      { fichier: 'appli/line_08_amel.mp3', qui: 'Amel répond',
        texte: "Non. Vous dites votre nom et votre groupe. C'est tout.", montrer: true },
    ],
    retenir: "Écoutez les deux extraits deux fois. On ne vous a encore donné aucune règle.",
    attente: "Écoutez, puis continuez.",
  },

  // ── 3. Le cœur : six phrases, deux déguisées. ────────────────────────────
  {
    id:   'tri-six',
    type: 'tri',
    eye:  'À vous de trancher',
    menu: 'Six phrases',
    titre: "Six phrases du centre. Rangez-les.",
    consigne: "Une question, une seule&nbsp;: est-ce que j'ai le choix&nbsp;? "
            + "Ne regardez pas les verbes — regardez ce que la phrase vous fait.",
    colonnes: [
      { id: 'obl', t: "C'est obligatoire", b: "C'est obligatoire" },
      { id: 'per', t: "C'est permis",      b: "C'est permis" },
    ],
    items: [
      { txt: "Je dois prévenir avant mon absence.", ok: 'obl',
        rat: "«&nbsp;Je dois&nbsp;» ne demande rien et n'offre rien&nbsp;: c'est déjà décidé. "
           + "Personne ne va vous répondre «&nbsp;oui&nbsp;» ou «&nbsp;non&nbsp;».",
        pourquoi: "Je n'ai pas le choix." },
      { txt: "Est-ce que je peux payer en deux fois ?", ok: 'per',
        sous: "au comptoir de l'école",
        rat: "Vous demandez le droit de faire quelque chose. La personne peut dire oui, "
           + "elle peut dire non. C'est elle qui décide, pas vous.",
        pourquoi: "Je demande le droit. L'autre décide." },
      { txt: "Soyez à l'heure.", ok: 'obl',
        sous: "écrit sur la porte du local",
        rat: "Il n'y a ni «&nbsp;je dois&nbsp;», ni «&nbsp;il faut&nbsp;» — et c'est quand "
           + "même une obligation. Sur une affiche, on écrit le verbe seul&nbsp;: "
           + "<b>Soyez à l'heure. Fermez la porte. Écrivez votre nom.</b> "
           + "C'est un ordre pour tout le monde.",
        pourquoi: "Un ordre sur une affiche. Obligatoire." },
      { txt: "Vous pouvez venir au comptoir le matin.", ok: 'per',
        rat: "On ne vous oblige pas à venir le matin&nbsp;: on vous dit que c'est possible. "
           + "«&nbsp;Vous pouvez&nbsp;» ouvre une porte, il ne pousse personne.",
        pourquoi: "C'est possible. Ce n'est pas obligé." },
      { txt: "Vous allez au comptoir et vous prévenez la secrétaire.", ok: 'obl',
        sous: "ce qu'Amel explique à Sami",
        rat: "Le verbe est au présent, comme si on racontait. Mais Amel ne raconte pas&nbsp;: "
           + "elle explique ce qu'il <b>faut</b> faire. C'est la façon la plus courante "
           + "d'expliquer une obligation, et c'est celle qui trompe le plus.",
        pourquoi: "Le présent, mais c'est la marche à suivre. Obligatoire." },
      { txt: "L'eau est permise en classe.", ok: 'per',
        rat: "Le mot est écrit&nbsp;: <b>permis</b>. On vous donne un droit, on ne vous "
           + "demande rien. Son contraire est <b>interdit</b>.",
        pourquoi: "Permis : j'ai le droit." },
    ],
    attente: "Rangez les six phrases pour continuer.",
  },

  // ── 4. La règle, écrite comme un constat. Le métalangage arrive ici. ─────
  {
    id:   'le-test',
    type: 'notion',
    eye:  'Ce que vous venez de faire',
    menu: 'Le test',
    titre: "Vous n'avez pas regardé les verbes. Vous avez cherché : est-ce que j'ai le choix ?",
    paras: [
      "Gardez cette question. C'est votre test, et il marche sur une phrase que vous n'avez "
      + "jamais entendue&nbsp;: <b>mettez «&nbsp;c'est obligatoire&nbsp;» ou «&nbsp;c'est "
      + "permis&nbsp;» à la place. Celui des deux qui va, c'est le bon.</b>",

      "Maintenant les noms. <b>Je dois</b> = c'est obligatoire, pour moi. "
      + "<b>Je peux</b> = c'est permis, ou c'est possible. "
      + "<b>Il faut</b> = c'est obligatoire, pour tout le monde.",

      "Vous voyez qu'il n'y a que <b>deux idées</b>, pas trois&nbsp;: obligatoire, ou permis. "
      + "«&nbsp;Je dois&nbsp;» et «&nbsp;il faut&nbsp;» disent la même chose&nbsp;; ils ne "
      + "disent pas <i>à qui</i>.",
    ],
    retenir: "<b>Obligatoire ou permis&nbsp;?</b> Répondez à ça d'abord. "
           + "Le verbe vient après, tout seul.",
    attente: "Lisez, puis continuez.",
  },

  // ── 5. La réponse trahit le verbe. C'est la moitié qui manque partout. ───
  {
    id:   'la-reponse',
    type: 'verif',
    eye:  'Vérification',
    menu: 'Écoutez la réponse',
    titre: "On vous répond « Non, ce n'est pas nécessaire. » Vous aviez demandé quoi ?",
    consigne: "Écoutez l'échange, puis choisissez.",
    sons: [
      { fichier: 't2/line_07_amel.mp3', qui: 'Amel demande',
        texte: "Est-ce que je dois écrire un papier ?", montrer: true },
      { fichier: 't2/line_08_line.mp3', qui: 'La secrétaire répond',
        texte: "Non, ce n'est pas nécessaire. Je préviens l'enseignante.", montrer: true },
    ],
    options: [
      { txt: "« Est-ce que je dois… ? » — je demandais si c'est obligatoire.", juste: true },
      { txt: "« Est-ce que je peux… ? » — je demandais la permission.",
        rat_t: "On ne vous aurait pas répondu ça.",
        rat: "À «&nbsp;est-ce que je peux&nbsp;», un non se dit «&nbsp;non, c'est "
           + "<b>interdit</b>&nbsp;» ou «&nbsp;non, ce n'est pas <b>possible</b>&nbsp;». "
           + "«&nbsp;Ce n'est pas nécessaire&nbsp;» répond à une tout autre question." },
      { txt: "Les deux réponses vont.",
        rat_t: "Les deux «&nbsp;non&nbsp;» ne veulent pas dire la même chose.",
        rat: "«&nbsp;Non, c'est interdit&nbsp;» vous ferme une porte. «&nbsp;Non, ce n'est "
           + "pas nécessaire&nbsp;» vous enlève du travail — c'est une bonne nouvelle. "
           + "Les confondre, c'est repartir en croyant qu'on vous a refusé quelque chose." },
    ],
    pourquoi: "<b>La réponse vous dit quel verbe on a entendu.</b> "
            + "«&nbsp;Pas nécessaire&nbsp;» → on avait entendu <i>je dois</i>. "
            + "«&nbsp;Interdit&nbsp;» → on avait entendu <i>je peux</i>. "
            + "Quand vous doutez, écoutez la réponse&nbsp;: elle corrige votre question.",
    attente: "Choisissez une réponse pour continuer.",
  },

  // ── 6. « Il faut », et ses deux déguisements. ────────────────────────────
  {
    id:   'il-faut',
    type: 'notion',
    eye:  'Le mot qui ne nomme personne',
    menu: '« Il faut »',
    titre: "« Il faut » ne dit jamais qui. C'est pour ça qu'on l'emploie.",
    paras: [
      "«&nbsp;<b>Il faut</b> prévenir avant huit heures.&nbsp;» Qui&nbsp;? Tout le monde. "
      + "C'est la règle de la place, pas une phrase sur vous. Ce «&nbsp;il&nbsp;» n'est "
      + "personne&nbsp;: on ne dit jamais «&nbsp;je faut&nbsp;». Pour parler de soi, "
      + "on dit «&nbsp;je dois&nbsp;».",

      "Le piège est ailleurs&nbsp;: <b>presque personne ne dit «&nbsp;il faut&nbsp;».</b> "
      + "On donne l'ordre tout seul, ou on met le verbe au présent. Écoutez les deux "
      + "extraits&nbsp;: il n'y a ni «&nbsp;il faut&nbsp;», ni «&nbsp;vous devez&nbsp;», "
      + "et pourtant ce sont deux obligations.",
    ],
    sons: [
      { fichier: 't2b/line_08_marc.mp3', qui: "Monsieur Ouellet — l'ordre tout seul",
        texte: "Mardi, tout est ouvert. Soyez à l'heure !", montrer: true },
      { fichier: 'appli/line_06_amel.mp3', qui: 'Amel — le présent',
        texte: "Vous allez au comptoir et vous prévenez la secrétaire.", montrer: true },
    ],
    retenir: "Une affiche, un ordre, un présent qui explique la marche à suivre&nbsp;: "
           + "<b>c'est «&nbsp;il faut&nbsp;» sans le dire.</b> Faites votre test.",
    attente: "Écoutez, puis continuez.",
  },

  // ── 7. « Je peux » a deux sens, et l'autre trompe. ───────────────────────
  {
    id:   'deux-sens',
    type: 'verif',
    eye:  'Le cas qui trompe',
    menu: 'Deux sens',
    titre: "La secrétaire dit « je peux ». Est-ce qu'elle vous demande la permission ?",
    consigne: "Écoutez, puis choisissez.",
    sons: [
      { fichier: 't1/line_02_line.mp3', qui: 'La secrétaire, au comptoir',
        texte: "Bonjour ! Qu'est-ce que je peux faire pour vous ?", montrer: true },
    ],
    options: [
      { txt: "Non. Elle offre son aide. C'est à moi de parler.", juste: true },
      { txt: "Oui. Elle demande la permission de m'aider.",
        rat_t: "Personne ne demande la permission d'aider.",
        rat: "«&nbsp;Je peux&nbsp;» ne demande pas toujours&nbsp;: ici, il veut dire "
           + "«&nbsp;je suis capable, je suis là pour ça&nbsp;». C'est la phrase d'accueil "
           + "de tous les comptoirs du Québec." },
      { txt: "Elle dit qu'elle est obligée de m'aider.",
        rat_t: "«&nbsp;Je peux&nbsp;» n'oblige jamais.",
        rat: "Faites le test&nbsp;: mettez «&nbsp;c'est obligatoire&nbsp;» à la place. "
           + "«&nbsp;Il est obligatoire que je fasse quelque chose pour vous&nbsp;»&nbsp;: "
           + "ça ne va pas. C'est donc l'autre idée." },
    ],
    pourquoi: "<b>«&nbsp;Je peux&nbsp;» a deux sens</b>&nbsp;: je demande le droit, "
            + "ou je suis capable. C'est le début de la phrase qui tranche&nbsp;: "
            + "«&nbsp;Est-ce que je peux…&nbsp;?&nbsp;» demande&nbsp;; "
            + "«&nbsp;Qu'est-ce que je peux…&nbsp;?&nbsp;» offre.",
    attente: "Choisissez une réponse pour continuer.",
  },

  // ── 8. Le refus qui ne dit pas « non ». ──────────────────────────────────
  {
    id:   'le-refus',
    type: 'verif',
    eye:  'Vérification',
    menu: 'Un non déguisé',
    titre: "Vous demandez : « Est-ce que je peux venir à midi ? » On vous répond ceci.",
    consigne: "Écoutez. Est-ce oui ou non&nbsp;?",
    sons: [
      { fichier: 't1b/line_04_line.mp3', qui: 'La secrétaire',
        texte: "À seize heures. Mais le midi, c'est fermé.", montrer: true },
    ],
    options: [
      { txt: "C'est non. Je viens avant midi, ou après treize heures.", juste: true },
      { txt: "C'est oui, jusqu'à seize heures.",
        rat_t: "Seize heures, c'est l'heure de la fermeture du soir.",
        rat: "Elle donne deux informations&nbsp;: le comptoir ferme à seize heures, <b>et</b> "
           + "il est fermé le midi. Votre midi tombe dans le trou. Vous trouveriez porte close." },
      { txt: "Elle ne m'a pas répondu.",
        rat_t: "Elle a répondu — par la règle.",
        rat: "C'est très fréquent ici&nbsp;: au lieu de dire «&nbsp;non&nbsp;», on vous donne "
           + "la règle. «&nbsp;C'est fermé&nbsp;», «&nbsp;c'est interdit&nbsp;», "
           + "«&nbsp;c'est complet&nbsp;»&nbsp;: ce sont des non." },
    ],
    pourquoi: "Quand vous demandez «&nbsp;est-ce que je peux&nbsp;», la réponse n'est presque "
            + "jamais un «&nbsp;non&nbsp;» tout seul. <b>C'est une règle, et la règle est le "
            + "non.</b> Redemandez alors&nbsp;: «&nbsp;Et à quelle heure, alors&nbsp;?&nbsp;»",
    attente: "Choisissez une réponse pour continuer.",
  },

  // ── 9. Écrire, pas reconnaître. ──────────────────────────────────────────
  {
    id:   'votre-message',
    type: 'verif',
    eye:  'À vous d\'écrire',
    menu: 'Votre message',
    titre: "Vous écrivez à votre employeur. Jeudi, vous avez un rendez-vous à la clinique.",
    consigne: "Vous voulez partir à midi. Quel message envoyez-vous&nbsp;?",
    options: [
      { txt: "« Jeudi, je dois aller à la clinique. Est-ce que je peux partir à midi ? »",
        juste: true },
      { txt: "« Jeudi, est-ce que je dois partir à midi ? »",
        rat_t: "Vous lui demandez s'il vous oblige.",
        rat: "Votre patron ne sait rien de votre rendez-vous&nbsp;: il ne peut pas vous dire "
           + "si c'est obligatoire pour vous. C'est vous qui savez, et c'est vous qui devez "
           + "l'expliquer avant de demander." },
      { txt: "« Jeudi, il faut partir à midi. »",
        rat_t: "«&nbsp;Il faut&nbsp;» ne dit pas qui.",
        rat: "Votre patron lira&nbsp;: est-ce que tout l'atelier ferme à midi&nbsp;? "
           + "Pour parler de soi, on dit <b>je dois</b>. Et comme vous ne demandez rien, "
           + "il ne saura pas qu'il doit répondre." },
    ],
    pourquoi: "Les deux verbes vont ensemble, et toujours dans cet ordre&nbsp;: "
            + "<b>«&nbsp;je dois&nbsp;» explique, «&nbsp;est-ce que je peux&nbsp;» "
            + "demande.</b> Sans le premier, on refuse&nbsp;; sans le second, on ne répond pas.",
    attente: "Choisissez une réponse pour continuer.",
  },

  // ── 10. La fermeture : le même cas qu'à l'écran 1. ───────────────────────
  {
    id:   'fermeture',
    type: 'verif',
    eye:  'La dernière',
    menu: 'Pour finir',
    titre: "Cette fois, c'est vous à la place d'Amel. Demain, vous ne venez pas.",
    consigne: "Écoutez ce qu'elle dit, puis choisissez votre phrase au comptoir.",
    sons: [
      { fichier: 't2/line_03_amel.mp3', qui: 'Amel, au comptoir',
        texte: "Non. J'ai un rendez-vous à la clinique.", montrer: true },
    ],
    options: [
      { txt: "« Bonjour. Demain, je ne viens pas : je dois aller à la clinique. "
           + "Est-ce que je dois écrire un papier ? »", juste: true },
      { txt: "« Bonjour. Est-ce que je peux ne pas venir demain ? »",
        rat_t: "Vous demandez une permission que personne ne donne.",
        rat: "Le centre ne vous donne pas le droit d'être malade ou d'avoir un rendez-vous. "
           + "Vous n'avez pas à demander&nbsp;: vous <b>prévenez</b>. «&nbsp;Je ne viens "
           + "pas demain&nbsp;», et vous dites pourquoi." },
      { txt: "« Bonjour. Il faut aller à la clinique demain. »",
        rat_t: "On ne saura pas que c'est vous.",
        rat: "«&nbsp;Il faut&nbsp;» parle de tout le monde. La secrétaire attend un nom, "
           + "un groupe et une raison. Dites <b>je dois</b>&nbsp;: c'est le seul mot qui "
           + "vous met dans la phrase." },
    ],
    pourquoi: "<b>Je dois</b>, pour ce qui est déjà décidé. "
            + "<b>Est-ce que je peux</b>, pour ce que l'autre décide. "
            + "Et la question de la fin — «&nbsp;est-ce que je dois écrire un papier&nbsp;?&nbsp;» — "
            + "vous évite de revenir demain.",
    attente: "Choisissez une réponse pour finir.",
  },

];
