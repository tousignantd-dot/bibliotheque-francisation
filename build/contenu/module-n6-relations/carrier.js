const CARRIER_PHRASES = {
  // Une phrase porteuse par mot isolé à prononcer. Un mot envoyé seul à la
  // synthèse sort mal accentué, et parfois lu à l'anglaise. La phrase le
  // remet dans un contexte français ; seul le mot est découpé ensuite.
  //
  // Les clés sont les mots **accentués**, tels qu'ils paraissent dans les
  // listes savoir[…][2] de exos.js. Une clé écrite en slug ne serait jamais
  // trouvée.

  // ── Je découvre — les évènements d'un courriel de nouvelles ───────
  'une naissance':          "Il annonce une naissance dès le premier paragraphe.",
  'un déménagement':        "Leur déménagement a eu lieu en juin.",
  'des funérailles':        "Les funérailles ont eu lieu au pays, en février.",
  'un faire-part':          "Elle a gardé le faire-part du mariage sur la porte du réfrigérateur.",
  'un accident de travail': "Son beau-frère a eu un accident de travail en novembre.",

  // ── Défi 1 — ce que le courriel raconte ──────────────────────────
  'une réadaptation':       "Après le plâtre, sa réadaptation a duré presque trois mois.",
  'des retrouvailles':      "Ces retrouvailles arrivent après deux ans sans nouvelles.",
  'un imprévu':             "Elle a répondu tout de suite, au cas où il y aurait un imprévu.",
  'un paragraphe à part':   "La mauvaise nouvelle se met dans un paragraphe à part, à la fin.",

  // ── Défi 2 — décrire quelqu'un ───────────────────────────────────
  'une silhouette':         "De l'autre bout du terminus, on ne voit qu'une silhouette et une valise.",
  'un visage allongé':      "Elle a un visage allongé et les pommettes hautes.",
  'des cheveux ondulés':    "Ses cheveux ondulés sont attachés en chignon bas.",
  'un signe particulier':   "Sa petite cicatrice au-dessus du sourcil est un signe particulier.",
  'le jour où il est tombé': "Le jour où il est tombé, sa sœur venait de s'installer.",

  // ── Défi 3 — l'organisme et l'article ────────────────────────────
  'un jumelage':            "Le jumelage dure six mois, à raison d'une rencontre aux deux semaines.",
  'un organisme communautaire': "L'organisme communautaire occupe deux locaux au sous-sol de l'église.",
  'un bénévole':            "Chaque duo est accompagné par un bénévole du quartier.",
  'une coordonnatrice':     "La coordonnatrice a été citée deux fois dans l'article.",
  'un duo':                 "Chaque duo s'engage pour six mois.",

  // ── Les mots de l'exercice de graphie-phonie ─────────────────────
  // Gardées pour mémoire : pour un `vf` à `cards:true listen:true`, le
  // relevé de `build/releve_sons.js` rend le **texte de la rangée**, pas la
  // phrase porteuse. Ces clés-là sont donc inutilisées par le moteur — et
  // `coherence.js` a raison de ne pas les compter comme un écart. C'est
  // `enrichir()` de `build/voix.py` qui donne à ces mots courts leur contexte
  // français au moment de la synthèse, sans quoi « un short » et « du
  // shampoing » sortiraient à l'anglaise.
  'une chorale':            "La chorale du quartier répète le mercredi soir.",
  'une chorale du quartier': "Une chorale du quartier chante à la fête de septembre.",
  'la technique':           "La technique de réparation n'a pas changé depuis vingt ans.",
  'un écho':                "Un écho répond dans le sous-sol vide.",
  'la psychologie':         "La psychologie de l'accueil intéresse beaucoup l'organisme.",
  'dix':                    "Elle a relu la lettre dix fois avant de l'envoyer.",
  'six':                    "Le jumelage dure six mois.",
  'soixante':               "Ghislain a soixante-deux ans.",
  'Bruxelles':              "Sa cousine a vécu deux ans à Bruxelles.",
  'un short':               "Il portait un short et de vieilles sandales.",
  'un schéma':              "Elle a dessiné un schéma pour lui expliquer le trajet.",
  'du shampoing':           "Il a acheté du shampoing en revenant du terminus.",
};
