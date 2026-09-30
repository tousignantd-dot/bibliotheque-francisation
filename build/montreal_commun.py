"""Ce que partagent le guide de Montréal et ses générateurs (voix, images).

Le contenu vit dans build/contenu/montreal/ : lieux_1.py, lieux_2.py,
lieux_3.py (les 28 lieux, dans l'ordre), extras.py (circuits, fiches
pratiques, mots d'ici). Chargés par importlib sous un nom propre : d'autres
trousses ont des modules du même nom (voir compostelle_croquis._charger).
"""
import importlib.util, pathlib

RACINE = pathlib.Path(__file__).resolve().parent.parent
CONTENU = RACINE / "build" / "contenu" / "montreal"
MEDIA = RACINE / "assets" / "interactive" / "montreal"
LANGUES = ("fr", "en", "es")


def charger(nom):
    sp = importlib.util.spec_from_file_location(f"montreal_{nom}", CONTENU / f"{nom}.py")
    m = importlib.util.module_from_spec(sp); sp.loader.exec_module(m)
    return m


def lieux():
    out = []
    for n in (1, 2, 3):
        if (CONTENU / f"lieux_{n}.py").exists():
            out += charger(f"lieux_{n}").LIEUX
    return out


def extraits():
    """Tous les sons du guide : (chemin relatif à MEDIA/audio, langue, texte)."""
    t = []
    for l in lieux():
        for lg in LANGUES:
            t.append((f"{lg}/{l['id']}.mp3", lg, l["texte"][lg]))
    if (CONTENU / "extras.py").exists():
        for i, m in enumerate(charger("extras").MOTS):
            t.append((f"mots/{i:02d}.mp3", "fr", m["exemple"]))
    return t
