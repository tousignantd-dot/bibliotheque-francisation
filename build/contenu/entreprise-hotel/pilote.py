"""Le pilote réel de l'Hôtel Rive-Claire — ce qui se remplit une fois l'hôtel trouvé.

Lu par build/hotel_pilote_trousse.py (la trousse du pilote : décisions, calendrier,
documents à imprimer). Tant qu'une valeur est None, les documents portent une
ligne à remplir à la main : ils s'impriment quand même.

Les valeurs viennent de l'export de la page hotellerie-pilote-trousse.html.
"""

HOTEL = None          # le nom de l'hôtel partenaire (réel), ex. « Hôtel du Parc »
VILLE = None
CONTACT = None        # la personne qui reçoit la lettre (titre, pas forcément un nom)
SEANCE_1 = None       # « mardi 13 octobre 2026, 14 h »
SEANCE_2 = None
FORMATEUR = None      # « Daniel Tousignant » ou le formateur de l'hôtel
OBSERVATEUR = None
CONDITIONS = None     # clé de CONDITIONS_TEXTE
GROUPES = None        # clé de GROUPES_TEXTE

CONDITIONS_TEXTE = {
    "validation": "Le pilote est offert : c'est un pilote de validation. En échange, l'hôtel accepte d'être nommé "
                  "comme lieu du pilote et de fournir un court témoignage écrit s'il en est satisfait.",
    "reduit": "Le pilote est offert à la moitié du prix de la formule « pilote » (4 000 à 8 000 $), en échange "
              "d'un témoignage écrit et du droit de nommer l'hôtel.",
    "plein": "Le pilote est facturé selon la formule « pilote » (4 000 à 8 000 $, prix fixe selon la portée).",
}
GROUPES_TEXTE = {
    "deux": ("Deux petits groupes : A, des réceptionnistes francophones qui servent des clients anglophones "
             "(ils apprennent l'anglais) ; B, des réceptionnistes hispanophones qui apprennent le français."),
    "A": "Un groupe : des réceptionnistes francophones qui servent des clients anglophones (ils apprennent l'anglais).",
    "B": "Un groupe : des réceptionnistes hispanophones qui apprennent le français.",
}

# Les deux séances, minute par minute, pour la feuille de route du formateur.
# Le protocole (hotel_pilote.py) en donne la version détaillée, chiffres compris :
# hotel_pilote_trousse.py refuse de construire si les minutes divergent.
SEANCES = [
    ("Séance 1", [
        ("Accueil, langues, puis le test (première forme)", 20,
         "Chacun choisit sa langue et celle qu'il apprend. Le test : le code du formateur ouvre la passation ; "
         "le formateur note l'oral et confirme le niveau."),
        ("Le comptoir dessiné et les planches", 20,
         "Toucher les objets, écouter. Noter : touchent-ils « voir dans ma langue » à chaque mot, ou jamais ?"),
        ("Les exercices : entendre, image, pièges, nombres", 35,
         "Chacun à son rythme, écouteurs. L'observateur note où ça bloque, sans aider."),
        ("Retour à chaud", 15, "Deux questions : qu'est-ce qui était difficile à entendre ? que voulez-vous refaire ?"),
    ]),
    ("Séance 2", [
        ("Épeler, ce que le client veut, ce que je réponds", 20,
         "La règle du relais tient-elle ? (ce qu'on décide seul, ce qu'on transmet au gérant)"),
        ("Au comptoir", 35,
         "Huit clients, trois à cinq minutes chacun. Compter « réussies sur 8 » et « du premier coup ». "
         "Le formateur conteste le bilan quand il le faut : c'est une donnée du pilote."),
        ("Le test, repassé (seconde forme)", 20, "Des items nouveaux ; l'écart avec la première passation."),
        ("Entretien de groupe", 15, "Les questions du protocole. Rien de nominatif."),
    ]),
]
