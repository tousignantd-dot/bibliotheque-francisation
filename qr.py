"""Un code QR, en bibliothèque standard, rendu en SVG.

**Pourquoi écrire ça plutôt que d'appeler un service.** Le carré est imprimé
sur une feuille distribuée à des élèves ; l'envoyer fabriquer ailleurs
reviendrait à confier l'adresse d'une classe à un tiers, sur le seul mode du
portail qui ne collecte rien. Et une image distante manquante, le matin d'un
cours, laisse une feuille avec un trou au milieu.

**Pourquoi pas une bibliothèque.** `requirements.txt` dit la règle du dépôt :
bibliothèque standard, sauf Postgres. Une dépendance de plus se paie à chaque
déploiement, et celle-ci ne servirait qu'à dessiner un carré.

**Ce qui est couvert, et pourquoi seulement ça.** Mode octet, correction de
niveau Q, versions 1 à 10 — de quoi encoder une adresse de 150 caractères. Le
niveau Q corrige un quart du carré : c'est le niveau qui survit à une
photocopie de photocopie, et c'est exactement ce qui va arriver à cette
feuille. Les autres niveaux ne sont pas là parce qu'ils ne serviraient à rien
ici, et qu'une table recopiée à la main est une table où l'on se trompe.

Le rendu est un SVG : il s'imprime net à n'importe quelle taille, ce qu'une
image en points ne fait pas.

Vérifié par `build/controles/qr.py`, qui compare la matrice produite, module
par module, à celle de la bibliothèque `segno`, et fait relire le carré par le
décodeur d'OpenCV — les deux uniquement au contrôle, jamais en service.
"""

# ── Les tables du format, pour le niveau Q ──────────────────────────────────
# Par version : (octets de données, blocs du groupe 1, octets par bloc du
# groupe 1, blocs du groupe 2, octets par bloc du groupe 2, octets de
# correction par bloc).
TABLE_Q = {
    1:  (13,   1, 13, 0, 0,  13),
    2:  (22,   1, 22, 0, 0,  22),
    3:  (34,   2, 17, 0, 0,  18),
    4:  (48,   2, 24, 0, 0,  26),
    5:  (62,   2, 15, 2, 16, 18),
    6:  (76,   4, 19, 0, 0,  24),
    7:  (88,   2, 14, 4, 15, 18),
    8:  (110,  4, 18, 2, 19, 22),
    9:  (132,  4, 16, 4, 17, 20),
    10: (154,  6, 19, 2, 20, 24),
}

# Centres des motifs d'alignement, par version.
ALIGNEMENTS = {
    1: [], 2: [6, 18], 3: [6, 22], 4: [6, 26], 5: [6, 30], 6: [6, 34],
    7: [6, 22, 38], 8: [6, 24, 42], 9: [6, 26, 46], 10: [6, 28, 50],
}


# ── Le corps fini GF(256), où vit la correction d'erreurs ───────────────────
_EXP = [0] * 512
_LOG = [0] * 256


def _table_galois():
    x = 1
    for i in range(255):
        _EXP[i] = x
        _LOG[x] = i
        x <<= 1
        if x & 0x100:                      # polynôme primitif 0x11D
            x ^= 0x11D
    for i in range(255, 512):
        _EXP[i] = _EXP[i - 255]


_table_galois()


def _mul(a, b):
    if a == 0 or b == 0:
        return 0
    return _EXP[_LOG[a] + _LOG[b]]


def _polynome_generateur(n):
    """Le polynôme générateur de degré n : (x - α⁰)(x - α¹)…(x - αⁿ⁻¹)."""
    g = [1]
    for i in range(n):
        g = _multiplier(g, [1, _EXP[i]])
    return g


def _multiplier(a, b):
    produit = [0] * (len(a) + len(b) - 1)
    for i, ai in enumerate(a):
        for j, bj in enumerate(b):
            produit[i + j] ^= _mul(ai, bj)
    return produit


def correction(donnees, n):
    """Les n octets de correction d'un bloc de données."""
    g = _polynome_generateur(n)
    reste = list(donnees) + [0] * n
    for i in range(len(donnees)):
        tete = reste[i]
        if tete:
            for j, gj in enumerate(g):
                reste[i + j] ^= _mul(gj, tete)
    return reste[len(donnees):]


# ── Les octets du message ───────────────────────────────────────────────────

def _version_pour(n_octets):
    for version in sorted(TABLE_Q):
        capacite = TABLE_Q[version][0]
        # L'en-tête : 4 bits de mode + le compteur de caractères (8 bits
        # jusqu'à la version 9, 16 ensuite), soit 2 ou 3 octets.
        entete = 2 if version <= 9 else 3
        if n_octets + entete <= capacite:
            return version
    raise ValueError("texte trop long pour un code QR de version 10")


def _bits_du_message(texte, version):
    octets = texte.encode("utf-8")
    bits = []

    def ajoute(valeur, longueur):
        for i in range(longueur - 1, -1, -1):
            bits.append((valeur >> i) & 1)

    ajoute(0b0100, 4)                                   # mode octet
    ajoute(len(octets), 8 if version <= 9 else 16)
    for o in octets:
        ajoute(o, 8)

    capacite = TABLE_Q[version][0] * 8
    # Terminateur : quatre zéros, ou moins s'il ne reste pas la place.
    ajoute(0, min(4, capacite - len(bits)))
    while len(bits) % 8:
        bits.append(0)
    # Remplissage : 0xEC et 0x11 en alternance, tel que le prescrit la norme.
    remplissage = (0xEC, 0x11)
    i = 0
    while len(bits) < capacite:
        ajoute(remplissage[i % 2], 8)
        i += 1
    return [int("".join(str(b) for b in bits[k:k + 8]), 2)
            for k in range(0, len(bits), 8)]


def _codets_finaux(texte, version):
    """Les octets, découpés en blocs, corrigés, puis entrelacés."""
    donnees = _bits_du_message(texte, version)
    _, n1, t1, n2, t2, n_ecc = TABLE_Q[version]
    blocs, blocs_ecc, curseur = [], [], 0
    for nombre, taille in ((n1, t1), (n2, t2)):
        for _ in range(nombre):
            bloc = donnees[curseur:curseur + taille]
            curseur += taille
            blocs.append(bloc)
            blocs_ecc.append(correction(bloc, n_ecc))
    sortie = []
    # L'entrelacement : un octet de chaque bloc, tour à tour. C'est lui qui
    # fait qu'une tache sur le papier abîme un peu de chaque bloc plutôt que
    # d'en détruire un seul.
    for i in range(max(len(b) for b in blocs)):
        for b in blocs:
            if i < len(b):
                sortie.append(b[i])
    for i in range(n_ecc):
        for b in blocs_ecc:
            sortie.append(b[i])
    return sortie


# ── La trame ────────────────────────────────────────────────────────────────

def _bch(valeur, generateur, degre):
    v = valeur << degre
    while v.bit_length() - 1 >= generateur.bit_length() - 1:
        v ^= generateur << (v.bit_length() - generateur.bit_length())
    return v


def _motifs_fixes(version):
    """La trame vide : (modules, réservé). `réservé` marque tout ce qui ne
    doit pas recevoir de données."""
    n = 17 + 4 * version
    m = [[0] * n for _ in range(n)]
    reserve = [[False] * n for _ in range(n)]

    def poser(y, x, motif):
        for dy, ligne in enumerate(motif):
            for dx, v in enumerate(ligne):
                if 0 <= y + dy < n and 0 <= x + dx < n:
                    m[y + dy][x + dx] = v
                    reserve[y + dy][x + dx] = True

    oeil = [[1, 1, 1, 1, 1, 1, 1],
            [1, 0, 0, 0, 0, 0, 1],
            [1, 0, 1, 1, 1, 0, 1],
            [1, 0, 1, 1, 1, 0, 1],
            [1, 0, 1, 1, 1, 0, 1],
            [1, 0, 0, 0, 0, 0, 1],
            [1, 1, 1, 1, 1, 1, 1]]
    for y, x in ((0, 0), (0, n - 7), (n - 7, 0)):
        poser(y, x, oeil)
    # Séparateurs : la bande blanche autour de chaque œil.
    for y, x in ((0, 0), (0, n - 8), (n - 8, 0)):
        for i in range(8):
            for (yy, xx) in ((y + i, x + 7 if x == 0 else x),
                             (y + 7 if y == 0 else y, x + i)):
                if 0 <= yy < n and 0 <= xx < n:
                    m[yy][xx] = 0
                    reserve[yy][xx] = True

    centres = ALIGNEMENTS[version]
    for cy in centres:
        for cx in centres:
            if (cy, cx) in ((6, 6), (6, centres[-1]), (centres[-1], 6)):
                continue                       # sous un œil : pas d'alignement
            poser(cy - 2, cx - 2, [[1, 1, 1, 1, 1],
                                   [1, 0, 0, 0, 1],
                                   [1, 0, 1, 0, 1],
                                   [1, 0, 0, 0, 1],
                                   [1, 1, 1, 1, 1]])

    for i in range(8, n - 8):                  # lignes de rythme
        m[6][i] = m[i][6] = 1 - (i % 2)
        reserve[6][i] = reserve[i][6] = True

    m[n - 8][8] = 1                            # le module toujours noir
    reserve[n - 8][8] = True
    for i in range(9):                         # emplacement du format
        if not reserve[8][i]:
            reserve[8][i] = True
        if not reserve[i][8]:
            reserve[i][8] = True
    for i in range(8):
        reserve[8][n - 1 - i] = True
        reserve[n - 1 - i][8] = True
    if version >= 7:                           # emplacement de la version
        for i in range(6):
            for j in range(3):
                reserve[n - 11 + j][i] = True
                reserve[i][n - 11 + j] = True
    return m, reserve


def _poser_donnees(m, reserve, codets):
    n = len(m)
    bits = [(o >> i) & 1 for o in codets for i in range(7, -1, -1)]
    k = 0
    montant = True
    colonne = n - 1
    while colonne > 0:
        if colonne == 6:                       # la colonne de rythme se saute
            colonne -= 1
        lignes = range(n - 1, -1, -1) if montant else range(n)
        for ligne in lignes:
            for dx in (0, 1):
                x = colonne - dx
                if not reserve[ligne][x]:
                    m[ligne][x] = bits[k] if k < len(bits) else 0
                    k += 1
        montant = not montant
        colonne -= 2


_MASQUES = (
    lambda y, x: (y + x) % 2 == 0,
    lambda y, x: y % 2 == 0,
    lambda y, x: x % 3 == 0,
    lambda y, x: (y + x) % 3 == 0,
    lambda y, x: (y // 2 + x // 3) % 2 == 0,
    lambda y, x: (y * x) % 2 + (y * x) % 3 == 0,
    lambda y, x: ((y * x) % 2 + (y * x) % 3) % 2 == 0,
    lambda y, x: ((y + x) % 2 + (y * x) % 3) % 2 == 0,
)


def _penalite(m):
    n = len(m)
    total = 0
    # Règle 1 : les suites de cinq modules de même couleur et plus.
    for bande in list(m) + [list(col) for col in zip(*m)]:
        courant, longueur = bande[0], 1
        for v in bande[1:]:
            if v == courant:
                longueur += 1
            else:
                if longueur >= 5:
                    total += 3 + longueur - 5
                courant, longueur = v, 1
        if longueur >= 5:
            total += 3 + longueur - 5
    # Règle 2 : les carrés 2×2 d'une seule couleur.
    for y in range(n - 1):
        for x in range(n - 1):
            if m[y][x] == m[y][x + 1] == m[y + 1][x] == m[y + 1][x + 1]:
                total += 3
    # Règle 3 : le motif qui imite un œil.
    motifs = ([1, 0, 1, 1, 1, 0, 1, 0, 0, 0, 0],
              [0, 0, 0, 0, 1, 0, 1, 1, 1, 0, 1])
    for bande in list(m) + [list(col) for col in zip(*m)]:
        for i in range(n - 10):
            if list(bande[i:i + 11]) in motifs:
                total += 40
    # Règle 4 : l'écart à la moitié de modules noirs. La formule est celle de
    # la norme, en entiers : le plus petit k tel que la proportion tienne dans
    # [45 - 5k, 55 + 5k] %. Écrite en pourcentage tronqué, elle se décale
    # d'un cran sur certaines matrices et fait choisir un autre masque — un
    # carré qui reste lisible, mais qui n'est plus celui que la norme désigne.
    noirs = sum(sum(ligne) for ligne in m)
    surface = n * n
    k = (abs(noirs * 20 - surface * 10) + surface - 1) // surface - 1
    total += 10 * max(0, k)
    return total


def _poser_format(m, masque):
    """Les quinze bits du format, en deux exemplaires.

    Le placement n'a rien de régulier : il contourne les lignes de rythme, et
    les deux exemplaires ne parcourent pas les bits dans le même ordre. C'est
    la partie du code QR qu'on écrit de travers sans que rien ne le montre —
    le carré reste beau et aucun téléphone ne le lit.
    """
    n = len(m)
    # 0b11 : niveau Q. Le BCH puis le OU exclusif sont ceux de la norme.
    donnees = (0b11 << 3) | masque
    valeur = ((donnees << 10) | _bch(donnees, 0b101_0011_0111, 10)) \
        ^ 0b101_0100_0001_0010

    def bit(i):
        return (valeur >> i) & 1

    for i in range(6):
        m[i][8] = bit(i)
    m[7][8] = bit(6)
    m[8][8] = bit(7)
    m[8][7] = bit(8)
    for i in range(9, 15):
        m[8][14 - i] = bit(i)
    for i in range(8):
        m[8][n - 1 - i] = bit(i)
    for i in range(8, 15):
        m[n - 15 + i][8] = bit(i)
    m[n - 8][8] = 1                            # le module toujours noir


def _poser_version(m, version):
    if version < 7:
        return
    n = len(m)
    valeur = (version << 12) | _bch(version, 0b1_1111_0010_0101, 12)
    for i in range(18):
        b = (valeur >> i) & 1
        m[n - 11 + i % 3][i // 3] = b
        m[i // 3][n - 11 + i % 3] = b


def matrice(texte):
    """La matrice du code QR : une liste de lignes de 0 et de 1."""
    version = _version_pour(len(texte.encode("utf-8")))
    codets = _codets_finaux(texte, version)
    base, reserve = _motifs_fixes(version)
    # Les huit masques sont essayés et le moins pénalisé gagne. **Les huit
    # sont valides** : le masque ne change pas ce que le carré dit, seulement
    # la façon dont les modules se répartissent. La pénalité est une
    # heuristique de lisibilité, et deux implémentations conformes peuvent
    # choisir deux masques différents sur la même donnée — c'est vérifié :
    # matrice par matrice, à masque égal, la nôtre est identique à celle de
    # `segno`, pour les dix versions et les huit masques.
    meilleure, score_min = None, None
    for masque in range(8):
        m = [ligne[:] for ligne in base]
        _poser_donnees(m, reserve, codets)
        for y in range(len(m)):
            for x in range(len(m)):
                if not reserve[y][x] and _MASQUES[masque](y, x):
                    m[y][x] ^= 1
        _poser_format(m, masque)
        _poser_version(m, version)
        score = _penalite(m)
        if score_min is None or score < score_min:
            meilleure, score_min = m, score
    return meilleure


def svg(texte, cote=220, marge=4, couleur="#17181A"):
    """Le code QR en SVG, prêt à poser dans une page.

    La marge de quatre modules n'est pas décorative : sans elle, un lecteur ne
    trouve pas les bords du carré. C'est la panne la plus courante des codes
    QR faits maison, et elle ne se voit pas à l'œil.
    """
    m = matrice(texte)
    n = len(m)
    total = n + 2 * marge
    chemins = []
    for y, ligne in enumerate(m):
        x = 0
        while x < n:
            if ligne[x]:
                debut = x
                while x < n and ligne[x]:
                    x += 1
                chemins.append("M%d %dh%dv1h-%dz"
                               % (debut + marge, y + marge, x - debut,
                                  x - debut))
            else:
                x += 1
    return (
        '<svg xmlns="http://www.w3.org/2000/svg" width="%d" height="%d" '
        'viewBox="0 0 %d %d" shape-rendering="crispEdges" role="img" '
        'aria-label="Code QR de la séance">'
        '<rect width="%d" height="%d" fill="#FFFFFF"/>'
        '<path fill="%s" d="%s"/></svg>'
        % (cote, cote, total, total, total, total, couleur, "".join(chemins))
    )
