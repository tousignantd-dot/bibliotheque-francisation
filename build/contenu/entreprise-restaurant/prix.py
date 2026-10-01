"""Les prix de la page acheteur de Chez Jocelyne — UN SEUL ENDROIT pour les changer.

Décision du plan (30 sept. 2026, « vente : comme Francœur et l'hôtel ») : les
mêmes formules et les mêmes règles — jamais à l'heure ; le premier prix est le
plancher des suivants ; le droit de réutilisation du matériel est conservé.
Montants de la Maison Francœur : comme elle, la restauration a UNE langue apprise
et UN groupe pilote (l'hôtel en avait deux, d'où son pilote relevé).

À CONFIRMER par Daniel : CONFIRME vaut None tant qu'il ne l'a pas fait, et la page
le dit.
"""

CONFIRME = None

# (titre, montant affiché, unité, pour qui, ce qui est compris)
FORMULES = [
    ("Le pilote dans votre restaurant", "3 000 à 6 000 $", "prix fixe",
     "Pour commencer : un restaurant, un petit groupe d'employés de cuisine et de salle.",
     ["la trousse ajustée à votre restaurant : votre menu, vos plats, vos allergènes, votre cuisine",
      "le pilote : deux séances avec un groupe de quatre à huit employés, et votre formateur",
      "le diagnostic : ce que le matériel a fait rater, et sa révision",
      "les fiches de poche et le guide du formateur"]),
    ("La trousse à votre métier", "12 000 à 25 000 $", "prix fixe",
     "Pour un autre poste : boulangerie, épicerie, cafétéria, entretien, entrepôt…",
     ["un lexique neuf, son décor, ses voix et ses langues d'appui",
      "les exercices, le test de niveau et les situations jouées, écrits pour ce poste",
      "le pilote et la révision",
      "les fiches de poche et le guide du formateur"]),
    ("La licence annuelle", "2 000 à 5 000 $", "par année",
     "Pour une chaîne, une bannière ou un partenaire qui la déploie lui-même.",
     ["l'usage de la trousse par vos groupes, sans limite d'employés",
      "l'hébergement, les voix et les situations jouées",
      "les corrections et les mises à jour de l'année"]),
]

NOTES = [
    "Des prix fixes, jamais à l'heure. La fourchette dépend de la portée : le nombre de situations et de "
    "langues d'appui.",
    "Montants avant taxes.",
    "Le matériel reste notre propriété ; vous en avez l'usage.",
    "La trousse ne remplace pas la formation en hygiène et salubrité exigée des restaurants.",
    "Ces montants paient du développement de matériel de formation, une dépense que certains "
    "programmes publics financent — admissibilité à vérifier avec votre conseiller.",
]
