const CARRIER_PHRASES = {
  // Une phrase porteuse par mot isolé à prononcer. Un mot envoyé seul à la
  // synthèse sort mal accentué ; la phrase le remet dans un contexte
  // français, et seul le mot est découpé.
  //
  // Les clés sont les mots **accentués**, tels qu'ils paraissent dans les
  // listes savoir[…][2] de exos.js — jamais en slug, sans quoi la pastille
  // lirait le mot seul sans que rien ne le signale, et cela ne s'entendrait
  // qu'une fois les MP3 payés.
  //
  // Seize clés pour seize pastilles, une par mot du banc de vocabulaire :
  // les quatre bandeaux `speak:true` du module sont ceux des quatre
  // exercices « Vrai ou Faux » — un par section.
  //
  // Les cartes de `prChiffres` (`cards:true listen:true`) n'ont pas de clé
  // ici, et c'est normal : pour ce type d'exercice, le moteur lit le texte
  // de la rangée et non une phrase porteuse.

  // ── Je découvre : ce que dit le papier ──
  "un relevé de compte":  "Le relevé de compte est arrivé par la poste comme les autres mois.",
  "le solde":             "Le solde n'avait baissé que de quatre cents dollars en un an.",
  "le paiement minimum":  "Le paiement minimum garde le compte en règle, rien de plus.",
  "les frais de crédit":  "Les frais de crédit se calculent chaque jour sur ce qui reste dû.",

  // ── Défi 1 : les mots de l'emprunt ──
  "le taux d'intérêt":    "Le taux d'intérêt de la marge est de neuf et quarante-cinq.",
  "une marge de crédit":  "Une marge de crédit ne coûte rien tant qu'on n'y touche pas.",
  "un prêt personnel":    "Un prêt personnel se termine à la date écrite au contrat.",
  "la cote de crédit":    "La cote de crédit décide du taux qu'on vous offrira.",

  // ── Défi 2 : les mots de l'épargne ──
  "un placement":         "Un placement garanti à douze pour cent, ça n'existe pas.",
  "le rendement":         "Le rendement du dépôt à terme est connu dès le premier jour.",
  "un dépôt à terme":     "Elle a choisi un dépôt à terme de deux ans pour le cégep.",
  "l'assurance-dépôts":   "L'assurance-dépôts s'applique toute seule, sans rien demander.",

  // ── Défi 3 : les mots de la contestation ──
  "une opération non autorisée": "Une opération non autorisée se signale le jour même.",
  "une contestation":     "La contestation a été ouverte pendant l'appel de onze heures.",
  "l'hameçonnage":        "L'hameçonnage imite une institution pour vous faire écrire un numéro.",
  "un numéro de dossier": "Sans numéro de dossier, il faut tout raconter une deuxième fois.",
};
