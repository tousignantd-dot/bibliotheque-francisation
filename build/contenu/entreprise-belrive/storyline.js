// ═══════════════════════════════════════════════════════════════════════════
// BLOC 3 — « Je n'ai pas compris »
// Démonstration entreprise · Aliments Belrive inc. (usine fictive)
//
// Le troisième des huit blocs d'une heure. C'est celui qu'on montre en premier
// à un employeur : si l'on ne devait payer qu'une heure, ce serait celle-là.
// Un travailleur qui répond « oui, oui » sans avoir compris coûte plus cher
// qu'un travailleur qui ne parle pas — parce que personne ne s'en aperçoit.
//
// ── Ce que le bloc enseigne ────────────────────────────────────────────────
// Quatre gestes, et un cinquième plus difficile :
//   1. ARRÊTER          « Attendez, s'il vous plaît. »
//   2. FAIRE RALENTIR   « Vous parlez trop vite pour moi. Répétez lentement ? »
//   3. FAIRE MONTRER    « Montrez-moi, s'il vous plaît. »
//   4. REDIRE           « Je vide la palette deux, et j'apporte les étiquettes. »
//   5. DIRE NON         « Je n'aurai pas le temps avant la pause. »
//
// Ce n'est pas du vocabulaire : c'est un comportement. D'où le défi de la
// semaine à l'écran 8 — la seule pièce qui produise du Kirkpatrick niveau 3.
//
// ── La langue d'appui ──────────────────────────────────────────────────────
// `appui: [es, en]`. Chaque écran porte un objet `es` et un objet `en` qui ne
// contiennent QUE l'appui : consigne, explication, rattrapage. Les phrases
// françaises — les options, les extraits, la fiche de poche — ne basculent
// jamais. Le moteur pose l'appui SOUS le français, jamais à sa place.
//
// ── Les extraits ───────────────────────────────────────────────────────────
// Produits pour ce bloc, dans `assets/interactive/entreprise-belrive/`.
// Jean-Guy parle au débit normal d'Azure — c'est-à-dire vite ; Nadia et
// Marie-Ève sont ralenties. Le contraste EST la leçon : on n'a pas besoin
// d'écrire que le superviseur parle trop vite, on le fait entendre.
// ═══════════════════════════════════════════════════════════════════════════

const PARCOURS = {
  slug:     'belrive-bloc3',
  module:   'entreprise-belrive',
  titre:    "Je n'ai pas compris",
  surtitre: "Aliments Belrive · Bloc 3 sur 8",
  niveau:   2,
  appui: [
    { c: 'es', n: 'Español' },
    { c: 'en', n: 'English' },
  ],
};

const ECRANS = [

  // ── 1. LE MOMENT. On tranche avant d'avoir rien appris. ──────────────────
  {
    id:   'oui-oui',
    type: 'verif',
    eye:  'Le moment',
    menu: '« Oui, oui »',
    titre: "Nadia a dit «&nbsp;oui, oui&nbsp;». Que va-t-il arriver&nbsp;?",
    consigne: "Écoutez les trois extraits, puis répondez avec ce que vous savez déjà.",
    images: [
      { fichier: 'images/palette.jpg',
        alt: "Une palette de caisses de plastique grises, dans l'allée d'une usine "
           + "de conditionnement de légumes.",
        leg: "La palette numéro deux, dans l'allée d'emballage." },
    ],
    sons: [
      { fichier: 'a1.mp3', qui: 'Jean-Guy, superviseur',
        texte: "Nadia&nbsp;! La deux est pleine, tu la vides pis tu m'apportes les étiquettes du lot d'hier avant la pause." },
      { fichier: 'a2.mp3', qui: 'Nadia',
        texte: "Oui, oui." },
      { fichier: 'a3.mp3', qui: 'Marie-Ève, chef d\'équipe, vingt minutes plus tard',
        texte: "Nadia… ce ne sont pas les étiquettes d'hier, ça. Et la palette est encore pleine." },
    ],
    options: [
      { txt: "Nadia va faire le travail correctement.",
        rat_t: "Écoutez le troisième extrait encore une fois.",
        rat: "La palette est encore pleine, et les étiquettes ne sont pas les bonnes. Deux tâches sur deux&nbsp;: ratées." },
      { txt: "Le travail va être à recommencer, et personne ne saura pourquoi.", juste: true },
      { txt: "Jean-Guy va s'apercevoir que Nadia n'a pas compris.",
        rat_t: "C'est justement ce qui n'arrive jamais.",
        rat: "Jean-Guy est déjà reparti. Il a entendu «&nbsp;oui, oui&nbsp;» et il est passé à autre chose. C'est vingt minutes plus tard que le problème apparaît — et à ce moment-là, il ressemble à une faute de Nadia." },
    ],
    pourquoi: "«&nbsp;Oui, oui&nbsp;» est la réponse la plus coûteuse de l'usine. Elle ne coûte rien à dire, et elle coûte une heure de travail à quelqu'un d'autre.",
    attente: "Choisissez une réponse pour continuer.",
    es: {
      images: [{ leg: "La paleta número dos, en el pasillo de empaque." }],
      attente: "Elija una respuesta para continuar.",
      titre: "Nadia dijo « oui, oui ». ¿Qué va a pasar?",
      consigne: "Escuche los tres audios y responda con lo que ya sabe.",
      options: [
        { rat_t: "Escuche otra vez el tercer audio.",
          rat: "La paleta sigue llena y las etiquetas no son las correctas. Dos tareas de dos: falladas." },
        {},
        { rat_t: "Eso es precisamente lo que nunca pasa.",
          rat: "Jean-Guy ya se fue. Oyó « oui, oui » y siguió con otra cosa. El problema aparece veinte minutos después — y para entonces parece un error de Nadia." },
      ],
      pourquoi: "« Oui, oui » es la respuesta más cara de la fábrica. No cuesta nada decirla, y le cuesta una hora de trabajo a otra persona.",
    },
    en: {
      images: [{ leg: "Pallet number two, in the packing aisle." }],
      attente: "Choose an answer to continue.",
      titre: "Nadia said « oui, oui ». What is going to happen?",
      consigne: "Listen to the three clips, then answer with what you already know.",
      options: [
        { rat_t: "Listen to the third clip again.",
          rat: "The pallet is still full and the labels are the wrong ones. Two tasks out of two: missed." },
        {},
        { rat_t: "That is exactly what never happens.",
          rat: "Jean-Guy has already walked away. He heard « oui, oui » and moved on. The problem shows up twenty minutes later — and by then it looks like Nadia's mistake." },
      ],
      pourquoi: "« Oui, oui » is the most expensive answer in the plant. It costs nothing to say, and it costs someone else an hour of work.",
    },
  },

  // ── 2. Le vrai problème n'est pas le vocabulaire. ────────────────────────
  {
    id:   'trois-choses',
    type: 'notion',
    eye:  "Ce qui s'est vraiment passé",
    menu: 'Trois choses',
    titre: "Jean-Guy a demandé trois choses en huit secondes.",
    paras: [
      "Réécoutez-le. Il n'a pas été impoli, il n'a pas parlé un français difficile&nbsp;: "
      + "il a dit <b>trois choses d'affilée</b>, vite, en marchant.",

      "<b>1.</b> Vider la palette numéro deux. <b>2.</b> Apporter les étiquettes du lot d'hier. "
      + "<b>3.</b> Avant la pause.",

      "Le problème n'est pas le vocabulaire de Nadia. Elle connaît «&nbsp;palette&nbsp;», elle "
      + "connaît «&nbsp;pause&nbsp;». Le problème, c'est <b>la vitesse et le nombre</b>. "
      + "Personne ne retient trois consignes dans une langue qu'il apprend, à huit secondes.",
    ],
    sons: [
      { fichier: 'a1.mp3', qui: 'Jean-Guy, superviseur',
        texte: "Nadia&nbsp;! La deux est pleine, tu la vides pis tu m'apportes les étiquettes du lot d'hier avant la pause." },
    ],
    retenir: "Vous n'avez pas à apprendre plus de mots pour régler ça. Vous avez à <b>arrêter Jean-Guy</b>.",
    attente: "Écoutez l'extrait, puis continuez.",
    es: {
      attente: "Escuche el audio y continúe.",
      titre: "Jean-Guy pidió tres cosas en ocho segundos.",
      paras: [
        "Vuelva a escucharlo. No fue grosero ni habló un francés difícil: dijo <b>tres cosas seguidas</b>, rápido, mientras caminaba.",
        "<b>1.</b> Vaciar la paleta número dos. <b>2.</b> Traer las etiquetas del lote de ayer. <b>3.</b> Antes de la pausa.",
        "El problema no es el vocabulario de Nadia. Ella conoce « palette », conoce « pause ». El problema es <b>la velocidad y la cantidad</b>. Nadie retiene tres instrucciones en un idioma que está aprendiendo, en ocho segundos.",
      ],
      retenir: "No necesita aprender más palabras para resolver esto. Necesita <b>detener a Jean-Guy</b>.",
    },
    en: {
      attente: "Listen to the clip, then continue.",
      titre: "Jean-Guy asked for three things in eight seconds.",
      paras: [
        "Listen again. He was not rude, and his French was not difficult: he said <b>three things in a row</b>, fast, while walking.",
        "<b>1.</b> Empty pallet number two. <b>2.</b> Bring the labels from yesterday's lot. <b>3.</b> Before the break.",
        "The problem is not Nadia's vocabulary. She knows « palette », she knows « pause ». The problem is <b>speed and number</b>. Nobody holds three instructions in a language they are learning, in eight seconds.",
      ],
      retenir: "You do not need more words to fix this. You need to <b>stop Jean-Guy</b>.",
    },
  },

  // ── 3. La reprise, en entier. Les quatre gestes. ─────────────────────────
  {
    id:   'quatre-gestes',
    type: 'notion',
    eye:  'La même scène, autrement',
    menu: 'Quatre gestes',
    titre: "Voici la même scène, avec quatre gestes de plus.",
    paras: [
      "Rien n'a changé chez Jean-Guy&nbsp;: il parle aussi vite. C'est Nadia qui fait quatre choses.",

      "<b>1. Arrêter</b> — «&nbsp;Attendez, s'il vous plaît.&nbsp;» "
      + "<b>2. Faire ralentir</b> — «&nbsp;Vous parlez trop vite pour moi. Répétez lentement&nbsp;?&nbsp;» "
      + "<b>3. Faire montrer</b> — «&nbsp;Montrez-moi, s'il vous plaît.&nbsp;» "
      + "<b>4. Redire</b> — elle répète la consigne dans ses mots.",

      "Écoutez la fin&nbsp;: Jean-Guy dit «&nbsp;c'est ça, parfait&nbsp;». <b>Il n'est pas fâché.</b> "
      + "Un superviseur préfère toujours vingt secondes de plus à une palette à refaire.",
    ],
    images: [
      { fichier: 'images/chemise-jaune.jpg',
        alt: "Une chemise cartonnée jaune, fermée, sur un plan de travail en acier "
           + "inoxydable.",
        leg: "«&nbsp;Celles-là. Dans la chemise jaune.&nbsp;» &mdash; c'est ce que "
           + "Nadia obtient en disant «&nbsp;montrez-moi&nbsp;»." },
    ],
    sons: [
      { fichier: 'b1.mp3', qui: 'Jean-Guy', texte: "Nadia&nbsp;! La deux est pleine, tu la vides pis tu m'apportes les étiquettes du lot d'hier avant la pause." },
      { fichier: 'b2.mp3', qui: 'Nadia — elle arrête', texte: "Attendez, s'il vous plaît. Vous parlez trop vite pour moi. Répétez lentement&nbsp;?" },
      { fichier: 'b3.mp3', qui: 'Jean-Guy', texte: "OK. La palette numéro deux. Tu la vides." },
      { fichier: 'b4.mp3', qui: 'Nadia — elle redit', texte: "Je vide la palette deux. Après&nbsp;?" },
      { fichier: 'b5.mp3', qui: 'Jean-Guy', texte: "Après, tu m'apportes les étiquettes du lot d'hier. Avant la pause." },
      { fichier: 'b6.mp3', qui: 'Nadia — elle fait montrer', texte: "Les étiquettes… Montrez-moi, s'il vous plaît." },
      { fichier: 'b7.mp3', qui: 'Jean-Guy', texte: "Celles-là. Dans la chemise jaune." },
      { fichier: 'b8.mp3', qui: 'Nadia — elle redit tout', texte: "Je vide la palette deux, et j'apporte les étiquettes jaunes avant la pause." },
      { fichier: 'b9.mp3', qui: 'Jean-Guy', texte: "C'est ça. Parfait." },
    ],
    retenir: "Vingt secondes de plus au début. Une heure de moins à la fin.",
    attente: "Écoutez au moins un extrait, puis continuez.",
    es: {
      images: [{ leg: "« Celles-là. Dans la chemise jaune. » — es lo que Nadia obtiene al decir « montrez-moi »." }],
      attente: "Escuche al menos un audio y continúe.",
      titre: "Aquí está la misma escena, con cuatro gestos más.",
      paras: [
        "Nada cambió en Jean-Guy: habla igual de rápido. Es Nadia quien hace cuatro cosas.",
        "<b>1. Detener</b> — « Attendez, s'il vous plaît. » <b>2. Hacer hablar más lento</b> — « Vous parlez trop vite pour moi. Répétez lentement ? » <b>3. Hacer mostrar</b> — « Montrez-moi, s'il vous plaît. » <b>4. Repetir</b> — ella repite la instrucción con sus palabras.",
        "Escuche el final: Jean-Guy dice « c'est ça, parfait ». <b>No está enojado.</b> Un supervisor siempre prefiere veinte segundos más que una paleta que hay que rehacer.",
      ],
      retenir: "Veinte segundos más al principio. Una hora menos al final.",
    },
    en: {
      images: [{ leg: "« Celles-là. Dans la chemise jaune. » — that is what Nadia gets by saying « montrez-moi »." }],
      attente: "Listen to at least one clip, then continue.",
      titre: "Here is the same scene, with four extra moves.",
      paras: [
        "Nothing changed about Jean-Guy: he still talks fast. It is Nadia who does four things.",
        "<b>1. Stop him</b> — « Attendez, s'il vous plaît. » <b>2. Slow him down</b> — « Vous parlez trop vite pour moi. Répétez lentement ? » <b>3. Make him show you</b> — « Montrez-moi, s'il vous plaît. » <b>4. Say it back</b> — she repeats the instruction in her own words.",
        "Listen to the end: Jean-Guy says « c'est ça, parfait ». <b>He is not annoyed.</b> A supervisor will always take twenty extra seconds over a pallet that has to be redone.",
      ],
      retenir: "Twenty seconds more at the start. One hour less at the end.",
    },
  },

  // ── 4. Le tri : ce qui arrête sans nuire. ────────────────────────────────
  {
    id:   'poli-ou-pas',
    type: 'tri',
    eye:  'À vous de trancher',
    menu: 'Huit phrases',
    titre: "Huit phrases pour arrêter quelqu'un. Lesquelles vous aident&nbsp;?",
    consigne: "Toutes se disent en français. Mais dans une usine, devant un superviseur pressé, "
            + "elles n'ont pas le même effet.",
    colonnes: [
      { id: 'aide',  t: 'Ça vous aide',   b: 'Ça vous aide' },
      { id: 'nuit',  t: 'Ça vous nuit',   b: 'Ça vous nuit' },
    ],
    items: [
      { txt: "Attendez, s'il vous plaît.", ok: 'aide',
        rat: "C'est la phrase la plus utile du bloc. Trois mots, polie, et elle arrête n'importe qui.",
        pourquoi: "Attendez, s'il vous plaît. — elle arrête sans vexer." },
      { txt: "Oui, oui.", ok: 'nuit',
        rat: "Elle vous nuit deux fois&nbsp;: le travail sera à refaire, et Jean-Guy croira que vous aviez compris.",
        pourquoi: "« Oui, oui » — la réponse qui coûte le plus cher." },
      { txt: "Vous parlez trop vite pour moi.", ok: 'aide',
        rat: "Elle dit la vérité sans accuser personne. «&nbsp;Pour moi&nbsp;» change tout&nbsp;: ce n'est pas un reproche.",
        pourquoi: "Vous parlez trop vite pour moi. — vrai, et sans reproche." },
      { txt: "Hein&nbsp;?", ok: 'nuit',
        rat: "Elle se dit entre collègues, mais elle sonne sec, et surtout elle ne demande rien de précis&nbsp;: Jean-Guy va répéter à la même vitesse.",
        pourquoi: "« Hein ? » — sec, et Jean-Guy répétera aussi vite." },
      { txt: "Répétez lentement, s'il vous plaît.", ok: 'aide',
        rat: "Elle demande une chose précise. C'est ce qui la rend efficace&nbsp;: on sait quoi faire pour vous aider.",
        pourquoi: "Répétez lentement, s'il vous plaît. — une demande précise." },
      { txt: "Je comprends pas rien.", ok: 'nuit',
        rat: "La phrase est fautive, mais ce n'est pas le pire&nbsp;: elle ne dit pas <i>quoi</i> vous n'avez pas compris. Dites plutôt&nbsp;: «&nbsp;Je n'ai pas compris la deuxième chose.&nbsp;»",
        pourquoi: "Dites plutôt : « Je n'ai pas compris la deuxième chose. »" },
      { txt: "Montrez-moi, s'il vous plaît.", ok: 'aide',
        rat: "Le geste remplace vingt mots. Dans une usine, c'est souvent la demande la plus rapide.",
        pourquoi: "Montrez-moi, s'il vous plaît. — le geste vaut vingt mots." },
      { txt: "Excusez-moi de vous déranger, je suis vraiment désolée, mais…", ok: 'nuit',
        rat: "Trop long. Le temps de finir la phrase, Jean-Guy est reparti. La politesse tient dans «&nbsp;s'il vous plaît&nbsp;».",
        pourquoi: "Trop long : Jean-Guy sera reparti avant la fin." },
    ],
    attente: "Rangez les huit phrases pour continuer.",
    es: {
      attente: "Clasifique las ocho frases para continuar.",
      titre: "Ocho frases para detener a alguien. ¿Cuáles le ayudan?",
      consigne: "Todas existen en francés. Pero en una fábrica, ante un supervisor apurado, no tienen el mismo efecto.",
      items: [
        { rat: "Es la frase más útil del bloque. Tres palabras, cortés, y detiene a cualquiera." },
        { rat: "Le perjudica dos veces: habrá que rehacer el trabajo, y Jean-Guy creerá que usted había entendido." },
        { rat: "Dice la verdad sin acusar a nadie. « Pour moi » lo cambia todo: no es un reproche." },
        { rat: "Se usa entre compañeros, pero suena seca — y sobre todo no pide nada preciso: Jean-Guy va a repetir a la misma velocidad." },
        { rat: "Pide algo preciso. Eso es lo que la hace eficaz: se sabe qué hacer para ayudarle." },
        { rat: "La frase tiene un error, pero eso no es lo peor: no dice <i>qué</i> no entendió. Diga mejor: « Je n'ai pas compris la deuxième chose. »" },
        { rat: "El gesto reemplaza veinte palabras. En una fábrica suele ser la petición más rápida." },
        { rat: "Demasiado larga. Para cuando termine la frase, Jean-Guy ya se fue. La cortesía cabe en « s'il vous plaît »." },
      ],
    },
    en: {
      attente: "Sort all eight sentences to continue.",
      titre: "Eight ways to stop someone. Which ones help you?",
      consigne: "All of them are real French. But in a plant, in front of a supervisor in a hurry, they do not have the same effect.",
      items: [
        { rat: "The most useful sentence in this block. Three words, polite, and it stops anyone." },
        { rat: "It hurts you twice: the work will have to be redone, and Jean-Guy will believe you understood." },
        { rat: "It tells the truth without blaming anyone. « Pour moi » changes everything: it is not a complaint." },
        { rat: "Coworkers use it, but it sounds blunt — and above all it asks for nothing specific: Jean-Guy will repeat just as fast." },
        { rat: "It asks for one specific thing. That is what makes it work: people know how to help you." },
        { rat: "The sentence is incorrect, but that is not the worst part: it does not say <i>what</i> you missed. Say instead: « Je n'ai pas compris la deuxième chose. »" },
        { rat: "The gesture replaces twenty words. In a plant it is often the fastest thing to ask for." },
        { rat: "Too long. By the time you finish, Jean-Guy is gone. The politeness fits inside « s'il vous plaît »." },
      ],
    },
  },

  // ── 5. Redire : la seule preuve qu'on a compris. ─────────────────────────
  {
    id:   'redire',
    type: 'verif',
    eye: 'Le geste le plus important',
    menu: 'Redire',
    titre: "Jean-Guy vient de tout répéter. Que dites-vous maintenant&nbsp;?",
    consigne: "Une seule de ces réponses prouve à Jean-Guy que vous avez compris.",
    sons: [
      { fichier: 'b5.mp3', qui: 'Jean-Guy',
        texte: "Après, tu m'apportes les étiquettes du lot d'hier. Avant la pause." },
    ],
    options: [
      { txt: "OK, parfait, merci.",
        rat_t: "C'est poli, mais ça ne prouve rien.",
        rat: "«&nbsp;OK&nbsp;» est un autre «&nbsp;oui, oui&nbsp;». Jean-Guy repart avec la même incertitude — sauf qu'il ne le sait pas." },
      { txt: "Je vide la palette deux, et j'apporte les étiquettes jaunes avant la pause.", juste: true },
      { txt: "Oui, j'ai compris, ne vous inquiétez pas.",
        rat_t: "Dire qu'on a compris n'est pas montrer qu'on a compris.",
        rat: "C'est la phrase que dit aussi quelqu'un qui n'a rien compris. <b>Elle ne distingue pas les deux.</b> Redites la consigne&nbsp;: c'est la seule preuve." },
    ],
    pourquoi: "<b>Redire, c'est la seule preuve.</b> Et si vous vous trompez en redisant, Jean-Guy vous corrige tout de suite — pendant que ça ne coûte encore rien.",
    attente: "Choisissez une réponse pour continuer.",
    es: {
      attente: "Elija una respuesta para continuar.",
      titre: "Jean-Guy acaba de repetir todo. ¿Qué dice usted ahora?",
      consigne: "Solo una de estas respuestas le prueba a Jean-Guy que usted entendió.",
      options: [
        { rat_t: "Es cortés, pero no prueba nada.",
          rat: "« OK » es otro « oui, oui ». Jean-Guy se va con la misma incertidumbre — solo que no lo sabe." },
        {},
        { rat_t: "Decir que entendió no es mostrar que entendió.",
          rat: "Es la frase que dice también alguien que no entendió nada. <b>No distingue entre los dos casos.</b> Repita la instrucción: es la única prueba." },
      ],
      pourquoi: "<b>Repetir es la única prueba.</b> Y si se equivoca al repetir, Jean-Guy la corrige enseguida — cuando todavía no cuesta nada.",
    },
    en: {
      attente: "Choose an answer to continue.",
      titre: "Jean-Guy has just repeated everything. What do you say now?",
      consigne: "Only one of these answers proves to Jean-Guy that you understood.",
      options: [
        { rat_t: "Polite, but it proves nothing.",
          rat: "« OK » is another « oui, oui ». Jean-Guy walks away with the same uncertainty — except he does not know it." },
        {},
        { rat_t: "Saying you understood is not showing you understood.",
          rat: "It is the same sentence someone who understood nothing would say. <b>It does not tell the two apart.</b> Say the instruction back: that is the only proof." },
      ],
      pourquoi: "<b>Saying it back is the only proof.</b> And if you get it wrong, Jean-Guy corrects you right away — while it still costs nothing.",
    },
  },

  // ── 6. Un mot inconnu : on ne devine pas, on fait montrer. ───────────────
  {
    id:   'montrez-moi',
    type: 'verif',
    eye: 'Un mot que vous ne connaissez pas',
    menu: 'Montrez-moi',
    titre: "Jean-Guy dit un mot que vous n'avez jamais entendu. Vous faites quoi&nbsp;?",
    consigne: "Il dit&nbsp;: «&nbsp;Va me chercher la <b>jauge</b> dans le cabinet.&nbsp;» Vous ne savez pas ce qu'est une jauge.",
    options: [
      { txt: "Vous allez au cabinet et vous cherchez.",
        rat_t: "Vous allez y passer dix minutes.",
        rat: "Et vous reviendrez peut-être avec le mauvais objet. C'est exactement le scénario du début du bloc, avec un mot de plus." },
      { txt: "Vous demandez à un collègue ce que veut dire «&nbsp;jauge&nbsp;».",
        rat_t: "Ce n'est pas mauvais — mais ce n'est pas le plus rapide.",
        rat: "Votre collègue est peut-être occupé, et il traduira peut-être mal. La personne qui sait exactement ce qu'elle veut est <b>devant vous</b>." },
      { txt: "«&nbsp;Une jauge&nbsp;? Montrez-moi, s'il vous plaît.&nbsp;»", juste: true },
    ],
    pourquoi: "<b>Répétez le mot, puis demandez à voir.</b> En répétant le mot, vous dites précisément où vous êtes bloqué — et vous l'apprenez pour de bon, avec l'objet dans les mains.",
    attente: "Choisissez une réponse pour continuer.",
    es: {
      attente: "Elija una respuesta para continuar.",
      titre: "Jean-Guy dice una palabra que usted nunca oyó. ¿Qué hace?",
      consigne: "Él dice: « Va me chercher la <b>jauge</b> dans le cabinet. » Usted no sabe qué es una « jauge ».",
      options: [
        { rat_t: "Va a perder diez minutos.",
          rat: "Y quizá vuelva con el objeto equivocado. Es exactamente la escena del principio del bloque, con una palabra más." },
        { rat_t: "No está mal — pero no es lo más rápido.",
          rat: "Su compañero puede estar ocupado, y puede traducir mal. La persona que sabe exactamente qué quiere está <b>delante de usted</b>." },
        {},
      ],
      pourquoi: "<b>Repita la palabra y pida ver.</b> Al repetirla, dice exactamente dónde se atascó — y la aprende de verdad, con el objeto en las manos.",
    },
    en: {
      attente: "Choose an answer to continue.",
      titre: "Jean-Guy uses a word you have never heard. What do you do?",
      consigne: "He says: « Va me chercher la <b>jauge</b> dans le cabinet. » You do not know what a « jauge » is.",
      options: [
        { rat_t: "You are about to lose ten minutes.",
          rat: "And you may come back with the wrong object. That is exactly the opening scene of this block, with one more word in it." },
        { rat_t: "Not bad — but not the fastest.",
          rat: "Your coworker may be busy, and may translate it wrong. The person who knows exactly what they want is <b>standing in front of you</b>." },
        {},
      ],
      pourquoi: "<b>Repeat the word, then ask to see it.</b> Repeating it says exactly where you got stuck — and you learn it for good, with the object in your hands.",
    },
  },

  // ── 7. Le geste le plus difficile : dire non. ────────────────────────────
  {
    id:   'pas-le-temps',
    type: 'verif',
    eye: 'Le plus difficile',
    menu: 'Dire non',
    titre: "Vous avez compris — et vous savez que vous n'aurez pas le temps.",
    consigne: "La pause est dans dix minutes. Vider la palette en prend vingt. Écoutez, puis choisissez.",
    sons: [
      { fichier: 'c1.mp3', qui: 'Nadia',
        texte: "Jean-Guy, je n'aurai pas le temps avant la pause. Je peux vous apporter les étiquettes après&nbsp;?" },
    ],
    options: [
      { txt: "Ne rien dire, commencer, et voir ce qui arrive.",
        rat_t: "C'est ce que font presque tous les nouveaux employés.",
        rat: "Et à la pause, la palette est à moitié vide et les étiquettes ne sont pas là. Jean-Guy apprend la mauvaise nouvelle <b>au pire moment</b>&nbsp;: quand il ne peut plus rien organiser." },
      { txt: "Le dire tout de suite, et proposer autre chose.", juste: true },
      { txt: "Demander à un collègue de faire la moitié sans le dire à Jean-Guy.",
        rat_t: "Vous venez de créer un deuxième problème.",
        rat: "Votre collègue a son propre travail, et Jean-Guy pense toujours que la palette sera vide. Deux personnes en retard au lieu d'une." },
    ],
    pourquoi: "Dire non est le geste le plus difficile du bloc, et le plus utile pour l'entreprise&nbsp;: <b>une mauvaise nouvelle dite tôt est une information ; dite tard, c'est un dégât.</b> Et proposer autre chose («&nbsp;je peux vous les apporter après&nbsp;?&nbsp;») fait toute la différence.",
    attente: "Choisissez une réponse pour continuer.",
    es: {
      attente: "Elija una respuesta para continuar.",
      titre: "Usted entendió — y sabe que no le va a alcanzar el tiempo.",
      consigne: "La pausa es en diez minutos. Vaciar la paleta toma veinte. Escuche y elija.",
      options: [
        { rat_t: "Es lo que hacen casi todos los empleados nuevos.",
          rat: "Y en la pausa, la paleta está a medio vaciar y las etiquetas no están. Jean-Guy se entera de la mala noticia <b>en el peor momento</b>: cuando ya no puede organizar nada." },
        {},
        { rat_t: "Acaba de crear un segundo problema.",
          rat: "Su compañero tiene su propio trabajo, y Jean-Guy sigue creyendo que la paleta estará vacía. Dos personas atrasadas en vez de una." },
      ],
      pourquoi: "Decir que no es el gesto más difícil del bloque y el más útil para la empresa: <b>una mala noticia dicha a tiempo es información; dicha tarde, es un daño.</b> Y proponer otra cosa (« je peux vous les apporter après ? ») cambia todo.",
    },
    en: {
      attente: "Choose an answer to continue.",
      titre: "You understood — and you know you will not have time.",
      consigne: "The break is in ten minutes. Emptying the pallet takes twenty. Listen, then choose.",
      options: [
        { rat_t: "This is what almost every new employee does.",
          rat: "And at the break, the pallet is half empty and the labels are not there. Jean-Guy hears the bad news <b>at the worst moment</b>: when he can no longer reorganize anything." },
        {},
        { rat_t: "You have just created a second problem.",
          rat: "Your coworker has their own job, and Jean-Guy still thinks the pallet will be empty. Two people behind instead of one." },
      ],
      pourquoi: "Saying no is the hardest move in this block and the most useful one for the company: <b>bad news said early is information; said late, it is damage.</b> And offering something else (« je peux vous les apporter après ? ») makes all the difference.",
    },
  },

  // ── 8. On emporte. La fiche, et le défi de la semaine. ───────────────────
  {
    id:   'dans-la-poche',
    type: 'notion',
    eye: "Ce que vous emportez",
    menu: 'Dans la poche',
    titre: "Cinq phrases à garder dans la poche du sarrau.",
    paras: [
      "<b>1.</b> Attendez, s'il vous plaît.<br>"
      + "<b>2.</b> Vous parlez trop vite pour moi. Répétez lentement&nbsp;?<br>"
      + "<b>3.</b> Montrez-moi, s'il vous plaît.<br>"
      + "<b>4.</b> Je fais… (redites la consigne dans vos mots)<br>"
      + "<b>5.</b> Je n'aurai pas le temps. Je peux le faire après&nbsp;?",

      "Aucune de ces phrases n'est difficile. Vous les connaissiez déjà presque toutes. "
      + "<b>Ce bloc ne vous a pas appris des mots&nbsp;: il vous a donné la permission de les dire.</b>",

      "<b>Le défi de la semaine.</b> Une seule chose, d'ici le prochain bloc&nbsp;: "
      + "<b>demandez une fois à quelqu'un de répéter plus lentement.</b> Une seule fois. "
      + "Votre chef d'équipe le note sur sa fiche.",
    ],
    images: [
      { fichier: 'images/sarrau.jpg',
        alt: "Un sarrau de travail blanc suspendu à un crochet, une feuille pliée "
           + "dans la poche de poitrine.",
        leg: "La fiche reste dans la poche. C'est le seul endroit où elle sert." },
    ],
    retenir: "La personne qui demande de répéter n'est pas celle qui parle le moins bien français. C'est celle qui coûte le moins cher à l'usine.",
    attente: "Lisez, puis terminez le bloc.",
    es: {
      images: [{ leg: "La ficha se queda en el bolsillo. Es el único lugar donde sirve." }],
      attente: "Lea y termine el bloque.",
      titre: "Cinco frases para guardar en el bolsillo de la bata.",
      paras: [
        "Las cinco frases quedan en francés: son exactamente lo que hay que decir en la planta.",
        "Ninguna de estas frases es difícil. Usted ya conocía casi todas. <b>Este bloque no le enseñó palabras: le dio permiso para decirlas.</b>",
        "<b>El desafío de la semana.</b> Una sola cosa, antes del próximo bloque: <b>pídale una vez a alguien que repita más despacio.</b> Una sola vez. Su jefe de equipo lo anota en su ficha.",
      ],
      retenir: "La persona que pide que le repitan no es la que habla peor francés. Es la que menos le cuesta a la fábrica.",
    },
    en: {
      images: [{ leg: "The card stays in the pocket. It is the only place where it is any use." }],
      attente: "Read, then finish the block.",
      titre: "Five sentences to keep in your coat pocket.",
      paras: [
        "The five sentences stay in French: they are exactly what you have to say on the floor.",
        "None of these sentences is hard. You already knew almost all of them. <b>This block did not teach you words: it gave you permission to say them.</b>",
        "<b>The challenge of the week.</b> One single thing, before the next block: <b>ask someone once to repeat more slowly.</b> Just once. Your team leader ticks it on their sheet.",
      ],
      retenir: "The person who asks you to repeat is not the one whose French is worst. They are the one who costs the plant the least.",
    },
  },

];
