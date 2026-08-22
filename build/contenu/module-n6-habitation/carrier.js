const CARRIER_PHRASES = {
  // Une phrase porteuse par mot isolé à prononcer. Un mot envoyé seul à la
  // synthèse sort mal accentué, et parfois lu à l'anglaise — « un short » et
  // « le shampoing » en sont deux candidats évidents. La phrase le remet dans
  // un contexte français ; seul le mot est découpé.
  //
  // Les clés sont les mots **accentués**, tels qu'ils paraissent dans les
  // listes savoir[…][2] de exos.js. Une clé écrite en slug ne serait jamais
  // trouvée, et la pastille lirait le mot seul sans que rien ne le signale.

  // ── Les pastilles des bandeaux de savoir (les seize mots du module) ──
  'un entrepreneur général':  "L'entrepreneur général fait venir chaque métier au bon moment.",
  'une soumission':           "La soumission tient sur deux pages et se lit ligne par ligne.",
  'un corps de métier':       "Quatre corps de métier vont se suivre dans le sous-sol.",
  'un permis de rénovation':  "Le permis de rénovation a pris dix jours ouvrables.",

  'la fondation':             "La fondation du côté nord a fendu sur un mètre.",
  'une fissure':              "La fissure monte en biais derrière l'étagère.",
  'une descente de gouttière': "La descente de gouttière se vide au pied du mur.",
  'la pente du terrain':      "On refait la pente du terrain sur deux mètres.",

  "un rapport d'inspection":  "Le rapport d'inspection compte onze pages.",
  "le taux d'humidité":       "Le taux d'humidité du mur nord est de dix-neuf pour cent.",
  'les exclusions':           "Les exclusions sont écrites en bas de la deuxième page.",
  'un échéancier':            "L'échéancier prévoit six semaines, séchage compris.",

  'une dalle de béton':       "La dalle de béton a été coulée en 1961.",
  'une membrane':             "Une membrane se pose avant les fourrures et le revêtement.",
  'un imprévu':               "Le puisard condamné est un imprévu au sens de la soumission.",
  'un acompte':               "L'acompte de trente pour cent se verse à la signature.",

  // ── Les mots de l'exercice de graphie-phonie ────────────────────────
  // Le pilote du niveau 6 l'a vérifié : pour un `vf` à cards + listen, le
  // relevé de `build/releve_sons.js` rend le **texte de la rangée**, pas la
  // phrase porteuse. Les douze clés ci-dessous ne sont donc pas lues par le
  // moteur — elles restent ici parce qu'elles disent au lecteur dans quel
  // sens le mot doit s'entendre, et parce que le générateur audio, lui, passe
  // ces mots par `enrichir()` de `build/voix.py` pour la même raison :
  // « un short » et « le shampoing » existent en anglais et sortiraient à
  // l'anglaise sans contexte français. `node build/coherence.js` ne compte pas
  // une clé inutilisée comme un écart, et il a raison.
  'un architecte':            "Un architecte a signé le plan modifié.",
  'la technique':             "La technique d'injection se fait sous pression.",
  'le chlore':                "Le chlore sert à désinfecter le puisard.",
  'une orchidée':             "Une orchidée est posée sur le rebord de la fenêtre.",
  'dix':                      "Le permis prend dix jours ouvrables.",
  'six':                      "Le chantier dure six semaines.",
  'soixante':                 "La gouttière se vide à soixante centimètres du mur.",
  'Bruxelles':                "Sa cousine habite Bruxelles depuis quinze ans.",
  'un schéma':                "Le rapport était accompagné d'un schéma très clair.",
  'le shampoing':             "Le shampoing à tapis ne règle rien à l'humidité.",
  'le schiste':               "Le schiste est une pierre qui se fend en feuillets.",
  'un short':                 "Un short n'est pas une tenue de chantier.",
};
