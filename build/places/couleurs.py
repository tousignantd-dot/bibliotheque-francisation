# -*- coding: utf-8 -*-
"""« Place ce que j'entends » — la table. Niveau 2.

La scène est décrite D'APRÈS les zones du dessin, jamais l'inverse : chaque
phrase nomme une zone qui existe sur l'image et une couleur de la palette.
C'est ce qui rend la correction possible — et c'est aussi ce qui fait
travailler les prépositions de lieu, au programme du niveau 2.
"""

ZONES = [
 # id,        libellé,                     x1,    y1,    x2,    y2   (en % de l'image)
 ("gauche",   "sur la table, à gauche",   0.255, 0.335, 0.395, 0.435),
 ("milieu",   "sur la table, au milieu",  0.425, 0.295, 0.565, 0.400),
 ("droite",   "sur la table, à droite",   0.600, 0.320, 0.745, 0.425),
 ("sous",     "sous la table",            0.330, 0.665, 0.700, 0.790),
 ("chaise",   "sur la chaise",            0.605, 0.115, 0.740, 0.250),
 ("acote",    "à côté de la table",       0.040, 0.580, 0.175, 0.790),
]

# Chaque couleur porte ses accords : la page écrit « une tasse bleue », jamais
# « une tasse bleu ». Dans un cours de français, un accord fautif affiché à
# l'élève enseigne la faute.
COULEURS = [
 ("bleu",  "#1565C0", "bleue",   "bleus",   "bleues"),
 ("rouge", "#D32F2F", "rouge",   "rouges",  "rouges"),
 ("vert",  "#2E7D32", "verte",   "verts",   "vertes"),
 ("jaune", "#F2C200", "jaune",   "jaunes",  "jaunes"),
 ("noir",  "#17181A", "noire",   "noirs",   "noires"),
 ("blanc", "#FFFFFF", "blanche", "blancs",  "blanches"),
 ("brun",  "#6D4C33", "brune",   "bruns",   "brunes"),
 ("orange","#E8720C", "orange",  "orange",  "orange"),   # invariable
]

# La banque : douze objets, six servent. Les six autres sont des leurres —
# sans eux, l'élève placerait juste en éliminant.
# Le genre sert à l'accord de la couleur : m, f, ou fp (féminin pluriel).
BANQUE = [
 ("une assiette","une-assiette","f"),   ("une fourchette","une-fourchette","f"),
 ("un couteau","un-couteau","m"),       ("un verre","un-verre","m"),
 ("une pomme","une-pomme","f"),         ("une banane","une-banane","f"),
 ("une bouteille","une-bouteille","f"), ("une tasse","une-tasse","f"),
 ("du pain","du-pain","m"),             ("du fromage","du-fromage","m"),
 ("du lait","du-lait","m"),             ("des carottes","des-carottes","fp"),
]

# La bonne réponse : un objet, une zone, une couleur.
SCENE = [
 ("une-assiette",   "milieu", "blanc"),
 ("une-fourchette", "gauche", "noir"),
 ("une-pomme",      "droite", "rouge"),
 ("une-bouteille",  "sous",   "vert"),
 ("une-banane",     "chaise", "jaune"),
 ("une-tasse",      "acote",  "bleu"),
]

PHRASES = [
 "Écoutez bien. Je décris une table. Placez les objets sur l'image.",
 "Sur la table, au milieu, il y a une assiette blanche.",
 "Sur la table, à gauche, il y a une fourchette noire.",
 "Sur la table, à droite, il y a une pomme rouge.",
 "Sous la table, il y a une bouteille verte.",
 "Sur la chaise, il y a une banane jaune.",
 "À côté de la table, il y a une tasse bleue.",
 "C'est fini. Touchez « Vérifier ».",
]

# ── Contrôles : la scène doit être cohérente avec les zones et la palette ──
if __name__ == "__main__":
    ids_z = {z[0] for z in ZONES}
    ids_c = {c[0] for c in COULEURS}
    ids_o = {o[1] for o in BANQUE}
    for obj, zone, coul in SCENE:
        assert obj in ids_o, ("objet hors banque", obj)
        assert zone in ids_z, ("zone inconnue", zone)
        assert coul in ids_c, ("couleur hors palette", coul)
    assert len({z for _, z, _ in SCENE}) == len(SCENE), "deux objets dans la même zone"
    # Chaque phrase de placement doit nommer sa zone et sa couleur.
    lib = dict((z[0], z[1]) for z in ZONES)
    for obj, zone, coul in SCENE:
        acc = dict((c[0], (c[2], c[3], c[4])) for c in COULEURS)[coul]
        fem = acc[0]
        bas = [p.lower() for p in PHRASES]
        trouve = any(lib[zone].lower() in p and (coul in p or fem in p)
                     for p in bas)
        assert trouve, ("aucune phrase ne décrit", obj, zone, coul)
    print("  zones :", len(ZONES), "· couleurs :", len(COULEURS),
          "· banque :", len(BANQUE), "· à placer :", len(SCENE))
    print("  ✓ scène cohérente : chaque objet a une zone réelle, une couleur de"
          " la palette, et une phrase qui le dit")
