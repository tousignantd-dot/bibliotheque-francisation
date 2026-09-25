"""Les zones à toucher du comptoir — (id du lexique, x %, y %, rayon %).

Mesurées sur `assets/interactive/hotel/croquis/comptoir.jpg` (3:2) et
vérifiées par superposition (`python3 build/hotel_planches.py --zones`, qui
dessine les pastilles sur l'image). Refaire le comptoir oblige à les remesurer.
"""
ZONES = [
    ("ecran",         15, 66, 7),
    ("imprimante",    32, 76, 4),
    ("terminal",      41, 81, 4),
    ("encodeur",      49, 78, 4),
    ("telephone",     66, 80, 5),
    ("tiroir-caisse", 82, 93, 4),
    ("sonnette",      78, 58, 3),
    ("carte-cle",     52, 85, 3),
    ("dossier",       89, 82, 5),
    ("plan-ville",    33, 58, 5),
    ("presentoir",    21, 48, 4),
    ("depliant",      17, 30, 4),
    ("horloges",      66, 27, 5),
    ("bureau-gerant", 87, 37, 6),
    ("hall",          45, 47, 7),
]
