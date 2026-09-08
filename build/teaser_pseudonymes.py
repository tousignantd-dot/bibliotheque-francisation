#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Remplace les noms d'élèves du film de présentation par des pseudonymes.

    python3 build/teaser_pseudonymes.py --essai 65   # une image, pour juger
    python3 build/teaser_pseudonymes.py              # le film entier

POURQUOI
Le tableau de groupe du film porte « Amina B. », « Karim H. », « Lucía R. » —
prénom et initiale. C'est exactement ce que le portail refuse : un élève y
porte un pseudonyme, jamais son nom. Les noms du film sont fictifs, donc
personne n'est exposé ; mais le film **montre le produit se comporter comme le
dossier Loi 25 promet qu'il ne se comporte pas**, et c'est ce dossier qu'une
direction aura lu avant de le regarder.

CE QUE CE SCRIPT N'EST PAS
Une bonne solution. La bonne solution est de changer six chaînes dans la source
du film et de réexporter : c'est sans perte et ça prend deux minutes. Ceci est
la parade quand la source n'est pas à portée — on repeint six mots dans un
H.264 déjà compressé, et il faut réencoder.

COMMENT
Le plan dure environ neuf secondes et **la caméra zoome lentement** — mesuré :
le bord gauche du tableau dérive de 3,5 px par seconde. Un cache fixe dériverait
donc de trente pixels d'un bout à l'autre. Chaque image est mesurée pour
elle-même : on repère les bandes de texte sombre de la colonne, on couvre
chacune avec **la couleur du fond prise à côté d'elle** — ce qui suit tout seul
la rangée qui passe au vert — et on réécrit le pseudonyme en Nunito, à la
taille déduite de la hauteur de capitale mesurée.

Le cache s'arrête **avant la colonne voisine** : au premier essai il mangeait le
début de « Un appel au superviseur ». La largeur est donc bornée par le début
du texte de la colonne « SCÉNARIO », cherché sur l'image.
"""

import argparse
import pathlib
import shutil
import subprocess
import sys
import tempfile

from PIL import Image, ImageDraw, ImageFont

RACINE = pathlib.Path(__file__).resolve().parent.parent
FILM = RACINE / "assets" / "tutoriels" / "teaser-francis.mp4"
POLICE_SRC = RACINE / "assets" / "design-system" / "fonts" / "nunito-latin.woff2"

IPS = 30
ENCRE = (23, 24, 26)

# ── L'échelle, et pourquoi elle existe ───────────────────────────────────────
# Tout ce fichier a été mesuré sur un export **1920×1080**. Le second export,
# remis le 7 septembre 2026, est arrivé en **1280×720** : hauteur de rangée,
# gouttière, fenêtre de recherche — pas une seule de ces mesures ne tombait
# plus, et le script ne détectait rien du tout sans rien signaler. Les
# longueurs sont donc écrites dans l'étalon 1080 et ramenées à la hauteur
# réelle du film par `px()`.
HAUTEUR_ETALON = 1080

# La fenêtre où chercher la colonne des noms, en **fractions de l'image**. Un
# rectangle en pixels ne survit pas à un changement de définition, et un
# rectangle simplement mis à l'échelle ne survit pas à un recadrage : le
# nouveau montage ne cadre pas le tableau comme l'ancien. Large des deux
# côtés — c'est `gauche_du_texte()` qui trouve la colonne, pas ce cadre.
FENETRE_REL = (0.078, 0.139, 0.500, 0.833)

_TAILLE = None


def taille_du_film():
    """(largeur, hauteur) du film, demandées à ffprobe une seule fois."""
    global _TAILLE
    if _TAILLE is None:
        sortie = subprocess.run(
            ["ffprobe", "-v", "error", "-select_streams", "v:0",
             "-show_entries", "stream=width,height", "-of", "csv=p=0:s=x",
             str(FILM)], capture_output=True, text=True, check=True)
        l, h = sortie.stdout.strip().split("x")
        _TAILLE = (int(l), int(h))
    return _TAILLE


def px(valeur):
    """Une longueur mesurée sur l'étalon 1080, ramenée à ce film-ci."""
    return max(1, int(round(valeur * taille_du_film()[1] / HAUTEUR_ETALON)))

# Les pseudonymes de la maison — ceux de la classe de démonstration. Six, dans
# l'ordre alphabétique du tableau, comme les six noms qu'ils remplacent.
PSEUDOS = ["Alouette", "Bambou", "Cactus", "Colibri", "Épinette", "Érable"]

# La légende sous le tableau, réécrite au pseudonyme de la deuxième rangée.
LEGENDE = "%s — le futur simple revient dans 2 scénarios sur 3."

def fenetre():
    """La zone où chercher la colonne des noms, pour ce film-ci."""
    l, h = taille_du_film()
    x0, y0, x1, y1 = FENETRE_REL
    return (int(x0 * l), int(y0 * h), int(x1 * l), int(y1 * h))


def police(dossier, graisse, nom):
    """Nunito en graisse 800 — celle des noms du tableau. La police du dépôt
    est variable (axe wght 200→1000) : on l'instancie plutôt que d'en chercher
    une autre, pour que le film garde la police du système de design."""
    from fontTools.ttLib import TTFont
    from fontTools.varLib import instancer
    f = TTFont(POLICE_SRC)
    f.flavor = None
    dest = dossier / nom
    instancer.instantiateVariableFont(f, {"wght": graisse}).save(dest)
    return dest


def seuil_adaptatif(gris, fenetre):
    """Le niveau au-dessous duquel un pixel est « du texte », pour CETTE image.

    Un seuil fixe à 120 marche sur le plan établi et devient aveugle pendant
    les fondus : le tableau y est à demi transparent, ses lettres ne sont plus
    qu'un gris clair sur le crème. Cinquante images sur trois cent dix-huit
    sont ainsi ressorties avec les vrais noms — au début et à la fin du plan,
    c'est-à-dire là où l'œil les cherche.
    """
    ext = gris.crop(fenetre)
    h = ext.histogram()
    total = sum(h)
    # Le fond est le niveau le plus représenté ; le texte est ce qui s'en
    # détache franchement vers le bas.
    fond = max(range(256), key=lambda v: h[v])
    sombre = min((v for v in range(256) if h[v] and v < fond), default=fond)
    return max(40, int(fond - max(16, (fond - sombre) * 0.35)))


def bandes(gris, fenetre, seuil=120, mini=3):
    """Les bandes horizontales de texte sombre, dans la fenêtre donnée."""
    x0, y0, x1, y1 = fenetre
    px = gris.crop(fenetre).load()
    w, h = x1 - x0, y1 - y0
    out, dans, d = [], False, 0
    for y in range(h):
        n = sum(1 for x in range(w) if px[x, y] < seuil)
        if n > mini and not dans:
            dans, d = True, y
        elif n <= mini and dans:
            dans = False
            if y - d >= 6:
                out.append((d + y0, y + y0))
    return out


def gauche_du_texte(gris, y0, y1, fenetre, seuil=120):
    x0, x1 = fenetre[0], fenetre[2]
    px = gris.load()
    for x in range(x0, x1):
        if any(px[x, y] < seuil for y in range(y0, y1)):
            return x
    return None


def patcher(im, chemin_police, chemin_police_normale, memoire=None):
    memoire = {} if memoire is None else memoire
    """Rend l'image corrigée, ou None si le tableau n'y est pas."""
    gris = im.convert("L")
    FEN = fenetre()
    seuil = seuil_adaptatif(gris, FEN)
    bs = bandes(gris, FEN, seuil=seuil, mini=px(3))
    # On veut six rangées de noms. Le titre et l'en-tête « APPRENANT » entrent
    # aussi dans la fenêtre : les rangées sont les six DERNIÈRES bandes
    # régulièrement espacées.
    if len(bs) < 2:
        return None
    # Six bandes RÉGULIÈREMENT espacées, cherchées parmi toutes. Prendre « les
    # six dernières » marchait tant que le tableau était seul ; dès la huitième
    # seconde, la légende « Karim H. — le futur simple… » paraît sous lui et
    # devient la dernière bande : on aurait renommé la légende et laissé la
    # première rangée intacte, sans qu'aucune erreur ne le dise.
    # L'en-tête « APPRENANT » est en petites capitales : sa bande fait dix
    # pixels de haut quand une rangée de nom en fait dix-neuf. Sans ce tri, il
    # entre dans le groupe régulier — l'écart en-tête/première rangée ne
    # diffère que de 12 % des autres, et « Alouette » s'est écrit SUR l'en-tête
    # pendant que « Fatou D. » restait en bas. La hauteur les sépare
    # franchement ; l'espacement, non.
    # Une rangée de nom fait entre douze et trente pixels de haut. En dessous
    # c'est l'en-tête « APPRENANT », en petites capitales ; au-dessus c'est le
    # titre « Tout le groupe, d'un coup d'œil », qui fait cinquante-deux pixels
    # et se glissait dans le groupe pendant l'entrée du tableau — d'où trois
    # bandes « régulières » qui ne l'étaient pas, et douze images sorties avec
    # les vrais noms au moment précis où l'œil arrive sur le plan.
    bs = [(a, b) for a, b in bs if px(12) <= (b - a) <= px(30)]
    if len(bs) < 2:
        return None
    # Le tableau N'ARRIVE PAS D'UN COUP : ses rangées entrent l'une après
    # l'autre, du haut vers le bas, sur une seconde environ. Exiger six bandes
    # régulières laissait donc intactes toutes les images de cette entrée —
    # et « Amina B. », « Karim H. », « Lucía R. » y sont parfaitement lisibles,
    # au moment même où l'œil arrive sur le plan. On accepte maintenant un
    # groupe PARTIEL, de trois à six rangées, et on l'apparie aux pseudonymes
    # du haut vers le bas : les rangées manquantes sont toujours celles du bas.
    rangees = None
    for n in range(6, 1, -1):
        for d in range(len(bs) - n + 1):
            grp = bs[d:d + n]
            ecarts = [grp[i + 1][0] - grp[i][0] for i in range(n - 1)]
            moyen = sum(ecarts) / len(ecarts)
            if not (px(40) <= moyen <= px(110)):
                continue
            if max(abs(e - moyen) for e in ecarts) <= moyen * 0.12:
                rangees = grp
                break
        if rangees:
            break
    if rangees is None and memoire.get("x_nom"):
        # Repli guidé. Aux deux extrémités du plan, le tableau entre rangée par
        # rangée puis s'efface : jamais six bandes régulières, et pendant la
        # sortie le fond change tellement que le seuil calculé sur l'histogramme
        # part à 231 et ne voit plus rien. On reprend alors la colonne connue de
        # l'image précédente — la caméra ne bouge que de 0,12 px par image — et
        # on accepte toute bande qui commence à cet endroit-là.
        # Les toutes premières images du fondu portent un texte à peine plus
        # foncé que le fond : il faut monter très haut pour le voir.
        for essai_seuil in (seuil, 200, 215, 228, 238):
            cand = [(a, b) for a, b in bandes(gris, FEN, seuil=essai_seuil,
                                              mini=px(3))
                    if px(8) <= (b - a) <= px(30)
                    and (gauche_du_texte(gris, a, b, FEN, essai_seuil) or 0)
                    and abs(gauche_du_texte(gris, a, b, FEN, essai_seuil)
                            - memoire["x_nom"]) <= px(14)]
            # Une seule rangée suffit dans le repli : à la toute première
            # image du tableau, « Amina B. » paraît seule, et c'est justement
            # celle-là qu'il ne faut pas laisser passer. Le risque de faux
            # positif reste faible — la bande doit commencer à quatorze pixels
            # près de la colonne connue de l'image voisine.
            if len(cand) >= 1:
                rangees, seuil = cand[:6], essai_seuil
                break
    if rangees is None:
        return None

    x_nom = min(filter(None, (gauche_du_texte(gris, a, b, FEN, seuil)
                              for a, b in rangees)))
    memoire["x_nom"] = x_nom
    # Le bord droit du cache : la gouttière qui sépare les noms de la colonne
    # voisine. Deux bornes, et il faut les deux :
    #  · cherchée sur CHAQUE rangée puis prise au maximum — calculée sur la
    #    seule première, elle laissait le point de « Oleksii P. » à côté
    #    d'« Épinette », le nom le plus long dépassant les autres ;
    #  · sans cette gouttière du tout, le cache mangeait le début de
    #    « Un appel au superviseur ».
    pix = gris.load()
    largeur = taille_du_film()[0]
    x_fin = x_nom + px(40)
    for a, b in rangees:
        vide, fin = 0, x_nom + px(40)
        for x in range(x_nom + px(40), min(largeur, FEN[2] + px(700))):
            if any(pix[x, y] < seuil + 25 for y in range(a - px(2), b + px(2))):
                vide = 0
            else:
                vide += 1
                if vide > px(26):
                    fin = x - px(26)
                    break
        x_fin = max(x_fin, fin)
    # La gouttière ne se mesure plus pendant un fondu : le texte y est à peine
    # plus foncé que le fond, la recherche ne trouve donc rien et le cache se
    # réduit à sa largeur minimale — d'où, à la sortie du plan, « Bambou »
    # écrit par-dessus « Karim » et le « H. » d'origine resté à côté, sur six
    # rangées à la fois. On garde la plus grande LARGEUR mesurée sur ce plan,
    # jamais la position : la colonne dérive avec le zoom, sa largeur non.
    memoire["largeur_nom"] = max(memoire.get("largeur_nom", 0), x_fin - x_nom)
    x_fin = max(x_fin, x_nom + memoire["largeur_nom"])
    memoire["x_fin"] = x_fin

    hauteur = max(b - a for a, b in rangees)
    taille = 8
    for t in range(6, 60):
        f = ImageFont.truetype(str(chemin_police), t)
        bb = f.getbbox("A")
        if (bb[3] - bb[1]) >= hauteur - px(5):
            taille = t
            break
    fonte = ImageFont.truetype(str(chemin_police), taille)

    d = ImageDraw.Draw(im)

    # La légende sous le tableau nomme le même élève : « Karim H. — le futur
    # simple revient dans 2 scénarios sur 3. » La laisser intacte aurait été le
    # pire des deux mondes — un tableau anonymisé et un nom juste en dessous.
    # Elle se réécrit en entier, en graisse normale, à sa taille mesurée.
    for y0, y1 in bs:
        if y0 <= rangees[-1][1] or (y1 - y0) > px(30):
            continue
        gx = gauche_du_texte(gris, y0, y1, (FEN[0], y0, min(largeur, px(900)), y1),
                             seuil)
        if gx is None or gx > x_nom:
            continue
        vide, fin = 0, gx
        for x in range(gx + px(20), largeur):
            if any(pix[x, y] < seuil + 25 for y in range(y0 - px(2), y1 + px(2))):
                vide, fin = 0, x
            else:
                vide += 1
                if vide > px(30):
                    break
        # La taille se règle sur la LARGEUR de la ligne d'origine, pas sur sa
        # hauteur : réglée en hauteur, la ligne sortait tassée — « revientdans
        # 2scénarios » — parce que le film porte un léger interlettrage que
        # notre rendu n'a pas. En visant la largeur, l'œil retrouve le rythme.
        texte = LEGENDE % PSEUDOS[1]
        vise = (fin - gx) * (len(texte) / max(1, len(LEGENDE % "Karim H.")))
        t, ecart = 12, None
        for tt in range(8, 40):
            f = ImageFont.truetype(str(chemin_police_normale), tt)
            l = f.getbbox(texte)[2]
            if ecart is None or abs(l - vise) < ecart:
                ecart, t = abs(l - vise), tt
        f = ImageFont.truetype(str(chemin_police_normale), t)
        fond = im.getpixel((max(0, gx - px(12)), (y0 + y1) // 2))
        # L'encre se relève AVANT d'effacer, comme pour les rangées. Elle se
        # relevait après : on échantillonnait le rectangle qu'on venait de
        # peindre, la légende était donc réécrite dans la couleur du fond —
        # c'est-à-dire effacée. Sur le 1080 la ligne paraissait tard dans le
        # plan et le défaut n'a jamais été regardé ; sur le 1280×720 il laisse
        # un blanc là où une phrase était.
        encre_l = min((im.getpixel((x, y)) for y in range(y0, y1)
                       for x in range(gx, min(fin, gx + px(300)), 2)),
                      key=lambda c: c[0] + c[1] + c[2])
        d.rectangle([gx - px(6), y0 - px(8), fin + px(8), y1 + px(8)], fill=fond)
        bb = f.getbbox(texte)
        d.text((gx, (y0 + y1) // 2 - (bb[3] + bb[1]) // 2), texte, font=f,
               fill=encre_l)
        break

    for (y0, y1), mot in zip(rangees, PSEUDOS):
        milieu = (y0 + y1) // 2
        fond = im.getpixel((max(0, x_nom - px(16)), milieu))
        # L'encre se relève sur le texte qu'on efface : pendant un fondu, le
        # nom d'origine n'est qu'un gris clair, et le réécrire en noir plein
        # ferait clignoter la rangée à l'entrée du plan.
        encre = min((im.getpixel((x, y)) for y in range(y0, y1)
                     for x in range(x_nom, min(x_fin, x_nom + px(200)), 2)),
                    key=lambda c: c[0] + c[1] + c[2])
        d.rectangle([x_nom - px(5), y0 - px(8), x_fin, y1 + px(8)], fill=fond)
        bb = fonte.getbbox(mot)
        d.text((x_nom, milieu - (bb[3] + bb[1]) // 2), mot, font=fonte, fill=encre)

    # ── La rangée qui n'est pas encore arrivée ──────────────────────────────
    # Le tableau se pose rangée par rangée. Celle qui entre est plus pâle que
    # les autres : elle ne rejoint pas le groupe régulier, donc elle n'est pas
    # repeinte — et « Thanh N. » restait parfaitement lisible sur l'image même
    # où le plan se pose. Sous la dernière rangée traitée, on efface donc tout
    # ce qui reste dans la colonne des noms. Rien n'est réécrit : sur un fondu
    # d'entrée, une case vide se lit comme une case qui n'est pas encore
    # arrivée, alors qu'un pseudonyme posé sur une géométrie non mesurée se
    # verrait de travers.
    if len(rangees) < 6:
        # On n'essaie plus de *voir* les rangées manquantes : à quelques pour
        # cent d'opacité, une détection les rate une fois sur trente, et il
        # suffit d'une image pour qu'un nom paraisse. On efface donc la colonne
        # par BANDES RÉGULIÈRES, du pas mesuré, depuis la première rangée
        # traitée jusqu'au bas de la fenêtre — sans rien chercher. Un rectangle
        # de la couleur du fond posé sur du fond ne se voit pas ; un nom laissé
        # une image, oui.
        if len(rangees) >= 2:
            memoire["pas"] = (rangees[-1][0] - rangees[0][0]) / (len(rangees) - 1)
        pas = memoire.get("pas")
        if pas and pas > px(10):
            haut = rangees[0][0] - px(4)
            y = haut
            while y < FEN[3] - px(6):
                milieu = int(y + pas / 2)
                if not any(milieu >= a - px(6) and milieu <= b + px(6)
                           for a, b in rangees):
                    couleur = im.getpixel((max(0, x_nom - px(16)),
                                           min(milieu, im.height - 1)))
                    d.rectangle([x_nom - px(5), int(y), x_fin,
                                 int(min(y + pas - px(2), FEN[3]))], fill=couleur)
                y += pas
    return im


def effacer_colonne(im, x0, x1):
    """Dernier recours : effacer tout texte de la colonne des noms.

    Les toutes premières images de l'entrée du tableau ne se laissent pas
    mesurer — une seule rangée, à peine plus foncée que le fond, dans un
    tableau qui n'a pas fini de grandir. Plutôt que d'y laisser « Amina B. »
    paraître un quart de seconde, on efface la colonne : pendant un fondu
    d'entrée, une case encore vide se lit comme une case qui n'est pas encore
    arrivée. Rien n'est écrit à la place — inventer un pseudonyme sur une
    géométrie qu'on n'a pas mesurée le poserait de travers.
    """
    gris = im.convert("L")
    pix = gris.load()
    haut, bas = px(150), min(taille_du_film()[1], px(900))
    fond = max(range(256), key=lambda v: gris.crop((x0, haut, x1, bas)).histogram()[v])
    lignes, dans, d = [], False, 0
    for y in range(haut, bas):
        # `fond - 3` et `sombre > 1` : à la sortie du plan, le tableau se
        # dissout jusqu'à quelques pour cent d'opacité, et un seuil plus franc
        # laissait passer « Karim H. » et « Fatou D. » sur les deux dernières
        # images. Un faux positif ici ne coûte qu'un rectangle de la couleur du
        # fond, posé sur du fond.
        sombre = sum(1 for x in range(x0, x1, 2) if pix[x, y] < fond - 3)
        if sombre > 1 and not dans:
            dans, d = True, y
        elif sombre <= 1 and dans:
            dans = False
            if px(8) <= y - d <= px(30):
                lignes.append((d, y))
    if not lignes:
        return None
    dr = ImageDraw.Draw(im)
    for a, b in lignes:
        couleur = im.getpixel((max(0, x0 - px(14)), (a + b) // 2))
        dr.rectangle([x0 - px(5), a - px(6), x1, b + px(6)], fill=couleur)
    return im


def rangees_visibles(im):
    """Le nombre de rangées de noms régulièrement espacées dans cette image.

    Sert à trouver le plan tout seul. C'est la même mesure que `patcher()`,
    sans le dessin : un tableau qu'on sait repeindre est un tableau qu'on sait
    reconnaître.
    """
    gris = im.convert("L")
    FEN = fenetre()
    seuil = seuil_adaptatif(gris, FEN)
    bs = [(a, b) for a, b in bandes(gris, FEN, seuil=seuil, mini=px(3))
          if px(8) <= (b - a) <= px(30)]
    for n in range(6, 2, -1):
        for d in range(len(bs) - n + 1):
            grp = bs[d:d + n]
            ecarts = [grp[i + 1][0] - grp[i][0] for i in range(n - 1)]
            moyen = sum(ecarts) / len(ecarts)
            if not (px(28) <= moyen <= px(110)):
                continue
            if max(abs(e - moyen) for e in ecarts) <= moyen * 0.12:
                return n
    return 0


def trouver_le_plan(pas=0.2, marge=1.0):
    """Cherche dans tout le film la fenêtre où le tableau de groupe paraît.

    Elle était écrite en dur — 61,0 à 71,6 s — et le second montage l'a
    déplacée de huit secondes en plus de changer de définition. Deux mesures à
    refaire à la main au prochain export, c'est une de trop : on balaie le
    film et on prend le plus long passage où six rangées régulières se lisent.
    Les groupes de trois ou quatre ne comptent pas ici — d'autres écrans du
    film en donnent, et seule la table de groupe en a six.

    La marge est large (une seconde) parce que le tableau se pose rangée par
    rangée : à un dixième de seconde du bord, « Amina B. » et « Karim H. »
    sont déjà lisibles alors que six rangées régulières ne le sont pas encore.
    """
    tmp = pathlib.Path(tempfile.mkdtemp())
    subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-i", str(FILM),
                    "-vf", "fps=%g" % (1 / pas), str(tmp / "%05d.png")], check=True)
    fichiers = sorted(tmp.glob("*.png"))
    vus = [(i * pas, rangees_visibles(Image.open(f).convert("RGB")))
           for i, f in enumerate(fichiers)]
    passages, debut = [], None
    for t, n in vus + [(len(vus) * pas, 0)]:
        if n >= 6 and debut is None:
            debut = t
        elif n < 6 and debut is not None:
            passages.append((debut, t))
            debut = None
    if not passages:
        raise SystemExit("Aucun tableau de six rangées trouvé dans le film.")
    d, f = max(passages, key=lambda p: p[1] - p[0])
    # La marge attrape l'entrée et la sortie du tableau, où les rangées
    # arrivent une à une : ce sont justement les images où les vrais noms se
    # lisent, et `patcher()` sait les traiter par son repli guidé.
    return max(0.0, d - marge), f + marge


def essai(seconde):
    tmp = pathlib.Path(tempfile.mkdtemp())
    pol = police(tmp, 800, "b.ttf")
    nor = police(tmp, 400, "r.ttf")
    src = tmp / "f.png"
    subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-ss", str(seconde),
                    "-i", str(FILM), "-frames:v", "1", str(src)], check=True)
    im = patcher(Image.open(src).convert("RGB"), pol, nor)
    if im is None:
        print("tableau non détecté à %s s" % seconde)
        return 1
    dest = RACINE / "essais" / ("teaser-pseudos-%s.png" % seconde)
    dest.parent.mkdir(exist_ok=True)
    im.save(dest)
    im.crop((px(150), px(150), px(900), px(830))).resize(
        (1500, 1360), Image.LANCZOS).save(
        dest.with_name(dest.stem + "-zoom.png"))
    print("→ %s" % dest.relative_to(RACINE))
    return 0


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--essai", type=float)
    ap.add_argument("--fenetre", action="store_true",
                    help="dire où est le plan, sans rien produire")
    ap.add_argument("--de", type=float, help="forcer le début du plan")
    ap.add_argument("--a", type=float, dest="jusqua", help="forcer la fin")
    a = ap.parse_args()
    if a.essai is not None:
        return essai(a.essai)

    l, h = taille_du_film()
    if a.de is not None and a.jusqua is not None:
        DEBUT, FIN = a.de, a.jusqua
    else:
        print("Recherche du plan dans %s (%d×%d)…" % (FILM.name, l, h))
        DEBUT, FIN = trouver_le_plan()
    print("Le tableau est à l'écran de %.1f à %.1f s." % (DEBUT, FIN))
    if a.fenetre:
        return 0

    tmp = pathlib.Path(tempfile.mkdtemp())
    pol = police(tmp, 800, "b.ttf")
    nor = police(tmp, 400, "r.ttf")
    images = tmp / "img"
    images.mkdir()
    print("Extraction du plan (%.1f → %.1f s)…" % (DEBUT, FIN))
    subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-ss", str(DEBUT),
                    "-t", str(FIN - DEBUT), "-i", str(FILM),
                    "-vsync", "0", str(images / "%05d.png")], check=True)
    fichiers = sorted(images.glob("*.png"))
    faits = 0
    # DEUX PASSES, en avant puis en arrière. La mémoire de géométrie ne sert
    # qu'aux images qui suivent une réussite ; or les plus gênantes — l'entrée
    # du tableau, où les vrais noms sont parfaitement lisibles — viennent AVANT
    # la première. Une seule passe les laissait toutes.
    reste, memoire_finale = list(fichiers), {}
    for sens in ("avant", "arrière"):
        memoire, encore = {}, []
        for f in (reste if sens == "avant" else reversed(reste)):
            im = patcher(Image.open(f).convert("RGB"), pol, nor, memoire)
            if im is None:
                encore.append(f)
            else:
                im.save(f)
                faits += 1
        reste = encore
        if memoire.get("x_nom"):
            memoire_finale = memoire
        if not reste:
            break
    if reste and memoire_finale.get("x_nom"):
        efface = 0
        for f in reste:
            im = effacer_colonne(Image.open(f).convert("RGB"),
                                 memoire_finale["x_nom"],
                                 memoire_finale.get("x_fin",
                                                    memoire_finale["x_nom"] + px(210)))
            if im is not None:
                im.save(f)
                efface += 1
        print("  %d images sans tableau mesurable : colonne effacée sur %d"
              % (len(reste), efface))
    print("  %d images sur %d corrigées" % (faits, len(fichiers)))
    if not faits:
        print("Aucune image corrigée — rien à remonter.")
        return 1

    # Trois segments, tous réencodés avec les MÊMES réglages : c'est ce qui
    # permet au concat de recoller sans saut. Le son ne bouge pas, il est
    # recopié du film d'origine à la toute fin.
    reglages = ["-c:v", "libx264", "-preset", "slow", "-crf", "16",
                "-pix_fmt", "yuv420p", "-r", str(IPS), "-an"]
    a1, a2, a3 = tmp / "a.mp4", tmp / "b.mp4", tmp / "c.mp4"
    subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-i", str(FILM),
                    "-t", str(DEBUT)] + reglages + [str(a1)], check=True)
    subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-framerate", str(IPS),
                    "-i", str(images / "%05d.png")] + reglages + [str(a2)], check=True)
    subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-ss", str(FIN),
                    "-i", str(FILM)] + reglages + [str(a3)], check=True)
    liste = tmp / "liste.txt"
    liste.write_text("".join("file '%s'\n" % p for p in (a1, a2, a3)))
    muet = tmp / "muet.mp4"
    subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-f", "concat",
                    "-safe", "0", "-i", str(liste), "-c", "copy", str(muet)],
                   check=True)
    dest = FILM.with_name("teaser-francis-pseudos.mp4")
    subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-i", str(muet),
                    "-i", str(FILM), "-map", "0:v", "-map", "1:a",
                    "-c:v", "copy", "-c:a", "copy", "-shortest", str(dest)],
                   check=True)
    shutil.rmtree(tmp, ignore_errors=True)
    d = subprocess.run(["ffprobe", "-v", "error", "-show_entries",
                        "format=duration", "-of", "csv=p=0", str(dest)],
                       capture_output=True, text=True).stdout.strip()
    print("→ %s · %.1f Mo · %s s" % (dest.name, dest.stat().st_size / 1e6, d))
    return 0


if __name__ == "__main__":
    sys.exit(main())
