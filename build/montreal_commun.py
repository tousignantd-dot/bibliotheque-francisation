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
    """Les scènes « Parler » (scenes_1.py, scenes_2.py), puis celles des enfants
    (enfants.py, id « e-… », deux choix par tour, `enfant: True`)."""
    out = []
    for n in (1, 2):
        if (CONTENU / f"scenes_{n}.py").exists():
            out += charger(f"scenes_{n}").SCENES
    if (CONTENU / "enfants.py").exists():
        out += [dict(sc, enfant=True) for sc in charger("enfants").SCENES_ENFANTS]
    return out


# ---------- le mode famille (Filou) ----------
FILOU_GENERIQUE = {
    "salut": {"fr": "Salut ! Moi, c'est Filou, le raton du mont Royal. On part explorer Montréal ?",
              "en": "Hi! I'm Filou, the raccoon from Mount Royal. Shall we go explore Montreal?",
              "es": "¡Hola! Soy Filou, el mapache del monte Royal. ¿Nos vamos a explorar Montreal?"},
    "essaie": {"fr": "Oups ! Regarde bien, et essaie encore.",
               "en": "Oops! Look carefully, and try again.",
               "es": "¡Uy! Mira bien e inténtalo otra vez."},
    "diplome": {"fr": "Bravo, explorateur ! Tu as tous tes autocollants. Ton diplôme t'attend !",
                "en": "Well done, explorer! You have all your stickers. Your certificate is waiting!",
                "es": "¡Bravo, explorador! Tienes todas tus pegatinas. ¡Tu diploma te espera!"},
}
ET_OU = {"fr": "ou", "en": "or", "es": "o"}


def ordre_enigme(e):
    """L'ordre d'affichage des trois réponses, fixé à la construction : la voix
    les lit dans l'ordre où l'écran les montre. La bonne est la première du
    contenu ; on la déplace selon le lieu, jamais au hasard d'un rechargement."""
    k = sum(map(ord, e["lieu"])) % 3
    o = [1, 2]; o.insert(k, 0)
    return o


def enfants():
    """Les dix fiches du mode famille, avec l'énigme dans l'ordre d'affichage."""
    if not (CONTENU / "enfants.py").exists():
        return []
    out = []
    for e in charger("enfants").ENFANTS:
        o = ordre_enigme(e)
        g = dict(e["enigme"]); g["choix"] = [e["enigme"]["choix"][i] for i in o]; g["bonne"] = o.index(0)
        out.append(dict(e, enigme=g))
    return out


def texte_enigme(e, lg):
    c = [x[lg] for x in e["enigme"]["choix"]]
    return f'{e["enigme"]["q"][lg]} {c[0]}, {c[1]}, {ET_OU[lg]} {c[2]} ?'.replace(" ?", " ?" if lg == "fr" else "?")


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
    for e in enfants():
        for lg in LANGUES:
            b = f"famille/{lg}/{e['lieu']}"
            t += [(f"{b}-r.mp3", lg, e["raconte"][lg], "filou"), (f"{b}-e.mp3", lg, texte_enigme(e, lg), "filou"),
                  (f"{b}-b.mp3", lg, e["enigme"]["bravo"][lg], "filou"), (f"{b}-d.mp3", lg, e["defi"][lg], "filou")]
    if enfants():
        for k, v in FILOU_GENERIQUE.items():
            for lg in LANGUES:
                t.append((f"famille/{lg}/{k}.mp3", lg, v[lg], "filou"))
    for sc in scenes():
        for k, tour in enumerate(sc["tours"]):
            if "dit" in tour:
                t.append((f"scenes/{sc['id']}/t{k}.mp3", "fr", tour["dit"], sc["perso"]["voix"]))
            else:
                t.append((f"scenes/{sc['id']}/t{k}c.mp3", "fr", tour["choix"][0][0], voix_apprenant(sc)))
        for i, ph in enumerate(sc["phrases"]):
            t.append((f"scenes/{sc['id']}/p{i}.mp3", "fr", ph[0], "sylvie"))
    return t
