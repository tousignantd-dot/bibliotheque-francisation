// ═══════════════════════════════════════════════════════════════════════════
// BLOC A — « Un instant, s'il vous plaît »
// Démonstration détail · Chaussures Rivard (magasin fictif)
//
// Le premier des quatre blocs. C'est celui qu'on montre à un marchand : si
// l'on ne devait payer qu'une heure, ce serait celle-là. Un vendeur qui dit
// « oui » sans avoir compris ne casse rien, ne fâche personne, et ne laisse
// aucune trace — le client sort, et personne dans le magasin ne sait qu'il y
// a eu une vente perdue. C'est la version détail du « oui, oui » de l'usine,
// en pire : à l'usine, la palette encore pleine finit par se voir.
//
// ── Ce que le bloc enseigne ────────────────────────────────────────────────
// Quatre gestes, et un cinquième qui est le plus difficile :
//   1. ARRÊTER        « Un instant, s'il vous plaît. »
//   2. FAIRE PRÉCISER « Vous cherchez quel modèle ? Quelle pointure ? »
//   3. REDIRE         « Trente-huit, en large. Je vais voir en réserve. »
//   4. TENIR LA PORTE « Parfait. Je suis là si vous avez besoin. »
//   5. PASSER LE RELAIS « Un instant. Je vais chercher ma collègue. »
//
// Le cinquième est le plus dur parce qu'il se sent comme un aveu. Tout le
// bloc sert à établir que ce n'en est pas un : il garde le client dans le
// magasin, ce qu'aucune autre réponse ne fait.
//
// ── Pourquoi ce n'est pas du programme ─────────────────────────────────────
// Le programme ministériel enseigne à ACHETER, jamais à VENDRE : neuf
// situations d'achat entre les niveaux 2, 3 et 4, toutes écrites du côté du
// client. Une seule intention, dans tout le programme, touche le fait de
// servir quelqu'un. Ce bloc est donc une formation AU POSTE, comme le bloc 3
// de Belrive, et il ne s'inscrit pas au catalogue avec une situation.
//
// ── Le casting, compté AVANT d'écrire ──────────────────────────────────────
// Quatre voix, deux par genre, et deux personnages du même genre ne peuvent
// pas se répondre. D'où un client MASCULIN : il libère les deux voix
// féminines pour Yasmine et Chantal, qui, elles, se répondent.
// Contraste mesuré : le client à 18,8 car/s, Yasmine à 12,5 — ×1,51. On n'a
// pas eu à écrire que le client parle vite.
//
// ── Les images ─────────────────────────────────────────────────────────────
// AUCUNE, et c'est volontaire : le registre n'est pas tranché. Le banc est
// fait (assets/presentations/chaussure/banc/), il reste à le juger à la
// taille de la carte. Tout dessin produit avant cette décision est à refaire.
// ═══════════════════════════════════════════════════════════════════════════

const PARCOURS = {
  slug:     'chaussure-blocA',
  module:   'entreprise-chaussure',
  titre:    "Un instant, s'il vous plaît",
  surtitre: "Chaussures Rivard · Bloc A sur 4",
  niveau:   2,
  appui: [
    { c: 'es', n: 'Español' },
    { c: 'en', n: 'English' },
  ],
};

const ECRANS = [

  // ── 1. LE MOMENT. On tranche avant d'avoir rien appris. ──────────────────
  {
    id:   'il-est-parti',
    type: 'verif',
    eye:  'Le moment',
    menu: 'Il est parti',
    titre: "Yasmine a dit «&nbsp;oui&nbsp;». Que va-t-il arriver&nbsp;?",
    consigne: "Écoutez les trois extraits, puis répondez avec ce que vous savez déjà.",
    sons: [
      { fichier: 'a1.mp3', qui: 'Un client, en entrant',
        texte: "Bonjour&nbsp;! Écoutez, le soulier brun là, dans la vitrine, vous l'auriez-tu en trente-huit pis en large&nbsp;?" },
      { fichier: 'a2.mp3', qui: 'Yasmine, nouvelle vendeuse',
        texte: "Oui… bonjour&nbsp;!" },
      { fichier: 'a3.mp3', qui: 'Chantal, gérante, deux minutes plus tard',
        texte: "Yasmine&nbsp;? Le monsieur est reparti. Il est allé voir en face." },
    ],
    options: [
      { txt: "Le client va revenir&nbsp;: il n'a pas eu sa réponse.",
        rat_t: "Réécoutez le troisième extrait.",
        rat: "Il est déjà chez le concurrent. Un client qui n'obtient pas de réponse ne redemande pas&nbsp;: il sort." },
      { txt: "Une vente est perdue, et personne dans le magasin ne saura pourquoi.", juste: true },
      { txt: "Chantal va s'apercevoir que Yasmine n'avait pas compris.",
        rat_t: "C'est justement ce qui n'arrive jamais.",
        rat: "Chantal voit un client qui sort. Elle ne sait pas qu'on lui a demandé un trente-huit en large. Rien n'est cassé, rien n'est noté&nbsp;: c'est pour ça que ça se répète." },
    ],
    pourquoi: "À l'usine, une palette encore pleine finit par se voir. Dans un magasin, <b>une vente perdue ne laisse aucune trace</b>. C'est le défaut le plus cher du plancher, et le seul que personne ne signale.",
    attente: "Choisissez une réponse pour continuer.",
    es: {
      attente: "Elija una respuesta para continuar.",
      titre: "Yasmine dijo « oui ». ¿Qué va a pasar?",
      consigne: "Escuche los tres audios y responda con lo que ya sabe.",
      options: [
        { rat_t: "Vuelva a escuchar el tercer audio.",
          rat: "Ya está en la tienda de enfrente. Un cliente que no obtiene respuesta no vuelve a preguntar: se va." },
        {},
        { rat_t: "Eso es precisamente lo que nunca pasa.",
          rat: "Chantal ve a un cliente que sale. No sabe que le pidieron un treinta y ocho ancho. Nada se rompe, nada queda anotado: por eso se repite." },
      ],
      pourquoi: "En una fábrica, una paleta llena acaba por verse. En una tienda, <b>una venta perdida no deja ningún rastro</b>. Es el defecto más caro del piso de venta, y el único que nadie señala.",
    },
    en: {
      attente: "Choose an answer to continue.",
      titre: "Yasmine said « oui ». What is going to happen?",
      consigne: "Listen to the three clips, then answer with what you already know.",
      options: [
        { rat_t: "Listen to the third clip again.",
          rat: "He is already across the street. A customer who gets no answer does not ask twice: he leaves." },
        {},
        { rat_t: "That is exactly what never happens.",
          rat: "Chantal sees a customer walking out. She does not know he asked for a thirty-eight in a wide fit. Nothing breaks, nothing is written down — which is why it keeps happening." },
      ],
      pourquoi: "In a plant, a pallet left full eventually shows. In a shop, <b>a lost sale leaves no trace at all</b>. It is the most expensive fault on the floor, and the only one nobody reports.",
    },
  },

  // ── 2. Le vrai problème n'est pas le vocabulaire. ────────────────────────
  {
    id:   'deux-questions',
    type: 'notion',
    eye:  "Ce qui s'est vraiment passé",
    menu: 'Deux questions',
    titre: "Le client a posé deux questions en cinq secondes.",
    paras: [
      "Réécoutez-le. Il n'a pas été impoli et son français n'est pas difficile&nbsp;: "
      + "il a posé <b>deux questions d'affilée</b>, vite, en marchant vers la vitrine.",

      "<b>1.</b> Avez-vous ce modèle&nbsp;? <b>2.</b> En trente-huit, et en large&nbsp;?",

      "Le problème n'est pas le vocabulaire de Yasmine. Elle connaît «&nbsp;pointure&nbsp;», "
      + "elle connaît «&nbsp;large&nbsp;». Le problème, c'est <b>la vitesse et le nombre</b> — "
      + "et le fait qu'elle n'a pas osé arrêter quelqu'un qui entrait dans son magasin.",
    ],
    sons: [
      { fichier: 'a1.mp3', qui: 'Un client, en entrant',
        texte: "Bonjour&nbsp;! Écoutez, le soulier brun là, dans la vitrine, vous l'auriez-tu en trente-huit pis en large&nbsp;?" },
    ],
    retenir: "Vous n'avez pas à apprendre plus de mots pour régler ça. Vous avez à <b>arrêter le client</b> — et il ne demande que ça.",
    attente: "Écoutez l'extrait, puis continuez.",
    es: {
      attente: "Escuche el audio y continúe.",
      titre: "El cliente hizo dos preguntas en cinco segundos.",
      paras: [
        "Vuelva a escucharlo. No fue grosero y su francés no es difícil: hizo <b>dos preguntas seguidas</b>, rápido, mientras caminaba hacia el escaparate.",
        "<b>1.</b> ¿Tienen este modelo? <b>2.</b> ¿En treinta y ocho, y ancho?",
        "El problema no es el vocabulario de Yasmine. Ella conoce « pointure », conoce « large ». El problema es <b>la velocidad y la cantidad</b> — y que no se atrevió a detener a alguien que entraba en su tienda.",
      ],
      retenir: "No necesita aprender más palabras para resolver esto. Necesita <b>detener al cliente</b> — y él no pide otra cosa.",
    },
    en: {
      attente: "Listen to the clip, then continue.",
      titre: "The customer asked two questions in five seconds.",
      paras: [
        "Listen again. He was not rude and his French is not hard: he asked <b>two questions in a row</b>, fast, while walking towards the window display.",
        "<b>1.</b> Do you have this model? <b>2.</b> In a thirty-eight, and a wide fit?",
        "The problem is not Yasmine's vocabulary. She knows « pointure », she knows « large ». The problem is <b>speed and number</b> — and that she did not dare stop someone walking into her own shop.",
      ],
      retenir: "You do not need more words to fix this. You need to <b>stop the customer</b> — and it is all he is waiting for.",
    },
  },

  // ── 3. La reprise, en entier. Les trois gestes. ──────────────────────────
  {
    id:   'trois-gestes',
    type: 'notion',
    eye:  'La même scène, autrement',
    menu: 'Trois gestes',
    titre: "Voici la même scène, avec trois gestes de plus.",
    paras: [
      "Rien n'a changé chez le client&nbsp;: il parle aussi vite. C'est Yasmine qui fait "
      + "trois choses.",

      "<b>1. Arrêter</b> — «&nbsp;Un instant, s'il vous plaît.&nbsp;» "
      + "<b>2. Faire préciser, une chose à la fois</b> — «&nbsp;Vous cherchez quel "
      + "modèle&nbsp;?&nbsp;» puis «&nbsp;Et quelle pointure&nbsp;?&nbsp;» "
      + "<b>3. Redire</b> — elle répète la demande dans ses mots avant d'aller en réserve.",

      "Écoutez la fin&nbsp;: le client dit «&nbsp;parfait, merci&nbsp;». <b>Il n'est pas "
      + "impatient.</b> Il a attendu quinze secondes de plus et il est encore dans le magasin — "
      + "ce qui ne serait pas arrivé autrement.",
    ],
    sons: [
      { fichier: 'b1.mp3', qui: 'Le client', texte: "Bonjour&nbsp;! Écoutez, le soulier brun là, dans la vitrine, vous l'auriez-tu en trente-huit pis en large&nbsp;?" },
      { fichier: 'b2.mp3', qui: 'Yasmine', texte: "Un instant, s'il vous plaît. Vous cherchez quel modèle&nbsp;?" },
      { fichier: 'b3.mp3', qui: 'Le client', texte: "Le brun, là. Dans la vitrine." },
      { fichier: 'b4.mp3', qui: 'Yasmine', texte: "Le brun. Et quelle pointure&nbsp;?" },
      { fichier: 'b5.mp3', qui: 'Le client', texte: "Trente-huit. En large, si vous l'avez." },
      { fichier: 'b6.mp3', qui: 'Yasmine', texte: "Trente-huit, en large. Je vais voir en réserve. Je reviens tout de suite." },
      { fichier: 'b7.mp3', qui: 'Le client', texte: "Parfait, merci." },
    ],
    retenir: "«&nbsp;Je reviens tout de suite&nbsp;» est la moitié du geste. Un client qui sait qu'on revient attend&nbsp;; un client qui vous voit disparaître s'en va.",
    attente: "Écoutez l'échange, puis continuez.",
    es: {
      attente: "Escuche el diálogo y continúe.",
      titre: "Esta es la misma escena, con tres gestos más.",
      paras: [
        "Nada ha cambiado en el cliente: habla igual de rápido. Es Yasmine quien hace tres cosas.",
        "<b>1. Detener</b> — « Un instant, s'il vous plaît. » <b>2. Hacer precisar, una cosa a la vez</b> — « Vous cherchez quel modèle ? » y luego « Et quelle pointure ? » <b>3. Repetir</b> — repite el pedido con sus palabras antes de ir al almacén.",
        "Escuche el final: el cliente dice « parfait, merci ». <b>No está impaciente.</b> Esperó quince segundos más y sigue en la tienda — lo que no habría pasado de otro modo.",
      ],
      retenir: "« Je reviens tout de suite » es la mitad del gesto. Un cliente que sabe que usted vuelve espera; un cliente que lo ve desaparecer se va.",
    },
    en: {
      attente: "Listen to the exchange, then continue.",
      titre: "Here is the same scene, with three more moves.",
      paras: [
        "Nothing has changed about the customer: he speaks just as fast. It is Yasmine who does three things.",
        "<b>1. Stop him</b> — « Un instant, s'il vous plaît. » <b>2. Make him be specific, one thing at a time</b> — « Vous cherchez quel modèle ? » then « Et quelle pointure ? » <b>3. Say it back</b> — she repeats the request in her own words before going to the stockroom.",
        "Listen to the end: the customer says « parfait, merci ». <b>He is not impatient.</b> He waited fifteen seconds longer and he is still in the shop — which would not have happened otherwise.",
      ],
      retenir: "« Je reviens tout de suite » is half the move. A customer who knows you are coming back waits; a customer who watches you vanish leaves.",
    },
  },

  // ── 4. Le tri. Ce qui aide, ce qui nuit, à l'accueil. ────────────────────
  {
    id:   'huit-phrases',
    type: 'tri',
    eye:  'À vous de trancher',
    menu: 'Huit phrases',
    titre: "Huit phrases pour accueillir quelqu'un. Lesquelles vous aident&nbsp;?",
    consigne: "Toutes se disent en français. Mais devant un client pressé, elles n'ont pas "
            + "le même effet.",
    colonnes: [
      { id: 'aide', t: 'Ça vous aide', b: 'Ça vous aide' },
      { id: 'nuit', t: 'Ça vous nuit', b: 'Ça vous nuit' },
    ],
    items: [
      { txt: "Un instant, s'il vous plaît.", ok: 'aide',
        rat: "C'est la phrase la plus utile du bloc. Quatre mots, polie, et elle arrête n'importe qui sans le vexer.",
        pourquoi: "Un instant, s'il vous plaît. — elle arrête sans vexer." },
      { txt: "Oui.", ok: 'nuit',
        rat: "Elle vous nuit deux fois&nbsp;: le client croit que vous avez compris, et il repart sans sa réponse.",
        pourquoi: "« Oui » — le client croit que vous avez compris." },
      { txt: "Vous cherchez quel modèle&nbsp;?", ok: 'aide',
        rat: "Elle demande <b>une</b> chose. C'est ce qui la rend efficace&nbsp;: le client sait quoi répondre.",
        pourquoi: "Vous cherchez quel modèle ? — une seule chose à la fois." },
      { txt: "Hein&nbsp;?", ok: 'nuit',
        rat: "Elle se dit entre amis, mais elle sonne sec — et surtout elle ne demande rien de précis&nbsp;: le client va répéter à la même vitesse.",
        pourquoi: "« Hein ? » — et il répétera aussi vite." },
      { txt: "Quelle pointure, s'il vous plaît&nbsp;?", ok: 'aide',
        rat: "Une question fermée, à laquelle on répond par un nombre. C'est la plus facile à comprendre de tout le magasin.",
        pourquoi: "Quelle pointure ? — on répond par un nombre." },
      { txt: "Je m'excuse, je m'excuse, mon français n'est pas très bon…", ok: 'nuit',
        rat: "Trop long, et elle déplace le problème sur vous. Le client ne veut pas évaluer votre français&nbsp;: il veut ses souliers. La politesse tient dans «&nbsp;s'il vous plaît&nbsp;».",
        pourquoi: "Trop long — et le client n'est pas venu juger votre français." },
      { txt: "Un instant. Je vais chercher ma collègue.", ok: 'aide',
        rat: "Elle garde le client dans le magasin. C'est la seule chose qui compte, et aucune autre réponse ne le fait.",
        pourquoi: "Je vais chercher ma collègue. — le client reste." },
      { txt: "Je sais pas.", ok: 'nuit',
        rat: "Elle ferme la porte. Elle n'est pas fausse, mais elle ne propose rien&nbsp;: le client n'a plus qu'à sortir. Dites plutôt&nbsp;: «&nbsp;Je vais vérifier.&nbsp;»",
        pourquoi: "Dites plutôt : « Je vais vérifier. »" },
    ],
    attente: "Rangez les huit phrases pour continuer.",
    es: {
      attente: "Clasifique las ocho frases para continuar.",
      titre: "Ocho frases para atender a alguien. ¿Cuáles le ayudan?",
      consigne: "Todas existen en francés. Pero ante un cliente apurado, no tienen el mismo efecto.",
    },
    en: {
      attente: "Sort the eight sentences to continue.",
      titre: "Eight ways to greet someone. Which ones help you?",
      consigne: "They are all real French. But in front of a customer in a hurry, they do not have the same effect.",
    },
  },

  // ── 5. « Je regarde. » Le piège inverse. ─────────────────────────────────
  {
    id:   'je-regarde',
    type: 'verif',
    eye:  'Le piège inverse',
    menu: '« Je regarde »',
    titre: "Un client entre et dit&nbsp;: «&nbsp;Non, non, je regarde.&nbsp;»",
    consigne: "Écoutez, puis choisissez ce que vous faites.",
    sons: [
      { fichier: 'd1.mp3', qui: 'Un client', texte: "Non, non, je regarde." },
    ],
    options: [
      { txt: "Vous le laissez et vous retournez à la réserve.",
        rat_t: "Il vient de dire qu'il regarde — pas qu'il n'achètera pas.",
        rat: "La moitié des gens qui disent «&nbsp;je regarde&nbsp;» ont une question trente secondes plus tard. S'ils ne vous voient plus, ils sortent avec leur question." },
      { txt: "Vous le suivez pour lui montrer les nouveautés.",
        rat_t: "Il a dit non.",
        rat: "Le suivre après un «&nbsp;non&nbsp;» est la façon la plus sûre de le faire sortir. Il faut le laisser tranquille <b>et</b> rester joignable&nbsp;: ce n'est pas la même chose." },
      { txt: "Vous répondez une phrase, et vous restez dans son champ de vision.", juste: true },
    ],
    pourquoi: "«&nbsp;Parfait. Je suis là si vous avez besoin.&nbsp;» — huit mots, et vous avez laissé la porte ouverte sans insister. <b>Rester visible n'est pas insister</b>&nbsp;; c'est ce qui permet au client de revenir vers vous.",
    attente: "Choisissez une réponse pour continuer.",
    es: {
      attente: "Elija una respuesta para continuar.",
      titre: "Un cliente entra y dice: « Non, non, je regarde. »",
      consigne: "Escuche y elija qué hace usted.",
      options: [
        { rat_t: "Acaba de decir que está mirando — no que no va a comprar.",
          rat: "La mitad de las personas que dicen « je regarde » tienen una pregunta treinta segundos después. Si ya no lo ven a usted, salen con su pregunta." },
        { rat_t: "Dijo que no.",
          rat: "Seguirlo después de un « no » es la forma más segura de que se vaya. Hay que dejarlo tranquilo <b>y</b> seguir disponible: no es lo mismo." },
        {},
      ],
      pourquoi: "« Parfait. Je suis là si vous avez besoin. » — ocho palabras, y usted dejó la puerta abierta sin insistir. <b>Quedarse visible no es insistir</b>; es lo que permite que el cliente vuelva hacia usted.",
    },
    en: {
      attente: "Choose an answer to continue.",
      titre: "A customer comes in and says: « Non, non, je regarde. »",
      consigne: "Listen, then choose what you do.",
      options: [
        { rat_t: "He just said he is browsing — not that he will not buy.",
          rat: "Half the people who say « je regarde » have a question thirty seconds later. If they cannot see you any more, they leave with the question." },
        { rat_t: "He said no.",
          rat: "Following him after a « no » is the surest way to make him leave. You have to leave him alone <b>and</b> stay reachable: those are not the same thing." },
        {},
      ],
      pourquoi: "« Parfait. Je suis là si vous avez besoin. » — eight words, and you left the door open without pushing. <b>Staying visible is not pushing</b>; it is what lets the customer come back to you.",
    },
  },

  // ── 6. Le relais. Le geste le plus difficile. ────────────────────────────
  {
    id:   'le-relais',
    type: 'verif',
    eye:  'Le geste le plus dur',
    menu: 'Le relais',
    titre: "Vous avez fait répéter deux fois. Vous ne comprenez toujours pas.",
    consigne: "Écoutez le client, puis choisissez.",
    sons: [
      { fichier: 'c1.mp3', qui: 'Le client',
        texte: "Pis là, je voudrais savoir si je peux l'échanger si jamais ça fait pas, parce que c'est pour un cadeau, faque il faudrait que ça soit possible." },
    ],
    options: [
      { txt: "Vous répondez «&nbsp;oui&nbsp;» — ça a l'air d'être une question à laquelle on répond oui.",
        rat_t: "C'est la faute du premier écran, en plus grave.",
        rat: "Vous venez de promettre un échange sans connaître la politique du magasin. Si elle est de quinze jours et qu'il revient le vingtième, c'est <b>votre gérante</b> qui devra tenir votre promesse — ou dire non à votre place." },
      { txt: "Vous dites que vous ne comprenez pas, et vous attendez.",
        rat_t: "C'est honnête, et ça s'arrête à mi-chemin.",
        rat: "Le client, lui, ne sait pas quoi faire de cette phrase. Il va la répéter, plus fort ou plus vite, et vous serez au même point. Dire qu'on ne comprend pas ne suffit pas&nbsp;: <b>il faut proposer la suite</b>." },
      { txt: "«&nbsp;Un instant, s'il vous plaît. Je vais chercher ma collègue.&nbsp;»", juste: true },
    ],
    pourquoi: "Passer le relais est le geste qui se sent comme un aveu, et qui n'en est pas un. <b>C'est le seul qui garde le client dans le magasin.</b> Deviner le fait sortir avec une fausse réponse&nbsp;; s'excuser le fait sortir tout court.",
    attente: "Choisissez une réponse pour continuer.",
    es: {
      attente: "Elija una respuesta para continuar.",
      titre: "Ya hizo repetir dos veces. Sigue sin entender.",
      consigne: "Escuche al cliente y elija.",
      options: [
        { rat_t: "Es el error de la primera pantalla, pero más grave.",
          rat: "Acaba de prometer un cambio sin conocer la política de la tienda. Si es de quince días y él vuelve el vigésimo, será <b>su gerente</b> quien tenga que cumplir su promesa — o decir que no en su lugar." },
        { rat_t: "Es honesto, y se queda a mitad de camino.",
          rat: "El cliente no sabe qué hacer con esa frase. La va a repetir, más fuerte o más rápido, y usted estará igual. Decir que no se entiende no basta: <b>hay que proponer lo que sigue</b>." },
        {},
      ],
      pourquoi: "Pasar el relevo es el gesto que se siente como una confesión, y no lo es. <b>Es el único que mantiene al cliente en la tienda.</b> Adivinar lo hace salir con una respuesta falsa; disculparse lo hace salir sin más.",
    },
    en: {
      attente: "Choose an answer to continue.",
      titre: "You have asked twice. You still do not understand.",
      consigne: "Listen to the customer, then choose.",
      options: [
        { rat_t: "It is the first screen's mistake, only worse.",
          rat: "You have just promised an exchange without knowing the shop's policy. If it is fifteen days and he comes back on the twentieth, <b>your manager</b> has to keep your promise — or say no on your behalf." },
        { rat_t: "It is honest, and it stops halfway.",
          rat: "The customer does not know what to do with that sentence. He will repeat it, louder or faster, and you will be no further ahead. Saying you do not understand is not enough: <b>you have to offer the next step</b>." },
        {},
      ],
      pourquoi: "Handing over feels like an admission, and it is not one. <b>It is the only move that keeps the customer in the shop.</b> Guessing sends him out with a wrong answer; apologising just sends him out.",
    },
  },

  // ── 7. Ce que la gérante en pense. Lever l'objection. ────────────────────
  {
    id:   'chantal',
    type: 'notion',
    eye:  "Ce que la gérante en pense",
    menu: 'La gérante',
    titre: "«&nbsp;Je vais chercher ma collègue&nbsp;» n'est pas un aveu.",
    paras: [
      "C'est l'objection qui arrête tout le monde&nbsp;: <i>si je vais chercher quelqu'un, "
      + "on va voir que je ne comprends pas.</i>",

      "Écoutez ce que Chantal répond au client. <b>Elle ne s'excuse pas pour Yasmine.</b> "
      + "Elle répond à la question, et la vente continue.",

      "Une gérante compare deux choses&nbsp;: vingt secondes de son temps, ou un client "
      + "sorti. Et il y a pire qu'un client sorti&nbsp;: un client à qui on a promis un "
      + "échange qui n'existe pas, et qui reviendra le réclamer.",
    ],
    sons: [
      { fichier: 'c2.mp3', qui: 'Yasmine', texte: "Un instant, s'il vous plaît. Je vais chercher ma collègue." },
      { fichier: 'c3.mp3', qui: 'Chantal, gérante', texte: "Bonjour&nbsp;! Oui, vous pouvez l'échanger. Vous avez trente jours, avec la facture." },
    ],
    retenir: "La personne qui va chercher une collègue n'est pas celle qui parle le moins bien français. C'est celle qui fait <b>sortir le moins de clients</b>.",
    attente: "Écoutez, puis continuez.",
    es: {
      attente: "Escuche y continúe.",
      titre: "« Je vais chercher ma collègue » no es una confesión.",
      paras: [
        "Es la objeción que detiene a todo el mundo: <i>si voy a buscar a alguien, van a ver que no entiendo.</i>",
        "Escuche lo que Chantal le responde al cliente. <b>No se disculpa por Yasmine.</b> Responde a la pregunta, y la venta sigue.",
        "Una gerente compara dos cosas: veinte segundos de su tiempo, o un cliente que se va. Y hay algo peor que un cliente que se va: un cliente a quien se le prometió un cambio que no existe, y que volverá a reclamarlo.",
      ],
      retenir: "La persona que va a buscar a una colega no es la que peor habla francés. Es la que hace <b>salir a menos clientes</b>.",
    },
    en: {
      attente: "Listen, then continue.",
      titre: "« Je vais chercher ma collègue » is not an admission.",
      paras: [
        "This is the objection that stops everyone: <i>if I go and get someone, they will see that I do not understand.</i>",
        "Listen to what Chantal says to the customer. <b>She does not apologise for Yasmine.</b> She answers the question, and the sale carries on.",
        "A manager weighs two things: twenty seconds of her time, or a customer out the door. And there is something worse than a customer leaving: a customer who was promised an exchange that does not exist, and who will come back to claim it.",
      ],
      retenir: "The person who fetches a colleague is not the one whose French is worst. They are the one who lets <b>the fewest customers walk out</b>.",
    },
  },

  // ── 8. Ce qu'on emporte, et le défi de la semaine. ───────────────────────
  {
    id:   'dans-la-poche',
    type: 'notion',
    eye:  "Ce que vous emportez",
    menu: 'Dans la poche',
    titre: "Cinq phrases à garder dans la poche du tablier.",
    paras: [
      "<b>1.</b> Un instant, s'il vous plaît.<br>"
      + "<b>2.</b> Vous cherchez quel modèle&nbsp;?<br>"
      + "<b>3.</b> Quelle pointure, s'il vous plaît&nbsp;?<br>"
      + "<b>4.</b> Je vais voir en réserve. Je reviens tout de suite.<br>"
      + "<b>5.</b> Un instant. Je vais chercher ma collègue.",

      "Aucune de ces phrases n'est difficile. Vous les connaissiez déjà presque toutes. "
      + "<b>Ce bloc ne vous a pas appris des mots&nbsp;: il vous a donné la permission de "
      + "les dire.</b>",

      "<b>Le défi de la semaine.</b> Une seule chose, d'ici le prochain bloc&nbsp;: "
      + "<b>dites une fois «&nbsp;un instant, s'il vous plaît&nbsp;» à un client qui parle "
      + "trop vite.</b> Une seule fois. Votre gérante le note sur sa fiche.",
    ],
    retenir: "Un client arrêté poliment reste. Un client à qui on a dit «&nbsp;oui&nbsp;» sort, et personne ne le compte.",
    attente: "Lisez, puis terminez le bloc.",
    es: {
      attente: "Lea y termine el bloque.",
      titre: "Cinco frases para guardar en el bolsillo del delantal.",
      paras: [
        "Las cinco frases quedan en francés: son exactamente lo que hay que decir en el piso de venta.",
        "Ninguna de estas frases es difícil. Usted ya conocía casi todas. <b>Este bloque no le enseñó palabras: le dio permiso para decirlas.</b>",
        "<b>El desafío de la semana.</b> Una sola cosa, antes del próximo bloque: <b>diga una vez « un instant, s'il vous plaît » a un cliente que habla demasiado rápido.</b> Una sola vez. Su gerente lo anota en su ficha.",
      ],
      retenir: "Un cliente detenido con cortesía se queda. Un cliente a quien se le dijo « oui » se va, y nadie lo cuenta.",
    },
    en: {
      attente: "Read, then finish the block.",
      titre: "Five sentences to keep in your apron pocket.",
      paras: [
        "The five sentences stay in French: they are exactly what you have to say on the floor.",
        "None of these sentences is hard. You already knew almost all of them. <b>This block did not teach you words: it gave you permission to say them.</b>",
        "<b>The challenge of the week.</b> One single thing, before the next block: <b>say « un instant, s'il vous plaît » once, to a customer who is talking too fast.</b> Just once. Your manager ticks it on her sheet.",
      ],
      retenir: "A customer stopped politely stays. A customer who was told « oui » walks out, and nobody counts him.",
    },
  },

];
