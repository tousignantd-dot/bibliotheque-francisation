"""Ce que partagent le générateur de voix et celui de la page de Compostelle.

Une seule fonction dit QUELS extraits existent et OÙ ils vivent : `extraits()`.
La page s'en sert pour savoir quel son jouer, le générateur pour savoir quoi
synthétiser. Deux listes écrites à la main finiraient par diverger (le défaut
« deux sources pour une idée » que ce dépôt a déjà payé ailleurs).

CONVENTIONS DU CONTENU (etapes.py) : `{o|a}` → deux enregistrements, suffixés
`-m` (pèlerin) et `-f` (pèlerine) ; une réplique à variantes (`var`) → un
enregistrement par valeur, suffixé `-v<j>`, plus `-vd` pour le défaut.
"""
import importlib.util, pathlib, re

RACINE = pathlib.Path(__file__).resolve().parent.parent
CONTENU = RACINE / "build" / "contenu" / "compostelle"
SONS = RACINE / "assets" / "interactive" / "compostelle" / "sons"
GENRE = re.compile(r"\{([^{}|]*)\|([^{}|]*)\}")
ALG = re.compile(r"\{alg:(\w+)\}")


def charger(nom):
    sp = importlib.util.spec_from_file_location(f"compostelle_{nom}", CONTENU / f"{nom}.py")
    m = importlib.util.module_from_spec(sp); sp.loader.exec_module(m)
    return m


def genres(texte):
    """[(suffixe, texte)] : une forme si le texte ne varie pas, deux sinon."""
    if not GENRE.search(texte):
        return [("", texte)]
    return [("-m", GENRE.sub(lambda m: m.group(1), texte)),
            ("-f", GENRE.sub(lambda m: m.group(2), texte))]


def a_dire(texte):
    """Ce qui est entre parenthèses au lexique est une glose, pas un texte à dire."""
    return re.sub(r"\s*\([^)]*\)", "", texte).replace("…", "").strip()


def allergenes(texte):
    """[(suffixe, texte)] : une forme par allergène si le texte porte {alg:…}
    (audit tour 2 : l'allergie choisie traverse la scène de León et le test).
    Le suffixe `-a<code>` précède celui du genre."""
    if not ALG.search(texte):
        return [("", texte)]
    PO = charger("poche")
    return [(f"-a{c}", ALG.sub(lambda m: PO.formes(c)[m.group(1)], texte)) for c, *_ in PO.ALERGENOS]


def _pour(fichier, texte, perso, emo=None, tel=False):
    for sa, ta in allergenes(texte):
        yield from _pour_genre(fichier + sa, ta, perso, emo, tel)


def _pour_genre(fichier, texte, perso, emo=None, tel=False):
    for suf, t in genres(texte):
        yield {"fichier": f"{fichier}{suf}.mp3", "texte": t, "perso": perso,
               "emo": emo, "tel": tel}


def extraits():
    LX, ET = charger("lexique"), charger("etapes")
    for e in LX.LEXIQUE:
        yield from _pour(f"mots/{e[0]}", a_dire(e[2]), "narratrice")
    for i, t in LX.PIEGES.items():
        yield from _pour(f"pieges/{i}", t[0], "narratrice")
    PO = charger("poche")
    for i, es, _ in PO.URGENCES:
        yield from _pour(f"poche/{i}", es, "narratrice")
    for code, *_ in PO.ALERGENOS:
        yield from _pour(f"poche/alergia-{code}", PO.phrase_alergia(code), "narratrice")
    TS = charger("test"); TS.verifier()
    for f, forme in enumerate(TS.FORMES):
        for n, it in enumerate(forme):
            if it["type"] in ("rep", "repondre"):
                yield from _pour(f"test/{f}-{n}", it["es"], it["qui"])
            if it["type"] == "repondre":
                yield from _pour(f"test/{f}-{n}-c0", it["choix"][0][0], "narratrice")
    for et in ET.ETAPES:
        d = et["id"]
        for i, (es, _) in enumerate(et["voir"]):
            yield from _pour(f"voir/{d}-{i}", es, "narratrice")
        for i, (es, _) in enumerate(et["ecoute"]):
            yield from _pour(f"{d}/ecoute-{i}", es, et["local"])
        for i, dire in enumerate(et["dire"]):
            yield from _pour(f"{d}/dire-{i}", dire[1], "narratrice")
        for bloc in ("scene", "soir"):
            for k, tour in enumerate(et[bloc]["tours"]):
                base = f"{d}/{bloc}-{k}"
                if "dit" in tour:
                    if "var" in tour:
                        for j, (es, _) in enumerate(tour["var"].values()):
                            yield from _pour(f"{base}-v{j}", es, tour["dit"], tour.get("emo"), tour.get("tel", False))
                        if "defaut" in tour:
                            yield from _pour(f"{base}-vd", tour["defaut"][0], tour["dit"], tour.get("emo"), tour.get("tel", False))
                    else:
                        yield from _pour(base, tour["es"], tour["dit"], tour.get("emo"), tour.get("tel", False))
                else:
                    for j, c in enumerate(tour["choix"]):
                        if j == 0 or tour.get("libre"):
                            yield from _pour(f"{base}-c{j}", c[0], "narratrice")


if __name__ == "__main__":
    from collections import Counter
    xs = list(extraits())
    print(len(xs), "extraits,", sum(len(x["texte"]) for x in xs), "caractères")
    print(Counter(x["perso"] for x in xs))
    assert len({x["fichier"] for x in xs}) == len(xs), "deux extraits au même fichier"
