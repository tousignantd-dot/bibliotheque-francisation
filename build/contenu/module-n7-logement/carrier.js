const CARRIER_PHRASES = {
  // Une phrase porteuse par mot isolé à prononcer. Un mot envoyé seul à la
  // synthèse sort mal accentué ; la phrase le remet dans un contexte
  // français, et seul le mot est découpé.
  //
  // Les clés sont les mots **accentués**, tels qu'ils paraissent dans les
  // listes savoir[…][2] de exos.js — jamais en slug, sans quoi la pastille
  // lirait le mot seul sans que rien ne le signale.
  //
  // Dix-neuf clés pour vingt et une pastilles : « un compromis » et « une
  // contrepartie » paraissent dans deux bandeaux (Je découvre et Défi 1) et
  // ne prennent qu'une phrase chacun.

  // ── Je découvre : les mots de l'avis reçu ──
  'un avis de modification': "L'avis de modification était coincé dans la porte, sans enveloppe.",
  'une hausse de loyer':     "La hausse de loyer demandée est de quatre-vingt-quatre dollars par mois.",
  'un délai de réponse':     "Le délai de réponse est d'un mois à partir de la réception.",
  'la fixation du loyer':    "Faute d'entente, le locateur demande la fixation du loyer au Tribunal.",
  'une contrepartie':        "La fenêtre changée avant l'hiver était sa contrepartie.",
  'un compromis':            "Cinquante-cinq dollars et un vitrier en septembre : le compromis tenait.",

  // ── Défi 1 : les mots de la négociation ──
  'une contre-proposition':  "Sa contre-proposition tenait en deux points, un chiffre et une date.",
  'une entente écrite':      "Deux lignes et des initiales suffisent à faire une entente écrite.",
  'les travaux d\'entretien': "Les travaux d'entretien restent à la charge du propriétaire.",

  // ── Défi 2 : les mots de la visite ──
  'un courtier immobilier':  "Le courtier immobilier du vendeur ne représente pas l'acheteur.",
  'un contrat de courtage':  "Sa rétribution est fixée dans le contrat de courtage signé par le vendeur.",
  'les frais de copropriété': "Les frais de copropriété sont de cent quatre-vingt-dix dollars par mois.",
  'le fonds de prévoyance':  "Demandez toujours ce qu'il y a dans le fonds de prévoyance.",
  'une fiche descriptive':   "La fiche descriptive donne l'année de construction et les frais mensuels.",

  // ── Défi 3 : les mots de l'achat ──
  'une promesse d\'achat':    "Une fois acceptée, la promesse d'achat engage les deux parties.",
  'la mise de fonds':        "Sous cinq cent mille dollars, la mise de fonds minimale est de cinq pour cent.",
  'une préautorisation':     "Elle est allée chercher une préautorisation avant de faire une offre.",
  'une inspection préachat': "L'inspection préachat n'est pas obligatoire, mais y renoncer coûte cher.",
  'les droits de mutation':  "Les droits de mutation arrivent quelques mois après l'achat.",
};
