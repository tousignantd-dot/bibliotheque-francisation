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
import html, json, pathlib, sys

RACINE = pathlib.Path(__file__).resolve().parent.parent
CONTENU = RACINE / "build" / "contenu" / "entreprise-francoeur"
sys.path.insert(0, str(CONTENU))
sys.path.insert(0, str(RACINE / "build"))
from lexique import LEXIQUE, PLANCHES, verifier  # noqa: E402
from francoeur_etape0 import TEINTES, MOTIFS  # noqa: E402
from demandes import DEMANDES, COULEURS_DISTRACTRICES, TAILLES  # noqa: E402
import random  # noqa: E402
import test as TEST  # noqa: E402
import clients as CLI  # noqa: E402

CROQUIS = RACINE / "assets" / "interactive" / "francoeur" / "croquis"
SONS = RACINE / "assets" / "interactive" / "francoeur" / "sons"
SORTIE = RACINE / "modules-autonomes" / "francoeur-planches" / "index.html"

# Incrémenter après toute image ou tout son refait : même nom, même adresse,
# le navigateur servirait l'ancien sans rien dire.
MEDIA_V = "3"   # 3 : lin, polyester, rose refaits à l’oreille, 24 septembre 2026


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
        mots.append(m)
    langues = [{"c": c, "loc": v["loc"], "rtl": v["rtl"], "relu": v["relu"],
                "ui": v.get("interface", {}),
                "mots": {k: [t["mot"], t["note"]] for k, t in v["mots"].items()}}
               for c, v in trad.items()]
    return {"planches": [{"k": k, "t": t} for k, t in PLANCHES], "mots": mots,
            "langues": langues, "demandes": demandes(mots), "test": le_test(mots),
            "magasin": le_magasin()}


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


ETIQUETTE = {"tp": "TP", "p": "P", "m": "M", "g": "G", "tg": "TG"}


def demandes(mots):
    """Les quatre variantes de chaque demande, DÉDUITES et non écrites : chaque
    distracteur ne diffère de la bonne réponse que par UN attribut. Tirage semé
    sur l'id, pour que deux constructions rendent la même page."""
    par_id = {m["id"]: m for m in mots}
    planche = {e[0]: e[1] for e in LEXIQUE}
    sortie = []
    for ident, _voix, phrase, art, coul, taille in DEMANDES:
        assert art in par_id and "img" in par_id[art], f"{ident} : {art} sans croquis"
        assert coul in TEINTES, f"{ident} : couleur {coul} inconnue"
        v = variantes(ident, art, coul, taille, par_id, planche)
        sortie.append({"id": ident, "phrase": phrase,
                       "son": f"/assets/interactive/francoeur/sons/demandes/{ident}.mp3?v={MEDIA_V}",
                       "v": cartes(v, par_id)})
    return sortie


def variantes(graine, art, coul, taille, par_id, planche, article_seul=False):
    """La bonne réponse d'abord, puis trois distracteurs qui ne changent chacun
    qu'UN attribut. `article_seul` : les trois changent l'article (cran 1 du
    test, où la phrase ne dit ni couleur ni taille)."""
    r = random.Random(graine)
    voisins = [e[0] for e in LEXIQUE if e[1] == planche[art] and e[0] != art
               and "img" in par_id[e[0]]]
    v = [(art, coul, taille)]
    if article_seul:
        return v + [(a, coul, taille) for a in r.sample(voisins, 3)]
    autres_c = [c for c in COULEURS_DISTRACTRICES if c != coul]
    v.append((art, r.choice(autres_c), taille))                     # la couleur change
    if taille:
        i = TAILLES.index(taille)
        proches = [TAILLES[j] for j in (i - 1, i + 1) if 0 <= j < len(TAILLES)]
        v.append((art, coul, r.choice(proches)))                    # la taille change
    else:
        v.append((art, r.choice([c for c in autres_c if c != v[1][1]]), None))
    v.append((r.choice(voisins), coul, taille))                     # l'article change
    return v


def cartes(v, par_id):
    return [{"a": a, "img": par_id[a]["img"], "mot": par_id[a]["mot"], "c": c,
             "cmot": par_id[c]["mot"], "hex": TEINTES[c],
             "t": ETIQUETTE.get(t) if t else None} for a, c, t in v]


def le_test(mots):
    """Les items du test, par partie et par cran. Distracteurs déduits aux crans
    1-2, écrits au cran 3 (voir build/contenu/entreprise-francoeur/test.py)."""
    par_id = {m["id"]: m for m in mots}
    planche = {e[0]: e[1] for e in LEXIQUE}
    avec_img = [m["id"] for m in mots if "img" in m]
    son = lambda i: f"/assets/interactive/francoeur/sons/test/{i}.mp3?v={MEDIA_V}"
    for i in TEST.A_CRAN1 + TEST.A_CRAN2 + [x for x, _ in TEST.A_CRAN3]:
        assert i in par_id and "img" in par_id[i] and "son" in par_id[i], f"A : {i}"
    A = {1: [], 2: [], 3: []}
    for cible in TEST.A_CRAN1:
        r = random.Random("A1" + cible)
        A[1].append({"id": cible, "son": par_id[cible]["son"],
                     "o": [cible] + r.sample([i for i in avec_img if planche[i] != planche[cible]], 3)})
    for cible in TEST.A_CRAN2:
        r = random.Random("A2" + cible)
        A[2].append({"id": cible, "son": par_id[cible]["son"],
                     "o": [cible] + r.sample([i for i in avec_img if planche[i] == planche[cible] and i != cible], 3)})
    for cible, pieges in TEST.A_CRAN3:
        A[3].append({"id": cible, "son": par_id[cible]["son"], "o": [cible] + pieges})
    B = {1: [], 2: [], 3: []}
    for ident, cran, _v, phrase, bonne, distr in TEST.B:
        v = [bonne] + distr if distr else variantes(ident, *bonne, par_id, planche, article_seul=(cran == 1))
        B[cran].append({"id": ident, "son": son(ident), "phrase": phrase, "v": cartes(v, par_id)})
    C = {1: [], 2: [], 3: []}
    for ident, cran, phrase, question, bonne, distr in TEST.C:
        for i in [bonne] + distr:
            assert "img" in par_id[i], f"C {ident} : {i} sans croquis"
        C[cran].append({"id": ident, "son": son(ident), "phrase": phrase, "q": question,
                        "o": [bonne] + distr})
    return {"A": A, "B": B, "C": C,
            "D": [{"id": i, "son": son(i), "phrase": p} for i, _v, p in TEST.D],
            "oral": TEST.ORAL, "paliers": [{"k": k, "t": t, "n": n} for k, t, n in TEST.PALIERS],
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
:root{--mf-teinte:var(--acier-600);--mf-fond:var(--acier-100)}
body{margin:0;background:var(--surface-page);color:var(--text-body);font-family:Nunito,system-ui,sans-serif}
.mf{max-width:1080px;margin:0 auto;padding:18px 16px 60px}
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
.carte .gestes{display:flex;flex-wrap:wrap;gap:8px;margin:14px 0 6px}
.carte .trad{margin-top:8px;padding:12px 14px;border-radius:12px;background:var(--mf-fond);font-size:22px;font-weight:800;color:var(--text-strong)}
.carte .trad[hidden]{display:none}
.carte .trad small{display:block;font-size:15px;font-weight:600;color:var(--text-body);margin-top:6px}
.carte .trad .relu{display:block;font-size:12px;font-weight:600;color:var(--text-muted);margin-top:8px}
.carte .piege{margin-top:10px;padding:10px 12px;border-radius:10px;background:var(--warn-bg);border:1px solid var(--warn-line);
  color:var(--warn-ink);font-size:15px;font-weight:700}
.carte .nav{display:flex;justify-content:space-between;gap:8px;margin-top:14px}
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
.filtre select{font:inherit;font-size:16px;padding:8px 10px;border-radius:10px;border:1px solid var(--line-300);background:var(--surface-card);color:var(--text-strong)}
.jeu{margin-top:12px}
.jeu .barre{height:6px;border-radius:3px;background:var(--line-200);overflow:hidden;margin-bottom:12px}
.jeu .barre i{display:block;height:100%;background:var(--accent)}
.jeu .consigne{font-weight:700;margin:0 0 10px}
.jeu .sujet{background:#fff;border-radius:14px;border:1px solid var(--line-200);display:grid;place-items:center;padding:8px;max-width:320px;margin:0 auto 12px}
.jeu .sujet img{width:100%;max-width:260px;aspect-ratio:1/1;object-fit:contain}
.jeu .sujet .past{width:100%;aspect-ratio:3/2;border-radius:10px}
.jeu .ecoute{display:flex;gap:8px;justify-content:center;flex-wrap:wrap;margin:6px 0 14px}
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
.code{display:flex;gap:8px;flex-wrap:wrap;align-items:center;margin-top:12px}
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
@media (max-width:760px){.scene{grid-template-columns:1fr}.avatar{position:static;max-width:260px;margin:0 auto}}
@media (max-width:640px){.clients{grid-template-columns:repeat(2,minmax(0,1fr))}.client b{font-size:15px}.client span{font-size:13px}}

/* Le test */
.intro{max-width:620px}
.intro p{margin:0 0 10px}
.partie{font-size:13px;font-weight:800;letter-spacing:.06em;text-transform:uppercase;color:var(--mf-teinte);margin:0 0 4px}
.question{font-size:19px;font-weight:800;color:var(--text-strong);margin:4px 0 12px;text-align:center}
.oral{display:flex;flex-direction:column;align-items:center;gap:10px;margin:10px 0}
.oral .etat{font-weight:700;min-height:1.4em}
.rec{background:var(--audio);border-color:var(--audio);color:#fff}
.resultat{display:grid;gap:14px;margin-top:14px}
.bloc{background:var(--surface-card);border:1px solid var(--line-200);border-radius:14px;padding:16px}
.gros-palier{font-size:34px;font-weight:900;color:var(--text-strong);margin:4px 0}
.parts{display:grid;gap:8px;margin-top:8px}
.parts div{display:grid;grid-template-columns:1fr auto;gap:10px;align-items:center}
.jauge{grid-column:1/-1;height:8px;border-radius:4px;background:var(--line-200);overflow:hidden}
.jauge i{display:block;height:100%;background:var(--mf-teinte)}
.choisir3{display:flex;flex-wrap:wrap;gap:8px;margin-top:8px}
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
  pour_formateur:"Pour le formateur", confirmer_palier:"Confirmer le niveau du jeu de rôle",
  refaire_test:"Refaire le test",
  magasin:"Le magasin", magasin_sous:"Des clients vous parlent. Vous répondez.",
  code_acces:"Votre code d'accès", code_aide:"Le code vous est donné par votre formateur.",
  entrer:"Entrer", niveau_jeu:"Niveau des clients", faire_test:"Faites d'abord le test « Mon niveau », ou choisissez :",
  choisir_client:"Choisissez un client.", ecouter_sans_lire:"Écouter sans lire",
  lire:"Lire", parler:"Parler", envoyer:"Envoyer", ecrire:"Ou écrivez votre réponse…",
  fini:"J'ai fini", attente_client:"Le client réfléchit…", vous:"Vous",
  bilan_titre:"Le bilan", client_part:"Le client est parti", vos_phrases:"Vos phrases, corrigées",
  gestes_titre:"Les gestes du vendeur — lesquels avez-vous faits ?", autre_client:"Un autre client",
  code_refuse:"Ce code n'est pas reconnu.", voix_indispo:"La voix n'est pas disponible pour le moment. Lisez la réplique.", erreur_reseau:"Impossible de joindre le serveur."};
const T = k => dit(k, FR[k]);
const app = document.getElementById('app');
let audio = null;
function joue(src) { if (!src) return; if (audio) audio.pause(); audio = new Audio(src); audio.play().catch(()=>{}); }

function image(m, grand) {
  if (m.img) return '<img src="' + m.img + '" alt="' + esc(m.mot) + '"' + (grand ? '' : ' loading="lazy"') + '>';
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

function ecranAccueil() {
  app.innerHTML = tete('Bienvenue', '', false)
    + '<div class="accueil">'
    + '<button type="button" class="porte" id="aRayons"><b>' + T('apprendre') + '</b><span>' + T('apprendre_sous') + '</span></button>'
    + '<button type="button" class="porte" id="aExos"><b>' + T('exercer') + '</b><span>' + T('exercer_sous') + '</span></button>'
    + '<button type="button" class="porte" id="aTest"><b>' + T('test') + '</b><span>' + T('test_sous') + '</span></button>'
    + '<button type="button" class="porte" id="aMag"><b>' + T('magasin') + '</b><span>' + T('magasin_sous') + '</span></button></div>';
  document.getElementById('aRayons').onclick = ecranRayons;
  document.getElementById('aExos').onclick = ecranExercices;
  document.getElementById('aTest').onclick = ecranTest;
  document.getElementById('aMag').onclick = ecranMagasin;
  document.getElementById('chLangue').onclick = ecranLangue;
  window.scrollTo(0, 0);
}


function tete(titre, sous, retour, cleRetour) {
  return '<div class="mf-tete"><div><p class="mf-enseigne">Maison Francœur</p><h1>' + titre + '</h1>'
    + (sous ? '<p style="margin:6px 0 0">' + sous + '</p>' : '') + '</div><div style="display:flex;gap:8px;flex-wrap:wrap">'
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
    + (m.autre ? '<p class="autre">' + esc(FR.aussi) + ' : <b>' + esc(m.autre) + '</b></p>' : '')
    + '<div class="gestes">'
    + (m.son ? '<button type="button" class="mf-btn mf-btn--pri" id="ecoute">' + ICO.son + '<span>' + T('ecouter') + '</span></button>' : '')
    + (t ? '<button type="button" class="mf-btn" id="voir" aria-expanded="false">' + ICO.oeil + '<span>' + T('voir') + '</span></button>' : '')
    + '</div>'
    + (t ? '<div class="trad" id="trad" hidden lang="' + l.c + '" dir="' + (l.rtl ? 'rtl' : 'ltr') + '">' + esc(t[0])
        + (t[1] ? '<small>' + esc(t[1]) + '</small>' : '')
        + (l.relu ? '' : '<span class="relu" dir="ltr" lang="fr">' + esc(FR.non_relu) + (l.ui.non_relu ? ' · <span dir="' + (l.rtl ? 'rtl' : 'ltr') + '">' + esc(l.ui.non_relu) + '</span>' : '') + '</span>')
        + '</div>' : '')
    + (m.piege && !(t && t[1]) ? '<p class="piege">' + esc(m.note.replace(/^PIÈGE\s*:\s*/, '')) + '</p>' : '')
    + '<div class="nav"><button type="button" class="mf-btn" id="prec"' + (i ? '' : ' disabled') + '>' + ICO.retour + FR.precedent + '</button>'
    + '<button type="button" class="mf-btn" id="suiv"' + (i < courante.length - 1 ? '' : ' disabled') + '>' + FR.suivant + ICO.suiv + '</button></div>';
  fiche.hidden = false;
  document.getElementById('ferme').onclick = fermer;
  const e = document.getElementById('ecoute'); if (e) e.onclick = () => joue(m.son);
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
   Cinq, du mot isolé à la phrase du client. Une série = 8 questions.
   Deux essais, puis la bonne réponse se montre (règle du dépôt : jamais la
   réponse au premier envoi). Les mots ratés vont dans « à revoir » et
   repassent devant à la série suivante. Tout reste sur l'appareil. */
const EXOS = [
  {k:'ecoute', n:1}, {k:'image', n:2}, {k:'rappel', n:3}, {k:'rayon', n:4}, {k:'client', n:5, pont:true}];
const RAYONS = ['hauts','bas','robes','exterieur','dessous','chaussures','accessoires'];
const SERIE = 8;
const CLE_REVOIR = 'francoeur-revoir';
let revoir = new Set();
try { revoir = new Set(JSON.parse(localStorage.getItem(CLE_REVOIR) || '[]')); } catch(e) {}
const garderRevoir = () => { try { localStorage.setItem(CLE_REVOIR, JSON.stringify([...revoir])); } catch(e) {} };
let filtre = '';
const melange = a => { a = a.slice(); for (let i = a.length - 1; i > 0; i--) { const j = Math.floor(Math.random() * (i + 1)); [a[i], a[j]] = [a[j], a[i]]; } return a; };
const visuel = m => m.img || m.pastille;
function tirage(pool) {
  // Les mots « à revoir » d'abord, puis le reste au hasard.
  const a = melange(pool.filter(m => revoir.has(m.id))), b = melange(pool.filter(m => !revoir.has(m.id)));
  return a.concat(b).slice(0, SERIE);
}

function ecranExercices() {
  app.innerHTML = tete(T('exercices'), '', true, 'accueil')
    + '<div class="filtre"><select id="filtre" aria-label="' + esc(FR.tous_rayons) + '"><option value="">' + esc(FR.tous_rayons) + '</option>'
    + D.planches.filter(p => RAYONS.includes(p.k) || p.k === 'couleurs').map(p => '<option value="' + p.k + '"' + (filtre === p.k ? ' selected' : '') + '>' + esc(p.t) + '</option>').join('')
    + '</select></div><div class="exos">'
    + EXOS.map(x => '<button type="button" class="exo-porte' + (x.pont ? ' pont' : '') + '" data-x="' + x.k + '"><span class="rang">' + x.n + '</span><span><b>'
      + T('ex_' + x.k) + '</b><span style="display:block;margin-top:4px">' + T('ex_' + x.k + '_c') + '</span></span></button>').join('') + '</div>';
  document.getElementById('filtre').onchange = e => { filtre = e.target.value; };
  app.querySelectorAll('[data-x]').forEach(b => b.onclick = () => lancer(b.dataset.x));
  document.getElementById('retour').onclick = ecranAccueil;
  document.getElementById('chLangue').onclick = ecranLangue;
  window.scrollTo(0, 0);
}

let J = null;   // la série en cours
function lancer(k) {
  const dansFiltre = m => !filtre || m.p === filtre;
  let items;
  if (k === 'client') items = melange(D.demandes).slice(0, SERIE);
  else if (k === 'rayon') items = tirage(D.mots.filter(m => m.img && RAYONS.includes(m.p) && dansFiltre(m)));
  else items = tirage(D.mots.filter(m => visuel(m) && m.son && dansFiltre(m)));
  J = {k, items, i: 0, essais: 0, premier: 0, fini: false};
  question();
}

function cadreJeu(corps) {
  app.innerHTML = tete(T('ex_' + J.k), T('ex_' + J.k + '_c'), true, 'exercices')
    + '<div class="jeu"><div class="barre"><i style="width:' + Math.round(100 * J.i / J.items.length) + '%"></i></div>' + corps
    + '<p class="retro" id="retro" aria-live="polite"></p><div class="suite" id="suite"></div></div>';
  document.getElementById('retour').onclick = () => { if (audio) audio.pause(); ecranExercices(); };
  document.getElementById('chLangue').onclick = ecranLangue;
}
const boutonsEcoute = () => '<div class="ecoute"><button type="button" class="mf-btn mf-btn--pri" id="reec">' + ICO.son + '<span>' + T('reecouter') + '</span></button>'
  + '<button type="button" class="mf-btn" id="lent"><span>' + T('lentement') + '</span></button></div>';
function brancherEcoute(src) {
  document.getElementById('reec').onclick = () => joue(src);
  document.getElementById('lent').onclick = () => { joue(src); if (audio) { audio.preservesPitch = true; audio.playbackRate = 0.75; } };
}

function question() {
  if (J.i >= J.items.length) return bilan();
  J.essais = 0;
  const it = J.items[J.i];
  if (J.k === 'ecoute') {
    const autres = melange(D.mots.filter(m => m.p === it.p && m.id !== it.id && visuel(m))).slice(0, 5);
    J.bonne = it.id; J.options = melange([it].concat(autres));
    cadreJeu(boutonsEcoute() + '<div class="choix">' + J.options.map(m => '<button type="button" class="opt" data-o="' + m.id + '">' + image(m) + '</button>').join('') + '</div>');
    brancherEcoute(it.son); joue(it.son);
  } else if (J.k === 'image') {
    const autres = melange(D.mots.filter(m => m.p === it.p && m.id !== it.id)).slice(0, 2);
    J.bonne = it.id; J.options = melange([it].concat(autres));
    cadreJeu('<div class="sujet">' + image(it, true) + '</div><div class="choix mots">'
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
    cadreJeu('<div class="sujet">' + image(it, true) + '</div><div class="revele" id="revele"><button type="button" class="mf-btn mf-btn--pri" id="voirMot">' + ICO.oeil + '<span>' + T('voir_mot') + '</span></button></div>');
    document.getElementById('voirMot').onclick = () => {
      joue(it.son);
      document.getElementById('revele').innerHTML = '<p class="gros">' + esc(it.mot) + '</p>'
        + '<div class="ecoute"><button type="button" class="mf-btn mf-btn--pri" id="savais"><span>' + T('savais') + '</span></button>'
        + '<button type="button" class="mf-btn" id="arevoir"><span>' + T('a_revoir') + '</span></button></div>';
      const auto = ok => rapporter({zone: 'ex-rappel-' + it.id, exo: 'ex-rappel', exoNum: 'Exercice 3', exoTitre: FR.ex_rappel,
        section: 'exercices', type: 'rappel', enonce: it.mot, bonne: '', reponse: '', ok, essais: 1});
      document.getElementById('savais').onclick = () => { auto(true); J.premier++; revoir.delete(it.id); garderRevoir(); J.i++; question(); };
      document.getElementById('arevoir').onclick = () => { auto(false); revoir.add(it.id); garderRevoir(); J.i++; question(); };
    };
    return;
  } else if (J.k === 'client') {
    J.bonne = 0; J.options = melange(it.v.map((v, n) => Object.assign({n}, v)));
    cadreJeu(boutonsEcoute() + '<div class="choix">' + J.options.map(v =>
      '<button type="button" class="opt gris" data-o="' + v.n + '"><img src="' + v.img + '" alt="' + esc(v.mot) + '" loading="lazy">'
      + '<span class="attrs"><span class="chip" style="background:' + v.hex + '" role="img" aria-label="' + esc(v.cmot) + '"></span>'
      + (v.t ? '<span class="tag">' + v.t + '</span>' : '') + '</span></button>').join('') + '</div>');
    brancherEcoute(it.son); joue(it.son);
  }
  app.querySelectorAll('[data-o]').forEach(b => b.onclick = () => repondre(b));
}

function repondre(b) {
  const it = J.items[J.i], retro = document.getElementById('retro');
  const juste = String(b.dataset.o) === String(J.bonne);
  const idMot = J.k === 'client' ? null : it.id;
  if (juste) {
    b.classList.add('juste');
    if (J.essais === 0) { J.premier++; if (idMot) { revoir.delete(idMot); garderRevoir(); } }
    retro.className = 'retro ok'; retro.innerHTML = T('bravo');
    if (J.k !== 'ecoute' && J.k !== 'client') joue(it.son);
    finQuestion();
  } else {
    J.essais++; b.classList.add('faux'); b.disabled = true;
    if (idMot) { revoir.add(idMot); garderRevoir(); }
    if (J.essais >= 2) {
      const bon = app.querySelector('[data-o="' + J.bonne + '"]'); if (bon) bon.classList.add('juste');
      retro.className = 'retro non'; retro.innerHTML = T('reponse');
      if (J.k === 'client') retro.innerHTML += '<span class="appui" style="font-style:italic" lang="fr">« ' + esc(it.phrase) + ' »</span>';
      else joue(it.son);
      finQuestion();
    } else { retro.className = 'retro non'; retro.innerHTML = T('essaie'); }
  }
}
function finQuestion() {
  const it = J.items[J.i], juste = !!app.querySelector('.opt.juste:not(.faux)') && J.essais < 2;
  const fautif = app.querySelector('.opt.faux');
  const libelle = o => J.k === 'client' ? carteTexte(J.options.find(v => String(v.n) === String(o)))
    : J.k === 'rayon' ? (D.planches.find(p => p.k === o) || {}).t : etiquette(o);
  rapporter({zone: 'ex-' + J.k + '-' + it.id, exo: 'ex-' + J.k, exoNum: 'Exercice ' + (EXOS.find(x => x.k === J.k).n),
    exoTitre: FR['ex_' + J.k], section: 'exercices', type: J.k,
    enonce: J.k === 'client' ? it.phrase : it.mot, bonne: libelle(J.bonne),
    reponse: juste ? libelle(J.bonne) : (fautif ? libelle(fautif.dataset.o) : ''), ok: juste, essais: J.essais + 1});
  app.querySelectorAll('[data-o]').forEach(x => x.disabled = true);
  const s = document.getElementById('suite');
  s.innerHTML = '<button type="button" class="mf-btn mf-btn--pri" id="apres"><span>' + T('suivant') + '</span>' + ICO.suiv + '</button>';
  const a = document.getElementById('apres'); a.onclick = () => { J.i++; question(); }; a.focus();
}
function bilan() {
  J.fini = true;
  rapporterSerie(J.items.length, J.premier);
  app.innerHTML = tete(T('ex_' + J.k), '', true, 'exercices')
    + '<div class="bilan"><p style="font-weight:800;margin:0">' + T('fin') + '</p><p class="score">' + J.premier + ' / ' + J.items.length + '</p>'
    + '<p style="margin:0 0 16px">' + T('premier_coup') + '</p>'
    + '<button type="button" class="mf-btn mf-btn--pri" id="encore"><span>' + T('recommencer') + '</span></button></div>';
  document.getElementById('encore').onclick = () => lancer(J.k);
  document.getElementById('retour').onclick = ecranExercices;
  document.getElementById('chLangue').onclick = ecranLangue;
}
window.__francoeur = { etat: () => J, D };
/* ── Le test de positionnement (étape 3) ───────────────────────────────
   A (mots), B (client), C (gérante) : adaptatif. À un cran, 3 bonnes le
   valident et font monter ; 2 erreurs arrêtent la partie. Aucune rétroaction.
   D (oral) : enregistré sur l'appareil, jamais envoyé, noté par le formateur.
   Le palier se PROPOSE ; le formateur le confirme. Historique sur l'appareil. */
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
    + (der ? '<p class="bloc">' + esc(FR.derniere) + ' : <b>' + esc(nomPalier(der.confirme || der.palier).t) + '</b> · ' + der.date + '</p>' : '')
    + '<button type="button" class="mf-btn mf-btn--pri" id="go"><span>' + T('commencer') + '</span>' + ICO.suiv + '</button></div>';
  document.getElementById('go').onclick = debuterTest;
  document.getElementById('retour').onclick = ecranAccueil;
  document.getElementById('chLangue').onclick = ecranLangue;
  window.scrollTo(0, 0);
}
function debuterTest() {
  X = {parties: ['A', 'B', 'C'], p: 0, cran: 1, bons: 0, faux: 0, niveau: {A: 0, B: 0, C: 0},
       vus: new Set(), reponses: [], oral: [], blobs: [], fini: false};
  questionTest();
}
function itemSuivant() {
  const P = X.parties[X.p], pool = D.test[P][X.cran].filter(it => !X.vus.has(it.id));
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
    corps = ecoute + '<div class="choix">' + X.options.map(id => { const m = D.mots.find(x => x.id === id);
      return '<button type="button" class="opt" data-o="' + id + '">' + image(m) + '</button>'; }).join('') + '</div>';
  } else if (P === 'B') {
    X.options = melange(it.v.map((v, n) => Object.assign({n}, v))); X.bonne = 0;
    corps = ecoute + '<div class="choix">' + X.options.map(v => '<button type="button" class="opt gris" data-o="' + v.n + '"><img src="' + v.img + '" alt="' + esc(v.mot) + '">'
      + '<span class="attrs"><span class="chip" style="background:' + v.hex + '" role="img" aria-label="' + esc(v.cmot) + '"></span>'
      + (v.t ? '<span class="tag">' + v.t + '</span>' : '') + '</span></button>').join('') + '</div>';
  } else {
    X.options = melange(it.o); X.bonne = it.o[0];
    corps = ecoute + '<p class="question">' + dit('tq_' + it.id, it.q) + '</p><div class="choix">' + X.options.map(id => { const m = D.mots.find(x => x.id === id);
      return '<button type="button" class="opt" data-o="' + id + '">' + image(m) + '<span style="font-weight:800">' + esc(m.mot) + '</span></button>'; }).join('') + '</div>';
  }
  app.innerHTML = tete(T('test'), T('c' + P.toLowerCase()), false)
    + '<div class="jeu">' + titre + corps + '</div>';
  document.getElementById('chLangue').remove();
  document.getElementById('reec').onclick = () => joue(it.son);
  joue(it.son);
  app.querySelectorAll('[data-o]').forEach(b => b.onclick = () => repondreTest(String(b.dataset.o) === String(X.bonne)));
  window.scrollTo(0, 0);
}
function repondreTest(juste) {
  // Aucune rétroaction : on passe à la suite, c'est tout.
  if (audio) audio.pause();
  X.reponses.push({p: X.parties[X.p], cran: X.cran, id: X.item.id, juste});
  { const P = X.parties[X.p], it = X.item;
    rapporter({zone: 'test-' + P + '-' + it.id, exo: 'test-' + P, exoNum: 'Test · cran ' + X.cran,
      exoTitre: FR['partie_' + P.toLowerCase()], section: 'test', type: 'test',
      enonce: P === 'A' ? etiquette(it.id) : P === 'B' ? it.phrase : it.phrase + ' — ' + it.q,
      bonne: P === 'B' ? carteTexte(it.v[0]) : etiquette(P === 'A' ? it.id : it.o[0]), reponse: '', ok: juste, essais: 1}); }
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
  if (i >= D.test.D.length) return resultatTest();
  const it = D.test.D[i];
  app.innerHTML = tete(T('test'), T('cd'), false)
    + '<div class="jeu"><p class="partie">' + esc(FR.partie_d) + ' · ' + (i + 1) + ' / ' + D.test.D.length + '</p>'
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
  const n = X.niveau, pal = calculPalier(n.A, n.B, n.C);
  const h = histo();
  const entree = {date: new Date().toISOString().slice(0, 10), a: n.A, b: n.B, c: n.C, palier: pal, confirme: null, oral: [null, null]};
  h.push(entree); garderHisto(h);
  const premiere = h.length > 1 ? h[0] : null;
  const jauge = (k, v) => '<div><span>' + esc(FR['partie_' + k]) + '</span><b>' + v + ' / 3</b><span class="jauge"><i style="width:' + Math.round(v / 3 * 100) + '%"></i></span></div>';
  app.innerHTML = tete(T('resultat'), '', true, 'accueil')
    + '<div class="resultat"><div class="bloc"><p style="margin:0">' + T('palier_propose') + '</p>'
    + '<p class="gros-palier">' + esc(nomPalier(pal).t) + '</p><p style="margin:0;color:var(--text-muted)">' + esc(nomPalier(pal).n) + ' · ' + T('pas_examen') + '</p>'
    + '<div class="parts">' + jauge('a', n.A) + jauge('b', n.B) + jauge('c', n.C) + '</div></div>'
    + (premiere ? '<div class="bloc"><b>' + esc(FR.premiere) + '</b> (' + premiere.date + ') : ' + esc(nomPalier(premiere.confirme || premiere.palier).t)
        + ' — A ' + premiere.a + ' · B ' + premiere.b + ' · C ' + premiere.c + '<br><b>' + esc(FR.aujourdhui) + '</b> : ' + esc(nomPalier(pal).t)
        + ' — A ' + n.A + ' · B ' + n.B + ' · C ' + n.C + '</div>' : '')
    + '<div class="bloc formateur"><b>' + esc(FR.pour_formateur) + '</b>'
    + D.test.D.map((d, i) => '<p style="margin:12px 0 4px">« ' + esc(d.phrase) + ' »</p>'
        + (X.blobs[i] ? '<audio controls src="' + X.blobs[i] + '"></audio>' : '<p style="margin:0;color:var(--text-muted)">—</p>')
        + '<div class="choisir3" data-oral="' + i + '">' + D.test.oral.map((o, k) => '<button type="button" class="mf-btn" data-v="' + k + '" aria-pressed="false">' + esc(o) + '</button>').join('') + '</div>').join('')
    + '<p style="margin:16px 0 4px">' + esc(FR.confirmer_palier) + '</p><div class="choisir3" data-conf="1">'
    + D.test.paliers.map(p => '<button type="button" class="mf-btn" data-v="' + p.k + '" aria-pressed="false">' + esc(p.t) + '</button>').join('') + '</div></div>'
    + '<div><button type="button" class="mf-btn" id="refaire"><span>' + T('refaire_test') + '</span></button></div></div>';
  const maj = () => { const hh = histo(); hh[hh.length - 1] = entree; garderHisto(hh); };
  app.querySelectorAll('[data-oral] button').forEach(b => b.onclick = () => {
    const i = +b.parentNode.dataset.oral; entree.oral[i] = +b.dataset.v; maj();
    b.parentNode.querySelectorAll('button').forEach(x => x.setAttribute('aria-pressed', String(x === b))); });
  app.querySelectorAll('[data-conf] button').forEach(b => b.onclick = () => {
    entree.confirme = b.dataset.v; maj();
    b.parentNode.querySelectorAll('button').forEach(x => x.setAttribute('aria-pressed', String(x === b))); });
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
    const dispo = M.clients.filter(c => !niveauJeu || c.paliers.includes(niveauJeu));
    app.innerHTML = tete(T('magasin'), T('choisir_client'), true, 'accueil')
      + '<p style="margin:10px 0 4px"><b>' + T('niveau_jeu') + '</b>' + (niveauJeu ? '' : ' — ' + T('faire_test')) + '</p>'
      + '<div class="choisir3" id="niv">' + D.test.paliers.map(p => '<button type="button" class="mf-btn" data-v="' + p.k + '" aria-pressed="' + (p.k === niveauJeu) + '">' + esc(p.t) + '</button>').join('') + '</div>'
      + '<div class="clients">' + dispo.map(c => '<button type="button" class="client" data-c="' + c.id + '"><img src="' + c.p.neutre + '" alt=""><b>' + esc(c.nom) + '</b><span>' + esc(c.carte) + '</span></button>').join('') + '</div>';
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
  S = {c, hist: [], humeur: 'neutre', fini: false, sansLire: false};
  app.innerHTML = tete(esc(c.nom), esc(c.carte), true, 'magasin')
    + '<div class="scene"><div class="avatar"><img id="av" src="' + c.p.neutre + '" alt="' + esc(c.nom) + '"><p class="nom" id="hum"></p></div>'
    + '<div><div class="choisir3"><button type="button" class="mf-btn" id="sansLire" aria-pressed="false"><span>' + T('ecouter_sans_lire') + '</span></button></div>'
    + '<div class="fil" id="fil" aria-live="polite"></div>'
    + '<div class="saisie"><button type="button" class="mf-btn rec" id="micro"><span>' + T('parler') + '</span></button>'
    + '<input id="txt" placeholder="' + esc(FR.ecrire) + '"><button type="button" class="mf-btn mf-btn--pri" id="env"><span>' + T('envoyer') + '</span></button></div>'
    + '<div class="suite"><button type="button" class="mf-btn" id="fin"><span>' + T('fini') + '</span></button></div>'
    + '<p class="retro non" id="err"></p></div></div>';
  document.getElementById('retour').onclick = () => { arreterTout(); ecranMagasin(); };
  document.getElementById('chLangue').remove();
  document.getElementById('sansLire').onclick = e => { S.sansLire = !S.sansLire; e.currentTarget.setAttribute('aria-pressed', String(S.sansLire)); document.getElementById('fil').classList.toggle('cache', S.sansLire); };
  document.getElementById('env').onclick = () => envoyer(document.getElementById('txt').value);
  document.getElementById('txt').onkeydown = e => { if (e.key === 'Enter') envoyer(e.target.value); };
  document.getElementById('micro').onclick = micro;
  document.getElementById('fin').onclick = bilanMagasin;
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
function montrerHumeur(h) { S.humeur = h; const av = document.getElementById('av'); if (av) av.src = S.c.p[h]; }
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
    if (fin) { S.fini = true; setTimeout(bilanMagasin, 2500); }
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
function arreterTout() { if (audio) audio.pause(); if (reco) { try { reco.abort(); } catch(e) {} reco = null; } }
function micro() {
  const R = window.SpeechRecognition || window.webkitSpeechRecognition;
  const b = document.getElementById('micro');
  if (!R) { document.getElementById('err').textContent = FR.micro_refuse; return; }
  if (reco) { reco.stop(); return; }
  if (audio) audio.pause();
  reco = new R(); reco.lang = 'fr-CA'; reco.interimResults = true; reco.continuous = false;
  let dernier = '';
  reco.onresult = e => { dernier = [...e.results].map(x => x[0].transcript).join(' '); document.getElementById('txt').value = dernier; };
  reco.onend = () => { reco = null; b.innerHTML = '<span>' + T('parler') + '</span>'; if (dernier.trim()) envoyer(dernier); };
  reco.onerror = () => { document.getElementById('err').textContent = FR.micro_refuse; };
  reco.start(); b.innerHTML = '<span>' + T('arreter') + '</span>';
}
async function bilanMagasin() {
  arreterTout();
  rapporter({zone: 'mag-' + S.c.id + '-' + niveauJeu, exo: 'magasin', exoNum: 'Magasin · ' + niveauJeu,
    exoTitre: 'Le magasin', section: 'magasin', type: 'magasin', enonce: 'Visite : ' + S.c.nom,
    bonne: '', reponse: '', ok: S.humeur === 'contente', essais: S.hist.filter(m => m.role === 'user').length});
  const mes = S.hist.filter(m => m.role === 'user').map(m => m.contenu).slice(1);   // l'accueil n'est pas de l'employé
  const partiContent = S.humeur === 'contente';
  app.innerHTML = tete(T('bilan_titre'), '', true, 'magasin')
    + '<div class="resultat"><div class="bloc" style="display:flex;gap:14px;align-items:center"><img src="' + S.c.p[S.humeur] + '" alt="" style="width:110px;border-radius:10px;background:#fff">'
    + '<p style="margin:0">' + esc(FR.client_part) + ' : <b>' + esc(S.c.nom) + '</b></p></div>'
    + '<div class="bloc"><b>' + T('vos_phrases') + '</b><div id="corr"><p class="attente">…</p></div></div>'
    + '<div class="bloc bilan-gestes"><b>' + T('gestes_titre') + '</b>'
    + M.gestes.map((g, i) => '<label><input type="checkbox"> <span>' + esc(g) + '</span></label>').join('') + '</div>'
    + '<div><button type="button" class="mf-btn mf-btn--pri" id="autre"><span>' + T('autre_client') + '</span></button></div></div>';
  document.getElementById('autre').onclick = ecranMagasin;
  document.getElementById('retour').onclick = ecranMagasin;
  document.getElementById('chLangue').onclick = ecranLangue;
  const corr = document.getElementById('corr');
  if (!mes.length) { corr.innerHTML = '<p>—</p>'; return; }
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
