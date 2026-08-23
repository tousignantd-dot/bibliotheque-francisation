const CARRIER_PHRASES = {
  // Les clés sont les mots **accentués**, tels qu'ils paraissent dans la
  // troisième colonne des bandeaux `savoir` de `exos.js`. Une clé écrite en
  // slug n'est jamais trouvée par le gabarit, qui fait `CARRIER_PHRASES[w]`
  // sur le mot affiché — la pastille lirait alors le mot seul, mal prononcé.
  // Le relevé se fait dans les deux sens par `node build/coherence.js
  // module-n8-habitation`, jamais à la main.
  //
  // Seize mots, seize phrases : ce sont exactement les seize cartes de
  // `fccards.js`, chacune reprise dans un bandeau de savoir.
  "un refoulement d'égout": "Le refoulement d'égout a inondé le sous-sol.",
  'un sinistre': "La date du sinistre est le quatorze septembre.",
  'une réclamation': "Sa réclamation porte un numéro à sept chiffres.",
  'un avenant': "L'avenant ajoute une protection au contrat.",
  'une franchise': "La franchise est de mille dollars par sinistre.",
  'un clapet antiretour': "Le clapet antiretour empêche l'eau de revenir.",
  'un expert en sinistre': "L'expert en sinistre est venu deux jours après.",
  'une contre-expertise': "La contre-expertise a duré une heure et demie.",
  'un drain de fondation': "Le drain de fondation évacue l'eau du sol.",
  'un constat': "Le constat dit ce que l'expert a vu de ses yeux.",
  'une exclusion': "L'exclusion est écrite à l'article sept point trois.",
  "le défaut d'entretien": "Le défaut d'entretien est le motif du refus.",
  'une facture acquittée': "Elle a gardé la facture acquittée du nettoyage.",
  'une réponse finale': "La réponse finale arrive par écrit en soixante jours.",
  'un transfert de dossier': "Elle demande le transfert de dossier à l'Autorité.",
  'une décision motivée': "Une décision motivée dit sur quoi elle s'appuie.",
};
