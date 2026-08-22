const CARRIER_PHRASES = {
  // La clé est le mot LITTÉRAL tel qu'il paraît dans FC_CARDS et dans la
  // troisième colonne d'une rangée `savoir` à pastilles : le gabarit fait
  // `CARRIER_PHRASES[w]` sans normaliser. Une clé écrite autrement — en slug,
  // sans article, sans accent — ne serait jamais trouvée, et le mot partirait
  // seul à la synthèse, mal accentué.
  //
  // Une seule clé de ce module porte une apostrophe, « l'indice UV ». Elle
  // est écrite ici entre guillemets doubles, exactement comme dans exos.js et
  // fccards.js.
  //
  // Deux sigles à surveiller à la synthèse : « UV » se dit lettre par lettre
  // et la phrase porteuse le place au milieu, jamais à la fin, pour que la
  // voix ne l'avale pas.

  // Je découvre — l'avis météo et ses trois mots
  'une veille':               "Une veille de tempête hivernale a été émise pour le Bas-Saint-Laurent.",
  'un avertissement':         "L'avertissement de pluie verglaçante est en vigueur jusqu'à samedi matin.",
  'les prévisions':           "Les prévisions de vendredi ont changé trois fois dans la même journée.",
  'une éclaircie':            "On annonce quelques éclaircies en fin d'après-midi.",

  // Défi 1 — l'hiver tel que le bulletin le nomme
  'la pluie verglaçante':     "La pluie verglaçante laissera trois millimètres de glace sur les trottoirs.",
  'la poudrerie':             "La poudrerie réduira la visibilité à moins d'un kilomètre en soirée.",
  'le refroidissement éolien': "Moins douze au thermomètre, mais un refroidissement éolien de moins vingt-deux.",
  'une bordée de neige':      "La bordée de neige de la nuit a laissé trente centimètres dans le stationnement.",

  // Défi 2 — le printemps et la décision
  'la crue printanière':      "La crue printanière a inondé les sentiers du bas du parc.",
  'le dégel':                 "Le dégel de la semaine dernière a transformé le sentier en boue.",
  'reporter':                 "La sortie est reportée au samedi vingt-deux, à la même heure.",
  'annuler':                  "On annule seulement quand il n'y a aucune date de rechange.",

  // Défi 3 — l'été, le froid, et le sac qu'on prépare
  'la chaleur extrême':       "Un avertissement de chaleur extrême était en vigueur toute la fin de semaine.",
  "l'indice UV":              "Avec un indice UV de neuf, une heure au soleil suffit à brûler la peau.",
  'un coup de chaleur':       "On boit avant d'avoir soif : c'est comme ça qu'on évite un coup de chaleur.",
  'des crampons':             "Avec des crampons, un trottoir gelé redevient marchable.",
};
