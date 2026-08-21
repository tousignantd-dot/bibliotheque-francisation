const CARRIER_PHRASES = {
  // La clé est le mot LITTÉRAL tel qu'il apparaît dans un tableau `mots` d'un
  // bloc `savoir` : le gabarit fait `CARRIER_PHRASES[w]` sans normaliser. Une
  // clé écrite en style de nom de fichier (`etat_des_lieux`) ne serait jamais
  // trouvée, et le mot partirait seul à la synthèse — mal accentué.
  'déménagement':      "Le déménagement est le premier juillet.",
  'camion':            "Le camion arrive à huit heures.",
  'appartement':       "Mon appartement est au deuxième étage.",
  'chambre':           "La chambre du fond donne sur la ruelle.",
  'quarante':          "Une égratignure de quarante centimètres.",
  'salon':             "Le divan va dans le salon.",
  'plafond':           "Il y a une tache jaune au plafond.",
  'maison':            "Ils ont acheté une maison à Beauport.",
  'seulement':         "Il reste seulement des camions le matin.",
  'bonne':             "La voisine est bien bonne avec moi.",
  'faire le tour':     "Il faut faire le tour du logement avant de signer.",
  "l'état des lieux":  "L'état des lieux se fait dans un logement vide.",
};
