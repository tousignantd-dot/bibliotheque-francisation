// ═══════════════════════════════════════════════════════════════════════════
// Point express — Jamais, rien, personne : dire non sans « pas »
//
// Savoir n2-s08 (Phrases négatives). Une ORDONNANCE : l'enseignant l'envoie à
// un élève qui répond « je mange pas quelque chose » ou « il vient pas
// quelqu'un » — c'est-à-dire qui n'a que « ne… pas » pour dire non. Dix
// minutes, dix écrans, niveau 2.
//
// ── Ce qui le sépare de ce qui existe déjà ─────────────────────────────────
// Le dépôt traite la négation à trois endroits, et les trois s'arrêtent à
// « pas » :
//   · `module-n2-secretaire` — mini-leçon « Dire non : « ne … pas » » : la
//     forme de base, rien d'autre.
//   · `module-n3-loyer` — mini-leçon « Il n'y a pas de : répondre non ».
//   · Deux points express de l'étagère : « J'ai du lait → Je n'ai pas de lait »
//     (le petit mot après « pas ») et « Dire non : ce qui s'entend, ce qui
//     s'écrit » (le « ne » qui tombe à l'oral).
// Un élève qui a tout lu sait faire « ne… pas » et ne sait dire ni « je n'ai
// rien mangé », ni « personne n'est venu ». Les cinq écarts tenus :
//
//   1. INDUCTIF. L'élève range huit réponses entendues AVANT qu'on lui nomme
//      les trois mots. La règle de l'écran 3 est le constat de son tri.
//   2. PARTIEL, JAMAIS LA LISTE. Aucun tableau des négations. Un TEST — de quoi
//      parle la question : un moment, une chose, une personne ? — qui marche
//      sur une phrase jamais vue. « Ne… plus », « ne… aucun », « ne… ni » sont
//      volontairement laissés dehors.
//   3. « PAS » EST DIT EN DERNIER, à l'écran 8 : c'est le cas que l'élève
//      connaît déjà, et le nommer d'entrée ferait croire à quatre règles.
//   4. LE « NE » QUI TOMBE À L'ORAL N'EST PAS LE SUJET. Il a son propre point
//      express ; ici, une seule phrase de rappel, à l'écran 8.
//   5. EXEMPLES VARIÉS, JAMAIS CEUX D'UN MODULE. Un comptoir, un texto, une
//      note à l'école, une salle d'attente, un appel à un propriétaire.
//
// Aucun média : ces trois mots s'entendent parfaitement. Ce que l'élève ne
// sait pas, c'est lequel choisir — et ça se décide sur la question posée.
// ═══════════════════════════════════════════════════════════════════════════

const PARCOURS = {
  slug:     'ne-jamais-rien-personne',
  titre:    "Jamais, rien, personne : dire non sans « pas »",
  surtitre: "Point express · 10 minutes",
  niveau:   2,
  savoir:   'n2-s08',
};

const ECRANS = [

  // ── 1. Une décision, sans aucune règle donnée. ───────────────────────────
  {
    id:   'depart',
    type: 'verif',
    eye:  'Une question, pour commencer',
    menu: 'Au comptoir',
    titre: "Au comptoir, on vous demande : « Vous avez mangé quelque chose ? »",
    consigne: "Vous n'avez rien mangé depuis le matin. Répondez avec ce que vous savez déjà — ou "
            + "au feeling. On expliquera après&nbsp;: c'est fait exprès.",
    options: [
      { txt: "Non, je n'ai rien mangé.", juste: true },
      { txt: "Non, je n'ai pas mangé quelque chose.",
        rat_t: "On vous comprend. Mais personne ne répond comme ça.",
        rat: "Vous avez employé le seul outil que vous aviez&nbsp;: <b>ne… pas</b>. Le problème "
           + "est «&nbsp;quelque chose&nbsp;»&nbsp;: dans une phrase négative, il devient "
           + "<b>rien</b>, et il prend la place de «&nbsp;pas&nbsp;». On va voir comment." },
      { txt: "Non, je n'ai pas rien mangé.",
        rat_t: "Vous avez mis les deux mots, au cas où.",
        rat: "Un seul mot après le verbe. <b>Rien</b> remplace <b>pas</b>, il ne s'ajoute pas à "
           + "lui. Mettre les deux dit en fait le contraire&nbsp;: que vous avez mangé quelque "
           + "chose." },
    ],
    pourquoi: "«&nbsp;Je n'ai rien mangé.&nbsp;» Gardez cette phrase&nbsp;: on y revient au "
            + "dernier écran.",
    attente: "Choisissez une réponse pour continuer.",
  },

  // ── 2. On trie AVANT de savoir. ──────────────────────────────────────────
  {
    id:   'tri-questions',
    type: 'tri',
    eye:  'À vous de trancher',
    menu: 'Huit questions',
    titre: "Huit questions. Sur quoi porte chacune ?",
    consigne: "Ne cherchez pas la réponse. Demandez-vous seulement de quoi on vous "
            + "parle&nbsp;: d'un <b>moment</b>, d'une <b>chose</b>, ou d'une <b>personne</b>&nbsp;? "
            + "Aucune règle ne vous a été donnée — c'est normal.",
    colonnes: [
      { id: 'mom', t: "Un moment",   b: "Un moment" },
      { id: 'cho', t: "Une chose",   b: "Une chose" },
      { id: 'per', t: "Une personne", b: "Une personne" },
    ],
    items: [
      { txt: "Vous avez déjà pris l'autobus 55 ?", sous: "un collègue, à la pause", ok: 'mom',
        rat: "«&nbsp;Déjà&nbsp;» parle du temps&nbsp;: est-ce arrivé une fois, un jour&nbsp;? "
           + "La question porte sur un <b>moment</b>.",
        pourquoi: "« déjà » : la question porte sur un moment." },
      { txt: "Quelqu'un a téléphoné pour moi ?", sous: "en rentrant à la maison", ok: 'per',
        rat: "«&nbsp;Quelqu'un&nbsp;» est une <b>personne</b> qu'on ne nomme pas. La question ne "
           + "porte ni sur un moment ni sur un objet.",
        pourquoi: "« quelqu'un » : la question porte sur une personne." },
      { txt: "Vous voulez quelque chose à boire ?", sous: "chez une voisine", ok: 'cho',
        rat: "«&nbsp;Quelque chose&nbsp;» est une <b>chose</b>&nbsp;: un café, un verre d'eau. "
           + "Ce n'est ni un moment ni une personne.",
        pourquoi: "« quelque chose » : la question porte sur une chose." },
      { txt: "Vous êtes souvent en retard ?", sous: "un employeur, en entrevue", ok: 'mom',
        rat: "«&nbsp;Souvent&nbsp;» compte les fois. C'est encore une question de <b>moment</b>.",
        pourquoi: "« souvent » : la question porte sur un moment." },
      { txt: "Il y a quelqu'un dans le bureau ?", sous: "au comptoir d'un centre", ok: 'per',
        rat: "On demande si une <b>personne</b> se trouve là. Le lieu est dans la phrase, mais "
           + "ce qu'on cherche, c'est quelqu'un.",
        pourquoi: "« quelqu'un » : la question porte sur une personne." },
      { txt: "Vous avez oublié quelque chose ?", sous: "à la fin d'un rendez-vous", ok: 'cho',
        rat: "Un papier, un manteau, une carte&nbsp;: c'est une <b>chose</b>.",
        pourquoi: "« quelque chose » : la question porte sur une chose." },
      { txt: "Vous travaillez le samedi, parfois ?", sous: "un texto à une amie", ok: 'mom',
        rat: "«&nbsp;Parfois&nbsp;» parle de la fréquence, comme «&nbsp;souvent&nbsp;» et "
           + "«&nbsp;déjà&nbsp;». Un <b>moment</b>.",
        pourquoi: "« parfois » : la question porte sur un moment." },
      { txt: "Quelqu'un vous a expliqué le formulaire ?", sous: "à la clinique", ok: 'per',
        rat: "Le formulaire est dans la phrase, mais la question est&nbsp;: <b>qui</b> vous l'a "
           + "expliqué. C'est une personne.",
        pourquoi: "La question est « qui ? » : une personne." },
    ],
    attente: "Tranchez les huit questions pour continuer.",
  },

  // ── 3. La règle, écrite comme un constat. ────────────────────────────────
  {
    id:   'le-constat',
    type: 'notion',
    eye:  'Ce que vous venez de faire',
    menu: 'Trois mots',
    titre: "Vos trois colonnes sont exactement trois façons de dire non.",
    paras: [
      "Pour répondre non à ces questions, vous n'employez pas «&nbsp;pas&nbsp;». Vous employez "
      + "le mot qui va avec la colonne&nbsp;:",

      "<b>Un moment</b> → <b>jamais</b>. «&nbsp;Je n'ai <b>jamais</b> pris l'autobus 55.&nbsp;» "
      + "<b>Une chose</b> → <b>rien</b>. «&nbsp;Je ne veux <b>rien</b>, merci.&nbsp;» "
      + "<b>Une personne</b> → <b>personne</b>. «&nbsp;Je n'ai vu <b>personne</b>.&nbsp;»",

      "<b>Le test, à appliquer sur n'importe quelle question&nbsp;:</b> demandez-vous ce qu'on "
      + "vous demande — un moment, une chose, quelqu'un — et prenez le mot de cette colonne-là. "
      + "Il se met à la place de «&nbsp;pas&nbsp;», jamais avec lui.",
    ],
    retenir: "Un moment&nbsp;: <b>jamais</b>. Une chose&nbsp;: <b>rien</b>. Quelqu'un&nbsp;: "
           + "<b>personne</b>. Et le mot <b>ne</b> reste toujours devant le verbe.",
    attente: "Lisez, puis continuez.",
  },

  // ── 4. Le premier piège : les deux mots ensemble. ────────────────────────
  {
    id:   'un-seul-mot',
    type: 'verif',
    eye:  'Le piège',
    menu: 'Un seul mot',
    titre: "On vous demande : « Vous venez souvent au centre le soir ? »",
    consigne: "Vous n'y venez jamais le soir. Quelle phrase écrivez-vous dans un courriel&nbsp;?",
    options: [
      { txt: "Je ne viens jamais le soir.", juste: true },
      { txt: "Je ne viens pas jamais le soir.",
        rat_t: "Vous avez gardé «&nbsp;pas&nbsp;» par sécurité.",
        rat: "C'est le réflexe de tout le monde&nbsp;: on a appris «&nbsp;ne… pas&nbsp;» et on "
           + "n'ose pas le lâcher. Mais <b>jamais</b> prend exactement la place de "
           + "«&nbsp;pas&nbsp;». Un seul des deux, jamais les deux ensemble." },
      { txt: "Je viens jamais pas le soir.",
        rat_t: "Il manque le mot le plus discret de la phrase.",
        rat: "Deux choses&nbsp;: «&nbsp;pas&nbsp;» est en trop, et le mot <b>ne</b> a disparu. À "
           + "l'oral, on l'entend rarement&nbsp;; à l'écrit, il s'écrit toujours&nbsp;: "
           + "«&nbsp;je <b>ne</b> viens jamais&nbsp;»." },
    ],
    pourquoi: "<b>Ne + le mot choisi.</b> Deux mots par phrase, pas trois.",
    attente: "Choisissez une réponse pour continuer.",
  },

  // ── 5. La place, et la réponse courte. ───────────────────────────────────
  {
    id:   'la-place',
    type: 'notion',
    eye:  'Où se mettent ces mots',
    menu: 'La place',
    titre: "Deux d'entre eux se mettent où va « pas ». Le troisième bouge.",
    paras: [
      "<b>Jamais</b> et <b>rien</b> prennent la place de «&nbsp;pas&nbsp;», sans rien changer "
      + "d'autre&nbsp;: «&nbsp;je ne comprends <b>pas</b>&nbsp;» → «&nbsp;je ne comprends "
      + "<b>rien</b>&nbsp;». «&nbsp;Il n'est <b>pas</b> venu&nbsp;» → «&nbsp;il n'est <b>jamais</b> "
      + "venu&nbsp;».",

      "<b>Personne</b> se met <b>à la fin</b> quand le verbe est au passé&nbsp;: «&nbsp;je n'ai "
      + "vu <b>personne</b>&nbsp;», et non «&nbsp;je n'ai personne vu&nbsp;». C'est le seul des "
      + "trois qui se comporte ainsi.",

      "Et pour répondre vite, le mot suffit tout seul&nbsp;: «&nbsp;— Vous voulez quelque "
      + "chose&nbsp;? — <b>Rien</b>, merci.&nbsp;» «&nbsp;— Qui est là&nbsp;? — "
      + "<b>Personne</b>.&nbsp;» «&nbsp;— Vous y allez le samedi&nbsp;? — <b>Jamais</b>.&nbsp;» "
      + "Là, il n'y a ni «&nbsp;ne&nbsp;», ni verbe.",
    ],
    retenir: "<b>Rien</b> et <b>jamais</b> à la place de «&nbsp;pas&nbsp;». <b>Personne</b> à la "
           + "fin. Et seuls, en réponse courte.",
    attente: "Lisez, puis continuez.",
  },

  // ── 6. Trier des phrases écrites. ────────────────────────────────────────
  {
    id:   'tri-ecrites',
    type: 'tri',
    eye:  'À vous de trancher',
    menu: 'Six phrases',
    titre: "Six phrases écrites. Lesquelles sont correctes ?",
    consigne: "Deux choses à regarder&nbsp;: y a-t-il un seul mot de négation, et le mot "
            + "<b>ne</b> est-il écrit&nbsp;?",
    colonnes: [
      { id: 'ok',   t: 'Correct',   b: 'Correct' },
      { id: 'faux', t: 'Une faute', b: 'Une faute' },
    ],
    items: [
      { txt: "Je n'ai rien reçu par la poste.", ok: 'ok',
        rat: "<b>Ne</b> devant le verbe, <b>rien</b> à la place de «&nbsp;pas&nbsp;». Deux mots, "
           + "et c'est juste.",
        pourquoi: "« ne » + « rien ». Juste." },
      { txt: "Elle n'a pas jamais travaillé ici.", ok: 'faux',
        rat: "«&nbsp;Pas&nbsp;» et «&nbsp;jamais&nbsp;» disent la même chose&nbsp;: on n'en garde "
           + "qu'un. «&nbsp;Elle n'a <b>jamais</b> travaillé ici.&nbsp;»",
        pourquoi: "Il faut « elle n'a jamais travaillé »." },
      { txt: "Je n'ai vu personne dans le couloir.", ok: 'ok',
        rat: "<b>Personne</b> est bien à la fin, après le verbe au passé. C'est sa place.",
        pourquoi: "« personne » à la fin. Juste." },
      { txt: "Il ne mange rien le matin.", ok: 'ok',
        rat: "<b>Rien</b> occupe exactement la place de «&nbsp;pas&nbsp;»&nbsp;: «&nbsp;il ne "
           + "mange pas&nbsp;» → «&nbsp;il ne mange rien&nbsp;».",
        pourquoi: "« rien » à la place de « pas ». Juste." },
      { txt: "Je n'ai personne rencontré au centre.", ok: 'faux',
        rat: "C'est le seul des trois qui ne se met pas là. Il va à la fin&nbsp;: «&nbsp;je n'ai "
           + "rencontré <b>personne</b> au centre&nbsp;».",
        pourquoi: "Il faut « je n'ai rencontré personne »." },
      { txt: "Nous ne travaillons jamais le dimanche.", ok: 'ok',
        rat: "<b>Ne</b> écrit, un seul mot de négation, à la bonne place. Rien à corriger.",
        pourquoi: "« ne » + « jamais ». Juste." },
    ],
    attente: "Tranchez les six phrases pour continuer.",
  },

  // ── 7. « Personne » en tête de phrase. ───────────────────────────────────
  {
    id:   'personne-devant',
    type: 'verif',
    eye:  'Vérification',
    menu: 'En début de phrase',
    titre: "Vous écrivez à votre propriétaire : le concierge n'est pas passé.",
    consigne: "Vous voulez dire qu'aucune personne n'est venue réparer le robinet. Quelle "
            + "phrase&nbsp;?",
    options: [
      { txt: "Personne n'est venu réparer le robinet.", juste: true },
      { txt: "Personne est venu réparer le robinet.",
        rat_t: "Le mot est au bon endroit. C'est le petit mot qui manque.",
        rat: "Même en tête de phrase, <b>ne</b> reste devant le verbe&nbsp;: «&nbsp;personne "
           + "<b>n'</b>est venu&nbsp;». C'est le mot le plus facile à oublier, parce qu'on ne "
           + "l'entend presque jamais." },
      { txt: "Ne personne est venu réparer le robinet.",
        rat_t: "Vous avez mis le petit mot, mais du mauvais côté.",
        rat: "<b>Ne</b> se colle toujours au verbe, pas au mot de négation. Ici, le verbe est "
           + "«&nbsp;est&nbsp;»&nbsp;: «&nbsp;Personne <b>n'est</b> venu&nbsp;»." },
    ],
    pourquoi: "<b>Personne</b> peut être le sujet de la phrase — et alors il passe devant. Le "
            + "«&nbsp;ne&nbsp;», lui, ne quitte jamais le verbe.",
    attente: "Choisissez une réponse pour continuer.",
  },

  // ── 8. « Pas » en dernier : le cas qu'il connaissait déjà. ───────────────
  {
    id:   'et-pas',
    type: 'notion',
    eye:  'Ce qui reste',
    menu: 'Et « pas » ?',
    titre: "« Pas » n'a rien perdu. Il sert dans tous les autres cas.",
    paras: [
      "On a gardé «&nbsp;pas&nbsp;» pour la fin, et c'est volontaire&nbsp;: c'est celui que vous "
      + "connaissez, et le nommer d'abord aurait fait quatre règles à retenir. En vérité, il n'y "
      + "en a qu'une&nbsp;: <b>on emploie « pas », sauf quand la question porte sur un moment, "
      + "une chose ou une personne</b>.",

      "«&nbsp;Je ne comprends <b>pas</b>.&nbsp;» «&nbsp;Ce n'est <b>pas</b> ouvert.&nbsp;» "
      + "«&nbsp;Je ne suis <b>pas</b> en retard.&nbsp;» Aucun moment, aucune chose, aucune "
      + "personne&nbsp;: c'est «&nbsp;pas&nbsp;».",

      "Un mot sur le <b>ne</b>, pour finir&nbsp;: à l'oral, au Québec, vous ne l'entendrez presque "
      + "jamais — «&nbsp;j'ai rien vu&nbsp;», «&nbsp;y a personne&nbsp;». Ce n'est pas votre "
      + "oreille. Mais dès que vous <b>écrivez</b>, il s'écrit.",
    ],
    retenir: "Une seule règle&nbsp;: «&nbsp;pas&nbsp;» partout, <b>sauf</b> pour un moment, une "
           + "chose ou une personne.",
    attente: "Lisez, puis continuez.",
  },

  // ── 9. Écrire, pas reconnaître. ──────────────────────────────────────────
  {
    id:   'votre-message',
    type: 'verif',
    eye:  'Vérification',
    menu: 'Votre message',
    titre: "Lina écrit à l'école. Quelle version tient d'un bout à l'autre ?",
    consigne: "Sa fille est restée à la maison hier. Personne n'a appelé, et l'enfant n'a rien "
            + "mangé de la journée.",
    options: [
      { txt: "Nour est restée à la maison hier. Personne n'a téléphoné, et elle n'a rien mangé.",
        juste: true },
      { txt: "Nour est restée à la maison hier. Personne a téléphoné, et elle n'a pas rien mangé.",
        rat_t: "Les deux mots de négation sont bien choisis. Ce sont les petits mots qui ont lâché.",
        rat: "Deux corrections&nbsp;: le <b>ne</b> manque dans «&nbsp;personne <b>n'</b>a "
           + "téléphoné&nbsp;», et «&nbsp;pas&nbsp;» est en trop dans «&nbsp;elle n'a "
           + "<b>rien</b> mangé&nbsp;». Un seul mot de négation par phrase." },
      { txt: "Nour est restée à la maison hier. Rien n'a téléphoné, et elle n'a personne mangé.",
        rat_t: "Vous avez interverti les deux mots.",
        rat: "Un téléphone se prend par <b>quelqu'un</b>&nbsp;: c'est «&nbsp;personne&nbsp;». Ce "
           + "qu'on mange est une <b>chose</b>&nbsp;: c'est «&nbsp;rien&nbsp;». Le test de "
           + "l'écran 3 tranche les deux d'un coup." },
    ],
    pourquoi: "Personne pour la personne, rien pour la chose, et le <b>ne</b> écrit deux fois. "
            + "<b>C'est tout le point en une phrase.</b>",
    attente: "Choisissez une réponse pour continuer.",
  },

  // ── 10. La fermeture : le cas de l'écran 1. ──────────────────────────────
  {
    id:   'fermeture',
    type: 'verif',
    eye:  'La dernière',
    menu: 'Pour finir',
    titre: "On revient au comptoir. « Vous avez mangé quelque chose ? »",
    consigne: "Cette fois, on vous pose une deuxième question&nbsp;: «&nbsp;Et quelqu'un vous "
            + "accompagne&nbsp;?&nbsp;» Vous êtes seule. Quelle réponse&nbsp;?",
    options: [
      { txt: "Non, je n'ai rien mangé, et personne ne m'accompagne.", juste: true },
      { txt: "Non, je n'ai rien mangé, et je n'accompagne personne.",
        rat_t: "La première moitié est parfaite. La seconde dit autre chose.",
        rat: "Regardez qui fait quoi&nbsp;: dans votre phrase, c'est <b>vous</b> qui "
           + "n'accompagnez personne. Or on vous demandait si quelqu'un vous accompagne, "
           + "<b>vous</b>&nbsp;: «&nbsp;personne ne m'accompagne&nbsp;»." },
      { txt: "Non, je n'ai pas mangé rien, et personne m'accompagne.",
        rat_t: "Les deux moitiés ont chacune un défaut, et ce sont les deux du point.",
        rat: "«&nbsp;Pas&nbsp;» est en trop devant «&nbsp;rien&nbsp;», et le <b>ne</b> manque "
           + "devant «&nbsp;m'accompagne&nbsp;». Un seul mot de négation, et le "
           + "«&nbsp;ne&nbsp;» toujours écrit." },
    ],
    pourquoi: "Vous avez fait les trois choses&nbsp;: choisir le mot d'après la question, n'en "
            + "garder qu'un, et écrire le «&nbsp;ne&nbsp;» qu'on n'entend pas.",
    attente: "Choisissez une réponse pour finir.",
  },

];
