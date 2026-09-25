#!/usr/bin/env python3
"""L'écran de l'employé de la réception — étape 1 : les mots et le comptoir.

    python3 build/hotel_planches.py   # → modules-autonomes/hotel-reception/index.html

Produit, jamais écrit à la main. Il lit, dans build/contenu/entreprise-hotel/ :
`lexique.py` (les mots, en trois langues), `interface.py` (les textes de
l'écran, trois fois), `comptoir.py` (les zones à toucher du grand dessin).

LES DEUX LANGUES. L'employé choisit celle qu'il PARLE et celle qu'il APPREND.
L'écran est dans la première ; les mots, leur voix et ce qu'il devra dire sont
dans la seconde. Sa langue à lui reste CACHÉE sous chaque mot tant qu'il ne la
demande pas (règle langue-appui-trois-couches).

LES PIÈGES d'une direction ne sont que ceux de SA paire de langues : un
francophone qui apprend l'anglais ne voit pas « embarazada ».

LE THÈME est celui de francis, tel quel (décision du 24 sept.) : aucune
couleur redéfinie, seulement les jetons du système de design. La marque garde
son nom ; son descripteur suit la langue apprise.

Paramètres d'adresse, pour les captures : ?parle=fr&apprend=en#comptoir
"""
import html, importlib.util, json, pathlib

RACINE = pathlib.Path(__file__).resolve().parent.parent
CONTENU = RACINE / "build" / "contenu" / "entreprise-hotel"
CROQUIS = RACINE / "assets" / "interactive" / "hotel" / "croquis"
SORTIE = RACINE / "modules-autonomes" / "hotel-reception" / "index.html"
MEDIA_V = "9"   # 9 : tour 3 de l'audit du test (es b52 refait), 25 sept. 2026


def _charger(nom):
    s = importlib.util.spec_from_file_location(f"hotel_{nom}", CONTENU / f"{nom}.py")
    m = importlib.util.module_from_spec(s); s.loader.exec_module(m)
    return m


def donnees():
    LX, IF, CP, EX, TS = (_charger("lexique"), _charger("interface"), _charger("comptoir"),
                          _charger("exercices"), _charger("test"))
    LX.verifier()
    mots = []
    for i, pl, fr, en, es, dessin, note in LX.LEXIQUE:
        paire = note[len("PIÈGE ("):note.index(")")] if note.startswith("PIÈGE (") else ""
        notes = {"fr": note} if note else {}
        notes.update(IF.PIEGES.get(i, {}))
        if paire:
            for l in paire.split("·"):
                assert l in notes, f"{i} : piège {paire} sans note en {l}"
        mots.append({"id": i, "p": pl, "fr": fr, "en": en, "es": es,
                     "img": dessin == "croquis" and (CROQUIS / f"{i}.jpg").exists(),
                     "k": dessin == "comptoir", "paire": paire, "notes": notes})
    ids = {m["id"] for m in mots}
    for z in CP.ZONES:
        assert z[0] in ids, f"zone {z[0]} absente du lexique"
    for i, par_ui in EX.PIEGES.items():
        m = next(x for x in mots if x["id"] == i)
        assert m["paire"], f"{i} : item de piège sur un mot sans piège"
        assert set(par_ui) <= set(m["paire"].split("·")), f"{i} : interface hors de la paire"
        for ui, t in par_ui.items():
            # Tour 1 (D4 bloquant) : jamais un faux ami montré sans sa phrase.
            assert len(t) == 4 and all(t), f"{i}/{ui} : phrase, fausse lecture, second distracteur et explication obligatoires"
    for i, dit, bonne, vs in EX.NOMBRES:
        for l in ("fr", "en", "es"):
            assert len(vs[l]) == 3, f"{i}/{l} : trois voisines"
            for v, code in vs[l]:
                e = EX.ERREURS_NOMBRES[code]
                assert l in e or ("fr" in e and isinstance(e["fr"], str)), f"{i}/{l} : l'erreur « {code} » n'existe pas quand on apprend {l}"
    for r in EX.REPONSES:
        reps = r["reps"]
        assert reps[0][1] is None and all(fb for _, fb, _ in reps[1:]), f"{r['id']} : la bonne d'abord, une rétroaction par mauvaise"
        for l in ("fr", "en", "es"):
            b = len(reps[0][0][l])
            assert all(abs(len(t[l]) - b) / b <= 0.2 for t, _, _ in reps[1:]), f"{r['id']}/{l} : longueurs à ±20 %"
    import unicodedata
    slug = lambda n: "".join(c for c in unicodedata.normalize("NFD", n.lower()) if (c.isalpha() and c.isascii()) or c in " -").replace(" ", "-")
    ex = {"pieges": EX.PIEGES, "noms": [[n, slug(n)] for n in EX.NOMS], "nombres": EX.NOMBRES,
          "erreurs": EX.ERREURS_NOMBRES, "lits": EX.LITS, "demandes": EX.DEMANDES, "nuits": EX.NUITS,
          "reponses": EX.REPONSES, "regle": EX.REGLE_RELAIS, "promesse": EX.PROMESSE,
          "jamais": [sorted(g) for g in EX.JAMAIS_ENSEMBLE]}
    # Le test (révisé aux tours 1 et 2 de son audit) : A adaptatif à 4 items par
    # cran, carré latin, nuits′ tantôt −1 tantôt +1 ; B entièrement TAPÉ ; C à
    # deux « personne » par forme et du contexte hors des seuls « personne ».
    lex = {m["id"] for m in mots}
    for forme in (1, 2):
        for cran in (1, 2, 3):
            assert sum(x[1] == cran for x in TS.A[forme]) == 4, f"A{forme} cran {cran} : quatre items"
        ecarts = []
        for i, cran, dit, lit, n, lit2, n2 in TS.A[forme]:
            assert lit in lex and set(dit) == {"fr", "en", "es"}, i
            if cran == 1:
                assert lit in TS.LITS_C1[forme], f"{i} : cible hors des cartes du cran 1"
            else:
                assert lit2 in TS.LITS and lit2 != lit and n2 != n and n2 >= 1, f"{i} : carré latin"
                ecarts.append(n2 - n)
        assert ecarts.count(-1) >= 3 and ecarts.count(1) >= 3, f"A{forme} : nuits′ déséquilibrées {ecarts}"
        assert all(len(x) == 3 if x[1] == "nom" else len(x) == 4 for x in TS.B[forme]), f"B{forme} : format"
        assert len(TS.C[forme]) == 6 and sum(x[3] == "personne" for x in TS.C[forme]) == 2
        assert any(x[1] and x[3] != "personne" for x in TS.C[forme]), f"C{forme} : un contexte = « personne »"
        assert len(TS.D[forme]) == 5
    assert [len(x[2]) for x in TS.B[1] if x[1] == "nom"] == [len(x[2]) for x in TS.B[2] if x[1] == "nom"], "noms nivelés"
    bx = TS.B
    test = {"A": TS.A, "B": bx, "C": TS.C, "D": TS.D, "lits": TS.LITS, "lits_c1": TS.LITS_C1,
            "sous_b": TS.SOUS_B, "choix_c": TS.CHOIX_C, "gestes": TS.GESTES, "code": TS.CODE_FORMATEUR,
            "oral_geste": TS.ORAL_GESTE, "oral_langue": TS.ORAL_LANGUE, "c_seuil": TS.C_SEUIL,
            "oral_incomp": TS.ORAL_INCOMPREHENSIBLE_MAX,
            "debutant_max": TS.DEBUTANT_MAX, "aise_min": TS.AISE_MIN, "oral_aise": TS.ORAL_AISE,
            "paliers": TS.PALIERS, "cadrage": TS.CADRAGE, "ui": TS.UI}
    return {"hotel": IF.HOTEL, "ui": {**IF.UI, **EX.UI}, "ex": ex, "test": test, "langues": IF.NOM_LANGUE, "desc": IF.DESCRIPTEUR,
            "planches": [[k, IF.PLANCHES[k]] for k, _ in LX.PLANCHES],
            "mots": mots, "zones": CP.ZONES, "v": MEDIA_V}


def main():
    d = donnees()
    page = GABARIT.replace("%%DONNEES%%", json.dumps(d, ensure_ascii=False).replace("</", "<\\/"))
    SORTIE.parent.mkdir(parents=True, exist_ok=True)
    SORTIE.write_text(page, encoding="utf-8")
    print(f"{SORTIE.relative_to(RACINE)} — {len(d['mots'])} mots, {len(d['zones'])} zones au comptoir")


GABARIT = r"""<!DOCTYPE html>
<html lang="fr">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Hôtel Rive-Claire — la réception</title>
<link rel="stylesheet" href="/assets/design-system/styles.css">
<link rel="stylesheet" href="/assets/design-system/marque-francis.css">
<link rel="icon" href="/assets/design-system/marque-francis-favicon.svg">
<style>
/* Page produite par build/hotel_planches.py — ne pas l'éditer.
   La palette RIVE-CLAIRE (Daniel, 25 septembre 2026, parmi six propositions :
   assets/presentations/hotellerie-couleurs.html) : l'eau et le sable. Sarcelle
   pour l'action et l'enseigne, corail pour la marque et les pièges, fond sable.
   On redéfinit les jetons du système de design, rien d'autre ; le vert et le
   rouge de la rétroaction restent. Contrastes mesurés ≥ 4,5:1 (le point du
   « i » ≥ 3:1). */
:root{
  --surface-page:#F3EFE6;--surface-card:#FFFFFF;--surface-sunken:#ECE6DA;
  --text-strong:#132A2C;--text-body:#132A2C;--text-muted:#4D5E5F;--text-accent:#0F5E63;
  --line-200:#DFD8C9;--line-300:#C9C0AE;
  --accent:#0F5E63;--accent-soft:#DDEDEC;
  --marque-600:#C4613A;
  --warn-bg:#F8E3D8;--warn-line:#C4613A;--warn-ink:#8A3A1C;
  --ok-bg:#E3F1E9;--ok-line:#1F7A4D;--ok-ink:#1F7A4D}
.fr-barre .fr-desc{color:var(--text-accent)}
body{margin:0;background:var(--surface-page);color:var(--text-body);font-family:Nunito,system-ui,sans-serif}
.hr{max-width:1080px;margin:0 auto;padding:18px 16px 60px}
.fr-barre .fr-barre__in{max-width:1080px;padding-left:16px;padding-right:16px}
.secteur{display:flex;flex-direction:column;align-items:flex-end;text-align:right;line-height:1.15}
.secteur small{font-size:11px;font-weight:800;letter-spacing:.08em;text-transform:uppercase;color:var(--text-muted)}
.secteur b{font-size:19px;font-weight:900;color:var(--text-accent)}
.secteur .court{display:none}
@media (max-width:480px){.secteur small{display:none}.secteur b{font-size:16px}.secteur .long{display:none}.secteur .court{display:inline}}
.enseigne{font-size:13px;font-weight:800;letter-spacing:.08em;text-transform:uppercase;color:var(--text-accent);margin:0}
.hr h1{font-size:28px;line-height:1.15;margin:4px 0 8px;color:var(--text-strong)}
.hr h2{font-size:20px;margin:26px 0 10px;color:var(--text-strong)}
.chapeau{font-size:17px;line-height:1.5;max-width:720px;margin:0 0 6px}
.btn{font:inherit;font-weight:700;font-size:15px;cursor:pointer;border-radius:10px;padding:9px 14px;min-height:44px;
  border:1px solid var(--line-300);background:var(--surface-card);color:var(--text-strong);display:inline-flex;gap:8px;align-items:center}
.btn:hover{border-color:var(--accent)}
.btn--pri{background:var(--accent);border-color:var(--accent);color:#fff}
.btn svg{width:20px;height:20px;flex:none}
.btn--son{background:var(--audio);border-color:var(--audio);color:#fff}
.barre-haut{display:flex;flex-wrap:wrap;gap:12px;align-items:center;justify-content:space-between;margin-bottom:10px}
.avis{font-size:13px;color:var(--text-muted);margin:24px 0 0}

/* Le choix des deux langues */
.choix-l{margin:18px 0 6px;font-size:13px;font-weight:800;letter-spacing:.06em;text-transform:uppercase;color:var(--text-muted)}
.langues{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:12px;max-width:620px}
.langues button{font:inherit;cursor:pointer;text-align:start;padding:14px 16px;border-radius:12px;min-height:64px;
  border:1px solid var(--line-300);background:var(--surface-card);font-size:20px;font-weight:800;color:var(--text-strong)}
.langues button small{display:block;font-size:13px;font-weight:600;color:var(--text-muted)}
.langues button[aria-pressed=true]{border-color:var(--accent);box-shadow:inset 0 0 0 2px var(--accent);background:var(--accent-soft)}
.langues button:disabled{opacity:.35;cursor:not-allowed}
@media (max-width:480px){.langues button{font-size:17px;padding:12px}}

/* L'accueil */
.carte-comptoir{display:grid;grid-template-columns:minmax(0,1.4fr) minmax(0,1fr);gap:16px;align-items:center;cursor:pointer;
  background:var(--surface-card);border:1px solid var(--line-200);border-radius:16px;padding:12px;margin-top:16px;text-align:start;font:inherit;width:100%}
.carte-comptoir:hover{border-color:var(--accent)}
.carte-comptoir img{width:100%;border-radius:10px;display:block}
.carte-comptoir b{font-size:22px;color:var(--text-strong);display:block}
.carte-comptoir span{color:var(--text-muted)}
@media (max-width:640px){.carte-comptoir{grid-template-columns:1fr}}
.planches{display:grid;grid-template-columns:repeat(auto-fill,minmax(200px,1fr));gap:12px}
.planche-c{font:inherit;cursor:pointer;text-align:start;border:1px solid var(--line-200);background:var(--surface-card);
  border-radius:14px;padding:10px;display:flex;flex-direction:column;gap:6px}
.planche-c:hover{border-color:var(--accent)}
.planche-c .vign{display:grid;grid-template-columns:repeat(3,1fr);gap:4px;background:#fff;border-radius:10px;padding:6px;min-height:40px}
.planche-c .vign img{width:100%;aspect-ratio:1/1;object-fit:contain;display:block}
.planche-c b{font-size:17px;color:var(--text-strong)}
.planche-c .n{font-size:13px;color:var(--text-muted);font-weight:600}

/* Une planche */
.grille{display:grid;grid-template-columns:repeat(auto-fill,minmax(210px,1fr));gap:12px}
.mot{background:var(--surface-card);border:1px solid var(--line-200);border-radius:14px;padding:10px;display:flex;flex-direction:column;gap:8px}
.mot.piege{border-color:var(--warn-line);box-shadow:inset 0 3px 0 var(--warn-line)}
.mot .img{width:100%;aspect-ratio:1/1;object-fit:contain;background:#fff;border-radius:10px;display:block}
.mot .appris{font-size:20px;font-weight:900;color:var(--text-strong);line-height:1.25;margin:0}
.mot .actions{display:flex;flex-wrap:wrap;gap:12px}
.mot .trad{margin:0;font-size:16px;color:var(--text-muted);font-weight:700}
.mot .note{margin:0;font-size:14px;line-height:1.45;color:var(--text-body)}
.mot.piege .note{background:var(--warn-bg);color:var(--warn-ink);border-radius:8px;padding:8px 10px;font-weight:700}
@media (max-width:480px){.grille{grid-template-columns:repeat(2,minmax(0,1fr));gap:10px}.mot .appris{font-size:17px}
  .mot .actions{flex-direction:column}
  .mot .actions .btn{padding:8px 10px;font-size:14px;width:100%;justify-content:flex-start;white-space:normal;text-align:start}}

/* Le comptoir */
.scene{position:relative;background:#fff;border-radius:14px;overflow:hidden;border:1px solid var(--line-200)}
.scene img{width:100%;display:block}
.zone{position:absolute;transform:translate(-50%,-50%);width:44px;height:44px;border-radius:50%;cursor:pointer;
  border:3px solid var(--accent);background:rgba(255,255,255,.55);font:inherit;font-weight:900;font-size:15px;color:var(--text-strong);padding:0}
.zone[aria-pressed=true]{background:var(--accent);color:#fff}
@media (max-width:640px){.zone{width:30px;height:30px;font-size:12px;border-width:2px}}
.panneau{margin-top:12px;background:var(--surface-card);border:1px solid var(--line-200);border-radius:14px;padding:14px;min-height:76px}
.panneau .appris{font-size:24px;font-weight:900;color:var(--text-strong);margin:0 0 10px}
.panneau .actions{display:flex;flex-wrap:wrap;gap:12px;align-items:center}
.panneau .trad{margin:10px 0 0;font-size:17px;color:var(--text-muted);font-weight:700}
.objets{display:flex;flex-wrap:wrap;gap:12px;margin-top:10px;padding:0;list-style:none}
.objets button{font:inherit;cursor:pointer;border:1px solid var(--line-300);background:var(--surface-card);border-radius:999px;padding:8px 12px;min-height:40px;color:var(--text-strong)}
.objets button b{margin-right:6px;color:var(--text-accent)}
.objets button[aria-pressed=true]{border-color:var(--accent);background:var(--accent-soft)}

/* Les exercices */
.exos{display:grid;grid-template-columns:repeat(auto-fill,minmax(240px,1fr));gap:12px}
.exo-c{font:inherit;cursor:pointer;text-align:start;border:1px solid var(--line-200);background:var(--surface-card);
  border-radius:14px;padding:14px;display:flex;flex-direction:column;gap:4px}
.exo-c:hover{border-color:var(--accent)}
.exo-c b{font-size:17px;color:var(--text-strong)}
.exo-c span{font-size:14px;color:var(--text-muted)}
.progres{font-size:14px;font-weight:800;color:var(--text-muted)}
.consigne{font-size:17px;margin:0 0 14px;color:var(--text-body)}
.contexte{display:inline-block;background:var(--surface-sunken);border-radius:8px;padding:6px 10px;font-weight:800;margin:0 0 10px}
.alerte{background:var(--warn-bg);color:var(--warn-ink);border:1px solid var(--warn-line);border-radius:10px;padding:10px 12px;font-weight:700;margin:0 0 12px}
.cible{font-size:26px;font-weight:900;color:var(--text-strong);margin:0 0 12px}
.cible-img{width:min(260px,70%);aspect-ratio:1/1;object-fit:contain;background:#fff;border-radius:12px;border:1px solid var(--line-200);display:block;margin:0 0 12px}
.ecoute{display:flex;flex-wrap:wrap;gap:12px;margin:0 0 16px}
.choix{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:12px;max-width:640px}
.choix.large{grid-template-columns:1fr}
.choix button{font:inherit;cursor:pointer;text-align:start;border:2px solid var(--line-300);background:var(--surface-card);
  border-radius:12px;padding:12px;min-height:56px;font-size:18px;font-weight:800;color:var(--text-strong);display:flex;flex-direction:column;gap:6px}
.choix.large button{font-size:17px;font-weight:700}
.choix button img{width:100%;aspect-ratio:1/1;object-fit:contain;background:#fff;border-radius:8px}
.choix button small{font-size:15px;font-weight:800;color:var(--text-body)}
.choix button.ok{border-color:var(--ok-line);background:var(--ok-bg)}
.choix button.ko{border-color:var(--warn-line);background:var(--warn-bg);opacity:.8}
.choix button:disabled{cursor:default}
.retour-fb{margin:14px 0 0;min-height:28px;font-size:17px;font-weight:700;max-width:640px}
.retour-fb.ok{color:var(--ok-ink)}
.retour-fb.ko{color:var(--warn-ink)}
.saisie{display:flex;flex-wrap:wrap;gap:12px;align-items:center;max-width:640px}
.saisie input{font:inherit;font-size:22px;font-weight:800;letter-spacing:.12em;text-transform:uppercase;padding:10px 12px;
  border:2px solid var(--line-300);border-radius:10px;flex:1 1 220px;min-width:0;background:var(--surface-card);color:var(--text-strong)}
.suite{margin-top:18px}
.bilan{font-size:22px;font-weight:900;color:var(--text-strong)}
.resultats{list-style:none;padding:0;margin:12px 0;display:grid;gap:10px;max-width:640px}
.resultats li{background:var(--surface-card);border:1px solid var(--line-200);border-radius:12px;padding:10px 12px}
.ok-txt{color:var(--ok-ink);font-weight:800}.ko-txt{color:var(--warn-ink);font-weight:800}
.palier{display:flex;flex-direction:column;gap:2px;background:var(--accent-soft);border-radius:12px;padding:12px 14px;max-width:640px}
.palier b{font-size:24px;color:var(--text-strong)}
.palier small{color:var(--text-muted)}
.formateur{margin-top:18px;max-width:720px;border:1px solid var(--line-300);border-radius:12px;padding:10px 14px;background:var(--surface-card)}
.formateur summary{cursor:pointer;font-weight:800;min-height:32px}
.oral{border-top:1px solid var(--line-200);padding:10px 0}
.oral p{margin:4px 0}
.choix-oral{display:flex;flex-wrap:wrap;gap:12px;margin-top:8px}
.btn[aria-pressed=true]{border-color:var(--accent);background:var(--accent-soft)}
.carte-test{display:flex;flex-direction:column;gap:6px;background:var(--surface-card);border:2px solid var(--accent);border-radius:14px;padding:14px;cursor:pointer;font:inherit;text-align:start;width:100%;max-width:640px}
.carte-test b{font-size:20px;color:var(--text-strong)}
.regle{background:var(--surface-sunken);border-left:4px solid var(--accent);border-radius:8px;padding:10px 12px;margin:0 0 14px;max-width:640px}
.regle summary{cursor:pointer;min-height:32px}
.regle b{color:var(--text-strong)}
.phrase{font-size:20px;font-weight:700;color:var(--text-strong);margin:0 0 6px;max-width:640px}
.mot-vise{font-size:15px;color:var(--text-muted);margin:0 0 12px}
.mot-vise b{color:var(--text-strong);font-size:18px}
.dite{margin:10px 0 0;font-size:16px;color:var(--text-muted)}
@media (max-width:480px){.choix{gap:10px}.choix button{font-size:16px;padding:10px}.cible{font-size:22px}}
</style>
</head>
<body>
<div class="fr-barre"><div class="fr-barre__in">
  <span class="fr-lockup"><span class="fr-nom" role="img" aria-label="francis">franc<span class="fr-i" aria-hidden="true">ı<span class="fr-point"></span></span>s</span><span class="fr-trait" aria-hidden="true"></span><span class="fr-desc" id="desc"></span></span>
  <span class="secteur"><small id="surtitre"></small><b><span class="long" id="secteur"></span><span class="court" id="secteurCourt"></span></b></span>
</div></div>
<main class="hr" id="app"></main>
<script>
const D = %%DONNEES%%;
const E = s => String(s).replace(/[&<>"]/g, c => ({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;'}[c]));
const ICO = {
  son:'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"><path d="M11 5 6 9H3v6h3l5 4V5z"/><path d="M15.5 8.5a5 5 0 0 1 0 7"/><path d="M18.5 5.5a9 9 0 0 1 0 13"/></svg>',
  oeil:'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"><path d="M2 12s3.5-7 10-7 10 7 10 7-3.5 7-10 7S2 12 2 12z"/><circle cx="12" cy="12" r="3"/></svg>',
  retour:'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"><path d="M15 18l-6-6 6-6"/></svg>'};
const PAR_ID = Object.fromEntries(D.mots.map(m => [m.id, m]));
const CLE = 'hotel-reception-langues';
let L = {parle:null, apprend:null};
try { L = Object.assign(L, JSON.parse(localStorage.getItem(CLE) || '{}')); } catch (e) {}
const q = new URLSearchParams(location.search);
if (q.get('parle')) L.parle = q.get('parle');
if (q.get('apprend')) L.apprend = q.get('apprend');
function sauver(){ try { localStorage.setItem(CLE, JSON.stringify(L)); } catch (e) {} }
const T = k => D.ui[k][L.parle || 'fr'];
const paire = () => [L.parle, L.apprend].sort().join('·');
const PAIRE_ORDRE = {'en·fr':'fr·en','es·fr':'fr·es','en·es':'es·en'};

let son = null;
function ecouter(id){
  if (son) son.pause();
  son = new Audio(`/assets/interactive/hotel/sons/${L.apprend}/${id}.mp3?v=${D.v}`);
  son.play().catch(()=>{});
}
function piegeDe(m){ return m.paire && m.paire === PAIRE_ORDRE[paire()]; }
function noteDe(m){
  // Un piège d'une autre paire ne se montre pas ; une note ordinaire n'existe
  // pour l'instant qu'en français (étape 1).
  if (m.paire) return piegeDe(m) ? (m.notes[L.parle] || '') : '';
  return m.notes[L.parle] || '';
}

function marque(){
  const p = L.parle || 'fr';
  document.documentElement.lang = p;
  document.getElementById('desc').textContent = L.apprend ? D.desc[p][L.apprend] : D.desc.fr.fr;
  document.getElementById('surtitre').textContent = D.ui.surtitre[p];
  document.getElementById('secteur').textContent = D.ui.secteur[p];
  document.getElementById('secteurCourt').textContent = D.ui.secteur_court[p];
}

function ecranLangue(){
  const bouton = (g, l) => {
    const pris = g === 'apprend' && l === L.parle;
    return `<button type="button" data-g="${g}" data-l="${l}" aria-pressed="${L[g]===l}" ${pris?'disabled':''}>`
      + `${E(D.langues[l][l])}<small>${E(D.langues[L.parle||'fr'][l])}</small></button>`;
  };
  const pret = L.parle && L.apprend && L.parle !== L.apprend;
  return `<p class="enseigne">${E(D.hotel)}</p>
    <h1>Bienvenue · Welcome · Bienvenido</h1>
    <p class="choix-l">${E(D.ui.je_parle.fr)} · ${E(D.ui.je_parle.en)} · ${E(D.ui.je_parle.es)}</p>
    <div class="langues">${['fr','en','es'].map(l => bouton('parle', l)).join('')}</div>
    <p class="choix-l">${E(D.ui.j_apprends.fr)} · ${E(D.ui.j_apprends.en)} · ${E(D.ui.j_apprends.es)}</p>
    <div class="langues">${['fr','en','es'].map(l => bouton('apprend', l)).join('')}</div>
    <p style="margin-top:20px"><button type="button" class="btn btn--pri" id="go" ${pret?'':'disabled'}>${E(T('commencer'))}</button></p>`;
}

function ecranAccueil(){
  const vign = k => D.mots.filter(m => m.p === k && m.img).slice(0,3)
    .map(m => `<img src="/assets/interactive/hotel/croquis/${m.id}.jpg?v=${D.v}" alt="" loading="lazy">`).join('');
  const cartes = D.planches.filter(([k]) => k !== 'comptoir').map(([k, t]) =>
    `<button type="button" class="planche-c" data-aller="p-${k}"><span class="vign">${vign(k)}</span>`
    + `<b>${E(t[L.parle])}</b><span class="n">${D.mots.filter(m=>m.p===k).length} ${E(T('mots'))}</span></button>`).join('');
  return `<div class="barre-haut"><p class="enseigne">${E(D.hotel)}</p>
      <button type="button" class="btn" data-aller="langue">${E(T('changer'))}</button></div>
    <h1>${E(T('bienvenue_tit'))}</h1>
    <p class="chapeau">${E(T('intro'))}</p>
    <button type="button" class="carte-comptoir" data-aller="comptoir">
      <img src="/assets/interactive/hotel/croquis/comptoir.jpg?v=${D.v}" alt="">
      <span><b>${E(T('comptoir_tit'))}</b><span>${E(T('comptoir_sous'))}</span></span></button>
    <h2>${E(T('les_planches'))}</h2>
    <div class="planches">${cartes}</div>
    <h2>${E(D.test.ui.test_tit[L.parle])}</h2>
    <button type="button" class="carte-test" data-aller="test"><b>${E(D.test.ui.test_tit[L.parle])}</b><span>${E(D.test.ui.test_carte[L.parle])}</span></button>
    <h2>${E(T('exercices'))}</h2>
    <div class="exos">${FAMILLES.map(f => `<button type="button" class="exo-c" data-aller="x-${f}"><b>${E(T('x_'+f))}</b><span>${E(T('x_'+f+'_c'))}</span></button>`).join('')}</div>
    <p class="avis">${E(T('non_relu'))}</p>`;
}

function carteMot(m){
  const note = noteDe(m), pg = piegeDe(m);
  const img = m.img ? `<img class="img" src="/assets/interactive/hotel/croquis/${m.id}.jpg?v=${D.v}" alt="" loading="lazy">` : '';
  return `<article class="mot${pg?' piege':''}" data-id="${m.id}">${img}
    <p class="appris" lang="${L.apprend}">${E(m[L.apprend])}</p>
    <div class="actions"><button type="button" class="btn btn--son" data-son="${m.id}">${ICO.son}${E(T('ecouter'))}</button>
      <button type="button" class="btn" data-voir="${m.id}" aria-expanded="false">${ICO.oeil}${E(T('voir'))}</button></div>
    <p class="trad" id="tr-${m.id}" hidden>${E(m[L.parle])}</p>
    ${note ? `<p class="note">${pg ? `<b>${E(T('piege'))}</b> · ` : ''}${E(note.replace(/^(PIÈGE|TRAP|TRAMPA)\s*(\([^)]*\))?\s*:\s*/, ''))}</p>` : ''}
  </article>`;
}

function ecranPlanche(k){
  const t = D.planches.find(p => p[0] === k)[1];
  return `<div class="barre-haut"><button type="button" class="btn" data-aller="accueil">${ICO.retour}${E(T('retour'))}</button></div>
    <p class="enseigne">${E(D.hotel)}</p><h1>${E(t[L.parle])}</h1>
    <div class="grille">${D.mots.filter(m => m.p === k).map(carteMot).join('')}</div>`;
}

let objet = null;
function ecranComptoir(){
  const zones = D.zones.map(([id, x, y], i) =>
    `<button type="button" class="zone" style="left:${x}%;top:${y}%" data-objet="${id}" aria-pressed="${objet===id}"
      aria-label="${i+1}">${i+1}</button>`).join('');
  const liste = D.zones.map(([id], i) =>
    `<li><button type="button" data-objet="${id}" aria-pressed="${objet===id}"><b>${i+1}</b><span lang="${L.apprend}">${E(PAR_ID[id][L.apprend])}</span></button></li>`).join('');
  const m = objet && PAR_ID[objet];
  const panneau = m ? `<p class="appris" lang="${L.apprend}">${E(m[L.apprend])}</p>
      <div class="actions"><button type="button" class="btn btn--son" data-son="${m.id}">${ICO.son}${E(T('ecouter'))}</button>
      <button type="button" class="btn" data-voir="${m.id}" aria-expanded="false">${ICO.oeil}${E(T('voir'))}</button></div>
      <p class="trad" id="tr-${m.id}" hidden>${E(m[L.parle])}</p>` : `<p>${E(T('touchez'))}</p>`;
  return `<div class="barre-haut"><button type="button" class="btn" data-aller="accueil">${ICO.retour}${E(T('retour'))}</button></div>
    <p class="enseigne">${E(D.hotel)}</p><h1>${E(T('comptoir_tit'))}</h1>
    <p class="chapeau">${E(T('comptoir_sous'))}</p>
    <div class="scene"><img src="/assets/interactive/hotel/croquis/comptoir.jpg?v=${D.v}" alt="">${zones}</div>
    <div class="panneau" aria-live="polite">${panneau}</div>
    <h2>${E(T('liste_objets'))}</h2><ul class="objets">${liste}</ul>`;
}


// ── Les exercices ────────────────────────────────────────────────────────
const FAMILLES = ['entends','image','souviens','dire','pieges','epeler','nombres','client','reponds'];
const melange = a => { a = a.slice(); for (let i = a.length - 1; i > 0; i--) { const j = Math.floor(Math.random() * (i + 1)); [a[i], a[j]] = [a[j], a[i]]; } return a; };
// La bonne réponse TOURNE d'un item à l'autre (leçon de la boucle : « toujours
// la deuxième » réussissait l'épreuve). Graine tirée au début de la série.
// Les places sont ÉQUILIBRÉES (chacune revient autant de fois) puis MÉLANGÉES :
// une rotation régulière (0, 1, 2, 3, 0…) se devine aussi bien qu'une place fixe.
let PLACES = [];
function places(n, N){
  // Une série plus courte que deux tours de places ne peut pas les équilibrer :
  // on tire alors chaque place au hasard, SANS autre règle. Interdire de répéter
  // la place précédente (tour 2) en faisait un indice : jamais deux fois de
  // suite au même endroit (tour 3, 0 cas sur 1 200).
  if (N < 2 * n) { PLACES = Array.from({length: N}, () => Math.floor(Math.random() * n)); return; }
  PLACES = melange(Array.from({length: N}, (_, k) => k % n));
}
function placer(bonne, autres, i){
  const out = melange(autres);
  out.splice(PLACES[i] % (autres.length + 1), 0, bonne); return out;
}
const imgUrl = id => `/assets/interactive/hotel/croquis/${id}.jpg?v=${D.v}`;
function jouer(chemin, lent){
  if (son) son.pause();
  son = new Audio(`/assets/interactive/hotel/sons/${chemin}?v=${D.v}`);
  if (lent) son.playbackRate = 0.8;
  son.play().catch(()=>{});
}
let X = null;

function serie(fam){
  const A = L.apprend, P = L.parle;
  const avecImg = D.mots.filter(m => m.img);
  // Jamais ensemble : les images indiscernables ou qui se contiennent (tour 1, D4).
  const exclu = m => new Set([m.id, ...(D.ex.jamais.find(g => g.includes(m.id)) || [])]);
  const voisins = (m, n, filtre) => {
    const ex = exclu(m);
    let v = D.mots.filter(x => !ex.has(x.id) && x.p === m.p && filtre(x));
    if (v.length < n) v = v.concat(D.mots.filter(x => !ex.has(x.id) && x.p !== m.p && filtre(x)));
    const out = [];
    for (const x of melange(v)) {
      if (out.length >= n) break;
      if (out.some(y => exclu(y).has(x.id))) continue;
      out.push(x);
    }
    return out;
  };
  let items = [];
  if (fam === 'entends' || fam === 'image') places(4, 8);
  if (fam === 'nombres') places(4, D.ex.nombres.length);
  if (fam === 'client') places(4, D.ex.demandes.length);
  if (fam === 'reponds') places(3, D.ex.reponses.length);
  if (fam === 'entends' || fam === 'image')
    items = melange(avecImg).slice(0, 8).map((m, i) => ({m, choix: placer(m, voisins(m, 3, x => x.img), i)}));
  if (fam === 'souviens') items = melange(D.mots).slice(0, 10).map(m => ({m}));
  if (fam === 'pieges') {
    const pr = PAIRE_ORDRE[paire()];
    const lot = melange(D.mots.filter(m => m.paire === pr && D.ex.pieges[m.id] && D.ex.pieges[m.id][P]));
    places(3, lot.length);
    items = lot.map((m, i) => { const [phrase, faux, autre, expl] = D.ex.pieges[m.id][P];
      return {m, phrase, expl, choix: placer({t: m[P], ok: true}, [{t: faux}, {t: autre}], i)}; });
  }
  if (fam === 'epeler') items = melange(D.ex.noms).slice(0, 8).map(([nom, slug]) => ({nom, slug}));
  if (fam === 'nombres') items = melange(D.ex.nombres).map(([id, dit, bonne, parL], i) => ({id, dit, bonne, vs: parL[A], choix: placer(bonne, parL[A].map(v => v[0]), i)}));
  if (fam === 'client') items = melange(D.ex.demandes).map(([id, lit, n], i) => {
    const autreLit = melange(D.ex.lits.filter(l => l !== lit)), autreN = melange([1,2,3,4,5].filter(k => k !== n));
    return {id, lit, n, choix: placer({lit, n}, [{lit, n: autreN[0]}, {lit: autreLit[0], n}, {lit: autreLit[1], n: autreN[1]}], i)};
  });
  if (fam === 'reponds') items = melange(D.ex.reponses).slice(0, 8).map((r, i) => ({r, choix: placer({k: 0}, [{k: 1}, {k: 2}], i)}));
  // « Je le dis » (tour 1, D1) : produire vers la langue apprise, de mémoire.
  if (fam === 'dire') items = melange([
    ...melange(D.mots.filter(m => m.p === 'politesse')).slice(0, 6).map(m => ({m})),
    ...melange(D.ex.reponses).slice(0, 6).map(r => ({r}))]);
  X = {fam, items, n0: items.length, promesses: 0, i: 0, premier: 0, essais: 0, resolu: false, sus: 0, file: []};
}

function nuits(n){ const [un, pl] = D.ex.nuits[L.parle]; return `${n} ${n > 1 ? pl : un}`; }
function jouerItem(lent){
  const it = X.items[X.i], A = L.apprend;
  if (!it) return;
  if (X.fam === 'entends' || X.fam === 'souviens') jouer(`${A}/${it.m.id}.mp3`, lent);
  if (X.fam === 'pieges') jouer(`x/pieges/${A}/${it.m.id}.mp3`, lent);
  if (X.fam === 'epeler') jouer(`x/epeler/${A}/${it.slug}.mp3`, lent);
  if (X.fam === 'nombres') jouer(`x/nombres/${A}/${it.id}.mp3`, lent);
  if (X.fam === 'client') jouer(`x/client/${A}/${it.id}.mp3`, lent);
  if (X.fam === 'reponds') jouer(`x/reponds/${A}/${it.r.id}.mp3`, lent);
  // « Je le dis » : on entend le client ; le modèle, seulement après avoir dit.
  if (X.fam === 'dire' && it.r) jouer(`x/reponds/${A}/${it.r.id}.mp3`, lent);
}

function ecranExercice(fam){
  if (!X || X.fam !== fam) serie(fam);
  const A = L.apprend, P = L.parle, N = X.items.length;
  const tete = `<div class="barre-haut"><button type="button" class="btn" data-aller="accueil">${ICO.retour}${E(T('retour'))}</button>
    <span class="progres">${Math.min(X.i + 1, N)} / ${N}</span></div>
    <p class="enseigne">${E(D.hotel)}</p><h1>${E(T('x_' + fam))}</h1>`;
  if (!N) return tete + `<p class="consigne">${E(T('aucun_piege'))}</p>`;
  if (X.i >= N) return tete + `<p class="bilan">${E(T('fini'))}</p>
    ${X.promesses ? `<p class="alerte">${E(D.ex.promesse[P])} (${X.promesses})</p>` : ''}
    <p class="consigne">${fam === 'souviens' || fam === 'dire' ? `${X.premier} / ${X.n0} ${E(T('je_savais').toLowerCase())}` : `${X.premier} ${E(T('sur'))} ${X.n0} ${E(T('premier_coup'))}`}</p>
    <div class="ecoute"><button type="button" class="btn btn--pri" data-refaire="${fam}">${E(T('recommencer'))}</button>
    <button type="button" class="btn" data-aller="accueil">${E(T('autres_ex'))}</button></div>`;
  const it = X.items[X.i];
  const boutonsSon = `<div class="ecoute"><button type="button" class="btn btn--son" data-rejouer="0">${ICO.son}${E(T('reecouter'))}</button>
    ${['epeler','client','nombres','reponds'].includes(fam) ? `<button type="button" class="btn" data-rejouer="1">${E(T('lent'))}</button>` : ''}</div>`;
  let corps = `<p class="consigne">${E(T('x_' + fam + '_c'))}</p>`;
  // Le texte des images : le SENS, dans la langue de l'employé (tour 1, G1) — il
  // ne donne pas le mot entendu, il dit ce que l'image montre à qui la voit.
  if (fam === 'entends') corps += boutonsSon + `<div class="choix">${it.choix.map(m =>
      `<button type="button" data-rep="${m.id}"><img src="${imgUrl(m.id)}" alt="${E(m[P])}"></button>`).join('')}</div>`;
  if (fam === 'image') corps += `<img class="cible-img" src="${imgUrl(it.m.id)}" alt="${E(it.m[P])}"><div class="choix large">${it.choix.map(m =>
      `<button type="button" data-rep="${m.id}" lang="${A}">${E(m[A])}</button>`).join('')}</div>`;
  if (fam === 'souviens') corps += `<p class="cible" lang="${A}">${E(it.m[A])}</p>` + boutonsSon
      + `<p class="trad" id="sens" hidden style="font-size:20px;font-weight:800">${E(it.m[P])}</p>
      <div class="ecoute"><button type="button" class="btn" id="voirSens">${ICO.oeil}${E(T('voir_sens'))}</button></div>
      <div class="ecoute" id="auto" hidden><button type="button" class="btn btn--pri" data-auto="1">${E(T('je_savais'))}</button>
      <button type="button" class="btn" data-auto="0">${E(T('pas_encore'))}</button></div>`;
  if (fam === 'dire' && it.m) {
    corps += `<p class="mot-vise">${E(T('vous_dites'))}</p><p class="phrase" lang="${P}">${E(it.m[P])}</p>`;
  }
  if (fam === 'dire' && it.r) {
    // Tour 2 (D1) : le contexte s'affiche, et le client se fait ENTENDRE dans la
    // langue apprise, comme au comptoir ; sa traduction reste cachée.
    const ctx = it.r.ctx_dire || it.r.ctx;
    corps += (ctx ? `<p class="contexte">${E(ctx[P])}</p>` : '')
      + `<p class="mot-vise">${E(T('le_client_dit'))}</p>
      <div class="ecoute"><button type="button" class="btn btn--son" data-rejouer="0">${ICO.son}${E(T('reecouter'))}</button>
      <button type="button" class="btn" id="voirClient">${ICO.oeil}${E(T('voir'))}</button></div>
      <p class="phrase" id="client" lang="${P}" hidden>« ${E(it.r.client[P])} »</p>`;
  }
  if (fam === 'dire') {
    const modele = it.m ? it.m[A] : it.r.reps[0][0][A];
    corps += `
      <div class="ecoute"><button type="button" class="btn btn--son" id="modele" data-m="${it.m ? `${A}/${it.m.id}.mp3` : `x/modele/${A}/${it.r.id}.mp3`}">${ICO.son}${E(T('ecouter_modele'))}</button></div>
      <p class="phrase" id="sens" lang="${A}" hidden>${E(modele)}</p>
      <div class="ecoute" id="auto" hidden><button type="button" class="btn btn--pri" data-auto="1">${E(T('dit_pareil'))}</button>
      <button type="button" class="btn" data-auto="0">${E(T('pas_encore'))}</button></div>`;
  }
  if (fam === 'pieges') corps += `<p class="phrase" lang="${A}">${E(it.phrase)}</p><p class="mot-vise"><b lang="${A}">« ${E(it.m[A])} »</b></p>` + boutonsSon + `<div class="choix large">${it.choix.map((c, k) =>
      `<button type="button" data-rep="${k}">${E(c.t)}</button>`).join('')}</div>`;
  if (fam === 'epeler') corps += boutonsSon + `<form class="saisie" id="formNom"><input id="nom" autocomplete="off" autocapitalize="characters" spellcheck="false" aria-label="${E(T('votre_reponse'))}">
      <button type="submit" class="btn btn--pri">${E(T('verifier'))}</button></form>`;
  if (fam === 'nombres') corps += boutonsSon + `<p class="dite" id="dite" lang="${A}" hidden>${E(T('phrase_dite'))} « ${E(it.dit[A])} »</p><div class="choix">${it.choix.map(c =>
      `<button type="button" data-rep="${E(c)}" style="font-size:24px">${E(c)}</button>`).join('')}</div>`;
  if (fam === 'client') corps += boutonsSon + `<div class="choix">${it.choix.map((c, k) =>
      `<button type="button" data-rep="${k}"><img src="${imgUrl(c.lit)}" alt=""><small>${E(PAR_ID[c.lit][P])} · ${E(nuits(c.n))}</small></button>`).join('')}</div>`;
  if (fam === 'reponds') {
    const {ctx, client, reps} = it.r;
    // La règle est dite AVANT, toujours et pareil (O4) ; aucun avertissement propre à l'item.
    // En entier au premier item, repliée ensuite : relue huit fois, elle
    // finissait par désigner les réponses en mots-clés (tour 3).
    corps += `<details class="regle"${X.i === 0 ? ' open' : ''}><summary><b>${E(T('regle_tit'))}</b></summary>${E(D.ex.regle[P])}</details>`
      + (ctx ? `<p class="contexte">${E(ctx[P])}</p>` : '')
      + `<p class="cible" lang="${A}" style="font-size:20px">« ${E(client[A])} »</p>` + boutonsSon
      + `<div class="choix large">${it.choix.map(c => `<button type="button" data-rep="${c.k}" lang="${A}">${E(reps[c.k][0][A])}</button>`).join('')}</div>`;
  }
  return tete + corps + `<p class="retour-fb" id="fb" aria-live="polite"></p>
    <div class="suite" id="suite" hidden><button type="button" class="btn btn--pri" data-suivant="1">${E(T('suivant'))}</button></div>`;
}

function repondre(b){
  const it = X.items[X.i], A = L.apprend, P = L.parle, fb = document.getElementById('fb');
  if (X.resolu || b.disabled) return;
  let ok = false, msg = '';
  if (X.fam === 'entends' || X.fam === 'image') {
    ok = b.dataset.rep === it.m.id;
    if (!ok) { const m = PAR_ID[b.dataset.rep]; msg = `${T('non_cest')} « ${X.fam === 'entends' ? m[A] : m[P]} ».`;
      if (X.fam === 'entends') jouer(`${A}/${m.id}.mp3`); }
  }
  if (X.fam === 'pieges') { const c = it.choix[+b.dataset.rep]; ok = !!c.ok; msg = ok ? it.expl : `${T('encore')} ${it.expl}`; }
  if (X.fam === 'nombres') {
    ok = b.dataset.rep === it.bonne;
    if (!ok) {
      const v = it.vs.find(x => x[0] === b.dataset.rep);
      // L'erreur qui tient à la langue ENTENDUE a sa version par langue apprise.
      let e = D.ex.erreurs[v[1]]; if (e[L.apprend] && typeof e[L.apprend] === 'object') e = e[L.apprend];
      msg = e[P];
      // Après deux erreurs, on montre ce qui a été dit (tour 1, E1).
      if (X.essais >= 1) document.getElementById('dite').hidden = false;
    }
  }
  if (X.fam === 'client') {
    const c = it.choix[+b.dataset.rep]; ok = c.lit === it.lit && c.n === it.n;
    if (!ok) msg = c.lit === it.lit ? T('lit_ok') : c.n === it.n ? T('nuits_ok') : T('rien_ok');
  }
  if (X.fam === 'reponds') {
    const k = +b.dataset.rep, [, fb, promesse] = it.r.reps[k]; ok = k === 0;
    if (!ok) msg = fb[P];
    if (promesse) {
      // La promesse hors règle a une CONSÉQUENCE : l'item compte comme échoué
      // et le bilan le dit (tour 1, E2) — ce n'est pas une erreur comme une autre.
      X.promesses++;
      msg = `${fb[P]} ${D.ex.promesse[P]}`;
    }
  }
  noter(ok, msg, b);
}

function noter(ok, msg, b){
  const fb = document.getElementById('fb');
  if (ok) {
    if (X.essais === 0) X.premier++;
    X.resolu = true;
    if (b) b.classList.add('ok');
    document.querySelectorAll('.choix button').forEach(x => x.disabled = true);
    fb.className = 'retour-fb ok'; fb.textContent = `${T('juste')} ${msg}`.trim();
    document.getElementById('suite').hidden = false;
    document.querySelector('[data-suivant]').focus();
  } else {
    X.essais++;
    if (b) { b.classList.add('ko'); b.disabled = true; }
    fb.className = 'retour-fb ko'; fb.textContent = msg;
  }
}

// La saisie accepte les accents ; un nom juste sans ses accents ou ses traits
// d'union passe, avec un rappel. On signale la PREMIÈRE lettre fausse, pas un
// compte position par position (une lettre oubliée faussait tout le reste).
const nu = t => t.normalize('NFD').replace(/[̀-ͯ]/g, '').toUpperCase().replace(/[^A-Z]/g, '');
function verifierNom(){
  const it = X.items[X.i], brut = document.getElementById('nom').value.trim().toUpperCase(), v = nu(brut), att = nu(it.nom);
  if (!v || X.resolu) return;
  if (v === att) return noter(true, brut === it.nom ? it.nom : `${T('accent_oublie')} ${it.nom}`, null);
  let k = 0; while (k < v.length && v[k] === att[k]) k++;
  if (X.essais >= 1) {
    noter(false, `${T('la_bonne')} ${it.nom}`, null);
    X.resolu = true; document.getElementById('suite').hidden = false;
  } else noter(false, `${T('encore')} ${T('premiere_fausse')} ${k + 1}.`, null);
}

function suivant(){ X.i++; X.essais = 0; X.resolu = false; rendre(); setTimeout(() => jouerItem(false), 150); }

// ── Le test de positionnement (étape 3) ──────────────────────────────────
// A adaptatif (3 justes montent, 2 erreurs arrêtent) ; B en trois sous-parties
// passées par tous ; C éliminatoire, règle entière affichée avant ; D noté par
// le formateur sur deux lignes. Aucune rétroaction. La règle du palier vit dans
// test.py, en données ; appliquée ICI seulement (palierDe).
// L'historique suit la langue APPRISE, pas celle de l'interface (tour 3 : changer
// de langue d'interface ouvrait un historique vide, donc une passation sans code).
// Un code dans la page est un FREIN, pas une serrure : il se lit dans la source.
// Limite assumée (journal, tour 3) ; la vraie serrure viendra du serveur.
const CLE_TEST = () => `hotel-test-${L.apprend}`;
const CLE_ESSAIS = 'hotel-test-code-essais';
function codeBloque(){ try { const c = JSON.parse(localStorage.getItem(CLE_ESSAIS) || '{}'); return c.n >= 3 && Date.now() - c.t < 60000; } catch (e) { return false; } }
function codeEssai(ok){ try { const c = ok ? {n: 0} : JSON.parse(localStorage.getItem(CLE_ESSAIS) || '{"n":0}');
  if (!ok) { c.n = (Date.now() - (c.t || 0) > 60000 && c.n >= 3) ? 1 : c.n + 1; c.t = Date.now(); } localStorage.setItem(CLE_ESSAIS, JSON.stringify(c)); } catch (e) {} }
function verifierCode(v){ if (codeBloque()) return 'bloque'; const ok = v.trim() === D.test.code; codeEssai(ok); return ok ? 'ok' : (codeBloque() ? 'bloque' : 'faux'); }
const histo = () => { try { return JSON.parse(localStorage.getItem(CLE_TEST()) || '[]'); } catch (e) { return []; } };
const garderHisto = h => { try { localStorage.setItem(CLE_TEST(), JSON.stringify(h)); } catch (e) {} };
const TT = k => D.test.ui[k][L.parle];
let TX = null, micro = null;

// L'oral se garde dans IndexedDB jusqu'à la confirmation du formateur (tour 1 :
// il ne vivait qu'en mémoire et se perdait au rechargement).
function idb(){ return new Promise((ok, ko) => { try { const r = indexedDB.open('hotel-test', 1);
  r.onupgradeneeded = () => r.result.createObjectStore('oral'); r.onsuccess = () => ok(r.result); r.onerror = () => ko(r.error); } catch (e) { ko(e); } }); }
async function oralPut(k, blob){ try { const db = await idb(); db.transaction('oral', 'readwrite').objectStore('oral').put(blob, k); } catch (e) {} }
async function oralDel(k){ try { const db = await idb(); db.transaction('oral', 'readwrite').objectStore('oral').delete(k); } catch (e) {} }
async function oralGet(k){ try { const db = await idb(); return await new Promise(ok => { const r = db.transaction('oral').objectStore('oral').get(k); r.onsuccess = () => ok(r.result); r.onerror = () => ok(null); }); } catch (e) { return null; } }
const cleOral = (n, id) => `${CLE_TEST()}:${n}:${id}`;

// Une passation EN COURS se garde à chaque pas (tour 2 : un rechargement la
// faisait repartir de zéro, parfois dans l'autre forme).
const CLE_ENCOURS = () => CLE_TEST() + ':encours';
function garderEnCours(){ if (!TX || TX.part === 'fin') return;
  const c = Object.assign({}, TX, {d: {i: TX.d.i, enreg: {}}}); try { localStorage.setItem(CLE_ENCOURS(), JSON.stringify(c)); } catch (e) {} }
function purgerOral(n){ D.test.D[1].concat(D.test.D[2]).forEach(([id]) => oralDel(cleOral(n, id))); }
// Tour 3 : les voix se rechargent AUSSI en reprenant une passation en cours.
function chargerOral(){ const n = TX.n; D.test.D[TX.forme].forEach(async ([id]) => { const b = await oralGet(cleOral(n, id)); if (b && TX && TX.n === n && !TX.d.enreg[id]) { TX.d.enreg[id] = URL.createObjectURL(b); rendre(); } }); }
// Loi 25 : une passation jamais confirmée ne garde pas ses voix plus de 30 jours.
function purgerVieux(){ const h = histo(), lim = new Date(Date.now() - 30 * 864e5).toISOString().slice(0, 10);
  h.forEach((e, k) => { if (!e.confirme && e.date < lim) purgerOral(k + 1); }); }
function nouveauTest(){
  const h = histo();
  // Contrebalancement : la première forme au hasard, puis on alterne (tour 1).
  const forme = h.length ? 3 - h[h.length - 1].forme : (Math.random() < .5 ? 1 : 2);
  TX = {n: h.length + 1, forme, part: 'intro', cran: 1, bons: 0, err: 0, idx: 0, ordre: null, ecoutes: 0, rejoue: false,
        niv: {A: 0}, b: {i: 0, numero: 0, prix: 0, nom: 0}, c: {i: -1, ok: 0, promesse: false}, d: {i: 0, enreg: {}},
        oral: {}, formateur: false, codeFaux: false, codeOk: !h.length};
  // Les voix d'une passation abandonnée ne se mêlent pas à celle-ci ; celles des
  // passations précédentes quittent l'appareil : le formateur est passé à la suite.
  for (let k = 1; k <= TX.n; k++) purgerOral(k);
}
function reprendre(){
  try { const c = JSON.parse(localStorage.getItem(CLE_ENCOURS()) || 'null');
    if (c) { TX = c; TX.repriseEnCours = TX.part !== 'intro'; chargerOral(); return true; } } catch (e) {}
  // Au rechargement, une passation non confirmée rouvre SES résultats.
  const h = histo(), e = h[h.length - 1];
  if (!e || e.confirme) return false;
  TX = {n: h.length, forme: e.forme, part: 'fin', niv: {A: e.A}, b: e.B, c: {ok: e.C, promesse: e.promesse},
        d: {enreg: {}}, oral: e.oral || {}, formateur: false, codeFaux: false, repris: true};
  chargerOral();
  return true;
}
const cranItems = () => D.test.A[TX.forme].filter(x => x[1] === TX.cran);
function allerA(p){ Object.assign(TX, {part: p, cran: 1, bons: 0, err: 0, idx: 0, ordre: null, ecoutes: 0, rejoue: false}); }
function finPartie(){
  const suite = {A: 'B', B: 'Cintro', C: 'D', D: 'fin'}[TX.part];
  if (suite === 'fin') finTest(); else { allerA(suite); garderEnCours(); }
  rendre(); setTimeout(jouerTest, 150);
}
function suivantItem(){ TX.bVide = null; TX.ordre = null; TX.ecoutes = 0; TX.rejoue = false; garderEnCours(); rendre(); setTimeout(jouerTest, 150); }
function repA(ok){
  if (ok) TX.bons++; else TX.err++;
  TX.idx++;
  if (TX.bons === 3) {
    TX.niv.A = TX.cran;
    if (TX.cran === 3) return finPartie();
    Object.assign(TX, {cran: TX.cran + 1, bons: 0, err: 0, idx: 0});
  } else if (TX.err === 2 || TX.idx >= cranItems().length) return finPartie();
  suivantItem();
}
function repB(ok){
  const it = D.test.B[TX.forme][TX.b.i];
  if (ok) TX.b[it[1]]++;
  TX.b.i++;
  if (TX.b.i >= D.test.B[TX.forme].length) return finPartie();
  suivantItem();
}
function palierDe(e){
  const s = e.A + D.test.sous_b.filter(k => e.B[k] >= 2).length;
  const cOk = !e.promesse && e.C >= D.test.c_seuil;
  const notees = Object.values(e.oral || {}).filter(o => o.g !== undefined || o.l !== undefined);
  const notes = notees.filter(o => o.g !== undefined);
  const gestes = notes.filter(o => o.g <= 1).length, promesseOrale = notes.some(o => o.g === 2);
  // La langue compte aussi (tour 2) : « geste fait, incompréhensible » n'est pas « à l'aise ».
  const incomp = Object.values(e.oral || {}).filter(o => o.l === 2).length;
  const oralOk = !notees.length || (gestes >= D.test.oral_aise && !promesseOrale && incomp <= D.test.oral_incomp);
  if (s <= D.test.debutant_max || e.A === 0) return 'debutant';
  if (s >= D.test.aise_min && cOk && oralOk) return 'aise';
  return 'fonctionnel';
}
function finTest(){
  const h = histo();
  const e = {date: new Date().toISOString().slice(0, 10), forme: TX.forme, A: TX.niv.A,
             B: {numero: TX.b.numero, prix: TX.b.prix, nom: TX.b.nom}, C: TX.c.ok, promesse: TX.c.promesse,
             oral: {}, confirme: null};
  e.palier = palierDe(e); h.push(e); garderHisto(h);
  try { localStorage.removeItem(CLE_ENCOURS()); } catch (x) {}
  TX.n = h.length; TX.part = 'fin';
  Object.entries(TX.d.enreg).forEach(([id, u]) => { if (u) fetch(u).then(r => r.blob()).then(b => oralPut(cleOral(TX.n, id), b)); });
}
function majEntree(f){ const h = histo(); const e = h[h.length - 1]; f(e); e.palier = palierDe(e); garderHisto(h); }
function itemTest(){
  if (TX.part === 'A') return cranItems()[TX.idx];
  if (TX.part === 'B') return D.test.B[TX.forme][TX.b.i];
  if (TX.part === 'C') return D.test.C[TX.forme][TX.c.i];
  if (TX.part === 'D') return D.test.D[TX.forme][TX.d.i];
}
function jouerTest(){
  const it = itemTest(); if (!it || location.hash !== '#test') return;
  TX.ecoutes = (TX.ecoutes || 0) + 1;
  jouer(`test/${TX.part.toLowerCase()}/${L.apprend}/${it[0]}.mp3`);
}
function nuitsT(n){ const [un, pl] = TT('nuits').split('|'); return `${n} ${n > 1 ? pl : un}`; }

function ecranTest(){
  if (!TX) { purgerVieux(); if (!reprendre()) nouveauTest(); }
  const A = L.apprend, P = L.parle, h = histo();
  const tete = `<div class="barre-haut"><button type="button" class="btn" data-aller="accueil">${ICO.retour}${E(T('retour'))}</button>
    ${['A','B','C','D'].includes(TX.part) ? `<span class="progres">${E(TT('partie'))} ${TX.part} / D</span>` : ''}</div>
    <p class="enseigne">${E(D.hotel)}</p>`;
  if (TX.part === 'intro') return tete + `<h1>${E(TT('test_tit'))}</h1><p class="chapeau">${E(TT('test_intro'))}</p>
      <p class="alerte">${E(TT('regle_c'))}</p>
      <p class="consigne">${E(TT('passation'))} ${TX.n} · ${E(TT('forme'))} ${TX.forme}</p>
      ${TX.codeOk ? `<div class="ecoute"><button type="button" class="btn btn--pri" data-t="debut">${E(TT('commencer_test'))}</button></div>`
        : `<p class="dite">${E(TT('nouvelle_passation'))}</p><form class="saisie" id="formCodeDebut"><input id="codeD" inputmode="numeric" autocomplete="off" aria-label="${E(TT('code'))}" placeholder="${E(TT('code'))}">
           <button type="submit" class="btn btn--pri">${E(TT('commencer_test'))}</button></form>${TX.codeFaux ? `<p class="ko-txt">${E(TT(TX.codeFaux === 'bloque' ? 'code_attente' : 'code_faux'))}</p>` : ''}`}`;
  if (TX.part === 'Cintro') return tete + `<h1>C · ${E(TT('pC'))}</h1>
      <div class="regle"><b>${E(T('regle_tit'))}</b>${E(D.ex.regle[P])}</div>
      <p class="alerte">${E(TT('regle_c'))}</p>
      <div class="ecoute"><button type="button" class="btn btn--pri" data-t="cdebut">${E(TT('suivant'))}</button></div>`;
  if (TX.part === 'fin') return tete + ecranResultats();
  const it = itemTest();
  // Une seule réécoute, comme « Pardon? » au comptoir (tour 1, D2).
  const limite = TX.part === 'A' || TX.part === 'B';
  const son = `<div class="ecoute"><button type="button" class="btn btn--son" data-t="ecouter" ${limite && TX.rejoue ? 'disabled' : ''}>${ICO.son}${E(T('reecouter'))}</button></div>`
    + (limite ? `<p class="dite">${E(TT('une_reecoute'))}</p>` : '');
  let corps = `<h1>${TX.part} · ${E(TT('p' + TX.part))}</h1>`;
  if (TX.part === 'A') {
    const [id, cran, , lit, n, lit2, n2] = it;
    if (!TX.ordre) TX.ordre = melange(cran === 1
      ? [lit, ...melange(D.test.lits_c1[TX.forme].filter(l => l !== lit)).slice(0, 3)].map(l => ({lit: l, n: null}))
      : [{lit, n}, {lit, n: n2}, {lit: lit2, n}, {lit: lit2, n: n2}]);
    corps += `<p class="consigne">${E(TT('pA_c'))}</p>` + son + `<div class="choix">${TX.ordre.map((c, k) =>
      `<button type="button" data-t="rep" data-k="${k}"><img src="${imgUrl(c.lit)}" alt="${E(PAR_ID[c.lit][P])}"><small>${E(PAR_ID[c.lit][P])}${c.n ? ' · ' + E(nuitsT(c.n)) : ''}</small></button>`).join('')}</div>`;
  }
  if (TX.part === 'B') {
    // Tout se TAPE (tour 2) : un choix de nombres se déjoue toujours.
    const nom = it[1] === 'nom';
    corps += `<p class="mot-vise"><b>${E(TT('b_' + it[1]))}</b></p><p class="consigne">${E(TT(nom ? 'pB_nom' : 'pB_c'))}</p>` + son
      + `<form class="saisie" id="formTestB"><input id="saisieB" autocomplete="off" spellcheck="false" ${nom ? 'autocapitalize="characters"' : 'inputmode="text"'} aria-label="${E(TT('saisie_b'))}" placeholder="${E(TT('saisie_b'))}">
         <button type="submit" class="btn btn--pri">${E(TT('valider'))}</button></form>`
      + (TX.bVide ? `<p class="ko-txt" role="alert">${E(TT(TX.bVide))}</p>` : '');
  }
  if (TX.part === 'C') corps += `<p class="consigne">${E(TT('pC_c'))}</p>` + (it[1] ? `<p class="contexte">${E(it[1][P])}</p>` : '') + son
    + `<div class="choix large">${['moi', 'gerant', 'personne'].map(k =>
      `<button type="button" data-t="c" data-k="${k}">${E(D.test.choix_c[k][P])}</button>`).join('')}</div>`;
  if (TX.part === 'D') {
    const [id, ctx] = it, enr = TX.d.enreg[id];
    corps += `<p class="consigne">${E(TT('pD_c'))}</p>` + (ctx ? `<p class="contexte">${E(ctx[P])}</p>` : '') + son
      + (navigator.mediaDevices && window.MediaRecorder
        ? `<div class="ecoute">${micro ? `<button type="button" class="btn btn--son" data-t="stop">${E(TT('arreter'))}</button>`
            : `<button type="button" class="btn" data-t="rec">${E(TT('enregistrer'))}</button>`}
           ${enr ? `<button type="button" class="btn" data-t="playrec" data-id="${id}">${ICO.son}${E(TT('reecouter_moi'))}</button>` : ''}</div>`
        : `<p class="alerte">${E(TT('sans_micro'))}</p>`)
      + `<div class="suite"><button type="button" class="btn btn--pri" data-t="dsuite" ${micro ? 'disabled' : ''}>${E(TT('suivant'))}</button></div>`;
  }
  return tete + corps;
}

function ecranResultats(){
  const A = L.apprend, P = L.parle, h = histo(), e = h[h.length - 1];
  const ligne = (t, v) => `<li><b>${E(t)}</b> — ${v}</li>`;
  let f = `<h1>${E(TT('fini_tit'))}</h1>` + (TX.repris ? `<p class="alerte">${E(TT('reprise'))}</p>` : '')
    + `<p class="chapeau">${E(TT('fini_c'))}</p><ul class="resultats">`
    + ligne('A · ' + TT('pA'), `${E(TT('niveau'))} ${e.A} / 3`)
    + D.test.sous_b.map(k => ligne('B · ' + TT('b_' + k), `${e.B[k]} ${E(TT('bonnes'))} 3`)).join('')
    + ligne('C · ' + TT('pC'), `${e.C} ${E(TT('bonnes'))} 6 (${E(TT('c_vise'))})`) + `</ul>`
    + (e.promesse ? `<p class="alerte">${E(TT('promesse_c'))}</p>` : '')
    + `<p class="dite">${E(D.test.cadrage[P])}</p>`
    + (h.length > 1 ? (p => `<p class="dite"><b>${E(TT('precedent'))}</b> (${E(p.date)}) — A ${p.A}/3 · B ${D.test.sous_b.map(k => p.B[k]).join('-')} · C ${p.C}/6 · ${E(TT(p.confirme || p.palier))}</p>`)(h[h.length - 2]) : '')
    + `<p class="palier"><span>${E(TT('palier_propose'))}</span><b>${E(TT(e.confirme || e.palier))}</b><small>${E(TT('palier_oral'))}</small></p>`;
  f += `<details class="formateur"${TX.formateur ? ' open' : ''}><summary>${E(TT('formateur'))}</summary>`;
  if (!TX.formateur) f += `<form class="saisie" id="formCode"><input id="codeF" inputmode="numeric" autocomplete="off" aria-label="${E(TT('code'))}" placeholder="${E(TT('code'))}">
      <button type="submit" class="btn">${E(TT('ouvrir'))}</button></form>${TX.codeFaux ? `<p class="ko-txt">${E(TT(TX.codeFaux === 'bloque' ? 'code_attente' : 'code_faux'))}</p>` : ''}`;
  else {
    const gg = D.test.oral_geste[P].split('|'), gl = D.test.oral_langue[P].split('|');
    f += D.test.D[e.forme].map(([id, ctx, client, geste, ex]) => { const o = (e.oral || {})[id] || {};
      return `<div class="oral"><p><b>« ${E(client[A])} »</b></p><p>${E(TT('geste'))} : ${E(D.test.gestes[geste][P])}</p>
        <p class="dite">${E(TT('exemple'))} : <span lang="${A}">${E(ex[A])}</span></p>
        ${TX.d.enreg[id] ? `<button type="button" class="btn" data-t="playrec" data-id="${id}">${ICO.son}${E(TT('reecouter_moi'))}</button>` : `<p class="dite">—</p>`}
        <p class="dite">${E(TT('ligne_geste'))}</p><div class="choix-oral">${gg.map((g, k) => `<button type="button" class="btn" data-t="oral" data-l="g" data-id="${id}" data-k="${k}" aria-pressed="${o.g === k}">${E(g)}</button>`).join('')}</div>
        <p class="dite">${E(TT('ligne_langue'))}</p><div class="choix-oral">${gl.map((g, k) => `<button type="button" class="btn" data-t="oral" data-l="l" data-id="${id}" data-k="${k}" aria-pressed="${o.l === k}">${E(g)}</button>`).join('')}</div></div>`; }).join('')
      + `<p><b>${E(TT('confirmer'))}</b></p><div class="ecoute">${D.test.paliers.map(p =>
        `<button type="button" class="btn" data-t="palier" data-p="${p}" aria-pressed="${e.confirme === p}">${E(TT(p))}</button>`).join('')}</div>`
      + (TX.avertir ? `<p class="alerte">${E(TT('oral_incomplet'))}</p>` : '')
      + (e.confirme ? `<p class="ok-txt">${E(TT('confirme'))} ${E(TT(e.confirme))}</p>` : '')
      // « Refaire » derrière le code : il consommerait l'autre forme (tour 1).
      + `<div class="ecoute" style="margin-top:14px"><button type="button" class="btn" data-t="refaire">${E(TT('refaire_test'))}</button></div>`;
  }
  f += `</details><div class="ecoute" style="margin-top:18px"><button type="button" class="btn" data-aller="accueil">${E(TT('retour_accueil'))}</button></div>`;
  return f;
}

async function enregistrer(){
  if (son) son.pause();   // micro et voix exclusifs (Chrome dégrade la sortie)
  try {
    const flux = await navigator.mediaDevices.getUserMedia({audio: true});
    const rec = new MediaRecorder(flux), morceaux = [], id = itemTest()[0];
    rec.ondataavailable = e => morceaux.push(e.data);
    rec.onstop = () => { flux.getTracks().forEach(t => t.stop());
      const blob = new Blob(morceaux, {type: rec.mimeType}); TX.d.enreg[id] = URL.createObjectURL(blob);
      oralPut(cleOral(TX.n, id), blob); micro = null; rendre(); };
    rec.start(); micro = rec; rendre();
  } catch (e) { micro = null; alert(TT('sans_micro')); }
}

function clicTest(b){
  const t = b.dataset.t, it = itemTest();
  if (t === 'debut') { allerA('A'); garderEnCours(); rendre(); setTimeout(jouerTest, 150); return; }
  if (t === 'cdebut') { TX.part = 'C'; TX.c.i = 0; suivantItem(); return; }
  if (t === 'ecouter') { if ((TX.part === 'A' || TX.part === 'B') && TX.rejoue) return; TX.rejoue = true; garderEnCours(); jouerTest(); rendre(); return; }
  if (t === 'rep' && TX.part === 'A') { const c = TX.ordre[+b.dataset.k]; return repA(c.lit === it[3] && (it[1] === 1 || c.n === it[4])); }
  if (t === 'c') {
    const k = b.dataset.k, bonne = it[3];
    if (k === bonne) TX.c.ok++;
    // Accorder soi-même ce qui revient au gérant, ou ce que personne ne peut accorder.
    if (k === 'moi' && bonne !== 'moi') TX.c.promesse = true;
    TX.c.i++;
    if (TX.c.i >= D.test.C[TX.forme].length) return finPartie();
    suivantItem(); return;
  }
  if (t === 'rec') { enregistrer(); return; }
  if (t === 'stop') { if (micro) micro.stop(); return; }
  if (t === 'playrec') { const u = TX.d.enreg[b.dataset.id]; if (u) { if (son) son.pause(); son = new Audio(u); son.play(); } return; }
  if (t === 'dsuite') { TX.d.i++; if (TX.d.i >= D.test.D[TX.forme].length) return finPartie(); suivantItem(); return; }
  if (t === 'oral') { const id = b.dataset.id, l = b.dataset.l, k = +b.dataset.k;
    majEntree(e => { e.oral = e.oral || {}; e.oral[id] = Object.assign(e.oral[id] || {}, {[l]: k}); }); rendre(); return; }
  if (t === 'palier') {
    const e0 = histo().slice(-1)[0], notees = Object.values(e0.oral || {}).filter(o => o.g !== undefined && o.l !== undefined).length;
    if (Object.keys(TX.d.enreg).length && notees < D.test.D[e0.forme].length && TX.avertir !== b.dataset.p) { TX.avertir = b.dataset.p; rendre(); return; }
    TX.avertir = null; majEntree(e => { e.confirme = b.dataset.p; });
    // Confirmé : les voix de l'employé quittent l'appareil (Loi 25 ; tour 2).
    purgerOral(TX.n); TX.d.enreg = {}; rendre(); return; }
  if (t === 'refaire') { nouveauTest(); TX.codeOk = true; rendre(); return; }
}
// Tour 3 : la saisie compare une VALEUR. Un prix : 239 = 239.00 = 239,00 $ ;
// 175,40 = 175.4. Une heure : 17:15 = 17h15 = 1715 = 5:15 pm ; quand la voix
// apprise dit l'heure sur 12 (en, es), « 5:15 » seul est juste aussi.
const chiffres = t => String(t).replace(/\D/g, '');
function heure(t){ const x = String(t).toLowerCase(), pm = /p\.?\s*m|tarde|noche|soir/.test(x), am = /a\.?\s*m|ma[ñn]ana|matin/.test(x);
  let m = x.match(/(\d{1,2})\s*[:h.]\s*(\d{2})/) || x.replace(/\D/g, '').match(/^(\d{1,2})(\d{2})$/);
  if (!m) return null; let h = +m[1]; if (pm && h < 12) h += 12; return {h, m: +m[2], pm, am}; }
function prix(t){ const x = String(t).replace('$', '').trim().replace(/^(\d+)\s+(\d{2})$/, '$1.$2').replace(/\s/g, '').replace(',', '.'); return /^\d+(\.\d{1,2})?$/.test(x) ? +x : null; }
function valeurJuste(v, att){
  if (att.includes(':')) { const a = heure(att), r = heure(v); if (!r) return false;
    return r.m === a.m && (r.h === a.h || (L.apprend !== 'fr' && !r.pm && !r.am && r.h + 12 === a.h)); }
  if (att.includes('$')) { const a = prix(att), r = prix(v); return r !== null && Math.abs(r - a) < 0.001; }
  return chiffres(v) === chiffres(att); }
document.addEventListener('submit', e => {
  if (e.target.id === 'formTestB') { e.preventDefault(); const v = document.getElementById('saisieB').value, it = itemTest();
    const nom = it[1] === 'nom', vide = nom ? !nu(v) : !chiffres(v);
    TX.bVide = vide ? (nom ? 'que_lettres' : 'que_chiffres') : null;
    if (vide) { rendre(); const i = document.getElementById('saisieB'); if (i) { i.value = v; i.focus(); } return; }
    return nom ? repB(nu(v) === nu(it[2])) : repB(valeurJuste(v, it[3])); }
  if (e.target.id === 'formCodeDebut') { e.preventDefault(); const r = verifierCode(document.getElementById('codeD').value);
    if (r === 'ok') { TX.codeOk = true; TX.codeFaux = false; allerA('A'); garderEnCours(); rendre(); setTimeout(jouerTest, 150); }
    else { TX.codeFaux = r; rendre(); } return; }
  if (e.target.id === 'formCode') { e.preventDefault(); const r = verifierCode(document.getElementById('codeF').value);
    if (r === 'ok') { TX.formateur = true; TX.codeFaux = false; } else TX.codeFaux = r;
    rendre(); }
});

function rendre(){
  marque();
  const h = location.hash.slice(1);
  const pret = L.parle && L.apprend && L.parle !== L.apprend;
  let html;
  if (!pret || h === 'langue') html = ecranLangue();
  else if (h === 'comptoir') html = ecranComptoir();
  else if (h.startsWith('p-') && D.planches.some(p => 'p-'+p[0] === h)) html = ecranPlanche(h.slice(2));
  else if (h.startsWith('x-') && FAMILLES.includes(h.slice(2))) html = ecranExercice(h.slice(2));
  else if (h === 'test') html = ecranTest();
  else html = ecranAccueil();
  document.getElementById('app').innerHTML = html;
}

document.addEventListener('click', e => {
  const b = e.target.closest('button'); if (!b) return;
  // On reste sur le choix des langues jusqu'à « Commencer » : sans l'ancre,
  // le second choix faisait sauter à l'accueil.
  if (b.dataset.t && location.hash === '#test') { clicTest(b); return; }
  if (b.dataset.g) { L[b.dataset.g] = b.dataset.l; if (L.apprend === L.parle) L.apprend = null; sauver();
    if (location.hash !== '#langue') history.replaceState(null, '', '#langue'); rendre(); return; }
  if (b.id === 'go') { location.hash = 'accueil'; return; }
  if (b.dataset.aller) { location.hash = b.dataset.aller; window.scrollTo(0, 0); return; }
  if (b.dataset.son) { ecouter(b.dataset.son); return; }
  if (b.dataset.rep !== undefined && X) { repondre(b); return; }
  if (b.dataset.rejouer !== undefined) { jouerItem(b.dataset.rejouer === '1'); return; }
  if (b.dataset.suivant) { suivant(); return; }
  if (b.dataset.refaire) { serie(b.dataset.refaire); rendre(); setTimeout(() => jouerItem(false), 150); return; }
  if (b.id === 'voirClient') { document.getElementById('client').hidden = false; b.hidden = true; return; }
  if (b.id === 'modele') { jouer(b.dataset.m); document.getElementById('sens').hidden = false; document.getElementById('auto').hidden = false; return; }
  if (b.id === 'voirSens') { document.getElementById('sens').hidden = false; document.getElementById('auto').hidden = false; b.hidden = true; return; }
  if (b.dataset.auto !== undefined) {
    // « Je me souviens » n'est pas jugé : « pas encore » remet la carte une fois en fin de série.
    const it = X.items[X.i];
    if (b.dataset.auto === '1') X.premier++; else if (!it.revu) X.items.push(Object.assign({}, it, {revu: true}));
    suivant(); return; }
  if (b.dataset.voir) {
    const tr = document.getElementById('tr-' + b.dataset.voir), ouvert = tr.hidden;
    tr.hidden = !ouvert; b.setAttribute('aria-expanded', ouvert);
    b.lastChild.textContent = ouvert ? T('cacher') : T('voir'); return; }
  if (b.dataset.objet) {
    objet = b.dataset.objet; rendre(); ecouter(objet);
    document.querySelector('.panneau').scrollIntoView({block:'nearest'}); return; }
});
document.addEventListener('submit', e => { if (e.target.id === 'formNom') { e.preventDefault(); verifierNom(); } });
window.addEventListener('hashchange', () => {
  objet = null;
  const h = location.hash.slice(1);
  if (h.startsWith('x-')) { serie(h.slice(2)); rendre(); setTimeout(() => jouerItem(false), 150); }
  else { X = null; rendre(); }
});
// Pour les contrôles joués par programme (build/controles) : l'état de la série.
window.HR = {familles: FAMILLES, etat: () => X, test: () => TX,
  donnees: /[?&]controle=1/.test(location.search) ? D : undefined};
rendre();
</script>
</body>
</html>
"""

if __name__ == "__main__":
    main()
