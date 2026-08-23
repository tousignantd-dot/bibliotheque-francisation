const CARRIER_PHRASES = {
  // La clé est le mot LITTÉRAL, tel qu'il paraît dans FC_CARDS et dans la
  // troisième colonne des rangées `savoir` de exos.js : le gabarit fait
  // `CARRIER_PHRASES[w]` sans rien normaliser. Une clé écrite en slug, sans
  // article ou sans accent, ne serait jamais trouvée — la pastille lirait
  // alors le mot tout seul, mal accentué, et rien ne le signalerait avant
  // l'écoute.
  //
  // Cinq clés portent un accent qui compte : « la boîte vocale », « un
  // répondeur », « un empêchement », « un motif », « les coordonnées ». Elles
  // sont écrites ici exactement comme dans fccards.js.
  //
  // Deux mots de ce module existent aussi en anglais et en espagnol —
  // « un message », « une signature » — et un troisième, « le clavier »,
  // ressemble à « clavier » du français seulement. La phrase porteuse les
  // remet tous dans un contexte français ; `enrichir()` de build/voix.py fait
  // le reste au moment de la synthèse.
  //
  // Les seize mots servent tous de pastille au moins une fois dans un bloc
  // `savoir` à `speak:true` — relevé croisé fait sur exos.js, dans les deux
  // sens : aucun mot sans phrase porteuse, aucune clé inutilisée.

  // Je découvre — ce qu'il y a au bout du fil
  'la boîte vocale':   "Avant huit heures, c'est la boîte vocale qui répond.",
  'un répondeur':      "Le répondeur du centre donne les heures d'ouverture avant tout.",
  'le clavier':        "Elle a cherché le 1 sur le clavier du téléphone.",
  'la ligne':          "La ligne était occupée : elle a rappelé plus tard.",

  // Défi 1 — le message qu'on laisse
  'un poste':          "Le secrétariat, c'est le poste 224 du centre.",
  'le signal sonore':  "Parlez après le signal sonore, jamais avant.",
  'un message':        "Son message durait cinquante secondes en tout.",
  'les coordonnées':   "Elle a laissé ses coordonnées deux fois, lentement.",

  // Défi 2 — les motifs
  'un retard':         "Un retard de dix minutes se signale aussi.",
  'une absence':       "Son absence de lundi est inscrite au dossier.",
  'un abandon':        "Un abandon annoncé par écrit n'est pas un échec.",
  'un empêchement':    "Elle a téléphoné dès qu'elle a su qu'elle avait un empêchement.",

  // Défi 3 — la note écrite
  'une note':          "La note tient en cinq lignes, datées et signées.",
  'un motif':          "Le motif se dit en une seule phrase.",
  'une signature':     "Sans signature, la note reste une simple feuille.",
  'une copie':         "Elle a fait une copie avant de descendre au comptoir.",
};
