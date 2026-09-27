"""Les prix de la page acheteur de l'hôtel — UN SEUL ENDROIT pour les changer.

Mêmes fourchettes et mêmes règles que la Maison Francœur
(build/contenu/entreprise-francoeur/prix.py, ajoutées à la demande de Daniel le
24 septembre 2026) : jamais à l'heure ; le premier prix est le plancher des
suivants ; le droit de réutilisation du matériel est conservé. Seuls les mots
changent : un hôtel, un comptoir, trois langues. Les montants sont À CONFIRMER
par Daniel pour ce secteur — l'hôtellerie n'a pas été chiffrée à part.
"""

# (titre, montant affiché, unité, pour qui, ce qui est compris)
FORMULES = [
    ("Le pilote à votre réception", "3 000 à 6 000 $", "prix fixe",
     "Pour commencer : un hôtel, un petit groupe de réceptionnistes.",
     ["la trousse ajustée à votre hôtel : vos chambres, vos tarifs, vos services, votre politique",
      "le pilote : deux séances avec un groupe de trois à six employés, et votre formateur",
      "le diagnostic : ce que le matériel a fait rater, et sa révision",
      "les fiches de poche et le guide du formateur"]),
    ("La trousse à votre métier", "12 000 à 25 000 $", "prix fixe",
     "Pour un autre poste d'accueil : restaurant, clinique, location d'autos, service à la clientèle…",
     ["un lexique neuf, son décor, ses voix, dans les langues de vos employés",
      "les exercices, le test de niveau et les clients du jeu de rôle, écrits pour ce poste",
      "le pilote et la révision",
      "les fiches de poche et le guide du formateur"]),
    ("La licence annuelle", "2 000 à 5 000 $", "par année",
     "Pour un réseau, une chaîne ou un partenaire qui la déploie lui-même.",
     ["l'usage de la trousse par vos groupes, sans limite d'employés",
      "l'hébergement, les voix et le jeu de rôle",
      "les corrections et les mises à jour de l'année"]),
]

NOTES = [
    "Des prix fixes, jamais à l'heure. La fourchette dépend de la portée : le nombre de situations, "
    "de clients et de langues.",
    "Montants avant taxes.",
    "Le matériel reste notre propriété ; vous en avez l'usage.",
    "Ces montants paient du développement de matériel de formation, une dépense que certains "
    "programmes publics financent — admissibilité à vérifier avec votre conseiller.",
]
