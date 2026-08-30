# -*- coding: utf-8 -*-
"""Les captures des documents de la trousse, posées là où le thème les cherche.

`Deck.capture()` va lire `_captures/<slug>/<code>.png` — un dossier d'épreuves
produit par `captures.py`, et **ignoré par git**. Les captures de la trousse,
elles, sont versionnées dans `assets/presentations/captures-cas/` et
`captures-telephone/`, en JPEG.

Ce module fait le pont : il recopie ce qu'un deck demande, converti en PNG,
sous le nom que `capture()` attend. On ne touche pas à `theme.py` pour si peu —
il sert aussi aux diaporamas de séance, et lui ajouter un paramètre pour un
besoin de la trousse serait payer cher un aller simple.

    from vues import poser
    poser('cas', '07-module-avec-ia')      # -> code 'cas-07-module-avec-ia'
"""

import os
import pathlib
import shutil

from pptx.util import Inches

from theme import (BODY_TOP, C, CONTENT_W, FOOT_Y, FS, MARGIN,
                   RADIUS_CTRL, h_of)

ICI = pathlib.Path(__file__).resolve().parent
RACINE = ICI.parents[2]
PRES = RACINE / 'assets' / 'presentations'
EPREUVES = ICI.parent / '_captures' / 'presentation-francis'

SOURCES = {'cas': PRES / 'captures-cas',
           'tel': PRES / 'captures-telephone',
           'mat': PRES / 'captures-materiel'}


def poser(famille, nom):
    """Recopie une capture en PNG dans le dossier d'épreuves, rend son code.

    Le code rendu est ce qu'on passe à `d.capture()`. Il porte la famille en
    préfixe : les deux dossiers ont des `01-…`, et à plat le second écraserait
    le premier sans que rien ne le dise.
    """
    src = SOURCES[famille] / (nom + '.jpg')
    if not src.exists():
        raise SystemExit('!! capture introuvable : %s' % src)
    code = '%s-%s' % (famille, nom)
    dst = EPREUVES / (code + '.png')
    EPREUVES.mkdir(parents=True, exist_ok=True)
    # On ne reconvertit pas ce qui est déjà à jour : la conversion est le seul
    # geste lent de la construction, et cinq decks se partagent des captures.
    if dst.exists() and dst.stat().st_mtime >= src.stat().st_mtime:
        return code
    try:
        from PIL import Image
        with Image.open(src) as im:
            im.convert('RGB').save(dst)
    except ImportError:
        # Sans Pillow, python-pptx sait quand même insérer un JPEG : on se
        # contente de le renommer. Le thème, lui, ouvre l'image avec Pillow
        # pour en lire le rapport — donc ce repli ne sert qu'à ne pas mourir
        # ici, pas à s'en passer plus loin.
        shutil.copyfile(src, dst)
    return code


def ecran(d, surtitre, titre, code, consigne, notes=''):
    """Une capture d'écran, plein cadre, avec son sur-titre à nous.

    `Deck.capture()` du thème ferait presque l'affaire, mais son sur-titre est
    figé sur « Dans l'activité interactive » — la phrase d'un diaporama de
    séance, qui n'a aucun sens dans la trousse — et sa consigne tient sur une
    ligne. Vu à l'aperçu, pas en relisant : la deuxième ligne passait par-dessus
    l'image.

    **La boîte de consigne se mesure, elle ne se devine pas.** Une hauteur écrite
    en dur était juste pour la phrase qui a servi à la choisir et fausse pour les
    dix-neuf autres : mesurées, elles font toutes 0,675 pouce contre les 0,62 que
    le premier jet leur donnait, et la deuxième ligne passait sous l'image. On
    demande donc au thème la hauteur qu'il occupera vraiment, et on refuse
    au-delà de trois lignes — au-delà, ce n'est plus une consigne, c'est une
    diapositive de texte à laquelle on a collé une image.
    """
    chemin = str(EPREUVES / (code + '.png'))
    if not os.path.exists(chemin):
        raise SystemExit('!! épreuve manquante : %s' % chemin)

    h = h_of(consigne, FS['body_sm'], False, CONTENT_W)
    if h > 3 * 0.34:
        raise SystemExit(
            '!! %s : consigne trop longue (%.2f po, %d caractères).\n'
            "   Trois lignes au plus — la place restante est celle de l'image."
            % (titre, h, len(consigne)))

    sl = d._new()
    d._entete(sl, surtitre, titre)
    y = BODY_TOP + 0.02
    sl.text(consigne, MARGIN, y, CONTENT_W, h, size=FS['body_sm'],
            color='ink_400', autofit=False)
    y += h + 0.14
    haut = FOOT_Y - 0.22 - y

    from PIL import Image as _Img
    with _Img.open(chemin) as im:
        ratio = im.width / im.height
    iw, ih = CONTENT_W, CONTENT_W / ratio
    if ih > haut:
        ih, iw = haut, haut * ratio
    ix, iy = MARGIN + (CONTENT_W - iw) / 2, y + (haut - ih) / 2
    sl.rect(ix - 0.02, iy - 0.02, iw + 0.04, ih + 0.04,
            fill=C['white'], line=C['line_300'], radius=RADIUS_CTRL)
    sl.shapes.add_picture(chemin, Inches(ix), Inches(iy), Inches(iw), Inches(ih))
    sl.notes(notes)
    return sl


def nettoyer():
    """Le dossier d'épreuves n'est pas versionné : on le laisse propre."""
    if EPREUVES.exists():
        shutil.rmtree(EPREUVES)


__all__ = ['poser', 'ecran', 'nettoyer', 'EPREUVES']
