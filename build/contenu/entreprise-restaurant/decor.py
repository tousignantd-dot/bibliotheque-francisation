"""Les zones du décor (le poste vu de la place du commis), en % de l'image.

(id du lexique, gauche, haut, largeur, hauteur). Les trois mots « decor » du
lexique (la ligne, le passe, la plonge) n'ont PAS d'autre image que celle-ci ;
les autres zones désignent, dans le poste, des objets qui ont aussi leur croquis.
Placées à l'œil puis DESSINÉES sur l'image pour contrôle (30 sept. 2026).
"""
ZONES = [
    ("passe",       21, 37, 58, 22),
    ("ligne",       11, 81, 75,  7),
    ("plonge",       1, 25, 18, 48),
    ("planche",     16, 69, 22, 11),
    ("bac",         39, 62, 21, 10),
    ("plaque",      61, 60, 21, 18),
    ("friteuse",    83, 56, 16, 16),
]
