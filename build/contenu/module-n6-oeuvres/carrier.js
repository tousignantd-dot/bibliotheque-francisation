const CARRIER_PHRASES = {
  // Une phrase porteuse par mot isolé à prononcer. Un mot envoyé seul à la
  // synthèse sort mal accentué, et parfois lu à l'anglaise — « un flash-back »
  // et « un parti pris » en sont deux candidats évidents. La phrase le remet
  // dans un contexte français ; seul le mot est découpé ensuite.
  //
  // Les clés sont les mots **accentués**, tels qu'ils paraissent dans les
  // listes savoir[…][2] de exos.js. Une clé écrite en slug ne serait jamais
  // trouvée, et la pastille lirait le mot seul.
  //
  // Les douze mots de l'exercice de graphie-phonie (`prGraphie`) ne sont
  // **pas** ici, et c'est voulu : pour un `vf` à `cards:true listen:true`, le
  // moteur lit le texte de la rangée et non `CARRIER_PHRASES`. Ces mots-là
  // partent donc seuls à la synthèse, et c'est `enrichir()` de `build/voix.py`
  // qui leur pose un contexte français — sans quoi « un flash-back » et
  // « un shérif » sortiraient à l'anglaise, ce qui est exactement le contraire
  // de ce que l'exercice enseigne.

  // ── Je découvre : la salle, la séance, les formats ────────────────
  'un ciné-club':        "Le ciné-club de la salle Beauchemin se réunit le mercredi soir.",
  'un long métrage':     "Elle a attendu quinze ans avant de tourner un long métrage.",
  'une bande-annonce':   "La bande-annonce montre trois images et ne raconte rien.",
  'le générique':        "Plusieurs personnes se lèvent avant la fin du générique.",

  // ── Défi 1 : le déroulement ───────────────────────────────────────
  'le déroulement':      "Le déroulement du film tient en trois jours.",
  'une scène':           "La scène du quai dure moins de deux minutes.",
  'un retour en arrière': "Chaque retour en arrière est annoncé par le bruit de la mer.",
  'le dénouement':       "On ne raconte jamais le dénouement à quelqu'un qui n'a pas vu le film.",

  // ── Défi 2 : la fabrication du film ───────────────────────────────
  'une réalisatrice':    "La réalisatrice a refusé de parler avant la projection.",
  'un tournage':         "Le tournage a duré sept semaines en Gaspésie.",
  'le montage':          "Elle a appris son métier dans une salle de montage.",
  'une rétrospective':   "Une rétrospective de son œuvre a eu lieu ici en deux mille seize.",

  // ── Défi 3 : le jugement ──────────────────────────────────────────
  'une critique':        "La critique a paru le jeudi matin dans l'hebdomadaire local.",
  'un reproche':         "Son premier reproche porte sur la lenteur du début.",
  'convaincant':         "Le personnage de la voisine est plus convaincant que celui du frère.",
  'un parti pris':       "La lenteur du début est un parti pris, pas une maladresse.",
};
