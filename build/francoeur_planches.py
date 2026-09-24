#!/usr/bin/env python3
"""Les planches de la Maison Francœur — l'écran de l'employé (étape 1).

    python3 build/francoeur_planches.py   # → modules-autonomes/francoeur-planches/index.html

Produite, jamais écrite à la main. Elle lit trois sources, et rien d'autre :
  build/contenu/entreprise-francoeur/lexique.py        les mots
  build/contenu/entreprise-francoeur/traductions.json  les onze langues, figées
  assets/interactive/francoeur/{croquis,sons}/         ce qui existe sur le disque

LE PARCOURS : choisir sa langue (une fois, gardée sous `francisation-langue`,
la clé que partagent déjà les modules) → les onze rayons → une planche
numérotée → un article : le croquis, le mot d'ici, l'autre mot, le bouton
d'écoute, et « Voir dans ma langue ».

LES TROIS COUCHES, qui ne se confondent pas :
  - le mot à apprendre ne se traduit jamais à sa place : il reste en tête ;
  - la consigne de l'écran s'écrit en français, sa langue d'appui DESSOUS ;
  - la traduction du mot est MASQUÉE par défaut — visible d'emblée, le
    français ne serait plus traité.

LA PLANCHE EST COMPOSÉE, pas engendrée : chaque croquis est un fichier à lui,
posé dans une grille numérotée. C'est ce qui permet à un exercice de désigner
« le numéro 7 », et de corriger un seul dessin sans refaire les onze autres.
"""
import re
import html, json, pathlib, sys

RACINE = pathlib.Path(__file__).resolve().parent.parent
CONTENU = RACINE / "build" / "contenu" / "entreprise-francoeur"
sys.path.insert(0, str(CONTENU))
sys.path.insert(0, str(RACINE / "build"))
from lexique import LEXIQUE, PLANCHES, verifier  # noqa: E402
from francoeur_etape0 import TEINTES, MOTIFS  # noqa: E402
from demandes import DEMANDES, COULEURS_DISTRACTRICES, TAILLES, DECISIF, CONFONDUES  # noqa: E402
import random  # noqa: E402
import test as TEST  # noqa: E402
import clients as CLI  # noqa: E402
import gerante as GER  # noqa: E402
import modeles as MOD  # noqa: E402
import pieges as PIE  # noqa: E402
import fiche as FIC  # noqa: E402

CROQUIS = RACINE / "assets" / "interactive" / "francoeur" / "croquis"
SONS = RACINE / "assets" / "interactive" / "francoeur" / "sons"
SORTIE = RACINE / "modules-autonomes" / "francoeur-planches" / "index.html"

# Incrémenter après toute image ou tout son refait : même nom, même adresse,
# le navigateur servirait l'ancien sans rien dire.
MEDIA_V = "7"   # 7 : révision du tour 3 (formes appariées, gérante, mise de côté), 24 septembre 2026


def donnees():
    trad = json.loads((CONTENU / "traductions.json").read_text(encoding="utf-8"))
    mots = []
    for ident, planche, mot, autre, dessin, note in LEXIQUE:
        m = {"id": ident, "p": planche, "mot": mot, "autre": autre, "note": note,
             "piege": note.startswith("PIÈGE")}
        if dessin == "croquis" and (CROQUIS / f"{ident}.jpg").exists():
            m["img"] = f"/assets/interactive/francoeur/croquis/{ident}.jpg?v={MEDIA_V}"
        elif dessin == "pastille":
            m["pastille"] = MOTIFS.get(ident) or f"background:{TEINTES[ident]}"
        if (SONS / f"{ident}.mp3").exists():
            m["son"] = f"/assets/interactive/francoeur/sons/{ident}.mp3?v={MEDIA_V}"
        if (SONS / "autre" / f"{ident}.mp3").exists():
            m["autre_son"] = f"/assets/interactive/francoeur/sons/autre/{ident}.mp3?v={MEDIA_V}"
        mots.append(m)
    langues = [{"c": c, "loc": v["loc"], "rtl": v["rtl"], "relu": v["relu"],
                "ui": v.get("interface", {}), "fiche": v.get("fiche", {}),
                "mots": {k: [t["mot"], t["note"]] for k, t in v["mots"].items()}}
               for c, v in trad.items()]
    return {"planches": [{"k": k, "t": t} for k, t in PLANCHES], "mots": mots,
            "langues": langues, "demandes": demandes(mots), "test": le_test(mots),
            "magasin": le_magasin(), "gerante": la_gerante(mots), "modeles": les_modeles(),
            "reponses": les_reponses(), "phrases": les_phrases(),
            "pieges": {"p": [{"id": i, "o": [i] + c} for i, c in PIE.PIEGES], "ordinaires": PIE.ORDINAIRES},
            "tailles": {"tp": "très petit", "p": "petit", "m": "moyen", "g": "grand", "tg": "très grand"},
            "accueil": s_("accueil.mp3")}


def s_(chemin):
    return f"/assets/interactive/francoeur/sons/{chemin}?v={MEDIA_V}"


def nomme_dans(i, phrase):
    """Vrai si l'article `i` du lexique est nommé dans la phrase (pluriel compris)."""
    lex = {e[0]: e for e in LEXIQUE}
    # La tête du nom suffit : « des bottes d'hiver » est nommé par « bottes ».
    n = re.sub(r"^(un |une |des |le |la |les |l')", "", lex[i][2]).lower().split(" ")[0]
    base = n[:-1] if n.endswith(("s", "x")) and len(n) > 4 else n
    return bool(re.search(r"(?<![\w-])" + re.escape(base) + r"[sx]?(?![\w-])", phrase.lower()))


def autre_nomme(phrase, bonne, distr):
    """Un autre objet NOMMÉ dans la consigne figure-t-il parmi les choix ? Sinon,
    reconnaître le seul mot connu suffit (audit, tour 3, A3 majeur)."""
    return any(nomme_dans(d, phrase) for d in distr if d != bonne)


def la_gerante(mots):
    """L'exercice 6 : seize consignes d'entraînement (O5), autres que celles du test."""
    avec = {m["id"] for m in mots if "img" in m}
    out = []
    for i, phrase, q, bonne, distr in GER.CONSIGNES:
        assert all(x in avec for x in [bonne] + distr), f"gérante {i} : image manquante"
        out.append({"id": i, "son": s_(f"gerante/{i}.mp3"), "phrase": phrase, "q": q, "o": [bonne] + distr})
    n = sum(autre_nomme(p, b, d) for _i, p, _q, b, d in GER.CONSIGNES)
    assert n * 2 >= len(GER.CONSIGNES), f"gérante : {n} consignes sur {len(GER.CONSIGNES)} mettent un autre objet nommé parmi les choix"
    return out


def les_modeles():
    return [{"id": i, "geste": g, "cle": cle,
             "lignes": [{"qui": qui, "texte": t, "son": s_(f"modeles/{i}-{n}.mp3")}
                        for n, (qui, t) in enumerate(lignes, 1)]}
            for i, g, lignes, cle in MOD.MODELES]


def les_reponses():
    return [{"id": i, "son": s_(f"reponses/{i}-client.mp3"), "phrase": phrase, "bonne": bonne,
             "bonne_son": s_(f"reponses/{i}-bonne.mp3"), "expl": expl,
             "mauvaises": [{"t": t, "x": x} for t, x in mauvaises]}
            for i, _qui, phrase, bonne, mauvaises, expl in MOD.REPONSES]


def les_phrases():
    return [{"id": i, "texte": t, "quand": q, "son": s_(f"phrases/{i}.mp3")} for i, t, q in FIC.PHRASES]


def le_magasin():
    """Les huit clients du jeu de rôle, lus dans clients.py — la même source que
    le serveur. Un portrait manquant retombe sur le neutre."""
    base = RACINE / "assets" / "interactive" / "francoeur" / "clients"
    clients = []
    for ident, nom, voix, paliers, carte, _portrait, _faits in CLI.CLIENTS:
        assert (base / f"{ident}-neutre.jpg").exists(), f"portrait neutre manquant : {ident}"
        clients.append({"id": ident, "nom": nom, "voix": voix, "paliers": paliers, "carte": carte,
                        "p": {h: f"/assets/interactive/francoeur/clients/{ident}-"
                                 f"{h if (base / f'{ident}-{h}.jpg').exists() else 'neutre'}.jpg?v={MEDIA_V}"
                              for h in CLI.HUMEURS}})
    return {"clients": clients, "gestes": CLI.GESTES, "debit": CLI.DEBIT_JEU,
            "humeurs": CLI.HUMEURS}


# Un seul système de tailles : celui des étiquettes, que la planche enseigne
# aussi (très petit = XS…). Audit (D2, majeur) : la planche disait XS/S/M/L/XL
# et les cartes TP/P/M/G/TG, un système jamais vu.
ETIQUETTE = {"tp": "XS", "p": "S", "m": "M", "g": "L", "tg": "XL"}


def demandes(mots):
    """Les quatre variantes de chaque demande, DÉDUITES et non écrites : chaque
    distracteur ne diffère de la bonne réponse que par UN attribut. Tirage semé
    sur l'id, pour que deux constructions rendent la même page."""
    par_id = {m["id"]: m for m in mots}
    planche = {e[0]: e[1] for e in LEXIQUE}
    sortie, n_taille, t_decide = [], 0, 0
    for d in DEMANDES:
        ident, _voix, phrase, art, coul, taille = d[:6]
        ecartes = d[6] if len(d) > 6 else None
        assert art in par_id and "img" in par_id[art], f"{ident} : {art} sans croquis"
        assert coul in TEINTES, f"{ident} : couleur {coul} inconnue"
        assert not ecartes or ecartes[1] not in CONFONDUES.get(coul, ()), f"{ident} : {ecartes[1]} se confond avec {coul}"
        dec = decisif_de(ident, n_taille, DECISIF)
        if taille and not ecartes:
            n_taille += 1
        v = (carre(art, coul, taille, *ecartes, decisif=dec) if ecartes
             else variantes(ident, art, coul, taille, par_id, planche, decisif=dec))
        assert not devinable(v), f"{ident} : la bonne carte se devine sans écouter"
        if taille:
            assert trait_necessaire(v, "act".index(dec)), f"{ident} : le trait {dec} ne décide pas"
            t_decide += trait_necessaire(v, 2)
        sortie.append({"id": ident, "phrase": phrase,
                       "son": f"/assets/interactive/francoeur/sons/demandes/{ident}.mp3?v={MEDIA_V}",
                       "reprise": bool(ecartes), "taille": taille, "v": cartes(v, par_id)})
    avec_t = sum(1 for d in DEMANDES if d[5])
    assert t_decide * 3 >= avec_t, f"la taille ne décide que {t_decide} demandes sur {avec_t}"
    return sortie


def variantes(graine, art, coul, taille, par_id, planche, article_seul=False, decisif="t"):
    """La bonne réponse d'abord, puis trois autres cartes.

    EN CARRÉ LATIN (audit de la boucle didactique, 24 septembre 2026 — bloquant) :
    (A,C,T) (A,C′,T′) (A′,C,T′) (A′,C′,T). Chaque article, chaque couleur,
    chaque taille paraît exactement DEUX fois : aucune carte n'est majoritaire,
    et seule la phrase entendue désigne la bonne. L'ancienne règle — trois
    distracteurs qui changeaient chacun un seul trait — rendait la bonne carte
    majoritaire sur chaque trait : les 20 demandes se réussissaient sans écouter.
    Sans taille, le carré se fait sur deux traits : (A,C) (A,C′) (A′,C) (A′,C′).
    `article_seul` : trois autres articles, même couleur (cran 1 du test, où la
    phrase ne dit ni couleur ni taille)."""
    r = random.Random(graine)
    voisins = [e[0] for e in LEXIQUE if e[1] == planche[art] and e[0] != art
               and "img" in par_id[e[0]]]
    if article_seul:
        return [(art, coul, taille)] + [(a, coul, taille) for a in r.sample(voisins, 3)]
    a2 = r.choice(voisins)
    c2 = r.choice([c for c in COULEURS_DISTRACTRICES if c != coul and c not in CONFONDUES.get(coul, ())])
    t2 = None
    if taille:
        i = TAILLES.index(taille)
        t2 = r.choice([TAILLES[j] for j in (i - 1, i + 1) if 0 <= j < len(TAILLES)])
    return carre(art, coul, taille, a2, c2, t2, decisif)


def carre(a, c, t, a2, c2, t2, decisif="t"):
    """Les quatre cartes, la bonne d'abord.

    Sans taille : le carré sur deux traits, (A,C) (A,C′) (A′,C) (A′,C′).
    Avec taille : UN trait décisif varie seul, les deux autres varient ensemble
    (audit de la boucle didactique, tour 2, A3 majeur : dans le carré latin,
    l'article et la couleur suffisaient toujours, la taille ne décidait jamais).
    Chaque valeur paraît deux fois : rien ne se devine à la majorité."""
    if t is None:
        return [(a, c, None), (a, c2, None), (a2, c, None), (a2, c2, None)]
    if decisif == "t":
        return [(a, c, t), (a, c, t2), (a2, c2, t), (a2, c2, t2)]
    if decisif == "c":
        return [(a, c, t), (a, c2, t), (a2, c, t2), (a2, c2, t2)]
    return [(a, c, t), (a2, c, t), (a, c2, t2), (a2, c2, t2)]


ROTATION = "tca"   # le trait décisif des items sans reprise, à tour de rôle


def decisif_de(ident, n, table):
    return table.get(ident) or ROTATION[n % 3]


def trait_necessaire(v, k):
    """Vrai si, sans le trait k, la bonne carte (la première) ne se distingue
    plus d'une autre : c'est ce trait-là qu'il faut avoir entendu."""
    garde = lambda x: tuple(x[j] for j in range(3) if j != k)
    return any(garde(x) == garde(v[0]) for x in v[1:])


def devinable(v):
    """Vrai si la bonne carte (la première) se trouve sans écouter : elle est la
    seule à réunir les valeurs les plus fréquentes. Le contrôle qui a manqué."""
    from collections import Counter
    comptes = [Counter(x[k] for x in v) for k in range(3)]
    score = [sum(comptes[k][x[k]] for k in range(3)) for x in v]
    return score[0] == max(score) and score.count(max(score)) == 1


def cartes(v, par_id):
    return [{"a": a, "img": par_id[a]["img"], "mot": par_id[a]["mot"], "c": c,
             "cmot": par_id[c]["mot"], "hex": TEINTES[c], "tid": t,
             "t": ETIQUETTE.get(t) if t else None} for a, c, t in v]


def le_test(mots):
    """Les items du test en DEUX FORMES parallèles (audit F1 : le test repassé
    reprenait les mêmes items). La première passation prend la forme 1, la
    suivante la forme 2, puis on alterne. La partie A est dite par une voix de
    client (sons/test/a-<id>.mp3), jamais par la voix des planches."""
    par_id = {m["id"]: m for m in mots}
    planche = {e[0]: e[1] for e in LEXIQUE}
    avec_img = [m["id"] for m in mots if "img" in m]
    son = lambda i: s_(f"test/{i}.mp3")

    def partie_a(c1, c2, c3, graine):
        A = {1: [], 2: [], 3: []}
        for i in c1 + c2 + [x for x, _ in c3]:
            assert i in par_id and "img" in par_id[i] and (SONS / "test" / f"a-{i}.mp3").exists(), f"A : {i}"
        for cible in c1:
            r = random.Random(graine + "1" + cible)
            A[1].append({"id": cible, "son": son(f"a-{cible}"),
                         "o": [cible] + r.sample([i for i in avec_img if planche[i] != planche[cible]], 3)})
        for cible in c2:
            r = random.Random(graine + "2" + cible)
            A[2].append({"id": cible, "son": son(f"a-{cible}"),
                         "o": [cible] + r.sample([i for i in avec_img if planche[i] == planche[cible] and i != cible], 3)})
        lex = {e[0]: e for e in LEXIQUE}
        nu = lambda i: lex[i][2].split(" ", 1)[-1].lower()
        for cible, pieges in c3:
            for p in pieges:   # audit, tour 2 (D4) : aucun distracteur défendable
                mot_dans = lambda m, note: re.search(r"(?<![\w-])" + re.escape(m) + r"(?![\w-])", (note or "").lower())
                # Exception voulue : la note d'un PIÈGE nomme le sens de France,
                # et ce sens-là est le distracteur qu'on veut voir tomber.
                piege = (lex[cible][5] or "").startswith("PIÈGE")
                assert not mot_dans(nu(cible), lex[p][5]) and (piege or not mot_dans(nu(p), lex[cible][5])), \
                    f"A cran 3 : {p} est défendable pour {cible} (notes du lexique)"
            A[3].append({"id": cible, "son": son(f"a-{cible}"), "o": [cible] + pieges})
        return A

    def partie_b(items):
        B = {1: [], 2: [], 3: []}
        n = 0
        for ident, cran, _v, phrase, bonne, ecartes in items:
            dec = decisif_de(ident, n, TEST.DECISIF)
            if bonne[2] and not ecartes:
                n += 1
            v = (carre(*bonne, *ecartes, decisif=dec) if ecartes
                 else variantes(ident, *bonne, par_id, planche, article_seul=(cran == 1), decisif=dec))
            assert not devinable(v), f"{ident} : la bonne carte se devine sans écouter"
            if bonne[2] and cran > 1:
                assert trait_necessaire(v, "act".index(dec)), f"{ident} : le trait {dec} ne décide pas"
            B[cran].append({"id": ident, "son": son(ident), "phrase": phrase, "v": cartes(v, par_id)})
        return B

    def partie_c(items):
        C = {1: [], 2: [], 3: []}
        for ident, cran, phrase, question, bonne, distr in items:
            for i in [bonne] + distr:
                assert "img" in par_id[i], f"C {ident} : {i} sans croquis"
            if cran > 1:
                assert autre_nomme(phrase, bonne, distr), f"C {ident} : aucun autre objet nommé parmi les choix"
            C[cran].append({"id": ident, "son": son(ident), "phrase": phrase, "q": question,
                            "o": [bonne] + distr})
        return C

    def partie_d(items):
        return [{"id": i, "son": son(i), "phrase": p, "geste": g, "attendu": att}
                for i, _v, p, g, att, _r in items]

    # Audit, tour 3 (F1, majeur) : les deux formes doivent être PARALLÈLES — la
    # seconde sert après la formation, et une forme plus facile gonfle le gain.
    # Longueur moyenne des phrases, par partie et par cran : ±2 mots.
    for nom, f1, f2 in (("B", TEST.B, TEST.B2), ("C", TEST.C, TEST.C2)):
        k = 3 if nom == "B" else 2
        for cran in (2, 3):
            m = [sum(len(x[k].split()) for x in f if x[1] == cran) / max(1, sum(1 for x in f if x[1] == cran)) for f in (f1, f2)]
            assert abs(m[0] - m[1]) <= 2, f"{nom} cran {cran} : {m[0]:.1f} mots contre {m[1]:.1f} — formes non parallèles"
    return {"formes": [
                {"A": partie_a(TEST.A_CRAN1, TEST.A_CRAN2, TEST.A_CRAN3, "f1"),
                 "B": partie_b(TEST.B), "C": partie_c(TEST.C), "D": partie_d(TEST.D)},
                {"A": partie_a(TEST.A2_CRAN1, TEST.A2_CRAN2, TEST.A2_CRAN3, "f2"),
                 "B": partie_b(TEST.B2), "C": partie_c(TEST.C2), "D": partie_d(TEST.D2)}],
            "code_formateur": TEST.CODE_FORMATEUR,
            "oral": TEST.ORAL, "paliers": [{"k": k, "t": t, "n": n} for k, t, n in TEST.PALIERS],
            "seuils": {k: {"s": v[0], "t": v[1]} for k, v in TEST.SEUILS.items()},
            "regle": {"debutant_max": TEST.DEBUTANT_MAX, "aise_min": TEST.AISE_MIN,
                      "aise_b_min": TEST.AISE_B_MIN}}


def main():
    verifier()
    d = donnees()
    SORTIE.parent.mkdir(parents=True, exist_ok=True)
    page = GABARIT.replace("%%DONNEES%%", json.dumps(d, ensure_ascii=False, separators=(",", ":")))
    SORTIE.write_text(page, encoding="utf-8")
    n_img = sum("img" in m for m in d["mots"])
    n_son = sum("son" in m for m in d["mots"])
    print(f"{SORTIE.relative_to(RACINE)} — {len(d['mots'])} mots, {n_img} croquis, "
          f"{n_son} sons, {len(d['langues'])} langues, {len(page)//1024} Ko")


GABARIT = r"""<!DOCTYPE html>
<html lang="fr">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Maison Francœur — les vêtements</title>
<link rel="stylesheet" href="/assets/design-system/styles.css">
<link rel="stylesheet" href="/assets/design-system/marque-francis.css">
<link rel="icon" href="/assets/design-system/marque-francis-favicon.svg">
<style>
/* Page produite par build/francoeur_planches.py — ne pas l'éditer. */
:root{--mf-teinte:var(--acier-600);--mf-fond:var(--acier-100);
  /* 4,25:1 sur le fond acier : on fonce le texte discret (audit, tour 2, G1). */
  --text-muted:#585B60}
body{margin:0;background:var(--surface-page);color:var(--text-body);font-family:Nunito,system-ui,sans-serif}
.mf{max-width:1080px;margin:0 auto;padding:18px 16px 60px}
/* La barre de marque suit la colonne de la page : même largeur, même gouttière,
   sinon « francis » se décale du titre qu'il surmonte. */
.fr-barre .fr-barre__in{max-width:1080px;padding-left:16px;padding-right:16px}
.mf-tete{display:flex;align-items:flex-start;justify-content:space-between;gap:12px;flex-wrap:wrap;margin-bottom:14px}
.mf-enseigne{font-size:13px;font-weight:800;letter-spacing:.08em;text-transform:uppercase;color:var(--mf-teinte);margin:0}
.mf h1{font-size:28px;line-height:1.15;margin:4px 0 0;color:var(--text-strong)}
.appui{display:block;font-size:15px;font-weight:600;color:var(--text-muted);margin-top:3px}
.appui:empty{display:none}
[dir=rtl].appui,.appui[dir=rtl]{text-align:right}
.mf-btn{font:inherit;font-weight:700;font-size:15px;cursor:pointer;border-radius:10px;padding:9px 14px;
  border:1px solid var(--line-300);background:var(--surface-card);color:var(--text-strong);display:inline-flex;gap:8px;align-items:center}
.mf-btn:hover{border-color:var(--mf-teinte)}
.mf-btn--pri{background:var(--accent);border-color:var(--accent);color:#fff}
.mf-btn svg{width:20px;height:20px;flex:none}
.mf-btn .appui{font-size:12px;margin:0}
.mf-btn--pri .appui{color:#fff;opacity:.9}
.mf-btn--pile{flex-direction:column;align-items:flex-start;gap:0}

/* Choix de la langue */
.langues{display:grid;grid-template-columns:repeat(auto-fill,minmax(170px,1fr));gap:10px;margin-top:18px}
.langues button{font:inherit;cursor:pointer;text-align:start;padding:14px 16px;border-radius:12px;
  border:1px solid var(--line-300);background:var(--surface-card);font-size:20px;font-weight:800;color:var(--text-strong)}
.langues button:hover,.langues button:focus-visible{border-color:var(--mf-teinte);background:var(--mf-fond)}
.langues button small{display:block;font-size:13px;font-weight:600;color:var(--text-muted)}
.sans-trad{font:inherit;cursor:pointer;text-align:start;margin-top:18px;width:100%;max-width:520px;padding:16px 18px;border-radius:12px;
  border:2px solid var(--mf-teinte);background:var(--mf-fond);font-size:22px;font-weight:900;color:var(--text-strong)}
.sans-trad small{display:block;font-size:15px;font-weight:700;color:var(--mf-teinte)}
.ou-langue{margin:18px 0 0;font-weight:700;color:var(--text-muted)}
.langues button[aria-pressed=true],.sans-trad[aria-pressed=true]{box-shadow:0 0 0 3px var(--mf-teinte)}

/* Les rayons */
.rayons{display:grid;grid-template-columns:repeat(auto-fill,minmax(200px,1fr));gap:12px;margin-top:16px}
.rayon{font:inherit;cursor:pointer;text-align:start;border:1px solid var(--line-200);background:var(--surface-card);
  border-radius:14px;padding:10px;display:flex;flex-direction:column;gap:6px}
.rayon:hover{border-color:var(--mf-teinte)}
.rayon .vign{display:grid;grid-template-columns:repeat(3,1fr);gap:4px;background:#fff;border-radius:10px;padding:6px}
.rayon .vign img,.rayon .vign i{width:100%;aspect-ratio:1/1;object-fit:contain;display:block;border-radius:6px}
.rayon b{font-size:17px;color:var(--text-strong)}
.rayon .n{font-size:13px;color:var(--text-muted);font-weight:600}

/* Une planche */
.planche{display:grid;grid-template-columns:repeat(auto-fill,minmax(150px,1fr));gap:10px;margin-top:14px}
.art{font:inherit;cursor:pointer;position:relative;border:1px solid var(--line-200);background:#fff;border-radius:12px;
  padding:8px 8px 10px;display:flex;flex-direction:column;gap:4px;text-align:center;color:#17181A}
.art:hover,.art:focus-visible{border-color:var(--mf-teinte);box-shadow:0 0 0 3px var(--mf-fond)}
.art .num{position:absolute;top:6px;inset-inline-start:8px;font-size:13px;font-weight:800;color:var(--ink-500)}
.art img,.art .past,.art .sans{width:100%;aspect-ratio:1/1;object-fit:contain;border-radius:8px}
.art .past{aspect-ratio:3/2;margin:18px 0 10px;border:1px solid var(--line-200)}
.art .sans{display:grid;place-items:center;aspect-ratio:3/2;margin:18px 0 10px;background:var(--surface-sunken);
  font-size:26px;font-weight:900;color:var(--ink-400)}
.art .mot{font-weight:800;font-size:16px;line-height:1.2}
.art.piege{box-shadow:inset 0 3px 0 var(--warn-line)}

/* La fiche d'un article */
.fiche{position:fixed;inset:0;background:rgba(23,24,26,.55);display:grid;place-items:center;padding:16px;z-index:10}
.fiche[hidden]{display:none}
.carte{background:var(--surface-card);border-radius:16px;max-width:520px;width:100%;max-height:100%;overflow:auto;padding:16px}
.carte .grand{background:#fff;border-radius:12px;display:grid;place-items:center}
.carte .grand img{width:100%;max-width:360px;aspect-ratio:1/1;object-fit:contain}
.carte .grand .past{width:100%;aspect-ratio:3/2;border-radius:12px}
.carte .grand .sans{padding:28px;font-size:34px;font-weight:900;color:var(--ink-400)}
.carte h2{font-size:30px;margin:12px 0 0;color:var(--text-strong)}
.carte .autre{margin:2px 0 0;color:var(--text-muted);font-weight:600}
.carte .autre b{color:var(--text-body)}
.carte .gestes{display:flex;flex-wrap:wrap;gap:12px;margin:14px 0 6px}
.carte .trad{margin-top:8px;padding:12px 14px;border-radius:12px;background:var(--mf-fond);font-size:22px;font-weight:800;color:var(--text-strong)}
.carte .trad[hidden]{display:none}
.carte .trad small{display:block;font-size:15px;font-weight:600;color:var(--text-body);margin-top:6px}
.carte .trad .relu{display:block;font-size:12px;font-weight:600;color:var(--text-muted);margin-top:8px}
.carte .piege{margin-top:10px;padding:10px 12px;border-radius:10px;background:var(--warn-bg);border:1px solid var(--warn-line);
  color:var(--warn-ink);font-size:15px;font-weight:700}
.carte .nav{display:flex;justify-content:space-between;gap:12px;margin-top:14px}
.ferme{float:inline-end}
/* Accueil et exercices */
.accueil{display:grid;grid-template-columns:repeat(auto-fit,minmax(260px,1fr));gap:14px;margin-top:18px}
.porte{font:inherit;cursor:pointer;text-align:start;border:1px solid var(--line-200);background:var(--surface-card);
  border-radius:16px;padding:18px;display:flex;flex-direction:column;gap:6px}
.porte:hover{border-color:var(--mf-teinte)}
.porte b{font-size:22px;color:var(--text-strong)}
.exos{display:grid;gap:10px;margin-top:14px}
.exo-porte{font:inherit;cursor:pointer;text-align:start;border:1px solid var(--line-200);background:var(--surface-card);
  border-radius:14px;padding:14px 16px;display:flex;gap:14px;align-items:center}
.exo-porte:hover{border-color:var(--mf-teinte)}
.exo-porte .rang{flex:none;width:34px;height:34px;border-radius:50%;display:grid;place-items:center;background:var(--mf-fond);color:var(--mf-teinte);font-weight:900}
.exo-porte b{font-size:18px;color:var(--text-strong)}
.exo-porte.pont{border-color:var(--mf-teinte);box-shadow:inset 4px 0 0 var(--mf-teinte)}
.filtre{margin-top:14px;display:flex;gap:10px;align-items:center;flex-wrap:wrap}
.filtre select{font:inherit;font-size:16px;min-height:44px;padding:8px 10px;border-radius:10px;border:1px solid var(--line-300);background:var(--surface-card);color:var(--text-strong)}
.jeu{margin-top:12px}
.jeu .barre{height:6px;border-radius:3px;background:var(--line-200);overflow:hidden;margin-bottom:12px}
.jeu .barre i{display:block;height:100%;background:var(--accent)}
.jeu .consigne{font-weight:700;margin:0 0 10px}
.jeu .sujet{background:#fff;border-radius:14px;border:1px solid var(--line-200);display:grid;place-items:center;padding:8px;max-width:320px;margin:0 auto 12px}
.jeu .sujet img{width:100%;max-width:260px;aspect-ratio:1/1;object-fit:contain}
.jeu .sujet .past{width:100%;aspect-ratio:3/2;border-radius:10px}
.jeu .ecoute{display:flex;gap:12px;justify-content:center;flex-wrap:wrap;margin:6px 0 14px}
.choix{display:grid;gap:10px;grid-template-columns:repeat(auto-fill,minmax(150px,1fr))}
.choix.mots{grid-template-columns:1fr}
.opt{font:inherit;cursor:pointer;border:2px solid var(--line-200);background:#fff;border-radius:12px;padding:8px;color:#17181A;
  display:flex;flex-direction:column;align-items:center;gap:6px;position:relative}
.opt:hover{border-color:var(--mf-teinte)}
.opt img{width:100%;aspect-ratio:1/1;object-fit:contain}
.opt .past{width:100%;aspect-ratio:3/2;border-radius:8px;border:1px solid var(--line-200)}
.choix.mots .opt{flex-direction:row;justify-content:center;font-size:20px;font-weight:800;padding:14px}
.opt.gris img{filter:grayscale(1) contrast(.9) opacity(.75)}
.opt .attrs{display:flex;gap:8px;align-items:center;justify-content:center}
.opt .chip{width:34px;height:34px;border-radius:50%;border:2px solid #17181A33}
.opt .tag{font-weight:900;font-size:16px;border:2px solid #17181A;border-radius:6px;padding:2px 7px;background:#fff}
.opt.faux{border-color:var(--no-line);background:var(--no-bg);animation:non .3s}
.opt.juste{border-color:var(--ok-line);background:var(--ok-bg)}
.opt[disabled]{cursor:default}
@keyframes non{25%{transform:translateX(-5px)}75%{transform:translateX(5px)}}
@media (prefers-reduced-motion:reduce){.opt.faux{animation:none}}
.retro{margin:12px 0 0;font-weight:800;min-height:1.4em}
.retro.ok{color:var(--ok-ink)} .retro.non{color:var(--no-ink)}
.suite{display:flex;justify-content:flex-end;margin-top:12px}
.revele{text-align:center;margin:10px 0}
.revele .gros{font-size:30px;font-weight:900;color:var(--text-strong)}
.bilan{text-align:center;padding:20px 0}
.bilan .score{font-size:44px;font-weight:900;color:var(--text-strong)}

/* Le magasin */
.code{display:flex;gap:12px;flex-wrap:wrap;align-items:center;margin-top:12px}
.code input{font:inherit;font-size:20px;letter-spacing:.15em;text-transform:uppercase;width:10ch;padding:8px 10px;border-radius:10px;border:1px solid var(--line-300)}
.clients{display:grid;grid-template-columns:repeat(auto-fill,minmax(210px,1fr));gap:12px;margin-top:14px}
.client{font:inherit;cursor:pointer;text-align:start;border:1px solid var(--line-200);background:var(--surface-card);border-radius:14px;padding:10px;display:flex;flex-direction:column;gap:6px}
.client:hover{border-color:var(--mf-teinte)}
.client img{width:100%;aspect-ratio:1/1;object-fit:cover;background:#fff;border-radius:10px}
.client b{font-size:18px;color:var(--text-strong)}
.scene{display:grid;grid-template-columns:minmax(0,340px) minmax(0,1fr);gap:16px;margin-top:10px;align-items:start}
.avatar{background:#fff;border:1px solid var(--line-200);border-radius:16px;padding:8px;position:sticky;top:8px}
.avatar img{width:100%;aspect-ratio:1/1;object-fit:cover;display:block;border-radius:10px;transition:opacity .15s}
.avatar .nom{text-align:center;font-weight:800;margin:6px 0 0}
.fil{display:flex;flex-direction:column;gap:8px;min-height:120px}
.bulle{max-width:88%;padding:10px 12px;border-radius:14px;line-height:1.4}
.bulle.client{align-self:flex-start;background:var(--surface-card);border:1px solid var(--line-200)}
.bulle.vous{align-self:flex-end;background:var(--mf-fond);color:var(--text-strong)}
.bulle .qui{display:block;font-size:12px;font-weight:800;color:var(--text-muted);margin-bottom:2px}
.fil.cache .bulle.client .txt{filter:blur(6px);user-select:none}
.saisie{display:flex;gap:8px;margin-top:12px;flex-wrap:wrap}
.saisie input{flex:1;min-width:180px;font:inherit;font-size:17px;padding:10px 12px;border-radius:10px;border:1px solid var(--line-300)}
.attente{color:var(--text-muted);font-weight:700}
.bilan-gestes label{display:flex;gap:8px;align-items:flex-start;margin:6px 0}
@media (max-width:760px){.scene{grid-template-columns:1fr}.avatar{position:static;max-width:260px;margin:0 auto}.avatar img{max-height:170px;width:auto;margin:0 auto;display:block}}
.note-fr{color:var(--text-muted);margin:6px 0 0}
@media (max-width:640px){.clients{grid-template-columns:repeat(2,minmax(0,1fr))}.client b{font-size:15px}.client span{font-size:13px}}


/* Révision des majeurs de l'audit (24 septembre 2026) */
.chemin{list-style:none;margin:14px 0 0;padding:0;display:grid;gap:12px}
.chemin .porte{flex-direction:row;align-items:center;gap:12px;width:100%}
.chemin .rang{flex:none;width:34px;height:34px;border-radius:50%;display:grid;place-items:center;background:var(--mf-fond);color:var(--mf-teinte);font-weight:900}
.chemin li.fait .rang{background:var(--ok-bg);color:var(--ok-ink)}
.chemin li.prochaine .porte{border:2px solid var(--mf-teinte)}
.pastille-p{display:inline-block;margin-left:8px;font-size:12px;font-weight:800;color:#fff;background:var(--mf-teinte);border-radius:99px;padding:2px 8px}
.etat-f{display:inline-block;margin-left:8px;font-size:13px;color:var(--ok-ink);font-weight:700}
.bloc.tache,.bloc.rappel,.bloc.avant{background:var(--mf-fond);border-color:var(--mf-teinte)}
.mes-phrases{list-style:none;margin:12px 0 0;padding:0;display:grid;gap:10px}
.mes-phrases li{display:flex;gap:10px;align-items:flex-start;background:var(--surface-card);border:1px solid var(--line-200);border-radius:12px;padding:10px 12px}
.mes-phrases b{display:block;font-size:17px;color:var(--text-strong)}
.mes-phrases small{display:block;margin-top:3px;font-size:14px;color:var(--text-body)}
.mf-btn.ph,.mf-btn.mini{padding:8px;min-width:44px;min-height:44px;justify-content:center}
.phrases-scene summary{cursor:pointer;min-height:44px;display:flex;align-items:center}
.modele .dialogue{margin:6px 0 10px}
.modele .dialogue p{margin:4px 0;padding:6px 10px;border-radius:10px;max-width:92%}
.modele .dialogue .cli{background:var(--surface-sunken)}
.modele .dialogue .vend{background:var(--mf-fond);margin-left:auto}
.modele .qui{display:block;font-size:12px;font-weight:800;color:var(--text-muted)}
mark{background:#FFE58A;color:#17181A;padding:0 2px;border-radius:3px}
.opt .cmot{font-size:14px;font-weight:700;color:#17181A}
.opt .motseul{font-size:19px;font-weight:800;padding:10px 4px}
.opt.phrase{text-align:start;justify-content:flex-start;font-size:17px;font-weight:700}
.retro p{margin:4px 0}
.transcrit{font-style:italic}
.seuil{font-weight:800;margin:0 0 12px}
.seuil.ok{color:var(--ok-ink)} .seuil.non{color:var(--warn-ink)}
.parts small.seuil{display:block;grid-column:1/-1;margin:0;font-size:13px}
.gestes-bilan{list-style:none;margin:8px 0 0;padding:0;display:grid;gap:8px}
.gestes-bilan li{display:flex;gap:10px;align-items:flex-start}
.gestes-bilan .marque{flex:none;width:26px;height:26px;border-radius:50%;display:grid;place-items:center;font-weight:900}
.gestes-bilan li.fait .marque{background:var(--ok-bg);color:var(--ok-ink)}
.gestes-bilan li.manque .marque{background:var(--warn-bg);color:var(--warn-ink)}
.gestes-bilan li.inutile{color:var(--text-muted)}
.gestes-bilan small{display:block;margin-top:2px}
.avatar .nom{font-size:16px}
/* Contrastes et zones tactiles (audit, mineurs relevés au passage) */
.mf-btn{min-height:44px}
.mf-btn--pri{background:#087A4E;border-color:#087A4E}
.bulle.client .txt{font-size:17px}


/* RÈGLE — JAMAIS DEUX BOUTONS À MOINS DE 12 PX (demande de Daniel, 24 septembre
   2026 : « Un autre client » et « Mes phrases » se touchaient au bilan du
   magasin). L'écart des rangées de boutons n'était défini que DANS un exercice
   (.jeu .ecoute) ; hors exercice, il tombait à zéro. Il vaut maintenant
   partout, pour tout conteneur de boutons, et `ESPACE_MIN` le vérifie à
   l'écran (voir window.__francoeur.espaces). */
.ecoute,.choisir3,.gestes,.nav,.saisie,.code,.tete-boutons{display:flex;flex-wrap:wrap;gap:12px;align-items:center}
.ecoute{margin:6px 0 14px}
.choix,.planche,.rayons,.langues,.clients,.accueil,.exos{gap:12px}

/* Le test */
.intro{max-width:620px}
.intro p{margin:0 0 10px}
.partie{font-size:13px;font-weight:800;letter-spacing:.06em;text-transform:uppercase;color:var(--mf-teinte);margin:0 0 4px}
.question{font-size:19px;font-weight:800;color:var(--text-strong);margin:4px 0 12px;text-align:center}
.oral{display:flex;flex-direction:column;align-items:center;gap:10px;margin:10px 0}
.oral .etat{font-weight:700;min-height:1.4em}
.rec{background:var(--audio);border-color:var(--audio);color:#fff}
/* La traduction sous un bouton rouge : blanche, sinon elle disparaît (1,02:1). */
.rec .appui{color:#fff}
details.bloc>summary{cursor:pointer;min-height:44px;padding:10px 0;box-sizing:border-box}
.resultat{display:grid;gap:14px;margin-top:14px}
.bloc{background:var(--surface-card);border:1px solid var(--line-200);border-radius:14px;padding:16px}
.gros-palier{font-size:34px;font-weight:900;color:var(--text-strong);margin:4px 0}
.parts{display:grid;gap:8px;margin-top:8px}
.parts div{display:grid;grid-template-columns:1fr auto;gap:10px;align-items:center}
.jauge{grid-column:1/-1;height:8px;border-radius:4px;background:var(--line-200);overflow:hidden}
.jauge i{display:block;height:100%;background:var(--mf-teinte)}
.choisir3{display:flex;flex-wrap:wrap;gap:12px;margin-top:8px}
.choisir3 button[aria-pressed=true]{background:var(--ok-bg);border-color:var(--ok-line)}
.bloc.formateur{border-style:dashed}

@media (max-width:640px){
  .mf h1{font-size:23px}
  .choix{grid-template-columns:repeat(2,minmax(0,1fr))}
  .planche{grid-template-columns:repeat(2,minmax(0,1fr))}
  .rayons{grid-template-columns:repeat(2,minmax(0,1fr))}
  .langues{grid-template-columns:repeat(2,minmax(0,1fr))}
  .langues button{font-size:17px;padding:12px}
}
@media (prefers-reduced-motion:no-preference){.art,.rayon{transition:border-color .15s,box-shadow .15s}}
</style>
</head>
<body>
<div class="fr-barre"><div class="fr-barre__in">
  <span class="fr-lockup"><span class="fr-nom" role="img" aria-label="francis">franc<span class="fr-i" aria-hidden="true">ı<span class="fr-point"></span></span>s</span><span class="fr-trait" aria-hidden="true"></span><span class="fr-desc">Aide à l'apprentissage du français</span></span>
</div></div>
<main class="mf" id="app"></main>
<div class="fiche" id="fiche" hidden><div class="carte" role="dialog" aria-modal="true" aria-labelledby="ficheMot" id="carte"></div></div>
<script>
const D = %%DONNEES%%;
const CLE = 'francisation-langue';
const ICO = {
  son:'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M4 9v6h4l5 4V5L8 9H4z"/><path d="M16.5 8.5a5 5 0 0 1 0 7"/><path d="M19 6a8.5 8.5 0 0 1 0 12"/></svg>',
  oeil:'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M2 12s3.5-7 10-7 10 7 10 7-3.5 7-10 7S2 12 2 12z"/><circle cx="12" cy="12" r="3"/></svg>',
  retour:'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M15 18l-6-6 6-6"/></svg>',
  suiv:'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M9 18l6-6-6-6"/></svg>',
  globe:'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><circle cx="12" cy="12" r="9"/><path d="M3 12h18M12 3c3 3.5 3 14.5 0 18M12 3c-3 3.5-3 14.5 0 18"/></svg>',
  ferme:'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" aria-hidden="true"><path d="M6 6l12 12M18 6L6 18"/></svg>'
};
const esc = s => String(s).replace(/[&<>"]/g, c => ({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;'}[c]));
let langue = null;
try { langue = localStorage.getItem(CLE); } catch(e) {}
const L = () => D.langues.find(l => l.c === langue) || null;
// Une consigne : le français, et la langue d'appui dessous.
function dit(cle, fr) {
  const l = L(), t = l && l.ui[cle];
  return esc(fr) + (t ? '<span class="appui" dir="' + (l.rtl ? 'rtl' : 'ltr') + '" lang="' + l.c + '">' + esc(t) + '</span>' : '');
}
const FR = {choisir:"Choisissez votre langue", choisir_sous:"Les mots restent en français. Votre langue vous aide à comprendre.",
  francais_seul:"Français seulement", rayons:"Les rayons du magasin", toucher:"Touchez un vêtement pour l'entendre.",
  ecouter:"Écouter", voir:"Voir dans ma langue", cacher:"Cacher", retour:"Retour aux rayons", langue:"Changer de langue",
  non_relu:"Traduction pas encore vérifiée par une personne.", piege:"Attention", aussi:"On entend aussi",
  suivant:"Suivant", precedent:"Précédent", mots:"mots",
  accueil:"Accueil", apprendre:"Apprendre les mots", apprendre_sous:"Les onze rayons, mot par mot.",
  exercer:"Je m'exerce", exercer_sous:"Cinq exercices, du mot au client.", exercices:"Les exercices",
  tous_rayons:"Tous les rayons",
  ex_ecoute:"Je l'entends, je le trouve", ex_ecoute_c:"Écoutez, puis touchez le bon vêtement.",
  ex_image:"Le mot et son image", ex_image_c:"Touchez le bon mot.",
  ex_rappel:"Je me souviens", ex_rappel_c:"Dites le mot à voix haute, puis vérifiez.",
  ex_rayon:"Range le rayon", ex_rayon_c:"Dans quel rayon va cet article ?",
  ex_client:"Ce que le client veut", ex_client_c:"Écoutez le client. Touchez ce qu'il demande.",
  reecouter:"Réécouter", lentement:"Plus lentement", voir_mot:"Voir le mot",
  savais:"Je le savais", a_revoir:"À revoir", bravo:"Bien joué !",
  essaie:"Pas tout à fait. Essayez encore.", reponse:"Voici la bonne réponse.",
  fin:"Série terminée", premier_coup:"du premier coup", recommencer:"Une autre série",
  test:"Mon niveau", test_sous:"Un test de dix minutes, sans note.",
  t_intro:"Ce test dure environ dix minutes. Il sert à choisir le niveau des clients dans le jeu de rôle.",
  t_intro2:"Ce n'est pas un examen. L'écran ne dit pas si la réponse est bonne : répondez comme vous pouvez.",
  commencer:"Commencer", derniere:"Dernier résultat",
  partie_a:"Les mots", partie_b:"Le client", partie_c:"La gérante", partie_d:"Parler",
  ca:"Écoutez. Touchez ce que vous entendez.", cb:"Écoutez le client. Touchez ce qu'il demande.",
  cc:"Écoutez la gérante, puis répondez à la question.", cd:"Écoutez le client. Répondez à voix haute.",
  enregistrer:"Enregistrer ma réponse", arreter:"Arrêter", passer:"Passer", ecoute_micro:"Je vous écoute…",
  micro_refuse:"Le micro n'est pas disponible. Vous pouvez passer.",
  resultat:"Votre résultat", palier_propose:"Niveau proposé pour le jeu de rôle",
  pas_examen:"Ce n'est pas une note.", premiere:"Première passation", aujourdhui:"Aujourd'hui",
  pour_formateur:"Pour le formateur", pas_ce_rayon:"ne se range pas dans le rayon", code_formateur:"Code du formateur", ouvrir:"Ouvrir", code_faux:"Ce n'est pas le bon code.", confirmer_palier:"Confirmer le niveau du jeu de rôle",
  refaire_test:"Refaire le test",
  magasin:"Le magasin", magasin_sous:"Des clients vous parlent. Vous répondez.",
  code_acces:"Votre code d'accès", code_aide:"Le code vous est donné par votre formateur.",
  entrer:"Entrer", niveau_jeu:"Niveau des clients", faire_test:"Faites d'abord le test « Mon niveau », ou choisissez :",
  choisir_client:"Choisissez un client.", ecouter_sans_lire:"Écouter sans lire",
  lire:"Lire", parler:"Parler", envoyer:"Envoyer", ecrire:"Ou écrivez votre réponse…",
  fini:"J'ai fini", attente_client:"Le client réfléchit…", vous:"Vous",
  bilan_titre:"Le bilan", client_part:"Le client est parti", vos_phrases:"Vos phrases, corrigées",
  gestes_titre:"Les gestes du vendeur, dans cette visite", autre_client:"Un autre client",
  code_refuse:"Ce code n'est pas reconnu.", voix_indispo:"La voix n'est pas disponible pour le moment. Lisez la réplique.", erreur_reseau:"Impossible de joindre le serveur.",
  chemin:"Votre chemin", prochaine:"Prochaine étape", fait:"fait", etape_test:"Mon niveau", etape_mots:"Apprendre les mots", etape_exos:"Je m'exerce", etape_gestes:"Les gestes du vendeur", etape_magasin:"Le magasin", tache_titre:"Un client entre", tache:"Un client vous parle. Touchez ce qu'il demande.", tache_ok:"Oui : « une tuque ». Voici par où continuer.", tache_non:"Pas celui-là. Écoutez encore, puis touchez ce qu'il demande.", voir_bilan:"Voir le bilan", serie_pieges:"La série des pièges", serie_pieges_c:"Les mots qui ne veulent pas dire la même chose en France et au Québec.", fiche_poche:"Ma fiche de poche", fiche_sous:"Six phrases à dire au plancher.", rappel:"Une série de rappel vous attend.", rappel_sous:"Vous avez pratiqué il y a %n jours. Huit mots, dont ceux à revoir.", rappel_go:"Faire la série", gestes:"Les gestes du vendeur", gestes_sous:"Écoutez un vendeur faire chaque geste.", ecouter_dialogue:"Écouter le dialogue", a_vous:"À vous : ce que je réponds", vendeur:"Le vendeur", client:"Le client", ex_gerante:"Ce que la gérante demande", ex_gerante_c:"Écoutez la gérante, puis touchez la réponse.", ex_reponse:"Ce que je réponds", ex_reponse_c:"Écoutez le client. Choisissez ce que dit le vendeur.", pieges:"Les pièges", ca_cest:"Ça, c'est :", bon_article:"Bon article", mauvais_article:"Pas le bon article", bonne_couleur:"bonne couleur", mauvaise_couleur:"pas la bonne couleur", bonne_taille:"bonne taille", mauvaise_taille:"pas la bonne taille", objectif:"Objectif", atteint:"Objectif atteint", pas_encore:"Pas encore : refaites une série.", pas_encore_court:"pas encore", a_revoir_liste:"À revoir", suite:"Ensuite", aller_magasin:"Aller au magasin à ce niveau", mots_a_revoir:"Mes mots à revoir", mes_phrases:"Mes phrases", avant_entrer:"Avant d'entrer : écoutez les gestes du vendeur, et gardez vos phrases sous la main.", humeur_neutre:"écoute.", humeur_contente:"est content.", humeur_contente_f:"est contente.", humeur_hesitante:"hésite.", humeur_impatiente:"s'impatiente.", parti_content:"est reparti content.", parti_content_f:"est repartie contente.", parti_pas:"est reparti sans être satisfait.", parti_pas_f:"est repartie sans être satisfaite.", geste_fait:"fait", geste_manque:"à faire la prochaine fois", geste_inutile:"pas nécessaire ici", bilan_attente:"Relecture de la visite…", reussis_sur:"réussis sur", geste_attendu:"Geste attendu", exemple:"Exemple", forme:"forme"};
const T = k => dit(k, FR[k]);
const app = document.getElementById('app');
let audio = null;
function joue(src) { if (!src) return; if (audio) audio.pause(); audio = new Audio(src); audio.play().catch(()=>{}); }

// `muet` : l'image EST la question — son texte alternatif donnerait la réponse
// à un lecteur d'écran avant le choix (audit, G1).
function image(m, grand, muet) {
  if (m.img) return '<img src="' + m.img + '" alt="' + (muet ? '' : esc(m.mot)) + '"' + (grand ? '' : ' loading="lazy"') + '>';
  if (m.pastille) return '<span class="past" style="' + m.pastille + '" aria-hidden="true"></span>';
  return '<span class="sans" aria-hidden="true">' + esc(m.mot.replace(/^(un |une |des |le |la |les |l')/, '').slice(0, 2).toUpperCase()) + '</span>';
}

function ecranLangue() {
  app.innerHTML = '<p class="mf-enseigne">Maison Francœur</p>'
    + '<h1>Choisissez votre langue</h1><p style="margin:6px 0 0">Les mots restent en français. Votre langue vous aide à comprendre.</p>'
    // « Sans traduction » d'abord, et bien en vue : c'est un choix à part entière,
    // pas un oubli au bout de la liste (demande de Daniel, 24 septembre 2026).
    + '<button type="button" class="sans-trad" data-l="fr"' + (langue === 'fr' ? ' aria-pressed="true"' : '') + '>Français seulement<small>Sans traduction</small></button>'
    + '<p class="ou-langue">ou avec l\'aide d\'une langue :</p>'
    + '<div class="langues">' + D.langues.map(l => '<button type="button" data-l="' + l.c + '" lang="' + l.c + '" dir="' + (l.rtl ? 'rtl' : 'ltr') + '"' + (langue === l.c ? ' aria-pressed="true"' : '') + '>'
        + esc(l.loc) + (l.ui.choisir ? '<small>' + esc(l.ui.choisir) + '</small>' : '') + '</button>').join('') + '</div>';
  app.querySelectorAll('[data-l]').forEach(b => b.onclick = () => {
    langue = b.dataset.l; try { localStorage.setItem(CLE, langue); } catch(e) {}
    ecranAccueil();
  });
}




function tete(titre, sous, retour, cleRetour) {
  return '<div class="mf-tete"><div><p class="mf-enseigne">Maison Francœur</p><h1>' + titre + '</h1>'
    + (sous ? '<p style="margin:6px 0 0">' + sous + '</p>' : '') + '</div><div class="tete-boutons">'
    + (retour ? '<button type="button" class="mf-btn mf-btn--pile" id="retour">' + T(cleRetour || 'retour') + '</button>' : '')
    + '<button type="button" class="mf-btn mf-btn--pile" id="chLangue">' + T('langue') + '</button></div></div>';
}

function ecranRayons() {
  const l = L();
  app.innerHTML = tete(T('rayons'), T('toucher'), true, 'accueil')
    + '<div class="rayons">' + D.planches.map(p => {
        const ms = D.mots.filter(m => m.p === p.k), v = ms.filter(m => m.img || m.pastille).slice(0, 3);
        const tr = l && l.ui['planche_' + p.k];
        return '<button type="button" class="rayon" data-p="' + p.k + '"><span class="vign">'
          + v.map(m => m.img ? '<img src="' + m.img + '" alt="" loading="lazy">' : '<i style="' + m.pastille + '"></i>').join('')
          + '</span><b>' + esc(p.t) + (tr ? '<span class="appui" dir="' + (l.rtl ? 'rtl' : 'ltr') + '">' + esc(tr) + '</span>' : '') + '</b>'
          + '<span class="n">' + ms.length + ' ' + FR.mots + '</span></button>';
      }).join('') + '</div>';
  app.querySelectorAll('[data-p]').forEach(b => b.onclick = () => ecranPlanche(b.dataset.p));
  document.getElementById('retour').onclick = ecranAccueil;
  document.getElementById('chLangue').onclick = ecranLangue;
  window.scrollTo(0, 0);
}

let courante = [];
function ecranPlanche(k) {
  marquer('planche');
  const p = D.planches.find(x => x.k === k), l = L(), tr = l && l.ui['planche_' + k];
  courante = D.mots.filter(m => m.p === k);
  app.innerHTML = tete(esc(p.t) + (tr ? '<span class="appui" dir="' + (l.rtl ? 'rtl' : 'ltr') + '">' + esc(tr) + '</span>' : ''), T('toucher'), true)
    + '<div class="planche">' + courante.map((m, i) =>
        '<button type="button" class="art' + (m.piege ? ' piege' : '') + '" data-i="' + i + '"><span class="num">' + (i + 1) + '</span>'
        + image(m) + '<span class="mot">' + esc(m.mot) + '</span></button>').join('') + '</div>';
  app.querySelectorAll('[data-i]').forEach(b => b.onclick = () => ouvrir(+b.dataset.i));
  document.getElementById('retour').onclick = ecranRayons;
  document.getElementById('chLangue').onclick = ecranLangue;
  window.scrollTo(0, 0);
}

const fiche = document.getElementById('fiche'), carte = document.getElementById('carte');
let ouvert = -1, avant = null;
function ouvrir(i) {
  if (ouvert < 0) avant = document.activeElement;
  ouvert = i; const m = courante[i], l = L(), t = l && l.mots[m.id];
  carte.innerHTML = '<button type="button" class="mf-btn ferme" id="ferme" aria-label="Fermer">' + ICO.ferme + '</button>'
    + '<div class="grand">' + image(m, true) + '</div>'
    + '<h2 id="ficheMot">' + esc(m.mot) + '</h2>'
    + (m.autre ? '<p class="autre">' + esc(FR.aussi) + ' : <b>' + esc(m.autre) + '</b>'
        + (m.autre_son ? ' <button type="button" class="mf-btn mini" id="ecouteAutre" aria-label="' + esc(FR.ecouter) + ' : ' + esc(m.autre) + '">' + ICO.son + '</button>' : '') + '</p>' : '')
    // Le piège se lit TOUJOURS, en français, même quand une langue d'appui est
    // choisie : il ne se cache plus derrière « Voir dans ma langue » (audit C3).
    + notePiege(m)
    // Une note qui n'est pas un piège se lit aussi en français (audit, tour 3).
    + (m.note && !m.piege ? '<p class="note-fr">' + esc(m.note) + '</p>' : '')
    + '<div class="gestes">'
    + (m.son ? '<button type="button" class="mf-btn mf-btn--pri" id="ecoute">' + ICO.son + '<span>' + T('ecouter') + '</span></button>' : '')
    + (t ? '<button type="button" class="mf-btn" id="voir" aria-expanded="false">' + ICO.oeil + '<span>' + T('voir') + '</span></button>' : '')
    + '</div>'
    + (t ? '<div class="trad" id="trad" hidden lang="' + l.c + '" dir="' + (l.rtl ? 'rtl' : 'ltr') + '">' + esc(t[0])
        + (t[1] && !m.piege ? '<small>' + esc(t[1]) + '</small>' : '')   // le piège est déjà traduit plus haut
        + (l.relu ? '' : '<span class="relu" dir="ltr" lang="fr">' + esc(FR.non_relu) + (l.ui.non_relu ? ' · <span dir="' + (l.rtl ? 'rtl' : 'ltr') + '">' + esc(l.ui.non_relu) + '</span>' : '') + '</span>')
        + '</div>' : '')
    + '<div class="nav"><button type="button" class="mf-btn" id="prec"' + (i ? '' : ' disabled') + '>' + ICO.retour + FR.precedent + '</button>'
    + '<button type="button" class="mf-btn" id="suiv"' + (i < courante.length - 1 ? '' : ' disabled') + '>' + FR.suivant + ICO.suiv + '</button></div>';
  fiche.hidden = false;
  document.getElementById('ferme').onclick = fermer;
  const e = document.getElementById('ecoute'); if (e) e.onclick = () => joue(m.son);
  const ea = document.getElementById('ecouteAutre'); if (ea) ea.onclick = () => joue(m.autre_son);
  const v = document.getElementById('voir');
  if (v) v.onclick = () => { const tr = document.getElementById('trad'); tr.hidden = !tr.hidden; v.setAttribute('aria-expanded', String(!tr.hidden)); };
  document.getElementById('prec').onclick = () => ouvrir(i - 1);
  document.getElementById('suiv').onclick = () => ouvrir(i + 1);
  (e || document.getElementById('ferme')).focus();
  joue(m.son);
}
function fermer() { fiche.hidden = true; ouvert = -1; if (audio) audio.pause(); if (avant) avant.focus(); }
fiche.addEventListener('click', ev => { if (ev.target === fiche) fermer(); });
document.addEventListener('keydown', ev => {
  if (fiche.hidden) return;
  if (ev.key === 'Escape') fermer();
  if (ev.key === 'ArrowRight' && ouvert < courante.length - 1) ouvrir(ouvert + 1);
  if (ev.key === 'ArrowLeft' && ouvert > 0) ouvrir(ouvert - 1);
});


/* ── Les exercices ─────────────────────────────────────────────────────
   Sept, du mot isolé à la réponse du vendeur. Une série = 8 questions.
   Deux essais, puis la bonne réponse se montre (règle du dépôt : jamais la
   réponse au premier envoi). La rétroaction DIT ce qu'on a choisi, rappelle le
   piège, ou nomme le trait qui était faux (audit de la boucle didactique,
   24 septembre 2026, E1). Les mots ratés vont dans « à revoir ». Le bilan se
   lit contre le seuil de l'objectif (A1, F1). Tout reste sur l'appareil. */
const EXOS = [
  {k:'ecoute', n:1, o:'O1'}, {k:'image', n:2, o:'O1'}, {k:'rappel', n:3, o:'O1'}, {k:'rayon', n:4, o:'O1'},
  {k:'client', n:5, o:'O2', pont:true}, {k:'gerante', n:6, o:'O5'}, {k:'reponse', n:7, o:'O3'}];
// Le seuil de chaque objectif, rapporté à une série de 8 (cadrage O1-O5).
const SEUIL = {O1: 7, O2: 6, O5: 6, O3: 6};
const RAYONS = ['hauts','bas','robes','exterieur','dessous','chaussures','accessoires'];
const SERIE = 8;
const CLE_REVOIR = 'francoeur-revoir';
let revoir = new Set();
try { revoir = new Set(JSON.parse(localStorage.getItem(CLE_REVOIR) || '[]')); } catch(e) {}
const garderRevoir = () => { try { localStorage.setItem(CLE_REVOIR, JSON.stringify([...revoir])); } catch(e) {} };
let filtre = '';
const melange = a => { a = a.slice(); for (let i = a.length - 1; i > 0; i--) { const j = Math.floor(Math.random() * (i + 1)); [a[i], a[j]] = [a[j], a[i]]; } return a; };
const visuel = m => m.img || m.pastille;
const mot = id => D.mots.find(x => x.id === id);
function tirage(pool) {
  // Les mots « à revoir » d'abord, puis le reste au hasard.
  const a = melange(pool.filter(m => revoir.has(m.id))), b = melange(pool.filter(m => !revoir.has(m.id)));
  return a.concat(b).slice(0, SERIE);
}
// Une note de piège, sans son préfixe, en français ; sa traduction dessous.
function notePiege(m) {
  if (!m || !m.piege) return '';
  const l = L(), t = l && l.mots[m.id];
  return '<p class="piege">' + esc(m.note.replace(/^PIÈGE\s*:\s*/, ''))
    + (t && t[1] ? '<span class="appui" dir="' + (l.rtl ? 'rtl' : 'ltr') + '" lang="' + l.c + '">' + esc(t[1].replace(/^[^:：፦]{1,12}[:：፦]\s*/, '')) + '</span>' : '') + '</p>';
}
// Une carte « article · couleur · taille » : la couleur est dite EN MOTS sous
// la pastille — une pastille seule ne suffit pas à un daltonien (audit G1).
function carteHTML(v, attrs) {
  return '<button type="button" class="opt gris" ' + attrs + '><img src="' + v.img + '" alt="" loading="lazy">'
    + '<span class="attrs"><span class="chip" style="background:' + v.hex + '" aria-hidden="true"></span>'
    + (v.t ? '<span class="tag">' + v.t + '</span>' : '') + '</span>'
    + '<span class="cmot">' + esc(v.cmot) + (v.t ? ' · ' + v.t : '') + '</span></button>';
}

function ecranExercices() {
  app.innerHTML = tete(T('exercices'), '', true, 'accueil')
    + '<div class="filtre"><select id="filtre" aria-label="' + esc(FR.tous_rayons) + '"><option value="">' + esc(FR.tous_rayons) + '</option>'
    + '<option value="pieges"' + (filtre === 'pieges' ? ' selected' : '') + '>' + esc(FR.pieges) + '</option>'
    + D.planches.map(p => '<option value="' + p.k + '"' + (filtre === p.k ? ' selected' : '') + '>' + esc(p.t) + '</option>').join('')
    + '</select></div><div class="exos">'
    + EXOS.map(x => '<button type="button" class="exo-porte' + (x.pont ? ' pont' : '') + '" data-x="' + x.k + '"><span class="rang">' + x.n + '</span><span><b>'
      + T('ex_' + x.k) + '</b><span style="display:block;margin-top:4px">' + T('ex_' + x.k + '_c') + '</span></span></button>').join('')
    // La série des pièges avait une porte cachée dans le filtre (audit, tour 2, D3).
    + '<button type="button" class="exo-porte" id="xPieges"><span class="rang">!</span><span><b>' + T('serie_pieges') + '</b><span style="display:block;margin-top:4px">' + T('serie_pieges_c') + '</span></span></button></div>';
  document.getElementById('filtre').onchange = e => { filtre = e.target.value; };
  app.querySelectorAll('[data-x]').forEach(b => b.onclick = () => lancer(b.dataset.x));
  document.getElementById('xPieges').onclick = () => { filtre = 'pieges'; lancer('ecoute'); J.titre = 'serie_pieges'; filtre = ''; question(); };
  document.getElementById('retour').onclick = ecranAccueil;
  document.getElementById('chLangue').onclick = ecranLangue;
  window.scrollTo(0, 0);
}

let J = null;   // la série en cours
function lancer(k, rappel) {
  const dansFiltre = m => !filtre || filtre === 'pieges' || m.p === filtre;
  let items;
  if (k === 'client') items = melange(D.demandes).slice(0, SERIE);
  else if (k === 'gerante') items = melange(D.gerante).slice(0, SERIE);
  else if (k === 'reponse') items = melange(D.reponses).slice(0, SERIE);
  else if (k === 'ecoute' && filtre === 'pieges') {
    // Les pièges côte à côte avec ce qu'on confond, entrelacés avec des mots
    // ordinaires : une série faite QUE de pièges apprendrait à tout soupçonner.
    const p = melange(D.pieges.p).slice(0, 5).map(x => Object.assign({}, mot(x.id), {contrastes: x.o}));
    const o = melange(D.pieges.ordinaires).slice(0, 3).map(mot);
    items = melange(p.concat(o));
  }
  else if (k === 'rayon') items = tirage(D.mots.filter(m => m.img && RAYONS.includes(m.p) && dansFiltre(m)));
  // « Je l'entends » accepte AUSSI les mots sans image (tailles, service :
  // échange, remboursement, en arrière…) — ils se choisissent écrits (audit A3).
  else if (k === 'ecoute') items = tirage(D.mots.filter(m => m.son && dansFiltre(m) && m.p !== 'couleurs' || (m.p === 'couleurs' && visuel(m) && dansFiltre(m))));
  else items = tirage(D.mots.filter(m => visuel(m) && m.son && dansFiltre(m)));
  // Un rayon qui ne donne aucun mot pour cet exercice : on retombe sur tous les
  // rayons plutôt que d'afficher « 0 / 0 — Objectif atteint » (audit, tour 2).
  if (!items.length && filtre) { filtre = ''; return lancer(k, rappel); }
  J = {k, items, i: 0, essais: 0, premier: 0, fini: false, rates: [], rappel: !!rappel};
  marquer('exo');
  question();
}

function cadreJeu(corps) {
  app.innerHTML = tete(T(J.titre || 'ex_' + J.k), T(J.titre ? J.titre + '_c' : 'ex_' + J.k + '_c'), true, 'exercices')
    + '<div class="jeu"><div class="barre"><i style="width:' + Math.round(100 * J.i / J.items.length) + '%"></i></div>' + corps
    + '<div class="retro" id="retro" aria-live="polite"></div><div class="suite" id="suite"></div></div>';
  document.getElementById('retour').onclick = () => { if (audio) audio.pause(); ecranExercices(); };
  document.getElementById('chLangue').onclick = ecranLangue;
}
const boutonsEcoute = () => '<div class="ecoute"><button type="button" class="mf-btn mf-btn--pri" id="reec">' + ICO.son + '<span>' + T('reecouter') + '</span></button>'
  + '<button type="button" class="mf-btn" id="lent"><span>' + T('lentement') + '</span></button></div>';
function brancherEcoute(src) {
  document.getElementById('reec').onclick = () => joue(src);
  document.getElementById('lent').onclick = () => { joue(src); if (audio) { audio.preservesPitch = true; audio.playbackRate = 0.75; } };
}
const optMot = m => '<button type="button" class="opt" data-o="' + m.id + '">' + (visuel(m) ? image(m) : '<span class="motseul">' + esc(m.mot) + '</span>') + '</button>';

function question() {
  if (J.i >= J.items.length) return bilan();
  J.essais = 0;
  const it = J.items[J.i];
  if (J.k === 'ecoute') {
    let autres;
    if (it.contrastes) autres = it.contrastes.slice(1).map(mot);
    else if (visuel(it)) autres = melange(D.mots.filter(m => m.p === it.p && m.id !== it.id && visuel(m) && tete_(m) !== tete_(it))).slice(0, 5);
    // Sans image, les autres choix sont écrits aussi : un seul mot écrit parmi
    // des dessins se trouvait sans écouter (audit, tour 2, D4).
    else autres = melange(D.mots.filter(m => m.p === it.p && m.id !== it.id && !visuel(m))).slice(0, 3);
    J.bonne = it.id; J.options = melange([it].concat(autres));
    cadreJeu(boutonsEcoute() + '<div class="choix' + (visuel(it) ? '' : ' mots') + '">' + J.options.map(optMot).join('') + '</div>');
    brancherEcoute(it.son); joue(it.son);
  } else if (J.k === 'image') {
    const autres = melange(D.mots.filter(m => m.p === it.p && m.id !== it.id)).slice(0, 2);
    J.bonne = it.id; J.options = melange([it].concat(autres));
    cadreJeu('<div class="sujet">' + image(it, true, true) + '</div><div class="choix mots">'
      + J.options.map(m => '<button type="button" class="opt" data-o="' + m.id + '">' + esc(m.mot) + '</button>').join('') + '</div>');
  } else if (J.k === 'rayon') {
    const autres = melange(RAYONS.filter(r => r !== it.p)).slice(0, 3);
    J.bonne = it.p; J.options = melange([it.p].concat(autres));
    const l = L();
    cadreJeu('<div class="sujet">' + image(it, true) + '</div><p style="text-align:center;font-weight:800;font-size:20px;margin:0 0 10px">' + esc(it.mot) + '</p><div class="choix mots">'
      + J.options.map(k => { const tr = l && l.ui['planche_' + k];
          return '<button type="button" class="opt" data-o="' + k + '"><span>' + esc(D.planches.find(p => p.k === k).t)
            + (tr ? '<span class="appui" dir="' + (l.rtl ? 'rtl' : 'ltr') + '">' + esc(tr) + '</span>' : '') + '</span></button>'; }).join('') + '</div>');
    joue(it.son);
  } else if (J.k === 'rappel') {
    cadreJeu('<div class="sujet">' + image(it, true, true) + '</div><div class="revele" id="revele"><button type="button" class="mf-btn mf-btn--pri" id="voirMot">' + ICO.oeil + '<span>' + T('voir_mot') + '</span></button></div>');
    document.getElementById('voirMot').onclick = () => {
      joue(it.son);
      document.getElementById('revele').innerHTML = '<p class="gros">' + esc(it.mot) + '</p>' + notePiege(it)
        + '<div class="ecoute"><button type="button" class="mf-btn mf-btn--pri" id="savais"><span>' + T('savais') + '</span></button>'
        + '<button type="button" class="mf-btn" id="arevoir"><span>' + T('a_revoir') + '</span></button></div>';
      const auto = ok => rapporter({zone: 'ex-rappel-' + it.id, exo: 'ex-rappel', exoNum: 'Exercice 3', exoTitre: FR.ex_rappel,
        section: 'exercices', type: 'rappel', enonce: it.mot, bonne: '', reponse: '', ok, essais: 0});
      document.getElementById('savais').onclick = () => { auto(true); J.premier++; revoir.delete(it.id); garderRevoir(); J.i++; question(); };
      document.getElementById('arevoir').onclick = () => { auto(false); J.rates.push(it.mot); revoir.add(it.id); garderRevoir(); J.i++; question(); };
    };
    return;
  } else if (J.k === 'client') {
    J.bonne = 0; J.options = melange(it.v.map((v, n) => Object.assign({n}, v)));
    cadreJeu(boutonsEcoute() + '<div class="choix">' + J.options.map(v => carteHTML(v, 'data-o="' + v.n + '"')).join('') + '</div>');
    brancherEcoute(it.son); joue(it.son);
  } else if (J.k === 'gerante') {
    J.bonne = it.o[0]; J.options = melange(it.o);
    cadreJeu(boutonsEcoute() + '<p class="question">' + dit('gq_' + it.id, it.q) + '</p><div class="choix">'
      + J.options.map(id => { const m = mot(id); return '<button type="button" class="opt" data-o="' + id + '">' + image(m) + '<span style="font-weight:800">' + esc(m.mot) + '</span></button>'; }).join('') + '</div>');
    brancherEcoute(it.son); joue(it.son);
  } else if (J.k === 'reponse') {
    const opts = [{n: 0, t: it.bonne}].concat(it.mauvaises.map((x, k) => ({n: k + 1, t: x.t})));
    J.bonne = 0; J.options = melange(opts);
    cadreJeu(boutonsEcoute() + '<div class="choix mots">'
      + J.options.map(o => '<button type="button" class="opt phrase" data-o="' + o.n + '">« ' + esc(o.t) + ' »</button>').join('') + '</div>');
    brancherEcoute(it.son); joue(it.son);
  }
  app.querySelectorAll('[data-o]').forEach(b => b.onclick = () => repondre(b));
}

// La tête du nom : « un pantalon cargo » et « un pantalon » se confondent à
// l'oreille, l'un ne sert pas de distracteur à l'autre (audit, tour 3).
const tete_ = m => m.mot.replace(/^(un |une |des |le |la |les |l')/, '').split(' ')[0].toLowerCase();
// Ce que la rétroaction dit, par exercice, après un choix faux.
function pourquoiFaux(it, o) {
  const l = L();
  if (J.k === 'client') {
    const v = J.options.find(x => String(x.n) === String(o)), b = it.v[0], ecarts = [];
    ecarts.push(v.a === b.a ? 'bon_article' : 'mauvais_article');
    ecarts.push(v.c === b.c ? 'bonne_couleur' : 'mauvaise_couleur');
    if (b.t) ecarts.push(v.t === b.t ? 'bonne_taille' : 'mauvaise_taille');
    const tr = l && ecarts.every(k => l.ui[k]) ? ecarts.map(k => l.ui[k]).join(' · ') : '';
    return '<p>' + esc(ecarts.map(k => FR[k]).join(' · '))
      + (tr ? '<span class="appui" dir="' + (l.rtl ? 'rtl' : 'ltr') + '">' + esc(tr) + '</span>' : '') + '</p>';
  }
  if (J.k === 'reponse') {
    const x = it.mauvaises[Number(o) - 1];
    const tr = l && l.ui['rm_' + it.id + '_' + o];
    return '<p>' + esc(x.x) + (tr ? '<span class="appui" dir="' + (l.rtl ? 'rtl' : 'ltr') + '">' + esc(tr) + '</span>' : '') + '</p>';
  }
  // « Range le rayon » : on nomme le rayon choisi (audit, tour 2 — la
  // rétroaction était vide au premier essai).
  if (J.k === 'rayon') return '<p><b>' + esc(it.mot) + '</b> — ' + esc(FR.pas_ce_rayon) + ' « ' + esc((D.planches.find(p => p.k === o) || {}).t || '') + ' ».</p>';
  const m = mot(o);
  if (!m) return '';
  if (m.son) joue(m.son);
  // Au premier choix faux : la note du mot CHOISI seulement. Celle de la cible
  // désignait la bonne réponse (audit, tour 3, D4 majeur) ; elle vient après.
  return '<p>' + T('ca_cest') + ' <b>' + esc(m.mot) + '</b></p>' + notePiege(m);
}
// La phrase entendue, avec les mots qui décident mis en évidence.
function phraseMarquee(it) {
  let p = esc(it.phrase);
  if (J.k === 'client') {
    const b = it.v[0], marques = [b.cmot.replace(/^(le |la |l'|un |une |des )/, '').slice(0, 4),
      b.mot.replace(/^(le |la |l'|un |une |des )/, '').split(' ')[0].slice(0, 5)];
    if (b.tid) marques.push(D.tailles[b.tid]);
    marques.forEach(w => { if (w) p = p.replace(new RegExp('(' + w.replace(/[.*+?^${}()|[\]\\]/g, '\\$&') + '[a-zé]*)', 'gi'), '<mark>$1</mark>'); });
  }
  return '<p class="transcrit">« ' + p + ' »</p>';
}

function repondre(b) {
  const it = J.items[J.i], retro = document.getElementById('retro');
  const juste = String(b.dataset.o) === String(J.bonne);
  const idMot = ['client', 'gerante', 'reponse', 'rayon'].includes(J.k) ? (J.k === 'rayon' ? it.id : null) : it.id;
  if (juste) {
    b.classList.add('juste');
    if (J.essais === 0) { J.premier++; if (idMot) { revoir.delete(idMot); garderRevoir(); } }
    retro.className = 'retro ok';
    let plus = '';
    if (J.k === 'reponse') { const l = L(), tr = l && l.ui['rx_' + it.id];
      plus = '<p>' + esc(it.expl) + (tr ? '<span class="appui" dir="' + (l.rtl ? 'rtl' : 'ltr') + '">' + esc(tr) + '</span>' : '') + '</p>'; joue(it.bonne_son); }
    else if (J.k === 'ecoute' || J.k === 'image') { plus = notePiege(it); if (J.k === 'image') joue(it.son); }
    else if (J.k === 'rayon') joue(it.son);
    retro.innerHTML = '<p><b>' + T('bravo') + '</b></p>' + plus;
    finQuestion();
  } else {
    J.essais++; b.classList.add('faux'); b.disabled = true;
    if (idMot) { revoir.add(idMot); garderRevoir(); }
    if (J.essais >= 2) {
      const bon = app.querySelector('[data-o="' + J.bonne + '"]'); if (bon) bon.classList.add('juste');
      retro.className = 'retro non';
      let plus = '';
      if (J.k === 'client' || J.k === 'gerante') { plus = phraseMarquee(it); joue(it.son); }
      else if (J.k === 'reponse') { plus = '<p>« ' + esc(it.bonne) + ' » — ' + esc(it.expl) + '</p>'; joue(it.bonne_son); }
      else if (J.k === 'rayon') { plus = '<p><b>' + esc(it.mot) + '</b> → ' + esc(D.planches.find(p => p.k === it.p).t) + '</p>'; joue(it.son); }
      else { plus = '<p><b>' + esc(it.mot) + '</b></p>' + notePiege(it); joue(it.son); }
      retro.innerHTML = '<p><b>' + T('reponse') + '</b></p>' + plus;
      J.rates.push(it.mot || it.phrase);
      finQuestion();
    } else { retro.className = 'retro non'; retro.innerHTML = '<p><b>' + T('essaie') + '</b></p>' + pourquoiFaux(it, b.dataset.o); }
  }
}
function finQuestion() {
  const it = J.items[J.i], juste = !!app.querySelector('.opt.juste:not(.faux)') && J.essais < 2;
  const fautif = app.querySelector('.opt.faux');
  const libelle = o => J.k === 'client' ? carteTexte(J.options.find(v => String(v.n) === String(o)))
    : J.k === 'rayon' ? (D.planches.find(p => p.k === o) || {}).t
    : J.k === 'reponse' ? (J.options.find(v => String(v.n) === String(o)) || {}).t : etiquette(o);
  rapporter({zone: 'ex-' + J.k + '-' + it.id, exo: 'ex-' + J.k, exoNum: 'Exercice ' + (EXOS.find(x => x.k === J.k).n),
    exoTitre: FR['ex_' + J.k], section: 'exercices', type: J.k,
    enonce: it.phrase || it.mot, bonne: libelle(J.bonne),
    reponse: juste ? libelle(J.bonne) : (fautif ? libelle(fautif.dataset.o) : ''), ok: juste, essais: J.essais});
  app.querySelectorAll('[data-o]').forEach(x => x.disabled = true);
  const s = document.getElementById('suite');
  s.innerHTML = '<button type="button" class="mf-btn mf-btn--pri" id="apres"><span>' + T('suivant') + '</span>' + ICO.suiv + '</button>';
  const a = document.getElementById('apres'); a.onclick = () => { J.i++; question(); }; a.focus();
}
// La suite logique d'un exercice : où aller ensuite (audit F2).
const SUITE_EXO = {ecoute: 'image', image: 'rappel', rappel: 'rayon', rayon: 'client', client: 'gerante', gerante: 'gestes', reponse: 'magasin'};
function bilan() {
  J.fini = true;
  rapporterSerie(J.items.length, J.premier);
  // « Je me souviens » est déclaré par l'employé : il ne se juge pas contre un
  // seuil (audit, tour 2, D1). Les autres, oui.
  const x = EXOS.find(e => e.k === J.k), seuil = Math.min(SEUIL[x.o], J.items.length), ok = J.premier >= seuil, juge = J.k !== 'rappel';
  const suite = SUITE_EXO[J.k];
  const libSuite = suite === 'gestes' ? T('gestes') : suite === 'magasin' ? T('magasin') : T('ex_' + suite);
  app.innerHTML = tete(T('ex_' + J.k), '', true, 'exercices')
    + '<div class="bilan"><p style="font-weight:800;margin:0">' + T('fin') + '</p><p class="score">' + J.premier + ' / ' + J.items.length + '</p>'
    + (juge ? '<p style="margin:0 0 6px">' + T('premier_coup') + '</p>' : '<p style="margin:0 0 6px">' + T('savais') + '</p>')
    + (!juge ? '' : '<p class="seuil ' + (ok ? 'ok' : 'non') + '">' + esc(FR.objectif) + ' : ' + seuil + ' / ' + J.items.length + ' — ' + (ok ? T('atteint') : T('pas_encore')) + '</p>')
    + (J.rates.length ? '<div class="bloc" style="text-align:start"><b>' + T('a_revoir_liste') + '</b><ul>' + J.rates.map(r => '<li>' + esc(r) + '</li>').join('') + '</ul></div>' : '')
    + '<div class="ecoute"><button type="button" class="mf-btn" id="encore"><span>' + T('recommencer') + '</span></button>'
    + '<button type="button" class="mf-btn mf-btn--pri" id="ensuite"><span>' + esc(FR.suite) + ' : ' + '</span>' + libSuite + '</button></div></div>';
  document.getElementById('encore').onclick = () => lancer(J.k);
  document.getElementById('ensuite').onclick = () => suite === 'gestes' ? ecranGestes() : suite === 'magasin' ? ecranMagasin() : lancer(suite);
  document.getElementById('retour').onclick = ecranExercices;
  document.getElementById('chLangue').onclick = ecranLangue;
}
window.__francoeur = { etat: () => J, D };

/* ── Le suivi du chemin, sur l'appareil ────────────────────────────────
   Ce qui a été fait (test, rayons vus, séries, gestes, visites) et les jours
   de pratique : l'accueil en tire la prochaine étape et le rappel (audit B1,
   F3). Rien ne sort de l'appareil par ce chemin-ci. */
const CLE_SUIVI = 'francoeur-suivi';
function suivi() { try { return JSON.parse(localStorage.getItem(CLE_SUIVI) || '{}'); } catch(e) { return {}; } }
function marquer(quoi) {
  const s = suivi(), auj = new Date().toISOString().slice(0, 10);
  s[quoi] = (s[quoi] || 0) + 1;
  s.jours = Array.from(new Set((s.jours || []).concat([auj]))).slice(-60);
  try { localStorage.setItem(CLE_SUIVI, JSON.stringify(s)); } catch(e) {}
}
// Les rappels espacés : J+2, J+7, J+30 après la dernière pratique (Cepeda).
function rappelDu() {
  const s = suivi(), j = s.jours || [];
  if (!j.length) return null;
  const der = j[j.length - 1], n = Math.round((Date.now() - Date.parse(der + 'T12:00:00')) / 86400000);
  return n >= 2 ? n : null;
}
const ETAPES = [
  {k: 'test',    fait: s => histo().length > 0,  ouvre: () => ecranTest()},
  {k: 'mots',    fait: s => (s.planche || 0) >= 3, ouvre: () => ecranRayons()},
  {k: 'exos',    fait: s => (s.exo || 0) >= 3,   ouvre: () => ecranExercices()},
  {k: 'gestes',  fait: s => (s.gestes || 0) >= 1, ouvre: () => ecranGestes()},
  {k: 'magasin', fait: s => (s.visite || 0) >= 1, ouvre: () => ecranMagasin()}];

function ecranAccueil() {
  const s = suivi(), prochaine = ETAPES.find(e => !e.fait(s)) || ETAPES[4], n = rappelDu();
  const tache = !s.tache;
  app.innerHTML = tete(tache ? T('tache_titre') : T('chemin'), '', false)
    // La première fois : une tâche, pas un menu (audit B1). Un client parle,
    // l'employé touche ce qu'il demande — avant toute explication.
    + (tache ? '<div class="bloc tache"><p style="margin:0 0 8px"><b>' + T('tache') + '</b></p>'
        + '<div class="ecoute"><button type="button" class="mf-btn mf-btn--pri" id="tEcoute">' + ICO.son + '<span>' + T('reecouter') + '</span></button></div>'
        + '<div class="choix">' + melange(['tuque', 'casquette', 'foulard', 'mitaines']).map(id => '<button type="button" class="opt" data-t="' + id + '">' + image(mot(id), false, true) + '</button>').join('')
        + '</div><div class="retro" id="tRetro" aria-live="polite"></div></div>' : '')
    + (n ? '<div class="bloc rappel"><b>' + T('rappel') + '</b><p style="margin:4px 0 8px">' + esc(FR.rappel_sous.replace('%n', n)) + '</p>'
        + '<button type="button" class="mf-btn mf-btn--pri" id="aRappel"><span>' + T('rappel_go') + '</span></button></div>' : '')
    + '<ol class="chemin">' + ETAPES.map((e, i) => {
        const f = e.fait(s), p = e === prochaine;
        return '<li class="' + (f ? 'fait' : '') + (p ? ' prochaine' : '') + '"><button type="button" class="porte" data-e="' + i + '">'
          + '<span class="rang">' + (f ? '✓' : i + 1) + '</span><span><b>' + T('etape_' + e.k) + '</b>'
          + (p ? '<span class="pastille-p">' + esc(FR.prochaine) + '</span>' : f ? '<span class="etat-f">' + esc(FR.fait) + '</span>' : '')
          + '</span></button></li>'; }).join('') + '</ol>'
    + '<div class="accueil"><button type="button" class="porte" id="aFiche"><b>' + T('fiche_poche') + '</b><span>' + T('fiche_sous') + '</span></button></div>';
  if (tache) {
    const src = D.accueil;
    document.getElementById('tEcoute').onclick = () => joue(src);
    joue(src);
    app.querySelectorAll('[data-t]').forEach(b => b.onclick = () => {
      const r = document.getElementById('tRetro');
      if (b.dataset.t === 'tuque') {
        b.classList.add('juste'); r.className = 'retro ok'; r.innerHTML = '<p><b>' + T('tache_ok') + '</b></p>';
        joue(mot('tuque').son);
        const x = suivi(); x.tache = 1; try { localStorage.setItem(CLE_SUIVI, JSON.stringify(x)); } catch(e) {}
        // Un bouton, pas une minuterie (audit, tour 2, G2) : la rétroaction
        // reste à l'écran le temps qu'on la lise.
        r.innerHTML += '<div class="suite"><button type="button" class="mf-btn mf-btn--pri" id="tSuite"><span>' + T('suivant') + '</span>' + ICO.suiv + '</button></div>';
        app.querySelectorAll('[data-t]').forEach(x => x.disabled = true);
        document.getElementById('tSuite').onclick = ecranAccueil; document.getElementById('tSuite').focus();
      } else { b.classList.add('faux'); r.className = 'retro non'; r.innerHTML = '<p>' + T('tache_non') + '</p>'; joue(src); }
    });
  }
  if (n) document.getElementById('aRappel').onclick = () => { filtre = ''; lancer('ecoute', true); };
  app.querySelectorAll('[data-e]').forEach(b => b.onclick = () => ETAPES[+b.dataset.e].ouvre());
  document.getElementById('aFiche').onclick = ecranFichePoche;
  document.getElementById('chLangue').onclick = ecranLangue;
  window.scrollTo(0, 0);
}

/* ── Ma fiche de poche, à l'écran (audit F2) ───────────────────────────
   Les six phrases du vendeur, dans l'ordre d'une vente, avec leur voix (le
   vendeur modèle) et « quand s'en servir » dans la langue d'appui. */
function phrasesHTML() {
  const l = L();
  return '<ol class="mes-phrases">' + D.phrases.map(p => {
    const q = l && l.fiche && l.fiche['quand_' + p.id];
    return '<li><button type="button" class="mf-btn mf-btn--pri ph" data-s="' + p.son + '" aria-label="' + esc(FR.ecouter) + '">' + ICO.son + '</button>'
      + '<span><b>' + esc(p.texte) + '</b><small>' + esc(p.quand) + '</small>'
      + (q ? '<small class="appui" dir="' + (l.rtl ? 'rtl' : 'ltr') + '">' + esc(q) + '</small>' : '') + '</span></li>'; }).join('') + '</ol>';
}
function brancherPhrases(racine) { (racine || app).querySelectorAll('[data-s]').forEach(b => b.onclick = () => joue(b.dataset.s)); }
function ecranFichePoche() {
  app.innerHTML = tete(T('fiche_poche'), T('fiche_sous'), true, 'accueil') + phrasesHTML();
  brancherPhrases();
  document.getElementById('retour').onclick = ecranAccueil;
  document.getElementById('chLangue').onclick = ecranLangue;
  window.scrollTo(0, 0);
}

/* ── Les gestes du vendeur : l'exemple travaillé (audit C4) ────────────
   Cinq dialogues très courts, un par geste : on ENTEND un vendeur faire le
   geste, la phrase clé est mise en évidence. Puis « À vous » : l'exercice
   « Ce que je réponds », où l'on choisit la réponse. Puis le magasin. */
function ecranGestes() {
  marquer('gestes');
  const l = L();
  app.innerHTML = tete(T('gestes'), T('gestes_sous'), true, 'accueil')
    + D.modeles.map(m => {
        const g = l && l.ui['mg_' + m.id];
        return '<div class="bloc modele"><h2 style="margin:0 0 6px;font-size:19px">' + esc(m.geste)
          + (g ? '<span class="appui" dir="' + (l.rtl ? 'rtl' : 'ltr') + '">' + esc(g) + '</span>' : '') + '</h2>'
          + '<div class="dialogue">' + m.lignes.map(x => '<p class="' + (x.qui === 'vendeur' ? 'vend' : 'cli') + '"><span class="qui">'
              + esc(x.qui === 'vendeur' ? FR.vendeur : FR.client) + '</span>'
              + (x.qui === 'vendeur' ? esc(x.texte).replace(esc(m.cle.split(' … ')[0]), '<mark>' + esc(m.cle.split(' … ')[0]) + '</mark>') : esc(x.texte)) + '</p>').join('') + '</div>'
          + '<button type="button" class="mf-btn mf-btn--pri" data-m="' + m.id + '">' + ICO.son + '<span>' + T('ecouter_dialogue') + '</span></button></div>'; }).join('')
    + '<div class="ecoute"><button type="button" class="mf-btn mf-btn--pri" id="aVous"><span>' + T('a_vous') + '</span>' + ICO.suiv + '</button></div>';
  app.querySelectorAll('[data-m]').forEach(b => b.onclick = () => {
    const m = D.modeles.find(x => x.id === b.dataset.m);
    let k = 0;
    const suivant = () => { if (k >= m.lignes.length) return; const a = joue(m.lignes[k++].son); if (audio) audio.onended = suivant; };
    suivant();
  });
  document.getElementById('aVous').onclick = () => lancer('reponse');
  document.getElementById('retour').onclick = ecranAccueil;
  document.getElementById('chLangue').onclick = ecranLangue;
  window.scrollTo(0, 0);
}
/* ── Le test de positionnement (étape 3) ───────────────────────────────
   A (mots), B (client), C (gérante) : adaptatif. À un cran, 3 bonnes le
   valident et font monter ; 2 erreurs arrêtent la partie. Aucune rétroaction.
   DEUX FORMES : la première passation prend la forme 1, la suivante la
   forme 2, puis on alterne (audit F1 — le test repassé reprenait les mêmes
   items). D (oral) : quatre situations qui exigent chacune UN geste ;
   enregistré sur l'appareil, jamais envoyé, noté par le formateur contre le
   geste attendu. Le résultat se lit contre les SEUILS des objectifs. */
const CLE_TEST = 'francoeur-test';
const histo = () => { try { return JSON.parse(localStorage.getItem(CLE_TEST) || '[]'); } catch(e) { return []; } };
const garderHisto = h => { try { localStorage.setItem(CLE_TEST, JSON.stringify(h)); } catch(e) {} };
const nomPalier = k => D.test.paliers.find(p => p.k === k);
function calculPalier(a, b, c) {
  const R = D.test.regle, s = a + b + c;
  if (s <= R.debutant_max || b === 0) return 'debutant';
  if (s >= R.aise_min && b >= R.aise_b_min) return 'aise';
  return 'fonctionnel';
}
let X = null;   // la passation en cours

function ecranTest() {
  const h = histo(), der = h[h.length - 1];
  app.innerHTML = tete(T('test'), '', true, 'accueil')
    + '<div class="intro"><p>' + T('t_intro') + '</p><p>' + T('t_intro2') + '</p>'
    + '<ul class="simple">' + Object.values(D.test.seuils).map(x => '<li>' + esc(x.t) + '</li>').join('') + '</ul>'
    + (der ? '<p class="bloc">' + esc(FR.derniere) + ' : <b>' + esc(nomPalier(der.confirme || der.palier).t) + '</b> · ' + der.date + '</p>' : '')
    + '<button type="button" class="mf-btn mf-btn--pri" id="go"><span>' + T('commencer') + '</span>' + ICO.suiv + '</button></div>';
  document.getElementById('go').onclick = debuterTest;
  document.getElementById('retour').onclick = ecranAccueil;
  document.getElementById('chLangue').onclick = ecranLangue;
  window.scrollTo(0, 0);
}
function debuterTest() {
  const f = histo().length % 2;   // 0 → forme 1, 1 → forme 2, puis on alterne
  // L'ordre des situations orales se tire (audit, tour 3, F1) : à la seconde
  // passation, on ne sait pas d'avance quel geste vient en premier.
  X = {f, F: D.test.formes[f], D: melange(D.test.formes[f].D), parties: ['A', 'B', 'C'], p: 0, cran: 1, bons: 0, faux: 0, niveau: {A: 0, B: 0, C: 0},
       vus: new Set(), reponses: [], oral: [], blobs: [], fini: false};
  questionTest();
}
function itemSuivant() {
  const P = X.parties[X.p], pool = X.F[P][X.cran].filter(it => !X.vus.has(it.id));
  return pool.length ? melange(pool)[0] : null;
}
function questionTest() {
  if (X.p >= X.parties.length) return partieOrale(0);
  const P = X.parties[X.p], it = itemSuivant();
  if (!it) return partieFinie();
  X.vus.add(it.id); X.item = it;
  let corps = '';
  const titre = '<p class="partie">' + esc(FR['partie_' + P.toLowerCase()]) + '</p>';
  const ecoute = '<div class="ecoute"><button type="button" class="mf-btn mf-btn--pri" id="reec">' + ICO.son + '<span>' + T('reecouter') + '</span></button></div>';
  if (P === 'A') {
    X.options = melange(it.o); X.bonne = it.id;
    corps = ecoute + '<div class="choix">' + X.options.map(id => '<button type="button" class="opt" data-o="' + id + '">' + image(mot(id), false, true) + '</button>').join('') + '</div>';
  } else if (P === 'B') {
    X.options = melange(it.v.map((v, n) => Object.assign({n}, v))); X.bonne = 0;
    corps = ecoute + '<div class="choix">' + X.options.map(v => carteHTML(v, 'data-o="' + v.n + '"')).join('') + '</div>';
  } else {
    X.options = melange(it.o); X.bonne = it.o[0];
    corps = ecoute + '<p class="question">' + dit('tq_' + it.id, it.q) + '</p><div class="choix">' + X.options.map(id => { const m = mot(id);
      return '<button type="button" class="opt" data-o="' + id + '">' + image(m) + '<span style="font-weight:800">' + esc(m.mot) + '</span></button>'; }).join('') + '</div>';
  }
  app.innerHTML = tete(T('test'), T('c' + P.toLowerCase()), false)
    + '<div class="jeu">' + titre + corps + '</div>';
  document.getElementById('chLangue').remove();
  document.getElementById('reec').onclick = () => joue(it.son);
  joue(it.son);
  app.querySelectorAll('[data-o]').forEach(b => b.onclick = () => repondreTest(String(b.dataset.o) === String(X.bonne), b.dataset.o));
  window.scrollTo(0, 0);
}
function repondreTest(juste, choix) {
  // Aucune rétroaction : on passe à la suite, c'est tout.
  if (audio) audio.pause();
  X.reponses.push({p: X.parties[X.p], cran: X.cran, id: X.item.id, juste});
  { const P = X.parties[X.p], it = X.item;
    if (P === 'A' && !juste) { revoir.add(it.id); garderRevoir(); }
    rapporter({zone: 'test' + (X.f + 1) + '-' + P + '-' + it.id, exo: 'test-' + P, exoNum: 'Test · forme ' + (X.f + 1) + ' · cran ' + X.cran,
      exoTitre: FR['partie_' + P.toLowerCase()], section: 'test', type: 'test',
      enonce: P === 'A' ? etiquette(it.id) : P === 'B' ? it.phrase : it.phrase + ' — ' + it.q,
      bonne: P === 'B' ? carteTexte(it.v[0]) : etiquette(P === 'A' ? it.id : it.o[0]),
      // Le choix fait remonte : le pilote lit quel distracteur attire (audit, tour 3).
      reponse: P === 'B' ? carteTexte(X.options.find(v => String(v.n) === String(choix))) : etiquette(choix), ok: juste, essais: 0}); }
  if (juste) {
    X.bons++;
    if (X.bons >= 3) {
      X.niveau[X.parties[X.p]] = X.cran;
      if (X.cran === 3) return partieFinie();
      X.cran++; X.bons = 0; X.faux = 0;
    }
  } else if (++X.faux >= 2) return partieFinie();
  questionTest();
}
function partieFinie() { X.p++; X.cran = 1; X.bons = 0; X.faux = 0; questionTest(); }

let enreg = null;
function partieOrale(i) {
  const DD = X.D;
  if (i >= DD.length) return resultatTest();
  const it = DD[i];
  app.innerHTML = tete(T('test'), T('cd'), false)
    + '<div class="jeu"><p class="partie">' + esc(FR.partie_d) + ' · ' + (i + 1) + ' / ' + DD.length + '</p>'
    + '<div class="ecoute"><button type="button" class="mf-btn mf-btn--pri" id="reec">' + ICO.son + '<span>' + T('reecouter') + '</span></button></div>'
    + '<div class="oral"><button type="button" class="mf-btn rec" id="rec"><span>' + T('enregistrer') + '</span></button>'
    + '<p class="etat" id="etatRec" aria-live="polite"></p><div id="rejouer"></div></div>'
    + '<div class="suite"><button type="button" class="mf-btn" id="apres"><span>' + T('passer') + '</span>' + ICO.suiv + '</button></div></div>';
  document.getElementById('chLangue').remove();
  document.getElementById('reec').onclick = () => joue(it.son);
  joue(it.son);
  const rec = document.getElementById('rec'), etat = document.getElementById('etatRec');
  rec.onclick = async () => {
    if (enreg && enreg.state === 'recording') { enreg.stop(); return; }
    if (audio) audio.pause();
    try {
      const flux = await navigator.mediaDevices.getUserMedia({audio: true});
      const morceaux = []; enreg = new MediaRecorder(flux);
      enreg.ondataavailable = e => morceaux.push(e.data);
      enreg.onstop = () => {
        // Le micro se ferme pour de bon : ouvert, il dégrade la sortie audio de Chrome.
        flux.getTracks().forEach(t => t.stop());
        const url = URL.createObjectURL(new Blob(morceaux, {type: enreg.mimeType}));
        X.blobs[i] = url;
        rec.innerHTML = '<span>' + T('enregistrer') + '</span>'; etat.textContent = '';
        document.getElementById('rejouer').innerHTML = '<audio controls src="' + url + '"></audio>';
        document.getElementById('apres').innerHTML = '<span>' + T('suivant') + '</span>' + ICO.suiv;
      };
      enreg.start(); rec.innerHTML = '<span>' + T('arreter') + '</span>'; etat.innerHTML = T('ecoute_micro');
    } catch(e) { etat.innerHTML = T('micro_refuse'); }
  };
  document.getElementById('apres').onclick = () => { if (enreg && enreg.state === 'recording') enreg.stop(); partieOrale(i + 1); };
  window.scrollTo(0, 0);
}

function resultatTest() {
  X.fini = true;
  marquer('test');
  const n = X.niveau, pal = calculPalier(n.A, n.B, n.C);
  const h = histo();
  // Les taux par partie, contre le seuil de l'objectif (audit F1, A1).
  const taux = {};
  ['A', 'B', 'C'].forEach(P => { const r = X.reponses.filter(x => x.p === P); taux[P] = {j: r.filter(x => x.juste).length, n: r.length}; });
  const entree = {date: new Date().toISOString().slice(0, 10), forme: X.f + 1, a: n.A, b: n.B, c: n.C, taux, palier: pal, confirme: null,
                  oral: X.D.map(() => null)};
  h.push(entree); garderHisto(h);
  const premiere = h.length > 1 ? h[0] : null;
  const ligne = (k, v) => {
    // Audit, tour 2 (F1) : dans un test adaptatif, le taux brut dépend de
    // l'ordre des erreurs. L'objectif est atteint quand le cran qui porte sa
    // tâche est VALIDÉ (trois bonnes à ce cran).
    const t = taux[k.toUpperCase()], s = D.test.seuils[k.toUpperCase()], ok = v >= s.s;
    return '<div><span>' + esc(FR['partie_' + k]) + ' — ' + t.j + ' ' + esc(FR.reussis_sur) + ' ' + t.n + '</span><b>' + v + ' / 3</b>'
      + '<span class="jauge"><i style="width:' + Math.round(v / 3 * 100) + '%"></i></span>'
      + '<small class="seuil ' + (ok ? 'ok' : 'non') + '">' + esc(s.t) + ' — ' + (ok ? esc(FR.atteint) : esc(FR.pas_encore_court)) + '</small></div>'; };
  app.innerHTML = tete(T('resultat'), '', true, 'accueil')
    + '<div class="resultat"><div class="bloc"><p style="margin:0">' + T('palier_propose') + '</p>'
    + '<p class="gros-palier">' + esc(nomPalier(pal).t) + '</p><p style="margin:0;color:var(--text-muted)">' + esc(nomPalier(pal).n) + ' · ' + T('pas_examen') + '</p>'
    + '<div class="parts">' + ligne('a', n.A) + ligne('b', n.B) + ligne('c', n.C) + '</div>'
    + '<div class="ecoute" style="justify-content:flex-start;margin-top:14px"><button type="button" class="mf-btn mf-btn--pri" id="versMag"><span>' + T('aller_magasin') + '</span>' + ICO.suiv + '</button>'
    + '<button type="button" class="mf-btn" id="versMots"><span>' + T('mots_a_revoir') + '</span></button></div></div>'
    + (premiere ? '<div class="bloc"><b>' + esc(FR.premiere) + '</b> (' + premiere.date + ') : ' + esc(nomPalier(premiere.confirme || premiere.palier).t)
        + ' — A ' + premiere.a + ' · B ' + premiere.b + ' · C ' + premiere.c + '<br><b>' + esc(FR.aujourdhui) + '</b> (' + esc(FR.forme) + ' ' + (X.f + 1) + ') : ' + esc(nomPalier(pal).t)
        + ' — A ' + n.A + ' · B ' + n.B + ' · C ' + n.C + '</div>' : '')
    // La clé et la grille, derrière le code du formateur (audit, tour 2, F1) :
    // l'employé ne voit ni le geste attendu ni la réponse modèle, et ne peut
    // pas se noter lui-même.
    + '<div class="bloc formateur"><b>' + esc(FR.pour_formateur) + '</b>'
    + '<div class="code" style="margin-top:8px"><label for="codeF">' + esc(FR.code_formateur) + '</label><input id="codeF" inputmode="numeric" maxlength="6" autocomplete="off">'
    + '<button type="button" class="mf-btn" id="okF"><span>' + esc(FR.ouvrir) + '</span></button></div><p class="retro non" id="errF" aria-live="polite"></p>'
    + '<div id="zoneF" hidden>'
    + X.D.map((d, i) => '<p style="margin:14px 0 2px">« ' + esc(d.phrase) + ' »</p>'
        + '<p style="margin:0 0 4px;font-size:15px"><b>' + esc(FR.geste_attendu) + ' :</b> ' + esc(d.geste) + ' — ' + esc(FR.exemple) + ' : ' + esc(d.attendu) + '</p>'
        + (X.blobs[i] ? '<audio controls src="' + X.blobs[i] + '"></audio>' : '<p style="margin:0;color:var(--text-muted)">—</p>')
        + '<div class="choisir3" data-oral="' + i + '">' + D.test.oral.map((o, k) => '<button type="button" class="mf-btn" data-v="' + k + '" aria-pressed="false">' + esc(o) + '</button>').join('') + '</div>').join('')
    + '<p style="margin:16px 0 4px">' + esc(FR.confirmer_palier) + '</p><div class="choisir3" data-conf="1">'
    + D.test.paliers.map(p => '<button type="button" class="mf-btn" data-v="' + p.k + '" aria-pressed="false">' + esc(p.t) + '</button>').join('') + '</div></div></div>'
    + '<div><button type="button" class="mf-btn" id="refaire"><span>' + T('refaire_test') + '</span></button></div></div>';
  const maj = () => { const hh = histo(); hh[hh.length - 1] = entree; garderHisto(hh); };
  const ouvrirF = () => {
    if (document.getElementById('codeF').value.trim() === D.test.code_formateur) {
      document.getElementById('zoneF').hidden = false; document.getElementById('errF').textContent = '';
      document.getElementById('codeF').closest('.code').remove();
    } else document.getElementById('errF').textContent = FR.code_faux; };
  document.getElementById('okF').onclick = ouvrirF;
  document.getElementById('codeF').onkeydown = e => { if (e.key === 'Enter') ouvrirF(); };
  app.querySelectorAll('[data-oral] button').forEach(b => b.onclick = () => {
    const i = +b.parentNode.dataset.oral; entree.oral[i] = +b.dataset.v; maj();
    b.parentNode.querySelectorAll('button').forEach(x => x.setAttribute('aria-pressed', String(x === b)));
    // Le geste noté par le formateur remonte au direct (O3, O4 évalués).
    rapporter({zone: 'test' + (X.f + 1) + '-D-' + X.D[i].id, exo: 'test-D', exoNum: 'Test · forme ' + (X.f + 1) + ' · oral', exoTitre: FR.partie_d, section: 'test',
      type: 'oral', enonce: X.D[i].geste, bonne: '', reponse: '', ok: +b.dataset.v === 0, essais: 0}); });
  app.querySelectorAll('[data-conf] button').forEach(b => b.onclick = () => {
    entree.confirme = b.dataset.v; maj();
    b.parentNode.querySelectorAll('button').forEach(x => x.setAttribute('aria-pressed', String(x === b))); });
  document.getElementById('versMag').onclick = () => { niveauJeu = entree.confirme || pal; ecranMagasin(); };
  document.getElementById('versMots').onclick = () => { filtre = ''; lancer('ecoute'); };
  document.getElementById('refaire').onclick = ecranTest;
  document.getElementById('retour').onclick = ecranAccueil;
  document.getElementById('chLangue').onclick = ecranLangue;
  window.scrollTo(0, 0);
}
window.__francoeur.test = () => X;
/* ── Le magasin (étape 4) ──────────────────────────────────────────────
   L'employé est le vendeur ; l'avatar est le client. La conversation passe par
   /api/jeu-de-role (scénario « magasin », source build/contenu/…/clients.py) :
   il faut un code d'élève ou de séance. Le client ouvre chaque réplique par
   son humeur entre crochets ; l'écran la retire et change le visage. Le mot
   FIN à la fin d'une réplique clôt la visite. Micro et voix ne tournent jamais
   ensemble : ouvert, le micro dégrade la sortie audio de Chrome. */
const M = D.magasin;
let codeAcces = new URLSearchParams(location.search).get('code') || '';
try { codeAcces = codeAcces || localStorage.getItem('francoeur-code') || ''; } catch(e) {}
let niveauJeu = null;
function niveauDuTest() { const h = histo(); const d = h[h.length - 1]; return d ? (d.confirme || d.palier) : null; }

function ecranMagasin() {
  niveauJeu = niveauJeu || niveauDuTest();
  if (!codeAcces) {
    app.innerHTML = tete(T('magasin'), T('code_aide'), true, 'accueil')
      + '<div class="code"><label for="codeIn"><b>' + T('code_acces') + '</b></label><input id="codeIn" maxlength="8" autocomplete="off">'
      + '<button type="button" class="mf-btn mf-btn--pri" id="codeOk"><span>' + T('entrer') + '</span></button></div>';
    document.getElementById('codeOk').onclick = () => {
      codeAcces = document.getElementById('codeIn').value.trim().toUpperCase();
      if (!codeAcces) return;
      try { localStorage.setItem('francoeur-code', codeAcces); } catch(e) {}
      ecranMagasin();
    };
  } else {
    const l = L();
    const dispo = M.clients.filter(c => !niveauJeu || c.paliers.includes(niveauJeu));
    app.innerHTML = tete(T('magasin'), T('choisir_client'), true, 'accueil')
      // Avant d'entrer : l'exemple travaillé et les phrases (audit C4).
      + '<div class="bloc avant"><p style="margin:0 0 8px">' + T('avant_entrer') + '</p>'
      + '<div class="ecoute" style="justify-content:flex-start;margin:0"><button type="button" class="mf-btn" id="versGestes"><span>' + T('gestes') + '</span></button>'
      + '<button type="button" class="mf-btn" id="versFiche"><span>' + T('mes_phrases') + '</span></button></div></div>'
      + '<p style="margin:10px 0 4px"><b>' + T('niveau_jeu') + '</b>' + (niveauJeu ? '' : ' — ' + T('faire_test')) + '</p>'
      + '<div class="choisir3" id="niv">' + D.test.paliers.map(p => '<button type="button" class="mf-btn" data-v="' + p.k + '" aria-pressed="' + (p.k === niveauJeu) + '">' + esc(p.t) + '</button>').join('') + '</div>'
      + '<div class="clients">' + dispo.map(c => { const tr = l && l.ui['carte_' + c.id];
          return '<button type="button" class="client" data-c="' + c.id + '"><img src="' + c.p.neutre + '" alt=""><b>' + esc(c.nom) + '</b><span>' + esc(c.carte) + '</span>'
            + (tr ? '<span class="appui" dir="' + (l.rtl ? 'rtl' : 'ltr') + '">' + esc(tr) + '</span>' : '') + '</button>'; }).join('') + '</div>';
    document.getElementById('versGestes').onclick = ecranGestes;
    document.getElementById('versFiche').onclick = ecranFichePoche;
    app.querySelectorAll('#niv button').forEach(b => b.onclick = () => { niveauJeu = b.dataset.v; ecranMagasin(); });
    app.querySelectorAll('[data-c]').forEach(b => b.onclick = () => { if (!niveauJeu) niveauJeu = 'debutant'; scene(b.dataset.c); });
  }
  document.getElementById('retour').onclick = ecranAccueil;
  document.getElementById('chLangue').onclick = ecranLangue;
  window.scrollTo(0, 0);
}

let S = null;   // la visite en cours
function scene(id) {
  const c = M.clients.find(x => x.id === id);
  S = {c, hist: [], humeur: 'neutre', fini: false, sansLire: false, fem: c.voix === 'jr_feminin'};
  app.innerHTML = tete(esc(c.nom), esc(c.carte), true, 'magasin')
    + '<div class="scene"><div class="avatar"><img id="av" src="' + c.p.neutre + '" alt="' + esc(c.nom) + '"><p class="nom" id="hum" aria-live="polite"></p></div>'
    + '<div><div class="choisir3"><button type="button" class="mf-btn" id="sansLire" aria-pressed="false"><span>' + T('ecouter_sans_lire') + '</span></button></div>'
    // Les phrases du vendeur, repliables, sous la main pendant la visite (audit C4).
    + '<details class="bloc phrases-scene"><summary><b>' + T('mes_phrases') + '</b></summary>' + phrasesHTML() + '</details>'
    + '<div class="fil" id="fil" aria-live="polite"></div>'
    + '<div class="saisie"><button type="button" class="mf-btn rec" id="micro"><span>' + T('parler') + '</span></button>'
    + '<input id="txt" placeholder="' + esc(FR.ecrire) + '"><button type="button" class="mf-btn mf-btn--pri" id="env"><span>' + T('envoyer') + '</span></button></div>'
    + '<div class="suite"><button type="button" class="mf-btn" id="fin"><span>' + T('fini') + '</span></button></div>'
    + '<p class="retro non" id="err"></p></div></div>';
  brancherPhrases(app.querySelector('.phrases-scene'));
  document.getElementById('retour').onclick = () => { arreterTout(); ecranMagasin(); };
  document.getElementById('chLangue').remove();
  document.getElementById('sansLire').onclick = e => { S.sansLire = !S.sansLire; e.currentTarget.setAttribute('aria-pressed', String(S.sansLire)); document.getElementById('fil').classList.toggle('cache', S.sansLire); };
  document.getElementById('env').onclick = () => envoyer(document.getElementById('txt').value);
  document.getElementById('txt').onkeydown = e => { if (e.key === 'Enter') envoyer(e.target.value); };
  document.getElementById('micro').onclick = micro;
  document.getElementById('fin').onclick = bilanMagasin;
  montrerHumeur('neutre');
  window.scrollTo(0, 0);
  tour();   // le client parle le premier, après l'accueil
}
function bulle(qui, texte) {
  const fil = document.getElementById('fil'); if (!fil) return;
  const d = document.createElement('div'); d.className = 'bulle ' + qui;
  d.innerHTML = '<span class="qui">' + (qui === 'vous' ? esc(FR.vous) : esc(S.c.nom)) + '</span><span class="txt">' + esc(texte) + '</span>';
  fil.appendChild(d); d.scrollIntoView({block: 'nearest'});
}
function lireHumeur(t) {
  let h = 'neutre', fin = false;
  const m = t.match(/^\s*\[(neutre|contente?|hesitante?|hésitante?|impatiente?)\]\s*/i);
  if (m) { h = m[1].toLowerCase().normalize('NFD').replace(/[̀-ͯ]/g, '').replace(/e?$/, 'e'); t = t.slice(m[0].length); }
  if (!M.humeurs.includes(h)) h = 'neutre';
  t = t.replace(/\[[^\]]*\]/g, '').trim();
  if (/\bFIN\.?\s*$/.test(t)) { fin = true; t = t.replace(/\s*\bFIN\.?\s*$/, '').trim(); }
  return {h, t, fin};
}
// L'humeur DITE, pas seulement dessinée (audit E2) : sous le visage, et pour
// un lecteur d'écran.
function humeurTexte(h) {
  const f = S.fem, n = S.c.nom;
  return n + ' ' + ({neutre: FR.humeur_neutre, contente: f ? FR.humeur_contente_f : FR.humeur_contente,
    hesitante: FR.humeur_hesitante, impatiente: FR.humeur_impatiente})[h];
}
function montrerHumeur(h) {
  S.humeur = h;
  const av = document.getElementById('av'); if (av) { av.src = S.c.p[h]; av.alt = humeurTexte(h); }
  const hum = document.getElementById('hum'); if (hum) hum.textContent = humeurTexte(h);
}
async function tour() {
  const err = document.getElementById('err'); err.textContent = '';
  const attente = document.createElement('p'); attente.className = 'attente'; attente.textContent = FR.attente_client;
  document.getElementById('fil').appendChild(attente);
  try {
    const r = await fetch('/api/jeu-de-role', {method: 'POST', headers: {'Content-Type': 'application/json'},
      body: JSON.stringify({code: codeAcces, scenario: 'magasin', cas: S.c.id, role: 'vendeur', niveau: niveauJeu, historique: S.hist})});
    const d = await r.json().catch(() => ({}));
    attente.remove();
    if (!r.ok) {
      if (r.status === 401) { codeAcces = ''; try { localStorage.removeItem('francoeur-code'); } catch(e) {} err.textContent = FR.code_refuse; }
      else err.textContent = d.error || FR.erreur_reseau;
      return;
    }
    if (d.ouverture) { S.hist.push({role: 'user', contenu: d.ouverture}); bulle('vous', d.ouverture); }
    S.hist.push({role: 'assistant', contenu: d.reponse});
    const {h, t, fin} = lireHumeur(d.reponse);
    montrerHumeur(h); bulle('client', t); dire(t);
    if (fin) {
      // Le client a dit au revoir : on laisse la dernière réplique à l'écran,
      // et c'est l'employé qui passe au bilan (audit, tour 2, G2).
      S.fini = true;
      ['txt', 'env', 'micro'].forEach(id => { const x = document.getElementById(id); if (x) x.disabled = true; });
      const suite = document.querySelector('.scene .suite');
      if (suite) { suite.innerHTML = '<button type="button" class="mf-btn mf-btn--pri" id="versBilan"><span>' + T('voir_bilan') + '</span>' + ICO.suiv + '</button>';
        document.getElementById('versBilan').onclick = bilanMagasin; }
    }
  } catch(e) { attente.remove(); err.textContent = FR.erreur_reseau; }
}
function envoyer(texte) {
  texte = (texte || '').trim(); if (!texte || S.fini) return;
  arreterTout();
  document.getElementById('txt').value = '';
  S.hist.push({role: 'user', contenu: texte}); bulle('vous', texte);
  tour();
}
async function dire(t) {
  if (!t) return;
  try {
    const palier = M.debit[niveauJeu] || null;
    const r = await fetch('/api/voix', {method: 'POST', headers: {'Content-Type': 'application/json'},
      body: JSON.stringify({code: codeAcces, texte: t, role: 'vendeur', personnage: S.c.voix, palier})});
    if (!r.ok) throw new Error();
    const url = URL.createObjectURL(await r.blob());
    if (audio) audio.pause();
    audio = new Audio(url);
    // Le serveur ralentit lui-même quand il le sait (en-tête X-Palier) ; sinon on étire ici.
    if (palier && !r.headers.get('X-Palier')) { audio.preservesPitch = true; audio.playbackRate = 0.8; }
    audio.play().catch(() => {});
  } catch(e) {
    // Pas de repli sur la voix du navigateur : toutes les voix de la trousse
    // sont d'Azure (décision de Daniel, 24 septembre 2026). Une panne se dit.
    const err = document.getElementById('err'); if (err) err.textContent = FR.voix_indispo;
  }
}
let reco = null;
function arreterTout() { if (audio) audio.pause(); recoFini = true; clearTimeout(recoMinuterie); if (reco) { const r = reco; reco = null; r.onend = null; try { r.abort(); } catch(e) {} } }
// Le micro du magasin. Il était réglé pour UNE phrase (continuous: false) :
// Chrome le fermait à la première pause, au milieu d'une réponse d'apprenant,
// qui hésite par définition (Daniel, 24 septembre 2026). Désormais il écoute en
// continu, ACCUMULE ce qui est dit, se relance si le navigateur le coupe, et ne
// s'arrête que sur « Arrêter » ou après un vrai silence (SILENCE_MS).
const SILENCE_MS = 4000, SILENCE_DEBUT_MS = 9000;
let recoFini = true, recoMinuterie = null;
function micro() {
  const R = window.SpeechRecognition || window.webkitSpeechRecognition;
  const b = document.getElementById('micro'), txt = document.getElementById('txt');
  if (!R) { document.getElementById('err').textContent = FR.micro_refuse; return; }
  if (reco) { recoFini = true; reco.stop(); return; }
  if (audio) audio.pause();
  let acquis = '';
  recoFini = false;
  const attendre = ms => { clearTimeout(recoMinuterie); recoMinuterie = setTimeout(() => { recoFini = true; if (reco) reco.stop(); }, ms); };
  const terminer = () => {
    clearTimeout(recoMinuterie); reco = null; b.innerHTML = '<span>' + T('parler') + '</span>';
    const dit = txt.value.trim(); if (dit) envoyer(dit);
  };
  const demarrer = () => {
    reco = new R(); reco.lang = 'fr-CA'; reco.interimResults = true; reco.continuous = true;
    reco.onresult = e => {
      let provisoire = '';
      for (let i = e.resultIndex; i < e.results.length; i++) {
        const t = e.results[i][0].transcript.trim();
        if (e.results[i].isFinal) acquis = (acquis + ' ' + t).trim(); else provisoire += ' ' + t;
      }
      txt.value = (acquis + provisoire).trim();
      attendre(SILENCE_MS);
    };
    // Le navigateur coupe parfois de lui-même (fin de session, pause) : on
    // reprend, sauf si l'employé a arrêté ou que le silence a duré.
    reco.onend = () => { if (!recoFini) { try { demarrer(); return; } catch (e) {} } terminer(); };
    reco.onerror = ev => {
      if (ev.error === 'no-speech' || ev.error === 'aborted') return;
      recoFini = true; document.getElementById('err').textContent = FR.micro_refuse;
    };
    reco.start();
  };
  txt.value = '';
  demarrer(); attendre(SILENCE_DEBUT_MS);
  b.innerHTML = '<span>' + T('arreter') + '</span>';
}
async function bilanMagasin() {
  arreterTout();
  marquer('visite');
  const mes = S.hist.filter(m => m.role === 'user').map(m => m.contenu).slice(1);   // l'accueil n'est pas de l'employé
  const content = S.humeur === 'contente', f = S.fem;
  const issue = S.c.nom + ' ' + (content ? (f ? FR.parti_content_f : FR.parti_content) : (f ? FR.parti_pas_f : FR.parti_pas));
  app.innerHTML = tete(T('bilan_titre'), '', true, 'magasin')
    + '<div class="resultat"><div class="bloc" style="display:flex;gap:14px;align-items:center"><img src="' + S.c.p[S.humeur] + '" alt="' + esc(humeurTexte(S.humeur)) + '" style="width:110px;border-radius:10px;background:#fff">'
    + '<p style="margin:0;font-weight:800">' + esc(issue) + '</p></div>'
    // Le bilan PAR GESTE, produit par le serveur à partir de la visite (audit
    // E1) — la grammaire passe au second plan.
    + '<div class="bloc"><b>' + T('gestes_titre') + '</b><div id="gestesBilan"><p class="attente">' + esc(FR.bilan_attente) + '</p></div></div>'
    + '<details class="bloc"><summary><b>' + T('vos_phrases') + '</b></summary><div id="corr"><p class="attente">…</p></div></details>'
    + '<div class="ecoute" style="justify-content:flex-start"><button type="button" class="mf-btn mf-btn--pri" id="autre"><span>' + T('autre_client') + '</span></button>'
    + '<button type="button" class="mf-btn" id="versFiche"><span>' + T('mes_phrases') + '</span></button></div></div>';
  document.getElementById('autre').onclick = ecranMagasin;
  document.getElementById('versFiche').onclick = ecranFichePoche;
  document.getElementById('retour').onclick = ecranMagasin;
  document.getElementById('chLangue').onclick = ecranLangue;
  const zone = document.getElementById('gestesBilan');
  if (!mes.length) { zone.innerHTML = '<p>—</p>'; document.getElementById('corr').innerHTML = '<p>—</p>'; return; }
  const nomGeste = id => (M.gestes.find(g => g.id === id) || {nom: id}).nom;
  try {
    const r = await fetch('/api/jeu-de-role', {method: 'POST', headers: {'Content-Type': 'application/json'},
      body: JSON.stringify({code: codeAcces, scenario: 'magasin', cas: S.c.id, role: 'vendeur', niveau: niveauJeu, bilan: true,
        // La première réplique « vendeur » est l'accueil écrit par la page : le
        // bilan ne l'attribue pas à l'employé (audit, tour 3).
        historique: S.hist.slice(1)})});
    const d = await r.json().catch(() => ({}));
    if (!r.ok || !d.bilan) { zone.innerHTML = '<p>' + esc(d.error || FR.erreur_reseau) + '</p>'; }
    else {
      const G = (d.bilan.gestes || []).filter(g => g.necessaire).concat((d.bilan.gestes || []).filter(g => !g.necessaire));
      zone.innerHTML = (d.bilan.resume ? '<p>' + esc(d.bilan.resume) + '</p>' : '') + '<ul class="gestes-bilan">' + G.map(g => {
        const etat = !g.necessaire ? 'inutile' : g.fait ? 'fait' : 'manque';
        return '<li class="' + etat + '"><span class="marque">' + (etat === 'fait' ? '✓' : etat === 'manque' ? '→' : '·') + '</span><span><b>' + esc(nomGeste(g.id)) + '</b> — '
          + esc(etat === 'fait' ? FR.geste_fait : etat === 'manque' ? FR.geste_manque : FR.geste_inutile)
          + (g.citation ? '<small>« ' + esc(g.citation) + ' »</small>' : '') + (etat === 'manque' && g.conseil ? '<small>' + esc(g.conseil) + '</small>' : '') + '</span></li>'; }).join('') + '</ul>';
      G.filter(g => g.necessaire).forEach(g => rapporter({zone: 'mag-' + S.c.id + '-' + g.id, exo: 'magasin', exoNum: 'Magasin · ' + niveauJeu,
        exoTitre: 'Le magasin', section: 'magasin', type: 'geste', enonce: nomGeste(g.id) + ' — ' + S.c.nom, bonne: '', reponse: '', ok: !!g.fait, essais: 0}));
    }
  } catch(e) { zone.innerHTML = '<p>' + esc(FR.erreur_reseau) + '</p>'; }
  rapporter({zone: 'mag-' + S.c.id + '-' + niveauJeu, exo: 'magasin', exoNum: 'Magasin · ' + niveauJeu,
    exoTitre: 'Le magasin', section: 'magasin', type: 'magasin', enonce: 'Visite : ' + S.c.nom,
    bonne: '', reponse: '', ok: content, essais: 0});
  const corr = document.getElementById('corr');
  try {
    const r = await fetch('/api/correct-french', {method: 'POST', headers: {'Content-Type': 'application/json'},
      body: JSON.stringify({code: codeAcces, text: mes.join(' '),
        question: "Vous êtes vendeur dans un magasin de vêtements et vous répondez à un client."})});
    const d = await r.json();
    if (!r.ok) { corr.innerHTML = '<p>' + esc(d.error || FR.erreur_reseau) + '</p>'; return; }
    corr.innerHTML = '<p style="font-size:18px;font-weight:700;color:var(--text-strong)">' + esc(d.corrige) + '</p>'
      + (d.erreurs || []).map(e => '<p style="margin:4px 0">· ' + esc(e.explication) + '</p>').join('');
  } catch(e) { corr.innerHTML = '<p>' + esc(FR.erreur_reseau) + '</p>'; }
}

window.__francoeur.magasin = () => S;
/* ── Le rapport au portail (étape 5, le pilote) ────────────────────────
   Ouverte depuis le portail ou une séance sans compte, la page connaît le code
   (dans sa propre adresse, relayé par viewer.html) et le numéro d'activité
   (dans l'adresse du visualiseur). Elle rapporte alors chaque réponse FERMÉE au
   direct de la classe — l'événement `zone_repondue` que les modules envoient
   déjà, sur /api/student/progress. Rien d'autre : ni les phrases libres du
   magasin, ni l'oral, ni la langue choisie. Ouverte hors du portail, elle ne
   rapporte rien et marche pareil. Le diagnostic didactique lit ces traces :
   un item raté par la moitié du groupe accuse l'item, pas le groupe. */
const CTX = (function () {
  try {
    const moi = new URLSearchParams(location.search);
    let parent = new URLSearchParams('');
    try { parent = new URLSearchParams(window.parent.location.search); } catch (e) {}
    const code = moi.get('code') || parent.get('code');
    const id = parseInt(moi.get('activityId') || parent.get('activityId'), 10);
    return code && id ? {code, activityId: id} : null;
  } catch (e) { return null; }
})();
if (CTX && !codeAcces) codeAcces = CTX.code;
function rapporter(o) {
  if (!CTX) return;
  const corps = Object.assign({code: CTX.code, activityId: CTX.activityId,
    activityTitle: 'Maison Francœur', event: 'zone_repondue'}, o);
  fetch('/api/student/progress', {method: 'POST', headers: {'Content-Type': 'application/json'},
    body: JSON.stringify(corps)}).catch(() => {});
}
function rapporterSerie(zones, premier) {
  if (!CTX) return;
  fetch('/api/student/progress', {method: 'POST', headers: {'Content-Type': 'application/json'},
    body: JSON.stringify({code: CTX.code, activityId: CTX.activityId, event: 'exercise_completed',
      zones, zonesDone: zones, firstTry: premier, totalErrors: zones - premier})}).catch(() => {});
}
const etiquette = id => { const m = D.mots.find(x => x.id === id); return m ? m.mot : String(id); };
const carteTexte = v => v ? (v.mot + ' · ' + v.cmot + (v.t ? ' · ' + v.t : '')) : '';
window.__francoeur.ctx = () => CTX;

window.__francoeur.lireHumeur = lireHumeur;
// Le contrôle de la règle des 12 px : pour chaque paire de boutons visibles qui
// se chevauchent verticalement (même rangée), la distance horizontale entre
// eux ; et pour ceux d'une même colonne, la distance verticale. Rend les paires
// sous le seuil. Sert aux vérifications, jamais à l'élève.
const ESPACE_MIN = 12;
window.__francoeur.espaces = () => {
  // Une fenêtre ouverte (la fiche d'un article) cache ce qui est dessous : on
  // ne mesure alors que ses propres boutons.
  const racine = !document.getElementById('fiche').hidden ? document.getElementById('fiche') : document;
  const b = [...racine.querySelectorAll('button, .mf-btn, a.mf-btn')].filter(x => x.offsetParent && x.getBoundingClientRect().width > 0
      && !(x.closest('details:not([open])') && !x.closest('summary')))
    .map(x => ({x, r: x.getBoundingClientRect()}));
  const fautes = [];
  for (let i = 0; i < b.length; i++) for (let j = i + 1; j < b.length; j++) {
    const A = b[i].r, B = b[j].r;
    if (b[i].x.contains(b[j].x) || b[j].x.contains(b[i].x)) continue;
    const vChev = Math.min(A.bottom, B.bottom) - Math.max(A.top, B.top), hChev = Math.min(A.right, B.right) - Math.max(A.left, B.left);
    let d = null;
    if (vChev > 4) d = Math.max(B.left - A.right, A.left - B.right);
    else if (hChev > 4) d = Math.max(B.top - A.bottom, A.top - B.bottom);
    if (d !== null && d < ESPACE_MIN - 0.5) fautes.push({d: Math.round(d), a: (b[i].x.innerText || b[i].x.id).trim().slice(0, 24), b: (b[j].x.innerText || b[j].x.id).trim().slice(0, 24)});
  }
  return fautes;
};



/* ── Ouvrir un état précis par l'adresse ───────────────────────────────
   Pour la démonstration en rencontre, le guide du formateur et les captures :
   ?langue=es&ecran=planche&p=hauts&a=veste&voir=1 · ecran=exercice&x=client ·
   ecran=magasin (la liste des clients, sans code ni appel au serveur). */
function ouvrirParAdresse() {
  const q = new URLSearchParams(location.search), e = q.get('ecran');
  if (q.get('langue')) { langue = q.get('langue'); }
  if (!e) return false;
  if (e === 'langue') { ecranLangue(); return true; }
  if (!langue) langue = 'fr';
  if (e === 'rayons') ecranRayons();
  else if (e === 'planche') {
    ecranPlanche(q.get('p') || 'hauts');
    const i = courante.findIndex(m => m.id === q.get('a'));
    if (i >= 0) { ouvrir(i); if (audio) audio.pause(); if (q.get('voir')) document.getElementById('voir')?.click(); }
  }
  else if (e === 'exercices') ecranExercices();
  else if (e === 'gestes') ecranGestes();
  else if (e === 'fiche') ecranFichePoche();
  else if (e === 'exercice') { lancer(q.get('x') || 'client'); if (audio) audio.pause(); }
  else if (e === 'test') ecranTest();
  else if (e === 'magasin') {
    niveauJeu = q.get('niveau') || 'aise';
    if (!codeAcces) codeAcces = 'DEMO';   // la liste seulement : aucun appel n'est fait ici
    ecranMagasin();
  }
  else ecranAccueil();
  return true;
}
if (!ouvrirParAdresse()) { if (langue) ecranAccueil(); else ecranLangue(); }
</script>
</body>
</html>
"""

if __name__ == "__main__":
    main()
