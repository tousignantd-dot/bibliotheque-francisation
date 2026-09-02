#!/usr/bin/env python3
"""Monte les capsules à partir des films d'écran.

Ce que ça change par rapport au montage d'images fixes : la durée de chaque
image vient de son horodatage réel, relevé pendant le tournage. Le
`screencast` de Chrome n'émet une image que lorsque la page change — un
écran immobile n'en produit aucune. Poser une cadence constante ferait donc
défiler les mouvements trop vite et escamoterait les temps d'arrêt.

Trois pièces montées bout à bout :
  carton de titre → film de la capsule → carton de fin,
plus la narration mixée en une seule piste, et un fichier de sous-titres.

`python3 monter_film.py [idCapsule]`
"""
import json
import subprocess
import sys
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

ICI = Path(__file__).parent
FILMS, VOIX = ICI / "films", ICI / "voix"
TRAVAIL, SORTIE = ICI / "travail", ICI / "capsules"
L, H, IPS = 1920, 1080, 30
CRF = 23          # défaut ; une capsule peut le relever dans le manifeste
RESPIRATION = 0.7
LOGO_S, TITRE_S, FIN_S = 1.8, 2.6, 2.2

ENCRE = (23, 24, 26)
PAPIER = (247, 247, 245)
BLANC = (255, 255, 255)
VERT = (10, 143, 91)
GRIS = (110, 113, 117)
MARQUE = (107, 79, 187)        # --marque-600
TRAIT = (240, 240, 238)        # --marque-trait


def duree(f):
    return float(subprocess.run(
        ["ffprobe", "-v", "error", "-show_entries", "format=duration",
         "-of", "default=nw=1:nk=1", str(f)],
        capture_output=True, text=True, check=True).stdout.strip())


NUNITO = None


def nunito(taille, poids=900):
    """Nunito à la taille et au poids demandés, tirée du dépôt.

    Le logotype ne se dessine PAS dans une police de repli : sans Nunito, le
    « ı » sans point change de chasse et la marque se lit de travers — c'est
    exactement le défaut signalé le 2 septembre. Le dépôt versionne la police
    en `.woff2` (variable, 400→900) ; Pillow ne lit pas le woff2, alors on la
    déflate une fois dans `travail/`. Renvoie None si la conversion échoue,
    et l'appelant retombe alors sur `police()`.
    """
    global NUNITO
    if NUNITO is None:
        ttf = TRAVAIL / "nunito-variable.ttf"
        try:
            if not ttf.exists():
                from fontTools.ttLib import TTFont
                f = TTFont(ICI.parent.parent
                           / "assets/design-system/fonts/nunito-latin.woff2")
                f.flavor = None
                TRAVAIL.mkdir(exist_ok=True)
                f.save(str(ttf))
            NUNITO = ttf
        except Exception as e:                     # fontTools ou brotli absent
            print("  (Nunito indisponible : %s)" % e)
            NUNITO = False
    if not NUNITO:
        return None
    f = ImageFont.truetype(str(NUNITO), taille)
    f.set_variation_by_axes([poids])
    return f


def logotype(d, centre_x, ligne_base, nom_px, avec_descripteur=True):
    """Dessine le logotype francis : le nom, le trait, le descripteur.

    Il n'existe aucune image de la marque, et c'est voulu — elle se compose,
    elle ne se colle pas. Le seul signe est **le point du « i »** : le nom est
    écrit avec « ı » (U+0131) et le disque mauve est posé par-dessus, centré
    sur la chasse du glyphe et calé sur le haut de sa hampe. Les proportions
    sont celles de `marque-francis.css`, ramenées à des fractions du corps :
    disque 1/4, gouttière 4/7, trait 5/6 de haut.

    Renvoie la largeur dessinée.
    """
    fn = nunito(nom_px, 900)
    fd = nunito(round(nom_px * 20 / 36), 900)
    if fn is None:
        return 0
    nom, desc = "francıs", "Aide à l'apprentissage du français"
    # `letter-spacing` négatif : Pillow ne l'a pas, on avance lettre à lettre.
    sn, sd = -0.035 * nom_px, -0.015 * fd.size

    def largeur(f, texte, serrage):
        return sum(f.getlength(c) + serrage for c in texte) - serrage

    l_nom = largeur(fn, nom, sn)
    gouttiere = round(nom_px * 16 / 28)
    h_trait = round(nom_px * 30 / 36)
    e_trait = max(2, round(nom_px / 18))
    l_desc = largeur(fd, desc, sd) if avec_descripteur else 0
    total = l_nom + (gouttiere * 2 + e_trait + l_desc if avec_descripteur else 0)

    x = centre_x - total / 2
    depart = x
    pos_i = None
    for c in nom:
        if c == "ı":
            pos_i = (x, fn.getlength(c))
        d.text((x, ligne_base), c, font=fn, fill=ENCRE, anchor="ls")
        x += fn.getlength(c) + sn
    # Le disque : diamètre au quart du corps, centré sur la chasse du « ı »,
    # posé juste au-dessus de la hampe — dont le haut est relevé dans la
    # police, jamais estimé.
    if pos_i:
        xi, li = pos_i
        _, haut, _, bas = fn.getbbox("ı")     # relevé dans la police même
        stem = ligne_base - (bas - haut)       # haut de la hampe
        r = nom_px * 0.25 / 2
        cy = stem - nom_px * 0.015 - r
        d.ellipse([xi + li / 2 - r, cy - r, xi + li / 2 + r, cy + r],
                  fill=MARQUE)
    if avec_descripteur:
        x += gouttiere
        d.rectangle([x, ligne_base - h_trait * 0.72,
                     x + e_trait, ligne_base + h_trait * 0.28], fill=TRAIT)
        x += e_trait + gouttiere
        for c in desc:
            d.text((x, ligne_base), c, font=fd, fill=MARQUE, anchor="ls")
            x += fd.getlength(c) + sd
    return x - depart


def carton_logo(chemin):
    """Le premier écran de chaque capsule : la marque, seule, sur du blanc."""
    img = Image.new("RGB", (L, H), BLANC)
    d = ImageDraw.Draw(img)
    d.rectangle([0, 0, L, 10], fill=VERT)
    logotype(d, L / 2, H / 2 + 26, 88)
    img.save(chemin)


def police(taille, gras=True):
    """Nunito est la police du système de design.

    Elle vient du dépôt (`nunito()`), et non plus d'une installation dans le
    système : les cartons de titre sortaient en Helvetica sur un poste où
    Nunito n'est pas installée — donc partout — pendant que le carton de
    marque, lui, la tirait du dépôt. Deux polices dans le même film.
    On retombe sur la police du système en dernier recours : un carton
    illisible vaut mieux qu'un montage qui s'arrête.
    """
    f = nunito(taille, 900 if gras else 700)
    if f is not None:
        return f
    for nom in (("Nunito-Black.ttf", "Nunito-Bold.ttf") if gras
                else ("Nunito-SemiBold.ttf", "Nunito-Regular.ttf")):
        for base in (Path.home() / "Library/Fonts", Path("/Library/Fonts")):
            if (base / nom).exists():
                return ImageFont.truetype(str(base / nom), taille)
    for repli in ("/System/Library/Fonts/Helvetica.ttc",
                  "/System/Library/Fonts/Supplemental/Arial.ttf"):
        if Path(repli).exists():
            return ImageFont.truetype(repli, taille)
    return ImageFont.load_default()


def carton(chemin, surtitre, titre, pied=None, inverse=False):
    fond, encre = (ENCRE, PAPIER) if inverse else (PAPIER, ENCRE)
    img = Image.new("RGB", (L, H), fond)
    d = ImageDraw.Draw(img)
    d.rectangle([0, 0, L, 10], fill=VERT)
    d.text((140, H / 2 - 150), surtitre.upper(), font=police(26), fill=VERT)
    y = H / 2 - 95
    for ligne in titre.split("\n"):
        d.text((140, y), ligne, font=police(76), fill=encre)
        y += 92
    if pied:
        d.text((140, H / 2 + 130), pied, font=police(30, gras=False),
               fill=PAPIER if inverse else GRIS)
    img.save(chemin)


def segment_fixe(image, secondes, sortie):
    subprocess.run([
        "ffmpeg", "-y", "-loglevel", "error", "-loop", "1", "-framerate", str(IPS),
        "-t", f"{secondes:.3f}", "-i", str(image),
        "-f", "lavfi", "-t", f"{secondes:.3f}", "-i", "anullsrc=r=48000:cl=stereo",
        "-vf", f"scale={L}:{H},format=yuv420p",
        "-c:v", "libx264", "-preset", "medium", "-crf", "20",
        "-c:a", "aac", "-b:a", "160k", "-ar", "48000", "-ac", "2",
        "-shortest", str(sortie),
    ], check=True)


def horodatage(s):
    h, r = divmod(s, 3600)
    m, r = divmod(r, 60)
    return f"{int(h):02d}:{int(m):02d}:{r:06.3f}"


def monter(capsule, decalage_titre):
    dossier = FILMS / capsule["id"]
    releve = json.loads((dossier / "images.json").read_text())
    images, reperes = releve["images"], releve["reperes"]
    if not images:
        raise SystemExit(f"{capsule['id']} : aucune image filmée")

    t0 = images[0]["t"]

    # Chrome n'émet une image que lorsque la page change, mais il l'émet par
    # rafales : dix images peuvent porter presque le même horodatage. Leur
    # imposer un plancher d'une image de sortie chacune allongeait la rafale
    # et le film prenait du retard sur la voix — jusqu'à 46 s en fin de
    # capsule 7, mesuré. Une rafale plus serrée que 1/30 s ne peut de toute
    # façon pas être montrée : on garde une image sur la rafale, et la durée
    # totale reste celle du tournage.
    gardees = [images[0]]
    for im in images[1:]:
        if im["t"] - gardees[-1]["t"] >= 1.0 / IPS:
            gardees.append(im)

    total = reperes[-1]["fin"] / 1000.0 - t0 + RESPIRATION
    lignes = []
    for i, im in enumerate(gardees):
        suivant = (gardees[i + 1]["t"] if i + 1 < len(gardees)
                   else t0 + total)
        lignes.append(f"file '{im['nom']}'\nduration {suivant - im['t']:.4f}\n")
    # La dernière image doit être répétée, sinon `concat` ignore sa tenue ;
    # mais la répétition rejoue cette tenue une seconde fois. D'où `-t` plus
    # bas : c'est lui qui arrête le film à la durée réelle du tournage.
    lignes.append(f"file '{gardees[-1]['nom']}'\n")
    liste = dossier / "montage.txt"
    liste.write_text("".join(lignes))

    # Le taux de compression se règle par capsule : une capsule qui défile
    # beaucoup pèse trois fois une capsule immobile, à qualité égale. Sur du
    # texte d'interface, monter le CRF de 23 à 27 ne se voit pas et divise le
    # poids par deux. `crf` dans le manifeste l'emporte sur le défaut.
    crf = str(capsule.get("crf", CRF))
    corps = TRAVAIL / f"{capsule['id']}-corps.mp4"
    subprocess.run([
        "ffmpeg", "-y", "-loglevel", "error",
        "-f", "concat", "-safe", "0", "-i", "montage.txt",
        "-t", f"{total:.3f}",
        "-vf", f"scale={L}:{H}:flags=lanczos,fps={IPS},format=yuv420p",
        "-c:v", "libx264", "-preset", "slow", "-crf", crf,
        # Surtout PAS `-tune stillimage` : réglé pour des images figées, il
        # coûte 3 Mo sur une capsule qui défile (mesuré : 11,8 contre 8,8 à
        # CRF 27) sans rien apporter à la lisibilité.
        str(corps),
    ], check=True, cwd=dossier)

    # La narration : chaque MP3 posé à l'instant où son plan a commencé.
    entrees, filtres = ["-i", str(corps)], []
    for i, repere in enumerate(reperes):
        son = VOIX / f"{capsule['id']}_{repere['plan']}.mp3"
        entrees += ["-i", str(son)]
        # L'origine est la première image filmée, pas le premier plan : le
        # tournage capte l'écran un instant avant que la voix commence, et
        # prendre le plan comme origine avançait toute la bande de 0,3 s.
        ms = int(repere["debut"] - t0 * 1000)
        filtres.append(f"[{i + 1}:a]adelay={ms}|{ms}[a{i}]")
    melange = "".join(f"[a{i}]" for i in range(len(reperes)))
    filtres.append(f"{melange}amix=inputs={len(reperes)}:normalize=0[voix]")

    avec_voix = TRAVAIL / f"{capsule['id']}-voix.mp4"
    subprocess.run([
        "ffmpeg", "-y", "-loglevel", "error", *entrees,
        "-filter_complex", ";".join(filtres),
        "-map", "0:v", "-map", "[voix]",
        "-c:v", "copy", "-c:a", "aac", "-b:a", "160k", "-ar", "48000", "-ac", "2",
        str(avec_voix),
    ], check=True)

    logo_png = TRAVAIL / "logo.png"
    titre_png, fin_png = TRAVAIL / f"{capsule['id']}-t.png", TRAVAIL / "fin.png"
    carton_logo(logo_png)
    # Pas de pied de carton : « Francisation · Niveau 4 » datait les capsules
    # d'un niveau alors qu'elles montrent le portail, le même à tous les
    # niveaux. Retiré après visionnement, le 2 septembre 2026.
    carton(titre_png, f"Espace enseignant · capsule {decalage_titre}",
           capsule["titre"])
    carton(fin_png, "Pour aller plus loin",
           "Le guide complet\nest dans le portail",
           "Bouton « Tutoriels », barre de groupe", inverse=True)
    t_mp4, f_mp4 = TRAVAIL / f"{capsule['id']}-t.mp4", TRAVAIL / f"{capsule['id']}-f.mp4"
    l_mp4 = TRAVAIL / "logo.mp4"
    segment_fixe(logo_png, LOGO_S, l_mp4)
    segment_fixe(titre_png, TITRE_S, t_mp4)
    segment_fixe(fin_png, FIN_S, f_mp4)

    liste2 = TRAVAIL / f"{capsule['id']}-tout.txt"
    liste2.write_text("".join(f"file '{p.name}'\n" for p in (l_mp4, t_mp4, avec_voix, f_mp4)))
    film = SORTIE / f"{capsule['id']}.mp4"
    subprocess.run([
        "ffmpeg", "-y", "-loglevel", "error", "-f", "concat", "-safe", "0",
        "-i", str(liste2.name), "-c", "copy", str(film),
    ], check=True, cwd=TRAVAIL)

    # Sous-titres : une réplique par plan, décalée du carton de titre.
    # Public en apprentissage du français — lire pendant qu'on écoute aide.
    vtt = ["WEBVTT", ""]
    for repere, plan in zip(reperes, capsule["plans"]):
        d = repere["debut"] / 1000.0 - t0 + LOGO_S + TITRE_S
        f = repere["fin"] / 1000.0 - t0 + LOGO_S + TITRE_S
        vtt += [f"{horodatage(d)} --> {horodatage(f)}", plan["texte"], ""]
    (SORTIE / f"{capsule['id']}.vtt").write_text("\n".join(vtt))

    return film


def main():
    seule = sys.argv[1] if len(sys.argv) > 1 else None
    TRAVAIL.mkdir(exist_ok=True)
    SORTIE.mkdir(exist_ok=True)
    manifeste = json.loads((ICI / "manifeste.json").read_text())
    for n, capsule in enumerate(manifeste["capsules"], 1):
        if seule and capsule["id"] != seule:
            continue
        film = monter(capsule, n)
        print(f"✓ {film.name} — {duree(film):.0f} s, {film.stat().st_size / 1e6:.1f} Mo")


if __name__ == "__main__":
    main()
