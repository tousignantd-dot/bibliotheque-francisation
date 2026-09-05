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

DEBUT, FIN = 61.0, 71.6          # la fenêtre où le tableau est à l'écran
IPS = 30
ENCRE = (23, 24, 26)

# Les pseudonymes de la maison — ceux de la classe de démonstration. Six, dans
# l'ordre alphabétique du tableau, comme les six noms qu'ils remplacent.
PSEUDOS = ["Alouette", "Bambou", "Cactus", "Colibri", "Épinette", "Érable"]

# La légende sous le tableau, réécrite au pseudonyme de la deuxième rangée.
LEGENDE = "%s — le futur simple revient dans 2 scénarios sur 3."

# La zone où chercher la colonne des noms. Large : le tableau bouge.
FENETRE = (150, 150, 700, 820)


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
    seuil = seuil_adaptatif(gris, FENETRE)
    bs = bandes(gris, FENETRE, seuil=seuil)
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
    bs = [(a, b) for a, b in bs if 12 <= (b - a) <= 30]
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
            if not (40 <= moyen <= 110):
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
            cand = [(a, b) for a, b in bandes(gris, FENETRE, seuil=essai_seuil)
                    if 8 <= (b - a) <= 30
                    and (gauche_du_texte(gris, a, b, FENETRE, essai_seuil) or 0)
                    and abs(gauche_du_texte(gris, a, b, FENETRE, essai_seuil)
                            - memoire["x_nom"]) <= 14]
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

    x_nom = min(filter(None, (gauche_du_texte(gris, a, b, FENETRE, seuil)
                              for a, b in rangees)))
    memoire["x_nom"] = x_nom
    # Le bord droit du cache : la gouttière qui sépare les noms de la colonne
    # voisine. Deux bornes, et il faut les deux :
    #  · cherchée sur CHAQUE rangée puis prise au maximum — calculée sur la
    #    seule première, elle laissait le point de « Oleksii P. » à côté
    #    d'« Épinette », le nom le plus long dépassant les autres ;
    #  · sans cette gouttière du tout, le cache mangeait le début de
    #    « Un appel au superviseur ».
    px = gris.load()
    x_fin = x_nom + 40
    for a, b in rangees:
        vide, fin = 0, x_nom + 40
        for x in range(x_nom + 40, FENETRE[2] + 700):
            if any(px[x, y] < seuil + 25 for y in range(a - 2, b + 2)):
                vide = 0
            else:
                vide += 1
                if vide > 26:
                    fin = x - 26
                    break
        x_fin = max(x_fin, fin)
    memoire["x_fin"] = x_fin

    hauteur = max(b - a for a, b in rangees)
    taille = 8
    for t in range(8, 60):
        f = ImageFont.truetype(str(chemin_police), t)
        bb = f.getbbox("A")
        if (bb[3] - bb[1]) >= hauteur - 5:
            taille = t
            break
    fonte = ImageFont.truetype(str(chemin_police), taille)

    d = ImageDraw.Draw(im)

    # La légende sous le tableau nomme le même élève : « Karim H. — le futur
    # simple revient dans 2 scénarios sur 3. » La laisser intacte aurait été le
    # pire des deux mondes — un tableau anonymisé et un nom juste en dessous.
    # Elle se réécrit en entier, en graisse normale, à sa taille mesurée.
    for y0, y1 in bs:
        if y0 <= rangees[-1][1] or (y1 - y0) > 30:
            continue
        gx = gauche_du_texte(gris, y0, y1, (FENETRE[0], y0, 900, y1), seuil)
        if gx is None or gx > x_nom:
            continue
        vide, fin = 0, gx
        for x in range(gx + 20, 1400):
            if any(px[x, y] < seuil + 25 for y in range(y0 - 2, y1 + 2)):
                vide, fin = 0, x
            else:
                vide += 1
                if vide > 30:
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
        fond = im.getpixel((max(0, gx - 12), (y0 + y1) // 2))
        d.rectangle([gx - 6, y0 - 8, fin + 8, y1 + 8], fill=fond)
        bb = f.getbbox(texte)
        encre_l = min((im.getpixel((x, y)) for y in range(y0, y1)
                       for x in range(gx, min(fin, gx + 300), 2)),
                      key=lambda c: c[0] + c[1] + c[2])
        d.text((gx, (y0 + y1) // 2 - (bb[3] + bb[1]) // 2), texte, font=f,
               fill=encre_l)
        break

    for (y0, y1), mot in zip(rangees, PSEUDOS):
        milieu = (y0 + y1) // 2
        fond = im.getpixel((max(0, x_nom - 16), milieu))
        # L'encre se relève sur le texte qu'on efface : pendant un fondu, le
        # nom d'origine n'est qu'un gris clair, et le réécrire en noir plein
        # ferait clignoter la rangée à l'entrée du plan.
        encre = min((im.getpixel((x, y)) for y in range(y0, y1)
                     for x in range(x_nom, min(x_fin, x_nom + 200), 2)),
                    key=lambda c: c[0] + c[1] + c[2])
        d.rectangle([x_nom - 5, y0 - 8, x_fin, y1 + 8], fill=fond)
        bb = fonte.getbbox(mot)
        d.text((x_nom, milieu - (bb[3] + bb[1]) // 2), mot, font=fonte, fill=encre)
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
    px = gris.load()
    fond = max(range(256), key=lambda v: gris.crop((x0, 150, x1, 900)).histogram()[v])
    lignes, dans, d = [], False, 0
    for y in range(150, 900):
        sombre = sum(1 for x in range(x0, x1, 2) if px[x, y] < fond - 6)
        if sombre > 2 and not dans:
            dans, d = True, y
        elif sombre <= 2 and dans:
            dans = False
            if 8 <= y - d <= 30:
                lignes.append((d, y))
    if not lignes:
        return None
    dr = ImageDraw.Draw(im)
    for a, b in lignes:
        couleur = im.getpixel((max(0, x0 - 14), (a + b) // 2))
        dr.rectangle([x0 - 5, a - 6, x1, b + 6], fill=couleur)
    return im


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
    im.crop((150, 150, 900, 830)).resize((1500, 1360), Image.LANCZOS).save(
        dest.with_name(dest.stem + "-zoom.png"))
    print("→ %s" % dest.relative_to(RACINE))
    return 0


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--essai", type=float)
    a = ap.parse_args()
    if a.essai is not None:
        return essai(a.essai)

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
                                                    memoire_finale["x_nom"] + 210))
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
