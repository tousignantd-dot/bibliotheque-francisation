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


FEMININES = {"sylvie"}


def scenes():
    """Les scènes « Parler » (scenes_1.py, scenes_2.py), dans l'ordre."""
    out = []
    for n in (1, 2):
        if (CONTENU / f"scenes_{n}.py").exists():
            out += charger(f"scenes_{n}").SCENES
    return out


def voix_apprenant(sc):
    """L'apprenant s'entend dans la voix de l'autre genre que le personnage :
    deux voix pareilles qui se répondent, on ne sait plus qui parle."""
    return "thierry" if sc["perso"]["voix"] in FEMININES else "sylvie"


def extraits():
    """Tous les sons du guide : (chemin relatif à MEDIA/audio, langue, texte[, voix]).
    La voix n'est donnée que pour les scènes ; sinon, celle de la langue."""
    t = []
    for l in lieux():
        for lg in LANGUES:
            t.append((f"{lg}/{l['id']}.mp3", lg, l["texte"][lg]))
    if (CONTENU / "extras.py").exists():
        for i, m in enumerate(charger("extras").MOTS):
            t.append((f"mots/{i:02d}.mp3", "fr", m["exemple"]))
    for sc in scenes():
        for k, tour in enumerate(sc["tours"]):
            if "dit" in tour:
                t.append((f"scenes/{sc['id']}/t{k}.mp3", "fr", tour["dit"], sc["perso"]["voix"]))
            else:
                t.append((f"scenes/{sc['id']}/t{k}c.mp3", "fr", tour["choix"][0][0], voix_apprenant(sc)))
        for i, ph in enumerate(sc["phrases"]):
            t.append((f"scenes/{sc['id']}/p{i}.mp3", "fr", ph[0], "sylvie"))
    return t
