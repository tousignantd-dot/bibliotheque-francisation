#!/usr/bin/env python3
"""L'application « Une semaine à Toronto » — l'anglais du touriste francophone, sur téléphone.

    python3 build/toronto_app.py     # → modules-autonomes/toronto/index.html

Produite, jamais écrite à la main. Elle lit build/contenu/toronto/ (`preparation.py`,
`lexique.py`, `personnages.py`) et la liste des sons de build/toronto_commun.py,
la même que celle du générateur de voix (build/toronto_audio.py).

ÉTAPE 1 (1er oct. 2026) : l'accueil, « Avant de partir » (huit séances de
quinze minutes, trois temps chacune) et le test « Prêt à partir ? ». Le moteur
est celui de Compostelle (build/compostelle_app.py) — son, micro, avis de la
Loi 25, comparaison des réponses, place tournante de la bonne réponse — réécrit
pour l'anglais. Les étapes suivantes (les mots, la semaine jouée, la poche)
viendront s'y ajouter.

FAUX DÉBUTANT (décision du plan) : rien n'est verrouillé ; le test se passe
d'abord si l'on veut, et « Solide » partout dit qu'on peut sauter les séances.

RIEN NE PART : l'état vit dans le localStorage du téléphone. La reconnaissance
vocale est celle du navigateur, annoncée avant le premier usage.
"""
import json, pathlib, re, sys

RACINE = pathlib.Path(__file__).resolve().parent.parent
sys.path.insert(0, str(RACINE / "build"))
import toronto_commun as C  # noqa: E402

SORTIE = RACINE / "modules-autonomes" / "toronto" / "index.html"
MEDIA = RACINE / "assets" / "interactive" / "toronto"
MEDIA_V = "6"  # 6 : tour 3 des exercices (allergie, nombres, totaux refaits, mêmes noms) ; 5 : tour 2 des exercices (totaux et allergie refaits, mêmes noms) ; 4 : exercices refaits au tour 1 (numéros décalés, même nom, autre son) ; 3 : test 0-5 refait (fin coupée) ; 2 : cinq extraits refaits après le tour 3 (même nom, autre son) ; 1 : première production


def plan_ville():
    """Le plan du métro de la page du plan (build/toronto_plan.py) : un seul dessin de la ville."""
    import toronto_plan as TP
    style = re.search(r"<style>(.*?)</style>", TP.STYLE, re.S).group(1)
    regles = "\n".join(l for l in style.splitlines() if l.startswith(".plan") or l.startswith(".defile"))
    return TP.plan_metro(), regles


def donnees():
    PR, LX, PS = C.charger("preparation"), C.charger("lexique"), C.charger("personnages")
    SE = C.charger("semaine"); SE.verifier(PS.VOIX)
    LX.verifier()
    PR.verifier({e[0] for e in LX.LEXIQUE}, PS.VOIX)
    tous = C.extraits()
    noms = [x["fichier"] for x in tous]
    assert len(noms) == len(set(noms)), "deux extraits au même nom"
    sons = sorted(f for f in noms if (C.SONS / f).exists())
    mots = {}
    for i, pl, en, fr, dessin, note in LX.LEXIQUE:
        img = "croquis" if dessin == "croquis" and (MEDIA / "croquis" / f"{i}.jpg").exists() else ""
        mots[i] = {"p": pl, "en": en, "fr": fr, "img": img, "note": note}
    perso = {k: {"nom": v[0], "qui": v[4]} for k, v in PS.VOIX.items()}
    for i, pl, en, fr, dessin, note in LX.LEXIQUE:
        if dessin.startswith("picto:"):
            mots[i]["img"] = dessin
    # La série des pièges : (id, phrase, bonne, fausse lecture, second choix, explication).
    pieges = [{"id": i, "en": t[0], "bonne": t[1], "fausse": t[2], "seconde": t[3], "expl": t[4], "expl2": t[5],
               "vrai": i in LX.VRAIS_AMIS} for i, t in LX.PIEGES.items()]
    gens = {g[0]: {"nom": g[1], "role": g[3], "voix": "toronto_" + g[2],
                   "portrait": (MEDIA / "gens" / f"{g[0]}-neutre.jpg").exists()} for g in SE.GENS}
    # L'étape 5 : la semaine jouée (build/contenu/toronto/jeu_de_role.py, chargé aussi par server.py).
    JR = C.charger("jeu_de_role"); JR.verifier()
    # L'étape 6 : la poche — urgences et phrases à montrer (poche.py), puis, par lieu, les phrases
    # « Je le dis » et ce qu'on peut vous répondre, avec les sons des exercices.
    PO, EXP = C.charger("poche"), C.charger("exercices"); PO.verifier()
    CF = C.charger("confidentialite"); CF.verifier()
    confid = {"responsable": CF.RESPONSABLE, "courriel": CF.COURRIEL, "maj": CF.MISE_A_JOUR, "bref": CF.EN_BREF,
              "donnees": CF.DONNEES, "hors": CF.HORS_QUEBEC, "nefait": CF.NE_FAIT_PAS}
    sons_ok = set(sons)
    def s_(f): return f if f in sons_ok else ""
    poche = {"urgences": [{"en": en, "fr": fr, "son": s_(f"poche/{i}.mp3")} for i, en, fr in PO.URGENCES],
             "montrer": [{"en": en, "fr": fr, "son": s_(f"poche/{i}.mp3")} for i, en, fr in PO.A_MONTRER],
             "pourboires": PO.POURBOIRES,
             "lieux": [{"lieu": l[3],
                        "dire": [{"en": en, "fr": fr, "son": s_(f"exos/dire-{k}.mp3")} for k, (li, fr, en, cles) in enumerate(EXP.DIRE) if li == l[0]],
                        "reponses": [{"en": en, "fr": ch[0][0], "son": s_(f"exos/rep-{k}.mp3")} for k, (li, q, ctx, en, ch) in enumerate(EXP.REPONSES) if li == l[0]]}
                       for l in SE.LIEUX]}
    poids = round(sum((C.SONS / f).stat().st_size for f in sons) / 1e6)
    jeu = {"consigne": JR.CONSIGNE, "gestes": JR.GESTES, "elim": list(JR.ELIMINATOIRE), "regle": JR.REGLE_ELIM,
           "maya": [{"cas": m[0], "jour": m[1], "ou": m[2]} for m in JR.MAYA]}
    EX = C.charger("exercices"); EX.verifier({l[0] for l in SE.LIEUX} | {"magasin"}, PS.VOIX, {g[0] for g in SE.GENS})
    nom_lieu = {l[0]: l[3] for l in SE.LIEUX} | {"magasin": "Un magasin"}
    totaux = []
    for (l, q, ctx, en, prix, mal, pb, mot, inclus) in EX.TOTAL:
        ch, calcul = EX.total(prix, mal, pb, mot, inclus)
        totaux.append({"lieu": nom_lieu[l], "qui": q, "ctx": ctx, "en": en, "calcul": calcul,
                       "choix": [[f"{v:.2f} $".replace(".", ","), r] for v, r in ch]})
    exos = {"reponses": [{"lieu": nom_lieu[l], "qui": q, "ctx": ctx, "en": en, "choix": ch} for l, q, ctx, en, ch in EX.REPONSES],
            "nombres": [{"qui": q, "en": en, "choix": ch} for q, en, ch in EX.NOMBRES],
            "totaux": totaux,
            "chemins": [{"qui": q, "en": en, "blocs": b, "tourner": t} for q, en, b, t in EX.CHEMIN],
            "dire": [{"lieu": nom_lieu[l], "fr": fr, "en": en, "cles": cles, "garde": EX.garde(fr)} for l, fr, en, cles in EX.DIRE],
            "allergie": {"regle": EX.REGLE_ALLERGIE, "items": [{"qui": it[0], "ctx": it[1], "en": it[2], "apres": it[4],
                         "choix": EX.choix_allergie(it)} for it in EX.ALLERGIE]},
            "proches": [sorted(g) for g in EX.PROCHES], "horsSerie": sorted(EX.HORS_SERIE)}
    semaine = [{"id": l[0], "n": l[1], "jour": l[2], "lieu": l[3], "situation": l[4], "geste": l[5], "qui": l[6],
                "carte": (MEDIA / "cartes" / f"{l[0]}.jpg").exists()} for l in SE.LIEUX]
    return {"v": MEDIA_V, "mots": mots, "perso": perso, "sons": sons, "planches": LX.PLANCHES, "pieges": pieges,
            "semaine": semaine, "gens": gens, "exos": exos, "jeu": jeu, "poche": poche, "poids": poids, "confid": confid,
            "prep": {"seances": PR.SEANCES, "test": PR.TEST, "objectifs": PR.OBJECTIFS, "seuil": PR.SEUIL,
                     "conseils": PR.CONSEILS, "fin": PR.FIN, "lieu": PR.LIEU, "solide": PR.SEUIL_SOLIDE},
            # Les réponses témoins des clés, rejouées dans le moteur de la page (audit tour 5) : `window.__toronto`.
            "controle": {"refus": PR.REFUS + EX.REFUS, "accepte": PR.ACCEPTE + EX.ACCEPTE}}, len(sons), len(noms)


def icones():
    """L'icône de l'application installée : une tour d'observation dessinée au trait, rien d'écrit,
    aucun logo d'organisme ; le rouge de la ville. Et le manifeste (même forme que Compostelle)."""
    from PIL import Image, ImageDraw
    dest = SORTIE.parent / "icones"; dest.mkdir(parents=True, exist_ok=True)
    for nom, cote, part in (("icone-192.png", 192, .78), ("icone-512.png", 512, .78),
                            ("icone-maskable-512.png", 512, .56), ("icone-180.png", 180, .78)):
        im = Image.new("RGB", (cote, cote), "#FFFFFF"); d = ImageDraw.Draw(im)
        h = cote * part; x0 = cote / 2; bas = (cote + h) / 2; haut = bas - h; r = (0xC8, 0x10, 0x2E)
        d.polygon([(x0 - h * .09, bas), (x0 - h * .025, haut + h * .32), (x0 + h * .025, haut + h * .32), (x0 + h * .09, bas)], fill=r)
        d.ellipse([x0 - h * .1, haut + h * .26, x0 + h * .1, haut + h * .36], fill=r)
        d.rectangle([x0 - h * .012, haut, x0 + h * .012, haut + h * .27], fill=r)
        d.rectangle([cote * .12, bas - h * .02, cote * .88, bas], fill=r)
        im.save(dest / nom, optimize=True)
    base = "/modules-autonomes/toronto/"
    (SORTIE.parent / "manifest.webmanifest").write_text(json.dumps({
        "name": "Une semaine à Toronto — francis", "short_name": "Toronto",
        "description": "L'anglais du touriste francophone, pour une semaine à Toronto.",
        "lang": "fr-CA", "dir": "ltr", "start_url": base, "scope": base,
        "display": "standalone", "orientation": "portrait",
        "background_color": "#FFFFFF", "theme_color": "#FFFFFF",
        "icons": [{"src": base + "icones/icone-192.png", "sizes": "192x192", "type": "image/png", "purpose": "any"},
                  {"src": base + "icones/icone-512.png", "sizes": "512x512", "type": "image/png", "purpose": "any"},
                  {"src": base + "icones/icone-maskable-512.png", "sizes": "512x512", "type": "image/png", "purpose": "maskable"}],
    }, ensure_ascii=False, indent=2), encoding="utf-8")


def main():
    icones()
    D, n, total = donnees()
    svg, regles = plan_ville()
    page = (GABARIT.replace("%%DONNEES%%", json.dumps(D, ensure_ascii=False, separators=(",", ":")))
            .replace("%%PLAN%%", svg).replace("/*%%PLAN_CSS%%*/", regles))
    SORTIE.parent.mkdir(parents=True, exist_ok=True)
    SORTIE.write_text(page, encoding="utf-8")
    print(f"{SORTIE.relative_to(RACINE)}  {len(page)//1024} Ko — sons {n}/{total}")


GABARIT = r"""<!DOCTYPE html>
<html lang="fr">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>Une semaine à Toronto</title>
<meta name="description" content="L'anglais du touriste francophone, pour une semaine à Toronto.">
<link rel="stylesheet" href="/assets/design-system/styles.css">
<link rel="stylesheet" href="/assets/design-system/marque-francis.css">
<link rel="icon" href="/assets/design-system/marque-francis-favicon.svg">
<link rel="manifest" href="/modules-autonomes/toronto/manifest.webmanifest">
<link rel="apple-touch-icon" href="/modules-autonomes/toronto/icones/icone-180.png">
<meta name="theme-color" content="#FFFFFF">
<meta name="robots" content="noindex">
<style>
/* Page produite par build/toronto_app.py — ne pas l'éditer. */
/* La carte postale : un brun d'encre (#7A3B1D), réservé à la progression ; l'action
   reste le vert de francis. Le rouge du tramway marque la ville sur l'en-tête. */
:root{--carte:#7A3B1D;--carte-bg:#FBF3EC;--ville:#C8102E}
*{box-sizing:border-box}
[hidden]{display:none!important}
html{-webkit-text-size-adjust:100%}
body{margin:0;background:var(--surface-page,#F7F7F5);color:var(--text-body,#2B2D31);
  font-family:Nunito,system-ui,sans-serif;font-size:17px;line-height:1.5}
.fr-barre .fr-barre__in{max-width:760px;padding-left:16px;padding-right:16px}
.secteur{display:flex;flex-direction:column;align-items:flex-end;text-align:right;line-height:1.15}
.secteur small{font-size:11px;font-weight:800;letter-spacing:.08em;text-transform:uppercase;color:var(--text-muted)}
.secteur b{font-size:17px;font-weight:900;color:var(--ville)}
@media (max-width:480px){.secteur small{display:none}.secteur b{font-size:15px}}
main{max-width:760px;margin:0 auto;padding:14px 16px 90px}
h1{font-size:28px;line-height:1.15;margin:6px 0 6px;color:var(--text-strong)}
h2{font-size:21px;line-height:1.2;margin:22px 0 10px;color:var(--text-strong)}
p{margin:0 0 10px}
.muted{color:var(--text-muted)}
.surtitre{font-size:13px;font-weight:800;letter-spacing:.08em;text-transform:uppercase;color:var(--text-muted);margin:0}
button{font:inherit}
.btn{font-weight:800;font-size:16px;cursor:pointer;border-radius:12px;padding:10px 16px;min-height:48px;
  border:1px solid var(--line-300,#D6D6D2);background:var(--surface-card,#fff);color:var(--text-strong);
  display:inline-flex;gap:8px;align-items:center;justify-content:center;text-decoration:none}
.btn--pri{background:var(--accent);border-color:var(--accent);color:#fff}
.btn--large{width:100%;white-space:normal;line-height:1.25}
.btn--son{background:var(--audio);border-color:var(--audio);color:#fff;min-width:48px;padding:10px 12px}
.btn--petit{min-height:44px;padding:6px 12px;font-size:14.5px}
.btn svg{width:20px;height:20px;flex:none}
.btn[disabled]{opacity:.45;cursor:not-allowed}
.rangee{display:flex;flex-wrap:wrap;gap:10px;align-items:center}
.carte{background:var(--surface-card,#fff);border:1px solid var(--line-200,#E8E8E4);border-radius:16px;padding:16px}
.retour{display:inline-flex;align-items:center;gap:6px;font-weight:800;font-size:15px;color:var(--text-muted);
  background:none;border:0;padding:8px 0;cursor:pointer;min-height:44px}
.retour svg{width:18px;height:18px}
#app a{color:var(--text-accent)}
.acc{background:#fff;border:1px solid var(--line-200);border-radius:18px;padding:16px;margin:14px 0}
.acc--carte{background:var(--carte-bg);border-color:#E7D3C3}
.acc h2{margin:2px 0 6px}
.valise{display:grid;grid-template-columns:repeat(4,minmax(0,1fr));gap:6px;margin:10px 0}
.valise span{aspect-ratio:3/2;border:1.5px dashed #D7BFAE;border-radius:6px;display:grid;place-items:center;font-weight:900;color:#B79A86;background:#fff}
.valise span.fait{border:1.5px solid var(--carte);background:var(--carte);color:#fff}
.ariane{list-style:none;padding:0;margin:12px 0 14px;display:flex}
.ariane li{flex:1;position:relative;text-align:center;min-width:0}
.ariane li+li::before{content:"";position:absolute;top:17px;right:calc(50% + 19px);left:calc(-50% + 19px);height:3px;border-radius:2px;background:var(--line-200)}
.ariane li.relie::before{background:var(--ok-line,#2E7D4F)}
.ariane button{background:none;border:0;padding:0;font:inherit;color:inherit;cursor:pointer;display:flex;flex-direction:column;align-items:center;gap:5px;width:100%}
.ariane button:disabled{cursor:not-allowed}
.ariane .rond{width:36px;height:36px;border-radius:50%;display:grid;place-items:center;font-weight:900;font-size:16px;background:#fff;border:2px solid var(--carte);color:var(--carte);position:relative;z-index:1}
.ariane .lib{font-size:13px;font-weight:800;line-height:1.2}
.ariane li.fait .rond{background:var(--ok-line,#2E7D4F);border-color:var(--ok-line,#2E7D4F);color:#fff}
.ariane li.ici .rond{background:var(--carte);color:#fff;box-shadow:0 0 0 4px rgba(122,59,29,.2)}
.ariane li.ferme .rond{border-color:var(--line-300);color:var(--text-muted);background:#F3F0E8}
.ariane li.ferme .lib{color:var(--text-muted);font-weight:700}
.fil-legende{font-size:14.5px;color:var(--text-muted);margin:-4px 0 12px;text-align:center}
.meca{background:#fff;border:1px solid var(--line-200);border-left:4px solid var(--carte);border-radius:12px;padding:10px 14px;margin:10px 0 14px}
.meca ul{margin:6px 0 0;padding-left:18px}.meca li{margin:5px 0;font-size:15.5px;line-height:1.5}
.objectif{background:var(--carte-bg);border:1px solid #E7D3C3;border-radius:12px;padding:10px 12px;margin:10px 0;font-size:15.5px;color:#4A2412}
.etapes-j{list-style:none;padding:0;margin:14px 0 0;display:flex;flex-direction:column;gap:8px}
.etapes-j button{width:100%;display:flex;align-items:center;gap:12px;text-align:left;background:#fff;border:1px solid var(--line-200);
  border-radius:14px;padding:12px 14px;cursor:pointer;min-height:60px}
.etapes-j .num{width:32px;height:32px;border-radius:50%;display:flex;align-items:center;justify-content:center;font-weight:900;
  background:var(--surface-sunken,#FBFBFA);border:1px solid var(--line-200);flex:none;font-size:14px}
.etapes-j .fait .num{background:var(--ok-bg);border-color:var(--ok-line);color:var(--ok-ink)}
.etapes-j b{display:block;color:var(--text-strong)}
.etapes-j span.d{font-size:13.5px;color:var(--text-muted);display:block;line-height:1.3}
.etat{margin-left:auto;font-size:12.5px;font-weight:800;color:var(--ok-ink);white-space:nowrap}
.ph{display:flex;gap:10px;align-items:center;padding:10px 14px;border-top:1px solid var(--line-200)}
.ph:first-child{border-top:0}
.ph .t{flex:1;min-width:0}
.ph .t b{display:block;color:var(--text-strong);font-size:16.5px;line-height:1.25}
.ph .t span{font-size:14px;color:var(--text-muted)}
.liste-ecoute{padding:4px 0}
.grille{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:10px}
@media (min-width:600px){.grille{grid-template-columns:repeat(3,minmax(0,1fr))}}
.mot{background:#fff;border:1px solid var(--line-200);border-radius:14px;padding:10px;display:flex;flex-direction:column;gap:4px;cursor:pointer;text-align:left;min-width:0;font:inherit}
.mot img{width:100%;aspect-ratio:1;object-fit:contain}
.mot .en{font-weight:900;font-size:16.5px;color:var(--text-strong);line-height:1.2;overflow-wrap:anywhere}
.mot .fr{font-size:14px;color:var(--text-muted);line-height:1.25}
.mot .piege{font-size:11.5px;font-weight:900;letter-spacing:.06em;text-transform:uppercase;color:var(--warn-ink);background:var(--warn-bg);
  border:1px solid var(--warn-line);border-radius:99px;padding:1px 8px;align-self:flex-start}
.consigne{font-size:15.5px;color:var(--text-muted);margin:0 0 10px}
.progres{height:8px;background:#EEE9DA;border-radius:99px;overflow:hidden;margin:6px 0 14px}
.progres i{display:block;height:100%;background:var(--carte);border-radius:99px;transition:width .3s}
.choix{display:flex;flex-direction:column;gap:8px;margin:10px 0}
.choix button{text-align:left;background:#fff;border:1.5px solid var(--line-300,#D6D6D2);border-radius:12px;padding:12px 14px;
  cursor:pointer;min-height:52px;font-size:16.5px;color:var(--text-strong);line-height:1.3}
.choix button.juste::before{content:"✓ ";font-weight:900}
.choix button.juste{border-color:var(--ok-line);background:var(--ok-bg);color:var(--ok-ink)}
.choix button.faux::before{content:"✕ ";font-weight:900}
.choix button.faux{border-color:var(--no-line);background:var(--no-bg);color:var(--no-ink);cursor:default}
.retro{border-radius:10px;padding:10px 12px;margin:8px 0;font-size:15.5px}
.retro.ok{background:var(--ok-bg);border:1px solid var(--ok-line);color:var(--ok-ink)}
.retro.no{background:var(--no-bg);border:1px solid var(--no-line);color:var(--no-ink)}
.retro.info{background:var(--carte-bg);border:1px solid #E7D3C3;color:#4A2412}
.gros-son{display:flex;justify-content:center;margin:10px 0 4px}
.gros-son .btn--son{width:84px;height:84px;border-radius:50%}
.gros-son .btn--son svg{width:36px;height:36px}
.phrase-en{font-size:21px;font-weight:900;color:var(--text-strong);line-height:1.3;margin:6px 0}
.micro{display:flex;flex-direction:column;align-items:center;gap:8px;margin:12px 0}
.micro .btn-micro{width:84px;height:84px;border-radius:50%;background:var(--surface-inverse,#17181A);color:#fff;border:0;cursor:pointer;display:flex;align-items:center;justify-content:center}
.micro .btn-micro svg{width:34px;height:34px}
.micro .btn-micro.ecoute{background:var(--audio);animation:pouls 1.2s infinite}
@keyframes pouls{0%{box-shadow:0 0 0 0 rgba(220,38,38,.45)}70%{box-shadow:0 0 0 16px rgba(220,38,38,0)}100%{box-shadow:0 0 0 0 rgba(220,38,38,0)}}
.entendu{font-size:15.5px;min-height:24px;text-align:center;color:var(--text-body)}
.scene-tete{display:flex;gap:12px;align-items:center;margin:4px 0 10px}
.rappel{font-size:12.5px;font-weight:900;letter-spacing:.06em;text-transform:uppercase;color:#7A5A45;background:var(--carte-bg);border:1px solid #E7D3C3;border-radius:99px;padding:2px 10px;display:inline-block;margin-bottom:6px}
.regle{border:1px dashed var(--warn-line);background:var(--warn-bg);color:var(--warn-ink);border-radius:12px;padding:10px 12px;font-size:15px;margin:8px 0}
.aide-bascule{display:flex;align-items:center;gap:8px;min-height:44px;font-size:15px;font-weight:800;color:var(--text-body);margin:6px 0;cursor:pointer}
.aide-bascule input{width:22px;height:22px}
.avis-fond{position:fixed;inset:0;background:rgba(19,35,59,.55);display:grid;place-items:center;padding:16px;z-index:50}
.avis-micro{background:#fff;border-radius:16px;padding:18px;max-width:440px;width:100%;box-shadow:0 16px 40px rgba(0,0,0,.3)}
.avis-micro h3{margin:0 0 8px}.avis-micro p{margin:0 0 10px;font-size:15.5px}
.sans-son{background:var(--warn-bg);border:1px solid var(--warn-line);color:var(--warn-ink);border-radius:12px;padding:10px 12px;font-size:14.5px;margin:0 0 12px}
.pied{max-width:720px;margin:24px auto 0;padding:14px 16px 28px;text-align:center;font-size:13.5px;color:var(--text-muted)}
.pied a{color:var(--text-muted)}
.avis-local{font-size:13px;color:var(--text-muted)}
/* Étape 2 : les planches */
.pl-liste{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:10px}
.pl-liste button{display:flex;flex-direction:column;gap:2px;text-align:left;background:#fff;border:1px solid var(--line-200);border-left:4px solid var(--carte);
  border-radius:14px;padding:12px;cursor:pointer;min-height:72px;font:inherit;color:var(--text-body)}
.pl-liste b{font-size:16px;color:var(--text-strong)}.pl-liste span{font-size:13px;color:var(--text-muted)}
.mot .vis{aspect-ratio:1;border-radius:10px;background:#fff;display:flex;align-items:center;justify-content:center;overflow:hidden}
.mot .vis img{width:100%;height:100%;object-fit:contain}
.mot .vis svg{width:62%;height:62%}
.mot .vis.vide{background:var(--carte-bg);color:#D7BFAE}.mot .vis.vide svg{width:36%;height:36%}
.mot .note{font-size:12.5px;line-height:1.35;color:var(--text-muted)}
.mot.piege-m{border-color:var(--warn-line)}
.bascule-sens{margin:0 0 12px}
.mini-plan{width:100%;max-width:360px;display:block;margin:6px auto 4px}
.mini-plan .rue-g{stroke:#D8D3CC;stroke-width:9;stroke-linecap:round}
.mini-plan .lettre{font:900 14px Nunito,system-ui,sans-serif;fill:#7A3B1D}
.mini-plan .nord{font:800 12px Nunito,system-ui,sans-serif;fill:var(--text-muted)}
/* Étape 3 : le plan de la ville et l'album des cartes postales */
/*%%PLAN_CSS%%*/
.album{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:12px}
.cp-carte{background:#fff;border:1px solid #E7D3C3;border-radius:6px;padding:6px;box-shadow:0 2px 0 #E7D3C3;font:inherit;text-align:left;cursor:pointer;color:inherit;display:block;width:100%}
.cp-recto{aspect-ratio:3/2;border-radius:3px;overflow:hidden;display:flex;align-items:flex-end;position:relative;background:linear-gradient(160deg,#F4E6D9,#E7CDB8)}
.cp-recto img{width:100%;height:100%;object-fit:cover;position:absolute;inset:0}
.cp-recto b{position:relative;margin:6px 8px;font-size:15px;color:#4A2412;background:rgba(255,255,255,.85);border-radius:4px;padding:1px 6px}
.cp-carte.a-gagner .cp-recto{filter:grayscale(1);opacity:.55}
.cp-carte small{display:block;font-size:12.5px;color:var(--text-muted);margin:6px 2px 0}
.cp-n{position:absolute;top:6px;left:6px;width:24px;height:24px;border-radius:3px;background:#fff;border:1.5px solid var(--carte);color:var(--carte);font-size:12px;font-weight:900;display:grid;place-items:center}
.verso{background:#FFFDF8;border:1px solid #E7D3C3;border-radius:6px;padding:14px;display:grid;grid-template-columns:1fr 1fr;gap:14px;min-height:180px;margin-top:12px}
.verso .msg{border-right:1px solid #E7D3C3;padding-right:12px;font-size:15px;color:var(--text-muted)}
.verso .timbre{justify-self:end;width:54px;height:64px;border:2px dashed #C8102E;border-radius:3px;display:grid;place-items:center;color:#C8102E;font-size:11px;font-weight:900;text-align:center}
.verso .lignes{border-bottom:1px solid #D7BFAE;height:26px}
.verso .ecrit{font-family:"Segoe Print","Bradley Hand",cursive;font-size:16px;color:#1F2A44;white-space:pre-wrap;line-height:26px}
/* La semaine jouée (étape 5) */
.scene-tete img{width:64px;height:64px;border-radius:50%;object-fit:cover;border:2px solid #fff;box-shadow:0 0 0 1px var(--line-200)}
.fil{display:flex;flex-direction:column;gap:10px}
.bulle{max-width:88%;border-radius:16px;padding:10px 12px;background:#fff;border:1px solid var(--line-200)}
.bulle.lui{align-self:flex-start;border-top-left-radius:4px}
.bulle.moi{align-self:flex-end;background:var(--carte-bg);border-color:#E7D3C3;border-top-right-radius:4px}
.bulle .qui{font-size:13px;font-weight:900;letter-spacing:.05em;text-transform:uppercase;color:var(--text-muted)}
.bulle .en{font-size:17px;color:var(--text-strong);font-weight:700}
.bulle.cache .en{filter:blur(6px);user-select:none}
.saisie-txt{flex:1;min-width:0;font:inherit;padding:10px;border-radius:10px;border:1px solid var(--line-300)}
.code-champ{font:inherit;font-size:20px;letter-spacing:.2em;padding:10px;border-radius:10px;border:1px solid var(--line-300);width:10em;text-transform:uppercase}
.code-achat{font-size:32px;font-weight:900;letter-spacing:.16em;text-align:center;background:#fff;border:2px dashed var(--carte);color:var(--carte);border-radius:14px;padding:14px;margin:12px 0}
details.rub{background:#fff;border:1px solid var(--line-200);border-radius:12px}
details.rub summary{cursor:pointer;padding:12px 14px;font-weight:800;display:flex;justify-content:space-between;gap:10px}
.prix-barre{color:var(--text-muted);font-weight:700}
.avis-local{font-size:14px;color:var(--text-muted);margin:6px 0 0}
.geste{display:flex;gap:8px;align-items:baseline;margin:4px 0;font-size:15.5px}
.geste b{flex:none;width:1.2em}
.carte-postale-txt{width:100%;min-height:96px;font:inherit;font-size:17px;padding:10px;border-radius:10px;border:1px solid var(--line-300)}
/* La poche (étape 6) */
.ph{display:flex;gap:10px;align-items:center;padding:8px 12px;border-top:1px solid var(--line-200)}
.ph .t{flex:1;min-width:0;display:flex;flex-direction:column}.ph .t b{color:var(--text-strong);font-size:16.5px}.ph .t span{font-size:14.5px;color:var(--text-muted)}
.ph-tete{background:var(--carte-bg)}.ph-tete b{font-size:13px;letter-spacing:.06em;text-transform:uppercase;color:var(--carte)}
details.rub{margin:8px 0}details.rub summary span{color:var(--text-muted);font-weight:700}
.calc{padding:4px 14px 14px}.calc label{display:flex;flex-direction:column;gap:6px;font-weight:800;margin-bottom:10px}
.calc input{font:inherit;font-size:22px;padding:10px;border-radius:10px;border:1px solid var(--line-300);max-width:12em}
.calcul{font-size:18px;margin-top:10px;min-height:28px;color:var(--text-strong)}.calcul b{font-size:22px}
.montrer{position:fixed;inset:0;background:#fff;z-index:50;display:flex;flex-direction:column;align-items:center;justify-content:center;padding:24px;text-align:center}
.montrer .fermer{position:absolute;top:14px;right:14px}
.montrer .grand{font-size:clamp(30px,8vw,52px);font-weight:900;line-height:1.15;color:var(--text-strong)}
.montrer .petit{font-size:18px;color:var(--text-muted);margin-top:16px}
.cf-bref ul{margin:0;padding-left:20px}.cf-bref li{margin:6px 0}
.cf-ligne{margin:8px 0}.cf-ligne dl{display:grid;grid-template-columns:auto 1fr;gap:4px 12px;margin:8px 0 0;font-size:15px}
.cf-ligne dt{color:var(--text-muted);font-weight:700}.cf-ligne dd{margin:0}.cf-hors{margin:6px 0}
@media (max-width:420px){.cf-ligne dl{grid-template-columns:1fr}.cf-ligne dt{margin-top:4px}}
.maya-jours{display:grid;grid-template-columns:repeat(auto-fill,minmax(150px,1fr));gap:8px}
</style>
</head>
<body>
<div class="fr-barre"><div class="fr-barre__in">
  <span class="fr-lockup"><span class="fr-nom" role="img" aria-label="francis">franc<span class="fr-i" aria-hidden="true">ı<span class="fr-point"></span></span>s</span><span class="fr-trait" aria-hidden="true"></span><span class="fr-desc">Aide à l'apprentissage de l'anglais</span></span>
  <span class="secteur"><small>Voyage · anglais</small><b>Une semaine à Toronto</b></span>
</div></div>
<main id="app"></main>
<footer class="pied"><a href="/modules-autonomes/toronto/presentation.html">Comment ça marche ?</a> · <a href="#avis">Donner mon avis</a> · <a href="#reglages">Réglages</a> · <a href="#confidentialite">Confidentialité</a></footer>
<audio id="lecteur" preload="none"></audio>
<script>
const D = %%DONNEES%%;
const SONS = new Set(D.sons);
const BASE = '/assets/interactive/toronto/';
const E = s => String(s).replace(/[&<>"]/g, c => ({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;'}[c]));
const $ = s => document.querySelector(s);
const ICO = {
  son:'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"><path d="M11 5 6 9H3v6h3l5 4V5z"/><path d="M15.5 8.5a5 5 0 0 1 0 7"/><path d="M18.5 5.5a9 9 0 0 1 0 13"/></svg>',
  retour:'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round"><path d="M15 18l-6-6 6-6"/></svg>',
  micro:'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"><rect x="9" y="3" width="6" height="11" rx="3"/><path d="M5 11a7 7 0 0 0 14 0"/><path d="M12 18v3"/></svg>',
  stop:'<svg viewBox="0 0 24 24" fill="currentColor"><rect x="6" y="6" width="12" height="12" rx="2"/></svg>',
  test:'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M9 11l3 3L22 4"/><path d="M21 12v7a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2V5a2 2 0 0 1 2-2h11"/></svg>'
};
const LIEUX = {union: 'à Union Station, le premier jour', cafe: 'au café, le premier matin', hotel: 'à la réception de l’hôtel', kensington: 'dans Kensington, quand vous chercherez votre chemin'};

/* ---------- l'état, dans ce téléphone seulement ---------- */
const CLE = 'toronto:v1';
let S = {lent:false, aide:false, prep:{}};
try { Object.assign(S, JSON.parse(localStorage.getItem(CLE) || '{}')); } catch(e) {}
function sauver(){ try { localStorage.setItem(CLE, JSON.stringify(S)); } catch(e) {} }
const aujourdhui = () => new Date().toLocaleDateString('fr-CA', {day:'numeric', month:'short', year:'numeric'}).replace(/^1 /, '1er ');

/* ---------- le son ---------- */
const lecteur = $('#lecteur');
function jouer(fichier, naturel){
  return new Promise(res => {
    if (!fichier || !SONS.has(fichier)) { res(false); return; }
    arreterMicro(); lecteur.pause();
    lecteur.src = BASE + 'sons/' + fichier + '?v=' + D.v;
    // Le ralenti étire dans le navigateur, sans changer la hauteur : les fichiers
    // restent au débit naturel (mémoire bouton-vitesse-voix).
    lecteur.playbackRate = (S.lent && !naturel) ? 0.8 : 1; lecteur.preservesPitch = true;
    lecteur.onended = () => res(true); lecteur.onerror = () => res(false);
    const p = lecteur.play(); if (p && p.catch) p.catch(() => res(false));
  });
}
const SANS_SON = !D.sons.length;

/* ---------- le micro (reconnaissance du navigateur, en en-CA) ---------- */
const Reco = window.SpeechRecognition || window.webkitSpeechRecognition;
let recoActive = null, micRefuse = false, micErreur = '';
function arreterMicro(){ if (recoActive) { const r = recoActive; try { r.stop(); } catch(e) {} if (r.terminer) setTimeout(r.terminer, 1500); } }
const rienEntendu = sinon => {
  const repli = 'Dites la phrase à voix haute, puis touchez « C’est dit ! ».';
  if (micRefuse) return 'Micro fermé, comme vous l’avez choisi. ' + repli;
  if (micErreur === 'not-allowed' || micErreur === 'service-not-allowed')
    return 'Le navigateur bloque le micro. Touchez l’icône à gauche de l’adresse du site, choisissez « Autoriser » pour le micro, puis réessayez. Sinon : ' + repli.charAt(0).toLowerCase() + repli.slice(1);
  if (micErreur === 'audio-capture') return 'Aucun micro trouvé sur cet appareil. ' + repli;
  if (micErreur === 'network') return 'La reconnaissance de la voix demande une connexion Internet. ' + repli;
  return sinon;
};
function fournisseurVoix(){
  const u = navigator.userAgent;
  if (/Edg\//.test(u)) return 'Microsoft (Edge)';
  if (/Chrome|CriOS|Android/.test(u)) return 'Google (Chrome)';
  if (/Safari|iPhone|iPad|Macintosh/.test(u)) return 'Apple (Safari)';
  return 'l’éditeur de votre navigateur';
}
/* Loi 25 : avant le premier usage, dire où va la voix — chez le fournisseur du
   navigateur, pas chez nous. Accepté une fois, gardé dans le téléphone. */
function ecouterMicro(surTexte, surFin){
  if (S.avisMicro) return ouvrirMicro(surTexte, surFin);
  const fond = document.createElement('div'); fond.className = 'avis-fond';
  fond.innerHTML = `<div class="avis-micro" role="dialog" aria-modal="true" aria-labelledby="avisT">
    <h3 id="avisT">Avant d'ouvrir le micro</h3>
    <p>Pour comprendre ce que vous dites, l'application utilise la reconnaissance vocale de <b>votre navigateur</b>.
    Votre voix est donc envoyée à <b>${fournisseurVoix()}</b>, aux États-Unis, qui la transcrit et renvoie le texte.</p>
    <p>Nous ne recevons pas votre voix et ne l'enregistrons pas. Le texte reste dans votre téléphone.</p>
    <p class="muted" style="font-size:14px">Vous préférez ne pas l'utiliser ? Tout se fait aussi sans micro : dites la phrase à voix haute, puis touchez « C’est dit ! » — elle n’est alors pas vérifiée.</p>
    <div class="rangee"><button class="btn btn--pri" id="avisOui">J'ai compris, ouvrir le micro</button><button class="btn" id="avisNon">Pas maintenant</button></div></div>`;
  document.body.appendChild(fond);
  fond.querySelector('#avisOui').onclick = () => { S.avisMicro = aujourdhui(); sauver(); fond.remove(); ouvrirMicro(surTexte, surFin); };
  fond.querySelector('#avisNon').onclick = () => { fond.remove(); micRefuse = true; surFin(''); micRefuse = false; };
  fond.querySelector('#avisOui').focus();
}
function ouvrirMicro(surTexte, surFin){
  // Reconnaissance continue qui accumule ; fin sur « Arrêter » ou 4 s de silence
  // (9 s avant le premier mot). Une seule fin, quoi qu'il arrive (leçon de Compostelle).
  const r = new Reco(); r.lang = 'en-CA'; r.continuous = true; r.interimResults = true;
  let final = '', minuterie = null, fini = false;
  const terminer = () => { if (fini) return; fini = true; clearTimeout(minuterie); if (recoActive === r) recoActive = null; surFin(final.trim()); };
  r.terminer = terminer;
  const relancer = d => { clearTimeout(minuterie); minuterie = setTimeout(() => { try { r.stop(); } catch(e) {} setTimeout(terminer, 1500); }, d); };
  r.onresult = ev => { let prov = '';
    for (let i = ev.resultIndex; i < ev.results.length; i++) {
      if (ev.results[i].isFinal) final += ev.results[i][0].transcript + ' '; else prov += ev.results[i][0].transcript; }
    surTexte((final + prov).trim()); relancer(4000); };
  micErreur = '';
  r.onerror = e => { if (e && e.error && e.error !== 'aborted' && e.error !== 'no-speech') micErreur = e.error; setTimeout(terminer, 300); };
  r.onend = terminer;
  recoActive = r; lecteur.pause();
  try { r.start(); relancer(9000); } catch(e) { terminer(); }
}
/* La reconnaissance anglaise écrit les nombres en chiffres (« 2 coffees », « $13.50 »,
   « 10:30 ») : on les remet en lettres avant de comparer, comme preparation.py le fait. */
const UN = 'zero one two three four five six seven eight nine ten eleven twelve thirteen fourteen fifteen sixteen seventeen eighteen nineteen'.split(' ');
const DIZ = {2:'twenty',3:'thirty',4:'forty',5:'fifty',6:'sixty',7:'seventy',8:'eighty',9:'ninety'};
function nombreEn(n){ n = +n; if (n < 20) return UN[n]; if (n < 100) return DIZ[Math.floor(n / 10)] + (n % 10 ? ' ' + UN[n % 10] : ''); return String(n); }
const enLettres = t => String(t)
  .replace(/(\d{1,2}):(\d{2})/g, (_, h, m) => nombreEn(h) + (+m ? ' ' + nombreEn(m) : ''))
  .replace(/\$\s*(\d+)\.(\d{2})/g, (_, a, b) => nombreEn(a) + ' ' + nombreEn(b))
  .replace(/\d+/g, n => ' ' + nombreEn(n) + ' ');
const plat = t => enLettres(String(t).replace(/['’]/g, ' ')).toLowerCase().normalize('NFD').replace(/[̀-ͯ]/g, '').replace(/[^a-z0-9 ]+/g, ' ').replace(/\s+/g, ' ').trim();
// Une clé qui commence par « ~ » est une expression régulière sur le texte aplati.
const trouve = (t, cle) => cle.startsWith('~') ? new RegExp(cle.slice(1)).test(plat(t)) : cle.split('|').some(a => new RegExp('(^| )' + plat(a).replace(/[.*+?^${}()|[\]\\]/g, '\\$&') + '(s|es)?( |$)').test(plat(t)));
/* ---------- ordre des choix : jamais la bonne toujours au même rang ---------- */
// Audit tour 2 : une rotation garde l'ordre cyclique (la bonne précède toujours le leurre). Mélange à graine stable.
function ordre(n, g){ const o = [...Array(n).keys()]; g = g + 1; for (let i = n - 1; i > 0; i--) { g = (g * 16807) % 2147483647; const j = g % (i + 1); [o[i], o[j]] = [o[j], o[i]]; } return o; }

/* ---------- navigation ---------- */
const app = $('#app');
function aller(h){ location.hash = h; }
function retour(h, t){ return `<button class="retour" onclick="aller('${h}')">${ICO.retour} ${E(t)}</button>`; }
function rendre(){
  window.scrollTo(0, 0); arreterMicro(); lecteur.pause(); voixEnCours = null; try { speechSynthesis.cancel(); } catch(e) {}
  const p = (location.hash.slice(1) || 'accueil').split('/');
  if (p[0] !== 'avis') { try { sessionStorage.setItem('toronto:vu', location.hash); } catch(e) {} }
  if (p[0] === 'avis') return vueAvis();
  if (p[0] === 'confidentialite') return vueConfidentialite();
  if (p[0] === 'prep') return p[1] === 'test' ? vuePrepTest() : p[1] ? vueSeance(p[1], p[2]) : vuePrep();
  if (p[0] === 'reglages') return vueReglages();
  if (p[0] === 'mots') return p[1] ? vuePlanche(p[1]) : vueMots();
  if (p[0] === 'pieges') return vuePieges();
  if (p[0] === 'semaine') return p[2] === 'jouer' ? vueJouer(p[1]) : p[2] === 'ecrire' ? vueEcrire(p[1]) : p[1] ? vueCarte(p[1]) : vueSemaine();
  if (p[0] === 'maya') return vueJouer(p[1]);
  if (p[0] === 'poche') return vuePoche();
  if (p[0] === 'achat') return vueAchat(p[1]);
  if (p[0] === 'achat-annule') return vueAchatAnnule();
  if (p[0] === 'exos') return p[1] ? vueFamille(p[1]) : vueExos();
  return vueAccueil();
}
window.addEventListener('hashchange', rendre);

/* ---------- l'accueil ---------- */
function vueAccueil(){
  const n = prepFaites(), tot = D.prep.seances.length, pro = prepProchaine(), t = S.prep.test || {};
  app.innerHTML = `<p class="surtitre">Voyage · anglais</p><h1>Une semaine à Toronto</h1>
    <p>Arriver, prendre le métro, s'installer à l'hôtel, commander, visiter, manger au restaurant, bavarder avec les gens de la ville :
    l'anglais qu'il vous faut pour une semaine à Toronto, à préparer chez vous, quinze minutes à la fois.</p>
    ${SANS_SON ? '<div class="sans-son">Version de travail : les voix ne sont pas encore enregistrées. Les écrans se parcourent, mais rien ne se fait entendre.</div>' : ''}
    <section class="acc acc--carte">
      <p class="surtitre">1 · Avant de partir</p><h2>Faire ma valise</h2>
      <p>Huit séances de quinze minutes : les sons de l'anglais, les politesses, les prix, l'heure, les demandes, les questions,
      se présenter, et surtout <b>comprendre la réponse</b>.</p>
      <div class="valise" aria-label="${n} séances faites sur ${tot}">${D.prep.seances.map((x, i) => `<span class="${prepEtat(x.id).fin ? 'fait' : ''}">${prepEtat(x.id).fin ? '✓' : i + 1}</span>`).join('')}</div>
      ${pro ? `<button class="btn btn--pri btn--large" onclick="aller('prep/${pro.id}')">${n ? 'Continuer' : 'Commencer'} : séance ${n + 1}, ${E(pro.titre.toLowerCase())}</button>`
            : `<div class="retro ok">✓ Les huit séances sont faites.</div>`}
      <button class="btn btn--large" style="margin-top:8px" onclick="aller('prep')">Les huit séances</button>
    </section>
    <section class="acc">
      <p class="surtitre">Vous avez déjà de l'anglais ?</p><h2>Prêt à partir ?</h2>
      <p>${D.prep.test[0].length} questions, un quart d'heure, avec le son et le micro. Le test vous situe ; « Solide » partout, et vous pouvez
      sauter les séances.${t.dernier ? ' Dernier passage : ' + E(t.dernier) + '.' : ''}</p>
      <button class="btn btn--large" onclick="aller('prep/test')">${ICO.test} Faire le test</button>
    </section>
    <section class="acc">
      <p class="surtitre">S'exercer</p><h2>Les exercices de la semaine</h2>
      <p>Comprendre la réponse, les prix et les heures, le total à payer, suivre un chemin, le dire au micro : par séries courtes, dans
      les lieux de la semaine.</p>
      <button class="btn btn--pri btn--large" onclick="aller('exos')">Les exercices</button>
    </section>
    <section class="acc">
      <p class="surtitre">Les mots</p><h2>Douze planches</h2>
      <p>Près de deux cents mots du voyage, avec leur voix : se déplacer, l'hôtel, le café, le restaurant, payer, visiter… et les
      faux amis qui trompent un francophone.</p>
      <div class="rangee"><button class="btn btn--pri" style="flex:1" onclick="aller('mots')">Les planches</button>
      <button class="btn" style="flex:1" onclick="aller('pieges')">Les faux amis</button></div>
    </section>
    <section class="acc">
      <p class="surtitre">2 · La semaine</p><h2>Dix lieux, dix cartes postales</h2>
      <p class="muted">Union Station, l'hôtel, le café, la tour CN, le marché St. Lawrence, Kensington, les îles, la pharmacie,
      le restaurant, le départ. Chaque lieu se joue avec l'assistance, qui tient le rôle de la personne en anglais ; une situation
      réussie vous donne sa carte postale.</p>
      <button class="btn btn--pri btn--large" onclick="aller('semaine')">Jouer la semaine</button>
    </section>
    <section class="acc">
      <p class="surtitre">3 · Sur place</p><h2>Ma poche</h2>
      <p>Les phrases de chaque lieu avec leur voix, même sans réseau ; les urgences ; « plus lentement, s'il vous plaît » à
      montrer en grand ; et ce que ça coûte vraiment, taxe et pourboire compris.</p>
      <button class="btn btn--large" onclick="aller('poche')">Ouvrir ma poche</button>
    </section>`;
}

/* ---------- avant de partir : huit séances et « Prêt à partir ? » ---------- */
const PREP_TEMPS = [['ecoute', 'J’écoute', 'Les phrases et les mots, avec leur voix'],
                    ['quiz', 'Je reconnais', 'J’entends, je choisis'],
                    ['dire', 'Je le dis', 'Au micro, puis le modèle']];
function prepEtat(id){ if (!S.prep) S.prep = {}; return S.prep[id] || (S.prep[id] = {faits:{}, fin:null}); }
const seanceParId = id => D.prep.seances.find(x => x.id === id);
const prepFaites = () => D.prep.seances.filter(x => prepEtat(x.id).fin).length;
const prepProchaine = () => D.prep.seances.find(x => !prepEtat(x.id).fin) || null;
const numSeance = x => D.prep.seances.indexOf(x) + 1;
function vuePrep(){
  const n = prepFaites(), pro = prepProchaine();
  const liste = D.prep.seances.map((x, i) => { const e = prepEtat(x.id);
    return `<li class="${e.fin ? 'fait' : ''}"><button onclick="aller('prep/${x.id}')"><span class="num">${e.fin ? '✓' : i + 1}</span>
      <span><b>${E(x.titre)}</b><span class="d">${E(D.prep.objectifs[x.obj])} · ${x.minutes} min</span></span>${e.fin ? '<span class="etat">✓ faite</span>' : ''}</button></li>`; }).join('');
  app.innerHTML = `${retour('accueil', 'Accueil')}<p class="surtitre">1 · Avant de partir · ${n} sur ${D.prep.seances.length}</p>
  <h1>Faire ma valise</h1>
  <p>Huit séances de quinze minutes, dans l'ordre, dans les semaines qui précèdent le départ. Chacune a trois temps : on écoute, on
  reconnaît, puis on le dit au micro. Rien n'est fermé : si vous avez déjà de l'anglais, passez le test et sautez ce que vous savez.</p>
  ${pro ? `<button class="btn btn--pri btn--large" style="margin:6px 0 4px" onclick="aller('prep/${pro.id}')">${n ? 'Continuer' : 'Commencer'} : ${E(pro.titre)}</button>` : ''}
  <ul class="etapes-j">${liste}</ul>
  <button class="btn btn--large" style="margin-top:14px" onclick="aller('prep/test')">${ICO.test} Le test « Prêt à partir ? »</button>`;
}
const CADENAS = '<svg viewBox="0 0 24 24" width="14" height="14" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><rect x="5" y="11" width="14" height="10" rx="2"/><path d="M8 11V8a4 4 0 0 1 8 0v3"/></svg>';
function tempsOuvert(x, j){ const e = prepEtat(x.id); return !!e.fin || PREP_TEMPS.slice(0, j).every(([t]) => e.faits[t]); }
function filSeance(x, actif){
  const e = prepEtat(x.id);
  return `<ol class="ariane" aria-label="Les temps de la séance">${PREP_TEMPS.map(([t, nom], j) => {
    const fait = !!e.faits[t], ouvert = tempsOuvert(x, j), ici = t === actif, avant = j > 0 && e.faits[PREP_TEMPS[j - 1][0]];
    const cls = [fait ? 'fait' : '', ici ? 'ici' : '', ouvert ? '' : 'ferme', avant ? 'relie' : ''].filter(Boolean).join(' ');
    return `<li class="${cls}"><button ${ouvert && !ici ? `onclick="aller('prep/${x.id}/${t}')"` : ''} ${ouvert ? '' : 'disabled'}
      ${ouvert ? '' : `title="D'abord : ${E(PREP_TEMPS[j - 1][1])}"`} ${ici ? 'aria-current="step"' : ''}><span class="rond">${fait ? '✓' : ouvert ? j + 1 : CADENAS}</span><span class="lib">${nom}</span></button></li>`; }).join('')}</ol>`;
}
function teteSeance(x, k){
  const i = PREP_TEMPS.findIndex(t => t[0] === k);
  return `${retour('prep/' + x.id, 'Séance ' + numSeance(x) + ' · ' + x.titre)}${filSeance(x, k)}<h1>${PREP_TEMPS[i][1]}</h1>`;
}
function finTemps(x, k){
  const e = prepEtat(x.id); e.faits[k] = true;
  if (PREP_TEMPS.every(([t]) => e.faits[t]) && !e.fin) e.fin = aujourdhui();
  sauver();
  const suivant = PREP_TEMPS.find(([t]) => !e.faits[t]);
  if (suivant) return `<button class="btn btn--pri btn--large" onclick="aller('prep/${x.id}/${suivant[0]}')">Suivant : ${suivant[1]}</button>`;
  const pro = prepProchaine();
  return `<div class="retro ok">✓ Séance terminée : ${prepFaites()} sur ${D.prep.seances.length} dans la valise.</div>
    ${pro ? `<button class="btn btn--pri btn--large" onclick="aller('prep/${pro.id}')">Séance suivante : ${E(pro.titre)}</button>` :
      `<button class="btn btn--pri btn--large" onclick="aller('prep/test')">Les huit sont faites : le test « Prêt à partir ? »</button>`}
    <button class="btn btn--large" style="margin-top:8px" onclick="aller('prep')">Ma valise</button>`;
}
function vueSeance(id, k){
  const x = seanceParId(id); if (!x) return vuePrep();
  const jk = PREP_TEMPS.findIndex(([t]) => t === k);
  if (jk > 0 && !tempsOuvert(x, jk)) { const f = PREP_TEMPS.find(([t]) => !prepEtat(x.id).faits[t]); history.replaceState(null, '', '#prep/' + x.id + '/' + f[0]); k = f[0]; }
  if (k === 'ecoute') return seanceEcoute(x);
  if (k === 'quiz') return seanceQuiz(x);
  if (k === 'dire') return seanceDire(x);
  const e = prepEtat(x.id), suivant = PREP_TEMPS.find(([t]) => !e.faits[t]) || PREP_TEMPS[0];
  app.innerHTML = `${retour('prep', 'Ma valise')}<p class="surtitre">Séance ${numSeance(x)} sur ${D.prep.seances.length} · ${x.minutes} minutes</p>
    <h1>${E(x.titre)}</h1><p>${E(x.intro)}</p>
    ${filSeance(x, e.fin ? null : suivant[0])}
    <p class="fil-legende">${e.fin ? '✓ Séance faite. Refaites le temps de votre choix.' : 'Dans l’ordre : on écoute, on reconnaît, et on finit par parler.'}</p>
    <button class="btn btn--pri btn--large" onclick="aller('prep/${x.id}/${suivant[0]}')">${e.fin ? 'Refaire' : Object.keys(e.faits).length ? 'Continuer' : 'Commencer'} : ${suivant[1]}</button>
    <div class="objectif" style="margin-top:16px">${E(D.prep.fin[x.obj])}</div>
    <div class="meca"><p class="surtitre">L'aide-mémoire</p><ul>${x.meca.map(t => `<li>${t}</li>`).join('')}</ul></div>`;
}
function carteMot(id){
  const m = D.mots[id]; if (!m) return '';
  return `<button class="mot" onclick="jouer('mots/${id}.mp3')" aria-label="Écouter : ${E(m.en)}">
    ${m.img ? `<img src="${BASE}croquis/${id}.jpg?v=${D.v}" alt="" loading="lazy">` : ''}
    <span class="en" lang="en">${E(m.en)}</span><span class="fr">${E(m.fr)}</span>${m.note.startsWith('PIÈGE') ? '<span class="piege">Piège</span>' : ''}</button>`;
}
function seanceEcoute(x){
  // Le temps n'est fait qu'une fois chaque phrase écoutée (audit de Compostelle, G2).
  const entendues = new Set();
  const lignes = x.ecoute.map(([en, fr], k) => `<div class="ph"><button class="btn btn--son" aria-label="Écouter" data-k="${k}" data-f="prep/${x.id}/e${k}.mp3">${ICO.son}</button>
    <div class="t"><b lang="en">${E(en)}</b><span class="sens" ${S.aide ? '' : 'hidden'}>${E(fr)}</span></div></div>`).join('');
  app.innerHTML = `${teteSeance(x, 'ecoute')}
    <p class="consigne">Touchez le haut-parleur : vous entendez la phrase, et son sens apparaît. Répétez-la à voix haute, deux fois.</p>
    <div class="carte liste-ecoute">${lignes}</div>
    <h2>Les mots</h2><p class="consigne">Touchez un mot pour l'entendre.</p>
    <div class="grille">${x.mots.map(carteMot).join('')}</div>
    <div id="finEcoute" style="margin-top:16px"><button class="btn btn--pri btn--large" id="jaiEcoute" disabled>J'ai tout écouté (0 sur ${x.ecoute.length})</button></div>`;
  app.querySelectorAll('.liste-ecoute .btn--son').forEach(b => b.onclick = () => {
    jouer(b.dataset.f); b.closest('.ph').querySelector('.sens').hidden = false; entendues.add(b.dataset.k);
    const bt = $('#jaiEcoute'); if (!bt) return;
    bt.textContent = entendues.size >= x.ecoute.length ? 'J’ai tout écouté' : `J'ai tout écouté (${entendues.size} sur ${x.ecoute.length})`;
    bt.disabled = entendues.size < x.ecoute.length; });
  $('#jaiEcoute').onclick = () => { $('#finEcoute').innerHTML = finTemps(x, 'ecoute'); };
}
/* Une question à choix, jouée jusqu'à la bonne réponse : chaque mauvais choix
   dit pourquoi, et la place de la bonne tourne. */
function questionPrep(it, fichier, graine, surFin, rappel, une){
  const p = it.qui ? D.perso[it.qui] : null, estEn = it.type === 'dire' || (it.type === 'rep' && !!it.q) || (it.type === 'mot' && !it.q);
  const o = ordre(it.choix.length, graine);
  let fini = false, erreurs = 0;
  const titre = it.q || (it.type === 'rep' ? 'Que veut dire la phrase ?' : it.type === 'mot' ? 'Quel mot entendez-vous ?' : 'Que dites-vous ?');
  const haut = it.type === 'dire' ? `<div class="carte"><p style="font-size:18px;font-weight:800;margin:0">${E(it.fr)}</p></div>`
    : `${p ? `<div class="scene-tete"><div><b>${E(p.nom)}</b><div class="muted" style="font-size:14px">${E(p.qui)}</div></div></div>` : ''}
       <div class="gros-son"><button class="btn btn--son" aria-label="Écouter" id="rejouer">${ICO.son}</button></div>`;
  const html = `${rappel ? `<span class="rappel">${E(rappel)}</span>` : ''}${une ? '<span class="rappel">Une seule écoute, comme au comptoir : touchez le haut-parleur quand vous êtes prêt</span>' : ''}
    <h2 style="margin-top:6px">${titre}</h2>${haut}
    <div class="choix">${o.map(i => `<button data-i="${i}" ${estEn ? 'lang="en"' : ''}>${E(it.choix[i][0])}</button>`).join('')}</div><div id="r" aria-live="polite"></div>`;
  function brancher(){
    if ($('#rejouer')) {
      const jouerUne = () => { if (une) $('#rejouer').disabled = true; jouer(fichier, une).then(ok => { if (!ok && une) $('#rejouer').disabled = false; }); };
      $('#rejouer').onclick = jouerUne; if (!une) setTimeout(jouerUne, 250); }
    app.querySelectorAll('.choix button').forEach(b => b.onclick = () => {
      if (fini || b.disabled) return; const i = +b.dataset.i;
      if (i === 0) { fini = true; b.classList.add('juste');
        $('#r').innerHTML = `<div class="retro ok">✓ ${it.type === 'rep' ? '« ' + E(it.en) + ' »' : it.type === 'dire' ? 'C’est bien ce qu’il faut dire.' : 'Bien entendu.'}</div>`;
        if (it.type === 'dire') jouer(fichier);
        surFin(erreurs);
      } else { erreurs++; b.classList.add('faux'); b.disabled = true;
        $('#r').innerHTML = `<div class="retro no">${E(it.choix[i][1])} Essayez encore.</div>`; }
    });
  }
  return [html, brancher];
}
function seanceQuiz(x){
  // Deux questions des séances précédentes ouvrent le quiz (rappel espacé, audit de Compostelle D1).
  const idx = D.prep.seances.indexOf(x);
  const vues = D.prep.seances.slice(0, idx).flatMap((y, j) => y.quiz.map((it, k) => ({it, sid:y.id, k, rappel:'Rappel · séance ' + (j + 1)})));
  const tires = []; while (vues.length && tires.length < 2) tires.push(vues.splice(Math.floor(Math.random() * vues.length), 1)[0]);
  // Aux séances 3, 4 et 8, les deux dernières questions ne s'écoutent qu'une fois, comme au comptoir.
  const unefois = ['p3', 'p4', 'p8'].includes(x.id);
  const items = [...tires, ...x.quiz.map((it, k) => ({it, sid:x.id, k, une: unefois && it.type !== 'dire' && k >= x.quiz.length - 2}))];
  let n = 0, erreurs = 0;
  function tour(){
    if (n >= items.length) {
      app.innerHTML = `${teteSeance(x, 'quiz')}<div class="retro ok">✓ ${items.length} questions${erreurs ? ', ' + erreurs + ' essai' + (erreurs > 1 ? 's' : '') + ' de trop — c’est ainsi qu’on apprend' : ', toutes du premier coup'}.</div>
        <div style="margin-top:12px">${finTemps(x, 'quiz')}</div>`; return; }
    const {it, sid, k, rappel, une} = items[n];
    const fichier = `prep/${sid}/q${k}` + (it.type === 'dire' ? '-c0' : '') + '.mp3';
    // Tour 4 : au hasard à chaque affichage — un rappel refait de mémoire de bouton ne prouve rien.
    const [html, brancher] = questionPrep(it, fichier, Math.floor(Math.random() * 9973), e => {
      erreurs += e; const b = document.createElement('button'); b.className = 'btn btn--pri btn--large'; b.textContent = 'Suivant';
      b.onclick = () => { n++; tour(); }; $('#r').appendChild(b); }, rappel, une);
    app.innerHTML = `${teteSeance(x, 'quiz')}<div class="progres"><i style="width:${100 * n / items.length}%"></i></div>${html}`;
    brancher();
  }
  tour();
}
// Les mots du modèle qui correspondent à une clé manquante, écrits comme dans le modèle.
function motDuModele(en, cle){
  const mots = en.replace(/[?!.,]/g, ' ').split(/\s+/).filter(Boolean);
  for (const n of [1, 2, 3, 4])
    for (let i = 0; i + n <= mots.length; i++) { const bout = mots.slice(i, i + n).join(' '); if (trouve(bout, cle)) return bout; }
  return cle.startsWith('~') ? en : cle.split('|')[0];
}
function seanceDire(x){
  let n = 0, comprises = 0, dites = 0;
  function tour(){
    if (n >= x.dire.length) {
      const assez = dites >= Math.ceil(x.dire.length / 2);
      app.innerHTML = `${teteSeance(x, 'dire')}<div class="retro ${assez ? 'ok' : 'info'}">${assez ? '✓' : '→'} ${dites} phrase${dites > 1 ? 's' : ''} dite${dites > 1 ? 's' : ''} sur ${x.dire.length}${Reco ? `, dont ${comprises} comprise${comprises > 1 ? 's' : ''} au micro du premier ou du deuxième coup` : ''}. ${assez ? 'Le plus dur est fait : oser.' : 'Dites-en au moins la moitié à voix haute pour terminer la séance.'}</div>
        <div style="margin-top:12px">${assez ? finTemps(x, 'dire') : `<button class="btn btn--pri btn--large" onclick="rendre()">Recommencer</button>`}</div>`; return; }
    const [fr, en, cles] = x.dire[n], fichier = `prep/${x.id}/d${n}.mp3`;
    let tente = false, essais = 0, modeleVu = false;
    app.innerHTML = `${teteSeance(x, 'dire')}<div class="progres"><i style="width:${100 * n / x.dire.length}%"></i></div>
      <div class="carte"><p class="surtitre">À vous</p><p style="font-size:19px;font-weight:800;color:var(--text-strong);margin:4px 0 0">${E(fr)}</p></div>
      ${Reco ? `<div class="micro"><button class="btn-micro" id="mic" aria-label="Parler">${ICO.micro}</button>
        <div class="muted" id="micEtat" style="font-size:14px">Touchez le micro, dites-le en anglais.</div><div class="entendu" id="entendu"></div></div>` : ''}
      <button class="btn btn--large" id="dit" style="margin:6px 0">C'est dit !</button><div id="r" aria-live="polite"></div>
      <div class="rangee" style="margin-top:10px"><button class="btn" id="modele" disabled>${ICO.son} Le modèle</button>
       <button class="btn btn--pri" id="suite" style="flex:1" disabled>Suivant</button></div>
      <p class="avis-local" style="margin-top:8px">Le modèle s'ouvre après votre essai : on cherche d'abord, on compare ensuite.</p>
      <button class="btn btn--petit" id="passer" style="margin-top:4px">Passer cette phrase</button>`;
    const zone = $('#r');
    const poserR = h => { zone.querySelectorAll(':scope > :not(.modele-carte)').forEach(y => y.remove()); zone.insertAdjacentHTML('afterbegin', h); };
    const montrer = () => { if (!document.body.contains(zone)) return;
      if (!modeleVu) { modeleVu = true; $('#modele').innerHTML = `${ICO.son} Réécouter`; $('#dit').disabled = true;
        zone.insertAdjacentHTML('beforeend', `<div class="retro info modele-carte"><span class="surtitre">Le modèle</span><div class="phrase-en" lang="en">${E(en)}</div></div>`); }
      $('#modele').disabled = false; jouer(fichier); };
    const essaye = () => { if (!tente) { tente = true; dites++; } $('#modele').disabled = false; $('#suite').disabled = false; };
    $('#modele').onclick = montrer;
    $('#suite').onclick = () => { n++; tour(); };
    $('#passer').onclick = () => { n++; tour(); };
    $('#dit').onclick = () => { essaye(); montrer(); };
    if (Reco) $('#mic').onclick = () => {
      const mic = $('#mic'); if (recoActive) { arreterMicro(); return; }
      mic.classList.add('ecoute'); mic.innerHTML = ICO.stop; $('#micEtat').textContent = 'Je vous écoute… touchez pour arrêter.';
      ecouterMicro(t => { $('#entendu').textContent = '« ' + t + ' »'; }, final => {
        mic.classList.remove('ecoute'); mic.innerHTML = ICO.micro; $('#micEtat').textContent = 'Touchez le micro pour réessayer.';
        if (!final) { poserR(`<div class="retro info">${rienEntendu('Je n’ai rien entendu. Vérifiez que le micro est permis, ou dites-le et touchez « C’est dit ! ».')}</div>`); return; }
        essais++;
        const manque = cles.filter(c => !trouve(final, c));
        if (!manque.length) { if (essais <= 2 && !modeleVu) comprises++;
          poserR(`<div class="retro ok">✓ Well done! On vous a compris.</div>`); essaye(); setTimeout(montrer, 600); return; }
        if (manque.some(c => trouve('', c))) { poserR(`<div class="retro no">Votre phrase dit le contraire de ce qu’il faut. ${essais < 2 && !modeleVu ? 'Réessayez.' : 'Comparez avec le modèle.'}</div>`);
          essaye(); if (essais >= 2) montrer(); else $('#modele').disabled = false; return; }
        const presque = manque.length <= cles.filter(c => !trouve('', c)).length / 2;   // hors gardes (tour 5)
        poserR(`<div class="retro no">${presque ? `Presque. Il manque : <b lang="en">${manque.map(c => E(motDuModele(en, c))).join(', ')}</b>. ` : 'Je n’ai pas reconnu la phrase. '}${essais < 2 && !modeleVu ? 'Réessayez, sans regarder le modèle.' : 'Comparez avec le modèle.'}</div>`);
        essaye();
        if (essais >= 2) montrer(); else $('#modele').disabled = false;
      });
    };
  }
  tour();
}
function vuePrepTest(){
  const T = S.prep.test || (S.prep.test = {});
  const f = T.prochaine != null ? T.prochaine : Math.floor(Math.random() * 2);
  const items = D.prep.test[f]; let k = 0; const res = {}, nonVerif = {}, manquees = {};
  function intro(){
    app.innerHTML = `${retour('accueil', 'Accueil')}<p class="surtitre">Le test de la maison</p><h1>Prêt à partir ?</h1>
      <p>${items.length} questions, un quart d'heure, avec le son et le micro. Pour chacun des cinq objectifs, quelques questions — des phrases
      nouvelles : les mêmes outils que dans les séances, d'autres mots.</p>
      <div class="regle"><b>Comme à Toronto.</b> Les phrases qu'on vous dit ne s'écoutent <b>qu'une fois</b>, au débit normal. Au micro, <b>deux essais</b>.
      ${E(D.prep.seuil.replace(" Au micro, deux essais au plus ; les phrases entendues ne s'écoutent qu'une fois.", ''))} C'est un repère, pas une note : il ne vous empêche de rien.</div>
      ${Reco ? '' : '<div class="sans-son">Ce navigateur ne reconnaît pas la voix : ouvrez la page dans Chrome ou Safari pour mesurer l’oral. Sans cela, les questions au micro ne compteront pas.</div>'}
      <button class="btn btn--pri btn--large" id="go">Commencer</button>`;
    // Tour 3 : la forme suivante est fixée dès le départ — un test abandonné ne retombe pas sur la même.
    // Tour 5 : une forme vue, même abandonnée, est « revue » au passage suivant.
    $('#go').onclick = () => { T.prochaine = 1 - f; T.vues = T.vues || {}; T.revu = !!T.vues[f]; T.vues[f] = true; sauver(); tour(); };
  }
  function tour(){
    if (k >= items.length) return bilan();
    const it = items[k]; let compte = false;
    const noter = ok => { if (compte) return; compte = true; const r = res[it.obj] || (res[it.obj] = [0, 0]); r[1]++; if (ok) r[0]++;
      else (manquees[it.obj] || (manquees[it.obj] = [])).push(it.en || it.modele || it.choix[0][0]); };
    const suite = () => { const b = document.createElement('button'); b.className = 'btn btn--pri btn--large'; b.textContent = 'Suivant'; b.onclick = () => { k++; tour(); }; $('#r').appendChild(b); };
    const tete2 = `${retour('accueil', 'Accueil')}<p class="surtitre">Question ${k + 1} sur ${items.length}</p><div class="progres"><i style="width:${100 * k / items.length}%"></i></div>`;
    if (it.type === 'oral') {
      // Audit tour 1 (M3) : la présentation se compte par parties (2 sur 3 = en route), pas tout ou rien.
      let prises = 0, bons = 0;
      app.innerHTML = `${tete2}<h1>Dites-le</h1><div class="carte"><p style="font-size:18px;font-weight:800;margin:0">${E(it.fr)}</p></div>
        ${Reco ? `<div class="micro"><button class="btn-micro" id="mic" aria-label="Parler">${ICO.micro}</button><div class="muted" id="micEtat" style="font-size:14px">Deux essais.</div><div class="entendu" id="entendu"></div></div>` : ''}
        <div id="r" aria-live="polite"></div><button class="btn btn--large" id="sansmic" style="margin-top:8px">${Reco ? 'Sans micro : c’est dit !' : 'C’est dit !'}</button>`;
      const fin = (ok, verifie) => {
        if (verifie && it.parties) { compte = true; const r = res[it.obj] || (res[it.obj] = [0, 0]); r[0] += ok ? it.cles.length : bons; r[1] += it.cles.length;
          if (!ok) (manquees[it.obj] || (manquees[it.obj] = [])).push(it.modele); }
        else if (verifie) noter(ok); else { compte = true; nonVerif[it.obj] = (nonVerif[it.obj] || 0) + 1; }
        if ($('#sansmic')) $('#sansmic').remove(); if ($('#mic')) $('#mic').disabled = true;
        $('#r').insertAdjacentHTML('beforeend', `<div class="retro ${!verifie ? 'info' : ok ? 'ok' : 'no'}">${!verifie ? 'Non vérifié : sans le micro, cet objectif ne pourra pas être « Solide ».' : ok ? '✓ On vous a compris.' : 'Deux essais sans qu’on vous comprenne tout à fait.'}</div>
          <div class="retro info"><span class="surtitre">Le modèle</span><div class="phrase-en" lang="en">${E(it.modele)}</div></div>`);
        jouer(`prep/test/${f}-${k}-m.mp3`); suite(); };
      $('#sansmic').onclick = () => fin(false, false);
      if (Reco) $('#mic').onclick = () => { const mic = $('#mic'); if (recoActive) { arreterMicro(); return; }
        mic.classList.add('ecoute'); mic.innerHTML = ICO.stop;
        ecouterMicro(t => { $('#entendu').textContent = '« ' + t + ' »'; }, final => {
          mic.classList.remove('ecoute'); mic.innerHTML = ICO.micro;
          if (!final) { $('#r').innerHTML = `<div class="retro info">${rienEntendu($('#sansmic') ? 'Je n’ai rien entendu. Vérifiez que le micro est permis et réessayez — ou touchez « Sans micro : c’est dit ! ».' : 'Je n’ai rien entendu. Vérifiez que le micro est permis et réessayez.')}</div>`; return; }
          const manque = it.cles.map((c, i) => [c, i]).filter(([c]) => !trouve(final, c));
          prises++; bons = Math.max(bons, it.cles.length - manque.length);
          // Une fois le micro entendu, « sans micro » n'est plus une issue (Compostelle, tour 2, F1).
          if ($('#sansmic')) $('#sansmic').remove();
          if (!manque.length) { $('#r').innerHTML = ''; return fin(true, true); }
          const quoi = it.parties ? 'Il manque : ' + manque.map(([, i]) => E(it.parties[i])).join(', ') + '.' : `J'ai entendu « ${E(final)} ».`;
          if (prises >= 2) { $('#r').innerHTML = `<div class="retro no">${quoi}</div>`; return fin(false, true); }
          $('#r').innerHTML = `<div class="retro no">${quoi} Réessayez (dernier essai).</div>`;
        }); };
      return;
    }
    // Au test, le premier choix compte. P2 et P5 : une seule écoute, au débit naturel.
    const fichier = `prep/test/${f}-${k}` + (it.type === 'dire' ? '-c0' : '') + '.mp3';
    const unefois = it.obj === 'P2' || it.obj === 'P5';
    // Tour 4 : un tirage indépendant à chaque affichage. Une graine fixe mettait la bonne au même bouton
    // (tour 3) ; une permutation posée dans les données se déduisait des places déjà montrées (tour 4).
    const o = ordre(it.choix.length, Math.floor(Math.random() * 9973)).filter(i => i !== 0);
    o.splice(Math.floor(Math.random() * it.choix.length), 0, 0);
    const estEn = it.type !== 'rep', p = it.qui ? D.perso[it.qui] : null;
    const titre = it.type === 'rep' ? 'Que veut dire la phrase ?' : it.type === 'mot' ? 'Quel mot entendez-vous ?' : 'Que dites-vous ?';
    app.innerHTML = `${tete2}<h1>${titre}</h1>
      ${it.type === 'dire' ? `<div class="carte"><p style="font-size:18px;font-weight:800;margin:0">${E(it.fr)}</p></div>` :
        `${p ? `<div class="scene-tete"><div><b>${E(p.nom)}</b><div class="muted" style="font-size:14px">${unefois ? 'Une seule écoute, comme au comptoir : touchez le haut-parleur quand vous êtes prêt.' : 'Vous pouvez réécouter.'}</div></div></div>` : ''}
         <div class="gros-son"><button class="btn btn--son" aria-label="Écouter" id="ecoute1">${ICO.son}</button></div>`}
      <div class="choix">${o.map(i => `<button data-i="${i}" ${estEn ? 'lang="en"' : ''}>${E(it.choix[i][0])}</button>`).join('')}</div><div id="r" aria-live="polite"></div>`;
    if (it.type !== 'dire') {
      let joue = false;
      // Une seule écoute : elle part au toucher, jamais toute seule (Compostelle, 27 sept. 2026).
      const une = () => { if (unefois && joue) return; if (unefois) { joue = true; $('#ecoute1').disabled = true; }
        jouer(fichier, unefois).then(ok => { if (!ok && unefois) { joue = false; $('#ecoute1').disabled = false; } }); };
      $('#ecoute1').onclick = une; if (!unefois) setTimeout(une, 250);
    }
    app.querySelectorAll('.choix button').forEach(b => b.onclick = () => {
      if (compte) return; const i = +b.dataset.i; noter(i === 0);
      b.classList.add(i === 0 ? 'juste' : 'faux'); if (i !== 0) app.querySelector('.choix button[data-i="0"]').classList.add('juste');
      $('#r').innerHTML = `<div class="retro ${i === 0 ? 'ok' : 'no'}">${i === 0 ? '✓' + (it.en ? ' « ' + E(it.en) + ' »' : '') : E(it.choix[i][1]) + (it.en ? ' « ' + E(it.en) + ' »' : '')}</div>`;
      if ($('#ecoute1')) { $('#ecoute1').disabled = false; $('#ecoute1').onclick = () => jouer(fichier); }
      if (it.type === 'dire') jouer(fichier); suite();
    });
  }
  function bilan(){
    // Tour 4 : deux formes seulement ; dès le 3e passage, on a déjà vu les réponses de la forme.
    const revu = !!T.revu;
    let solides = 0;
    const lignes = Object.keys(D.prep.objectifs).map(o => {
      const [ok, tot] = res[o] || [0, 0], nv = nonVerif[o] || 0, lieu = LIEUX[D.prep.lieu[o]];
      if (!tot) return `<div class="carte" style="margin:8px 0"><b>${E(D.prep.objectifs[o])}</b><div class="retro info" style="margin:6px 0">Non vérifié au micro : refaites ces questions avec le micro.</div><p class="muted" style="margin:0;font-size:15px">${E(D.prep.conseils[o])}</p></div>`;
      // Audit tour 2 : une question passée sans micro empêche « Solide » (sinon on saute l'item difficile).
      const r = ok / tot, solideIci = r >= D.prep.solide && !nv; if (solideIci) solides++;
      const etat = solideIci ? ['ok', '✓ Solide'] : r >= .5 ? ['info', '→ En route'] : ['no', '— À reprendre'];
      return `<div class="carte" style="margin:8px 0"><b>${E(D.prep.objectifs[o])}</b><div class="retro ${etat[0]}" style="margin:6px 0">${etat[1]} — ${ok} sur ${tot}${nv ? ` (et ${nv} non vérifiée${nv > 1 ? 's' : ''} au micro)` : ''}</div>
        ${!solideIci ? `<p class="muted" style="margin:0;font-size:15px">${E(D.prep.conseils[o])}</p>` : ''}
        ${(manquees[o] || []).length ? `<p class="muted" style="margin:4px 0 0;font-size:14px">À revoir : ${manquees[o].map(t => '<i lang="en">' + E(t) + '</i>').join(' · ')}</p>` : ''}
        ${lieu ? `<p class="muted" style="margin:4px 0 0;font-size:14px">Vous en aurez besoin ${E(lieu)}.</p>` : ''}</div>`;
    }).join('');
    T.prochaine = 1 - f; T.passages = (T.passages || 0) + 1; T.dernier = aujourdhui(); sauver();
    const tous = solides === Object.keys(D.prep.objectifs).length;
    app.innerHTML = `${retour('accueil', 'Accueil')}<h1>Où vous en êtes</h1>
      <p>Un repère sur un échantillon, pas une note. La prochaine fois — la veille du départ, par exemple — ce sera l'autre forme.</p>
      ${tous ? (revu ? '<div class="retro info">Vous connaissiez déjà ces questions : ce résultat dit surtout que vous vous en souvenez. Pour vous situer pour vrai, faites une séance que vous n’avez pas faite.</div>' : '<div class="retro ok">✓ Solide partout : vous pouvez sauter les séances, ou n’y revenir que pour vous rafraîchir la mémoire.</div>') : ''}${lignes}
      <button class="btn btn--pri btn--large" onclick="aller('prep')">${tous ? 'Ma valise' : 'Aux séances'}</button>`;
  }
  intro();
}

/* ---------- étape 2 : les planches et les faux amis ---------- */
const PICTO = {
  gauche:'<svg viewBox="0 0 64 64"><path d="M50 32H16M28 18 14 32l14 14" fill="none" stroke="#7A3B1D" stroke-width="7" stroke-linecap="round" stroke-linejoin="round"/></svg>',
  droite:'<svg viewBox="0 0 64 64"><path d="M14 32h34M36 18l14 14-14 14" fill="none" stroke="#7A3B1D" stroke-width="7" stroke-linecap="round" stroke-linejoin="round"/></svg>',
  droit:'<svg viewBox="0 0 64 64"><path d="M32 52V14M18 26l14-14 14 14" fill="none" stroke="#7A3B1D" stroke-width="7" stroke-linecap="round" stroke-linejoin="round"/></svg>',
  blocs:'<svg viewBox="0 0 64 64"><rect x="6" y="6" width="22" height="22" rx="2" fill="#E9DCD2"/><rect x="36" y="6" width="22" height="22" rx="2" fill="#E9DCD2"/><rect x="6" y="36" width="22" height="22" rx="2" fill="#E9DCD2"/><rect x="36" y="36" width="22" height="22" rx="2" fill="#E9DCD2"/><path d="M32 60V32H58" fill="none" stroke="#7A3B1D" stroke-width="4" stroke-linecap="round" stroke-dasharray="1 7"/><circle cx="32" cy="60" r="4" fill="#7A3B1D"/></svg>',
  carrefour:'<svg viewBox="0 0 64 64"><rect x="26" y="2" width="12" height="60" fill="#D8D3CC"/><rect x="2" y="26" width="60" height="12" fill="#D8D3CC"/><circle cx="32" cy="32" r="6" fill="#C8102E"/></svg>',
  huard:'<svg viewBox="0 0 64 64"><polygon points="32,6 54,17 54,47 32,58 10,47 10,17" fill="#D4A62A" stroke="#7A5A10" stroke-width="2"/><path d="M20 38c6-8 16-8 24-2" fill="none" stroke="#7A5A10" stroke-width="3" stroke-linecap="round"/><circle cx="40" cy="30" r="2.5" fill="#7A5A10"/></svg>',
  deux:'<svg viewBox="0 0 64 64"><circle cx="32" cy="32" r="27" fill="#C9CDD2" stroke="#5F656C" stroke-width="2"/><circle cx="32" cy="32" r="17" fill="#D4A62A" stroke="#7A5A10" stroke-width="2"/></svg>',
  '25':'<svg viewBox="0 0 64 64"><circle cx="32" cy="32" r="22" fill="#C9CDD2" stroke="#5F656C" stroke-width="2"/><path d="M22 40c4-10 14-14 20-10" fill="none" stroke="#5F656C" stroke-width="3" stroke-linecap="round"/></svg>',
  thermo:'<svg viewBox="0 0 64 64"><rect x="26" y="6" width="12" height="40" rx="6" fill="#fff" stroke="#333" stroke-width="2.5"/><rect x="29" y="20" width="6" height="28" fill="#C8102E"/><circle cx="32" cy="50" r="9" fill="#C8102E" stroke="#333" stroke-width="2.5"/></svg>'
};
function boussole(dir){ const ang = {nord:0, est:90, sud:180, ouest:270}[dir];
  return `<svg viewBox="0 0 64 64"><circle cx="32" cy="32" r="27" fill="#fff" stroke="#333" stroke-width="2.5"/><g transform="rotate(${ang} 32 32)"><polygon points="32,9 39,34 32,29 25,34" fill="#C8102E"/></g><circle cx="32" cy="32" r="3" fill="#333"/></svg>`; }
function horloge(h, m){
  const a = (h % 12) * 30 + m / 2, b = m * 6, rad = x => (x - 90) * Math.PI / 180;
  const pt = (ang, L) => [32 + L * Math.cos(rad(ang)), 32 + L * Math.sin(rad(ang))];
  let t = ''; for (let i = 0; i < 12; i++) { const [x1, y1] = pt(i * 30, 24), [x2, y2] = pt(i * 30, 27); t += `<line x1="${x1}" y1="${y1}" x2="${x2}" y2="${y2}" stroke="#333" stroke-width="2"/>`; }
  const [ax, ay] = pt(a, 15), [bx, by] = pt(b, 23);
  return `<svg viewBox="0 0 64 64"><circle cx="32" cy="32" r="29" fill="#fff" stroke="#333" stroke-width="3"/>${t}<line x1="32" y1="32" x2="${ax}" y2="${ay}" stroke="#111" stroke-width="4" stroke-linecap="round"/><line x1="32" y1="32" x2="${bx}" y2="${by}" stroke="#111" stroke-width="2.5" stroke-linecap="round"/><circle cx="32" cy="32" r="2.5" fill="#111"/></svg>`;
}
function picto(nom){
  if (PICTO[nom]) return PICTO[nom];
  if (['nord', 'sud', 'est', 'ouest'].includes(nom)) return boussole(nom);
  const m = /^h(\d{2})(\d{2})?$/.exec(nom); if (m) return horloge(+m[1], m[2] ? +m[2] : 0);
  return '';
}
function visuel(m, id){
  if (m.img === 'croquis') return `<span class="vis"><img src="${BASE}croquis/${id}.jpg?v=${D.v}" alt="" loading="lazy"></span>`;
  if (m.img && m.img.startsWith('picto:')) return `<span class="vis">${picto(m.img.slice(6))}</span>`;
  return `<span class="vis vide" aria-hidden="true">${ICO.son}</span>`;
}
function vueMots(){
  const n = p => D.planches.length && Object.values(D.mots).filter(m => m.p === p).length;
  app.innerHTML = `${retour('accueil', 'Accueil')}<p class="surtitre">Les mots</p><h1>Douze planches</h1>
    <p>Touchez un mot : vous l'entendez, et son sens en français apparaît. Répétez-le à voix haute. Les <b>faux amis</b> sont marqués : ils ont
    leur série à part.</p>
    <div class="pl-liste">${D.planches.map(([k, fr, en]) => `<button onclick="aller('mots/${k}')"><b>${E(fr)}</b><span lang="en">${E(en)} · ${n(k)} mots</span></button>`).join('')}</div>
    <button class="btn btn--large" style="margin-top:14px" onclick="aller('pieges')">Les faux amis : la série</button>`;
}
function vuePlanche(k){
  const pl = D.planches.find(x => x[0] === k); if (!pl) return vueMots();
  const i = D.planches.indexOf(pl), suiv = D.planches[i + 1];
  const ids = Object.keys(D.mots).filter(id => D.mots[id].p === k);
  app.innerHTML = `${retour('mots', 'Les planches')}<p class="surtitre">Planche ${i + 1} sur ${D.planches.length}</p><h1>${E(pl[1])}</h1>
    <label class="aide-bascule bascule-sens"><input type="checkbox" id="sens" ${S.aide ? 'checked' : ''}> Montrer le sens en français</label>
    <div class="grille">${ids.map(id => { const m = D.mots[id], pg = m.note.startsWith('PIÈGE');
      return `<button class="mot${pg ? ' piege-m' : ''}" data-id="${id}" aria-label="Écouter : ${E(m.en)}">${visuel(m, id)}
        <span class="en" lang="en">${E(m.en)}</span><span class="fr" ${S.aide ? '' : 'hidden'}>${E(m.fr)}</span>
        ${pg ? '<span class="piege">Faux ami</span>' : ''}${m.note && !pg ? `<span class="note" ${S.aide ? '' : 'hidden'}>${E(m.note)}</span>` : ''}</button>`; }).join('')}</div>
    ${suiv ? `<button class="btn btn--pri btn--large" style="margin-top:14px" onclick="aller('mots/${suiv[0]}')">Planche suivante : ${E(suiv[1])}</button>` : ''}`;
  app.querySelectorAll('.mot').forEach(b => b.onclick = () => { jouer('mots/' + b.dataset.id + '.mp3'); b.querySelectorAll('.fr,.note').forEach(x => x.hidden = false); });
  $('#sens').onchange = e => { S.aide = e.target.checked; sauver(); app.querySelectorAll('.mot .fr,.mot .note').forEach(x => x.hidden = !S.aide); };
}
/* La série des faux amis : chaque piège dans sa phrase de voyage (règle de l'hôtel : jamais montré seul).
   La place de la bonne lecture est tirée au hasard (leçon de la boucle de l'étape 1). */
function vuePieges(){
  // Un à trois vrais amis par série, tirés (tour 2 : un seul, annoncé, et tous les autres étaient faux).
  const vrais = melange(D.pieges.filter(x => x.vrai)), faux = melange(D.pieges.filter(x => !x.vrai));
  const nv = 1 + Math.floor(Math.random() * Math.min(3, vrais.length));
  const items = melange([...vrais.slice(0, nv), ...faux.slice(0, 10 - nv)]);
  let n = 0, premiers = 0;
  function tour(){
    if (n >= items.length) {
      if (!S.exos) S.exos = {}; S.exos.pieges = `${premiers} sur ${items.length}`; sauver();
      app.innerHTML = `${retour('mots', 'Les planches')}<h1>Les faux amis</h1><div class="retro ok">✓ ${items.length} pièges, dont ${premiers} déjoués du premier coup.</div>
        <p class="muted">La série tire dix mots sur ${D.pieges.length}, dont quelques « vrais amis » : refaites-la, ce ne seront pas les mêmes.</p>
        <button class="btn btn--pri btn--large" onclick="rendre()">Une autre série</button>
        <button class="btn btn--large" style="margin-top:8px" onclick="aller('mots')">Les planches</button>`; return; }
    const it = items[n], ch = [[it.bonne, null], [it.fausse, it.expl], [it.seconde, it.expl2]];
    const o = ordre(3, Math.floor(Math.random() * 9973)); let erreurs = 0, fini = false;
    app.innerHTML = `${retour('mots', 'Les planches')}<p class="surtitre">Faux ami ${n + 1} sur ${items.length}</p>
      <div class="progres"><i style="width:${100 * n / items.length}%"></i></div><h2>Que veut dire la phrase ?</h2>
      <div class="gros-son"><button class="btn btn--son" aria-label="Écouter" id="rejouer">${ICO.son}</button></div>
      <p class="phrase-en" lang="en" style="text-align:center">${E(it.en)}</p>
      <div class="choix">${o.map(i => `<button data-i="${i}">${E(ch[i][0])}</button>`).join('')}</div><div id="r" aria-live="polite"></div>`;
    const f = 'pieges/' + it.id + '.mp3'; $('#rejouer').onclick = () => jouer(f); setTimeout(() => jouer(f), 250);
    app.querySelectorAll('.choix button').forEach(b => b.onclick = () => {
      if (fini || b.disabled) return; const i = +b.dataset.i;
      if (i === 0) { fini = true; if (!erreurs) premiers++; b.classList.add('juste');
        $('#r').innerHTML = `<div class="retro ok">✓ ${E(it.expl)}</div>`;
        const s2 = document.createElement('button'); s2.className = 'btn btn--pri btn--large'; s2.textContent = 'Suivant'; s2.onclick = () => { n++; tour(); }; $('#r').appendChild(s2);
      } else { erreurs++; b.classList.add('faux'); b.disabled = true; $('#r').innerHTML = `<div class="retro no">${i === 1 && !it.vrai ? 'C’est le piège. ' : ''}${E(ch[i][1])} Essayez encore.</div>`; }
    });
  }
  tour();
}

/* ---------- étape 3 : la semaine, le plan et l'album ---------- */
/* Une carte postale se gagne à l'étape 5, en réussissant la situation jouée du lieu ; d'ici là,
   l'album montre les dix cartes à gagner. Le recto est le dessin du lieu (cartes/<id>.jpg) ;
   tant qu'il n'est pas dessiné, un recto composé en HTML le remplace. */
function carteGagnee(id){ return !!((S.cartes || {})[id]); }
function vueSemaine(){
  const n = D.semaine.filter(l => carteGagnee(l.id)).length;
  app.innerHTML = `${retour('accueil', 'Accueil')}<p class="surtitre">2 · La semaine</p><h1>Dix lieux, dix cartes postales</h1>
    <p>On arrive à Union Station, on loge au centre-ville, et la semaine rayonne le long du métro, du tramway et du traversier.
    Chaque situation réussie vous donne la carte postale du lieu, que vous écrirez vous-même en deux lignes d'anglais.</p>
    <div class="defile">%%PLAN%%</div>
    <h2>L'album · ${n} sur ${D.semaine.length}</h2>
    <div class="album">${D.semaine.map(l => `<button class="cp-carte${carteGagnee(l.id) ? '' : ' a-gagner'}" onclick="aller('semaine/${l.id}')">
      <span class="cp-recto">${l.carte ? `<img src="${BASE}cartes/${l.id}.jpg?v=${D.v}" alt="" loading="lazy">` : ''}<span class="cp-n">${l.n}</span><b>${E(l.lieu)}</b></span>
      <small>${E(l.jour)} · ${E(l.situation)}${carteGagnee(l.id) ? ' · ✓ gagnée' : ''}</small></button>`).join('')}</div>
    <h2>Bavarder avec Maya</h2>
    <p>Maya est infirmière, née à Toronto. Vous la croisez chaque jour : elle vous pose des questions, vous lui en posez à votre tour.</p>
    <div class="maya-jours">${D.jeu.maya.map(m => `<button class="btn" onclick="aller('maya/${m.cas}')">${(S.maya || {})[m.cas] ? '✓ ' : ''}${E(m.jour)} · ${E(m.ou)}</button>`).join('')}</div>`;
}
function vueCarte(id){
  const l = D.semaine.find(x => x.id === id); if (!l) return vueSemaine();
  const g = D.gens[l.qui], gagne = carteGagnee(l.id);
  app.innerHTML = `${retour('semaine', "L'album")}<p class="surtitre">${E(l.jour)} · carte ${l.n} sur ${D.semaine.length}</p><h1>${E(l.lieu)}</h1>
    <div class="cp-carte${gagne ? '' : ' a-gagner'}" style="cursor:default"><span class="cp-recto">${l.carte ? `<img src="${BASE}cartes/${l.id}.jpg?v=${D.v}" alt="">` : ''}<span class="cp-n">${l.n}</span><b>${E(l.lieu)}</b></span></div>
    <div class="verso" aria-label="Le dos de la carte"><div class="msg">${gagne && (S.ecrits || {})[l.id] ? `<div class="ecrit">${E(S.ecrits[l.id])}</div>` : `${gagne ? 'Votre carte attend ses deux lignes.' : 'Ici, vous écrirez deux lignes en anglais, une fois la carte gagnée.'}<div class="lignes"></div><div class="lignes"></div><div class="lignes"></div>`}</div>
      <div><div class="timbre">TIMBRE</div><div class="lignes" style="margin-top:28px"></div><div class="lignes"></div></div></div>
    <div class="objectif" style="margin-top:14px"><b>${E(l.situation)}</b> — avec ${E(g.nom)}, ${E(l.qui === 'kevin' ? (l.id === 'iles' ? 'le guichetier du traversier' : 'l’agent de la gare') : g.role.charAt(0).toLowerCase() + g.role.slice(1))}.
      Pour gagner la carte : ${D.jeu.gestes[l.id].map(E).join(' · ')}.</div>
    ${gagne ? `<div class="retro ok">✓ Carte gagnée le ${E(S.cartes[l.id])}.</div>
      <button class="btn btn--pri btn--large" onclick="aller('semaine/${l.id}/ecrire')">${(S.ecrits || {})[l.id] ? 'Récrire la carte' : 'Écrire la carte'}</button>
      <button class="btn btn--large" style="margin-top:8px" onclick="aller('semaine/${l.id}/jouer')">Rejouer la situation</button>`
    : `<button class="btn btn--pri btn--large" onclick="aller('semaine/${l.id}/jouer')">Jouer la situation</button>
      <p class="muted" style="margin-top:8px;font-size:15px">Préparez-la d'abord dans les exercices : les mêmes lieux, les mêmes gens.</p>`}`;
}

/* ---------- étape 5 : la semaine jouée, avec l'assistance ---------- */
/* /api/jeu-de-role, scénario « toronto-en » (build/contenu/toronto/jeu_de_role.py) :
   la personne du lieu vous répond en anglais, avec sa voix (/api/voix, rôles toronto_*).
   Le bilan, en français, dit les gestes accomplis ; au restaurant, l'allergie est
   éliminatoire. Une situation réussie donne la carte postale du lieu, qu'on écrit
   ensuite en deux lignes, relues par l'assistance. Un code ouvre l'assistance. */
const CLE_CODE = 'toronto:code';
// Un accord au masculin quand aucun genre n'est choisi (« vous vous êtes débrouillé », « vous êtes allé »).
const ACCORDE = /vous vous êtes (\S+ )?\S*(é|i|u|is)(?=[\s.,;:!?»]|$)|vous êtes (\S+ )?(allé|arrivé|venu|prêt|enseignant|perdu|resté|parti|parvenu)(?=[\s.,;:!?»]|$)|vous avez été (\S+ )?(clair|précis|poli|prudent)(?=[\s.,;:!?»]|$)/i;
// Une question se reconnaît au « ? », ou à sa forme : le micro du navigateur ne ponctue souvent pas.
// Tour 3 : deviner une question à sa forme comptait « thank you » et ratait « you like poutine ».
// Le bilan CITE les questions du touriste ; la page vérifie la provenance et écarte les demandes
// de clarification et les formules de politesse, puis compte.
// Un mot seul (« Hockey? ») n'est pas une relance — sauf « you » et « yourself » (tour 4).
const CLARIF = /^(sorry|pardon|what|excuse me|huh|again|repeat|can you repeat|could you repeat|say that again|slowly|more slowly|what do you mean|what does .* mean|(?!you$|yourself$)[a-z]+)$/;
const POLI = /^(ok |okay |yes |no )?(thank you|thanks|see you( [a-z]+)?|nice to meet you|nice meeting you|bye|good bye|goodbye)( bye)?$/;
const sansMerci = q => q.replace(/ (thank you|thanks)$/, '');
const estRelance = q => q && !CLARIF.test(q) && !POLI.test(q) && !/(^| )(repeat|slowly|again)( |$)/.test(q);
// Tour 4 (bloquant) : compter les RÉPLIQUES qui portent une question vérifiée — « And you? » dit deux fois
// compte deux fois ; deux morceaux d'une même réplique comptent une fois. Provenance au mot près.
// Une citation courte (« you », « and you ») ne vaut que si la réplique FINIT par elle, jamais « thank you ».
const contient = (d, q) => q.split(' ').length <= 2 ? (d === q || (d.endsWith(' ' + q) && !/(thank|see|meet) you$/.test(d))) : (' ' + d + ' ').includes(' ' + q + ' ');
const repliquesRelancees = (citees, dits) => { const qs = (citees || []).map(q => sansMerci(plat(q))).filter(estRelance);
  return dits.filter(d => qs.some(q => contient(sansMerci(d), q))).length; };
// A-t-il RÉPONDU à Maya ? Une réplique anglaise qui n'est ni une clarification, ni une politesse seule, ni une
// question citée (tour 4 : « Sorry? » et des questions sans aucune réponse passaient pour un succès).
// Tour 5 : « Quebec. », « Yes. », « No, first time. » SONT des réponses (le palier lent parle ainsi) ; ne
// sont pas des réponses : une demande de clarification, un salut, une politesse, une question citée.
const PAS_REPONSE = /^((sorry|pardon|excuse me|what|huh)( please)?|(sorry )?(can|could) you repeat( that)?( please)?|repeat( please)?|(sorry )?(more )?slowly( please)?|again( please)?|hello|hi|hey|ok|okay|bye|ok bye|thanks|thank you)$/;
const QUEUE = / (and you|what about you|how about you|and yourself|you|thank you|thanks|bye|nice to meet you( too)?|nice meeting you|see you)$/;
const aRepondu = (citees, dits) => { const qs = (citees || []).map(q => plat(q)).filter(Boolean);
  return dits.some(d => { let r = ' ' + d + ' ';
    qs.forEach(q => { r = r.split(' ' + q + ' ').join(' '); });
    r = r.replace(/\s+/g, ' ').trim(); let avant;
    do { avant = r; r = (' ' + r).replace(QUEUE, '').trim(); } while (r !== avant);
    return !!r && !PAS_REPONSE.test(r) && !POLI.test(r); }); };
// Ce qui COMPTE les questions est retiré, phrase par phrase ; parler des questions de Maya reste permis.
const COMPTE_Q = /(\d+|une|deux|trois|aucune|plusieurs|pas assez de|assez de|toutes? (ses|les|vos)|une seule) questions?/i;
const sansCompte = t => String(t || '').split(/(?<=[.!?])\s+/).filter(x => !COMPTE_Q.test(x)).join(' ');
// Une correction garde le sens : on compare les mots PLEINS (contractions dépliées, radical de 5 lettres) ;
// rejetée si elle en ajoute plus qu'elle n'en garde, plus un (tour 3 : « allergy at the peanuts → allergic
// to peanuts » était jeté ; « OK bye → I haven't eaten yet, bye » reste rejeté).
const VIDES = new Set('a an the to please do does did is are am was were will would it i you me my we us of at in on for and so ok okay yes no not be have has had can could i m s ll d re ve t'.split(' '));
const deplie = t => plat(t).replace(/\bi m\b/g, 'i am').replace(/\b(\w+) t\b/g, '$1 not').replace(/\b(\w+) ll\b/g, '$1 will').replace(/\b(\w+) re\b/g, '$1 are');
const pleins = t => deplie(t).split(' ').filter(w => w && !VIDES.has(w)).map(w => w.slice(0, 5));
const fideleA = (dit, mieux) => { const d = new Set(pleins(dit)), m = pleins(mieux);
  const ajoutes = m.filter(w => !d.has(w)).length, gardes = m.filter(w => d.has(w)).length;
  return ajoutes <= gardes + 1; };
// Une réplique en français : un pronom, ou deux marqueurs (« Do you like Les Misérables? » reste anglaise).
const FRANCAIS = { test: t => /(^| )(je|j|tu|toi|vous|nous|ca va|hein|pis|merci|bonjour|oui)( |$)/.test(t)
  || (t.match(/(^| )(est|et|le|la|les|des|ou|aussi|comment|quoi|avec|pour|dans)(?= |$)/g) || []).length >= 2 };
// Ce qui touche le produit dangereux, dans un lieu à éliminatoire : on ne le peaufine jamais.
// Tour 5 : le produit en mots entiers (« start » contenait « tart »), dans une réplique qui n'est ni une question
// ni un refus (« The salmon, please » commande ; « Are there nuts in the tart? » demande).
const PRODUIT = /(^| )(salmon|pecans?|almonds?|tart|ice cream|walnuts?|hazelnuts?|cookies?|biscuits?|peanuts?)( |$)/;
const QUESTION_REFUS = /^(is|are|does|do|has|have|any|what|which|can you|could you)( |$)|(^| )(no|not|don t|do not|without|allerg[a-z]*|nut free|peanut free)( |$)/;
const DANGER = { test: t => PRODUIT.test(t) && !QUESTION_REFUS.test(t) };
const PALIERS = [['lent', 'Lentement'], ['normal', 'Normalement'], ['rapide', 'Vite, comme à Toronto']];
const estCode = c => /^PC[A-Z2-9]{6}$/.test(c || '');
const lireCode = () => { try { return localStorage.getItem(CLE_CODE) || ''; } catch(e) { return ''; } };
const garderCode = c => { try { localStorage.setItem(CLE_CODE, c); } catch(e) {} };
let voixEnCours = null;
function voixRepli(t){
  try { speechSynthesis.cancel(); const u = new SpeechSynthesisUtterance(t); u.lang = 'en-CA'; u.rate = S.lent ? .8 : 1;
    const v = speechSynthesis.getVoices().find(x => x.lang === 'en-CA') || speechSynthesis.getVoices().find(x => /^en/.test(x.lang));
    if (v) u.voice = v; speechSynthesis.speak(u); } catch(e) {}
}
async function direAvecVoix(t, code, personnage, palier){
  try { speechSynthesis.cancel(); } catch(e) {}
  lecteur.pause();
  const n = voixEnCours = {};
  try {
    const r = await fetch('/api/voix', {method:'POST', headers:{'Content-Type':'application/json'},
      body: JSON.stringify({code, texte:t, personnage, role:'touriste', palier: palier === 'lent' ? 'lent' : null})});
    if (!r.ok) throw 0;
    const b = await r.blob(); if (n !== voixEnCours) return;
    lecteur.src = URL.createObjectURL(b); lecteur.playbackRate = 1;
    await lecteur.play();
  } catch(e) { if (n === voixEnCours) voixRepli(t); }
}
function casDe(cas){
  if (cas.startsWith('maya-')) { const m = D.jeu.maya.find(x => x.cas === cas); return m && {cas, maya:true, qui:'maya', titre:'Bavarder avec Maya', jour:m.jour, ou:m.ou, retour:'semaine'}; }
  const l = D.semaine.find(x => x.id === cas); return l && {cas, qui:l.qui, titre:l.situation, jour:l.jour, lieu:l.lieu, retour:'semaine/' + l.id, l};
}
function vueJouer(cas){
  const c = casDe(cas); if (!c) return vueSemaine();
  const g = D.gens[c.qui];
  let code = lireCode(), palier = S.palier || 'lent';
  const choixPal = () => PALIERS.map(([k, t]) => `<button class="btn btn--petit ${palier === k ? 'btn--pri' : ''}" data-pal="${k}">${t}</button>`).join('');
  const titreRetour = c.maya ? "L'album" : c.lieu;
  const choixGenre = () => [['f', 'Féminin'], ['m', 'Masculin'], ['', 'Sans accord']].map(([k, t]) => `<button class="btn btn--petit ${(S.genre || '') === k ? 'btn--pri' : ''}" data-genre="${k}">${t}</button>`).join('');
  function accueil(err){
    app.innerHTML = `${retour(c.retour, titreRetour)}<p class="surtitre">${E(c.jour)} · avec l'assistance</p><h1>${E(c.titre)}</h1>
      <div class="objectif">${c.maya ? `Vous croisez Maya ${E(c.ou)}. Elle vous parle, vous répondez — et vous lui posez au moins deux questions à votre tour (And you? What about you?).`
        : E(D.jeu.consigne[c.cas])}</div>
      ${c.maya ? '' : `<p class="muted" style="font-size:15px">Pour gagner la carte : ${D.jeu.gestes[c.cas].map(E).join(' · ')}.${D.jeu.elim.includes(c.cas) ? ' <b>L’allergie est éliminatoire :</b> ' + E(D.jeu.regle[c.cas]) : ''}</p>`}
      <p class="muted">${E(g.nom)} vous répond vraiment, en anglais : dites ce que vous voulez, comme vous pouvez. Il faut du réseau.</p>
      <h3>Comment on vous parle</h3><div class="rangee" id="pal">${choixPal()}</div>
      <h3>Le bilan, en français, s'accorde au</h3><div class="rangee" id="genre">${choixGenre()}</div>
      <h3>Votre code</h3><input id="code" class="code-champ" value="${E(code)}" autocomplete="off" autocapitalize="characters">
      <div id="compte"></div>
      <p class="avis-local">Le code de votre achat. Il ouvre l'assistance ; il ne dit pas qui vous êtes.</p>
      ${err ? `<div class="retro no">${E(err)}</div>` : ''}
      <button class="btn btn--pri btn--large" id="go" style="margin-top:10px">Commencer</button>
      <div id="offre"></div>`;
    afficherCompte(code); afficherOffre(!code);
    $('#genre').onclick = e => { const b = e.target.closest('[data-genre]'); if (b) { S.genre = b.dataset.genre; sauver(); $('#genre').innerHTML = choixGenre(); } };
    $('#pal').onclick = e => { const b = e.target.closest('[data-pal]'); if (b) { palier = S.palier = b.dataset.pal; sauver(); $('#pal').innerHTML = choixPal(); } };
    $('#go').onclick = () => { code = $('#code').value.trim().toUpperCase(); garderCode(code); conversation(); };
  }
  function conversation(){
    const hist = []; let fini = false, cache = false;
    app.innerHTML = `${retour(c.retour, titreRetour)}
      <div class="scene-tete">${g.portrait ? `<img src="${BASE}gens/${c.qui}-neutre.jpg?v=${D.v}" alt="">` : ''}<div><b>${E(g.nom)}</b><div class="muted" style="font-size:14px">${E(c.titre)}</div></div></div>
      <label class="aide-bascule"><input type="checkbox" id="cache"> Écouter sans lire (le texte se montre en le touchant)</label>
      <div class="fil" id="fil"></div>
      <div id="saisie" style="margin-top:12px">
        ${Reco ? `<div class="micro"><button class="btn-micro" id="mic" aria-label="Parler">${ICO.micro}</button><div class="entendu" id="entendu"></div></div>` : ''}
        <div class="rangee"><input id="txt" class="saisie-txt" placeholder="…ou écrivez en anglais" autocomplete="off">
        <button class="btn btn--pri" id="env">Envoyer</button></div>
        <button class="btn btn--large" id="fin" style="margin-top:10px">Terminer et voir le bilan</button></div><div id="r"></div>`;
    const fil = $('#fil');
    $('#cache').onchange = e => { cache = e.target.checked; fil.querySelectorAll('.bulle.lui').forEach(b => b.classList.toggle('cache', cache)); };
    const bulle = (moi, t) => { const b = document.createElement('div'); b.className = 'bulle ' + (moi ? 'moi' : 'lui') + (!moi && cache ? ' cache' : '');
      b.innerHTML = `<div class="qui">${moi ? 'Vous' : E(g.nom)}</div><div class="en">${E(t)}</div>`;
      if (!moi) { b.title = 'Toucher pour réentendre'; b.onclick = () => { b.classList.remove('cache'); direAvecVoix(t, code, g.voix, palier); }; }
      fil.appendChild(b); b.scrollIntoView({behavior:'smooth', block:'end'}); };
    async function tour(texte){
      if (texte) { hist.push({role:'user', contenu:texte}); bulle(true, texte); }
      const att = document.createElement('div'); att.className = 'muted'; att.textContent = g.nom + ' réfléchit…'; fil.appendChild(att);
      try {
        const r = await fetch('/api/jeu-de-role', {method:'POST', headers:{'Content-Type':'application/json'},
          body: JSON.stringify({code, scenario:'toronto-en', cas:c.cas, role:'touriste', niveau:palier, historique:hist})});
        const d = await r.json().catch(() => ({})); att.remove();
        if (!r.ok) {
          if (r.status === 401) return accueil('Ce code n’est pas accepté.');
          if (d.pelerin || r.status === 403) return accueil(d.error);
          $('#r').innerHTML = `<div class="retro no">${E(d.error || 'Erreur')}</div>`; return; }
        if (d.pelerin) memoCompte(d.pelerin);
        if (d.ouverture) { hist.unshift({role:'user', contenu:d.ouverture}); bulle(true, d.ouverture); }
        let t = String(d.reponse || ''); fini = /\bFIN\W*$/.test(t); t = t.replace(/\bFIN\W*$/, '').trim();
        hist.push({role:'assistant', contenu:t}); bulle(false, t); direAvecVoix(t, code, g.voix, palier);
        if (fini) bilan();
      } catch(e) { att.remove(); $('#r').innerHTML = `<div class="retro no">Pas de réseau ? L’assistance a besoin d’une connexion.</div>`; }
    }
    const envoyer = () => { const t = $('#txt').value.trim(); if (t && !fini) { $('#txt').value = ''; tour(t); } };
    $('#env').onclick = envoyer; $('#txt').onkeydown = e => { if (e.key === 'Enter') envoyer(); };
    $('#fin').onclick = () => bilan();
    if (Reco) $('#mic').onclick = () => {
      const mic = $('#mic'); if (recoActive) { arreterMicro(); return; }
      try { speechSynthesis.cancel(); } catch(e) {} lecteur.pause();
      mic.classList.add('ecoute'); mic.innerHTML = ICO.stop;
      ecouterMicro(t => { $('#entendu').textContent = '« ' + t + ' »'; }, final => {
        mic.classList.remove('ecoute'); mic.innerHTML = ICO.micro; $('#entendu').textContent = '';
        if (!final) { $('#entendu').textContent = rienEntendu('Je n’ai rien entendu. Réessayez, ou écrivez votre réponse.'); return; }
        if (!fini) tour(final);
      });
    };
    async function bilan(){
      fini = true; arreterMicro();
      if (hist.filter(m => m.role === 'user').length < 2) { $('#saisie').innerHTML = `<div class="retro info">Vous n’avez encore rien dit : le bilan juge ce que vous dites.</div>
        <button class="btn btn--pri btn--large" onclick="rendre()">Recommencer</button>`; return; }
      $('#saisie').innerHTML = `<div class="muted">Le bilan arrive…</div>`;
      try {
        const demander = async () => { const r = await fetch('/api/jeu-de-role', {method:'POST', headers:{'Content-Type':'application/json'},
          body: JSON.stringify({code, scenario:'toronto-en', cas:c.cas, role:'touriste', bilan:true, genre:S.genre || null, historique:hist.slice(1)})});
          return [r, await r.json().catch(() => ({}))]; };
        let [r, d] = await demander();
        // Tour 2 : sans genre choisi, le modèle accordait encore au masculin malgré la consigne — un second tirage.
        if (r.ok && d.bilan && !S.genre && ACCORDE.test([d.bilan.resume, d.bilan.conseil, ...(d.bilan.compris || [])].join(' '))) [r, d] = await demander();
        const b = d.bilan;
        if (!r.ok || !b) { $('#saisie').innerHTML = `<div class="retro no">${E(d.error || 'Pas de bilan cette fois.')}</div>`; return; }
        // Audit étape 5 : la carte ne tient pas au seul « reussi » du modèle — chaque geste attendu doit être coché.
        const att = c.maya ? [] : (D.jeu.gestes[c.cas] || []);
        const gestesOk = Array.isArray(b.gestes) && b.gestes.length === att.length && b.gestes.every(x => x && x.fait === true);
        const gagne = !c.maya && b.reussi === true && gestesOk;
        // Maya : les relances se comptent ici, pas par le modèle (tour 2 : deux relances jugées « pas réussi »).
        const repliques = hist.slice(1).filter(m => m.role === 'user').map(m => plat(m.contenu)).filter(t => !FRANCAIS.test(t));
        const relances = repliquesRelancees(b.questions, repliques);
        // Maya : « reussi » absent → a-t-il répondu en anglais ? ; et deux questions vérifiées.
        // Maya se juge dans la page : a répondu en anglais ET deux répliques relancent (le « reussi » du modèle
        // était absent 3 fois sur 9 et vrai sans réponse).
        const repondu = aRepondu(b.questions, repliques);
        if (c.maya) { b.reussi = repondu && relances >= 2;
          b.compris = (b.compris || []).filter(x => !COMPTE_Q.test(x)); b.conseil = sansCompte(b.conseil); b.resume = sansCompte(b.resume); }
        // « dit » doit venir d'une réplique du touriste : sinon le bilan corrige ce qu'il n'a pas dit.
        const dits = hist.filter(m => m.role === 'user').map(m => plat(m.contenu)).join(' | ');
        b.phrases = (b.phrases || []).filter(x => x && x.dit && x.mieux && dits.includes(plat(x.dit)) && plat(x.dit) !== plat(x.mieux) && fideleA(x.dit, x.mieux)
          && !(D.jeu.elim.includes(c.cas) && !gagne && DANGER.test(plat(x.dit)) && !/allerg/i.test(x.mieux)));
        if (gagne) { S.cartes = S.cartes || {}; if (!S.cartes[c.cas]) S.cartes[c.cas] = aujourdhui(); }
        if (c.maya && b.reussi === true) { S.maya = S.maya || {}; S.maya[c.cas] = aujourdhui(); }
        sauver();
        $('#saisie').innerHTML = `<h2>Le bilan</h2>
          ${b.resume ? `<div class="retro info">${E(b.resume)}</div>` : ''}
          ${att.length ? `<h3>Les gestes</h3>${att.map((g, i) => { const f = !!(b.gestes && b.gestes[i] && b.gestes[i].fait === true);
            return `<div class="geste"><b>${f ? '✓' : '—'}</b><span>${E(g)}${f ? '' : ' <span class="muted">(pas encore)</span>'}</span></div>`; }).join('')}` : ''}
          ${c.maya ? (b.reussi === true ? `<div class="retro ok">✓ Vous avez répondu et posé ${relances} questions à Maya.</div>`
                                        : `<div class="retro no">— Pas encore : ${!repondu ? 'répondez à ses questions en anglais, même brièvement' + (relances < 2 ? `, et posez-lui au moins deux questions (${relances} pour l’instant)` : '') : `vous lui avez posé ${relances} question${relances > 1 ? 's' : ''} ; il en faut au moins deux (And you? What about you?)`}.</div>`) : ''}
          ${!c.maya && !gagne && D.jeu.elim.includes(c.cas) && att.some((g, i) => /allerg|arachide|noix/i.test(g) && !(b.gestes && b.gestes[i] && b.gestes[i].fait === true))
            ? `<div class="retro no"><b>Éliminatoire :</b> ${E(D.jeu.regle[c.cas])}</div>` : ''}
          ${(b.compris || []).length ? `<h3>Ce que vous avez obtenu</h3><ul>${b.compris.map(x => `<li>${E(x)}</li>`).join('')}</ul>` : ''}
          ${(b.phrases || []).length ? `<h3>À dire autrement</h3>${b.phrases.map(x => `<div class="carte" style="margin:6px 0"><div class="muted">${E(x.dit)}</div><div style="font-size:18px;font-weight:800;color:var(--text-strong)">${E(x.mieux)}</div></div>`).join('')}` : ''}
          ${b.conseil ? `<div class="retro info">${E(b.conseil)}</div>` : ''}
          ${c.maya ? '' : gagne ? `<div class="retro ok">✓ Carte postale gagnée : ${E(c.lieu)}. Écrivez-la maintenant, en deux lignes.</div>
              <button class="btn btn--pri btn--large" onclick="aller('semaine/${c.cas}/ecrire')">Écrire la carte</button>`
            : `<div class="retro no">— Pas encore la carte : rejouez la situation en visant les gestes qui manquent.</div>`}
          <button class="btn btn--large" style="margin-top:8px" onclick="rendre()">Rejouer</button>
          <button class="btn btn--large" style="margin-top:8px" onclick="aller('${c.retour}')">${c.maya ? "Retour à l'album" : 'Retour à la carte'}</button>`;
        $('#saisie').scrollIntoView({behavior:'smooth', block:'start'});
      } catch(e) { $('#saisie').innerHTML = `<div class="retro no">Pas de réseau pour le bilan.</div>`; }
    }
    tour('');
  }
  accueil();
}
function vueEcrire(id){
  const l = D.semaine.find(x => x.id === id); if (!l) return vueSemaine();
  if (!carteGagnee(id)) return aller('semaine/' + id);
  const ecrits = S.ecrits || {};
  app.innerHTML = `${retour('semaine/' + id, l.lieu)}<p class="surtitre">Carte ${l.n} · ${E(l.lieu)}</p><h1>Deux lignes au dos</h1>
    <p>Écrivez à quelqu'un de chez vous, en anglais : où vous êtes, ce que vous avez fait, ce que vous en pensez. Deux phrases suffisent.</p>
    <textarea id="txt" class="carte-postale-txt" maxlength="400" placeholder="Hi Léa! Today I…">${E(ecrits[id] || '')}</textarea>
    <p class="avis-local">Le texte reste dans ce téléphone ; il part seulement pour être relu, si vous le demandez, avec votre code.</p>
    <div class="rangee"><button class="btn btn--pri" id="relire" style="flex:1">Faire relire</button><button class="btn" id="garder" style="flex:1">Garder tel quel</button></div>
    <div id="r"></div>`;
  const garder = () => { S.ecrits = S.ecrits || {}; S.ecrits[id] = $('#txt').value.trim(); sauver(); };
  $('#garder').onclick = () => { garder(); aller('semaine/' + id); };
  $('#relire').onclick = async () => {
    const t = $('#txt').value.trim(), code = lireCode();
    if (t.split(/\s+/).length < 4) { $('#r').innerHTML = `<div class="retro info">Écrivez au moins une phrase avant de la faire relire.</div>`; return; }
    if (!code) { $('#r').innerHTML = `<div class="retro info">La relecture passe par l'assistance : entrez d'abord votre code dans une situation jouée.</div>`; return; }
    garder(); $('#r').innerHTML = `<div class="muted">La relecture arrive…</div>`;
    try {
      const r = await fetch('/api/jeu-de-role', {method:'POST', headers:{'Content-Type':'application/json'},
        body: JSON.stringify({code, scenario:'toronto-en', cas:'carte-' + id, role:'touriste', bilan:true, genre:S.genre || null, historique:[{role:'user', contenu:t}]})});
      const d = await r.json().catch(() => ({})), b = d.bilan;
      if (!r.ok || !b) { $('#r').innerHTML = `<div class="retro no">${E(d.error || 'Pas de relecture cette fois.')}</div>`; return; }
      b.phrases = (b.phrases || []).filter(x => x && x.dit && x.mieux && plat(t).includes(plat(x.dit)) && plat(x.dit) !== plat(x.mieux) && fideleA(x.dit, x.mieux));
      $('#r').innerHTML = `${b.resume ? `<div class="retro info">${E(b.resume)}</div>` : ''}
        ${(b.compris || []).length ? `<ul>${b.compris.map(x => `<li>${E(x)}</li>`).join('')}</ul>` : ''}
        ${(b.phrases || []).length ? `<h3>À écrire autrement</h3>${b.phrases.map(x => `<div class="carte" style="margin:6px 0"><div class="muted">${E(x.dit)}</div><div style="font-size:18px;font-weight:800;color:var(--text-strong)">${E(x.mieux)}</div></div>`).join('')}
          <p class="muted" style="font-size:14.5px">Corrigez vous-même, puis gardez la carte.</p>` : ''}
        ${b.conseil ? `<div class="retro info">${E(b.conseil)}</div>` : ''}`;
    } catch(e) { $('#r').innerHTML = `<div class="retro no">Pas de réseau pour la relecture.</div>`; }
  };
}

/* ---------- l'accès payant à l'assistance ---------- */
/* Même vente que Compostelle (pelerins.py, produit « toronto ») : tout est gratuit
   sauf la semaine jouée. Le serveur fait foi sur le prix et les limites. */
const enDollars = c => (c / 100).toLocaleString('fr-CA', {style:'currency', currency:'CAD'});
const dateFr = iso => { const [a, m, j] = String(iso).split('-').map(Number); return a ? new Date(a, m - 1, j).toLocaleDateString('fr-CA', {day:'numeric', month:'long', year:'numeric'}) : ''; };
let OFFRE = null;
async function offreServeur(){
  if (OFFRE) return OFFRE;
  try { const r = await fetch('/api/pelerins/offre'); if (r.ok) OFFRE = await r.json(); } catch(e) {}
  return OFFRE;
}
function memoCompte(etat){ try { localStorage.setItem('toronto:compte', JSON.stringify(etat)); } catch(e) {} }
async function afficherCompte(code){
  if (!$('#compte') || !estCode(code)) return;
  let e = null;
  try { const r = await fetch('/api/pelerins/etat?code=' + encodeURIComponent(code)); if (r.ok) e = await r.json(); } catch(x) {}
  if (!e) { try { e = JSON.parse(localStorage.getItem('toronto:compte') || 'null'); } catch(x) {} }
  if (!e || !$('#compte')) return;
  memoCompte(e);
  const expire = e.expire && e.expire < new Date().toISOString().slice(0, 10);
  $('#compte').innerHTML = `<div class="retro ${e.restant && !expire ? 'info' : 'no'}" style="margin-top:8px">${
    expire ? `Votre accès a pris fin le ${dateFr(e.expire)}.` :
    `Il vous reste <b>${e.restant} conversation${e.restant > 1 ? 's' : ''}</b>, jusqu'au ${dateFr(e.expire)}.`}</div>`;
  const o = await offreServeur();
  if (o && o.ouverte && !expire && e.restant <= 10)
    $('#compte').insertAdjacentHTML('beforeend', `<button class="btn btn--large" id="recharger" style="margin-top:6px">Ajouter ${o.rechargeConversations} conversations — ${enDollars(o.recharge)}</button>`);
  if (o && o.ouverte && expire) afficherOffre(true);
  const b = $('#recharger'); if (b) b.onclick = () => acheter(code);
}
async function afficherOffre(ouvrir){
  const o = await offreServeur(), z = $('#offre');
  if (!z || !o || !o.ouverte) return;
  const promo = o.promo && o.prixRegulier > o.prix;
  const prixHtml = promo ? `<s class="prix-barre">${enDollars(o.prixRegulier)}</s> <b>${enDollars(o.prix)}</b>` : enDollars(o.prix);
  z.innerHTML = `<details class="rub" style="margin-top:16px"${ouvrir ? ' open' : ''}><summary>Pas encore de code ? <span>${prixHtml}</span></summary>
    <div style="padding:0 14px 14px;font-size:15.5px">
     ${promo ? `<p>Prix de lancement : <b>${enDollars(o.prix)}</b> au lieu de ${enDollars(o.prixRegulier)}${o.promoFin ? `, jusqu'au ${dateFr(o.promoFin)} inclusivement` : ''}.</p>` : ''}
     <p style="margin:0 0 8px"><b>${o.conversations} conversations</b> avec les gens de Toronto, pendant <b>${Math.round(o.jours / 30.4)} mois</b> :
     la personne du lieu, ou Maya, qui vous répond vraiment en anglais, puis un bilan en français. La relecture des cartes postales est comprise.</p>
     <p class="muted" style="font-size:14px;margin:0 0 10px">Les séances, les mots, les exercices et le test restent gratuits. Paiement par carte chez Stripe ;
     nous ne recevons ni votre nom ni votre carte. Le code s'affiche ici tout de suite, et il est aussi écrit sur votre reçu.</p>
     <p class="muted" style="font-size:14px;margin:0 0 10px">Vendu par Boucledidactique. Carte de crédit seulement. Remboursable dans les 14 jours si 3 conversations au plus ont servi.
     Réservé aux personnes majeures (ou avec l'accord d'un parent). Aucune taxe. <a href="/conditions-de-vente.html" target="_blank" rel="noopener">Conditions de vente</a></p>
     <button class="btn btn--pri btn--large" id="acheter">Obtenir mon code — ${enDollars(o.prix)}</button></div></details>`;
  $('#acheter').onclick = () => acheter(null);
}
async function acheter(recharge){
  const b = document.activeElement; if (b && b.tagName === 'BUTTON') { b.disabled = true; b.textContent = 'Vers le paiement…'; }
  try {
    const r = await fetch('/api/pelerins/achat', {method:'POST', headers:{'Content-Type':'application/json'},
      body: JSON.stringify(recharge ? {recharge} : {produit:'toronto'})});
    const d = await r.json().catch(() => ({}));
    if (r.ok && d.url) { try { sessionStorage.setItem('toronto:retour', location.hash); } catch(e) {} location.href = d.url; return; }
    alert(d.error || 'Le paiement ne s’ouvre pas. Réessayez dans un moment.');
  } catch(e) { alert('Pas de réseau : le paiement demande une connexion.'); }
  if (b && b.tagName === 'BUTTON') { b.disabled = false; b.textContent = 'Réessayer'; }
}
function suiteApresAchat(){
  let h = ''; try { h = sessionStorage.getItem('toronto:retour') || ''; } catch(e) {}
  return /^#(semaine\/[a-z]+\/jouer|maya\/maya-\d)$/.test(h) ? h.slice(1) : 'semaine';
}
async function vueAchat(sid){
  app.innerHTML = `<p class="surtitre">Merci !</p><h1>Votre accès</h1><div class="muted" id="att">Nous vérifions le paiement auprès de Stripe…</div><div id="z"></div>`;
  let d = null, err = '';
  for (let essai = 0; essai < 6 && !d; essai++) {
    try {
      const r = await fetch('/api/pelerins/session?id=' + encodeURIComponent(sid || ''));
      const j = await r.json().catch(() => ({}));
      if (r.ok) d = j; else if (r.status === 409) await new Promise(ok => setTimeout(ok, 2000)); else { err = j.error || 'Paiement introuvable.'; break; }
    } catch(e) { err = 'Pas de réseau.'; await new Promise(ok => setTimeout(ok, 2000)); }
  }
  $('#att').remove();
  if (!d) { $('#z').innerHTML = `<div class="retro no">${E(err || 'Le paiement n’est pas encore confirmé.')} Si vous avez payé, votre code est écrit sur le reçu reçu par courriel.</div>
    <button class="btn btn--large" onclick="location.reload()">Vérifier de nouveau</button>`; return; }
  garderCode(d.code); memoCompte(d);
  $('#z').innerHTML = `<p>Voici votre code. Il est gardé dans ce téléphone ; notez-le quand même, pour un autre appareil (il est aussi sur votre reçu).</p>
    <div class="code-achat">${E(d.code)}</div>
    <div class="rangee" style="justify-content:center"><button class="btn" id="copier">Copier le code</button></div>
    <div class="retro ok" style="margin-top:12px">✓ ${d.restant} conversations, jusqu'au ${dateFr(d.expire)}.</div>
    <button class="btn btn--pri btn--large" style="margin-top:10px" onclick="aller('${suiteApresAchat()}')">Jouer la semaine</button>`;
  $('#copier').onclick = async () => { try { await navigator.clipboard.writeText(d.code); $('#copier').textContent = 'Copié'; } catch(e) {} };
}
function vueAchatAnnule(){
  app.innerHTML = `${retour('semaine', "L'album")}<h1>Paiement annulé</h1>
    <div class="retro info">Rien n'a été facturé. Les séances, les mots, les exercices et le test ne demandent aucun code.</div>
    <button class="btn btn--pri btn--large" onclick="aller('${suiteApresAchat()}')">Revenir</button>`;
}

/* ---------- étape 4 : les exercices ---------- */
/* Un seul moteur pour les familles à choix : une série de questions, jouées jusqu'à la bonne ;
   chaque mauvais choix dit pourquoi ; la place de la bonne est tirée au hasard (leçon de la
   boucle de l'étape 1). Le contenu : build/contenu/toronto/exercices.py. */
const FAMILLES = [
  ['reponses', 'Ce qu’on me répond', 'Une vraie réponse, dite vite : que veut-elle dire ?'],
  ['allergie', 'L’allergie', 'Comprendre la réponse, et savoir quand ne pas commander'],
  ['nombres', 'Les prix et les heures', 'Fourteen ou forty ? Quarter past ou quarter to ?'],
  ['totaux', 'Le total à payer', 'Le prix entendu, la taxe, le pourboire : combien, vraiment ?'],
  ['chemins', 'Où je vais', 'Suivez les indications sur le plan'],
  ['entendre', 'Je l’entends, je le trouve', 'Un mot entendu : son sens'],
  ['souvenir', 'Je me souviens', 'Le sens en français : le mot anglais'],
  ['pieges', 'Les faux amis', 'Le piège, dans sa phrase'],
  ['dire', 'Je le dis', 'La situation en français ; vous le dites en anglais'],
];
const melange = a => { const b = [...a]; for (let i = b.length - 1; i > 0; i--) { const j = Math.floor(Math.random() * (i + 1)); [b[i], b[j]] = [b[j], b[i]]; } return b; };
const dollars = v => v.toFixed(2).replace('.', ',') + ' $';
function vueExos(){
  const ex = S.exos || {};
  app.innerHTML = `${retour('accueil', 'Accueil')}<p class="surtitre">S'exercer</p><h1>Les exercices</h1>
    <p>Des séries courtes, à reprendre autant de fois qu'il faut : chaque série tire d'autres questions.</p>
    <ul class="etapes-j">${FAMILLES.map(([k, t, d], i) => `<li class="${ex[k] ? 'fait' : ''}"><button onclick="aller(${k === 'pieges' ? "'pieges'" : `'exos/${k}'`})">
      <span class="num">${ex[k] ? '✓' : i + 1}</span><span><b>${E(t)}</b><span class="d">${E(d)}</span></span>${ex[k] ? `<span class="etat">${E(ex[k])}</span>` : ''}</button></li>`).join('')}</ul>`;
}
function itemsDe(fam){
  const X = D.exos;
  if (fam === 'reponses') return melange(X.reponses.map((it, k) => ({k, it}))).slice(0, 8).map(({k, it}) => ({
    son: `exos/rep-${k}.mp3`, qui: D.gens[it.qui], haut: `<p class="consigne"><b>${E(it.lieu)}.</b> ${E(it.ctx)}</p>`, q: 'Que vous répond-on ?', en: it.en, choix: it.choix}));
  if (fam === 'nombres') return melange(X.nombres.map((it, k) => ({k, it}))).slice(0, 8).map(({k, it}) => ({
    son: `exos/nb-${k}.mp3`, q: 'Qu’entendez-vous ?', en: it.en, choix: it.choix}));
  if (fam === 'totaux') return melange(X.totaux.map((it, k) => ({k, it}))).map(({k, it}) => ({
    son: `exos/tot-${k}.mp3`, haut: `<p class="consigne"><b>${E(it.lieu)}.</b> ${E(it.ctx)}</p>`, q: 'Combien payez-vous en tout ?',
    en: it.en, apresTexte: it.calcul, choix: it.choix}));
  // Tour 2 : trois réponses tirées sur les six du saumon (les quatre cases y sont), plus le marché ;
  // la série change à chaque fois, et la dernière ne se déduit plus des deux autres.
  if (fam === 'allergie') { const tous = X.allergie.items.map((it, k) => ({k, it}));
    const saumon = melange(tous.filter(x => x.it.qui === 'ada')).slice(0, 3), autres = melange(tous.filter(x => x.it.qui !== 'ada')).slice(0, 1);
    return melange([...saumon, ...autres]).map(({k, it}) => ({
    son: `exos/all-${k}.mp3`, qui: D.gens[it.qui], haut: `<p class="consigne">${E(it.ctx)}</p>`, q: 'Que vous répond-on ?',
    en: it.en, apresTexte: it.apres, choix: it.choix})); }
  if (fam === 'chemins') return melange(X.chemins.map((it, k) => ({k, it}))).map(({k, it}) => {
    // Les quatre points du carré (2 ou 3 coins de rue) × (gauche ou droite) ; les lettres tirées au hasard.
    const pts = [[it.blocs, it.tourner], [it.blocs, it.tourner === 'gauche' ? 'droite' : 'gauche'],
                 [5 - it.blocs, it.tourner], [5 - it.blocs, it.tourner === 'gauche' ? 'droite' : 'gauche']];
    const lettres = melange(['A', 'B', 'C', 'D']);
    const retro = ['', `${it.blocs} coins de rue, oui ; mais on tourne à ${it.tourner}.`, `On tourne bien à ${it.tourner} ; mais après ${it.blocs} coins de rue.`, `${it.blocs} coins de rue, puis à ${it.tourner}.`];
    return {son: `exos/ch-${k}.mp3`, plan: pts.map((p, i) => [...p, lettres[i]]), q: 'Où arrivez-vous ?', en: it.en,
      choix: pts.map((p, i) => [`Le point ${lettres[i]}`, i ? retro[i] : null])};
  });
  const hors = new Set(D.exos.horsSerie), proche = (a, b) => D.exos.proches.some(g => g.includes(a) && g.includes(b));
  // Tour 2 : un faux ami ne se montre jamais seul (règle de l'hôtel) — il vit dans sa phrase, série des faux amis.
  const ids = Object.keys(D.mots).filter(id => !/[?!]/.test(D.mots[id].en) && !hors.has(id) && !String(D.mots[id].note).startsWith('PIÈGE'));
  if (fam === 'entendre' || fam === 'souvenir') return melange(ids).slice(0, 8).map(id => {
    const m = D.mots[id], voisins = melange(ids.filter(x => x !== id && D.mots[x].p === m.p && !proche(x, id))).slice(0, 3);
    const lib = x => fam === 'entendre' ? D.mots[x].fr : D.mots[x].en;
    return {son: 'mots/' + id + '.mp3', q: fam === 'entendre' ? 'Que veut dire le mot ?' : 'Comment le dit-on en anglais ?', apres: fam === 'souvenir',
      haut: fam === 'souvenir' ? `<div class="carte"><p style="font-size:19px;font-weight:800;margin:0">${E(m.fr)}</p></div>` : '',
      en: m.en, enChoix: fam === 'souvenir',
      choix: [[lib(id), null], ...voisins.map(x => [lib(x), fam === 'entendre' ? `« ${D.mots[x].en} » : ${D.mots[x].fr}.` : `${D.mots[x].en} veut dire : ${D.mots[x].fr}.`])]};
  });
  return [];
}
function planChemin(pts){
  // Le petit plan : une grille de rues ; l'étoile au départ, face au nord ; quatre points lettrés.
  const X = c => 30 + c * 40, Y = l => 20 + l * 40, x0 = 3, y0 = 5;
  let rues = ''; for (let i = 0; i <= 6; i++) rues += `<line x1="${X(i)}" y1="${Y(0)}" x2="${X(i)}" y2="${Y(5)}" class="rue-g"/><line x1="${X(0)}" y1="${Y(i < 6 ? i : 5)}" x2="${X(6)}" y2="${Y(i < 6 ? i : 5)}" class="rue-g"/>`;
  const marques = pts.map(([b, t, L]) => { const x = X(x0 + (t === 'gauche' ? -1 : 1)), y = Y(y0 - b);
    return `<g><circle cx="${x}" cy="${y}" r="13" fill="#fff" stroke="#7A3B1D" stroke-width="2.5"/><text x="${x}" y="${y + 5}" text-anchor="middle" class="lettre">${L}</text></g>`; }).join('');
  return `<svg class="mini-plan" viewBox="0 0 300 240" role="img" aria-label="Petit plan : vous êtes à l'étoile, face au nord ; quatre points A, B, C, D">${rues}
    <text x="${X(x0)}" y="14" text-anchor="middle" class="nord">N ↑</text>${marques}
    <polygon points="${X(x0)},${Y(y0) - 12} ${X(x0) + 4},${Y(y0) - 3} ${X(x0) + 12},${Y(y0) - 3} ${X(x0) + 6},${Y(y0) + 3} ${X(x0) + 8},${Y(y0) + 12} ${X(x0)},${Y(y0) + 7} ${X(x0) - 8},${Y(y0) + 12} ${X(x0) - 6},${Y(y0) + 3} ${X(x0) - 12},${Y(y0) - 3} ${X(x0) - 4},${Y(y0) - 3}" fill="#C8102E"/></svg>`;
}
function vueFamille(fam){
  const nom = (FAMILLES.find(f => f[0] === fam) || [])[1]; if (!nom) return vueExos();
  if (fam === 'dire') return serieDire();
  if (fam === 'allergie' && !vueFamille.regleVue) {
    app.innerHTML = `${retour('exos', 'Les exercices')}<p class="surtitre">L'allergie</p><h1>Avant de commencer</h1>
      <div class="regle"><b>La règle.</b> ${E(D.exos.allergie.regle)}</div>
      <p>Les noix portent souvent leur nom : <b lang="en">pecans</b> (pacanes), <b lang="en">almonds</b> (amandes), <b lang="en">walnuts</b> (noix de Grenoble), <b lang="en">hazelnuts</b> (noisettes). Les arachides, ce sont les <b lang="en">peanuts</b>.</p>
      <p>Quatre réponses de serveuse ou de marchand. Comprenez ce qu'on vous dit ; la décision s'affiche ensuite. Au marché, c'est vous qui décidez.</p>
      <button class="btn btn--pri btn--large" id="go">Commencer</button>`;
    $('#go').onclick = () => { vueFamille.regleVue = true; vueFamille(fam); vueFamille.regleVue = false; }; return;
  }
  const items = itemsDe(fam); let n = 0, premiers = 0;
  function tour(){
    if (n >= items.length) {
      if (!S.exos) S.exos = {}; S.exos[fam] = `${premiers} sur ${items.length}`; sauver();
      app.innerHTML = `${retour('exos', 'Les exercices')}<h1>${E(nom)}</h1><div class="retro ok">✓ ${items.length} questions, ${premiers} du premier coup.</div>
        <button class="btn btn--pri btn--large" onclick="rendre()">Une autre série</button>
        <button class="btn btn--large" style="margin-top:8px" onclick="aller('exos')">Les exercices</button>`; return; }
    const it = items[n], o = ordre(it.choix.length, Math.floor(Math.random() * 9973)).filter(i => i !== 0);
    o.splice(Math.floor(Math.random() * it.choix.length), 0, 0);
    let erreurs = 0, fini = false;
    app.innerHTML = `${retour('exos', 'Les exercices')}<p class="surtitre">${E(nom)} · ${n + 1} sur ${items.length}</p>
      <div class="progres"><i style="width:${100 * n / items.length}%"></i></div>${it.haut || ''}
      ${it.qui ? `<div class="scene-tete"><div><b>${E(it.qui.nom)}</b><div class="muted" style="font-size:14px">${E(it.qui.role)}</div></div></div>` : ''}
      ${it.plan ? planChemin(it.plan) : ''}
      <h2 style="margin-top:6px">${E(it.q)}</h2>
      ${it.apres ? '' : `<div class="gros-son"><button class="btn btn--son" aria-label="Écouter" id="rejouer">${ICO.son}</button></div>`}
      <div class="choix">${o.map(i => `<button data-i="${i}" ${it.enChoix ? 'lang="en"' : ''}>${E(it.choix[i][0])}</button>`).join('')}</div><div id="r" aria-live="polite"></div>`;
    if ($('#rejouer')) { $('#rejouer').onclick = () => jouer(it.son); setTimeout(() => jouer(it.son), 250); }
    app.querySelectorAll('.choix button').forEach(b => b.onclick = () => {
      if (fini || b.disabled) return; const i = +b.dataset.i;
      if (i === 0) { fini = true; if (!erreurs) premiers++; b.classList.add('juste');
        $('#r').innerHTML = `<div class="retro ok">✓ « ${E(it.en)} »${it.apresTexte ? `<br>${E(it.apresTexte)}` : ''}</div>`; if (it.apres || it.plan) jouer(it.son);
        const s2 = document.createElement('button'); s2.className = 'btn btn--pri btn--large'; s2.textContent = 'Suivant'; s2.onclick = () => { n++; tour(); }; $('#r').appendChild(s2);
      } else { erreurs++; b.classList.add('faux'); b.disabled = true; $('#r').innerHTML = `<div class="retro no">${E(it.choix[i][1])} Essayez encore.</div>`; }
    });
  }
  tour();
}
function serieDire(){
  const items = melange(D.exos.dire.map((it, k) => ({...it, son: `exos/dire-${k}.mp3`}))).slice(0, 6);
  let n = 0, dites = 0, comprises = 0;
  function tour(){
    if (n >= items.length) {
      if (!S.exos) S.exos = {}; S.exos.dire = `${dites} sur ${items.length}`; sauver();
      app.innerHTML = `${retour('exos', 'Les exercices')}<h1>Je le dis</h1><div class="retro ok">✓ ${dites} phrase${dites > 1 ? 's' : ''} dite${dites > 1 ? 's' : ''} sur ${items.length}${Reco ? `, dont ${comprises} comprise${comprises > 1 ? 's' : ''} au micro` : ''}.</div>
        <button class="btn btn--pri btn--large" onclick="rendre()">Une autre série</button>
        <button class="btn btn--large" style="margin-top:8px" onclick="aller('exos')">Les exercices</button>`; return; }
    const it = items[n]; let tente = false, essais = 0, modeleVu = false;
    app.innerHTML = `${retour('exos', 'Les exercices')}<p class="surtitre">Je le dis · ${n + 1} sur ${items.length}</p><div class="progres"><i style="width:${100 * n / items.length}%"></i></div>
      <div class="carte"><p class="surtitre">${E(it.lieu)}</p><p style="font-size:19px;font-weight:800;color:var(--text-strong);margin:4px 0 0">${E(it.fr)}</p></div>
      ${Reco ? `<div class="micro"><button class="btn-micro" id="mic" aria-label="Parler">${ICO.micro}</button>
        <div class="muted" id="micEtat" style="font-size:14px">Touchez le micro, dites-le en anglais.</div><div class="entendu" id="entendu"></div></div>` : ''}
      <button class="btn btn--large" id="dit" style="margin:6px 0">C'est dit !</button><div id="r" aria-live="polite"></div>
      <div class="rangee" style="margin-top:10px"><button class="btn" id="modele" disabled>${ICO.son} Le modèle</button>
       <button class="btn btn--pri" id="suite" style="flex:1" disabled>Suivant</button></div>`;
    const zone = $('#r');
    const poserR = h => { zone.querySelectorAll(':scope > :not(.modele-carte)').forEach(y => y.remove()); zone.insertAdjacentHTML('afterbegin', h); };
    const montrer = () => { if (!document.body.contains(zone)) return;
      if (!modeleVu) { modeleVu = true; $('#dit').disabled = true;
        zone.insertAdjacentHTML('beforeend', `<div class="retro info modele-carte"><span class="surtitre">Le modèle</span><div class="phrase-en" lang="en">${E(it.en)}</div></div>`); }
      $('#modele').disabled = false; jouer(it.son); };
    const essaye = () => { if (!tente) { tente = true; dites++; } $('#modele').disabled = false; $('#suite').disabled = false; };
    $('#modele').onclick = montrer; $('#suite').onclick = () => { n++; tour(); };
    $('#dit').onclick = () => { essaye(); montrer(); };
    if (Reco) $('#mic').onclick = () => {
      const mic = $('#mic'); if (recoActive) { arreterMicro(); return; }
      mic.classList.add('ecoute'); mic.innerHTML = ICO.stop; $('#micEtat').textContent = 'Je vous écoute… touchez pour arrêter.';
      ecouterMicro(t => { $('#entendu').textContent = '« ' + t + ' »'; }, final => {
        mic.classList.remove('ecoute'); mic.innerHTML = ICO.micro; $('#micEtat').textContent = 'Touchez le micro pour réessayer.';
        if (!final) { poserR(`<div class="retro info">${rienEntendu('Je n’ai rien entendu. Vérifiez que le micro est permis, ou dites-le et touchez « C’est dit ! ».')}</div>`); return; }
        essais++; const manque = it.cles.filter(c => !trouve(final, c));
        // Une garde ratée (clé vraie sur la phrase vide) : le geste est faux — jamais « Presque », jamais un mot du modèle.
        if (manque.some(c => trouve('', c))) { poserR(`<div class="retro no">${E(it.garde || 'Votre phrase dit le contraire de ce qu’il faut.')} ${essais < 2 && !modeleVu ? 'Réessayez.' : 'Comparez avec le modèle.'}</div>`);
          essaye(); if (essais >= 2) montrer(); else $('#modele').disabled = false; return; }
        if (!manque.length) { if (essais <= 2 && !modeleVu) comprises++; poserR(`<div class="retro ok">✓ Well done! On vous a compris.</div>`); essaye(); setTimeout(montrer, 600); return; }
        poserR(`<div class="retro no">${manque.length <= it.cles.filter(c => !trouve('', c)).length / 2 ? `Presque. Il manque : <b lang="en">${manque.map(c => E(motDuModele(it.en, c))).join(', ')}</b>. ` : 'Je n’ai pas reconnu la phrase. '}${essais < 2 && !modeleVu ? 'Réessayez, sans regarder le modèle.' : 'Comparez avec le modèle.'}</div>`);
        essaye(); if (essais >= 2) montrer(); else $('#modele').disabled = false;
      });
    };
  }
  tour();
}

/* ---------- étape 6 : la poche ---------- */
/* Gardée dans le téléphone, sans réseau : les phrases de chaque lieu avec leur son (celles des
   exercices), ce qu'on peut vous répondre, les urgences, les phrases à montrer en grand, et
   l'aide-mémoire du total à payer. « Préparer pour le voyage » demande une fois chaque fichier :
   le service worker du site (/sw.js) les garde (sons : cache d'abord). Le jeu de rôle, lui,
   a besoin du réseau. Contenu : build/contenu/toronto/poche.py. */
function lignePoche(x, i, montrable){
  return `<div class="ph"><button class="btn btn--son" aria-label="Écouter" onclick="jouer('${x.son}')">${ICO.son}</button>
    <div class="t"><b lang="en">${E(x.en)}</b><span>${E(x.fr)}</span></div>
    ${montrable ? `<button class="btn btn--petit" onclick="montrerPoche('${i}')">Montrer</button>` : ''}</div>`;
}
const POCHE_IDX = {};
function vuePoche(){
  const P = D.poche; let k = 0;
  const idx = x => { const i = 'p' + (k++); POCHE_IDX[i] = x; return i; };
  app.innerHTML = `${retour('accueil', 'Accueil')}<p class="surtitre">Sur place · même sans réseau</p><h1>Ma poche</h1>
    <p class="muted">Les phrases de chaque lieu, avec leur voix. « Montrer » affiche la phrase en grand, pour la tendre à quelqu'un.</p>
    <div class="carte" style="margin:12px 0"><b>Pas de réseau dans le métro ?</b>
      <p class="muted" style="font-size:15px;margin:4px 0 10px">Une fois, avec du wifi : mettez tous les sons dans ce téléphone (environ ${D.poids} Mo).</p>
      <button class="btn btn--pri" id="prep">Préparer pour le voyage</button><div id="prepEtat" class="muted" style="font-size:14px;margin-top:8px"></div></div>
    <details class="rub" open><summary>Ce que ça coûte vraiment <span>$</span></summary><div class="calc">
      <label>Le prix affiché, avant taxe <input id="prix" type="number" inputmode="decimal" min="0" step="0.01" placeholder="25.00"></label>
      <div class="rangee" id="pbs">${[['0', 'Sans pourboire'], ...P.pourboires.flatMap(([lieu, a, b]) => [[String(a), `${a} % · ${lieu.toLowerCase()}`], [String(b), `${b} %`]])]
        .map(([v, t], j) => `<button class="btn btn--petit${j === 0 ? ' btn--pri' : ''}" data-pb="${v}">${E(t)}</button>`).join('')}</div>
      <div id="calcul" class="calcul" aria-live="polite"></div>
      <p class="muted" style="font-size:14px;margin:6px 0 0">En Ontario, la taxe (13 %) s'ajoute à la caisse : le prix affiché ne la comprend pas. Le pourboire se calcule sur le prix <b>avant</b> taxe ; « tip included » veut dire qu'il est déjà compris.</p>
    </div></details>
    <details class="rub"><summary>Urgences <span>${P.urgences.length}</span></summary>${P.urgences.map(x => lignePoche(x, idx(x), true)).join('')}</details>
    <details class="rub"><summary>À montrer <span>${P.montrer.length}</span></summary>${P.montrer.map(x => lignePoche(x, idx(x), true)).join('')}</details>
    ${P.lieux.map(l => `<details class="rub"><summary>${E(l.lieu)} <span>${l.dire.length + l.reponses.length}</span></summary>
      ${l.dire.map(x => lignePoche(x, idx(x), true)).join('')}
      ${l.reponses.length ? `<div class="ph ph-tete"><b>Ce qu'on peut vous répondre</b></div>${l.reponses.map(x => lignePoche(x, idx(x), false)).join('')}` : ''}</details>`).join('')}`;
  $('#prep').onclick = preparer;
  let pb = 0;
  const calculer = () => {
    const v = parseFloat(String($('#prix').value).replace(',', '.'));
    if (!(v > 0)) { $('#calcul').innerHTML = ''; return; }
    const t = Math.round(v * 13) / 100, p = Math.round(v * pb) / 100;
    $('#calcul').innerHTML = `${dollars(v)} + ${dollars(t)} de taxe${pb ? ` + ${dollars(p)} de pourboire (${pb} %)` : ''} = <b>${dollars(v + t + p)}</b>`;
  };
  $('#prix').oninput = calculer;
  $('#pbs').onclick = e => { const b = e.target.closest('[data-pb]'); if (!b) return; pb = +b.dataset.pb;
    $('#pbs').querySelectorAll('button').forEach(x => x.classList.toggle('btn--pri', x === b)); calculer(); };
}
function montrerPoche(i){
  const x = POCHE_IDX[i]; if (!x) return;
  const v = document.createElement('div'); v.className = 'montrer'; v.setAttribute('role', 'dialog');
  v.innerHTML = `<button class="btn fermer">Fermer</button><div class="grand" lang="en">${E(x.en)}</div><div class="petit">${E(x.fr)}</div>
    <button class="btn btn--son" style="margin-top:22px;width:72px;height:72px;border-radius:50%" aria-label="Écouter">${ICO.son}</button>`;
  document.body.appendChild(v);
  v.querySelector('.fermer').onclick = () => v.remove();
  v.querySelector('.btn--son').onclick = () => jouer(x.son);
}
async function preparer(){
  const bouton = $('#prep'), txt = $('#prepEtat'); bouton.disabled = true;
  if ('serviceWorker' in navigator) { try { await navigator.serviceWorker.register('/sw.js'); await navigator.serviceWorker.ready; } catch(e) {} }
  const urls = D.sons.map(f => BASE + 'sons/' + f + '?v=' + D.v);
  Object.entries(D.mots).forEach(([id, m]) => m.img === 'croquis' && urls.push(BASE + 'croquis/' + id + '.jpg?v=' + D.v));
  D.semaine.forEach(l => l.carte && urls.push(BASE + 'cartes/' + l.id + '.jpg?v=' + D.v));
  urls.push(location.pathname);
  // Ce que la page a chargé avant que le service worker ne la contrôle (feuilles, polices, icônes) :
  // sans eux, la page hors ligne s'affiche sans ses styles (leçon de Compostelle, 25 sept. 2026).
  performance.getEntriesByType('resource').forEach(r => { try { const u = new URL(r.name);
    if (u.origin === location.origin && !u.pathname.startsWith('/api/') && !urls.includes(u.pathname + u.search)) urls.push(u.pathname + u.search); } catch(e) {} });
  ['/assets/design-system/styles.css', '/assets/design-system/marque-francis.css', '/assets/design-system/marque-francis-favicon.svg']
    .forEach(u => urls.includes(u) || urls.push(u));
  let fait = 0, echec = 0;
  const un = async u => { try { const r = await fetch(u, {cache:'reload'}); if (!r.ok) echec++; } catch(e) { echec++; } fait++; txt.textContent = `${fait} / ${urls.length} fichiers…`; };
  for (let i = 0; i < urls.length; i += 6) await Promise.all(urls.slice(i, i + 6).map(un));
  const controle = navigator.serviceWorker && navigator.serviceWorker.controller;
  txt.innerHTML = echec ? `${echec} fichiers n'ont pas pu être pris. Réessayez avec un meilleur réseau.` :
    (controle ? '✓ Tout est dans le téléphone. Bon voyage !' : '✓ Téléchargé. Rouvrez la page une fois, avec du réseau, pour que le téléphone la garde aussi.');
  bouton.disabled = false;
}

/* ---------- étape 7 : le pilote — « Donner mon avis » ---------- */
/* L'avis part par courriel : rien n'est gardé dans l'application (même formule que Compostelle). */
const AVIS_COURRIEL = 'support@edufrancis.ca';
function vueAvis(){
  let ici = 'accueil'; try { ici = decodeURIComponent((sessionStorage.getItem('toronto:vu') || '').replace(/^#/, '')) || 'accueil'; } catch(e) {}
  const corps = `Écran où j'étais : ${ici}\nNavigateur : ${navigator.userAgent.slice(0, 120)}\n\n`
    + `1. Ce qui est clair :\n\n2. Ce qui est confus ou bloque :\n\n3. L'anglais (une phrase, un mot, une voix qui sonne faux) :\n\n4. Ce qui manque pour un vrai voyage à Toronto :\n\n5. Combien de temps a pris une séance, une série, une situation ?\n`;
  const sujet = 'Toronto — mon avis';
  app.innerHTML = `${retour('accueil', 'Accueil')}<p class="surtitre">Essai avant le lancement</p><h1>Donner mon avis</h1>
    <p>Merci d'essayer « Une semaine à Toronto ». Tout nous aide : une consigne confuse, une phrase anglaise qui ne se dit pas au Canada,
    une voix qui sonne faux, un bouton qui ne répond pas, un bilan injuste.</p>
    <div class="carte"><h3 style="margin-top:0">Ce qui nous aide le plus</h3><ul style="margin:0;padding-left:20px">
      <li><b>Si vous partez</b> : les situations ressemblent-elles à ce que vous avez vécu ? Qu'est-ce qui vous a servi, ou manqué ?</li>
      <li><b>Si l'anglais est votre langue</b> : les phrases sont-elles justes et naturelles au Canada ? Notez la phrase et l'écran.</li>
      <li><b>Tous</b> : où avez-vous hésité ? Le bilan de la semaine jouée était-il juste ?</li></ul></div>
    <a class="btn btn--pri btn--large" href="mailto:${AVIS_COURRIEL}?subject=${encodeURIComponent(sujet)}&body=${encodeURIComponent(corps)}">Écrire mon avis (logiciel de courriel)</a>
    <a class="btn btn--large" style="margin-top:8px" target="_blank" rel="noopener"
       href="https://mail.google.com/mail/?view=cm&fs=1&to=${encodeURIComponent(AVIS_COURRIEL)}&su=${encodeURIComponent(sujet)}&body=${encodeURIComponent(corps)}">Écrire mon avis dans Gmail</a>
    <details class="rub" style="margin-top:10px"><summary>Rien ne s'ouvre ? Copiez le texte <span>à coller</span></summary>
      <div style="padding:0 14px 14px"><textarea id="avisTexte" readonly class="carte-postale-txt" style="min-height:220px;font-size:14px">${E(corps)}</textarea>
      <button class="btn" id="avisCopier" style="margin-top:8px">Copier le texte</button>
      <p class="muted" style="font-size:14px;margin:8px 0 0">Puis envoyez-le à <b>${AVIS_COURRIEL}</b>, avec l'objet « ${sujet} ».</p></div></details>`;
  $('#avisCopier').onclick = () => { const t = $('#avisTexte'); t.select();
    (navigator.clipboard ? navigator.clipboard.writeText(t.value) : Promise.reject()).catch(() => document.execCommand('copy'))
      .finally(() => { $('#avisCopier').textContent = 'Copié ✓'; }); };
}

/* ---------- étape 8 : vos renseignements personnels (Loi 25) ---------- */
/* Texte : build/contenu/toronto/confidentialite.py. La durée de conservation des codes se relit au
   serveur (/api/pelerins/offre) : la page ne promet que ce qui a lieu. */
function vueConfidentialite(){
  const C = D.confid;
  const resp = [C.responsable[0], C.responsable[1]].filter(Boolean).map(E).join(', ');
  const rendu = cons => {
    const duree = `effacés ${cons} jours après la fin de votre accès (et un code jamais payé, après 7 jours)`;
    app.innerHTML = `${retour('accueil', 'Accueil')}
    <p class="surtitre">Loi 25 · mise à jour le ${E(C.maj)}</p><h1>Vos renseignements personnels</h1>
    <div class="carte cf-bref"><h3 style="margin-top:0">En bref</h3><ul>${C.bref.map(t => `<li>${t}</li>`).join('')}</ul></div>
    <h2>Ce que nous savons de vous, et où c'est</h2>
    ${C.donnees.map(([q, ou, qui, dur]) => `<div class="carte cf-ligne"><b>${E(q)}</b>
      <dl><dt>Où</dt><dd>${E(ou)}</dd><dt>Qui le voit</dt><dd>${E(qui)}</dd><dt>Combien de temps</dt><dd>${E(dur).replace('{conservation}', duree)}</dd></dl></div>`).join('')}
    <h2>Ce qui sort du Québec</h2>
    <p>Certains services sont situés à l'extérieur du Québec. Voici lesquels, et ce qu'ils reçoivent :</p>
    <div class="carte">${C.hors.map(([qui, quoi, ou]) => `<p class="cf-hors"><b>${E(qui)}</b> — ${E(quoi)} <span class="muted">(${E(ou)})</span></p>`).join('')}</div>
    <p>Vous pouvez éviter l'envoi de votre voix : n'ouvrez pas le micro ; dites les phrases à voix haute et touchez « C'est dit ! », ou écrivez-les. Vous pouvez éviter l'envoi à Anthropic et à Azure : ne jouez pas la semaine avec l'assistance. Tout le reste de l'application fonctionne sans.</p>
    <h2>Ce que nous ne faisons pas</h2><ul>${C.nefait.map(t => `<li>${E(t)}</li>`).join('')}</ul>
    <h2>Vos droits</h2>
    <p>Vous pouvez demander à savoir ce que nous détenons à votre sujet, le faire corriger ou effacer. Comme nous ne savons pas qui vous êtes, donnez-nous votre <b>code d'accès</b> : c'est tout ce que nous avons.
    Ce qui est dans votre téléphone, vous l'effacez vous-même : <a href="#reglages">Réglages</a> → tout recommencer, ou vider les données du navigateur.</p>
    <p>Pour toute question ou demande : <a href="mailto:${E(C.courriel)}">${E(C.courriel)}</a>. Responsable de la protection des renseignements personnels : ${resp}.</p>
    <p class="muted" style="font-size:14px">Si notre réponse ne vous satisfait pas, vous pouvez vous adresser à la Commission d'accès à l'information du Québec.</p>
    <h2>En cas d'incident</h2>
    <p>Si un incident touchait des renseignements que nous détenons (vos codes), nous le consignerions et avertirions la Commission d'accès à l'information et les personnes concernées lorsque la loi l'exige.</p>
    <p class="muted" style="font-size:14px">Conditions de vente : <a href="/conditions-de-vente.html" target="_blank" rel="noopener">conditions-de-vente.html</a>.</p>`;
  };
  rendu('365'); offreServeur().then(o => { if (o && o.conservation && location.hash === '#confidentialite') rendu(String(o.conservation)); });
}

/* ---------- réglages ---------- */
function vueReglages(){
  app.innerHTML = `${retour('accueil', 'Accueil')}<h1>Réglages</h1>
    <label class="aide-bascule"><input type="checkbox" id="lent" ${S.lent ? 'checked' : ''}> Les voix plus lentes (sauf au test)</label>
    <label class="aide-bascule"><input type="checkbox" id="aide" ${S.aide ? 'checked' : ''}> Montrer le sens en français dès l'arrivée</label>
    <p class="muted" style="font-size:14.5px">Votre progression reste dans ce téléphone : rien n'est envoyé.</p>
    <button class="btn" id="raz">Tout recommencer</button>`;
  $('#lent').onchange = e => { S.lent = e.target.checked; sauver(); };
  $('#aide').onchange = e => { S.aide = e.target.checked; sauver(); };
  $('#raz').onclick = () => { if (confirm('Effacer votre progression dans ce téléphone ?')) { S = {lent:false, aide:false, prep:{}}; sauver(); aller('accueil'); } };
}

// Le contrôle par programme (leçon de Compostelle : jouer chaque temps trouve ce qu'aucune relecture ne voit).
window.__toronto = {D, S: () => S, trouve, plat, extraits: () => D.sons, itemsDe,
  controle: () => [...D.controle.refus.filter(([c, t]) => trouve(t, c)).map(([, t]) => 'accepte à tort : ' + t),
                   ...D.controle.accepte.filter(([c, t]) => !trouve(t, c)).map(([, t]) => 'refuse à tort : ' + t)]};
rendre();
if ('serviceWorker' in navigator) window.addEventListener('load', () => navigator.serviceWorker.register('/sw.js').catch(() => {}));
</script>
</body>
</html>
"""


if __name__ == "__main__":
    main()
