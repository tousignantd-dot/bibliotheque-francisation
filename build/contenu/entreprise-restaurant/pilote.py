"""Le pilote réel de Chez Jocelyne — ce qui se remplit une fois le restaurant trouvé.

Lu par build/restauration_pilote_trousse.py (la trousse du pilote : décisions,
calendrier, documents à imprimer). Tant qu'une valeur est None, les documents
portent une ligne à remplir à la main : ils s'impriment quand même.

Les valeurs viennent de l'export de la page restauration-pilote-trousse.html.
"""

RESTAURANT = None     # le nom du restaurant partenaire (réel), ex. « Casse-croûte du Coin »
VILLE = None
CONTACT = None        # la personne qui reçoit la lettre (titre, pas forcément un nom)
SEANCE_1 = None       # « mardi 13 octobre 2026, 14 h 30 »
SEANCE_2 = None
FORMATEUR = None      # « Daniel Tousignant » ou le formateur du restaurant
OBSERVATEUR = None
CONDITIONS = None     # clé de CONDITIONS_TEXTE
POSTES = None         # clé de POSTES_TEXTE

CONDITIONS_TEXTE = {
    "validation": "Le pilote est offert : c'est un pilote de validation. En échange, le restaurant accepte d'être "
                  "nommé comme lieu du pilote et de fournir un court témoignage écrit s'il en est satisfait.",
    "reduit": "Le pilote est offert à la moitié du prix de la formule « pilote » (3 000 à 6 000 $), en échange "
              "d'un témoignage écrit et du droit de nommer le restaurant.",
    "plein": "Le pilote est facturé selon la formule « pilote » (3 000 à 6 000 $, prix fixe selon la portée).",
}
POSTES_TEXTE = {
    "deux": "Un groupe de quatre à huit employés qui commencent, en cuisine et en salle.",
    "cuisine": "Un groupe de quatre à huit employés de cuisine qui commencent (commis, cuisiniers, plongeurs).",
    "salle": "Un groupe de quatre à huit employés de salle qui commencent (serveurs, hôtes, caissiers).",
}

# Les deux séances, minute par minute, pour la feuille de route du formateur.
# Le protocole (restauration_pilote.py) en donne la version détaillée :
# restauration_pilote_trousse.py refuse de construire si les minutes divergent.
SEANCES = [
    ("Séance 1", [
        ("Accueil, langue d'appui, puis le test (première forme)", 20,
         "Chacun choisit sa langue d'appui. Le test : le formateur ouvre son panneau avec son code, écoute l'oral, "
         "note et confirme le niveau."),
        ("Le poste de cuisine et les planches", 20,
         "Toucher le poste, écouter les mots. Noter : touchent-ils « voir dans ma langue » à chaque mot, ou jamais ?"),
        ("Les exercices : entendre, image, pièges, la consigne du chef", 35,
         "Chacun à son rythme, écouteurs, bruit de cuisine au « Faible » puis au « Fort ». L'observateur note où ça "
         "bloque, sans aider."),
        ("Retour à chaud", 15, "Deux questions : qu'est-ce qui était difficile à entendre ? le bruit a-t-il aidé ou gêné ?"),
    ]),
    ("Séance 2", [
        ("La commande modifiée, l'allergie, je le redis", 25,
         "Les erreurs graves à l'allergie, une par une : l'item ou le geste ?"),
        ("Le service", 30,
         "Chacun joue sa porte (cuisine ou salle) : deux ou trois situations, dont l'allergie. Le formateur conteste "
         "le bilan quand il le faut : c'est une donnée du pilote."),
        ("Le test, repassé (seconde forme)", 20, "« Avant → maintenant » à l'écran ; le formateur note l'oral."),
        ("Entretien de groupe", 15, "Les questions du protocole. Rien de nominatif."),
    ]),
]
