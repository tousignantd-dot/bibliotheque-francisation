"""Les prix de la page acheteur — UN SEUL ENDROIT pour les changer.

Repris des fourchettes établies le 19 septembre 2026 pour le chantier du détail
(mémoire chantier-detail-chaussure) : CONSTRUITES, jamais relevées — aucun
tarif de formation sur mesure n'est publié, ni au privé ni dans le réseau
public. Trois règles qui vont avec, et qui se lisent dans la page :

  · jamais à l'heure : notre avantage est la vitesse de la chaîne, et l'horaire
    le convertit en rabais ;
  · le premier prix devient le plancher de tous les suivants — pour gagner une
    entente, on réduit la PORTÉE, pas le prix ;
  · le droit de réutilisation du matériel est conservé.

Ajoutés à la page acheteur à la demande de Daniel, le 24 septembre 2026.
"""

# (titre, montant affiché, unité, pour qui, ce qui est compris)
FORMULES = [
    ("Le pilote sur votre plancher", "3 000 à 6 000 $", "prix fixe",
     "Pour commencer : un magasin, un petit groupe d'employés.",
     ["la trousse ajustée à votre magasin : vos rayons, vos mots, votre politique de retour, vos clients",
      "le pilote : deux séances avec un groupe de quatre à huit employés, et votre formateur",
      "le diagnostic : ce que le matériel a fait rater, et sa révision",
      "les fiches de poche et le guide du formateur"]),
    ("La trousse à votre enseigne", "12 000 à 25 000 $", "prix fixe",
     "Pour un autre commerce : chaussures, quincaillerie, épicerie, pharmacie…",
     ["un lexique neuf, ses croquis, ses voix et ses traductions dans les onze langues",
      "les exercices, le test de niveau et les clients du magasin, écrits pour ce commerce",
      "le pilote et la révision",
      "les fiches de poche et le guide du formateur"]),
    ("La licence annuelle", "2 000 à 5 000 $", "par année",
     "Pour un réseau ou un partenaire qui la déploie lui-même.",
     ["l'usage de la trousse par vos groupes, sans limite d'employés",
      "l'hébergement, les voix et le jeu de rôle",
      "les corrections et les mises à jour de l'année"]),
]

NOTES = [
    "Des prix fixes, jamais à l'heure. La fourchette dépend de la portée : le nombre de rayons, "
    "de clients et de langues.",
    "Montants avant taxes.",
    "Le matériel reste notre propriété ; vous en avez l'usage.",
    "Ces montants paient du développement de matériel de formation, une dépense que certains "
    "programmes publics financent — admissibilité à vérifier avec votre conseiller.",
]
