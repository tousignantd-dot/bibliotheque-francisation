const CARRIER_PHRASES = {
  // La clé est le mot LITTÉRAL, tel qu'il paraît dans FC_CARDS et dans la
  // troisième colonne des rangées `savoir` de exos.js : le gabarit fait
  // `CARRIER_PHRASES[w]` sans rien normaliser. Une clé écrite sans article,
  // sans accent ou avec une apostrophe droite ne serait jamais trouvée — la
  // pastille lirait alors le mot tout seul, mal accentué, et rien ne le
  // signalerait avant l'écoute.
  //
  // Trois clés demandent de l'attention : « une œuvre » et « une onomatopée »
  // portent une ligature ou une suite de voyelles que la synthèse rate quand
  // le mot est envoyé seul, et « l'intrigue » porte une apostrophe qui fait
  // partie de la clé. Elles sont écrites ici exactement comme dans exos.js et
  // fccards.js.
  //
  // Dix-sept clés : les seize mots de FC_CARDS, plus « un avis », qui sert de
  // pastille dans deux bandeaux du Défi 3 sans être une carte de vocabulaire.

  // Je découvre — ce qu'on présente au club
  'une œuvre':        "Chaque membre du club présente une œuvre qu'il a aimée.",
  'un roman':         "Elle a fini son roman dans l'autobus, un mardi matin.",
  'une série':        "La série compte huit épisodes de quarante minutes.",
  'un coup de cœur':  "Le comptoir affiche les coups de cœur du mois.",

  // Défi 1 — ce que raconte l'histoire
  "l'intrigue":       "L'intrigue commence quand elle ouvre la maison de sa mère.",
  'un personnage':    "Le personnage principal revient au village après vingt ans.",
  'le dénouement':    "Au club, on s'arrête toujours avant le dénouement.",
  'un extrait':       "Elle lit un extrait de deux pages pour donner le ton.",

  // Défi 2 — lire une bande dessinée
  'une case':         "Dans la première case, on voit seulement une porte fermée.",
  'une bulle':        "La pointe de la bulle montre qui est en train de parler.",
  'une planche':      "Cette planche compte neuf cases et une seule bulle.",
  'une onomatopée':   "L'onomatopée occupe le tiers de la case, en grosses lettres.",
  'un album':         "L'album que vous tenez est le premier tome de la série.",

  // Défi 3 — dire ce qu'on en pense
  'émouvant':         "La scène du départ est la plus émouvante du film.",
  'prévisible':       "La fin est un peu prévisible, mais le reste tient debout.",
  'recommander':      "Je vous le recommande si vous avez déjà quitté un pays.",
  'un avis':          "Un avis sans raison derrière, ça n'apprend rien à personne.",
};
