const CARRIER_PHRASES = {
  // Une phrase porteuse par mot isolé à prononcer. Un mot envoyé seul à la
  // synthèse sort mal accentué, et parfois lu à l'anglaise — « un t-shirt »,
  // « un short » et « un shampoing » en sont trois candidats évidents. La
  // phrase le remet dans un contexte français ; seul le mot est découpé.
  //
  // Les clés sont les mots **accentués**, tels qu'ils paraissent dans les
  // listes savoir[…][2] de exos.js. Une clé écrite en slug ne serait jamais
  // trouvée, et la pastille lirait le mot seul sans que rien ne le signale.

  // ── Les pastilles des bandeaux de savoir (les seize mots du module) ──
  'un babillard':            "Le babillard est à côté de la porte du vestiaire.",
  'un affichage interne':    "L'affichage interne reste dix jours ouvrables au mur.",
  'une mutation':            "Ce n'est pas une promotion, c'est une mutation.",
  'une candidature interne': "Elle a déposé sa candidature interne le mardi matin.",

  'les ressources humaines': "Les ressources humaines sont au bureau douze.",
  'un formulaire':           "Le formulaire RH-04 tient sur une seule page.",
  'un comité de sélection':  "Le comité de sélection est formé de deux personnes.",
  "l'ancienneté":            "Son ancienneté est de deux ans et trois mois.",
  "une période d'essai":     "La période d'essai dure trente jours travaillés.",

  'une note de service':     "La note de service est sortie hier après-midi.",
  'une politique interne':   "La politique interne est numérotée par articles.",
  'les exigences du poste':  "Les exigences du poste tiennent en trois lignes.",
  'un droit de retour':      "Le droit de retour protège les deux parties.",

  'un compte rendu':         "Le compte rendu sera affiché vendredi.",
  'un ordre du jour':        "L'ordre du jour comptait trois points.",
  'les qualifications':      "Ses qualifications sont inscrites à son dossier.",

  // ── Les mots de l'exercice de graphie-phonie ────────────────────────
  // Le pilote du niveau 6 l'a vérifié : pour un `vf` à cards + listen, le
  // relevé de `build/releve_sons.js` rend le **texte de la rangée**, pas la
  // phrase porteuse. Les douze clés ci-dessous ne sont donc pas lues par le
  // moteur — elles restent ici parce qu'elles disent au lecteur dans quel
  // sens le mot doit s'entendre, et parce que le générateur audio, lui, passe
  // ces mots par `enrichir()` de `build/voix.py` pour la même raison :
  // « un short » et « un t-shirt » existent en anglais et sortiraient à
  // l'anglaise sans contexte français.
  'un technicien':           "Le technicien de la qualité passe deux fois par quart.",
  'un chronomètre':          "Un chronomètre sert à mesurer le temps de cycle.",
  'le chlore':               "Le chlore du lavage doit être dosé avec soin.",
  'un écho':                 "Un écho court sur le plancher depuis ce matin.",
  'dix':                     "L'affichage reste dix jours ouvrables.",
  'six':                     "Il faut six mois d'ancienneté.",
  'soixante':                "La cafétéria compte soixante places.",
  'soixante-dix':            "L'usine emploie soixante-dix personnes le jour.",
  'un schéma':               "La note était accompagnée d'un schéma très clair.",
  'un shampoing':            "Le shampoing est un produit que l'usine embouteille.",
  'un t-shirt':              "Elle portait un t-shirt bleu de l'entreprise.",
  'un short':                "Un short n'est pas permis dans l'atelier.",
};
