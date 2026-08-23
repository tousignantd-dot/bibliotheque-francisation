const CARRIER_PHRASES = {
  // Une phrase porteuse par mot isolé à prononcer. Un mot envoyé seul à la
  // synthèse sort mal accentué — et plusieurs de ceux-ci existent aussi en
  // anglais (« normal », « palier », « concession », « témoin ») : la phrase
  // les remet dans un contexte français, et seul le mot est découpé.
  //
  // Les clés sont les mots **accentués**, tels qu'ils paraissent dans les
  // listes savoir[…][2] de exos.js — jamais en slug, sans quoi la pastille
  // lirait le mot seul sans que rien ne le signale.
  //
  // Seize clés pour dix-huit pastilles : « un palier » et « un registre des
  // bruits » paraissent chacun dans deux bandeaux et ne prennent qu'une
  // phrase.

  // ── Je découvre : nommer ce qui arrive ──
  "un trouble de voisinage": "Quinze matins de suite, cela devient un trouble de voisinage.",
  "une nuisance sonore": "Le règlement de la ville appelle cela une nuisance sonore.",
  "la jouissance paisible": "Le bail promet à la locataire la jouissance paisible des lieux.",
  "un inconvénient normal": "Des pas à sept heures du soir restent un inconvénient normal.",

  // ── Défi 1 : la conversation sur le palier ──
  "un palier": "La conversation s'est tenue debout sur un palier.",
  "un arrangement à l'amiable": "Les deux voisins ont trouvé un arrangement à l'amiable.",
  "une concession": "Descendre le vélo à l'épaule était une concession.",
  "un reproche": "Elle est montée avec des dates plutôt qu'avec un reproche.",

  // ── Défi 2 : la preuve et l'arbitrage ──
  "un registre des bruits": "Elle tient un registre des bruits depuis le quatre février.",
  "un témoin": "La voisine du deux est devenue un témoin ce matin-là.",
  "la médiation citoyenne": "Le quartier offre gratuitement la médiation citoyenne.",
  "le règlement municipal": "Le règlement municipal découpe la journée en trois périodes.",

  // ── Défi 3 : l'écrit qui règle ──
  "une mise en demeure": "Elle a posté une mise en demeure le vingt mars.",
  "un délai raisonnable": "Dix jours passent pour un délai raisonnable.",
  "un courrier recommandé": "La lettre est partie par courrier recommandé.",
  "une diminution de loyer": "Elle ne demande pas une diminution de loyer.",
};
