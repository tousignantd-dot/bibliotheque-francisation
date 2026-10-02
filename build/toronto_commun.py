"""Ce que partagent l'application d'« Une semaine à Toronto » et son générateur de voix.

UNE SEULE liste d'extraits (leçon de Compostelle, 25 sept. 2026 : jouer les 70
temps par programme a trouvé un son « undefined » qu'aucune relecture n'aurait
vu). La page ne joue que ce que cette liste nomme ; le générateur ne produit que
ce qu'elle nomme. Les noms de fichiers sont ceux que la page fabrique.
"""
import importlib.util, pathlib, re

RACINE = pathlib.Path(__file__).resolve().parent.parent
CONTENU = RACINE / "build" / "contenu" / "toronto"
SONS = RACINE / "assets" / "interactive" / "toronto" / "sons"


def charger(nom):
    """Sous un nom à soi : `lexique`, `sujets`, `personnages` existent aussi ailleurs
    (Francœur, Compostelle), et un import ordinaire rendrait LEURS modules."""
    sp = importlib.util.spec_from_file_location(f"toronto_{nom}", CONTENU / f"{nom}.py")
    m = importlib.util.module_from_spec(sp); sp.loader.exec_module(m)
    return m


def extraits():
    """[{fichier, texte, voix}] — tout ce que la page peut jouer."""
    PR, LX, PS = charger("preparation"), charger("lexique"), charger("personnages")
    n = PS.NARRATRICE
    out = []
    for s in PR.SEANCES:
        b = f"prep/{s['id']}"
        for k, (en, _) in enumerate(s["ecoute"]):
            out.append({"fichier": f"{b}/e{k}.mp3", "texte": en, "voix": n})
        for k, q in enumerate(s["quiz"]):
            if q["type"] == "dire":
                out.append({"fichier": f"{b}/q{k}-c0.mp3", "texte": q["choix"][0][0], "voix": n})
            else:
                out.append({"fichier": f"{b}/q{k}.mp3", "texte": q["en"], "voix": q.get("qui", n)})
        for k, d in enumerate(s["dire"]):
            out.append({"fichier": f"{b}/d{k}.mp3", "texte": d[1], "voix": n})
    for f, forme in enumerate(PR.TEST):
        for k, it in enumerate(forme):
            if it["type"] == "oral":
                out.append({"fichier": f"prep/test/{f}-{k}-m.mp3", "texte": it["modele"], "voix": n})
            elif it["type"] == "dire":
                out.append({"fichier": f"prep/test/{f}-{k}-c0.mp3", "texte": it["choix"][0][0], "voix": n})
            else:
                out.append({"fichier": f"prep/test/{f}-{k}.mp3", "texte": it["en"], "voix": it.get("qui", n)})
    # Étape 2 (1er oct. 2026) : tous les mots des douze planches, et la phrase de voyage de chaque piège.
    for e in LX.LEXIQUE:
        # Ce qui est entre parenthèses est une glose, pas un texte à dire (règle du lexique).
        out.append({"fichier": f"mots/{e[0]}.mp3", "texte": re.sub(r"\s*\([^)]*\)", "", e[2]).strip(), "voix": n})
    for i, t in LX.PIEGES.items():
        out.append({"fichier": f"pieges/{i}.mp3", "texte": t[0], "voix": "liam"})
    # Étape 4 : les exercices. REPONSES et TOTAL nomment des personnes (semaine.py), dont on prend la voix.
    EX, SE = charger("exercices"), charger("semaine")
    voix_de = {g[0]: g[2] for g in SE.GENS}
    for k, (l, q, ctx, en, ch) in enumerate(EX.REPONSES):
        out.append({"fichier": f"exos/rep-{k}.mp3", "texte": en, "voix": voix_de[q]})
    for k, (q, en, ch) in enumerate(EX.NOMBRES):
        out.append({"fichier": f"exos/nb-{k}.mp3", "texte": en, "voix": q})
    for k, it in enumerate(EX.TOTAL):
        out.append({"fichier": f"exos/tot-{k}.mp3", "texte": it[3], "voix": voix_de[it[1]]})
    for k, (q, en, b, t) in enumerate(EX.CHEMIN):
        out.append({"fichier": f"exos/ch-{k}.mp3", "texte": en, "voix": q})
    # 2 oct. 2026 : la série « Sans viande » remplace celle de l'allergie (autres textes, autres noms : veg-, plus all-).
    for k, it in enumerate(EX.VEGE):
        out.append({"fichier": f"exos/veg-{k}.mp3", "texte": it[2], "voix": voix_de[it[0]]})
    for k, (l, fr, en, cles) in enumerate(EX.DIRE):
        out.append({"fichier": f"exos/dire-{k}.mp3", "texte": en, "voix": n})
    # Étape 6 : la poche — les urgences et les phrases à montrer (le reste reprend les sons des exercices).
    PO = charger("poche")
    for i, en, fr in PO.URGENCES + PO.A_MONTRER:
        out.append({"fichier": f"poche/{i}.mp3", "texte": en, "voix": n})
    return out


if __name__ == "__main__":
    x = extraits()
    from collections import Counter
    print(f"{len(x)} extraits, {sum(len(e['texte']) for e in x)} caractères")
    print(dict(Counter(e["voix"] for e in x)))
