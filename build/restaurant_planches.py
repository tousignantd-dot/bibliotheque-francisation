#!/usr/bin/env python3
"""Les planches de Chez Jocelyne — l'écran de l'employé de restaurant (étape 1).

    python3 build/restaurant_planches.py   # → modules-autonomes/restaurant-planches/index.html

Produite, jamais écrite à la main. Même parcours que la Maison Francœur
(francoeur_planches.py), réduit à l'étape 1 — les exercices viendront à
l'étape 2, sur ce même écran. Elle lit, et rien d'autre :
  build/contenu/entreprise-restaurant/lexique.py        les mots, les 12 planches
  build/contenu/entreprise-restaurant/decor.py          les zones du poste
  build/contenu/entreprise-restaurant/traductions.json  espagnol et anglais, figés
  build/contenu/entreprise-restaurant/identite.py       le nom, le secteur
  assets/interactive/restaurant/{croquis,sons}/         ce qui existe sur le disque

LE PARCOURS : la langue (Français seulement, Español, English ; gardée sous
`francisation-langue`, la clé des modules) → les planches, et d'abord le POSTE
(le décor : on touche la ligne, le passe, la plonge) → une planche numérotée →
un mot : le croquis, le mot d'ici, l'autre, Écouter, « Voir dans ma langue »
MASQUÉ par défaut, le piège.

LES TROIS COUCHES : le mot reste en français en tête ; la consigne de l'écran
en français, l'appui DESSOUS ; la traduction du mot masquée par défaut.

ÉTATS PAR ADRESSE (démo, captures) : ?langue=es&planche=ustensiles&mot=poele,
?planche=poste. `window.__resto` expose les données aux contrôles.
"""
import html, json, pathlib, re, sys

RACINE = pathlib.Path(__file__).resolve().parent.parent
CONTENU = RACINE / "build" / "contenu" / "entreprise-restaurant"
sys.path.insert(0, str(CONTENU))
from lexique import LEXIQUE, PLANCHES, verifier  # noqa: E402
from decor import ZONES  # noqa: E402
import identite as IDE  # noqa: E402
import exercices as EX  # noqa: E402
import test as TE  # noqa: E402
import situations as SI  # noqa: E402
sys.path.insert(0, str(RACINE / "build"))
from restaurant_traductions import INTERFACE  # noqa: E402  (le français de l'écran : une seule source)

CROQUIS = RACINE / "assets" / "interactive" / "restaurant" / "croquis"
SONS = RACINE / "assets" / "interactive" / "restaurant" / "sons"
SORTIE = RACINE / "modules-autonomes" / "restaurant-planches" / "index.html"
URL = "/assets/interactive/restaurant"

# Incrémenter après toute image ou tout son refait : même nom, même adresse,
# le navigateur servirait l'ancien sans rien dire.
MEDIA_V = "5"   # 5 : quatre actes réécrits (audit, tour 4), 30 sept. 2026


def donnees():
    trad_f = CONTENU / "traductions.json"
    trad = json.loads(trad_f.read_text(encoding="utf-8")) if trad_f.exists() else {}
    lex = {e[0] for e in LEXIQUE}
    assert all(z[0] in lex for z in ZONES), "zone du décor absente du lexique"
    zones = {z[0]: z[1:] for z in ZONES}
    mots = []
    for ident, planche, mot, autre, dessin, note in LEXIQUE:
        m = {"id": ident, "p": planche, "mot": mot, "autre": autre, "note": note,
             "piege": note.startswith("PIÈGE")}
        if dessin == "croquis" and (CROQUIS / f"{ident}.jpg").exists():
            m["img"] = f"{URL}/croquis/{ident}.jpg?v={MEDIA_V}"
        if ident in zones:
            m["zone"] = zones[ident]
        if (SONS / f"{ident}.mp3").exists():
            m["son"] = f"{URL}/sons/{ident}.mp3?v={MEDIA_V}"
        if (SONS / "autre" / f"{ident}.mp3").exists():
            m["autre_son"] = f"{URL}/sons/autre/{ident}.mp3?v={MEDIA_V}"
        mots.append(m)
    langues = [{"c": c, "loc": trad[c]["loc"], "relu": trad[c]["relu"], "rtl": trad[c].get("rtl", False),
                "ui": trad[c].get("interface", {}),
                # Le modèle a préfixé les pièges tantôt « Atención: », tantôt
                # « Attention: » ou « Careful: » : l'écran dit déjà « Attention ».
                "mots": {k: [t["mot"], re.sub(r"^(Atención|Attention|Careful|Cuidado)\s*:\s*", "", t["note"])]
                         for k, t in trad[c]["mots"].items()}}
               for c in IDE.LANGUES_APPUI if c in trad]
    return {"planches": [{"k": k, "t": t, "poste": p} for k, t, p in PLANCHES],
            "mots": mots, "langues": langues,
            "poste": f"{URL}/croquis/poste.jpg?v={MEDIA_V}",
            "zones": [z[0] for z in ZONES], "ex": exercices(mots), "test": le_test(mots),
            "service": le_service()}


def le_service():
    """L'étape 4 (situations.py). Les portraits attendent le crédit d'images :
    chaque situation montre le décor de sa porte (le poste, ou la salle)."""
    SI.verifier()
    return {"situations": [{"id": i, "porte": p, "nom": n, "voix": v, "paliers": pa, "gestes": g,
                            "cuisine": bool(SI.REPONSES_CUISINE.get(i))}
                           for i, p, n, v, pa, _c, g, _po, _f in SI.SITUATIONS],
            "gestes": [{"id": g["id"], "phrase": g["phrase"]} for g in SI.GESTES],
            "portes": {p: {"scenario": v["scenario"], "eleve": v["eleve"]} for p, v in SI.PORTES.items()},
            "decor": {"cuisine": f"{URL}/croquis/poste.jpg?v={MEDIA_V}", "salle": f"{URL}/croquis/banquette.jpg?v={MEDIA_V}"},
            "humeurs": SI.HUMEURS, "debit": SI.DEBIT_JEU}


def s_(chemin):
    assert (SONS / chemin).exists(), f"voix manquante : {chemin}"
    return f"{URL}/sons/{chemin}?v={MEDIA_V}"


def exercices(mots):
    """L'étape 2 : le contenu d'exercices.py, avec ses sons. Le carré latin des
    commandes se construit ICI, et le build refuse une carte devinable."""
    EX.verifier()
    cons = [{"id": i, "son": s_(f"chef/{i}.mp3"), "phrase": ph, "q": "q_" + i, "o": [b] + d,
             "redit": r, "redit_son": s_(f"redit/{i}.mp3")} for i, ph, _q, b, d, r in EX.CONSIGNES]
    com = []
    for i, _v, ph, bon, autre, r in EX.COMMANDES:
        com.append({"id": i, "son": s_(f"commandes/{i}.mp3"), "phrase": ph, "cartes": cartes_commande(i, bon, autre),
                    "redit": r, "redit_son": s_(f"redit/{i}.mp3")})
    alg = [{"id": i, "son": s_(f"allergies/{i}.mp3"), "phrase": ph, "qui": "qui_" + qui, "contre": c,
            "actes": [{"k": f"acte_{i}_{n}", "s": st, "p": f"pourquoi_{i}_{n}" if pq else "",
                       "son": s_(f"actes/{i}-{n}.mp3")} for n, (_a, st, pq) in enumerate(actes)]}
           for i, qui, _v, ph, c, actes in EX.ALLERGIES]
    return {"consignes": cons, "commandes": com, "allergies": alg,
            "pieges": [{"id": i, "o": [i] + c} for i, c in EX.PIEGES], "ordinaires": EX.ORDINAIRES,
            "regle": [s_(f"regle/{n}.mp3") for n in range(1, len(EX.REGLE) + 4)],   # 3 gestes, préférence, cuisine, critère
            "formules": [{"k": k, "son": s_(f"redit/{x}.mp3")} for k, _t, x in EX.FORMULES],
            "changements": EX.CHANGEMENTS}


def cartes_commande(i, bon, autre):
    """Les cartes d'une commande, la bonne en premier. Exercices ET test."""
    a, m, g = bon
    if g is None:
        # La cuisson : trois cartes du même plat, la cuisson écrite et dessinée.
        cartes = [[a, m, m]] + [[a, c, c] for c in EX.CUISSONS if c != m]
    else:
        a2, m2, g2 = autre
        # (audit, tour 1, D4) Une carte ne diffère de la bonne QUE par le
        # changement : reconnaître le plat et l'ingrédient ne suffit plus.
        # Et chaque valeur revient deux fois : le vote majoritaire reste nul.
        cartes = [[a, m, g], [a, m2, g], [a2, m, g2], [a2, m2, g2]]
        assert any(c[0] == a and c[2] == g and c[1] != m for c in cartes[1:]), i
        for trait in range(3):
            valeurs = [c[trait] for c in cartes]
            assert valeurs.count(cartes[0][trait]) == 2, f"{i} : trait {trait} devinable"
    return cartes


def le_test(mots):
    """L'étape 3 (test.py). Tout se fige ici — choix et places —, pour que les
    deux formes restent parallèles et qu'une passation ressemble à l'autre."""
    import random
    TE.verifier()
    par_id = {m["id"]: m for m in mots}
    avec = [m for m in mots if "img" in m]
    formes = {}
    for f in (1, 2):
        alea = random.Random(f"resto-test-{f}")
        derniere = {3: None, 4: None}
        def place(n):
            # (audit du test, tour 1, D4) au hasard, jamais deux fois la même de
            # suite — et sans blocs, dont la dernière place se déduisait.
            k = alea.choice([x for x in range(n) if x != derniere[n]])
            derniere[n] = k
            return k
        def poser(bonne, autres, n):
            k = place(n); o = list(autres); o.insert(k, bonne); return o, k
        A = {}
        for cran in (1, 2, 3):
            items = []
            for x in TE.A[f][cran]:
                ident, contrastes = x if isinstance(x, tuple) else (x, None)
                m = par_id[ident]
                if contrastes is None:
                    meme = [y["id"] for y in avec if y["p"] == m["p"] and y["id"] != ident and y["mot"] != m["mot"]]
                    autre = [y["id"] for y in avec if y["p"] != m["p"]]
                    pool = meme if cran == 2 else autre
                    contrastes = alea.sample(pool, 3)
                o, k = poser(ident, contrastes, 4)
                items.append({"id": ident, "son": s_(f"test/a-{ident}.mp3"), "o": o, "bonne": k})
            A[cran] = items
        B = []
        for i, ph, _q, b, d in TE.B_CHEF[f]:
            o, k = poser(b, d, 4)
            B.append({"id": i, "type": "chef", "son": s_(f"test/{i}.mp3"), "q": "q_" + i, "o": o, "bonne": k})
        for i, _v, ph, bon, autre in TE.B_COMMANDE[f]:
            c = cartes_commande(i, bon, autre)
            o, k = poser(c[0], c[1:], len(c))
            B.append({"id": i, "type": "commande", "son": s_(f"test/{i}.mp3"), "cartes": o, "bonne": k})
        C = []
        for i, qui, _v, ph, contre, actes in TE.C[f]:
            juste = next(n for n, (_a, st) in enumerate(actes) if st == "juste")
            autres = [n for n in range(3) if n != juste]
            o, k = poser(juste, autres, 3)
            C.append({"id": i, "son": s_(f"test/{i}.mp3"), "qui": "qui_" + qui,
                      "actes": [{"k": f"acte_{i}_{n}", "s": actes[n][1]} for n in o], "bonne": k})
        D = [{"id": i, "qui": "qui_" + qui, "son": s_(f"test/{i}.mp3"), "modele": s_(f"test/{i}-modele.mp3"),
              "attendu": modele, "phrase": ph} for i, qui, _v, ph, modele in TE.D[f]]
        formes[f] = {"A": A, "B": B, "C": C, "D": D}
    return {"formes": formes, "code": TE.CODE_FORMATEUR, "oral_redit": TE.ORAL_REDIT, "oral_langue": TE.ORAL_LANGUE,
            "regles": {"debutant_a": TE.DEBUTANT_A, "debutant_b": TE.DEBUTANT_B, "aise_b": TE.AISE_B,
                       "oral_aise": TE.ORAL_AISE, "oral_debutant": TE.ORAL_DEBUTANT,
                       "valide": TE.A_VALIDE, "arret": TE.A_ARRET}}


def main():
    verifier()
    d = donnees()
    page = (GABARIT.replace("%%NOM%%", html.escape(IDE.NOM))
            .replace("%%SURTITRE%%", html.escape(IDE.SURTITRE))
            .replace("%%SECTEUR%%", html.escape(IDE.SECTEUR))
            .replace("%%SECTEUR_COURT%%", html.escape(IDE.SECTEUR_COURT))
            .replace("%%FR%%", json.dumps(INTERFACE, ensure_ascii=False))
            .replace("%%DONNEES%%", json.dumps(d, ensure_ascii=False).replace("</", "<\\/")))
    SORTIE.parent.mkdir(parents=True, exist_ok=True)
    SORTIE.write_text(page, encoding="utf-8")
    n_img = sum("img" in m for m in d["mots"])
    n_son = sum("son" in m for m in d["mots"])
    print(f"{len(d['mots'])} mots · {n_img} croquis · {n_son} voix · "
          f"{len(d['langues'])} langues d'appui → {SORTIE.relative_to(RACINE)}")


GABARIT = r"""<!DOCTYPE html>
<html lang="fr">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="color-scheme" content="light">
<meta name="robots" content="noindex">
<title>%%NOM%% — les mots du restaurant</title>
<link rel="stylesheet" href="/assets/design-system/styles.css">
<link rel="stylesheet" href="/assets/design-system/marque-francis.css">
<link rel="icon" href="/assets/design-system/marque-francis-favicon.svg">
<style>
/* Page produite par build/restaurant_planches.py — ne pas l'éditer. */
:root{
  /* Palette PROVISOIRE « brique » (30 sept. 2026, à faire trancher comme
     Francœur l'a fait sur sa page de couleurs) : pas le mauve de francis.
     Brique pour l'action et l'enseigne, orange pour les pièges, fond crème.
     Brique sur blanc ≈ 9:1 ; texte discret ≥ 4,5:1 sur le fond. */
  --surface-page:#F5F0EA;--surface-card:#FFFFFF;--text-strong:#241A14;--text-body:#241A14;
  --line-200:#E4DAD0;--line-300:#CDBFB2;--accent:#8A2E1C;--text-muted:#5E5046;
  --warn-bg:#FBE9DC;--warn-line:#C8692A;--warn-ink:#8A3F0F;
  --rj-teinte:#8A2E1C;--rj-fond:#F3E3DC}
.fr-barre .fr-desc{color:var(--rj-teinte)}
body{margin:0;background:var(--surface-page);color:var(--text-body);font-family:Nunito,system-ui,sans-serif}
.rj{max-width:1080px;margin:0 auto;padding:18px 16px 60px}
.fr-barre .fr-barre__in{max-width:1080px;padding-left:16px;padding-right:16px}
.rj-tete>div:first-child{flex:1 1 220px}
.rj-tete{display:flex;align-items:flex-start;justify-content:space-between;gap:12px;flex-wrap:wrap;margin-bottom:14px}
.rj-enseigne{font-size:13px;font-weight:800;letter-spacing:.08em;text-transform:uppercase;color:var(--rj-teinte);margin:0}
.rj h1{font-size:28px;line-height:1.15;margin:4px 0 0;color:var(--text-strong)}
/* (audit de design, majeur) L'appui est TOUJOURS plus petit que le français qu'il suit : une seule échelle, relative. */
.appui{display:block;font-size:.85em;font-weight:600;color:var(--text-muted);margin-top:3px}
.appui:empty{display:none}
.appui[dir=rtl],.trad[dir=rtl]{text-align:right}
.btn-rj{font:inherit;font-weight:700;font-size:15px;cursor:pointer;border-radius:10px;padding:9px 14px;min-height:44px;
  border:1px solid var(--line-300);background:var(--surface-card);color:var(--text-strong);display:inline-flex;gap:8px;align-items:center}
.btn-rj:hover{border-color:var(--rj-teinte)}
.btn-rj--pri{background:var(--accent);border-color:var(--accent);color:#fff}
.btn-rj--pri .appui{color:#fff;opacity:.9}
.btn-rj svg{width:20px;height:20px;flex:none}
.btn-rj .appui{font-size:.8em;margin:0}
.btn-rj--pile{flex-direction:column;align-items:flex-start;gap:0}

/* La langue */
.sans-trad{font:inherit;cursor:pointer;text-align:start;margin-top:18px;width:100%;max-width:520px;padding:16px 18px;border-radius:12px;
  border:2px solid var(--rj-teinte);background:var(--rj-fond);font-size:22px;font-weight:900;color:var(--text-strong)}
.sans-trad small{display:block;font-size:15px;font-weight:700;color:var(--rj-teinte)}
.langues{display:grid;grid-template-columns:repeat(auto-fill,minmax(200px,1fr));gap:10px;margin-top:12px;max-width:520px}
.langues button{font:inherit;cursor:pointer;text-align:start;padding:14px 16px;border-radius:12px;
  border:1px solid var(--line-300);background:var(--surface-card);font-size:20px;font-weight:800;color:var(--text-strong)}
.langues button:hover,.langues button:focus-visible{border-color:var(--rj-teinte);background:var(--rj-fond)}

/* Les planches */
.planches{display:grid;grid-template-columns:repeat(auto-fill,minmax(210px,1fr));gap:12px;margin-top:16px}
.pl{font:inherit;cursor:pointer;text-align:start;border:1px solid var(--line-200);background:var(--surface-card);
  border-radius:14px;padding:10px;display:flex;flex-direction:column;gap:6px;color:var(--text-body)}
.pl:hover{border-color:var(--rj-teinte)}
.pl .vign{display:grid;grid-template-columns:repeat(3,1fr);gap:4px;background:#fff;border-radius:10px;padding:6px}
.pl .vign img{width:100%;aspect-ratio:1/1;object-fit:contain;display:block}
.pl .vign i{display:grid;place-items:center;aspect-ratio:1/1;border-radius:6px;background:var(--rj-fond);color:var(--rj-teinte)}
.pl .vign i svg{width:40%;height:40%}
.pl .large{width:100%;aspect-ratio:3/2;object-fit:cover;border-radius:10px;display:block}
.pl.poste{grid-column:1/-1;flex-direction:row;align-items:center;gap:16px;border-color:var(--rj-teinte);box-shadow:inset 4px 0 0 var(--rj-teinte)}
.pl.poste .large{width:min(360px,45%)}
.pl b{font-size:17px;color:var(--text-strong)}
.pl .n{font-size:13px;color:var(--text-muted);font-weight:600}
.etiq{display:inline-block;font-size:12px;font-weight:800;letter-spacing:.04em;text-transform:uppercase;color:var(--rj-teinte);background:var(--rj-fond);border-radius:6px;padding:2px 7px;align-self:flex-start}

/* Une planche */
.planche{display:grid;grid-template-columns:repeat(auto-fill,minmax(150px,1fr));gap:10px;margin-top:14px}
.art{font:inherit;cursor:pointer;position:relative;border:1px solid var(--line-200);background:#fff;border-radius:12px;
  padding:8px 8px 10px;display:flex;flex-direction:column;gap:4px;text-align:center;color:#17181A}
.art:hover,.art:focus-visible{border-color:var(--rj-teinte);box-shadow:0 0 0 3px var(--rj-fond)}
.art .num{position:absolute;top:6px;inset-inline-start:8px;font-size:13px;font-weight:800;color:var(--text-muted)}
.art img{width:100%;aspect-ratio:1/1;object-fit:contain;border-radius:8px}
.art .sans{display:grid;place-items:center;aspect-ratio:3/2;margin:18px 0 10px;background:var(--rj-fond);border-radius:8px;color:var(--rj-teinte)}
.art .sans svg{width:34px;height:34px}
.art .mot{font-weight:800;font-size:16px;line-height:1.2}
.art.piege{box-shadow:inset 0 3px 0 var(--warn-line)}
.art .dec{margin:18px 0 10px}

/* Le décor et ses zones */
.decor{position:relative;margin-top:14px;background:#fff;border-radius:14px;overflow:hidden;border:1px solid var(--line-200)}
.decor img{width:100%;display:block}
.zone{position:absolute;font:inherit;cursor:pointer;border:3px solid transparent;border-radius:10px;background:transparent;padding:0}
.zone:hover,.zone:focus-visible{border-color:var(--rj-teinte);background:rgba(138,46,28,.08)}
.zone .pastille{position:absolute;top:-2px;inset-inline-start:-2px;min-width:26px;height:26px;border-radius:13px;background:var(--rj-teinte);color:#fff;font-weight:900;font-size:14px;display:grid;place-items:center;padding:0 6px}
.zliste{list-style:none;padding:0;margin:14px 0 0;display:grid;grid-template-columns:repeat(auto-fill,minmax(200px,1fr));gap:8px}
.zliste button{font:inherit;cursor:pointer;width:100%;text-align:start;display:flex;gap:10px;align-items:center;border:1px solid var(--line-200);background:var(--surface-card);border-radius:10px;padding:8px 12px;min-height:44px;font-weight:800;color:var(--text-strong)}
.zliste .pastille{flex:none;min-width:26px;height:26px;border-radius:13px;background:var(--rj-teinte);color:#fff;font-size:14px;display:grid;place-items:center}
.mini{position:relative;border-radius:8px;overflow:hidden}
.mini img{width:100%;display:block;aspect-ratio:auto}
.mini i{position:absolute;border:3px solid var(--rj-teinte);border-radius:6px;box-shadow:0 0 0 999px rgba(255,255,255,.45)}

/* La fiche d'un mot */
.fiche{position:fixed;inset:0;background:rgba(23,24,26,.55);display:grid;place-items:center;padding:16px;z-index:10}
.fiche[hidden]{display:none}
.carte{background:var(--surface-card);border-radius:16px;max-width:520px;width:100%;max-height:100%;overflow:auto;padding:16px;box-sizing:border-box}
.carte .grand{background:#fff;border-radius:12px;display:grid;place-items:center;border:1px solid var(--line-200)}
.carte .grand > img{width:100%;max-width:360px;aspect-ratio:1/1;object-fit:contain}
.carte .grand .mini{width:100%}
.carte .grand .sans{padding:26px;color:var(--rj-teinte)}
.carte .grand .sans svg{width:48px;height:48px}
.carte h2{font-size:30px;margin:12px 0 0;color:var(--text-strong)}
.carte .autre{margin:4px 0 0;color:var(--text-muted);font-weight:600;display:flex;gap:8px;align-items:center;flex-wrap:wrap}
.carte .autre b{color:var(--text-body)}
.carte .gestes{display:flex;flex-wrap:wrap;gap:12px;margin:14px 0 6px}
.carte .trad{margin-top:8px;padding:12px 14px;border-radius:12px;background:var(--rj-fond);font-size:22px;font-weight:800;color:var(--text-strong)}
.carte .trad[hidden]{display:none}
.carte .trad small{display:block;font-size:15px;font-weight:600;color:var(--text-body);margin-top:6px}
.carte .trad .relu{display:block;font-size:12px;font-weight:600;color:var(--text-muted);margin-top:8px}
.carte .piege{margin-top:10px;padding:10px 12px;border-radius:10px;background:var(--warn-bg);border:1px solid var(--warn-line);color:var(--warn-ink);font-size:15px;font-weight:700}
.carte .note{margin-top:10px;font-size:15px;color:var(--text-body)}
.carte .nav{display:flex;justify-content:space-between;gap:12px;margin-top:14px}
.ferme{float:inline-end}
/* (audit de design, majeur) 44 px au moins : des mains de cuisine. */
.petit{padding:6px 10px;min-height:44px;min-width:44px;font-size:14px}

.secteur{display:flex;flex-direction:column;align-items:flex-end;text-align:right;line-height:1.15}
.secteur small{font-size:11px;font-weight:800;letter-spacing:.08em;text-transform:uppercase;color:var(--text-muted)}
.secteur b{font-size:19px;font-weight:900;color:var(--rj-teinte)}
.secteur .court{display:none}
@media (max-width:640px){
  .rj h1{font-size:23px}
  .planche,.planches{grid-template-columns:repeat(2,minmax(0,1fr))}
  .pl.poste{flex-direction:column;align-items:stretch}
  .pl.poste .large{width:100%}
  .zone .pastille{min-width:22px;height:22px;font-size:12px}
}
@media (max-width:480px){.secteur small{display:none}.secteur b{font-size:16px}.secteur .long{display:none}.secteur .court{display:inline}}

/* Accueil et exercices (étape 2) */
.accueil{display:grid;grid-template-columns:repeat(auto-fit,minmax(260px,1fr));gap:14px;margin-top:18px}
.porte{font:inherit;cursor:pointer;text-align:start;border:1px solid var(--line-200);background:var(--surface-card);border-radius:16px;padding:14px;display:flex;flex-direction:column;gap:6px;color:var(--text-body)}
.porte:hover{border-color:var(--rj-teinte)}
.porte img{width:100%;aspect-ratio:3/2;object-fit:cover;border-radius:10px}
.porte .porte-ico{display:grid;place-items:center;aspect-ratio:3/2;border-radius:10px;background:var(--rj-fond);color:var(--rj-teinte)}
.porte .porte-ico svg{width:64px;height:64px}
.porte b{font-size:22px;color:var(--text-strong)}
.exos{display:grid;gap:10px;margin-top:14px}
.exo-porte{font:inherit;cursor:pointer;text-align:start;border:1px solid var(--line-200);background:var(--surface-card);border-radius:14px;padding:14px 16px;display:flex;gap:14px;align-items:center;color:var(--text-body)}
.exo-porte:hover{border-color:var(--rj-teinte)}
.exo-porte .rang{flex:none;width:34px;height:34px;border-radius:50%;display:grid;place-items:center;background:var(--rj-fond);color:var(--rj-teinte);font-weight:900}
.exo-porte b{font-size:18px;color:var(--text-strong);display:block}
.exo-porte .sous{display:block;font-size:16px;margin-top:2px}
.exo-porte.pont{border-color:var(--rj-teinte);box-shadow:inset 4px 0 0 var(--rj-teinte)}
.filtre{margin-top:4px;display:flex;gap:10px;align-items:center;flex-wrap:wrap}
.filtre select{font:inherit;font-size:16px;min-height:44px;padding:8px 10px;border-radius:10px;border:1px solid var(--line-300);background:var(--surface-card);color:var(--text-strong);max-width:100%}
.bruit{display:flex;gap:8px;align-items:center;flex-wrap:wrap;margin-top:8px;font-weight:700;font-size:14px}
.bruit [aria-pressed=true]{background:var(--rj-fond);border-color:var(--rj-teinte)}
.jeu{margin-top:12px}
.jeu .barre{height:6px;border-radius:3px;background:var(--line-200);overflow:hidden;margin-bottom:12px}
.jeu .barre i{display:block;height:100%;background:var(--accent)}
.jeu .qui{font-weight:700;text-align:center;margin:0 0 8px}
.jeu .sujet{background:#fff;border-radius:14px;border:1px solid var(--line-200);display:grid;place-items:center;padding:8px;max-width:300px;margin:0 auto 12px}
.jeu .sujet img{width:100%;max-width:260px;aspect-ratio:1/1;object-fit:contain}
.jeu .ecoute{display:flex;gap:12px;justify-content:center;flex-wrap:wrap;margin:6px 0 14px}
.question{font-size:19px;font-weight:800;color:var(--text-strong);margin:4px 0 12px;text-align:center}
.choix{display:grid;gap:10px;grid-template-columns:repeat(4,minmax(0,1fr))}
.choix.mots{grid-template-columns:repeat(2,minmax(0,1fr))}
.choix.actes{grid-template-columns:1fr}
.choix.tickets{grid-template-columns:repeat(2,minmax(0,1fr))}
.opt{position:relative;font:inherit;cursor:pointer;border:2px solid var(--line-200);background:#fff;border-radius:12px;padding:8px;color:#17181A;display:flex;flex-direction:column;align-items:center;justify-content:center;gap:6px;min-height:52px}
.opt:hover{border-color:var(--rj-teinte)}
.opt img{width:100%;aspect-ratio:1/1;object-fit:contain}
.choix.mots .opt{font-size:19px;font-weight:800;padding:12px}
.choix.actes .opt{align-items:flex-start;text-align:start;font-size:17px;font-weight:700;padding:12px 14px}
.ticket{display:grid;grid-template-columns:1fr auto 1fr;align-items:center;gap:6px;width:100%}
.ticket img{width:100%;aspect-ratio:1/1;object-fit:contain}
.ticket .chg{font-weight:900;font-size:17px;border:2px solid #17181A;border-radius:6px;padding:2px 7px;background:#fff;white-space:nowrap}
.opt.faux{border-color:var(--no-line,#C0392B);background:var(--no-bg,#FDECEA);animation:non .3s}
.opt.juste{border-color:var(--ok-line,#2E7D32);background:var(--ok-bg,#E8F5E9)}
.opt[disabled]{cursor:default}
@keyframes non{25%{transform:translateX(-5px)}75%{transform:translateX(5px)}}
@media (prefers-reduced-motion:reduce){.opt.faux{animation:none}}
.retro{margin:12px 0 0;font-weight:800;min-height:1.4em}
.retro.ok{color:var(--ok-ink,#1B5E20)} .retro.non{color:var(--no-ink,#9B1C1C)}
.rappel-regle{display:block;font-weight:600;font-size:15px;color:var(--text-body);margin-top:6px}
.apres .dit{margin:8px 0 0;font-size:17px}
.apres .piege{margin-top:10px;padding:10px 12px;border-radius:10px;background:var(--warn-bg);border:1px solid var(--warn-line);color:var(--warn-ink);font-size:15px;font-weight:700}
.suite{display:flex;justify-content:flex-end;margin-top:12px}
.revele{text-align:center;margin:10px 0}
.revele .gros{font-size:30px;font-weight:900;color:var(--text-strong);margin:6px 0}
.revele .gros-phrase{font-size:22px;font-weight:800;color:var(--text-strong);margin:6px 0}
.gestes-bilan{display:flex;gap:12px;justify-content:center;flex-wrap:wrap;margin-top:12px}
.bilan{text-align:center;padding:20px 0}
.bilan .score{font-size:44px;font-weight:900;color:var(--text-strong);margin:4px 0}
.bilan .graves{font-size:20px;font-weight:900;color:var(--ok-ink,#1B5E20)} .bilan .graves.non{color:var(--no-ink,#9B1C1C)}
.grave-sous{font-weight:700;color:var(--warn-ink)}
.regle{background:var(--surface-card);border:2px solid var(--warn-line);border-radius:14px;padding:16px;margin-top:10px}
.regle h2{margin:0 0 8px;font-size:22px}
.regle p{font-size:17px}
@media (max-width:640px){.choix{grid-template-columns:repeat(2,minmax(0,1fr))}.choix.tickets{grid-template-columns:1fr}.choix.mots{grid-template-columns:1fr}}

.seuil{font-weight:700;color:var(--rj-teinte);margin:0 0 6px}
.seuil-porte{display:block;font-size:13px;font-weight:700;color:var(--rj-teinte);margin-top:4px}
.non-relu{font-size:14px;color:var(--text-muted);margin:6px 0}
.unique{text-align:center;font-weight:800;color:var(--rj-teinte);margin:6px 0 14px}
.regle-liste{padding-left:0;margin:0 0 10px;list-style:none;counter-reset:geste}
.regle-liste li{counter-increment:geste}
.regle-liste li>span:first-child::before{content:counter(geste) ". ";color:var(--rj-teinte);font-weight:900}
.regle-liste li{margin:8px 0;font-size:17px;font-weight:700}
.regle-liste li,.regle .pref{display:flex;gap:10px;align-items:flex-start;justify-content:space-between}
.regle .pref{font-size:16px}
.acte-ligne{display:flex;gap:8px;align-items:stretch}
.acte-ligne .opt{flex:1}
.ecoute-acte{align-self:center}
.ticket.cuisson{grid-template-columns:auto 1fr}
@media (max-width:640px){.ticket.cuisson{grid-template-columns:1fr;grid-template-areas:none}.ticket.cuisson .chg{grid-area:auto}}
.critere{font-weight:800;color:var(--warn-ink);display:flex;gap:10px;align-items:flex-start;justify-content:space-between}
.pourquoi{display:block;font-weight:700;color:var(--text-strong);margin-top:6px}
@media (max-width:640px){.ticket{grid-template-columns:1fr auto 1fr}.ticket img{max-height:90px}.choix.tickets{grid-template-columns:repeat(2,minmax(0,1fr))}.ticket{grid-template-columns:1fr 1fr;grid-template-areas:"p p" "c i"}.ticket img:first-child{grid-area:p}.ticket .chg{grid-area:c;justify-self:center;font-size:15px}.ticket img:last-child{grid-area:i}}

/* Le test (étape 3) */
.resultat{display:grid;gap:14px;margin-top:10px}
.bloc{background:var(--surface-card);border:1px solid var(--line-200);border-radius:14px;padding:16px}
.bloc.formateur{border-style:dashed}
.bloc h2{margin:0 0 8px;font-size:20px}
.gros-palier{font-size:34px;font-weight:900;color:var(--text-strong);margin:4px 0}
.parts div{display:grid;grid-template-columns:1fr auto;gap:10px;align-items:center;padding:6px 0;border-bottom:1px solid var(--line-200)}
.ok-txt{font-weight:800;color:var(--ok-ink,#1B5E20)}
.n{font-size:14px;color:var(--text-muted)}
.oral{display:flex;flex-direction:column;align-items:center;gap:10px;margin:14px 0}
.oral .etat{font-weight:700;min-height:1.4em}
.rec{background:#8A2E1C;border-color:#8A2E1C;color:#fff}.rec .appui{color:#fff}
.rec.en-cours{background:#B3261E;border-color:#B3261E}
.code-f{display:flex;gap:10px;align-items:center;flex-wrap:wrap}
.code-f input{font:inherit;font-size:20px;width:8ch;padding:8px 10px;border-radius:10px;border:1px solid var(--line-300)}
.oral-f{border-top:1px solid var(--line-200);padding-top:10px;margin-top:10px}
.choisir3{display:flex;flex-wrap:wrap;gap:8px;margin:4px 0 8px}
.choisir3 [aria-pressed=true]{background:var(--ok-bg,#E8F5E9);border-color:var(--ok-line,#2E7D32)}
#notesF{font:inherit;width:100%;box-sizing:border-box;border-radius:10px;border:1px solid var(--line-300);padding:8px}

/* Le service (étape 4) */
.porte-titre{font-size:20px;margin:18px 0 4px}
.appui-sous{display:block;font-size:14px;font-weight:600;color:var(--text-muted)}
.clients{display:grid;grid-template-columns:repeat(auto-fill,minmax(210px,1fr));gap:12px;margin-top:8px}
.client{font:inherit;cursor:pointer;text-align:start;border:1px solid var(--line-200);background:var(--surface-card);border-radius:14px;padding:10px;display:flex;flex-direction:column;gap:6px;color:var(--text-body)}
.client:hover{border-color:var(--rj-teinte)}
.client img{width:100%;aspect-ratio:3/2;object-fit:cover;background:#fff;border-radius:10px}
.client b{font-size:18px;color:var(--text-strong)}
.scene{display:grid;grid-template-columns:minmax(0,320px) minmax(0,1fr);gap:16px;margin-top:10px;align-items:start}
.avatar{background:#fff;border:1px solid var(--line-200);border-radius:16px;padding:8px;position:sticky;top:8px}
.avatar img{width:100%;aspect-ratio:3/2;object-fit:cover;display:block;border-radius:10px}
.avatar .nom{text-align:center;font-weight:900;margin:6px 0 0;font-size:18px}
.avatar .humeur{text-align:center;font-weight:700;margin:2px 0}
.carte-sit{font-size:14px;margin:6px 0 0}
.fil{display:flex;flex-direction:column;gap:8px;min-height:120px;margin-top:10px}
.fil.cache .bulle.client .txt{filter:blur(6px)}
.bulle{max-width:88%;padding:10px 12px;border-radius:14px;line-height:1.4}
.bulle .qui{display:block;font-size:12px;font-weight:800;color:var(--text-muted)}
.bulle.client{align-self:flex-start;background:var(--surface-card);border:1px solid var(--line-200)}
.bulle.vous{align-self:flex-end;background:var(--rj-fond)}
.attente{color:var(--text-muted)}
.saisie{display:flex;gap:8px;flex-wrap:wrap;margin-top:12px}
.saisie input{flex:1;min-width:160px;font:inherit;font-size:16px;padding:10px;border-radius:10px;border:1px solid var(--line-300)}
.gestes-liste{margin:6px 0 0;padding-left:18px}
.bilan-gestes{list-style:none;padding:0;margin:8px 0 0;display:grid;gap:8px}
.bilan-gestes li{display:flex;gap:10px}
.bilan-gestes small{display:block;color:var(--text-muted)}
.bilan-gestes .marque{font-weight:900;width:18px}
.bilan-gestes .fait .marque{color:var(--ok-ink,#1B5E20)} .bilan-gestes .manque .marque{color:var(--warn-ink)}
@media (max-width:640px){.scene{grid-template-columns:1fr}.avatar{position:static}.avatar img{max-height:160px}}

/* (audit de design, majeurs) Un bouton désactivé se voit ; le verdict d'une carte porte un signe, pas la couleur seule. */
.btn-rj:disabled,.btn-rj[disabled]{opacity:.45;cursor:not-allowed}
.opt:disabled:not(.juste):not(.faux){opacity:.55;cursor:not-allowed}
.opt.juste::after,.opt.faux::after{position:absolute;top:6px;inset-inline-end:6px;width:28px;height:28px;border-radius:50%;
  display:grid;place-items:center;font-weight:900;font-size:16px;color:#fff;line-height:1}
.opt.juste::after{content:"✓";background:var(--ok-ink,#1B5E20)}
.opt.faux::after{content:"✕";background:var(--no-ink,#9B1C1C)}
.jeu .ecoute{margin-bottom:12px}
.regle .pref{margin-top:8px}
.verrou{text-align:center;font-size:14px;color:var(--text-muted);margin:0}
/* (audit de design, majeur) Le service à 375 px : une ligne par situation, l'image du poste une fois. */
@media (max-width:640px){
  .clients{grid-template-columns:1fr;gap:8px}
  .client img{display:none}
  .client{padding:12px 14px}
  .porte-titre{margin-top:14px}
}
</style>
</head>
<body>
<div class="fr-barre"><div class="fr-barre__in">
  <span class="fr-lockup"><span class="fr-nom" role="img" aria-label="francis">franc<span class="fr-i" aria-hidden="true">ı<span class="fr-point"></span></span>s</span><span class="fr-trait" aria-hidden="true"></span><span class="fr-desc">Aide à l'apprentissage du français</span></span>
  <span class="secteur"><small>%%SURTITRE%%</small><b><span class="long">%%SECTEUR%%</span><span class="court">%%SECTEUR_COURT%%</span></b></span>
</div></div>
<main class="rj" id="app"></main>
<div class="fiche" id="fiche" hidden><div class="carte" role="dialog" aria-modal="true" aria-labelledby="ficheMot" id="carte"></div></div>
<script>
(function(){
const D = %%DONNEES%%;
const NOM = %%NOM_JS%%;
const CLE = 'francisation-langue';
const ICO = {
  son:'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M4 9v6h4l5 4V5L8 9H4z"/><path d="M16.5 8.5a5 5 0 0 1 0 7"/><path d="M19 6a8.5 8.5 0 0 1 0 12"/></svg>',
  oeil:'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M2 12s3.5-7 10-7 10 7 10 7-3.5 7-10 7S2 12 2 12z"/><circle cx="12" cy="12" r="3"/></svg>',
  x:'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" aria-hidden="true"><path d="M6 6l12 12M18 6L6 18"/></svg>',
  g:'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M15 18l-6-6 6-6"/></svg>',
  d:'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M9 18l6-6-6-6"/></svg>',
  niveau:'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M4 20V14M10 20V9M16 20V4M22 20H2"/></svg>',
  jeu:'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M9 11l3 3L22 4"/><path d="M21 12v7a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2V5a2 2 0 0 1 2-2h11"/></svg>'
};
const FR = %%FR%%;

const $ = s => document.querySelector(s);
const esc = s => String(s).replace(/[&<>"]/g, c => ({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;'}[c]));
const app = $('#app'), fiche = $('#fiche'), carte = $('#carte');
const parId = Object.fromEntries(D.mots.map(m => [m.id, m]));
let langue = null, liste = [], rang = 0, retourFocus = null, courante = null;
const audio = new Audio();

function lireLangue(){ try { return localStorage.getItem(CLE); } catch(e){ return null; } }
function poserLangue(c){ try { localStorage.setItem(CLE, c); } catch(e){} }
function L(){ return D.langues.find(l => l.c === langue) || null; }
// Une consigne : le français, puis l'appui DESSOUS (jamais à sa place).
// L'arabe, le persan et l'ourdou s'écrivent de droite à gauche : l'appui seul, le français reste à gauche.
const dirL = l => l && l.rtl ? ' dir="rtl"' : '';
function t(k){ const l = L(); const a = l && l.ui[k]; return esc(FR[k]) + (a ? '<span class="appui" lang="' + l.c + '"' + dirL(l) + '>' + esc(a) + '</span>' : ''); }
function tb(k){ const l = L(); const a = l && l.ui[k]; return '<span>' + esc(FR[k]) + '</span>' + (a ? '<span class="appui" lang="' + l.c + '"' + dirL(l) + '>' + esc(a) + '</span>' : ''); }
function jouer(src){ if (!src) return; try { audio.pause(); audio.src = src; audio.currentTime = 0; audio.play().catch(()=>{}); } catch(e){} }

function adresse(o){
  const u = new URL(location.href);
  ['planche','mot','ecran','ex'].forEach(k => u.searchParams.delete(k));
  Object.entries(o || {}).forEach(([k,v]) => v && u.searchParams.set(k, v));
  history.replaceState(null, '', u);
}
function tete(titreK, sousK, retour){
  const r = {planches: ['planches', 'retour'], exercices: ['exercices', 'retour_ex'], accueil: ['accueil', 'accueil'], service: ['service', 'service']}[retour];
  return '<div class="rj-tete"><div><p class="rj-enseigne">' + esc(NOM) + '</p><h1>' + t(titreK) + '</h1>'
    + (sousK ? '<p style="margin:6px 0 0">' + t(sousK) + '</p>' : '') + '</div><div style="display:flex;gap:8px;flex-wrap:wrap">'
    + (r ? '<button class="btn-rj btn-rj--pile" data-act="' + r[0] + '">' + tb(r[1]) + '</button>' : '')
    + '<button class="btn-rj btn-rj--pile" data-act="langue">' + tb('langue') + '</button></div></div>';
}

function ecranLangue(){
  arreter();
  adresse({});
  app.innerHTML = '<div class="rj-tete"><div><p class="rj-enseigne">' + esc(NOM) + '</p><h1>' + esc(FR.choisir) + '</h1>'
    + '<p style="margin:6px 0 0">' + esc(FR.choisir_sous) + '</p></div></div>'
    + '<button class="sans-trad" data-lang="fr">' + esc(FR.francais_seul) + '<small>' + esc(FR.francais_seul_sous) + '</small></button>'
    + '<div class="langues">' + D.langues.map(l => '<button data-lang="' + l.c + '" lang="' + l.c + '" dir="auto">' + esc(l.loc) + '</button>').join('') + '</div>';
  app.querySelector('button').focus();
}

function accueil(){
  arreter();
  adresse({});
  app.innerHTML = tete('accueil', null, null)
    + '<div class="accueil"><button class="porte" data-act="planches"><img src="' + D.poste + '" alt=""><b>' + t('apprendre') + '</b><span>' + t('apprendre_sous') + '</span></button>'
    + '<button class="porte" data-act="exercices"><span class="porte-ico">' + ICO.jeu + '</span><b>' + t('exercer') + '</b><span>' + t('exercer_sous') + '</span></button>'
    + '<button class="porte" data-act="test"><span class="porte-ico">' + ICO.niveau + '</span><b>' + t('test') + '</b><span>' + t('test_sous') + '</span></button>'
    + '<button class="porte" data-act="service"><img src="' + D.service.decor.salle + '" alt=""><b>' + t('service') + '</b><span>' + t('service_accueil') + '</span></button></div>';
}

function vignettes(p){
  const ms = D.mots.filter(m => m.p === p.k);
  const avec = ms.filter(m => m.img).slice(0, 6);
  let v = avec.map(m => '<img src="' + m.img + '" alt="" loading="lazy">').join('');
  // Une planche sans croquis (les repas, le quart) : des mots à entendre.
  for (let i = avec.length; i < 3; i++) v += '<i>' + ICO.son + '</i>';
  return '<span class="vign">' + v + '</span>';
}
function planches(){
  arreter();
  adresse({ecran: 'planches'});
  const posteN = D.zones.length;
  app.innerHTML = tete('planches', 'planches_sous', 'accueil')
    + '<div class="planches">'
    + '<button class="pl poste" data-planche="poste"><img class="large" src="' + D.poste + '" alt=""><span><span class="etiq">' + esc(FR.cuisine) + '</span><br><b>' + t('decor') + '</b><br><span class="n">' + posteN + ' ' + esc(FR.mots) + '</span></span></button>'
    + D.planches.map(p => {
        const n = D.mots.filter(m => m.p === p.k).length;
        return '<button class="pl" data-planche="' + p.k + '"><span class="etiq">' + esc(FR[p.poste]) + '</span>' + vignettes(p)
          + '<b>' + t('p_' + p.k) + '</b><span class="n">' + n + ' ' + esc(FR.mots) + '</span></button>';
      }).join('') + '</div>';
}

function illustration(m, grand){
  if (m.img) return '<img src="' + m.img + '" alt="">';
  if (m.zone) {
    const [x,y,w,h] = m.zone;
    return '<span class="mini' + (grand ? '' : ' dec') + '"><img src="' + D.poste + '" alt=""><i style="left:' + x + '%;top:' + y + '%;width:' + w + '%;height:' + h + '%"></i></span>';
  }
  return '<span class="sans">' + ICO.son + '</span>';
}
function planche(k){
  courante = k;
  adresse({planche: k});
  if (k === 'poste') return decor();
  const p = D.planches.find(x => x.k === k);
  if (!p) return planches();
  liste = D.mots.filter(m => m.p === k);
  app.innerHTML = tete('p_' + k, 'toucher', 'planches')
    + '<div class="planche">' + liste.map((m, i) =>
      '<button class="art' + (m.piege ? ' piege' : '') + '" data-i="' + i + '"><span class="num">' + (i + 1) + '</span>'
      + illustration(m, false) + '<span class="mot">' + esc(m.mot) + '</span></button>').join('') + '</div>';
}
function decor(){
  liste = D.zones.map(id => parId[id]);
  app.innerHTML = tete('decor', 'decor_sous', 'planches')
    + '<div class="decor"><img src="' + D.poste + '" alt="">' + liste.map((m, i) => {
      const [x,y,w,h] = m.zone;
      return '<button class="zone" data-i="' + i + '" aria-label="' + (i + 1) + ' — ' + esc(m.mot) + '" style="left:' + x + '%;top:' + y + '%;width:' + w + '%;height:' + h + '%"><span class="pastille">' + (i + 1) + '</span></button>';
    }).join('') + '</div>'
    // Sur téléphone, les zones se serrent : la liste numérotée les double.
    + '<ol class="zliste">' + liste.map((m, i) => '<li><button data-i="' + i + '"><span class="pastille">' + (i + 1) + '</span>' + esc(m.mot) + '</button></li>').join('') + '</ol>';
}

function ouvrir(i){
  rang = i;
  const m = liste[i];
  adresse({planche: courante, mot: m.id});
  const l = L(), tr = l && l.mots[m.id];
  const note = m.note ? m.note.replace(/^PIÈGE\s*:\s*/, '') : '';
  carte.innerHTML = '<button class="btn-rj ferme petit" data-act="fermer" aria-label="' + esc(FR.fermer) + '">' + ICO.x + '</button>'
    + '<div class="grand">' + illustration(m, true) + '</div>'
    + '<h2 id="ficheMot">' + esc(m.mot) + '</h2>'
    + (m.autre ? '<p class="autre">' + esc(FR.aussi) + ' : <b>' + esc(m.autre) + '</b>'
        + (m.autre_son ? ' <button class="btn-rj petit" data-act="autre" aria-label="' + esc(FR.ecouter) + ' : ' + esc(m.autre) + '">' + ICO.son + '</button>' : '') + '</p>' : '')
    + '<div class="gestes">' + (m.son ? '<button class="btn-rj btn-rj--pri btn-rj--pile" data-act="ecouter">' + tb('ecouter') + '</button>' : '')
    + (tr ? '<button class="btn-rj btn-rj--pile" data-act="voir" aria-expanded="false">' + tb('voir') + '</button>' : '') + '</div>'
    + (tr ? '<div class="trad" id="trad" hidden lang="' + l.c + '"' + dirL(l) + '>' + esc(tr[0]) + (tr[1] ? '<small>' + esc(tr[1]) + '</small>' : '')
        + (l.relu ? '' : '<span class="relu" dir="ltr" lang="fr">' + t('non_relu') + '</span>') + '</div>' : '')
    + (note ? (m.piege ? '<div class="piege">' + esc(FR.piege) + ' : ' + esc(note) + '</div>' : '<p class="note">' + esc(note) + '</p>') : '')
    + '<div class="nav"><button class="btn-rj petit" data-act="prec" ' + (i ? '' : 'disabled') + '>' + ICO.g + esc(FR.precedent) + '</button>'
    + '<button class="btn-rj petit" data-act="suiv" ' + (i < liste.length - 1 ? '' : 'disabled') + '>' + esc(FR.suivant) + ICO.d + '</button></div>';
  if (fiche.hidden) retourFocus = document.activeElement;
  fiche.hidden = false;
  carte.querySelector('[data-act=ecouter]') ? carte.querySelector('[data-act=ecouter]').focus() : carte.querySelector('[data-act=fermer]').focus();
  jouer(m.son);
}
function fermer(){
  fiche.hidden = true; audio.pause();
  adresse({planche: courante});
  if (retourFocus && document.contains(retourFocus)) retourFocus.focus();
}

/* ═══ Étape 5 : le rapport au direct de la classe (le pilote) ══════════
   Ouverte en séance (ou depuis le portail), la page connaît un code et
   l'activité : elle rapporte chaque réponse FERMÉE au premier essai, et chaque
   situation jouée avec ses gestes. Jamais les phrases dites, ni l'oral, ni le
   test, ni la langue d'appui. `essais` compte les erreurs AVANT la réponse
   (0 = du premier coup) : la page n'envoie que le premier essai, donc 0, et
   « encore faux » au direct se lit « raté au premier essai » (leçon de la
   répétition du pilote de l'hôtel). L'énoncé est lisible : le mot ou la phrase,
   puis le code de l'item. */
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
function rapporter(o){
  if (!CTX) return;
  fetch('/api/student/progress', {method: 'POST', headers: {'Content-Type': 'application/json'},
    body: JSON.stringify(Object.assign({code: CTX.code, activityId: CTX.activityId,
      activityTitle: 'Chez Jocelyne', event: 'zone_repondue', bonne: '', reponse: '', essais: 0}, o))}).catch(() => {});
}
const libelle = (txt, id) => { const s = String(txt || ''); return (s.length > 120 ? s.slice(0, 117) + '…' : s) + (s ? ' (' + id + ')' : String(id)); };
const TITRES_EX = {ecoute: "Je l'entends, je le trouve", image: 'Le mot et son image', pieges: 'Les pièges',
  chef: 'La consigne du chef', commande: 'La commande modifiée', allergie: "L'allergie"};
function rapporterItem(it, ok, extra){
  if (!S || !it.zid || !TITRES_EX[S.k]) return;
  rapporter(Object.assign({zone: 'rj-' + S.k + '-' + it.zid, exo: 'rj-' + S.k, exoNum: TITRES_EX[S.k], exoTitre: TITRES_EX[S.k],
    section: 'exercices', type: S.k, enonce: libelle(it.lib, it.zid), ok}, extra || {}));
}

/* ═══ Étape 2 : les exercices ══════════════════════════════════════════
   Huit exercices, chacun rattaché à un objectif du cadrage. Séries de 8 ;
   deux essais puis la réponse (l'allergie : un seul, c'est un geste) ; la
   bonne réponse TOURNE de place d'un item à l'autre ; la phrase entendue ne
   s'écrit qu'APRÈS la réponse. */
const EXOS = [
  {k: 'ecoute', filtre: true}, {k: 'image', filtre: true}, {k: 'rappel', filtre: true}, {k: 'pieges'},
  {k: 'chef', bruit: true, pont: true}, {k: 'commande', pont: true}, {k: 'allergie', bruit: true, pont: true}, {k: 'redis', bruit: true}];
const N = 8;
const REVOIR = 'resto-a-revoir', BRUIT = 'resto-bruit';
let S = null;   // la série en cours

function lire(k, d){ try { const v = localStorage.getItem(k); return v == null ? d : JSON.parse(v); } catch(e){ return d; } }
function ecrire(k, v){ try { localStorage.setItem(k, JSON.stringify(v)); } catch(e){} }
function aRevoir(id, oui){
  const r = new Set(lire(REVOIR, []));
  oui ? r.add(id) : r.delete(id);
  ecrire(REVOIR, [...r]);
}
const melange = a => { a = a.slice(); for (let i = a.length - 1; i > 0; i--) { const j = Math.floor(Math.random() * (i + 1)); [a[i], a[j]] = [a[j], a[i]]; } return a; };
// Les places de la bonne réponse : des blocs mélangés de 0..n-1, jamais deux
// fois la même de suite (la bonne toujours au même endroit trahit l'exercice).
function places(nItems, n){
  const out = [];
  while (out.length < nItems) {
    let b = melange([...Array(n).keys()]);
    if (out.length && b[0] === out[out.length - 1]) b.push(b.shift());
    out.push(...b);
  }
  return out.slice(0, nItems);
}
function poser(bonne, autres, place){ const o = autres.slice(); o.splice(place, 0, bonne); return o; }

/* Le bruit de cuisine, fabriqué dans le navigateur (décision du plan : réglable,
   on peut le couper). La hotte (bruit brun filtré), la friture (bruit blanc
   haut, qui ondule), et un choc de métal de temps en temps. */
const Bruit = {
  ctx: null, noeuds: [], minuteur: null, niveau: lire(BRUIT, 1),
  demarrer(){
    this.arreter();
    if (!this.niveau) return;
    try { this.ctx = this.ctx || new (window.AudioContext || window.webkitAudioContext)(); } catch(e){ return; }
    const c = this.ctx; if (c.state === 'suspended') c.resume();
    const g = c.createGain(); g.gain.value = this.niveau === 2 ? 0.22 : 0.08; g.connect(c.destination);
    const tampon = (brun) => {
      const b = c.createBuffer(1, c.sampleRate * 2, c.sampleRate), d = b.getChannelData(0); let l = 0;
      for (let i = 0; i < d.length; i++) { const w = Math.random() * 2 - 1; if (brun) { l = (l + 0.02 * w) / 1.02; d[i] = l * 3.5; } else d[i] = w; }
      const s = c.createBufferSource(); s.buffer = b; s.loop = true; return s;
    };
    const hotte = tampon(true), bp = c.createBiquadFilter(); bp.type = 'lowpass'; bp.frequency.value = 500;
    hotte.connect(bp).connect(g); hotte.start();
    const frit = tampon(false), hp = c.createBiquadFilter(); hp.type = 'highpass'; hp.frequency.value = 3500;
    const fg = c.createGain(); fg.gain.value = 0.25; const lfo = c.createOscillator(), lg = c.createGain();
    lfo.frequency.value = 0.7; lg.gain.value = 0.15; lfo.connect(lg).connect(fg.gain); lfo.start();
    frit.connect(hp).connect(fg).connect(g); frit.start();
    this.noeuds = [hotte, frit, lfo, g];
    const choc = () => {
      if (!this.ctx) return;
      const t0 = c.currentTime;
      [1830, 2710, 4190].forEach((f, n) => {
        const o = c.createOscillator(), e = c.createGain(); o.frequency.value = f * (0.9 + Math.random() * 0.2);
        e.gain.setValueAtTime(0.35 / (n + 1), t0); e.gain.exponentialRampToValueAtTime(0.001, t0 + 0.35);
        o.connect(e).connect(g); o.start(t0); o.stop(t0 + 0.4);
      });
      this.minuteur = setTimeout(choc, 1500 + Math.random() * 3000);
    };
    this.minuteur = setTimeout(choc, 800);
  },
  arreter(){
    clearTimeout(this.minuteur);
    this.noeuds.forEach(n => { try { n.stop ? n.stop() : n.disconnect(); } catch(e){} });
    this.noeuds = [];
  },
  regler(n){ this.niveau = n; ecrire(BRUIT, n); this.demarrer(); }
};
function arreter(){ Bruit.arreter(); try { audio.pause(); } catch(e){} S = null; }
function jouerLent(src){ jouer(src); try { audio.playbackRate = 0.75; audio.preservesPitch = true; } catch(e){} }
function jouerNormal(src){ jouer(src); try { audio.playbackRate = 1; } catch(e){} }

function exercices(){
  arreter();
  adresse({ecran: 'exercices'});
  app.innerHTML = tete('exercices', null, 'accueil') + nonRelu() + '<div class="exos">' + EXOS.map((x, i) =>
    '<button class="exo-porte' + (x.pont ? ' pont' : '') + '" data-ex="' + x.k + '"><span class="rang">' + (i + 1) + '</span><span><b>' + t('ex_' + x.k) + '</b>'
    + '<span class="sous">' + t('ex_' + x.k + '_c') + '</span>' + (FR['seuil_' + x.k] ? '<span class="seuil-porte">' + t('seuil_' + x.k) + '</span>' : '') + '</span></button>').join('') + '</div>';
}

// ── La construction des séries ──
function avecImage(filtre){
  let ms = D.mots.filter(m => m.img && m.son);
  if (filtre === 'revoir') { const r = new Set(lire(REVOIR, [])); ms = ms.filter(m => r.has(m.id)); }
  else if (filtre && filtre !== 'tous') ms = ms.filter(m => m.p === filtre);
  return ms;
}
function voisins(m, n, cle){
  // D'abord la même planche, puis le même poste ; jamais le même mot écrit.
  const pl = D.planches.find(p => p.k === m.p);
  const pris = new Set([m[cle] || m.mot]);
  const out = [];
  const tirer = arr => melange(arr).forEach(x => { if (out.length < n && !pris.has(x.mot) && x.id !== m.id) { pris.add(x.mot); out.push(x); } });
  tirer(D.mots.filter(x => x.img && x.p === m.p));
  tirer(D.mots.filter(x => x.img && (D.planches.find(p => p.k === x.p) || {}).poste === pl.poste));
  tirer(D.mots.filter(x => x.img));
  return out;
}
const imgChoix = m => ({html: '<img src="' + m.img + '" alt="">', cle: m.id});
function construire(k, filtre){
  const E = D.ex;
  if (k === 'ecoute' || k === 'image' || k === 'rappel') {
    const pool = melange(avecImage(filtre)).slice(0, N);
    const pl = places(pool.length, 4);
    return pool.map((m, i) => {
      const v = voisins(m, 3);
      if (k === 'ecoute') return {zid: m.id, lib: m.mot, son: m.son, revoir: m.id, choix: poser(imgChoix(m), v.map(imgChoix), pl[i]), bonne: pl[i], apres: m.mot, type: 'img'};
      if (k === 'image') return {zid: m.id, lib: m.mot, sujet: m.img, son: null, revoir: m.id, choix: poser({html: esc(m.mot)}, v.map(x => ({html: esc(x.mot)})), pl[i]), bonne: pl[i], apres: m.mot, apresSon: m.son, type: 'mot'};
      return {sujet: m.img, rappel: m, revoir: m.id, type: 'rappel'};
    });
  }
  if (k === 'pieges') {
    // Six pièges et deux mots ordinaires, entrelacés : une série faite QUE de
    // pièges apprendrait à tout soupçonner.
    const p = melange(E.pieges).slice(0, 6).map(x => ({id: x.id, o: x.o.slice(1)}));
    const o = melange(E.ordinaires).slice(0, 2).map(id => ({id, o: voisins(parId[id], 3).map(x => x.id)}));
    const pool = [...p.slice(0, 3), o[0], ...p.slice(3), o[1]];
    const pl = places(pool.length, 4);
    return pool.map((x, i) => { const m = parId[x.id]; return {zid: m.id, lib: m.mot, son: m.son, revoir: m.id, choix: poser(imgChoix(m), x.o.map(id => imgChoix(parId[id])), pl[i]), bonne: pl[i], apres: m.mot, note: m.piege ? m.note.replace(/^PIÈGE\s*:\s*/, '') : '', type: 'img'}; });
  }
  if (k === 'chef') {
    const pool = melange(E.consignes).slice(0, N), pl = places(pool.length, 4);
    // (audit, tour 1, A3/D2) Les trois derniers : une seule écoute, sans « Plus
    // lentement » — la condition de l'objectif. Après la réponse, on entend ce
    // qu'on répond au chef.
    return pool.map((c, i) => ({zid: c.id, lib: c.phrase, son: c.son, q: c.q, choix: poser(imgChoix(parId[c.o[0]]), c.o.slice(1).map(id => imgChoix(parId[id])), pl[i]), bonne: pl[i], apres: c.phrase, type: 'img',
      unique: i >= pool.length - 3, modele: c.redit_son, redit: c.redit}));
  }
  if (k === 'commande') {
    const pool = melange(E.commandes).slice(0, N);
    const pl = places(pool.length, 4), pl3 = places(pool.length, 3);
    const carteHTML = ([p, ch, g]) => p === g || !parId[p].img
      ? '<span class="ticket cuisson"><span class="chg">' + esc(E.changements[ch]) + '</span><img src="' + parId[g].img + '" alt=""></span>'
      : '<span class="ticket"><img src="' + parId[p].img + '" alt="' + esc(parId[p].mot) + '"><span class="chg">' + esc(E.changements[ch]) + '</span><img src="' + parId[g].img + '" alt="' + esc(parId[g].mot) + '"></span>';
    return pool.map((c, i) => {
      const autres = melange(c.cartes.slice(1));
      const place = c.cartes.length === 4 ? pl[i] : pl3[i];
      return {zid: c.id, lib: c.phrase, son: c.son, choix: poser({html: carteHTML(c.cartes[0])}, autres.map(x => ({html: carteHTML(x)})), place), bonne: place, apres: c.phrase, type: 'ticket'};
    });
  }
  if (k === 'allergie') {
    // Au moins un contre-exemple par série (un « je n'aime pas »), pas plus de deux.
    const contre = melange(E.allergies.filter(a => a.contre)), vrai = melange(E.allergies.filter(a => !a.contre));
    const pool = melange([...contre.slice(0, 1 + (Math.random() < .5 ? 1 : 0)), ...vrai]).slice(0, N);
    if (!pool.some(a => a.contre)) pool[Math.floor(Math.random() * pool.length)] = contre[0];
    const pl = places(pool.length, 3);
    return pool.map((a, i) => {
      const bonne = a.actes.find(x => x.s === 'juste'), autres = melange(a.actes.filter(x => x.s !== 'juste'));
      const ch = poser(bonne, autres, pl[i]);
      return {zid: a.id, lib: a.phrase, son: a.son, qui: a.qui, choix: ch.map(x => ({html: t(x.k), s: x.s, p: x.p, son: x.son})), bonne: pl[i], apres: a.phrase, type: 'acte', contre: a.contre};
    });
  }
  if (k === 'redis') {
    const pool = melange([...melange(E.consignes).slice(0, 5), ...melange(E.commandes).slice(0, 3)]);
    return pool.map(c => ({son: c.son, modele: c.redit_son, redit: c.redit, phrase: c.phrase, type: 'redis', qui: c.q ? 'qui_chef' : 'qui_client'}));
  }
  return [];
}

// ── Le déroulé ──
function lancer(k, filtre){
  const x = EXOS.find(e => e.k === k); if (!x) return exercices();
  arreter();
  adresse({ecran: 'exercices', ex: k});
  if (k === 'allergie' && !filtre) return regle();
  if (k === 'redis' && !filtre) return formules();
  const f = x.filtre ? (filtre && filtre !== 'x' ? filtre : 'tous') : null;
  const items = construire(k, f);
  S = {k, x, filtre: f, items, n: 0, premier: 0, graves: 0};
  if (x.bruit) Bruit.demarrer();
  item();
}
function regleHTML(){
  return '<ol class="regle-liste">' + [1, 2, 3].map(n => '<li><span>' + t('regle_' + n) + '</span><button class="btn-rj petit" data-regle="' + (n - 1) + '" aria-label="' + esc(FR.ecouter) + '">' + ICO.son + '</button></li>').join('') + '</ol>'
    + '<p class="pref"><span>' + t('regle_pref') + '</span><button class="btn-rj petit" data-regle="3" aria-label="' + esc(FR.ecouter) + '">' + ICO.son + '</button></p>'
    + '<p class="pref"><span>' + t('regle_cuisine') + '</span><button class="btn-rj petit" data-regle="4" aria-label="' + esc(FR.ecouter) + '">' + ICO.son + '</button></p>'
    + '<p class="critere"><span>' + t('critere_grave') + '</span><button class="btn-rj petit" data-regle="5" aria-label="' + esc(FR.ecouter) + '">' + ICO.son + '</button></p>';
}
function nonRelu(){ const l = L(); return l && !l.relu ? '<p class="non-relu">' + t('non_relu') + '</p>' : ''; }
function regle(){
  app.innerHTML = tete('ex_allergie', null, 'exercices')
    + '<div class="regle"><h2>' + t('regle_titre') + '</h2>' + regleHTML() + '<p class="grave-sous">' + t('grave_sous') + '</p>'
    + '<button class="btn-rj btn-rj--pri btn-rj--pile" data-act="commencer">' + tb('compris') + '</button>' + nonRelu() + '</div>';
}
function formules(){
  // (audit, tour 1, C4) Les deux phrases à dire, avec un exemple entendu, AVANT la série.
  app.innerHTML = tete('ex_redis', null, 'exercices')
    + '<div class="regle"><h2>' + t('formules_titre') + '</h2><ol class="regle-liste">' + D.ex.formules.map((f, n) =>
      '<li><span>' + t('formule_' + f.k) + '</span><button class="btn-rj petit" data-formule="' + n + '" aria-label="' + esc(FR.ecouter) + '">' + ICO.son + '</button></li>').join('') + '</ol>'
    + '<button class="btn-rj btn-rj--pri btn-rj--pile" data-act="commencer">' + tb('compris') + '</button></div>';
}
function barreBruit(){
  if (!S.x.bruit) return '';
  return '<div class="bruit" role="group" aria-label="' + esc(FR.bruit) + '"><span>' + t('bruit') + '</span>'
    + [0, 1, 2].map(n => '<button class="btn-rj petit" data-bruit="' + n + '" aria-pressed="' + (Bruit.niveau === n) + '">' + esc(FR['bruit_' + n]) + '</button>').join('') + '</div>';
}
function filtreHTML(){
  if (!S.x.filtre) return '';
  const r = lire(REVOIR, []).length;
  return '<div class="filtre"><label for="filtre">' + esc(FR.filtre) + '</label><select id="filtre">'
    + '<option value="tous">' + esc(FR.tous) + '</option>'
    + (r ? '<option value="revoir">' + esc(FR.a_revoir_filtre) + ' (' + r + ')</option>' : '')
    + D.planches.filter(p => D.mots.some(m => m.p === p.k && m.img)).map(p => { const l = L(), a = l && l.ui['p_' + p.k];
        return '<option value="' + p.k + '">' + esc(p.t) + (a ? ' — ' + esc(a) : '') + '</option>'; }).join('')
    + '</select></div>';
}
function item(){
  const it = S.items[S.n];
  if (!it) return bilan();
  S.essais = 0; S.fini = false;
  const k = S.k;
  let h = tete('ex_' + k, 'ex_' + k + '_c', 'exercices') + filtreHTML() + barreBruit()
    + '<div class="jeu"><div class="barre"><i style="width:' + (100 * S.n / S.items.length) + '%"></i></div>';
  if (it.qui) h += '<p class="qui">' + t(it.qui) + '</p>';
  if (it.sujet) h += '<div class="sujet"><img src="' + it.sujet + '" alt=""></div>';
  if (it.son && it.unique) h += '<p class="unique">' + t('une_ecoute') + '</p>';
  else if (it.son) h += '<div class="ecoute"><button class="btn-rj btn-rj--pri btn-rj--pile" data-act="reecouter">' + tb('reecouter') + '</button>'
    + '<button class="btn-rj btn-rj--pile" data-act="lent">' + tb('lentement') + '</button></div>';
  if (it.q) h += '<p class="question">' + t(it.q) + '</p>';
  if (it.type === 'rappel') h += '<div class="revele" id="revele"><button class="btn-rj btn-rj--pri btn-rj--pile" data-act="voirmot">' + tb('voir_mot') + '</button></div>';
  else if (it.type === 'redis') h += '<p class="question">' + t('a_vous') + '</p><div class="revele" id="revele"><button class="btn-rj btn-rj--pile" data-act="modele">' + tb('modele') + '</button></div>';
  else if (it.type === 'acte') h += '<div class="choix mots actes">' + it.choix.map((c, i) =>
      '<div class="acte-ligne"><button class="opt" data-o="' + i + '">' + c.html + '</button><button class="btn-rj petit ecoute-acte" data-acte="' + i + '" aria-label="' + esc(FR.ecouter_acte) + '">' + ICO.son + '</button></div>').join('') + '</div>';
  else h += '<div class="choix ' + {img: 'imgs', mot: 'mots', ticket: 'tickets'}[it.type] + '">' + it.choix.map((c, i) =>
      '<button class="opt" data-o="' + i + '" aria-label="' + esc(FR.choix_n || 'Choix') + ' ' + (i + 1) + '">' + c.html + '</button>').join('') + '</div>';
  h += '<p class="retro" id="retro" aria-live="polite"></p><div class="apres" id="apres"></div><div class="suite" id="suite"></div></div>';
  app.innerHTML = h;
  const f = document.getElementById('filtre'); if (f) f.value = S.filtre;
  if (it.son) jouerNormal(it.son);
  const premier = app.querySelector('.opt, [data-act=voirmot], [data-act=reecouter]'); if (premier) premier.focus({preventScroll: true});
  if (it.unique) {
    // Les choix s'ouvrent à la fin du son — ou s'il ne part pas (lecture
    // refusée, fichier en erreur) : jamais de choix grisés sans issue (G1).
    const ouvrir = () => { audio.onended = audio.onerror = null; clearTimeout(S.secours);
      app.querySelectorAll('.opt').forEach(o => o.disabled = false); const o = app.querySelector('.opt'); if (o) o.focus({preventScroll: true}); };
    app.querySelectorAll('.opt').forEach(o => o.disabled = true);
    audio.onended = audio.onerror = ouvrir;
    S.secours = setTimeout(ouvrir, 12000);
  }
}
function montrerApres(it){
  // La phrase entendue s'écrit APRÈS la réponse : on apprend à écouter, pas à lire.
  const a = document.getElementById('apres');
  let h = '';
  if (it.apres) h += '<p class="dit"><span>' + (it.type === 'img' || it.type === 'mot' ? '' : esc(FR.phrase) + ' : ') + '</span><b>« ' + esc(it.apres) + ' »</b>'
    + (it.apresSon ? ' <button class="btn-rj petit" data-act="apresson" aria-label="' + esc(FR.ecouter) + '">' + ICO.son + '</button>' : '') + '</p>';
  if (it.note) h += '<div class="piege">' + esc(FR.piege) + ' : ' + esc(it.note) + '</div>';
  if (it.type === 'img' && it.redit) h += '<p class="dit">' + esc(FR.on_repond) + ' <b>« ' + esc(it.redit) + ' »</b> <button class="btn-rj petit" data-act="remodele" aria-label="' + esc(FR.ecouter) + '">' + ICO.son + '</button></p>';
  a.innerHTML = h;
  // (audit, tour 2, C3) le retour et son « pourquoi » viennent à l'écran.
  document.getElementById('suite').innerHTML = '<button class="btn-rj btn-rj--pri" data-act="suivant">' + esc(FR.suivant) + ICO.d + '</button>';
  document.querySelector('[data-act=suivant]').focus({preventScroll: true});
  // (audit, tour 3, C3) le retour et son « pourquoi » à l'écran — après le focus,
  // sans animation : l'animation se faisait interrompre.
  // (audit, tour 4) on défile jusqu'à la BONNE réponse, retour dessous — pas
  // au retour seul, qui poussait la réponse verte hors de l'écran.
  const r = app.querySelector('.opt.juste') || document.getElementById('retro');
  if (r && document.getElementById('retro').getBoundingClientRect().bottom > innerHeight) r.scrollIntoView({block: 'start', behavior: 'auto'});
}
function repondre(i){
  const it = S.items[S.n]; if (S.fini) return;
  const opts = [...app.querySelectorAll('.opt')], b = opts[i], retro = document.getElementById('retro');
  if (it.type === 'acte') {
    // Un geste, un seul essai : la conséquence vient APRÈS le choix.
    S.fini = true;
    opts.forEach(o => o.disabled = true);
    opts[it.bonne].classList.add('juste');
    const c = it.choix[i], s = c.s;
    rapporterItem(it, s === 'juste', s === 'grave' ? {enonce: libelle(it.lib, it.zid) + ' — erreur grave'} : null);
    // (audit, tour 1, E1) POURQUOI ce choix, puis la règle — et pour une simple
    // préférence, seulement la phrase sur la préférence.
    const pourquoi = c.p ? '<span class="pourquoi">' + t(c.p) + '</span>' : '';
    // En cuisine, « je l'écris sur la commande » ne s'applique pas : son propre rappel.
    const cuisine = it.qui !== 'qui_client';
    const rappel = '<span class="rappel-regle">' + (it.contre ? t('regle_pref')
      : cuisine ? t('regle_cuisine') + '<br>' + t('regle_3') : [1, 2, 3].map(n => t('regle_' + n)).join('<br>')) + '</span>'
      + (s === 'grave' ? '<span class="rappel-regle">' + t('critere_grave') + '</span>' : '');
    if (s === 'juste') {
      S.premier++; retro.className = 'retro ok';
      const pj = it.choix[it.bonne].p; retro.innerHTML = t('juste_acte') + (pj ? '<span class="pourquoi">' + t(pj) + '</span>' : '');
    } else {
      b.classList.add('faux');
      if (s === 'grave') S.graves++;
      retro.className = 'retro non'; retro.innerHTML = t(s === 'grave' ? 'grave' : 'faux_acte') + pourquoi + rappel;
    }
    return montrerApres(it);
  }
  if (S.essais === 0) rapporterItem(it, i === it.bonne);
  if (i === it.bonne) {
    S.fini = true; b.classList.add('juste'); opts.forEach(o => o.disabled = true);
    if (S.essais === 0) { S.premier++; if (it.revoir) aRevoir(it.revoir, false); }
    retro.className = 'retro ok'; retro.innerHTML = t('bravo');
    return montrerApres(it);
  }
  S.essais++; b.classList.add('faux'); b.disabled = true;
  const reste = opts.find(o => !o.disabled); if (reste && S.essais < 2) reste.focus({preventScroll: true});
  if (S.essais >= 2) {
    S.fini = true; opts.forEach(o => o.disabled = true); opts[it.bonne].classList.add('juste');
    if (it.revoir) aRevoir(it.revoir, true);
    retro.className = 'retro non'; retro.innerHTML = t('reponse');
    return montrerApres(it);
  }
  retro.className = 'retro non'; retro.innerHTML = t('essaie');
}
function autoEval(bien){
  const it = S.items[S.n];
  if (bien) S.premier++;
  if (it.revoir) aRevoir(it.revoir, !bien);
  S.n++; item();
}
function bilan(){
  const k = S.k, tot = S.items.length;
  app.innerHTML = tete('ex_' + k, null, 'exercices') + '<div class="bilan"><p class="fin">' + t('fin') + '</p>'
    + '<p class="score">' + S.premier + ' / ' + tot + '</p><p>' + t(k === 'rappel' || k === 'redis' ? 'auto_bilan' : 'premier_coup') + '</p>'
    + (k === 'allergie' ? '<p class="graves' + (S.graves ? ' non' : '') + '">' + S.graves + ' ' + esc(FR.graves) + '</p><p class="grave-sous">' + t('grave_sous') + '</p>'
       : FR['seuil_' + k] ? '<p class="seuil">' + t('seuil_' + k) + '</p>' : '')
    + '<div class="gestes-bilan"><button class="btn-rj btn-rj--pri btn-rj--pile" data-act="encore">' + tb('recommencer') + '</button>'
    + '<button class="btn-rj btn-rj--pile" data-act="exercices">' + tb('retour_ex') + '</button></div></div>';
  Bruit.arreter();
  S.fini = true;
}

/* ═══ Étape 3 : le test de positionnement ══════════════════════════════
   Quatre parties (test.py). AUCUNE rétroaction. Deux formes, la première au
   hasard, l'autre à la passation suivante. Le résultat vit sur l'appareil ;
   l'oral dans IndexedDB, gardé jusqu'à ce que le formateur confirme. Un
   résultat non confirmé se rouvre au rechargement. */
const TK = 'resto-test', TF = 'resto-test-forme', TH = 'resto-test-historique';
let T = null;
const TD = D.test;
const F = () => TD.formes[T.forme];
const idb = {
  ouvrir(){ return new Promise((ok, ko) => { try { const r = indexedDB.open('resto-test', 1);
    r.onupgradeneeded = () => r.result.createObjectStore('oral'); r.onsuccess = () => ok(r.result); r.onerror = () => ko(r.error); } catch(e){ ko(e); } }); },
  async mettre(k, v){ try { const db = await this.ouvrir(); await new Promise(ok => { const t = db.transaction('oral', 'readwrite'); t.objectStore('oral').put(v, k); t.oncomplete = ok; t.onerror = ok; }); } catch(e){} },
  async prendre(k){ try { const db = await this.ouvrir(); return await new Promise(ok => { const r = db.transaction('oral').objectStore('oral').get(k); r.onsuccess = () => ok(r.result); r.onerror = () => ok(null); }); } catch(e){ return null; } },
  async vider(){ try { const db = await this.ouvrir(); db.transaction('oral', 'readwrite').objectStore('oral').clear(); } catch(e){} }
};
// Ni l'espace formateur ouvert ni la minuterie ne se gardent : au rechargement, le code se redemande.
function tGarder(){ ecrire(TK, Object.assign({}, T, {_ouvert: undefined, _s: undefined})); }
function enTete(k, n, total){
  // Une sortie, toujours : la passation reprend au début de la partie en cours.
  return '<div class="rj-tete"><div><p class="rj-enseigne">' + esc(NOM) + ' · ' + esc(FR.test) + '</p><h1>' + t(k) + '</h1></div>'
    + '<div><button class="btn-rj btn-rj--pile" data-act="accueil">' + tb('accueil') + '</button></div></div>'
    + (total ? '<div class="jeu"><div class="barre"><i style="width:' + (100 * n / total) + '%"></i></div></div>' : '');
}
function test(){
  arreter();
  adresse({ecran: 'test'});
  const r = lire(TK, null);
  if (r && r.termine) { T = r; return resultats(); }
  // Une passation interrompue reprend au début de sa partie, même forme.
  if (r && r.partie) { T = r; return introPartie(r.partie); }
  app.innerHTML = tete('test', 'test_sous', 'accueil')
    + '<div class="regle"><p>' + t('t_intro1') + '</p><p>' + t('t_intro2') + '</p>'
    + '<button class="btn-rj btn-rj--pri btn-rj--pile" data-t="demarrer">' + tb('commencer') + '</button>'
    + '<p class="n" style="margin-top:14px">' + t('t_cadrage') + '</p></div>';
}
function demarrer(){
  const avant = lire(TF, null);
  const forme = avant ? (avant === 1 ? 2 : 1) : (Math.random() < .5 ? 1 : 2);
  ecrire(TF, forme);
  T = {forme, quand: Date.now(), joue: {}, A: {cran: 1, i: 0, bonnes: 0, erreurs: 0, niveau: 0}, B: [], C: [], D: {}, bi: 0, ci: 0, di: 0,
       termine: false, confirme: false, oral: {}, notes: '', palier: null};
  tGarder();
  introPartie('A');
}
function introPartie(p){
  T.partie = p; tGarder(); Bruit.arreter();
  app.innerHTML = enTete('part' + p) + '<div class="regle"><p>' + t('part' + p + '_c') + '</p>'
    + (p === 'C' ? regleHTML() : '')
    + '<button class="btn-rj btn-rj--pri btn-rj--pile" data-t="partie">' + tb('continuer') + '</button></div>';
}
function lancerPartie(){ ({A: aItem, B: bItem, C: cItem, D: dItem})[T.partie](); }
function choixImages(ids){ return '<div class="choix imgs">' + ids.map((id, i) => '<button class="opt" data-r="' + i + '" aria-label="' + esc(FR.choix_n || 'Choix') + ' ' + (i + 1) + '"><img src="' + parId[id].img + '" alt=""></button>').join('') + '</div>'; }

// A · adaptative : trois bonnes montent d'un cran, deux erreurs arrêtent.
function aItem(){
  const a = T.A, it = F().A[a.cran][a.i];
  app.innerHTML = enTete('partA', a.cran - 1 + a.i / 4, 3) + '<p class="question">' + t('partA_c') + '</p>'
    + '<div class="ecoute"><button class="btn-rj btn-rj--pri btn-rj--pile" data-t="son">' + tb('reecouter') + '</button></div>' + choixImages(it.o);
  jouerNormal(it.son);
}
function aRepondre(i){
  const a = T.A, it = F().A[a.cran][a.i];
  i === it.bonne ? a.bonnes++ : a.erreurs++;
  a.i++;
  if (a.bonnes >= TD.regles.valide) { a.niveau = a.cran; a.cran++; a.i = a.bonnes = a.erreurs = 0; if (a.cran > 3) return finA(); }
  else if (a.erreurs >= TD.regles.arret) return finA();
  tGarder(); aItem();
}
function finA(){ tGarder(); introPartie('B'); }

// B · une seule écoute, passée en entier.
function bItem(){
  const it = F().B[T.bi];
  if (!it) return introPartie('C');
  if (it.type === 'chef') { Bruit.niveau = 1; Bruit.demarrer(); } else Bruit.arreter();
  const choix = it.type === 'chef' ? choixImages(it.o)
    : '<div class="choix tickets">' + it.cartes.map((c, i) => '<button class="opt" data-r="' + i + '" aria-label="' + esc(FR.choix_n || 'Choix') + ' ' + (i + 1) + '">' + ticketHTML(c) + '</button>').join('') + '</div>';
  app.innerHTML = enTete('partB', T.bi, F().B.length)
    + '<p class="qui">' + t(it.type === 'chef' ? 'qui_chef' : 'qui_client') + '</p>'
    + '<div class="ecoute"><button class="btn-rj btn-rj--pri btn-rj--pile" data-t="une">' + tb('jouer_une') + '</button></div>'
    + (it.q ? '<p class="question">' + t(it.q) + '</p>' : '') + choix;
  // (audit, tour 1, D2) Déjà joué avant un rechargement : pas de seconde écoute.
  if ((T.joue || {})[it.id]) { const b = app.querySelector('[data-t=une]'); b.disabled = true; b.innerHTML = tb('deja_joue'); return; }
  app.querySelectorAll('.opt').forEach(o => o.disabled = true);
}
function bJouer(b){
  const it = F().B[T.bi];
  b.disabled = true; b.innerHTML = tb('deja_joue');
  audio.onplaying = () => { audio.onplaying = null; T.joue = T.joue || {}; T.joue[it.id] = true; tGarder(); };
  // Les choix s'ouvrent à la fin du son, ou s'il ne part pas (issue de secours).
  const ouvrir = () => { audio.onended = audio.onerror = null; clearTimeout(T._s);
    app.querySelectorAll('.opt').forEach(o => o.disabled = false); const o = app.querySelector('.opt'); if (o) o.focus({preventScroll: true}); };
  audio.onended = audio.onerror = ouvrir; T._s = setTimeout(ouvrir, 12000);
  jouerNormal(it.son);
}
function bRepondre(i){ const it = F().B[T.bi]; T.B.push(i === it.bonne); T.bi++; tGarder(); bItem(); }
const ticketHTML = ([p, ch, g]) => p === g || !parId[p].img
  ? '<span class="ticket cuisson"><span class="chg">' + esc(D.ex.changements[ch]) + '</span><img src="' + parId[g].img + '" alt=""></span>'
  : '<span class="ticket"><img src="' + parId[p].img + '" alt=""><span class="chg">' + esc(D.ex.changements[ch]) + '</span><img src="' + parId[g].img + '" alt=""></span>';

// C · l'allergie, éliminatoire.
function cItem(){
  Bruit.arreter();
  const it = F().C[T.ci];
  if (!it) return introPartie('D');
  app.innerHTML = enTete('partC', T.ci, F().C.length) + '<p class="qui">' + t(it.qui) + '</p>'
    + '<div class="ecoute"><button class="btn-rj btn-rj--pri btn-rj--pile" data-t="son">' + tb('reecouter') + '</button></div>'
    + '<div class="choix mots actes">' + it.actes.map((a, i) => '<div class="acte-ligne"><button class="opt" data-r="' + i + '">' + t(a.k) + '</button></div>').join('') + '</div>';
  jouerNormal(it.son);
}
function cRepondre(i){ const it = F().C[T.ci]; T.C.push(it.actes[i].s); T.ci++; tGarder(); cItem(); }

// D · redire à voix haute, enregistré sur l'appareil.
let rec = null, morceaux = [];
function dItem(){
  const it = F().D[T.di];
  if (!it) return finTest();
  app.innerHTML = enTete('partD', T.di, F().D.length) + '<p class="qui">' + t(it.qui) + '</p>'
    + '<div class="ecoute"><button class="btn-rj btn-rj--pri btn-rj--pile" data-t="une">' + tb('jouer_une') + '</button></div>'
    + '<div class="oral"><button class="btn-rj btn-rj--pile rec" data-t="rec"' + ((T.joue || {})[it.id] ? '' : ' disabled') + '>' + tb('enregistrer') + '</button>'
    + ((T.joue || {})[it.id] ? '' : '<p class="verrou" id="verrou">' + t('ecoute_dabord') + '</p>')
    + '<p class="etat" id="etat" aria-live="polite"></p><button class="btn-rj btn-rj--pile" data-t="passer">' + tb('passer') + '</button></div>';
}
function dJouer(b){
  const it = F().D[T.di];
  b.disabled = true; b.innerHTML = tb('deja_joue');
  audio.onplaying = () => { audio.onplaying = null; T.joue = T.joue || {}; T.joue[it.id] = true; tGarder(); };
  const ouvrir = () => { audio.onended = audio.onerror = null; clearTimeout(T._s); const r = app.querySelector('[data-t=rec]'); if (r) { r.disabled = false; r.focus({preventScroll: true}); }
    const v = document.getElementById('verrou'); if (v) v.remove(); };
  audio.onended = audio.onerror = ouvrir; T._s = setTimeout(ouvrir, 12000);
  jouerNormal(it.son);
}
async function dEnregistrer(b){
  const it = F().D[T.di], etat = document.getElementById('etat');
  if (rec && rec.state === 'recording') { rec.stop(); return; }
  try {
    const flux = await navigator.mediaDevices.getUserMedia({audio: true});
    morceaux = []; rec = new MediaRecorder(flux);
    rec.ondataavailable = e => morceaux.push(e.data);
    rec.onstop = async () => {
      flux.getTracks().forEach(x => x.stop());
      await idb.mettre(T.forme + '-' + it.id, new Blob(morceaux, {type: rec.mimeType || 'audio/webm'}));
      T.D[it.id] = true; etat.innerHTML = t('enregistre');
      T.di++; tGarder(); setTimeout(dItem, 700);
    };
    rec.start(); b.innerHTML = tb('arreter'); b.classList.add('en-cours'); etat.textContent = '●';
  } catch(e) {
    // Pas de micro (refusé, absent) : ce n'est pas « ne sait pas parler ». L'item
    // est marqué « micro » — l'oral se fera avec le formateur, palier provisoire.
    etat.innerHTML = t('micro_test');
    T.D[it.id] = 'micro'; T.micro = true; tGarder();
    const p = app.querySelector('[data-t=passer]'); if (p) p.innerHTML = tb('continuer');
  }
}
function dPasser(){ if (rec && rec.state === 'recording') { rec.onstop = null; rec.stop(); }
  const id = F().D[T.di].id; if (T.D[id] !== 'micro') T.D[id] = T.micro ? 'micro' : false; T.di++; tGarder(); dItem(); }

function finTest(){ T.termine = true; T.partie = null; tGarder(); Bruit.arreter(); resultats(); }

// Le palier, par la règle de test.py appliquée une seule fois.
// (audit du test, tour 1) Un item passé compte « Rien ou faux » ; sans oral
// noté en entier, le palier est PROVISOIRE et ne dépasse pas « fonctionnel ».
function oralNotes(){
  // Enregistré, ou sans micro (noté par le formateur de vive voix) : la note du
  // formateur. Sauté alors que le micro marchait : « Rien ou faux ».
  return F().D.map(it => T.D[it.id] ? ((T.oral || {})[it.id] || {}) : {r: 2, l: 2, passe: true});
}
function oralComplet(){ return oralNotes().every(n => n.r != null && n.l != null); }
function palierPropose(){
  const R = TD.regles, A = T.A.niveau, B = T.B.filter(Boolean).length, cOk = !T.C.includes('grave');
  const notes = oralNotes(), complet = oralComplet();
  if (A <= R.debutant_a || B <= R.debutant_b) return 'debutant';
  if (notes.filter(n => n.r === 2).length >= R.oral_debutant) return 'debutant';   // n.r vide pour un item sans micro
  if (!complet) return 'fonctionnel';
  const oralOk = notes.filter(n => n.r === 0).length >= R.oral_aise && notes.filter(n => n.l === 2).length <= 1;
  if (A === 3 && B >= R.aise_b && cOk && oralOk) return 'aise';
  return 'fonctionnel';
}
function resultats(){
  arreter(); adresse({ecran: 'test'});
  const pal = T.palier || palierPropose(), cOk = !T.C.includes('grave');
  let h = tete('resultat', null, 'accueil')
    + '<div class="resultat"><div class="bloc"><p>' + t('palier_propose') + '</p><p class="gros-palier">' + t('p_' + pal) + '</p>'
    + '<p class="' + (cOk ? 'ok-txt' : 'grave-sous') + '">' + t(cOk ? 'c_reussie' : 'c_ratee') + '</p>'
    + (!T.confirme && !oralComplet() ? '<p class="seuil">' + t(T.micro ? 'provisoire_micro' : 'provisoire') + '</p>' : '')
    + '<p class="n">' + (T.confirme ? t('confirme') : t('pas_examen')) + '</p></div>'
    + '<div class="bloc parts">'
    + '<div><span>' + t('res_A') + '</span><b>' + T.A.niveau + ' / 3</b></div>'
    // (audit, tour 1, A3) deux compétences, deux postes : la cuisine et la salle à part.
    + '<div><span>' + t('res_B_chef') + '</span><b>' + F().B.filter((it, i) => it.type === 'chef' && T.B[i]).length + ' / ' + F().B.filter(it => it.type === 'chef').length + '</b></div>'
    + '<div><span>' + t('res_B_commande') + '</span><b>' + F().B.filter((it, i) => it.type === 'commande' && T.B[i]).length + ' / ' + F().B.filter(it => it.type === 'commande').length + '</b></div>'
    + '<div><span>' + t('ex_allergie') + '</span><b>' + T.C.filter(s => s === 'juste').length + ' / ' + F().C.length + '</b></div>'
    + '<div><span>' + t('res_D') + '</span><b>' + (T.micro && !oralComplet() ? t('avec_formateur') : !Object.values(T.D).some(Boolean) ? t('rien_enregistre') : oralComplet() ? '✓' : t('non_note')) + '</b></div>'
    + '<p class="n">' + esc(FR.forme) + ' ' + T.forme + '</p></div>';
  h += '<div class="bloc formateur" id="formateur">' + (T._ouvert ? formateurHTML() : '<h2>' + t('formateur') + '</h2><div class="code-f"><label for="codeF">' + esc(FR.code) + '</label>'
    + '<input id="codeF" inputmode="numeric" autocomplete="off"><button class="btn-rj" data-t="code">' + esc(FR.ouvrir) + '</button></div>') + '</div>';
  // (audit, tour 1, F1) La passation d'avant, gardée : l'écart est la preuve d'apprentissage.
  const avant = lire(TH, []).filter(x => x.quand !== T.quand).slice(-1)[0];
  if (avant) h += '<div class="bloc parts"><h2>' + t('avant_maintenant') + '</h2>'
    + '<div><span>' + t('res_A') + '</span><b>' + avant.A + ' → ' + T.A.niveau + '</b></div>'
    + '<div><span>' + t('res_B') + '</span><b>' + avant.B + ' → ' + T.B.filter(Boolean).length + '</b></div>'
    + '<div><span>' + t('palier_propose') + '</span><b>' + esc(FR['p_' + avant.palier]) + ' → ' + esc(FR['p_' + (T.palier || palierPropose())]) + '</b></div></div>';
  app.innerHTML = h + '</div>';
}
function formateurHTML(){
  const pal = palierPropose();
  return '<h2>' + t('formateur') + '</h2>' + F().D.map(it => {
      const n = (T.oral || {})[it.id] || {};
      return '<div class="oral-f"><p class="qui">' + t(it.qui) + '</p><p><b>« ' + esc(it.attendu) + ' »</b></p>'
        + '<div class="gestes-bilan">' + (T.D[it.id] === true ? '<button class="btn-rj petit" data-t="ecoute-rep" data-id="' + it.id + '">' + ICO.son + esc(FR.ecouter_reponse) + '</button>' : '')
        + '<button class="btn-rj petit" data-t="ecoute-mod" data-id="' + it.id + '">' + ICO.son + esc(FR.modele) + '</button></div>'
        + (T.D[it.id] === 'micro' ? '<p class="n">' + esc(FR.oral_de_vive_voix) + '</p><p>' + esc(FR.phrase_a_redire) + ' : « ' + esc(it.phrase) + ' » <button class="btn-rj petit" data-t="ecoute-phrase" data-id="' + it.id + '">' + ICO.son + '</button></p>' : '')
        + (T.D[it.id] ? '' : '<p class="n">' + esc(FR.pas_de_reponse) + '</p></div>')
        + (!T.D[it.id] ? '' : '<p class="n">' + esc(FR.oral_redit) + '</p><div class="choisir3">' + TD.oral_redit.map((x, k) => '<button class="btn-rj petit" data-t="or" data-id="' + it.id + '" data-k="' + k + '" aria-pressed="' + (n.r === k) + '">' + esc(x) + '</button>').join('') + '</div>'
        + '<p class="n">' + esc(FR.oral_langue) + '</p><div class="choisir3">' + TD.oral_langue.map((x, k) => '<button class="btn-rj petit" data-t="ol" data-id="' + it.id + '" data-k="' + k + '" aria-pressed="' + (n.l === k) + '">' + esc(x) + '</button>').join('') + '</div></div>');
    }).join('')
    + '<p>' + esc(FR.palier_propose) + ' : <b>' + esc(FR['p_' + pal]) + '</b></p>'
    + '<div class="choisir3">' + ['debutant', 'fonctionnel', 'aise'].map(p => '<button class="btn-rj" data-t="confirmer" data-p="' + p + '" aria-pressed="' + (T.confirme && T.palier === p) + '">' + esc(FR['p_' + p]) + '</button>').join('') + '</div>'
    + '<label class="n" for="notesF">' + esc(FR.notes) + ' — ' + esc(FR.aucun_nom) + '</label><textarea id="notesF" rows="3">' + esc(T.notes || '') + '</textarea>'
    + (T.confirme ? '<p><button class="btn-rj btn-rj--pile" data-t="refaire">' + tb('refaire_test') + '</button></p>' : '');
}
async function ecouterBlob(id){ const b = await idb.prendre(T.forme + '-' + id); if (b) { audio.pause(); audio.src = URL.createObjectURL(b); audio.play().catch(() => {}); } }

app.addEventListener('input', e => { if (e.target.id === 'notesF' && T) { T.notes = e.target.value; tGarder(); } });
app.addEventListener('click', e => {
  const b = e.target.closest('[data-t], [data-r]'); if (!b || !app.contains(b)) return;
  e.stopImmediatePropagation();
  const a = b.dataset.t;
  if (a === 'demarrer') return demarrer();
  if (a === 'partie') return lancerPartie();
  if (a === 'son') { const p = T.partie, it = p === 'A' ? F().A[T.A.cran][T.A.i] : F().C[T.ci]; return jouerNormal(it.son); }
  if (a === 'une') return T.partie === 'D' ? dJouer(b) : bJouer(b);
  if (a === 'rec') return dEnregistrer(b);
  if (a === 'passer') return dPasser();
  if (b.dataset.r != null) { const i = +b.dataset.r; return ({A: aRepondre, B: bRepondre, C: cRepondre})[T.partie](i); }
  if (a === 'code') { if (document.getElementById('codeF').value.trim() === TD.code) { T._ouvert = true; resultats(); } else document.getElementById('codeF').value = ''; return; }
  if (a === 'ecoute-rep') return ecouterBlob(b.dataset.id);
  if (a === 'ecoute-phrase') return jouerNormal(F().D.find(x => x.id === b.dataset.id).son);
  if (a === 'ecoute-mod') return jouerNormal(F().D.find(x => x.id === b.dataset.id).modele);
  if (a === 'or' || a === 'ol') { T.oral = T.oral || {}; const n = T.oral[b.dataset.id] = T.oral[b.dataset.id] || {}; n[a === 'or' ? 'r' : 'l'] = +b.dataset.k; tGarder(); return resultats(); }
  if (a === 'confirmer') {
    T.palier = b.dataset.p; T.confirme = true; tGarder();
    // L'historique ne garde que des chiffres, jamais la voix ; les voix s'effacent à la confirmation.
    const h = lire(TH, []).filter(x => x.quand !== T.quand);
    h.push({quand: T.quand, forme: T.forme, A: T.A.niveau, B: T.B.filter(Boolean).length, C: T.C.includes('grave') ? 'grave' : 'ok', palier: T.palier});
    ecrire(TH, h.slice(-6)); idb.vider();
    return resultats();
  }
  if (a === 'refaire') { try { localStorage.removeItem(TK); } catch(e){} idb.vider(); T = null; return test(); }
}, true);

/* ═══ Étape 4 : le service joué ════════════════════════════════════════
   Deux portes : en cuisine, l'IA joue le chef (l'élève est commis) ; en salle,
   le client (l'élève sert). /api/jeu-de-role, scénarios « resto-cuisine » et
   « resto-salle » (source : build/contenu/entreprise-restaurant/situations.py).
   Il faut un code d'élève ou de séance. L'IA ouvre chaque réplique par son
   humeur entre crochets ; l'écran la retire et la DIT. « FIN » clôt. Micro et
   voix ne tournent jamais ensemble : ouvert, le micro dégrade la sortie audio. */
const SV = D.service;
let codeAcces = new URLSearchParams(location.search).get('code') || '';
// Le code authentifie : il ne reste pas dans l'adresse ni dans l'historique (audit, tour 1).
// Sauf en séance (activityId présent) : un rechargement perdrait le lien avec le direct
// de la classe (vu à la répétition générale du 30 sept. 2026).
if (codeAcces && !new URLSearchParams(location.search).get('activityId')) { try { localStorage.setItem('resto-code', codeAcces); } catch(e) {} const u = new URL(location.href); u.searchParams.delete('code'); history.replaceState(null, '', u); }
try { codeAcces = codeAcces || localStorage.getItem('resto-code') || ''; } catch(e) {}
if (!codeAcces && CTX) codeAcces = CTX.code;   // en séance : le jeton du participant
let niveauJeu = null, V = null;
function niveauDuTest(){ const r = lire('resto-test', null); return r && r.termine ? (r.palier || palierDe(r)) : null; }
function palierDe(r){ const T0 = T; T = r; try { return palierPropose(); } finally { T = T0; } }

function service(){
  arreter(); arreterService();
  adresse({ecran: 'service'});
  niveauJeu = niveauJeu || niveauDuTest();
  if (!codeAcces) {
    app.innerHTML = tete('service', 'code_aide', 'accueil')
      + '<div class="code-f"><label for="codeIn"><b>' + esc(FR.code_acces) + '</b></label><input id="codeIn" maxlength="8" autocomplete="off">'
      + '<button class="btn-rj btn-rj--pri" data-s="code">' + esc(FR.entrer) + '</button></div>';
    return;
  }
  const l = L();
  app.innerHTML = tete('service', 'service_sous', 'accueil')
    + '<p class="n">' + t('ia_avis') + '</p>'
    + '<p style="margin:10px 0 4px"><b>' + t('niveau_jeu') + '</b>' + (niveauJeu ? '' : '<span class="n">' + t('faire_test') + '</span>') + '</p>'
    + '<div class="choisir3">' + ['debutant', 'fonctionnel', 'aise'].map(p => '<button class="btn-rj petit" data-s="niv" data-v="' + p + '" aria-pressed="' + (p === niveauJeu) + '">' + esc(FR['p_' + p]) + '</button>').join('') + '</div>'
    + ['cuisine', 'salle'].map(p => '<h2 class="porte-titre">' + t('porte_' + p) + '<span class="appui-sous">' + t('porte_' + p + '_sous') + '</span></h2><div class="clients">'
      + SV.situations.filter(s => s.porte === p && (!niveauJeu || s.paliers.includes(niveauJeu))).map(s =>
        '<button class="client" data-s="scene" data-id="' + s.id + '"><img src="' + SV.decor[p] + '" alt=""><b>' + esc(s.nom) + '</b><span>' + t('carte_' + s.id) + '</span></button>').join('')
      + '</div>').join('');
}

function arreterService(){ if (typeof recoStop === 'function') recoStop(); try { audio.pause(); } catch(e){} Bruit.arreter(); }
function scene(id){
  const s = SV.situations.find(x => x.id === id);
  if (!niveauJeu) niveauJeu = 'debutant';
  // (audit, tour 1) O1 se pratique ENTENDU : en cuisine, dès le palier fonctionnel,
  // le texte du chef est masqué par défaut, et le bruit de cuisine joue.
  const masquer = s.porte === 'cuisine' && niveauJeu !== 'debutant';
  V = {s, hist: [], humeur: 'neutre', fini: false, sansLire: masquer, porte: SV.portes[s.porte]};
  adresse({ecran: 'service', sit: id});
  app.innerHTML = tete('service', null, 'service')
    + '<div class="scene"><div class="avatar"><img src="' + SV.decor[s.porte] + '" alt=""><p class="nom">' + esc(s.nom) + '</p><p class="humeur" id="hum" aria-live="polite"></p>'
    + '<p class="carte-sit">' + t('carte_' + s.id) + '</p></div>'
    + '<div><div class="choisir3"><button class="btn-rj petit" data-s="sanslire" aria-pressed="' + V.sansLire + '">' + esc(FR.ecouter_sans_lire) + '</button>'
    + (s.cuisine ? '<button class="btn-rj petit" data-s="verifier" id="btnVerif" hidden>' + esc(FR.aller_verifier) + '</button>' : '') + '</div>'
    + '<div class="bloc regle" id="repCuisine" hidden><p class="n">' + esc(FR.cuisine_dit) + '</p><p>' + t('rc_' + s.id) + '</p></div>'
    + '<details class="bloc phrases-scene"><summary><b>' + t('mes_gestes') + '</b></summary><ul class="gestes-liste">'
    + s.gestes.map(g => { const G = SV.gestes.find(x => x.id === g); return '<li><b>' + t('g_' + g) + '</b> — « ' + esc(G.phrase) + ' »</li>'; }).join('') + '</ul></details>'
    + '<div class="fil' + (V.sansLire ? ' cache' : '') + '" id="fil" aria-live="polite"></div>'
    + '<div class="saisie"><button class="btn-rj rec" id="micro" data-s="micro">' + esc(FR.parler) + '</button>'
    + '<input id="txt" placeholder="' + esc(FR.ecrire) + '" aria-label="' + esc(FR.ecrire) + '"><button class="btn-rj btn-rj--pri" id="env" data-s="envoyer">' + esc(FR.envoyer) + '</button></div>'
    + '<div class="suite" id="suiteSc"><button class="btn-rj" data-s="fini">' + esc(FR.fini) + '</button></div>'
    + '<p class="retro non" id="err"></p></div></div>';
  montrerHumeur('neutre');
  window.scrollTo(0, 0);
  if (s.porte === 'cuisine') { Bruit.niveau = Math.max(1, lire(BRUIT, 1)); Bruit.demarrer(); }
  tourService();
}
function bulleS(qui, texte){
  const fil = document.getElementById('fil'); if (!fil) return;
  const d = document.createElement('div'); d.className = 'bulle ' + (qui === 'vous' ? 'vous' : 'client');
  d.innerHTML = '<span class="qui">' + (qui === 'vous' ? esc(FR.vous) : esc(V.s.nom)) + '</span><span class="txt">' + esc(texte) + '</span>';
  fil.appendChild(d); d.scrollIntoView({block: 'nearest'});
}
function lireHumeur(txt){
  let h = 'neutre', fin = false;
  const m = txt.match(/^\s*\[([^\]]+)\]\s*/);
  if (m) { h = m[1].toLowerCase().normalize('NFD').replace(/[̀-ͯ]/g, '').replace(/e$/, ''); txt = txt.slice(m[0].length); }
  if (!SV.humeurs.includes(h)) h = 'neutre';
  txt = txt.replace(/\[[^\]]*\]/g, '').trim();
  if (/\bFIN\.?\s*$/.test(txt)) { fin = true; txt = txt.replace(/\s*\bFIN\.?\s*$/, '').trim(); }
  return {h, txt, fin};
}
function montrerHumeur(h){
  V.humeur = h;
  const f = V.s.voix === 'jr_feminin', k = 'humeur_' + h + (f && (h === 'content') ? '_f' : '');
  const e = document.getElementById('hum'); if (e) e.innerHTML = esc(V.s.nom) + ' ' + t(k);
}
async function tourService(){
  const err = document.getElementById('err'); err.textContent = '';
  const attente = document.createElement('p'); attente.className = 'attente'; attente.textContent = '…';
  document.getElementById('fil').appendChild(attente);
  try {
    const r = await fetch('/api/jeu-de-role', {method: 'POST', headers: {'Content-Type': 'application/json'},
      body: JSON.stringify({code: codeAcces, scenario: V.porte.scenario, cas: V.s.id, role: V.porte.eleve, niveau: niveauJeu, historique: V.hist})});
    const d = await r.json().catch(() => ({}));
    attente.remove();
    if (!r.ok) {
      if (r.status === 401) { codeAcces = ''; try { localStorage.removeItem('resto-code'); } catch(e){} err.textContent = FR.code_refuse; }
      else err.innerHTML = esc(d.error || FR.erreur_reseau) + ' <button class="btn-rj petit" data-s="reessayer">' + esc(FR.reessayer) + '</button>';
      return;
    }
    if (d.ouverture) { V.hist.push({role: 'user', contenu: d.ouverture}); bulleS('vous', d.ouverture); }
    V.hist.push({role: 'assistant', contenu: d.reponse});
    const {h, txt, fin} = lireHumeur(d.reponse);
    montrerHumeur(h); bulleS('ia', txt); direS(txt);
    if (fin) {
      V.fini = true;
      ['txt', 'env', 'micro'].forEach(id => { const x = document.getElementById(id); if (x) x.disabled = true; });
      document.getElementById('suiteSc').innerHTML = '<button class="btn-rj btn-rj--pri" data-s="fini">' + esc(FR.voir_bilan) + ICO.d + '</button>';
    }
  } catch(e) { attente.remove(); err.innerHTML = esc(FR.erreur_reseau) + ' <button class="btn-rj petit" data-s="reessayer">' + esc(FR.reessayer) + '</button>'; }
}
function envoyerS(texte){
  texte = (texte || '').trim(); if (!texte || V.fini) return;
  arreterService();
  document.getElementById('txt').value = '';
  V.hist.push({role: 'user', contenu: texte}); bulleS('vous', texte);
  // Le bouton de la cuisine n'apparaît qu'une fois que l'employé a dit qu'il allait
  // vérifier : sinon il révélait la réponse avant la question (audit, tour 2).
  const bv = document.getElementById('btnVerif'); if (bv && /v[ée]rifi|cuisine|demande/i.test(texte)) bv.hidden = false;
  tourService();
}
async function direS(txt){
  if (!txt) return;
  try {
    const palier = SV.debit[niveauJeu] || null;
    const r = await fetch('/api/voix', {method: 'POST', headers: {'Content-Type': 'application/json'},
      body: JSON.stringify({code: codeAcces, texte: txt, role: V.porte.eleve, personnage: V.s.voix, palier})});
    if (!r.ok) throw new Error();
    audio.pause(); audio.src = URL.createObjectURL(await r.blob());
    audio.playbackRate = 1;
    if (palier && !r.headers.get('X-Palier')) { audio.preservesPitch = true; audio.playbackRate = 0.8; }
    audio.play().catch(() => {});
  } catch(e) { const err = document.getElementById('err'); if (err) err.textContent = FR.voix_indispo; }
}
// Le micro : continu, il ACCUMULE, se relance si le navigateur le coupe, et
// s'arrête sur « Arrêter » ou après un vrai silence (leçon de Francœur).
const SILENCE_MS = 4000, SILENCE_DEBUT_MS = 9000;
let reco = null, recoFini = true, recoMinuterie = null;
function recoStop(){ recoFini = true; clearTimeout(recoMinuterie); if (reco) { const r = reco; reco = null; r.onend = null; try { r.abort(); } catch(e){} } }
function microS(){
  const R = window.SpeechRecognition || window.webkitSpeechRecognition;
  const b = document.getElementById('micro'), txt = document.getElementById('txt');
  if (!R) { document.getElementById('err').textContent = FR.micro_refuse; return; }
  if (reco) { recoFini = true; reco.stop(); return; }
  audio.pause(); Bruit.arreter();   // le micro ne doit pas entendre le bruit fabriqué
  let acquis = '';
  recoFini = false;
  const attendre = ms => { clearTimeout(recoMinuterie); recoMinuterie = setTimeout(() => { recoFini = true; if (reco) reco.stop(); }, ms); };
  const terminer = () => { clearTimeout(recoMinuterie); reco = null; b.textContent = FR.parler;
    if (V && V.s.porte === 'cuisine' && !V.fini) Bruit.demarrer();
    const dit = txt.value.trim(); if (dit) envoyerS(dit); };
  const demarrerR = () => {
    reco = new R(); reco.lang = 'fr-CA'; reco.interimResults = true; reco.continuous = true;
    reco.onresult = e => {
      let prov = '';
      for (let i = e.resultIndex; i < e.results.length; i++) {
        const x = e.results[i][0].transcript.trim();
        if (e.results[i].isFinal) acquis = (acquis + ' ' + x).trim(); else prov += ' ' + x;
      }
      txt.value = (acquis + prov).trim(); attendre(SILENCE_MS);
    };
    reco.onend = () => { if (!recoFini) { try { demarrerR(); return; } catch(e){} } terminer(); };
    reco.onerror = ev => { if (ev.error === 'no-speech' || ev.error === 'aborted') return; recoFini = true; document.getElementById('err').textContent = FR.micro_refuse; };
    reco.start();
  };
  txt.value = ''; demarrerR(); attendre(SILENCE_DEBUT_MS);
  b.textContent = FR.arreter;
}
async function bilanService(){
  arreterService();
  const mes = V.hist.filter(m => m.role === 'user').map(m => m.contenu).slice(1);   // l'ouverture est écrite par la page
  app.innerHTML = tete('bilan_titre', null, 'service')
    + '<div class="resultat"><div class="bloc"><p style="margin:0;font-weight:800">' + esc(V.s.nom) + ' ' + t('humeur_' + V.humeur + (V.s.voix === 'jr_feminin' && V.humeur === 'content' ? '_f' : '')) + '</p></div>'
    + '<div class="bloc" id="graveBloc" hidden></div>'
    + '<div class="bloc"><b>' + t('gestes_titre') + '</b><div id="gestesBilan"><p class="attente">' + esc(FR.bilan_attente) + '</p></div></div>'
    + '<details class="bloc"><summary><b>' + t('vos_phrases') + '</b></summary><div id="corr"><p class="attente">…</p></div></details>'
    + '<div class="gestes-bilan"><button class="btn-rj btn-rj--pri btn-rj--pile" data-s="retour">' + tb('autre_situation') + '</button></div></div>';
  const zone = document.getElementById('gestesBilan');
  if (!mes.length) { zone.innerHTML = '<p>—</p>'; document.getElementById('corr').innerHTML = '<p>—</p>'; return; }
  try {
    const r = await fetch('/api/jeu-de-role', {method: 'POST', headers: {'Content-Type': 'application/json'},
      body: JSON.stringify({code: codeAcces, scenario: V.porte.scenario, cas: V.s.id, role: V.porte.eleve, niveau: niveauJeu, bilan: true, historique: V.hist.slice(1)})});
    let d = await r.json().catch(() => ({}));
    // Un geste attendu manque (le juge a inventé un id) : on relance une fois.
    const manque = b => !b || V.s.gestes.some(g => !(b.gestes || []).some(x => x.id === g));
    if (r.ok && manque(d.bilan)) {
      const r2 = await fetch('/api/jeu-de-role', {method: 'POST', headers: {'Content-Type': 'application/json'},
        body: JSON.stringify({code: codeAcces, scenario: V.porte.scenario, cas: V.s.id, role: V.porte.eleve, niveau: niveauJeu, bilan: true, historique: V.hist.slice(1)})});
      const d2 = await r2.json().catch(() => ({})); if (r2.ok && d2.bilan && !manque(d2.bilan)) d = d2;
    }
    if (!r.ok || !d.bilan) zone.innerHTML = '<p>' + esc(d.error || FR.erreur_reseau) + '</p>';
    else {
      const B = d.bilan;
      // L'erreur grave à l'allergie, À PART et en tête : c'est l'éliminatoire.
      if (B.grave && V.s.gestes.includes('allergie')) { const g = document.getElementById('graveBloc'); g.hidden = false; g.className = 'bloc regle';
        g.innerHTML = '<p class="grave-sous">' + t('grave_service') + '</p>' + (B.grave_citation ? '<p>« ' + esc(B.grave_citation) + ' »</p>' : '') + '<p>' + t('critere_grave') + '</p>'; }
      const nom = id => FR['g_' + id] || id;
      // Le juge invente parfois un geste ou en répète un : on ne garde que les
      // gestes connus, une fois chacun (essai réel du 30 sept. 2026).
      const connus = new Set(SV.gestes.map(g => g.id)), vus = new Set();
      const G0 = (B.gestes || []).filter(g => connus.has(g.id) && !vus.has(g.id) && vus.add(g.id));
      // Un geste attendu que le juge n'a pas rendu, même après la relance : dit « non évalué », jamais tu.
      V.s.gestes.filter(id => !vus.has(id)).forEach(id => G0.push({id, necessaire: true, fait: false, nonEvalue: true}));
      const G = G0.filter(g => g.necessaire).concat(G0.filter(g => !g.necessaire));
      // Au direct : chaque geste nécessaire, puis la situation (réussie : aucun geste nécessaire manqué, pas d'erreur grave).
      const titre = 'Le service · ' + niveauJeu;
      G.filter(g => g.necessaire && !g.nonEvalue).forEach(g => rapporter({zone: 'rj-jeu-' + V.s.id + '-' + g.id, exo: 'rj-jeu', exoNum: titre,
        exoTitre: 'Le service', section: 'service', type: 'geste', enonce: (FR['g_' + g.id] || g.id) + ' — ' + V.s.nom + ' (' + V.s.id + ')', ok: !!g.fait}));
      rapporter({zone: 'rj-jeu-' + V.s.id, exo: 'rj-jeu', exoNum: titre, exoTitre: 'Le service', section: 'service', type: 'situation',
        enonce: 'Situation : ' + V.s.id + (B.grave && V.s.gestes.includes('allergie') ? ' (erreur grave à l’allergie)' : ''),
        ok: !(B.grave && V.s.gestes.includes('allergie')) && G.filter(g => g.necessaire && !g.nonEvalue).every(g => g.fait)});
      zone.innerHTML = (B.resume ? '<p>' + esc(B.resume) + '</p>' : '') + '<ul class="bilan-gestes">' + G.map(g => {
        const e = g.nonEvalue ? 'inutile' : !g.necessaire ? 'inutile' : g.fait ? 'fait' : 'manque';
        return '<li class="' + e + '"><span class="marque">' + (e === 'fait' ? '✓' : e === 'manque' ? '→' : '·') + '</span><span><b>' + esc(nom(g.id)) + '</b> — '
          + esc(g.nonEvalue ? FR.non_evalue : FR['geste_' + e]) + (g.citation ? '<small>« ' + esc(g.citation) + ' »</small>' : '') + (e === 'manque' && g.conseil ? '<small>' + esc(g.conseil) + '</small>' : '') + '</span></li>'; }).join('') + '</ul>';
    }
  } catch(e) { zone.innerHTML = '<p>' + esc(FR.erreur_reseau) + '</p>'; }
  const corr = document.getElementById('corr');
  try {
    const r = await fetch('/api/correct-french', {method: 'POST', headers: {'Content-Type': 'application/json'},
      body: JSON.stringify({code: codeAcces, text: mes.join(' '),
        question: "Vous travaillez dans un restaurant familial au Québec" + (V.s.porte === 'cuisine' ? ", en cuisine, et vous répondez au chef" : ", en salle, et vous répondez à un client") + ". À l'oral, en français québécois courant : « Oui, chef : deux poutines » et « Un hamburger sans oignons, c'est bien ça ? » sont justes. Ne corrige que les vraies fautes de français (grammaire, prépositions, accords), jamais le style, le registre ni une tournure déjà juste, et explique chaque correction."})});
    const d = await r.json();
    if (!r.ok) { corr.innerHTML = '<p>' + esc(d.error || FR.erreur_reseau) + '</p>'; return; }
    corr.innerHTML = '<p style="font-size:18px;font-weight:700;color:var(--text-strong)">' + esc(d.corrige) + '</p>' + (d.erreurs || []).map(x => '<p style="margin:4px 0">· ' + esc(x.explication) + '</p>').join('');
  } catch(e) { corr.innerHTML = '<p>' + esc(FR.erreur_reseau) + '</p>'; }
}
app.addEventListener('keydown', e => { if (e.target.id === 'txt' && e.key === 'Enter' && V) envoyerS(e.target.value); });
app.addEventListener('click', e => {
  const b = e.target.closest('[data-s]'); if (!b || !app.contains(b)) return;
  e.stopImmediatePropagation();
  const a = b.dataset.s;
  if (a === 'code') { codeAcces = document.getElementById('codeIn').value.trim().toUpperCase(); if (!codeAcces) return; try { localStorage.setItem('resto-code', codeAcces); } catch(e){} return service(); }
  if (a === 'niv') { niveauJeu = b.dataset.v; return service(); }
  if (a === 'scene') return scene(b.dataset.id);
  if (a === 'retour') { arreterService(); V = null; return service(); }
  if (a === 'sanslire') { V.sansLire = !V.sansLire; b.setAttribute('aria-pressed', String(V.sansLire)); document.getElementById('fil').classList.toggle('cache', V.sansLire); return; }
  if (a === 'envoyer') return envoyerS(document.getElementById('txt').value);
  if (a === 'micro') return microS();
  if (a === 'fini') return bilanService();
  if (a === 'reessayer') { document.getElementById('err').textContent = ''; return tourService(); }
  if (a === 'verifier') { document.getElementById('repCuisine').hidden = false; V.verifie = true; return; }
}, true);

app.addEventListener('change', e => { if (e.target.id === 'filtre' && S) lancer(S.k, e.target.value); });
app.addEventListener('click', e => {
  const b = e.target.closest('button'); if (!b) return;
  if (b.dataset.lang) { langue = b.dataset.lang === 'fr' ? null : b.dataset.lang; poserLangue(b.dataset.lang); return accueil(); }
  const a = b.dataset.act;
  if (a === 'langue') return ecranLangue();
  if (a === 'accueil') return accueil();
  if (a === 'planches') return planches();
  if (a === 'exercices') return exercices();
  if (a === 'test') return test();
  if (a === 'service') { V = null; return service(); }
  if (b.dataset.ex) { lancer(b.dataset.ex); window.scrollTo(0, 0); return; }
  if (b.dataset.planche) { planche(b.dataset.planche); window.scrollTo(0, 0); return; }
  if (b.dataset.bruit != null) { Bruit.regler(+b.dataset.bruit); app.querySelectorAll('[data-bruit]').forEach(x => x.setAttribute('aria-pressed', x === b)); return; }
  if (a === 'commencer') { const k = new URLSearchParams(location.search).get('ex'); return lancer(k, 'x'); }
  if (b.dataset.regle != null) return jouerNormal(D.ex.regle[+b.dataset.regle]);
  if (b.dataset.formule != null) return jouerNormal(D.ex.formules[+b.dataset.formule].son);
  if (a === 'encore') return lancer(S.k, S.x.filtre ? S.filtre : 'x');
  if (S) {
    const it = S.items[S.n];
    if (a === 'reecouter') return jouerNormal(it.son);
    if (a === 'lent') return jouerLent(it.son);
    if (a === 'apresson') return jouerNormal(it.apresSon);
    if (a === 'suivant') { S.n++; item(); window.scrollTo(0, 0); return; }
    if (b.dataset.o != null) return repondre(+b.dataset.o);
    if (b.dataset.acte != null) return jouerNormal(it.choix[+b.dataset.acte].son);
    if (a === 'voirmot') {
      const m = it.rappel;
      document.getElementById('revele').innerHTML = '<p class="gros">' + esc(m.mot) + '</p>'
        + '<div class="gestes-bilan"><button class="btn-rj btn-rj--pile" data-act="bien">' + tb('savais') + '</button><button class="btn-rj btn-rj--pile" data-act="mal">' + tb('a_revoir') + '</button></div>';
      jouerNormal(m.son); return;
    }
    if (a === 'modele') {
      document.getElementById('revele').innerHTML = '<p class="gros-phrase">« ' + esc(it.redit) + ' »</p><p class="dit">' + esc(FR.phrase) + ' : « ' + esc(it.phrase) + ' »</p>'
        + '<div class="gestes-bilan"><button class="btn-rj petit" data-act="remodele">' + ICO.son + esc(FR.modele) + '</button></div>'
        + '<div class="gestes-bilan"><button class="btn-rj btn-rj--pile" data-act="bien">' + tb('bien_dit') + '</button><button class="btn-rj btn-rj--pile" data-act="mal">' + tb('a_refaire') + '</button></div>';
      jouerNormal(it.modele); return;
    }
    if (a === 'remodele') return jouerNormal(it.modele);
    if (a === 'bien') return autoEval(true);
    if (a === 'mal') return autoEval(false);
  }
  if (b.dataset.i != null) return ouvrir(+b.dataset.i);
});
carte.addEventListener('click', e => {
  const b = e.target.closest('button'); if (!b) return;
  const m = liste[rang];
  if (b.dataset.act === 'fermer') return fermer();
  if (b.dataset.act === 'ecouter') return jouer(m.son);
  if (b.dataset.act === 'autre') return jouer(m.autre_son);
  if (b.dataset.act === 'prec' && rang > 0) return ouvrir(rang - 1);
  if (b.dataset.act === 'suiv' && rang < liste.length - 1) return ouvrir(rang + 1);
  if (b.dataset.act === 'voir') {
    const tr = $('#trad'), vu = tr.hidden; tr.hidden = !vu;
    b.setAttribute('aria-expanded', vu); b.innerHTML = tb(vu ? 'cacher' : 'voir');
  }
});
fiche.addEventListener('click', e => { if (e.target === fiche) fermer(); });
document.addEventListener('keydown', e => {
  if (fiche.hidden) return;
  if (e.key === 'Escape') fermer();
  if (e.key === 'ArrowRight' && rang < liste.length - 1) ouvrir(rang + 1);
  if (e.key === 'ArrowLeft' && rang > 0) ouvrir(rang - 1);
  if (e.key === 'Tab') {  // le focus reste dans la fiche
    const f = [...carte.querySelectorAll('button:not([disabled])')];
    if (!f.length) return;
    if (e.shiftKey && document.activeElement === f[0]) { e.preventDefault(); f[f.length - 1].focus(); }
    else if (!e.shiftKey && document.activeElement === f[f.length - 1]) { e.preventDefault(); f[0].focus(); }
  }
});

// Démarrage : la langue de l'adresse, sinon celle déjà choisie, sinon le choix.
const q = new URLSearchParams(location.search);
const choisie = q.get('langue') || lireLangue();
window.__resto = {D, ctx: () => CTX, etat: () => ({langue, planche: q.get('planche'), liste: liste.map(m => m.id), rang, ouverte: !fiche.hidden,
  serie: S && {k: S.k, n: S.n, total: S.items.length, premier: S.premier, graves: S.graves, fini: S.fini,
               bonne: S.items[S.n] && S.items[S.n].bonne, item: S.items[S.n]}}), bruit: Bruit};
if (!choisie || (choisie !== 'fr' && !D.langues.some(l => l.c === choisie))) { ecranLangue(); return; }
langue = choisie === 'fr' ? null : choisie;
if (q.get('planche')) {
  planche(q.get('planche'));
  const i = liste.findIndex(m => m.id === q.get('mot'));
  if (i >= 0) ouvrir(i);
} else if (q.get('ex')) lancer(q.get('ex'));
else if (q.get('ecran') === 'exercices') exercices();
else if (q.get('ecran') === 'test') test();
else if (q.get('ecran') === 'service') { if (q.get('sit') && codeAcces) scene(q.get('sit')); else service(); }
else if (q.get('ecran') === 'planches') planches();
else accueil();
})();
</script>
</body>
</html>
"""
GABARIT = GABARIT.replace("%%NOM_JS%%", json.dumps(IDE.NOM, ensure_ascii=False))

if __name__ == "__main__":
    main()
