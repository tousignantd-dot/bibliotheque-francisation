"""La série « Les pièges » — les faux amis, côte à côte avec ce qu'on confond.

Audit de la boucle didactique, 24 septembre 2026 (D3, majeur) : les paires que
le test mesure (veste/veston, bas/pantalon…) ne se rencontraient jamais en
pratique, parce que les distracteurs de l'exercice venaient du MÊME rayon et
que ces mots vivent dans des rayons différents. Ici, chaque piège revient avec
des contrastes écrits à la main — AUTRES que ceux du test, qui doit rester
inédit —, entrelacé avec des mots ordinaires.

(id du piège, [trois contrastes])
"""

PIEGES = [
    ("veste",           ["cardigan", "parka", "polo"]),
    ("bas-chaussettes", ["bermuda", "jogging", "short"]),
    ("mitaines",        ["tuque", "cache-cou", "gants"]),
    ("jaquette",        ["pyjama", "blouse", "robe-soiree"]),
    ("espadrilles",     ["bottillons", "gougounes", "talons"]),
    ("sacoche",         ["ceinture", "portefeuille", "chapeau"]),
    ("taille-ceinture", ["poche", "jambe", "ourlet"]),
    ("culotte",         ["boxer", "maillot", "collants"]),
]
# Des mots ordinaires, entrelacés : une série faite QUE de pièges apprendrait
# à tout soupçonner.
ORDINAIRES = ["t-shirt", "jeans", "manteau", "robe", "souliers", "casquette"]
